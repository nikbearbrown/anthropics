# Simulation Ideas — quantum-mechanics-vol3

Medhavy-register "Claude Code + Manim" workflow reels.

---

## Sim-01 — WKB Tunneling: STM Current Drops 7× per Ångström
- Source: `quantum-mechanics-vol3/chapters/04-the-wkb-approximation-and-tunneling.md`
- Topic: CLAUDE CODE · MANIM
- Physical rule: T ≈ e^(−2κd), κ=√(2mφ)/ℏ; for φ=4 eV, κ≈1.02 Å⁻¹ → factor of e²≈7.4 per Å
- Concrete numbers: φ=4 eV, κ=1.02 Å⁻¹; at d=5 Å current I₀; at d=6 Å current I₀/7.4; at d=4 Å current 7.4·I₀
- Visual artifact: wavefunction decay through vacuum gap; semi-log plot of I vs d showing linear slope −2κ
- Two testable predictions: P1: slope of ln(I) vs d equals exactly −2κ = −2.04 Å⁻¹; P2: reducing gap by 1 Å multiplies current by e^2 ≈ 7.4 (Binnig-Rohrer rule)
- Sim slug: medhavy-vol3-stm-tunneling
- Note: CROSS-REFERENCE — vox-stm-exponential is an explainer in quantum-mechanics-a-companion-guide. This is the simulation workflow reel showing Claude Code generating the scene; build it.

---

## Sim-02 — Fermi's Golden Rule: Transition Rate vs Perturbation Strength
- Source: `quantum-mechanics-vol3/chapters/06-radiation-and-fermis-golden-rule.md`
- Topic: CLAUDE CODE · MANIM
- Physical rule: Γ = 2π/ℏ |⟨f|V̂|i⟩|² ρ(E_f); rate proportional to |matrix element|² and density of states
- Concrete numbers: hydrogen 2p→1s: A coefficient = 6.27×10⁸ s⁻¹ (lifetime ≈ 1.6 ns); Lyman-α photon energy = 10.2 eV = hc/121.6 nm
- Visual artifact: energy levels with transition arrow; bar graph of rate vs coupling strength showing quadratic growth; log-log slope = 2
- Two testable predictions: P1: rate scales as |⟨f|V̂|i⟩|² (doubling the coupling quadruples the rate); P2: 2p→1s rate = 6.27×10⁸ s⁻¹ (matches NIST value)
- Sim slug: medhavy-vol3-golden-rule

---

## Sim-03 — Variational Principle: Every Guess Is Too High
- Source: `quantum-mechanics-vol3/chapters/03-the-variational-principle.md`
- Topic: CLAUDE CODE · MANIM
- Physical rule: ⟨ψ_trial|Ĥ|ψ_trial⟩ ≥ E₀; equality only when ψ_trial = ψ₀ exact
- Concrete numbers: Helium ground state E₀ = −79.0 eV (NIST); trial with Z*=2 (no screening) → −74.8 eV; trial with Z*=1.69 (optimized) → −77.5 eV; both above −79.0 eV
- Visual artifact: energy axis with true ground state floor; sequence of trial-state energies descending toward but never crossing the floor as Z* is optimized
- Two testable predictions: P1: Z*=2 gives −74.8 eV > E₀ (upper bound); P2: optimal Z*=27/16=1.6875 gives −77.5 eV, still above −79.0 eV
- Sim slug: medhavy-vol3-variational-floor
- Note: CROSS-REFERENCE — vox-variational-floor is an explainer in quantum-mechanics-vol3. The simulation workflow reel (Claude Code generating the variational calculation scene) is new; build it.

---

## Sim-04 — Perturbation Theory: Energy Levels Repel and Avoid Crossing
- Source: `quantum-mechanics-vol3/chapters/01-time-independent-perturbation-theory.md`
- Topic: CLAUDE CODE · MANIM
- Physical rule: E_n^(2) = Σ_{m≠n} |⟨m|Ĥ'|n⟩|²/(E_n^(0) − E_m^(0)); denominator shrinks → shift grows as gap closes
- Concrete numbers: two-level system with E₁=0, E₂=1 eV; coupling V=0.1 eV; avoided gap = 2V = 0.2 eV; energy levels never cross
- Visual artifact: two energy curves approaching each other as a knob turns; they bend apart instead of crossing; minimum gap = 2|V|
- Two testable predictions: P1: minimum gap = 2|⟨1|Ĥ'|2⟩| exactly at the degeneracy point; P2: set coupling to zero → levels cross freely; nonzero coupling → always avoid
- Sim slug: medhavy-vol3-avoided-crossing

---

<!-- ============================================================ -->
<!-- SIM-SCOUT CARDS — full schema, ordered by Score descending   -->
<!-- ============================================================ -->

## Candidate 01 — Animate: Rabi Oscillations vs. First-Order Perturbation Theory Breakdown
- Source: `quantum-mechanics-vol3/chapters/05-time-dependent-perturbation-theory-and-transitions.md`
- Topic: Quantum Transitions · Rabi Oscillations
- Lane: MANIM (directed animation)
- Hook: First-order perturbation theory confidently predicts a probability of 247% — the exact Rabi formula says "you're wrong, and the atom is already coming back."
- The rule: Exact two-level Rabi formula P(t) = sin²(Ωt/2) at resonance; first-order PT approximation P_PT(t) = (Ωt/2)². Both derived from Ĥ' = ℏΩcos(ωt) on a two-level system with detuning Δ = 0.
- Concrete numbers: ℏω₀ = 2.00 eV, ℏΩ = 0.010 eV; π-pulse time t_π = π/Ω ≈ 0.21 ps; at t = t_π, exact gives P = 1, PT gives P = (π/2)² ≈ 2.47; PT "predicts P = 1" at t_PT = 2/Ω ≈ 0.13 ps when true P = sin²(1) ≈ 0.708.
- The artifact / what moves: Two curves drawn in real time — sin²(Ωt/2) (bounded, oscillating) and (Ωt/2)² (a parabola climbing off the top of the frame). A red "INVALID" zone appears above P = 1. The PT curve crashes through it; the Rabi curve turns back.
- Output medium: Manim (mp4)
- Two testable predictions: P1: at Ωt = π (the first π-pulse), exact P = 1 exactly; PT gives P = π²/4 ≈ 2.47, which is >1. P2: PT and exact agree to within 10% only while Ωt < 0.55 rad (i.e., t < 0.55/Ω ≈ 0.036 ps for these parameters).
- The change: Reduce coupling to ℏΩ = 10⁻⁶ eV — the π-pulse stretches to ~2100 ps, coherence time (ns) is now shorter than one Rabi cycle, and the two curves are indistinguishable in the physical window. PT works.
- Human supplies (Claude can't): Nothing — fully synthetic/analytic.
- Teardown angle: A small parameter is not enough; the product Ωt is the actual control. The experiment fails not because coupling is small but because time is long.
- Exclusions: Counter-rotating terms (Bloch-Siegert shift), multi-level systems, decoherence.
- Sim slug: vol3-rabi-vs-pt-breakdown
- Score: 10/10

---

## Candidate 02 — Explore: Kronig-Penney Band Structure vs. Barrier Strength P
- Source: `quantum-mechanics-vol3/chapters/10-periodic-potentials-and-band-structure.md`
- Topic: Band Structure · Periodic Potentials
- Lane: D3/DATAVIZ (emergent / interactive)
- Hook: Zero potential → metals everywhere. Crank up the barrier → gaps carve out insulators. Watch the free-electron parabola fracture into forbidden zones in real time.
- The rule: Kronig-Penney dispersion relation cos(ka) = cos(αa) + (P/αa)sin(αa); allowed bands where |RHS| ≤ 1, forbidden gaps where |RHS| > 1. Energy E = ℏ²α²/2m.
- Concrete numbers: Units ℏ = 2m = a = 1 (energy in ℏ²/2ma²); sweep αa from 0 to 6π; slider P from 0 to 20. At P = 0: no gaps (free electrons). At P = 3π/2 ≈ 4.71: first gap opens at αa = π (E = π² ≈ 9.87) and extends to E ≈ 22.2. At P → ∞: bands collapse to zero width (isolated atoms).
- The artifact / what moves: Left panel: animated RHS curve f(αa) oscillating; horizontal band |f| ≤ 1 shaded; gap regions highlighted in red. Right panel: reduced-zone E(k) band diagram updating in real time as P slider moves. Bands narrow, gaps widen.
- Output medium: d3 v7 animated/interactive HTML
- Two testable predictions: P1: at P = 0, band diagram is a continuous parabola E = ℏ²k²/2m — no gaps. P2: at P = 3π/2, first band gap opens precisely at αa = π with gap width ΔE = E_second_band_bottom − π² > 0, computable to 4 significant figures from the dispersion relation.
- The change: Add a second slider for the number of bands displayed (1–5) and toggle between extended, reduced, and repeated zone schemes.
- Human supplies (Claude can't): Nothing — fully synthetic/analytic.
- Teardown angle: The gap is not a quantum weirdness add-on; it is where Bragg reflection makes a real k impossible. Larger barrier → stronger Bragg → wider gap → better insulator.
- Exclusions: 2D/3D band structure, spin-orbit coupling, DFT self-consistency.
- Sim slug: vol3-kronig-penney-explorer
- Score: 10/10
- Status: BUILT — `open /Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-vol3/youtube/vol3-kronig-penney-explorer/vol3-kronig-penney-explorer.html`

---

## Candidate 03 — Animate: Geiger-Nuttall Law — 24 Decades from One Exponent
- Source: `quantum-mechanics-vol3/chapters/04-the-wkb-approximation-and-tunneling.md`
- Topic: Alpha Decay · WKB Tunneling
- Lane: MANIM (directed animation)
- Hook: Two isotopes, same mechanism, half-lives differing by 10²⁴. One equation explains every point on a 33-decade straight line.
- The rule: Gamow factor γ = (1/ℏ)∫√(2m(V(r)−E))dr over the Coulomb barrier from R to r_c = 2Z′e²/4πε₀E_α; T ≈ e^(−2γ); log₁₀(τ₁/₂) ≈ A(Z′) + B(Z′)/√E_α (Geiger-Nuttall law).
- Concrete numbers: Po-212: E_α = 8.78 MeV, τ₁/₂ ≈ 3×10⁻⁷ s. Th-232: E_α = 4.08 MeV, τ₁/₂ ≈ 1.4×10¹⁰ yr. U-238: E_α = 4.27 MeV, Z′ = 90, R ≈ 7.4 fm, r_c ≈ 60 fm, γ ≈ 43, τ₁/₂(predicted) ≈ 5×10⁸ yr vs. measured 4.5×10⁹ yr (factor 10 on a 10²⁴ range).
- The artifact / what moves: Semi-log plot of half-life vs. 1/√E_α builds point by point as known alpha emitters are placed. A best-fit Geiger-Nuttall line appears. Inset: Coulomb barrier diagram with shaded forbidden zone shrinking as E_α slider increases, transmitting exponentially more.
- Output medium: Manim (mp4)
- Two testable predictions: P1: log₁₀(τ₁/₂) is linear in 1/√E_α — slope equals B(Z′) = πZ′e²√(2m)/ℏ (computable from known constants, no fitting). P2: Po-212 vs. U-238 ratio of half-lives is predicted to 10²³-fold by the Gamow exponent difference alone.
- The change: Add a second Z′ series (e.g., radium isotopes, Z′ = 86) — it plots as a parallel Geiger-Nuttall line, same slope, shifted intercept because B depends only on Z′.
- Human supplies (Claude can't): Nothing — empirical nuclide data is published (NNDC) and synthetic for animation purposes.
- Teardown angle: The 24-decade range is not variety among isotopes — it is the exponential amplification of a small energy difference through a barrier integral. The WKB exponent is the whole story; prefactors are invisible on this scale.
- Exclusions: Alpha pre-formation probability, nuclear structure corrections, even-odd staggering.
- Sim slug: vol3-geiger-nuttall-law
- Score: 9/10

---

## Candidate 04 — Explore: Rabi Oscillations vs. Detuning — the Resonance Landscape
- Source: `quantum-mechanics-vol3/chapters/05-time-dependent-perturbation-theory-and-transitions.md` + `quantum-mechanics-vol3/chapters/09-atoms-in-fields.md`
- Topic: Quantum Control · Resonance
- Lane: D3/DATAVIZ (emergent / interactive)
- Hook: One hertz of detuning in a 400 MHz NMR machine and you lose 99.5% of your spin flip. The formula makes "close enough" a calculable disaster.
- The rule: P_flip(t) = [Ω²/(Ω²+Δ²)] sin²(√(Ω²+Δ²) t/2); generalized Rabi frequency Ω_gen = √(Ω²+Δ²); max achievable flip probability P_max = Ω²/(Ω²+Δ²).
- Concrete numbers: Ω = 2π×1 kHz (NMR-scale Rabi), ω₀ = 2π×300 MHz, Δ slider from 0 to 10Ω. At Δ = 0: P_max = 1, full inversion. At Δ = Ω: P_max = 0.5. At Δ = 2Ω: P_max = 0.2. At Δ = 3Ω: P_max ≈ 0.1.
- The artifact / what moves: Live P_flip(t) curve oscillating as time plays forward; Δ slider changes detuning in real time, visibly capping the amplitude and speeding the oscillation. A second panel shows P_max(Δ) = 1/(1+(Δ/Ω)²) — a Lorentzian — with a vertical marker at the current Δ.
- Output medium: d3 v7 animated/interactive HTML
- Two testable predictions: P1: at Δ = Ω, the oscillation frequency increases by √2 relative to Δ = 0, while amplitude drops to exactly 1/2. P2: the full-width at half-maximum of P_max(Δ) equals 2Ω — set by the Rabi frequency, not the transition frequency ω₀.
- The change: Add a second Ω slider to show that increasing drive power widens the resonance window (power broadening) — the FWHM grows as 2Ω.
- Human supplies (Claude can't): Nothing — fully synthetic/analytic.
- Teardown angle: Frequency precision is not free — a sharper resonance (small Ω) requires longer pulse time; a shorter pulse (large Ω) broadens the resonance and excites neighbors. This trade-off is built into the formula.
- Exclusions: T₁/T₂ relaxation, inhomogeneous broadening, multi-spin systems, counter-rotating terms.
- Sim slug: vol3-rabi-detuning-landscape
- Score: 9/10
- Status: BUILT — `open /Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-vol3/youtube/vol3-rabi-detuning-landscape/vol3-rabi-detuning-landscape.html`

---

## Candidate 05 — Animate: Stark Effect — Four States Fan Into Three Lines
- Source: `quantum-mechanics-vol3/chapters/02-degenerate-perturbation-theory-and-fine-structure.md` + `quantum-mechanics-vol3/chapters/09-atoms-in-fields.md`
- Topic: Hydrogen Stark Effect · Degenerate Perturbation Theory
- Lane: MANIM (directed animation)
- Hook: Stark applied one field to four degenerate states and watched only three lines appear. Two states merged; one pair split symmetrically; one pair didn't budge. The 4×4 matrix has only two nonzero entries — and they explain everything Stark saw in 1913.
- The rule: Degenerate PT on the hydrogen n=2 manifold {|2s⟩, |2p₀⟩, |2p₊₁⟩, |2p₋₁⟩}. Perturbation W = eε̂z. Only ⟨2s|eεz|2p₀⟩ = −3a₀eε survives (parity + m_ℓ selection rules). Eigenvalues: ±3a₀eε, 0 (doubly degenerate). Splitting is linear in field ε.
- Concrete numbers: Electric field ε = 10⁵ V/m; 3a₀eε = 3×0.0529 nm×1.6×10⁻¹⁹ C×10⁵ V/m ≈ 2.54×10⁻²⁴ J ≈ 1.6×10⁻⁵ eV. Ground state (n=1) shift is quadratic, ΔE₁ = −(9/2)a₀³ε² ≈ −2.25×10⁻¹¹ eV — fourteen orders of magnitude smaller than the n=2 linear shift at this field.
- The artifact / what moves: Four horizontal energy lines degenerate at ε = 0. As the field slider moves right, two lines split symmetrically (±3a₀eε), two stay flat. Below, the 4×4 W matrix animates: most entries zero out in sequence (selection rules applied visually), leaving two nonzero off-diagonal entries that drive the split.
- Output medium: Manim (mp4)
- Two testable predictions: P1: splitting is linear in ε — slope = 6a₀e = 3.18×10⁻²⁸ J/(V/m). P2: |2p₊₁⟩ and |2p₋₁⟩ do not shift at all — they are unaffected by a z-directed field because ⟨m_ℓ = ±1|z|m_ℓ = ±1⟩ = 0 by m_ℓ conservation.
- The change: Rotate the field from ẑ to x̂ — the active 2×2 block shifts to {|2s⟩, (|2p₊₁⟩−|2p₋₁⟩)/√2} and the degenerate pair changes, but the eigenvalue magnitudes are identical (rotational symmetry of |e|).
- Human supplies (Claude can't): Nothing — fully synthetic/analytic.
- Teardown angle: The linear Stark effect is only possible because hydrogen has accidental Coulomb degeneracy. Every other atom has a quantum defect splitting s and p — so their Stark effect is always quadratic.
- Exclusions: Fine structure breaking the n=2 degeneracy, Lamb shift (separates 2s from 2p at ~4×10⁻⁶ eV), higher-order Stark corrections.
- Sim slug: vol3-stark-effect-n2
- Score: 9/10

---

## Candidate 06 — Explore: Hard-Sphere Scattering — 4 at Low Energy, 2 at High Energy
- Source: `quantum-mechanics-vol3/chapters/07-scattering-i-partial-waves.md`
- Topic: Quantum Scattering · Partial Waves
- Lane: D3/DATAVIZ (emergent / interactive)
- Hook: Classical physics says a hard sphere of radius a scatters πa² worth of particles. Quantum mechanics at low energy gives 4πa² — four times bigger. At high energy it gives 2πa² — still twice classical. Neither answer is πa².
- The rule: Total cross-section σ_tot = (4π/k²)Σ_ℓ (2ℓ+1)sin²δ_ℓ. For hard sphere: δ_ℓ = −ka (exact, all ℓ). Low energy ka ≪ 1: only ℓ=0 survives, σ→4πa². High energy ka ≫ 1: average sin²δ_ℓ → 1/2, sum to ka, σ→2πa².
- Concrete numbers: σ/πa² vs. ka from 0.01 to 30. At ka = 0.1: σ/πa² ≈ 3.96 (approaching 4). At ka = 20: σ/πa² ≈ 2.04 (approaching 2). Partial-wave sum needs ℓ_max ≈ ka terms.
- The artifact / what moves: σ_tot(ka)/πa² curve displayed as ka slider moves from 0 to 30. Partial-wave contributions shown as stacked bars — at small ka only the ℓ=0 bar is nonzero; at large ka many bars fill in. Horizontal reference lines at 4 and 2 and 1 (classical).
- Output medium: d3 v7 animated/interactive HTML
- Two testable predictions: P1: at ka → 0, σ_tot → 4πa² regardless of barrier shape — the s-wave always scatters isotropically with σ = 4πa_s² and the hard sphere gives a_s = a. P2: at ka = 1, the exact result (partial-wave sum) gives σ/πa² ≈ 3.5 — measurably below 4 and above 2, interpolating smoothly.
- The change: Replace the hard sphere with a spherical square well of tunable depth — Ramsauer-Townsend zeros appear at specific ka values where the phase shift passes through nπ and sin²δ₀ → 0.
- Human supplies (Claude can't): Nothing — fully synthetic/analytic.
- Teardown angle: The factor-of-4 at low energy is not an error; wave diffraction scatters isotropically into 4π steradians. The factor-of-2 at high energy is Babinet's principle: creating a shadow requires forward scattering equal to the geometric blocking.
- Exclusions: Inelastic scattering, spin-dependent forces, Coulomb corrections, identical-particle symmetrization.
- Sim slug: vol3-hard-sphere-crosssection
- Score: 9/10
- Status: BUILT — `open /Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-vol3/youtube/vol3-hard-sphere-crosssection/vol3-hard-sphere-crosssection.html`

---

## Candidate 07 — Animate: Tight-Binding Cosine Band and the Sign Flip of Effective Mass
- Source: `quantum-mechanics-vol3/chapters/10-periodic-potentials-and-band-structure.md`
- Topic: Solid-State · Tight-Binding Dispersion
- Lane: MANIM (directed animation)
- Hook: At the band bottom, an electron in a crystal is lighter than a free electron. At the band top, it has negative mass — push it left and it accelerates right. That sign flip is not a paradox; it is a cosine.
- The rule: E(k) = E₀ − 2t cos(ka), k ∈ [−π/a, π/a]. Effective mass m* = ℏ²/(d²E/dk²) = ℏ²/(2ta²). Near band bottom (k≈0): m* > 0. Near band top (k≈±π/a): m* < 0 (curvature flips sign). Bandwidth = 4t.
- Concrete numbers: a = 3 Å (silicon-like), t = 0.5 eV; m* at band bottom = ℏ²/(2×0.5×(3×10⁻¹⁰)²) ≈ 0.28 mₑ. Band top: m* = −0.28 mₑ. Bandwidth = 4t = 2.0 eV. At k = π/2a: E = E₀, curvature zero, m* → ±∞.
- The artifact / what moves: The cosine E(k) dispersion curve draws over the BZ. A parabola overlay at the band bottom (m*>0, teal) and at the band top (m*<0, orange) simultaneously animate. A "particle" slides along the curve; an arrow shows its group velocity v_g = (1/ℏ)dE/dk (tangent slope), which reverses sign at the zone boundary. As t slider increases, the bandwidth grows and curvatures steepen.
- Output medium: Manim (mp4)
- Two testable predictions: P1: group velocity v_g = (2ta/ℏ)sin(ka) — zero at k=0 and k=±π/a, maximum at k=±π/2a. P2: at k=π/2a, m* → ∞ (inflection point of cosine — zero second derivative). This is verifiable from d²E/dk².
- The change: Reduce t → 0 (isolated atoms): band flattens to E = E₀ everywhere, all states degenerate. Increase t → large: band widens, effective mass at bottom approaches free-electron value mₑ (NFE limit).
- Human supplies (Claude can't): Nothing — fully synthetic/analytic.
- Teardown angle: The tight-binding band is one orbital per atom doing one thing. Real silicon has four bands from sp³ hybridization. The cosine captures the topology (boundary conditions + periodicity) perfectly; the chemistry changes only the numbers.
- Exclusions: Multi-orbital tight-binding, spin-orbit in the band, Bloch wavefunctions (spatial), phonon renormalization.
- Sim slug: vol3-tight-binding-dispersion
- Score: 8/10

---

## Candidate 08 — Explore: Born Approximation Validity Map — where it Works and where it Fails
- Source: `quantum-mechanics-vol3/chapters/08-scattering-ii-the-born-approximation.md`
- Topic: Scattering · Born Approximation
- Lane: D3/DATAVIZ (emergent / interactive)
- Hook: Born gives exactly the right Rutherford formula even though its validity parameter η ≈ 22 ≫ 1 for gold-alpha scattering. But ask it about an s-wave resonance and it predicts nothing — the resonance is invisible to Born.
- The rule: Born differential cross-section dσ/dΩ = (m/2πℏ²)²|Ṽ(q)|² where q = 2k sin(θ/2). For Yukawa V(r) = V₀e^(−μr)/μr: dσ/dΩ = (2mV₀/ℏ²μ)²/(q²+μ²)². Valid when ξ = 2m|V₀|/ℏ²μ² ≪ 1 (low E) or ka ≫ ξ (high E). Breaks at resonances where exact cross-section peaks.
- Concrete numbers: Yukawa parameters: μ = 1 fm⁻¹ (pion range), V₀ variable from 10 to 200 MeV·fm. ξ = 2m|V₀|/ℏ²μ² with m = nucleon mass. ka = k/μ for incident nucleon. Born-predicted σ_tot vs. exact s-wave resonance at ka ≈ ξ.
- The artifact / what moves: 2D (ξ, ka) parameter-space map: green region (Born valid, ξ < 1 or ka > ξ), red region (Born fails). Sliders for V₀ and k move a crosshair. Right panel: angular distribution dσ/dΩ(θ) — Born (smooth) vs. exact partial-wave sum (shows resonance peak). At resonance parameter, Born's smooth curve misses the unitarity spike by orders of magnitude.
- Output medium: d3 v7 animated/interactive HTML
- Two testable predictions: P1: Born total cross-section for Yukawa scales as V₀²/(k²+μ²)² at fixed angle; doubling V₀ quadruples σ. P2: At the s-wave resonance (when δ₀ = π/2), the exact partial cross-section saturates the unitarity bound 4π/k², while Born predicts a value smaller by a factor of (1/ξ)² ≪ 1.
- The change: Switch from Yukawa to Coulomb (μ→0 with V₀/μ = Ze²/4πε₀): Born gives exact Rutherford — the σ vs. θ panel shows Born matching exact perfectly, demonstrating the Coulomb exception.
- Human supplies (Claude can't): Nothing — fully synthetic/analytic.
- Teardown angle: Born is a perturbation in V. Resonances are non-perturbative — the wave function inside the well is dramatically enhanced, exactly what Born assumes away. The validity diagram is the honest map of where the approximation lives.
- Exclusions: Second Born term, eikonal resummation, nuclear optical-model potential, Coulomb-nuclear interference.
- Sim slug: vol3-born-validity-map
- Score: 8/10
- Status: BUILT — `open /Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-vol3/youtube/vol3-born-validity-map/vol3-born-validity-map.html`

---

## Candidate 09 — Animate: Fine Structure of Hydrogen n=2 — Three Scales, Three Mechanisms
- Source: `quantum-mechanics-vol3/chapters/02-degenerate-perturbation-theory-and-fine-structure.md`
- Topic: Hydrogen Fine Structure · Perturbation Theory
- Lane: MANIM (directed animation)
- Hook: The Bohr model puts all eight n=2 states on one level. Fine structure splits them into two groups separated by 4.5×10⁻⁵ eV. The Lamb shift then lifts 2s above 2p by 4×10⁻⁶ eV more — and that tiny residual required inventing quantum electrodynamics to explain.
- The rule: Fine structure formula E_fs = −(E_n^(0))²/2mc² × (4n/(j+½) − 3). Depends only on n and j. Three corrections (relativistic kinetic, spin-orbit, Darwin) conspire to cancel ℓ-dependence. Lamb shift: QED vacuum fluctuation shifts 2s above 2p by ~1057 MHz.
- Concrete numbers: E₂^(0) = −3.4 eV. For j=½: E_fs = −5.66×10⁻⁵ eV; for j=3/2: E_fs = −1.13×10⁻⁵ eV. Fine-structure splitting ΔE_fs = 4.53×10⁻⁵ eV. Lamb shift ΔE_Lamb = 4×10⁻⁶ eV (one order of magnitude smaller). Hierarchy: 3.4 eV → 4.5×10⁻⁵ eV → 4×10⁻⁶ eV.
- The artifact / what moves: Three-stage animation. Stage 1: eight n=2 states stack at −3.4 eV. Stage 2: fine structure splits them — 2p₃/₂ separates upward, 2s₁/₂ and 2p₁/₂ remain degenerate. Stage 3: Lamb shift lifts 2s₁/₂ above 2p₁/₂. Each stage zooms in by one order of magnitude. A log-scale sidebar shows ΔE at each tier.
- Output medium: Manim (mp4)
- Two testable predictions: P1: the fine-structure formula gives identical energies for 2s₁/₂ and 2p₁/₂ (both j=½, both n=2) — predicts exact degeneracy. P2: fine-structure splitting ΔE_fs = 4.53×10⁻⁵ eV is calculable from the formula with no free parameters; Lamb shift is ~1/10 of this, as measured at 1057 MHz.
- The change: Extend to n=3 — compute E_fs for j=½, 3/2, 5/2 using the same formula and show which states share energy. The 3s₁/₂/3p₁/₂ degeneracy is the same story one level up.
- Human supplies (Claude can't): Nothing — fully synthetic/analytic.
- Teardown angle: The fine-structure formula has no ℓ in it — the three corrections (relativistic KE, spin-orbit, Darwin) are individually ℓ-dependent but their sum cancels ℓ out, revealing the hidden SO(4) symmetry. The Lamb shift breaks this: 2s and 2p differ by a QED mechanism that doesn't respect it.
- Exclusions: Hyperfine structure, Zeeman splitting of fine-structure levels, explicit perturbation-theory derivation of each of the three corrections.
- Sim slug: vol3-hydrogen-fine-structure
- Score: 8/10

---

## Candidate 10 — Explore: Sinc-Squared Lineshape Sharpening into Fermi's Golden Rule
- Source: `quantum-mechanics-vol3/chapters/05-time-dependent-perturbation-theory-and-transitions.md` + `quantum-mechanics-vol3/chapters/06-radiation-and-fermis-golden-rule.md`
- Topic: Transition Rates · Density of States
- Lane: D3/DATAVIZ (emergent / interactive)
- Hook: Leave the drive on longer and the resonance gets sharper — and somehow the total area under the spike keeps growing linearly in time even as the spike narrows as 1/t. This is how a Rabi oscillation becomes an irreversible rate.
- The rule: First-order transition probability P(δ,T) = (|V_fi|/ℏ)² sin²(δT/2)/(δ/2)². At large T: (sin²(δT/2))/(δ/2)² → (πT/2)δ_Dirac(δ). Rate dP/dt = (π/2)(|V_fi|/ℏ)² × δ_Dirac(ω_fi − ω) = (2π/ℏ)|V_fi|²ρ(E_f) (Fermi's golden rule).
- Concrete numbers: Three values of T = 1, 10, 100 in units of 2π/Δω (where Δω is the Bohr frequency ω_fi). Central peak height grows as T²; width at first zero = 2π/T; area under central peak grows as T. At T = 100: central peak is 100× narrower than at T = 1 but 10000× taller; area = 100× T=1 area.
- The artifact / what moves: Three overlaid sinc-squared curves for T = 1, 10, 100 animate sequentially. A shaded area under each central peak shows its integral. Right panel: peak height (log scale, slope +2) and peak width (log scale, slope −1) as T increases. Convergence to a delta function is visible.
- Output medium: d3 v7 animated/interactive HTML
- Two testable predictions: P1: peak height scales as T² (verifiable from formula: sin²(0)/(0+ε)² → T² as ε→0). P2: width to first zero scales as 2π/T — measured from the curve and confirmed analytically. Both scalings hold exactly, not approximately.
- The change: Add N discrete final states uniformly spaced in energy near E_f. As N increases from 2 to 50, the oscillatory P_total(t) washes out and converges to the linear golden-rule line W·t — showing the discrete→continuum transition.
- Human supplies (Claude can't): Nothing — fully synthetic/analytic.
- Teardown angle: Fermi's golden rule is not a new equation; it is the large-T limit of the sinc-squared formula applied to a continuum. The "irreversibility" is a density-of-states effect, not new physics.
- Exclusions: Counter-rotating terms in the perturbation, multi-photon processes, Wigner-Weisskopf resummation.
- Sim slug: vol3-sinc-squared-to-golden-rule
- Score: 8/10
- Status: BUILT — `open /Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-vol3/youtube/vol3-sinc-squared-to-golden-rule/vol3-sinc-squared-to-golden-rule.html`

---

## Candidate 11 — Explore: Zeeman Crossover — Weak-Field Fan to Paschen-Back Pattern
- Source: `quantum-mechanics-vol3/chapters/09-atoms-in-fields.md`
- Topic: Zeeman Effect · Angular Momentum
- Lane: D3/DATAVIZ (emergent / interactive)
- Hook: The "anomalous" Zeeman effect baffled physics for 30 years. Turn the field up high enough and the irregular multi-line pattern snaps into a simple regular triplet. The crossover is a continuous numerical diagonalization — there is no analytic formula for the middle.
- The rule: H = H_fs + H_Z; H_fs = A(L·S) sets fine-structure splitting ΔE_fs; H_Z = μ_B B(L̂_z + 2Ŝ_z)/ℏ. 6×6 matrix diagonalization at each B. Weak-field limit: g_J·μ_B·B·m_j (Landé g-factor). Strong-field limit: μ_B·B·(m_ℓ + 2m_s). Crossover at μ_B·B ~ ΔE_fs.
- Concrete numbers: Hydrogen 2p manifold, ℓ=1, s=½; ΔE_fs(2p) = 4.5×10⁻⁵ eV. Crossover field: B_c = ΔE_fs/μ_B = 4.5×10⁻⁵ eV / 5.79×10⁻⁵ eV/T ≈ 0.78 T. g_J for 2p₃/₂: 4/3; for 2p₁/₂: 2/3. B slider from 0 to 5 T.
- The artifact / what moves: Six energy level curves fan out from B=0 as B increases. At small B: weak-field Zeeman fan (unequal spacing from different g_J). At large B: Paschen-Back pattern (equal spacing from m_ℓ+2m_s = integer). In the middle: avoided crossings and non-analytic crossover computed numerically at each B.
- Output medium: d3 v7 animated/interactive HTML
- Two testable predictions: P1: at B → 0, energy shifts are ΔE = g_J μ_B B m_j with g_J exactly 4/3 (2p₃/₂) and 2/3 (2p₁/₂) — six levels with two different spacings. P2: at B → ∞ (Paschen-Back), the six levels cluster into four groups with values μ_B B × {−2, −1, 0, 0, +1, +2} corresponding to m_ℓ+2m_s combinations — equal spacing μ_B B.
- The change: Switch to the sodium D-line (3p manifold, ℓ=1) — same topology, larger fine-structure splitting, crossover at higher B. Both D₁ and D₂ lines visible.
- Human supplies (Claude can't): Nothing — fully synthetic/analytic (6×6 numerical diagonalization at each B point).
- Teardown angle: The intermediate field has no analytic formula. The "anomalous" Zeeman was anomalous only because spin was unknown — the numerical diagonalization fixes it entirely. The complexity lives entirely in the middle; both limits are simple.
- Exclusions: Hyperfine structure, nuclear spin coupling, diamagnetic term (B²), relativistic corrections to the Zeeman Hamiltonian.
- Sim slug: vol3-zeeman-crossover
- Score: 8/10
- Status: BUILT — `open /Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-vol3/youtube/vol3-zeeman-crossover/vol3-zeeman-crossover.html`

---

## Candidate 12 — Animate: H₂⁺ Bonding vs. Antibonding — Where Bonds Come From
- Source: `quantum-mechanics-vol3/chapters/03-the-variational-principle.md`
- Topic: Chemical Bonding · Variational Method
- Lane: MANIM (directed animation)
- Hook: Add an electron between two protons and you get a bond. Flip its phase and you get repulsion. The entire origin of every covalent bond in chemistry is destructive vs. constructive interference of two atomic orbitals.
- The rule: LCAO variational ansatz ψ± = (|A⟩ ± |B⟩)/√(2 ± 2S_AB). Bonding orbital ψ₊: constructive interference between nuclei. Antibonding ψ₋: node at midplane. E_total,±(R) = (H_AA ± H_AB)/(1 ± S_AB) + e²/4πε₀R. Overlap: S_AB(R) = e^(−R/a₀)(1 + R/a₀ + R²/3a₀²).
- Concrete numbers: H₂⁺ equilibrium: R_eq ≈ 1.3 Å (LCAO), experiment 1.06 Å; binding energy LCAO ≈ 1.77 eV, experiment 2.65 eV. Antibonding curve: purely repulsive, no minimum. S_AB(R=1.3 Å) ≈ 0.49.
- The artifact / what moves: Two E_total(R) curves animate — bonding (teal, has minimum) and antibonding (orange, purely repulsive) — as R sweeps from 0.3 to 6 Å. Electron density |ψ±|² shown in a side panel: bonding density peaks between nuclei, antibonding has a node. At R = R_eq, a dashed vertical line marks the equilibrium; the binding energy is annotated.
- Output medium: Manim (mp4)
- Two testable predictions: P1: the bonding curve has a minimum at R ≈ 1.3 Å with E_total,+ < −13.6 eV (the separated hydrogen + proton energy), confirming a bound state. P2: the antibonding curve E_total,−(R) > −13.6 eV for all R — it never dips below the dissociation threshold, so it never binds.
- The change: Add a second electron (H₂) — the bonding orbital fills with two spins, doubling the gain; the antibonding stays empty. Net binding ~ twice the one-electron gain minus the electron-electron repulsion. This shows why H₂ binds but He₂ does not (He₂ would fill both bonding and antibonding equally, canceling the gain).
- Human supplies (Claude can't): Nothing — fully synthetic/analytic.
- Teardown angle: The LCAO predicts the right minimum location to within 22% and misses binding energy by 33%. The miss comes from the fixed atomic orbitals — they can't polarize toward the other proton. The physics is right; the basis is too rigid.
- Exclusions: Molecular orbital theory beyond LCAO-MO, DFT geometry optimization, excited electronic states, vibrational/rotational structure.
- Sim slug: vol3-h2plus-lcao-bond
- Score: 8/10

---

## Candidate 13 — Animate: Quartic Oscillator — Perturbation Theory Breaks Faster at High n
- Source: `quantum-mechanics-vol3/chapters/01-time-independent-perturbation-theory.md`
- Topic: Perturbation Theory · Anharmonic Oscillator
- Lane: MANIM (directed animation)
- Hook: Adding a small quartic term to a harmonic oscillator doesn't destabilize the ground state — but it makes level n=4 fail at λ ten times smaller than n=0. The correction grows as n², turning a gentle perturbation into a catastrophe for excited states.
- The rule: Ĥ = Ĥ₀ + λx̂⁴; E_n^(1) = (3λ/4)(2n² + 2n + 1) in natural units ℏ = m = ω = 1. Breakdown criterion: |E_n^(1)|/ℏω ~ 1, i.e., λ ~ 1/(2n²+2n+1). Second-order correction E_n^(2) < 0 for all n, providing a sharper diagnostic.
- Concrete numbers: n=0: E₀^(1) = 3λ/4, breakdown at λ ~ 4/3 ≈ 1.3; n=1: E₁^(1) = 15λ/4, breakdown at λ ~ 4/15 ≈ 0.27; n=4: E₄^(1) = 30.75λ, breakdown at λ ~ 1/10.25 ≈ 0.097. For λ = 0.1: n=0 correction is 8% of level spacing (fine); n=4 correction is 307% (catastrophic).
- The artifact / what moves: Grouped bar chart of levels n=0 through 5 — unperturbed energies (grey bars) and first-order corrections (colored stacks). As λ slider increases, the colored stacks grow. A threshold line at "correction = level spacing" is crossed first by n=4, then n=3, then n=2, then n=1, then n=0, in order. Labels appear: "BREAKING" when the bar crosses the threshold.
- Output medium: Manim (mp4)
- Two testable predictions: P1: ratio of breakdown λ for n=0 vs. n=4 is (2×16+2×4+1)/(2×0+2×0+1) = 41, so n=4 fails at λ approximately 41× smaller than n=0. P2: E_n^(1) grows exactly as 2n²+2n+1 — quadratic in n — so plotting E^(1)/λ vs. n gives a parabola.
- The change: Show the Dyson argument: at λ < 0, the quartic potential goes to −∞, there is no bound state, and the series must diverge for ALL λ. The breakdown is not about being far from zero — it is that the radius of convergence is literally zero.
- Human supplies (Claude can't): Nothing — fully synthetic/analytic.
- Teardown angle: The Dyson argument: the series is divergent for every nonzero λ, but optimal truncation gives exponentially accurate results. "Convergent" and "useful" are not the same criterion.
- Exclusions: Resurgence theory, Borel summation, WKB connection to the divergent series.
- Sim slug: vol3-quartic-oscillator-breakdown
- Score: 7/10

---

## Candidate 14 — Explore: CdSe Quantum Dot Gap vs. Radius — Confinement Scaling
- Source: `quantum-mechanics-vol3/chapters/11-capstone-modeling-a-real-quantum-system.md`
- Topic: Quantum Confinement · Spherical Box Model
- Lane: D3/DATAVIZ (emergent / interactive)
- Hook: Shrink a semiconductor nanocrystal from 5 nm to 2 nm and watch the color of the emitted light shift from red to blue. The spherical-box formula predicts the trend; it overestimates at small R because effective mass is not constant.
- The rule: E_dot = E_bulk + ℏ²π²/2m_e*R² + ℏ²π²/2m_h*R² − 1.8e²/4πε₀ε_r R. For CdSe: E_bulk = 1.74 eV, m_e* = 0.13 mₑ, m_h* = 0.45 mₑ, ε_r = 10.6. E∝1/R² confinement term dominates at small R.
- Concrete numbers: R = 3 nm (6 nm dot): E_dot predicted 2.44 eV, measured ~2.10 eV (CdSe literature). R = 1.5 nm: predicted 3.23 eV, measured 2.44 eV (32% error from effective-mass nonparabolicity). R = 5 nm: predicted 1.87 eV, measured ~1.84 eV (2% error — near-bulk, model valid).
- The artifact / what moves: E_dot(R) theory curve + experimental data points (Norris-Bawendi 1996) displayed on the same plot. R slider moves a vertical marker; a color swatch shows the photon color (wavelength = hc/E_dot). Theory curve and data diverge at small R; converge at large R. Error annotation appears at each R.
- Output medium: d3 v7 animated/interactive HTML
- Two testable predictions: P1: E_dot − E_bulk scales as 1/R² at large R (confinement dominates) — verify from the theory curve slope on a log-log plot. P2: Coulomb correction term (−1.8e²/4πε₀ε_r R) scales as 1/R — at R = 3 nm it contributes −0.16 eV, reducing the gap by ~7%; computable exactly.
- The change: Switch to ZnS (larger E_bulk = 3.7 eV, smaller ε_r = 8.5, different m*) — the curve shifts up, and the confinement energy at the same R is larger because of different effective masses.
- Human supplies (Claude can't): Norris-Bawendi (1996) data points for CdSe — available from the published paper or a standard database.
- Teardown angle: The model gets the trend right (1/R² scaling) and quantitatively works at large R. At small R the effective mass itself depends on k, which depends on R — the model eats its own input. This is what "breakdown" looks like when the error is in the input, not the formula.
- Exclusions: Many-body effects, nonparabolicity correction explicitly, shape corrections (non-spherical dots), surface trap states.
- Sim slug: vol3-quantum-dot-confinement
- Score: 7/10
- Status: BUILT — `open /Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-vol3/youtube/vol3-quantum-dot-confinement/vol3-quantum-dot-confinement.html`

---

## Candidate 15 — "Animate the Breit-Wigner Resonance: Phase Shift Through π/2"
- Source: `quantum-mechanics-vol3/chapters/07-scattering-i-partial-waves.md`
- Topic: Scattering resonance — s-wave cross-section hitting the unitarity limit
- Lane: MANIM (directed animation)
- Hook: At exactly the right energy, a repulsive-looking sphere suddenly scatters particles 40 times better than its geometric size predicts. The cross-section rockets to 4π/k² — the quantum maximum — because the phase shift passed through π/2 and sin²δ₀ hit exactly 1.
- The rule: σ₀(E) = (4π/k²)sin²δ₀(E); near resonance: tan δ₀ = (Γ/2)/(E_R − E); σ₀(E) = (4π/k_R²) · (Γ/2)² / [(E−E_R)² + (Γ/2)²] (Breit-Wigner Lorentzian); peak when E = E_R, δ₀ = π/2, σ₀_peak = 4π/k_R²
- Concrete numbers: E_R = 1.00 eV, Γ = 0.20 eV (narrow resonance), m = mₑ; k_R = √(2mE_R)/ℏ ≈ 5.13 nm⁻¹; unitarity limit 4π/k_R² ≈ 0.476 nm²; geometric cross-section πa² with a = 0.1 nm → πa² ≈ 0.031 nm² (factor 15 smaller); at E = E_R + Γ/2 = 1.10 eV, σ₀ drops to half maximum — exactly 0.238 nm²; at E = 0.5 eV (far off resonance), σ₀ ≈ 1.8×10⁻³ nm² (264× below peak)
- The artifact / what moves: Two synchronized panels. Top panel: σ₀(E)/σ_classical Lorentzian curve draws in real time as an energy cursor sweeps left to right through E_R; a horizontal dashed line marks the unitarity ceiling 4π/k²; the Lorentzian peak visibly overshoots the classical geometric value by 15×. Bottom panel: phase shift δ₀(E) curve simultaneously sweeping from 0 through π/2 at E_R (peak of σ) to π at E_R + Γ; a vertical dashed marker locks to the cursor; the moment δ₀ = π/2 is labeled "UNITARITY MAXIMUM" and the sigma panel peaks simultaneously. A numerical readout shows σ₀/σ_classical at each E
- Output medium: Manim (mp4)
- Two testable predictions: P1: peak cross-section = 4π/k_R² = 0.476 nm² exactly when δ₀ = π/2 — not approximate, this is sin²(π/2) = 1 in the formula; P2: full-width at half-maximum of σ₀(E) equals Γ = 0.20 eV exactly — reading the width between the two E values where σ₀ = σ_peak/2 gives the resonance lifetime via τ = ℏ/Γ ≈ 3.3 fs
- The change: Widen Γ to 1.0 eV (broad resonance) — the Lorentzian broadens, peak stays at unitarity but the "resonance" becomes a wide bump that no longer looks like a sharp feature; compare τ_narrow/τ_broad = 5 — demonstrating the inverse time-width relation
- Human supplies (Claude can't): Nothing — fully synthetic/analytic
- Teardown angle: The resonance is not a bound state — the particle is not trapped. It is a quasi-bound state living for time τ = ℏ/Γ inside the potential before escaping. The cross-section spike reveals the presence of an almost-bound-state sitting just above threshold, visible only because the wave equation remembers what the potential almost did
- Exclusions: Multi-channel resonances, Fano resonances (asymmetric lineshape from continuum-bound interference), compound nuclear resonances (many overlapping levels), Feshbach resonances in ultracold physics
- Sim slug: vol3-breit-wigner-resonance
- Score: 10/10

---

## Candidate 16 — "Animate the Nuclear Form Factor: Diffraction Reveals the Proton's Size"
- Source: `quantum-mechanics-vol3/chapters/08-scattering-ii-the-born-approximation.md`
- Topic: Born approximation — nuclear form factor as Fourier transform of charge density
- Lane: MANIM (directed animation)
- Hook: Electrons scatter off gold nuclei and the angular distribution has a zero at a specific angle. That zero is not a coincidence — it is the first zero of J₁(qR)/qR, and reading off the angle gives you the nuclear radius to femtometer precision. A diffraction pattern becomes a ruler.
- The rule: dσ/dΩ = (dσ/dΩ)_point × |F(q)|²; F(q) = 3[sin(qR) − qR cos(qR)]/(qR)³ for uniform sphere; first zero at qR = 4.493; q = 2k sin(θ/2); R extracted from θ_zero via R = 4.493/(2k sin(θ_zero/2))
- Concrete numbers: Gold nucleus (A=197, Z=79): R ≈ 1.2 × 197^{1/3} fm ≈ 7.0 fm; electron beam at E = 250 MeV → k ≈ 1.27 fm⁻¹; first form-factor zero at θ_zero: qR = 4.493 → q = 0.642 fm⁻¹ → sin(θ_zero/2) = 0.253 → θ_zero ≈ 29.3°; at θ_zero the point-nucleus Rutherford prediction gives dσ/dΩ ≈ 1400 fm²/sr but measured cross-section → 0; factor suppression at first zero is formally infinite
- The artifact / what moves: Angular distribution dσ/dΩ(θ) draws as θ sweeps from 0° to 90°. Two curves animate simultaneously: Rutherford (dashed orange, smooth 1/sin⁴ decline — no zeros) and form-factor-modified Born (solid blue, oscillating with zeros). At each zero, the blue curve touches zero while the orange curve remains large — the contrast at θ_zero is labeled "∞× suppression." A side inset shows the uniform sphere charge density with radius R and a ruler annotation. A second slider changes R: as R increases, θ_zero shifts left (first zero moves to smaller angles — larger nucleus diffracts at smaller angles)
- Output medium: Manim (mp4)
- Two testable predictions: P1: first zero of |F(q)|² occurs at qR = 4.493 (first zero of 3j₁(qR)/qR) — at E=250 MeV electrons on Au-197, this gives θ_zero ≈ 29.3°, computable exactly from known constants; P2: the ratio of the first-zero angle to the second-zero angle (second at qR ≈ 7.72) is 4.493/7.725 ≈ 0.582 — a fixed numerical ratio independent of R or k, verifiable from the form factor formula
- The change: Replace uniform sphere with Gaussian charge density ρ(r) ∝ exp(−r²/2a²) — form factor becomes F(q) = exp(−q²a²/2) with no zeros (Gaussian Fourier transform is Gaussian); the oscillatory diffraction minima disappear entirely, demonstrating that the zeros are a signature of the sharp nuclear surface, not of scattering per se
- Human supplies (Claude can't): Nothing — fully synthetic/analytic (Hofstadter data can be sketched from the analytic formula; no external data file needed for the animation)
- Teardown angle: Hofstadter won the 1961 Nobel Prize for measuring proton charge radii this way. The entire technique rests on one fact: Born approximation makes dσ/dΩ factorize into a point-scatterer piece times |F(q)|² — and F(q) is just the Fourier transform of the charge distribution. Every diffraction experiment on nuclei or protons is a Born-approximation Fourier transform with a different basis
- Exclusions: Multiple scattering corrections (Glauber theory), inelastic form factors, spin-dependent charge distributions, quark substructure (deep inelastic scattering)
- Sim slug: vol3-form-factor-diffraction
- Score: 8/10
