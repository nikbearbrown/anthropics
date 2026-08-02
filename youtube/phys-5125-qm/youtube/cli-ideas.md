# PHYS 5125 Quantum Mechanics — CLI Video Ideas ("X with Claude")

---

## Candidate 01 — Build the Collider Bias Demo in QM Dress: Uncertainty from the Commutator
- Source: phys-5125-qm/chapters/02-ch1-formalism.md
- Lane: BUILD (Claude Code)
- Hook: The uncertainty relation σ_A σ_B ≥ |⟨[A,B]⟩|/2 is a theorem that follows from the commutator algebra alone. This script derives it numerically — no approximation — and sweeps over states to show which superpositions saturate it.
- The artifact: a Python script (~50 lines) using numpy that: (1) builds the position and momentum operators as finite-difference matrices on an N=500 grid, (2) computes [x̂,p̂] numerically and checks it equals iℏI, (3) sweeps over 20 random normalized states |ψ⟩ and plots σ_x σ_p vs |⟨[x̂,p̂]⟩|/2 for each, marking which are Gaussian (saturate) vs. which exceed the bound. Manim animates the scatter plot building up point by point with the equality line.
- Prompt seed: `claude "Write a Python script using numpy that: (1) builds discretized position and momentum operators as NxN matrices on a grid x = linspace(-5,5,500) with dx = 10/500; p_hat = -i*hbar * finite-difference matrix; (2) computes the commutator [x,p] numerically and verifies it approximates i*hbar*I; (3) generates 20 random normalized states psi, computes sigma_x = sqrt(<x^2>-<x>^2), sigma_p similarly, and the lower bound |<[x,p]>|/2; (4) prints a table of sigma_x * sigma_p vs bound for each state. Use hbar=1 units."`
- Read / check: Confirm the commutator [x,p] diagonal is approximately i (in ℏ=1 units). Verify that Gaussian states (generated separately as exp(-x²/2)) saturate the bound within numerical precision. Check that the finite-difference momentum operator is correctly anti-Hermitian.
- Human supplies: Nothing — fully synthetic. Python with numpy.
- Output medium: Manim (scatter plot: x-axis = lower bound |⟨[x,p]⟩|/2, y-axis = σ_x σ_p; all points above the y=x diagonal; Gaussian state marked with a star at the saturation point; the diagonal line animating in first)
- The change: Replace position/momentum with spin operators Sx and Sy (2×2 Pauli matrices) and show the uncertainty relation for spin — now the states are qubit superpositions.
- Teardown angle: The uncertainty relation is not a statement about measurement disturbance. It is a theorem about the algebra of operators — the commutator sets the floor, and no state can beat it. The Gaussian is special because it achieves the floor exactly.
- Exclusions: Relativistic QM, QFT, decoherence.
- Score: 9/10

---

## Candidate 02 — Build the Hydrogen Spectrum: Quantization from a Boundary Condition
- Source: phys-5125-qm/chapters/03-ch2-hydrogen-atom.md
- Lane: BUILD (Claude Code)
- Hook: The hydrogen spectrum falls out of one demand: the power series must terminate. This script implements the recursion relation for the radial wavefunctions and shows which energies allow termination — quantization from pure mathematics, not postulate.
- The artifact: a Python script (~60 lines) that: (1) implements the recurrence c_{k+1}/c_k = (k+ℓ+1-ρ_0)/(k+1)(k+2ℓ+2) for arbitrary ρ_0, (2) sweeps ρ_0 ∈ [1,5] for ℓ=0 and plots |P(ρ)| at ρ=10 vs ρ_0 — showing divergence everywhere except at ρ_0 = n (integer), (3) highlights the allowed values and labels their n quantum number. Manim animates the ρ_0 sweep as a curve, with the divergence dips animating in, then the allowed values highlighting in red.
- Prompt seed: `claude "Write a Python script using numpy and matplotlib that: (1) implements the power-series recursion relation for the hydrogen radial function: c[k+1] = c[k] * (k + l + 1 - rho_0) / ((k+1)*(k+2*l+2)) with l=0, c[0]=1; (2) for rho_0 in linspace(0.5, 5.5, 1000), computes |P(rho=10)| where P is summed to k=30; (3) plots |P(10)| vs rho_0 on a log scale, marking the minima near rho_0 = 1,2,3,4,5 with vertical lines labeled n=1,2,3,4,5; (4) prints the rho_0 values at those minima."`
- Read / check: Verify that the minima occur at ρ_0 = n = 1, 2, 3, 4, 5 within numerical precision. Confirm the series diverges between integer values (the points not at minima should show large |P(10)|). Check the recurrence formula matches the chapter derivation exactly.
- Human supplies: Nothing — fully synthetic. Python with numpy, matplotlib.
- Output medium: Manim (animated curve: ρ_0 on x-axis, log|P(10)| on y-axis; curve traces in left to right; at each n value, a vertical red line drops and a label appears "n=1 → E₁", "n=2 → E₂", etc.)
- The change: Repeat for ℓ=1 and show the minima shift by 1 (ρ_0 = 2,3,4,5 for ℓ=1) — demonstrating the n = n_r + ℓ + 1 rule.
- Teardown angle: Quantization is not imposed on the atom. The atom imposes it on itself, through the requirement that the wavefunction stay finite at infinity. The power series that doesn't terminate grows like e^ρ and can't be normalized — the boundary condition, not a postulate, forces the energy levels.
- Exclusions: Spin, relativistic corrections (Chapter 7), many-electron atoms.
- Score: 9/10

---

## Candidate 03 — Build the Stark Effect: Perturbation Theory at First and Second Order
- Source: phys-5125-qm/chapters/04-ch3-time-independent-pt.md
- Lane: BUILD (Claude Code)
- Hook: The quadratic Stark shift of hydrogen's ground state and the linear splitting of its first excited level demonstrate both orders of perturbation theory in one calculation — and the degeneracy rescue is the moment where the method nearly fails.
- The artifact: a Python script (~70 lines) using numpy and scipy.linalg that: (1) sets up the H-atom energy levels for n=1,2 in atomic units, (2) computes the first-order energy correction for n=1 ground state under electric field V = eEz (matrix element ⟨1s|z|1s⟩ = 0 by parity, so first-order vanishes), (3) computes the second-order shift for n=1 numerically (sum over n=2..10 intermediate states), (4) diagonalizes the 4×4 degenerate subspace for n=2 and shows linear Stark splitting. Output: a Manim two-panel: left shows n=1 level shift vs field strength E, right shows n=2 level splitting as a function of E with 4 levels diverging linearly.
- Prompt seed: `claude "Write a Python script in atomic units (hbar=m=e=1, a0=1) that: (1) computes matrix elements <nlm|z|n'l'm'> for hydrogen using the known analytic expressions or numerical integration on a radial grid; (2) shows E_ground^(1) = 0 (parity argument); (3) computes E_ground^(2) = sum_{n=2..8} |<nlm|eEz|1s>|^2 / (E_1 - E_n) as a function of electric field E in range 0 to 0.05 a.u.; (4) diagonalizes the 4x4 matrix for n=2 degenerate subspace (2s, 2p_0, 2p_+1, 2p_-1) in the field and plots all 4 eigenvalues vs E. Use scipy.linalg.eigh."`
- Read / check: Confirm E_ground^(1) = 0 from the parity argument (z has odd parity, |1s⟩ is even). Verify the second-order shift is negative (ground state lowers in a field). Confirm n=2 splitting shows two levels that shift linearly in E and two that remain degenerate (m=±1 states don't mix with z perturbation). Check atomic units are consistent throughout.
- Human supplies: Nothing — fully synthetic. Python with numpy, scipy.
- Output medium: Manim (two-panel: left — n=1 energy shift curve (quadratic, negative) vs field E; right — n=2 splitting showing 4 lines, 2 diverging linearly outward from the unperturbed level, 2 staying flat; field E animates from 0 to max value)
- The change: Set the field strength above the perturbation theory validity range and show the perturbation series diverging from the known exact result (Padé approximant comparison) — demonstrating the honest caveat about convergence.
- Teardown angle: The Stark effect is where perturbation theory both works and nearly fails in the same calculation. First order is zero, second order gives a real physical answer, and the degenerate n=2 level requires a rotation to a "good basis" before the formula can run. The machinery reveals itself under stress.
- Exclusions: Relativistic Stark effect, strong-field ionization.
- Score: 9/10

---

## Candidate 04 — Build the Exchange Energy: Where the Singlet-Triplet Split Comes From
- Source: phys-5125-qm/chapters/06-ch5-identical-particles.md
- Lane: BUILD (Claude Code)
- Hook: Spin never appears in the helium Hamiltonian. Yet it controls the singlet-triplet energy splitting. The exchange integral is a purely quantum effect with no classical analog — and it's computable in ~30 lines.
- The artifact: a Python script (~45 lines) using numpy and scipy.integrate that: (1) sets up the helium ground state as a product of two hydrogenic 1s wavefunctions, (2) computes the direct Coulomb integral J = ⟨1s1s|e²/r₁₂|1s1s⟩ numerically (the classical term), (3) computes the exchange integral K = ⟨1s2s|e²/r₁₂|2s1s⟩ numerically (the purely quantum term), (4) prints J and K in eV and explains that E_singlet - E_triplet = 2K. Manim animates a two-bar chart: J bar (classical, larger) and K bar (exchange, purely quantum), with labels explaining which goes with singlet vs triplet.
- Prompt seed: `claude "Write a Python script in atomic units (Z=2 for He, a0=1) that: (1) defines psi_1s(r) = 2*(Z/a0)^(3/2) * exp(-Z*r/a0) / sqrt(4*pi); (2) numerically computes the direct integral J = integral over r1,r2 of |psi_1s(r1)|^2 * (1/|r1-r2|) * |psi_1s(r2)|^2 d3r1 d3r2 using 3D Gaussian quadrature or Monte Carlo with N=100000 samples; (3) analytically notes the exchange integral K for 1s-2s He and prints its known value 1.19 eV; (4) prints J and K and the singlet-triplet splitting 2K. Use scipy.integrate or numpy random for Monte Carlo."`
- Read / check: Verify J ≈ 34 eV for helium ground state. Confirm K = 1.19 eV matches the known helium singlet-triplet splitting (approximately). Check that the Monte Carlo integral for J converges within ~5% with N=100000 samples.
- Human supplies: Nothing — fully synthetic. Python with numpy, scipy.
- Output medium: Manim (two-bar chart: J bar labeled "Direct (classical analog)" and K bar labeled "Exchange (no classical analog)"; K bar animates in colored distinctively; annotation: "E_singlet - E_triplet = 2K = 2.38 eV")
- The change: Vary Z from 1 to 4 (hydrogen through beryllium-like) and plot K vs Z — showing how the exchange integral scales and when Hund's rule breaks down.
- Teardown angle: Exchange is real energy. It determines whether two electrons with paired vs. parallel spins are more stable. And it comes entirely from the (anti)symmetry requirement on the wave function — from the indistinguishability of particles, not from anything in the Hamiltonian. Spin controls the energy through the back door of quantum statistics.
- Exclusions: Multi-configuration CI, DFT exchange-correlation functionals.
- Score: 9/10

---

## Candidate 05 — Build the Variational Bound: Helium Ground State from a One-Parameter Ansatz
- Source: phys-5125-qm/chapters/07-ch6-variational-method.md
- Lane: BUILD (Claude Code)
- Hook: Guess the shape, leave one parameter free, minimize the energy. For helium, a single number — the effective nuclear charge Z_eff — brings the variational estimate within 2% of the exact ground-state energy. This script does the whole calculation.
- The artifact: a Python script (~50 lines) using numpy and scipy.optimize that: (1) defines the helium trial wavefunction ψ(r₁,r₂;Z_eff) as a product of two hydrogenic 1s orbitals with effective charge Z_eff, (2) computes ⟨H⟩ analytically (the formula involves known hydrogen integrals plus the electron-electron repulsion term 5Z_eff/8 in atomic units), (3) minimizes over Z_eff using scipy.optimize.minimize_scalar, (4) prints the optimal Z_eff, the variational energy, and the percent error vs. the exact E = -2.904 a.u. Manim animates ⟨H⟩ vs Z_eff curve with the minimum highlighted.
- Prompt seed: `claude "Write a Python script in atomic units that computes the variational energy for helium using a trial wavefunction psi(r1,r2;Z) = phi_1s(r1;Z)*phi_1s(r2;Z) where phi_1s(r;Z)=(Z^3/pi)^(1/2)*exp(-Z*r). The variational energy is E(Z) = Z^2 - 2*Z*(2) + 5*Z/8 (in atomic units, using known He integrals). Minimize E(Z) over Z using scipy.optimize.minimize_scalar in range (1,3). Print the optimal Z_eff, E_variational, and percent error vs exact -2.9037 a.u. Plot E(Z) vs Z for Z in [1,3]."`
- Read / check: Verify the analytical formula E(Z) = Z² - 4Z + 5Z/8. Confirm the minimum occurs at Z_eff = 27/16 ≈ 1.6875. Verify the variational energy -2.848 a.u. is above the exact -2.904 a.u. (the variational theorem guarantees this). Check the percent error is ~2%.
- Human supplies: Nothing — fully synthetic. Python with numpy, scipy.
- Output medium: Manim (curve: ⟨H⟩ vs Z_eff, parabola-like shape; minimum point highlighted with label "Z_eff = 27/16, E = -2.848 a.u."; exact energy dashed line below; annotation "variational bound: always above exact")
- The change: Add a second variational parameter (let the two electrons have different effective charges Z₁ and Z₂) and show the energy improvement — demonstrating that richer ansätze give tighter bounds.
- Teardown angle: The variational principle is the most useful inequality in quantum mechanics. It turns the intractable (exact ground state of multi-electron atoms) into a concrete optimization problem: guess, compute, improve the guess. The 2% accuracy from one parameter is remarkable for a two-line ansatz.
- Exclusions: DFT, Hartree-Fock, coupled-cluster — these are the extensions the method grew into.
- Score: 9/10

---

## Candidate 06 — Build the Rabi Oscillation: Time-Dependent Perturbation on a Two-Level System
- Source: phys-5125-qm/chapters/05-ch4-time-dependent-pt.md
- Lane: BUILD (Claude Code)
- Hook: A resonant oscillating field pumps a two-level system back and forth between ground and excited state at the Rabi frequency. On-resonance: complete inversion. Off-resonance: partial oscillation. This is the physics of every atomic clock and NMR machine.
- The artifact: a Python script (~50 lines) using numpy and scipy.integrate.solve_ivp that: (1) sets up the two-level Hamiltonian H(t) = ℏω₀/2 σ_z + ℏΩ cos(ωt) σ_x, (2) integrates the Schrödinger equation for C_1(t), C_2(t) over 0 to 5T_Rabi, (3) plots |C_2(t)|² (excited state population) for three cases: ω = ω₀ (resonance), ω = ω₀ ± Δ with Δ = 0.2 Ω. Manim animates the three curves building simultaneously, labeled by detuning.
- Prompt seed: `claude "Write a Python script using numpy and scipy.integrate.solve_ivp that solves the two-level Schrödinger equation in the rotating wave approximation. Parameters: omega_0 = 1.0, Omega (Rabi coupling) = 0.1, integrate from t=0 to t=200/omega_0. Solve for three cases: delta=omega-omega_0 in [-0.2, 0, +0.2] (in units of Omega). Plot |C2(t)|^2 (excited state population) vs t for all three cases on one plot. In the RWA, the equations are: dC1/dt = -i*Omega/2 * exp(i*delta*t) * C2, dC2/dt = -i*Omega/2 * exp(-i*delta*t) * C1, with C1(0)=1, C2(0)=0."`
- Read / check: Confirm on-resonance (Δ=0) shows complete oscillation to |C_2|²=1. Verify off-resonance cases show reduced amplitude oscillations at higher frequency (generalized Rabi frequency Ω_R = √(Ω²+Δ²)). Check that RWA equations are correctly implemented with the complex exponential.
- Human supplies: Nothing — fully synthetic. Python with numpy, scipy.
- Output medium: Manim (three animated curves on one plot: on-resonance (red, full amplitude), +detuning (blue, reduced), -detuning (green, reduced); all building simultaneously from left to right; y-axis 0 to 1, labeled "|C₂(t)|² = excited population")
- The change: Add the Bloch sphere visualization — show the state vector precessing on the Bloch sphere for the on-resonance case, sweeping a great circle.
- Teardown angle: Rabi oscillations are the clock of quantum control. Every quantum gate in a quantum computer is a calibrated Rabi pulse — a precisely timed resonant drive that rotates the state vector by exactly the right angle. The detuning curves show why being slightly off-resonance degrades the gate fidelity.
- Exclusions: Dissipation, Lindblad master equation, decoherence.
- Score: 9/10

---

## Candidate 07 — Build the Hyperfine Splitting: The 21-cm Line from First Principles
- Source: phys-5125-qm/chapters/08-ch7-fine-hyperfine.md
- Lane: BUILD (Claude Code)
- Hook: The 21-cm hydrogen line is the most important spectral line in radio astronomy. It comes from the hyperfine splitting of hydrogen's ground state — two spin-1/2 particles (electron and proton) coupling to form triplet and singlet states separated by 5.87 μeV. This script computes it.
- The artifact: a Python script (~40 lines) using scipy.constants that: (1) defines the hyperfine coupling constant A using the formula A = (2μ_0/3) g_e μ_B g_p μ_N |ψ_1s(0)|², (2) computes |ψ_1s(0)|² = 1/(π a₀³), (3) evaluates A numerically in joules and eV, (4) computes the singlet-triplet splitting ΔE = A (eigenvalues from the 4×4 matrix: E_triplet = A/4, E_singlet = -3A/4, so ΔE = A), (5) converts to frequency (21.1 cm wavelength). Manim animates the 4×4 spin matrix diagonalizing, the triplet and singlet levels appearing, and the 21-cm photon emitting.
- Prompt seed: `claude "Write a Python script using scipy.constants that computes the hyperfine splitting of hydrogen's ground state. Use: A = (2*mu_0/3) * g_e * mu_B * g_p * mu_N * abs_psi_1s_0_squared, where abs_psi_1s_0_squared = 1/(pi * a0^3), g_e=2.002, g_p=5.586, mu_B = e*hbar/(2*m_e), mu_N = e*hbar/(2*m_p). Print A in joules and eV. From the eigenvalues (A/4 for triplet, -3A/4 for singlet), compute the splitting delta_E = A, convert to frequency f = delta_E/h and wavelength lambda = c/f. Verify lambda is approximately 21.1 cm."`
- Read / check: Verify μ_B = 9.274 × 10⁻²⁴ J/T from scipy.constants. Verify |ψ_1s(0)|² = 1/(π a₀³) with a₀ from scipy.constants. Confirm ΔE ≈ 5.87 μeV and λ ≈ 21.1 cm. Check the eigenvalue calculation: E_triplet = A/4, E_singlet = -3A/4 from the 4×4 matrix.
- Human supplies: Nothing — fully synthetic. Python with scipy.
- Output medium: Manim (left panel: 4×4 spin matrix animating to diagonal form; right panel: two energy levels (triplet above, singlet below) with a 21-cm photon arrow between them, labeled with ΔE = 5.87 μeV and λ = 21.1 cm)
- The change: Scale the calculation to a muonic hydrogen atom (replace m_e with m_μ = 207 m_e) and show how the hyperfine splitting scales — demonstrating the mass dependence of μ_B.
- Teardown angle: The 21-cm line is the only spectral line visible through most of the interstellar medium. Radio astronomers have mapped the entire Milky Way with it. It comes from two spin-1/2 particles doing quantum bookkeeping — the triplet-to-singlet decay emits one photon with a 1-in-10-million-year lifetime in any given atom, and there are enough hydrogen atoms to make it the brightest radio line in the sky.
- Exclusions: Fine structure, Zeeman effect, magnetic resonance.
- Score: 10/10

---

## Candidate 08 — Build the Fermi's Golden Rule Calculator: Transition Rate from a Perturbation
- Source: phys-5125-qm/chapters/05-ch4-time-dependent-pt.md
- Lane: BUILD (Claude Code)
- Hook: Fermi's Golden Rule says the transition rate from state i to state f under a perturbation is Γ = (2π/ℏ)|⟨f|V|i⟩|² ρ(E_f). This script applies it to spontaneous photon emission from hydrogen and recovers the known 2p→1s lifetime.
- The artifact: a Python script (~55 lines) using scipy.constants and numpy that: (1) sets up the hydrogen 2p→1s transition in atomic units, (2) computes the dipole matrix element ⟨1s|r|2p_m=0⟩ using the known radial integral, (3) computes the density of states ρ(E) for the emitted photon using the 3D free-photon density of states, (4) applies Fermi's Golden Rule to get the transition rate Γ and spontaneous emission lifetime τ = 1/Γ, (5) compares to the known τ = 1.596 ns. Manim animates the two-level diagram with a photon emitting and the lifetime τ appearing.
- Prompt seed: `claude "Write a Python script in atomic units (hbar=m=e=1, c=137) that computes the 2p->1s spontaneous emission rate in hydrogen using Fermi's Golden Rule. The dipole matrix element: |<1s|r|2p_0>|^2 = (2^8/3^10) * a0^2 (known value, cite it). The photon frequency: omega_0 = E_2p - E_1s = 3/8 Ry in a.u. The spontaneous emission rate: Gamma = (4*omega_0^3*e^2)/(3*hbar*c^3) * |<1s|r|2p>|^2. Convert tau=1/Gamma to seconds. Compare to known tau=1.596 ns."`
- Read / check: Verify the radial matrix element |⟨1s|r|2p⟩|² = 128/243 in atomic units (standard hydrogen result). Confirm ω_0 = 3/8 Ry = 10.2 eV/ℏ. Check that the computed τ is within 5% of 1.596 ns. Verify c = 137 a.u. is correct (atomic units: c = 1/α ≈ 137).
- Human supplies: Nothing — fully synthetic. Python with scipy.constants, numpy.
- Output medium: Manim (two-level diagram: 2p level above, 1s below; photon arrow animating downward with wavelength label "λ = 121.6 nm (Lyman-α)"; τ = 1.596 ns appearing with calculation trace)
- The change: Compute the ratio of 2p→1s to 3p→1s transition rates and show why the 3p→1s lifetime is longer (scales as ω³, so the lower frequency 3p→1s photon decays more slowly).
- Teardown angle: Fermi's Golden Rule is the bridge between quantum mechanics and the macroscopic world of rates and lifetimes. Every atomic transition, every beta decay rate, every tunneling current in a semiconductor traces back to this formula — the density of states times the matrix element squared.
- Exclusions: Multi-photon transitions, stimulated emission, laser physics.
- Score: 8/10
