# Physics: Thermodynamics — CLI Video Ideas ("X with Claude")

## Candidate 01 — "Compute Landauer's Limit with Claude: The Minimum Energy to Erase One Bit"
- Source: physics-thermodynamics/chapters/10-capstone-entropy-information-quantum.md
- Lane: BUILD (Claude Code)
- Hook: Every time your computer deletes a file, physics charges a minimum fee: k_BT ln 2 ≈ 3 × 10⁻²¹ J per bit at room temperature. At modern transistor densities, chips are approaching this floor — and Claude can show you exactly how close.
- The artifact: A log-log plot of "energy per bit erased vs. year" from 1970 to 2024, with real CPU data points overlaid on the Landauer limit line at k_BT ln 2 (T=300K). The data points march toward but never cross the line. A second panel shows the Landauer limit vs. temperature from 1K to 1000K — showing cryogenic computing shrinks the floor.
- Prompt seed: `claude "Write Python that: (1) Computes the Landauer limit k_B * T * ln(2) for T from 1K to 1000K and plots it. (2) Loads this table of CPU energy/operation data (provide: Intel 4004 1971: 1e-5 J, ... modern 2nm: 1e-16 J) and overlays it on the same log-log plot vs year. Mark where the data points are relative to the Landauer limit at 300K."`
- Read / check: Code: verify k_BT ln2 at 300K ≈ 2.87e-21 J; verify CPU trend slope on log-log plot is negative (improving). Output: all CPU data points should be ABOVE the Landauer line; the most recent should be within ~5 orders of magnitude of the limit.
- Human supplies: A curated table of CPU energy-per-operation from datasheets or published papers (e.g., from Koomey's law datasets). The book gives the formula; the human must supply or verify the real historical CPU numbers. Synthetic illustration acceptable if exact sources unavailable.
- Output medium: Manim — animate the CPU data points appearing chronologically, the Landauer line glowing as a floor; annotate the gap between the frontier and the limit.
- The change: Overlay a second line at 100k_BT (the "practical limit" due to noise margins), currently where real chips operate — showing the engineering gap above the physics limit.
- Teardown angle: Landauer's limit proves that information is physical. Computation has a thermodynamic cost that no engineering trick can eliminate — only the laws of physics can.
- Exclusions: Maxwell's demon full derivation; Szilard engine; reversible computation / quantum computing as workaround.
- Score: 9/10

## Candidate 02 — "Plot the Maxwell-Boltzmann Tail with Claude: Which Molecules Escape Mars?"
- Source: physics-thermodynamics/chapters/03-ideal-gas-kinetic-theory.md
- Lane: BUILD (Claude Code)
- Hook: Mars lost most of its atmosphere over billions of years because fast-moving molecules in the tail of the Maxwell-Boltzmann distribution exceed escape velocity. The same distribution that explains a room-temperature gas explains a planet's fate.
- The artifact: A Maxwell-Boltzmann speed distribution f(v) for CO₂, N₂, and H₂O at T=200K (Mars surface), with a vertical red line at the Mars escape velocity (5,027 m/s). The area to the right of the line — the escaping fraction — is shaded and annotated as a fraction (e.g., ~10⁻³⁰ for CO₂, much larger for H₂). A second panel compares the same molecules at T=300K (Earth), showing the escape fractions shrink further.
- Prompt seed: `claude "Write Python that plots the Maxwell-Boltzmann speed distribution f(v) = 4*pi*(m/(2*pi*kT))^(3/2) * v^2 * exp(-m*v^2/(2kT)) for CO2 (m=44 amu), N2 (28 amu), and H2O (18 amu) at T=200K. Mark the Mars escape velocity 5027 m/s. Use scipy.integrate.quad to compute the fraction of molecules with v > v_escape for each gas. Print those fractions."`
- Read / check: Code: verify each distribution integrates to 1.0 over [0,∞); verify peak velocity v_p = sqrt(2kT/m) matches formula. Output: escaping fraction should be < 1e-10 for CO₂, > 1e-5 for H₂ at 200K — the mass ratio drives the gap.
- Human supplies: Nothing — fully synthetic (Maxwell-Boltzmann is analytic).
- Output medium: Manim — animate the three distribution curves appearing, then the escape velocity line sliding in from the right; shade the tail areas and display the fraction numbers growing digit by digit.
- The change: Add hydrogen (H₂, m=2 amu) and show its escape fraction is dramatically larger — explaining why hydrogen is rare on Mars while CO₂ dominates.
- Teardown angle: Atmospheric retention is a statistics problem: it's not the average molecule that escapes, it's the rare tail. The exponential tail makes small mass differences produce enormous fractional differences in escape rates.
- Exclusions: Jeans escape full derivation; UV photodissociation; magnetic field effects on ion escape.
- Score: 9/10

## Candidate 03 — "Build a Carnot Efficiency Calculator with Claude: The Landscape of Heat Engine Performance"
- Source: physics-thermodynamics/chapters/06-second-law-heat-engines.md
- Lane: BUILD (Claude Code)
- Hook: The Carnot efficiency η_C = 1 − T_C/T_H is the hard ceiling on every heat engine ever built — and a single 2D heatmap shows you why power plants run so hot and refrigerators are so expensive to run.
- The artifact: A 2D heatmap of Carnot efficiency η_C as a function of T_H (300–2000K) and T_C (200–400K), with color scale from 0% (dark blue) to 90% (bright red). Overlaid white contour lines at η = 0.3, 0.5, 0.7. Annotated points: a coal power plant (T_H≈810K, T_C≈300K, η_C≈63%), a nuclear plant (T_H≈600K, T_C≈300K, η_C≈50%), a car engine (T_H≈900K, T_C≈350K, η_C≈61%), a home refrigerator (T_H=310K, T_C=255K, η_C=18%).
- Prompt seed: `claude "Write Python that computes and plots eta_C = 1 - T_C/T_H as a 2D heatmap with T_H on the x-axis (300 to 2000K) and T_C on the y-axis (200 to 400K). Use matplotlib with a red-blue diverging colormap. Draw contour lines at eta=0.3, 0.5, 0.7. Annotate 4 real engine operating points: coal plant (810K/300K), nuclear (600K/300K), car engine (900K/350K), refrigerator (310K/255K)."`
- Read / check: Code: verify η_C(T_H=T_C) = 0; verify η_C→1 as T_H→∞; verify coal plant point reads ≈63% on the heatmap. Output: all four annotated points should lie in physically reasonable regions (0 < η < 1, T_C < T_H).
- Human supplies: Nothing — fully synthetic (all operating temperatures are standard engineering reference values).
- Output medium: Manim — animate the heatmap filling in, then reveal the real-engine points one by one with text labels; animate a "temperature slider" that sweeps T_H upward showing efficiency improve.
- The change: Overlay the actual efficiency of each real engine (coal: ~35%, car: ~25%) as a separate color, and compute the "Carnot fraction" — how close each engine is to its theoretical max.
- Teardown angle: Every engineer who runs a power plant is chasing the Carnot limit on one axis while battling materials limits on the other. The heatmap makes the two constraints visible at once.
- Exclusions: Endoreversible engine (Curzon-Ahlborn efficiency); specific turbine/compressor design; thermodynamic cycles beyond Carnot.
- Score: 8/10

## Candidate 04 — "Derive Thermodynamics from Z with Claude: Partition Function → Free Energy → Everything"
- Source: physics-thermodynamics/chapters/08-statistical-mechanics.md
- Lane: BUILD (Claude Code)
- Hook: The partition function Z = Σ e^{−E_i/kT} is the master key — every thermodynamic quantity follows from a single derivative. Claude builds the machinery and demonstrates it on a monatomic ideal gas.
- The artifact: A table and set of plots showing Z(T), F(T) = −kT ln Z, S(T) = −∂F/∂T, ⟨E⟩(T) = −∂ ln Z/∂β, C_v(T) = ∂⟨E⟩/∂T, and P(T,V) = −∂F/∂V for an ideal monatomic gas. Each column is computed two ways: from the derivative formula and analytically — they match to machine precision.
- Prompt seed: `claude "Write Python that computes the canonical partition function for a monatomic ideal gas: Z = V * (2*pi*m*kT/h^2)^(3/2) (single particle). From Z compute: Helmholtz free energy F = -kT*ln(Z*N/N!), entropy S = -dF/dT, mean energy <E> = -d(ln Z)/d(beta), heat capacity Cv = d<E>/dT, and pressure P = -dF/dV. Compare each to the known analytic result (e.g., Cv = (3/2)*N*kB). Print a comparison table."`
- Read / check: Code: verify Sackur-Tetrode entropy formula matches the derivative; verify C_v = (3/2)Nk_B to 4 decimal places; verify PV = NkT from the pressure formula. Output: all comparison columns should agree to < 0.01%.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim — animate each thermodynamic quantity being "turned on" from Z in sequence, with arrows showing the derivative relationships; final frame shows the full tree of derived quantities.
- The change: Swap to a diatomic gas (add rotational degrees of freedom) and show C_v → (5/2)Nk_B, then add vibrational modes at high T showing C_v → (7/2)Nk_B — the equipartition staircase.
- Teardown angle: The partition function is the reason statistical mechanics works — one object encodes all thermodynamics. The derivative chain reveals thermodynamics as a hierarchy, not a collection of separate laws.
- Exclusions: Grand canonical ensemble; quantum ideal gas (Bose/Fermi); configuration integral for real gases.
- Score: 8/10

## Candidate 05 — "Model Heat Pump COP vs Furnace with Claude: When Electricity Beats Gas"
- Source: physics-thermodynamics/chapters/09-thermodynamics-real-world.md
- Lane: BUILD (Claude Code)
- Hook: A heat pump moves thermal energy rather than generating it — so its coefficient of performance (COP) can exceed 1. But COP drops as outdoor temperature falls, and at some crossover point a gas furnace wins. Claude finds that crossover.
- The artifact: A plot of heat pump COP_hp = T_H/(T_H − T_C) (Carnot limit) and COP_real = 0.4 × COP_Carnot (real-world fraction) vs. outdoor temperature T_C from −20°C to 15°C, with a dashed horizontal line at "furnace equivalent COP" (typically ~0.95 for gas, ~3.0 in primary-energy terms accounting for grid efficiency). The crossover temperature where heat pump wins vs. loses is annotated.
- Prompt seed: `claude "Write Python that plots heat pump COP vs outdoor temperature. T_H=70F (294K) indoor setpoint. T_C sweeps from 253K to 288K (-20C to 15C). Plot: (1) Carnot COP = T_H/(T_H-T_C), (2) Real COP = 0.4 * Carnot COP, (3) Gas furnace effective COP = 0.95 * (1/grid_carbon_factor) where grid_carbon_factor=0.45. Find and annotate the T_C where heat pump real COP equals furnace COP."`
- Read / check: Code: verify COP_Carnot > 1 everywhere; verify crossover temperature is in physically plausible range (typically around 0°C–5°C for a 40% Carnot efficiency). Output: the crossover annotation should name the temperature in both °C and °F.
- Human supplies: Nothing — fully synthetic (parameters from engineering standards).
- Output medium: Manim — animate the two COP curves being drawn as T_C slides from cold to warm; the furnace line slides in as a horizontal baseline; the crossover point flashes when found.
- The change: Vary the "real COP fraction" from 30% to 60% (the range of real heat pumps) and show how the crossover temperature shifts — revealing the sensitivity to installation quality.
- Teardown angle: Heat pumps are thermodynamically superior in most climates — the engineering challenge is keeping real COP close to Carnot. The model shows exactly what "close enough" means in practice.
- Exclusions: Vapor compression cycle detailed design; refrigerant selection; ground-source vs. air-source comparison in depth.
- Score: 8/10

## Candidate 06 — "Simulate Entropy of Mixing with Claude: Why Free Expansion Is Irreversible"
- Source: physics-thermodynamics/chapters/07-entropy.md
- Lane: BUILD (Claude Code)
- Hook: When a gas expands into vacuum, temperature doesn't change — but entropy increases. Why? Because the number of microstates multiplies. Boltzmann's formula S = k_B ln Ω makes this computable and visible.
- The artifact: A bar chart animation showing Ω (number of microstates) and S = k_B ln Ω for N=20 particles distributed between two halves of a box, as the constraint "all left" is released and the system equilibrates. The chart shows Ω growing by 2^N when the partition is removed, and S growing by Nk_B ln 2.
- Prompt seed: `claude "Write Python that computes the number of microstates Omega = C(N, n_left) and entropy S = kB * ln(Omega) for N=20 particles partitioned into a box (left half: n_left, right half: N-n_left). Plot Omega and S vs n_left/N. Mark the maximum at n_left=N/2. Compute the entropy increase when all particles start on the left and the partition is removed: Delta_S = kB * ln(2^N)."`
- Read / check: Code: verify Ω is maximized at n_left = N/2; verify ΔS = Nk_B ln 2 for free expansion; verify S(n=N/2) − S(n=N) = Nk_B ln 2. Output: the Ω curve should be a symmetric binomial distribution peaking at n=10.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim — animate the partition being "removed" and particles redistributing; bar chart of Ω growing from Ω=1 (all left) to Ω=C(20,10) at equilibrium; label ΔS.
- The change: Increase N from 20 to 100 and show how the distribution sharpens (narrower peak relative to N) — demonstrating why macroscopic fluctuations are statistically impossible.
- Teardown angle: Irreversibility is a counting argument: the equilibrium microstate is overwhelmingly more probable than the initial state. The second law is statistical, not absolute.
- Exclusions: Boltzmann H-theorem; ergodicity; quantum statistical mechanics.
- Score: 8/10

## Candidate 07 — "Build a PV Diagram Solver with Claude: Work from Any Thermodynamic Cycle"
- Source: physics-thermodynamics/chapters/05-pv-diagrams-processes.md
- Lane: BUILD (Claude Code)
- Hook: Every thermodynamic cycle — Carnot, Otto, Diesel, Rankine — is just a closed path on a PV diagram, and the enclosed area is work. Claude codes the four processes and lets you build any cycle interactively.
- The artifact: A PV diagram animation showing four processes for a Carnot cycle (isothermal expansion → adiabatic expansion → isothermal compression → adiabatic compression), with each process drawn as a curve and the enclosed area shaded and numerically labeled as W_net (in joules, for specific n, T_H, T_C parameters). A companion bar shows η_actual vs. η_Carnot.
- Prompt seed: `claude "Write Python that draws a Carnot cycle PV diagram for n=1 mol ideal monatomic gas, T_H=500K, T_C=300K, V1=0.01 m^3. Compute the 4 process curves: isothermal expansion (pV=nRT_H), adiabatic (pV^gamma=const), isothermal compression (pV=nRT_C), adiabatic return. Compute W_net = enclosed area using numerical integration (scipy.integrate.trapz). Compare to Q_H*(1-T_C/T_H) = Carnot work."`
- Read / check: Code: verify W_net from area integration matches η_C × Q_H to < 1%; verify the cycle closes (returns to V1, P1). Output: the four curves should form a closed loop with no gaps; the enclosed area should be positive (net work out).
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim — animate each process being drawn sequentially with color coding; final frame shades the enclosed area and labels W_net.
- The change: Add a real Otto cycle (for a car engine) on the same axes and compare enclosed areas — showing why the Otto cycle has lower efficiency than Carnot at the same temperature limits.
- Teardown angle: The PV diagram is a visual proof of the second law: you can't build a cycle that does more work than the area enclosed, and the Carnot cycle maximizes that area at fixed temperature limits.
- Exclusions: Rankine cycle with phase transitions; real gas corrections; irreversible processes on PV diagrams.
- Score: 8/10

## Candidate 08 — "Simulate Random Walk to Diffusion with Claude: Fick's Law from Brownian Motion"
- Source: physics-thermodynamics/chapters/03-ideal-gas-kinetic-theory.md
- Lane: BUILD (Claude Code)
- Hook: Diffusion looks like a smooth flow, but it's just the average of countless random walks. Claude runs 1,000 random-walking particles and watches Fick's law emerge — no fluid dynamics needed, just coin flips.
- The artifact: A time-lapse animation of 1,000 particles starting at x=0, each taking random ±1 steps at each time step. The density profile at each time is shown as a histogram, and a Gaussian fit overlay shows the diffusion profile ρ(x,t) = (4πDt)^{−1/2} exp(−x²/4Dt) matching the histogram. A log-log plot of ⟨x²⟩ vs t confirms the linear scaling ⟨x²⟩ = 2Dt.
- Prompt seed: `claude "Write Python that simulates 1000 random walkers each taking N=500 steps of size ±1. At each time step, compute the histogram of positions. Fit a Gaussian to the histogram and extract the width sigma(t). Plot sigma^2 vs t and verify linear scaling. Animate 10 snapshots of the histogram + Gaussian fit using matplotlib FuncAnimation. Export as numpy array."`
- Read / check: Code: verify ⟨x²⟩ = t (for unit step size and time step); verify Gaussian fit R² > 0.99 after t > 20 steps. Output: the log-log slope of ⟨x²⟩ vs t should be 1.00 ± 0.02.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim — animate the random walkers as dots spreading from origin, with the Gaussian envelope growing; label D from the slope of ⟨x²⟩ vs t.
- The change: Add a reflecting boundary at x=±L and show the distribution saturating to uniform — demonstrating equilibration and maximum entropy.
- Teardown angle: Diffusion is emergent statistical behavior: no particle "knows" about Fick's law; the law appears from randomness when you have enough particles. This is the thermodynamic arrow of time, made atomic.
- Exclusions: Fokker-Planck equation derivation; Langevin equation; anomalous diffusion.
- Score: 7/10

## Candidate 09 — "Compute Szilard Engine Efficiency with Claude: Information as Thermodynamic Resource"
- Source: physics-thermodynamics/chapters/10-capstone-entropy-information-quantum.md
- Lane: BUILD (Claude Code)
- Hook: The Szilard engine converts a single bit of information into exactly k_BT ln 2 of work — the same amount Landauer says it costs to erase that bit. This isn't a coincidence: information and energy are interchangeable at a known exchange rate.
- The artifact: A step-by-step diagram with computed numbers: (1) One-particle gas in volume V at temperature T. (2) Demon observes which half the particle is in (1 bit of information, cost = 0 for ideal observation). (3) Insert piston at center; expand isothermally to extract work W = k_BT ln 2 = 2.87 × 10⁻²¹ J at T=300K. (4) Erase the demon's memory: cost ≥ k_BT ln 2. Net cycle: zero work extracted — second law preserved.
- Prompt seed: `claude "Write Python that: (1) Computes the work extractable from a Szilard engine at temperatures T from 1K to 1000K: W = kB * T * ln(2). (2) Plots W vs T. (3) Computes the Landauer erasure cost = kB * T * ln(2) and overlays it — they should be identical. (4) Prints: at T=300K, W = ? joules, which equals ? electron-volts, which equals ? ATP molecules worth of energy (1 ATP ~ 5e-20 J)."`
- Read / check: Code: verify W = k_BT ln 2 at T=300K ≈ 2.87e-21 J; verify Landauer cost equals W (same formula); verify ATP conversion gives ~0.057 ATP molecules (showing one bit is worth much less than one chemical bond). Output: the two curves should be identical (overlapping); the ATP comparison should make the scale concrete.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim — animate the Szilard engine cycle as a 4-panel sequence with numerical values appearing at each step; final panel shows the Landauer cost closing the loop.
- The change: Compute the maximum number of Szilard engine cycles a 1 Watt power source could run per second at 300K — showing how far real computation is from this theoretical limit.
- Teardown angle: Bennett's resolution of Maxwell's demon (via Landauer) is one of the cleanest connections between physics and information theory. The second law isn't violated — it's enforced through the cost of memory erasure.
- Exclusions: Full Landauer derivation; quantum Szilard engine; mutual information formalism.
- Score: 7/10

## Candidate 10 — "Plot Real vs Ideal Gas with Claude: When the Van der Waals Equation Diverges"
- Source: physics-thermodynamics/chapters/09-thermodynamics-real-world.md
- Lane: BUILD (Claude Code)
- Hook: The ideal gas law PV = nRT breaks down near the condensation point — pressure can drop while volume decreases (the "spinodal" region). The van der Waals equation captures this, and the instability it predicts is the physics of phase transitions.
- The artifact: A family of isotherms (P vs V) for CO₂ from the van der Waals equation at T = 280K, 304K (critical), and 330K. The 280K isotherm shows the van der Waals "kink" with a non-physical region (∂P/∂V > 0). A Maxwell equal-area construction line replaces the kink with the phase-transition plateau. The critical point is marked.
- Prompt seed: `claude "Write Python that plots van der Waals isotherms P = nRT/(V-nb) - a*n^2/V^2 for CO2 (a=3.640 L^2*atm/mol^2, b=0.04267 L/mol, n=1 mol) at T=280K, 304K (critical), 330K. For the 280K isotherm, find the three volumes where dP/dV=0 (spinodal points). Apply the Maxwell construction to find the saturation pressure. Mark the critical point (T_c=304K, P_c=73atm)."`
- Read / check: Code: verify critical point conditions ∂P/∂V = 0 and ∂²P/∂V² = 0 satisfied at T_c, V_c; verify Maxwell construction equal areas above and below the plateau. Output: the 330K isotherm should be monotonic (no kink); the 280K should show a kink that disappears after Maxwell construction.
- Human supplies: Nothing — fully synthetic (van der Waals parameters from standard tables).
- Output medium: Manim — animate the three isotherms appearing in sequence; for the 280K curve, shade the non-physical region and animate the Maxwell construction line sliding into place.
- The change: Add the ideal gas isotherms at the same temperatures and compare — show where and by how much the van der Waals and ideal gas equations diverge.
- Teardown angle: The van der Waals "kink" is the mathematical signature of a phase transition. Thermodynamic stability (∂P/∂V < 0) tells you which parts of the isotherm are physically accessible — the rest is the two-phase region.
- Exclusions: Clausius-Clapeyron equation; full phase diagram; Gibbs free energy minimization.
- Score: 7/10
