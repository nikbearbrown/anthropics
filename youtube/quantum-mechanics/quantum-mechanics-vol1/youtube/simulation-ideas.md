# Simulation Ideas — quantum-mechanics-vol1

Medhavy-register "Claude Code + Manim" workflow reels.

---

## Sim-01 — Classical Simulations: Photoelectric / Compton / UV Catastrophe (3-sim reel)
- Source: `quantum-mechanics-vol1/chapters/01-why-classical-physics-failed.md`
- Topic: CLAUDE CODE · MANIM
- Physical rule: K_max=hν−φ; Δλ=(h/m_e c)(1−cosθ); Planck vs Rayleigh-Jeans
- Concrete numbers: Na φ=2.28 eV, 700/546/300 nm photons; λ_C=2.426 pm at 0°/90°/180°; T=3000 K blackbody
- Visual artifact: photon-threshold arrows; Compton collision panels; Planck vs RJ curves
- Two testable predictions: P1: 546 nm blocked by Na (E=2.27<2.28 eV); P2: Compton Δλ doubles from 90° to 180°
- Sim slug: medhavy-ch1-classical-sims
- Status: BUILT — `quantum-mechanics-vol1/youtube/medhavy-ch1-classical-sims/medhavy-ch1-classical-sims-review.mp4`
- Watch: `open /Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-vol1/youtube/medhavy-ch1-classical-sims/medhavy-ch1-classical-sims-review.mp4`

---

## Sim-02 — Infinite Square Well: Energy Ladder and n² Spectrum
- Source: `quantum-mechanics-vol1/chapters/05-the-infinite-square-well.md`
- Topic: CLAUDE CODE · MANIM
- Physical rule: E_n = n²π²ℏ²/(2mL²); boundary conditions force discrete k_n = nπ/L
- Concrete numbers: L=2 nm, m=m_e; E₁≈0.094 eV, E₂≈0.376 eV, E₃≈0.846 eV; ratios 1:4:9:16
- Visual artifact: energy ladder with sine eigenstates; change L and watch E₁ shift as 1/L²
- Two testable predictions: P1: E₂/E₁ = 4.000 exactly (n² spacing); P2: halving L from 2 nm to 1 nm quadruples E₁ from 0.094 eV to 0.376 eV
- Sim slug: medhavy-vol1-pib-spectrum

---

## Sim-03 — Quantum Harmonic Oscillator: Ladder and Zero-Point Energy
- Source: `quantum-mechanics-vol1/chapters/07-the-harmonic-oscillator.md`
- Topic: CLAUDE CODE · MANIM
- Physical rule: E_n = ℏω(n + 1/2); ground state energy ℏω/2 ≠ 0; equally spaced levels
- Concrete numbers: ω = 10¹⁴ rad/s → ℏω ≈ 0.066 eV; ground state 0.033 eV; spacing uniform at ℏω
- Visual artifact: parabolic potential with equally-spaced energy rungs; highlight the non-zero E₀
- Two testable predictions: P1: E₁ − E₀ = E₂ − E₁ = ℏω exactly (uniform spacing); P2: lowest rung at ℏω/2 > 0
- Sim slug: medhavy-vol1-harmonic-ladder

---

## Sim-04 — Wave Packet Spreading: Dispersion in Free Space
- Source: `quantum-mechanics-vol1/chapters/08-the-free-particle-and-wave-packets.md`
- Topic: CLAUDE CODE · MANIM
- Physical rule: σ(t)² = σ₀²/2 + ℏ²t²/(2m²σ₀²); width grows as √(1 + (ℏt/mσ₀²)²)
- Concrete numbers: σ₀=1 nm electron; spreading time τ=mσ₀²/ℏ ≈ 8.6 fs; at t=τ width is σ₀√2
- Visual artifact: Gaussian envelope moving right and visibly broadening over several τ
- Two testable predictions: P1: centroid moves at v = ℏk₀/m (group velocity); P2: at t=τ the packet width exactly doubles (σ=√2 σ₀)
- Sim slug: medhavy-vol1-packet-spread

---

## Sim-05 — 1D Quantum Sandbox: Eigensolver Benchmark
- Source: `quantum-mechanics-vol1/chapters/11-capstone-a-1d-quantum-sandbox.md`
- Topic: CLAUDE CODE · MANIM
- Physical rule: Tridiagonal Hamiltonian H_jj = 2t_k + V_j; H_{j±1,j} = −t_k; t_k = ℏ²/(2mh²)
- Concrete numbers: L=2 nm, N=500 grid points; analytic E₁=0.094 eV; ratio E₂/E₁ must equal 4.000
- Visual artifact: energy level diagram overlaid on the potential; dots at analytic vs numerical levels show near-perfect agreement
- Two testable predictions: P1: E₂/E₁ = 4.000 ± 0.001 (ratio independent of units); P2: fractional error in E₁ < 10⁻⁵ for N=500
- Sim slug: medhavy-vol1-sandbox-benchmark

---

# Quantum Mechanics Vol. 1 — Simulation Candidates (sim-scout run)

---

## Candidate 01 — "Animate the Sloshing State: Quantum Probability in Motion"
- Source: `quantum-mechanics-vol1/chapters/05-the-infinite-square-well.md`
- Topic: Quantum superposition — the sloshing probability packet
- Lane: MANIM (directed animation)
- Hook: A pure energy eigenstate sits frozen forever, but the moment you mix two levels the probability surges left, halts, surges right, and repeats — at femtosecond cadence inside a nanometer box.
- The rule: |Ψ(x,t)|² = ½[ψ₁² + ψ₂² + 2ψ₁ψ₂ cos((E₂−E₁)t/ℏ)]; ⟨x⟩(t) = L/2 − (16L/9π²)cos(ωt); ω = 3E₁/ℏ
- Concrete numbers: L = 1 nm electron; E₁ ≈ 0.377 eV; E₂ ≈ 1.508 eV; beat period T = h/(E₂−E₁) ≈ 3.66 fs; ⟨x⟩ oscillates between 0.320 L and 0.680 L with amplitude 0.360 L
- The artifact / what moves: Three-panel animation — top: |Ψ(x,t)|² blob sloshing left↔right over one full beat period; middle: ⟨x⟩(t) sinusoidal trace building in real time; bottom: ⟨Ĥ⟩(t) flat line proving energy stays fixed while position swings
- Output medium: Manim (mp4)
- Two testable predictions: P1: ⟨x⟩ oscillates at exactly ω = 3E₁/ℏ (not ω₁ or ω₂ separately but their difference); P2: ⟨Ĥ⟩ = (E₁+E₂)/2 = 0.943 eV constant to numerical precision throughout
- The change: Switch to ψ₁+ψ₃ — now ⟨x⟩ stays pinned at L/2 by parity symmetry while |Ψ|² still pulses, revealing a different class of superposition behavior
- Human supplies (Claude can't): Nothing — fully synthetic/analytic
- Teardown angle: The energy budget never moves; only the phase relationship between two fixed clocks changes — that phase shift is everything we call "motion" in quantum mechanics
- Exclusions: Many-state superpositions, decoherence, measurement collapse
- Sim slug: vol1-sloshing-state
- Score: 10/10

---

## Candidate 02 — "Explore the Uncertainty Hyperbola: σ_x × σ_p ≥ ℏ/2"
- Source: `quantum-mechanics-vol1/chapters/03-the-wave-function.md` (+ "LLM Exercise" from ch09)
- Topic: Heisenberg uncertainty principle — the Kennard bound as a live hyperbola
- Lane: D3/DATAVIZ (emergent / interactive)
- Hook: Drag a slider to squeeze the wave packet narrower — watch the momentum distribution explode wider in real time, and see your operating point slide along the uncertainty hyperbola but never cross it.
- The rule: Gaussian σ_x = a/√2, σ_p = ℏ/(√2 a), product = ℏ/2 for all a; infinite-square-well ground state: σ_x ≈ 0.181L, σ_p = ℏπ/L, product ≈ 1.136 × ℏ/2
- Concrete numbers: a slider from 0.2 nm to 4 nm; ℏ = 0.6582 eV·fs; Gaussian sits exactly on σ_xσ_p = ℏ/2; ISW ground state lands at ratio 1.136 on the log-log plot
- The artifact / what moves: Left panel: live |ψ(x)|² and |φ(p)|² Gaussian curves that grow/shrink together as slider moves; Right panel: log-log σ_x vs σ_p scatter with the ℏ/2 hyperbola — Gaussian point glides along curve, ISW point sits above it; readout shows current ratio
- Output medium: d3 v7 animated/interactive HTML
- Two testable predictions: P1: Gaussian always sits at ratio = 1.000 regardless of a (can be verified by reading the readout at any slider position); P2: Infinite-square-well ground state point (pre-computed, shown as fixed marker) sits at ratio ≈ 1.136 — above the hyperbola but never below
- The change: Toggle between Gaussian, ISW n=1, and ISW n=5 state points — shows ratio growing as ~n·π/√3 for large n, making the classical approach visible
- Human supplies (Claude can't): Nothing — fully synthetic/analytic
- Teardown angle: The bound is not a measurement disturbance story — it is a geometric constraint on the shape of any normalizable function, encoded in Fourier analysis before any experiment begins
- Exclusions: Error-disturbance (Ozawa) formulation, Robertson for Pauli matrices
- Sim slug: vol1-uncertainty-hyperbola
- Score: 9/10
- Status: BUILT — `open /Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-vol1/youtube/vol1-uncertainty-hyperbola/vol1-uncertainty-hyperbola.html`

---

## Candidate 03 — "Animate Quantum Tunneling: Wave Function Through a Forbidden Wall"
- Source: `quantum-mechanics-vol1/chapters/06-finite-wells-steps-and-barriers.md`
- Topic: Quantum tunneling — rectangular barrier transmission
- Lane: MANIM (directed animation)
- Hook: The particle has 1 eV; the wall is 5 eV high. Classical physics says full stop. The wave function disagrees — a tiny exponentially damped tail leaks through and launches a real transmitted wave on the far side.
- The rule: T_exact = [1 + V₀²sinh²(κL) / 4E(V₀−E)]⁻¹; κ = √(2m(V₀−E))/ℏ; thick-barrier limit T ≈ (16E(V₀−E)/V₀²)·e^{−2κL}
- Concrete numbers: E = 1 eV, V₀ = 5 eV, L = 5 Å, m = mₑ; κ ≈ 1.025 Å⁻¹; κL = 5.125; T_exact ≈ 9.1×10⁻⁵; WKB T ≈ 3.5×10⁻⁵; ratio = prefactor 2.56 exactly
- The artifact / what moves: Left-to-right time evolution showing: oscillating ψ in region I, exponentially decaying amplitude inside barrier (region II), small but non-zero oscillating transmitted wave in region III; probability current arrows showing rightward net flow in region III despite zero current in evanescent region
- Output medium: Manim (mp4)
- Two testable predictions: P1: T_exact / T_WKB = 16E(V₀−E)/V₀² = 2.56 for E=1 eV, V₀=5 eV (prefactor check); P2: doubling L to 10 Å drops T_WKB by e^{−10.25} ≈ 1.25×10⁻⁹ (four additional orders of magnitude)
- The change: Sweep barrier width from 2 Å to 10 Å and show T on a log axis — the exponential collapse of T with L is the STM sensitivity story
- Human supplies (Claude can't): Nothing — fully synthetic/analytic
- Teardown angle: The particle borrows no energy — total energy E is constant and labeled throughout; the decay inside the barrier is a real-exponential solution to a valid ODE, not a forbidden region in any mathematical sense
- Exclusions: Time-energy uncertainty borrowing narrative, Gamow alpha-decay full calculation, resonant tunneling diode
- Sim slug: vol1-tunneling-barrier
- Score: 9/10

---

## Candidate 04 — "Watch Probability Slosh: Single-Electron Double-Slit Buildup"
- Source: `quantum-mechanics-vol1/chapters/02-matter-waves.md`
- Topic: Wave-particle duality — single-electron double-slit interference buildup
- Lane: MANIM (directed animation)
- Hook: Each electron lands as one dot. Ten dots look random. By 70,000 dots the pattern is unmistakable — but no two electrons ever met. The interference is the wave function interfering with itself.
- The rule: Born rule I(x) ∝ |ψ₁(x) + ψ₂(x)|² = |ψ₁|² + |ψ₂|² + 2Re(ψ₁*ψ₂); fringe spacing Δx = λL/d; de Broglie λ = h/p
- Concrete numbers: Electron at 54 eV → λ = 0.167 nm; slit separation d = 500 nm; screen distance L = 50 cm → Δx ≈ 167 μm; show buildup at 10, 200, 6000, 70000 electrons (Tonomura 1989 counts)
- The artifact / what moves: Animated detector screen: dots accumulate one by one as Poisson draws from |ψ|² distribution; running histogram builds underneath; fringe visibility statistic displayed in corner climbing from noise to >90%
- Output medium: Manim (mp4)
- Two testable predictions: P1: fringe spacing Δx = λL/d ≈ 167 μm for the given parameters — measurable from the accumulated pattern; P2: fringe visibility approaches 1.0 as N→∞ (fully coherent superposition), regardless of the random order of individual events
- The change: Block one slit — fringes disappear and replace with a single broad Gaussian; unblock and fringes return — demonstrating that both slits must be open simultaneously even for a single electron
- Human supplies (Claude can't): Nothing — fully synthetic/analytic
- Teardown angle: The interference pattern is not the electrons talking to each other — it is the squared modulus of a single complex amplitude that passed through both slits simultaneously
- Exclusions: Which-way experiments, quantum eraser, Bell inequalities
- Sim slug: vol1-double-slit-buildup
- Score: 9/10

---

## Candidate 05 — "Explore Tunneling Transmission: Interactive Barrier Lab"
- Source: `quantum-mechanics-vol1/chapters/06-finite-wells-steps-and-barriers.md` (+ "LLM Exercise" ch6 Q4, Q6)
- Topic: Barrier transmission — exact formula vs. WKB, resonances above barrier
- Lane: D3/DATAVIZ (emergent / interactive)
- Hook: Below the barrier T looks vanishingly small — but drag the energy slider above V₀ and T doesn't jump to 1: it oscillates, hitting 1 only at resonances where the barrier width is an integer half-wavelength, exactly like an anti-reflection coating.
- The rule: T_exact = [1 + V₀²sinh²(κL)/4E(V₀−E)]⁻¹ for E<V₀; T_exact = [1 + V₀²sin²(k₂L)/4E(E−V₀)]⁻¹ for E>V₀; resonances at k₂L = nπ
- Concrete numbers: V₀ = 2 eV, L = 1 nm, m = mₑ; resonances at E = V₀ + n²π²ℏ²/2mL² ≈ 2 + 0.376n² eV; first resonance at ≈ 2.376 eV; log(T) ranges from −12 to 0
- The artifact / what moves: Three sliders (E, V₀, L) update T(E) curve in real time on log y-axis; a vertical cursor shows current (E, T) point; WKB approximation shown as dashed overlay; resonance peaks above barrier flash when T = 1 exactly; STM sensitivity readout: "one extra Å changes T by factor ×7"
- Output medium: d3 v7 animated/interactive HTML
- Two testable predictions: P1: first above-barrier resonance at E = V₀ + π²ℏ²/2mL² (can be verified by dragging E until T readout = 1.000); P2: in thick-barrier limit, T_exact/T_WKB = 16E(V₀−E)/V₀² — confirm numerically at E=1 eV, V₀=5 eV, L=5Å reading 2.56
- The change: Set L → 0: barrier disappears and T → 1 for all E; set L → large: T below barrier → 0 exponentially while resonances above remain at T=1
- Human supplies (Claude can't): Nothing — fully synthetic/analytic
- Teardown angle: The resonances above the barrier reveal that quantum mechanics does not simply let particles through when E > V₀ — the barrier's width and the particle's wavelength inside the barrier together gate the transmission, exactly like a Fabry-Pérot cavity
- Exclusions: Double barrier / resonant tunneling diode device physics, time-dependent tunneling (attosecond experiments)
- Sim slug: vol1-barrier-explorer
- Score: 9/10
- Status: BUILT — `open /Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-vol1/youtube/vol1-barrier-explorer/vol1-barrier-explorer.html`

---

## Candidate 06 — "Animate Phase vs. Group Velocity: The Crests That Lag the Packet"
- Source: `quantum-mechanics-vol1/chapters/08-the-free-particle-and-wave-packets.md`
- Topic: Wave packet dispersion — phase velocity vs. group velocity for a free particle
- Lane: MANIM (directed animation)
- Hook: The probability blob moves at the classical particle speed — but the individual wave crests inside it move at exactly half that speed. Watch new crests appear at the back of the packet and vanish at the front as the envelope outruns its own internal oscillation.
- The rule: ω(k) = ℏk²/2m; v_ph = ω/k = ℏk/2m = v_cl/2; v_g = dω/dk = ℏk₀/m = v_cl; ratio v_g/v_ph = 2 exactly
- Concrete numbers: k₀ = 5 nm⁻¹ electron; v_g = ℏk₀/mₑ ≈ 5.78×10⁵ m/s; v_ph = v_g/2 ≈ 2.89×10⁵ m/s; σ₀ = 1 nm; doubling time τ = 2mₑσ₀²/ℏ ≈ 17.2 fs; carrier wavelength λ = 2π/k₀ ≈ 1.26 nm
- The artifact / what moves: Two-layer animation: |Ψ(x,t)|² orange envelope advances at v_g; Re(Ψ) blue oscillation advances at v_ph = v_g/2; labeled arrows track one specific crest that enters from the rear of the packet and exits at the front; simultaneously the envelope broadens per the spreading formula
- Output medium: Manim (mp4)
- Two testable predictions: P1: v_g/v_ph = 2.000 exactly for free electron (measure crest speed vs. envelope centroid speed from the animation); P2: at t = τ ≈ 17.2 fs the envelope width is √2 × σ₀ = 1.414 nm (measurable from the width display)
- The change: Change the mass to a proton (1836×mₑ) — v_g drops 43×, spreading slows by 1836×, making the packet nearly classical
- Human supplies (Claude can't): Nothing — fully synthetic/analytic
- Teardown angle: The phase velocity is not where the particle is — a detector in the path records the envelope (the probability), not the crests; tracking the wrong velocity gives a speed that predicts where the particle is not
- Exclusions: Relativistic dispersion (light in a medium), negative group velocity, slow light
- Sim slug: vol1-phase-vs-group
- Score: 9/10

---

## Candidate 07 — "Explore the Blackbody Spectrum: Planck vs. Rayleigh-Jeans"
- Source: `quantum-mechanics-vol1/chapters/01-why-classical-physics-failed.md`
- Topic: UV catastrophe — Planck distribution beats Rayleigh-Jeans by 20 orders of magnitude
- Lane: D3/DATAVIZ (emergent / interactive)
- Hook: The classical curve looks identical to Planck at long wavelengths — then drag the temperature slider up and watch the Rayleigh-Jeans line blast off to infinity while Planck's curve turns over and falls exponentially, exactly as every hot object in the room refuses to kill you with ultraviolet radiation.
- The rule: u(ν,T) = (8πhν³/c³)·1/(e^{hν/kT}−1) [Planck]; u_RJ(ν,T) = (8πν²/c³)·kT [Rayleigh-Jeans]; ratio = (hν/kT)/(e^{hν/kT}−1); peak at hν_max = 2.821 kT
- Concrete numbers: T slider 1000–10000 K; T=3000 K: peak at λ≈966 nm (IR), T=5778 K: peak at 501 nm (green-visible); ratio Planck/RJ at ν=3×10¹⁵ Hz, T=3000 K equals ≈7×10⁻²⁰ (20 orders of magnitude); Wien peak frequency linear in T
- The artifact / what moves: Two animated curves update in real time as T slider moves: Planck curve (blue) sweeps and peaks shift right with T; Rayleigh-Jeans (red dashed) rises linearly without bound; shaded area under Planck = finite; shaded area under RJ indicated as ∞; dimensionless x = hν/kT marked; vertical line at current peak ν_max tracks Wien's law
- Output medium: d3 v7 animated/interactive HTML
- Two testable predictions: P1: Wien peak frequency ν_max doubles when T doubles (linear relation — verifiable by setting T=3000 K and T=6000 K and reading the peak position); P2: at x=hν/kT ≪ 1 the ratio Planck/RJ approaches 1.000 (the two curves overlap at low frequency regardless of T — confirm by zooming into the low-ν region)
- The change: Switch x-axis to wavelength — the peak in wavelength does NOT map to ν_max via λ=c/ν, showing that the density-per-wavelength and density-per-frequency peak at different points (a famous subtlety)
- Human supplies (Claude can't): Nothing — fully synthetic/analytic
- Teardown angle: The classical formula is not "a little wrong" in the UV — it is wrong by a factor that grows like e^x, reaching 10²⁰ at room temperature for UV light; the failure is not approximate, it is categorical
- Exclusions: Derivation of Planck's formula from statistical mechanics, Bose-Einstein distribution, CMB measurements
- Sim slug: vol1-planck-vs-rj
- Score: 8/10
- Status: BUILT — `open /Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-vol1/youtube/vol1-planck-vs-rj/vol1-planck-vs-rj.html`

---

## Candidate 08 — "Animate the Stationary-State Clock: Re and Im Oscillate, |Ψ|² Doesn't"
- Source: `quantum-mechanics-vol1/chapters/04-the-schrodinger-equation.md`
- Topic: Stationary states — the rotating phase that leaves probability frozen
- Lane: MANIM (directed animation)
- Hook: The wave function is spinning in the complex plane at 10¹⁵ revolutions per second — yet the probability distribution is completely static. The "stationary" state is a clock whose shadow never moves.
- The rule: Ψ_n(x,t) = ψ_n(x)·e^{−iEₙt/ℏ}; |Ψ_n|² = |ψ_n|² (time-independent); Re(Ψ) = ψ_n cos(Eₙt/ℏ); Im(Ψ) = −ψ_n sin(Eₙt/ℏ); 90° phase-shifted oscillation
- Concrete numbers: Infinite-well n=1, L=1 nm: E₁=0.377 eV, period T=h/E₁ ≈ 11 fs; n=2: E₂=1.508 eV, T≈2.75 fs; show at t=0, T/4, T/2, 3T/4, T — Re and Im swap roles, |Ψ|² identical at all five snapshots
- The artifact / what moves: Three-row animation: Row 1 (Re Ψ in orange) oscillates between +ψ_n and −ψ_n; Row 2 (Im Ψ in blue dashed) oscillates 90° behind; Row 3 (|Ψ|² filled) sits completely still; a phase-clock inset shows the rotating complex phasor; time counter runs
- Output medium: Manim (mp4)
- Two testable predictions: P1: |Ψ|² at t=T/4 is identical to |Ψ|² at t=0 to numerical precision (stationary means exactly stationary); P2: Re(Ψ) at t=T/4 equals Im(Ψ) at t=0 up to a sign — the two components are exactly 90° out of phase
- The change: Switch to the two-state superposition — |Ψ|² now moves, demolishing the stationarity and confirming it was the pure eigenstate that caused the freezing
- Human supplies (Claude can't): Nothing — fully synthetic/analytic
- Teardown angle: A stationary state is not a particle sitting still — it is a particle whose probability distribution happens to be time-invariant, while its wave function churns in the complex plane at a fixed rate set by its energy
- Exclusions: Measurement collapse on a stationary state, decoherence, mixed states
- Sim slug: vol1-stationary-clock
- Score: 8/10

---

## Candidate 09 — "Explore Finite Well Bound States: How Many Levels Fit?"
- Source: `quantum-mechanics-vol1/chapters/06-finite-wells-steps-and-barriers.md` (+ "LLM Exercise" ch6 Q1, Q7)
- Topic: Finite square well — graphical bound-state counting and evanescent tails
- Lane: D3/DATAVIZ (emergent / interactive)
- Hook: Make the well deeper — a new bound state pops into existence the moment the quarter-circle on the graphical solution sweeps past a new tangent branch. One more level, discretely, like a new stair appearing under your foot.
- The rule: Even states: √(z₀²−z²) = z·tan(z); odd states: √(z₀²−z²) = −z·cot(z); z₀ = (L/2ℏ)√(2mV₀); bound-state count N ≈ z₀/(π/2) rounded up; always at least 1 state
- Concrete numbers: L = 1 nm, m = mₑ; V₀ slider 0–10 eV; z₀ = (L/2ℏ)√(2mₑV₀); at V₀=1 eV: z₀≈2.56, 2 states; at V₀=5 eV: z₀≈5.73, 4 states; at V₀→∞: levels approach infinite-well values from below
- The artifact / what moves: Left panel: quarter-circle of radius z₀ sweeps as V₀ increases; tangent and cotangent branches fixed; intersection dots light up as new bound states appear; Right panel: wave functions drawn for each level with evanescent tails visible outside the well; penetration depth 1/κ labeled
- Output medium: d3 v7 animated/interactive HTML
- Two testable predictions: P1: even as V₀→0, exactly 1 bound state always exists (quarter-circle always touches first tangent branch — observable by dragging V₀ to near-zero and seeing one dot remain); P2: bound-state energies approach infinite-well values from below as V₀→∞ (toggle switch adds infinite-well reference lines and shows convergence)
- The change: Narrow the well (decrease L): same V₀ can support fewer states — reveals the (V₀L²) dependence through z₀
- Human supplies (Claude can't): Nothing — fully synthetic/analytic
- Teardown angle: The finite number of bound states is not a failure of the infinite-well model — it is a richer truth: a well of finite depth simply cannot hold arbitrarily many levels, and quantum particles leak into the forbidden region with a penetration depth that grows as the level approaches the continuum
- Exclusions: Scattering states (continuum), nuclear physics applications requiring relativistic corrections
- Sim slug: vol1-finite-well-explorer
- Score: 8/10
- Status: BUILT — `open /Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-vol1/youtube/vol1-finite-well-explorer/vol1-finite-well-explorer.html`

---

## Candidate 10 — "Explore the Bloch Sphere: Rotating Qubit States and Measurement Statistics"
- Source: `quantum-mechanics-vol1/chapters/10-measurement-and-the-qubit.md`
- Topic: Qubit measurement — Born rule on the Bloch sphere
- Lane: D3/DATAVIZ (emergent / interactive)
- Hook: Drag the state vector anywhere on the Bloch sphere — the three measurement probability bar charts update instantly, and the Robertson uncertainty bound for σ_x vs σ_z tightens and loosens as you rotate, saturating exactly when you point along the y-axis.
- The rule: |ψ⟩ = cos(θ/2)|0⟩ + e^{iφ}sin(θ/2)|1⟩; Bloch vector (sin θ cos φ, sin θ sin φ, cos θ); P(σ_z=+1) = cos²(θ/2); Robertson: σ_{σ_x}·σ_{σ_z} ≥ |⟨σ_y⟩|
- Concrete numbers: θ=π/3, φ=π/2: P(σ_z=+1)=3/4, P(σ_z=−1)=1/4, P(σ_x=±1)=1/2, P(σ_y=+1)≈0.933; Robertson bound saturated at exactly √3/2; equatorial states (θ=π/2) give P(σ_z)=50/50 for any φ
- The artifact / what moves: 3D Bloch sphere with draggable state vector; three grouped bar charts update live for σ_x, σ_y, σ_z probabilities; Robertson product σ_xσ_z and bound |⟨σ_y⟩| displayed as two numbers with inequality; saturation indicator flashes when the state is a σ_y eigenstate
- Output medium: d3 v7 animated/interactive HTML
- Two testable predictions: P1: at any equatorial point (θ=π/2), P(σ_z=+1) = P(σ_z=−1) = 0.500 exactly regardless of φ (verifiable by dragging around the equator); P2: Robertson bound is saturated (both sides equal) precisely when the state vector points along the y-axis (θ=π/2, φ=π/2 or 3π/2)
- The change: Run repeated "virtual measurements" — click Measure and watch the state collapse to the north or south pole with the Born-rule probability; re-prepare and measure again; histogram accumulates Born rule empirically
- Human supplies (Claude can't): Nothing — fully synthetic/analytic
- Teardown angle: The Bloch sphere makes visible what the algebra hides — the relative phase φ is physically real (it shifts σ_x and σ_y probabilities) while the global phase is not (rotating the overall phase leaves all three bar charts unchanged)
- Exclusions: Mixed states (density matrix), entanglement, two-qubit gates
- Sim slug: vol1-bloch-sphere
- Score: 8/10
- Status: BUILT — `open /Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-vol1/youtube/vol1-bloch-sphere/vol1-bloch-sphere.html`

---

## Candidate 11 — "Animate the Coherent State: The Gaussian That Never Spreads"
- Source: `quantum-mechanics-vol1/chapters/07-the-harmonic-oscillator.md`
- Topic: Coherent states — minimum-uncertainty Gaussian riding the classical orbit
- Lane: MANIM (directed animation)
- Hook: Every free-particle Gaussian spreads and smears — but inside the harmonic potential, there exists one special Gaussian that rides its classical orbit forever without changing shape. This is how a laser photon lives in a mode of the electromagnetic field.
- The rule: |α(t)⟩ = e^{−|α|²/2}Σ (α(t))^n/√n! |n⟩; α(t) = α₀e^{−iωt}; ⟨x(t)⟩ = √(2ℏ/mω)|α|cos(ωt − arg α); σ_x σ_p = ℏ/2 at all times; Poisson photon-number distribution P(n) = e^{−|α|²}|α|^{2n}/n!
- Concrete numbers: ω = 10¹⁴ rad/s; |α| = 3 (mean occupation ⟨n⟩=9); x₀ = √(2ℏ/mₑω)·3 ≈ 0.63 nm amplitude; σ_x = √(ℏ/2mₑω) ≈ 0.074 nm constant throughout; period T = 2π/ω ≈ 62.8 fs
- The artifact / what moves: Side-by-side: Left panel — coherent state |Ψ(x,t)|² Gaussian slides back and forth along the parabola without changing width for 3 full periods; Right panel — free-particle Gaussian (same initial σ) spreads until it fills the screen; width meter beneath each shows left = flat, right = growing
- Output medium: Manim (mp4)
- Two testable predictions: P1: σ_x(t) = constant = √(ℏ/2mω) ≈ 0.074 nm for the coherent state at all times (width meter flat); P2: ⟨x(t)⟩ = x₀ cos(ωt) exactly — same as a classical particle on a parabolic potential (overlay classical trajectory and confirm coincidence)
- The change: Start with a slightly displaced eigenstate (not the coherent state) — it also rides the parabola but σ_x oscillates at 2ω (breathing mode), demonstrating that the non-spreading is unique to the coherent state
- Human supplies (Claude can't): Nothing — fully synthetic/analytic
- Teardown angle: The coherent state is special not because it is semiclassical but because the restoring force of the potential exactly cancels the dispersive spreading — two physics mechanisms with a perfect balance that holds to all time
- Exclusions: Squeezed states, quantum optics photon statistics measurement, laser mode theory
- Sim slug: vol1-coherent-state
- Score: 8/10

---

## Candidate 12 — "Explore de Broglie Wavelengths: From Electrons to Buckyballs"
- Source: `quantum-mechanics-vol1/chapters/02-matter-waves.md` (+ "LLM Exercise" ch2 Q6)
- Topic: de Broglie relation — wavelength vs. mass/energy on a logarithmic scale
- Lane: D3/DATAVIZ (emergent / interactive)
- Hook: Drag the mass slider from electron to C₆₀ buckyball to a marble — the de Broglie wavelength plummets 35 orders of magnitude, crossing from "diffractable by crystals" to "unmeasurable by any instrument ever built," and the slider makes you feel every decade.
- The rule: λ = h/p = h/√(2mK); for thermal particles K ≈ (3/2)kT; λ_electron = 1.226 nm/√V (V in volts)
- Concrete numbers: Electron at 54 eV: λ=0.167 nm (crystal diffraction range); thermal neutron at 293 K: λ≈1.46 Å; C₆₀ at 900 K: λ≈2.5 pm (smaller than the molecule!); 70 kg person at 1 m/s: λ≈10⁻³⁵ m; proton radius ≈10⁻¹⁵ m for reference
- The artifact / what moves: Log-axis slider for mass (10⁻³⁰ to 10⁰ kg) and energy (0.01 eV to 1 keV); λ readout updates live; a reference bar marks crystal-plane spacing (0.1 nm), visible light (400–700 nm), proton radius; color-coded "diffractable" / "borderline" / "classically invisible" zones; particle identity labels pop as you pass canonical values
- Output medium: d3 v7 animated/interactive HTML
- Two testable predictions: P1: at V=54 V, the electron shortcut λ≈1.226/√54 = 0.167 nm matches the full formula (verify by setting m=mₑ, K=54 eV — both routes must agree to 3 sig figs); P2: C₆₀ at 900 K thermal velocity gives λ≈2.5 pm — smaller than the ~0.7 nm molecular diameter (counterintuitive: the wavelength is smaller than the object that diffracts)
- The change: Fix mass, vary temperature — shows that λ ∝ T^{−1/2} for thermal particles, and locates the temperature where quantum effects turn on (λ ≈ interparticle spacing)
- Human supplies (Claude can't): Nothing — fully synthetic/analytic
- Teardown angle: The de Broglie wavelength of a buckyball is smaller than the buckyball itself — yet it diffracts. The wavelength is not the size of the particle; it is a property of the state of motion
- Exclusions: Relativistic corrections for high-energy electrons, internal molecular vibrations, thermal de Broglie wavelength in statistical mechanics
- Sim slug: vol1-debroglie-scale
- Score: 7/10
- Status: BUILT — `open /Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-vol1/youtube/vol1-debroglie-scale/vol1-debroglie-scale.html`

---

## Candidate 13 — "Animate Born's Rule: Probability Current and the Continuity Equation"
- Source: `quantum-mechanics-vol1/chapters/03-the-wave-function.md`
- Topic: Probability current — conservation law for |Ψ|²
- Lane: MANIM (directed animation)
- Hook: The wave function spreads but total probability stays locked at exactly 1.000 — because probability flows like a fluid, and the continuity equation prevents any leakage. Watch the current arrows show where probability is flowing even as the density redistributes.
- The rule: ∂|Ψ|²/∂t = −∂J/∂x; J(x,t) = (ℏ/m)Im(Ψ*∂Ψ/∂x); ∫|Ψ|²dx = 1 for all t; for a rightward Gaussian J > 0 in the high-probability region
- Concrete numbers: Gaussian Ψ(x,0) with σ₀=1 nm, k₀=5 nm⁻¹, mₑ; J_peak = ℏk₀/(mₑ)·|Ψ|²_peak ≈ 5.78×10⁵ m/s × (nm⁻¹); show normalization integral staying at 1.000±0.001 over 5 spreading times; probability current arrow field overlaid on the density
- The artifact / what moves: Three-panel animation: Top: |Ψ(x,t)|² spreading Gaussian with colored regions; Middle: J(x,t) arrow field showing rightward flow in the high-density region; Bottom: running normalization integral displayed as a flat line at 1.000 with ±0.001 tolerance band; a "probability meter" box on the left half shows how much probability is there vs. the right half, redistributing as the packet moves
- Output medium: Manim (mp4)
- Two testable predictions: P1: ∫|Ψ|²dx = 1.000 at every animation frame (the flat line never moves); P2: for a real-valued wave function with k₀=0, J=0 everywhere (no current arrows appear — confirm by starting with a stationary Gaussian and watching all arrows disappear)
- The change: Replace Gaussian with the sloshing superposition from Ch. 5 — J becomes alternating left/right in different regions, showing how the same conservation law governs a more complex probability flow
- Human supplies (Claude can't): Nothing — fully synthetic/analytic
- Teardown angle: Normalization is not maintained by definition or by rescaling — it is a theorem derived from the Schrödinger equation; the continuity equation is the mechanism, and a non-unitary time stepper (explicit Euler) visibly breaks it within 50 steps
- Exclusions: Probability current in 3D (gradient form), spin currents, electromagnetic analogy in detail
- Sim slug: vol1-probability-current
- Score: 7/10

---

## Candidate 14 — "Animate Potential Step Reflection: Quantum Impedance Mismatch"
- Source: `quantum-mechanics-vol1/chapters/06-finite-wells-steps-and-barriers.md`
- Topic: Potential step — partial quantum reflection above the barrier
- Lane: MANIM (directed animation)
- Hook: The particle has twice the energy needed to clear the step — classically it sails through. Quantum mechanically, a reflected wave appears from nowhere at the step edge, exactly like light reflecting from glass even when it has more than enough energy to enter.
- The rule: R = ((k₀−k₁)/(k₀+k₁))²; T = 4k₀k₁/(k₀+k₁)²; k₀=√(2mE)/ℏ, k₁=√(2m(E−V₀))/ℏ; R+T=1; R=0 only when V₀=0
- Concrete numbers: E = 2V₀ (double the barrier): k₁ = k₀/√2; R = (1−1/√2)²/(1+1/√2)² ≈ 0.029; T ≈ 0.971; even with E=4V₀: R ≈ 0.003 — never zero; incident wave amplitude A=1, reflected B/A=(k₀−k₁)/(k₀+k₁)
- The artifact / what moves: Time-evolving wave packet (Gaussian) strikes the step: incident rightward packet; small reflected leftward packet appears; larger transmitted packet moves right at reduced amplitude; amplitude labels show |B/A| and |C/A|; R+T meter confirms sum = 1.000; repeat for step-down (V₀<0) to show reflection also occurs there
- Output medium: Manim (mp4)
- Two testable predictions: P1: R+T = 1.000 at all times (probability current conservation — displayed continuously); P2: for a step downward (V₀<0) with E=3 eV, V₀=−1 eV: R=(k₀−k₁)²/(k₀+k₁)²=((1−√(4/3))/(1+√(4/3)))²≈0.005 — nonzero reflection even for energy increase
- The change: Make the step abrupt vs. smooth (tapered over one wavelength) — smooth step reduces R toward zero, showing that reflection depends on the sharpness of the impedance mismatch, not the sign or magnitude of V₀ alone
- Human supplies (Claude can't): Nothing — fully synthetic/analytic
- Teardown angle: There is no energy argument that explains the reflection — the particle has more than enough energy; the reflection is purely a wave phenomenon arising from the mismatch in spatial frequency k at the boundary
- Exclusions: Step below threshold (evanescent case), Fabry-Pérot resonances, optical thin-film coatings (though the analogy is worth one sentence)
- Sim slug: vol1-step-reflection
- Score: 7/10

---

## Candidate 15 — "Animate Ehrenfest's Theorem: The Centroid That Obeys Newton"
- Source: `quantum-mechanics-vol1/chapters/09-operators-and-uncertainty.md`
- Topic: Ehrenfest theorem — quantum expectation values obeying classical equations of motion
- Lane: MANIM (directed animation)
- Hook: The probability blob spreads and smears — yet its center of mass moves in a perfect parabola, exactly as Newton would predict. Quantum mechanics hides a classical particle inside every spreading wave packet.
- The rule: d⟨x⟩/dt = ⟨p⟩/m (exact); d⟨p⟩/dt = −⟨∂V/∂x⟩ (exact); for a harmonic potential V = mω²x²/2, these become d²⟨x⟩/dt² = −ω²⟨x⟩ — identical to the classical oscillator equation of motion
- Concrete numbers: Gaussian wave packet in a harmonic well: ω = 10¹⁴ rad/s, m = mₑ; initial ⟨x⟩₀ = 0.5 nm off-center; ⟨x⟩(t) = 0.5 nm · cos(ωt) exactly; period T = 2π/ω ≈ 62.8 fs; packet width σ_x constant (coherent state); for a free particle: ⟨x⟩(t) = ⟨x⟩₀ + (⟨p⟩₀/m)t linear in t; d⟨p⟩/dt = 0 exactly since V = 0 → ⟨∂V/∂x⟩ = 0
- The artifact / what moves: Two-panel side-by-side animation. Left panel — free particle: |Ψ(x,t)|² Gaussian envelope moves right and spreads; centroid marker (red dot) rides the peak tracing a straight line; classical particle (orange dot) overlaid follows same straight line — both dots coincide to pixel accuracy. Right panel — harmonic oscillator: |Ψ(x,t)|² bounces back and forth on the parabola without spreading; centroid traces a cosine; classical trajectory overlaid is identical. Below each panel: a time-trace of ⟨x⟩(t) building in real time confirming exact match
- Output medium: Manim (mp4)
- Two testable predictions: P1: for the free particle, ⟨x⟩(t) = ⟨x⟩₀ + (ℏk₀/m)t = ⟨x⟩₀ + v_g·t — the centroid displacement at t = τ = mσ₀²/ℏ ≈ 8.6 fs is exactly v_g·τ = ℏk₀τ/m, computable from known parameters; P2: for the harmonic oscillator (coherent state), ⟨x⟩(t) completes exactly one full cycle in T = 2π/ω ≈ 62.8 fs and returns to 0.5 nm — the centroid period is identical to the classical frequency, not 2ω or ω/2
- The change: Switch to an anharmonic potential V = mω²x²/2 + λx⁴ — now d⟨p⟩/dt = −mω²⟨x⟩ − 4λ⟨x³⟩ ≠ −mω²⟨x⟩ because ⟨x³⟩ ≠ ⟨x⟩³; the centroid drifts away from the classical orbit over several periods, demonstrating where the quantum-classical correspondence breaks down
- Human supplies (Claude can't): Nothing — fully synthetic/analytic
- Teardown angle: Ehrenfest's theorem proves classical mechanics is inside quantum mechanics — but only for the averages. The individual measurement outcomes are still quantum-random; it is only the mean that follows Newton. The spread of outcomes is the quantum residue that classical mechanics throws away
- Exclusions: Many-body Ehrenfest (mean-field approximation), non-Ehrenfest behavior (wave packet bifurcation in double wells), WKB connection
- Sim slug: vol1-ehrenfest-centroid
- Score: 10/10

---

## Candidate 16 — "Animate Sequential Stern-Gerlach: How Measurement Erases Certainty"
- Source: `quantum-mechanics-vol1/chapters/10-measurement-and-the-qubit.md`
- Topic: Measurement collapse — sequential Stern-Gerlach destroys prior spin certainty
- Lane: MANIM (directed animation)
- Hook: Filter a beam to pure spin-up — measure again and it's still spin-up, probability 1.000. Now measure spin-x first, then spin-z again — and the spin-up certainty you had is completely gone. One measurement in the middle can erase everything a prior measurement established.
- The rule: Collapse postulate: after measuring Ŝ_z = +ℏ/2, state → |↑⟩; P(↑|↑) = 1. Then Ŝ_x eigenstates: |+x⟩ = (|↑⟩ + |↓⟩)/√2, |−x⟩ = (|↑⟩ − |↓⟩)/√2; from |↑⟩: P(+x) = P(−x) = 1/2. After collapse to |+x⟩: P(↑ from Z) = |⟨↑|+x⟩|² = 1/2. Commutator [σ_x, σ_z] = −2iσ_y ≠ 0 is the algebraic cause
- Concrete numbers: Three sequential arrangements, all exact probabilities — Z→Z: P(↑) = 1.000 exactly; Z→X→Z: P(+x after Z↑) = 0.500 exactly, P(↑ after +x) = 0.500 exactly; Z→X(both)→Z: filtering neither X output still gives P(↑) = 0.500 — the X apparatus has permanently randomized the Z outcome regardless of which X channel was selected. Contrast with Z→Z→Z where P(↑) = 1.000 at every stage
- The artifact / what moves: Three-panel stacked animation, each panel a horizontal beam-splitting sequence. Panel 1 (Z→Z): initial beam splits into thin lower and thick upper beams; thick upper feeds into second Z magnet; one single output beam emerges — labeled P=1.000. Panel 2 (Z→X→Z): thick upper beam → X magnet splits 50/50 → one branch feeds final Z magnet → two equal beams emerge labeled P=0.500 each. Panel 3 (Z→X→Z with both X branches merged): both X branches rejoin before final Z — still two equal Z outputs. The beam thickness visually encodes probability at each stage. Probabilities animate as numerical labels building in real time
- Output medium: Manim (mp4)
- Two testable predictions: P1: in the Z→X→Z sequence, P(↑ from final Z) = 0.500 exactly regardless of which X branch is selected — computable from ⟨↑|+x⟩ = 1/√2 and ⟨↑|−x⟩ = 1/√2, both giving |·|² = 0.500; P2: in the Z→Z sequence, P(↑ from second Z) = 1.000 exactly because the collapsed state |↑⟩ is an eigenstate of Ŝ_z — confirmed by ⟨↑|↑⟩ = 1 and P = |1|² = 1.000, not 0.999 or "approximately 1"
- The change: Replace the middle apparatus with a Z apparatus (Z→Z→Z) — the output is P(↑) = 1.000 at every stage; inserting a commuting observable does not erase certainty, only a non-commuting one does
- Human supplies (Claude can't): Nothing — fully synthetic/analytic
- Teardown angle: The erasure is not due to mechanical disturbance by the X apparatus — even if the X deflection force is negligibly small, the Z certainty is gone. The cause is algebraic: [σ_x, σ_z] ≠ 0. The commutator predicts the physical beam pattern before any apparatus enters the lab
- Exclusions: Quantum eraser (restoring coherence), weak measurements, many-worlds interpretation, density matrix formalism for mixed states
- Sim slug: vol1-stern-gerlach-sequential
- Score: 9/10
