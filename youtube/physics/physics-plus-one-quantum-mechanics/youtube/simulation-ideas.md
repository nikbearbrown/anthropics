# Physics: Quantum Mechanics (Plus One) — Simulation Ideas

**Pilot run: MANIM lane only — D3/DATAVIZ candidates deferred to a second pass.**

*sim-scout run 2026-07-26 — chapters read: 01, 03, 11 and supporting chapters.*

---

## Candidate 01 — Animate "Harmonic Oscillator Ladder: Energy Levels E_n = (n + ½)ℏω"
- Source: `physics-plus-one-quantum-mechanics/chapters/03-the-harmonic-oscillator.md`
- Topic: Quantum harmonic oscillator / ladder operators
- Lane: MANIM (directed animation)
- Hook: The quantum harmonic oscillator cannot have zero energy — even the ground state vibrates with ½ℏω of zero-point energy. This is not classical noise; it is a consequence of the uncertainty principle, and it is why liquid helium never freezes under atmospheric pressure.
- The rule: Ĥ = p̂²/2m + ½mω²x̂². Ladder operators â± = (1/√(2mℏω))(mωx̂ ∓ ip̂). Energy eigenvalues: E_n = (n + ½)ℏω, n = 0, 1, 2, …. â+|n⟩ = √(n+1)|n+1⟩; â−|n⟩ = √n|n−1⟩.
- Concrete numbers: ω = 2π × 10¹² rad/s (optical phonon, near-infrared). ℏ = 1.055×10⁻³⁴ J·s. E₀ = ½ℏω = ½ × 1.055×10⁻³⁴ × 2π×10¹² = 3.31×10⁻²² J = 2.07 meV. E₁ = (3/2)ℏω = 6.21 meV. Spacing ℏω = 4.14 meV = same between every adjacent pair.
- The artifact / what moves: A parabolic potential well V(x) = ½mω²x² draws. Energy levels E₀, E₁, E₂, E₃, E₄ draw as horizontal lines inside the well, equally spaced. A "ladder" visual: â+ arrow lifts from level n to n+1 (labeled √(n+1)); â− arrow drops (labeled √n). The |ψ_n(x)|² probability densities for n = 0..4 animate as overlays, each showing n nodes. Zero-point energy ½ℏω is highlighted — the n = 0 level is conspicuously above the potential minimum.
- Output medium: Manim (mp4)
- Two testable predictions: P1: E_n are equally spaced: E_{n+1} − E_n = ℏω for all n — the spacing is uniform, independent of n, visible as equal gaps between horizontal lines. P2: Ground state |ψ₀|² is a Gaussian centered at x = 0 with width σ = √(ℏ/2mω) — zero nodes, maximum at origin, confirming the zero-point energy sits above the classical turning point.
- The change: Compare to a classical oscillator: at the same total energy E = ½ℏω, the classical particle slows near the turning points and speeds through the center — the probability density is U-shaped (piling up at the edges). The quantum ground state is Gaussian (maximum at center). The inversion is the surprise.
- Human supplies (Claude can't): Nothing — fully synthetic/analytic.
- Teardown angle: Zero-point energy is not a technicality. It is why helium stays liquid at 4 K. It is why atoms in a crystal vibrate even at absolute zero (Casimir effect uses it). The ladder operator is an elegant algebraic machine that makes the whole spectrum fall out without solving a differential equation.
- Exclusions: Coherent states; Husimi Q-function; anharmonic corrections; molecular vibration selection rules (Δn=±1); squeezed states.
- Sim slug: qm-harmonic-ladder
- Score: 9/10

---

## Candidate 02 — Animate "WKB Tunneling: The Gamow Factor and the Geiger-Nuttall Law"
- Source: `physics-plus-one-quantum-mechanics/chapters/11-the-wkb-approximation-and-tunneling.md`
- Topic: WKB approximation / quantum tunneling
- Lane: MANIM (directed animation)
- Hook: An alpha particle inside a nucleus sees a barrier it classically cannot cross — yet it escapes. The transmission probability is e^{−2G} where G is the Gamow factor, an integral of the tunneling momentum through the barrier. Small changes in energy produce enormous changes in decay rate, explaining why uranium-238 (4.5 billion year half-life) and polonium-212 (0.3 microseconds) can both exist.
- The rule: WKB tunneling amplitude: T ≈ e^{−2G}, G = (1/ℏ)∫_{x_1}^{x_2} √(2m(V(x)−E)) dx (Gamow factor). Geiger-Nuttall: log(t_{1/2}) ∝ 1/√E_α (empirical; WKB explains it).
- Concrete numbers: Alpha particle: m = 6.644×10⁻²⁷ kg. U-238: E_α = 4.27 MeV, t_{1/2} = 4.5×10⁹ yr. Po-212: E_α = 8.78 MeV, t_{1/2} = 0.3 μs. Energy change factor: 8.78/4.27 ≈ 2.06. Half-life ratio: 4.5×10⁹ yr / 0.3×10⁻⁶ s ≈ 4.7×10²³. Same exponential factor in e^{−2G}.
- The artifact / what moves: A nuclear potential curve draws: deep well (nuclear potential) with a Coulomb barrier hump. E_α shown as a horizontal line below the barrier peak. The classically forbidden region is shaded. The WKB wavefunction draws: oscillatory inside the well, exponentially decaying through the barrier, oscillatory outside. A slider for E_α moves the energy line — as E_α rises, the shaded barrier area shrinks, G drops, and T = e^{−2G} rises exponentially. A Geiger-Nuttall log(t_{1/2}) vs 1/√E_α line draws with U-238 and Po-212 plotted.
- Output medium: Manim (mp4)
- Two testable predictions: P1: Geiger-Nuttall law: log(t_{1/2}) is linear in 1/√E_α — visible as a straight line on a log(λ) vs E_α^{−1/2} plot, with U-238 and Po-212 both landing on it. P2: T = 0 in the classical limit: if E_α > V_barrier (barrier disappears), the exponent e^{−2G} → e^0 = 1 (full transmission) — visible at high E in the slider sweep.
- The change: Show barrier width effect: hold E_α fixed, change the nuclear radius (barrier width) — wider barrier → smaller T, exponentially. Two nuclei same E_α but different radii have dramatically different half-lives, making the geometry of the barrier tangible.
- Human supplies (Claude can't): Nothing — fully synthetic/analytic.
- Teardown angle: Uranium-238 and Polonium-212 differ in half-life by 10²³. The WKB Gamow factor changes by a factor of log(10²³) ≈ 53 in the exponent. A factor of two in alpha energy changes decay rate by 23 orders of magnitude. This is exponential sensitivity — the most violent mathematical relationship in nuclear physics.
- Exclusions: Full derivation of WKB connection formulas at turning points; Breit-Wigner resonance; proton tunneling in fusion; tunneling in field effect transistors.
- Sim slug: qm-wkb-tunneling
- Score: 9/10

---

## Candidate 03 — Animate "Gaussian Wave Packet: Minimum Uncertainty and σ_x σ_p = ℏ/2"
- Source: `physics-plus-one-quantum-mechanics/chapters/01-the-wave-function.md`
- Topic: Heisenberg uncertainty principle / Gaussian wave packets
- Lane: MANIM (directed animation)
- Hook: The Gaussian wave packet is the unique quantum state that saturates the Heisenberg uncertainty bound: σ_x σ_p = ℏ/2 exactly, with nothing left over. Every other state does worse. Tighten the spatial spread and the momentum spread widens by exactly the same factor — a see-saw that cannot be beaten.
- The rule: ψ(x) = (2πa²)^{−1/4} e^{−x²/4a²}: σ_x = a. Momentum space: φ̃(p) = (2πℏ²/a²)^{−1/4} e^{−p²a²/2ℏ²}: σ_p = ℏ/(2a). Product: σ_x σ_p = ℏ/2 (minimum). Kennard inequality: σ_x σ_p ≥ ℏ/2.
- Concrete numbers: a = 1 nm → σ_x = 1 nm, σ_p = ℏ/(2×10⁻⁹) = 1.055×10⁻³⁴/(2×10⁻⁹) = 5.28×10⁻²⁶ kg·m/s. Mass m = 9.109×10⁻³¹ kg (electron): σ_v = σ_p/m = 5.80×10⁴ m/s = 58 km/s. Tightening to a = 0.1 nm: σ_v = 580 km/s.
- The artifact / what moves: Two panels: left shows |ψ(x)|² (position space Gaussian, width σ_x = a). Right shows |φ̃(p)|² (momentum space Gaussian, width σ_p = ℏ/2a). A single slider "a" changes both simultaneously: as a decreases, the position Gaussian narrows, the momentum Gaussian widens by the same factor (the product σ_x σ_p stays at ℏ/2, labeled). The product σ_x σ_p is displayed numerically in real time — it stays at ℏ/2 throughout the slider sweep. A third panel shows the see-saw schematically.
- Output medium: Manim (mp4)
- Two testable predictions: P1: σ_x × σ_p = a × ℏ/(2a) = ℏ/2 — the product is constant at every value of a, confirmed by numerical display throughout slider sweep. P2: At a = 0.1 nm (atom scale), σ_p = ℏ/(2×10⁻¹⁰) = 5.28×10⁻²⁵ kg·m/s → σ_v = 580 km/s for an electron — a confinement velocity larger than Earth escape velocity.
- The change: Compare to a non-Gaussian state (e.g., uniform/box distribution in x): σ_x σ_p > ℏ/2, showing the Gaussian is special as the minimum-uncertainty state. The box state in momentum space has slower-falling tails (sinc function) and a strictly larger σ_p.
- Human supplies (Claude can't): Nothing — fully synthetic/analytic.
- Teardown angle: The uncertainty principle is not about disturbing the particle with your measurement. It is built into the wave — any function that is narrow in x must be wide in p, by the mathematics of Fourier transforms. The Gaussian is the one function that is equally wide in both senses (in the right units), sitting exactly at the limit.
- Exclusions: Robertson generalized uncertainty; time-energy uncertainty; squeezed states that circumvent position uncertainty; quantum noise in optomechanics.
- Sim slug: qm-gaussian-uncertainty
- Score: 9/10

---

## Candidate 04 — Animate "Probability Current: Continuity Equation Makes Probability Flow"
- Source: `physics-plus-one-quantum-mechanics/chapters/01-the-wave-function.md`
- Topic: Probability current / continuity equation
- Lane: MANIM (directed animation)
- Hook: Quantum probability is not just a number — it flows. The probability current J tells you how quickly probability is moving past any point in space. If probability piles up somewhere, it must have flowed in from somewhere else: the continuity equation is probability conservation made local.
- The rule: J = (ℏ/2mi)(ψ* ∂ψ/∂x − ψ ∂ψ*/∂x) = (ℏ/m) Im(ψ* ∂ψ/∂x). Continuity: ∂|ψ|²/∂t = −∂J/∂x. For a plane wave ψ = Ae^{ikx}: J = ℏk|A|²/m = |A|²v (probability density × group velocity).
- Concrete numbers: Electron, ψ = A e^{ikx}: k = 2π/λ, λ = 1 nm. v = ℏk/m = 1.055×10⁻³⁴ × 2π/10⁻⁹ / 9.109×10⁻³¹ = 7.26×10⁵ m/s. J = |A|² × 7.26×10⁵ m/s. For a Gaussian packet moving at v₀: J(x,t) peaks where |ψ|² peaks, moves with the packet, equals zero in the tail.
- The artifact / what moves: A moving Gaussian wave packet |ψ(x,t)|² animates as it travels to the right. Below it, the probability current J(x,t) animates as an arrow field — positive (rightward) under the packet, near-zero far from it. The continuity equation is shown: at the leading edge of the packet, J is positive (probability flowing in); at the trailing edge, J is negative (probability flowing out). The integral ∫|ψ|²dx is displayed as a constant — normalization is conserved.
- Output medium: Manim (mp4)
- Two testable predictions: P1: For a rightward-moving plane wave ψ = Ae^{ikx}, J = ℏk|A|²/m > 0 everywhere — probability flows uniformly rightward at velocity v = ℏk/m. P2: For ψ = A cos(kx) (real standing wave): J = 0 everywhere — real wavefunctions have zero probability current (no net flow, confirming bound-state solutions carry no current).
- The change: Apply to tunneling: show the probability current on both sides of a barrier — incident + reflected on the left, transmitted on the right. The ratio J_transmitted / J_incident is the transmission coefficient T, directly visualized.
- Human supplies (Claude can't): Nothing — fully synthetic/analytic.
- Teardown angle: The continuity equation is not an assumption — it follows from the Schrödinger equation. Probability is locally conserved. You cannot have probability disappear from one place and reappear somewhere else without flowing through the intervening space. This is what makes quantum mechanics a theory, not a collection of rules.
- Exclusions: Three-dimensional J; current in the hydrogen atom (circulating states); probability current in relativistic Dirac equation; supercurrent in superconductors.
- Sim slug: qm-probability-current
- Score: 8/10

---

## Candidate 05 — Animate "Free Packet Spreading: σ_x(t) Grows as √(1 + (t/t_spread)²)"
- Source: `physics-plus-one-quantum-mechanics/chapters/01-the-wave-function.md`
- Topic: Wave packet spreading / free evolution
- Lane: MANIM (directed animation)
- Hook: Release a quantum particle with a definite position and it immediately starts spreading. The uncertainty principle guarantees it — a narrow x means wide p, and different momentum components travel at different speeds. Within one spreading time, a 1-nm electron packet has doubled its width.
- The rule: Free evolution: i ℏ ∂ψ/∂t = −(ℏ²/2m) ∂²ψ/∂x². Gaussian packet width: σ_x(t) = σ_0 √(1 + (ℏt/2mσ_0²)²) = σ_0 √(1 + (t/t_spread)²), where t_spread = 2mσ_0²/ℏ.
- Concrete numbers: Electron (m = 9.109×10⁻³¹ kg), σ_0 = 1 nm. t_spread = 2 × 9.109×10⁻³¹ × (10⁻⁹)² / 1.055×10⁻³⁴ = 1.73×10⁻¹⁴ s = 17.3 femtoseconds. At t = t_spread: σ_x = √2 × 1 nm = 1.41 nm. At t = 10 t_spread: σ_x ≈ 10 nm. Proton same σ_0 = 1 nm: t_spread_proton ≈ 1 836 × 17.3 fs = 31.8 ps — proton spreads 1836× slower.
- The artifact / what moves: A |ψ(x,t)|² Gaussian (normalized) animates spreading over time. σ_x(t) is labeled in real time, growing from σ_0 = 1 nm. Below, a σ_x(t) vs t curve draws, following the hyperbolic growth √(1 + (t/t_spread)²). At t = 0: minimum width. At t = t_spread: √2 × σ_0. The packet visibly flattens and widens while maintaining normalization (area under |ψ|² stays 1). A proton packet (same σ_0) is overlaid for comparison — much slower spreading.
- Output medium: Manim (mp4)
- Two testable predictions: P1: At t = t_spread, σ_x = √2 × σ_0 — the width has grown by exactly factor √2, a clean prediction verifiable from the formula. P2: For a proton vs electron, same initial σ_0: t_spread scales as mass, so proton t_spread = 1836 × electron t_spread — the proton packet spreads 1836× more slowly at any given time.
- The change: Show the momentum-space width σ_p(t): it stays constant (momentum distribution doesn't change under free evolution). This makes the see-saw vivid — the position spreads but the momentum is frozen, which is exactly the content of the free Schrödinger equation.
- Human supplies (Claude can't): Nothing — fully synthetic/analytic.
- Teardown angle: Free wave packet spreading is not a quantum mystery — it is wave mechanics. The same thing happens to a water wave pulse: different wavenumber components travel at different group velocities and the pulse disperses. Quantum mechanics adds only the probability interpretation. The spreading happens whether you watch or not.
- Exclusions: Wavepacket in a potential well (revivals); Gaussian wavepacket in a harmonic trap (coherent state, no spreading); fractional revivals; spreading in curved spacetime.
- Sim slug: qm-packet-spreading
- Score: 8/10

---

## Candidate 06 — Animate "Bohr-Sommerfeld: Phase-Space Ellipse Quantization ∮p dx = (n+½)h"
- Source: `physics-plus-one-quantum-mechanics/chapters/11-the-wkb-approximation-and-tunneling.md`
- Topic: WKB / Bohr-Sommerfeld quantization
- Lane: MANIM (directed animation)
- Hook: Before Schrödinger, Bohr and Sommerfeld quantized orbits by requiring the phase-space area enclosed by a classical trajectory to be an integer multiple of Planck's constant. For a harmonic oscillator, this phase-space ellipse has exactly area (n+½)h — the WKB refinement adds the ½ that Bohr missed.
- The rule: Bohr-Sommerfeld (WKB): ∮ p dx = (n + ½)h, n = 0, 1, 2, … For the harmonic oscillator: the phase-space trajectory is an ellipse with semi-axes x_max = √(2E/mω²) and p_max = √(2mE). Area = π × x_max × p_max = 2πE/ω = E×(2π/ω) = Eh/(ℏω) = nh → E_n = nℏω. WKB ½ correction: E_n = (n + ½)ℏω.
- Concrete numbers: n = 0 (ground state): ∮ p dx = ½h = h/2. Area of phase-space ellipse = ½h = 3.313×10⁻³⁴ J·s. n = 1: area = (3/2)h. n = 2: area = (5/2)h. Ratio of consecutive areas: always equals h (one quantum of phase-space area per level).
- The artifact / what moves: Phase space (x-axis: position, p-axis: momentum) is the canvas. For n = 0, 1, 2, 3, four nested ellipses draw. Each ellipse is labeled E_n = (n+½)ℏω and ∮ p dx = (n+½)h. The area between consecutive ellipses is shaded and labeled as h (exactly one Planck unit per level). A classical trajectory dot orbits each ellipse. The discrete quantum levels emerge from a continuous phase-space area quantization — the quantum condition is one picture.
- Output medium: Manim (mp4)
- Two testable predictions: P1: Ellipse area for n = 0 is h/2 = 3.313×10⁻³⁴ J·s — computed from π × x_max × p_max with E₀ = ½ℏω. P2: Area between n = 1 and n = 0 ellipses = (3/2)h − (1/2)h = h — exactly one Planck unit, regardless of ω or m.
- The change: Apply to the particle in a box: ∮ p dx = 2pL = nh (no ½ correction because there are no classical turning points). Comparing the box quantization (2pL = nh) to the oscillator (ellipse area = (n+½)h) shows why the ½ matters and when it appears.
- Human supplies (Claude can't): Nothing — fully synthetic/analytic.
- Teardown angle: Bohr's original quantization rule (∮ p dx = nh) is wrong by ½. The WKB correction (the Maslov index from the two turning points) adds the ½ that matches experiment. The same phase-space ellipse picture connects classical mechanics to quantum mechanics through one geometric fact: nature counts area in units of h.
- Exclusions: EBK quantization in 3D (separability conditions); Maslov index in detail; modern path-integral derivation; quantum chaology (non-separable systems).
- Sim slug: qm-bohr-sommerfeld
- Score: 8/10

---

| # | Title | Lane | Score | Slug |
|---|---|---|---|---|
| 01 | Harmonic Oscillator Ladder: E_n = (n+½)ℏω | MANIM | 9 | qm-harmonic-ladder |
| 02 | WKB Tunneling: Gamow Factor | MANIM | 9 | qm-wkb-tunneling |
| 03 | Gaussian Wave Packet: σ_x σ_p = ℏ/2 | MANIM | 9 | qm-gaussian-uncertainty |
| 04 | Probability Current: Continuity Equation | MANIM | 8 | qm-probability-current |
| 05 | Free Packet Spreading: σ_x(t) Grows | MANIM | 8 | qm-packet-spreading |
| 06 | Bohr-Sommerfeld: Phase-Space Ellipse | MANIM | 8 | qm-bohr-sommerfeld |

*6 candidates. MANIM: 6. D3/DATAVIZ: 0 (deferred). Score ≥8: 6.*
