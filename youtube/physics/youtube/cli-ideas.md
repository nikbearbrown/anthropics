# Physics (Introductory) — CLI Video Ideas ("X with Claude")

---

## Candidate 01 — Build the Carnot Efficiency Calculator: Why Two-Thirds of Your Gasoline Disappears
- Source: physics/chapters/15-thermodynamics.md
- Lane: BUILD (Claude Code)
- Hook: A gasoline engine converts only ~30% of chemical energy into motion. The other 70% leaves as heat — not because of bad engineering but because of a 200-year-old mathematical ceiling. This script computes it, plots it, and shows where the ceiling sits for real engines.
- The artifact: a Python script (~40 lines) using numpy and matplotlib that: (1) plots Carnot efficiency η = 1 - T_c/T_h vs T_h for fixed T_c = 300 K, over T_h from 400 to 3000 K, (2) marks real engine operating points (gasoline: T_h ≈ 2200 K, diesel: T_h ≈ 2500 K), (3) shows the gap between Carnot ceiling and actual efficiency (accounting for irreversibilities), (4) plots the PV diagram for a Carnot cycle with labeled isothermal and adiabatic strokes. Manim animates the curve sweeping up and the operating points appearing with annotations.
- Prompt seed: `claude "Write a Python script using numpy and matplotlib that: (1) plots Carnot efficiency eta=1-Tc/Th vs Th for Tc=300 K, Th from 400 to 3000 K; (2) marks points: gasoline (Th=2200K, actual_eta=0.30), diesel (Th=2500K, actual_eta=0.40), steam (Th=800K, actual_eta=0.38); (3) draws horizontal lines from each Carnot point down to the actual efficiency, labeling the gap as 'irreversibility losses'; (4) on a separate subplot, draws a Carnot PV cycle for n=1 mol ideal gas with Th=600K, Tc=300K showing two isotherms and two adiabats, shading the net work area."`
- Read / check: Verify Carnot efficiency at T_h = 2200 K, T_c = 300 K is (1 - 300/2200) ≈ 0.864. Confirm real gasoline efficiency is correctly stated as ~30%, leaving a gap of ~56 percentage points attributable to irreversibilities. Verify the PV cycle shape: isotherms are hyperbolas (PV=const), adiabats steeper than isotherms.
- Human supplies: Nothing — fully synthetic. Python with numpy, matplotlib.
- Output medium: Manim (two-panel: left — efficiency vs T_h curve with operating points annotated; right — PV Carnot cycle with shaded work area and four labeled strokes animating in)
- The change: Add a steam turbine to the comparison and compute what T_h would be needed to achieve 50% Carnot efficiency — showing the materials constraint on real improvement.
- Teardown angle: The gap between Carnot and actual efficiency is not laziness — it's physics. The Carnot ceiling is set by thermodynamics; the gap below it is set by friction, turbulence, and incomplete combustion. Engineers can narrow the gap; they cannot repeal the ceiling.
- Exclusions: Nuclear power thermodynamics, refrigeration cycle analysis.
- Score: 9/10

---

## Candidate 02 — Build the Kinetic Theory Simulator: Hot Is Fast
- Source: physics/chapters/13-temperature-kinetic-theory-and-the-gas-laws.md
- Lane: BUILD (Claude Code)
- Hook: Temperature is the average kinetic energy of randomly moving molecules. This simulation makes that connection visual — a box of particles whose speed distribution evolves toward a Maxwell-Boltzmann distribution as the "temperature" dial turns.
- The artifact: a Python script (~55 lines) using numpy that: (1) generates N=1000 particles with random initial velocities for three temperatures (300 K, 600 K, 1200 K), (2) computes the speed distribution for each, (3) plots it against the Maxwell-Boltzmann analytic curve f(v) = 4π (m/2πkT)^(3/2) v² exp(-mv²/2kT) for air (m = 4.8×10⁻²⁶ kg), (4) marks the mean, rms, and most-probable speeds on each distribution. Manim animates the histogram building up with the analytic curve overlaid, then temperature increasing and the distribution shifting right.
- Prompt seed: `claude "Write a Python script using numpy and matplotlib that: (1) for T in [300, 600, 1200] K and m=4.8e-26 kg (N2 molecule), generates N=2000 particle speeds from the Maxwell-Boltzmann distribution using numpy: speeds = np.sqrt(-2*k*T/m * np.log(np.random.uniform(0,1,N))) is NOT correct — use the correct method: speeds from chi distribution with df=3; (2) plots histograms and analytic MB curves f(v) = 4*pi*(m/(2*pi*k*T))^(3/2)*v^2*exp(-m*v^2/(2*k*T)); (3) marks v_mp, v_mean, v_rms for each temperature."`
- Read / check: Verify the Maxwell-Boltzmann sampling method is correct: speeds = χ(df=3) × √(kT/m) using scipy.stats.chi. Confirm v_rms = √(3kT/m) and v_mean = √(8kT/πm) for each temperature. Verify the analytic curve is properly normalized.
- Human supplies: Nothing — fully synthetic. Python with numpy, scipy, matplotlib.
- Output medium: Manim (three overlaid MB distributions for T=300/600/1200 K, building up simultaneously; speed markers (v_mp, v_mean, v_rms) animating in as vertical lines; annotation showing T doubles → v_rms scales as √T)
- The change: Change the molecule from N₂ to H₂ (4× lighter) at the same temperature and show the distribution shifts right by 2× — demonstrating the 1/√m scaling.
- Teardown angle: The Maxwell-Boltzmann distribution is not an assumption — it is the unique distribution that maximizes entropy subject to fixed total energy. The temperature you read on a thermometer is the mean of this distribution. Hot really is just fast.
- Exclusions: Quantum statistics (Fermi-Dirac, Bose-Einstein), non-equilibrium distributions.
- Score: 9/10

---

## Candidate 03 — Build the Orbital Mechanics Simulator: Newton's Cannon Orbits
- Source: physics/chapters/06-uniform-circular-motion-and-gravitation.md
- Lane: BUILD (Claude Code)
- Hook: Newton imagined a cannon on a mountain that fires a ball fast enough to orbit Earth. This script numerically integrates the orbit for any muzzle speed — showing circular orbit, elliptical orbit, parabolic escape, and hyperbolic flyby as one simulation.
- The artifact: a Python script (~50 lines) using numpy and scipy.integrate.solve_ivp that: (1) integrates Newton's gravity equations ẍ = -GM x/r³, ÿ = -GM y/r³ with Earth's parameters, (2) runs for four initial horizontal speeds: v₁ = 6000 m/s (suborbital arc), v₂ = 7910 m/s (circular orbit), v₃ = 10000 m/s (elliptical), v₄ = 11200 m/s (escape), (3) plots all four trajectories in a single frame with Earth as a circle. Manim animates each trajectory tracing out sequentially, then all four together.
- Prompt seed: `claude "Write a Python script using scipy.integrate.solve_ivp and matplotlib that numerically integrates the 2D gravitational orbit equations dx/dt=vx, dy/dt=vy, dvx/dt=-G*M*x/r^3, dvy/dt=-G*M*y/r^3 for G*M=3.986e14 m^3/s^2, starting at x0=6.371e6+100e3 (100 km altitude), y0=0, vy0=0 for 4 horizontal speeds vx0 in [6000, 7910, 10000, 11180] m/s. Integrate for t=0 to 5400 s. Plot all 4 trajectories, draw Earth as a filled circle of radius 6.371e6, label each trajectory."`
- Read / check: Verify circular orbit speed at r=6.471e6 m is v = √(GM/r) = √(3.986e14/6.471e6) ≈ 7850 m/s. Confirm escape speed at that altitude is v_esc = √(2GM/r) ≈ 11100 m/s. Check that the circular orbit closes (x,y returns near start after T ≈ 5400 s). Verify the solver uses RK45 or DOP853.
- Human supplies: Nothing — fully synthetic. Python with numpy, scipy, matplotlib.
- Output medium: Manim (Earth circle centered; four trajectories animate in sequence: arc falling back (red), closed circle (green), open ellipse (blue), escaping hyperbola (orange); labels and speed annotations appear with each)
- The change: Add a fifth trajectory at v = 7910 m/s but angled 5° upward from horizontal — showing the Keplerian precession of the ellipse over 10 orbits.
- Teardown angle: The orbit is just falling — continuously missing the ground. The circular orbit speed is the one muzzle velocity where the acceleration of free fall exactly matches the curvature of the Earth. Newton computed this with a telescope and a quill pen. The simulation does it in 30 lines.
- Exclusions: Atmospheric drag, multi-body orbits, relativistic corrections.
- Score: 10/10

---

## Candidate 04 — Build the Photoelectric Effect: Why Intensity Doesn't Matter
- Source: physics/chapters/29-quantum-physics.md
- Lane: BUILD (Claude Code)
- Hook: Double the intensity of light below the threshold frequency: still no electrons. Use dim light above the threshold: electrons fly out immediately. Einstein's 1905 explanation broke classical wave theory — and this script makes the prediction quantitative.
- The artifact: a Python script (~40 lines) using numpy and matplotlib that: (1) defines KE_max = hf - φ for three metals (sodium φ=2.36 eV, copper φ=4.7 eV, gold φ=5.1 eV), (2) plots KE_max vs frequency f for each metal, showing the threshold frequency f₀ = φ/h and the linear slope h above it, (3) shows that below f₀, KE_max = 0 regardless of intensity, (4) marks the visible light range and shows which metals respond to visible light. Manim animates the three lines sweeping up from their respective threshold frequencies.
- Prompt seed: `claude "Write a Python script using numpy and matplotlib that plots the photoelectric effect. For three metals: sodium (phi=2.36 eV), copper (phi=4.7 eV), gold (phi=5.1 eV): (1) plot KE_max = h*f - phi (in eV) vs frequency f from 0 to 2e15 Hz, clipping at 0 for f < phi/h; (2) mark the threshold frequency f0=phi/h for each metal with a vertical dashed line; (3) shade the visible light range 4e14 to 7e14 Hz; (4) label the slope as h=6.626e-34 J*s = 4.136e-15 eV*s on the sodium line. Use h=4.136e-15 eV*s."`
- Read / check: Verify threshold for sodium: f₀ = 2.36/(4.136e-15) ≈ 5.7×10¹⁴ Hz (visible light). Confirm copper threshold ~1.14×10¹⁵ Hz (UV). Verify lines have identical slope h regardless of metal — only the intercept (work function) differs. Confirm sodium responds to visible light; copper and gold do not.
- Human supplies: Nothing — fully synthetic. Python with numpy, matplotlib.
- Output medium: Manim (three colored lines animating in simultaneously, threshold verticals dropping at different points, visible light region shaded; annotation showing "same slope h for all metals — photon energy is hf")
- The change: Show a classical wave prediction (intensity determines KE, not frequency) as a dashed line and demonstrate where it fails — motivating the photon concept.
- Teardown angle: The photoelectric effect is not about whether light is a wave or a particle — light is both. It's about what determines the energy of individual electrons. The answer is frequency, not intensity. That answer requires quantization.
- Exclusions: Compton scattering, X-ray photoelectron spectroscopy, semiconductor photodetectors.
- Score: 9/10

---

## Candidate 05 — Build the Double-Slit Interference Pattern: From Single to Double to Many Slits
- Source: physics/chapters/27-wave-optics.md (anticipated chapter)
- Lane: BUILD (Claude Code)
- Hook: Young's 1801 experiment showed that light makes a striped pattern through two slits — and the only way to explain it is with wave interference. This script computes the pattern from 1 slit to 2 slits to a diffraction grating with 20 slits, showing how the pattern sharpens.
- The artifact: a Python script (~45 lines) using numpy that: (1) computes the single-slit diffraction pattern I(θ) = I₀ (sin(β/2)/(β/2))² where β = 2π a sin(θ)/λ, (2) multiplies by the double-slit interference factor cos²(π d sin(θ)/λ), (3) computes the N-slit grating pattern I(θ) = I₀ (sin(Nγ/2)/(N sin(γ/2)))², (4) plots all three on the same x-axis (y = screen coordinate) for λ = 500 nm, d = 10λ, a = 2λ, N = 1, 2, 20. Manim animates the patterns building up simultaneously with the fringe spacing and principal maximum labeled.
- Prompt seed: `claude "Write a Python script using numpy and matplotlib that computes and plots three interference patterns on a screen at L=1 m: (1) single slit: I = I0*(sin(pi*a*y/(lambda*L))/(pi*a*y/(lambda*L)))^2 with a=1e-6 m; (2) double slit: I = I0*cos(pi*d*y/(lambda*L))^2 * (sinc term)^2 with d=5e-6 m; (3) 20-slit grating: I = I0*(sin(N*pi*d*y/(lambda*L))/(N*sin(pi*d*y/(lambda*L))))^2 * (sinc)^2 with N=20. Use lambda=500e-9 m, y from -0.05 to 0.05 m. Plot all three on separate subplots with fringe spacing annotated."`
- Read / check: Verify fringe spacing for double slit: Δy = λL/d = 500e-9 * 1 / 5e-6 = 0.1 m — check this matches the plot. Confirm the 20-slit pattern shows 19 secondary maxima between each principal maximum. Verify single-slit central maximum is twice as wide as secondary maxima.
- Human supplies: Nothing — fully synthetic. Python with numpy, matplotlib.
- Output medium: Manim (three horizontally stacked intensity patterns, each building up left to right; labels mark fringe spacing, number of secondary maxima; color of the pattern matches λ = 500 nm green)
- The change: Vary the slit separation d from 5λ to 50λ and show the fringe pattern compressing — animating the inverse relationship between slit spacing and fringe spacing.
- Teardown angle: The grating is the double slit taken seriously as an engineering tool. The more slits, the sharper the principal maxima and the more precisely you can measure wavelength. The spectrometer in a chemistry lab is 20,000 slits. It works because of Young's 1801 experiment.
- Exclusions: X-ray diffraction, electron diffraction, near-field effects.
- Score: 8/10

---

## Candidate 06 — Build the Projectile Motion Analyzer: Where Does a Ball Land?
- Source: physics/chapters/03-two-dimensional-kinematics.md
- Lane: BUILD (Claude Code)
- Hook: Projectile motion is two kinematic equations running simultaneously. This script shows all possible landing positions for a ball thrown at any angle, finds the optimal angle for maximum range, and adds air resistance to show how the ideal parabola breaks down.
- The artifact: a Python script (~45 lines) using numpy that: (1) plots trajectories for launch angles θ = 15°, 30°, 45°, 60°, 75° with v₀ = 30 m/s, (2) connects the landing points to show the "envelope" parabola, (3) adds Stokes drag F = -bv and numerically integrates the trajectory for θ = 45°, comparing to the ideal (vacuum) case. Manim animates all vacuum trajectories appearing simultaneously, then the drag trajectory tracing separately.
- Prompt seed: `claude "Write a Python script using numpy that: (1) plots projectile trajectories for v0=30 m/s, g=9.8 m/s^2, angles=[15,30,45,60,75] degrees using parametric equations x=v0*cos(a)*t, y=v0*sin(a)*t-0.5*g*t^2 until y<0; (2) marks the landing points and draws the envelope parabola connecting them (the equation is y = H - x^2/(4H) where H = v0^2/(2g)); (3) for theta=45 deg, numerically integrates dx/dt=vx, dy/dt=vy, dvx/dt=-b*vx/m, dvy/dt=-g-b*vy/m with b/m=0.1 s^-1 using scipy.integrate.solve_ivp and overlays on the vacuum trajectory."`
- Read / check: Verify maximum range at θ = 45° is R = v₀²/g = 900/9.8 ≈ 91.8 m. Confirm the envelope parabola equation y = H - x²/(4H) passes through all landing points. Check that air resistance reduces range and shifts the optimal angle below 45°.
- Human supplies: Nothing — fully synthetic. Python with numpy, scipy.
- Output medium: Manim (five vacuum trajectories animate simultaneously; envelope parabola draws last; then air-resistance trajectory for 45° overlays on vacuum 45°, showing shortened range and steeper descent)
- The change: Find the optimal launch angle with air resistance numerically (scan over angles, find max range) and show it is less than 45° — quantifying how much drag shifts the optimum.
- Teardown angle: The 45° rule is exact only in vacuum. As soon as you add drag — a baseball, a soccer ball, a cannonball — the optimal angle drops. Artillery tables from the 1940s were empirical because the math was intractable. Now it's a 40-line script.
- Exclusions: Magnus effect (spinning balls), wind effects, 3D trajectories.
- Score: 8/10

---

## Candidate 07 — Build the PV Diagram Engine: Simulate Four Thermodynamic Cycles
- Source: physics/chapters/15-thermodynamics.md
- Lane: BUILD (Claude Code)
- Hook: Every heat engine follows a closed loop on the PV diagram. The area inside is the net work per cycle. This script draws and computes the efficiency of four famous cycles — Carnot, Otto (gasoline engine), Diesel, and Brayton (jet engine) — from first principles.
- The artifact: a Python script (~60 lines) using numpy and matplotlib that: (1) plots the PV diagram for Carnot (two isotherms + two adiabats), Otto (two isochors + two adiabats), Diesel (one isobar + two adiabats + one isochor), and Brayton (two isobars + two adiabats), (2) computes net work W = shaded area by numerical integration for each, (3) computes efficiency η = W/Q_in for each and prints a comparison table. Manim animates each cycle tracing clockwise, then the efficiency table appearing.
- Prompt seed: `claude "Write a Python script using numpy and scipy.integrate that: (1) plots four PV cycles for an ideal diatomic gas (gamma=7/5): Carnot (Th=600K, Tc=300K, V1=1L, V3=10L), Otto (r=8 compression ratio, V1=1L, Qin=1000J), Diesel (rc=2 cutoff ratio, r=18, V1=1L, Qin=1000J), Brayton (pressure ratio 10, T1=300K, Qin=1000J/mol); (2) numerically integrates P dV for each to get W_net; (3) computes eta=W/Qin; (4) prints a comparison table: cycle, W_net (J), Qin (J), eta (percent), Carnot limit (percent)."`
- Read / check: Verify Otto efficiency η = 1 - 1/r^(γ-1) = 1 - 1/8^0.4 ≈ 0.565 (56.5%). Confirm Carnot efficiency for same temperatures is higher. Check that net work = area under the expansion stroke minus area under compression stroke — verify sign is positive (net work out).
- Human supplies: Nothing — fully synthetic. Python with numpy, scipy, matplotlib.
- Output medium: Manim (four PV diagrams in a 2×2 grid, each cycle tracing clockwise with the enclosed area shading as it fills; efficiency values appearing in the table below each diagram)
- The change: Vary the compression ratio r from 4 to 16 for the Otto cycle and plot efficiency vs r — showing diminishing returns and why higher compression ratios are limited by fuel knock.
- Teardown angle: The PV diagram turns a thermodynamic cycle into geometry. The efficiency is the ratio of the shaded area to the heat input. Every real engine is an approximation of one of these cycles, and the gap between the approximation and Carnot is the engineering challenge of the last 200 years.
- Exclusions: Steam Rankine cycle, refrigeration, combined cycle plants.
- Score: 8/10

---

## Candidate 08 — Build the Standing Waves Simulator: Why Only Certain Frequencies Resonate
- Source: physics/chapters/16-oscillatory-motion-and-waves.md
- Lane: BUILD (Claude Code)
- Hook: A guitar string sounds the same note every time you pluck it because only certain frequencies — those where a whole number of half-wavelengths fit between the endpoints — form standing waves. This script shows why, and animates the first 5 harmonics.
- The artifact: a Python script (~40 lines) using numpy that: (1) plots the displacement u(x,t) = A sin(nπx/L) cos(2πf_n t) for n = 1,2,3,4,5 on a string of length L=1 m with v=50 m/s, (2) animates one full oscillation cycle for each harmonic at the correct frequency f_n = nv/2L, (3) plots the frequency spectrum showing the harmonic series f_n as vertical lines. Manim animates each standing wave mode appearing in sequence, then all five simultaneously, then the frequency spectrum below.
- Prompt seed: `claude "Write a Python script using numpy and matplotlib that: (1) defines u(x,t,n) = sin(n*pi*x/L)*cos(2*pi*n*v/(2*L)*t) for L=1 m, v=50 m/s, n=1..5; (2) creates a 5-panel figure showing one full oscillation of each harmonic (20 frames per cycle, use matplotlib.animation.FuncAnimation); (3) below the string plots, shows a frequency spectrum with vertical bars at f_n = n*v/(2L) for n=1..5, labeled with f1=25Hz, f2=50Hz etc. Use animate=False and just show snapshots at t=0, T/4, T/2 for each mode."`
- Read / check: Verify f₁ = v/2L = 50/2 = 25 Hz. Confirm f_n = n × 25 Hz (harmonic series). Check that n=1 has one antinode (one hump), n=2 has two antinodes (two humps). Verify nodes are at x = 0, L/n, 2L/n, ..., L for each mode.
- Human supplies: Nothing — fully synthetic. Python with numpy, matplotlib.
- Output medium: Manim (5 rows: each row shows one harmonic mode animating through one full oscillation cycle; below all rows, a frequency spectrum with 5 bars at f, 2f, 3f, 4f, 5f labeled; all five modes superimpose in the final beat)
- The change: Add a non-resonant frequency (37 Hz between f₁ and f₂) and show the pattern failing to form a standing wave — it's a traveling wave that doesn't fit the boundary conditions.
- Teardown angle: Resonance is a geometric constraint: the wavelength must divide evenly into the string length. That's why instruments have a fundamental pitch. The harmonics are what make a guitar sound like a guitar and not a sine wave.
- Exclusions: Quantum mechanical analogy (particle in a box), 2D drumhead modes, acoustic resonance.
- Score: 8/10

---

## Candidate 09 — Build the Special Relativity Time Dilation Calculator: GPS Needs It Every Day
- Source: physics/chapters/28-special-relativity.md
- Lane: BUILD (Claude Code)
- Hook: GPS satellites need both special and general relativistic corrections to stay accurate — without them, your phone's position would drift by 11 km per day. This script computes both corrections and shows which dominates.
- The artifact: a Python script (~40 lines) using scipy.constants and numpy that: (1) computes special relativistic time dilation for GPS orbit speed (v = 3874 m/s): Δt_SR = γ - 1 per second, satellite runs slow by 7.2 μs/day, (2) computes general relativistic gravitational blueshift for GPS altitude (h = 20,200 km): Δt_GR = gh/c² per second, satellite runs fast by 45.9 μs/day, (3) shows net correction = +38.4 μs/day (GR wins), (4) computes the position error without correction: 38.4 μs × c = 11.5 km/day. Manim animates a two-bar chart: SR effect (negative, satellite runs slow) and GR effect (positive, satellite runs fast).
- Prompt seed: `claude "Write a Python script using scipy.constants that computes relativistic corrections for GPS satellites. Parameters: orbital radius r=26560e3 m, v=3874 m/s, GM=3.986e14 m^3/s^2. (1) SR time dilation: gamma=1/sqrt(1-v^2/c^2), fractional rate change = -(gamma-1) = -v^2/(2c^2) (slow); (2) GR gravitational blueshift: fractional rate change = +GM/c^2*(1/Re - 1/r) (fast) where Re=6.371e6 m; (3) net fractional rate change; (4) multiply by seconds per day (86400) to get microseconds per day; (5) multiply by c to get position error in km per day without correction."`
- Read / check: Verify SR correction ≈ -7.2 μs/day. Verify GR correction ≈ +45.9 μs/day. Confirm net ≈ +38.4 μs/day (satellite clock runs fast). Verify position error: 38.4e-6 s × 3e8 m/s = 11.5 km/day.
- Human supplies: Nothing — fully synthetic. Python with scipy.constants.
- Output medium: Manim (two-bar chart: SR bar below zero (−7.2 μs/day, labeled "SR: satellite runs slow"), GR bar above zero (+45.9 μs/day, labeled "GR: satellite runs fast"), net bar showing +38.4 μs/day; position error consequence: 11.5 km/day animating as annotation)
- The change: Compute the same corrections for a hypothetical satellite at the Moon's distance — showing how each effect scales with altitude.
- Teardown angle: General relativity is not an exotic theory for black holes. It is the firmware running inside every GPS receiver. Without the GR correction, the civilian positioning system would be useless within hours.
- Exclusions: Twin paradox, length contraction, relativistic momentum.
- Score: 9/10

---

## Candidate 10 — Build the Conservation of Momentum Simulator: Elastic and Inelastic Collisions
- Source: physics/chapters/08-linear-momentum-and-collisions.md
- Lane: BUILD (Claude Code)
- Hook: Momentum is conserved in every collision. Kinetic energy is conserved only in elastic ones. This script computes both for any mass ratio and initial velocity, showing the range of outcomes and marking the elastic and perfectly inelastic limits.
- The artifact: a Python script (~45 lines) using numpy that: (1) for a 1D collision between m₁ = 1 kg (v₁ = 5 m/s) and m₂ at rest, plots final velocities v₁' and v₂' as a function of mass ratio m₂/m₁ from 0.1 to 10, (2) separately plots fractional kinetic energy retained KE_final/KE_initial vs mass ratio for elastic collision, (3) marks special cases: equal masses (m₁=m₂: full transfer), m₂>>m₁ (m₁ bounces back), perfectly inelastic (stick together: KE loss = ½m₁m₂v₁²/(m₁+m₂)). Manim animates curves tracing in and marks appearing.
- Prompt seed: `claude "Write a Python script using numpy and matplotlib that: (1) for elastic 1D collision m1=1 kg, v1=5 m/s, v2=0, mass_ratio=m2/m1 from 0.1 to 20: plots v1_final=(m1-m2)/(m1+m2)*v1 and v2_final=2*m1/(m1+m2)*v1 vs mass_ratio; (2) plots KE_final/KE_initial = (m1*(v1_final^2) + m2*(v2_final^2))/(m1*v1^2) — verify it equals 1 for elastic collision; (3) for perfectly inelastic (stick together): marks KE_retained=(m1/(m1+m2)) as a function of mass_ratio; (4) marks special cases at mass_ratio=1 (equal masses) with a vertical line labeled 'full transfer'."`
- Read / check: Verify v₁' = 0 and v₂' = v₁ when m₁ = m₂ (equal mass elastic: full transfer). Confirm KE_final/KE_initial = 1 for all elastic collisions. Verify perfectly inelastic KE retention = m₁/(m₁+m₂) approaches 0 as m₂→∞. Check that v₁' → -v₁ (full bounce) as m₂/m₁ → ∞.
- Human supplies: Nothing — fully synthetic. Python with numpy, matplotlib.
- Output medium: Manim (two-panel: left — v₁' and v₂' curves vs mass ratio, animated tracing; right — KE retention for elastic (flat at 1) and inelastic (decaying curve) vs mass ratio; equal-mass marker animating in)
- The change: Extend to 2D collision with an impact parameter and show how the angle of deflection depends on impact parameter — introducing the concept used in particle physics scattering.
- Teardown angle: Momentum conservation is inviolable. Kinetic energy conservation is the exception, not the rule. Every real collision is somewhere between elastic and perfectly inelastic — and the mass ratio tells you where most of the energy ends up.
- Exclusions: Relativistic collisions, particle physics cross-sections.
- Score: 8/10
