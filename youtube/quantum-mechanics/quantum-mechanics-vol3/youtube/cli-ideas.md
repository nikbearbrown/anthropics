# Quantum Mechanics Vol. 3 — CLI Video Ideas ("X with Claude")

## Candidate 01 — "Model STM Tunneling Current: WKB Applied to a Real Experiment" (Capstone System A)
- Source: quantum-mechanics-vol3/chapters/11-capstone-modeling-a-real-quantum-system.md
- Lane: BUILD (Claude Code)
- Hook: STM measures quantum tunneling — and the "rule of thumb" (current drops 7-10x per ångström gap) comes from the WKB approximation. Claude Code derives and validates it against Binnig & Rohrer's Nobel data.
- The artifact: A Manim animation of ln(I) vs. tip-sample distance d — a straight line with slope -2κ animating from left to right, with the experimental data points from the original STM paper appearing as dots, then the theoretical line threading through them.
- Prompt seed: `claude "Write a Python script that: (1) computes the WKB tunneling current I(d) = I_0 * exp(-2*kappa*d) where kappa = sqrt(2*m_e*phi)/hbar for typical metal work function phi=4 eV; (2) plots ln(I/I_0) vs d from 0 to 10 Angstroms; (3) prints the slope 2*kappa in units of inverse Angstroms; (4) compute the factor by which current decreases per Angstrom; (5) compare to Binnig & Rohrer 1982 reported slope of approximately 2 per Angstrom."`
- Read / check: κ = sqrt(2*m_e*4eV)/hbar ≈ 1.025 Å⁻¹. Slope of ln(I) vs d should be -2κ ≈ -2.05 Å⁻¹. Current per Angstrom factor: exp(2.05) ≈ 7.8 (consistent with "7-10x" rule of thumb). Verify scipy.constants for m_e, hbar. Cite Binnig & Rohrer Rev. Mod. Phys. 59, 615 (1987).
- Human supplies: Nothing — fully synthetic (comparison values from published Nobel lecture, publicly available).
- Output medium: Manim (ln(I) vs d straight line drawing from left to right, slope label appearing, "factor of 7.8 per Å" annotation, Nobel prize medallion icon in corner)
- The change: Vary the work function φ from 2 eV to 6 eV and plot the family of ln(I) curves — showing how different metals give different decay rates.
- Teardown angle: The WKB approximation assumes the potential varies slowly compared to the de Broglie wavelength. For a vacuum gap (~1 eV/Å slope), this fails at the barrier edges — but the exponential body of the tunneling probability is accurate. The 10% error from image-charge corrections is smaller than the gain from making the gap atomically sharp.
- Exclusions: Tersoff-Hamann model for lateral resolution, Fowler-Nordheim (large bias), 3D tip geometry.
- Score: 9/10

## Candidate 02 — "Build the Variational Helium Calculation: Two-Parameter Optimization" (Capstone)
- Source: quantum-mechanics-vol3/chapters/03-the-variational-principle.md
- Lane: BUILD (Claude Code)
- Hook: The variational principle gives an upper bound on the ground state energy — and a one-parameter trial function for helium gets within 2% of experiment. Claude Code finds the optimal Z_eff in 10 lines.
- The artifact: A Manim animation of E(Z_eff) — a curve drawing from left to right, with the minimum appearing at Z_eff=27/16=1.6875, the variational bound E_var=-77.5 eV labeled, and the exact value E_exact=-79.0 eV shown as a dashed reference line below.
- Prompt seed: `claude "Write a Python script performing the variational calculation for helium ground state: trial function psi = exp(-Z_eff*(r1+r2)/a0). The energy E(Z_eff) = (Z_eff^2 - 2*Z_eff*(Z - 5/16)*2) * 27.2 eV (in Hartree units: Z_eff^2 - 27*Z_eff/8 + ... use E = (Z_eff^2 - 2*Z_eff*27/16)*27.2 eV for the one-parameter family). Minimize E(Z_eff) analytically (dE/dZ_eff=0) and numerically with scipy.optimize.minimize_scalar. Compare to exact helium energy -79.005 eV."`
- Read / check: Optimal Z_eff = 27/16 = 1.6875. E_var ≈ -77.5 eV. Percent error vs exact: (79.0-77.5)/79.0 ≈ 1.9%. Verify the energy expression is correct (the key term is the electron-electron repulsion <V_ee> = 5Z_eff/8 in atomic units). Analytical and numerical minima should agree.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim (E(Z_eff) curve drawing, minimum marked with dashed lines, variational bound vs exact energy shown on a vertical axis with gap highlighted, percent error labeled)
- The change: Add a two-parameter trial function psi = exp(-Z1*r1/a0) * exp(-Z2*r2/a0) with Z1 ≠ Z2, minimize over both parameters simultaneously, and show the improved bound.
- Teardown angle: The variational bound is always an upper bound — the exact energy lies below. The 2% error from a one-parameter function is remarkable because the exact Hamiltonian has 6 spatial degrees of freedom. The principle of minimization does enormous work with almost no information about the exact wave function.
- Exclusions: Hylleraas 6-parameter calculation, density functional theory, coupled-cluster methods.
- Score: 9/10

## Candidate 03 — "Compute WKB Tunneling: α-Decay Lifetime with Claude Code"
- Source: quantum-mechanics-vol3/chapters/04-the-wkb-approximation-and-tunneling.md
- Lane: BUILD (Claude Code)
- Hook: Alpha decay lifetimes span 20 orders of magnitude — from microseconds to billions of years. The WKB approximation explains all of them with one formula. Claude Code computes it for uranium-238.
- The artifact: A Manim animation of the Gamow factor G vs nuclear charge Z — a curve showing how the log of the decay rate depends on Z and Q (decay energy), with U-238, Th-232, and Ra-226 plotted as data points with their known half-lives.
- Prompt seed: `claude "Write a Python script that computes the Gamow factor G = 2*integral(kappa(r)dr from R1 to R2) for alpha decay using WKB: kappa(r) = sqrt(2*m_alpha*(V_coulomb(r)-Q))/hbar, V_coulomb(r) = 2*(Z-2)*e^2/(4*pi*eps0*r), Q = decay energy. For U-238 (Z=92, Q=4.27 MeV, R1=7.4 fm): evaluate G numerically with scipy.integrate.quad. Compute decay probability per unit time and half-life t_{1/2}. Compare to known 4.47 Gyr."`
- Read / check: G for U-238 should be approximately 86 (Gamow factor). Computed half-life should agree with 4.47 Gyr within a factor of 2-3 (WKB is an approximation; prefactors are uncertain). Verify R2 (outer turning point where V_coulomb = Q) is correctly computed as r2 = 2*(Z-2)*e^2/(4*pi*eps0*Q). Use m_alpha = 4*u in atomic mass units.
- Human supplies: Nothing — fully synthetic (decay parameters from NNDC, publicly available).
- Output medium: Manim (Gamow factor curve vs Z drawing, U-238/Th-232/Ra-226 data points appearing with half-life labels, exponential sensitivity to G demonstrated)
- The change: Show the sensitivity: changing Q by 0.5 MeV changes the half-life by 6 orders of magnitude — making the Geiger-Nuttall law (log t vs Q^{-1/2}) visible as a straight line.
- Teardown angle: The 20 orders of magnitude variation in alpha-decay lifetimes is entirely explained by the exponential sensitivity of the Gamow factor to the decay energy Q and nuclear charge Z. The WKB approximation is not just qualitatively right — it explains the numerical range.
- Exclusions: Shell model corrections, beta decay, fission probability.
- Score: 8/10

## Candidate 04 — "Simulate Avoided Level Crossing with Degenerate Perturbation Theory"
- Source: quantum-mechanics-vol3/chapters/02-degenerate-perturbation-theory-and-fine-structure.md
- Lane: BUILD (Claude Code)
- Hook: Two levels approach each other as a parameter varies — and they repel. They never cross. This "avoided crossing" is behind every band gap in solid-state physics.
- The artifact: A Manim animation of two energy levels E± as a function of detuning δ (distance from degeneracy) — two curves approaching, then repelling. The gap at δ=0 is labeled as 2|V| (the matrix element of the perturbation).
- Prompt seed: `claude "Write a Python script that computes and plots avoided level crossing: for a 2x2 Hamiltonian H = [[E0 + delta, V], [V, E0 - delta]] where E0=1 eV, V=0.1 eV, vary delta from -0.5 to 0.5 eV. Diagonalize H at each value of delta using numpy.linalg.eigh, extract the two eigenvalues E+ and E-. Plot E+ and E- vs delta on one figure. Mark the gap 2V=0.2 eV at delta=0. Print the minimum gap."`
- Read / check: At δ=0, eigenvalues should be E0 ± |V| = 1.0 ± 0.1 eV. Minimum gap should be 2|V| = 0.2 eV. Curves should be hyperbola-shaped (not two intersecting lines). At large |δ|, eigenvalues should approach E0 ± δ (the uncoupled levels). Verify numpy.linalg.eigh returns eigenvalues in ascending order.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim (two energy curves drawing simultaneously as δ varies, gap label appearing at δ=0, asymptotic uncoupled-level dashes for reference)
- The change: Vary |V| from 0 to 0.5 eV and show the gap opening — demonstrating that the gap is exactly 2|V| (the perturbation matrix element).
- Teardown angle: Avoided crossings in solid-state physics create the band gap — the gap between valence and conduction bands that makes semiconductors work. The quantum mechanics is the same 2×2 matrix diagonalization; only the physical context changes.
- Exclusions: Landau-Zener transition probability, conical intersections, band structure calculations.
- Score: 8/10

## Candidate 05 — "Compute Fermi's Golden Rule: Transition Rates with Claude Code"
- Source: quantum-mechanics-vol3/chapters/06-radiation-and-fermis-golden-rule.md
- Lane: BUILD (Claude Code)
- Hook: An atom in an excited state decays by spontaneous emission. Fermi's golden rule gives the transition rate — and it depends on the density of final states, not just the matrix element. Claude Code computes the A coefficient for hydrogen 2p→1s.
- The artifact: A Manim animation of the hydrogen atom transitioning from 2p to 1s — an energy level diagram with the photon wavelength labeled (Lyman alpha, 121.6 nm), the transition matrix element |⟨1s|r|2p⟩| computed, and the spontaneous emission rate A₂₁ displayed and compared to the known value.
- Prompt seed: `claude "Write a Python script that computes the spontaneous emission rate for hydrogen 2p_z -> 1s using Fermi's golden rule: A = omega^3 * |d|^2 / (3*pi*eps0*hbar*c^3) where d = e*<1s|z|2p_z>. Compute the dipole matrix element numerically: d = e * integral(R_10(r)*R_21(r)*r^3 dr) * integral(Y_0^0 * cos(theta) * Y_1^0 * sin(theta) dtheta dphi). Compare to A_known = 6.27e8 s^-1 and print percent error."`
- Read / check: The dipole matrix element should give d ≈ e * 2.96 * 10^-11 m (from known result ⟨1s|r|2p⟩ = (2^7.5 / 3^5) a₀). A coefficient should agree with 6.27×10⁸ s⁻¹ within 5%. Lyman alpha wavelength: λ = 2πc/ω = 121.6 nm. Verify the angular integral gives 1/√3 (for z-component selection).
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim (energy level diagram with 2p and 1s levels, photon wavelength label, matrix element computation appearing step by step, final rate compared to NIST value)
- The change: Compute the rate for 3p→1s (second Lyman line) and 3p→2s — showing how A scales as ω³ and |d|².
- Teardown angle: The density of states factor in Fermi's golden rule is why spontaneous emission is irreversible — the photon escapes into a continuum of modes. Without that continuum, the atom would re-absorb the photon indefinitely (Rabi oscillations). The formula encodes both the coupling and the irreversibility.
- Exclusions: Stimulated emission and lasers, Einstein A and B coefficients full derivation, cavity QED.
- Score: 7/10

## Candidate 06 — "Plot the Band Structure: Tight-Binding Model with Claude Code"
- Source: quantum-mechanics-vol3/chapters/10-periodic-potentials-and-band-structure.md
- Lane: BUILD (Claude Code)
- Hook: Band gaps make semiconductors possible. The simplest model — tight-binding — gives the band structure E(k) = E0 - 2t·cos(ka) in 5 lines. Claude Code plots it and shows where the gap opens.
- The artifact: A Manim animation of the 1D tight-binding band structure E(k) vs k from -π/a to π/a — the cosine band drawing from left to right, the Brillouin zone boundaries marked, and a second band added by extending to a two-site unit cell with a gap opening at k=π/a.
- Prompt seed: `claude "Write a Python script that plots the 1D tight-binding band structure: (1) single-site unit cell: E(k) = E0 - 2*t*cos(k*a) for k in [-pi/a, pi/a], t=1 eV, a=3 Angstroms; (2) two-site unit cell with alternating hoppings t1=1.0 eV, t2=0.5 eV: E_pm(k) = E0 +/- sqrt(t1^2 + t2^2 + 2*t1*t2*cos(k*a)). Plot both on one figure with Brillouin zone boundaries marked. Print the band gap for case 2."`
- Read / check: Single-site band: bandwidth 4t=4 eV, no gap. Two-site band gap at k=π/a: gap = 2|t1-t2| = 1 eV. Verify the two-site formula reduces to the single-site case when t1=t2. Brillouin zone boundaries should be at k = ±π/a for single-site, ±π/(2a) for two-site.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim (single-site cosine band drawing, then two-site bands appearing with gap opening at zone boundary, gap labeled in eV)
- The change: Add a 2D square lattice tight-binding model — E(k_x,k_y) = E0 - 2t(cos(k_x*a)+cos(k_y*a)) — and plot as a 3D surface or 2D color map showing the Dirac point at K when the lattice is honeycomb (graphene).
- Teardown angle: The band gap from periodic potential is entirely a wave phenomenon — Bragg reflection at the Brillouin zone boundary splits a single band into two. The alternating hopping (dimerization) model shows how a structural distortion opens a gap at the Fermi level — the Peierls instability.
- Exclusions: DFT band structure, spin-orbit coupling, topological insulators.
- Score: 7/10
