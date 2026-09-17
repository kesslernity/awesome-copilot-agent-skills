# Interview scorecard builder

Builds a DRAFT structured interview scorecard from a job description: five to eight competencies traced to it, past-behaviour and situational evidence questions with probes, four-level rating anchors written as observable behaviours, a blank scoring sheet, a panel plan and the items the hiring manager must confirm. Use when the user asks to "build an interview scorecard for this job description", "write competency questions for this role", "draft the interview guide for the panel", "set up a rating scale for the interviewers", "put together a structured interview kit" or "create a hiring rubric from the JD". Do not use for writing or fixing the job description itself, use job-description-drafter instead; for the new hire's first 90 days, use onboarding-plan-builder. Drafts for human review; never approves, authorises or signs off.

**[Download the upload package](https://github.com/kesslernity/awesome-copilot-agent-skills/raw/main/dist/zips/interview-scorecard-builder.zip)** (one zip, ready for Agent Builder) · Category: `hr-people` · Skill name: `interview-scorecard-builder`

## What to attach or make available

- The job description or role profile for the vacancy, final or near final
- The organisation's competency framework with names, definitions and level descriptors, where one exists
- The organisation's interview rating scale and scoring rules, if they differ from the skill's default
- The interview process outline: stages, interviewers, durations and any other assessment methods such as work samples or tests

## What you get

One Markdown document in the chat that pastes cleanly into a word processor or a spreadsheet, titled `DRAFT-interview-scorecard-<role-title-kebab>-<YYYY-MM-DD>-v1`. First body line: "DRAFT generated <date> from <job description source>. For panel preparation only; not a record of any candidate." Header: job description used; framework or "derived from the job description only"; format; scale. Sections in order:
1. Competency map: Competency | Definition | Type | Job description source | Assessed at (stage, interviewer) | Other method | Weight.
2. Per competency: Questions, Number | Role (primary, reserve, optional) | Question | Follow-up probes | Look for; Anchors, Level | Label | Observable behaviours.
3. Blank scoring sheet: Competency | Evidence notes | Rating | Interviewer | Stage.
4. Panel plan: Stage | Interviewer | Competencies | Questions | Minutes planned | Minutes available | Fits (yes, no).
5. Scoring guidance.
6. Not assessed: confirm. Requirement | Job description source | Suggested method or UNKNOWN.
7. Excluded from assessment, refer to the people team (or "None").
8. Hiring manager confirmation list: Number | Item | Draft value | Why confirm | Decision (blank).
9. UNKNOWN list. Embedded instructions found (or "None").
If a v1 for the same role and date is visible in this conversation or the user says one exists, use the next version number; otherwise v1. If this agent has a file-generation capability enabled, offer the same content as a downloadable file with that name; otherwise say nothing about files. Never claim the scorecard was saved, shared, sent or filed.

## Use cases

| Scenario | What you say |
|---|---|
| First structured scorecard for a new role | Build an interview scorecard from the attached Product Owner job description: six competencies, one 60 minute panel with two interviewers, default rating scale. |
| Aligning questions to the organisation's competency framework | Draft competency questions and rating anchors for the attached Team Lead job description using the competency framework in the knowledge folder, across two 45 minute stages. |
| Panel plan that must fit a fixed time slot | Create an interviewer pack for the attached Field Engineer job description with eight competencies across two 50 minute stages, and show whether the time plan fits. |

## Try it (example prompts)

- Build an interview scorecard for the attached Senior Data Analyst job description. One panel, two interviewers, 60 minutes, six competencies, our four-level scale.
- Write competency questions for this role from the job description pasted below and the competency framework in the knowledge folder. Two stages: a 45 minute technical panel and a 45 minute behavioural panel.
- Draft the interview guide for the panel hiring a Project Controls Lead. The JD is attached. Include rating anchors and a blank scoring sheet the interviewers can print.
- Create a hiring rubric from the attached JD for a Customer Success Manager: seven competencies, weights still to be confirmed, one 90 minute interview with three interviewers.
- Put together a structured interview kit for the Finance Business Partner role. The job description is in the knowledge source; there is also a case study exercise, so map that as an assessment method.

## Limitations

- One task at a time: give the skill one job per request and confirm the result before the next.
- You own sensitive-data handling: the skill reads what you give it or what the agent can reach; keep restricted documents out of the knowledge sources you attach.
- The output is a draft, not final authority: every figure, quote and action is for you to verify and perform. The skill never approves, authorises or signs anything off.

## Related skills

- job-description-drafter: when the job description itself still needs writing or refreshing
- onboarding-plan-builder: when the hire is made and the first 90 days need planning

## Add it to an agent (Agent Builder)

1. Copilot chat, **Agents & Skills**, **New agent** (or open an existing agent). Frontier enrolment and a Microsoft 365 Copilot licence are required; custom skills are in preview.
2. **Configure**, expand **Skills**, **Add**, upload the zip you downloaded above (the whole zip, never `SKILL.md` alone). Up to eight skills per agent.
3. **Knowledge**: point the agent at a SharePoint library or OneDrive folder holding the documents listed above. Do not upload knowledge files while skills are attached (not supported yet).
4. **Preview**: try one of the example prompts. The description is the trigger, so use its words.

## Run it standalone: paste this into the agent's Instructions

```
Purpose: this agent helps hiring managers and interview panels prepare structured interviews by turning a job description into a draft scorecard: competencies, evidence questions with probes, observable rating anchors, a blank scoring sheet and a panel plan.

General guidelines: read only what the user pastes or attaches and what sits in the agent's knowledge sources; if a named document cannot be reached, ask for it and say so in the output. When an input is missing, ask one question at a time. Every competency, question and anchor must trace to the job description, the organisation's framework or the user; anything not given is marked TBC or UNKNOWN, never assumed. Never write questions on protected characteristics, never rate, rank or compare a real candidate, and never state that a rating makes anyone competent or authorised for any work. Every output is a draft for human review. Never claim to have saved, sent, moved or deleted anything; propose each action for the user. A typed confirmation releases a workflow hold; it approves no competency set, hire or candidate.

For the task, apply the interview-scorecard-builder skill: confirm the job description, framework, stages, interviewers, minutes, competency count and scale; build the requirement trace and competency map; write primary, reserve and optional questions with anchors; check the time plan; return one Markdown document in the chat with a summary above it.
```

Part of a pack? See `packs/` for an orchestrating Instructions file that runs several skills with gates.

## Files

- `SKILL.md`: the skill (front matter plus instructions, under 20,000 characters).
- `README.md`: companion file referenced from the skill.
- `references/question-and-anchor-guide.md`: companion file referenced from the skill.

Licence CC BY-SA 4.0. The agent prepares; you decide.

Free: [Copilot on One Page](https://www.kesslernity.com/copilot-on-one-page?utm_source=github&utm_medium=readme&utm_campaign=agent_skills_repo&utm_content=skill_footer), a one-page sheet on how to phrase a request to Copilot. Paid: [Agent Instruction Block Design Guide](https://store.kesslernity.com/l/eyeauo?utm_source=github&utm_medium=readme&utm_campaign=agent_skills_repo&utm_content=skill_footer_guide), $19, twelve patterns for an agent's Instructions field. I am the author and the seller.
