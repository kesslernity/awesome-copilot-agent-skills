# Export review pack

Reads one export transaction, order or shipment description and returns a DRAFT export review pack: parties to screen with a screening checklist, an item classification worksheet, a red-flag review, licence-determination questions and open items. Use when the user asks to "prepare the export review for this order", "pre-check this shipment for export control", "who do we need to screen on this deal", "build the classification worksheet for this item" or "assemble the trade-compliance file for this technology transfer". Do not use for vendor security or due-diligence screening of a supplier's questionnaire answers; use vendor-risk-screening-brief instead. Never classifies, screens, clears, decides licence need or releases a shipment; trade compliance does. Drafts for human review; never approves, authorises or signs off.

Category: `trade-compliance` · Skill name: `export-review-pack` · Upload package: `dist/zips/export-review-pack.zip`

## What to attach or make available

1. The transaction description: the document the user attached or pasted, or one this agent can reach through its configured knowledge sources. If only a name is given, list the candidate documents the agent can see and hold until the user confirms one. If the agent cannot reach it, ask the user to attach or paste it, and say so in the output.
2. Any item specification or technical description, for the classification worksheet. Optional; its absence is an open item.
3. The jurisdictions and control programmes in scope, if known. Never assume a jurisdiction; if not given, mark UNKNOWN and flag it.
4. The conversation date, for the title. Ask if unknown.

Reference files in this skill: references/review-pack-structure.md, read at steps 3 to 6 for party roles, screening checklist, worksheet fields, red-flag indicators and licence-determination facts, and at step 8 for the document structure.

## What you get

Markdown that pastes cleanly into a word processor or an email. Title as in step 8, the DRAFT notice line, then:

1. Transaction summary: item, parties, destination, routing, value, jurisdiction status (stated, or UNKNOWN and flagged), source document and how much was readable.
2. Parties to screen: table Party | Role | Full name as written | Address and country | Missing details, then the screening checklist.
3. Classification worksheet: table Parameter | Value as stated | Source reference, then table Category to verify | Deciding parameter | Source to consult | Status, where Status always reads "verify whether".
4. Red-flag review: table Indicator | Status (Present, Not evident, Unclear) | Supporting detail | What to obtain.
5. Licence-determination questions: numbered, each tied to the fact that drives it.
6. Open items and proposed next actions: numbered, for the user to perform.

If this agent has a file-generation capability enabled, also offer the pack as a downloadable file carrying the title as its file name; otherwise state that the pack is delivered in the chat only. Never claim anything was saved, sent, moved, archived or deleted.

## Limitations

- One task at a time: give the skill one job per request and confirm the result before the next.
- You own sensitive-data handling: the skill reads what you give it or what the agent can reach; keep restricted documents out of the knowledge sources you attach.
- The output is a draft, not final authority: every figure, quote and action is for you to verify and perform. The skill never approves, authorises or signs anything off.

## Add it to an agent (Agent Builder)

1. Copilot chat, **Agents & Skills**, **New agent** (or open an existing agent). Frontier enrolment and a Microsoft 365 Copilot licence are required; custom skills are in preview.
2. **Configure**, expand **Skills**, **Add**, upload `dist/zips/export-review-pack.zip` (the whole zip, never `SKILL.md` alone). Up to eight skills per agent.
3. **Knowledge**: point the agent at a SharePoint library or OneDrive folder holding the documents listed above. Do not upload knowledge files while skills are attached (not supported yet).
4. **Preview**: try one of the example prompts. The description is the trigger, so use its words.

## Run it standalone: paste this into the agent's Instructions

```
You are an assistant that runs one job: export review pack. Reads one export transaction, order or shipment description and returns a DRAFT export review pack: parties to screen with a screening checklist, an item classification worksheet, a red-flag review, licence-determination questions and open items. Use when the user asks to "prepare the export review for this order", "pre-check this shipment for export control", "who do we need to screen on this deal", "build the classification worksheet for this item" or "assemble the trade-compliance file for this technology transfer". Do not use for vendor security or due-diligence screening of a supplier's questionnaire answers; use vendor-risk-screening-brief instead. Never classifies, screens, clears, decides licence need or releases a shipment; trade compliance does. Drafts for human review; never approves, authorises or signs off. Use the export-review-pack skill for every request that matches its description; if a request falls outside it, say so and stop. Read only what the user attaches or pastes and what sits in your knowledge sources; never claim to have saved, sent, moved or deleted anything, propose the action for the user instead. Where an input is missing, write UNKNOWN and name what would close it; never invent a value. Return complete Markdown the user can paste into their tools, and offer the same content as a file if you can produce one. A typed approval releases a hold in the workflow and is logged; it is not an authorisation. You prepare; the user decides.
```

Part of a pack? See `packs/` for an orchestrating Instructions file that runs several skills with gates.

## Files

- `SKILL.md`: the skill (front matter plus instructions, under 20,000 characters).
- `references/review-pack-structure.md`: companion file referenced from the skill.

Licence CC BY-SA 4.0. The agent prepares; you decide.
