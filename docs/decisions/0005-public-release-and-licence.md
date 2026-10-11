# 0005: Public release, with a split licence

**Recorded 2026-10-11 in the public-release PR; confirmed by merging it.** The kit is
published as a portfolio piece. This settles the question 0004 deferred.

- **Code is MIT** (`LICENSE`): `tools/`, `demo.sh`, the `Makefile` and CI.
- **Method and templates are CC BY 4.0** (`LICENSE-METHOD.md`): `method/`,
  `taxonomy/`, `skills/`, `docs/`, `templates/` and the fixture. Reuse with credit.
- The pack templates keep the position in 0004: once filled for an engagement, a pack
  is a deliverable owned per that engagement's contract, separate from the kit.

Conditions for publishing, each enforced in the repo:

- **Nothing from a real engagement appears anywhere**, in files or in history. The
  only engagement committed is the invented Caldergate Freight fixture, and the
  fixture's people, companies and tools are invented.
- **No third party's brand assets.** The HTML templates use a system font stack and a
  neutral slate blue accent; a skin (`skins/README.md`) supplies real branding.
- **The claims are checkable or caveated.** Headline numbers from the private replay
  are stated with their limits in `docs/results.md`; everything else can be rerun with
  `make demo`.
- **CI runs the demo** and diffs the regenerated `facts.json` against the committed
  file, so the fixture cannot drift from the tools.
