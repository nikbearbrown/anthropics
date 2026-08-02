# Astronomy: with LLMs — CLI Video Ideas ("X with Claude")

---

## Candidate 01 — "Build Kepler's Third Law Verifier with Claude Code" (LLM Exercise harvest)
- Source: astronomy-with-llms/chapters/03-orbits-and-gravity.md — LLM Exercise
- Lane: BUILD (Claude Code)
- Hook: Kepler's law holds across the entire solar system — P²=a³ — but what does it mean that the units (Earth-years and AU) absorb the gravitational constant? Claude can derive the full formula AND verify why P²=a³ is a special case of Newton's more general law.
- The artifact: A Manim animated log-log scatter plot of P² vs a³ for all planets + selected moons + Halley's comet (period 75.3 yr → a computed), with the Newton-derived theoretical line, residuals labeled per body, and a sidebar showing the full G, M_sun derivation that collapses to the unit-absorbed Kepler form.
- Prompt seed: `claude "Write a Python script that: (1) uses G=6.674e-11, M_sun=1.989e30 to derive Kepler's third law T^2 = (4pi^2/GM) a^3; (2) shows why plugging in years and AU reduces constants to 1; (3) verifies the law for 8 planets, Halley's comet (a=17.8 AU, P=75.3 yr), and Europa orbiting Jupiter (derive Jupiter's mass from Europa's orbit). Animate the log-log plot in Manim with each body revealed sequentially."`
- Read / check: Verify the unit absorption derivation is shown explicitly in code comments. Verify Europa is used with Jupiter's actual mass (not Sun's). Verify Halley's computed semi-major axis matches 17.8 AU within 5%.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim (animated log-log scatter with Kepler line, residuals, derivation sidebar)
- The change: Add the Newton generalization (a³ = (M1+M2)P²) and apply it to the Sirius binary (M_total = 3.2 solar masses) — show how the formula needs both masses when they're comparable.
- Teardown angle: The law works because angular momentum is conserved and inverse-square gravity is universal. The unit simplification is a convenience — the physics is there regardless.
- Exclusions: Cut relativistic orbital precession; cut multi-body N-body simulation; cut tidal locking.
- Score: 9/10

---

## Candidate 02 — "Compute Orbital Velocities at LEO and GEO with Claude Code" (LLM Exercise harvest)
- Source: astronomy-with-llms/chapters/03-orbits-and-gravity.md — LLM Exercise
- Lane: BUILD (Claude Code)
- Hook: Higher orbits are slower — that feels backwards. A satellite at geostationary orbit moves at 3 km/s while the ISS screams past at 7.68 km/s. Claude can compute the full v(r) curve and animate why the counterintuitive direction is forced by Newton's law.
- The artifact: A Manim animation of a v_orbital vs altitude curve from just above Earth's surface to geostationary orbit (36,000 km), with ISS (400 km, 7.68 km/s) and GEO (35,786 km, 3.07 km/s) marked. A second panel shows the inverse-square-root relationship as the physics behind the curve.
- Prompt seed: `claude "Write a Python script that computes orbital velocity v = sqrt(GM/r) for altitudes from 100 km to 40,000 km above Earth, using G=6.674e-11 and M_Earth=5.972e24 kg and R_Earth=6.371e6 m. Plot the curve. Mark ISS at 400 km and GEO at 35786 km. Then build a Manim animation that draws the curve and reveals each satellite's position, with a sidebar showing why higher orbits are slower."`
- Read / check: Verify ISS speed computes to ~7.66 km/s and GEO to ~3.07 km/s. Verify the v ∝ r^(-1/2) relationship is annotated. Check that the sidereal day (86,164 s) vs solar day (86,400 s) distinction is addressed for GEO period.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim (v vs altitude curve with satellite markers + physics sidebar)
- The change: Add escape velocity v_esc = sqrt(2GM/r) as a second curve on the same plot — show the √2 ratio at every altitude and explain why the ratio is exact.
- Teardown angle: The inverse relationship is not a coincidence — it reflects that higher orbits have more energy (despite being slower) because potential energy dominates kinetic. Gravity stores energy in a way our intuition about speed doesn't capture.
- Exclusions: Cut Hohmann transfer orbit calculation; cut drag effects on LEO decay; cut Lagrange points.
- Score: 9/10

---

## Candidate 03 — "Plot Stellar Blackbody Curves and Infer Temperature with Claude Code" (LLM Exercise harvest)
- Source: astronomy-with-llms/chapters/05-radiation-and-spectra.md — LLM Exercise
- Hook: Vienna's displacement law converts star color to temperature without touching the star. Claude can build an interactive reverse-engineering tool: given a "bright blue-white" description, what temperature does Wien predict? And which Balmer lines would be visible?
- The artifact: A Python script that: (1) prompts for a star color description, (2) Claude reasons to a temperature estimate via Wien's law, (3) generates the Planck curve for that temperature, (4) marks which Balmer hydrogen lines fall inside vs. outside the visible range, (5) predicts whether H is ionized (>10,000 K → fewer visible Balmer lines). Manim animates the Planck curve and marks the lines.
- Prompt seed: `claude "Build a CLI tool that: (1) accepts a stellar color description (e.g., 'blue-white like Rigel'); (2) reasons using Wien's law to estimate surface temperature; (3) generates the Planck blackbody curve for that temperature; (4) marks the first 4 Balmer hydrogen lines (656nm, 486nm, 434nm, 410nm) and labels which are in the visible band; (5) notes whether hydrogen is ionized at this temperature (T>10000K means fewer visible Balmer lines). Then animate in Manim."`
- Read / check: Verify the Wien's law inversion is correct (T = 2.9e-3 / λ_peak). Verify that the Balmer series visibility logic matches: Rigel (~11,000 K) is too hot for maximum Balmer absorption. Verify ionization threshold statement.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim (Planck curve with Balmer line markers, ionization state annotation)
- The change: Add the "full spectrum read" — given a fictional spectrum with Doppler shift, line widths, and ionization state, ask Claude to extract temperature, velocity, and rotation speed simultaneously.
- Teardown angle: Every measurement is extracted from light that traveled years to reach us. The laws of physics being universal is what makes spectroscopy work. If atomic energy levels varied by location, the fingerprints would be unreadable.
- Exclusions: Cut derivation of Saha equation; cut telescope instrumentation; cut stellar classification history.
- Score: 9/10

---

## Candidate 04 — "Simulate the Proton-Proton Chain and Solar Neutrino Problem with Claude Code" (LLM Exercise harvest)
- Source: astronomy-with-llms/chapters/16-the-sun-a-nuclear-powerhouse.md — LLM Exercises
- Lane: BUILD (Claude Code)
- Hook: The Sun produces billions of neutrinos per second — but only 1 in 3 was detected for 30 years. The detector was right. The particle had a property nobody had predicted. Claude can compute the mass deficit, model the Davis experiment, and show the Sudbury resolution.
- The artifact: A three-panel Manim animation: (1) pp-chain flow diagram with mass balance (4H → He4 + 0.7% energy), (2) Davis experiment schematic showing "1/3 detected" vs predicted, (3) SNO three-flavor diagram showing total = predicted but electron-flavor = 1/3. Python script computes the energy yield and neutrino production rate from first principles.
- Prompt seed: `claude "Write a Python script computing: (1) the proton-proton chain mass deficit (4×1.007276 - 4.001506 amu, converted to joules); (2) neutrinos produced per second given Sun's luminosity = 3.828e26 W; (3) flux at Earth's surface (1 AU away). Then build a Manim 3-panel animation: pp-chain flow, Davis chlorine tank showing 1/3 detection, SNO heavy water showing all 3 flavors totaling 100% of prediction."`
- Read / check: Verify neutrino flux at Earth (~6.5×10^10 per cm^2 per second) matches published values. Verify the Davis result (1/3 detected) is labeled correctly. Verify SNO result (total = predicted, electron = 1/3) is correctly explained as neutrino oscillation proof.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim (3-panel: pp-chain flow + Davis tank + SNO three-flavor result)
- The change: Add the "if neutrinos have mass" implication — compute an upper bound on neutrino mass from the oscillation length and solar distance.
- Teardown angle: The Sun was correctly modeled. The mistake was in particle physics — neutrinos have mass, which Standard Model theorists initially resisted. The solar neutrino problem corrected particle physics, not astrophysics.
- Exclusions: Cut nuclear tunneling derivation; cut neutrino mass hierarchy; cut reactor neutrino experiments.
- Score: 9/10

---

## Candidate 05 — "Build the Cosmic Distance Ladder with Error Propagation with Claude Code" (LLM Exercise harvest)
- Source: astronomy-with-llms/chapters/19-celestial-distances.md — LLM Exercises
- Lane: BUILD (Claude Code)
- Hook: A 0.3% error in Sirius's parallax produces a 0.3% error in its distance — because parallax and distance are inverse. But what happens to that error as it propagates through the Cepheid calibration and up to the Hubble constant? Claude can trace it.
- The artifact: A Python script that computes: (1) Sirius distance from parallax 0.379", (2) error from 0.380" vs 0.379" — shows ~0.26% distance error, (3) Andromeda Cepheid distance from 30-day period (L = 10,000 L_sun) and apparent brightness 5e-19 W/m², (4) compares to known 2.5 Mly. Manim animates the ladder with each rung's uncertainty bounds growing.
- Prompt seed: `claude "Write a Python script that: (1) computes Sirius distance from parallax 0.379 arcsec; (2) shows the distance error from a 0.380 arcsec measurement (is error linear or nonlinear?); (3) computes Andromeda distance from Cepheid: period=30d, L=10000 L_sun=3.83e30 W, apparent brightness b=5e-19 W/m^2, using d=sqrt(L/(4*pi*b)); (4) compares to 2.5 million ly. Animate the distance ladder in Manim with error bars that widen at each rung."`
- Read / check: Verify Sirius calculation: D = 1/0.379 = 2.638 pc = 8.60 ly (known value 8.6 ly — correct). Verify error propagation is truly ~0.26% (not 0.3%). Verify Cepheid calculation yields value close to 2.5 Mly. Check error bars widen at each rung in animation.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim (animated distance ladder with widening error bars at each rung)
- The change: Add the Hubble tension at the top — show that a systematic 2% shift in Cepheid calibration could explain the 9% H0 discrepancy (it can't — the math doesn't work out), which means new physics is needed.
- Teardown angle: The ladder is epistemically asymmetric — errors can propagate up but can't be reduced from the top. Gaia's bottom-rung precision matters more than any improvement at higher rungs.
- Exclusions: Cut CMB power spectrum calculation; cut gravitational wave standard sirens; cut BAO distance method.
- Score: 9/10

---

## Candidate 06 — "Compute Schwarzschild Radii and Black Hole Shadow Sizes with Claude Code" (LLM Exercise harvest)
- Source: astronomy-with-llms/chapters/24-black-holes-and-curved-spacetime.md — LLM Exercises
- Lane: BUILD (Claude Code)
- Hook: The EHT photographed M87's black hole at 40 microarcseconds resolution — matching exactly what GR predicts for a 6.5-billion-solar-mass black hole at 55 Mly. Claude can compute both sides of this verification from first principles.
- The artifact: A Python script that computes: (1) Schwarzschild radii for 1, 10, and 1e9 solar masses; (2) the predicted shadow angular size for M87 using θ = ~5.2 R_s / d and verifies it matches the EHT result of 40 μas; (3) the same for Sgr A* (4e6 M_sun, 8 kpc); (4) a Manim animation comparing both shadows to their respective distance-scale contexts.
- Prompt seed: `claude "Write a Python script computing: (1) Schwarzschild radius r_s = 2GM/c^2 for 1, 10, and 1e9 solar masses; (2) angular size of M87 black hole shadow: r_s for 6.5e9 M_sun at 55 Mly, convert to microarcseconds and compare to EHT measurement of 40 µas; (3) same for Sgr A* (4e6 M_sun, 8 kpc). Animate both results in Manim showing how the shadow size equals the EHT measurement."`
- Read / check: Verify M87 r_s ≈ 1.9e13 m. Verify angular size calculation: θ = r_s / d in radians × 206265 arcsec → μas. Verify result is near 40 μas. Verify Sgr A* shadow is also computable (~50 μas — larger in angular size despite smaller mass because it's much closer).
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim (shadow size comparison with EHT measurement verification for both M87 and Sgr A*)
- The change: Add Hawking radiation evaporation time estimate for a 1-solar-mass black hole — show t ≈ 2e67 years, compare to age of universe (1.4e10 years), making clear this has never been and will never be observed.
- Teardown angle: GR's predictions hold across 28 orders of magnitude in mass with no free parameters. The shadow shape, size, and brightness distribution all matched the theory before the image was taken.
- Exclusions: Cut GR field equations; cut interior Schwarzschild metric; cut information paradox.
- Score: 8/10

---

## Candidate 07 — "Simulate CMB Acoustic Peaks and What They Measure with Claude Code" (LLM Exercise harvest)
- Source: astronomy-with-llms/chapters/29-the-big-bang.md — LLM Exercise
- Lane: BUILD (Claude Code)
- Hook: The CMB power spectrum has three acoustic peaks — and their positions and heights encode the geometry of space, the baryon density, and the dark matter density. Claude can compute what the peaks would look like if the universe had different composition.
- The artifact: A Python script using a simplified CMB power spectrum model (or calling CAMB if available, otherwise analytic approximation) that generates the C_l vs l curve for three cosmologies: (1) standard ΛCDM, (2) twice the baryon density, (3) no dark matter. A Manim animation overlays all three curves, highlighting how each peak shifts or grows, with annotation of what each peak encodes.
- Prompt seed: `claude "Build a Python script that generates a simplified CMB angular power spectrum for three cosmologies using the analytic approximation for acoustic peaks: (1) standard ΛCDM (Omega_b=0.05, Omega_DM=0.27); (2) doubled baryon density (Omega_b=0.10); (3) no dark matter (Omega_DM=0). Plot C_l vs multipole l from l=2 to l=2000. Annotate where the first peak (flat universe geometry), second peak (baryon density), and third peak (dark matter density) appear. Animate the three curves in Manim."`
- Read / check: Verify that doubling baryon density increases the second peak amplitude (baryons fall into potential wells, enhancing odd peaks vs. even). Verify that removing dark matter changes the third peak. Verify first peak position is near l=220 for flat space.
- Human supplies: Nothing — fully synthetic (analytic approximation). If CAMB is available, results improve.
- Output medium: Manim (three-cosmology CMB power spectrum overlay with peak annotations)
- The change: Add a Hubble tension scenario — show what happens to the derived H0 if the first peak position shifts by 1%.
- Teardown angle: The CMB is not just pretty — it's a precision measurement. Every peak position and height is a different cosmological number, and the universe has been consistent across all of them.
- Exclusions: Cut Boltzmann equation derivation; cut polarization spectrum; cut inflation physics in detail.
- Score: 8/10

---

## Candidate 08 — "Research Big Bang Nucleosynthesis Predictions vs. Measured Abundances with Claude"
- Source: astronomy-with-llms/chapters/29-the-big-bang.md — LLM Exercise
- Lane: RESEARCH (Claude assistant)
- Hook: Gamow and Alpher computed in 1948 that the Big Bang should produce ~25% helium by mass — before any precision measurement existed. The measured value is 24-25%. Claude can reconstruct the prediction and verify it against current data.
- The artifact: A sourced 3-section brief: (1) the nucleosynthesis prediction (neutron:proton freeze-out ratio, reaction network, He/H and D/H predictions), (2) current measured values vs. predictions with error bars (He mass fraction, D/H, Li-7), (3) the lithium problem — why lithium is off by a factor of 3 and what the competing explanations are. Includes 4+ verifiable citations.
- Prompt seed: `claude "Research Big Bang nucleosynthesis. Describe: (1) how Gamow and Alpher (1948) computed the neutron-proton freeze-out ratio and predicted helium mass fraction ~25%; (2) current measured values for He mass fraction (cite specific observations of metal-poor HII regions), D/H ratio (cite quasar absorption studies), and Li-7 (cite metal-poor star measurements); (3) the lithium problem — predicted vs. observed factor-of-3 discrepancy and the 3 main proposed explanations. Include at least 4 verifiable citations."`
- Read / check: Verify helium mass fraction prediction (25%) and measured value (~24-25%). Verify D/H measured value (~2.5e-5) from quasar absorption line studies. Verify Li-7 discrepancy factor (×3 lower than predicted). Check that all 3 explanations for the lithium problem are current (stellar processing, nuclear physics gaps, new physics).
- Human supplies: Access to arXiv for citation verification. Wikipedia cross-check is sufficient for video.
- Output medium: slate (3-panel brief with prediction-vs-measurement table, human fills with Gamow-era lab photos if available via public archives)
- The change: Ask Claude to compute what the He/H ratio would be if neutron half-life were 10% shorter — show how the prediction changes and whether it would still match the measurement.
- Teardown angle: BBN works because the universe had a specific thermal history during a specific 3-minute window. No other cosmological model predicted these ratios before they were measured.
- Exclusions: Cut quark-gluon plasma era; cut inflationary baryogenesis; cut dark matter nucleosynthesis effects.
- Score: 8/10

---

## Candidate 09 — "Research Henrietta Leavitt's Period-Luminosity Discovery with Claude"
- Source: astronomy-with-llms/chapters/19-celestial-distances.md — AI Wayback Machine
- Lane: RESEARCH (Claude assistant)
- Hook: Leavitt found the key to measuring galaxy distances in 1908 — while being paid 30 cents an hour and not allowed to use the telescopes. Claude can reconstruct the reasoning chain she actually used from photographic plates of the LMC.
- The artifact: A sourced 3-section brief: (1) the observational setup — what data Leavitt actually had (photographic plates of LMC Cepheids, apparent magnitude vs. period), (2) why the LMC location was crucial (all at same distance → apparent brightness differences are intrinsic), (3) how the relation was later calibrated against parallax by others and used by Hubble to measure Andromeda. Includes 4+ verifiable citations.
- Prompt seed: `claude "Research Henrietta Swan Leavitt's discovery of the Cepheid period-luminosity relation. Explain: (1) what her actual data looked like (photographic plates, apparent magnitudes of LMC Cepheids, period measurements); (2) why the LMC location was scientifically crucial — not just convenient; (3) how the relation was calibrated by others after her death and used by Hubble; (4) what prevented her from being credited — and whether she was nominated for a Nobel Prize. Include at least 4 verifiable citations."`
- Read / check: Verify the LMC distance (~160,000 ly) and why same-distance argument is valid. Verify Leavitt's 1908 paper date. Verify the Nobel nomination story (Mittag-Leffler did write to her, but she had died in 1921). Check that Shapley's role in calibrating the relation is accurately characterized.
- Human supplies: Nothing — fully researchable. Leavitt's original 1908 paper is publicly available (Harvard Observatory Circular).
- Output medium: slate (3-section brief, human fills with digitized photographic plates from Harvard plate collection — public access available)
- The change: Ask Claude to walk through the exact calculation: given a Cepheid with a 10-day period in the LMC, compute its intrinsic luminosity and then its distance if seen in Andromeda with apparent magnitude 20.
- Teardown angle: Leavitt found the cosmic distance ladder's foundation while unable to operate the instruments. The discovery came from analysis of archival plates, not from telescope time. This is a story about what work is valued.
- Exclusions: Cut full history of the Harvard Computers; cut Cannon's spectral classification; cut current Gaia Cepheid calibration.
- Score: 8/10

---

## Candidate 10 — "Build an H-R Diagram from Gaia Data with Evolutionary Tracks with Claude Code"
- Source: astronomy-with-llms/chapters/18-the-stars-a-celestial-census.md — LLM Exercises
- Lane: BUILD (Claude Code)
- Hook: The H-R diagram built from real Gaia parallax data shows that 90% of stars live on the main sequence — which encodes the fact that stars spend 90% of their lives there. Claude can build this from live data and animate the lifetime relationship.
- The artifact: A Python/astropy script that queries Gaia DR3 for ~500 stars within 100 pc, computes absolute magnitude and B-V color, plots the H-R diagram, then uses the mass-luminosity relation L ∝ M^3.9 and lifetime ∝ M/L to animate evolutionary tracks for 0.5, 1, and 10 solar mass stars sweeping across the diagram.
- Prompt seed: `claude "Write a Python script using astroquery to fetch 500 Gaia DR3 stars within 100 pc. Compute absolute G magnitude (M_G = G - 5*log10(d/10pc)) and BP-RP color. Plot the H-R diagram (M_G vs BP-RP). Then calculate evolutionary track lifetimes using L ~ M^3.5 and lifetime ~ M/L ~ M^{-2.5}: for 0.5, 1.0, 10.0 solar masses. Animate in Manim: build the diagram from data, then sweep 3 colored tracks from main sequence toward the giant branch."`
- Read / check: Verify the distance calculation uses parallax correctly (d = 1000/parallax_mas pc). Verify lifetime scaling: 10 M_sun → ~30 Myr, 1 M_sun → ~10 Gyr, 0.5 M_sun → ~80 Gyr (all roughly correct with M^{-2.5}). Check that the 90% main-sequence fraction appears in the data.
- Human supplies: Internet access for Gaia archive query (astroquery handles this). No manual download needed.
- Output medium: Manim (H-R diagram built from real Gaia data + 3 animated evolutionary tracks)
- The change: Add the Salpeter IMF (ξ(M) ∝ M^{-2.35}) as a mass distribution overlay — show that the diagram's population counts match the IMF prediction (many low-mass stars, few high-mass stars visible).
- Teardown angle: The H-R diagram is a census and a clock simultaneously. The fraction of stars in each region is a direct measurement of how long each phase lasts.
- Exclusions: Cut white dwarf cooling track calculation; cut spectral type classification history; cut binary star contamination.
- Score: 9/10

---

## Candidate 11 — "Simulate the Stellar Mass-Luminosity Relation and Binary Star Mass Measurement with Claude Code"
- Source: astronomy-with-llms/chapters/18-the-stars-a-celestial-census.md — LLM Exercises
- Lane: BUILD (Claude Code)
- Hook: Half of all stars are in binary systems — and that's lucky, because binaries are the only way to directly measure stellar mass. The Sirius system calculation takes 4 lines of Newton's law. Claude can build the full analysis.
- The artifact: A Python script that applies Newton's form of Kepler's third law (D^3 = (M1+M2)P^2) to: (1) Sirius binary (D=20 AU, P=50 yr → M_total=3.2 M_sun), (2) a hypothetical binary with D=8 AU, P=16 yr → total mass derived, then mass ratio from speed ratio. Manim animates a binary orbit and shows the Doppler spectral line oscillation that reveals the velocity ratio.
- Prompt seed: `claude "Write a Python script applying Newton's Kepler third law D^3=(M1+M2)P^2 (D in AU, P in years, M in solar masses) to: (1) Sirius (D=20 AU, P=50 yr — compute total mass); (2) a binary where one star moves 3× faster than the other — compute mass ratio and individual masses given total mass 2.0 M_sun. Then build a Manim animation of the binary orbit showing both stars orbiting the center of mass, with Doppler spectral line splitting/merging at orbital frequency."`
- Read / check: Verify Sirius total mass = 20^3 / 50^2 = 8000/2500 = 3.2 M_sun (correct). Verify faster star = less massive star (momentum conservation). Verify the Doppler animation shows lines separating and coming together periodically.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim (binary orbit animation with Doppler spectral line oscillation)
- The change: Add the mass-luminosity plot — given L ∝ M^3.5, plot luminosity predictions for measured binary masses and compare to observed luminosities.
- Teardown angle: Binary stars are the calibration standard for everything we know about stellar masses. Without them, the mass-luminosity relation would be hypothetical. Half the sky is binaries; that's the only reason we know what a star weighs.
- Exclusions: Cut spectroscopic binary type derivation; cut eclipsing binary light curves; cut triple/quadruple system complications.
- Score: 8/10

---

## Candidate 12 — "Research Karl Schwarzschild's Wartime Solution and Its Delayed Impact with Claude"
- Source: astronomy-with-llms/chapters/24-black-holes-and-curved-spacetime.md — AI Wayback Machine
- Lane: RESEARCH (Claude assistant)
- Hook: Schwarzschild solved Einstein's field equations while dying on the Russian front in 1916 — and the solution implied black holes, which physicists agreed to ignore for decades. What did he actually find, and what was resisted?
- The artifact: A sourced 3-event brief: (1) the battlefield context (1916, Eastern Front, Schwarzschild's illness, the manuscript mailed to Einstein), (2) the mathematical result — what the Schwarzschild metric actually says and why physicists resisted the "singularity," (3) how the result was eventually accepted (Penrose-Hawking theorems, Wheeler's coinage of "black hole"). Includes 3+ verifiable citations.
- Prompt seed: `claude "Research Karl Schwarzschild's 1916 solution to Einstein's field equations. Include: (1) the biographical context — where he was, his illness, how the paper reached Einstein; (2) what the Schwarzschild metric actually predicts (the singularity and what physicists of the time called it); (3) how the result went from 'mathematical curiosity' to accepted physical reality — include Penrose's 1965 singularity theorem and Wheeler's 1967 coinage of 'black hole'. Include at least 3 verifiable citations."`
- Read / check: Verify Schwarzschild died of pemphigus (an autoimmune disease, not combat wounds). Verify the paper was sent from the Eastern Front and received/presented by Einstein in early 1916. Verify Wheeler's "black hole" coinage year (1967, at a conference in New York). Check Penrose theorem year (1965).
- Human supplies: Nothing — fully researchable.
- Output medium: slate (3-event timeline brief, human fills with archival portrait images — public domain)
- The change: Add the modern connection: the Schwarzschild metric's prediction of the photon sphere (r = 1.5 R_s) explains the bright ring in the EHT images. The 1916 solution directly predicts what the 2019 image shows.
- Teardown angle: The mathematics was correct in 1916. The physics was resisted for 50 years for sociological and philosophical reasons. The universe didn't care. The solutions were there.
- Exclusions: Cut full GR tensor derivation; cut Kerr metric for rotating black holes; cut Hawking radiation details.
- Score: 7/10
