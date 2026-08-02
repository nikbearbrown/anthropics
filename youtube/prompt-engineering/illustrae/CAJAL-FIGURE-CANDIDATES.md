# CAJAL figure candidates — prompt-engineering (previz track)

Mechanism and workflow figures mined from chapter text. Blank unannotated vector — no baked text.
Okabe-Ito, white bg, 1pt strokes, no red-green, no 3D perspective, ≤6–8 components.

---

## 1. four-layer-prompt-architecture  — root/constraints/persona/format as separable architectural layers  (VG · structural schematic · Critical)
*Source: chapter 05 — "The Architect Mindset"*

**PASTE:** Draw a blank four-layer horizontal stack on a white background: four equal-height horizontal rectangles stacked top to bottom inside an outer containing rectangle, separated by thin horizontal rules. Each inner rectangle has a distinct left-edge tab of different widths suggesting separable concern groups. No text, no labels. Uniform strokes, flat fills, no shading.
- [S] single-column 89mm, 300 DPI, vector, white bg, portrait.
- [C] four architectural layers top to bottom: persona (widest left tab), root task (medium tab), constraints (medium tab), format (narrowest tab); outer container is the prompt boundary; tab width encodes the layer's behavioral scope.
- [O] vertical stacked layers; outer rectangle; left-edge tabs of differing widths; thin internal rules between layers.
- [P] flat vector, Okabe-Ito: persona layer Blue #0072B2, root layer Sky Blue #56B4E9, constraints layer Orange #E69F00, format layer Bluish Green #009E73. No baked text.
- [E] exclude: label text inside layers, PAST/PLFR annotations, XML bracket symbols, a fifth layer.

**NEGATIVE:** text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, 3D perspective

---

## 2. react-loop-thought-action-observation  — interleaved reasoning-action-observation cycle that interrupts error compounding  (MC · cycle diagram · Critical)
*Source: chapter 11 — "Agentic and Multi-Turn Systems"*

**PASTE:** Draw a blank three-node clockwise cycle on a white background: three rounded rectangles arranged equidistantly in a triangle, connected by single-headed arrows curving clockwise. One of the three connecting arrows (the one flowing from the Action node to the Observation node) is shown as a differently styled arrow — thicker with a small perpendicular tick — indicating that the Observation token enters from outside the model. No text, no labels. Uniform strokes, flat fills, no shading.
- [S] single-column 89mm, 300 DPI, vector, white bg, square.
- [C] three interleaved stages: Thought (model-generated reasoning), Action (tool call), Observation (externally injected ground-truth token); the Action-to-Observation arrow is differentiated as an external-input edge, not a model-generated arc.
- [O] triangular clockwise cycle; three nodes; three clockwise arrows; Action-to-Observation arrow thicker with external-input marker.
- [P] flat vector, Okabe-Ito: Thought node Blue #0072B2, Action node Orange #E69F00, Observation node Bluish Green #009E73, standard arrows Black #000000, external-input arrow Sky Blue #56B4E9 thick. No baked text.
- [E] exclude: token probability labels, ReAct paper citation, benchmark accuracy numbers, a fourth node.

**NEGATIVE:** text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, 3D perspective

---

## 3. tighten-vs-widen-distribution  — two opposite pattern types on the output-distribution  (VG · comparison panels · Important)
*Source: chapter 08 — "Reasoning and Range Patterns"*

**PASTE:** Draw a blank two-panel comparison on a white background: two square panels side by side. In the left panel, a tall narrow bell curve centered on the horizontal midpoint — suggesting a sharp, peaked distribution. In the right panel, several short, wide low-amplitude curves spread across the horizontal axis — suggesting a flattened, spread distribution. A thin vertical divider separates the panels. No text, no labels. Uniform strokes, flat fills, no shading.
- [S] single-column 89mm, 300 DPI, vector, white bg, landscape.
- [C] two distribution postures: left panel — tightened path (chain-of-thought; one narrow high-probability peak); right panel — widened sample (range patterns; multiple lower-probability modes spread across the space).
- [O] two side-by-side panels; shared horizontal baseline; left panel one tall peak; right panel multiple low spread curves.
- [P] flat vector, Okabe-Ito: left panel curve Blue #0072B2, right panel curves Orange #E69F00, baselines neutral gray, divider neutral gray. No baked text.
- [E] exclude: axis tick marks with numeric values, pattern-name annotations, temperature-knob icon, probability percentages.

**NEGATIVE:** text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, 3D perspective

---

## Video candidates

FIGURE four-layer-prompt-architecture — Status: STATIC SUFFICIENT · Criterion: — · Reason: the figure is a spatial cross-section or structural schematic whose value lies in inspecting all parts simultaneously.
FIGURE react-loop-thought-action-observation — Status: VIDEO CANDIDATE · Criterion: 3 · Reason: a recurring process where the closed nature of the cycle and the change accumulated on each pass are part of the concept, not merely a round arrangement of steps.
FIGURE tighten-vs-widen-distribution — Status: STATIC SUFFICIENT · Criterion: — · Reason: the figure is a simultaneous comparison of two or more states; motion would replace side-by-side display with a sequence that the chapter does not assert.

**Chapter recommendation:** **react-loop-thought-action-observation** — the sole video candidate; a recurring process where the closed nature of the cycle and the change accumulated on each pass are part of the concept, not merely a round arrangement of steps.
