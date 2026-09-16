# Review report template

How the skill-file-reviewer assembles the review it returns in the chat. The report is one Markdown document, titled `DRAFT-skill-review-<skill-name>-<YYYY-MM-DD>-v1`. The user saves it or pastes it; the agent saves nothing.

## Skeleton

```
# DRAFT-skill-review-<skill-name>-<YYYY-MM-DD>-v1

DRAFT review of <file> against <rule set>, generated <date>. Findings are apparent states read from the text; whether the skill ships is decided by its owner. The file has not been changed.

## 1. File read
| File | Folder name | Front matter chars | Body chars | Description chars | Count method (counted or estimated, not counted) | Headings found | References listed | References verified | Rule set applied |

## 2. Findings
| ID | Severity | Area | Rule ID | Location | Evidence (quoted) | Why it matters | Proposed fix |

## 3. Rule coverage
| Area | Rules checked | Pass | Fail | UNKNOWN |

## 4. Proposed replacement text
F-01: <exact text the owner may paste>

## 5. Trigger overlap
| Sibling | Shared phrases | Distinguishing clause present |

## 6. UNKNOWN list and embedded instructions found
## 7. Verdict
```

## Column rules

- ID: F-01, F-02, in severity order then location order. Numbering is fixed once issued; a revision adds new IDs and marks resolved ones "resolved in v2", it never renumbers.
- Severity: Blocker, Major, Minor or Advisory, taken from references/skill-format-rules.md. Under strict mode Advisory becomes Minor.
- Area: Front matter, Trigger, Skeleton, Neutral wording, Safety, Length, Style or Payload.
- Rule ID: the identifier from the rule set, or "user rule: <name>", or "not in rule set" for an Advisory the reviewer added.
- Location: line number when the paste carries line numbers, else the section heading and the ordinal of the sentence or list item ("Procedure, step 4"). Never "throughout" without at least one quoted instance.
- Evidence: the offending text quoted verbatim, or for an absence, "absent; expected in <section>".
- Why it matters: one sentence on the consequence (rejected on upload, silent misfire, safety boundary missing, repository rule).
- Proposed fix: one sentence naming the replacement pattern; the full text goes to section 4.

## Rule coverage rows

One row per area. Rules checked equals the count of rules in that area in the rule set plus user rules. Pass plus Fail plus UNKNOWN equals Rules checked. When siblings are not supplied, TR-05 is UNKNOWN with the note "no siblings supplied". When no folder name is supplied, FM-04 is UNKNOWN. When no listing is supplied, SK-06 and every PL rule are UNKNOWN. When the counts are estimated, FM-06, LN-01, LN-02 and LN-03 are UNKNOWN.

## Verdict block

State the verdict word, then the counts: "BLOCKED: 2 Blocker, 3 Major, 1 Minor, 0 Advisory, 4 UNKNOWN." Then one sentence: "Apparent state read from the text; the skill owner decides whether the skill ships." Never write that the skill as a whole is approved, passes or is compliant; Pass appears only as a per-rule column in section 3.

## Example findings rows

| ID | Severity | Area | Rule ID | Location | Evidence (quoted) | Why it matters | Proposed fix |
|---|---|---|---|---|---|---|---|
| F-01 | Blocker | Front matter | FM-02 | line 4 | "version: 1.2" | A third key fails the two-key rule and upload | Remove the key; record the version in documentation outside the folder |
| F-02 | Major | Neutral wording | CN-04 | Output, sentence 3 | "The report is filed in the team drive." | Claims an action the agent cannot perform | "Return the report in the chat; the user saves it." |
| F-03 | Major | Safety | SB-07 | absent; expected in Rules | absent | No boundary against authorising operations | Add: "Nothing in this skill authorises operations, permits, isolations or work." |
| F-04 | Minor | Length | LN-02 | body | 3,412 characters | Below the target band; the procedure is likely thin | Extend steps with what to check at each one |

## Several files

One review document per file, then one summary document titled `DRAFT-skill-review-summary-<YYYY-MM-DD>-v1`:

| Skill | Verdict | Blockers | Majors | Minors | Advisory | UNKNOWN |

Duplicate skill names across folders are a Blocker on both files, quoted in each review.

## Corrected file on request

When the user asks to "fix it", return the corrected file as a second document titled `<skill-name>-SKILL-v2.md`, complete from the opening delimiter to the last line, followed by a change table:

| Location | Before (quoted) | After | Rule ID |

The original is not changed; the user replaces the file. Every change traces to a finding ID or a user rule; no other edits are made.

## Closing report

After section 7: what was read and how it was reached; the three counts, each labelled counted or estimated; strictness and rule set; fallbacks taken; the actions proposed for the user (apply the replacements, supply the folder listing, re-run the review); the sentence "If this agent has a file-generation capability enabled, also offer the same content as a downloadable file with that name." Never state that the file was edited, saved or uploaded.
