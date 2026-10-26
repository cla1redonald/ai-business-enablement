# Diagram templates

There are five HTML diagrams with parameters, rendered from the taxonomy plus the
engagement data, so a new client's versions are generated rather than redrawn. Each file
is self-contained. The render pipeline uses a headless browser to screenshot one file to
one PNG at 2x, which is why the body width and height are fixed in each file.

| File | Shows | Parameterised by |
|---|---|---|
| `enabler-stack.html` | The five enablers as four layers carrying the opportunity load, with Proof as a rail beside them. Dark chips are already in place. | Payload line (opportunity and stream counts); per-layer move chips with done-state |
| `readiness-grid.html` | The 20 areas, five rows of four, cell colour by rating | Area names and ratings from the instrument |
| `enabler-waves.html` | Which moves start in which wave | Three wave columns: label, timing line, move chips |
| `value-pillars.html` | The three pillars with the scope boundary | Pillar descriptions; which are in scope |
| `identity-layers.html` | The three identity layers with the client's position per layer | Per-layer position line and status chip |

These conventions apply.

- On `enabler-stack`, the stack runs from top to bottom, from Adoption and capacity down
  to Trusted information, because the payload rests on adoption and everything rests on
  data. Proof is the rail at the side, measuring all four. This deliberately inverts the
  canonical list order. The canonical order is the order of dependency, and the stack
  draws that dependency.
- The palette and fonts sit in `:root` variables at the top of each file, so you re-skin
  a diagram by changing the variables and nothing else. The defaults are neutral,
  pending the kit's decision on positioning.
- No text goes into a diagram unless it is in the taxonomy or the facts manifest.
