# Physics: Quantum Mechanics — CLI Video Ideas ("X with Claude")

## Candidate 01 — "Measure Uncertainty with Claude: Does Your Wave Function Saturate Heisenberg?"
- Source: physics-quantum-mechanics/chapters/01-the-wave-function.md (LLM Exercise)
- Lane: BUILD (Claude Code)
- Hook: The uncertainty principle is a bound, not a law of averages — a Gaussian saturates it exactly while most wave functions don't. Which states actually hit the floor?
- The artifact: A bar chart animated left to right showing σ_x · σ_p / (ℏ/2) for six wave functions (Gaussian, infinite-well ground state, infinite-well n=2, triangle wave, step function, random), with a red floor line at 1.0. The Gaussian bar stops exactly at the line; every other bar lands above it.
- Prompt seed: `claude "Write Python that numerically computes sigma_x and sigma_p for six quantum wave functions (Gaussian, infinite-well n=1 and n=2, triangle wave, step function, random noise) on a 1000-point grid. Print sigma_x * sigma_p / (hbar/2) for each and export a CSV. Use scipy and numpy."`
- Read / check: Code: verify the grid integral for normalization reads 1.000; verify Gaussian ratio ≈ 1.000 ± 0.001; verify n=1 infinite well ratio > 1.1. Output: CSV column "ratio" should have exactly one entry ≤ 1.001 (the Gaussian).
- Human supplies: Nothing — fully synthetic. All wave functions are analytic or generated in code. No real hardware or external dataset needed.
- Output medium: Manim — animate a bar chart growing from left to right, red saturation line at 1.0, Gaussian bar stops exactly there with a "SATURATED" label.
- The change: Add the coherent state of the harmonic oscillator (α=2) to the bar chart and show it also saturates — unlike the Fock states which don't.
- Teardown angle: Saturation is rare. The uncertainty principle is almost always a loose bound; the Gaussian and coherent states are the exception that reveals why the math was built around them.
- Exclusions: Proof of Robertson inequality; momentum-space derivation; Fourier duality.
- Score: 9/10

## Candidate 02 — "Build a Quantum Well Slosher with Claude: Watch Energy Quantize"
- Source: physics-quantum-mechanics/chapters/02-the-time-independent-schrodinger-equation.md (LLM Exercise)
- Lane: BUILD (Claude Code)
- Hook: Boundary conditions alone force energy levels to be discrete — there's no "half quantum" allowed. But what does a superposition of those levels actually look like in time?
- The artifact: An animation of |Ψ(x,t)|² for an infinite square well superposition of n=1 and n=2, sloshing back and forth with period T = 2πℏ / (E₂ − E₁). The probability cloud bounces wall-to-wall like a pendulum, then snaps back — a purely quantum oscillation with no classical restoring force.
- Prompt seed: `claude "Write Python that animates |Psi(x,t)|^2 for an infinite square well superposition of n=1 and n=2 with equal coefficients. Grid 500 points, animate 2 full revival periods. Export a frame array as numpy .npy. Use scipy, numpy, matplotlib FuncAnimation."`
- Read / check: Code: verify normalization ∫|Ψ|²dx = 1 at every frame; verify period T = 2πℏ/(E₂−E₁) matches animation. Output: the peak of |Ψ|² should oscillate between left and right halves of the well with the correct period.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim — render the sloshing |Ψ(x,t)|² animation with a time counter and period label; show the energy diagram above.
- The change: Add a third eigenstate (n=3) with a small coefficient and show how the revival period lengthens and the motion loses its clean pendulum shape — a hint of quantum chaos.
- Teardown angle: Quantization is a geometric constraint (boundary conditions), not an imposed rule. The sloshing shows that "stationary" states are only stationary in probability — position isn't.
- Exclusions: Finite well; tunneling from a finite well; analytic derivation of energy levels.
- Score: 9/10

## Candidate 03 — "Simulate WKB Tunneling with Claude: The Log-Linear Geiger-Nuttall Law"
- Source: physics-quantum-mechanics/chapters/11-the-wkb-approximation-and-tunneling.md (LLM Exercise)
- Lane: BUILD (Claude Code)
- Hook: Alpha decay half-lives span 20 orders of magnitude, yet a single formula — the Gamow factor — predicts all of them with a straight line on a log plot. A 40-line script reproduces a century of nuclear physics data.
- The artifact: A log(half-life) vs. 1/√E_α scatter plot for eight real alpha emitters (U-238, Ra-226, Po-212, etc.) with the WKB straight-line fit overlaid. The Geiger-Nuttall law emerges as a visible linear trend across the data points.
- Prompt seed: `claude "Write Python that computes the WKB Gamow factor for alpha decay: gamma = (2/hbar)*integral from r1 to r2 of sqrt(2*m*(V(r)-E)) dr, where V(r) = k*Z1*Z2*e^2/r is the Coulomb barrier. Use scipy.integrate.quad. For 8 real alpha emitters (provide Z, A, Q-value from a table), compute T = exp(-2*gamma) and log10(half-life). Export CSV."`
- Read / check: Code: verify integration converges for each emitter; verify Gamow exponent is in the range 20–80 for physical emitters. Output: log(T₁/₂) vs. 1/√E_α should show R² > 0.97 when a linear fit is applied.
- Human supplies: A table of real alpha emitters (Z, A, Q-value in MeV) — these are available from NNDC or Wikipedia; the human should verify the values before approving. Alternatively, the script can use the 8 emitters cited in Griffiths, which the human confirms from the book table.
- Output medium: Manim — animate the scatter points appearing one by one in order of increasing E_α, then draw the WKB straight line through them; label slope and intercept.
- The change: Overlay the exact quantum-mechanical transmission coefficient T(E) (from a numerical transfer-matrix calculation) on the same plot; show WKB and exact track each other closely.
- Teardown angle: The Gamow factor is an approximation that works better than it has any right to — because the exponential sensitivity amplifies even a crude barrier estimate into a good prediction.
- Exclusions: Full nuclear potential (Woods-Saxon); fission; proton emission.
- Score: 9/10

## Candidate 04 — "Test Bell's Inequality with Claude: Cross the Classical Bound"
- Source: physics-quantum-mechanics/chapters/12-entanglement-and-quantum-information.md (LLM Exercise)
- Lane: BUILD (Claude Code)
- Hook: Quantum mechanics predicts correlations stronger than any classical hidden-variable theory allows. A 30-line Monte Carlo shows you exactly where the boundary is — and how far quantum beats it.
- The artifact: A plot of the CHSH parameter S vs. detector angle θ, sweeping θ from 0° to 90°. A red dashed line at |S|=2 (classical bound), a blue dashed line at 2√2≈2.83 (Tsirelson bound), and the quantum prediction curve S(θ) = 2√2 cos(2θ) crossing the classical bound and peaking at the Tsirelson value.
- Prompt seed: `claude "Write Python that simulates a CHSH Bell test on a singlet state. For angles A1=0, A2=45, B1=22.5, B2=67.5 degrees, compute the quantum expectation E(Ai,Bj) = -cos(Ai-Bj) and the CHSH parameter S = E(A1,B1) + E(A1,B2) + E(A2,B1) - E(A2,B2). Then sweep the angle offset from 0 to 90 degrees and plot S(theta). Mark the classical |S|=2 bound and the Tsirelson 2*sqrt(2) limit."`
- Read / check: Code: verify E(A,B) = −cos(A−B) for the singlet; verify S = 2√2 at the optimal angles. Output: peak of S curve should hit 2√2 ≈ 2.828 ± 0.001; classical bound crossed for a wide range of angles.
- Human supplies: Nothing — fully synthetic (quantum expectation values are analytic).
- Output medium: Manim — animate the S(θ) curve being traced out as θ sweeps, with the classical and Tsirelson bounds appearing as horizontal rules; label where S crosses 2.
- The change: Add a Monte Carlo simulation with N=10,000 measurement samples per angle to show statistical fluctuations around the theoretical curve — and show how many samples you need before the violation is statistically significant (p < 0.01).
- Teardown angle: The violation isn't about "weird particles" — it's about correlation structure. Classical correlations are geometrically constrained; quantum correlations aren't. The math forces it.
- Exclusions: Loophole-free experiments; detector efficiency issues; specific experimental setups (Aspect, Zeilinger).
- Score: 9/10

## Candidate 05 — "Animate a Coherent State with Claude: The Quantum Pendulum That Acts Classical"
- Source: physics-quantum-mechanics/chapters/03-the-harmonic-oscillator.md (LLM Exercise)
- Lane: BUILD (Claude Code)
- Hook: Quantum eigenstates sit still — but coherent states oscillate exactly like a classical pendulum. The wave packet moves without spreading, the expectation value of x traces a cosine, and the Wigner function glides around phase space like a ball on a frictionless surface.
- The artifact: A side-by-side animation — left panel shows |Ψ(x,t)|² for a coherent state (α=3) oscillating back and forth with period 2π/ω; right panel shows the Wigner function W(x,p) as a 2D heat map, a Gaussian disk gliding clockwise around an ellipse in phase space. Both panels run synchronized.
- Prompt seed: `claude "Write Python that computes the time-dependent wave function of a coherent state alpha=3 for the harmonic oscillator. Express Psi(x,t) as a sum of the first 20 Fock states, each with coefficient c_n = exp(-|alpha|^2/2) * alpha^n / sqrt(n!) * exp(-i*E_n*t/hbar). Compute |Psi(x,t)|^2 on 400 grid points and export frame arrays. Use scipy for Hermite polynomials."`
- Read / check: Code: verify |Ψ|² normalization = 1 at every frame; verify ⟨x⟩(t) = 2Re(α)cos(ωt) (classical trajectory). Output: peak of |Ψ|² should trace a clean sinusoid with no spreading visible over 2 periods.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim — side-by-side panels, left |Ψ|² animation, right Wigner function heat map; both synchronized to the oscillation period.
- The change: Switch from coherent state to Fock state n=4 and show the Wigner function developing negative regions (the non-classical signature) while |Ψ|² becomes a double-peaked standing distribution.
- Teardown angle: Coherent states reveal why the quantum and classical worlds are connected — they're the states that make quantum mechanics look classical. Fock states are where the weirdness lives.
- Exclusions: Ladder operator derivation; squeezed states; quantum optics applications.
- Score: 8/10

## Candidate 06 — "Simulate Stern-Gerlach with Claude: Half-Angle Born Rule from Monte Carlo"
- Source: physics-quantum-mechanics/chapters/06-spin.md (LLM Exercise)
- Lane: BUILD (Claude Code)
- Hook: Spin measurement is a gamble with a strange rule — the probability of "spin up" along any axis is cos²(γ/2), where γ is the angle between the spin state and the analyzer. Half the angle, squared. A Monte Carlo makes this visible.
- The artifact: A polar plot showing measured P(+|θ) vs. θ from N=50,000 simulated spin-½ particles, overlaid with the exact cos²(θ/2) prediction curve. The Monte Carlo points lie exactly on the curve across all angles 0°–180°. A second panel shows the sequential Stern-Gerlach result: P(+z after +x) = 0.5, regardless of the first measurement.
- Prompt seed: `claude "Write Python that Monte Carlo simulates spin-1/2 measurements. A particle is prepared in the |+z> state. For each of 180 analyzer angles theta from 0 to 180 degrees, sample N=1000 measurements using P(+) = cos^2(theta/2). Plot the empirical P(+) vs theta and overlay the exact formula. Also simulate sequential SG: first measure along x, then z — show P(+z|+x) = 0.5."`
- Read / check: Code: verify P(+|θ=0) ≈ 1.0 ± 0.01 and P(+|θ=90°) ≈ 0.5 ± 0.02 from Monte Carlo; verify sequential P(+z|+x) ≈ 0.5 ± 0.02. Output: the polar plot should show Monte Carlo points hugging the cos²(θ/2) curve with small scatter.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim — animate the polar plot building up point by point as θ sweeps, then reveal the sequential SG result as a separate panel.
- The change: Show what happens when the analyzer angle is swept continuously from θ=0 to θ=180° — animate the probability smoothly changing, and annotate the "surprise" at θ=90° where P(+)=P(-)=0.5.
- Teardown angle: The half-angle rule is geometrically strange (why cos²(γ/2) and not cos²(γ)?), and the answer — the Bloch sphere geometry — is the key to all of quantum information.
- Exclusions: Spinors and SU(2); relativistic spin; specific experimental apparatus.
- Score: 8/10

## Candidate 07 — "Solve Perturbation Theory with Claude: Stark Effect Energy Shifts"
- Source: physics-quantum-mechanics/chapters/09-time-independent-perturbation-theory.md
- Lane: BUILD (Claude Code)
- Hook: The hydrogen atom in an electric field shifts its energy levels by amounts you can actually measure spectroscopically — and first-order perturbation theory gives you those shifts with a single matrix element.
- The artifact: A bar chart of first-order Stark energy shifts ΔE_n^(1) = ⟨n,l,m|eEz|n,l,m⟩ for hydrogen n=1,2 states, plotted as functions of applied field E. The n=1 ground state shows zero shift (by symmetry); the n=2 degenerate states split into a visible linear Stark pattern.
- Prompt seed: `claude "Write Python that computes first-order Stark effect energy shifts for hydrogen n=1 and n=2 states. Use the fact that <n,l,m|z|n,l,m> = 0 for all states by parity (ground state no shift). For n=2, compute the 4x4 perturbation matrix elements <2,l,m|eEz|2,l',m'> using hydrogen radial wave functions and spherical harmonics from scipy.special. Diagonalize to get the Stark-shifted energies."`
- Read / check: Code: verify n=1 shift = 0 (parity); verify n=2 has exactly two nonzero off-diagonal matrix elements. Output: the four n=2 energy levels should split symmetrically ±3eEa₀ for the two mixed states, with two states remaining unshifted.
- Human supplies: Nothing — fully synthetic (hydrogen wave functions are analytic).
- Output medium: Manim — animate the n=2 energy level diagram splitting as E-field ramps from 0 to E_max; label each level with its quantum numbers.
- The change: Add second-order correction for the n=1 ground state (which has zero first-order shift) and show the quadratic dependence on field strength.
- Teardown angle: Symmetry — parity — determines which matrix elements survive before any calculation. Perturbation theory is as much about knowing what's zero as what's nonzero.
- Exclusions: Zeeman effect; relativistic corrections (fine structure); numerical exact diagonalization.
- Score: 8/10

## Candidate 08 — "Animate Wave Packet Tunneling with Claude: Crank-Nicolson Under the Barrier"
- Source: physics-quantum-mechanics/chapters/11-the-wkb-approximation-and-tunneling.md (LLM Exercise)
- Lane: BUILD (Claude Code)
- Hook: Tunneling is usually a number — the transmission coefficient T. But running the actual Schrödinger equation forward in time shows something stranger: the wave packet partly reflects, partly transmits, and the transmitted piece arrives early — before a classical particle could get through.
- The artifact: A time-lapse animation of |Ψ(x,t)|² as a Gaussian wave packet hits a rectangular potential barrier. The packet splits: reflected wave moving left, transmitted wave emerging on the right side at the correct tunneling speed. A plot of ∫|Ψ|²dx on each side vs. time shows the probability balance.
- Prompt seed: `claude "Implement the Crank-Nicolson method to solve the time-dependent Schrodinger equation for a Gaussian wave packet hitting a rectangular barrier. Grid: 500 points, L=100 bohr. Barrier: width 5 bohr, height V0=2*E_particle centered at x=60. Packet: initial Gaussian centered at x=30, k0 such that E=hbar^2*k0^2/2m=E_particle. Run 2000 time steps. Use the Thomas algorithm for the tridiagonal solve. Export |Psi(x,t)|^2 as a numpy array."`
- Read / check: Code: verify norm ∫|Ψ|²dx = 1 ± 0.001 at every step (Crank-Nicolson is unitary). Output: transmission coefficient T = ∫_{right side}|Ψ|²dx at t→∞ should match the analytic formula T = [1 + (V₀² sinh²(κa))/(4E(V₀-E))]⁻¹ within 2%.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim — animate |Ψ(x,t)|² as a wave packet movie; shade the barrier region; annotate T on screen as it builds up on the right side.
- The change: Vary the barrier height V₀ from 0.5E to 3E and show how T changes on a log scale — confirm the WKB exponential suppression ≈ e^{-2κa} in the thick-barrier limit.
- Teardown angle: The Crank-Nicolson method reveals that the tunneled packet is not "delayed" by the barrier — it emerges at almost the same time as the reflected peak. Tunneling time is one of quantum mechanics' weirdest open questions.
- Exclusions: Hartman effect derivation; resonant tunneling; STM device physics.
- Score: 8/10

## Candidate 09 — "Compute Partition Functions with Claude: From Z to Free Energy in One Differentiation"
- Source: physics-quantum-mechanics/chapters/13-capstone-quantum-mechanics-in-research.md
- Lane: BUILD (Claude Code)
- Hook: The partition function Z = Σ e^{-E_n/kT} is the generating function of all thermodynamics — every observable follows from a single derivative. A two-level system is small enough to do exactly, and the result shows why quantum systems freeze out at low T.
- The artifact: Three plots on one figure: Z(T), ⟨E⟩(T) = -∂ ln Z/∂β, and C_v(T) = ∂⟨E⟩/∂T for a quantum two-level system. The heat capacity shows a Schottky anomaly — a peak at T ≈ ΔE/(2k_B) — that collapses to zero both at high and low T.
- Prompt seed: `claude "Write Python that computes the canonical partition function Z(T), mean energy <E>(T), and heat capacity C_v(T) for a quantum two-level system with energies 0 and Delta_E. Use T from 0.01*Delta_E/kB to 10*Delta_E/kB. Compute all quantities analytically and numerically-via-differentiation and compare. Plot all three on a single figure with labeled axes."`
- Read / check: Code: verify Z(T→∞) → 2 (both states equally likely); verify C_v(T→0) → 0 exponentially; verify Schottky peak at T_peak ≈ ΔE/(2k_B). Output: analytic and numerical derivatives should agree to < 0.1%.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim — animate the three curves being traced from left (low T) to right (high T), with a vertical marker sweeping through the Schottky peak and labeling it.
- The change: Add a 3-level system (energies 0, ΔE, 2ΔE) and show how the heat capacity peak shifts and changes shape — a preview of realistic spin systems.
- Teardown angle: The Schottky anomaly is quantum freezing made visible: at low T the system can't absorb energy because the gap is too big, so C_v → 0 — the quantum signature in a thermodynamic quantity.
- Exclusions: Grand canonical ensemble; Bose/Fermi statistics; density of states for continuous spectra.
- Score: 8/10

## Candidate 10 — "Simulate Lindblad Decoherence with Claude: T1 and T2 on the Bloch Sphere"
- Source: physics-quantum-mechanics/chapters/13-capstone-quantum-mechanics-in-research.md
- Lane: BUILD (Claude Code)
- Hook: Real qubits don't stay in superposition — they decohere. The Lindblad equation tracks exactly how the Bloch vector shrinks toward the mixed state, on two distinct timescales T1 (energy relaxation) and T2 (dephasing).
- The artifact: An animation of a Bloch vector trajectory decohering toward the south pole (|0⟩ → |1⟩ relaxation) under T1=100μs, T2=50μs parameters. The Bloch vector spirals inward and downward, tracing the characteristic T2 < T1/2 spiral. A companion plot shows ρ_01(t) decaying as e^{-t/T2} and ρ_11(t) growing as 1-e^{-t/T1}.
- Prompt seed: `claude "Write Python that integrates the Lindblad master equation for a qubit with T1=100e-6 and T2=50e-6 seconds. Start from |+x> state (Bloch vector pointing at (1,0,0)). Use two Lindblad operators: L1 = sqrt(1/T1) * sigma_minus for amplitude damping, L2 = sqrt(1/(2*T2) - 1/(4*T1)) * sigma_z for pure dephasing. Integrate using scipy.integrate.solve_ivp. Output the Bloch vector (x,y,z) vs time."`
- Read / check: Code: verify Tr[ρ]=1 at all times; verify ρ_01→0 with time constant T2; verify ρ_11→1 with time constant T1. Output: Bloch vector should satisfy |r|≤1 at all times; z component should saturate at -1 (ground state) at t>>T1.
- Human supplies: Nothing — fully synthetic (Lindblad parameters are given as inputs).
- Output medium: Manim — 3D Bloch sphere with the Bloch vector trajectory animated as a decaying spiral; a transparent sphere shows the unit constraint.
- The change: Set T2 > T1/2 (forbidden by physics) and show that the Bloch vector exits the unit sphere — demonstrating why T2 ≤ 2T1 is a fundamental constraint, not just an empirical observation.
- Teardown angle: T1 and T2 are the design knobs of every quantum computer — making T2 approach 2T1 (the coherence limit) is the engineering challenge the field has been chasing since 2000.
- Exclusions: Lindblad derivation from Born-Markov; specific qubit platforms; quantum error correction.
- Score: 8/10

## Candidate 11 — "Build a Bloch Sphere Simulator with Claude: Robertson Bound from 1000 Samples"
- Source: physics-quantum-mechanics/chapters/04-formalism-dirac-notation-and-operators.md (LLM Exercise)
- Lane: BUILD (Claude Code)
- Hook: The Robertson uncertainty bound ΔA · ΔB ≥ ½|⟨[A,B]⟩| looks abstract until you measure it — 1000 independent samples of σ_x and σ_z on a |+y⟩ state produce exactly σ_x = σ_z = 1, while ½|⟨[σ_x,σ_z]⟩| = |⟨σ_y⟩| = 1. The bound saturates.
- The artifact: A scatter plot of (Δσ_x, Δσ_z) computed from batches of N=1000 measurements at 50 different spin states (uniformly sampled from the Bloch sphere). The Robertson bound ΔA·ΔB ≥ ½|⟨[A,B]⟩| = |⟨σ_y⟩| appears as a hyperbolic boundary — all 50 points lie on or above it, with the |+y⟩ state on the boundary.
- Prompt seed: `claude "Write Python that Monte Carlo verifies the Robertson bound for spin-1/2. For 50 randomly chosen Bloch sphere states (theta, phi), compute: (1) theoretical Delta_sigma_x and Delta_sigma_z from the density matrix, (2) simulated Delta_sigma_x and Delta_sigma_z from N=1000 measurements each, (3) the Robertson lower bound |<sigma_y>|. Plot Delta_sigma_x * Delta_sigma_z vs |<sigma_y>| for all 50 states."`
- Read / check: Code: verify for |+y⟩: ΔσxΔσz = 1 and |⟨σy⟩| = 1 (saturated); verify for |+z⟩: ΔσxΔσz ≈ 1 and |⟨σy⟩| = 0 (bound not tight). Output: all points should lie on or above the diagonal ΔA·ΔB = lower bound in the scatter plot.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim — animate the 50 data points appearing one by one on the scatter plot, then reveal the Robertson hyperbola; highlight the saturating states on the Bloch sphere.
- The change: Repeat for the pair (σ_x, σ_y) where the bound depends on ⟨σ_z⟩ — show how the bound tightens as the state approaches the equator and vanishes for the poles (eigenstates of σ_z).
- Teardown angle: The Robertson bound makes the uncertainty principle precise: it tells you which pairs of observables are incompatible and exactly how incompatible they are, depending on the state.
- Exclusions: Schrödinger uncertainty relation; non-Hermitian operators; continuous-variable uncertainty.
- Score: 7/10

## Candidate 12 — "Compute Probability Current with Claude: Where Does the Quantum Flux Go?"
- Source: physics-quantum-mechanics/chapters/01-the-wave-function.md
- Lane: BUILD (Claude Code)
- Hook: Probability doesn't just sit at a point — it flows. The probability current J = (ℏ/2mi)(Ψ*∇Ψ − Ψ∇Ψ*) is a real quantity you can plot, and for a plane wave it flows in one direction at a constant rate. For a superposition, it produces interference fringes in the current density.
- The artifact: A two-panel animation — left panel shows Re(Ψ(x,t)) oscillating; right panel shows J(x,t) the probability current. For a free Gaussian wave packet, J is everywhere positive (current flowing right). When a reflected wave is added, J develops regions of negative flux (backflow) near the interference nodes.
- Prompt seed: `claude "Write Python that computes the probability current J(x,t) = hbar/(2mi) * (Psi*.dPsi/dx - Psi.dPsi*/dx) for (1) a free Gaussian wave packet moving right, and (2) a superposition of the wave packet and a reflected version. Use numpy.gradient for the spatial derivative. Animate both on side-by-side panels. Verify continuity equation: dJ/dx + d|Psi|^2/dt = 0 at each frame."`
- Read / check: Code: verify continuity equation residual < 1e-4 at each grid point each frame. Output: for free packet, J should be everywhere positive; for superposition, J should have negative regions near interference zeros.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim — two-panel synchronized animation with colored flux arrows in the current panel.
- The change: Plot the integrated current ∫J dx as a function of time for the free packet and show it equals the group velocity — connecting J to the classical momentum.
- Teardown angle: Probability current resolves the "where does the particle go?" question for quantum systems without requiring a classical trajectory — it's the field version of momentum.
- Exclusions: 3D probability current; continuity equation in electromagnetism analogy; relativistic probability current (Dirac equation).
- Score: 7/10
