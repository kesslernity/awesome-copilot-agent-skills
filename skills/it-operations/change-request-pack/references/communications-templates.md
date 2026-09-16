# Change communications: notice templates

Three notices are drafted with every pack: pre-change, completion, rollback. Each is headed DRAFT, built from supported facts only, and returned inside section 8 (Communications) of the change request pack; if the user asks for them as a separate document, title it `change-notices-<identifier or short title>-<YYYY-MM-DD>`. The user sends them at the times the communications table states. The agent sends nothing.

A notice element with no supporting input reads UNKNOWN inside the notice, so the sender sees the gap. Nothing is invented to make a notice read smoothly.

## Pre-change notice

Recipients: <audience as stated in the communications table, or UNKNOWN>

Subject: Planned change to <affected service or item>: <window start, time zone>

Body:

1. One sentence naming what changes and why, from the description and justification.
2. Window: start and end with time zone, as stated; or UNKNOWN.
3. Expected effect on the recipients during the window, as stated by the requester (interruption, degraded function, none stated); or UNKNOWN. Never write "no impact" unless the requester stated it, and then attribute it.
4. What recipients should do before or during the window, if the notes state anything; otherwise omit the paragraph.
5. Where to report a problem or ask a question: the channel or queue as stated; or UNKNOWN.
6. Change identifier if assigned; otherwise "reference to follow".
7. Sign-off as the sender named in the communications table, or as the user.

## Completion notice

Recipients: same as the pre-change notice unless the table states otherwise.

Subject: Change to <affected service or item> completed

Body:

1. One sentence stating that the change described in the pre-change notice was implemented; the outcome is left as <within the window, or outside the window> and the end time as <actual end time>, both for the sender to fill with the true reading at send time.
2. What recipients may notice now, as stated by the requester; or UNKNOWN.
3. Where to report a problem: the channel or queue as stated.
4. Change identifier.
5. Sign-off as above.

## Rollback notice

Recipients: same as the pre-change notice unless the table states otherwise.

Subject: Change to <affected service or item> backed out

Body:

1. One sentence stating that the change was backed out and the service returned to its previous state, as the rollback plan describes; the time is left as <rollback time> for the sender to fill.
2. Effect on recipients during the back-out, as stated in the rollback plan; or UNKNOWN.
3. Next step: "A new window will be communicated" only if the notes state a retry is planned; otherwise "Next steps will be communicated".
4. Where to report a problem: the channel or queue as stated.
5. Change identifier.
6. Sign-off as above.

## Rules

- Every fact in a notice traces to the pack; no reassurance, apology or explanation the notes do not contain.
- No deadline, escalation or consequence the requester did not state.
- No additional recipients and no forwarding suggestion.
- Times carry their time zone. Placeholders in angle brackets mark values the sender fills at send time.
- The notices never state that the change has been approved; approval is the change authority's record, not the notice's claim.
- The agent drafts the text; the user sends it. Nothing is sent, scheduled or posted by the agent.
