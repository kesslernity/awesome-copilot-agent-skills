# Review tests, finding codes and default thresholds

Used by the RAID log review skill. The project manager may override any threshold; the pack header states the values used. The tests fire on evidence in the log or the supporting sources, never on silence. Every code is a proposal for the project manager, not a change to the log.

## Finding codes

| Code | Test | Fires when | Evidence to record | Proposed update pattern |
|------|------|------------|--------------------|-------------------------|
| CURRENT | All tests | No other code fires | None | "Current: no change proposed" |
| OVERDUE | Date | Status is open or in progress and the forward date (review-by, validate-by, needed-by) is before the review date | The forward date and the review date | Proposed text: "Review by: [PM to set]"; decision Ask owner |
| STALE | Date | Status is open or in progress and the last update is older than the threshold: 30 days (14 for issues), or twice the log's stated review cadence where the log states one, the cadence rule replacing the default | The last-updated date, the threshold and rule used | Proposed text: "Next step: [owner to confirm status]"; decision Ask owner |
| DATE-UNKNOWN | Date | No forward date and no last-updated date can be read for the row | Which date fields are blank | Proposed text: "Review by: [PM to set]"; decision Edit |
| CONFIRM-DUE | Date | Type is dependency, status is open or in progress, needed-by falls within 14 days after the review date and no counterparty confirmation is recorded | The needed-by date and the blank confirmation | Proposed text: "Counterparty confirmation: [owner to obtain]"; decision Ask owner |
| NOOWNER | Owner | Owner cell blank, UNKNOWN, TBC, a team name with no person or role, or several names | The owner cell as written | Proposed text: "Owner: [PM to assign]"; decision Edit |
| OWNERCHECK | Owner | A roster is provided and the owner named is absent from it | The owner cell and "not in roster" | Proposed text: "Owner: [confirm <owner> still holds this]"; decision Ask owner |
| DUP-EXACT | Duplicate | Two rows carry the same wording, allowing for punctuation | Both identifiers and the shared text | "Merge into <earliest identifier>?"; decision Accept, Reject |
| DUP-NEAR | Duplicate | Two rows describe the same subject with different wording | Both identifiers and the overlapping phrases | "Merge into <earliest identifier>?"; decision Accept, Reject, Ask owner |
| DUP-RELATED | Duplicate | One row's cause is another row's effect, or an assumption pairs with the risk that guards it | Both identifiers and the causal phrase | "Cross-reference <identifier>?"; decision Accept, Reject |
| INCOMPLETE | Completeness | A required field for the row's type is blank (table below) | The field names missing | Proposed text per field: "<Field>: [owner to supply]"; decision Ask owner |
| MISFILED | Type | The wording does not match the type filed under | The quoted phrase and the type it reads as | "Reclassify as <type>?"; decision Accept, Reject |
| MOVED | Movement | A supporting source states the entry closed, materialised, was delivered or changed owner or scope | Quoted passage, source, date | "Status: <as stated in source>, owner to confirm"; decision Ask owner |

Several codes may apply to one row. List them all, separated by commas, in the order above.

## Default thresholds by type

| Type | Forward date field | Overdue when | Stale when | Note |
|------|--------------------|--------------|------------|------|
| Risk | Review by | Before the review date | Last update more than 30 days before the review date | A risk with status closed or superseded is never tested |
| Assumption | Validate by | Before the review date | Last update more than 30 days before the review date | An assumption past its validate-by date is also a candidate for the question "validated, or now a risk?" |
| Issue | Target date or next step date | Before the review date | Last update more than 14 days before the review date | Issues move faster than risks; the shorter threshold is the default |
| Dependency | Needed by | Before the review date | Last update more than 30 days before the review date | CONFIRM-DUE also fires when needed-by falls within 14 days after the review date and no counterparty confirmation is recorded |

Where the log states its own review cadence (weekly, fortnightly, monthly), the cadence rule replaces the default: Stale fires when the last update is older than twice that cadence. The header names the rule applied.

## Required fields by type (completeness test)

| Type | Required when status is open or in progress |
|------|---------------------------------------------|
| Risk | Description, owner, mitigation or next step, review-by date, rating as the log names it (blank rating is reported as missing, never filled) |
| Assumption | Assumption text, impact if wrong, owner, validate-by date |
| Issue | Description, impact as the log names it, owner, next step |
| Dependency | Dependency text, needed-by date, owner, counterparty |

Closed and superseded rows are checked only for a closure date; a closed row with no date gets INCOMPLETE with "closure date" as the missing field.

## Type definitions and check phrases

Definitions: a risk might happen; an assumption is taken as true and not yet verified; an issue is happening now; a dependency relies on someone outside the team. Compare each row's wording with the type it is filed under.

| Filed as | Reads as | When the text | Example phrase |
|----------|----------|---------------|----------------|
| Risk | Issue | Describes something already happening or past | "has been delayed", "is blocking", "failed on" |
| Issue | Risk | Describes a possibility | "may", "might", "could", "if" |
| Assumption | Dependency | Names a third party the team is waiting on | "once <counterparty> delivers", "subject to <counterparty> approval" |
| Dependency | Assumption | States a belief with no counterparty | "we assume", "it is expected that" |

A match here is a reclassification candidate. The project manager decides; the agent never moves a row.

## Decision options

Accept (apply the proposed text as written), Edit (apply with changes the project manager writes), Reject (leave the row as it is), Ask owner (the project manager puts the question to the named owner before deciding; the pack supplies the question text). Every line in the decision list offers only the options that make sense for its code.
