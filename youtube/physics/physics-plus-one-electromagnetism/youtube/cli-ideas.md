# Physics +1: Advanced Electromagnetism — CLI Video Ideas ("X with Claude")

## Candidate 01 — Visualize Electric Field Lines and Equipotential Surfaces with Claude

- Source: physics-plus-one-electromagnetism/chapters/02-electric-field.md
- Lane: BUILD (Claude Code)
- Hook: Electric field lines are not real — they are a visualization tool invented by Faraday that perfectly predicts where forces point and how strong they are. But the pattern of lines around a dipole, a charged conductor, or a point charge is beautiful and the rules are exact. Build the full 2D field plot.
- The artifact: A D3 animation showing the electric field of a configurable charge distribution: 1–4 point charges (draggable), with live-updating field lines and equipotential contours. The field lines are computed using streamline integration from the Coulomb force field. Equipotentials are computed by contour-finding on the scalar potential grid V = Σ(kq_i/r_i). Color encodes |E| magnitude. A "net charge" readout shows that field lines terminate only on charges.
- Prompt seed: `claude "Build a D3 v7 single-file HTML electric field and equipotential visualizer. Up to 4 draggable point charges (±1 to ±10 µC, set by slider). Compute E_x = Σ(kq_i·(x-x_i)/r_i³), E_y on a 60×60 grid. Draw: (1) field lines via streamline integration starting from unit circle around each charge, (2) equipotential contours (green, at V = -200 to +200 kV levels), (3) |E| colormap (blue=low, red=high). Verify: single +q charge → radial field lines, circular equipotentials."`
- Read / check: For a single charge at origin: E_x = kq×x/r³, E_y = kq×y/r³ → purely radial field lines. Equipotentials: circles V = kq/r = const → r = kq/V. For a dipole (+q at x=+d, −q at x=−d): field lines should connect + to −, and the equipotential pattern should show the saddle point between charges. Field lines should terminate only on charges, never mid-air.
- Human supplies: Nothing — fully synthetic. Coulomb's law analytic.
- Output medium: d3 (animated, single HTML file)
- The change: Add a conductor: place a conducting sphere and show how charges redistribute on the surface, producing zero field inside and field lines perpendicular to the surface outside. This demonstrates Gauss's law in action.
- Teardown angle: The field line picture is not just aesthetics — the density of lines is proportional to |E|, so the diagram encodes the quantitative field strength. Faraday invented this visualization before anyone had Maxwell's equations; it turned out to be exactly consistent with them.
- Exclusions: Multipole expansion derivation, numerical FEM methods, induced charge distributions in detail.
- Score: 9/10

---

## Candidate 02 — Build a DC Circuit Solver with Kirchhoff's Laws using Claude

- Source: physics-plus-one-electromagnetism/chapters/07-dc-circuits.md
- Lane: BUILD (Claude Code)
- Hook: Kirchhoff's laws are just conservation of energy and conservation of charge — applied to every node and every loop in a circuit. Build a general DC circuit solver: give it any network of resistors and voltage sources, and it solves for every current and voltage drop automatically using matrix inversion.
- The artifact: A D3 interactive circuit builder: the viewer places resistors and voltage sources on a grid by clicking. The circuit topology is extracted as an adjacency matrix. Modified nodal analysis (MNA) sets up the system of linear equations [G][V] = [I] and solves it with matrix inversion. Branch currents and node voltages are displayed on the circuit diagram. A "Wheatstone bridge" preset tests the bridge-balance condition.
- Prompt seed: `claude "Build a D3 v7 single-file HTML DC circuit solver using Modified Nodal Analysis (MNA). Grid-based circuit editor: click to place wires, resistors (slider for R), voltage sources (slider for V), ground node. Extract node-admittance matrix G and source vector; solve [G][V]=[I] using Gaussian elimination (JavaScript). Display: node voltages (color-coded), branch currents (arrow width ∝ current). Presets: voltage divider, Wheatstone bridge. Verify: two 10Ω resistors in series with 10V source → 5V at midpoint, I=0.5A."`
- Read / check: Two 10Ω in series with 10V: node voltage at midpoint = 5V (voltage divider). I = 10V/20Ω = 0.5A. Wheatstone bridge: R1=R3=R2=R4=100Ω with 12V supply → V_bridge = 0V (balanced). Change one resistor to 101Ω → tiny voltage appears. Verify matrix setup: G[i,j] = sum of conductances for node i (diagonal) and −conductance between i and j (off-diagonal).
- Human supplies: Nothing — fully synthetic. MNA matrix setup is systematic and Claude can implement Gaussian elimination in JavaScript.
- Output medium: d3 (animated, single HTML file)
- The change: Add capacitors and inductors: switch to phasor domain (AC circuit analysis) for sinusoidal sources. Compute impedances Z_C = 1/(jωC) and Z_L = jωL. Frequency slider sweeps from 1 Hz to 1 MHz, showing how the circuit response changes — the viewer finds the resonant frequency of an RLC circuit.
- Teardown angle: Kirchhoff's laws reduce circuit analysis to linear algebra. Any circuit, however complex, is a system of linear equations — and matrix inversion is the complete solution. The art is in formulating the equations; the computation does the rest.
- Exclusions: Nonlinear elements (diodes, transistors), transmission line effects at high frequency, SPICE-level modeling.
- Score: 9/10

---

## Candidate 03 — Simulate Gauss's Law: Verify Electric Flux for Any Charge Distribution with Claude

- Source: physics-plus-one-electromagnetism/chapters/03-gauss-law.md
- Lane: BUILD (Claude Code)
- Hook: Gauss's law says the total flux through any closed surface equals Q_enclosed/ε₀. You can draw the weirdest possible surface around a point charge — a crumpled, asymmetric blob — and the flux is still exactly Q/ε₀. Build the numerical verifier and prove it.
- The artifact: A D3 visualization of a 2D Gaussian surface (a user-drawn closed curve) around a configurable charge distribution. The electric field at each surface segment is computed from Coulomb's law (sum over all charges). The outward normal at each segment is computed from the curve geometry. The flux Φ = ΣE·n̂ dA is integrated numerically over the surface. A real-time readout compares Φ_numerical vs. Q_enclosed/ε₀ — they should agree within numerical precision, regardless of surface shape.
- Prompt seed: `claude "Build a D3 v7 single-file HTML Gauss's law verifier. User draws a closed surface (click to add vertices, auto-close). Inside the surface: 1–3 draggable point charges (±1 to ±5 µC). Compute: outward normal at each edge segment, E = Σ(kq/r²)·r̂ at each segment midpoint, flux Φ = ΣE·n̂·Δl. Display Φ_numerical vs. Q_enc/ε₀. Show % error. Also display total charge outside the surface → confirm contributes zero flux. Verify: Q=+1µC, any surface → Φ = 1×10⁻⁶/8.854×10⁻¹² = 1.13×10⁵ V·m."`
- Read / check: Q_enclosed = 1µC → Φ = Q/ε₀ = 10⁻⁶/(8.854×10⁻¹²) = 1.130×10⁵ V·m (in 3D). In 2D the formula is Φ = Q/ε₀ per unit length, but the proportionality holds. Charges outside the surface: their field lines enter and exit the surface in equal amounts → net flux contribution = 0 (verify numerically). Asymmetric surface should give same result as circle around same charge.
- Human supplies: Nothing — fully synthetic.
- Output medium: d3 (animated, single HTML file)
- The change: Demonstrate the shell theorem: place a uniform shell of charge and show that the flux through a surface inside the shell is zero (E=0 inside a conductor). Then show that a surface outside the shell gives the same flux as a point charge of equal total charge at the center.
- Teardown angle: Gauss's law works because electric field lines from a point charge obey an inverse-square law, which exactly cancels the surface area growing as r² — the flux through any enclosing surface is the same. Any other power law would fail.
- Exclusions: Vector potential, magnetic Gauss's law (∇·B=0), displacement current.
- Score: 9/10

---

## Candidate 04 — Build a Magnetic Field Visualizer for Current Configurations with Claude

- Source: physics-plus-one-electromagnetism/chapters/09-sources-magnetic-fields.md
- Lane: BUILD (Claude Code)
- Hook: The magnetic field of a solenoid is nearly uniform inside and nearly zero outside — and Ampere's law explains why in one line. But the field of a single wire, a dipole, or a toroid looks completely different. Build the Biot-Savart visualizer and compute the field for any current configuration.
- The artifact: A D3 animation of magnetic field lines for user-configurable current configurations: straight wire, circular loop, solenoid (approximated as stack of loops), Helmholtz coil pair. The Biot-Savart law dB = μ₀I/(4π) × dl×r̂/r² is integrated numerically along each wire segment. Field lines are drawn by streamline integration from B. Field magnitude color map. A "Helmholtz coil" preset shows the uniform-field region between two coils separated by their radius.
- Prompt seed: `claude "Build a D3 v7 single-file HTML magnetic field visualizer using Biot-Savart. Source options: (1) straight finite wire, (2) circular loop radius R, (3) solenoid (N loops, length L), (4) Helmholtz pair (two loops, separation=R). Numerically integrate dB = μ₀I·dl×r̂/(4π·r²) along wire segments. Plot |B| colormap and field line streamlines. Sliders: I (1–100 A), R, L, N. Verify: infinite straight wire → B = μ₀I/(2πr) = 2×10⁻⁷/r for I=1A; at r=1cm, B=20µT."`
- Read / check: Straight wire I=1A, r=0.01 m: B = μ₀I/(2πr) = 4π×10⁻⁷×1/(2π×0.01) = 2×10⁻⁵ T = 20 µT. Field lines should be concentric circles around the wire. Circular loop at center: B = μ₀I/(2R). Solenoid interior: B ≈ μ₀nI (uniform). Helmholtz coils at midpoint: B is maximally uniform (∂B/∂z = ∂²B/∂z² = 0 at center).
- Human supplies: Nothing — fully synthetic. Biot-Savart numerical integration.
- Output medium: d3 (animated, single HTML file)
- The change: Add Ampere's law verification: draw a circular Amperian loop around the wire and compute ∮B·dl numerically; verify it equals μ₀I_enclosed. Show that for a surface inside the solenoid, ∮B·dl = μ₀nI (the enclosed current per unit length × length).
- Teardown angle: Ampere's law is to magnetism what Gauss's law is to electricity — both are field-line counting arguments that exploit symmetry to compute fields without integration. Biot-Savart is the general tool; Ampere's law is the shortcut when symmetry applies.
- Exclusions: Magnetic vector potential A, magnetization and susceptibility, ferromagnetic hysteresis.
- Score: 9/10

---

## Candidate 05 — Simulate Electromagnetic Induction and Faraday's Law with Claude

- Source: physics-plus-one-electromagnetism/chapters/10-electromagnetic-induction.md
- Lane: BUILD (Claude Code)
- Hook: Faraday's law is the foundation of every generator, transformer, and wireless charger: a changing magnetic flux induces an EMF. Build a simulation where a magnet moves through a coil — watch the induced current appear, reverse direction as the magnet exits, and compute the EMF from dΦ/dt.
- The artifact: A D3 animation of a bar magnet moving through a solenoid coil. The magnetic flux Φ(t) = ∫B·dA through the coil is computed at each time step from the dipole field of the moving magnet. The induced EMF ε = −dΦ/dt is computed as a numerical derivative. The induced current I = ε/R in a resistor R is displayed. A current meter (galvanometer) deflects left/right depending on current direction. A second panel plots ε(t) and Φ(t) vs. time.
- Prompt seed: `claude "Build a D3 v7 single-file HTML Faraday's law simulator. Bar magnet with dipole field B_z(z,r) = μ₀m/(4π)·[3cos²θ-1)/r³] moves along the axis through a coil (N turns, radius a). Compute Φ(t) = N·∫B_z·dA numerically over the coil area. Compute ε = -dΦ/dt (numerical derivative). Display: (1) animated magnet and coil, (2) galvanometer deflecting with I = ε/R, (3) time series Φ(t) and ε(t). Sliders: magnet speed v, coil turns N, coil radius a, load resistance R. Verify: ε reverses sign as magnet enters vs. exits coil."`
- Read / check: As magnet enters coil (Φ increasing): ε = −dΦ/dt < 0 (opposing increase by Lenz's law). As magnet exits (Φ decreasing): ε > 0. The ε(t) curve should look like a derivative of Φ(t) — peak when magnet is near coil center (Φ changing fastest). Verify Lenz's law: induced current creates a B field opposing the change.
- Human supplies: Nothing — fully synthetic. Dipole field formula analytic; flux integral numerical.
- Output medium: d3 (animated, single HTML file)
- The change: Add a transformer: replace the moving magnet with an AC source in a primary coil and a secondary coil on the same core. Show V_s/V_p = N_s/N_p (transformer equation) and verify power conservation I_p V_p = I_s V_s.
- Teardown angle: Lenz's law is not a separate law — it is the negative sign in Faraday's law, which follows from energy conservation. If the sign were positive, you could create energy by moving a magnet — which would violate the first law of thermodynamics.
- Exclusions: Self-inductance derivation, eddy currents, mutual inductance coupling coefficient.
- Score: 8/10

---

## Candidate 06 — Plot the Charging and Discharging of a Capacitor in an RC Circuit with Claude

- Source: physics-plus-one-electromagnetism/chapters/05-capacitance-dielectrics.md
- Lane: BUILD (Claude Code)
- Hook: Every time you take a photo, a capacitor in your camera flash discharges in milliseconds. Every time your phone screen dims, an RC circuit controls the fade. The time constant τ = RC is the single number that governs both — and it emerges from the simplest first-order ODE.
- The artifact: A D3 animation of an RC circuit charging and discharging. A voltage source V₀ charges a capacitor C through a resistor R. The charge Q(t) = CV₀(1 − e^(−t/RC)) and current I(t) = (V₀/R)e^(−t/RC) animate live. Sliders for R (1 kΩ to 1 MΩ), C (1 nF to 1000 µF), and V₀. A switch button toggles between charging and discharging. A log-scale plot shows the exponential decay, with the time constant τ marked. The "five time constants" rule (99.3% complete) is illustrated.
- Prompt seed: `claude "Build a D3 v7 single-file HTML RC circuit charging/discharging simulator. Show: circuit diagram (switch, V₀, R, C), Q(t)=C·V₀·(1-exp(-t/τ)) and I(t)=(V₀/R)·exp(-t/τ) where τ=RC. Sliders: R (1kΩ–1MΩ), C (1nF–10mF), V₀ (1–100V). Switch between charging and discharging modes. Plots: Q(t) and I(t) on linear scale; also V_C(t) on log scale (linear for charging: shows slope=1/τ). Mark τ, 2τ, 5τ. Verify: R=10kΩ, C=100µF → τ=1s; at t=τ: Q/Q_max = 1-1/e = 0.632."`
- Read / check: τ = 10,000 × 100×10⁻⁶ = 1.0 s. At t=τ: Q/Q_max = 1−e⁻¹ = 0.6321. At t=5τ: Q/Q_max = 1−e⁻⁵ = 0.9933 (99.3%). Discharging: Q(t) = Q₀e^(−t/τ); same τ. Log plot of V_C during discharge: ln(V_C) = −t/τ + ln(V₀) → straight line with slope −1/τ. Verify slope matches −1/RC.
- Human supplies: Nothing — fully synthetic. Analytic solution to the RC ODE.
- Output medium: d3 (animated, single HTML file)
- The change: Add an RLC circuit: replace the discharging phase with an LC oscillator (R→0 limit). Show the oscillating charge Q(t) = Q₀cos(ω₀t) where ω₀ = 1/√(LC). Then add R back and show underdamped, critically damped, and overdamped regimes.
- Teardown angle: The time constant τ = RC is the characteristic timescale for exponential processes — the same mathematical form appears in radioactive decay, population growth, Newton's cooling, and photon statistics. The RC circuit is the simplest physical system that teaches this universal behavior.
- Exclusions: Impedance in the complex plane, Q-factor of resonance, op-amp integrators.
- Score: 8/10

---

## Candidate 07 — Build a Maxwell's Equations Divergence and Curl Visualizer with Claude

- Source: physics-plus-one-electromagnetism/chapters/11-maxwells-equations.md
- Lane: BUILD (Claude Code)
- Hook: Maxwell's four equations, written in differential form, look terrifying. But ∇·E = ρ/ε₀ just means "field lines start and end on charges," and ∇×B = μ₀J + μ₀ε₀∂E/∂t just means "current and changing electric fields create magnetic circulation." Build the visual proof of all four.
- The artifact: A D3 four-panel visualization: each panel shows one of Maxwell's equations. (1) ∇·E: a charge with field lines, with a Gaussian surface showing net outward flux = Q/ε₀. (2) ∇·B = 0: magnetic dipole field lines, any closed surface shows zero net flux (no magnetic monopoles). (3) ∇×E = −∂B/∂t: a changing B field (sinusoidal, slider-controlled) induces circulating E field lines — Faraday's law. (4) ∇×B = μ₀J + μ₀ε₀∂E/∂t: a current-carrying wire with B field lines circulating.
- Prompt seed: `claude "Build a D3 v7 single-file HTML four-panel Maxwell's equations visualizer. Panel 1 (∇·E=ρ/ε₀): point charge, field lines, Gaussian surface, net flux readout. Panel 2 (∇·B=0): magnetic dipole, any drawn surface → flux=0 indicator. Panel 3 (∇×E=-∂B/∂t): animated sinusoidal B(t) inside a circle (slider ω), induced E field arrows circulating (Faraday); E magnitude ∝ dB/dt. Panel 4 (∇×B=μ₀J): straight wire (I slider), B arrows circulating in right-hand-rule direction; Amperian loop showing ∮B·dl = μ₀I. All panels labeled with equation."`
- Read / check: Panel 1: ∮E·dA = Q/ε₀. At Q=1 µC: Φ = 1.13×10⁵ V·m. Field lines radiate outward. Panel 2: draw any closed surface around a dipole → count field lines entering = exiting → net = 0. Panel 3: dB/dt = Bω cos(ωt) → E_induced = r×dB/dt / 2 (Faraday's law in differential form). Panel 4: ∮B·dl = μ₀I → B = μ₀I/(2πr) at radius r.
- Human supplies: Nothing — fully synthetic.
- Output medium: d3 (animated, single HTML file)
- The change: Add the displacement current: show that a charging capacitor (current flowing into plates, E field building between plates) produces a magnetic field via μ₀ε₀∂E/∂t — Maxwell's correction. Without it, Ampere's law is inconsistent. With it, electromagnetic waves propagate.
- Teardown angle: Maxwell's equations are not four separate laws — they are one statement about the behavior of a single entity, the electromagnetic field. The displacement current term was Maxwell's single addition that united electricity, magnetism, and optics into one theory.
- Exclusions: Covariant formulation (Fµν), gauge invariance, quantum electrodynamics.
- Score: 8/10

---

## Candidate 08 — Simulate Electromagnetic Wave Propagation with Claude

- Source: physics-plus-one-electromagnetism/chapters/11-maxwells-equations.md, chapters/12-capstone-unified-field.md
- Lane: BUILD (Claude Code)
- Hook: Light is an oscillating electric field that creates a magnetic field that creates an electric field — self-sustaining, traveling at c = 1/√(ε₀μ₀). The speed of light drops out of Maxwell's equations with no additional assumptions. Build the traveling wave and verify c.
- The artifact: A D3 animation of a plane electromagnetic wave traveling in the +x direction: E(x,t) = E₀sin(kx−ωt)ŷ and B(x,t) = (E₀/c)sin(kx−ωt)ẑ drawn as orthogonal wave traces. The wavelength slider (1 nm to 1 m) controls k; the frequency f = c/λ is computed. A Poynting vector S = E×B/μ₀ is drawn (rightward). The speed c = ω/k is verified numerically. The electromagnetic spectrum (gamma to radio) is labeled at the appropriate wavelength positions.
- Prompt seed: `claude "Build a D3 v7 single-file HTML plane electromagnetic wave visualization. Animate E_y(x,t) = E₀·sin(2π(x/λ - t/T)) as a wave curve in 3D perspective (E in y, B in z, propagation in x). Draw B_z = E_y/c. Arrows show E and B at discrete x points, perpendicular to each other and to propagation. Sliders: λ (1nm–1m), E₀. Compute and display f=c/λ, T=1/f, k=2π/λ, ω=2πf. Show Poynting vector magnitude S=E₀²/(2μ₀c) (time-averaged intensity). Label EM spectrum at current λ. Verify: λ=550nm → visible green; c=3×10⁸ m/s verified from ω/k."`
- Read / check: For λ=550 nm: f = 3×10⁸/550×10⁻⁹ = 5.45×10¹⁴ Hz. k = 2π/550×10⁻⁹ = 1.14×10⁷ rad/m. ω = 2π×f = 3.42×10¹⁵ rad/s. Verify ω/k = 3.42×10¹⁵/1.14×10⁷ = 3×10⁸ m/s = c. E and B should be perpendicular to each other and to the propagation direction at all times. Time-averaged Poynting vector should be positive (always in +x direction).
- Human supplies: Nothing — fully synthetic. Plane wave formula analytic.
- Output medium: d3 (animated, single HTML file)
- The change: Show the derivation of c: starting from Maxwell's equations in a vacuum, the wave equation for E gives ∂²E/∂t² = (1/ε₀μ₀)∂²E/∂x². Display the wave equation and highlight where c = 1/√(ε₀μ₀) appears — the speed of light dropping out of purely electrical and magnetic constants.
- Teardown angle: Maxwell published the prediction c = 1/√(ε₀μ₀) = 3×10⁸ m/s in 1864. Fizeau had already measured the speed of light in 1849. The agreement was not a coincidence — it was the discovery that light is an electromagnetic wave. One equation unified three previously separate fields.
- Exclusions: Polarization and Fresnel coefficients, waveguide modes, nonlinear optics.
- Score: 8/10

---

## Candidate 09 — Compute the Capacitance of Any 2D Geometry Using Laplace's Equation with Claude

- Source: physics-plus-one-electromagnetism/chapters/04-electric-potential.md
- Lane: BUILD (Claude Code)
- Hook: The capacitance of a parallel-plate capacitor is textbook. But the capacitance of a cylinder inside a box, or two wires side by side, or a PCB trace above a ground plane — there's no formula. Numerical solution of Laplace's equation gives the answer for any geometry.
- The artifact: A D3 simulation that solves Laplace's equation ∇²V = 0 numerically (finite-difference relaxation) on a 2D grid with user-drawn boundary conditions: the viewer clicks to place conductors at fixed voltages. After convergence, the potential field V(x,y) is shown as a color map and as equipotential contours. The electric field E = −∇V is shown as arrows. The capacitance is computed from Q = ε₀∮E·dA (flux through a surface around the conductor).
- Prompt seed: `claude "Build a D3 v7 single-file HTML Laplace equation solver for 2D electrostatics. Grid: 80×80 cells. User places conductor pixels (click to paint) at V=+1V or V=-1V. Solve ∇²V=0 using successive over-relaxation (SOR) until convergence (max|ΔV|<10⁻⁴). Display: V(x,y) color map (blue to red), equipotential contours, E-field arrows (E=-∇V finite difference). Compute and display capacitance C = ε₀·∮E·n̂ dA/ΔV (numerical surface integral around +V conductor). Verify: parallel plates → C ≈ ε₀·A/d."`
- Read / check: Parallel plates: V varies linearly between plates (Laplace solution). E is uniform = ΔV/d. Capacitance: C = ε₀A/d. For plate width w = 40 cells, separation d = 10 cells: C/L = ε₀×40/10 = 4ε₀ per unit cell area. SOR should converge in ~100 iterations for an 80×80 grid with ω=1.9. Equipotentials should be parallel straight lines between parallel plates.
- Human supplies: Nothing — fully synthetic. Finite-difference Laplace solver in JavaScript.
- Output medium: d3 (animated, single HTML file)
- The change: Draw a coaxial cable cross-section (circular outer conductor, circular inner conductor) and compute C per unit length. Compare to the analytic result C/L = 2πε₀/ln(b/a). The numerical and analytic answers should agree within a few percent.
- Teardown angle: Laplace's equation has no free charges — it is the potential equation in empty space between conductors. The uniqueness theorem guarantees that specifying V on all boundaries uniquely determines V everywhere inside. The numerical method just finds that unique solution by relaxation.
- Exclusions: Poisson's equation (ρ≠0), method of images, multipole expansion.
- Score: 7/10

---

## Candidate 10 — Build an AC RLC Resonance and Phasor Diagram Simulator with Claude

- Source: physics-plus-one-electromagnetism/chapters/07-dc-circuits.md
- Lane: BUILD (Claude Code)
- Hook: At resonance, the capacitor's impedance and the inductor's impedance exactly cancel — and the current is limited only by the resistance. Your AM radio tunes to a station by adjusting a capacitor until the RLC circuit resonates at exactly the station's frequency. Build it.
- The artifact: A D3 interactive RLC circuit with an AC source. The phasor diagram animates: V_R (in phase with I), V_L (leading I by 90°), V_C (lagging I by 90°) as rotating vectors. The total impedance Z = √(R² + (ωL − 1/ωC)²) is computed. Amplitude |I| = V₀/Z and phase φ = arctan((ωL−1/ωC)/R) animate live. A frequency sweep panel plots |I(f)| — the resonance peak at f₀ = 1/(2π√(LC)) with width determined by Q = ω₀L/R.
- Prompt seed: `claude "Build a D3 v7 single-file HTML AC RLC resonance simulator. Sliders: R (1–1000 Ω), L (1mH–1H), C (1nF–10mF), V₀ (1–10V), f (1Hz–10MHz). Compute: Z = sqrt(R² + (ωL - 1/(ωC))²), I_max = V₀/Z, phase φ = atan((ωL - 1/(ωC))/R). Animate: (1) phasor diagram with rotating V_R, V_L, V_C vectors, (2) frequency sweep: plot |I(f)| from f=0.01f₀ to 10f₀ (log scale), (3) resonance markers f₀ = 1/(2π√(LC)), Q = ω₀L/R. Verify: at f=f₀, Z=R (pure resistive), |I|=V₀/R (maximum)."`
- Read / check: f₀ = 1/(2π√(LC)). At resonance: ωL = 1/ωC → they cancel → Z = R → I_max = V₀/R. Q = ω₀L/R = bandwidth: higher Q → sharper resonance. For R=100Ω, L=1mH, C=1µF: f₀ = 1/(2π√(10⁻³×10⁻⁶)) = 1/(2π×10⁻⁴·⁵) = 5033 Hz. Phase angle φ: below f₀ → capacitive (φ<0), above → inductive (φ>0). At f₀: φ=0 (current in phase with voltage).
- Human supplies: Nothing — fully synthetic. Phasor algebra analytic.
- Output medium: d3 (animated, single HTML file)
- The change: Add an AM radio tuning demo: fix the source frequency to 1000 kHz (AM band). Show that by adjusting C, the circuit resonates at different frequencies — find the C value that selects exactly 1000 kHz. This is the physical mechanism of radio tuning.
- Teardown angle: Resonance in an RLC circuit is the electrical analog of a mechanical resonance (mass-spring-damper). The same equations govern both systems — the only difference is variable names. Q-factor, bandwidth, phase angle — these concepts transfer unchanged between mechanical and electrical domains.
- Exclusions: Coupled resonators, filter design (Butterworth, Chebyshev), transmission line resonators.
- Score: 7/10
