# KPI definition sheet

Turns a list of KPIs or metrics into a DRAFT definition sheet: one row per KPI with the name as stated, formula quoted from a source, source system, owner, refresh cadence, unit, filters and known caveats, with UNKNOWN in every cell no source fills and a gap list grouped by data owner. Never composes a formula, sets a target or names an owner the sources do not state. Use when the user asks to "define these KPIs", "build a metrics definition sheet", "document how each KPI is calculated", "which of our KPIs have no owner or formula" or "reconcile the two KPI lists". Do not use for the weekly numbers report, use kpi-weekly-report-writer instead; for field-level definitions of a table, use data-dictionary-builder; for logging a wrong figure as a defect, use data-quality-issue-log. Drafts for human review; never approves, authorises or signs off.

**[Download the upload package](https://github.com/kesslernity/awesome-copilot-agent-skills/raw/main/dist/zips/kpi-definition-sheet.zip)** (one zip, ready for Agent Builder) · Category: `data-analytics` · Skill name: `kpi-definition-sheet`

## What to attach or make available

- The KPI or metric list: a dashboard, scorecard, report or slide naming the KPIs, attached, pasted or in the knowledge sources
- Definition sources: dashboard or report specifications, query or measure text, glossary and catalogue entries, procedures and messages from metric owners
- Ownership source: the metric ownership register, RACI or contact list naming owners and data stewards
- Optional: the existing definition sheet to reconcile against, and the organisation's sheet template if its columns differ from the default

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

## Use cases

| Scenario | What you say |
|---|---|
| New dashboard needs a definition sheet before launch | Build a definition sheet for the 12 KPIs in the attached dashboard specification, quoting formulas from the measure text pasted below and owners from the register in the knowledge sources. |
| Two teams disagree on how a metric is calculated | Two definitions of customer churn rate appear in the attached documents. Record both side by side with source and date and frame the question the owner must answer; do not pick one. |
| Gap hunt across an inherited scorecard | The pasted scorecard lists 40 KPIs and I have inherited it with no documentation beyond the attached glossary. List every KPI with no formula, owner or cadence, grouped by owner. |

## Try it (example prompts)

- Define these KPIs. The scorecard listing them is attached as a slide export and the dashboard measure definitions are pasted below. Build the definition sheet with UNKNOWN wherever nothing states the formula.
- Build a metrics definition sheet for the 18 KPIs in the attached operations dashboard specification, quoting formulas from the pasted glossary and owners from the ownership register in the knowledge sources.
- Document how each KPI is calculated from the attached report specification and the measure text pasted below; quote every formula verbatim with its source and flag anything with no source.
- Which of our KPIs have no owner or formula? The KPI list is pasted below and the only documentation is the attached catalogue export; group the gaps by owner.
- Reconcile the two KPI lists: the finance scorecard attached as a spreadsheet and the existing definition sheet attached as a document. Show where the formulas differ without choosing one.

## Limitations

- One task at a time: give the skill one job per request and confirm the result before the next.
- You own sensitive-data handling: the skill reads what you give it or what the agent can reach; keep restricted documents out of the knowledge sources you attach.
- The output is a draft, not final authority: every figure, quote and action is for you to verify and perform. The skill never approves, authorises or signs anything off.

## Related skills

- kpi-weekly-report-writer: when the weekly or monthly figures report is wanted, not the definitions
- data-dictionary-builder: when field-level definitions of a table or extract are wanted
- data-quality-issue-log: when a wrong figure should be logged as a defect

## Add it to an agent (Agent Builder)

1. Copilot chat, **Agents & Skills**, **New agent** (or open an existing agent). Frontier enrolment and a Microsoft 365 Copilot licence are required; custom skills are in preview.
2. **Configure**, expand **Skills**, **Add**, upload the zip you downloaded above (the whole zip, never `SKILL.md` alone). Up to eight skills per agent.
3. **Knowledge**: point the agent at a SharePoint library or OneDrive folder holding the documents listed above. Do not upload knowledge files while skills are attached (not supported yet).
4. **Preview**: try one of the example prompts. The description is the trigger, so use its words.

## Run it standalone: paste this into the agent's Instructions

```
Purpose: this agent helps analysts, data owners and reporting teams turn a list of KPIs or metrics into a definition sheet recording, for each KPI, how it is calculated, where its data comes from, who owns it and how often it refreshes, exactly as the supplied documentation states it. General guidelines: read only the KPI list, definition sources and ownership records the user attaches or pastes, and what sits in the knowledge sources configured on this agent; never fill a gap from memory. When a required input is missing, such as the KPI list or the documentation to quote from, ask one question at a time and wait for the answer. Assume no capability beyond chat; if file generation is not available, return the sheet in the chat and say so. Never claim to have saved, sent, published or updated anything; every action is proposed for the user to perform. Every formula, target, cadence and owner is a verbatim quote with source and date; anything no source states reads UNKNOWN. Never compose a formula, set a target, choose between conflicting definitions or name an owner the sources do not name. Every sheet is a draft for human review. A typed confirmation from the user releases a workflow hold; it approves no definition and authorises nothing. For the task: when the user asks to define, document, standardise or reconcile KPIs or metrics, follow the kpi-definition-sheet skill exactly and return one complete Markdown document marked DRAFT.
```

Part of a pack? See `packs/` for an orchestrating Instructions file that runs several skills with gates.

## Files

- `SKILL.md`: the skill (front matter plus instructions, under 20,000 characters).
- `README.md`: companion file referenced from the skill.

Licence CC BY-SA 4.0. The agent prepares; you decide.

Free: [Copilot on One Page](https://www.kesslernity.com/copilot-on-one-page?utm_source=github&utm_medium=readme&utm_campaign=agent_skills_repo&utm_content=skill_footer), a one-page sheet on how to phrase a request to Copilot. Paid: [Agent Instruction Block Design Guide](https://store.kesslernity.com/l/eyeauo?utm_source=github&utm_medium=readme&utm_campaign=agent_skills_repo&utm_content=skill_footer_guide), $19, twelve patterns for an agent's Instructions field. I am the author and the seller.
