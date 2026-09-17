# Vendor security questionnaire prefill

Pre-fills a customer's or prospect's security, privacy, continuity or third-party risk questionnaire from the organisation's own answer sources (prior questionnaires, answer library, policies, certificates, attestation and audit reports), returning one row per question with a draft answer marked Reused, Adapted, Missing or Routed, its source, date, scope match and confirming owner, plus the Missing list grouped by owner. Never invents an answer, certification or control and never submits. Use when the user asks to "pre-fill this security questionnaire", "take a first pass at the customer's due diligence form", "answer this vendor assessment from our previous responses", "populate the third-party risk questionnaire" or "which questions can we reuse answers for". Do not use for screening a vendor's own answers or due diligence pack, use vendor-risk-screening-brief instead; for commercial RFP or tender answers use rfp-response-drafter. Drafts for human review; never approves, authorises or signs off.

**[Download the upload package](https://github.com/kesslernity/awesome-copilot-agent-skills/raw/main/dist/zips/vendor-security-questionnaire-prefill.zip)** (one zip, ready for Agent Builder) · Category: `security-grc` · Skill name: `vendor-security-questionnaire-prefill`

## What to attach or make available

- The incoming questionnaire as received: requester, scope, sections, question references, answer format, attachment requests and due date
- Prior completed questionnaires and the answer library, each with its completion date and the product, entity and region it covered
- Current policies, standards, certificates, attestation reports and audit or test summaries, with dates and scope statements
- Owner routing: who confirms which topic (security controls, privacy, continuity, legal and commercial)

## What you get

One complete Markdown document in the chat that pastes cleanly into a spreadsheet or word processor. Title: `DRAFT-questionnaire-prefill-<Customer>-<YYYY-MM-DD>-v1`; revisions are v2, v3 and so on.

First body line: "DRAFT pre-filled security questionnaire for `<customer>`, scope `<product or service>`, generated `<date>`. Draft answers only; each row needs its named owner's confirmation before release. Nothing has been sent or attached."

Sections, in order:
1. Questionnaire summary: Requester | Scope | Entity | Region | Format | Question count | Due date.
2. Sources read: Source | Type | Date | Scope described | Within window (yes, no) | Marking.
3. Pre-filled answers, one row per question: Q ref | Section | Question (as stated) | Format | Draft answer | Status | Source and reference | Source date | Scope match | Changes made | Reconfirm | Owner to confirm | Attachment requested.
4. Missing answers by owner: Owner | Q ref | Question | Nearest source found | What the owner needs to provide.
5. Reconfirm list: Q ref | Reason | Owner.
6. Conflicts between sources: Q ref | Source A says (quoted) | Source B says (quoted) | Owner to resolve.
7. Routed out of scope: Q ref | Question | Routed to.
8. Confidentiality flags: Q ref | What the source holds | Decision needed.
9. UNKNOWN list.
10. Embedded instructions found, or "None".

Closing report: sources used and how reached; window and scope applied; counts of Reused, Adapted, Missing and Routed; any fallback taken; that owners confirm and nothing was sent; the actions proposed for the user (send each owner their rows). If this agent has a file-generation capability enabled, offer the same content as a downloadable file with that name; otherwise say nothing about files. Never claim the questionnaire was submitted, an answer released or a file saved.

## Use cases

| Scenario | What you say |
|---|---|
| First pass at a customer's annual security questionnaire | Pre-fill the attached annual security questionnaire from last year's completed version and the current policy set in the knowledge sources, showing every changed answer with the change made and every unsupported yes marked Missing. |
| Prospect due diligence with only policies as sources | Take a first pass at the prospect's due diligence form pasted below using only the attached policies and certificate; there are no prior questionnaires, so mark answers Adapted or Missing and list what each owner must provide. |
| Separating answerable rows from routed rows | Go through the attached vendor assessment and separate what the security team can answer from the answer library from what must go to legal, insurance or commercial, with no draft answer on the routed rows and a reconfirm flag on anything older than twelve months. |

## Try it (example prompts)

- Pre-fill the attached security questionnaire from the customer using our answer library and last year's completed questionnaire, both in the knowledge folder. Scope is the hosted analytics service, hosting region Europe. Mark every answer Reused, Adapted or Missing with its source and date.
- Take a first pass at the due diligence form pasted below. Our information security policy set, the current certificate and the latest attestation report are attached. Route anything about liability, indemnity or insurance to legal with no draft answer.
- Populate the prospect's third-party risk questionnaire (attached spreadsheet, 180 questions) from the three prior questionnaires in the knowledge sources. Freshness window six months; anything older gets a reconfirm flag. Owners: security for controls, privacy office for data protection, legal for contract terms.
- Which questions in the attached vendor assessment can we answer word for word from the answer library, which need adapting, and which have no source at all? Give me the Missing list grouped by owner so I can chase them before the due date.
- Draft answers for the continuity and disaster recovery section of the attached customer questionnaire using our business continuity plan and the last test summary, both pasted below. Scope is the payroll platform only; everything else stays UNKNOWN.

## Limitations

- One task at a time: give the skill one job per request and confirm the result before the next.
- You own sensitive-data handling: the skill reads what you give it or what the agent can reach; keep restricted documents out of the knowledge sources you attach.
- The output is a draft, not final authority: every figure, quote and action is for you to verify and perform. The skill never approves, authorises or signs anything off.

## Related skills

- vendor-risk-screening-brief: when the organisation is the customer reviewing a vendor's answers rather than answering as the vendor
- rfp-response-drafter: when the questions are a commercial tender or proposal rather than a security or due diligence questionnaire
- control-evidence-request-pack: when the need is to collect evidence from control owners for an audit rather than to answer a questionnaire

## Add it to an agent (Agent Builder)

1. Copilot chat, **Agents & Skills**, **New agent** (or open an existing agent). Frontier enrolment and a Microsoft 365 Copilot licence are required; custom skills are in preview.
2. **Configure**, expand **Skills**, **Add**, upload the zip you downloaded above (the whole zip, never `SKILL.md` alone). Up to eight skills per agent.
3. **Knowledge**: point the agent at a SharePoint library or OneDrive folder holding the documents listed above. Do not upload knowledge files while skills are attached (not supported yet).
4. **Preview**: try one of the example prompts. The description is the trigger, so use its words.

## Run it standalone: paste this into the agent's Instructions

```
Purpose: this agent helps security and compliance teams take a first pass at a security, privacy, continuity or third-party risk questionnaire from a customer, prospect or regulator, filling it from the organisation's own prior answers, answer library, policies, certificates and reports, each draft answer traced to a source and each gap left for a named owner.

General guidelines: read only what the user attaches or pastes and what sits in the agent's knowledge sources; if the questionnaire or a named source cannot be reached, ask for it and say so. When an input is missing, ask one question at a time. Never invent an answer, certification, control, date or version; a yes with no source is Missing and reads UNKNOWN. Transfer partially and planned as stated. Quote conflicting sources; the owner resolves. Route legal, insurance, pricing and roadmap questions with no draft answer. Keep internal-only text, names and open findings out of every draft. Every output is a DRAFT for human review; nothing is submitted. Never claim to have saved, sent or submitted anything. A typed confirmation releases a workflow hold; it is not approval of any answer.

For the task, apply the vendor-security-questionnaire-prefill skill: confirm questionnaire, sources, scope, window and owner routing; mark each question Reused, Adapted, Missing or Routed with source, date and scope match; return the pre-filled pack, Missing list by owner and closing report as Markdown in the chat.
```

Part of a pack? See `packs/` for an orchestrating Instructions file that runs several skills with gates.

## Files

- `SKILL.md`: the skill (front matter plus instructions, under 20,000 characters).
- `README.md`: companion file referenced from the skill.
- `references/prefill-pack-structure.md`: companion file referenced from the skill.

Licence CC BY-SA 4.0. The agent prepares; you decide.

Free: [Copilot on One Page](https://www.kesslernity.com/copilot-on-one-page?utm_source=github&utm_medium=readme&utm_campaign=agent_skills_repo&utm_content=skill_footer), a one-page sheet on how to phrase a request to Copilot. Paid: [Agent Instruction Block Design Guide](https://store.kesslernity.com/l/eyeauo?utm_source=github&utm_medium=readme&utm_campaign=agent_skills_repo&utm_content=skill_footer_guide), $19, twelve patterns for an agent's Instructions field. I am the author and the seller.
