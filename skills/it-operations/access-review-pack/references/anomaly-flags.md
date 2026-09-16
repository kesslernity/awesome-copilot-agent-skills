# Access review pack: anomaly flags and the decision each needs

A flag is a question for the system owner to confirm. It is never a finding, a rating or a verdict. Each flag needs the data named in its row; where that data is absent from the export and extracts, the flag reads "not assessed" for the whole pack and the header says why. A line may carry several flags; each flag adds its own decision. The Decision required string is copied into the pack exactly as written here; it names the question, never the answer.

## Flag table

| Flag | Condition | Data needed | Decision required |
|---|---|---|---|
| Leaver | The account holder's HR status is left, terminated or ended, or the leaver date is on or before the review date | HR extract with status or leaver date, matched on exact identifier | Decide: leaver still holds this access |
| Mover | Department or manager in the HR extract differs from the value in the export | HR extract and a department or manager column in the export; where the export carries neither column, Mover is not assessed and the header says so | Confirm still needed in current role |
| Dormant | Last used is older than the inactivity threshold, or the account has never been used, and the account is enabled | Last used column; Status column (if absent, Dormant is assessed on Last used alone and the header says status was not available) | Decide: dormant account |
| Disabled | Account status is disabled and the entitlement is still present | Status column | Decide: disabled account still entitled |
| Privileged | Entitlement or account type contains a privileged marker | Entitlement column; type column if present | Confirm privileged need and approver |
| Orphan | Account type is service, shared or generic, or the identifier has no match in the directory or HR extract when one was provided | Type column, or directory extract | Identify account holder or custodian |
| Stale grant | Grant date is older than the stale grant threshold and no Last confirmed value exists | Grant date column | Confirm still needed: long-standing grant |
| No approver | Approver or grantor column is empty for the line | Approver column | Confirm who approved this grant |
| External | Account type is external, or the identifier is marked as outside the organisation in the export | Type column or an explicit external marker | Confirm external need and end date |
| Conflict | Both entitlements of a listed conflicting pair sit on the same account in the same system | User-supplied conflict list | Decide: listed conflict on one account |
| No flag | None of the above conditions met | | Confirm still needed |

## Matching rules

- Privileged markers are case-insensitive substring matches on the entitlement and type values. A marker hit on an entitlement such as "Report Owner" is still flagged; the owner clears it. Never remove a hit by judgement.
- Identity matching between the export and any extract is on the exact account identifier only. Display names, initials and email prefixes are not used for matching.
- Dates are compared to the review date stated in the header. An unparseable date is UNKNOWN and makes Dormant and Stale grant "not assessed" for that line, stated in the UNKNOWN list.
- Thresholds are the defaults in the skill (inactivity 90 days, stale grant 365 days) unless the user overrode them for this run; the header records the values used.
- No flag is added beyond this table unless the user asks for one and defines its condition and data in the conversation; the addition is recorded in the header.

## Owner decision values

These are the values the owner may enter in the Owner decision column. The agent never enters one.

| Value | Meaning |
|---|---|
| Keep | Access is still needed as it stands |
| Remove | Access is no longer needed; the owner raises the removal through the usual request or change path |
| Reduce | Access is needed at a lower level; the owner states the target level in Comment |
| Transfer | Access belongs with another person; the owner names them in Comment |
| Cannot decide | The owner is not the right decider; the owner names who is in Comment |

A completed section is the owner's record. The pack itself changes no access, and a decision written in it triggers nothing until the owner acts through the normal process.
