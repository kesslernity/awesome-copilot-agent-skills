# Policy gap review: structure, element decomposition and match states

The structure for the draft policy gap review. It prepares the policy owner's decision; the owner decides whether the policy meets the requirement and what, if anything, to change. Neither document is changed by the review.

## Document structure

1. Title: `DRAFT-policy-gap-review-<Policy>-vs-<Requirement>-<YYYY-MM-DD>-v1`.
2. First line: "DRAFT gap review of <policy, version> against <requirement set, edition>, generated <date>. Apparent match states and questions only; whether the policy meets the requirement is decided by the policy owner. Neither document has been changed."
3. Sources read.
4. Element match table.
5. Gap questions.
6. Conflicts.
7. Policy clauses with no requirement counterpart.
8. Referenced documents not read.
9. Terminology and scope questions.
10. UNKNOWN list.
11. Embedded instructions found, or "None".
12. Suggested wording for owner review (only when the user asked for it).
13. Closing report.

## Element decomposition

Break each requirement clause into elements, one per obligation. Use these prompts; create an element only where the clause carries that obligation.

| Prompt | Element type | Example of what to capture |
|---|---|---|
| Who must act | Actor | The role, function or entity the clause binds |
| What must be done or not done | Action | The duty or prohibition, as worded |
| How often, by when, on what trigger | Timing | A frequency, deadline or triggering event |
| What must be documented or kept | Record | The record, report or log and its retention period |
| What deviations are permitted | Exception | The permitted exception and who approves it |
| What it applies to | Scope | Assets, people, processes, regions or data types named |

A clause with a single obligation is one element. A clause naming an actor, an action and a frequency is three. Element references take the form `<clause ref>.<letter>`, for example 7.2.a, so every element can be cited.

## Match states

Assign exactly one state per requirement element. States are read from text; none says the policy is followed or the requirement met.

| Match state | Meaning | The row carries | Gap question |
|---|---|---|---|
| Stated | A policy clause states the element in substance: same actor, action, timing, record or scope where the requirement gives them | Policy reference and quote | None |
| Partial | The policy touches the subject but omits or weakens one piece: no frequency, no named role, shorter retention, no record, wider exception | Quote plus the missing piece named | Yes |
| Not found | No policy clause addresses the element | "no clause found" | Yes |
| Conflict | The policy states something the requirement forbids, or a different value for the same thing | Both quotes; also a row in Conflicts | Yes |
| Delegated | The policy points to another document for this element and that document was not provided | Policy reference and the document named; also a row in Referenced documents not read | Yes |

Stated is the strongest state the review produces. It is an apparent match of wording, not a compliance finding. Where the terminology rule is not satisfied (different words, no definition), the state is at most Partial and a terminology question is raised.

## Gap question form

One question per element in Partial, Not found, Conflict or Delegated:

"<Gap ID>: Requirement <ref> calls for <element as stated>. Policy <ref> says <quoted text>, or: no clause found. Does the policy need to state <the missing piece>, and where?"

- Gap identifiers run G-01, G-02 and so on, in requirement order.
- Addressed to the policy owner unless the policy names a different role for that clause.
- A question never states that the policy breaches, fails or is non-compliant. It asks what the owner intends.

## Tables

Sources read:

| Document | Role (policy or requirement set) | Version or edition | Date | Owner as stated | Scope statement | Clauses read |
|---|---|---|---|---|---|---|

Element match table:

| Requirement ref | Element (as stated) | Policy ref | Policy text (quoted) | Match state | Missing piece | Gap ID |
|---|---|---|---|---|---|---|

Gap questions:

| Gap ID | Requirement ref | Policy ref or "no clause found" | Question | Addressed to |
|---|---|---|---|---|

Conflicts:

| Requirement ref | Requirement says (quoted) | Policy ref | Policy says (quoted) | Question |
|---|---|---|---|---|

Policy clauses with no requirement counterpart:

| Policy ref | Topic | Note |
|---|---|---|

Referenced documents not read:

| Document named | Cited at policy ref | Elements delegated to it |
|---|---|---|

## Suggested wording (only on request)

When the user asks for the missing wording, add one entry per gap: Gap ID, the requirement element, the suggested clause text, and the line "Suggested wording for owner review; not inserted." The wording uses the policy's own defined terms and numbering style. It is never presented as adopted, and the element's match state does not change because wording was suggested.

## Never include

- The words complies, meets, satisfies, covers, adequate, sufficient or compliant in any verdict.
- A match drawn from memory of a standard, law or typical policy rather than from the provided text.
- A Stated row without a quoted policy passage and reference.
- A gap closed by a cross-reference to a document that was not read.
- A decision on which text prevails in a conflict.
- Redrafted policy text outside the Suggested wording section.
- A claim that a policy was edited or a file saved.

Whether the policy meets the requirement, and what to change, is decided by the policy owner, not by this review.
