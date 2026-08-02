# Quantum Mechanics with LLMs — CLI Video Ideas ("X with Claude")

## Candidate 01 — "Build the Free-Particle Wave Packet Simulation with Claude" (LLM Exercise)
- Source: quantum-mechanics-with-llms/chapters/00-introduction.md   (LLM Exercise — Ch00 simulation)
- Lane: BUILD (Claude Code)
- Hook: The book's first assignment: watch a Gaussian wave packet spread in real time before any derivation. Claude builds the D3.js animation from a four-sentence prompt. The blob drifts at v_g, the ripples inside slip at v_g/2.
- The artifact: A screen-recording mp4 of the browser showing `00-wave-packet.html` — the blue |ψ|² blob drifting right at group velocity, orange Re(ψ) ripples sliding backward through it at phase velocity. A slider changes σ; the packet spreads faster when narrower.
- Prompt seed: `claude "Build a single self-contained HTML file 00-wave-packet.html using D3.js v7 from CDN: animate a free-particle Gaussian wave packet psi(x,t) with group velocity v_g = hbar*k0/m and width sigma(t) = sqrt(a^2/2 + hbar^2*t^2/(2*m^2*a^2)). Show |psi|^2 (blue filled), Re(psi) (orange solid), Im(psi) (gray dashed). Add sliders for k0 and initial width a. Display normalization integral in corner (red if |1 - integral| > 0.01). SVG only, no canvas, no external files."`
- Read / check: Normalization indicator should stay within 1% throughout. Group velocity arrow (if added) should move at v_g = hbar*k0/m. Setting k0=0 should produce a non-translating spreading packet. The orange crests inside the blob should visibly move slower than the blob center (v_p = v_g/2). Verify the HTML file opens without a build step.
- Human supplies: A screen-recording of the simulation running in a browser — Chrome or Firefox. QuickTime or OBS. No simulation code can be synthetic for a screen-recording card.
- Output medium: screen-recording mp4 (browser full-screen, slider being dragged, blob spreading and translating, normalization indicator visible in corner)
- The change: Add a fourth panel showing |φ(k)|² (the momentum-space distribution) — which should remain constant for a free particle, demonstrating momentum conservation while position spreads.
- Teardown angle: The ratio v_g/v_p = 2 is specific to the quadratic dispersion relation E=p²/2m of non-relativistic quantum mechanics. For a photon (E=pc, linear dispersion), v_g = v_p = c. The simulation makes the dispersion relation visible without writing the word "dispersion."
- Exclusions: Schrödinger equation derivation, de Broglie hypothesis, relativistic corrections.
- Score: 9/10

## Candidate 02 — "Build the Born Rule Explorer: Normalize and Measure with Claude" (LLM Exercise)
- Source: quantum-mechanics-with-llms/chapters/01-the-wave-function.md   (LLM Exercise)
- Lane: BUILD (Claude Code)
- Hook: The Born rule says |ψ|² is probability density — but density is not probability. You must integrate. Claude builds an interactive probability explorer: drag a region boundary and watch the probability update.
- The artifact: A screen-recording mp4 of `01-probability-explorer.html` — a wave function displayed with a shaded region [a,b] that the user drags. The probability P(a,b) = ∫|ψ|²dx updates in real time. σ_x and σ_p are displayed for several built-in wave functions.
- Prompt seed: `claude "Build 01-probability-explorer.html in D3.js v7: (1) display |psi|^2 for a Gaussian wave function psi(x) = (1/(pi*a^2))^0.25 * exp(-x^2/(2*a^2)), normalized, on [-10,10] nm; (2) add two draggable vertical lines marking [a,b] region; (3) shade the region and display P(a,b) = integral_a^b |psi|^2 dx using the trapezoidal rule in real time; (4) add a wave function gallery dropdown (Gaussian, infinite-well n=1, infinite-well n=2, double-Gaussian); (5) display sigma_x for each."`
- Read / check: Normalization indicator should show integral = 1.000 for all wave functions. Dragging [a,b] to cover the full range should give P → 1.0. For the Gaussian, P(-a, a) should give 0.683 (one standard deviation). Verify the probability is computed by numerical integration (not analytic). The gallery dropdown should switch wave functions without breaking normalization.
- Human supplies: A screen-recording of the browser with all four wave functions demonstrated and the region drag demonstrated.
- Output medium: screen-recording mp4 (browser with draggable region, four wave functions cycling, probability readout updating in real time)
- The change: Add a "measurement" button that samples a random position from |ψ|² (using inverse CDF sampling) and marks it as a dot — run 100 measurements and show the histogram converging to |ψ|².
- Teardown angle: The Born rule is easy to state but subtle to believe: ψ itself is not observable; only |ψ|² appears in measurement statistics. The explorer makes the density-vs-probability distinction tangible — a high |ψ|² peak is not "the particle is here" but "measurements cluster here."
- Exclusions: Collapse postulate, many-worlds interpretation, quantum field theory.
- Score: 9/10

## Candidate 03 — "Build the Stern-Gerlach Simulator: Bloch Sphere and Spin Measurement" (LLM Exercise)
- Source: quantum-mechanics-with-llms/chapters/06-spin.md   (LLM Exercise)
- Lane: BUILD (Claude Code)
- Hook: The chapter's LLM Exercise builds `06-stern-gerlach.html` — an interactive three-panel simulation: drag a state on the Bloch sphere, drag the analyzer axis, watch the beam split. Claude builds it from the four-move prompt.
- The artifact: A screen-recording mp4 of `06-stern-gerlach.html` — left panel: Bloch sphere with draggable state vector; center panel: the analyzer axis with draggable orientation; right panel: the two output beams with probability bars showing cos²(γ/2) and sin²(γ/2). Toggling magnetic field shows Larmor precession.
- Prompt seed: `claude "Build 06-stern-gerlach.html in D3.js v7: three panels. Left: Bloch sphere (orthographic projection, 2D) with a draggable Bloch vector (theta, phi). Center: analyzer axis (draggable angle gamma from z-axis). Right: two output beams with animated split showing P_up = cos^2(gamma/2) and P_down = sin^2(gamma/2) as growing bars. Add a magnetic field toggle: when on, animate Larmor precession omega_0 = gamma_proton * B (B=1T slider). Single HTML file, D3 v7 CDN, SVG only."`
- Read / check: Probabilities should sum to 1.0 for all Bloch vector positions and analyzer orientations. At γ=0 (analyzer parallel to state): P_up=1, P_down=0. At γ=π/2: P_up=P_down=0.5. At γ=π: P_up=0, P_down=1. Larmor precession should rotate the Bloch vector about z at the correct frequency. Normalization indicator should remain 1.000 throughout.
- Human supplies: A screen-recording showing: (1) dragging the Bloch vector; (2) dragging the analyzer angle; (3) demonstrating the probability bars; (4) toggling the B field and showing precession.
- Output medium: screen-recording mp4 (three-panel browser, all four demonstrations above)
- The change: Add a second sequential Stern-Gerlach apparatus — show that if you measure in the z-basis then the x-basis, the z-information is destroyed (sequential measurements don't commute).
- Teardown angle: The cos²(γ/2) rule is the Born rule for spin-1/2 — the projection of the Bloch vector onto the measurement axis gives the expectation value, and the probability is a function of the half-angle because spin-1/2 has a 4π symmetry (rotation by 2π gives -|ψ⟩, not |ψ⟩).
- Exclusions: Spin-1 and higher, Stern-Gerlach actual experimental apparatus, spin-orbit coupling.
- Score: 9/10

## Candidate 04 — "Build the Quantum Research Paper Reader: NV-Center Magnetometer with Claude" (LLM Exercise)
- Source: quantum-mechanics-with-llms/chapters/13-capstone-quantum-mechanics-in-research.md   (LLM Exercise)
- Lane: BUILD (Claude Code)
- Hook: The capstone's research-direction explorer builds a simulation showing the Bloch vector spiraling inward under T1/T2 decoherence — Tab 1 of a three-tab research tool. This is the deliverable.
- The artifact: A screen-recording mp4 of `13-decoherence-simulator.html` — Tab 1: Bloch sphere with spiraling trajectory under T1/T2 sliders; Tab 2: surface code threshold — logical vs. physical error rate curves; Tab 3: NV-center ODMR spectrum with B-field slider showing Zeeman splitting. All three interactive.
- Prompt seed: `claude "Build 13-decoherence-simulator.html in D3.js v7 with 3 tabs. Tab 1: Bloch sphere (500x500 SVG orthographic projection) showing Bloch vector trajectory under T1 and T2 sliders (range 1–1000 μs). Integrate Bloch equations numerically (Euler method, 500 steps). Tab 2: surface code threshold — plot p_L vs code distance d=3,5,7,9,11 for p=0.005, 0.01, 0.02. Tab 3: NV-center ODMR — plot microwave absorption vs frequency for B=0 to 100 mT (B slider), showing Zeeman-split dips at f = D_gs ± gamma_NV*B where D_gs=2.87 GHz, gamma_NV=28 GHz/T. SVG only, single file, D3 v7 CDN."`
- Read / check: Tab 1: Bloch vector magnitude decays from 1 toward 0. T2≤2T1 should be enforced (or warned). Tab 2: below-threshold curve (p=0.5%) should be monotonically decreasing. Tab 3: at B=0, single dip at 2.87 GHz; at B>0, two dips at 2.87 ± 28e9*B Hz — verify the splitting is linear in B. Normalization indicator on Tab 1.
- Human supplies: A screen-recording showing all three tabs demonstrated with slider interactions.
- Output medium: screen-recording mp4 (all three tabs shown, each slider demonstrated)
- The change: Add a "purity" readout to Tab 1: Tr(ρ²) = (1+|r|²)/2, showing it decays from 1.0 (pure) toward 0.5 (maximally mixed) as the Bloch vector shrinks.
- Teardown angle: The three-tab design encodes the three research doorways of the capstone — open systems (Tab 1), quantum error correction (Tab 2), quantum sensing (Tab 3). The decoherence simulator is why they're all connected: T1 and T2 limit every quantum technology, from error correction to sensing.
- Exclusions: Hamiltonian engineering, dynamical decoupling, quantum metrology limits.
- Score: 9/10

## Candidate 05 — "Build the Quantum Harmonic Oscillator: Ladder Operators Animated" (LLM Exercise)
- Source: quantum-mechanics-with-llms/chapters/03-the-harmonic-oscillator.md
- Lane: BUILD (Claude Code)
- Hook: The ladder operators â₊ and â₋ step between energy levels of the harmonic oscillator. Claude builds the interactive HTML simulation showing all six levels and the probability density updating as you click up and down the ladder.
- The artifact: A screen-recording mp4 of `03-harmonic-oscillator.html` — left panel: the harmonic potential V(x) = ½mω²x² in red, the 6 energy levels as horizontal lines, the current wave function |ψ_n|² in blue. Right panel: +/- ladder buttons that step n up or down, animating the wave function change.
- Prompt seed: `claude "Build 03-harmonic-oscillator.html in D3.js v7: (1) plot harmonic potential V(x) = x^2 in red and the first 6 energy levels E_n = 2n+1 as green horizontal lines (dimensionless units); (2) display the wave function psi_n(x) = H_n(x)*exp(-x^2/2) (Hermite polynomials evaluated numerically as sum_k from recurrence relation, not from library) normalized, in blue filled; (3) up/down buttons to step n from 0 to 5; (4) animate the transition smoothly (500ms interpolation); (5) display n and E_n in the corner. SVG only, single file."`
- Read / check: n=0: Gaussian (0 nodes). n=1: one node at x=0. n=2: two nodes. n=5: five nodes. Energy levels equally spaced by 2 units (in dimensionless units). Wave functions should be zero at boundaries. Normalization indicator should show 1.000 for all n. Verify Hermite recurrence: H_0=1, H_1=2x, H_{n+1}=2x*H_n - 2n*H_{n-1}.
- Human supplies: A screen-recording showing the ladder being climbed from n=0 to n=5 and back, with normalization indicator visible throughout.
- Output medium: screen-recording mp4 (browser panel, ladder buttons pressed, wave function animating between levels, node count updating)
- The change: Add a "superposition" mode — click to select two levels and show the time-dependent superposition |ψ⟩ = (|n⟩ + |m⟩)/√2 oscillating between the two wave functions at the beat frequency (E_n - E_m)/ℏ.
- Teardown angle: The ladder operator connection â₊|n⟩ = √(n+1)|n+1⟩ is what makes the harmonic oscillator algebraically solvable — you don't need to solve a differential equation. The animation makes the "rungs" of the ladder physical: each click changes the node count by 1 and the energy by ℏω.
- Exclusions: Coherent states, squeezed states, harmonic oscillator in 3D (vibrations in molecules).
- Score: 8/10

## Candidate 06 — "Build the Entanglement Visualizer: Bell States and Schmidt Decomposition" (LLM Exercise)
- Source: quantum-mechanics-with-llms/chapters/12-entanglement-and-quantum-information.md
- Lane: BUILD (Claude Code)
- Hook: The four Bell states are the maximally entangled states of two qubits. Claude builds a visual simulator showing which states are entangled and displaying the Schmidt coefficients as the measure of entanglement.
- The artifact: A screen-recording mp4 of `12-entanglement.html` — a 2×2 density matrix visualization for user-selected two-qubit states, with Schmidt decomposition displayed and entanglement entropy S computed and shown as a bar.
- Prompt seed: `claude "Build 12-entanglement.html in D3.js v7: (1) dropdown to select from 6 two-qubit states: |00>, |01>, |+>|0>, Bell state Phi+=(|00>+|11>)/sqrt(2), Phi-=(|00>-|11>)/sqrt(2), and a partially entangled state (cos(theta)|00>+sin(theta)|11>) with a theta slider; (2) display the 4x4 density matrix rho = psi psi* as a heatmap (real and imaginary parts); (3) compute reduced density matrix rho_A by partial trace; (4) compute von Neumann entanglement entropy S = -Tr(rho_A log2 rho_A); (5) display S as a bar (0=separable, 1=maximally entangled). SVG only, D3 v7 CDN."`
- Read / check: |00⟩: S=0 (separable). Bell state Φ+: S=1 (maximally entangled). Partially entangled (θ=π/4): S=1; (θ=0): S=0; (θ=π/8): S between 0 and 1. Density matrix heatmap should show off-diagonal elements for entangled states. Partial trace should be a 2×2 matrix. Verify partial trace: rho_A[i,j] = sum_k rho[ik, jk] (trace over second qubit).
- Human supplies: A screen-recording showing all 6 states demonstrated, with the theta slider varying the entanglement entropy from 0 to 1.
- Output medium: screen-recording mp4 (browser with dropdown, density matrix heatmap updating, entanglement entropy bar animating)
- The change: Add the CHSH parameter S_CHSH computed from the density matrix — show that states with S=1 (maximally entangled) give |S_CHSH| = 2√2, while separable states give |S_CHSH| ≤ 2.
- Teardown angle: Entanglement entropy is the measure of entanglement for pure states — it is zero for product states and log₂(d) for maximally entangled states in d dimensions. The density matrix's off-diagonal elements are the fingerprint of entanglement; the Schmidt decomposition makes it quantitative.
- Exclusions: Mixed state entanglement, entanglement distillation, monogamy of entanglement.
- Score: 8/10

## Candidate 07 — "Build the Perturbation Theory Explorer: Energy Level Splitting Animated" (LLM Exercise)
- Source: quantum-mechanics-with-llms/chapters/09-time-independent-perturbation-theory.md
- Lane: BUILD (Claude Code)
- Hook: First-order perturbation theory says the energy shift is E'_n = ⟨n|H'|n⟩. Claude builds an interactive simulation where you dial a perturbation strength and watch the energy levels split.
- The artifact: A screen-recording mp4 of `09-perturbation.html` — left panel: infinite square well with a perturbation (bump in the middle) whose height is adjustable with a slider. Right panel: the first 4 energy levels drawn as horizontal lines, shifting as the slider moves — first-order shifts computed analytically and shown alongside numeric diagonalization.
- Prompt seed: `claude "Build 09-perturbation.html in D3.js v7: (1) infinite square well L=1 (dimensionless) with perturbation H' = lambda * bump(x) where bump(x) = 1 if |x-0.5| < 0.1, else 0; (2) lambda slider from 0 to 2; (3) left panel: plot V(x) + lambda*bump(x); (4) compute first-order energy corrections E'_n = lambda * (2/L)*integral(sin^2(n*pi*x/L)*bump(x)dx) = lambda * 0.2 (for n=1 — bump at antinode) analytically; (5) right panel: animate energy levels E_n + E'_n as horizontal lines moving as lambda changes; (6) overlay exact numeric diagonalization (tridiagonal matrix) for comparison."`
- Read / check: At λ=0: all levels at E_n = n²π². At λ=2: first-order shifts should be 0.2*λ for odd n (bump at antinode), 0 for even n (bump at node). Analytic and numeric should agree to within 5% for small λ. Verify the bump integrates correctly: ∫₀.₄^₀.₆ sin²(nπx)dx = 0.1 - sin(0.4nπ)cos(0.6nπ)/(nπ) approximately 0.1 for n=1.
- Human supplies: A screen-recording showing the slider being dragged from λ=0 to λ=2, energy levels visibly shifting, analytic and numeric comparison shown.
- Output medium: screen-recording mp4 (browser with slider, energy levels animating, comparison between perturbation theory and exact shown as two colored sets of lines)
- The change: Move the bump from x=0.5 (antinode of n=1) to x=0.25 (node of n=2) — show that the n=2 level is now unaffected at first order while n=1 shifts.
- Teardown angle: First-order perturbation theory is "sandwich the perturbation in the unperturbed eigenstate" — the shift depends entirely on whether the perturbation overlaps with the wave function density at that location. The bump-at-node/antinode comparison makes this geometric interpretation visible.
- Exclusions: Degenerate perturbation theory, second-order corrections, time-dependent perturbation theory.
- Score: 7/10
