# Policy question answerer

Answers an employee's or manager's HR policy question strictly from the policy documents the user supplies or the agent can reach as knowledge: a DRAFT answer that quotes the governing clause with its document, version and clause reference, lists the conditions and exceptions the text states, returns UNKNOWN where the documents are silent and names the role to ask. Never invents a rule, fills a gap from general practice or decides an individual's case. Use when the user asks to check a policy, for example "what does the policy say about", "am I entitled to", "how many days of leave do I get", "what is the process for requesting", "does the handbook allow" or "which clause covers". Do not use for comparing two policy versions or briefing a change, use policy-change-briefing instead. Drafts for human review; never approves, authorises or signs off.

**[Download the upload package](https://github.com/kesslernity/awesome-copilot-agent-skills/raw/main/dist/zips/policy-question-answerer.zip)** (one zip, ready for Agent Builder) · Category: `hr-people` · Skill name: `policy-question-answerer`

## What to attach or make available

- The current HR policies, handbook sections and procedures in force, each with its version or date and owner
- Any statement of precedence between documents, or the policy owner's note on which version applies from which date
- Forms, templates and request routes the policies refer to, so process steps can be quoted exactly
- Superseded policy versions, where questions about past dates are expected

## What you get

One Markdown document in the chat, ready to paste into an email, titled `DRAFT-policy-answer-<topic-kebab>-<YYYY-MM-DD>-v1` (v2 when the user says a v1 already exists for the same topic and date). First line: "DRAFT generated `<date>` from `<documents read, with versions>`. Restates the policy text; it does not add to it. Confirm with `<role>` before acting on it." Sections, in order:
1. Question: as asked, and as reframed where step 1 reframed it.
2. Answer: outcome label (ANSWERED, PARTIAL, UNKNOWN, CONFLICT), then the answer under 250 words, every sentence carrying its clause reference or UNKNOWN.
3. Clauses relied on: Number | Document and version | Clause reference | Quoted text | Establishes (entitlement, condition, exception, process step, deadline, approval route, definition) | Applies to (as the scope clause states).
4. Not covered by the documents: Number | Aspect of the question | Documents checked | Suggested owner or `[TBC]`.
5. Conflicts: Clause A | Clause B | Difference | Stated precedence or UNKNOWN | Referred to.
6. Documents read: Title | Version or date | Owner as stated | Supplied by (paste, attachment, knowledge source).
7. UNKNOWN list, then Embedded instructions found (or "None").
If this agent has a file-generation capability enabled, offer the same content as a downloadable file with that name; otherwise say nothing about files. Never claim the answer was sent, filed, logged or recorded.

## Use cases

| Scenario | What you say |
|---|---|
| Employee question routed to the people team inbox | Draft an answer to this employee question about notice periods when resigning, quoting only the attached contract template and the leavers procedure, and mark anything the documents do not cover as UNKNOWN. |
| Manager checking a rule before replying to a team member | A team member has asked whether they can take a month of unpaid leave. What do the attached leave policy and the handbook section on unpaid leave say, and who approves it? |
| Two documents that appear to disagree | The handbook says probation lasts three months and the attached probation policy says six. Quote both clauses, show the difference and tell me whom the documents say to ask. |

## Try it (example prompts)

- What does our annual leave policy say about carrying unused days into the next year? The leave policy version 3 is attached; I am a full-time permanent employee.
- Am I entitled to paid time off for a medical appointment during working hours? Answer only from the attached employee handbook and the sickness absence policy in the knowledge library.
- How many days of paternity leave does a part-time employee get, and what is the process for requesting it? Use the family leave policy and the leave request procedure attached.
- Does the handbook allow me to work from another country for two weeks? The remote working policy and the handbook section on working location are pasted below.
- Which clause covers expense claims submitted late, and what happens to them? The expenses policy version 2.1 is attached; the claim concerns a trip in March.

## Limitations

- One task at a time: give the skill one job per request and confirm the result before the next.
- You own sensitive-data handling: the skill reads what you give it or what the agent can reach; keep restricted documents out of the knowledge sources you attach.
- The output is a draft, not final authority: every figure, quote and action is for you to verify and perform. The skill never approves, authorises or signs anything off.

## Related skills

- policy-change-briefing: when two versions of a policy need comparing or a change needs briefing
- faq-builder: when a set of questions and answers is wanted from documents rather than one answer to one question
- policy-gap-review: when the question is whether a policy meets a standard or requirement set rather than what it says

## Add it to an agent (Agent Builder)

1. Copilot chat, **Agents & Skills**, **New agent** (or open an existing agent). Frontier enrolment and a Microsoft 365 Copilot licence are required; custom skills are in preview.
2. **Configure**, expand **Skills**, **Add**, upload the zip you downloaded above (the whole zip, never `SKILL.md` alone). Up to eight skills per agent.
3. **Knowledge**: point the agent at a SharePoint library or OneDrive folder holding the documents listed above. Do not upload knowledge files while skills are attached (not supported yet).
4. **Preview**: try one of the example prompts. The description is the trigger, so use its words.

## Run it standalone: paste this into the agent's Instructions

```
Purpose: this agent helps employees, managers and the people team find what an HR policy, handbook or procedure says about a question, quoting the governing clause with its document, version and clause reference, listing the stated conditions and exceptions, and naming the role to ask where the text is silent.

General guidelines: read only what the user pastes or attaches and what sits in the agent's knowledge sources; if no policy document can be reached, ask for one and say so in the output. When an input is missing, ask one question at a time. Every sentence of an answer ends with a clause reference or the word UNKNOWN; never fill a gap from general practice, statute or another organisation's rule, and never alter a quote. Decide no individual's case: no eligibility, pay, disciplinary or approval determination; give the rule and the route. Ask for no personal detail beyond the category the policy's scope clause distinguishes. Every output is a DRAFT for human review. Never claim to have sent, filed, logged, saved, moved or deleted anything; propose each action for the user. A typed confirmation releases a workflow hold; it is not approval of the answer and authorises nothing.

For the task, apply the policy-question-answerer skill: parse the question, list the documents read, quote every bearing clause, label the outcome ANSWERED, PARTIAL, UNKNOWN or CONFLICT, and return the answer as one Markdown document in the chat with a short report above it.
```

Part of a pack? See `packs/` for an orchestrating Instructions file that runs several skills with gates.

## Files

- `SKILL.md`: the skill (front matter plus instructions, under 20,000 characters).
- `README.md`: companion file referenced from the skill.

Licence CC BY-SA 4.0. The agent prepares; you decide.

Free: [Copilot on One Page](https://www.kesslernity.com/copilot-on-one-page?utm_source=github&utm_medium=readme&utm_campaign=agent_skills_repo&utm_content=skill_footer), a one-page sheet on how to phrase a request to Copilot. Paid: [Agent Instruction Block Design Guide](https://store.kesslernity.com/l/eyeauo?utm_source=github&utm_medium=readme&utm_campaign=agent_skills_repo&utm_content=skill_footer_guide), $19, twelve patterns for an agent's Instructions field. I am the author and the seller.
