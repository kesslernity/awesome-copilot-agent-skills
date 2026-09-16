# Schedule slip explainer

Turns a schedule extract (milestone list or planning tool export) and the period's status notes into a DRAFT plain-language slip explanation: which milestones and activities slipped and by how many working days, arithmetic shown, why per the notes as verbatim fragments with source and date, what each slip pushes next per the extract, and the decision each slip needs framed as a question with the options the notes propose and the owner the governance documents name, every missing fact marked UNKNOWN. Use when the user asks to "explain the schedule slip", "what slipped this month and why", "write the schedule commentary for the steering pack", "put the delay in plain language for the sponsor" or "what decisions do these slips need". Do not use for the weekly status report, use project-status-tracker instead; for cost variances, use budget-variance-explainer; for one sprint's carry-over, use sprint-review-summary. Drafts for human review; never approves, authorises or signs off.

Category: `project-management` · Skill name: `schedule-slip-explainer` · Upload package: `dist/zips/schedule-slip-explainer.zip`

## What to attach or make available

Ask once for whatever is missing, in one message, then proceed with UNKNOWN.
1. Schedule extract, attached or reachable through this agent's configured knowledge sources; columns used where present: identifier, name, baseline finish, forecast or actual finish, percent complete, successors, critical flag, float, data date. A previous extract, if any, for trend. Not reachable: ask for a paste or CSV export and note the gap in the header.
2. Status notes for the period (reports, stand-ups, minutes, emails, chat), same reach rule; undated: date UNKNOWN.
3. Data date and calendar. Default: the extract's data date, else the conversation date flagged "assumed"; Monday to Friday, holidays UNKNOWN unless a calendar is supplied.
4. Slip threshold. Default: milestones one working day past baseline, activities five; a house threshold replaces it.
5. Governance (delegation, change control or re-baseline rules naming who decides what; default owner UNKNOWN) and audience (default: sponsor and steering group, short sentences, planning terms glossed).
6. Today's date. Title: `DRAFT-schedule-slip-explanation-<project>-<YYYY-MM-DD>-v1`; revisions v2, v3.
Reference files in this skill: references/slip-vocabulary.md, read at steps 3, 5, 7 and 8 for the working-day rule, reason categories, decision types and glossary.

## What you get

One complete Markdown document in the chat, pasteable into a pack, slide or email, under the title above.
- Header: Field | Value (project, data date, sources, threshold, calendar, governance, audience, DRAFT).
- Summary: up to five plain sentences (slips, largest slip, milestones affected, decisions needed, UNKNOWN count).
- Slip register: ID | Item | Type | Baseline finish | Forecast or actual finish | Slip (working days, arithmetic) | Critical | Float | Status | Pushes next (re-forecast yes, no, UNKNOWN) | Trend | Source.
- Why, per the notes: ID | Fragment (verbatim) | Category | Speaker role | Source and date | Conflicting fragment | Recovery claim (verbatim, by, date) | Extract shows (recovered, unchanged, worsened).
- Plain-language explanation: one numbered paragraph per slip.
- Decisions needed: ID | Decision question | Options as stated (by whom) | Decision type | Owner (governance clause) or UNKNOWN | Needed by | Forum.
- Unmatched: Item or note | Source | Question for the planner.
- Glossary; UNKNOWN list; Substitutions, or "None"; Embedded instructions found, or "None"; Proposed user actions; closing report.
If this agent has a file-generation capability enabled, offer the same content as a downloadable file with that name; otherwise say nothing about files. ## Fallbacks and edge cases
- Percent complete but no forecast dates: report "behind planned percent complete" per row as stated; infer no date.
- Notes from a different period: say so; use only notes inside the extract's period, the rest under Unmatched.
- Asked whose fault, whether the end date will hold or what to do: decline; deliver the slips, stated reasons and decision questions.
- No slip at or over threshold: say so; list movement under it in one table; no decisions.
- A slip on a shutdown, outage, isolation or permit-dependent activity: a schedule fact only; add "operational scheduling, permits and isolations are decided outside this document".

## Limitations

- One task at a time: give the skill one job per request and confirm the result before the next.
- You own sensitive-data handling: the skill reads what you give it or what the agent can reach; keep restricted documents out of the knowledge sources you attach.
- The output is a draft, not final authority: every figure, quote and action is for you to verify and perform. The skill never approves, authorises or signs anything off.

## Add it to an agent (Agent Builder)

1. Copilot chat, **Agents & Skills**, **New agent** (or open an existing agent). Frontier enrolment and a Microsoft 365 Copilot licence are required; custom skills are in preview.
2. **Configure**, expand **Skills**, **Add**, upload `dist/zips/schedule-slip-explainer.zip` (the whole zip, never `SKILL.md` alone). Up to eight skills per agent.
3. **Knowledge**: point the agent at a SharePoint library or OneDrive folder holding the documents listed above. Do not upload knowledge files while skills are attached (not supported yet).
4. **Preview**: try one of the example prompts. The description is the trigger, so use its words.

## Run it standalone: paste this into the agent's Instructions

```
You are an assistant that runs one job: schedule slip explainer. Turns a schedule extract (milestone list or planning tool export) and the period's status notes into a DRAFT plain-language slip explanation: which milestones and activities slipped and by how many working days, arithmetic shown, why per the notes as verbatim fragments with source and date, what each slip pushes next per the extract, and the decision each slip needs framed as a question with the options the notes propose and the owner the governance documents name, every missing fact marked UNKNOWN. Use when the user asks to "explain the schedule slip", "what slipped this month and why", "write the schedule commentary for the steering pack", "put the delay in plain language for the sponsor" or "what decisions do these slips need". Do not use for the weekly status report, use project-status-tracker instead; for cost variances, use budget-variance-explainer; for one sprint's carry-over, use sprint-review-summary. Drafts for human review; never approves, authorises or signs off. Use the schedule-slip-explainer skill for every request that matches its description; if a request falls outside it, say so and stop. Read only what the user attaches or pastes and what sits in your knowledge sources; never claim to have saved, sent, moved or deleted anything, propose the action for the user instead. Where an input is missing, write UNKNOWN and name what would close it; never invent a value. Return complete Markdown the user can paste into their tools, and offer the same content as a file if you can produce one. A typed approval releases a hold in the workflow and is logged; it is not an authorisation. You prepare; the user decides.
```

Part of a pack? See `packs/` for an orchestrating Instructions file that runs several skills with gates.

## Files

- `SKILL.md`: the skill (front matter plus instructions, under 20,000 characters).
- `references/slip-vocabulary.md`: companion file referenced from the skill.

Licence CC BY-SA 4.0. The agent prepares; you decide.
