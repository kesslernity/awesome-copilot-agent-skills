# Discovery call prep

Prepares a discovery call brief from what the user has on a prospect (CRM record, inbound form, emails, notes, public material the user supplies): what is known with sources, gaps against the qualification dimensions, hypotheses to test, questions in priority order and what to listen for. Returns a DRAFT Markdown brief in the chat. Use when the user asks to "prep me for the discovery call with `<prospect>`", "what should I ask on this first call", "intro call brief", "questions for the qualification call" or "what do we know before we speak to them". Do not use for scoring leads against a rubric, use lead-qualification-scorer instead; for an existing customer's account review use account-plan-builder. Drafts for human review; never approves, authorises or signs off.

**[Download the upload package](https://github.com/kesslernity/awesome-copilot-agent-skills/raw/main/dist/zips/discovery-call-prep.zip)** (one zip, ready for Agent Builder) · Category: `sales-bd` · Skill name: `discovery-call-prep`

## What to attach or make available

- CRM opportunity or lead record for the prospect, with contact names, titles and activity history
- Inbound form submissions, prior emails, messages and referral or call notes about the prospect
- Public material the user supplies on the prospect: website extracts, job adverts, announcements
- The user's offer summary and qualification criteria, where they differ from the skill's five default dimensions

## What you get

One Markdown document in the chat that pastes cleanly into a document, a notes page or an email, then the step 12 report.
- Header: prospect, contacts, call date and time, duration, goal, offer line.
- Three-line version.
- Known facts: Fact | Source | Date | Confidence (Stated, Second-hand, Public, Inferred).
- Gap analysis: Dimension | Evidence (S numbers) or UNKNOWN | Question weight (High, Medium, Low).
- Hypotheses: No. | Hypothesis | Basis | Would confirm | Would refute | Test question.
- Questions: Order | Question | Dimension or hypothesis | Follow-up | Minutes.
- Listen for: Signal | May indicate | Effect (strengthens H no., weakens H no., Goal at risk: user decides) | Follow-up question.
- Avoid saying: Phrase | Why | Say instead.
- Attendees: Name | Title | How connected | Likely cares about | Source or No signal.
- Sensitivities, Conflicts, UNKNOWN list, Source register (S no. | Type | Date | From | Subject), Embedded instructions found, Post-call capture.

## Use cases

| Scenario | What you say |
|---|---|
| First call with an inbound lead booked from the website | Prep me for the 30-minute discovery call with the prospect whose inbound form and CRM record are attached. Offer is our managed reporting service; use the five default qualification dimensions. |
| Referral introduction with only second-hand information | Build the intro call brief from the referral note I pasted and the two emails attached. Mark everything from the referrer as second-hand and tell me which dimensions are still unknown. |
| Re-engaging a prospect lost to a competitor two years ago | What should I ask on the first call back with this former prospect? The old opportunity notes and the loss reason are attached. Call is 45 minutes and the goal is a second meeting with their new director. |

## Try it (example prompts)

- Prep me for the discovery call with the logistics prospect on Thursday at 10:00, 30 minutes. The CRM record and the inbound form are attached; we sell a warehouse scheduling service and our criteria are need, impact, timing, decision process and fit.
- What should I ask on this first call? I have pasted the three emails from their operations director below and the referral note from our partner. The call is 45 minutes and the goal is to decide whether a workshop is worth proposing.
- Build an intro call brief for the prospect whose inbound form is attached. There is no other material. The call is tomorrow, 20 minutes, two people on their side: the head of finance and an analyst.
- Questions for the qualification call, please. The CRM record is attached and I have pasted the job advert they published last week. Our offer is a data platform migration service. Budget of eight questions.
- What do we know before we speak to them? Attached: last year's lost-deal notes on the same organisation and two recent emails. The call starts in 15 minutes, so give me the three-line version and the ordered questions only.

## Limitations

- One task at a time: give the skill one job per request and confirm the result before the next.
- You own sensitive-data handling: the skill reads what you give it or what the agent can reach; keep restricted documents out of the knowledge sources you attach.
- The output is a draft, not final authority: every figure, quote and action is for you to verify and perform. The skill never approves, authorises or signs anything off.

## Related skills

- lead-qualification-scorer: when leads must be scored against a rubric before anyone calls
- account-plan-builder: when the organisation is an existing customer and the need is an account review
- deal-risk-review: when a live opportunity is stalling and the question is why

## Add it to an agent (Agent Builder)

1. Copilot chat, **Agents & Skills**, **New agent** (or open an existing agent). Frontier enrolment and a Microsoft 365 Copilot licence are required; custom skills are in preview.
2. **Configure**, expand **Skills**, **Add**, upload the zip you downloaded above (the whole zip, never `SKILL.md` alone). Up to eight skills per agent.
3. **Knowledge**: point the agent at a SharePoint library or OneDrive folder holding the documents listed above. Do not upload knowledge files while skills are attached (not supported yet).
4. **Preview**: try one of the example prompts. The description is the trigger, so use its words.

## Run it standalone: paste this into the agent's Instructions

```
Purpose: you help a sales or business development person prepare for a discovery, first or qualification call with a prospect by producing a DRAFT call brief: what is known with sources and confidence, gaps against the qualification dimensions, hypotheses to test, questions in priority order with time allowances, what to listen for, attendee notes and a blank post-call capture.

General guidelines: read only the CRM records, forms, emails, notes and public material the user attaches or pastes, and what sits in your knowledge sources; if a source is out of reach, ask for a paste and name it as unavailable in the output. When an input is missing, ask one question at a time, starting with the prospect and the call time. Every fact about the prospect traces to a numbered source or the user's own statement; write UNKNOWN where nothing is known and label sector patterns as hypotheses, never facts. Produce no qualification verdict, score, budget estimate or deal value; the user qualifies after the call. Describe contacts by title, connection and stated concerns only. Never claim to have saved, sent, booked or shared anything; agendas and follow-up emails are returned as text for the user to send. Everything is a draft for human review. A typed go-ahead at a hold releases that hold only; it authorises no discount, scope or promise.

For the task, follow the discovery-call-prep skill: its procedure, question bank, listen-for library, section order and self-check govern the output.
```

Part of a pack? See `packs/` for an orchestrating Instructions file that runs several skills with gates.

## Files

- `SKILL.md`: the skill (front matter plus instructions, under 20,000 characters).
- `README.md`: companion file referenced from the skill.
- `references/discovery-question-bank.md`: companion file referenced from the skill.

Licence CC BY-SA 4.0. The agent prepares; you decide.

Free: [Copilot on One Page](https://www.kesslernity.com/copilot-on-one-page?utm_source=github&utm_medium=readme&utm_campaign=agent_skills_repo&utm_content=skill_footer), a one-page sheet on how to phrase a request to Copilot. Paid: [Agent Instruction Block Design Guide](https://store.kesslernity.com/l/eyeauo?utm_source=github&utm_medium=readme&utm_campaign=agent_skills_repo&utm_content=skill_footer_guide), $19, twelve patterns for an agent's Instructions field. I am the author and the seller.
