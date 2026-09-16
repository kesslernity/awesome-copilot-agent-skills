# Register tests, test codes, default thresholds and required fields

Used by the master document register check. Document control may override any threshold; the question list header states the values used. Every test fires on evidence in the extract or the sources given, never on silence. Every code is a question for document control or the originating discipline, not a change to the register and not a judgement on any document's content.

## Test codes

| Code | Family | Fires when | Evidence to record | Addressee | Question pattern |
|------|--------|------------|--------------------|-----------|------------------|
| NUM-FORMAT | Numbering | The document number does not parse against the convention or the inferred pattern | Quoted number, expected pattern, whether the pattern is inferred | Document control | Correct the number, or confirm the exception? |
| NUM-DUP | Numbering | Two rows carry the same document number | Both row references, whether the revision is also the same | Document control | One document twice, or two documents needing distinct numbers? |
| NUM-DISC | Numbering | A discipline or type code inside the number disagrees with the discipline or type column | Quoted number, column value | Document control | Which is right, the number or the column? |
| NUM-GAP | Numbering | A sequence within a series skips one or more numbers | Series, the missing numbers | Document control | Is the number intentionally unused, or is a row missing from the extract? |
| REV-MISSING | Revision | Status reads issued or later and revision or revision date is blank | Status, blank field names | Document control | Supply the revision and date? |
| REV-SEQ | Revision | The history or a previous extract shows a skipped revision code | Codes before and after the gap, source | Originating discipline | Was a revision skipped or not recorded? |
| REV-BACK | Revision | The current revision is earlier than one previously recorded | Both revisions, source and date | Document control | Which revision is current? |
| REV-REPEAT | Revision | One revision code carries two different revision dates | Both dates | Document control | Which date is right, or was the revision re-issued unchanged? |
| REV-STATUS | Revision | The revision code family does not match the status under the scheme | Revision, status, scheme rule (procedure or inferred) | Document control | Update the status, the revision, or confirm as is? |
| REV-FUTURE | Revision | The revision date is after the check date | Both dates | Document control | Correct the date? |
| SCH-OVERDUE | Schedule | Planned date is before the check date and no actual date exists | Planned date, check date, days past planned, purpose column | Originating discipline | Forecast date, and reason for the delay? |
| SCH-DUE-SOON | Schedule | Planned date falls within the due-soon window after the check date | Planned date, days to planned | Originating discipline | On track, or forecast to move? |
| SCH-SLIP | Schedule | Forecast date is later than the planned date | Planned, forecast, days of slip | Originating discipline | Is the slip agreed, and is a re-baseline requested? (the agent re-baselines nothing) |
| SCH-STATUS-LAG | Schedule | An actual date exists but the status still reads not started or in progress | Actual date, status | Document control | Update the status? |
| SCH-NO-ACTUAL | Schedule | Status reads issued and no actual date is recorded | Status, blank field | Document control | Supply the actual date? |
| STALE | Schedule | An in-progress row's last update is older than the threshold | Last updated, threshold used | Originating discipline | Confirm the row is current? |
| CMP-FIELD | Completeness | A required field for the row's status is blank (table below) | Field names missing | Document control | Supply the missing fields? |
| TTL-MISMATCH | Title | One document number carries different titles across rows or extracts | Both titles, sources | Document control | Which title is current? |
| DUP-TITLE | Title | Two numbers carry the same or near-identical title in one discipline | Both numbers, overlapping words, grade Exact or Near | Originating discipline | Same deliverable twice, or two documents? |
| XCK-NO-TRANSMITTAL | Cross-check | A row reads issued with no transmittal reference and the log shows none | Status, log search result | Document control | Was it transmitted, and under which number? |
| XCK-NOT-IN-REGISTER | Cross-check | The log shows a document or revision the extract does not carry | Log line with date | Document control | Missing from the register, or outside the extract's scope? |
| XCK-REV-DIFF | Cross-check | The transmitted revision differs from the register's current revision | Both revisions, log date | Document control | Register behind, or log wrong? |

Several codes may apply to one row. List them all, in the order above.

## Default thresholds

| Test | Default | Note |
|------|---------|------|
| Overdue | Planned date before the check date, no actual date | Rows issued at their final purpose are never tested |
| Due soon | Planned date within 14 days after the check date | Reported for awareness, one question per row |
| Slip | Forecast later than planned by any margin | The user may set a tolerance in days; the header states it |
| Stale | Last update more than 30 days before the check date, in-progress rows only | Skipped when no last-updated column exists |
| Inferred pattern | At least half the rows must share one pattern for NUM-FORMAT to run | Below that, NUM-FORMAT is skipped and the header says so |

## Required fields by status (completeness test)

| Status as the register names it | Required fields |
|--------------------------------|-----------------|
| Not started or planned | Document number, title, discipline, originator, planned date for the first purpose |
| In progress | The above plus current revision or a stated draft marker, forecast date |
| Issued (any purpose) | The above plus revision, revision date, actual date, transmittal reference where the register carries that column |
| Superseded, cancelled, void, on hold | Document number, title, status date or remark stating why |

Status names differ between projects; map the register's own values to these rows and record the mapping in the closing report. A status that maps to none of them is "status UNKNOWN".

## Inferred pattern rule

When no numbering procedure or revision scheme is provided, the agent derives the dominant pattern from the extract, states it with the count of rows that match, and labels every question that relies on it "inferred from register, not from procedure". Those rows also appear in the UNKNOWN list. An inferred pattern is a working assumption for asking questions; it is never presented as the project rule.

## Date format rule

State the day and month order used to read the dates, and the evidence for it (a column header, an unambiguous value such as a day above twelve). Where a value could be read either way and nothing settles it, the date is UNKNOWN and the row is excluded from the schedule tests with a note.

## Addressee rule

Numbering, revision-record, completeness, title and cross-check questions go to document control. Schedule, stale, skipped-revision and duplicate-deliverable questions go to the originating discipline named in the row; where no originator is recorded, they go to document control with "originator UNKNOWN".

## Options offered on every question

Correct (the user supplies the corrected value), Confirm as is (document control confirms the register is right), Supply missing (the missing value is added by the user), Ask originator (the question is routed to the discipline first). Each question offers only the options that fit its code. The agent applies none of them; it re-runs on the corrected extract when asked.
