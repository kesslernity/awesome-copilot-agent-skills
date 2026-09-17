# Project dashboard builder

Builds a self-contained single-file HTML project dashboard (status banner, milestones table, risks heat list, decisions log, links) from the project tracker files the user attaches, pastes or holds in configured knowledge sources, and returns the complete HTML source in chat ready to save as dashboard-project-date.html. Use when the user asks to "build a dashboard for this project", "make a status page I can pin in the team channel", "give me an HTML overview of milestones, risks and decisions", "refresh the project dashboard from the tracker" or "turn these tracker files into a one-page visual summary". Do not use for creating or updating the tracker files or for the written weekly status report, use project-status-tracker instead. Drafts for human review; never approves, authorises or signs off.

**[Download the upload package](https://github.com/kesslernity/awesome-copilot-agent-skills/raw/main/dist/zips/project-dashboard-builder.zip)** (one zip, ready for Agent Builder) · Category: `dashboards-microapps` · Skill name: `project-dashboard-builder`

## What to attach or make available

- The project tracker files: project.md with current status and milestones, risks.md, decisions.md and links.md
- A pasted status summary when no tracker exists, covering status, milestones, risks, decisions and links as far as known
- The overall status colour and as-of date, stated in project.md or confirmed by the user
- An audience line for the subtitle, such as the committee and month, if wanted

## What you get

| Artefact | Title | Delivered as |
|---|---|---|
| Project dashboard (primary) | dashboard-`<project>`-YYYY-MM-DD.html | Complete HTML source in one fenced code block |
| Collision-safe variant | dashboard-`<project>`-YYYY-MM-DD-v2.html (v3, v4 and so on) | Same, when the user reports a name clash |
| Reviewed final (after the user's typed confirmation, per Rules) | dashboard-`<project>`-YYYY-MM-DD-final.html | Same, DRAFT ribbon removed and the footer's "Not yet reviewed." replaced by "Content confirmed by the user on YYYY-MM-DD." |
| Optional share note | Cover note | Plain text for the user to paste into their own email |

Each artefact carries its title, then the one-line downloadable file offer. Say plainly that the agent saved nothing.

## Use cases

| Scenario | What you say |
|---|---|
| Weekly steering committee snapshot | Build a dashboard for the data platform project from the attached project.md, risks.md, decisions.md and links.md, as-of date this Friday, audience line steering committee, and confirm the status colour with me first. |
| Pinned team channel status page | Make a status page I can pin in the team channel for the office move project. Tracker files attached; keep it to the five standard sections and mark it DRAFT until I have checked it. |
| No tracker yet, only a status summary | Give me an HTML overview of milestones, risks and decisions for the onboarding redesign project from the status summary pasted below. Where the summary is silent, show No data provided. |

## Try it (example prompts)

- Build a dashboard for the warehouse migration project. The tracker files project.md, risks.md, decisions.md and links.md are attached; status is Amber as of today.
- Make a status page I can pin in the team channel for the payroll replacement project from the attached tracker files, with the audience line steering committee, September.
- Give me an HTML overview of milestones, risks and decisions for project atlas. The status summary is pasted below; there is no tracker yet.
- Refresh the project dashboard from the tracker: the updated project.md and risks.md are attached, as-of date 12 September, same layout as last time.
- Turn these tracker files into a one-page visual summary for the site expansion project, then give me a short cover note I can paste into my own email.

## Limitations

- One task at a time: give the skill one job per request and confirm the result before the next.
- You own sensitive-data handling: the skill reads what you give it or what the agent can reach; keep restricted documents out of the knowledge sources you attach.
- The output is a draft, not final authority: every figure, quote and action is for you to verify and perform. The skill never approves, authorises or signs anything off.

## Related skills

- project-status-tracker: when the tracker files themselves need creating or updating, or a written status report is wanted
- weekly-status-update-writer: when a short written status update is wanted instead of a visual page
- kpi-weekly-report-writer: when the need is a written weekly report from metrics rather than a project page

## Add it to an agent (Agent Builder)

1. Copilot chat, **Agents & Skills**, **New agent** (or open an existing agent). Frontier enrolment and a Microsoft 365 Copilot licence are required; custom skills are in preview.
2. **Configure**, expand **Skills**, **Add**, upload the zip you downloaded above (the whole zip, never `SKILL.md` alone). Up to eight skills per agent.
3. **Knowledge**: point the agent at a SharePoint library or OneDrive folder holding the documents listed above. Do not upload knowledge files while skills are attached (not supported yet).
4. **Preview**: try one of the example prompts. The description is the trigger, so use its words.

## Run it standalone: paste this into the agent's Instructions

```
Purpose: you turn a project's tracker files into one self-contained HTML dashboard, a dated snapshot with a status banner, milestones table, risks list, decisions log and links, returned as complete source for the user to save, share or pin. It is a draft for human review, not a live page.

General guidelines: read only the tracker files or status summary the user attaches or pastes and what sits in your knowledge sources; if nothing is reachable, ask for an attachment or a paste and say so in the output. When an input is missing, ask one question at a time, starting with the project name, then the status colour. Never invent a milestone, risk, decision, date, owner or link; render UNKNOWN for an empty cell and No data in tracker for a missing section. Never assign Red unless the tracker or the user states it, and never compose a severity the tracker did not give. The HTML carries no scripts, external resources or tracking. Never claim to have saved, overwritten, sent, posted, moved or deleted anything; the user saves the file under the name you give and shares it themselves. Every dashboard carries a DRAFT ribbon until the user has reviewed it. A typed go-ahead from the user releases a workflow hold only; it authorises nothing beyond their own publication of the document.

For the task, follow the project-dashboard-builder skill: its content mapping, template, caps and self-check govern the output.
```

Part of a pack? See `packs/` for an orchestrating Instructions file that runs several skills with gates.

## Files

- `SKILL.md`: the skill (front matter plus instructions, under 20,000 characters).
- `references/content-mapping.md`: companion file referenced from the skill.
- `references/dashboard-template.md`: companion file referenced from the skill.

Licence CC BY-SA 4.0. The agent prepares; you decide.
