# Quantum Mechanics Vol. 4 — CLI Video Ideas ("X with Claude")

## Candidate 01 — "Simulate CHSH Violation: Build the Bell Test Experiment with Claude Code"
- Source: quantum-mechanics-vol4/chapters/03-bells-theorem-and-chsh.md
- Lane: BUILD (Claude Code)
- Hook: Bell's theorem is one page of algebra — but simulating the experiment makes the violation tangible. Claude Code runs 10,000 virtual measurements on the singlet state and shows |S| > 2 emerges from the statistics.
- The artifact: A Manim animation of a simulated Bell test — 10,000 measurement pairs appearing as a growing scatter plot, with the CHSH parameter S accumulating in a corner readout, converging toward -2√2. The LHV bound (S=2) appears as a red line the accumulation crosses.
- Prompt seed: `claude "Write a Python script that simulates a Bell test on the singlet state |psi> = (|01> - |10>)/sqrt(2): (1) generate N=10000 measurement pairs with Alice choosing a1=0 or a2=pi/2 (50/50) and Bob choosing b1=pi/4 or b2=-pi/4 (50/50); (2) for each pair, sample the quantum correlations E(theta_a - theta_b) = -cos(theta_ab) to get +/-1 outcomes; (3) compute S = E(a1,b1) + E(a1,b2) + E(a2,b1) - E(a2,b2) from the sample averages; (4) plot S vs number of trials showing convergence to -2*sqrt(2)."`
- Read / check: Final S should converge to -2√2 ≈ -2.828 within ±0.05 for N=10,000. The LHV bound |S|≤2 should be visibly crossed early and maintain the violation throughout. Verify the sampling uses quantum probabilities: P(+,+ | theta_a, theta_b) = (1 - cos(theta_ab))/4 for the singlet. All four correlation functions should print.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim (S vs N line chart converging toward -2√2, LHV bound at S=-2 as red dashed line, quantum bound at S=-2√2 as blue dashed line, final value labeled)
- The change: Implement a local hidden-variable simulation (assigning pre-determined ±1 values to each detector angle) and show that S never exceeds 2 — making the classical limit concrete alongside the quantum violation.
- Teardown angle: The simulation does not prove Bell's theorem — the math proves it. The simulation makes the statistical convergence visceral: with 10,000 trials, the violation is 20 standard deviations away from the LHV bound. The 2022 Nobel Prize closed the remaining experimental loopholes.
- Exclusions: Loophole taxonomy, photon pair generation, CHSH vs. CH inequality.
- Score: 9/10

## Candidate 02 — "Build a Quantum Circuit Simulator: Bell State Preparation with Claude Code"
- Source: quantum-mechanics-vol4/chapters/04-quantum-gates-and-circuits.md
- Lane: BUILD (Claude Code)
- Hook: A Hadamard gate plus a CNOT gate creates a Bell state from |00⟩. Claude Code builds a 2-qubit simulator from scratch in 25 lines and verifies the entanglement.
- The artifact: A Manim animation of the quantum circuit — two wires entering (|0⟩, |0⟩), the H gate appearing on wire 1, the CNOT gate appearing with a bullet on wire 1 and ⊕ on wire 2, then the output state (|00⟩ + |11⟩)/√2 appearing with its density matrix visualization showing the off-diagonal entanglement.
- Prompt seed: `claude "Write a Python script implementing a 2-qubit quantum circuit simulator using numpy: (1) represent qubit states as 4-element complex vectors in the {|00>,|01>,|10>,|11>} basis; (2) implement gates: H = Hadamard on qubit 0, CNOT with control=0 target=1; (3) apply H then CNOT to initial state |00> = [1,0,0,0]; (4) verify the output is (|00>+|11>)/sqrt(2); (5) compute and print the density matrix rho = psi @ psi.conj().T; (6) verify entanglement: Tr(rho_A^2) < 1 where rho_A = partial_trace(rho, B)."`
- Read / check: Output state should be [1/√2, 0, 0, 1/√2]. Density matrix should have nonzero off-diagonal elements rho[0,3] = rho[3,0] = 0.5. Partial trace rho_A should be I/2 (maximally mixed — Tr(rho_A²) = 0.5 < 1). Verify the H gate is [[1,1],[1,-1]]/√2 and CNOT is the correct 4×4 matrix with bit ordering.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim (animated circuit diagram — gates appearing on wires, state vector evolving step by step, density matrix heat map appearing with off-diagonal elements highlighted)
- The change: Add a measurement in the Z basis — show the state collapsing to either |00⟩ or |11⟩ with equal probability, and simulate 1000 measurements to verify the 50/50 distribution.
- Teardown angle: The 4×4 CNOT matrix and the 2×2 Hadamard implement all of quantum computing's key primitives. The density matrix with Tr(ρ_A²) = 0.5 is the algebraic definition of maximal entanglement. Building the simulator from first principles makes the math tangible.
- Exclusions: Toffoli gate, quantum error correction circuits, variational quantum eigensolver.
- Score: 9/10

## Candidate 03 — "Simulate Quantum Teleportation: Step-by-Step Protocol with Claude Code"
- Source: quantum-mechanics-vol4/chapters/05-quantum-teleportation-and-dense-coding.md
- Lane: BUILD (Claude Code)
- Hook: Quantum teleportation does not send matter — it sends quantum information using a Bell state and 2 classical bits. Claude Code implements the protocol in 15 lines and verifies the teleported state.
- The artifact: A Manim animation of the teleportation protocol — Alice holding qubits 1 and 2 (shared Bell pair), Bob holding qubit 3. Alice's Bell measurement result (2 classical bits) appears in a speech bubble, Bob applies the correct correction gate, and the final state is shown matching the original.
- Prompt seed: `claude "Write a Python script that simulates quantum teleportation: (1) Alice wants to teleport state |phi> = alpha|0> + beta|1> with alpha=0.6, beta=0.8i; (2) prepare Bell state: qubits 2,3 in (|00>+|11>)/sqrt(2); (3) 3-qubit system state = |phi>_1 x Bell_{23}; (4) Alice applies CNOT(1,2) then H(1) to her two qubits; (5) Alice measures qubits 1,2 — 4 possible outcomes; (6) Bob applies correction (I, X, Z, XZ) based on Alice's result; (7) verify Bob's qubit 3 is in state |phi> for all 4 measurement outcomes."`
- Read / check: For all 4 measurement outcomes (00, 01, 10, 11), after Bob's correction gate, qubit 3's state should match |φ⟩ = 0.6|0⟩ + 0.8i|1⟩ with fidelity = 1.0. Verify the total state is a 3-qubit vector (8 elements). Verify |α|²+|β|² = 1 is preserved. Print the teleported state amplitude for each measurement outcome.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim (animated circuit: Alice's gates applying, Bell measurement collapsing, classical bits traveling to Bob, correction gate applying, final state matching original)
- The change: Show that teleportation without the 2 classical bits is impossible — if Bob guesses the correction gate randomly, his fidelity averages to 0.5.
- Teardown angle: Teleportation is not faster-than-light because Alice must send 2 classical bits to Bob before the state is recovered. The quantum resource (the Bell pair) enables the protocol; the classical channel provides the classical information that makes it work.
- Exclusions: Photon-pair sources for teleportation, long-distance teleportation, quantum repeaters.
- Score: 9/10

## Candidate 04 — "Model Qubit Decoherence: T1 and T2 with the Lindblad Equation"
- Source: quantum-mechanics-vol4/chapters/06-open-systems-and-lindblad.md
- Lane: BUILD (Claude Code)
- Hook: A superconducting qubit's Bloch vector spirals inward as T1 (energy relaxation) and T2 (dephasing) act. Claude Code integrates the Bloch equations and shows why T2 ≤ 2T1.
- The artifact: A Manim animation of the Bloch sphere with the Bloch vector starting on the equator and spiraling inward toward the south pole under combined T1 and T2 relaxation — three panels showing pure precession (T1=T2=∞), pure dephasing (T1=∞, T2=100 ns), and combined (T1=50 μs, T2=30 μs).
- Prompt seed: `claude "Write a Python script that integrates the Bloch equations for a qubit with T1=50e-6 s (energy relaxation) and T2=30e-6 s (dephasing): dr_x/dt = -r_x/T2 - omega_0*r_y; dr_y/dt = omega_0*r_x - r_y/T2; dr_z/dt = -(r_z + 1)/T1. Use omega_0=2*pi*5e9 rad/s (5 GHz transmon), initial state r=(1,0,0) (equatorial). Integrate with scipy.integrate.solve_ivp. Plot the Bloch vector trajectory in 3D (x,y,z vs time)."`
- Read / check: |r(t)| should decay from 1.0 to 0. At t=T2=30 μs, the transverse components r_x, r_y should be reduced to 1/e of initial. At t=T1=50 μs, r_z should approach -1 (ground state) at rate 1/T1. Verify T2 ≤ 2T1 (30 μs ≤ 100 μs — satisfied). Print r(t) at t=0, T2, 2*T2, T1.
- Human supplies: Nothing — fully synthetic. Parameters from Google Sycamore transmon qubits (publicly reported).
- Output medium: Manim (3D Bloch sphere with spiral trajectory, three-panel comparison of the three decoherence regimes, T1 and T2 labels with arrow to the trajectory)
- The change: Compute the purity Tr(ρ²) = (1+|r|²)/2 as a function of time and show it decaying from 1 (pure) toward 0.5 (maximally mixed).
- Teardown angle: T2 ≤ 2T1 is not a law of physics — it is a mathematical consequence of the Lindblad equation structure. Physical T2 is often much shorter than 2T1 because dephasing can occur without energy exchange. The constraint is tight in superconducting qubits with pure Hamiltonians and well-isolated qubits.
- Exclusions: Ramsey spectroscopy, spin-echo pulse sequences, non-Markovian effects.
- Score: 8/10

## Candidate 05 — "Research Quantum Error Correction: The Surface Code Threshold with Claude"
- Source: quantum-mechanics-vol4/chapters/09-error-and-the-threshold-theorem.md
- Lane: BUILD (Claude Code)
- Hook: The threshold theorem says: if physical error rate p < p_th ≈ 1%, logical error rate p_L drops exponentially with code distance d. Claude Code computes and plots p_L vs d for the surface code.
- The artifact: A Manim animation of logical error rate vs code distance for three physical error rates — p=0.5% (below threshold), p=1% (at threshold), p=2% (above). Below threshold: p_L falls as d grows. Above threshold: p_L rises. The threshold appears as the crossover point.
- Prompt seed: `claude "Write a Python script that models surface code logical error rate using the approximate threshold scaling: p_L(d) = A * (p/p_th)^((d+1)/2) where p_th=0.01 (1% threshold), A=0.1. Plot p_L vs code distance d=3,5,7,9,11,13 for three physical error rates: p=0.005 (below threshold), p=0.01 (at threshold), p=0.02 (above threshold). Verify: below threshold, p_L decreases with d; above threshold, p_L increases. Mark Google's reported p_L=0.00143 at d=7 as a data point."`
- Read / check: Below-threshold curve should be monotonically decreasing. Above-threshold curve should be monotonically increasing. At-threshold curve should be approximately flat. Google's d=7 data point (p_L=0.143% per cycle ≈ 0.00143) should lie on or near the below-threshold curve. Verify formula gives p_L(d=3, p=0.005) ≈ 0.1*(0.5)^2 = 0.025.
- Human supplies: Nothing — fully synthetic. Google 2023 Nature paper data point is publicly reported in the abstract.
- Output medium: Manim (three curves — below/at/above threshold — drawing simultaneously, crossover point labeled as "threshold p_th=1%", Google data point appearing as a star)
- The change: Plot the "quantum advantage" threshold — how many logical qubits at what code distance are needed to run Shor's algorithm for RSA-2048, and how many physical qubits that requires (millions).
- Teardown angle: The threshold theorem is not a proof that fault-tolerant quantum computers are easy to build — it is a proof that they are possible in principle. The distance between "in principle" and "in practice" is the current $1B+ investment in qubit coherence improvement.
- Exclusions: Full concatenated code analysis, magic state distillation, specific hardware implementations.
- Score: 8/10

## Candidate 06 — "Compute Dense Coding: How 2 Classical Bits Fit in 1 Qubit with Claude Code"
- Source: quantum-mechanics-vol4/chapters/05-quantum-teleportation-and-dense-coding.md
- Lane: BUILD (Claude Code)
- Hook: Dense coding sends 2 classical bits using 1 qubit plus 1 shared ebit (pre-entangled qubit pair). Claude Code implements all 4 Bell state preparations and shows the 2-bit capacity.
- The artifact: A Manim animation of the dense coding protocol — Alice holds one qubit of a Bell pair, applies one of {I, X, iY, Z} to encode 2 bits, sends the qubit to Bob. Bob's Bell measurement reads out the 2-bit message. The four protocol options animate as a 2×2 table.
- Prompt seed: `claude "Write a Python script simulating superdense coding: (1) prepare Bell state (|00>+|11>)/sqrt(2) as initial shared resource; (2) Alice applies one of {I, X, iY, Z} to her qubit (qubit 0) to encode messages {00, 01, 10, 11}; (3) Alice sends her qubit to Bob; (4) Bob applies CNOT(0,1) then H(0); (5) Bob measures both qubits and reads the 2-bit message. Verify all 4 encodings decode correctly. Print the decoded message for each gate."`
- Read / check: Applying I → message 00, X → 01, iY → 10, Z → 11. After Bob's decoding circuit, the 4-element state vector should have amplitude 1 at exactly the basis state corresponding to the message. Verify Bob's circuit correctly decodes all 4: CNOT then H on qubit 0 reverses the Bell state preparation.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim (2×2 table of 4 protocols animating one by one, Alice's gate highlighted, Bob's measurement result appearing, all 4 showing correct decoding)
- The change: Show why superdense coding requires the entangled pair — without the Bell pair, Alice can only send 1 classical bit per qubit (Holevo's theorem). State but do not derive the theorem.
- Teardown angle: Dense coding is the dual of teleportation — teleportation uses 2 classical bits + 1 ebit to send 1 qubit; dense coding uses 1 qubit + 1 ebit to send 2 classical bits. The same Bell pair is the quantum resource in both protocols.
- Exclusions: Holevo bound derivation, quantum channel capacity, quantum key distribution.
- Score: 7/10
