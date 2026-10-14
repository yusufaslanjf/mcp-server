---
name: onboarding-and-events
description: Run client onboarding or event management across products. Use when one request needs a registration, RSVP, or intake form reused in a client portal or event app, with a separate contract only if the user asks for one. This is not Jotform Workflows, and there is no Workflows connector to call.
---

# Onboarding and events

Use this skill when one request needs more than one of Forms, Apps, and Sign, and those connectors are available in the same conversation. A request that needs only one product should use that product's skill. Jotform Workflows is a separate product and has no connector here. Do not look for a workflows tool or invent an automation.

## Pick the recipe

- Client intake, a client portal, and an optional service agreement: read [client onboarding](references/client-onboarding.md).
- Event registration, an event app, and optional consent: read [event management](references/event-management.md).

Follow `jotform-forms`, `jotform-apps`, and `jotform-sign` for each connector the recipe uses.

## Coordinate the steps

1. Identify the outcomes the user asked for and the details they already gave. Ask only for what a step needs. Creating an onboarding form is not a request to create an app or an agreement.
2. Use the same Jotform account and workspace for assets that are meant to be shared. Connect a product only when the request needs it. A shared OAuth provider does not mean the connections use the same account. If access fails, stop the step that depends on it.
3. Keep a short working list of each finished step: connector, asset type, returned ID, user-facing URL, state, and verified relationship. This is context for the current task, not a stored record.
4. Wait until the source asset is ready before a step that depends on it. Read each tool result as that product returns it.
5. Pass only identifiers and content the user authorized, and only after the tool result confirms them. Use the product's own `search`, `fetch`, or status tool when short names overlap. Never turn a form ID into an app ID or a Sign ID.
6. Verify that the app uses the exact source form. Two created assets are not evidence that they are connected. A successful generation is not proof of the requested relationship.
7. Create a Sign document only when the user asked for one. Do not copy submission data into a contract unless the user authorized that. Do not send, sign, or place personal signing links in an app unless the user asked for that specific action.
8. On a partial failure, report what exists and what is unfinished, with the identifiers needed to resume. Keep completed assets. Do not roll back, delete, create again, or send again without a new request and evidence that the first attempt did not succeed.

## Finish

Report each requested outcome as completed, pending, failed, or unverified. Return the actual previews and links. Do not call the request complete while embedding or sending is unverified. These recipes run during the conversation. Do not promise later synchronization, automatic triggers, or unattended monitoring.
