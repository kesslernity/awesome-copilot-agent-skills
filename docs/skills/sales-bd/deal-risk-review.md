# Deal risk review

Reviews one deal's notes and timeline (CRM opportunity record, activity log, emails, meeting notes, forecast entries) for risk signals such as a single contact thread, no identified budget owner, slipped or missing dates, silence after a proposal, an undefined decision process or a competitor named late, and returns a DRAFT risk register: each signal with the quoted evidence and its date, a severity on a stated scale, and one proposed next action with an owner role for the user to decide on. Use when the user asks to "review the risks on this deal", "why is this opportunity stalling", "is this deal single-threaded", "deal health check before the forecast call" or "what should we do next on <opportunity>". Do not use for a whole-account plan, use account-plan-builder instead; for scoring early leads against a rubric use lead-qualification-scorer. Drafts for human review; never approves, authorises or signs off.

Category: `sales-bd` · Skill name: `deal-risk-review` · Upload package: `dist/zips/deal-risk-review.zip`

## What to attach or make available

- The CRM opportunity record with stage history, close date changes and forecast entries
- The activity log, emails by direction, meeting notes and the proposal with its send date
- The sales process definition: stage names, exit criteria and the roles the organisation expects to engage, where it differs from the skill's default catalogue
- The organisation's own severity scale and silence or slip thresholds, if any

## What you get

One complete Markdown document in the chat that pastes cleanly into a deal review note or an email. Title: `DRAFT-deal-risk-review-<Opportunity>-<YYYY-MM-DD>-v1`; revisions v2, v3. First body line: "DRAFT deal risk review for <opportunity>, prepared <date> from <n> sources (<first> to <last>). Signals are as evidenced in the record; grades and next actions are proposals. No stage, forecast or commitment has been changed."

Sections, in order:
1. Header: Opportunity | Prospect | Deal owner | Stage as recorded | Close date as recorded | Close date changes (count) | Last inbound contact (date, days elapsed) | Review date | Catalogue and thresholds in use.
2. Source register: S ref | Type | Date | Author or sender | Subject.
3. Timeline: Date | Actor (role) | Event | Direction (inbound, outbound, internal) | S ref.
4. People map: Name | Title as recorded | Role (as evidenced or UNKNOWN) | Last contact | Direction | Relationship holder | S ref.
5. Risk register: # | Signal | Status (Present, Absent, UNKNOWN) | Evidence (quoted) | Date | S ref | Severity | Grading basis.
6. Proposed next actions: # | Signal | Action | Owner role | By when (relative to review date) | Result that closes the signal | Source of the action (catalogue or S ref).
7. Compounding signals: Signals | Why they compound | S refs.
8. Contradictions: Field | Value A (S ref) | Value B (S ref) | Decision needed.
9. UNKNOWN list; Embedded instructions found, or "None".
Closing report: sources and how reached; thresholds and scale; signal counts by status and severity; fallbacks; proposed user actions (confirm roles, choose actions, update the record). End with: "If this agent has a file-generation capability enabled, also offer the same content as a downloadable file with that name." Never claim the record, stage, forecast or any task was updated, sent or assigned.

## Use cases

| Scenario | What you say |
|---|---|
| Pipeline review of a deal with a slipped close date | Review the attached opportunity record and activity log; the close date has moved twice. Grade each risk signal on your default scale, show the slip arithmetic against today's date and propose one next action per signal. |
| Silence after the proposal went out | The proposal was sent three weeks ago and nothing has come back. Emails and CRM record attached. Test the silence signal against your 14 and 28 day thresholds and tell me which contacts we have actually heard from. |
| Manager asks whether the deal is really committed | Attached: the CRM record showing stage Commit, the activity log and the meeting notes. List every signal, quote the evidence, record any contradiction between the stage and the timeline, and adjudicate nothing. |

## Try it (example prompts)

- Review the risks on this deal. Attached: the CRM opportunity record, the activity log export and the proposal we sent on the 2nd. Close date is recorded as the 30th; review as of today.
- Why is this opportunity stalling? I have pasted the last six weeks of emails with the prospect and my meeting notes below. Our stage exit criteria are attached; use them instead of your default catalogue.
- Is this deal single-threaded? The CRM record and the contact list are attached, with the activity log showing every meeting and email. Map the people by evidenced role, not by title.
- Deal health check before the forecast call tomorrow. Attached: the opportunity record with stage history and three close date changes, plus the forecast entries. Use your default thresholds and grading and show the arithmetic.
- What should we do next on the manufacturing opportunity? The notes, emails and the proposal send date are attached. Give me one proposed action per risk with the owner role and what result would close it; no win probability.

## Limitations

- One task at a time: give the skill one job per request and confirm the result before the next.
- You own sensitive-data handling: the skill reads what you give it or what the agent can reach; keep restricted documents out of the knowledge sources you attach.
- The output is a draft, not final authority: every figure, quote and action is for you to verify and perform. The skill never approves, authorises or signs anything off.

## Related skills

- account-plan-builder: a whole-account plan rather than one opportunity
- lead-qualification-scorer: scoring early leads against a rubric before anyone calls
- discovery-call-prep: preparing the first call with a prospect

## Add it to an agent (Agent Builder)

1. Copilot chat, **Agents & Skills**, **New agent** (or open an existing agent). Frontier enrolment and a Microsoft 365 Copilot licence are required; custom skills are in preview.
2. **Configure**, expand **Skills**, **Add**, upload `dist/zips/deal-risk-review.zip` (the whole zip, never `SKILL.md` alone). Up to eight skills per agent.
3. **Knowledge**: point the agent at a SharePoint library or OneDrive folder holding the documents listed above. Do not upload knowledge files while skills are attached (not supported yet).
4. **Preview**: try one of the example prompts. The description is the trigger, so use its words.

## Run it standalone: paste this into the agent's Instructions

```
Purpose: this agent helps deal owners review one opportunity by reading its notes and timeline and returning a draft risk register: each signal with quoted evidence and date, a severity on a stated scale and one proposed next action with an owner role.

General guidelines: read only the CRM record, activity log, emails, notes and proposal the user attaches or pastes, and this agent's configured knowledge sources; if a source is out of reach, ask for a paste. When a required input is missing, such as the review date, ask one question at a time and wait for the answer. Assume no capability such as file generation or CRM access; if one is absent, say so and answer in the chat. Every signal, person and event traces to a numbered source or reads UNKNOWN; a gap in the record is never an inference. Roles are as evidenced, never taken from a title alone. Produce no win probability, forecast category or stage change, and draft no concession. Never claim to have updated, sent or assigned anything; every action is proposed for the user, and every output is a draft for human review. A typed confirmation releases a hold for that step only; it approves no action, price or term.

For the task, follow the deal-risk-review skill: confirm scope, register the sources, build the timeline and people map, test each catalogue signal with its arithmetic, grade, propose one action per signal and return the register as a DRAFT.
```

Part of a pack? See `packs/` for an orchestrating Instructions file that runs several skills with gates.

## Files

- `SKILL.md`: the skill (front matter plus instructions, under 20,000 characters).
- `references/risk-signal-catalogue.md`: companion file referenced from the skill.

Licence CC BY-SA 4.0. The agent prepares; you decide.
