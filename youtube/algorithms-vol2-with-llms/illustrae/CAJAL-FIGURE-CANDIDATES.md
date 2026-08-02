# CAJAL figure candidates — algorithms-vol2-with-llms (previz track)

Mechanism and structure figures mined from chapter text. Blank unannotated vector — no baked text;
labels applied post-generation. Okabe-Ito, white bg, 1pt strokes, no red-green, no 3D perspective, ≤6–8 components.

> Chapter content is identical to **algorithms-vol2**. All CAJAL figure candidates carry over directly from `../algorithms-vol2/illustrae/CAJAL-FIGURE-CANDIDATES.md`. Candidates are restated here for self-containment.

---

## 1. payoff-matrix-prisoner-dilemma  — the 2×2 payoff matrix structure for the Prisoner's Dilemma  (VG · structural · Critical)
*Source: chapter 4 — "Game Theory"*

**PASTE:** Draw a blank 2×2 payoff matrix on a white background: four equal cells. Each cell contains two payoff-indicator symbols (colored circles) — one for each player. Fill intensity encodes payoff magnitude (darker = better). Top-left (both cooperate — medium), top-right (player 1 defects — high P1/low P2), bottom-left (player 2 defects — low P1/high P2), bottom-right (both defect — low for both). No text, no numbers.
- [S] single-column 89mm, 300 DPI, vector, white bg, square.
- [C] 2×2 grid; four cells; two payoff-indicator symbols per cell; fill intensity varies by payoff level.
- [O] equal cells; rows = Player 1 strategies; columns = Player 2 strategies.
- [P] flat vector, Okabe-Ito: Player 1 indicators Blue #0072B2, Player 2 indicators Orange #E69F00, cell borders Black #000000. No baked text.
- [E] exclude: strategy names, payoff numbers, player labels, equilibrium markers.

**NEGATIVE:** text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, 3D perspective

---

## 2. scheduling-dependency-dag  — task-dependency DAG with critical path highlighted  (VG · systems diagram · Critical)
*Source: chapter 5 — "Scheduling"*

**PASTE:** 7-node DAG, left-to-right directed edges, critical path (longest) highlighted bold. Source left, sink right. No text.
- [S] single-column 89mm, 300 DPI, vector, white bg, landscape.
- [C] 7-node DAG; directed edges; critical path in bold blue; other paths neutral gray; source/sink distinct.
- [O] left-to-right flow; parallel levels; critical path one unbroken chain.
- [P] flat vector, Okabe-Ito: source/sink Bluish Green #009E73, critical-path nodes/edges Blue #0072B2 bold, others neutral gray. No baked text.
- [E] exclude: task names, duration labels, machine assignments.

**NEGATIVE:** text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, 3D perspective

---

## 3. stable-matching-preference-bipartite  — bipartite graph of proposers and receivers with preference ordering  (VG · structural · Critical)
*Source: chapter 6 — "Stable Matching and Gale-Shapley"*

**PASTE:** 4 proposer nodes (left column) and 4 receiver nodes (right column). Each proposer has three edges at varying boldness (first preference boldest, third lightest). No text.
- [S] single-column 89mm, 300 DPI, vector, white bg.
- [C] 4 proposer nodes left; 4 receiver nodes right; 3 edges per proposer; edge boldness = preference rank.
- [O] two vertical columns; edges cross between them at various positions.
- [P] flat vector, Okabe-Ito: proposers Blue #0072B2, receivers Orange #E69F00, first-pref edges Black at 2pt, second Sky Blue at 1.5pt, third neutral gray at 0.75pt. No baked text.
- [E] exclude: names, numbers, rank labels.

**NEGATIVE:** text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, 3D perspective

---

## 4. social-network-strong-weak-ties  — two dense clusters connected by a single weak-tie bridge  (VG · systems diagram · Critical)
*Source: chapter 8 — "Social Networks"*

**PASTE:** Two dense 5-node clusters; bold internal edges; one thin dashed bridge edge between the clusters. No text.
- [S] single-column 89mm, 300 DPI, vector, white bg, landscape.
- [C] two 5-node clusters with many internal edges; one bridge edge; bridge-adjacent nodes distinct.
- [O] clusters left and right; bridge edge in the gap.
- [P] flat vector, Okabe-Ito: left cluster Blue #0072B2, right cluster Orange #E69F00, internal edges neutral gray bold, bridge Bluish Green #009E73 thin dashed. No baked text.
- [E] exclude: node names, edge labels, centrality values.

**NEGATIVE:** text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, 3D perspective

---

*Chapters with zero CAJAL candidates: 01, 02, 03, 07 — same as algorithms-vol2. Zero-candidate chapter count: 4.*

---

## Video candidates

FIGURE payoff-matrix-prisoner-dilemma — Status: STATIC SUFFICIENT · Criterion: — · Reason: the figure is a spatial cross-section or structural schematic whose value lies in inspecting all parts simultaneously.
FIGURE scheduling-dependency-dag — Status: STATIC SUFFICIENT · Criterion: — · Reason: the mechanism is fully carried by arrow direction and shape arrangement in one frame; motion would not add information a careful static figure does not already hold.
FIGURE stable-matching-preference-bipartite — Status: STATIC SUFFICIENT · Criterion: — · Reason: the figure is a spatial cross-section or structural schematic whose value lies in inspecting all parts simultaneously.
FIGURE social-network-strong-weak-ties — Status: STATIC SUFFICIENT · Criterion: — · Reason: the mechanism is fully carried by arrow direction and shape arrangement in one frame; motion would not add information a careful static figure does not already hold.

**Chapter recommendation:** None — no entry in this file clears the motion bar; static figures serve every concept here.
