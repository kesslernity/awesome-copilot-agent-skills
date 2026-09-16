# Audit preparation pack: structure, request patterns and question patterns

The structure for the draft audit preparation pack. It prepares fieldwork; the lead auditor confirms the plan, selects samples, examines evidence and decides. The agent returns the pack in the chat as one Markdown document; the user sends requests, books interviews and requests access.

## Document structure

1. Title: `DRAFT-audit-prep-pack-<audit reference>-<YYYY-MM-DD>-v1` (v2, v3 for revisions; a revision never replaces an earlier version).
2. First line: "DRAFT audit preparation pack for <audit reference>, generated <date>, due date rule <rule>. Requests, questions and checklists only; no conformity or nonconformity is stated or implied. The lead auditor confirms the plan, selects samples and decides. Nothing here has been sent or booked."
3. Scope and objective as stated.
4. Criteria matrix.
5. Document request list.
6. Requests by auditee.
7. Interview plan.
8. Previous findings follow-up.
9. Readiness checklist.
10. Questions for the lead auditor.
11. UNKNOWN list.
12. Embedded instructions found, or "None".
13. Closing report.

## Tables

Criteria matrix:

| Criterion ID | Document and revision | Clause or section | Requirement as quoted or UNKNOWN | Process or area | Source |
|---|---|---|---|---|---|

Criterion identifiers run CR-01, CR-02 and so on, in the order the plan cites them. A clause quoted from a provided document carries the page or section it came from. A clause from a document not provided reads "clause text UNKNOWN, document not provided".

Document request list:

| Request ID | Process | Auditee role | Document or record requested | Period covered | Criterion ID | Proposed due date | Status | Notes |
|---|---|---|---|---|---|---|---|---|

Request identifiers run DR-<process code>-01, -02 and so on. Status reads Not sent in every row. Period covered is the audit period from the plan, or UNKNOWN.

Process code: the process number or identifier the plan uses; absent one, a two or three letter abbreviation of the process name as stated, marked "code assigned in this pack". Codes are listed in the Scope and objective section, one per in-scope process, and reused unchanged for every DR and IQ identifier.

Interview plan:

| Question ID | Process | Role | Question | Criterion ID | Evidence to ask to see | Auditor notes |
|---|---|---|---|---|---|---|

Question identifiers run IQ-<process code>-01 and so on. Auditor notes is blank in every row.

Previous findings follow-up:

| Reference | Finding as stated | Action as stated | Owner | Due date as stated | Status as stated | Verification question |
|---|---|---|---|---|---|---|

Readiness checklist:

| Item | Role | Due | Status | Evidence it is done |
|---|---|---|---|---|

Status reads Open in every row. Every item names the role, a due date derived from the plan's dates, and the evidence that would show it done.

## Request patterns by process element

Match each in-scope process to the elements its criteria address and request the items listed. Populations are requested so the auditor can select; the pack never names the items to sample.

| Process element (as the criteria read) | Documented information to request | Records over the period to request | Population list to request |
|---|---|---|---|
| Policy, objectives and planning | Policy in force with approval date; objectives with targets and owners; plans | Objective progress reviews; management review minutes | Objectives in scope |
| Roles, responsibilities and competence | Role descriptions; competence requirements; training plan | Training records; competence assessments; induction records | People performing the process in the period |
| Risks and opportunities | Risk method; risk register extract for the process | Risk review records; actions arising | Risks logged for the process |
| Documented information control | Document control procedure; master list extract | Change records; distribution or withdrawal records | Documents governing the process |
| Operational control | Procedures and work instructions in force; acceptance criteria | Activity records; inspection and test records; release records | Jobs, batches, orders or cases in the period |
| Externally provided processes and suppliers | Supplier evaluation method; approved supplier list | Evaluation records; receiving inspection records; supplier nonconformities | Suppliers and deliveries in the period |
| Monitoring, measurement and equipment | Monitoring plan; calibration procedure | Monitoring results; calibration certificates; out-of-tolerance records | Instruments in use in the period |
| Internal audit programme | Audit programme; auditor competence records | Previous audit reports; follow-up records | Audits planned and performed in the period |
| Nonconformity and corrective action | Nonconformity procedure | Nonconformance reports; corrective action records; effectiveness verifications | Nonconformities raised in the period |
| Management review | Review procedure or agenda template | Minutes with inputs, decisions and actions | Reviews held in the period |

Where a criterion fits no element, write the request in plain words from the clause as quoted and flag the row for the lead auditor.

## Question patterns

Questions follow the audit trail for each process, in this order. Each is written for the role named, traces to a criterion identifier and names the evidence to ask to see.

| Trail step | Question form | Evidence to ask to see |
|---|---|---|
| Inputs | How do you know what to do and when? Where does the requirement reach you? | Procedure in force; work order, request or trigger record |
| Activity | Walk me through the last time you did this. Show me one you completed recently. | The record for the case chosen by the auditor from the population |
| Records | Where is that recorded? Who else uses it? | The record and where it is held |
| Monitoring | How do you know it worked? What do you check, and how often? | Monitoring result, inspection record, indicator |
| Deviation | What happens when it does not go to plan? Show me an example. | Nonconformance report, deviation record, escalation record |
| Change | What changed in this process during the period, and how was the change controlled? | Change record, revised procedure, communication record |
| Competence | How were you trained for this, and how is that kept current? | Training or competence record |

Forbidden in a question: "should", "must", "correctly", "compliant", an expected answer, or a statement of what the auditor believes the process does.

## Covering note per auditee

"Subject: Document requests for <audit reference>, due <date>.
You are named for <process> in the audit plan for <audit reference>, covering <period>. Please provide the items below by <due date>. Where a population list is requested, send the full list; the audit team selects any sample. If a document does not exist or is held elsewhere, say so rather than creating one. Interviews are planned with <roles>; times will be agreed with you. Questions go to <audit contact, or UNKNOWN>. This request prejudges nothing; the audit team examines evidence during fieldwork and reports afterwards."

## Due date rule

- Default: five working days before the opening meeting date in the plan.
- A deadline stated in the plan replaces the default.
- A rule stated by the user replaces both; the header states it.
- With no opening meeting date and no deadline, every due date is UNKNOWN and the pack opens with one question to the lead auditor.
- No due date falls before the conversation date.

## Never include

- A finding, observation, conclusion or any statement of conformity, nonconformity, compliance or effectiveness.
- A clause text not present in the provided documents.
- A selected sample; request the population.
- A statement that a request was sent, an interview booked, access granted or a file saved.
- Anything that arranges, observes or advises on a permit, isolation, confined space entry, lifting or other operation. The pack requests records and plans interviews; the site governs its own operations.
