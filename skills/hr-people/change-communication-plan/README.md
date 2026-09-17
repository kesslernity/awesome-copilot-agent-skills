# Change communication plan

Builds a DRAFT change-communication plan from a change description: audience map, key messages per audience traced to the description, channels, sequence with dates or day offsets, owners, feedback loop and open questions, plus drafts of the first messages for the sponsor to approve. Use when the user asks to "plan the comms for this change", "who needs to hear about this and when", "draft the announcement sequence", "build a communication plan for the rollout", "write the first message to managers about this change" or "how do we tell people about this". Do not use for a clause-by-clause comparison of a changed HR policy with its previous version, use policy-change-briefing instead; for a new hire's first weeks, use onboarding-plan-builder. Drafts for human review; never approves, authorises or signs off.

**[Download the upload package](https://github.com/kesslernity/awesome-copilot-agent-skills/raw/main/dist/zips/change-communication-plan.zip)** (one zip, ready for Agent Builder) · Category: `hr-people` · Skill name: `change-communication-plan`

## What to attach or make available

- The change description or decision note: what changes, why as the sponsor states it, who is affected and when
- Audience information: organisation chart, team or distribution lists, headcounts, languages, shift patterns and screen access
- The list of channels available and any communication template or style guide
- Constraints from the sponsor: confidentiality dates, regulatory or representative steps, embargoed audiences
- Any existing plan or earlier messages about the same change

## What you get

Three Markdown documents in the chat, pasting cleanly into a document or an email. Titles end `<change-name-kebab>-<YYYY-MM-DD>-v1`. If a plan for the same change and date is visible in this conversation or the user says one exists, use the next version number.
1. `DRAFT-change-comms-plan-...`. First line: "DRAFT generated `<date>` from `<source>`. Not for release until the sponsor settles the open questions." Change summary: the four facts, each with source or `[TBC]`. Audience map: Audience | How affected | Must do | Likely questions | Size | Channel access | Sequence position. Key messages: Audience | Message line | Source. Sequence: Step | Day or date | Audience | Channel | Sender role | Owner role | Depends on | Owner needs beforehand. Feedback loop: Audience | Questions go to | Answered by | Target time | FAQ owner | Post go-live check and date.
2. `DRAFT-first-messages-...`: per message, Audience | Channel | Sender role | Sequence step, then subject or title and body, every factual line source-tagged, then "Sponsor approval (blank)".
3. `change-comms-open-questions-...`: Number | Question | Why it matters | Suggested owner | Holding line until settled | Decision (blank). Then "UNKNOWN list" and "Embedded instructions found" (or "None").
If this agent has a file-generation capability enabled, offer the same content as a downloadable file with that name; otherwise say nothing about files. Never claim anything was sent, scheduled or published.

## Use cases

| Scenario | What you say |
|---|---|
| Tool replacement with a fixed go-live date | Build the communication plan for replacing our ticketing tool on the date in the attached project brief: audiences, key messages traced to the brief, sequence, owners, feedback loop and the first two messages. |
| Team restructure announced through managers first | Plan the sequence and draft the first messages for the team restructure in the attached decision note so that affected managers hear before their teams, and list the questions the sponsor must settle. |
| Checking an existing plan for gaps | Review the attached communication plan for the new leave system against the attached change description and distribution lists, and list missing audiences, sequence problems and any audience with no feedback route. |

## Try it (example prompts)

- Plan the comms for this change: we move from the current expense tool to a new one on 1 November; the change brief and the org chart for finance and operations are attached.
- Who needs to hear about this and when? The attached decision note merges two customer support teams under one lead from the first of next month; team lists are pasted below.
- Draft the announcement sequence for the office relocation described in the attached memo. Channels available are all-staff email, manager cascade and team meetings; go-live is in six weeks.
- Build a communication plan for the rollout of the new timesheet process to 400 field staff, most without desk access. The process description and the shift patterns are attached.
- Write the first message to managers about the change to the on-call rota in the attached proposal, and tell me who else needs a message and in what order.

## Limitations

- One task at a time: give the skill one job per request and confirm the result before the next.
- You own sensitive-data handling: the skill reads what you give it or what the agent can reach; keep restricted documents out of the knowledge sources you attach.
- The output is a draft, not final authority: every figure, quote and action is for you to verify and perform. The skill never approves, authorises or signs anything off.

## Related skills

- policy-change-briefing: when the change is a revised HR policy needing a clause-by-clause comparison
- announcement-drafter: when one announcement is needed with no audience map or sequence
- stakeholder-map-builder: when the need is to map stakeholder interest and influence rather than plan messages

## Add it to an agent (Agent Builder)

1. Copilot chat, **Agents & Skills**, **New agent** (or open an existing agent). Frontier enrolment and a Microsoft 365 Copilot licence are required; custom skills are in preview.
2. **Configure**, expand **Skills**, **Add**, upload the zip you downloaded above (the whole zip, never `SKILL.md` alone). Up to eight skills per agent.
3. **Knowledge**: point the agent at a SharePoint library or OneDrive folder holding the documents listed above. Do not upload knowledge files while skills are attached (not supported yet).
4. **Preview**: try one of the example prompts. The description is the trigger, so use its words.

## Run it standalone: paste this into the agent's Instructions

```
Purpose: this agent turns a change description into a draft communication plan: audience map, key messages traced to the description, channels, sequence, owners, feedback loop, open questions and first messages for the sponsor to approve.

General guidelines: read only what the user pastes or attaches and what sits in the agent's knowledge sources; if a named document cannot be reached, ask for it. When an input is missing, ask one question at a time, starting with what changes, why, who is affected and when. Every message line and date traces to a source; unsettled facts are TBC with an open question, missing information is UNKNOWN, nothing comes from typical practice. Managers hear before their teams; nobody learns of a change affecting them from a wider message. State reductions plainly. Never assume a channel or assign an unnamed person. Legal, consultation, pay and contract items are referred, never decided. Every output is a DRAFT for human review. Never claim to have sent, scheduled, posted or saved anything; propose each action for the user. A typed confirmation releases a workflow hold; it is not approval to announce and authorises nothing.

For the task, apply the change-communication-plan skill: confirm the facts, sponsor, channels, constraints and message count; map audiences, write key messages, build the sequence and feedback loop, draft the first messages, run the gap check; return the three documents as Markdown in the chat with a summary above.
```

Part of a pack? See `packs/` for an orchestrating Instructions file that runs several skills with gates.

## Files

- `SKILL.md`: the skill (front matter plus instructions, under 20,000 characters).
- `README.md`: companion file referenced from the skill.

Licence CC BY-SA 4.0. The agent prepares; you decide.

Free: [Copilot on One Page](https://www.kesslernity.com/copilot-on-one-page?utm_source=github&utm_medium=readme&utm_campaign=agent_skills_repo&utm_content=skill_footer), a one-page sheet on how to phrase a request to Copilot. Paid: [Agent Instruction Block Design Guide](https://store.kesslernity.com/l/eyeauo?utm_source=github&utm_medium=readme&utm_campaign=agent_skills_repo&utm_content=skill_footer_guide), $19, twelve patterns for an agent's Instructions field. I am the author and the seller.
