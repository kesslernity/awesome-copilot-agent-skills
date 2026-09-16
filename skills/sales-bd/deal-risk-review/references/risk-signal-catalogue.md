# Risk signal catalogue

Read by the deal-risk-review skill at step 5 (signal definitions, evidence tests, candidate next actions) and step 6 (severity definitions). The user's own sales process definition and scale replace any part of this catalogue when supplied; anything taken from here is labelled "default catalogue" or "default grading, confirm".

## Role vocabulary (default)

| Role | Evidence that assigns it | Not sufficient on its own |
|---|---|---|
| Economic buyer | The material shows this person approving, owning or releasing the budget for this purchase | A senior title |
| Budget owner | The material names the budget line, amount or cost centre and this person as holding it | "Has budget" in an owner's note with no source |
| Decision-maker | The prospect states this person decides, or the material shows them making the call | Attendance at meetings |
| Champion | The material shows this person advancing the deal inside the prospect (introductions, internal advocacy, sharing information) | Friendliness or frequent replies |
| Technical evaluator | The material shows this person assessing fit, running a trial or setting requirements | A technical title |
| Procurement or legal | The material shows this person handling terms, tendering or contract steps | None; must be evidenced |

## Signal definitions and evidence tests

Each signal is tested to Present, Absent or UNKNOWN. Present needs quoted evidence with an S ref and date; Absent needs the evidence that rules it out; otherwise UNKNOWN.

| # | Signal | Test | Default severity |
|---|---|---|---|
| 1 | Single thread | Only one prospect-side contact has any evidenced two-way exchange | High |
| 2 | No identified budget owner | No contact carries the budget owner or economic buyer role by evidence | High |
| 3 | Budget not confirmed | No source states that budget exists for this purchase in this period | Medium |
| 4 | Decision process undefined | No source describes who decides, the steps or the criteria | Medium |
| 5 | Close date slipped | Close date changed twice, moved more than 30 days in total, or recorded earlier than the review date, arithmetic shown (defaults) | Medium; High if the date has passed |
| 6 | Silence past threshold | No inbound contact from the prospect for 14 calendar days or more (default) | Medium; High past 28 days |
| 7 | Proposal sent, no recorded response | A proposal send event exists with no later inbound event referring to it | Medium |
| 8 | Competitor named | Any source names an alternative supplier or an in-house option | Low; Medium if named after the proposal |
| 9 | Overdue commitment by the user's side | A promise by the user's organisation with a due date earlier than the review date and no completion event | Medium |
| 10 | Stage advanced without exit criterion | A stage change event with no evidence of the criterion the sales process sets for that stage | Medium |
| 11 | Champion absent or departed | The champion's last inbound is older than the silence threshold, or a source records their departure or role change | High |
| 12 | Scope or requirement changed late | A source after the proposal introduces a requirement the proposal does not address | Medium |
| 13 | Legal or procurement not yet engaged | Stage is at or past proposal and no procurement or legal contact is evidenced | Low; Medium within 30 days of close |
| 14 | Contradictory record | Two recorded values for one field, or a stage the timeline does not support | Medium |

## Severity definitions (default)

- High: the signal alone can stop the deal if nothing changes.
- Medium: the signal delays or weakens the deal; it needs an action before the next review.
- Low: worth tracking; no action required beyond noting it.
- Compounding signals are noted together; they never produce a new grade.

## Candidate next actions

One per Present or UNKNOWN signal. Each proposal names the owner role, a relative due date and the result that would close the signal. These are proposals for the user to decide on; none is scheduled, sent or assigned by the agent.

| Signal | Candidate action | Closing result |
|---|---|---|
| Single thread | Ask the current contact for an introduction to a named second stakeholder in a stated role | A second contact with a two-way exchange evidenced |
| No identified budget owner | Ask the current contact who holds the budget for this purchase and when it is released | A named budget owner with the source recorded |
| Budget not confirmed | Ask directly whether budget is allocated for this period and what it covers | A stated budget position in the record |
| Decision process undefined | Ask the prospect to walk through the steps, people and criteria to a decision | A recorded decision process |
| Close date slipped | Ask the prospect what changed and what date they now expect; record the reason | A close date with the prospect's own reason recorded |
| Silence past threshold | One outbound contact with a specific question or offer of a specific next step; escalate to the relationship holder if a second period passes | An inbound reply |
| Proposal sent, no response | Ask for a review meeting on the proposal with a named agenda | A recorded response or meeting |
| Competitor named | Ask the prospect what they are comparing and on which criteria; record it | Recorded comparison criteria |
| Overdue commitment | Deliver or reschedule the commitment and tell the prospect | A completion or new date recorded |
| Stage advanced without exit criterion | Deal owner to confirm the criterion evidence or move the stage back | Criterion evidence recorded, or the stage corrected by the owner |
| Champion absent or departed | Confirm the champion's status; identify a successor | A confirmed champion with recent inbound |
| Scope changed late | Confirm the change with the prospect and route it to the delivery lead and pricing owner | A recorded scope decision |
| Legal or procurement not engaged | Ask the prospect who runs contracting and when they join | A named procurement or legal contact |
| Contradictory record | Deal owner to confirm which value is current and correct the record | One value recorded with the correction date |
| Any signal UNKNOWN | Deal owner to supply the missing source or date named in the UNKNOWN list | The signal re-tested to Present or Absent |

## Arithmetic conventions

- Days elapsed: review date minus the last inbound date, in calendar days, shown as "<later> minus <earlier> = <n> days".
- Slip total: sum of every close date move in days, with each move listed as "<old> to <new> = <n> days".
- Close date passed: review date minus the recorded close date, in calendar days, shown the same way.
- A missing or undated event makes the dependent test UNKNOWN; never estimate a date.
