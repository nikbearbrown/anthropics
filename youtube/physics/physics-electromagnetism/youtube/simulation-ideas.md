# Physics: Electromagnetism — Simulation Ideas

## Candidate 01 — Animate "Cyclotron Motion: Speed-Independent Period, Spiral Aurora"
- Source: `physics-electromagnetism/chapters/08-magnetism-magnetic-force.md`
- Topic: Charged Particle Motion in a Magnetic Field
- Lane: MANIM (directed animation)
- Hook: Double the speed of a proton in a magnetic field. The radius of its circle doubles — but the time around the loop stays identical. That speed-independence is the entire engineering principle behind the cyclotron, and it is far from obvious.
- The rule: Lorentz magnetic force provides centripetal acceleration: qvB = mv²/r, so r = mv/(qB). Period T = 2πr/v = 2πm/(qB) — independent of v. Cyclotron frequency ω_c = qB/m = constant. Adding a velocity component parallel to B: helical pitch = v_∥ × T.
- Concrete numbers: Proton in B = 0.50 T: m = 1.67×10⁻²⁷ kg, q = 1.60×10⁻¹⁹ C. ω_c = qB/m = (1.60×10⁻¹⁹ × 0.50)/(1.67×10⁻²⁷) = 4.79×10⁷ rad/s, T = 131 ns. At v = 1.0×10⁶ m/s: r = mv/(qB) = 2.09 cm. At v = 2.0×10⁶ m/s: r = 4.18 cm — radius doubled, T unchanged. Aurora at Earth (B ≈ 5×10⁻⁵ T, proton 1 MeV): r ≈ 140 km, T ≈ 1.3 ms.
- The artifact / what moves: A proton enters a uniform B field (field vectors shown as dots into screen). It curves into a circle. A period timer ticks. Then a second proton enters at 2× speed — its radius doubles immediately, but the period timer stays synchronized. Both complete laps in T = 131 ns. Third scene: v_∥ component added — the particle screws into a helix along the B field line. The pitch (distance per revolution) grows with v_∥ while ω_c stays constant. Final scene: zoom out to Earth's dipole field — helix spirals from pole to equator and back, compressing as B strengthens at the poles (magnetic mirror effect visible in the shrinking helix pitch).
- Output medium: Manim (mp4)
- Two testable predictions: P1: At B = 0.50 T, T_proton = 2πm_p/(qB) = 131 ns exactly; doubling B to 1.00 T halves T to 65.5 ns — the simulation period counter must agree to four significant figures. P2: The radius ratio at v₁ = 1.0×10⁶ m/s vs v₂ = 3.0×10⁶ m/s is exactly 3.00 (r ∝ v for fixed B, m, q); r₁ = 2.09 cm, r₂ = 6.27 cm — the trajectory arcs must be in exactly a 1:3 radius ratio.
- The change: Raise v until the proton is relativistic (v ≈ 0.9c). Now m → γm; ω_c = qB/(γm) falls — the particle spirals outward AND slows its angular frequency. This is the isochronous cyclotron problem that synchrocyclotrons solve by modulating B.
- Human supplies (Claude can't): Nothing — fully synthetic/analytic; all parameters are standard physical constants and published Earth-field values.
- Teardown angle: The cyclotron works because T = 2πm/qB has no v in it. Engineers exploit that: a fixed RF frequency matches every orbit regardless of energy, up to relativistic corrections. When γ kicks in, the machine breaks — and fixing it took a decade of accelerator physics. The formula predicts its own failure condition.
- Exclusions: Synchrotron radiation; full relativistic treatment; derivation of Lorentz force from Maxwell; drift motion in crossed E and B fields.
- Sim slug: em-cyclotron-motion
- Score: 9/10

## Candidate 02 — Animate "Faraday's Law: Motional EMF Rod-on-Rails — Mechanical Power Equals Electrical Power"
- Source: `physics-electromagnetism/chapters/10-electromagnetic-induction.md`
- Topic: Faraday's Law and Electromagnetic Induction
- Lane: MANIM (directed animation)
- Hook: A rod slides along rails at constant velocity. The voltage it generates drives current through a resistor. You push harder to maintain speed. Mechanical power in equals electrical power out — exactly. The law of induction is a live energy conservation proof, not just a formula.
- The rule: Motional EMF: ε = BLv (rod length L, field B, velocity v). Current: I = ε/R = BLv/R. Braking force on rod: F_B = BIL = B²L²v/R. Power balance: P_mech = F_B × v = B²L²v²/R = ε²/R = P_elec. Lenz's law: induced current opposes the change (braking).
- Concrete numbers: B = 0.50 T, L = 0.30 m, R = 2.0 Ω. Pulling at v = 4.0 m/s: ε = 0.50 × 0.30 × 4.0 = 0.600 V. I = 0.600/2.0 = 0.300 A. F_B = BIL = 0.50 × 0.300 × 0.30 = 0.0450 N. P_mech = 0.0450 × 4.0 = 0.180 W. P_elec = I²R = (0.300)²(2.0) = 0.180 W. At v = 8.0 m/s: P scales as v² → 4 × 0.180 = 0.720 W both sides.
- The artifact / what moves: Two parallel rails in a uniform B field (arrows pointing up). A rod slides to the right at v = 4.0 m/s — pulled by an applied force arrow. Current arrows appear in the circuit as the rod moves; a resistor heats up (color-coded). Real-time readouts: ε (volts), I (amps), F_braking, P_mech, P_elec. Both power readouts display side by side — always equal. Then v ramps up: P_mech and P_elec both climb quadratically in lockstep. The applied force also rises (∝ v) while the rod speed stays constant — more effort needed to maintain the same velocity as speed increases.
- Output medium: Manim (mp4)
- Two testable predictions: P1: At v = 4.0 m/s, P_mech = P_elec = 0.180 W; at v = 8.0 m/s, both = 0.720 W — a factor of 4.00 for a factor of 2.00 in v; simulation must verify this quadratic scaling. P2: The braking force at v = 4.0 m/s is F_B = B²L²v/R = 0.0450 N; if R is halved to 1.0 Ω, F_B doubles to 0.0900 N and P_elec still equals P_mech — the simulation must show this resistor-halving test.
- The change: Remove the external applied force. Let the rod decelerate freely under magnetic braking. Show v(t) = v₀ e^(−B²L²t/(mR)) — an exponential decay. The rod asymptotically approaches rest; total electrical energy dissipated equals ½mv₀².
- Human supplies (Claude can't): Nothing — fully synthetic/analytic; all parameters chosen to produce clean round-number outputs.
- Teardown angle: Every generator ever built is just a conductor moving through a magnetic field. The efficiency debates — friction, winding resistance, eddy currents — are all ways that P_mech is not fully converted. The rod-on-rails sim is the ideal limit: 100% conversion, zero leakage. Reality is measured against this baseline.
- Exclusions: Derivation of Faraday's law from first principles; AC generation with rotating coil; mutual inductance; transformer design.
- Sim slug: em-motional-emf-rails
- Score: 9/10

## Candidate 03 — Animate "AC Generator: Rotating Coil Produces Sinusoidal EMF"
- Source: `physics-electromagnetism/chapters/10-electromagnetic-induction.md`
- Topic: Electromagnetic Induction — AC Generation
- Lane: MANIM (directed animation)
- Hook: A square coil rotates in a uniform magnetic field. The flux is a cosine; its derivative is a sine; the voltage output is sinusoidal. The shape of AC electricity follows directly from the geometry of rotation — and the simulation makes the connection visible.
- The rule: Magnetic flux: Φ_B = NBAcos(ωt). EMF by Faraday's law: ε = −dΦ_B/dt = NBAω sin(ωt) = ε_max sin(ωt). Peak EMF: ε_max = NBAω. Power delivered to load R: P = ε²/(2R) = ε_max²/(2R) (RMS value: ε_rms = ε_max/√2).
- Concrete numbers: N = 200 turns, B = 0.150 T, A = 0.100 m² (coil 0.316 m × 0.316 m). Rotating at ω = 2π × 60 Hz = 377 rad/s. ε_max = 200 × 0.150 × 0.100 × 377 = 1,131 V ≈ 1.13 kV. ε_rms = 1,131/√2 = 800 V. For US standard 120 V rms: ε_max = 170 V, requires ω or N or BA adjustment. Time period T = 1/60 = 16.7 ms.
- The artifact / what moves: Left panel: the coil rotates in a uniform B field — the flux arrow (Φ = NBA cosθ) projects onto the coil face, growing and shrinking as the coil turns. Right panel: the EMF vs t curve draws in real time, lagging the flux by 90°. The curve is a pure sine. At θ = 0° (coil parallel to B): flux is zero, EMF is maximum; at θ = 90° (coil perpendicular to B): flux is maximum, EMF is zero. Annotations sync: "maximum EMF here" fires exactly when the coil plane aligns with B. An rms bar appears horizontally at ε_max/√2.
- Output medium: Manim (mp4)
- Two testable predictions: P1: EMF is zero exactly when flux is maximum (θ = 90°, coil perpendicular to B) and maximum when flux is zero (θ = 0°, coil parallel to B); these four crossover moments must align perfectly between the rotating coil animation and the sine-curve plot. P2: ε_max = NBAω; doubling ω (to 120 Hz) doubles ε_max to 2,262 V — the simulation curve must scale by exactly 2.000 when frequency doubles, verifiable on the y-axis amplitude.
- The change: Add a load resistor and show power P(t) = ε²(t)/R = ε_max²sin²(ωt)/R — a sine-squared curve oscillating at 2ω, always positive. Mark the time-average ε_max²/(2R) as a flat line, demonstrating why RMS voltage is the engineering convention.
- Human supplies (Claude can't): Nothing — fully synthetic/analytic; all parameters produce exact textbook outputs.
- Teardown angle: The sinusoidal shape of AC electricity isn't a design choice — it's the derivative of a cosine. Rotate uniformly, and sine output is unavoidable. The 60 Hz standard exists because that ω produces 120 V rms with reasonable coil dimensions; the frequency is set by the physics of practical generators, not vice versa.
- Exclusions: Three-phase generation; transformer step-up/step-down; alternator vs DC generator; slip rings vs commutators.
- Sim slug: em-ac-generator
- Score: 9/10

## Candidate 04 — Animate "Gauss's Law Symmetry: One Equation, Three Field Geometries"
- Source: `physics-electromagnetism/chapters/03-gauss-law.md`
- Topic: Gauss's Law and Electric Field Symmetry
- Lane: MANIM (directed animation)
- Hook: Surround a charged sphere with a surface. Surround a charged line. Surround a charged plane. The same equation — ∮E·dA = Q_enc/ε₀ — gives completely different field laws for each geometry. The symmetry of the charge is encoded in the field falloff.
- The rule: ∮E·dA = Q_enc/ε₀. Spherical: E(4πr²) = Q/ε₀ → E = Q/(4πε₀r²) = kQ/r² (1/r² falloff). Cylindrical: E(2πrL) = λL/ε₀ → E = λ/(2πε₀r) (1/r falloff). Planar: E(2A) = σA/ε₀ → E = σ/(2ε₀) (no falloff — uniform everywhere).
- Concrete numbers: Q = 10 nC point charge: E at r = 0.10 m is kQ/r² = (8.99×10⁹)(10⁻⁸)/(0.01) = 8,990 N/C. At r = 0.20 m: 2,248 N/C (factor of 4 drop for factor of 2 radius). Infinite line, λ = 100 nC/m: E at r = 0.10 m = (100×10⁻⁹)/(2π×8.85×10⁻¹²×0.10) = 17,985 N/C. At r = 0.20 m: 8,993 N/C (factor of 2 drop). Infinite plane, σ = 10 μC/m²: E = σ/(2ε₀) = 565,000 N/C everywhere — independent of distance.
- The artifact / what moves: Three side-by-side Gaussian surface animations. Sphere case: a transparent sphere expands around a point charge; E-field arrows maintain 1/r² spacing outward. Cylinder case: transparent cylinder around a line charge; E-arrows at 1/r spacing. Plane case: pillbox straddles the sheet; E-arrows point away from both faces at constant length regardless of height — flat field, unchanged as the pillbox grows. A log-log E vs r graph plots all three simultaneously: slopes −2 (sphere), −1 (cylinder), 0 (plane). The three lines diverge visibly.
- Output medium: Manim (mp4)
- Two testable predictions: P1: Sphere E at r = 0.20 m / E at r = 0.10 m = (0.10/0.20)² = 0.250; cylinder ratio at same radii = 0.10/0.20 = 0.500; plane ratio = 1.000 — all three ratios must be displayed and verified. P2: On a log-log plot, the slope of the sphere field is exactly −2.000, cylinder is exactly −1.000, and plane is exactly 0.000; the simulation must draw three straight lines with those slopes over at least one decade of r.
- The change: Replace the infinite line with a finite rod of length L. The 1/r falloff only holds near the center (r ≪ L); at r ≫ L it transitions to 1/r². Animate the crossover — the curve smoothly bends from slope −1 to slope −2 as the rod starts to look like a point charge.
- Human supplies (Claude can't): Nothing — fully synthetic/analytic; three idealized geometries with exact Gaussian surface calculations.
- Teardown angle: The three field laws aren't three separate discoveries — they're one law applied to three symmetries. The falloff is encoded in how many dimensions the field can spread into: 2D for a sphere (1/r²), 1D for a cylinder (1/r), 0D for a plane (constant). Symmetry is doing all the work.
- Exclusions: Derivation of Gauss's law from Coulomb's law; finite-charge distributions; electric field inside conductors (separate topic); dielectrics.
- Sim slug: em-gauss-three-symmetries
- Score: 9/10

## Candidate 05 — Animate "Dipole Field Falloff: 1/r³ vs Monopole 1/r²"
- Source: `physics-electromagnetism/chapters/02-electric-field.md`
- Topic: Electric Dipole and Multipole Hierarchy
- Lane: MANIM (directed animation)
- Hook: A single charge's field reaches across the room. A dipole's field — two opposite charges separated by a tiny gap — fades eight times faster when you double the distance. Add more charges to cancel the dipole and it fades even faster. The hierarchy of field falloff is the story of how charge distributions hide from each other at large distances.
- The rule: Monopole: E = kq/r², falls as 1/r². Dipole (on axis, r ≫ d): E ≈ 2kp/r³, falls as 1/r³, where p = qd (dipole moment). Quadrupole: E ∝ 1/r⁴. Each additional cancellation adds one power to the falloff. Water molecule: p = 6.17×10⁻³⁰ C·m — a permanent dipole with ≈0.6 electron charge at 0.1 nm separation.
- Concrete numbers: q = 1.0 nC, d = 0.010 m (dipole), so p = 10⁻¹¹ C·m. Monopole at r = 0.10 m: E = kq/r² = 900 N/C. Monopole at r = 0.20 m: 225 N/C (4× drop). Dipole on-axis at r = 0.10 m: E ≈ 2kp/r³ = 2×(8.99×10⁹)×(10⁻¹¹)/(10⁻³) = 180 N/C. Dipole at r = 0.20 m: 22.5 N/C (8× drop for 2× distance — that extra power of 1/r). Ratio dipole/monopole at r = 0.10 m: 180/900 = 0.2 — the partial cancellation suppresses the far-field immediately.
- The artifact / what moves: A log-log E vs r plot with three curves drawing simultaneously: monopole (slope −2), dipole (slope −3), quadrupole (slope −4). Below, the corresponding charge arrangements animate: a single charge → two opposite charges separated by d → four charges in a square. As the view zooms out (r increases), the monopole curve stays highest, dipole falls faster, quadrupole fastest — the hierarchy separates visibly on the log-log scale. At r = 1.0 m, monopole is 9 N/C, dipole is 0.018 N/C — a factor of 500 suppression from partial cancellation alone.
- Output medium: Manim (mp4)
- Two testable predictions: P1: Dipole E at r = 0.10 m / E at r = 0.20 m = (0.20/0.10)³ = 8.00; at r = 0.30 m, E = 2kp/(0.027) = 6.66 N/C — ratio E(0.10)/E(0.30) = 180/6.66 = 27.0 = 3³; the simulation must show this ratio to 3 significant figures. P2: On the log-log plot, the dipole slope is exactly −3.000 and the monopole slope is exactly −2.000; the two lines must be parallel on linear scale (same shape, different offset) and diverge by one slope unit on log-log; crossing occurs near r = d/2 where near-field terms dominate.
- The change: Add the perpendicular-axis dipole field: E_perp ≈ kp/r³ (half the on-axis value, pointing opposite direction). Show how the full dipole field pattern — the classic four-lobed flower — is traced by combining both. The field line geometry emerges from superposition.
- Human supplies (Claude can't): Nothing — fully synthetic/analytic; all parameters chosen to yield clean round-number ratios.
- Teardown angle: Molecules don't care about your single-charge field — they interact primarily through dipole-dipole forces (van der Waals) because individual charges cancel. The faster a field falls, the less it reaches. Chemistry is dominated by dipole and quadrupole terms precisely because the monopole contribution is zero for neutral molecules.
- Exclusions: Full multipole expansion derivation; torque on a dipole in an external field; magnetic dipole analogy; quantum mechanical permanent dipoles.
- Sim slug: em-dipole-falloff
- Score: 8/10

## Candidate 06 — Animate "Maxwell's EM Wave: E ⊥ B ⊥ Propagation, c Emerges from Two Constants"
- Source: `physics-electromagnetism/chapters/11-maxwells-equations.md`
- Topic: Maxwell's Equations and Electromagnetic Waves
- Lane: MANIM (directed animation)
- Hook: Maxwell added one extra term to Ampere's law — the displacement current. From that single correction, a wave equation fell out with a speed fixed entirely by two measurable constants: ε₀ from electrostatics, μ₀ from magnetostatics. The predicted speed was the speed of light. Nobody expected that.
- The rule: Wave equation: ∂²E/∂x² = μ₀ε₀ ∂²E/∂t². Speed: c = 1/√(μ₀ε₀) = 1/√((8.85×10⁻¹²)(4π×10⁻⁷)) = 3.00×10⁸ m/s. Plane wave: E = E₀ sin(kx − ωt) ŷ; B = B₀ sin(kx − ωt) ẑ. E ⊥ B ⊥ propagation. E₀/B₀ = c. Energy: S = (1/μ₀)E × B (Poynting vector).
- Concrete numbers: Visible light at λ = 550 nm (green): f = c/λ = 5.45×10¹⁴ Hz, ω = 3.42×10¹⁵ rad/s, k = 1.14×10⁷ m⁻¹. E₀ = 1,000 V/m (typical sunlight): B₀ = E₀/c = 3.33×10⁻⁶ T = 3.33 µT. Intensity I = E₀²/(2μ₀c) = 1.33×10³ W/m² (matches solar constant at 1 AU). Radio wave λ = 1.0 m (300 MHz): same structure, frequency 1.8×10¹² times lower — same E₀/B₀ = c relation holds.
- The artifact / what moves: A 3D wave packet propagates to the right. The E-field oscillates vertically (ŷ), drawn as a sinusoidal ribbon in blue. The B-field oscillates horizontally (ẑ), drawn in red, phase-locked 90° ahead. The two ribbons are mutually perpendicular and perpendicular to the propagation direction. A third vector (k̂) arrows along the direction of travel. The amplitude of E is labeled 1,000 V/m; the amplitude of B is labeled 3.33 µT; their ratio is marked = c = 3×10⁸ m/s. A frozen frame reveals the E × B Poynting vector pointing forward. A second scene changes λ from visible (550 nm) to radio (1 m) — the wave slows down visually to show fewer oscillations in the same window, but E₀/B₀ stays exactly c.
- Output medium: Manim (mp4)
- Two testable predictions: P1: At any wavelength, E₀/B₀ = c = 2.998×10⁸ m/s exactly; the simulation must display both amplitudes and their ratio; for E₀ = 1,000 V/m the B₀ annotation must read 3.336 µT to four significant figures. P2: The speed of propagation c = 1/√(μ₀ε₀); substituting μ₀ = 4π×10⁻⁷ T·m/A and ε₀ = 8.854×10⁻¹² F/m gives c = 2.998×10⁸ m/s — the simulation must display this derivation numerically in a side panel, verifying the same value as the measured speed of light to four significant figures.
- The change: Add polarization: rotate the E-field direction. Show linear → circular polarization as a 90° phase shift is added between Ex and Ey components. The B-field rotates correspondingly; the Poynting vector stays along k̂ throughout.
- Human supplies (Claude can't): Nothing — fully synthetic/analytic; all parameters derive from the two fundamental constants.
- Teardown angle: Maxwell didn't discover the speed of light — he predicted it from measurements of static fields made in labs by Coulomb and Ampere, who had no idea about light. The displacement current correction is a one-line fix to Ampere's law; the fact that c = 1/√(μ₀ε₀) emerges from that fix is among the most surprising results in all of physics.
- Exclusions: Full derivation of all four Maxwell equations; gauge freedom; near-field vs far-field radiation; polarization filters; relativity of electromagnetic fields.
- Sim slug: em-maxwell-wave
- Score: 9/10

## Candidate 07 — Animate "Electric Potential: Equipotential Surfaces and E = −∇V"
- Source: `physics-electromagnetism/chapters/04-electric-potential.md`
- Topic: Electric Potential and Field Relationship
- Lane: MANIM (directed animation)
- Hook: The electric field and the potential describe the same physics twice, in two different languages. Every field line crosses every equipotential at exactly 90°. Draw the contours; the field arrows emerge perpendicular to them. The gradient is a machine that converts one representation into the other.
- The rule: V = kq/r for a point charge. E = −∇V; in 1D: E_x = −dV/dx. Equipotential surfaces are surfaces of constant V; field lines are perpendicular to these surfaces (since E · dl = 0 along equipotentials). Work done moving charge q along an equipotential: W = 0 (ΔV = 0). Energy released/stored: U = qΔV = q(V_f − V_i).
- Concrete numbers: q = 5.0 µC point charge. V at r = 0.10 m: kq/r = (8.99×10⁹)(5×10⁻⁶)/(0.10) = 450,000 V = 450 kV. At r = 0.20 m: 225 kV. At r = 0.50 m: 90 kV. E at r = 0.10 m: 4.50 MV/m. E = −dV/dr = −(−kq/r²) = kq/r². Moving a charge Q = 1 µC from r = 0.20 m to r = 0.10 m: W = QΔV = (10⁻⁶)(450−225)×10³ = 0.225 J.
- The artifact / what moves: A central positive charge generates visible equipotential contours (concentric circles) in 2D — labeled 450 kV, 225 kV, 90 kV, etc. (V ∝ 1/r spacing). As each contour draws in, field lines sprout perpendicular to it, radiating outward. A cursor moves along an equipotential — the work readout stays at zero throughout the path. Then the cursor moves inward, crossing equipotentials: work readout climbs proportional to ΔV. A second scene: two point charges (dipole). The equipotentials become non-circular; the field lines remain perpendicular to every contour at the crossing point — confirmed by a small perpendicularity marker.
- Output medium: Manim (mp4)
- Two testable predictions: P1: Moving a 1 µC test charge from the 225 kV surface to the 450 kV surface requires W = QΔV = 0.225 J regardless of path taken (any two paths shown must give identical energy readout); P2: The gradient E = −dV/dr for V = kq/r gives E = kq/r²; at r = 0.10 m, dV/dr = −kq/r² = −4.50×10⁶ V/m, so E = +4.50×10⁶ V/m (pointing outward); the simulation must verify E = 4.50 MV/m at that radius from the potential contour spacing alone.
- The change: Switch to a parallel-plate capacitor: V varies linearly between the plates, equipotentials are parallel planes, E is uniform and perpendicular to the plates. The contrast with the point-charge case — curved vs flat equipotentials — makes the gradient-field relationship geometrically vivid.
- Human supplies (Claude can't): Nothing — fully synthetic/analytic; point charge and parallel plate geometries are exact.
- Teardown angle: Potential is the scalar field; the electric field is its gradient. Engineers almost always work in potential because it adds as a scalar — no direction required. The field is derived from V, not the other way around. That's why circuit analysis uses voltage (V) rather than field (E/m).
- Exclusions: Derivation of work integral; Poisson's equation; capacitance calculation; dielectric effects; numerical methods for non-symmetric distributions.
- Sim slug: em-equipotentials-gradient
- Score: 8/10

## Candidate 08 — Animate "Mass Spectrometer: Radius Separates Particles by m/q"
- Source: `physics-electromagnetism/chapters/08-magnetism-magnetic-force.md`
- Topic: Magnetic Force and the Mass Spectrometer
- Lane: MANIM (directed animation)
- Hook: Two ions enter a magnetic field at identical velocities. One lands 2 cm farther along the detector. That 2 cm measurement tells you the mass difference to four decimal places. The entire periodic table was mapped this way, one isotope at a time.
- The rule: Ion enters at velocity v selected by a velocity selector (E = vB: only particles with v = E/B pass). In analysis chamber: qvB = mv²/r → r = mv/(qB). For ions with same q and v, r ∝ m. Landing position x = 2r = 2mv/(qB). Mass difference Δm/m = Δx/x. Resolution: R = m/Δm = x/(2Δx).
- Concrete numbers: B = 0.500 T (analysis), v = 2.00×10⁵ m/s (from velocity selector E = 1.00×10⁵ V/m, B_sel = 0.500 T). Neon-20 (m = 20 u = 3.32×10⁻²⁶ kg, q = e): r₂₀ = mv/(qB) = (3.32×10⁻²⁶ × 2×10⁵)/(1.60×10⁻¹⁹ × 0.500) = 0.0828 m = 8.28 cm. Landing at x₂₀ = 16.56 cm. Neon-22 (m = 22 u = 3.65×10⁻²⁶ kg): r₂₂ = 9.11 cm, x₂₂ = 18.22 cm. Separation: Δx = 1.66 cm — easily resolved. Uranium-235 vs -238: Δx/x = 3/235 = 1.28% → Δx ≈ 2 mm at typical detector scales.
- The artifact / what moves: A velocity selector filters ions at the left: crossed E and B fields, only v = E/B survives. Ions enter a curved analysis chamber (B into page). Two arcs of different radii draw simultaneously — ²⁰Ne curves tightly, ²²Ne curves wider. Both arcs terminate on a detector strip. The landing positions are marked and the separation Δx = 1.66 cm is labeled. A mass readout appears at each landing spot: 20.00 u and 22.00 u — derived from the arc radius and the known q, B, v. A third scene: sweep B from 0.3 to 0.8 T and watch both landing spots shift inward as B increases (r ∝ 1/B), but their separation shrinks proportionally.
- Output medium: Manim (mp4)
- Two testable predictions: P1: r(²²Ne)/r(²⁰Ne) = 22/20 = 1.100 exactly; the ratio of the two arc radii in the simulation must equal 1.100 to three significant figures; landing positions x₂₀ = 16.56 cm and x₂₂ = 18.22 cm must match. P2: Doubling B from 0.500 to 1.000 T halves both radii (r ∝ 1/B): r₂₀ drops from 8.28 to 4.14 cm; x₂₀ from 16.56 to 8.28 cm — the simulation must show this 2× compression, and the proportional separation (ratio Δx/x₂₀ = (22−20)/20 = 0.100) must remain constant regardless of B.
- The change: Add a third ion at the same charge but half the mass (¹⁰Be, q = +e): its radius is half that of ²⁰Ne. Show that the instrument's resolving power R = m/Δm is set by the detector pixel size, not the magnetic field strength — finer position resolution, not stronger B, is what separates close-mass isotopes.
- Human supplies (Claude can't): Nothing — fully synthetic/analytic; all data from standard isotope mass tables.
- Teardown angle: The mass spectrometer is the instrument that proved isotopes exist. Before it, "neon" was assumed to be a single element. After 1913, Thomson's parabola method and Aston's mass spectrograph showed two neon landing spots. Geometry and a magnetic field did what chemistry could not: separate atoms by mass.
- Exclusions: Ion source design; time-of-flight alternatives; chemical ionization methods; full isotope abundance tables; quadrupole MS.
- Sim slug: em-mass-spectrometer
- Score: 8/10

## Candidate 09 — Animate "Faraday Cage: E = 0 Inside a Conductor — From Gauss's Law"
- Source: `physics-electromagnetism/chapters/03-gauss-law.md`
- Topic: Conductor in Electrostatic Equilibrium
- Lane: MANIM (directed animation)
- Hook: A metal shell has zero electric field inside, regardless of what's outside. This isn't a material property of metal — it's a consequence of Gauss's law. Every free charge that needs to move does, until the internal field is exactly zero. The equilibrium is the law.
- The rule: Inside a conductor at equilibrium: E_internal = 0 (otherwise free charges would move). Gauss's law with a Gaussian surface inside the conductor: ∮E·dA = 0 → Q_enc = 0. All excess charge resides on the outer surface. External field is expelled from interior; any charges outside induce surface charges that cancel the interior field exactly. MRI scanner's copper shielding attenuates external RF by a factor of ~10⁸.
- Concrete numbers: Outer sphere radius R = 0.20 m, carrying charge Q = 50 nC. E at r = 0.30 m (outside): E = kQ/r² = 4,994 N/C. E at r = 0.15 m (inside the conductor shell): E = 0 exactly. If an external charge Q_ext = 100 nC is placed at r = 1.0 m, the exterior field rearranges: induced surface charge distribution appears on the shell exterior, but E inside remains 0. Induced charges: inner surface 0, outer surface = +50 nC (original) rearranged — the shape changes, total is fixed.
- The artifact / what moves: Cross-section of a conducting spherical shell. The shell is shown as a thick ring. Initial state: uniform surface charge. External uniform field switched on: field lines bend around the shell, enter the conductor from one side, are expelled inside. Inside the cavity: field lines stop at the outer surface — interior is field-free (solid black region). A Gaussian surface sweeps through the conductor: E·dA = 0 everywhere on it, confirming Q_enc = 0 inside the conductor material itself. A second scene: a point charge placed inside the cavity induces charges on the inner surface — but outside is still exactly as if the total charge were distributed on the outer surface. The field inside is due only to the trapped charge, not the exterior.
- Output medium: Manim (mp4)
- Two testable predictions: P1: When an external uniform field E₀ is applied, the field inside the cavity remains exactly 0 N/C regardless of E₀ magnitude; the simulation must show this by displaying E_interior = 0.000 N/C even as the external readout climbs from 0 to 10,000 N/C. P2: A charge Q_inner placed at the center of the cavity induces −Q_inner on the inner surface and +Q_inner appears on the outer surface; the outer-surface charge density is uniform (spherical symmetry) and produces E = kQ_inner/r² outside — identical to a point charge at the center; the simulation must verify this numerically at r = 0.30 m.
- The change: Replace the spherical shell with a mesh (gaps in the conductor). Show the attenuation factor vs mesh size: E_penetrates ∝ e^(−πd/a) where d = thickness and a = mesh spacing. At a = 1 cm, the interior field is still 99.7% shielded; at a = 10 cm, shielding drops to 73%.
- Human supplies (Claude can't): Nothing — fully synthetic/analytic; the cage geometry and field are purely mathematical.
- Teardown angle: A Faraday cage works because metal surrenders its free electrons to enforce the law. The equilibrium state — zero internal field — is a minimum energy state that the free electrons find automatically. The shielding isn't a design parameter; it's a consequence. The only question is how quickly the charges can rearrange, which is what determines shielding bandwidth.
- Exclusions: Time-varying fields and skin depth; magnetic shielding (different mechanism — mu-metal); antenna theory; quantum Hall effect.
- Sim slug: em-faraday-cage
- Score: 8/10

## Candidate 10 — Animate "Lenz's Law: The Induced Current Always Opposes the Change"
- Source: `physics-electromagnetism/chapters/10-electromagnetic-induction.md`
- Topic: Lenz's Law and Electromagnetic Induction
- Lane: MANIM (directed animation)
- Hook: Push a magnet into a coil — the coil pushes back. Pull the magnet out — the coil pulls it back. The induced current always fights the change, never helps it. This isn't a separate law; it's energy conservation wearing a magnetic mask.
- The rule: Faraday's law: ε = −dΦ_B/dt. The minus sign is Lenz's law: the induced EMF drives a current whose magnetic field opposes the change in flux. Inserting North pole → increasing flux upward → induced current creates downward B → repels magnet. Removing North pole → decreasing flux upward → induced current creates upward B → attracts magnet. Either way, work must be done by the external agent.
- Concrete numbers: Coil: N = 100 turns, A = 0.020 m², R = 5.0 Ω. Magnet moves so dB/dt = 2.0 T/s: ε = −N dΦ/dt = −N A dB/dt = −100 × 0.020 × 2.0 = −4.0 V. |ε| = 4.0 V. I = ε/R = 0.800 A. Power dissipated in coil: P = I²R = (0.800)²(5.0) = 3.2 W — all extracted from the work done pushing the magnet. EMF = 0 when magnet is stationary (dΦ/dt = 0). EMF = maximum when magnet passes through the plane of the coil (fastest flux change).
- The artifact / what moves: A bar magnet (labeled N, S) approaches a solenoid from the left. As it enters: the flux meter climbs, the induced current direction (right-hand rule) is shown by animated arrows in the wire, and a compass inside the coil shows the opposing B field. Repulsion arrows appear on the magnet and coil face. The magnet stops: current drops to zero, repulsion vanishes. The magnet exits: flux decreases, current reverses, coil now attracts the magnet (wants to maintain flux). Throughout: EMF and current readouts track dΦ/dt exactly. A power meter shows the work done by the hand pushing/pulling as equal to I²R.
- Output medium: Manim (mp4)
- Two testable predictions: P1: EMF = −N dΦ/dt; when the magnet passes through at twice the speed (dB/dt doubles), the induced EMF doubles from 4.0 to 8.0 V and the current doubles to 1.60 A — the simulation must display this 2× scaling accurately. P2: When the magnet is stationary anywhere (dΦ/dt = 0), induced EMF = 0.000 V and I = 0.000 A exactly; the simulation must display zero regardless of the magnet's position, confirming that position alone does not drive induction.
- The change: Replace the coil with a conducting ring (no resistance — a superconductor). Lenz's law in the limit R → 0: the induced current grows without bound to perfectly cancel any flux change — total flux through the ring stays constant. Show the ring levitating a magnet above it (Meissner-like expulsion).
- Human supplies (Claude can't): Nothing — fully synthetic/analytic; all parameters set to yield clean round-number outputs.
- Teardown angle: Lenz's law is energy conservation stated electromagnetically. If the induced current helped rather than opposed, you could extract unlimited energy from a moving magnet — perpetual motion. The minus sign in Faraday's law is a structural impossibility theorem: free energy cannot be conjured from induction.
- Exclusions: Derivation of Lenz's law from Maxwell's equations; eddy current braking in bulk conductors; transformer coupling; self-inductance vs mutual inductance.
- Sim slug: em-lenz-law
- Score: 9/10
