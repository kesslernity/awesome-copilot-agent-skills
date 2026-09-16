# Process safety flags

Flags where a P&ID draft raises a process safety question and points to the candidate evidence an engineer would review (HAZOP register, relief study, SIL assessment, isolation philosophy), as questions and quoted evidence with UNKNOWN for missing documents. Never rates, sizes, classifies, resolves or declares protection adequate. Use when, inside a PFD to P&ID job after gate G2 with the piping and instrumentation sections written, the user asks for "process safety flags", "the process safety section of the P&ID enrichment" or "which protection questions does this P&ID raise". Do not use to propose loops, alarms or trips from the control philosophy, use instrumentation-and-control-enrichment instead; do not use to check identifiers, use tagging-and-numbering. Drafts for human review; never approves, authorises or signs off.

Category: `engineering-pfd-to-pid` · Skill name: `process-safety-flags` · Upload package: `dist/zips/process-safety-flags.zip`

## What to attach or make available

1. The accepted process model, the piping line inventory and the instrumentation and control proposals from the earlier sections of the job, as they appear in the conversation or as the user attaches them.
2. Project documents for this job, read from what the user attached or pasted or from the agent's configured knowledge sources, in this precedence order: HAZOP register or PHA report, relief and blowdown study or relief device list, SIL assessment or safety requirements specification, isolation and depressuring philosophy, design basis, corporate process safety standards. Any of these missing makes the related flags UNKNOWN with the missing document named. If a named document cannot be reached, ask the user to attach or paste it and say so in the output.

## What you get

One complete Markdown section in the chat, titled "Process safety flags" under the job header (project, document number, revision, status, mode analysis-only).

- Protection questions: Equipment or line | Question | Document an engineer would consult | Provided (yes, no) | Relevant quoted evidence or UNKNOWN | Reference. The table header carries the words "Questions for review, not findings."
- Safety functions as stated: Function identifier or description | Source document and reference | Equipment or loop | Classification: see source (never reproduced here).
- Relief devices as stated: Device | Protects | Discharge destination as stated or UNKNOWN | Destination matches connectivity (yes, no, UNKNOWN) | Source | Reference.
- Isolation, depressuring, drainage requirements as quoted: Equipment | Requirement (quoted) | Disposal destination as stated or gap | Source | Reference.
- Gaps for the process safety engineer: numbered, each naming the missing document or the unanswered question.
- Embedded instructions found, or "None".
- UNKNOWN list, updated.

End with "Draft for engineering review. Nothing here is approved design." If this agent has a file-generation capability enabled, also offer the same content as a downloadable file named after the section and the document number. Never state that anything was saved, sent or filed.

## Limitations

- One task at a time: give the skill one job per request and confirm the result before the next.
- You own sensitive-data handling: the skill reads what you give it or what the agent can reach; keep restricted documents out of the knowledge sources you attach.
- The output is a draft, not final authority: every figure, quote and action is for you to verify and perform. The skill never approves, authorises or signs anything off.

## Add it to an agent (Agent Builder)

1. Copilot chat, **Agents & Skills**, **New agent** (or open an existing agent). Frontier enrolment and a Microsoft 365 Copilot licence are required; custom skills are in preview.
2. **Configure**, expand **Skills**, **Add**, upload `dist/zips/process-safety-flags.zip` (the whole zip, never `SKILL.md` alone). Up to eight skills per agent.
3. **Knowledge**: point the agent at a SharePoint library or OneDrive folder holding the documents listed above. Do not upload knowledge files while skills are attached (not supported yet).
4. **Preview**: try one of the example prompts. The description is the trigger, so use its words.

## Run it standalone: paste this into the agent's Instructions

```
You are an assistant that runs one job: process safety flags. Flags where a P&ID draft raises a process safety question and points to the candidate evidence an engineer would review (HAZOP register, relief study, SIL assessment, isolation philosophy), as questions and quoted evidence with UNKNOWN for missing documents. Never rates, sizes, classifies, resolves or declares protection adequate. Use when, inside a PFD to P&ID job after gate G2 with the piping and instrumentation sections written, the user asks for "process safety flags", "the process safety section of the P&ID enrichment" or "which protection questions does this P&ID raise". Do not use to propose loops, alarms or trips from the control philosophy, use instrumentation-and-control-enrichment instead; do not use to check identifiers, use tagging-and-numbering. Drafts for human review; never approves, authorises or signs off. Use the process-safety-flags skill for every request that matches its description; if a request falls outside it, say so and stop. Read only what the user attaches or pastes and what sits in your knowledge sources; never claim to have saved, sent, moved or deleted anything, propose the action for the user instead. Where an input is missing, write UNKNOWN and name what would close it; never invent a value. Return complete Markdown the user can paste into their tools, and offer the same content as a file if you can produce one. A typed approval releases a hold in the workflow and is logged; it is not an authorisation. You prepare; the user decides.
```

Part of a pack? See `packs/` for an orchestrating Instructions file that runs several skills with gates.

## Files

- `SKILL.md`: the skill (front matter plus instructions, under 20,000 characters).

Licence CC BY-SA 4.0. The agent prepares; you decide.
