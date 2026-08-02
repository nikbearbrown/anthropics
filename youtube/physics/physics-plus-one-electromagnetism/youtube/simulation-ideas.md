# Physics: Electromagnetism (Plus One) — Simulation Ideas

**Pilot run: MANIM lane only — D3/DATAVIZ candidates deferred to a second pass.**

*sim-scout run 2026-07-26 — chapters read: 02, 04, 10 and supporting chapters.*

---

## Candidate 01 — Animate "Faraday's Law: Moving Magnet, Changing Flux, Induced EMF"
- Source: `physics-plus-one-electromagnetism/chapters/10-electromagnetic-induction.md`
- Topic: Electromagnetic induction / Faraday's law
- Lane: MANIM (directed animation)
- Hook: A stationary magnet near a loop does nothing. A moving magnet induces a current — but only while it moves. The rate of flux change is the only thing that matters. This single fact is the engine of every power plant on Earth.
- The rule: ε = −dΦ_B/dt, Φ_B = ∫ B · dA. For a uniform field through area A: Φ_B = BA cosθ. Lenz's law: induced current opposes the change.
- Concrete numbers: Circular loop r = 5 cm, area A = 7.85×10⁻³ m². Magnet moving through at v = 0.5 m/s; ΔB/Δt ≈ 0.2 T/s → ε ≈ 1.57×10⁻³ V = 1.57 mV. N = 100 turns: ε = 0.157 V, detectable on a galvanometer.
- The artifact / what moves: A bar magnet slides toward and through a wire loop. A flux gauge Φ_B(t) draws in real time — rising as magnet approaches, peaking at center, falling as it exits. Below, the EMF = −dΦ/dt curve draws in real time, showing the positive and negative peaks flanking the zero crossing. A current direction arrow in the loop flips (Lenz's law) at the zero crossing. Static magnet → flat lines; moving magnet → live curves.
- Output medium: Manim (mp4)
- Two testable predictions: P1: EMF = 0 when magnet is centered in the loop (maximum Φ_B, zero dΦ/dt) — visible as the zero crossing in the EMF trace at the flux peak. P2: Reversing magnet direction flips the sign of ε — the curve inverts, confirmed by Lenz's law.
- The change: Replace the single loop with a solenoid of N turns: ε_total = −N·dΦ/dt. Show that 100 turns multiplies the EMF by 100 — motivating why transformer cores have thousands of windings.
- Human supplies (Claude can't): Nothing — fully synthetic/analytic.
- Teardown angle: Faraday had no equations. He had a galvanometer and a moving magnet, and he noticed the needle only moved while the magnet moved. Every generator in every power plant, every transformer on every pole, runs on that observation. Maxwell turned it into math sixty years later.
- Exclusions: Derivation of Faraday's law from Maxwell's equations; eddy current thermal dissipation; Lenz's law in superconductors; self-inductance back-EMF (handled in Candidate 04).
- Sim slug: em-faraday-induction
- Score: 9/10

---

## Candidate 02 — Animate "AC Generator: ε(t) = NBAω sin(ωt) from Rotating Coil"
- Source: `physics-plus-one-electromagnetism/chapters/10-electromagnetic-induction.md`
- Topic: AC generator / electromagnetic induction
- Lane: MANIM (directed animation)
- Hook: Every wall socket in your home is powered by a rotating coil in a magnetic field. The sinusoidal voltage is not an engineering choice — it is the mathematical consequence of Faraday's law applied to a rotating loop.
- The rule: ε(t) = NBAω sin(ωt). Peak EMF: ε₀ = NBAω. At θ=0 (coil parallel to B): ε = 0, maximum flux. At θ=90° (coil perpendicular to B): ε = ε₀, zero flux, maximum rate of change.
- Concrete numbers: N = 200 turns, B = 0.1 T, A = 10⁻² m² (10×10 cm coil), ω = 2π×60 = 377 rad/s (60 Hz US grid). ε₀ = 200 × 0.1 × 10⁻² × 377 = 75.4 V peak. RMS: 75.4/√2 = 53.3 V. (For household 120 V RMS: ε₀ ≈ 170 V.)
- The artifact / what moves: Left panel: coil rotating in magnetic field, current real-time angle θ(t) labeled. Right panel: ε(t) = ε₀ sin(ωt) sinusoid drawing in real time, synchronized to the coil rotation — coil hits parallel at t where ε = 0; coil hits perpendicular at t where ε = ε₀. ω slider changes period; N slider scales amplitude. The phase relationship between coil angle and EMF is the pedagogical payload.
- Output medium: Manim (mp4)
- Two testable predictions: P1: ε = 0 when coil is parallel to B (flux is maximum, rate of change is zero) — visible as simultaneous zero crossing on the sinusoid when the coil hits the parallel orientation. P2: ε = ε₀ when coil is perpendicular to B (flux is zero, rate of change is maximum) — peak of sinusoid at the perpendicular orientation.
- The change: Show RMS voltage = ε₀/√2: shade the area under ε²(t) and demonstrate that it equals (ε₀)²/2, making RMS the "DC-equivalent" power delivery — the reason your voltmeter reads 120 V, not 170 V.
- Human supplies (Claude can't): Nothing — fully synthetic/analytic.
- Teardown angle: 60 Hz is not arbitrary — it is a frequency where transformer iron doesn't overheat and AC motors run at convenient speeds. The sinusoidal shape is free; Faraday's law produces it automatically. You would have to work hard to get anything else from a rotating coil.
- Exclusions: Three-phase power; rectification to DC; motor vs generator distinction (same machine, reversed); slip rings vs commutator.
- Sim slug: em-ac-generator
- Score: 9/10

---

## Candidate 03 — Animate "Electric Dipole Field: 1/r³ vs Single Charge 1/r²"
- Source: `physics-plus-one-electromagnetism/chapters/02-electric-field.md`
- Topic: Electric field / dipole
- Lane: MANIM (directed animation)
- Hook: A single charge's electric field falls as 1/r². Put two equal and opposite charges close together and their fields partially cancel — the combined field falls as 1/r³. Double the distance: the dipole field is 8× weaker, the monopole only 4× weaker. Distance punishes the dipole harder.
- The rule: Single charge: E = kq/r². Dipole on axis: E_axis ≈ 2kqd/r³ (r ≫ d). Field line pattern: cardioid-like loops from +q to −q, compressed on axis, spread on the equatorial plane.
- Concrete numbers: q = 1 nC, d = 1 cm (dipole separation). At r = 0.1 m: E_single = 9×10⁹×10⁻⁹/(0.1)² = 900 V/m. E_dipole_axis ≈ 2×9×10⁹×10⁻⁹×0.01/(0.1)³ = 180 V/m. At r = 0.2 m: E_single = 225 V/m (÷4); E_dipole = 22.5 V/m (÷8).
- The artifact / what moves: Two panels: left shows field lines from a single positive charge (radial, uniform), right shows field lines from a +q/−q dipole (cardioid loops). Then a single panel with r-axis: two curves draw — E_single(r) ∝ 1/r² and E_dipole(r) ∝ 1/r³ on the same log-log plot. The slope difference (−2 vs −3) is labeled. A "double the distance" marker shows ÷4 vs ÷8 fall-off explicitly.
- Output medium: Manim (mp4)
- Two testable predictions: P1: At r = 0.1 m with the given parameters, E_dipole_axis = 180 V/m vs E_single = 900 V/m — ratio 1:5, checkable from the formulas. P2: On the dipole equatorial plane, E_equatorial ≈ kqd/r³ (half the axial value) — the ratio E_axis/E_equatorial = 2 is a clean, exact geometric prediction.
- The change: Generalize to higher multipoles: show the quadrupole (∝ 1/r⁴) — each added order of cancellation costs one more power of r.
- Human supplies (Claude can't): Nothing — fully synthetic/analytic.
- Teardown angle: Chemistry is dominated by dipoles. Water molecules are dipoles; that is why water dissolves salt. Every polar bond in biology is a dipole interaction. The 1/r³ fall-off means dipole forces are short-range enough to be selective — proteins fold because only the nearest dipoles matter.
- Exclusions: Torque on dipole in external field; dipole energy U = −p·E; quadrupole moment tensor formalism; multipole expansion derivation.
- Sim slug: em-dipole-field
- Score: 9/10

---

## Candidate 04 — Animate "RL Circuit: Current Grows on a τ = L/R Timescale"
- Source: `physics-plus-one-electromagnetism/chapters/10-electromagnetic-induction.md`
- Topic: RL circuit transient
- Lane: MANIM (directed animation)
- Hook: Connect an inductor to a battery and the current does not jump to its final value — it rises exponentially, reaching 63% in one time constant τ = L/R. The inductor opposes the change, and the time constant is the inductor "pushing back" against the resistor's pull.
- The rule: I(t) = (ε/R)(1 − e^{−t/τ}), τ = L/R. At t = τ: I = 0.632 × I_final. At t = 5τ: I ≈ 0.993 × I_final (effectively steady state). Stored energy when steady: U_L = ½LI².
- Concrete numbers: ε = 12 V, R = 6 Ω, L = 30 mH. I_final = ε/R = 2 A. τ = 30×10⁻³/6 = 5 ms. At t = 5 ms: I = 2(1−e⁻¹) = 1.264 A. At t = 25 ms (5τ): I ≈ 1.986 A. U_L = ½ × 0.030 × (2)² = 60 mJ at steady state.
- The artifact / what moves: Circuit schematic animates with current arrow growing. Graph I(t) draws in real time — exponential rise with 63% annotation at τ and horizontal asymptote at I_final = ε/R. τ marker drops vertically from the curve. An L slider and an R slider both update τ = L/R in real time; the curve steepens or flattens accordingly. A stored energy U_L(t) = ½LI(t)² panel draws simultaneously.
- Output medium: Manim (mp4)
- Two testable predictions: P1: At t = τ = 5 ms, I = (12/6)(1−e⁻¹) = 1.264 A — 63.2% of final, arithmetic check verifiable from the formula. P2: At t = 2τ: I = 2(1−e⁻²) = 2×0.865 = 1.729 A — 86.5% of final; two-time-constant rule confirmed.
- The change: Compare RL rise-time to RC rise-time on the same axes — same exponential form I = I_final(1−e^{−t/τ}) but τ_RC = RC vs τ_RL = L/R. The duality between C and L becomes visible in the identical mathematical form.
- Human supplies (Claude can't): Nothing — fully synthetic/analytic.
- Teardown angle: Inductors "remember" current the way capacitors "remember" voltage. The time constant τ = L/R is the timescale of that memory. Power supply designers hate it — it is why you cannot instantly switch off a high-current electromagnet without a spike that destroys the circuit.
- Exclusions: RLC oscillator (requires adding C); resonance frequency derivation; Q factor; LC circuit energy shuttling.
- Sim slug: em-rl-circuit
- Score: 8/10

---

## Candidate 05 — Animate "Ring of Charge: Axial Field Peaks at z = R/√2"
- Source: `physics-plus-one-electromagnetism/chapters/02-electric-field.md`
- Topic: Electric field of a ring of charge
- Lane: MANIM (directed animation)
- Hook: The electric field on the axis of a ring of charge is zero at the center (by symmetry) and zero at infinity — so it must peak somewhere in between. The peak is at z = R/√2, a result that requires calculus to find but is visible on a single curve.
- The rule: E_z(z) = kQz / (R² + z²)^{3/2}. Maximum at dE_z/dz = 0 → z_max = R/√2. At z_max: E_max = kQ / (R²·(3/2)^{3/2}/1) … simplified: E_max = kQ·(R/√2) / (R² + R²/2)^{3/2} = kQ / (3^{3/2}/2 · R²).
- Concrete numbers: R = 5 cm = 0.05 m, Q = 10 nC = 10⁻⁸ C. E_z at z = 0: 0. z_max = R/√2 = 3.54 cm. E_max at z = 3.54 cm: evaluate numerically ≈ 3.18×10⁴ V/m. At z = R: E_z = kQ·R/(2R²)^{3/2} = kQ/(2√2 R²) ≈ 2.55×10⁴ V/m (80% of max).
- The artifact / what moves: A ring of charge (top panel) with a point on the z-axis moving. E_z(z) curve draws as the axial position sweeps from z = −3R to +3R. The peak at z = R/√2 is marked with a dashed line. Simultaneously, the axial field vector at the moving point updates direction and magnitude. The curve is symmetric: E_z(−z) = −E_z(z), so the vector flips at z = 0.
- Output medium: Manim (mp4)
- Two testable predictions: P1: E_z = 0 at z = 0 (center of ring) — radial components cancel by symmetry, exact zero. P2: The peak E_z occurs at z = R/√2 = 0.707R — confirmed by setting dE_z/dz = 0 analytically.
- The change: Generalize to a disk of charge (integrate rings from 0 to R): show that E_z(disk) → σ/2ε₀ for an infinite plane — the field becomes uniform, independent of z. The limiting behavior is a separate classic result.
- Human supplies (Claude can't): Nothing — fully synthetic/analytic.
- Teardown angle: The peak-at-R/√2 result is not a coincidence — it is what happens when two competing effects balance: moving the test point farther from the ring weakens 1/r² but moves it into better alignment with the ring's charge. The optimal distance is geometrically fixed.
- Exclusions: Off-axis field (requires elliptic integrals); disk/infinite plane derivation; Gauss's law application to uniform field; charge distribution in a conductor.
- Sim slug: em-ring-axial-field
- Score: 8/10

---

## Candidate 06 — Animate "Equipotentials: Field Lines Always Perpendicular, Potential is a Landscape"
- Source: `physics-plus-one-electromagnetism/chapters/04-electric-potential.md`
- Topic: Electric potential / equipotential surfaces
- Lane: MANIM (directed animation)
- Hook: You can read the electric field directly from the potential landscape: the field is steepest where equipotentials are closest, and the field direction is always exactly perpendicular to them. A single scalar V encodes a vector field E.
- The rule: E = −∇V. Equipotential surfaces: V = const. On any equipotential, W = qΔV = 0 (no work done moving a charge along an equipotential). Field lines are orthogonal trajectories of equipotential curves.
- Concrete numbers: Single charge q = +1 nC: V(r) = kq/r. At r = 0.1 m: V = 9×10⁹×10⁻⁹/0.1 = 90 V. At r = 0.2 m: V = 45 V. Equipotentials are concentric spheres. For a dipole (+1 nC, −1 nC, 2 cm apart): equipotentials are distorted ovals, perpendicular to dipole field lines everywhere.
- The artifact / what moves: Two configurations animate side by side. Left: single charge — concentric circular equipotentials appear labeled with V values (90, 45, 30, 22.5 V), field lines radiate outward perpendicular to each equipotential. Right: dipole — distorted equipotentials draw, field lines draw, right-angle tick marks shown at each crossing. A test charge slides along an equipotential — its potential energy gauge stays flat (no work done). Then the test charge slides along a field line — potential energy changes monotonically.
- Output medium: Manim (mp4)
- Two testable predictions: P1: For the single charge, equipotential spacing ∝ 1/r — the shells are denser near the charge, matching V = kq/r spacing explicitly. At r = 0.05 m, V = 180 V (double the r = 0.1 m value), but the 180-V shell is at half the radius, not double. P2: The work done moving a +1 nC charge from the 90-V to 45-V equipotential = qΔV = 10⁻⁹ × 45 = 45 nJ — independent of path taken (path independence of conservative field, confirming zero circulation).
- The change: Show a conductor placed in a uniform external field: surface becomes an equipotential; internal field lines vanish; external field lines re-route perpendicular to the surface. Faraday cage appears as a natural consequence.
- Human supplies (Claude can't): Nothing — fully synthetic/analytic.
- Teardown angle: Voltage is a map. The electric field is the gradient of that map — always pointing downhill, always perpendicular to the contour lines. Every topographic map you have ever read is the same mathematical structure as an equipotential diagram.
- Exclusions: Laplace/Poisson equation derivation; image charge method; boundary-value problems; dielectric polarization.
- Sim slug: em-equipotentials
- Score: 8/10

---

## Candidate 07 — Animate "Transformer: V₂/V₁ = N₂/N₁, Power Must Be Conserved"
- Source: `physics-plus-one-electromagnetism/chapters/10-electromagnetic-induction.md`
- Topic: Transformer / mutual induction
- Lane: MANIM (directed animation)
- Hook: A transformer steps 120 V up to 12 000 V by wrapping more turns on the secondary coil — but power is conserved, so the high-voltage side carries proportionally less current. This tradeoff is what makes transcontinental power transmission possible.
- The rule: V₂/V₁ = N₂/N₁ (ideal transformer). Power conservation: P = V₁I₁ = V₂I₂ (ideal). Therefore I₂/I₁ = N₁/N₂.
- Concrete numbers: Step-up: V₁ = 120 V, N₁ = 100 turns, N₂ = 10 000 turns → V₂ = 12 000 V. If P = 1 200 W: I₁ = 10 A, I₂ = 0.1 A. Step-down: N₁ = 10 000, N₂ = 100 → V₂ = 1.2 V (e.g., USB charger). Power grid: 120 V → 500 000 V transmission → 120 V home.
- The artifact / what moves: A transformer schematic with two coils on a core. V₁ and I₁ sinusoids animate on the primary; V₂ and I₂ sinusoids animate on the secondary. An N₂/N₁ slider morphs V₂ (up for N₂ > N₁) while I₂ simultaneously falls by the same factor. Power gauges P₁ and P₂ both read the same value throughout the slider sweep (ideal transformer: P₁ = P₂). The "× turns ratio" label updates.
- Output medium: Manim (mp4)
- Two testable predictions: P1: At N₂/N₁ = 100, V₂ = 100 × V₁ = 12 000 V for V₁ = 120 V — direct from the turns ratio formula. P2: Current drops inversely: I₂ = I₁/(N₂/N₁) = I₁/100 — power P = V₂I₂ = (100V₁)(I₁/100) = V₁I₁ = unchanged.
- The change: Add a resistance loss model: I²R losses in transmission line at 120 V vs 12 000 V — show that stepping up voltage by 100× reduces resistive losses by 100² = 10 000× at the same transmitted power.
- Human supplies (Claude can't): Nothing — fully synthetic/analytic.
- Teardown angle: The entire electrical grid is a transformer chain. Power leaves the generator at ~20 kV, gets stepped up to ~500 kV for transmission, then stepped down in stages to the 120 V at your outlet. Without the transformer, long-distance transmission is thermodynamically impossible — you would lose it all to I²R heating.
- Exclusions: Hysteresis losses; leakage flux; load regulation; three-phase transformer banks; real efficiency curves.
- Sim slug: em-transformer
- Score: 7/10

---

| # | Title | Lane | Score | Slug |
|---|---|---|---|---|
| 01 | Faraday Induction: Flux → EMF | MANIM | 9 | em-faraday-induction |
| 02 | AC Generator: ε = NBAω sin(ωt) | MANIM | 9 | em-ac-generator |
| 03 | Electric Dipole: 1/r³ vs 1/r² | MANIM | 9 | em-dipole-field |
| 04 | RL Circuit: I(t) = (ε/R)(1−e^{−t/τ}) | MANIM | 8 | em-rl-circuit |
| 05 | Ring of Charge: Peak at z = R/√2 | MANIM | 8 | em-ring-axial-field |
| 06 | Equipotentials: E ⊥ V contours | MANIM | 8 | em-equipotentials |
| 07 | Transformer: Turns Ratio and Power | MANIM | 7 | em-transformer |

*7 candidates. MANIM: 7. D3/DATAVIZ: 0 (deferred). Score ≥8: 6.*
