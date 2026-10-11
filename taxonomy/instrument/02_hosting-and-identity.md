# Enabler 2: Hosting and identity

*Where does AI run, and under whose identity?* Four areas. Where AI runs, and as whom,
determines what can safely be built on top of it. This theme decides how far agentic
ambition can go, and it is usually where the assessment finds the widest distance between
what an organisation is trying to do and what it has built to do it on.

## 5. Assistant estate

**Definition.** Whether the surfaces where AI runs are known and deliberately chosen: the
licensed assistants, the per-team tools, and the AI embedded in software bought for other
reasons. The gap is usually inventory rather than control: a real policy governing a list
nobody has written down.

**What to look for.** The licensed assistant(s) and seat counts. Any deliberate tool
splits between populations (engineering on a different tool is common; note whether the
split was a decision or a drift, and whether the second tool is now doing knowledge work
beyond its original case, which duplicates the connector estate and its governance). AI
features embedded in the existing SaaS estate (finance, email, files, chat, CRM), none
of which passed through an AI decision. Whether guidance exists on which tool to reach
for and when. Usually needs direct examination: build the list in the room with IT.

**How to surface it.** "List every place AI runs here" (then extend it together with the
SaaS estate). "Was the tool split a decision? What does the second tool get used for
now?" "If a new starter asked which AI tool to use for a task, what would they be told?"

**Rating anchors.**
- In place: a current inventory of AI surfaces, guidance on which tool when, and embedded
  AI treated as part of the estate.
- Partial: the main assistants known and licensed deliberately, but embedded AI
  unenumerated and tool-choice guidance absent.
- Gap: nobody can list where AI runs; adoption is tool-by-tool drift.
- Blocked: rarely applicable; use only if enumeration is actively prevented.

**Sequencing note.** Enumerating is not rationalising, and the two are easily confused.
The list is an hour of work and among the most useful items in the report; unpicking a
deliberate tool split is a separate, later question that should be argued from evidence
of duplicated effort, not tidiness.

## 6. Agent hosting

**Definition.** Whether there is an approved place for automations and agents to run that
is not an individual's machine: a runtime, scheduling, and enough logging to know when
something failed. Without it, every automation depends on a person's laptop being open,
their session live and their credentials current.

**What to look for.** Where anything unattended runs today. Whether engineering has
solved hosting for its own work (it usually has) and whether that pattern has left
engineering. Whether the cloud primitives the organisation already pays for (compute,
identity, secrets, scheduling, monitoring) have been applied to this. Whether a managed
agent runtime from the model provider is in use or under evaluation. Who is "on the cusp
of asking how to host things properly" (there is usually someone mailing HTML files
around).

**How to surface it.** "What happens to your automations when the person who built them
is on holiday?" "Where would a scheduled agent run today if a team asked for one this
week?" "What has engineering already solved here, and could anyone else use it?"

**Rating anchors.**
- In place: a defined, approved runtime for business automations with scheduling and
  logging, in actual use beyond engineering.
- Partial: a runtime exists for one population (usually engineering) or a managed route
  is chosen and being tested; the business at large still runs on laptops.
- Gap: nothing runs anywhere except on individuals' machines.
- Blocked: an approved runtime is formally prevented (security posture, data residency)
  with no agreed alternative.

**Sequencing note.** The route matters more than the destination: whatever the first
hosted agent runs on becomes the pattern, and the identity it authenticates as becomes
the precedent, chosen deliberately or not. A managed runtime is the credible first move
for a team with no capacity to build, because it requires the least build; hold
self-hosting until a first managed test has run, and date the revisit rather than
leaving it open.

## 7. Identity and service accounts

**Definition.** Whether automations can run as the business rather than as a person:
service identities with managed credentials, a settled identity provider direction, and
joiner-mover-leaver events that reach the AI estate. An automation on personal
credentials either stops working when its author leaves or keeps running on credentials
that should have been revoked; neither is discovered until something goes wrong.

**What to look for.** How sign-in works and whether an identity provider move is under
consideration (an unsettled IdP decision changes how every connector and agent
authenticates, so it is cheaper to settle before more of them exist). Whether anything
defines how a business-critical automation should run as a service account. Which
automations already run as their authors. Whether the plan tier of the AI supplier caps
provisioning automation (joiner and leaver events staying manual is a common tier
boundary). What the policy says about approved identities, and whether personal-credential
automations satisfy it in letter only.

**How to surface it.** "What does your most business-critical automation authenticate
as?" "What happens to it the day its author leaves?" "Is an identity provider change
under consideration, and who owns that decision?" Direct examination of the identity
model; nobody raises it unprompted.

**Rating anchors.**
- In place: service identities defined and used for unattended work, credentials
  managed, lifecycle events automated to the extent the tier allows, IdP direction
  settled.
- Partial: single sign-on works and seats are managed, but automations run as
  individuals and no service-account pattern exists.
- Gap: identity for AI is whatever each person's login happens to be, and the IdP
  question is open with no owner.
- Blocked: the identity rollout everything waits on is stalled with no date.

## 8. Permission scoping

**Definition.** Whether connector and agent permissions are deliberately scoped and
recorded: least privilege practised rather than merely stated. Most connectors grant
everything once approved, which combined with connected email is a live prompt-injection
exposure; scoped permissions bound the blast radius without removing it.

**What to look for.** Whether new connectors start from no permissions or from
everything. Whether a record exists of what each connector can reach. Whether write
permissions get a harder look than read. Whether the policy states least privilege while
no technical control enforces it (a policy naming a risk it cannot enforce is the
recognisable shape). Whether the supplier tier limits fine-grained access control, making
scoping a commercial question as well as a configuration one.

**How to surface it.** "Show me what this connector can reach" (direct examination).
"When you approved it, what did you scope?" "Which connectors have write access to
anything?"

**Rating anchors.**
- In place: read-only defaults for new connectors, per-connector grants recorded, write
  access individually justified.
- Partial: the principle in policy and some deliberate scoping practised, but no record
  and no default.
- Gap: grants are whatever the connector asked for; no record of what anything can
  reach.
- Blocked: scoping is impossible on the current tier for a connector the business
  depends on, and the tier decision is unowned.

**Sequencing note.** Make read-only the default at the moment connector count starts to
grow (typically when an internal marketplace opens). A default applied across a populated
estate is a migration; applied early it is a setting. Record what each connector reaches
while the list is still short.
