# Enabler 3: Control and accountability

*Is it controlled, and can accountability be traced?* Four areas. What AI is permitted to
do, and who answers for it when it goes wrong, are two questions rather than one, and
they often have different answers.

## 9. AI policy

**Definition.** Whether a real AI policy exists and is doing its job: covering embedded
AI and supplier products as well as assistants, naming accountable owners, requiring
competent human review before reliance, requiring evaluation evidence at approval,
prohibiting final automated decisions with legal or financial effect without oversight,
and mandating training. The strongest clause to look for: applying a human name or
approval to unreviewed AI content does not meet the review requirement.

**What to look for.** The policy itself, read end to end (direct examination). Its
coverage: assistants only, or embedded AI and suppliers too. Named owners. The review
requirement and whether anything implements it (that is area 12's question; here the
question is whether the requirement exists). Training obligations and their cadence.
Whether the policy makes commitments the organisation cannot yet evidence (a monitoring
commitment with no telemetry is the common one): a strong policy that outruns its
evidence is an exposure, not a comfort.

**How to surface it.** Read it. Then: "who owns this day to day?" "When was it last
revised, and what triggers revision?" "Which of its commitments could you demonstrate to
an auditor this week?"

**Rating anchors.**
- In place: the policy exists, covers the full estate, names owners, and its clauses are
  live practice. In place does not mean finished: record where commitments outrun
  evidence, and grade those under Proof rather than here.
- Partial: a policy exists but covers assistants only, sits in draft, or is unknown to
  the people it governs.
- Gap: nothing in writing, or a generic acceptable-use line with no AI substance.
- Blocked: rarely applicable.

**Sequencing note.** Most improvements to a good policy are drafting exercises: writing
down a practice that already exists. Revise now rather than at the annual review;
capability moves faster than an annual cycle, and a certified business has to evidence
what it says it does.

## 10. Supplier and connector approval

**Definition.** Whether new tools and connectors pass a working review with named
approvers and a clear red line (recognised certification is the usual one), and whether
the path scales: one queue handling fast-changing items (skills) and slow-changing items
(connectors, MCP servers) guarantees the fast one waits behind the slow one.

**What to look for.** Whether the review exists and functions today rather than on
paper. Its shape: question count, named approvers, the red-line criterion. Whether
already-approved suppliers connect freely (the right design). Where the friction
concentrates (usually a few named people handling everything manually). Whether skills
and connectors share one path.

**How to surface it.** "What happens when someone wants a new tool or connector?" "Who
are the approvers, and how many requests reach them a month?" "How long does a
fast-moving item wait behind a slow one?"

**Rating anchors.**
- In place: a working review with named approvers, an evidence trail, and paths split by
  pace of change.
- Partial: a real, functioning review that scales only so far: manual per-request
  friction on a few people, one queue for everything, or no record left behind.
- Gap: tools and connectors arrive without review.
- Blocked: approvals frozen pending an unresolved question, with demand queueing.

**Sequencing note.** Split the path by pace of change before volume arrives: fast-moving
items through a lightweight route with a licence check; slow-moving items keep the fuller
security review, with a quick lane for vendors already under contract. Cheaper to design
in than to retrofit.

## 11. Incident response

**Definition.** Whether AI incidents route through the existing incident process, and
whether anything would raise one. The failure modes worth naming (data leakage, prompt
injection, hallucination causing client detriment, shadow AI) leave no trace at the
network layer: a hallucination that reaches a client does not announce itself, and prompt
injection is designed not to. Detection for AI otherwise depends on a person noticing.

**What to look for.** Whether the policy routes AI incidents into the incident process
with the right functions involved (security, compliance, legal or DPO). Whether the
named AI failure modes appear as examples. What the existing detection machinery covers
(DLP, exfiltration, endpoint monitoring cover data movement, not what an AI tool was
asked, produced or reached). Whether any AI-specific trigger exists.

**How to surface it.** "If an AI tool produced something harmful that reached a client,
how would you find out?" "Has an AI incident ever been raised? What would raise one?"
Read the incident process and the acceptable use policy (direct examination).

**Rating anchors.**
- In place: routing sound and an AI-specific detection trigger live (which requires AI
  telemetry; see Proof).
- Partial: the process sound and properly routed, the AI-specific trigger missing.
  This closes when AI telemetry is collected, and not before; say so.
- Gap: no incident process covers AI, or nobody knows AI incidents belong in it.
- Blocked: rarely applicable.

## 12. Output verification

**Definition.** Whether the review-before-reliance requirement is implemented and
recorded, rather than remembered. Verification belongs inside the tools rather than in a
clause people are asked to remember: a skill that carries its own checks is enforceable,
a written requirement is not. The widest policy-to-practice distance in most assessments,
and the one with the clearest fix.

**What to look for.** Whether anything implements the policy's review requirement and
whether any review is recorded. What happened during builds: outputs that would not have
been safe to rely on, caught only because the builder was close to the work. Whether any
evaluation harness or scorecard exists, per skill or shared. Home-made checkers (when a
skill gives confidently wrong answers, the root cause is usually the home-made checker).
Whether anything would catch a wrong answer once a tool is used by people who did not
build it, which is exactly when it becomes useful enough to be relied on.

**How to surface it.** "How do you know this skill's answers are right?" "Show me the
record of a review before something was relied on." "Who agreed what correct looks
like?"

**Rating anchors.**
- In place: a shared verification pattern in use (cases run, checks applied, results
  recorded), with sign-off recording its own boundary: a specific capability against
  specific criteria, never AI for a function in general.
- Partial: verification exists for some published capability, or one worked evaluation
  is in flight as a deliberate first instance.
- Gap: the policy requires review, nothing implements it, nothing records it.
- Blocked: rarely applicable.

**Sequencing note.** Finish the first evaluation before starting a second. One finished
example of verification living inside a tool is worth more than three started ones, and
it becomes the template the review gate points at.
