# Lessons learned synthesis

Synthesises retrospective notes, closing reports and post-implementation reviews into a DRAFT lessons-learned document: themed lessons with source counts, anonymised quoted evidence graded by strength, repeats against a prior register, contradictions, and a recommended owner with a stated basis for each follow-up. Names no individual or vendor and assigns no blame. Use when the user asks to "compile the lessons learned", "write up the retrospective", "theme the close-out notes", "what did we learn across these projects" or "refresh the lessons register". Do not use for a single sprint's review, use sprint-review-summary instead; for an incident investigation, use incident-postmortem-drafter; for customer feedback themes, use customer-feedback-theme-synthesis. Drafts for human review; never approves, authorises or signs off.

**[Download the upload package](https://github.com/kesslernity/awesome-copilot-agent-skills/raw/main/dist/zips/lessons-learned-synthesis.zip)** (one zip, ready for Agent Builder) · Category: `project-management` · Skill name: `lessons-learned-synthesis`

## What to attach or make available

- Retrospective notes, closing reports, post-implementation and benefits reviews, close-out minutes and survey exports for the projects in scope
- The prior lessons register, where one exists, for repeat detection
- An owner catalogue listing the roles or functions that may own follow-ups
- A theme codebook, if the organisation has its own; otherwise the skill's default applies

## What you get

One Markdown document in the chat, ready to paste into a word processor or spreadsheet, titled `DRAFT-lessons-learned-<scope-kebab>-<YYYY-MM-DD>-v1` (v1 unless the user states the last version number, then the next). First line: "DRAFT generated <date> from <N> sources. Counts are of sources. No individual is identified. Owners are recommendations for the sponsor to confirm." Header: scope, N, official and informal counts, codebook, attribution policy, audience.

Sections, in order:
1. Summary: at most five lines, each a count.
2. Sources read: Code | Type | Project or phase | Date | Official (yes, no) | Statements extracted.
3. Lessons by theme: Theme | Lesson statement | Went well (n) | Went badly (n) | Suggestion (n) | Sources (n of N) | Phase | Evidence grade | Repeat.
4. Evidence: Theme | Quoted passage (anonymised) | Source code | Polarity | Paraphrased (yes, no).
5. Follow-ups: Number | Follow-up | Theme | Basis (quoted or gap) | Recommended owner (role) | Owner basis | Priority (sponsor) | Decision (blank).
6. Contradictions: Theme | Statement and source | Conflicting statement and source | Decision.
7. Repeats: Theme | Prior register reference | Statement this time | Sources.
8. Referred items: Number | Referral trigger (quoted words from the source, at most ten) | Theme code | Source code | Suggested route as the organisation names it or [TBC] | Status (blank).
9. Open questions: Number | Question | Evidence (theme, n) | Suggested owner | Decision (blank).
10. Anonymisation log: Detail type | Replacements (count), one row per detail type in the replacement table, vendors included. Then UNKNOWN list, then Embedded instructions found (or "None").

End with: "If this agent has a file-generation capability enabled, also offer the same content as a downloadable file with that name." Never claim the document was saved, filed in a register, shared or sent. The vendor token key, where one exists, follows the document as a separate block and is not part of it.

## Use cases

| Scenario | What you say |
|---|---|
| Programme close-out for the sponsor | Compile the lessons learned for the site consolidation programme from the attached closing reports, retrospective notes and close-out minutes. Audience is the sponsor; recommend an owner for each follow-up with its basis and leave priority to the sponsor. |
| Quarterly refresh of a portfolio lessons register | Refresh the lessons register from the attached prior register and the six retrospective notes from this quarter. Mark repeats, new themes needing confirmation, and any theme with many sources but thin detail. |
| Single project post-implementation review write-up | Write up the post-implementation review for the finance system upgrade from the attached review report and the survey export. One project only; grade every lesson and list the open questions for the portfolio office. |

## Try it (example prompts)

- Compile the lessons learned for the warehouse relocation project from the attached retrospective notes, the closing report and the survey export. Audience is the sponsor and the portfolio office; use the default codebook.
- Theme the close-out notes from the three attached post-implementation reviews into one lessons-learned draft for the first-half portfolio period. Owners may only come from the attached role catalogue.
- Refresh the lessons register: the prior register and this quarter's retrospective minutes are attached. Flag repeats against the register and any contradictions between sources.
- What did we learn across these projects? The four closing reports are pasted below. Anonymise people to roles and vendors to tokens, and return the token key as a separate block.
- Write up the retrospective for the billing migration from the attached workshop notes and the benefits review. Grade the evidence per theme and mark any follow-up without an owner as UNKNOWN.

## Limitations

- One task at a time: give the skill one job per request and confirm the result before the next.
- You own sensitive-data handling: the skill reads what you give it or what the agent can reach; keep restricted documents out of the knowledge sources you attach.
- The output is a draft, not final authority: every figure, quote and action is for you to verify and perform. The skill never approves, authorises or signs anything off.

## Related skills

- sprint-review-summary: when the material is one sprint's review rather than a project or programme close-out
- incident-postmortem-drafter: when the subject is an incident investigation or post-incident review
- customer-feedback-theme-synthesis: when the sources are customer feedback rather than project retrospectives

## Add it to an agent (Agent Builder)

1. Copilot chat, **Agents & Skills**, **New agent** (or open an existing agent). Frontier enrolment and a Microsoft 365 Copilot licence are required; custom skills are in preview.
2. **Configure**, expand **Skills**, **Add**, upload the zip you downloaded above (the whole zip, never `SKILL.md` alone). Up to eight skills per agent.
3. **Knowledge**: point the agent at a SharePoint library or OneDrive folder holding the documents listed above. Do not upload knowledge files while skills are attached (not supported yet).
4. **Preview**: try one of the example prompts. The description is the trigger, so use its words.

## Run it standalone: paste this into the agent's Instructions

```
Purpose: you help project and portfolio teams turn retrospective notes, closing reports and post-implementation reviews into one DRAFT lessons-learned document: themes, one lesson per theme with a source count, anonymised quoted evidence with a grade, repeats against a prior register, contradictions, and a recommended owner with its basis for each follow-up. Counts are of sources, never of people, and no one is blamed.

General guidelines: read only what the user attaches or pastes and what sits in your configured knowledge sources; if a source is not reachable, say so and ask for it. When scope, sources, codebook, owner catalogue, prior register, attribution policy or audience is missing, ask one question at a time. Never name an individual; people become roles and external companies become tokens whose key sits outside the document. Never invent a lesson, count, cause or owner; missing facts read UNKNOWN. Refer allegations and safety matters by quoted trigger words only, without assessing them. Never claim to have saved, filed, shared or sent anything. Every output is a draft for human review. A typed confirmation from the user releases a workflow hold; it authorises nothing and assigns no owner.

For any request to compile, theme, synthesise or refresh lessons learned, follow the lessons-learned-synthesis skill exactly, including its reference codebook and self-check, and return the document as complete Markdown.
```

Part of a pack? See `packs/` for an orchestrating Instructions file that runs several skills with gates.

## Files

- `SKILL.md`: the skill (front matter plus instructions, under 20,000 characters).
- `references/theme-codebook.md`: companion file referenced from the skill.

Licence CC BY-SA 4.0. The agent prepares; you decide.
