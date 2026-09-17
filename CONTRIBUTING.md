# Contributing

One skill per folder under `skills/<category>/<skill-name>/`, with a required `SKILL.md` and optional `references/*.md`. Contributors need Python 3 with PyYAML for the two tools; users of the repository need nothing. Run `python3 tools/check_skills.py` before opening a pull request; it asserts every published limit for custom skills in declarative agents and rebuilds the zips.

Format rules (the checker enforces them):
- Front matter with exactly two keys, `name` (kebab-case, identical to the folder name) and `description` written as a folded block (`description: >-`). Agent Builder parses the front matter as strict YAML: a colon followed by a space in a plain description breaks the upload (the parser reads a second key), which is why every description here is a block scalar.
- Instructions under 20,000 characters (aim for 4,000 to 9,000), with the eight headings: Purpose, When to use, Inputs, Procedure, Output, Fallbacks and edge cases, Rules, Self-check.
- Capability-neutral: the agent reads what the user attaches, pastes or has placed in its configured knowledge sources; the skill proposes every write, send, move or delete for the user to perform; outputs are complete Markdown in the chat, with one line offering a downloadable file if the agent has that capability.
- Safety: draft-only, no invented data (UNKNOWN for missing inputs), a typed approval is a checkpoint recorded in the output and never an authorisation, nothing authorises operations, permits, isolations or work. AI prepares, humans decide.
- No URLs, no brand or company names, no em or en dashes inside a skill. British spelling.
- Companion files only of the types Microsoft lists; directory depth at most three; no scripts that need network access or package installation (the sandbox has neither).

Two more rules from the build: the description is the trigger (what it produces, then "Use when the user asks to ..." with quoted phrases, then "Do not use for ..., use <sibling> instead", ending "Drafts for human review; never approves, authorises or signs off."), and a skill folder's `README.md` is the human page (GitHub renders it) and is never included in the zip; regenerate it with `python3 tools/build_readmes.py` from `tools/meta/<skill>.json`. Licence: CC BY-SA 4.0, the same as the sibling repositories; a contribution is a contribution under that licence.
