# CAJAL figure candidates — phys-5125-qm (previz track)

Graduate QM course volume (Prof. Feiguin's PHYS 5125 lecture notes). 7 scannable chapters: Formalism → Hydrogen Atom → Time-Independent Perturbation Theory → Time-Dependent Perturbation Theory → Identical Particles → Variational Method → Fine/Hyperfine Structure. Mechanism figures mined chapter-by-chapter. Blank unannotated vector — no baked text; previz owns every symbol. Okabe-Ito, white bg, 1pt strokes, no red-green, no 3D perspective, ≤6–8 components.

De-confliction: figures already in vol1–vol5 / companion are NOT re-listed. This book's figures are the advanced/graduate-level mechanisms not present there.

---

## 1. hydrogen-series-power-series-cutoff  — the series diverges unless it terminates  (MC · structural · Critical)
*Source: chapter 02 — "The Hydrogen Atom"*

**PASTE:** Draw a blank flowchart on a white background, left to right. Start with a small wavy power-series symbol (an infinite stack of short horizontal bars suggesting many terms). A branching diamond splits it into two paths: TOP path (series does NOT terminate): an arrow leads to a growing/diverging staircase shape (bars getting larger and larger, representing e^ρ growth). BOTTOM path (series DOES terminate): an arrow leads to a small finite stack of three short bars (a polynomial, finite). At the end of the bottom path, a small checkmark glyph; at the end of the top path, a small strike/cross. Connect the two end states with a vertical bracket labeled neither — just the two outcomes. Uniform strokes, flat fills, no shading, no labels — no text.
- [S] single-column 89mm, 300 DPI, vector, white bg, landscape.
- [C] the power-series solution to the hydrogen radial equation has a ratio c_{k+1}/c_k → 1/k at large k — same as e^ρ, which diverges. The series must terminate (become a polynomial) to keep the wavefunction normalizable. Termination forces discrete energies.
- [O] power series → diamond branch → diverging path (struck) vs terminating path (checked); left→right.
- [P] flat vector, Okabe-Ito: power series bars neutral gray, branch diamond Blue #0072B2, diverging bars Vermillion #D55E00, terminating bars Bluish Green #009E73, strike/check neutral gray. No baked text.
- [E] exclude: recurrence relation formula, energy-level numbers, the ratio c_{k+1}/c_k explicitly, a second branch.

**NEGATIVE:** recurrence formula, energy numbers, ratio text, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## 2. hydrogen-energy-degeneracy  — n fixes the energy; ℓ and m do not  (VG · level diagram · Critical)
*Source: chapter 02 — "The Hydrogen Atom"*

**PASTE:** Draw a blank energy-level diagram on a white background with three levels stacked vertically (n=1, n=2, n=3 from bottom to top). For each level draw a horizontal bar. For the n=1 bar: just one bar (no split — one state). For the n=2 bar: the single bar has four closely stacked sub-bars beside it (four degenerate states, the same energy). For the n=3 bar: the single bar has nine closely stacked sub-bars (nine degenerate states). Mark the degenerate sub-bars as equal-height clusters beside the main bar. Uniform strokes, flat fills, no shading, no labels — no text or numbers.
- [S] single-column 89mm, 300 DPI, vector, white bg, portrait.
- [C] hydrogen energy depends ONLY on n: E_n = −13.6/n² eV. For n=1: one state (ℓ=0, m=0). For n=2: four states (ℓ=0 + ℓ=1 with m=−1,0,+1). For n=3: nine states. Degeneracy grows as n². The sub-bar clusters make this visual.
- [O] vertical energy axis; three levels; sub-state clusters grow upward; equal-height clusters encode degeneracy.
- [P] flat vector, Okabe-Ito: n=1 bar Blue #0072B2, n=2 bars Orange #E69F00, n=3 bars Bluish Green #009E73, degenerate sub-bars same color slightly offset. No baked text.
- [E] exclude: energy values in eV, ℓ/m quantum-number labels, fine-structure splitting, a fourth level.

**NEGATIVE:** energy numbers, quantum-number labels, fine structure, fourth level, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## 3. perturbation-degenerate-subspace  — inside the degenerate manifold, first rotate before dividing  (MC · process · Critical)
*Source: chapter 03 — "Time-Independent Perturbation Theory"*

**PASTE:** Draw a blank three-step flowchart on a white background, top to bottom. STEP 1: a horizontal bar labeled "degenerate subspace" (a cluster of equal-height bars at the same level). STEP 2: below it, a rotated version of the same cluster — the bars are now spread at slight angles from vertical, suggesting a rotation inside the subspace (basis change). STEP 3: the spread bars now have slight differences in height (diagonal in the new basis) — with short arrows showing each bar has shifted to a distinct height. Connect steps with downward single arrows. Uniform strokes, flat fills, no shading, no labels — no text.
- [S] single-column 89mm, 300 DPI, vector, white bg, portrait.
- [C] degenerate perturbation theory: inside the degenerate subspace the standard formula blows up (energy denominators → 0). Fix: rotate to the basis that diagonalizes V in that subspace FIRST; then the off-diagonal couplings vanish and the denominators stay finite. The three steps are: identify the manifold → rotate (diagonalize V) → read off split levels.
- [O] top-to-bottom three steps: cluster → rotated cluster → spread-height bars; downward arrows.
- [P] flat vector, Okabe-Ito: degenerate bars Blue #0072B2 (step 1), rotated bars Sky Blue #56B4E9 (step 2), split bars Bluish Green #009E73 (step 3, distinct heights). No baked text.
- [E] exclude: V matrix entries, energy denominator formula, Stark-effect energy values, a non-degenerate comparison panel.

**NEGATIVE:** V matrix, energy denominator formula, Stark values, non-degenerate comparison, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## 4. sudden-vs-adiabatic-approximation  — fast change freezes the state; slow change rides the eigenstate  (MC · comparison · Critical)
*Source: chapter 04 — "Time-Dependent Perturbation Theory"*

**PASTE:** Draw two blank comparison panels on a white background divided by a thin vertical rule. Each panel shows a horizontal axis (time) and a curved potential-well schematic that changes shape from left to right along the axis (the Hamiltonian evolves). LEFT panel (sudden): the well shape changes abruptly (a sharp vertical step in the shape change); the state wavefunction (a curve inside the well) remains the same shape as before the change — frozen. RIGHT panel (adiabatic): the well shape changes gradually (a smooth slope across the panel); the state wavefunction inside the well tracks the evolving well shape smoothly, staying in the instantaneous ground state. Uniform strokes, flat fills, no shading, no labels — no text.
- [S] single-column 89mm, 300 DPI, vector, white bg, two equal panels.
- [C] left = sudden approximation: Hamiltonian changes faster than the state can respond → state is "frozen" in the old eigenstate, re-read in the new basis. Right = adiabatic: Hamiltonian changes slowly → state tracks the evolving eigenstate (with a geometric Berry phase, not shown). The clock rate relative to ω_mn is the deciding factor.
- [O] mirrored two-panel; time axis; well shape change abrupt (left) vs gradual (right); state frozen vs tracking.
- [P] flat vector, Okabe-Ito: potential wells neutral gray, abrupt change step Vermillion #D55E00, frozen state Blue #0072B2, gradual change slope Orange #E69F00, tracking state Bluish Green #009E73. No baked text.
- [E] exclude: time scale numbers, Berry phase annotation, transition probability formula, a resonant-driving comparison.

**NEGATIVE:** time scale numbers, Berry phase, probability formula, resonance comparison, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## 5. slater-determinant-structure  — rows are particles, columns are states, swap swaps rows  (VG · structural · Important)
*Source: chapter 05 — "Identical Particles"*

**PASTE:** Draw a blank 3×3 grid (a matrix outline) on a white background, with one row and one column clearly highlighted. The grid has three rows (particles 1, 2, 3) and three columns (single-particle states a, b, c). Each cell holds a small dot (an orbital assignment). Draw a curved double-headed arrow connecting row 1 to row 2 on the left side of the grid, indicating a particle-swap operation. Below the matrix draw a small minus-sign marker (the antisymmetry sign change from swapping two rows). Uniform strokes, flat fills, no shading, no labels — no text or letters.
- [S] single-column 89mm, 300 DPI, vector, white bg, square.
- [C] Slater determinant: rows = particles (1,2,3), columns = orbitals (a,b,c); swapping two particles = swapping two rows → determinant picks up a minus sign (antisymmetry automatically encoded). The structure is the geometry of the antisymmetry principle.
- [O] 3×3 grid; row-swap arrow on left; minus-sign marker below; dots in cells.
- [P] flat vector, Okabe-Ito: grid lines neutral gray, dot-filled cells Blue #0072B2, row-swap arrow Orange #E69F00, minus marker Vermillion #D55E00. No baked text.
- [E] exclude: orbital letter labels, determinant formula, particle-index numbers, Pauli exclusion proof, a 2×2 matrix.

**NEGATIVE:** orbital labels, determinant formula, index numbers, exclusion proof, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## 6. variational-upper-bound  — every trial state gives an energy above the ground state  (VG · structural · Important)
*Source: chapter 06 — "The Variational Method"*

**PASTE:** Draw a blank diagram on a white background: a horizontal line at the bottom (the true ground-state energy). Above it, draw three separate horizontal tick marks at varying heights — each one higher than the bottom line (the three are variational energies for three different trial states). From each tick mark draw a short downward arrow toward the bottom line. The bottom line is clearly lower than all three tick marks. Uniform strokes, flat fills, no shading, no labels — no text or numbers.
- [S] single-column 89mm, 300 DPI, vector, white bg, square.
- [C] variational principle: for ANY normalized trial state |ψ_trial⟩, the expectation value ⟨H⟩ ≥ E₀ (the true ground-state energy). Every trial gives an upper bound. Minimizing over trial parameters drives the bound down toward E₀.
- [O] bottom line = E₀; three tick marks above at different heights = three trial energies; downward arrows = bounding direction.
- [P] flat vector, Okabe-Ito: ground-state line Blue #0072B2, three trial-energy ticks Orange #E69F00, downward arrows Bluish Green #009E73. No baked text.
- [E] exclude: energy numbers, parameter labels, helium atom context, wavefunction trial shape, the variational formula.

**NEGATIVE:** energy numbers, parameter labels, helium context, formula text, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## 7. hyperfine-splitting  — two electron-proton spin couplings, one triplet and one singlet  (VG · level diagram · Important)
*Source: chapter 07 — "Fine and Hyperfine Structure"*

**PASTE:** Draw a blank energy-level diagram on a white background: a single horizontal bar on the left (the unperturbed 1s level). A dashed vertical dividing line. On the right: two levels — an UPPER bar with three closely spaced sub-bars beside it (the triplet, F=1, three degenerate states) and a LOWER bar separated by a larger gap (the singlet, F=0, one state). A small downward bracket with a gap marker between the two levels indicates the hyperfine splitting. Uniform strokes, flat fills, no shading, no labels — no text or numbers.
- [S] single-column 89mm, 300 DPI, vector, white bg, landscape.
- [C] hydrogen 1s level: adding the proton spin (I=1/2) to the electron spin (S=1/2) gives total spin F=S+I; F=1 is the triplet (three m_F states, upper level) and F=0 is the singlet (lower level). The triplet-singlet gap is the 21-cm hyperfine transition.
- [O] left: single unperturbed bar; right: upper triplet (three sub-bars) + lower singlet (one bar); gap bracket between them.
- [P] flat vector, Okabe-Ito: unperturbed bar neutral gray, triplet upper bars Bluish Green #009E73, singlet lower bar Blue #0072B2, gap bracket Orange #E69F00. No baked text.
- [E] exclude: F quantum-number labels, 21-cm wavelength numerals, magnetic-field splitting, Landé g-factor, spin-orbit comparison.

**NEGATIVE:** F labels, 21-cm numbers, magnetic splitting, g-factor, spin-orbit, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## Video candidates

FIGURE hydrogen-series-power-series-cutoff — Status: STATIC SUFFICIENT · Criterion: — · Reason: the figure is a spatial cross-section or structural schematic whose value lies in inspecting all parts simultaneously.
FIGURE hydrogen-energy-degeneracy — Status: STATIC SUFFICIENT · Criterion: — · Reason: the mechanism is fully carried by arrow direction and shape arrangement in one frame; motion would not add information a careful static figure does not already hold.
FIGURE perturbation-degenerate-subspace — Status: STATIC SUFFICIENT · Criterion: — · Reason: the mechanism is fully carried by arrow direction and shape arrangement in one frame; motion would not add information a careful static figure does not already hold.
FIGURE sudden-vs-adiabatic-approximation — Status: STATIC SUFFICIENT · Criterion: — · Reason: the figure is a simultaneous comparison of two or more states; motion would replace side-by-side display with a sequence that the chapter does not assert.
FIGURE slater-determinant-structure — Status: STATIC SUFFICIENT · Criterion: — · Reason: the figure is a spatial cross-section or structural schematic whose value lies in inspecting all parts simultaneously.
FIGURE variational-upper-bound — Status: STATIC SUFFICIENT · Criterion: — · Reason: the figure is a spatial cross-section or structural schematic whose value lies in inspecting all parts simultaneously.
FIGURE hyperfine-splitting — Status: STATIC SUFFICIENT · Criterion: — · Reason: the mechanism is fully carried by arrow direction and shape arrangement in one frame; motion would not add information a careful static figure does not already hold.

**Chapter recommendation:** None — no entry in this file clears the motion bar; static figures serve every concept here.
