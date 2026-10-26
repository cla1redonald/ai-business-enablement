# Skins

The kit is neutral (decision 0001). A skin is everything a particular context adds so
that the deliverables carry its brand. It is applied for each engagement without
touching the kit's files. A skin is a folder, kept outside this repo whenever it holds a
firm's real assets, and it supplies five things.

1. **Palette and type.** These are overrides for the `:root` variables at the top of
   each HTML template and diagram (`--ink`, `--accent`, `--line`, `--muted`, `--link`,
   `--paper`, `--font-head`, `--font-body`), plus a font `<link>` if the skin uses web
   fonts. The kit itself ships with a system font stack and makes no external requests.
   Nothing else in the HTML carries branding.
2. **The register exemplar.** This is the opening paragraphs of the firm's best
   comparable report, supplied to criterion 10 of `tools/rubric.md`. The kit ships
   without one.
3. **Identity slots.** These are `{consultancy}`, the consultant's name and the footer
   lines, which the `pack` tool fills at build time from the engagement config.
4. **Publishing pipeline.** If the firm has a renderer for branded documents, the report
   skeleton's directive markers (`[!box:]`, `[!table-metrics]`, `[pagebreak]`...) map
   onto it. If not, the markdown renders plain, and the list of directives in
   `tools/check.config.json` is edited to match what the chosen pipeline supports.
5. **House lint additions.** Extra ban-list rules or changes to budgets go into a copy
   of `check.config.json`. Every rule added needs poison and clean fixtures, or the
   self-test refuses to grade.

As a rule of thumb, if applying a skin means editing anything under `taxonomy/`,
`method/`, `skills/` or `tools/` (other than a copy of the config), the kit has a leak.
Fix the kit, not the skin.
