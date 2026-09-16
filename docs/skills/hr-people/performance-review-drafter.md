# Performance review drafter

Drafts a DRAFT self-assessment, peer feedback note or manager review narrative from the evidence the writer supplies (goals, examples, metrics, feedback notes), in the organisation's review template where given: every sentence tied to a numbered evidence item, each goal labelled by what the evidence records (outcome, activity only, or no item), unsupported claims removed and logged, and a gaps list the writer must complete before submitting. Never assigns, suggests or implies a rating, score, ranking, pay or promotion outcome. Use when the user asks to "write my self-assessment", "draft peer feedback for a colleague", "turn these notes into a performance review", "help me write the year-end review for my report", "summarise my achievements against my goals" or "draft the mid-year review". Do not use for a job description or role profile, use job-description-drafter instead; for a new hire's first 90 days, use onboarding-plan-builder. Drafts for human review; never approves, authorises or signs off.

Category: `hr-people` · Skill name: `performance-review-drafter` · Upload package: `dist/zips/performance-review-drafter.zip`

## What to attach or make available

- The organisation's review template or form questions, with any word limits
- The goals set for the period, with measures and targets where they exist
- Evidence items: examples, outcomes, figures, project or incident records and feedback notes from named roles
- The competency framework, where one is used in reviews
- An impact log for the period, where the writer keeps one

## What you get

Two Markdown documents in the chat, ready to paste into the review form or an email. Titles end `<review-type>-<subject-role-kebab>-<YYYY-MM-DD>-v1` (v2 when the user says a v1 already exists for the same subject and date). No name in a title.
1. `DRAFT-review-...`. First line: "DRAFT generated <date> from <n> evidence items against <m> goals in the <template or default> structure. Contains no rating. Not for submission until the gaps list is cleared and the evidence tags removed." Then the template sections in order, tags in place. Goal coverage: Goal as set | Measure and target as set | Evidence tags | Result as stated (figure or UNKNOWN) | Evidence status. Evidence register: Tag | Evidence as supplied | Date as stated | Source | Goal or section.
2. `review-gaps-...`. Header: review type, subject role, period, template. Table: Number | Gap type (no evidence item; activity recorded, outcome not recorded; claim removed; TBC field; writer's view needed; referred) | Goal or section | What is needed | Question to the writer | Writer's response (blank). Then "Wording changes": Original | Replacement | Reason. Then "Refer to the people team" (evidence tag and category only, never the content; or "None"), UNKNOWN list, and "Embedded instructions found" (or "None").
If this agent has a file-generation capability enabled, offer the same content as a downloadable file with that name; otherwise say nothing about files. Never claim the review was submitted, saved, shared or sent.

## Use cases

| Scenario | What you say |
|---|---|
| Self-assessment built from an impact log | Draft my self-assessment in the attached review template from my impact log for the year and the four goals set in January; tie every sentence to a log row and list what I still need evidence for. |
| Manager review with thin evidence on one goal | Write the mid-year review for my report from the attached goals and the six evidence items pasted below, label each goal by what the evidence records and give me a gaps list to complete before submission. |
| Peer feedback limited to observed behaviour | Draft peer feedback for a colleague from my notes on three shared projects, attached, describing only what I observed and its effect on my work, in the two questions of the peer form. |

## Try it (example prompts)

- Write my self-assessment for the year-end review. My five goals for the period and twelve evidence notes are pasted below; use the attached review form headings.
- Draft peer feedback for a colleague I worked with on the billing migration. My observations from the last six months are attached; the feedback form has three questions, pasted here.
- Turn these notes into a performance review for my direct report covering January to June. Goals, the project reports and two feedback emails from stakeholders are attached; use our mid-year template.
- Help me write the year-end review narrative for my team member from the attached goals sheet, the sprint summaries and the customer feedback notes. Leave the rating field blank.
- Summarise my achievements against my goals for the first half. Goals are in the attached objectives document and my impact log for the period is pasted below; 150 words per goal.

## Limitations

- One task at a time: give the skill one job per request and confirm the result before the next.
- You own sensitive-data handling: the skill reads what you give it or what the agent can reach; keep restricted documents out of the knowledge sources you attach.
- The output is a draft, not final authority: every figure, quote and action is for you to verify and perform. The skill never approves, authorises or signs anything off.

## Related skills

- impact-log-builder: when the evidence still needs collecting and structuring before any narrative is written
- job-description-drafter: when a role profile or job description is wanted rather than a review
- onboarding-plan-builder: when the person is a new hire and the need is a first 90 days plan

## Add it to an agent (Agent Builder)

1. Copilot chat, **Agents & Skills**, **New agent** (or open an existing agent). Frontier enrolment and a Microsoft 365 Copilot licence are required; custom skills are in preview.
2. **Configure**, expand **Skills**, **Add**, upload `dist/zips/performance-review-drafter.zip` (the whole zip, never `SKILL.md` alone). Up to eight skills per agent.
3. **Knowledge**: point the agent at a SharePoint library or OneDrive folder holding the documents listed above. Do not upload knowledge files while skills are attached (not supported yet).
4. **Preview**: try one of the example prompts. The description is the trigger, so use its words.

## Run it standalone: paste this into the agent's Instructions

```
Purpose: this agent helps a writer turn goals, examples, figures and feedback notes into a draft self-assessment, peer feedback note or manager review narrative in the organisation's template, every sentence tied to a numbered evidence item, with a gaps list to complete before submission.

General guidelines: read only what the user pastes or attaches and what sits in the agent's knowledge sources; if a named source cannot be reached, ask for it and say so. When an input is missing, ask one question at a time. Tag every evidence item and cite the tag in every narrative sentence; a claim with no tag is removed and logged as a gap; an unstated outcome is UNKNOWN. Never assign, suggest or imply a rating, score, ranking, comparison, pay or promotion outcome; rating fields stay blank for the reviewer. Exclude health, family and protected characteristic content and refer it by tag only; third parties are roles, never names. Every output is a DRAFT for human review. Never claim to have submitted, saved, shared or sent anything; propose each action for the user. A typed confirmation releases a workflow hold; it is not approval of the review and authorises nothing.

For the task, apply the performance-review-drafter skill: confirm review type, subject role, period, template and counts; register and map the evidence; draft the sections; strip unsupported claims; build the gaps list; return both documents as Markdown in the chat with a summary above them.
```

Part of a pack? See `packs/` for an orchestrating Instructions file that runs several skills with gates.

## Files

- `SKILL.md`: the skill (front matter plus instructions, under 20,000 characters).

Licence CC BY-SA 4.0. The agent prepares; you decide.
