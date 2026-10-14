# Releasing integrations

Release each integration through its platform's distribution route. Keep the package identity stable and update the affected package's version for a new release.

## Before a release

1. Run the [repository and package checks](plugin-development.md#validate).
2. Install the package in a clean client environment and complete account connection.
3. Verify the scenarios affected by the release, recording the client version and outcome.
4. Check the setup guide, integration index, and endpoint reference against the package.
5. Publish release notes describing the user-visible changes and any required setup action.

## Claude

The repository marketplace points to `integrations/claude/jotform/`. Keep its name aligned with `.claude-plugin/plugin.json` inside the package.

For a public directory listing, submit that plugin folder through Anthropic's portal. A hosted MCP connector has its own submission and can be paired with the plugin. See [Claude publication](https://claude.com/docs/directory/publish) and [plugin submissions](https://claude.com/docs/plugins/submit).

When creating an archive, include the plugin folder and its contents, including hidden configuration files. Exclude the repository marketplace and unrelated integrations.

## Gemini CLI

Keep `gemini-extension.json` and its declared context file available at the extension root. Preserve the `jotform` identity and the existing repository installation URL.

GitHub Release archives must contain the manifest at their root. Gemini CLI tracks GitHub's **Latest** release for release-based installations, so a Claude or OpenAI release must not replace the Gemini release marked Latest. Keep any Gemini release archive self-contained and its manifest version aligned with the release tag. See [Gemini release rules](https://geminicli.com/docs/extensions/releasing/).

## OpenAI

The repository currently documents the existing ChatGPT connection and direct Codex MCP setup. Add a package only when its contents and installation route are ready to validate.

New OpenAI packages should follow the [current package format](https://developers.openai.com/plugins/build/plugins). Public directory distribution has its own [submission process](https://developers.openai.com/plugins/deploy/submission); adding a repository catalog does not publish a directory listing.

## Track verification

Record the package version, source commit, client version, tested scenarios, and result with each release. Offline validation confirms repository structure; account authentication and tool execution require separate live checks.

[Development guide](plugin-development.md) · [Contributing](../CONTRIBUTING.md)
