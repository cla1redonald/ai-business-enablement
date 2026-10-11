# 0001: The kit is neutral, with branding applied as skins

**Decided 2026-08-31 by Claire.** Considered: a kit branded to the author's own
company, a kit branded to a consulting firm, or deliberately neutral with a skin per
context. Chosen: **neutral with skins**.

Consequences:

- The repo is named `ai-business-enablement`.
- No firm name, palette or register exemplar lives in the kit's method, templates or
  tools. Method docs are written in kit voice ("the consultant", "the house guide").
- Every brandable surface is a token: HTML palettes and fonts are `:root` variables;
  the judgement rubric's register exemplar is a slot supplied by the skin; pack
  footers carry `{consultancy}` slots filled at build time.
- `skins/` documents how a context applies its branding without touching kit files.
- The licence question is separated out (0004) rather than implied by positioning.
