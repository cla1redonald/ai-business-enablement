# Hosting, identity and security: the deep-dive module

This is the engagement's technical annex material, split out so that it can be sold on
its own. For any regulated client it is a natural follow-on after the fast diagnostic,
and for a buyer who thinks like a CTO it stands up as a piece of work by itself.
Everything here is framework, and the client's own positions fill the slots when it
runs.

## 1. The three identity layers (they fail independently)

**Layer one is who can sign in.** This covers the identity provider, how seats are
managed and how a leaver is blocked. It usually works, is often manual, and copes at the
current scale. One finding comes up again and again at this layer. Two sign-in
mechanisms run side by side (SAML and OAuth), so a person can appear to authenticate
through one while actually using the other. That gap belongs inside the scope of the
identity rollout, with a named owner.

**Layer two is what a signed-in person's AI can reach.** Connectors inherit the
permissions of the person using them, so **the AI layer is exactly as trustworthy as the
permission model in each connected system**. An identity rollout has to make those
permissions deliberate and current everywhere, with one place where joiner, mover and
leaver events set permissions across every connected system.

Two caveats should be stated plainly with any such rollout. First, the AI supplier's
tier can limit what the rollout automates. Provisioning through SCIM is commonly a
higher-tier feature, so lifecycle events in the AI tool stay manual until the client
moves up a tier. Second, the rollout governs who reaches each application, not what they
may do inside it. Per-user AI access depends on each connected system's own permission
model, so cleaning up permissions system by system remains a separate piece of work.

**Layer three is what runs when nobody is signed in.** Agents need identities of their
own. They need service accounts, so an automation survives its author leaving. They need
scoped permissions, ideally with short-lived credentials brokered at the boundary so
that an agent never holds a long-lived key. And they need an approved place to run, with
per-user authentication on shared agents. This is the layer every ambition for agents
depends on, and most organisations have nothing in it.

Keep the basic position in proportion. An organisation with no standing agents, only
skills and subagents inside signed-in sessions, is secure by default, because a run can
never see more than its user may. The same fact limits it. An automation stops on the
day its author leaves, and no run can serve a workflow wider than its owner can see.

Scoping permissions is more than good hygiene. Most connectors grant everything once
they are approved, and combined with connected email that is a live exposure to prompt
injection. Scoped permissions limit how much damage is possible without removing the
risk. That makes scoping first-wave work with a named owner, and it still needs regular
review afterwards.

## 2. The agent infrastructure layers (a framework for judgement, not an assessment)

Running agents in production is a different discipline from using a chat assistant well.
There are six layers, and the client is assessed on where it stands on each.

1. **Standardised tool access.** This is how a model reaches a system with permissions
   attached, in other words the connector estate. It is often the layer where the client
   is strongest without knowing it.
2. **Live retrieval rather than a stale index.** Connectors that query the source at the
   moment of asking do better than a retrieval index, which is correct on the day it is
   built and wrong from then on. Structure the source first, and only consider anything
   semantic once the structure is settled.
3. **Orchestration.** Something has to run a multi-step task, retry what fails and stop
   what loops. It is commonly present in engineering and missing everywhere else.
4. **Memory and state.** This is where a long-running agent keeps its state between
   runs. It is rarely a live constraint early on, and it is a design decision rather
   than a setting.
5. **Sandboxed execution.** Code carried by skills needs somewhere to run that is
   neither a person's laptop nor production. Reviewing code is not the same as
   containing it.
6. **Security and observability.** This is a trace of what an agent did, what it reached
   and what it cost. It is the weakest layer almost everywhere, and it matters more for
   agents than for assistants, because an agent takes actions instead of only producing
   text.

The usual reading is that the hardest layer, tool access, is largely in place, and the
layers that make agents safe to run (isolation, orchestration and observability) are
missing. Those need a first candidate to build around, not a whole programme.

## 3. The routes to running agents

Set out the options with what each one assumes, and recommend the managed route first.

- **Managed agents, hosted by the model provider.** There is almost nothing to build,
  and identity, execution and scheduling come with the service. The cost is less
  control, less reach inside the network, and more dependence on one vendor. For a
  business with no platform capacity to spare, that is a trade worth making.
- **Building on the existing cloud estate.** The building blocks are there (compute,
  IAM, secrets, scheduling, monitoring), and this route reaches internal systems
  properly. It is also a platform, and a platform needs an owner, a backlog and
  maintenance. Committing to it without the capacity means committing to something
  nobody can look after.
- **The workflow tool already licensed.** A general workflow engine makes a reasonable
  orchestration layer and a poor agent layer. It schedules and connects things well, but
  it does not give an agent identity, isolation or evaluation.
- **Whatever engineering already runs.** Engineering has usually solved hosting for its
  own work. Ask what they use before choosing anything for the business, because
  adopting an internal pattern that already works is cheaper than picking one from
  outside.
- **Doing nothing, and accepting the ceiling.** This is a fair choice for another
  quarter, provided it is chosen deliberately rather than drifted into, and nobody
  expects it to scale.

The principle behind recommending the managed route first is to own as little as the
data allows. Self-hosting has to be justified by the case, and is never the default. Two
questions decide the choice. Who supplies the machinery that runs the agent, and who
supplies the environment it runs in? Check features, regions and data residency against
the workload. Judge against the models that are coming as well as the ones available
today, because the managed route picks up every model improvement without further work.
Whatever the first hosted agent runs on becomes the pattern, and the identity it
authenticates as becomes the precedent. So settle both in the same piece of work, and
put a date on revisiting self-hosting instead of leaving it open.

While almost nothing is built yet, adopt one design principle. Keep execution,
orchestration and data as separate layers, rather than letting one vendor cover all
three. That keeps the option of changing one layer without rebuilding the others, and it
is the honest answer to the worry about depending on one vendor that the managed route
raises.

Whichever route is chosen, set out what operating at scale would need, so that the first
step is taken knowing where it leads. Present it as context, not as a proposal.
Operating at scale needs a register of what runs, who owns each item and what it
reaches. It needs an identity for each agent, with managed credentials, and isolated
execution. It needs evaluation that runs before any change ships, observability covering
what each agent did, touched and cost, and a named operator whose job includes all of
this. The managed route buys time on every one of those requirements and removes none of
them permanently. They stop being avoidable at roughly the point where the internal
marketplace succeeds.

Two findings from published research are worth carrying, once you have checked they are
still current. The first warns against over-preparing. Imperfect data should not stop
progress, and high-value cases can be piloted in fragmented environments, so the finding
about internal data must not turn into "nothing can start". The second warns against
under-estimating the work. Fewer than one in ten agentic programmes reach meaningful
scale, and the reason is rarely the model. It is fragmentation, missing controls and
absent lifecycle management, which is the argument for doing one thing properly with
governance attached.

## 4. Workflow shapes and the graduation path

Each piece of delivery work has a shape, chosen route by route. The shapes are not a
maturity scale.

- **Human-led.** A person drives and AI assists. This needs working sign-in and a
  verified skill.
- **Agent-led.** An agent carries the work, and a person confirms at defined points.
  This needs the permission layer and the review gate.
- **Autonomous.** The agent runs to a defined outcome within capped iterations and
  spend, and a separate check grades the result. This needs agent identities, scoped
  permissions and an approved place to run.

A route graduates from one shape to the next. An organisation does not "become" agentic.
Each shape maps onto a wave, so choosing a shape tells a team what it is waiting on. In
any pitch, keep this framework separate from the four gears, which are about people, or
the two will blur together.

When a route does graduate, the architecture should follow the case. This is
practitioner judgement rather than a finding from the engagement. A single agent holding
an entire complex case runs out of working context, and a large fan-out multiplies the
cost by re-reading the same material. The designs that work best are small fixed
pipelines, where a fast, inexpensive step prepares the material and a strong model then
works through each bounded part. Decide case by case. A standing policy of always using
one agent, or always using many, is where cost surprises start.

## 5. Tier decisions, made when a trigger fires

Never move up a supplier tier by default. Name the conditions that would make the
upgrade necessary, review them every quarter, and move when one of them happens. For an
AI supplier's enterprise tier, the usual triggers are agents acting on systems of record
in production, a client or regulator asking for evidence of AI activity, and a workload
that needs retention or network controls. Do not move just to get telemetry when the
current tier already exposes telemetry you can use. Collect it first, and let the tier
decision follow the requirement. When a trigger does fire, negotiate the bundle
(provisioning, audit logs, scanning, retention controls) as one package, because these
arrive together, and model the change in billing as well as the list of features.
Adoption counts move quickly during an engagement, so confirm the current seat counts
and the supplier's published minimums before any decision.

## 6. Proof before scale

Friction can be located without anyone knowing what it costs, for example from pain
scores collected without timings. So define the measure for each initiative before it
starts, against the team's own baseline. In a regulated business, the telemetry is
evidence for audit and compliance as much as evidence of value, and assurance is far
cheaper to build before scale than to add afterwards. The review gate plus one shared
verification pattern is how one person's win becomes something the whole company can
use. The finding worth repeating to clients is this one. When a skill gives confidently
wrong answers, the root cause is usually the home-made checker.
