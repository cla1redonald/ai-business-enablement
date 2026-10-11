# Results, and what they do and do not show

The README quotes one headline result. This page gives the numbers again with the
caveats that belong to them.

## The result

The kit was distilled from a real engagement: a two-week AI readiness diagnostic. An
earlier, heavier pipeline built by the author had processed that engagement's
evidence. Afterwards the engagement was replayed through this lean rebuild, on the
same confidential corpus.

| Measure | Earlier pipeline | This kit |
|---|---|---|
| Observations extracted | 212 | 438 |
| Observations passing this kit's own mechanical checks (verbatim quote in the cited source, valid locator, no registry name in a claim, valid enums, no quote from a consultant turn). Self-graded: the kit's checker marking the kit's output, so it shows internal consistency, not accuracy against an outside reference | not reported here | 438 of 438 |
| 20-area readiness ratings matched, with the earlier grid in context | n/a (the reference) | 20 of 20 |

## Caveats

**It cannot be reproduced here.** The corpus is confidential client material and is
not in this repository, and neither are the engagement's outputs. The numbers above
are reported by the author. What anyone can rerun is the fixture (`make demo`), which
shows the tools behave as described on invented material, not that the replay
numbers are right.

**438 against 212 is not a like-for-like recall measure.** The rebuild extracts at a
finer granularity: where the earlier pipeline recorded one observation, the rebuild
often records several narrower ones. Some of the gap is fewer misses. Some of it is
the same evidence cut into smaller pieces. The split between the two is not quantified
here, so do not read the ratio as "twice as much was found".

**"Verified" means mechanically verified, and no more.** The observations check
confirms that each quote exists verbatim in the source it cites and that the
structure holds. It cannot tell you that the right things were extracted, that a
quote supports the claim attached to it, or that nothing important was missed. Those
judgements stay with the consultant at the confirm gate.

**The readiness replay was not blind.** The earlier pipeline's 20-area grid was
available in context when the rebuild rated the areas. Reproducing the ratings shows
the instrument and the evidence rules are consistent with the earlier result. It is
a consistency check, not an independent test of whether the ratings are right.

**One engagement, one corpus.** Nothing here says how the kit performs on a different
organisation, sector or transcript quality.

## Where the checker earned its place

On a small hand-built sample of four sources, the observations check caught three
genuine misquotes (one of them a stutter that had been silently cleaned). Those were
fixed against the exact source text. On the Caldergate fixture it caught three
document quotes broken by line-wrapping, which led to whitespace-normalised matching.
Both are small samples, offered as examples of what the check is for, not as a
measured error rate.
