# Astronomy (Fry) — CLI Video Ideas ("X with Claude")

---

## Candidate 01 — "Build Kepler's Third Law Verifier with Claude Code"
- Source: astronomy-fry/chapters/03-orbits-and-gravity.md
- Lane: BUILD (Claude Code)
- Hook: Kepler's third law says P²=a³ for every planet — but it feels like magic until you watch it hold across Mercury, Jupiter, and Pluto simultaneously. Can Claude derive the formula AND verify it on the full solar system in one script?
- The artifact: an animated log-log scatter plot (Manim) of orbital period vs. semimajor axis for all 8 planets + Pluto + 5 dwarf planets, with the P²=a³ line drawn as the model, each point labeled, residuals displayed. The curve draws in as each planet's data is added.
- Prompt seed: `claude "Write a Python script that fetches planetary data from NASA's Horizons API, computes semimajor axis in AU and orbital period in years for every planet plus 5 dwarf planets, plots them on a log-log graph with the P^2=a^3 theoretical line, labels each body, and prints the residual percentage for each. Then generate a Manim animation that draws the line first, then adds each planet one by one."`
- Read / check: Verify the data source retrieves real orbital elements (not hardcoded). Verify the log-log slope is exactly 1.5 (P ∝ a^1.5). Check residuals are <1% for all planets. Inspect the animation shows the line first, then planets accumulating.
- Human supplies: Nothing — fully synthetic. NASA's public Horizons API is free and programmatic. A screen-recording of the Manim render is the deliverable.
- Output medium: Manim (animated log-log scatter, point-by-point reveal, residual table)
- The change: Add Newton's generalized version (a³ = (M1+M2)P²) and show how the planet's own mass shifts the Sirius binary off the solar-only line — demonstrating the correction Kepler couldn't make.
- Teardown angle: The law holds over 6 orders of magnitude in mass and 4 in period. What does that tell you about the universality of inverse-square gravity?
- Exclusions: Cut derivation of the law from first principles; cut historical Brahe dataset reconstruction; cut relativistic precession.
- Score: 9/10

---

## Candidate 02 — "Simulate Escape Velocity vs. Orbital Velocity with Claude Code"
- Source: astronomy-fry/chapters/03-orbits-and-gravity.md
- Lane: BUILD (Claude Code)
- Hook: Escape velocity is exactly √2 times orbital velocity — always. Claude can derive this in 10 lines and then animate Newton's cannonball thought experiment to show why.
- The artifact: A Manim animation of Newton's mountain: four cannonball trajectories at increasing speeds (sub-orbital, near-orbital, orbital, escape), each color-coded, with the surface of a curved Earth shown. A sidebar shows v_orbital and v_escape computed in real time for any input mass and radius.
- Prompt seed: `claude "Build a Manim scene that animates Newton's cannonball thought experiment on a curved Earth. Show four trajectories: 6 km/s (falls short), 7.9 km/s (orbits), 9 km/s (high ellipse), 11.2 km/s (escape). Compute v_orbital and v_escape from first principles using G, M_Earth, R_Earth. Color each trajectory differently and label with speed. Include a sidebar comparing v_escape = sqrt(2) * v_orbital."`
- Read / check: Check the trajectory physics — are the paths true conic sections? Verify v_escape/v_orbital = sqrt(2) is explicit in the code. Verify Earth's curvature is visible and to-scale enough to be instructive.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim (animated trajectories on curved-Earth canvas)
- The change: Add a second scene showing the same calculation for Mars — ask "why is it so much easier to launch from Mars?" and animate the lower escape velocity.
- Teardown angle: The √2 relationship is pure energy geometry. The mass cancels. This is why a feather and a rocket ship have the same escape velocity from Earth.
- Exclusions: Cut multi-body gravity assists; cut Hohmann transfer orbit math; cut Lagrange points.
- Score: 9/10

---

## Candidate 03 — "Plot Blackbody Spectra for Three Star Types with Claude Code"
- Source: astronomy-fry/chapters/05-radiation-and-spectra.md
- Lane: BUILD (Claude Code)
- Hook: A red dwarf and Sirius emit the same kind of light — but Wien's law says the peak wavelength changes by a factor of 3. Claude can plot three Planck curves and show why star color is a thermometer.
- The artifact: A Manim animation of overlapping Planck curves for a red dwarf (3,000 K), the Sun (5,800 K), and Sirius (10,000 K) — each curve drawing in one at a time, peak wavelength annotated, the visible band highlighted, and a final frame showing that only the Sun peaks inside the human eye's sensitivity range.
- Prompt seed: `claude "Write a Python script using scipy and matplotlib that plots the Planck blackbody radiation curves for temperatures 3000K, 5800K, and 10000K on the same axes (wavelength 100-3000nm, intensity normalized to peak). Mark the visible light band (400-700nm) as a shaded region. Mark each curve's peak using Wien's law. Export as data for a Manim animation that draws each curve sequentially, then reveals the visible band and annotates each peak."`
- Read / check: Verify the Planck formula is correct (B_λ = 2hc²/λ⁵ × 1/(exp(hc/λkT)-1)). Verify Wien's law peaks match: ~970nm, ~500nm, ~290nm. Check the visible-band shading ends at correct wavelengths (400-700nm).
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim (sequential Planck curve draws with visible-band overlay)
- The change: Add the Stefan-Boltzmann comparison: same luminosity from Betelgeuse (cool but huge) vs. a hot white dwarf (hot but tiny) — animate surface area compensating for temperature.
- Teardown angle: Temperature is the only variable. The shape of the curve is universal. The color of a star is a direct measurement of its surface temperature with no assumptions about what the star is made of.
- Exclusions: Cut quantum mechanics derivation of the Planck formula; cut atmospheric absorption; cut photometry filter systems.
- Score: 8/10

---

## Candidate 04 — "Compute Schwarzschild Radii Across 10 Orders of Magnitude with Claude Code"
- Source: astronomy-fry/chapters/24-black-holes-and-curved-spacetime.md
- Lane: BUILD (Claude Code)
- Hook: The Schwarzschild radius formula is the same for a pickup truck and a supermassive black hole — just 2GM/c². What does that size comparison actually look like?
- The artifact: A Manim size-comparison animation: a bar or circle whose radius scales logarithmically across pickup truck → Earth → Sun → Sgr A* → M87, each labeled with both mass and Schwarzschild radius, with a human figure as a scale reference. Values computed from first principles in the script.
- Prompt seed: `claude "Write a Python script that computes the Schwarzschild radius r_s = 2GM/c^2 for: (1) a 2000 kg pickup truck, (2) Earth, (3) the Sun, (4) Sagittarius A* (4 million solar masses), (5) M87's black hole (6.5 billion solar masses). Print each result in meters, compare to something familiar, and generate a Manim scene that visualizes all five on a log-scale ruler from 10^-24 m to 10^13 m with labeled comparison objects."`
- Read / check: Verify the formula — r_s = 2 × 6.674e-11 × M / (3e8)^2. Verify Earth → ~9mm, Sun → ~3km, Sgr A* → ~12 million km (compare to ~0.08 AU). Inspect that the log-scale animation makes the 28-order-of-magnitude span legible.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim (log-scale size comparison animation)
- The change: Add average interior density for each — show that supermassive black holes have lower average density than water, which is deeply counterintuitive.
- Teardown angle: The formula depends only on mass. Nothing about composition, history, or temperature. The universe is economical.
- Exclusions: Cut general relativity derivation; cut Hawking radiation; cut information paradox.
- Score: 8/10

---

## Candidate 05 — "Build the Cosmic Distance Ladder with Claude Code"
- Source: astronomy-fry/chapters/19-celestial-distances.md
- Lane: BUILD (Claude Code)
- Hook: Every distance in cosmology traces back to one geometric measurement made in 1838. Claude can simulate the full ladder — parallax to Cepheids to supernovae — and show where each rung's uncertainty propagates.
- The artifact: A Manim animated "ladder" diagram with four rungs (parallax → Cepheids → Type Ia supernovae → Hubble constant), each rung computing a sample distance and showing how uncertainty propagates upward. A sidebar shows the Hubble tension (73 vs 67 km/s/Mpc) as a gap between the two measurement methods.
- Prompt seed: `claude "Build a Python script that: (1) computes the distance to Sirius from its parallax of 0.379 arcsec; (2) computes the distance to a Cepheid in Andromeda from a 30-day period using the period-luminosity relation (L = L_sol × 10^(period/10), calibrated at 770 kpc); (3) shows how Type Ia supernovae extend this to z=1; (4) uses these to estimate H0. Then generate a Manim ladder animation showing each rung and the Hubble tension gap."`
- Read / check: Verify parsec conversion is correct (D = 1/p arcsec → parsecs → 3.26 ly/parsec). Verify Cepheid period-luminosity math produces plausible luminosities. Check the Hubble tension frame is labeled with both values (73 and 67).
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim (animated ladder with rung-by-rung propagation and Hubble tension callout)
- The change: Add an "error amplification" pass — show what a 1% error in parallax does to the Cepheid calibration and ultimately to the Hubble constant.
- Teardown angle: The ladder is only as strong as its bottom rung. Gaia's precision matters to cosmology because every rung above it inherits its uncertainty.
- Exclusions: Cut full CMB analysis; cut gravitational wave standard sirens; cut BAO distance method.
- Score: 9/10

---

## Candidate 06 — "Research the Discovery of Neptune's Existence Before It Was Seen with Claude"
- Source: astronomy-fry/chapters/03-orbits-and-gravity.md
- Lane: RESEARCH (Claude assistant)
- Hook: In 1846, Adams and Le Verrier calculated the position of an unseen planet from orbital deviations — and an astronomer found Neptune within one degree of the prediction. How good is this story, and what are the contested details?
- The artifact: A sourced 5-event timeline (prediction → independent calculation → telescope search → discovery → priority dispute) with key quantitative claims verified against primary sources (Galle's letter, Royal Astronomical Society records). Output is a formatted research brief with citations.
- Prompt seed: `claude "Research the discovery of Neptune in 1846. Construct a sourced timeline with at least 5 events from Adams's first prediction through Le Verrier's publication through Galle's observation to the priority dispute. For each event include: date, actors, the key calculation or observation made, and a primary or secondary source. Note any contested historical claims and what the current scholarly consensus is."`
- Read / check: Verify dates against Wikipedia and NASA history pages. Check whether Adams's 1845 prediction is accurately characterized (he did predict but wasn't acted on). Verify the angular distance between predicted and observed position.
- Human supplies: Access to JSTOR or Google Scholar for verifying primary source citations, if deep verification is needed. Wikipedia cross-check is sufficient for the video level. Nothing else — fully researchable.
- Output medium: slate (formatted timeline card, human fills with archival images from public domain NASA/RAS archives)
- The change: Extend to the Pluto non-discovery story — Le Verrier's method was also used to predict Pluto, but Pluto is far too small to cause Uranus's perturbations. The prediction was a coincidence.
- Teardown angle: The method works because gravity is the measuring instrument. The same technique now finds thousands of exoplanets.
- Exclusions: Cut full orbital perturbation math; cut general history of Uranus discovery; cut Planet Nine speculation.
- Score: 8/10

---

## Candidate 07 — "Research Cecilia Payne-Gaposchkin's Discovery That Stars Are Made of Hydrogen with Claude"
- Source: astronomy-fry/chapters/05-radiation-and-spectra.md
- Lane: RESEARCH (Claude assistant)
- Hook: In 1925, Payne showed stars are overwhelmingly hydrogen — and was told to hedge her conclusions because it contradicted accepted consensus. She was right. How did the spectroscopic argument actually work?
- The artifact: A sourced 3-section brief: (1) the spectroscopic reasoning chain Payne used (Saha ionization equation → temperature → hydrogen abundance), (2) who told her to hedge and why, (3) when the result was accepted and who ultimately got credit. Includes 4+ verifiable citations.
- Prompt seed: `claude "Research Cecilia Payne-Gaposchkin's 1925 PhD thesis discovery that stars are composed mainly of hydrogen. Explain: (1) what spectroscopic evidence and reasoning she used (specifically the Saha ionization equation and Harvard classification system); (2) who advised her to qualify her conclusions and why; (3) how Henry Norris Russell later confirmed the same conclusion; (4) how she is credited today. Include at least 4 verifiable citations."`
- Read / check: Verify the Saha equation connection — does Claude correctly explain how ionization state depends on temperature, allowing composition inference? Check that Russell's 1929 confirmation is accurately characterized and distinguished from Payne's 1925 thesis. Verify advisor identity (Otto Struve vs. Henry Norris Russell).
- Human supplies: Nothing — fully researchable from published sources. Payne's thesis is digitized.
- Output medium: slate (formatted research brief, human fills with historical portrait images in public domain)
- The change: Add the parallel question: what would have been the spectroscopic evidence if stars were iron-rich (as many assumed)? Would the Fraunhofer lines look different? Ask Claude to reason through the counterfactual.
- Teardown angle: The correct answer was in the data but rejected for sociological reasons. The science worked; the sociology didn't. This is a story about the lag between evidence and consensus.
- Exclusions: Cut full Harvard Computers history; cut Fraunhofer biography; cut current stellar nucleosynthesis details.
- Score: 8/10

---

## Candidate 08 — "Simulate the Proton-Proton Chain Mass Deficit with Claude Code"
- Source: astronomy-fry/chapters/16-the-sun-a-nuclear-powerhouse.md
- Lane: BUILD (Claude Code)
- Hook: The Sun converts 4 million metric tons of matter to energy every second — and the script to verify this is just 10 lines of physics. Claude can compute the 0.7% mass deficit and show exactly how the Sun has enough fuel to last 10 billion years.
- The artifact: A Python script that computes (1) the proton-proton chain mass deficit (4 × m_proton - m_helium4 in amu, then in joules), (2) the mass consumed per second to match the Sun's luminosity, (3) the fraction of the Sun's hydrogen converted so far in 4.5 Gyr, (4) remaining lifetime. Outputs a Manim infographic showing the three steps of the pp-chain as a flow diagram with mass balance numbers.
- Prompt seed: `claude "Write a Python script that computes the proton-proton chain. Use atomic mass data: 4 × proton mass (1.007276 amu) minus helium-4 mass (4.001506 amu). Convert the mass deficit to energy via E=mc^2. Compute: (1) energy per reaction, (2) mass consumed per second given L_sun = 3.828e26 watts, (3) fraction of Sun's hydrogen mass (0.74 × 2e30 kg) burned in 4.5 Gyr, (4) estimated remaining lifetime. Print all results and build a Manim flow diagram of the 3-step pp-chain with mass labels."`
- Read / check: Verify mass values are in correct units (amu × 1.66e-27 kg/amu). Verify E=mc² calculation: (0.027598 amu × 1.66e-27 kg/amu) × (3e8)^2 ≈ 4.1e-12 J per reaction, then scale to solar luminosity. Check fraction burned matches "about 4.5/10 = 45% through its lifetime."
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim (pp-chain flow diagram with mass labels + sidebar summary numbers)
- The change: Add the Kelvin-Helmholtz gravitational contraction alternative and show numerically why it fails by a factor of 100 — this was Darwin's problem.
- Teardown angle: The 0.7% that vanishes is not lost — it becomes the light hitting your face. The Sun's stability comes from a self-regulating thermostat, not brute force.
- Exclusions: Cut quantum tunneling derivation; cut CNO cycle; cut neutrino oscillation physics.
- Score: 9/10

---

## Candidate 09 — "Animate the H-R Diagram as a Stellar Census with Claude Code"
- Source: astronomy-fry/chapters/18-the-stars-a-celestial-census.md
- Lane: BUILD (Claude Code)
- Hook: The H-R diagram isn't just a plot — it's a time machine. The fraction of stars in each region encodes how long each phase lasts. Claude can build it from real Gaia data and animate evolutionary tracks.
- The artifact: A Manim animation that builds the H-R diagram using a CSV of ~1000 stars from the Gaia DR3 catalog (publicly available via astropy). Main sequence populates first, then giants appear, then white dwarfs. Three evolutionary tracks (high/solar/low mass) are overlaid, sweeping across the diagram at rates proportional to mass-dependent lifetimes.
- Prompt seed: `claude "Write a Python script using astropy to query ~1000 stars from the Gaia DR3 catalog within 100 parsecs, compute their absolute magnitudes and B-V colors, and output a CSV. Then build a Manim animation that plots the H-R diagram (absolute magnitude vs. B-V color index), reveals the main sequence, giants, and white dwarfs in sequence, overlays evolutionary tracks for 10, 1, and 0.5 solar-mass stars showing how position changes with age, and labels all three regions."`
- Read / check: Verify the Gaia query uses correct distance filter and proper motion parallax. Verify absolute magnitude calculation (M = m - 5 log10(d/10pc)). Check evolutionary tracks are correctly directed (high mass → upper left, then sweeps right toward giant branch).
- Human supplies: Internet access to query the Gaia archive (astropy/astroquery). The script handles this programmatically — no manual download needed.
- Output medium: Manim (progressive H-R diagram reveal from real data + animated evolutionary tracks)
- The change: Add the mass-luminosity relation L ∝ M^3.9 as a sidebar that explains why the main sequence is diagonal — show that moving along the sequence is moving in mass.
- Teardown angle: 90% of stars lie on the main sequence because stars spend 90% of their lives there. The diagram's population ratios are literally a clock.
- Exclusions: Cut spectral classification history; cut binary star mass measurement; cut white dwarf degeneracy pressure derivation.
- Score: 9/10

---

## Candidate 10 — "Research the Big Bang's Three Independent Lines of Evidence with Claude"
- Source: astronomy-fry/chapters/29-the-big-bang.md
- Lane: RESEARCH (Claude assistant)
- Hook: Three completely independent observations — galaxy recession, the CMB, and helium abundance — all point to the same hot dense beginning. Can Claude assemble a brief that explains why no other cosmological model predicts all three?
- The artifact: A 3-panel sourced brief: (1) Hubble's law and the age estimate (sources: Hubble 1929, Planck 2018), (2) the CMB — Penzias & Wilson discovery, acoustic peaks, composition constraints (sources: Penzias & Wilson 1965, Planck collaboration 2020), (3) Big Bang nucleosynthesis predictions vs. measured He/H and D/H ratios (sources: Gamow & Alpher 1948, current observational papers). Each panel includes 2+ verifiable citations and a one-line "what other models get wrong" note.
- Prompt seed: `claude "Research the three independent lines of evidence for the Big Bang: (1) the expanding universe and Hubble's law, (2) the cosmic microwave background, (3) Big Bang nucleosynthesis and light element abundances. For each line: describe the key observation, the key prediction it confirms, one historical figure central to it, at least 2 verifiable citations, and what a non-Big-Bang cosmology would predict instead. Format as a sourced comparison brief."`
- Read / check: Verify the CMB temperature (2.725K, not 2.73K — the precise value). Verify helium mass fraction prediction (25%) and measured value (~24-25%). Verify deuterium abundance cited matches current observational estimates. Check that the "Steady State" model is correctly identified as the main competing historical alternative.
- Human supplies: Access to arXiv or NASA ADS for checking cosmology citations. Wikipedia cross-check is sufficient for video production.
- Output medium: slate (3-panel brief with sourced claims, human fills with NASA Planck CMB images which are public domain)
- The change: Add the Hubble tension as a fourth current open question — show that the three independent measurements agree, but there's now a fourth measurement (local H0 vs. CMB H0) that doesn't.
- Teardown angle: Convergence of three independent methods is the strongest argument for a scientific framework. The Big Bang is not one measurement — it's three that couldn't all be right unless the framework is correct.
- Exclusions: Cut inflationary cosmology details; cut dark matter particle candidates; cut future of the universe.
- Score: 8/10

---

## Candidate 11 — "Simulate the Hubble Tension Numerically with Claude Code"
- Source: astronomy-fry/chapters/19-celestial-distances.md
- Lane: BUILD (Claude Code)
- Hook: Two careful measurements of the universe's expansion rate disagree by 9%. Claude can simulate how uncertainty in each rung of the distance ladder propagates into H0 and show exactly where the tension lives.
- The artifact: A Python script that models the distance ladder with calibrated uncertainties: parallax error → Cepheid period-luminosity scatter → supernova calibration → H0. Monte Carlo sampling shows the resulting H0 distribution. A second distribution from the CMB value is overlaid. Manim animates both distributions building up, with the 9% gap highlighted.
- Prompt seed: `claude "Write a Python Monte Carlo simulation of the cosmic distance ladder: start with 1000 sample stars with parallax uncertainty of 0.01 arcsec, propagate to Cepheid calibration (assume 0.1 mag scatter in period-luminosity relation), then to Type Ia supernova distances (0.15 mag scatter), then compute H0. Run 10,000 trials. Plot the resulting H0 distribution. Overlay the CMB H0 = 67.4 km/s/Mpc value. Animate the two distributions building up in Manim and highlight the gap."`
- Read / check: Verify the Monte Carlo correctly draws uncertainties at each step (not just at the final step). Verify that the resulting H0 distribution is centered near 73 km/s/Mpc with appropriate width. Check the CMB value is correctly labeled as the Planck 2018 result.
- Human supplies: Nothing — fully synthetic simulation.
- Output medium: Manim (two H0 distributions building up via Monte Carlo, gap highlighted)
- The change: Add a third scenario: "what if Cepheid calibration has a systematic 2% bias" — show how the distributions shift and whether the tension resolves.
- Teardown angle: A 9% disagreement between two careful methods is not noise — it's either the most significant systematic error in modern cosmology or the first hint of new physics.
- Exclusions: Cut full CMB power spectrum analysis; cut dark energy equation of state; cut gravitational wave standard sirens.
- Score: 8/10

---

## Candidate 12 — "Research the Solar Neutrino Problem and Its Resolution with Claude"
- Source: astronomy-fry/chapters/16-the-sun-a-nuclear-powerhouse.md
- Lane: RESEARCH (Claude assistant)
- Hook: For 30 years, the Sun appeared to produce only one-third the predicted neutrinos. The solar model was correct — the particle physics was wrong. Claude can reconstruct the detective story.
- The artifact: A 4-event sourced timeline: (1) Davis's 1970 Homestake experiment and the one-third deficit, (2) helioseismology confirming the solar model, (3) the Sudbury detector's 1999 three-flavor measurement, (4) the Nobel Prize 2015. Each event includes key numbers (tank size, measured vs. predicted count, SNO heavy water volume) and 2+ verifiable citations.
- Prompt seed: `claude "Research the solar neutrino problem from 1970 to 2015. Construct a 4-event sourced timeline covering: (1) the Homestake experiment (year, setup, measured vs. predicted count, Ray Davis's reaction); (2) how helioseismology ruled out a wrong solar model; (3) the Sudbury Neutrino Observatory result showing total neutrino flux matched predictions; (4) the 2015 Nobel Prize. Include key quantitative claims and at least 2 verifiable citations per event."`
- Read / check: Verify Homestake used 400,000 liters (not 400 liters) of tetrachloroethylene. Verify SNO used heavy water (D2O). Verify Nobel Prize year (2015, Kajita and McDonald). Check the fraction detected at Homestake (~1/3 of predicted).
- Human supplies: Nothing — fully researchable. SNOLAB and Homestake historical records are public.
- Output medium: slate (4-event timeline brief, human fills with historical lab photos from publicly available SNOLAB/Brookhaven archives)
- The change: Extend to the implication: neutrinos must have mass (they can only oscillate between flavors if massive). Ask Claude to quantify the upper bound on neutrino mass from oscillation data.
- Teardown angle: The Sun was correctly understood; the particle was not. Fixing the physics of the particle gave us a new measurement of what the Standard Model was missing.
- Exclusions: Cut full Standard Model review; cut reactor neutrino experiments; cut Daya Bay/RENO experiments.
- Score: 7/10
