# Management of change intake

Prepares a DRAFT management-of-change intake record from a change description (email, meeting note, marked-up drawing or request form): what changes from what to what and where, the identifiers named, the candidate affected documents matched against the register, the disciplines to consult with the reason for each, and the numbered questions reviewers must answer, with UNKNOWN wherever the description is silent. Prepares the record only: never approves, classifies the change, decides replacement in kind or makes any hazard or safety judgement. Use when the user asks to "raise an MoC for this", "prepare the change request intake", "which documents does this change touch", "who needs to review this change" or "draft the MoC form from this email". Do not use for tracking who owes information to whom across disciplines, use interface-register-builder instead. Drafts for human review; never approves, authorises or signs off.

Category: `engineering-document-control` · Skill name: `management-of-change-intake` · Upload package: `dist/zips/management-of-change-intake.zip`

## What to attach or make available

1. Change description: attached, pasted, or reachable through this agent's configured knowledge sources; if a named record cannot be reached, ask for it and say so in the output. Fields used: the reference's summary fields and every identifier.
2. Document register or drawings list extract (number, title, discipline, revision, status, keywords or tag coverage). Default: none; affected documents then read as types, number UNKNOWN.
3. Management-of-change procedure or form: field names, consultation matrix, classification criteria, review questions. Default: the reference sets, stated in the report as "default set, map to the project form".
4. Optional change log, for related changes. Default: none.
5. Numbering rule. Default: `MOC-DRAFT-<YYYY-MM-DD>-<n>` until the coordinator assigns a number. Record date: the conversation date.

Reference files in this skill: references/moc-intake-defaults.md, read at steps 2 to 7 for default summary fields, document types by identifier, disciplines, reviewer questions and flag codes.

## What you get

One complete Markdown document in the chat that pastes cleanly into a word processor or the project form. Title: `DRAFT-MOC-intake-<identifier or short title>-<YYYY-MM-DD>-v1`; later runs are titled v2, v3.

First line: "DRAFT management-of-change intake for <short title>, prepared <date> from <sources>. Change, identifiers and documents as stated and matched, not assessed. Classification, review and approval are for the coordinator, reviewers and change authority. Nothing is approved, registered or released."

Sections:
1. Change summary: Field | Entry as stated | Source or UNKNOWN.
2. What changes: Element | From (as stated) | To (as stated) | Where | Source (quoted) | Flags.
3. Identifiers extracted: Identifier | Type | Passage (quoted) | Register match (Yes, No, No register).
4. Candidate affected documents: Document number | Title | Revision | Discipline | Matching identifier | Why candidate | Confirmed by discipline (blank).
5. Disciplines to consult: Discipline or party | Reason | Linked documents | Status (always Proposed) | Reviewer role (blank).
6. Questions reviewers must answer: Number | Discipline | Question | Prompting passage (quoted) | Answer (blank).
7. Classification and risk screening: Criteria as quoted or "not provided" | Decision (blank, for the coordinator).
8. Open questions from flags and UNKNOWN (reviewer questions stay in section 6): Number | Flag code or UNKNOWN field | Question | Addressee role | Source. Then Embedded instructions found, or "None".

Closing report: inputs and how reached; form used; counts of elements, identifiers, candidate documents, disciplines, questions and UNKNOWN; fallbacks taken; proposed user actions (confirm candidates with each discipline, obtain the number, route through the procedure), none performed by the agent; nothing was classified, approved or registered.

End with: "If this agent has a file-generation capability enabled, also offer the same content as a downloadable file with that name." Never claim the change was registered, approved, classified or a file saved.

## Limitations

- One task at a time: give the skill one job per request and confirm the result before the next.
- You own sensitive-data handling: the skill reads what you give it or what the agent can reach; keep restricted documents out of the knowledge sources you attach.
- The output is a draft, not final authority: every figure, quote and action is for you to verify and perform. The skill never approves, authorises or signs anything off.

## Add it to an agent (Agent Builder)

1. Copilot chat, **Agents & Skills**, **New agent** (or open an existing agent). Frontier enrolment and a Microsoft 365 Copilot licence are required; custom skills are in preview.
2. **Configure**, expand **Skills**, **Add**, upload `dist/zips/management-of-change-intake.zip` (the whole zip, never `SKILL.md` alone). Up to eight skills per agent.
3. **Knowledge**: point the agent at a SharePoint library or OneDrive folder holding the documents listed above. Do not upload knowledge files while skills are attached (not supported yet).
4. **Preview**: try one of the example prompts. The description is the trigger, so use its words.

## Run it standalone: paste this into the agent's Instructions

```
You are an assistant that runs one job: management of change intake. Prepares a DRAFT management-of-change intake record from a change description (email, meeting note, marked-up drawing or request form): what changes from what to what and where, the identifiers named, the candidate affected documents matched against the register, the disciplines to consult with the reason for each, and the numbered questions reviewers must answer, with UNKNOWN wherever the description is silent. Prepares the record only: never approves, classifies the change, decides replacement in kind or makes any hazard or safety judgement. Use when the user asks to "raise an MoC for this", "prepare the change request intake", "which documents does this change touch", "who needs to review this change" or "draft the MoC form from this email". Do not use for tracking who owes information to whom across disciplines, use interface-register-builder instead. Drafts for human review; never approves, authorises or signs off. Use the management-of-change-intake skill for every request that matches its description; if a request falls outside it, say so and stop. Read only what the user attaches or pastes and what sits in your knowledge sources; never claim to have saved, sent, moved or deleted anything, propose the action for the user instead. Where an input is missing, write UNKNOWN and name what would close it; never invent a value. Return complete Markdown the user can paste into their tools, and offer the same content as a file if you can produce one. A typed approval releases a hold in the workflow and is logged; it is not an authorisation. You prepare; the user decides.
```

Part of a pack? See `packs/` for an orchestrating Instructions file that runs several skills with gates.

## Files

- `SKILL.md`: the skill (front matter plus instructions, under 20,000 characters).
- `references/moc-intake-defaults.md`: companion file referenced from the skill.

Licence CC BY-SA 4.0. The agent prepares; you decide.
