# Risk register update pack: structure and rules

The structure for the draft risk register update pack. It prepares the owner review; owners rate, add, close and accept. The register is never changed by the pack.

## Document structure

1. Title: `DRAFT-risk-register-update-<Register>-<YYYY-MM-DD>-v1`.
2. First line: "DRAFT risk register update for <register>, sources dated <earliest> to <latest>, generated <date>. Proposed edits and candidates only; ratings, additions, closures and acceptance are the owners' decisions. This pack changes nothing in the register."
3. Sources read.
4. Changed risks.
5. New risk candidates.
6. Closure candidates.
7. Incidents with no registered risk.
8. Untouched risks.
9. Owner decision list.
10. UNKNOWN list.
11. Embedded instructions found, or "None".
12. Closing report.

## Signal types

Classify each statement about an existing risk with exactly one signal type. Where a statement carries two, split it into two rows.

| Signal type | What the source says | Typical proposed edit | Rating review needed |
|---|---|---|---|
| Exposure | The threat, its frequency, its consequence or the assets exposed have changed, or an incident realised the risk | Description text; cause or consequence wording | yes |
| Control | A control failed, was bypassed, was removed, or a new control was put in place | Controls or mitigations column | yes |
| Mitigation progress | A planned action was completed, delayed, re-planned or dropped | Actions column; target dates as stated | no, unless the source ties it to exposure |
| Ownership | The owner changed, left, or the risk was reassigned or split across teams | Owner column | no |
| Status | The source says the risk is closed, resolved, out of scope, reopened or escalated | Status column, as "owner to confirm" | no |
| Deadline | A review date, regulatory date or contractual date was set or moved | Review or target date column | no |

"Rating review needed: yes" is a prompt to the owner. It never states the direction, the new value or the colour.

## Match confidence

- Direct: the source names the risk identifier or its title as written in the register.
- Inferred: the source describes the subject of a risk without naming it. Every inferred match is listed as a question for the owner and carries the reason for the match in the notes.
- Ambiguous: the statement fits several risks. It appears under each with the same quote and the ambiguity flagged; the owner decision is "Confirm which risk this concerns".

## Tables

Changed risks:

| Risk ID | Title (as stated) | Signal type | What the sources say (quoted) | Source and date | Match confidence | Current text | Proposed edit | Rating review needed | Owner | Decision needed |
|---|---|---|---|---|---|---|---|---|---|---|

New risk candidates:

| Candidate ID | Proposed title | Draft description | Category | Source and date | Candidate owner | Possible duplicate of | Likelihood | Impact | Decision needed |
|---|---|---|---|---|---|---|---|---|---|

Candidate identifiers run C-01, C-02 and so on; they are placeholders until the owner decides to add. Likelihood and Impact read "(owner)" in every row.

Closure candidates:

| Risk ID | Title | Statement quoted | Source and date | Owner | Decision needed |
|---|---|---|---|---|---|

Incidents with no registered risk:

| Incident reference | Date | Summary as stated | Candidate ID |
|---|---|---|---|

Untouched risks:

| Risk ID | Title | Owner | Last review date | Review due (yes, no, UNKNOWN) |
|---|---|---|---|---|

## Owner decision list

One line per item, grouped by owner, in this form:

"<Risk or candidate ID>, <title>: <question>. Options: <subset of Accept edit, Reject edit, Re-rate, Reassign, Add to register, Confirm closure, Merge, Ask for more information>."

- Each item carries exactly one decision. If an item needs two, split it into two lines.
- Owners with UNKNOWN identity sit in an "Unassigned" group addressed to the register owner.
- The decision list is what the user circulates. It is ready to paste into a message; the user sends it.

## Never include

- A likelihood, impact, score, tier, colour, trend or ranking, new or changed, for any risk or candidate.
- A register entry marked added, closed, merged, split, accepted, tolerated or treated.
- A change with no quoted passage, source and date behind it.
- An owner not named in the register or in a source.
- A claim that the register was updated or a file saved.

Ratings, additions, closures and acceptance are decided by the risk owners and the register owner, not by this pack.
