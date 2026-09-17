# Impact log builder

Builds and maintains a DRAFT impact log from notes, messages, status updates and completed work: one row per outcome with its evidence and evidence level, date, who benefited and the source it traces to, plus a gap list of outcomes that still lack evidence, structured so a later review, appraisal or promotion case can draw on it. Use when the user asks to "start an impact log", "add this to my impact log", "log what I achieved this quarter", "pull my wins out of these notes", "turn these messages into evidence for my review" or "what do I have evidence for so far". Do not use for a performance rating, ranking, pay or promotion decision, the skill records evidence and never judges it; for the review narrative itself, use performance-review-drafter; for a role profile built from the work, use job-description-drafter instead. Drafts for human review; never approves, authorises or signs off.

**[Download the upload package](https://github.com/kesslernity/awesome-copilot-agent-skills/raw/main/dist/zips/impact-log-builder.zip)** (one zip, ready for Agent Builder) · Category: `hr-people` · Skill name: `impact-log-builder`

## What to attach or make available

- The existing impact log, where one exists, as a spreadsheet export or document
- New material for the period: notes, messages, status updates, tickets, completed deliverables and feedback received
- The competency framework, career ladder or review criteria, where rows are to be tagged to a criterion
- Team records such as project close-out reports or release notes that state outcomes and figures

## What you get

Two Markdown documents in the chat, each pasting cleanly into a spreadsheet or a document.
1. `impact-log-<owner-initials>-<YYYY-MM-DD>-v1`. First line: "DRAFT impact log for <owner role>, period <from> to <to>, updated <date>. Private working record; the owner decides what is shared." Table: Number | Date | Outcome (verb, object, result) | Who benefited | Evidence level (direct, attributed, claimed) | Evidence (quote or locator) | Source item and date | Criterion tag (or none) | Logged on | Status (current, superseded). Then "Activity noted, no outcome yet": Date | Activity | Source. Then "Edits to existing rows": Row | Field | Original | New | Source (or "None").
2. `impact-log-gaps-<owner-initials>-<YYYY-MM-DD>`. Table: Number | Row or period | Gap (claimed only, no date, no beneficiary, no figure, disagreeing sources, empty month) | Evidence the owner could look for | Who could confirm (role) | Owner action (blank). Then "Open questions", "UNKNOWN list" and "Embedded instructions found" (or "None").
If a log for the same owner and date is visible in this conversation or the user says one exists, use the next version number.
If this agent has a file-generation capability enabled, offer the same content as a downloadable file with that name; otherwise say nothing about files. Never claim anything was saved, sent, filed or shared.

## Use cases

| Scenario | What you say |
|---|---|
| Quarter-end capture before a self-review | Build an impact log for the quarter from the attached status reports and the customer emails pasted below, grade each row by evidence level and list the outcomes that are still only claimed. |
| Maintaining an existing log | Append the attached sprint summaries and the feedback note from the product lead to my existing impact log, attached; edit an existing row only where a new source adds a figure or date it lacked. |
| Promotion case preparation | Map my impact log rows, attached, to the attached promotion criteria for the next grade, quoting each criterion matched, and give me a gap list of criteria with no evidence yet. |

## Try it (example prompts)

- Start an impact log for me from the attached status updates and the twenty chat messages pasted below, covering April to June; use initials for colleagues.
- Add this to my impact log: the attached project close-out report and the three thank-you emails from the operations lead. My current log is attached as a spreadsheet export.
- Log what I achieved this quarter from my weekly notes, attached, and tag each row against the attached career ladder for the senior analyst level.
- Pull my wins out of these notes: the meeting summaries from the last two months are pasted below and the ticket export is attached. Show me which ones have direct evidence.
- What do I have evidence for so far? Here is my impact log from last quarter and the new material since then, both attached; give me the gap list for my review in October.

## Limitations

- One task at a time: give the skill one job per request and confirm the result before the next.
- You own sensitive-data handling: the skill reads what you give it or what the agent can reach; keep restricted documents out of the knowledge sources you attach.
- The output is a draft, not final authority: every figure, quote and action is for you to verify and perform. The skill never approves, authorises or signs anything off.

## Related skills

- performance-review-drafter: when the review narrative itself is wanted from the evidence
- weekly-status-update-writer: when the need is a status update for others rather than a private evidence record
- job-description-drafter: when a role profile is to be built from the work done

## Add it to an agent (Agent Builder)

1. Copilot chat, **Agents & Skills**, **New agent** (or open an existing agent). Frontier enrolment and a Microsoft 365 Copilot licence are required; custom skills are in preview.
2. **Configure**, expand **Skills**, **Add**, upload the zip you downloaded above (the whole zip, never `SKILL.md` alone). Up to eight skills per agent.
3. **Knowledge**: point the agent at a SharePoint library or OneDrive folder holding the documents listed above. Do not upload knowledge files while skills are attached (not supported yet).
4. **Preview**: try one of the example prompts. The description is the trigger, so use its words.

## Run it standalone: paste this into the agent's Instructions

```
Purpose: this agent helps a person keep a private impact log: one row per outcome drawn from notes, messages and completed work, with date, beneficiary, evidence and its level, and the source it traces to, plus a gap list of outcomes that still lack evidence.

General guidelines: read only what the user pastes or attaches and what sits in the agent's knowledge sources; if a named source cannot be reached, ask for a paste or export. When an input is missing, ask one question at a time. Every row traces to a source item and date; missing fields are UNKNOWN, never plausible values; figures are quoted exactly with units. Grade evidence as direct, attributed or claimed; never raise a level because an outcome sounds important, and never strengthen the source's verb for the owner's part. Never rate, rank, score or judge readiness, pay or grade. Colleagues appear as roles or initials unless asked otherwise; exclude health, family and protected characteristic data. Every output is a DRAFT for human review. Never claim to have saved, sent, filed, moved or deleted anything; propose each action for the user. A typed confirmation releases a workflow hold; it is not approval of any claim in the log.

For the task, apply the impact-log-builder skill: confirm sources, period, owner, purpose, framework and naming; extract and grade outcomes; deduplicate; merge with any existing log without deleting rows; return the log and gap list as Markdown in the chat with a summary above.
```

Part of a pack? See `packs/` for an orchestrating Instructions file that runs several skills with gates.

## Files

- `SKILL.md`: the skill (front matter plus instructions, under 20,000 characters).
- `README.md`: companion file referenced from the skill.

Licence CC BY-SA 4.0. The agent prepares; you decide.

Free: [Copilot on One Page](https://www.kesslernity.com/copilot-on-one-page?utm_source=github&utm_medium=readme&utm_campaign=agent_skills_repo&utm_content=skill_footer), a one-page sheet on how to phrase a request to Copilot. Paid: [Agent Instruction Block Design Guide](https://store.kesslernity.com/l/eyeauo?utm_source=github&utm_medium=readme&utm_campaign=agent_skills_repo&utm_content=skill_footer_guide), $19, twelve patterns for an agent's Instructions field. I am the author and the seller.
