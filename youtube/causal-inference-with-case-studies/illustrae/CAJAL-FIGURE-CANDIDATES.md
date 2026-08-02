# CAJAL figure candidates — causal-inference-with-case-studies (previz track)

Structural DAG candidates with case-study grounding. Near-identical chapter structure to
Causal-Inference main book but with applied case-study framing in chapters 15–25. Core
identification-theory chapters (01–14) carry the same high CAJAL density; case chapters
(15–25) add applied DAG instances. Blank unannotated vector, Okabe-Ito, white bg, ≤6–8 components.

Zero-candidate chapters: 00-frontmatter, 00-preface-and-toc, 09-how-to-read-a-case-study, 99-back-matter.

---

## 1. chain-fork-collider-triad  — the three elementary DAG structures side by side  (MC · comparison panels · Critical)
*Source: Chapter 2 — "The Language of Causal Diagrams"*

**PASTE:** Draw a blank three-panel comparison on a white background: three small directed-acyclic-graph schematics arranged left to right. Left: chain — three circles horizontal with arrows pointing left-to-right. Middle: fork — one circle at top, arrows pointing down to two separate circles below. Right: collider — two circles on left and right with arrows pointing inward to a center circle. Uniform circles, 1pt stroke arrows, flat fills, no labels — no text.
- [S] single-column 89mm, 300 DPI, vector, white bg, landscape.
- [C] chain A→B→C; fork B←A→C; collider A→B←C; three panels one structure each.
- [O] three panels left-to-right; arrows consistent in direction semantics.
- [P] flat vector, Okabe-Ito: chain nodes Blue #0072B2, fork nodes Orange #E69F00, collider nodes Bluish Green #009E73, arrows Black #000000. No baked text.
- [E] exclude: d-separation notation, variable names, correlation symbols, conditioning boxes.

**NEGATIVE:** text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, 3D perspective

---

## 2. confounder-vs-mediator  — same data, two DAG interpretations, opposite adjustment decisions  (MC · comparison panels · Critical)
*Source: Chapter 3 — "Confounding and Adjustment"*

**PASTE:** Draw a blank two-panel DAG comparison on a white background. Left panel: three nodes arranged as a fork — top node with arrows pointing down-left to X and down-right to Y, plus a direct X→Y arrow; the fork node is highlighted as the structural confounder. Right panel: same three nodes but the third node sits between X and Y on the causal path — X→Z→Y only, no fork; the middle node is highlighted as a mediator. Each panel has a small symbol below it to differentiate (e.g., a square for confounder, a circle for mediator). No labels — no text.
- [S] single-column 89mm, 300 DPI, vector, white bg, landscape two-panel.
- [C] left: G→X, G→Y, X→Y (G is confounder); right: X→Z→Y (Z is mediator); same variable count, opposite structural roles.
- [O] two equal-width panels; identical node count; structural difference in arrow pattern is the sole visual argument.
- [P] flat vector, Okabe-Ito: X node Blue #0072B2, Y node Bluish Green #009E73, confounder node Vermillion #D55E00, mediator node Orange #E69F00, arrows Black #000000. No baked text.
- [E] exclude: Simpson's paradox table, regression output, specific clinical variables, M-bias structure.

**NEGATIVE:** text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, 3D perspective

---

## 3. backdoor-criterion-path-trace  — tracing back-door paths and finding the valid adjustment set  (MC · process flowchart · Critical)
*Source: Chapter 3 — "Confounding and Adjustment"*

**PASTE:** Draw a blank five-node DAG on a white background with paths visually distinguished: four circles positioned roughly at corners of a diamond plus one at top; arrows connecting them to create one direct causal path (top→right) and two back-door paths (top←left→right and top←bottom→right); back-door paths shown in a contrasting color. One intermediate node on the back-door path is enclosed in a small square to indicate it is the chosen adjustment variable that blocks both back-door paths. No labels — no text.
- [S] single-column 89mm, 300 DPI, vector, white bg, square.
- [C] five nodes: T (treatment), Y (outcome), two confounders on separate back-door paths, one adjustment node that blocks both; back-door paths vs. causal path visually separated.
- [O] T center-left, Y center-right, confounders above and below; causal arrow direct, back-door paths arcing; adjustment node boxed.
- [P] flat vector, Okabe-Ito: T node Blue #0072B2, Y node Bluish Green #009E73, confounder nodes Orange #E69F00, adjustment node Reddish Purple #CC79A7 with box outline, causal path Black #000000, back-door paths Vermillion #D55E00 dashed. No baked text.
- [E] exclude: d-separation algebra, specific case-study variables, do-operator, frontdoor structure.

**NEGATIVE:** text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, 3D perspective

---

## 4. propensity-score-weighting  — IPW as a reweighting of the sample to remove confounding  (MC · comparison panels · Important)
*Source: Chapter 6 — "Weighting Methods"*

**PASTE:** Draw a blank two-panel comparison on a white background showing sample reweighting. Left panel: two rows of dots (one row larger dots, one row smaller dots) representing an imbalanced sample where one group is overrepresented; the dots are arranged informally, sizes unequal. Right panel: same rows, but all dots are now the same visual size, with faint rings around the underrepresented-group dots showing upward weighting; the rows now appear balanced. No labels — no text or numbers.
- [S] single-column 89mm, 300 DPI, vector, white bg, landscape two-panel.
- [C] unweighted sample with group imbalance; IPW-reweighted sample restoring balance; weight magnitude shown by dot ring size.
- [O] left = imbalanced, right = balanced; visual point mass change is the argument.
- [P] flat vector, Okabe-Ito: group 1 dots Blue #0072B2, group 2 dots Orange #E69F00, weight rings Bluish Green #009E73, balanced frame light gray background. No baked text.
- [E] exclude: Horvitz-Thompson formula, propensity score formula, overlap trimming steps, regression adjustment.

**NEGATIVE:** text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, 3D perspective

---

## 5. counterfactual-abduction-action-prediction  — the three-step SCM counterfactual procedure  (MC · process flowchart · Important)
*Source: Chapter 8 — "Counterfactuals and Mediation"*

**PASTE:** Draw a blank three-stage horizontal process flowchart on a white background: three equally sized rectangles arranged left-to-right with arrows between them, each containing only a distinct abstract shape (not text) to distinguish the step — step 1: an eye or lens shape (observation/abduction); step 2: a hand or gear (action/intervention); step 3: a branching arrow (prediction/counterfactual outcome). Below each rectangle, no text — only the abstract shape. Arrow connectors between boxes. Uniform strokes, flat fills, no labels.
- [S] single-column 89mm, 300 DPI, vector, white bg, landscape.
- [C] three steps: abduction (infer noise values from observed data), action (modify SCM for counterfactual X), prediction (compute Y under modified model with inferred noise).
- [O] left-to-right sequential; → between steps; each box has a geometric icon only.
- [P] flat vector, Okabe-Ito: step 1 box Sky Blue #56B4E9, step 2 box Orange #E69F00, step 3 box Bluish Green #009E73, arrows Black #000000. No baked text.
- [E] exclude: structural equations, specific U_M / U_Y notation, individual case values, mathematical coefficients.

**NEGATIVE:** text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, 3D perspective

---

## 6. feedback-loop-dag  — a testing-to-cases feedback loop as a DAG showing self-reinforcing bias  (MC · systems diagram · Important)
*Source: Chapter 14 — "Causal Agents"*

**PASTE:** Draw a blank three-node directed cycle on a white background — not an acyclic graph, but a cycle deliberately illustrating a feedback loop: three circles arranged in a triangle with arrows forming a loop (A→B→C→A or a longer chain closing on itself); one node has a double-outlined circle to indicate it is the entry point where a decision is made that reinforces itself. Uniform strokes, flat fills, no shading, no labels — no text.
- [S] single-column 89mm, 300 DPI, vector, white bg, square.
- [C] three nodes in a cycle: prior rate (input), algorithmic recommendation (decision), observed cases (output that feeds back into the prior); self-reinforcing loop structure.
- [O] triangle arrangement; arrows travel clockwise; one entry node double-outlined; loop closure arrow slightly curved.
- [P] flat vector, Okabe-Ito: entry/decision node Blue #0072B2, downstream node Orange #E69F00, feedback node Vermillion #D55E00, loop arrows Vermillion #D55E00, one causal arrow Black #000000. No baked text.
- [E] exclude: COVID-specific labels, geographic maps, FERC notation, testing-rate numbers.

**NEGATIVE:** text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, 3D perspective

---

## Video candidates

FIGURE chain-fork-collider-triad — Status: STATIC SUFFICIENT · Criterion: — · Reason: the figure is a simultaneous comparison of two or more states; motion would replace side-by-side display with a sequence that the chapter does not assert.
FIGURE confounder-vs-mediator — Status: STATIC SUFFICIENT · Criterion: — · Reason: the figure is a simultaneous comparison of two or more states; motion would replace side-by-side display with a sequence that the chapter does not assert.
FIGURE backdoor-criterion-path-trace — Status: STATIC SUFFICIENT · Criterion: — · Reason: the concept is a classification or taxonomy with no temporal component; animation would impose a false sequence.
FIGURE propensity-score-weighting — Status: STATIC SUFFICIENT · Criterion: — · Reason: the figure is a simultaneous comparison of two or more states; motion would replace side-by-side display with a sequence that the chapter does not assert.
FIGURE counterfactual-abduction-action-prediction — Status: STATIC SUFFICIENT · Criterion: — · Reason: the concept is a classification or taxonomy with no temporal component; animation would impose a false sequence.
FIGURE feedback-loop-dag — Status: VIDEO CANDIDATE · Criterion: 3 · Reason: a closed cycle in which the return to start is conceptually load-bearing — each iteration changes the conditions for the next, a relationship that a static loop diagram cannot express.

**Chapter recommendation:** **feedback-loop-dag** — the sole video candidate; a closed cycle in which the return to start is conceptually load-bearing — each iteration changes the conditions for the next, a relationship that a static loop diagram cannot express.
