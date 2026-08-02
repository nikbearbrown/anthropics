# CAJAL figure candidates — algorithms-vol1 (previz track)

Mechanism and structure figures mined from chapter text. Blank unannotated vector — no baked text;
labels applied post-generation. Okabe-Ito, white bg, 1pt strokes, no red-green, no 3D perspective, ≤6–8 components.

---

## 1. memory-layout-array-vs-linkedlist  — contiguous array vs scattered linked-list memory layout  (VG · comparison panels · Critical)
*Source: chapter 3 — "Data Structures"*

**PASTE:** Draw a blank two-panel memory layout diagram on a white background. Top panel: a row of equal-sized adjacent rectangles (contiguous colored blocks) all touching each other in a line — the dynamic array. Bottom panel: the same number of rectangles but scattered across the panel at various positions, each containing a small curved arrow pointing to the next one at a different location — the linked list. No text, no numbers, no address labels.
- [S] single-column 89mm, 300 DPI, vector, white bg.
- [C] top panel: 6 adjacent equal-sized contiguous rectangles; bottom panel: same 6 rectangles scattered with pointer arrows connecting each to the next at a different position; panel labels omitted.
- [O] top panel has all blocks touching; bottom panel has blocks at varied positions with curved pointer arrows; visual contrast between the two layouts is the key.
- [P] flat vector, Okabe-Ito: array blocks Blue #0072B2, linked-list blocks Sky Blue #56B4E9, pointer arrows Vermillion #D55E00, panel divider neutral gray dashed. No baked text.
- [E] exclude: memory addresses, index numbers, data values, "array"/"linked list" labels.

**NEGATIVE:** text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, 3D perspective

---

## 2. heap-tree-and-array  — min-heap as binary tree paired with its flat-array representation  (VG · comparison panels · Critical)
*Source: chapter 3 — "Data Structures"*

**PASTE:** Draw a blank two-panel diagram on a white background. Left panel: a binary tree with 7 nodes arranged in heap structure (root at top, filled in level-by-level) — nodes are numbered circles (indices 0–6) with no values, connected by edges. Right panel: a flat row of 7 equal-sized rectangles (one per node) arranged left to right, representing the array — with small curved arrows from each tree node in the left panel indicating its corresponding array slot. No text, no values inside circles or rectangles.
- [S] single-column 89mm, 300 DPI, vector, white bg, landscape.
- [C] left panel: 7-node complete binary tree (heap shape); right panel: 7-element array row; connector arrows from tree nodes to corresponding array slots; index markers (small dots only, no numbers).
- [O] tree on left, array on right; arrows cross from left panel to right; root node connects to slot 0.
- [P] flat vector, Okabe-Ito: tree nodes Blue #0072B2, tree edges neutral gray, array slots Sky Blue #56B4E9, connector arrows Orange #E69F00. No baked text.
- [E] exclude: node values, index numbers, parent-child formulas, heap-property labels.

**NEGATIVE:** text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, 3D perspective

---

## 3. bst-degenerate-vs-balanced  — degenerate BST (sorted-input chain) vs balanced red-black tree  (VG · comparison panels · Critical)
*Source: chapter 3 — "Data Structures"*

**PASTE:** Draw a blank two-panel tree diagram on a white background. Left panel: a degenerate binary search tree — all nodes strung in a right-leaning chain (like a linked list tilted), height n. Right panel: the same number of nodes arranged in a balanced tree with height approximately log n — roughly a symmetric branching structure. Each node is a small circle, edges are lines. No text, no values, no colors inside nodes.
- [S] single-column 89mm, 300 DPI, vector, white bg, landscape.
- [C] left panel: 6-node right-leaning chain tree (degenerate); right panel: same 6 nodes in a balanced 3-level tree; root nodes at top in both panels.
- [O] root at top; left panel is tall/narrow; right panel is short/wide; height contrast is the teaching point.
- [P] flat vector, Okabe-Ito: degenerate tree nodes Vermillion #D55E00, degenerate edges Vermillion #D55E00, balanced tree nodes Bluish Green #009E73, balanced edges Bluish Green #009E73 (lighter). No baked text.
- [E] exclude: key values, rotation labels, red/black colors, height annotations, n vs log-n text.

**NEGATIVE:** text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, 3D perspective

---

## 4. path-compression-union-find  — before/after path compression in Union-Find  (MC · comparison panels · Critical)
*Source: chapter 3 — "Data Structures"*

**PASTE:** Draw a blank two-panel diagram on a white background. Left panel: a deep chain of 5 nodes (a tall tree) — each node points only to its parent in a vertical chain, root at top. Right panel: the same 5 nodes after path compression — all nodes except the root now point directly to the root, forming a flat star shape. Arrows show parent pointers. No text, no labels.
- [S] single-column 89mm, 300 DPI, vector, white bg, landscape.
- [C] left panel: 5-node vertical chain tree with upward parent-pointer arrows; right panel: same 5 nodes with 4 of them pointing directly to root (flat star structure); root node distinct.
- [O] left panel tall, right panel flat; visual emphasis on the structural difference.
- [P] flat vector, Okabe-Ito: root node Blue #0072B2, other nodes Sky Blue #56B4E9, parent arrows Bluish Green #009E73, right-panel arrows Orange #E69F00 (showing the compressed paths). No baked text.
- [E] exclude: node index labels, rank values, path-compression algorithm text, α notation.

**NEGATIVE:** text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, 3D perspective

---

## 5. bfs-vs-dfs-traversal  — BFS and DFS traversal order on the same graph  (MC · comparison panels · Critical)
*Source: chapter 5 — "Graphs and Graph Search Algorithms"*

**PASTE:** Draw a blank two-panel diagram on a white background. Each panel shows the same small graph (8 nodes, ~10 edges). Left panel: nodes colored or numbered to show BFS visit order — nodes at the same distance from source share a color level (concentric-ring coloring). Right panel: same graph with nodes colored to show DFS visit order — one continuous path highlighted before backtracking. Source node is distinct in both panels. No text, no numbers.
- [S] single-column 89mm, 300 DPI, vector, white bg, landscape.
- [C] two panels with identical graph structure (8 nodes, ~10 edges); left: BFS-order coloring (source = darkest, each ring lighter); right: DFS-order coloring (one path bold, backtracks lighter); source node marked differently.
- [O] graph layout identical in both panels; source node at same position; edges identical.
- [P] flat vector, Okabe-Ito: source node Black #000000, BFS ring 1 Blue #0072B2, BFS ring 2 Sky Blue #56B4E9, DFS path Bluish Green #009E73, DFS backtracks Orange #E69F00, edges neutral gray. No baked text.
- [E] exclude: node/edge labels, visit-order numbers, BFS/DFS text, algorithm steps.

**NEGATIVE:** text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, 3D perspective

---

## 6. dijkstra-negative-edge-failure  — graph where Dijkstra's finalization fails due to a negative edge  (VG · mechanism cross-section · Critical)
*Source: chapter 5 — "Graphs and Graph Search Algorithms"*

**PASTE:** Draw a blank directed graph on a white background: four nodes (A, B, C, D — represented as circles only, no letters) arranged so that Dijkstra finalizes one node prematurely. Show one edge with a distinctive appearance (dashed or distinct color) indicating the negative weight. Show with an X marker that the algorithm's "finalized" node has an incorrect distance. Edges are directed (one-way arrows). No text, no weights, no labels.
- [S] single-column 89mm, 300 DPI, vector, white bg.
- [C] 4–5 node directed graph; one negative-edge highlighted in a distinct style; one node marked with an X (incorrectly finalized); directed arrows on all edges.
- [O] nodes arranged in a diamond or chain layout; the negative edge creates a shortcut the algorithm missed.
- [P] flat vector, Okabe-Ito: regular edges neutral gray arrows, negative edge Vermillion #D55E00 dashed, incorrectly-finalized node Orange #E69F00 with X mark, source node Blue #0072B2, other nodes Sky Blue #56B4E9. No baked text.
- [E] exclude: edge weights, node labels (A/B/C/D), algorithm step numbers, "Dijkstra" text.

**NEGATIVE:** text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, 3D perspective

---

## 7. mst-construction-steps  — step-by-step MST construction on a small weighted graph  (MC · timeline/progression · Important)
*Source: chapter 5 — "Graphs and Graph Search Algorithms"*

**PASTE:** Draw a blank three-panel diagram on a white background. Each panel shows the same 5-node graph. Panel 1: the full graph with all edges drawn (no MST yet). Panel 2: the graph with the first two cheapest edges added to the MST highlighted (heavier strokes). Panel 3: the complete MST highlighted — spanning all 5 nodes with 4 edges bold, the remaining non-MST edges shown as thin gray. No text, no weight labels.
- [S] single-column 89mm, 300 DPI, vector, white bg, landscape.
- [C] three panels of the same 5-node graph; panel 1 all edges same weight appearance; panel 2 two MST edges bold; panel 3 four MST edges bold with non-MST edges faint.
- [O] graph layout identical across all three panels; progression shows growing MST.
- [P] flat vector, Okabe-Ito: nodes Blue #0072B2, non-MST edges neutral gray, MST edges Bluish Green #009E73 bold strokes. No baked text.
- [E] exclude: edge weights, node labels, Kruskal/Prim algorithm labels, step numbers.

**NEGATIVE:** text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, 3D perspective

---

## 8. dp-subproblem-dag  — the DAG of overlapping subproblems in dynamic programming  (VG · systems diagram · Critical)
*Source: chapter 8 — "Dynamic Programming"*

**PASTE:** Draw a blank directed acyclic graph (DAG) on a white background showing the subproblem-overlap structure. Root node at top. The graph fans out downward into an overlapping tree structure where several intermediate nodes are shared by multiple paths (these shared nodes appear only once but have multiple incoming edges from different parents). Leaf nodes at the bottom. The shared (overlapping) nodes are visually distinct (different fill). No text, no labels.
- [S] single-column 89mm, 300 DPI, vector, white bg.
- [C] ~7 nodes in a DAG; root at top; several intermediate shared-subproblem nodes (multiple incoming edges); leaf nodes at bottom; directed edges point downward.
- [O] root at top; DAG fans downward; shared nodes at the second and third levels; edges show the overlap clearly.
- [P] flat vector, Okabe-Ito: root node Blue #0072B2, unique subproblem nodes Sky Blue #56B4E9, shared/overlapping subproblem nodes Bluish Green #009E73, leaf nodes Orange #E69F00, edges Black #000000. No baked text.
- [E] exclude: subproblem formulas, node labels, memoization annotations, recurrence text.

**NEGATIVE:** text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, 3D perspective

---

## 9. network-flow-residual  — a flow network and its residual graph side by side  (VG · comparison panels · Important)
*Source: chapter 9 — "Network Flow"*

**PASTE:** Draw a blank two-panel diagram on a white background. Left panel: a directed flow network — 4–5 nodes connected by directed edges; some edges have heavier strokes indicating flow. Right panel: the same network showing the residual graph — original edges with remaining capacity shown as thinner arrows, and backward (reverse) edges shown as dashed arrows in the opposite direction. No text, no capacity numbers, no labels.
- [S] single-column 89mm, 300 DPI, vector, white bg, landscape.
- [C] two panels; left: 5-node directed graph with flow edges; right: same graph with forward residual edges + backward dashed residual edges; source and sink nodes marked distinctly.
- [O] same node layout in both panels; flow network on left; residual graph on right.
- [P] flat vector, Okabe-Ito: source node Bluish Green #009E73, sink node Orange #E69F00, other nodes Blue #0072B2, flow edges Black #000000 (bold), residual forward edges Sky Blue #56B4E9, residual backward edges Vermillion #D55E00 dashed. No baked text.
- [E] exclude: capacity numbers, flow values, source/sink labels (s/t), algorithm steps.

**NEGATIVE:** text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, 3D perspective

---

## 10. np-complexity-class-hierarchy  — the four complexity class containments P ⊆ NP, NP-hard, NP-complete  (VG · hierarchy · Critical)
*Source: chapter 10 — "NP-Completeness and Intractability"*

**PASTE:** Draw a blank nested-oval hierarchy on a white background showing complexity class containments: an innermost oval (P), contained within a larger oval (NP), with a region just outside the NP oval labeled as NP-hard territory (a partial outer oval), and the overlap region between NP and NP-hard shown as NP-complete (a crescent or intersection region). Distinct fill colors for each region. No text, no labels.
- [S] single-column 89mm, 300 DPI, vector, white bg, square.
- [C] innermost oval (P); enclosing oval (NP); outer region arching over NP (NP-hard); intersection crescent region (NP-complete); distinct fill for each region.
- [O] nested ovals centered; P smallest; NP larger; NP-hard region partially overlapping NP from outside; NP-complete as the overlap crescent.
- [P] flat vector, Okabe-Ito: P oval Bluish Green #009E73, NP oval Blue #0072B2 (border only, P fills interior), NP-hard outer region neutral gray, NP-complete crescent Orange #E69F00. No baked text.
- [E] exclude: class name labels (P/NP/NP-hard/NP-complete), problem examples, reduction arrows, "polynomial time" text.

**NEGATIVE:** text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, 3D perspective

---

*Chapters with zero CAJAL candidates: 01-introduction-to-algorithms (conceptual framework — no structure diagram), 02-algorithm-analysis (asymptotic notation — quantitative plots), 04-sorting-and-caching (algorithm performance — quantitative; cache diagrams are structural but primarily quantitative comparisons), 11-approximation-algorithms (ratio bounds — no structure mechanism diagram), 12-randomized-algorithms (probabilistic analysis — quantitative), 13-linear-programming (geometric feasible region — axis-based). Zero-candidate chapter count: 6.*

---

## Video candidates

FIGURE memory-layout-array-vs-linkedlist — Status: STATIC SUFFICIENT · Criterion: — · Reason: the figure is a simultaneous comparison of two or more states; motion would replace side-by-side display with a sequence that the chapter does not assert.
FIGURE heap-tree-and-array — Status: STATIC SUFFICIENT · Criterion: — · Reason: the figure is a simultaneous comparison of two or more states; motion would replace side-by-side display with a sequence that the chapter does not assert.
FIGURE bst-degenerate-vs-balanced — Status: STATIC SUFFICIENT · Criterion: — · Reason: the mechanism is fully carried by arrow direction and shape arrangement in one frame; motion would not add information a careful static figure does not already hold.
FIGURE path-compression-union-find — Status: STATIC SUFFICIENT · Criterion: — · Reason: the figure is a simultaneous comparison of two or more states; motion would replace side-by-side display with a sequence that the chapter does not assert.
FIGURE bfs-vs-dfs-traversal — Status: STATIC SUFFICIENT · Criterion: — · Reason: the figure is a simultaneous comparison of two or more states; motion would replace side-by-side display with a sequence that the chapter does not assert.
FIGURE dijkstra-negative-edge-failure — Status: STATIC SUFFICIENT · Criterion: — · Reason: the mechanism is fully carried by arrow direction and shape arrangement in one frame; motion would not add information a careful static figure does not already hold.
FIGURE mst-construction-steps — Status: STATIC SUFFICIENT · Criterion: — · Reason: the concept is a classification or taxonomy with no temporal component; animation would impose a false sequence.
FIGURE dp-subproblem-dag — Status: STATIC SUFFICIENT · Criterion: — · Reason: the mechanism is fully carried by arrow direction and shape arrangement in one frame; motion would not add information a careful static figure does not already hold.
FIGURE network-flow-residual — Status: STATIC SUFFICIENT · Criterion: — · Reason: the figure is a simultaneous comparison of two or more states; motion would replace side-by-side display with a sequence that the chapter does not assert.
FIGURE np-complexity-class-hierarchy — Status: STATIC SUFFICIENT · Criterion: — · Reason: the mechanism is fully carried by arrow direction and shape arrangement in one frame; motion would not add information a careful static figure does not already hold.

**Chapter recommendation:** None — no entry in this file clears the motion bar; static figures serve every concept here.
