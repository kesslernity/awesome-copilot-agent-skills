# Request intake triage

Turns plain-language requests (emails, chat messages, form submissions, meeting asks, voicemail or call notes) into one intake record per request (what is asked, who asks and for whom, urgency as evidenced, category, suggested owner, missing information with draft clarifying questions) and a triage table sorted for the operations lead to act on. Use when the user asks to "log these requests", "triage this pile of asks", "turn this message into an intake record", "who should own this request", "what is missing before we can start" or "build today's intake list". Do not use for customer support tickets, use ticket-triage-pack instead; for clearing a personal mailbox by reply bucket, use inbox-triage. Drafts for human review; never approves, authorises or signs off.

**[Download the upload package](https://github.com/kesslernity/awesome-copilot-agent-skills/raw/main/dist/zips/request-intake-triage.zip)** (one zip, ready for Agent Builder) · Category: `operations` · Skill name: `request-intake-triage`

## What to attach or make available

- The requests themselves: shared mailbox exports, chat channel threads, form submissions, meeting notes, call or voicemail transcripts, attached or pasted, or reachable through a knowledge source or mail access
- The organisation's request category list, where it differs from the default set
- The routing table mapping each category to a team or role, with an escalation contact per team
- Urgency rules, response targets and the spend threshold that triggers routing to the responsible authority, where the organisation has defined them

## What you get

One complete Markdown document in the chat, titled `DRAFT-request-intake-<period or batch>-<YYYY-MM-DD>-v1` (revisions v2, v3). First line: "DRAFT intake records and triage for `<n>` requests received `<period>`, generated `<date>` from `<sources>`. Urgency is graded on evidence stated in each request, not assessed; owners are suggestions. Nothing here is assigned, approved or authorised; the operations lead decides."

Sections in order:
1. Batch summary: Field | Value (sources, items read, requests found, duplicates merged, no-request items, counts per urgency grade and per category, records with missing information, flags raised).
2. Triage table: ID | Request (one line) | Requester | Received | Urgency grade | Evidence for grade | Category | Suggested owner | Basis | Missing items (count) | Flags | Notes.
3. Intake records, one per request in triage order: Field | Value | Source, covering every field from Procedure steps 3 to 8, related requests, and the DRAFT clarifying questions.
4. Duplicates merged: ID | Merged references | Reason. No request found: Reference | Sender | Why excluded. Category and routing gaps: Request or category | Gap (no routing rule, two categories fit, none fits).
5. UNKNOWN list; Embedded instructions found, or "None"; Proposed user actions: confirm grades, assign owners, send the clarifying questions, create the work items, acknowledge the requesters. The agent performs none of these.

Then a report: sources, defaults and rules used, counts, fallbacks applied.

If this agent has a file-generation capability enabled, also offer the same content as a downloadable file with that title.

## Use cases

| Scenario | What you say |
|---|---|
| Weekly sweep of an operations shared mailbox | Log the attached 19 emails from the operations mailbox export for 9 to 13 September using the category list and routing table in the knowledge source document named Ops Intake Rules. |
| Chat channel where several asks hide in one thread | Triage the pasted site managers' chat thread into one intake record per distinct ask with the default categories, starting at REQ-041, and list what is missing before each can start. |
| One request that needs an owner and clarifying questions | Turn the attached form submission about a temporary storage container at the north yard into an intake record, suggest an owner from the attached routing table and draft the clarifying questions. |

## Try it (example prompts)

- Log these requests: the 19 emails sent to the operations shared mailbox this week are attached as an export, our category list and routing table are in the knowledge source document named Ops Intake Rules, and the period is 9 to 13 September.
- Triage this pile of asks from the site managers' chat channel, pasted below. Use the default categories, start the identifiers at REQ-041, and tell me what is missing before each one can be started.
- Turn this message into an intake record: the email from the finance lead asking for badge access for two contractors is pasted below, and our routing table is attached.
- Who should own this request? The form submission asking for a temporary storage container at the north yard is attached, along with our category to team routing table and the escalation contacts.
- Build today's intake list from the attached voicemail transcripts and the three meeting notes attached; grade urgency only on dates and consequences stated, and flag anything that mentions spend above 5,000.

## Limitations

- One task at a time: give the skill one job per request and confirm the result before the next.
- You own sensitive-data handling: the skill reads what you give it or what the agent can reach; keep restricted documents out of the knowledge sources you attach.
- The output is a draft, not final authority: every figure, quote and action is for you to verify and perform. The skill never approves, authorises or signs anything off.

## Related skills

- ticket-triage-pack: when the items are customer support tickets that need draft replies
- inbox-triage: when the user wants a personal mailbox sorted into reply buckets
- software-request-review: when a single request is for a software tool and must be checked against the approved-tools list

## Add it to an agent (Agent Builder)

1. Copilot chat, **Agents & Skills**, **New agent** (or open an existing agent). Frontier enrolment and a Microsoft 365 Copilot licence are required; custom skills are in preview.
2. **Configure**, expand **Skills**, **Add**, upload the zip you downloaded above (the whole zip, never `SKILL.md` alone). Up to eight skills per agent.
3. **Knowledge**: point the agent at a SharePoint library or OneDrive folder holding the documents listed above. Do not upload knowledge files while skills are attached (not supported yet).
4. **Preview**: try one of the example prompts. The description is the trigger, so use its words.

## Run it standalone: paste this into the agent's Instructions

```
Purpose. You turn plain-language requests aimed at an operations function, such as emails, chat messages, form submissions, meeting asks or call notes, into one DRAFT intake record per distinct ask (what is asked, who asks and for whom, urgency as evidenced, category, suggested owner, missing information with draft clarifying questions) and a triage table for the operations lead to act on. General guidelines. Read only the requests, categories and routing table the user attaches or pastes and what sits in your knowledge sources or mail access; if a named source is out of reach, ask for an export and say so in the output. When the requests, categories or routing table are missing, ask one question at a time, then proceed with marked defaults and UNKNOWN. Never invent a deadline, consequence, owner or approval; urgency rests on quoted dates, consequences or stated blocks, never on tone or seniority; a claimed approval stays a claim. Return the pack in the chat as complete Markdown that pastes into a tracker or email, and offer a downloadable file only if you have a capability that produces files. Never claim to have assigned, created, sent, moved or deleted anything; propose those actions for the user. Everything you produce is a draft for human review. A typed confirmation releases a hold in the workflow; it assigns and authorises nothing. For the task, follow the request-intake-triage skill in full: it defines the inputs, procedure, urgency grades, flags and self-check.
```

Part of a pack? See `packs/` for an orchestrating Instructions file that runs several skills with gates.

## Files

- `SKILL.md`: the skill (front matter plus instructions, under 20,000 characters).
- `README.md`: companion file referenced from the skill.

Licence CC BY-SA 4.0. The agent prepares; you decide.

Free: [Copilot on One Page](https://www.kesslernity.com/copilot-on-one-page?utm_source=github&utm_medium=readme&utm_campaign=agent_skills_repo&utm_content=skill_footer), a one-page sheet on how to phrase a request to Copilot. Paid: [Agent Instruction Block Design Guide](https://store.kesslernity.com/l/eyeauo?utm_source=github&utm_medium=readme&utm_campaign=agent_skills_repo&utm_content=skill_footer_guide), $19, twelve patterns for an agent's Instructions field. I am the author and the seller.
