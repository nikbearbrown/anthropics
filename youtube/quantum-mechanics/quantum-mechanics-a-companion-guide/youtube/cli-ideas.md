# Quantum Mechanics: A Companion Guide — CLI Video Ideas ("X with Claude")

## Candidate 01 — "Simulate the Ultraviolet Catastrophe: Planck vs. Rayleigh-Jeans with Claude Code"
- Source: quantum-mechanics-a-companion-guide/chapters/01-why-quantum-mechanics.md
- Lane: BUILD (Claude Code)
- Hook: The Rayleigh-Jeans law predicts infinite energy in a box. Planck fixed it by quantizing energy exchange. The two curves on one plot tell the whole story of why classical physics failed.
- The artifact: A Manim animation of the blackbody spectrum at T=5000K — the Rayleigh-Jeans curve (blue, diverging to infinity at high frequencies) and the Planck curve (orange, showing a peak then exponential drop) drawing simultaneously. The divergence point animates with a label: "ultraviolet catastrophe."
- Prompt seed: `claude "Write a Python script using numpy and matplotlib that plots the Rayleigh-Jeans spectral energy density rho_RJ(nu) = 8*pi*nu^2*k_B*T/c^3 and the Planck distribution rho_Planck(nu) = (8*pi*h*nu^3/c^3)/(exp(h*nu/(k_B*T))-1) for T=5000K, nu from 1e12 to 2e15 Hz. Use physical constants from scipy.constants. Cap the RJ curve at 3x the Planck peak for display. Label the peak wavelength and the catastrophe region."`
- Read / check: Planck peak should be near 580 nm (visible, T=5000K). Rayleigh-Jeans should agree with Planck at low frequencies (nu < 1e13 Hz) and diverge at high frequencies. Verify physical constants from scipy.constants (h, c, k_B). The cap on RJ prevents the plot from being unreadable.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim (animated dual curves drawing together, RJ diverging at high frequency, Planck curving gracefully, catastrophe region shaded in red)
- The change: Animate the transition from T=3000K to T=6000K — show the peak wavelength shifting (Wien's law) as temperature changes.
- Teardown angle: Planck's quantization of energy exchange — not of light itself — is the specific claim that fixed the catastrophe. Einstein's 1905 paper quantized the field. Understanding which came first matters for understanding what quantum mechanics actually says.
- Exclusions: Bose-Einstein statistics derivation, Stefan-Boltzmann total power, blackbody engineering applications.
- Score: 9/10

## Candidate 02 — "Build the 1D Quantum Sandbox: Infinite Square Well with Claude Code"
- Source: quantum-mechanics-a-companion-guide/chapters/04-one-dimensional-problems.md
- Lane: BUILD (Claude Code)
- Hook: The particle-in-a-box has an exact solution. Claude Code can reproduce it numerically using matrix diagonalization — and the first check is whether E_n = n²π²ℏ²/2mL² to 6 decimal places.
- The artifact: A Manim animation of the first four wave functions ψ₁–ψ₄ plotted inside the box, each appearing in sequence with its energy level labeled. The energy ladder grows on the left side of the frame as each eigenfunction appears.
- Prompt seed: `claude "Write a Python script that numerically solves the 1D infinite square well (L=1 nm, electron mass) using finite-difference matrix diagonalization: build the tridiagonal Hamiltonian H with N=500 grid points, diagonalize with scipy.linalg.eigh, find the first 4 eigenstates. Plot them offset vertically by their energies. Compare numerical energies to the analytic E_n = n^2*pi^2*hbar^2/(2*m*L^2) and print the fractional error."`
- Read / check: Fractional errors should be below 0.01% for n=1–4 with N=500. Wave functions should show 1, 2, 3, 4 half-wavelengths respectively. All wave functions should be zero at boundaries x=0 and x=L. Energy ordering should be E₁ < E₂ < E₃ < E₄.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim (wave functions appearing one by one, energy ladder growing on the left, analytic vs. numerical comparison table appearing)
- The change: Change the potential to a finite square well (V=0 inside, V=10 eV outside) and show the evanescent tail — the wave function penetrating classically forbidden regions.
- Teardown angle: The zero-point energy E₁ > 0 is not an artifact of quantization — it is forced by the uncertainty principle. Confine the particle and finite position uncertainty forces nonzero momentum uncertainty forces nonzero kinetic energy. The simulation makes this inevitable.
- Exclusions: Harmonic oscillator ladder operators, delta-function potential, scattering states.
- Score: 9/10

## Candidate 03 — "Compute the CHSH Inequality Violation with Claude Code"
- Source: quantum-mechanics-a-companion-guide/chapters/10-quantum-mechanics-in-the-modern-world.md
- Lane: BUILD (Claude Code)
- Hook: Bell's theorem fits on one page of algebra. The violation is 2√2 ≈ 2.83, not 2. Claude Code computes it from scratch in 15 lines — then finds the measurement angles that maximize it.
- The artifact: A Manim animation of a number line from 0 to 3, with three labeled regions animating: "Classical LHV: |S| ≤ 2" (gray), "Quantum maximum: |S| = 2√2" (blue dot appearing), "Tsirelson bound" (dashed line). Then the four correlation functions E(aᵢ,bⱼ) fill in as the calculation runs.
- Prompt seed: `claude "Write a Python script that computes the CHSH parameter S for the singlet state at measurement angles a1=0, a2=pi/2, b1=pi/4, b2=-pi/4. Use the formula E(theta_a, theta_b) = -cos(theta_a - theta_b) for spin-1/2 singlet correlations. Compute S = E(a1,b1) + E(a1,b2) + E(a2,b1) - E(a2,b2). Verify S = 2*sqrt(2) and print each correlation function and S. Then use scipy.optimize.minimize to find the 4 angles that maximize |S|."`
- Read / check: S should be exactly -2√2 ≈ -2.828 (or +2√2 depending on sign convention). Each correlation E should be ±1/√2. The optimizer should reproduce the same angles (or equivalent by symmetry). Verify the formula uses cos, not cos², and that the angle differences match the derivation.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim (number line animation showing LHV bound at 2 and quantum value at 2√2; four correlation values filling in one by one; optimizer trajectory shown as dots converging)
- The change: Sweep all four angles simultaneously using a grid search and plot the surface of S values — showing the maximum at the standard angles is a true global maximum.
- Teardown angle: The CHSH derivation assumes only that outcomes are predetermined (±1) and local — no quantum mechanics needed. The quantum calculation then shows the same formula exceeds the bound. That gap is what the 2022 Nobel Prize closed experimentally.
- Exclusions: Loophole discussion, Tsirelson bound proof, quantum cryptography applications.
- Score: 9/10

## Candidate 04 — "Animate Wave Packet Tunneling Through a Barrier with Claude Code"
- Source: quantum-mechanics-a-companion-guide/chapters/04-one-dimensional-problems.md
- Lane: BUILD (Claude Code)
- Hook: Classically, a particle without enough energy never crosses a barrier. Quantum mechanically, it does — with a transmission coefficient that drops exponentially with barrier width. Watch it happen.
- The artifact: A Manim animation of a Gaussian wave packet propagating toward a rectangular barrier — the packet splitting into a reflected part and a transmitted (tunneling) part, with a real-time normalization indicator and a tunneling coefficient readout.
- Prompt seed: `claude "Write a Python script that time-evolves a 1D Gaussian wave packet through a rectangular barrier using the split-operator Fourier method: (1) initial state psi(x,0) = Gaussian centered at x=-5nm with k0=5/nm; (2) barrier: V=2eV for -0.5nm < x < 0.5nm, else V=0; (3) electron energy ~1 eV (below barrier); (4) evolve for 500 time steps; (5) animate |psi|^2 using matplotlib.animation; (6) print transmission and reflection coefficients each frame."`
- Read / check: Transmission coefficient T = exp(-2*kappa*d) should be approximately exp(-2*sqrt(2m*0.5eV)*0.5nm/hbar) ≈ 0.02 for these parameters. Reflected + transmitted probability should sum to 1 (normalization). Verify the split-operator method uses exp(-iV*dt/2*hbar) * FFT * exp(-iK^2*dt/(2m*hbar)) * IFFT * exp(-iV*dt/2*hbar).
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim (animated wave packet propagating and splitting — blue |ψ|² filled, red barrier rectangle, tunneling coefficient readout updating in corner)
- The change: Vary the barrier width from 0.1 nm to 2 nm and plot T vs. d — showing the exponential decay and the "rule of thumb" that T drops by ~7x per ångström for a 4 eV barrier.
- Teardown angle: Tunneling is not the wave function "leaking through" — it is the evanescent solution in the classically forbidden region connecting two propagating solutions. The split-operator method reveals this because it evolves the Schrödinger equation exactly on the grid.
- Exclusions: WKB derivation, Josephson effect, radioactive decay alpha tunneling.
- Score: 8/10

## Candidate 05 — "Variational Calculation: Estimate Helium Ground State Energy with Claude Code"
- Source: quantum-mechanics-a-companion-guide/chapters/09-approximation-methods.md
- Lane: BUILD (Claude Code)
- Hook: The helium atom has no exact solution. Hylleraas reproduced the ground state energy to 4 significant figures in 1929 with a variational trial function. Claude Code does it in 10 lines.
- The artifact: A Manim animation showing the variational energy as a function of the effective nuclear charge Z_eff — a curve drawing from left to right, the minimum marking at Z_eff = 27/16 = 1.6875, and the variational bound E_var appearing above the exact value E_exact on a vertical energy axis.
- Prompt seed: `claude "Write a Python script that performs the variational calculation for helium ground state energy using a trial wave function psi = exp(-Z_eff*(r1+r2)/a0): (1) compute <T> + <V_nuclear> + <V_ee> as functions of Z_eff analytically (using known hydrogen-like integrals); (2) minimize the total energy E(Z_eff) using scipy.optimize.minimize_scalar; (3) report optimum Z_eff, variational energy in eV, and compare to the exact -79.0 eV."`
- Read / check: Optimum Z_eff should be 27/16 = 1.6875. Variational energy should be approximately -77.5 eV (Griffiths result). This is above -79.0 eV (exact), consistent with the variational principle. Verify the expression for <V_ee> = 5Z_eff/8 * (e²/4πε₀a₀) is used correctly.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim (E(Z_eff) curve drawing, minimum marked with dashed lines, variational vs. exact energy comparison on vertical axis with gap highlighted)
- The change: Add a second, more flexible trial function with two parameters (Z_eff1 ≠ Z_eff2 for each electron) and show the improved variational bound.
- Teardown angle: The variational principle guarantees an upper bound — the true ground state energy is always at or below the variational estimate. The 2% error from a one-parameter function is remarkable for a fully ab initio calculation.
- Exclusions: Hylleraas 6-parameter calculation, DFT, Hartree-Fock method.
- Score: 8/10

## Candidate 06 — "Research the Five Experiments That Broke Classical Physics with Claude"
- Source: quantum-mechanics-a-companion-guide/chapters/01-why-quantum-mechanics.md
- Lane: RESEARCH (Claude assistant)
- Hook: Five experiments killed classical physics between 1900 and 1926. Each one forced a specific quantization. Claude can reconstruct the cause-and-effect chain with citations.
- The artifact: A Remotion animated timeline — five experiments appearing chronologically with: year, experiment name, what classical physics predicted, what was observed, what quantization was forced. Each row animates in with the "forced quantization" result highlighted.
- Prompt seed: `claude "Research the five experiments that motivated quantum mechanics: blackbody radiation (1900), photoelectric effect (1905), Compton scattering (1923), Bohr model / hydrogen spectra (1913), Davisson-Germer electron diffraction (1927). For each: (1) what classical physics predicted quantitatively; (2) what was actually observed; (3) what quantization hypothesis was required. Cite original papers. Format as a 5-row chronological table."`
- Read / check: Blackbody: Rayleigh-Jeans diverges, Planck quantizes energy exchange (not light). Photoelectric: intensity should matter, frequency doesn't — Einstein quantizes light itself. Compton: continuous scattering, discrete momentum transfer. Bohr: radiation should be continuous, discrete lines observed. Davisson-Germer: electrons diffract like waves. Verify citation for Davisson & Germer (Phys. Rev. 30, 705, 1927).
- Human supplies: Nothing — citations are all public domain or freely accessible. Human should verify one or two citation DOIs.
- Output medium: Remotion (animated timeline — rows appear chronologically, each with classical prediction → observed → forced quantization columns populating left to right)
- The change: Add a sixth row: Stern-Gerlach (1922) — continuous angular momentum predicted, discrete spin-1/2 observed, quantization of angular momentum forced.
- Teardown angle: The five experiments are not independent failures of classical physics — they are a connected sequence. Each one made a specific, quantitative prediction that failed in a specific, quantitative way. The pattern is accumulating evidence, not revolutionary overthrow.
- Exclusions: EPR paradox, Bell's theorem, measurement problem philosophy.
- Score: 7/10

## Candidate 07 — "Compute the Photoelectric Effect Threshold Across Multiple Metals with Claude Code"
- Source: quantum-mechanics-a-companion-guide/chapters/01-why-quantum-mechanics.md
- Lane: BUILD (Claude Code)
- Hook: Einstein's 1905 equation K_max = hν - φ predicts a sharp threshold frequency that depends on the metal's work function. Claude Code computes the threshold for 6 common metals in 5 lines.
- The artifact: A Manim animation of threshold wavelengths and photon energies for 6 metals — a bar chart where each metal's bar extends to its threshold wavelength (nm), color-coded by whether visible light can eject photoelectrons or only UV can.
- Prompt seed: `claude "Write a Python script that computes the photoelectric threshold wavelength for 6 metals: cesium (phi=2.1 eV), potassium (2.3 eV), sodium (2.36 eV), aluminum (4.08 eV), copper (4.70 eV), platinum (5.65 eV). Use lambda_0 = h*c/phi. Print a table with metal, work function, threshold wavelength (nm), and whether visible light (380-700 nm) can eject electrons. Plot a bar chart."`
- Read / check: Cesium threshold: 1240/2.1 ≈ 590 nm (visible — orange light!). Platinum: 1240/5.65 ≈ 220 nm (deep UV only). Verify formula uses 1240 eV·nm constant. Table should have 6 rows × 4 columns. Bar chart should have a vertical line marking 380 nm and 700 nm (visible range boundaries).
- Human supplies: Nothing — fully synthetic (NIST work function values are public).
- Output medium: Manim (animated bar chart — bars extend to threshold wavelength, vertical lines marking visible range, labels showing "visible" or "UV only" per metal)
- The change: Add a kinetic energy calculation — for 350 nm UV light hitting each metal, compute K_max for each metal that it can ionize, and plot K_max vs. metal.
- Teardown angle: The linear relationship K_max = hν - φ (two parallel lines for two metals, differing only in φ) is what Millikan measured to disprove Einstein's theory and accidentally confirmed it. The slope gives h. The teardown is about how confirming evidence can be gathered by someone trying to refute.
- Exclusions: Photomultiplier tubes, CCD sensor design, work function temperature dependence.
- Score: 7/10

## Candidate 08 — "Visualize the Compton Scattering Formula with Claude Code"
- Source: quantum-mechanics-a-companion-guide/chapters/01-why-quantum-mechanics.md
- Lane: BUILD (Claude Code)
- Hook: Compton's wavelength shift formula Δλ = (h/m_e c)(1 - cos θ) predicts exactly how much X-ray wavelength increases with scattering angle. At 90° it's 2.43 pm. Claude Code plots the full angular dependence in 8 lines.
- The artifact: A Manim animation of Δλ vs. scattering angle θ from 0° to 180° — the curve drawing from left to right, with key angles labeled (0° → Δλ=0; 90° → λ_C; 180° → 2λ_C). The Compton wavelength λ_C = 2.426 pm appears as a horizontal reference line.
- Prompt seed: `claude "Write a Python script that plots the Compton wavelength shift delta_lambda = (h/(m_e*c)) * (1 - cos(theta)) for theta from 0 to pi radians. Use scipy.constants for h, m_e, c. Label the Compton wavelength lambda_C = h/(m_e*c) as a horizontal dashed line. Mark theta = pi/2 and theta = pi. Print the shift at 90 and 180 degrees in picometers."`
- Read / check: At θ=90°: Δλ = h/(m_e c) ≈ 2.426 pm. At θ=180°: Δλ = 2×2.426 pm ≈ 4.852 pm. Verify scipy.constants values match NIST. Curve should be zero at θ=0 and monotonically increasing to 2λ_C at θ=π. Plot should have labeled axes in radians (or degrees with conversion).
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim (curve drawing left to right, key points appearing with labels, Compton wavelength reference line animating in)
- The change: Compute the shift for a 0.1 nm X-ray (hard X-ray typical energy) and show the shifted wavelength at three angles — making the physical measurement concrete.
- Teardown angle: The Compton shift is tiny — picometers. The fact that Compton measured it to 0.5% precision in 1923, confirming Einstein's photon hypothesis that Millikan had tried to disprove, closed the photon debate. The precision of the measurement is the story.
- Exclusions: Inverse Compton scattering, Klein-Nishina formula, Compton polarimetry.
- Score: 7/10
