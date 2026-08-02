# CAJAL figure candidates — claude-code-for-teachers (previz track)

Mechanism and workflow figures mined from chapter text. Blank unannotated vector — no baked text.
Okabe-Ito, white bg, 1pt strokes, no red-green, no 3D perspective, ≤6–8 components.

---

## 1. hooks-enforcement-hierarchy  — advisory-to-deterministic enforcement stack for classroom tool control  (VG · hierarchy/taxonomy · Critical)
*Source: chapter 08 — "Hooks"*

**PASTE:** Draw a blank three-tier vertical stack on a white background: three wide horizontal rectangles stacked bottom to top, the bottom widest, the top narrowest. The top rectangle has a bold solid border; the middle rectangle has a normal solid border; the bottom rectangle has a thin dashed border. A small upward arrow beside the left edge of the stack. Uniform strokes, flat fills, no shading, no labels — no text.
- [S] single-column 89mm, 300 DPI, vector, white bg, portrait.
- [C] three tiers from bottom to top: CLAUDE.md advisory instructions (dashed border, widest); PreToolUse/PostToolUse hooks (normal border, medium); deterministic enforcement (bold border, narrowest); upward arrow marks enforcement-strength direction.
- [O] vertical tapered stack; border weight encodes enforcement strength; upward arrow on left.
- [P] flat vector, Okabe-Ito: bottom tier Sky Blue #56B4E9 dashed, middle tier Orange #E69F00, top tier Blue #0072B2 bold, arrow Black #000000. No baked text.
- [E] exclude: script syntax inside tiers, settings.json path labels, a fourth tier, per-event type breakdown.

**NEGATIVE:** text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, 3D perspective

---

## 2. explore-plan-implement-commit-loop  — four-phase Claude Code workflow for specification-driven builds  (MC · process flowchart · Critical)
*Source: chapter 04 — "Prompts to Specifications"*

**PASTE:** Draw a blank four-stage horizontal pipeline on a white background: four rectangles connected left-to-right by single-headed arrows. The third rectangle (Implement) has a small vertical double-line gate mark on its left edge, indicating the plan-approval gate before implementation begins. A curved back-arrow runs from the fourth box back to the first, indicating the iterative nature of the loop. No text, no labels. Uniform strokes, flat fills, no shading.
- [S] single-column 89mm, 300 DPI, vector, white bg, landscape.
- [C] four phases: Explore (read files), Plan (propose steps in plan-mode), Implement (execute with gate), Commit (verify and save); gate marker before Implement; back-arrow from Commit to Explore for next iteration.
- [O] left-to-right pipeline; gate mark before phase three; curved back-arc below pipeline returning to phase one.
- [P] flat vector, Okabe-Ito: Explore and Commit boxes Sky Blue #56B4E9, Plan box Orange #E69F00, Implement box Bluish Green #009E73, gate mark Blue #0072B2, arrows Black #000000. No baked text.
- [E] exclude: specific code content inside boxes, branch paths for failure, user-prompt text annotations.

**NEGATIVE:** text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, 3D perspective

---

## 3. skills-vs-hooks-boundary  — CLAUDE.md / Skill / Hook responsibility partition model  (VG · systems diagram · Important)
*Source: chapters 07 — "Skills" and 08 — "Hooks"*

**PASTE:** Draw a blank three-zone partition diagram on a white background: a wide horizontal rectangle divided into three vertical panels by two thin vertical dividers. The leftmost panel is the widest; the middle panel is medium width; the right panel is the narrowest and has a bold border. A small upward arrow sits at the top of the right panel only. Uniform strokes, flat fills, no shading, no labels — no text.
- [S] single-column 89mm, 300 DPI, vector, white bg, landscape.
- [C] three zones: CLAUDE.md (project-level context, wide, advisory); Skills (task-specific reusable workflows, medium, invoked on demand); Hooks (lifecycle enforcement, narrow bold border, deterministic); upward arrow on hooks zone encodes enforcement strength.
- [O] three-panel horizontal partition; left widest (context scope), right narrowest (enforcement focus); bold border on right panel; upward enforcement arrow.
- [P] flat vector, Okabe-Ito: CLAUDE.md panel Sky Blue #56B4E9, Skills panel Orange #E69F00, Hooks panel Blue #0072B2 bold border, dividers neutral gray. No baked text.
- [E] exclude: YAML frontmatter fields shown in skills panel, specific hook-event types in right panel, a fourth zone.

**NEGATIVE:** text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, 3D perspective

---

## Video candidates

FIGURE hooks-enforcement-hierarchy — Status: STATIC SUFFICIENT · Criterion: — · Reason: the concept is a classification or taxonomy with no temporal component; animation would impose a false sequence.
FIGURE explore-plan-implement-commit-loop — Status: STATIC SUFFICIENT · Criterion: — · Reason: the concept is a classification or taxonomy with no temporal component; animation would impose a false sequence.
FIGURE skills-vs-hooks-boundary — Status: STATIC SUFFICIENT · Criterion: — · Reason: the mechanism is fully carried by arrow direction and shape arrangement in one frame; motion would not add information a careful static figure does not already hold.

**Chapter recommendation:** None — no entry in this file clears the motion bar; static figures serve every concept here.
