# Repository guide

This repository documents Jotform's hosted MCP services and packages integrations for AI clients. The user journey is: discover a capability, understand the MCP service, choose an integration, connect an account, and make a first request.

## Find the right file

| Task | Start here |
| --- | --- |
| Understand the user journey | `README.md` |
| Explain MCP services, tools, or account access | `docs/mcp/README.md`, `docs/mcp/endpoints.md`, `docs/mcp/tools.md`, `docs/mcp/authentication.md` |
| Find available integrations | `integrations/README.md` |
| Change Claude plugin behavior | `integrations/claude/jotform/skills/` |
| Change Claude connections or skill references | `integrations/claude/jotform/.claude-plugin/plugin.json` (`mcpServers` and `skills`) |
| Change Claude package metadata or catalog | `integrations/claude/jotform/.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json` |
| Change Gemini connections or context | `gemini-extension.json` and `JOTFORM.md` |
| Update setup instructions | `docs/*-setup.md`, indexed in `docs/README.md` |
| Add a client package | `docs/plugin-development.md` |
| Prepare a release | `docs/releasing.md` |

## Keep the boundaries clear

- Maintain setup steps in one guide per client; indexes link to those guides.
- Public documentation describes what a user can do and how to do it. Agent behavior belongs in skills and context files.
- Keep product and service claims aligned with [Jotform MCP](https://www.jotform.com/mcp/) and the [developer reference](https://www.jotform.com/developers/mcp/). Use the relevant MCP implementation to verify gaps; document published services. Flag conflicting claims instead of guessing.
- Package manifests are the source for configured endpoints. Keep `docs/mcp/endpoints.md` aligned with them and Jotform's documented standard address. Direct setup examples use `https://mcp.jotform.com`; the Gemini package's `/default` route selects the same service.
- Preserve the root Gemini manifest and its declared context file; direct repository installation depends on that layout.
- OpenAI currently has connection guides but no plugin package in this repository. Describe only the distribution routes that exist.
- Keep installed packages self-contained. Preserve plugin names and service URLs unless the task explicitly changes them.
- Keep Claude MCP connections inline in `plugin.json` and list each bundled skill directory in its `skills` array. Update that list when adding or removing a skill.

## Verify changes

Run `python3 scripts/validate.py` and `git diff --check`. For Claude changes, also run `claude plugin validate .` and `claude plugin validate ./integrations/claude/jotform`. Follow the affected behavior checks in `docs/plugin-development.md`; record live checks separately from offline validation.
