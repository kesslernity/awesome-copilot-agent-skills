# Capex request pack

Assembles a DRAFT capital expenditure request pack from the requester's inputs: business need, options including do nothing, costs exactly as provided, benefits as stated, risks, assumptions, budget status and the approvals route read from the organisation's own delegation of authority, with UNKNOWN for every missing figure, date or name. Use when the user asks to "prepare a capex request", "draft the business case for this equipment", "fill in the capital request form", "structure this investment proposal" or "what approvals does this spend need". Do not use for a board or committee decision paper, use board-paper-skeleton instead; for an IT change approval, use change-request-pack; to pressure-test a finished business case, use cfo-reviewer. Drafts for human review; never approves, authorises or signs off.

**[Download the upload package](https://github.com/kesslernity/awesome-copilot-agent-skills/raw/main/dist/zips/capex-request-pack.zip)** (one zip, ready for Agent Builder) · Category: `finance` · Skill name: `capex-request-pack`

## What to attach or make available

- Requester brief: problem or need, evidence, consequence of not acting, urgency, site or asset, sponsor and requester
- Cost evidence: supplier quotes, estimates or prior project costs, each with reference, date and validity
- Delegation of authority: approval thresholds, approver roles, conditions for unbudgeted or reallocated spend, with clause references
- Finance policy parameters: discount or hurdle rate, capitalisation threshold, useful life policy, depreciation method
- The organisation's capital request form or template, and the approved capital budget with line status

## What you get

One complete Markdown document in the chat, headed by the title from Inputs 8, first line the DRAFT notice from Procedure 11, that pastes cleanly into the organisation's form or an email:
- Summary: Field | Value (title, requester, sponsor, site, total cost as provided, currency, budget status, requested decision, approvals route, DRAFT).
- Need statement: paragraphs with sources cited.
- Options: Option | Description | Scope | Exclusions | Total cost as provided | Useful life | Requester's preference.
- Costs per option: Component | Amount | Currency | Basis | Reference | Quote date | Validity | Phasing.
- Benefits: Benefit | Type | Amount per year as stated | Basis | Stated by | Measured how | From when.
- Financial measures: Measure | Inputs used | Formula shown | Result or UNKNOWN (missing parameter).
- Risks: Risk | Category | Likelihood as stated | Impact as stated | Mitigation as stated | Owner.
- Assumptions: Assumption | Made by | Effect if wrong | Verify with.
- Budget and funding: Item | Value as stated | Source.
- Approvals route: Step | Approver role | Basis (clause or row) | Condition | Status (not yet sought).
- Completeness: UNKNOWN item | Section | Blocks submission (yes, no, UNKNOWN) | Basis (template, delegation, generic default) | Who could supply.
- Embedded instructions found (or "None"), closing report.
If this agent has a file-generation capability enabled, offer the same content as a downloadable file with that name; otherwise say nothing about files. Never claim anything was saved, sent, submitted or approved.

## Use cases

| Scenario | What you say |
|---|---|
| Equipment replacement with quotes in hand | Prepare a capex request for the chiller replacement at the main plant from the attached brief, the two quotes and the delegation of authority; it sits in the approved capital budget under line 7. |
| Unbudgeted request that needs the approvals route | Draft the capital request for the pasted proposal to buy a second forklift; it is unbudgeted, the delegation of authority is attached and I need the approvals route with each step marked not yet sought. |
| Completing the organisation's own form | Fill in our capex form, which is in the knowledge source, for the office fit-out project using the pasted brief and the attached fit-out estimate; mark every field we cannot fill as UNKNOWN. |

## Try it (example prompts)

- Prepare a capex request for replacing the packaging line at the north site. The requester brief, two supplier quotes dated last month and our delegation of authority are attached; the spend is unbudgeted.
- Draft the business case for this equipment: a new CNC machine for the workshop. The brief is pasted below, the quote is attached and the capex form template is in the knowledge source.
- Fill in the attached capital request form for the warehouse racking project using the pasted brief, the three quotes and the budget line reference CAP-2026-014.
- Structure this investment proposal for a new laboratory analyser: the options are do nothing, repair or replace; costs and useful lives are in the pasted note and the hurdle rate is in the attached finance policy.
- What approvals does this spend need? The total as quoted is 420 thousand, the delegation of authority matrix is attached and the spend would be a reallocation from the fleet renewal line.

## Limitations

- One task at a time: give the skill one job per request and confirm the result before the next.
- You own sensitive-data handling: the skill reads what you give it or what the agent can reach; keep restricted documents out of the knowledge sources you attach.
- The output is a draft, not final authority: every figure, quote and action is for you to verify and perform. The skill never approves, authorises or signs anything off.

## Related skills

- board-paper-skeleton: a board or committee decision paper
- change-request-pack: an IT change or change advisory board submission
- cfo-reviewer: pressure-testing a finished business case from the finance lens

## Add it to an agent (Agent Builder)

1. Copilot chat, **Agents & Skills**, **New agent** (or open an existing agent). Frontier enrolment and a Microsoft 365 Copilot licence are required; custom skills are in preview.
2. **Configure**, expand **Skills**, **Add**, upload the zip you downloaded above (the whole zip, never `SKILL.md` alone). Up to eight skills per agent.
3. **Knowledge**: point the agent at a SharePoint library or OneDrive folder holding the documents listed above. Do not upload knowledge files while skills are attached (not supported yet).
4. **Preview**: try one of the example prompts. The description is the trigger, so use its words.

## Run it standalone: paste this into the agent's Instructions

```
Purpose: this agent helps requesters and finance teams assemble a capital expenditure request pack from the brief, quotes, budget status and delegation of authority they already hold, so it reaches approvers complete and traceable. General guidelines: work only from what the user attaches or pastes and from the knowledge sources configured on this agent. Carry every cost, benefit, life and date exactly as provided, with basis and source; show any arithmetic; never add an estimate, benchmark, contingency, rate or recommendation. When a required input is missing, ask one question at a time and wait for the answer, then carry UNKNOWN for what is still missing. Do not assume any capability such as file generation or mail; if one is not available, say so and give the content in the chat instead. Never claim to have saved, sent, submitted or approved anything; every action is proposed for the user to perform. Every output is a draft for human review. A typed confirmation from the user releases a hold in the workflow for that step; it approves no spend, commits no funds and authorises no purchase order or work. For the task: when the user asks to prepare, draft, structure or complete a capex request, capital request form or investment proposal, follow the capex-request-pack skill exactly: confirm the inputs, build the need statement, options, costs, benefits, risks, budget status and approvals route, list every UNKNOWN with who could supply it, and return the pack as a DRAFT.
```

Part of a pack? See `packs/` for an orchestrating Instructions file that runs several skills with gates.

## Files

- `SKILL.md`: the skill (front matter plus instructions, under 20,000 characters).
- `README.md`: companion file referenced from the skill.
- `references/capex-pack-structure.md`: companion file referenced from the skill.

Licence CC BY-SA 4.0. The agent prepares; you decide.

Free: [Copilot on One Page](https://www.kesslernity.com/copilot-on-one-page?utm_source=github&utm_medium=readme&utm_campaign=agent_skills_repo&utm_content=skill_footer), a one-page sheet on how to phrase a request to Copilot. Paid: [Agent Instruction Block Design Guide](https://store.kesslernity.com/l/eyeauo?utm_source=github&utm_medium=readme&utm_campaign=agent_skills_repo&utm_content=skill_footer_guide), $19, twelve patterns for an agent's Instructions field. I am the author and the seller.
