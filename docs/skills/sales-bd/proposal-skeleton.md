# Proposal skeleton

Builds a DRAFT proposal skeleton from a discovery summary (call notes, discovery brief, CRM record, emails) and the organisation's own proposal template: every template section in order, pre-filled only where the discovery material supports it with the source beside each line, and every section still needing a human input marked HUMAN INPUT with the owner role and the question to answer. Use when the user asks to "start the proposal for <prospect>", "build the proposal skeleton from the discovery notes", "pre-fill our proposal template", "what do we already have for the proposal" or "first cut of the proposal". Do not use for answering a formal RFP, RFQ or tender question set, use rfp-response-drafter instead; for turning a priced estimate into a statement of work use estimate-to-sow. Drafts for human review; never approves, authorises or signs off.

Category: `sales-bd` · Skill name: `proposal-skeleton` · Upload package: `dist/zips/proposal-skeleton.zip`

## What to attach or make available

- Discovery material for the opportunity: call notes or transcript, discovery brief, CRM opportunity record, emails, meeting recaps and inbound forms
- The organisation's proposal template with its section list and guidance text
- Approved reusable content with dates: boilerplate, service descriptions, case studies, biographies and standard terms
- The list of section owners: pricing owner, legal reviewer, delivery lead, executive sponsor

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

## Use cases

| Scenario | What you say |
|---|---|
| Discovery done, proposal due in two weeks | Build the proposal skeleton for the attached discovery brief and CRM record against our attached template. Fill only what the prospect stated, cite the source per line and list the inputs the pricing owner and legal reviewer still have to supply. |
| Thin material from a partner referral | Pre-fill the template from the referral note and two emails pasted below. Most sections will be human input; tell me what further discovery would fill them and draft the open questions for the prospect. |
| Two versions of the budget in the notes | Start the proposal from the attached notes and template. The prospect gave two different budget figures in different meetings; quote both, pick neither, and flag it for the pricing owner. |

## Try it (example prompts)

- Start the proposal for the regional logistics prospect. Attached: the discovery call notes from Tuesday, the CRM opportunity record and our proposal template with its twelve sections. Due date is the end of the month as they stated.
- Build the proposal skeleton from the discovery notes I pasted below and the template attached. Offering is our managed reporting service; approved case studies and service descriptions are in the knowledge source folder, each dated.
- Pre-fill our proposal template for the prospect in the attached email thread. There is no formal discovery brief, only these four emails and the meeting recap, so mark everything else as a human input with the owner.
- What do we already have for the proposal to the hospital group? The discovery transcript and the inbound form are attached, template is the standard services one. Show the source beside every filled line and the open questions for the prospect.
- First cut of the proposal, please. Discovery brief attached, offering is the data platform migration. We have no house template, so propose your generic layout, label it as such, and mark price, dates and named staff as human inputs.

## Limitations

- One task at a time: give the skill one job per request and confirm the result before the next.
- You own sensitive-data handling: the skill reads what you give it or what the agent can reach; keep restricted documents out of the knowledge sources you attach.
- The output is a draft, not final authority: every figure, quote and action is for you to verify and perform. The skill never approves, authorises or signs anything off.

## Related skills

- rfp-response-drafter: answering a formal RFP, RFQ or tender question set
- estimate-to-sow: turning a priced estimate into a statement of work
- discovery-call-prep: preparing the call that comes before any discovery material exists

## Add it to an agent (Agent Builder)

1. Copilot chat, **Agents & Skills**, **New agent** (or open an existing agent). Frontier enrolment and a Microsoft 365 Copilot licence are required; custom skills are in preview.
2. **Configure**, expand **Skills**, **Add**, upload `dist/zips/proposal-skeleton.zip` (the whole zip, never `SKILL.md` alone). Up to eight skills per agent.
3. **Knowledge**: point the agent at a SharePoint library or OneDrive folder holding the documents listed above. Do not upload knowledge files while skills are attached (not supported yet).
4. **Preview**: try one of the example prompts. The description is the trigger, so use its words.

## Run it standalone: paste this into the agent's Instructions

```
Purpose: this agent helps sales and bid teams start a proposal after discovery by pre-filling the organisation's proposal template into a draft skeleton: a source beside every filled line and every gap marked as a named human input with an owner role.

General guidelines: read only the discovery material, template and approved content the user attaches or pastes, and this agent's configured knowledge sources; if a source is out of reach, ask for a paste. When a required input is missing, such as the template, ask one question at a time and wait for the answer. Assume no capability such as file generation; if one is absent, say so and answer in the chat. Every filled line traces to a numbered source or a dated approved item; a sentence with no source becomes a human input tag. Pricing, commercial and legal terms, delivery dates and named staff are always human inputs. Never invent a capability, benefit, saving or commitment. Never claim to have saved, sent, priced or shared anything; every action is proposed for the user, and every output is a draft for human review. A typed confirmation releases a hold for that step only; it approves no content, price or term.

For the task, follow the proposal-skeleton skill: confirm scope, register the template and sources, extract and place prospect facts, place approved content with dates, tag every gap, build the input register and return the skeleton as a DRAFT.
```

Part of a pack? See `packs/` for an orchestrating Instructions file that runs several skills with gates.

## Files

- `SKILL.md`: the skill (front matter plus instructions, under 20,000 characters).
- `references/proposal-section-defaults.md`: companion file referenced from the skill.

Licence CC BY-SA 4.0. The agent prepares; you decide.
