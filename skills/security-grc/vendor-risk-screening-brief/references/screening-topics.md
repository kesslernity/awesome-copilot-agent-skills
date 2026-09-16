# Screening topics, evidence statuses and artefact guide

Defaults for the vendor risk screening brief. The organisation's own topic list replaces the default list when supplied. Nothing here rates a vendor; the tables define what counts as evidence and what to ask for when it is absent.

## Default screening topics

| No. | Topic | What it covers | Artefact that normally evidences it | If only an answer exists |
|---|---|---|---|---|
| 1 | Governance and policies | Security policy set, ownership, review cycle | Policy index with approval dates, management review record | Asserted |
| 2 | Certifications and independent assurance | Certificates and assurance reports, their scope and period | The certificate itself; the report with scope and exceptions sections | Asserted |
| 3 | Identity and access control | Joiner, mover and leaver process, multi-factor authentication, privileged access, access reviews | Access control policy, access review record extract, control listing in an assurance report | Asserted |
| 4 | Data protection and encryption | Classification, encryption at rest and in transit, key management | Encryption standard, key management description, report control listing | Asserted |
| 5 | Data location and subcontractors | Hosting regions, subcontractor or subprocessor list, transfer mechanism | Dated subcontractor list, hosting description, data processing extract | Asserted |
| 6 | Secure development and change | Development lifecycle, code review, change control, environment separation | Development policy, change record sample, report control listing | Asserted |
| 7 | Vulnerability and patch management | Scanning, patch timescales, penetration testing | Penetration test summary with date and scope, patch policy | Asserted |
| 8 | Logging, monitoring and detection | Log retention, monitoring, alerting | Logging standard, report control listing | Asserted |
| 9 | Incident management and notification | Response plan, customer notification commitment and timing | Response plan or summary, contract notification clause | Asserted |
| 10 | Business continuity and disaster recovery | Plans, recovery objectives, test evidence | Plan summary, last test date and result summary | Asserted |
| 11 | Personnel security | Pre-employment screening, training, confidentiality | Personnel security policy, training completion statement | Asserted |
| 12 | Physical and environmental security | Data centre controls, own or provider | Provider assurance report or attestation, physical security policy | Asserted |
| 13 | Privacy and regulatory | Privacy notice, data processing terms, data subject request handling, retention | Data processing extract, retention schedule, privacy policy | Asserted |
| 14 | Contract and commercial protections | Liability, insurance, audit rights, termination, data return | Contract extract, insurance certificate | Asserted |

## Evidence status definitions

Assign exactly one status per topic. A topic that meets part of Evidenced and part of another status takes the weaker status.

| Status | Conditions | Note cell |
|---|---|---|
| Evidenced | A document (not only a questionnaire answer) covers the topic, its scope matches the service in question (Same or Broader), and its date sits inside the freshness window or the certificate is unexpired | Document, reference, date |
| Partial | A document covers part of the topic; or the whole topic but with scope Broader and a qualification; or the document is outside the window | Name the part covered and the part not covered |
| Asserted | The only support is a questionnaire answer, a policy statement of intent, a web page extract or marketing text | "answer only" or "marketing text" |
| Contradicted | Two items in the material disagree on the topic | Quote both, with references |
| Missing | No answer and no document | "no answer, no document" |
| Declared not applicable | The vendor states the topic does not apply | Reason as stated, or UNKNOWN |

A "yes", "in place" or "fully compliant" answer without a document is Asserted. "Planned", "in progress" and "partially" transfer as stated and never count as Evidenced.

## Scope match

| Scope match | Meaning | Effect on status |
|---|---|---|
| Same | The document names the product, entity, sites and region the engagement concerns | None |
| Broader | The document covers a wider scope that includes the engagement | Evidenced with a note, or Partial where the document qualifies the wider scope |
| Different | The document covers another product, entity or region | Asserted at best; near match noted |
| UNKNOWN | The scope statement is absent, cropped, illegible or in a language the agent cannot read | Partial at best; question to the vendor |

## Certificate fields to record

Standard or scheme named; issuing body as stated; certificate identifier; issue date; expiry date; scope statement quoted in full; sites, entities or regions listed; version or edition of the standard as stated; language of the copy; whether the copy is complete. Record every field as stated. Validity, authenticity and the issuing body's accreditation are never checked and the brief says "verified: no, as stated only".

## Assurance report and test summary fields to record

Report type exactly as the report names it; period covered or test date; scope statement quoted; systems, locations and services in scope; count of exceptions, deviations or findings as stated; quoted headings of each; management responses as stated; controls the report expects the customer to operate; sections present and sections missing from the copy; whether the copy is a full report, a summary letter or a bridge letter. A finding is closed only where the material shows the closure with a date.

## Vendor question template

"Topic <number>, <topic>. Please provide <artefact type>, covering <product or service and region> for <period or as at date>. Reason: your submission <states, omits or contradicts> <quoted or summarised item, with reference>."

Group questions by topic in the default order. One artefact per question. Never ask the vendor to confirm a conclusion; the brief draws none. Ask for the artefact, not agreement.
