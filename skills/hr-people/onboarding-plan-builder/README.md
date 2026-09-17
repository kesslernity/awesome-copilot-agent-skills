# Onboarding plan builder

Produces a DRAFT 30-60-90 day onboarding plan for a new hire from the role, the team context and the systems list: phase outcomes traced to the role, activities with a named owner and due window, an access and equipment request table, learning items, manager checkpoints and the items the manager must confirm. Use when the user asks to "build an onboarding plan for our new hire", "draft the induction plan for this role", "write a first 90 days plan", "put together a new starter plan with owners", "create a ramp plan from this job description" or "plan the integration of an internal mover". Do not use for writing the job description itself, use job-description-drafter instead; for interview questions or a scorecard, use interview-scorecard-builder. Drafts for human review; never approves, authorises or signs off.

**[Download the upload package](https://github.com/kesslernity/awesome-copilot-agent-skills/raw/main/dist/zips/onboarding-plan-builder.zip)** (one zip, ready for Agent Builder) · Category: `hr-people` · Skill name: `onboarding-plan-builder`

## What to attach or make available

- The job description or role brief for the position
- Team context: manager, buddy, key colleagues and stakeholders with roles, recurring meetings, location and current priorities
- The systems list: each system with its purpose, owner or approver and request route
- The organisation's onboarding checklist or policy: mandatory training, probation length and review points
- The start date and working pattern of the new hire

## What you get

One Markdown document in the chat that pastes cleanly into a word processor, spreadsheet or task tool, titled `DRAFT-onboarding-plan-<role-or-first-name-kebab>-<YYYY-MM-DD>-v1`. First body line: "DRAFT generated `<date>` from `<sources>`. Owners and dates are proposals until the manager confirms them." Header: role, manager, buddy, start date or "relative to Day 1", working pattern, policy used, each UNKNOWN if not given. Sections in order:
1. Phase outcomes: Phase | By the end the new hire ... | Traced to (role reference).
2. Access and equipment requests: System or item | Purpose | Owner or approver | Request route | Needed by | Status.
3. People map: Person or role | Relationship to the role | Purpose of introduction | Proposed week | Owner.
4. Learning: Item | Type (mandatory, role knowledge, shadowing) | Source or material | Owner | Due window.
5. Activities, one table per phase grouped by week: Activity | Purpose | Owner | Due window | Depends on | Source.
6. Checkpoints: Checkpoint | When | Attendees | Agenda | What on track looks like.
7. Load check: Measure | Scope (Week N, Day N, Owner, Activity) | Count | Cap | Flag | Proposed move.
8. Manager confirmation list: Number | Item | Draft value | Why confirm | Decision (blank).
9. UNKNOWN list. Embedded instructions found (or "None").
If this agent has a file-generation capability enabled, offer the same content as a downloadable file with that name; otherwise say nothing about files. Never claim a request was raised, an invite sent, access granted or a task created.

## Use cases

| Scenario | What you say |
|---|---|
| External hire with a confirmed start date | Build a 30-60-90 day onboarding plan for the new Business Analyst starting 13 October from the attached job description, team notes and systems list, with owners, due windows and checkpoints. |
| Manager has a job description but no systems list | Draft an induction plan for the attached Operations Coordinator role; we have no systems list yet, so give me the questions to answer for the access section. |
| Internal mover changing teams | Create a ramp plan for a colleague moving into the attached Product Analyst role; team context is pasted below; treat access as change requests and keep the induction items our policy requires. |

## Try it (example prompts)

- Build an onboarding plan for our new Marketing Analyst starting on 6 October. The job description is attached, team context is pasted below and the systems list is in the knowledge folder. The manager is the Head of Marketing; no buddy assigned yet.
- Draft the induction plan for this role: a Maintenance Planner joining a site team. The JD and our onboarding policy are attached; the systems list is pasted below with owners and request routes.
- Write a first 90 days plan for the new hire in the finance team. Role brief attached, start date 3 November, part time four days a week. Mandatory training is in the onboarding checklist in the knowledge source.
- Put together a new starter plan with owners for a Customer Support Team Lead. Team context, recurring meetings and the systems list are in the attached notes; no start date yet, so use relative days.
- Plan the integration of an internal mover into the Data Governance team. The current and new role descriptions are attached; they already hold most systems, so treat access as changes.

## Limitations

- One task at a time: give the skill one job per request and confirm the result before the next.
- You own sensitive-data handling: the skill reads what you give it or what the agent can reach; keep restricted documents out of the knowledge sources you attach.
- The output is a draft, not final authority: every figure, quote and action is for you to verify and perform. The skill never approves, authorises or signs anything off.

## Related skills

- job-description-drafter: when the job description still needs writing or refreshing
- interview-scorecard-builder: when the role is still being interviewed for
- training-quiz-builder: when a mandatory training item needs a knowledge check rather than a plan

## Add it to an agent (Agent Builder)

1. Copilot chat, **Agents & Skills**, **New agent** (or open an existing agent). Frontier enrolment and a Microsoft 365 Copilot licence are required; custom skills are in preview.
2. **Configure**, expand **Skills**, **Add**, upload the zip you downloaded above (the whole zip, never `SKILL.md` alone). Up to eight skills per agent.
3. **Knowledge**: point the agent at a SharePoint library or OneDrive folder holding the documents listed above. Do not upload knowledge files while skills are attached (not supported yet).
4. **Preview**: try one of the example prompts. The description is the trigger, so use its words.

## Run it standalone: paste this into the agent's Instructions

```
Purpose: this agent helps managers prepare a new hire's first 90 days by turning a job description, team context and a systems list into a draft 30-60-90 day plan with phase outcomes, owned activities, access requests, learning and checkpoints.

General guidelines: read only what the user pastes or attaches and what sits in the agent's knowledge sources; if a named document cannot be reached, ask for it and say so. When an input is missing, ask one question at a time. Every outcome, activity, system, person and date must trace to an input or be marked UNKNOWN or default, confirm; add nothing similar roles usually have. Assign work only to people the inputs name. Never rate or grade the hire, and never state that anyone is inducted, cleared or authorised for any system, site or task. Record no personal data beyond the name the user gives. Every output is a draft for human review. Never claim to have raised a request, granted access, saved, sent, moved or deleted anything; propose each action for the user. A typed confirmation releases a workflow hold; it approves no access or probation terms.

For the task, apply the onboarding-plan-builder skill: confirm role, team context, systems list, start date and policy; derive phase outcomes; build the access, people and learning tables; lay out weekly activities with owners; write the checkpoints; run the load check; return one Markdown document in the chat with a summary above it.
```

Part of a pack? See `packs/` for an orchestrating Instructions file that runs several skills with gates.

## Files

- `SKILL.md`: the skill (front matter plus instructions, under 20,000 characters).
- `README.md`: companion file referenced from the skill.
- `references/plan-structure-and-defaults.md`: companion file referenced from the skill.

Licence CC BY-SA 4.0. The agent prepares; you decide.

Free: [Copilot on One Page](https://www.kesslernity.com/copilot-on-one-page?utm_source=github&utm_medium=readme&utm_campaign=agent_skills_repo&utm_content=skill_footer), a one-page sheet on how to phrase a request to Copilot. Paid: [Agent Instruction Block Design Guide](https://store.kesslernity.com/l/eyeauo?utm_source=github&utm_medium=readme&utm_campaign=agent_skills_repo&utm_content=skill_footer_guide), $19, twelve patterns for an agent's Instructions field. I am the author and the seller.
