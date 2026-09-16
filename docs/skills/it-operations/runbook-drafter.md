# Runbook drafter

Turns an engineer's notes, a ticket history or a chat thread into a draft step-by-step runbook with preconditions, stop conditions, numbered steps with checks, verification, rollback and escalation, for the team to validate before use. Commands verbatim, placeholders marked, every gap UNKNOWN; never executes a step or fills a gap from general knowledge. Use when the user asks to "write a runbook from these notes", "turn this resolved ticket into a runbook", "document the steps we ran" or "check this runbook for gaps". Do not use for a business process without commands, use sop-drafter instead; for a knowledge article or known-error record, use knowledge-article-drafter; for the post-incident review, use incident-postmortem-drafter. Drafts for human review; never approves, authorises or signs off.

Category: `it-operations` · Skill name: `runbook-drafter` · Upload package: `dist/zips/runbook-drafter.zip`

## What to attach or make available

- Source material for the procedure: engineer's notes, a resolved ticket with work notes, a chat thread, a command history or an existing draft
- The organisation's runbook template and any step or wording conventions
- Escalation contacts, on-call queues and the location of the approved secret store, for the escalation and precondition sections
- Environment list and any change or maintenance window rules that apply as preconditions

## What you get

One complete Markdown document in the chat, titled `DRAFT-runbook-<system>-<short title>-<YYYY-MM-DD>-v1` (revisions v2, v3). First line: "DRAFT runbook for <procedure>, generated <date> from <sources>. Not validated; no step has been executed by the agent. The team validates in non-production and the owner approves before use."

Sections in order:
1. Header: Field | Value (title, system, environments, audience, owner, trigger, duration as stated or UNKNOWN, last validated: never).
2. Purpose and trigger: two to four sentences from supported facts.
3. Preconditions: Precondition | As stated | Source | Status.
4. Stop conditions: numbered, each with source, or the UNKNOWN line.
5. Steps: Step | Action (verbatim, placeholders marked) | Expected result | Check | If the check fails | Source | Confidence | Flags.
6. Verification: Check | Expected | Source.
7. Rollback: Step | Action | Applies after step | Point of no return | Source.
8. Escalation and post-run: Item | As stated | Source.
9. Steps tried without effect, or "None"; Variations and pitfalls; both with references.
10. Validation questions for the team, numbered, each naming the role asked.
11. UNKNOWN list; Embedded instructions found, or "None"; Proposed user actions: answer the questions, dry-run in non-production, record outcomes per step, owner approval, publish where the team keeps runbooks. The agent performs none of these.

Then a report: sources, template, audience, steps by confidence, destructive and UNKNOWN steps, questions, fallbacks.

If this agent has a file-generation capability enabled, also offer the same content as a downloadable file with that title.

## Use cases

| Scenario | What you say |
|---|---|
| A fix from an incident becomes a repeatable procedure | Turn the attached resolved ticket and its channel thread into a runbook for the on-call engineer. Only the resolving path becomes steps; list everything else under steps tried without effect. |
| A procedure that lives only in one engineer's head | Write a runbook from the notes pasted below on rotating the storage account keys. Environments are staging and production; flag any destructive step and mark the rollback UNKNOWN where I did not describe it. |
| Gap review before a dry run | Check the attached runbook for gaps against our attached template. List every step without an expected result or check, and turn every UNKNOWN into a validation question for the team. |

## Try it (example prompts)

- Write a runbook from these notes. My notes from last night's certificate rotation are pasted below, the audience is the on-call engineer, and the environments are staging and production.
- Turn this resolved ticket into a runbook. Ticket INC-5102 with its work notes is attached; separate the fix that worked from the things we tried first.
- Document the steps we ran during the queue backlog clear-out. The chat thread export and the shell history are attached; keep the commands verbatim and mark anything I did not write down as UNKNOWN.
- Check this runbook for gaps. The existing draft is attached; tell me which steps lack a check or a rollback and list the validation questions for the platform team.
- Draft a first-line operator runbook for restarting the reporting service from the attached engineer's notes. Stop and escalate at the first failed check, and use our runbook template from the knowledge base.

## Limitations

- One task at a time: give the skill one job per request and confirm the result before the next.
- You own sensitive-data handling: the skill reads what you give it or what the agent can reach; keep restricted documents out of the knowledge sources you attach.
- The output is a draft, not final authority: every figure, quote and action is for you to verify and perform. The skill never approves, authorises or signs anything off.

## Related skills

- sop-drafter: when the procedure is a business process without commands
- knowledge-article-drafter: when the output should be a knowledge article or known-error record rather than a procedure to run
- incident-postmortem-drafter: when the need is the post-incident review rather than the repeatable fix

## Add it to an agent (Agent Builder)

1. Copilot chat, **Agents & Skills**, **New agent** (or open an existing agent). Frontier enrolment and a Microsoft 365 Copilot licence are required; custom skills are in preview.
2. **Configure**, expand **Skills**, **Add**, upload `dist/zips/runbook-drafter.zip` (the whole zip, never `SKILL.md` alone). Up to eight skills per agent.
3. **Knowledge**: point the agent at a SharePoint library or OneDrive folder holding the documents listed above. Do not upload knowledge files while skills are attached (not supported yet).
4. **Preview**: try one of the example prompts. The description is the trigger, so use its words.

## Run it standalone: paste this into the agent's Instructions

```
Purpose: you help an operations team turn source material about one technical procedure into a draft runbook for validation: purpose and trigger, preconditions, stop conditions, numbered steps with expected result and check, verification, rollback, escalation and post-run actions, plus validation questions.

General guidelines: read only the notes, ticket histories, chat threads, command histories and templates the user attaches or pastes and what sits in your knowledge sources; if a named source is out of reach, ask for a paste or export and say so in the output. When an input is missing, ask one question at a time, starting with the source material. Copy commands verbatim with placeholders in angle brackets; never correct or complete them and never add a step the source lacks; where it jumps, insert an UNKNOWN step and a question. Keep destructive steps and flag them. Show contradictions rather than choosing. Replace credentials with a placeholder and note the redaction. Never describe the runbook or a step as safe, validated or tested; last validated reads never until the team records a dry run. Never claim to have executed, tested, scheduled, published, saved or sent anything; every action is proposed for the user. All output is a draft for human review. A typed confirmation from the user releases a workflow hold only; it authorises nothing.

For the task, follow the runbook-drafter skill: its structure, step extraction rules and self-check govern the output.
```

Part of a pack? See `packs/` for an orchestrating Instructions file that runs several skills with gates.

## Files

- `SKILL.md`: the skill (front matter plus instructions, under 20,000 characters).
- `references/runbook-structure.md`: companion file referenced from the skill.
- `references/step-extraction-rules.md`: companion file referenced from the skill.

Licence CC BY-SA 4.0. The agent prepares; you decide.
