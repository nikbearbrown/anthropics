# Quantum Mechanics Vol. 5 (Mathematical Methods) — CLI Video Ideas ("X with Claude")

## Candidate 01 — "Visualize the Fourier Transform: From Square Wave to Sine Components with Claude Code"
- Source: quantum-mechanics-vol5/chapters/06-the-fourier-transform.md
- Lane: BUILD (Claude Code)
- Hook: A square wave is a sum of infinitely many sine waves. Claude Code builds the Fourier series one term at a time and animates the convergence — Gibbs phenomenon and all.
- The artifact: A Manim animation — left panel: partial Fourier sums 1, 3, 5, 7, 9 terms appearing on the square wave; right panel: the Fourier spectrum showing spikes at odd harmonics. Both panels animate simultaneously as each new term is added.
- Prompt seed: `claude "Write a Python script that: (1) computes the Fourier series for a square wave f(x) = 4/pi * sum(sin((2n-1)*x)/(2n-1), n=1 to N) for N=1,3,5,7,9,15; (2) plots all 6 partial sums on one figure; (3) plots the amplitude spectrum |c_n| vs n; (4) computes and prints the Gibbs overshoot (maximum value) for each N and shows convergence to ~1.089 (9% overshoot). Use numpy for the computation."`
- Read / check: 1-term approximation: simple sine. 9-term approximation: recognizably square with ringing. Gibbs overshoot should stabilize near 1.089 regardless of N. Amplitude spectrum should show spikes only at odd n with amplitudes 4/(π·n). Verify the total energy (Parseval: sum of |c_n|²) converges to 1 as N→∞.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim (dual-panel animation: left panel accumulates Fourier terms on the square wave, right panel spectrum spikes appear one by one at odd harmonics)
- The change: Replace the square wave with the uncertainty-principle connection: show that a narrower Gaussian in position space has a wider Gaussian in frequency space, making σ_x·σ_k = 1/2 visible as a Fourier pair relationship.
- Teardown angle: The Gibbs phenomenon — the 9% overshoot that never disappears no matter how many terms you add — is the mathematical reason why windowing functions exist in signal processing. The Fourier series converges in L² but not pointwise at discontinuities.
- Exclusions: Discrete Fourier transform (FFT algorithm), Nyquist sampling theorem, filter design.
- Score: 9/10

## Candidate 02 — "Build a Quantum Uncertainty Calculator: Position-Momentum Fourier Pair"
- Source: quantum-mechanics-vol5/chapters/06-the-fourier-transform.md + quantum-mechanics-vol5/chapters/09-operators-and-dirac-notation.md
- Lane: BUILD (Claude Code)
- Hook: The Heisenberg uncertainty principle is a theorem about Fourier transform pairs. Claude Code proves it numerically for 4 wave functions and shows the Gaussian minimizes σ_x·σ_p.
- The artifact: A Manim two-panel animation — position space (|ψ(x)|² in blue) and momentum space (|φ(k)|² in orange) side by side. σ_x and σ_p computed and displayed for each of 4 wave functions. The product σ_x·σ_p/ℏ shown as a bar, with 0.5 (minimum for Gaussian) as the reference line.
- Prompt seed: `claude "Write a Python script that computes sigma_x and sigma_p for 4 wave functions on a 1000-point grid [-10 to 10 nm]: (1) Gaussian a=1nm, (2) infinite-well ground state L=4nm, (3) double-Gaussian peaks at ±1nm sigma=0.3nm, (4) top-hat width=2nm. For each: compute psi(x), normalize, compute sigma_x via <x^2>-<x>^2, take FFT to get phi(k), normalize, compute sigma_k via <k^2>-<k>^2. Print sigma_x*sigma_k/(0.5) for each — Gaussian should give 1.0."`
- Read / check: Gaussian: σ_x·σ_k/(0.5) ≈ 1.0 (saturates bound). Infinite well: ≈ 1.14. Double-Gaussian: > 2 (two peaks in position → two peaks in momentum, product larger). Top-hat: > 1 (sinc function in momentum space has wide tails). All ratios ≥ 1. Verify FFT normalization: phi(k) = dx * FFT(psi) with correct k-axis from numpy.fft.fftfreq.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim (two-panel side-by-side, four wave functions cycling through, σ_x·σ_k bar chart updating for each, reference line at the Heisenberg minimum)
- The change: Sweep Gaussian width a from 0.5 to 5 nm and plot σ_x·σ_k as a function of a — showing it is constant (= ℏ/2) confirming the Gaussian as the minimum-uncertainty state for any width.
- Teardown angle: The uncertainty principle is not about measurement disturbance — it is about Fourier pairs. A wave function narrow in position space must be wide in momentum space because of how the Fourier transform works. The math forces it, not any physical limitation on measurement precision.
- Exclusions: Time-energy uncertainty, Robertson inequality for general observables, Wigner function.
- Score: 9/10

## Candidate 03 — "Diagonalize a Quantum Hamiltonian: Eigenvalues and Eigenvectors with Claude Code"
- Source: quantum-mechanics-vol5/chapters/08-eigenvalues-and-diagonalization.md
- Lane: BUILD (Claude Code)
- Hook: The energy levels of a quantum system are the eigenvalues of its Hamiltonian. Claude Code diagonalizes a 4×4 Hamiltonian and shows what "good quantum numbers" means algebraically.
- The artifact: A Manim animation of the 4×4 matrix transforming to diagonal form — the off-diagonal elements shrinking to zero as a unitary transformation rotates the basis, the eigenvalues appearing on the diagonal.
- Prompt seed: `claude "Write a Python script that diagonalizes the two-qubit Hamiltonian H = -J*(sigma_z x sigma_z) + h*(sigma_z x I + I x sigma_z) for J=1 eV, h=0.5 eV. Use numpy 4x4 matrix representation: sigma_z=[[1,0],[0,-1]], compute H using np.kron. Diagonalize with numpy.linalg.eigh. Print eigenvalues and eigenvectors. Verify H*v = E*v for each eigenpair. Plot the energy spectrum as a function of h from -2 to 2 eV, showing level crossings or avoided crossings."`
- Read / check: At h=0: eigenvalues should be {-J, J, J, -J} = {-1, 1, 1, -1} eV. At large h: eigenvalues should approach ±2h (polarized states dominate). Level crossings or avoided crossings should appear near h=0. Verify all eigenvectors are orthonormal (V@V.T = I). Print the degeneracy structure at h=0.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim (4×4 matrix appearing, eigenvalue equation animating, energy vs h plot with 4 curves drawing)
- The change: Add entanglement entropy — compute von Neumann entropy S = -Tr(ρ_A log ρ_A) for the ground state at each value of h, and show how entanglement peaks near the level crossing.
- Teardown angle: Diagonalization transforms a problem into the basis where it is trivially solvable — in this basis, the Hamiltonian is just a list of energy values. The "good quantum numbers" are the quantum numbers associated with the diagonal basis. Finding this basis is what quantum mechanics problems are mostly about.
- Exclusions: QR algorithm, LAPACK internals, sparse matrix methods.
- Score: 8/10

## Candidate 04 — "Compute Tensor Products: Build Two-Qubit States from Single Qubits"
- Source: quantum-mechanics-vol5/chapters/16-tensor-products-and-composite-systems.md
- Lane: BUILD (Claude Code)
- Hook: Two qubits live in a 4-dimensional space. The tensor product is the mathematical operation that builds the composite system — and it is the gate to understanding entanglement.
- The artifact: A Manim animation showing the tensor product construction — two 2-element state vectors appearing, the Kronecker product operation animating to produce a 4-element vector, then the separability check: can the 4-element vector be written as a tensor product of two 2-element vectors?
- Prompt seed: `claude "Write a Python script that: (1) computes the tensor product of two single-qubit states using np.kron; (2) constructs four test states: |00>, (|+>|0>), (|0>+i|1>)/sqrt(2) x |+>, and the Bell state (|00>+|11>)/sqrt(2); (3) for each 4-element state vector, attempts to find single-qubit states a,b such that state = kron(a,b) using optimization; (4) reports whether each is separable (fidelity > 0.99) or entangled. Print the separability verdict and fidelity for each."`
- Read / check: |00⟩, |+⟩⊗|0⟩, and (|0⟩+i|1⟩)/√2 ⊗ |+⟩ should all be separable (fidelity=1.0). The Bell state (|00⟩+|11⟩)/√2 should fail (fidelity < 0.01 for any product state ansatz). Verify np.kron produces the correct ordering (row-major: first qubit varies slowest). Use scipy.optimize.minimize with the product-state ansatz parameterized by 4 angles (2 per qubit).
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim (tensor product multiplication animating: two vectors combining into one, separability check appearing as a verdict card with fidelity bar)
- The change: Compute the Schmidt decomposition for the Bell state — show the two Schmidt coefficients are both 1/√2 (maximally entangled), and for a product state they are 1 and 0.
- Teardown angle: The tensor product is the mathematical reason composite quantum systems have exponentially many degrees of freedom. N qubits require 2^N complex amplitudes. This exponential scaling is simultaneously why quantum computers are hard to simulate classically and why they might have computational advantage.
- Exclusions: Partial trace, quantum channel as tensor product, many-body tensor network.
- Score: 8/10

## Candidate 05 — "Solve the Harmonic Oscillator ODE: From Differential Equation to Hermite Polynomials"
- Source: quantum-mechanics-vol5/chapters/03-ordinary-differential-equations.md + quantum-mechanics-vol5/chapters/11-special-functions.md
- Lane: BUILD (Claude Code)
- Hook: The harmonic oscillator wave functions are Hermite polynomials times a Gaussian. Claude Code derives them by solving the ODE numerically and comparing to the analytic formula.
- The artifact: A Manim animation of the first 5 harmonic oscillator wave functions — numeric integration (Runge-Kutta) drawing as dashed lines, analytic Hermite functions appearing as solid lines. The two overlap perfectly, verifying the numeric solution.
- Prompt seed: `claude "Write a Python script that: (1) numerically solves the harmonic oscillator TISE -psi'' + x^2*psi = (2n+1)*psi by shooting from x=-6 to x=6 using scipy.integrate.solve_ivp with Runge-Kutta 45; (2) for n=0,1,2,3,4, choose E=2n+1 and integrate with initial conditions psi(0)=1 (even) or psi'(0)=1 (odd), normalize; (3) compare to analytic H_n(x)*exp(-x^2/2) using scipy.special.hermite; (4) compute and print max absolute difference between numeric and analytic."`
- Read / check: Max absolute difference should be below 0.001 for all n=0–4. n=0 should give a Gaussian. n=1 should give a Gaussian times x (one node at x=0). Wave functions should be zero at boundaries (|x|=6). Verify the analytic function uses the probabilist's Hermite polynomial with the correct normalization.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim (5 wave functions appearing sequentially, numeric (dashed) and analytic (solid) overlapping, node count labeled for each)
- The change: Add the classically forbidden region shading — for each level, shade the region where |x| > sqrt(2n+1) (the classical turning points) and show the evanescent tail of the wave function.
- Teardown angle: The ODE solution is the direct implementation of the Schrödinger equation as a boundary-value problem. The fact that only specific E values (E = 2n+1) give normalizable solutions is not imposed by hand — it emerges from the requirement that psi → 0 at x → ±∞. Quantization is a consequence of boundary conditions, not an axiom.
- Exclusions: Ladder operator derivation, creation/annihilation operators in field theory, anharmonic corrections.
- Score: 8/10

## Candidate 06 — "Estimate Using Dimensional Analysis: Bohr Radius from Scratch with Claude Code"
- Source: quantum-mechanics-vol5/chapters/17-units-dimensions-and-estimation.md
- Lane: BUILD (Claude Code)
- Hook: The Bohr radius a₀ = 0.529 Å can be derived from dimensional analysis alone — no Schrödinger equation required. Claude Code builds the dimensional analysis calculator and extends it to estimate 5 other quantum scales.
- The artifact: A Manim animation of the dimensional analysis computation — fundamental constants appearing (ℏ, m_e, e, 4πε₀), then combining to form a length with the correct units, the Bohr radius value appearing. A table of 5 quantum estimates follows.
- Prompt seed: `claude "Write a Python script that: (1) uses dimensional analysis to estimate the Bohr radius: the only combination of hbar, m_e, e, 4*pi*eps0 with units of length is a0 = (4*pi*eps0*hbar^2)/(m_e*e^2); compute numerically and compare to known 0.529 Angstrom; (2) estimate 5 other quantum scales: de Broglie wavelength (thermal electron, 300K), Compton wavelength, Rydberg energy, fine structure constant (dimensionless), proton radius (from hbar and QCD scale Lambda_QCD~200 MeV). Print each estimate and percent error vs known value."`
- Read / check: Bohr radius: a₀ = 4πε₀ℏ²/(m_e e²) ≈ 0.529 Å. Compton wavelength: λ_C = h/(m_e c) ≈ 2.426 pm. Fine structure constant: α = e²/(4πε₀ℏc) ≈ 1/137. Rydberg energy: E_R = m_e e⁴/(2ℏ²(4πε₀)²) ≈ 13.6 eV. All values should agree with scipy.constants to < 0.01%.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim (dimensional analysis "equation" animating — constants appearing, combining, units balancing, numerical value appearing; then 5-row table of quantum scales appearing one by one)
- The change: Add "order of magnitude" checks — estimate the hydrogen atom size from first principles by minimizing the uncertainty-principle energy E = ℏ²/(2m_e r²) - e²/(4πε₀ r) and show the minimum gives the Bohr radius without any matrix diagonalization.
- Teardown angle: Dimensional analysis is not approximation — it is exact for quantities determined by a unique combination of fundamental constants. The Bohr radius, Compton wavelength, and fine structure constant are all in this class. When dimensional analysis gives the wrong order of magnitude, it means either the physics is wrong or a dimensionless constant of order 1 is hiding.
- Exclusions: Buckingham Pi theorem, renormalization group, natural units vs SI.
- Score: 7/10

## Candidate 07 — "Plot Legendre Polynomials and Angular Momentum: Special Functions with Claude Code"
- Source: quantum-mechanics-vol5/chapters/11-special-functions.md
- Lane: BUILD (Claude Code)
- Hook: The spherical harmonics Y_l^m that appear in every 3D quantum problem are built from Legendre polynomials. Claude Code plots P_l(cos θ) for l=0–4 and shows the orthogonality integral.
- The artifact: A Manim animation of the first 5 Legendre polynomials on the interval [-1, 1] — each curve drawing in sequence, with the orthogonality check ∫P_l·P_l' dθ = 2/(2l+1) δ_ll' displayed as a heat-map matrix.
- Prompt seed: `claude "Write a Python script that: (1) computes Legendre polynomials P_l(x) for l=0,1,2,3,4 on 500 points in [-1,1] using scipy.special.legendre; (2) plots all 5 on one figure with labels; (3) computes the orthogonality matrix O_ij = integral(P_i(x)*P_j(x) dx) from -1 to 1 using scipy.integrate.quad for all i,j pairs; (4) verifies O_ij = 2/(2i+1) * delta_ij; (5) displays O as a heatmap using matplotlib.imshow."`
- Read / check: O_ii should equal 2/(2l+1) for l=0: 2.0, l=1: 0.667, l=2: 0.4, l=3: 0.286, l=4: 0.222. Off-diagonal elements should be < 0.001 (numerical noise). P_0(x)=1 (flat line), P_1(x)=x (linear), P_2(x)=(3x²-1)/2 (parabola). Verify using scipy.special.legendre(n)(x) or scipy.special.eval_legendre.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim (5 Legendre polynomials animating onto the axes one by one; then orthogonality matrix heat map appearing with diagonal highlighted)
- The change: Extend to associated Legendre functions P_l^m(x) for l=2, m=0,1,2 — the building blocks of the spherical harmonics — and plot them in 3D as polar surfaces representing the angular distribution.
- Teardown angle: Orthogonality of Legendre polynomials is not a coincidence — it follows from the Legendre differential equation being a Sturm-Liouville problem. The orthogonality is what makes the series expansion of any function in terms of P_l coefficients unique (no cross-terms).
- Exclusions: Generating function derivation, spherical Bessel functions, quantum defects.
- Score: 7/10
