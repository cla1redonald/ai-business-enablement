# Skill: summarise-call

Turn one raw conversation source (a transcript with frontmatter) into the pack-facing
call summary: the conversation layer of the evidence base. The summary is a navigation
aid; the transcript stays the evidence. Never let summaries replace transcripts
downstream: a summarised corpus is a lossy corpus.

## Inputs

One transcript file carrying `participants:` and `speaker_labels:` frontmatter, plus
the engagement's source sub-type declaration (discovery interview, consultant-led
session, client-shared summary).

## Output

One markdown summary: session token, date, sub-type, roles present (tokens only), then
sections: what the session covered; the processes described (each with frequency,
duration, people, where it stalls, as stated); handoff pains; **numbers said, verbatim
with who said them** (by role token); tools named; tried and abandoned, and why;
contradictions with other accounts; who to talk to next.

## Rules that bite here

- Identify the consultant from `participants:` matched against the configured
  consultant identity, then find their label in `speaker_labels:`. Never assume "Me"
  or the host label is the consultant.
- Consultant turns are context, never content: summarise what the client said, with
  the consultant's question kept only where the answer needs it to be interpretable.
  Second-hand relay by the consultant is kept, marked indirect.
- Preserve every number verbatim with its speaker role. A number said in passing is
  the most valuable thing in the file; a summary that drops the quantified statements
  has failed regardless of how well it reads.
- **Quotes carry the transcript's noise; prose carries the meaning.** Speech-to-text
  garbles words ("border ports" for board reports). A quoted span stays verbatim,
  noise included, because the quote's job is to be findable in the source; the
  summary's prose normalises the meaning around it. Never "fix" a quote, and never
  quote a garbled span where the reading is genuinely uncertain: paraphrase and say
  the transcript is unclear.
- Roles, never names, including vocatives buried in speech; seed the sweep from
  `participants:`. Tokenise prospect and customer company names.
- Refuse a source whose speakers cannot be attributed (no participants, no labels):
  say so rather than guessing.
- If the recording failed and only recollection exists, the summary is marked
  consultant recollection, usable as background and refused as evidence; prefer the
  client's own summary of the call if one can be asked for.

## Gate

The consultant reads each summary before it enters the pack. Summaries ship in the
client pack; write them as shareable from the first line.
