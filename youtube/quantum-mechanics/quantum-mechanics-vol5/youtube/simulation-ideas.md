# Simulation Ideas — quantum-mechanics-vol5

Medhavy-register "Claude Code + Manim" workflow reels.

---

## Sim-01 — Fourier Series: Building a Square Wave from Sines
- Source: `quantum-mechanics-vol5/chapters/05-fourier-series-and-the-wave-equation.md`
- Topic: CLAUDE CODE · MANIM
- Physical rule: f(x) = Σ_n (4/nπ) sin(nπx/L) for odd n; each term a harmonic; convergence improves as N → ∞
- Concrete numbers: N=1 term: pure sine; N=3: closer to square; N=9: sharp edges (Gibbs 9% overshoot); N=99: overshoot persists at 9%
- Visual artifact: partial sums animated incrementally; see the square wave emerge; Gibbs overshoot marked at the corner
- Two testable predictions: P1: the Gibbs overshoot is always ≈9% regardless of N (does NOT go away with more terms); P2: at x=L/2 all odd harmonics contribute sin(nπ/2) = ±1, converges to 1.0 exactly
- Sim slug: medhavy-vol5-fourier-square
- Status: BUILT
- Watch: `open /Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-vol5/youtube/medhavy-vol5-fourier-square/medhavy-vol5-fourier-square-review.mp4`

---

## Sim-02 — Fourier Transform: Bandwidth-Duration Uncertainty
- Source: `quantum-mechanics-vol5/chapters/06-the-fourier-transform.md`
- Topic: CLAUDE CODE · MANIM
- Physical rule: σ_t · σ_ω ≥ 1/2; Gaussian in time has Gaussian FT; width in time × width in frequency = 1/2 (minimum)
- Concrete numbers: Gaussian pulse σ_t = 1 ps → σ_ω = 0.5/(1 ps) = 5×10¹¹ rad/s → bandwidth Δν ≈ 80 GHz; compress to 0.5 ps → bandwidth doubles
- Visual artifact: two panels — pulse in time and its Fourier transform in frequency; drag slider to narrow/widen pulse and watch FT widen/narrow reciprocally
- Two testable predictions: P1: σ_t × σ_ω = 0.5 for a pure Gaussian (minimum uncertainty); P2: halving σ_t exactly doubles σ_ω (inverse proportionality)
- Sim slug: medhavy-vol5-fourier-uncertainty
- Status: BUILT
- Watch: `open /Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-vol5/youtube/medhavy-vol5-fourier-uncertainty/medhavy-vol5-fourier-uncertainty-review.mp4`

---

## Sim-03 — Group vs Phase Velocity: Wave Packet Dispersion
- Source: `quantum-mechanics-vol5/chapters/18-trigonometry-waves-and-the-harmonic-model.md`
- Topic: CLAUDE CODE · MANIM
- Physical rule: v_phase = ω/k; v_group = dω/dk; for quadratic dispersion ω=ℏk²/2m: v_group = ℏk₀/m, v_phase = ℏk₀/2m (group travels twice as fast as phase)
- Concrete numbers: electron k₀ = 1 nm⁻¹; ω₀ = ℏk₀²/2m ≈ 6×10¹³ rad/s; v_group = ℏk₀/m ≈ 1.2×10⁵ m/s; v_phase = v_group/2
- Visual artifact: carrier wave crests (moving at v_phase) and envelope (moving at v_group = 2×v_phase); clearly visible mismatch — crests slide backward through the envelope
- Two testable predictions: P1: for quadratic dispersion v_group = 2 v_phase exactly (from dω/dk = 2×ω/k); P2: group velocity = centroid velocity of |ψ|² (envelope peak tracks ⟨x⟩(t))
- Sim slug: medhavy-vol5-group-phase-velocity
- Status: BUILT
- Watch: `open /Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-vol5/youtube/medhavy-vol5-group-phase-velocity/medhavy-vol5-group-phase-velocity-review.mp4`

---

## Sim-04 — Multiplicity and the Peak: Combinatorics of Quantum States
- Source: `quantum-mechanics-vol5/chapters/14-combinatorics-and-multiplicity.md`
- Topic: CLAUDE CODE · MANIM
- Physical rule: multiplicity Ω(N,n) = C(N,n); peaks at n=N/2; ln Ω sharply peaked → entropy maximized at equilibrium
- Concrete numbers: N=10 spins: Ω peaks at n=5 with C(10,5)=252; next bin C(10,4)=210 (16% lower); N=100: peak/half-peak ratio >> 1000
- Visual artifact: bar chart of Ω vs n for N=10, then N=50; peak sharpens dramatically — the "why equilibrium is stable" visual
- Two testable predictions: P1: peak at exactly n=N/2 for any N (symmetry of Pascal's triangle); P2: peak height C(N,N/2) ≈ 2^N/√(πN/2) (Stirling estimate)
- Sim slug: medhavy-vol5-multiplicity-peak
- Status: BUILT
- Watch: `open /Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-vol5/youtube/medhavy-vol5-multiplicity-peak/medhavy-vol5-multiplicity-peak-review.mp4`
- Note: CROSS-REFERENCE — vox-multiplicity-peak is an explainer in quantum-mechanics-vol5. This simulation workflow reel is new; build it.

---

## Candidate 01 — Animate: The Euler Spiral — How e^{iθ} Draws the Unit Circle
- Source: `quantum-mechanics-vol5/chapters/01-complex-numbers-and-the-complex-exponential.md`
- Topic: Complex Exponential · Unit Circle · Phasor
- Lane: MANIM (directed animation)
- Hook: A purely algebraic formula — e raised to an imaginary power — traces a perfect circle. Watch the point spiral out from the Taylor series partial sums and land exactly on cos θ + i sin θ.
- The rule: e^{iθ} = Σ_{n=0}^{N} (iθ)^n / n! — even terms land on the real axis, odd terms on the imaginary axis; as N grows the partial sum spirals onto the unit circle
- Concrete numbers: θ = π/2 target point (0, 1); partial sums at N=1: (1, i·π/2); N=2: (1 − π²/8, iπ/2); N=6: converges to within 0.1% of (0, 1); full circle sweep θ ∈ [0, 2π]
- The artifact / what moves: dot traces the partial-sum spiral in the complex plane; at each step a new term is added as an arrow (even arrows along real axis, odd along imaginary); final locus closes the unit circle
- Output medium: Manim (mp4)
- Two testable predictions: P1: at θ = π, the partial sum series converges to (−1, 0) — i.e., e^{iπ} = −1; P2: modulus of e^{iθ} = 1 exactly for all real θ, so the locus never leaves the unit circle
- The change: replace θ → −γ + iω (complex exponent) to animate the inward spiral e^{(−γ+iω)t} — the decaying oscillator
- Human supplies (Claude can't): Nothing — fully synthetic/analytic
- Teardown angle: Euler's formula isn't a coincidence — it's the only way the exponential series can be self-consistent in the complex plane; the circle is forced by algebra
- Exclusions: derivation of the formula from first principles; connection to Fourier; quantum applications
- Sim slug: complex-euler-unit-circle
- Score: 9/10

---

## Candidate 02 — Animate: Stationary-State Phasor — Rotating Phase, Constant Probability
- Source: `quantum-mechanics-vol5/chapters/01-complex-numbers-and-the-complex-exponential.md`
- Topic: Quantum Phase · Stationary State · |ψ|² Invariance
- Lane: MANIM (directed animation)
- Hook: The wavefunction of an energy eigenstate spins relentlessly in the complex plane — yet |ψ|² never budges. Watch the phase rotate while the probability density stays frozen.
- The rule: ψ(x,t) = ψ(x) · e^{−iEt/ℏ}; |ψ(x,t)|² = |ψ(x)|²; phase rotates at angular rate ω = E/ℏ; probability density time-independent
- Concrete numbers: E₁ = π²ℏ²/(2mL²) for infinite square well, L = 1 nm → ω₁ ≈ 3.7×10¹⁵ rad/s; three eigenstates n=1,2,3 each rotating at different rates ωₙ = n²ω₁
- The artifact / what moves: left panel — phasor tip tracing unit circle at rate E/ℏ (different rates for each n); right panel — |ψ|² bars frozen at constant height; bottom panel — superposition of n=1+n=2 shows |ψ|² oscillating at frequency (E₂−E₁)/h
- Output medium: Manim (mp4)
- Two testable predictions: P1: for a single eigenstate |ψ(x,t)|² is exactly time-independent regardless of rotation speed; P2: for superposition ψ₁ + ψ₂, |ψ|² oscillates at frequency (E₂−E₁)/h = 3ω₁/(2π) ≈ 1.77×10¹⁵ Hz
- The change: switch to a superposition of n=1 and n=2 — now |ψ|² breathes at the beat frequency, making the interference term visible
- Human supplies (Claude can't): Nothing — fully synthetic/analytic
- Teardown angle: the "rotating but frozen" paradox forces the question of what is real in quantum mechanics — the probability, not the phase, is observable
- Exclusions: time-dependent perturbation theory; measurement collapse; spin states
- Sim slug: stationary-state-phasor-rotation
- Score: 9/10

---

## Candidate 03 — Animate: Phasor Addition — Why Two Oscillations Add as Vectors
- Source: `quantum-mechanics-vol5/chapters/01-complex-numbers-and-the-complex-exponential.md`
- Topic: Phasor · Superposition · Complex Amplitude
- Lane: MANIM (directed animation)
- Hook: Adding two sinusoids with the same frequency looks like painful trig — until you see it's just vector addition in the complex plane. Watch 3cos(ωt) + 4cos(ωt+90°) become 5cos(ωt+53°) in one Pythagorean step.
- The rule: A₁cos(ωt) + A₂cos(ωt+φ) = Re[(Ã₁+Ã₂)e^{iωt}]; Ã₁ = A₁, Ã₂ = A₂e^{iφ}; resultant = |Ã₁+Ã₂| at angle arg(Ã₁+Ã₂)
- Concrete numbers: A₁=3, φ₁=0 → phasor (3,0); A₂=4, φ₂=90° → phasor (0,4); vector sum (3,4); |result| = 5, phase = arctan(4/3) = 53.1°
- The artifact / what moves: two phasors rotating on the complex plane; their vector sum (tip-to-tail) also rotates; real part projected onto x-axis gives oscillation — three sinusoids plotted below showing the two inputs and the output
- Output medium: Manim (mp4)
- Two testable predictions: P1: for perpendicular phasors (90° phase difference) amplitude is exactly √(A₁²+A₂²) by Pythagoras — for (3,4) that is exactly 5; P2: phase cancellation — when φ = 180°, resultant amplitude = |A₁−A₂|, for A₁=A₂ the result is exactly zero
- The change: sweep φ from 0 to 2π and animate amplitude as a function of phase — showing the full cos(φ/2) dependence
- Human supplies (Claude can't): Nothing — fully synthetic/analytic
- Teardown angle: trig identities are the slow path; complex vector addition is the fast path — the same calculation, two notations, wildly different cognitive load
- Exclusions: Fourier series; quantum interference; circuit phasors in AC analysis
- Sim slug: phasor-vector-addition
- Score: 8/10

---

## Candidate 04 — Explore: Quantum Revival Explorer — Superposition Breathing in a Box
- Source: `quantum-mechanics-vol5/chapters/05-fourier-series-and-the-wave-equation.md` (LLM Exercise 5)
- Topic: Quantum Revival · Fourier Beating · Superposition
- Lane: D3/DATAVIZ (emergent / interactive)
- Hook: Drop any initial wavefunction into an infinite square well and watch it deform, spread, reform — and at the revival time, the original shape reconstructs from incommensurable frequencies alone.
- The rule: ψ(x,t) = Σ_n cₙ e^{−iEₙt/ℏ} ψₙ(x); Eₙ = n²E₁; |ψ(x,t)|² computed in real time; revival when all phases return simultaneously at T_rev = 2πℏ/E₁
- Concrete numbers: parabola initial state x(L−x); c_n = 0 for even n; c₁ dominates; T_rev = 2πℏ/(π²ℏ²/2mL²) = 4mL²/πℏ; for L=1 nm electron: T_rev ≈ 2.4 fs
- The artifact / what moves: animated |ψ(x,t)|² sloshes left-right; slider for N terms included (1→20); timeline bar showing fraction of T_rev elapsed; play/pause button
- Output medium: d3 v7 animated/interactive HTML
- Two testable predictions: P1: for superposition of n=1 and n=3 only, |ψ|² beats at frequency (E₃−E₁)/h = 8E₁/h; P2: revival at T_rev/2 gives a time-reversed mirror of the initial shape — the parabola reforms reflected
- The change: switch initial state from parabola to a pure Gaussian bump — now many modes contribute and the revival is partial, showing imperfect reconstruction
- Human supplies (Claude can't): Nothing — fully synthetic/analytic
- Teardown angle: revival is not magic — it is constructive interference of incommensurable frequencies; the box's n² spectrum is the only reason it works
- Exclusions: anharmonic oscillator revivals; coherent states; measurement
- Sim slug: quantum-revival-box-explorer
- Score: 9/10
- Status: BUILT — `open /Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-vol5/youtube/quantum-revival-box-explorer/quantum-revival-box-explorer.html`

---

## Candidate 05 — Explore: Eigenvalue Explorer — Hermitian Matrices and the Spectral Theorem
- Source: `quantum-mechanics-vol5/chapters/08-eigenvalues-and-diagonalization.md`
- Topic: Eigenvalue · Hermitian Matrix · Spectral Decomposition
- Lane: D3/DATAVIZ (emergent / interactive)
- Hook: Drag any matrix entry and watch the eigenvalues move in real time. The moment a matrix becomes Hermitian, eigenvalues snap to the real axis — and stay there no matter how you twirl the complex entries.
- The rule: for 2×2 matrix A = [[a,b],[c,d]], eigenvalues λ = (a+d)/2 ± √(((a−d)/2)²+bc); for Hermitian (c = b*), discriminant is always real, so λ ∈ ℝ
- Concrete numbers: start with σ_y = [[0,−i],[i,0]] → eigenvalues ±1; perturb off-diagonal to make non-Hermitian → eigenvalues go complex; restore Hermitian condition → snap back to real axis
- The artifact / what moves: matrix entries editable; complex eigenvalue plane shown; two dots tracking λ₁ λ₂; color coding — real eigenvalues shown in blue, complex in red; eigenvector arrows update in real time
- Output medium: d3 v7 animated/interactive HTML
- Two testable predictions: P1: for any real symmetric matrix (a special case of Hermitian) eigenvalues are guaranteed real — verify by constructing one and dragging entries; P2: for non-Hermitian matrix with purely imaginary off-diagonal entries, eigenvalues can become pure imaginary — confirm with [[0,2],[−2,0]] giving eigenvalues ±2i
- The change: toggle between 2×2 and show the characteristic polynomial curve p(λ) = det(A−λI) — roots are visible as zero-crossings
- Human supplies (Claude can't): Nothing — fully synthetic/analytic
- Teardown angle: Hermiticity is not a postulate about nature — it is a constraint on the matrix that forces measurement outcomes to be real numbers; relax it and outcomes become complex and unphysical
- Exclusions: infinite-dimensional operators; continuous spectrum; degenerate perturbation theory
- Sim slug: hermitian-eigenvalue-explorer
- Status: BUILT — `open /Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-vol5/youtube/hermitian-eigenvalue-explorer/hermitian-eigenvalue-explorer.html`
- Score: 8/10

---

## Candidate 06 — Animate: Gram-Schmidt in the Complex Plane — Building Orthonormal Bases
- Source: `quantum-mechanics-vol5/chapters/07-vectors-vector-spaces-and-inner-products.md`
- Topic: Gram-Schmidt · Inner Product · Orthonormalization
- Lane: MANIM (directed animation)
- Hook: Start with two non-orthogonal vectors in ℂ². Watch Gram-Schmidt carve out the perpendicular direction — using the complex inner product, which requires conjugation — to produce an orthonormal pair that would serve as a valid quantum measurement basis.
- The rule: given u₁, u₂; e₁ = u₁/‖u₁‖; e₂ = (u₂ − ⟨e₁|u₂⟩e₁)/‖…‖; complex inner product ⟨φ|ψ⟩ = Σᵢ φᵢ*ψᵢ
- Concrete numbers: u₁ = (1,i)ᵀ → ‖u₁‖ = √2 → e₁ = (1,i)ᵀ/√2; u₂ = (1,0)ᵀ; projection ⟨e₁|u₂⟩ = 1/√2; residual = (1/2,−i/2)ᵀ; e₂ = (1,−i)ᵀ/√2
- The artifact / what moves: animated 2D complex-vector representation; projection arrow shrinking as component is removed; orthogonality verified by showing inner product meter go to 0.00; final pair drawn as perpendicular quantum basis vectors
- Output medium: Manim (mp4)
- Two testable predictions: P1: ⟨e₁|e₂⟩ = (1/2)(1·1 + (−i)(i)) = (1/2)(1+1)... wait — correct: (1/2)(1*(1) + (−i)*(−i)) = (1/2)(1−1) = 0; verifiable to machine precision; P2: using real dot product uᵀv instead of uᴴv gives nonzero "orthogonality" — u₁·u₂ = 1+0 = 1 ≠ 0 — demonstrating necessity of conjugation
- The change: repeat with a degenerate pair (u₁ ∥ u₂) — show Gram-Schmidt fails (zero residual), producing no second basis vector
- Human supplies (Claude can't): Nothing — fully synthetic/analytic
- Teardown angle: the conjugate inner product is not a formalism nicety — it is the only inner product for which Gram-Schmidt produces an orthonormal basis in complex space
- Exclusions: infinite-dimensional function spaces; Legendre polynomial orthogonalization; entanglement
- Sim slug: gram-schmidt-complex-plane
- Score: 8/10

---

## Candidate 07 — Animate: Quantization from Boundary Conditions — Standing Waves and Energy Levels
- Source: `quantum-mechanics-vol5/chapters/03-ordinary-differential-equations.md`
- Topic: ODE · Quantization · Energy Levels
- Lane: MANIM (directed animation)
- Hook: Continuous energy, continuous solutions — until the walls speak. Watch a sinusoidal wavefunction sweep through all energies: almost all fail the boundary condition. Only at discrete E_n does a standing wave fit exactly inside the box.
- The rule: ψ″ = −k²ψ inside [0,L]; general solution A sin(kx) + B cos(kx); ψ(0)=0 forces B=0; ψ(L)=0 forces sin(kL)=0 → k_n = nπ/L → E_n = n²π²ℏ²/(2mL²)
- Concrete numbers: L = 1 nm electron; E₁ = 0.376 eV, E₂ = 4E₁ = 1.50 eV, E₃ = 9E₁ = 3.38 eV; rejected curve at k = 1.7π/L shown failing to reach zero at x=L
- The artifact / what moves: k slider sweeping from 0 to 4π/L; wavefunction drawn in real time; the right wall at x=L — accepted curves glow green and freeze when ψ(L)=0; rejected curves glow red and pass through
- Output medium: Manim (mp4)
- Two testable predictions: P1: allowed energies scale exactly as n² — E₃/E₁ = 9 exactly, verifiable from the slider positions; P2: the n-th allowed wavefunction has exactly n−1 interior nodes (zero crossings), testable by counting
- The change: replace infinite wall with finite step V₀ — now there are only finitely many bound states, and the wavefunction leaks into the classically forbidden region (evanescent tail)
- Human supplies (Claude can't): Nothing — fully synthetic/analytic
- Teardown angle: quantization is not put in by hand — it falls out from requiring a continuous wavefunction to hit zero at both walls simultaneously; continuous energy → discrete spectrum is a boundary-condition theorem
- Exclusions: scattering states; time evolution; harmonic oscillator
- Sim slug: quantization-boundary-conditions
- Score: 10/10

---

## Candidate 08 — Animate: Taylor Convergence and the Small-Angle Approximation
- Source: `quantum-mechanics-vol5/chapters/04-series-expansions-and-approximation.md`
- Topic: Taylor Series · Convergence · Small-Angle
- Lane: MANIM (directed animation)
- Hook: sin(θ) and θ are indistinguishable at small angles — until they diverge. Animate each successive Taylor term as a correction: watch the polynomial wrap around sin(x) progressively tighter, and mark exactly where the 1% error threshold lies.
- The rule: sin(x) = x − x³/6 + x⁵/120 − …; N-term truncation error ≤ |x|^{N+2}/(N+2)!; small-angle approximation sin(x)≈x valid to 1% for |x| < 0.244 rad
- Concrete numbers: at x=15°=0.262 rad, truncation at N=1 (linear): error = 0.262 − sin(0.262) = 0.003 (1.2%); at x=30°=0.524 rad, error = 2.4%; N=3 (cubic) reduces 30° error to 0.02%
- The artifact / what moves: sin(x) curve in blue; successive polynomial approximations added one term at a time; shaded "good approximation" band showing where |sin(x)−P_N(x)| < 1%; vertical markers at 5°, 15°, 30°
- Output medium: Manim (mp4)
- Two testable predictions: P1: at x = π/2 the linear approximation gives π/2 ≈ 1.571 vs sin(π/2) = 1.0 — a 57% error, demonstrating the approximation completely fails beyond its domain; P2: the cubic approximation sin(x) ≈ x − x³/6 predicts sin(30°) = 0.524 − 0.524³/6 = 0.500 to within 0.02% of the exact value 0.5000
- The change: switch to perturbation theory context — animate how E_n(λ) = E_n⁰ + λE_n¹ + λ²E_n² diverges when λ exceeds the radius of convergence
- Human supplies (Claude can't): Nothing — fully synthetic/analytic
- Teardown angle: the small-angle approximation is not "approximately true" — it is a Taylor truncation with a quantifiable error bound; know the bound before trusting it
- Exclusions: WKB approximation; Padé approximants; asymptotic vs. convergent series
- Sim slug: taylor-convergence-small-angle
- Score: 8/10

---

## Candidate 09 — Animate: Hermite Polynomial Nodes — QHO Eigenstates and the Gaussian Envelope
- Source: `quantum-mechanics-vol5/chapters/11-special-functions.md`
- Topic: Harmonic Oscillator · Hermite Polynomials · Node Counting
- Lane: MANIM (directed animation)
- Hook: The quantum harmonic oscillator's eigenstates are Hermite polynomials times a Gaussian. Each higher level adds exactly one more node — and the ground state has zero nodes and nonzero energy. Watch the energy ladder climb as nodes accumulate.
- The rule: ψₙ(ξ) = Nₙ Hₙ(ξ) e^{−ξ²/2}; Eₙ = ℏω(n+½); Hₙ has exactly n real zeros; orthogonality weight e^{−ξ²}
- Concrete numbers: n=0: H₀=1, ψ₀∝e^{−ξ²/2}, E₀=ℏω/2 (zero nodes); n=1: H₁=2ξ, one node at ξ=0, E₁=3ℏω/2; n=2: H₂=4ξ²−2, nodes at ξ=±1/√2, E₂=5ℏω/2; n=5: 5 nodes, classical turning points at ξ=±√11
- The artifact / what moves: energy ladder on the left; wavefunction plotted on the right for each n; Gaussian envelope shown as dashed curve; node positions marked as red dots; classical turning points shown as vertical dashed lines (where |ψ|² leaks into classically forbidden region)
- Output medium: Manim (mp4)
- Two testable predictions: P1: ψₙ has exactly n nodes — verifiable for n=0,1,2,3,4 by counting zero crossings; P2: the probability density |ψₙ|² leaks past the classical turning points (ξ=±√(2n+1)) for all n — measurable as fraction of area outside the classical region
- The change: overlay classical probability distribution (proportional to 1/v(x)) on top of |ψₙ|² for large n — showing the correspondence principle: quantum probability concentrates near turning points just as classical particle slows down there
- Human supplies (Claude can't): Nothing — fully synthetic/analytic
- Teardown angle: zero-point energy is not a quirk — it is forced by the n=0 termination condition on the Hermite series; no Gaussian with zero energy can satisfy Hermite's ODE
- Exclusions: ladder operators; coherent states; squeezed states; anharmonic oscillator
- Sim slug: qho-hermite-eigenstates
- Score: 9/10

---

## Candidate 10 — Explore: Bloch Sphere Explorer — Qubit States and Spin Rotations
- Source: `quantum-mechanics-vol5/chapters/12-matrices-determinants-and-linear-systems.md`
- Topic: Bloch Sphere · Pauli Matrices · Spin-½
- Lane: D3/DATAVIZ (emergent / interactive)
- Hook: Every qubit state lives on a sphere. Every rotation gate moves the state along a geodesic arc. Apply H, X, Z, S in any order — and trace where the Bloch vector lands.
- The rule: ρ = (I + r⃗·σ⃗)/2, |r⃗|≤1; pure states on surface; U = exp(−iα n̂·σ⃗/2) rotates r⃗ by angle α about n̂; Pauli gate X flips (θ→π−θ, φ→φ+π), H maps Z-axis to X-axis
- Concrete numbers: |0⟩ = north pole (0,0,1); |+⟩ = (1,0,0) after H; S gate adds phase — rotates around Z by 90°; T gate rotates by 45°; CNOT on two qubits creates entanglement (takes state off sphere to interior)
- The artifact / what moves: 3D interactive Bloch sphere; drag to rotate view; buttons for X Y Z H S T gates; state vector arrow updates immediately; path traced as arc; measurement outcome probabilities shown
- Output medium: d3 v7 animated/interactive HTML
- Two testable predictions: P1: H gate applied twice returns to initial state (H²=I) — Bloch vector returns to start after two applications; P2: a 2π rotation (full 360° around any axis) sends the Bloch vector back to itself, but the spinor picks up a −1 phase — verifiable by computing U(2π) = −I, which requires 720° for the spinor to return to itself
- The change: apply a depolarizing channel to shrink the Bloch vector toward the origin — showing the mixed state at the center (maximally mixed)
- Human supplies (Claude can't): Nothing — fully synthetic/analytic
- Teardown angle: the Bloch sphere is not just a picture — it is the complete state space of a qubit; every physical operation is a rotation or contraction of this sphere
- Exclusions: two-qubit entanglement; quantum teleportation; error correction codes
- Sim slug: bloch-sphere-qubit-explorer
- Score: 8/10
- Status: BUILT — `open /Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-vol5/youtube/bloch-sphere-qubit-explorer/bloch-sphere-qubit-explorer.html`

---

## Candidate 11 — Animate: Spherical Harmonics Gallery — Angular Momentum Eigenstates
- Source: `quantum-mechanics-vol5/chapters/11-special-functions.md`
- Topic: Spherical Harmonics · Angular Momentum · Hydrogen Orbitals
- Lane: MANIM (directed animation)
- Hook: The hydrogen atom's angular wavefunctions are not arbitrary — they are the unique solutions that stay finite at the poles. Watch Y_{ℓm}(θ,φ) unfurl on the sphere: each new ℓ adds a nodal circle, each m twists the azimuthal phase.
- The rule: Y_{ℓm}(θ,φ) = N_{ℓm} P_ℓ^m(cosθ) e^{imφ}; L̂² Y_{ℓm} = ℏ²ℓ(ℓ+1)Y_{ℓm}; L̂_z Y_{ℓm} = ℏm Y_{ℓm}; |Y_{ℓm}|² plotted as radial distance from origin
- Concrete numbers: Y₀₀ = 1/√(4π) (sphere); Y₁₀ = √(3/4π)cosθ (dumbbell); Y₁,±₁ = ∓√(3/8π)sinθ e^{±iφ}; Y₂₀ has two nodal cones at θ where P₂(cosθ)=0 → θ ≈ 54.7°
- The artifact / what moves: 3D surface |Y_{ℓm}|² morphing as ℓ and m advance; nodal circles highlighted; color encoding m (azimuthal winding number); separate panel showing real and imaginary parts of the phase e^{imφ} winding around the z-axis
- Output medium: Manim (mp4)
- Two testable predictions: P1: Y_{ℓ0} has ℓ nodal cones (zeros of P_ℓ(cosθ)) — verifiable: Y₂₀ has 2 cones, Y₃₀ has 3; P2: the total angular node count for Y_{ℓm} is ℓ total — (ℓ−|m|) polar nodes plus |m| azimuthal nodes; for Y₂₂ that is 0 polar + 2 azimuthal = 2 total ✓
- The change: form real combinations (Y_{ℓ,+m} ± Y_{ℓ,−m})/√2 — produce the p_x, p_y, d_{xy} orbital shapes used in chemistry; show the azimuthal winding cancels to give real lobes
- Human supplies (Claude can't): Nothing — fully synthetic/analytic
- Teardown angle: hydrogen orbitals are not arbitrary shapes chosen for chemistry — they are the unique functions on a sphere that are eigenstates of L̂² and L̂_z; shape is forced by angular momentum quantization
- Exclusions: radial wavefunctions; spin; perturbation theory; molecular orbital theory
- Sim slug: spherical-harmonics-gallery
- Score: 9/10

---

## Candidate 12 — Animate: Separation of Variables — Three Quantum Numbers from One PDE
- Source: `quantum-mechanics-vol5/chapters/10-multivariable-calculus-and-separation-of-variables.md`
- Topic: Separation of Variables · Quantum Numbers · Central Potential
- Lane: MANIM (directed animation)
- Hook: One PDE in three variables becomes three independent ODEs — and each ODE births a quantum number. Watch the separation cascade: first φ peels off and forces m to be an integer; then θ peels off and forces ℓ ≥ |m|; finally the radial equation forces n.
- The rule: ψ(r,θ,φ) = R(r)Θ(θ)Φ(φ); Φ″ = −m²Φ → e^{imφ}; single-valuedness Φ(φ+2π)=Φ(φ) → m ∈ ℤ; polar equation → P_ℓ^m finite at poles → ℓ ∈ {0,1,2,…}; radial termination → n = 1,2,3,…
- Concrete numbers: for hydrogen n=2: allowed (ℓ,m) pairs: (0,0), (1,−1), (1,0), (1,1) — 4-fold spatial degeneracy from n²=4; E₂ = −13.6/4 = −3.4 eV
- The artifact / what moves: flowchart animation showing the PDE splitting → ODE₁ (φ) → ODE₂ (θ) → ODE₃ (r); each arrow labeled with the separation constant; each ODE box shows solution and the quantization condition that discretizes the constant
- Output medium: Manim (mp4)
- Two testable predictions: P1: m must be an integer — demonstrate by showing e^{im(φ+2π)} = e^{imφ} requires e^{2πim}=1, satisfied only for m ∈ ℤ; P2: total number of (n,ℓ,m) states at level n is exactly n² (summing 2ℓ+1 from ℓ=0 to n−1 = n²)
- The change: replace Coulomb potential with a spherical harmonic oscillator — angular equation unchanged (Y_{ℓm} still the eigenfunctions), only radial equation changes; demonstrates that angular functions are universal to all central potentials
- Human supplies (Claude can't): Nothing — fully synthetic/analytic
- Teardown angle: the quantum numbers n, ℓ, m are not postulated — they fall out of three separate regularity/single-valuedness conditions on three independent ODEs produced by separation of variables
- Exclusions: spin quantum number; relativistic corrections; multi-electron atoms
- Sim slug: separation-variables-quantum-numbers
- Score: 9/10

---

## Candidate 13 — Animate: Tunneling Transmission — Exponential Suppression vs. Barrier Width
- Source: `quantum-mechanics-vol5/chapters/13-logarithms-exponentials-and-scales.md`
- Topic: Quantum Tunneling · WKB · Exponential Decay
- Lane: MANIM (directed animation)
- Hook: Double the barrier width and transmission drops by a factor of e^{2κ·ΔL}. That's not halving — it's exponential annihilation. Watch T = e^{−2κL} collapse from 0.6 to 10^{−5} as you stretch the barrier by 1 nm.
- The rule: T ≈ e^{−2κL}; κ = √(2m(V₀−E))/ℏ; ln T = −2κL (linear on semi-log plot); each 2.3 units of 2κL reduces T by one decade
- Concrete numbers: electron with V₀−E = 1 eV → κ = 5.1 nm⁻¹; at L=0.1 nm: 2κL=1.02 → T=0.36; at L=0.5 nm: T=e^{−5.1}≈0.006; at L=1 nm: T≈4×10^{−5}; at L=2 nm: T≈2×10^{−9}
- The artifact / what moves: left panel — wavefunction oscillating in, decaying through barrier, oscillating out (with amplitude showing T); right panel — semi-log plot of T vs L showing the straight line; L slider moves simultaneously
- Output medium: Manim (mp4)
- Two testable predictions: P1: on semi-log axes T vs L is an exact straight line with slope −2κ — verifiable from two points; P2: doubling V₀−E increases κ by √2, so the same L now gives T² (squaring the suppression) — e.g., at L=0.5 nm, V₀−E=4 eV gives T = e^{−2·10.2·0.5} = e^{−10.2} ≈ 3.7×10^{−5} vs (0.006)² = 3.6×10^{−5} ✓
- The change: replace rectangular barrier with triangular (linear ramp) — WKB integral becomes (2/3)κ_max·L instead of κ·L; show the wavefunction decay is now curved on semi-log axes
- Human supplies (Claude can't): Nothing — fully synthetic/analytic
- Teardown angle: exponential sensitivity is why STM has atomic resolution — a 1 Å change in tip height changes current by e^{1.02}≈2.8×; a 0.02 Å change is measurable
- Exclusions: resonant tunneling; alpha decay Gamow factor; time-reversal in tunneling
- Sim slug: tunneling-transmission-barrier
- Score: 9/10

---

## Candidate 14 — Explore: Uncertainty Principle Sandbox — Position and Momentum Trade-Off
- Source: `quantum-mechanics-vol5/chapters/06-the-fourier-transform.md`
- Topic: Uncertainty Principle · Gaussian Wave Packet · Fourier Reciprocity
- Lane: D3/DATAVIZ (emergent / interactive)
- Hook: Squeeze the position wavepacket with a slider and watch the momentum spread explode — the product σ_x · σ_p stays pinned at ℏ/2. The uncertainty principle is not a limit of our instruments; it is a theorem about Fourier pairs.
- The rule: ψ(x) = (πa²)^{−1/4} e^{−x²/2a²}; Δx = a/√2; Δp = ℏ/(a√2); Δx·Δp = ℏ/2 (exact for Gaussian); any non-Gaussian gives Δx·Δp > ℏ/2
- Concrete numbers: a = 1 nm → Δx = 0.707 nm, Δp = 0.707 ℏ/nm, product = ℏ/2; a = 0.1 nm → Δx = 0.0707 nm, Δp = 7.07 ℏ/nm; a = 10 nm → Δx = 7.07 nm, Δp = 0.0707 ℏ/nm
- The artifact / what moves: two-panel display — |ψ(x)|² on left, |φ̃(p)|² on right; a slider (log scale) controlling width parameter a; live readout of Δx, Δp, and Δx·Δp; dashed line at ℏ/2 showing the minimum is never violated; switch to non-Gaussian (top-hat or triangle) to see product increase
- Output medium: d3 v7 animated/interactive HTML
- Two testable predictions: P1: for the Gaussian, Δx·Δp = ℏ/2 exactly regardless of a — product readout stays pinned at ℏ/2 as slider moves; P2: for a top-hat function of width W, the FT is a sinc function with Δp ≈ 2πℏ/W, giving Δx·Δp ≈ πℏ > ℏ/2 — inequality is strict for non-Gaussians
- The change: shift center momentum by adding phase e^{ik₀x} — Δx·Δp is unchanged (momentum boost shifts mean but not spread), demonstrating that the uncertainty is about spread, not location
- Human supplies (Claude can't): Nothing — fully synthetic/analytic
- Teardown angle: the uncertainty principle has nothing to do with disturbing particles during measurement — it is a mathematical identity about any function and its Fourier transform
- Exclusions: Robertson's commutator derivation; energy-time uncertainty; squeezed states
- Sim slug: uncertainty-principle-sandbox
- Score: 10/10
- Status: BUILT — `open /Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-vol5/youtube/uncertainty-principle-sandbox/uncertainty-principle-sandbox.html`

---

## Candidate 15 — Animate: Perturbation Convergence — When the Series Breaks Down
- Source: `quantum-mechanics-vol5/chapters/04-series-expansions-and-approximation.md`
- Topic: Perturbation Theory · Energy Levels · Convergence Radius
- Lane: MANIM (directed animation)
- Hook: Perturbation theory is a Taylor series in disguise. Watch two energy levels repel each other as a perturbation grows — and crash when the denominator hits zero. The divergence is a convergence radius failure, not physics.
- The rule: E_n(λ) = E_n⁰ + λ⟨n|H′|n⟩ + λ² Σ_{m≠n} |⟨m|H′|n⟩|²/(E_n⁰−E_m⁰) + …; convergence fails when λ|⟨m|H′|n⟩|/(E_n⁰−E_m⁰) ≥ 1
- Concrete numbers: 2×2 system H = diag(0, ε) + λ[[0,1],[1,0]]; exact eigenvalues λ_± = (ε/2) ± √((ε/2)²+λ²); perturbation series valid for λ ≪ ε; at λ = ε/2 the series is at its radius of convergence; for ε = 0 (degenerate) the series diverges immediately for any λ ≠ 0
- The artifact / what moves: two energy curves plotted vs. λ (exact: avoided crossing hyperbola); perturbation series truncated at 1st, 2nd, 3rd order shown as dashed curves; watch them diverge from exact solution as λ increases past the convergence radius marked by vertical line
- Output medium: Manim (mp4)
- Two testable predictions: P1: at λ = 0 all truncated series agree with exact eigenvalues (exact match at the expansion point); P2: for ε = 0 (degenerate case) even the first-order correction E_n^{(1)} = ⟨n|H′|n⟩ = 0 fails to lift the degeneracy — must diagonalize H′ in the degenerate subspace first
- The change: animate the degenerate case ε → 0 in slow motion — show the avoided crossing collapse and the eigenvalues kissing at λ=0; the gap is exactly 2|⟨1|H′|2⟩| = 2λ
- Human supplies (Claude can't): Nothing — fully synthetic/analytic
- Teardown angle: degeneracy is not just a special case — it is a pole of the perturbation series; the fix (diagonalizing H′ in the degenerate subspace) is choosing the right expansion point for the underlying Taylor series
- Exclusions: time-dependent perturbation theory; Stark effect specifics; variational method
- Sim slug: perturbation-convergence-avoided-crossing
- Score: 8/10

---

## Candidate 16 — Explore: Variational Bound Optimizer — Upper-Bounding the Ground State
- Source: `quantum-mechanics-vol5/chapters/15-calculus-of-variations.md`
- Topic: Variational Method · Ground State · Upper Bound
- Lane: D3/DATAVIZ (emergent / interactive)
- Hook: Any normalized wavefunction gives an upper bound on the ground-state energy. Drag the shape of your trial function — wider, narrower, bumped left — and watch ⟨H⟩ descend toward (but never below) E₀. The Gaussian bottoms out exactly.
- The rule: E₀ ≤ ⟨ψ_trial|Ĥ|ψ_trial⟩/⟨ψ_trial|ψ_trial⟩ for any ψ_trial; for harmonic oscillator with ψ_trial = (2α/π)^{1/4} e^{−αx²}: ⟨H⟩ = ℏω(α/ω_c + ω_c/4α) where ω_c = mω/ℏ; minimized at α = ω_c/2 giving ⟨H⟩ = ℏω/2 = E₀ exactly
- Concrete numbers: for harmonic oscillator with ω = 10¹⁵ rad/s (optical phonon scale): E₀ = ℏω/2 ≈ 0.33 eV; trial Gaussian with wrong width α = 2ω_c gives ⟨H⟩ ≈ 0.625ℏω = 1.25E₀ (25% too high); correct α gives ⟨H⟩ = E₀ exactly
- The artifact / what moves: interactive trial wavefunction with width slider (Gaussian) and shape buttons (triangle, parabola, top-hat); ⟨H⟩ readout updates in real time; red dashed line at exact E₀; the bound can never go below the red line; optimize button runs gradient descent to find best Gaussian width
- Output medium: d3 v7 animated/interactive HTML
- Two testable predictions: P1: for the quantum harmonic oscillator, the Gaussian trial function achieves the exact ground-state energy ⟨H⟩ = ℏω/2 at optimal width α = mω/2ℏ; P2: for the infinite square well, the parabola trial ψ∝x(L−x) gives ⟨H⟩ = 5ℏ²π²/(mL²) ≈ 1.013E₀ — exactly 1.3% above the true ground state
- The change: switch to an anharmonic oscillator V = mω²x²/2 + λx⁴ — now no analytic exact answer; the variational bound provides the best numerical estimate
- Human supplies (Claude can't): Nothing — fully synthetic/analytic
- Teardown angle: the variational principle is not a trick — it is the stationarity condition δ⟨H⟩=0 that IS the Schrödinger equation; the upper bound property follows because E₀ is the minimum eigenvalue
- Exclusions: Rayleigh-Ritz matrix method; time-dependent variational principle; density functional theory
- Sim slug: variational-bound-optimizer
- Score: 9/10
- Status: BUILT — `open /Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-vol5/youtube/variational-bound-optimizer/variational-bound-optimizer.html`

---

## Candidate 17 — Animate: Schmidt Decomposition — Entanglement Hidden in a Matrix
- Source: `quantum-mechanics-vol5/chapters/16-tensor-products-and-composite-systems.md`
- Topic: Tensor Product · Entanglement · Schmidt Decomposition
- Lane: MANIM (directed animation)
- Hook: Any two-qubit state hides a 2×2 matrix of coefficients. Apply SVD to that matrix and read off the Schmidt number. If rank = 1 the state is separable; rank = 2 is maximally entangled. Watch a state morph from product to Bell state as one matrix entry grows.
- The rule: |ψ⟩ = Σ_{ij} c_{ij}|ij⟩; coefficient matrix M = [[c₀₀,c₀₁],[c₁₀,c₁₁]]; Schmidt decomposition via SVD M = UΣVᵀ; Schmidt coefficients are singular values; entanglement = (rank M) = 1 iff M is rank 1
- Concrete numbers: product state |00⟩: M=[[1,0],[0,0]], rank 1, σ₁=1, σ₂=0; Bell state |Φ⁺⟩=(|00⟩+|11⟩)/√2: M=(1/√2)[[1,0],[0,1]], rank 2, σ₁=σ₂=1/√2; von Neumann entropy S=−Σσᵢ²log₂(σᵢ²) = 0 (product) or 1 ebit (Bell)
- The artifact / what moves: 2×2 complex matrix shown with adjustable entries; SVD computed in real time; singular values displayed; Bloch spheres for each subsystem (reduced density matrix); entanglement entropy meter; animate path from |00⟩ to |Φ⁺⟩ by growing the off-diagonal c₁₁ entry
- Output medium: Manim (mp4)
- Two testable predictions: P1: any state with rank-1 coefficient matrix is separable (tensor product of two single-qubit states) — verifiable by checking that the partial trace gives a pure state with Tr(ρₐ²)=1; P2: for maximally entangled state, partial trace gives ρₐ = I/2 (maximally mixed) with Tr(ρₐ²) = 1/2
- The change: generalize to a 3-qubit GHZ state |000⟩+|111⟩ — Schmidt decomposition requires a different bipartition; show that cutting A|BC vs. AB|C gives different Schmidt spectra
- Human supplies (Claude can't): Nothing — fully synthetic/analytic
- Teardown angle: entanglement is not a philosophical mystery — it is the rank of a coefficient matrix; SVD computes it in one step
- Exclusions: quantum teleportation protocol; LOCC operations; entanglement distillation
- Sim slug: schmidt-decomposition-entanglement
- Score: 8/10

---

## Candidate 18 — Animate: Dimensional Analysis — Building the Bohr Radius from Three Constants
- Source: `quantum-mechanics-vol5/chapters/17-units-dimensions-and-estimation.md`
- Topic: Dimensional Analysis · Bohr Radius · Atomic Scale
- Lane: MANIM (directed animation)
- Hook: Three physical constants — ℏ, mₑ, e²/4πε₀ — contain only one combination with units of length. Animate the dimensional algebra: powers of mass, length, time cancel one by one until the Bohr radius is the only survivor.
- The rule: a₀ = ℏ^α mₑ^β (e²/4πε₀)^γ with α=2, β=−1, γ=−1; [ℏ]=ML²T⁻¹; [mₑ]=M; [e²/4πε₀]=ML³T⁻²; dimensional equations: M: β+γ=0; L: 2α+3γ=1; T: −α−2γ=0
- Concrete numbers: solving: γ=−1, β=1, α=2; a₀ = ℏ²/(mₑ·e²/4πε₀) = (1.055×10⁻³⁴)²/(9.11×10⁻³¹ × 2.31×10⁻²⁸) = 5.29×10⁻¹¹ m = 0.529 Å; fine structure constant α = e²/(4πε₀ℏc) ≈ 1/137
- The artifact / what moves: three constant-blocks with dimension labels; algebraic manipulation animated step by step — mass cancels, time cancels, length equations solved; final result: unique power-law combination with dimension of length; numerical computation shown
- Output medium: Manim (mp4)
- Two testable predictions: P1: any attempt to build a length from ℏ and mₑ alone (without e²/4πε₀) fails — no purely quantum-mechanical length exists without the electromagnetic coupling; P2: a₀ = λ_C/α where λ_C = ℏ/(mₑc) = 3.86×10⁻¹³ m and α = 1/137, giving a₀ = 3.86×10⁻¹³ × 137 = 5.29×10⁻¹¹ m ✓
- The change: replace the central charge with Ze (hydrogen-like ions) — a₀ scales as 1/Z; helium nucleus Z=2 gives orbital radius half the Bohr radius, uranium Z=92 gives 0.006 Å
- Human supplies (Claude can't): Nothing — fully synthetic/analytic
- Teardown angle: classical physics predicts no atomic size — the electron spirals in to r=0; the Bohr radius exists only because ℏ ≠ 0; dimensional analysis makes this visible without solving a single differential equation
- Exclusions: Bohr model circular orbits; quantum defects; relativistic corrections
- Sim slug: dimensional-analysis-bohr-radius
- Score: 8/10

---

## Candidate 19 — Explore: Band Gap Explorer — Fourier Coefficients and Energy Gaps
- Source: `quantum-mechanics-vol5/chapters/05-fourier-series-and-the-wave-equation.md` (LLM Exercise 8)
- Topic: Bloch Theorem · Band Gap · Fourier Coefficient
- Lane: D3/DATAVIZ (emergent / interactive)
- Hook: The energy gap at a Brillouin zone boundary is exactly 2|V₁| — twice the first Fourier coefficient of the periodic potential. Slide V₁ and watch the gap open and close. Slide a (lattice spacing) and watch which k-states get split.
- The rule: V(x) = V₀ + 2V₁cos(2πx/a); gap at k=π/a is 2|V₁|; free-electron dispersion E=ℏ²k²/2m; at k=π/a two degenerate states mix; eigenvalues are (ℏ²π²/2ma²) ± |V₁|
- Concrete numbers: a=0.5 nm (silicon-like), mₑ; free-electron energy at k=π/a: E₀ = ℏ²π²/(2mₑa²) ≈ 6.0 eV; V₁ = 0.5 eV → gap = 1.0 eV; V₁ = 1.0 eV → gap = 2.0 eV; gap independent of V₀
- The artifact / what moves: dispersion curve E(k) from k=−2π/a to k=2π/a showing parabolic free-electron curve; add periodic potential → avoided crossings appear at zone boundaries; sliders for V₁, V₂ (second harmonic), a; gap widths labeled; density of states panel updates in real time
- Output medium: d3 v7 animated/interactive HTML
- Two testable predictions: P1: gap at first Brillouin zone boundary (k=π/a) is exactly 2|V₁| — set V₁=0.5 eV and gap reads 1.0 eV; set V₁=1.0 eV and gap reads 2.0 eV; P2: setting V₁=0 (V₂ only) leaves first zone boundary gap at exactly 0, while gap at second zone boundary (k=2π/a) opens as 2|V₂| — proving each gap is controlled by one specific Fourier coefficient
- The change: add V₂ slider (second harmonic) — only affects gap at k=2π/a, leaving first gap unchanged; demonstrates that each Fourier coefficient couples one specific pair of degenerate free-electron states
- Human supplies (Claude can't): Nothing — fully synthetic/analytic
- Teardown angle: band gaps are not a property of the lattice geometry — they are set by the Fourier coefficients of the potential; change V₁ and you change the gap, not the band structure topology
- Exclusions: Wannier functions; tight-binding model; spin-orbit coupling; topological bands
- Sim slug: band-gap-fourier-explorer
- Score: 9/10
- Status: BUILT — `open /Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-vol5/youtube/band-gap-fourier-explorer/band-gap-fourier-explorer.html`

---

## Candidate 20 — Animate: Gaussian Wave Packet Spreading — The Fourier Width in Time
- Source: `quantum-mechanics-vol5/chapters/06-the-fourier-transform.md`
- Topic: Wave Packet · Dispersion · Fourier Bandwidth
- Lane: MANIM (directed animation)
- Hook: A perfectly localized electron starts as a narrow Gaussian and spreads inevitably — not because of measurement, not because of interaction, but because Fourier width in momentum means different velocity components. Watch Δx(t) grow as √(1 + t²/τ²).
- The rule: ψ(x,t) = ∫ φ̃(p) e^{i(px−p²t/2mℏ)/ℏ} dp/(2πℏ)^{1/2}; for Gaussian φ̃(p): Δx(t) = Δx(0)√(1 + (ℏt/2mΔx(0)²)²); spreading time τ = 2mΔx(0)²/ℏ
- Concrete numbers: electron, Δx(0) = 1 nm → τ = 2×9.11×10⁻³¹×(10⁻⁹)²/1.055×10⁻³⁴ ≈ 17 fs; at t=τ: Δx = √2 nm; at t=2τ: Δx = √5 nm ≈ 2.24 nm; macroscopic ball Δx(0)=10⁻¹⁰ m, m=1 g: τ ≈ 10²⁰ s (longer than age of universe)
- The artifact / what moves: |ψ(x,t)|² animated over time — Gaussian spreading and flattening; envelope width Δx(t) shown as bracket growing with √(1+t²/τ²); center moving at group velocity v_g = p₀/m; momentum space |φ̃(p)|² shown fixed — it never changes
- Output medium: Manim (mp4)
- Two testable predictions: P1: Δx(t) = Δx(0)√2 at exactly t = τ = 2mΔx(0)²/ℏ; P2: momentum-space width |φ̃(p)|² remains exactly constant in time (dispersion relation preserves Fourier amplitude magnitudes); the spreading is purely phase, not amplitude, in momentum space
- The change: double the initial width Δx(0) → 2 nm — spreading time increases by 4× (quadratic dependence), demonstrating that wider initial packets spread more slowly
- Human supplies (Claude can't): Nothing — fully synthetic/analytic
- Teardown angle: wavepacket spreading is not a quantum quirk — it is the classical consequence of different-frequency components traveling at different speeds; it would happen to a classical pulse too in a dispersive medium
- Exclusions: squeezed states; quantum Zeno effect; decoherence
- Sim slug: gaussian-wavepacket-spreading
- Score: 9/10

---

## Candidate 21 — Explore: Sturm-Liouville Orthogonality Gallery — One Theorem, Six Families
- Source: `quantum-mechanics-vol5/chapters/11-special-functions.md`
- Topic: Sturm-Liouville · Orthogonal Polynomials · Special Functions
- Lane: D3/DATAVIZ (emergent / interactive)
- Hook: Hermite, Legendre, Laguerre — three completely different polynomials, three completely different ODEs — but ONE orthogonality proof. Click through the families and watch the same two-line argument apply each time, just with a different weight function.
- The rule: ∫ yₘ(x) yₙ(x) w(x) dx = 0 for m≠n; Sturm-Liouville operator is self-adjoint with weight w; eigenfunctions at different eigenvalues are w-orthogonal; for Hermite: w=e^{−ξ²}; for Legendre: w=1 on [−1,1]; for Laguerre: w=e^{−ρ}ρ^k
- Concrete numbers: Legendre: ∫₋₁¹ P₂(u)P₃(u)du = ∫₋₁¹ [(3u²−1)/2][(5u³−3u)/2]du = 0 (verifiable by expanding); Hermite: ∫₋∞^∞ H₁(ξ)H₃(ξ)e^{−ξ²}dξ = 0; normalization ∫ H₂² e^{−ξ²}dξ = √π·4·2! = 8√π
- The artifact / what moves: tabs for each family (Hermite, Legendre, Laguerre, Bessel, Chebyshev, spherical harmonics); for each, interactive plot of first 5 polynomials; orthogonality matrix shown as color heatmap (off-diagonal should be 0); click two polynomials and watch their weighted product integrate to zero in real time
- Output medium: d3 v7 animated/interactive HTML
- Two testable predictions: P1: for any two distinct Legendre polynomials Pₘ, Pₙ the heatmap shows ∫₋₁¹ PₘPₙdu = 0 (off-diagonal zero); diagonal entry = 2/(2n+1); P2: for Hermite polynomials H₀ and H₂: ∫(1)(4ξ²−2)e^{−ξ²}dξ = 4·(√π/2) − 2√π = 0 exactly — verifiable
- The change: switch weight function to a non-Sturm-Liouville one (e.g., w=1 for Hermite) — the orthogonality integral becomes nonzero, demonstrating that the weight function is essential
- Human supplies (Claude can't): Nothing — fully synthetic/analytic
- Teardown angle: there are not six different orthogonality theorems — there is one theorem applied to six weight functions; Sturm-Liouville is the unifying engine behind all of them
- Exclusions: completeness proof; Gram-Schmidt from special functions; numerical quadrature
- Sim slug: sturm-liouville-orthogonality-gallery
- Score: 8/10
- Status: BUILT — `open /Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-vol5/youtube/sturm-liouville-orthogonality-gallery/sturm-liouville-orthogonality-gallery.html`

---

## Candidate 22 — Animate: 3D Infinite Square Well — Degeneracy from Symmetry
- Source: `quantum-mechanics-vol5/chapters/10-multivariable-calculus-and-separation-of-variables.md`
- Topic: 3D Box · Degeneracy · Quantum Numbers
- Lane: MANIM (directed animation)
- Hook: In 3D, energy levels that are distinct in 1D can fuse into a single degenerate level. E_{211} = E_{121} = E_{112} exactly — all three wavefunctions have different shapes but identical energies. Watch the degeneracy emerge from cubic symmetry.
- The rule: E_{nₓnᵧn_z} = (ℏ²π²/2mL²)(nₓ²+nᵧ²+n_z²); degeneracy = number of (nₓ,nᵧ,n_z) triples with the same n²=nₓ²+nᵧ²+n_z²; each permutation of a triple gives a different spatial wavefunction with the same energy
- Concrete numbers: ground state (1,1,1): E=3E₁, degeneracy=1; first excited (2,1,1) and permutations: E=6E₁, degeneracy=3; (2,2,1) and permutations: E=9E₁, degeneracy=3; (3,1,1) also sums to 11, but (2,2,2) sums to 12, not 11
- The artifact / what moves: energy ladder showing degenerate multiplets as horizontal bands; 3D isosurface plots of ψ_{nₓnᵧn_z} for each degenerate partner — visually different spatial patterns at the same energy height; arrows showing which permutations correspond to the same energy
- Output medium: Manim (mp4)
- Two testable predictions: P1: any permutation of (nₓ,nᵧ,n_z) gives identical energy — E_{211} = E_{121} = E_{112} exactly from nₓ²+nᵧ²+n_z² = 4+1+1 = 6 in all three cases; P2: the first non-degenerate excited level (after the 3-fold degenerate first excited) occurs for (2,2,1) and permutations at n²=9, then a non-degenerate (3,1,1) fails since 9+1+1=11 ≠ 4+4+1=9; find the first accidental degeneracy at (3,2,1) sharing n²=14 with… no partner — confirming most degeneracies are exact symmetry degeneracies
- The change: deform the cube into a rectangular box (Lx≠Ly) — the 3-fold degeneracy of (2,1,1) splits into two separate levels; shows that symmetry breaking lifts degeneracy
- Human supplies (Claude can't): Nothing — fully synthetic/analytic
- Teardown angle: degeneracy is not a coincidence — it is a consequence of spatial symmetry; breaking the symmetry lifts it; this is the mathematical root of fine structure in hydrogen
- Exclusions: hydrogen degeneracy from hidden SO(4) symmetry; Stark and Zeeman effects; crystal field splitting
- Sim slug: 3d-box-degeneracy-symmetry
- Score: 8/10
