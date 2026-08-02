# Physics + Astronomy — CLI Video Ideas ("X with Claude")

---

## Candidate 01 — Build the Solar Lifetime Calculator: Four Numbers, One Answer
- Source: physics-astronomy/chapters/05-the-sun.md
- Lane: BUILD (Claude Code)
- Hook: How long does the Sun have left? You need four numbers — luminosity, energy per fusion, proton mass, and hydrogen fraction — and you can derive it at the terminal. The answer is 5 billion years, and this script shows every step.
- The artifact: a Python script (~35 lines) using scipy.constants that: (1) computes the proton-proton chain energy release per fusion: 4p → He-4 + 2e⁺ + 2ν_e + 26.7 MeV, (2) computes the Sun's luminosity-implied fuel burn rate: dN/dt = L_sun/E_per_fusion = 3.83e26 / (4.28e-12) ≈ 8.95e37 protons/s, (3) estimates the fusible hydrogen mass (10% of M_sun, from the core), (4) computes remaining lifetime t = M_H/(m_p × dN/dt). Manim animates a four-step cascade: luminosity → fuel rate → hydrogen mass → lifetime.
- Prompt seed: `claude "Write a Python script using scipy.constants that computes the Sun's remaining hydrogen-burning lifetime. Steps: (1) energy per pp-chain reaction: E = 0.7% of 4*m_p*c^2 = 0.007*4*1.673e-27*(3e8)^2 = 4.28e-12 J per fusion of 4 protons; (2) fusion rate: dN/dt = L_sun/(E/4) where L_sun=3.828e26 W (protons consumed per second); (3) fusible hydrogen mass: M_H = 0.10 * M_sun * 0.74 (10% of mass in core, 74% hydrogen fraction); (4) remaining lifetime: t = M_H/(m_p * dN/dt). Print each step with units. Convert t to years and Gyr."`
- Read / check: Verify E per fusion ≈ 4.28×10⁻¹² J (0.7% of 4 proton masses × c²). Confirm fusion rate ≈ 8.95×10³⁷ protons/s. Verify remaining lifetime ≈ 5 Gyr. Check the scipy.constants values used: m_p = 1.6726e-27 kg, c = 2.9979e8 m/s.
- Human supplies: Nothing — fully synthetic. Python with scipy.constants.
- Output medium: Manim (four-step waterfall diagram: L_sun → dN/dt → M_H → t; each step animates with the numerical value appearing, final answer "5 billion years" appearing large)
- The change: Repeat for a 10 M_sun star (L ∝ M^4, lifetime ∝ M/L ∝ M^-3) and show it burns 1000× faster — lasting only 30 million years.
- Teardown angle: Four numbers is all you need. The Sun's luminosity, measured by satellites; the energy per fusion, from E=mc²; the proton mass; the hydrogen fraction from spectroscopy. The rest is arithmetic. Astrophysics is not mysticism — it's dimensional analysis applied at solar scale.
- Exclusions: Stellar evolution beyond the main sequence, red giant phase details, nuclear physics of the pp chain.
- Score: 10/10

---

## Candidate 02 — Build the Chandrasekhar Limit: Why White Dwarfs Can't Grow Past 1.4 Solar Masses
- Source: physics-astronomy/chapters/10-death-of-stars.md
- Lane: BUILD (Claude Code)
- Hook: A star's dead core collapses until electron degeneracy pressure stops it — unless the mass exceeds 1.4 solar masses, at which point the electrons go relativistic and the pressure can't hold. This script derives the limit numerically.
- The artifact: a Python script (~55 lines) using numpy and scipy.constants that: (1) computes non-relativistic electron degeneracy pressure P_nr = K_nr × ρ^(5/3) where K_nr depends on fundamental constants, (2) computes relativistic electron degeneracy pressure P_r = K_r × ρ^(4/3), (3) sweeps over white dwarf mass M from 0.1 to 1.5 M_sun and computes whether the central density requires relativistic or non-relativistic treatment, (4) plots the "radius vs mass" curve showing the radius going to zero at M = 1.4 M_sun (Chandrasekhar limit). Manim animates the radius-mass curve collapsing to zero.
- Prompt seed: `claude "Write a Python script using scipy.constants and numpy that estimates the Chandrasekhar limit. Use: electron degeneracy pressure P = K*(rho/mu_e)^(gamma) where gamma=5/3 (NR) or 4/3 (relativistic), K_NR = (hbar^2/(5*m_e)) * (3*pi^2)^(2/3) / m_H^(5/3), mu_e=2 (for C/O WD). For each mass M from 0.1 to 1.4 M_sun (in steps), estimate the mean density rho=M/V assuming hydrostatic balance (use Lane-Emden polytrope result R ~ M^(1/3-1) for gamma=5/3), and plot R vs M. Show that R->0 near 1.4 M_sun."`
- Read / check: Verify the Chandrasekhar mass M_Ch ≈ 1.4 M_sun emerges naturally from the transition from γ=5/3 to γ=4/3. Confirm the radius-mass relation is an inverse: more massive white dwarfs are smaller. Check the units: K_nr has units of Pa/(kg/m³)^(5/3).
- Human supplies: Nothing — fully synthetic. Python with scipy.constants, numpy.
- Output medium: Manim (radius-mass curve animating from left (large R, small M) to right (R→0, M→1.4 M_sun); a vertical red line at 1.4 M_sun labeled "Chandrasekhar limit"; annotation "above this: core collapse → neutron star or black hole")
- The change: Extend the plot to show neutron star radii for M > 1.4 M_sun using the analogous neutron degeneracy pressure argument — showing the next stable regime before the TOV limit.
- Teardown angle: The Chandrasekhar limit is not an empirical observation — it is a theorem. It follows from the relativistic energy-momentum relation for electrons and the requirement of hydrostatic equilibrium. Chandrasekhar derived it at age 19 on a ship from India to England in 1930.
- Exclusions: TOV equation for neutron stars, pair instability supernovae, quark stars.
- Score: 9/10

---

## Candidate 03 — Build the Hubble Constant Calculator: Two Methods, One Tension
- Source: physics-astronomy/chapters/13-the-big-bang.md
- Lane: BUILD (Claude Code)
- Hook: Measure H₀ from the early universe (CMB): 67.4 km/s/Mpc. Measure it from nearby supernovae: 73.0 km/s/Mpc. The 5-sigma tension has not been resolved in 15 years. This script plots both measurements and shows what the universe's age looks like under each.
- The artifact: a Python script (~40 lines) using scipy.constants that: (1) defines H₀ in two versions: CMB (Planck 2018: 67.4 ± 0.5 km/s/Mpc) and SNe (Riess et al. 2022: 73.0 ± 1.0 km/s/Mpc), (2) converts both to SI (s⁻¹), (3) computes the naive age estimate T = 1/H₀ for each in Gyr, (4) computes the percent tension in σ, (5) plots both measurements with error bars on a number line. Manim animates both measurements appearing with error bars that do not overlap.
- Prompt seed: `claude "Write a Python script using numpy and matplotlib that: (1) defines H0_CMB=67.4, err_CMB=0.5, H0_SNe=73.0, err_SNe=1.0 (in km/s/Mpc); (2) converts to SI: H0_SI = H0 * 1000 / (3.0857e22) (1 Mpc = 3.0857e22 m); (3) computes age estimate T_Hubble = 1/H0_SI in Gyr for each; (4) computes tension sigma = (H0_SNe - H0_CMB)/sqrt(err_CMB^2 + err_SNe^2); (5) plots both measurements on a horizontal axis with error bars, shading the overlap region; (6) prints tension in sigma and both age estimates in Gyr."`
- Read / check: Verify tension = (73.0-67.4)/√(0.5²+1.0²) ≈ 5.0 σ. Confirm T = 1/H₀ in Gyr: for H₀=67.4: T ≈ 14.5 Gyr; for H₀=73.0: T ≈ 13.4 Gyr. Verify 1 Mpc = 3.0857×10²² m. Check error bars do not overlap at 2σ.
- Human supplies: Nothing — fully synthetic. Python with numpy, matplotlib.
- Output medium: Manim (horizontal measurement axis; two measurement markers appearing with error bars — CMB (blue) and SNe (red) — gap between them labeled "5.0σ tension"; age estimates for each appearing below)
- The change: Add a third measurement (BAO, H₀ ≈ 68 km/s/Mpc) and show it agrees with CMB — suggesting the tension may be on the SNe side.
- Teardown angle: The Hubble tension is the most important unresolved problem in cosmology. Both measurements are careful, both teams have checked their work, and the results disagree. Either there is an unknown systematic error in one measurement, or the standard cosmological model is missing physics.
- Exclusions: Dark energy models, modified gravity, inflation.
- Score: 9/10

---

## Candidate 04 — Research the Corona Heating Problem: Why the Sun's Atmosphere is Hotter Than its Surface
- Source: physics-astronomy/chapters/05-the-sun.md
- Lane: RESEARCH (Claude assistant)
- Hook: The Sun's surface is 5,800 K. Its outer atmosphere — which is farther from the heat source — is 1–3 million K. That violates every intuition about how heat flows. After 80 years, the mechanism is still not settled.
- The artifact: a sourced 4-section brief: (1) the temperature inversion observed and measured (instruments, approximate dates); (2) the two leading mechanisms (Alfvén wave dissipation and nanoflare heating — Parker 1988); (3) the current observational evidence for and against each; (4) what Solar Orbiter (ESA, launched 2020) has found as of 2025. Manim animates a temperature profile T(r) from core to corona with the paradoxical upturn highlighted.
- Prompt seed: `claude "Research the solar corona heating problem. Cover: (1) the observed temperature inversion — surface 5800 K, corona 1-3 million K — with instruments that measure the corona temperature and approximate years of measurement; (2) Eugene Parker's nanoflare mechanism (1988 paper in Astrophysical Journal) and the Alfvén wave dissipation mechanism — state each as a one-paragraph physical mechanism; (3) current observational evidence for and against each, citing specific missions or papers; (4) what Solar Orbiter has found relevant to corona heating as of 2024-2025. Flag any claim you cannot verify."`
- Read / check: Verify Parker's 1988 nanoflare paper is in the Astrophysical Journal. Confirm Solar Orbiter launched February 2020. Verify the chromosphere temperature minimum (~4400 K just above the photosphere) before the rise. Check that any Solar Orbiter findings cited have actual publication references.
- Human supplies: Nothing — fully synthetic from astrophysics literature.
- Output medium: Manim (temperature profile curve: x = radius in solar radii from 0 to 3, y = log temperature; curve drops from 1.5×10⁷ K at core to 5800 K at photosphere, then rises to 10⁶ K in corona; the paradoxical upturn region highlighted with "UNSOLVED" annotation)
- The change: Ask Claude to estimate the energy flux needed to heat the corona and compare it to the Sun's total luminosity — showing the corona heating is energetically minor but mechanistically mysterious.
- Teardown angle: The corona heating problem is 80 years old and survives every proposed solution. It is not important because the energy is large (it isn't — it's a thousandth of the Sun's total output). It is important because it reveals that our understanding of plasma physics and magnetic reconnection is incomplete.
- Exclusions: Solar wind, space weather forecasting, Earth's magnetosphere effects.
- Score: 8/10

---

## Candidate 05 — Build the Blackbody Spectrum: Planck vs. Rayleigh-Jeans and the UV Catastrophe
- Source: physics-astronomy/chapters/03-radiation-and-spectra.md (anticipated scope)
- Lane: BUILD (Claude Code)
- Hook: Classical physics predicted that hot objects should emit infinite energy at short wavelengths. Planck fixed it in 1900 by quantizing energy — and accidentally invented quantum mechanics. This script plots both predictions and shows where classical physics breaks down.
- The artifact: a Python script (~40 lines) using numpy and scipy.constants that: (1) computes the Planck spectral radiance B(λ,T) = (2hc²/λ⁵) × 1/(exp(hc/λkT)-1) for T = 3000 K, 5800 K (Sun), 8000 K, (2) computes the Rayleigh-Jeans classical prediction B_RJ(λ,T) = 2ckT/λ⁴, (3) plots both on the same axes for T=5800 K, showing the divergence at short λ, (4) marks the visible light range. Manim animates the three Planck curves building simultaneously, then the RJ curve sweeping up and diverging in the UV.
- Prompt seed: `claude "Write a Python script using numpy, matplotlib, and scipy.constants that: (1) for T in [3000, 5800, 8000] K, plots Planck spectral radiance B(lambda,T) = 2*h*c^2/lambda^5 / (exp(h*c/(lambda*k*T))-1) for lambda from 100e-9 to 3000e-9 m; (2) for T=5800K, also plots the Rayleigh-Jeans approximation B_RJ = 2*c*k*T/lambda^4; (3) marks the visible range 380-700 nm shaded; (4) labels the UV divergence of B_RJ as 'UV Catastrophe'. Use log scale for y-axis."`
- Read / check: Verify Wien's peak for T=5800 K: λ_peak = b/T = 2.898e-3/5800 ≈ 500 nm (visible green — why the Sun peaks in green). Confirm RJ agrees with Planck at long wavelengths (λ >> hc/kT) and diverges at short λ. Check scipy.constants: h = 6.626e-34, k = 1.381e-23, c = 2.998e8.
- Human supplies: Nothing — fully synthetic. Python with scipy.constants, numpy, matplotlib.
- Output medium: Manim (three Planck curves animating simultaneously for 3000/5800/8000 K; then RJ curve for 5800 K sweeping in from long wavelengths, diverging upward in UV; "UV Catastrophe" label animating in at the divergence)
- The change: Add Wien's approximation B_W = (2hc²/λ⁵) exp(-hc/λkT) and show it fails at long wavelengths — demonstrating that Planck's formula is the correct interpolation between two regimes.
- Teardown angle: The UV catastrophe was not a small discrepancy. Classical theory predicted infinite power output at short wavelengths — a physically absurd result. Planck's quantization was not meant as physics; he called it "an act of desperation." It worked because the universe is actually quantized.
- Exclusions: CMB spectrum (a perfect Planck curve at 2.725 K), synchrotron radiation, non-thermal spectra.
- Score: 9/10

---

## Candidate 06 — Build the Stellar Death Router: Mass In, Endpoint Out
- Source: physics-astronomy/chapters/10-death-of-stars.md
- Lane: BUILD (Claude Code)
- Hook: Whether a star ends as a white dwarf, neutron star, or black hole depends almost entirely on its initial mass. This script implements the routing logic and animates it as an interactive decision tree.
- The artifact: a Python script (~35 lines) using matplotlib that: (1) defines the routing function endpoint(M_initial) → "white dwarf" (M<8 M_sun), "neutron star" (8<M<20), "black hole" (M>20), (2) plots a horizontal mass axis with color-coded regions, (3) for a user-input mass, traces the routing: main sequence → (red giant / red supergiant) → (planetary nebula + WD) / (supernova + NS or BH), (4) annotates with known examples (Sirius B = 2.1 M_sun → 0.6 M_sun WD; SN 1987A progenitor 18 M_sun → NS). Manim animates the decision tree with a pointer sweeping along the mass axis.
- Prompt seed: `claude "Write a Python script using matplotlib that visualizes stellar endpoint routing. (1) Plot a horizontal bar from M=0.1 to M=100 M_sun with three color regions: green (0.1-8: white dwarf endpoint), yellow (8-20: neutron star), red (20-100: black hole); (2) Label each region with the endpoint type and approximate remnant mass; (3) Mark known examples: Sun (1 M_sun -> WD), Sirius B progenitor (5 M_sun -> 1.0 M_sun WD), SN 1987A progenitor (18-20 M_sun -> NS), stellar black hole (30+ M_sun -> BH); (4) Draw flowchart arrows below the bar: each region -> labeled endpoint box. Use matplotlib.patches.FancyArrowPatch."`
- Read / check: Verify boundary at ~8 M_sun is correct (commonly accepted core-collapse threshold). Confirm SN 1987A progenitor mass was approximately 18-20 M_sun (Sanduleak -69 202). Verify Sirius B is a 1.02 M_sun white dwarf (not 0.6) — use the correct value. Check remnant mass estimates are labeled as approximate.
- Human supplies: Nothing — fully synthetic. Python with matplotlib.
- Output medium: Manim (mass axis animating in; color regions filling left to right; example markers appearing with labels; then flowchart arrows dropping below the axis connecting each region to its endpoint box)
- The change: Add the pair-instability supernova regime (M = 140–260 M_sun) where stars explode completely leaving no remnant — and the ultra-massive regime (M > 260 M_sun) where direct collapse to black hole is expected.
- Teardown angle: The routing is ruthlessly simple: one number, three outcomes. The Chandrasekhar limit and the Tolman-Oppenheimer-Volkoff limit set the boundaries. Everything else — the nebula, the supernova, the elements forged in the collapse — is the implementation detail.
- Exclusions: Population III stars, pair instability, chemical yields per stellar type.
- Score: 8/10

---

## Candidate 07 — Research the Big Bang Nucleosynthesis: Why There's So Much Helium
- Source: physics-astronomy/chapters/13-the-big-bang.md
- Lane: RESEARCH (Claude assistant)
- Hook: The universe is 74% hydrogen, 25% helium, and almost nothing else by mass. The helium was made in the first 3 minutes after the Big Bang — not in stars. Claude traces the nuclear physics of those 3 minutes.
- The artifact: a sourced 4-section brief: (1) the timeline: T=0 to T=3 minutes — key events and temperatures (quark-hadron at 10 μs, neutrino decoupling at 1 s, nucleosynthesis at 100 s), (2) the n/p ratio and why it freezes at 1/7, (3) why the helium mass fraction is ~25% given the n/p ratio, (4) the prediction vs. observation for He, D, Li abundances (cite Schramm & Turner 1998 or Cyburt et al. 2016). Manim animates a 3-minute timeline with temperature and n/p ratio evolving.
- Prompt seed: `claude "Research Big Bang Nucleosynthesis (BBN). Cover: (1) the timeline from T=0 to T=3 minutes — key epochs (quark-hadron transition, neutrino decoupling, proton-neutron freezeout, deuterium bottleneck, helium synthesis) with temperatures in MeV/keV; (2) why the n/p ratio freezes at approximately 1/7 at T~1 MeV; (3) how the 1/7 n/p ratio leads to ~25% He-4 mass fraction (arithmetic: 2n per He-4 nucleus from n/p=1/7); (4) predicted vs. observed abundances for He-4, D, He-3, Li-7. Cite Schramm & Turner 1998 (Physics Reports) or Cyburt et al. 2016. Flag unverified claims."`
- Read / check: Verify n/p ratio at freeze-out ≈ 1/7. Confirm He-4 mass fraction calculation: if n/p = 1/7, then for every 7 protons there is 1 neutron → 1 He-4 (using 2n + 2p) + 6p → mass fraction = 4/(4+6) = 0.40 is WRONG → recalculate: 1n + 7p → He-4 needs 2n, so start with 2n + 14p → 1 He-4 + 12p → Y_p = 4/16 = 0.25. Confirm this arithmetic matches the cited paper.
- Human supplies: Nothing — fully synthetic from astrophysics literature.
- Output medium: Manim (horizontal timeline from 10⁻⁶ s to 10³ s; temperature curve dropping from 10 MeV to 0.01 MeV above; n/p ratio decaying from 1 to 1/7 and then slowly decreasing due to neutron decay; epoch labels appearing at each key moment)
- The change: Ask Claude to explain what the observed Li-7 abundance discrepancy (the "lithium problem") tells us — why BBN predicts 3-4× more Li-7 than observed.
- Teardown angle: The first 3 minutes determined 25% of the mass of everything. The arithmetic is elementary school: if n/p = 1/7, pair up all the neutrons with protons and you get exactly 25% helium by mass. The Big Bang is not speculation — it is a calculation confirmed by spectroscopy.
- Exclusions: Stellar nucleosynthesis (beyond helium), r-process and s-process.
- Score: 8/10

---

## Candidate 08 — Build the Spectral Classification Tool: OBAFGKM from Stellar Colors
- Source: physics-astronomy/chapters/06-analyzing-starlight.md
- Lane: BUILD (Claude Code)
- Hook: "Oh Be A Fine Girl/Guy Kiss Me" — the spectral sequence OBAFGKM maps stellar temperature to color to spectral lines. This script classifies any star's color index B-V into its spectral type and plots the HR diagram population.
- The artifact: a Python script (~45 lines) using numpy and matplotlib that: (1) defines the B-V color index ranges for each spectral class O (-0.4 to -0.3), B (-0.3 to 0), A (0 to 0.3), F (0.3 to 0.6), G (0.6 to 0.8), K (0.8 to 1.4), M (>1.4), (2) given a list of 50 synthetic stars with random B-V values, classifies each and plots them on a color-magnitude HR diagram (x = B-V, y = absolute magnitude M_V), (3) draws the main sequence curve. Manim animates the stars populating the HR diagram color-coded by class.
- Prompt seed: `claude "Write a Python script using numpy and matplotlib that: (1) defines spectral class boundaries by B-V color index: O<-0.3, B:-0.3 to 0, A:0 to 0.3, F:0.3 to 0.6, G:0.6 to 0.8, K:0.8 to 1.4, M>1.4; (2) generates 100 synthetic stars with B-V from np.random.uniform(-0.4, 2.0) and M_V from a main-sequence polynomial M_V = 10*(B-V) - 2 (approximate); (3) classifies each star and colors the scatter plot by class (O=violet, B=blue, A=white, F=yellow-white, G=yellow, K=orange, M=red); (4) labels class boundaries as vertical dashed lines; (5) inverts the y-axis (brighter = lower M_V = top of plot)."`
- Read / check: Verify the Sun is classified as G (B-V ≈ 0.65). Confirm Sirius is A (B-V ≈ 0.0). Check that y-axis inversion is correct (brighter at top). Verify class boundary B-V values match standard references (Allen's Astrophysical Quantities).
- Human supplies: Nothing — fully synthetic. Python with numpy, matplotlib.
- Output medium: Manim (HR diagram axes animate in; 100 star dots appear one by one color-coded by spectral class; then class boundary lines appear; Sun location highlighted with a label)
- The change: Add giant and supergiant sequences by giving some stars anomalously high luminosity for their B-V — showing that B-V alone doesn't determine luminosity class.
- Teardown angle: The HR diagram is not a plot of measurements. It is the revelation that stars are not random — they cluster in patterns that trace out their physics. The main sequence is stars burning hydrogen; the giant branch is what happens next. The classification system is 130 years old and still the primary way astronomers catalog stellar populations.
- Exclusions: White dwarfs on the HR diagram, evolved stellar populations, Hertzsprung gap.
- Score: 8/10
