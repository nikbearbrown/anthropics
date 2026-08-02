# Simulation Ideas — quantum-mechanics-vol2

Medhavy-register "Claude Code + Manim" workflow reels.

---

## Sim-01 — Bloch Sphere: Qubit State and Single-Axis Rotation
- Source: `quantum-mechanics-vol2/chapters/07-spin-and-the-bloch-sphere.md`
- Topic: CLAUDE CODE · MANIM
- Physical rule: |ψ⟩ = cos(θ/2)|↑⟩ + e^(iφ)sin(θ/2)|↓⟩; Bloch vector (sin θ cos φ, sin θ sin φ, cos θ)
- Concrete numbers: |↑⟩ → north pole; |+⟩=(|↑⟩+|↓⟩)/√2 → equator at φ=0; Hadamard maps |↑⟩ to |+⟩ (rotation by π about (x+z)/√2)
- Visual artifact: 3D sphere with labeled poles (|↑⟩, |↓⟩, |+⟩, |−⟩); Bloch vector rotating continuously from pole to equator
- Two testable predictions: P1: |↑⟩ at north pole (θ=0) → measurement outcome ↑ with probability 1; P2: equatorial state (θ=π/2) → ⟨Z⟩=0 (equal superposition)
- Sim slug: medhavy-vol2-bloch-rotation

---

## Sim-02 — Commutators and Uncertainty: Squeezing One Width Stretches the Other
- Source: `quantum-mechanics-vol2/chapters/03-commutators-and-uncertainty.md`
- Topic: CLAUDE CODE · MANIM
- Physical rule: σ_x σ_p ≥ ℏ/2; for Gaussian state σ_x σ_p = ℏ/2 (minimum uncertainty)
- Concrete numbers: Gaussian state σ_x = 1 nm → σ_p = ℏ/2/(1 nm) ≈ 5.27×10⁻²⁶ kg·m/s ≈ 0.33 eV/c; squeeze σ_x to 0.5 nm → σ_p doubles
- Visual artifact: two coupled width bars for x and p; dragging one bar in forces the other to expand; product ℏ/2 stays constant
- Two testable predictions: P1: Gaussian ground state of harmonic oscillator saturates the bound (σ_x σ_p = ℏ/2 exactly); P2: squeezing σ_x by factor 2 doubles σ_p
- Sim slug: medhavy-vol2-uncertainty-squeeze

---

## Sim-03 — Hydrogen Radial Probability: Why 1s Mean ≠ Mode
- Source: `quantum-mechanics-vol2/chapters/09-the-hydrogen-atom.md`
- Topic: CLAUDE CODE · MANIM
- Physical rule: P(r) = |R₁₀(r)|² · 4πr² = (4/a₀³) r² e^(−2r/a₀); peak at r=a₀, mean at 3a₀/2
- Concrete numbers: Bohr radius a₀ = 0.0529 nm; peak of P(r) at a₀; ⟨r⟩ = 3a₀/2 = 0.0794 nm
- Visual artifact: P(r) curve with two vertical markers — peak at a₀ (green), mean at 1.5 a₀ (orange); the gap between them is visible
- Two testable predictions: P1: P(r) peaks exactly at a₀ (differentiate P'(r)=0 → r=a₀); P2: ⟨r⟩ = 3a₀/2 from the integral (larger than peak)
- Sim slug: medhavy-vol2-hydrogen-radial
- Note: CROSS-REFERENCE — vox-hydrogen-cloud is an explainer in quantum-mechanics-a-companion-guide. This is the simulation workflow reel; build it.

---

## Sim-04 — Capstone: Atomic Orbital Builder (Screening + Energy Ordering)
- Source: `quantum-mechanics-vol2/chapters/11-capstone-the-atom.md`
- Topic: CLAUDE CODE · MANIM
- Physical rule: E(nl) depends on both n and l through screening; E(ns) < E(np) < E(nd) for multi-electron atoms; Z_eff from Slater's rules
- Concrete numbers: Na (Z=11): 3s at −5.1 eV, 3p at −3.0 eV; gap ≈ 2.1 eV; Slater Z_eff(3s)≈6.6, Z_eff(3p)≈6.1
- Visual artifact: energy level diagram with l-split shells; change Z and watch Z_eff shift; compare hydrogen (no l-split) vs sodium (clear l-split)
- Two testable predictions: P1: hydrogen n=3 shows 3s=3p=3d all degenerate (SO(4) symmetry); P2: sodium n=3 splits: E(3s) < E(3p) < E(3d) by measurable gaps
- Sim slug: medhavy-vol2-orbital-energies

---

## Candidate 01 — Animate: Wavepacket Spreading and Free-Particle Dispersion
- Source: `quantum-mechanics-vol2/chapters/04-quantum-dynamics-and-the-pictures.md`
- Topic: Free-particle wavepacket spreading
- Lane: MANIM (directed animation)
- Hook: A quantum particle launched with a sharp position immediately starts to smear — momentum uncertainty is irresistibly real and visible, not just a formula.
- The rule: Gaussian wavepacket ψ(x,t) under H = p²/2m; σ_x(t) = σ_0 √(1 + (ℏt/2mσ_0²)²). Each momentum component e^{ikx} acquires phase e^{-iℏk²t/2m}, causing dephasing and broadening.
- Concrete numbers: electron (m = 9.11×10⁻³¹ kg), σ_0 = 1 nm initial width; spreading time τ = 2mσ_0²/ℏ ≈ 17 fs; at t = τ, σ_x = σ_0 √2 ≈ 1.41 nm; at t = 5τ, σ_x ≈ 5.1 nm. Use ħ=1 units: m=1, σ_0=1, show t from 0 to 10.
- The artifact / what moves: a bright Gaussian envelope |ψ(x,t)|² spreading smoothly leftward and rightward in real time — the peak height drops as the wings grow, area constant (normalization held). Color-code phase angle.
- Output medium: Manim (mp4)
- Two testable predictions: P1: σ_x(t=τ) = σ_0 √2 exactly (checkable from formula, τ = 2mσ_0²/ℏ); P2: ⟨x⟩ = ⟨x⟩_0 + ⟨p⟩t/m — center moves at group velocity, not at phase velocity.
- The change: start with a moving wavepacket (⟨p⟩ ≠ 0) — the envelope drifts AND spreads; the center follows Newton's first law while the width obeys the uncertainty bound.
- Human supplies (Claude can't): Nothing — fully synthetic/analytic.
- Teardown angle: The Heisenberg picture says x̂_H(t) = x̂ + (p̂/m)t exactly; the spreading is the initial σ_x growing with time because different momentum components travel at different speeds. Quantum uncertainty is not a measurement artifact; it propagates classically once prepared.
- Exclusions: Do not attempt full numerical TDSE; Gaussian analytic solution is exact and sufficient. Do not show position measurement collapse.
- Sim slug: qm2-wavepacket-spread
- Score: 10/10

---

## Candidate 02 — Explore: Rabi Oscillation — Spin Flopping Between Up and Down
- Source: `quantum-mechanics-vol2/chapters/04-quantum-dynamics-and-the-pictures.md`
- Topic: Rabi oscillation / spin dynamics in transverse field
- Lane: D3/DATAVIZ (emergent / interactive)
- Hook: A spin that starts pointing up can transfer completely to pointing down and back — with no measurement, no collapse, just deterministic beating. Drag the Rabi frequency and watch the period change in real time.
- The rule: H = ω_0 S_x = (ω_0 ℏ/2)σ_x; |ψ(t)⟩ = cos(ω_0 t/2)|↑⟩ − i sin(ω_0 t/2)|↓⟩; P↑(t) = cos²(ω_0 t/2), P↓(t) = sin²(ω_0 t/2). Driven by beat between two energy eigenstates separated by ℏω_0.
- Concrete numbers: ω_0/(2π) = 1 MHz (NMR-scale); period T = 2π/ω_0 = 1 µs; at t = π/ω_0, P↑ = 0 (complete inversion); at t = π/2ω_0, P↑ = P↓ = 1/2.
- The artifact / what moves: Two live probability bars (P↑ in blue, P↓ in orange) oscillating sinusoidally while summing to 1 at all times. A Bloch-sphere panel shows the state vector sweeping through a great circle at rate ω_0. Slider for ω_0 speeds or slows the oscillation.
- Output medium: d3 v7 animated/interactive HTML
- Two testable predictions: P1: complete inversion at t = π/ω_0 (P↑ = 0 exactly); P2: P↑ + P↓ = 1 at all times — unitarity is enforced by the cos²+sin²=1 identity.
- The change: add a slider for initial polar angle θ_0 — equatorial start (θ_0 = π/2) gives maximum oscillation amplitude; polar start (θ_0 = 0) gives zero oscillation (stationary state).
- Human supplies (Claude can't): Nothing — fully synthetic/analytic.
- Teardown angle: This is the physics behind every NMR pulse. The spin's period = 1/f_Rabi. The transition probability is not probabilistic in time — it is completely deterministic. Randomness only enters when you measure.
- Exclusions: Do not add relaxation (T1/T2 decay) — keep it unitary. Do not simulate the magnetic field gradient (that's MRI, not Rabi oscillation).
- Sim slug: qm2-rabi-oscillation
- Score: 10/10
- Status: BUILT — `open /Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-vol2/youtube/qm2-rabi-oscillation/qm2-rabi-oscillation.html`

---

## Candidate 03 — Animate: Angular Momentum Cone — The Vector That Can Never Align
- Source: `quantum-mechanics-vol2/chapters/05-quantum-mechanics-in-three-dimensions.md` + `quantum-mechanics-vol2/chapters/06-angular-momentum.md`
- Topic: Angular momentum cone geometry and the ℓ(ℓ+1) vs ℓ² distinction
- Lane: MANIM (directed animation)
- Hook: Even when L_z is as large as it can be, the angular momentum vector cannot point along the z-axis — it's constrained to sweep a cone. This is not measurement uncertainty; it's baked into the algebra.
- The rule: For |ℓ, m=ℓ⟩: |L| = ℏ√(ℓ(ℓ+1)), L_z = ℓℏ; cone half-angle = arccos(ℓ/√(ℓ(ℓ+1))). As ℓ→∞, half-angle → 0 (classical limit). ⟨L_x⟩ = ⟨L_y⟩ = 0 but σ_{L_x} = σ_{L_y} = ℏ√(ℓ/2).
- Concrete numbers: ℓ=1: |L|=ℏ√2, half-angle=45°; ℓ=2: |L|=ℏ√6, half-angle≈35.3°; ℓ=10: half-angle≈17.5°; ℓ=100: half-angle≈5.7°. Robertson bound saturated: σ_{L_x}σ_{L_y} = ℏ²ℓ/2 exactly.
- The artifact / what moves: A 3D cone with a labeled vector of length ℏ√(ℓ(ℓ+1)) precessing around the z-axis. The z-projection ℓℏ is shown as a vertical bar. As ℓ increases (slider), the cone narrows visually toward the z-axis. At ℓ=∞, the cone closes to a line — classical limit.
- Output medium: Manim (mp4)
- Two testable predictions: P1: at ℓ=1, half-angle = arccos(1/√2) = 45° exactly; P2: Robertson bound σ_{L_x}σ_{L_y} = ℏ²ℓ/2 is saturated at every ℓ for the |ℓ,ℓ⟩ state.
- The change: show the full ladder of m values (m = -ℓ to +ℓ) as a stack of cones at different latitudes; together they form a "fan" of allowed orientations — the semiclassical picture of quantized angular momentum.
- Human supplies (Claude can't): Nothing — fully synthetic/analytic.
- Teardown angle: The Bohr model required angular momentum to point in a definite direction (circular orbit in a fixed plane). The algebra forbids it. No definite orbital plane. No definite orbit. There is only a cone.
- Exclusions: Do not attempt to visualize the full spherical harmonic as a 3D surface in this card — that gets its own sim. Stay focused on the cone geometry and the Robertson saturation.
- Sim slug: qm2-angular-momentum-cone
- Score: 9/10

---

## Candidate 04 — Explore: Hydrogen Energy Levels — Sweep n, ℓ, and Watch the Radial Wavefunction
- Source: `quantum-mechanics-vol2/chapters/09-the-hydrogen-atom.md`
- Topic: Hydrogen radial wavefunctions, nodes, and the centrifugal barrier
- Lane: D3/DATAVIZ (emergent / interactive)
- Hook: Every time you increase ℓ by 1 you lose a radial node and gain an angular one — but the energy is unchanged. That "accidental" degeneracy is the deepest symmetry in atomic physics.
- The rule: R_{nℓ}(r) ∝ (r/a₀)^ℓ · e^{-r/na₀} · L^{2ℓ+1}_{n-ℓ-1}(2r/na₀). Radial nodes = n-ℓ-1; angular nodes = ℓ; total nodes = n-1. P(r) = r²|R_{nℓ}|². E_n = -13.6 eV/n² (independent of ℓ).
- Concrete numbers: (1,0): 0 radial nodes, peak at a₀=0.529 Å; (2,0): 1 radial node at 2a₀, (2,1): 0 radial nodes, peak at 5a₀; (3,0): 2 radial nodes; (3,2): 0 radial nodes, peak near 9a₀. ⟨r⟩_{nℓ} = (a₀/2)[3n²-ℓ(ℓ+1)].
- The artifact / what moves: Live plot of P(r) = r²|R_{nℓ}(r)|² updating in real time as the user changes n (1–5) and ℓ (0 to n-1) via dropdowns. Radial nodes marked as red dots. Mean radius ⟨r⟩ as a vertical dashed line. Effective potential V_eff(r) shown faintly in the background.
- Output medium: d3 v7 animated/interactive HTML
- Two testable predictions: P1: number of peaks in P(r) = n-ℓ (checkable by counting for any (n,ℓ)); P2: ⟨r⟩_{nℓ} = (a₀/2)[3n²-ℓ(ℓ+1)] — verify numerically for (2,0): ⟨r⟩=6a₀; (2,1): ⟨r⟩=5a₀.
- The change: add an overlay toggle showing the same n, different ℓ curves simultaneously — all sharing the same energy (Coulomb degeneracy), with wildly different radial shapes. Switch to a Yukawa potential (add screening) and watch the degeneracy split.
- Human supplies (Claude can't): Nothing — fully synthetic/analytic (Laguerre polynomials available analytically).
- Teardown angle: The Coulomb potential is special: its SO(4) symmetry makes E depend only on n, not ℓ. The moment you add any perturbation (screening, external field), the degeneracy breaks and every (n,ℓ) pair gets a distinct energy. This is exactly the spectroscopic origin of the periodic table's structure.
- Exclusions: Do not render 3D orbital isosurfaces (different card). Do not include spin or time evolution.
- Sim slug: qm2-hydrogen-radial-explorer
- Score: 9/10
- Status: BUILT — `open /Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-vol2/youtube/qm2-hydrogen-radial-explorer/qm2-hydrogen-radial-explorer.html`

---

## Candidate 05 — Animate: Parabolic State in a Square Well — Two Bases, Same Expectation Value
- Source: `quantum-mechanics-vol2/chapters/01-the-formalism.md`
- Topic: Basis independence of expectation values; energy-basis expansion
- Lane: MANIM (directed animation)
- Hook: The same state computed two completely different ways — a weighted discrete sum in energy space versus a double derivative in position space — lands on the exact same number. That is what "basis-independent" actually means.
- The rule: ψ(x) = √(30/L⁵)·x(L-x); c_n = 4√60/(n³π³) for odd n, 0 for even n; ⟨H⟩ = Σ|c_n|²E_n = 5ℏ²/mL² = also -(ℏ²/2m)∫ψ∂²ψ/∂x² dx. E_n = n²π²ℏ²/(2mL²).
- Concrete numbers: c_1 = 4√60/π³ ≈ 0.9986 so |c_1|² ≈ 0.9986²; c_3/c_1 = 1/27; ⟨H⟩/E_1 = 10/π² ≈ 1.013; the ground state carries essentially all (>99.8%) of the probability. Normalization check: Σ_{odd}|c_n|² = (960/π⁶)(π⁶/960) = 1 exactly.
- The artifact / what moves: Split screen — left panel shows the parabolic ψ(x) and the running sum of energy eigenstates building up toward it (partial sums |c_1ψ_1⟩ + |c_3ψ_3⟩ + …). Right panel shows the |c_n|² bar chart collapsing to essentially one bar at n=1. Bottom: two running integrals converging to the same ⟨H⟩ value by different routes.
- Output medium: Manim (mp4)
- Two testable predictions: P1: Σ_{odd n}|c_n|² = 1 (normalization check, uses π⁶/960 identity); P2: ⟨H⟩ = 5ℏ²/mL² from both the position-basis integral and the energy-basis sum — same number, verifiable.
- The change: perturb the initial state slightly (shift the parabola) and watch the energy spectrum respond — odd/even symmetry breaks, even modes appear.
- Human supplies (Claude can't): Nothing — fully synthetic/analytic.
- Teardown angle: The energy-basis route requires knowing the eigenstates. For a complicated potential you cannot write them down — the abstract formalism is exact but the energy-basis route is unavailable. The position-basis route works whenever you can evaluate the integral. The choice of basis is a computational convenience, not a physical preference.
- Exclusions: Do not animate time evolution (the state is not evolving here). Do not compute Fourier transform separately — the c_n ARE the Fourier-sine coefficients.
- Sim slug: qm2-parabolic-state-basis
- Score: 9/10

---

## Candidate 06 — Animate: Larmor Precession on the Bloch Sphere
- Source: `quantum-mechanics-vol2/chapters/07-spin-and-the-bloch-sphere.md`
- Topic: Larmor precession; spin in a magnetic field; MRI physics
- Lane: MANIM (directed animation)
- Hook: The Bloch vector circles at exactly the MRI frequency — the same equation that drives every clinical scanner. Point at a proton at 1.5 T and watch it spin at 63.87 MHz.
- The rule: H = (γB₀ℏ/2)σ_z; U(t) = diag(e^{-iω_Lt/2}, e^{+iω_Lt/2}); ω_L = γB₀. State at polar angle θ₀: ⟨S_x⟩ = (ℏ/2)sinθ₀·cos(ω_Lt), ⟨S_y⟩ = (ℏ/2)sinθ₀·sin(ω_Lt), ⟨S_z⟩ = (ℏ/2)cosθ₀ (constant).
- Concrete numbers: Proton γ/(2π) = 42.58 MHz/T; at B₀ = 1.5 T: ω_L/(2π) = 63.87 MHz, T_L = 15.66 ns. At B₀ = 3.0 T: 127.74 MHz. θ₀ = π/3: P(+) = cos²(π/6) = 3/4 (constant in time).
- The artifact / what moves: Bloch sphere with a labeled vector at fixed polar angle θ₀ sweeping azimuthal circles at ω_L. The projections ⟨S_x⟩ and ⟨S_y⟩ oscillate sinusoidally on side-panel time traces; ⟨S_z⟩ stays flat. A field strength slider changes ω_L and the precession speed updates instantly.
- Output medium: Manim (mp4)
- Two testable predictions: P1: ⟨S_z⟩ = (ℏ/2)cosθ₀ is time-independent (constant of motion); P2: ω_L = γB₀ — doubling B₀ doubles the precession frequency exactly, verifiable in the animation.
- The change: set θ₀ = 0 (north pole, S_z eigenstate) — the state is stationary, nothing precesses, demonstrating that an energy eigenstate acquires only a global phase.
- Human supplies (Claude can't): Nothing — fully synthetic/analytic.
- Teardown angle: The precessing vector is the expectation value of spin — a probability distribution, not a physical spinning needle. The randomness only appears when you measure. But the frequency is real: every clinical MRI scanner relies on ω_L = γ_p B₀ to 6 significant figures.
- Exclusions: Do not simulate pulse sequences or T1/T2 relaxation. Do not introduce rotating frames.
- Sim slug: qm2-larmor-precession
- Score: 9/10

---

## Candidate 07 — Explore: Robertson Bound on the Bloch Sphere — Color-Map the Uncertainty
- Source: `quantum-mechanics-vol2/chapters/03-commutators-and-uncertainty.md`
- Topic: State-dependent Robertson bound for spin; uncertainty as a map on the Bloch sphere
- Lane: D3/DATAVIZ (emergent / interactive)
- Hook: At the north and south poles of the Bloch sphere the Robertson bound for S_x and S_y is zero — but the actual product σ_{S_x}σ_{S_y} is NOT zero. The bound gives zero only because it's weak there, not because the uncertainties vanish.
- The rule: [S_x, S_y] = iℏS_z → Robertson: σ_{S_x}σ_{S_y} ≥ (ℏ/2)|⟨S_z⟩| = (ℏ²/4)|cosθ|. Actual product for |ℓ,ℓ⟩ states: σ_{S_x}σ_{S_y} = ℏ²/4 everywhere on Bloch sphere (for spin-½). Bound is maximized at poles (|cosθ|=1), zero at equator.
- Concrete numbers: At θ=0 (north pole): bound = ℏ²/4, actual = ℏ²/4 (saturated). At θ=π/2 (equator): bound = 0, actual = ℏ²/4 (unsaturated — bound is vacuous). At S_y eigenstate (θ=π/2, φ=π/2): ⟨S_z⟩=0, bound=0, actual σ_{S_x}σ_{S_z} = ℏ²/4.
- The artifact / what moves: Interactive Bloch sphere colored by Robertson bound value (ℏ/2)|⟨S_z⟩| — blue at equator (bound=0), red at poles (bound=ℏ²/4). Click any point on the sphere: tooltip shows state (θ,φ), the bound value, and the actual σ product. A second heat-map tab shows actual σ_{S_x}σ_{S_y} — constant everywhere (spin-½ special property).
- Output medium: d3 v7 animated/interactive HTML
- Two testable predictions: P1: At θ=0 (|↑⟩), bound = ℏ²/4 and σ_{S_x}σ_{S_y} = ℏ²/4 — exactly saturated; P2: At θ=π/2 (equatorial state), bound = 0 but σ_{S_x}σ_{S_y} = ℏ²/4 ≠ 0 — zero bound does not imply zero uncertainty.
- The change: Switch to the [S_x, S_z] = −iℏS_y Robertson bound — now the S_y eigenstates are where the bound is maximized and saturated.
- Human supplies (Claude can't): Nothing — fully synthetic/analytic (Bloch sphere trig + Pauli algebra).
- Teardown angle: A zero Robertson bound is the theorem being silent, not the uncertainty being zero. Students consistently confuse "the bound is zero" with "the quantities can both be sharp." This sim makes the distinction unavoidable: click the equator, see bound=0 and actual≠0 simultaneously.
- Exclusions: Do not plot the Schrödinger bound (anticommutator term) — keep the comparison clean. Do not go beyond spin-½.
- Sim slug: qm2-robertson-bloch-heatmap
- Score: 9/10
- Status: BUILT — `open /Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-vol2/youtube/qm2-robertson-bloch-heatmap/qm2-robertson-bloch-heatmap.html`

---

## Candidate 08 — Animate: Singlet vs Triplet — One Minus Sign Separates 21-cm Radio Astronomy
- Source: `quantum-mechanics-vol2/chapters/08-addition-of-angular-momenta.md`
- Topic: Hyperfine splitting; singlet-triplet energy gap; hydrogen 21-cm line
- Lane: MANIM (directed animation)
- Hook: The most observed spectral line in radio astronomy — the 21-cm hydrogen line — is controlled by a single minus sign in a quantum state. Two states identical in spatial structure, differing only by that sign, split by 5.87×10⁻⁶ eV.
- The rule: H_hf = A·S_e·S_p = (A/2)(F² − S_e² − S_p²). Triplet F=1: E = +Aℏ²/4. Singlet F=0: E = −3Aℏ²/4. Gap ΔE = Aℏ² = 5.87×10⁻⁶ eV → f = 1420.405 MHz → λ = 21.1 cm. The two states: |1,0⟩ = (|↑↓⟩+|↓↑⟩)/√2 (triplet, +sign) vs |0,0⟩ = (|↑↓⟩−|↓↑⟩)/√2 (singlet, −sign).
- Concrete numbers: A = 5.87×10⁻⁶ eV/ℏ² = 9.40×10⁻²⁵ J/ℏ²; f = Aℏ²/h = 1420.405 MHz (to 7 sig figs); λ = c/f = 21.106 cm; Engraved on Voyager golden record as a time unit (T = 0.704 ns).
- The artifact / what moves: Two-panel animation. Left: the four two-spin states building up via the CG ladder algorithm — |1,1⟩, then J_- lowering to |1,0⟩, then the orthogonalization that produces |0,0⟩ with the minus sign highlighted in red. Right: an energy level diagram showing the F=1 triplet (three degenerate levels) above F=0 singlet, with the 21-cm photon emission arrow labeled with 1420.405 MHz.
- Output medium: Manim (mp4)
- Two testable predictions: P1: ⟨J²⟩|0,0⟩ = 0 (verify by acting with J²=J_1²+J_2²+2J_{1z}J_{2z}+J_{1+}J_{2-}+J_{1-}J_{2+} on the singlet and checking exact cancellation); P2: Energy gap = Aℏ² — triplet at +ℏ²/4, singlet at −3ℏ²/4, gap = ℏ² (in units of A).
- The change: show what happens if the minus sign is flipped to plus — both states become the symmetric |1,0⟩ triplet, the J=0 state disappears, and the 21-cm line cannot exist.
- Human supplies (Claude can't): Nothing — fully synthetic/analytic.
- Teardown angle: The singlet-triplet energy splitting is not from any spin-spin magnetic force. It is from the exchange term in the antisymmetrized wavefunction. The sign distinguishes whether the two-spin state is symmetric or antisymmetric under exchange — and that sign is not detectable by measuring either spin alone.
- Exclusions: Do not animate the actual radio telescope observation. Do not go into hyperfine fine-structure beyond the F=0,1 splitting.
- Sim slug: qm2-singlet-triplet-21cm
- Score: 9/10

---

## Candidate 09 — Explore: Centrifugal Barrier and Effective Potential — Sweep ℓ and Watch the Well Deform
- Source: `quantum-mechanics-vol2/chapters/05-quantum-mechanics-in-three-dimensions.md` + `quantum-mechanics-vol2/chapters/09-the-hydrogen-atom.md`
- Topic: Effective radial potential; centrifugal barrier; how ℓ repels from the nucleus
- Lane: D3/DATAVIZ (emergent / interactive)
- Hook: Increase ℓ and the potential well physically lifts away from the nucleus — the electron is pushed outward by nothing but angular momentum. The radial Schrödinger equation looks 1D, but ℓ changes the entire landscape.
- The rule: V_eff(r) = V(r) + ℏ²ℓ(ℓ+1)/(2mr²). For hydrogen: V(r) = -e²/(4πε₀r). Centrifugal term grows as ℓ(ℓ+1). For ℓ=0: pure Coulomb, finite at r→0. For ℓ≥1: diverging repulsive wall at origin.
- Concrete numbers: At r=a₀ (Bohr radius): V_Coulomb = -27.2 eV; centrifugal term at r=a₀: ℓ(ℓ+1)×ℏ²/(2m_e a₀²) = ℓ(ℓ+1)×13.6 eV. For ℓ=1: +27.2 eV at r=a₀ — nearly cancels Coulomb. For ℓ=2: +81.6 eV — strongly repulsive near origin. Minimum of V_eff shifts from r=a₀ (ℓ=0) outward with ℓ.
- The artifact / what moves: Live plot of V_eff(r) for hydrogen updating as user drags ℓ slider (0, 1, 2, 3, 4). Pure Coulomb shown as dashed baseline. Centrifugal barrier shown as a separate fill. The combined curve V_eff animates smoothly. A horizontal slider for energy E shows which bound states exist below E=0. For the spherical infinite well variant: show how level ordering changes with ℓ.
- Output medium: d3 v7 animated/interactive HTML
- Two testable predictions: P1: For ℓ=0, V_eff = V(r) — no barrier; wavefunction is finite at r=0 (verified by R_{10}(0) ≠ 0); P2: Minimum of V_eff for hydrogen shifts outward as ℓ increases — for ℓ=1, minimum is at r = 2a₀ (derivable by dV_eff/dr = 0).
- The change: switch to the spherical infinite well (V=0 inside, ∞ outside) and show how energies E_{nℓ} = ℏ²β_{nℓ}²/(2ma²) depend on Bessel zeros — nuclear shell model level ordering emerges visually.
- Human supplies (Claude can't): Nothing — fully synthetic/analytic.
- Teardown angle: The centrifugal barrier is kinetic energy (L²/2mr²), not a potential. Students who label it "potential energy" misidentify the physics. The radial equation looks like a 1D problem in a modified potential, but the modification is angular kinetic energy in disguise.
- Exclusions: Do not attempt to plot 3D orbitals. Do not add fine-structure perturbations.
- Sim slug: qm2-centrifugal-barrier-explorer
- Score: 8/10
- Status: BUILT — `open /Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-vol2/youtube/qm2-centrifugal-barrier-explorer/qm2-centrifugal-barrier-explorer.html`

---

## Candidate 10 — Animate: Ehrenfest Breakdown in a Double Well
- Source: `quantum-mechanics-vol2/chapters/04-quantum-dynamics-and-the-pictures.md`
- Topic: Ehrenfest's theorem; classical-quantum correspondence; wavepacket bifurcation
- Lane: MANIM (directed animation)
- Hook: A narrow quantum wavepacket obeys Newton's law perfectly — until the wave spreads enough to "feel" the curvature of the potential. Then the expectation value of position can sit exactly at the unstable equilibrium while the actual probability density bifurcates into two lobes. Classical prediction: dead wrong.
- The rule: d⟨x⟩/dt = ⟨p⟩/m; d⟨p⟩/dt = -⟨V'(x)⟩ ≠ -V'(⟨x⟩) unless V is exactly quadratic. Difference ≈ (Δx)² V'''(⟨x⟩)/6. Double well: V(x) = -ax²/2 + bx⁴/4. At x=0: V'(0)=0, V'''(0)=−6a. Wavepacket started at x=0 (unstable equilibrium): ⟨x⟩ stays at 0, but |ψ|² splits.
- Concrete numbers: Use ħ=1 units; m=1; V(x) = -x²/2 + x⁴/4 (symmetric double well with minima at x=±1, barrier height 0.25). Start Gaussian at x=0, σ=0.3. Split time ~ 1/√a. ⟨x⟩=0 for all time (symmetry). Probability in left half vs. right half grows from 50/50 → peaks at 50/50 but with bimodal shape.
- The artifact / what moves: Side-by-side panel. Left: |ψ(x,t)|² plotted as a filled curve, initially a single Gaussian at the central maximum, slowly deforming and splitting into two lobes over the double-well minima. Right: ⟨x⟩ vs t (a flat line at zero — perfectly classical!), alongside the classical trajectory from the same initial conditions (also stays at 0). A third trace shows σ_x(t) growing — the two panels diverge dramatically.
- Output medium: Manim (mp4)
- Two testable predictions: P1: ⟨x⟩(t) = 0 for all t — symmetry of V(x) and initial state forces this exactly, regardless of splitting; P2: σ_x grows monotonically after the split — the variance of position increases even though the mean is constant.
- The change: displace the initial Gaussian slightly off-center (x₀ = 0.01): ⟨x⟩ now follows a classical trajectory into one of the wells, but |ψ|² can still tunnel to the other. The Ehrenfest equation still holds approximately while the packet is narrow, then fails.
- Human supplies (Claude can't): Nothing — requires numerical TDSE integration, fully synthetic.
- Teardown angle: Ehrenfest is exact only for harmonic or lower-order potentials. Every real physical system is anharmonic at large amplitude. Quantum mechanics departs from classical not because measurements disturb things, but because wavefunctions have non-zero width and the curvature of the potential matters.
- Exclusions: Do not attempt to add measurement collapse or decoherence. Keep potential smooth — no hard walls or delta functions in this card.
- Sim slug: qm2-ehrenfest-double-well
- Score: 8/10

---

## Candidate 11 — Explore: Exchange Interaction and Para/Ortho Helium Splitting
- Source: `quantum-mechanics-vol2/chapters/10-identical-particles.md`
- Topic: Exchange integral K; para/orthohelium energy splitting; spatial symmetry and Coulomb energy
- Lane: D3/DATAVIZ (emergent / interactive)
- Hook: Helium has two spectral families — para and ortho — that behave like different elements. There is no spin-spin force. The splitting comes entirely from the sign of the spatial wavefunction and its effect on how close the two electrons get.
- The rule: E± = E⁰ + J ± K. J = direct (Coulomb) integral. K = exchange integral = ∫∫ φ₁s*(r₁)φ₂s*(r₂) [e²/4πε₀|r₁-r₂|] φ₂s(r₁)φ₁s(r₂) d³r₁ d³r₂ > 0. Symmetric spatial (parahelium, singlet spin): energy J+K (higher). Antisymmetric spatial (orthohelium, triplet spin): energy J-K (lower by 2K).
- Concrete numbers: For 1s2s configuration: J ≈ 11.4 eV, K ≈ 0.40 eV; 2K ≈ 0.80 eV observed splitting. Antisymmetric spatial ψ_-(r₁,r₂) = 0 when r₁=r₂ — Pauli node at coincidence. This reduces ⟨1/|r₁-r₂|⟩ → less repulsion → lower energy.
- The artifact / what moves: A 2D joint probability density |ψ(x₁,x₂)|² shown as a heatmap (one spatial coordinate per axis, simplified to 1D model). Toggle between symmetric (+) and antisymmetric (−) spatial wavefunctions. The antisymmetric map shows a clear diagonal exclusion zone (Pauli node at x₁=x₂). Energy readout shows J±K updating as K is dialed.
- Output medium: d3 v7 animated/interactive HTML
- Two testable predictions: P1: ψ_-(r,r) = 0 exactly — the antisymmetric state vanishes on the x₁=x₂ diagonal (verifiable in the heatmap as a white diagonal stripe); P2: orthohelium 1s2s lies below parahelium 1s2s by 2K ≈ 0.80 eV (literature value checkable).
- The change: slide K from 0 (degenerate) to the helium value — watch the two energy levels split apart. At K=0 there is no splitting; antisymmetry has no energy consequence without the Coulomb interaction.
- Human supplies (Claude can't): Nothing — model computable with hydrogenic wave functions; exact value requires numerical integral but functional form is analytic.
- Teardown angle: The exchange interaction is not a force. There is no spin-spin term in the Hamiltonian. The energy split is purely geometric: where the wavefunction is zero (the Pauli node), the electrons cannot meet; where they cannot meet, they repel less. The "exchange force" is the Coulomb repulsion weighted by a wavefunction that vanishes on the diagonal.
- Exclusions: Do not attempt to compute the full 3D exchange integral numerically in real-time. Use the 1D model as a proxy — label it clearly as a pedagogical simplification.
- Sim slug: qm2-exchange-pauli-node
- Score: 8/10
- Status: BUILT — `open /Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-vol2/youtube/qm2-exchange-pauli-node/qm2-exchange-pauli-node.html`

---

## Candidate 12 — Animate: Spherical Harmonics — |Y_ℓ^m|² on the Sphere and the φ-Independence Fact
- Source: `quantum-mechanics-vol2/chapters/05-quantum-mechanics-in-three-dimensions.md`
- Topic: Spherical harmonics; axial symmetry of |Y_ℓ^m|²; chemistry vs physics orbital comparison
- Lane: MANIM (directed animation)
- Hook: Every physics student expects the m≠0 spherical harmonics to look like rings — and they do. But the real p_x and p_y orbitals are dumbbells pointing along x and y. Both descriptions are "correct." Why?
- The rule: |Y_ℓ^m(θ,φ)|² = f(θ) only — independent of φ because e^{imφ} has |e^{imφ}|=1. Real chemistry orbitals: p_x ∝ (Y_1^1 - Y_1^{-1})/√2 ∝ sinθcosφ — NOT an eigenstate of L_z. L_z p_x = iℏ p_y ≠ λ p_x.
- Concrete numbers: Y_1^0: |Y_1^0|² ∝ cos²θ — two lobes on z-axis, φ-independent. Y_1^{±1}: |Y_1^{±1}|² ∝ sin²θ — a torus around z-axis, φ-independent. p_x: ∝ sinθcosφ — dumbbell along x-axis, φ-dependent. Same ℓ=1 subspace, but one diagonalizes L_z, the other doesn't.
- The artifact / what moves: A rotating 3D surface on a sphere plotting |Y_ℓ^m(θ,φ)|² as radial distance. Start at (ℓ=0,m=0): sphere. Step to (1,0): a peanut on z-axis. Step to (1,1): a donut around z-axis. Then animate the linear combination forming p_x — the donut morphs into a dumbbell. Finally show L_z acting on p_x → producing ip_y, visually demonstrating non-eigenstate behavior.
- Output medium: Manim (mp4)
- Two testable predictions: P1: All |Y_ℓ^m|² are φ-independent — confirmed by showing the same cross-section at φ=0, π/3, π/2 overlapping perfectly; P2: L_z(p_x) = iℏ p_y — applying -iℏ∂/∂φ to sinθcosφ gives sinθsinφ = p_y (times iℏ), not p_x.
- The change: compare Y_2^0 (d_z² orbital) with its real combination d_x²-y² — same ℓ=2 subspace, one is a L_z eigenstate, the other is a bonding d orbital from chemistry. Same energy, completely different angular structure.
- Human supplies (Claude can't): Nothing — fully synthetic/analytic.
- Teardown angle: Chemistry picks the real basis because orbitals need to point toward bonding partners. Physics picks the complex basis because L_z is diagonal. Neither is "wrong." The choice of basis reveals what you care about: spatial orientation (chemistry) or angular momentum projection (physics).
- Exclusions: Do not attempt to include radial wavefunction in this visualization — just the angular part. Do not animate time evolution.
- Sim slug: qm2-spherical-harmonics-basis
- Score: 8/10

---

## Candidate 13 — Explore: Madelung Exceptions — Exchange Energy vs Orbital Gap
- Source: `quantum-mechanics-vol2/chapters/11-capstone-the-atom.md`
- Topic: Chromium/Copper Madelung exceptions; exchange energy stabilization; 3d/4s competition
- Lane: D3/DATAVIZ (emergent / interactive)
- Hook: The Madelung rule for filling electrons fails for about 20 elements. The mechanism is a competition between two energy contributions — you can watch which one wins as you dial Z across the transition series.
- The rule: Total energy = orbital energy (from Slater Z_eff) + exchange energy E_K = −K × (number of parallel-spin pairs). K ≈ 0.18 eV for 3d in Cr. Half-filled 3d (Cr: 5 parallel-spin pairs vs 6 for 3d⁴) has 10 parallel pairs vs 6 — exchange gain of 4K ≈ 0.72 eV. 3d-4s gap ≈ 0.2 eV for Cr.
- Concrete numbers: Cr (Z=24): Madelung [Ar]3d⁴4s² → actual [Ar]3d⁵4s¹. Parallel pairs in 3d⁴: C(4,2)=6; in 3d⁵: C(5,2)=10; gain=4 pairs × 0.18 eV = 0.72 eV > gap 0.2 eV → exception. Ti (Z=22): [Ar]3d²4s²; 3d²: 1 pair, 3d³: 3 pairs; gain=2×0.18=0.36 eV; but gap is larger (~0.5 eV) → no exception.
- The artifact / what moves: Interactive energy level diagram for Z=21 to 30. Slider for Z. Two energy bars: "Orbital energy cost of promoting one 4s → 3d" (grows smaller near Z=24,29) and "Exchange energy gain from extra parallel pair" (fixed ~0.18 eV per pair). When the gain bar exceeds the cost bar, the exception occurs — highlighted in red. The actual NIST configuration shown vs Madelung prediction.
- Output medium: d3 v7 animated/interactive HTML
- Two testable predictions: P1: For Cr (Z=24): exchange gain (4×K) > orbital gap → exception predicted; for Ti (Z=22): exchange gain (2×K) < orbital gap → no exception; P2: Cu (Z=29): 3d⁹→3d¹⁰ gains C(10,2)-C(9,2)=9 pairs × K ≈ 1.62 eV vs ~0.1 eV gap → exception.
- The change: dial K from 0 (no exchange) to the Cr value — at K=0, no exceptions occur anywhere; as K grows, Cr and Cu flip first because they have the smallest 3d-4s gaps.
- Human supplies (Claude can't): 3d-4s gap values for each transition metal from NIST/Hartree-Fock tables (Clementi-Roetti 1974); K value from spectroscopic data.
- Teardown angle: The Madelung rule has no derivation from first principles. It is an empirical pattern. The exceptions are the places where it fails — and understanding them requires quantitative competition between two energy scales that Madelung ignores.
- Exclusions: Do not attempt full Hartree-Fock computation. Use the simplified exchange-energy counting model, labeled as an approximation.
- Sim slug: qm2-madelung-exceptions
- Score: 7/10
- Status: BUILT — `open /Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-vol2/youtube/qm2-madelung-exceptions/qm2-madelung-exceptions.html`

---

## Candidate 14 — Animate: Ladder Operator Climb — Building the ℓ=2 Spectrum from Commutator Algebra
- Source: `quantum-mechanics-vol2/chapters/06-angular-momentum.md`
- Topic: Raising/lowering operators; algebraic derivation of angular momentum spectrum; ladder normalization
- Lane: MANIM (directed animation)
- Hook: The entire quantum number structure of angular momentum — every half-integer ℓ, every m from -ℓ to +ℓ — follows from three commutation relations and one inequality. You never solve a differential equation. The ladder terminates because a norm cannot be negative.
- The rule: [L_z, L_+] = ℏL_+; L_+|ℓ,m⟩ = ℏ√((ℓ-m)(ℓ+m+1))|ℓ,m+1⟩; termination condition: L_+|ℓ,ℓ⟩ = 0 → λ = ℏ²ℓ(ℓ+1). Coefficients: √((ℓ-m)(ℓ+m+1)) for ℓ=2: √8, √(2·4)=√8... specifically: |2,-2⟩→|2,-1⟩: √(4·1)=2; |2,-1⟩→|2,0⟩: √(3·2)=√6; |2,0⟩→|2,1⟩: √6; |2,1⟩→|2,2⟩: 2.
- Concrete numbers: For ℓ=2: coefficients on ladder rungs are 2, √6, √6, 2 (symmetric). Top rung: L_+|2,2⟩ = 0 — coefficient = √((2-2)(2+3)) = 0 exactly. L² eigenvalue = 6ℏ². Robertson saturation: σ_{L_x}σ_{L_y} = ℏ²·ℓ/2 = ℏ² at ℓ=2.
- The artifact / what moves: A vertical ladder with 5 rungs labeled |2,-2⟩ through |2,2⟩. Animated arrows climb the ladder when you press "raise" and descend when you press "lower." Each arrow is labeled with its normalization coefficient. At the top, the arrow is grayed out and shows "= 0 (terminated)." An L² eigenvalue display shows 6ℏ² throughout. A small "Robertson saturation" panel tracks σ_{L_x}σ_{L_y} at each rung.
- Output medium: Manim (mp4)
- Two testable predictions: P1: All rungs have L² eigenvalue = 6ℏ² = ℏ²·2·3 (computed from the same |ℓ=2⟩ states — L² commutes with L_±); P2: Coefficient at |2,1⟩ is √6 — verifiable as √((2-1)(2+1+1)) = √(1·4) = 2... wait: √((ℓ-m)(ℓ+m+1)) = √((2-1)(2+1+1)) = √(1·4) = 2; at m=0: √((2-0)(2+0+1)) = √(2·3) = √6. Checkable against explicit matrix multiplication.
- The change: switch to ℓ=1/2 (spin-½): only two rungs, coefficients are both 1. The matrices are σ_±/2. The same algebraic derivation — one line shorter — produces the Pauli matrices.
- Human supplies (Claude can't): Nothing — fully synthetic/analytic.
- Teardown angle: The half-integer possibility (ℓ=1/2, 3/2, ...) emerges naturally from the algebra. The integer restriction for orbital angular momentum is an additional constraint from wave-function single-valuedness on the sphere. Spin lives in a different space and faces no such constraint — which is why spin-½ is physical despite having no classical analog.
- Exclusions: Do not animate the position-space derivation of spherical harmonics here. Stay in abstract Hilbert space with the ladder.
- Sim slug: qm2-ladder-operators-ell2
- Score: 8/10

---

## Candidate 15 — Explore: Hydrogen Transition Explorer — Selection Rules and Spectral Series
- Source: `quantum-mechanics-vol2/chapters/09-the-hydrogen-atom.md`
- Topic: Electric-dipole selection rules; Lyman/Balmer/Paschen series; forbidden transitions
- Lane: D3/DATAVIZ (emergent / interactive)
- Hook: Not every transition between hydrogen energy levels produces a photon. Only Δℓ = ±1, Δm = 0, ±1 transitions are allowed. Click any two levels: the sim tells you allowed or forbidden, the wavelength if allowed, and how slow the forbidden process is.
- The rule: E_n = -13.6 eV/n²; photon energy ℏω = E_ni - E_nf = 13.6 eV (1/n_f² - 1/n_i²). Selection rule Δℓ = ±1 comes from ⟨ψ_f|r|ψ_i⟩ ≠ 0 only if angular momentum changes by 1 (dipole matrix element). Forbidden Δℓ=0 transition (2s→1s): two-photon emission, lifetime ≈ 0.12 s.
- Concrete numbers: Lyman α (2p→1s): λ = 1240 eV·nm/(10.2 eV) = 121.6 nm (UV). Balmer α (3→2): λ = 656.3 nm (red). Paschen α (4→3): λ = 1875 nm (IR). Forbidden 2s→1s: τ ≈ 0.12 s vs allowed transitions τ ≈ ns — 8 orders of magnitude.
- The artifact / what moves: Energy level diagram for n=1 to 6, with ℓ sublevels shown. Click any two levels (start, end): allowed transitions light up in color (Lyman=UV/purple, Balmer=visible gradient, Paschen=IR/red); forbidden transitions show a dashed gray arrow with "FORBIDDEN: Δℓ=0" and the two-photon lifetime. A live spectrum panel (wavelength axis) lights up the corresponding line as you click.
- Output medium: d3 v7 animated/interactive HTML
- Two testable predictions: P1: Balmer α (3p→2s or 3d→2p) at 656.3 nm — check against Rydberg formula; P2: 2s→1s lifetime ≈ 0.12 s vs 2p→1s lifetime ≈ 1.6 ns — ratio ~10⁸, testable against published values.
- The change: toggle on "fine structure" mode — each n,ℓ level splits by spin-orbit coupling (Δℓ±1 pattern breaks into J-sublevels), revealing the sodium D-line doublet structure as a preview of spin-orbit coupling.
- Human supplies (Claude can't): Nothing — fully synthetic/analytic (Rydberg formula + selection rules).
- Teardown angle: The 2s state is metastable (0.12 s lifetime) precisely because the electric-dipole transition is forbidden and only two-photon emission can proceed. This metastability is what makes the 1S-2S two-photon transition so exquisitely measurable — it has been measured to 15 significant figures and used to test CPT symmetry with antihydrogen.
- Exclusions: Do not compute actual dipole matrix elements numerically in-browser. Use the selection rule as a check. Do not include hyperfine structure.
- Sim slug: qm2-hydrogen-transitions
- Score: 7/10
- Status: BUILT — `open /Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-vol2/youtube/qm2-hydrogen-transitions/qm2-hydrogen-transitions.html`
