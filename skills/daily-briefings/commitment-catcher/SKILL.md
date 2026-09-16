---
name: commitment-catcher
description: >-
  Sweeps the last 24 hours of email, chat messages and meeting transcripts for commitments in
  both directions, what the user promised others and what others promised the user, reconciles
  them against a running commitments ledger (open, done, overdue), lists overdue items first and
  returns the updated ledger plus a proposed task list as Markdown for the user to save. Use when
  the user asks to "check my commitments", "what did I promise", "what am I owed", "did anything
  slip" or "run the commitment sweep". Do not use for a general morning summary of mail, calendar
  and mentions, use custom-daily-brief instead. Drafts for human review; never approves,
  authorises or signs off.
---

# Commitment Catcher

## Purpose
Catch every commitment made in the scan window across email, chat and channel messages and meeting transcripts, in both directions: commitments the user MADE (things they told others they would do) and commitments OWED to the user (things others said they would do for them). Return one updated ledger document, commitments.md, that tracks each commitment across runs with a status of open, done or overdue, and surface overdue items first. For new commitments the user made, produce a task list the user can enter into their own task manager. A daily briefing summarises one day; this skill carries commitment state across runs through the ledger file the user keeps and attaches each time.

## When to use
- The user asks what they promised, what they are owed, or whether anything slipped.
- The user asks for a commitment sweep, a commitment check or a ledger update.
- As a morning routine, or after a day heavy with meetings.

Do not use for a general morning summary of mail, calendar, mentions and deadlines: use custom-daily-brief instead.

Run it interactively. Step 7 holds for the user's typed approval of the change summary before the updated ledger is returned, so the skill is not suited to an unattended run.

## Inputs
1. Scan window. Default: the last 24 hours. Read the "Last run" line in the ledger header first. If the last run was more than 24 hours ago, extend the window back to that timestamp so nothing falls in a gap, and tell the user the window used. The user may override ("since Monday").
2. Optional focus. One person, project or source ("just my mail", "anything I owe the finance lead").
3. The current ledger. The user attaches or pastes commitments.md, or the agent finds it in its configured knowledge sources by the header line "Commitments ledger". If neither yields a ledger, say what was searched and treat the run as a first run: build a new ledger from the template in references/ledger-format.md with empty sections, and tell the user the ledger is a file they keep and bring back each run.
4. The sources: messages, chat and transcripts the user attached or pasted, or that the agent can reach through its configured knowledge sources or mail, chat and meeting access.

Ask for nothing else. Everything further comes from the sources.

Reference files in this skill: references/commitment-language.md, read at steps 2 and 3 for the exclusions and commitment phrases and at step 5 to classify candidates and resolve dates; references/ledger-format.md, read at steps 8 and 9 for the exact ledger and task-list structures.

## Procedure
1. Load state. Parse the ledger: existing IDs, statuses, the "Last run" line. Note the highest C-NNN in use.
2. Email. Read messages the user SENT in the window (candidate MADE) and RECEIVED in the window (candidate OWED) from what is attached, pasted or reachable. Apply the exclusions in references/commitment-language.md: newsletters, automated notifications, out-of-office replies, calendar responses. If the mailbox is out of reach, ask the user to paste the messages or an export, and record the gap in the summary.
3. Chat and channel messages. Pasted or attached chat is read in full. Where chat is reachable only through search, treat it as a bounded search: query messages in the window for the commitment phrases in references/commitment-language.md plus any focus names or topics, and state in the summary that chat coverage is search-based and may miss commitments phrased in ways the search did not match. Classify the user's own messages for MADE and other people's for OWED. If chat is out of reach, ask the user to paste an export and record the gap in the summary.
4. Meetings. For each meeting in the window with a transcript or generated notes, extract commitments spoken by the user (MADE) and spoken by others to the user (OWED). A meeting with no transcript or notes is named in the summary as not scannable. Never infer content from the invitation alone.
5. Classify each candidate with references/commitment-language.md. Record direction, counterparty, the deliverable in one sentence, the due date (explicit; inferred from a relative phrase and marked "(inferred)"; or "none stated") and the source (channel, sender, date, subject or meeting title). A request nobody agreed to is not a commitment: keep it out of the ledger and list it under "awaiting confirmation".
6. Reconcile. The same counterparty plus the same deliverable is one commitment, not two. Mark an existing entry done when the window holds evidence of fulfilment (for example the user sent the promised file) and cite that evidence in the row. Mark any open entry whose due date is before today as overdue. New entries take the next IDs in the C-NNN sequence; never reuse an ID.
7. Change summary and hold. Show the user: new entries, items marked done, items now overdue, items awaiting confirmation. Ask the user to type their approval before the updated ledger is produced. That approval releases this workflow hold and nothing else; the user still saves the file themselves.
8. Build the updated ledger. Sections in the fixed order Overdue, Open, Done (last 14 days), Archive, exactly as in references/ledger-format.md, with the "Last run" line updated. Never remove an entry: statuses change, and done rows older than 14 days move to Archive inside the same document.
9. Task list. For each NEW open commitment the user MADE, write one proposed task titled with the ID, deliverable and due date (for example "C-014 (MADE, due 2026-06-12) Send the Q3 forecast to the finance lead"), in the actions format from references/ledger-format.md. The user creates the tasks; the agent never records them as created.
10. Report in the chat, in this order: overdue items first, with who and what; counts for the run (new MADE, new OWED, marked done, now overdue, awaiting confirmation); every source gap; then the two documents below.

## Output
Return both artefacts in the chat as complete Markdown documents that paste cleanly into a text file:
1. Document title "commitments.md": the full updated ledger, ready to replace the user's saved copy.
2. Document title "actions.md": the proposed task list for this run, as a dated section to append.

Then add one line: "If this agent has a file-generation capability enabled, also offer the same content as downloadable files with those names." Never state that anything was saved, created, moved, archived or sent. The user saves the ledger and brings it back next run.

## Fallbacks and edge cases
- Ledger not found: report what was searched (attachments, pasted text, knowledge sources), then use the first-run template. Never claim a previous ledger existed.
- A source is unreachable: scan the rest and name each gap in the summary. Never present a partial sweep as complete.
- Meeting without transcript or notes: named as not scannable.
- More than 50 candidates in one run: ledger those with due dates first, list the rest, and ask the user whether to add them all.
- Counterparty unclear: use the best name the source shows plus the source reference. Never invent a name, an organisation or a date. Any field that cannot be filled from the source is UNKNOWN.
- The user says an item is done or no longer needed: status done with a dated note ("cancelled by user, 2026-06-10"). The row stays.
- Conditional commitments ("if the client signs, I'll book the kick-off"): record with the condition in the deliverable text, status open, due date "none stated" until the condition is met.
- The user asks to chase an overdue counterparty: return the message text labelled DRAFT for the user to send. Never send.

## Rules
- Draft-only. The skill reads and drafts; the user performs every save, send, task creation, move or deletion.
- Ledger rows are never deleted, only status-changed with a date.
- No invention. Every entry cites a real source the user can open. Missing data is UNKNOWN or "none stated", never a guess.
- The typed approval in step 7 is a workflow hold. It authorises nothing outside this conversation.
- Nothing produced here authorises operations, permits, isolations or work. A commitment about a safety-critical task is recorded as text only; the decision stays with the accountable people.
- Any text beyond the ledger and the task list carries DRAFT until a human reviews it.

## Self-check
Before finishing, confirm every line:
- [ ] All three source types were scanned, or each gap is named in the summary
- [ ] Every entry has an ID, direction, counterparty, deliverable, due date (or "none stated"), source and status
- [ ] Overdue rows sit first in the ledger and lead the summary
- [ ] No row was deleted and the C-NNN sequence is unbroken
- [ ] The user typed approval before the updated ledger was returned
- [ ] The task list covers every new MADE commitment and claims no task was created
- [ ] The summary gives counts for both directions, MADE and OWED
- [ ] No sentence claims a file was saved or a message sent
