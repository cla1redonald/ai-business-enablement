# Hosting, identity and security: the deep-dive module

The engagement's technical annex material, split out so it can be sold separately: a
natural follow-on after the fast diagnostic for any regulated client, and a credible
standalone for a CTO-shaped buyer. Everything here is framework; the client's positions
fill the slots when it runs.

## 1. The three identity layers (they fail independently)

**Layer one: who can sign in.** The identity provider, seat management, how a leaver is
blocked. Usually working, often manual, workable at current scale. The recurring
finding at this layer: two sign-in mechanisms running side by side (SAML and OAuth) so
a person can appear to authenticate through one while using the other; that gap belongs
inside the identity rollout's scope with a named owner.

**Layer two: what a signed-in person's AI can reach.** Connectors inherit the
permissions of the person using them, so **the AI layer is exactly as trustworthy as
the permission model in each connected system**. The job of an identity rollout is to
make those permissions deliberate and current everywhere: one place where joiner, mover
and leaver events set permissions across every connected system. Two honest caveats
travel with any such rollout. The AI supplier's tier can cap what the rollout automates
(provisioning via SCIM is commonly a higher-tier feature, so lifecycle events into the
AI tool stay manual until that boundary is crossed). And the rollout governs who
reaches each application, not what they may do inside it: per-user AI access stands on
each connected system's own permission model, so the per-system permission clean-up
remains its own piece of work.

**Layer three: what runs when nobody is signed in.** Agents need identities of their
own: service accounts so an automation survives its author leaving; scoped permissions,
ideally short-lived credentials brokered at the boundary so an agent never holds a
long-lived key; and an approved place to run, with per-user authentication on shared
agents. This is where agent ambition lives, and most organisations have nothing there.
Keep the grounding fact in proportion: an organisation with no standing agents, only
skills and subagents inside signed-in sessions, is secure by default (a run can never
see more than its user may) and limited by the same fact (an automation stops the day
its author leaves, and no run serves a workflow wider than its owner's view).

Permission scoping is not hygiene alone. Most connectors grant everything once
approved, which combined with connected email is a live prompt-injection exposure;
scoped permissions bound the blast radius without removing it. That makes scoping
first-wave work with a named owner, and a review cadence remains after it.

## 2. The agent infrastructure layers (judgement framework, not assessment)

Running agents in production is a different discipline from using a chat assistant
well. Six layers, assessed for where the client stands on each:

1. **Standardised tool access**: how a model reaches a system with permissions
   attached (the connector estate). Often the layer the client is strongest on
   without knowing it.
2. **Live retrieval over a stale index**: connectors that query the source at the
   point of asking beat a retrieval index that is correct on the day it is built and
   wrong thereafter. Structure the source first; consider anything semantic only when
   the structure is settled.
3. **Orchestration**: something to run a multi-step task, retry what fails, and stop
   what loops. Commonly present in engineering and absent everywhere else.
4. **Memory and state**: where a long-running agent keeps state between runs. Rarely a
   live constraint early; a design decision, not a setting.
5. **Sandboxed execution**: somewhere for skill-carried code to run that is not a
   person's laptop and not production. Reviewing code is not the same as containing
   it.
6. **Security and observability**: a trace of what an agent did, reached and cost.
   The weakest layer almost everywhere, and it matters more for agents than
   assistants because an agent takes actions rather than producing text.

The practical read is usually: the hardest layer (tool access) largely in place, and
the layers that make agents safe to run (isolation, orchestration, observability)
missing. Those need a first candidate, not a programme.

## 3. The routes to running agents

State the options with what each assumes; recommend managed first.

- **Managed agents, hosted by the model provider.** Almost nothing to build; identity,
  execution and scheduling come with the service. The trade is control, reach inside
  the network, and vendor concentration. For a business with no platform capacity to
  spare, the trade is the right way round.
- **Build on the existing cloud estate.** The primitives exist (compute, IAM, secrets,
  scheduling, monitoring) and this route reaches internal systems properly. It is also
  a platform, and platforms need an owner, a backlog and maintenance; committing
  without capacity is a commitment without anyone to hold it.
- **The workflow tool already licensed.** A general workflow engine is a reasonable
  orchestration layer and a poor agent layer: it schedules and connects well, and it
  does not give an agent identity, isolation or evaluation.
- **Whatever engineering already runs.** Engineering has usually solved hosting for
  its own work; ask what they use before choosing anything for the business, because
  inheriting a working internal pattern is cheaper than selecting one from outside.
- **Do nothing, and accept the ceiling.** Legitimate for another quarter, provided it
  is chosen rather than defaulted into, and nobody expects it to scale.

**Managed-first, stated as a principle: own as little as the data allows.**
Self-hosting is an exception to earn, not a default to justify. Two questions decide
the choice: who supplies the machinery that runs the agent, and who supplies the
environment it runs in. Check features, regions and residency against the workload,
and judge against tomorrow's models as well as today's: the managed path picks up
every model improvement without further work. Whatever the first hosted agent runs on
becomes the pattern, and the identity it authenticates as becomes the precedent, so
settle both in the same piece of work, and date the self-hosting revisit rather than
leaving it open.

**One design principle to adopt while almost nothing is built**: keep execution,
orchestration and data as separate layers rather than letting one vendor span all
three. It preserves the option to change one layer without rebuilding the others, and
it is the honest answer to the vendor-concentration worry the managed route raises.

**What operating at scale would require**, whichever route (state it so the first step
is taken knowing where it leads, not as a proposal): a register of what runs, who owns
each one and what it reaches; identity per agent with managed credentials; isolated
execution; evaluation that runs before a change ships; observability covering what
each agent did, touched and cost; and a named operator whose job includes it. The
managed route buys time against every one of those and removes none permanently; they
stop being avoidable at roughly the point the internal marketplace succeeds.

Two published-research anchors worth carrying (check currency before citing): the
caution against over-preparing (imperfect data should not prevent progress; high-value
cases can be piloted in fragmented environments, so the internal-data finding must not
become "nothing can start"), and the caution against under-estimating (fewer than one
in ten agentic programmes reach meaningful scale, and the gap is rarely the model: it
is fragmentation, missing controls and absent lifecycle management, which is the
argument for one thing done properly with governance attached).

## 4. Workflow shapes and the graduation path

Each piece of delivery work has a shape, chosen per route, never a maturity scale:

- **Human-led**: a person drives and AI assists. Needs working sign-in and a verified
  skill.
- **Agent-led**: an agent carries the work; a person confirms at defined points. Needs
  the permission layer and the review gate.
- **Autonomous**: the agent runs to a defined outcome within capped iterations and
  spend, and a separate check grades the result. Needs agent identities, scoped
  permissions and an approved place to run.

A route graduates; an organisation does not "become" agentic. Each shape maps onto a
wave, so choosing one tells a team what it is waiting on. Keep this framework apart
from the four gears (which are about people) in any pitch, or they blur.

When a route does graduate, architecture follows the case (practitioner judgement, not
a finding): one agent holding an entire complex case runs out of working context; a
large fan-out multiplies cost by re-reading the same material; the designs that win
are small fixed pipelines, a fast inexpensive step preparing the material, then a
strong model working each bounded part. Decide per case; a standing single-agent or
multi-agent policy in either direction is where cost surprises start.

## 5. Trigger-gated tier decisions

Never upgrade a supplier tier by default. Name the conditions that would make the
upgrade necessary, revisit them quarterly, and move when one fires. The recurring
trigger set for an AI supplier's enterprise tier: agents acting on systems of record
in production; a client or regulator asking for evidence of AI activity; a workload
needing retention or network controls. Do not move for telemetry alone when the
current tier already exposes usable telemetry; collect first, and let the tier
decision follow the requirement. When a trigger fires, negotiate the bundle
(provisioning, audit logs, scanning, retention controls) as one package, because they
arrive together, and model the billing change as well as the feature list. Adoption
counts move fast during an engagement; confirm current seat counts and the supplier's
published minimums before any decision.

## 6. The proof-before-scale companion

Friction can be located without cost being known (pain scores without timings), so
define the measure per initiative before it starts, against the team's own baseline.
In a regulated business the telemetry is the audit and compliance evidence as much as
the value evidence, and assurance is far cheaper to build before scale than to
retrofit. The review gate plus one shared verification pattern is the path from one
person's win to company capability; the memorable finding to reuse: when a skill gives
confidently wrong answers, the root cause is usually the home-made checker.
