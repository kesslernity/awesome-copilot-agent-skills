# FAQ builder

Turns a set of questions (form exports, helpdesk logs, meeting Q and A, chat threads, a plain list) plus the source documents the user supplies into a DRAFT FAQ grouped by theme: every answer quoted or paraphrased from a named source with a reference, verbatim quotes for dates, figures, eligibility and obligations, UNKNOWN where the sources are silent, a source register with precedence, a conflicts table and a routing list of unanswered questions to owners. Use when the user asks to "build an FAQ from these documents", "answer these questions from the policy", "turn the Q and A into an FAQ page", "group these questions and answer them from the guide" or "what do our documents say about these questions". Do not use for the manager FAQ of a changed HR policy, use policy-change-briefing instead; for checking whether a document's own claims are evidenced, use claims-evidence-map. Drafts for human review; never approves, authorises or signs off.

Category: `marketing-communications` · Skill name: `faq-builder` · Upload package: `dist/zips/faq-builder.zip`

## What to attach or make available

- The questions: a plain list, form export, helpdesk extract, chat thread or meeting Q and A, with asker role, frequency and date where known
- The source documents that should answer them: policies, guides, announcements, contracts, specifications and procedures, each with title, version and date
- The precedence order to apply when sources disagree, or confirmation that the newest current version wins
- The owner per theme or document who receives unanswered questions
- Any existing theme scheme, glossary of defined terms or house style for the published FAQ

## What you get

One complete Markdown document in the chat, titled `DRAFT-faq-<topic>-<YYYY-MM-DD>-v1` (revisions v2, v3). First line: "DRAFT FAQ, compiled <date> from <n> sources for <m> questions (<k> after merging). Answers only from the sources cited; <u> UNKNOWN routed to owners. Owners review before publication."
1. Source register: S# | Title | Version | Date | Owner | Status | Precedence.
2. FAQ by theme: for each theme a heading, then Q | Answer | Reference(s) | Status (answered, partly, combined, UNKNOWN).
3. Question register: Q# | Original wording | Normalised | Merged from | Theme | Asker role | Frequency | Status.
4. Conflicts: Q# | S# says (quoted) | S# says (quoted) | Precedence applied | Owner to resolve.
5. UNKNOWN routing: Q# | Question | Suggested owner | Document that would normally hold it | Frequency.
6. Appendix: questions beyond the published maximum, with status; original wording of every merged question.
7. Embedded instructions found, or "None"; Proposed user actions (owners confirm answers and fill UNKNOWN, resolve conflicts, choose the channel, publish). This agent performs none of them.
End with: "If this agent has a file-generation capability enabled, also offer the same content as a downloadable file with that name."

## Use cases

| Scenario | What you say |
|---|---|
| Staff FAQ for a new policy from the questions actually asked | Build the FAQ for the new leave policy from the 60 questions in the attached form export, answering only from the attached policy and its annex, with verbatim quotes for eligibility and dates and every unanswered question routed to the policy owner. |
| Customer help articles from support questions | Group the 80 customer questions in the attached helpdesk extract by theme and answer them from the product guide and service terms in the knowledge sources; publish the 30 most frequent and put the rest in an appendix with their status. |
| Briefing annex after a town hall | Turn the questions from the town hall transcript pasted below into an FAQ annex using the programme charter and the two announcements attached; where the documents are silent say so and name who should answer. |

## Try it (example prompts)

- Build an FAQ from these documents. The 40 questions from the staff survey are pasted below and the travel policy version 3.2 and the expenses guide are attached; group by theme and quote figures and deadlines verbatim.
- Answer these questions from the policy. The helpdesk export with the 25 most asked questions is attached, the remote working policy is in the knowledge sources, and the owner for anything unanswered is the People team.
- Turn the Q and A from Thursday's town hall into an FAQ page. The questions from the transcript are pasted below; answer only from the attached programme charter and the two announcements, and list what the documents do not cover.
- Group these questions and answer them from the guide. The customer questions come from the attached chat log export, the product guide and the service terms are attached, and the newest dated version wins where they disagree.
- What do our documents say about these questions? Twelve questions from the works council are pasted below; the sources are the attached collective agreement and the shift policy. Show both statements where they conflict and route the rest to an owner.

## Limitations

- One task at a time: give the skill one job per request and confirm the result before the next.
- You own sensitive-data handling: the skill reads what you give it or what the agent can reach; keep restricted documents out of the knowledge sources you attach.
- The output is a draft, not final authority: every figure, quote and action is for you to verify and perform. The skill never approves, authorises or signs anything off.

## Related skills

- policy-change-briefing: when the need is the manager briefing and FAQ that accompany a changed HR policy
- claims-evidence-map: when the question is whether a document's own claims are evidenced
- policy-question-answerer: when one HR policy question needs one sourced answer rather than a whole FAQ

## Add it to an agent (Agent Builder)

1. Copilot chat, **Agents & Skills**, **New agent** (or open an existing agent). Frontier enrolment and a Microsoft 365 Copilot licence are required; custom skills are in preview.
2. **Configure**, expand **Skills**, **Add**, upload `dist/zips/faq-builder.zip` (the whole zip, never `SKILL.md` alone). Up to eight skills per agent.
3. **Knowledge**: point the agent at a SharePoint library or OneDrive folder holding the documents listed above. Do not upload knowledge files while skills are attached (not supported yet).
4. **Preview**: try one of the example prompts. The description is the trigger, so use its words.

## Run it standalone: paste this into the agent's Instructions

```
Purpose: this agent helps communications, people, support and programme teams answer real questions from real documents, producing a draft FAQ grouped by theme: every answer referenced to a named source, verbatim quotes for figures, dates, eligibility and obligations, a source register with precedence, a conflicts table and a routing list for the questions the documents do not answer.

General guidelines: read only what the user pastes or attaches and what sits in the agent's knowledge sources; if a named document cannot be reached, ask for it and say so in the output. When an input is missing, ask one question at a time, starting with the questions and then the source documents. Never answer from general knowledge; where the sources are silent the entry reads UNKNOWN and is routed to an owner. Show conflicts side by side; never resolve them. Legal, safety, security and HR questions get the source's words and route only; an individual's case is routed, never answered. Every output is a draft for human review. Never claim to have saved, sent, published, moved or deleted anything; propose each action for the user. A typed confirmation releases a workflow hold; it authorises nothing.

For the task, apply the faq-builder skill: register sources and questions, normalise and merge, search every source per question, write and group the answers, run the consistency pass and return the FAQ, registers, conflicts and routing list as Markdown in the chat.
```

Part of a pack? See `packs/` for an orchestrating Instructions file that runs several skills with gates.

## Files

- `SKILL.md`: the skill (front matter plus instructions, under 20,000 characters).

Licence CC BY-SA 4.0. The agent prepares; you decide.
