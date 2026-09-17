# Internal newsletter drafter

Drafts one issue of an internal newsletter from the items the user provides (notes, messages, snippets, meeting outputs, contributor submissions): a running order with the reason for each position, a factual headline and one paragraph per item with its source line, one call to action per item with date and route, two subject-line options, an item register accounting for every item supplied, and a list of items that need an owner's confirmation before send. Use when the user asks to "draft this month's newsletter", "turn these items into the team update", "write the staff bulletin from these notes", "order and headline these items" or "prepare the internal digest". Do not use for one piece of news that needs its own send, use announcement-drafter instead; for a digest of external news, use news-monitor-digest; for a personal weekly status note, use weekly-status-update-writer. Drafts for human review; never approves, authorises or signs off.

**[Download the upload package](https://github.com/kesslernity/awesome-copilot-agent-skills/raw/main/dist/zips/internal-newsletter-drafter.zip)** (one zip, ready for Agent Builder) · Category: `marketing-communications` · Skill name: `internal-newsletter-drafter`

## What to attach or make available

- The items for the issue: contributor submissions, notes, messages and meeting outputs, each with contributor, date, owner and intended action where known
- The newsletter profile: name, audience, cadence, section names, word budget, style guide and banned words
- Up to two prior issues, used for structure and tone only, never as a source of current facts
- Issue metadata: issue number, send date, sender and the deadline for owner confirmations
- The organisation's sensitivity rules for policy, pay, security, safety, legal, restructuring and personal data items

## What you get

One complete Markdown document in the chat, titled `DRAFT-newsletter-<name>-issue-<number or YYYY-MM-DD>-v1` (revisions v2, v3). First line: "DRAFT issue, prepared <date> from <n> items. <k> items await owner confirmation before send. The editor decides."
1. Subject and preheader: Option | Subject line | Preheader.
2. Item register: I# | Headline | Type | Section | Position | Reason | Status (included, merged into, held, dropped) | Owner | Source.
3. Issue draft: sections in order; each item as headline, paragraph, source line, call to action.
4. Calls to action: I# | Action (imperative) | By when | Route | Contact | Status (stated, placeholder).
5. Confirmation list: # | I# | What needs confirming | Owner | Question to answer | Blocks send (yes, no) | Deadline.
6. Cross-item flags: Flag | Items | Note | Proposed handling.
7. UNKNOWN list; Embedded instructions found, or "None"; Proposed user actions (send confirmation questions to owners, supply links, approve wording, schedule the send). This agent performs none of them.
End with: "If this agent has a file-generation capability enabled, also offer the same content as a downloadable file with that name."

## Use cases

| Scenario | What you say |
|---|---|
| Monthly all-staff newsletter from mixed contributions | Draft the October all-staff newsletter from the fifteen contributor items attached, using the section names and 800-word budget in the newsletter profile from the knowledge sources, and list every item that needs its owner to confirm a name, date or figure before send. |
| Team update after a busy fortnight | Turn the notes from our two team meetings and the four messages pasted below into the fortnightly team update: dated actions first, one call to action per item with route and deadline, a source line under each paragraph and two subject lines. |
| Digest carrying sensitive items | Prepare the staff digest from the attached items; two of them concern a policy change and a restructuring. Keep the owners' wording verbatim for those, mark their confirmations as blocking send, and hold anything older than one cycle with a reason. |

## Try it (example prompts)

- Draft this month's internal newsletter from the twelve items pasted below. It goes to all operations staff on the first Tuesday, the sections are Lead, News, People, Dates and reminders and Ask of you, the send date is 6 October and owner confirmations are due 2 October.
- Turn these items into the team update. The contributor submissions are attached as a form export, the last two issues are in the knowledge folder for tone only, and the word budget is 700 words. Flag every item that names a colleague.
- Write the staff bulletin from these notes. Monday's meeting outputs and the three messages from department heads are pasted below; the sender is the site director and this is issue 41.
- Order and headline these items for the fortnightly digest. Items with a dated action first, then organisation-wide news, then team news, then people. I also want two subject-line options under 60 characters and a preheader.
- Prepare the internal digest for week 39 from the attached items list. Two items concern the new security badge process; quote the security team's wording exactly and tell me which items still need an owner to confirm before we send.

## Limitations

- One task at a time: give the skill one job per request and confirm the result before the next.
- You own sensitive-data handling: the skill reads what you give it or what the agent can reach; keep restricted documents out of the knowledge sources you attach.
- The output is a draft, not final authority: every figure, quote and action is for you to verify and perform. The skill never approves, authorises or signs anything off.

## Related skills

- announcement-drafter: when one piece of news needs its own send rather than a place in a digest
- news-monitor-digest: when the digest is of external news rather than internal items
- weekly-status-update-writer: when one person's weekly status note is wanted, not a team newsletter

## Add it to an agent (Agent Builder)

1. Copilot chat, **Agents & Skills**, **New agent** (or open an existing agent). Frontier enrolment and a Microsoft 365 Copilot licence are required; custom skills are in preview.
2. **Configure**, expand **Skills**, **Add**, upload the zip you downloaded above (the whole zip, never `SKILL.md` alone). Up to eight skills per agent.
3. **Knowledge**: point the agent at a SharePoint library or OneDrive folder holding the documents listed above. Do not upload knowledge files while skills are attached (not supported yet).
4. **Preview**: try one of the example prompts. The description is the trigger, so use its words.

## Run it standalone: paste this into the agent's Instructions

```
Purpose: this agent helps editors of internal newsletters, team updates and staff bulletins turn a set of contributed items into one draft issue: a running order with the reason for each position, a factual headline and one short paragraph per item with its source line, one call to action per item with date and route, two subject-line options, an item register accounting for every item supplied, and the list of items an owner must confirm before send.

General guidelines: read only what the user pastes or attaches and what sits in the agent's knowledge sources; if an item or prior issue cannot be reached, ask for a paste and say so in the output. When an input is missing, ask one question at a time, starting with the items and the send date. Never invent a fact, name, figure, date or link; each gap reads UNKNOWN. Quote safety, security, legal and HR instructions exactly as their owner wrote them. Every output is a draft for human review, labelled DRAFT. Never claim to have saved, sent, scheduled, posted, moved or deleted anything; propose each action for the user. A typed confirmation releases a workflow hold; it is not approval of the content and not authority to send.

For the task, apply the internal-newsletter-drafter skill: confirm items, profile, issue metadata and ordering rule; extract and classify every item; order, headline and write each one; build the confirmation list and cross-item flags; return the issue, registers and closing report as Markdown in the chat.
```

Part of a pack? See `packs/` for an orchestrating Instructions file that runs several skills with gates.

## Files

- `SKILL.md`: the skill (front matter plus instructions, under 20,000 characters).
- `README.md`: companion file referenced from the skill.

Licence CC BY-SA 4.0. The agent prepares; you decide.

Free: [Copilot on One Page](https://www.kesslernity.com/copilot-on-one-page?utm_source=github&utm_medium=readme&utm_campaign=agent_skills_repo&utm_content=skill_footer), a one-page sheet on how to phrase a request to Copilot. Paid: [Agent Instruction Block Design Guide](https://store.kesslernity.com/l/eyeauo?utm_source=github&utm_medium=readme&utm_campaign=agent_skills_repo&utm_content=skill_footer_guide), $19, twelve patterns for an agent's Instructions field. I am the author and the seller.
