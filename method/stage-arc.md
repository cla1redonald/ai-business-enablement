# The stage arc and what the earlier pipeline taught

The reference pipeline proved a processing arc of six stages: **intake → observe →
resolve and confirm → landscape → converge → export**. The order is right, and each
boundary between stages earned its place. The machinery that implemented it has not been
carried over. This file gives one section per stage, covering what the stage does, what
the reference implementation got right, what made it hard to update, and what v0.1
builds instead. Where v0.1 disagrees with the reference, v0.1 wins, and any deliberate
divergence is recorded in the repo's decision log.

Some engineering ideas apply to every stage. Privacy is enforced at intake. A person
confirms the work between stages. Each source is fingerprinted, so unchanged work is
never redone. And any number that is produced comes from deterministic code. The work is
divided on a simple basis. A stage that needs judgement is a skill, and a stage that has
to give the same answer every time is a script. Every stage should be readable and
editable in one sitting, and if changing a prompt means changing code, the stage is
wrong.

## 1. Intake

**What it does.** Sources arrive as transcripts and documents. Each one gets its privacy
treatment, its metadata and its identity. Participants and speaker labels are read from
the frontmatter, the source's sub-type is declared (discovery interview, consultant-led
session, client-shared summary or consultant recollection), companies are tokenised, and
a fingerprint is recorded for the source.

**Got right.** Privacy was handled at the boundary, so nothing further down could leak
by accident. The participants frontmatter served as the authoritative registry of names.
Each source had a fingerprint. Sources whose speakers could not be attributed were
refused.

**Hard to update.** The workdir mechanics were monolithic. Tokenisation lived partly
outside the tool, and transcripts were far heavier to tokenise than summaries. The
choice between redacting at ingest and checking at export was never fully settled.
Tokens had caused a real misattribution error, but checking at export is only as strong
as the number of export paths, and nobody had counted them.

**v0.1.** Intake is a runbook step rather than a fifth tool (decision 0003). The token
registry is seeded from the participants frontmatter, companies are always tokenised,
and every file has to declare its sub-type, all done in the session under the evidence
rules. A person declares sub-types and settles anything ambiguous. Bookkeeping for each
source takes the place of fingerprints. If a source has not changed it keeps its
observation file, so unchanged work is never redone. Under the names policy (decision
0002), anything shareable uses tokens. That is enforced twice, at intake for companies
and participants and by the checker at export, so the kit does not depend on a single
boundary holding.

## 2. Observe

**What it does.** It reads each source and extracts observations tied to evidence. Each
observation is a claim with a verbatim quote, a source reference, scale, held_by and any
dependencies the speaker stated.

**Got right.** It bound evidence to claims and verified the quotes. Nothing had ever
checked that quotes existed until this stage did, and when it started it found real
holes. It kept the rule on consultant speech. It used real transcripts rather than
summaries, because the summarised corpus lost three quarters of the quantified
statements. It processed one source at a time, so in principle the work could grow in
small steps.

**Hard to update.** The observer spec was written for summaries, and it skimmed over the
numbers in transcripts. Any schema change invalidated every observation, so spec changes
had to land before ingests, or the run was paid for twice. Full rebuilds meant that
growing the corpus cost about 85 minutes of re-observing sources that had not changed.
The prompts lived inside the code.

**v0.1.** Observe is a skill (`skills/extract-observations.md`), run one source at a
time under the evidence rules, and the fingerprint ledger (a script) skips sources that
have not changed. The skill is a markdown file, so changing the spec is an edit, not a
build. Observations from sources already processed are only extracted again when the
skill changes materially, and that is a person's decision, never an automatic
invalidation.

## 3. Resolve and confirm

**What it does.** It works out identity across observations, such as the same process
described twice or the same opportunity heard three different ways. It proposes merges
and surfaces conflicts. Then comes the human gate, where the consultant confirms the
observation set before anything is built on it.

**Got right.** The confirm gate itself. It treated corrections from the operator as part
of the main flow, and grade overrides were used live 28 times. It surfaced disputed
boundaries as explicit, named decisions rather than picking one quietly.

**Hard to update.** An all-pairs resolver was specified, but its input kept changing
underneath it. Most groups turned out to have a single member, and the few real merges
were found by hand in one evening. The operator's corrections did not reliably reach the
outputs. Results varied from one run to the next, so conclusions could not be repeated.

**v0.1.** A skill drafts merge and conflict proposals with the evidence side by side,
and a person decides. A small script records the decisions so they survive rebuilds and
can be shown to reach every output. A correction that never reaches the artefact was the
defect that hurt most. There is no all-pairs machinery. At the scale of one engagement,
a skill that proposes plus one evening of judgement does better than a resolver that has
to be retuned for every corpus.

## 4. Landscape

**What it does.** It builds the opportunity landscape. Each opportunity gets an ID,
functions, the streams it belongs to, impact and effort grades, quantified figures, and
the enabling gaps it waits on. The value streams themselves are proposed and confirmed,
and the readiness instrument runs alongside.

**Got right.** It graded impact at stream level. It drew the distinction between gated
and open, with counts of the opportunities waiting on each gap, and that is the bridge
that turns a diagnosis into a sequence. It avoided composite scores, counted by
share-weighting, and graded with discipline (no tools, and model calls kept under
control).

**Hard to update.** The enabler pass ran once over the whole corpus as one giant prompt,
which was expensive, unstable and impossible to review. Grades were capped when
quantification was missing, when the real cause was a loss at the observe stage. Full
rebuilds were expensive here as well.

**v0.1.** A skill (`skills/propose-opportunities.md`) drafts each entity against the
confirmed observations, and the `facts` script owns every count, so every number comes
from deterministic code. The readiness instrument runs as its own skill
(`skills/assess-readiness.md`) against the taxonomy. Nothing is run as a single call
over the whole corpus. The work is bounded by stream, by gap and by area, so a re-run
touches one entity.

## 5. Converge

**What it does.** It goes deeper on the chosen few. It draws step-level maps for the
streams that matter, writes briefs for the gaps that gate them, and proposes the routes
worth testing.

**Got right.** The formats of the shipped artefacts (the map and the brief) serve as the
spec. It made the call on each constraint with evidence and corroboration, and was
honest about what had not been measured. The briefs framed a decision before anything
was built.

**Hard to update.** Deep maps were assembled by hand in working directories, with
scratch scripts doing the consistency work. Nothing could be regenerated, and every edit
to the narrative meant recounting figures by hand across five places.

**v0.1.** Skills (`skills/draft-map.md`, `skills/draft-brief.md`) draft into the
templates, and every figure is read from the facts manifest. Regenerating is a rebuild
rather than a dig through old working files. The fast path only converges the top 3 to 5
streams and the gaps that gate the top opportunities.

## 6. Export

**What it does.** It produces the set the client receives. That is the report (prose
written by a person on the generated skeleton and facts), the workbook, maps, briefs,
summaries, diagrams and indexes, and the versioned pack with its README and a CLAUDE.md
written for the client's AI.

**Got right.** It treated the pack as an artefact with checks of its own. It kept the
baseline immutable, and it gave the client's AI its own CLAUDE.md. It had a prose
checker for each engagement, and a judgement rubric run by fresh eyes. Layout QA on
rendered pages found problems the checkers could not.

**Hard to update.** Nearly everything the client received was assembled by hand. Joins
on display text silently broke 31 workbook cells. Renames had to be carried across five
places by hand. The round trip for publishing lived in scratch scripts that were rebuilt
from memory each session, and the facts sheet was maintained by hand.

**v0.1.** Scripts own export from start to finish. The `facts` script builds the
manifest with provenance, `check` handles lint, budgets, figures and layout, and
`workbook` builds from the data and joins by stable ID. Then `pack` produces the folder,
zip, audit, README and CLAUDE.md as immutable baselines that can be loaded again as the
start of the next engagement. A person writes the report prose on the skeleton, and the
tools verify it but never write it. The computed report was replaced wholesale and
nobody missed it, so that question is closed.
