# Change journal format

How the no-delete-guardrail skill builds the change journal it returns in the chat as `change-journal.md`. The user saves it, or appends the new rows to their own journal file. The journal is append-only: add rows at the bottom, never edit or remove existing rows.

## Creating the journal

When the user has no journal yet, return this exact header before the first row:

```
# Change journal

Append-only log produced with the no-delete-guardrail skill. One row per create, modify, move, rename, archive or delete, including refused and pending operations. Do not edit existing rows.

| Timestamp (UTC) | Item | Operation | Approval | Result |
|---|---|---|---|---|
```

## Column rules

- Timestamp (UTC): ISO 8601, for example 2026-06-10T14:32:00Z. If the current time is not known, ask, or write UNKNOWN.
- Item: full path for files and folders exactly as the user gave it; subject line plus mailbox folder for email; event title plus date for calendar items. Never invent a path.
- Operation: one of create, modify, move, rename, archive, delete.
- Approval: one of not-required (non-destructive create or new versioned file), approved (quote the user's approving words in brackets), declined (the user refused; quote their words in brackets), refused (bulk destructive), pending (listed but not yet approved).
- Result: one of proposed (action list returned, the user has not yet confirmed performing it), done (the user confirmed performing it), failed (add the one-line reason the user gave), refused, skipped (the user chose not to perform a released action).

## Example rows

| Timestamp (UTC) | Item | Operation | Approval | Result |
|---|---|---|---|---|
| 2026-06-10T09:14:00Z | /Projects/Q3/q3-summary-v2.docx | create | not-required (versioned copy, original untouched) | proposed |
| 2026-06-10T09:21:00Z | /Projects/Q3/old-draft.docx | delete | approved ("yes, delete the old draft") | done |
| 2026-06-10T09:25:00Z | /Archive/ (all 47 files) | delete | refused (bulk destructive) | refused |
