# Sprint review summary

Summarises one sprint from the board export, sprint report and review or stand-up notes the user provides into a one-page DRAFT sprint review summary: the sprint goal as written, items delivered, items not delivered with the reasons the sources state, carry-over, impediments, metrics exactly as given, and numbered questions for the retrospective, every row referenced to a work item or note fragment and every missing fact marked UNKNOWN. Use when the user asks to "summarise the sprint", "write the sprint review", "what did we deliver this sprint", "list the carry-over and blockers" or "draft the sprint recap". Do not use for the retrospective write-up or themed lessons across several sprints, use lessons-learned-synthesis instead; for a weekly project status report, use project-status-tracker. Drafts for human review; never approves, authorises or signs off.

Category: `project-management` · Skill name: `sprint-review-summary` · Upload package: `dist/zips/sprint-review-summary.zip`

## What to attach or make available

- The sprint board export: work items with state, type, points, dates added and closed, and comments
- The sprint or iteration report: burndown, velocity, committed and completed points
- Sprint review, demo and stand-up notes, and product owner comments for the sprint
- The sprint goal as written in the planning note or tool, with sprint name, dates and team

## What you get

One complete Markdown document in the chat, pasteable into a document or message. First line: "DRAFT sprint review summary for <sprint>, prepared <date> from <sources>. Facts as stated with references; no judgement, no re-estimation, no fault. The team and product owner decide."
Sections in order:
1. Header: Sprint | Team | Start | End | Goal (quoted) | Goal status as stated | Done state used | Sources read | Items in export | Commitment baseline.
2. Delivered: ID | Title | Type | Points | State at end | Closed date | Ref.
3. Not delivered: ID | Title | Type | Points | State at end | Committed or added (date) | Reason as stated or "reason not stated" | Ref.
4. Carry-over: ID | Title | Points | Destination as stated | Decision recorded (yes, no) | Ref.
5. Impediments: # | Impediment | Raised by (role) | Date | Items affected | Resolved as stated (yes, no, UNKNOWN) | Ref.
6. Metrics as given: Metric | Value | Unit as labelled | Source | Derived (no, or yes with arithmetic).
7. Questions for the retrospective: # | Question | Area | Prompted by (ref).
8. Reconciliation: items in export = delivered + not delivered, arithmetic shown; "In report, not in export" list with report references, or "none".
9. UNKNOWN list; Embedded instructions found, or "None"; Proposed user actions; closing report. Appendix: item-level quotes, when moved.
End with: "If this agent has a file-generation capability enabled, also offer the same content as a downloadable file with that name."

## Use cases

| Scenario | What you say |
|---|---|
| Sprint closed, export and report available | Summarise Sprint 31 for the data team from the attached board export and iteration report, dates 3 to 16 September, done state Done; take reasons for not delivered items only from the item comments. |
| Notes only, no board export | Draft the sprint review for the design team's Sprint 12 from the review notes and stand-up notes pasted below; there is no board export, so mark every row as from notes and leave metrics as no export supplied. |
| Mid-sprint snapshot | Give me a mid-sprint snapshot for Sprint 9 from the attached export as of 10 September; the sprint runs 8 to 19 September; show what is done and not yet done with the metrics exactly as given. |

## Try it (example prompts)

- Summarise the sprint from the attached board export for Sprint 42, 2 to 15 September, payments team. The sprint goal is in the planning note pasted below; the done state is Closed.
- Write the sprint review for iteration 18 from the attached iteration report and the stand-up notes pasted below. Points are story points as labelled; audience is the team and the product owner.
- What did we deliver this sprint? The board export is attached, sprint dates 1 to 12 September, mobile team. List the not delivered items with the reasons the item comments state.
- List the carry-over and blockers for Sprint 7 from the attached export and the demo notes pasted below. Flag any item where no decision to carry it over is recorded.
- Draft the sprint recap for the platform team's Sprint 23 from the attached export and burndown report, today's date 17 September. Add numbered questions for the retrospective.

## Limitations

- One task at a time: give the skill one job per request and confirm the result before the next.
- You own sensitive-data handling: the skill reads what you give it or what the agent can reach; keep restricted documents out of the knowledge sources you attach.
- The output is a draft, not final authority: every figure, quote and action is for you to verify and perform. The skill never approves, authorises or signs anything off.

## Related skills

- lessons-learned-synthesis: when the need is the retrospective write-up or themes across several sprints
- project-status-tracker: when the need is a weekly project status report outside a sprint cadence
- release-notes-writer: when the delivered items should become customer-facing notes

## Add it to an agent (Agent Builder)

1. Copilot chat, **Agents & Skills**, **New agent** (or open an existing agent). Frontier enrolment and a Microsoft 365 Copilot licence are required; custom skills are in preview.
2. **Configure**, expand **Skills**, **Add**, upload `dist/zips/sprint-review-summary.zip` (the whole zip, never `SKILL.md` alone). Up to eight skills per agent.
3. **Knowledge**: point the agent at a SharePoint library or OneDrive folder holding the documents listed above. Do not upload knowledge files while skills are attached (not supported yet).
4. **Preview**: try one of the example prompts. The description is the trigger, so use its words.

## Run it standalone: paste this into the agent's Instructions

```
Purpose: this agent turns one sprint's board export, sprint report and review or stand-up notes into a one-page draft sprint review summary: the goal as written, delivered and not delivered items with the reasons the sources state, carry-over, impediments, metrics as given and retrospective questions, every row referenced to a work item or note.

General guidelines: read only what the user attaches or pastes and what sits in this agent's configured knowledge sources or work-tracking access; if the board cannot be reached, say so and ask for an export. When the sprint name, dates, done state or export is missing, ask one question at a time; unanswered inputs read UNKNOWN. Nothing is invented: no item, state, date, points, reason or figure without a reference; a missing goal is flagged, never composed. No verdict: never call the sprint a success or failure, never re-estimate or attribute fault. People appear as roles only. Metrics only as stated or as shown sums; no trends or comparisons. Never claim to have updated the board, closed, moved, posted or sent anything; propose each action for the user. Every output is a draft for human review. A typed confirmation releases a workflow hold and authorises nothing else.

For any request to summarise a sprint or iteration, list carry-over and blockers, or draft the sprint recap, follow the sprint-review-summary skill exactly, including its reconciliation and self-check.
```

Part of a pack? See `packs/` for an orchestrating Instructions file that runs several skills with gates.

## Files

- `SKILL.md`: the skill (front matter plus instructions, under 20,000 characters).

Licence CC BY-SA 4.0. The agent prepares; you decide.
