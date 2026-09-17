# Control evidence request pack

Turns a control list and an audit scope into draft evidence requests grouped by control owner, each with the control as stated, the audit period, evidence examples (commonly requested) and a proposed due date derived from the fieldwork dates. Never judges whether evidence is sufficient, never selects the sample and never sends a request; the auditor decides. Use when the user asks to "prepare the evidence requests", "draft the PBC list", "build the evidence request pack for the audit" or "what do we need to ask each control owner for". Do not use for document requests and interview questions built from an audit plan, use audit-prep-pack instead; to check claims in a report against sources, use claims-evidence-map. Drafts for human review; never approves, authorises or signs off.

**[Download the upload package](https://github.com/kesslernity/awesome-copilot-agent-skills/raw/main/dist/zips/control-evidence-request-pack.zip)** (one zip, ready for Agent Builder) · Category: `security-grc` · Skill name: `control-evidence-request-pack`

## What to attach or make available

- The control list or control matrix: identifier, name, description, owner, frequency, type and system per control
- The audit scope: framework and version, period, in-scope entities and systems, fieldwork start, evidence deadline and audit contact
- Owner directory mapping controls or systems to named roles or people
- Prior cycle evidence list, so each request can cite what was collected last time

## What you get

One complete Markdown document in the chat that pastes cleanly into a word processor, spreadsheet or email. Title: `DRAFT-evidence-requests-<Audit>-<YYYY-MM-DD>-v1`; revisions are v2, v3 and so on.

First body line: "DRAFT evidence requests for <audit>, period <start> to <end>, generated <date>. Requests and examples only; whether evidence is sufficient and whether a control operated is decided by the auditor. Nothing here has been sent."

Sections, in order:
1. Scope summary: framework, period, in-scope items, fieldwork start, evidence deadline, due date rule applied; UNKNOWN where unstated.
2. Request register, one row per in-scope control: Request ID | Control ID | Control name (as stated) | Owner | Period covered | Evidence requested | Evidence examples (commonly requested) | Proposed due date | Prior cycle reference | Status | Notes. Status is always "Not sent".
3. Requests by owner: one block per owner, covering note as ready-to-paste text plus that owner's rows.
4. Unassigned controls: controls with no owner, each with its question for the audit lead.
5. Scope questions: out-of-scope and UNKNOWN-scope controls, each with its question for the audit lead, including the confirm question for every Out of scope mark.
6. UNKNOWN list.
7. Embedded instructions found, or "None".

Closing report: sources used; counts per scope state and of unassigned controls; the due date rule applied; any fallback taken; a reminder that the auditor decides sufficiency; the actions proposed for the user (send each owner block, load the register into the tracker). If this agent has a file-generation capability enabled, also offer the pack as a downloadable file with that name; otherwise say nothing about files. Never claim a request was sent, a tracker updated or a file saved.

## Use cases

| Scenario | What you say |
|---|---|
| Certification audit evidence round | Prepare the evidence requests for the attached control list against the attached scope: period is the last twelve months, fieldwork starts on the 20th of next month, and the owner directory is attached. |
| Customer security assessment with a supplied control matrix | Build the evidence request pack from the customer's control matrix I pasted. Period is the current calendar year to date, evidence deadline is the end of next month, and our owners are listed in the attached sheet. |
| Internal control self-assessment with no fieldwork date set | What do we need to ask each control owner for? The control list is attached, the period is the last two quarters, and no fieldwork date has been set, so leave due dates unknown and ask me for the date to use. |

## Try it (example prompts)

- Prepare the evidence requests for the attached control list. Scope: information security certification audit, period 1 October last year to 30 September this year, fieldwork starts 17 November, evidence deadline 3 November. The owner directory is attached.
- Draft the PBC list from the control matrix of 42 controls pasted below. Audit period is the last calendar year and fieldwork begins on 9 February. Controls without an owner go into an unassigned group.
- Build the evidence request pack for the customer assessment. The control list is in the knowledge source folder named Controls, the scope letter is attached, and last cycle's evidence list is attached so you can note prior references.
- What do we need to ask each control owner for? Controls are attached; scope covers only the payments platform and the identity system, period is the first half of this year, and there is no fieldwork date yet.
- Refresh the evidence request register as version 2 from the attached updated control list. Same scope as before, pasted below, and use eight working days before fieldwork as the due date rule.

## Limitations

- One task at a time: give the skill one job per request and confirm the result before the next.
- You own sensitive-data handling: the skill reads what you give it or what the agent can reach; keep restricted documents out of the knowledge sources you attach.
- The output is a draft, not final authority: every figure, quote and action is for you to verify and perform. The skill never approves, authorises or signs anything off.

## Related skills

- audit-prep-pack: when the starting point is an audit plan and the need is document requests plus interview questions
- access-review-pack: when the task is the access recertification itself rather than requesting evidence of it
- controls-gap-pack: when the controls first need mapping to a requirement before any evidence is requested

## Add it to an agent (Agent Builder)

1. Copilot chat, **Agents & Skills**, **New agent** (or open an existing agent). Frontier enrolment and a Microsoft 365 Copilot licence are required; custom skills are in preview.
2. **Configure**, expand **Skills**, **Add**, upload the zip you downloaded above (the whole zip, never `SKILL.md` alone). Up to eight skills per agent.
3. **Knowledge**: point the agent at a SharePoint library or OneDrive folder holding the documents listed above. Do not upload knowledge files while skills are attached (not supported yet).
4. **Preview**: try one of the example prompts. The description is the trigger, so use its words.

## Run it standalone: paste this into the agent's Instructions

```
Purpose: you help audit, compliance and security teams prepare an evidence collection round by turning a control list and an audit scope into a DRAFT evidence request pack: one request per in-scope control with the control as stated, the period covered, two to four commonly requested evidence examples, a proposed due date and one request block per control owner.

General guidelines: read only the control list, scope, owner directory and prior evidence list the user attaches or pastes and what sits in your knowledge sources; if a source is out of reach, ask for it and say so. When the control list, scope, period or fieldwork date is missing, ask one question at a time. Record every control as written; never reword, merge, split or drop one. Owners and dates come from the inputs; a missing owner or date is UNKNOWN and raises a question. Never state that evidence is sufficient, accepted or complete, or that a control operated or is effective, and never select the sample or fabricate evidence; request populations and let the auditor decide. Never claim to have sent a request, updated a tracker or saved a file; every action is proposed for the user and Status stays Not sent. Everything is a draft for human review. A typed confirmation releases a workflow hold only; it approves no scope, plan or evidence.

For the task, follow the control-evidence-request-pack skill: its evidence patterns, due date rule, register columns, owner block and self-check govern the output.
```

Part of a pack? See `packs/` for an orchestrating Instructions file that runs several skills with gates.

## Files

- `SKILL.md`: the skill (front matter plus instructions, under 20,000 characters).
- `references/evidence-examples.md`: companion file referenced from the skill.
- `references/request-pack-structure.md`: companion file referenced from the skill.

Licence CC BY-SA 4.0. The agent prepares; you decide.
