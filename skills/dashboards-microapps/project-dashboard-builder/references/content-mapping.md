# Content mapping rules

How a project's tracker files map to dashboard sections. Apply these rules exactly; where a tracker file uses different headings, map by meaning and say so when confirming scope with the user. Use only what the files or the user state. A value the layout needs that no source supplies renders UNKNOWN, with three named exceptions: a decision with no date renders "Undated", a risk with no mitigation renders "None recorded", a risk with no severity renders "Unrated".

## File to section map

| Tracker file | Dashboard section | What to extract |
|---|---|---|
| project.md, Current status section | Status banner | Overall colour (Green, Amber, Red), one headline sentence, a 2 to 3 sentence summary, reporting period or as-of date |
| project.md, Milestones table | Milestones table | Milestone name, due date (the tracker's Target date column), owner where recorded, state |
| risks.md, Risks (R-) table | Risks heat list | Risk description, severity (see Risks heat list below), mitigation if recorded, Status |
| risks.md, Assumptions (A-), Issues (I-), Dependencies (D-) tables | Not rendered by default | Render Issues only when the user asks, as its own list under an "Issues" heading with the same severity rule; never render Assumptions or Dependencies unasked |
| decisions.md | Decisions log | Decision date, decision text, owner or decider |
| links.md | Links list | Link label and address, in the order listed |
| actions.md | Not rendered | Do not render open actions as a section; if the user asks for them, suggest adding an open-actions count to the status summary sentence instead |
| any other .md | Background only | Use for understanding context; never render content the user has not asked for |

## Status colour rules

1. If the Current status section of project.md states a colour (Green, Amber, Red, or RAG wording such as "we are amber"), use it.
2. If not stated, propose a colour and ask the user to confirm before generating:
   - propose Amber if any milestone is marked late or at risk, or any open risk is High severity
   - propose Green otherwise
3. Never propose Red. Red appears only when the tracker states it or the user says it.
4. `{{STATUS_WORD}}` in the template is the capitalised word (Green, Amber, Red); `{{STATUS_CLASS}}` is the lowercase class (green, amber, red).

## Milestones

- Keep tracker order unless the tracker is clearly unordered, in which case sort by due date ascending.
- State is one of Done, Not started, On track, At risk, Late. Map tracker wording to the closest of these; wording that maps to none of them renders verbatim; a milestone with no state recorded renders UNKNOWN in the `{{STATE_OR_UNKNOWN}}` cell.
- Dates render as written in the tracker; do not reformat or infer missing dates. A milestone with no due date or no owner renders UNKNOWN in that cell.

## Risks heat list

- Severity is the tracker's severity word when one exists; map wording to High, Medium or Low (for example critical to High, minor to Low). When the tracker holds Likelihood and Impact cells instead of a severity word, severity is the Impact cell (H renders High, M Medium, L Low); never multiply, add or average the two cells. A row whose description says "score UNKNOWN" renders Unrated whatever its cells. A risk with neither a severity word nor an Impact cell renders Unrated.
- Unrated items sit after the Low items with the severity word "Unrated", no severity class on the item (the base `.risk` grey border) and the `unrated` modifier on the severity span: `<div class="risk"><span class="sev unrated">Unrated</span> ...`.
- Sort High, then Medium, then Low, then Unrated. Within a band keep tracker order.
- Render only the Risks (R-) table. Render Issues (I-) only when the user asks, as a separate list under its own heading; never render Assumptions (A-) or Dependencies (D-) unasked.
- Include rows with Status Open or Mitigating; exclude Closed and Superseded unless the user asks. A tracker with no Status column: exclude rows the tracker marks closed or resolved in words.
- Cap at 10 items. If truncated, fill the count line under the list: "Showing 10 of N risks; full list in risks.md". If not truncated, delete the count line.
- Mitigation not recorded renders "None recorded".

## Decisions log

- Newest first, capped at 10. If truncated, fill the count line under the table: "Showing 10 of N decisions; full list in decisions.md". If not truncated, delete the count line.
- A decision with no date renders with the date cell containing "Undated". A decision with no owner renders UNKNOWN in the owner cell.

## Links

- Render only links found in links.md or given by the user in this conversation. Never add links you believe exist (document sites, team channels) without an address from a source.
- If a link has no label, use the visible address as the label.

## Pasted-summary mode

When building from a pasted summary instead of tracker files:

- Parse the summary into the same five sections by meaning.
- Any section the summary does not cover renders as "No data provided".
- Severity, state and colour rules above still apply; ask rather than guess.
- `{{SOURCE_DESCRIPTION}}` in the footer becomes "a summary supplied in conversation".
