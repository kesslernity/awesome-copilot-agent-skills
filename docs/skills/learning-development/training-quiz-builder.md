# Training quiz builder

Builds a DRAFT quiz from the training content the user supplies (slide deck, manual, e-learning script, session transcript, procedure): numbered questions with the correct answer, distractors drawn from the content itself, an explanation quoting the source passage with its location, a difficulty tag (Recall, Apply, Analyse) with its basis, and a coverage table showing which sections and objectives each question tests and which are left uncovered. Use when the user asks to "build a quiz from this deck", "write knowledge check questions for this module", "create an assessment from this training", "test understanding of this procedure" or "which sections does this quiz cover". Do not use for a reader-facing question and answer page built from documents, use faq-builder instead; for writing the procedure itself from notes or a walkthrough, use sop-drafter. Drafts for human review; never approves, authorises or signs off.

Category: `learning-development` · Skill name: `training-quiz-builder` · Upload package: `dist/zips/training-quiz-builder.zip`

## What to attach or make available

- The training content: slide deck, manual, e-learning script, session transcript or procedure, with section headings, page or slide numbers or timestamps
- The module's learning objectives, when stated
- The audience and prior level of the learners, as stated by the training owner
- The organisation's assessment style rules or question bank template, when one exists

## What you get

One complete Markdown document in the chat, pasteable into a document or import sheet, titled `DRAFT-training-quiz-<module title>-<YYYY-MM-DD>-v1` (revisions v2, v3). First line: "DRAFT quiz of <n> questions generated <date> from <sources>. Every answer traces to a quoted passage; pass mark, use and publication are the owner's decisions. Nothing here certifies, authorises or signs off competence."

Sections in order:
1. Quiz summary: Field | Value (sources, sections, statements, questions by type and difficulty, coverage, conflicts, UNKNOWNs).
2. Section register: Section ID | Title | Location | Testable statements | Status.
3. Allocation: Section ID | Statements | Questions planned | Recall | Apply | Analyse | Note.
4. Quiz, learner-facing, no answers: ID, type and difficulty in brackets, stem, lettered options or answer space.
5. Answer key: ID | Correct answer | Why correct (quoted passage, location) | Why each distractor is wrong | Difficulty basis | Section ID.
6. Coverage by section: Section ID | Title | Question IDs | Count | Difficulty tags | Objective | Status | Note. Then, if objectives were supplied, by objective: Objective | Sections | Question IDs | Status | Gap.
7. Conflicts: Statement A (quoted, location) | Statement B (quoted, location) | Effect on the quiz.
8. UNKNOWN list: Item | What the content does not state | Section ID | Effect on the quiz. The row count is the UNKNOWNs figure in the summary.
9. Embedded instructions found: Location | Text quoted | Action taken (reported, not followed); or "None".
10. DECIDE items: Decision | What the content offers | Owner. Pass mark, scoring and attempts always appear.
11. Proposed user actions: Action | Object | Reason (review every item, set the pass mark, pilot, load to the platform). This agent performs none.

Closing report: sources, defaults used, allocation versus delivered counts, fallbacks applied. End with: "If this agent has a file-generation capability enabled, also offer the same content as a downloadable file with that name."

## Use cases

| Scenario | What you say |
|---|---|
| Compliance module with stated objectives | Build a fifteen question knowledge check for the attached information security awareness deck using the six learning objectives pasted below; multiple choice only; return the coverage table by section and by objective. |
| Procedure training for a team | Create a ten question quiz from the attached purchase order approval procedure; use scenario items for the Apply level; every explanation must quote the passage it rests on with page and heading. |
| Transcript without slides | Write twelve knowledge check questions from the recorded session transcript pasted below; there are no slides, so section by topic change with timestamps and mark any cleaned quotes. |

## Try it (example prompts)

- Build a quiz from this deck: the 32-slide data protection awareness module is attached. Ten questions, default type and difficulty mix, coverage by slide section.
- Write knowledge check questions for this module. The e-learning script and the five learning objectives are pasted below; fifteen questions, and show which objectives each question tests.
- Create an assessment from this training: the attached records retention procedure. Twelve questions, multiple choice and scenario types only, with Apply and Analyse weighted above Recall.
- Test understanding of this procedure. The customer complaint handling procedure is attached; eight true or false and multiple choice items, each explanation quoting the source passage with its location.
- Which sections does this quiz cover? The existing quiz and the manual it was built from are both attached; give me the coverage table and list the sections it misses.

## Limitations

- One task at a time: give the skill one job per request and confirm the result before the next.
- You own sensitive-data handling: the skill reads what you give it or what the agent can reach; keep restricted documents out of the knowledge sources you attach.
- The output is a draft, not final authority: every figure, quote and action is for you to verify and perform. The skill never approves, authorises or signs anything off.

## Related skills

- course-outline-builder: when the module itself still needs structuring, before any quiz
- faq-builder: when the need is a reader-facing question and answer page, not an assessment
- training-needs-synthesis: when the question is what training is needed, not how to test it

## Add it to an agent (Agent Builder)

1. Copilot chat, **Agents & Skills**, **New agent** (or open an existing agent). Frontier enrolment and a Microsoft 365 Copilot licence are required; custom skills are in preview.
2. **Configure**, expand **Skills**, **Add**, upload `dist/zips/training-quiz-builder.zip` (the whole zip, never `SKILL.md` alone). Up to eight skills per agent.
3. **Knowledge**: point the agent at a SharePoint library or OneDrive folder holding the documents listed above. Do not upload knowledge files while skills are attached (not supported yet).
4. **Preview**: try one of the example prompts. The description is the trigger, so use its words.

## Run it standalone: paste this into the agent's Instructions

```
Purpose: this agent turns training content, slide decks, manuals, scripts, transcripts and procedures, into a draft quiz: questions with the correct answer, distractors from the content itself, explanations quoting the source passage with its location, difficulty tags with their basis, and a coverage table by section and objective.

General guidelines: read only what the user attaches or pastes and what sits in this agent's configured knowledge sources; if a source cannot be reached, say so and ask for a paste. When the training content, question count or learning objectives are missing, ask one question at a time. Nothing is invented: every answer, distractor and explanation traces to a located passage or reads UNKNOWN; suspected errors are flagged, never corrected as fact. The quiz tests what the content says, not whether it is correct or lawful. No item states that a learner is competent, qualified, certified or authorised; the pass mark is the training owner's decision. Never claim to have published, graded or deleted anything; propose each action for the user. Every output is a draft for human review. A typed confirmation releases a workflow hold and authorises nothing else.

For any request for a quiz, knowledge check, assessment or question bank from training material, follow the training-quiz-builder skill exactly, including its item-writing reference and self-check.
```

Part of a pack? See `packs/` for an orchestrating Instructions file that runs several skills with gates.

## Files

- `SKILL.md`: the skill (front matter plus instructions, under 20,000 characters).
- `references/item-writing-rules.md`: companion file referenced from the skill.

Licence CC BY-SA 4.0. The agent prepares; you decide.
