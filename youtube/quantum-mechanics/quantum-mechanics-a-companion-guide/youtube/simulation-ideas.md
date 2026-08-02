# Simulation Ideas — quantum-mechanics-a-companion-guide

Medhavy-register "Claude Code + Manim" workflow reels. The physics is the excuse;
the lesson is the prompt→read→run→check→change loop.

---

## Sim-01 — Photoelectric Threshold (3-sim reel)
- Source: `quantum-mechanics-a-companion-guide/chapters/01-why-quantum-mechanics.md`
- Topic: CLAUDE CODE · MANIM
- Physical rule: K_max = hν − φ; threshold at ν₀ = φ/h
- Concrete numbers: Na work function φ = 2.28 eV; photons at 700 nm (1.77 eV, blocked), 546 nm (2.27 eV, blocked), 300 nm (4.13 eV, K = 1.85 eV ejected)
- Visual artifact: three photon arrows (red, green, UV) hitting a sodium surface; red/green produce ✗, UV launches an electron arrow scaled as √K
- Two testable predictions: P1: 546 nm (E = 2.27 eV < φ) → zero electrons even at maximum intensity; P2: 300 nm (E = 4.13 eV) → K = 1.85 eV, electron speed ∝ √1.85
- Sim slug: medhavy-companion-photoelectric
- Note: CROSS-REFERENCE — this concept is built in quantum-mechanics-vol1/youtube/medhavy-ch1-classical-sims (B01–B04). Do not rebuild; link to that reel.

---

## Sim-02 — Compton Scattering (cross-reference)
- Source: `quantum-mechanics-a-companion-guide/chapters/01-why-quantum-mechanics.md`
- Physical rule: Δλ = (h/m_e c)(1 − cos θ), λ_C = 2.426 pm
- Note: CROSS-REFERENCE — built in quantum-mechanics-vol1/youtube/medhavy-ch1-classical-sims (B05–B08). Do not rebuild.

---

## Sim-03 — UV Catastrophe (cross-reference)
- Source: `quantum-mechanics-a-companion-guide/chapters/01-why-quantum-mechanics.md`
- Physical rule: Planck ρ(ν) = 8πhν³/c³ · 1/(e^(hν/kT)−1) vs Rayleigh-Jeans ρ_RJ = 8πν²kT/c³
- Note: CROSS-REFERENCE — built in quantum-mechanics-vol1/youtube/medhavy-ch1-classical-sims (B09–B12). Do not rebuild.

---

## Sim-04 — Particle in a Box: Zero-Point Energy and n² Spectrum
- Source: `quantum-mechanics-a-companion-guide/chapters/04-one-dimensional-problems.md`
- Topic: CLAUDE CODE · MANIM
- Physical rule: E_n = n²π²ℏ²/(2mL²); ground state at n=1, never zero
- Concrete numbers: L = 1 nm, electron: E₁ ≈ 0.376 eV, E₂ ≈ 1.504 eV, E₃ ≈ 3.384 eV; ratios 1:4:9
- Visual artifact: energy ladder with sine-wave eigenfunctions drawn at each rung; squeezing L visibly raises E₁
- Two testable predictions: P1: E₂/E₁ = 4.000 exactly; P2: halving L quadruples E₁ (E₁ ∝ 1/L²)
- Sim slug: medhavy-companion-pib
- Status: BUILT
- Watch: `open /Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-a-companion-guide/youtube/medhavy-companion-pib/medhavy-companion-pib-review.mp4`
- Note: CROSS-REFERENCE — vox-pib-zero-point is an explainer in this same book. The simulation workflow reel (showing Claude Code building the scene) is new and distinct; build it.

---

## Sim-05 — Quantum Tunneling: Exponential Barrier Dependence
- Source: `quantum-mechanics-a-companion-guide/chapters/04-one-dimensional-problems.md`
- Topic: CLAUDE CODE · MANIM
- Physical rule: T ≈ e^(−2κd), κ = √(2m(V₀−E))/ℏ; for φ≈4 eV, κ ≈ 1 Å⁻¹ → factor of 7 per Å
- Concrete numbers: V₀ = 1 eV, E = 0.5 eV, d varies 0.5–2 nm; T changes by e^(2×1.02×d) per Å step
- Visual artifact: wave decaying through barrier; log(T) vs d plot showing linear slope = −2κ
- Two testable predictions: P1: at d = 0 transmission T = 1 (no barrier); P2: each 1 Å increase multiplies T by e^(−2κ) ≈ 1/7.4 for typical metals
- Sim slug: medhavy-companion-tunneling
- Status: BUILT
- Watch: `open /Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-a-companion-guide/youtube/medhavy-companion-tunneling/medhavy-companion-tunneling-review.mp4`

---

# Quantum Mechanics: A Companion Guide — Simulation Ideas

*Sim-scout pass 2026-07-15. Candidates 01–16 below. Ordered by Score descending.*

---

## Candidate 01 — Animate: Gaussian Wavepacket Spreading — The Free-Particle Clock

- Source: `quantum-mechanics-a-companion-guide/chapters/03-the-schrodinger-equation.md`
- Topic: Free-particle wavepacket dispersion
- Lane: MANIM (directed animation)
- Hook: A classical particle follows a trajectory forever — a quantum particle spreads and never retraces. Watch exactly when and how fast the spreading becomes irreversible.
- The rule: σ(t) = σ₀ √(1 + (ħt / 2mσ₀²)²). At early times spreading is slow (quadratic); at late times width grows linearly in t. Each momentum component k accumulates phase e^{i(kx − ħk²t/2m)}, so different momentum components walk apart.
- Concrete numbers: electron, σ₀ = 1 nm, ħ = 1 (atomic units). Spreading time τ = 2mσ₀²/ħ ≈ 0.76 fs for electron; animate 0–5τ. At t = τ, σ = σ₀√2 ≈ 1.41 nm. At t = 5τ, σ ≈ 5.1 nm.
- The artifact / what moves: |ψ(x,t)|² envelope starts as a sharp Gaussian, then visibly flattens and broadens as time sweeps. A running readout shows σ(t) overlaid on the wavepacket. The phase of ψ (shown as color) ripples faster at the packet edges — revealing momentum dispersion as the cause.
- Output medium: Manim (mp4)
- Two testable predictions: P1: at t = τ = 2mσ₀²/ħ, width is exactly σ₀√2 (1.414× initial); P2: for a proton (m ≈ 1836 mₑ), the same σ₀ gives a spreading time 1836× longer — the packet is still narrow at the electron's t = 5τ.
- The change: double σ₀ to 2 nm — spreading time quadruples (∝ σ₀²), showing the packet is stable much longer. Intuition fails: wider packets survive longer, not shorter.
- Human supplies (Claude can't): Nothing — fully synthetic/analytic.
- Teardown angle: The $i$ in the Schrödinger equation is the entire reason this is a spreading wave, not a smoothing diffusion. Remove it → exponential decay, not oscillation. The complex phase is load-bearing.
- Exclusions: No momentum-space plot (saves runtime); skip relativistic corrections.
- Sim slug: qmcg-wavepacket-spreading
- Score: 10/10

---

## Candidate 02 — Explore: Uncertainty Principle Uncertainty Explorer — Trade σ_x for σ_p

- Source: `quantum-mechanics-a-companion-guide/chapters/05-quantum-formalism.md`  (+ "LLM Exercise" from chapter 5)
- Topic: Robertson uncertainty bound — state preparation, not measurement disturbance
- Lane: D3/DATAVIZ (emergent / interactive)
- Hook: The balloon analogy says you disturb the particle by measuring it. Robertson proved something different: the state itself has a joint width floor, before any measurement. Drag the σ_x slider and watch σ_p grow in real time — the floor is the law.
- The rule: σ_x · σ_p ≥ ħ/2 (Robertson 1929). For a Gaussian state: σ_x σ_p = ħ/2 (saturation). For a square-well ground state: σ_x σ_p = (π²/3 − 2)^{1/2} · ħ/2 ≈ 0.568 · ħ (never saturates). User picks σ_x via slider; σ_p floor = ħ/(2σ_x) renders in real time; displayed Gaussian ψ(x) matches chosen σ_x.
- Concrete numbers: ħ = 1 (natural units). σ_x slider range 0.1–10. Floor curve σ_p = 0.5/σ_x. Harmonic oscillator ground state sits at the floor (σ_x σ_p = 0.5). Box ground state sits at σ_x σ_p ≈ 0.568. Display both as highlighted dot vs hyperbola.
- The artifact / what moves: Hyperbola σ_p = ħ/(2σ_x) drawn on σ_x vs σ_p axes. User drags σ_x; a dot rides the hyperbola. The |ψ(x)|² Gaussian in an adjacent panel updates width in real time. Labeled dots mark the harmonic oscillator ground state (on the curve) and the box ground state (above it).
- Output medium: d3 v7 animated/interactive HTML
- Two testable predictions: P1: harmonic oscillator ground state (Gaussian) lies exactly on the Robertson floor: σ_x σ_p = ħ/2; P2: excited harmonic oscillator states have σ_x σ_p = (n + 1/2)ħ, all above the floor — a labeled series appears at σ_x = √((n+1/2)ħ/(mω)).
- The change: toggle from Robertson to Schrödinger bound (adds covariance term) — for uncorrelated states the bounds coincide; for squeezed states they diverge.
- Human supplies (Claude can't): Nothing — fully synthetic/analytic.
- Teardown angle: Preparation uncertainty vs measurement disturbance: two different inequalities, one of which the balloon story never told you about. The floor is a property of the amplitude function, not of the apparatus.
- Exclusions: Skip Ozawa measurement-disturbance formalism (different chapter); no 2D phase space plot.
- Sim slug: qmcg-uncertainty-explorer
- Score: 10/10
- Status: BUILT — `/Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-a-companion-guide/youtube/qmcg-uncertainty-explorer/qmcg-uncertainty-explorer.html`

---

## Candidate 03 — Animate: Quantum Beat — Two Stationary States Interfering in Time

- Source: `quantum-mechanics-a-companion-guide/chapters/03-the-schrodinger-equation.md`
- Topic: Bohr frequency / quantum beat / oscillating expectation value
- Lane: MANIM (directed animation)
- Hook: A stationary state is stationary — until you mix two of them. Then ⟨x⟩(t) swings like a pendulum at the exact frequency of every spectral line in atomic physics.
- The rule: ψ(x,t) = (1/√2)[ψ₁(x)e^{−iE₁t/ħ} + ψ₂(x)e^{−iE₂t/ħ}]. The cross term in |ψ|² oscillates at ω = (E₂ − E₁)/ħ. ⟨x⟩(t) = L/2 − (16L/9π²)cos(ωt) for the infinite square well.
- Concrete numbers: L = 1 nm electron infinite well. E₁ = 0.376 eV, E₂ = 1.504 eV. ω = (E₂ − E₁)/ħ = 1.128 eV / ħ ≈ 1.72 × 10¹⁵ rad/s. Beat period T = 2π/ω ≈ 3.65 fs. Amplitude of ⟨x⟩ oscillation = 16L/9π² ≈ 0.180 nm.
- The artifact / what moves: |ψ(x,t)|² animated in a box as a probability lump that rocks left-right at the Bohr frequency. Below: ⟨x⟩(t) trace drawing in real time. Phase clocks for the two stationary states spin at different rates — when their relative phase is 0 the lump is left; when it's π the lump is right.
- Output medium: Manim (mp4)
- Two testable predictions: P1: oscillation amplitude = 16L/9π² ≈ 0.1803L exactly; P2: beat frequency ω = 3E₁(π²ħ)/(2mL²) = 3(E₂−E₁)/ħ (since E₂ = 4E₁ → ω = 3E₁/ħ).
- The change: mix n=1 and n=3 instead — the integral ∫xψ₁ψ₃ dx is zero by symmetry (both odd parity × odd parity in ψ₁ψ₃ → ⟨x⟩ doesn't oscillate). Lesson: not every superposition produces a visible beat. Selection rules appear.
- Human supplies (Claude can't): Nothing — fully synthetic/analytic.
- Teardown angle: Every spectral line in atomic physics — every wavelength in the Balmer series — exists because two stationary-state phases rotate at the Bohr frequency. This single animation is the mechanism behind emission spectroscopy.
- Exclusions: No radiation field; no decay / decoherence.
- Sim slug: qmcg-quantum-beat
- Score: 10/10

---

## Candidate 04 — Animate: Gamow Alpha Decay — 24 Orders of Magnitude from One Exponent

- Source: `quantum-mechanics-a-companion-guide/chapters/04-one-dimensional-problems.md`
- Topic: WKB tunneling / Gamow factor / Geiger-Nuttall law
- Lane: MANIM (directed animation)
- Hook: Po-212 and Th-232 alpha energies differ by a factor of 2. Their half-lives differ by 10²⁴. One exponential does all of that.
- The rule: T ≈ exp(−2γ) where γ = (1/ħ)∫_{r₁}^{r₂}√(2m(V(r)−E))dr for the Coulomb barrier V(r) = 2(Z−2)e²/(4πε₀r). In thick-barrier limit: γ ≈ π(Z−2)e²/(4πε₀ħv), v = √(2E/m). Half-life t_{1/2} = (r₁/v)·e^{2γ}·ln2.
- Concrete numbers: Po-212: Z=84, E=8.78 MeV → γ≈26, T≈e^{-52}, t_{1/2}≈0.3 μs. Th-232: Z=90, E=4.01 MeV → γ≈77, T≈e^{-154}, t_{1/2}≈1.4×10¹⁰ yr. Animate barrier height at each nucleus, wavefunction tail inside.
- The artifact / what moves: Nuclear potential-well diagram with Coulomb barrier sweeping up. The wavefunction ψ(r) drawn inside the barrier region as an exponentially decaying tail. As E slider moves from 4 MeV to 9 MeV, the outer turning point r₂ = 2(Z−2)e²/E shrinks visibly — the barrier thins. Running log(t_{1/2}) readout drops from 17 (years) to −5 (microseconds). The Geiger-Nuttall plot (log t_{1/2} vs 1/√E) draws in as a straight line.
- Output medium: Manim (mp4)
- Two testable predictions: P1: log(t_{1/2}) vs 1/√E is linear — Geiger-Nuttall law — with slope proportional to Z; P2: Po-212 at E=8.78 MeV gives γ≈26 → t_{1/2}≈0.3 μs (measured: 0.298 μs).
- The change: Fix E and vary Z from 82 to 92 — slope of Geiger-Nuttall plot scales as Z, so heavier nuclei at the same energy have dramatically longer half-lives.
- Human supplies (Claude can't): Nothing — fully synthetic/analytic (nuclear data from NNDC).
- Teardown angle: The exponential does everything. A factor-of-2 energy change spans 24 orders of magnitude in lifetime. No other force in nature produces this dynamic range from a single formula.
- Exclusions: No nuclear shell effects, no even-odd staggering; skip preformation probability.
- Sim slug: qmcg-gamow-alpha-decay
- Score: 10/10

---

## Candidate 05 — Explore: CHSH Bell Inequality Tester — Drag Angles, Watch the Bound Break

- Source: `quantum-mechanics-a-companion-guide/chapters/10-quantum-mechanics-in-the-modern-world.md`  (+ "LLM Exercise" implied by chapter structure)
- Topic: CHSH inequality / entanglement / local hidden variables
- Lane: D3/DATAVIZ (emergent / interactive)
- Hook: Local hidden variables guarantee |S| ≤ 2. Quantum mechanics gives 2√2 ≈ 2.828. Drag Alice and Bob's four angles and watch the CHSH quantity try to exceed 2. Find the angles that push it to the Tsirelson bound.
- The rule: E_QM(a,b) = −cos(a−b) for the spin singlet. S = E(a₁,b₁) + E(a₁,b₂) + E(a₂,b₁) − E(a₂,b₂). LHV bound: |S| ≤ 2. Quantum bound (Tsirelson): |S| ≤ 2√2. Saturation at a₁=0, a₂=π/2, b₁=π/4, b₂=−π/4.
- Concrete numbers: Four angle dials (0–2π each). S computed live. Display: current S value, LHV bound at ±2 (red lines), Tsirelson bound at ±2√2 (blue lines), correlation wheel showing all four E(aᵢ,bⱼ) as color-mapped squares.
- The artifact / what moves: Four angle dials (Alice a₁, a₂; Bob b₁, b₂). As user drags any dial, E values update as cosines, S updates, and a needle on a meter swings. When |S| > 2 the background turns red — "LHV violated." A Monte-Carlo random-angle search button sweeps all configurations and plots max |S| achieved vs. tries — converging to 2√2.
- Output medium: d3 v7 animated/interactive HTML
- Two testable predictions: P1: optimal angles a₁=0, a₂=π/2, b₁=π/4, b₂=−π/4 yield |S| = 2√2 = 2.8284…; P2: if all four angles are equal (a₁=a₂=b₁=b₂), |S| = 0 — no violation because all correlations cancel.
- The change: Switch from singlet (anti-correlated) to triplet |1,0⟩ (symmetric) — E(a,b) = +cos(a−b). Max |S| for triplet at optimal angles is also 2√2 — same Tsirelson bound, different physics.
- Human supplies (Claude can't): Nothing — fully synthetic/analytic.
- Teardown angle: A Nobel Prize lives in one page of algebra. The local-realist bound of 2 is an arithmetic fact about ±1 products. The quantum violation of 2√2 is a cosine. The gap between them is the entire content of the 2022 Nobel Prize in Physics.
- Exclusions: Skip detection loophole details; skip Bohmian mechanics / nonlocal hidden variables.
- Sim slug: qmcg-chsh-explorer
- Score: 10/10
- Status: BUILT — `/Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-a-companion-guide/youtube/qmcg-chsh-explorer/qmcg-chsh-explorer.html`

---

## Candidate 06 — Animate: Hydrogen 1s Radial Density — Why the Orbit Picture Fails

- Source: `quantum-mechanics-a-companion-guide/chapters/06-the-hydrogen-atom.md`
- Topic: Hydrogen radial probability density; most probable radius vs mean radius
- Lane: MANIM (directed animation)
- Hook: Bohr got the energy right with a circular orbit at radius a₀. The actual probability density peaks there too — but the mean radius is 3a₀/2. Those two numbers differ because there is no orbit, only a cloud.
- The rule: P(r) = |R₁₀(r)|² r² = (4/a₀³) r² e^{−2r/a₀}. Peak at r_mp = a₀. Mean ⟨r⟩ = 3a₀/2. The asymmetric tail above r_mp pulls the mean up from the mode.
- Concrete numbers: a₀ = 0.0529 nm. P(r) peak at r = 0.0529 nm. ⟨r⟩ = 0.0794 nm. At 90% enclosure radius ≈ 3.3 a₀. The distribution has zero probability at r=0 (goes as r²) and exponential tail beyond a₀.
- The artifact / what moves: P(r) curve animates in, peak labeled a₀. Vertical line sweeps from r=0 to ∞ accumulating probability; when area = 50% a dashed line marks the median (≈ 1.34 a₀). A second vertical line shows ⟨r⟩ = 3a₀/2. Three distinct markers (mode, median, mean) end up at different positions — the orbit picture predicts all three should be the same point.
- Output medium: Manim (mp4)
- Two testable predictions: P1: probability maximum at exactly r = a₀; P2: ⟨r⟩ = 3a₀/2 exactly (verified by the integral (4/a₀³)∫₀^∞ r³ e^{−2r/a₀} dr = 3a₀/2).
- The change: Switch to 2p state: P(r) = |R₂₁|² r² ∝ r⁴ e^{−r/a₀}. Peak shifts to r_mp = 4a₀. The Bohr model's n=2 orbit predicts r = 4a₀ for circular orbit — again hits the mode exactly, but ⟨r⟩ = 5a₀. The coincidence of Bohr's radius with the mode (not mean) is the hidden symmetry's signature.
- Human supplies (Claude can't): Nothing — fully synthetic/analytic.
- Teardown angle: Bohr was right about one number (the length scale a₀) and wrong about everything else (definite position, circular trajectory, sharp radius). The SO(4) symmetry of the Coulomb potential secretly guaranteed he'd get the energies right; the statistics of the cloud guarantee he'd get everything else wrong.
- Exclusions: Skip angular probability (θ, φ dependence); skip excited states other than the one-parameter change.
- Sim slug: qmcg-hydrogen-radial-density
- Score: 9/10

---

## Candidate 07 — Explore: Harmonic Oscillator Ladder — Energy Levels and Uncertainty Floor

- Source: `quantum-mechanics-a-companion-guide/chapters/04-one-dimensional-problems.md`  (+ "LLM Exercise" LLM-E2)
- Topic: Quantum harmonic oscillator; ladder operators; Robertson saturation at n=0
- Lane: D3/DATAVIZ (emergent / interactive)
- Hook: Every rung up the ladder adds exactly ħω. Only the ground state saturates the uncertainty bound σ_x σ_p = ħ/2. Higher rungs have σ_x σ_p = (n+½)ħ — the ladder is climbing away from the uncertainty floor.
- The rule: E_n = ħω(n + ½). ψ_n(x) ∝ H_n(ξ)e^{−ξ²/2} where ξ = x/x₀, x₀ = √(ħ/mω). σ_x = x₀√(n+½), σ_p = ħ/(2x₀)·√(n+½)·2, σ_x σ_p = (n+½)ħ.
- Concrete numbers: ħ=1 units; ω=1; x₀=1. n slider 0–10. E_n from 0.5 to 10.5. σ_x σ_p from 0.5 to 10.5 (in units of ħ). Robertson floor = 0.5ħ.
- The artifact / what moves: Left panel: energy ladder with n-th rung highlighted; ψ_n(x) wavefunction drawn at that rung showing n nodes. Right panel: σ_x vs σ_p plane with Robertson hyperbola σ_x σ_p = ħ/2; a dot traces the location of the current state as n increases — rising vertically along the hyperbola's branch. When n=0 the dot sits exactly on the curve.
- Output medium: d3 v7 animated/interactive HTML
- Two testable predictions: P1: n=0 state has σ_x σ_p = ħ/2 exactly (Robertson saturation); P2: each increment n → n+1 adds exactly ħ to σ_x σ_p (linear, not quadratic — the ladder of uncertainty mirrors the energy ladder).
- The change: Add a "squeeze" control that deforms the ground state into a squeezed coherent state: σ_x decreases, σ_p increases, product stays at ħ/2 but the dot moves along the floor curve instead of up the ladder.
- Human supplies (Claude can't): Nothing — fully synthetic/analytic.
- Teardown angle: Zero-point energy and uncertainty saturation are the same constraint seen from two angles. The ground state is exactly as uncertain as any state can be while still minimizing energy. Higher states are "further" from the floor in two dimensions simultaneously.
- Exclusions: Skip time evolution (covered in Candidate 03); skip coherent states beyond the squeeze control.
- Sim slug: qmcg-harmonic-oscillator-ladder
- Score: 9/10
- Status: BUILT — `open /Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-a-companion-guide/youtube/qmcg-harmonic-oscillator-ladder/qmcg-harmonic-oscillator-ladder.html`

---

## Candidate 08 — Explore: Fermi-Dirac vs Bose-Einstein Distribution Explorer

- Source: `quantum-mechanics-a-companion-guide/chapters/08-identical-particles.md`
- Topic: Quantum statistics; fermion vs boson occupation; one sign in the denominator
- Lane: D3/DATAVIZ (emergent / interactive)
- Hook: One sign difference in the denominator — a + vs a − — is the entire difference between a star that can collapse and one that cannot, between electrons that form shells and photons that condense. Drag the temperature slider and watch the two distributions diverge.
- The rule: ⟨n_i⟩_FD = 1/(e^{(E−μ)/kT} + 1). ⟨n_i⟩_BE = 1/(e^{(E−μ)/kT} − 1). At high T, both → Maxwell-Boltzmann. At low T: FD → step function at μ; BE diverges at E=μ (condensation).
- Concrete numbers: Energy axis 0–5 eV; μ = 2 eV; T slider 0–5000 K. At T=300 K, kT ≈ 0.026 eV → FD step is very sharp; BE diverges strongly near E=μ. At T=5000 K (kT ≈ 0.43 eV) both approach the same classical Boltzmann curve.
- The artifact / what moves: Two overlaid curves (FD blue, BE red) on ⟨n⟩ vs E axes. As T slider moves: at T→0 FD sharpens to a step, BE shoots up near μ. At T→∞ both converge on the same classical exponential. A third curve (Maxwell-Boltzmann, dashed) shows the classical limit. When T < 100 K, the "universe" panel shows a schematic: fermions filling states one by one (electron shell structure); bosons piling into the lowest state (BEC).
- Output medium: d3 v7 animated/interactive HTML
- Two testable predictions: P1: at T=0, ⟨n_i⟩_FD = 1 for E < μ, 0 for E > μ (perfect step); P2: at T such that kT ≫ E−μ, both distributions converge to e^{−(E−μ)/kT} within 1% — classical limit is quantitative, not just qualitative.
- The change: Move μ slider to change the Fermi energy — watch how the thermal smearing width (~4kT) scales, showing why metals have nearly temperature-independent conductivity up to very high T.
- Human supplies (Claude can't): Nothing — fully synthetic/analytic.
- Teardown angle: The entire difference between the Pauli exclusion principle (fermions build periodic table) and Bose-Einstein condensation (bosons collapse into one state) is the algebraic sign in a denominator. One sign. The difference between solid matter and laser light.
- Exclusions: Skip density of states integration; skip BEC critical temperature calculation.
- Sim slug: qmcg-quantum-statistics-explorer
- Score: 9/10
- Status: BUILT — `open /Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-a-companion-guide/youtube/qmcg-quantum-statistics-explorer/qmcg-quantum-statistics-explorer.html`

---

## Candidate 09 — Explore: Variational Helium — Effective Nuclear Charge Minimization

- Source: `quantum-mechanics-a-companion-guide/chapters/09-approximation-methods.md`
- Topic: Variational principle; helium ground state; screening as emergent physics
- Lane: D3/DATAVIZ (emergent / interactive)
- Hook: You can't solve helium exactly. But one adjustable parameter — an effective nuclear charge Z* — gives 98% of the right energy. Drag Z* and watch ⟨H⟩ find its own minimum. The minimum is at Z* = 27/16 = 1.6875 because each electron screens 5/16 of the nuclear charge.
- The rule: ⟨H⟩(Z*) = (Z*)² − 2ZZ* + (5/8)Z* in atomic units (Hartrees). Minimizing: dE/dZ* = 2Z* − 2Z + 5/8 = 0 → Z* = Z − 5/16. For He: Z* = 27/16 ≈ 1.6875. E_var = −(27/16)² ≈ −2.848 Hartree ≈ −77.5 eV. Exact: −79.0 eV.
- Concrete numbers: Z = 2 (helium). Z* slider 0–3. Three energy-component curves drawn: kinetic (Z*)², nucleus attraction −2ZZ*, ee-repulsion (5/8)Z*. Sum = ⟨H⟩. Running minimum marker. Experimental target line at −2.904 Hartree.
- The artifact / what moves: ⟨H⟩(Z*) parabola drawn on energy vs Z* axes. Three component curves draw simultaneously showing how each term varies. A movable dot rides the ⟨H⟩ curve; as user drags Z*, the dot moves. When released, the dot snaps to the minimum at Z*=27/16 and a "variational bound" label appears. Distance from experimental value shown as a percentage.
- Output medium: d3 v7 animated/interactive HTML
- Two testable predictions: P1: minimum of ⟨H⟩ occurs at Z* = Z − 5/16 = 27/16 exactly; P2: E_var = −(27/16)² = −2.8477 Hartree, within 1.9% of exact −2.9037 Hartree.
- The change: Try Z = 3 (lithium-like ion Li+): Z* = 3 − 5/16 = 43/16 ≈ 2.6875. E_var = −(43/16)² ≈ −7.22 Hartree. Exact: −7.28 Hartree. Same formula, different atom.
- Human supplies (Claude can't): Nothing — fully synthetic/analytic.
- Teardown angle: The variational method gives you a bound (always above the true energy), not a guess. Hylleraas with six parameters got 4 significant figures. One parameter gets 98%. The energy is robust to imprecision in the wavefunction — that's the theorem.
- Exclusions: Skip excited states; skip multi-parameter optimization.
- Sim slug: qmcg-variational-helium
- Score: 9/10
- Status: BUILT — `open /Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-a-companion-guide/youtube/qmcg-variational-helium/qmcg-variational-helium.html`

---

## Candidate 10 — Animate: Single-Electron Diffraction Buildup — The Tonomura Sequence

- Source: `quantum-mechanics-a-companion-guide/chapters/01-why-quantum-mechanics.md`  (+ S2 exercise, LLM-E3)
- Topic: de Broglie matter waves; single-electron double-slit; interference from one particle at a time
- Lane: MANIM (directed animation)
- Hook: 100 electrons hit a screen and form random dots. 70,000 electrons hit the same screen and a diffraction pattern appears. No two electrons interacted. The pattern is the electron interfering with itself. Watch it build.
- The rule: Fringe positions: d sinθ = nλ, λ = h/p. |ψ|² = 2cos²(kd sinθ / 2). Each electron lands according to |ψ|²; accumulation reveals the distribution. Monte-Carlo sampling from |ψ|² models the Tonomura 1989 experiment.
- Concrete numbers: Slit separation d = 300 nm; λ = 0.05 nm (from 54 eV electrons: p = √(2mK), λ = h/p ≈ 0.167 nm, adjust to 0.05 nm for visual clarity); screen at 10 cm. First-order fringe at sinθ = λ/d ≈ 1.67 × 10⁻⁴ rad → 0.167 μm from center. Animate N = 1, 10, 100, 1000, 10000 electrons.
- The artifact / what moves: Screen accumulates electron hits one dot at a time (each randomly placed by Monte-Carlo sampling from |ψ|²). At N=100: random-looking scatter. At N=1000: faint bands appear. At N=10000: crisp diffraction pattern. Frame counter shows N. A "what classical particles would do" comparison panel shows a two-slit blob with no fringes.
- Output medium: Manim (mp4)
- Two testable predictions: P1: first bright fringe angle satisfies d sinθ = λ → sinθ = λ/d; fringe spacing = λ×L/d at screen distance L; P2: if one slit is blocked, fringes vanish and a single-slit diffraction envelope appears — the two-slit pattern requires both paths open.
- The change: Replace electrons with protons at the same kinetic energy — λ_proton = λ_electron × √(mₑ/mₚ) ≈ 1/43 × λ_electron. Fringe spacing shrinks by factor 43. Interference persists but pattern is 43× finer.
- Human supplies (Claude can't): Nothing — fully synthetic/analytic.
- Teardown angle: Intensity (beam brightness) controls how many dots per second, not fringe position. The fringes are determined entirely by momentum (wavelength). There is no classical reading of this. The electron had no partner to interfere with.
- Exclusions: Skip decoherence effects; skip which-path information / eraser variants.
- Sim slug: qmcg-tonomura-buildup
- Score: 9/10

---

## Candidate 11 — Animate: Bloch Sphere Spin Evolution — From Stern-Gerlach to Precession

- Source: `quantum-mechanics-a-companion-guide/chapters/07-angular-momentum.md`  (+ `quantum-mechanics-a-companion-guide/chapters/02-mathematical-foundations.md`)
- Topic: Spin-1/2 on the Bloch sphere; Stern-Gerlach basis change; 720° spinor rotation
- Lane: MANIM (directed animation)
- Hook: A spin-up state along z looks like 50/50 along x. That fact — one spin measurement disturbing the next — is a point moving on a sphere. Watch the spin state precess around any axis as a vector on the Bloch sphere, then watch it return to itself only after 720°.
- The rule: |ψ⟩ = cos(θ/2)|↑⟩ + e^{iφ}sin(θ/2)|↓⟩ maps to point (sinθcosφ, sinθsinφ, cosθ) on unit sphere. Time evolution under H = −(ħω₀/2)σ_z is precession: φ(t) = ω₀t. Rotation operator: U(θ,n̂) = cos(θ/2)I − i·sin(θ/2)(n̂·σ). At θ=2π: U=−I (720° returns to self).
- Concrete numbers: ω₀ = 2π × 1 MHz (Larmor frequency in ~35 mT field). One precession period T = 1 μs. Animate 0–2T. Show |↑_z⟩ at north pole, |↑_x⟩ at equator (φ=0), |↑_y⟩ at equator (φ=π/2). Rotation from z-up to x-up: 90° arc.
- The artifact / what moves: Bloch sphere in 3D with state vector (Bloch vector) as a red arrow. Starting at north pole (|↑_z⟩). Under Larmor precession: vector sweeps the equator. When axis changed to n̂=(1,0,0): state precesses around x-axis. At the end: animate U(2π) — the vector returns to north pole but the global phase is −1 (shown by a phasor clock that completes only 180° even as the Bloch vector returns).
- Output medium: Manim (mp4)
- Two testable predictions: P1: starting in |↑_z⟩ and rotating 90° around x-axis gives |↑_x⟩ — measurement probability along x is 100% up; P2: 360° rotation returns Bloch vector to origin but multiplies quantum state by −1 (measurable in neutron interferometry as π phase shift).
- The change: Show sequential Stern-Gerlach measurement: z→x→z. After x-measurement, z-measurement is 50/50 again. On Bloch sphere: projection onto x-axis collapses to equator point, then z-measurement collapses to north or south pole with equal probability.
- Human supplies (Claude can't): Nothing — fully synthetic/analytic.
- Teardown angle: Non-commuting measurements are a single geometric fact: the Bloch sphere isn't flat. Measuring x moves your point to the equator; measuring z afterward picks north or south. The non-commutativity is the curvature of the sphere.
- Exclusions: Skip density matrix / mixed states; skip decoherence.
- Sim slug: qmcg-bloch-sphere-spin
- Score: 9/10

---

## Candidate 12 — Explore: Finite Square Well — Bound States vs Depth

- Source: `quantum-mechanics-a-companion-guide/chapters/04-one-dimensional-problems.md`  (+ C1 exercise)
- Topic: Finite square well; transcendental bound-state equation; "always binds in 1D" theorem
- Lane: D3/DATAVIZ (emergent / interactive)
- Hook: A 1D well always traps at least one bound state, no matter how shallow. Drag the depth to zero and watch the ground-state energy chase the continuum — but never reach it. This is the theorem every student forgets when they move to 3D, where it's false.
- The rule: Even-parity bound states satisfy z·tan(z) = √(z₀²−z²) where z=ka, z₀²=2mV₀a²/ħ². Number of even states = ceil(z₀/π). There is always at least one solution for any z₀ > 0. Each solution gives energy E = −V₀(1 − z²/z₀²).
- Concrete numbers: a = 0.5 nm (half-width), m = electron mass. z₀ = √(2mV₀a²/ħ²). V₀ slider 0–100 eV. At V₀=1 eV: z₀≈0.36, one even-parity bound state near E≈−0.05 eV. At V₀=50 eV: z₀≈2.56, two even states. Show odd-parity states (z·cot(z)=−√…) appearing at higher V₀.
- The artifact / what moves: Graphical solution: z·tan(z) curve (blue) and √(z₀²−z²) semicircle (red) plotted together. Intersections are bound states. As V₀ slider moves, the red semicircle radius z₀ grows — new intersections appear at each new π/2 crossing. Below the main plot: actual potential well drawn with bound-state energies as horizontal lines. Energy tail of ground state approaches 0 but never reaches it.
- Output medium: d3 v7 animated/interactive HTML
- Two testable predictions: P1: first odd-parity bound state appears only when z₀ > π/2, i.e., V₀ > π²ħ²/(8ma²) ≈ 0.94 eV for a = 0.5 nm electron; P2: as V₀→0, ground-state energy → 0⁻ (approaches threshold from below, never zero).
- The change: Toggle "3D spherical well" mode — the 3D condition is z·cot(z) = −√(z₀²−z²) (odd parity only). No solution exists until z₀ > π/2. The viewer sees the graphical solution fail to intersect for z₀ small — the 1D guarantee is gone.
- Human supplies (Claude can't): Nothing — fully synthetic/analytic.
- Teardown angle: The 1D well's guaranteed binding is a topological accident of one dimension. In 3D, binding requires a minimum depth. A student who only does 1D problems learns the wrong lesson about confinement.
- Exclusions: Skip numerical solution for excited states; skip scattering states (E > 0).
- Sim slug: qmcg-finite-well-explorer
- Score: 8/10
- Status: BUILT — `open /Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-a-companion-guide/youtube/qmcg-finite-well-explorer/qmcg-finite-well-explorer.html`

---

## Candidate 13 — Animate: Born Rule Probability Density — Where the Particle Actually Is

- Source: `quantum-mechanics-a-companion-guide/chapters/03-the-schrodinger-equation.md`
- Topic: Born rule; probability density vs charge density; the 9% vs 25% surprise
- Lane: MANIM (directed animation)
- Hook: A particle in a box's ground state has a 9% chance of being in the left quarter — not 25%. The wave function peaks in the middle, not uniformly. That 9% vs 25% is the Born rule doing physics.
- The rule: P = (2/L)∫₀^{L/4} sin²(πx/L)dx = 1/4 − 1/(2π) ≈ 0.091. The probability density ρ(x) = |ψ₁(x)|² = (2/L)sin²(πx/L) is not uniform — it peaks at L/2.
- Concrete numbers: L = 1 nm. P(left quarter) = 1/4 − 1/2π ≈ 9.1%. P(middle half) = 1/2 + 1/π ≈ 81.8%. P(right quarter) = 9.1% (by symmetry). For n=2: P(left quarter) ≈ 40.9%, P(middle) ≈ 18.2% (node kills probability). At large n: all → 25% (classical limit).
- The artifact / what moves: ψ₁(x) drawn in a box. |ψ₁(x)|² shown below in red. Three colored region highlights: left quarter (blue), middle half (green), right quarter (blue). Running probability readout for each. Then sweep n from 1 to 20 — watch left-quarter probability oscillate but trend toward 25% (correspondence principle limit). Classical prediction (25% for all regions at all n) shown as dashed line.
- Output medium: Manim (mp4)
- Two testable predictions: P1: left-quarter probability for n=1 is exactly 1/4 − 1/(2π) = 0.0908...; P2: for n=2, left-quarter probability is 1/4 + 1/(2π) ≈ 0.409 (above classical) because the n=2 wave function peaks at L/4.
- The change: Switch from infinite to finite well: probability leaks into the barrier region (classically forbidden). Left-quarter probability slightly increases due to exponential tail. Shows that Born rule applies everywhere, including classically forbidden zones.
- Human supplies (Claude can't): Nothing — fully synthetic/analytic.
- Teardown angle: Schrödinger thought |ψ|² was charge density. Born's interpretation survived because it gave the right probabilities. The 9% vs 25% discrepancy is measurable and rules out any uniform distribution.
- Exclusions: Skip time-dependent density evolution; skip mixed states.
- Sim slug: qmcg-born-rule-probability
- Score: 8/10

---

## Candidate 14 — Explore: Fermi's Golden Rule Resonance — Transition Rate vs Detuning

- Source: `quantum-mechanics-a-companion-guide/chapters/09-approximation-methods.md`
- Topic: Fermi's golden rule; sin²(Ωt/2)/Ω² lineshape; transition rate vs time
- Lane: D3/DATAVIZ (emergent / interactive)
- Hook: At early times the transition probability grows as t². At late times it grows as t (a constant rate). The crossover is the moment Fermi's golden rule kicks in. Drag time and watch the sinc-squared peak sharpen into a delta function.
- The rule: P_if(t) = (|⟨f|V|i⟩|²/ħ²) · (4sin²(Ωt/2)/Ω²), where Ω = (E_f − E_i − ħω)/ħ is detuning. Rate W = lim_{t→∞} P/t = (2π/ħ)|⟨f|V|i⟩|²δ(E_f − E_i − ħω). Short time: P ≈ (|⟨f|V|i⟩|²/ħ²)·t² (quadratic). Late time: P = Wt (linear).
- Concrete numbers: ħ = 1 units. |⟨f|V|i⟩| = 0.1 (coupling). Ω range −5 to +5. t slider 0.1–20. At t=1: lineshape width ∼4π/t ≈ 12.6; at t=10: width ∼1.26; height scales ∝ t². The δ-function limit shown as a vertical spike at Ω=0.
- The artifact / what moves: Top panel: P(Ω) = 4sin²(Ωt/2)/Ω² plotted vs Ω for current t. Peak narrows and grows as t increases. Dashed curve shows the δ-function envelope (∝ πt at Ω=0). Bottom panel: P(Ω=0) vs t — quadratic at first, then linear at large t. Toggle "rate mode" to show dP/dt vs t (constant at late times = Fermi's golden rule rate).
- Output medium: d3 v7 animated/interactive HTML
- Two testable predictions: P1: at resonance (Ω=0), P(t) = (|⟨f|V|i⟩|t/ħ)² at early times (exact, not an approximation); P2: peak height at Ω=0 grows as t² while peak width shrinks as 1/t, keeping the integral ∝ t — consistent with the delta-function limit.
- The change: Add a "density of states" slider ρ(E_f). When ρ is large, the golden rule rate W = (2π/ħ)|V|²ρ is large even for weak coupling. Shows how spontaneous emission rate (large radiation field density of states) can exceed stimulated emission even for the same matrix element.
- Human supplies (Claude can't): Nothing — fully synthetic/analytic.
- Teardown angle: Fermi's golden rule is a limit, not a law. It applies in a specific time window (long enough for the sinc to sharpen, short enough for first-order to hold). Outside that window the quadratic growth or Rabi oscillations take over. Recognizing the window is the engineering judgment the formula can't supply.
- Exclusions: Skip Rabi oscillations (discrete case); skip density-matrix approach.
- Sim slug: qmcg-fermis-golden-rule
- Score: 8/10
- Status: BUILT — `open /Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-a-companion-guide/youtube/qmcg-fermis-golden-rule/qmcg-fermis-golden-rule.html`

---

## Candidate 15 — Animate: The Singlet State — Rotational Invariance and Bell Correlations

- Source: `quantum-mechanics-a-companion-guide/chapters/07-angular-momentum.md`
- Topic: Two-spin singlet; rotational invariance in all bases; bridge to Bell inequality
- Lane: MANIM (directed animation)
- Hook: The singlet (1/√2)(|↑↓⟩ − |↓↑⟩) looks the same in every basis. Rotate both spins and the state is unchanged. This rotational invariance — a 2-particle algebraic fact — is what makes the CHSH violation possible. Watch the anti-correlation hold in every direction.
- The rule: |0,0⟩ = (1/√2)(|↑↓⟩ − |↓↑⟩). In x-basis: (1/√2)(|+x⟩₁|−x⟩₂ − |−x⟩₁|+x⟩₂). Correlation: E(n̂_A, n̂_B) = −cos(θ), θ = angle between measurement axes. Anti-correlation is perfect and direction-independent.
- Concrete numbers: θ sweep 0° to 180°. E(θ) = −cos(θ). At θ=0: E=−1 (perfect anti-correlation). At θ=90°: E=0 (uncorrelated). At θ=180°: E=+1 (perfect correlation — opposite measurements along same axis). CHSH angles: θ values 0°, 45°, 90°, 135° → S = −cos0° − cos45° − cos45° + cos135° = −2√2 (magnitude = 2√2).
- The artifact / what moves: Two Bloch spheres (Alice and Bob). Alice's measurement axis shown as a blue arrow. Bob's axis as red arrow. θ between them shown numerically. When θ is swept: a correlation meter needle (−1 to +1) tracks E(θ) = −cos(θ). The meter passes zero at θ=90°. Below: CHSH meter showing current |S| for current four-angle configuration. When optimal angles hit: red "LHV violated" indicator.
- Output medium: Manim (mp4)
- Two testable predictions: P1: at θ=0 (parallel), E = −1 exactly — every measurement perfectly anti-correlated; P2: at θ=90° (perpendicular), E = 0 — completely uncorrelated, as if the spins were independent.
- The change: Replace singlet |0,0⟩ with triplet |1,0⟩ = (1/√2)(|↑↓⟩ + |↓↑⟩). Correlation becomes E(θ) = +cos(θ) — all correlations flip sign. CHSH quantity reaches 2√2 again (same bound, different optimal angles). But the singlet and triplet are physically distinguishable by a θ=0 measurement: singlet → always anti-correlated; triplet |1,0⟩ → always anti-correlated along z but correlated along x.
- Human supplies (Claude can't): Nothing — fully synthetic/analytic.
- Teardown angle: The singlet's rotational invariance is the physical fact that makes it both (a) the ground state of helium and (b) the state that maximally violates Bell. It's the same quantum number j=0 doing both jobs.
- Exclusions: Skip Clebsch-Gordan coefficients; skip addition of angular momentum for j>1/2.
- Sim slug: qmcg-singlet-correlations
- Score: 8/10

---

## Candidate 16 — Explore: Kronig-Penney Band Structure — Where Forbidden Gaps Come From

- Source: `quantum-mechanics-a-companion-guide/chapters/10-quantum-mechanics-in-the-modern-world.md`
- Topic: Bloch's theorem; Kronig-Penney model; band gaps in periodic potentials
- Lane: D3/DATAVIZ (emergent / interactive)
- Hook: A perfectly periodic crystal should let electrons through — it's just repeated copies of the same potential. Yet some energies are forbidden. Drag the barrier strength and watch the allowed bands shrink and the gaps open. The transistor your phone runs on exists because of a sign mismatch in a cosine.
- The rule: cos(ka) = cos(qa) + (mV₀a/ħ²q)sin(qa) where q = √(2mE)/ħ. When |RHS| > 1, no real k exists → forbidden gap. Allowed bands: |RHS| ≤ 1. As V₀ increases, gaps widen; as V₀→0, free-electron parabola E=ħ²k²/2m recovered.
- Concrete numbers: a = 0.3 nm (lattice spacing). m = electron mass. V₀ slider 0–10 eV. E axis 0–20 eV. At V₀=0: pure parabola. At V₀=2 eV: first gap opens at k=π/a ≈ 10.5 nm⁻¹ (E≈4 eV). At V₀=5 eV: first gap ≈ 2 eV wide; second gap appears.
- The artifact / what moves: Left panel: RHS function of the Kronig-Penney equation vs q (or equivalently E), with ±1 bounds drawn as dashed red lines. Where |RHS| > 1: gray shading (forbidden). Right panel: E vs k band structure, showing parabolic-like allowed bands with gaps at k = nπ/a. As V₀ slider moves: gray shading expands, gaps widen on both panels simultaneously.
- Output medium: d3 v7 animated/interactive HTML
- Two testable predictions: P1: at V₀=0, band structure recovers free-electron parabola E = ħ²k²/2m exactly — no gaps; P2: first gap center is at k = π/a (first Brillouin zone edge), E ≈ ħ²π²/(2ma²) ≈ 4.2 eV for a = 0.3 nm.
- The change: Double lattice spacing a → 0.6 nm. First gap energy drops by factor 4 (∝ 1/a²). Gaps shift to lower energies — the band structure is entirely controlled by lattice geometry, not just barrier height.
- Human supplies (Claude can't): Nothing — fully synthetic/analytic.
- Teardown angle: Transistors, LEDs, solar cells, and CCDs all depend on the existence of band gaps — which exist because electrons in a periodic potential satisfy a cosine equation that periodically exceeds its bounds. Bloch's 1928 theorem turns the Schrödinger equation in a crystal into a two-liner that produces 21st-century electronics.
- Exclusions: Skip 3D band structure; skip tight-binding model.
- Sim slug: qmcg-kronig-penney-bands
- Score: 8/10
- Status: BUILT — `open /Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-a-companion-guide/youtube/qmcg-kronig-penney-bands/qmcg-kronig-penney-bands.html`
