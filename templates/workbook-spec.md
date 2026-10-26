# Workbook specification

The opportunity workbook is the data companion to the report: every opportunity, stream
and enabling gap as data, arranged so the six-question choosing framework can be run
directly against it in one working session. It is built by the `workbook` tool from the
engagement data, never edited by hand: names are not identifiers, and a hand-edited
join breaks silently.

## Identity rules (the hard lesson)

- **Every entity carries a stable ID**: opportunities (`OPP-001`), value streams
  (`VS-01`), enabling gaps (`GAP-01`). IDs are assigned at creation and never reused or
  renamed.
- **Joins are by ID.** Display names are metadata and may change; a rename touches one
  cell, not every cell that references it.
- **Display columns show names** so the workbook reads naturally in the session; ID
  columns sit alongside for the joins and the checker.
- Multi-valued cells (an opportunity on two streams) separate values with a vertical
  bar, in both the ID and display forms.

## Sheets and columns

### Read me
Title, one-paragraph description, the six-questions-to-columns table (kept in step with
the report's annex E, verbatim), the delivery-status paragraph, and the reading notes
(role tokens, multi-value cells, blank-cell counts). The Read me is generated from the
same source as annex E so the two can never disagree.

### Opportunities (one row per opportunity)
| Column | Content |
|---|---|
| Opportunity ID | Stable ID |
| Opportunity | Short name |
| Description | What was evidenced, in one or two sentences |
| Function(s) | Display names, bar-separated |
| Value stream(s) | Display names, bar-separated (blank = sits on no stream) |
| Value stream ID(s) | Bar-separated IDs |
| Impact grade | High / Medium / Low (blank = ungraded, a recorded gap) |
| Effort grade | High / Medium / Low, consultant judgement |
| Quantified figure | Number only (blank = evidenced but not quantified) |
| Figure unit | e.g. hours per week, items per month |
| Enabling gap dependencies | Display names, bar-separated (blank = open) |
| Enabling gap ID(s) | Bar-separated IDs |
| Theme | The stream-of-work or cluster label, if used |

### Value streams (one row per stream)
| Column | Content |
|---|---|
| Value stream ID | Stable ID |
| Value stream | "X to Y" display name |
| Statement | One-sentence description of the path |
| Start event | The trigger |
| End event | The outcome |
| Functions crossed | Display names |
| Member count | Opportunities on this stream (memberships, not unique) |
| Source count | Sources evidencing this stream |
| Enabling gaps | Display names, bar-separated |
| Enabling gap ID(s) | Bar-separated IDs |
| Impact grade | High / Medium |

### Enabling gaps (one row per gap)
| Column | Content |
|---|---|
| Enabling gap ID | Stable ID |
| Enabling gap | Display name, stated as the capability wanted |
| Enabler | One of the five, canonical names |
| Status | In place / Partial / Gap (the gap's own readiness, not delivery) |
| Opportunities waiting | Count (sums past the gated total when opportunities wait on more than one gap; the report says so) |

## Data honesty rules

- **No delivery status columns, ever**, on Opportunities or Value streams. The only
  Status column is on Enabling gaps and records the gap's own readiness.
- **Blank cells are recorded gaps in the data, not errors**, and the Read me states the
  counts (n ungraded, n without function, n on no stream).
- Role tokens and client-organisation tokens are left exactly as recorded.
- Quantified figures carry their unit; a figure without a unit fails the checker.

## Consistency checks (enforced by the `check` tool)

- Every stream and gap referenced from Opportunities exists on its own sheet (join by
  ID).
- Member counts and opportunities-waiting counts recompute from the Opportunities
  sheet exactly.
- Read me table matches report annex E verbatim.
- Counts on the Read me match the facts manifest.

## Open question (carried from the PRD)

Whether the workbook stays xlsx only or gains a rendered HTML twin. HTML travels
better, and xlsx is what execs open in the session. The kit's build plan leaves this
open for now, and the spec above is format-neutral except the sheet structure.
