# Client onboarding

## Example request

"Create a client onboarding form for contact details and project requirements. Put that same form in a new client portal with a welcome page and resources. Prepare a separate service agreement draft from the terms I provide, but don't send it."

## Execution

1. Reuse the user's existing intake form when they ask for that. Otherwise call Forms `create_form` with the supplied fields and the intended workspace. Do not invent contact details or project terms. Keep the returned form ID and URL, and confirm the form is ready with Forms tools.
2. Call Apps `create_app` with a description that includes the exact form ID and URL, the requested welcome and resources pages, and an instruction to embed that form rather than generate a replacement. For an existing portal, use Apps `edit_app` with its app ID and the same instruction.
3. Track app generation with Apps `fetch` when the server supports it. Confirm the portal opens the original form ID. If the result does not show that destination, report reuse as unverified and ask the user to inspect the preview. Keep the source form and the portal.
4. If the user asked for an agreement, call Sign `create_sign_document` with the agreement content they supplied. A service agreement is a separate document, not a conversion of the intake form. Do not infer terms, recipients, or permission to use submissions. If the agreement terms are missing, ask before that step. Form and app work that does not depend on it can continue.
5. If the user asked to send the agreement, inspect the signer roles, confirm the document is ready, then call Sign `send_for_signature` once. Keep any returned sent-copy ID. If the user asked for a draft only, stop at the draft.

## Observable success

- The intake form exists and is ready.
- The portal exists and reuses that form, with no second form created for the embed.
- A requested agreement is reported as draft, pending, or sent, and no invitation was sent unless the user asked for it.
- The user receives the actual results and any step that is still incomplete.

This recipe does not route leads, synchronize later submissions, or monitor signatures after the conversation.
