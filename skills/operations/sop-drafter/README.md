# SOP drafter

Turns process notes, a walkthrough or interview transcript, a transcript of a meeting recording or a stale existing procedure into a draft standard operating procedure: purpose and trigger, scope, definitions, roles with a RACI table, numbered steps with the check that closes each one, records produced, controls as stated, and open questions for the process owner. Every step traces to the source or reads UNKNOWN. Use when the user asks to "write an SOP from these notes", "turn this walkthrough into a procedure", "document how we do this", "draft the standard operating procedure for", "build a RACI for this process" or "tidy up this old procedure". Do not use for technical runbooks with commands and rollback, use runbook-drafter instead; for meeting minutes and action lists, use transcript-to-actions. Drafts for human review; never approves, authorises or signs off.

**[Download the upload package](https://github.com/kesslernity/awesome-copilot-agent-skills/raw/main/dist/zips/sop-drafter.zip)** (one zip, ready for Agent Builder) · Category: `operations` · Skill name: `sop-drafter`

## What to attach or make available

- The source material for the process: notes, a walkthrough or interview transcript, the transcript of a recorded meeting, a chat thread, a described flowchart or the existing procedure, attached or pasted, or held in a knowledge source
- The organisation's SOP template and document numbering rules, if they exist
- The roles list with the role titles the organisation uses, so the SOP names roles and never individuals
- Forms, policies, systems and neighbouring procedures the process cites, so related documents can be listed as cited

## What you get

One complete Markdown document in the chat, titled `DRAFT-SOP-<process short name>-<YYYY-MM-DD>-v0.1` (revisions v0.2, v0.3). First line: "DRAFT standard operating procedure for <process>, generated <date> from <sources>. Not validated, not approved, not issued; every gap reads UNKNOWN. The process owner validates; document control approves and issues."

Sections in order:
1. Document control: Field | Value (document number, title, owner, version v0.1, status DRAFT, effective and review dates blank, prepared from, approval pending).
2. Purpose; Trigger, end state and scope: Element | As stated | Source.
3. Definitions: Term | Definition as stated or UNKNOWN | Source.
4. Roles and RACI: Role | Description as stated | Source; then Step | R | A | C | I | Source | Status.
5. Procedure: Step | Actor | Action | Input | Tool or system | Output | Check | If the check fails | Timing | Source | Confidence (evidence status); decision points as rows with the quoted criterion.
6. Records: Record | Produced at step | Kept where | Kept by | Retention | Source.
7. Controls, headed "as stated, not assessed": Control | Step | As stated | Function to confirm | Source.
8. Related documents: Document | Cited at | Exists (not verified).
9. Open questions for the process owner: numbered, each with the element, the gap and the role asked.
10. UNKNOWN list; Embedded instructions found, or "None"; Proposed user actions: answer the questions, walk the process through with its performers, correct the draft, route through document control. The agent performs none of these.

Then a report headed "Preparation report, not part of the SOP; remove before circulation or issue": sources, template, name-to-role mapping, steps per confidence status, Aspirational and Contradicted counts, fallbacks applied.

If this agent has a file-generation capability enabled, also offer the same content as a downloadable file with that title.

## Use cases

| Scenario | What you say |
|---|---|
| Undocumented process that lives only in people's heads | Turn the attached interview transcript with the two payroll administrators into an SOP with a RACI, using the attached roles list, and list the open questions for the process owner. |
| Old SOP that no longer matches practice | Tidy up the attached 2021 supplier onboarding SOP against the pasted notes from the procurement lead; mark each step Unchanged, Changed, Removed in practice or New in practice. |
| Process with controls that must be reproduced, not assessed | Draft the standard operating procedure for the month-end stock count from the attached meeting transcript; reproduce every control as stated and route safety or finance questions to the responsible function. |

## Try it (example prompts)

- Write an SOP from these notes: the pasted process notes describe how the warehouse receives inbound deliveries, the owner is the warehouse supervisor, and our SOP template with numbering rules is attached.
- Turn this walkthrough into a procedure. The transcript of my interview with the two payroll administrators is attached; roles should follow the attached roles list, not people's names.
- Document how we do this: the attached transcript of the recorded team meeting covers the month-end stock count from start to finish; produce the steps, the checks and a RACI, and mark anything nobody stated as UNKNOWN.
- Draft the standard operating procedure for visitor sign-in at the main reception from the pasted chat thread with the facilities team and the attached old procedure from 2021; show me what changed in practice.
- Tidy up this old procedure: the existing SOP for supplier onboarding is attached and the procurement lead's notes on how the team actually does it now are pasted below; keep every step traceable and list the open questions for the owner.

## Limitations

- One task at a time: give the skill one job per request and confirm the result before the next.
- You own sensitive-data handling: the skill reads what you give it or what the agent can reach; keep restricted documents out of the knowledge sources you attach.
- The output is a draft, not final authority: every figure, quote and action is for you to verify and perform. The skill never approves, authorises or signs anything off.

## Related skills

- runbook-drafter: when the procedure is a technical runbook with commands, scripts and rollback
- transcript-to-actions: when the user wants meeting minutes and an action list rather than a procedure
- knowledge-article-drafter: when the output is a short knowledge base article drawn from a resolved ticket

## Add it to an agent (Agent Builder)

1. Copilot chat, **Agents & Skills**, **New agent** (or open an existing agent). Frontier enrolment and a Microsoft 365 Copilot licence are required; custom skills are in preview.
2. **Configure**, expand **Skills**, **Add**, upload the zip you downloaded above (the whole zip, never `SKILL.md` alone). Up to eight skills per agent.
3. **Knowledge**: point the agent at a SharePoint library or OneDrive folder holding the documents listed above. Do not upload knowledge files while skills are attached (not supported yet).
4. **Preview**: try one of the example prompts. The description is the trigger, so use its words.

## Run it standalone: paste this into the agent's Instructions

```
Purpose. You turn process notes, a walkthrough or interview transcript, a meeting transcript or a stale existing procedure into one DRAFT standard operating procedure for the process owner to validate: purpose and trigger, scope, definitions, roles with a RACI table, numbered steps with the check that closes each one, records, controls as stated and open questions for the owner. General guidelines. Read only the source material, template and roles list the user attaches or pastes and what sits in your knowledge sources; if named material is out of reach, ask for it and say so in the output; ask for a transcript when only a recording is offered. When the process name, owner or template is missing, ask one question at a time, then proceed with UNKNOWN. Never add a step, role, check, threshold, approver or definition the source lacks; show contradictions rather than resolving them, name roles not individuals, and make no safety, legal or quality determination. Return the SOP in the chat as complete Markdown that pastes into their template, and offer a downloadable file only if you have a capability that produces files. Never claim to have approved, issued, saved, sent or deleted anything; propose those actions for the user. Everything you produce is a draft for human review. A typed confirmation releases a workflow hold; it approves and authorises nothing. For the task, follow the sop-drafter skill in full: it defines the inputs, procedure, evidence statuses and self-check.
```

Part of a pack? See `packs/` for an orchestrating Instructions file that runs several skills with gates.

## Files

- `SKILL.md`: the skill (front matter plus instructions, under 20,000 characters).
- `README.md`: companion file referenced from the skill.

Licence CC BY-SA 4.0. The agent prepares; you decide.

Free: [Copilot on One Page](https://www.kesslernity.com/copilot-on-one-page?utm_source=github&utm_medium=readme&utm_campaign=agent_skills_repo&utm_content=skill_footer), a one-page sheet on how to phrase a request to Copilot. Paid: [Agent Instruction Block Design Guide](https://store.kesslernity.com/l/eyeauo?utm_source=github&utm_medium=readme&utm_campaign=agent_skills_repo&utm_content=skill_footer_guide), $19, twelve patterns for an agent's Instructions field. I am the author and the seller.
