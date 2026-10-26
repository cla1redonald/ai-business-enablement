# Tools

There are four scripts and there will not be a fifth. They are small and deterministic,
and between them they own every number, join, check and export. The skills do the
drafting and a person makes the decisions. If a tool ever seems to need a tree of
subcommands, it is doing a skill's job and the design is wrong.

| Tool | Job | Status |
|---|---|---|
| `facts.py` | Builds the facts manifest (`facts.json`): every count and figure any artefact may use, each with its provenance, derived from the engagement data and never typed. Consultant-verified evidence figures are carried from `engagement.json` with their contexts. Enforces referential integrity on the landscape and the 20-area shape on readiness. | Working, proven on the fixture |
| `check.py` | Facts verification plus prose lint: the config-driven ban list and budgets (`check.config.json`), the directive check, the figure traceability check against `facts.json`, and `--layout` page-end checks on rendered PDFs. Self-testing: every rule proves it can fire and stay silent before anything is graded. | Working, proven on the fixture |
| `workbook.py` | Builds the xlsx from the engagement data per `templates/workbook-spec.md`. Joins carry stable IDs; every count is recomputed from the landscape; the Read me's six-questions table is kept in step with the report skeleton's annex E. | Working, proven on the fixture |
| `pack.py` | Builds the versioned baseline folder and zip: writes README and CLAUDE.md from the templates and the facts manifest, audits for draft markers, unfilled slots and stray names, and refuses to overwrite an existing baseline. Baselines are immutable. | Working, proven on the fixture |

All four run against the worked example in `fixtures/caldergate/`, and its README gives
the order to run them in.

Running `check.py --observations <workspace>` verifies the extraction outputs
mechanically. It checks that each quote exists verbatim (allowing for line-wrapping),
that locators name real files, that no registry names appear in claims and that the
schema shape holds. Where speaker labels are configured, it also checks that no quote is
drawn from a consultant turn. It has its own poison and clean self-test. It cannot judge
whether the right observations were extracted. That stays with the comparison and the
human gate.

The file `rubric.md` covers the half of checking that needs judgement. Run it through a
model in a fresh session that did not write the draft, with the house register exemplar
alongside.

For each engagement, copy `check.config.json` and fill in `names` (the list behind the
roles-not-names rule) and `guarded_pairs` (figures that must never be merged into one
claim). Then append any claim rules specific to the engagement, each with its poison and
clean fixtures.
