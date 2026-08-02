# University Physics Bundle with LLMs — CLI Video Ideas ("X with Claude")

## Candidate 01 — Build a Unit-Conversion Verifier: Never Lose a Spacecraft Again with Claude

- Source: university-physics-bundle-with-llms/chapters/02-units-and-measurement.md
- Lane: BUILD (Claude Code)
- Hook: The Mars Climate Orbiter burned up in 1999 because one module reported pound-force-seconds while the rest of the system expected newton-seconds. A $325M spacecraft died from a missing multiply-by-4.45. Build a dimensional analysis checker that would have caught it in 5 lines.
- The artifact: A Manim animation of a unit-conversion graph: nodes are unit families (force, momentum, energy), edges are conversion factors, and a path-finding algorithm traces the shortest conversion route from lbf·s to N·s — with the factor 4.45 annotated on the edge, and the Mars Climate Orbiter loss ticker shown in the corner.
- Prompt seed: `claude "Build a dimensional analysis and unit conversion verifier in Python. Define the SI base units (kg, m, s, A, K, mol, cd) and common derived units (N, J, Pa, W). For any expression with mixed units, compute the conversion factor to pure SI and flag mismatches. Demo with the Mars Climate Orbiter case: lbf·s vs N·s. Show the conversion graph with networkx and matplotlib."`
- Read / check: Verify the conversion factor 1 lbf = 4.44822 N is correctly applied. Check that the tool correctly identifies lbf·s and N·s as momentum units (force × time). Confirm the graph correctly links pound-force to newtons via the 4.44822 factor.
- Human supplies: Nothing — fully synthetic. The Mars Climate Orbiter case uses well-documented public facts. No proprietary data.
- Output medium: Manim (unit conversion graph animation: nodes appear, edges draw with conversion factors labeled, MCO case path highlighted in red with the spacecraft loss annotated)
- The change: Extend to dimensional analysis checking for arbitrary physics equations — verify that F = ma is dimensionally consistent by checking [kg][m/s²] = [N], and flag any equation where left and right side dimensions don't match.
- Teardown angle: The error wasn't arithmetic — it was architectural. A unit-verification layer in the software interface would have raised a type mismatch before any spacecraft maneuvering. Type safety for physical quantities is the lesson.
- Exclusions: Skip the full SI base unit redefinition history (2019 Planck constant), skip significant figures, skip the Kibble balance explanation.
- Score: 9/10

---

## Candidate 02 — Simulate Newton's Second Law: Falcon 9 Landing with Claude

- Source: university-physics-bundle-with-llms/chapters/06-newton-s-laws-of-motion.md
- Lane: BUILD (Claude Code)
- Hook: The Falcon 9 first stage falls at 235 m/s and needs to touch down at 1.5 m/s. The center engine fires not to stop the fall — but to control it. Build the numerical simulation of the landing burn and watch Newton's second law execute in real time.
- The artifact: A Manim animation of the Falcon 9 landing burn: a vertical timeline showing altitude vs. time, with thrust and gravity force vectors drawn as arrows whose lengths update at 10 Hz (as the real computer does), velocity curve drawing from 235 m/s to 1.5 m/s, and the net force arrow shrinking as the rocket decelerates.
- Prompt seed: `claude "Simulate the SpaceX Falcon 9 first-stage landing burn using Newton's second law. Given: mass ≈ 30,000 kg (first stage empty), gravity = 9.81 m/s², Merlin engine thrust ≈ 340,000 N (throttled), initial velocity = 235 m/s downward, target landing velocity = 1.5 m/s. Use Euler integration at dt=0.1s to simulate the burn. Plot altitude vs. time, velocity vs. time, and net force vs. time. Show how the engine throttle must be reduced as the rocket slows to avoid overshooting."`
- Read / check: Verify the net force calculation includes both gravity (downward) and thrust (upward). Check that the simulation reaches near-zero velocity before altitude goes negative. Confirm the throttle must be reduced (not increased) during the final phase to prevent bouncing.
- Human supplies: Nothing — fully synthetic simulation. SpaceX has published general figures for Merlin engine thrust and Falcon 9 mass that are publicly documented.
- Output medium: Manim (dual-panel animation: left = altitude timeline with rocket icon falling, right = force vector diagram updating at each timestep; velocity annotation changes color from red to green as landing threshold approaches)
- The change: Add drag force (F_drag = ½ρv²C_d A) and show how the simulation changes when air resistance is included — the terminal velocity now limits the unburned fall phase, and less fuel is needed for the landing burn.
- Teardown angle: The Falcon 9 computer adjusts throttle 10 times per second because the correct throttle changes continuously as velocity changes. Discrete-time Euler integration captures exactly why constant thrust produces overshoot — the design lesson is real-time feedback.
- Exclusions: Skip the guidance algorithm (3-burn sequence), skip fuel mass depletion during the burn, skip the landing leg deployment mechanics.
- Score: 9/10

---

## Candidate 03 — Build an Energy Conservation Analyzer for Roller Coasters with Claude

- Source: university-physics-bundle-with-llms/chapters/09-potential-energy-and-conservation-of-energy.md
- Lane: BUILD (Claude Code)
- Hook: A roller coaster that starts at 45 meters and drops to ground level: what's the speed at the bottom? With energy conservation, you don't need to solve any differential equations. You just need the bookkeeping rule. Build a calculator that does the bookkeeping for any coaster profile.
- The artifact: A Manim animation of a roller coaster profile (configurable hill heights), with gravitational PE and KE bars growing and shrinking as the cart moves along the track — total mechanical energy shown as a constant horizontal line, the two bars always summing to it. Speed is computed at each point from E_total - U(h) = KE = ½mv².
- Prompt seed: `claude "Build a roller coaster energy conservation analyzer in Python. Given a coaster height profile (list of (x, height) points), compute gravitational PE = mgh and KE = E_total - PE at each point (assuming no friction), then compute speed v = sqrt(2*KE/m). Plot the height profile, PE bar, KE bar, and total energy as a function of position. Demo with a coaster that starts at 45m, drops to 0m, climbs to 40m, and drops again."`
- Read / check: Verify KE is always positive (no negative heights relative to reference). Check that speed at the second hill (40m) is slower than at ground level as required by energy conservation. Confirm total energy is constant (within floating-point precision) at every point.
- Human supplies: Nothing — fully synthetic. The height profile is user-specified.
- Output medium: Manim (animated coaster profile: cart icon moves along track, PE and KE bars animate below, total energy line stays flat; speed annotation updates at each point)
- The change: Add friction: introduce a frictional energy loss proportional to track length traveled (E_loss = μ × mg × distance). Watch the total energy bar gradually drop and the second hill become unreachable if friction is large enough.
- Teardown angle: Energy conservation turns a hard dynamics problem (integrate F=ma along a curved track) into a bookkeeping problem (compare heights). The power of the conservation law is that you bypass the complicated forces entirely.
- Exclusions: Skip the derivation of the work-energy theorem, skip spring potential energy, skip rotational kinetic energy for the coaster wheels.
- Score: 8/10

---

## Candidate 04 — Build a Significant Figures and Measurement Uncertainty Propagator with Claude

- Source: university-physics-bundle-with-llms/chapters/02-units-and-measurement.md
- Lane: BUILD (Claude Code)
- Hook: You measure a table as 1.23 m long and 0.456 m wide. What's the area? The calculator says 0.56088 m² — but that's five significant figures from two-and-three sig-fig inputs. Build a calculator that propagates uncertainty correctly and shows why the extra digits are lies.
- The artifact: A Manim animation showing two measured quantities with their uncertainty ranges, the arithmetic operation (multiplication), and the resulting uncertainty propagation — with the "false precision" digits highlighted in red and the significant figures rule annotated.
- Prompt seed: `claude "Build a significant figures and uncertainty propagation calculator in Python. Given two measurements with uncertainties (e.g., L = 1.23 ± 0.01 m, W = 0.456 ± 0.002 m), propagate the uncertainty through multiplication (A = L × W) using the fractional uncertainty addition rule: δA/A = sqrt((δL/L)² + (δW/W)²). Show the result with the correct number of significant figures and flag any digits beyond the uncertainty as 'false precision'."`
- Read / check: Verify the fractional uncertainty formula is the quadrature rule (not simple addition). Check that the result is rounded to the correct number of significant figures (determined by the larger fractional uncertainty). Confirm the "false precision" flag correctly identifies the digits beyond the uncertainty.
- Human supplies: Nothing — fully synthetic. The measurement values and uncertainties are user-specified.
- Output medium: Manim (two input measurement bars with uncertainty ranges shown as error bars, multiplication result bar with full precision shown then truncated to correct sig figs, false-precision digits lighting up red)
- The change: Extend to a chain of three measurements combined in a formula (e.g., density = mass / volume = mass / (L × W × H)) — show how uncertainty compounds through each operation and how the final result has fewer reliable digits than the inputs.
- Teardown angle: False precision is not just aesthetically wrong — it implies a level of measurement accuracy that doesn't exist. Significant figures are the honest accounting of what the instrument actually knows.
- Exclusions: Skip the statistical definition of standard deviation and its role in uncertainty, skip systematic vs. random error distinction in depth.
- Score: 8/10

---

## Candidate 05 — Build a Free-Body Diagram Generator and Net Force Solver with Claude

- Source: university-physics-bundle-with-llms/chapters/06-newton-s-laws-of-motion.md
- Lane: BUILD (Claude Code)
- Hook: Every Newton's second law problem starts with a free-body diagram. Build a tool that takes a plain-language description of a physical situation and outputs the correct FBD with labeled force vectors — then solves for the net force and acceleration automatically.
- The artifact: A Manim animation of a free-body diagram building itself: a box on an inclined plane, gravity vector pointing down, normal force perpendicular to the slope, friction force parallel to the slope — each force appearing with its calculated magnitude and the vector sum arrow appearing last with the net force annotated.
- Prompt seed: `claude "Build a free-body diagram generator and Newton's second law solver in Python. Given: a mass m on a frictionless inclined plane at angle θ, identify all forces (weight mg downward, normal force perpendicular to surface), resolve each into x and y components along the incline coordinate system, compute the net force along the incline, and solve for acceleration a = F_net / m. Draw the FBD using matplotlib with labeled force arrows."`
- Read / check: Verify the normal force is perpendicular to the incline surface (not vertical). Check that the weight component along the incline is mg sin(θ) (not mg cos(θ)). Confirm the net force arrow points down the incline for a frictionless surface.
- Human supplies: Nothing — fully synthetic. Mass and angle are user-specified.
- Output medium: Manim (FBD animation: inclined surface appears, block placed, then each force arrow draws in sequence with label and magnitude, net force arrow appears last, acceleration solved and annotated)
- The change: Add friction (f = μN) and show how the FBD changes — the friction arrow appears pointing up the incline, the net force reduces, and the acceleration decreases as μ increases from 0 to tan(θ) (the no-slip condition).
- Teardown angle: The FBD is the physics contract: once you've drawn all the forces correctly, the algebra is just arithmetic. The discipline is identifying and labeling every force before writing F = ma.
- Exclusions: Skip pulleys and multi-body systems for this card, skip torque and rotational dynamics, skip tension in ropes.
- Score: 8/10

---

## Candidate 06 — Simulate Projectile Motion with Drag and Measure the Golf Ball Effect with Claude

- Source: university-physics-bundle-with-llms/chapters/05-motion-in-two-and-three-dimensions.md
- Lane: BUILD (Claude Code)
- Hook: A golf ball without dimples travels about 130 yards. With dimples it travels 270 yards. The difference is turbulent vs. laminar airflow — a 45% drag reduction from surface texture. Build the simulation and measure the range improvement.
- The artifact: A Manim animation of two projectile trajectories side by side: smooth ball (high drag coefficient C_d ≈ 0.47) and dimpled ball (C_d ≈ 0.25) — both launched at 45° at 70 m/s, trajectories curving with drag, landing points annotated with range and the ratio between them.
- Prompt seed: `claude "Simulate projectile motion with aerodynamic drag in Python. For a golf ball launched at 70 m/s at 45°, simulate two cases: (1) smooth sphere with C_d = 0.47, diameter = 0.0427 m, mass = 0.0459 kg, air density = 1.225 kg/m³; (2) dimpled ball with C_d = 0.25. Use Euler integration with dt = 0.01s. Plot both trajectories and compute the range for each. Show the drag force vector at each timestep."`
- Read / check: Verify drag force formula is F_drag = ½ρv²C_d A (where A = πr²). Check that both simulations start from the same initial conditions. Confirm the dimpled ball range is approximately twice the smooth ball range (matching documented golf physics).
- Human supplies: Nothing — fully synthetic. Golf ball parameters are publicly documented physical facts.
- Output medium: Manim (dual-trajectory animation: both paths drawing simultaneously, drag force arrows visible at each step, landing markers with range annotation)
- The change: Vary launch angle from 10° to 80° for both ball types and plot range as a function of angle — show that the optimal angle for the dimpled ball is closer to 45° while the smooth ball's optimum shifts due to drag asymmetry.
- Teardown angle: The dimple texture doesn't reduce drag to zero — it changes the flow regime from laminar to turbulent, which counterintuitively reduces the pressure drag. Physics rewards counter-intuitive designs.
- Exclusions: Skip the Magnus effect (backspin / topspin), skip the full fluid dynamics derivation of the drag coefficient, skip altitude effects on air density.
- Score: 8/10

---

## Candidate 07 — Build a Momentum Conservation Lab: Elastic vs. Inelastic Collisions with Claude

- Source: university-physics-bundle-with-llms/chapters/10-linear-momentum-and-collisions.md
- Lane: BUILD (Claude Code)
- Hook: In a perfectly elastic collision, both momentum AND kinetic energy are conserved. In a perfectly inelastic collision, only momentum is — the objects stick together and KE is "lost." Build a collision simulator that measures both conserved quantities and shows exactly where the energy goes.
- The artifact: A Manim animation of a 1D collision: two masses approaching, colliding, and separating (or sticking), with momentum bars and KE bars for each object shown before and after — total momentum bar staying constant, total KE bar dropping for inelastic collisions with a "heat generated" annotation.
- Prompt seed: `claude "Build a 1D collision simulator in Python. Given two masses m1, m2 and initial velocities v1, v2, compute post-collision velocities for: (1) perfectly elastic collision (use both momentum and KE conservation equations); (2) perfectly inelastic collision (objects stick, use only momentum conservation). For each case, compute and display: total momentum before/after, total KE before/after, energy 'lost' as heat in the inelastic case. Animate the collision with matplotlib."`
- Read / check: Verify the elastic collision formulas (v1' = (m1-m2)v1/(m1+m2) + 2m2v2/(m1+m2)) are correctly implemented. Check that momentum is conserved in both cases (within floating-point precision). Confirm KE loss in the inelastic case is positive (not negative) — energy is lost, not gained.
- Human supplies: Nothing — fully synthetic. Masses and velocities are user-specified.
- Output medium: Manim (1D collision animation: two blocks approaching, collision flash, separation or sticking; momentum and KE bars animate; heat annotation appears for inelastic case)
- The change: Add a coefficient of restitution e (0 = perfectly inelastic, 1 = perfectly elastic) and simulate partially inelastic collisions — show how KE loss scales smoothly with e and identify the e value that corresponds to a real rubber ball collision.
- Teardown angle: Energy is never destroyed — it changes form. The KE "lost" in an inelastic collision reappears as heat, sound, and deformation. The conservation law is always satisfied; the trick is accounting for all the channels.
- Exclusions: Skip 2D collision kinematics, skip center-of-mass reference frame, skip collisions with walls.
- Score: 8/10

---

## Candidate 08 — Build a Gravitational Orbit Simulator with Kepler's Laws with Claude

- Source: university-physics-bundle-with-llms/chapters/14-gravitation.md
- Lane: BUILD (Claude Code)
- Hook: Kepler's third law says orbital period squared is proportional to semi-major axis cubed. Newton derived it from gravity. Build a numerical orbit simulator and verify Kepler's law holds — then watch what happens when you set Earth's tangential velocity to escape speed.
- The artifact: A Manim animation of a planet orbiting the Sun: the orbit path drawing in real time from numerical integration of Newton's gravitational force, with Kepler's third law verified in an annotation (T² vs. a³ ratio computed live), and a second orbit shown for a different semi-major axis confirming the same ratio.
- Prompt seed: `claude "Build a gravitational orbit simulator in Python using Newton's law of gravitation. Given masses M_sun = 2e30 kg, m_planet = 6e24 kg, Newton's G = 6.674e-11, and initial position and velocity for a circular orbit at 1 AU (Earth orbit), integrate the equations of motion using Euler or RK4, compute the orbital period, and verify Kepler's third law: T² ∝ a³. Then set the tangential velocity to v_escape = sqrt(2GM/r) and show the orbit becomes a parabola."`
- Read / check: Verify the circular orbit initial velocity is v = sqrt(GM/r). Check that the orbital period matches Earth's year (≈365 days) within 5%. Confirm the escape-speed trajectory is open (not closed). Verify Kepler's T²/a³ ratio is the same for two different orbits.
- Human supplies: Nothing — fully synthetic. All values are well-documented physical constants.
- Output medium: Manim (orbital animation: planet tracing its orbit, period and semi-major axis computed live, Kepler ratio annotated; second panel shows escape trajectory opening outward)
- The change: Simulate a Hohmann transfer orbit — the most fuel-efficient way to transfer between two circular orbits — by firing a brief tangential impulse and watching the orbit elongate from a circle to an ellipse to the target circle.
- Teardown angle: Kepler's laws are not postulates — Newton derived them from F = GMm/r². The simulation makes the derivation visible: the same gravity law that drops an apple produces the ellipses Kepler measured with a naked eye.
- Exclusions: Skip multi-body gravitational interactions, skip relativistic corrections, skip Lagrange points.
- Score: 8/10

---

## Candidate 09 — Build a Harmonic Oscillator: Springs, Pendulums, and the Math That Unifies Them with Claude

- Source: university-physics-bundle-with-llms/chapters/17-oscillations.md
- Lane: BUILD (Claude Code)
- Hook: A mass on a spring and a pendulum are different physical systems — but they obey the same differential equation. Build both simulators and overlay their phase portraits to show why angular frequency ω = sqrt(k/m) for one and sqrt(g/L) for the other are the same mathematical structure.
- The artifact: A Manim dual-panel animation: left = mass on spring oscillating, right = pendulum swinging, with position-vs-time plots drawn beneath each. A third panel shows both phase portraits (position vs. velocity) overlaid — both are ellipses, confirming the same underlying SHM equation.
- Prompt seed: `claude "Build a simple harmonic oscillator simulator in Python. Implement two systems: (1) mass-spring oscillator with m=1 kg, k=10 N/m, initial displacement x0=0.1 m; (2) simple pendulum with L=1 m, small angle approximation, initial angle θ0=0.1 rad. Integrate both using RK4. Plot position vs. time for each, and overlay their phase portraits (position vs. velocity) on a single axes. Compute and compare the angular frequencies for both."`
- Read / check: Verify ω = sqrt(k/m) for the spring and ω = sqrt(g/L) for the pendulum are correctly computed. Check that the phase portraits are ellipses (not circles — they're ellipses unless normalized). Confirm the period T = 2π/ω for both systems matches the numerical period from the simulation.
- Human supplies: Nothing — fully synthetic. All parameters are user-specified.
- Output medium: Manim (dual-panel animation: spring mass bouncing + pendulum swinging simultaneously, position curves drawing below, phase portraits appearing in a third panel as both traces draw together)
- The change: Break the small-angle approximation for the pendulum — set θ0 = 1.0 rad instead of 0.1 rad and show how the phase portrait deforms from an ellipse toward the separatrix, with the period becoming amplitude-dependent (no longer simple harmonic).
- Teardown angle: Simple harmonic motion is not just a model for springs — it's the universal behavior of any system displaced slightly from stable equilibrium. The same equation describes circuits, molecular vibrations, and acoustic resonance.
- Exclusions: Skip damping and driven oscillations for this card, skip resonance phenomena, skip coupled oscillators.
- Score: 7/10

---

## Candidate 10 — Build a Wave Interference Simulator: Double Slit with Claude

- Source: university-physics-bundle-with-llms/chapters/18-waves.md
- Lane: BUILD (Claude Code)
- Hook: The double-slit experiment is the most counter-intuitive result in all of physics. Two holes produce not two bright spots but a whole pattern of light and dark bands — because waves add and cancel. Build the simulation and measure the fringe spacing before a detector is placed.
- The artifact: A Manim animation of the double-slit interference pattern: two point sources separated by distance d, wavelength λ, and a screen at distance L — wave amplitudes computed via the superposition principle and the intensity pattern I = I_0 cos²(πd sin(θ)/λ) drawing out as a bright/dark fringe pattern on the screen.
- Prompt seed: `claude "Simulate double-slit interference in Python. Given slit separation d = 0.0001 m, wavelength λ = 500e-9 m, screen distance L = 1 m, compute the intensity pattern I(y) = I_0 * cos²(π * d * y / (λ * L)) on the screen for y from -0.03 to 0.03 m. Plot the pattern and annotate the fringe spacing Δy = λL/d. Then show how the pattern changes if λ doubles."`
- Read / check: Verify fringe spacing formula Δy = λL/d = (500e-9 × 1) / (0.0001) = 0.005 m = 5 mm. Check that doubling λ doubles the fringe spacing. Confirm the intensity pattern has a maximum at y=0 (central maximum) and zeros at the correct positions.
- Human supplies: Nothing — fully synthetic. All values are standard textbook parameters.
- Output medium: Manim (animated pattern building: wavefronts propagating from two slits, interference computed at each screen point, intensity pattern drawing left to right with fringe positions annotated)
- The change: Add a third slit and show how the interference pattern changes — the primary maxima sharpen and secondary maxima appear between them, motivating the diffraction grating as the limit of many slits.
- Teardown angle: Interference is a property of the wave equation, not of light specifically — it happens with water, sound, and matter waves too. The double-slit is the portable demonstration that any wave-like entity will produce this pattern.
- Exclusions: Skip single-slit diffraction, skip the quantum mechanical interpretation, skip polarization.
- Score: 7/10
