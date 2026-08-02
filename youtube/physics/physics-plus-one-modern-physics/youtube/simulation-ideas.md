# Physics: Modern Physics (Plus One) — Simulation Ideas

**Pilot run: MANIM lane only — D3/DATAVIZ candidates deferred to a second pass.**

*sim-scout run 2026-07-26 — chapters read: 01, 04, 08 and supporting chapters.*

---

## Candidate 01 — Animate "The Ultraviolet Catastrophe: Rayleigh-Jeans Diverges, Planck Saves It"
- Source: `physics-plus-one-modern-physics/chapters/04-the-quantum-nature-of-light.md`
- Topic: Blackbody radiation / ultraviolet catastrophe
- Lane: MANIM (directed animation)
- Hook: Classical physics predicts that a hot object should radiate infinite energy at short wavelengths — a catastrophe that never happens. Planck's quantum hypothesis fixes it, but only by requiring energy to come in discrete chunks. The "fix" was the beginning of quantum mechanics.
- The rule: Rayleigh-Jeans: B_λ^{RJ} ∝ λ⁻⁴T (diverges as λ → 0). Planck: B_λ = (2hc²/λ⁵) / (e^{hc/λkT} − 1) (finite everywhere). Planck energy quanta: E = hf = hc/λ, h = 6.626×10⁻³⁴ J·s.
- Concrete numbers: T = 5 778 K (solar surface). Rayleigh-Jeans at λ = 200 nm: B_λ^{RJ} → ∞. Planck at λ = 200 nm: B_λ finite, ~10% of peak. Wien peak: λ_peak = 2.898×10⁻³/5778 = 502 nm (green). At λ = 10 μm (far IR): Planck and Rayleigh-Jeans converge (classical limit).
- The artifact / what moves: Two curves draw: Planck (solid) and Rayleigh-Jeans (dashed). As the wavelength axis sweeps from IR → visible → UV, the Rayleigh-Jeans curve climbs toward infinity while Planck peaks and falls. At λ = 502 nm, the Wien peak marker appears. A shaded "UV catastrophe" region (λ < ~300 nm) highlights where classical physics fails. A T slider morphs both curves — the divergence always appears in Rayleigh-Jeans regardless of T; Planck always stays finite.
- Output medium: Manim (mp4)
- Two testable predictions: P1: At long wavelengths (λ ≫ hc/kT), Planck and Rayleigh-Jeans agree to within 1% — the classical limit is exact, visible as curve overlap at λ > 5 μm for T = 5 778 K. P2: Wien peak at T = 5 778 K lands at λ = 502 nm, matching NIST blackbody tables to 0.2%.
- The change: Show the progressive "quantum correction" by plotting the Planck correction factor (e^{hc/λkT} − 1)^{−1} vs (hc/λkT): the 1/x classical tail diverges; the 1/(e^x − 1) quantum tail converges.
- Human supplies (Claude can't): Nothing — fully synthetic/analytic.
- Teardown angle: The ultraviolet catastrophe was not a footnote — it was a fundamental breakdown of classical statistical mechanics. Planck's "desperate" quantization was meant as a mathematical trick; he did not believe it was physical. Einstein took it seriously six years later with the photoelectric effect, and the whole program became quantum mechanics.
- Exclusions: Derivation of the Planck distribution from statistical mechanics; Bose-Einstein statistics; Stefan-Boltzmann law integration; CMB blackbody (handled elsewhere).
- Sim slug: modern-uv-catastrophe
- Score: 9/10

---

## Candidate 02 — Animate "Time Dilation: The Light Clock and the Pythagorean Derivation"
- Source: `physics-plus-one-modern-physics/chapters/01-special-relativity.md`
- Topic: Special relativity / time dilation
- Lane: MANIM (directed animation)
- Hook: A clock made of a photon bouncing between two mirrors runs slower when moving — not because of any mechanical failure, but because the photon must travel a longer diagonal path at the same speed c. This is time dilation, and it is a pure geometric consequence of one postulate: the speed of light is constant.
- The rule: Δt = Δt₀ / √(1 − v²/c²) = γΔt₀. The light clock: in the moving frame, photon travels diagonal distance d = √((v·Δt/2)² + L²). Since c = d/(Δt/2): c²Δt² = v²Δt² + 4L²; rearranging with cΔt₀ = 2L → Δt = Δt₀/√(1 − v²/c²).
- Concrete numbers: Muon: Δt₀ = 2.2 μs (rest lifetime), v = 0.9994c, γ = √(1/(1−0.9988)) = √(1/0.0012) ≈ 28.9. Observed lifetime: 63.5 μs. Distance traveled: 0.9994c × 63.5 μs ≈ 19 km (atmospheric muon reaches sea level; classical prediction: 0.66 km, doesn't make it).
- The artifact / what moves: Left panel: stationary light clock (vertical bounce). Right panel: moving light clock — photon travels diagonal path. Pythagorean triangle draws: horizontal leg vΔt/2, vertical leg L = cΔt₀/2, hypotenuse cΔt/2. The derivation animates step by step. Below: γ(v) curve draws from v = 0 to v = 0.9999c; the muon point is plotted at v = 0.9994c, γ = 28.9. A classical-prediction timeline vs relativistic timeline shows the muon surviving 19 km instead of dying at 0.66 km.
- Output medium: Manim (mp4)
- Two testable predictions: P1: At v = 0.9994c, γ = 28.9 → Δt = 63.5 μs — matches observed muon lifetime in cosmic ray experiments (Rossi and Hall, 1941). P2: At v = 0 (stationary), γ = 1, Δt = Δt₀ — time dilation vanishes, Pythagorean triangle collapses to a vertical segment (zero horizontal leg).
- The change: Add the symmetric view: in the muon's rest frame, the atmosphere is length-contracted from 15 km to 15 km/28.9 = 0.52 km. Both frames agree the muon survives — one via time dilation, one via length contraction. Show both simultaneously.
- Human supplies (Claude can't): Nothing — fully synthetic/analytic.
- Teardown angle: The light clock argument is not a metaphor. It is a derivation from one postulate. The muon is not "experiencing" anything unusual — it follows geodesics in Minkowski spacetime. The strangeness is entirely in the classical observer's expectation.
- Exclusions: Twin paradox (requires general relativity or non-inertial frames); Lorentz transformation derivation; simultaneity relativity (handled separately); four-vector formalism.
- Sim slug: modern-time-dilation
- Score: 9/10

---

## Candidate 03 — Animate "The Photoelectric Effect: KE = hf − BE, and the Threshold That Classical Physics Cannot Explain"
- Source: `physics-plus-one-modern-physics/chapters/04-the-quantum-nature-of-light.md`
- Topic: Photoelectric effect
- Lane: MANIM (directed animation)
- Hook: Shine UV light on a metal and electrons fly off — but only if the frequency exceeds a threshold. Brighter light does not help below the threshold; higher frequency does. Classical wave theory predicts no threshold. Einstein's explanation earned him the Nobel Prize.
- The rule: KE_max = hf − BE (work function). Threshold frequency: f_threshold = BE/h. h = 6.626×10⁻³⁴ J·s = 4.136×10⁻¹⁵ eV·s.
- Concrete numbers: Calcium: BE = 2.71 eV, f_threshold = 2.71 / (4.136×10⁻¹⁵) = 6.55×10¹⁴ Hz (UV, λ = 458 nm). At f = 8×10¹⁴ Hz: KE = 4.136×10⁻¹⁵ × 8×10¹⁴ − 2.71 = 3.309 − 2.71 = 0.599 eV. At f = 6×10¹⁴ Hz (below threshold): KE = negative → no emission, regardless of intensity.
- The artifact / what moves: A KE_max vs f plot draws. Below f_threshold: flat line at KE = 0 (no emission). Above threshold: KE = hf − BE line with slope h (labeled in eV·s). The x-intercept is f_threshold = BE/h. Three data points for different metals appear at their respective thresholds — each a different intercept but the same slope h. An intensity slider increases brightness below threshold: no change in KE_max or in whether emission occurs. A classical prediction overlay shows KE should increase with intensity — it doesn't.
- Output medium: Manim (mp4)
- Two testable predictions: P1: For calcium (BE = 2.71 eV), threshold at λ = 458 nm (f = 6.55×10¹⁴ Hz) — below this, zero electrons no matter how bright the light. P2: Slope of KE_max vs f line = h = 4.136×10⁻¹⁵ eV·s — confirmed across all metals; the slope is universal, the intercept shifts by metal.
- The change: Show stopping potential V_stop = KE_max/e on a separate axis — this is what Millikan measured experimentally, confirming E = hf by measuring V_stop vs f on a graph with slope h/e.
- Human supplies (Claude can't): Nothing — fully synthetic/analytic.
- Teardown angle: Einstein's 1905 Nobel Prize was not for relativity. It was for explaining this graph. The threshold frequency is the signature of quantization — a continuous wave cannot produce a discrete threshold. Every photodetector, every solar cell, every CCD camera is a photoelectric effect machine.
- Exclusions: Quantum efficiency and reflectivity; photoelectron spectroscopy; Compton scattering (separate quantum photon experiment); band structure in solids.
- Sim slug: modern-photoelectric
- Score: 9/10

---

## Candidate 04 — Animate "The Gamma Factor γ(v): The Relativistic Rise Toward c"
- Source: `physics-plus-one-modern-physics/chapters/01-special-relativity.md`
- Topic: Special relativity / gamma factor
- Lane: MANIM (directed animation)
- Hook: At everyday speeds, γ = 1 to many decimal places — Newtonian mechanics is exact. But as v → c, γ rises without bound, meaning infinite energy would be required to reach c. The speed of light is not a speed limit imposed by engineers; it is a mathematical asymptote.
- The rule: γ = 1/√(1 − v²/c²). At v = 0: γ = 1. At v = 0.5c: γ = 1.155. At v = 0.9c: γ = 2.294. At v = 0.99c: γ = 7.089. At v = 0.9994c: γ ≈ 28.9 (muon). As v → c: γ → ∞.
- Concrete numbers: Muon at v = 0.9994c: γ = 28.9, Δt = 63.5 μs (vs 2.2 μs rest). LHC protons at v ≈ 0.9999999896c: γ ≈ 7 461. Total energy E = γmc² = 7461 × 938 MeV = 7 000 GeV = 7 TeV per proton.
- The artifact / what moves: γ(v/c) curve draws from v = 0 to v = 0.9999c. The x-axis is β = v/c (0 to 1); the y-axis is γ (1 to 100+). A dashed γ = 1 horizontal line shows the Newtonian approximation. Key points are labeled: muon at β = 0.9994, LHC proton at β ≈ 1. A "Newtonian regime" shaded region (β < 0.1, γ within 0.5% of 1) is marked. The curve visibly approaches a vertical asymptote at β = 1.
- Output medium: Manim (mp4)
- Two testable predictions: P1: At β = 0.5 (v = 0.5c), γ = 1/√(1−0.25) = 1/√0.75 = 1.155 — direct arithmetic verification. P2: At β = 0.9, γ = 1/√(1−0.81) = 1/√0.19 = 2.294 — time runs 2.3× slower for the moving observer relative to the stationary one.
- The change: Add the relativistic momentum p = γmv and kinetic energy KE = (γ−1)mc² curves on the same v-axis — showing how all relativistic quantities share the same γ factor and diverge together as v → c.
- Human supplies (Claude can't): Nothing — fully synthetic/analytic.
- Teardown angle: The γ factor is not exotic. It is the geometric factor in a right triangle (Pythagorean theorem applied to the light clock). Everything relativistic — time dilation, length contraction, mass-energy equivalence — flows from one curve that approaches a vertical asymptote at β = 1.
- Exclusions: Four-velocity and four-momentum formalism; energy-momentum invariant E² = (pc)² + (mc²)²; relativistic Doppler effect; rapidity.
- Sim slug: modern-gamma-factor
- Score: 8/10

---

## Candidate 05 — Animate "Length Contraction: The Muon's Atmosphere Is Only 0.52 km Thick"
- Source: `physics-plus-one-modern-physics/chapters/01-special-relativity.md`
- Topic: Special relativity / length contraction
- Lane: MANIM (directed animation)
- Hook: In the muon's rest frame, it does not live longer — the atmosphere contracts. A 15 km atmosphere shrinks to 0.52 km at v = 0.9994c. Two observers, two explanations, one outcome: the muon reaches sea level.
- The rule: L = L₀/γ = L₀ √(1 − v²/c²). L₀ is the proper length (rest frame of the object). At v = 0.9994c, γ = 28.9: L = 15 km / 28.9 = 0.52 km.
- Concrete numbers: Atmospheric depth to muon production: L₀ = 15 km. γ = 28.9 (v = 0.9994c). L_contracted = 15 km / 28.9 = 0.52 km. Muon rest lifetime: 2.2 μs. At 0.52 km, travel time = 0.52 km / 0.9994c ≈ 1.73 μs < 2.2 μs — muon survives easily in its own frame.
- The artifact / what moves: Split screen — left: Earth frame (atmosphere 15 km, muon lifetime dilated to 63.5 μs, muon traverses in time). Right: muon frame (atmosphere length-contracted to 0.52 km, muon's own clock at 2.2 μs rest lifetime, muon traverses the 0.52 km in 1.73 μs and survives). Both frames show the muon reaching sea level simultaneously. A length bar explicitly shows L₀ vs L = L₀/γ with the γ = 28.9 divisor labeled.
- Output medium: Manim (mp4)
- Two testable predictions: P1: L = 15 km / 28.9 = 0.52 km — in the muon frame, the atmosphere is less than one-third of a kilometer. P2: Travel time in muon frame = 0.52 km / (0.9994 × 3×10⁸ m/s) = 1.73 μs < 2.2 μs rest lifetime — the muon survives with time to spare.
- The change: Show a "ruler" scenario: a 1-meter rod at rest is photographed from a frame moving at β = 0.9 — it appears 1/γ = 0.436 m long. Then swap frames: now the rod is moving and the observer is stationary — same contraction, same result. Frame symmetry demonstrated.
- Human supplies (Claude can't): Nothing — fully synthetic/analytic.
- Teardown angle: Length contraction and time dilation are the same event described from two frames. Neither frame is "really" right — both are correct simultaneously. The fact that they agree on the muon surviving is the consistency check that proves the theory hangs together.
- Exclusions: Terrell rotation (visual appearance vs measured length); ladder paradox; rigid body in relativity; derivation of Lorentz transformation from scratch.
- Sim slug: modern-length-contraction
- Score: 8/10

---

## Candidate 06 — Animate "Gravitational Redshift: λ_∞/λ_r = 1/√(1 − R_S/r)"
- Source: `physics-plus-one-modern-physics/chapters/08-black-holes-and-curved-spacetime.md`
- Topic: Gravitational redshift / general relativity
- Lane: MANIM (directed animation)
- Hook: Light climbing out of a gravitational well loses energy — its frequency drops and wavelength grows. A photon emitted at radius r from a black hole arrives at infinity redshifted by a factor that diverges as r → R_S. This is measurable on Earth with a Mossbauer experiment over a 22.5-meter height difference.
- The rule: Gravitational redshift: λ_∞/λ_r = 1/√(1 − R_S/r), equivalently f_∞/f_r = √(1 − R_S/r). For Earth (weak field): Δf/f ≈ gh/c² = 9.80 × 22.5 / (3×10⁸)² = 2.46×10⁻¹⁵ (Pound-Rebka experiment).
- Concrete numbers: R_S for 10 M_☉ black hole: R_S = 2GM/c² = 2 × 6.674×10⁻¹¹ × 10 × 1.989×10³⁰ / (3×10⁸)² ≈ 29.5 km. At r = 2R_S: λ_∞/λ_r = 1/√(0.5) = √2 = 1.414. At r = 1.1R_S: λ_∞/λ_r = 1/√(0.091) ≈ 3.32. Pound-Rebka 1959: Δf/f = 2.46×10⁻¹⁵ measured at 1% precision.
- The artifact / what moves: A radial axis from r = R_S outward. A photon "emitted" at radius r near the black hole climbs outward; its wavelength λ(r) is shown stretching as it rises (color shifts from blue to red on the spectrum bar). The ratio λ_∞/λ_r draws as a curve vs r/R_S — from 1 (at r → ∞) rising steeply toward ∞ as r → R_S. Pound-Rebka scenario inset: a 22.5-m vertical shaft, Δf/f = 2.46×10⁻¹⁵ labeled.
- Output medium: Manim (mp4)
- Two testable predictions: P1: At r = 2R_S, λ_∞/λ_r = √2 = 1.414 — photon wavelength 41.4% longer at infinity. P2: Pound-Rebka experimental result: Δf/f = gh/c² = 2.46×10⁻¹⁵ for h = 22.5 m on Earth — matches the 1959 measurement to within experimental precision (confirmed at 1%).
- The change: Show GPS gravitational correction: GPS satellites at r ≈ 26 560 km altitude must correct for both gravitational blueshift (+45.9 μs/day) and SR time dilation (−7.2 μs/day) for a net +38.4 μs/day — without it, GPS drifts ~10 km/day.
- Human supplies (Claude can't): Nothing — fully synthetic/analytic.
- Teardown angle: General relativity is not just a theory about black holes and the Big Bang. It runs your GPS. The gravitational redshift correction is a real number, applied every day, measurable in your phone. Pound and Rebka proved it with gamma-ray spectroscopy in an elevator shaft.
- Exclusions: Derivation of Schwarzschild metric from Einstein field equations; frame-dragging (Kerr metric); perihelion precession of Mercury; gravitational wave emission.
- Sim slug: modern-gravitational-redshift
- Score: 8/10

---

| # | Title | Lane | Score | Slug |
|---|---|---|---|---|
| 01 | UV Catastrophe: Rayleigh-Jeans vs Planck | MANIM | 9 | modern-uv-catastrophe |
| 02 | Time Dilation: Light Clock Derivation | MANIM | 9 | modern-time-dilation |
| 03 | Photoelectric Effect: KE = hf − BE | MANIM | 9 | modern-photoelectric |
| 04 | Gamma Factor γ(v): Rise Toward c | MANIM | 8 | modern-gamma-factor |
| 05 | Length Contraction: Muon's 0.52 km Atmosphere | MANIM | 8 | modern-length-contraction |
| 06 | Gravitational Redshift: λ_∞/λ_r Curve | MANIM | 8 | modern-gravitational-redshift |

*6 candidates. MANIM: 6. D3/DATAVIZ: 0 (deferred). Score ≥8: 6.*
