# The AI Business Enablement kit, on a page

## What it is

A complete, reusable kit for running an AI readiness assessment and a top-opportunities
diagnostic at a mid-sized organisation, and for doing it quickly. It supports a two-week
diagnostic or a six-week reference engagement. It was distilled from an engagement that
was actually delivered, and it carries no branding on purpose. Branding is added for
each context as a "skin".

## What it is technically

It is a playbook and a toolbox rather than an app. The work that needs judgement
(summarising calls, extracting evidence, drafting maps and briefs) is written as six
markdown skill files, which Claude carries out under strict evidence rules. The work
that must come out the same every time (every count, join, check and export) is done by
four small Python command-line tools. The deliverables are rendered from static
templates. There is no server, no database and no user interface.

The client receives a folder. It holds the report, a data workbook, interactive HTML
maps and briefs, call summaries, a README, and a guide written for the client's own AI
so that it can find its way around the folder.

## The method in four moves

1. **Discover.** Structured conversations and documents go in. Every opportunity heard
   is recorded as an observation bound to its evidence, with verbatim quotes, source
   references and nothing invented. The consultant's own words never count as evidence.
2. **Assess.** Readiness is rated on a 20-area instrument, four areas for each enabler,
   and each area is rated in place, partial, gap or blocked. The five enablers are
   Trusted information, Hosting and identity, Control and accountability, Proof, and
   Adoption and capacity.
3. **Bridge.** However many opportunities there are, they come down to a handful of root
   causes, which the five enablers clear. Each enabling gap is sized by the number of
   opportunities waiting on it. The point for leadership is that the missing groundwork
   holds them back far more than any lack of appetite.
4. **Choose.** In one session, leadership works through six questions against its own
   workbook and picks a starting portfolio. The session can be repeated every quarter.
   Two decisions come before it. One names an accountable owner, and the other settles
   whether the work is led by growth or by cost. The work is then grouped into waves,
   and every wave of groundwork is paired with a quick win.

## What keeps it honest

Nothing a skill drafts is final until the tools have checked it and a person has
accepted it. Every number in every deliverable traces back to a generated facts
manifest. Before anything ships, a checker that tests itself first lints the prose,
verifies the figures and looks for stray names. Client packs are versioned baselines
that are never overwritten. Privacy is enforced twice, once at intake, where people are
replaced by role tokens, and again at export, where the pack is audited.

## Status

This is v0.1. It has been assembled and proven end to end on a fixture engagement that
is invented throughout, an imaginary freight forwarder committed in the repo as the
worked example. Its output has also been compared with a replay of the real engagement
it was distilled from, and that replay is kept private (see `docs/results.md`). The code
is MIT licensed. The method and templates are licensed CC BY 4.0.

## Where to look

For how the parts fit together, with diagrams, read `docs/ARCHITECTURE.md`. To run the
kit, use `docs/QUICKSTART.md`. The worked example is in `fixtures/caldergate/`, and the
reasons the kit is shaped the way it is are recorded in `docs/decisions/`.
