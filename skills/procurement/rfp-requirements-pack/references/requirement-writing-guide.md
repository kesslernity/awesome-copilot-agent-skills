# Requirement writing guide

Rules and patterns for the DRAFT requirements pack. Everything here shapes wording; nothing here supplies a fact, a target or a weight the inputs do not give.

## Requirement sentence

Shape: "The solution shall <one capability> <for whom or under what condition> <measurable outcome where the source gives one>."

A requirement passes when all four hold:
1. One capability. If the sentence contains "and" joining two capabilities, split it.
2. Testable. A supplier demonstration, document, reference or test could show it met or not met. "Easy to use" fails; "a trained user completes task X within Y minutes" passes only when the need or a standard supplies Y, otherwise Y is `[TBC]`.
3. Solution-neutral. No product name, supplier name, or feature that only one known product offers. Describe the outcome, not the mechanism.
4. Traced. It cites at least one need trace row, constraint or standard.

Words that fail the test and how to handle them:
- "etc.", "and so on", "including but not limited to": enumerate or drop.
- "user-friendly", "intuitive", "modern", "robust", "seamless": replace with the observable behaviour the need describes, or mark `[TBC]` and ask.
- "industry standard", "best practice": name the standard or drop the phrase.
- "should be able to": write "shall".
- "as required", "as appropriate": name who decides and when, or mark `[TBC]`.

## Priority scheme (default)

- Must: the need or a constraint states it as essential, or its absence defeats the stated outcome.
- Should: stated as wanted; the outcome survives without it at a cost the need names.
- Could: stated as desirable with no cost of absence given.
- `[TBC]`: the need does not say. Goes to the confirmation list.

Priorities come from the source wording, never from the agent's view of what matters.

## Non-functional categories and measure shapes

Each category lists the shape a target takes. The value inside comes from the need or a standard, or stays `[TBC]`.
- Performance: response time for a named transaction at a named load; batch window.
- Availability: percentage over a named period; planned maintenance window; recovery time and recovery point objectives.
- Security: named baseline or control set the solution must evidence; authentication method; encryption in transit and at rest as the policy states.
- Privacy and data location: where data is stored and processed; retention period; deletion on exit; roles of the parties.
- Integration: named systems, direction of data flow, protocol or interface type as stated, frequency.
- Accessibility: named standard and level the organisation is bound to.
- Usability: named user group, named task, completion measure.
- Scalability: named growth figure over a named period.
- Supportability and service levels: support hours, severity definitions, response and resolution times as stated.
- Compliance: named regulation, certification or audit right.
- Sustainability: named reporting or footprint requirement as stated.
- Exit and data portability: export format, timescale, assistance period as stated.

## Gate or scored requirement

A gate is pass or fail and is never weighted. Treat a constraint as a gate only when the source says the organisation cannot trade it (legal, regulatory, security baseline, data location, a ceiling stated as absolute). Everything else is a scored requirement. When the source is unclear, keep it scored and ask.

## Criteria families

Typical grouping; adapt to the organisation's template when one exists.
1. Functional fit: coverage of Must and Should functional requirements.
2. Non-functional and technical: coverage of the non-functional set.
3. Delivery and transition: plan, resourcing, migration, training, timescale.
4. Supplier capability and references: comparable work, team, financial standing as the plan asks.
5. Commercial: price and terms, scored only by a formula the organisation supplies.

Weights are `[TBC]` unless given. Given weights are checked for their stated total and never renormalised silently.

## Default scoring scale (mark "default, confirm")

- 0: No answer, or the answer does not address the requirement.
- 1: Addressed by assertion only; no evidence offered.
- 2: Partly met; evidence covers part of the requirement or depends on customisation not yet built.
- 3: Met; evidence (document, demonstration, reference) covers the requirement as written.
- 4: Met and evidenced with a verifiable measure exceeding the stated target, where a target exists.

Anchors describe evidence, not opinions of quality.

## Supplier question patterns

- Fact: "State the <measure> your solution achieves for <named transaction> at <named load>. Attach the test evidence." Linked to the requirement; answer format named.
- Document: "Provide the <named document, certificate, report> covering <requirement>."
- Demonstration: "Demonstrate <capability> during evaluation using the scenario in <annex>."
- Reference: "Name one client where <capability> is in live use, with a contact who has agreed to be approached."
- Yes or no with evidence: "Confirm <requirement>. If yes, cite the section of your response that evidences it."

A question never states the answer that scores well, never names a competitor's feature, and never asks for information the organisation is not permitted to collect.

## Confirmation list

Every `[TBC]`, every gate, every solution-neutrality flag, every defaulted setting and every technical assertion inside a question goes on the business owner confirmation list with a blank decision column. The pack is DRAFT until that list is worked through by a human, and nothing in it authorises a purchase, a contract, operations, permits, isolations or work.
