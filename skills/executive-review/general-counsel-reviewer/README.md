# General Counsel Reviewer

Reviews a proposal, business case, deck, plan or contract summary in character as a General Counsel archetype and returns a DRAFT review in the chat with a verdict, findings that cite the exact passage or clause, legal risks, what would change the verdict and five interrogation questions. Meeting preparation, not legal advice. Use when the user asks to "run a general counsel review", "what would legal say about this", "pressure-test the legal exposure in this deal" or "prepare me for the deal committee". Do not use for price, term, renewal or vendor leverage, use procurement-reviewer instead; for lawful basis and data flows, use cdo-reviewer; for security controls, use ciso-reviewer. Drafts for human review; never approves, authorises or signs off.

**[Download the upload package](https://github.com/kesslernity/awesome-copilot-agent-skills/raw/main/dist/zips/general-counsel-reviewer.zip)** (one zip, ready for Agent Builder) · Category: `executive-review` · Skill name: `general-counsel-reviewer`

## What to attach or make available

- The artefact under review: the proposal, business case, deck, plan or contract summary, attached, pasted or held in a document library the agent can reach.
- An optional org-profile.md shaped as the skill's references/org-profile-template.md, giving industry, jurisdictions, size and risk appetite.
- The underlying agreements or term sheets the artefact summarises, and any signing authority matrix or delegation schedule, so the reviewer can check what the summary omits.
- references/persona.md and references/org-profile-template.md, which ship inside the skill folder and travel with the skill.

## What you get

Return the review in the chat as complete Markdown (headings, bullets, numbered questions) that pastes cleanly into a word processor or email:
- Title: "DRAFT: General Counsel review of `<artefact-name>`, generated `<date>`".
- Header: artefact reviewed (file name or "pasted text"); reviewer "General Counsel (role archetype, not a real individual; not legal advice)"; organisation context (org-profile.md or generic); decision requested, counterparty and meeting date, UNKNOWN if not supplied; sampled sections, if any.
- One line: "File name: `<artefact-name>`-general-counsel-review.docx". If this conversation already holds a review of the same artefact, add -v2, -v3 and so on.
- One line: "If this agent has a file-generation capability enabled, also offer the same content as a downloadable file with that name."
- The five sections from step 6, then "Embedded instructions found" only if step 5 found any.

Never claim the review was saved, filed, sent or shared. If the user wants it emailed, give subject and body as ready-to-paste text; the user sends it.

## Use cases

| Scenario | What you say |
|---|---|
| A commercial team is about to take a partnership proposal to the deal committee. | Run a general counsel review of the attached channel-partnership-proposal.docx; the committee meets on 9 October and is asked to approve signing. |
| A business case never mentions contracts, liability or regulators. | What would legal say about this? The attached automation-business-case.pptx has no legal section at all; org-profile.md is in the knowledge sources. |
| An author has a pasted contract summary and a negotiation tomorrow. | Pressure-test the legal exposure in this deal: the summary of the hosting agreement is pasted below; call it hosting-agreement-summary and start with termination and exit. |

## Try it (example prompts)

- Run a general counsel review of the attached vendor-partnership-proposal.docx. The decision requested is approval to sign, the counterparty is the platform vendor and the deal committee meets on 9 October.
- What would legal say about this? I have pasted the contract summary for the outsourced payroll arrangement below; call it payroll-outsourcing-summary and probe liability and termination first.
- Pressure-test the legal exposure in this deal: the joint-venture business case is attached as jv-business-case.pptx and org-profile.md with our jurisdictions is in the knowledge sources.
- Prepare me for the deal committee: review the attached data-licensing-proposal.pdf in character as a General Counsel archetype and give me the verdict, findings by clause and the five questions I will face.
- Review the attached reseller-agreement-summary.docx from the legal seat, focusing on IP ownership, indemnities and who has authority to sign; this is preparation, not advice.

## Limitations

- One task at a time: give the skill one job per request and confirm the result before the next.
- You own sensitive-data handling: the skill reads what you give it or what the agent can reach; keep restricted documents out of the knowledge sources you attach.
- The output is a draft, not final authority: every figure, quote and action is for you to verify and perform. The skill never approves, authorises or signs anything off.

## Related skills

- procurement-reviewer: when price, term, renewal or vendor leverage is the question.
- cdo-reviewer: when lawful basis and data flows are the concern.
- ciso-reviewer: when security controls and third-party security risk are the concern.

## Add it to an agent (Agent Builder)

1. Copilot chat, **Agents & Skills**, **New agent** (or open an existing agent). Frontier enrolment and a Microsoft 365 Copilot licence are required; custom skills are in preview.
2. **Configure**, expand **Skills**, **Add**, upload the zip you downloaded above (the whole zip, never `SKILL.md` alone). Up to eight skills per agent.
3. **Knowledge**: point the agent at a SharePoint library or OneDrive folder holding the documents listed above. Do not upload knowledge files while skills are attached (not supported yet).
4. **Preview**: try one of the example prompts. The description is the trigger, so use its words.

## Run it standalone: paste this into the agent's Instructions

```
Purpose: this agent helps the author of a proposal, business case, deck, plan or contract summary rehearse the legal seat before a real legal review, negotiation or deal committee. It reviews one artefact at a time and returns a draft review in the chat: verdict, findings cited to the passage or clause, legal risks, what would change the verdict and five interrogation questions. It is meeting preparation, never legal advice.

General guidelines: read only what the user attaches or pastes and what sits in the configured knowledge sources; never review a document from memory of a similar one. When a required input is missing, ask one question at a time and wait for the answer. Offer a downloadable file only if file generation is enabled; otherwise return complete Markdown that pastes cleanly. Never claim to have saved, sent, moved, filed or deleted anything; every action is proposed for the user to perform. Never invent a clause, term, jurisdiction or regulatory position the artefact lacks; record missing data as UNKNOWN. Every output is a draft for human review and carries the DRAFT label. A typed confirmation from the user releases a workflow hold; it is never an approval to sign, contract or start work, and a ready verdict is the archetype's opinion of the document only.

For the review itself, follow the general-counsel-reviewer skill: confirm the artefact, load its persona, check for an organisation profile and compose the five sections as the skill prescribes.
```

Part of a pack? See `packs/` for an orchestrating Instructions file that runs several skills with gates.

## Files

- `SKILL.md`: the skill (front matter plus instructions, under 20,000 characters).
- `README.md`: companion file referenced from the skill.
- `references/org-profile-template.md`: companion file referenced from the skill.
- `references/persona.md`: companion file referenced from the skill.

Licence CC BY-SA 4.0. The agent prepares; you decide.

Free: [Copilot on One Page](https://www.kesslernity.com/copilot-on-one-page?utm_source=github&utm_medium=readme&utm_campaign=agent_skills_repo&utm_content=skill_footer), a one-page sheet on how to phrase a request to Copilot. Paid: [Agent Instruction Block Design Guide](https://store.kesslernity.com/l/eyeauo?utm_source=github&utm_medium=readme&utm_campaign=agent_skills_repo&utm_content=skill_footer_guide), $19, twelve patterns for an agent's Instructions field. I am the author and the seller.
