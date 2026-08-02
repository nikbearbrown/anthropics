# Mathematical Methods for Physics — CLI Video Ideas ("X with Claude")

## Candidate 01 — Animate Solving the Harmonic Oscillator ODE with Claude

- Source: math-for-physics/chapters/11-differential-equations-and-oscillatory-motion.md
- Lane: BUILD (Claude Code)
- Hook: The mass-spring equation ẍ = -ω²x looks like a function whose second derivative is its negative — and the answer is cosine. Watch Claude derive it by the characteristic-equation method, then animate the phase portrait.
- The artifact: a Python script using sympy to solve the ODE ẍ + ω²x = 0 symbolically, display the general solution x(t) = A·cos(ωt) + B·sin(ωt), then animate: (1) the displacement x(t) over 3 periods, (2) the phase portrait (x vs. ẋ) as an ellipse being traced in real time. Parameters: ω=2, A=1, B=0.5.
- Prompt seed: `claude "Use sympy to solve the ODE x'' + 4*x = 0 (omega=2). Display the general solution. Set A=1, B=0.5. Then animate two subplots: 1) x(t) from t=0 to 3*pi, 2) the phase portrait (x vs x') as the trajectory traces an ellipse. Mark t=0 as a red dot. Title: 'Harmonic Oscillator: Position and Phase Portrait'. Save as mp4."`
- Read / check: Verify general solution x(t) = A·cos(2t) + B·sin(2t). Check x'(t) = -2A·sin(2t) + 2B·cos(2t). Confirm the phase portrait is an ellipse (not a spiral — no damping). Verify the red starting dot moves correctly. Check period T = π is visible in the animation.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim or screen-recording mp4 (dual-panel animated ODE solution + phase portrait)
- The change: Add damping (ẍ + 2γẋ + ω²x = 0) with γ=0.3 and show the phase portrait spiraling inward — demonstrating underdamped behavior and exponential decay envelope.
- Teardown angle: The characteristic equation method works because exponentials are eigenfunctions of differentiation. When you assume x=e^{rt}, the ODE becomes an algebraic equation — this is the fundamental trick that makes linear ODEs tractable.
- Exclusions: Full derivation from first principles; driven oscillator; resonance; Laplace transforms.
- Score: 9/10

---

## Candidate 02 — Plot a Wave Equation Solution: Superposition and Standing Waves with Claude

- Source: math-for-physics/chapters/14-partial-derivatives-wave-equation-and-fourier.md
- Lane: BUILD (Claude Code)
- Hook: Two waves traveling in opposite directions interfere to produce standing waves — fixed nodes, oscillating antinodes. Claude derives y(x,t) = sin(kx)·cos(ωt) from the wave equation and animates the string.
- The artifact: a Python script that: (1) animates y(x,t) = sin(πx/L)·cos(2πt) for a string of length L=1, t from 0 to 2 periods, (2) marks nodes (x=0, L) as fixed points, (3) overlays the +/- envelope sin(πx/L). Second animation shows two traveling waves y₁ = 0.5·sin(kx-ωt) and y₂ = 0.5·sin(kx+ωt) and their sum — demonstrating superposition.
- Prompt seed: `claude "Animate two things using matplotlib: 1) A standing wave y = sin(pi*x)*cos(2*pi*t) on [0,1] for t=0 to 2. Mark nodes at x=0 and x=1 as red dots. Draw the +/- envelope. 2) Show the sum of two traveling waves y1 = 0.5*sin(pi*x - 2*pi*t) and y2 = 0.5*sin(pi*x + 2*pi*t), animated simultaneously with their sum. Save both animations as mp4."`
- Read / check: Verify y₁ + y₂ = sin(πx)·cos(2πt) (standing wave from superposition). Check nodes at x=0, 1 are stationary throughout. Verify the envelope sin(πx) is the max amplitude at each x. Confirm two-panel layout is clear.
- Human supplies: Nothing — fully synthetic. The traveling-wave solution is analytic.
- Output medium: screen-recording mp4 (dual-panel animated wave simulation)
- The change: Add a third harmonic (2nd mode): y = sin(2πx)·cos(4πt) and animate the superposition of 1st + 2nd modes showing the resulting complex waveform.
- Teardown angle: The wave equation is linear, so superposition holds exactly — any sum of solutions is a solution. This is why a plucked string sounds complex: it vibrates in many modes simultaneously, and Fourier series is the tool that decomposes the sound.
- Exclusions: 2D wave equation; electromagnetic waves; quantum mechanical wave packets.
- Score: 9/10

---

## Candidate 03 — Visualize the Dot and Cross Product: Alignment and Twist with Claude

- Source: math-for-physics/chapters/04-vectors-and-vector-algebra.md
- Lane: BUILD (Claude Code)
- Hook: The dot product measures how much two vectors align. The cross product measures how much they twist. Same two vectors, two numbers, two completely different geometric facts. Claude animates both for rotating vectors.
- The artifact: a Manim 3D animation: two vectors A and B in 3D space. As angle θ between them rotates from 0 to 2π, animate: (1) A·B = |A||B|cosθ plotted as a cosine curve in a side panel, (2) |A×B| = |A||B|sinθ plotted as a sine curve in another side panel, (3) the cross product direction vector rotating perpendicular to both.
- Prompt seed: `claude "Create a Manim 3D animation: Vector A = [2,0,0] fixed. Vector B rotates in the xy-plane from 0 to 2*pi. Animate: 1) In 3D: the cross product A x B as a perpendicular arrow, 2) Left panel: A·B vs theta as a cosine curve drawing from left to right, 3) Right panel: |A x B| vs theta as a sine curve. Title: 'Dot Product: Alignment. Cross Product: Twist.'"`
- Read / check: Verify A·B = 2·cosθ for |A|=|B|=1. Verify |A×B| = 2·sinθ for |A|=|B|=1 when B is in the xy-plane. Confirm the cross product direction is always the z-axis for this configuration. Check the cosine and sine curves match the 3D animation.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim 3D (animated rotating vector with dual side-panel plots)
- The change: Use two non-perpendicular, non-parallel vectors in 3D and show the cross product direction via the right-hand rule animation — making the 3D orientation concrete.
- Teardown angle: The dot product collapses two vectors to a scalar (losing direction, keeping alignment). The cross product collapses two vectors to a new vector (keeping orientation, measuring the "lever arm"). They answer orthogonal questions about the same pair.
- Exclusions: Scalar triple product; vector triple product identity; general tensors.
- Score: 9/10

---

## Candidate 04 — Animate Fourier Series Building a Square Wave with Claude

- Source: math-for-physics/chapters/14-partial-derivatives-wave-equation-and-fourier.md
- Lane: BUILD (Claude Code)
- Hook: A square wave is "obviously" not sinusoidal — yet it's exactly equal to an infinite sum of sine waves. Watch each harmonic being added, and watch Gibbs phenomenon appear at the edges.
- The artifact: a Manim animation starting with a fundamental sine wave, then adding the 3rd, 5th, 7th, ... harmonics one at a time. After each addition, the running sum is overlaid on the target square wave. The Gibbs overshoot at discontinuities appears around the 20th harmonic. Final panel shows 50-harmonic approximation.
- Prompt seed: `claude "Animate a Fourier series approximation of a square wave: f(x) = sum_{n=1,3,5,...} (4/(n*pi)) * sin(n*x). Start with n=1 and add each odd harmonic up to n=49. For each step: show the new harmonic added (gray, faint), the running sum (blue), and the target square wave (red dashed). Animate with a half-second pause after each harmonic. Save as mp4."`
- Read / check: Verify coefficients: 4/(nπ) for n=1,3,5,...  Verify at x=0, the series converges to 0 (midpoint of jump). Check the Gibbs overshoot at discontinuities (≈9% overshoot visible by n=21). Confirm the running sum visually approaches the square wave.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim (animated harmonic-addition sequence)
- The change: Switch to a sawtooth wave and show different coefficients — demonstrating that Fourier series works for any periodic function, not just square waves.
- Teardown angle: Gibbs phenomenon is permanent — it doesn't go away with more harmonics, it just gets narrower. This matters for signal processing: you cannot eliminate all ringing near a step discontinuity with a finite Fourier series.
- Exclusions: Fourier transform (continuous); FFT algorithm; spectral leakage.
- Score: 9/10

---

## Candidate 05 — Animate the Gradient as Steepest Ascent with Claude

- Source: math-for-physics/chapters/14-partial-derivatives-wave-equation-and-fourier.md
- Lane: BUILD (Claude Code)
- Hook: The gradient of a scalar field points in the direction of steepest increase — like a compass for climbing. Claude plots a 2D potential surface and animates gradient descent finding the minimum.
- The artifact: a Manim or matplotlib animation: (1) plot z = sin(x)·cos(y) as a 3D surface, (2) animate gradient arrows ∇f = (cos(x)cos(y), -sin(x)sin(y)) at a grid of points, (3) animate a particle following gradient descent from a starting point, tracing the path to the nearest minimum.
- Prompt seed: `claude "Plot f(x,y) = sin(x)*cos(y) as a 3D surface using matplotlib. In a 2D contour subplot, animate: 1) gradient arrows at a 5x5 grid of points, 2) a gradient descent path starting from (x0,y0) = (1,0.5), taking 50 steps with learning rate 0.1. Color the path red. Animate arrows appearing first, then the path tracing step by step. Save as mp4."`
- Read / check: Verify gradient ∇f = (cos(x)cos(y), -sin(x)sin(y)) analytically. Confirm gradient descent path moves downhill (decreasing f values). Check learning rate 0.1 converges without oscillation. Verify the path terminates near a local minimum.
- Human supplies: Nothing — fully synthetic. The function is analytic.
- Output medium: screen-recording mp4 (dual-panel 3D surface + 2D gradient descent animation)
- The change: Show gradient ascent (maximize instead of minimize) and demonstrate the mountain-climbing interpretation — showing that gradient direction is both uphill and the direction ∇V field points in electrostatics.
- Teardown angle: The gradient is the most information-efficient descriptor of a scalar field — one vector tells you both the direction and magnitude of steepest change. This is why neural network training (backpropagation) uses gradient descent, and why E = -∇V in electrostatics.
- Exclusions: Hessian; second-order methods; stochastic gradient descent.
- Score: 8/10

---

## Candidate 06 — Simulate Exponential Decay and Half-Life with Claude

- Source: math-for-physics/chapters/11-differential-equations-and-oscillatory-motion.md
- Lane: BUILD (Claude Code)
- Hook: Radioactive decay obeys dN/dt = -λN. Claude derives the solution N(t) = N₀e^{-λt} by separation of variables, then animates decay curves for three different isotopes with very different half-lives.
- The artifact: a Python script that: (1) uses sympy to solve dN/dt = -lambda*N symbolically, (2) animates three decay curves on the same axes for isotopes with T_{1/2} = 1 day, 1 year, 5730 years (scaled), (3) marks the half-life point on each with a dashed horizontal line at N₀/2.
- Prompt seed: `claude "Use sympy to solve the ODE N' = -lambda*N symbolically. Show the general solution N(t) = N0*exp(-lambda*t). Then animate three decay curves on the same normalized plot (N/N0 vs t/T_half) for: T_half = 1, 5, 20 (normalized units). Mark the half-life (N/N0 = 0.5) with a horizontal dashed line. Label each curve with its half-life. Save as mp4."`
- Read / check: Verify λ = ln(2)/T_{1/2}. At t = T_{1/2}, confirm N/N₀ = 0.5. Check sympy's symbolic solution matches N₀·e^{-λt}. Confirm all three curves intersect the N/N₀=0.5 line at t/T_{1/2}=1. Verify normalized plot makes curves directly comparable.
- Human supplies: Nothing — fully synthetic.
- Output medium: screen-recording mp4 (animated multi-curve normalized decay plot)
- The change: Add a "daughter product" accumulation curve: D(t) = N₀(1 - e^{-λt}) — showing the decay product growing as the parent decays, demonstrating conservation.
- Teardown angle: Separation of variables transforms a differential equation into two simple integrals. This technique works whenever the equation separates into f(N)dN = g(t)dt — a large class of physically important equations.
- Exclusions: Decay chains; Bateman equations; quantum mechanical tunneling.
- Score: 8/10

---

## Candidate 07 — Build a Log-Log Kepler's Third Law Plotter with Claude

- Source: math-for-physics/chapters/05-functions-graphs-and-power-laws.md
- Lane: BUILD (Claude Code)
- Hook: Plot planetary orbital period vs. semi-major axis on log-log axes and you get a straight line with slope 3/2 — this is Kepler's third law T² ∝ a³ made visible. The data points for all 8 planets lie exactly on the line.
- The artifact: a Python script that loads planetary data (a in AU, T in years), plots T vs. a on log-log axes, fits a power law using numpy.polyfit on log data, displays the slope (should be ≈ 1.5), and animates the planets appearing one by one from Mercury to Neptune with labels.
- Prompt seed: `claude "Plot Kepler's Third Law for the solar system. Data: Mercury(a=0.387, T=0.241), Venus(0.723, 0.615), Earth(1.0, 1.0), Mars(1.524, 1.881), Jupiter(5.203, 11.86), Saturn(9.537, 29.46), Uranus(19.19, 84.01), Neptune(30.07, 164.8). Plot T vs a on log-log axes. Fit a power law (polyfit on log data). Display slope. Animate planets appearing in order. Title: 'Kepler's Third Law: T^2 proportional to a^3'. Save as mp4."`
- Read / check: Verify slope ≈ 1.5 (i.e., log T ≈ 1.5 log a). Verify all 8 planets' data points lie on the fitted line. Confirm log-log axes are correctly labeled. Check the fit residuals are small (good law fit). Verify planetary data is correct.
- Human supplies: Nothing — fully synthetic. Planetary data is public knowledge.
- Output medium: screen-recording mp4 (animated log-log scatter + power law fit)
- The change: Add asteroid Ceres (a=2.77, T=4.60) and Pluto (a=39.48, T=247.9) — showing the law extends beyond classical planets.
- Teardown angle: A straight line on log-log axes IS a power law — this is not an approximation but an exact mathematical equivalence. The slope is the exponent. This is why log-log plots are the diagnostic tool for power laws in data.
- Exclusions: Derivation of Kepler's law from Newton's gravity; elliptical orbit mechanics; perturbation theory.
- Score: 8/10

---

## Candidate 08 — Animate Taylor Series Convergence with Claude

- Source: math-for-physics/chapters/13-series-expansions-and-approximations.md
- Lane: BUILD (Claude Code)
- Hook: e^x is its own Taylor series — and the approximation gets better with each term. Watch the partial sums converge to the exact curve, and watch the "radius of convergence" spreading outward with each term added.
- The artifact: a Manim animation that: starting with the constant term (1), adds x, x²/2!, x³/3!, ... up to x¹⁰/10!. After each term is added, the partial sum curve is drawn on the same axes as e^x. The regions where the approximation is good vs. bad are highlighted.
- Prompt seed: `claude "Create a Manim animation of the Taylor series for e^x. Start with y=1. Add each term x^n/n! for n=1 to 10. After each addition, plot the partial sum in blue and e^x in red on [-3, 3]. Shade the region where |error| < 0.01 in green. Show the current term being added. Title: 'Taylor Series for e^x: 10 Terms'. Save as mp4."`
- Read / check: Verify the 10-term approximation is accurate to <1% for |x| < 2.5. Confirm each partial sum is the correct polynomial. Check the green "accurate" region expands with more terms. Verify e^x in red is correctly plotted.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim (animated series convergence with accuracy region)
- The change: Compare convergence of sin(x) Taylor series vs. e^x Taylor series — showing that sin's alternating signs cause faster apparent convergence for small x.
- Teardown angle: Taylor series show that every smooth function is locally a polynomial. The radius of convergence tells you how far from the center the polynomial approximation remains useful — this is the bridge between local and global function behavior.
- Exclusions: Laurent series; complex analysis; generating functions.
- Score: 8/10

---

## Candidate 09 — Visualize Complex Exponentials and Euler's Formula with Claude

- Source: math-for-physics/chapters/12-complex-numbers-and-exponentials.md
- Lane: BUILD (Claude Code)
- Hook: e^{iθ} = cos(θ) + i·sin(θ) is the most surprising fact in mathematics. Claude animates the complex exponential tracing a circle in the complex plane, and shows how it encodes oscillation.
- The artifact: a Manim animation: a point e^{iθ} traces the unit circle in the complex plane as θ goes from 0 to 2π. Simultaneously: (1) the real part Re(e^{iθ}) = cos(θ) is projected onto the x-axis and plotted as a time series, (2) the imaginary part Im(e^{iθ}) = sin(θ) is projected onto the y-axis and plotted. Final frame: Euler's identity e^{iπ} + 1 = 0 highlighted.
- Prompt seed: `claude "Create a Manim animation of Euler's formula: e^(i*theta) traces the unit circle as theta goes from 0 to 2*pi. Simultaneously animate: 1) The complex plane with the point moving on the unit circle, 2) Left panel: cos(theta) plotted as theta grows (projection onto real axis), 3) Right panel: sin(theta) plotted (projection onto imaginary axis). End with e^(i*pi) = -1 highlighted. Save as mp4."`
- Read / check: Verify at θ=0: point=(1,0), cos=1, sin=0. At θ=π/2: point=(0,1), cos=0, sin=1. At θ=π: point=(-1,0), cos=-1, sin=0. Confirm both sine and cosine plots match the projections. Verify the period is correct (2π). Check e^{iπ}=-1 is highlighted at θ=π.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim (animated complex plane + dual projection plots)
- The change: Show how e^{(σ+iω)t} for σ<0 traces a decaying spiral — connecting to the damped oscillator and demonstrating that complex exponentials encode both oscillation and decay.
- Teardown angle: Euler's formula is not a coincidence — it follows from matching Taylor series of e^z, sin(z), cos(z) in the complex plane. The "most beautiful equation" in mathematics is a direct consequence of how these three functions relate via their series.
- Exclusions: Riemann surface of complex log; analytic continuation; residue theorem.
- Score: 8/10

---

## Candidate 10 — Compute Eigenvalues of a Coupled Oscillator System with Claude

- Source: math-for-physics/chapters/10-linear-systems-and-matrices.md
- Lane: BUILD (Claude Code)
- Hook: Two coupled masses on springs have confused motion — energy sloshing back and forth. But in the eigenvector basis, they are two independent oscillators. Claude finds the eigenvalues, reveals the normal modes, and animates both.
- The artifact: a Python script using numpy to compute eigenvalues and eigenvectors of the coupled oscillator stiffness matrix [[-2, 1],[1,-2]] (for equal masses and spring constants). Displays ω₁ = 1 and ω₂ = √3. Then animates: (1) the two normal modes (in-phase and out-of-phase), (2) a general superposition showing beat oscillation.
- Prompt seed: `claude "Two coupled oscillators: K = np.array([[-2,1],[1,-2]]) (stiffness matrix, masses=1). Use numpy.linalg.eig to find eigenvalues and eigenvectors. Print the natural frequencies omega = sqrt(-eigenvalue). Animate two subplots: 1) Mode 1 (in-phase): both masses moving together at omega1=1, 2) Mode 2 (out-of-phase): masses moving oppositely at omega2=sqrt(3). Then animate the superposition beat oscillation. Save as mp4."`
- Read / check: Verify eigenvalues of K are -1 and -3, giving ω₁=1, ω₂=√3. Confirm eigenvectors are [1,1]/√2 (in-phase) and [1,-1]/√2 (out-of-phase). Verify the superposition shows beat frequency |ω₂-ω₁| ≈ 0.73 rad/s. Confirm animation shows two distinct modes.
- Human supplies: Nothing — fully synthetic.
- Output medium: screen-recording mp4 (animated dual normal mode + beat superposition)
- The change: Add damping (imaginary parts to eigenvalues) and show the modes decaying — demonstrating that complex eigenvalues encode both frequency and decay rate.
- Teardown angle: The eigenvector basis decouples the system — in the right coordinates, a coupled problem becomes two independent problems. This is the central payoff of linear algebra: the right basis makes complexity disappear.
- Exclusions: Generalized eigenvalue problem; continuous normal modes; quantum mechanics of coupled systems.
- Score: 8/10
