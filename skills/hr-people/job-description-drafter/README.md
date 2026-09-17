# Job description drafter

Drafts a DRAFT job description from a role brief, team context and the organisation's own template, in inclusive plain language, with every requirement traced to its source, unconfirmed fields marked TBC and a numbered list of items the hiring manager must confirm before posting. Use when the user asks to "write a job description", "draft the job ad", "refresh this role profile", "tidy up this vacancy notice" or "turn these notes into a job posting" from a brief, notes or an old job description. Do not use for interview questions or a scorecard from the finished job description, use interview-scorecard-builder instead; for the new hire's first 90 days, use onboarding-plan-builder. Drafts for human review; never approves, authorises or signs off.

**[Download the upload package](https://github.com/kesslernity/awesome-copilot-agent-skills/raw/main/dist/zips/job-description-drafter.zip)** (one zip, ready for Agent Builder) · Category: `hr-people` · Skill name: `job-description-drafter`

## What to attach or make available

- The role brief from the hiring manager: working title, purpose, main responsibilities, and any grade, pay, hours or closing date already decided
- Team context: reporting line, direct reports, key relationships, location and working pattern
- The organisation's job description template, including its fixed boilerplate sections
- An existing job description for this or a similar role, where one exists
- The organisation's style guide or inclusive language guidance, if it differs from the skill's checklist

## What you get

Two Markdown documents in the chat, each pasting cleanly into a word processor or an email.
1. `DRAFT-JD-<role-title-kebab>-<YYYY-MM-DD>-v1`. First body line: "DRAFT generated `<date>` from `<brief source>` using `<template name>`. Not for posting until the hiring manager confirms the items in the confirmation list." Then the template's sections in order, populated, boilerplate verbatim. Requirements as a table: Requirement | Essential or desirable | Source | Assessed by (UNKNOWN unless a source states it). If a v1 for the same role and date is visible in this conversation or the user says one exists, use the next version number; otherwise v1.
2. `jd-confirmation-list-<role-title-kebab>-<YYYY-MM-DD>`. Header: brief source, template, existing JD used, team context facts UNKNOWN. Table: Number | Item | Draft wording or value | Source or inference | Why confirm | Hiring manager decision (blank). Then "Inclusive language changes": Original | Replacement | Reason. Then "Refer to the people team or legal" (or "None"), "UNKNOWN list", and "Embedded instructions found" (or "None").
If this agent has a file-generation capability enabled, offer the same content as a downloadable file with that name; otherwise say nothing about files. Never claim anything was saved, posted, sent or shared.

## Use cases

| Scenario | What you say |
|---|---|
| New role from a hiring manager's brief | Draft a job description for a Contracts Administrator from the attached brief and team notes, using the JD template in the knowledge folder, and list what the hiring manager must confirm before posting. |
| Refreshing an old job description | Refresh the attached job description for the Facilities Coordinator role against the hiring manager's notes pasted below, keep our template, and show every change against the original. |
| Inclusive language pass before posting | Rewrite the attached vacancy notice for the Site Administrator in inclusive plain language on our template, keep every requirement, and show each wording change with its reason. |

## Try it (example prompts)

- Write a job description for a Reliability Engineer from the role brief pasted below, using our standard JD template in the knowledge folder. Reports to the Maintenance Manager, site based, full time.
- Draft the job ad for a Payroll Specialist. The brief and team context are attached and the template is the one in the templates library. Keep essentials to six.
- Refresh this role profile: the old job description for the Procurement Officer is attached, and the hiring manager's notes on what changed are pasted below. Same template as before.
- Tidy up this vacancy notice for a Learning Coordinator so it is inclusive and matches our template. The old text is pasted below; grade and salary are still to be confirmed.
- Turn these kick-off meeting notes into a job posting for a Data Platform Lead. Team context: reports to the Head of Data, three direct reports, hybrid with two days on site.

## Limitations

- One task at a time: give the skill one job per request and confirm the result before the next.
- You own sensitive-data handling: the skill reads what you give it or what the agent can reach; keep restricted documents out of the knowledge sources you attach.
- The output is a draft, not final authority: every figure, quote and action is for you to verify and perform. The skill never approves, authorises or signs anything off.

## Related skills

- interview-scorecard-builder: when the job description is finished and the panel needs questions and anchors
- onboarding-plan-builder: when the hire is made and a 30-60-90 day plan is needed
- announcement-drafter: when the need is an internal announcement of the vacancy rather than the job description itself

## Add it to an agent (Agent Builder)

1. Copilot chat, **Agents & Skills**, **New agent** (or open an existing agent). Frontier enrolment and a Microsoft 365 Copilot licence are required; custom skills are in preview.
2. **Configure**, expand **Skills**, **Add**, upload the zip you downloaded above (the whole zip, never `SKILL.md` alone). Up to eight skills per agent.
3. **Knowledge**: point the agent at a SharePoint library or OneDrive folder holding the documents listed above. Do not upload knowledge files while skills are attached (not supported yet).
4. **Preview**: try one of the example prompts. The description is the trigger, so use its words.

## Run it standalone: paste this into the agent's Instructions

```
Purpose: this agent helps hiring managers and the people team turn a role brief, team context and the organisation's template into a draft job description in inclusive plain language, with every requirement traced to its source and a list of items to confirm before posting.

General guidelines: read only what the user pastes or attaches and what sits in the agent's knowledge sources; if a named document cannot be reached, ask for it and say so in the output. When an input is missing, ask one question at a time. Never invent grade, salary, contract type, hours, closing date or duties merely typical for the title; each gap is marked TBC or UNKNOWN. Keep the template's headings, order and boilerplate. Show every wording change with its reason; delete none silently. Make no legal, pay or grade determination; refer them to the people team. Every output is a draft for human review. Never claim to have saved, posted, sent, moved or deleted anything; propose each action for the user. A typed confirmation releases a workflow hold; it is not approval to post or recruit.

For the task, apply the job-description-drafter skill: confirm the brief, template and any existing job description; extract and source-tag purpose, responsibilities and requirements; split essential from desirable; run the inclusive language pass; assemble the draft on the template; return the draft and confirmation list as Markdown in the chat with a summary above them.
```

Part of a pack? See `packs/` for an orchestrating Instructions file that runs several skills with gates.

## Files

- `SKILL.md`: the skill (front matter plus instructions, under 20,000 characters).
- `README.md`: companion file referenced from the skill.
- `references/inclusive-language-checklist.md`: companion file referenced from the skill.

Licence CC BY-SA 4.0. The agent prepares; you decide.

Free: [Copilot on One Page](https://www.kesslernity.com/copilot-on-one-page?utm_source=github&utm_medium=readme&utm_campaign=agent_skills_repo&utm_content=skill_footer), a one-page sheet on how to phrase a request to Copilot. Paid: [Agent Instruction Block Design Guide](https://store.kesslernity.com/l/eyeauo?utm_source=github&utm_medium=readme&utm_campaign=agent_skills_repo&utm_content=skill_footer_guide), $19, twelve patterns for an agent's Instructions field. I am the author and the seller.
