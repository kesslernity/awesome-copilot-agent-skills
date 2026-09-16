# Blameless language rules

Applied to every sentence the agent writes in the postmortem. Quoted evidence is reproduced as written, in quotation marks, with its reference; the rules below govern the agent's own text only. Where a quote names a person, the name is replaced by the role in square brackets, and the substitution is counted in the report.

## Name to role mapping

Map each person to the role they held during the incident, as the sources show it. Use the organisation's role names where the sources use them. Otherwise use this list.

| Role | Assign when the sources show the person |
|---|---|
| Incident commander | Coordinating the response, assigning tasks, declaring status |
| On-call engineer | Paged or responding first for the affected service |
| Service owner | Named as owning the affected service or product |
| Subject expert | Engaged for a specific system, brought in by escalation |
| Communications lead | Writing status page updates or customer notices |
| Reporting user | Raising the first report from outside the response team |
| Approver | Approving a change, rollback or emergency action |
| Responder A, B, C | Any participant whose role cannot be determined |

One person who held two roles in sequence is described by the role held at that moment. The mapping table stays out of the document; it appears in the report only if the user asks for it.

## Words and phrases the agent does not write

| Do not write | Write instead |
|---|---|
| X failed to, X forgot, X missed | The <check or step> did not occur (source, reference) |
| X should have | The review may consider whether <step> would have changed the outcome |
| Human error, operator error, user error | The specific condition: for example, the runbook step was not present; the alert threshold was not set |
| Root cause, the cause was | Candidate factor; the evidence points to |
| Fault, blame, negligent, careless, incompetent | Do not use; describe the event and its evidence |
| Obviously, clearly, simply | Do not use |
| Would have prevented | The review may consider whether <action> reduces the likelihood or the impact of <factor> |
| X made a mistake | <Action> was taken at <time>; its outcome as stated was <outcome> |

## Counterfactuals

A counterfactual ("if the deployment had been rolled back at 10:05") is a question for the review, not a statement in the draft. Place it under Open questions, phrased as "Should the response include <action> when <condition>?", with the evidence line it arises from.

## Hypotheses

A cause voiced during the incident ("I think it's the cache") is recorded as a candidate factor with status "stated by responder" and the quote with its reference. The draft never upgrades a hypothesis to a finding, even when the responders agreed among themselves in the channel. Agreement in the channel is recorded as "agreed by responders in channel at <time>", which is still a hypothesis until the review meeting confirms it.

## Praise and criticism

What went well and What was difficult name practices, tools, decisions and conditions with references. They do not name or rate individuals or teams. "The on-call engineer responded quickly" becomes "Detection to first response: <duration>, basis shown in Key durations".

## Sensitive content

Credentials, tokens, session identifiers, customer personal data, and messages unrelated to the incident are not reproduced. Each such item is named under UNKNOWN as "redacted content at <reference>", and the report proposes that the user redact the export before circulation.
