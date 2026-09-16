# Document formats: commitments.md and actions.md

Exact structures for the two documents this skill returns. Follow them precisely so every run can parse the previous run's output. The user keeps both files and brings the ledger back on each run; the agent returns the updated versions in the chat and never saves them itself.

## commitments.md structure

```markdown
# Commitments ledger

Updated by the commitment-catcher skill on each run and kept by the user. Entries are never deleted; statuses change instead.
Bring this file to every run.
Last run: 2026-06-10 08:15 (UTC+2), window 2026-06-09 08:15 to 2026-06-10 08:15

## Overdue

| ID | Direction | Who | Commitment | Due | Source | Status | Last update |
|---|---|---|---|---|---|---|---|
| C-009 | MADE | Client contact, external firm | Send the Q3 forecast workbook | 2026-06-08 | Email to the client contact, 5 Jun 2026, "Q3 planning" | overdue | 2026-06-10 |

## Open

| ID | Direction | Who | Commitment | Due | Source | Status | Last update |
|---|---|---|---|---|---|---|---|
| C-014 | MADE | Onboarding lead (colleague) | Review the onboarding deck and return comments | 2026-06-12 (inferred) | Chat with the onboarding lead, 9 Jun 2026 | open | 2026-06-10 |
| C-015 | OWED | Vendor account manager, supplier firm | Send the signed SOW | none stated | "Vendor sync" meeting transcript, 9 Jun 2026 | open | 2026-06-10 |

## Done (last 14 days)

| ID | Direction | Who | Commitment | Due | Source | Status | Last update |
|---|---|---|---|---|---|---|---|
| C-011 | MADE | Onboarding lead (colleague) | Book the workshop room | 2026-06-09 | Chat, 8 Jun 2026 | done (booking confirmation sent 2026-06-09) | 2026-06-09 |

## Archive

| ID | Direction | Who | Commitment | Due | Source | Status | Last update |
|---|---|---|---|---|---|---|---|
```

## Rules

- **ID**: C-NNN, zero-padded to three digits, strictly increasing, never reused, sequence continues across runs.
- **Direction**: exactly MADE or OWED.
- **Who**: the counterparty, never the user. Display name, plus organisation when external. UNKNOWN when the source does not show a usable name.
- **Commitment**: one sentence, the deliverable. Conditional commitments include the condition in this cell.
- **Due**: YYYY-MM-DD, with "(inferred)" appended when resolved from a relative phrase, or "none stated".
- **Source**: enough to find the original (channel, person, date, subject or meeting title).
- **Status**: open, overdue or done. Cancelled items become "done (cancelled by user, YYYY-MM-DD)". Done items carry brief closing evidence in parentheses. Every date inside the Status cell is YYYY-MM-DD.
- **Section order is fixed**: Overdue, Open, Done (last 14 days), Archive. A row lives in exactly one section, matching its status.
- Done rows older than 14 days move to Archive on the next run. Nothing is ever removed from the document.
- Update the "Last run" header line on every run with the timestamp and the window scanned.

## actions.md structure (proposed task list)

The agent returns a new dated section per run for the user to append to their copy; earlier sections are never rewritten. Each line is a task the user creates in their own task manager. The agent proposes; it never records a task as created.

```markdown
# Proposed tasks: new commitments the user made, to enter in a task manager

## 2026-06-10 run

- [ ] C-014 (MADE, due 2026-06-12) Review the onboarding deck and return comments for the onboarding lead
- [ ] C-016 (MADE, due none stated) Send conference notes to the #q3-launch channel
```

Each line carries the ledger ID, direction, due date and deliverable so the user can act from this document alone.
