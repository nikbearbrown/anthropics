# CAJAL figure candidates — java-programming (previz track)

Mechanism figures mined from chapter content. Blank unannotated vector — no baked text;
previz owns every label (contract elements, state names …). Okabe-Ito, white bg, 1pt strokes,
no red-green, no 3D perspective, ≤6–8 components.

> De-confliction: this book owns OOP contract/specification and state-machine figures; embedded-ai owns hardware figures.

---

## 1. specification-chain-delegation  — Spec → AI Output → Audit → Accept/Reject → Next  (MC · process flowchart · Critical)
*Source: chapter 03 — "The Conductor's Frame"*

**PASTE:** Draw a blank five-box linear chain on a white background: five equal-size rectangles in a row connected by right-pointing arrows. From the fourth box, a dashed arrow loops back above the chain to the first box (the reject/revise branch). No text.
- [S] single-column 89mm, 300 DPI, vector, white bg, landscape.
- [C] five stages: Specification → AI Output → Human Audit → Accept/Reject decision → Next Component; dashed reject loop returns to Specification; the audit gate is the teaching point.
- [O] left-to-right main flow; reject loop arcs above; Accept/Reject box is the gate node.
- [P] flat vector, Okabe-Ito: Specification Blue #0072B2, AI Output Sky Blue #56B4E9, Human Audit Orange #E69F00, Accept/Reject box Bluish Green #009E73, Next Component Blue #0072B2, forward arrows Black #000000, reject loop dashed Vermillion #D55E00. No baked text.
- [E] exclude: step-label text, handoff condition language, a sixth stage, a second reject path.

**NEGATIVE:** step names, handoff text, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## 2. seven-component-contract-anatomy  — the seven elements of an OOP component contract  (VG · structural · Critical)
*Source: chapter 07 — "Inheritance and the Specification Contract"*

**PASTE:** Draw a blank seven-segment vertical rectangle on a white background: one large rectangle divided into seven horizontal bands by six horizontal lines. Each band is equal height. No labels or text in any band.
- [S] single-column 89mm, 300 DPI, vector, white bg, portrait.
- [C] seven contract elements (top to bottom): Responsibility, Fields, Visibility, Constructor, Methods, Invariants, Shared State; the stacked anatomy is the teaching point.
- [O] top-to-bottom reading order; seven equal-height bands in one rectangle; no sub-divisions within bands.
- [P] flat vector, Okabe-Ito: alternating bands Blue #0072B2 and Sky Blue #56B4E9, outermost border Black #000000. No baked text.
- [E] exclude: contract-element names, example text, a method signature example, an eighth band.

**NEGATIVE:** contract element names, example code, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## 3. lsp-square-rectangle-failure  — three-panel substitution failure sequence  (VG · sequence · Critical)
*Source: chapter 07 — "Inheritance and the Specification Contract"*

**PASTE:** Draw a blank three-panel sequence on a white background: three panels side by side separated by vertical dividers. Panel 1: two boxes connected by an arrow (hierarchy claimed). Panel 2: one box with an invariant checkmark on the right side (behavior expected). Panel 3: the same hierarchy but with an X on the invariant — the checkmark is replaced by an X (substitution fails). No text anywhere.
- [S] single-column 89mm, 300 DPI, vector, white bg, landscape.
- [C] panel 1: Rectangle → Square hierarchy arrow; panel 2: Rectangle with preserved-invariant check mark; panel 3: Square substituted, invariant X (fails); the three-step progression shows structural claim vs. behavioral violation.
- [O] left-to-right three panels; panel 3 is the failure state; X replaces checkmark.
- [P] flat vector, Okabe-Ito: Rectangle boxes Blue #0072B2, Square boxes Sky Blue #56B4E9, hierarchy arrow Black #000000, checkmark Bluish Green #009E73, X mark Vermillion #D55E00. No baked text.
- [E] exclude: UML notation text, method signature text, Java code, a fourth panel.

**NEGATIVE:** UML text, Java code, method signatures, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## 4. event-driven-state-machine  — two diagrams: procedural stack vs. event-driven state graph  (VG · comparison · Important)
*Source: chapter 11 — "Event-Driven Specification"*

**PASTE:** Draw a blank two-panel diagram on a white background. Left panel: a vertical stack of five rectangles connected by downward arrows (linear procedural execution). Right panel: four circles with multiple arrows between them in different directions, some looping (state machine with incoming event arrows from outside the circle boundary). No text or labels.
- [S] single-column 89mm, 300 DPI, vector, white bg, landscape.
- [C] left: procedural linear call stack (top to bottom, deterministic); right: event-driven state machine (multiple nodes, arrows from outside representing external events); the contrast between predictable sequence and indeterminate event-arrival is the teaching point.
- [O] two panels side by side; left = linear stack; right = state graph with external event arrows; equal panel widths.
- [P] flat vector, Okabe-Ito: procedural rectangles Blue #0072B2, procedural arrows Black #000000, state circles Bluish Green #009E73, event arrows Orange #E69F00, external event arrows Vermillion #D55E00. No baked text.
- [E] exclude: state names, event label text, Java listener syntax, a third panel.

**NEGATIVE:** state names, event labels, Java code, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## 5. cascade-failure-propagation  — domain model error radiating to three downstream components  (MC · dependency graph · Critical)
*Source: chapter 16 — "Final Boondoggle Score Defense"*

**PASTE:** Draw a blank hub-and-spoke failure propagation diagram on a white background: one rectangle at the top center (source failure node). Three arrows radiate downward from it to three rectangles arranged in a row below. Each of the three lower rectangles has a small warning triangle in its top-right corner (representing "needs rebuild"). No text.
- [S] single-column 89mm, 300 DPI, vector, white bg, portrait.
- [C] root failure node at top (the domain model); three downstream dependent components below (Repository, Controller, View); warning markers on each downstream node show propagation; the cascade structure is the teaching point.
- [O] top-down from root to three dependents; warning triangles on each downstream node; equal-width arrows.
- [P] flat vector, Okabe-Ito: root failure box Vermillion #D55E00, downstream boxes Blue #0072B2, propagation arrows Orange #E69F00, warning triangles Black #000000 outline with Yellow #F0E442 fill. No baked text.
- [E] exclude: field-name text, Java type annotations, a fourth downstream node, a second root node.

**NEGATIVE:** field names, type annotations, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## 6. call-stack-recursive-growth  — normal recursion vs stack-overflow  (VG · comparison · Important)
*Source: chapter 13 — "Recursion as Problem Decomposition"*

**PASTE:** Draw a blank two-panel call-stack comparison on a white background. Left panel: a tall stack of five rectangles growing downward from a top rectangle, with upward arrows showing unwinding — the bottom rectangle has a checkmark (base case reached). Right panel: the same stack continuing to grow downward past the canvas edge, with a jagged cut-line at the bottom (overflow). No text.
- [S] single-column 89mm, 300 DPI, vector, white bg, landscape.
- [C] left: normal recursion — stack grows down to a base case, then unwinds; right: infinite recursion — stack never reaches a base case, overflows; the base-case checkmark vs. cut-line contrast is the teaching point.
- [O] two panels; left = bounded descent with checkmark; right = unbounded descent with cut-line overflow.
- [P] flat vector, Okabe-Ito: stack frames Blue #0072B2, base-case checkmark Bluish Green #009E73, unwind arrows Orange #E69F00, overflow cut-line Vermillion #D55E00. No baked text.
- [E] exclude: function-name labels, frame-count numbers, Java stack trace text, a third panel.

**NEGATIVE:** function names, frame counts, Java text, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## Video candidates

FIGURE specification-chain-delegation — Status: VIDEO CANDIDATE · Criterion: 2 · Reason: a sequence of causal steps: the student must witness each stage causing the next to understand the mechanism, not merely see the endpoints.
FIGURE seven-component-contract-anatomy — Status: STATIC SUFFICIENT · Criterion: — · Reason: the figure is a spatial cross-section or structural schematic whose value lies in inspecting all parts simultaneously.
FIGURE lsp-square-rectangle-failure — Status: STATIC SUFFICIENT · Criterion: — · Reason: the mechanism is fully carried by arrow direction and shape arrangement in one frame; motion would not add information a careful static figure does not already hold.
FIGURE event-driven-state-machine — Status: STATIC SUFFICIENT · Criterion: — · Reason: the figure is a simultaneous comparison of two or more states; motion would replace side-by-side display with a sequence that the chapter does not assert.
FIGURE cascade-failure-propagation — Status: STATIC SUFFICIENT · Criterion: — · Reason: the value of the figure lies in comparing quantities simultaneously; animating bars or curves removes the measurement it exists to make.
FIGURE call-stack-recursive-growth — Status: STATIC SUFFICIENT · Criterion: — · Reason: the figure is a simultaneous comparison of two or more states; motion would replace side-by-side display with a sequence that the chapter does not assert.

**Chapter recommendation:** **specification-chain-delegation** — the sole video candidate; a sequence of causal steps: the student must witness each stage causing the next to understand the mechanism, not merely see the endpoints.
