# AI Business Enablement kit

**Skills draft, tools check, the human decides.**

Most organisations want to use AI and cannot say where to start. This kit runs a
two-week diagnostic that turns interviews and documents into a readiness rating, a
short list of root causes and a picked starting portfolio. Every observation is tied
to a verbatim quote, scripts check the numbers, and a consultant confirms each stage.
Run `make demo` to see it work on an invented freight company in about a minute.

My first version was a heavy six-stage pipeline, and it worked until I wanted to
change anything: every change broke something else. A real engagement then showed me
that the method and the artefacts were the product, not the machinery: evidence-bound
observations, a readiness rating on a fixed instrument, maps and briefs that show where
the work waits, and a pack the client's own AI can navigate. This is the lean rebuild.

Six markdown skills draft (Claude executes them under strict evidence rules). Four
small Python scripts check, count and build. A human confirms at every gate. No app,
no server, no database.

## What a replay showed

I replayed the real engagement through the rebuild, on the same confidential corpus.
It produced 438 observations, each quote found verbatim in its source, against 212
from the earlier pipeline, and it matched the 20-area readiness ratings, with the
earlier grid in context.

This is not a like-for-like recall measure: the rebuild splits evidence more finely,
and the gap is not quantified. The readiness replay was not blind, and it is one
engagement that cannot be reproduced here. The caveats are spelled out in
[docs/results.md](docs/results.md).

## Run the demo in 60 seconds

You need Python 3.10 or later and `openpyxl`.

```bash
pip install -r requirements.txt
make demo
```

The demo runs the whole toolchain on the fixture engagement: Caldergate Freight, an
invented 140-person UK freight forwarder, assessed by an invented consultant. Every
person, company, tool, figure and date in it is made up. It works in a temp copy, so
your checkout stays clean. You should see:

```
[ ok ] self-test              19 rules and budgets each proved against a poison and a clean fixture
[ ok ] observations check     9 files, 47 observations: 0 failure(s), 2 warning(s). Mechanical checks pass.
[ ok ] facts                  facts: 21 opportunities, 6 streams (4 high, 2 medium), 6 gaps, 13 gated, ...
[ ok ] facts vs committed     regenerated facts.json is identical to the committed file
[ ok ] workbook               workbook.xlsx built, 4 sheets
[ ok ] check report           Deterministic checks pass.
[ ok ] pack                   baseline V1 built and audited clean, zipped (temp dir, removed on exit)
```

The two warnings are planted: a name leaking inside a verbatim quote, which the check
is meant to flag. Open a map from `fixtures/caldergate/workspace/artefacts/maps/` in a
browser to see a deliverable. `fixtures/caldergate/README.md` lists what every source
deliberately plants.

## What is in the box

| Path | What it holds |
|---|---|
| `taxonomy/` | The five enablers, the controlled vocabulary and term rules, and the runnable 20-area readiness instrument (one file per enabler plus how to run it) |
| `method/` | The engagement arc and fast-path frame, the session kit (kickoff messages, discovery calls, drop-ins, the fictional sandbox pattern), the where-to-start kit (two decisions, waves, quick win, six questions, don'ts), governed distribution (review gate and verification pattern), the hosting and identity deep-dive, and the stage-arc rationale |
| `templates/` | The report skeleton with drafting guidance, the value-stream map and enabling-gap brief HTML, the workbook spec, the pack README and agent-facing CLAUDE.md, and five parameterised diagrams |
| `skills/` | The evidence rules and the six skills: summarise-call, extract-observations, propose-opportunities, assess-readiness, draft-map, draft-brief. Schemas carried as specs in `skills/schemas/` |
| `tools/` | Four deterministic scripts, no more: `facts` (the manifest), `check` (lint, budgets, figures, layout, observations; self-testing), `workbook` (xlsx builder), `pack` (versioned baseline builder). Plus the judgement `rubric.md` |
| `fixtures/` | One fully synthetic engagement (an invented company, invented transcripts) exercising every module. No client material, ever |
| `skins/` | How a context's branding is applied without touching the kit |
| `docs/` | Architecture (with diagrams), quickstart, the one-page explanation, results, and the decision log in `docs/decisions/` |

## How I know it works

**The checker tests itself first.** Every lint rule in `tools/check.config.json`
carries a poison fixture that must trigger it and a clean fixture that must not. If
any rule fails either test, `check.py` refuses to grade anything. A checker that
cannot fail is worse than no checker, because it hands you false assurance.

**The observations check verifies evidence mechanically.**
`python3 tools/check.py --observations <workspace>` reads every extraction output and
fails it if:

- a quote does not exist verbatim in its cited source (whitespace-normalised, so
  hard-wrapped transcripts still match on the words);
- a quote sits inside a consultant's turn, because the consultant's own words never
  count as evidence;
- a name from the registry appears in a claim, scale or dependency (inside a verbatim
  quote it only warns, since the quote is the source's own words).

It also checks locators, enums, duplicate ids and refused sources, and it has its own
poison and clean workspace pair, with each poison case required to trip individually.
It cannot judge whether the *right* observations were extracted. That stays with a
human.

**Every number is derived.** `tools/facts.py` builds the manifest; `check.py` flags
any figure in a deliverable it cannot trace to it, for a human to confirm.

**CI keeps the fixture honest.** On every push and pull request, GitHub Actions runs
the demo on Python 3.12 and diffs the regenerated `facts.json` against the committed
file, so the fixture cannot drift from the tools.

## The method in brief

1. **Discover.** Conversations and documents in; every opportunity heard is recorded
   as an observation with a verbatim quote and a source reference. Nothing invented.
2. **Assess.** A 20-area readiness instrument, four areas per enabler, each rated in
   place, partial, gap or blocked.
3. **Bridge.** The many opportunities reduce to a handful of root causes, cleared by
   five enablers. Leaders want more AI use cases than they have the groundwork to deliver.
4. **Choose.** Leadership runs six questions against their own workbook in one
   session and picks a starting portfolio.

To run a real engagement, start with `method/engagement-arc.md` and
[docs/QUICKSTART.md](docs/QUICKSTART.md). Live engagements run in a workspace outside
this repo (`docs/workspace-layout.md`); client material never enters it. The one-page
version is [docs/ON-A-PAGE.md](docs/ON-A-PAGE.md); how it fits together is
[docs/ARCHITECTURE.md](docs/ARCHITECTURE.md). Agent sessions start at
[CLAUDE.md](CLAUDE.md).

## Licence

Code (`tools/`, `demo.sh`, CI) is MIT: see [LICENSE](LICENSE). The method, skills,
taxonomy, templates and fixture are CC BY 4.0: see
[LICENSE-METHOD.md](LICENSE-METHOD.md).
