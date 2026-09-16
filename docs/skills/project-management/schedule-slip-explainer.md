# Schedule slip explainer

Turns a schedule extract (milestone list or planning tool export) and the period's status notes into a DRAFT plain-language slip explanation: which milestones and activities slipped and by how many working days, arithmetic shown, why per the notes as verbatim fragments with source and date, what each slip pushes next per the extract, and the decision each slip needs framed as a question with the options the notes propose and the owner the governance documents name, every missing fact marked UNKNOWN. Use when the user asks to "explain the schedule slip", "what slipped this month and why", "write the schedule commentary for the steering pack", "put the delay in plain language for the sponsor" or "what decisions do these slips need". Do not use for the weekly status report, use project-status-tracker instead; for cost variances, use budget-variance-explainer; for one sprint's carry-over, use sprint-review-summary. Drafts for human review; never approves, authorises or signs off.

Category: `project-management` · Skill name: `schedule-slip-explainer` · Upload package: `dist/zips/schedule-slip-explainer.zip`

## What to attach or make available

- The schedule extract: milestone list or planning tool export with identifier, name, baseline finish, forecast or actual finish, percent complete, successors, critical flag, float and data date
- Status notes for the period: status reports, stand-up notes, minutes, emails and chat naming the slipped items and what happened
- Governance documents: delegation, change control or re-baseline rules naming who decides each type of schedule decision
- Optional: the previous schedule extract for trend, and the working calendar with holidays

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

## Use cases

| Scenario | What you say |
|---|---|
| Monthly steering pack commentary | Draft the schedule commentary for the October steering pack from the attached milestone export and the four weekly status reports pasted below, with a threshold of one working day for milestones and five for activities. |
| Sponsor asks why a key milestone moved | The go-live milestone in the attached extract moved by three weeks. Explain in plain language what the notes pasted below say happened, what it pushes next per the extract, and what decision the sponsor is being asked to take. |
| Trend against last month's extract | Compare the attached current and previous schedule extracts for the plant upgrade, list which slips are new, grown, shrunk or recovered with both dates, and match each to the reasons in the status notes in the knowledge sources. |

## Try it (example prompts)

- Explain the schedule slip on the plant maintenance preparation project. The milestone export is attached as a CSV with baseline and forecast finish columns and the September status reports are pasted below. Data date 30 September.
- What slipped this month and why? The current and previous planning tool exports are attached, the stand-up notes are pasted below, and the working week is Sunday to Thursday.
- Write the schedule commentary for the steering pack from the attached milestone list and the minutes of the two progress meetings pasted below; the audience is the sponsor, so gloss planning terms.
- Put the delay in plain language for the sponsor: the attached extract shows milestone M4 moving from 12 June to 26 June and the notes explaining it are pasted below. Show the working-day arithmetic.
- What decisions do these slips need? Use the attached schedule extract, the status notes in the knowledge sources and the change control rules attached as a document to name who decides each.

## Limitations

- One task at a time: give the skill one job per request and confirm the result before the next.
- You own sensitive-data handling: the skill reads what you give it or what the agent can reach; keep restricted documents out of the knowledge sources you attach.
- The output is a draft, not final authority: every figure, quote and action is for you to verify and perform. The skill never approves, authorises or signs anything off.

## Related skills

- project-status-tracker: when the weekly status report itself is wanted
- budget-variance-explainer: when the variance is cost, not time
- sprint-review-summary: when one sprint's carry-over is the subject

## Add it to an agent (Agent Builder)

1. Copilot chat, **Agents & Skills**, **New agent** (or open an existing agent). Frontier enrolment and a Microsoft 365 Copilot licence are required; custom skills are in preview.
2. **Configure**, expand **Skills**, **Add**, upload `dist/zips/schedule-slip-explainer.zip` (the whole zip, never `SKILL.md` alone). Up to eight skills per agent.
3. **Knowledge**: point the agent at a SharePoint library or OneDrive folder holding the documents listed above. Do not upload knowledge files while skills are attached (not supported yet).
4. **Preview**: try one of the example prompts. The description is the trigger, so use its words.

## Run it standalone: paste this into the agent's Instructions

```
Purpose: this agent helps planners and project managers explain schedule movement to sponsors: what slipped and by how many working days, what the status notes say happened, what it pushes next, and what decision it needs and from whom. General guidelines: read only the schedule extract, notes and governance documents the user attaches or pastes, and what sits in the knowledge sources configured on this agent; never fill a gap from memory. When a required input is missing, such as the data date, ask one question at a time and wait for the answer. Assume no capability beyond chat; if file generation is not available, return it in the chat and say so. Never claim to have updated the schedule or sent anything; every action is proposed for the user to perform. Every slip shows its arithmetic and source; every reason is a verbatim fragment with source and date, or reason not stated in notes; anything the sources omit reads UNKNOWN. Never re-plan, invent a cause, assign blame, judge whether a date will hold or pick a decision; decisions are questions with the options the notes propose and the owner governance names. Every output is a draft for human review. A typed confirmation from the user releases a workflow hold; it authorises nothing. For the task: when the user asks to explain schedule slips, draft schedule commentary or list the decisions they require, follow the schedule-slip-explainer skill exactly and return one complete Markdown document marked DRAFT.
```

Part of a pack? See `packs/` for an orchestrating Instructions file that runs several skills with gates.

## Files

- `SKILL.md`: the skill (front matter plus instructions, under 20,000 characters).
- `references/slip-vocabulary.md`: companion file referenced from the skill.

Licence CC BY-SA 4.0. The agent prepares; you decide.
