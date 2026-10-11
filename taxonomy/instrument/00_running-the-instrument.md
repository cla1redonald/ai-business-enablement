# Running the 20-area readiness instrument

The instrument rates an organisation's AI groundwork across 20 areas, four per enabler,
in the canonical enabler order (`../enablers.md`). It is runnable standalone: an interview
pack and a set of documents in, a rated grid and roll-up out. It answers "how ready are
we, and where are we not". It does not size opportunities or gaps; that is the discovery's
job, with its own instrument.

## The rating scale

Exactly four values. No score, percentage or maturity level, and adding one would imply a
scale that was never published.

- **In place**: the control exists and is doing its job today. It does not mean finished.
  An area can be in place and still carry the most commentary in the assessment, because a
  strong control that outruns the ability to evidence it is a specific and recognisable
  exposure.
- **Partial**: something real exists and works, and a material half is missing. Grade
  partial when the practice is present but unevidenced, present in one population but not
  another, or present for one class of system but not the class that matters.
- **Gap**: nothing implements the area, or what exists is individual habit rather than
  organisational capability. A gap that is actively closing may be marked "gap, closing
  now"; the rating stays gap until the control is doing its job.
- **Blocked**: something actively prevents progress (a network boundary, an undecided
  decision that everything waits on, a commercial tier), and no agreed route exists.
  Blocked is rare. A blocked sub-item can sit inside an area rated partial; name it and
  count it separately rather than dragging the whole area down.

## Evidence modes

Discovery conversations surface what is slow in somebody's day. Nobody volunteers their
audit posture or their identity model unprompted, so some areas must be **examined
directly** rather than waited for: review the admin console together, read the policy set,
ask to be shown the permission grants. Mark every directly-observed rating "observed
directly" so a reader knows how the evidence arrived. Expect roughly a quarter of areas to
need direct examination, concentrated in Proof and in Hosting and identity.

Two lines to keep visible in every output:

- **Findings are evidence-derived; actions are consulting judgement.**
- Anything assessing what does not yet exist (agent infrastructure an organisation has not
  built) is **judgement, not evidence**, carries no rating, and says so.

Rate the ability, not the instance: if the question is whether the organisation can
attribute cost, the grade covers its ability to attribute, not what the attribution would
show. And keep absence apart from non-examination: "not seen" is a different sentence from
"not there", and coverage that was deliberately light must say so.

## Running it

1. **Assemble the inputs.** Interview and session summaries from the discovery, the policy
   set (AI policy, acceptable use, data protection and classification), an admin-console
   review for each AI surface, and the connector list. The instrument works from real
   conversations, not summaries of summaries, wherever it can.
2. **Rate each area** using its definition, evidence prompts and rating anchors (files
   01 to 05, one per enabler). For each area record: the rating, the finding with its
   evidence, and the action. Finding first, action last, always separated.
3. **Roll up.** Count ratings per enabler into the summary table and render the readiness
   grid (20 cells, five rows). Report one line per area in the summary; the full argument
   lives in the per-area detail.
4. **Read the clusters, not the count.** Where the gaps concentrate says more than how
   many there are. A theme rated gap in every area is a finding in itself; so is a single
   gap that is the largest item in its theme.
5. **State the strengths.** An assessment of this shape drifts negative without active
   effort. Name what is genuinely in place, and aim the whole at roughly 60/40 rather than
   a catalogue of absences.

## Quality bar

A second consultant, given the same inputs and this instrument, should land within one
rating step of the first on most areas. Where a rating is genuinely arguable, the finding
should say what would settle it.
