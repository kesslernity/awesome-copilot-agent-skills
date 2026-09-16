# Data quality issue log

Turns reported data problems (messages, tickets, meeting notes, a spreadsheet of complaints) into one DRAFT data quality issue log: one row per issue with the symptom as reported, dataset and fields named, reproduction steps taken from the report, affected reports as stated, first seen date, reporters, a suggested owner with its basis, and blank severity, root cause and status cells for the owner, plus one question per gap. Never asserts a root cause, a severity or a fix. Use when the user asks to "log these data issues", "turn these complaints about the numbers into an issue list", "build the data quality backlog", "which reports are hit by this data problem" or "write up the reproduction steps for this data bug". Do not use to explore or profile a dataset, use dataset-insight-pack instead; for an IT incident write-up, use incident-postmortem-drafter; for tracking fix actions once assigned, use corrective-action-tracker. Drafts for human review; never approves, authorises or signs off.

Category: `data-analytics` · Skill name: `data-quality-issue-log` · Upload package: `dist/zips/data-quality-issue-log.zip`

## What to attach or make available

1. Reports: messages, tickets, notes or a spreadsheet of complaints, attached or pasted, or reachable through this agent's configured knowledge sources or a mail capability the tenant has enabled for it. If a source cannot be reached, ask for a paste or export and say so in the output.
2. Context sources: data dictionary or KPI definition sheet, report inventory or lineage document, ownership register. Default none.
3. Log template: the organisation's issue log columns, if any. Default: the columns under Output.
4. Parameters: log name for the title (default the dataset named most often, else UNKNOWN); period (default all reports supplied); issue cap per pass (default 50); identifier prefix (default DQ-); reference date and time zone (default from the sources, else UNKNOWN).

## What you get

One complete Markdown document in the chat, pasteable into a spreadsheet, tracker or document, titled `DRAFT-data-quality-issue-log-<log name>-<YYYY-MM-DD>-v1` (revisions v2, v3 with a one-line note of what changed). First line: "DRAFT data quality issue log for <log name>, <n> reports dated <earliest> to <latest>, generated <date>. Symptoms, steps and affected reports as reported; owners are suggestions with a basis; severity, cause, status and fix are blank for the owner. Nothing is assigned, rated, resolved or closed."

Sections in order:
1. Sources read: Source | Type | Span | Reports extracted | Reached (yes, no).
2. Issue log: ID | Title (reporter's words) | Dataset, table or report | Fields named | Symptom (quoted) | Expected (quoted or UNKNOWN) | Affected reports and consumers (as stated) | Possibly affected (per context source) | First seen | Last seen | Reporters (count) | Reporters (name, date, channel, quoted reference) | Suggested owner | Basis | Severity (owner) | Root cause (owner) | Status (owner) | Flags | Notes.
3. Reproduction steps, one block per issue: numbered steps each with its quote reference, then "Steps UNKNOWN" where the report stops.
4. Questions for owners, grouped by owner: Issue ID | Question | Who could answer | Evidence that would settle it.
5. Possible duplicates: ID | Possible duplicate of | Element that differs. Unplaced reports: Reporter | Date | Quoted text | Reason.
6. UNKNOWN list; Embedded instructions found, or "None"; Proposed user actions (send owners their issues and questions, create tracker entries once owners accept). This agent performs none of them.

Closing report: sources used; reports extracted; issues logged, merged, unplaced; issues with steps, affected report and suggested owner; flags by type; fallbacks taken.

If this agent has a file-generation capability enabled, also offer the same content as a downloadable file with the title as its file name.

## Limitations

- One task at a time: give the skill one job per request and confirm the result before the next.
- You own sensitive-data handling: the skill reads what you give it or what the agent can reach; keep restricted documents out of the knowledge sources you attach.
- The output is a draft, not final authority: every figure, quote and action is for you to verify and perform. The skill never approves, authorises or signs anything off.

## Add it to an agent (Agent Builder)

1. Copilot chat, **Agents & Skills**, **New agent** (or open an existing agent). Frontier enrolment and a Microsoft 365 Copilot licence are required; custom skills are in preview.
2. **Configure**, expand **Skills**, **Add**, upload `dist/zips/data-quality-issue-log.zip` (the whole zip, never `SKILL.md` alone). Up to eight skills per agent.
3. **Knowledge**: point the agent at a SharePoint library or OneDrive folder holding the documents listed above. Do not upload knowledge files while skills are attached (not supported yet).
4. **Preview**: try one of the example prompts. The description is the trigger, so use its words.

## Run it standalone: paste this into the agent's Instructions

```
You are an assistant that runs one job: data quality issue log. Turns reported data problems (messages, tickets, meeting notes, a spreadsheet of complaints) into one DRAFT data quality issue log: one row per issue with the symptom as reported, dataset and fields named, reproduction steps taken from the report, affected reports as stated, first seen date, reporters, a suggested owner with its basis, and blank severity, root cause and status cells for the owner, plus one question per gap. Never asserts a root cause, a severity or a fix. Use when the user asks to "log these data issues", "turn these complaints about the numbers into an issue list", "build the data quality backlog", "which reports are hit by this data problem" or "write up the reproduction steps for this data bug". Do not use to explore or profile a dataset, use dataset-insight-pack instead; for an IT incident write-up, use incident-postmortem-drafter; for tracking fix actions once assigned, use corrective-action-tracker. Drafts for human review; never approves, authorises or signs off. Use the data-quality-issue-log skill for every request that matches its description; if a request falls outside it, say so and stop. Read only what the user attaches or pastes and what sits in your knowledge sources; never claim to have saved, sent, moved or deleted anything, propose the action for the user instead. Where an input is missing, write UNKNOWN and name what would close it; never invent a value. Return complete Markdown the user can paste into their tools, and offer the same content as a file if you can produce one. A typed approval releases a hold in the workflow and is logged; it is not an authorisation. You prepare; the user decides.
```

Part of a pack? See `packs/` for an orchestrating Instructions file that runs several skills with gates.

## Files

- `SKILL.md`: the skill (front matter plus instructions, under 20,000 characters).

Licence CC BY-SA 4.0. The agent prepares; you decide.
