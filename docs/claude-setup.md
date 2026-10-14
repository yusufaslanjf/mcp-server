# Set up Jotform in Claude

Choose the setup that fits your work:

- **Forms and submissions on claude.ai:** [connect Jotform from the directory](#connect-on-claudeai).
- **Forms, Sign, Apps, and reusable skills:** [install the Jotform plugin](#install-the-plugin) in Claude Code, claude.ai, or Cowork.

## Connect on claude.ai

1. Open your profile menu and select **Connectors**.
2. Find **Jotform** in the connector directory and choose **Connect**.
3. Sign in to Jotform and authorize access.
4. Enable the Jotform connector in your conversation and ask: **Find my forms.**

This is the directory connection described in [Jotform's Claude connection guide](https://www.jotform.com/mcp/).

## Install the plugin

### Claude Code

With [Claude Code](https://code.claude.com/docs/en/overview) installed, run these commands in your terminal:

```sh
claude plugin marketplace add jotform/mcp-server
claude plugin install jotform@jotform-plugins
```

Start Claude Code:

```sh
claude
```

Inside the session, enter `/mcp`, select the Jotform connection you want to use, and complete sign-in in your browser.

### claude.ai and Cowork

1. Open **Customize > Plugins > Add > Add marketplace**.
2. Enter `https://github.com/jotform/mcp-server`.
3. Install **Jotform** from the marketplace.
4. Open the plugin's **Connectors** tab and connect the products you want to use.
5. Sign in with your Jotform account when prompted.

On Team and Enterprise plans, an owner may need to enable the plugin or connectors for your organization.

## Choose your connections

| Connection | Use it for |
| --- | --- |
| Jotform | Forms and submission analysis. |
| Jotform Sign | Signing documents and signature status. |
| Jotform Apps | Client portals and event apps. |

Use the same Jotform account and workspace across connections when sharing forms or other assets between products.

## Check the setup

Start a conversation and ask:

> Find my forms.

Claude should use the Jotform connection and return your forms, or indicate that your account has none. To try creating one, ask:

> Create a customer feedback form with a rating and an optional comment.

The [plugin overview](../integrations/claude/jotform/README.md#try-it) has more examples. In Claude Code, you can also invoke a skill directly, such as `/jotform:jotform-forms`.

## Troubleshooting

| Problem | What to check |
| --- | --- |
| Plugin not found | Confirm you added `jotform/mcp-server` and used the install ID `jotform@jotform-plugins`. |
| Skills missing | Confirm the plugin is enabled, then start a new session. In Claude Code, `claude plugin list` lists installed plugins. |
| Connection needs authentication | Open `/mcp` in Claude Code, or the relevant connection in **Connectors** on claude.ai and in Cowork, and finish sign-in. |
| A form is available in one product but not another | Check the Jotform account and workspace used by each connection. |
| Installation or connection blocked by organization policy | Ask your organization owner to enable the plugin or connector. |

## References

- [Claude marketplace installation](https://code.claude.com/docs/en/plugin-marketplaces)
- [Plugins on claude.ai and in Cowork](https://claude.com/docs/plugins/build)
- [MCP connections in Claude Code](https://code.claude.com/docs/en/mcp)

[MCP endpoints](mcp/endpoints.md) · [Authentication and access](mcp/authentication.md) · [All setup guides](README.md)
