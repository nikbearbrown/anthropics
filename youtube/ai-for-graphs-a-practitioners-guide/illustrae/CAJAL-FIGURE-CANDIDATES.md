# CAJAL figure candidates — ai-for-graphs-a-practitioners-guide (previz track)

Mechanism figures mined from chapter content. Blank unannotated vector — no baked text;
previz owns every label (chart names, channel names …). Okabe-Ito, white bg, 1pt strokes,
no red-green, no 3D perspective, ≤6–8 components.

> De-confliction: this book owns visualization design-decision figures (chart taxonomy, channel hierarchy, layout decisions). NOT to be confused with data charts themselves — these are structural diagrams about chart choice, not the charts.

> Note: Most chapters describe actual data visualizations, which are NOT CAJAL candidates (bar charts, scatter plots, and standard charts are out of scope). Only structural decision diagrams and mark/channel taxonomy figures qualify.

---

## 1. mark-channel-hierarchy  — position vs luminance vs hue as perceptual accuracy levels  (VG · hierarchy · Critical)
*Source: chapter 03 — "Marks and Channels"*

**PASTE:** Draw a blank five-tier vertical ranking ladder on a white background: five horizontal rectangular bands stacked vertically, with the topmost band widest and most prominent (most accurate) and each band narrower than the one below it (less accurate). Connecting arrows point downward between adjacent bands. No labels or text.
- [S] single-column 89mm, 300 DPI, vector, white bg, portrait.
- [C] five perceptual accuracy levels from top (most accurate) to bottom: Position → Length → Area → Color Luminance → Color Hue; the narrowing ladder shape encodes decreasing perceptual accuracy.
- [O] top-to-bottom accuracy descent; widest band = highest accuracy; narrowing toward base.
- [P] flat vector, Okabe-Ito: Position band Blue #0072B2, Length band Sky Blue #56B4E9, Area band Bluish Green #009E73, Luminance band Orange #E69F00, Hue band Reddish Purple #CC79A7, downward arrows Black #000000. No baked text.
- [E] exclude: channel-name text, Stevens' law values, a sixth tier, specific example charts.

**NEGATIVE:** channel names, perceptual numbers, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## 2. chart-selection-decision-tree  — question-type to chart-type branching path  (MC · decision tree · Critical)
*Source: chapter 04 — "Chart Selection as Design Decision"*

**PASTE:** Draw a blank binary decision tree on a white background: one root rectangle at the top. Two arrows fork from it downward (left and right). Each fork leads to a rectangle. From the left rectangle, two more arrows fork to two leaf rectangles below. From the right rectangle, two more arrows fork to two leaf rectangles below. Total: 1 root + 2 intermediate + 4 leaves = 7 boxes, 6 arrows. No labels or text.
- [S] single-column 89mm, 300 DPI, vector, white bg, portrait.
- [C] root: "What is the question?" ; first branch: Comparison vs. Distribution vs. Relationship vs. Part-to-whole; each branch resolves to specific chart families; the branching logic is the teaching point.
- [O] top-down tree; root → two intermediate → four leaf nodes; binary forks.
- [P] flat vector, Okabe-Ito: root box Blue #0072B2, intermediate boxes Bluish Green #009E73, leaf boxes Sky Blue #56B4E9, arrows Black #000000. No baked text.
- [E] exclude: question-text labels, chart-name text, a third level of branching, an "eighth" leaf.

**NEGATIVE:** question text, chart names, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## 3. treemap-vs-tree-diagram  — two visual structures for the same hierarchy  (VG · comparison · Important)
*Source: chapter 12 — "Hierarchy Charts"*

**PASTE:** Draw a blank two-panel hierarchy representation on a white background. Left panel: a rectangle subdivided into nested smaller rectangles (treemap — space-filling). Right panel: a top-down tree of circles and lines (node-link diagram — spatial). Both panels represent the same abstract hierarchy. No labels or text.
- [S] single-column 89mm, 300 DPI, vector, white bg, landscape.
- [C] left panel: treemap (space-filling, nested rectangles encode part-to-whole); right panel: node-link tree (spatial, connected circles encode parent-child structure); same hierarchy, different visual questions answered.
- [O] two equal-size panels side by side; left = space-filling, right = relational structure.
- [P] flat vector, Okabe-Ito: treemap large rectangles Blue #0072B2, treemap small rectangles Sky Blue #56B4E9, tree nodes Bluish Green #009E73, tree links Black #000000. No baked text.
- [E] exclude: node-name text, area-value percentages, a third panel, color-coded categories.

**NEGATIVE:** node names, area values, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## 4. sankey-magnitude-flow  — width-encoded flow through intermediate nodes  (MC · mechanism · Important)
*Source: chapter 13 — "Flow and Network Charts"*

**PASTE:** Draw a blank Sankey-style flow diagram on a white background: on the left, two wide horizontal bands (two source streams) flow right through a central region, merge and re-split through one intermediate rectangle node, then emerge as three thinner bands on the right (three destination streams). Band width varies; no labels or text.
- [S] single-column 89mm, 300 DPI, vector, white bg, landscape.
- [C] two source flows (left) merging through one intermediate node; three destination flows (right); flow-width encodes magnitude; the width-magnitude encoding is the teaching point.
- [O] left-to-right flow; source bands wider than destination bands; intermediate node bridges flows.
- [P] flat vector, Okabe-Ito: source-A band Blue #0072B2, source-B band Bluish Green #009E73, intermediate node Orange #E69F00, destination bands Sky Blue #56B4E9. No baked text.
- [E] exclude: flow-volume numbers, category labels, a second intermediate node, percent annotations.

**NEGATIVE:** flow volume numbers, category text, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## 5. specialized-chart-decision-gate  — use-specialized-form vs replace-with-standard fork  (VG · decision flow · Supplementary)
*Source: chapter 15 — "Specialized and Financial Charts"*

**PASTE:** Draw a blank two-branch decision gate on a white background: one root diamond (decision node) at top center. Left branch arrow leads to a rectangle (keep specialized form). Right branch arrow leads to a rectangle (replace with standard form). A small circle gateway sits between the root diamond and the right rectangle (audience-check gate). No text.
- [S] single-column 89mm, 300 DPI, vector, white bg, landscape.
- [C] decision diamond: "Does the specialized form answer the question better?" Yes → keep specialized; No → audience-graphicacy check → replace with standard; the two-step gate is the teaching point.
- [O] root diamond → left (keep) and right (replace) branches; right branch has intermediate gateway circle.
- [P] flat vector, Okabe-Ito: decision diamond Orange #E69F00, keep rectangle Blue #0072B2, audience-check circle Sky Blue #56B4E9, replace rectangle Bluish Green #009E73, arrows Black #000000. No baked text.
- [E] exclude: chart-type names, audience-level text, a third branch, a return loop.

**NEGATIVE:** chart type names, audience labels, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## Video candidates

FIGURE mark-channel-hierarchy — Status: STATIC SUFFICIENT · Criterion: — · Reason: the mechanism is fully carried by arrow direction and shape arrangement in one frame; motion would not add information a careful static figure does not already hold.
FIGURE chart-selection-decision-tree — Status: STATIC SUFFICIENT · Criterion: — · Reason: the steps are discrete, separated by significant time, and none has a transition mechanism the student must witness; numbered panels let the learner control pacing.
FIGURE treemap-vs-tree-diagram — Status: STATIC SUFFICIENT · Criterion: — · Reason: the figure is a simultaneous comparison of two or more states; motion would replace side-by-side display with a sequence that the chapter does not assert.
FIGURE sankey-magnitude-flow — Status: STATIC SUFFICIENT · Criterion: — · Reason: the mechanism is fully carried by arrow direction and shape arrangement in one frame; motion would not add information a careful static figure does not already hold.
FIGURE specialized-chart-decision-gate — Status: STATIC SUFFICIENT · Criterion: — · Reason: the mechanism is fully carried by arrow direction and shape arrangement in one frame; motion would not add information a careful static figure does not already hold.

**Chapter recommendation:** None — no entry in this file clears the motion bar; static figures serve every concept here.
