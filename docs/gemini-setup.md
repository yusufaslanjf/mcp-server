# Set up Jotform in Gemini CLI

The [Jotform extension](../integrations/gemini/README.md) connects Gemini CLI to Jotform for working with forms and submissions.

## Install

With [Gemini CLI](https://geminicli.com/docs/get-started/installation/) installed, run in your terminal:

```sh
gemini extensions install https://github.com/jotform/mcp-server
gemini
```

## Connect your account

Inside Gemini CLI, run:

```text
/mcp auth jotform
```

Complete sign-in with your Jotform account in the browser. Enter `/mcp` in Gemini CLI to check the connection and available tools.

## Try it

Ask in natural language:

- "Find my forms."
- "Create a contact form with name, email, and message fields."
- "Show responses to my customer feedback form."

## Troubleshooting

| Problem | What to check |
| --- | --- |
| Extension missing | Run `gemini extensions list` in your terminal and check for `jotform`. Restart Gemini CLI after installation. |
| Authentication required | Run `/mcp auth jotform` inside Gemini CLI and complete browser sign-in. |
| Wrong forms returned | Check that you signed in to the intended Jotform account. |

The connection is configured in [`gemini-extension.json`](../gemini-extension.json). Gemini loads [`JOTFORM.md`](../JOTFORM.md) as the extension's context.

## References

- [Gemini CLI extensions](https://geminicli.com/docs/extensions/)
- [Gemini CLI command reference](https://geminicli.com/docs/reference/commands/)

[MCP endpoints](mcp/endpoints.md) · [Authentication and access](mcp/authentication.md) · [All setup guides](README.md)
