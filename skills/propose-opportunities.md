# Skill: propose-opportunities

Turn confirmed observations into the opportunity landscape: opportunities with stable
IDs, function and stream membership, impact and effort grades, quantified figures, and
enabling-gap dependencies. Schema references: `schemas/candidate-streams.schema.json`
and `schemas/opportunity-landscape.schema.json`.

## Inputs

The confirmed observation set; the value-stream list as it stands (streams are
proposed and confirmed separately); the enabling-gap list as it stands.

## Output

Draft opportunities, each carrying: a stable ID; a short name and an evidenced
description; function(s); stream membership(s); impact grade (stream-level grading
rules below); effort grade, marked as consultant judgement; quantified figure and unit
where the evidence carries one; and enabling-gap dependencies (gated) or none (open).

## Rules that bite here

- Every opportunity traces to observations; every figure traces to a source. An
  opportunity with no observation behind it does not exist.
- **Impact is graded at stream level** against the first two pillars: how much
  friction, manual effort and waiting the stream carries, and what removing it would
  release. **Effort is consultant judgement**, indicates deliverability, and never
  decides worth.
- **Quantified means captured timings and volumes, not delivery effort.** A figure
  carries its unit or it fails the checker. Self-reported figures stay marked
  self-reported.
- **Gating**: an opportunity waits on an enabling gap or it is open; record the
  dependency by gap ID. No other status of any kind: **no delivery statuses, ever**.
  What is already moving is the owning teams' knowledge, asked at the choosing
  session, not data in this artefact.
- **Membership counting**: an opportunity may sit on several streams and splits
  share-weighted across functions (1/n each) so nothing double-counts. Counts that sum
  past the opportunity total are correct and must be explained wherever shown.
- Multi-gap opportunities count against each gap's waiting count; that column sums
  past the gated total, and the report says so.
- No composite scores, no invented weights, no ranking formula. The six questions rank
  in the room; this artefact supplies the evidence columns they read.

## Gate

The consultant confirms the landscape (names, grades, memberships, gates) before the
workbook is built from it. The `facts` tool derives every published count from the
confirmed set; nothing is typed.
