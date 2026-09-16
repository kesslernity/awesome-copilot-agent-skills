# Corrective action tracker: fields, status families, flags, thresholds and evidence patterns

Used by the corrective action tracker. Every flag fires on evidence in the sources, never on silence, and every flag is a question for the owner or the quality lead, not a judgement that an action is late, complete or effective. The agent changes nothing; owners act and the quality lead decides.

## Tracker fields

| Field | Filled from | Rule |
|---|---|---|
| Action ID | Source identifier, else `CA-DRAFT-<n>` | Temporary identifiers are marked as such |
| Source and reference | Document title, section or page, date | One source per row; a duplicate in another source is a second row flagged DUPLICATE |
| Type as stated | Containment, correction, corrective, preventive, as the source names it | UNKNOWN where the source names none; never inferred |
| Action as stated | Verbatim wording | Never reworded, merged or split |
| Owner | Name or role as stated, or the directory | UNKNOWN where none is stated; never guessed from a similar action |
| Raised date | As stated | UNKNOWN where none is stated or the date is ambiguous; never inferred from the source document date |
| Due date | As stated | UNKNOWN where none or where the date is ambiguous |
| Days past or to due | Status date minus due date | Blank where the due date is UNKNOWN |
| Evidence expected | Quoted from the source, or proposed | Proposed entries carry "proposed, owner to confirm" |
| Evidence referenced | Attachment, record or link named in the source | "none referenced" where absent; never "received" |
| Status as stated | The source's own value | Never replaced by the agent |
| Status family | Open, closed, verified, or UNKNOWN | Mapping shown in the header |
| Last update | As stated | UNKNOWN where none |
| Verification recorded | Effectiveness verification as recorded, or UNKNOWN | Never "verified" unless the source records it |
| Reconciliation | Identifier match with the existing tracker, then exact wording match | Matched, New or Orphan; "no tracker" when none was given |
| Flags | Codes below, in order | Several per row allowed |
| Question | One per flag, with options | Addressed per the addressee rule |

## Status family mapping

Map each status the sources use to one family and show the mapping in the header, for example "In progress, Open, Assigned: open; Done, Closed, Completed: closed; Verified effective, Closed and verified: verified". A status that fits no family reads "status family UNKNOWN". The agent never adds a status the sources do not use, and never moves an action between families.

## Flags

| Code | Fires when | Evidence to record | Addressee | Question and options |
|---|---|---|---|---|
| OVERDUE | Due date is before the status date and the family is open or UNKNOWN | Due date, status date, days past due, status as stated | Owner | New forecast date and reason? Options: Supply forecast, Confirm complete with evidence, Ask quality lead |
| DUE-SOON | Due date falls within the due-soon window after the status date | Due date, days to due | Owner | On track, or forecast to move? Options: Confirm on track, Supply forecast |
| UNOWNED | No owner stated and none in the directory | Source reference | Quality lead | Who owns this action? Options: Name owner, Ask originator |
| NO-DUE-DATE | Open action with no due date | Source reference | Owner, else quality lead | What is the due date? Options: Supply date, Ask quality lead |
| NO-EVIDENCE-DEFINED | Source states no evidence of completion and the proposal is unconfirmed | Proposed evidence | Owner | Confirm or replace the proposed evidence? Options: Confirm, Replace, Ask quality lead |
| STALE | Open action whose last update is older than the stale threshold | Last update, threshold | Owner | Is the action still current? Options: Update, Confirm current |
| LONG-OPEN | Action open longer than the long-open threshold since it was raised | Raised date, days open | Quality lead | Awareness only. Options: Note, Escalate per procedure |
| CLOSED-NO-EVIDENCE | Family closed or verified with no evidence referenced | Status, "none referenced" | Owner | Where is the completion evidence? Options: Supply reference, Ask quality lead |
| CLOSED-NO-VERIFICATION | Family closed, the procedure requires effectiveness verification, none recorded | Status, verification rule quoted | Quality lead | Is verification due, done or waived? Options: Record, Schedule, Ask |
| CONFLICT | Tracker and source disagree on owner, due date or status | Both values with dates | Quality lead | Which value is the record of reference? Options: Tracker, Source, Ask originator |
| DUPLICATE | Same action appears in two sources or twice in one | Both references, wording overlap | Quality lead | One action or two? Options: Merge, Keep both |
| ORPHAN | Action in the existing tracker with no source in this run | Tracker row | Quality lead | Source missing from this run, or action to retire? Options: Supply source, Ask |

Several codes may apply to one action. List them all, in the order above. Where the effectiveness verification rule is UNKNOWN, CLOSED-NO-VERIFICATION is not applied and the header says so.

## Default thresholds

| Test | Default | Note |
|---|---|---|
| Overdue | Due date before the status date; family open or UNKNOWN | Closed and verified actions are never overdue |
| Due soon | Within 14 days after the status date | One question per action, awareness |
| Stale | Last update more than 30 days before the status date, open actions only | Skipped when no last-update field exists |
| Long-open | Open more than 90 days after the raised date | Skipped when no raised date exists |

The user may change any threshold; the header states the values used.

## Date reading rule

State the day and month order used and the evidence for it (a column header, an unambiguous value such as a day above twelve). A date readable either way is UNKNOWN, excluded from OVERDUE, DUE-SOON, STALE and LONG-OPEN, and listed in the UNKNOWN list with a note.

## Evidence expected patterns

Used only where the source does not state what shows the action done. Each proposal names the artefact, the date stamp it should carry and who holds it, and is labelled "proposed, owner to confirm".

| Action wording pattern | Proposed evidence |
|---|---|
| Train, brief, communicate | Attendance or completion record with names or roles and date; the material version delivered |
| Revise, update or issue a procedure, form or drawing | The revised document with its new revision and approval date; distribution or withdrawal record |
| Repair, replace, adjust, recalibrate | Work order closure record; inspection or calibration record after the work, with date and result as recorded |
| Add or change an inspection, check or control | Revised inspection plan or checklist with revision; first records produced under it |
| Supplier action | Supplier's response with date; receiving inspection records after the change |
| Design or specification change | Change record with approval; the revised specification revision |
| Investigate, analyse, review | The investigation or review record with date, participants by role and outcome as recorded |
| Contain, segregate, quarantine | Hold or quarantine record; item list with identifiers |

A proposal never states the evidence will be sufficient; the quality lead decides that when the evidence exists.

## Addressee rule

Owner-facing questions (OVERDUE, DUE-SOON, NO-DUE-DATE, NO-EVIDENCE-DEFINED, STALE, CLOSED-NO-EVIDENCE) go into that owner's chase block; CLOSED-NO-EVIDENCE sits under the block's closed sub-heading described below. Governance questions (UNOWNED, LONG-OPEN, CLOSED-NO-VERIFICATION, CONFLICT, DUPLICATE, ORPHAN) go to the quality lead. An owner-facing question on an UNKNOWN owner goes to the Unassigned block.

## Chase block

For each owner, in this order: heading with the owner as stated and the count of open actions; covering note; that owner's open rows; one line per question. Closed rows carrying CLOSED-NO-EVIDENCE follow the open rows under a sub-heading "Closed, evidence reference requested"; they ask for the evidence reference only and are not chased for completion.

Covering note, ready to paste: "Subject: Corrective actions in your name, status date <date>. You are named as owner of <n> open actions in <sources>. The rows below show each action as recorded, its due date and the evidence expected. Please answer the questions listed, supply a forecast date where one is asked, and point to the evidence where an action is complete. This note records the position as at <date>; it closes, extends or reassigns nothing. Questions go to <quality contact, or UNKNOWN>."

## Never include

- A status the sources do not use, or an action moved between families by the agent.
- A statement that an action is complete, effective, verified or late as a fact; flags are questions with quoted evidence.
- An owner, date or evidence reference not present in the sources or the directory.
- A root cause supplied by the agent.
- A claim that the tracker was updated, an action closed, a message sent or a file saved.
- Anything that states an action made an operation safe or authorises any operation, permit, isolation or work.
