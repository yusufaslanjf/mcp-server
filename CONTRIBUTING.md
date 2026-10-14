# Contributing

Help people connect Jotform to their AI tools and get useful work done.

## Find the right place

| Change | Start here |
| --- | --- |
| Service capabilities, endpoints, or account access | [MCP documentation](docs/mcp/README.md) |
| Installation or troubleshooting | [Setup guides](docs/README.md) |
| A plugin, extension, or skill | [Development guide](docs/plugin-development.md) |
| Package versions and distribution | [Release guide](docs/releasing.md) |

## Submit a change

1. Describe the user problem and update the smallest relevant set of files.
2. Run `python3 scripts/validate.py` and `git diff --check` from the repository root.
3. For Claude package changes, run the Claude validation commands in the [development guide](docs/plugin-development.md#validate).
4. Check the affected setup or task in the relevant client. Record the client version, result, and anything you could not test in the pull request.

Keep each setup procedure in its guide and link to it from indexes. Put agent behavior in skills or context files. When documenting capabilities, use the package configuration, current server tools, and official product documentation as sources.

## Report a problem

For a repository issue, include the guide or package involved, the client and version, what you expected, and what happened. Remove credentials and private account data from examples.

For account access or an operation on Jotform, contact [Jotform Support](https://www.jotform.com/answers/).

[Repository overview](README.md)
