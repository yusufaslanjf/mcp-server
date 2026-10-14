# Jotform MCP

Jotform's hosted MCP services let AI assistants work with your Jotform account. Your client discovers the available tools, requests the operation you describe, and presents the result in the conversation.

**[Connect a client](../mcp-setup.md)** · **[Endpoints](endpoints.md)** · **[Tools](tools.md)** · **[Authentication](authentication.md)** · **[Integrations](../../integrations/README.md)**

## Choose your experience

| Experience | Use it for | Connect |
| --- | --- | --- |
| **Standard MCP** | Text-based form creation, editing, and submission analysis in an assistant or development tool. | `https://mcp.jotform.com` |
| **MCP Apps** | Interactive form previews, submission tables, signing documents, and app previews inside a compatible client. | Choose the Forms, Sign, or Apps [endpoint](endpoints.md). |

These are the two experiences described in [Jotform's developer overview](https://www.jotform.com/developers/mcp/). Interactive views require client support for MCP Apps. **Jotform Apps** is the product for building portals and apps, with its own MCP App connection.

## What you can do

| Area | Examples | Connection |
| --- | --- | --- |
| Forms | Find a form, create a survey, update questions or content. | Forms MCP or Forms MCP App |
| Submissions | Retrieve responses and explore feedback; the Forms MCP App also supports adding submissions. | Forms MCP or Forms MCP App |
| Sign | Prepare signing documents, manage signers, check signature status. | Jotform Sign |
| Apps | Create or edit a portal or event app and include existing forms. | Jotform Apps |

The [endpoint reference](endpoints.md) maps each connection to its address and package. The [tool reference](tools.md) shows which operations each connection provides.

## How it works

1. **Connect.** Add a service URL in your MCP client, or install a package that configures it.
2. **Authorize.** Sign in to Jotform and approve the requested access.
3. **Ask.** Describe the form, document, app, or information you need.
4. **Review.** Open the returned preview or link, or use the response in your next request.

Jotform runs the service. You need a Jotform account, an internet connection, and an AI client that supports the selected connection.

## MCP services and ready-to-use packages

The MCP service provides tools and account access. A **connector** is the connection your client makes to that service. A **plugin** or **extension** packages connection settings and can include **skills**: instructions that help the assistant carry out a task.

For example, the [Claude plugin](../../integrations/claude/jotform/README.md) connects Forms, Sign, and Apps and includes skills for each product plus onboarding and event recipes. The [Gemini CLI extension](../../integrations/gemini/README.md) configures the forms service and supplies Jotform context.

## Discover the tools

Start with the [tool reference](tools.md) for an overview. After connecting, open your client's MCP tool list for current names, descriptions, and input schemas. Developers can retrieve the same catalog through MCP's [`tools/list` method](https://modelcontextprotocol.io/specification/2025-06-18/server/tools).

Use the connected server's schema when building an integration. Tool names and input fields can differ between endpoints, and the server's catalog reflects the operations available to your account.

Start with a request that reads existing data:

> Find my forms.

Then try:

> Show the responses to my customer feedback form.

## Account limits and support

Jotform MCP has no additional service charge. Your Jotform plan's features and limits continue to apply. For current service and Enterprise information, see the [Jotform developer documentation](https://www.jotform.com/developers/mcp/).

For connection issues, start with [authentication and troubleshooting](authentication.md). For help with a Jotform operation, contact [Jotform Support](https://www.jotform.com/answers/) and include your client, endpoint, and the error message.

[All documentation](../README.md) · [Repository overview](../../README.md)
