# Quick start

## Prerequisites

- Python 3.10 or later with `openpyxl` (`pip install -r requirements.txt`); nothing
  else.
- A Claude Code session opened at this repo (the skills are prompt files Claude
  executes; there is no other runtime).
- For a real engagement: a workspace folder OUTSIDE this repo (see
  `docs/workspace-layout.md`). Client material never enters the repo.

## Ten minutes: see the whole thing work

The committed fixture is a complete worked engagement (Caldergate Freight, invented).
One command runs the whole toolchain against a throwaway copy of it and prints a line
per step:

```bash
make demo
```

Or run the steps yourself, in order. Each one is a real gate in an engagement:

```bash
python3 tools/check.py --self-test
```

Proves every lint rule can fire on its poison fixture and stay silent on its clean one,
before anything is graded.

```bash
python3 tools/check.py --observations fixtures/caldergate/workspace \
  --config fixtures/caldergate/workspace/check.config.json
```

Mechanically verifies the extraction outputs: every quote exists verbatim in its cited
source (modulo line-wrapping), locators name real files, no registry name reaches a
claim, enums and shapes hold, refused sources have no observations, and no quote is
drawn from a consultant turn (when speaker labels are configured in the config). It
has its own poison and clean self-test. The fixture's two planted name leaks inside
verbatim quotes show as warnings, by design. It cannot judge whether the right
observations were extracted; that stays with you.

```bash
python3 tools/facts.py fixtures/caldergate/workspace
```

```bash
python3 tools/workbook.py fixtures/caldergate/workspace
```

```bash
python3 tools/check.py fixtures/caldergate/workspace/artefacts/report.md --config fixtures/caldergate/workspace/check.config.json --facts fixtures/caldergate/workspace/facts.json
```

```bash
python3 tools/pack.py fixtures/caldergate/workspace --version 2
```

(The committed pack is V1 and baselines are immutable, so a rebuild is V2; delete
`packs/` first if you want a clean V1. Pack zips are gitignored.) `make demo` avoids
all of this by working in a temp directory. Open a map from
`fixtures/caldergate/workspace/artefacts/maps/` in a browser to see a deliverable.
`fixtures/caldergate/README.md` explains what every source deliberately plants.

## Running a real engagement

1. **Read the playbook**: `method/engagement-arc.md` (the shape and pacing), then
   `method/session-kit.md` (the messages and session formats). Send the kickoff
   messages and book everything in week one.
2. **Set up the workspace** per `docs/workspace-layout.md`: `engagement.json`
   (client name, consultancy, names list), copy `tools/check.config.json` in and
   fill the `names` list, empty `sources/`, `intake/`, `observations/`, `data/`,
   `artefacts/` folders.
3. **Intake each source** as it arrives, following the intake rules in
   `skills/00_evidence-rules.md`: participants-seeded token registry, company
   tokens, sub-type declared per file, label adequacy recorded in the source
   ledger. Refuse what cannot be attributed; mark recollections as recollections.
4. **Run the conversation layer**: for each accepted source, have Claude run
   `skills/summarise-call.md` and `skills/extract-observations.md`. You confirm
   the observation set before anything builds on it.
   Then run `python3 tools/check.py --observations <workspace> --config
   <ws>/check.config.json` (fill `observation_checks` with the consultant and client
   speaker labels) before you read the set: it fails any quote that is not verbatim
   in its source, any registry name in a claim, and any quote taken from a consultant
   turn.
5. **Rate readiness** with `taxonomy/instrument/` (`skills/assess-readiness.md`),
   examining directly what conversations never surface (consoles, policies,
   permission grants). **Build the landscape** with
   `skills/propose-opportunities.md`; confirm it at the gate; write it to
   `data/landscape.json` and `data/readiness.json`.
6. **Derive the numbers**: `python3 tools/facts.py <workspace>`. Every figure any
   artefact publishes comes from `facts.json` or is added to `engagement.json`'s
   `verified_figures` with its context, never typed loose.
7. **Build the artefacts**: maps and briefs via `skills/draft-map.md` and
   `skills/draft-brief.md` into the templates; the workbook via
   `python3 tools/workbook.py <workspace>`; the report written BY YOU on
   `templates/report-skeleton.md`. Gate every prose artefact through
   `python3 tools/check.py <artefact> --config <ws>/check.config.json --facts
   <ws>/facts.json`, and run `tools/rubric.md` through a fresh session that did
   not write the draft.
8. **Ship**: `python3 tools/pack.py <workspace> --version 1`. The pack audits
   itself (stray names, unfilled slots, draft markers) and refuses to overwrite a
   baseline. Book the choosing session (`method/where-to-start.md`).

The two-week fast path (what it cuts and what it never cuts) is in
`method/engagement-arc.md`.

## Rules that save you later

- Real transcripts in, not summaries; a summarised corpus loses the quantified
  statements.
- No delivery statuses per opportunity, ever; the choosing session asks the teams.
- Numbers are derived or consultant-verified with context; the checker flags
  anything it cannot trace.
- Baselines are immutable: changes are the next version, in a new folder.
- If a tool wants a subcommand tree or a skill will not fit one sitting, the
  design is wrong; see `docs/decisions/0003-intake-is-a-runbook-step.md`.
