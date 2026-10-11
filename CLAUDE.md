# Working in this repo: instructions for Claude sessions

This is the AI Business Enablement kit: a consulting methodology as a repo (markdown
skills Claude executes, four deterministic Python tools, static templates). Read
`docs/ON-A-PAGE.md` for the one-page picture, `docs/ARCHITECTURE.md` for how it fits
together, `docs/QUICKSTART.md` to run anything.

## Hard rules

1. **Nothing client-identifying ever enters this repo**: no names, tokens, figures or
   quotes from any real engagement. The synthetic Caldergate fixture is the only
   engagement committed here. Live engagements run in workspaces outside the repo
   (`docs/workspace-layout.md`). Comparisons against the real replay may appear in
   `README.md` and `docs/results.md` only, with their caveats inline and never with
   anything that identifies the client.
2. **The thesis is binding: skills draft, tools check, the human decides.** Four
   tools, no more; a skill fits one sitting; no prompt lives in code. If a change
   fights those caps, the design is wrong (decision 0003), not the cap.
3. **Deterministic wherever a number is produced.** Counts derive in `facts.py`;
   artefacts read the manifest; nothing is typed loose. Every checker rule carries
   poison and clean fixtures or the self-test refuses to grade.
4. **The fixture is the regression surface.** Any change to a skill, tool, template
   or rule updates `fixtures/caldergate/` in the same change, and the toolchain
   rerun (`make demo`, or by hand: `check.py --self-test`, `check.py --observations`,
   `facts.py`, `workbook.py`, `check.py` on the fixture report, `pack.py` on a fresh
   version) must pass before committing. CI runs the same thing.
5. **Branch, then PR; never push to main.** Record deliberate design divergences as
   files in `docs/decisions/`, numbered on from the last.
6. **House style in every file**: British English, no em dashes anywhere, evidence
   before interpretation, roles never names. The kit must pass its own checker's
   ban list.
7. **Baselines are immutable** (fixture packs included): a change is the next
   version, and `pack.py`'s refusal to overwrite is load-bearing, not an
   inconvenience.
8. **Keep the kit neutral** (decision 0001): no firm names, palettes or exemplars in
   kit files; brandable surfaces stay tokenised, and skins supply the rest
   (`skins/README.md`).

## Map

| Path | What it holds |
|---|---|
| `taxonomy/` | The five enablers, controlled vocabulary, the 20-area instrument |
| `method/` | Engagement arc, session kit, where-to-start, governed distribution, hosting deep-dive, stage-arc rationale |
| `skills/` | `00_evidence-rules.md` (read first) and the six skills; schemas as specs |
| `tools/` | `facts.py`, `check.py`, `workbook.py`, `pack.py`, plus `rubric.md` (the judgement half, run by fresh eyes) |
| `templates/` | Report skeleton, map/brief HTML, diagrams, workbook spec, pack README and CLAUDE.md |
| `fixtures/caldergate/` | The synthetic worked engagement; its README lists what every source deliberately plants |
| `docs/` | Architecture, quickstart, on-a-page, workspace layout, decision log |
| `skins/` | How branding is applied without touching kit files |

## Useful entry points

- Change a rule safely: edit the skill or config, add fixtures, rerun the fixture
  end to end, update `fixtures/caldergate/README.md` if the planted cases changed.
- Run an engagement: `docs/QUICKSTART.md`, then the skills in stage-arc order with
  the human confirming at every gate.
- Understand a design choice: `docs/decisions/`, then `method/stage-arc.md` for the
  per-stage rationale.
