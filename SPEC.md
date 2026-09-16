# Rewrite spec: Cowork custom skill -> declarative agent custom skill (Agent Builder / Agents Toolkit)

Target: github.com/kesslernity/awesome-copilot-agent-skills (public, CC BY-SA 4.0). Every skill must satisfy Microsoft Learn, "Custom skills in declarative agents (preview)", pages dated 2026-09-04, and the one gotcha learned on a real upload (16 Sep 2026): Agent Builder parses the front matter as STRICT YAML.

## File shape (hard rules, checked by tools/check_skills.py)
- Path: `skills/<category>/<skill-name>/SKILL.md`, optional `skills/<category>/<skill-name>/references/<file>.md`. Depth from the skill root at most 3. Only these companion types: .md .txt .json .yaml .yml .csv .docx .pdf .xlsx .pptx .png .jpg. No scripts in this repo unless a skill truly needs one (none of the rewritten skills do).
- Front matter: exactly two keys, in this order and this form:
  ```
  ---
  name: <skill-name>
  description: >-
    <one to three sentences, third person, concrete trigger conditions starting with what the skill does and then "Use when the user ...", 40 to 1,024 characters (the cap the marketplace additions below and tools/check_skills.py enforce), no colon problems because the folded block scalar (>-) makes any punctuation safe>
  ---
  ```
  `name` is kebab-case and IDENTICAL to the folder name. Nothing else in the front matter.
- Instructions (everything after the front matter): under 20,000 characters; aim for 4,000 to 9,000. No URLs. No em dashes or en dashes anywhere (use commas, colons, full stops). No brand names (no Kesslernity), no company names, no person names. British spelling.

## What changes from the Cowork version
A Cowork skill runs inside Copilot Cowork, which has 13 built-in skills (Word, Excel, PowerPoint, PDF, Email, Scheduling, Calendar, Meetings, Daily Briefing, Enterprise Search, Communications, Deep Research, Adaptive Cards), reads and writes the user's OneDrive and SharePoint files, and discovers skills from a OneDrive folder. A declarative agent custom skill runs inside a Copilot agent built in Agent Builder or the Agents Toolkit. The agent answers in chat. It reads what the user attaches or pastes and what sits in the knowledge sources configured on the agent (SharePoint sites, OneDrive folders, Graph connectors), and it may or may not have extra capabilities enabled (web search, code interpreter for producing files, email, meetings, Teams messages). A skill cannot assume any capability. Therefore:

1. Remove every reference to Cowork, to "built-in skills", to the Cowork skills folder, to `/Documents/Cowork/...` paths, to "start a new conversation so the skill is discovered", and to Cowork limits. The word Cowork must not appear.
2. Reading data. Replace "use the Email built-in skill to read the messages" with capability-neutral wording: "Read the messages the user attached or pasted, or that this agent can reach through its configured knowledge sources or mail access. If the agent cannot reach the mailbox, ask the user to paste the messages or an export, and say so in the output." Same pattern for calendar, Teams, files, SharePoint.
3. Writing outputs. Replace every "save to OneDrive at <path>" and every "create a draft in the Drafts folder" with: return the artefact in the chat as a complete Markdown document (headings, tables, numbered lists) that pastes cleanly into Word, Excel or an email; give it the file name the original skill would have used, as the document title; add one line: "If this agent has a file-generation capability enabled, also offer the same content as a downloadable file with that name." Never claim the agent saved, sent, moved, archived or deleted anything. Every action on the user's data is proposed for the user to perform; the skill produces the ready-to-paste text or the exact list of actions.
4. Keep, unchanged in meaning: purpose, trigger conditions, inputs and their defaults, the workflow logic and its order, output structure, fallbacks, the safety rules (draft-only, no invention, UNKNOWN for missing data, approval gates written as workflow holds released by the user's own typed approval and never as authorisations, no destructive actions), and the quality self-check. Tighten prose; do not pad.
5. References. Keep the `references/*.md` files, copy them with the skill, and refer to them by relative path from the skill root (`references/<file>.md`). Rewrite any Cowork or OneDrive wording inside them the same way. A reference the skill no longer needs is dropped.
6. Section skeleton for every skill (use these exact headings):
   `# <Title>` then `## Purpose`, `## When to use`, `## Inputs`, `## Procedure`, `## Output`, `## Fallbacks and edge cases`, `## Rules`, `## Self-check`.
7. The description is the trigger. Agent Builder shows the model the descriptions and it picks the skill by matching the conversation. Write it so a model can decide: what it produces, from what, and the phrases a user would say.
8. Domain skills (the engineering PFD to P&ID pack) are already in agent form: keep them as they are in substance, apply the front matter and skeleton rules, remove any wording that ties them to one pack, version, company or project ("the pack's acceptance cases", version numbers), keep every gate, UNKNOWN rule and the process-safety boundaries verbatim in meaning (the skill prepares; the engineer decides; no SIL, no sizing, no adequacy words, no permits or isolation decisions).

## Tone
Instructions to a capable colleague who has read access and cannot ask you questions. Plain, short sentences. No marketing, no adjectives about quality.

## Additions from the marketplace survey (16 Sep 2026, agentskills.io spec, anthropics/skills, Microsoft Cowork and Agent Builder docs, github/awesome-copilot, Salesforce afv-library, CAT gallery)
- Name rule, verbatim from the open spec and enforced by Microsoft's surfaces: 1 to 64 characters, lowercase a-z, 0-9 and hyphens only, no leading, trailing or consecutive hyphens, identical to the folder name.
- Description: up to 1,024 characters (the spec's cap; Cowork and Copilot Studio read the same field). Shape: what it produces, from what; then the trigger phrases a user would type, in quotes, introduced by "Use when the user asks to ..."; then one negative-scope clause, "Do not use for ..., use <sibling-skill> instead" when a sibling exists; end with "Drafts for human review; never approves, authorises or signs off." The orchestrator picks skills from descriptions alone, so the description is the trigger surface.
- Reference files: list them explicitly at the end of the Inputs section ("Reference files in this skill: references/x.md, read when ...") so the model knows they exist; one level deep, relative paths, `references/` only (no `reference/`, `examples/` or root-level extras).
- Payload discipline (CAT gallery rule, confirmed by Agent Builder showing "included files"): a skill folder contains only SKILL.md and references/. No README, CHANGELOG, meta or hidden files inside the folder; per-skill documentation lives in docs/skills/<category>/<name>.md and the machine-readable facts in catalog.json.
- Body size: the spec recommends under 5,000 tokens (about 1,500 to 2,000 words); our 4,000 to 9,000 characters sits inside it. Depth goes to references/, not into a longer body.
- Every skill's When to use section carries one "Do not use for" line naming the sibling that should fire instead, where one exists.
