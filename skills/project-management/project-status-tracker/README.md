# Project status tracker

Maintains four living project files (overview and progress log, decision log, RAID log, links) from the mail, channel posts, documents and meeting notes the user attaches or the agent can reach, returns each touched file complete in the chat for the user to save, and builds a weekly DRAFT status report from those files. Use when the user asks to "set up tracking for project X", "catch the project files up", "log this decision against the project", "add this risk to the RAID log", "save this link to the project" or "write this week's status report". Do not use for reviewing an existing RAID log for stale or ownerless entries, use raid-log-review instead; for an HTML status page, use project-dashboard-builder; for minutes of one meeting, use meeting-minutes-writer. Drafts for human review; never approves, authorises or signs off.

**[Download the upload package](https://github.com/kesslernity/awesome-copilot-agent-skills/raw/main/dist/zips/project-status-tracker.zip)** (one zip, ready for Agent Builder) · Category: `project-management` · Skill name: `project-status-tracker`

## What to attach or make available

- The four tracker files for the project, project.md, decisions.md, risks.md and links.md, in their current versions
- Mail, channel posts, documents and meeting notes or recaps that mention the project name or its aliases within the agreed window
- The project name, its aliases and the time window for the run, stated by the user

## What you get

- project.md, decisions.md, risks.md, links.md: all four on the first run; afterwards only the files touched, each complete and headed by its file name.
- status-YYYY-WW: the weekly DRAFT status document, only when asked.
- actions.md (date, action, owner, due date, source): only when the user asks for action tracking.
- The closing report from step 7.
Every artefact is complete Markdown in the chat that pastes cleanly into a document, spreadsheet or email; the agent reports nothing as saved. If this agent has a file-generation capability enabled, also offer each returned file as a downloadable file with that name.

## Use cases

| Scenario | What you say |
|---|---|
| First run for a new project | Set up tracking for the customer portal project. Aliases CP and portal-v2; sponsor is the head of digital. Scaffold project.md, decisions.md, risks.md and links.md with UNKNOWN wherever I have not given a value. |
| Weekly catch-up from mail and minutes | Update the files for the lab relocation project from the attached current versions, the two meeting recaps and the email thread pasted below, window since the last Changes entry. Return only the files you touched. |
| Weekly status report for the steering committee | Update then produce the weekly status document for the ERP upgrade: the four current files are attached, window the last seven days, audience the steering committee. Put every risk with no owner under Asks. |

## Try it (example prompts)

- Set up tracking for the Warehouse Relocation project. Aliases are WR and WHREL; the sponsor is the operations director. Scaffold the four files and return them for me to save.
- Catch the project files up for payroll-replacement: the current project.md, decisions.md, risks.md and links.md are attached, plus this week's steering minutes and the sponsor's emails pasted below. Window is the last 14 days.
- Log this decision against the data platform project: the steering group agreed on 12 September to defer the reporting module to phase two. The current decisions.md is attached.
- Add this risk to the RAID log for the office move: the fit-out contractor has not confirmed the November start date; owner is the facilities lead. The current risks.md is attached.
- Write this week's status report for the onboarding redesign from the attached four tracker files. Audience is the steering committee; keep the summary to five lines.

## Limitations

- One task at a time: give the skill one job per request and confirm the result before the next.
- You own sensitive-data handling: the skill reads what you give it or what the agent can reach; keep restricted documents out of the knowledge sources you attach.
- The output is a draft, not final authority: every figure, quote and action is for you to verify and perform. The skill never approves, authorises or signs anything off.

## Related skills

- raid-log-review: when an existing RAID log needs a line-by-line check for stale, duplicate or ownerless entries
- project-dashboard-builder: when the tracker files should become an HTML status page
- meeting-minutes-writer: when the need is the minutes of one meeting rather than a project record

## Add it to an agent (Agent Builder)

1. Copilot chat, **Agents & Skills**, **New agent** (or open an existing agent). Frontier enrolment and a Microsoft 365 Copilot licence are required; custom skills are in preview.
2. **Configure**, expand **Skills**, **Add**, upload the zip you downloaded above (the whole zip, never `SKILL.md` alone). Up to eight skills per agent.
3. **Knowledge**: point the agent at a SharePoint library or OneDrive folder holding the documents listed above. Do not upload knowledge files while skills are attached (not supported yet).
4. **Preview**: try one of the example prompts. The description is the trigger, so use its words.

## Run it standalone: paste this into the agent's Instructions

```
Purpose: you keep a project's record as four living files, project.md, decisions.md, risks.md and links.md, updated from the mail, posts, documents and meeting notes the user provides, and you build a weekly DRAFT status report from those files. You return every touched file complete in the chat for the user to save.

General guidelines: read only what the user attaches or pastes and what sits in your configured knowledge sources; if a source type is not reachable, say so, ask for a paste or export and record the gap. When the project name, the current files, the aliases, the time window or the purpose of the run is missing, ask one question at a time. Never rebuild files from memory: without the current versions, ask for them or confirm a first run. Append and revise only; mark items Superseded, never delete. Every item carries a date and a source; owners, status colours and risk scores come from the sources or the user, never from your judgement, and anything unstated reads UNKNOWN. Never claim to have saved, sent, archived, created a task or moved anything; list those as actions for the user. Every status document carries DRAFT until the user has reviewed it. A typed approval releases a workflow hold for the named step only and authorises nothing else.

For any request to set up, update or report on a project, follow the project-status-tracker skill exactly, including its file templates and self-check.
```

Part of a pack? See `packs/` for an orchestrating Instructions file that runs several skills with gates.

## Files

- `SKILL.md`: the skill (front matter plus instructions, under 20,000 characters).
- `references/file-templates.md`: companion file referenced from the skill.
- `references/raid-log-template.md`: companion file referenced from the skill.

Licence CC BY-SA 4.0. The agent prepares; you decide.
