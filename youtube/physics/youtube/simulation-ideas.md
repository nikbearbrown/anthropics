# Physics (College Physics) — Simulation Ideas

**Pilot run: MANIM lane only. D3/DATAVIZ pass follows after human approval.**
*sim-scout run 2026-07-26 — chapters 02, 03, 06, 07, 08, 10, 16, 18, 27, 28, 29 read.*

---

## Candidate 01 — Animate "Projectile Range Curve: 45° Wins and Complementary Pairs Tie"
- Source: `physics/chapters/03-two-dimensional-kinematics.md`
- Topic: Projectile Motion / Range Equation
- Lane: MANIM (directed animation)
- Hook: Launch the same ball at five angles from 15° to 75°. Watch the arcs draw in sequence. Then watch the 30°/60° pair land at the same spot — and the 45° arc out-range everything. The range equation is one curve you can read off from watching trajectories.
- The rule: R = v₀²sin(2θ)/g. Horizontal: x = v₀cosθ · t. Vertical: y = v₀sinθ · t − ½gt². R is maximized when sin(2θ) = 1, i.e., θ = 45°. Complementary angles θ and 90°−θ satisfy sin(2θ) = sin(2(90°−θ)), so they share range.
- Concrete numbers: v₀ = 20 m/s, g = 9.80 m/s². θ = 15°: R = 20²×sin(30°)/9.80 = 20.4 m. θ = 30°: R = 35.3 m. θ = 45°: R = 40.8 m (max). θ = 60°: R = 35.3 m (same as 30°). θ = 75°: R = 20.4 m (same as 15°). Peak height at 45°: y_max = v₀²sin²(45°)/(2g) = 10.2 m.
- The artifact / what moves: Five arcs draw sequentially from the same launch point, each a different color (15° through 75°). Landing markers drop where each parabola hits y = 0. After all five draw, arrows bracket the 30°/60° pair showing equal range. A final sweep animates R(θ) as a single point tracing the full range curve from θ = 0° to 90°, peaking at 45°. The curve's shape emerges from the arcs already on screen.
- Output medium: Manim (mp4)
- Two testable predictions: P1: R(45°) = v₀²/g = 20²/9.80 = 40.8 m — the maximum range, verifiable from the range formula with sin(90°) = 1; P2: R(30°) = R(60°) = v₀²sin(60°)/g = 35.3 m exactly — checkable from sin(2×30°) = sin(2×60°) = sin(60°), an exact equality, not an approximation
- The change: Set v₀ = 30 m/s and repeat — the same relative angle structure holds but all ranges scale as v₀², so they grow by a factor of 2.25; shows that the angle pattern is universal while the absolute ranges depend on launch speed
- Human supplies (Claude can't): Nothing — fully synthetic/analytic; all trajectories computed from kinematics equations with no empirical inputs
- Teardown angle: Real projectiles (artillery shells, shot-put balls) optimum at angles below 45° because air drag penalizes high arcs more than low ones — the 45° maximum is vacuum physics, and knowing that tells you which way every real optimum deviates from it
- Exclusions: Derivation of the range equation (belongs in narration, not animation beats); air-resistance trajectory correction (different simulation card); relative-velocity corrections (Chapter 3 boat-in-current content)
- Sim slug: physics-projectile-range-curve
- Score: 9/10

---

## Candidate 02 — Animate "Orbital Speed and Kepler's Third Law: T² ∝ r³ Traced Live"
- Source: `physics/chapters/06-uniform-circular-motion-and-gravitation.md`
- Topic: Orbital Mechanics / Kepler's Third Law
- Lane: MANIM (directed animation)
- Hook: Put three satellites at different altitudes and watch them orbit. The outer one is visibly slower — not just going a longer way round, but moving at lower speed. After two minutes of animation, they've lapped each other at exact integer ratios. Then plot their (T², r³) data points on a log-log grid and watch them line up perfectly.
- The rule: v = √(GM/r). T = 2πr/v = 2π√(r³/GM). Therefore T² = (4π²/GM)×r³ — linear on log-log axes with slope 1. For Earth orbits, GM_⊕ = 3.986×10¹⁴ m³/s².
- Concrete numbers: LEO at r = 6.628×10⁶ m: v = 7755 m/s, T = 89.5 min. ISS at r = 6.778×10⁶ m: v = 7660 m/s, T = 92.7 min. GPS at r = 2.656×10⁷ m: v = 3874 m/s, T = 718 min. GEO at r = 4.216×10⁷ m: v = 3070 m/s, T = 1436 min (= 24 h). At T = 89.5 min, GPS has completed 89.5/718 = 0.125 orbits — the inner satellite has lapped 8 times by the time GPS completes one.
- The artifact / what moves: A scaled Earth at center. Three labeled orbital rings (LEO, GPS, GEO) appear. Satellites launch simultaneously and trace their orbits at true relative speeds — the LEO satellite visibly races, GPS crawls, GEO barely moves. A time counter runs. After enough simulated time for LEO to complete 16 orbits, pause: GPS has completed exactly 2 (confirming T ratio ≈ 8.0, since (r_GPS/r_LEO)^(3/2) ≈ 8.0). Second scene: log-log grid plots (r, T) for all three plus the Moon — four points, one line, slope = 1, labeled "Kepler's Third Law."
- Output medium: Manim (mp4)
- Two testable predictions: P1: T_GEO/T_LEO = (r_GEO/r_LEO)^(3/2) = (4.216×10⁷/6.628×10⁶)^(3/2) ≈ 16.0 — GEO takes exactly 16 times longer than LEO — checkable from the ratio (1436/89.5 ≈ 16.0); P2: GPS orbital speed = √(GM/r_GPS) = √(3.986×10¹⁴/2.656×10⁷) = 3874 m/s — checkable, and explains the +38 µs/day special-relativistic correction GPS clocks receive
- The change: Add the Moon at r = 3.84×10⁸ m — it falls on the same log-log line even though it was the data point that verified the law for Newton in 1687; shows that Kepler's Third Law holds over 4 orders of magnitude in orbital radius from LEO to the Moon
- Human supplies (Claude can't): Nothing — fully synthetic/analytic; all parameters from published GM_⊕ and orbital radii
- Teardown angle: Every GPS satellite is a proof that Newton's gravity and special relativity are simultaneously correct — the orbital period determines the orbital speed determines the relativistic time correction that must be pre-loaded into the satellite's clock before launch, or your map app drifts 11 km per day
- Exclusions: General-relativistic correction to GPS (gravitational blueshift, +45 µs/day — belongs in narration); derivation of Kepler's Third Law from centripetal force = gravity (belongs in narration); elliptical orbit corrections
- Sim slug: physics-kepler-third-law-orbits
- Score: 9/10

---

## Candidate 03 — Animate "Free Fall and the Constant-Acceleration Parabola: Three Panels in Sync"
- Source: `physics/chapters/02-kinematics.md`
- Topic: Kinematics / Free Fall
- Lane: MANIM (directed animation)
- Hook: Throw a rock upward and track position, velocity, and acceleration simultaneously on three linked graphs. The position panel draws a parabola; the velocity panel draws a straight falling line that crosses zero at the peak; the acceleration panel draws a flat horizontal line at −9.80 m/s² — unchanging even at the peak. At the peak, velocity = 0 and acceleration ≠ 0. Most students mix them up once, and never again after watching the three panels.
- The rule: y(t) = y₀ + v₀t − ½gt². v(t) = v₀ − gt. a(t) = −g = −9.80 m/s² = constant throughout. Peak time: t_peak = v₀/g. Peak height: y_max = v₀²/(2g).
- Concrete numbers: v₀ = 13.0 m/s (thrown upward from cliff edge, y₀ = 0). t_peak = 13.0/9.80 = 1.33 s. y_max = (13.0)²/(2×9.80) = 8.6 m. At t = 2.0 s: y = 6.4 m (falling back), v = −6.6 m/s. At t = 3.0 s: y = −5.1 m (below cliff), v = −16.4 m/s. a = −9.80 m/s² at all times.
- The artifact / what moves: Three panels stacked vertically on the same time axis. A dot (the rock) moves on a vertical strip on the left. At t = 0: all three graphs start drawing simultaneously. Top panel: y vs t — parabola opening downward, peaking at 1.33 s, crossing y = 0 at t ≈ 2.65 s, continuing below. Middle panel: v vs t — straight line from +13.0, crossing 0 at 1.33 s, continuing negative. Bottom panel: a vs t — flat horizontal line at −9.80 from t = 0 to t = 3.0 s, never changing. A vertical cursor sweeps rightward across all three panels simultaneously. At t = 1.33 s the cursor reaches the parabola's peak on panel 1, the zero crossing on panel 2, and the same flat line on panel 3. Callout: "v = 0 here; a = −9.80 here — not 0."
- Output medium: Manim (mp4)
- Two testable predictions: P1: Peak time t_peak = v₀/g = 13.0/9.80 = 1.327 s — exact, checkable from the v vs t crossing; peak height y_max = v₀²/(2g) = 8.62 m — checkable from the y vs t panel; P2: At t = 2.65 s the rock returns to y = 0 with v = −13.0 m/s (magnitude equals launch speed, opposite direction) — a symmetry of constant-acceleration motion, exact for symmetric trajectories
- The change: Re-run on the Moon with g_Moon = 1.62 m/s² — same initial velocity, but peak height = 52.2 m (6× higher), return time = 16.0 s (6× longer); the three-panel comparison shows the same parabola and line structure but with dramatically different scales, making the g-dependence concrete
- Human supplies (Claude can't): Nothing — fully synthetic/analytic
- Teardown angle: At the peak, students always want acceleration to be zero because the rock "isn't moving." But acceleration is not velocity — it is the rate at which velocity changes, and gravity never pauses; the moment-by-moment record of all three quantities kills the confusion permanently
- Exclusions: Air resistance correction (a separate simulation card); derivation of the kinematic equations from definitions (belongs in narration); projectile motion in 2D (Chapter 3 content)
- Sim slug: physics-free-fall-three-panels
- Score: 9/10

---

## Candidate 04 — Animate "SHM Energy Exchange: KE and PE Trading Every Quarter Period"
- Source: `physics/chapters/16-oscillatory-motion-and-waves.md`
- Topic: Simple Harmonic Motion / Energy Conservation
- Lane: MANIM (directed animation)
- Hook: A mass on a spring cycles forever. Watch kinetic energy and potential energy chase each other in perfect antiphase — KE peaks when PE bottoms, and vice versa, twice per cycle — while their sum never moves. The shape of each curve is a squared cosine: a fact the algebra guarantees and the animation makes obvious.
- The rule: x(t) = A cos(ωt), ω = √(k/m). KE(t) = ½mv² = ½mω²A²sin²(ωt). PE(t) = ½kx² = ½kA²cos²(ωt). E_total = ½kA² = constant. v_max = Aω (at x = 0). T = 2π√(m/k). Period is independent of amplitude — isochronism.
- Concrete numbers: m = 0.50 kg, k = 50 N/m, A = 0.10 m. ω = √(50/0.50) = 10 rad/s. T = 2π/10 = 0.628 s. E_total = ½×50×(0.10)² = 0.25 J. v_max = 0.10×10 = 1.0 m/s. At x = 0.07 m: PE = ½×50×(0.07)² = 0.122 J, KE = 0.25 − 0.122 = 0.128 J.
- The artifact / what moves: Top panel: animated mass-spring system (mass sliding horizontally, spring stretching/compressing). Bottom panel: energy vs time graph, two curves drawing simultaneously — KE (blue, sin²) and PE (red, cos²), both oscillating between 0 and 0.25 J, a horizontal green line at 0.25 J labeled "E_total = constant." The time axis of the energy graph is synchronized with the top panel: when the mass passes through equilibrium, the KE curve peaks and the PE curve hits zero simultaneously. At the turnaround (maximum compression/extension), KE hits zero and PE peaks. A second demo sweeps amplitude from 0.10 m to 0.20 m and back — the energy curves grow (higher total), but the period of the mass on top doesn't change.
- Output medium: Manim (mp4)
- Two testable predictions: P1: v_max = A√(k/m) = 0.10×√(50/0.50) = 1.0 m/s — exact, checkable from energy conservation at x = 0 (½mv_max² = ½kA²); P2: T = 2π√(m/k) = 2π√(0.50/50) = 0.628 s — independent of A; doubling A from 0.10 to 0.20 m does not change T, checkable by counting oscillation cycles in the animation at both amplitudes
- The change: Replace the spring with a pendulum (same mass, length L such that T matches): L = gT²/(4π²) = 9.80×(0.628)²/(4π²) ≈ 0.099 m ≈ 10 cm pendulum. The energy curves are identical in shape, demonstrating that SHM's energy structure is universal across all linear restoring systems
- Human supplies (Claude can't): Nothing — fully synthetic/analytic
- Teardown angle: Isochronism — that the period doesn't depend on amplitude — is what makes oscillators work as clocks; a pendulum that swings 5° or 10° keeps the same time, which is why pendulum clocks were the world's most accurate timekeepers for 200 years, until the quartz crystal (also a harmonic oscillator) replaced them
- Exclusions: Damped oscillation decay envelope (separate card); resonance driving (separate card); derivation of ω = √(k/m) from the differential equation (belongs in narration)
- Sim slug: physics-shm-energy-exchange
- Score: 9/10

---

## Candidate 05 — Animate "Young's Double-Slit: Fringe Pattern Building From Path Difference"
- Source: `physics/chapters/27-wave-optics.md`
- Topic: Wave Optics / Interference
- Lane: MANIM (directed animation)
- Hook: Two slits emit circular wavefronts. Watch the expanding rings overlap — where crests meet crests, a bright stripe; where crests meet troughs, dark silence. The interference pattern isn't painted on the screen. It emerges from the geometry, one path-difference calculation at a time.
- The rule: Bright fringe: d sinθ = mλ. Fringe spacing on screen: Δy = λL/d. At small angles, y_m = mλL/d. Central bright fringe at m = 0. Dark fringes at d sinθ = (m+½)λ.
- Concrete numbers: λ = 633 nm (red laser), d = 0.10 mm = 10⁻⁴ m, L = 2.00 m. Δy = (633×10⁻⁹×2.00)/(10⁻⁴) = 1.27 cm. m = 1 bright fringe: sinθ₁ = λ/d = 6.33×10⁻³, θ₁ = 0.36°. m = ±1, ±2, ±3 fringes visible within ±5° (small angle approx holds to better than 1%).
- The artifact / what moves: Two slits on the left emit expanding circular wavefronts (animated concentric arcs from each slit). The arcs expand rightward and overlap. Where they are in phase (path difference = 0, λ, 2λ...) the overlap region brightens to white; where out of phase (λ/2, 3λ/2...) the overlap darkens to black. The pattern of constructive/destructive interference traces out naturally from the wave geometry. A vertical screen on the right accumulates intensity: bright bands build up at predicted y_m values, dark gaps at (m+½)λ/d×L. After pattern establishes, a wavelength slider shifts λ from 400 nm (violet) to 700 nm (red): fringe spacing Δy = λL/d expands visibly as λ increases, confirming the linear relationship.
- Output medium: Manim (mp4)
- Two testable predictions: P1: Fringe spacing Δy = λL/d = 633×10⁻⁹×2.00/10⁻⁴ = 1.27 cm — exact, measurable from the screen in the animation; P2: Switching to λ = 400 nm (violet) gives Δy = 0.80 cm — ratio Δy_violet/Δy_red = 400/633 = 0.632, an exact wavelength ratio, verifiable from the relative fringe spacings in the animation
- The change: Reduce slit separation d from 0.10 mm to 0.05 mm while holding all else constant — fringe spacing doubles from 1.27 cm to 2.54 cm, confirming Δy ∝ 1/d; this is the experimental handle Young used to extract wavelengths from sunlight in 1803
- Human supplies (Claude can't): Nothing — fully synthetic/analytic; wavelengths and slit geometry are input parameters
- Teardown angle: Young's experiment didn't just show that light is a wave — it gave the first measurement of the wavelength of visible light, a number nobody had before; watching the fringes build from geometry is watching 200 years of debate resolved in three lines of arithmetic
- Exclusions: Diffraction grating (N-slit extension — a separate card); single-slit diffraction envelope that modulates the double-slit pattern (second-order effect, belongs in narration); thin-film interference (separate setup)
- Sim slug: physics-double-slit-interference
- Score: 9/10

---

## Candidate 06 — Animate "Lorentz Factor γ: Flat Until 0.5c, Then the Cliff"
- Source: `physics/chapters/28-special-relativity.md`
- Topic: Special Relativity / Time Dilation and Length Contraction
- Lane: MANIM (directed animation)
- Hook: At everyday speeds — cars, aircraft, even satellites — the Lorentz factor is 1.000000001. Nothing. But at 0.9c it's 2.3. At 0.99c it's 7. At 0.999c it's 22. Watch the γ curve draw and see the cliff that makes "faster than light" physically impossible, not just against the rules.
- The rule: γ = 1/√(1−v²/c²). Time dilation: Δt = γΔt₀ (moving clock runs slow). Length contraction: L = L₀/γ (moving ruler shrinks). As v → c, γ → ∞, which means infinite energy required. Energy: E = γmc².
- Concrete numbers: v = 0.1c: γ = 1.005 (0.5% correction). v = 0.5c: γ = 1.155 (15% correction). v = 0.866c: γ = 2.0 (doubled time, halved length). v = 0.9c: γ = 2.29. v = 0.99c: γ = 7.09. v = 0.999c: γ = 22.4. Muon at 0.999c: proper lifetime 2.20 µs → measured lifetime 49.3 µs. LHC proton: γ ≈ 7460, speed = c − 9 parts per billion.
- The artifact / what moves: Horizontal axis: v/c from 0 to 1.0. Vertical axis: γ from 1 to 20. The γ curve draws left to right. From v = 0 to 0.5c: barely moves, labeled "GPS satellite, airplane, rock." From 0.5c to 0.9c: begins to curve upward noticeably. From 0.9c to 0.99c: steepens dramatically. The curve asymptotes toward v = c with a vertical dashed line at exactly c. Labeled markers: muon (0.999c, γ = 22.4); LHC proton (0.9999999c, γ = 7460, marked as a dot near the asymptote). Second panel: a moving clock animation at three speeds — at 0.1c, nearly normal rate; at 0.9c, running at half speed; at 0.99c, running at 1/7 speed — the ticking rate visually confirms Δt = γΔt₀.
- Output medium: Manim (mp4)
- Two testable predictions: P1: At v = 0.866c, γ = 1/√(1−0.75) = 1/0.5 = 2.0 exactly — moving clock runs at exactly half rate, moving ruler at exactly half length; this is the only speed where γ is an exact integer near the interesting part of the curve; P2: LHC proton at 7 TeV kinetic energy: γ = (E_total)/(m_pc²) = (7000 MeV + 938 MeV)/(938 MeV) = 8.46×10³/938 ≈ 7460; from this γ, v/c = √(1 − 1/γ²) = 1 − 9×10⁻⁹, meaning the proton travels at c minus 9 parts per billion — verifiable from γ alone
- The change: Overlay the classical kinetic energy KE = ½mv² vs the relativistic KE = (γ−1)mc² on a single plot vs v/c: they agree below 0.1c and diverge dramatically above 0.5c, showing exactly where classical mechanics starts failing and where the energy cost of further acceleration becomes prohibitive
- Human supplies (Claude can't): Nothing — fully synthetic/analytic; all values from the Lorentz formula and published particle physics parameters
- Teardown angle: There is no physics prohibition sign at v = c — there is a mathematical wall: γ diverges, meaning an infinite amount of energy would be required to reach c; you cannot exceed c not because you break a rule but because the bookkeeping forbids it
- Exclusions: Full twin-paradox resolution (belongs in narration); general-relativistic gravitational time dilation (GPS's +45 µs/day — separate topic); energy-momentum invariant E² = (pc)² + (mc²)² (belongs in narration)
- Sim slug: physics-lorentz-gamma-curve
- Score: 8/10

---

## Candidate 07 — Animate "de Broglie Wavelength: Why We Don't See Bowling-Ball Diffraction"
- Source: `physics/chapters/29-quantum-physics.md`
- Topic: Quantum Physics / Matter Waves
- Lane: MANIM (directed animation)
- Hook: Every moving object has a wavelength: λ = h/p. A bowling ball at 10 m/s has λ = 2×10⁻³⁵ m — smaller than a proton by 20 orders of magnitude. An electron at 100 eV has λ = 0.12 nm — comparable to atomic spacings, which is why electrons diffract from crystals. Watch the wavelength animate across 35 orders of magnitude as you slide mass from electron to bowling ball.
- The rule: λ = h/p = h/(mv) for non-relativistic particles. For electron at voltage V: KE = eV = ½mv², so λ = h/√(2meV). For non-relativistic particles: λ decreases as 1/√(KE). h = 6.626×10⁻³⁴ J·s. m_e = 9.11×10⁻³¹ kg.
- Concrete numbers: Electron at 100 eV: KE = 1.6×10⁻¹⁷ J, p = √(2×9.11×10⁻³¹×1.6×10⁻¹⁷) = 1.71×10⁻²⁴ kg·m/s, λ = 6.626×10⁻³⁴/1.71×10⁻²⁴ = 0.39 Å = 0.039 nm. Davisson-Germer (54 eV): λ ≈ 0.167 nm, Ni lattice spacing = 0.215 nm (same order). TEM at 200 keV (relativistic): λ ≈ 0.0025 Å. Bowling ball (3 kg, 10 m/s): λ = 6.626×10⁻³⁴/(30) = 2.2×10⁻³⁵ m. Human (70 kg, 1.5 m/s): λ = 6.3×10⁻³⁶ m.
- The artifact / what moves: Log-scale horizontal axis spanning 35 orders of magnitude in λ (from 10⁻³⁵ m to 1 m). A marker slides along the axis as object mass/energy sweeps from electron to proton to protein molecule to human to bowling ball. At each position, a labeled dot shows the object and its wavelength. Key reference lines: atomic spacing (0.1 nm), X-ray wavelength (0.1 nm), visible light (400–700 nm). The electron's wavelength falls in the atomic-spacing band — label "diffraction possible." The bowling ball's wavelength falls 20 orders of magnitude below any conceivable aperture — label "diffraction impossible." A simulation of the Davisson-Germer experiment shows: electron beam on nickel crystal, interference pattern appears. Same beam energy but now proton mass — wavelength shrinks by √(1836), pattern disappears.
- Output medium: Manim (mp4)
- Two testable predictions: P1: λ_electron(54 eV) = h/√(2m_eV) = 6.626×10⁻³⁴/√(2×9.11×10⁻³¹×54×1.6×10⁻¹⁹) = 1.67 Å — matches the Ni lattice spacing (2.15 Å) closely enough for strong diffraction, exactly what Davisson-Germer observed at their 50° peak; P2: λ_bowling/λ_electron(100 eV) = (2.2×10⁻³⁵)/(3.9×10⁻¹¹) = 5.6×10⁻²⁵ — the ratio of wavelengths is 25 orders of magnitude, verifiable from the log-scale axis; no slit this small could be machined
- The change: Slide from electron to proton (both at 100 eV kinetic energy): λ_proton = h/√(2×1.67×10⁻²⁷×1.6×10⁻¹⁷) = 9.1×10⁻¹² m — still sub-atomic, so proton diffraction from crystals should also be possible; thermal neutrons (at room temperature) have λ ≈ 1 Å — same order as atomic spacings, and neutron diffraction is indeed a standard crystal-structure tool
- Human supplies (Claude can't): Nothing — fully synthetic/analytic; all parameters from fundamental constants and tabulated particle masses
- Teardown angle: Wave-particle duality isn't weird for electrons because electrons are small — it's because h is so tiny that the wavelength only becomes comparable to anything real when momenta are also tiny; the bowling ball has a perfectly good de Broglie wavelength, it's just invisible because no aperture in the universe is small enough to diffract it
- Exclusions: Davisson-Germer Bragg peak derivation (belongs in narration); full quantum-mechanical wavefunction evolution (beyond this chapter); Compton effect calculation (separate worked example)
- Sim slug: physics-de-broglie-wavelength-scale
- Score: 8/10

---

## Candidate 08 — Animate "Resonance Quality Factor Q: Sharp vs. Broad Response Curves"
- Source: `physics/chapters/16-oscillatory-motion-and-waves.md`
- Topic: Resonance / Damping
- Lane: MANIM (directed animation)
- Hook: A tuning fork and a car shock absorber have the same natural frequency. But when you drive them, the tuning fork rings for thousands of cycles and responds only to a needle-thin frequency band; the shock absorber barely rings and responds to almost anything. Watch three response curves — Q = 2, Q = 10, Q = 100 — narrow from broad plateau to sharp spike as Q rises.
- The rule: Steady-state amplitude at driving frequency f: A(f) ∝ 1/√((f²−f₀²)² + (f₀f/Q)²). Peak amplitude ∝ Q. Peak width (FWHM) = f₀/Q. Free-decay: amplitude envelope ∝ e^(−πf₀t/Q). Number of oscillations to decay to 1/e: Q/π.
- Concrete numbers: f₀ = 440 Hz (A above middle C tuning fork). Q = 1000 (tuning fork): FWHM = 440/1000 = 0.44 Hz. Q = 1 (shock absorber): FWHM = 440 Hz (responds to entire range). Taipei 101 TMD: f₀ ≈ 0.15 Hz, L_pendulum = gT²/(4π²) = 9.80×(6.67)²/(4π²) ≈ 11 m, Q ≈ 5 (deliberately low to dissipate energy). Quartz crystal: f₀ = 32,768 Hz, Q ≈ 10⁵, FWHM ≈ 0.33 Hz.
- The artifact / what moves: Frequency axis: 0 to 2f₀. Amplitude axis: 0 to Q×(reference). Three curves draw sequentially: Q = 2 (broad, low peak — barely distinguishable from baseline), Q = 10 (moderate peak), Q = 100 (sharp spike at f₀, peak 100× the Q = 2 height). All three peak at exactly the same natural frequency f₀. A horizontal ruler shows each peak's FWHM: Q = 2 → very wide, Q = 100 → very narrow. Second panel: time-domain decay for each Q — Q = 2 dies in ~2 oscillations, Q = 100 rings for ~30 oscillations. Final callout: quartz watch (Q = 10⁵, FWHM = 0.33 Hz), car suspension (Q ≈ 0.5–1.0, FWHM spans entire range).
- Output medium: Manim (mp4)
- Two testable predictions: P1: FWHM = f₀/Q — at Q = 100 and f₀ = 440 Hz, FWHM = 4.4 Hz; at Q = 10, FWHM = 44 Hz — ratio of bandwidths = 10, exactly equal to the Q ratio; P2: Number of oscillations to decay to 1/e of initial amplitude = Q/π — for Q = 100, the ring-down lasts 100/π ≈ 32 oscillations; for Q = 2, it lasts 2/π ≈ 0.64 oscillations (dies before completing one full cycle)
- The change: Show the Taipei 101 tuned mass damper — the building has a natural frequency f₀ ≈ 0.15 Hz, and the 660-tonne ball is tuned to match, but deliberately with low Q so it dissipates energy rather than storing it; the same Q concept that makes tuning forks useful as frequency references is weaponized in reverse to kill building resonance
- Human supplies (Claude can't): Nothing — fully synthetic/analytic; the Q-factor formula is analytic and Taipei 101's parameters are published engineering data used only as labeled reference points
- Teardown angle: The 1940 Tacoma Narrows Bridge collapse is usually taught as "resonance" — a tidy story. The actual failure mode was aeroelastic flutter, a nonlinear feedback between the bridge's motion and the aerodynamic forces it generated. But the lesson is the same: structures have natural frequencies, and sustained forcing near those frequencies can destroy them; high-Q makes instruments useful and bridges dangerous
- Exclusions: Full damped-oscillator differential equation solution (belongs in narration); Tacoma Narrows aerodynamics derivation (beyond chapter scope); electrical circuit Q-factor analog (Chapter 23 content)
- Sim slug: physics-resonance-quality-factor
- Score: 8/10

---

## Candidate 09 — Animate "Electric Field Lines: Dipole Geometry and the 1/r² vs 1/r³ Falloff"
- Source: `physics/chapters/18-electric-charge-and-electric-field.md`
- Topic: Electric Field / Dipole
- Lane: MANIM (directed animation)
- Hook: A single charge's field fades as 1/r². A dipole's field fades faster — as 1/r³ — because the two contributions nearly cancel at large distances. Watch field lines trace the dipole's characteristic figure-eight pattern, then plot |E| vs distance along the axis to see the steeper falloff confirmed numerically.
- The rule: Point charge: E = kq/r². Dipole (along axis, r >> d): E_axis ≈ 2kp/r³ where p = qd. Dipole (perpendicular bisector): E_perp ≈ kp/r³. Falloff ratio at any given r: E_dipole/E_monopole ∝ d/r → 0 as r → ∞.
- Concrete numbers: q = 1 nC = 10⁻⁹ C, d = 0.01 m (p = qd = 10⁻¹¹ C·m). At r = 0.05 m along axis: E_axis = 2kp/r³ = 2×9×10⁹×10⁻¹¹/(0.05)³ = 1440 N/C. Compare single +q at same r: E = kq/r² = 9×10⁹×10⁻⁹/(0.05)² = 3600 N/C. Ratio = 1440/3600 = 0.4 (dipole already weaker by 2.5×). At r = 0.10 m: dipole/monopole = (0.05/0.10)² × (d/r) — falloff is steeper by exactly one power.
- The artifact / what moves: Two point charges (+q on top, −q on bottom) appear at separation d. Field lines draw from +q, curve through space, and terminate on −q in the characteristic figure-eight hourglass pattern. As lines draw, color-coded arrows show field direction. Second scene: axes E vs r drawn. Two curves draw simultaneously — monopole (1/r², blue) and dipole along axis (1/r³, red). At r = 0.05 m they're both plotted from the concrete numbers above. The 1/r³ curve falls noticeably faster. At r = 0.20 m the monopole curve is 4× above its r = 0.10 m value; the dipole is 8× above its r = 0.10 m value. Both verified by numerical labels at marked points.
- Output medium: Manim (mp4)
- Two testable predictions: P1: E_axis at r = 0.05 m = 2kp/r³ = 2×9×10⁹×10⁻¹¹/(1.25×10⁻⁴) = 1440 N/C — exact, checkable from the dipole formula; E_monopole at same r = 3600 N/C — ratio = 0.4 = 2d/(r) = 2×0.01/0.05 = 0.4, confirming the extra 1/r factor; P2: Doubling r from 0.05 m to 0.10 m: monopole drops by factor 4, dipole drops by factor 8 — the ratio of ratios is exactly 2 = r_2/r_1, confirming one extra power of r in the falloff
- The change: Introduce a quadrupole (two dipoles head-to-tail) — field falls as 1/r⁴; animate all three (monopole, dipole, quadrupole) together to show the multipole hierarchy; this explains why molecules with net charge (monopole) dominate at long range, while neutral polar molecules (dipole) dominate at intermediate range, and neutral non-polar molecules (quadrupole or higher) interact only very close up
- Human supplies (Claude can't): Nothing — fully synthetic/analytic
- Teardown angle: The 1/r³ dipole falloff is why water dissolves salt: the dipole field of a water molecule is strong enough at short range to peel Na⁺ and Cl⁻ apart from their crystal, but vanishes quickly enough at longer range that the solution bulk is electrically quiet
- Exclusions: Full multipole expansion derivation (belongs in narration); Maxwell stress tensor (beyond this chapter); induced dipoles and polarizability (Chapter 19 content)
- Sim slug: physics-dipole-field-falloff
- Score: 8/10

---

## Candidate 10 — Animate "Elastic Collision Mass Ratio: Cue Ball Stops, Heavy Target Bounces Back"
- Source: `physics/chapters/08-linear-momentum-and-collisions.md`
- Topic: Linear Momentum / Elastic Collisions
- Lane: MANIM (directed animation)
- Hook: Two elastic collision formulas, two extreme mass ratios, two completely different outcomes. Equal masses: the bullet stops dead and the target takes off. Heavy bullet hits light target: bullet barely slows, target launches at twice the bullet speed. Light bullet hits wall: bounces back at the same speed. Watch all three as parametric morphs as the mass ratio sweeps from 0.01 to 100.
- The rule: 1D elastic collision, m₁ moving at v₁, m₂ at rest. v₁f = (m₁−m₂)/(m₁+m₂)×v₁. v₂f = 2m₁/(m₁+m₂)×v₁. Special limits: m₁ = m₂ → v₁f = 0, v₂f = v₁ (Newton's cradle). m₁ >> m₂ → v₁f ≈ v₁, v₂f ≈ 2v₁ (light target barely affects bullet). m₁ << m₂ → v₁f ≈ −v₁, v₂f ≈ 0 (ping-pong ball bounces off wall).
- Concrete numbers: m₁ = m₂ = 1 kg, v₁ = 2 m/s: v₁f = 0, v₂f = 2 m/s. m₁ = 10 kg, m₂ = 1 kg: v₁f = (9/11)×2 = 1.636 m/s, v₂f = (20/11)×2 = 3.636 m/s. m₁ = 1 kg, m₂ = 10 kg: v₁f = (−9/11)×2 = −1.636 m/s, v₂f = (2/11)×2 = 0.364 m/s. All cases: momentum before = 2 kg·m/s, momentum after = 2 kg·m/s (exact). KE before = ½×1×4 = 2 J; KE after = ½×1×0 + ½×1×4 = 2 J (exact, equal masses).
- The artifact / what moves: Two colored blocks on a frictionless track. Block 1 (blue) moves right at v₁ = 2 m/s. Block 2 (red) sits at rest. They collide and separate. Velocity arrows update before and after. A mass-ratio slider r = m₁/m₂ sweeps from 0.1 to 10. At r = 1: blue stops, red moves off at same speed. At r > 1: blue continues forward (slower), red moves faster than blue. At r < 1: blue bounces backward, red barely moves. Numerical readouts confirm v₁f and v₂f at every slider position. Momentum check: sum of momentum×mass shown at all times — flat horizontal line confirming conservation.
- Output medium: Manim (mp4)
- Two testable predictions: P1: At equal masses (r = 1), v₁f = 0 exactly — the cue ball stops dead; this is the exact solution to the two-equation system and can be verified from the formula (m₁−m₂)/(m₁+m₂) → 0; P2: At m₁ >> m₂ (r = 100), v₂f ≈ 2v₁ = 4 m/s — a light target acquires twice the bullet's speed; from the formula, v₂f = 2m₁/(m₁+m₂)×v₁ → 2v₁ as m₁/m₂ → ∞, with the r = 100 case giving 2×100/101×2 = 3.96 m/s, within 2% of 4.0 m/s
- The change: Show a Newton's cradle with 5 balls — why does only one ball fly out when one comes in, not two at half speed? The system must satisfy both momentum AND kinetic energy conservation simultaneously, and the "two balls at half speed" solution violates kinetic energy conservation — the animation can verify this by computing KE for both outcomes
- Human supplies (Claude can't): Nothing — fully synthetic/analytic
- Teardown angle: The equal-mass stop-dead result is the physics behind billiards strategy — the cue ball stops and the target ball moves because conservation of energy + momentum simultaneously demand it; no other outcome is consistent with both equations
- Exclusions: 2D collision geometry (off-axis billiard shots — separate card); inelastic collision KE loss derivation (different setup); center-of-mass frame analysis (beyond this chapter's scope)
- Sim slug: physics-elastic-collision-mass-ratio
- Score: 8/10

---

## Summary — pilot scan (physics, MANIM lane)

| Candidate | Title | Manim move | Score |
|---|---|---|---|
| 01 | Projectile Range Curve — 45° Wins | Five arcs draw, then R(θ) traces out from arcs | 9/10 |
| 02 | Orbital Speed + Kepler T² ∝ r³ | Live orbits at relative speeds, then log-log line | 9/10 |
| 03 | Free Fall — Three Panels in Sync | y(t), v(t), a(t) drawing simultaneously, cursor sweeps | 9/10 |
| 04 | SHM Energy Exchange KE↔PE | Mass-spring + energy graph antiphase cosine curves | 9/10 |
| 05 | Young's Double-Slit Fringe Pattern | Wavefront expansion → interference pattern buildup | 9/10 |
| 06 | Lorentz Factor γ Cliff Near c | γ curve drawing left to right, asymptoting at c | 8/10 |
| 07 | de Broglie Wavelength 35-Decade Span | Log-scale slider: electron → bowling ball | 8/10 |
| 08 | Resonance Quality Factor Q | Three A(f) curves narrowing with Q | 8/10 |
| 09 | Dipole Field 1/r³ vs Monopole 1/r² | Field-line figure-eight + log-log falloff comparison | 8/10 |
| 10 | Elastic Collision Mass-Ratio Morph | Two blocks + mass-ratio slider showing three regimes | 8/10 |

**Build-soon (9/10):** Candidates 01–05.
**Build after tightening (8/10):** Candidates 06–10.
**D3/DATAVIZ pass (not yet scouted):** Interactive projectile launcher, real-time orbit simulator with eccentricity slider, double-slit pattern with wavelength control, Lorentz-factor energy cost explorer.
