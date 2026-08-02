# Physics: Classical Mechanics — CLI Video Ideas ("X with Claude")

---

## Candidate 01 — Build the Figure Skater: Angular Momentum Conservation Visualized
- Source: physics-classical-mechanics/chapters/13-rotational-motion-and-angular-momentum.md
- Lane: BUILD (Claude Code)
- Hook: Yu-Na Kim pulls her arms in and spins 4× faster — without pushing against anything. Angular momentum conservation does all the work. This script makes it quantitative and animates the moment of inertia trading against angular velocity.
- The artifact: a Python script (~40 lines) using numpy that: (1) defines I_extended = 4 kg·m² (arms out), ω_extended = 1.5 rev/s, (2) sweeps the moment of inertia from I_extended down to I_tucked = 1 kg·m² as arms come in, (3) plots ω(I) = L/I (constant L) — showing ω rising from 1.5 to 6 rev/s, (4) plots rotational KE = ½Iω² = L²/2I rising as arms tuck — energy came from muscle work. Manim animates two simultaneous curves: ω rising and KE rising as I falls.
- Prompt seed: `claude "Write a Python script using numpy and matplotlib that: (1) defines L = I_ext * omega_ext = 4 * 1.5 * 2*pi = constant angular momentum (in SI, rad/s); (2) sweeps I from 4 to 1 kg*m^2; (3) plots omega(I) = L/I (in rev/s) and KE(I) = L^2/(2*I) on two vertically stacked subplots vs I; (4) marks the initial state (I=4, omega=1.5 rev/s) and final state (I=1, omega=6 rev/s) with dots; (5) annotates the KE increase as 'work done by muscles pulling arms in' — DeltaKE = KE_f - KE_i."`
- Read / check: Verify L = 4 × 1.5 × 2π ≈ 37.7 kg·m²/s. Confirm ω at I=1: ω = 37.7/1 ≈ 37.7 rad/s ≈ 6 rev/s. Verify KE_initial = ½ × 4 × (9.42)² ≈ 177 J and KE_final = ½ × 1 × (37.7)² ≈ 710 J — ΔKE ≈ 533 J of muscle work.
- Human supplies: Nothing — fully synthetic. Python with numpy, matplotlib.
- Output medium: Manim (two-panel, I on x-axis decreasing right to left: top — ω(I) curve rising; bottom — KE(I) curve rising; a moving dot sweeps from initial to final state on both curves simultaneously, trailing a path)
- The change: Add a third panel showing the work done per unit decrease in I — dW/dI = -L²/2I² — showing work goes as 1/I² and is hardest near the tucked position.
- Teardown angle: The skater didn't add energy from outside. She converted chemical energy (muscle work) into rotational kinetic energy — with angular momentum as the conserved thread connecting the two states. No torque required; just a change in mass distribution.
- Exclusions: Real biomechanical torques, precession and gyroscopic effects.
- Score: 9/10

---

## Candidate 02 — Build the K2 Skier: When Does Friction Save You on a 50° Slope?
- Source: physics-classical-mechanics/chapters/07-further-applications-of-newton-s-laws-friction-drag-and-elasticity.md
- Lane: BUILD (Claude Code)
- Hook: On a 50° slope, friction alone barely slows you — the calculation shows you'd still accelerate at 7.2 m/s². What actually saves a skier like Bargiel is turn geometry. This script shows the force balance for straight descent vs. carving, making the geometry concrete.
- The artifact: a Python script (~45 lines) using numpy that: (1) computes net acceleration on a 50° slope for μ_k from 0 to 0.5: a = g(sin50° - μ_k cos50°), (2) marks μ_snow ≈ 0.05 showing a ≈ 7.2 m/s² (friction barely helps), (3) for a carving turn: decomposes forces into along-fall-line and cross-fall-line components for a turn angle θ from 0° to 90°, showing effective deceleration from the cross-fall component, (4) plots speed after 5 seconds of straight descent vs. speed after 5 s with 60° carving turns. Manim animates the force vector decomposition rotating as the ski angle changes.
- Prompt seed: `claude "Write a Python script using numpy and matplotlib that: (1) plots net acceleration on a 50-degree slope vs kinetic friction coefficient mu: a = 9.8*(sin(50*pi/180) - mu*cos(50*pi/180)); mark mu=0.05 (ski on snow) and show a~7.2 m/s^2; (2) for a carving turn at angle phi (0=straight down, 90=traverse), compute the component of gravitational acceleration along the ski direction: a_eff = g*sin(50)*sin(phi) - mu_k*g*cos(50)*cos(phi); (3) plot speed v=a_eff*t at t=5s vs phi from 0 to 90 degrees; (4) mark phi_optimal that minimizes speed at t=5s."`
- Read / check: Verify at φ=0 (straight down): a ≈ 7.2 m/s², v(5s) ≈ 36 m/s (fast and dangerous). Confirm at φ=90° (full traverse): a ≈ −0.03 m/s² (nearly stops). Find the threshold φ where a_eff = 0 (gravity balanced by friction along traverse). Check that the formula for carving acceleration is geometrically correct.
- Human supplies: Nothing — fully synthetic. Python with numpy, matplotlib.
- Output medium: Manim (left panel: force vectors on slope — gravity (down), normal (perpendicular to slope), friction (up the slope); ski direction rotates as φ increases; right panel: speed at t=5s curve vs φ, minimum marked)
- The change: Add Stokes drag (aerodynamic, F = -bv) and show how air resistance changes the speed curve at very high v — relevant for downhill racing speeds.
- Teardown angle: Friction is necessary but not sufficient to control descent on K2. Turn geometry is what converts the kinetic energy of descent into lateral momentum — the physics of skiing is the physics of redirecting vectors, not of braking.
- Exclusions: Mogul dynamics, ski flex, snow deformation.
- Score: 8/10

---

## Candidate 03 — Build the Momentum Transfer Calculator: All Collisions, One Script
- Source: physics-classical-mechanics/chapters/10-linear-momentum-and-collisions.md (chapter 10 — "Linear Momentum")
- Lane: BUILD (Claude Code)
- Hook: Elastic collisions, perfectly inelastic collisions, and everything in between — the coefficient of restitution e interpolates between them. This script computes final velocities and energy loss for any e, mass ratio, and initial speeds.
- The artifact: a Python script (~45 lines) using numpy that: (1) implements the general 1D collision formula: v₁' = (m₁-e·m₂)v₁ + (1+e)m₂v₂)/(m₁+m₂), v₂' = ((1+e)m₁v₁ + (m₂-e·m₁)v₂)/(m₁+m₂), (2) sweeps e from 0 (perfectly inelastic) to 1 (elastic) for m₁=1 kg, m₂=3 kg, v₁=4 m/s, v₂=0, (3) plots v₁', v₂', and energy loss ΔKE/KE₀ vs e, (4) marks the elastic (e=1) and inelastic (e=0) limits. Manim animates three curves simultaneously.
- Prompt seed: `claude "Write a Python script using numpy and matplotlib that: (1) defines general 1D collision with coefficient of restitution e: v1_final = ((m1 - e*m2)*v1 + (1+e)*m2*v2)/(m1+m2), v2_final = ((1+e)*m1*v1 + (m2-e*m1)*v2)/(m1+m2); (2) for m1=1, m2=3, v1=4, v2=0, sweeps e from 0 to 1 in 100 steps; (3) plots v1_final, v2_final, and energy_loss_fraction = (KE_initial - KE_final)/KE_initial vs e on three stacked subplots; (4) marks e=0 (perfectly inelastic) and e=1 (elastic) with vertical lines."`
- Read / check: Verify at e=1 (elastic): v₁' = (1-3)·4/(1+3) = -2 m/s, v₂' = 2·1·4/4 = 2 m/s, energy loss = 0. Verify at e=0 (perfectly inelastic): v' = m₁v₁/(m₁+m₂) = 4/4 = 1 m/s for both, energy loss = ΔKE/KE₀ = 1 - m₁/(m₁+m₂) = 0.75. Check formula derivation: Newton's restitution condition e = -(v₁'-v₂')/(v₁-v₂).
- Human supplies: Nothing — fully synthetic. Python with numpy, matplotlib.
- Output medium: Manim (three stacked panels, all with e on x-axis 0→1: top — v₁' and v₂' curves; middle — ΔKE/KE₀ curve from 0.75 to 0; bottom — a schematic of the collision for e=0, 0.5, 1; all animating simultaneously)
- The change: Add a 2D collision with impact parameter b and show how e and b together determine the scattering angle — connecting classical mechanics to the Rutherford scattering formula.
- Teardown angle: The coefficient of restitution is the single number that interpolates between the two idealized limits — and in engineering, virtually every collision sits between them. Car crash analysis uses e ≈ 0.1; billiard balls use e ≈ 0.95. The formula quantifies what "partially elastic" means.
- Exclusions: Oblique collisions in 3D, relativistic collisions.
- Score: 8/10

---

## Candidate 04 — Build the Orbital Mechanics: Kepler's Three Laws from Newton's Gravity
- Source: physics-classical-mechanics/chapters/08-uniform-circular-motion-and-gravitation.md (chapter 8 — circular motion)
- Lane: BUILD (Claude Code)
- Hook: Kepler extracted his three laws from 20 years of Tycho Brahe's data. Newton derived all three from his inverse-square law in a few pages. This script numerically verifies all three Kepler laws from simulated orbital data.
- The artifact: a Python script (~60 lines) using scipy.integrate.solve_ivp and numpy that: (1) integrates the 2D gravitational orbit for three elliptical orbits with different semi-major axes a = 1, 4, 9 AU (Earth, Mars-like, Jupiter-like), (2) extracts orbital period T from the simulation, (3) verifies Kepler's third law: T² ∝ a³, (4) sweeps out equal areas in equal times (Kepler's second law) by computing area swept per unit time at perihelion vs. aphelion. Manim animates three orbits simultaneously with area-sweep shading.
- Prompt seed: `claude "Write a Python script using scipy.integrate.solve_ivp that: (1) integrates three elliptical orbits in 2D with GM=4*pi^2 AU^3/yr^2 (Earth units), semi-major axes a=[1,4,9] AU, eccentricity e=0.3, initial conditions from vis-viva: v_perihelion=sqrt(GM*(2/r_peri - 1/a)); (2) extracts orbital period T from the simulation by timing when y crosses 0 twice; (3) verifies T^2 proportional to a^3 by printing T^2/a^3 for each orbit; (4) computes the area swept per unit time at 3 points (perihelion, semi-major, aphelion) and shows it is constant."`
- Read / check: Verify T² ∝ a³ holds to within 1% for all three orbits. Confirm area swept per unit time is constant across perihelion, semi-latus rectum, and aphelion. Check vis-viva initial speed v_peri = √(GM(2/r_peri - 1/a)) is correctly computed. Verify GM = 4π² gives T=1 year for a=1 AU.
- Human supplies: Nothing — fully synthetic. Python with numpy, scipy.
- Output medium: Manim (three elliptical orbits animating simultaneously; small planets sweeping around each; area triangles shading equal areas at perihelion and aphelion — equal shaded area, different time sweeps; T² vs a³ table appearing)
- The change: Add a precessing orbit (Schwarzschild correction to Newton: add a small -GML²/r³ term) and show Mercury-like perihelion precession — where Newtonian mechanics fails.
- Teardown angle: Kepler's laws are not independent discoveries. They are all consequences of one equation — Newton's inverse-square gravity — plus energy and angular momentum conservation. The simulation extracts all three from numerical trajectories, showing that the laws are embedded in the dynamics.
- Exclusions: N-body chaos, tidal forces, relativistic precession corrections beyond Mercury.
- Score: 9/10

---

## Candidate 05 — Build the Free-Fall Analyzer: Apollo 15 Hammer-and-Feather in Numbers
- Source: physics-classical-mechanics/chapters/03-kinematics.md
- Lane: BUILD (Claude Code)
- Hook: David Scott dropped a hammer (1.32 kg) and a feather (0.03 kg) on the Moon simultaneously. They hit at the same time — 1.4 seconds later. This script predicts the exact time, plots both trajectories, and shows why mass doesn't matter.
- The artifact: a Python script (~35 lines) using numpy that: (1) computes y(t) = y₀ - ½ g_moon t² for g_moon = 1.62 m/s², y₀ = 1.5 m (drop height from hands to ground), (2) finds the time of impact: t = √(2y₀/g) = √(2×1.5/1.62) ≈ 1.36 s, (3) plots y(t) for both masses (identical trajectories — proving independence from mass), (4) marks g_moon vs g_earth with a comparison bar. Manim animates both masses falling as overlapping curves with a countdown timer.
- Prompt seed: `claude "Write a Python script using numpy and matplotlib that: (1) computes the free-fall trajectory y(t) = 1.5 - 0.5*1.62*t^2 (Moon, g=1.62 m/s^2) from t=0 to t=2 s; (2) finds the impact time t_impact = sqrt(2*1.5/1.62) and prints it; (3) plots y vs t for both the hammer (1.32 kg) and feather (0.03 kg) — they are identical; (4) on a second subplot shows the same fall on Earth (g=9.8, no drag) — also identical; (5) adds a text annotation: 'Mass does not appear in y(t) = y0 - gt^2/2'."`
- Read / check: Verify t_impact = √(3.0/1.62) ≈ 1.36 s. Confirm on Earth without drag: same time √(3.0/9.8) ≈ 0.55 s for both masses. Verify the trajectory equation contains no mass term — the cancellation of m from F=ma and F=mg is explicit.
- Human supplies: Nothing — fully synthetic. Python with numpy, matplotlib.
- Output medium: Manim (two panels: left — Moon drop: hammer and feather as two superimposed dots falling on the same y(t) curve, countdown to impact; right — Earth drop: same two dots, faster; annotation "mass cancels from F=ma and F=mg")
- The change: Add air resistance on Earth (F_drag = ½ρCdAv² with different cross-sections for hammer and feather) and show the feather falling much slower — demonstrating why the demo only works in vacuum.
- Teardown angle: Galileo argued that all objects fall at the same rate in a thought experiment. Astronaut Scott proved it in 1971 on live television. The mathematics had been correct for 300 years before the vacuum conditions existed to confirm it without equivocation.
- Exclusions: Relativistic gravity, tidal forces, rotation effects.
- Score: 8/10

---

## Candidate 06 — Build the Fluid Dynamics Simulator: Reynolds Number and the Transition to Turbulence
- Source: physics-classical-mechanics/chapters/15-fluid-dynamics-and-its-biological-and-medical-applications.md
- Lane: BUILD (Claude Code)
- Hook: Flow through a pipe is smooth (laminar) until the Reynolds number hits ~2300 — then it turns chaotic. The same equation predicts the flight of a golf ball and blood flow in an artery. This script computes Re for a range of real-world scenarios and plots the laminar-turbulent transition.
- The artifact: a Python script (~40 lines) using numpy and scipy.constants that: (1) computes Re = ρvD/μ for 6 real scenarios (blood in aorta, blood in capillary, water in garden hose, air over a car, flow in a river, oil in a pipeline), (2) plots all on a log-scale Re axis with colored regions: Re<2300 (green, laminar) and Re>4000 (red, turbulent), (3) for pipe flow: plots pressure drop ΔP vs flow rate Q for Hagen-Poiseuille (laminar) and turbulent drag laws. Manim animates the Re markers appearing on the axis with their flow regime labeled.
- Prompt seed: `claude "Write a Python script using numpy and matplotlib that: (1) defines 6 fluid scenarios with rho, v, D, mu: (a) blood in aorta: rho=1060, v=0.4, D=0.025, mu=0.003; (b) blood in capillary: v=0.001, D=0.00001, mu=0.003; (c) water in garden hose: rho=1000, v=1, D=0.019, mu=0.001; (d) air over car: rho=1.2, v=30, D=2, mu=1.8e-5; (e) river: rho=1000, v=1, D=5, mu=0.001; (f) oil pipeline: rho=850, v=1, D=0.5, mu=0.1; (2) computes Re=rho*v*D/mu for each; (3) plots on log10(Re) axis with laminar/transition/turbulent zones shaded; (4) labels each scenario."`
- Read / check: Verify blood in aorta Re ≈ 1060×0.4×0.025/0.003 ≈ 3533 (near transition — correct!). Confirm blood in capillary Re ≈ 0.35 (deeply laminar — correct). Check air over car Re ≈ 4×10⁶ (turbulent — correct). Verify oil pipeline Re ≈ 4250 (just turbulent — interesting case).
- Human supplies: Nothing — fully synthetic. Python with numpy, matplotlib.
- Output medium: Manim (horizontal log-scale Re axis; three color zones (laminar/transition/turbulent) shading in; 6 labeled markers appearing at their computed Re values; pulse animation for blood scenarios)
- The change: Animate a cross-section of pipe flow switching from Poiseuille laminar (parabolic velocity profile) to turbulent (flatter profile) as Re crosses 2300 — showing the velocity field change.
- Teardown angle: The Reynolds number is not a number — it is a ratio of inertial to viscous forces that determines whether a flow is orderly or chaotic. The same dimensionless group governs a hummingbird's wing and a tanker's hull. Dimensional analysis is physics' most powerful compression tool.
- Exclusions: Navier-Stokes derivation, turbulence modeling, chaos theory of fluids.
- Score: 8/10

---

## Candidate 07 — Build the Simple Harmonic Oscillator Zoo: Spring, Pendulum, LC Circuit, CO2 Vibration
- Source: physics-classical-mechanics/chapters/18-oscillatory-motion-and-waves.md
- Lane: BUILD (Claude Code)
- Hook: A spring, a pendulum, an LC circuit, and a vibrating CO₂ molecule are all governed by the same equation: ẍ = -ω²x. This script computes ω for each, shows the shared mathematical structure, and animates all four oscillating in phase.
- The artifact: a Python script (~45 lines) using numpy and scipy.constants that: (1) computes ω for spring (k=100 N/m, m=1 kg → ω=10 rad/s), pendulum (L=1 m, g=9.8 → ω=3.13), LC circuit (L=0.01 H, C=10 μF → ω=3162), CO₂ symmetric stretch (k_eff=1900 N/m, μ=reduced mass → ω≈2×10¹³), (2) normalizes all to phase plots, (3) plots x(t) = A cos(ωt) for all four on the same normalized time axis (0 to 2π). Manim animates all four oscillating simultaneously with the equation ẍ = -ω²x displayed.
- Prompt seed: `claude "Write a Python script using numpy, scipy.constants, and matplotlib that computes omega for four SHM systems: (1) spring: omega=sqrt(100/1); (2) pendulum: omega=sqrt(9.8/1); (3) LC circuit: omega=1/sqrt(0.01*10e-6); (4) CO2 symmetric stretch: k_eff=1900 N/m, reduced_mass=m_O*m_C/(2*m_O+m_C) with m_O=16*1.66e-27, m_C=12*1.66e-27, omega=sqrt(k_eff/reduced_mass); print all omega values with units; plot x(t)=cos(omega*t) for each on a shared normalized axis tau = omega*t from 0 to 4*pi."`
- Read / check: Verify ω_spring = 10 rad/s, ω_pendulum = √9.8 ≈ 3.13 rad/s, ω_LC = 1/√(10⁻⁴) = 100 rad/s (check: L=0.01, C=10e-6 → ω=1/√(10e-8) ≈ 3162 rad/s). Verify CO₂ reduced mass and ω is in the infrared (∼10¹³ rad/s). Confirm all four plots are identical cosine waves when plotted vs. τ = ωt.
- Human supplies: Nothing — fully synthetic. Python with numpy, scipy.constants.
- Output medium: Manim (four oscillators shown: spring-mass diagram, pendulum, LC circuit schematic, CO₂ molecule; all four x(t) curves animate together on the same normalized axis; annotation "same equation, different ω")
- The change: Add damping (ẍ + 2γẋ + ω²x = 0) for one system and show critical damping (γ=ω), overdamping, and underdamping on one plot — the three regimes of the damped oscillator.
- Teardown angle: SHM is the universal small-oscillation approximation. Any potential with a minimum acts like a spring near that minimum — Taylor expand to second order and you get ẍ = -ω²x. The CO₂ vibration and the pendulum are the same math at 13 orders of magnitude difference in frequency.
- Exclusions: Chaotic oscillators, anharmonic corrections, quantum harmonic oscillator.
- Score: 9/10

---

## Candidate 08 — Build the Drag Racer: Terminal Velocity and the Quadratic Drag Equation
- Source: physics-classical-mechanics/chapters/07-further-applications-of-newton-s-laws-friction-drag-and-elasticity.md
- Lane: BUILD (Claude Code)
- Hook: A skydiver reaches 56 m/s in free fall and then stops accelerating. A raindrop reaches 9 m/s. A baseball reaches 42 m/s. This script computes terminal velocity for any object and integrates the trajectory to show the approach to terminal — including the exponential tail.
- The artifact: a Python script (~40 lines) using numpy and scipy.integrate.solve_ivp that: (1) integrates dv/dt = g - (ρ Cd A/2m) v² for a skydiver (m=80 kg, A=0.7 m², Cd=1.0, ρ=1.2 kg/m³), (2) computes v_terminal = √(2mg/ρCdA), (3) plots v(t) for 0 to 30 s, showing the approach to v_t, (4) computes the exact solution v(t) = v_t tanh(gt/v_t) and overlays it on the numerical solution. Manim animates the velocity curve approaching the terminal asymptote.
- Prompt seed: `claude "Write a Python script using scipy.integrate.solve_ivp and numpy that: (1) computes terminal velocity v_t=sqrt(2*m*g/(rho*Cd*A)) for skydiver: m=80, g=9.8, rho=1.2, Cd=1.0, A=0.7; (2) integrates dv/dt = g - g/v_t^2 * v^2 from t=0 to t=30 s using solve_ivp; (3) plots numerical v(t) vs exact solution v_t*tanh(g*t/v_t); (4) adds a horizontal dashed line at v_t labeled 'terminal velocity = {v_t:.1f} m/s'; (5) also plots the case with no drag (v=g*t) for comparison."`
- Read / check: Verify v_t = √(2×80×9.8/(1.2×1.0×0.7)) ≈ 43 m/s for the skydiver (close to the 56 m/s for a tucked vs. spread-eagle position — the A differs). Confirm the exact tanh solution matches the numerical integration to within 1%. Check that without drag, v = gt = 294 m/s at t=30 s (far above terminal).
- Human supplies: Nothing — fully synthetic. Python with scipy, numpy.
- Output medium: Manim (velocity vs time: no-drag line (dashed, rising steeply), exact solution (solid, approaching v_t), numerical solution (dots on the exact line); terminal velocity dashed horizontal animating in; annotation showing time to reach 99% of terminal)
- The change: Compare three objects side by side: skydiver (43 m/s), baseball (42 m/s), raindrop (9 m/s) — showing how A/m ratio determines terminal velocity, not mass alone.
- Teardown angle: Terminal velocity is where gravity and drag balance exactly. The approach is always an exponential decay toward the terminal — but for large objects in dense air, it happens quickly. The tanh solution is one of the rare closed-form results in a nonlinear ODE.
- Exclusions: Stokes drag for small Re (linear drag, v not v²), compressibility effects.
- Score: 8/10
