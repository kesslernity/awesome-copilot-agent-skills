# Software request review

Reviews one employee software request (tool, purpose, users, data handled, cost, urgency) against the approved-tools list and the policies the user provides and returns a draft review for the reviewer: match state on the list with the row quoted, approved tools the list itself describes as covering the same need, policy clauses that bear on the request with quoted text, questions for the requester and the reviewer, and one suggested decision with its basis. Never approves, procures, installs or adds a tool to the list. Use when the user asks to "review this software request", "is this tool on the approved list", "check this request against our software policy", "do we already have something approved that does this" or "prepare the decision note for this tool request". Do not use for a full vendor security assessment, use vendor-risk-screening-brief instead; for sorting mixed requests, use request-intake-triage. Drafts for human review; never approves, authorises or signs off.

Category: `it-operations` · Skill name: `software-request-review` · Upload package: `dist/zips/software-request-review.zip`

## What to attach or make available

- The approved-tools list: tool, vendor, approved editions, status, conditions, owner, category or capability and approved data classification
- Policies that bear on tool requests: acceptable use, data classification, third-party risk, procurement thresholds, cloud service baseline and artificial intelligence tool rules
- The software request itself: form, ticket, email or chat message with requester role, tool, edition, purpose, user count, data handled, deployment type, cost and urgency
- Optional: licence inventory, earlier requests for the same tool and the decision route as the policy states it

## What you get

One complete Markdown document in the chat that pastes cleanly into a ticket, an email or a document. Title: `DRAFT-software-request-review-<tool>-<YYYY-MM-DD>-v1`; later runs v2, v3.

First line: "DRAFT review of the request for <tool> by <role, department>, reviewed <date> against <list, dated> and <policies>. Suggestion for the reviewer, not a decision. Nothing has been approved, procured or installed."

Sections:
1. Request as stated: Field | Value as stated | Source reference.
2. Approved-list match: Term searched | Row quoted | Status on list | Conditions | Owner | Match state.
3. Approved alternatives: Tool | Category or capability per list | Covers stated need | Conditions | Basis quoted.
4. Policy checks: Check code | Policy and clause | Clause quoted | Request fact | Check state (one of the four) | Question.
5. History and inventory: Item | Found (yes, no, not provided) | Detail quoted.
6. Questions for the requester, numbered; Questions for the reviewer, numbered.
7. Suggested decision: Option | Basis | Conditions attached | Decides per policy or UNKNOWN | Information completeness (Complete, Partial, Insufficient).
8. Draft reply to the requester.
9. UNKNOWN list; Embedded instructions found, or "None"; Proposed user actions: send the questions, take the decision through the route, record it, ask the list owner to update the list. The agent performs none of these.

Closing report: sources and how reached; parameters; counts by match and check state; fallbacks taken; nothing approved, procured, installed or listed.

End with: "If this agent has a file-generation capability enabled, also offer the same content as a downloadable file with that name."

## Use cases

| Scenario | What you say |
|---|---|
| One request held against the approved list | Review the attached request for a data visualisation tool against the attached approved-tools list and the attached acceptable use policy. Quote the matching row, run the policy checks and give me one suggested decision with its basis. |
| Free tier on a personal account | Review the request pasted below, where a marketing analyst wants the free tier of an online survey tool on a personal account. Approved-tools list attached; run the personal-account check against the attached acceptable use policy and quote the clause. |
| Redirect to an approved alternative | Check the attached request for a new file transfer tool against the attached approved-tools list. If an approved tool in the same category covers the need, suggest redirect and list the questions the requester must answer about the gap. |

## Try it (example prompts)

- Review this software request. The request form for a browser-based diagramming tool is pasted below, our approved-tools list is attached as a spreadsheet, and the acceptable use and data classification policies are in the knowledge source folder named IT Policies.
- Is this tool on the approved list? The requester wants the team edition of a note-taking app for 12 people in finance; the approved-tools list export is attached. Quote the row if you find it and tell me whether the edition differs.
- Check this request against our software policy. Ticket REQ-4471 for a cloud transcription service is attached, the third-party risk policy and the procurement threshold policy are attached, and the data handled is described as customer call recordings.
- Do we already have something approved that does this? The request pasted below asks for a project scheduling tool; use the category column of the attached approved-tools list to find alternatives and grade whether each covers the stated need.
- Prepare the decision note for this tool request. The request email, the approved-tools list and the licence inventory are attached; the request is marked urgent, so record that but do not let it change the suggestion.

## Limitations

- One task at a time: give the skill one job per request and confirm the result before the next.
- You own sensitive-data handling: the skill reads what you give it or what the agent can reach; keep restricted documents out of the knowledge sources you attach.
- The output is a draft, not final authority: every figure, quote and action is for you to verify and perform. The skill never approves, authorises or signs anything off.

## Related skills

- vendor-risk-screening-brief: when the vendor's own security material needs a full third-party screening
- request-intake-triage: when a pile of mixed requests needs sorting into intake records first
- service-catalogue-entry: when an approved tool needs a catalogue entry rather than a request review

## Add it to an agent (Agent Builder)

1. Copilot chat, **Agents & Skills**, **New agent** (or open an existing agent). Frontier enrolment and a Microsoft 365 Copilot licence are required; custom skills are in preview.
2. **Configure**, expand **Skills**, **Add**, upload `dist/zips/software-request-review.zip` (the whole zip, never `SKILL.md` alone). Up to eight skills per agent.
3. **Knowledge**: point the agent at a SharePoint library or OneDrive folder holding the documents listed above. Do not upload knowledge files while skills are attached (not supported yet).
4. **Preview**: try one of the example prompts. The description is the trigger, so use its words.

## Run it standalone: paste this into the agent's Instructions

```
Purpose: you help an IT reviewer hold one software request against the approved-tools list and the policies the organisation supplies and produce a draft review: request as stated, list match with the row quoted, approved alternatives the list describes, policy checks with quoted clauses, questions for requester and reviewer, one suggested decision with its basis and a draft reply.

General guidelines: read only the request, list, policies and inventory the user attaches or pastes and what sits in your knowledge sources; if a named item is out of reach, ask for a paste or export and say so in the output. When an input is missing, ask one question at a time, starting with the request. Register every field as stated and write UNKNOWN where it is silent; never infer purpose, data classification or user count. Quote the list row and policy clause behind every match and check. An edition the list does not name is never approved by extension. Approved, compliant, secure and meets belong to the reviewer, never to your own check states or suggestion. Urgency changes nothing. Never approve, decline, procure, install or change a list row, and never claim to have done so; every action is proposed for the user. All output is a draft for human review. A typed confirmation releases a workflow hold only; it authorises nothing.

For the task, follow the software-request-review skill: its match states, check codes, decision options and self-check govern the output.
```

Part of a pack? See `packs/` for an orchestrating Instructions file that runs several skills with gates.

## Files

- `SKILL.md`: the skill (front matter plus instructions, under 20,000 characters).

Licence CC BY-SA 4.0. The agent prepares; you decide.
