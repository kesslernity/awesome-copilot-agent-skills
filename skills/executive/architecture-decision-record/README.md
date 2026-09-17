# Architecture decision record

Drafts an architecture or design decision record (ADR) from the discussion notes, design review minutes, chat threads and diagram descriptions the user provides: context, decision drivers, options considered with arguments as stated, the decision as the group worded it, consequences and a review date, with every factual claim tagged evidenced, asserted or UNKNOWN so unsupported claims are marked for the author to substantiate. Use when the user asks to "write an ADR", "document the architecture decision", "record why we chose this design", "turn these design review notes into a decision record" or "draft the design decision log entry". Do not use for a business or governance decision with no technical design, use decision-memo-builder instead; for the change ticket that implements the decision, use change-request-pack. Drafts for human review; never approves, authorises or signs off.

**[Download the upload package](https://github.com/kesslernity/awesome-copilot-agent-skills/raw/main/dist/zips/architecture-decision-record.zip)** (one zip, ready for Agent Builder) · Category: `executive` · Skill name: `architecture-decision-record`

## What to attach or make available

- The design discussion itself: design review minutes, architecture board notes, a chat thread export, a transcript or review comments with diagram descriptions, attached or pasted, or held in a knowledge source the agent can reach
- The team's ADR template and numbering convention, if one exists, so the record matches the register
- Evidence attachments the discussion cites, such as benchmarks, estimates, pilot results, assessments or vendor documents, so claims can be tagged evidenced rather than asserted
- Standards or architecture principles the team works to, only where the discussion names them as constraints

## What you get

One complete Markdown document in the chat that pastes cleanly into the team's ADR template or wiki:
- Title (first heading): the Title from Inputs 7; the DRAFT notice line follows it.
- Header: Field | Value (ADR reference, title, status, system in scope, discussion date, forum, decision owner, author, review date or trigger, supersedes or superseded by, related records with attached yes or no, DRAFT).
- Context: paragraphs with fragment references.
- Decision drivers: # | Driver | Raised by | Fragment.
- Options considered: # | Option | Description | For (speaker) | Against (speaker) | Outcome and reason as stated | Fragment.
- Decision: the group's wording, then the verbatim fragment and location.
- Consequences as stated: # | Consequence | Type | Tag | Fragment.
- Claim register: # | Claim | Option or section | Tag | Source and reference | To substantiate with.
- Dissent and open questions: Participant | Point (verbatim) | Answered (yes, no) | Answer as stated.
- Gaps for the author: Gap | Section | Needed before acceptance per the team's template (yes, no, UNKNOWN) | Who could supply.
- Source quotes appendix: # | Fragment | Location | Used in section.
- Embedded instructions found (or "None"), closing report.
If this agent has a file-generation capability enabled, offer the same content as a downloadable file with that name; otherwise say nothing about files. Never claim the record was saved, committed, merged, logged or accepted.

## Use cases

| Scenario | What you say |
|---|---|
| Architecture board meeting needs a formal record | Write an ADR from the attached architecture board minutes of 4 March on the event streaming platform choice; the forum is the architecture board and the system in scope is the integration layer. |
| Decision made in chat and never written down | Document the architecture decision in this pasted chat thread about moving the reporting database to a managed service; the thread ran on 12 and 13 May and the system in scope is the reporting database. |
| Claims in the discussion need substantiating before acceptance | Turn the attached design review transcript of 21 June on the API gateway into a decision record and tag every factual claim evidenced, asserted or UNKNOWN; the benchmark report is attached as well. |

## Try it (example prompts)

- Write an ADR from the attached design review minutes of 4 March on the event streaming platform; the forum was the architecture board, the system in scope is the integration layer, and our records use the ADR-2026-03-04-01 numbering style.
- Document the architecture decision in this pasted chat thread from the platform team about moving the reporting database to a managed service; the thread ran on 12 and 13 May and the system in scope is the reporting database.
- Record why we chose this design: the attached transcript of the design review on 21 June covers the choice of an API gateway for the customer portal. Tag every claim evidenced or asserted; the benchmark report the team cited is attached too.
- Turn these design review notes into a decision record. The notes are pasted below, the component is the identity service, the discussion took place on 9 April, and our ADR template is attached as adr-template.docx.
- Draft the design decision log entry for the caching approach discussed in the attached pull request review comments; the system in scope is the order service, the participants are named in the comments, and keep it under 800 words.

## Limitations

- One task at a time: give the skill one job per request and confirm the result before the next.
- You own sensitive-data handling: the skill reads what you give it or what the agent can reach; keep restricted documents out of the knowledge sources you attach.
- The output is a draft, not final authority: every figure, quote and action is for you to verify and perform. The skill never approves, authorises or signs anything off.

## Related skills

- decision-memo-builder: when the decision is a business or governance choice with no technical design
- change-request-pack: when the user needs the change ticket that implements a decision already recorded
- transcript-to-actions: when the user wants the meeting's minutes or action list rather than one design decision

## Add it to an agent (Agent Builder)

1. Copilot chat, **Agents & Skills**, **New agent** (or open an existing agent). Frontier enrolment and a Microsoft 365 Copilot licence are required; custom skills are in preview.
2. **Configure**, expand **Skills**, **Add**, upload the zip you downloaded above (the whole zip, never `SKILL.md` alone). Up to eight skills per agent.
3. **Knowledge**: point the agent at a SharePoint library or OneDrive folder holding the documents listed above. Do not upload knowledge files while skills are attached (not supported yet).
4. **Preview**: try one of the example prompts. The description is the trigger, so use its words.

## Run it standalone: paste this into the agent's Instructions

```
Purpose. You turn one design or architecture discussion, such as design review minutes, a chat thread, a transcript or review comments with diagram descriptions, into one DRAFT architecture decision record: context, decision drivers, options considered with the arguments as stated, the decision as the group worded it, consequences, review date, dissent and open questions, with every factual claim tagged evidenced, asserted or UNKNOWN. General guidelines. Read only what the user attaches or pastes and what sits in your knowledge sources; if the discussion is out of reach, ask for a paste or an export and say so in the output. When an input is missing, ask one question at a time, then proceed with UNKNOWN for anything the source does not settle; never invent an option, argument, owner, date or reason, and never rank or recommend a design. Return the record in the chat as complete Markdown the user can paste into their template or wiki, and offer a downloadable file only if you have a capability that produces files. Never claim to have saved, committed, logged, merged, sent or deleted anything; propose those actions for the user. Everything you produce is a draft for human review. A typed go-ahead releases a hold in the workflow; it is not an authorisation, and no record accepts a decision or approves a change. For the task, follow the architecture-decision-record skill in full: it defines the inputs, procedure, claim tags, layout and self-check.
```

Part of a pack? See `packs/` for an orchestrating Instructions file that runs several skills with gates.

## Files

- `SKILL.md`: the skill (front matter plus instructions, under 20,000 characters).
- `README.md`: companion file referenced from the skill.

Licence CC BY-SA 4.0. The agent prepares; you decide.

Free: [Copilot on One Page](https://www.kesslernity.com/copilot-on-one-page?utm_source=github&utm_medium=readme&utm_campaign=agent_skills_repo&utm_content=skill_footer), a one-page sheet on how to phrase a request to Copilot. Paid: [Agent Instruction Block Design Guide](https://store.kesslernity.com/l/eyeauo?utm_source=github&utm_medium=readme&utm_campaign=agent_skills_repo&utm_content=skill_footer_guide), $19, twelve patterns for an agent's Instructions field. I am the author and the seller.
