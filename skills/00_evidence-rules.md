# The evidence rules

Every skill in this kit restates the rules that matter most for it, so a skill pasted
alone still holds the line. This file is the full reference. The rules were proven in a
delivered engagement and a reference pipeline before they were rules; each one exists
because its absence produced a real defect.

## What a skill is

A drafter. A skill produces a draft; a named human decides. Never run past the confirm
gate. A skill is a markdown file editable in one sitting; no prompt lives in code.

## Evidence binding (non-negotiable)

- **Every asserted claim carries at least one source reference.** No source, no claim.
- A source reference names the **source file exactly as supplied, extension included**,
  then the position within it ("transcript-sales.md, SPEAKER-4"). The promise under
  every citation is that a person can go and look. Never substitute what a source is
  about for what it is called: "the all-hands", "the SOP" and "the workshop" are
  descriptions, not files.
- **A quote must exist verbatim in the source it cites.** Quote verification is a
  check, not a courtesy.
- **A speaker label alone identifies nobody**: labels are assigned per file, so only
  the file name makes one mean anything.
- **Two citations of the same passage are one piece of evidence.** Never repeat a
  locator to make support look broader; indistinguishable citations inflate confidence
  in a claim only one person made.
- **Confidence is one shared scale**: high (corroborated by 2 or more independent
  sources, or a system timestamp), medium (a single credible source, uncontradicted),
  low (self-reported estimate, stale document, or a single unverified mention).
  Source type carries claimed/stated/measured semantics; confidence carries strength;
  they are independent.

## The consultant's own voice

- **Consultant speech is framing, never evidence.** Identify the consultant from the
  transcript's `participants:` and `speaker_labels:` frontmatter, never by assuming a
  label like "Me" is the consultant. Extract evidence only from non-consultant turns.
- **Instruct, do not strip.** The consultant's questions stay in view because they make
  the answers interpretable ("how long does that take?" gives "a day and a half" its
  meaning); they are context, never evidence.
- **The second-hand relay exception**: "they were showing me how they copy and paste"
  is the consultant speaking and is real client evidence, just indirect. Keep it, cited
  as the weaker evidence it is.
- **Reject first-person consultant claims** even when a speaker label is missing
  ("I bet", "it doesn't sound like", "we came up with").

## Source sub-types (declared, not inferred)

Different evidence classes, marked at intake: **discovery interview**,
**consultant-led session**, **client-shared summary**, **consultant recollection**.
Recollection written same-hour and marked as recollection is usable background;
**consultant recollection is refused as evidence**. A source whose speakers cannot be
attributed (no participants, no labels) is refused as a conversation source. A
client-shared summary of an unrecorded call outranks the consultant's memory of it.

## Real conversations, not summaries

A summarised corpus is a lossy corpus: a 2.5 KB summary of a 20 KB transcript loses
half the observations and most of the quantified statements. Ingest the real
conversations; a number said in passing is often the most valuable thing in the file.

## Names, roles and companies

- People appear by role, from a standard vocabulary (sponsor, CTO / engineering lead,
  finance lead, reviewer, operator...), extended by function plus seniority, never by
  name or initials.
- The name-to-role mapping lives outside every artefact, in the intake-side key. Never
  write the mapping into any output; that re-introduces the name and defeats the
  redaction.
- Seed name handling from each source's `participants:` frontmatter (authoritative,
  per source) rather than inference; the same person appears under short and long
  forms and as vocatives all through real speech, and a participants-seeded sweep
  alone has been seen to miss exactly those (a full name in passing, a "bye" with a
  first name attached). Sweep the speech, not the list.
- **Prospect and customer company names are tokenised at intake regardless** of any
  other choice: commercially sensitive, absent from participants lists, and the one
  case where the client seeing them is also a problem.
- **Tokenisation never matches numerics.** A pattern-matching tokeniser has been
  seen to eat a percentage (a figure became a token, and the evidence was
  destroyed). Numbers are never names; exclude digit spans from every token
  pattern, and audit each token in the registry once against a raw occurrence so a
  collision (one token absorbing two different things) is caught while the source
  is still at hand.
- **Check label adequacy per source at intake.** Some recorders separate the
  consultant from the room but conflate the client participants under one label,
  and some merge whole calls into one block. Record in the source ledger, per
  source, whether the labels separate the client speakers; where they do not,
  attribute claims only where content makes the speaker unambiguous, and mark the
  rest. Upstream, prefer one lead per booked call and recorder settings that label
  speakers individually; the cheapest attribution fix happens before the call.

## Omission is correct

- **Omitting what a source cannot know is correct, not a gap.** A single interview
  does not know it is describing step four of a stream; the assembled set settles
  sequence and boundaries. Never invent a value to satisfy a required-looking field:
  the three observed failures are inventing it, refusing the whole source, and
  silently dropping the evidence, and the third is the worst because nothing reports
  it.
- **A measurement carries a number or it does not exist.** Where a source evidences
  that something takes time but not how much, record that in prose with its source
  reference and say no number was given. Never invent a number to make a claim
  recordable; an unmeasured claim that stays visible is evidence.
- Timings carry their method: system timestamp (the only baseline-grade method),
  observed, self-reported, or estimated. A self-reported number is never presented as
  measured, and no baseline or win claim is built on one.

## Capture fields that earn their place

Per observation, when the source states them: **scale**, whose keys are exactly
`cadence`, `load` and `held_by` (who carries the work, and whether it is
concentrated; a headcount is a `load` or `held_by` fact), and
**stated_dependencies** (the speaker's own linkage, as a quote; not an
identity claim, resolution owns identity). These are where quantification and
connective reasoning are otherwise lost.

## Room-facing language

No process-engineering jargon in anything a client reads (no takt, PCE, value-add
ratio). Plain language: how long start to finish, working versus waiting, how often it
bounces back. Capture the room's own verbs as spoken; never impose a taxonomy.

## Failure behaviour

When sources are thin, stale or contradictory: say so, at low confidence, and surface
the gap. A visible "we do not know this yet" is worth more than a confident
fabrication; the exposure is part of the product.
