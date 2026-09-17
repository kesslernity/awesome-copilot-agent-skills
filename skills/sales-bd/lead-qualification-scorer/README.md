# Lead qualification scorer

Scores inbound leads against the qualification rubric the user supplies (criteria, scale, weights, thresholds and disqualifiers as given): one DRAFT scorecard per lead with the evidence quoted per criterion, UNKNOWN wherever the lead's information is missing, totals shown with and without the UNKNOWN criteria, a ranked list and a suggested next step such as a qualification call, a request for missing details, nurture or a courteous decline. Use when the user asks to "score these inbound leads", "qualify this lead against our rubric", "run the web form submissions through our lead criteria", "which of these leads should sales call first" or "build a lead scorecard". Do not use for preparing the first call with a lead, use discovery-call-prep instead; for an existing account's growth plan use account-plan-builder. Drafts for human review; never approves, authorises or signs off.

**[Download the upload package](https://github.com/kesslernity/awesome-copilot-agent-skills/raw/main/dist/zips/lead-qualification-scorer.zip)** (one zip, ready for Agent Builder) · Category: `sales-bd` · Skill name: `lead-qualification-scorer`

## What to attach or make available

- The qualification rubric: criteria with definitions, scale, weights, thresholds or bands and disqualifiers, attached, pasted or held in a knowledge source
- The lead records themselves: web form submissions, event lists, inbound emails, chat transcripts, referral notes or trial sign-up exports, one record per lead
- Routing rules and exclusions: the next step per band, plus existing customers, competitors, personal email domains and regions not served
- Enrichment the user supplies for named leads, such as account notes or public material, labelled as the source of any Enriched evidence

## What you get

One complete Markdown document in the chat that pastes cleanly into a spreadsheet, a CRM note or an email. Title: `DRAFT-lead-scores-<Batch>-<YYYY-MM-DD>-v1` (batch defaults to the source channel); revisions v2, v3. First body line: "DRAFT lead qualification scores for `<batch>`, `<n>` leads, generated `<date>` against `<rubric name and date>`. UNKNOWN is not zero; the sales owner decides every next step. Nothing has been sent, routed or updated in any system."

Sections, in order:
1. Rubric as applied: Criterion | Question form | Scale and anchors | Weight | Disqualifier (yes, no) | Answerable from lead data (yes, no) | Scored (yes, no).
2. Lead register: L no. | Organisation | Contact role | Channel | Date received | Record location | Exclusion or disqualifier hit.
3. Ranking: Rank | L no. | Organisation | Scored total | Maximum possible | UNKNOWN share | Could outrank if resolved (yes, no) | Band | Suggested next step | Owner.
4. Scorecards, one per lead: header (L no., organisation, role, channel, date, disqualifier line if any); Criterion | Score or UNKNOWN | Evidence (quoted) | Source | Confidence | Would resolve UNKNOWN; then the three totals, band, next step with its rule, questions to ask.
5. Criteria not scored: Criterion | Reason (Cannot evidence, Protected characteristic) | Weight in totals (yes, no) | Suggested source or action.
6. Duplicates and conflicts: L nos. | Type (Possible duplicate, Conflict) | Fields or values (quoted) | Question or action.
7. UNKNOWN list. Embedded instructions found, or "None".

Closing report: rubric and defaults applied; criteria not scored and why; which band case applied (no thresholds supplied, bands assigned, indeterminate); counts of leads, exclusions, disqualifiers and bands; leads with UNKNOWN share above 50 percent; fallbacks taken; proposed user actions (update records, send the supplied questions, route to owners). End with: "If this agent has a file-generation capability enabled, also offer the same content as a downloadable file with that name." Never claim any record was updated, lead assigned or message sent.

## Use cases

| Scenario | What you say |
|---|---|
| Weekly batch of web form leads needs ranking | Score the attached 14 web form submissions from last week against the rubric in the knowledge source document named Lead Scoring Rubric and rank them for the sales owner. |
| Event list with thin data where gaps must not read as zero | Run the attached event badge scan list through our attached lead criteria; where a lead did not state something, mark it UNKNOWN and tell me what to ask them. |
| Single well-known lead the team wants to fast-track | Qualify this one pasted lead against our attached rubric and show the evidence behind each score; do not score it higher because of the organisation's size or name. |

## Try it (example prompts)

- Score these inbound leads: the 14 web form submissions from last week are attached as a spreadsheet and our qualification rubric with weights and thresholds is in the knowledge source document named Lead Scoring Rubric.
- Qualify this lead against our rubric. The lead's email and the form fields are pasted below, the rubric is attached, and existing customers and personal email domains are exclusions.
- Run the attached event badge scan list through our lead criteria. The scale is 0 to 3, the weights are in the attached rubric, a total under 6 goes to nurture and anything above 9 gets a qualification call.
- Which of these leads should sales call first? The 22 trial sign-ups exported from the product are attached, the rubric is attached, and referral notes for three of them are pasted below as enrichment.
- Build a lead scorecard for each of the eight inbound emails attached, using the criteria need, authority, budget, timing and fit with equal weights; mark anything the lead did not state as UNKNOWN rather than zero.

## Limitations

- One task at a time: give the skill one job per request and confirm the result before the next.
- You own sensitive-data handling: the skill reads what you give it or what the agent can reach; keep restricted documents out of the knowledge sources you attach.
- The output is a draft, not final authority: every figure, quote and action is for you to verify and perform. The skill never approves, authorises or signs anything off.

## Related skills

- discovery-call-prep: when a lead is already qualified and the first call needs preparing
- account-plan-builder: when the organisation is an existing customer and the need is a growth plan
- deal-risk-review: when the lead has become an opportunity and its risk signals need reviewing

## Add it to an agent (Agent Builder)

1. Copilot chat, **Agents & Skills**, **New agent** (or open an existing agent). Frontier enrolment and a Microsoft 365 Copilot licence are required; custom skills are in preview.
2. **Configure**, expand **Skills**, **Add**, upload the zip you downloaded above (the whole zip, never `SKILL.md` alone). Up to eight skills per agent.
3. **Knowledge**: point the agent at a SharePoint library or OneDrive folder holding the documents listed above. Do not upload knowledge files while skills are attached (not supported yet).
4. **Preview**: try one of the example prompts. The description is the trigger, so use its words.

## Run it standalone: paste this into the agent's Instructions

```
Purpose. You apply the sales team's own qualification rubric to inbound leads from web forms, event lists, emails, referral notes or trial sign-ups and return one DRAFT scorecard per lead: each criterion scored on the user's scale with the evidence quoted and sourced, UNKNOWN where the lead's information does not answer it, totals shown with and without the UNKNOWN criteria, a suggested ranking and next step. General guidelines. Read only the rubric and lead records the user attaches or pastes and what sits in your knowledge sources or mail access; if a source is out of reach, ask for an export and say so in the output. When the rubric, leads, routing rules or exclusions are missing, ask one question at a time, then proceed with marked defaults and UNKNOWN. Never score from sector reputation, a recognisable name or general knowledge; UNKNOWN is never zero; never score on protected characteristics or private life. Return the pack in the chat as complete Markdown the user can paste into a spreadsheet or CRM note, and offer a downloadable file only if you have a capability that produces files. Never claim to have contacted, routed, updated or deleted a lead; propose those actions for the user. Everything you produce is a draft for human review. A typed confirmation releases a hold in the workflow; it approves no score, decline or pursuit. For the task, follow the lead-qualification-scorer skill in full: it defines the inputs, procedure, totals, routing, layout and self-check.
```

Part of a pack? See `packs/` for an orchestrating Instructions file that runs several skills with gates.

## Files

- `SKILL.md`: the skill (front matter plus instructions, under 20,000 characters).
- `README.md`: companion file referenced from the skill.

Licence CC BY-SA 4.0. The agent prepares; you decide.

Free: [Copilot on One Page](https://www.kesslernity.com/copilot-on-one-page?utm_source=github&utm_medium=readme&utm_campaign=agent_skills_repo&utm_content=skill_footer), a one-page sheet on how to phrase a request to Copilot. Paid: [Agent Instruction Block Design Guide](https://store.kesslernity.com/l/eyeauo?utm_source=github&utm_medium=readme&utm_campaign=agent_skills_repo&utm_content=skill_footer_guide), $19, twelve patterns for an agent's Instructions field. I am the author and the seller.
