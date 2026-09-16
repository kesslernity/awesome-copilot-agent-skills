# Validation and review package

Runs twice in a PFD to P&ID job. Part 1, before gate G3, validates the discipline proposals for provenance, UNKNOWN handling, conflicts, prohibited content and cross-section consistency and returns results and blocking items. Part 2, before gate G5, assembles the review package, with job header, gate record, every register and proposal, consolidated UNKNOWN list, feedback log and closing statement. Use when the user asks to "validate the enrichment", "run validation before G3", "assemble the review package" or "build the G5 package". Do not use for the readiness map, use pid-tool-readiness-mapping instead; do not use to produce a missing discipline section, use the discipline skill that owns it. Drafts for human review; never approves, authorises or signs off.

Category: `engineering-pfd-to-pid` · Skill name: `validation-and-review-package` · Upload package: `dist/zips/validation-and-review-package.zip`

## What to attach or make available

1. Every section produced in the job so far, as it appears in the conversation or as the user attaches it: extraction register and unknowns, process model findings and conflicts, the four discipline sections, and for Part 2 the validation results and the readiness map.
2. The gate approval lines as typed by the user in chat, with the names as typed.
3. The list of source documents used, with revision and status as provided, and the precedence order applied.
4. Every correction the user gave during the job, quoted.
5. The date of the run as stated by the user, otherwise UNKNOWN. Documents named but not reachable in the conversation or the agent's configured knowledge sources are listed as missing; ask the user to attach or paste them and say so in the output.

## What you get

Part 1: one complete Markdown section in the chat titled "Validation results" under the job header.
- Validation results: Check | Result (pass, fail, cannot run: section missing) | Occurrences (section, row, quote).
- Blocking items: numbered.
- Then the line: "Validation complete. GATE G3: waiting for the discipline engineers to accept the enrichment. Reply APPROVE G3 with your name to continue."

Part 2: one complete Markdown document in the chat titled "Review package, <document number> Rev <revision>, DRAFT", holding the twelve parts in order, with the sections quoted in full. If any blocking item from validation remains open, say so in the first line under the title.

If this agent has a file-generation capability enabled, also offer the same content as a downloadable file with that title. Never state that the package was saved, filed, issued or sent; the user does that through the project's document control.

## Limitations

- One task at a time: give the skill one job per request and confirm the result before the next.
- You own sensitive-data handling: the skill reads what you give it or what the agent can reach; keep restricted documents out of the knowledge sources you attach.
- The output is a draft, not final authority: every figure, quote and action is for you to verify and perform. The skill never approves, authorises or signs anything off.

## Add it to an agent (Agent Builder)

1. Copilot chat, **Agents & Skills**, **New agent** (or open an existing agent). Frontier enrolment and a Microsoft 365 Copilot licence are required; custom skills are in preview.
2. **Configure**, expand **Skills**, **Add**, upload `dist/zips/validation-and-review-package.zip` (the whole zip, never `SKILL.md` alone). Up to eight skills per agent.
3. **Knowledge**: point the agent at a SharePoint library or OneDrive folder holding the documents listed above. Do not upload knowledge files while skills are attached (not supported yet).
4. **Preview**: try one of the example prompts. The description is the trigger, so use its words.

## Run it standalone: paste this into the agent's Instructions

```
You are an assistant that runs one job: validation and review package. Runs twice in a PFD to P&ID job. Part 1, before gate G3, validates the discipline proposals for provenance, UNKNOWN handling, conflicts, prohibited content and cross-section consistency and returns results and blocking items. Part 2, before gate G5, assembles the review package, with job header, gate record, every register and proposal, consolidated UNKNOWN list, feedback log and closing statement. Use when the user asks to "validate the enrichment", "run validation before G3", "assemble the review package" or "build the G5 package". Do not use for the readiness map, use pid-tool-readiness-mapping instead; do not use to produce a missing discipline section, use the discipline skill that owns it. Drafts for human review; never approves, authorises or signs off. Use the validation-and-review-package skill for every request that matches its description; if a request falls outside it, say so and stop. Read only what the user attaches or pastes and what sits in your knowledge sources; never claim to have saved, sent, moved or deleted anything, propose the action for the user instead. Where an input is missing, write UNKNOWN and name what would close it; never invent a value. Return complete Markdown the user can paste into their tools, and offer the same content as a file if you can produce one. A typed approval releases a hold in the workflow and is logged; it is not an authorisation. You prepare; the user decides.
```

Part of a pack? See `packs/` for an orchestrating Instructions file that runs several skills with gates.

## Files

- `SKILL.md`: the skill (front matter plus instructions, under 20,000 characters).

Licence CC BY-SA 4.0. The agent prepares; you decide.
