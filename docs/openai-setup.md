# Set up Jotform in ChatGPT or Codex

Choose the tool you use: [ChatGPT](#chatgpt) or [Codex](#codex).

## ChatGPT

1. Open the [ChatGPT directory](https://chatgpt.com/apps) and search for **Jotform**.
2. Open the Jotform listing and choose **Connect** or the connection action shown there.
3. Sign in to Jotform and authorize access.
4. Start a chat, select Jotform, and ask:

> Find my forms.

You can then ask Jotform to create a form or explore its responses. See [Jotform's ChatGPT connection guide](https://www.jotform.com/mcp/) for the directory route.

## Codex

With Codex CLI installed, add the forms MCP service and sign in:

```sh
codex mcp add jotform --url https://mcp.jotform.com
codex mcp login jotform
```

Complete authorization in your browser, then start Codex:

```sh
codex
```

Enter `/mcp` to inspect the connection. Ask:

> Find my forms.

To configure the connection in a supported Codex settings UI, add an HTTP MCP server named `jotform` with `https://mcp.jotform.com`, then authenticate. This is the standard address in [Jotform's MCP reference](https://www.jotform.com/developers/mcp/?tab=mcp). See the [official Codex MCP guide](https://learn.chatgpt.com/docs/extend/mcp?surface=cli) for client-specific settings.

## Try it

> Create a contact form with name, email, and message fields.

> Summarize the responses to my customer feedback form.

## Troubleshooting

| Problem | What to check |
| --- | --- |
| Jotform is unavailable in ChatGPT | Check your workspace's directory and ask its administrator about connection availability. |
| Codex tools are missing | Run `codex mcp list`, check that `jotform` is present, and restart the session. |
| Authentication is required | Reconnect from the ChatGPT listing, or run `codex mcp login jotform`. |
| The wrong forms appear | Check the Jotform account used during authorization. |

[Authentication and access](mcp/authentication.md) · [OpenAI integration overview](../integrations/openai/README.md) · [All setup guides](README.md)
