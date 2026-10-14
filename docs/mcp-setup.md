# Connect an MCP client to Jotform

Use this guide for a direct connection from Cursor, VS Code, or another client that supports remote HTTP MCP servers and OAuth.

For a packaged integration, use [Claude setup](claude-setup.md) or [Gemini setup](gemini-setup.md). For ChatGPT or Codex, follow [OpenAI setup](openai-setup.md).

## Server address

Use the standard forms and submissions server listed in [Jotform's MCP documentation](https://www.jotform.com/developers/mcp/?tab=mcp):

```text
https://mcp.jotform.com
```

Add this URL in your client's MCP settings and sign in with your Jotform account when prompted. The [endpoint reference](mcp/endpoints.md) describes the other Jotform connections.

## Cursor

Add the following to `.cursor/mcp.json` in your project, or merge the `jotform` entry into an existing `mcpServers` object:

```json
{
  "mcpServers": {
    "jotform": {
      "url": "https://mcp.jotform.com"
    }
  }
}
```

Open Cursor's MCP settings and complete authentication for `jotform`.

## VS Code

Run **MCP: Add Server** from the Command Palette, choose **HTTP**, and enter the server address above. Name the server `jotform` and choose where to save the configuration.

Alternatively, add the following to `.vscode/mcp.json`, or merge the entry into an existing `servers` object:

```json
{
  "servers": {
    "jotform": {
      "type": "http",
      "url": "https://mcp.jotform.com"
    }
  }
}
```

Run **MCP: List Servers**, select `jotform`, and start the connection. Complete browser sign-in when prompted.

## Check the connection

Open an agent conversation with the Jotform tools enabled and ask:

> Find my forms.

The assistant should retrieve forms from your account, or indicate that you have none. If tools are unavailable, check the client's server status and finish any pending authentication.

## References

- [Cursor MCP configuration](https://cursor.com/docs/mcp)
- [VS Code MCP configuration](https://code.visualstudio.com/docs/agent-customization/mcp-servers)

[MCP overview](mcp/README.md) · [Authentication and access](mcp/authentication.md) · [All setup guides](README.md)
