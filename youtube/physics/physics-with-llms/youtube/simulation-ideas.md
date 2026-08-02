# Physics With LLMs — Simulation Ideas

> MANIM lane only. Score ≥ 6. Cards produced by sim-scout 2026-07-26.

---

## Candidate 01 — Projectile Parabola Traces as Launch Angle Sweeps from 0° to 90°

- Source: `physics-with-llms/chapters/05-motion-in-two-dimensions.md`
- Topic: Projectile Motion
- Lane: MANIM (directed animation)
- Hook: The 45° sweet spot for maximum range looks arbitrary — until you watch every angle trace its parabola simultaneously and only one reaches farthest.
- The rule: Range R = v₀² sin(2θ) / g; vertical y = v₀ sinθ · t − ½gt²; horizontal x = v₀ cosθ · t
- Concrete numbers: v₀ = 100 m/s, g = 9.80 m/s²; at θ = 45° R = 1020 m; at θ = 30° R = 883 m; at θ = 60° R = 883 m (complementary angles match)
- The artifact / what moves: Seventeen parabolic arcs draw simultaneously frame-by-frame — short arcs for 0° and 90°, the broadest arch peaking at θ = 45°; a moving dot marks the landing point on a ground-line, sweeping out to 1020 m and back as θ climbs; at 45° the landing dot stops farthest out and a flash highlights it
- Output medium: Manim (mp4)
- Two testable predictions: P1: Range at θ = 30° equals range at θ = 60° exactly (both = v₀² sin 60° / g = 883 m for v₀ = 100 m/s); P2: At θ = 45°, range = v₀²/g = 1020 m, which is 15.4% greater than at 30° or 60°
- The change: Replace level ground with a cliff — the range-maximizing angle shifts below 45° and the animation shows it
- Human supplies (Claude can't): Nothing — fully synthetic/analytic
- Teardown angle: Complementary angles tie: the animation exposes the sin(2θ) = sin(180° − 2θ) symmetry that textbooks state but rarely make visible
- Exclusions: Air resistance, spin, wind — keep vacuum parabola clean
- Sim slug: `physics-projectile-angle-sweep`
- Score: 8/10

---

## Candidate 02 — Centripetal Acceleration v² Scaling: Speed Doubles, Force Quadruples

- Source: `physics-with-llms/chapters/06-circular-and-rotational-motion.md`
- Topic: Circular Motion / Centripetal Force
- Lane: MANIM (directed animation)
- Hook: Every driver "knows" a sharp curve is dangerous at high speed — but most don't know the danger scales with v², not v. Double the speed and you need four times the grip.
- The rule: a_c = v²/r; F_c = mv²/r
- Concrete numbers: r = 500 m; v = 25 m/s → a_c = 1.25 m/s² (≈ 0.13 g); v = 50 m/s → a_c = 5.0 m/s² (≈ 0.51 g); 1200 kg car: F_c goes from 1500 N to 6000 N
- The artifact / what moves: A car icon traces a fixed circular arc; a vector arrow rooted at the car's position grows and shrinks as the car's speed (shown on a speedometer readout) increases from 20 m/s to 60 m/s; the vector length follows v², making the quadrupling visually jarring; a second panel shows a live bar chart: "centripetal force (N)" growing with the curve of x²
- Output medium: Manim (mp4)
- Two testable predictions: P1: At v = 50 m/s the centripetal force is exactly 4× the force at v = 25 m/s (6000 N vs 1500 N) for the same radius and mass; P2: At v = 25 m/s, r = 500 m, a_c = 1.25 m/s² — this is about 12.8% of g, matching the textbook worked example
- The change: Vary radius instead of speed — halve r and the force doubles even at constant v, revealing the 1/r dependence
- Human supplies (Claude can't): Nothing — fully synthetic/analytic
- Teardown angle: The quadratic growth makes intuitions about "twice the speed = twice the danger" dangerously wrong — the animation shows the gap between linear and quadratic in real time
- Exclusions: Banked curves, friction coefficient breakdown, non-circular paths
- Sim slug: `physics-centripetal-v-squared`
- Score: 8/10

---

## Candidate 03 — Standing Waves: n = 1, 2, 3, 4 Modes Building in Sequence on a Fixed String

- Source: `physics-with-llms/chapters/13-waves-and-their-properties.md`
- Topic: Standing Waves / Harmonics
- Lane: MANIM (directed animation)
- Hook: A guitar string can vibrate at infinitely many frequencies — but only certain ones "stand." Watch the same string transform through four distinct locked patterns, each with a new count of nodes.
- The rule: Standing wave y_total(x,t) = 2A sin(kx) cos(ωt); nodes at x = nλ/2; allowed wavelengths λ_n = 2L/n; frequencies f_n = nv/(2L)
- Concrete numbers: L = 2 m string, wave speed v = 4 m/s; f₁ = 1.0 Hz (1 antinode), f₂ = 2.0 Hz (2 antinodes), f₃ = 3.0 Hz (3 antinodes), f₄ = 4.0 Hz (4 antinodes); nodes fixed; antinodes oscillate at ±2A
- The artifact / what moves: A taut horizontal string animates, cycling through modes 1 → 4: in each mode the antinodes oscillate sinusoidally while red dots mark the stationary nodes; between modes the string relaxes and reforms at the next harmonic; a counter in the corner displays "n = 1" through "n = 4" and shows the formula f_n = nv/2L with the current value plugged in
- Output medium: Manim (mp4)
- Two testable predictions: P1: For the n = 2 mode, two antinodes oscillate in antiphase — the midpoint (a node) never moves; measurable by tracking any two symmetric antinodes and confirming they peak 180° apart; P2: Frequency ratio f₄/f₁ = 4 exactly; at v = 4 m/s, L = 2 m: f₁ = 1.0 Hz, f₄ = 4.0 Hz
- The change: Free one end — boundary condition changes so nodes/antinodes swap placement and only odd harmonics appear
- Human supplies (Claude can't): Nothing — fully synthetic/analytic
- Teardown angle: Nodes never move even though "the wave is moving" — the animation forces the viewer to reconcile superposition with apparent stillness
- Exclusions: Damping, overtone mixtures, instrument timbre — keep one clean mode at a time
- Sim slug: `physics-standing-wave-modes`
- Score: 9/10

---

## Candidate 04 — Double-Slit Interference: Bright and Dark Fringes Drawing from Path-Difference Rule

- Source: `physics-with-llms/chapters/17-diffraction-and-interference.md`
- Topic: Wave Optics / Double-Slit Interference
- Lane: MANIM (directed animation)
- Hook: Passing light through two slits should give two bright spots — instead it creates a spreading ladder of brightness and darkness. Two sources working together can produce darkness.
- The rule: Bright fringes at d sin θ = mλ (m = 0, ±1, ±2, …); dark fringes at d sin θ = (m + ½)λ; fringe spacing y_m = mλL/d on a screen at distance L
- Concrete numbers: He-Ne laser λ = 633 nm, slit separation d = 0.0100 mm, screen distance L = 1.5 m; fringe spacing = λL/d = 94.95 mm ≈ 95 mm; third-order bright band at θ = arcsin(3λ/d) = 10.95°
- The artifact / what moves: Two vertical slit lines emit semicircular wavefronts that visibly propagate toward a screen; where crests meet crests, a bright dot appears; where crest meets trough, a dark region appears; the screen builds up a full fringe pattern left-to-right as the wavefronts sweep across; a separate panel shows the intensity profile I(y) ∝ cos²(πdy/λL) tracing out its peaks in sync
- Output medium: Manim (mp4)
- Two testable predictions: P1: Fringe spacing = λL/d = (633 × 10⁻⁹ m)(1.5 m)/(0.01 × 10⁻³ m) = 94.95 mm — the animation's screen ruler must match this; P2: The third bright fringe (m = 3) appears at y = 3 × 94.95 mm = 284.85 mm from center — verifiable by measuring three fringe spacings in the rendered frame
- The change: Increase slit separation d → fringes compress; decrease d → fringes spread; the animation shows this live as a slider
- Human supplies (Claude can't): Nothing — fully synthetic/analytic
- Teardown angle: Destructive interference is not "cancellation into nothing" — energy is just redistributed; the animation makes this explicit by showing where the missing energy reappears
- Exclusions: Single-slit envelope modulation, coherence width, near-field Fresnel effects
- Sim slug: `physics-double-slit-fringe-build`
- Score: 9/10

---

## Candidate 05 — Photoelectric Threshold Line: KE_max vs Frequency Sweeping Across the Cut-off

- Source: `physics-with-llms/chapters/21-the-quantum-nature-of-light.md`
- Topic: Photoelectric Effect / Quantum Nature of Light
- Lane: MANIM (directed animation)
- Hook: Below a critical frequency no electrons emerge — not even with a floodlight. Above it, a single dim photon is enough. The wave model predicts intensity should matter; it doesn't.
- The rule: KE_max = hf − BE (binding energy); threshold frequency f₀ = BE/h; for f < f₀ no emission; KE_max vs f is a straight line with slope h
- Concrete numbers: Calcium: BE = 2.71 eV, f₀ = (2.71 eV)(1.602 × 10⁻¹⁹ J/eV)/(6.626 × 10⁻³⁴ J·s) = 6.55 × 10¹⁴ Hz (λ = 458 nm); at f = 7.14 × 10¹⁴ Hz (420 nm violet): KE_max = 2.96 − 2.71 = 0.25 eV; sodium: BE = 2.28 eV, f₀ = 5.51 × 10¹⁴ Hz (544 nm green)
- The artifact / what moves: A frequency axis sweeps from IR through visible to UV; at the left, frequency is below threshold — a cartoon photon hits the metal and bounces away, electron stays put; as the sweep crosses f₀ the first electron pops out with zero kinetic energy; above f₀ a growing diagonal line traces KE_max = hf − BE in real time; the slope of the line is h; a second metal (sodium) appears showing a different threshold at lower frequency
- Output medium: Manim (mp4)
- Two testable predictions: P1: For calcium, the threshold wavelength is λ = hc/BE = (6.626 × 10⁻³⁴)(3 × 10⁸)/(2.71 × 1.602 × 10⁻¹⁹) = 458 nm — the animation's threshold marker lands on 458 nm in the visible spectrum; P2: At 420 nm (7.14 × 10¹⁴ Hz) on calcium, KE_max = 0.25 eV = 4.01 × 10⁻²⁰ J; the animated electron escaping at this frequency has a stopping potential of exactly 0.25 V
- The change: Show two metals side-by-side (calcium and sodium) — both lines are parallel (same slope h) but shifted horizontally by their different work functions
- Human supplies (Claude can't): Nothing — fully synthetic/analytic
- Teardown angle: The slope of KE_max vs f is Planck's constant h for every metal — same slope, different intercept; the animation makes the slope measurable and universal
- Exclusions: Compton scattering, photon counting statistics, intensity effects on electron count (not on KE)
- Sim slug: `physics-photoelectric-threshold-line`
- Score: 8/10

---

## Candidate 06 — Bohr Hydrogen Spectrum: Energy Levels En = −13.6/n² and Emission Lines Appearing

- Source: `physics-with-llms/chapters/22-the-atom.md`
- Topic: Atomic Spectra / Bohr Model
- Lane: MANIM (directed animation)
- Hook: Hydrogen should emit a rainbow. Instead it emits four visible lines, always at the same wavelengths, because electrons can only exist at certain energies — and the photon captures the exact difference.
- The rule: E_n = −13.6 eV/n²; emitted photon energy ΔE = E_i − E_f = hf; Rydberg formula 1/λ = R(1/n_f² − 1/n_i²), R = 1.097 × 10⁷ m⁻¹
- Concrete numbers: Balmer series (n_f = 2): n_i = 3 → λ = 656 nm (red); n_i = 4 → λ = 486 nm (cyan-green); n_i = 5 → λ = 434 nm (violet); n_i = 6 → λ = 410 nm (far violet); ground state energy E₁ = −13.6 eV; ionization from n = 2 requires 3.4 eV
- The artifact / what moves: A vertical energy-level diagram shows E₁ through E₆ as horizontal rungs labeled with their eV values; an electron dot starts at n = 4, then drops to n = 2; a colored photon arrow shoots outward carrying the energy difference; where it hits a horizontal spectrum strip, a colored line appears at 486 nm (cyan-green); the animation repeats for three other Balmer transitions, each depositing a line at its exact wavelength; the final frame shows four vertical lines on a black spectrum strip — hydrogen's fingerprint
- Output medium: Manim (mp4)
- Two testable predictions: P1: The n = 3 → n = 2 transition emits at λ = 1/(R(1/4 − 1/9)) = 1/(R × 5/36) = 656 nm — the animation's red line lands at 656 nm, verifiable against known hydrogen spectrum; P2: The n = 4 → n = 2 energy drop is ΔE = 13.6(1/4 − 1/16) = 13.6 × 3/16 = 2.55 eV, corresponding to f = 6.17 × 10¹⁴ Hz and λ = 486 nm — a second independently checkable line
- The change: Show the Lyman series (n_f = 1) — transitions all fall in the UV, showing no visible lines, which is why hydrogen in air looks colorless without a spectrometer
- Human supplies (Claude can't): Nothing — fully synthetic/analytic
- Teardown angle: The spectral lines are not a list to memorize — they are the geometry of a ladder, and the animation makes every line a measured rung-drop
- Exclusions: Multi-electron atoms, spin, fine structure, quantum mechanical wavefunctions (Bohr model only)
- Sim slug: `physics-bohr-emission-spectrum`
- Score: 9/10
