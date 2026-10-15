# MCP endpoints

For a standard connection, use `https://mcp.jotform.com`, the address in [Jotform's MCP reference](https://www.jotform.com/developers/mcp/?tab=mcp). Choose a product-specific MCP App endpoint when you want interactive views in a supported client.

## Connections used in this repository

| Connection | Endpoint | Purpose | Configuration |
| --- | --- | --- | --- |
| Standard MCP | `https://mcp.jotform.com` | Text-based forms and submissions. | [Direct client setup](../mcp-setup.md); [Codex setup](../openai-setup.md#codex) |
| Forms MCP App | `https://mcp.jotform.com/mcp-app` | Forms and submissions with interactive views in compatible clients. | [Claude plugin manifest](../../integrations/claude/jotform/.claude-plugin/plugin.json) |
| Jotform Sign | `https://mcp.jotform.com/mcp-sign-v1` | Signing documents, signers, and signature status. | [Claude plugin manifest](../../integrations/claude/jotform/.claude-plugin/plugin.json) |
| Jotform Apps | `https://mcp.jotform.com/mcp-jotform-apps-v1` | App and portal creation and editing. | [Claude plugin manifest](../../integrations/claude/jotform/.claude-plugin/plugin.json) |

The [Gemini extension](../../gemini-extension.json) uses `https://mcp.jotform.com/default`, the explicit route to the same standard MCP service. Both addresses select the standard tool set.

## Choose a connection

- **Installing the Claude plugin?** It includes the three product connections. Follow [Claude setup](../claude-setup.md).
- **Using Gemini CLI?** The extension configures `/default`. Follow [Gemini setup](../gemini-setup.md).
- **Connecting another MCP client?** Start with `https://mcp.jotform.com` for forms and submissions. Follow [direct MCP setup](../mcp-setup.md).
- **Using ChatGPT?** Follow [OpenAI setup](../openai-setup.md#chatgpt) to connect through the Jotform directory listing.

The three product connections follow [Jotform's MCP Apps reference](https://www.jotform.com/developers/mcp/?tab=mcp-app). Keep the endpoint supplied by your package when following its guide. See the [tool reference](tools.md) for the operations exposed by each service.

## Client requirements

Direct connections use remote HTTP MCP and browser-based OAuth. Interactive previews additionally depend on the client's MCP Apps support. Once connected, inspect the tools offered by that specific endpoint for its current operations and input schemas.

[MCP overview](README.md) · [Available tools](tools.md) · [Authentication and access](authentication.md)
