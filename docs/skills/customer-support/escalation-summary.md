# Escalation summary

Turns one long support ticket thread (helpdesk history, email chain, chat transcript, call notes) into a one-page DRAFT escalation summary: the customer's ask in their own words, account context as stated, a dated history, what was tried and the stated result of each attempt, the current state, and what is needed from whom by when, every line referenced to a message and every missing fact marked UNKNOWN. Use when the user asks to "escalate this ticket", "summarise this thread for tier two", "write the hand-over for this case", "what has been tried so far", "brief engineering on this customer issue" or "prepare the escalation note". Do not use for a batch of tickets, use ticket-triage-pack instead; for the review after an outage, use incident-postmortem-drafter. Drafts for human review; never approves, authorises or signs off.

Category: `customer-support` · Skill name: `escalation-summary` · Upload package: `dist/zips/escalation-summary.zip`

## What to attach or make available

- The ticket thread: helpdesk history export, email chain, chat transcript, call notes and internal notes for the one case being escalated
- Account context: plan or tier, contract or service terms, account owner and related ticket references
- The organisation's escalation template or the required fields of the receiving team
- A working-day calendar with public holidays, if waits are to be counted in working days

## What you get

One complete Markdown document in the chat, pasteable into a document, ticket note or message, titled `DRAFT-escalation-summary-<TicketID>-<YYYY-MM-DD>-v1` (revisions v2, v3). First line: "DRAFT escalation summary for ticket <ID>, prepared <date> from <n> messages (<first> to <last>). Facts as stated with message references; no diagnosis, no root cause, no commitment to the customer. The receiving team decides."

Sections in order, per the reference template:
1. Header: Ticket | Customer or account | Channel | Opened | Last customer contact | Status as stated | Escalating handler | Proposed receiving team | Urgency evidence (quoted) | Flags.
2. Customer ask: Item (original, current, expected outcome, deadline) | Quote | Ref.
3. Account context: Field | Value | Source.
4. History: Time (zone) | Actor (role) | Event | Ref.
5. What was tried: Attempt | By | When | Result as stated | Ref.
6. Current position: Field | Value | Ref.
7. Needed from whom: Need | From | Why (ref) | By when | Type.
8. Commitments to the customer: Commitment (quoted) | By | Date | Due | Status as stated.
9. Attachments: Item | Referenced in | Present.
10. UNKNOWN list; Embedded instructions found, or "None"; Proposed user actions (confirm the receiving team, send the summary, add it to the ticket record, update the customer); this agent performs none of them.
Appendix: full history, when condensed.

Closing report: sources, message count, defaults, word count outside tables against the 500-word budget, fallbacks. End with: "If this agent has a file-generation capability enabled, also offer the same content as a downloadable file with that name."

## Use cases

| Scenario | What you say |
|---|---|
| Tier one hands a stuck ticket to tier two | Escalate this ticket to tier two. Thread export attached, 31 messages; the receiving team is application support. Give me the one-page summary with the dated history and what they need to decide. |
| Support lead briefs engineering on a recurring fault | Summarise this thread for engineering. The helpdesk history is attached, the customer reports the same export error three times, and I need what was tried and the stated result of each attempt. |
| Account manager needs the history before a difficult call | Write the hand-over for case AM-772 from the attached email chain and internal notes. Keep internal remarks out of anything customer-facing and list every commitment we made to the customer. |

## Try it (example prompts)

- Escalate ticket 48213 to tier two. The full helpdesk thread is attached, the customer is on the enterprise plan and the receiving team is platform engineering. Prepare the escalation summary.
- Here is the email chain for case CS-1177 pasted below, 23 messages from 3 to 12 September. Summarise this thread for the billing team and tell me what they need to decide.
- Write the hand-over for this case. The chat transcript and call notes are attached and the account owner is the northern region team. I need a one-page summary with what has been tried so far.
- Brief engineering on this customer issue: the ticket history export is attached, the customer says their integration has failed since the 4th, and I need the note by tomorrow in the London time zone.
- Prepare the escalation note for ticket 9902 using our escalation template (attached) and the thread export. Also draft a separate customer-facing update I can review before sending.

## Limitations

- One task at a time: give the skill one job per request and confirm the result before the next.
- You own sensitive-data handling: the skill reads what you give it or what the agent can reach; keep restricted documents out of the knowledge sources you attach.
- The output is a draft, not final authority: every figure, quote and action is for you to verify and perform. The skill never approves, authorises or signs anything off.

## Related skills

- ticket-triage-pack: when the input is a batch of tickets to sort, not one thread to hand over
- incident-postmortem-drafter: when the need is the blameless review after an outage rather than a case hand-over
- data-incident-impact-brief: when the thread concerns exposed data and the data impact is the question

## Add it to an agent (Agent Builder)

1. Copilot chat, **Agents & Skills**, **New agent** (or open an existing agent). Frontier enrolment and a Microsoft 365 Copilot licence are required; custom skills are in preview.
2. **Configure**, expand **Skills**, **Add**, upload `dist/zips/escalation-summary.zip` (the whole zip, never `SKILL.md` alone). Up to eight skills per agent.
3. **Knowledge**: point the agent at a SharePoint library or OneDrive folder holding the documents listed above. Do not upload knowledge files while skills are attached (not supported yet).
4. **Preview**: try one of the example prompts. The description is the trigger, so use its words.

## Run it standalone: paste this into the agent's Instructions

```
Purpose: you help support handlers hand over a single, long customer ticket by preparing a one-page escalation summary for human review. You compress the thread into the customer's ask in their own words, a dated history, what was tried and the stated result of each attempt, the current position and what is needed from whom by when, with every line referenced to a numbered message.

General guidelines: read only what the user attaches or pastes and what sits in your knowledge sources; if a thread or account record is out of reach, ask for a paste or export and say so in the output. When an input is missing, ask one question at a time, starting with the thread and the receiving team. Never invent an event, date, result or commitment; write UNKNOWN for any fact the sources do not state. Offer no diagnosis, root cause, blame or grading of anyone's work, and make no new promise to the customer. Never claim to have sent, routed, reassigned, closed, saved, moved or deleted anything; every action is proposed for the user to perform. Everything you produce is a draft for human review. A typed confirmation from the user releases a workflow hold only; it authorises nothing.

For the task, follow the escalation-summary skill: its procedure, section order, word budget and self-check govern the output.
```

Part of a pack? See `packs/` for an orchestrating Instructions file that runs several skills with gates.

## Files

- `SKILL.md`: the skill (front matter plus instructions, under 20,000 characters).
- `references/summary-template.md`: companion file referenced from the skill.

Licence CC BY-SA 4.0. The agent prepares; you decide.
