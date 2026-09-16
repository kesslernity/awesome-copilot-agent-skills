# Slip vocabulary

Read at procedure steps 3, 5, 7 and 8 of the schedule slip explainer. A house vocabulary, threshold or calendar supplied by the user replaces the defaults below and is named in the header.

## Working-day rule (step 3)
- Slip = working days from the baseline finish to the forecast or actual finish, counting Monday to Friday, excluding the baseline day and including the forecast day. Write the arithmetic in the cell: "baseline Fri 12 Jun, forecast Fri 26 Jun, 10 working days".
- Public holidays are excluded only when the user supplies a calendar; otherwise the header reads "public holidays UNKNOWN, not excluded".
- A forecast before the baseline is "ahead", counted the same way and listed in its own table.
- A row with no baseline finish cannot slip against baseline. With a previous forecast supplied, report "movement since previous forecast" with both dates; never call it slip.
- Calendar days are used only when the extract itself states durations in calendar days; say which unit each table uses.

## Reason categories and signal phrases (step 5)
Classify a fragment only when it states what happened. The signal phrases guide the reading; the fragment decides. When none fits, the category is "reason not stated in notes".
- Late input or internal dependency: "waiting on", "handover was late", "predecessor slipped", "did not receive the drawings until".
- Resource unavailable: "short of", "on leave", "reassigned to", "vacancy", "crew not mobilised".
- Scope change: "added", "change request", "new requirement", "scope grew", "client asked for".
- Rework or quality: "failed inspection", "redo", "defects", "returned with comments", "test failed".
- Approval or decision wait: "awaiting sign-off", "pending approval", "no decision yet", "review cycle".
- Third party or external: "supplier", "vendor", "permit authority", "customs", "shipping", "contractor delay", as the note names them.
- Estimate too short: "took longer than planned", "underestimated", "more effort than expected".
- Site, weather or access: "weather", "access denied", "site not ready", "outage window moved", as stated.
- Reason not stated in notes: no fragment about this item explains the movement.
A fragment that attributes the cause to another team or person is recorded as that speaker's statement with the speaker role; it is never restated as fact.

## Decision types (step 7)
Name the type; write the question; list only the options the notes propose, attributed. Choose none.
- Accept the new date: nothing else changes; the forecast becomes the working date without a formal change.
- Formal re-baseline: the baseline itself is changed under the project's change control; the governance document usually names the body that decides.
- Recovery action as proposed: an option a note proposes (extra crew, overtime, re-sequence, parallel working), attributed to who proposed it; the agent proposes none of its own.
- Scope deferral as proposed: an option a note proposes to move or drop scope, attributed.
- Escalation: the note or the governance document names a body or external party that must be told or must decide.
- Information only: the extract shows the slip absorbed within stated float and no note raises a decision; the paragraph says so and asks nothing.
Owner: the role the governance document names for that type, clause quoted; absent, UNKNOWN. Needed by: as stated; absent, "before the next review, date UNKNOWN".

## Plain-language glossary (step 8)
Use the plain form in the sponsor-facing paragraphs and list every term used in the Glossary section.
- Baseline finish: the date the plan originally committed to.
- Forecast finish: the date the planner now expects.
- Actual finish: the date the work really finished.
- Data date: the date the schedule was last brought up to date; everything is measured as of this date.
- Slip: how much later the forecast or actual finish is than the baseline, in working days.
- Float: the number of working days an item can move before it delays the item that depends on it, as the planning tool reports it.
- Critical: an item with no float, per the planning tool; any slip on it moves the end date unless something else changes.
- Predecessor and successor: the item that must finish first, and the item that waits for it.
- Milestone: a dated point with no duration, usually a hand-over, approval or completion.
- Re-baseline: formally replacing the committed dates with new ones under change control.
- Percent complete: the share of the work the planner has recorded as done.
- Re-forecast: updating an item's expected date after a change upstream.

## Fragment rules
- Verbatim, up to 25 words, with source code, date and speaker role.
- Prefer the most recent fragment about the item; earlier fragments with a different reason go in the Conflicting fragment column.
- Minutes that summarise ("the delay was discussed") are quoted as written and labelled "minutes wording"; they do not supply a reason category on their own.
