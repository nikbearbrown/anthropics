# Math for Physics Vol 2 — Simulation Ideas

## Candidate 01 — Fourier Transform Bandwidth: the Slit Paradox Made Visible
- Source: `math-for-physics-vol-2/chapters/06-fourier-transforms-and-their-physics.md`
- Topic: Fourier Transform — Bandwidth Relation (Δx · Δk ≥ 1/2)
- Lane: MANIM (directed animation)
- Hook: Make the slit narrower and the diffraction pattern gets *wider* — the opposite of what every beginner expects. Watch the mathematical reason happen in real time.
- The rule: Top-hat aperture of width a transforms to sinc(ka/2); first zero at k = 2π/a, so central peak width ∝ 1/a. The Gaussian f(x) = exp(−x²/2a²) transforms to exp(−a²k²/2) and saturates Δx · Δk = 1/2.
- Concrete numbers: Slit widths a = 1.0, 0.5, 0.25 (arbitrary units). At a = 1.0: first zero at k = 2π ≈ 6.28; at a = 0.5: first zero at k = 4π ≈ 12.57. Halving the slit exactly doubles the peak width.
- The artifact / what moves: Three panels run in parallel (or sequentially). Left: a top-hat aperture with sliders showing width a. Right: the sinc²(ka/2) diffraction pattern. As a is halved, the central lobe visibly doubles in width. A running label shows the first-zero position and confirms 1/a scaling. Final beat: switch to a Gaussian pair — narrow Gaussian in x, wide Gaussian in k — and display Δx · Δk = 0.50 (exactly saturated).
- Output medium: Manim (mp4)
- Two testable predictions: P1: At a = 1.0 the first zero of sinc(ka/2) falls at k = 2π ≈ 6.283; at a = 0.5 it falls at k = 4π ≈ 12.566 — exact 2× shift, verifiable from the formula. P2: The Gaussian f(x) = exp(−x²/2a²) has position width Δx = a/√2 and momentum width Δk = 1/(a√2), so their product Δx · Δk = 1/2 regardless of a — the bound is saturated exactly, and no other shape can do better.
- The change: Switch aperture to a square pulse of narrower width — watch the first-zero position jump outward and secondary lobes appear; then switch to a Gaussian which eliminates all side lobes at the cost of smoother falloff.
- Human supplies (Claude can't): Nothing — fully analytic/synthetic
- Teardown angle: Every diffraction lab demo lives in the physics hall. The math is one line: narrow → wide because the Fourier pair forces it. The Gaussian is the minimum — it cannot be beaten.
- Exclusions: Do not animate the integral derivation of the transform; do not include the Dirac delta. Stay in the time-domain/k-domain amplitude picture.
- Sim slug: math-fourier-bandwidth-slit-paradox
- Score: 10/10

## Candidate 02 — Normal Modes of Two Coupled Carts: Eigenvalues as Frequencies
- Source: `math-for-physics-vol-2/chapters/04-vector-spaces-eigenvalues-and-diagonalization.md`
- Topic: Normal Modes — Stiffness-Matrix Eigenvalue Problem
- Lane: MANIM (directed animation)
- Hook: Two carts connected by three springs look hopelessly complicated — each drives the other. But there exist exactly two special starting conditions where both carts oscillate at one pure frequency. Miss them by a millimeter and the motion becomes a confusing beat pattern.
- The rule: Stiffness matrix K = [[2k, −k],[−k, 2k]] (equal masses m); eigenvalue equation det(K − mω²I) = 0 gives ω₁² = k/m (in-phase, middle spring unstretched) and ω₂² = 3k/m (out-of-phase, middle spring maximally stretched). Mode shapes (1,1)/√2 and (1,−1)/√2 — orthogonal eigenvectors.
- Concrete numbers: m = 1 kg, k = 4 N/m. ω₁ = 2 rad/s (T₁ = π ≈ 3.14 s); ω₂ = 2√3 ≈ 3.46 rad/s (T₂ = π/√3 ≈ 1.81 s). Beat period for a general motion: T_beat = 2π/(ω₂ − ω₁) = 2π/(3.46 − 2.00) ≈ 4.30 s.
- The artifact / what moves: Two carts slide on a frictionless track. Walls anchor outer springs; a middle spring connects carts. Act 1: pure in-phase mode — both carts oscillate identically at ω₁ = 2 rad/s. Act 2: pure out-of-phase mode — carts oscillate oppositely at ω₂ = 3.46 rad/s. Act 3: one cart displaced by 1, other not — the superposition plays out as a visible beat, energy sloshing from one cart to the other with period 4.30 s. A matrix panel shows the stiffness matrix and its two eigenvalues live.
- Output medium: Manim (mp4)
- Two testable predictions: P1: In-phase mode frequency ω₁ = √(k/m) = 2.00 rad/s; out-of-phase mode ω₂ = √(3k/m) = 3.46 rad/s — exact ratio √3 ≈ 1.732, verifiable by measuring animation cycles. P2: When only cart 1 is displaced (a₁ = 1, a₂ = 0), the amplitude envelope on each cart follows cos((ω₂ − ω₁)t/2) in time — energy returns completely to cart 1 every T_beat ≈ 4.30 s.
- The change: Triple the middle-spring stiffness to k_mid = 3k (outer springs remain k). Watch ω₂ shift upward while ω₁ stays fixed — because the in-phase mode never stretches the middle spring, so its stiffness cannot affect that mode.
- Human supplies (Claude can't): Nothing — fully analytic/synthetic
- Teardown angle: The "complicated" motion is just two pure tones. Diagonalizing the stiffness matrix is the only calculation needed; the carts are the eigenvectors made physical.
- Exclusions: Do not add damping; do not label every spring constant with a moving number. Keep the matrix display minimal.
- Sim slug: math-normal-modes-coupled-carts-eigenvalues
- Score: 9/10

## Candidate 03 — Lorentz Boost as Hyperbolic Rotation: Rapidity and the Saturation of Speed
- Source: `math-for-physics-vol-2/chapters/10-the-mathematics-of-special-relativity.md`
- Topic: Rapidity — β = tanh φ and the Velocity-Addition Formula
- Lane: MANIM (directed animation)
- Hook: You add 0.75c and 0.75c and expect 1.50c. You get 0.96c. That is not a patch. Rapidities add exactly. Watch tanh saturate, and see why light speed can never be reached.
- The rule: tanh φ = β = v/c; rapidities add linearly φ_total = φ₁ + φ₂; velocity addition formula β_total = tanh(φ₁ + φ₂) = (β₁ + β₂)/(1 + β₁β₂). The β = tanh φ curve rises linearly near origin, bends toward the asymptote β = 1.
- Concrete numbers: β₁ = β₂ = 0.75c: φ = tanh⁻¹(0.75) ≈ 0.9730; φ_total = 1.9459; β_total = tanh(1.9459) ≈ 0.9600. The naive sum 1.50c is replaced by 0.96c. For β = 0.99c: φ = tanh⁻¹(0.99) ≈ 2.647; adding five such boosts gives φ = 13.24, β = tanh(13.24) → 0.99999... — still below 1.
- The artifact / what moves: A Cartesian plane with β (0 to 1) on the y-axis and φ (rapidity) on the x-axis. The β = tanh φ curve is drawn and labeled. Two marked points show φ₁ = φ₂ = 0.973 (for 0.75c). An animated arrow slides along the rapidity axis: φ₁ is marked, then φ₁ + φ₂ is added — the rapidity tip advances on the x-axis, then drops down to the curve to read off β_total = 0.96. A second beat shows the same for ten boosts of 0.5c each — the rapidity sum grows linearly, but the velocity saturates at 0.999c, never reaching 1.
- Output medium: Manim (mp4)
- Two testable predictions: P1: Two boosts of β = 0.75c give β_total = tanh(2 × 0.9730) = tanh(1.9459) = 0.9600 — not 1.50c and not 0.90c, but exactly 0.9600, verifiable by plugging into the velocity-addition formula. P2: Adding N identical boosts of rapidity φ_0 gives β_N = tanh(Nφ_0). For φ_0 = tanh⁻¹(0.5) = 0.5493, five boosts give φ_5 = 2.747 and β_5 = tanh(2.747) ≈ 0.9915 — still below 1, no matter how many are added.
- The change: Switch from equal boosts to one enormous boost β → 0.9999c. Rapidity is tanh⁻¹(0.9999) ≈ 4.60 — finite. Adding any finite rapidity to it changes nothing visible in β. The curve is so flat near 1 that even doubling the rapidity only changes the seventh decimal place.
- Human supplies (Claude can't): Nothing — fully analytic/synthetic
- Teardown angle: The velocity-addition formula is infamous for looking unmotivated. Rapidity makes it tautological — tanh(A+B) is the tangent addition formula. The saturation at c is not a law, it is the geometry of tanh.
- Exclusions: Do not draw the Minkowski spacetime diagram; do not animate the Lorentz boost matrix. Stay on the β-vs-φ curve.
- Sim slug: math-lorentz-rapidity-speed-saturation
- Score: 9/10

## Candidate 04 — Brachistochrone Cycloid vs. Straight Line: the Fastest Descent
- Source: `math-for-physics-vol-2/chapters/11-calculus-of-variations-and-lagrangian-hamiltonian.md`
- Topic: Euler–Lagrange Equation — Brachistochrone Solution
- Lane: MANIM (directed animation)
- Hook: The shortest path is a straight line. The fastest path is not. A ball rolling on a cycloid beats a ball rolling on the straight chord — every time, without exception.
- The rule: T[y] = ∫√((1+y'²)/(2gy)) dx is minimized by the cycloid x = R(φ − sin φ), y = R(1 − cos φ). The straight-line descent time between the same two endpoints is always longer; the cycloid wins by a computable factor.
- Concrete numbers: Endpoint A = (0, 0), endpoint B = (π R, 2R) with R = 0.5 m. Cycloid descent time T_cyc = π√(R/g) = π√(0.5/9.81) ≈ 0.709 s. Straight-line descent: path length = √((πR)² + (2R)²) ≈ 1.854 m at R = 0.5 m; average speed calculation gives T_line ≈ 0.866 s. The cycloid wins by about 18%.
- The artifact / what moves: A frame shows endpoints A (upper left) and B (lower right). Three paths are drawn: the straight chord (grey dashed), a circular arc (blue), and the cycloid (red). Three beads are released simultaneously from A. The cycloid bead reaches B first despite traveling a longer path — it builds speed early by dropping steeply, which more than compensates for the extra distance. A timer shows each bead's arrival time. The cycloid wins every time.
- Output medium: Manim (mp4)
- Two testable predictions: P1: With R = 0.5 m and g = 9.81 m/s², the cycloid descent time is π√(R/g) = π × 0.2257 ≈ 0.709 s — a single exact formula, verifiable from the parametric equations. P2: The straight-line descent time between the same pair of endpoints is longer. For the specific geometry above (A to B = (πR, 2R)), the line length is √(π²+4) × R ≈ 1.854 × 0.5 = 0.927 m; using kinematics the straight-line time is approximately 0.866 s > 0.709 s.
- The change: Move endpoint B lower (increase R) — the cycloid's advantage grows with steeper descent angles. Move B almost directly below A — the cycloid and straight line nearly coincide and the timing difference shrinks.
- Human supplies (Claude can't): Nothing — fully analytic/synthetic (parametric equations exact)
- Teardown angle: Bernoulli threw this challenge to "the sharpest mathematicians in the world" in 1696. The straight line loses to a curve that most people cannot even name. The Euler–Lagrange equation delivers the answer in about ten lines of algebra.
- Exclusions: Do not derive the Euler–Lagrange equation on screen. Do not animate the variational perturbation δy. Show the race, not the derivation.
- Sim slug: math-brachistochrone-cycloid-descent
- Score: 9/10

## Candidate 05 — Eigenvector Grid Deformation: the Directions a Matrix Cannot Rotate
- Source: `math-for-physics-vol-2/chapters/04-vector-spaces-eigenvalues-and-diagonalization.md`
- Topic: Eigenvalues and Eigenvectors — 2×2 Symmetric Matrix
- Lane: MANIM (directed animation)
- Hook: A matrix rotates almost every vector it touches. But two directions survive unmoved — they only stretch. If you know which two, you instantly understand the whole transformation.
- The rule: A = [[2,1],[1,2]]. Eigenvalues λ₁ = 3, λ₂ = 1. Eigenvectors v₁ = (1,1)/√2 (stretched by 3), v₂ = (1,−1)/√2 (stretched by 1). A generic vector is rotated AND stretched; an eigenvector is only stretched.
- Concrete numbers: v = (1, 0): Av = (2, 1) — direction changes, magnitude changes. v₁ = (1/√2, 1/√2): Av₁ = (3/√2, 3/√2) = 3v₁ — direction unchanged, magnitude tripled. v₂ = (1/√2, −1/√2): Av₂ = (1/√2, −1/√2) = v₂ — direction unchanged, magnitude preserved.
- The artifact / what moves: A 2D grid is drawn. The matrix A acts on the grid — the grid deforms. Before deformation: arrows at many grid points show the direction of the input vector. After: arrows show where A sends each vector. A generic arrow (pointing at 30°) visibly rotates AND stretches. Then the two eigenvector arrows are highlighted: one along (1,1) — it only stretches by 3×, no rotation. One along (1,−1) — it stays unchanged (scale 1). A slow "eigenvalue sweep" shows how grid squares distort everywhere except along those two axes.
- Output medium: Manim (mp4)
- Two testable predictions: P1: A vector pointing along (1,1)/√2 is mapped to (3/√2, 3/√2)/√2 = (1,1) × 3/√2... more precisely Av₁ = 3v₁ — a tripling with no angular change. P2: det(A) = λ₁ × λ₂ = 3 × 1 = 3; tr(A) = λ₁ + λ₂ = 2 + 2 = 4 = 3 + 1. Both can be checked directly from the matrix entries — providing two independent verification handles.
- The change: Switch to a rotation matrix R(45°) — which has NO real eigenvectors. The grid still deforms but every arrow spins; no direction is preserved. Contrast makes the symmetric matrix's special property vivid.
- Human supplies (Claude can't): Nothing — fully analytic/synthetic
- Teardown angle: A linear transformation's whole character is encoded in two numbers and two directions. Diagonalization is the change of coordinates in which "complicated" becomes "trivial."
- Exclusions: Do not show the characteristic polynomial derivation on screen. Do not animate Gram-Schmidt. One matrix, two eigenvectors, one grid deformation.
- Sim slug: math-eigenvector-grid-deformation-symmetric
- Score: 8/10

## Candidate 06 — Gaussian Wave Packet: Position-Momentum Width Tradeoff
- Source: `math-for-physics-vol-2/chapters/06-fourier-transforms-and-their-physics.md`
- Topic: Fourier Transform — Minimum Uncertainty State (Δx · Δk = 1/2)
- Lane: MANIM (directed animation)
- Hook: Squeezing a wave packet in position forces it to spread in momentum — and the product can never go below 1/2. The Gaussian is the unique shape that hits the floor.
- The rule: ψ(x) = (πa²)^(−1/4) exp(−x²/2a²); its Fourier transform is ψ̃(k) ∝ exp(−a²k²/2). Width in x: Δx = a/√2. Width in k: Δk = 1/(a√2). Product: Δx · Δk = 1/2 (minimum uncertainty state, saturates the Gabor limit).
- Concrete numbers: Show a = 2.0: Δx = 2/√2 = 1.414, Δk = 1/(2√2) = 0.354, product = 0.500. Then a = 0.5: Δx = 0.354, Δk = 1.414, product = 0.500. Then a = 0.1: Δx = 0.071, Δk = 7.07, product = 0.500. The product is invariant under scaling.
- The artifact / what moves: Two panels: left shows ψ(x) in position space, right shows |ψ̃(k)|² in momentum space. A slider controls the width parameter a. As a decreases (packet narrows in x), the right panel visibly spreads in k. Numerical labels show Δx, Δk, and Δx · Δk in real time. At every value of a, the product reads 0.500. A superimposed horizontal line marks the Gabor floor.
- Output medium: Manim (mp4)
- Two testable predictions: P1: At a = 1.0, the Gaussian has Δx = 1/√2 ≈ 0.707 and its transform has Δk = 1/√2 ≈ 0.707, product = 0.500 — exact, with no rounding. P2: A top-hat function of the same half-width a gives Δx · Δk > 0.5 (it exceeds the Gaussian minimum). Specifically, for a rectangular pulse of half-width a/√3 (same rms width), the transform has heavier tails and a larger Δk, so the product exceeds 0.5 — the Gaussian is demonstrably the unique minimizer.
- The change: Replace the Gaussian with a top-hat: the k-space profile becomes sinc-shaped (with side lobes), and the product rises above 0.5, confirming the Gaussian is special.
- Human supplies (Claude can't): Nothing — fully analytic/synthetic
- Teardown angle: The Heisenberg uncertainty principle is often presented as a physics axiom. It is a theorem about Fourier pairs — and the Gaussian is its tightest proof.
- Exclusions: Do not animate the derivation of the Gaussian transform (complete-the-square integral). Show the result and the tradeoff.
- Sim slug: math-gaussian-wave-packet-uncertainty
- Score: 8/10

## Candidate 07 — Gradient as Steepest Ascent: Navigating a Potential Landscape
- Source: `math-for-physics-vol-2/chapters/03-vector-calculus-and-field-theorems.md`
- Topic: Gradient — Direction of Steepest Increase of a Scalar Field
- Lane: MANIM (directed animation)
- Hook: Stand anywhere on a hilly surface. Which direction rises fastest? There is exactly one answer at every point — and a vector field labels it everywhere at once. That field is the gradient.
- The rule: ∇f = (∂f/∂x, ∂f/∂y) points in the direction of steepest increase of f; magnitude |∇f| is the rate of increase in that direction. Level curves are perpendicular to ∇f. Electric field E = −∇V (the field points downhill on the potential surface).
- Concrete numbers: f(x,y) = sin(x)cos(y). At point (π/4, 0): ∇f = (cos(π/4)cos(0), −sin(π/4)sin(0)) = (1/√2, 0) ≈ (0.707, 0) — gradient points purely in +x. At (0, 0): ∇f = (1, 0). At (π/4, π/4): ∇f = (cos(π/4)cos(π/4), −sin(π/4)sin(π/4)) = (1/2, −1/2) — 45° diagonal direction.
- The artifact / what moves: A colored 2D surface (heatmap) of f(x,y) = sin(x)cos(y). Superimposed: the gradient field drawn as arrows at a grid of points — arrows point in the direction of steepest ascent, lengths proportional to |∇f|. Dashed level curves (contour lines) are drawn crossing the gradient arrows at 90° — the orthogonality is visible. An animated particle is released at a local minimum and follows the gradient uphill (gradient ascent), tracing the path of steepest ascent to the nearest maximum.
- Output medium: Manim (mp4)
- Two testable predictions: P1: At the point (π/2, 0), ∇f = (cos(π/2) cos(0), −sin(π/2) sin(0)) = (0, 0) — a critical point (saddle or extremum). The gradient arrow vanishes exactly there, which is the visual prediction. P2: The gradient is always perpendicular to the level curves f = const. At any point on the level curve f = 0.5, the gradient arrow drawn there must be at exactly 90° to the tangent of that level curve — verifiable by measuring the angle in the animation.
- The change: Switch f to an electrostatic potential V(x,y) = 1/r around a point charge at the origin. The gradient −∇V gives the radial electric field E ∝ r̂/r² — outward arrows that get longer as r increases. The level curves become circles (equipotentials), perpendicular to the field lines everywhere.
- Human supplies (Claude can't): Nothing — fully analytic/synthetic
- Teardown angle: "Steepest ascent" sounds qualitative. The gradient makes it a precise vector. Every machine-learning optimizer runs on this idea — it is the mathematical engine of gradient descent.
- Exclusions: Do not derive the divergence theorem. Do not show Stokes' theorem. Stay with the 2D gradient and level curves only.
- Sim slug: math-gradient-steepest-ascent-potential
- Score: 7/10

## Candidate 08 — Poisson Distribution and √N: Why Counting Experiments Improve Slowly
- Source: `math-for-physics-vol-2/chapters/08-probability-and-statistics-for-physics.md`
- Topic: Poisson Distribution — σ² = μ and the √N Counting Rule
- Lane: MANIM (directed animation)
- Hook: Count 100 radioactive decays — uncertainty is ±10. Count 10,000 — uncertainty is ±100. To halve the relative error, you need four times as many counts. That is the iron law of every counting experiment in physics, astronomy, and medical imaging.
- The rule: Poisson distribution P(k) = λᵏe^(−λ)/k! has mean μ = λ and variance σ² = λ, so σ = √λ. The relative uncertainty is σ/μ = 1/√λ. To achieve relative uncertainty ε, one must count N = 1/ε² events.
- Concrete numbers: λ = 100: σ = 10, relative uncertainty = 10%. λ = 400: σ = 20, relative uncertainty = 5% (halved by 4× counts). λ = 10,000: σ = 100, relative uncertainty = 1%. Rule: doubling precision costs 4× time.
- The artifact / what moves: A bar chart of the Poisson distribution for increasing λ = 1, 4, 16, 100. At each λ, the distribution is shown alongside a Gaussian overlay (since large-λ Poisson converges to Gaussian). The ±σ = ±√λ band is shaded. A separate animated panel shows relative uncertainty σ/μ = 1/√λ plotted vs. λ on a log-log scale — a straight line of slope −1/2, confirming the √N rule. A running label counts a simulated decaying source and shows the relative error shrinking as counts accumulate.
- Output medium: Manim (mp4)
- Two testable predictions: P1: At λ = 25, the Poisson distribution P(k = 25) = 25^25 e^(−25)/25! ≈ 0.0796; the Gaussian approximation N(25, 5) gives f(25) = 1/(5√2π) ≈ 0.0798 — within 0.3%, confirming rapid convergence. P2: The relative uncertainty σ/μ = 1/√λ; to reach 1% precision (σ/μ = 0.01), one needs λ = 10,000 counts. The log-log slope of σ/μ vs. λ is exactly −1/2, confirmed by the animation's straight line.
- The change: Add two Poisson variables with means λ₁ and λ₂: the sum has mean λ₁ + λ₂ and variance λ₁ + λ₂ (variances add). Show that combining two detectors reduces relative uncertainty by √2 — the same rule, applied to parallel counting.
- Human supplies (Claude can't): Nothing — fully analytic/synthetic
- Teardown angle: The √N rule appears as a recipe in every physics lab manual. This animation shows it is a theorem — the variance-equals-mean property of the Poisson distribution derived from the rare-event limit of the binomial.
- Exclusions: Do not derive the binomial or the central limit theorem. Start from the Poisson distribution and its moments. Do not show the partition function or thermodynamics connection.
- Sim slug: math-poisson-sqrt-n-counting-rule
- Score: 7/10
