# The five enablers

An **enabler** is something that has to be true before AI capability can be built on it
safely and at scale. The five enablers are also the five themes of the readiness
assessment. The same frame runs from the assessment to the build plan, with the same
names, because the themes the assessment rates are exactly what gets built.

## Canonical order

The order is deliberate. It follows what an AI system depends on rather than how a business
is organised, and each enabler rests on the one above it. Use this order in the instrument,
the report, the diagrams and the workbook alike. Do not re-sort by rating, size or
alphabet.

1. **Trusted information.** Whether the data and documents AI needs can be reached and
   relied on. Nothing else works if AI cannot reach what it needs, or cannot rely on what
   it finds. *Key question: can AI reach information that can be trusted?*
2. **Hosting and identity.** Where AI runs, and who it acts as when it does. This
   determines what can safely be built on top. *Key question: where does AI run, and under
   whose identity?*
3. **Control and accountability.** The policy, review and approval machinery that makes AI
   use defensible. What AI is permitted to do, and who answers for it when it goes wrong,
   are two questions rather than one, and they often have different answers. *Key question:
   is it controlled, and can accountability be traced?*
4. **Proof.** Whether anything can be measured, evidenced and shown to have paid back. What
   can be seen and what can be shown to someone who asks are different bars, and the gap
   between them is usually where an assessment finds the most. *Key question: can you see,
   and evidence, what is happening?*
5. **Adoption and capacity.** Whether people have the time, practice and ownership to use
   what is built. This is where most programmes of this kind succeed or quietly stop.
   *Key question: can the organisation use this, and sustain it?*

## The proof pattern

Every enabler is proved by a first business outcome, never by its own completion. An
enabler pays back only when a business outcome is delivered across it, so never run an
enabler bare. Every wave of enabling work pairs groundwork with a visible win. State each
enabler's proof when it is proposed. Typical shapes:

| Enabler | Proved by |
|---|---|
| Trusted information | Trusted reporting from connected sources |
| Hosting and identity | Per-user AI access to systems of record |
| Control and accountability | Capability publishing safely through the governed route |
| Proof | Baselines captured on the first work the other enablers unlock |
| Adoption and capacity | Teams actually testing what is built |

## The bridge

The signature analytical move, connecting discovery to recommendation:

1. Discovery records **opportunities** (typically a large number).
2. Taken one at a time they invite that many separate arguments. Grouped by what holds them
   back, they reduce to a handful of **root causes**.
3. A short list of **enablers** clears the root causes. Expect one root cause that needs
   decisions rather than groundwork (typically handoffs between teams); it holds the work
   that can start first.
4. Inside the enablers, the discovery evidence sizes **enabling gaps**, each with a count
   of opportunities waiting on it. The gap counts are what turn a diagnosis into a
   sequence.

The pitch line: appetite is not the limit; groundwork is.

## Two instruments, kept apart

The kit rates readiness and sizes gaps with two different instruments, and they must never
be merged or summed against each other.

- The **readiness areas** (20, four per enabler) rate the ground: how ready the
  organisation is, area by area, on the four-value scale. They come from the instrument in
  `instrument/`.
- The **enabling gaps** are sized pieces of groundwork found by the discovery, each rated
  for the gap itself and carrying an opportunities-waiting count. The discovery sizes gaps,
  not programmes, so some enabler content (an identity rollout, measurement moves) rightly
  appears without a gap count.

The two tables will not add up to each other. That is by design. Say so in the report
before a reader notices.
