# P&ID tool readiness mapping

Maps every proposed P&ID object to the class family and attributes the project's intelligent P&ID authoring tool catalogue would need, as a readiness table with UNKNOWN wherever the project catalogue is not provided, plus connectivity readiness and import blockers. Mapping only, it never writes to the tool and never claims a class exists in the catalogue. Use when the user asks for "the readiness map", "how far is the draft from a sandbox import" or "what would block the import" after gate G3. Do not use to validate the sections or assemble the review package, use validation-and-review-package instead. Drafts for human review; never approves, authorises or signs off.

Category: `engineering-pfd-to-pid` · Skill name: `pid-tool-readiness-mapping` · Upload package: `dist/zips/pid-tool-readiness-mapping.zip`

## What to attach or make available

1. The accepted discipline proposals from the job so far: equipment, lines, instruments, safety items as stated, tags and proposed tag structures, as they appear in the conversation or as the user attaches them.
2. A project catalogue extract or class list for the tool, if the user provides one, read from what was attached or pasted or from the agent's configured knowledge sources. Without it, class names are UNKNOWN and the map records the object's generic family only (equipment, piping segment, inline component, instrument, off-page connector, note) as a placeholder for the tool administrator.
3. Any DEXPI or project data mapping document, if provided, read the same way. If a named document cannot be reached, ask the user to attach or paste it and say so in the output.

## What you get

One complete Markdown section in the chat, titled "P&ID tool readiness map" under the job header (project, document number, revision, status, mode analysis-only). Tables paste cleanly into a spreadsheet.

- Object inventory: Object | Section | Identifier | Provenance.
- Class mapping: Object | Generic family | Catalogue class (quoted) or UNKNOWN | Catalogue reference | Question if several candidates.
- Attribute readiness: Object | Attribute | Value status (sourced, placeholder, UNKNOWN) | Source.
- Connectivity readiness: Line | From resolves (yes, no, UNKNOWN) | To resolves (yes, no, UNKNOWN) | Note (unresolved ends are UNKNOWN and appear in the blockers).
- Import blockers: numbered list.
- Embedded instructions found, or "None".
- Statement of scope, as worded in the procedure.

End with "Draft for engineering review. Nothing here is approved design." If this agent has a file-generation capability enabled, also offer the same content as a downloadable file named after the section and the document number. Never state that anything was saved, sent, imported or filed.

## Limitations

- One task at a time: give the skill one job per request and confirm the result before the next.
- You own sensitive-data handling: the skill reads what you give it or what the agent can reach; keep restricted documents out of the knowledge sources you attach.
- The output is a draft, not final authority: every figure, quote and action is for you to verify and perform. The skill never approves, authorises or signs anything off.

## Add it to an agent (Agent Builder)

1. Copilot chat, **Agents & Skills**, **New agent** (or open an existing agent). Frontier enrolment and a Microsoft 365 Copilot licence are required; custom skills are in preview.
2. **Configure**, expand **Skills**, **Add**, upload `dist/zips/pid-tool-readiness-mapping.zip` (the whole zip, never `SKILL.md` alone). Up to eight skills per agent.
3. **Knowledge**: point the agent at a SharePoint library or OneDrive folder holding the documents listed above. Do not upload knowledge files while skills are attached (not supported yet).
4. **Preview**: try one of the example prompts. The description is the trigger, so use its words.

## Run it standalone: paste this into the agent's Instructions

```
You are an assistant that runs one job: p&id tool readiness mapping. Maps every proposed P&ID object to the class family and attributes the project's intelligent P&ID authoring tool catalogue would need, as a readiness table with UNKNOWN wherever the project catalogue is not provided, plus connectivity readiness and import blockers. Mapping only, it never writes to the tool and never claims a class exists in the catalogue. Use when the user asks for "the readiness map", "how far is the draft from a sandbox import" or "what would block the import" after gate G3. Do not use to validate the sections or assemble the review package, use validation-and-review-package instead. Drafts for human review; never approves, authorises or signs off. Use the pid-tool-readiness-mapping skill for every request that matches its description; if a request falls outside it, say so and stop. Read only what the user attaches or pastes and what sits in your knowledge sources; never claim to have saved, sent, moved or deleted anything, propose the action for the user instead. Where an input is missing, write UNKNOWN and name what would close it; never invent a value. Return complete Markdown the user can paste into their tools, and offer the same content as a file if you can produce one. A typed approval releases a hold in the workflow and is logged; it is not an authorisation. You prepare; the user decides.
```

Part of a pack? See `packs/` for an orchestrating Instructions file that runs several skills with gates.

## Files

- `SKILL.md`: the skill (front matter plus instructions, under 20,000 characters).

Licence CC BY-SA 4.0. The agent prepares; you decide.
