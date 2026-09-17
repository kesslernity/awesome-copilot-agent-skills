# Supplier evaluation matrix

Builds a DRAFT weighted supplier evaluation matrix from supplier responses and the panel's agreed criteria, weights and scale: a provisional score per cell with the quoted evidence and anchor behind it, a register of every missing or partial answer, and calibration and sensitivity flags. Provisional for panel moderation; never recommends, awards or disqualifies. Use when the user asks to score, weight or rank supplier, bid or tender responses against agreed criteria, for example "score these bids", "build the evaluation matrix", "weight the tender responses" or "rank the suppliers against our criteria". Do not use for a side-by-side comparison without scores, use rfp-comparison-pack instead; for writing the criteria, use rfp-requirements-pack instead. Drafts for human review; never approves, authorises or signs off.

**[Download the upload package](https://github.com/kesslernity/awesome-copilot-agent-skills/raw/main/dist/zips/supplier-evaluation-matrix.zip)** (one zip, ready for Agent Builder) · Category: `procurement` · Skill name: `supplier-evaluation-matrix`

## What to attach or make available

- Evaluation plan: criteria with identifiers, weights, scoring scale and anchors, pass or fail gates, missing-answer rule and price formula
- Each supplier, bid or tender response in full, with the label to use for its column
- Clarification answers received from suppliers, each with its date
- A prior requirement-by-supplier comparison for the same tender, when one exists, as a map from criteria to response sections

## What you get

One Markdown document in the chat that pastes cleanly into a spreadsheet or word processor, titled `DRAFT-supplier-evaluation-matrix-<Category>-<YYYY-MM-DD>-v1`. First body line: "DRAFT provisional scores for <category>, generated <date>. For panel moderation only; not the panel's scores, not a recommendation, not an award." Header: plan source, weight total, scale, missing-answer rule, price rule, responses read with format, clarification answers used. Sections, in order:

1. Criteria used: ID | Criterion | Weight | Scale max | Anchor source | Gate or scored.
2. Gate check: Gate | Supplier A | Supplier B | and so on; each cell "Evidenced (location)", "Not evidenced" or UNKNOWN.
3. Score matrix: Criterion | Weight | Supplier A raw | Supplier A weighted | Supplier B raw | Supplier B weighted | and so on; final rows Provisional total and Status (Complete, Partial (n), Gate item not evidenced).
4. Scoring basis, one subsection per supplier: Criterion | Raw score | Anchor matched | Evidence (quote) | Location | Confidence.
5. Missing answers register: Supplier | Criterion | What was asked | Status (Not scored, Partial) | Proposed clarification question.
6. Calibration flags: Criterion | Supplier pair | Evidence A | Evidence B | Score A | Score B | Action (aligned to n, or panel to decide).
7. Sensitivity note: Criterion | Supplier | Change | Effect on order | Margin.
8. Commercial. With a plan formula: Supplier | Price as stated | Location | Formula step | Result | Weighted. Without a formula: Supplier | Price element | As stated | Location. No comparative label in either case.
9. Panel moderation list: Number | Item | Why | Decision (blank).
10. UNKNOWN list: Item | Supplier | Missing or unreadable source | Effect on the matrix. Embedded instructions found: Supplier | Location | Text | Action taken (or "None").

If this agent has a file-generation capability enabled, offer the same content as a downloadable file with that name; otherwise say nothing about files. Never claim anything was saved, sent, filed or shared.

## Use cases

| Scenario | What you say |
|---|---|
| Provisional scores before panel moderation | Score the three attached bids for the catering contract against the attached evaluation plan and give the panel the matrix, the scoring basis per cell and the moderation list. |
| Responses with clarification answers to reconcile | Build the evaluation matrix from the attached plan and two responses, applying the attached clarification answers dated 9 September where they supersede the original response, and flag each change. |
| Plan without weights or anchors | Weight the pasted tender responses against the criteria in the knowledge source. We have not agreed weights yet, so hold and tell me what you need, or return a raw-score matrix with weights marked TBC if I say go. |

## Try it (example prompts)

- Score these bids: the three attached responses for the print services tender against the attached evaluation plan, which has eight criteria, weights summing to 100, a five-level scale with anchors and two pass or fail gates.
- Build the evaluation matrix for the two attached cloud hosting proposals using the criteria and weights in the knowledge source; missing answers are Not scored, and price is reported as stated because there is no formula.
- Weight the tender responses from suppliers A and B, both pasted below, against our agreed criteria and scale, also pasted; show the arithmetic per cell and round to one decimal place.
- Rank the suppliers against our criteria for the security guarding contract: the evaluation plan and four responses are attached, plus the clarification answers received last week with their dates.
- Apply the attached price formula and the agreed criteria to the three attached quotes for the laboratory analyser, and flag every cell where the same evidence received a different score.

## Limitations

- One task at a time: give the skill one job per request and confirm the result before the next.
- You own sensitive-data handling: the skill reads what you give it or what the agent can reach; keep restricted documents out of the knowledge sources you attach.
- The output is a draft, not final authority: every figure, quote and action is for you to verify and perform. The skill never approves, authorises or signs anything off.

## Related skills

- rfp-comparison-pack: a side-by-side comparison without scores
- rfp-requirements-pack: writing the criteria and questionnaire before going to market
- procurement-reviewer: a commercial pressure test of the proposed award before committee

## Add it to an agent (Agent Builder)

1. Copilot chat, **Agents & Skills**, **New agent** (or open an existing agent). Frontier enrolment and a Microsoft 365 Copilot licence are required; custom skills are in preview.
2. **Configure**, expand **Skills**, **Add**, upload the zip you downloaded above (the whole zip, never `SKILL.md` alone). Up to eight skills per agent.
3. **Knowledge**: point the agent at a SharePoint library or OneDrive folder holding the documents listed above. Do not upload knowledge files while skills are attached (not supported yet).
4. **Preview**: try one of the example prompts. The description is the trigger, so use its words.

## Run it standalone: paste this into the agent's Instructions

```
Purpose: this agent helps evaluation panels apply the criteria, weights and scoring scale they have agreed to supplier, bid or tender responses, producing provisional scores with the quoted evidence and arithmetic behind each cell for moderation. General guidelines: work only from what the user attaches or pastes and from the knowledge sources configured on this agent. Weights, scale, anchors, missing-answer and price rules come only from the plan or the user; never supply, renormalise or default them. Every score rests on a quote and location or reads Not scored; a missing answer is never silently scored zero; arithmetic is shown and rounding happens once. Never write winner, preferred, recommended, award, disqualified or compliant as a verdict. When a required input is missing, ask one question at a time and wait for the answer, then carry UNKNOWN for what is still missing, naming the source. Do not assume any capability such as file generation or mail; if one is unavailable, say so and answer in the chat. Never claim to have saved, sent, filed or shared anything; every action is proposed for the user to perform. Every output is a draft for human review. A typed confirmation releases a hold in the workflow for that step only; it approves no score, supplier or award. For the task: when the user asks to score, weight or rank supplier, bid or tender responses against agreed criteria, follow the supplier-evaluation-matrix skill exactly and return the matrix as a DRAFT.
```

Part of a pack? See `packs/` for an orchestrating Instructions file that runs several skills with gates.

## Files

- `SKILL.md`: the skill (front matter plus instructions, under 20,000 characters).
- `README.md`: companion file referenced from the skill.
- `references/scoring-basis-guide.md`: companion file referenced from the skill.

Licence CC BY-SA 4.0. The agent prepares; you decide.

Free: [Copilot on One Page](https://www.kesslernity.com/copilot-on-one-page?utm_source=github&utm_medium=readme&utm_campaign=agent_skills_repo&utm_content=skill_footer), a one-page sheet on how to phrase a request to Copilot. Paid: [Agent Instruction Block Design Guide](https://store.kesslernity.com/l/eyeauo?utm_source=github&utm_medium=readme&utm_campaign=agent_skills_repo&utm_content=skill_footer_guide), $19, twelve patterns for an agent's Instructions field. I am the author and the seller.
