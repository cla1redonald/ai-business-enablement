# Controlled vocabulary and term rules

One vocabulary file, used by every artefact. When a term needs changing, change it here
first, then propagate: terminology is a spine, and a rename touches every surface that
carries it (report, workbook, maps, briefs, diagrams). Never let two artefacts define the
same term differently.

## Core terms

| Term | Definition |
|---|---|
| Enabler | Something that has to be true before AI capability can be built on it safely and at scale. There are five, in canonical order; see `enablers.md`. |
| Enabling gap | A sized piece of groundwork, such as a data connection or a review process, that must be in place before the opportunities behind it can start. Rated for the gap itself (in place, partial, gap) and carrying an opportunities-waiting count. |
| Root cause | What a group of opportunities shares that holds them back. Never "constraints". Root causes outlive any organisational design, which is why the enablers that clear them are the durable part of a report. |
| Opportunity | A specific, evidenced possibility for AI to remove friction, manual effort or waiting. Carries source references; may carry a quantified figure (time spent or volume handled). |
| Observation | An evidence-bound record drawn from a source, with a reference back to it. Observations underpin opportunities; the two counts are reported separately. |
| Source | A conversation (interview, working session, drop-in, message thread) or a document. Report conversation and document counts separately, and never merge the foundations source count with the opportunities source count if they differ. |
| Value stream | The path a piece of work travels through the business, from the event that triggers it to the outcome it exists to produce, crossing teams and systems on the way. Named "X to Y" after its trigger and outcome. |
| Route | A path through a value stream: the level of detail at which impact and effort can be judged meaningfully. Routes are what the choosing session chooses between. |
| Portfolio | The set of routes funded together. |
| Gated / open | An opportunity is gated when it waits on at least one enabling gap, open when it waits on none. Gated is not lesser; a gated route's first step is the gate. |
| Wave | A group of moves that wait on nothing outside the group, so the wave can start the day the decision is made. |
| Quick win | The stream with the most quantified evidence that waits on nothing. |
| Choosing session | The client-owned working session where leadership runs the six questions against the workbook and picks a starting set. Repeatable quarterly and at any reorganisation. |
| Connector | The mechanism by which an AI tool reaches a source system. Connectors inherit the permissions of the person using them. |
| Skill / plugin | A skill is a set of instructions an AI tool follows; a plugin is a skill packaged so a workspace can install it. |
| Impact grade | Graded at stream level: how much friction, manual effort and waiting a stream carries, and what removing it would release. High / medium / low. |
| Effort grade | Consultant judgement on deliverability, not a measured estimate. Effort decides the sequence and never decides worth. |
| Stream membership | An opportunity can sit on more than one stream; membership counts sum past the opportunity count. Say so wherever the numbers appear together. |
| Share-weighted count | An opportunity split across n functions counts 1/n to each, so nothing is double counted. Name the weighting before the reader discovers it. |
| Quantified | Carrying a captured timing or volume. Quantified means captured timings and volumes, not delivery effort. |
| In flight | Work the client already has moving. Recorded so the plan finishes rather than restarts it; distinct from a delivery status, which is never recorded per opportunity. |

## Frameworks (people vs routes: keep them apart)

| Term | Definition |
|---|---|
| The four gears | Where **people** sit: think with it, work with it, act agentically, built in. Self-placeable in a live poll. Strategy rule: move the mass one gear, not two. |
| Workflow shapes | A design choice per **route**, not a maturity scale: human-led (a person drives, AI assists), agent-led (an agent carries the work, a person confirms at defined points), autonomous (the agent runs to a defined outcome within capped iterations and spend, and a separate check grades the result). A route graduates; an organisation does not "become" agentic. |
| The three pillars | How AI creates value in a business: employees working smarter, processes running faster, the product itself getting better. Its job is scoping: "this engagement points at the first two" is a one-sentence boundary. |
| Readiness rating | Exactly four values: in place, partial, gap, blocked. See the instrument for semantics. No scores, percentages or maturity levels, ever. |

## Term rules (hard)

1. **"Root causes", never "constraints".**
2. Client artefacts never say **corpus**, **register**, **landscape** or **data pack**.
   (Exception: a proper noun the client uses, such as a market landscape report.) These are
   working-tool words; the client-facing words are "the discovery", "the evidence", "the
   opportunities", "the workbook".
3. **No delivery statuses per opportunity, ever.** The discovery deliberately records none,
   because there is no authoritative source of delivery progress. The choosing session
   opens by asking the owning teams what is genuinely moving. The only Status field
   anywhere is on enabling gaps, and it records the readiness of the gap itself.
4. **People by role, never by name**, in anything shareable. Client organisations by
   neutral token until the client approves naming.
5. **No verbatim quotes in client artefacts.** Paraphrase source material into the
   narrative. (Working files may hold quotes; they must exist in their cited source.)
6. **Evidence before interpretation.** State what was found, then what it means, then what
   to do.
7. **Numerals for quantities.** Counts and figures are numerals, not words, so they can be
   checked mechanically.
8. **No em dashes. British English.** Sentence-level style budgets live in the checker
   config, not here.
9. **Absence and non-examination are different findings.** Never write that something is
   not there when the truth is it was not examined. Mark deliberately light coverage and
   say what it does and does not imply.
10. **Findings are evidence-derived; actions are consulting judgement.** Keep that line
    visible wherever both appear, and mark any unrated forward-looking section "judgement,
    not evidence".
