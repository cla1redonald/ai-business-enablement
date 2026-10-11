<!--
TEMPLATE: pack README.md
The pack is the versioned client deliverable folder: report plus workbook plus maps plus
briefs plus call summaries, zipped. The `pack` tool writes this README from the facts
manifest and audits the folder before baselining. Baselines are immutable: changes are
V2, in a new folder. A pack is also re-loadable as a next engagement's starting state.
-->

# {Client token} AI Business Enablement, V{n} baseline

Deliverables from the {consultancy} AI business enablement engagement, {period}. This
folder is the complete, versioned handover: the report plus the working materials it
draws on. Prepared by {consultant name}, {consultancy}. Baselined {date}.

## Contents

| Path | What it is |
|---|---|
| `{report_file}` | The report. Read this first; everything else supports it. |
| `{workbook_file}` | The {n_opportunities} opportunities, {n_streams} value streams and {n_gaps} enabling gaps as data. Arranged so the report's six questions can be run against it directly (the report's annex E maps each question to a column). |
| `value-stream-maps/` | {n_maps} step-level value stream maps as interactive HTML. Open in any browser; no server needed. |
| `enabling-gap-briefs/` | {n_briefs} one-page briefs. Each covers what the gap is, what waits on it and what closing it looks like. |
| `call-summaries/` | {n_conversations} conversation summaries from the discovery, as markdown. These are the conversation layer of the evidence base. |

## How the pieces join

- The report's section 5 table of {n_gaps} enabling gaps matches the Enabling gaps
  sheet in the workbook by ID and name; the {n_briefs} briefs in
  `enabling-gap-briefs/` cover the gaps that gate the leading opportunities.
- The {n_streams} streams in the report's section 3.2 tables match the Value streams
  sheet in the workbook by ID and name; the {n_maps} maps in `value-stream-maps/`
  cover the streams mapped at step level.
- The workbook's "Enabling gap dependencies" column joins to the Enabling gaps sheet.
  Blank means the opportunity is open, waiting on nothing.
- The report's annex E maps each of the six choosing-session questions to the workbook
  column that answers it.

## Conventions

- People appear by role, and in the call summaries by bracketed role token (for example
  `[CONSULTANT-1]`); named client organisations appear by neutral token. This is
  deliberate.
- No delivery status is recorded for any opportunity or stream. The evidence describes
  {evidence_period}; re-confirm what is moving before acting on it.
- Blank workbook cells are recorded gaps in the data, not errors.
