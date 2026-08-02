# Simulation Ideas — quantum-mechanics-vol4

Medhavy-register "Claude Code + Manim" workflow reels.

---

## Sim-01 — CHSH Inequality: −cos θ Curve Beats the Classical Bound
- Source: `quantum-mechanics-vol4/chapters/03-bells-theorem-and-chsh.md`
- Topic: CLAUDE CODE · MANIM
- Physical rule: CHSH score S = −cos(θ_AB) − cos(θ_AB') − cos(θ_A'B) + cos(θ_A'B'); max classical = 2; quantum max = 2√2 ≈ 2.828
- Concrete numbers: optimal angles θ = 0°, 45°, 90°, 135°; S_QM = 2√2 = 2.828; S_classical ≤ 2; gap = 0.828
- Visual artifact: −cos(θ) correlation curve sweeping over angle; horizontal lines at S=2 (classical) and S=2√2 (quantum); highlight region that violates Bell
- Two testable predictions: P1: S = 2.000 exactly at classical-mimicking angles (0°/90°/0°/90°); P2: S = 2√2 at optimal quantum angles (measurable to 4 decimal places in experiment)
- Sim slug: medhavy-vol4-chsh-curve
- Status: BUILT
- Watch: `open /Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-vol4/youtube/medhavy-vol4-chsh-curve/medhavy-vol4-chsh-curve-review.mp4`
- Note: CROSS-REFERENCE — vox-chsh-ceiling is an explainer in quantum-mechanics-a-companion-guide. This simulation workflow reel (Claude Code plotting the correlation curve) is new; build it.

---

## Sim-02 — Bloch Decoherence: T₂ Decay of the Off-Diagonal
- Source: `quantum-mechanics-vol4/chapters/06-open-systems-and-lindblad.md`
- Topic: CLAUDE CODE · MANIM
- Physical rule: ρ₀₁(t) = ρ₀₁(0) · e^(−t/T₂); Bloch vector component in x-y plane decays exponentially with time T₂
- Concrete numbers: T₂ = 1 μs (typical NMR); at t=T₂, |ρ₀₁| has fallen to 1/e ≈ 0.368 of initial; at t=3T₂ → 0.050
- Visual artifact: Bloch sphere with the equatorial component spiraling inward exponentially while the z-component stays (if pure dephasing, T₁ → ∞)
- Two testable predictions: P1: |ρ₀₁(T₂)| / |ρ₀₁(0)| = 1/e = 0.3679 exactly; P2: doubling γ_dephasing halves T₂ (T₂ = 1/γ)
- Sim slug: medhavy-vol4-decoherence-t2
- Status: BUILT
- Watch: `open /Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-vol4/youtube/medhavy-vol4-decoherence-t2/medhavy-vol4-decoherence-t2-review.mp4`

---

## Sim-03 — Quantum Gates: Hadamard and Phase on the Bloch Sphere
- Source: `quantum-mechanics-vol4/chapters/04-quantum-gates-and-circuits.md`
- Topic: CLAUDE CODE · MANIM
- Physical rule: H = (X+Z)/√2 maps |0⟩→|+⟩ (rotation by π about x+z axis); S gate adds phase e^(iπ/2) to |1⟩ (rotation by π/2 about z)
- Concrete numbers: |0⟩ at north pole; H → |+⟩ at equator (φ=0); then S → |i⟩ = (|0⟩+i|1⟩)/√2 at equator (φ=π/2); position shifts 90° on Bloch sphere
- Visual artifact: Bloch sphere; vector animates from north pole to equator (H gate) then rotates 90° in-plane (S gate); label each gate
- Two testable predictions: P1: H∘H = I (applying Hadamard twice returns to |0⟩); P2: S gate maps |+⟩=(|0⟩+|1⟩)/√2 to |i⟩=(|0⟩+i|1⟩)/√2 (equatorial 90° rotation)
- Sim slug: medhavy-vol4-gate-bloch
- Status: BUILT
- Watch: `open /Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-vol4/youtube/medhavy-vol4-gate-bloch/medhavy-vol4-gate-bloch-review.mp4`

---

## Candidate 01 — Animate the Surface Code Threshold: Logical vs. Physical Error Rate
- Source: `quantum-mechanics-vol4/chapters/09-error-and-the-threshold-theorem.md`
- Topic: Surface code threshold — when bigger codes get better, not worse
- Lane: MANIM (directed animation)
- Hook: Below a magic error rate of 1%, every extra layer of redundancy makes the computer more reliable — above it, more redundancy makes things worse. A single number separates "quantum computing is possible" from "it is not."
- The rule: p_L ≈ A·(p/p_th)^⌈(d+1)/2⌉ with p_th ≈ 0.01, A = 0.1; three curves d=3,5,7 fanning apart below threshold and converging above it; the crossing point is the threshold
- Concrete numbers: p_th = 0.01 (1%); A = 0.1; d=3 exponent=2, d=5 exponent=3, d=7 exponent=4; at p=0.002 (below threshold): p_L(d=3)≈4×10⁻⁴, p_L(d=7)≈1.6×10⁻⁶ — a 250× improvement; at p=0.02 (above threshold): all curves > 0.1 and larger d is worse
- The artifact / what moves: three log-log curves animate in simultaneously, meet at a single crossing point (the threshold), then fan apart — below the crossing d=7 is lowest, above it d=7 is highest; a vertical "threshold" line sweeps in and locks at 1%
- Output medium: Manim (mp4)
- Two testable predictions: P1: all three curves intersect at p=p_th where p_L=A=0.1 exactly; P2: the suppression factor Λ=p_L(d)/p_L(d+2) equals p_th/p — at p=0.002 Λ=5, verified from the formula
- The change: sweep physical error rate p from 0.005 to 0.02 as a slider annotation, showing the fan flip as p crosses p_th
- Human supplies (Claude can't): Nothing — fully synthetic/analytic
- Teardown angle: The threshold is not a property of the hardware alone — it depends on code architecture, decoder quality, and syndrome extraction fidelity; Willow's Λ=2.14 implies p_eff≈0.0047, pluggable directly into the formula
- Exclusions: Magic state distillation, decoding algorithms, concatenated codes
- Sim slug: vol4-surface-code-threshold
- Score: 10/10

---

## Candidate 02 — Entanglement Entropy vs. Schmidt Angle: The Ebit Curve
- Source: `quantum-mechanics-vol4/chapters/02-composite-systems-and-entanglement.md`
- Topic: How entanglement grows from zero to one ebit as a two-qubit state tilts from product to Bell
- Lane: D3/DATAVIZ (emergent / interactive)
- Hook: There is exactly one number — the Schmidt angle θ — that controls how entangled two qubits are. Turn it from 0 to π/4 and you watch a product state become a Bell state. The entropy curve has a shape that surprises everyone: it is not linear, it is concave, and it saturates abruptly.
- The rule: S_E(θ) = −cos²θ·log₂(cos²θ) − sin²θ·log₂(sin²θ) for state cos θ|00⟩ + sin θ|11⟩; Schmidt coefficients λ₁=cos²θ, λ₂=sin²θ; purity Tr(ρ_A²) = ½(1+cos²(2θ))
- Concrete numbers: θ=0: S_E=0, purity=1 (product); θ=π/6 (30°): S_E=−(3/4)log₂(3/4)−(1/4)log₂(1/4)≈0.811 ebits, purity=5/8; θ=π/4 (45°): S_E=1 ebit, purity=1/2 (Bell state, maximally mixed subsystem)
- The artifact / what moves: slider on θ from 0 to π/4; live curve tracing S_E(θ) as point moves along it; side panel shows Bloch ball shrinking (subsystem purity decreasing) as θ increases; coefficient matrix C shown updating
- Output medium: d3 v7 animated/interactive HTML
- Two testable predictions: P1: S_E=0 at θ=0 and S_E=1 at θ=π/4 (boundary values exact); P2: at θ=π/6 S_E≈0.811 ebits — matches formula and the partially-entangled worked example in Ch. 2
- The change: add a second slider for Schmidt coefficient asymmetry (generalize to λ₁=α², λ₂=1−α²); show entropy collapses to 0 whenever α→0 or α→1
- Human supplies (Claude can't): Nothing — fully synthetic/analytic
- Teardown angle: The subsystem purity and the entanglement entropy encode the same information differently — neither tells you about the individual qubit; all the physics lives in the joint correlations
- Exclusions: Mixed-state entanglement measures, entanglement distillation rates, multipartite entanglement
- Sim slug: vol4-entanglement-entropy-slider
- Score: 9/10
- Status: BUILT — `open /Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-vol4/youtube/vol4-entanglement-entropy-slider/vol4-entanglement-entropy-slider.html`

---

## Candidate 03 — Bloch Equations: T₁ and T₂ Decay Regimes on One Sphere
- Source: `quantum-mechanics-vol4/chapters/06-open-systems-and-lindblad.md`
- Topic: How a qubit's Bloch vector dies — two time constants, three regimes, one surprise
- Lane: MANIM (directed animation)
- Hook: Most people think "decoherence" means "the qubit collapses to the ground state." Wrong. Pure dephasing leaves the qubit equally likely to be |0⟩ or |1⟩ forever — it just erases the phase. The two processes leave the Bloch vector in completely different places.
- The rule: ṙ_x = −ω₀r_y − r_x/T₂; ṙ_y = +ω₀r_x − r_y/T₂; ṙ_z = −(r_z+1)/T₁; with 1/T₂ = 1/(2T₁) + 1/T_φ; solution: r_x(t)=e^(−t/T₂)cos(ω₀t), r_y(t)=e^(−t/T₂)sin(ω₀t), r_z(t)=−1+(1+r_z(0))e^(−t/T₁)
- Concrete numbers: T₁=4μs, T_φ=4μs → T₂=2μs; initial state on equator (r_x=1); at t=T₂: |r_xy|=1/e≈0.368; T₂=2T₁ limit: T_φ→∞, r_xy decays at exactly half the longitudinal rate; pure dephasing (T₁→∞): r_z stays fixed at initial value, r_xy→0, endpoint NOT south pole
- The artifact / what moves: Bloch sphere with animated spiral trajectory — three labeled segments: (1) pure dephasing: equatorial spiral inward to z-axis, endpoint on z-axis; (2) pure T₁ decay: vertical arc to south pole; (3) combined: diagonal spiral to south pole; side panels show ρ matrix element magnitudes decaying
- Output medium: Manim (mp4)
- Two testable predictions: P1: At t=T₂, |ρ₀₁(t)|/|ρ₀₁(0)|=1/e=0.3679 exactly; P2: T₂≤2T₁ always — equality only when T_φ→∞ (no pure dephasing)
- The change: vary T_φ/T₁ ratio from 0 (all dephasing) to ∞ (no dephasing); watch endpoint sweep from z-axis to south pole
- Human supplies (Claude can't): Nothing — fully synthetic/analytic
- Teardown angle: The natural linewidth limit T₂=2T₁ is a hard ceiling — every real qubit falls below it because pure dephasing always adds to energy relaxation; the gap tells you how much room is left to improve through noise engineering
- Exclusions: Non-Markovian decay, dynamical decoupling, Gaussian bath crossover
- Sim slug: vol4-bloch-t1-t2-regimes
- Score: 9/10

---

## Candidate 04 — CHSH Angle Explorer: Why 45° Spacing Wins
- Source: `quantum-mechanics-vol4/chapters/03-bells-theorem-and-chsh.md`   (+ "LLM Exercise" from exercise 3)
- Topic: The quantum correlation landscape — why the optimal Bell angles are 45° apart, not 90°
- Lane: D3/DATAVIZ (emergent / interactive)
- Hook: The CHSH violation is not magic — it is geometry. Drag Alice's and Bob's measurement axes and watch S climb toward 2√2 only when the angles are equally spaced at 45°. At 90° spacing you get S=2, indistinguishable from classical.
- The rule: E(θ_a, θ_b) = cos(θ_a − θ_b) for |Φ+⟩; S = E(A₁,B₁)+E(A₁,B₂)+E(A₂,B₁)−E(A₂,B₂); classical bound S≤2; Tsirelson bound S≤2√2
- Concrete numbers: optimal (0°,90°,45°,−45°): S=2√2=2.828; all-same angles (0°,0°,0°,0°): S=2 exactly (classical mimicry); exercise-3 angles (0°,60°,30°,90°): S=√3≈1.732 (no violation at all); Tsirelson maximum 2√2 unreachable with any other configuration
- The artifact / what moves: four draggable angle pointers on a polar dial; live S readout updating as angles move; color bands: red S<2, yellow 2≤S<2√2, green S=2√2; a "violation region" highlights when S>2
- Output medium: d3 v7 animated/interactive HTML
- Two testable predictions: P1: S=2 exactly when all four angles are equal (regardless of the common angle); P2: S=2√2 achieved only when angles are evenly spaced at 45° intervals (e.g. 0°,45°,90°,135° in the right assignment)
- The change: switch the underlying quantum state from |Φ+⟩ to |Ψ−⟩ (singlet); watch all correlations flip sign but |S|_max remain 2√2
- Human supplies (Claude can't): Nothing — fully synthetic/analytic
- Teardown angle: The violation requires all four correlations to cooperate — a single strong correlation is easily explained classically; the 41% gap above S=2 is what no local model can reproduce
- Exclusions: Tsirelson bound proof, PR boxes, information causality
- Sim slug: vol4-chsh-angle-explorer
- Score: 9/10
- Status: BUILT — `open /Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-vol4/youtube/vol4-chsh-angle-explorer/vol4-chsh-angle-explorer.html`

---

## Candidate 05 — Quantum Teleportation Protocol: State Flow Animated
- Source: `quantum-mechanics-vol4/chapters/05-quantum-teleportation-and-dense-coding.md`
- Topic: Quantum teleportation — why two classical bits move one qubit
- Lane: MANIM (directed animation)
- Hook: Alice destroys a qubit to send it. No quantum channel, no faster-than-light signal — just a Bell pair and a phone call. Without the two classical bits, Bob's qubit is maximally mixed: perfectly random, zero information.
- The rule: Three-qubit evolution: |ψ⟩_S ⊗ |Φ+⟩_AB → (CNOT_SA)(H_S) → sum over four equiprobable branches → Alice measures (SA), sends 2 cbits → Bob applies I/X/Z/ZX; ρ_B = Tr_SA(|Ψ₂⟩⟨Ψ₂|) = I/2 before classical bits arrive
- Concrete numbers: |ψ⟩=α|0⟩+β|1⟩ arbitrary; each of 4 outcomes has probability 1/4; Bob's state before classical bits: Bloch vector = (0,0,0) regardless of α,β; after correction: fidelity=1 exactly for perfect Bell pair
- The artifact / what moves: three-wire circuit animates gate-by-gate; state labels update at each step; after Alice's measurement, Bob's Bloch ball shown at center (maximally mixed); then classical bits "travel" as arrows → Bob's Bloch vector jumps to the correct surface point; original |ψ⟩ shown as a destroyed/consumed qubit on Alice's wire
- Output medium: Manim (mp4)
- Two testable predictions: P1: ρ_B = I/2 exactly before the classical bits arrive (any α,β — no information leaks); P2: all four correction gates (I,X,Z,ZX) restore |ψ⟩ exactly — verified by the correction table in the worked example
- The change: replace perfect |Φ+⟩ with Werner state ρ=(1−ε)|Φ+⟩⟨Φ+|+ε(I/4); show teleportation fidelity F=(1+S/2√2)/2 degrading from 1 as ε increases
- Human supplies (Claude can't): Nothing — fully synthetic/analytic
- Teardown angle: No-cloning is not violated because Alice's qubit is destroyed in the measurement — the protocol consumes the original; the two classical bits are essential, not ceremonial
- Exclusions: Continuous-variable teleportation, entanglement swapping, quantum repeaters
- Sim slug: vol4-teleportation-animated
- Score: 9/10

---

## Candidate 06 — Purity vs. Bloch Radius: The Bloch Ball Interior
- Source: `quantum-mechanics-vol4/chapters/01-mixed-states-and-the-density-matrix.md`
- Topic: What mixedness looks like geometrically — purity as a ball, not a sphere
- Lane: D3/DATAVIZ (emergent / interactive)
- Hook: Pure quantum states live on the surface of a sphere. Mixed states live inside it. Decoherence is not a collapse — it is a shrinkage. Drag the Bloch vector inward and watch the density matrix lose its quantum character, one element at a time.
- The rule: ρ = ½(I + r·σ), |r|≤1; purity Tr(ρ²) = ½(1+|r|²); off-diagonal |ρ₀₁| = |r_xy|/2 where r_xy=√(r_x²+r_y²); S_entropy = −½(1+|r|)log₂½(1+|r|) − ½(1−|r|)log₂½(1−|r|) (von Neumann entropy)
- Concrete numbers: |r|=1 (surface): purity=1, |ρ₀₁|=|r_xy|/2, von Neumann entropy=0; |r|=0 (center): purity=0.5, |ρ₀₁|=0, entropy=1 bit; lab example ρ=(3/4,1/4;1/4,1/4): |r|=√(1/4+(1/2)²)=√(1/2)≈0.707, purity=3/4
- The artifact / what moves: cross-section of Bloch ball with draggable point; as point moves inward, density matrix heatmap updates in real-time (off-diagonals fade), purity bar shrinks, von Neumann entropy bar grows; marker for maximally mixed state at center
- Output medium: d3 v7 animated/interactive HTML
- Two testable predictions: P1: Tr(ρ²)=½(1+|r|²) — at |r|=0 gives 0.5 (minimum for qubit), at |r|=1 gives 1.0; P2: off-diagonal |ρ₀₁|=0 at center, |ρ₀₁|=1/2 at equator of surface (|r|=1, r_z=0)
- The change: add a "mixture decomposition" overlay showing two surface points that average to the current interior point — demonstrating that the same density matrix has infinitely many ensemble decompositions (non-uniqueness from Ch. 1 Fig. 1.3)
- Human supplies (Claude can't): Nothing — fully synthetic/analytic
- Teardown angle: The Bloch ball makes explicit what "classically mixed" vs. "quantum superposition" means geometrically — a diagonal ρ sits on the z-axis interior, while a coherent superposition sits on the surface
- Exclusions: Higher-dimensional state spaces, qutrit geometry, GHZ state visualization
- Sim slug: vol4-bloch-ball-purity
- Score: 9/10
- Status: BUILT — `open /Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-vol4/youtube/vol4-bloch-ball-purity/vol4-bloch-ball-purity.html`

---

## Candidate 07 — Bell State Preparation: H + CNOT, Step by Step
- Source: `quantum-mechanics-vol4/chapters/04-quantum-gates-and-circuits.md`   (+ "LLM Exercise" from exercise 3/6)
- Topic: How two gates create maximal entanglement — the circuit that runs every quantum protocol
- Lane: MANIM (directed animation)
- Hook: One gate (Hadamard) creates a superposition but no entanglement. The next gate (CNOT) creates entanglement but no superposition on its own. Together, in one step, both qubits become maximally mixed individually while perfectly correlated jointly. The Bloch vectors both collapse to the origin.
- The rule: |00⟩ →(H⊗I)→ |+⟩|0⟩ →CNOT→ |Φ+⟩=(|00⟩+|11⟩)/√2; det(C) goes from 0 (product, after H) to 1/2 (entangled, after CNOT); ρ_A = ρ_B = I/2 after CNOT
- Concrete numbers: After H: C = (1/√2)(1,0;1,0), det=0, both Bloch vectors: A at +x equator, B at north pole; after CNOT: C=(1/√2)(1,0;0,1), det=1/2, both Bloch vectors at origin; all four initial states |00⟩,|01⟩,|10⟩,|11⟩ → four distinct Bell states
- The artifact / what moves: two-wire circuit with Bloch spheres shown live above each wire; step 1: H animates qubit A from north pole to +x equator (product state preserved); step 2: CNOT fires and both Bloch vectors simultaneously collapse inward to origin; Bell state label appears; table of all four initial states cycles through
- Output medium: Manim (mp4)
- Two testable predictions: P1: After H⊗I, det(C)=0 — state is still separable, confirmed by r_A=(1,0,0), r_B=(0,0,1); P2: After CNOT, both reduced density matrices = I/2 (Bloch vectors at origin) — maximal entanglement, confirmed by purity=1/2
- The change: run the circuit backward (CNOT then H†=H) and show the state returning to |00⟩ — demonstrating reversibility; then introduce a bit-flip error on qubit 2 midway and show the syndrome detection
- Human supplies (Claude can't): Nothing — fully synthetic/analytic
- Teardown angle: The Hadamard does not create entanglement — it is the CNOT applied to a superposed control that does; local operations alone cannot change Schmidt rank from 1 to 2
- Exclusions: Clifford group simulation, fault-tolerant encoding, magic state distillation
- Sim slug: vol4-bell-prep-circuit
- Score: 8/10

---

## Candidate 08 — Surface Code Syndrome: Bit-Flip Error Detected Without Reading the Qubit
- Source: `quantum-mechanics-vol4/chapters/09-error-and-the-threshold-theorem.md`   (+ "LLM Exercise" from exercises 2 and 7)
- Topic: Quantum error correction — measuring parity without measuring the qubit
- Lane: MANIM (directed animation)
- Hook: The syndrome measurement is the magic trick of quantum computing: you can learn exactly which qubit flipped without ever finding out what state it was in. The logical qubit's α and β survive untouched.
- The rule: 3-qubit bit-flip code |ψ̄⟩=α|000⟩+β|111⟩; stabilizers M₁=Z₁Z₂, M₂=Z₂Z₃; each error (none, X₁, X₂, X₃) maps to a unique syndrome (±1,±1) pair; syndrome tells location without revealing amplitudes
- Concrete numbers: No error: syndrome (+1,+1); X₁ error: (−1,+1); X₂ error: (−1,−1); X₃ error: (+1,−1); ancilla measurement result is deterministic (+1 or −1) even though logical state is in superposition — both terms give identical parity eigenvalue
- The artifact / what moves: 3 data qubits + 2 ancilla qubits shown as nodes; X error "strikes" a random data qubit (animated lightning bolt); ancilla syndrome extraction circuit fires; meter shows ±1 outcome for each ancilla; syndrome table lights up the matching row; correction gate applies and state restores
- Output medium: Manim (mp4)
- Two testable predictions: P1: Both terms α|010⟩ and β|101⟩ give eigenvalue −1 for both M₁ and M₂ (qubit 2 error) — syndrome is definite even in superposition; P2: The syndrome measurement commutes with logical Z̄=Z₁Z₂Z₃ — confirmed by explicit operator algebra
- The change: show what happens when two qubits are simultaneously flipped (X₁X₃): syndrome is (+1,−1), same as X₃ alone → decoder fails and logical error occurs, motivating larger code distance
- Human supplies (Claude can't): Nothing — fully synthetic/analytic
- Teardown angle: The syndrome extracts only error location, not logical state — this is why QEC is possible; classical majority vote fails because it reads the qubit and destroys superposition
- Exclusions: Fault-tolerant syndrome extraction, surface code geometry, neural-net decoders
- Sim slug: vol4-syndrome-bit-flip
- Score: 8/10

---

## Candidate 09 — Density Matrix Heatmap: Partial Trace Kills Coherence
- Source: `quantum-mechanics-vol4/chapters/01-mixed-states-and-the-density-matrix.md`   (+ "LLM Exercise" from Ch. 2 exercises 6 and Ch. 6 exercise 1)
- Topic: The partial trace — how tracing out one qubit turns a pure state mixed
- Lane: D3/DATAVIZ (emergent / interactive)
- Hook: The joint Bell state is perfectly pure — it has maximum quantum coherence. Throw away one qubit by tracing it out and the remaining qubit is maximally mixed: zero coherence, no quantum phase, indistinguishable from a classical coin. All the information was in the correlation, not the parts.
- The rule: ρ_A = Tr_B(|ψ⟩⟨ψ|) = Σ_j ⟨j|_B ρ_AB |j⟩_B; for |Φ+⟩: ρ_A = I/2; for cos θ|00⟩+sin θ|11⟩: ρ_A = diag(cos²θ, sin²θ); purity Tr(ρ_A²) = cos⁴θ+sin⁴θ = ½(1+cos²(2θ))
- Concrete numbers: θ=0 (product): ρ_A=|0⟩⟨0|, purity=1, all coherences=0; θ=π/6: ρ_A=diag(3/4,1/4), purity=5/8; θ=π/4 (Bell): ρ_A=I/2, purity=1/2, both diagonals=1/2, off-diagonals=0
- The artifact / what moves: slider on θ; left panel shows 4×4 joint density matrix heatmap (all elements animating); right panel shows 2×2 reduced density matrix of qubit A with color-coded elements; purity bar and entropy bar update live; the off-diagonal joint elements shrink and vanish in ρ_A as θ increases
- Output medium: d3 v7 animated/interactive HTML
- Two testable predictions: P1: At θ=π/4 (Bell state), ρ_A=I/2 exactly — purity=0.5, off-diagonals of ρ_A are zero even though joint state has large off-diagonals; P2: purity of ρ_A equals ½(1+cos²(2θ)) — matches 5/8 at θ=π/6 to four significant figures
- The change: compare two different purification pathways to the same ρ_A=I/2: (1) partial trace of |Φ+⟩, (2) equal-weight classical mixture of |0⟩ and |1⟩ — same density matrix, different physical origins (demonstrating non-uniqueness of decomposition)
- Human supplies (Claude can't): Nothing — fully synthetic/analytic
- Teardown angle: The off-diagonal elements of ρ_AB encode the entanglement; the partial trace discards them; what remains is classical — this is the formal definition of decoherence when B is an environment
- Exclusions: Quantum discord, entanglement of formation for mixed states, multipartite partial traces
- Sim slug: vol4-partial-trace-heatmap
- Score: 8/10
- Status: BUILT — `open /Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-vol4/youtube/vol4-partial-trace-heatmap/vol4-partial-trace-heatmap.html`

---

## Candidate 10 — Deutsch Algorithm: Phase Kickback Cancellation Animated
- Source: `quantum-mechanics-vol4/chapters/04-quantum-gates-and-circuits.md`
- Topic: The Deutsch algorithm — how one quantum query beats two classical ones via interference, not parallelism
- Lane: MANIM (directed animation)
- Hook: Every introduction to quantum computing says "quantum parallelism evaluates f(0) and f(1) simultaneously." That is wrong — and the Deutsch algorithm shows it. The speedup comes entirely from interference of phases, not from parallel function evaluation.
- The rule: H⊗H → U_f (phase kickback: U_f|x⟩|−⟩ = (−1)^f(x)|x⟩|−⟩) → H on q₀; constant f: both phases equal → q₀ ends as |+⟩ → H maps to |0⟩; balanced f: phases opposite → q₀ ends as |−⟩ → H maps to |1⟩; one measurement decides constant vs. balanced
- Concrete numbers: constant f(x)=0: after oracle q₀=(|0⟩+|1⟩)/√2 (same sign); balanced f(x)=x: after oracle q₀=(|0⟩−|1⟩)/√2 (opposite signs); final measurement: 0 for constant, 1 for balanced — zero error, one query; classical needs 2 queries minimum
- The artifact / what moves: two-wire circuit animates step-by-step; amplitudes shown as signed bars on |0⟩ and |1⟩ in query register; oracle step shows phases flipping or not; final Hadamard shown converting relative phase into amplitude difference; measurement outcome lights up
- Output medium: Manim (mp4)
- Two testable predictions: P1: For constant f, the query register amplitude for |0⟩ and |1⟩ are equal after the oracle — they add constructively after H giving |0⟩ with probability 1; P2: For balanced f, the amplitudes are opposite — they cancel at |0⟩ and add at |1⟩ after H giving |1⟩ with probability 1
- The change: extend to Deutsch-Jozsa on n=2 qubits; show that one quantum query still suffices vs. 3 classical queries; amplitude bar chart now has 4 entries
- Human supplies (Claude can't): Nothing — fully synthetic/analytic
- Teardown angle: Phase kickback is the mechanism, not parallelism — the ancilla qubit in |−⟩ is essential; without it the oracle writes f(x) into a bit and no interference is possible
- Exclusions: Simon's algorithm, Grover's algorithm, BQP vs. NP
- Sim slug: vol4-deutsch-phase-kickback
- Score: 8/10

---

## Candidate 11 — NV Center ODMR: Field-to-Frequency Linear Map
- Source: `quantum-mechanics-vol4/chapters/08-quantum-hardware.md`   (+ "LLM Exercise" from exercise 3 and Doorway 3 in Ch. 10)
- Topic: NV-center magnetometry — how a single spin in diamond reads a magnetic field
- Lane: D3/DATAVIZ (emergent / interactive)
- Hook: A single atomic defect in diamond is a magnetic sensor. Sweep microwave frequency across the spin resonance and two dips appear in the fluorescence — their spacing is a direct linear readout of the magnetic field. No classical sensor can compete at this spatial scale.
- The rule: H_NV = D·S_z² + g_e·μ_B·B·S_z; eigenvalues E(0)=0, E(±1)=D±g_e μ_B B; transition frequencies f± = D ± (g_e μ_B/h)B ≈ 2870 ± 28B MHz (B in mT); splitting Δf = 56B MHz/mT
- Concrete numbers: B=0: single dip at 2870 MHz; B=10 mT: dips at 2590 and 3150 MHz, splitting=560 MHz; B=30 mT: dips at 2030 and 3710 MHz; sensitivity η ≈ 1/(γ_e T₂ √N) — at T₂=1μs, γ_e/2π=28 MHz/mT → η≈36 nT/√Hz per shot
- The artifact / what moves: slider on B from 0 to 50 mT; ODMR spectrum (fluorescence vs. microwave frequency) updates live with two Lorentzian dips moving symmetrically outward; numerical readout of f+ and f− and their splitting; field-to-frequency calibration line shown in side panel
- Output medium: d3 v7 animated/interactive HTML
- Two testable predictions: P1: At B=0, only one dip at 2870 MHz (zero-field splitting only); P2: Dip spacing Δf=56B MHz/mT — at B=10 mT Δf=560 MHz, at B=20 mT Δf=1120 MHz (linear, not quadratic)
- The change: add dip linewidth control (T₂ slider); show that longer T₂ → narrower linewidth → better field resolution; demonstrate the T₂-limited sensitivity formula
- Human supplies (Claude can't): Nothing — fully synthetic/analytic
- Teardown angle: The linear Zeeman splitting is exact first-order perturbation theory from Vol. 3; the NV center is unique because the zero-field splitting D makes the sensor work at zero applied bias field
- Exclusions: Ramsey-based AC sensing, vector magnetometry, hyperfine coupling to ¹⁴N
- Sim slug: vol4-nv-odmr-field-map
- Score: 8/10
- Status: BUILT — `open /Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-vol4/youtube/vol4-nv-odmr-field-map/vol4-nv-odmr-field-map.html`

---

## Candidate 12 — Superdense Coding: One Qubit, Four Messages
- Source: `quantum-mechanics-vol4/chapters/05-quantum-teleportation-and-dense-coding.md`   (+ "LLM Exercise" from exercise 5)
- Topic: Superdense coding — how shared entanglement doubles classical channel capacity
- Lane: MANIM (directed animation)
- Hook: Alice can send Bob one of four two-bit messages by sending only one qubit. Without pre-shared entanglement, one qubit carries at most one classical bit (Holevo's theorem). Entanglement doubles the capacity — not by magic, but by pre-positioning information.
- The rule: Alice applies I/X/Z/iY to her half of |Φ+⟩ → steers joint state to one of four orthogonal Bell states; sends her qubit; Bob applies CNOT then H → measures in computational basis → reads two bits; encoding: 00→I, 01→X, 10→Z, 11→iY
- Concrete numbers: Message "10": Alice applies Z to |Φ+⟩ = (|00⟩+|11⟩)/√2 → (|00⟩−|11⟩)/√2 = |Φ−⟩; Bob: CNOT → (|00⟩−|10⟩)/√2 = |−⟩|0⟩; H on qubit A → |1⟩|0⟩; measures 10 ✓; all four messages verified by the Ch. 5 worked example
- The artifact / what moves: Alice's Pauli gate choice animates onto her half of the Bell pair — showing the joint state morph to each of four Bell states; the qubit travels to Bob; Bob's decode circuit animates; final measurement lights up the two-bit message; duality diagram showing teleportation ↔ dense coding resource swap
- Output medium: Manim (mp4)
- Two testable predictions: P1: All four Bell states are orthogonal — Bob's measurement is unambiguous with certainty (not probabilistic); P2: Without the pre-shared ebit, Bob cannot decode — his reduced density matrix before receiving Alice's qubit is I/2 regardless of Alice's encoding
- The change: show what Bob sees if the Bell pair has fidelity F<1 (Werner state); decode success probability degrades as F drops; at F=1/4 (separable) all four messages become indistinguishable
- Human supplies (Claude can't): Nothing — fully synthetic/analytic
- Teardown angle: Holevo's theorem is not violated — the ebit is a resource consumed in the protocol, not created from nothing; the capacity doubling trades pre-shared entanglement for classical bit rate
- Exclusions: Quantum channel capacity theory, entanglement-assisted capacity formula, continuous-variable dense coding
- Sim slug: vol4-superdense-coding
- Score: 7/10

---

## Candidate 13 — T₂ Platform Comparison: Log-Scale Coherence Time Races
- Source: `quantum-mechanics-vol4/chapters/08-quantum-hardware.md`   (+ "LLM Exercise" from exercise 5)
- Topic: Which qubit platform wins — and what the figure of merit N_gates = T₂/t_gate actually measures
- Lane: D3/DATAVIZ (emergent / interactive)
- Hook: Trapped ions have T₂ in seconds; superconducting qubits have T₂ in microseconds — six orders of magnitude difference. Yet for fault-tolerant computing the superconducting qubit can be competitive, because it runs gates a thousand times faster. The figure of merit is not T₂ alone: it is T₂/t_gate, and the race is much closer than the raw numbers suggest.
- The rule: N_gates = T₂/t_gate; 1/T₂ = 1/(2T₁) + 1/T_φ; fault-tolerance threshold requires N_gates ≫ 10⁴; platform comparison across five platforms (transmon, trapped ion, neutral atom, NV center, spin qubit)
- Concrete numbers: Transmon: T₂=400μs, t_gate=100ns → N_gates=4000; Trapped ion: T₂=10s, t_gate=500μs → N_gates=20000; Neutral atom: T₂=1s, t_gate=1μs → N_gates=10⁶; NV center: T₂=100μs, t_gate=200ns → N_gates=500; fault-tolerance target: N_gates>10⁴; megaquop milestone: 10⁶ ops
- The artifact / what moves: horizontal log-scale bar chart for T₁, T₂, and N_gates per platform; toggle between raw T₂ view and N_gates view — watch the ranking change; slider on t_gate for each platform shows how improving gate speed shifts N_gates
- Output medium: d3 v7 animated/interactive HTML
- Two testable predictions: P1: N_gates for trapped ion (20000) > transmon (4000) by 5× even though T₂ differs by 25000×; P2: T₂≤2T₁ for every platform — confirmed by the data (no platform violates the ceiling)
- The change: add a "fault-tolerance threshold line" at N_gates=10⁴; show which platforms currently cross it and which do not; show what t_gate improvement each platform needs to cross
- Human supplies (Claude can't): Nothing — fully synthetic/analytic
- Teardown angle: The platform comparison inverts intuition — the "worst" coherence time platform (transmon) may still be the most practical because of infrastructure and gate speed advantages; no single number decides the winner
- Exclusions: Qubit connectivity, two-qubit gate fidelity comparison, NISQ vs. fault-tolerant regime
- Sim slug: vol4-platform-ngates-compare
- Score: 7/10
- Status: BUILT — `open /Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-vol4/youtube/vol4-platform-ngates-compare/vol4-platform-ngates-compare.html`

---

## Candidate 14 — Logical Error Rate Suppression: Google Willow Reconstruction
- Source: `quantum-mechanics-vol4/chapters/09-error-and-the-threshold-theorem.md`   (+ "LLM Exercise" from exercise 4 and Doorway 2 in Ch. 10)
- Topic: Reconstructing Google Willow's QEC result from the threshold formula
- Lane: D3/DATAVIZ (emergent / interactive)
- Hook: Google published a logical error rate of 0.143% per cycle for their distance-7 surface code. Can you reproduce that number from first principles in 30 seconds? With the threshold formula and one experimental parameter (Λ=2.14), you can get within a factor of 3. That is what it means to read a quantum paper.
- The rule: p_L ≈ A·(p/p_th)^⌈(d+1)/2⌉ with p_th=0.01, A=0.1; suppression factor Λ = p_L(d)/p_L(d+2) ≈ p_th/p; from Λ=2.14: p_eff ≈ 0.01/2.14 ≈ 0.0047; plug in to get p_L predictions for d=3,5,7
- Concrete numbers: Λ=2.14 → p_eff=0.00467; p_L(d=3)≈A·(0.467)²≈2.2%; p_L(d=5)≈A·(0.467)³≈1.0%; p_L(d=7)≈A·(0.467)⁴≈0.48%; paper reports 0.143% — formula overshoots by 3×; discrepancy is known: simple scaling is not exact at small d
- The artifact / what moves: three log-log curves for d=3,5,7 plotted vs. p; a vertical slider on p; "Willow data point" marker at (p_eff, 0.143%) shown on the d=7 curve; reconstruction error shown as vertical gap; second panel shows Λ vs. p with the Willow Λ=2.14 marked
- Output medium: d3 v7 animated/interactive HTML
- Two testable predictions: P1: At p=p_th, all three d-curves intersect at p_L=A=0.1 (exact from formula); P2: Λ=p_th/p at p=0.00467 → Λ=2.14, matching Willow's reported suppression factor
- The change: extend to p_L=10⁻⁶ target (needed for Shor); compute required d≈25 and physical qubit count 2d²≈1250 per logical qubit — show the overhead scaling
- Human supplies (Claude can't): Nothing — fully synthetic/analytic
- Teardown angle: The Willow result is a demonstration of a theorem (threshold theorem), not a computational advantage claim — it cannot be "simulated away" by classical computers; the 3× discrepancy from the formula teaches why exact threshold formulas require simulation beyond simple power laws
- Exclusions: Minimum weight perfect matching decoding, magic state distillation, post-NISQ roadmap
- Sim slug: vol4-willow-threshold-reconstruction
- Score: 7/10
- Status: BUILT — `open /Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-vol4/youtube/vol4-willow-threshold-reconstruction/vol4-willow-threshold-reconstruction.html`
