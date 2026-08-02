# Quantum Mechanics Vol. 2 — CLI Video Ideas ("X with Claude")

## Candidate 01 — "Build the Multi-Electron Atom Simulator: Aufbau Principle with Claude Code" (Capstone)
- Source: quantum-mechanics-vol2/chapters/11-capstone-the-atom.md
- Lane: BUILD (Claude Code)
- Hook: The periodic table is built on Hund's rules and the Aufbau principle. Claude Code can simulate orbital filling for any element and predict electron configurations — then validate against NIST data.
- The artifact: A Manim animation showing orbital energy levels appearing (1s, 2s, 2p, 3s, 3p, 3d, 4s…) as a ladder on the left, then electrons filling in one by one according to Aufbau + Hund's rules, with the occupied orbitals lighting up as each electron is added.
- Prompt seed: `claude "Write a Python script that simulates the Aufbau principle for elements Z=1 to 36 (H to Kr): (1) define orbital energies using Slater's rules (Z_eff = Z - sigma) and E_nl = -13.6 eV * Z_eff^2 / n^2; (2) fill orbitals in energy order respecting Pauli exclusion and Hund's first rule (maximize spin); (3) output the electron configuration and term symbol (S, L, J) for each element; (4) compare predicted vs. NIST actual configurations for the 5 anomalous cases (Cr, Cu, Nb, Mo, Ag). Print anomaly table."`
- Read / check: Carbon should be [He]2s²2p² with term ³P₀. Iron should be [Ar]3d⁶4s² with term ⁵D₄. Chromium (anomaly: [Ar]3d⁵4s¹ instead of 3d⁴4s²) should be identified. Verify Slater's rule groupings: [ns,np] together, [nd] separate, with correct shielding coefficients (0.35 for same group, 0.85 for one shell inside, 1.0 for two+ shells inside).
- Human supplies: Nothing — NIST electron configurations are public (physics.nist.gov/PhysRefData).
- Output medium: Manim (animated orbital filling — electrons (arrows for spin) appearing in orbitals, configuration notation updating, anomalous cases highlighted in orange)
- The change: Add Z_eff vs Z plot — showing how Z_eff grows more slowly than Z due to screening, with s and p electrons more screened than d electrons.
- Teardown angle: Slater's rules predict 31 of 36 configurations correctly for H through Kr. The 5 anomalies (Cr, Cu, etc.) reveal where exchange energy exceeds the energy cost of the 3d→4s promotion — the model's breakdown is instructive, not a failure.
- Exclusions: Relativistic effects in heavy atoms, Hartree-Fock self-consistency, Kohn-Sham DFT.
- Score: 9/10

## Candidate 02 — "Visualize the Hydrogen Atom: Radial Probability Densities with Claude Code"
- Source: quantum-mechanics-vol2/chapters/09-the-hydrogen-atom.md
- Lane: BUILD (Claude Code)
- Hook: The most probable radius for a hydrogen electron in the ground state is not the Bohr radius — it is a₀. But the average radius ⟨r⟩ = 1.5a₀. Claude Code computes both and plots the radial probability density.
- The artifact: A Manim animation of R_{nl}(r)²r² for the first six hydrogen orbitals (1s, 2s, 2p, 3s, 3p, 3d) — each curve drawing from left to right in a new color, with a₀ marked as a vertical reference and both r_peak and ⟨r⟩ labeled for the 1s state.
- Prompt seed: `claude "Write a Python script that computes and plots the hydrogen radial probability density P_nl(r) = |R_nl(r)|^2 * r^2 for n=1,2,3 and all allowed l values. Use the analytic hydrogen wave functions with scipy.special.genlaguerre and exp(-r/n*a0) factors. For the 1s state: compute r_peak (where dP/dr=0), mean radius <r> = integral r*P_1s dr, and verify <r> = 1.5*a0. Plot all 6 curves on one figure with Bohr radius marked."`
- Read / check: 1s peak at r=a₀, ⟨r⟩1s = 1.5a₀. 2s has two peaks (inner and outer); outer peak near 5a₀. 3d has single peak near 9a₀. All curves should be zero at r=0 and r=∞, normalized to 1 when integrated. Verify the normalization integral for each curve is 1.0 ± 0.01.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim (six curves appearing one by one in sequence n=1→2→3 within each n, a₀ vertical reference line, labeled peaks for 1s)
- The change: Plot the 3D probability density |ψ_{nlm}|² = |R_{nl}|²|Y_l^m|² as a 2D color map in the xz plane for the 2p_z orbital — showing the dumbbell shape.
- Teardown angle: The most probable radius ≠ average radius is the lesson that students consistently confuse. For the 1s state r_peak = a₀, ⟨r⟩ = 1.5a₀ — the distribution is skewed because r² dr grows for larger r. The plot makes this visual without algebra.
- Exclusions: Fine structure derivation, Lamb shift, reduced mass correction.
- Score: 9/10

## Candidate 03 — "Rotate a Qubit: Bloch Sphere and SU(2) with Claude Code"
- Source: quantum-mechanics-vol2/chapters/07-spin-and-the-bloch-sphere.md
- Lane: BUILD (Claude Code)
- Hook: A spin-1/2 particle precessing in a magnetic field traces a circle on the Bloch sphere. Claude Code animates the Larmor precession and shows why you can never distinguish spin-1/2 from spin-1/2 by observation alone.
- The artifact: A Manim animation of the Bloch sphere with the Bloch vector precessing around the z-axis at the Larmor frequency ω₀ = γB₀ — the vector tracing a circular path on the sphere surface, the precession angle updating in the corner.
- Prompt seed: `claude "Write a Python script that simulates Larmor precession of a spin-1/2 particle in a magnetic field B=1T along z: (1) initial state |+x> = (|0>+|1>)/sqrt(2), Bloch vector at (1,0,0); (2) time evolution under H = -gamma*B*sigma_z/2 gives: r_x(t) = cos(omega_0*t), r_y(t) = sin(omega_0*t), r_z(t) = 0 where omega_0 = gamma*B (proton gamma = 2.675e8 rad/s/T); (3) animate the Bloch vector precessing on a 3D wireframe sphere for 200 steps covering one full cycle."`
- Read / check: Larmor frequency ω₀ = γ*B = 2.675e8 rad/s for proton in 1T field. Full precession period T = 2π/ω₀ ≈ 23.5 ns. Bloch vector magnitude should remain 1.0 throughout (pure state). Verify r_x(T) = r_x(0) = 1 (full cycle returns to start). This is the basis of NMR/MRI.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim (3D wireframe Bloch sphere, Bloch vector animating as a red arrow tracing the precession circle, frequency and period labeled)
- The change: Add a transverse magnetic field (rotating frame — the spin-flip pulse) and show the Bloch vector tipping from north pole toward the equator — the NMR π/2 pulse.
- Teardown angle: Larmor precession in the Bloch sphere picture is the basis of MRI. The rotating frame transform turns the oscillating field into a DC field — making spin flips analyzable as simple rotations. The teardown connects the abstract formalism to a technology everyone has encountered.
- Exclusions: Spin echo, T1/T2 relaxation, gradient fields in MRI.
- Score: 8/10

## Candidate 04 — "Compute Angular Momentum Addition: Clebsch-Gordan Coefficients with Claude Code"
- Source: quantum-mechanics-vol2/chapters/08-addition-of-angular-momenta.md
- Lane: BUILD (Claude Code)
- Hook: Two spin-1/2 particles combine into a triplet (spin-1) or singlet (spin-0). The Clebsch-Gordan decomposition is the calculation behind atomic spectroscopy, nuclear physics, and quantum computing.
- The artifact: A Manim animation of the angular momentum addition — two spin-1/2 arrows on the left combining into either three triplet states |1,m⟩ (m=-1,0,+1) or the singlet |0,0⟩ on the right. The Clebsch-Gordan coefficients (1/√2) appear as labels on the transition arrows.
- Prompt seed: `claude "Write a Python script that computes Clebsch-Gordan coefficients for j1=1/2, j2=1/2 using the ladder operator method: (1) start with |j1=1/2,m1=1/2> x |j2=1/2,m2=1/2> = |J=1,M=1>; (2) apply J_- to both sides to get |J=1,M=0>; (3) find |J=0,M=0> as the orthogonal combination; (4) print all 4 CG coefficients as fractions; (5) verify the decomposition using the sympy.physics.quantum.cg module for comparison."`
- Read / check: |1,0⟩ = (|↑↓⟩ + |↓↑⟩)/√2 (coefficient 1/√2). |0,0⟩ = (|↑↓⟩ - |↓↑⟩)/√2 (coefficient ±1/√2). All 4 CG coefficients should match sympy output. Verify orthogonality: ⟨1,0|0,0⟩ = 0.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim (animated decomposition diagram — two spin-1/2 arrows combining, output states appearing with CG coefficient labels, singlet state labeled "antisymmetric")
- The change: Extend to j1=1, j2=1/2 (spin-1 plus spin-1/2 → spin-3/2 or spin-1/2) and print the full 6-coefficient table.
- Teardown angle: The singlet state (|↑↓⟩ - |↓↑⟩)/√2 is the famous EPR-Bell state — antisymmetric under particle exchange, the source of perfect spin anticorrelation. The Clebsch-Gordan calculation shows exactly where the antisymmetry comes from.
- Exclusions: 3j symbols, 6j symbols, Racah algebra, coupling schemes in heavy nuclei.
- Score: 8/10

## Candidate 05 — "Simulate Identical Particles: Bosons vs. Fermions Bunching with Claude Code"
- Source: quantum-mechanics-vol2/chapters/10-identical-particles.md
- Lane: BUILD (Claude Code)
- Hook: Two identical bosons bunch — they prefer to be in the same state. Two identical fermions cannot. Claude Code simulates both and plots the arrival probability at a beam splitter.
- The artifact: A Manim animation of the Hong-Ou-Mandel effect — two particles entering a 50/50 beam splitter, with probability bars for the four outcomes (both transmitted, both reflected, one each) for: distinguishable, bosons, and fermions. The boson bunching (zero probability for one-each) animates to zero.
- Prompt seed: `claude "Write a Python script simulating a 50/50 beam splitter for two identical particles. Compute the probability of each outcome (both go to output A, both go to B, one each) for: (1) distinguishable particles (each 25/25/50%); (2) identical bosons — symmetric state shows HOM bunching (50/50/0%); (3) identical fermions — antisymmetric state shows antibunching (25/25/50% but different phase). Use the quantum amplitudes: bosons add, fermions subtract. Print probabilities and verify they sum to 1."`
- Read / check: Distinguishable: P(AA)=0.25, P(BB)=0.25, P(AB)=0.5. Bosons (HOM effect): P(AA)=0.5, P(BB)=0.5, P(AB)=0. Fermions: same as distinguishable (for this specific setup — fermions "anti-bunch" into different outputs). Verify using |T|² = (1/√2)² = 0.5 for each beam splitter path. Sum to 1 for each case.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim (animated probability bar chart — three outcome bars for each particle type appearing in sequence, HOM bunching effect showing AB bar dropping to zero)
- The change: Vary the beam splitter transmission from 0 to 1 and plot P(both same output) vs. T for bosons — showing the maximum bunching at T=0.5.
- Teardown angle: The Hong-Ou-Mandel effect (bosons bunch at a beam splitter) is the experimental signature used to verify photon indistinguishability in quantum optics experiments and is a key benchmark for photonic quantum computers.
- Exclusions: Fock space, second quantization, many-body entanglement.
- Score: 8/10

## Candidate 06 — "Derive and Plot Hydrogen Fine Structure with First-Order Perturbation Theory"
- Source: quantum-mechanics-vol2/chapters/09-the-hydrogen-atom.md
- Lane: BUILD (Claude Code)
- Hook: The hydrogen spectrum splits into fine structure doublets. First-order perturbation theory gives the splitting exactly — and Claude Code can compute and animate the splitting for all n=2 states.
- The artifact: A Manim animation showing the n=2 energy levels splitting into fine structure components as a perturbation parameter is dialed from 0 to its physical value: 2s₁/₂ and 2p₁/₂ remaining degenerate (to this order), 2p₃/₂ splitting upward.
- Prompt seed: `claude "Write a Python script that computes the fine-structure energy corrections to hydrogen for n=2 using first-order perturbation theory. The correction is E_nl_j = -13.6 eV * alpha^2/(n^3) * (1/(j+0.5) - 3/(4n)) where alpha=1/137 (fine structure constant). Compute E for all n=2 states: 2s_1/2, 2p_1/2, 2p_3/2. Print the corrections in MHz (divide by h) and plot an energy level diagram showing the splitting."`
- Read / check: 2p₃/₂ should be higher than 2p₁/₂ by ~10.9 GHz (the Lamb shift is not included — pure fine structure). 2s₁/₂ and 2p₁/₂ should be degenerate to this order. Verify alpha=1/137.036. The corrections should be of order alpha²*13.6 eV ≈ 7.2×10⁻⁴ eV.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim (energy level diagram — n=2 level appearing, then splitting into fine structure components as alpha²/n³ correction is applied, gap labeled in GHz)
- The change: Add the Lamb shift correction (2s₁/₂ raised above 2p₁/₂ by 1.058 GHz — famous Lamb 1947 result) and show how the degeneracy is broken.
- Teardown angle: The fine structure is α² times smaller than the Bohr energies. The Lamb shift is another factor of α smaller — but its measurement in 1947 disproved the Dirac equation's prediction and launched quantum electrodynamics. Three orders of magnitude of refinement led to the most precisely tested theory in physics.
- Exclusions: Hyperfine structure, QED loop corrections, muonic hydrogen.
- Score: 7/10
