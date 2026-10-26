# Governed distribution: the review gate and the verification pattern

This is the path from a tool that works for one person to something the whole company
can rely on. It rests on three controls, which are usually all within the client's reach
at the time of the assessment. They are the review gate, the verification pattern and
the Proof measures. In practice the gate comes first, the pattern is built alongside it,
and the measures are switched on before anyone uses the first published capability for
real work. This file is the source of truth, and annex B of the report skeleton mirrors
it.

## The review gate

Before anything is published company-wide, it passes a review gate. A named engineer
owns the gate, which is made up of a one-page rulebook for authors and a checklist for
reviewers, and it is enforced in the publication pipeline. The gate checks what a
skill's instructions actually do before the skill is published. These are the rules that
matter most.

- A skill never touches credentials and never fetches instructions while it runs.
- It holds only the narrowest permissions it needs, and it treats everything it reads as
  data rather than as instructions.
- It stops for confirmation before any action that cannot be undone, and it describes
  itself accurately.
- A change only reaches users through a version increase, so every published capability
  can be traced back to what was reviewed.
- A good skill records what a new colleague could not find out for themselves, meaning
  the organisation's own rules and boundaries, rather than technique the tools already
  carry.

Some things are much harder to add later, so design them in from the start. Run a
licence and provenance check alongside the check for malicious behaviour, because skills
that carry executable code make this a real risk. Make read-only the default for new
connectors from the day the marketplace opens, while the estate is still small. Split
the review path by how fast things change. Skills go through a lightweight merge-request
lane that includes the licence check. Connectors and MCP servers go through the fuller
security review, with a quicker lane for vendors already under contract.

Be honest about what the supplier can and cannot do. Vendor features that scan skills
usually sit on higher tiers, and may not be available at all under zero-data-retention
configurations. In that case the gate has to carry that load on the current plan.

## The verification pattern

The same thing comes up again and again. Skills that work in general give confidently
wrong answers until someone debugs them by hand, and each one has its own home-made
checker. **When a skill gives confidently wrong answers, the root cause is usually the
home-made checker.**

The recommendation is one shared pattern. A harness runs the cases, applies the checks
and reports the results, and each skill supplies only its own cases and expected
answers, agreed with the people who know what a correct answer looks like. Good practice
looks like this.

- Deterministic checks come first. Any check that uses a model is calibrated against
  human judgement before it counts.
- Failures in the infrastructure are reported separately from wrong answers, so the fix
  goes to the right place.
- Twenty to fifty realistic cases per skill is a practical place to start.
- People can experiment freely against a working set that keeps growing. To graduate, a
  skill is tested against a frozen set that only change control can alter, and judged on
  separate thresholds for quality, safety, cost and consistency, never on one blended
  score.
- A sign-off records its own limits. What passes is a specific capability against
  specific criteria, never "AI for a function" in general, and the record of what was
  not approved protects the business later.

Verification belongs inside the tools, not in a policy clause people are asked to
remember. A skill that carries its own checks can be enforced, and a written requirement
cannot. Finish the first evaluation before starting a second one. One finished example
is worth more than three started ones, and it becomes the template the gate points to.

## Why this sells

The person who built the risky tool usually names the risk without being asked, and puts
it better than any policy clause would ("people would come back saying the assistant
told them so"). The control is what allows a careful owner to publish. So present the
gate and the pattern as the way one person's win becomes something the whole company can
use, and never as compliance overhead. When distribution has a review in front of it,
every other investment in the report pays back more.
