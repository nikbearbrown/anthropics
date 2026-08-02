# CAJAL figure candidates — prompt-engineering-old (previz track)

Mechanism and workflow figures mined from chapter text. Blank unannotated vector — no baked text.
Okabe-Ito, white bg, 1pt strokes, no red-green, no 3D perspective, ≤6–8 components.

> Note: prompt-engineering-old shares substantial content overlap with prompt-engineering.
> Unique candidates below reflect chapters present in the old edition not duplicated above.

---

## 1. four-layer-prompt-architecture  — root/constraints/persona/format as separable architectural layers  (VG · structural schematic · Critical)
*Source: chapter 05 — "The Architect Mindset"*

**PASTE:** Draw a blank four-layer horizontal stack on a white background: four equal-height horizontal rectangles stacked top to bottom inside an outer containing rectangle, separated by thin horizontal rules. Each inner rectangle has a distinct left-edge tab of different widths. No text, no labels. Uniform strokes, flat fills, no shading.
- [S] single-column 89mm, 300 DPI, vector, white bg, portrait.
- [C] four architectural layers top to bottom: persona (widest tab), root task (medium tab), constraints (medium tab), format (narrowest tab); outer container is the prompt boundary; tab width encodes behavioral scope.
- [O] vertical stacked layers; outer rectangle; left-edge tabs of differing widths; thin internal rules between layers.
- [P] flat vector, Okabe-Ito: persona layer Blue #0072B2, root layer Sky Blue #56B4E9, constraints layer Orange #E69F00, format layer Bluish Green #009E73. No baked text.
- [E] exclude: label text inside layers, XML bracket symbols, a fifth layer.

**NEGATIVE:** text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, 3D perspective

---

## 2. react-loop-thought-action-observation  — interleaved reasoning-action-observation cycle  (MC · cycle diagram · Critical)
*Source: chapter 11 — "Agentic and Multi-Turn Systems"*

**PASTE:** Draw a blank three-node clockwise cycle on a white background: three rounded rectangles arranged equidistantly in a triangle, connected by single-headed clockwise arrows. One arrow (Action-to-Observation) is thicker with a perpendicular tick, indicating an external-input edge. No text, no labels.
- [S] single-column 89mm, 300 DPI, vector, white bg, square.
- [C] Thought (model-generated reasoning), Action (tool call), Observation (externally injected ground-truth); the Action-to-Observation arrow differentiated as external-input edge.
- [O] triangular clockwise cycle; three clockwise arrows; one thicker external-input arrow.
- [P] flat vector, Okabe-Ito: Thought Blue #0072B2, Action Orange #E69F00, Observation Bluish Green #009E73, standard arrows Black, external arrow Sky Blue #56B4E9 thick. No baked text.
- [E] exclude: ReAct paper citation, benchmark numbers, token probability labels, a fourth node.

**NEGATIVE:** text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, 3D perspective

---

## Video candidates

FIGURE four-layer-prompt-architecture — Status: STATIC SUFFICIENT · Criterion: — · Reason: the figure is a spatial cross-section or structural schematic whose value lies in inspecting all parts simultaneously.
FIGURE react-loop-thought-action-observation — Status: VIDEO CANDIDATE · Criterion: 3 · Reason: a recurring process where the closed nature of the cycle and the change accumulated on each pass are part of the concept, not merely a round arrangement of steps.

**Chapter recommendation:** **react-loop-thought-action-observation** — the sole video candidate; a recurring process where the closed nature of the cycle and the change accumulated on each pass are part of the concept, not merely a round arrangement of steps.
