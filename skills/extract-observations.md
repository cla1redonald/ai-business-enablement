# Skill: extract-observations

Read one conversation or document source and extract evidence-bound observations: the
atomic layer everything else (opportunities, streams, readiness findings) is built on.
Schema reference: `schemas/landscape-observation.schema.json`.

## Inputs

One source (real transcript or document, never a summary of a transcript when the
transcript exists), its sub-type, and the running observation set for dedupe awareness.

## Output

Observations, each carrying: the claim, in plain language using the room's own verbs;
at least one source reference (file name exactly as supplied, then position); the
verbatim quote where available; confidence on the shared scale; and, when the source
states them, `scale` (cadence, load, headcount, each with its own reference),
`held_by`, and `stated_dependencies` (the speaker's own linkage, as a quote).

## Rules that bite here

- **No source, no claim. A quote must exist verbatim in the source it cites.**
- Extract from non-consultant turns only; the consultant's questions signal what
  matters and are never evidence. Keep the second-hand relay exception, cited as
  indirect. Reject first-person consultant claims.
- Omit what the source cannot know: a single interview does not know where its process
  sits in a wider stream. Never invent a value to fill a required-looking field, and
  never silently drop evidence that will not fit; say what would not fit.
- A measurement carries a number or it does not exist. "It takes ages" is recorded as
  prose evidence that no number was given; it never becomes a number.
- Two citations of the same passage are one piece of evidence.
- One observation per claim: do not bundle a workflow description and its timing and
  its pain into one blob; downstream grading needs them separable.
- Pointed at a transcript, work the whole file: the recurring failure is extracting
  the workflow and skimming the sentence where somebody says "a day and a half".

## Gate

The consultant confirms observations (spot-check against sources) before they feed
opportunities or readiness. Surface the weak ones at low confidence rather than
polishing them.
