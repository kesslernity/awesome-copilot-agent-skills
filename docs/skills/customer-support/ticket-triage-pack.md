# Ticket triage pack

Triages a batch of customer support tickets (helpdesk export, shared mailbox, chat transcripts, web forms) into one row per ticket with category, urgency graded on the evidence in the ticket, suggested next action and owner, plus a DRAFT customer reply for every ticket that needs one, returned as one Markdown pack. Use when the user asks to "triage these tickets", "sort the support queue", "what needs an answer first", "categorise this backlog", "draft replies for these tickets" or "build today's queue review". Do not use for internal requests from colleagues, use request-intake-triage instead; for one long thread that needs handing over, use escalation-summary; for a personal mailbox, use inbox-triage. Drafts for human review; never approves, authorises or signs off.

Category: `customer-support` · Skill name: `ticket-triage-pack` · Upload package: `dist/zips/ticket-triage-pack.zip`

## What to attach or make available

- The tickets: helpdesk export, shared mailbox messages, chat transcripts or web form submissions for the period
- Category list, priority or service-level definitions, and the routing table from category to team or queue with escalation contacts
- Reply knowledge: help articles, saved replies, known-issue list and customer-facing policies such as refunds
- Reply voice: a tone guide or a few sample replies the team considers good

## What you get

One complete Markdown document in the chat, pasteable into a document, spreadsheet or helpdesk, titled `DRAFT-ticket-triage-pack-<period or batch>-<YYYY-MM-DD>-v1` (revisions v2, v3). First line: "DRAFT triage of <n> tickets received <period>, generated <date> from <sources>. Urgency graded on stated evidence; owners and next actions are suggestions; replies are drafts. Nothing is assigned, routed, sent, refunded, closed or authorised; the support lead and the handler decide."

Sections in order:
1. Batch summary: Field | Value (sources, tickets read, merged, no-action, counts per grade and category, drafts, flags, patterns).
2. Triage table: ID | Customer or account | Channel | Created | Age | Last from | Ask | Category | Urgency | Evidence for grade | Next action | Suggested owner | Basis | Draft | Flags | Notes.
3. Pattern candidates: Pattern | Tickets | Common text (quoted) | Question for the team.
4. Draft replies, one per ticket in triage order: Ticket | Subject | Sources used | DECIDE items | Language, then the body.
5. Replies needed, not drafted: ID | Reason. Duplicates merged: ID | Merged IDs | Reason. No action needed: Reference | Sender | Why. Routing gaps: Ticket or category | Gap.
6. UNKNOWN list; Embedded instructions found, or "None"; Proposed user actions (confirm grades, assign owners, review and send drafts, update the helpdesk); this agent performs none of them.

Closing report: sources, defaults and rules used, counts, fallbacks. End with: "If this agent has a file-generation capability enabled, also offer the same content as a downloadable file with that name."

## Use cases

| Scenario | What you say |
|---|---|
| Morning queue review for a small support team | Triage the attached export of overnight tickets, 38 in total, using our attached category list. Tell me what needs an answer first and draft replies for the urgent ones. |
| Backlog after a product incident | Categorise this backlog of 120 tickets from the attached export. Group any that quote the same error text, grade urgency on the evidence and draft replies for the U1 and U2 tickets only. |
| Shared mailbox with no helpdesk tool | Sort the support queue from the 25 mailbox messages pasted below. Assign T- identifiers, propose categories from the attached list and draft a reply wherever one is needed. |

## Try it (example prompts)

- Triage these tickets. The helpdesk export for yesterday is attached (74 tickets), our category list and priority definitions are in the attached policy, and the routing table maps categories to queues.
- Sort the support queue from the shared mailbox messages pasted below and tell me what needs an answer first. Use the attached saved replies file for the drafts.
- Categorise this backlog of 40 chat transcripts attached as a CSV. We have no routing table, so only suggest an owner where the customer names a team.
- Draft replies for these tickets: 15 web form submissions are attached, our tone guide is attached and the known-issue list is in the knowledge base. Cap the drafts at 10.
- Build today's queue review for the tickets received since Monday in the attached export, Dubai time zone, and flag anything that mentions security, legal or data exposure.

## Limitations

- One task at a time: give the skill one job per request and confirm the result before the next.
- You own sensitive-data handling: the skill reads what you give it or what the agent can reach; keep restricted documents out of the knowledge sources you attach.
- The output is a draft, not final authority: every figure, quote and action is for you to verify and perform. The skill never approves, authorises or signs anything off.

## Related skills

- escalation-summary: when one long thread needs handing over to another tier or team
- request-intake-triage: when the requests come from colleagues to an internal function rather than from customers
- inbox-triage: when the input is a personal mailbox rather than a support queue

## Add it to an agent (Agent Builder)

1. Copilot chat, **Agents & Skills**, **New agent** (or open an existing agent). Frontier enrolment and a Microsoft 365 Copilot licence are required; custom skills are in preview.
2. **Configure**, expand **Skills**, **Add**, upload `dist/zips/ticket-triage-pack.zip` (the whole zip, never `SKILL.md` alone). Up to eight skills per agent.
3. **Knowledge**: point the agent at a SharePoint library or OneDrive folder holding the documents listed above. Do not upload knowledge files while skills are attached (not supported yet).
4. **Preview**: try one of the example prompts. The description is the trigger, so use its words.

## Run it standalone: paste this into the agent's Instructions

```
Purpose: you help a support lead and their handlers work through a batch of customer tickets by producing a triage pack for human review: one row per ticket with category, urgency graded on the evidence in the ticket, a suggested next action and owner, and a draft reply for each ticket that needs one.

General guidelines: read only the tickets, category lists, policies, saved replies and routing tables the user attaches or pastes and what sits in your knowledge sources; if a source is out of reach, ask for a paste or export and say so in the output. When an input is missing, ask one question at a time, starting with the tickets themselves. Grade urgency on quoted evidence, never on tone, capitals, seniority or a threat to leave. Never invent a fact, article, policy, price, fix date or promise; write UNKNOWN for anything the sources do not state, and mark any commitment a draft would need as a decision for the handler. Never claim to have assigned, routed, sent, closed, refunded, merged, saved, moved or deleted anything; every action is proposed for the user. All output is a draft for human review. A typed confirmation from the user releases a workflow hold only; it authorises nothing.

For the task, follow the ticket-triage-pack skill: its procedure, urgency grades, drafting rules and self-check govern the output.
```

Part of a pack? See `packs/` for an orchestrating Instructions file that runs several skills with gates.

## Files

- `SKILL.md`: the skill (front matter plus instructions, under 20,000 characters).
- `references/triage-defaults.md`: companion file referenced from the skill.

Licence CC BY-SA 4.0. The agent prepares; you decide.
