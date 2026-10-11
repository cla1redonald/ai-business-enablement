# The stage arc: context, not constraint

The reference pipeline proved a six-stage processing arc: **intake → observe → resolve
and confirm → landscape → converge → export**. The order is right and each boundary
earned its place; the machinery that implemented it is not carried. One page per stage:
what it does, what the reference implementation got right, what made it hard to update,
and what v0.1 builds instead. Where v0.1 disagrees with the reference, v0.1 wins;
record deliberate divergences in the repo's decision log.

The engineering ideas that stay everywhere: privacy enforced at intake, human confirm
gates between stages, fingerprinting so unchanged work is never redone, and
deterministic outputs wherever a number is produced. The division of labour: a stage
that needs judgement is a skill; a stage that needs determinism is a script; a stage
should be readable and editable in one sitting, and if changing a prompt means changing
code, that stage is wrong.

## 1. Intake

**What it does.** Sources arrive (transcripts, documents), get their privacy treatment,
their metadata, and their identity: participants and speaker labels read from
frontmatter, source sub-type declared (discovery interview, consultant-led session,
client-shared summary, consultant recollection), companies tokenised, a fingerprint
recorded per source.

**Got right.** Privacy at the boundary, so nothing downstream can leak by accident.
The participants frontmatter as the authoritative name registry. Fingerprints per
source. Refusing sources whose speakers cannot be attributed.

**Hard to update.** Monolithic workdir mechanics; tokenisation lived partly outside
the tool and transcripts were far heavier to tokenise than summaries; the
redact-at-ingest versus check-at-export decision never fully landed (tokens caused a
real misattribution error, but check-at-export is only as strong as the number of
export paths, and nobody had counted them).

**v0.1.** A runbook step, not a fifth tool (decision 0003): token registry seeded from
participants frontmatter, company tokenisation always, sub-type declaration required
per file, all done in-session under the evidence rules. The human declares sub-types
and rules on ambiguity. Per-source bookkeeping stands in for fingerprints: a source
unchanged keeps its observation file, so unchanged work is never redone. Names policy
(decision 0002): tokens in anything shareable, enforced both at intake (companies,
participants) and by the checker at export (defence in depth rather than a bet on one
boundary).

## 2. Observe

**What it does.** Reads each source and extracts evidence-bound observations: claims
with verbatim quotes, source references, scale, held_by, stated dependencies.

**Got right.** Evidence binding with quote verification (nothing ever checked quotes
existed until it did, and it found real holes). The consultant-speech rule. Real
transcripts over summaries: the summarised corpus lost three quarters of the
quantified statements. Per-source processing, so growth is incremental in principle.

**Hard to update.** The observer spec was written for summaries and skimmed
transcripts' numbers; schema changes invalidated every observation, so spec changes
had to land before ingests or the run was paid for twice; full rebuilds made corpus
growth cost ~85 minutes of re-observing unchanged sources; prompts lived inside code.

**v0.1.** A skill (`skills/extract-observations.md`), one source at a time, under the
evidence rules; the fingerprint ledger (script) skips unchanged sources. The skill is
a markdown file, so a spec change is an edit, not a build; observations from
already-processed sources are only re-extracted when the skill materially changes,
and that is a human call, not an automatic invalidation.

## 3. Resolve and confirm

**What it does.** Identity across observations (the same process described twice, the
same opportunity heard three ways), merges proposed, conflicts surfaced, and the human
gate: the consultant confirms the observation set before anything is built on it.

**Got right.** The confirm gate itself; operator corrections as first-class
(grade overrides used live 28 times); surfacing contested boundaries as explicit named
decisions rather than silent picks.

**Hard to update.** An all-pairs resolver was speced but its input kept changing
underneath it; most groups were singletons and the few real merges were found by hand
in one evening; operator corrections did not reliably reach outputs; cross-run
instability made conclusions unrepeatable.

**v0.1.** A skill drafts merge and conflict proposals with the evidence side by side;
the human decides; a small script records decisions so they survive rebuilds and
provably reach every output (a correction that does not reach the artefact is the
defect that hurt most). No all-pairs machinery: at engagement scale, a proposing skill
plus one evening of judgement beats a resolver that must be re-tuned per corpus.

## 4. Landscape

**What it does.** Builds the opportunity landscape: opportunities with IDs, functions,
stream memberships, impact and effort grades, quantified figures, gates against
enabling gaps; the value streams themselves proposed and confirmed; the readiness
instrument run alongside.

**Got right.** Stream-level impact grading; the gated/open distinction and
opportunities-waiting counts (the bridge that turns diagnosis into sequence); no
composite scores; share-weighted counting; the grading posture (tools off, model calls
disciplined).

**Hard to update.** The whole-corpus single-call enabler pass (one giant prompt over
everything, expensive, unstable, unreviewable); grades capped on missing
quantification that was really an observe-stage loss; full-rebuild economics again.

**v0.1.** A skill (`skills/propose-opportunities.md`) drafts per entity against the
confirmed observations; the `facts` script owns every count (deterministic wherever a
number is produced); the readiness instrument runs as its own skill
(`skills/assess-readiness.md`) against the taxonomy. No whole-corpus single calls:
work is bounded per stream, per gap, per area, so a re-run touches one entity.

## 5. Converge

**What it does.** Deepens the chosen few: step-level maps for the streams that matter,
briefs for the gaps that gate them, proposals for the routes worth testing.

**Got right.** The shipped artefact formats (map, brief) are the spec; the constraint
call with evidence, corroboration and honesty about what is unmeasured;
decision-before-build framing in briefs.

**Hard to update.** Deep maps were hand-assembled in working directories with scratch
scripts doing the consistency work; nothing regenerated; every narrative edit
recounted figures by hand across five surfaces.

**v0.1.** Skills draft (`skills/draft-map.md`, `skills/draft-brief.md`) into the
templates; every figure reads from the facts manifest; regeneration is a rebuild, not
an archaeology dig. The fast path converges only the top 3 to 5 streams and the gaps
that gate the top opportunities.

## 6. Export

**What it does.** The client-facing set: report (human-written prose on the generated
skeleton and facts), workbook, maps, briefs, summaries, diagrams, indexes, the
versioned pack with README and agent-facing CLAUDE.md.

**Got right.** The pack as an artefact with its own checks; the immutable baseline;
the agent-facing CLAUDE.md; the per-engagement prose checker and
the judgement rubric run by fresh eyes; layout QA on rendered pages found what
checkers could not.

**Hard to update.** Nearly everything the client received was hand-assembled; joins
on display text broke 31 workbook cells silently; renames swept five surfaces by
hand; the publish round-trip lived in scratch scripts rebuilt from memory each
session; the facts sheet was hand-maintained.

**v0.1.** Scripts own it end to end: `facts` (the manifest with provenance), `check`
(lint, budgets, figures, layout), `workbook` (built from data, joined by stable ID),
`pack` (folder, zip, audit, README, CLAUDE.md, immutable baselines, re-loadable as
the next engagement's start). The report prose is written by the human on the
skeleton; the tools verify it and never write it. The computed report was replaced
wholesale and unmissed; that lesson is final.
