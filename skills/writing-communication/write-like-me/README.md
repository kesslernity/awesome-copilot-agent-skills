# Write like me

Builds a personal voice profile from roughly 90 days of the user's own sent messages and meeting speech, then drafts emails and documents that match how the user actually writes, returning the profile and every draft as Markdown for the user to keep, paste or send themselves. Use when the user asks to "write this like me", "match my voice", "draft this in my tone", "build my voice profile" or "refresh my voice profile". Do not use for an announcement in the organisation's voice, use announcement-drafter instead, nor for a weekly status email, use weekly-status-update-writer instead. Drafts for human review; never approves, authorises or signs off.

**[Download the upload package](https://github.com/kesslernity/awesome-copilot-agent-skills/raw/main/dist/zips/write-like-me.zip)** (one zip, ready for Agent Builder) · Category: `writing-communication` · Skill name: `write-like-me`

## What to attach or make available

- The user's own sent messages from the last 90 days, exported with date, internal or external recipient and body
- Meeting transcripts with speaker labels where the user spoke, internal meetings only unless the user opts in to external ones
- The saved voice profile document, titled voice-profile, once BUILD has run
- Source material for a requested draft: notes, prior threads, documents or key points the draft must cover

## What you get

- BUILD: voice-profile.md, complete Markdown per references/voice-profile-template.md with the metadata block, plus the keep and delete instructions.
- DRAFT, email: the DRAFT line, then subject and body text for the user to paste and send.
- DRAFT, document: DRAFT-<topic>-YYYY-MM-DD.md with DRAFT on the title line.
- One closing line offering a downloadable file where the agent has that capability, and a closing report naming the profile build date.

## Use cases

| Scenario | What you say |
|---|---|
| First-time voice profile build | Build my voice profile from the attached 90-day sent-mail export, mail only, and return the profile with its metadata block and instructions on where to keep it and when to rebuild. |
| Email in the user's own voice | Write this like me: an email to the finance team asking for the revised budget by Friday, using the attached voice profile and the two points pasted below. |
| Document drafted to match the user's style | Draft this in my tone: a two-page decision note for my manager on the vendor choice, from the attached comparison and my voice profile in the knowledge sources, with DRAFT on the title line. |

## Try it (example prompts)

- Build my voice profile from my sent mail over the last 90 days. The export is attached; skip meeting transcripts for now and tell me how many messages you could use.
- Write this like me: an email to the project sponsor explaining the two-week slip and the recovery plan. My voice profile is in the knowledge folder and the schedule note is pasted below.
- Draft this in my tone: a one-page note to my team about the new on-call rota, based on the attached rota and the three points pasted below. Keep it to my usual length.
- Refresh my voice profile using the attached sent-mail export and the attached transcripts of my internal meetings from the last quarter; external meetings excluded.
- Match my voice for a reply to the pasted customer email, declining the discount request but offering the extended payment term. Use the voice profile attached.

## Limitations

- One task at a time: give the skill one job per request and confirm the result before the next.
- You own sensitive-data handling: the skill reads what you give it or what the agent can reach; keep restricted documents out of the knowledge sources you attach.
- The output is a draft, not final authority: every figure, quote and action is for you to verify and perform. The skill never approves, authorises or signs anything off.

## Related skills

- announcement-drafter: when the message must speak in the organisation's voice rather than the user's own
- weekly-status-update-writer: when the email is a periodic status update built from notes and trackers
- transcript-to-actions: when the need is owner emails and actions after a meeting rather than a personal-voice draft

## Add it to an agent (Agent Builder)

1. Copilot chat, **Agents & Skills**, **New agent** (or open an existing agent). Frontier enrolment and a Microsoft 365 Copilot licence are required; custom skills are in preview.
2. **Configure**, expand **Skills**, **Add**, upload the zip you downloaded above (the whole zip, never `SKILL.md` alone). Up to eight skills per agent.
3. **Knowledge**: point the agent at a SharePoint library or OneDrive folder holding the documents listed above. Do not upload knowledge files while skills are attached (not supported yet).
4. **Preview**: try one of the example prompts. The description is the trigger, so use its words.

## Run it standalone: paste this into the agent's Instructions

```
Purpose: this agent helps a person produce emails and documents that read as if they wrote them, in two modes: BUILD creates a reusable voice profile from the user's own sent messages and their own speech turns in meeting transcripts; DRAFT applies that profile to a requested email or document.

General guidelines: read only what the user attaches or pastes and what sits in the agent's knowledge sources or mail and meeting access; if the sent mail, transcripts or a named source cannot be reached, ask for an export and say so. When an input is missing, ask one question at a time. Analyse only the user's own words; strip quoted messages, signatures and other participants' speech. The profile records stylistic features only and never carries third-party names, client identifiers, deal terms or message subjects. Never invent a fact, date, figure or commitment; gaps read UNKNOWN and unstated decisions read DECIDE. Every email and document is a DRAFT for human review; the user pastes and sends it. Never claim to have saved, sent, moved or deleted anything. A typed confirmation releases a workflow hold; it is not approval of the content.

For the task, apply the write-like-me skill: select mode, confirm scope and the transcript decision, build or load the profile, draft to the recorded greeting, sign-off, sentence length, vocabulary and structure habits, run the self-check, and return the profile or the draft as Markdown in the chat with the profile build date.
```

Part of a pack? See `packs/` for an orchestrating Instructions file that runs several skills with gates.

## Files

- `SKILL.md`: the skill (front matter plus instructions, under 20,000 characters).
- `references/voice-profile-template.md`: companion file referenced from the skill.

Licence CC BY-SA 4.0. The agent prepares; you decide.
