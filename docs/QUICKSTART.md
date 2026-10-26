# Quick start

## Prerequisites

- Python 3.10 or later with `openpyxl` (`pip install -r requirements.txt`). Nothing else
  is needed.
- A Claude Code session opened at this repo. The skills are prompt files that Claude
  carries out, and there is no other runtime.
- For a real engagement, a workspace folder OUTSIDE this repo (see
  `docs/workspace-layout.md`). Client material never enters the repo.

## See the whole thing work in ten minutes

The committed fixture is a complete worked engagement for Caldergate Freight, which is
invented. One command runs every tool against a throwaway copy of it and prints one line
per step.

```bash
make demo
```

You can also run the steps yourself, in order. Each one is a gate you would pass through
in a real engagement.

```bash
python3 tools/check.py --self-test
```

This proves that every lint rule fires on its poison fixture and stays silent on its
clean one. Nothing is graded until it passes.

```bash
python3 tools/check.py --observations fixtures/caldergate/workspace \
  --config fixtures/caldergate/workspace/check.config.json
```

This verifies the extraction outputs mechanically. It checks the following.

- Every quote exists verbatim in the source it cites, allowing for line-wrapping.
- Locators name real files.
- No registry name reaches a claim.
- Enums and shapes hold.
- Refused sources have no observations.
- No quote is drawn from a consultant turn, when speaker labels are configured in the
  config.

It has its own poison and clean self-test. The fixture's two planted name leaks inside
verbatim quotes show as warnings, by design. It cannot judge whether the right
observations were extracted. That stays with you.

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

The committed pack is V1, and baselines are immutable, so a rebuild has to be V2. If you
want a clean V1, delete `packs/` first. Pack zips are gitignored. Running `make demo`
avoids all of this, because it works in a temp directory. To see a deliverable, open a
map from `fixtures/caldergate/workspace/artefacts/maps/` in a browser. What every source
deliberately plants is explained in `fixtures/caldergate/README.md`.

## Running a real engagement

1. Read the playbook. Start with `method/engagement-arc.md`, which covers the shape and
   pacing, then read `method/session-kit.md` for the messages and session formats. Send
   the kickoff messages and book everything in week one.
2. Set up the workspace as `docs/workspace-layout.md` describes. Create
   `engagement.json` with the client name, consultancy and names list. Copy
   `tools/check.config.json` in and fill its `names` list. Create empty `sources/`,
   `intake/`, `observations/`, `data/` and `artefacts/` folders.
3. Take in each source as it arrives, following the intake rules in
   `skills/00_evidence-rules.md`. Seed the token registry from the participants,
   tokenise companies, declare a sub-type for each file and record in the source ledger
   whether the speaker labels are adequate. Refuse anything that cannot be attributed,
   and mark recollections as recollections.
4. Run the conversation layer. For each accepted source, have Claude run
   `skills/summarise-call.md` and `skills/extract-observations.md`. You confirm the
   observation set before anything is built on it. Before you read the set, fill
   `observation_checks` in the config with the consultant and client speaker labels and
   run
   `python3 tools/check.py --observations <workspace> --config <ws>/check.config.json`.
   It fails any quote that is not verbatim in its source, any registry name in a claim,
   and any quote taken from a consultant turn.
5. Rate readiness with `taxonomy/instrument/` (`skills/assess-readiness.md`), and
   examine directly what conversations never bring up, such as consoles, policies and
   permission grants. Then build the landscape with `skills/propose-opportunities.md`,
   confirm it at the gate, and write it to `data/landscape.json` and
   `data/readiness.json`.
6. Derive the numbers with `python3 tools/facts.py <workspace>`. Every figure that any
   artefact publishes either comes from `facts.json` or is added, with its context, to
   `verified_figures` in `engagement.json`. Nothing is ever typed in loose.
7. Build the artefacts. Maps and briefs come from `skills/draft-map.md` and
   `skills/draft-brief.md`, filled into the templates. The workbook comes from
   `python3 tools/workbook.py <workspace>`. You write the report yourself, on
   `templates/report-skeleton.md`. Put every prose artefact through
   `python3 tools/check.py <artefact> --config <ws>/check.config.json --facts <ws>/facts.json`,
   and run `tools/rubric.md` in a fresh session that did not write the draft.
8. Ship with `python3 tools/pack.py <workspace> --version 1`. The pack audits itself for
   stray names, unfilled slots and draft markers, and refuses to overwrite a baseline.
   Then book the choosing session (`method/where-to-start.md`).

The two-week fast path, including what it cuts and what it never cuts, is described in
`method/engagement-arc.md`.

## Rules that save you later

- Use real transcripts, not summaries. A summarised corpus loses the quantified
  statements.
- Never record a delivery status for an opportunity. The choosing session asks the teams
  instead.
- Every number is either derived or verified by the consultant with its context, and the
  checker flags anything it cannot trace.
- Baselines are immutable. A change becomes the next version, in a new folder.
- If a tool seems to need a subcommand tree, or a skill will not fit into one sitting,
  the design is wrong. See `docs/decisions/0003-intake-is-a-runbook-step.md`.
