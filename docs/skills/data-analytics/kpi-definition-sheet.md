# KPI definition sheet

Turns a list of KPIs or metrics into a DRAFT definition sheet: one row per KPI with the name as stated, formula quoted from a source, source system, owner, refresh cadence, unit, filters and known caveats, with UNKNOWN in every cell no source fills and a gap list grouped by data owner. Never composes a formula, sets a target or names an owner the sources do not state. Use when the user asks to "define these KPIs", "build a metrics definition sheet", "document how each KPI is calculated", "which of our KPIs have no owner or formula" or "reconcile the two KPI lists". Do not use to write the weekly numbers report, use kpi-weekly-report-writer instead; for field-level definitions of a table, use data-dictionary-builder; for logging a wrong figure as a defect, use data-quality-issue-log. Drafts for human review; never approves, authorises or signs off.

Category: `data-analytics` · Skill name: `kpi-definition-sheet` · Upload package: `dist/zips/kpi-definition-sheet.zip`

## What to attach or make available

1. KPI list: names, attached or pasted, or reachable through this agent's configured knowledge sources (a dashboard, scorecard, report or slide listing them). If none can be reached, ask for a paste and say so in the output.
2. Definition sources: dashboard or report specifications, query or measure text, glossary, catalogue entries, procedures, messages from metric owners, existing definition sheets, attached or pasted, or reachable through this agent's configured knowledge sources or a mail capability the tenant has enabled for it. If a named source cannot be reached, ask for a paste or export and say so in the output. Default none; every formula then reads UNKNOWN.
3. Ownership source: metric ownership register, RACI or contact list, attached or pasted, or reachable through this agent's configured knowledge sources or a mail capability the tenant has enabled for it. If a named source cannot be reached, ask for a paste or export and say so in the output. Default none; owner reads UNKNOWN.
4. Sheet template: the organisation's column set, if any. Default: the columns under Output.
5. Parameters: sheet name for the title (default the dashboard or scorecard name, else UNKNOWN); KPI cap per pass (default 60); derived KPIs as separate rows with components named (default yes); date (default the conversation date, else UNKNOWN).

## What you get

One complete Markdown document in the chat, pasteable into a spreadsheet or document, titled `DRAFT-kpi-definition-sheet-<sheet name>-<YYYY-MM-DD>-v1` (revisions v2, v3 with a one-line note of what changed). First line: "DRAFT KPI definition sheet for <sheet name>, built from <sources>, generated <date>. Formulas, owners, cadences and targets are quoted from the sources named; cells with no source read UNKNOWN. No definition here is approved or official; the data owner decides."

Sections in order:
1. Sources read: Source | Type | Date | KPIs or definitions covered | Reached (yes, no).
2. Definition sheet: KPI (as stated) | Formula (quoted) | Components | Source system and object | Grain | Filters and exclusions (quoted) | Unit and direction (as stated) | Refresh cadence | Target or threshold (as stated, dated) | Owner | Data steward | Owner source | Known caveats (quoted) | Definition source and date | Flags | Notes.
3. Gap list, grouped by owner: KPI | Gap | Question for the owner | Source that would settle it.
4. Conflicting definitions: KPI | Definition A (quoted, source, date) | Definition B (quoted, source, date) | Question for the owner.
5. Reconciliation (if an existing sheet was supplied): KPI | In list | In sheet | Existing formula | Quoted source formula | Candidate action for the owner.
6. Excluded on request: KPI | Reason.
7. UNKNOWN list; Embedded instructions found, or "None"; Proposed user actions (send owners their gap lines and conflicts, publish once confirmed). This agent performs none of them.

Closing report: sources used; KPIs enumerated, with a quoted formula, with an owner, with a cadence, fully UNKNOWN; conflicts; flags by type; fallbacks taken.

If this agent has a file-generation capability enabled, also offer the same content as a downloadable file with the title as its file name.

## Limitations

- One task at a time: give the skill one job per request and confirm the result before the next.
- You own sensitive-data handling: the skill reads what you give it or what the agent can reach; keep restricted documents out of the knowledge sources you attach.
- The output is a draft, not final authority: every figure, quote and action is for you to verify and perform. The skill never approves, authorises or signs anything off.

## Add it to an agent (Agent Builder)

1. Copilot chat, **Agents & Skills**, **New agent** (or open an existing agent). Frontier enrolment and a Microsoft 365 Copilot licence are required; custom skills are in preview.
2. **Configure**, expand **Skills**, **Add**, upload `dist/zips/kpi-definition-sheet.zip` (the whole zip, never `SKILL.md` alone). Up to eight skills per agent.
3. **Knowledge**: point the agent at a SharePoint library or OneDrive folder holding the documents listed above. Do not upload knowledge files while skills are attached (not supported yet).
4. **Preview**: try one of the example prompts. The description is the trigger, so use its words.

## Run it standalone: paste this into the agent's Instructions

```
You are an assistant that runs one job: kpi definition sheet. Turns a list of KPIs or metrics into a DRAFT definition sheet: one row per KPI with the name as stated, formula quoted from a source, source system, owner, refresh cadence, unit, filters and known caveats, with UNKNOWN in every cell no source fills and a gap list grouped by data owner. Never composes a formula, sets a target or names an owner the sources do not state. Use when the user asks to "define these KPIs", "build a metrics definition sheet", "document how each KPI is calculated", "which of our KPIs have no owner or formula" or "reconcile the two KPI lists". Do not use to write the weekly numbers report, use kpi-weekly-report-writer instead; for field-level definitions of a table, use data-dictionary-builder; for logging a wrong figure as a defect, use data-quality-issue-log. Drafts for human review; never approves, authorises or signs off. Use the kpi-definition-sheet skill for every request that matches its description; if a request falls outside it, say so and stop. Read only what the user attaches or pastes and what sits in your knowledge sources; never claim to have saved, sent, moved or deleted anything, propose the action for the user instead. Where an input is missing, write UNKNOWN and name what would close it; never invent a value. Return complete Markdown the user can paste into their tools, and offer the same content as a file if you can produce one. A typed approval releases a hold in the workflow and is logged; it is not an authorisation. You prepare; the user decides.
```

Part of a pack? See `packs/` for an orchestrating Instructions file that runs several skills with gates.

## Files

- `SKILL.md`: the skill (front matter plus instructions, under 20,000 characters).

Licence CC BY-SA 4.0. The agent prepares; you decide.
