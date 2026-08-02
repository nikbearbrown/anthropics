# CAJAL figure candidates — algorithms-vol1-with-llms (previz track)

Mechanism and structure figures mined from chapter text. Blank unannotated vector — no baked text;
labels applied post-generation. Okabe-Ito, white bg, 1pt strokes, no red-green, no 3D perspective, ≤6–8 components.

> Chapter content is identical to **algorithms-vol1**. All CAJAL figure candidates carry over directly from `../algorithms-vol1/illustrae/CAJAL-FIGURE-CANDIDATES.md`. The candidates below are restated here for completeness so each book's `illustrae/` is self-contained.

---

## 1. memory-layout-array-vs-linkedlist  — contiguous array vs scattered linked-list memory layout  (VG · comparison panels · Critical)
*Source: chapter 3 — "Data Structures"*

**PASTE:** Draw a blank two-panel memory layout diagram on a white background. Top panel: a row of equal-sized adjacent rectangles (contiguous colored blocks) all touching each other in a line — the dynamic array. Bottom panel: the same number of rectangles but scattered across the panel at various positions, each containing a small curved arrow pointing to the next one at a different location — the linked list. No text, no numbers, no address labels.
- [S] single-column 89mm, 300 DPI, vector, white bg.
- [C] top panel: 6 adjacent equal-sized contiguous rectangles; bottom panel: same 6 rectangles scattered with pointer arrows connecting each to the next at a different position.
- [O] top panel has all blocks touching; bottom panel has blocks at varied positions with curved pointer arrows; visual contrast is the key.
- [P] flat vector, Okabe-Ito: array blocks Blue #0072B2, linked-list blocks Sky Blue #56B4E9, pointer arrows Vermillion #D55E00, panel divider neutral gray dashed. No baked text.
- [E] exclude: memory addresses, index numbers, data values, "array"/"linked list" labels.

**NEGATIVE:** text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, 3D perspective

---

## 2. heap-tree-and-array  — min-heap as binary tree paired with its flat-array representation  (VG · comparison panels · Critical)
*Source: chapter 3 — "Data Structures"*

**PASTE:** Draw a blank two-panel diagram on a white background. Left panel: a binary tree with 7 nodes arranged in heap structure — nodes are circles connected by edges. Right panel: a flat row of 7 equal-sized rectangles representing the array — small curved arrows from each tree node indicate its corresponding array slot. No text, no values.
- [S] single-column 89mm, 300 DPI, vector, white bg, landscape.
- [C] left: 7-node complete binary tree; right: 7-element flat array; connector arrows from tree to array.
- [O] tree left, array right; arrows cross panels; root connects to slot 0.
- [P] flat vector, Okabe-Ito: tree nodes Blue #0072B2, tree edges neutral gray, array slots Sky Blue #56B4E9, connector arrows Orange #E69F00. No baked text.
- [E] exclude: node values, index numbers, parent-child formulas, heap-property labels.

**NEGATIVE:** text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, 3D perspective

---

## 3. bst-degenerate-vs-balanced  — degenerate BST vs balanced red-black tree  (VG · comparison panels · Critical)
*Source: chapter 3 — "Data Structures"*

**PASTE:** Draw a blank two-panel tree diagram. Left panel: 6-node right-leaning chain (degenerate BST). Right panel: same 6 nodes in a balanced 3-level tree. No values, no labels.
- [S] single-column 89mm, 300 DPI, vector, white bg, landscape.
- [C] left: 6-node chain tree (degenerate); right: 6-node balanced tree; roots at top.
- [O] root at top; left tall/narrow; right short/wide; height contrast visible.
- [P] flat vector, Okabe-Ito: degenerate nodes/edges Vermillion #D55E00, balanced nodes/edges Bluish Green #009E73. No baked text.
- [E] exclude: key values, rotation labels, red/black coloring, height annotations.

**NEGATIVE:** text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, 3D perspective

---

## 4. path-compression-union-find  — before/after path compression in Union-Find  (MC · comparison panels · Critical)
*Source: chapter 3 — "Data Structures"*

**PASTE:** Left panel: 5-node vertical chain tree with upward parent pointers. Right panel: same nodes after path compression — all 4 non-root nodes point directly to root (flat star). No text, no labels.
- [S] single-column 89mm, 300 DPI, vector, white bg, landscape.
- [C] left: 5-node chain with upward arrows; right: flat star with 4 direct-to-root arrows; root node distinct.
- [O] left tall, right flat; visual emphasis on structural flattening.
- [P] flat vector, Okabe-Ito: root Blue #0072B2, other nodes Sky Blue #56B4E9, pre-compression arrows Bluish Green #009E73, post-compression arrows Orange #E69F00. No baked text.
- [E] exclude: node index labels, rank values, algorithm text.

**NEGATIVE:** text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, 3D perspective

---

## 5. bfs-vs-dfs-traversal  — BFS and DFS traversal on the same graph  (MC · comparison panels · Critical)
*Source: chapter 5 — "Graphs and Graph Search Algorithms"*

**PASTE:** Two panels showing the same 8-node graph. Left: BFS-order coloring (concentric rings). Right: DFS-order (one bold path + lighter backtracks). No text, no numbers.
- [S] single-column 89mm, 300 DPI, vector, white bg, landscape.
- [C] two panels; identical 8-node graph; left BFS concentric-ring coloring; right DFS path coloring; source node distinct.
- [O] identical graph layout both panels; source at same position.
- [P] flat vector, Okabe-Ito: source Black #000000, BFS ring 1 Blue #0072B2, BFS ring 2 Sky Blue #56B4E9, DFS path Bluish Green #009E73, DFS backtracks Orange #E69F00, edges neutral gray. No baked text.
- [E] exclude: node/edge labels, visit-order numbers, algorithm names.

**NEGATIVE:** text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, 3D perspective

---

## 6. dijkstra-negative-edge-failure  — graph where Dijkstra fails due to a negative edge  (VG · mechanism cross-section · Critical)
*Source: chapter 5 — "Graphs and Graph Search Algorithms"*

**PASTE:** 4–5 node directed graph; one edge dashed/colored differently (negative); one node marked with X (incorrectly finalized). No text, no weights.
- [S] single-column 89mm, 300 DPI, vector, white bg.
- [C] 4-node directed graph; negative edge highlighted; incorrectly-finalized node with X mark; directed arrows on all edges.
- [O] diamond or chain node layout; negative edge creating the shortcut.
- [P] flat vector, Okabe-Ito: regular edges neutral gray, negative edge Vermillion #D55E00 dashed, X-node Orange #E69F00, source Blue #0072B2, others Sky Blue #56B4E9. No baked text.
- [E] exclude: edge weights, node labels, algorithm steps.

**NEGATIVE:** text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, 3D perspective

---

## 7. dp-subproblem-dag  — DAG of overlapping subproblems in dynamic programming  (VG · systems diagram · Critical)
*Source: chapter 8 — "Dynamic Programming"*

**PASTE:** ~7-node DAG; root at top; shared intermediate nodes have multiple incoming edges; leaves at bottom; shared nodes visually distinct. No text.
- [S] single-column 89mm, 300 DPI, vector, white bg.
- [C] root node; unique subproblem nodes; shared/overlapping subproblem nodes (multiple incoming edges); leaf nodes; downward directed edges.
- [O] root at top; DAG fans downward; shared nodes at second/third levels.
- [P] flat vector, Okabe-Ito: root Blue #0072B2, unique nodes Sky Blue #56B4E9, shared nodes Bluish Green #009E73, leaves Orange #E69F00, edges Black #000000. No baked text.
- [E] exclude: subproblem formulas, node labels, memoization annotations.

**NEGATIVE:** text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, 3D perspective

---

## 8. np-complexity-class-hierarchy  — P ⊆ NP, NP-hard, NP-complete containment structure  (VG · hierarchy · Critical)
*Source: chapter 10 — "NP-Completeness and Intractability"*

**PASTE:** Nested ovals: innermost (P), enclosing (NP), outer region (NP-hard), crescent overlap (NP-complete). Distinct fill colors. No text.
- [S] single-column 89mm, 300 DPI, vector, white bg, square.
- [C] four nested/overlapping regions with distinct colors; P smallest; NP-complete crescent at NP/NP-hard boundary.
- [O] centered nesting; P centered inside NP; NP-hard extends beyond NP.
- [P] flat vector, Okabe-Ito: P region Bluish Green #009E73, NP border Blue #0072B2, NP-hard neutral gray, NP-complete Orange #E69F00. No baked text.
- [E] exclude: class name labels, problem examples, reduction arrows.

**NEGATIVE:** text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, 3D perspective

---

*Chapters with zero CAJAL candidates: 01, 02, 04, 11, 12, 13 — same as algorithms-vol1. Zero-candidate chapter count: 6.*

---

## Video candidates

FIGURE memory-layout-array-vs-linkedlist — Status: STATIC SUFFICIENT · Criterion: — · Reason: the figure is a simultaneous comparison of two or more states; motion would replace side-by-side display with a sequence that the chapter does not assert.
FIGURE heap-tree-and-array — Status: STATIC SUFFICIENT · Criterion: — · Reason: the figure is a simultaneous comparison of two or more states; motion would replace side-by-side display with a sequence that the chapter does not assert.
FIGURE bst-degenerate-vs-balanced — Status: STATIC SUFFICIENT · Criterion: — · Reason: the figure is a simultaneous comparison of two or more states; motion would replace side-by-side display with a sequence that the chapter does not assert.
FIGURE path-compression-union-find — Status: STATIC SUFFICIENT · Criterion: — · Reason: the figure is a simultaneous comparison of two or more states; motion would replace side-by-side display with a sequence that the chapter does not assert.
FIGURE bfs-vs-dfs-traversal — Status: STATIC SUFFICIENT · Criterion: — · Reason: the figure is a simultaneous comparison of two or more states; motion would replace side-by-side display with a sequence that the chapter does not assert.
FIGURE dijkstra-negative-edge-failure — Status: STATIC SUFFICIENT · Criterion: — · Reason: the mechanism is fully carried by arrow direction and shape arrangement in one frame; motion would not add information a careful static figure does not already hold.
FIGURE dp-subproblem-dag — Status: STATIC SUFFICIENT · Criterion: — · Reason: the mechanism is fully carried by arrow direction and shape arrangement in one frame; motion would not add information a careful static figure does not already hold.
FIGURE np-complexity-class-hierarchy — Status: STATIC SUFFICIENT · Criterion: — · Reason: the mechanism is fully carried by arrow direction and shape arrangement in one frame; motion would not add information a careful static figure does not already hold.

**Chapter recommendation:** None — no entry in this file clears the motion bar; static figures serve every concept here.
