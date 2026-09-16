# Change request pack: default field set

Used when the organisation has no change template of its own. When a template exists, its field names and order win; map these fields onto it and record the mapping in the report. Every field appears in the pack. A field with no supporting input reads UNKNOWN and gets a numbered question addressed to the engineer or the role named.

## Fields in order

| Field | What it holds | Fill only from | UNKNOWN wording |
|---|---|---|---|
| Change title | One line, what changes on what | Notes | UNKNOWN: title to be confirmed |
| Change identifier | Number assigned by the change tool | Change tool, user | UNKNOWN: assigned on submission |
| Requester and implementer | Role or team; a person only if the notes name one | Notes | UNKNOWN |
| Change type | Standard, normal, emergency or the policy's own terms; copied as the requester states it, labelled "as stated by requester" | Notes, verbatim | UNKNOWN: type to be set with the change manager |
| Description | Two to five sentences: what changes, in which environments, from what to what | Notes | UNKNOWN |
| Justification | The business or technical reason, linked incident or problem if named | Notes, linked records | UNKNOWN: reason not stated |
| Out of scope | What this change does not do, where stated | Notes | Not stated |
| Affected items | Systems, services, configuration items, environments, user groups, locations, dependencies, each as named | Notes, configuration list (exact match) | UNKNOWN |
| Requested window | Start, end, time zone, duration as stated | Notes | UNKNOWN: window to be proposed by requester |
| Policy comparison | Freeze period and lead time comparison, only when a policy was provided | Policy and window | No policy provided |
| Implementation plan | Numbered steps as given: action, role, expected result, verification, source | Notes, verbatim order | UNKNOWN step where the notes jump |
| Risk factors | What could fail, who would notice, downtime, data effect, each verbatim | Notes | UNKNOWN: no risk factors stated |
| Risk rating | Copied as the requester states it, labelled "as stated by requester"; never computed | Notes, verbatim | UNKNOWN: rating to be set with the change manager |
| Rollback plan | Trigger, steps, role, time to complete, point of no return, data restoration | Notes | UNKNOWN, mandatory question |
| Test evidence | One row per test: environment, date, result as stated, evidence provided yes or no, reference | Attached evidence, notes | Claimed, evidence not provided |
| Communications | Audience, purpose, channel, timing, sender | Notes | UNKNOWN |
| Approvals route | Approvers and order as the policy or notes name them; every status Pending | Policy, notes | UNKNOWN: route to be confirmed |
| Related records | Incidents, problems, previous changes, pull requests, by identifier | Notes, linked records | None stated |
| Post-implementation review | Whether and when one is required, as stated by the policy or notes | Policy, notes | UNKNOWN |

## Pre-submission checklist

Built from the fields above. Each item reads Ready yes or no with what is missing.

1. Description and justification filled from the notes.
2. Every affected item named; configuration list matches recorded where a list exists.
3. Window stated with time zone; policy comparison written where a policy exists.
4. Implementation steps numbered, each with a verification or an UNKNOWN marker.
5. Risk factors listed; rating cell as stated or UNKNOWN, never filled by the agent.
6. Rollback plan present as stated, or the mandatory question is first in the list.
7. Every test claim has evidence attached or reads "claimed, evidence not provided".
8. Communications rows complete or UNKNOWN; notices drafted and headed DRAFT.
9. Approvals route named or UNKNOWN; every status Pending.
10. Credentials and secrets absent from the pack.

## Writing rules

- Plain sentences, present tense. No adjectives about risk or ease ("routine", "trivial", "low-impact", "safe") except inside a quotation attributed to the requester.
- Figures, times and names appear exactly as the inputs give them, with unit and time zone. Nothing is rounded, converted or tightened.
- A Conflict between inputs is shown as "Conflict: <value A> (<source A>); <value B> (<source B>)" and carries a question. The agent never chooses.
- The pack stays DRAFT until the engineer completes it and the change authority approves. Submission, scheduling and approval are the user's actions in the change tool, never the agent's.
