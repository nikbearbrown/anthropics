# Physics with LLMs — CLI Video Ideas ("X with Claude")

## Candidate 01 — "Build Special Relativity Visualizer with Claude: Muon Survival from Time Dilation"
- Source: physics-with-llms/chapters/10-special-relativity.md (LLM Exercise)
- Lane: BUILD (Claude Code)
- Hook: Cosmic-ray muons are created 15 km up and live only 2.2 μs — classically they should decay before reaching Earth. But time dilation makes them survive, and a 20-line calculation shows exactly why.
- The artifact: A two-panel animation — left panel shows the muon's rest-frame life (short distance, decays early), right panel shows the lab-frame view (dilated time, muon reaches ground). A plot of survival probability P = e^{−t/γτ} vs. altitude sweeps from 15 km to 0, with classical (γ=1) and relativistic (γ=50) curves — the relativistic curve stays near 1 all the way to the ground; the classical one collapses before reaching sea level.
- Prompt seed: `claude "Write Python that computes the survival probability of a cosmic-ray muon as a function of altitude. Muon proper lifetime tau=2.2e-6 s, v=0.9994c. Compute Lorentz factor gamma=1/sqrt(1-v^2/c^2). Plot P_survive(h) = exp(-h/(gamma*v*tau)) for h from 15000m to 0m. Also plot the classical case (gamma=1). Print gamma, the lab-frame lifetime gamma*tau, and the fraction surviving classically vs relativistically."`
- Read / check: Code: verify γ ≈ 28.9 for v=0.9994c; verify lab-frame lifetime γτ ≈ 63.6 μs; verify classical survival to sea level P ≈ 1e-10, relativistic P ≈ 0.28. Output: the two curves should diverge by orders of magnitude below 10 km altitude.
- Human supplies: Nothing — fully synthetic (muon parameters from published particle physics data; the human may verify from PDG).
- Output medium: Manim — side-by-side frames showing classical vs. relativistic survival curves with altitude on y-axis; animate a muon "particle" descending with classical and relativistic decay markers.
- The change: Sweep v from 0.5c to 0.9999c and plot survival probability at sea level vs. v — show the sharp transition where relativity becomes essential.
- Teardown angle: Time dilation isn't just a thought experiment — it's the reason we can detect muons at all. Without relativity, cosmic ray physics would produce undetectable particles.
- Exclusions: Length contraction derivation; twin paradox; general relativity and gravity.
- Score: 9/10

## Candidate 02 — "Simulate Photoelectric Effect with Claude: Threshold Frequency from Work Functions"
- Source: physics-with-llms/chapters/21-the-quantum-nature-of-light.md (LLM Exercise)
- Lane: BUILD (Claude Code)
- Hook: Einstein's Nobel Prize was for a single equation: E_photon = hf must exceed the work function φ to eject an electron. Claude plots the experimental stopping voltage vs. frequency for three metals — and the slope is always h/e, regardless of metal.
- The artifact: A scatter plot of stopping voltage V_stop vs. photon frequency f for three metals (cesium φ=2.1 eV, sodium φ=2.3 eV, platinum φ=5.7 eV), showing three parallel lines with slope h/e = 4.14×10⁻¹⁵ V·s but different x-intercepts (threshold frequencies). An inset shows the threshold frequency f_0 = φ/h for each metal labeled.
- Prompt seed: `claude "Write Python that models the photoelectric effect for three metals (cesium phi=2.1eV, sodium phi=2.3eV, platinum phi=5.7eV). For each metal, compute the threshold frequency f0 = phi/h. For f from 0.5*f0 to 3*f0, compute stopping voltage Vstop = (h*f - phi)/e (where Vstop=0 for f<f0). Plot Vstop vs f for all three metals on one graph. Add a linear fit line and compute the slope — it should equal h/e = 4.14e-15 V*s."`
- Read / check: Code: verify threshold frequencies f_0(Cs) ≈ 5.1×10¹⁴ Hz, f_0(Na) ≈ 5.6×10¹⁴ Hz, f_0(Pt) ≈ 1.4×10¹⁵ Hz; verify slope of all three lines = h/e to 3 sig figs. Output: the three lines should be parallel with different x-intercepts; cesium line should start at lowest frequency.
- Human supplies: Nothing — fully synthetic (work functions are standard reference values; human may verify from CRC Handbook).
- Output medium: Manim — animate the three lines appearing one by one from their threshold frequency; annotate the slope h/e as the same for all three; label the threshold frequencies.
- The change: Vary the photon intensity (not frequency) and show that V_stop doesn't change — only the number of ejected electrons changes. This is the experimental fact that killed the classical wave theory of light.
- Teardown angle: The universality of h/e as the slope, regardless of metal, is why Einstein's equation convinced people. The work function sets the intercept; the quantum of action h sets the slope — and h is the same for everything.
- Exclusions: UV catastrophe derivation; Compton scattering; wave-particle duality of electrons.
- Score: 9/10

## Candidate 03 — "Measure Diffraction Gratings with Claude: Wavelength from Angle"
- Source: physics-with-llms/chapters/17-diffraction-and-interference.md (LLM Exercise)
- Lane: BUILD (Claude Code)
- Hook: A diffraction grating separates white light into its spectrum because d sin θ = mλ. Claude codes the inverse problem — given measured angles, recover the wavelengths — and shows how astronomers use starlight to determine what distant suns are made of.
- The artifact: A simulated diffraction pattern image (intensity vs. angle) for a grating with d=500 nm illuminated by three wavelengths (violet 400 nm, green 550 nm, red 700 nm). The first-order peaks appear at θ_1 = arcsin(λ/d) for each color. An inverse calculation table: given measured θ_m angles, recovered λ — values match inputs to < 0.1 nm.
- Prompt seed: `claude "Write Python that simulates a diffraction grating (d=500nm, N=1000 slits). For wavelengths 400nm, 550nm, 700nm, compute the intensity pattern I(theta) = (sin(N*pi*d*sin(theta)/lambda) / (N*sin(pi*d*sin(theta)/lambda)))^2 for theta from -30 to 30 degrees. Plot all three overlaid. Mark the m=1 peaks. Then invert: given peak angles theta_1, recover lambda = d*sin(theta_1) and compare to inputs."`
- Read / check: Code: verify first-order peak positions match arcsin(λ/d) for each wavelength; verify inversion recovers λ within 0.1 nm; verify resolving power R = mN = 1000 for first order. Output: three distinct peak clusters should be clearly separated for all three wavelengths.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim — animate the diffraction pattern appearing, with three colored intensity envelopes; animate the inverse-problem table filling in row by row.
- The change: Reduce from N=1000 to N=10 slits and show the peaks broadening and overlapping — demonstrating why resolving power scales with the number of slits.
- Teardown angle: The grating equation is a measurement instrument disguised as optics. Every spectroscope — from a chemistry lab to the James Webb Space Telescope — is running the same inversion problem Claude just coded.
- Exclusions: Grating manufacture; echelon gratings; polarization effects.
- Score: 8/10

## Candidate 04 — "Model Ohm's Law Circuits with Claude: Series vs Parallel from First Principles"
- Source: physics-with-llms/chapters/19-electrical-circuits.md (LLM Exercise)
- Lane: BUILD (Claude Code)
- Hook: Series and parallel resistors follow opposite rules — and the crossover in equivalent resistance has a physical interpretation. Claude builds both networks, plots R_eq vs N, and shows where parallel dominates.
- The artifact: Two plots side by side. Left: R_eq = N × R for N resistors in series (linear). Right: R_eq = R/N for N resistors in parallel (hyperbolic decay). A third panel shows power dissipation P = V²/R_eq for both, with a fixed voltage V=12V — parallel networks dissipate more power for the same voltage.
- Prompt seed: `claude "Write Python that: (1) Computes R_series = N*R for N from 1 to 20, R=100 ohms. (2) Computes R_parallel = R/N. (3) For V=12V, computes I=V/R_eq and P=V^2/R_eq for both. Plot R_eq vs N and P vs N on side-by-side panels. Add a third resistor value R=10 ohm and R=1000 ohm to show the ratios are independent of R value."`
- Read / check: Code: verify R_series(N=1) = R_parallel(N=1) = R; verify R_series(N=2) = 2R, R_parallel(N=2) = R/2; verify power ratio P_parallel/P_series = N². Output: the three R-value lines should be identical in shape, only scaled by R.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim — animate resistors being added one by one to each network; show R_eq and current updating in real time as N increases.
- The change: Build a mixed series-parallel network (two parallel banks in series) and apply Kirchhoff's laws to find the equivalent resistance — showing the systematic reduction method.
- Teardown angle: Parallel resistors lower resistance because they add current paths; series adds barriers. The power story is the practical consequence: parallel wiring is why household circuits are wired in parallel, not series.
- Exclusions: AC circuits (impedance); Kirchhoff's voltage law derivation; RC and RL transients.
- Score: 8/10

## Candidate 05 — "Build a Projectile Motion Calculator with Claude: Max Range, Wind Correction"
- Source: physics-with-llms/chapters/02-motion-in-one-dimension.md (LLM Exercise, extended to 2D)
- Lane: BUILD (Claude Code)
- Hook: The 45° optimal launch angle is only optimal in a vacuum — add drag and the optimal angle drops below 45°, and the exact value depends on speed and ball diameter. Claude finds it.
- The artifact: A family of trajectory curves (height vs. range) for launch angles 20°, 30°, 45°, 60°, 70° at v₀=30 m/s, with and without air drag (C_d=0.47, r=0.1 m, sea level). The no-drag case shows maximum range at exactly 45°; the drag case shifts the optimal angle to ~38°. A separate plot of R_max vs. v₀ shows how drag kills range at high speeds.
- Prompt seed: `claude "Write Python that simulates projectile motion with air drag. Drag force F_drag = 0.5 * rho * Cd * A * v^2, direction opposing velocity. rho=1.225 kg/m^3, Cd=0.47 (sphere), r=0.1m, mass=0.5kg. Use scipy.integrate.solve_ivp to solve the ODE system dx/dt=vx, dy/dt=vy, dvx/dt=-F_drag_x/m, dvy/dt=-g-F_drag_y/m. Sweep theta from 10 to 80 degrees at v0=30m/s. Find the theta that maximizes range."`
- Read / check: Code: verify vacuum case max range at exactly 45°; verify drag case optimal angle < 45°; verify range at 45° is less with drag than without. Output: the drag trajectories should be clearly shorter and more asymmetric than vacuum parabolas.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim — animate all trajectory curves on one axes, with the optimal angle labeled and highlighted; animate a "drag adjustment" showing the optimal angle shifting down as C_d increases.
- The change: Add wind (a horizontal velocity offset in the drag force) and show how the optimal angle and range change — a practical problem for any ball-sport analysis.
- Teardown angle: The 45° rule is a physicist's lie: it assumes no air resistance. Drag breaks the symmetry between ascending and descending phases. The real optimal angle depends on the drag-to-gravity ratio.
- Exclusions: Magnus effect (spinning ball); terminal velocity derivation; multi-body problems.
- Score: 8/10

## Candidate 06 — "Measure Simple Machines with Claude: Force-Distance Trade-offs Plotted"
- Source: physics-with-llms/chapters/09-work-energy-and-simple-machines.md (LLM Exercise)
- Lane: BUILD (Claude Code)
- Hook: Every simple machine has the same law — work in equals work out (ignoring friction). But the lever, pulley, inclined plane, and wheel-and-axle each have different mechanical advantage formulas. Claude builds the comparison.
- The artifact: A comparison bar chart of mechanical advantage (MA) for five simple machines, each configured to lift a 100 kg load with the minimum force — lever (arm ratio 5:1, MA=5), pulley (4 ropes, MA=4), inclined plane (length/height=6, MA=6), wheel-and-axle (radius ratio 10:1, MA=10), screw (pitch 2mm, handle 10cm, MA=314). Input force and output force labeled for each.
- Prompt seed: `claude "Write Python that computes and plots the mechanical advantage for five simple machines: (1) lever MA = L_effort/L_load, (2) fixed+movable pulley system MA = n_rope_segments, (3) inclined plane MA = length/height, (4) wheel-and-axle MA = R_wheel/R_axle, (5) screw MA = 2*pi*r_handle/pitch. For a 100kg load (F_load=981N), compute the required input force for each. Plot a bar chart of MA and input force side-by-side."`
- Read / check: Code: verify MA × F_input = F_load for each machine; verify screw MA ≈ 314 for the given parameters. Output: screw should have highest MA by far; lever and pulley should be in the 4–10 range.
- Human supplies: Nothing — fully synthetic (geometric parameters given in prompt).
- Output medium: Manim — animate each simple machine diagram beside its bar, with the force arrows scaling inversely with MA; annotate that work = F × d is constant.
- The change: Add friction efficiency (η=0.8 for each) and show the actual mechanical advantage falls — and compute the efficiency needed to make each machine "worth using."
- Teardown angle: Simple machines don't create or destroy energy — they trade force for distance. The mechanical advantage is always a ratio. Understanding this is the foundation of all mechanical engineering.
- Exclusions: Compound machines; efficiency derivations from friction coefficients; gear trains.
- Score: 7/10

## Candidate 07 — "Model the Standard Model with Claude: Particle Families and Force Carriers"
- Source: physics-with-llms/chapters/23-particle-physics.md (LLM Exercise)
- Lane: BUILD (Claude Code)
- Hook: The Standard Model has 17 fundamental particles organized in three families plus four force carriers — and every observable phenomenon in chemistry, biology, and engineering emerges from their interactions. Claude maps the whole table and reveals the pattern.
- The artifact: A structured visualization — the Standard Model particle table rendered as a color-coded grid (quarks/leptons by generation, bosons in a separate column), with each particle labeled by mass, charge, and spin. A second panel shows a "force web" diagram connecting particles to their carrier bosons (photon=EM, W/Z=weak, gluon=strong, graviton=gravity).
- Prompt seed: `claude "Write Python that creates a visualization of the Standard Model particle table. Create a 4-column, 5-row grid (3 quark generations + leptons, plus bosons). For each particle store: name, symbol, mass (MeV), charge (e), spin. Use matplotlib to draw colored rectangles (quarks=green, leptons=yellow, gauge bosons=red, Higgs=blue) with text labels. Also draw a force-carrier diagram using networkx."`
- Read / check: Code: verify all 12 fermions (6 quarks + 6 leptons) and 5 bosons present; verify charge assignments correct (up quark +2/3, down quark -1/3, electron -1). Output: the grid should have correct mass ordering across generations (electron < muon < tau).
- Human supplies: A verified particle data table (masses, charges, spins) — from PDG 2024. The human should check that the values match the current Particle Data Group tables before approving. Synthetic values from textbook approximations are acceptable for illustration.
- Output medium: Manim — animate the table building particle by particle in order of discovery (electron 1897, proton 1919, ..., Higgs 2012), with year labels appearing.
- The change: Highlight which particles the human body is "made of" (up quarks, down quarks, electrons) and compute what fraction of the total SM particle count that represents — 3/17 fundamental particles make all of chemistry.
- Teardown angle: The Standard Model is the most tested physical theory in history, and it fits on a single page. The gap (gravity, dark matter, dark energy) is what makes particle physics interesting now.
- Exclusions: Feynman diagrams; QCD color charge; neutrino mass and mixing; beyond-Standard-Model theories.
- Score: 7/10

## Candidate 08 — "Compute Time Dilation GPS Correction with Claude: Why Your Phone Needs Relativity"
- Source: physics-with-llms/chapters/10-special-relativity.md
- Lane: BUILD (Claude Code)
- Hook: GPS satellites experience two relativistic effects in opposite directions — special relativity slows their clocks (moving fast), general relativity speeds them up (high altitude). Without correction, your phone's GPS would drift 11 km/day.
- The artifact: A bar chart showing three contributions to daily GPS clock error: (1) special relativistic time dilation Δt_SR = −7.2 μs/day (SR slows satellite clock), (2) gravitational time dilation Δt_GR = +45.9 μs/day (GR speeds satellite clock), (3) net effect +38.7 μs/day. A second calculation: distance error = c × 38.7 μs = 11.6 km/day without correction.
- Prompt seed: `claude "Write Python that computes GPS relativistic corrections. Satellite altitude h=20200km above Earth surface. Orbital speed v=3.87 km/s. (1) SR time dilation: delta_t_SR/t = -v^2/(2c^2) (first order), giving microseconds per day. (2) GR gravitational blueshift: delta_t_GR/t = g*h/c^2 (approx), refined as GM/c^2*(1/R_earth - 1/(R_earth+h)), giving microseconds per day. (3) Net = SR + GR. (4) Position error = c * net_time_error * 86400 seconds."`
- Read / check: Code: verify Δt_SR ≈ −7.2 μs/day; verify Δt_GR ≈ +45.9 μs/day; verify net ≈ +38.7 μs/day; verify position drift ≈ 11.6 km/day. Output: all three corrections should have correct sign and magnitude matching published GPS values.
- Human supplies: Nothing — fully synthetic (orbital parameters from GPS specifications; the human may verify from GPS IIF satellite datasheets).
- Output medium: Manim — animate a bar chart with three bars appearing: SR correction (negative, blue), GR correction (positive, red), net correction (green); then animate a map showing 11 km drift accumulating over one day.
- The change: Compute how much the GPS error would grow if only the SR correction were applied (forgetting GR) vs. neither correction — showing which effect dominates and why GR can't be ignored.
- Teardown angle: GPS is the most commercially important application of general relativity — and it works only because Einstein was right. The correction isn't small; 11 km/day would make GPS useless within hours.
- Exclusions: Sagnac effect (Earth rotation); satellite geometry and PDOP; full metric tensor approach.
- Score: 9/10

## Candidate 09 — "Simulate Energy Conservation with Claude: Pendulum from Release to Swing"
- Source: physics-with-llms/chapters/09-work-energy-and-simple-machines.md (LLM Exercise)
- Lane: BUILD (Claude Code)
- Hook: A pendulum trades potential energy for kinetic energy exactly — and the conservation law means you can predict the speed at any point from the height alone, without solving the differential equation.
- The artifact: A plot of KE(t), PE(t), and total E(t) for a pendulum released from 30° over 2 full periods. Total energy stays constant (within numerical error); KE peaks at the bottom; PE peaks at the turning points. A companion animation shows the pendulum swinging with a colored energy bar updating each frame.
- Prompt seed: `claude "Write Python that solves the pendulum ODE theta'' = -(g/L)*sin(theta) using scipy.integrate.solve_ivp, initial angle 30 degrees, L=1m, 4 periods. Compute KE = 0.5*m*L^2*omega^2 and PE = m*g*L*(1-cos(theta)) at each time step. Plot KE, PE, and KE+PE vs time. Print max deviation of total energy from initial value."`
- Read / check: Code: verify total energy E = KE + PE varies < 0.01% over 4 periods (energy conservation test); verify period T ≈ 2π√(L/g) to within 2% for 30° amplitude (small-angle approximation starts breaking down). Output: KE and PE should be perfectly anti-correlated; total E should be flat.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim — animate the pendulum swinging with a real-time energy bar chart updating beside it; annotate KE max at the bottom and PE max at the turning points.
- The change: Increase initial angle to 90° and show the deviation from the small-angle approximation (period increases); compare the numerically integrated period to the small-angle formula.
- Teardown angle: Conservation of energy is a theorem (Noether's theorem: time-translation symmetry), not an empirical law. The pendulum shows it in its simplest form — and the deviation at large angles shows where the approximation breaks.
- Exclusions: Damped pendulum; driven resonance; chaotic pendulum (double pendulum).
- Score: 8/10

## Candidate 10 — "Model Population Growth with Claude: Exponential vs Logistic with Carrying Capacity"
- Source: physics-with-llms/chapters/01-what-is-physics.md (mathematical modeling, LLM Exercise)
- Lane: BUILD (Claude Code)
- Hook: Exponential growth is the simplest model in physics — but it always breaks down. The logistic equation adds a single parameter (carrying capacity K) and turns explosion into an S-curve. Claude fits both to historical US population data.
- The artifact: A scatter plot of US census population from 1790 to 2020 with two fitted curves: exponential N(t) = N₀ e^{rt} (fits well to 1900, then diverges), and logistic N(t) = K/(1 + ((K-N₀)/N₀) e^{-rt}) (fits the full range). The logistic curve shows the S-shape flattening near K. A residuals panel shows the exponential error growing; the logistic error staying small.
- Prompt seed: `claude "Write Python that loads US census population data (provide: year and population for 1790-2020 from census.gov). Fit two models: (1) exponential N=N0*exp(r*t) using scipy.optimize.curve_fit, (2) logistic N=K/(1+((K-N0)/N0)*exp(-r*t)). Plot both fits over the data and a residuals panel. Print fitted parameters and R^2 for both."`
- Read / check: Code: verify exponential model R² < 0.9 over full time range (it fails after 1900); verify logistic R² > 0.99; verify fitted K (carrying capacity) is in physically interpretable range (200M–2B for US). Output: logistic curve should show clear S-shape flattening; exponential should diverge after 1950.
- Human supplies: US census population table 1790–2020 (from census.gov, 23 data points). The human should pull this table — it's publicly available and verifiable.
- Output medium: Manim — animate the data points appearing year by year, then the two fitted curves being overlaid; animate the residual panel showing the exponential error growing.
- The change: Use the same logistic parameters to forecast US population to 2100 — and compute confidence intervals from the fit uncertainty to show how uncertain the forecast is.
- Teardown angle: The logistic model is the simplest model that knows the world is finite. Exponential models always fail eventually; the question is whether you add the constraint before or after the system hits it.
- Exclusions: Age-structured models; immigration and demographic components; multi-species Lotka-Volterra.
- Score: 7/10
