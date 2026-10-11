# 0003: Intake is a runbook step, not a fifth tool

**Decided 2026-08-31, reconciling a harvest inconsistency.** The stage-arc pass first
described v0.1 intake as "a script"; the PRD's tool cap says four scripts, no more
(`facts`, `check`, `workbook`, `pack`), and the cap is a guardrail against the kit
growing back into the machinery it replaced.

Resolution: intake in v0.1 is a documented manual step, run in-session under
`skills/00_evidence-rules.md`: token registry seeded from `participants:` frontmatter,
company tokenisation always, source sub-type declared per file, and per-source
bookkeeping (a source unchanged keeps its observation file, so unchanged work is never
redone; that is a convention the workspace layout enforces, not machinery).
The export-side checker and the pack audit are the safety net (0002).

Revisit only if a replay of a real engagement (kept private) shows manual intake is
where the time goes. If a script is ever added, one of the four tools gives way or the cap is raised in a decision, not
by drift.
