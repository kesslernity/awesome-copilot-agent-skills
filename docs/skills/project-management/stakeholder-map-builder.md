# Stakeholder map builder

Builds a DRAFT stakeholder map for one project from the charter, organisation chart, RACI, governance terms, steering minutes, meeting notes and messages the user provides: a stakeholder register, interest and influence ratings each with its stated basis, stance as evidenced by a verbatim fragment with source and date, gaps, and a proposed engagement plan per stakeholder, every line traced to a source and every missing fact marked UNKNOWN. Use when the user asks to "build the stakeholder map", "who are the stakeholders on this project", "map interest and influence", "where does each stakeholder stand", "draft the stakeholder engagement plan" or "refresh the stakeholder register". Do not use for a customer account's stakeholders, use account-plan-builder instead; for a one-page brief before one meeting, use meeting-prep-onepager; for logging decisions and risks against the project, use project-status-tracker. Drafts for human review; never approves, authorises or signs off.

Category: `project-management` · Skill name: `stakeholder-map-builder` · Upload package: `dist/zips/stakeholder-map-builder.zip`

## What to attach or make available

Ask once for whatever is missing, in one message, then proceed with UNKNOWN.
1. Project documents (charter, organisation chart, RACI, governance terms, communication plan, minutes, notes, emails, chat), pasted, attached or reachable through this agent's configured knowledge sources, mail or meeting access. Not reachable: ask for a paste or export and say so in the header.
2. Project name, phase and its start date (default UNKNOWN), and purpose of the map (a gate, a go-live, general engagement). Default: general engagement.
3. Previous stakeholder map, if any, for the delta.
4. Rating scale. Default: High, Medium, Low, UNKNOWN per the reference bases; a house scale replaces it and is named in the header.
5. Stance vocabulary. Default: Supportive, Neutral, Concerned, Opposed, Mixed, UNKNOWN; never extended with personal descriptors.
6. Channel and cadence catalogue (optional). Default: channels the sources name, plus one-to-one, governance forum and written update.
7. Circulation. Default: project manager and sponsor only; header marked "restricted: contains statements attributed to named people".
8. Today's date. Title: `DRAFT-stakeholder-map-<project>-<YYYY-MM-DD>-v1`; revisions v2, v3.
Reference files in this skill: references/rating-and-stance-rules.md, read at steps 5 to 8, 10 and 12 for rating bases, stance signal phrases, grid labels, engagement plan fields and banned descriptors.

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

## Limitations

- One task at a time: give the skill one job per request and confirm the result before the next.
- You own sensitive-data handling: the skill reads what you give it or what the agent can reach; keep restricted documents out of the knowledge sources you attach.
- The output is a draft, not final authority: every figure, quote and action is for you to verify and perform. The skill never approves, authorises or signs anything off.

## Add it to an agent (Agent Builder)

1. Copilot chat, **Agents & Skills**, **New agent** (or open an existing agent). Frontier enrolment and a Microsoft 365 Copilot licence are required; custom skills are in preview.
2. **Configure**, expand **Skills**, **Add**, upload `dist/zips/stakeholder-map-builder.zip` (the whole zip, never `SKILL.md` alone). Up to eight skills per agent.
3. **Knowledge**: point the agent at a SharePoint library or OneDrive folder holding the documents listed above. Do not upload knowledge files while skills are attached (not supported yet).
4. **Preview**: try one of the example prompts. The description is the trigger, so use its words.

## Run it standalone: paste this into the agent's Instructions

```
You are an assistant that runs one job: stakeholder map builder. Builds a DRAFT stakeholder map for one project from the charter, organisation chart, RACI, governance terms, steering minutes, meeting notes and messages the user provides: a stakeholder register, interest and influence ratings each with its stated basis, stance as evidenced by a verbatim fragment with source and date, gaps, and a proposed engagement plan per stakeholder, every line traced to a source and every missing fact marked UNKNOWN. Use when the user asks to "build the stakeholder map", "who are the stakeholders on this project", "map interest and influence", "where does each stakeholder stand", "draft the stakeholder engagement plan" or "refresh the stakeholder register". Do not use for a customer account's stakeholders, use account-plan-builder instead; for a one-page brief before one meeting, use meeting-prep-onepager; for logging decisions and risks against the project, use project-status-tracker. Drafts for human review; never approves, authorises or signs off. Use the stakeholder-map-builder skill for every request that matches its description; if a request falls outside it, say so and stop. Read only what the user attaches or pastes and what sits in your knowledge sources; never claim to have saved, sent, moved or deleted anything, propose the action for the user instead. Where an input is missing, write UNKNOWN and name what would close it; never invent a value. Return complete Markdown the user can paste into their tools, and offer the same content as a file if you can produce one. A typed approval releases a hold in the workflow and is logged; it is not an authorisation. You prepare; the user decides.
```

Part of a pack? See `packs/` for an orchestrating Instructions file that runs several skills with gates.

## Files

- `SKILL.md`: the skill (front matter plus instructions, under 20,000 characters).
- `references/rating-and-stance-rules.md`: companion file referenced from the skill.

Licence CC BY-SA 4.0. The agent prepares; you decide.
