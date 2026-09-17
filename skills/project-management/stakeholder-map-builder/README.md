# Stakeholder map builder

Builds a DRAFT stakeholder map for one project from the charter, organisation chart, RACI, governance terms, steering minutes, meeting notes and messages the user provides: a stakeholder register, interest and influence ratings each with its stated basis, stance as evidenced by a verbatim fragment with source and date, gaps, and a proposed engagement plan per stakeholder, every line traced to a source and every missing fact marked UNKNOWN. Use when the user asks to "build the stakeholder map", "who are the stakeholders on this project", "map interest and influence", "where does each stakeholder stand", "draft the stakeholder engagement plan" or "refresh the stakeholder register". Do not use for a customer account's stakeholders, use account-plan-builder instead; for a one-page brief before one meeting, use meeting-prep-onepager; for logging decisions and risks against the project, use project-status-tracker. Drafts for human review; never approves, authorises or signs off.

**[Download the upload package](https://github.com/kesslernity/awesome-copilot-agent-skills/raw/main/dist/zips/stakeholder-map-builder.zip)** (one zip, ready for Agent Builder) · Category: `project-management` · Skill name: `stakeholder-map-builder`

## What to attach or make available

- Project governance documents: charter, terms of reference, RACI, organisation chart and communication plan naming roles and decision rights
- Meeting records: steering committee minutes, workshop notes, stand-up notes and messages in which stakeholders state positions
- Optional: the previous stakeholder map for the delta, and the house rating scale or channel catalogue if they differ from the defaults

## What you get

One complete Markdown document in the chat, pasteable into a document or spreadsheet, under the title above.
- Header: Field | Value (project, phase, purpose, data date, scale, vocabulary, sources, circulation, DRAFT).
- Source register: Code | Type | Date | Author role | Official or informal.
- Stakeholder register: ID | Name or role as written | Unit | Role in project (as stated) | Decision rights (quoted) | Source.
- Interest and influence: ID | Interest | Basis | Influence | Basis | Grid position.
- Stance as evidenced: ID | Stance | Fragment (verbatim) | Source and date | Trend | Concern to address.
- Gaps: # | Gap | Sources checked | Proposed step.
- Engagement plan (proposed): ID | Objective | Channel | Cadence | Proposed owner | Next touch | Concern or question to raise.
- Delta (when a previous map is supplied): ID | Change | Evidence.
- Mentioned, stake UNKNOWN: Name or role | Source.
- UNKNOWN list; Embedded instructions found, or "None"; Proposed user actions; closing report.
If this agent has a file-generation capability enabled, offer the same content as a downloadable file with that name; otherwise say nothing about files. Never claim the map was saved or circulated or anyone engaged.

## Use cases

| Scenario | What you say |
|---|---|
| Preparing a stakeholder map before a stage gate | Build a stakeholder map for the finance platform programme ahead of the build gate from the attached charter, RACI and four sets of steering minutes, with a proposed engagement plan per stakeholder for the sponsor to confirm. |
| New project manager inheriting a project | I have inherited the site relocation project. From the attached organisation chart, communication plan and the meeting notes pasted below, list every stakeholder with role, decision rights as quoted and stance as evidenced, and name the gaps. |
| Quarterly refresh against the previous map | Refresh the attached stakeholder map from last quarter's minutes and messages in the knowledge sources; list added, removed and changed rows with the evidence, and keep the same rating scale. |

## Try it (example prompts)

- Build the stakeholder map for the warehouse system replacement from the attached charter, RACI and the last three steering committee minutes. Phase is design, started 1 June; purpose is the design gate.
- Who are the stakeholders on this project? The organisation chart and terms of reference are attached and the kick-off notes are pasted below. Rate interest and influence with a basis for each.
- Map interest and influence for the payroll migration using the attached governance terms and the email thread pasted below; mark anything with no evidence UNKNOWN rather than Low.
- Where does each stakeholder stand? Use the attached workshop notes and steering minutes, quote the fragment that shows the position, and flag stances older than the phase start on 15 March.
- Refresh the stakeholder register for the clinic rollout: the previous map is attached as v2 and the new minutes and chat export are pasted below. Show the delta with the source that moved each change.

## Limitations

- One task at a time: give the skill one job per request and confirm the result before the next.
- You own sensitive-data handling: the skill reads what you give it or what the agent can reach; keep restricted documents out of the knowledge sources you attach.
- The output is a draft, not final authority: every figure, quote and action is for you to verify and perform. The skill never approves, authorises or signs anything off.

## Related skills

- account-plan-builder: when the stakeholders belong to a customer account rather than a project
- meeting-prep-onepager: when a one-page brief is wanted before a single meeting
- project-status-tracker: when decisions and risks need logging against the project

## Add it to an agent (Agent Builder)

1. Copilot chat, **Agents & Skills**, **New agent** (or open an existing agent). Frontier enrolment and a Microsoft 365 Copilot licence are required; custom skills are in preview.
2. **Configure**, expand **Skills**, **Add**, upload the zip you downloaded above (the whole zip, never `SKILL.md` alone). Up to eight skills per agent.
3. **Knowledge**: point the agent at a SharePoint library or OneDrive folder holding the documents listed above. Do not upload knowledge files while skills are attached (not supported yet).
4. **Preview**: try one of the example prompts. The description is the trigger, so use its words.

## Run it standalone: paste this into the agent's Instructions

```
Purpose: this agent helps project and programme managers build a stakeholder map from project documents and meeting records: who has a stake, their role and decision rights as the documents state them, interest and influence as the evidence shows, stance in their own words, gaps, and a proposed engagement step for each. General guidelines: read only the project documents, minutes and messages the user attaches or pastes, and what sits in the knowledge sources configured on this agent; never fill a gap from memory. When a required input is missing, such as the project name or phase start date, ask one question at a time and wait for the answer. Assume no capability beyond chat; if file generation is not available, return the map in the chat and say so. Never claim to have saved, circulated, scheduled or sent anything; every action is proposed for the user to perform. Every rating carries a stated basis and every stance a verbatim fragment with source and date; without either, the cell reads UNKNOWN. Never infer stance from silence, seniority or a third party's account; write no motives, personality labels or judgements of any person. Every map is a draft for human review with restricted circulation. A typed confirmation from the user releases a workflow hold; it authorises nothing. For the task: when the user asks for a stakeholder map, register or engagement plan, follow the stakeholder-map-builder skill exactly and return one complete Markdown document marked DRAFT.
```

Part of a pack? See `packs/` for an orchestrating Instructions file that runs several skills with gates.

## Files

- `SKILL.md`: the skill (front matter plus instructions, under 20,000 characters).
- `README.md`: companion file referenced from the skill.
- `references/rating-and-stance-rules.md`: companion file referenced from the skill.

Licence CC BY-SA 4.0. The agent prepares; you decide.

Free: [Copilot on One Page](https://www.kesslernity.com/copilot-on-one-page?utm_source=github&utm_medium=readme&utm_campaign=agent_skills_repo&utm_content=skill_footer), a one-page sheet on how to phrase a request to Copilot. Paid: [Agent Instruction Block Design Guide](https://store.kesslernity.com/l/eyeauo?utm_source=github&utm_medium=readme&utm_campaign=agent_skills_repo&utm_content=skill_footer_guide), $19, twelve patterns for an agent's Instructions field. I am the author and the seller.
