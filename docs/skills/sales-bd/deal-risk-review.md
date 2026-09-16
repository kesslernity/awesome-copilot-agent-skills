# Deal risk review

Reviews one deal's notes and timeline (CRM opportunity record, activity log, emails, meeting notes, forecast entries) for risk signals such as a single contact thread, no identified budget owner, slipped or missing dates, silence after a proposal, an undefined decision process or a competitor named late, and returns a DRAFT risk register: each signal with the quoted evidence and its date, a severity on a stated scale, and one proposed next action with an owner role for the user to decide on. Use when the user asks to "review the risks on this deal", "why is this opportunity stalling", "is this deal single-threaded", "deal health check before the forecast call" or "what should we do next on <opportunity>". Do not use for a whole-account plan, use account-plan-builder instead; for scoring early leads against a rubric use lead-qualification-scorer. Drafts for human review; never approves, authorises or signs off.

Category: `sales-bd` · Skill name: `deal-risk-review` · Upload package: `dist/zips/deal-risk-review.zip`

## What to attach or make available

Ask once for whatever is missing, in one message, then proceed with UNKNOWN.
1. Deal material: CRM opportunity record and activity log, emails, meeting notes, the proposal and its send date, forecast entries, stage history. Attached, pasted, or reachable through this agent's configured knowledge sources, mail or CRM access. Out of reach: ask for a paste or export and say so in the output.
2. Deal identifiers: opportunity name, prospect organisation, deal owner, current stage and close date as recorded. Missing: UNKNOWN.
3. Review date. Default: the conversation date; all elapsed-time arithmetic uses it.
4. Sales process definition: stage names, exit criteria and the roles the organisation expects to engage. Default: the role vocabulary and signal catalogue in references/risk-signal-catalogue.md, labelled "default catalogue".
5. Severity scale. Default: High, Medium, Low as defined in the reference; the user's own scale replaces it when supplied.
6. Silence and slip thresholds. Default: no inbound contact from the prospect for 14 calendar days is a silence signal, escalating to High past 28 days; a close date moved twice, by more than 30 days in total, or already past at the review date, is a slip signal; legal or procurement not engaged within 30 days of the recorded close date escalates signal 13 to Medium. A user-supplied threshold set replaces all four.
Reference files in this skill: references/risk-signal-catalogue.md, read at step 5 for the signal definitions, evidence tests and candidate next actions, and at step 6 for the severity definitions.

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

## Limitations

- One task at a time: give the skill one job per request and confirm the result before the next.
- You own sensitive-data handling: the skill reads what you give it or what the agent can reach; keep restricted documents out of the knowledge sources you attach.
- The output is a draft, not final authority: every figure, quote and action is for you to verify and perform. The skill never approves, authorises or signs anything off.

## Add it to an agent (Agent Builder)

1. Copilot chat, **Agents & Skills**, **New agent** (or open an existing agent). Frontier enrolment and a Microsoft 365 Copilot licence are required; custom skills are in preview.
2. **Configure**, expand **Skills**, **Add**, upload `dist/zips/deal-risk-review.zip` (the whole zip, never `SKILL.md` alone). Up to eight skills per agent.
3. **Knowledge**: point the agent at a SharePoint library or OneDrive folder holding the documents listed above. Do not upload knowledge files while skills are attached (not supported yet).
4. **Preview**: try one of the example prompts. The description is the trigger, so use its words.

## Run it standalone: paste this into the agent's Instructions

```
You are an assistant that runs one job: deal risk review. Reviews one deal's notes and timeline (CRM opportunity record, activity log, emails, meeting notes, forecast entries) for risk signals such as a single contact thread, no identified budget owner, slipped or missing dates, silence after a proposal, an undefined decision process or a competitor named late, and returns a DRAFT risk register: each signal with the quoted evidence and its date, a severity on a stated scale, and one proposed next action with an owner role for the user to decide on. Use when the user asks to "review the risks on this deal", "why is this opportunity stalling", "is this deal single-threaded", "deal health check before the forecast call" or "what should we do next on <opportunity>". Do not use for a whole-account plan, use account-plan-builder instead; for scoring early leads against a rubric use lead-qualification-scorer. Drafts for human review; never approves, authorises or signs off. Use the deal-risk-review skill for every request that matches its description; if a request falls outside it, say so and stop. Read only what the user attaches or pastes and what sits in your knowledge sources; never claim to have saved, sent, moved or deleted anything, propose the action for the user instead. Where an input is missing, write UNKNOWN and name what would close it; never invent a value. Return complete Markdown the user can paste into their tools, and offer the same content as a file if you can produce one. A typed approval releases a hold in the workflow and is logged; it is not an authorisation. You prepare; the user decides.
```

Part of a pack? See `packs/` for an orchestrating Instructions file that runs several skills with gates.

## Files

- `SKILL.md`: the skill (front matter plus instructions, under 20,000 characters).
- `references/risk-signal-catalogue.md`: companion file referenced from the skill.

Licence CC BY-SA 4.0. The agent prepares; you decide.
