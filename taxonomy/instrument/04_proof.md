# Enabler 4: Proof

*Can you see, and evidence, what is happening?* Four areas. What can be seen and what can
be shown to someone who asks are different bars, and for a certified or regulated
business the second is the one that counts.

The four areas share a single cause when they fail together: nothing records what AI is
doing. Because nothing is recorded, usage cannot be seen, activity cannot be evidenced to
an assessor, value cannot be measured and cost cannot be attributed. Fixing the recording
addresses all four; fixing any one separately addresses none of the others. A uniformly
gapped Proof theme also holds up work elsewhere: incident response waits on detection,
and the funding case for every other enabler waits on measurement. When all four are
gaps, say that as one finding, not four.

Most of this theme needs **direct examination**: review the admin console together,
because nobody volunteers their audit posture unprompted, and what an administrator can
actually see is frequently less than anyone assumed.

## 13. Usage and activity

**Definition.** Whether anyone can see AI usage beyond spend: by person, by team, as
activity rather than cost. While cost is the only visible number, cost is the only
conversation available, and AI appears in a board pack as spend or not at all. A
reporting limitation gets read as a business fact.

**What to look for.** What the admin console actually shows (review it together). Whether
the limits are configuration or tier: analytics behind a higher plan is common, and it is
one recurring tier decision rather than several separate findings. Whether telemetry the
current tier already exposes (analytics exports, OpenTelemetry-style logging) is being
collected. Which surfaces are unmeasured even if the main assistant is instrumented
(secondary tools, embedded AI).

**How to surface it.** "Show me what you can see about last month's AI use." "Per
person? Per team? Or only the invoice?" "What does the tier include that you are not
collecting?"

**Rating anchors.**
- In place: per-user and per-team usage visible, collected as a matter of course, across
  the main surfaces.
- Partial: usage visible for the main assistant only, or collected but not looked at.
- Gap: cost is the whole of what anyone can see.
- Blocked: visibility impossible on the current tier AND collection of what the tier
  does expose has been examined and is genuinely insufficient. (Rare: usually what the
  tier exposes has simply not been collected.)

**Sequencing note.** Turn on visibility before buying it. Export what the current tier
already exposes into whatever observability platform the organisation runs today; an
established engineering function usually has somewhere for it to land. A higher tier
buys an audit interface, not an audit capability: collection, storage and search are
yours to build either way. Collect first, then let the tier decision follow the
requirement. Done this way, three gaps start closing at once: usage and activity, audit
evidence, and the detection trigger incident response is missing. This is typically the
highest ratio of unblocked-to-spent in the whole report.

## 14. Audit evidence

**Definition.** Whether a per-event trail exists that would satisfy an assessor: what was
asked, produced, reached and by whom. AI-specific: infrastructure logging is usually in
reasonable order, and the AI layer has no equivalent. The bar is set by commitments
already made (a policy that promises monitoring, a certification that requires controls
to be demonstrable), not by best practice in the abstract.

**What to look for.** Whether any per-user activity log or audit interface exists on the
current plan (check directly). What the other surfaces offer (file layers usually have
audit logs; establish rather than assume; the surface carrying the most AI use often
offers the least). The organisation's standing commitments: certifications held, policy
monitoring clauses, client contractual promises. The relevant standards for framing
(ISO/IEC 27001 requires controls to be demonstrable; ISO/IEC 42001 maps the AI-specific
bar), used to show where the bar will sit when somebody asks, not as an assessment.

**How to surface it.** "If a client audit asked for evidence of AI activity, what would
you produce?" "Which of your existing certifications cover the AI estate today?" "Has
anyone established what each surface logs?"

**Rating anchors.**
- In place: an activity trail collected and retained across the main surfaces, adequate
  to the organisation's own commitments.
- Partial: trails exist for some surfaces and nobody has established the whole; or
  collection has started and retention is undecided.
- Gap: no per-event trail on the main surface and no established picture elsewhere,
  against standing commitments that assume one.
- Blocked: as area 13; rare.

## 15. Value measurement

**Definition.** Whether anything beyond raw spend can show what AI use has achieved:
baselines captured before change, value measures defined per initiative, targets set and
reported. Licence activations measure procurement, not value. This area decides whether
anything else gets funded, and its deadline partly passes with every delivered change: a
baseline only exists before the change happens.

**What to look for.** Any measure in use beyond spend and activations. Whether any
baseline was captured before current AI work started. Whether friction is located
without cost being known (pain recorded on process steps, timings absent is the common
shape: friction can be located while nothing can be sized in advance). Whether anyone
could say if adoption is spreading or concentrating.

**How to surface it.** "What would you show the board to prove AI has paid back
anything?" "What was measured before the current tools arrived?" "If a pilot saved
time, whose baseline would you compare it against?"

**Rating anchors.**
- In place: measures per initiative, baselined before start, reported against targets.
- Partial: some real measures exist or are being stood up, but no baselines predate the
  change.
- Gap: no established way to value AI output; spend and activation counts are the only
  proxies.
- Blocked: rarely applicable.

**Sequencing note.** Baseline a few measures now, imperfectly; a well-designed framework
started later measures the wrong period. The standard three: weekly active use by
function (not activations), depth of use (the share of active users doing anything
beyond chat), and end-to-end cycle time on one chosen value stream, measured before work
starts on it. The third is the only one that speaks the board's language. Add spend per
active user once telemetry exists, which turns a rising total into a unit economic.

## 16. Cost attribution

**Definition.** Whether there is a route from AI usage back to a team, a budget or an
owner, produced as a matter of course and kept current. Immaterial at a handful of
users; stops being immaterial exactly as adoption spreads, which is what the rest of the
programme is designed to cause.

**What to look for.** Whether any attribution exists or could be derived by hand (small
populations in known teams usually can be, once). Material spend nobody can allocate
(a large tool bill "noticed but not attributed" is the exact shape of the gap; treat
figures given in passing as orders of magnitude, and say so). Whether spend sits central
or with teams, and whether that was decided or defaulted. Note the grade covers the
ability to attribute, not the attribution itself.

**How to surface it.** "What does AI cost each part of the business?" "Could you derive
that by hand today? Has anyone?" "Who would decide whether spend moves to team
budgets?"

**Rating anchors.**
- In place: attribution produced routinely and current, with the central-versus-teams
  question decided.
- Partial: derived by hand at least once and broadly right, but nothing keeps it
  current.
- Gap: no route from usage to team, budget or owner.
- Blocked: attribution impossible until usage visibility (area 13) exists; grade gap
  and name the dependency rather than blocked, unless area 13 is itself blocked.

**Sequencing note.** Derive it by hand once to answer the immediate question, then let
the finance-model decision (central or per-team) be taken deliberately. It cannot be
automated until usage and activity closes, so area 13 comes first either way.
