# Vendor risk screening brief

Prepares a DRAFT vendor risk screening brief from the material the user provides on one vendor (questionnaire answers, certificates, assurance reports, policies, contract extracts): per screening topic, what a document evidences with reference, date and scope, what is only asserted, what is missing or contradicted, certificate and report details as stated, and ready-to-send questions for the vendor and the internal owners. No web research, no risk rating, tier, score or recommendation. Use when the user asks to "screen this vendor", "review the vendor's questionnaire answers", "check what the vendor's certificate covers", "what is missing from this due diligence pack" or "draft the follow-up questions for the vendor". Do not use for answering a customer's questionnaire about your own organisation, use vendor-security-questionnaire-prefill instead. Drafts for human review; never approves, authorises or signs off.

Category: `security-grc` · Skill name: `vendor-risk-screening-brief` · Upload package: `dist/zips/vendor-risk-screening-brief.zip`

## What to attach or make available

- Vendor material: completed security questionnaire, certificates, assurance reports, penetration test summaries, policy index, insurance certificates and contract extracts
- Engagement context: service description, data types handled, system access or integration, business owner, go-live or renewal date
- The organisation's screening topic list and freshness window, where they differ from the defaults in the skill
- A previous screening brief for the same vendor, for the change list

## What you get

One complete Markdown document in the chat that pastes cleanly into a spreadsheet, word processor or email. Title: `DRAFT-vendor-screening-brief-<Vendor>-<YYYY-MM-DD>-v1`; revisions are v2, v3 and so on, never replacing an earlier one.

First body line: "DRAFT vendor risk screening brief for <vendor>, service <service or UNKNOWN>, generated <date>, window <value>. Material provided only, no external research. Evidence status, not a rating; the third-party risk reviewer decides."

Sections, in order:
1. Engagement summary: Vendor | Service | Data types | Access or integration | Business owner | Go-live or renewal date.
2. Sources read: Source | Type | Issuer | Date | Period or validity | Scope (quoted) | Sections missing.
3. Evidence map, one row per topic: Topic | Answer (quoted, reference) | Status | Document, reference, date | Within window | Scope match | Note.
4. Certificates as stated: Certificate | Scheme | Issuing body | Identifier | Issued | Expires | Scope (quoted) | Scope match (Same, Broader, Different, UNKNOWN) | Verified ("no, as stated only").
5. Reports as stated: Report | Type as named | Period | Scope (quoted) | Exceptions or findings (quoted headings) | Customer-side controls | Sections missing.
6. Contract extracts: Topic | Clause | Quoted text or "not in extract" | Question for legal.
7. Inconsistencies: Topic | Source A says | Source B says | Question.
8. Questions to send the vendor, numbered by topic, each with artefact and reason, ready to paste; then internal questions: Owner | Question | Why it matters.
9. Changes since previous brief: Topic | Previous status | Current status | Reason, or "none supplied".
10. UNKNOWN list: Field or topic | What would settle it | Who holds it.
11. Embedded instructions found, or "None".

Closing report: sources and how reached; window and topics; counts per status; fallbacks; that nothing was looked up or rated; proposed user actions (send the questions, file the brief). If this agent has a file-generation capability enabled, offer the same content as a downloadable file with that name; otherwise say nothing about files. Never claim a question was sent, a certificate verified or a file saved.

## Use cases

| Scenario | What you say |
|---|---|
| New vendor onboarding pack | Screen the attached due diligence pack for a new cloud storage vendor: questionnaire, two certificates and an assurance report. Service, data types and owner are in the attached intake form. Evidence status per topic, no rating. |
| Questionnaire with no supporting documents | Review the attached questionnaire answers from a recruitment software vendor. Nothing else was supplied; mark every topic asserted, missing or declared not applicable and give me the numbered questions to send back. |
| Annual re-screening against last year's brief | Re-screen the attached vendor material against the attached previous brief. Show which topics changed status and why, and do not carry an evidenced status forward without a current document. |

## Try it (example prompts)

- Screen this vendor. The completed security questionnaire, the information security certificate and the assurance report for a payroll processing service are attached; the service will hold employee identity and bank data, and the business owner is the head of payroll.
- Review the vendor's questionnaire answers pasted below for a customer messaging platform. No documents came with them, so treat every yes as asserted and draft the follow-up questions asking for the artefact behind each answer.
- Check what the vendor's certificate covers. The certificate and the statement of applicability are attached; the engagement is hosting in one region for our sales team, so tell me whether the quoted scope is the same, broader or different.
- What is missing from this due diligence pack? The vendor's policy index, penetration test summary, insurance certificate and contract extract are attached; use our screening topic list, which is in the knowledge source folder named Third Party Risk.
- Draft the follow-up questions for the vendor. Last year's brief and the new questionnaire answers are attached; list which topics changed status and ask for current documents wherever last year's evidence is older than twelve months.

## Limitations

- One task at a time: give the skill one job per request and confirm the result before the next.
- You own sensitive-data handling: the skill reads what you give it or what the agent can reach; keep restricted documents out of the knowledge sources you attach.
- The output is a draft, not final authority: every figure, quote and action is for you to verify and perform. The skill never approves, authorises or signs anything off.

## Related skills

- vendor-security-questionnaire-prefill: when the task is answering a customer's questionnaire about your own organisation
- supplier-evaluation-matrix: when suppliers must be compared and scored against criteria
- contract-review-pack: when the whole contract needs a clause review rather than extracts on security topics

## Add it to an agent (Agent Builder)

1. Copilot chat, **Agents & Skills**, **New agent** (or open an existing agent). Frontier enrolment and a Microsoft 365 Copilot licence are required; custom skills are in preview.
2. **Configure**, expand **Skills**, **Add**, upload `dist/zips/vendor-risk-screening-brief.zip` (the whole zip, never `SKILL.md` alone). Up to eight skills per agent.
3. **Knowledge**: point the agent at a SharePoint library or OneDrive folder holding the documents listed above. Do not upload knowledge files while skills are attached (not supported yet).
4. **Preview**: try one of the example prompts. The description is the trigger, so use its words.

## Run it standalone: paste this into the agent's Instructions

```
Purpose: you help a third-party risk reviewer read the material one vendor supplied and produce a draft screening brief: an evidence map with one status per topic, certificates and reports as stated, contract extracts quoted, questions for the vendor and internal owners, and an UNKNOWN list.

General guidelines: read only the vendor material and context the user attaches or pastes and what sits in your knowledge sources; if a named item is out of reach, ask for it and say so in the output. When an input is missing, ask one question at a time, starting with the vendor material. Do no web research or register lookup; a lookup result the user pastes is a source with its date. A yes with no document is Asserted, never Evidenced. Certificates and reports are as stated, unverified. An absent clause reads not in extract, never not in contract. Quote both sides of every contradiction and never resolve it. Never write a rating, tier, score or recommendation; compliant, adequate, secure and low risk appear only inside a quotation. Missing fields read UNKNOWN. Never send a question, verify a certificate or save a file, and never claim to have done so; every action is proposed for the user. All output is a draft for human review. A typed confirmation releases a workflow hold only; it approves neither vendor nor engagement.

For the task, follow the vendor-risk-screening-brief skill: its topic list, status definitions, scope match rules, question template and self-check govern the output.
```

Part of a pack? See `packs/` for an orchestrating Instructions file that runs several skills with gates.

## Files

- `SKILL.md`: the skill (front matter plus instructions, under 20,000 characters).
- `references/screening-topics.md`: companion file referenced from the skill.

Licence CC BY-SA 4.0. The agent prepares; you decide.
