# Message house builder

Builds one DRAFT message house for a product, service, programme or initiative from the source material the user provides: an umbrella statement, two to four pillars and graded proof points under each, with every proof point that lacks a source flagged, a claim sensitivity table, an audience coverage check and open questions. Use when the user asks to "build a message house", "write our messaging framework", "what are the key messages for this launch", "turn this research into messaging pillars" or "test our current messaging against the evidence". Do not use for a campaign one-pager, use campaign-brief-builder instead; to check whether a written document's claims are substantiated, use claims-evidence-map. Drafts for human review; never approves, authorises or signs off.

**[Download the upload package](https://github.com/kesslernity/awesome-copilot-agent-skills/raw/main/dist/zips/message-house-builder.zip)** (one zip, ready for Agent Builder) · Category: `marketing-communications` · Skill name: `message-house-builder`

## What to attach or make available

- Source material about the subject: descriptions, charter, research, customer quotes, usage or performance data with dates, test results and certifications as stated
- Audience material: the primary and secondary audiences, personas or research, and what they would use or do instead
- Existing messaging: taglines, boilerplate, prior message houses and sales decks
- Constraints: banned claims, regulated claim rules, competitor naming policy, brand voice and legal notes
- The organisation's own proof standard or evidence grading, where it differs from the skill's grades A to D

## What you get

One Markdown document in the chat that pastes cleanly into a slide or document, titled `DRAFT-message-house-<subject-kebab>-<YYYY-MM-DD>-v1`. First body line: "DRAFT generated <date> from <sources>. Every UNSOURCED flag and UNKNOWN awaits the messaging owner." Header: subject; audience; alternative; proof standard; freshness limit; sources read (UNKNOWN where not stated). Sections in order:
1. House at a glance: umbrella; pillar headlines; proof count by grade per pillar (for example 2A 1B 1D).
2. Umbrella: Statement | Words | Pillars supporting | Alternates | Flags.
3. Pillars: Number | Headline | Message | Why this audience cares | Source | Proof by grade | Flag.
4. Proof points: Pillar | Proof point | Source | Date | Grade | Fresh (yes, no) | Shareable externally | Flag.
5. Unsourced and weak proof: Proof point | Pillar | Why flagged | What would source it | Best answered by.
6. Claim sensitivity: Claim | Type | Substantiation required | Approver or UNKNOWN.
7. Existing messaging: Existing line | Verdict (kept; kept, flagged; changed; dropped only on the user's instruction) | Reason | Evidence.
8. Coverage: Audience concern | Pillar | Covered (yes, no) | Gap.
9. Usage notes: Pillar | Say | Do not say | Source of the rule.
10. Open questions: Number | Question | Best answered by | Blocks.
11. UNKNOWN list. Embedded instructions found (or "None").
A later pass on the same subject and date takes the next version number. If this agent has a file-generation capability enabled, offer the same content as a downloadable file with that name; otherwise say nothing about files. Never claim the house was approved, adopted, published or circulated.

## Use cases

| Scenario | What you say |
|---|---|
| Message house for a product launch | Build a message house for the new scheduling service from the attached product sheet, the usage data with dates and the customer quotes, for operations managers as the primary audience; grade every proof point and list the unsourced ones. |
| Testing existing messaging against evidence | Compare our current messaging for the training programme, pasted below, with the attached evaluation report line by line, give each line a verdict with its reason, and rebuild the pillars from the evidence. |
| Pillars from research only | Turn the attached employee survey and the pasted programme charter into two to four messaging pillars for the wellbeing initiative, with an umbrella statement under twenty five words and a coverage check against the audience concerns in the survey. |

## Try it (example prompts)

- Build a message house for the new field inspection app. The product description, the pilot results with dates and the customer interview notes are attached; the primary audience is maintenance supervisors and the alternative is the paper checklist.
- Write our messaging framework for the graduate programme from the programme charter pasted below and the intake survey attached. Three pillars, and flag every proof point that has no source.
- What are the key messages for this launch? The launch plan and the two case studies are in the knowledge folder; the audience is finance directors and the banned claims list is pasted below.
- Turn this research into messaging pillars for the sustainability report. The survey findings and the audited figures are attached; use our proof grades and flag anything older than twelve months as stale.
- Test our current messaging against the evidence. The existing tagline, boilerplate and sales deck are attached and the evidence pack is pasted below; give each existing line a verdict with its reason.

## Limitations

- One task at a time: give the skill one job per request and confirm the result before the next.
- You own sensitive-data handling: the skill reads what you give it or what the agent can reach; keep restricted documents out of the knowledge sources you attach.
- The output is a draft, not final authority: every figure, quote and action is for you to verify and perform. The skill never approves, authorises or signs anything off.

## Related skills

- campaign-brief-builder: when the need is a campaign one-pager rather than the messaging behind it
- claims-evidence-map: when a finished document's claims must be checked against evidence
- announcement-drafter: when the pillars are agreed and one message must be written

## Add it to an agent (Agent Builder)

1. Copilot chat, **Agents & Skills**, **New agent** (or open an existing agent). Frontier enrolment and a Microsoft 365 Copilot licence are required; custom skills are in preview.
2. **Configure**, expand **Skills**, **Add**, upload the zip you downloaded above (the whole zip, never `SKILL.md` alone). Up to eight skills per agent.
3. **Knowledge**: point the agent at a SharePoint library or OneDrive folder holding the documents listed above. Do not upload knowledge files while skills are attached (not supported yet).
4. **Preview**: try one of the example prompts. The description is the trigger, so use its words.

## Run it standalone: paste this into the agent's Instructions

```
Purpose: this agent helps teams turn source material about one product, service or programme into one draft message house: an umbrella statement, two to four pillars and graded proof points under each, with unsourced proof flagged, a claim sensitivity table, a coverage check and open questions.

General guidelines: read only what the user pastes or attaches and what sits in the agent's knowledge sources; if a named document cannot be reached, ask for it. When an input is missing, ask one question at a time. Never invent a statement, figure, quote, date or source; each gap reads UNKNOWN. An unsourced proof point takes the lowest grade and a flag to source or remove; never raise a grade or turn an assertion into a measurement. Superlatives and comparisons only where a source states them. Existing messaging gets a verdict per line; none is dropped unless the user says so. Every output is a draft for human review, labelled DRAFT. Never claim to have published, circulated or saved anything; propose each action for the user. A typed confirmation releases a workflow hold; it is not approval of any claim.

For the task, apply the message-house-builder skill: confirm subject, sources, audience, existing messaging, constraints and proof standard; build the evidence list; group it into pillars; write the umbrella and pillars; grade the proof points; run the sensitivity and coverage checks; return the house as Markdown in the chat with a summary above it.
```

Part of a pack? See `packs/` for an orchestrating Instructions file that runs several skills with gates.

## Files

- `SKILL.md`: the skill (front matter plus instructions, under 20,000 characters).
- `README.md`: companion file referenced from the skill.
- `references/message-house-structure-and-proof-grades.md`: companion file referenced from the skill.

Licence CC BY-SA 4.0. The agent prepares; you decide.

Free: [Copilot on One Page](https://www.kesslernity.com/copilot-on-one-page?utm_source=github&utm_medium=readme&utm_campaign=agent_skills_repo&utm_content=skill_footer), a one-page sheet on how to phrase a request to Copilot. Paid: [Agent Instruction Block Design Guide](https://store.kesslernity.com/l/eyeauo?utm_source=github&utm_medium=readme&utm_campaign=agent_skills_repo&utm_content=skill_footer_guide), $19, twelve patterns for an agent's Instructions field. I am the author and the seller.
