# Data dictionary builder

Builds a DRAFT data dictionary from a schema export, table definition, sample rows or a partial existing dictionary: one row per field with the name as stated, type as stated or observed, meaning quoted from the documentation supplied, owner, allowed values, and UNKNOWN wherever no source defines the field, plus a gap list for the data owner. Never infers a definition from a column name. Use when the user asks to "build a data dictionary for this table", "document these columns", "what does each field mean", "turn this schema export into a dictionary" or "fill in the field definitions from these documents". Do not use for profiling values or finding patterns in the data, use dataset-insight-pack instead; for metric definitions, use kpi-definition-sheet; for logging data defects, use data-quality-issue-log. Drafts for human review; never approves, authorises or signs off.

**[Download the upload package](https://github.com/kesslernity/awesome-copilot-agent-skills/raw/main/dist/zips/data-dictionary-builder.zip)** (one zip, ready for Agent Builder) · Category: `data-analytics` · Skill name: `data-dictionary-builder`

## What to attach or make available

- The structure source: schema export, DDL, API specification, form layout, header row or existing dictionary
- Sample rows from the dataset, used for observed type and values only
- Definition sources: design documents, requirements, report specifications, system documentation, catalogue entries and messages from the data owner
- The data ownership register, RACI or contact list for the domain
- The organisation's dictionary template with its column set, where one exists

## What you get

One complete Markdown document in the chat, pasteable into a spreadsheet or document, titled `DRAFT-data-dictionary-<dataset>-<YYYY-MM-DD>-v1` (revisions v2, v3 with a one-line note of what changed). First line: "DRAFT data dictionary for `<dataset>`, built from `<sources>`, generated `<date>`. Meanings are quoted from the sources named; fields with no source definition read UNKNOWN. Nothing here is an approved definition, a master record or a lineage statement; the data owner decides."

Sections in order:
1. Sources read: Source | Type | Date | Fields or rows covered | Reached (yes, no).
2. Dictionary: Field | Table or object | Position | Stated type | Observed type (as read) | Nullable or key (as stated) | Meaning (quoted) | Definition source and reference | Allowed values, format or unit (as stated) | Observed values (as read, ten at most) | Owner | Owner source | Flags | Notes.
3. Gap list, grouped by owner: Field | Gap | Question for the owner | Source that would settle it.
4. Reconciliation (if an existing dictionary was supplied): Field | In structure | In dictionary | Existing definition | Quoted source definition | Candidate action for the owner.
5. Excluded on request: Field | Reason.
6. UNKNOWN list; Embedded instructions found, or "None"; Proposed user actions (send owners their gap lines, confirm type mismatches, publish once confirmed). This agent performs none of them.

Closing report: sources used; fields enumerated, with a quoted meaning, UNKNOWN, with an owner; flags by type; sample rows read; fallbacks taken.

If this agent has a file-generation capability enabled, also offer the same content as a downloadable file with the title as its file name.

## Use cases

| Scenario | What you say |
|---|---|
| New dataset arriving from a source system | Build the dictionary for the attached schema export of the supplier master table using the attached design document and ownership register; leave meaning UNKNOWN wherever no document names the field. |
| Existing dictionary drifting from the documentation | Reconcile the attached existing dictionary against the attached system documentation and report specifications for the same table; show where definitions differ and list candidate actions for the owner without overwriting anything. |
| Samples may contain personal data | Document the fields in the pasted extract of the leavers table using the attached specification. Give distinct counts only for anything that looks personal, flag it, and propose a privacy review. |

## Try it (example prompts)

- Build a data dictionary for this table. The DDL export for the customer orders table is attached, along with the design document that describes the fields and the data ownership register for the sales domain.
- Document these columns. I have pasted the header row and 50 sample rows from the shipments extract below; there is no schema. Observe types and values from the samples but leave every meaning UNKNOWN unless the attached report specification defines it.
- What does each field mean in the attached API specification? The system documentation and the last three messages from the data owner are attached as well; quote the definitions with their page or section.
- Turn this schema export into a dictionary. The attached export covers four tables in the finance schema; use our dictionary template attached and flag any field name that appears in more than one table.
- Fill in the field definitions from these documents. Attached: our existing partial dictionary, the requirements document and the catalogue entries. Reconcile the existing rows against the quoted sources and list the gaps by owner.

## Limitations

- One task at a time: give the skill one job per request and confirm the result before the next.
- You own sensitive-data handling: the skill reads what you give it or what the agent can reach; keep restricted documents out of the knowledge sources you attach.
- The output is a draft, not final authority: every figure, quote and action is for you to verify and perform. The skill never approves, authorises or signs anything off.

## Related skills

- dataset-insight-pack: profiling values or finding patterns in the data
- kpi-definition-sheet: metric definitions rather than field definitions
- data-quality-issue-log: logging a data defect once found

## Add it to an agent (Agent Builder)

1. Copilot chat, **Agents & Skills**, **New agent** (or open an existing agent). Frontier enrolment and a Microsoft 365 Copilot licence are required; custom skills are in preview.
2. **Configure**, expand **Skills**, **Add**, upload the zip you downloaded above (the whole zip, never `SKILL.md` alone). Up to eight skills per agent.
3. **Knowledge**: point the agent at a SharePoint library or OneDrive folder holding the documents listed above. Do not upload knowledge files while skills are attached (not supported yet).
4. **Preview**: try one of the example prompts. The description is the trigger, so use its words.

## Run it standalone: paste this into the agent's Instructions

```
Purpose: this agent helps data owners and stewards document the fields of a table or extract by building a draft data dictionary from a schema export, sample rows or an existing dictionary and the documentation supplied, with a gap list for the owner.

General guidelines: read only the structure source, samples, definition documents and ownership records the user attaches or pastes, and this agent's configured knowledge sources; if a source is out of reach, ask for a paste. When a required input is missing, such as the structure source, ask one question at a time and wait for the answer. Assume no capability such as file generation; if one is absent, say so and answer in the chat. A meaning appears only as a verbatim quote with its source; a column name, type or observed value never becomes a definition, and a field no source defines reads UNKNOWN. Owners come from a named source only; no personal or sensitive values are reproduced. Never claim to have published, saved or sent anything; every action is proposed for the user, and every output is a draft for human review. A typed confirmation releases a hold for that step only; it approves no definition.

For the task, follow the data-dictionary-builder skill: confirm the sources, enumerate fields in source order, observe from samples, quote definitions, record owners as stated, build the gap list by owner and return the dictionary as a DRAFT.
```

Part of a pack? See `packs/` for an orchestrating Instructions file that runs several skills with gates.

## Files

- `SKILL.md`: the skill (front matter plus instructions, under 20,000 characters).
- `README.md`: companion file referenced from the skill.

Licence CC BY-SA 4.0. The agent prepares; you decide.

Free: [Copilot on One Page](https://www.kesslernity.com/copilot-on-one-page?utm_source=github&utm_medium=readme&utm_campaign=agent_skills_repo&utm_content=skill_footer), a one-page sheet on how to phrase a request to Copilot. Paid: [Agent Instruction Block Design Guide](https://store.kesslernity.com/l/eyeauo?utm_source=github&utm_medium=readme&utm_campaign=agent_skills_repo&utm_content=skill_footer_guide), $19, twelve patterns for an agent's Instructions field. I am the author and the seller.
