# File templates: project.md, decisions.md, links.md

Use these as the initial content when scaffolding a new project file set. Replace `<Project name>` and the date placeholders with real values; set every field the user has not supplied to UNKNOWN. The risks.md template lives separately in references/raid-log-template.md. Each file is returned complete in the chat, headed by its file name, for the user to save.

Shared conventions:

- Every file starts with a Changes section. Prepend one dated line per update run: date, what was added or revised, sources scanned and window, sources not reachable.
- Logs are newest first.
- Decision Status values: Agreed, Superseded by D-xxx. Superseded decisions stay in the table.
- Never delete rows or log entries; mark them Superseded instead.
- UNKNOWN marks any field no source states. Never fill it by inference.

---

## Template: project.md

```markdown
# Project: <Project name>

## Changes

- YYYY-MM-DD: File created.

## Overview

- Project name: <Project name>
- File set name: <project-name>
- Aliases (other names used in email and channel posts): UNKNOWN
- Sponsor: UNKNOWN
- Project lead: UNKNOWN
- Start date: UNKNOWN
- Target end date: UNKNOWN
- Goal (one sentence): UNKNOWN

## Current status

- Overall: Green, Amber or Red as stated by the sources or the user; UNKNOWN when none states it
- Summary (3 lines maximum): UNKNOWN

## Milestones

| Milestone | Target date | Status |
|-----------|-------------|--------|
| UNKNOWN | YYYY-MM-DD | Not started |

## Progress log (newest first)

- YYYY-MM-DD: UNKNOWN (source: UNKNOWN)
```

---

## Template: decisions.md

```markdown
# Decision log: <Project name>

## Changes

- YYYY-MM-DD: File created.

## Decisions (newest first)

| ID | Date | Decision | Context (why) | Decided by | Source | Status |
|----|------|----------|---------------|------------|--------|--------|
| D-001 | YYYY-MM-DD | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | Agreed |
```

Note: decision IDs (D-001) and dependency IDs in risks.md (also D-001) are separate sequences in separate files; when cross-referencing, write "decisions.md D-001" or "risks.md D-001" to avoid ambiguity. A decision is recorded as the source states it; logging it does not judge or approve it.

---

## Template: links.md

```markdown
# Links and key files: <Project name>

## Changes

- YYYY-MM-DD: File created.

## Links (newest first)

| Added | Title | Type | Location | Why it matters |
|-------|-------|------|----------|----------------|
| YYYY-MM-DD | UNKNOWN | document / channel thread / email / external link | UNKNOWN | UNKNOWN |
```

Location holds the path or reference exactly as it appears in the source. Do not construct or guess a location.
