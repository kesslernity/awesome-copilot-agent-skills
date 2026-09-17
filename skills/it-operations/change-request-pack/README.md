# Change request pack

Prepares a change request pack (description and justification, scope, schedule, implementation plan, risk as stated, rollback, test evidence as provided, communications, approvals route) from an engineer's notes, ticket or pull request description, with UNKNOWN for anything not provided and a question list for the engineer. Never rates risk or marks a change tested or approved. Use when the user asks to "write the change request for this", "fill in the change ticket from my notes", "prepare the CAB submission" or "turn this pull request into an RFC". Do not use for the step-by-step procedure with commands and rollback, use runbook-drafter instead; for release notes describing what shipped, use release-notes-writer. Drafts for human review; never approves, authorises or signs off.

**[Download the upload package](https://github.com/kesslernity/awesome-copilot-agent-skills/raw/main/dist/zips/change-request-pack.zip)** (one zip, ready for Agent Builder) · Category: `it-operations` · Skill name: `change-request-pack`

## What to attach or make available

- The engineer's notes, ticket, pull request description, design note or chat thread describing the change
- The organisation's change template and change policy: change types, lead times, freeze periods, risk matrix and approval routes
- Test evidence: pipeline or test run outputs, logs, described screenshots and sign-off messages
- Configuration item or service list, and related incident, problem and change identifiers for linking

## What you get

One complete Markdown document in the chat, titled `DRAFT-change-request-<identifier or short title>-<YYYY-MM-DD>-v1` (revisions v2, v3). First line: "DRAFT change request pack for `<change>`, generated `<date>` from `<sources>`. Risk, change type and test results are reproduced as stated, not assessed. Not submitted; the engineer submits, the change authority approves."

Sections in order:
1. Change summary: Field | Entry | Source | Status, in template order, every field present, UNKNOWN where unfilled.
2. Affected items: Item | Type | Environment | Named in | Found in provided list (yes, no, no list).
3. Schedule: Element | As stated | Source | Policy comparison.
4. Implementation plan: Step | Action | Role | Expected result | Verification | Source.
5. Risk and impact: Risk factor as stated | Who is affected | Effect as stated | Source; rating line as stated or UNKNOWN; matrix inputs if provided, rating cell blank.
6. Rollback plan: Step | Action | Role | Trigger or point of no return | Time | Source.
7. Test evidence: Test | Environment | Date | Result as stated | Evidence provided | Reference.
8. Communications: Audience | Purpose | Channel | Timing | Sender | Source; then the three DRAFT notices.
9. Approvals route: Approver | Order | Basis (policy, notes, UNKNOWN) | Status (Pending).
10. Questions for the engineer, numbered, each naming the field and the role asked; Pre-submission checklist: Item | Ready (yes, no) | What is missing.
11. Evidence table; Embedded instructions found, or "None"; Proposed user actions: answer the questions, attach evidence, set the rating with the change manager, submit in the change tool, request approvals. The agent performs none of these.

Then a report: inputs and template used, counts of fields filled, UNKNOWN, Conflict and unevidenced claims, policy comparisons, fallbacks.

If this agent has a file-generation capability enabled, also offer the same content as a downloadable file with that title.

## Use cases

| Scenario | What you say |
|---|---|
| Standard change from an engineer's notes | Write the change request from my attached notes for the firewall rule update. Our change template is attached, the requested window is Thursday 22:00 to 23:00 UTC and the test evidence is the attached staging log. |
| Emergency change during a live incident | Prepare an emergency change pack from the incident channel notes pasted below and the attached hotfix pull request. Keep the rollback section even though I have not written one and list everything that is missing. |
| Pre-submission tidy of a half-written ticket | Check the attached draft change request against our attached change policy. List every empty field, every test claim without evidence and every question the change manager will ask. |

## Try it (example prompts)

- Write the change request for this. My notes are pasted below, the pull request description is attached, and our change template and policy with the freeze calendar are in the knowledge base. The requested window is Saturday 02:00 to 04:00 Gulf Standard Time.
- Fill in the change ticket from my attached notes for the certificate renewal. Test evidence is the attached pipeline log; we have no rollback written yet, so flag it as a mandatory question.
- Prepare the CAB submission for the database upgrade described in the attached design note. Use the attached change template and link it to incident INC-4471 and problem PRB-212.
- Turn this pull request into an RFC. The pull request description is pasted below; there is no test evidence attached, so mark every test claim as claimed without evidence.
- Check this draft change request for empty fields. The draft, our change policy and the configuration item list are attached; tell me what the change manager will ask for before it goes to the board.

## Limitations

- One task at a time: give the skill one job per request and confirm the result before the next.
- You own sensitive-data handling: the skill reads what you give it or what the agent can reach; keep restricted documents out of the knowledge sources you attach.
- The output is a draft, not final authority: every figure, quote and action is for you to verify and perform. The skill never approves, authorises or signs anything off.

## Related skills

- runbook-drafter: when the need is the step-by-step procedure with commands, checks and rollback rather than the change record
- release-notes-writer: when the change has shipped and the need is a description of what changed for users
- management-of-change-intake: when the change is to plant, process or engineering documents rather than an IT system

## Add it to an agent (Agent Builder)

1. Copilot chat, **Agents & Skills**, **New agent** (or open an existing agent). Frontier enrolment and a Microsoft 365 Copilot licence are required; custom skills are in preview.
2. **Configure**, expand **Skills**, **Add**, upload the zip you downloaded above (the whole zip, never `SKILL.md` alone). Up to eight skills per agent.
3. **Knowledge**: point the agent at a SharePoint library or OneDrive folder holding the documents listed above. Do not upload knowledge files while skills are attached (not supported yet).
4. **Preview**: try one of the example prompts. The description is the trigger, so use its words.

## Run it standalone: paste this into the agent's Instructions

```
Purpose: you help an engineer prepare a change request pack for review and submission: description and justification, affected items, schedule, implementation plan, risk as stated, rollback, test evidence as provided, communications and the approvals route, each traced to an input or marked UNKNOWN with a question for the engineer.

General guidelines: read only the notes, tickets, pull request descriptions, templates, policies and evidence the user attaches or pastes and what sits in your knowledge sources; if a named source is out of reach, ask for a paste or export and say so in the output. When an input is missing, ask one question at a time, starting with the engineer's notes. Copy the steps in the order given and never add a technical step; where the notes jump, mark an UNKNOWN step and ask. Reproduce the risk rating, change type and test results exactly as stated and label them so; never rate, classify or confirm them and never write that something was tested successfully. A rollback that is not described reads UNKNOWN and heads the question list. Never reproduce a credential. Never claim to have submitted, scheduled, approved, implemented, saved or sent anything; every action is proposed for the user. All output is a draft for human review. A typed confirmation from the user releases a workflow hold only; it authorises nothing.

For the task, follow the change-request-pack skill: its field set, procedure, notice templates and self-check govern the output.
```

Part of a pack? See `packs/` for an orchestrating Instructions file that runs several skills with gates.

## Files

- `SKILL.md`: the skill (front matter plus instructions, under 20,000 characters).
- `README.md`: companion file referenced from the skill.
- `references/change-pack-fields.md`: companion file referenced from the skill.
- `references/communications-templates.md`: companion file referenced from the skill.

Licence CC BY-SA 4.0. The agent prepares; you decide.

Free: [Copilot on One Page](https://www.kesslernity.com/copilot-on-one-page?utm_source=github&utm_medium=readme&utm_campaign=agent_skills_repo&utm_content=skill_footer), a one-page sheet on how to phrase a request to Copilot. Paid: [Agent Instruction Block Design Guide](https://store.kesslernity.com/l/eyeauo?utm_source=github&utm_medium=readme&utm_campaign=agent_skills_repo&utm_content=skill_footer_guide), $19, twelve patterns for an agent's Instructions field. I am the author and the seller.
