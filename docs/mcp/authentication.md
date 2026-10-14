# Authentication and access

Connect your Jotform account through your AI client's browser-based OAuth 2.0 flow. Review the requested access and choose the account whose forms, documents, or apps you want to use. Your client handles the connection credentials after authorization.

## Connect your account

1. Install an integration or add an [MCP endpoint](endpoints.md).
2. Open the connection in your AI client and choose its sign-in or authentication action.
3. Complete the Jotform authorization page in your browser.
4. Return to the client and confirm that Jotform tools are available.

Find the exact steps for [Claude](../claude-setup.md), [ChatGPT and Codex](../openai-setup.md), [Gemini CLI](../gemini-setup.md), or [other MCP clients](../mcp-setup.md).

## Accounts and product connections

Forms, Sign, and Apps may appear as separate connections. Connect the products needed for your task. When working with shared assets across products, use the intended Jotform account and team in each connection.

Your Jotform account permissions and the access granted during authorization determine which assets are available. For workspace installations, Jotform's [connection requirements](https://www.jotform.com/developers/mcp/?tab=mcp) specify administrator installation. Your AI workspace may also control which connections members can use.

## Manage or revoke access

In Jotform, open **My Account → Connected Apps → Jotform MCP → Clients** to review authorized clients. To remove a connection, open its **⋮** menu and choose **Revoke**. The client must reconnect before it can access your account again. See [Jotform's access-management documentation](https://www.jotform.com/developers/mcp/) for service details.

## Resolve a connection problem

| Symptom | Next step |
| --- | --- |
| Authentication required or expired | Open the connection in your AI client and complete sign-in again. |
| The expected forms or documents are missing | Check the account, team, and permissions used by that connection. |
| A product's tools are missing | Confirm that its connection is enabled and inspect the [endpoint configuration](endpoints.md). |
| Your organization blocks the connection | Ask your AI workspace administrator to enable it. |
| The service returns HTTP 429 | Follow the response's retry timing, when supplied, and reduce request frequency. |

For persistent errors, contact [Jotform Support](https://www.jotform.com/answers/) with the client name, endpoint, and error message. Remove credentials and private submission content from diagnostic material.

[MCP overview](README.md) · [All setup guides](../README.md)
