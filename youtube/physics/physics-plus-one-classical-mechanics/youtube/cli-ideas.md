# Physics +1: Classical Mechanics — CLI Video Ideas ("X with Claude")

## Candidate 01 — Simulate Projectile Motion with Air Resistance with Claude

- Source: physics-plus-one-classical-mechanics/chapters/03-kinematics.md
- Lane: BUILD (Claude Code)
- Hook: Every textbook plots the parabola with no air resistance. But a baseball in real air travels 40% shorter than that parabola predicts — and the optimal launch angle drops from 45° to ~35°. Build both trajectories and measure the gap.
- The artifact: A D3 animation of two projectile trajectories on the same axes: the ideal parabola (no drag) and the numerically integrated trajectory with quadratic air drag F_drag = −(1/2)ρC_dAv²v̂. Sliders for launch angle (0°–90°), initial speed (10–100 m/s), drag coefficient (0 to 0.5), and projectile type (baseball, soccer ball, cannonball — preset C_d and A values). The range, maximum height, and time of flight display for both. An angle sweep animates the range-vs-angle curve for both cases, marking the true optimal angle.
- Prompt seed: `claude "Build a D3 v7 single-file HTML projectile motion simulator with and without air drag. Use Euler/RK4 integration with Δt=0.01s. Drag force: F_drag = -(1/2)·ρ·Cd·A·v²·v_hat. Sliders: v₀ (10–100 m/s), θ (0–90°), Cd (0–0.5), A (area 0.01–0.2 m²). Preset buttons: baseball (m=0.145kg, A=0.0042m², Cd=0.47), soccer ball, cannonball. Show two trajectories (no-drag parabola and drag trajectory). Range comparison readout. Verify: baseball at v₀=50m/s, θ=45°, no drag: range = v₀²sin(2θ)/g = 255m."`
- Read / check: No-drag range = v₀²sin(2θ)/g. At v₀=50 m/s, θ=45°: R = 2500×1/9.81 = 254.8 m. With drag (baseball, C_d=0.47, A=0.0042 m², m=0.145 kg, ρ=1.225 kg/m³): range ≈ 155–165 m (drag parameter b/m = ½ρC_dA/m ≈ 0.108 m⁻¹, giving significant drag). Optimal angle with drag: ~35° rather than 45°.
- Human supplies: Nothing — fully synthetic. RK4 integration in pure JavaScript.
- Output medium: d3 (animated, single HTML file)
- The change: Add the Magnus effect: a spinning baseball curves. Add a spin slider (rpm) and compute the Magnus force F_M = C_M × v × ω × r̂. Show the curved trajectory — the curveball — and compare to a fastball with no spin.
- Teardown angle: The 45° optimal angle assumes no drag. With drag, the optimal angle is lower because you're trading height (time in air) for horizontal range, and drag penalizes horizontal speed more than it penalizes vertical height. The textbook result is the special case, not the rule.
- Exclusions: Wind effects, variable density with altitude, shock waves at supersonic speeds.
- Score: 9/10

---

## Candidate 02 — Build a Two-Body Orbital Mechanics Simulator with Claude

- Source: physics-plus-one-classical-mechanics/chapters/08-uniform-circular-motion-and-gravitation.md
- Lane: BUILD (Claude Code)
- Hook: Newton proved that an inverse-square force produces elliptical orbits. Keplers three laws follow from F = GMm/r² and nothing else. Watch an orbit precess when you add a tiny extra force — and see why Mercury's orbit betrayed Newtonian gravity.
- The artifact: A D3 animation of a two-body orbital system: a planet orbiting a star, with the star at one focus of the ellipse. The position is computed by RK4 integration of ẍ = −GM/r³ × x. Sliders for: initial position (x₀), initial velocity (v_y₀, controlling eccentricity), and a small perturbation force (r⁻³ term) that produces orbital precession. The orbit trace draws over multiple periods; a perihelion marker shows the precessing perihelion direction. Kepler's second law is verified by shading equal-area wedges at different orbital phases.
- Prompt seed: `claude "Build a D3 v7 single-file HTML two-body orbital mechanics simulator. Integrate ẍ = -GM/r³·x using RK4, Δt=0.001 years. Sliders: semi-major axis a (0.5–3 AU), eccentricity e (0–0.9), perturbation ε (adds -ε·GM/r⁴ extra force). Animate: (1) orbit trace building over 5 periods with current position dot, (2) perihelion direction arrow showing precession, (3) equal-area shading demonstrating Kepler's 2nd law. Display: period T, eccentricity e, perihelion shift per orbit (degrees). Verify: e=0 → circle; e=0.5 → clear ellipse; ε=0 → no precession."`
- Read / check: Kepler's third law: T² = 4π²a³/(GM). At a=1 AU: T=1 year. At a=2 AU: T=2.83 years. For ε=0, orbit should close exactly (no precession). For ε>0: perihelion advances each orbit — analog of GR correction for Mercury (GR gives 43 arcsec/century). Kepler 2nd law: area swept per unit time should be constant → verify numerically.
- Human supplies: Nothing — fully synthetic. RK4 integration of the two-body problem.
- Output medium: d3 (animated, single HTML file)
- The change: Add the Hohmann transfer orbit: the viewer selects a starting orbit and a target orbit; Claude computes the two burn ΔV magnitudes and animates the spacecraft transferring between orbits with the two burns marked.
- Teardown angle: Kepler's laws are not independent laws — they are consequences of Newton's inverse-square gravity. The ellipse arises because any central inverse-square force has a conserved Laplace-Runge-Lenz vector. Add any perturbation and the orbit precesses.
- Exclusions: Three-body problem chaos, Lagrange points full derivation, general relativistic corrections beyond the perturbative approach.
- Score: 9/10

---

## Candidate 03 — Simulate a 1D Elastic Collision and Verify Momentum-Energy Conservation with Claude

- Source: physics-plus-one-classical-mechanics/chapters/10-linear-momentum-and-collisions.md
- Lane: BUILD (Claude Code)
- Hook: Newton's cradle works because momentum and kinetic energy are both conserved — and the only solution to those two equations for equal masses is that all the momentum transfers completely. Build a multi-ball collision simulator and watch the conservation laws enforce the outcome.
- The artifact: A D3 animation of N balls on a line (N slider: 2–8) that collide elastically. Each collision is resolved using the 1D elastic collision formulas v₁' = (m₁−m₂)v₁/(m₁+m₂) + 2m₂v₂/(m₁+m₂) (and symmetric for v₂'). Mass sliders for each ball. A live readout shows total momentum p_total and total kinetic energy KE_total at each frame — both should be constant. A special "Newton's cradle" preset sets equal masses and shows the one-in/one-out behavior.
- Prompt seed: `claude "Build a D3 v7 single-file HTML elastic collision simulator. N balls (slider 2–8) on a horizontal track. Sliders: individual masses (0.5–5 kg), initial velocities. Elastic collision detection and resolution using center-of-mass frame formulas. Live display: (1) momentum bars for each ball (colored, signed), (2) KE bars, (3) total p and total KE — both with green 'CONSERVED' indicator when change < 0.01%. Newton's cradle preset. Verify: 2 equal masses, v2=0 → after collision v1=0, v2=v1_initial."`
- Read / check: For m₁=m₂=m: v₁' = 0, v₂' = v₁ (masses swap velocities). For m₁=2m, m₂=m at rest: v₁' = (2m−m)v₁/(3m) = v₁/3, v₂' = 2(2m)v₁/(3m) = 4v₁/3. Verify KE_before = KE_after. Total momentum: p_before = m₁v₁ = p_after = m₁v₁' + m₂v₂'. Newton's cradle: N=5 equal balls, 1 swings in → 1 swings out, 2 in → 2 out.
- Human supplies: Nothing — fully synthetic. Elastic collision formula is analytic.
- Output medium: d3 (animated, single HTML file)
- The change: Add an inelasticity coefficient e (0=perfectly inelastic, 1=elastic): v_rel_after = −e × v_rel_before. Show how kinetic energy is "lost" (converted to heat/deformation) as e decreases from 1 to 0, while momentum is still conserved throughout.
- Teardown angle: The equal-mass velocity-swap is not magic — it is the only solution to two equations (momentum conservation and energy conservation) in two unknowns. The Newton's cradle result is forced by the math, not by "knowing about" the number of balls.
- Exclusions: 2D/3D collision geometry, impact parameter, glancing collisions.
- Score: 8/10

---

## Candidate 04 — Animate a Rotating Rigid Body and Demonstrate Conservation of Angular Momentum with Claude

- Source: physics-plus-one-classical-mechanics/chapters/13-rotational-motion-and-angular-momentum.md
- Lane: BUILD (Claude Code)
- Hook: When a spinning figure skater pulls in their arms, they spin faster — and the product Iω stays constant. Build the simulation and measure: is the angular momentum actually conserved, or is this just an approximation that textbooks round off?
- The artifact: A D3 animation of a figure skater (simplified as a bar with two masses at the ends): a torso (fixed mass, fixed radius) and two arms (masses at variable radius, controlled by a slider). The moment of inertia I = I_torso + 2m_arm×r² is computed live. As r decreases (arms pulled in), the angular velocity ω = L/I increases. A live readout shows L = Iω (constant, verified), KE = ½Iω² (not constant — energy is added by the skater doing work), and ω(t) animating.
- Prompt seed: `claude "Build a D3 v7 single-file HTML angular momentum conservation simulator. Model: a rotating 'skater' = central disk (I_body = 2 kg·m²) + two arms (m_arm = 2 kg each at radius r, slider 0.2–1.5 m). Initial ω₀ = 1 rad/s with arms extended. Animate: (1) rotating body with arms animating as r changes, (2) live I = I_body + 2·m_arm·r², ω = L₀/I (L₀ = I_initial·ω₀), KE = ½·I·ω², L = I·ω. Show L CONSERVED indicator (green), KE rising as arms pulled in. Verify: arms in at r=0.2m → ω = L₀/I_new (higher than ω₀)."`
- Read / check: L₀ = (2 + 2×2×1.5²)×1 = (2 + 9)×1 = 11 kg·m²/s. With arms at r=0.2m: I_new = 2 + 2×2×0.04 = 2.16 kg·m²/s. ω_new = 11/2.16 = 5.09 rad/s. KE_initial = ½×11×1 = 5.5 J. KE_new = ½×2.16×5.09² = 28 J. Angular momentum should read 11 kg·m²/s throughout — verify within numerical precision.
- Human supplies: Nothing — fully synthetic.
- Output medium: d3 (animated, single HTML file)
- The change: Add gyroscopic precession: apply a small torque to a spinning wheel and show the precession direction Ω_prec = τ/L (perpendicular to both L and τ). The wheel precesses instead of falling — animate this counterintuitive result.
- Teardown angle: The skater gains kinetic energy not by magic but by doing work against the centrifugal force as the arms are pulled in. Angular momentum is the conserved quantity; kinetic energy is not — and the gap tells you exactly how much muscular work was done.
- Exclusions: Euler's equations for asymmetric tops, nutation, Euler angles.
- Score: 8/10

---

## Candidate 05 — Simulate Simple Harmonic Motion and the Mass-Spring System with Claude

- Source: physics-plus-one-classical-mechanics/chapters/18-oscillatory-motion-and-waves.md
- Lane: BUILD (Claude Code)
- Hook: The same equation — ẍ + ω²x = 0 — describes a mass on a spring, the motion of a pendulum for small angles, an LC circuit, a sound wave in a pipe, and the quantum harmonic oscillator. Build the mass-spring and measure: does the period really not depend on amplitude?
- The artifact: A D3 animation of a mass on a spring: the spring (drawn as a zigzag extending from a fixed wall), a mass block animated at position x(t) = A cos(ωt + φ). Sliders for mass m, spring constant k, amplitude A, and damping coefficient b. The phase portrait (ẋ vs. x) draws as a spiral (underdamped) or ellipse (undamped). Live readouts: ω = √(k/m), period T = 2π/ω, total energy E = ½kA² (conserved for b=0). A second panel plots x(t) and ẋ(t) vs. time.
- Prompt seed: `claude "Build a D3 v7 single-file HTML mass-spring oscillator simulation. Integrate ẍ = -ω²x - 2βẋ (where ω²=k/m, β=b/(2m)) using RK4. Sliders: m (0.1–5 kg), k (1–100 N/m), A (0.01–1 m), b (0–5 N·s/m). Animate: (1) spring-mass diagram with spring drawing, (2) phase portrait ẋ vs. x (ellipse for b=0, inward spiral for b>0), (3) time series x(t). Display: ω, T, total energy E = ½mv²+½kx². Verify: b=0 → E conserved; T independent of A (SHM)."`
- Read / check: ω = √(k/m). At k=10 N/m, m=1 kg: ω=3.162 rad/s, T=1.987 s. Change A from 0.1 to 0.5 m — T should remain 1.987 s (SHM amplitude independence). For b>0 (damping): phase portrait spirals inward; energy decays exponentially. Verify energy E = ½mv² + ½kx² oscillates between KE and PE but is constant for b=0.
- Human supplies: Nothing — fully synthetic.
- Output medium: d3 (animated, single HTML file)
- The change: Add resonance: drive the oscillator with F(t) = F₀cos(ωt) and sweep the driving frequency. Plot amplitude response A(ω_drive) — the resonance curve peaks at ω₀ = √(k/m) and narrows as damping decreases. This is the mechanism behind MRI, radio tuning, and earthquake-building coupling.
- Teardown angle: The amplitude independence of period is not obvious from the equation — it is a consequence of the restoring force being exactly proportional to displacement (Hooke's law). Any deviation from linearity (a nonlinear spring) breaks this, and you get amplitude-dependent frequencies (the anharmonic oscillator).
- Exclusions: Nonlinear pendulum (large amplitude), chaos via the driven Duffing oscillator (save for a dedicated card), normal modes of coupled oscillators.
- Score: 8/10

---

## Candidate 06 — Simulate Wave Interference and Standing Waves with Claude

- Source: physics-plus-one-classical-mechanics/chapters/16-waves-and-their-properties.md
- Lane: BUILD (Claude Code)
- Hook: Standing waves are not waves that stopped — they are two traveling waves moving in opposite directions, and their superposition creates nodes that never move. A guitar string sounds A4 at 440 Hz because the string length is exactly half a wavelength. Build the simulation and find the resonant frequencies.
- The artifact: A D3 animation showing two traveling waves (rightward and leftward) and their superposition. Sliders for frequency f, amplitude A, and wave speed v. The standing wave nodes and antinodes are highlighted. A second panel shows a "string" of fixed length L with a frequency slider: the simulation shows which frequencies produce standing waves (f_n = nv/2L) and which produce a mess — only the resonant frequencies produce stable nodes.
- Prompt seed: `claude "Build a D3 v7 single-file HTML standing wave simulator. Panel 1: two traveling waves y1=A·sin(kx-ωt) and y2=A·sin(kx+ωt); show y1 (orange), y2 (blue), superposition y=y1+y2 (white) animating in time. Sliders: f (1–10 Hz), A, v (1–20 m/s). Panel 2: string (length L=1m, fixed ends) with frequency slider — compute n = 2L·f/v; if n is integer, draw the nth standing wave mode; otherwise draw chaotic interference. Display: nodes, antinodes, resonant frequencies f_n = n·v/(2L). Verify: f=5Hz, v=10m/s, L=1m → n=1, resonant."`
- Read / check: Superposition: y = 2A sin(kx) cos(ωt) — the standing wave formula. Nodes at kx = nπ → x = nλ/2. First harmonic (n=1): f₁ = v/(2L) = 10/(2×1) = 5 Hz. Second harmonic: f₂ = 10 Hz. Non-resonant frequency (say f=7 Hz): k=2π×7/10 = 4.4 rad/m; 2L×f/v = 2×1×7/10 = 1.4 → non-integer → no stable nodes, chaotic pattern.
- Human supplies: Nothing — fully synthetic.
- Output medium: d3 (animated, single HTML file)
- The change: Add a "listening" panel: model a microphone at a fixed x position and plot its output (pressure vs. time). Show that at resonant frequencies you hear a pure tone; at non-resonant frequencies you hear beats. This connects the wave physics to audible sound.
- Teardown angle: A guitar string doesn't just vibrate at one frequency — it vibrates at all the harmonics simultaneously. What you perceive as the "tone" is the fundamental; the harmonics are what give different instruments different timbre for the same note.
- Exclusions: 2D drumhead modes, Chladni figures, nonlinear string theory.
- Score: 8/10

---

## Candidate 07 — Model Newton's Law of Cooling and Thermal Equilibration with Claude

- Source: physics-plus-one-classical-mechanics/chapters/07-further-applications-of-newton-s-laws-friction-drag-and-elasticity.md
- Lane: BUILD (Claude Code)
- Hook: Newton's law of cooling says dT/dt = −k(T−T_env). That's the same equation as radioactive decay — but it describes your coffee cooling, not a nucleus decaying. Measure k by timing how fast a cup of coffee cools to room temperature — and check whether Newton was right.
- The artifact: A D3 animation with a "coffee cup" that cools from an initial temperature T₀ (slider: 50–100°C) to room temperature T_env (slider: 15–30°C). The exponential cooling curve T(t) = T_env + (T₀−T_env)e^(−kt) animates. A second panel plots ln(T−T_env) vs. t — which should be a straight line with slope −k. A "measurement" mode lets the viewer click on the curve at two points and compute k from the two-point formula. The half-time (how long to go halfway to equilibrium) is displayed.
- Prompt seed: `claude "Build a D3 v7 single-file HTML Newton's Law of Cooling simulator. Animate T(t) = T_env + (T₀-T_env)·exp(-k·t). Sliders: T₀ (50–100°C), T_env (10–30°C), k (0.01–0.1 min⁻¹). Panel 1: T vs. t curve (minutes 0–120). Panel 2: ln(T-T_env) vs. t (should be linear, slope = -k). 'Measurement' mode: click two points on panel 1 to compute k_measured = ln(ΔT₁/ΔT₂)/(t₂-t₁). Display half-time τ = ln2/k. Verify: at k=0.05/min, T₀=90°C, T_env=20°C → τ = 13.86 min."`
- Read / check: τ = ln(2)/k = 0.693/0.05 = 13.86 min. At t=τ: T = 20 + (90−20)×e^(−0.05×13.86) = 20 + 70×0.5 = 55°C. Log-plot slope: slope = −0.05 per min, exactly. Two-point measurement: k = [ln((T₁-T_env)/(T₂-T_env))]/(t₂-t₁) — verify within 1% of true k.
- Human supplies: Nothing — fully synthetic. Optional: the viewer can plug in their own real coffee-cooling measurements to estimate k.
- Output medium: d3 (animated, single HTML file)
- The change: Add Newton's law of heating: the same equation applies when T₀ < T_env (the cup is cold, room is warm). Show the symmetric heating curve, verify the same k governs both — this is the principle behind Peltier cooling elements and heat exchangers.
- Teardown angle: Newton's law of cooling is the simplest first-order ODE. Every differential equation with this form — exponential approach to equilibrium — from pharmacokinetics to RC circuits to radioactive decay — has the same mathematical solution. Learning one is learning all.
- Exclusions: Radiative cooling (T⁴ law), multi-layer thermal resistance (Fourier law), phase transitions (latent heat).
- Score: 7/10

---

## Candidate 08 — Simulate Fluid Flow with Bernoulli's Principle with Claude

- Source: physics-plus-one-classical-mechanics/chapters/15-fluid-dynamics-and-its-biological-and-medical-applications.md
- Lane: BUILD (Claude Code)
- Hook: A wing generates lift not because air goes faster over the top — that's wrong — but because the pressure above a wing is lower than the pressure below. Bernoulli's equation quantifies exactly how much lower, and it's the same equation that explains why a curveball curves, why a shower curtain blows inward, and why tall buildings sway.
- The artifact: A D3 animation of fluid flowing through a pipe of variable cross-section. The pipe narrows in the middle (Venturi tube geometry), controlled by a "throat radius" slider. The flow velocity at each position is computed from continuity (Av = const), and the pressure from Bernoulli (P + ½ρv² = const). Color-coded pressure visualization shows low pressure at the constriction. Streamlines animate through the pipe. A pressure gauge animates at three positions (inlet, throat, outlet).
- Prompt seed: `claude "Build a D3 v7 single-file HTML Bernoulli simulator. Show a horizontal pipe with variable cross-section: radius r1 (inlet) slider, r2 (throat, r2 < r1) slider. Flow velocity: v2 = v1·(r1/r2)². Pressure: P2 = P1 + ½ρ(v1²-v2²). Animate streamlines (pathlines) compressing at throat. Color pipe interior by pressure (blue=high, red=low). Show animated pressure gauges at inlet, throat, outlet. Sliders: r1 (5–20 cm), r2 (1–15 cm), v1 (1–10 m/s), fluid density ρ (1000 kg/m³ for water). Verify: r1=10cm, r2=5cm, v1=2m/s → v2=8m/s, ΔP=30kPa."`
- Read / check: Continuity: v2 = v1(r1/r2)² = 2×(10/5)² = 2×4 = 8 m/s. Bernoulli: P1−P2 = ½ρ(v2²−v1²) = ½×1000×(64−4) = 30,000 Pa = 30 kPa. This is substantial — 0.3 atm. Verify conservation of mass: π×r1²×v1 = π×r2²×v2, i.e., 100×2 = 25×8 = 200 cm³/s per unit depth.
- Human supplies: Nothing — fully synthetic. Inviscid, incompressible flow with steady streamlines.
- Output medium: d3 (animated, single HTML file)
- The change: Add a second configuration: a wing cross-section (airfoil). Use the computed pressure distribution from a NACA profile (approximate with a parabolic camber line) and integrate to get the lift force per unit span. Compare to the Kutta-Joukowski theorem result.
- Teardown angle: Bernoulli's equation is energy conservation for a fluid element — the kinetic energy term ½ρv² and the pressure term P are the fluid equivalent of KE and PE. Where the fluid speeds up, it must drop in pressure, because the total energy per unit volume is constant along a streamline.
- Exclusions: Viscous flow (Navier-Stokes), turbulence, compressible effects (shock waves).
- Score: 7/10

---

## Candidate 09 — Build a Gravity Simulator: N-Body System with Claude

- Source: physics-plus-one-classical-mechanics/chapters/08-uniform-circular-motion-and-gravitation.md
- Lane: BUILD (Claude Code)
- Hook: Two bodies under gravity trace perfect ellipses. Three bodies — the three-body problem — is chaotic: small changes in initial conditions produce completely different orbits. Build a 3-body simulator and watch the orbits diverge from a tiny perturbation.
- The artifact: A D3 animation of an N-body gravitational system (N = 2–5 bodies, slider). Each body's position is integrated using RK4 with F = GM₁M₂/r² between each pair. The orbit traces draw in colored trails. A "perturb" button applies a tiny velocity kick (0.1%) to one body and shows the subsequent trajectory in a different color — demonstrating sensitive dependence on initial conditions for N≥3. A "figure-8" preset shows the famous stable 3-body solution.
- Prompt seed: `claude "Build a D3 v7 single-file HTML N-body gravitational simulator (N=2 to 5). RK4 integration, softened potential F = GM₁M₂/(r²+ε²) to avoid singularities. Sliders: N (2–5), masses, G (tune for display). Draw colored orbit trails. Perturb button: apply 0.001 fractional kick to body 1's velocity, redraw diverging trajectory in dashed line. Preset: 'figure-8' (Chenciner-Montgomery 3-body solution, equal masses, specific initial conditions). Verify: 2-body → stable ellipse; 3+ body → chaotic divergence with perturbation."`
- Read / check: 2-body: should produce a stable ellipse, period T = 2π√(a³/GM_total) by Kepler. 3-body (non-special): perturbed trajectory should diverge from unperturbed on a Lyapunov timescale. Figure-8: initial conditions from Chenciner & Montgomery (2000): m=1, positions and velocities exactly as published (embed them). The figure-8 is periodic with period T = 6.326 in normalized units.
- Human supplies: Nothing — fully synthetic. Initial conditions for the figure-8 solution are published.
- Output medium: d3 (animated, single HTML file)
- The change: Add a "Lagrange points" mode for the 2-body case: place a test particle at each of the 5 Lagrange points and show which are stable (L4, L5) and which are unstable (L1, L2, L3) by perturbing the particle and watching it drift or oscillate.
- Teardown angle: The two-body problem is exactly solvable because it reduces to a one-body problem in the center-of-mass frame. The three-body problem cannot be reduced further — there are too few constants of motion to constrain the trajectories, so chaos is generic. The integrable exceptions (like the figure-8) are rare islands in a chaotic sea.
- Exclusions: Poincaré sections and KAM theory, Lyapunov exponent numerical computation, restricted 3-body problem (Jacobi constant).
- Score: 7/10

---

## Candidate 10 — Simulate Sound Wave Interference and the Doppler Effect with Claude

- Source: physics-plus-one-classical-mechanics/chapters/17-sound.md
- Lane: BUILD (Claude Code)
- Hook: A siren at 500 Hz sounds higher as the ambulance approaches and lower as it leaves — by an amount that tells you exactly how fast it's going. The Doppler formula is Newtonian mechanics applied to wave sources, and with two sirens you can make a beat frequency that slowly sweeps as they pass.
- The artifact: A D3 animation showing two panels: (1) a moving source (ambulance) emitting circular wavefronts, with wavefronts compressed in the direction of motion and expanded behind it — the observer hears f' = f₀(v_sound/(v_sound − v_source)) in front. Speed slider (0–340 m/s) animates the wavefront compression up to and past Mach 1. (2) A frequency readout f_observed vs. observer position. Beat frequency when two nearby-frequency sources are present.
- Prompt seed: `claude "Build a D3 v7 single-file HTML Doppler effect simulator. Panel 1: animate circular sound wavefronts emitted by a moving source (v_source slider 0–400 m/s, v_sound=343 m/s). Show wavefronts compressing ahead (Mach cone at v≥v_sound). Stationary observer at left: display f_observed = f₀·v/(v-v_s) (approaching) and f₀·v/(v+v_s) (receding). Panel 2: two sources at f1=440Hz and f2=443Hz, both stationary; plot superposed waveform showing beats at f_beat=3Hz. Verify: source at v=171.5m/s → f_observed_front = 2f₀."`
- Read / check: f_obs (approaching) = f₀ × v_sound/(v_sound − v_source). At v_source = v_sound/2 = 171.5 m/s: f_obs = f₀ × 343/(343-171.5) = f₀ × 2. At v_source = 343 m/s (Mach 1): f_obs → ∞ (Mach cone forms). Beat frequency: two sinusoids at 440 Hz and 443 Hz → beat frequency = 3 Hz (period 333 ms). Verify the wavefront animation compresses correctly.
- Human supplies: Nothing — fully synthetic. Circular wavefront geometry analytic.
- Output medium: d3 (animated, single HTML file)
- The change: Add the relativistic Doppler effect (for light): f_obs = f₀√((1+β)/(1−β)) for recession (β=v/c). Show the difference between classical and relativistic Doppler at v=0.5c — the relativistic transverse Doppler (pure time dilation) has no classical analog.
- Teardown angle: The Doppler effect is not about the sound "changing" — the source frequency is fixed. The observed frequency shifts because the wavefronts are compressed or stretched between source and observer. At Mach 1, wavefronts pile up into a shock — the sonic boom is not loud because the source is loud, but because all the wavefronts arrive simultaneously.
- Exclusions: Shock wave structure (Rankine-Hugoniot conditions), sonic boom carpet calculation, acoustic impedance matching.
- Score: 7/10
