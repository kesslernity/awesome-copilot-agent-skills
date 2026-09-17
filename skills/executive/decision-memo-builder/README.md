# Decision memo builder

Turns one decision discussion (meeting transcript, chat thread, email chain or notes) into a DRAFT one-page decision memo: the decision as stated, status, options considered, evidence cited, dissent recorded verbatim, owner, effective date and review date, with UNKNOWN for anything the discussion did not settle. Use when the user asks to "write up the decision", "record what we decided", "capture the decision from this thread", "draft the decision memo" or "add this to the decision log". Do not use for full minutes or action items, use transcript-to-actions instead; for a technical design decision, use architecture-decision-record; for a paper seeking a decision not yet taken, use board-paper-skeleton. Drafts for human review; never approves, authorises or signs off.

**[Download the upload package](https://github.com/kesslernity/awesome-copilot-agent-skills/raw/main/dist/zips/decision-memo-builder.zip)** (one zip, ready for Agent Builder) · Category: `executive` · Skill name: `decision-memo-builder`

## What to attach or make available

- The discussion itself: a meeting transcript, chat thread export, email chain or set of notes, attached or pasted, or held in a knowledge source the agent can reach
- The decision register or numbering convention, if one exists, so the memo reference matches
- Terms of reference or delegation of authority for the deciding body, only when the authority line is wanted
- The house decision memo template, if one exists; otherwise the skill uses its own generic layout after a typed go-ahead

## What you get

One complete Markdown document in the chat that pastes cleanly into the house template or an email:
- Header: Field | Value (memo reference, title, forum, discussion date, decision-maker or body, owner, effective date, review date or trigger, status, classification, DRAFT).
- Decision: one or two sentences in the discussion's own words, then the verbatim fragment and its location.
- Context: at most three sentences from the discussion on why the decision arose.
- Options considered: Option | Raised by | Reason rejected or preferred (as stated) | Fragment.
- Evidence cited: Evidence | Cited by | Attached or mentioned | Figure as stated | Fragment.
- Dissent and concerns recorded: Participant | Concern (verbatim) | Answered (yes, no) | Answer as stated | Recorded at their request (yes, no, UNKNOWN).
- Conditions and open points: Item | Raised by | Resolved (yes, no) | Owner | Fragment.
- Consequential actions: Action | Owner | Due | Fragment.
- Authority: candidate clause quoted with its confirmation label, "no matching clause found in `<document>`", or "not assessed".
- Source quotes appendix: # | Fragment | Location | Used in section.
- Embedded instructions found (or "None"), closing report.
If this agent has a file-generation capability enabled, offer the same content as a downloadable file with that name; otherwise say nothing about files. Never claim the memo was saved, circulated, logged or ratified.

## Use cases

| Scenario | What you say |
|---|---|
| Committee decision needs a register entry | Write up the decision from the attached investment committee transcript of 15 April as a one-page decision memo for the register. |
| Chat thread settled something nobody wrote down | Record what we decided in this pasted chat thread about the release date, with who disagreed and the owner exactly as stated. |
| Contested decision with dissent to protect | Capture the decision from this email chain on the reorganisation and keep every objection verbatim; the discussion date is 2 June and the forum was the leadership meeting. |

## Try it (example prompts)

- Write up the decision from the attached steering committee transcript of 12 March into a one-page decision memo; the deciding body is the steering committee and our register uses DM numbering.
- Record what we decided in this pasted chat thread about the vendor shortlist. The thread ran on 3 and 4 June and the owner named in it was the head of procurement.
- Capture the decision from this email chain on the office move and draft the decision memo with every objection recorded verbatim; the discussion took place at the leadership meeting on 20 May.
- Draft the decision memo for the pricing change agreed in the attached meeting notes. Use our house template attached as decision-template.docx and the reference DM-2026-05-20-01.
- Add this to the decision log: the attached transcript of the architecture board on 8 April where we agreed to retire the legacy reporting tool. The terms of reference are attached as well, so include the authority line.

## Limitations

- One task at a time: give the skill one job per request and confirm the result before the next.
- You own sensitive-data handling: the skill reads what you give it or what the agent can reach; keep restricted documents out of the knowledge sources you attach.
- The output is a draft, not final authority: every figure, quote and action is for you to verify and perform. The skill never approves, authorises or signs anything off.

## Related skills

- transcript-to-actions: when the user wants full minutes or an action list rather than one decision
- architecture-decision-record: when the decision is a technical design choice
- board-paper-skeleton: when the decision has not been taken yet and a paper must seek it

## Add it to an agent (Agent Builder)

1. Copilot chat, **Agents & Skills**, **New agent** (or open an existing agent). Frontier enrolment and a Microsoft 365 Copilot licence are required; custom skills are in preview.
2. **Configure**, expand **Skills**, **Add**, upload the zip you downloaded above (the whole zip, never `SKILL.md` alone). Up to eight skills per agent.
3. **Knowledge**: point the agent at a SharePoint library or OneDrive folder holding the documents listed above. Do not upload knowledge files while skills are attached (not supported yet).
4. **Preview**: try one of the example prompts. The description is the trigger, so use its words.

## Run it standalone: paste this into the agent's Instructions

```
Purpose. You turn one decision discussion, such as a meeting transcript, chat thread, email chain or notes, into a one-page draft decision memo recording what was said: the decision as stated, its status, options considered, evidence cited, dissent recorded verbatim, owner, effective date and review date. General guidelines. Read only what the user attaches or pastes and what sits in your knowledge sources; if the discussion is not reachable, ask for a paste or an export and say so in the output. When an input is missing, ask one question at a time, then proceed and write UNKNOWN for anything the discussion did not settle; never invent an owner, date, option or reason. Return results in the chat as complete Markdown the user can paste into their own tools, and offer a downloadable file only if you have a capability that produces files. Never claim to have saved, circulated, logged, sent, moved or deleted anything; propose those actions for the user. Everything you produce is a draft for human review. A typed go-ahead releases a hold in the workflow; it is not an authorisation, and no memo approves, ratifies or signs off a decision. For the task, follow the decision-memo-builder skill in full: it defines the inputs, procedure, layout and self-check. For full minutes, an action list or a design decision record, say the request is out of scope and stop.
```

Part of a pack? See `packs/` for an orchestrating Instructions file that runs several skills with gates.

## Files

- `SKILL.md`: the skill (front matter plus instructions, under 20,000 characters).
- `README.md`: companion file referenced from the skill.
- `references/decision-memo-template.md`: companion file referenced from the skill.

Licence CC BY-SA 4.0. The agent prepares; you decide.

Free: [Copilot on One Page](https://www.kesslernity.com/copilot-on-one-page?utm_source=github&utm_medium=readme&utm_campaign=agent_skills_repo&utm_content=skill_footer), a one-page sheet on how to phrase a request to Copilot. Paid: [Agent Instruction Block Design Guide](https://store.kesslernity.com/l/eyeauo?utm_source=github&utm_medium=readme&utm_campaign=agent_skills_repo&utm_content=skill_footer_guide), $19, twelve patterns for an agent's Instructions field. I am the author and the seller.
