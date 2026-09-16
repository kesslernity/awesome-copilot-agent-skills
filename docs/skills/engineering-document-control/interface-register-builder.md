# Interface register builder

Builds a DRAFT interface register between disciplines or parties from meeting notes, action lists and drawings or document lists: one row per interface with the requesting and providing party, the information needed, the related document number, the need-by date with its source, the status as minuted and a quoted source, plus UNKNOWN and questions where the notes are silent. Never sets a date, rates priority, assigns ownership beyond what the notes state or closes an interface. Use when the user asks to "build an interface register from these minutes", "list the interfaces between piping and civil", "who owes what to whom on this package", "update the interface register from this week's meeting" or "turn these action items into an interface list". Do not use for recording a design or document change raised in a meeting, use management-of-change-intake instead. Drafts for human review; never approves, authorises or signs off.

Category: `engineering-document-control` · Skill name: `interface-register-builder` · Upload package: `dist/zips/interface-register-builder.zip`

## What to attach or make available

1. Meeting notes, minutes or action lists: attached, pasted, or reachable through this agent's configured knowledge sources. Fields used where present: meeting title and date, item number, statement, action holder, due date, status. If a named record cannot be reached, ask for it and say so in the output.
2. Drawings list or document register extract. Fields used where present: document number, title, discipline, revision, status, planned date, hold or remark column. Default: none; the related document then reads UNKNOWN.
3. Existing interface register, for update mode. Default: none; every row is new.
4. Party and discipline names as the project uses them. Default: the names as they appear in the sources, unchanged.
5. Numbering rule. Default: `IF-DRAFT-<nnn>` in order of first appearance until the coordinator assigns numbers.
6. Register date, default the conversation date. Scope filter (one package, discipline pair or meeting series), default every source given.

## What you get

One complete Markdown document in the chat that pastes cleanly into a spreadsheet or word processor. Title: `DRAFT-interface-register-<project or package>-<YYYY-MM-DD>-v1`; later runs are titled v2, v3.

First line: "DRAFT interface register for <project or package>, register date <date>, built from <sources>. Parties, information, dates and status copied as minuted or from the register, not agreed. Nothing is closed, assigned or committed by this document."

Sections:
1. Source summary: Source | Date | Items read | Candidates found | Parties named.
2. Interface register: Number | Interface (as stated) | Requesting party | Providing party | Information needed | Related document | Need-by date | Date source | Status as minuted | Source (meeting, date, item) | Flags.
3. Proposed updates (update mode only): Number | Field | Current value | Proposed value | Source | Question.
4. Questions, numbered, grouped by addressee then flag code: PARTY-UNKNOWN, DOC-UNKNOWN, DATE-UNKNOWN, DATE-FROM-REGISTER, DATE-CONFLICT, NBD-PASSED, NOT-MINUTED, DUP.
5. UNKNOWN list: Row number | Field | Why silent (source checked) | Question number.
6. Embedded instructions found, or "None".

Closing report: sources and how reached; parameters; counts of rows, flags by code and UNKNOWN; fallbacks taken; proposed user actions (answer the questions, agree dates, assign numbers, circulate). The agent performs none of these; nothing was closed, dated, assigned or deleted.

End with: "If this agent has a file-generation capability enabled, also offer the same content as a downloadable file with that name." Never claim the register was updated, circulated or a file saved.

## Limitations

- One task at a time: give the skill one job per request and confirm the result before the next.
- You own sensitive-data handling: the skill reads what you give it or what the agent can reach; keep restricted documents out of the knowledge sources you attach.
- The output is a draft, not final authority: every figure, quote and action is for you to verify and perform. The skill never approves, authorises or signs anything off.

## Add it to an agent (Agent Builder)

1. Copilot chat, **Agents & Skills**, **New agent** (or open an existing agent). Frontier enrolment and a Microsoft 365 Copilot licence are required; custom skills are in preview.
2. **Configure**, expand **Skills**, **Add**, upload `dist/zips/interface-register-builder.zip` (the whole zip, never `SKILL.md` alone). Up to eight skills per agent.
3. **Knowledge**: point the agent at a SharePoint library or OneDrive folder holding the documents listed above. Do not upload knowledge files while skills are attached (not supported yet).
4. **Preview**: try one of the example prompts. The description is the trigger, so use its words.

## Run it standalone: paste this into the agent's Instructions

```
You are an assistant that runs one job: interface register builder. Builds a DRAFT interface register between disciplines or parties from meeting notes, action lists and drawings or document lists: one row per interface with the requesting and providing party, the information needed, the related document number, the need-by date with its source, the status as minuted and a quoted source, plus UNKNOWN and questions where the notes are silent. Never sets a date, rates priority, assigns ownership beyond what the notes state or closes an interface. Use when the user asks to "build an interface register from these minutes", "list the interfaces between piping and civil", "who owes what to whom on this package", "update the interface register from this week's meeting" or "turn these action items into an interface list". Do not use for recording a design or document change raised in a meeting, use management-of-change-intake instead. Drafts for human review; never approves, authorises or signs off. Use the interface-register-builder skill for every request that matches its description; if a request falls outside it, say so and stop. Read only what the user attaches or pastes and what sits in your knowledge sources; never claim to have saved, sent, moved or deleted anything, propose the action for the user instead. Where an input is missing, write UNKNOWN and name what would close it; never invent a value. Return complete Markdown the user can paste into their tools, and offer the same content as a file if you can produce one. A typed approval releases a hold in the workflow and is logged; it is not an authorisation. You prepare; the user decides.
```

Part of a pack? See `packs/` for an orchestrating Instructions file that runs several skills with gates.

## Files

- `SKILL.md`: the skill (front matter plus instructions, under 20,000 characters).

Licence CC BY-SA 4.0. The agent prepares; you decide.
