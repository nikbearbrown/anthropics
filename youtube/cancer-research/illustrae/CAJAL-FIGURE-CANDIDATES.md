# CAJAL figure candidates — cancer-research (previz track)

Mechanism/structural figures mined from all 11 chapters (B04). Blank unannotated vector, no
baked text, matte Claude palette, cream #F5F1E8 bg, 1pt strokes, no red-green, no 3D, ≤6–8 components.

> Route to the **graphs** skill, NOT previz tiles (they are quantitative/statistical, not
> mechanisms): `ppv-screening-collapse` (PPV vs prevalence curve), `screening-three-biases`
> (lead/length/overdiagnosis — table), `negative-biopsy-posterior` (pre/post-test bar),
> `liquid-biopsy-validity` (3×3 pass/fail grid — could be a table), `kras-vs-egfr-response`
> (two response trajectories — line chart), `lq-survival-curves` (semi-log cell survival —
> quantitative), `bed-grouped-bars` (BED comparison — quantitative), `carboplatin-calvert`
> (linear relationship — quantitative), `per-cycle-vs-cumulative-toxicity` (sawtooth vs step
> rise — quantitative).

---

## 1. staging-molecular-modifiers  — anatomic stage meets molecular modifiers  (VG · convergence tree · Important)
*Source: chapter 03 — "Molecular Diagnostics, Staging, and the Liquid Biopsy"*

**PASTE:** Draw a blank convergence diagram on a cream #F5F1E8 background. On the left, three small separate nodes joined by single-headed arrows merging into one middle node. Into that middle node, from below, two more small nodes feed in via single-headed arrows. All flows continue rightward into one final node. Keep the merges clean, arrows single-headed, strokes uniform, fills flat, no shading, no labels — no text.
- [S] single-column 89mm, 300 DPI, vector, cream #F5F1E8 bg, landscape.
- [C] T, N, M merge → anatomic stage (middle node); molecular modifiers (e.g. receptor status, genomic score) feed in → prognostic stage (final node).
- [O] two-stage convergence, left→right; anatomic inputs from left, molecular modifiers from below; → progression.
- [P] flat vector, matte Claude palette: anatomic inputs rust #C15F3C, molecular modifiers sage #A8C0B4, anatomic-stage node periwinkle #B5B4D6, prognostic-stage node warm-gray #7A7368. Black #000000 outlines. No baked text. Flat matte, low saturation — no gradients, no gloss, no drop-shadows.
- [E] exclude: TNM subcategory letters, biomarker names, score numbers, a treatment arm.

**NEGATIVE:** TNM letters, biomarker names, score numbers, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## 2. surrogate-endpoints  — the endpoint hierarchy that sometimes lies  (VG · hierarchy · Important)
*Source: chapter 04 — "Principles of Cancer Therapy: Goals and Modalities"*

**PASTE:** Draw a blank two-tier hierarchy on a cream #F5F1E8 background: one node at the top, two nodes below it, each connected to the top node by a single-headed arrow. Draw one of the two lower arrows as a solid line and the other as a dashed line to distinguish a valid from a broken link. Keep it symmetric, strokes uniform, fills flat, no shading, no labels — no text.
- [S] single-column 89mm, 300 DPI, vector, cream #F5F1E8 bg.
- [C] top = overall survival (hard endpoint); lower two = PFS and ORR (surrogates); solid link = surrogate translates to OS benefit, dashed link = it does not.
- [O] top-down hierarchy, two children; solid vs dashed encodes validity; → upward-justifying arrows.
- [P] flat vector, matte Claude palette: OS node rust #C15F3C, valid surrogate Bluish Green #009E73 (solid), invalid surrogate Vermillion #D55E00 (dashed). Black #000000 outlines. No baked text. Flat matte, low saturation — no gradients, no gloss, no drop-shadows.
- [E] exclude: drug names, trial names, hazard-ratio numbers, a third tier.

**NEGATIVE:** drug names, trial names, hazard ratios, more than two surrogates, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## 3. combination-chemo-logic  — no two drugs share a toxicity organ  (VG · matrix · Supplementary)
*Source: chapter 10 — "Chemotherapy: Principles and Major Drug Classes"*

**PASTE:** Draw a blank five-row matrix on a cream #F5F1E8 background: five equal horizontal rows, each row a rectangle split into two side-by-side cells by a thin vertical rule (a two-column table with five rows and a blank header strip on top). In the right-hand cell of each row draw a single small distinct organ-token silhouette, and make all five organ tokens different shapes. The left cells stay empty blocks. Uniform strokes, flat fills, no shading, no labels — no text.
- [S] single-column 89mm, 300 DPI, vector, cream #F5F1E8 bg, portrait.
- [C] five drugs (rows); left column = mechanism (blank block); right column = dose-limiting toxicity organ — five distinct organ tokens, none repeated (the design rule made visible).
- [O] 5×2 grid, blank header; distinctness of the organ tokens is the whole point.
- [P] flat vector, matte Claude palette: alternate row tints of Sky Blue #56B4E9 / neutral gray for readability; organ tokens rust #C15F3C. Black #000000 outlines. No baked text. Flat matte, low saturation — no gradients, no gloss, no drop-shadows.
- [E] exclude: drug names, mechanism words, organ labels, a sixth row.

**NEGATIVE:** drug names, organ labels, mechanism text, more than five rows, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## 4. screening-ppv-prevalence  — PPV collapses in low-prevalence populations  (MC · comparison panels · Critical)
*Source: chapter 01 — "Cancer Screening: Finding It Early Enough to Cure"*

**PASTE:** Draw a blank two-panel side-by-side comparison on a cream #F5F1E8 background. Left panel: a large pool of small circles, two circles filled (disease present), one circle highlighted with a ring (true positive) and one circle also highlighted differently (false positive among the many empties) — conveying a low-prevalence scenario where positives are outnumbered by the surrounding empty circles. Right panel: the same layout but with many more filled circles among the pool, and a clearly larger proportion of highlighted circles. Uniform strokes, flat fills, no shading, no labels — no text.
- [S] single-column 89mm, 300 DPI, vector, cream #F5F1E8 bg, landscape.
- [C] left panel = low-prevalence screened population (few diseased, many false positives); right panel = high-prevalence screened population (many diseased, far fewer false positives relative to true positives); the ratio of filled to ring-highlighted circles encodes PPV visually.
- [O] two panels side by side; diseased = filled circles; true positives = filled + ring; false positives = empty + ring; PPV contrast is the teaching point.
- [P] flat vector, matte Claude palette: diseased circles rust #C15F3C, true-positive rings sage #A8C0B4, false-positive rings periwinkle #B5B4D6, non-diseased circles warm-gray #7A7368. Black #000000 outlines. No baked text. Flat matte, low saturation — no gradients, no gloss, no drop-shadows.
- [E] exclude: percentage numbers, formulas, arrows between panels, a third panel.

**NEGATIVE:** numbers, formulas, axis labels, panel titles, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## 5. screening-three-biases  — lead-time, length-time, overdiagnosis as three structural artifacts  (VG · comparison panels · Critical)
*Source: chapter 01 — "Cancer Screening: Finding It Early Enough to Cure"*

**PASTE:** Draw a blank three-row, two-panel comparison on a cream #F5F1E8 background. Three rows, each a horizontal strip. Left column: a stylized forward timeline showing "early detection → long measured survival" for each row — a left arrow pointing right with an early detection marker. Right column: a matching timeline for each row showing the reality — a matching arrow of identical total length but with the outcome unchanged. Row 1: both arrows end at the same right terminus (same death date); the only difference is where the detection marker sits on the left column arrow (early vs late detection). Row 2: the left-column arrow passes through a wider shaded region (slow indolent tumor detected); the right-column arrow passes through a narrow region (fast lethal tumor). Row 3: left-column arrow shows a detection marker that is not followed by a harmful outcome terminus (overdiagnosis — detection without harm). No text, no labels, arrows only.
- [S] single-column 89mm, 300 DPI, vector, cream #F5F1E8 bg, portrait.
- [C] row 1 = lead-time bias (same death date, inflated survival time); row 2 = length-time bias (slow tumors over-detected); row 3 = overdiagnosis (detection with no harmful outcome); three structurally distinct artifacts shown in parallel.
- [O] three rows; two columns; left = "what screening shows," right = "the reality"; horizontal arrows encoding time; detection marker as a small vertical tick.
- [P] flat vector, matte Claude palette: detection marker and left-column elements Orange #E69F00; reality column elements Vermillion #D55E00 to flag artifact; death terminus neutral gray; overdiagnosis row endpoint absent (no terminus) to show no harm. Black #000000 outlines. No baked text. Flat matte, low saturation — no gradients, no gloss, no drop-shadows.
- [E] exclude: survival percentages, timeline tick numbers, a fourth row, connecting arrows between panels.

**NEGATIVE:** percentages, tick labels, survival curves, probability numbers, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## 6. diagnostic-chain  — five-link chain from clinical suspicion to molecular workup  (MC · process flowchart · Critical)
*Source: chapter 02 — "Cancer Diagnosis: Imaging and the Tissue Sample"*

**PASTE:** Draw a blank five-node horizontal process flowchart on a cream #F5F1E8 background: five equal rectangles arranged left to right, connected by four single-headed arrows. Below each arrow, attach a small downward-pointing branch ending in a small diamond node. Uniform strokes, flat fills, no shading, no labels — no text.
- [S] single-column 89mm, 300 DPI, vector, cream #F5F1E8 bg, landscape.
- [C] nodes: clinical suspicion → imaging → biopsy → pathology (privileged ground-truth node) → molecular workup; each arrow's downward branch = the failure mode at that link (false positive/negative; sampling miss; ambiguous tissue; insufficient material).
- [O] left→right, five nodes; pathology node visually distinguished as dominant; four failure branches below arrows pointing downward.
- [P] flat vector, matte Claude palette: clinical suspicion and molecular workup nodes rust #C15F3C, imaging node sage #A8C0B4, biopsy node periwinkle #B5B4D6, pathology node Blue #0072B2 (privileged anchor), failure-mode diamonds warm-gray #7A7368. Black #000000 outlines. No baked text. Flat matte, low saturation — no gradients, no gloss, no drop-shadows.
- [E] exclude: specific failure-mode text words, modality names, imaging device shapes, molecular panel details.

**NEGATIVE:** node labels, failure-mode text, imaging device icons, molecular marker names, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## 7. needle-false-negative  — three biopsy failure modes sharing the same result  (VG · comparison panels · Important)
*Source: chapter 02 — "Cancer Diagnosis: Imaging and the Tissue Sample"*

**PASTE:** Draw a blank three-panel stacked comparison on a cream #F5F1E8 background. Each panel is a cross-section of a tumor mass (an irregular oval blob) with a needle depicted at a different position. Panel 1: needle tip lands clearly outside the tumor blob, in surrounding tissue (miss). Panel 2: needle tip sits inside the tumor blob but in a shaded hollow central zone (necrotic core — unrepresentative region). Panel 3: needle tip sits inside the tumor blob in a solid zone but the needle shaft is very thin, suggesting a tiny core. All three panels show the same orientation. Uniform strokes, flat fills, no shading beyond the tumor-interior zone contrast, no labels — no text.
- [S] single-column 89mm, 300 DPI, vector, cream #F5F1E8 bg, portrait.
- [C] tumor mass (solid fill); surrounding stroma (light gray); necrotic core (hollow interior in panel 2); needle at three positions encoding the three failure modes: miss, unrepresentative zone, insufficient material.
- [O] three stacked panels; needle trajectory from same direction each panel; tumor blob constant shape; the needle endpoint is the only variable.
- [P] flat vector, matte Claude palette: tumor mass rust #C15F3C, stroma warm-gray #7A7368, necrotic core hollow/light gray interior, needle shaft and tip Vermillion #D55E00 (signals failure). Black #000000 outlines. No baked text. Flat matte, low saturation — no gradients, no gloss, no drop-shadows.
- [E] exclude: cell illustrations, arrow labels, diagnostic outcome text, a fourth panel.

**NEGATIVE:** cell diagrams, annotation text, outcome labels, histology details, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## 8. three-validity-hierarchy  — analytic validity, clinical validity, clinical utility as narrowing gates  (MC · process flowchart · Critical)
*Source: chapter 03 — "Molecular Diagnostics, Staging, and the Liquid Biopsy"*

**PASTE:** Draw a blank three-gate funnel on a cream #F5F1E8 background: three rectangular gate-nodes arranged left to right, connected by two arrows, with the connecting channel between them visibly narrowing (the gap between gates tapers inward from left to right). Below each connection add a small downward arrow ending in a small circle to represent tests that fail to clear the gate and drop out. Uniform strokes, flat fills, no shading, no labels — no text.
- [S] single-column 89mm, 300 DPI, vector, cream #F5F1E8 bg, landscape.
- [C] gate 1 = analytic validity (does the assay measure accurately?); gate 2 = clinical validity (does the result correlate with a clinical state?); gate 3 = clinical utility (does acting on the result improve outcomes?); channel narrows at each gate; dropped tests shown below.
- [O] left→right flow; funnel narrows; gate 3 is the dominant hard gate; drop-out branches below each gap.
- [P] flat vector, matte Claude palette: gates 1 and 2 Bluish Green #009E73 (passable), gate 3 Blue #0072B2 (dominant, hardest), drop-out circles rust #C15F3C. Black #000000 outlines. No baked text. Flat matte, low saturation — no gradients, no gloss, no drop-shadows.
- [E] exclude: gate labels, test names, percentages, a fourth gate.

**NEGATIVE:** gate labels, test names, percentages, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## 9. liquid-biopsy-two-sources  — tumor DNA and clonal hematopoiesis both feed the plasma pool  (VG · systems diagram · Important)
*Source: chapter 03 — "Molecular Diagnostics, Staging, and the Liquid Biopsy"*

**PASTE:** Draw a blank two-source convergence schematic on a cream #F5F1E8 background. Two source nodes on the left side (one above, one below), both feeding rightward arrows into one central oval pool node in the middle. From the central pool, one arrow continues rightward to a final output node. The two leftward arrows merge visibly before the pool (converging paths). Uniform strokes, flat fills, no shading, no labels — no text.
- [S] single-column 89mm, 300 DPI, vector, cream #F5F1E8 bg, landscape.
- [C] upper source = tumor fragments (intended signal); lower source = aging white blood cells / clonal hematopoiesis (confounding signal); central pool = plasma cfDNA pool; output = flagged mutation of untraceable origin.
- [O] two sources converge into one pool; one output; the merge is the point — once pooled, the two inputs are indistinguishable.
- [P] flat vector, matte Claude palette: tumor source node Blue #0072B2 (primary/dominant), white-cell source node warm-gray #7A7368, pool node rust #C15F3C, output node Vermillion #D55E00 (signals interpretive hazard). Black #000000 outlines. No baked text. Flat matte, low saturation — no gradients, no gloss, no drop-shadows.
- [E] exclude: gene mutation symbols, DNA illustrations, barcode/sequence icons, a third source.

**NEGATIVE:** gene symbols, DNA helix, barcodes, molecular details, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## 10. treatment-intent-tree  — disease extent and fitness determine the four treatment goals  (VG · hierarchy · Important)
*Source: chapter 04 — "Principles of Cancer Therapy: Goals and Modalities"*

**PASTE:** Draw a blank top-down decision tree on a white background: one root node at the top, two child nodes below (first branch), each child with two further child nodes below (second branch), giving four leaf nodes at the bottom. Connect root to first-level children with downward single-headed arrows; connect first-level children to leaves with downward arrows. Keep the tree symmetric, strokes uniform, fills flat, no shading, no labels — no text.
- [S] single-column 89mm, 300 DPI, vector, white bg, portrait.
- [C] root = patient at presentation; first branch = localized disease (left) vs metastatic disease (right); second branch from localized = fit (left leaf) vs frail (right leaf); from metastatic = fit vs frail; four leaves encode cure, control, palliation, comfort goals.
- [O] top-down; binary branches; four leaves encode distinct treatment goals; goal encoding by fill color only.
- [P] flat vector, Okabe-Ito: root node neutral gray, localized branch Sky Blue #56B4E9, metastatic branch Orange #E69F00, cure leaf Bluish Green #009E73, control leaf Blue #0072B2, palliation leaf Orange #E69F00, comfort leaf neutral gray. No baked text.
- [E] exclude: goal names, patient statistics, endpoint text, a fifth leaf.

**NEGATIVE:** goal names, treatment names, survival statistics, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## 11. predictive-vs-prognostic  — four-quadrant grid separating biomarker types  (VG · comparison panels · Critical)
*Source: chapter 05 — "Precision Oncology: Matching Therapy to Tumor"*

**PASTE:** Draw a blank 2×2 grid on a cream #F5F1E8 background: four equal rectangular cells arranged in two rows and two columns, separated by a thin cross-shaped rule. In each cell, place two small schematic survival curves (one solid line above a dashed line — simple smooth downward arcs). Vary the relationship between the two curves across cells: top-left and top-right cells have curves that are parallel (no gap between them); bottom-left cell has the two curves close together; bottom-right cell has the solid curve clearly riding above the dashed one (a visible gap). Keep all curves smooth arcs with no axis marks, no fills, just lines. No labels — no text.
- [S] single-column 89mm, 300 DPI, vector, cream #F5F1E8 bg.
- [C] 2×2: rows = biomarker positive / biomarker negative; columns = prognostic marker / predictive marker; prognostic column: both rows show parallel curves (outcome separated regardless of treatment); predictive column: biomarker-positive row shows treatment benefit gap (curves diverge), biomarker-negative row shows no gap.
- [O] 2×2 grid; survival curves as visual encoding; the presence or absence of a gap between solid and dashed curves is the teaching point.
- [P] flat vector, matte Claude palette: solid (treated) curves rust #C15F3C, dashed (untreated) curves warm-gray #7A7368, diverging gap in predictive/positive cell Bluish Green #009E73 fill between curves. Black #000000 outlines. No baked text. Flat matte, low saturation — no gradients, no gloss, no drop-shadows.
- [E] exclude: axis labels, survival percentages, time markers, patient counts, a third column.

**NEGATIVE:** axis labels, percentages, patient counts, time ticks, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## 12. basket-umbrella-platform  — three precision-oncology trial architectures  (VG · comparison panels · Important)
*Source: chapter 05 — "Precision Oncology: Matching Therapy to Tumor"*

**PASTE:** Draw a blank three-panel side-by-side comparison on a cream #F5F1E8 background. Panel 1 (basket): three separate small geometric shapes (triangle, circle, pentagon — distinct tumor types) each with an arrow converging inward toward one common central rectangular box. Panel 2 (umbrella): one common rectangular box at the top with three arrows diverging outward to three separate small labeled rectangular arms below. Panel 3 (platform): a horizontal spine line with three short vertical arm segments pointing upward at different points along the spine — the first arm ends in a dot, the second arm ends in a dot, but the third arm is longer and still active. Keep all shapes small, arrows single-headed, fills flat, no shading, no labels — no text.
- [S] single-column 89mm, 300 DPI, vector, cream #F5F1E8 bg, landscape.
- [C] panel 1 = basket (multiple tumor types → one biomarker arm); panel 2 = umbrella (one tumor type → multiple biomarker arms); panel 3 = platform (one continuous infrastructure, arms added/dropped over time).
- [O] three panels in a row; convergent arrows for basket, divergent for umbrella, temporal spine for platform; the direction of flow encodes the trial logic.
- [P] flat vector, matte Claude palette: basket tumor-type shapes rust #C15F3C, Sky sage #A8C0B4, Reddish Purple #CC79A7; common arm/root nodes Blue #0072B2; umbrella arms Bluish Green #009E73; platform spine warm-gray #7A7368, active arm periwinkle #B5B4D6. Black #000000 outlines. No baked text. Flat matte, low saturation — no gradients, no gloss, no drop-shadows.
- [E] exclude: cancer type names, drug names, trial names, patient counts, a fourth panel.

**NEGATIVE:** cancer names, drug names, trial names, patient counts, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## 13. margin-examined-vs-inferred  — what the pathologist examines versus what remains in the patient  (VG · comparison panels · Critical)
*Source: chapter 06 — "Surgical Oncology: Principles of Cancer Surgery"*

**PASTE:** Draw a blank two-panel cross-section comparison on a cream #F5F1E8 background. Left panel: an oval representing the excised surgical specimen with three concentric zones — a small dark inner oval (tumor core), a surrounding ring (margin tissue), and an inked outer boundary (examined surface); the outer boundary is a thick distinct stroke. Right panel: the same outer boundary stroke but only the portion of tissue visible beyond the cut line — a thin half-ring of tissue outside where the specimen was; the interior of the specimen is absent (it has been removed). Add a vertical dashed rule between the panels representing the surgical cut. No labels — no text.
- [S] single-column 89mm, 300 DPI, vector, cream #F5F1E8 bg, landscape.
- [C] left panel = excised specimen: tumor core + margin rim + inked surface (what is directly assessed); right panel = patient tissue immediately adjacent to the cut edge (not examined, only inferred); the cut line separates the two domains.
- [O] two panels flanking a central dashed cut-line; left = examined, right = inferred; the absence of the specimen interior in the right panel makes the inference explicit.
- [P] flat vector, matte Claude palette: tumor core rust #C15F3C, margin rim sage #A8C0B4, inked surface stroke Bluish Green #009E73 (examined, safe signal), patient tissue beyond cut Vermillion #D55E00 (unknown/inferred). Black #000000 outlines. No baked text. Flat matte, low saturation — no gradients, no gloss, no drop-shadows.
- [E] exclude: R0/R1/R2 letter codes, cell-level histology details, labels, a third panel.

**NEGATIVE:** R-code letters, histology details, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## 14. sentinel-node-sampling  — tracer flow to sentinel node with failure branch  (MC · process flowchart · Important)
*Source: chapter 06 — "Surgical Oncology: Principles of Cancer Surgery"*

**PASTE:** Draw a blank process flowchart with a failure branch on a cream #F5F1E8 background. Main track (left to right): four nodes connected by single-headed arrows — a small oval (tumor site) → a thin curved path segment (lymphatic channel) → a round node (sentinel node) → a final node (basin inferred clear). Below the second and third nodes, a branching arrow peels downward into a separate lower node (the failure mode: blocked tracer → bypassed true node). The main track continues straight; the failure branch drops down. No labels — no text.
- [S] single-column 89mm, 300 DPI, vector, cream #F5F1E8 bg, landscape.
- [C] tumor site → tracer along lymphatic → sentinel node → inference of clear basin (main track); failure branch: blocked tracer → bypassed true first node → missed disease (failure track).
- [O] left→right main track; failure branch descends from the tracer-segment node; main arrows solid, failure branch arrow dashed.
- [P] flat vector, matte Claude palette: tumor site rust #C15F3C, lymphatic channel Sky Blue #56B4E9 (thin path), sentinel node Bluish Green #009E73 (inference anchor), clear-basin node sage #A8C0B4, failure branch nodes and arrow periwinkle #B5B4D6. Black #000000 outlines. No baked text. Flat matte, low saturation — no gradients, no gloss, no drop-shadows.
- [E] exclude: tracer chemistry details, radiotracer icons, gamma-probe shapes, node count numbers.

**NEGATIVE:** tracer details, probe shapes, node counts, gamma-detector icons, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## 15. staging-vs-therapeutic-value  — one positive node, two separable values  (VG · systems diagram · Important)
*Source: chapter 06 — "Surgical Oncology: Principles of Cancer Surgery"*

**PASTE:** Draw a blank two-path divergence diagram on a cream #F5F1E8 background. One source node on the left. Two rightward-diverging paths from it: an upper path with a solid arrow leading to a right-side destination node; a lower path with an arrow ending in a perpendicular bar (a blocked connector) leading to a different right-side destination node. The upper destination node is visually open; the lower destination node is struck through with a diagonal line. Uniform strokes, flat fills, no shading, no labels — no text.
- [S] single-column 89mm, 300 DPI, vector, cream #F5F1E8 bg, landscape.
- [C] source = positive lymph node (confirmed finding); upper path = staging value (confirmed — solid arrow leads to "staging established" node); lower path = therapeutic value (refuted — blocked arrow leads to "survival benefit absent" node struck through).
- [O] one source, two diverging paths; solid arrow = value carries through; blocked connector = value severed; the visual asymmetry between solid and blocked encodes the lesson.
- [P] flat vector, matte Claude palette: source node Blue #0072B2 (dominant finding), upper solid arrow Bluish Green #009E73 (confirmed), upper destination node rust #C15F3C, lower blocked arrow Vermillion #D55E00 (refuted), lower destination node Vermillion #D55E00 with struck-through diagonal. Black #000000 outlines. No baked text. Flat matte, low saturation — no gradients, no gloss, no drop-shadows.
- [E] exclude: trial names (MSLT-II, Z0011), drug names, lymphedema illustration, specific cancer types.

**NEGATIVE:** trial names, drug names, cancer type text, lymphedema images, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## 16. mis-oncologic-lag  — recovery benefit early, oncologic harm surfaces late  (MC · timeline · Important)
*Source: chapter 07 — "Modern Surgical Oncology: Minimally Invasive and Reconstructive Approaches"*

**PASTE:** Draw a blank dual-track horizontal timeline on a cream #F5F1E8 background. A single horizontal axis running left to right with an anchor tick mark at the left ("Operation"). Two horizontal tracks: upper track has one positive marker dot early in the timeline (labeled nothing — just a filled circle); lower track has a cluster of neutral marker dots spaced across the middle of the axis, then one negative marker dot (a square or distinct shape) far to the right. A bracket or gap annotation indicates the time lag between the last upper marker and the lower-track negative marker. No labels — no text.
- [S] single-column 89mm, 300 DPI, vector, cream #F5F1E8 bg, landscape.
- [C] upper track = recovery/morbidity outcomes (visible days to weeks post-operation — early positive markers); lower track = oncologic outcomes (measured in years — distant negative marker); the lag between tracks is the teaching point.
- [O] shared horizontal axis; upper track = fast/early; lower track = slow/late; measurement lag bracket between last upper and lower negative markers.
- [P] flat vector, matte Claude palette: operation anchor tick warm-gray #7A7368, upper-track positive markers rust #C15F3C, lower-track neutral markers warm-gray #7A7368, lower-track negative (harm) marker sage #A8C0B4. Black #000000 outlines. No baked text. Flat matte, low saturation — no gradients, no gloss, no drop-shadows.
- [E] exclude: specific operation names, trial names, exact time values, a third track.

**NEGATIVE:** operation names, trial names, time values in text, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## 17. lacc-mechanism-candidates  — one established harm, three competing hypotheses  (VG · hierarchy · Supplementary)
*Source: chapter 07 — "Modern Surgical Oncology: Minimally Invasive and Reconstructive Approaches"*

**PASTE:** Draw a blank top-down hierarchy with one root and three leaf nodes on a cream #F5F1E8 background. Root at the top center: a filled rectangle. Three child nodes below, evenly spaced, each connected to the root by a downward single-headed arrow. All three child nodes are identical in size and fill weight (equal visual weight). A small asterisk or question-mark icon beside each child node indicates uncertainty (unresolved status). No labels — no text.
- [S] single-column 89mm, 300 DPI, vector, cream #F5F1E8 bg, portrait.
- [C] root = LACC harm (established outcome); three child nodes = uterine manipulator (candidate 1), CO₂ insufflation (candidate 2), technique differences (candidate 3); equal visual weight across children signals they are competing, unresolved hypotheses.
- [O] one root, three equidistant leaves; uniform downward arrows; root visually distinguished from leaves by fill only.
- [P] flat vector, matte Claude palette: root node Sky Blue #56B4E9 (established fact, anchor), child nodes neutral gray with small uncertainty mark rust #C15F3C, arrows warm-gray #7A7368. Black #000000 outlines. No baked text. Flat matte, low saturation — no gradients, no gloss, no drop-shadows.
- [E] exclude: medical device shapes, CO₂ molecule illustration, mechanism-specific text labels.

**NEGATIVE:** device shapes, molecular illustrations, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## 18. five-rs-tumor-vs-normal  — the five Rs of radiobiology as a two-column matrix  (MC · comparison panels · Critical)
*Source: chapter 08 — "Radiation Oncology: Principles and Biology"*

**PASTE:** Draw a blank five-row, two-column grid on a cream #F5F1E8 background. Five equal horizontal rows with a thin vertical rule dividing each row into two cells. A blank header row at the top with the two column areas. Each cell in the five rows contains a small simple geometric shape (circle, line, or arc) indicating the biological effect: column 1 cells each hold a small partially-filled circle; column 2 cells each hold a small differently-filled circle; vary the fill fraction between the two cells in each row to suggest different degrees of effect. No labels — no text.
- [S] single-column 89mm, 300 DPI, vector, cream #F5F1E8 bg, portrait.
- [C] rows 1–5 = the five Rs (repair, repopulation, redistribution, reoxygenation, radiosensitivity); left column = tumor behavior between fractions; right column = normal tissue behavior; the fill fraction or shape contrast encodes whether each R favors the normal tissue, the tumor, or neither.
- [O] 5-row × 2-column grid; blank header strip; row-by-row comparison; fill contrast encodes therapeutic direction.
- [P] flat vector, matte Claude palette: normal-tissue column accented Bluish Green #009E73 where it has the advantage (repair), neutral gray where equal; tumor column neutral gray; reoxygenation row tumor cell = partial Blue #0072B2 fill (gaining oxygen vulnerability). Black #000000 outlines. No baked text. Flat matte, low saturation — no gradients, no gloss, no drop-shadows.
- [E] exclude: R names, DNA illustrations, mitochondria shapes, cell-cycle diagrams, a sixth row.

**NEGATIVE:** R names, DNA helix, organelle shapes, cell-cycle diagrams, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## 19. bragg-peak-depth-dose  — photon exit dose versus proton sharp Bragg peak  (MC · comparison panels · Important)
*Source: chapter 09 — "Modern Radiation Therapy: Technology, Toxicity, and Integration"*

**PASTE:** Draw a blank two-curve depth-dose schematic on a cream #F5F1E8 background: a shared horizontal baseline (depth axis) and a shared vertical rise axis. Curve 1: starts high at the left, falls gradually in a smooth exponential decay and continues low but nonzero all the way to the right edge — representing ongoing exit dose. Curve 2: starts low at the left, stays low across most of the horizontal axis, then rises to a single sharp peak and drops immediately to zero — no curve extending to the right of the peak. Mark the region between two vertical dashed rules as the target zone. No labels — no text.
- [S] single-column 89mm, 300 DPI, vector, cream #F5F1E8 bg, landscape.
- [C] curve 1 = photon depth-dose (high entry dose, gradual falloff, exit dose trailing past target); curve 2 = proton single Bragg peak (low dose along path, sharp peak at end of range, negligible dose beyond); target zone = shaded region between two vertical reference lines.
- [O] shared horizontal depth axis; both curves from same left origin; Bragg peak rises and falls within or at the target; photon curve extends past target; the contrast in what happens beyond the target is the teaching point.
- [P] flat vector, matte Claude palette: photon curve neutral gray (secondary), proton peak curve Blue #0072B2 (dominant), target zone light shading Sky Blue #56B4E9 at low opacity, spared-beyond region Bluish Green #009E73 for proton benefit. Black #000000 outlines. No baked text. Flat matte, low saturation — no gradients, no gloss, no drop-shadows.
- [E] exclude: dose numbers on axis, tissue type illustrations, spread-out Bragg peak detail, clinical scenario annotations.

**NEGATIVE:** dose numbers, tissue labels, patient anatomy, Bragg-peak formula text, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## 20. radiation-systemic-sequencing  — concurrent chemoradiation vs consolidation immunotherapy as two temporal architectures  (MC · timeline · Important)
*Source: chapter 09 — "Modern Radiation Therapy: Technology, Toxicity, and Integration"*

**PASTE:** Draw a blank dual-track timeline on a cream #F5F1E8 background. Shared horizontal axis. Upper track: two overlapping rectangular blocks of equal height — the blocks physically overlap in the middle, with the overlap region slightly darker fill, representing simultaneous delivery and compounded cost. Lower track: two non-overlapping sequential rectangular blocks with a small gap between them and a rightward arrow from the first to the second, representing sequential delivery exploiting primed state. Both tracks share the same timeline axis. No labels — no text.
- [S] single-column 89mm, 300 DPI, vector, cream #F5F1E8 bg, landscape.
- [C] upper track = concurrent chemoradiation (simultaneous overlapping blocks = compounded toxicity as the cost); lower track = consolidation immunotherapy after chemoradiation (sequential non-overlapping blocks = primed immunity as the benefit); the structural difference between overlap and gap is the teaching point.
- [O] two tracks sharing an axis; upper = overlapping (concurrent); lower = sequential with gap (consolidation); overlap region vs gap encodes the strategy contrast.
- [P] flat vector, matte Claude palette: chemoradiation block rust #C15F3C, concurrent overlap region Vermillion #D55E00 (toxicity cost), immunotherapy block Bluish Green #009E73 (benefit). Black #000000 outlines. No baked text. Flat matte, low saturation — no gradients, no gloss, no drop-shadows.
- [E] exclude: specific drug names, PACIFIC trial name, specific cancer names, survival statistics.

**NEGATIVE:** drug names, trial names, cancer names, survival statistics, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## 21. drug-class-cell-cycle-matrix  — cytotoxic drug classes by phase of action  (VG · comparison panels · Important)
*Source: chapter 10 — "Chemotherapy: Principles and Major Drug Classes"*

**PASTE:** Draw a blank 4×5 grid on a cream #F5F1E8 background: four rows and five columns, separated by thin rules, with a blank header row above the five columns and a blank header column at the left of the four rows. Fill certain cells with a solid colored shape — a small filled circle inside the cell — and leave other cells empty. Specific filled cells: entire top row across all five columns (alkylating agents, phase-independent); second row, second column only (antimetabolites, S-phase only); third row, fourth column only (microtubule inhibitors, M-phase only); fourth row, second and third columns (topoisomerase inhibitors, S and G2). No labels — no text.
- [S] single-column 89mm, 300 DPI, vector, cream #F5F1E8 bg, landscape.
- [C] rows = four drug classes (alkylators, antimetabolites, microtubule inhibitors, topoisomerase inhibitors); columns = five cell-cycle phases (G1, S, G2, M, G0); filled cells = active phase for that class; all-filled alkylator row encodes phase independence; the sparseness of other rows encodes specificity.
- [O] 4×5 grid; blank header strip top and left; active cells filled; empty cells blank; alkylator row visually dominant (fully filled).
- [P] flat vector, matte Claude palette: active cell fill Blue #0072B2; empty cells white with thin gray border; grid rules warm-gray #7A7368. Black #000000 outlines. No baked text. Flat matte, low saturation — no gradients, no gloss, no drop-shadows.
- [E] exclude: drug names within classes, specific drug mechanism text, a fifth drug-class row.

**NEGATIVE:** drug names, mechanism text, class labels, phase labels, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## 22. six-resistance-mechanisms  — one resistant cell with six parallel defenses  (MC · structural schematic · Critical)
*Source: chapter 11 — "Chemotherapy: Pharmacology, Resistance, and Toxicity Management"*

**PASTE:** Draw a blank annotated cellular schematic on a cream #F5F1E8 background: one large central oval (the tumor cell) with six callout connector lines radiating outward to six small rectangular callout boxes arranged around it — two on the left membrane, two on the right membrane, one near the nucleus (inner oval), one near the base. Each callout box is blank. A small filled triangle (drug molecule) appears inside the cell attempting to reach the inner oval but is depicted as blocked at two intermediate points by small perpendicular bar symbols on its path. No labels — no text.
- [S] single-column 89mm, 300 DPI, vector, cream #F5F1E8 bg.
- [C] central oval = resistant cancer cell; left-membrane callouts = reduced uptake (broken transporter), increased efflux (pump); cytoplasm callouts = drug inactivation, target alteration; inner oval = nucleus; nuclear callout = enhanced DNA repair; basal callout = apoptosis evasion; drug triangle blocked mid-path = parallel interception.
- [O] central oval, six peripheral callout boxes, one drug path blocked at two points; callout lines radiate outward symmetrically.
- [P] flat vector, matte Claude palette: central cell oval Vermillion #D55E00 (signals resistance/harm), callout boxes warm-gray #7A7368, drug molecule triangle rust #C15F3C, blocking bar symbols sage #A8C0B4. Black #000000 outlines. No baked text. Flat matte, low saturation — no gradients, no gloss, no drop-shadows.
- [E] exclude: membrane protein shapes, organelle illustrations, molecular pathway diagrams, a seventh callout.

**NEGATIVE:** organelle illustrations, protein diagrams, molecular pathway maps, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## 23. pharmacogenomic-three-pairs  — normal vs impaired metabolizer: three gene-drug pairs  (MC · comparison panels · Critical)
*Source: chapter 11 — "Chemotherapy: Pharmacology, Resistance, and Toxicity Management"*

**PASTE:** Draw a blank three-row parallel comparison on a cream #F5F1E8 background. Three horizontal rows, each divided into a left cell and a right cell by a thin vertical rule. A blank header strip at the top. In each row, the left cell contains a small short vertical bar (safe exposure level) and the right cell contains a taller vertical bar (toxic accumulation from the same starting dose). The three rows have the same bar proportions but the right-cell bar height is consistently taller than the left-cell bar in each row. No labels — no text.
- [S] single-column 89mm, 300 DPI, vector, cream #F5F1E8 bg, portrait.
- [C] rows = three gene-drug pairs (DPYD/fluoropyrimidines, UGT1A1/irinotecan, TPMT/thiopurines); left column = normal metabolizer (safe exposure); right column = impaired metabolizer (toxic accumulation from the identical starting dose); bar height = drug exposure level.
- [O] 3-row × 2-column grid; left = safe, right = toxic; bars share a common zero baseline; height encodes exposure magnitude.
- [P] flat vector, matte Claude palette: left-column safe bars rust #C15F3C, right-column toxic bars sage #A8C0B4, grid rules warm-gray #7A7368. Black #000000 outlines. No baked text. Flat matte, low saturation — no gradients, no gloss, no drop-shadows.
- [E] exclude: gene names, drug names, enzyme diagrams, percentage accumulation numbers, a fourth row.

**NEGATIVE:** gene names, drug names, enzyme structures, percentage labels, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## 24. adme-sequence-to-nadir  — the four ADME steps driving the count nadir  (MC · process flowchart · Important)
*Source: chapter 11 — "Chemotherapy: Pharmacology, Resistance, and Toxicity Management"*

**PASTE:** Draw a blank two-track stacked flow on a white background. Upper track: four small rectangular nodes connected by three single-headed rightward arrows (a four-step left-to-right sequence), ending in an output oval. Lower track: a smooth curve starting at the output oval's position, descending to a deep trough at roughly two-thirds of the timeline, then rising back toward a baseline dashed line at the right end. A dotted vertical rule connects the upper track output oval to the nadir (lowest point) of the lower track curve. No labels — no text.
- [S] single-column 89mm, 300 DPI, vector, white bg, landscape.
- [C] upper track = four ADME process nodes (absorption → distribution → metabolism → excretion) leading to plasma drug concentration (output oval); lower track = neutrophil count over time: count falls after dose (driven by drug exposure), reaches nadir at the low point, recovers to baseline; dotted vertical rule links ADME output to nadir timing.
- [O] upper track left→right sequential nodes; lower track as a smooth nadir curve below; dotted vertical link; recovery at right toward baseline dashed line.
- [P] flat vector, Okabe-Ito: ADME nodes Blue #0072B2, output oval Orange #E69F00, nadir curve descent Vermillion #D55E00, nadir lowest-point dot Vermillion #D55E00, recovery ascent Bluish Green #009E73, baseline dashed rule neutral gray. No baked text.
- [E] exclude: ADME acronym letters, exact day numbers, drug concentration values, a fifth ADME node.

**NEGATIVE:** ADME letters, day numbers, concentration values, drug names, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## Scan summary

**Chapters scanned:** 11 (01–11; 00-frontmatter, 00-introduction, 99-back-matter skipped as administrative).

**Candidates produced:** 24 total (3 from pilot preserved, 21 new).

| Chapter | Candidates |
|---|---|
| 01 — Cancer Screening | 4 (pilot), 5 |
| 02 — Cancer Diagnosis | 6, 7 |
| 03 — Molecular Diagnostics | 1 (pilot), 8, 9 |
| 04 — Principles of Cancer Therapy | 2 (pilot), 10 |
| 05 — Precision Oncology | 11, 12 |
| 06 — Surgical Oncology | 13, 14, 15 |
| 07 — Modern Surgical Oncology | 16, 17 |
| 08 — Radiation Biology | 18 |
| 09 — Modern Radiation Technology | 19, 20 |
| 10 — Chemotherapy Principles | 3 (pilot), 21 |
| 11 — Chemotherapy Pharmacology | 22, 23, 24 |

**Priority distribution:** Critical × 10, Important × 11, Supplementary × 3.

**Routed to graphs skill (quantitative/statistical — NOT previz):** PPV vs prevalence curve (ch. 01), per-cycle vs cumulative toxicity sawtooth (ch. 10), carboplatin Calvert linear plot (ch. 10), LQ survival curves semi-log (ch. 08), BED grouped bar chart (ch. 08), proton vs IMRT comparative bar (ch. 09), three-fates tumor-burden trajectories (ch. 05), pre/post biopsy probability bar pair (ch. 02).

---

## Video candidates

FIGURE staging-molecular-modifiers — Status: STATIC SUFFICIENT · Criterion: — · Reason: the mechanism is fully carried by arrow direction and shape arrangement in one frame; motion would not add information a careful static figure does not already hold.
FIGURE surrogate-endpoints — Status: STATIC SUFFICIENT · Criterion: — · Reason: the mechanism is fully carried by arrow direction and shape arrangement in one frame; motion would not add information a careful static figure does not already hold.
FIGURE combination-chemo-logic — Status: STATIC SUFFICIENT · Criterion: — · Reason: the concept is a classification or taxonomy with no temporal component; animation would impose a false sequence.
FIGURE screening-ppv-prevalence — Status: STATIC SUFFICIENT · Criterion: — · Reason: the figure is a simultaneous comparison of two or more states; motion would replace side-by-side display with a sequence that the chapter does not assert.
FIGURE screening-three-biases — Status: STATIC SUFFICIENT · Criterion: — · Reason: the figure is a simultaneous comparison of two or more states; motion would replace side-by-side display with a sequence that the chapter does not assert.
FIGURE diagnostic-chain — Status: VIDEO CANDIDATE · Criterion: 2 · Reason: a sequence of causal steps: the student must witness each stage causing the next to understand the mechanism, not merely see the endpoints.
FIGURE needle-false-negative — Status: STATIC SUFFICIENT · Criterion: — · Reason: the figure is a simultaneous comparison of two or more states; motion would replace side-by-side display with a sequence that the chapter does not assert.
FIGURE three-validity-hierarchy — Status: STATIC SUFFICIENT · Criterion: — · Reason: the concept is a classification or taxonomy with no temporal component; animation would impose a false sequence.
FIGURE liquid-biopsy-two-sources — Status: STATIC SUFFICIENT · Criterion: — · Reason: the mechanism is fully carried by arrow direction and shape arrangement in one frame; motion would not add information a careful static figure does not already hold.
FIGURE treatment-intent-tree — Status: STATIC SUFFICIENT · Criterion: — · Reason: the mechanism is fully carried by arrow direction and shape arrangement in one frame; motion would not add information a careful static figure does not already hold.
FIGURE predictive-vs-prognostic — Status: STATIC SUFFICIENT · Criterion: — · Reason: the figure is a simultaneous comparison of two or more states; motion would replace side-by-side display with a sequence that the chapter does not assert.
FIGURE basket-umbrella-platform — Status: STATIC SUFFICIENT · Criterion: — · Reason: the figure is a simultaneous comparison of two or more states; motion would replace side-by-side display with a sequence that the chapter does not assert.
FIGURE margin-examined-vs-inferred — Status: STATIC SUFFICIENT · Criterion: — · Reason: the figure is a simultaneous comparison of two or more states; motion would replace side-by-side display with a sequence that the chapter does not assert.
FIGURE sentinel-node-sampling — Status: VIDEO CANDIDATE · Criterion: 2 · Reason: a sequence of causal steps: the student must witness each stage causing the next to understand the mechanism, not merely see the endpoints.
FIGURE staging-vs-therapeutic-value — Status: STATIC SUFFICIENT · Criterion: — · Reason: the mechanism is fully carried by arrow direction and shape arrangement in one frame; motion would not add information a careful static figure does not already hold.
FIGURE mis-oncologic-lag — Status: STATIC SUFFICIENT · Criterion: — · Reason: the concept is a classification or taxonomy with no temporal component; animation would impose a false sequence.
FIGURE lacc-mechanism-candidates — Status: STATIC SUFFICIENT · Criterion: — · Reason: the mechanism is fully carried by arrow direction and shape arrangement in one frame; motion would not add information a careful static figure does not already hold.
FIGURE five-rs-tumor-vs-normal — Status: STATIC SUFFICIENT · Criterion: — · Reason: the figure is a simultaneous comparison of two or more states; motion would replace side-by-side display with a sequence that the chapter does not assert.
FIGURE bragg-peak-depth-dose — Status: STATIC SUFFICIENT · Criterion: — · Reason: the figure is a simultaneous comparison of two or more states; motion would replace side-by-side display with a sequence that the chapter does not assert.
FIGURE radiation-systemic-sequencing — Status: STATIC SUFFICIENT · Criterion: — · Reason: the concept is a classification or taxonomy with no temporal component; animation would impose a false sequence.
FIGURE drug-class-cell-cycle-matrix — Status: STATIC SUFFICIENT · Criterion: — · Reason: the figure is a simultaneous comparison of two or more states; motion would replace side-by-side display with a sequence that the chapter does not assert.
FIGURE six-resistance-mechanisms — Status: VIDEO CANDIDATE · Criterion: 3 · Reason: the cycle's mechanism — including the return stroke that resets for the next cycle — IS the teaching content; a static diagram shows topology only.
FIGURE pharmacogenomic-three-pairs — Status: STATIC SUFFICIENT · Criterion: — · Reason: the figure is a simultaneous comparison of two or more states; motion would replace side-by-side display with a sequence that the chapter does not assert.
FIGURE adme-sequence-to-nadir — Status: VIDEO CANDIDATE · Criterion: 2 · Reason: a sequence of causal steps: the student must witness each stage causing the next to understand the mechanism, not merely see the endpoints.

**Chapter recommendation:** **six-resistance-mechanisms** — highest-priority candidate (criterion 3); if produced, **diagnostic-chain**, **sentinel-node-sampling**, **adme-sequence-to-nadir** could fold in as supporting beats rather than separate videos.
