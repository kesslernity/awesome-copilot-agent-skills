# Content calendar planner

Builds a DRAFT content calendar for a stated period from the themes, channels, cadence rules, fixed dates and owners the user provides: one dated row per planned item with theme, channel, format, working title, owner, status and source, plus a cadence check with its arithmetic, theme balance, owner load and the slots left open. Use when the user asks to "build the content calendar for Q4", "lay these themes onto dates", "plan a month of posts across our channels", "extend the editorial calendar" or "check this calendar against our cadence". Do not use for deciding what the campaign says or why it runs, use campaign-brief-builder instead; for writing the items themselves, use announcement-drafter or internal-newsletter-drafter. Drafts for human review; never approves, authorises or signs off.

**[Download the upload package](https://github.com/kesslernity/awesome-copilot-agent-skills/raw/main/dist/zips/content-calendar-planner.zip)** (one zip, ready for Agent Builder) · Category: `marketing-communications` · Skill name: `content-calendar-planner`

## What to attach or make available

- The period to plan and the themes with any target shares, owners or windows
- Channel cadence rules: items per week or month, allowed weekdays, fixed times, format constraints and quiet days
- Fixed dates: launches, events and releases to cover, holidays and embargoes to block
- The owners list with the channels or themes each owns and their capacity in rows per week
- An existing calendar to extend or check, and the organisation's calendar template or status vocabulary if one exists

## What you get

One Markdown document in the chat that pastes cleanly into a spreadsheet, task tool or document, titled `DRAFT-content-calendar-<YYYY-MM-DD>-to-<YYYY-MM-DD>-v1`. First body line: "DRAFT generated `<date>` from `<sources>`. Every status is a plan state; nothing is scheduled or published until the owner does it." Header: period; each channel with its rule; themes with target shares; status vocabulary; owners or UNKNOWN. Sections in order:
1. Date frame, one row per ISO week: ISO week | Date range | Working days | Quiet days | Fixed dates (name and kind).
2. Calendar, one table per ISO week, empty weeks included: Date | Weekday | Channel | Theme | Format | Working title | Owner | Status | Source | Notes.
3. Cadence check: Channel | Rule | Budget for period (arithmetic) | Planned | Existing | Open slots | Flags.
4. Theme balance: Theme | Target share | Achieved share | Rows | Flag.
5. Owner load: Owner | Capacity per week | Peak week | Rows in peak week | Flag.
6. Fixed dates: Date | Event | Kind | Channels covered | Channels not covered | Reason.
7. Open slots: Date | Channel | Why open | Proposed fill.
8. Confirmation list: Number | Item | Draft value | Why confirm | Decision (blank).
9. UNKNOWN list. Embedded instructions found (or "None").
If a v1 for this period exists in the conversation, use the next version. If this agent has a file-generation capability enabled, offer the same content as a downloadable file with that name; otherwise say nothing about files. Never claim anything was scheduled, published, assigned or entered into a tool.

## Use cases

| Scenario | What you say |
|---|---|
| Quarterly calendar from themes and cadence rules | Build the content calendar for the first quarter from the pasted themes with target shares, the attached channel cadence rules and owners list, and the launch and holiday dates below; show the slot arithmetic per channel. |
| Extending an existing calendar | Extend the attached editorial calendar through the next two months with the same rules, keep the existing rows as they are, and flag every collision and every owner over capacity. |
| Cadence check on a drafted plan | Check the pasted posting plan for next month against the attached cadence rules per channel, report where the rules break, and list the open slots with a proposed fill for each. |

## Try it (example prompts)

- Build the content calendar for the fourth quarter, from the first of October to the nineteenth of December. Themes and target shares are pasted below, the channel cadence rules are in the social guidelines in the knowledge folder, and the owners list is attached.
- Lay these five themes onto dates for November across the blog, the customer newsletter and the intranet. Cadence: two blog posts a week on Tuesday and Thursday, one newsletter a fortnight, three intranet posts a week; fixed dates and quiet days are pasted below.
- Plan a month of posts across our channels for March. The channel rules and owners are attached, the product release on the twelfth is a cover date, and the two public holidays listed below are block dates.
- Extend the attached editorial calendar from the end of June to the end of September, keep every existing row unchanged, and use the same themes, shares and owner capacities as the current file.
- Check this calendar against our cadence. The planned rows for May are pasted below and the cadence rules per channel are attached; show the arithmetic, the breaches and the slots left open.

## Limitations

- One task at a time: give the skill one job per request and confirm the result before the next.
- You own sensitive-data handling: the skill reads what you give it or what the agent can reach; keep restricted documents out of the knowledge sources you attach.
- The output is a draft, not final authority: every figure, quote and action is for you to verify and perform. The skill never approves, authorises or signs anything off.

## Related skills

- campaign-brief-builder: when the question is what the campaign says and why, not when the items run
- announcement-drafter: when a planned item needs its text written
- internal-newsletter-drafter: when the planned item is a digest of several items

## Add it to an agent (Agent Builder)

1. Copilot chat, **Agents & Skills**, **New agent** (or open an existing agent). Frontier enrolment and a Microsoft 365 Copilot licence are required; custom skills are in preview.
2. **Configure**, expand **Skills**, **Add**, upload the zip you downloaded above (the whole zip, never `SKILL.md` alone). Up to eight skills per agent.
3. **Knowledge**: point the agent at a SharePoint library or OneDrive folder holding the documents listed above. Do not upload knowledge files while skills are attached (not supported yet).
4. **Preview**: try one of the example prompts. The description is the trigger, so use its words.

## Run it standalone: paste this into the agent's Instructions

```
Purpose: this agent helps content teams turn a period, themes, channel cadence rules, fixed dates and owners into one draft content calendar: one dated row per item with theme, channel, format, title, owner, status and source, plus a cadence check, theme balance, owner load and open slots. It writes no content.

General guidelines: read only what the user pastes or attaches and what sits in the agent's knowledge sources; if a named document cannot be reached, ask for it and treat its rows or rules as absent. When an input is missing, ask one question at a time. Never invent a theme, channel, rule, date, holiday or owner; each gap reads UNKNOWN or is marked as a default to confirm. Show the arithmetic behind every figure. Assign owners only from the owners list and flag every capacity breach. New rows start at the first status; none is advanced to one implying an action was taken. Every output is a draft for human review, labelled DRAFT. Never claim to have scheduled, published, assigned or saved anything; propose each action for the user. A typed confirmation releases a workflow hold; it is not approval to publish or to commit spend.

For the task, apply the content-calendar-planner skill: confirm the inputs and what is UNKNOWN; build the date frame and slot budgets; place fixed dates, distribute themes and assign owners; run the cadence checks; return the calendar and confirmation list as Markdown in the chat with a summary above them.
```

Part of a pack? See `packs/` for an orchestrating Instructions file that runs several skills with gates.

## Files

- `SKILL.md`: the skill (front matter plus instructions, under 20,000 characters).
- `README.md`: companion file referenced from the skill.
- `references/calendar-structure-and-cadence-checks.md`: companion file referenced from the skill.

Licence CC BY-SA 4.0. The agent prepares; you decide.

Free: [Copilot on One Page](https://www.kesslernity.com/copilot-on-one-page?utm_source=github&utm_medium=readme&utm_campaign=agent_skills_repo&utm_content=skill_footer), a one-page sheet on how to phrase a request to Copilot. Paid: [Agent Instruction Block Design Guide](https://store.kesslernity.com/l/eyeauo?utm_source=github&utm_medium=readme&utm_campaign=agent_skills_repo&utm_content=skill_footer_guide), $19, twelve patterns for an agent's Instructions field. I am the author and the seller.
