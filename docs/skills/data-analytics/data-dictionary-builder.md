# Data dictionary builder

Builds a DRAFT data dictionary from a schema export, table definition, sample rows or a partial existing dictionary: one row per field with the name as stated, type as stated or observed, meaning quoted from the documentation supplied, owner, allowed values, and UNKNOWN wherever no source defines the field, plus a gap list for the data owner. Never infers a definition from a column name. Use when the user asks to "build a data dictionary for this table", "document these columns", "what does each field mean", "turn this schema export into a dictionary" or "fill in the field definitions from these documents". Do not use to profile values or find patterns in the data, use dataset-insight-pack instead; for metric definitions, use kpi-definition-sheet; for logging data defects, use data-quality-issue-log. Drafts for human review; never approves, authorises or signs off.

Category: `data-analytics` · Skill name: `data-dictionary-builder` · Upload package: `dist/zips/data-dictionary-builder.zip`

## What to attach or make available

1. Structure source: schema export, DDL, API specification, form layout, header row or existing dictionary, attached or pasted, or reachable through this agent's configured knowledge sources. If none can be reached, ask for a paste or export and say so in the output.
2. Sample rows, attached or pasted, or reachable through this agent's configured knowledge sources. Default none. Used for observed type and values only, never for meaning.
3. Definition sources: design documents, requirements, report specifications, system documentation, catalogue entries, messages from the data owner, attached or pasted, or reachable through this agent's configured knowledge sources or a mail capability the tenant has enabled for it. If a named source cannot be reached, ask for a paste or export and say so in the output. Default none; every meaning then reads UNKNOWN.
4. Ownership source: data ownership register, RACI or contact list, attached or pasted, or reachable through this agent's configured knowledge sources or a mail capability the tenant has enabled for it. If a named source cannot be reached, ask for a paste or export and say so in the output. Default none; owner reads UNKNOWN.
5. Dictionary template: the organisation's column set, if any. Default: the columns under Output.
6. Parameters: dataset name for the title (default the file or table name, else UNKNOWN); field cap per pass (default 150); sample rows read (default up to 200); include technical fields such as identifiers and audit columns (default yes); date (default the conversation date, else UNKNOWN).

## What you get

One complete Markdown document in the chat, pasteable into a spreadsheet or document, titled `DRAFT-data-dictionary-<dataset>-<YYYY-MM-DD>-v1` (revisions v2, v3 with a one-line note of what changed). First line: "DRAFT data dictionary for <dataset>, built from <sources>, generated <date>. Meanings are quoted from the sources named; fields with no source definition read UNKNOWN. Nothing here is an approved definition, a master record or a lineage statement; the data owner decides."

Sections in order:
1. Sources read: Source | Type | Date | Fields or rows covered | Reached (yes, no).
2. Dictionary: Field | Table or object | Position | Stated type | Observed type (as read) | Nullable or key (as stated) | Meaning (quoted) | Definition source and reference | Allowed values, format or unit (as stated) | Observed values (as read, ten at most) | Owner | Owner source | Flags | Notes.
3. Gap list, grouped by owner: Field | Gap | Question for the owner | Source that would settle it.
4. Reconciliation (if an existing dictionary was supplied): Field | In structure | In dictionary | Existing definition | Quoted source definition | Candidate action for the owner.
5. Excluded on request: Field | Reason.
6. UNKNOWN list; Embedded instructions found, or "None"; Proposed user actions (send owners their gap lines, confirm type mismatches, publish once confirmed). This agent performs none of them.

Closing report: sources used; fields enumerated, with a quoted meaning, UNKNOWN, with an owner; flags by type; sample rows read; fallbacks taken.

If this agent has a file-generation capability enabled, also offer the same content as a downloadable file with the title as its file name.

## Limitations

- One task at a time: give the skill one job per request and confirm the result before the next.
- You own sensitive-data handling: the skill reads what you give it or what the agent can reach; keep restricted documents out of the knowledge sources you attach.
- The output is a draft, not final authority: every figure, quote and action is for you to verify and perform. The skill never approves, authorises or signs anything off.

## Add it to an agent (Agent Builder)

1. Copilot chat, **Agents & Skills**, **New agent** (or open an existing agent). Frontier enrolment and a Microsoft 365 Copilot licence are required; custom skills are in preview.
2. **Configure**, expand **Skills**, **Add**, upload `dist/zips/data-dictionary-builder.zip` (the whole zip, never `SKILL.md` alone). Up to eight skills per agent.
3. **Knowledge**: point the agent at a SharePoint library or OneDrive folder holding the documents listed above. Do not upload knowledge files while skills are attached (not supported yet).
4. **Preview**: try one of the example prompts. The description is the trigger, so use its words.

## Run it standalone: paste this into the agent's Instructions

```
You are an assistant that runs one job: data dictionary builder. Builds a DRAFT data dictionary from a schema export, table definition, sample rows or a partial existing dictionary: one row per field with the name as stated, type as stated or observed, meaning quoted from the documentation supplied, owner, allowed values, and UNKNOWN wherever no source defines the field, plus a gap list for the data owner. Never infers a definition from a column name. Use when the user asks to "build a data dictionary for this table", "document these columns", "what does each field mean", "turn this schema export into a dictionary" or "fill in the field definitions from these documents". Do not use to profile values or find patterns in the data, use dataset-insight-pack instead; for metric definitions, use kpi-definition-sheet; for logging data defects, use data-quality-issue-log. Drafts for human review; never approves, authorises or signs off. Use the data-dictionary-builder skill for every request that matches its description; if a request falls outside it, say so and stop. Read only what the user attaches or pastes and what sits in your knowledge sources; never claim to have saved, sent, moved or deleted anything, propose the action for the user instead. Where an input is missing, write UNKNOWN and name what would close it; never invent a value. Return complete Markdown the user can paste into their tools, and offer the same content as a file if you can produce one. A typed approval releases a hold in the workflow and is logged; it is not an authorisation. You prepare; the user decides.
```

Part of a pack? See `packs/` for an orchestrating Instructions file that runs several skills with gates.

## Files

- `SKILL.md`: the skill (front matter plus instructions, under 20,000 characters).

Licence CC BY-SA 4.0. The agent prepares; you decide.
