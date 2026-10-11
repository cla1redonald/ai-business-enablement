# Diagram templates

Five parameterised HTML diagrams, rendered from the taxonomy plus engagement data, so a
new client's versions are generated, not redrawn. Each file is self-contained (the
render pipeline screenshots one file to one PNG at 2x with a headless browser; body
width and height are fixed per file for that reason).

| File | Shows | Parameterised by |
|---|---|---|
| `enabler-stack.html` | The five enablers as four layers carrying the opportunity load, with Proof as a rail beside them. Dark chips are already in place. | Payload line (opportunity and stream counts); per-layer move chips with done-state |
| `readiness-grid.html` | The 20 areas, five rows of four, cell colour by rating | Area names and ratings from the instrument |
| `enabler-waves.html` | Which moves start in which wave | Three wave columns: label, timing line, move chips |
| `value-pillars.html` | The three pillars with the scope boundary | Pillar descriptions; which are in scope |
| `identity-layers.html` | The three identity layers with the client's position per layer | Per-layer position line and status chip |

Conventions:

- Stack order on `enabler-stack` runs top-down from Adoption and capacity to Trusted
  information (the payload rests on adoption; everything rests on data), with Proof as
  the side rail measuring all four. This inverts the canonical list order deliberately:
  the canonical order is dependency order, the stack draws it.
- Palette and fonts sit in `:root` variables at the top of each file; re-skin by
  changing the variables only. The defaults are neutral pending the kit's positioning
  decision.
- No text enters a diagram that is not in the taxonomy or the facts manifest.
