# Tools

Four scripts, no more. Small deterministic scripts own every number, join, check and
export; skills draft; the human decides. If a tool needs a subcommand tree, it is doing
the skills' job and the design is wrong.

| Tool | Job | Status |
|---|---|---|
| `facts.py` | Builds the facts manifest (`facts.json`): every count and figure any artefact may use, each with its provenance, derived from the engagement data and never typed. Consultant-verified evidence figures are carried from `engagement.json` with their contexts. Enforces referential integrity on the landscape and the 20-area shape on readiness. | Working, proven on the fixture |
| `check.py` | Facts verification plus prose lint: the config-driven ban list and budgets (`check.config.json`), the directive check, the figure traceability check against `facts.json`, and `--layout` page-end checks on rendered PDFs. Self-testing: every rule proves it can fire and stay silent before anything is graded. | Working, proven on the fixture |
| `workbook.py` | Builds the xlsx from the engagement data per `templates/workbook-spec.md`. Joins carry stable IDs; every count is recomputed from the landscape; the Read me's six-questions table is kept in step with the report skeleton's annex E. | Working, proven on the fixture |
| `pack.py` | Builds the versioned baseline folder and zip: writes README and CLAUDE.md from the templates and the facts manifest, audits for draft markers, unfilled slots and stray names, and refuses to overwrite an existing baseline. Baselines are immutable. | Working, proven on the fixture |

All four run against the worked example in `fixtures/caldergate/`; see its README for
the run order.

`check.py --observations <workspace>` mechanically verifies extraction outputs
(quote exists verbatim modulo line-wrapping, locators name real files, no registry
names in claims, schema shape, and, where speaker labels are configured, no quote
drawn from a consultant turn), with its own poison/clean self-test. It cannot judge
whether the right observations were extracted; that stays with the comparison and
the human gate.

`rubric.md` is the judgement half of checking: run it through a model in a fresh session
that did not write the draft, with the house register exemplar alongside.

Per engagement: copy `check.config.json`, fill `names` (the roles-not-names list) and
`guarded_pairs` (figures that must never merge into one claim), and append any
engagement-specific claim rules with their poison and clean fixtures.
