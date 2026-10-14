# Jotform AI Integrations

![AI assistants connect through Jotform MCP to work with Forms, Sign, and Apps.](docs/assets/ai-integrations.svg)

**Build forms, understand responses, prepare signing documents, and create apps from your AI assistant.**

Explore Jotform's hosted MCP services, choose a ready-to-use integration, and connect your Jotform account. This repository brings together the service documentation, client packages, and setup guides.

[Explore MCP](docs/mcp/README.md) · [Choose your AI tool](#choose-your-ai-tool) · [Browse integrations](integrations/README.md) · [Contribute](CONTRIBUTING.md)

## What will you build?

| Start with a request | Work with |
| --- | --- |
| “Create a customer feedback form with a rating and an optional comment.” | **Forms** — surveys, registrations, and feedback. |
| “Summarize this week's responses to my feedback form.” | **Submissions** — explore responses and find useful patterns. |
| “Prepare a service agreement draft using these terms.” | **Sign** — signing documents and signature status. |
| “Create a client portal containing my onboarding form and a welcome page.” | **Apps** — portals and event apps built around your forms. |

Choose an integration with the products you need. The Claude plugin also includes recipes for client onboarding and event management.

## Explore the MCP service

[Jotform MCP](https://www.jotform.com/mcp/) gives AI tools access to Jotform through the Model Context Protocol. Jotform hosts the service; you connect from your AI tool and authorize access to your account.

For a direct forms and submissions connection, use the standard MCP server:

```text
https://mcp.jotform.com
```

Jotform offers two experiences: **standard MCP** for text-based work with forms and submissions, and **MCP Apps** for interactive previews and views in compatible clients. MCP Apps are available for Forms, Sign, and Jotform Apps. Ready-to-use packages configure these connections and can add skills for common tasks.

**[Service overview](docs/mcp/README.md)** · **[Endpoints](docs/mcp/endpoints.md)** · **[Available tools](docs/mcp/tools.md)** · **[Authentication and access](docs/mcp/authentication.md)**

## Choose your AI tool

| Your tool | How to connect | What you get | Start here |
| --- | --- | --- | --- |
| **Claude Code, claude.ai, Cowork** | Jotform plugin; directory connector on claude.ai | Plugin: Forms, Sign, Apps, and four skills. Connector: forms and submissions. | [Choose your setup](docs/claude-setup.md) |
| **ChatGPT** | Jotform directory connection | Jotform forms and submissions in chat. | [Connect Jotform](docs/openai-setup.md#chatgpt) |
| **Codex** | Direct MCP connection | Forms and submissions through the hosted service. | [Configure Codex](docs/openai-setup.md#codex) |
| **Gemini CLI** | Jotform extension | Forms and submissions with Jotform context. | [Install the extension](docs/gemini-setup.md) |
| **Cursor, VS Code, other MCP clients** | Direct MCP connection | Forms and submissions in your existing AI tool. | [Connect your client](docs/mcp-setup.md) |

### Quick install

**Claude Code**

```sh
claude plugin marketplace add jotform/mcp-server
claude plugin install jotform@jotform-plugins
```

**Gemini CLI**

```sh
gemini extensions install https://github.com/jotform/mcp-server
```

Open your AI tool and complete the account connection in its [setup guide](docs/README.md). Then ask:

> Find my forms.

Once you can see your forms, try one of the requests above.

## Explore the repository

| Looking for | Go to |
| --- | --- |
| MCP capabilities, endpoints, and account access | [MCP documentation](docs/mcp/README.md) |
| Available packages and connections | [Integration catalog](integrations/README.md) |
| Installation and troubleshooting | [Setup guides](docs/README.md) |
| Package structure and validation | [Development guide](docs/plugin-development.md) |
| A file map for repository agents | [AGENTS.md](AGENTS.md) |

For Jotform's product overview and full service reference, visit [Jotform MCP](https://www.jotform.com/mcp/) and the [MCP developer documentation](https://www.jotform.com/developers/mcp/).

## Support

For help connecting or using Jotform, visit [Jotform Support](https://www.jotform.com/answers/) or email [support@jotform.com](mailto:support@jotform.com), copying [mcp@jotform.com](mailto:mcp@jotform.com). Include the AI tool and the connection you are using.

For a documentation or package issue, [open an issue](https://github.com/jotform/mcp-server/issues).

[Privacy](https://www.jotform.com/privacy/) · [Terms](https://www.jotform.com/terms/) · [MIT license](LICENSE)
