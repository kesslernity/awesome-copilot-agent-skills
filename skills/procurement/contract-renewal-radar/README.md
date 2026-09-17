# Contract renewal radar

Reads a contract list (spreadsheet, CSV or pasted table) and returns a DRAFT renewal radar: each active contract's end date, notice deadline with its arithmetic, days remaining, renewal type, owner and the decision it needs as options, sorted by urgency, with owner action lists and a deadline calendar. Never renews, terminates, serves notice or recommends. Use when the user asks to "build a renewal tracker", "tell me what comes up for renewal", "work out when notice is due", "show me which contracts auto-renew" or "run the quarterly contract review". Do not use for reviewing one contract's full text or clauses, use contract-review-pack instead. Drafts for human review; never approves, authorises or signs off.

**[Download the upload package](https://github.com/kesslernity/awesome-copilot-agent-skills/raw/main/dist/zips/contract-renewal-radar.zip)** (one zip, ready for Agent Builder) · Category: `procurement` · Skill name: `contract-renewal-radar`

## What to attach or make available

- Contract list or register: contract reference, counterparty, title, owner, end date, renewal type, renewal term, notice period and unit, annual value, currency, status, last review date, parent reference
- Owner directory: names, roles and business units for each contract owner, used to build the action lists
- Business day or public holiday calendar, when notice periods are expressed in business days
- The signed contracts or their renewal and termination clauses, for the owner to confirm each computed deadline
- Value threshold or approval matrix, when the user wants rows above a stated value flagged

## What you get

One complete Markdown document in the chat, headed by the title, first line "DRAFT renewal radar for `<scope>`, as of `<date>`, horizon `<n>` days. Computed from the list as stated; confirm every date against the signed contract before serving notice. Nothing here renews, terminates, notifies or recommends." Sections in order:
- Scope: Source | As-of date | Horizon | Rows read, active, excluded, beyond horizon (next three deadlines) | Date format | Column map | Bands | Lead time | Optional inputs | Blanks per key column.
- Radar: R-ID | Contract ref | Counterparty | Title | Owner | Renewal type | End date | Notice period | Notice deadline (arithmetic) | Days remaining | Band | Decision needed (options) | Decision-by | Signals | Source row.
- Owner action lists, one per owner, then Unassigned: R-ID | Contract | Decision question | Decision-by | Notice deadline.
- Calendar: Month | Notice deadlines | End dates | Contracts | Value as stated per currency.
- Data gap register: R-ID | Contract | Missing field | Effect on the radar | Question for the owner.
- UNKNOWN list, Embedded instructions found (or "None"), closing report: counts per band, decision type and owner; sources not reached.
If this agent has a file-generation capability enabled, offer the same content as a downloadable file with that name; otherwise say nothing about files. Never claim anything was saved, sent, diarised, renewed, terminated or notified.

## Use cases

| Scenario | What you say |
|---|---|
| Quarterly review of one category's contracts | Run the quarterly contract review for the IT category from the attached register: as-of date today, horizon 180 days, dates in day-month-year order, and one action list per owner. |
| Owner asks what falls due before year end | From the pasted list of the contracts I own, work out which notice deadlines fall before 31 December, show the arithmetic for each and state the decision every one needs as options. |
| Register with gaps in dates and owners | Build a renewal radar from the attached contract list even though several rows have no end date or owner; mark those UNKNOWN, put them in the data gap register and tell me who to ask. |

## Try it (example prompts)

- Build a renewal tracker from the attached contract register. The as-of date is today, the horizon is 180 days and dates are in day-month-year order; the columns are contract ref, counterparty, owner, end date, renewal type, notice period and annual value.
- Tell me what comes up for renewal in the next six months from the pasted contract list. End dates and notice periods in months are in the table; use 1 October as the as-of date and show the notice deadline arithmetic for every row.
- Work out when notice is due on the software contracts in the attached spreadsheet. Treat the notice period column as calendar days, the as-of date is 16 September, and give each owner their own action list.
- Run the quarterly contract review for the facilities category from the contract list in the knowledge source: horizon 120 days, decision lead time 45 days, and flag every row with a missing end date or owner.
- Show me which contracts auto-renew in the pasted table of supplier agreements and give me a monthly deadline calendar. Notice periods are a mix of days and months; the as-of date is the first of next month and I want the default urgency bands.

## Limitations

- One task at a time: give the skill one job per request and confirm the result before the next.
- You own sensitive-data handling: the skill reads what you give it or what the agent can reach; keep restricted documents out of the knowledge sources you attach.
- The output is a draft, not final authority: every figure, quote and action is for you to verify and perform. The skill never approves, authorises or signs anything off.

## Related skills

- contract-review-pack: reviewing one contract's full text and clauses
- clause-comparison-table: comparing the wording of specific clauses across contracts
- procurement-reviewer: pressure-testing a renewal proposal before a sourcing committee

## Add it to an agent (Agent Builder)

1. Copilot chat, **Agents & Skills**, **New agent** (or open an existing agent). Frontier enrolment and a Microsoft 365 Copilot licence are required; custom skills are in preview.
2. **Configure**, expand **Skills**, **Add**, upload the zip you downloaded above (the whole zip, never `SKILL.md` alone). Up to eight skills per agent.
3. **Knowledge**: point the agent at a SharePoint library or OneDrive folder holding the documents listed above. Do not upload knowledge files while skills are attached (not supported yet).
4. **Preview**: try one of the example prompts. The description is the trigger, so use its words.

## Run it standalone: paste this into the agent's Instructions

```
Purpose: this agent helps contract owners and procurement or legal leads see which contracts come up for renewal, when notice falls due and what decision each needs, computed from the contract list they already hold. General guidelines: work only from what the user attaches or pastes and from the knowledge sources configured on this agent. Quote every date, period, value and name as stated, show the arithmetic behind each computed deadline, and never assume a notice period, renewal term, owner or threshold. Present decisions as options with a decision-by date, never as a recommendation; quote clause text without interpreting it. When a required input is missing, ask one question at a time and wait for the answer, then carry UNKNOWN for what is still missing, naming the field. Do not assume any capability such as file generation, calendar or mail; if one is unavailable, say so and answer in the chat. Never claim to have saved, sent, diarised, renewed, terminated or served notice on anything; every action is proposed for the user to perform. Every output is a draft for human review. A typed confirmation releases a hold in the workflow for that step only; it authorises no renewal, termination, payment or work. For the task: when the user asks what comes up for renewal, when notice is due, which contracts auto-renew, or for a renewal tracker, radar, calendar or quarterly contract review, follow the contract-renewal-radar skill exactly and return the radar as a DRAFT.
```

Part of a pack? See `packs/` for an orchestrating Instructions file that runs several skills with gates.

## Files

- `SKILL.md`: the skill (front matter plus instructions, under 20,000 characters).
- `README.md`: companion file referenced from the skill.
- `references/renewal-terms-and-urgency.md`: companion file referenced from the skill.

Licence CC BY-SA 4.0. The agent prepares; you decide.

Free: [Copilot on One Page](https://www.kesslernity.com/copilot-on-one-page?utm_source=github&utm_medium=readme&utm_campaign=agent_skills_repo&utm_content=skill_footer), a one-page sheet on how to phrase a request to Copilot. Paid: [Agent Instruction Block Design Guide](https://store.kesslernity.com/l/eyeauo?utm_source=github&utm_medium=readme&utm_campaign=agent_skills_repo&utm_content=skill_footer_guide), $19, twelve patterns for an agent's Instructions field. I am the author and the seller.
