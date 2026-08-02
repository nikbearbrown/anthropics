# Physics +1 (Modern Physics) — CLI Video Ideas ("X with Claude")

## Candidate 01 — Build a Relativistic Time Dilation Simulator with Claude

- Source: physics-modern-physics/chapters/01-special-relativity.md
- Lane: BUILD (Claude Code)
- Hook: You can accelerate to 90 % of the speed of light and still never gain on a photon — so what actually changes? Time dilation is the answer, and the numbers are wilder than your intuition says.
- The artifact: An animated D3 or Manim scene showing γ(v) sweeping from v = 0 to v → c: the Lorentz factor curve drawing itself, a twin-clock animation where the moving clock visibly slows, and a readout of elapsed proper time vs. coordinate time for a given trip velocity — all computed in real time from the two-postulate derivation.
- Prompt seed: `claude "Write a single-file D3 v7 HTML simulation of relativistic time dilation. Show (1) a live γ(v) curve drawing as a slider moves v from 0 to 0.999c, (2) two animated clocks — one stationary, one moving at v — where tick rate scales as 1/γ, (3) a readout of Δt and Δt₀ for a 10-light-year trip. Use vox-palette colors. Verify: at v=0, γ=1 and clocks match; at v=0.866c, γ=2 exactly."`
- Read / check: Verify γ formula is correct (1/√(1-v²/c²)), check that stationary clock runs exactly γ× faster than moving clock, confirm at v=0.866c the moving clock reads exactly half. Output: does the γ curve asymptote correctly near v=c?
- Human supplies: Nothing — fully synthetic. The light-clock geometry is analytic and the D3 animation is self-contained.
- Output medium: Manim (animated γ curve + dual clock scene) or d3 (animated, single HTML file)
- The change: Add a second iteration — extend the simulation to show the muon decay length experiment: at rest muon survives ~660 m, at 0.9994c it survives ~42 km. The viewer changes the muon speed slider and watches the survival distance animate in real time.
- Teardown angle: The asymmetry of the twin paradox is not a paradox at all — acceleration breaks the symmetry, and the equations were telling us this the whole time. The surprise is not that clocks slow, but that "simultaneous" loses meaning first.
- Exclusions: General relativity, gravitational time dilation, four-vectors — keep to the two-postulate SR derivation.
- Score: 9/10

---

## Candidate 02 — Simulate Quantum Tunneling Through the Coulomb Barrier with Claude

- Source: physics-modern-physics/chapters/03-the-sun-a-nuclear-powerhouse.md
- Lane: BUILD (Claude Code)
- Hook: The Sun should be cold and dark — the average proton at 15 million Kelvin doesn't have nearly enough energy to overcome the Coulomb barrier. Quantum tunneling is the only reason stars shine, and you can watch the probability leak through.
- The artifact: A Manim animation of a Gaussian wave packet incident on a finite Coulomb barrier: the packet splits at the barrier wall, a transmitted component leaks through and propagates to the right, and a reflected component bounces back. A real-time readout shows transmission probability T(E) as a function of barrier height and packet energy — the WKB tunneling exponent plotted as a curve on a second panel.
- Prompt seed: `claude "Using Python + Manim, animate a 1D quantum tunneling simulation. Show a Gaussian wave packet (width σ=1 nm, central energy E₀) incident on a finite square barrier of height V₀=10 eV and width d=0.1 nm. Display: (1) the animated |ψ(x,t)|² evolving in time, (2) reflected and transmitted components coloured separately, (3) a live readout of transmission probability T using the WKB approximation exp(-2∫√(2m(V-E)/ℏ²)dx). Sliders for E₀ and V₀."`
- Read / check: At E₀ > V₀, transmission should approach 1 (above-barrier transmission with Ramsauer-Townsend resonances). At E₀ << V₀, T should be exponentially suppressed. Check normalization of |ψ|² at each frame.
- Human supplies: Nothing — fully synthetic. The wave packet evolution uses the TDSE split-operator method, which Claude can implement analytically for a square barrier.
- Output medium: Manim (animated |ψ|² scene with dual panels)
- The change: Swap the square barrier for a Coulomb barrier profile V(r) = ke²/r and add the Gamow factor — show how the tunneling probability depends on temperature via the Maxwell-Boltzmann tail, with the Gamow peak animating as temperature increases.
- Teardown angle: The Sun shines not because tunneling is likely, but because 10⁵⁷ protons run the lottery every second. The lesson: improbable events become certain at cosmic scale.
- Exclusions: Full proton-proton chain kinematics, neutrino oscillations, solar neutrino problem.
- Score: 9/10

---

## Candidate 03 — Plot the Hydrogen Spectrum from Bohr's Formula with Claude

- Source: physics-modern-physics/chapters/05-the-atom.md
- Lane: BUILD (Claude Code)
- Hook: Balmer found the pattern in 1885 with no theory. Bohr derived it from a single quantization rule in 1913. Every spectral line you see in a discharge tube is a photon carrying the exact energy difference between two integer-labeled rungs — compute it yourself in 30 lines.
- The artifact: A D3 animation that starts with the Bohr energy-level ladder (n=1 through n=6), then sweeps through all transitions: each arrow animates from the upper level to the lower level, the corresponding spectral line lights up in its true visible color (or UV/IR label), and the wavelength/frequency readout updates. A slider lets the viewer pick the upper level n_i and watch all downward transitions populate the spectrum below.
- Prompt seed: `claude "Build a single-file D3 v7 HTML animation of the hydrogen emission spectrum using the Bohr model. Show: (1) an energy-level diagram with n=1..6 rungs to scale, (2) an animated arrow dropping from n_i (slider) to all n_f < n_i simultaneously, each arrow colored by photon wavelength using the visible-light color map, (3) the spectral line bar chart below updating in real time. Label the Lyman, Balmer, and Paschen series. Verify: n=3→2 gives 656 nm (red)."`
- Read / check: The Rydberg formula λ = R_H(1/n_f² - 1/n_i²)⁻¹ with R_H=1.097×10⁷ m⁻¹. Confirm n=3→2 at 656 nm, n=4→2 at 486 nm, n=2→1 at 122 nm (UV). Check that Lyman series is UV, Balmer partially visible.
- Human supplies: Nothing — fully synthetic. All wavelengths computed analytically.
- Output medium: d3 (animated, single HTML file)
- The change: Add the reduced-mass correction (deuterium vs hydrogen): the viewer toggles between H and D and watches every line shift by ~1.79 Å — exactly how Urey discovered deuterium in 1932.
- Teardown angle: The discreteness of the spectrum is not a property of light — it is a property of the boundary conditions on a confined wave. Bohr's rule is a half-wavelength condition in disguise.
- Exclusions: Fine structure, Zeeman effect, derivation of Schrödinger equation.
- Score: 8/10

---

## Candidate 04 — Animate the Blackbody Radiation Curve and the Ultraviolet Catastrophe with Claude

- Source: physics-modern-physics/chapters/04-the-quantum-nature-of-light.md, chapters/10-quantum-physics.md
- Lane: BUILD (Claude Code)
- Hook: Classical physics predicted that every hot object should instantly blind you with X-rays. The curve that didn't diverge is the one that started a revolution. Watch both curves on the same axes as you drag temperature from 1000 K to 10000 K.
- The artifact: A D3 animation showing the Planck blackbody spectrum B(λ,T) alongside the classical Rayleigh-Jeans prediction B_RJ(λ,T). The Planck curve sweeps and re-draws as a temperature slider moves; the peak wavelength tracks Wien's law (λ_max marked with a vertical dashed line); the Rayleigh-Jeans curve diverges to the upper-right. A color band shading the visible range (380–700 nm) shows the color shift from red to yellow-white.
- Prompt seed: `claude "Build a single D3 v7 HTML simulation of blackbody radiation. X-axis: wavelength 100–3000 nm. Y-axis: spectral radiance. Draw two curves: (1) Planck's formula B(λ,T) = (2hc²/λ⁵)/(exp(hc/λkT)-1), (2) Rayleigh-Jeans B_RJ = 2ckT/λ⁴. Temperature slider 1000–10000 K. Animate: peak wavelength marker moving with Wien's law. Shade the visible band 380–700 nm. Verify: at T=5778K, peak ≈ 502 nm."`
- Read / check: Wien's law λ_max = 2.898×10⁻³/T K·m. At 5778 K: ~502 nm (Sun, green-yellow). At 3000 K: ~966 nm (IR). The Rayleigh-Jeans curve should stay below Planck at long λ but rocket off to infinity at short λ.
- Human supplies: Nothing — fully synthetic. All formulas analytic.
- Output medium: d3 (animated, single HTML file)
- The change: Add a second iteration showing how a Planck curve shifts to model the Wien displacement law applied to real astronomical objects — display which color star matches which temperature by overlaying a stellar classification color gradient.
- Teardown angle: The catastrophe is not a calculation error; it is the correct answer from a wrong assumption. Every high-frequency mode being equally excitable is the assumption that breaks. Quantization is the only fix.
- Exclusions: Derivation of the Planck distribution from partition functions, photon statistics.
- Score: 8/10

---

## Candidate 05 — Compute the Chandrasekhar Limit and White Dwarf Mass-Radius Curve with Claude

- Source: physics-modern-physics/chapters/07-the-death-of-stars.md
- Lane: BUILD (Claude Code)
- Hook: A 20-year-old on a ship to England worked out that stars above 1.4 solar masses cannot hold themselves up against gravity — not with heat, not with fusion, but with quantum mechanics alone. The mass-radius curve has a cliff, and below it is the entire fate of the Sun.
- The artifact: A Manim scene that plots the white dwarf mass-radius relationship: the polytropic curve R(M) derived from the Chandrasekhar equation of state, starting at low mass (large radius) and sweeping toward M_Ch = 1.4 M☉ where the radius → 0. A horizontal dashed line marks M_Ch; the curve asymptotes to it. A second panel shows electron degeneracy pressure vs. density, with the non-relativistic and relativistic regimes labeled.
- Prompt seed: `claude "Using Python + Manim, plot the Chandrasekhar white dwarf mass-radius curve. Numerically integrate the Lane-Emden equation for a n=3/2 polytrope (non-relativistic electrons) and n=3 polytrope (relativistic electrons). Plot R (in Earth radii) vs M (in solar masses) for 0.1 to 1.4 M_sun. Mark the Chandrasekhar mass M_Ch = 1.44 M_sun with a vertical dashed line. Animate the curve drawing from low mass to high mass. Verify: at M = 0.6 M_sun, R ≈ 1.5 R_Earth."`
- Read / check: The n=3 polytrope gives M_Ch = 5.87(ℏc/G)^(3/2) / (μ_e m_H)² × 1/m_H. Numerically ≈ 1.44 M☉. Check that the curve is monotonically decreasing (heavier → smaller). At M → M_Ch, R → 0 correctly.
- Human supplies: Nothing — fully synthetic. Lane-Emden numerical integration is straightforward in NumPy.
- Output medium: Manim (animated curve-drawing scene)
- The change: Add a third panel showing where known white dwarfs from the Gaia catalog lie on the same plot — the viewer compares theory vs. observation.
- Teardown angle: Chandrasekhar's result was rejected by Eddington as an inelegant conclusion. The Nobel came 50 years later. The math was right from day one, and the universe was already doing it.
- Exclusions: Neutron star equation of state, rotating white dwarfs, mass transfer in binaries.
- Score: 8/10

---

## Candidate 06 — Simulate Radioactive Decay Chains with Claude

- Source: physics-modern-physics/chapters/13-radioactivity-and-nuclear-physics.md
- Lane: BUILD (Claude Code)
- Hook: Uranium-238 takes 4.5 billion years to decay into lead through 14 intermediate steps — some of which last microseconds. The bathtub equation that governs the whole chain is the same equation everywhere; what changes is the rate constant.
- The artifact: A D3 animation of the U-238 decay chain: 14 nuclides arrayed as nodes on a decay graph, colored by activity (red = high activity, blue = low). A time slider spans 0 to 4.5 Ga; the animation shows each intermediate's population evolving via the Bateman equations. Vertical bars give relative activity at each node; the viewer can see secular equilibrium being established and disturbed.
- Prompt seed: `claude "Build a D3 v7 HTML simulation of the uranium-238 decay chain (14 steps from U-238 to Pb-206). Compute population of each nuclide using the Bateman equations numerically (scipy.integrate or analytical). Time slider 0 to 4.5 Gyr. Display: (1) bar chart of relative activity per nuclide, colored cool-to-warm by half-life, (2) time series of each nuclide's count. Verify: after 4.5 Gyr, ~50% of U-238 has decayed (half-life = 4.47 Gyr). Label each nuclide."`
- Read / check: U-238 half-life 4.468 Gyr → after 4.5 Gyr, N/N₀ = 2^(−4.5/4.468) ≈ 0.489. Check that short-lived daughters (Th-234, t½=24.1d; Pa-234, t½=1.17 min) reach secular equilibrium with U-238 parent within the first few years. Verify Bateman equations sum to conservation of total nucleon number.
- Human supplies: Nothing — fully synthetic. Bateman equations solved numerically with known half-lives.
- Output medium: d3 (animated, single HTML file)
- The change: Add a second scenario: start with a sample of pure Ra-226 (the daughter product Curie discovered) and watch the buildup of its own decay chain toward Pb-206, showing how Curie's samples glowed hotter over time.
- Teardown angle: Secular equilibrium is the chain reaching a steady state where each daughter's activity equals the parent's — a beautiful example of how very different timescales can conspire to produce a stable ratio.
- Exclusions: Branching ratios for rare decay paths, neutrino emission details, nuclear binding energy derivation.
- Score: 8/10

---

## Candidate 07 — Measure the Age of the Universe from Hubble's Law with Claude

- Source: physics-modern-physics/chapters/11-the-big-bang.md
- Lane: BUILD (Claude Code)
- Hook: Hubble published one graph in 1929 with 24 data points. Running it backward gives the age of the universe. The number you get from dividing 1 by H₀ is 14 billion years — and the real calculation gets 13.8. Show the derivation live.
- The artifact: A D3 animation showing (1) Hubble's original 1929 data points (recession velocity vs. distance), (2) a best-fit line drawing itself whose slope is H₀, (3) the inferred age T = 1/H₀ computed live as the slope slider moves, with a comparison to the modern ΛCDM value of 13.8 Gyr and a brief labeled correction for the deceleration parameter.
- Prompt seed: `claude "Build a D3 v7 single-file HTML visualization of Hubble's law. Plot Hubble's original 1929 data (velocity km/s vs. distance Mpc — use the actual published values). Draw a least-squares best-fit line animating onto the plot. Show H₀ = slope in km/s/Mpc and compute T_H = 1/H₀ in Gyr. Add a second slider for H₀ (50–100 km/s/Mpc) and animate the inferred age updating. Mark the modern value H₀ = 70 km/s/Mpc and T = 13.8 Gyr. Verify: at H₀ = 70, T_H ≈ 13.97 Gyr."`
- Read / check: 1/H₀ = 1/(70 km/s/Mpc) = 1/(70 × 3.086×10¹⁹ m/s/m) = 4.41×10¹⁷ s ≈ 13.97 Gyr. The true age is 13.8 Gyr (ΛCDM correction for matter + dark energy). Hubble's original H₀ ~ 500 km/s/Mpc gives a naive age of only ~1.9 Gyr — younger than the Earth, a historical problem worth showing.
- Human supplies: Nothing — fully synthetic. Hubble's 1929 data is published and historical; the LLM can reproduce it from the paper.
- Output medium: d3 (animated, single HTML file)
- The change: Add a third panel comparing Hubble constant tension: H₀ from the CMB (Planck: 67.4) vs. from Cepheids (SH0ES: 73.2) — plot both lines and show the 5σ discrepancy as a gap.
- Teardown angle: Hubble's original H₀ was wrong by a factor of 7 (distance ladder errors), yet his method was right. The universe being older than the Earth was hidden in a miscalibrated distance scale for 20 years.
- Exclusions: Dark energy equation of state derivation, Friedmann equations full derivation, CMB power spectrum.
- Score: 8/10

---

## Candidate 08 — Animate Big Bang Nucleosynthesis: Why 25% Helium with Claude

- Source: physics-modern-physics/chapters/11-the-big-bang.md
- Lane: BUILD (Claude Code)
- Hook: The universe had exactly three minutes to make helium. Any longer and the proton-to-neutron ratio would have shifted; any shorter and deuterium wouldn't have had time to react. The 25% helium mass fraction is a precise prediction from a 14-billion-year-old event — and you can compute it in a script.
- The artifact: A Manim scene showing the first 3 minutes of the universe: a timeline from t = 0.01 s to t = 200 s with temperature and energy labeling. Three animated streams show n/p ratio, deuterium abundance, and helium-4 fraction building up. The freeze-out at ~1 s is marked; the deuterium bottleneck at ~100 s is labeled; the final He-4 mass fraction of 25% prints as the endpoint. A second panel shows the reaction network (p+n→D, D+p→He-3, He-3+n→He-4) with arrows pulsing to indicate active reactions.
- Prompt seed: `claude "Using Python + Manim, animate Big Bang nucleosynthesis (BBN) from t=0.1s to t=300s. Numerically integrate the Boltzmann equations for the n/p ratio (freeze-out at t~1s) and the chain: D, He-3, He-4 abundances using the Kawano code approach (simplified 4-reaction network). Show: (1) animated time series of He-4 mass fraction Y_p building to 0.25, (2) the reaction network graph with active reactions pulsing, (3) temperature axis T(t) = 10^10/√t K. Verify: Y_p ≈ 0.245 at t=300s."`
- Read / check: Final Y_p = 4*(n/p)/(1 + n/p) × (fraction captured into He-4) ≈ 0.245. The n/p freeze-out at ~1/6 gives Y_p ≈ 4*(1/7)/(1 + 1/7) × correction ≈ 0.245. Neutron decay from t=1s to t=100s reduces n/p from 1/6 to ~1/7. Verify D peak at ~100 s (the "deuterium bottleneck").
- Human supplies: Nothing — fully synthetic. The Boltzmann rate equations use published nuclear reaction rates (built into the prompt).
- Output medium: Manim (animated timeline scene)
- The change: Show what happens if the neutron-to-proton ratio at freeze-out were slightly different — e.g., if the weak interaction rate were 10% faster — and how the final He fraction shifts. This makes the anthropic sensitivity visible.
- Teardown angle: The 25% helium abundance is not a coincidence — it is the only number the Standard Model allows given the neutron half-life, the number of neutrino families, and the baryon-to-photon ratio. Any different and the periodic table would be different.
- Exclusions: Lithium-7 problem, baryon asymmetry, inflation physics.
- Score: 7/10

---

## Candidate 09 — Simulate Mass-Energy Equivalence: How Much Energy in an Atom? with Claude

- Source: physics-modern-physics/chapters/09-special-relativity.md
- Lane: BUILD (Claude Code)
- Hook: E = mc² is not just a bumper sticker — it is the reason nuclear fission releases a million times more energy per kilogram than chemical burning. Build a comparison tool that makes the factor visceral: type in any mass, get back the equivalent energy in joules and in TNT-tons.
- The artifact: A D3 interactive calculator showing: (1) a mass input slider (1 gram to 1 kg), (2) E = mc² computed live in joules, in kWh, and in kilotons of TNT equivalent, (3) an animated bar chart comparing chemical energy density (gasoline: 46 MJ/kg) vs. nuclear fission (8×10¹³ J/kg, 0.1% mass conversion) vs. full E = mc² conversion (9×10¹⁶ J/kg) — bars growing to scale.
- Prompt seed: `claude "Build a D3 v7 single-file HTML E=mc² calculator and comparison tool. Input: mass slider 1mg to 1kg. Output: E=mc² in joules (c=3×10⁸ m/s), in kWh, and in kilotons TNT (1 kton = 4.184×10¹² J). Animated bar chart comparing: chemical energy (gasoline 46 MJ/kg), U-235 fission (8.2×10¹³ J/kg), full annihilation (mc²). Bars scale logarithmically. Verify: 1 gram fully annihilated = 8.99×10¹³ J = ~21.5 kilotons TNT."`
- Read / check: 1g × (3×10⁸)² = 9×10¹³ J. 9×10¹³ / 4.184×10¹² ≈ 21.5 kilotons. Check fission fraction: U-235 releases ~200 MeV per fission, mass of U-235 = 235 u = 3.9×10⁻²⁵ kg, so ~200 MeV per 3.9×10⁻²⁵ kg = 8.2×10¹³ J/kg (0.091% mass conversion). Verify logarithmic bar scale is sensible.
- Human supplies: Nothing — fully synthetic. All values are tabulated physical constants.
- Output medium: d3 (animated, single HTML file)
- The change: Add a second slider: reactor conversion efficiency (1%–100%) and show how much of mc² each reactor type captures — bringing the abstract equivalence into engineering reality.
- Teardown angle: The factor-of-a-million between chemical and nuclear energy density comes from the ratio of electromagnetic to nuclear binding energy scales — nothing mysterious, just the strong force binding at MeV vs. chemical bonding at eV.
- Exclusions: Binding energy curve derivation, liquid drop model, thorium fuel cycles.
- Score: 7/10

---

## Candidate 10 — Visualize Rutherford Scattering Cross-Sections with Claude

- Source: physics-modern-physics/chapters/05-the-atom.md, chapters/12-atomic-physics.md
- Lane: BUILD (Claude Code)
- Hook: One in eight thousand alpha particles bounced backward. That ratio — measured in a darkened room with a phosphorescent screen — told Rutherford the nucleus was 100,000 times smaller than the atom. Simulate the scattering geometry yourself and read off the same conclusion.
- The artifact: A D3 animation showing alpha particles (dots) launched from the left at a nuclear target. Each particle follows a hyperbolic Rutherford trajectory computed from the Coulomb potential. The impact parameter b determines the deflection angle θ via the Rutherford formula. A histogram builds up showing dN/dΩ vs. θ — the Rutherford differential cross-section — as particles accumulate.
- Prompt seed: `claude "Build a D3 v7 single-file HTML Rutherford scattering simulation. Animate ~200 alpha particles approaching a gold nucleus (Z=79). For each particle, sample impact parameter b from 0 to b_max=10 fm. Compute deflection angle using the Rutherford formula: cot(θ/2) = 4πε₀ E b / (Z_α Z_Au e²). Animate each trajectory as a curved path. Simultaneously build a live histogram of dN/dΩ vs. θ (log scale). Verify: the differential cross-section scales as 1/sin⁴(θ/2)."`
- Read / check: The Rutherford cross-section dσ/dΩ = (a/4)²/sin⁴(θ/2) where a = Z_α Z_Au e²/(4πε₀ E). At E = 7.7 MeV for gold (Z=79), a ≈ 14.7 fm. Confirm that the histogram rises steeply toward small angles (forward scattering) and has the characteristic 1/sin⁴(θ/2) shape. Verify that fewer than 0.01% of particles scatter at θ > 90°.
- Human supplies: Nothing — fully synthetic. The Coulomb trajectories are analytic hyperbolas.
- Output medium: d3 (animated, single HTML file)
- The change: Allow the viewer to change the nuclear model: toggle between Thomson's "pudding" model (smooth positive sphere → small deflections only) and Rutherford's point nucleus → large deflections. The contrast in scattering patterns is the discovery.
- Teardown angle: Rutherford's backward-scattered particles are not an anomaly — they are the only possible result if the charge is concentrated. The data forced the nuclear model because no other geometry fits the scattering formula.
- Exclusions: Quantum corrections to Rutherford scattering (Mott), nuclear form factors, inelastic scattering.
- Score: 7/10
