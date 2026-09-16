# RAID log template for risks.md

Use everything below the line as the initial content of risks.md when scaffolding a new project. Replace `<Project name>` and the date placeholder; leave the example rows in place as UNKNOWN stubs only if the user has given no entries yet, otherwise replace them with real entries. The file is returned complete in the chat, headed by its file name, for the user to save.

Conventions:

- RAID = Risks (might happen), Assumptions (taken as true but unverified), Issues (happening now), Dependencies (the team relies on someone outside it).
- IDs are sequential per table: R-001, R-002 for risks; A-001 for assumptions; I-001 for issues; D-001 for dependencies. Continue the sequence on every update, never reuse an ID.
- Likelihood and Impact use H (high), M (medium), L (low). If a source does not state likelihood or impact, the cell reads UNKNOWN; never fill a score by default.
- Status values: Open, Mitigating, Closed, Superseded. Closed and Superseded rows stay in the table with the date of the change; never delete a row.
- Every Open risk needs an Owner and a Review by date. If none is stated in any source, set Owner to UNKNOWN; the skill carries Owner UNKNOWN risks into the Asks section of the weekly status document.
- A risk is recorded as the source states it. The skill does not judge whether a mitigation is adequate, and nothing in this log authorises any operation, permit, isolation or work.

---

# Risks log: <Project name>

## Changes

- YYYY-MM-DD: File created.

## Risks (might happen)

| ID | Raised | Description | Likelihood | Impact | Owner | Mitigation / next step | Review by | Status |
|----|--------|-------------|------------|--------|-------|------------------------|-----------|--------|
| R-001 | YYYY-MM-DD | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | YYYY-MM-DD | Open |

## Assumptions (taken as true, not yet verified)

| ID | Raised | Assumption | Impact if wrong | Owner | Validate by | Status |
|----|--------|------------|-----------------|-------|-------------|--------|
| A-001 | YYYY-MM-DD | UNKNOWN | UNKNOWN | UNKNOWN | YYYY-MM-DD | Open |

## Issues (happening now)

| ID | Raised | Description | Impact | Owner | Next step | Status |
|----|--------|-------------|--------|-------|-----------|--------|
| I-001 | YYYY-MM-DD | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | Open |

## Dependencies (the team relies on someone else)

| ID | Raised | Dependency | Needed by | Owner | Counterparty | Status |
|----|--------|------------|-----------|-------|--------------|--------|
| D-001 | YYYY-MM-DD | UNKNOWN | YYYY-MM-DD | UNKNOWN | UNKNOWN | Open |
