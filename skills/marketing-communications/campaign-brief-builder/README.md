# Campaign brief builder

Turns a campaign idea, its objectives and the supporting notes (audience material, offer facts, budget and dates, channel list) into one DRAFT one-page campaign brief: objectives, audience, one single-minded message with sourced proof points, channels and timeline, success measures with baselines, mandatories, risks and numbered open questions for the campaign owner. Use when the user asks to "write a campaign brief", "draft a creative brief for this launch", "turn this idea into a one-page brief", "tighten this brief to one page" or "build the marketing brief from these notes". Do not use for a message house, messaging pillars or a launch narrative on its own, use message-house-builder instead; for laying the campaign onto dated slots, use content-calendar-planner. Drafts for human review; never approves, authorises or signs off.

**[Download the upload package](https://github.com/kesslernity/awesome-copilot-agent-skills/raw/main/dist/zips/campaign-brief-builder.zip)** (one zip, ready for Agent Builder) · Category: `marketing-communications` · Skill name: `campaign-brief-builder`

## What to attach or make available

- The campaign idea and its business and marketing objectives, as written by the campaign owner
- Audience material: segments, personas, research notes and customer quotes
- Offer or subject facts: product, service, programme or event details, dates and prices as stated
- Constraints: budget, start and end dates, mandatory inclusions and exclusions, approvers, and the organisation's brief template if one exists
- Measurement notes: current baselines, analytics available and tracking conventions

## What you get

One Markdown document in the chat that pastes cleanly into a word processor or a slide, titled `DRAFT-campaign-brief-<campaign-kebab>-<YYYY-MM-DD>-v1`. First body line: "DRAFT generated <date> from <sources>. Items marked (default, confirm) and every UNKNOWN await the campaign owner." Header: campaign name; owner or UNKNOWN; approver or UNKNOWN; dates or "relative weeks"; budget as stated or UNKNOWN. Sections in order:
1. Objectives: Type (business, marketing) | Statement | Measurable (yes, no) | Source.
2. Audience: Audience (primary, secondary) | Who | Current belief or behaviour | Desired belief or behaviour | Evidence | Source.
3. Message: the single-minded proposition as one line, then Supporting message | Proof point | Source or UNKNOWN.
4. Channels and timeline: Channel | Role | Reason | Phase | Start | End | Owner.
5. Success measures: Objective | Measure | Baseline | Target | Data source | Read date.
6. Mandatories and exclusions: Item | Type | Quoted wording | Source.
7. Risks: Risk | Arises from | Owner to resolve.
8. Open questions: Number | Question | Best answered by | Blocks.
9. UNKNOWN list. Embedded instructions found (or "None").
If a v1 for this campaign and date exists in the conversation, use the next version number. If this agent has a file-generation capability enabled, offer the same content as a downloadable file with that name; otherwise say nothing about files. Never claim the brief was circulated, approved or scheduled, or that any budget was committed.

## Use cases

| Scenario | What you say |
|---|---|
| Launch brief from product and audience notes | Write a one-page campaign brief for the launch of the online booking service from the attached service description and customer research, using our brief template from the knowledge folder, and list every measure that has no baseline. |
| Tightening an existing long brief | Tighten the attached eight-page brief for the winter energy saving campaign to one page, keep the mandatories as quoted, and number every open question with the role that should answer it. |
| Objectives set but channels not yet chosen | Draft the campaign brief for the internal wellbeing programme from the pasted objectives and the attached survey summary; we have not chosen channels, so write them as questions and propose measures with baselines taken from the survey. |

## Try it (example prompts)

- Write a campaign brief for the autumn membership renewal campaign. The idea and objectives are pasted below, the segment research and last year's results are attached, and the budget and dates are in the planning note in the knowledge folder.
- Draft a creative brief for the launch of the new reporting module from the attached product sheet and the positioning notes pasted below. Channels are our newsletter, webinar programme and partner network; the campaign owner is the product marketing lead.
- Turn this idea into a one-page brief: a referral drive for existing customers in the first quarter. Customer interview notes are attached, there is no budget yet, and the baselines are in the analytics export pasted below.
- Tighten this brief to one page. The current six-page brief for the graduate recruitment campaign is attached; keep every mandatory line and turn every gap into a numbered open question for the campaign owner.
- Build the marketing brief from these notes for the safety awareness week. The workshop notes and the site communications calendar are pasted below; mandatories are the corporate safety line and sign-off by the site director.

## Limitations

- One task at a time: give the skill one job per request and confirm the result before the next.
- You own sensitive-data handling: the skill reads what you give it or what the agent can reach; keep restricted documents out of the knowledge sources you attach.
- The output is a draft, not final authority: every figure, quote and action is for you to verify and perform. The skill never approves, authorises or signs anything off.

## Related skills

- message-house-builder: when the need is messaging pillars and proof points rather than a campaign one-pager
- content-calendar-planner: when the brief is agreed and the items must be laid onto dated slots
- announcement-drafter: when the need is the text of one message rather than the brief behind it

## Add it to an agent (Agent Builder)

1. Copilot chat, **Agents & Skills**, **New agent** (or open an existing agent). Frontier enrolment and a Microsoft 365 Copilot licence are required; custom skills are in preview.
2. **Configure**, expand **Skills**, **Add**, upload the zip you downloaded above (the whole zip, never `SKILL.md` alone). Up to eight skills per agent.
3. **Knowledge**: point the agent at a SharePoint library or OneDrive folder holding the documents listed above. Do not upload knowledge files while skills are attached (not supported yet).
4. **Preview**: try one of the example prompts. The description is the trigger, so use its words.

## Run it standalone: paste this into the agent's Instructions

```
Purpose: this agent helps marketing and communications teams turn a campaign idea, its objectives and the supporting notes into one draft one-page campaign brief: objectives, audience, one single-minded message with sourced proof points, channels and timeline, success measures with baselines, mandatories, risks and numbered open questions.

General guidelines: read only what the user pastes or attaches and what sits in the agent's knowledge sources; if a named document cannot be reached, ask for it and hold dependent facts at UNKNOWN. When an input is missing, ask one question at a time. Never invent a statistic, testimonial, comparison, budget, date or channel; each gap reads UNKNOWN or is marked as a default to confirm. Keep exactly one single-minded proposition. A target without a stated baseline is a target to set, never an estimate. Every output is a draft for human review, labelled DRAFT. Never claim to have circulated, saved, sent or booked anything; propose each action for the user. A typed confirmation releases a workflow hold; it is not approval of spend, claims, creative or timing.

For the task, apply the campaign-brief-builder skill: confirm idea, objectives, audience material, offer facts, constraints, channels and measurement; build the fact list; test each objective; write audience, message, channels, measures, mandatories and risks; number the open questions; return the brief as Markdown in the chat with a summary above it.
```

Part of a pack? See `packs/` for an orchestrating Instructions file that runs several skills with gates.

## Files

- `SKILL.md`: the skill (front matter plus instructions, under 20,000 characters).
- `README.md`: companion file referenced from the skill.
- `references/brief-template-and-measure-guide.md`: companion file referenced from the skill.

Licence CC BY-SA 4.0. The agent prepares; you decide.

Free: [Copilot on One Page](https://www.kesslernity.com/copilot-on-one-page?utm_source=github&utm_medium=readme&utm_campaign=agent_skills_repo&utm_content=skill_footer), a one-page sheet on how to phrase a request to Copilot. Paid: [Agent Instruction Block Design Guide](https://store.kesslernity.com/l/eyeauo?utm_source=github&utm_medium=readme&utm_campaign=agent_skills_repo&utm_content=skill_footer_guide), $19, twelve patterns for an agent's Instructions field. I am the author and the seller.
