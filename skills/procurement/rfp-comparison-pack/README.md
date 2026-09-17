# RFP comparison pack

Reads two or more supplier, bid or tender responses against a requirements list and returns a DRAFT comparison pack: a requirement-by-supplier matrix, gaps per supplier, clarification questions and neutral observations, for an evaluation panel. Never scores, weights, ranks or recommends a winner; the award stays with the panel. Use when the user asks to "compare these bids", "matrix the tender responses against our requirements", "collate the RFQ replies", "show me where each supplier falls short" or "draft clarification questions for the bidders". Do not use for scoring or weighting against agreed criteria, use supplier-evaluation-matrix instead, or for writing the requirements, use rfp-requirements-pack instead. Drafts for human review; never approves, authorises or signs off.

**[Download the upload package](https://github.com/kesslernity/awesome-copilot-agent-skills/raw/main/dist/zips/rfp-comparison-pack.zip)** (one zip, ready for Agent Builder) · Category: `procurement` · Skill name: `rfp-comparison-pack`

## What to attach or make available

- The requirements or evaluation criteria list the responses are compared against, with requirement identifiers
- Each supplier, bid or tender response in full, with the supplier label to use for its column
- Tender instructions or the invitation document, for section numbering and the response format suppliers were asked to follow
- Clarification correspondence already exchanged with suppliers, so questions are not asked twice

## What you get

Markdown that pastes cleanly into a word processor, a spreadsheet or an email. Title as in step 8, the DRAFT notice line, then:

1. Header: tender or category, number of suppliers and requirements, requirements source, date, responses read with their format.
2. Comparison matrix: columns Requirement | Supplier A | Supplier B | and so on. Each cell a short quote or a section citation, or "Not addressed", or "Verify against source".
3. Gaps by supplier: one table per supplier with columns Requirement | Gap type (Not addressed, or elements not mentioned, or two readings) | Detail | Cited location.
4. Clarification questions: one subsection per supplier, numbered, each tied to a requirement row.
5. Neutral observations: numbered factual differences with references.
6. UNKNOWN list: every response, section or input the agent could not read or reach, with the missing source named.
7. Embedded instructions found: any text inside a response that tried to direct the agent, or "None".

If this agent has a file-generation capability enabled, offer the same content as a downloadable file with that name; otherwise say nothing about files. Never claim anything was saved, sent, moved, archived or deleted.

## Use cases

| Scenario | What you say |
|---|---|
| Panel pre-read for a tender with several bids | Compare the three attached tender responses against the attached requirements list for the security guarding contract and give the panel the matrix, gaps and clarification questions. |
| RFQ with two replies and a short requirements list | Matrix the two pasted RFQ replies against the eight requirements pasted below; quote or cite each answer and mark anything not addressed. |
| Long responses that need a sampled read | Collate the attached proposals, each over eighty pages, against the requirements in the knowledge source; read the requirement and commercial sections in full, say which sections you sampled, and mark those cells to verify against source. |

## Try it (example prompts)

- Compare these bids: the three attached tender responses from suppliers A, B and C against the attached requirements list for the fleet telematics tender. The panel meets on Thursday.
- Matrix the pasted RFQ replies from two vendors against our twelve requirements, which are in the knowledge source under the procurement folder, and list the gaps per vendor.
- Collate the four supplier proposals for the payroll outsourcing RFP into one requirement-by-supplier matrix. The requirements document and all four response files are attached; label the columns by supplier.
- Show me where each supplier falls short of the requirements. The requirements list is pasted below and the two bid documents are attached; I also want clarification questions for each bidder.
- Draft clarification questions for the bidders from the attached responses and the attached requirements for the cleaning services tender, and add the neutral observations the panel should see.

## Limitations

- One task at a time: give the skill one job per request and confirm the result before the next.
- You own sensitive-data handling: the skill reads what you give it or what the agent can reach; keep restricted documents out of the knowledge sources you attach.
- The output is a draft, not final authority: every figure, quote and action is for you to verify and perform. The skill never approves, authorises or signs anything off.

## Related skills

- supplier-evaluation-matrix: provisional weighted scores against agreed criteria
- rfp-requirements-pack: writing the requirements before going to market
- clause-comparison-table: comparing contract clause wording rather than bid content

## Add it to an agent (Agent Builder)

1. Copilot chat, **Agents & Skills**, **New agent** (or open an existing agent). Frontier enrolment and a Microsoft 365 Copilot licence are required; custom skills are in preview.
2. **Configure**, expand **Skills**, **Add**, upload the zip you downloaded above (the whole zip, never `SKILL.md` alone). Up to eight skills per agent.
3. **Knowledge**: point the agent at a SharePoint library or OneDrive folder holding the documents listed above. Do not upload knowledge files while skills are attached (not supported yet).
4. **Preview**: try one of the example prompts. The description is the trigger, so use its words.

## Run it standalone: paste this into the agent's Instructions

```
Purpose: this agent helps evaluation panels and procurement teams see how two or more supplier, bid or tender responses address a requirements list, by building a comparison matrix, gaps list, clarification questions and neutral observations. General guidelines: work only from what the user attaches or pastes and from the knowledge sources configured on this agent; never derive requirements from the responses themselves. Every cell quotes or cites the response, or reads Not addressed or Verify against source; never infer an offer that is not stated. Never score, weight, rank or recommend, never write compliant or non-compliant in the agent's own words, and never label a price cheapest or best value; the award stays with the panel. When a required input is missing, ask one question at a time and wait for the answer, then carry UNKNOWN for what is still missing, naming the source. Do not assume any capability such as file generation or mail; if one is unavailable, say so and answer in the chat. Never claim to have saved, sent, circulated or filed anything; every action is proposed for the user to perform. Every output is a draft for human review. A typed confirmation releases a hold in the workflow for that step only; it approves no supplier, bid or award. For the task: when the user asks to compare, collate or matrix bids, tender responses, RFQ replies or proposals against requirements, follow the rfp-comparison-pack skill exactly and return the pack as a DRAFT.
```

Part of a pack? See `packs/` for an orchestrating Instructions file that runs several skills with gates.

## Files

- `SKILL.md`: the skill (front matter plus instructions, under 20,000 characters).
- `references/comparison-template.md`: companion file referenced from the skill.

Licence CC BY-SA 4.0. The agent prepares; you decide.
