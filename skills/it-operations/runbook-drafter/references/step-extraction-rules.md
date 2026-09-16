# Step extraction rules

How source material becomes rows in the steps table. The rules keep the draft traceable to the source and keep the agent from completing, correcting or judging the procedure.

## Verbatim actions

- Commands, scripts, paths, menu paths, setting names and values are copied exactly as the source gives them, in code formatting. Spelling, casing, flags and quoting are preserved even where they look wrong; a suspected error becomes a validation question, never a silent correction.
- Variable parts (host names, identifiers, dates, tenant or account names, file names that change per run) become placeholders in angle brackets: <host>, <ticket identifier>, <date>. The placeholder names what the value is; the source value is kept in the Source column for the team's reference.
- Where the source gives a description instead of a command ("restart the service"), the action is the description in quotation marks with the source reference, and the validation question asks for the exact command or click path.

## One action per step

- A source sentence containing two actions ("stop the service and clear the cache") becomes two steps, both citing the same source reference.
- A source step whose order is unclear keeps the position the source gives it and carries the flag Contradicted with a question if another source places it elsewhere.

## Gaps

- Where the source moves from state A to state C without the action that produces B, insert a row "UNKNOWN step between n and n plus 1", Confidence UNKNOWN, and a validation question. Never fill the row from general knowledge of the platform.
- Where the expected result is not stated, the cell reads UNKNOWN and the question asks what the operator should see.
- Where the failure branch is not stated, the cell reads "UNKNOWN: escalate".

## Ticket histories and threads

- Work notes and messages that describe an action the responder later reverted, or that did not change the outcome, go to Steps tried without effect with their references. They are kept because the team may judge them useful or dangerous; the agent judges neither.
- The resolving path is the sequence of actions between the last reverted attempt and the stated resolution. Where the source does not make the boundary clear, both readings are shown and a question is raised.
- A responder's remark that a step is "probably unnecessary" or "might have helped" is kept verbatim in Variations and pitfalls; the step stays in the table with its source.

## Confidence

| Value | Meaning |
|---|---|
| Corroborated | The same action appears in two or more independent statements (two notes, a note and a command history line) |
| Stated once | One statement supports the step |
| UNKNOWN | The step's position is inferred from a gap; its content is missing |

Confidence describes evidence for the step's existence in the source. It says nothing about whether the step is correct or safe; that is the dry run's job.

## Destructive steps

- A step that deletes, drops, truncates, overwrites, restarts, disables, revokes, reboots or forces anything carries the flag "Destructive: confirm backup precondition". The flag points to the Preconditions section; where no backup or snapshot precondition is stated there, the precondition reads UNKNOWN and a question is raised.
- The step is kept exactly as stated. It is never removed, reordered, softened, wrapped in a confirmation prompt the source lacks, or annotated with an opinion about its risk.

## Secrets

- Passwords, tokens, keys, connection strings with embedded credentials and session identifiers are never reproduced. The value is replaced with <secret from approved store>, the UNKNOWN list records "credential redacted at <reference>", and a proposed user action asks the user to remove the value from the source.

## Physical, isolation and safety-related steps

- Where a step involves physical equipment, electrical or process isolation, a permit, a lock or a safety system, it is reproduced only as the source states it and carries the flag "the runbook authorises no isolation, permit or work". The validation question routes it to the responsible authority. The agent adds no procedure of its own for such steps and no statement about their adequacy.
