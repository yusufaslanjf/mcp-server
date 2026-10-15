# Plugin development

This repository contains service documentation and client packages for Jotform's hosted MCP services. Start with the file map below when changing a package or its documentation.

## Repository layout

| Path | Purpose |
| --- | --- |
| `README.md` | Entry point for users: choose an integration and find its setup guide. |
| `AGENTS.md` | File map and verification entry point for repository agents. |
| `docs/mcp/` | Service overview, endpoints, tools, authentication, and access. |
| `integrations/README.md` | Catalog of available packages and connection routes. |
| `.claude-plugin/marketplace.json` | Claude marketplace catalog. |
| `integrations/claude/` | Claude index and the self-contained `jotform/` plugin. |
| `integrations/claude/jotform/.claude-plugin/plugin.json` | Plugin identity, explicit skill directory references, and inline MCP connections. |
| `integrations/openai/` | ChatGPT and Codex connection routes and package status. |
| `integrations/gemini/` | Gemini CLI index linking to the root extension files. |
| `gemini-extension.json` | Gemini extension manifest and MCP connection. |
| `JOTFORM.md` | Context loaded by the Gemini extension. |
| `docs/*-setup.md` | Installation, account connection, first use, and troubleshooting for each client. |
| `scripts/validate.py` | Offline checks for documentation, manifests, and catalog paths. |

## Make a change

- **Skills:** edit `integrations/claude/jotform/skills/<skill-name>/SKILL.md`. Keep supporting references inside that skill directory. When adding or removing a skill, update the plugin manifest's `skills` array.
- **Connections:** edit `mcpServers` in the Claude plugin manifest or Gemini extension manifest, the endpoint reference, and affected setup examples.
- **New Claude plugin:** add `integrations/claude/<plugin-name>/`, register it in the root marketplace, and link it from the Claude index. Keep the marketplace entry name and plugin manifest name identical.
- **Documentation:** put installation steps in `docs/`, package capabilities and examples in the package README, and agent behavior in skill or context files.

The root Claude marketplace is a catalog pointing to the plugin folder. The Gemini manifest and context stay at the repository root so the repository URL works as an extension installation source. See the [Claude marketplace guide](https://code.claude.com/docs/en/plugin-marketplaces) and [Gemini extension reference](https://geminicli.com/docs/extensions/reference/).

The Claude plugin manifest declares its MCP servers inline and lists each skill directory. Skill paths resolve from the plugin root (`integrations/claude/jotform/`), so `./skills/jotform-forms` points to that skill's directory. See the [Claude manifest reference](https://code.claude.com/docs/en/plugins-reference).

Each installed package must include its own runtime resources. Keep shared source inside a package or copy it into each distribution when packaging; avoid links to files outside the installed package.

## Keep service documentation current

Use [Jotform MCP](https://www.jotform.com/mcp/) for the product overview and directory connection paths. Use the [standard MCP reference](https://www.jotform.com/developers/mcp/?tab=mcp) and [MCP Apps reference](https://www.jotform.com/developers/mcp/?tab=mcp-app) for service addresses and capabilities.

When those pages leave a gap, verify the relevant MCP implementation and the connected server's `tools/list` response. Keep tool descriptions tied to their endpoint. Package manifests identify the endpoints each distribution uses; the standard public address and its `/default` route both select the standard service. Report conflicting public claims for correction rather than copying them into setup guides.

## Validate

From the repository root, run the offline checks with Python 3.10 or newer:

```sh
python3 scripts/validate.py
git diff --check
```

The validator checks local Markdown links and anchors, JSON files and examples, Claude catalog paths and identities, inline MCP connections, declared skill directories, Gemini context, skill metadata, and endpoint documentation. The same command runs in GitHub Actions.

With Claude Code installed, also validate its catalog and package:

```sh
claude plugin validate .
claude plugin validate ./integrations/claude/jotform
```

These checks are offline. Verify account connection and tool behavior in the client for changes that affect them.

## Verify affected behavior

Use a test account for the scenarios affected by your change:

| Scenario | Expected result |
| --- | --- |
| Connect an account | The client shows the Jotform connection and available tools. |
| Find forms | Results match the connected account. |
| Create a feedback form | The returned preview or link opens the completed form. |
| Add an existing form to a portal | The app contains the original form. |
| Prepare a Sign draft | The requested draft is available for review. |
| Follow an operation that is processing | The existing operation reaches a final state without duplicate creation. |

Record the client version, scenarios run, and results in the pull request. Identify any checks that remain untested.

## Release

Follow the [release guide](releasing.md) for versioning, package boundaries, and platform distribution.

[Back to the repository overview](../README.md)
