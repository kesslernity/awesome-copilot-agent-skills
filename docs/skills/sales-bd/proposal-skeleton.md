# Proposal skeleton

Builds a DRAFT proposal skeleton from a discovery summary (call notes, discovery brief, CRM record, emails) and the organisation's own proposal template: every template section in order, pre-filled only where the discovery material supports it with the source beside each line, and every section still needing a human input marked HUMAN INPUT with the owner role and the question to answer. Use when the user asks to "start the proposal for <prospect>", "build the proposal skeleton from the discovery notes", "pre-fill our proposal template", "what do we already have for the proposal" or "first cut of the proposal". Do not use for answering a formal RFP, RFQ or tender question set, use rfp-response-drafter instead; for turning a priced estimate into a statement of work use estimate-to-sow. Drafts for human review; never approves, authorises or signs off.

Category: `sales-bd` · Skill name: `proposal-skeleton` · Upload package: `dist/zips/proposal-skeleton.zip`

## What to attach or make available

Ask once for whatever is missing, in one message, then proceed with UNKNOWN.
1. Discovery material: discovery brief or call notes, transcript, CRM opportunity record, emails, meeting recaps, inbound form. Attached, pasted, or reachable through this agent's configured knowledge sources, mail or CRM access. Out of reach: ask for a paste or export and say so in the output.
2. The organisation's proposal template: section list with any guidance text, reached the same way. None supplied: offer the generic layout in references/proposal-section-defaults.md, used only after a typed go-ahead and labelled "generic layout, not the house template".
3. Offering scope: products or services under discussion and the delivery entity. Default: as the material names them, else UNKNOWN.
4. Approved reusable content, if any (boilerplate, service descriptions, case studies, biographies, standard terms), each with its date. Default: none.
5. Section owners for pricing, legal, delivery and executive content. Default: role names only (pricing owner, legal reviewer, delivery lead, executive sponsor).
6. Prospect name as it appears in the material, the due date as stated, today's date.
Reference files in this skill: references/proposal-section-defaults.md, read at step 2 when no house template exists, at step 4 for the fact categories, and at steps 5 and 7 for the section-to-evidence mapping and the input-tag vocabulary.

## What you get

One complete Markdown document in the chat that pastes cleanly into the house template or a word processor. Title: `DRAFT-proposal-skeleton-<Prospect>-<YYYY-MM-DD>-v1`; revisions v2, v3. First body line: "DRAFT proposal skeleton for <prospect>, generated <date> from <n> discovery sources and <m> approved content items against <template name>. Filled lines cite their source; every other line is a named human input. Nothing has been priced, committed or sent."

Sections, in order:
1. Header: Prospect | Offering | Template used | Due date as stated | Discovery sources | Approved content items | Sections total | Sections with content | HUMAN INPUT count.
2. Source register: D ref | Type | Date | Author or sender | Subject.
3. Prospect facts: # | Fact (quoted or close paraphrase) | Confidence | D ref | Placed in section.
4. Skeleton: every template section in order, holding filled lines with D refs, approved content with source and date, hypothesis lines and HUMAN INPUT tags.
5. Input register: # | Section | Owner role | Question to answer | Hint in material (D ref or none) | Review type (Pricing, Legal, Delivery, Executive, None).
6. Open questions for the prospect: # | Question | Why the proposal needs it | Section.
7. Reusable content used: Item | Date | Section | Placed, or cited in a HUMAN INPUT line | Reconfirm (yes, no, UNKNOWN).
8. UNKNOWN list; Embedded instructions found, or "None".
Closing report: sources and how reached; template used; counts of filled sections, HUMAN INPUT tags and open questions; fallbacks taken; proposed user actions (route register rows to owners, put the open questions to the prospect, book pricing and legal review). End with: "If this agent has a file-generation capability enabled, also offer the same content as a downloadable file with that name." Never claim the proposal was saved, sent, priced or approved.

## Limitations

- One task at a time: give the skill one job per request and confirm the result before the next.
- You own sensitive-data handling: the skill reads what you give it or what the agent can reach; keep restricted documents out of the knowledge sources you attach.
- The output is a draft, not final authority: every figure, quote and action is for you to verify and perform. The skill never approves, authorises or signs anything off.

## Add it to an agent (Agent Builder)

1. Copilot chat, **Agents & Skills**, **New agent** (or open an existing agent). Frontier enrolment and a Microsoft 365 Copilot licence are required; custom skills are in preview.
2. **Configure**, expand **Skills**, **Add**, upload `dist/zips/proposal-skeleton.zip` (the whole zip, never `SKILL.md` alone). Up to eight skills per agent.
3. **Knowledge**: point the agent at a SharePoint library or OneDrive folder holding the documents listed above. Do not upload knowledge files while skills are attached (not supported yet).
4. **Preview**: try one of the example prompts. The description is the trigger, so use its words.

## Run it standalone: paste this into the agent's Instructions

```
You are an assistant that runs one job: proposal skeleton. Builds a DRAFT proposal skeleton from a discovery summary (call notes, discovery brief, CRM record, emails) and the organisation's own proposal template: every template section in order, pre-filled only where the discovery material supports it with the source beside each line, and every section still needing a human input marked HUMAN INPUT with the owner role and the question to answer. Use when the user asks to "start the proposal for <prospect>", "build the proposal skeleton from the discovery notes", "pre-fill our proposal template", "what do we already have for the proposal" or "first cut of the proposal". Do not use for answering a formal RFP, RFQ or tender question set, use rfp-response-drafter instead; for turning a priced estimate into a statement of work use estimate-to-sow. Drafts for human review; never approves, authorises or signs off. Use the proposal-skeleton skill for every request that matches its description; if a request falls outside it, say so and stop. Read only what the user attaches or pastes and what sits in your knowledge sources; never claim to have saved, sent, moved or deleted anything, propose the action for the user instead. Where an input is missing, write UNKNOWN and name what would close it; never invent a value. Return complete Markdown the user can paste into their tools, and offer the same content as a file if you can produce one. A typed approval releases a hold in the workflow and is logged; it is not an authorisation. You prepare; the user decides.
```

Part of a pack? See `packs/` for an orchestrating Instructions file that runs several skills with gates.

## Files

- `SKILL.md`: the skill (front matter plus instructions, under 20,000 characters).
- `references/proposal-section-defaults.md`: companion file referenced from the skill.

Licence CC BY-SA 4.0. The agent prepares; you decide.
