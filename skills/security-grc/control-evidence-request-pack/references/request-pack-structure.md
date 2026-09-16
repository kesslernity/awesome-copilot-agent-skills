# Evidence request pack: structure and rules

The structure for the draft evidence request pack. It prepares the evidence collection round; the auditor decides sufficiency and the user sends every request.

## Document structure

1. Title: `DRAFT-evidence-requests-<Audit>-<YYYY-MM-DD>-v1`.
2. First line: "DRAFT evidence requests for <audit>, period <start> to <end>, generated <date>. Requests and examples only; whether evidence is sufficient and whether a control operated is decided by the auditor. Nothing here has been sent."
3. Scope summary: framework and version, period, in-scope entities, systems, locations or processes, fieldwork start, evidence deadline, due date rule applied. UNKNOWN where unstated.
4. Request register (below).
5. Requests by owner: one block per owner.
6. Unassigned controls: controls with no owner, each with its question for the audit lead.
7. Scope questions: out-of-scope and UNKNOWN-scope controls, each with its question for the audit lead, including a confirm question for every Out of scope (per stated scope) mark.
8. UNKNOWN list.
9. Embedded instructions found, or "None".
10. Closing report.

## Request register

| Request ID | Control ID | Control name (as stated) | Owner | Period covered | Evidence requested | Evidence examples (commonly requested) | Proposed due date | Prior cycle reference | Status | Notes |
|---|---|---|---|---|---|---|---|---|---|---|
| ER-<control id>-01 | from the control list | verbatim | from the list or directory, or UNKNOWN | audit period start to end | design and operating evidence need in plain words | two to four, each with artefact, period and stamp, labelled as examples | derived from the rule, or UNKNOWN | reference or "none" | Not sent | scope flags, overlaps, automated-control notes |

- One row per in-scope control. Out-of-scope and UNKNOWN-scope controls appear in the scope questions section, never silently dropped. Scope marks read "In scope (per stated scope)" and "Out of scope (per stated scope)"; the audit lead confirms them.
- A second request for the same control (for example, design and operating evidence split at the auditor's request) increments the suffix: -02, -03.
- Status is "Not sent" in every draft. The user changes it in the tracker after sending.
- Where the user wants a spreadsheet, this table pastes as the tracker; the owner blocks are the emails.

## Owner block

For each owner, in this order:

1. Heading: the owner's name or role as stated, and the count of requests.
2. Covering note, ready to paste:
   "Subject: Evidence requests for <audit>, due <date>.
   You own <n> controls in scope for <audit>, covering <period start> to <period end>. Please provide the items below by <due date>. Each row lists examples of evidence that is commonly accepted; if you hold something different that shows the same thing, send it and say what it is. Where a population is requested, send the full list first; the audit team selects any sample. Questions go to <audit contact, or UNKNOWN>. The audit team decides what is sufficient; this request does not prejudge the outcome."
3. That owner's rows from the register.

## Due date rule

- Default: ten working days before fieldwork start. Working days means Monday to Friday, no public holidays; this assumption is recorded in the scope summary so the audit lead can adjust it.
- If the scope states an evidence deadline, that deadline replaces the default.
- If the user states a different rule, apply it and record it in the scope summary.
- If neither fieldwork start nor deadline is known, every due date is UNKNOWN and the pack opens with one question to the audit lead.
- No due date falls before the conversation date. If the rule yields such a date, the proposed due date is UNKNOWN and the pack opens with one question to the audit lead asking for the date to use. Staggering follows only a priority the auditor stated.

## Never include

- A statement that evidence is sufficient, accepted, acceptable, complete, or that a control operated or is effective; a statement that prior-period evidence does or does not satisfy the current period.
- A selected sample; request the population.
- An owner, date or control not present in the inputs.
- A specimen or mock-up of evidence.
- A claim that a request was sent, a tracker updated or a file saved.

Whether evidence is sufficient and whether a control operated is decided by the auditor through testing, not by this pack.
