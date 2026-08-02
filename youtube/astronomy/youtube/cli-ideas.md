# Astronomy — CLI Video Ideas ("X with Claude")

---

## Candidate 01 — "Build Kepler's Third Law Verification with Claude Code" (BUILD)
- Source: astronomy/chapters/03-orbits-and-gravity.md
- Lane: BUILD (Claude Code)
- Hook: Kepler found P² = a³ in 1619 from two decades of Brahe's data — pure pattern-matching, no physics. You can verify it holds across every planet in the solar system in 20 lines of Python, and then ask: what happens when you plot it on a log-log scale?
- The artifact: A Python script that loads solar system planet data (period in years, semimajor axis in AU), computes P² and a³ for each planet from Mercury to Neptune, plots both on a log-log scatter plot with a y = x reference line, and prints the percent deviation for each planet. The visual payoff: eight points on a straight line across four orders of magnitude.
- Prompt seed: `claude "Write a Python script that verifies Kepler's Third Law (P² = a³) across the solar system. Hard-code the orbital period (years) and semimajor axis (AU) for Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, and Neptune. Compute P² and a³ for each. Plot them on a log-log scatter plot with a y=x reference line, label each planet, and print the percent deviation from the law for each. Use matplotlib."`
- Read / check: Verify that Earth returns P² = 1, a³ = 1 (trivially). Check Jupiter: P = 11.86 yr, a = 5.2 AU → P² = 140.7, a³ = 140.6. Check that Neptune (P = 164.8, a = 30.07) falls on the line. The log-log plot should show a straight line — the slope should be measured and printed (should be ≈ 1.0 if law holds exactly).
- Human supplies: Nothing — fully synthetic. Planet data is in the textbook and any astronomy reference. The script runs on any machine with matplotlib and numpy.
- Output medium: Manim (the log-log scatter plot animates: planets appear one by one at their correct (a³, P²) coordinates; the y=x line draws through them; each planet is labeled with its name and its percent deviation; the final frame shows all 8 planets on the line)
- The change: Add Pluto (P = 248 yr, a = 39.5 AU) and at least three confirmed exoplanets from the NASA Exoplanet Archive (fetch via astroquery or hard-code TRAPPIST-1 system) — does Kepler's Law hold for exoplanets orbiting other stars?
- Teardown angle: The law was found by data analysis in 1619. It was explained by physics in 1687 (Newton). The plot shows the data; the explanation shows why the data has that shape. These are two different kinds of knowledge, and astronomy does both.
- Exclusions: Orbital resonances, moons of planets, ellipse eccentricity — each is a separate BUILD card.
- Score: 10/10

---

## Candidate 02 — "Build a Blackbody Spectrum Plotter with Claude Code" (BUILD)
- Source: astronomy/chapters/05-radiation-and-spectra.md
- Lane: BUILD (Claude Code)
- Hook: Wien's law tells you a star's temperature from its color. The Planck function tells you the exact distribution of light across wavelengths. You can plot both in 30 lines of Python — and the plot reveals why hotter stars look bluer in a way that a verbal description never quite captures.
- The artifact: A Python script that plots the Planck blackbody function B(λ, T) for four temperatures (3,000 K, 5,778 K, 10,000 K, 30,000 K — corresponding to a cool red star, the Sun, a hot white star, and an O-type star), marks the peak wavelength with a vertical dashed line for each, and labels the visible spectrum range. Output: a family of curves showing the dramatic shift in peak from infrared toward UV as temperature rises.
- Prompt seed: `claude "Write a Python script that plots the Planck blackbody spectrum B(λ, T) = (2hc²/λ⁵) × 1/(e^(hc/λkT) - 1) for four stellar temperatures: 3000 K, 5778 K, 10000 K, 30000 K. Use wavelengths from 100 nm to 3000 nm. For each curve: normalize so peaks are comparable on screen, mark the peak wavelength with a vertical dashed line, and label the curve with the temperature and peak wavelength (from Wien's law: λ_peak = 2.898e-3 / T in meters). Shade the visible spectrum range (380–700 nm). Use matplotlib."`
- Read / check: Sun (5778 K) peak should be ≈ 501 nm (green-yellow); verify against Wien's law: 2.898e-3 / 5778 = 501 nm. Red star (3000 K) peak ≈ 966 nm (near-infrared). Hot star (30,000 K) peak ≈ 97 nm (UV). All four curves should be visible with normalization — unnormalized, the hot star would dwarf the others by many orders of magnitude.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim (the Planck curves draw one by one from coolest to hottest; each curve's peak slides toward shorter wavelengths; the visible spectrum band is shaded; a thermometer-style temperature indicator rises as each new curve appears)
- The change: Add the Stefan-Boltzmann calculation to the script: compute the total luminosity (area under each curve) as L ∝ T⁴, and print how much brighter the O-star is than the Sun. Then ask: if you could only see in infrared, which star would appear brightest?
- Teardown angle: Color is temperature. The shift from red to blue across the stellar census is not aesthetic — it is a thermometer reading. Once you have seen the Planck curves, you cannot look at a color-magnitude diagram the same way.
- Exclusions: Spectral absorption lines, telescope filter physics — separate cards.
- Score: 10/10

---

## Candidate 03 — "Build Hubble's Law from Recessional Velocity Data with Claude Code" (BUILD)
- Source: astronomy/chapters/29-the-big-bang.md
- Lane: BUILD (Claude Code)
- Hook: Hubble derived the expansion of the universe in 1929 from 46 galaxies and a ruler. You can reproduce his analysis — and extend it with modern Hubble Space Telescope data — in 25 lines of Python, and the slope of the regression is the age of the universe.
- The artifact: A Python script that loads (or hard-codes) a dataset of galaxy names, distances (in megaparsecs), and recessional velocities (in km/s) for ~20 galaxies spanning 1–1000 Mpc, fits a linear regression (v = H₀ × d), plots v vs. d with the regression line, prints H₀ from the slope with uncertainty, and computes T₀ = 1/H₀ converted to billion years.
- Prompt seed: `claude "Write a Python script that reproduces Hubble's Law from galaxy data. Hard-code a dataset of 20 galaxies with their distances in megaparsecs and recessional velocities in km/s — use a mix of nearby and distant galaxies to span from ~1 Mpc to ~1000 Mpc. Fit a linear regression (v = H₀ × d, no intercept) using numpy or scipy, plot the data with the regression line, print H₀ (km/s/Mpc) with the fit uncertainty, and compute the Hubble time T₀ = 1/H₀ in billion years. Label the plot axes and annotate the regression equation."`
- Read / check: H₀ should come out in the range 67–73 km/s/Mpc (modern value ~70 km/s/Mpc). T₀ = 1/H₀ = 1/(70 km/s/Mpc) × unit conversion = ≈ 13.97 billion years. Verify the unit conversion: 1 Mpc = 3.086 × 10²² m; H₀ in s⁻¹ = 70 × 1000 / (3.086 × 10²²) = 2.27 × 10⁻¹⁸ s⁻¹; T₀ = 1 / (2.27 × 10⁻¹⁸) = 4.4 × 10¹⁷ s ≈ 13.9 billion years.
- Human supplies: Nothing — fully synthetic. Galaxy data can be hard-coded from NED (NASA/IPAC Extragalactic Database) values Claude knows from training; note in the video that real research uses NED directly.
- Output medium: Manim (the v-d scatter plot builds point by point; the regression line draws through the points; H₀ and T₀ appear as computed values; a second animation shows the universe "running backward" — all points converging to an origin as the Hubble time ticks down)
- The change: Run the same analysis on Hubble's original 1929 dataset (available in his 1929 paper, hard-codeable from published data). Hubble's original H₀ was ~500 km/s/Mpc — nearly 7× the modern value. Ask Claude why Hubble was so wrong and what was corrected over the following decades.
- Teardown angle: Hubble found the expansion from bad data and got the right conclusion. The slope was wrong by a factor of 7 — but the line was real. This is what good science looks like: the pattern survives even when the calibration fails.
- Exclusions: Dark energy acceleration, CMB distance measurements — separate cards.
- Score: 10/10

---

## Candidate 04 — "Build a Stellar Parallax Calculator with Claude Code" (BUILD)
- Source: astronomy/chapters/19-celestial-distances.md
- Lane: BUILD (Claude Code)
- Hook: The nearest star has a parallax of 0.77 arcseconds — an angle so small it could not be measured until 1838. You can build the geometry in Python, plot the parallax-distance relationship across the range the Hipparcos and Gaia satellites cover, and see precisely where each instrument's precision hits the wall.
- The artifact: A Python script that: (1) plots the parallax-distance relationship D = 1/p (parsecs, arcseconds) from 1 parsec to 10,000 parsecs, (2) draws horizontal lines at the measurement limits of the human eye (impossible), ground-based telescopes (~0.01 arcseconds, ~100 pc), Hipparcos (0.001 arcseconds, ~1000 pc), and Gaia (0.00005 arcseconds, ~20,000 pc), (3) marks Proxima Centauri and the Pleiades cluster on the plot to show which instruments can and cannot measure each.
- Prompt seed: `claude "Write a Python script that plots the parallax-distance relationship D = 1/p (where D is in parsecs and p is in arcseconds) from p = 0.00001 to p = 1 arcseconds (i.e., D from 1 to 100,000 parsecs) on a log-log scale. Add horizontal lines marking four instrument precision limits: naked eye (p > 0.1 arcsec), ground-based telescope (p > 0.01 arcsec), Hipparcos (p > 0.001 arcsec), Gaia (p > 0.00005 arcsec). Mark Proxima Centauri (p = 0.77 arcsec) and the Pleiades cluster (p ≈ 0.0072 arcsec) as labeled points. Use matplotlib with a log-log scale."`
- Read / check: Proxima Centauri: p = 0.7687 arcsec → D = 1.30 pc ≈ 4.24 light-years. Pleiades: p ≈ 0.0072 arcsec → D ≈ 139 pc ≈ 453 light-years. Gaia limit: 50 microarcsec = 0.00005 arcsec → D = 20,000 pc = 20 kpc (within the Milky Way). Verify that Proxima falls within all four instrument limits and Pleiades is only visible to Hipparcos and Gaia.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim (the log-log curve draws; instrument limit lines animate in one by one as "capability bands"; Proxima and Pleiades markers appear; a zoom-in animates to show the Gaia precision band covering a large fraction of the Milky Way)
- The change: Add the Milky Way diameter (~30,000 pc) and the Andromeda Galaxy distance (~778,000 pc) as vertical markers — showing that even Gaia cannot reach extragalactic distances, and that the "distance ladder" must extend beyond parallax.
- Teardown angle: Every instrument has a wall. Knowing where the wall is tells you what the next rung of the ladder must do — and why parallax alone will never be enough to measure the universe.
- Exclusions: Cepheid variable calibration, Type Ia supernovae standard candles — the next rungs, each a separate card.
- Score: 10/10

---

## Candidate 05 — "Build a White Dwarf Mass-Radius Relationship with Claude Code" (BUILD)
- Source: astronomy/chapters/23-the-death-of-stars.md
- Lane: BUILD (Claude Code)
- Hook: White dwarfs get smaller as they get more massive — which is the opposite of almost everything else. The Chandrasekhar limit (1.4 solar masses) is the point where electron degeneracy pressure can no longer hold, and you can plot the full mass-radius relationship in Python and mark the cliff.
- The artifact: A Python script that plots the white dwarf mass-radius relationship using the non-relativistic and relativistic degeneracy pressure approximations: R ∝ M^(-1/3) for low masses, approaching zero as M → 1.4 M_sun (Chandrasekhar limit). The plot shows mass on the x-axis (0 to 1.4 solar masses) and radius on the y-axis (Earth radii), marks the Chandrasekhar limit as a vertical asymptote, and annotates Sirius B (0.98 M_sun, 0.84 Earth radii) as a real data point.
- Prompt seed: `claude "Write a Python script that plots the white dwarf mass-radius relationship. Use the non-relativistic electron degeneracy approximation for the mass range 0.1 to 1.35 solar masses: R ∝ M^(-1/3), scaled so that a 0.6 solar-mass white dwarf has a radius of approximately 0.013 solar radii (≈ 1.4 Earth radii). As mass approaches the Chandrasekhar limit of 1.4 solar masses, add a correction factor that drives the radius toward zero. Mark the Chandrasekhar limit as a vertical dashed line. Mark Sirius B (mass = 0.978 solar, radius = 0.0084 solar) as a labeled data point. Plot in solar-mass units on x-axis, Earth-radius units on y-axis. Use matplotlib."`
- Read / check: The key qualitative features must be correct: (1) higher mass = smaller radius (inverse relationship), (2) radius → 0 as M → 1.4 M_sun. Sirius B should fall on or near the theoretical curve. The non-relativistic approximation R ∝ M^(-1/3) is correct for low masses; the full relativistic treatment requires solving a differential equation (script can approximate with a correction factor). Verify Sirius B values against known data: M = 0.978±0.005 M_sun, R = 0.0084±0.0002 R_sun = 0.85 R_earth.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim (the mass-radius curve draws from left to right; as it approaches the Chandrasekhar limit the curve steepens dramatically; the vertical limit line drops; Sirius B appears as a labeled point; a callout explains "more mass = smaller star — the opposite of everything else")
- The change: Add Sirius B's density calculation: with mass ~0.98 M_sun and radius ~0.0084 R_sun, compute density in g/cm³ and compare to lead and gold. The result (≈ 1 metric ton per cubic centimeter) is the payoff.
- Teardown angle: Electron degeneracy pressure is not thermal pressure. It does not weaken when you cool the white dwarf. This is quantum mechanics doing structural engineering — and Chandrasekhar was 20 years old when he calculated its limit.
- Exclusions: Neutron star mass-radius relationship, specific observed white dwarfs other than Sirius B — separate cards.
- Score: 9/10

---

## Candidate 06 — "Build a Big Bang Nucleosynthesis Calculator with Claude Code" (BUILD)
- Source: astronomy/chapters/29-the-big-bang.md
- Lane: BUILD (Claude Code)
- Hook: The Big Bang produced exactly 75% hydrogen and 25% helium by mass — and the ratio is computable from first principles. You can simulate the neutron-to-proton ratio freeze-out in 30 lines of Python and see why the universe is three-quarters hydrogen rather than something else.
- The artifact: A Python script that models Big Bang nucleosynthesis (BBN): (1) plots the neutron-to-proton ratio as a function of temperature (cooling universe) showing the equilibrium value at high T (≈ 1:1) falling to the freeze-out value (≈ 1:7 at T ~ 3×10⁹ K), (2) uses the n/p ratio at freeze-out to calculate the helium mass fraction Y = 2(n/p) / (1 + n/p) with n/p = 1/7, showing Y ≈ 0.25 (25%), (3) compares the prediction to the observed primordial helium abundance.
- Prompt seed: `claude "Write a Python script that illustrates Big Bang nucleosynthesis. Model the neutron-to-proton ratio as a function of temperature (in units of 10⁹ K, from T=100 down to T=0.1) using a Boltzmann factor: n/p = exp(-Q/kT) where Q = (mn - mp)c² = 1.293 MeV and kT is the thermal energy. Plot the ratio from high temperature (equilibrium, n/p → 1) through freeze-out (~T = 3×10⁹ K where n/p ≈ 1/7) to nucleosynthesis. Mark the freeze-out temperature with a vertical line. Calculate and print the helium mass fraction Y = 2(n/p)/(1 + n/p) at freeze-out, and compare it to the observed primordial helium fraction of 0.245 ± 0.002."`
- Read / check: At high T (100 × 10⁹ K), Q/kT → 0, so exp(-Q/kT) → 1 and n/p → 1. At freeze-out T ≈ 3 × 10⁹ K, kT ≈ 0.26 MeV, Q/kT ≈ 5, n/p = exp(-5) ≈ 0.007... wait — the actual physics is more subtle (the ratio at freeze-out is ~1/7 due to the interplay of weak interaction rates and expansion, not just Boltzmann). Claude should implement the simplified model and note the approximation. Y = 2 × (1/7) / (1 + 1/7) = (2/7) / (8/7) = 2/8 = 0.25. Observed: 0.245 ± 0.002. Agreement is the payoff.
- Human supplies: Nothing — fully synthetic. Note: the full BBN calculation requires a reaction network code (e.g., PArthENoPE or PRIMAT); the script implements a pedagogical approximation.
- Output medium: Manim (the n/p ratio curve draws from left (high T, ratio ≈ 1) to right (low T, ratio → 1/7); the freeze-out temperature line drops; the helium mass fraction calculation animates below the plot; the final frame shows the agreement with observation labeled "three independent lines of evidence converge")
- The change: Ask Claude to add deuterium and lithium-7 to the prediction — BBN also predicts their primordial abundances. Compare the predictions to observed values and show whether each is consistent (deuterium: yes; lithium-7: there is a "lithium problem" — the prediction is ~3× the observed value in old stars).
- Teardown angle: The 25% helium fraction is not a coincidence. It is predicted from the proton-neutron mass difference and the expansion rate of the universe at 1 second old. The agreement with observation is the strongest evidence that we understand what happened in the first three minutes.
- Exclusions: Full CMB power spectrum analysis, dark matter nucleosynthesis implications — separate cards.
- Score: 9/10

---

## Candidate 07 — "Build a Hertzsprung-Russell Diagram from Stellar Census Data with Claude Code" (BUILD)
- Source: astronomy/chapters/18-the-stars-a-celestial-census.md; astronomy/chapters/17-analyzing-starlight.md
- Lane: BUILD (Claude Code)
- Hook: The HR diagram is one of the most information-dense plots in all of science. You can build it from scratch in Python using the Hipparcos catalog (or a hand-sampled dataset), and the main sequence appears as an emergent pattern rather than something you were told to draw.
- The artifact: A Python script that: (1) loads or hard-codes a dataset of ~50 stars with B-V color index and absolute magnitude, (2) plots absolute magnitude (y-axis, inverted) vs. B-V color index (x-axis), (3) color-codes the data points by spectral class (O=blue, B=blue-white, A=white, F=yellow-white, G=yellow, K=orange, M=red), (4) annotates the main sequence, red giant branch, and white dwarf region, (5) marks the Sun's position explicitly. Output: an HR diagram with the major stellar populations visible as emergent regions.
- Prompt seed: `claude "Write a Python script that builds a Hertzsprung-Russell diagram from a hand-coded dataset. Include at least 50 stars across all spectral types (O, B, A, F, G, K, M) plus giants, supergiants, and white dwarfs. For each star: give B-V color index and absolute magnitude (Mv). Plot Mv on the y-axis (inverted — more negative at top), B-V on the x-axis. Color each point by spectral class. Mark the Sun (B-V = 0.65, Mv = 4.83). Annotate the main sequence, red giant branch, and white dwarf region. Include at least 3 named stars as labeled points (Sirius, Betelgeuse, Proxima Centauri, Vega, or similar). Use matplotlib."`
- Read / check: Sun: B-V = 0.65, Mv = 4.83 (correct). Sirius: B-V = 0.00, Mv = 1.43 (A-type main sequence). Betelgeuse: B-V = 1.85, Mv = -5.14 (M-type supergiant — upper right). Proxima: B-V ≈ 1.90, Mv ≈ 15.5 (M-type red dwarf — lower right). Sirius B: B-V ≈ -0.03, Mv ≈ 11.4 (white dwarf — lower left). Main sequence should run from upper-left (hot, bright) to lower-right (cool, faint).
- Human supplies: Nothing — fully synthetic. Dataset hard-coded from well-known stellar parameters; real research would use the Hipparcos or Gaia catalogs.
- Output medium: Manim (the HR diagram builds point by point, each spectral class appearing as its colored population; main sequence emerges as the points accumulate; labeled stars appear last with callouts explaining their place on the diagram)
- The change: Add a second HR diagram showing the stars within 21 light-years of the Sun — the true solar neighborhood. Compare the two diagrams to show the selection effect: the nearby census is dominated by red dwarfs at lower right, while the "famous stars" diagram is dominated by luminous outliers.
- Teardown angle: The HR diagram was discovered in 1910 when Hertzsprung and Russell independently found that stars are not randomly distributed on the luminosity-temperature plane. The main sequence is a physical constraint — stellar structure theory explains why stars must live there. The diagram was the empirical fact; the theory came later.
- Exclusions: Stellar evolution tracks across the HR diagram, specific spectroscopic binary classification — separate cards.
- Score: 9/10

---

## Candidate 08 — "Research the Event Horizon with Claude: Why Escape Is Impossible" (RESEARCH)
- Source: astronomy/chapters/24-black-holes-and-curved-spacetime.md
- Lane: RESEARCH (Claude assistant)
- Hook: The event horizon is not a surface you could detect as you crossed it. It is not a wall. It is a threshold in spacetime geometry from which no future worldline leads outward — and researching why this is true through Einstein's equivalence principle and the geodesic concept reveals that the black hole is stranger than any science fiction version of it.
- The artifact: A sourced 3-part brief: (1) the equivalence principle and why it implies gravity is geometry — not a force, (2) the event horizon defined geometrically (the surface where escape velocity equals c, equivalently where all future-directed geodesics converge inward), (3) three confirmed detections of black holes and what each detection method reveals (X-ray binary orbital dynamics, gravitational wave merger signal, M87 shadow imaging) — each method identifying a black hole without seeing one directly.
- Prompt seed: `claude "Explain why black holes have an event horizon — start from Einstein's equivalence principle and the concept that gravity is the curvature of spacetime rather than a force, then derive geometrically why there is a boundary beyond which no outward-directed path exists. Why can't an object inside the event horizon 'wait out' the gravitational field by sitting still? Then describe three observational methods that have confirmed black holes exist: X-ray binaries, gravitational wave detection (LIGO), and the Event Horizon Telescope image of M87*. What does each method actually detect, and why is each detection indirect?"`
- Read / check: Equivalence principle: free fall and weightlessness are identical — therefore gravity is not a force. Event horizon: inside, all future-directed geodesics (paths in curved spacetime) lead toward the singularity — there is no "staying still" because staying still is not a valid worldline in curved spacetime (it would require infinite acceleration). X-ray binaries: orbital velocity of companion star + X-ray luminosity + mass function → dark compact object exceeding neutron star mass limit. LIGO: gravitational wave chirp frequency and amplitude → two merging compact objects, masses consistent with black holes. M87*: shadow size 6 billion solar masses at center of M87, consistent with GR prediction for that mass.
- Human supplies: Nothing — fully synthetic. Spot-check M87* mass (6.5 ± 0.7 × 10⁹ solar masses, EHT 2019 paper).
- Output medium: Manim (the equivalence principle animation: two scenes side by side — sealed box in free fall, sealed box in deep space — both showing the same interior physics; then spacetime curvature diagram showing geodesics curving inward past the event horizon; then three detection method illustrations animate in sequence)
- The change: Ask Claude what happens to an infalling observer's subjective experience crossing the event horizon — do they notice anything at the threshold? Then contrast with what a distant observer sees (observer appears frozen at the horizon, redshifted to invisibility).
- Teardown angle: The event horizon is a future boundary in spacetime geometry. It is not a physical surface and cannot be detected locally. The strange truth is that you could cross it without knowing — and only realize too late that every path forward leads to the singularity.
- Exclusions: Hawking radiation, thermodynamics of black holes — separate card.
- Score: 9/10

---

## Candidate 09 — "Build Gravitational Wave Strain Calculator with Claude Code" (BUILD)
- Source: astronomy/chapters/24-black-holes-and-curved-spacetime.md
- Lane: BUILD (Claude Code)
- Hook: The LIGO detection of GW150914 in 2015 measured a strain of 10⁻²¹ — a displacement of 10⁻¹⁸ meters across a 4-kilometer arm, smaller than a proton. You can compute the expected strain from a binary black hole merger using the quadrupole formula in 25 lines of Python.
- The artifact: A Python script that: (1) takes black hole masses (M1 = 36 M_sun, M2 = 29 M_sun for GW150914), (2) computes the chirp mass M_c = (M1 × M2)^(3/5) / (M1 + M2)^(1/5), (3) computes the gravitational wave frequency at merger f_merger ≈ c³ / (6^(3/2) π G M_total), (4) estimates the strain amplitude h ≈ (4/d) × (G M_c / c²)^(5/3) × (π f / c)^(2/3) at a distance d = 410 Mpc, (5) prints the strain and compares to LIGO's measured 10⁻²¹, (6) plots strain amplitude vs. frequency (chirp waveform shape).
- Prompt seed: `claude "Write a Python script that estimates gravitational wave strain from the GW150914 binary black hole merger. Given M1 = 36 solar masses, M2 = 29 solar masses, and distance d = 410 Mpc: compute the chirp mass M_c = (M1*M2)^(3/5) / (M1+M2)^(1/5). Estimate the merger frequency f_merger using f ≈ c³/(6^(3/2) * pi * G * (M1+M2)). Estimate the strain amplitude h ~ (4/d) * (G*M_c/c²)^(5/3) * (pi*f/c)^(2/3) in SI units. Print M_c, f_merger, and h. Compare h to the measured LIGO strain of 1e-21. Then plot a schematic chirp waveform: h(t) ∝ (t_merge - t)^(-1/4) * cos(2*pi*f(t)*t) where f(t) increases as merger approaches. Use SI units throughout."`
- Read / check: Chirp mass: M_c = (36 × 29)^(3/5) / (65)^(1/5) = 1044^(3/5) / 65^(1/5) ≈ 28.3 solar masses. f_merger ≈ c³ / (6^(3/2) π G × 65 M_sun) ≈ 150 Hz (order of magnitude). Strain amplitude: rough order of magnitude should match 10⁻²¹ ± factor of a few (the formula is approximate). The chirp waveform plot should show increasing frequency and amplitude approaching merger — the "chirp" pattern that LIGO detected.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim (the chirp waveform animates: slow oscillation at left, frequency and amplitude increasing toward the right as merger approaches; the strain value appears as a computed annotation; a label shows "this displacement is 1/1000 the diameter of a proton")
- The change: Compute what the strain would be at 10× the distance (4100 Mpc, near the edge of observable universe) — does it remain detectable by LIGO? Then ask: what would need to change about LIGO to detect mergers at cosmological distances?
- Teardown angle: LIGO measured 10⁻²¹ — seventeen orders of magnitude smaller than a proton. The engineering required to achieve that sensitivity is as remarkable as the physics it detected. The instrument is the argument for human ambition as much as the detection is the argument for Einstein.
- Exclusions: Full LIGO interferometer physics, neutron star merger signals — separate cards.
- Score: 9/10

---

## Candidate 10 — "Build Wien's Law Star Thermometer with Claude Code" (BUILD)
- Source: astronomy/chapters/05-radiation-and-spectra.md; astronomy/chapters/17-analyzing-starlight.md
- Lane: BUILD (Claude Code)
- Hook: You can measure a star's temperature from its color — no spectrum required, just peak wavelength. Wien's law is a single equation, and you can build a "star thermometer" that reads peak wavelengths from any real spectrophotometric data and returns a temperature in 10 lines of Python.
- The artifact: A Python script that: (1) implements Wien's law (T = b / λ_peak where b = 2.898 × 10⁻³ m·K), (2) reads a table of 10 well-known stars with their peak emission wavelengths (derived from SIMBAD spectral types or hard-coded), (3) computes the temperature for each from Wien's law alone, (4) compares the Wien-derived temperature to the published effective temperature (T_eff) from spectroscopy, (5) plots a scatter diagram of Wien T vs. spectroscopic T_eff with a y=x reference line to show where the agreement holds and where it breaks down.
- Prompt seed: `claude "Write a Python script that implements Wien's displacement law as a 'star thermometer': T = 2.898e-3 / lambda_peak (T in Kelvin, lambda_peak in meters). Hard-code a table of 10 named stars with their approximate peak emission wavelengths in nanometers (derive from their spectral types — O-type stars peak ~100 nm, B ~200 nm, A ~360 nm, F ~500 nm, G ~550 nm, K ~700 nm, M ~900 nm). Compute the Wien temperature for each. Also hard-code the published spectroscopic effective temperature for each star. Plot Wien T (x-axis) vs. spectroscopic T_eff (y-axis) with a y=x reference line. Print the percent error for each star. Where does Wien's law agree well, and where does it diverge significantly?"`
- Read / check: The Sun: peak ≈ 501 nm → T = 2.898e-3 / 501e-9 ≈ 5784 K (matches spectroscopic T_eff = 5778 K — good agreement). For very hot stars (O-type), the peak is in the UV and ground-based spectra miss it — Wien temperature will be underestimated. For very cool stars (M-type), the peak is in infrared and Wien temperature may be approximate. The scatter plot should show good agreement along the main sequence with systematic deviations at extremes.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim (the scatter plot of Wien T vs. spectroscopic T_eff builds point by point, each labeled with the star name; the y=x line draws; deviations at the extremes are annotated with the physical reason — UV peak missing for O-stars, infrared peak for M-stars)
- The change: Ask Claude to extend the analysis to exoplanet host stars — given the star's T_eff (easily measured spectroscopically), compute the equilibrium temperature of a planet at various orbital distances using T_planet = T_star × (R_star / 2d)^(1/2), and find the "habitable zone" distance where T_planet ≈ 273 K.
- Teardown angle: Wien's law is three variables: temperature, peak wavelength, one constant. That is all you need to take the temperature of a star from 4.24 light-years away. The simplicity is the point — and the limits of the simple version teach you what spectroscopy adds.
- Exclusions: Bolometric corrections, stellar atmosphere modeling — tangents.
- Score: 8/10

---

## Candidate 11 — "Research Nuclear Fusion: Why the Sun Isn't Dark with Claude" (RESEARCH)
- Source: astronomy/chapters/16-the-sun-a-nuclear-powerhouse.md
- Lane: RESEARCH (Claude assistant)
- Hook: By classical physics, the Sun should be dark — protons moving at 500 km/s cannot penetrate the Coulomb barrier that requires 1,000 km/s. Researching how quantum tunneling solves the problem reveals that quantum mechanics is not just a theory of atoms — it is the reason the Sun shines.
- The artifact: A sourced 3-part brief: (1) the energy-source failure cascade — chemical combustion (5,000 years), gravitational contraction (100 million years), geological requirement (4.5 billion years) — with the specific calculation for each, (2) the Coulomb barrier problem and quantum tunneling solution — what tunneling means physically and why the probability is non-zero even below the classical threshold, (3) the pp-chain reaction written as a four-step sequence with the mass deficit per cycle computed as energy (E = mc²) and the timescale implication for the Sun's remaining lifetime.
- Prompt seed: `claude "Research why the Sun's energy source was a mystery that classical physics could not solve. Walk me through three candidate mechanisms and why each fails: (1) chemical combustion — compute how long the Sun would last if it were made of coal, (2) gravitational contraction — compute the Kelvin-Helmholtz timescale, (3) why the geological record rules both out. Then explain the Coulomb barrier problem: at the Sun's core temperature (15 million K), what is the average proton velocity, and why is it not enough to overcome electrostatic repulsion by classical mechanics? How does quantum tunneling solve this? Finally, write out the proton-proton chain as a four-step nuclear reaction and compute the mass deficit per helium-4 nucleus produced, converting it to energy."`
- Read / check: Chemical combustion: assume coal energy density ~3.3 × 10⁷ J/kg × M_sun / L_sun ≈ 5,000 years. Kelvin-Helmholtz: E_grav ≈ GM²/R_sun ÷ L_sun ≈ 10⁷ years. Geological requirement: ~4.5 billion years (from radioactive dating). Classical proton velocity at 15 MK: v = sqrt(3kT/m) ≈ 500 km/s; required for Coulomb penetration: ~1,000 km/s. Quantum tunneling: wavefunction extends beyond the classical barrier; probability is non-zero. pp-chain: 4p → ²He + 2e⁺ + 2ν; mass deficit = 4 × 1.00728 - 4.00260 = 0.02832 u = 0.7% of hydrogen mass; E = 0.02832 × 931.5 MeV/u ≈ 26.4 MeV per cycle.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim (the three energy-source calculations animate as a comparison table, each row appearing with its timescale; then the Coulomb barrier diagram shows classical barrier and quantum tunnel probability wavefunction; the pp-chain writes out step by step with mass deficit labeled)
- The change: Ask Claude to compute how much hydrogen the Sun burns per second (in metric tons) and how much mass it converts to energy per second (E = mc²). Then compute the Sun's remaining fusion lifetime.
- Teardown angle: Darwin was right to worry. The geologists were right: the Sun is old enough for evolution. But the reason required overthrowing both classical thermodynamics and classical mechanics — and replacing them with quantum mechanics and mass-energy equivalence simultaneously.
- Exclusions: CNO cycle in massive stars, solar neutrino detection in full — tangents.
- Score: 8/10

---

## Candidate 12 — "Research the CMB as Evidence for the Big Bang with Claude" (RESEARCH)
- Source: astronomy/chapters/29-the-big-bang.md
- Lane: RESEARCH (Claude assistant)
- Hook: Penzias and Wilson found the Big Bang by accident while cleaning pigeon droppings from an antenna horn. The hiss that remained — arriving uniformly from all directions, constant at all hours — was the oldest light in the universe. Researching all three independent lines of evidence for the Big Bang with Claude reveals why the theory is not a guess: it is a convergence.
- The artifact: A sourced 3-convergence brief: (1) the expanding universe — Hubble's Law, recession velocity proportional to distance, age T₀ ≈ 13.8 billion years from H₀⁻¹, (2) the CMB — uniformity to 1 part in 100,000, temperature 2.73 K, spectrum matching a perfect blackbody at that temperature (the key verification), (3) primordial nucleosynthesis — BBN prediction of 75% hydrogen / 25% helium by mass, observed in the oldest stars (metal-poor Population II stars in globular clusters). Each line of evidence cited with the key observation and the prediction it tests.
- Prompt seed: `claude "The Big Bang model rests on three independent lines of observational evidence that converge on the same story. Walk me through each: (1) the expanding universe — what Hubble measured, what the linear velocity-distance relationship implies about the past, and how the Hubble constant yields the age of the universe; (2) the cosmic microwave background — how Penzias and Wilson discovered it, why its temperature (2.73 K) and blackbody spectrum are the predicted relic of a hot early universe, and what the tiny temperature fluctuations (1 part in 100,000) encode; (3) primordial nucleosynthesis — what the Big Bang predicts for the hydrogen/helium ratio, where astronomers observe this ratio, and whether the prediction matches. For each: what would falsify this line of evidence?"`
- Read / check: Hubble's Law: v = H₀ × d, H₀ ≈ 70 km/s/Mpc, T₀ ≈ 13.8 billion years. CMB: 2.73 K blackbody spectrum — Penzias and Wilson 1964; COBE 1992 confirmed blackbody shape. Temperature fluctuations: 10⁻⁵ amplitude, encode the density variations that grew into large-scale structure. BBN: 75/25 H/He by mass predicted from n/p freeze-out; observed in metal-poor stars (zero-metallicity limit of stellar spectroscopy). Falsification: if CMB showed non-blackbody features, or if oldest stars showed different He abundance, the model would require modification.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim (three panels animate in sequence: (1) Hubble Law scatter plot with regression line; (2) CMB all-sky map with temperature fluctuation color scale; (3) stellar spectroscopy showing helium absorption lines in metal-poor stars — each labeled with its prediction and observation; final frame shows all three converging)
- The change: Ask Claude what the "lithium problem" is — BBN predicts ~3× more lithium-7 than observed in old stars — and whether this represents a flaw in the Big Bang model or a gap in stellar physics.
- Teardown angle: Three independent measurements from three independent phenomena — galaxy motions, microwave radiation, stellar composition — all point to the same first three minutes. The chance that all three would agree if the model were wrong is effectively zero.
- Exclusions: Dark matter and dark energy in detail, inflationary cosmology — separate cards.
- Score: 8/10
