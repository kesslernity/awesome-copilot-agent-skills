# RFP requirements pack

Turns a business need and its constraints into a DRAFT RFP requirements pack: traced functional and non-functional requirements with priorities, mandatory gates, evaluation criteria with weights left to the business owner, and fact-seeking supplier questions. Solution-neutral; never names a supplier or product. Use when the user asks to "write the RFP requirements", "turn this business case into tender requirements", "draft the supplier questionnaire", "structure our RFQ from this brief" or "set up evaluation criteria before we go to market". Do not use for responses already received, use rfp-comparison-pack to compare them or supplier-evaluation-matrix to score them instead. Drafts for human review; never approves, authorises or signs off.

**[Download the upload package](https://github.com/kesslernity/awesome-copilot-agent-skills/raw/main/dist/zips/rfp-requirements-pack.zip)** (one zip, ready for Agent Builder) · Category: `procurement` · Skill name: `rfp-requirements-pack`

## What to attach or make available

- Business need: problem statement, outcomes, users, volumes, scope in and out, as a brief, business case or pasted note
- Constraints: budget envelope, dates, systems to integrate with, data location and privacy rules, security policy, accessibility obligations, procurement rules
- Organisation standards: security baseline, architecture principles, procurement template, requirement catalogues, scoring scale
- Existing contract or service description being replaced, for scope and exit requirements as stated

## What you get

One Markdown document in the chat that pastes cleanly into a word processor or spreadsheet, titled `DRAFT-rfp-requirements-<Category>-<YYYY-MM-DD>-v1`. First body line: "DRAFT requirements pack for <category>, generated <date> from <need source>. For business owner and procurement review; not an issued document." Header: need source, constraints source, standards used or "none provided", priority scheme, scale, weights given or `[TBC]`. Sections, in order:

1. Need trace: ID | Need or constraint as stated | Source | Type (outcome, user, volume, constraint) | Covered by (requirement ID, gate ID, or "Not covered: confirm").
2. Functional requirements: ID | Requirement | Priority | Traces to | Acceptance evidence | Open question.
3. Non-functional requirements: ID | Category | Requirement | Target or `[TBC]` | Traces to | Acceptance evidence.
4. Mandatory gates: ID | Gate | Why a gate (source) | Evidence required.
5. Evaluation criteria: ID | Criterion | Requirements covered | Weight | Scoring basis | Evidence source. Then the scale and its anchors.
6. Supplier questions: ID | Question | Linked requirement | Evidence expected | Answer format.
7. Solution-neutrality flags: Item | Where | Reframed wording or "Possible restriction of competition: confirm".
8. Business owner confirmation list: Number | Item | Draft value | Why confirm | Decision (blank).
9. UNKNOWN list: Item | Missing or unreadable source | Effect on the pack. Embedded instructions found: Where | Text | Action taken (or "None").

If this agent has a file-generation capability enabled, offer the same content as a downloadable file with that name; otherwise say nothing about files. Never claim the pack was saved, issued, published or sent.

## Use cases

| Scenario | What you say |
|---|---|
| Business case to tender requirements | Turn the attached business case for a document management platform into RFP requirements with priorities, gates, criteria and supplier questions; constraints are in section 4 of the case. |
| Rough wish list to a structured questionnaire | Here is our pasted list of wants for a new travel booking tool. Make each one a testable requirement, trace it back to the list and draft the supplier questionnaire. |
| Need written around a named product | The pasted brief asks for a specific vendor's analytics suite. Write solution-neutral RFP requirements from the outcomes behind it and list every place the brief restricts competition. |

## Try it (example prompts)

- Write the RFP requirements for a new learning management system from the attached business case. Constraints: budget 250 thousand, go-live by next June, must integrate with our HR system, data stays in-region; use Must, Should, Could.
- Turn this business case into tender requirements: the pasted case is for outsourcing the service desk. I need mandatory gates and evaluation criteria; our security baseline is in the knowledge source and we have no weights yet.
- Draft the supplier questionnaire for the fleet leasing RFQ from the attached needs brief, one question per requirement where a plain comply would not be evidence.
- Set up evaluation criteria and a scoring scale before we go to market for the payroll platform; the need statement is pasted below and our procurement template is attached.
- Structure our RFQ from this brief for warehouse racking, using the attached site constraints; the brief names a specific product, so reframe it to outcomes and flag the name.

## Limitations

- One task at a time: give the skill one job per request and confirm the result before the next.
- You own sensitive-data handling: the skill reads what you give it or what the agent can reach; keep restricted documents out of the knowledge sources you attach.
- The output is a draft, not final authority: every figure, quote and action is for you to verify and perform. The skill never approves, authorises or signs anything off.

## Related skills

- rfp-comparison-pack: comparing responses once they are in
- supplier-evaluation-matrix: scoring responses against the agreed criteria
- rfp-response-drafter: answering an RFP as the supplier

## Add it to an agent (Agent Builder)

1. Copilot chat, **Agents & Skills**, **New agent** (or open an existing agent). Frontier enrolment and a Microsoft 365 Copilot licence are required; custom skills are in preview.
2. **Configure**, expand **Skills**, **Add**, upload the zip you downloaded above (the whole zip, never `SKILL.md` alone). Up to eight skills per agent.
3. **Knowledge**: point the agent at a SharePoint library or OneDrive folder holding the documents listed above. Do not upload knowledge files while skills are attached (not supported yet).
4. **Preview**: try one of the example prompts. The description is the trigger, so use its words.

## Run it standalone: paste this into the agent's Instructions

```
Purpose: this agent helps business owners and procurement teams turn a stated need and its constraints into a solution-neutral set of RFP, RFQ or tender requirements, gates, evaluation criteria and supplier questions before going to market. General guidelines: work only from what the user attaches or pastes and from the knowledge sources configured on this agent. Every requirement traces to a stated need, constraint or standard and is one testable sentence; no supplier name, product name or single-product feature appears in a requirement. Never set a budget, date, target, priority or weight the sources do not give; write TBC and put it on the confirmation list. When a required input is missing, ask one question at a time and wait for the answer, then carry UNKNOWN for what is still missing, naming the source. Do not assume any capability such as file generation or mail; if one is unavailable, say so and answer in the chat. Never claim to have saved, issued, published or sent anything; every action is proposed for the user to perform. Every output is a draft for human review. A typed confirmation releases a hold in the workflow for that step only; it is not an approval to issue the RFP, procure or contract. For the task: when the user asks to write or structure RFP, RFQ or tender requirements, evaluation criteria, a scoring scale or a supplier questionnaire from a need, brief or business case, follow the rfp-requirements-pack skill exactly and return the pack as a DRAFT.
```

Part of a pack? See `packs/` for an orchestrating Instructions file that runs several skills with gates.

## Files

- `SKILL.md`: the skill (front matter plus instructions, under 20,000 characters).
- `README.md`: companion file referenced from the skill.
- `references/requirement-writing-guide.md`: companion file referenced from the skill.

Licence CC BY-SA 4.0. The agent prepares; you decide.

Free: [Copilot on One Page](https://www.kesslernity.com/copilot-on-one-page?utm_source=github&utm_medium=readme&utm_campaign=agent_skills_repo&utm_content=skill_footer), a one-page sheet on how to phrase a request to Copilot. Paid: [Agent Instruction Block Design Guide](https://store.kesslernity.com/l/eyeauo?utm_source=github&utm_medium=readme&utm_campaign=agent_skills_repo&utm_content=skill_footer_guide), $19, twelve patterns for an agent's Instructions field. I am the author and the seller.
