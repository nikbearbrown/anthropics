# Math for Physics — Simulation Ideas

## Candidate 01 — Secant Lines Converging to the Tangent: the Derivative Born

- Source: `math-for-physics/chapters/06-limits-and-the-derivative.md`
- Topic: The Derivative as a Limit
- Lane: MANIM (directed animation)
- Hook: The speedometer reads a definite speed at one instant — yet dividing zero displacement by zero time is meaningless. Watch the paradox resolve in real time.
- The rule: `f'(t) = lim_{h→0} (f(t+h)−f(t))/h` — the difference quotient for `f(t) = t²`, evaluated at `t = 2`
- Concrete numbers: `t = 2`, `h` steps: 1.0, 0.5, 0.25, 0.1, 0.01; secant slopes converge to `f'(2) = 4`
- The artifact / what moves: A parabola `x(t) = t²` is drawn. A point is fixed at `t = 2`. A second point slides toward it from the right; the secant line through both pivots toward the tangent, and a running label shows the slope closing in on 4.0.
- Output medium: Manim (mp4)
- Two testable predictions: P1: At `h = 1` the secant slope is `(9−4)/1 = 5`; at `h = 0.1` it is `(4.41−4)/0.1 = 4.1` — both verifiable by arithmetic. P2: The secant slope for `f(t) = t²` at any `t` converges exactly to `2t` — so at `t = 3` the same animation would converge to 6.
- The change: Switch `f` to `f(t) = t³`; the secant converges to `3t²` — the power rule made visible for a new exponent.
- Human supplies (Claude can't): Nothing — fully synthetic/analytic
- Teardown angle: Every calculus textbook draws this picture; almost no student watches it move. The convergence is shockingly clean when animated — the "ghost of departed quantities" dissolving in real time.
- Exclusions: Do not add epsilon-delta formalism; do not animate the symbolic algebra of expanding `(t+h)²` — the visual is the limit, not the algebra.
- Sim slug: math-secant-to-tangent-derivative
- Score: 8/10

---

## Candidate 02 — Fourier Series Building Harmonic by Harmonic: the Square Wave

- Source: `math-for-physics/chapters/14-partial-derivatives-wave-equation-and-fourier.md`
- Topic: Fourier Series — Superposition of Harmonics
- Lane: MANIM (directed animation)
- Hook: A square wave has corners, yet you build it entirely from smooth sines. Watch the corners materialize one harmonic at a time — and the overshoot at every jump that never goes away.
- The rule: Square wave = `(4/π)[sin(ω₀t) + (1/3)sin(3ω₀t) + (1/5)sin(5ω₀t) + …]` — only odd harmonics, amplitudes falling as `1/n`
- Concrete numbers: `ω₀ = 2π` (period 1 s); show `N = 1, 3, 5, 7, 13` partial sums; at `N = 13` the central peak of the Gibbs overshoot is `≈ 8.9%` above the square wave's flat top (the Gibbs constant `≈ 1.089`).
- The artifact / what moves: A dashed square wave sits in the background. Successive sine harmonics are added one at a time; with each addition the partial sum waveform snaps closer to the square. The Gibbs overshoot at the jump persists and sharpens but never shrinks below `≈ 9%`.
- Output medium: Manim (mp4)
- Two testable predictions: P1: The first partial sum `(4/π)sin(ω₀t)` has amplitude `4/π ≈ 1.273` — verifiable exactly. P2: Adding the 5th harmonic produces a partial sum with 5 lobes between 0 and 1; the Gibbs overshoot is always `≈ 8.9%` regardless of how many terms are added (Wilbraham–Gibbs phenomenon, constant `≈ 9%`).
- The change: Switch to a triangle wave (`sin − (1/9)sin3 + (1/25)sin5 …`); the corners now converge faster (amplitudes fall as `1/n²`) and the Gibbs overshoot disappears — continuity is what killed it.
- Human supplies (Claude can't): Nothing — fully synthetic/analytic
- Teardown angle: Every instrument's timbre is its Fourier recipe; a clarinet vs. a violin playing the same note differs only in which harmonics are loud. The animation makes "sound is a sum of sines" viscerally concrete.
- Exclusions: Do not animate the coefficient integral formula; do not show frequency-domain bar charts (that is D3 territory). Stay in time-domain waveform space.
- Sim slug: math-fourier-series-square-wave
- Score: 10/10

---

## Candidate 03 — Damped Oscillator: Three Regimes of a Discriminant

- Source: `math-for-physics/chapters/11-differential-equations-and-oscillatory-motion.md`
- Topic: Damped Harmonic Oscillator — Characteristic Equation
- Lane: MANIM (directed animation)
- Hook: One quadratic decides whether the mass oscillates, slumps, or rockets back as fast as physics allows. Watch the three regimes emerge as a single parameter crosses two thresholds.
- The rule: `mẍ + bẋ + kx = 0`; characteristic roots `r = (−b ± √(b²−4mk))/(2m)`; three cases determined by discriminant `Δ = b²−4mk`
- Concrete numbers: `m = 1 kg`, `k = 100 N/m` (so `ω₀ = 10 rad/s`); vary `b` through: underdamped `b = 4` (Δ < 0), critically damped `b = 20` (Δ = 0), overdamped `b = 40` (Δ > 0). Underdamped oscillation frequency `ω' = √(ω₀²−(b/2m)²) = √(100−4) ≈ 9.8 rad/s`.
- The artifact / what moves: A single displacement-vs-time axis. As a slider for `b` sweeps from 0 to 50, a curve traces live: at low `b` a decaying sinusoid, at `b = 20` a single exponential hump returning fastest without crossing zero, at high `b` a slow exponential return. The discriminant value and regime label update beside the plot.
- Output medium: Manim (mp4)
- Two testable predictions: P1: At critical damping `b = 20`, `Δ = 400 − 4(1)(100) = 0` exactly — one repeated root `r = −10`. P2: In the underdamped case at `b = 4`, the quasi-period is `T' = 2π/ω' ≈ 0.641 s`, slightly longer than the undamped `T₀ = 2π/10 ≈ 0.628 s` — the damping slows the oscillation.
- The change: Fix `b` at underdamped and animate the complex-plane location of the roots as `b` increases — the roots move from purely imaginary (undamped) toward the real axis, collide at the critical value, and then split along the real axis. A geometric picture of the regime transition.
- Human supplies (Claude can't): Nothing — fully synthetic/analytic
- Teardown angle: Car shock absorbers are designed for critical damping — the fastest return to zero without bouncing. The math decides the engineering spec; the discriminant is the design constraint.
- Exclusions: Do not animate the spring-mass apparatus itself; the focus is the solution curve's shape, not the mechanical diagram. Do not introduce the driven (forced) oscillator — that is a separate animation.
- Sim slug: math-damped-oscillator-three-regimes
- Score: 9/10

---

## Candidate 04 — Taylor Series Convergence: Sine Approximations Widening Out

- Source: `math-for-physics/chapters/13-series-expansions-and-approximations.md`
- Topic: Taylor Series — Convergence and the Small-Angle Approximation
- Lane: MANIM (directed animation)
- Hook: The "small-angle approximation" is not a guess — it is exact truncation with a quantified error. Watch each extra term buy you more territory, and feel the approximation's domain expand.
- The rule: `sin x = x − x³/3! + x⁵/5! − x⁷/7! + …`; each partial sum is a polynomial approximation of increasing degree
- Concrete numbers: Show partial sums `N = 1` (line), `N = 3` (cubic), `N = 5` (5th degree), `N = 7`; at `x = π/4 ≈ 0.785 rad` the 1-term error is `≈ 6.1%`, the 3-term error is `≈ 0.12%`, the 5-term error `< 0.001%`. The 1-term (small-angle) approximation is good to 1% at `θ ≈ 0.245 rad ≈ 14°`.
- The artifact / what moves: A single axes showing the true `sin x` curve (dashed). The 1-term polynomial `y = x` draws first; then a button (or automatic sequence) adds terms, and each new curve extends its close-tracking region farther from the origin before peeling away. A running "error at x = 1 rad" counter shows the error shrink with each term.
- Output medium: Manim (mp4)
- Two testable predictions: P1: At `x = π/2`, the 1-term approximation gives `π/2 ≈ 1.571`, but `sin(π/2) = 1.000` — a 57% error; the 3-term gives `1.571 − 0.646 + 0.080 = 1.004`, a 0.4% error. Both exact and checkable. P2: Each successive polynomial tracks `sin x` well out to roughly `x ≈ N^{1/2}` radians (heuristic), so the 7-term polynomial stays good past `x = π`. Verify: 7-term sum at `x = π` gives `π − π³/6 + π⁵/120 − π⁷/5040 ≈ 0.0` to three decimal places (since `sin π = 0`).
- The change: Animate `e^x` partial sums; all coefficients are positive (no alternation), so the approximation lies above the true curve on one side — a qualitatively different convergence behavior that reveals the alternating-sign role in `sin`.
- Human supplies (Claude can't): Nothing — fully synthetic/analytic
- Teardown angle: Every calculator on the planet computes `sin` by summing this series (or a Chebyshev variant). The approximation you "assume" in intro physics is the first term of the exact answer — and you can always compute the next term to know your error.
- Exclusions: Do not animate the coefficient derivation by repeated differentiation. Do not show the pendulum nonlinear vs. linear comparison (that is a separate sim). Stay focused on the waveform convergence picture.
- Sim slug: math-taylor-sine-convergence
- Score: 9/10

---

## Candidate 05 — Standing Waves on a Fixed String: Modes One Through Four

- Source: `math-for-physics/chapters/14-partial-derivatives-wave-equation-and-fourier.md`
- Topic: Standing Waves — Normal Modes of a Vibrating String
- Lane: MANIM (directed animation)
- Hook: Nodes are forever. Pluck the string anywhere and these patterns are the only ones that survive; everything else is their sum. Watch a fixed string support only integer harmonics.
- The rule: Standing wave modes `y_n(x,t) = 2A sin(nπx/L) cos(nω₀t)`, with `f_n = nv/(2L)` and `n = 1, 2, 3, …`
- Concrete numbers: `L = 0.65 m`, `v = 427 m/s` (guitar E-string from the chapter's worked example); `f₁ = 329 Hz`, `f₂ = 658 Hz`, `f₃ = 987 Hz`, `f₄ = 1316 Hz`. Mode 2 has one interior node at `x = L/2`; mode 3 has two nodes at `x = L/3` and `2L/3`.
- The artifact / what moves: A horizontal string is drawn. Mode 1 oscillates as a single arch, then mode 2 appears (two arches oscillating in opposition), then 3 and 4. Nodes are highlighted as fixed points. A frequency counter and mode label accompany each. A final beat shows all four modes superimposed — the rich waveform a real guitar string produces.
- Output medium: Manim (mp4)
- Two testable predictions: P1: Mode `n` has exactly `n−1` interior nodes. At mode 4, nodes sit at `x = L/4, L/2, 3L/4` — three fixed points that can be verified by direct substitution into `sin(4πx/L) = 0`. P2: Frequency ratios are exact integers: `f₂/f₁ = 2`, `f₃/f₁ = 3`, `f₄/f₁ = 4` — the harmonic series, verifiable by the formula `fₙ = nv/(2L)`.
- The change: Superpose modes 1 and 3 only (as a "node selection" plucking): the combined waveform has a node permanently at `x = L/2` even though it contains two frequency components. This is why touching the string at its midpoint (flageolet) suppresses even harmonics.
- Human supplies (Claude can't): Nothing — fully synthetic/analytic
- Teardown angle: The harmonic series is not a metaphor — these are the literal allowed frequencies of a stretched string, enforced by boundary conditions. The math explains why an E-string on a guitar always sounds like an E.
- Exclusions: Do not derive the wave equation derivation (that is ch. 14 lecture territory). Do not animate traveling waves — focus only on the standing patterns.
- Sim slug: math-standing-waves-guitar-string
- Score: 8/10

---

## Candidate 06 — Centripetal Acceleration from a Rotating Vector: the `v²/r` Derivation

- Source: `math-for-physics/chapters/07-differentiation-in-motion.md`
- Topic: Circular Motion — Centripetal Acceleration from Vector Differentiation
- Lane: MANIM (directed animation)
- Hook: The speedometer never moves, yet the pilot is being slammed sideways at 8g. Watch `v²/r` emerge from two differentiations of a circle.
- The rule: `r(t) = r[cos(ωt)î + sin(ωt)ĵ]`; differentiate twice → `a(t) = −ω²r(t)`, so `aₓ = v²/r` pointing toward center
- Concrete numbers: `r = 229 m`, `v = 134 m/s` (the jet's 8g turn from the chapter); `ω = v/r ≈ 0.585 rad/s`; centripetal acceleration `aₓ = v²/r = 134²/229 ≈ 78.4 m/s² = 8g`
- The artifact / what moves: A point traces a circle at constant speed. The position vector `r(t)` is drawn from center to point; the velocity vector `v(t)` is drawn tangent to the circle (perpendicular to `r`). The acceleration vector `a(t)` appears pointing back to center, rotating as the point moves. A label shows `|a| = v²/r = const`, confirming the magnitude is constant even as the direction rotates.
- Output medium: Manim (mp4)
- Two testable predictions: P1: `v(t) · r(t) = 0` at every instant (velocity is always perpendicular to radius) — verifiable algebraically: `(−rω sin ωt)(r cos ωt) + (rω cos ωt)(r sin ωt) = 0`. P2: The speed `|v| = rω = 134 m/s` is constant throughout the motion, even though the acceleration vector has magnitude `78.4 m/s²` — speed constant, acceleration nonzero; both checkable from the formulas.
- The change: Let `ω` increase gradually (angular acceleration); show that the acceleration vector tilts away from purely centripetal and gains a tangential component, illustrating the difference between centripetal and angular acceleration.
- Human supplies (Claude can't): Nothing — fully synthetic/analytic
- Teardown angle: The misconception "constant speed means no acceleration" collapses the moment you watch the velocity vector rotating. The derivative sees the rotation even when the magnitude does not change.
- Exclusions: Do not animate the chain-rule algebra on screen; the visual is the vector diagram. Do not add a force-body diagram of the aircraft.
- Sim slug: math-centripetal-acceleration-rotating-vector
- Score: 8/10

---

## Candidate 07 — Spring-Mass Oscillation: Amplitude, Period, and the Independence Surprise

- Source: `math-for-physics/chapters/11-differential-equations-and-oscillatory-motion.md`
- Topic: Simple Harmonic Oscillator — Period Independent of Amplitude
- Lane: MANIM (directed animation)
- Hook: Pull the spring twice as far — the mass swings twice as wide, but the clock doesn't change. Period is immune to amplitude. Watch the cosine solution prove it.
- The rule: `x(t) = A cos(ωt)` with `ω = √(k/m)`, `T = 2π/ω = 2π√(m/k)` — no `A` in `T`
- Concrete numbers: `m = 2.00 kg`, `k = 32.0 N/m`, `ω = 4.00 rad/s`, `T = π/2 ≈ 1.571 s`. Show releases at `A = 0.020 m`, `A = 0.040 m`, `A = 0.080 m` — triple the amplitude range.
- The artifact / what moves: Three cosine curves launch simultaneously from their respective amplitudes (small, medium, large). All three complete their first cycle at exactly the same time. A vertical line sweeps from left to right showing the period ticks — all three curves cross zero at identical moments. A label "T = 1.57 s regardless of A" appears.
- Output medium: Manim (mp4)
- Two testable predictions: P1: At the concrete numbers, `T = 2π/4.00 = 1.5708 s` — all three amplitudes return to their starting position simultaneously at this exact time. P2: The maximum speed `v_max = Aω` varies with amplitude (0.080, 0.160, 0.320 m/s for the three cases) while the period does not — so the large-amplitude mass moves faster but takes the same time to complete its cycle.
- The change: Now use the actual (nonlinear) pendulum with identical release energies. At small angle the period matches the harmonic prediction; at larger angles (`45°`, `90°`) the period grows (`T ≈ T₀(1 + θ₀²/16)` from the chapter's correction formula), breaking the amplitude-independence. Shows why "small angle" is mandatory.
- Human supplies (Claude can't): Nothing — fully synthetic/analytic
- Teardown angle: This is why pendulum clocks work — the period is amplitude-independent to first order, so the clock ticks steadily even as the pendulum winds down. It is not incidental; it is the entire design principle.
- Exclusions: Do not simulate the spring-mass apparatus physically. Do not add phase portraits. Focus entirely on the three overlapping cosine curves and the period coincidence.
- Sim slug: math-shm-amplitude-independence
- Score: 8/10

---

## Candidate 08 — Power Law Log-Log Straightening: Reading an Exponent as a Slope

- Source: `math-for-physics/chapters/05-functions-graphs-and-power-laws.md`
- Topic: Power Laws and Log-Log Plots
- Lane: MANIM (directed animation)
- Hook: The free-fall data looks like a messy curve — until you take the log. Then it snaps to a line and the slope reads off the exponent. Watch a parabola become a ruler.
- The rule: `y = ax^b` → `log y = b·log x + log a`; a power law is linear on log-log axes with slope `b`
- Concrete numbers: Free-fall `d = 4.9t²` at `t = 1, 2, 5, 10, 20, 50, 100 s`; log-log slope = `Δ(log d)/Δ(log t) = (log 49000 − log 4.9)/(log 100 − log 1) = 4/2 = 2.000` exactly. Also show the same transformation applied to `F ∝ v²` (stopping distance).
- The artifact / what moves: Two side-by-side axes. Left: linear axes showing the curve `d = 4.9t²` — clearly curved. Right: log-log axes on which the same points appear; as the transformation animates, each data point migrates from linear to log-log coordinates and lands on a perfectly straight line. A slope-measurement triangle appears and the number "2.0" is read off.
- Output medium: Manim (mp4)
- Two testable predictions: P1: On the log-log plot the slope is exactly `2.0` — rising 4 log-decades in `d` over 2 log-decades in `t`; verifiable from the data table in the chapter. P2: If the exponent were `b = 1/2` (pendulum period vs. length), the log-log slope would be `0.5` — the graph would rise one decade for every two decades in `L`. Both are exact predictions of the log-log formula.
- The change: Animate a second dataset that is exponential (`y = e^{0.5x}`) on the same pair of axes — show it is straight on semi-log but curved on log-log, demonstrating the clean diagnostic separation between power law and exponential.
- Human supplies (Claude can't): Nothing — fully synthetic/analytic
- Teardown angle: Kepler read `T² ∝ r³` (slope 3/2) from a log-log plot of planetary data three centuries before anyone knew why. The tool doesn't care about the physics; the slope is the exponent every time.
- Exclusions: Do not show metabolic scaling or the contested 3/4 exponent — that invites a biology detour. Stay with clean physics examples where the exponent is unambiguous.
- Sim slug: math-power-law-loglog-slope
- Score: 7/10

---

## Candidate 09 — Phasor Rotation: Oscillation as the Shadow of a Rotating Arrow

- Source: `math-for-physics/chapters/12-complex-numbers-and-exponentials.md`
- Topic: Euler's Formula — Oscillation as the Real Part of a Phasor
- Lane: MANIM (directed animation)
- Hook: A cosine wave is nothing but a spinning arrow's shadow on the wall. Watch `e^{iωt}` rotate and project its real part — and watch two phasors add like vectors to produce a phase-shifted cosine in one step.
- The rule: `e^{iωt} = cos(ωt) + i·sin(ωt)`; `Re(Ae^{iφ}·e^{iωt}) = A cos(ωt + φ)`. Phasor addition: `A₁∠φ₁ + A₂∠φ₂` in the complex plane gives resultant amplitude and phase.
- Concrete numbers: From Example 2 in the chapter: `x₁ = 3cos(ωt)`, `x₂ = 4cos(ωt + 90°)`. Phasors: `Ã₁ = 3`, `Ã₂ = 4i`. Sum: `3 + 4i` — modulus `= 5`, argument `= arctan(4/3) = 53.1°`. Result: `x₁ + x₂ = 5cos(ωt + 53.1°)`.
- The artifact / what moves: Left panel: unit circle in the complex plane. A rotating arm (`e^{iωt}`) traces the circle; a horizontal projection drops down and draws out `cos(ωt)` on a time axis to the right. Right panel: two phasor arrows (`3+0i` and `0+4i`) are placed; a third arrow (their sum `3+4i`) is drawn, showing the resultant amplitude `5` and angle `53.1°` — the cosine sum falls out geometrically.
- Output medium: Manim (mp4)
- Two testable predictions: P1: The phasor `3+4i` has modulus `√(9+16) = 5` and argument `arctan(4/3) = 53.13°` — exact and verifiable. P2: The projection of `e^{iπ/2}` onto the real axis is `cos(π/2) = 0`; onto the imaginary axis is `sin(π/2) = 1` — Euler's formula at a specific checkable angle.
- The change: Show a decaying phasor `e^{(−γ+iω)t}`: the arm spirals inward as it rotates, and its real-axis projection traces a decaying cosine — the underdamped oscillator in one symbol.
- Human supplies (Claude can't): Nothing — fully synthetic/analytic
- Teardown angle: AC circuit engineers do every impedance calculation with phasors. The "imaginary" number is the most practical tool they have — it replaces a page of trig identities with a right-triangle calculation.
- Exclusions: Do not derive Euler's formula from the Taylor series in the animation — the visual is the geometric picture. Do not animate the full damped-oscillator derivation; the spiral phasor is the hint, not the derivation.
- Sim slug: math-phasor-rotation-euler
- Score: 8/10
