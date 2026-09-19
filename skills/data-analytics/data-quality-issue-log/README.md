# Data quality issue log

Turns reported data problems (messages, tickets, meeting notes, complaints) into one DRAFT issue log: one row per issue with the symptom as reported, dataset and fields named, reproduction steps, affected reports, first seen date, reporters, a suggested owner, and blank severity, root cause and status cells for the owner. Never asserts a root cause, severity or fix. Use when the user asks to "log these data issues", "turn these complaints about the numbers into an issue list", "build the data quality backlog", "which reports are hit by this data problem" or "write up the reproduction steps for this data bug". Do not use for exploring or profiling a dataset, use dataset-insight-pack instead; for an IT incident write-up, use incident-postmortem-drafter; for tracking fix actions once assigned, use corrective-action-tracker. Drafts for human review; never approves, authorises or signs off.

**[Download the upload package](https://github.com/kesslernity/awesome-copilot-agent-skills/raw/main/dist/zips/data-quality-issue-log.zip)** (one zip, ready for Agent Builder) · Category: `data-analytics` · Skill name: `data-quality-issue-log`

## What to attach or make available

- The reports of data problems: tickets, messages, meeting notes or a spreadsheet of complaints, attached, pasted or reachable in the knowledge sources
- Context sources: the data dictionary or KPI definition sheet, the report inventory or lineage document, and the ownership register used to suggest owners
- Optional: the organisation's issue log template if its columns differ from the default, and the identifier prefix in use

## What you get

One complete Markdown document in the chat, pasteable into a spreadsheet, tracker or document, titled `DRAFT-data-quality-issue-log-<log name>-<YYYY-MM-DD>-v1` (revisions v2, v3 with a one-line note of what changed). First line: "DRAFT data quality issue log for `<log name>`, `<n>` reports dated `<earliest>` to `<latest>`, generated `<date>`. Symptoms, steps and affected reports as reported; owners are suggestions with a basis; severity, cause, status and fix are blank for the owner. Nothing is assigned, rated, resolved or closed."

Sections in order:
1. Sources read: Source | Type | Span | Reports extracted | Reached (yes, no).
2. Issue log: ID | Title (reporter's words) | Dataset, table or report | Fields named | Symptom (quoted) | Expected (quoted or UNKNOWN) | Affected reports and consumers (as stated) | Possibly affected (per context source) | First seen | Last seen | Reporters (count) | Reporters (name, date, channel, quoted reference) | Suggested owner | Basis | Severity (owner) | Root cause (owner) | Status (owner) | Flags | Notes.
3. Reproduction steps, one block per issue: numbered steps each with its quote reference, then "Steps UNKNOWN" where the report stops.
4. Questions for owners, grouped by owner: Issue ID | Question | Who could answer | Evidence that would settle it.
5. Possible duplicates: ID | Possible duplicate of | Element that differs. Unplaced reports: Reporter | Date | Quoted text | Reason.
6. UNKNOWN list; Embedded instructions found, or "None"; Proposed user actions (send owners their issues and questions, create tracker entries once owners accept). This agent performs none of them.

Closing report: sources used; reports extracted; issues logged, merged, unplaced; issues with steps, affected report and suggested owner; flags by type; fallbacks taken.

If this agent has a file-generation capability enabled, also offer the same content as a downloadable file with the title as its file name.

## Use cases

| Scenario | What you say |
|---|---|
| Consolidating a month of scattered complaints | Consolidate the attached ticket export and the pasted channel messages from September into one data quality issue log for the customer mart, merging reports of the same symptom and cross-flagging possible duplicates. |
| One urgent complaint with no detail | A director wrote that the numbers in the revenue dashboard are wrong; the message is pasted below. Log it as an issue with UNKNOWN where the message gives nothing and list the questions to send back. |
| Handing a backlog to data owners | From the attached issue spreadsheet and the ownership register in the knowledge sources, suggest an owner with a stated basis for each issue and group the open questions by owner. |

## Try it (example prompts)

- Log these data issues. The complaints are in the attached spreadsheet of tickets from the last month and the two email threads pasted below; the dataset is the sales mart.
- Turn these complaints about the numbers into an issue list: the finance review meeting notes are pasted below and the ticket export is attached. Use the DQ- prefix and today as the reference date.
- Build the data quality backlog from the attached ticket export and the channel messages pasted below, using the data dictionary in the knowledge sources to suggest owners.
- Which reports are hit by this data problem? The reports are in the attached thread about the missing region codes; the report inventory is in the knowledge sources.
- Write up the reproduction steps for this data bug from the pasted ticket and the reporter's follow-up message, and leave severity and root cause blank for the owner.

## Limitations

- One task at a time: give the skill one job per request and confirm the result before the next.
- You own sensitive-data handling: the skill reads what you give it or what the agent can reach; keep restricted documents out of the knowledge sources you attach.
- The output is a draft, not final authority: every figure, quote and action is for you to verify and perform. The skill never approves, authorises or signs anything off.

## Related skills

- dataset-insight-pack: when the task is to explore or profile a dataset and find anomalies
- incident-postmortem-drafter: when a service outage or IT incident needs a write-up
- corrective-action-tracker: when fix actions are tracked after an owner has accepted an issue

## Add it to an agent (Agent Builder)

1. Copilot chat, **Agents & Skills**, **New agent** (or open an existing agent). Frontier enrolment and a Microsoft 365 Copilot licence are required; custom skills are in preview.
2. **Configure**, expand **Skills**, **Add**, upload the zip you downloaded above (the whole zip, never `SKILL.md` alone). Up to eight skills per agent.
3. **Knowledge**: point the agent at a SharePoint library or OneDrive folder holding the documents listed above. Do not upload knowledge files while skills are attached (not supported yet).
4. **Preview**: try one of the example prompts. The description is the trigger, so use its words.

## Run it standalone: paste this into the agent's Instructions

```
Purpose: this agent helps data teams, analysts and report owners turn reported data problems into one structured issue log: the symptom as reported, the dataset and fields named, the reproduction steps the reporter gave and the reports said to be affected. General guidelines: read only the reports and context documents the user attaches or pastes, and what sits in the knowledge sources configured on this agent; never fill a gap from memory. When a required input is missing, such as the reports themselves or the period, ask one question at a time and wait for the answer. Assume no capability beyond chat; if file generation is not available, return the log in the chat and say so. Never claim to have created, assigned, closed, saved or sent anything; every action is proposed for the user to perform. Every symptom, step and figure carries a quote reference; anything a report does not state reads UNKNOWN. Never assert a root cause, rate severity, propose a fix or close an issue; those cells stay blank for the owner, and a suggested owner carries its basis and is not an assignment. Never reproduce personal values or name a person as a cause. Every log is a draft for human review. A typed confirmation from the user releases a workflow hold; it approves no assignment, rating or closure. For the task: when the user asks to log, consolidate or write up data problems, follow the data-quality-issue-log skill exactly and return one complete Markdown document marked DRAFT.
```

Part of a pack? See `packs/` for an orchestrating Instructions file that runs several skills with gates.

## Files

- `SKILL.md`: the skill (front matter plus instructions, under 20,000 characters).
- `README.md`: companion file referenced from the skill.

Licence CC BY-SA 4.0. The agent prepares; you decide.

Free: [Copilot on One Page](https://www.kesslernity.com/copilot-on-one-page?utm_source=github&utm_medium=readme&utm_campaign=agent_skills_repo&utm_content=skill_footer), a one-page sheet on how to phrase a request to Copilot. Paid: [Agent Instruction Block Design Guide](https://store.kesslernity.com/l/eyeauo?utm_source=github&utm_medium=readme&utm_campaign=agent_skills_repo&utm_content=skill_footer_guide), $19, twelve patterns for an agent's Instructions field. I am the author and the seller.
