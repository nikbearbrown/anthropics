# Physics: Electromagnetism — CLI Video Ideas ("X with Claude")

---

## Candidate 01 — Build the Faraday Cage: How Much Shielding Does a Copper Box Provide?
- Source: physics-electromagnetism/chapters/03-gauss-law.md
- Lane: BUILD (Claude Code)
- Hook: An MRI room is lined with copper to attenuate external signals by 10⁸ to 10¹². Gauss's law explains why the field inside a conductor is exactly zero. This script computes the skin depth and attenuation for different conductor thicknesses and frequencies.
- The artifact: a Python script (~45 lines) using numpy and scipy.constants that: (1) computes the skin depth δ = √(2ρ/ωμ) for copper (ρ = 1.68×10⁻⁸ Ω·m, μ = μ₀) at frequencies from 1 kHz to 10 GHz, (2) computes attenuation in dB for a 1 mm copper sheet at each frequency: A = 20 log₁₀(e^(d/δ)), (3) marks the MRI frequency range (64 MHz for 1.5T, 128 MHz for 3T) and shows the attenuation there, (4) plots skin depth vs frequency and attenuation vs frequency on two panels. Manim animates the skin depth shrinking as frequency rises, then the attenuation rising.
- Prompt seed: `claude "Write a Python script using numpy, scipy.constants, and matplotlib that: (1) computes skin depth delta=sqrt(2*rho/(omega*mu0)) for copper (rho=1.68e-8, mu0=4*pi*1e-7) at frequencies f from 1e3 to 1e10 Hz, omega=2*pi*f; (2) for d=1e-3 m (1mm copper), computes attenuation A_dB=20*log10(exp(d/delta)) = 20/ln(10) * d/delta; (3) plots delta vs f and A_dB vs f on two subplots, both log-log; (4) marks f=64e6 Hz (1.5T MRI) and f=128e6 Hz (3T MRI) with vertical lines and their attenuation values."`
- Read / check: Verify skin depth for copper at 64 MHz: δ = √(2×1.68e-8/(2π×64e6×4πe-7)) ≈ 8.4 μm. Confirm attenuation for 1mm sheet at 64 MHz: A = 20×d/(δ ln10) ≈ 20×0.001/(8.4e-6×2.303) ≈ 1033 dB. Check that skin depth scales as f^(-1/2).
- Human supplies: Nothing — fully synthetic. Python with scipy.constants.
- Output medium: Manim (two panels: left — δ(f) log-log curve sweeping down; right — attenuation A_dB(f) log-log curve sweeping up; MRI frequency markers appearing; annotation "80-120 dB shielding for MRI" appearing in the right panel)
- The change: Add a comparison material (aluminum, stainless steel) and show how conductivity changes the skin depth at the same frequency — motivating why MRI rooms use copper specifically.
- Teardown angle: The Faraday cage works because charge redistributes on the surface of a conductor to exactly cancel any external field inside. Gauss's law makes this a mathematical necessity, not an engineering trick. The skin depth tells you how thick the cage needs to be.
- Exclusions: Wave transmission through the cage, MRI physics, RF waveguide design.
- Score: 9/10

---

## Candidate 02 — Build the Gauss's Law Symmetry Solver: Infinite Sheet, Wire, and Sphere
- Source: physics-electromagnetism/chapters/03-gauss-law.md
- Lane: BUILD (Claude Code)
- Hook: Gauss's law solves in seconds what Coulomb's law makes messy. For a line charge, a plane, and a sphere — three symmetry families — the electric field drops out of one integral. This script solves all three, plots the field, and shows where the symmetry breaks down.
- The artifact: a Python script (~50 lines) using numpy that: (1) computes E(r) = λ/(2πε₀r) for an infinite line charge (λ = 1 nC/m) from r=0.01 to r=10 m, (2) computes E = σ/(2ε₀) = constant for an infinite plane (σ = 1 nC/m²), (3) computes E(r) = ρr/3ε₀ (inside, r<R) and E(r) = Q/4πε₀r² (outside, r>R) for a sphere of radius R=1 m with uniform charge density ρ = 1 nC/m³, (4) plots all three field profiles. Manim animates each Gaussian surface appearing (cylinder, slab, sphere) then the corresponding E(r) curve tracing.
- Prompt seed: `claude "Write a Python script using numpy and matplotlib that plots three electric field profiles from Gauss's law: (1) infinite line charge lambda=1e-9 C/m: E(r)=lambda/(2*pi*eps0*r) for r from 0.01 to 10 m; (2) infinite plane sigma=1e-9 C/m^2: E=sigma/(2*eps0) — a horizontal line; (3) uniform sphere radius R=1 m, rho=1e-9 C/m^3 (so Q=4*pi*R^3/3*rho): inside E(r)=rho*r/(3*eps0), outside E(r)=Q/(4*pi*eps0*r^2). Plot all three on one figure with appropriate labels. eps0=8.854e-12."`
- Read / check: Verify E for line charge at r=1 m: λ/(2πε₀×1) = 1e-9/(2π×8.854e-12) ≈ 18 V/m. Confirm plane field is constant ≈ 1e-9/(2×8.854e-12) ≈ 56 V/m. Verify sphere: inside E increases linearly with r, outside E decreases as r⁻², and both join continuously at r=R. Check that E is continuous but its derivative is not at r=R.
- Human supplies: Nothing — fully synthetic. Python with numpy, matplotlib.
- Output medium: Manim (three panels or overlaid plot: each field profile animates in sequence; for the sphere, interior (green) and exterior (red) segments appear separately, then the junction is highlighted)
- The change: Show what happens when you take a line charge and give it finite length — the symmetry breaks and you must integrate Coulomb's law numerically instead. The off-axis field is no longer purely radial.
- Teardown angle: Gauss's law is always true. It is only easily solvable when the geometry has sufficient symmetry to make E factor out of the surface integral. The three symmetry families — spherical, cylindrical, planar — cover 90% of engineering problems. Outside them, you're back to numerical integration.
- Exclusions: Dielectric media, bound charges, numerical methods for arbitrary geometries.
- Score: 9/10

---

## Candidate 03 — Build the Circuit Analyzer: Kirchhoff's Laws on Any Resistor Network
- Source: physics-electromagnetism/chapters/07-dc-circuits.md
- Lane: BUILD (Claude Code)
- Hook: Any DC circuit with any number of loops can be solved with Kirchhoff's laws — set up the linear system, solve it. This script takes a circuit description as a list of nodes, branches, and resistors, and returns every branch current and node voltage.
- The artifact: a Python script (~55 lines) using numpy.linalg that: (1) implements a general node-voltage method for DC circuits, (2) solves the opening-case circuit (three lamps + laptop loading the power strip resistance), (3) outputs node voltages, branch currents, power dissipated per element, (4) shows how the voltage at the third lamp's node drops from 120 V to 116 V when the laptop is plugged in. Manim animates the circuit schematic with current magnitudes appearing as arrows proportional to branch current.
- Prompt seed: `claude "Write a Python script using numpy.linalg that implements the node-voltage method for DC circuits. (1) Define the circuit from the chapter: power strip resistance R_strip=0.5 ohm, laptop charger modeled as constant current source I_laptop=8 A, three lamp branches: lamp1=R1=144 ohm (120V/1A), lamp2=R2=144 ohm, lamp3=R3=200 ohm (120V minimum to light); source voltage V_s=120 V. (2) Build the conductance matrix G and current vector I for the node equations G*v=I. (3) Solve for node voltages v=solve(G,I). (4) Print node voltages, branch currents, and whether lamp3 lights (node voltage > 119V threshold)."`
- Read / check: Verify the node voltage at lamp3 drops by approximately IR_strip = 8A × 0.5Ω = 4V when laptop is active (from 120 to 116 V). Confirm lamp3 fails to light (116 < 119). Check that the conductance matrix is built correctly (G_ii = sum of conductances at node i, G_ij = -conductance of branch connecting i and j).
- Human supplies: Nothing — fully synthetic. Python with numpy.
- Output medium: Manim (circuit schematic: V_s on left, R_strip in series, then nodes branching to lamp1/lamp2/lamp3; when laptop is added, a current source appears; node voltage values animate in; lamp3 dims to gray when voltage drops below threshold)
- The change: Add a capacitor in parallel with lamp3 and show the transient response when the laptop is plugged in — the capacitor momentarily maintains the voltage, then lamp3 dims.
- Teardown angle: The loading effect is real and important. Every circuit element draws current through the wires connecting it to the source, and those wires have resistance. The failing lamp is not broken — the circuit it's embedded in changed. KCL and KVL make this calculable.
- Exclusions: AC circuit analysis, reactive impedance, non-linear components.
- Score: 9/10

---

## Candidate 04 — Build the Faraday's Law Generator: EMF from a Spinning Coil
- Source: physics-electromagnetism/chapters/10-electromagnetic-induction.md
- Lane: BUILD (Claude Code)
- Hook: 85% of the world's electricity comes from spinning coils in magnetic fields. Faraday's law predicts the EMF exactly: ε = -NdΦ/dt = NBAω sin(ωt). This script simulates a generator and shows how the AC waveform emerges from rotational motion.
- The artifact: a Python script (~45 lines) using numpy that: (1) defines a rotating coil: N=100 turns, A=0.05 m², B=0.5 T, ω=60×2π rad/s (60 Hz generator), (2) computes Φ(t) = NBAcos(ωt) and ε(t) = NBAω sin(ωt), (3) plots both on two panels showing the 90° phase shift, (4) computes peak EMF ε₀ = NBAω and RMS: ε_rms = ε₀/√2, (5) marks peak, RMS, and zero crossings. Manim animates a rotating coil schematic on the left and the EMF trace building on the right.
- Prompt seed: `claude "Write a Python script using numpy and matplotlib that: (1) defines generator: N=100, A=0.05, B=0.5, omega=2*pi*60 (60 Hz), (2) plots t from 0 to 2/60 s (two full cycles): Phi(t)=N*B*A*cos(omega*t) and emf(t)=-N*B*A*omega*sin(omega*t) on two stacked subplots; (3) prints peak emf = N*B*A*omega, rms emf = peak/sqrt(2); (4) marks the phase shift: when Phi is maximum (t=0), emf is zero; when Phi crosses zero, emf is maximum; (5) adds horizontal dashed lines at +/-emf_rms labeled 'RMS'."`
- Read / check: Verify ε₀ = 100 × 0.5 × 0.05 × 2π×60 = 942 V. Confirm ε_rms = 942/√2 ≈ 666 V. Verify the 90° phase shift: Φ = max → ε = 0; Φ = 0 → ε = max. Check that the minus sign in Faraday's law means ε is the negative derivative of Φ.
- Human supplies: Nothing — fully synthetic. Python with numpy, matplotlib.
- Output medium: Manim (two-panel: left — coil schematic rotating at 60 Hz (animated), field lines shown; right — EMF(t) trace building left to right; RMS dashed lines appearing; annotation showing NBAω = 942 V_peak)
- The change: Change ω from 60 Hz to 50 Hz (European grid standard) and show the frequency change while noting ε₀ also changes — then ask what N should be to maintain the same peak EMF at 50 Hz.
- Teardown angle: The generator is Faraday's law made mechanical. The rotating coil changes the flux through itself, and the changing flux drives a current. The sine wave you pull from a wall socket is the time derivative of a cosine — the EMF is exactly 90° behind the flux.
- Exclusions: Transformer efficiency, grid-scale generation, back-EMF in motors.
- Score: 9/10

---

## Candidate 05 — Build the Maxwell's Equations Consistency Checker: Light Falls Out
- Source: physics-electromagnetism/chapters/11-maxwells-equations.md
- Lane: BUILD (Claude Code)
- Hook: Maxwell added one term to Ampère's law to fix a mathematical contradiction. From that fix, in a vacuum with no sources, traveling-wave solutions emerge with speed c = 1/√(μ₀ε₀). This script derives c numerically from the constants and verifies the wave equation.
- The artifact: a Python script (~40 lines) using scipy.constants that: (1) computes c = 1/√(μ₀ε₀) from scipy.constants.mu_0 and scipy.constants.epsilon_0 and compares to scipy.constants.c, (2) sets up the wave equation ∂²E/∂t² = c² ∂²E/∂x² on a 1D grid, (3) numerically propagates a Gaussian wave packet for 100 time steps and confirms it travels at speed c, (4) measures the speed of the numerically propagated packet and compares to the analytic c. Manim animates the wave packet traveling across the grid.
- Prompt seed: `claude "Write a Python script using scipy.constants and numpy that: (1) computes c_derived = 1/sqrt(mu_0*eps_0) using scipy.constants.mu_0 and scipy.constants.epsilon_0, compares to scipy.constants.c, prints fractional error; (2) sets up a 1D EM wave simulation on x=linspace(0,10,1000) m with dx=0.01 m, dt=dx/(2*c) for stability; (3) initializes E(x,0) = exp(-(x-2)^2/0.1) (Gaussian pulse); (4) evolves using leapfrog: E[t+1] = 2*E[t] - E[t-1] + (c*dt/dx)^2*(E[t][2:] - 2*E[t][1:-1] + E[t][:-2]); (5) runs 500 steps and measures the pulse position at each step to compute propagation speed."`
- Read / check: Verify c_derived ≈ 2.9979×10⁸ m/s (fractional error should be <10⁻⁶ from scipy.constants). Confirm the Courant condition (c×dt/dx = 0.5 < 1) is satisfied for numerical stability. Verify the numerically measured propagation speed equals c within 1%.
- Human supplies: Nothing — fully synthetic. Python with scipy.constants, numpy.
- Output medium: Manim (wave packet animating rightward across the grid; a tracking dot following the peak; speed annotation appearing "v_measured = 2.998×10⁸ m/s = c"; equation "c = 1/√(μ₀ε₀)" displayed above)
- The change: Start with two wave packets traveling in opposite directions and show them passing through each other (superposition principle) — demonstrating that EM waves don't interact with each other.
- Teardown angle: Maxwell derived c from electrical and magnetic constants measured on a lab bench, with no reference to light. When his formula gave c = 3×10⁸ m/s — which matched the measured speed of light — he wrote "We can scarcely avoid the inference that light consists in the transverse undulations of the same medium." That is not hyperbole. That is the moment classical physics unified.
- Exclusions: Dispersion in media, polarization, photon physics.
- Score: 10/10

---

## Candidate 06 — Build the Capacitor Dielectric Explorer: How Polarization Changes the Field
- Source: physics-electromagnetism/chapters/05-capacitance-dielectrics.md
- Lane: BUILD (Claude Code)
- Hook: Insert a dielectric between capacitor plates and the stored energy drops — but the charge stays the same. The polarized material reduces the field inside. This script computes C, E, U, and D for any dielectric constant and shows the boundary conditions.
- The artifact: a Python script (~40 lines) using numpy and scipy.constants that: (1) for a parallel-plate capacitor (A=0.01 m², d=0.001 m) with Q=1 μC fixed, (2) sweeps κ (relative permittivity) from 1 to 100 (vacuum to high-κ ceramic), (3) plots C = κε₀A/d, E = Q/(κε₀A), U = Q²/(2C) = Q²d/(2κε₀A), and surface polarization charge σ_p = P = ε₀(κ-1)E vs κ, (4) shows that E decreases, C increases, U decreases — the dielectric does work as it's inserted. Manim animates all four curves sweeping as κ rises.
- Prompt seed: `claude "Write a Python script using numpy, scipy.constants, and matplotlib that: (1) defines parallel-plate capacitor: A=0.01, d=0.001, Q=1e-6; (2) for kappa=linspace(1,100,200): computes C=kappa*eps0*A/d, E=Q/(kappa*eps0*A), U=Q^2/(2*C), P_surface=eps0*(kappa-1)*E; (3) plots all four quantities vs kappa on 2x2 subplots; (4) marks kappa=1 (vacuum), kappa=3.9 (SiO2, used in CMOS transistors), kappa=80 (water), kappa=100 (BaTiO3). Use eps0=8.854e-12."`
- Read / check: Verify C at κ=1: ε₀×0.01/0.001 = 88.5 pF. Confirm E at κ=1: Q/(ε₀A) = 1e-6/(8.854e-12×0.01) ≈ 11.3 kV/m. Verify U(κ=1) = 0.5×Q²/C ≈ 5.65 μJ and U(κ=100) = 5.65/100 ≈ 56.5 nJ. Confirm polarization charge σ_p = ε₀(κ-1)E = Q(κ-1)/κA.
- Human supplies: Nothing — fully synthetic. Python with scipy.constants.
- Output medium: Manim (2×2 grid of panels: C(κ) rising, E(κ) falling, U(κ) falling, σ_p(κ) rising; all four animate simultaneously; kappa markers for SiO₂, water, BaTiO₃ appearing as vertical lines)
- The change: Fix the voltage instead of the charge (V = 100 V) and show that the energy now increases when a dielectric is inserted — the battery does work supplying additional charge.
- Teardown angle: The dielectric reduces the field inside the capacitor because the polarized molecules partially cancel the applied field. The stored energy decreases when Q is fixed — the polarization work comes from the material. The "paradox" of increasing C but decreasing U resolves immediately from Q=CV.
- Exclusions: Ferroelectric hysteresis, piezoelectrics, dielectric breakdown.
- Score: 8/10

---

## Candidate 07 — Build the Magnetic Force Simulator: Charged Particle in Crossed E and B Fields
- Source: physics-electromagnetism/chapters/08-magnetism-magnetic-force.md
- Lane: BUILD (Claude Code)
- Hook: A charged particle in crossed electric and magnetic fields drifts sideways — perpendicular to both fields. This E×B drift is the operating principle of a velocity selector, a mass spectrometer, and the magnetron in your microwave. This script simulates the trajectory for any particle speed and field ratio.
- The artifact: a Python script (~50 lines) using scipy.integrate.solve_ivp that: (1) integrates the Lorentz force equations: ṁv = q(E + v×B) for a proton in E = 10 kV/m (y-direction) and B = 0.1 T (z-direction), (2) runs three initial speeds: v < E/B (curves back), v = E/B (straight line — velocity selector), v > E/B (curves forward), (3) plots all three trajectories in the xy plane. Manim animates the three trajectories appearing simultaneously with the drift direction labeled.
- Prompt seed: `claude "Write a Python script using scipy.integrate.solve_ivp and numpy that simulates a proton in crossed fields: E=[0,1e4,0] V/m, B=[0,0,0.1] T. (1) Solves m*dv/dt = q*(E + cross(v,B)) and dr/dt = v for m=1.67e-27 kg, q=1.6e-19 C, initial position origin, initial velocities vx=[5e4, 1e5, 2e5] m/s, vy=vz=0; (2) Integrates 0 to 1e-6 s with max_step=1e-9 s; (3) Plots x vs y trajectories for all three cases; (4) Labels v=E/B=1e5 m/s as 'velocity selector — straight through'."`
- Read / check: Verify E/B = 1e4/0.1 = 1e5 m/s = the straight-through speed. Confirm that for v_x = E/B, the y-displacement should be negligible (straight line trajectory). Check that for v_x < E/B, the electric force dominates and the particle curves toward +y. Verify the proton cyclotron radius r = mv/(qB) ≈ 1.67e-27 × 1e5/(1.6e-19 × 0.1) ≈ 0.01 m.
- Human supplies: Nothing — fully synthetic. Python with scipy, numpy.
- Output medium: Manim (xy-plane plot; three trajectories appearing: slow proton curving back (red), E/B proton going straight (green, labeled "velocity selector"), fast proton curving forward (blue); E and B field direction indicators; drift arrow annotation)
- The change: Add a gradient in B (stronger on one side) and show the grad-B drift — the mechanism responsible for charged particle trapping in the Van Allen belts.
- Teardown angle: The velocity selector is a perfect application of vector physics: two forces exactly canceling at one speed. Only particles with v = E/B pass through undeflected. Mass spectrometers use this to select a beam before bending it in a pure B field, where radius of curvature gives the mass.
- Exclusions: Quantum effects on magnetic trapping, plasma physics beyond single-particle.
- Score: 9/10

---

## Candidate 08 — Build the Snell's Law Raytracer: Total Internal Reflection and Fiber Optics
- Source: physics-electromagnetism/chapters/12-capstone-unified-field.md
- Lane: BUILD (Claude Code)
- Hook: A light pulse enters a glass fiber and bounces along it for kilometers by total internal reflection. Snell's law sets the critical angle. This script traces rays through a fiber cross-section and shows how the critical angle depends on n₁ and n₂.
- The artifact: a Python script (~45 lines) using numpy that: (1) for glass-air interface (n₁=1.5, n₂=1.0), computes critical angle θ_c = arcsin(n₂/n₁) ≈ 41.8°, (2) traces five rays at incident angles 20°, 30°, 41.8°, 50°, 70° — showing the first three transmitting and refracting, the last two totally internally reflecting, (3) plots the ray paths in a cross-section diagram of a fiber (glass core, air cladding), (4) shows how reducing n₁-n₂ contrast (doped cladding, n₂=1.45 instead of 1.0) tightens the critical angle. Manim animates each ray tracing through the interface.
- Prompt seed: `claude "Write a Python script using numpy and matplotlib that: (1) for n1=1.5, n2=1.0: computes critical_angle = arcsin(n2/n1) in degrees; (2) traces 5 rays at incident angles theta_i = [20, 35, 41.8, 55, 70] degrees from inside glass hitting a flat interface at y=0: compute transmitted angle using Snell's law sin(theta_t)=n1/n2*sin(theta_i), with TIR if sin>1; (3) plots incident ray, reflected ray (for TIR angles) and refracted ray (for transmitting angles) for each; (4) draws the glass (y<0) and air (y>0) regions; (5) labels the critical angle case."`
- Read / check: Verify θ_c = arcsin(1.0/1.5) = 41.8°. Confirm for θ_i = 20°: sin(θ_t) = 1.5×sin(20°)/1 = 0.513, θ_t = 30.9°. Verify for θ_i = 55° > θ_c: sin(θ_t) = 1.5×sin(55°) > 1, total internal reflection. Check that at θ_c exactly, the refracted ray grazes the interface (θ_t = 90°).
- Human supplies: Nothing — fully synthetic. Python with numpy, matplotlib.
- Output medium: Manim (interface horizontal line: glass below, air above; five rays animate in sequentially — each shows incident (blue), then either refracted (green, partial reflection) or totally reflected (red) ray; critical angle case highlighted separately)
- The change: Add a second interface (fiber cladding, n₂=1.45 instead of air) and show how the critical angle changes — explaining why graded-index fiber has different propagation properties than step-index.
- Teardown angle: Fiber optic communication is Snell's law and TIR, applied at 200 million times per second over 10,000 km. The math is from 1621 (Snell) and 1866 (Maxwell). The engineering that puts 100 Tb/s through a hair-thin glass strand is the implementation.
- Exclusions: Dispersion in glass, optical amplifiers, modal propagation theory.
- Score: 8/10

---

## Candidate 09 — Build the Two-Slit Interference Pattern: Wave Optics from Maxwell
- Source: physics-electromagnetism/chapters/12-capstone-unified-field.md
- Lane: BUILD (Claude Code)
- Hook: Young's 1801 experiment destroyed the corpuscular theory of light. The striped pattern appears because two coherent wave sources interfere — constructively and destructively. This script computes the pattern analytically and shows how changing d, λ, and L changes the fringe spacing.
- The artifact: a Python script (~40 lines) using numpy that: (1) computes the double-slit intensity I(y) = I₀ cos²(πdy/λL) × sinc²(πay/λL) for d=0.5 mm slit separation, a=0.1 mm slit width, L=2 m screen distance, λ=500 nm, (2) plots the pattern, (3) uses an interactive slider (matplotlib.widgets) to change d from 0.1 to 2 mm and show fringe spacing Δy = λL/d changing in real time. Manim animates the pattern building up then the slit separation dial changing.
- Prompt seed: `claude "Write a Python script using numpy and matplotlib that: (1) computes double-slit intensity: I(y) = I0 * cos(pi*d*y/(lambda*L))^2 * (sin(pi*a*y/(lambda*L))/(pi*a*y/(lambda*L)))^2 for y from -0.02 to 0.02 m, d=5e-4, a=1e-4, L=2, lambda=500e-9; handle y=0 with np.sinc; (2) plots I vs y; (3) adds a slider widget for d from 1e-4 to 2e-3 m that updates the plot in real time; (4) shows the fringe spacing annotation Delta_y = lambda*L/d updating with the slider."`
- Read / check: Verify fringe spacing Δy = 500e-9 × 2 / 5e-4 = 2 mm at d=0.5 mm. Confirm that at y=0, the sinc²=1 and cos²=1, so I(0) = I₀ (central maximum). Verify the first single-slit minimum at y = λL/a = 10 mm (envelope zeros). Check that the slider updates the pattern correctly.
- Human supplies: Nothing — fully synthetic. Python with numpy, matplotlib, matplotlib.widgets.
- Output medium: Manim (intensity pattern animating in from center; bright central fringe then alternating dark/bright; fringe spacing labeled "Δy = λL/d"; then d-slider animation showing pattern compressing as d increases)
- The change: Replace coherent monochromatic light (λ=500 nm) with a mix of two wavelengths (λ₁=450 nm blue, λ₂=650 nm red) and show the colored fringe pattern — motivating the grating spectrometer.
- Teardown angle: The fringe pattern is the spatial Fourier transform of the aperture. The narrow slit envelope and the cosine interference combine multiplicatively — the single-slit pattern modulates the double-slit pattern. This is the same mathematics as AM radio modulation.
- Exclusions: Coherence length requirements, spatial coherence of real sources.
- Score: 8/10

---

## Candidate 10 — Build the Magnetic Field Map: Biot-Savart for Arbitrary Current Loops
- Source: physics-electromagnetism/chapters/09-sources-magnetic-fields.md
- Lane: BUILD (Claude Code)
- Hook: The Biot-Savart law computes the magnetic field from any current configuration — a straight wire, a loop, a solenoid, a Helmholtz coil. This script implements it numerically and maps the field for four classic geometries.
- The artifact: a Python script (~60 lines) using numpy that: (1) implements the Biot-Savart law numerically: dB = (μ₀I/4π) dL×r̂/r² summed over current segments, (2) computes and plots field lines and field strength for: (a) single current loop (z=0, radius R=0.1 m, I=1 A), (b) Helmholtz coil pair (two loops separated by R), (c) solenoid (10 loops), (3) uses matplotlib streamplot for field line visualization. Manim animates the field map building for each geometry sequentially.
- Prompt seed: `claude "Write a Python script using numpy and matplotlib that implements Biot-Savart law numerically. For a circular current loop: (1) discretize the loop at z=0, radius R=0.1 m into N=100 segments; (2) for each field point on a 50x50 grid in the xz plane (x from -0.3 to 0.3, z from -0.3 to 0.3), sum dB = mu0/(4*pi) * I * (dl cross r_hat) / r^2 over all segments; (3) plot streamlines using matplotlib.pyplot.streamplot with field magnitude as color; (4) also plot the Helmholtz configuration: two identical loops at z=+R/2 and z=-R/2."`
- Read / check: Verify on-axis field at center of single loop: B_z = μ₀I/(2R) = 4πe-7×1/(2×0.1) ≈ 6.28 μT. Confirm Helmholtz coils produce a more uniform central field. Verify field lines form closed loops (no magnetic monopoles — div B = 0). Check that the vectorized Biot-Savart computation handles the cross product correctly.
- Human supplies: Nothing — fully synthetic. Python with numpy, matplotlib.
- Output medium: Manim (field map animating for single loop first; streamlines drawing in; then Helmholtz coils appearing as a second panel; field uniformity annotation appearing in the central region of the Helmholtz configuration)
- The change: Add a magnetic dipole approximation B ∝ m/r³ and compare to the exact Biot-Savart result at large r — showing when the dipole approximation is valid.
- Teardown angle: Biot-Savart is the magnetic analog of Coulomb's law — both are inverse-square laws, both are summed over sources. The key difference: B never has divergence (no magnetic charges), so field lines always close on themselves. The streamplot makes that topology visible.
- Exclusions: Magnetic materials (μ≠μ₀), induced B from changing E (displacement current effects at high frequency).
- Score: 8/10
