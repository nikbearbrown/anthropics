# University Physics Bundle With LLMs — Simulation Ideas

> MANIM lane only. Score ≥ 6. Cards produced by sim-scout 2026-07-26.

---

## Candidate 01 — SHM Triple Sync: Position, Velocity, and Acceleration Dancing in Phase

- Source: `university-physics-bundle-with-llms/chapters/17-oscillations.md`
- Topic: Simple Harmonic Motion
- Lane: MANIM (directed animation)
- Hook: Everyone knows a spring oscillates — but almost no one can predict where velocity peaks. The answer is always exactly where displacement is zero, and the animation makes this unavoidable.
- The rule: x(t) = A cos(ω₀t + φ); v(t) = −Aω₀ sin(ω₀t + φ); a(t) = −Aω₀² cos(ω₀t + φ); ω₀ = √(k/m)
- Concrete numbers: m = 2.00 kg, k = 32.0 N/m; ω₀ = 4.00 rad/s, T = 1.57 s, A = 0.020 m; v_max = 0.080 m/s; a_max = 0.32 m/s²; equations: x(t) = 0.020 cos(4.00t), v(t) = −0.080 sin(4.00t), a(t) = −0.32 cos(4.00t)
- The artifact / what moves: Three synchronized sinusoidal curves draw simultaneously — x in blue, v in green, a in red — on a shared time axis; a moving vertical cursor sweeps across all three, with markers highlighting that v = v_max exactly when x = 0, and a = a_max exactly when x = ±A; at t = T/4 = 0.393 s a flash simultaneously marks: x = 0, v = −0.080 m/s (maximum), a = 0 — the three relationships locked in one frame
- Output medium: Manim (mp4)
- Two testable predictions: P1: At t = T/4 = 0.393 s, displacement is exactly zero and velocity is exactly −v_max = −0.080 m/s — verifiable by pausing the animation and reading the y-axis; P2: Acceleration lags displacement by exactly π (180°) — when x = +A, a = −a_max = −0.32 m/s², readable from the two curves being mirror images
- The change: Double the spring constant k → ω₀ increases by √2, period drops from 1.57 s to 1.11 s, all three curves compress horizontally but the phase relationships are unchanged — showing that the synchrony is independent of frequency
- Human supplies (Claude can't): Nothing — fully synthetic/analytic
- Teardown angle: Every student learns x, v, a separately and misremembers the phase. The animation forces recognition that they are all the same cosine, just shifted — and the simultaneous cursor makes the 90° phase lead of velocity unmistakable
- Exclusions: Damping, energy exchange, multiple DOF, phase shift φ ≠ 0
- Sim slug: `physics-shm-triple-sync`
- Score: 8/10

---

## Candidate 02 — Damped Oscillator Envelope: Three Regimes from One Equation

- Source: `university-physics-bundle-with-llms/chapters/17-oscillations.md`
- Topic: Damped Oscillations
- Lane: MANIM (directed animation)
- Hook: Add a little friction to a spring and it oscillates forever — but quieter each cycle. Add more, and it just glides back. Add exactly the critical amount, and it stops as fast as possible without overshooting. Three futures from one dial.
- The rule: x(t) = A₀ e^(−bt/2m) cos(ωt + φ) for underdamped; ω = √(ω₀² − (b/2m)²); critical: b_c = 2√(mk) = 2mω₀; τ = 2m/b (amplitude e-folding time)
- Concrete numbers: m = 1.0 kg, k = 16.0 N/m → ω₀ = 4.0 rad/s, T₀ = 1.57 s; underdamped: b = 2.0 N·s/m → b/2m = 1.0 s⁻¹, ω = √(16 − 1) = 3.87 rad/s, τ = 1.0 s; critically damped: b_c = 8.0 N·s/m; overdamped: b = 16.0 N·s/m; at t = 1.0 s (underdamped case), amplitude has decayed to A₀/e ≈ 0.368 A₀
- The artifact / what moves: A single spring-mass system; a damping slider (b) starts at underdamped — the mass oscillates while a dashed envelope curve e^(−bt/2m) descends around the oscillation; as b increases to b_c the oscillations fade and the return becomes a smooth S-curve; at b > b_c the mass sluggishly creeps back; a side panel plots all three return curves on the same time axis for direct comparison, with the critical-damping curve arriving first
- Output medium: Manim (mp4)
- Two testable predictions: P1: For b = 2.0 N·s/m (underdamped), amplitude at t = 1.0 s is exactly e⁻¹ ≈ 0.368 of the initial amplitude — the envelope curve must intersect the peak at that height; P2: The critically damped case (b = 8.0 N·s/m, b_c = 2√(1.0 × 16.0) = 8.0 N·s/m) returns to equilibrium strictly faster than any underdamped or overdamped case — verifiable by time-stamping when each curve crosses x = 0.01 m (1% of A₀)
- The change: Animate the quality factor Q = mω₀/b — high Q shows many oscillations before decay; Q = 0.5 is critical; Q < 0.5 is overdamped. The Tacoma Narrows had high Q until it didn't.
- Human supplies (Claude can't): Nothing — fully synthetic/analytic
- Teardown angle: The textbook says "critically damped returns fastest" — students nod and move on. The animation forces a comparison: every other b value is visibly slower, and only b_c threads the needle. Car shock absorbers, door closers, galvanometer needles — all critically damped for this reason.
- Exclusions: Coulomb friction, nonlinear damping, coupled oscillators, driven response
- Sim slug: `physics-damped-oscillator-regimes`
- Score: 9/10

---

## Candidate 03 — Resonance Amplitude Curve: A(ω_d) Peaking as Driving Frequency Sweeps Through ω₀

- Source: `university-physics-bundle-with-llms/chapters/17-oscillations.md`
- Topic: Driven Oscillations / Resonance
- Lane: MANIM (directed animation)
- Hook: A wine glass shatters, a bridge collapses, a radio finds one station out of a hundred — all the same equation. Drive anything at its natural frequency and the amplitude explodes. Drive it even slightly off, and it barely moves.
- The rule: A(ω_d) = F₀ / √(m²(ω_d² − ω₀²)² + b²ω_d²); at resonance A_max = F₀/(bω₀); Q = mω₀/b = ω₀/Δω
- Concrete numbers: m = 1.0 kg, k = 16.0 N/m → ω₀ = 4.0 rad/s; F₀ = 1.0 N; low damping b = 0.5 N·s/m → A_max = 1.0/(0.5 × 4.0) = 0.500 m, Q = 1.0 × 4.0/0.5 = 8.0; high damping b = 2.0 N·s/m → A_max = 1.0/(2.0 × 4.0) = 0.125 m, Q = 2.0; at ω_d = 4.0 rad/s and b = 0.5 the amplitude is 4× what it is at ω_d = 2.0 rad/s (where A ≈ 0.125 m from the denominator)
- The artifact / what moves: A driving-frequency axis sweeps from ω_d = 0 to 8 rad/s; the amplitude response curve A(ω_d) traces itself left-to-right in real time; a vertical marker riding the curve shows the current amplitude on a live mass-spring animation alongside; the curve peaks sharply at ω_d = ω₀ = 4.0 rad/s; a second curve for higher b is drawn simultaneously, showing the same peak location but shorter and broader; Q is labelled at each peak
- Output medium: Manim (mp4)
- Two testable predictions: P1: With b = 0.5 N·s/m, the peak amplitude is exactly 0.500 m at ω_d = ω₀ = 4.0 rad/s, and at ω_d = 2.0 rad/s the amplitude is approximately 0.124 m — the curve shape is measurable from the rendered frame; P2: The resonance bandwidth Δω = b/m = 0.5/1.0 = 0.5 rad/s for the low-damping case — the curve half-maximum points are at ω_d = 3.75 and 4.25 rad/s, verifiable by reading the x-axis at A = A_max/√2 = 0.354 m
- The change: Show three Q values (Q = 2, 8, 20) as three simultaneous curves — same peak location, same F₀, but peak heights differ by factor Q and widths differ inversely. Tacoma Narrows was high-Q and it showed.
- Human supplies (Claude can't): Nothing — fully synthetic/analytic
- Teardown angle: Resonance is not "vibrating at the same frequency" — it is the fraction F₀/(bω₀) that soars when damping is low. The animation makes the inverse relationship between damping and peak height impossible to miss.
- Exclusions: Transient response, phase lag at resonance, nonlinear resonance
- Sim slug: `physics-resonance-amplitude-curve`
- Score: 9/10

---

## Candidate 04 — Kepler's Equal-Area Law: An Elliptical Orbit Sweeping Equal Sectors in Equal Time

- Source: `university-physics-bundle-with-llms/chapters/14-gravitation.md`
- Topic: Kepler's Second Law / Angular Momentum Conservation
- Lane: MANIM (directed animation)
- Hook: A comet near the Sun moves so fast you can barely track it. The same comet near Pluto drifts almost imperceptibly. Yet in equal time intervals, both sweep out the same area. The universe is keeping a ledger — and the currency is angular momentum.
- The rule: dA/dt = L/2m = constant; L = mrv_⊥ = constant when τ_ext = 0; v_perihelion × r_perihelion = v_aphelion × r_aphelion (angular momentum)
- Concrete numbers: Halley's Comet: perihelion r_p = 0.586 AU, aphelion r_a = 35.0 AU, semi-major axis a = 17.8 AU, period T = 75.3 years; speed ratio v_p/v_a = r_a/r_p = 35.0/0.586 = 59.7 — the comet moves 59.7× faster at perihelion than aphelion; in equal time intervals Δt, area swept is identical at both extremes
- The artifact / what moves: A highly elliptical orbit draws — the Sun sits at one focus; the comet dot moves along the orbit, fast near perihelion and slow near aphelion; every 7.53-year interval (1/10 of the period), a shaded sector is drawn between two successive comet positions and the Sun; all ten sectors appear in sequence and are colored alternately — all sectors are visibly the same area despite their very different shapes (narrow wedges near perihelion, wide fan near aphelion); the area of each sector is numerically labeled
- Output medium: Manim (mp4)
- Two testable predictions: P1: The speed ratio v_perihelion/v_aphelion = r_aphelion/r_perihelion = 35.0/0.586 = 59.7 — the animation's velocity arrow near perihelion is 59.7× longer than near aphelion, measurable from the rendered frame; P2: The sector swept in the 7.53-year interval nearest perihelion has the same area as the sector swept in the 7.53-year interval nearest aphelion — sectors that look very different in shape must have equal numeric area labels
- The change: Animate a circular orbit — all sectors are equal-width wedges, and equal area is trivial (uniform speed). The ellipse makes the miracle visible by forcing vastly unequal widths to produce equal areas.
- Human supplies (Claude can't): Nothing — fully synthetic/analytic
- Teardown angle: Kepler observed equal areas empirically; Newton proved it is angular momentum conservation. The animation exposes the mechanism: the comet's close perihelion pass trades off distance for speed with exact compensation.
- Exclusions: Relativistic perihelion precession, tidal forces, non-Keplerian orbits
- Sim slug: `physics-kepler-equal-area-orbit`
- Score: 9/10

---

## Candidate 05 — Orbital Speed vs. Radius: v = √(GM/r) Showing the Inverse-Square Root Decay

- Source: `university-physics-bundle-with-llms/chapters/14-gravitation.md`
- Topic: Orbital Mechanics / Kepler's Third Law
- Lane: MANIM (directed animation)
- Hook: Double the orbital altitude and you expect half the speed. Wrong — it is only 1/√2 as fast. Triple the radius and the speed drops to 1/√3. The square root is the surprise, and it is why GPS satellites move slower than the ISS despite being higher.
- The rule: v_orbit = √(GM/r); T = 2π√(r³/GM); T² ∝ r³ (Kepler's Third Law)
- Concrete numbers: Earth: M = 5.97 × 10²⁴ kg, G = 6.67 × 10⁻¹¹ N·m²/kg²; ISS at r = 6.77 × 10⁶ m: v = 7.67 km/s, T = 92 min; GPS at r ≈ 26.56 × 10⁶ m (altitude 20,200 km): v = √(GM/r) = √(3.98 × 10¹⁴/2.656 × 10⁷) = 3.87 km/s, T ≈ 12 h; GEO at r = 42.16 × 10⁶ m: v = 3.07 km/s, T = 24 h
- The artifact / what moves: A schematic Earth sits at center; orbital rings appear at ISS, GPS, and GEO altitudes; a satellite dot moves along each ring simultaneously, clearly faster at lower orbits; a live graph plots v vs. r, tracing the 1/√r curve as r increases from 6.4 × 10⁶ m outward; numerical callouts label v and T at each of the three named orbits; the curve shape — concave, steeply dropping near Earth and flattening far away — makes the sublinear relationship viscerally clear
- Output medium: Manim (mp4)
- Two testable predictions: P1: At ISS altitude (r = 6.77 × 10⁶ m), v = 7.67 km/s and T = 92 min — the animation's ISS dot must complete one orbit in 92 animation-seconds (if 1 min → 1 s) with the speed label reading 7.67; P2: GPS speed (3.87 km/s) is exactly 7.67/3.87 = 1.98 times slower than ISS, not the 3.93× that would hold if speed were 1/r (not 1/√r) — the rendered v-axis labels expose the √r relationship
- The change: Add a v² vs. r panel — the curve becomes a clean straight-line 1/r, making Kepler's Third Law (T² ∝ r³, equivalent to v² ∝ 1/r) land visually
- Human supplies (Claude can't): Nothing — fully synthetic/analytic
- Teardown angle: Intuition says "higher orbit = slower" without knowing how much slower. The animation shows the exact √r scaling by placing three real satellites on the curve — and the GPS-vs-ISS comparison is close enough to recognizable to be jarring.
- Exclusions: Elliptical orbits, perturbations, atmospheric drag, orbital transfer burns
- Sim slug: `physics-orbital-speed-vs-radius`
- Score: 8/10

---

## Candidate 06 — Rolling Race: Solid Sphere vs. Hollow Shell, Moment of Inertia Decides

- Source: `university-physics-bundle-with-llms/chapters/11-fixed-axis-rotation.md`
- Topic: Rolling Without Slipping / Moment of Inertia
- Lane: MANIM (directed animation)
- Hook: Two balls, same mass, same radius, same slope, released simultaneously. One wins every time. The winner is not heavier, not larger, not smoother — it has more of its mass near the center. Moment of inertia is the hidden race variable.
- The rule: v_cm² = 2gh / (1 + I/MR²); solid sphere I = (2/5)MR² → v = √(10gh/7); hollow shell I = (2/3)MR² → v = √(6gh/5); ratio v_sphere/v_shell = √(10/7 ÷ 6/5) = √(50/42) ≈ 1.091
- Concrete numbers: h = 1.0 m; solid sphere v_cm = √(10 × 9.8 × 1.0/7) = √14.0 = 3.742 m/s; hollow shell v_cm = √(6 × 9.8 × 1.0/5) = √11.76 = 3.429 m/s; the solid sphere arrives 9.1% faster; time to bottom: using a = g sin θ/(1 + I/MR²) at θ = 30°: sphere a = 9.8 × 0.5/1.4 = 3.50 m/s²; shell a = 9.8 × 0.5/1.667 = 2.94 m/s²
- The artifact / what moves: Two side-by-side ramps at equal angles; a solid sphere (blue) and hollow shell (orange) of equal mass and radius release simultaneously; they roll downward, with a velocity arrow growing at each center of mass; the sphere pulls ahead and reaches the bottom first; a bar chart at the bottom shows the final-speed breakdown: translational KE and rotational KE as separate bars — the sphere converts less energy to rotation and more to translation, which is why it wins; the finish-line gap is labeled 9.1%
- Output medium: Manim (mp4)
- Two testable predictions: P1: At h = 1.0 m, the solid sphere arrives at v = 3.742 m/s and the hollow shell at v = 3.429 m/s — these speed labels must appear at the bottom of the rendered ramp; P2: The fraction of total energy in rotation at the bottom is (1/2)Iω²/Mgh = (I/MR²)/(1 + I/MR²) — for the sphere this is (2/5)/(7/5) = 2/7 ≈ 28.6%; for the shell it is (2/3)/(5/3) = 2/5 = 40.0% — the bar chart must show this 28.6% vs. 40.0% split
- The change: Add a uniform disk (I = MR²/2) and a ring (I = MR²) — four objects racing: sphere wins, then disk, then shell, then ring dead last. Every shape is a different fraction of rotational energy.
- Human supplies (Claude can't): Nothing — fully synthetic/analytic
- Teardown angle: Intuition says heavier or wider wins; the animation proves it is the mass distribution that decides — a hollow cannonball always loses to a solid marble of the same size and mass.
- Exclusions: Friction coefficient breakdown, slipping transitions, air resistance, non-uniform density
- Sim slug: `physics-rolling-race-moment-of-inertia`
- Score: 9/10

---

## Candidate 07 — Angular Momentum Conservation: Ice Skater Arms-In, Spin Quadruples

- Source: `university-physics-bundle-with-llms/chapters/12-angular-momentum.md`
- Topic: Conservation of Angular Momentum
- Lane: MANIM (directed animation)
- Hook: No external force, no push, no external torque — and yet she spins four times faster in an instant. She did it by moving her own arms. The rule is not about speed; it is about the product Iω staying constant while I collapses.
- The rule: L = Iω = constant when τ_ext = 0; if I₁ = I₀/4 then ω₁ = 4ω₀; KE_rot = L²/2I, so KE quadruples when I quarters (the extra energy comes from the skater's muscles)
- Concrete numbers: Arms extended: ω₀ = 2 rev/s, I₀ (arbitrary reference); arms pulled in: I₁ = I₀/4 → ω₁ = 4ω₀ = 8 rev/s; gymnast example (exact): I₀ = 21.6 kg·m², ω₀ = 1.0 rev/s → L = 21.6 kg·m²/s; tucked I₁ = 5.4 kg·m², ω₁ = 4.0 rev/s; KE_extended = ½ × 21.6 × (2π)² = 426 J; KE_tucked = ½ × 5.4 × (8π)² = 1704 J; muscle work = 1278 J
- The artifact / what moves: A figure-skater silhouette spins at 2 rev/s with arms extended; a moment-of-inertia diagram beside her shows mass distributed far from the axis; she pulls her arms in — the silhouette narrows, the spin rate jumps to 8 rev/s (4× visually obvious from the blur), and the I diagram collapses; two bar charts track simultaneously: angular momentum (flat line — conservation holds) and rotational KE (quadruples — the skater did work); the product Iω is shown numerically staying constant throughout
- Output medium: Manim (mp4)
- Two testable predictions: P1: Angular momentum before = L = I₀ × 2 rev/s and after = (I₀/4) × 8 rev/s = I₀ × 2 rev/s — equal, confirming conservation; the Iω numerical readout must show the same value at both states; P2: For the gymnast case (exact numbers), the tucked rotation rate is exactly 4.0 rev/s and the KE ratio KE_tucked/KE_extended = I₀/I₁ = 21.6/5.4 = 4.0 — the KE bar doubles twice (quadruples), labeled in joules
- The change: Show the reverse: skater extends arms while spinning — ω drops, KE decreases, L stays flat. The skater loses KE to the muscles doing negative work stretching out.
- Human supplies (Claude can't): Nothing — fully synthetic/analytic
- Teardown angle: Conservation of angular momentum feels passive — "nothing changes." The animation exposes the active flip: I drops, ω soars, and KE quadruples from muscle work — three quantities moving in opposite directions while L stands still.
- Exclusions: Precession, gyroscopic effects, friction at skate blade, non-axial angular momentum
- Sim slug: `physics-angular-momentum-skater`
- Score: 9/10
