# AI Business Enablement kit

Most organisations want to use AI and cannot say where to start. This kit runs a
two-week diagnostic that turns interviews and documents into a readiness rating, a short
list of root causes and a starting portfolio that the leadership team picks for itself.
Every observation is tied to a quote taken word for word from its source. Scripts check
the numbers, and a consultant confirms the output of each stage before the next one
begins. Run `make demo` to watch it work on an invented freight company, which takes
about a minute.

My first version was a heavy six-stage pipeline. It worked until I wanted to change
something, and then every change broke something else. A real engagement then showed me
that the method and the deliverables were what mattered, far more than the machinery.
The deliverables were observations tied to evidence, a readiness rating on a fixed
instrument, maps and briefs showing where work is held up, and a pack the client's own
AI can find its way around. This kit is the rebuild, with as little machinery as I could
get away with.

The work is split three ways. Six markdown skills do the drafting, and Claude carries
them out under strict evidence rules. Four small Python scripts check, count and build.
A person confirms the result at every gate. There is no app, no server and no database.

## What a replay showed

I replayed the real engagement through the rebuild, on the same confidential material.
The rebuild produced 438 observations, and every quote in them was found word for word
in its source. The earlier pipeline produced 212. The rebuild also matched the 20-area
readiness ratings, with the earlier grid in context.

The two observation counts do not measure recall on equal terms. The rebuild splits
evidence more finely, and how much of the gap comes from that has not been quantified.
The readiness replay was not blind. It is also one engagement, and it cannot be
reproduced here. [docs/results.md](docs/results.md) sets out each caveat in full.

## Run the demo in 60 seconds

You need Python 3.10 or later and `openpyxl`.

```bash
pip install -r requirements.txt
make demo
```

The demo runs every tool in the kit on the fixture engagement. The client is Caldergate
Freight, an invented 140-person UK freight forwarder, and the consultant is invented
too. Every person, company, tool, figure and date in it is made up. The demo works on a
temporary copy, so your checkout is left as it was. You should see this.

```
[ ok ] self-test              19 rules and budgets each proved against a poison and a clean fixture
[ ok ] observations check     9 files, 47 observations: 0 failure(s), 2 warning(s). Mechanical checks pass.
[ ok ] facts                  facts: 21 opportunities, 6 streams (4 high, 2 medium), 6 gaps, 13 gated, ...
[ ok ] facts vs committed     regenerated facts.json is identical to the committed file
[ ok ] workbook               workbook.xlsx built, 4 sheets
[ ok ] check report           Deterministic checks pass.
[ ok ] pack                   baseline V1 built and audited clean, zipped (temp dir, removed on exit)
```

The two warnings are planted on purpose. Each is a name left inside a verbatim quote,
which the check is there to flag. To see a deliverable, open one of the maps in
`fixtures/caldergate/workspace/artefacts/maps/` in a browser.
`fixtures/caldergate/README.md` lists what each source has planted in it.

## What is in the box

| Path | What it holds |
|---|---|
| `taxonomy/` | The five enablers, the controlled vocabulary and its term rules, and the 20-area readiness instrument you run with a client (one file per enabler, plus a guide to running it) |
| `method/` | How an engagement runs: the engagement arc and the faster two-week version, the session kit (kickoff messages, discovery calls, drop-ins, the fictional sandbox for demos), the where-to-start kit (two decisions, waves, the quick win, six questions, and what not to do), governed distribution (the review gate and verification pattern), the hosting and identity deep-dive, and the reasoning behind each stage |
| `templates/` | The report skeleton with drafting guidance, the HTML for value-stream maps and enabling-gap briefs, the workbook spec, the pack README and the CLAUDE.md written for the client's AI, and five diagrams that fill from engagement data |
| `skills/` | The evidence rules and the six skills: summarise-call, extract-observations, propose-opportunities, assess-readiness, draft-map and draft-brief. Their schemas are kept as specs in `skills/schemas/` |
| `tools/` | Four scripts that give the same output for the same input every time, and the kit will not grow a fifth. `facts` builds the manifest, `check` lints prose and verifies budgets, figures, layout and observations after testing itself, `workbook` builds the xlsx and `pack` builds each versioned baseline. Alongside them is `rubric.md`, for the checks that need judgement |
| `fixtures/` | One engagement, invented from start to finish (company, people and transcripts), that exercises every part of the kit. No client material, ever |
| `skins/` | How a firm's branding is applied without touching the kit |
| `docs/` | The architecture with diagrams, the quickstart, the kit on one page, the results, and the decision log in `docs/decisions/` |

## How I know it works

The checker tests itself before it grades anything. Every lint rule in
`tools/check.config.json` comes with a poison fixture that must trigger it and a clean
fixture that must not. If any rule fails either test, `check.py` refuses to grade at
all. I built it this way because an earlier checker reported passes for weeks while
testing nothing, and that kind of checker is worse than none, since it gives you
confidence you have not earned.

The observations check verifies the evidence mechanically.
`python3 tools/check.py --observations <workspace>` reads every extraction output and
fails it in three cases.

- A quote cannot be found verbatim in the source it cites. Whitespace is normalised
  first, so a hard-wrapped transcript still matches on the words.
- A quote comes from the consultant's own turn. What the consultant says never counts as
  evidence.
- A name from the registry appears in a claim, scale or dependency. Inside a verbatim
  quote it only produces a warning, because the quote is the source's own words.

It also checks locators, enums, duplicate ids and refused sources. It has its own pair
of poison and clean workspaces, and each poison case has to trip the check on its own.
It cannot judge whether the *right* observations were extracted. That stays with a
human.

Every number in a deliverable is derived. `tools/facts.py` builds the manifest of
figures, and `check.py` flags any figure in a deliverable that it cannot trace back to
the manifest, so that a person can confirm it.

CI keeps the fixture honest. On every push and pull request, GitHub Actions runs the
demo on Python 3.12 and compares the regenerated `facts.json` with the committed file,
so the fixture cannot drift away from what the tools produce.

## The method in brief

1. **Discover.** The consultant holds conversations and collects documents. Every
   opportunity anyone mentions is recorded as an observation, with a verbatim quote and
   a reference to its source. Nothing is invented.
2. **Assess.** Readiness is rated on a fixed instrument of 20 areas, four for each
   enabler. Each area is rated in place, partial, gap or blocked.
3. **Bridge.** However many opportunities there are, they come down to a handful of root
   causes, and five enablers clear those causes. The usual finding is that leaders want
   more uses for AI than they have the groundwork to deliver.
4. **Choose.** In one session, the leadership team works through six questions against
   its own workbook and picks a starting portfolio.

To run a real engagement, start with `method/engagement-arc.md` and
[docs/QUICKSTART.md](docs/QUICKSTART.md). A live engagement runs in a workspace outside
this repo (`docs/workspace-layout.md`), and client material never enters the repo. For
the kit on a single page, read [docs/ON-A-PAGE.md](docs/ON-A-PAGE.md). For how the parts
fit together, read [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md). Agent sessions start at
[CLAUDE.md](CLAUDE.md).

## Licence

The code (`tools/`, `demo.sh` and CI) is MIT licensed. See [LICENSE](LICENSE). The
method, skills, taxonomy, templates and fixture are licensed CC BY 4.0. See
[LICENSE-METHOD.md](LICENSE-METHOD.md).
