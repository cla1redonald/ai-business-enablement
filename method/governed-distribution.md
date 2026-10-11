# Governed distribution: the review gate and the verification pattern

The path from one person's working tool to something the whole company can rely on.
Three controls, usually all within the client's reach at assessment time: the review
gate, the verification pattern, and the Proof measures. The practical order is the gate
first, the pattern alongside it, and the measures switched on before the first
published capability is used in anger. This file is the source of truth; the report
skeleton's annex B mirrors it.

## The review gate

A review gate before company-wide publication, owned by a named engineer, built as a
one-page rulebook for authors and a checklist for reviewers, enforced in the
publication pipeline. The gate checks what a skill's instructions actually do before
publication. The rules that matter most:

- A skill never touches credentials and never fetches instructions at run time.
- It holds only the narrowest permissions it needs, and treats everything it reads as
  data rather than instruction.
- It stops for confirmation before irreversible actions, and describes itself
  accurately.
- A change reaches users only through a version increase, so every published
  capability stays traceable to what was reviewed.
- A good skill records what a new colleague could not discover (the organisation's own
  rules and boundaries) rather than technique the tools already carry.

Design in from the start, not retrofitted: a licence and provenance check alongside the
malicious-behaviour check (executable code inside skills makes this live, not
theoretical), and read-only as the default for new connectors at the moment the
marketplace opens, while the estate is still small. Split the review path by pace of
change: skills through a lightweight merge-request lane with the licence check;
connectors and MCP servers through the fuller security review, with a quick lane for
vendors already under contract.

Note the supplier-side limits honestly: vendor skill-scanning features typically sit on
higher tiers and may be unavailable under zero-data-retention configurations, in which
case the gate carries that load on the current plan.

## The verification pattern

The recurring observation: working skills giving confidently wrong answers until
debugged by hand, each with its own home-made checker. **When a skill gives confidently
wrong answers, the root cause is usually the home-made checker.**

The recommendation is one shared pattern: a harness that runs cases, applies checks and
reports results, with each skill supplying only its own cases and expected answers,
agreed by the people who know what correct looks like. What good looks like:

- Deterministic checks first; any model-based check is calibrated against human
  judgement before it counts.
- Infrastructure failures reported separately from wrong answers, so the fix lands in
  the right place.
- Twenty to fifty realistic cases per skill as a practical starting point.
- Experimentation stays free against a growing working set; graduation reads a frozen
  set that only change control may alter, judged on independent thresholds for
  quality, safety, cost and consistency, never one blended score.
- Sign-off records its own boundary. What passes is a specific capability against
  specific criteria, never AI for a function in general, and the record of what was
  not approved protects the business later.

Verification belongs inside the tools rather than in a policy clause people are asked
to remember: a skill that carries its own checks is enforceable, a written requirement
is not. Finish the first evaluation before starting a second; one finished example is
worth more than three started ones, and it becomes the template the gate points at.

## Why this sells

The person who built the risky tool usually names the risk unprompted, and better than
any policy clause ("people would come back saying the assistant told them so"). The
control is what lets a careful owner publish. Frame the gate and the pattern as the
route by which one person's win becomes company capability, never as compliance
overhead: distribution with review in front of it raises the return on every other
investment in the report.
