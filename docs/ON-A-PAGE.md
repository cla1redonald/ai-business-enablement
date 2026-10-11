# The AI Business Enablement kit, on a page

**What it is.** A complete, reusable kit for running an AI readiness assessment and
top-opportunities diagnostic at a mid-sized organisation, fast: a two-week diagnostic
or a six-week reference engagement. Distilled from a delivered engagement, and
deliberately unbranded (branding is applied per context as a "skin").

**What it is technically.** Not an app: a playbook plus a toolbox. The judgement work
(summarising calls, extracting evidence, drafting maps and briefs) is defined as six
markdown skill files that Claude executes under strict evidence rules; the
deterministic work (every count, join, check and export) is four small Python
command-line tools; the deliverables render from static templates. No server, no
database, no UI. The client receives a folder: report, data workbook, interactive
HTML maps and briefs, call summaries, and a README plus an agent-facing guide so
their own AI can navigate it.

**The method in four moves.**

1. **Discover**: structured conversations and documents in; every opportunity heard
   is recorded as evidence-bound observations (verbatim quotes, source references,
   nothing invented; the consultant's own words never count as evidence).
2. **Assess**: a 20-area readiness instrument, four areas per enabler, each rated in
   place / partial / gap / blocked. The five enablers: Trusted information, Hosting
   and identity, Control and accountability, Proof, Adoption and capacity.
3. **Bridge**: the many opportunities reduce to a handful of root causes, cleared by
   the five enablers, each enabling gap sized by how many opportunities wait on it.
   The pitch line: appetite is not the limit; groundwork is.
4. **Choose**: leadership runs six questions against their own workbook in one
   session, picking a starting portfolio; repeatable every quarter. Two decisions
   first (an accountable owner; growth-led or cost-led), work grouped into waves,
   and a quick win paired with every wave of groundwork.

**What keeps it honest.** Skills draft, tools check, the human decides. Every number
in every deliverable traces to a generated facts manifest; a self-testing checker
lints prose, verifies figures and audits for stray names before anything ships;
client packs are immutable versioned baselines; privacy is enforced twice (role
tokens at intake, an audit at export).

**Status.** v0.1. Assembled and proven end to end against a fully synthetic fixture
engagement (an invented freight forwarder, committed in the repo as the worked
example). Its output has also been compared against a replay of the real engagement
it was distilled from, which is kept private (see `docs/results.md`). Code is MIT,
method and templates are CC BY 4.0.

**Where to look.** `docs/ARCHITECTURE.md` for how it fits together (with diagrams),
`docs/QUICKSTART.md` to run it, `fixtures/caldergate/` for the worked example,
`docs/decisions/` for why it is shaped this way.
