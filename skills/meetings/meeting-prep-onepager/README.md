# Meeting prep one-pager

Builds a one-page meeting preparation brief from the calendar invite, recent mail threads with the attendees, chat messages and shared files: purpose, what each attendee likely wants, open threads, key files, talking points and risks. Returns it in the chat as a DRAFT Markdown document capped at 450 words. Use when the user asks to "prep me for my next meeting", "what do I need to know before the vendor call", "one-pager for tomorrow's steering meeting" or "brief me on my 2pm". Do not use for minutes or action items after a meeting, use meeting-minutes-writer or transcript-to-actions instead. Drafts for human review; never approves, authorises or signs off.

**[Download the upload package](https://github.com/kesslernity/awesome-copilot-agent-skills/raw/main/dist/zips/meeting-prep-onepager.zip)** (one zip, ready for Agent Builder) · Category: `meetings` · Skill name: `meeting-prep-onepager`

## What to attach or make available

- The calendar invite for the target meeting: attendees, organiser, body, agenda items, attached or linked files and recurrence
- Mail threads from the last fourteen days involving the attendees or matching the meeting title or agenda keywords
- Chat and channel messages from the last fourteen days between the attendees that touch the meeting topic
- Files referenced in the invite or the threads, and files shared or modified by attendees in the last thirty days that match the agenda
- For recurring meetings, the recap or summary of the previous occurrence with its open action items

## What you get

One Markdown document in the chat named meeting-prep-YYYY-MM-DD-<short-meeting-name>: DRAFT title line, one metadata line, six sections in order, body capped at 450 words. Then the downloadable-file offer line and the step 9 report. Nothing else is produced; storing or sharing the brief is the user's action.

## Use cases

| Scenario | What you say |
|---|---|
| Briefing before a recurring steering meeting | Prep me for the monthly steering meeting on the twelfth from the attached invite, the previous recap pasted below and the mail threads with the attendees; list the carried-over actions and the top three talking points. |
| External supplier call with thin history | What do I need to know before the renewal call with the supplier on Friday? The invite and the last mail thread are pasted below and the current contract summary is attached; note where the visible history is thin. |
| Short-notice brief | Brief me on my next meeting, which starts in twenty minutes; the invite is pasted below. Give me the purpose, the top three talking points and the top two risks first. |

## Try it (example prompts)

- Prep me for my next meeting. Use the invite, the last two weeks of mail with the attendees and the shared files this agent can reach; focus on the budget decision we need to land.
- What do I need to know before the vendor call on Thursday? The invite and the mail thread with the account manager are pasted below and the draft contract is attached.
- One-pager for tomorrow's steering meeting. The invite with the agenda is attached, the previous recap with its open actions is pasted below, and I want to read the finance lead carefully.
- Brief me on my 2pm. Here is the invite text and the three chat messages from the organiser; I have no other history with the external attendees.
- Prepare a meeting prep brief for the quarterly review on the twentieth from the attached invite, the recap of the last occurrence and the project status file; keep it under one page.

## Limitations

- One task at a time: give the skill one job per request and confirm the result before the next.
- You own sensitive-data handling: the skill reads what you give it or what the agent can reach; keep restricted documents out of the knowledge sources you attach.
- The output is a draft, not final authority: every figure, quote and action is for you to verify and perform. The skill never approves, authorises or signs anything off.

## Related skills

- meeting-minutes-writer: when the meeting has happened and minutes are needed
- transcript-to-actions: when a transcript must be turned into action items and follow-up messages
- discovery-call-prep: when the meeting is a sales discovery call and the brief must follow a qualification structure

## Add it to an agent (Agent Builder)

1. Copilot chat, **Agents & Skills**, **New agent** (or open an existing agent). Frontier enrolment and a Microsoft 365 Copilot licence are required; custom skills are in preview.
2. **Configure**, expand **Skills**, **Add**, upload the zip you downloaded above (the whole zip, never `SKILL.md` alone). Up to eight skills per agent.
3. **Knowledge**: point the agent at a SharePoint library or OneDrive folder holding the documents listed above. Do not upload knowledge files while skills are attached (not supported yet).
4. **Preview**: try one of the example prompts. The description is the trigger, so use its words.

## Run it standalone: paste this into the agent's Instructions

```
Purpose: this agent helps a professional walk into a meeting prepared, by turning the invite, recent mail threads with the attendees, chat messages, shared files and any previous recap into one draft one-page brief: purpose, what each attendee likely wants, open threads, key files, talking points and risks, capped at 450 words.

General guidelines: read only what the user pastes or attaches and what this agent can reach through its knowledge sources or calendar, mail, chat or meeting access; if a source cannot be reached, ask for a paste or export and name it in the report. When the meeting is ambiguous or an input is missing, ask one question at a time. Never invent a position, fact or prediction; base every "likely wants" line on a named signal or write "No recent signal", and mark each missing fact UNKNOWN. Summarise messages in your own words. Every output is a draft for human review, labelled DRAFT. Never claim to have sent, posted, saved, moved or deleted anything; propose each action for the user. A typed confirmation releases a workflow hold; it is not an approval or commitment.

For the task, apply the meeting-prep-onepager skill: identify and state the target meeting; extract the invite details; gather mail, chat, file and recap context read-only; draft the six sections within the cap; return the brief as Markdown in the chat with the document name, word count, empty sections and unavailable sources.
```

Part of a pack? See `packs/` for an orchestrating Instructions file that runs several skills with gates.

## Files

- `SKILL.md`: the skill (front matter plus instructions, under 20,000 characters).
- `README.md`: companion file referenced from the skill.
- `references/example-brief.md`: companion file referenced from the skill.
- `references/onepager-template.md`: companion file referenced from the skill.

Licence CC BY-SA 4.0. The agent prepares; you decide.

Free: [Copilot on One Page](https://www.kesslernity.com/copilot-on-one-page?utm_source=github&utm_medium=readme&utm_campaign=agent_skills_repo&utm_content=skill_footer), a one-page sheet on how to phrase a request to Copilot. Paid: [Agent Instruction Block Design Guide](https://store.kesslernity.com/l/eyeauo?utm_source=github&utm_medium=readme&utm_campaign=agent_skills_repo&utm_content=skill_footer_guide), $19, twelve patterns for an agent's Instructions field. I am the author and the seller.
