# Skill: assess-readiness

Run the 20-area readiness instrument against the engagement evidence and produce the
rated grid, the roll-up and the per-area findings. The instrument itself lives in
`taxonomy/instrument/`; this skill is how a session executes it.

## Inputs

The confirmed observation set and call summaries; the policy set as read; the direct
examination notes (console reviews, connector list walks, permission checks); the
taxonomy.

## Output

Per area: rating (in place / partial / gap / blocked), the finding with its evidence
references, and the action. Plus the per-enabler roll-up table and the grid render
data, in canonical enabler order.

## Rules that bite here

- **Findings are evidence-derived; actions are consulting judgement.** Keep the line
  visible in every output. Anything assessing what does not yet exist is marked
  "judgement, not evidence" and carries no rating.
- Mark every directly-examined rating "observed directly". Some areas never surface in
  conversation (audit posture, identity models, admin consoles); if the direct
  examination has not happened, the area is unassessed, not a gap.
- Rate the ability, not the instance, and keep absence apart from non-examination:
  "not seen" is a different sentence from "not there".
- In place means the control exists and is doing its job today, not finished. Where a
  strong control outruns its evidence, grade the control in place and the evidencing
  gap under Proof.
- No scores, percentages or maturity levels, ever. Four values only. Use blocked
  rarely, for something actively prevented; a blocked sub-item can sit inside a
  partial area, counted separately.
- Read the clusters, not the count, and state the strengths: the assessment drifts
  negative without active effort. Aim near 60/40.
- Every readiness finding cites its sources like any other claim. The readiness source
  count and the opportunity source count are reported separately and never merged.

## Gate

The consultant confirms every rating before the grid renders. Quality bar: a second
consultant, given the same inputs, lands within one rating step on most areas; where a
rating is arguable, the finding says what would settle it.
