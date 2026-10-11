# The Caldergate fixture

One fully synthetic engagement exercising every module: Caldergate Freight, an
invented 140-person UK freight forwarder, assessed by an invented consultant (Jordan
Vale, Fieldnote Advisory) in September 2027. Every person, company, tool, figure and
date is fictional; the tool names (Loadstone, Ledgerline, Portwick, Filestead,
Tallybook, Verrin) are meant to resemble no real vendor. This fixture is the worked example of
the whole flow and the kit's regression surface: update it with every module change,
or a private replay of a real engagement becomes the only real test.

## What each source exercises

| Source | Test cases planted |
|---|---|
| `2027-09-20_kickoff-sponsor.md` | Sponsor's verbal company picture; a second-hand estimate later contradicted (the 20-minute quote); spend-visible-value-invisible |
| `2027-09-22_ops-team.md` | Quantified self-reported timings; a consultant bottleneck suggestion that must NOT become evidence (the lead's own weighing must); a second-hand relay confirmed in the room; a stranded prototype with stated permission uncertainty; vocatives to tokenise |
| `2027-09-23_finance.md` | The no-home-for-operating-data pattern; stale-CSV dashboards; a stated controls condition |
| `2027-09-24_customer-service.md` | A first-person consultant claim to reject ("I bet..."); the abandoned-assistant story that anchors verification; an absent churn signal |
| `2027-09-27_sales.md` | A three-way contradiction (sponsor vs practice vs process doc); a deliberate AI boundary with a stated condition |
| `2027-09-28_it.md` | Direct observation (the console review); the laptop automation; coarse permissions as the named blocker; the two-person capacity pattern |
| `2027-09-29_customs-working-session.md` | The consultant-led session sub-type: the demo is the consultant's work, the clerk's condition is the evidence |
| `doc_ai-usage-note.md` | A partial policy: strong clause, narrow coverage, no owner |
| `doc_quote-process.md` | A document claim contradicted by practice; an official process depending on the laptop automation |
| `2027-09-30_allhands-clip.md` | **Refused**: no participants, no speaker labels, attribution impossible |
| `note_recollection-carrier-call.md` | **Refused as evidence**: consultant recollection, same-hour, marked; background only |

## The worked run (committed in `workspace/`, apart from the pack zip)

`intake/` (registry, source ledger) → `observations/` (47 evidence-bound
observations) → `data/landscape.json` (21 opportunities, 6 streams, 6 gaps) and
`data/readiness.json` (20 areas) → `facts.json` (`tools/facts.py`) →
`artefacts/` (report on the skeleton, 7 tokenised summaries, 2 maps, 2 briefs,
workbook via `tools/workbook.py`) → `packs/` (`tools/pack.py`, audited baseline; the
`.zip` is gitignored and rebuilt by the tool, so only the unzipped folder is
committed).
`check.config.json` is the engagement copy of the lint config with the fixture's
names list; the report passes `check.py` with the facts manifest.

Deliberate shapes worth knowing before comparing outputs:

- **No pain scores and no measured timings exist anywhere**: every figure is self
  reported, the maps say "pain scored on 0", and Proof rates all-gap. That is the
  honest capture of these interviews, not an omission.
- **No area rates in place** (0/6/14 roll-up): a business that adopted person by
  person, different from any real engagement's mix by design.
- **Every stream carries at least one gap**, so the quick win is built from open
  opportunities on the handoffs rather than a fully open stream, exercising the
  where-to-start kit's honesty rather than its happy path.

## v0.1 simplifications (recorded, not accidental)

- **The dates are invented.** The engagement window (September 2027) is later than
  the kit's own v0.1 build date and refers to no real period. File names and
  locators carry the dates, so they were left as they are rather than shifted.

- Sources are committed raw (fictional names included) and observation quotes verify
  against them verbatim; tokenisation applies to every shareable artefact and is
  enforced by the pack audit and the checker's names list. In a real engagement,
  `sources/` and `intake/registry.md` never enter any repo or pack.
- The report is markdown (no branded-render pipeline in the fixture); layout QA on a
  rendered PDF is exercised only in real engagements.
