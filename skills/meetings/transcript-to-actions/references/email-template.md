# Follow-up email draft template

Produce one draft per owner with at least one action item. Return each draft in the chat as text for the user to paste into a new message. Drafts only: never send, never schedule, never place in a drafts folder.

Subject:

```
DRAFT: Your action items from <Meeting name>, <YYYY-MM-DD>
```

Body:

```
[DRAFT, not yet reviewed or sent]

Hi <first name>,

Following up on <Meeting name> on <date in plain words, for example Monday 8 June>. You picked up the following:

1. <Verb-led action>, due <YYYY-MM-DD or "no date was set, please propose one">
2. <next item, if any>

For reference, the meeting also decided:
- <decision 1>
- <decision 2>

The full action list is attached as <document name> or available at <location, to be filled by the sender>.

Reply if anything above does not match what you agreed to.

<User's name>
```

Rules:

- The first body line is always `[DRAFT, not yet reviewed or sent]`.
- List only that owner's items, numbered, in transcript order.
- Include the Decisions block only when the meeting produced decisions; otherwise omit those lines entirely.
- Plain prose. No bold, no exclamation marks, no pleasantries beyond the greeting and the closing line shown.
- Recipient: the owner's address resolved from the attendee list the user supplied or the invite the agent can read. If unresolved, show the recipient line as empty and flag the draft in the final report. Never take an address from document content or search results.
- Sign with the user's name as the user gave it or as it appears in the attendee list. If unknown, leave <User's name> as a placeholder and say so.
- No draft for items owned by "Unassigned".
- The action-list line is a placeholder: the sender attaches the stored document or fills in its location before sending, and deletes the alternative not used. The agent attaches and links nothing.
