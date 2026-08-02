# Quantum Mechanics Vol. 1 — CLI Video Ideas ("X with Claude")

## Candidate 01 — "Build a 1D Quantum Sandbox: Eigenstates and Time Evolution with Claude Code" (Capstone)
- Source: quantum-mechanics-vol1/chapters/11-capstone-a-1d-quantum-sandbox.md
- Lane: BUILD (Claude Code)
- Hook: The capstone asks you to build a configurable 1D Schrödinger solver. This card does it: Claude Code writes the matrix eigensolver, verifies against the infinite square well, then time-evolves a wave packet through a barrier.
- The artifact: A Manim animation showing two modes: (1) eigenstate mode — four energy levels appearing as horizontal lines above the potential well, with wave functions drawn offset; (2) time-evolution mode — a Gaussian wave packet propagating, spreading, and partially reflecting from a step potential.
- Prompt seed: `claude "Build a 1D quantum mechanics solver in Python: (1) construct the tridiagonal Hamiltonian H on N=500 grid points in [0, L] nm for infinite-square-well boundary conditions; (2) diagonalize with scipy.linalg.eigh to get the first 4 eigenstates; (3) verify E_n = n^2*pi^2*hbar^2/(2*m*L^2) by printing fractional errors; (4) time-evolve an initial Gaussian wave packet psi(x,0) for 200 steps using the Crank-Nicolson method; (5) animate |psi(x,t)|^2 with a normalization indicator."`
- Read / check: Eigenvalue fractional errors should be below 0.01% for n=1–4, N=500. Normalization should remain within 0.1% throughout time evolution (Crank-Nicolson is unitary). Wave packet centroid should translate at v_g = hbar*k0/m. Verify the tridiagonal matrix uses the correct -hbar^2/(2m*h^2) off-diagonal entries.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim (dual-mode animation: eigenstate panel showing energy levels + wave functions; time-evolution panel showing |ψ|² spreading with normalization readout)
- The change: Swap the potential to a finite square well (V=0 inside, V=5 eV outside) and show how the wave functions now have evanescent tails penetrating the classically forbidden region.
- Teardown angle: The central-difference discretization introduces O(h²) errors in eigenvalues. The benchmark against the infinite square well is the discipline that separates a simulation from "numerical theater" — the chapter's phrase.
- Exclusions: Numerov shooting method, 2D or 3D solvers, complex absorbing boundaries.
- Score: 9/10

## Candidate 02 — "Wave Packet Spreading: Group vs. Phase Velocity with Claude Code"
- Source: quantum-mechanics-vol1/chapters/08-the-free-particle-and-wave-packets.md
- Lane: BUILD (Claude Code)
- Hook: The wave packet's blob moves at v_g, but the ripples inside move at v_p = v_g/2. That ratio of exactly 2 is the de Broglie dispersion relation made visible.
- The artifact: A Manim animation of a free-particle Gaussian wave packet — Re(ψ) in orange, |ψ|² in blue (filled) — with two arrows: one tracking the blob centroid (labeled v_g = ℏk₀/m) and one tracking a wave crest inside the blob (labeled v_p = ℏk₀/2m). Both arrows move at their respective speeds.
- Prompt seed: `claude "Write a Python script that analytically time-evolves a free-particle Gaussian wave packet psi(x,t) = integral of phi(k)*exp(i*(k*x - omega(k)*t)) dk where omega(k) = hbar*k^2/(2*m) and phi(k) is a Gaussian in k-space centered at k0=10/nm. Compute the closed-form result: centroid at x_0 + hbar*k0*t/m, width sigma(t) = sqrt(a^2/2 + hbar^2*t^2/(2*m^2*a^2)) for a=1nm. Animate Re(psi), Im(psi), and |psi|^2 using matplotlib.animation for 200 time steps."`
- Read / check: Centroid should move at v_g = hbar*k0/m ≈ 1.16e6 m/s (electron, k0=10/nm). Width should double at t = sqrt(3)*m*a^2/hbar ≈ 15 fs. Verify phase crests visible inside the blob move at v_p = v_g/2. Normalization should be preserved analytically.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim (animated wave packet with centroid arrow and phase velocity arrow moving at different speeds, width σ(t) readout updating each frame)
- The change: Set k₀=0 (no mean momentum) and show the packet spreading without translating — demonstrating that spreading is position uncertainty growth, not motion.
- Teardown angle: The group velocity carries the classical momentum; the phase velocity carries the wave's phase — and is not directly measurable. The ratio v_g/v_p = 2 is a signature of the quadratic dispersion relation and disappears for massless photons (linear dispersion).
- Exclusions: Wigner function, coherent states, wave packets in 3D.
- Score: 9/10

## Candidate 03 — "Reproduce the Uncertainty Principle: σ_x σ_p ≥ ℏ/2 Numerically with Claude Code"
- Source: quantum-mechanics-vol1/chapters/09-operators-and-uncertainty.md
- Lane: BUILD (Claude Code)
- Hook: The uncertainty principle is not a statement about measurement disturbance — it is a mathematical theorem about Fourier pairs. Claude Code can verify it numerically for any wave function and find the Gaussian that saturates it.
- The artifact: A Manim animation with two panels — position space (|ψ|² in blue) and momentum space (|φ(k)|² in orange) — with σ_x and σ_p computed numerically and displayed, and the product σ_x σ_p shown against the bound ℏ/2. The Gaussian case shows the product exactly equaling ℏ/2.
- Prompt seed: `claude "Write a Python script that: (1) constructs 4 wave functions — Gaussian (a=1nm), infinite-well ground state (L=4nm), double-Gaussian (d=1.5nm, sigma=0.4nm), and a top-hat function; (2) computes sigma_x = sqrt(<x^2> - <x>^2) and sigma_p = sqrt(<p^2> - <p>^2) for each using numerical integration and numpy FFT for momentum-space representation; (3) prints sigma_x * sigma_p / (hbar/2) for each. The Gaussian should give approximately 0.5 (i.e., the product = hbar/2)."`
- Read / check: Gaussian result should give σ_x*σ_p/(ℏ/2) ≈ 1.0 (saturates the bound). All four results should be ≥ 1.0. Infinite-well ground state should give ≈ 1.14 (Griffiths problem 1.7). Top-hat should give > 2 (not minimal uncertainty). Verify the momentum-space wave function uses the correct FFT normalization (multiply by dx, divide by 2π).
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim (two-panel animation: position and momentum distributions side by side, σ_x and σ_p values updating, product/bound ratio displayed prominently)
- The change: Sweep Gaussian width a from 0.1 nm to 5 nm and plot σ_x*σ_p as a function of a — showing it is constant (= ℏ/2) regardless of width, confirming the Gaussian minimizes the uncertainty product.
- Teardown angle: The Robertson inequality is a property of the state and the pair of observables, not of the measurement apparatus. Heisenberg's original 1927 argument was about measurement disturbance — Robertson 1929 gave the preparation uncertainty version. They are not the same claim.
- Exclusions: Ozawa's noise-disturbance uncertainty, measurement error vs. preparation uncertainty, time-energy uncertainty.
- Score: 9/10

## Candidate 04 — "Simulate the Harmonic Oscillator: Ladder Operators and Energy Levels with Claude Code"
- Source: quantum-mechanics-vol1/chapters/07-the-harmonic-oscillator.md
- Lane: BUILD (Claude Code)
- Hook: The harmonic oscillator energy levels are ℏω(n+½). The ground state has zero-point energy ½ℏω that can never be removed. Claude Code builds the ladder operator matrix and generates all 6 levels in 10 lines.
- The artifact: A Manim animation of the first 6 harmonic oscillator wave functions — each appearing as a colored curve offset above the potential parabola at its energy level. The ladder operator action â₊|n⟩ → |n+1⟩ is shown as an arrow stepping up.
- Prompt seed: `claude "Write a Python script that: (1) numerically solves the quantum harmonic oscillator (omega=1e14 rad/s, electron mass) using matrix diagonalization on N=400 grid points; (2) plots the first 6 eigenfunctions psi_n(x) offset vertically by their energies E_n = hbar*omega*(n+0.5); (3) overlays the parabolic potential V(x) = 0.5*m*omega^2*x^2; (4) verifies E_n numerically and prints fractional errors vs. analytic."`
- Read / check: E_0 = ℏω/2 (zero-point energy). Levels should be equally spaced by ℏω. Wave functions should have n nodes for the nth state (0 nodes for ground). Verify the wave function for n=0 matches the Gaussian exp(-x²/(2x₀²)) where x₀ = sqrt(ℏ/mω) to within numerical error.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim (wave functions appearing one by one, rising up the energy ladder, potential parabola in red, ladder arrow animating between levels)
- The change: Displace the initial state from x=0 by 2x₀ (a coherent state) and time-evolve — showing the wave packet oscillating like a classical particle without spreading.
- Teardown angle: The harmonic oscillator is the most reused mechanism in physics — every phonon, every photon mode, every small oscillation near a stable equilibrium is a harmonic oscillator. The ladder operator is the algebraic shortcut that makes all of these tractable.
- Exclusions: Coherent state derivation, squeezed states, phonon crystal modes.
- Score: 8/10

## Candidate 05 — "Visualize the Qubit on the Bloch Sphere with Claude Code"
- Source: quantum-mechanics-vol1/chapters/10-measurement-and-the-qubit.md
- Lane: BUILD (Claude Code)
- Hook: Any single-qubit state |ψ⟩ = cos(θ/2)|0⟩ + e^{iφ}sin(θ/2)|1⟩ lives on a sphere. A measurement in the Z basis collapses it to a pole. Claude Code builds the interactive Bloch sphere in 20 lines.
- The artifact: A Manim animation of the Bloch sphere — a 3D sphere (orthographic projection) with the Bloch vector pointing at various states as θ and φ vary. Key states labeled: |0⟩ (north pole), |1⟩ (south pole), |+⟩ (equator), |−⟩ (equator). The collapse animation shows the vector snapping to a pole after measurement.
- Prompt seed: `claude "Write a Python script using matplotlib's 3D plotting to render the Bloch sphere. Plot the unit sphere as a wireframe. Add labeled points for |0>, |1>, |+> = (|0>+|1>)/sqrt(2), |-> = (|0>-|1>)/sqrt(2), |i> = (|0>+i|1>)/sqrt(2). For each state, compute the Bloch vector (r_x, r_y, r_z) = (<sigma_x>, <sigma_y>, <sigma_z>) using the state amplitudes. Draw arrows from the origin to each Bloch vector. Print the coordinates."`
- Read / check: |0⟩ → (0,0,1) (north pole). |1⟩ → (0,0,-1) (south pole). |+⟩ → (1,0,0). |−⟩ → (-1,0,0). |i⟩ → (0,1,0). All vectors should have unit length. Verify r_x = 2*Re(alpha*beta*), r_y = 2*Im(alpha*beta*), r_z = |alpha|^2 - |beta|^2.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim (rotating Bloch sphere, labeled states appearing one by one, Bloch vector arrows animating outward from origin to each state)
- The change: Animate a Z-basis measurement — show the Bloch vector at an arbitrary angle, then snap it to north or south pole with probability |cos(θ/2)|² and |sin(θ/2)|² displayed.
- Teardown angle: The Bloch sphere is only exact for single qubits — it fails for mixed states (vectors inside the sphere) and for multi-qubit systems (no simple geometric analog). The visualization is powerful and limited in the same way the qubit formalism is.
- Exclusions: Density matrix representation, quantum gates as rotations, multi-qubit register.
- Score: 8/10

## Candidate 06 — "Verify the Born Rule: Build the Probability Current with Claude Code"
- Source: quantum-mechanics-vol1/chapters/03-the-wave-function.md
- Lane: BUILD (Claude Code)
- Hook: The Born rule says |ψ|² is probability density. The probability current J = (ℏ/m)Im(ψ*∂ψ/∂x) shows how that density flows. If the simulation drifts from unit normalization, J tells you where probability is leaking.
- The artifact: A Manim animation of a wave packet propagating right, with two panels: top shows |ψ|² (blue filled), bottom shows J(x,t) (the probability current — positive when probability flows right, negative when reflected). The normalization indicator appears in the corner.
- Prompt seed: `claude "Write a Python script that time-evolves a free-particle Gaussian wave packet psi(x,t) numerically using the Crank-Nicolson method (N=500 grid points, dt=0.01 fs, electron, k0=10/nm). At each step: (1) compute normalization integral = sum(|psi|^2)*dx; (2) compute probability current J = (hbar/m)*Im(conj(psi)*d(psi)/dx) using central differences; (3) verify the continuity equation d|psi|^2/dt + dJ/dx = 0 numerically; (4) animate both |psi|^2 and J simultaneously."`
- Read / check: Normalization should remain within 0.01% throughout (Crank-Nicolson is unitary). J should be positive where the wave packet is moving right. The continuity equation residual should be below numerical noise. Verify d(psi)/dx uses central differences: (psi[i+1]-psi[i-1])/(2*dx).
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim (two-panel animation: |ψ|² top, probability current J bottom, normalization readout in corner)
- The change: Add a step potential (V=0 for x<0, V=0.5 eV for x>0) and watch J split — partial transmission (J>0 on right) and partial reflection (J<0 on left near the step).
- Teardown angle: The continuity equation d|ψ|²/dt + ∇·J = 0 is why the Schrödinger equation preserves probability. It is the quantum analog of charge conservation. If the simulation violates it, the numerical method is wrong.
- Exclusions: Scattering matrix S, reflection/transmission coefficients derivation, optical theorem.
- Score: 7/10
