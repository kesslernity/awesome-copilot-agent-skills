# Branded deck builder

Builds a slide-by-slide presentation draft on the user's own slide template and checks every slide against written brand rules (colours with hex codes, fonts, logo placement, slide archetypes, tone, banned visuals), returning the approved outline, the DRAFT deck content and a compliance report as Markdown. Use when the user asks to "build this deck on our template", "make these slides on-brand", "check this presentation against our brand guidelines", "rebuild these slides to corporate identity (CI)" or asks for a CI-compliant or corporate-template presentation. Do not use for an accessibility review of slides, use document-accessibility-check instead. Drafts for human review; never approves, authorises or signs off.

**[Download the upload package](https://github.com/kesslernity/awesome-copilot-agent-skills/raw/main/dist/zips/branded-deck-builder.zip)** (one zip, ready for Agent Builder) · Category: `writing-communication` · Skill name: `branded-deck-builder`

## What to attach or make available

- The filled brand rules document: colours with hex codes, fonts, logo placement, slide archetypes with word limits, tone and banned visuals
- The organisation's slide template, or the layout names pasted from its slide master view
- Source material for the deck content: reports, spreadsheets, notes, charts and prior decks the slides draw on
- Existing deck versions, where the request is a rebuild, so the next version number can be used

## What you get

- <topic-slug>-outline.md: the approved outline, updated with any changes the user requested.
- <topic-slug>-deck-v1-DRAFT.md: the deck specification, one section per slide (title, layout, body, fonts and colours, logo, visuals, notes), DRAFT on the title slide. For rebuilds ask the user which version numbers already exist and use the next one; if they do not answer, use v1 and say so in the closing line.
- <topic-slug>-brand-compliance.md: the compliance report, a short summary of open MANUAL CHECK items at the top, then one table with the header row `| Slide | Colours | Fonts | Logo placement | Archetype and layout | Tone | Banned visuals | Notes |` and one row per slide, every rule area cell marked PASS, FIXED or MANUAL CHECK, and Notes holding the FIXED change or the MANUAL CHECK instruction for each cell that is not PASS.
- One closing line offering the same content as downloadable files under those names, a presentation file for the deck where the capability exists.

## Use cases

| Scenario | What you say |
|---|---|
| Executive review deck built from a report | Build an executive review deck on our template from the attached half-year report: outline first for my approval, then the slide-by-slide specification with layouts, colours and logo instructions from the attached brand rules, plus the compliance report. |
| Rebuild of off-brand slides onto the corporate template | Rebuild the attached off-template slides as a specification on our corporate template using the brand rules in the knowledge sources, keeping the content as it is, and list every rule area you fixed or could not verify from text alone. |
| Brand compliance check on a finished deck | Review the pasted slide content against the attached brand rules, slide by slide, and return the compliance table marking colours, fonts, logo placement, archetype and layout, tone and banned visuals as PASS, FIXED or MANUAL CHECK. |

## Try it (example prompts)

- Build a 12-slide quarterly business review deck on our corporate template. The brand rules document and the template are attached; the content comes from the attached quarterly report and the commentary from the finance lead pasted below.
- Make these slides on-brand: the attached draft deck was built off-template. Rebuild it as a specification on our template using the brand rules in the knowledge folder, and give me the compliance report slide by slide.
- Check this presentation against our brand guidelines. The slide text is pasted below and the brand rules document is attached; I need a per-slide table showing what passes, what you fixed and what I must check manually once built.
- Draft a 10-slide customer-facing proposal deck for the logistics project on our template. The layout names from the slide master are pasted below, the brand rules are attached, and the content comes from the attached proposal skeleton.
- Build the town hall deck on the corporate identity template from the attached script and the three attached charts. Target 15 slides; give me the outline first for approval before you write any slide.

## Limitations

- One task at a time: give the skill one job per request and confirm the result before the next.
- You own sensitive-data handling: the skill reads what you give it or what the agent can reach; keep restricted documents out of the knowledge sources you attach.
- The output is a draft, not final authority: every figure, quote and action is for you to verify and perform. The skill never approves, authorises or signs anything off.

## Related skills

- document-accessibility-check: when the slides need an accessibility review rather than brand compliance
- executive-briefing-pack: when leadership needs a pre-read document with no template requirement
- board-paper-skeleton: when the output is a formal paper seeking a resolution rather than slides

## Add it to an agent (Agent Builder)

1. Copilot chat, **Agents & Skills**, **New agent** (or open an existing agent). Frontier enrolment and a Microsoft 365 Copilot licence are required; custom skills are in preview.
2. **Configure**, expand **Skills**, **Add**, upload the zip you downloaded above (the whole zip, never `SKILL.md` alone). Up to eight skills per agent.
3. **Knowledge**: point the agent at a SharePoint library or OneDrive folder holding the documents listed above. Do not upload knowledge files while skills are attached (not supported yet).
4. **Preview**: try one of the example prompts. The description is the trigger, so use its words.

## Run it standalone: paste this into the agent's Instructions

```
Purpose: this agent helps anyone who must present on the organisation's slide template produce a presentation that follows the written brand rules on every slide, returning an approved outline, a slide-by-slide deck specification and a brand compliance report.

General guidelines: read only what the user attaches or pastes and what sits in the agent's knowledge sources; if the brand rules, the template or a named source cannot be reached, ask for it and say so in the output. When an input is missing, ask one question at a time. Write no slide until the user has typed approval of the outline. Never invent a statistic, quote, client name or source; a missing source reads [CONTENT NEEDED] and an unsourced figure reads UNKNOWN. Never claim compliance that cannot be verified from text alone; log it as MANUAL CHECK for the reviewer. Never propose changing the original template. Every output is a DRAFT for human review, labelled DRAFT on the title slide. Never claim to have saved, created, sent, moved or deleted anything; the user builds the file from the specification. A typed approval releases a workflow hold; it authorises nothing else.

For the task, apply the branded-deck-builder skill: confirm the brand rules and template by name, draft the outline, hold for approval, write the specification slide by slide, run the compliance pass against every rule area, and return the outline, deck specification and compliance report as Markdown in the chat.
```

Part of a pack? See `packs/` for an orchestrating Instructions file that runs several skills with gates.

## Files

- `SKILL.md`: the skill (front matter plus instructions, under 20,000 characters).
- `README.md`: companion file referenced from the skill.
- `references/brand-rules-template.md`: companion file referenced from the skill.

Licence CC BY-SA 4.0. The agent prepares; you decide.

Free: [Copilot on One Page](https://www.kesslernity.com/copilot-on-one-page?utm_source=github&utm_medium=readme&utm_campaign=agent_skills_repo&utm_content=skill_footer), a one-page sheet on how to phrase a request to Copilot. Paid: [Agent Instruction Block Design Guide](https://store.kesslernity.com/l/eyeauo?utm_source=github&utm_medium=readme&utm_campaign=agent_skills_repo&utm_content=skill_footer_guide), $19, twelve patterns for an agent's Instructions field. I am the author and the seller.
