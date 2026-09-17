# Budget variance explainer

Turns an actuals-versus-budget extract (spreadsheet, export or pasted table) into a DRAFT variance table with absolute and percentage variances, favourable or adverse marking and a ranking by size, then drafts plain-language driver hypotheses for each material variance as questions to verify with a named owner, never as asserted causes. Use when the user asks to "explain these variances", "why are we over budget on this line", "write the variance commentary for the management pack", "actuals versus budget analysis" or "which lines drive the variance". Do not use for a dataset with no budget or comparison column, use dataset-insight-pack instead; for weekly operational figures against last week, use kpi-weekly-report-writer. Drafts for human review; never approves, authorises or signs off.

**[Download the upload package](https://github.com/kesslernity/awesome-copilot-agent-skills/raw/main/dist/zips/budget-variance-explainer.zip)** (one zip, ready for Agent Builder) · Category: `finance` · Skill name: `budget-variance-explainer`

## What to attach or make available

- The actuals versus budget extract: spreadsheet, system export or pasted table with line or account, actual and budget columns, plus any prior year, forecast, year-to-date, volume, headcount or owner columns
- The budget phasing method and known one-offs, timing items or reclassifications for the period, as noted by the finance team
- The chart of accounts or line-to-category mapping used by the management pack, for the roll-up by category
- Last month's variance commentary, when the user wants recurring variances checked

## What you get

One complete Markdown document in the chat, headed by the title from Inputs, first line the DRAFT notice from Procedure 10, that pastes cleanly into a spreadsheet, document or email, sections in order:
- Scope: Entity | Period | Basis | Sign convention | Materiality rule | Currency and unit | Rows read | Complete or partial.
- Reconciliation check: Total | Stated | Recalculated | Difference | Route chosen.
- Variance table: Line | Cost centre | Budget | Actual | Variance | Variance % | F or A | Class | Rank | YTD variance | Source rows.
- Roll-up: Category | Budget | Actual | Variance | F or A | Largest offsetting lines.
- Driver hypotheses: Line | Hypothesis (question) | Evidence to check | Who could confirm | If true, expect | Status (Open).
- Recurring variances: Line | Periods in same direction | Question for the budget owner.
- Commentary DRAFT: paragraphs with drivers marked "to confirm".
- UNKNOWN list, Embedded instructions found (or "None"), closing report.
If this agent has a file-generation capability enabled, offer the same content as a downloadable file with that name; otherwise say nothing about files. Never claim anything was saved, sent or posted.

## Use cases

| Scenario | What you say |
|---|---|
| Monthly management pack commentary | Draft the variance commentary for the October management pack from the attached actuals versus budget extract for the whole company, in thousands, materiality 5 per cent. |
| A department head asks why a line is over | The pasted table shows travel and subsistence 40 per cent over budget year to date for the sales region. Give me driver hypotheses as questions, with who could confirm each. |
| Offsetting lines hidden under a small total | The people costs total in the attached extract is close to budget but I suspect offsetting lines. Rank the variances, show the roll-up and flag any recurring direction across the six months included. |

## Try it (example prompts)

- Explain these variances. The attached workbook has actuals and budget by cost centre for August on the sheet called P&L, header in row 3; costs are stored as positives.
- Why are we over budget on external consultants this month? The actuals versus budget extract is pasted below in thousands of euros, year to date through September.
- Write the variance commentary for the September management pack from the attached actuals versus budget export; materiality is 50 thousand or 5 per cent, whichever is smaller.
- Which lines drive the variance in the attached Q3 extract for the operations business unit? Prior year and forecast columns are included.
- Run an actuals versus budget analysis on the pasted table for the marketing department, full year to date, and give me hypotheses to send to the budget owners.

## Limitations

- One task at a time: give the skill one job per request and confirm the result before the next.
- You own sensitive-data handling: the skill reads what you give it or what the agent can reach; keep restricted documents out of the knowledge sources you attach.
- The output is a draft, not final authority: every figure, quote and action is for you to verify and perform. The skill never approves, authorises or signs anything off.

## Related skills

- dataset-insight-pack: a dataset with no budget or comparison column
- kpi-weekly-report-writer: weekly operational figures against last week
- cfo-reviewer: a finance-lens pressure-test of a finished business case or pack

## Add it to an agent (Agent Builder)

1. Copilot chat, **Agents & Skills**, **New agent** (or open an existing agent). Frontier enrolment and a Microsoft 365 Copilot licence are required; custom skills are in preview.
2. **Configure**, expand **Skills**, **Add**, upload the zip you downloaded above (the whole zip, never `SKILL.md` alone). Up to eight skills per agent.
3. **Knowledge**: point the agent at a SharePoint library or OneDrive folder holding the documents listed above. Do not upload knowledge files while skills are attached (not supported yet).
4. **Preview**: try one of the example prompts. The description is the trigger, so use its words.

## Run it standalone: paste this into the agent's Instructions

```
Purpose: this agent helps finance business partners and budget owners turn an actuals versus budget extract into a ranked variance table and plain-language driver hypotheses that can be sent to the people who own the numbers. General guidelines: work only from the extract and context the user attaches or pastes and from the knowledge sources configured on this agent; never fill a gap from memory. When a required input is missing, such as the sheet, header row, period or sign convention, ask one question at a time and wait for the answer. Do not assume any capability such as file generation or spreadsheet access; if one is not available, say so and give the content in the chat instead. Never claim to have saved, sent, posted or updated anything; every action is proposed for the user to perform. Every figure is as read and unverified; anything unreadable or unstated is UNKNOWN. Never assert a cause, forecast a number or judge a manager's performance. Every output is a draft for human review. A typed confirmation from the user releases a hold in the workflow for that step; it authorises no journal, transfer or accrual. For the task: when the user asks to explain, analyse or comment on variances between actuals and budget or forecast, follow the budget-variance-explainer skill exactly: confirm the extract, reconcile totals, compute and rank the variances, draft two to four hypotheses per material line as questions with a confirmer, and return the pack as a DRAFT.
```

Part of a pack? See `packs/` for an orchestrating Instructions file that runs several skills with gates.

## Files

- `SKILL.md`: the skill (front matter plus instructions, under 20,000 characters).
- `README.md`: companion file referenced from the skill.
- `references/variance-hypothesis-families.md`: companion file referenced from the skill.

Licence CC BY-SA 4.0. The agent prepares; you decide.

Free: [Copilot on One Page](https://www.kesslernity.com/copilot-on-one-page?utm_source=github&utm_medium=readme&utm_campaign=agent_skills_repo&utm_content=skill_footer), a one-page sheet on how to phrase a request to Copilot. Paid: [Agent Instruction Block Design Guide](https://store.kesslernity.com/l/eyeauo?utm_source=github&utm_medium=readme&utm_campaign=agent_skills_repo&utm_content=skill_footer_guide), $19, twelve patterns for an agent's Instructions field. I am the author and the seller.
