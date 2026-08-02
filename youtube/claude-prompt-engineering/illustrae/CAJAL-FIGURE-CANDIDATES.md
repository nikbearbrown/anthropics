# CAJAL figure candidates — claude-prompt-engineering (previz track)

Mechanism and workflow figures mined from chapter text. Blank unannotated vector — no baked text.
Okabe-Ito, white bg, 1pt strokes, no red-green, no 3D perspective, ≤6–8 components.

---

## 1. six-component-prompt-anatomy  — six separable components of a well-specified prompt  (VG · structural schematic · Critical)
*Source: chapter 01 — "Anatomy of a Claude Prompt"*

**PASTE:** Draw a blank six-panel stacked horizontal schematic on a white background: six equal-height horizontal rectangles stacked from top to bottom inside one outer containing rectangle, each inner rectangle separated by thin horizontal rules. The first and last rectangles have slightly taller height than the middle four. No text, no labels. Uniform strokes, flat fills, no shading.
- [S] single-column 89mm, 300 DPI, vector, white bg, portrait.
- [C] six prompt components stacked top to bottom: role/persona (tall), task description, source material (tall), constraints, evaluation criteria, output format; outer container is the prompt boundary.
- [O] vertical stacked layers inside outer rectangle; role and source slightly taller (highest-leverage components); thin internal rules between layers.
- [P] flat vector, Okabe-Ito: role layer Blue #0072B2, task layer Sky Blue #56B4E9, source layer Orange #E69F00, constraints layer Bluish Green #009E73, evaluation layer Reddish Purple #CC79A7, format layer neutral gray. No baked text.
- [E] exclude: XML tag symbols on layer boundaries, specific example text inside layers, a seventh layer.

**NEGATIVE:** text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, 3D perspective

---

## 2. agentic-handoff-scope-gate-boundary  — three required elements of a Claude Code / Cowork handoff prompt  (VG · systems diagram · Important)
*Source: chapter 11 — "Prompts as Handoffs to Claude Code and Cowork"*

**PASTE:** Draw a blank triangular three-node diagram on a white background: three rounded rectangles arranged at the corners of an equilateral triangle, connected by double-headed arrows along each edge. A small central circle at the centroid of the triangle. No text, no labels. Uniform strokes, flat fills, no shading.
- [S] single-column 89mm, 300 DPI, vector, white bg, square.
- [C] three handoff elements as corner nodes: scope (what workspace is permitted), authorization (what actions are allowed), boundary (what must not be done); central circle represents the approved agentic action; bidirectional edges indicate mutual constraint.
- [O] triangular arrangement; three corner nodes; central node; six edge arrows (two per edge, bidirectional); centroid circle.
- [P] flat vector, Okabe-Ito: scope node Blue #0072B2, authorization node Orange #E69F00, boundary node Bluish Green #009E73, central circle Reddish Purple #CC79A7, arrows neutral gray. No baked text.
- [E] exclude: text labels inside nodes, specific task examples, approval-gate symbol on edges, a fourth node.

**NEGATIVE:** text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, 3D perspective

---

## Video candidates

FIGURE six-component-prompt-anatomy — Status: STATIC SUFFICIENT · Criterion: — · Reason: the figure is a spatial cross-section or structural schematic whose value lies in inspecting all parts simultaneously.
FIGURE agentic-handoff-scope-gate-boundary — Status: STATIC SUFFICIENT · Criterion: — · Reason: the mechanism is fully carried by arrow direction and shape arrangement in one frame; motion would not add information a careful static figure does not already hold.

**Chapter recommendation:** None — no entry in this file clears the motion bar; static figures serve every concept here.
