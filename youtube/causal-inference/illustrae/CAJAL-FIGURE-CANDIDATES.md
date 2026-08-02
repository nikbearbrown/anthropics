# CAJAL figure candidates — Causal-Inference (previz track)

DAG topology, backdoor/frontdoor path schematics, do-calculus mechanism diagrams, and structural
comparison panels mined from chapters. Blank unannotated vector — no baked text; previz owns every
symbol. Okabe-Ito, white bg, 1pt strokes, no red-green, no 3D perspective, ≤6–8 components.

Zero-candidate chapters: 00-frontmatter, 00-preface-and-toc, 09-how-to-read-a-case-study, 99-back-matter.

---

## 1. chain-fork-collider-triad  — the three elementary DAG structures side by side  (MC · comparison panels · Critical)
*Source: Chapter 2 — "The Language of Causal Diagrams"*

**PASTE:** Draw a blank three-panel comparison on a white background: three small directed-acyclic-graph schematics arranged left to right, each with three nodes and two or three arrows. Left panel: a chain — three circles arranged horizontally with arrows pointing left to right. Middle panel: a fork — one circle at top with two arrows pointing down-left and down-right to two circles. Right panel: a collider — two circles at left and right with arrows pointing inward toward a central circle. Uniform circles, flat fills, no shading, no labels — no text or numbers.
- [S] single-column 89mm, 300 DPI, vector, white bg, landscape.
- [C] chain (A→B→C); fork (B←A→C); collider (A→B←C); each as an independent 3-node panel.
- [O] three panels left-to-right; → arrows throughout; collider arrows pointing inward are the contrast.
- [P] flat vector, Okabe-Ito: chain nodes Blue #0072B2, fork nodes Orange #E69F00, collider nodes Bluish Green #009E73, all arrows Black #000000. No baked text.
- [E] exclude: d-separation notation, path labels, correlation symbols, conditioning boxes, panel borders.

**NEGATIVE:** text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, 3D perspective

---

## 2. smoking-cancer-dag  — genotype confounds smoking and cancer via two routes  (VG · systems diagram · Critical)
*Source: Chapter 2 — "The Language of Causal Diagrams"*

**PASTE:** Draw a blank four-node directed acyclic graph on a white background: four circles arranged so one (top-left) has arrows pointing to a second (left) and to a fourth (right); the second has an arrow to a third (middle); the third has an arrow to the fourth. Two separate arrow routes from the top-left node to the fourth node — one through the middle two nodes, one direct. Uniform circles, uniform 1pt stroke arrows, flat fills, no shading, no labels — no text.
- [S] single-column 89mm, 300 DPI, vector, white bg, square.
- [C] four nodes: genotype (G, upstream), smoking (S), tar (T, mediator), cancer (C, outcome); G→S, S→T, T→C, G→C direct.
- [O] G top-left; S below-left; T center; C right; two converging paths from G to C are the visual argument.
- [P] flat vector, Okabe-Ito: G node Reddish Purple #CC79A7, S node Orange #E69F00, T node Sky Blue #56B4E9, C node Blue #0072B2, arrows Black #000000. No baked text.
- [E] exclude: probability annotations, regression coefficients, effect-size brackets, node counts.

**NEGATIVE:** text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, 3D perspective

---

## 3. backdoor-path-blocking  — how conditioning on a fork node blocks the back-door  (MC · mechanism cross-section · Critical)
*Source: Chapter 3 — "Confounding and Adjustment"*

**PASTE:** Draw a blank three-panel mechanism schematic on a white background: two side-by-side DAG panels of the same three-node fork structure. Left panel: X on the left, Z above-center, Y on the right — arrows Z→X and Z→Y and X→Y; a dashed curved band connects X to Y via Z to show the open back-door path. Right panel: same layout, but Z is enclosed in a small square (indicating conditioning); the dashed back-door band is crossed out or absent. Uniform circles, 1pt strokes, flat fills, no labels — no text.
- [S] single-column 89mm, 300 DPI, vector, white bg, landscape two-panel.
- [C] fork Z→X, Z→Y before and after conditioning on Z; back-door path X←Z→Y open vs. blocked; causal arrow X→Y unchanged.
- [O] left panel = open fork; right panel = conditioned (Z boxed); → arrow between panels showing transformation.
- [P] flat vector, Okabe-Ito: Z node Orange #E69F00, X node Blue #0072B2, Y node Bluish Green #009E73, back-door path Vermillion #D55E00 dashed, causal path Black #000000, conditioning box light gray outline. No baked text.
- [E] exclude: collider structures, mediator paths, do-operator notation, specific variable names.

**NEGATIVE:** text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, 3D perspective

---

## 4. collider-opens-path  — conditioning on a collider creates association  (MC · comparison panels · Critical)
*Source: Chapter 2 — "The Language of Causal Diagrams"*

**PASTE:** Draw a blank two-panel comparison on a white background showing collider conditioning. Left panel: three circles — A on left, B in center, C on right — arrows from A into B and from C into B (collider at B); A and C are shown as disconnected (no path between them — indicate with a blank gap or absent connection). Right panel: same layout, B enclosed in a square (conditioned); a new dashed curved band now connects A and C, representing the induced association. Uniform circles, 1pt strokes, flat fills, no labels — no text.
- [S] single-column 89mm, 300 DPI, vector, white bg, landscape two-panel.
- [C] collider B receives arrows from A and C; marginal independence between A and C; conditioning on B induces a spurious correlation between A and C.
- [O] left = no conditioning, no A–C connection; right = B conditioned (boxed), dashed A–C path appears.
- [P] flat vector, Okabe-Ito: A node Blue #0072B2, B node Orange #E69F00, C node Bluish Green #009E73, induced-association path Vermillion #D55E00 dashed, conditioning box light gray. No baked text.
- [E] exclude: Berkson's paradox specific context, disease names, hospital scenario, fork or chain structures.

**NEGATIVE:** text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, 3D perspective

---

## 5. rct-arrow-deletion  — randomization surgically deletes all incoming arrows on T  (MC · comparison panels · Critical)
*Source: Chapter 4 — "Randomization and Its Limits"*

**PASTE:** Draw a blank two-panel DAG comparison on a white background. Left panel (observational): treatment node T in center-left, outcome node Y at right, a cloud-shape of four small nodes above T each with arrows into T and into Y (confounding cloud). Right panel (RCT): same T and Y nodes, same cloud, but all arrows from cloud nodes into T are absent — crossed or erased; only the arrows from cloud nodes into Y remain; a coin or dice symbol indicates the random assignment of T. Uniform nodes, 1pt strokes, flat fills, no labels — no text.
- [S] single-column 89mm, 300 DPI, vector, white bg, landscape.
- [C] observational: multiple confounders cause T; RCT: random assignment severs all causal arrows into T while leaving confounder-to-outcome arrows intact.
- [O] left = observational; right = post-randomization; crossed arrows on right indicate deletion not absence from the start.
- [P] flat vector, Okabe-Ito: T node Blue #0072B2, Y node Bluish Green #009E73, confounder cloud nodes Orange #E69F00, deleted arrows Vermillion #D55E00 with X marks, surviving arrows Black #000000, random symbol Sky Blue #56B4E9. No baked text.
- [E] exclude: specific confounder names, p-values, sample sizes, CONSORT flow.

**NEGATIVE:** text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, 3D perspective

---

## 6. ladder-of-causation  — three rungs: association, intervention, counterfactual  (VG · hierarchy · Critical)
*Source: Chapters 1, 8 — "Why Causal Inference?", "Counterfactuals and Mediation"*

**PASTE:** Draw a blank three-rung ladder schematic on a white background: a vertical ladder with three horizontal rungs labeled by position from bottom to top; at each rung level, one small icon or abstract shape suggests the rung's type — bottom rung: two overlapping circles (association/correlation); middle rung: a hand touching a node (intervention/do); top rung: two branching paths from one node (counterfactual/what-if). No text, no numbers, only geometric shapes. Uniform strokes, flat fills, no shading.
- [S] single-column 89mm, 300 DPI, vector, white bg, portrait.
- [C] three rungs bottom-to-top: association (observation), intervention (do-operator), counterfactual (individual-level what-if); ascending complexity and evidence requirement.
- [O] vertical ladder; bottom = weakest epistemic claim, top = strongest; icons beside each rung distinguish them.
- [P] flat vector, Okabe-Ito: rung 1 Orange #E69F00, rung 2 Sky Blue #56B4E9, rung 3 Blue #0072B2, ladder rails Black #000000. No baked text.
- [E] exclude: probability notation, specific equations, Pearl's name, historical vignettes.

**NEGATIVE:** text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, 3D perspective

---

## 7. mediation-total-vs-direct  — decomposing total effect into direct and indirect paths  (MC · systems diagram · Important)
*Source: Chapter 8 — "Counterfactuals and Mediation"*

**PASTE:** Draw a blank three-node DAG on a white background with two distinct arrow routes between the leftmost and rightmost nodes: one direct arrow from the left node to the right node; one indirect route from the left node through a middle node (positioned above or below the direct arrow) to the right node. Both routes terminate at the same right node. The direct arrow and the two indirect arrows should be visually distinguishable by style (solid vs. dashed) or color. Uniform circles, 1pt strokes, flat fills, no labels — no text.
- [S] single-column 89mm, 300 DPI, vector, white bg, landscape.
- [C] three nodes: treatment T (left), mediator M (middle), outcome Y (right); T→Y direct arrow; T→M→Y indirect path; the two routes show the total effect decomposition.
- [O] T left, M above-center, Y right; direct path bottom, indirect path top; both paths converging on Y.
- [P] flat vector, Okabe-Ito: T node Blue #0072B2, M node Orange #E69F00, Y node Bluish Green #009E73, direct arrow Black #000000 solid, indirect arrows Reddish Purple #CC79A7 dashed. No baked text.
- [E] exclude: coefficients, effect-size numerals, natural-direct/indirect-effect notation, structural equations.

**NEGATIVE:** text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, 3D perspective

---

## 8. sensitivity-swiss-cheese  — confounding robustness as a stack of barrier slices with holes  (VG · process flowchart · Important)
*Source: Chapter 11 — "Sensitivity Analysis"*

**PASTE:** Draw a blank Swiss-cheese barrier diagram on a white background: a horizontal sequence of three vertical oval or rectangular slices, each with one or two irregular oval holes punched through it; a dashed horizontal arrow (representing a confounding path or finding) passes straight through each slice by threading through the holes; the final slice stops the arrow cleanly (or the arrow exits at the right edge to indicate that aligned holes mean the finding passes through). Uniform strokes, flat fills, no labels — no text.
- [S] single-column 89mm, 300 DPI, vector, white bg, landscape.
- [C] three defense slices (propensity matching, E-value threshold, domain plausibility); holes in each slice; alignment of holes allows a confounded finding to "pass through"; non-alignment stops it.
- [O] left-to-right flow; three slices; trajectory arrow passes through all three when holes align.
- [P] flat vector, Okabe-Ito: slices Blue #0072B2 with light-gray holes, trajectory arrow Vermillion #D55E00, successfully-blocked slice Bluish Green #009E73 outline. No baked text.
- [E] exclude: E-value formula, Rosenbaum-Γ notation, specific disease contexts, numerical thresholds.

**NEGATIVE:** text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, 3D perspective

---

## Video candidates

FIGURE chain-fork-collider-triad — Status: STATIC SUFFICIENT · Criterion: — · Reason: the figure is a simultaneous comparison of two or more states; motion would replace side-by-side display with a sequence that the chapter does not assert.
FIGURE smoking-cancer-dag — Status: STATIC SUFFICIENT · Criterion: — · Reason: the mechanism is fully carried by arrow direction and shape arrangement in one frame; motion would not add information a careful static figure does not already hold.
FIGURE backdoor-path-blocking — Status: STATIC SUFFICIENT · Criterion: — · Reason: the mechanism is fully carried by arrow direction and shape arrangement in one frame; motion would not add information a careful static figure does not already hold.
FIGURE collider-opens-path — Status: STATIC SUFFICIENT · Criterion: — · Reason: the figure is a simultaneous comparison of two or more states; motion would replace side-by-side display with a sequence that the chapter does not assert.
FIGURE rct-arrow-deletion — Status: STATIC SUFFICIENT · Criterion: — · Reason: the figure is a simultaneous comparison of two or more states; motion would replace side-by-side display with a sequence that the chapter does not assert.
FIGURE ladder-of-causation — Status: STATIC SUFFICIENT · Criterion: — · Reason: the mechanism is fully carried by arrow direction and shape arrangement in one frame; motion would not add information a careful static figure does not already hold.
FIGURE mediation-total-vs-direct — Status: STATIC SUFFICIENT · Criterion: — · Reason: the mechanism is fully carried by arrow direction and shape arrangement in one frame; motion would not add information a careful static figure does not already hold.
FIGURE sensitivity-swiss-cheese — Status: STATIC SUFFICIENT · Criterion: — · Reason: the concept is a classification or taxonomy with no temporal component; animation would impose a false sequence.

**Chapter recommendation:** None — no entry in this file clears the motion bar; static figures serve every concept here.
