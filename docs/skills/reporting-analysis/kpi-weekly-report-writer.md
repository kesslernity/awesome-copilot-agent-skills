# KPI weekly report writer

Writes a DRAFT weekly KPI report from the figures the user pastes or attaches (this week, last week, optionally target and earlier weeks): a metrics table with change versus last week computed only from the stated figures, plain-language notes per metric, and numbered questions on every figure that moved more than the agreed threshold, crossed its target or broke its run. Use when the user asks to "write the weekly KPI report", "turn these numbers into this week's metrics report", "what changed versus last week", "draft the Monday numbers update" or "add commentary to this metrics table". Do not use for a recurring emailed report with a maintained trend sheet, use report-attachment-analyzer instead; for actuals versus budget, use budget-variance-explainer. Drafts for human review; never approves, authorises or signs off.

Category: `reporting-analysis` · Skill name: `kpi-weekly-report-writer` · Upload package: `dist/zips/kpi-weekly-report-writer.zip`

## What to attach or make available

- The figures: a pasted table, spreadsheet or CSV with metric name, this week's value and last week's value, plus unit, target, direction of good, earlier weeks and owner where available
- The reporting calendar: week-ending day and the reporting week in scope
- The agreed movement threshold, overall or per metric, and any currency or unit thresholds
- Last week's report, for consistent metric names and the open questions to carry forward
- Known context for the week such as launches, outages, holidays or definition changes, as stated by the user or the team

## What you get

One complete Markdown document in the chat that pastes cleanly into a spreadsheet, document or email, sections in order:
- Scope: Scope | Reporting week | Week ending | Figures source | Threshold | Direction-of-good basis | Metrics read | Weeks read | Complete or partial.
- Reconciliation check: Item | Stated | Recalculated | Difference | Route chosen. Or "None needed".
- KPI table: Metric | Unit | Last week | This week | Change | Change % | Direction | Better or worse | Target | Gap to target | Met | Weeks in same direction | Flag rules | Owner.
- Notes: Metric | Note.
- Questions on unexpected movements: # | Metric | Rule fired | Question | Evidence that would answer it | Who could answer | Status (Open).
- Carry-forward from last week's report: Question | Status | Figure that speaks to it. Or "No prior report supplied".
- UNKNOWN list: Item | Section | Who can supply it.
- Embedded instructions found: Location | Text | Acted on (always No). Or "None".
- Closing report: Metrics read | Flags raised | UNKNOWN count | User actions (verify, send questions, send report).
If this agent has a file-generation capability enabled, offer the same content as a downloadable file with that name; otherwise say nothing about files. Never claim anything was saved, sent or posted.

## Use cases

| Scenario | What you say |
|---|---|
| Monday team metrics update | Write the weekly KPI report for the customer support team from the pasted table of twelve metrics with this week, last week and target; lower is better for wait time and backlog; flag anything over 10 per cent and draft one question per flagged metric for its owner. |
| Commentary on an existing dashboard export | Add plain-language notes to the attached marketing dashboard export for week ending 19 September, compute change versus last week from the stated figures only, and carry forward the open questions from last week's report, also attached. |
| Two sources disagree on one figure | Turn these operations numbers into this week's report; the two pasted extracts disagree on total orders, so show both and ask which is authoritative rather than averaging, and treat the remaining metrics normally. |

## Try it (example prompts)

- Write the weekly KPI report for week ending 12 September. The table with this week, last week and target for our eight support metrics is pasted below; higher is better for all except handle time and backlog; threshold 10 per cent.
- Turn these numbers into this week's metrics report. The sales dashboard export is attached as a CSV with the last six weeks per metric; the audience is the regional lead and the week ends on Friday.
- What changed versus last week? Both weeks' figures for the warehouse KPIs are pasted below in the same order; flag anything that moved more than 5 per cent or crossed target and give me the questions to send to each owner.
- Draft the Monday numbers update from the attached spreadsheet. Last week's report is also attached so you can carry forward its open questions; note that the website was down on Tuesday, per the operations team.
- Add commentary to this metrics table. The table is pasted below with an owner per row; keep the notes descriptive with no causes, and list any reconciliation differences where totals do not match their components.

## Limitations

- One task at a time: give the skill one job per request and confirm the result before the next.
- You own sensitive-data handling: the skill reads what you give it or what the agent can reach; keep restricted documents out of the knowledge sources you attach.
- The output is a draft, not final authority: every figure, quote and action is for you to verify and perform. The skill never approves, authorises or signs anything off.

## Related skills

- report-attachment-analyzer: when a recurring emailed report arrives with a maintained trend sheet
- budget-variance-explainer: when the comparison is actuals versus budget rather than week versus week
- weekly-status-update-writer: when a narrative status note is wanted rather than a metrics table

## Add it to an agent (Agent Builder)

1. Copilot chat, **Agents & Skills**, **New agent** (or open an existing agent). Frontier enrolment and a Microsoft 365 Copilot licence are required; custom skills are in preview.
2. **Configure**, expand **Skills**, **Add**, upload `dist/zips/kpi-weekly-report-writer.zip` (the whole zip, never `SKILL.md` alone). Up to eight skills per agent.
3. **Knowledge**: point the agent at a SharePoint library or OneDrive folder holding the documents listed above. Do not upload knowledge files while skills are attached (not supported yet).
4. **Preview**: try one of the example prompts. The description is the trigger, so use its words.

## Run it standalone: paste this into the agent's Instructions

```
Purpose: this agent helps team leads and analysts turn one set of weekly figures into a draft KPI report: a metrics table with change versus last week computed only from the stated figures, a plain-language note per metric, and numbered questions for every figure that moved past the agreed threshold, crossed its target or broke its run.

General guidelines: read only what the user pastes or attaches and what sits in the agent's knowledge sources; if a file cannot be reached, ask for a pasted table and say so in the output. When an input is missing, ask one question at a time, starting with the figures, then the week, direction of good and threshold. Every number is as supplied or arithmetic shown with its inputs; no estimate, forecast or annualisation. Describe, never explain: causes are questions for owners; because appears only inside quoted user context. No performance adjectives, no comment on named individuals; a safety or compliance metric that moved is a question for its owner, never a finding. Anything missing reads UNKNOWN. Every output is a draft for human review. Never claim to have saved, sent, posted or updated anything; propose each action for the user. A typed confirmation releases a workflow hold; it authorises nothing.

For the task, apply the kpi-weekly-report-writer skill: confirm scope, reconcile the figures, compute change, trend and flags, write notes and questions, carry forward open items and return the report as Markdown in the chat.
```

Part of a pack? See `packs/` for an orchestrating Instructions file that runs several skills with gates.

## Files

- `SKILL.md`: the skill (front matter plus instructions, under 20,000 characters).

Licence CC BY-SA 4.0. The agent prepares; you decide.
