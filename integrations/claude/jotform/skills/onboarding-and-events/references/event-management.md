# Event management

## Example request

"Create a workshop registration form and an event app containing that same form, the schedule, and venue details. Do not add a signing document unless I ask for one."

## Execution

1. Use the event dates, venue, schedule, and registration fields the user supplied. Ask for a missing essential before publishing it as fact. For an existing form, retrieve it with Forms tools. Otherwise call Forms `create_form` and keep its returned ID and URL.
2. When the form is ready, call Apps `create_app` with the event content and an instruction to embed that form ID and URL without creating a replacement. To update an existing event app, use Apps `edit_app` with the verified app ID and `instructions`.
3. Track background work through the connector that owns it. Confirm registration opens the original form. Do not claim publication, payment setup, attendee sync, or email reminders unless a tool result confirms an operation the user requested.
4. Prepare a Sign draft only if the user asked for a signing document, and only from content they supplied. Do not invent consent language, participant addresses, or a mass-signing workflow. Sending requires an explicit request and known signer roles.

## Observable success

- The registration form and the event app exist and are ready.
- The event app uses that same registration form, with the supplied schedule and venue.
- No Sign document or signature invitation exists unless the user asked for it.
- Any requested signing step is reported from its actual result.

This recipe does not create an unattended registration-to-signature trigger or ongoing event reminders.
