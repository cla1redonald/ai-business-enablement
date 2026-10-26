# The Caldergate fixture

This is one engagement, invented from start to finish, that exercises every module in
the kit. The client is Caldergate Freight, an invented 140-person UK freight forwarder,
assessed by an invented consultant (Jordan Vale, Fieldnote Advisory) in September 2027.
Every person, company, tool, figure and date is fictional, and the tool names
(Loadstone, Ledgerline, Portwick, Filestead, Tallybook, Verrin) are meant to resemble no
real vendor. The fixture is the worked example of the whole flow, and it is also the
kit's regression surface. Update it with every module change, or the only real test left
is a private replay of a real engagement.

## What each source exercises

| Source | Test cases planted |
|---|---|
| `2027-09-20_kickoff-sponsor.md` | The sponsor's verbal picture of the company; a second-hand estimate that is later contradicted (the 20-minute quote); spend that is visible while the value is not |
| `2027-09-22_ops-team.md` | Timings people report for themselves; a bottleneck the consultant suggests, which must NOT become evidence (the lead's own weighing must); a second-hand relay confirmed in the room; a stranded prototype whose owner is unsure it was allowed; vocatives to tokenise |
| `2027-09-23_finance.md` | Operating data with nowhere to live; dashboards built on stale CSVs; a condition on controls that the speaker states |
| `2027-09-24_customer-service.md` | A first-person claim by the consultant, to be rejected ("I bet..."); the story of the abandoned assistant, which anchors the verification finding; a churn signal that is missing |
| `2027-09-27_sales.md` | A three-way contradiction (the sponsor's account against practice against the process doc); a deliberate limit on AI, with a stated condition |
| `2027-09-28_it.md` | Direct observation (the console review); the automation running on a laptop; coarse permissions named as the blocker; the pattern of two people holding all the capacity |
| `2027-09-29_customs-working-session.md` | The consultant-led session sub-type, where the demo is the consultant's work and the clerk's condition is the evidence |
| `doc_ai-usage-note.md` | A partial policy, with a strong clause, narrow coverage and no owner |
| `doc_quote-process.md` | A claim in a document that practice contradicts; an official process that depends on the laptop automation |
| `2027-09-30_allhands-clip.md` | Refused, because it has no participants and no speaker labels, so attribution is impossible |
| `note_recollection-carrier-call.md` | Refused as evidence. It is the consultant's recollection, written within the hour and marked as such, and used as background only |

## The worked run (committed in `workspace/`, apart from the pack zip)

The run goes from `intake/` (registry and source ledger) to `observations/` (47
observations tied to evidence), then to `data/landscape.json` (21 opportunities, 6
streams, 6 gaps) and `data/readiness.json` (20 areas). From there `tools/facts.py`
builds `facts.json`. Next come the `artefacts/`, which are the report on the skeleton, 7
tokenised summaries, 2 maps, 2 briefs and the workbook from `tools/workbook.py`. Last is
`packs/`, the audited baseline built by `tools/pack.py`. Its `.zip` is gitignored and
rebuilt by the tool, so only the unzipped folder is committed.

`check.config.json` is the engagement's copy of the lint config, with the fixture's
names list, and the report passes `check.py` with the facts manifest.

Some shapes are deliberate, and worth knowing about before you compare outputs.

- **No pain scores and no measured timings exist anywhere.** Every figure is
  self-reported, the maps say "pain scored on 0", and all four Proof areas are rated
  gap. That is an honest record of what these interviews captured, and nothing has been
  left out.
- **No area rates in place** (a 0/6/14 roll-up). This is a business that adopted AI
  person by person, and its mix is deliberately unlike any real engagement's.
- **Every stream carries at least one gap.** So the quick win is built from open
  opportunities on the handoffs rather than from a fully open stream, which tests how
  honestly the where-to-start kit handles a harder case rather than the easy one.

## Simplifications in v0.1 (recorded, not accidental)

- **The dates are invented.** The engagement window (September 2027) is later than the
  kit's own v0.1 build date and refers to no real period. File names and locators carry
  the dates, so they were left as they are rather than shifted.
- Sources are committed raw, fictional names included, and the observation quotes verify
  against them verbatim. Tokenisation applies to every artefact that can be shared, and
  it is enforced by the pack audit and the checker's names list. In a real engagement,
  `sources/` and `intake/registry.md` never enter any repo or pack.
- The report is markdown, because the fixture has no branded rendering pipeline. Layout
  QA on a rendered PDF is only exercised in real engagements.
