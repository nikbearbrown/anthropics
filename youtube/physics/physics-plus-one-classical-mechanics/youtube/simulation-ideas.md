# Physics: Classical Mechanics (Plus One) — Simulation Ideas

**Pilot run: MANIM lane only — D3/DATAVIZ candidates deferred to a second pass.**

*sim-scout run 2026-07-26 — chapters read: 03, 05, 08, 16 and supporting chapters.*

---

## Candidate 01 — Animate "Kepler's Third Law: T² ∝ r³ on a Log-Log Plot"
- Source: `physics-plus-one-classical-mechanics/chapters/08-uniform-circular-motion-and-gravitation.md`
- Topic: Kepler's third law / orbital mechanics
- Lane: MANIM (directed animation)
- Hook: Every planet in the solar system, from Mercury to Neptune, falls on a single straight line on a log-log plot — and that line has slope exactly 3/2. This is Kepler's third law made visible, and Newton derived it from F = Gm₁m₂/r².
- The rule: T² = (4π²/GM_☉) r³, so log T = (3/2) log r + const. Rearranged: T = 2πr/v_orb, v_orb = √(GM_☉/r).
- Concrete numbers: Mercury: r = 0.387 AU, T = 0.241 yr. Earth: r = 1 AU, T = 1 yr. Mars: r = 1.524 AU, T = 1.881 yr. Jupiter: r = 5.203 AU, T = 11.86 yr. Sputnik: r = 6 571 km = 1.031 R_Earth above surface, T = 96.2 min.
- The artifact / what moves: A log-log plot draws with axes T² (yr²) vs r³ (AU³). Planet data points (Mercury through Neptune) appear one by one, each landing precisely on a slope-1 line. The line T² = r³ draws through them. A residual panel shows how close each point is to the theoretical line (all <0.1%). A zoom shows Sputnik added to the same line at low r — the law holds from satellites to gas giants.
- Output medium: Manim (mp4)
- Two testable predictions: P1: Earth at r = 1 AU gives T = 1 yr exactly — the law is calibrated to this point. P2: Jupiter at r = 5.203 AU gives T = √(5.203³) = √140.9 = 11.87 yr — matches NASA ephemeris to 0.1%.
- The change: Add moons of Jupiter (Io, Europa, Ganymede, Callisto) as a second line on the same log-log plot — different intercept (GM_Jup vs GM_☉) but identical slope 3/2, confirming the law is universal, not solar-system-specific.
- Human supplies (Claude can't): Nothing — fully synthetic/analytic.
- Teardown angle: Kepler found T² ∝ r³ empirically from Brahe's naked-eye data before calculus existed. Newton later showed it follows from a single equation. The log-log plot collapses an entire solar system into a straight line.
- Exclusions: Elliptical orbit derivation (full two-body problem); perturbation theory; tidal locking; general relativistic corrections to Mercury's perihelion.
- Sim slug: cm-kepler-t2-r3
- Score: 9/10

---

## Candidate 02 — Animate "Projectile Range: The 45° Maximum is Not the Whole Story"
- Source: `physics-plus-one-classical-mechanics/chapters/05-projectile-motion.md` (kinematics chapters)
- Topic: Projectile motion
- Lane: MANIM (directed animation)
- Hook: Everyone knows 45° maximizes range — but that is only true on flat ground with no air resistance. On a slope, the optimal angle shifts; with drag, it drops below 45°. The vacuum case is where the surprise lives.
- The rule: R = v₀² sin(2θ)/g (flat ground, vacuum). Maximum at θ = 45°: R_max = v₀²/g. Complementary angles give same range: θ and (90°−θ).
- Concrete numbers: v₀ = 20 m/s, g = 9.80 m/s². R_max at 45°: (20)²/9.80 = 40.8 m. At θ = 30°: R = 400 × sin(60°)/9.80 = 35.4 m. At θ = 60°: R = 35.4 m (same). At θ = 10°: R = 400 × sin(20°)/9.80 = 14.0 m.
- The artifact / what moves: A θ slider sweeps from 0° to 90°. The trajectory arc draws in real time; the landing point traces a curve on the ground. Simultaneously, a polar plot R(θ) builds up, showing the symmetric rise and fall peaking at 45°. Complementary pairs (30° and 60°, 20° and 70°) are highlighted with matching colors — same landing spot, different paths.
- Output medium: Manim (mp4)
- Two testable predictions: P1: R(30°) = R(60°) = 35.4 m for v₀ = 20 m/s — complementary angle symmetry, checkable analytically. P2: R_max(45°) = 40.8 m — exceeds R(30°) by factor sin(90°)/sin(60°) = 1/0.866 ≈ 1.155.
- The change: Overlay a drag-force trajectory (proportional to v²) — the optimal angle drops to ~38° for typical ball in air, and the symmetric complementary property breaks. The contrast makes the vacuum case retroactively surprising.
- Human supplies (Claude can't): Nothing — fully synthetic/analytic.
- Teardown angle: The 45° rule is the wrong thing to remember. The right thing is the complementary symmetry: two paths, same destination. Air resistance breaks that symmetry and shifts the optimum — which is why artillery tables exist.
- Exclusions: Coriolis force; spin effects (Magnus lift); drag coefficient derivation; 3D trajectories.
- Sim slug: cm-projectile-range
- Score: 9/10

---

## Candidate 03 — Animate "Orbital Speed: Why Sputnik Didn't Fall"
- Source: `physics-plus-one-classical-mechanics/chapters/08-uniform-circular-motion-and-gravitation.md`
- Topic: Circular orbital mechanics
- Lane: MANIM (directed animation)
- Hook: Sputnik was not blasted into space and left to float. It was thrown sideways so fast that the ground curved away as fast as it fell. Orbit is not escaping gravity — it is falling perfectly around a sphere.
- The rule: Centripetal condition: v_orb²/r = GM/r². Solving: v_orb = √(GM/r). At Earth's surface: v_orb = √(GM_E/R_E) ≈ 7.9 km/s. Period T = 2πr/v_orb.
- Concrete numbers: Sputnik: altitude 577 km, r = 6 578 km = 6.578×10⁶ m. v_orb = √(3.986×10¹⁴ / 6.578×10⁶) = 7.78 km/s. T = 2π(6.578×10⁶)/7780 = 5 310 s = 88.5 min (historical: 96.2 min — difference due to actual elliptical orbit).
- The artifact / what moves: Earth shown as a sphere. A projectile is launched horizontally at increasing speeds: at 1 km/s it falls short, at 4 km/s it goes further, at 7.9 km/s the ground curves away exactly as fast as the object falls — circular orbit traces. A free-fall vector (gravity) and the curved-away ground are shown simultaneously with a tangent construction. v slider from 1 to 11.2 km/s sweeps through suborbital → orbital → escape.
- Output medium: Manim (mp4)
- Two testable predictions: P1: v_orb at r = R_E = 6.371×10⁶ m: √(3.986×10¹⁴/6.371×10⁶) = 7.91 km/s — matches Newton's cannon calculation to 0.1%. P2: ISS at r ≈ 6 771 km gives v_orb ≈ 7.67 km/s, T ≈ 92.7 min — matches observed 92.9 min period.
- The change: Add escape velocity v_esc = √(2GM/r) = √2 × v_orb — show that escape velocity is always exactly √2 times orbital speed at the same radius, and animate a trajectory that just barely escapes vs. one that doesn't.
- Human supplies (Claude can't): Nothing — fully synthetic/analytic.
- Teardown angle: Sputnik computed its own orbit by obeying one equation. Every satellite, every moon, every planet is doing the same calculation at every instant. The "miracle" of orbit is that there is no miracle — just the balance between one force and one geometric fact.
- Exclusions: Elliptical orbit (Kepler's first law); orbital decay from drag; multi-body perturbations; spacecraft delta-v maneuvers.
- Sim slug: cm-orbital-speed
- Score: 9/10

---

## Candidate 04 — Animate "Free Fall: Position Parabola and Velocity Line, Simultaneously"
- Source: `physics-plus-one-classical-mechanics/chapters/03-kinematics.md`
- Topic: Kinematics / free fall
- Lane: MANIM (directed animation)
- Hook: Drop a hammer and a feather together in vacuum — they hit simultaneously. This surprises everyone, because intuition says heavier falls faster. The math says otherwise, and Apollo 15 proved it on the Moon.
- The rule: y(t) = y₀ + v₀t − ½g t². v(t) = v₀ − g t. a = −g = −9.80 m/s² (constant). Time to fall height h: t_fall = √(2h/g).
- Concrete numbers: Drop from h = 10 m, v₀ = 0: t_fall = √(20/9.80) = 1.43 s. v at impact = g·t_fall = 9.80×1.43 = 14.0 m/s. Apollo 15: g_Moon = 1.62 m/s², hammer + feather same t_fall from same height. Galileo: 4.5 s for Pisa drop from 55 m.
- The artifact / what moves: Split screen — left panel: object falling with y(t) parabola drawing in real time. Right panel: v(t) linear plot drawing simultaneously, slope = −g labeled. When the object hits, both plots freeze and the impact point is marked. A second run drops a "heavier" object in the same vacuum: both hit at identical t_fall (mass cancels). Optional g slider (Moon 1.62, Earth 9.80, Mars 3.72) morphs both curves together.
- Output medium: Manim (mp4)
- Two testable predictions: P1: t_fall from 10 m = √(2×10/9.80) = 1.43 s — arithmetic check verifiable on any stopwatch. P2: Impact velocity = √(2gh) = √(2×9.80×10) = 14.0 m/s — confirms energy conservation (v² = 2gh at bottom).
- The change: Add Galileo's inclined plane experiment: object rolling down ramp at angle θ has effective g_eff = g sinθ — show that the parabola stretches in time but the quadratic form holds, letting Galileo measure g by slowing the fall.
- Human supplies (Claude can't): Nothing — fully synthetic/analytic.
- Teardown angle: The Leaning Tower story may be apocryphal, but the physics is not. The mass cancels out of every free-fall equation. It took until the Moon landing to show it in a perfect vacuum without a crowd arguing the feather was "held up by air."
- Exclusions: Drag force derivation; terminal velocity; non-constant acceleration; multi-dimensional projectile (handled in Candidate 02).
- Sim slug: cm-free-fall
- Score: 8/10

---

## Candidate 05 — Animate "Standing Waves: Harmonics and the n=1..4 Node Structure"
- Source: `physics-plus-one-classical-mechanics/chapters/16-waves-and-their-properties.md`
- Topic: Standing waves / harmonics
- Lane: MANIM (directed animation)
- Hook: A string vibrating at its fundamental frequency has one loop — but at double the frequency it develops two loops, three gives three. Each harmonic is a distinct stable pattern, and the frequencies form an exact integer series: f_n = nf₁.
- The rule: Standing waves on a string: f_n = n·v/(2L), where v = √(F_T/μ), n = 1, 2, 3, … Nodes at x = k·L/n; antinodes at x = (2k+1)·L/(2n), k = 0,1,…
- Concrete numbers: L = 1 m string, v_wave = 200 m/s (typical guitar string). f₁ = 100 Hz, f₂ = 200 Hz, f₃ = 300 Hz, f₄ = 400 Hz. Node positions for n = 3: x = 0, 0.333, 0.667, 1.0 m.
- The artifact / what moves: A string of length L draws. An n-slider cycles n = 1 → 4. At each n, the standing wave pattern appears: nodes (zero displacement) are marked as fixed dots; antinodes (max displacement) pulse in opposite phase. The wave oscillates at frequency f_n (visual tempo proportional, not literal 100 Hz). Node count = n−1; antinode count = n. f_n label updates. A frequency spectrum panel shows a bar chart with harmonics 1 through 4, heights equal.
- Output medium: Manim (mp4)
- Two testable predictions: P1: For n = 3, there are exactly 2 interior nodes at L/3 and 2L/3 — geometric prediction, visually checkable. P2: f₄/f₁ = 4 exactly — integer harmonic ratio, confirmed from f_n = nv/2L.
- The change: Apply to closed-pipe (one node, one antinode at ends): only odd harmonics survive (f₁, f₃, f₅…). The pattern jump from string to pipe reuses the same standing-wave logic.
- Human supplies (Claude can't): Nothing — fully synthetic/analytic.
- Teardown angle: Every musical instrument is a standing-wave machine. The fret positions on a guitar are node locations — placing a finger there kills that harmonic. The "sweet spots" are antinodes, which is where you pluck.
- Exclusions: Dispersion relation derivation; damped oscillations; coupled-oscillator normal modes; wave on a 2D membrane.
- Sim slug: cm-standing-waves
- Score: 8/10

---

## Candidate 06 — Animate "Superposition: Constructive and Destructive Interference"
- Source: `physics-plus-one-classical-mechanics/chapters/16-waves-and-their-properties.md`
- Topic: Wave superposition / interference
- Lane: MANIM (directed animation)
- Hook: Two waves passing through the same point add — sometimes doubling in amplitude, sometimes canceling completely. The switch from constructive to destructive interference is a single half-wavelength shift. That half-wavelength is why noise-canceling headphones work.
- The rule: y_total(x,t) = y₁ + y₂ = A sin(kx − ωt) + A sin(kx − ωt + φ). At φ = 0: y = 2A sin(kx−ωt) (constructive, amplitude doubles). At φ = π: y = 0 everywhere (destructive, complete cancellation).
- Concrete numbers: A = 1 m, λ = 2 m, f = 1 Hz. φ slider: 0 → 2π. At φ = 0: max amplitude 2 m. At φ = π/2: max amplitude √2 m. At φ = π: amplitude 0. At φ = 3π/2: max amplitude √2 m.
- The artifact / what moves: Three panel display: top row shows wave 1 (blue) and wave 2 (orange, with phase offset φ). Bottom panel shows sum y_total (green). A φ slider sweeps 0 → 2π; all three panels update in real time. Amplitude of the sum is labeled and plotted as a function of φ in a side panel: 2A·|cos(φ/2)|. Constructive (φ=0, 2π) and destructive (φ=π) are labeled.
- Output medium: Manim (mp4)
- Two testable predictions: P1: At φ = π, y_total = 0 for all x and t — complete destructive interference, amplitude display reads 0.00 m. P2: At φ = π/3, resultant amplitude = 2A·cos(π/6) = 2×0.866 = 1.732 m — verifiable from the sum formula.
- The change: Show two-source interference pattern in 2D: place two point sources λ apart and animate the constructive/destructive fringe pattern spreading outward — the transition from 1D superposition to 2D diffraction pattern.
- Human supplies (Claude can't): Nothing — fully synthetic/analytic.
- Teardown angle: Noise-canceling headphones are not a filter. They are a second wave, engineered to be φ = π offset from the noise. When the phase is right, physics does the rest — the amplitude of the sum collapses to zero. The math was known in the 1800s; the hardware took another 150 years.
- Exclusions: Diffraction through a single slit; multi-slit interference; wave packets; quantum superposition.
- Sim slug: cm-wave-superposition
- Score: 8/10

---

| # | Title | Lane | Score | Slug |
|---|---|---|---|---|
| 01 | Kepler's Third Law: T² ∝ r³ | MANIM | 9 | cm-kepler-t2-r3 |
| 02 | Projectile Range: 45° Maximum | MANIM | 9 | cm-projectile-range |
| 03 | Orbital Speed: Why Sputnik Didn't Fall | MANIM | 9 | cm-orbital-speed |
| 04 | Free Fall: Parabola + Velocity Line | MANIM | 8 | cm-free-fall |
| 05 | Standing Waves: n=1..4 Harmonics | MANIM | 8 | cm-standing-waves |
| 06 | Superposition: Constructive/Destructive | MANIM | 8 | cm-wave-superposition |

*6 candidates. MANIM: 6. D3/DATAVIZ: 0 (deferred). Score ≥8: 6.*
