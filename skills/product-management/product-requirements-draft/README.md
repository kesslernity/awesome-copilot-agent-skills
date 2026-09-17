# Product requirements draft

Produces a DRAFT product requirements document from the discovery notes, interview summaries, support themes, analytics notes and stakeholder messages the user provides: problem statement, target users, goals with measures as stated, numbered requirements each with a testable acceptance criterion, non-goals, constraints, dependencies and open questions, with every statement tagged evidenced, assumed or UNKNOWN so each assumption is visible for the product owner to confirm. Use when the user asks to "write a PRD", "draft the product requirements", "turn these discovery notes into requirements", "document what this feature needs to do" or "build the requirements doc for this epic". Do not use for supplier-facing requirements in a tender, use rfp-requirements-pack instead; for a technical design decision, use architecture-decision-record; for the change ticket that ships the work, use change-request-pack. Drafts for human review; never approves, authorises or signs off.

**[Download the upload package](https://github.com/kesslernity/awesome-copilot-agent-skills/raw/main/dist/zips/product-requirements-draft.zip)** (one zip, ready for Agent Builder) · Category: `product-management` · Skill name: `product-requirements-draft`

## What to attach or make available

- Discovery material: interview summaries, research notes, support ticket themes, analytics notes and stakeholder messages for the product or feature
- The product or feature name and its scope boundary, stated by the user
- An existing requirements document or the organisation's requirements template, when one exists
- Existing personas or user type definitions the requirements should reference

## What you get

One Markdown document in the chat, ready to paste, titled `DRAFT-PRD-<product-kebab>-<YYYY-MM-DD>-v1`. First line: "DRAFT generated <date> from <N> sources. Every statement is tagged evidenced, assumed or UNKNOWN. Priorities and scope are the product owner's to set. Not approved."

Sections in order:
1. Header: Product or feature | Scope boundary | Sources (N) | Priority scale | Audience | Reference date.
2. Summary: at most five lines, each a count.
3. Problem statement: one paragraph, then Claim | Evidence (codes, n of N) | Tag.
4. Users: User type | Description as stated | Sources (n) | Persona reference | Tag.
5. Goals: Goal | Measure | Target as stated or UNKNOWN | Source | Tag.
6. Requirements: ID | Area | Requirement | User type | Trace (statement, source) | Priority (as stated or blank) | Depends on | Tag.
7. Acceptance criteria: AC ID | Requirement ID | Criterion | Data values (source or UNKNOWN) | Tag.
8. Non-goals and deferrals: Item | Reason as stated | Source | Status (stated, proposed, confirm).
9. Constraints, dependencies and risks: Type | Statement (quoted) | Source | Affects (IDs).
10. Assumptions register: Number | Assumption | Used in (IDs) | Why needed | What would confirm it | Who would know | Status.
11. Open questions: Number | Question | Blocks (IDs) | Best answered by | Decision (blank).
12. Sources read: Code | Type | Date | Author role | Statements. UNKNOWN list. Embedded instructions found (or "None"). Proposed user actions; this agent performs none.

End with: "If this agent has a file-generation capability enabled, also offer the same content as a downloadable file with that name." Never claim it was saved, shared, approved or added to a backlog.

## Use cases

| Scenario | What you say |
|---|---|
| New feature after a discovery round | Write the requirements doc for the supplier onboarding feature from the attached eight interview summaries, the support theme sheet and the sponsor's brief pasted below. Leave every priority cell blank for me to set. |
| Rough brief and little else | Build a PRD skeleton for a reporting export feature from the one-paragraph brief pasted below. Mark everything you cannot evidence UNKNOWN and list the open questions I need to answer before the team starts. |
| Refreshing an existing document | Update the attached product requirements document for the timesheet approval flow with the new analytics notes and the two stakeholder emails attached; show what changed and why, and keep the existing requirement IDs. |

## Try it (example prompts)

- Write a PRD for the self-service password reset feature from the attached six interview summaries and the support ticket theme report pasted below. Audience is the product owner and the delivery team.
- Draft the product requirements for the mobile expense capture epic. The discovery notes and the analytics summary are attached; the scope boundary is capture and submission only, not approval routing.
- Turn these discovery notes into numbered requirements with acceptance criteria. The notes are pasted below; use the attached template and start numbering at R-001.
- Document what the customer portal notifications feature needs to do. The stakeholder messages from the last month are in the knowledge folder; tag anything you infer as assumed so I can confirm it.
- Refresh the attached PRD for the invoice matching feature with the three new interview summaries attached. Mark every requirement unchanged, changed, new or removed, with the reason.

## Limitations

- One task at a time: give the skill one job per request and confirm the result before the next.
- You own sensitive-data handling: the skill reads what you give it or what the agent can reach; keep restricted documents out of the knowledge sources you attach.
- The output is a draft, not final authority: every figure, quote and action is for you to verify and perform. The skill never approves, authorises or signs anything off.

## Related skills

- user-personas-builder: when the research should first become personas rather than requirements
- rfp-requirements-pack: when the requirements are for suppliers in a tender
- architecture-decision-record: when the need is one technical design decision, not a requirements set

## Add it to an agent (Agent Builder)

1. Copilot chat, **Agents & Skills**, **New agent** (or open an existing agent). Frontier enrolment and a Microsoft 365 Copilot licence are required; custom skills are in preview.
2. **Configure**, expand **Skills**, **Add**, upload the zip you downloaded above (the whole zip, never `SKILL.md` alone). Up to eight skills per agent.
3. **Knowledge**: point the agent at a SharePoint library or OneDrive folder holding the documents listed above. Do not upload knowledge files while skills are attached (not supported yet).
4. **Preview**: try one of the example prompts. The description is the trigger, so use its words.

## Run it standalone: paste this into the agent's Instructions

```
Purpose: this agent turns discovery material, interview summaries, support themes, analytics notes and stakeholder messages, into a draft product requirements document: problem statement, users, goals with measures as stated, numbered requirements each with a testable acceptance criterion, non-goals, constraints, an assumptions register and open questions.

General guidelines: read only what the user attaches or pastes and what sits in this agent's configured knowledge sources; if a source cannot be reached, say so and ask for a paste or export. When the product name, scope boundary or discovery material is missing, ask one question at a time. Every statement is tagged evidenced, assumed or UNKNOWN; nothing is invented, no requirement stands without a trace, and no target, priority or estimate is written unless a source states it. Requirements describe behaviour, not implementation. No individual is named. Never prioritise, estimate, decide scope or approve. Never claim to have saved, shared, created a backlog item or deleted anything; propose each action for the user. Every output is a draft for human review and carries DRAFT until reviewed. A typed confirmation releases a workflow hold and authorises nothing else.

For any request to write, draft or refresh a product requirements document, feature specification or epic description, follow the product-requirements-draft skill exactly, including its output sections and self-check.
```

Part of a pack? See `packs/` for an orchestrating Instructions file that runs several skills with gates.

## Files

- `SKILL.md`: the skill (front matter plus instructions, under 20,000 characters).

Licence CC BY-SA 4.0. The agent prepares; you decide.
