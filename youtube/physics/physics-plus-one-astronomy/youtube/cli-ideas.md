# Physics +1: Advanced Astronomy — CLI Video Ideas ("X with Claude")

## Candidate 01 — Build an Interactive Planck Blackbody Curve for Stars with Claude

- Source: physics-plus-one-astronomy/chapters/03-radiation-and-spectra.md
- Lane: BUILD (Claude Code)
- Hook: You know the surface temperature of the Sun to four significant figures — and no spacecraft has ever touched it. Wien's displacement law reads the temperature from the color of the light. Build the tool that astronomers use and measure any star's temperature from its spectral peak.
- The artifact: A D3 animation plotting the Planck function B(λ,T) = (2hc²/λ⁵)/(exp(hc/λkT)−1) across 100–3000 nm as a temperature slider sweeps 3000–50,000 K. The visible band (380–700 nm) is shaded and colored. The peak wavelength marker moves with Wien's law λ_max = 2.898×10⁻³/T. Stellar classification labels (M, K, G, F, A, B, O) appear at the corresponding temperatures. A second panel shows two specific star blackbodies superposed for comparison.
- Prompt seed: `claude "Build a D3 v7 single-file HTML Planck blackbody curve simulator for astronomy. X-axis: wavelength 100–3000 nm. Y-axis: B(λ,T) normalized to peak. Slider: T from 3000–50000 K. Draw Planck curve. Mark λ_max with a dashed vertical line labeled with Wien's law result. Shade visible band 380–700 nm. Display stellar type label (OBAFGKM) for the current T. Second panel: superpose two temperatures (T1, T2 sliders). Verify: Sun T=5778K → λ_max = 501 nm (green-yellow)."`
- Read / check: λ_max = 2.898×10⁻³/5778 = 501 nm. At T=3000 K (M star): λ_max = 966 nm (NIR). At T=30,000 K (O star): λ_max = 97 nm (far UV). Verify the curve shape is the correct hump (not the Rayleigh-Jeans rising curve). Y-axis normalized: B(λ_max,T) = 1.
- Human supplies: Nothing — fully synthetic. Planck formula analytic.
- Output medium: d3 (animated, single HTML file)
- The change: Add the Stefan-Boltzmann luminosity calculation: given a star radius R (slider in solar radii) and T, compute L = 4πR²σT⁴ in solar luminosities and display. Let the viewer find where on an H-R diagram the star sits by plotting L vs. T.
- Teardown angle: The color of a star is a thermometer. Astronomers use this every night — no mass spectrometer, no contact, just the peak wavelength and Wien's law. The spectrum is the star's biography.
- Exclusions: Non-LTE stellar atmosphere deviations, limb darkening, extinction corrections.
- Score: 9/10

---

## Candidate 02 — Simulate Stellar Parallax and the Distance Ladder with Claude

- Source: physics-plus-one-astronomy/chapters/07-stellar-distances.md
- Lane: BUILD (Claude Code)
- Hook: The parsec is defined by an angle of one arcsecond. The nearest star is at 1.3 parsecs. Betelgeuse is so far that its parallax angle is smaller than the wobble of the telescope pointing system. Compute the geometric limit of the parallax method — and what replaces it beyond.
- The artifact: A D3 animation of the parallax geometry: Earth orbiting the Sun (1 AU baseline), a nearby star at distance d, and the parallax angle p = 1 arcsecond at d = 1 pc. A slider moves d from 1 to 1000 pc; the parallax angle shrinks accordingly (p = 1/d arcsec). A second panel shows the distance ladder: parallax (up to ~1000 pc from Gaia), Cepheid period-luminosity relation (up to ~50 Mpc), Type Ia SN standard candles (up to ~1 Gpc) — each range drawn on a log scale with the overlap regions marked.
- Prompt seed: `claude "Build a D3 v7 single-file HTML stellar parallax and distance-ladder simulator. Panel 1: Earth orbit (radius 1 AU), nearby star at distance d (slider 1–1000 pc), show parallax angle p = 1/d arcsec and the parallax triangle. Panel 2: log-scale cosmic distance ladder — horizontal bars showing: parallax (1pc–1kpc), Cepheids (1kpc–50Mpc), Type Ia SN (10Mpc–1Gpc), CMB (all scales). Animate expansion of each rung as slider selects scale. Verify: d=10pc → p=0.1 arcsec."`
- Read / check: p = 1/d where p is in arcseconds and d is in parsecs. At d=10 pc: p=0.1 arcsec. At d=1000 pc (Gaia limit): p=0.001 arcsec. The animation should make the parallax triangle visibly smaller at larger d. The distance ladder panel should show the four rungs with correct scale spans.
- Human supplies: Nothing — fully synthetic. All geometry and scale ranges from published catalog limits.
- Output medium: d3 (animated, single HTML file)
- The change: Add the Gaia uncertainty: plot the actual Gaia DR3 parallax error floor (~0.01 mas) as a horizontal line, and show how many stars in the Milky Way disk fall within reliable parallax distance (slider: parallax SNR > 5 threshold).
- Teardown angle: The distance ladder's weakness is that each rung is calibrated by the rung below it — errors compound. Gravitational wave standard sirens (and now JWST time-delay cosmography) are the first distance indicators that do not rely on the ladder.
- Exclusions: Cepheid period-luminosity derivation from stellar pulsations, Leavitt's full photometric analysis, surface-brightness fluctuations.
- Score: 9/10

---

## Candidate 03 — Model the Hertzsprung-Russell Diagram from Stellar Data with Claude

- Source: physics-plus-one-astronomy/chapters/06-analyzing-starlight.md
- Lane: BUILD (Claude Code)
- Hook: Plot 10,000 nearby stars by temperature and luminosity and you see a diagonal band, a horizontal branch, and a scattering of red giants. That pattern is the entire history of how stars live and die — and each star's position is determined by two numbers Claude can compute from published data.
- The artifact: A D3 scatter plot (H-R diagram): x-axis is surface temperature T (decreasing left to right, log scale, 50,000–2,500 K), y-axis is luminosity L/L☉ (log scale, 10⁻⁴ to 10⁶). Stars from the Hipparcos/Gaia catalog (a public dataset of ~1000 nearby stars) are plotted as dots colored by spectral type (OBAFGKM color map). The main sequence, giant branch, and white dwarf region are visible as clusters. Claude generates the plot from an embedded CSV of T and L values.
- Prompt seed: `claude "Build a D3 v7 single-file HTML Hertzsprung-Russell diagram. Use the embedded 1000-star dataset (columns: star name, T_eff K, L/L_sun, spectral class — you generate plausible synthetic data matching the real HR distribution: main sequence, red giant branch, white dwarf region). X-axis: T from 50000 to 2500 K (log, reversed). Y-axis: L from 10^-4 to 10^6 (log). Color dots by spectral type OBAFGKM. Draw labeled regions: main sequence, giant branch, white dwarf, supergiant. Hover: show star name and values."`
- Read / check: The main sequence should follow L ∝ M^4 ≈ (T/T☉)^8 roughly (for solar-type stars, L ∝ T^4 × R² varies). The Sun should be at T=5778K, L=1L☉ on the main sequence. White dwarfs should appear at high T (~10,000–50,000 K) but low L (~10⁻³ to 10⁻² L☉). Verify distribution looks like a real H-R diagram.
- Human supplies: Nothing — fully synthetic. Claude generates a plausible 1000-star synthetic dataset that mirrors the Hipparcos statistical distribution.
- Output medium: d3 (animated, single HTML file)
- The change: Add a "stellar evolution track" for a 1 M☉ star: draw an animated path from the zero-age main sequence (ZAMS) through the subgiant branch, red giant branch, horizontal branch, and white dwarf region — showing where the Sun will be in 5 Gyr.
- Teardown angle: The H-R diagram is not a scatter plot — it is a phase diagram of stellar physics. Stars don't live everywhere on it; they are channeled by the equations of stellar structure into the narrow bands we observe.
- Exclusions: Isochrone fitting for cluster ages, detailed stellar evolution equations, metallicity effects on main sequence location.
- Score: 9/10

---

## Candidate 04 — Simulate a Supernova Light Curve with Claude

- Source: physics-plus-one-astronomy/chapters/10-death-of-stars.md
- Lane: BUILD (Claude Code)
- Hook: SN 1987A was visible to the naked eye for three months. Twenty neutrinos arrived three hours before the light. The neutrino burst released more energy in one second than the Sun emits in its entire lifetime. Simulate the light curve and read off the nickel-56 decay signature.
- The artifact: A Manim animation of a Type II supernova light curve: brightness vs. time from 0 to 1 year. The initial shock-breakout flash, the plateau phase (powered by hydrogen recombination), and the radioactive decay tail (powered by ⁵⁶Ni→⁵⁶Co→⁵⁶Fe with half-lives 6.1 d and 77.2 d) are all modeled. The exponential decay tail animates as a straight line on a log-brightness plot. A second panel shows the ⁵⁶Ni and ⁵⁶Co populations decaying via the Bateman equations.
- Prompt seed: `claude "Using Python + Manim, animate a Type IIP supernova light curve (similar to SN 1987A). Model: (1) shock-breakout spike at t=0 (duration ~hours), (2) plateau phase at L~10^43 erg/s for 80 days, (3) radioactive tail from Ni-56 (t_1/2=6.1d) → Co-56 (t_1/2=77.2d) → Fe-56. Compute radioactive luminosity L(t) = epsilon × dN_Co/dt, where N_Co from Bateman equations. Animate both linear-time and log-scale panels. Overlay the SN 1987A data points (V-band, days 0-400). Verify: slope of log-L in tail = -ln2/t_half(Co-56) = -0.00897 per day."`
- Read / check: Co-56 t½ = 77.2 d → decay constant λ = 0.693/77.2 = 0.00897 d⁻¹. In the tail (after ~150 d), log L should decrease linearly with this slope. Ni-56 peak at ~6 days (1 Ni half-life). Verify Bateman equations conserve total A=56 nuclei. The SN 1987A data should fall on or near the curve.
- Human supplies: Nothing — fully synthetic. The SN 1987A V-band data points are published (Hamuy et al. 1988) and can be embedded as a table in the prompt.
- Output medium: Manim (animated light curve scene)
- The change: Toggle between Type Ia (thermonuclear, no plateau, Ni-56 powered from the start) and Type IIP (core collapse, hydrogen plateau) — showing the two very different light curve shapes and why Type Ia are standard candles.
- Teardown angle: The radioactive tail of a supernova is a nuclear clock visible across millions of light-years. The slope of the log-brightness curve tells you the half-life of Co-56 — the same measurement you'd make in a lab, encoded in starlight.
- Exclusions: Neutrino transport in core collapse, r-process nucleosynthesis, gravitational wave emission.
- Score: 8/10

---

## Candidate 05 — Compute the Schwarzschild Radius and Photon Sphere with Claude

- Source: physics-plus-one-astronomy/chapters/11-black-holes-and-curved-spacetime.md
- Lane: BUILD (Claude Code)
- Hook: The Schwarzschild radius is where escape velocity equals the speed of light. For the Sun it's 3 km. For the Earth it's 9 mm. For a 10 billion solar mass black hole — the kind we've imaged — it's the size of the solar system. Build the calculator and explore what happens at each scale.
- The artifact: A D3 interactive showing: (1) a mass slider (1 kg to 10¹⁰ M☉, log scale) with r_s = 2GM/c² computed live, (2) a log-scale "size comparison" bar showing r_s against a reference (proton: 10⁻¹⁵ m, atom: 10⁻¹⁰ m, cell: 10⁻⁵ m, Earth: 6.4×10⁶ m, solar system: 10¹³ m), (3) the photon sphere radius r_ph = 3GM/c² = 1.5 r_s drawn in a mini orbital diagram. A second panel shows the Event Horizon Telescope image scale: at d=55 Mly (M87), what angular size does r_s subtend?
- Prompt seed: `claude "Build a D3 v7 single-file HTML Schwarzschild radius calculator. Mass slider: 1 kg to 10^10 M_sun (log). Compute r_s = 2GM/c² in meters. Show log-scale bar chart comparing r_s to: proton (10^-15m), DNA (2×10^-9m), human (2m), Earth (6.4×10^6m), Sun (7×10^8m), solar system (1.5×10^13m). Compute photon sphere r_ph = 1.5×r_s. Angular size θ = r_s/d for M87 (d=16.4 Mpc): verify θ ≈ 3.8 µas. Animate bar growing as mass increases."`
- Read / check: r_s(Sun) = 2×6.674×10⁻¹¹×2×10³⁰/(3×10⁸)² = 2954 m ≈ 3 km. r_s(Earth) = 2×6.674×10⁻¹¹×6×10²⁴/(9×10¹⁶) = 8.87×10⁻³ m ≈ 9 mm. M87* mass ~6.5×10⁹ M☉ → r_s = 1.93×10¹³ m. At d=16.4 Mpc: θ = r_s/d = 1.93×10¹³ / (16.4×3.086×10²²) = 3.8×10⁻¹¹ rad = 7.8 µas (shadow diameter ~5r_s ≈ 40 µas, matching EHT image).
- Human supplies: Nothing — fully synthetic. All from physical constants.
- Output medium: d3 (animated, single HTML file)
- The change: Add gravitational time dilation: show t_far/t_near = 1/√(1−r_s/r) vs. radial position r, with the clock-rate going to zero at r = r_s. A slider lets the viewer choose r and see how much time passes at infinity per tick at that radius.
- Teardown angle: The event horizon is not a physical surface — it is a surface of no return defined by the geometry of spacetime. Nothing special happens locally as you cross it; the physics is in what can never be communicated back.
- Exclusions: Kerr metric (rotating black holes), Hawking radiation, black hole thermodynamics.
- Score: 8/10

---

## Candidate 06 — Simulate the Hubble Flow and the Cosmic Expansion with Claude

- Source: physics-plus-one-astronomy/chapters/13-the-big-bang.md
- Lane: BUILD (Claude Code)
- Hook: Every galaxy beyond the Local Group is moving away from us — not because it's flying through space, but because space itself is expanding. Run Hubble's law backward and the expansion converges to a single moment 13.8 billion years ago.
- The artifact: A D3 animation of the Hubble flow: 200 galaxies scattered in 2D space (representing a slice of the observable universe), each with a velocity vector v = H₀ × d pointing away from the center. A time-forward animation shows the galaxies moving apart (expansion). A time-reverse animation shows them converging. A sidebar plots v vs. d for the 200 galaxies, showing the linear Hubble relation with scatter (to model measurement uncertainty). H₀ slider (50–100 km/s/Mpc) updates all velocities live.
- Prompt seed: `claude "Build a D3 v7 single-file HTML Hubble flow simulator. Place 200 galaxy dots at random positions within a 500×500 px canvas centered at origin. Velocity v = H₀ × d (H₀ slider 50–100 km/s/Mpc). Forward-time animation: galaxies drift apart at v×dt. Reverse-time animation: they converge. Speed slider for animation. Side panel: scatter plot v vs. d with best-fit line and H₀ computed from slope. Verify: all vectors point radially outward; at H₀=70 km/s/Mpc, a galaxy at 500 Mpc recedes at 35,000 km/s."`
- Read / check: v = 70 × 500 = 35,000 km/s = 0.117c. The scatter plot should show a linear trend (by construction) with slope H₀. Forward integration: at time t, positions scale as a(t) where ȧ/a = H₀ (comoving, ignoring deceleration). Verify that 1/H₀ = 1/(70 km/s/Mpc) ≈ 13.97 Gyr (correct naive age).
- Human supplies: Nothing — fully synthetic. Galaxy positions randomly placed; velocities computed.
- Output medium: d3 (animated, single HTML file)
- The change: Add a second simulation showing the raisin-bread model: every galaxy (raisin) sees every other galaxy receding — there is no center. Place the observer on any galaxy and show the same Hubble relation holds everywhere. This counters the misconception that we're at the center of the Big Bang.
- Teardown angle: Hubble's law is a statement about geometry: if the universe expands uniformly, every point sees every other point receding with velocity proportional to distance. The Big Bang is not an explosion into pre-existing space — it is the expansion of space itself.
- Exclusions: ΛCDM acceleration, dark energy equation of state, cosmic distance ladder errors.
- Score: 8/10

---

## Candidate 07 — Plot the Maxwell-Boltzmann Speed Distribution for Stellar Atmospheres with Claude

- Source: physics-plus-one-astronomy/chapters/03-radiation-and-spectra.md
- Lane: BUILD (Claude Code)
- Hook: Mars is losing its atmosphere because of the tail of this curve. A small fraction of hydrogen molecules at any given moment are moving faster than escape velocity. Plot the full distribution and show where the escape velocity line falls for different planets — and for the Sun's corona.
- The artifact: A D3 animation of the Maxwell-Boltzmann speed distribution f(v) = 4πn(m/2πkT)^(3/2) v² exp(−mv²/2kT) for various gases (H₂, N₂, O₂, CO₂) at a temperature T. Vertical dashed lines mark v_rms = √(3kT/m), v_avg = √(8kT/πm), and v_mp = √(2kT/m). A second vertical line marks the escape velocity for a selected planetary body (Earth, Mars, Moon, Sun, Jupiter) from a dropdown. The tail area beyond v_escape is shaded and its integral computed — this is the fraction of molecules able to escape.
- Prompt seed: `claude "Build a D3 v7 single-file HTML Maxwell-Boltzmann speed distribution visualizer. X-axis: speed 0–5000 m/s. Y-axis: f(v) normalized. Dropdowns: gas species (H, H2, He, N2, O2, CO2) → molar mass, body (Moon, Mars, Earth, Jupiter, Sun corona) → escape velocity. Sliders: T (100–50000 K). Plot MB distribution, label v_mp, v_avg, v_rms. Draw v_escape line; shade tail area f(v>v_esc) and display its integral %. Verify: N2 at T=293K, Earth v_esc=11.2km/s → tail fraction ≈ 10^-100 (essentially zero, hence stable atmosphere)."`
- Read / check: For N₂ (m=28 u) at 293 K: v_rms = √(3×1.38×10⁻²³×293/(28×1.66×10⁻²⁷)) = 511 m/s. Earth v_esc = 11,200 m/s >> v_rms → tail fraction effectively zero. For H (m=1 u) at 293 K: v_rms = 1920 m/s, still below 11.2 km/s but the tail is non-negligible. For Mars (v_esc=5.03 km/s) and H: meaningful tail fraction explains atmospheric loss.
- Human supplies: Nothing — fully synthetic. Maxwell-Boltzmann formula analytic; escape velocities from known constants.
- Output medium: d3 (animated, single HTML file)
- The change: Add time evolution: for Mars's H₂ atmosphere over 4.5 Gyr, numerically estimate the fraction lost per year (Jeans escape) and animate the atmospheric column density depleting.
- Teardown angle: Atmospheric escape is not the average molecule escaping — it is the tail. Tails of probability distributions are invisible on linear scales but can dominate over geological time. The universe is patient.
- Exclusions: Non-thermal escape mechanisms (photochemical, sputtering), hydrodynamic escape, magnetic field effects.
- Score: 8/10

---

## Candidate 08 — Simulate Cepheid Variable Pulsations and the Period-Luminosity Relation with Claude

- Source: physics-plus-one-astronomy/chapters/07-stellar-distances.md
- Lane: BUILD (Claude Code)
- Hook: Henrietta Swan Leavitt noticed in 1908 that brighter Cepheid variables took longer to reach peak brightness. That single observation — a correlation between period and luminosity — gave astronomers their first ruler to extragalactic distances and led directly to the discovery that the universe is larger than the Milky Way.
- The artifact: A D3 animation of a pulsating Cepheid: a circle animating its radius R(t) in a sinusoidal oscillation, with temperature T(t) oscillating 180° out of phase (star is hottest when smallest, following κ-mechanism). The luminosity L(t) = 4πR²σT⁴ is computed live and plotted below as a light curve. A second panel plots the Leavitt period-luminosity law: log L vs. log P for a sample of 30 Cepheids (synthetic dataset), with the best-fit line drawn and its slope labeled.
- Prompt seed: `claude "Build a D3 v7 single-file HTML Cepheid pulsation simulator. Panel 1: animated pulsating star circle (R oscillating sinusoidally, T phase-shifted 180° — cool when large, hot when small). Compute L = 4πR²σT⁴ live; plot L(t) light curve below. Panel 2: scatter plot of log(L/L_sun) vs. log(P/days) for 30 synthetic Cepheids following L ∝ P^1.15 (Leavitt law). Draw best-fit line. Sliders: pulsation period P, amplitude ΔR/R. Verify: L_max/L_min ≈ 5 for typical ΔR/R=0.15, ΔT/T=0.05."`
- Read / check: For ΔR/R = 0.15 and ΔT/T = 0.05: L_max/L_min = (R_max/R_min)²×(T_max/T_min)⁴ = (1.15/0.85)²×(1.05/0.95)⁴ ≈ 1.83×1.49 ≈ 2.7. The light-curve period should match the input P slider. Leavitt slope: Δlog L / Δlog P ≈ 1.15 (canonical value for classical Cepheids).
- Human supplies: Nothing — fully synthetic. The kappa-mechanism drives real Cepheids; the simulation uses parametric approximations.
- Output medium: d3 (animated, single HTML file)
- The change: Add distance measurement: give the viewer an "unknown Cepheid" with a measured period and apparent magnitude. Using the Leavitt law and inverse-square law, compute its distance modulus and display it in Mpc — simulating how Hubble measured the distance to M31.
- Teardown angle: The Leavitt law works because more massive Cepheids are more luminous AND pulsate more slowly — both controlled by the same stellar physics. The period is the observable; the luminosity is derived. Distance follows from the inverse-square law.
- Exclusions: κ-mechanism derivation from opacity physics, Population I vs. II Cepheid metallicity corrections, period-luminosity calibration history.
- Score: 7/10

---

## Candidate 09 — Compute the Chandrasekhar Mass Limit in an Afternoon with Claude

- Source: physics-plus-one-astronomy/chapters/10-death-of-stars.md
- Lane: BUILD (Claude Code)
- Hook: A 20-year-old on a ship from India to England worked out in 1930 that no white dwarf heavier than 1.4 solar masses can exist. The calculation uses quantum mechanics and special relativity. Reproduce it numerically in 40 lines of Python.
- The artifact: A Manim scene showing the Lane-Emden solution for white dwarf structure: the dimensionless density profile θ(ξ) plotted from the numerical integration of the Lane-Emden equation for polytropic index n=3/2 (non-relativistic electrons) and n=3 (relativistic electrons). The total mass is computed by integrating the density profile; the n=3 solution gives the Chandrasekhar mass M_Ch = 5.87/(μ_e)² M☉. An animated mass-radius curve draws from M=0 to M_Ch where R→0.
- Prompt seed: `claude "Using Python + NumPy + Manim, numerically integrate the Lane-Emden equation d/dξ(ξ²·dθ/dξ)/ξ² = -θ^n for n=3/2 and n=3. Use RK4 with initial conditions θ(0)=1, θ'(0)=0. Integrate until θ→0 (surface). Compute dimensionless radius ξ_1 and mass ξ₁²|θ'(ξ₁)|. Scale to physical units: M_Ch = 5.87·M_sun/μ_e² (use μ_e=2 for He/C). Animate: (1) θ(ξ) profiles for n=3/2 and n=3, (2) mass-radius curve from 0 to M_Ch showing R→0. Verify: n=3 gives M_Ch = 1.44 M_sun."`
- Read / check: For n=3: ξ₁ = 6.897, |θ'(ξ₁)| = 0.04243. M_Ch = 4π×(K₃/G)^(3/2) × ... formula gives 1.44 M☉ for μ_e=2. The RK4 integration should reach θ=0 cleanly (use adaptive step size near ξ₁). The mass-radius curve should be monotonically decreasing (heavier → smaller) and asymptote to 0 at M_Ch.
- Human supplies: Nothing — fully synthetic. Lane-Emden equation solved numerically in NumPy.
- Output medium: Manim (animated numerical integration scene)
- The change: Show what happens if the speed of light were different: scale c and recompute M_Ch ∝ (ℏc/G)^(3/2). At lower c, M_Ch decreases — more stars collapse to neutron stars. This is the anthropic sensitivity hidden in the Chandrasekhar limit.
- Teardown angle: The Chandrasekhar mass is not a coincidence — it is the mass at which gravitational energy equals the relativistic electron degeneracy energy. It depends only on fundamental constants (ℏ, c, G, m_p) and the composition (μ_e). Every white dwarf in the universe obeys it.
- Exclusions: Neutron star equation of state, Tolman-Oppenheimer-Volkoff limit, rotating white dwarfs.
- Score: 7/10

---

## Candidate 10 — Build a Cosmic Microwave Background Power Spectrum Viewer with Claude

- Source: physics-plus-one-astronomy/chapters/13-the-big-bang.md
- Lane: BUILD (Claude Code)
- Hook: The CMB is light from 380,000 years after the Big Bang — the universe's baby photo. The acoustic peaks in its power spectrum encode the density of baryons, dark matter, and dark energy. The location of the first peak tells you the geometry of space. Build the viewer and read off the cosmological parameters.
- The artifact: A D3 plot of the CMB angular power spectrum C_ℓ vs. multipole moment ℓ (1–2500). The Planck 2018 data points are plotted (embedded as a table of (ℓ, C_ℓ) values from the published data). The best-fit ΛCDM model curve is drawn. Three labeled acoustic peaks are highlighted. An annotation panel identifies what each peak measures: peak 1 (Ω_tot = 1, flatness), peak 2/peak 1 ratio (baryon density), peak 3/peak 1 ratio (dark matter density).
- Prompt seed: `claude "Build a D3 v7 single-file HTML CMB power spectrum viewer. Use embedded table of Planck 2018 TT power spectrum data (ℓ, D_ℓ in µK²) for ℓ=2 to 2500 (you embed ~100 representative data points). Plot D_ℓ vs ℓ as a scatter plot with error bars. Overlay the best-fit ΛCDM model curve (can use the approximate parametric form with three Gaussian peaks at ℓ≈220, 540, 810). Label first three peaks. Annotation panel: peak-1 location → curvature Ω_k≈0, peak-2/peak-1 ratio → Ω_b. Verify: peak-1 at ℓ≈220."`
- Read / check: First acoustic peak at ℓ ≈ 220 (corresponding to angular scale θ = 180°/220 ≈ 0.82°, the sound horizon at recombination). Second peak at ℓ ≈ 540. Third at ℓ ≈ 810. The ratio of odd-to-even peaks is related to the baryon-to-photon ratio. Verify the embedded Planck 2018 data points fall near the model curve (within ±5%).
- Human supplies: Nothing — fully synthetic. The Planck 2018 TT spectrum data is publicly available; Claude can embed representative values from the published paper or generate the ΛCDM approximation.
- Output medium: d3 (animated, single HTML file)
- The change: Add a parameter variation demo: sliders for Ω_b (baryon density 0.01–0.10) and Ω_CDM (dark matter 0.1–0.5) that move the approximate analytic peak positions and amplitudes, showing how different cosmological models would have produced different CMB skies.
- Teardown angle: The CMB power spectrum is not a pretty pattern — it is the solution to a coupled fluid equation for photons and baryons in the early universe. The acoustic oscillations are sound waves in the primordial plasma, frozen in place at recombination and now visible across the sky.
- Exclusions: Polarization power spectrum (TE, EE, BB), primordial B-mode gravitational waves, CMB lensing.
- Score: 7/10
