# CAJAL figure candidates — causal-reasoning (previz track)

DAG topology and structural reasoning candidates from a course-oriented causal-reasoning book
with chapter-by-chapter structural concepts. High density: every identification chapter
(03–13) yields one or more CAJAL candidates. Okabe-Ito, white bg, ≤6–8 components, no baked text.

Zero-candidate chapters: 00-frontmatter, 00-introduction, 01-the-decision-that-looked-right,
02-three-words-for-the-same-problem, 15-the-full-analysis, 99-back-matter.

---

## 1. dag-three-representations  — DAG, probability factorization, and prose as three windows on one object  (VG · conceptual map · Important)
*Source: Chapter 3 — "The Map Before the Territory"*

**PASTE:** Draw a blank three-panel layout on a white background: three equal boxes arranged horizontally. Left box contains a small four-node DAG (circles and arrows only). Middle box contains a compact grid or matrix (blank rows and columns, no numbers — just the grid structure). Right box contains four wavy horizontal lines suggesting prose paragraphs (no text). A thin bracket or arc above all three boxes connects them to indicate they are representations of one object. Uniform strokes, flat fills, no labels — no text.
- [S] single-column 89mm, 300 DPI, vector, white bg, landscape.
- [C] three panels: DAG (graph), factorized probability table (structure only), prose statement (lines); one unifying bracket above.
- [O] three equal-width panels left-to-right; bracket unifying them; each panel has a distinct geometric vocabulary.
- [P] flat vector, Okabe-Ito: DAG panel Sky Blue #56B4E9, table panel Orange #E69F00, prose panel Bluish Green #009E73, unifying bracket Black #000000. No baked text.
- [E] exclude: specific equation, C/T/M/Y node identities, Python code, structural equation notation.

**NEGATIVE:** text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, 3D perspective

---

## 2. confounder-structural-position  — confounder as common cause on an open backdoor path  (VG · systems diagram · Critical)
*Source: Chapter 5 — "Confounders: The Variable You Forgot"*

**PASTE:** Draw a blank three-node fork DAG on a white background: U at top-center with arrows pointing down-left to X and down-right to Y; a direct arrow from X to Y at the bottom; a dashed curved arc from X to Y running above the direct arrow, overlapping with both U→X and U→Y to show the open back-door path. U is slightly larger to signal its structural importance. No labels — no text.
- [S] single-column 89mm, 300 DPI, vector, white bg, square.
- [C] U (unmeasured common cause), X (treatment), Y (outcome); U→X and U→Y create back-door path X←U→Y; X→Y is the causal path; back-door arc shown as open and spurious.
- [O] U centered at top; X lower-left; Y lower-right; causal arrow direct at bottom; back-door arc above and dashed.
- [P] flat vector, Okabe-Ito: U node Vermillion #D55E00 (unmeasured), X node Blue #0072B2, Y node Bluish Green #009E73, causal arrow Black #000000, back-door arc Vermillion #D55E00 dashed. No baked text.
- [E] exclude: Amazon/Obermeyer specific context, correlation-definition critique, regression coefficients.

**NEGATIVE:** text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, 3D perspective

---

## 3. mediator-forward-path  — mediator sits on the causal path; conditioning removes indirect effect  (MC · comparison panels · Critical)
*Source: Chapter 6 — "Mediators: The Variable You Shouldn't Touch"*

**PASTE:** Draw a blank two-panel DAG on a white background. Left panel: three circles P (left), D (above-center), R (right) — arrows P→D and D→R (indirect path) plus P→R (direct path). Right panel: same three circles, D now enclosed in a small square (conditioned); the P→D→R route is shown as blocked (a cross or break in the path from D to R). The direct P→R arrow remains intact. No labels — no text.
- [S] single-column 89mm, 300 DPI, vector, white bg, landscape two-panel.
- [C] three nodes: policy P, mediator D, outcome R; indirect path P→D→R and direct path P→R; conditioning on D blocks indirect path and underestimates total effect.
- [O] two equal panels; left = unconditioned, right = D conditioned (boxed and path blocked); → connector between panels.
- [P] flat vector, Okabe-Ito: P node Blue #0072B2, D node Orange #E69F00, R node Bluish Green #009E73, direct arrow Black #000000, indirect path Reddish Purple #CC79A7, block symbol Vermillion #D55E00. No baked text.
- [E] exclude: streaming-platform context, SDT motivation framing, specific retention numbers.

**NEGATIVE:** text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, 3D perspective

---

## 4. collider-hire-puzzle  — conditioning on the hired set induces a spurious correlation  (MC · comparison panels · Critical)
*Source: Chapter 7 — "Colliders: The Variable That Breaks Everything (Part 1)"*

**PASTE:** Draw a blank two-panel collider diagram on a white background. Left panel: three circles T (left), H (center), C (right); arrows from T into H and from C into H (two causes, one collider); T and C are not connected — an absent line or empty gap between them signals independence. Right panel: H enclosed in a small square; a new dashed arc now connects T and C, showing the induced association. No labels — no text.
- [S] single-column 89mm, 300 DPI, vector, white bg, landscape two-panel.
- [C] T (technical skill) and C (communication skill) independent in general population; H (hired) is their collider; conditioning on H creates a spurious negative association between T and C.
- [O] left = unconditioned, T–C independent; right = H conditioned (boxed), T–C dashed arc appears.
- [P] flat vector, Okabe-Ito: T node Blue #0072B2, C node Bluish Green #009E73, H node Orange #E69F00, induced arc Vermillion #D55E00 dashed, H conditioning box light gray. No baked text.
- [E] exclude: score correlation numbers, Berkson's paradox disease context, three-variable mediator.

**NEGATIVE:** text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, 3D perspective

---

## 5. backdoor-criterion-enumeration  — tracing all back-door paths from T to Y and finding a block  (MC · process flowchart · Critical)
*Source: Chapters 9–10 — "The Backdoor Criterion (Parts 1 & 2)"*

**PASTE:** Draw a blank five-node DAG on a white background: T (left), Y (right), and three intermediate nodes arranged above and below a center line — two nodes above forming a fork into T and Y, one node below connecting through T. The causal path T→Y is direct. Back-door paths trace through the upper nodes — highlight them with one color. The adjustment set node (one of the upper nodes) is enclosed in a small square to show it blocks both back-door paths. No labels — no text.
- [S] single-column 89mm, 300 DPI, vector, white bg, landscape.
- [C] T and Y with three potential confounders; two open back-door paths; one adjustment variable blocks both; clause (b) is represented by no arrow from T into the adjustment node.
- [O] T left, Y right, confounders arranged above; back-door arcs highlighted; adjustment node boxed.
- [P] flat vector, Okabe-Ito: T Blue #0072B2, Y Bluish Green #009E73, confounders Orange #E69F00, adjustment node Reddish Purple #CC79A7, back-door paths Vermillion #D55E00 dashed, causal path Black #000000. No baked text.
- [E] exclude: second condition (descendants), instrumental variable structure, specific domain variables.

**NEGATIVE:** text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, 3D perspective

---

## 6. pearl-ladder-three-rungs  — association / intervention / counterfactual as a vertical progression  (VG · hierarchy · Important)
*Source: Chapter 3 — "The Map Before the Territory"; referenced across multiple chapters*

**PASTE:** Draw a blank three-rung ladder schematic on a white background: a vertical ladder with three horizontal rungs, each at a distinct height; beside each rung a small abstract icon only — bottom rung: two overlapping ovals (observation/association); middle rung: a pointed hand or directional arrow icon (intervention); top rung: a forked path or two parallel lines diverging (counterfactual). No text, no numbers. Uniform strokes, flat fills.
- [S] single-column 89mm, 300 DPI, vector, white bg, portrait.
- [C] rung 1 (bottom): observation/association; rung 2 (middle): intervention/do-operator; rung 3 (top): counterfactual/individual reasoning.
- [O] vertical ladder; each rung paired with a distinct geometric icon; ascending complexity from bottom to top.
- [P] flat vector, Okabe-Ito: rung 1 Orange #E69F00, rung 2 Sky Blue #56B4E9, rung 3 Blue #0072B2, ladder rails Black #000000. No baked text.
- [E] exclude: Sewall Wright history, John Snow pump-handle narrative, Pearl's biographical information.

**NEGATIVE:** text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, 3D perspective

---

## Video candidates

FIGURE dag-three-representations — Status: STATIC SUFFICIENT · Criterion: — · Reason: the mechanism is fully carried by arrow direction and shape arrangement in one frame; motion would not add information a careful static figure does not already hold.
FIGURE confounder-structural-position — Status: STATIC SUFFICIENT · Criterion: — · Reason: the mechanism is fully carried by arrow direction and shape arrangement in one frame; motion would not add information a careful static figure does not already hold.
FIGURE mediator-forward-path — Status: STATIC SUFFICIENT · Criterion: — · Reason: the figure is a simultaneous comparison of two or more states; motion would replace side-by-side display with a sequence that the chapter does not assert.
FIGURE collider-hire-puzzle — Status: STATIC SUFFICIENT · Criterion: — · Reason: the figure is a simultaneous comparison of two or more states; motion would replace side-by-side display with a sequence that the chapter does not assert.
FIGURE backdoor-criterion-enumeration — Status: STATIC SUFFICIENT · Criterion: — · Reason: the concept is a classification or taxonomy with no temporal component; animation would impose a false sequence.
FIGURE pearl-ladder-three-rungs — Status: STATIC SUFFICIENT · Criterion: — · Reason: the mechanism is fully carried by arrow direction and shape arrangement in one frame; motion would not add information a careful static figure does not already hold.

**Chapter recommendation:** None — no entry in this file clears the motion bar; static figures serve every concept here.
