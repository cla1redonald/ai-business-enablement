# Skins

The kit is neutral (decision 0001). A skin is everything one context adds to make the
deliverables carry its brand, applied per engagement without touching kit files. A
skin is a folder (kept outside this repo when it carries a firm's real assets)
supplying:

1. **Palette and type**: overrides for the `:root` variables at the top of each HTML
   template and diagram (`--ink`, `--accent`, `--line`, `--muted`, `--link`,
   `--paper`, `--font-head`, `--font-body`, plus a font `<link>` if the skin's fonts
   are web fonts; the kit ships with a system font stack and no external requests). Nothing else in
   the HTML is branded.
2. **The register exemplar**: the opening paragraphs of the firm's best comparable
   report, supplied to `tools/rubric.md` criterion 10. The kit ships without one.
3. **Identity slots**: `{consultancy}`, consultant name and footer lines, filled by
   the `pack` tool at build time from the engagement config.
4. **Publishing pipeline**: if the firm has a branded-document renderer, the report
   skeleton's directive markers (`[!box:]`, `[!table-metrics]`, `[pagebreak]`...)
   map onto it; otherwise the markdown renders plain and the checker's directive
   list in `tools/check.config.json` is edited to match what the chosen pipeline
   supports.
5. **House lint additions**: extra ban-list rules or budget changes, appended to a
   copy of `check.config.json` (every added rule needs poison and clean fixtures or
   the self-test refuses to grade).

Rule of thumb: if applying a skin requires editing anything under `taxonomy/`,
`method/`, `skills/` or `tools/` (other than a config copy), the kit has a leak;
fix the kit, not the skin.
