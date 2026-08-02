# CAJAL figure candidates — prompt-engineering-with-clis (previz track)

Mechanism and workflow figures mined from chapter text. Blank unannotated vector — no baked text.
Okabe-Ito, white bg, 1pt strokes, no red-green, no 3D perspective, ≤6–8 components.

---

## 1. static-vs-dynamic-context-partition  — two-halves model of an agent's context window  (VG · comparison panels · Critical)
*Source: chapter 02 — "The Agent's Context System: Static vs Dynamic Context"*

**PASTE:** Draw a blank two-panel vertical split on a white background: one large outer rectangle divided vertically into two panels by a thick center divider line. The left panel contains three thin horizontal bands stacked from top to bottom, all of equal height and aligned left — representing authored, always-loaded content. The right panel shows a growing stack of bands that increase in density from top to bottom, with the bands in the lower half denser and slightly jagged-edged — suggesting accumulating dynamic content. No text, no labels. Uniform strokes, flat fills, no shading.
- [S] single-column 89mm, 300 DPI, vector, white bg, landscape.
- [C] left panel (static context): three equal stable bands — system prompt, CLAUDE.md instructions, always-loaded rules; right panel (dynamic context): accumulating bands growing denser — file reads, command output, conversation turns; thick center divider marks the boundary.
- [O] two-panel vertical split; left panel stable bands; right panel growing bands; center divider; outer containing rectangle.
- [P] flat vector, Okabe-Ito: left panel bands Blue #0072B2, left panel background light gray, right panel early bands Sky Blue #56B4E9, right panel late/dense bands Orange #E69F00, center divider Black #000000. No baked text.
- [E] exclude: specific file names inside bands, turn-number annotations, a third panel, token-count numbers.

**NEGATIVE:** text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, 3D perspective

---

## 2. progressive-disclosure-index-docs  — always-loaded index vs on-demand domain docs architecture  (MC · systems diagram · Critical)
*Source: chapter 05 — "Progressive Disclosure and the agent_docs Pattern"*

**PASTE:** Draw a blank two-tier architecture diagram on a white background: at the top, a small narrow rectangle (the always-loaded index). Below it, three medium rectangles arranged in a row (the on-demand domain docs). A single thin line connects the index rectangle to each of the three domain-doc rectangles below — these connecting lines are dashed, suggesting conditional access. One of the three lower rectangles has a bold border, indicating it is the currently-triggered doc. Uniform strokes, flat fills, no shading, no text.
- [S] single-column 89mm, 300 DPI, vector, white bg, portrait.
- [C] always-loaded index (top, narrow): the tiny pointer file; three domain docs (bottom): agent_docs/domain-A, domain-B, domain-C; dashed connection lines (conditional on task-trigger); one doc highlighted with bold border (currently loaded).
- [O] two-tier vertical hierarchy; index at top; domain docs below; dashed conditional connection lines; one bold-bordered active doc.
- [P] flat vector, Okabe-Ito: index rectangle Blue #0072B2, inactive domain docs Sky Blue #56B4E9, active domain doc Orange #E69F00 bold border, dashed connection lines neutral gray. No baked text.
- [E] exclude: file-path labels on rectangles, Markdown content suggestions inside docs, a fourth domain doc.

**NEGATIVE:** text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, 3D perspective

---

## 3. context-window-fill-and-rot  — single growing context window with fill bar crossing rot threshold  (MC · timeline/progression · Important)
*Source: chapter 01 — "Why CLI Agent Prompting Is a Different Discipline"*

**PASTE:** Draw a blank vertical fill-bar diagram on a white background: one tall thin rectangle representing the context window. Inside the rectangle, a fill bar rises from the bottom, shaded, with a horizontal dashed line across the interior at approximately 80% height. Below the dashed line the fill is one color; above the dashed line the fill is a second color (the danger/rot zone). A small upward arrow beside the bar indicates the direction of accumulation. No text, no labels. Uniform strokes, flat fills, no shading.
- [S] single-column 89mm, 300 DPI, vector, white bg, portrait.
- [C] context window (outer rectangle); fill bar rising from bottom; 80% threshold dashed line; below-threshold zone (reliable); above-threshold zone (context rot/danger); upward accumulation arrow.
- [O] tall vertical rectangle; fill bar; threshold line at 80%; two distinct fill regions; accumulation arrow on left.
- [P] flat vector, Okabe-Ito: outer rectangle neutral gray, below-threshold fill Bluish Green #009E73, above-threshold fill Vermillion #D55E00, threshold dashed line Blue #0072B2, accumulation arrow Black #000000. No baked text.
- [E] exclude: turn-number tick marks on the bar, specific content type annotations, a comparison second window.

**NEGATIVE:** text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, 3D perspective

---

## 4. three-tier-manifest-access-model  — canonical/task-triggered/ignored file access tiers for agent context  (VG · hierarchy/taxonomy · Important)
*Source: chapter 03 — "Persistent Instruction Files: CLAUDE.md and AGENTS.md"*

**PASTE:** Draw a blank three-tier horizontal stack on a white background: three equal-height wide rectangles stacked from top to bottom. The top rectangle has a bold solid border. The middle rectangle has a normal solid border. The bottom rectangle has a dashed border. An upward arrow on the right side of the stack. Uniform strokes, flat fills, no shading, no text.
- [S] single-column 89mm, 300 DPI, vector, white bg, portrait.
- [C] three access tiers from top to bottom: Tier 1 Canonical (always read — bold border), Tier 2 Task-triggered (read on demand — normal border), Tier 3 Ignored (not loaded unless explicitly requested — dashed border); upward arrow encodes priority/load-frequency direction.
- [O] vertical three-tier stack; top boldest; bottom dashed; upward priority arrow on right.
- [P] flat vector, Okabe-Ito: Tier 1 Blue #0072B2 bold, Tier 2 Sky Blue #56B4E9, Tier 3 neutral gray dashed, upward arrow Black #000000. No baked text.
- [E] exclude: specific file names inside tiers, token-count estimates beside tiers, a fourth tier.

**NEGATIVE:** text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, 3D perspective

---

## Video candidates

FIGURE static-vs-dynamic-context-partition — Status: STATIC SUFFICIENT · Criterion: — · Reason: the figure is a simultaneous comparison of two or more states; motion would replace side-by-side display with a sequence that the chapter does not assert.
FIGURE progressive-disclosure-index-docs — Status: STATIC SUFFICIENT · Criterion: — · Reason: the mechanism is fully carried by arrow direction and shape arrangement in one frame; motion would not add information a careful static figure does not already hold.
FIGURE context-window-fill-and-rot — Status: STATIC SUFFICIENT · Criterion: — · Reason: the concept is a classification or taxonomy with no temporal component; animation would impose a false sequence.
FIGURE three-tier-manifest-access-model — Status: STATIC SUFFICIENT · Criterion: — · Reason: the concept is a classification or taxonomy with no temporal component; animation would impose a false sequence.

**Chapter recommendation:** None — no entry in this file clears the motion bar; static figures serve every concept here.
