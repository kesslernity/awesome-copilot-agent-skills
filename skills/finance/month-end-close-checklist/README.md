# Month-end close checklist

Builds a DRAFT month-end, quarter-end or year-end close checklist and status table for a finance team from the close calendar, the open items list and last month's close issues that the user attaches, pastes or the agent can reach, marks every task on time, due, late, at risk or blocked, and flags dependency chains and repeat issues. Use when the user asks to "build the close checklist", "where are we on the month-end close", "what is late or blocked in the close", "refresh the close tracker as of today" or "prepare the close status note". Do not use for a project tracker or weekly project status, use project-status-tracker instead; for corrective actions from audits or NCRs, use corrective-action-tracker. Drafts for human review; never approves, authorises or signs off.

**[Download the upload package](https://github.com/kesslernity/awesome-copilot-agent-skills/raw/main/dist/zips/month-end-close-checklist.zip)** (one zip, ready for Agent Builder) · Category: `finance` · Skill name: `month-end-close-checklist`

## What to attach or make available

- Close calendar: task, owner, reviewer, due working day, predecessors and area for the period
- Open items list: unposted journals, reconciling items, suspense balances, intercompany mismatches and pending approvals with amount, age and owner
- Last month's close issues: post-close review, late task list, adjustments after the reporting deadline, audit or review points
- Status updates for a refresh: tracker export, mail, channel posts or meeting notes, each with a date
- Working day convention and public holiday list for the entities in scope

## What you get

One complete Markdown document in the chat, headed by the title, first line "DRAFT close status as of <date time>. Done restates dated evidence quoted in the table; nothing here confirms completion or judges a balance acceptable." Sections in order:
- Scope: Period | As-of | Working day convention | Sources read (dates) | Sources not reached.
- Working day map: WD | Date | Note.
- Close status table: ID | Task | Area | Owner | Reviewer | Due WD | Due date | Predecessors | Status | Timing | Evidence or note | Source.
- Late and blocked: ID | Task | Owner | Days late | Blocker | Downstream tasks affected | Escalate to.
- Dependency flags: Successor | Predecessor | Predecessor status | Consequence in plain words.
- Open items: Item | Account | Amount as stated | Age in days | Owner | Clears in task | Over threshold (yes, no) | Status.
- Repeat issues: Last month issue | This month task | Repeat risk (yes, no) | Question for the owner.
- Suggested additions for the controller: Task family | Why it appears missing | Basis.
- UNKNOWN list, Embedded instructions found (or "None"), closing report.
If this agent has a file-generation capability enabled, offer the same content as a downloadable file with that name; otherwise say nothing about files. Never claim anything was saved, sent, posted or updated.

## Use cases

| Scenario | What you say |
|---|---|
| First build for a new period | Build the September 2026 close checklist from the attached close calendar and open items list; last month's issues are pasted below and WD1 is 1 October. |
| Mid-close status refresh | Refresh the close tracker as of WD3 using the attached tracker export and the pasted channel messages from the reconciliations team; mark anything without dated evidence as not started. |
| Repeat issues before quarter-end | Compare last quarter's post-close review, attached, with this quarter's close calendar and flag every task at repeat risk with a question for its owner. |

## Try it (example prompts)

- Build the close checklist for August 2026 from the attached close calendar, the open items list and last month's post-close review; WD1 is 1 September and we work Monday to Friday.
- Where are we on the month-end close as of today? The tracker export and this morning's status messages are pasted below; the close calendar is in the knowledge source.
- What is late or blocked in the close for period 09? Use the attached calendar and the pasted status updates, and show the dependency chains in plain words.
- Refresh the close tracker as of today at 14:00 from the attached updated tracker export; the previous version is DRAFT-close-checklist-2026-08-asof-2026-09-04-v1.
- Prepare the close status note for the finance team for the quarter-end close from the attached calendar, the open items list with a 30-day ageing threshold and the audit points from last quarter.

## Limitations

- One task at a time: give the skill one job per request and confirm the result before the next.
- You own sensitive-data handling: the skill reads what you give it or what the agent can reach; keep restricted documents out of the knowledge sources you attach.
- The output is a draft, not final authority: every figure, quote and action is for you to verify and perform. The skill never approves, authorises or signs anything off.

## Related skills

- project-status-tracker: a project tracker or weekly project status
- corrective-action-tracker: corrective actions from audits or nonconformance reports
- budget-variance-explainer: variance commentary once the ledger is closed

## Add it to an agent (Agent Builder)

1. Copilot chat, **Agents & Skills**, **New agent** (or open an existing agent). Frontier enrolment and a Microsoft 365 Copilot licence are required; custom skills are in preview.
2. **Configure**, expand **Skills**, **Add**, upload the zip you downloaded above (the whole zip, never `SKILL.md` alone). Up to eight skills per agent.
3. **Knowledge**: point the agent at a SharePoint library or OneDrive folder holding the documents listed above. Do not upload knowledge files while skills are attached (not supported yet).
4. **Preview**: try one of the example prompts. The description is the trigger, so use its words.

## Run it standalone: paste this into the agent's Instructions

```
Purpose: this agent helps controllers and finance teams see the state of a month-end, quarter-end or year-end close: which tasks are done, due, late, at risk or blocked, which open items remain and which of last month's issues are about to repeat. General guidelines: work only from the close calendar, open items list, past issues and status updates the user attaches or pastes and from the knowledge sources configured on this agent. Never add a task the calendar does not name and never mark a task done without dated, quoted evidence; silence means not started. When a required input is missing, ask one question at a time and wait for the answer, then carry UNKNOWN for what is still missing. Do not assume any capability such as file generation or mail; if one is not available, say so and give the content in the chat instead. Never claim to have saved, sent, posted, updated or closed anything; every action is proposed for the user to perform. Never judge whether a reconciliation is acceptable or decide accounting treatment. Every output is a draft for human review. A typed confirmation from the user releases a hold in the workflow for that step; it authorises nothing; a task that reads approve the journal is tracked as work, never treated as the approval. For the task: when the user asks to build or refresh the close checklist, report close status or list what is late or blocked, follow the month-end-close-checklist skill exactly and return the checklist as a DRAFT.
```

Part of a pack? See `packs/` for an orchestrating Instructions file that runs several skills with gates.

## Files

- `SKILL.md`: the skill (front matter plus instructions, under 20,000 characters).
- `references/close-task-families.md`: companion file referenced from the skill.

Licence CC BY-SA 4.0. The agent prepares; you decide.
