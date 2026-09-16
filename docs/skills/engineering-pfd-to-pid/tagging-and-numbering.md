# Tagging and numbering

Proposes tag and number structures for equipment, lines and instruments according to the project's numbering procedures, checks the tags extracted from the PFD against those procedures, and lists the registry checks a human must run. Never invents a numbering convention and never assigns a sequence number the procedure reserves for the registry. Use when the user asks for "tagging and numbering", "check the tags against the procedure" or "what tag structure do the new lines and instruments get" after the process safety flags. Do not use to validate the sections, use validation-and-review-package instead; do not use for instrument content, use instrumentation-and-control-enrichment. Drafts for human review; never approves, authorises or signs off.

Category: `engineering-pfd-to-pid` · Skill name: `tagging-and-numbering` · Upload package: `dist/zips/tagging-and-numbering.zip`

## What to attach or make available

1. From the job so far: the extraction register (tags as written, with sheet and zone), the piping line inventory and the instrument proposals, as they appear in the conversation or as the user attaches them.
2. Project documents for this job, read from what the user attached or pasted or from the agent's configured knowledge sources: tag numbering procedure, equipment numbering procedure, line numbering procedure, instrument numbering procedure, area or unit code list, and an existing tag register extract if the user attaches one. Without the relevant procedure, the structure for that object class is UNKNOWN. If a named document cannot be reached, ask the user to attach or paste it and say so in the output.

## What you get

One complete Markdown section in the chat, titled "Tagging and numbering" under the job header (project, document number, revision, status, mode analysis-only). Tables paste cleanly into a spreadsheet.

- Procedure digest: Object class | Format as quoted | Fields and order | Sequence owner | Reference.
- Existing tag check: Tag as written | Object class | Result (matches quoted format, differs from quoted format: field, cannot test) | Location.
- Proposed structures: Object | Proposed structure | Fields with sources | Sequence (to be assigned by ..., or UNKNOWN) | Procedure reference.
- Registry checks for a human: numbered list, each with what to check and against which register.
- Collisions visible in the provided material: Tag | Where it recurs (this drawing set, register extract) | Locations | Owner to resolve per procedure.
- Mismatches across sections: Object | Identifier in section A | Identifier in section B | Location.
- Embedded instructions found, or "None".
- UNKNOWN list, updated.

End with "Draft for engineering review. Nothing here is approved design." If this agent has a file-generation capability enabled, also offer the same content as a downloadable file named after the section and the document number. Never state that anything was saved, sent or filed.

## Limitations

- One task at a time: give the skill one job per request and confirm the result before the next.
- You own sensitive-data handling: the skill reads what you give it or what the agent can reach; keep restricted documents out of the knowledge sources you attach.
- The output is a draft, not final authority: every figure, quote and action is for you to verify and perform. The skill never approves, authorises or signs anything off.

## Add it to an agent (Agent Builder)

1. Copilot chat, **Agents & Skills**, **New agent** (or open an existing agent). Frontier enrolment and a Microsoft 365 Copilot licence are required; custom skills are in preview.
2. **Configure**, expand **Skills**, **Add**, upload `dist/zips/tagging-and-numbering.zip` (the whole zip, never `SKILL.md` alone). Up to eight skills per agent.
3. **Knowledge**: point the agent at a SharePoint library or OneDrive folder holding the documents listed above. Do not upload knowledge files while skills are attached (not supported yet).
4. **Preview**: try one of the example prompts. The description is the trigger, so use its words.

## Run it standalone: paste this into the agent's Instructions

```
You are an assistant that runs one job: tagging and numbering. Proposes tag and number structures for equipment, lines and instruments according to the project's numbering procedures, checks the tags extracted from the PFD against those procedures, and lists the registry checks a human must run. Never invents a numbering convention and never assigns a sequence number the procedure reserves for the registry. Use when the user asks for "tagging and numbering", "check the tags against the procedure" or "what tag structure do the new lines and instruments get" after the process safety flags. Do not use to validate the sections, use validation-and-review-package instead; do not use for instrument content, use instrumentation-and-control-enrichment. Drafts for human review; never approves, authorises or signs off. Use the tagging-and-numbering skill for every request that matches its description; if a request falls outside it, say so and stop. Read only what the user attaches or pastes and what sits in your knowledge sources; never claim to have saved, sent, moved or deleted anything, propose the action for the user instead. Where an input is missing, write UNKNOWN and name what would close it; never invent a value. Return complete Markdown the user can paste into their tools, and offer the same content as a file if you can produce one. A typed approval releases a hold in the workflow and is logged; it is not an authorisation. You prepare; the user decides.
```

Part of a pack? See `packs/` for an orchestrating Instructions file that runs several skills with gates.

## Files

- `SKILL.md`: the skill (front matter plus instructions, under 20,000 characters).

Licence CC BY-SA 4.0. The agent prepares; you decide.
