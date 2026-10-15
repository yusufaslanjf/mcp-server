#!/usr/bin/env python3
"""Validate repository documentation and package wiring without network access."""

import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
IGNORED = {".git", "__pycache__", "node_modules", ".venv"}
FENCES = re.compile(r"^```[^\n]*\n.*?^```[ \t]*$", re.M | re.S)
LINKS = re.compile(r"!?\[[^\n]*?\]\(([^\s)]+)(?:\s+\"[^\"]*\")?\)")
REPO_URL = "https://github.com/jotform/mcp-server/blob/master/"
STANDARD_MCP_URL = "https://mcp.jotform.com"
MCP_URLS = re.compile(r"https://mcp\.jotform\.com(?:/[\w/-]*)?")
errors = []


def check(condition, message):
    if not condition:
        errors.append(message)


def label(path):
    return str(path.relative_to(ROOT))


def read_json(path):
    try:
        return json.loads(path.read_text())
    except (OSError, ValueError) as exc:
        errors.append(f"{label(path)}: {exc}")
        return {}


def anchors(content):
    result = set()
    for heading in re.findall(r"^#{1,6}\s+(.+?)\s*#*\s*$", FENCES.sub("", content), re.M):
        slug = re.sub(r"[^\w\- ]", "", heading.lower()).replace(" ", "-")
        anchor, suffix = slug, 0
        while anchor in result:
            suffix += 1
            anchor = f"{slug}-{suffix}"
        result.add(anchor)
    return result


def local_path(base, value):
    path = (base / value).resolve()
    if not path.is_relative_to(ROOT):
        errors.append(f"Path leaves repository: {value}")
        return None
    return path


def main():
    files = [p for p in ROOT.rglob("*") if p.is_file()
             and not IGNORED.intersection(p.relative_to(ROOT).parts)]
    documents = {p: p.read_text() for p in files if p.suffix == ".md"}
    json_files = {p: read_json(p) for p in files if p.suffix == ".json"}
    link_count = 0

    for path, content in documents.items():
        for example in re.findall(r"^```json\s*\n(.*?)^```", content, re.M | re.S):
            try:
                json.loads(example)
            except ValueError as exc:
                errors.append(f"{label(path)}: invalid JSON example: {exc}")
        for href in LINKS.findall(FENCES.sub("", content)):
            base = path.parent
            if href.startswith(REPO_URL):
                href, base = href[len(REPO_URL):], ROOT
            url = urlsplit(href)
            if url.scheme or url.netloc:
                continue
            target = local_path(base, unquote(url.path)) if url.path else path
            if target is None:
                continue
            link_count += 1
            check(target.exists(), f"{label(path)}: missing link target {href}")
            if url.fragment and target in documents:
                check(unquote(url.fragment) in anchors(documents[target]),
                      f"{label(path)}: missing anchor {href}")

    marketplace = json_files.get(ROOT / ".claude-plugin/marketplace.json", {})
    entries = marketplace.get("plugins", [])
    check(bool(entries), "Claude marketplace has no plugins")
    names = set()
    endpoints = set()
    for entry in entries:
        name, source = entry.get("name"), entry.get("source")
        check(name and name not in names, f"Missing or duplicate plugin name: {name}")
        names.add(name)
        if not isinstance(source, str) or not source.startswith("./"):
            errors.append(f"{name}: expected a repository-relative plugin source")
            continue
        package = local_path(ROOT, source)
        if package is None:
            continue
        manifest = json_files.get(package / ".claude-plugin/plugin.json", {})
        check(manifest.get("name") == name, f"{source}: manifest name must match {name}")
        check(bool(manifest.get("version")), f"{source}: package version missing")
        check((package / "README.md").is_file(), f"{source}: package README missing")
        config = manifest.get("mcpServers", {})
        if not isinstance(config, dict) or not config:
            errors.append(f"{source}: inline mcpServers configuration missing or invalid")
            config = {}
        check(not (package / ".mcp.json").exists(),
              f"{source}: keep MCP connections in plugin.json, not a separate .mcp.json")
        for server, settings in config.items():
            if not isinstance(settings, dict):
                errors.append(f"{source}: {server} configuration must be an object")
                continue
            url = settings.get("url", "")
            check(settings.get("type") == "http" and url.startswith("https://"),
                  f"{source}: {server} must have an HTTPS HTTP configuration")
            if url:
                endpoints.add(url)
        skill_paths = manifest.get("skills", [])
        if not isinstance(skill_paths, list) or not skill_paths:
            errors.append(f"{source}: skills must list each bundled skill directory")
            skill_paths = []
        declared_skills = set()
        for value in skill_paths:
            if not isinstance(value, str) or not value.startswith("./"):
                errors.append(f"{source}: invalid skill directory reference: {value}")
                continue
            directory = local_path(package, value)
            if directory is None:
                continue
            if not directory.is_relative_to(package):
                errors.append(f"{source}: skill directory leaves plugin: {value}")
                continue
            skill = directory / "SKILL.md"
            check(skill.is_file(), f"{source}: skill directory has no SKILL.md: {value}")
            check(skill not in declared_skills, f"{source}: duplicate skill reference: {value}")
            declared_skills.add(skill)
        packaged_skills = set(package.glob("skills/*/SKILL.md"))
        check(declared_skills == packaged_skills,
              f"{source}: manifest skills must match the bundled skill directories")
        for skill in sorted(packaged_skills):
            content = documents[skill]
            frontmatter = re.match(r"\A---\n(.*?)\n---(?:\n|$)", content, re.S)
            if not frontmatter:
                errors.append(f"{label(skill)}: skill frontmatter missing")
                continue
            for field in ("name", "description"):
                check(re.search(rf"^{field}:\s*\S", frontmatter[1], re.M),
                      f"{label(skill)}: {field} missing")

    gemini = json_files.get(ROOT / "gemini-extension.json", {})
    check(bool(gemini.get("name") and gemini.get("version")), "Gemini identity missing")
    context = local_path(ROOT, gemini.get("contextFileName", "GEMINI.md"))
    check(context is not None and context.is_file(), "Gemini context file missing")
    servers = gemini.get("mcpServers", {})
    check(bool(servers), "Gemini MCP configuration missing")
    for server, settings in servers.items():
        url = settings.get("httpUrl", "")
        check(url.startswith("https://"), f"Gemini {server}: HTTPS httpUrl missing")
        if url:
            endpoints.add(url)

    reference = documents.get(ROOT / "docs/mcp/endpoints.md", "")
    expected_endpoints = endpoints | {STANDARD_MCP_URL}
    documented = set(MCP_URLS.findall(reference))
    check(expected_endpoints == documented,
          "Endpoint reference differs from package configurations and standard address: "
          f"{sorted(expected_endpoints ^ documented)}")
    for path, content in documents.items():
        for url in MCP_URLS.findall(content):
            check(url in expected_endpoints,
                  f"{label(path)}: endpoint not in package configurations or standard address: {url}")

    if errors:
        print("Validation failed:\n" + "\n".join(f"- {error}" for error in errors))
        return 1
    print(f"Validated {len(documents)} Markdown files, {link_count} local links, "
          f"{len(json_files)} JSON files, {len(entries)} Claude package, "
          f"Gemini context, and {len(expected_endpoints)} documented endpoint URLs.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
