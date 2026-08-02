# Physics +1: Modern Physics (Advanced) — CLI Video Ideas ("X with Claude")

## Candidate 01 — Derive and Plot the Lorentz Factor with Claude

- Source: physics-plus-one-modern-physics/chapters/01-special-relativity.md
- Lane: BUILD (Claude Code)
- Hook: Take the two postulates. Apply Pythagoras. Out comes the Lorentz factor — and with it, the entire structure of time dilation, length contraction, and relativistic energy. The derivation is 8 lines. The consequence is that GPS satellites would miss by 11 km/day without correcting for it.
- The artifact: A D3 animation showing: (1) the light-clock geometry at velocity v — the right-triangle path of a photon with Pythagorean derivation of γ = 1/√(1−v²/c²) displayed as animated algebra steps, (2) the γ(v) curve sweeping from v=0 to v=0.999c (log x-axis), (3) a "GPS error" readout showing how many meters of positional error per day would accumulate if SR were ignored (v_satellite = 3.87 km/s → γ−1 ≈ 8.35×10⁻¹¹ → clock runs slow by 7.2 µs/day → 2.1 km error).
- Prompt seed: `claude "Build a D3 v7 single-file HTML Lorentz factor visualizer. Panel 1: animated light-clock diagram — stationary clock (vertical photon bounce) vs. moving clock (diagonal path) with Pythagorean relation Δt² = Δt₀² + (vΔt/c)², leading to γ = 1/√(1-v²/c²). Animate algebra steps. Panel 2: γ(v) curve for v/c from 0 to 0.9999 (log x-axis). Panel 3: GPS satellite (v=3.87km/s) SR time dilation = 7.2 µs/day → positional error. Verify: at v=0.866c, γ=2.000 exactly."`
- Read / check: γ = 1/√(1−(0.866)²) = 1/√(1−0.750) = 1/√0.250 = 1/0.500 = 2.000. GPS: v=3.87×10³ m/s, γ−1 ≈ v²/(2c²) = (3.87×10³)²/(2×9×10¹⁶) = 8.35×10⁻¹¹. Clock slow by Δt = 8.35×10⁻¹¹ × 86400 s = 7.2 µs/day. Position error = 7.2×10⁻⁶ × 3×10⁸ = 2160 m/day. Verify the derivation panel shows the correct Pythagorean step.
- Human supplies: Nothing — fully synthetic.
- Output medium: d3 (animated, single HTML file)
- The change: Add E = γmc²: show the relativistic kinetic energy KE = (γ−1)mc² approaching E = mc² at v→c. Plot KE/mc² vs. v/c and compare to the classical ½mv²/mc² = v²/(2c²). The curves coincide at low v but diverge dramatically near c.
- Teardown angle: The Lorentz factor is not a correction to Newtonian physics — it is the structure of spacetime itself. Time and length are not invariants; the spacetime interval s² = c²t²−x²−y²−z² is. The factor γ is just the conversion between reference frames.
- Exclusions: Minkowski diagrams, four-vectors, Lorentz group algebra.
- Score: 9/10

---

## Candidate 02 — Build a Photoelectric Effect Simulator with Claude

- Source: physics-plus-one-modern-physics/chapters/04-the-quantum-nature-of-light.md
- Lane: BUILD (Claude Code)
- Hook: Millikan spent 10 years trying to disprove Einstein's photon hypothesis by measuring the photoelectric effect. His 1916 measurements were so precise that they confirmed Einstein — and the slope of the graph gave him Planck's constant to 0.5%. Build the graph and read off h.
- The artifact: A D3 animation of the photoelectric effect: the user sets the metal (work function φ from a dropdown: cesium 2.1 eV, sodium 2.3 eV, copper 4.7 eV, gold 5.1 eV), the light frequency f, and the intensity. The stopping voltage V_stop = (hf − φ)/e is computed and displayed. A scatter plot builds up showing V_stop vs. f for multiple frequencies — the slope of the best-fit line is h/e, from which h is computed. The threshold frequency f₀ = φ/h below which no electrons emerge is marked.
- Prompt seed: `claude "Build a D3 v7 single-file HTML photoelectric effect simulator. Metal dropdown: Cs (φ=2.1eV), Na (2.3eV), Al (4.1eV), Cu (4.7eV), Au (5.1eV). Frequency slider (3×10¹⁴ to 2×10¹⁵ Hz). Compute: KE_max = hf - φ = e·V_stop (h=6.626×10⁻³⁴ J·s). Below threshold (hf<φ): no emission, V_stop=0. Show: (1) animated electron emission (dots flying off) only above threshold, (2) scatter plot V_stop vs. f for 8 frequencies; best-fit line → slope = h/e = 4.136×10⁻¹⁵ eV·s. Verify: Na, f=6.9×10¹⁴ Hz → KE=0.54eV, V_stop=0.54V."`
- Read / check: Na φ=2.3 eV. f=6.9×10¹⁴ Hz → E_photon = hf = 6.626×10⁻³⁴×6.9×10¹⁴/(1.6×10⁻¹⁹) = 2.85 eV. KE = 2.85−2.3 = 0.55 eV. V_stop = 0.55 V. Slope of V_stop vs. f line: h/e = 6.626×10⁻³⁴/1.6×10⁻¹⁹ = 4.14×10⁻¹⁵ eV·s. Millikan's measurement: h = 6.57×10⁻³⁴ J·s (0.8% from modern value).
- Human supplies: Nothing — fully synthetic. All from known work functions and Planck's constant.
- Output medium: d3 (animated, single HTML file)
- The change: Add intensity variation: at constant f (above threshold), show that increasing intensity increases the number of electrons (current) but NOT their kinetic energy. The stopping voltage stays constant — this refutes the classical wave prediction.
- Teardown angle: Millikan's measurement was the definitive proof that light is quantized. The slope of V_stop vs. f is Planck's constant divided by the electron charge — a universal constant of nature, independent of the metal or the light source. The wave model of light cannot predict this.
- Exclusions: Quantum efficiency, photodetector designs, two-photon ionization.
- Score: 9/10

---

## Candidate 03 — Compute Solar Fusion Rates with the Gamow Peak with Claude

- Source: physics-plus-one-modern-physics/chapters/03-the-sun-a-nuclear-powerhouse.md
- Lane: BUILD (Claude Code)
- Hook: The Sun's protons are too slow to classically fuse. But the Gamow peak — the product of the Maxwell-Boltzmann distribution and the tunneling probability — tells you exactly which energies contribute to fusion. At 15 million Kelvin, the Gamow peak sits at ~6 keV. Plot it and compute the fusion rate.
- The artifact: A Manim scene showing two curves on the same energy axis: (1) the Maxwell-Boltzmann distribution f_MB(E) at T = 15×10⁶ K, and (2) the tunneling probability T(E) = exp(−b/√E) where b = π α Z₁Z₂ √(2m_r) / ℏ. Their product — the Gamow factor — is plotted, showing a narrow peak at E_G = (bkT/2)^(2/3) ≈ 6 keV. The Gamow width ΔE_G is computed. Sliding the temperature from 10⁷ to 10⁸ K shows the Gamow peak shifting and the total reaction rate changing.
- Prompt seed: `claude "Using Python + NumPy + Manim, plot the Gamow peak for proton-proton fusion. E-axis: 0–50 keV. Plot: (1) Maxwell-Boltzmann distribution f(E) ∝ √E · exp(-E/kT) at T=15×10⁶K (normalized to peak=1), (2) Gamow tunneling factor G(E) = exp(-b/√E) where b = π·e²·Z1·Z2·√(2·m_r)/(ℏ·c) in appropriate units (for pp: b≈31.3 keV^(1/2)), (3) product f·G (Gamow integrand, normalized). Animate: temperature slider 10^7 to 10^8 K shifts peak. Mark E_Gamow peak and width. Display total rate integral ∝ ∫f·G dE."`
- Read / check: For pp fusion at T=1.5×10⁷ K: kT = 1.293 keV. Gamow peak E_G = (b²kT/4)^(1/3) = (31.3²×1.293/4)^(1/3) = (315.8)^(1/3) ≈ 6.8 keV. Width ΔE_G ≈ (4E_G kT/3)^(1/2) = (4×6.8×1.293/3)^(1/2) ≈ 3.4 keV. The MB peak is at ~2kT = 2.6 keV; the tunneling factor peaks at E→∞; their product peaks at E_G = 6.8 keV (a compromise).
- Human supplies: Nothing — fully synthetic. Gamow peak formula from published nuclear physics constants.
- Output medium: Manim (animated dual-curve scene with Gamow peak)
- The change: Compute the stellar nuclear reaction rate integral: S(E) factor (the astrophysical S-factor, approximately constant for the pp chain) × Gamow factor, integrated numerically. Show how the rate scales as T^4 near 15 MK — a strong temperature sensitivity that explains why stars regulate their luminosity.
- Teardown angle: The Gamow peak is not where the most particles are (the MB peak) or where tunneling is easiest (higher energies) — it's the compromise. This is the physical mechanism of stellar nucleosynthesis: the small fraction of particles at the Gamow energy, tunneling through a nearly-impenetrable barrier, is what makes stars shine.
- Exclusions: Full S-factor data, screening corrections, weak interaction matrix element.
- Score: 9/10

---

## Candidate 04 — Simulate the Bohr Model: Hydrogen Energy Levels and Transitions with Claude

- Source: physics-plus-one-modern-physics/chapters/05-the-atom.md
- Lane: BUILD (Claude Code)
- Hook: Bohr's model is wrong about almost everything — but it predicts the hydrogen spectrum exactly right. Every textbook plots the energy levels as a static diagram. Build the animated version: watch electrons jump between levels and emit photons at precisely the observed wavelengths.
- The artifact: A D3 animation of the Bohr hydrogen atom: circular Bohr orbits (n=1 to n=6, radii r_n = a₀n²), an electron dot orbiting at the current level. A "transition" button triggers the electron to jump from n_i to n_f (sliders), animating the fall with a photon (colored dot) flying off at the correct wavelength λ = 91.2 nm × n_f²n_i²/(n_i²−n_f²). The photon appears in the spectrum bar below. All 15 transitions from n=2 to n=6 can be triggered, building the complete visible + UV Balmer, Lyman, and Paschen series.
- Prompt seed: `claude "Build a D3 v7 single-file HTML Bohr model hydrogen spectrum visualizer. Show: (1) 6 concentric Bohr orbit circles (radii ∝ n²), orbiting electron dot, (2) transition selector: n_i and n_f sliders → animate electron drop, emit photon dot in color of λ = 91.2·n_i²·n_f²/(n_i²-n_f²) nm, (3) spectrum bar at bottom (UV: purple, visible: rainbow, IR: gray) showing emitted lines. Label Lyman (n_f=1), Balmer (n_f=2), Paschen (n_f=3) series. Display: E_photon, λ, series name. Verify: n=3→2 → λ=656nm (H-alpha, red)."`
- Read / check: Rydberg: E_n = −13.6/n² eV. n=3: −1.511 eV. n=2: −3.4 eV. ΔE = 1.889 eV. λ = 1240/1.889 = 656.8 nm. H-alpha in red. n=2→1: ΔE = 10.2 eV, λ = 122 nm (Lyman-α, UV). n=4→2: λ = 486 nm (blue-green). Verify all 15 inter-level transitions give the correct wavelengths to within 1 nm.
- Human supplies: Nothing — fully synthetic. All wavelengths from analytic Rydberg formula.
- Output medium: d3 (animated, single HTML file)
- The change: Add the de Broglie standing-wave interpretation: show that the n-th orbit has exactly n full wavelengths of the de Broglie electron wave. When n is not an integer, the wave doesn't close on itself — illustrating why only integer orbits are stable.
- Teardown angle: The Bohr model is a lucky accident — it gets the energy levels right for hydrogen not because its picture of electron orbits is correct (electrons don't orbit), but because its quantization condition L=nℏ happens to give the right energies. Schrödinger's equation gives the same energies from first principles.
- Exclusions: Fine structure, Lamb shift, Zeeman splitting, multi-electron atoms (the Bohr model fails for He).
- Score: 8/10

---

## Candidate 05 — Build a Nuclear Decay Chain Simulator with Bateman Equations with Claude

- Source: physics-plus-one-modern-physics/chapters/13-radioactivity-and-nuclear-physics.md
- Lane: BUILD (Claude Code)
- Hook: Uranium-238 takes 4.5 billion years to become lead through 14 steps — some lasting microseconds. The Bateman equations describe the entire chain. When the chain reaches secular equilibrium, every daughter is as active as the parent. Compute when that happens.
- The artifact: A D3 animation of the U-238 decay chain: 14 nuclides (U-238, Th-234, Pa-234, U-234, Th-230, Ra-226, Rn-222, Po-218, Pb-214, Bi-214, Po-214, Pb-210, Bi-210, Po-210, Pb-206) with their half-lives spanning 4.47 Gyr to 0.16 ms. The Bateman equations are solved numerically. Time slider spans from 0 to 1 Myr. Bar chart shows each nuclide's activity (decays/s) relative to U-238. "Secular equilibrium" is flagged when all activities within 1% of each other.
- Prompt seed: `claude "Build a D3 v7 single-file HTML U-238 decay chain simulator using the Bateman equations. Embed half-lives: U238=4.468Gyr, Th234=24.1d, Pa234=1.17min, U234=245kyr, Th230=75400yr, Ra226=1600yr, Rn222=3.82d, Po218=3.05min, Pb214=26.8min, Bi214=19.7min, Po214=164µs, Pb210=22.3yr, Bi210=5.01d, Po210=138.4d, Pb206=stable. Solve N'_i = λ_{i-1}N_{i-1} - λ_i N_i numerically. Time slider 0–10Myr (log). Bar chart: activity A_i = λ_i N_i relative to A(U238). Verify: secular equilibrium for Ra226 reached at t ~ 5×Ra_halflife = 8000 yr."`
- Read / check: Secular equilibrium: λ_i N_i = λ_{U238} N_{U238} for all i. For Ra-226 (t½=1600 yr): secular equilibrium reached at ~5×1600 = 8000 yr. Activity of Ra-226 should equal activity of U-238 at secular equilibrium. The short-lived daughters (Th-234, Po-218, etc.) reach secular equilibrium almost instantly. Pb-206 is stable → N_Pb206 accumulates; A_Pb206 = 0.
- Human supplies: Nothing — fully synthetic. Bateman equations with published half-lives.
- Output medium: d3 (animated, single HTML file)
- The change: Add a "start with pure Ra-226" scenario and watch the build-up from the parent, showing how Marie Curie's radium samples self-assembled their decay chains and grew hotter over time.
- Teardown angle: Secular equilibrium is the decay chain's steady state: every link runs at the same rate. In a freshly separated radioisotope, the chain builds up from scratch — which is why newly purified Ra-226 initially seems less radioactive than old Ra-226 that has had time to accumulate its daughters.
- Exclusions: Branching ratios, alpha vs. beta spectrum shapes, neutrino energy spectra.
- Score: 8/10

---

## Candidate 06 — Plot the de Broglie Wavelength Across Scales with Claude

- Source: physics-plus-one-modern-physics/chapters/10-quantum-physics.md
- Lane: BUILD (Claude Code)
- Hook: Every particle has a de Broglie wavelength λ = h/mv. For a baseball moving at 30 m/s, that wavelength is 10⁻³⁴ m — smaller than a proton by 10¹⁹. For a thermal neutron in a reactor, it's comparable to atomic spacing — which is why thermal neutrons diffract off crystal lattices.
- The artifact: A D3 log-log plot of de Broglie wavelength λ = h/(mv) vs. kinetic energy KE for multiple particles: electron, proton, neutron, alpha particle, and a baseball. The x-axis spans kinetic energy from 1 meV (thermal neutron) to 1 GeV (LHC proton). Reference lines mark: atomic spacing (0.1 nm), X-ray wavelengths (0.01–1 nm), nuclear radius (1 fm). A particle selector highlights where each particle's curve falls. A second panel shows electron diffraction: at what voltage V does an electron have λ = d (crystal spacing = 0.154 nm)?
- Prompt seed: `claude "Build a D3 v7 single-file HTML de Broglie wavelength visualizer. Log-log plot: x-axis KE (1meV–1GeV in eV), y-axis λ=h/√(2mKE) in meters (1fm–100nm). Draw curves for: electron (m=9.11×10⁻³¹ kg), proton (1.67×10⁻²⁷), neutron (same as proton), alpha (4×proton), baseball (0.142 kg, v=30m/s as single point). Reference lines: atomic spacing (0.154nm), DNA width (2nm), visible light (400-700nm). Label where electron diffraction (λ=d_crystal) occurs. Verify: thermal neutron (KE=25meV) → λ = 1.80 Å."`
- Read / check: Thermal neutron: KE = 25×10⁻³×1.6×10⁻¹⁹ = 4×10⁻²¹ J. λ = h/√(2mKE) = 6.626×10⁻³⁴/√(2×1.675×10⁻²⁷×4×10⁻²¹) = 6.626×10⁻³⁴/√(1.34×10⁻⁴⁷) = 6.626×10⁻³⁴/1.158×10⁻²³·⁵ = 1.80×10⁻¹⁰ m = 1.80 Å. Baseball at 30 m/s: λ = 6.626×10⁻³⁴/(0.142×30) = 1.56×10⁻³⁴ m (completely unobservable).
- Human supplies: Nothing — fully synthetic. Analytic formula.
- Output medium: d3 (animated, single HTML file)
- The change: Show electron microscopy: an electron accelerated through voltage V has λ = h/√(2meV). Plot the image resolution limit (≈ λ) vs. accelerating voltage. At V = 200 kV (typical TEM): λ ≈ 2.5 pm — smaller than an atom. This is why electron microscopes can image individual atoms.
- Teardown angle: The de Broglie wavelength is not a theoretical curiosity — it is the physical reason why electrons and neutrons can diffract off crystals. The day this wavelength becomes comparable to the size of the thing you're probing, wave behavior dominates.
- Exclusions: Relativistic de Broglie wavelength (p = γmv for high-energy electrons), matter-wave interferometry with molecules.
- Score: 8/10

---

## Candidate 07 — Simulate the Random Walk of a Solar Photon with Claude

- Source: physics-plus-one-modern-physics/chapters/02-the-sun-a-garden-variety-star.md
- Lane: BUILD (Claude Code)
- Hook: A photon produced in the Sun's core doesn't travel outward in 2 seconds — it takes 100,000 years. Each step in the random walk is about 1 cm. The expected distance after N steps of length l is l√N, not Nl. Simulate the walk and measure the diffusion time.
- The artifact: A D3 animation of a 2D random walk simulation: a photon (dot) takes steps of fixed length l in random directions. The simulation runs for N steps, with the root-mean-square displacement R_rms = l√N computed live. A histogram of final distances from origin (over 200 random-walk runs) is shown alongside the theoretical Gaussian distribution P(r) ∝ r exp(−r²/4Nl²). The expected time to travel R_sun ≈ 7×10⁸ m with l=0.01 m is computed: t = (R_sun/l)² × l/c.
- Prompt seed: `claude "Build a D3 v7 single-file HTML solar photon random walk simulator. Animate a 2D random walk: N steps (slider 100–10000) of step length l (slider 0.5–5 pixels). Each step random direction. Show: (1) walk path animating, (2) live R_rms = l√N vs. R_direct = N·l comparison, (3) histogram of final |r| over 500 walk instances vs. theoretical Rayleigh distribution. Compute: with l=0.01m and R=7×10⁸m, N=(R/l)²=4.9×10¹⁸ steps, time = N×(l/c) = 163,000 years. Display these numbers. Verify: mean |r| after N steps ≈ l√(πN/2)."`
- Read / check: After N steps of length l, R_rms = l√N, mean distance = l√(πN/2). For l=0.01 m, R=7×10⁸ m: N = (R/l)² = (7×10¹⁰)² = 4.9×10²¹ steps. Time = N × l/c = 4.9×10²¹ × 0.01/3×10⁸ = 1.63×10¹¹ s ≈ 5170 years. (The commonly cited 100,000 years includes thermalization delays; the pure random-walk gives ~5000 years — both valid to cite.) In 2D simulation: R_rms = l√N confirmed within ~√2 factor from 3D geometry.
- Human supplies: Nothing — fully synthetic. Random walk algorithm in JavaScript.
- Output medium: d3 (animated, single HTML file)
- The change: Show the contrast with a straight-line photon: at step l=0.01 m, a straight-line photon travels 7×10⁸ m in 2.3 seconds. The random walk takes 5000–100,000 years. The ratio is N = (R/l), and it grows as R². Plot the diffusion time vs. mean free path l.
- Teardown angle: The key insight is that random walk distance grows as √N, not as N. This is the difference between diffusion (√N growth) and ballistic transport (N growth). The Sun's interior is opaque precisely because the mean free path is so short — the photons are effectively trapped by a diffusion process.
- Exclusions: Energy transfer vs. photon transport distinction, opacity coefficients, full radiative transfer equation.
- Score: 7/10

---

## Candidate 08 — Compute the Blackbody Temperature of a Planet with Claude

- Source: physics-plus-one-modern-physics/chapters/02-the-sun-a-garden-variety-star.md
- Lane: BUILD (Claude Code)
- Hook: Venus is hotter than Mercury despite being farther from the Sun. Mars is colder than the equation predicts. The equilibrium temperature equation T_eq = T_sun × (R_sun/2d)^(1/2) × (1−A)^(1/4) is a 2-line derivation — but the greenhouse gas correction is what drives climate.
- The artifact: A D3 interactive solar system diagram: 8 planets on a log-scale distance axis, each with sliders for albedo A (0–1) and atmospheric emissivity ε (0–1, representing greenhouse effect). The equilibrium temperature T_eq is computed live. A second panel shows T_eq vs. distance for A=0.3 (Earth-like albedo), with the habitable zone (273–373 K) shaded. Planet dots are colored by temperature (blue=cold, red=hot). The greenhouse effect panel shows actual surface temperatures vs. equilibrium temperatures.
- Prompt seed: `claude "Build a D3 v7 single-file HTML planetary equilibrium temperature calculator. Solar system: 8 planets at real distances. Sliders per planet: albedo A (0-1), greenhouse parameter ε (0-1). Compute T_eq = T_sun · √(R_sun/(2d)) · (1-A)^(1/4) / (1-ε/2)^(1/4). Plot: (1) solar system to scale (log distance), planet dots colored by T_eq, (2) T vs. d for A=0.3, ε=0, with habitable zone 273-373K shaded green. Table: planet, d (AU), A, ε, T_eq, T_actual (embed real values). Verify: Earth (d=1AU, A=0.3, ε=0) → T_eq = 255K; with ε=0.78 (greenhouse) → T_eq = 288K."`
- Read / check: T_eq(no greenhouse) = 278×(1−0.3)^(1/4)/√1 = 278×0.915 = 254.4 K ≈ 255 K. Earth actual: 288 K (15°C). Greenhouse correction: (1−ε/2)^(1/4) in denominator; at ε=0.78: (1−0.39)^(1/4) = 0.61^(1/4) = 0.884; T_eq → 255/0.884 = 288 K. Mars: d=1.524 AU, A=0.25 → T_eq = 278×0.944/√1.524 = 212 K (actual ~210 K, good match — Mars has little greenhouse effect).
- Human supplies: Nothing — fully synthetic. Planet data embedded from public sources.
- Output medium: d3 (animated, single HTML file)
- The change: Add a "Venus scenario": set Earth albedo to A=0.77 (Venus's cloud albedo) and emissivity to ε~0.99 (extreme greenhouse) and show T → 737 K = 464°C. This makes the runaway greenhouse effect quantitative and observable.
- Teardown angle: The equilibrium temperature equation is energy balance: power absorbed = power emitted. It is not climate modeling — it is thermodynamics. The greenhouse parameter ε is what separates the textbook calculation from the actual surface temperature, and its value is set by atmospheric composition.
- Exclusions: Full radiative-convective climate models, cloud feedbacks, ocean heat capacity.
- Score: 7/10

---

## Candidate 09 — Simulate the Compton Effect: Photon-Electron Scattering with Claude

- Source: physics-plus-one-modern-physics/chapters/04-the-quantum-nature-of-light.md
- Lane: BUILD (Claude Code)
- Hook: The Compton effect proved that light carries momentum — not just energy. When an X-ray scatters off a free electron, it shifts in wavelength by an amount that depends only on the scattering angle and the electron's rest mass. The formula is Δλ = (h/m_e c)(1−cos θ). Build the billiard-ball collision in relativistic kinematics.
- The artifact: A D3 animation of a Compton scattering event: an X-ray photon (arrow, labeled with λ₀ and E = hc/λ₀) hits a stationary electron. The scattered photon (angle θ, slider 0°–180°) exits with wavelength λ' = λ₀ + Δλ where Δλ = 0.00243 nm × (1−cosθ). The electron recoils with kinetic energy KE = E − E'. A momentum vector diagram shows the relativistic momentum conservation. The Compton wavelength λ_C = h/(m_e c) = 0.00243 nm is marked.
- Prompt seed: `claude "Build a D3 v7 single-file HTML Compton scattering simulator. Incident X-ray: wavelength λ₀ slider (0.01–0.1 nm). Scattering angle θ slider (0°–180°). Compute: Δλ = (h/m_e c)(1-cosθ) = 0.002426·(1-cosθ) nm; λ' = λ₀ + Δλ; E_photon_scattered = hc/λ'; KE_electron = E_photon_incident - E_photon_scattered. Animate: incident arrow → scattering vertex → two outgoing arrows (photon at θ, electron at φ = atan(p_photon·sinθ/(p_photon_0 - p_photon·cosθ))). Show: momentum vector diagram. Verify: θ=180° (backscatter) → Δλ = 0.00485nm (maximum shift)."`
- Read / check: Compton shift Δλ = h/(m_e c) × (1−cosθ). At θ=90°: Δλ = h/(m_e c) = 6.626×10⁻³⁴/(9.11×10⁻³¹×3×10⁸) = 2.426×10⁻¹² m = 0.00243 nm. At θ=180°: Δλ = 2×2.426 pm = 0.00485 nm. For λ₀=0.05 nm (Cu K-alpha X-ray) and θ=90°: λ' = 0.05+0.00243 = 0.05243 nm. Energy shift: E' = hc/λ' = 23.7 keV vs. E = 24.8 keV; KE_electron = 1.1 keV.
- Human supplies: Nothing — fully synthetic. Relativistic Compton formula analytic.
- Output medium: d3 (animated, single HTML file)
- The change: Add a "classical wave prediction": what would a classical wave predict for scattered wavelength? (Classical: no change in wavelength, only amplitude. Thomson scattering at low energy gives the classical limit.) Show the deviation: at high incident energy, the Compton shift becomes large and the classical prediction fails completely.
- Teardown angle: The Compton effect requires both quantum mechanics (photon momentum p=h/λ) and special relativity (relativistic electron kinematics). Without either, the formula is wrong. It was the first proof that electromagnetic radiation behaves as a particle in scattering experiments — completing the evidence for the photon.
- Exclusions: Klein-Nishina differential cross-section, inverse Compton scattering, pair production threshold.
- Score: 7/10

---

## Candidate 10 — Derive E = mc² from Relativistic Momentum with Claude

- Source: physics-plus-one-modern-physics/chapters/09-special-relativity.md
- Lane: BUILD (Claude Code)
- Hook: E = mc² is usually presented as a fact. But it follows from a 10-line derivation using relativistic momentum and the work-energy theorem. Build the animated algebra — starting from p = γmv, apply the work-energy theorem, and watch E = γmc² appear on screen.
- The artifact: A D3 animated "algebra walkthrough" — each step of the derivation appears in sequence: (1) p = γmv, (2) dE = v dp (work-energy theorem), (3) integrating dE = v d(γmv) from rest, (4) result: KE = (γ−1)mc², (5) total energy E = γmc². A numerical panel shows: a 1 kg mass at rest has rest energy 9×10¹⁶ J; accelerating to 0.9c adds kinetic energy (γ−1)mc² = 1.29 mc². A "mass deficit" panel shows: helium-4 mass is 0.7% less than 4 protons → that missing mass × c² = the fusion energy released.
- Prompt seed: `claude "Build a D3 v7 single-file HTML E=mc² derivation walkthrough. Animate 8 steps sequentially (button to advance): (1) KE = ∫F·dx, (2) F = dp/dt, (3) p = γmv, (4) dp/dv = d(γmv)/dv = γ³m, (5) dE/dv = v·dp/dv = γ³mv, (6) KE = ∫₀ᵛ γ³mv dv = γmc² - mc², (7) total E = KE + mc² = γmc², (8) at v=0: E₀ = mc². Each step: highlighted equation with numerical example. Final panel: He-4 mass deficit: 4×938.27 - 3727.38 = 25.7 MeV = 0.0274 u × c²."`
- Read / check: Step 6 integral: ∫₀ᵛ γ³mv dv. Substitution: let u = γ² = 1/(1−v²/c²), du = 2γ⁴v/c² dv. Integral = mc²[γ]₀ᵛ = mc²(γ−1). So KE = mc²(γ−1). Total E = KE + mc² = γmc². Mass deficit for He-4: 4×(proton mass) − (He-4 mass) = 4×938.272 − 3727.379 = 25.709 MeV/c². This is the Q-value of the pp chain. Verify: 25.7 MeV × (6.022×10²³/4) × 1.6×10⁻¹³ = 6.2×10¹¹ J/mol H₂ = 2.5×10¹⁴ J/kg hydrogen.
- Human supplies: Nothing — fully synthetic.
- Output medium: d3 (animated, single HTML file)
- The change: Add the binding energy per nucleon curve (B/A vs. A): show that fusion from H to Fe releases energy (B/A increases), while fission from very heavy nuclei also releases energy (B/A increases toward Fe). The iron nucleus is at the bottom of the energy well — the most stable nucleus in the universe.
- Teardown angle: E = mc² is not about annihilation — it is about the energy stored in mass. Any process that changes mass (nuclear binding, particle-antiparticle creation) releases or absorbs energy × c². The formula is a conversion factor between the mass and energy units, and it applies to every process in the universe.
- Exclusions: Pair production/annihilation in detail, virtual particle mass-energy, vacuum energy.
- Score: 7/10
