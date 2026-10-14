# MCP tools

Use this reference to choose a connection by what you want to do. Your AI client discovers the tools after connecting; you can ask for these tasks in natural language.

## Standard MCP

The standard service at `https://mcp.jotform.com` provides the following tools. The Gemini extension's `/default` connection uses the same catalog.

| Tool | Use it to |
| --- | --- |
| `search` | Find forms and apps by title, date, and other criteria. |
| `create_form` | Build a form from a description. |
| `edit_form` | Change an existing form. |
| `fetch` | Read the details of a form or submission. |
| `get_submissions` | List a form's submission IDs with filters and pagination, then use `fetch` for details. |
| `assign_form` | Assign a form to an email recipient with a message. |
| `analyze_submissions` | Explore response patterns, summaries, and statistics. |

See the [official standard MCP reference](https://www.jotform.com/developers/mcp/?tab=mcp).

## MCP Apps

Each product has its own [endpoint](endpoints.md) and tool catalog. Compatible clients can display interactive previews and browsers alongside tool results.

### Forms

The Forms MCP App supports `search`, `fetch`, `create_form`, `edit_form`, `assign_form`, and `analyze_submissions`, plus these operations:

| Tool | Use it to |
| --- | --- |
| `display_form` | Open a form preview. |
| `list_submissions` | Browse a form's responses in a submission table. |
| `create_submission` | Add a response to a form. |
| `get_embed_code` | Get the HTML needed to embed a form. |
| `get_teams` | Find available Enterprise teams. |

For response retrieval, the standard service exposes `get_submissions`; the Forms MCP App exposes `list_submissions`.

### Sign

| Task | Tools |
| --- | --- |
| Find documents and review signing activity | `search`, `list_submissions` |
| Create or edit a signing document | `create_sign_document`, `edit_sign_document` |
| Review and update recipients | `get_signers`, `update_signer` |
| Send a signature request and check progress | `send_for_signature`, `get_signing_status` |

### Jotform Apps

| Task | Tools |
| --- | --- |
| Find an app and read its details | `search`, `fetch` |
| Build or update a portal or app | `create_app`, `edit_app` |
| Find available Enterprise teams | `get_teams` |

See the [official MCP Apps reference](https://www.jotform.com/developers/mcp/?tab=mcp-app) for product details and interactive views.

## Inspect the current schema

The tables summarize the main assistant-facing operations. Open your client's tool list, or use MCP's `tools/list` method, for the connected server's current input and output schemas. Use the definitions from that connection when constructing requests; a shared tool name such as `search` operates on the product connected to that server.

[MCP overview](README.md) · [Endpoints](endpoints.md) · [Connect a client](../mcp-setup.md)
