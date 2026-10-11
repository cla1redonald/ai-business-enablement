# 0002: Names are tokenised at intake AND checked at export

**Decided at harvest (2026-08-31).** The reference implementation carried an open
decision (its 2026-08-02 plan, step 2b): redact names at ingest, or keep them in the
corpus and enforce a rule at the export boundary.

The kit takes both, deliberately:

- **At intake**: people become role tokens seeded from each source's `participants:`
  frontmatter, and prospect and customer company names are tokenised always (they are
  commercially sensitive, absent from participants lists, and the one case where the
  client seeing them is also a problem).
- **At export**: the checker's per-engagement `names` list audits every shareable
  artefact anyway, and the `pack` tool refuses to baseline on a stray-name hit.

Why both: check-at-export alone is only as strong as the number of export paths, and
nobody counts them reliably; redact-at-intake alone caused a real misattribution error
in the reference engagement (tokens hid which of two leads was which). Defence in
depth costs little and each layer catches the other's failure mode. The intake-side
mapping from names to tokens lives outside every artefact, in the engagement
workspace, never in the repo or a pack.
