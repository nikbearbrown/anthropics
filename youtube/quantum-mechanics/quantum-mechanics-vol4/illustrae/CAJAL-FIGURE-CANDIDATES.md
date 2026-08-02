# CAJAL figure candidates — quantum-mechanics-vol4 (previz track)

Quantum-information volume. Mechanism figures mined chapter-by-chapter plus reel beat sheets. Blank unannotated vector — no baked text; previz owns every symbol. matte Claude palette, cream #F5F1E8 bg, 1pt strokes, no red-green, no 3D perspective, ≤6–8 components. (Cloud loop owns quantum. No duplicating vol1–vol3 figures — the plain Bloch sphere is vol1; here it's the DECOHERENCE variant.)

---

## 1. qubit-teleportation  — send a state with an entangled pair and two classical bits  (MC · protocol · Critical)
*Source: chapter 05 — "Quantum Teleportation" · reel `vox-qubit-teleport`*

**PASTE:** Draw a blank three-wire circuit on a white background, three horizontal lines left to right. Top two lines belong to the left side, bottom line to the right side. Connect the middle and bottom lines at the far left with a wavy link (an entangled pair). Enclose the top two lines in a single measurement box partway across. From that box draw a double line (two parallel rails) travelling right and down to a correction box sitting on the bottom line. Mark the far-right end of the bottom line with a small filled state dot (the arrived state), and the far-left end of the top line with a matching open state dot (the original). Uniform strokes, flat fills, no shading, no labels — no text.
- [S] single-column 89mm, 300 DPI, vector, white bg, landscape.
- [C] Alice: unknown qubit + one half of an EPR pair, jointly Bell-measured → two classical bits; Bob: other EPR half + a correction conditioned on those bits → recovers the state. Double line = classical channel.
- [O] left→right circuit; entangled link at start; measurement → classical double-wire → correction.
- [P] flat vector, Okabe-Ito: qubit wires Blue #0072B2, entangled link Bluish Green #009E73, measurement box neutral gray, classical double-wire Orange #E69F00, correction box Sky Blue #56B4E9, arrived state Bluish Green #009E73. No baked text.
- [E] exclude: gate letters (H, X, Z), ket labels, bit values 0/1, a fourth wire, Bloch spheres.

**NEGATIVE:** gate letters, ket labels, bit values, fourth wire, Bloch spheres, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## 2. three-qubit-code  — one logical qubit hides in three, majority fixes a flip  (MC · process · Critical)
*Source: chapter 08 — "Quantum Error Correction" · reel `vox-fault-tolerance`*

**PASTE:** Draw a blank left-to-right error-correction schematic on a cream #F5F1E8 background: a single horizontal line on the left that fans out via two junction dots into three parallel horizontal lines (encoding). On the MIDDLE of the three lines place a small burst/star glyph (an error). Feed all three lines into a single comparator box on the right, from which a short corrective arrow points back at the errored middle line; then the three lines merge via two junctions back into one line at the far right (decoding). Uniform strokes, flat fills, no shading, no labels — no text.
- [S] single-column 89mm, 300 DPI, vector, cream #F5F1E8 bg, landscape.
- [C] encode one qubit into three; a single physical error strikes one line; a syndrome/majority comparison detects and flips it back; decode to the restored logical qubit.
- [O] fan-out → error → comparator + correction → fan-in; left→right.
- [P] flat vector, matte Claude palette: wires & junctions rust #C15F3C, error burst sage #A8C0B4, comparator box warm-gray #7A7368, correction arrow & restored line periwinkle #B5B4D6. Black #000000 outlines. No baked text. Flat matte, low saturation — no gradients, no gloss, no drop-shadows.
- [E] exclude: gate symbols, syndrome bit values, a 5- or 7-qubit variant, ancilla labels, more than three data lines.

**NEGATIVE:** gate symbols, syndrome values, extra qubit lines, ancilla labels, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## 3. decoherence-bloch  — the vector shrinks off the surface into the murk  (VG · reveal · Important)
*Source: chapter 07 — "Open Quantum Systems" · reels `vox-bloch-decoherence` / `vox-t2-ceiling`*

**PASTE:** Draw a blank Bloch-circle schematic on a cream #F5F1E8 background as a FLAT 2D diagram: a circle with two crossing axes through the centre. Draw one full-length arrow from the centre to a point ON the circle (a pure state). Then draw two or three progressively SHORTER arrows from the centre, each rotated a little and clearly stopping further inside the circle, spiralling toward the middle. Mark the exact centre with a small filled dot (the maximally mixed end state). Uniform strokes, flat fills, no shading, no labels — no text or symbols.
- [S] single-column 89mm, 300 DPI, vector, cream #F5F1E8 bg, square.
- [C] a pure qubit lives on the sphere surface; decoherence shrinks the Bloch vector inward over time toward the centre (maximally mixed) — the surface-to-centre collapse.
- [O] centred axes; one full surface vector; a sequence of shortening inward vectors; centre dot as the limit.
- [P] flat vector, matte Claude palette: circle & axes warm-gray #7A7368, full pure-state vector rust #C15F3C, shrinking vectors sage #A8C0B4, centre mixed dot periwinkle #B5B4D6. Black #000000 outlines. No baked text. Flat matte, low saturation — no gradients, no gloss, no drop-shadows.
- [E] exclude: θ/φ symbols, T1/T2 numerals, a rendered 3D globe, density-matrix entries, a second vector set.

**NEGATIVE:** angle symbols, relaxation-time numbers, shaded 3D globe, matrix entries, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## 4. bell-test-setup  — two distant choices, one shared source  (VG · structural · Important)
*Source: chapter 02 — "Entanglement and Bell Inequalities" · reel `vox-chsh-arithmetic`*

**PASTE:** Draw a blank Bell-test layout on a cream #F5F1E8 background: a small source glyph at the centre emitting one particle to the left and one to the right along a wavy shared link. At each end draw a detector box with a small two-position selector dial on top (a lever pointing to one of two marks). Beside each detector place two small outcome markers, one filled and one open (the ±1 results). Keep the layout left-right symmetric about the source. Uniform strokes, flat fills, no shading, no labels — no text.
- [S] single-column 89mm, 300 DPI, vector, cream #F5F1E8 bg, landscape.
- [C] central entangled source; left (Alice) and right (Bob) each choose one of two measurement settings (dial); each records a ±1 outcome; the correlation is the Bell/CHSH quantity.
- [O] symmetric left↔source↔right; two-position dials encode free settings; paired ± markers.
- [P] flat vector, matte Claude palette: source rust #C15F3C, shared link neutral gray wavy, detectors sage #A8C0B4, setting dials periwinkle #B5B4D6, outcome markers warm-gray #7A7368. Black #000000 outlines. No baked text. Flat matte, low saturation — no gradients, no gloss, no drop-shadows.
- [E] exclude: angle numbers, the CHSH inequality, probability tables, spin arrows, a third party.

**NEGATIVE:** setting angles, inequality formula, probability tables, spin arrows, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## 5. tensor-product-dimension  — two systems multiply, not add  (VG · structural · Supplementary)
*Source: chapter 01 — "Quantum States and Composite Systems" · reel `vox-tensor-product`*

**PASTE:** Draw a blank combination diagram on a cream #F5F1E8 background: on the left a short vertical column of two dots (system A); a small combine glyph (a circled dot / ⊗-style crossing) to its right; then another short vertical column of two dots (system B); an arrow leading to the right into a 2×2 grid of four dots (the product space), the grid's rows aligned to A's dots and columns to B's dots. Uniform strokes, flat fills, no shading, no labels — no text or numbers.
- [S] single-column 89mm, 300 DPI, vector, cream #F5F1E8 bg, landscape.
- [C] system A (2 states) combined with system B (2 states) yields a 4-state product space — every A-state paired with every B-state (the 2×2 grid), dimensions multiply.
- [O] A ⊗ B → grid; grid rows index A, columns index B; → progression.
- [P] flat vector, matte Claude palette: A dots rust #C15F3C, B dots sage #A8C0B4, combine glyph warm-gray #7A7368, product grid periwinkle #B5B4D6. Black #000000 outlines. No baked text. Flat matte, low saturation — no gradients, no gloss, no drop-shadows.
- [E] exclude: dimension numerals, basis kets, direct-sum comparison, a third system, matrix notation.

**NEGATIVE:** dimension numbers, basis kets, matrix notation, third system, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## 6. density-matrix-pure-vs-mixed  — a pure state is an outer product; mixed is a weighted average  (VG · comparison · Critical)
*Source: chapter 03 — "Density Matrices and Mixed States"*

**PASTE:** Draw two blank comparison panels on a cream #F5F1E8 background divided by a thin vertical rule. Each panel shows a small 2×2 grid (a matrix outline). LEFT panel (pure state): the off-diagonal cells are filled with the same dark shade as the diagonal cells — all four cells are equally emphasized, encoding a coherent outer product. RIGHT panel (mixed state): only the two diagonal cells are filled (dark shade); the two off-diagonal cells are empty/white — all coherence is gone. Identical grid sizes both panels. Uniform strokes, flat fills, no shading inside cells beyond filled/empty, no labels — no text or numbers.
- [S] single-column 89mm, 300 DPI, vector, cream #F5F1E8 bg, two equal panels.
- [C] left = pure-state density matrix ρ=|ψ⟩⟨ψ|: all four entries nonzero, coherences survive; right = mixed state: only diagonal entries (populations) survive, off-diagonals zero (decoherence eliminated them). The off-diagonal pattern is the signature.
- [O] mirrored two-panel; 2×2 matrix grids; filled-diagonal-only vs all-filled-cells is the contrast.
- [P] flat vector, matte Claude palette: matrix grid lines warm-gray #7A7368, filled cells Blue #0072B2 (pure), filled cells Orange #E69F00 (diagonal-only mixed), empty cells white. Black #000000 outlines. No baked text. Flat matte, low saturation — no gradients, no gloss, no drop-shadows.
- [E] exclude: matrix entry values, ρ² formula, eigenvalue markers, a 3×3 matrix, Bloch-sphere representation.

**NEGATIVE:** entry values, formula text, eigenvalue markers, 3×3 matrix, Bloch sphere, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## 7. quantum-circuit-basic  — gates act left to right, then measure  (VG · structural · Important)
*Source: chapter 04 — "Quantum Circuits and Algorithms"*

**PASTE:** Draw a blank two-wire quantum circuit on a cream #F5F1E8 background: two horizontal lines left to right (the qubits). On the top wire place one small square (a single-qubit gate). Spanning both wires, place one CNOT gate symbol (a large dot on the top wire connected by a vertical line to a circled plus on the bottom wire). At the far right of each wire place a measurement box (a rectangle with a small internal meter dial). Uniform strokes, flat fills, no shading, no labels — no text or gate letters.
- [S] single-column 89mm, 300 DPI, vector, cream #F5F1E8 bg, landscape.
- [C] two-qubit circuit: single-qubit gate (top wire) → CNOT entangling gate (control top, target bottom) → measurement of both. This is the minimal circuit that creates and measures an entangled pair.
- [O] left→right on two horizontal wires; single-qubit gate; CNOT gate straddling both wires; meter boxes at the right.
- [P] flat vector, matte Claude palette: wires warm-gray #7A7368, single-qubit gate rust #C15F3C, CNOT control dot sage #A8C0B4, CNOT target circle periwinkle #B5B4D6, measurement boxes warm-gray #7A7368. Black #000000 outlines. No baked text. Flat matte, low saturation — no gradients, no gloss, no drop-shadows.
- [E] exclude: gate letter labels (H, X, Z), ket state notation, measurement outcome bits, a third qubit wire, classical-feedback lines.

**NEGATIVE:** gate letters, ket notation, bit outcomes, third wire, classical feedback, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## 8. dense-coding-protocol  — two classical bits sent per one shared qubit  (MC · sequence · Supplementary)
*Source: chapter 06 — "Quantum Communication"*

**PASTE:** Draw a blank left-to-right protocol schematic on a white background: two horizontal actor rows (Alice top, Bob bottom), connected at the left by a wavy shared entangled link. Above Alice's row, a small 2×2 choice grid (four small squares, each with a different fill pattern — representing four possible messages). Alice's row feeds into one small box (her gate operation). The shared link from that box travels right to Bob's row, which feeds into a Bell-measurement box at the right end. From the measurement box, two short downward output lines (two classical bits decoded). Uniform strokes, flat fills, no shading, no labels — no text.
- [S] single-column 89mm, 300 DPI, vector, white bg, landscape.
- [C] Alice and Bob share an EPR pair; Alice applies one of four gate operations (encoding 2 classical bits) on her half; she sends her qubit to Bob; Bob performs a Bell measurement and reads off the 2 bits. Two classical bits transmitted using one quantum channel transmission.
- [O] two actor rows; shared entangled link on left; Alice's operation box; qubit travels to Bob's Bell-measurement box; two decoded-bit lines exit right.
- [P] flat vector, Okabe-Ito: entangled link Bluish Green #009E73, choice grid Orange #E69F00, Alice's gate box Blue #0072B2, qubit travel arrow neutral gray, Bell-measurement box Sky Blue #56B4E9, decoded-bit lines Vermillion #D55E00. No baked text.
- [E] exclude: gate letters, ket states, bit-value labels, a third actor, classical pre-sharing details.

**NEGATIVE:** gate letters, ket states, bit labels, third actor, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## Video candidates

FIGURE qubit-teleportation — Status: STATIC SUFFICIENT · Criterion: — · Reason: the mechanism is fully carried by arrow direction and shape arrangement in one frame; motion would not add information a careful static figure does not already hold.
FIGURE three-qubit-code — Status: STATIC SUFFICIENT · Criterion: — · Reason: the mechanism is fully carried by arrow direction and shape arrangement in one frame; motion would not add information a careful static figure does not already hold.
FIGURE decoherence-bloch — Status: STATIC SUFFICIENT · Criterion: — · Reason: the mechanism is fully carried by arrow direction and shape arrangement in one frame; motion would not add information a careful static figure does not already hold.
FIGURE bell-test-setup — Status: STATIC SUFFICIENT · Criterion: — · Reason: the figure is a spatial cross-section or structural schematic whose value lies in inspecting all parts simultaneously.
FIGURE tensor-product-dimension — Status: STATIC SUFFICIENT · Criterion: — · Reason: the figure is a spatial cross-section or structural schematic whose value lies in inspecting all parts simultaneously.
FIGURE density-matrix-pure-vs-mixed — Status: STATIC SUFFICIENT · Criterion: — · Reason: the figure is a simultaneous comparison of two or more states; motion would replace side-by-side display with a sequence that the chapter does not assert.
FIGURE quantum-circuit-basic — Status: STATIC SUFFICIENT · Criterion: — · Reason: the figure is a spatial cross-section or structural schematic whose value lies in inspecting all parts simultaneously.
FIGURE dense-coding-protocol — Status: STATIC SUFFICIENT · Criterion: — · Reason: the mechanism is fully carried by arrow direction and shape arrangement in one frame; motion would not add information a careful static figure does not already hold.

**Chapter recommendation:** None — no entry in this file clears the motion bar; static figures serve every concept here.
