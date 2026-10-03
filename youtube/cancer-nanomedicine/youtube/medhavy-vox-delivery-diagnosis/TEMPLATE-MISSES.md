# TEMPLATE-MISSES.md — medhavy-vox-delivery-diagnosis

Beats whose original shot INTENT is a custom manim diagram that has no scene
class in `runtime/manim/animated_graphics.py`. This pass ships them as
FormACard slates with authored insight lines so the review cut is coherent
and audible; the diagram intent is preserved in `graphic.production_viz.*`
for a later authoring pass.

| Beat | Diagram intent (label) | Would need | Shipped as |
|---|---|---|---|
| B04 | one outcome, two opposite causes | `B04_TwoCauses` manim scene: crimson centre box → two upward crimson arrows to DRUG TOO WEAK and PARTICLE NEVER ARRIVED | FormACard: "Same outcome. Opposite causes." |
| B05 | opposite causes, opposite fixes | `B05_OppositeFixes` manim scene: two columns (DRUG FAILURE / DELIVERY FAILURE) with crimson cause + teal fix labels | FormACard: "Opposite causes. Opposite fixes." |
| B07 | label the particle, track it | `B07_LabeledParticle` manim scene: centre particle with three SLATE chips (fluorescent dye / iron oxide / radiolabel) + scanning line across a body outline | FormACard: "Label the particle. Track it." |
| B09 | delivery failure → fix the particle | `B09_DeliveryFix` manim scene: crimson top chip PARTICLES IN LIVER/SPLEEN, three teal fix chips (PEG / SIZE / SURFACE CHARGE) below with left-pointing arrows | FormACard: "Particles in liver: fix the particle." |
| B11 | two programs, same particle — illustrative | `B11_TwoPrograms` manim scene: two columns with bar chart. `runtime/remotion/src/scenes/BarChart.tsx` exists and could carry the LIVER 75%+ vs TUMOR <3% bars — worth a follow-up. | FormACard: "Same particle. Different knowledge." |

Each of these lines is a compressed insight drawn from the beat's own
`production_viz.label` / `mechanic` — not the narration. The `graphic.production_viz`
block is retained in every beat as the spec for future authoring.
