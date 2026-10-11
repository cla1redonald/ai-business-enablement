# Skill: draft-map

Build one step-level value stream map from the confirmed evidence, into
`templates/value-stream-map.html`. One file per stream; the map is generated from
data, never hand-copied.

## Inputs

The stream's confirmed observations and opportunities; the template; the facts
manifest for every count on the page.

## Output

The populated map HTML: title (trigger to outcome), coverage strip, the constraint
box, one step article per step in flow order, the how-to-read notes, the footer.

## Rules that bite here

- **Nothing is estimated to fill a gap.** A step with no figures had none in the
  evidence, and the how-to-read note says exactly how many steps carry pain scores
  and timings.
- Per step, capture what the evidence gives: who does it (role), working time, the
  wait before it starts, pain on the simple scale, the system it lives in, and the
  opportunities sitting on the step. Timings carry attribution ("self reported") and
  unresolved differences between two tellings stay unresolved and named.
- **The constraint call carries its five parts**: the evidence, the corroboration,
  the effect (why its delay cannot be absorbed), what would strengthen the call
  (name it provisional if it is), and what is unmeasured. Read the map by its waits
  and its pain, not its busiest steps.
- Maturity tags (think / work / act) only where the evidence places AI in the step
  today.
- Plain language throughout; the room's own verbs; roles never names; every number
  from the facts manifest.
- If the maps were derived from conversations rather than drawn in a room with the
  teams, the method note says so and recommends redrawing the important ones with
  timing before committing (the method lives in the report skeleton's annex D).

## Gate

The consultant reads each map end to end against its stream's evidence before it
enters the pack. Do not grep it; read it.
