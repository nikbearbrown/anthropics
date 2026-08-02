# Physics: Quantum Mechanics — Simulation Ideas

**Pilot run: MANIM lane only. D3/DATAVIZ pass follows after human approval.**
*sim-scout run 2026-07-26 — all 17 chapters read.*

---

## Candidate 01 — Animate "Gaussian Wave Packet Spreading: Uncertainty Product Evolving in Time"
- Source: `physics-quantum-mechanics/chapters/01-the-wave-function.md`
- Topic: Wave Function / Uncertainty Principle
- Lane: MANIM (directed animation)
- Hook: A perfectly localized particle is impossible — not because of limited instruments, but because of quantum mechanics. Watch a narrow Gaussian sharpen to near-certainty in position, then watch it spread. σxσp never falls below ℏ/2.
- The rule: Free-particle Gaussian: ψ(x,0)=(2πa²)^{−1/4} e^{−x²/4a²}; at time t: σx(t)=a√(1+(ℏt/2ma²)²); σp=ℏ/2a (constant); product σxσp=ℏ/2 at t=0 (minimum uncertainty state), grows with t; probability density |ψ(x,t)|² remains Gaussian but broadens
- Concrete numbers: Electron, a=1 nm: σp=0.053 eV/c; σx(t=0)=1 nm; spreading time τ=2ma²/ℏ=1.8 fs; at t=τ: σx=1.41 nm (width doubled); proton (1836× heavier) same a → τ=3.3 ps (1836× slower spreading)
- The artifact / what moves: |ψ(x,t)|² draws as a tall narrow Gaussian at t=0; time advances — the peak lowers, the width grows, the area stays exactly 1 (normalization preserved); two vertical markers track ±σx, visibly separating; a second panel shows σx(t) growing as hyperbola; σp(t) flat line; product σxσp on a third mini-panel starting at ℏ/2, rising above it; side-by-side comparison: electron vs proton at same t shows proton barely moved
- Output medium: Manim (mp4)
- Two testable predictions: P1: Spreading rate σx(t)/σx(0) = √(1+(t/τ)²) — at t=τ, σx exactly √2 times initial width (checkable algebraically); P2: Momentum-space wavefunction |φ(p)|² stays constant (time-independent Gaussian with σp=ℏ/2a) — the uncertainty is in position only; momentum width never grows
- The change: Compare two initial widths: a=1 nm (narrow → fast spreading) vs a=10 nm (broad → slow spreading) — demonstrates the trade-off: tighter initial localization means faster delocalization, the heart of uncertainty
- Human supplies (Claude can't): Nothing — fully synthetic/analytic; Gaussian integral, free-particle propagator
- Teardown angle: The wave packet spreading is not a failure of the description — it IS the description. A particle prepared in a sharp position has a broad momentum distribution; broad momentum means a broad range of velocities; the packet spreads because the particle's own momentum is uncertain
- Exclusions: Derivation of Born rule from measurement axioms; density matrix formalism; position operator eigenstates as delta functions; Wigner function; path integral formulation
- Sim slug: qm-gaussian-spreading
- Score: 9/10

---

## Candidate 02 — Animate "Infinite Square Well: Quantization from Boundary Conditions"
- Source: `physics-quantum-mechanics/chapters/02-the-time-independent-schrodinger-equation.md`
- Topic: Quantum Wells / Energy Quantization
- Lane: MANIM (directed animation)
- Hook: Why can't you put an electron at rest in a box? Because the boundary conditions force nodes. Every energy level is exactly n² times the ground state — not approximately, exactly. Watch the nodes appear as n climbs.
- The rule: ψn(x)=√(2/L) sin(nπx/L); En=n²π²ℏ²/(2mL²)=n²E₁; node count = n−1; orthogonality ∫ψm ψn dx = δmn; ground-state energy E₁=1.504 eV/L² (in nm) for electron
- Concrete numbers: L=1 nm electron box: E₁=0.376 eV, E₂=1.504 eV, E₃=3.385 eV, E₄=6.018 eV; E₄/E₁=16 exactly; L=0.1 nm (nuclear scale): E₁=37.6 MeV (explains nuclear confinement energy); n=1: zero nodes; n=2: one node at L/2; n=5: four nodes at L/5, 2L/5, 3L/5, 4L/5
- The artifact / what moves: Box walls materialize; ψ₁ draws — smooth half-sine, one lobe; energy level E₁ drawn as horizontal dashed line on the energy axis; n increments to 2: ψ₂ draws, one node at center, energy level E₂=4E₁ appears (gap doubles); n=3: two nodes, E₃=9E₁; sequence continues to n=6; at each step, node positions are marked with red dots; energy spacing labeled to show n² pattern; a |ψn|² panel beside shows probability density — for large n, density flattening toward classical uniform distribution
- Output medium: Manim (mp4)
- Two testable predictions: P1: E₄/E₁ = 16 exactly (4² = 16) — the energy ratios are perfect squares, checkable from the formula to any precision; P2: Node positions for ψn are exactly at x = kL/n for k=1,…,n−1 — for n=4, nodes at L/4, L/2, 3L/4, all checkable
- The change: Shrink L from 1 nm to 0.1 nm (nuclear scale) — E₁ jumps from 0.376 eV to 37.6 MeV, demonstrating why nucleon confinement energies are in the MeV range while atomic electron energies are in the eV range (100,000× ratio from 10× smaller box, squared)
- Human supplies (Claude can't): Nothing — fully synthetic/analytic; sine functions and algebra
- Teardown angle: The infinite square well is the simplest quantum system that explains why atoms exist at all — electrons cannot collapse to zero energy in a bound state because the wave must fit. The ground-state energy is the zero-point energy the uncertainty principle enforces
- Exclusions: Finite square well (tunneling tails); transmission resonances; 3D box and degeneracy; quantum dot applications; periodic potential and band structure
- Sim slug: qm-infinite-square-well
- Score: 9/10

---

## Candidate 03 — Animate "Two-State Sloshing: ⟨x⟩(t) Oscillates, ⟨H⟩ Does Not"
- Source: `physics-quantum-mechanics/chapters/02-the-time-independent-schrodinger-equation.md`
- Topic: Quantum Dynamics / Superposition
- Lane: MANIM (directed animation)
- Hook: An electron in a superposition of two energy states is not in either state — but its average position genuinely oscillates back and forth at the beat frequency. Energy stays constant. Position sloshes. Watch both.
- The rule: Ψ(x,t)=(1/√2)(ψ₁e^{−iE₁t/ℏ} + ψ₂e^{−iE₂t/ℏ}); |Ψ|²=½|ψ₁|²+½|ψ₂|²+ψ₁ψ₂cos((E₂−E₁)t/ℏ); ⟨x⟩(t) oscillates at angular frequency ω=(E₂−E₁)/ℏ; ⟨H⟩=(E₁+E₂)/2 (constant); beat period T=2πℏ/(E₂−E₁)
- Concrete numbers: Infinite square well, L=1 nm electron: E₁=0.376 eV, E₂=1.504 eV; beat frequency f=(E₂−E₁)/h=272 THz; period T=3.67 fs; ⟨x⟩ oscillates between ~0.35 nm and ~0.65 nm; ⟨H⟩=0.94 eV constant
- The artifact / what moves: Top panel: |Ψ(x,t)|² animates in real time — probability density sloshes left-right like a sloshing wave, beat frequency 272 THz; a dot marking ⟨x⟩(t) rides the moving hump; bottom panel: ⟨x⟩(t) plot draws — sinusoidal, period T=3.67 fs; beside it ⟨H⟩(t) flat line; third panel shows both ψ₁ (fixed shape) and ψ₂ (fixed shape) contributing, with their time-dependent phase factors rotating in the complex plane — the cross term responsible for the oscillation visualized as two phasors beating
- Output medium: Manim (mp4)
- Two testable predictions: P1: Beat period T=2πℏ/(E₂−E₁)=3.67 fs for L=1 nm electron — measurable in principle by ultrafast spectroscopy; P2: ⟨x⟩(t) oscillation amplitude is 2⟨x⟩₁₂/π where ⟨x⟩₁₂=∫ψ₁xψ₂dx — for infinite square well this evaluates to 16L/9π²≈0.18L, checkable analytically
- The change: Switch to an equal superposition of ψ₁ and ψ₃ — the beat frequency doubles (E₃−E₁=9E₁−E₁=8E₁ vs E₂−E₁=3E₁), period 3× shorter, and the sloshing pattern becomes asymmetric (involves a symmetric+symmetric superposition that doesn't move the mean); shows how the parity selection controls which superpositions create motion
- Human supplies (Claude can't): Nothing — fully synthetic/analytic; time-dependent Schrödinger equation exact solution for ISW superposition
- Teardown angle: This is the quantum model of absorption — an electromagnetic field oscillating at the beat frequency can drive transitions between levels. The oscillating dipole moment ⟨x⟩(t) is what couples to the photon. Quantum mechanics shows you the oscillator before you need classical EM
- Exclusions: Perturbation theory derivation of transition rates; Rabi oscillations; Fermi's golden rule; decoherence and why macroscopic objects don't slosh
- Sim slug: qm-two-state-slosh
- Score: 9/10

---

## Candidate 04 — Animate "Harmonic Oscillator: Eigenstates, Turning Points, and Classical Correspondence"
- Source: `physics-quantum-mechanics/chapters/03-the-harmonic-oscillator.md`
- Topic: Quantum Harmonic Oscillator
- Lane: MANIM (directed animation)
- Hook: A quantum harmonic oscillator's ground state spills beyond where a classical ball would stop — and is most likely to be found at the center, not the edges. A classical ball is never at the center. Watch the two descriptions converge as n grows.
- The rule: ψn(x) ∝ Hn(αx) e^{−α²x²/2} where α=(mω/ℏ)^{1/4}; En=(n+½)ℏω equally spaced; classical turning points x_tp=±√(2En/mω²)=±√(2n+1)/α; classical probability density ∝ 1/√(x_tp²−x²); n→∞: |ψn|² → classical shape (Bohr correspondence)
- Concrete numbers: H₂ molecule: ω=8.0×10¹³ rad/s, ℏω=0.527 eV, zero-point E₀=0.264 eV; n=0: single Gaussian peak at center; n=1: two peaks with central node; n=10: 10 oscillations, turning-point peaks emerging; n=50: |ψ|² nearly matches classical distribution
- The artifact / what moves: Parabolic V(x) draws; equally spaced energy levels E₀ through E₅ appear as horizontal dashed lines; |ψn|² for n=0 draws — centered Gaussian; classical probability (∝ 1/v) for same energy draws in dashed orange — bimodal, zero at center; the quantum-classical mismatch labeled; n increments 0→1→2→5→10→20→50 — |ψn|² evolves, oscillations multiply, envelope converges toward classical shape; at n=20 both curves visibly matching except near turning points; classical turning point markers ±x_tp extend with n
- Output medium: Manim (mp4)
- Two testable predictions: P1: Zero-point energy E₀=ℏω/2 — for H₂ this is 0.264 eV, measurable from vibrational spectroscopy ground-state position (never reaches E=0 even at 0 K); P2: Equally spaced energy levels En=(n+½)ℏω — IR absorption spectrum shows single peak at frequency ω/2π with no anharmonic splitting (for small n); verified in diatomic molecular spectra
- The change: Add harmonic oscillator ladder operators visually — show â₋|ψn⟩ → √n|ψ_{n−1}⟩ as an animation that lowers the state one rung and rescales the wavefunction, then â₊ raises it back; illustrates why ladder operators are the fast path to all wavefunctions
- Human supplies (Claude can't): Nothing — fully synthetic/analytic; Hermite polynomials computed exactly
- Teardown angle: The harmonic oscillator appears everywhere in physics because everything near a stable equilibrium is a harmonic oscillator to first approximation. The zero-point energy is not a rounding error — it means the vacuum itself has energy in every quantum field, and that vacuum energy is real (it powers the Casimir effect)
- Exclusions: Coherent states derivation; Wigner function negativity for excited states; 3D isotropic oscillator; ladder operator algebra derivation; anharmonic corrections to molecular spectra
- Sim slug: qm-harmonic-oscillator-correspondence
- Score: 9/10

---

## Candidate 05 — Animate "Hydrogen Radial Probability: r_mp vs ⟨r⟩ and the Missing Peak"
- Source: `physics-quantum-mechanics/chapters/07-the-hydrogen-atom.md`
- Topic: Hydrogen Atom / Radial Probability
- Lane: MANIM (directed animation)
- Hook: The most probable distance from the proton in the hydrogen ground state is exactly one Bohr radius. But the average distance is 1.5 Bohr radii. The probability distribution is not symmetric — and the difference tells you why ⟨1/r⟩ ≠ 1/⟨r⟩.
- The rule: Radial wave function R₁₀(r)=2a₀^{−3/2}e^{−r/a₀}; probability density P(r)=|R₁₀|²r²=4r²a₀^{−3}e^{−2r/a₀}; r_mp=a₀ (from dP/dr=0); ⟨r⟩=3a₀/2; ⟨r²⟩=3a₀² (so rms=a₀√3); for n,ℓ states: ⟨r⟩=a₀[3n²−ℓ(ℓ+1)]/2
- Concrete numbers: a₀=0.0529 nm; r_mp(1s)=0.0529 nm; ⟨r⟩(1s)=0.0794 nm; ⟨r⟩(2s)=6a₀=0.317 nm; ⟨r⟩(2p)=5a₀=0.265 nm; ⟨r⟩(3d)=7a₀=0.370 nm; energy E₁=−e²/2a₀=−13.6 eV (⟨1/r⟩=1/a₀ for 1s)
- The artifact / what moves: r-axis draws (0 to 6a₀); |ψ₁s|²∝e^{−2r/a₀} draws first — monotone decreasing, maximum at r=0; then the r² volume factor draws as an upward-curving parabola; their product P(r)=r²|R|² draws — bell-shaped, peak at r=a₀ labeled; two vertical dashed lines: one at r_mp=a₀, one at ⟨r⟩=1.5a₀ — visibly different positions; n increments to 2s, 2p: curves redraw, showing how ⟨r⟩ grows and the 2s curve has a node while 2p does not; a side-by-side comparison for all n=1,2,3 states
- Output medium: Manim (mp4)
- Two testable predictions: P1: ⟨r⟩=1.5a₀ for the 1s state — calculable exactly from ∫₀^∞ r·P(r)dr = 3a₀/2; P2: ⟨r⟩(2p)/⟨r⟩(1s) = 5a₀/a₀ = 5 — the 2p state is on average 5 Bohr radii from the nucleus, 5× farther than the ground state
- The change: Show the difference ⟨r⟩−r_mp for n=1,2,3 — the asymmetry grows with n, quantifying the skewness of the radial distribution; connects to why the Bohr model's most-probable radius matches but the average energy cannot be computed from it naively
- Human supplies (Claude can't): Nothing — fully synthetic/analytic; radial wavefunctions from standard hydrogen solution
- Teardown angle: Students conflate most-probable and average. They are not the same, and the difference matters — ⟨E⟩ is set by ⟨1/r⟩, not 1/⟨r⟩, and Jensen's inequality guarantees they differ. The probability distribution is the physics, not the label
- Exclusions: Angular wavefunctions and spherical harmonics; spin-orbit coupling; Zeeman effect; hyperfine structure; multielectron atoms and screening
- Sim slug: qm-hydrogen-radial-probability
- Score: 9/10

---

## Candidate 06 — Animate "Hydrogen 1s→2pz Superposition: Oscillating Electric Dipole"
- Source: `physics-quantum-mechanics/chapters/07-the-hydrogen-atom.md`
- Topic: Hydrogen Atom / Optical Transitions
- Lane: MANIM (directed animation)
- Hook: An atom in a superposition of ground state and an excited p-state has a charge distribution that oscillates. That oscillating charge is an antenna. It emits a photon at the Lyman-alpha frequency. Watch the electron cloud slosh.
- The rule: Ψ=c₁ψ₁₀₀e^{-iE₁t/ℏ}+c₂ψ₂₁₀e^{-iE₂t/ℏ}; |Ψ|² oscillates at ω₁₂=(E₂−E₁)/ℏ; ⟨z⟩(t)=2Re[c₁c₂*⟨z⟩₁₂]cos(ω₁₂t); selection rule Δℓ=±1 comes from ⟨z⟩₁₂≠0 only for Δℓ=±1; Lyman-α: E₂−E₁=10.2 eV, λ=121.6 nm
- Concrete numbers: ω₁₂=(E₂−E₁)/ℏ=1.55×10¹⁶ rad/s; period T=405 as (attoseconds); ⟨z⟩₁₂=−√(128/243)a₀≈−0.745a₀; ⟨z⟩(t) amplitude ≈1.49 c₁c₂a₀; Lyman-α λ=121.6 nm; for 1s→2s: ⟨z⟩₁₂=0 (selection rule forbids it)
- The artifact / what moves: Cross-section of |Ψ|²(x,z,t) in the xz-plane renders as a color map; at t=0 the distribution is spherically lopsided toward +z (1s+2pz dominant); as time advances (compressed by 10¹⁶×) the charge cloud visibly oscillates — bulging toward +z, then centering, then bulging −z — at the Lyman-α beat frequency; ⟨z⟩(t) traces out a sinusoid below; then switch to 1s+2s: the map shows radial breathing but no net dipole oscillation — the selection-rule-forbidden case made visible
- Output medium: Manim (mp4)
- Two testable predictions: P1: Selection rule Δℓ=±1 — ⟨z⟩₁₂=0 exactly for 1s→2s (both ℓ=0), so no oscillating dipole, no photon; for 1s→2p this matrix element is −0.745a₀, nonzero; P2: Lyman-α frequency f=ω₁₂/2π=2.47×10¹⁵ Hz → λ=c/f=121.6 nm — checked against ultraviolet spectroscopy tables
- The change: Switch to 2pz→3dz² (Balmer series): visualize the next selection-rule-allowed transition, showing the charge distribution oscillating between a dumbbell and a double-cone shape — the geometry of Δℓ=+1 is different from Δℓ=−1
- Human supplies (Claude can't): Nothing — fully synthetic/analytic; hydrogen wavefunctions standard closed-form; matrix element computed analytically
- Teardown angle: The "quantum jump" is not instantaneous — while the atom is in a superposition, there is a real oscillating charge distribution that radiates. Quantum mechanics explains where the photon comes from. It comes from the beating of two states, and the beat creates the antenna
- Exclusions: Wigner-Eckart theorem; angular momentum algebra derivation of selection rules; forbidden transitions; natural linewidth and lifetime; stimulated vs spontaneous emission
- Sim slug: qm-hydrogen-dipole-oscillation
- Score: 9/10

---

## Candidate 07 — Animate "WKB Wave Packet Tunneling: Splitting at a Rectangular Barrier"
- Source: `physics-quantum-mechanics/chapters/11-the-wkb-approximation-and-tunneling.md`
- Topic: Quantum Tunneling / WKB Approximation
- Lane: MANIM (directed animation)
- Hook: A quantum wave packet hits a barrier higher than its kinetic energy. Classically: it bounces 100%. Quantum mechanically: part of it leaks through. Watch the packet split, the transmitted piece emerge on the far side, and the transmitted fraction match the Gamow formula.
- The rule: WKB tunneling probability T≈e^{−2γ} where γ=(1/ℏ)∫_{x₁}^{x₂}√(2m(V₀−E))dx; for rectangular barrier of width L: γ=κL where κ=√(2m(V₀−E))/ℏ; reflection R=1−T; Crank-Nicolson (or split-operator) for time-dependent packet
- Concrete numbers: Electron, E=1 eV, V₀=2 eV, L=0.5 nm: κ=5.13 nm⁻¹, γ=2.56, T=e^{−5.13}≈0.006 (0.6% transmitted); L=0.2 nm same: T=e^{−2.05}≈0.13 (13% transmitted); alpha particle through Coulomb barrier: T≈e^{−87}≈10⁻³⁸ per nuclear vibration; nuclear vibration rate 10²¹/s → macroscopic half-life
- The artifact / what moves: Gaussian wave packet moves rightward; rectangular barrier V₀>E drawn as grey wall; packet approaches, collides — reflected wave packet forms moving left, transmitted wave packet forms moving right (smaller amplitude), evanescent region inside barrier shows exponential decay; transmitted probability computed and displayed: T=0.006 at L=0.5 nm; barrier width slider: L decreases → T increases rapidly; T vs L curve on a side panel shows exponential relationship; energy slider: E→V₀ → T→1 (barrier becomes transparent at resonance)
- Output medium: Manim (mp4)
- Two testable predictions: P1: T=e^{−2κL} — doubling barrier width from 0.2 to 0.4 nm squares the transmission (T₂=T₁²), so T drops from 13% to 1.7%; exact, checkable; P2: At E=V₀ (classically at the top of the barrier), WKB gives T=1 but exact quantum mechanics gives T=1/(1+m²V₀²L²/2ℏ²E)<1 — the discrepancy is a signature of the WKB approximation's failure at the classical turning point, checkable by comparing formulas
- The change: Replace rectangular barrier with a Coulomb barrier V∝1/r — show that the wider, softer barrier still tunnels but T is now governed by the Gamow integral; link to radioactive decay where the barrier shape determines the half-life
- Human supplies (Claude can't): Nothing — fully synthetic/analytic; split-operator or Crank-Nicolson time-stepping for the packet; WKB formula closed-form for rectangular case
- Teardown angle: Quantum tunneling is not a metaphor — it is the mechanism of scanning tunneling microscopy, the alpha decay of radioactive elements, the proton-proton fusion that powers the Sun, and the operation of tunnel diodes in your electronics. The packet splits and part of it arrives where it had no right to be
- Exclusions: Full derivation of WKB connection formulas at classical turning points; resonant tunneling (quantum well double-barrier); Josephson junction and superconducting tunneling; tunneling ionization; STM image formation
- Sim slug: qm-wkb-tunneling-packet
- Score: 9/10

---

## Candidate 08 — Animate "Geiger-Nuttall Plot: 24 Decades of Half-Life from One Straight Line"
- Source: `physics-quantum-mechanics/chapters/11-the-wkb-approximation-and-tunneling.md`
- Topic: Alpha Decay / Gamow Factor
- Lane: MANIM (directed animation)
- Hook: The half-lives of alpha emitters span 24 orders of magnitude — from microseconds to billions of years. Every data point falls on the same straight line when plotted as log t_{1/2} vs 1/√E_α. That line is the Gamow factor in disguise.
- The rule: Gamow factor G≈π Z₁Z₂e²/(ℏv_α) − correction; log t_{1/2} = A/√E_α + B (constants A,B depend on Z); T=e^{−2G} per barrier crossing; decay rate λ=f×T where f≈10²¹ Hz (nuclear vibration); t_{1/2}=ln2/λ
- Concrete numbers: ²³²Th: E_α=4.08 MeV, t_{1/2}=1.4×10¹⁰ yr; ²³⁸U: E_α=4.27 MeV, t_{1/2}=4.47×10⁹ yr; ²²⁶Ra: E_α=4.87 MeV, t_{1/2}=1600 yr; ²¹⁰Po: E_α=5.30 MeV, t_{1/2}=138 days; ²¹⁴Po: E_α=7.69 MeV, t_{1/2}=164 μs; ²¹²Po: E_α=8.78 MeV, t_{1/2}=298 ns — spanning 24 orders of magnitude
- The artifact / what moves: Two axes: y=log₁₀(t_{1/2}/s), x=1/√E_α (MeV^{-½}); data points appear one by one in increasing E_α order — each labeled with nuclide name; as each appears, the best-fit straight line (Geiger-Nuttall line) extends to accommodate it; the span of 24 decades is annotated (y from −7 to +17); a second panel shows E_α vs Z — the Z-dependence of the slope (heavier nuclei have steeper slope because Coulomb barrier is taller); residuals panel shows all points within 2 decades of the line despite the 24-decade range
- Output medium: Manim (mp4)
- Two testable predictions: P1: Log t_{1/2} vs 1/√E_α is linear for any fixed-Z series — confirmed for uranium isotopes (Z=92) with slope A=130 MeV^{1/2}; P2: A 0.5 MeV increase in E_α reduces half-life by ~4 orders of magnitude (from the exponential sensitivity of the Gamow factor) — checkable between Ra-226 (4.87 MeV, 1600 yr) and Po-210 (5.30 MeV, 138 days): ΔE=0.43 MeV, ratio≈4300×, ≈4 orders of magnitude
- The change: Show the Geiger-Nuttall line for different Z values (Z=82 Pb isotopes vs Z=92 U isotopes) — lines are parallel but displaced, confirming the Z-dependence of the intercept B while the slope structure is the same
- Human supplies (Claude can't): Nothing — fully synthetic/analytic; Geiger-Nuttall data from published nuclear data tables; all values tabulated in standard references
- Teardown angle: Geiger and Nuttall found this empirical law in 1911, before quantum mechanics. Gamow's 1928 derivation of quantum tunneling explained it. A 24-decade straight line that two people found empirically, explained by a 19-year-old's theory: that is what it looks like when a physical law is real
- Exclusions: Full Gamow integral derivation; barrier penetration in nuclear reactions (fusion cross sections); spontaneous fission; beta-decay correlations
- Sim slug: qm-geiger-nuttall-plot
- Score: 9/10

---

## Candidate 09 — Animate "CHSH Bell Inequality: Classical Bound Broken by Quantum Correlations"
- Source: `physics-quantum-mechanics/chapters/12-entanglement-and-quantum-information.md`
- Topic: Quantum Entanglement / Bell Inequality
- Lane: MANIM (directed animation)
- Hook: No local hidden variable theory can produce correlations stronger than S=2. Quantum mechanics predicts S=2√2≈2.83. The experiment gives 2.77. Watch the S(θ) curve rise above the classical line and into territory nature is not supposed to reach.
- The rule: Bell state |Φ⁺⟩=(|00⟩+|11⟩)/√2; correlation E(a,b)=⟨σ_a⊗σ_b⟩=−cos(a−b); CHSH: S=|E(a₁,b₁)−E(a₁,b₂)+E(a₂,b₁)+E(a₂,b₂)|; classical: |S|≤2; quantum maximum at a₁=0°, a₂=45°, b₁=22.5°, b₂=67.5°: S=2√2; local realism satisfied iff |S|≤2
- Concrete numbers: Optimal angles: a₁=0°, a₂=90°, b₁=45°, b₂=135°; E(0°,45°)=−cos(45°)=−1/√2; S=2√2=2.828; classical bound S=2; Aspect 1981 experiment: S=2.697±0.015 (11σ above classical); Zeilinger 2022 (Nobel): S=2.67 (loophole-free); quantum prediction S=2.828
- The artifact / what moves: Two measurement stations drawn at distance; a shared entangled pair emitted between them; angle dial for each station rotates; E(θ)=−cos(θ) correlation curve draws on a single axis — smooth cosine, ±1 range; CHSH quantity S computed from four points on the curve; classical bound S=2 drawn as horizontal dashed line; angles set to optimal values: four E values plotted, S=2√2 computed visually; then θ₁ sweeps from 0° to 180° while θ₂ stays at 22.5° — S(θ₁) curve draws, rising above S=2 in a bump centered at the optimal angle
- Output medium: Manim (mp4)
- Two testable predictions: P1: At optimal angles, S=2√2=2.828>2, violating the classical bound by (2√2−2)/2=41%; P2: For a=b (same measurement angle on both detectors), E(a,a)=−cos(0)=−1 — perfect anti-correlation; for a=b+90°, E=0 — no correlation; exact, checkable from the −cos formula
- The change: Replace |Φ⁺⟩ with a product state |00⟩ (separable, no entanglement) — E(a,b) becomes independent of angle (both always 0), S=0, far below the classical bound; demonstrates that entanglement is required to reach the classical bound, let alone exceed it
- Human supplies (Claude can't): Nothing — fully synthetic/analytic; correlation function E(a,b)=−cos(a−b) for singlet/Bell state; Aspect and Zeilinger experimental values from published papers (public record)
- Teardown angle: For 30 years physicists argued about whether loopholes invalidated Bell tests. Zeilinger and colleagues closed every loophole by 2015. The universe is not locally real. This is the most precisely tested prediction in physics, and the answer is: spooky action at a distance is real
- Exclusions: Derivation of CHSH from local realism; quantum key distribution (E91 protocol); quantum teleportation; GHZ state and other Bell inequalities; many-worlds vs Copenhagen implications
- Sim slug: qm-chsh-bell-violation
- Score: 9/10

---

## Candidate 10 — Animate "Coherent State Orbit: Gaussian Riding the Classical Phase-Space Circle"
- Source: `physics-quantum-mechanics/chapters/03-the-harmonic-oscillator.md`
- Topic: Harmonic Oscillator / Coherent States
- Lane: MANIM (directed animation)
- Hook: A laser field is a coherent state — a quantum state that moves exactly like a classical oscillator, with the same shape forever. Watch the Gaussian probability packet orbit in phase space without spreading, while an energy eigenstate sits still.
- The rule: Coherent state |α⟩=e^{−|α|²/2}∑(αⁿ/√n!)|n⟩; ⟨x⟩(t)=√(2ℏ/mω)|α|cos(ωt−φ); ⟨p⟩(t)=−√(2mℏω)|α|sin(ωt−φ); σx=√(ℏ/2mω) (constant); σp=√(mℏω/2) (constant); minimum uncertainty σxσp=ℏ/2 maintained at all times
- Concrete numbers: Optical mode ω=10¹⁴ rad/s, |α|=3: ⟨x⟩ amplitude A=3√(2ℏ/mω_ph)≈macroscopic; σx=√(ℏ/2mω); phase-space circle radius |α|=3 in units of ground-state width; energy ⟨E⟩=(|α|²+½)ℏω=9.5ℏω; Poisson distribution of photon number n with mean ⟨n⟩=|α|²=9
- The artifact / what moves: Phase-space (x, p) axes; energy eigenstate |n=9⟩ drawn as a ring at fixed radius — it does not move; coherent state |α=3⟩ drawn as a localized Gaussian blob; blob orbits the phase-space circle at frequency ω, maintaining its Gaussian shape throughout; x(t) projection below shows sinusoidal ⟨x⟩(t) with constant width uncertainty band; energy distribution panel shows Poisson distribution of n values peaked at n=9; comparison panel: energy eigenstate in phase space is delocalized ring (angular uncertainty total); coherent state is localized orbiting blob
- Output medium: Manim (mp4)
- Two testable predictions: P1: σx(t)=√(ℏ/2mω) constant throughout orbit — the Gaussian width never changes; P2: σxσp=ℏ/2 at all times — minimum uncertainty maintained, unlike wave packet spreading of a free particle; exact, checkable from the coherent state algebra
- The change: Let the state evolve with weak damping (add small imaginary part to ω to simulate cavity loss) — the orbit spirals inward toward the ground state, showing how a laser field decays into vacuum while remaining coherent throughout
- Human supplies (Claude can't): Nothing — fully synthetic/analytic; coherent state algebra from ladder operators
- Teardown angle: A laser is a coherent state, not a stream of photons in fixed number states. Coherent states are the closest quantum mechanics comes to classical fields. They behave classically because they saturate the uncertainty principle at every instant — and that is why classical EM works for macroscopic fields
- Exclusions: Derivation of coherent states from displacement operator; Wigner function negativity (squeezed states); optical homodyne detection; quantum optics applications; photon statistics and Hanbury Brown-Twiss
- Sim slug: qm-coherent-state-orbit
- Score: 8/10

---

## Candidate 11 — Animate "Hydrogen Orbital Gallery: Cross-Sections for (n,ℓ,m) with Node Counting"
- Source: `physics-quantum-mechanics/chapters/07-the-hydrogen-atom.md`
- Topic: Hydrogen Atom / Orbital Structure
- Lane: MANIM (directed animation)
- Hook: The 2p orbital's dumbbell shape is not arbitrary — it contains exactly one nodal plane and no radial nodes, because (n−ℓ−1)=0 and ℓ=1. Watch the node structure appear from the quantum numbers.
- The rule: ψ_{nℓm}(r,θ,φ)=R_{nℓ}(r)Y_ℓ^m(θ,φ); radial nodes = n−ℓ−1; angular nodes = ℓ; total nodes = n−1; |ψ|² cross-section in xz-plane; selection rule Δℓ=±1,Δm=0,±1
- Concrete numbers: 1s (n=1,ℓ=0,m=0): 0 nodes, spherical; 2s (n=2,ℓ=0,m=0): 1 radial node at r=2a₀, spherical; 2p (n=2,ℓ=1,m=0): 0 radial nodes, 1 nodal plane (xy), dumbbell; 3d (n=3,ℓ=2,m=0): 0 radial nodes, 2 nodal cones, cloverleaf; 4f: 3 angular nodes
- The artifact / what moves: Grid of cross-sections: rows n=1,2,3; columns ℓ=0,1,2; each cross-section draws as a color map of |ψ|² in the xz-plane; node lines drawn over each panel — radial nodes as dashed circles, angular nodes as dashed cones/planes; node count labeled (n−ℓ−1 radial, ℓ angular, total n−1); sequence: 1s→2s (radial node appears)→2p (angular node appears)→3s→3p→3d; transitions allowed by Δℓ=±1 drawn as arrows between panels
- Output medium: Manim (mp4)
- Two testable predictions: P1: Total node count for any state = n−1 — 1s has 0, 3d has 2, 4f has 3; exact, derivable from the polynomial degree of the wavefunction; P2: The 2s orbital has a radial node at r=2a₀ — verifiable from R₂₀(r)=0 at r=2a₀ exactly (the Laguerre polynomial zero)
- The change: Add m quantum number variation — show 2p_{m=0} (dumbbell along z) vs 2p_{m=±1} (toroids in xy-plane) cross-sections side by side; all three have the same energy (degenerate) but completely different spatial structure
- Human supplies (Claude can't): Nothing — fully synthetic/analytic; cross-sections computed from standard hydrogen wavefunctions
- Teardown angle: The orbital shapes are not electron paths — they are probability amplitudes squared. The dumbbell is not where the electron goes; it is where, if you measured, you would most likely find it. And the shape comes from two integers: n and ℓ
- Exclusions: Stern-Gerlach spin-orbit coupling; relativistic fine structure; multielectron screening and Slater's rules; molecular orbital theory; density functional theory
- Sim slug: qm-hydrogen-orbital-gallery
- Score: 8/10

---

## Summary

| # | Title | Lane | Score | Slug |
|---|---|---|---|---|
| 01 | Gaussian Wave Packet Spreading | MANIM | 9/10 | qm-gaussian-spreading |
| 02 | Infinite Square Well Quantization | MANIM | 9/10 | qm-infinite-square-well |
| 03 | Two-State Sloshing | MANIM | 9/10 | qm-two-state-slosh |
| 04 | Harmonic Oscillator Correspondence | MANIM | 9/10 | qm-harmonic-oscillator-correspondence |
| 05 | Hydrogen Radial Probability | MANIM | 9/10 | qm-hydrogen-radial-probability |
| 06 | Hydrogen 1s→2pz Dipole Oscillation | MANIM | 9/10 | qm-hydrogen-dipole-oscillation |
| 07 | WKB Wave Packet Tunneling | MANIM | 9/10 | qm-wkb-tunneling-packet |
| 08 | Geiger-Nuttall 24-Decade Line | MANIM | 9/10 | qm-geiger-nuttall-plot |
| 09 | CHSH Bell Inequality Violation | MANIM | 9/10 | qm-chsh-bell-violation |
| 10 | Coherent State Phase-Space Orbit | MANIM | 8/10 | qm-coherent-state-orbit |
| 11 | Hydrogen Orbital Gallery | MANIM | 8/10 | qm-hydrogen-orbital-gallery |

**Build-soon (≥9/10):** Candidates 01–09 (nine cards). All are self-contained, fully synthetic, and animate core QM results that state-based teaching cannot show.

**D3/DATAVIZ pass (future):** Interactive quantum measurement simulator (choose basis, watch Born-rule statistics accumulate); phase-space Wigner function drag-viewer; eigenstate superposition explorer with basis switching.
