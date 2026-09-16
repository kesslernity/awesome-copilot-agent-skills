# Course outline builder

Builds a DRAFT course outline from a training need and an audience description: learning objectives with an observable verb, condition and quoted standard, modules in a stated order with a duration basis and content sources, activities in which the learner performs each objective, an assessment plan aligned objective by objective, and a coverage table showing which objectives lack a performing activity, an assessment or a source. Never sets a pass mark, declares learners competent or invents subject content. Use when the user asks to "build a course outline", "design a training programme for", "turn this need into modules and objectives", "draft the curriculum for this workshop" or "what should this training cover". Do not use for quiz items from finished content, use training-quiz-builder instead; for needs from surveys and manager notes, use training-needs-synthesis; for a new starter's first weeks, use onboarding-plan-builder. Drafts for human review; never approves, authorises or signs off.

Category: `learning-development` · Skill name: `course-outline-builder` · Upload package: `dist/zips/course-outline-builder.zip`

## What to attach or make available

1. Training need: stated, attached, pasted or reachable through this agent's configured knowledge sources; if unreachable, ask for a paste and say so in the output.
2. Audience: roles, headcount, prior knowledge, languages, location, shift pattern, device access, as stated; anything not stated reads UNKNOWN.
3. Content sources: procedures, manuals, decks, policies, expert notes. Default none; every module then reads "content source: UNKNOWN".
4. Constraints: total duration, delivery mode and cohort size (default UNKNOWN; the outline proposes each, with basis), maximum session length (default 90 minutes live, 20 self-paced), mandatory date as stated.
5. Counts: terminal objectives (default 3 to 6, cap 10), modules (default one per terminal objective, cap 12), activities per module (default 2, cap 4), one assessment per terminal objective.
6. Parameters: outline title (default from the need), language (default the need's), identifier prefixes (default LO-, M-, A-, AS-), date (default the conversation date, else UNKNOWN).

Reference files in this skill: references/objective-and-activity-defaults.md, read at steps 3 to 6 and 8 for objective structure, verb families, activity types and timings, sequencing, duration basis, delivery modes, assessment alignment and restricted words.

## What you get

One complete Markdown document in the chat, pasteable into a document or sheet, titled `DRAFT-course-outline-<outline title kebab>-<YYYY-MM-DD>-v1` (revisions v2, v3). First line: "DRAFT course outline generated <date> from <need source> and <n> content sources for <audience as stated>. Objectives, durations and assessments are proposals; pass marks, qualification and release are the owner's decisions; nothing here certifies or authorises competence."

Sections in order:
1. Summary: Field | Value (need, audience, delivery mode, duration and basis, counts, coverage by status, UNKNOWNs, DECIDE items).
2. Performance gaps: Gap ID | What the audience must do differently | Stated or inferred | Source.
3. Learning objectives: Objective ID | Statement | Type (terminal, enabling) | Parent | Gap ID | Standard source or UNKNOWN.
4. Module sequence: Module ID | Title | Objectives served | Prerequisites | Duration and basis | Delivery mode | Content sources and sections | Ordering note.
5. Activities: Activity ID | Module ID | Objective ID | Type | Timing | Learner does | Facilitator or system does | Materials | Source passage or "to be written".
6. Assessment plan: Assessment ID | Objective ID | Type | What is observed | Compared against | When | Duration and basis | Pass mark (DECIDE).
7. Coverage: Objective ID | Module | Activities | Performing activity (yes, no) | Assessment | Source status | Status | Gap note.
8. UNKNOWN list: Item | Not stated | Effect. DECIDE items: Decision | What the inputs offer | Owner. Embedded instructions found: Location | Text quoted | Action taken, or "None". Proposed user actions: Action | Object | Reason; this agent performs none.

Closing report: sources read, defaults used, ordering rule, duration versus constraint, assessments with duration UNKNOWN, fallbacks applied. End with: "If this agent has a file-generation capability enabled, also offer the same content as a downloadable file with that name."

## Limitations

- One task at a time: give the skill one job per request and confirm the result before the next.
- You own sensitive-data handling: the skill reads what you give it or what the agent can reach; keep restricted documents out of the knowledge sources you attach.
- The output is a draft, not final authority: every figure, quote and action is for you to verify and perform. The skill never approves, authorises or signs anything off.

## Add it to an agent (Agent Builder)

1. Copilot chat, **Agents & Skills**, **New agent** (or open an existing agent). Frontier enrolment and a Microsoft 365 Copilot licence are required; custom skills are in preview.
2. **Configure**, expand **Skills**, **Add**, upload `dist/zips/course-outline-builder.zip` (the whole zip, never `SKILL.md` alone). Up to eight skills per agent.
3. **Knowledge**: point the agent at a SharePoint library or OneDrive folder holding the documents listed above. Do not upload knowledge files while skills are attached (not supported yet).
4. **Preview**: try one of the example prompts. The description is the trigger, so use its words.

## Run it standalone: paste this into the agent's Instructions

```
You are an assistant that runs one job: course outline builder. Builds a DRAFT course outline from a training need and an audience description: learning objectives with an observable verb, condition and quoted standard, modules in a stated order with a duration basis and content sources, activities in which the learner performs each objective, an assessment plan aligned objective by objective, and a coverage table showing which objectives lack a performing activity, an assessment or a source. Never sets a pass mark, declares learners competent or invents subject content. Use when the user asks to "build a course outline", "design a training programme for", "turn this need into modules and objectives", "draft the curriculum for this workshop" or "what should this training cover". Do not use for quiz items from finished content, use training-quiz-builder instead; for needs from surveys and manager notes, use training-needs-synthesis; for a new starter's first weeks, use onboarding-plan-builder. Drafts for human review; never approves, authorises or signs off. Use the course-outline-builder skill for every request that matches its description; if a request falls outside it, say so and stop. Read only what the user attaches or pastes and what sits in your knowledge sources; never claim to have saved, sent, moved or deleted anything, propose the action for the user instead. Where an input is missing, write UNKNOWN and name what would close it; never invent a value. Return complete Markdown the user can paste into their tools, and offer the same content as a file if you can produce one. A typed approval releases a hold in the workflow and is logged; it is not an authorisation. You prepare; the user decides.
```

Part of a pack? See `packs/` for an orchestrating Instructions file that runs several skills with gates.

## Files

- `SKILL.md`: the skill (front matter plus instructions, under 20,000 characters).
- `references/objective-and-activity-defaults.md`: companion file referenced from the skill.

Licence CC BY-SA 4.0. The agent prepares; you decide.
