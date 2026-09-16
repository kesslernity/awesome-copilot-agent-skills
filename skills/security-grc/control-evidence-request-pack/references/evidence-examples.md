# Evidence examples by control pattern

Match each in-scope control to the closest pattern by what its description says it does, then write two to four examples for the request. Examples are the artefacts commonly requested for that kind of control. They are not a checklist, they do not guarantee acceptance, and the auditor decides sufficiency. Where no pattern fits, write the evidence need in plain words from the control description and flag the row for the auditor.

Every example names three things: the artefact, the period it must cover, and the stamp that shows when and where it came from (system date stamp, export header, approval date, signature date).

## Design evidence, any pattern

- The current policy or procedure that describes the control, with version, approval date and approver.
- The configuration, setting or approval matrix that enforces it, exported with a date stamp.
- The role or team assignment that names who performs it.

## Operating evidence by pattern

| Control pattern (as the description reads) | Population to request first | Operating evidence examples | Stamp to look for |
|---|---|---|---|
| Joiner, mover, leaver access provisioning | List of all joiners, movers and leavers in the period from the source of record | Access request tickets with approval before provisioning; leaver tickets with removal date; system account list at period end | Ticket dates, approver identity, account disable date |
| Periodic access review | List of all reviews due in the period per system | Completed review records with reviewer, date and outcome; remediation tickets for removed access | Review completion date, sign-off identity |
| Privileged access | List of privileged accounts per in-scope system at period start and end | Approval for each privileged grant; privileged session logs or monitoring reports for the period | Grant date, log export date |
| Authentication settings | Not applicable; configuration control | Current authentication configuration export; change history for the period; list of exceptions with approval | Export date, change record date |
| Change management | List of all changes deployed to in-scope systems in the period | Change records with approval before deployment, test evidence, deployment record; emergency change list with retrospective approval | Approval date versus deployment date |
| Backup and restoration | Backup job schedule and failure list for the period | Backup completion reports; failure tickets and resolution; restoration test record with date and result as recorded | Job run dates, test date |
| Vulnerability management | Scan schedule and list of findings open and closed in the period | Scan reports with dates; remediation tickets; exception register with approval | Scan date, closure date |
| Incident management | List of all incidents logged in the period | Incident records with detection, response and closure dates; post-incident review records | Log date, closure date |
| Logging and monitoring | List of monitored systems and alert rules in force | Log retention configuration export; alert review records; alert list for the period as the population; handling notes for the alerts the audit team selects | Configuration date, review date |
| Third party and vendor oversight | List of in-scope vendors and contracts | Due diligence records; contract security clauses; periodic review records; vendor incident notifications | Review date, contract date |
| Security awareness training | List of staff in scope in the period | Training completion report per person with dates; content version delivered; follow-up for non-completion | Completion date, report export date |
| Policy governance | List of policies in scope with review cadence | Approved policy versions with approval records; review log for the period; communication record | Approval date, publication date |
| Physical access | List of secure areas and badge holders | Badge access approval records; access logs for the period; visitor logs; badge revocation records | Log export date, approval date |
| Data retention and disposal | Retention schedule and list of disposal events in the period | Disposal certificates or records; retention configuration export; exception approvals | Disposal date, export date |
| Continuity and recovery testing | Test schedule for the period | Test plan, test record with participants and date, results as recorded, follow-up actions list | Test date, sign-off date |
| Segregation of duties | Role and permission matrix per in-scope system | Conflict analysis report; approved exceptions with compensating control named; remediation tickets | Report date, approval date |
| Encryption and key management | Inventory of in-scope data stores and keys | Encryption configuration export; key rotation records for the period; key custodian assignments | Export date, rotation date |

## Wording rules for examples

- Write each example as something an owner can produce: "export of the account list for <system> as at <period end>, showing the export date".
- Name the period every time. An artefact with no date stamp is requested with the stamp named as a requirement of the request, not assumed.
- For recurring controls, request the population before any items; the auditor selects the sample.
- Never write "this proves", "sufficient", "complete" or "effective" in an example.
- Never draft or mock up an example artefact. The request describes what to send; it never contains a specimen.
