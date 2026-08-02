# math-calculus — Vox Explainer Video Candidates

Scout run: 2026-07-09. Chapters scanned: 01–06. Cards below scored ≥ 8/10.

---

## Candidate 01 — Why the Speed of Light Is a Calculus Problem

- Source: `math-calculus/chapters/02-limits.md`
- Topic: CALCULUS
- Hook: Einstein's mass formula gives a perfectly defined, perfectly useful answer as you approach the speed of light — and then fails to exist at the speed of light. How can "approaching" give a real answer while "arriving" gives nothing at all?
- Key case: Relativistic mass $m = m_0 / \sqrt{1 - v^2/c^2}$ at $v = 0.9c$, $0.99c$, $0.999c$ — each step costs more, the formula blows up at $v = c$, yet the behavior is completely determined.
- The Question: How can a formula have no value at a point yet tell you everything about what happens near it?
- Core idea: A limit is not the value of a function at a point — it is the behavior of the function near a point. These are different questions, and keeping them separate is the conceptual engine of all of calculus. The limit exists in the approach, not the arrival.
- Visual object: A single curve of $m/m_0$ vs. $v/c$ climbing steeply toward a vertical asymptote at $v = c$, with a zoom sequence showing the function values at $0.9c$, $0.99c$, $0.999c$ converging without ever touching the wall.
- Manim move: accumulate (values piling toward the asymptote), then trace (the curve from low speed to near-$c$)
- Example seed: At $v = 0.9c$ the object is 2.3× heavier than at rest. At $0.99c$, 7×. At $0.999c$, 22×. The formula is telling you exactly how the cost grows — while simultaneously refusing to give any answer at $v = c$ itself. The limit exists; the function value does not.
- Length band: 3–5 min
- Still lanes: geo/c2v
- Prerequisites: Basic algebra; comfortable reading a formula with a square root.
- Exclusions: Epsilon-delta formalism; one-sided vs. two-sided limit taxonomy; squeeze theorem.
- Score: 10/10

---

## Candidate 02 — The Theorem That Connected Everything: Why Differentiation and Integration Are Inverses

- Source: `math-calculus/chapters/05-integration.md`
- Topic: CALCULUS
- Hook: The derivative is a local concept — it asks what is happening at a single instant. The integral is a global concept — it asks what has accumulated over an entire interval. These sound completely unrelated. They are the same operation, run in opposite directions.
- Key case: A cyclist's varying speed over one hour. The derivative of position gives speed; integrating speed recovers position. The running total of an accumulation function has a rate of change exactly equal to the rate being accumulated.
- The Question: Why does knowing the instantaneous rate at every point give you the total accumulation — and why did it take 150 years after Newton and Leibniz to explain why this is true?
- Core idea: The accumulation function $F(x) = \int_a^x f(t)\,dt$ has $F'(x) = f(x)$: differentiating the running total recovers exactly the thing being accumulated. This local-global equivalence is the Fundamental Theorem of Calculus, and it turns limit-of-sums computation into antiderivative evaluation.
- Visual object: Two side-by-side timelines — left: the rate function $f(t)$ (cyclist speed), right: the accumulated area $F(x)$ growing in real time — with a moving vertical cursor on the left instantaneously matching the slope of the growing curve on the right.
- Manim move: accumulate (area building under speed curve), transform (rate → running total)
- Example seed: Integrate $v(t) = 18 + 5\sin(2\pi t)$ over one hour. The sinusoidal wobble integrates to zero — the fast stretches cancel the slow ones exactly — leaving a pure 18-mile total. Then show why: sine averages to zero over a full period.
- Length band: 3–5 min
- Still lanes: geo/c2v
- Prerequisites: Basic idea of area under a curve; what a derivative means.
- Exclusions: Riemann sum combinatorics; substitution technique; numerical integration methods; Liouville non-elementary antiderivatives.
- Score: 10/10

---

## Candidate 03 — The Earthquake Scale Hides a Factor of 350

- Source: `math-calculus/chapters/01-functions-and-graphs.md`
- Topic: CALCULUS
- Hook: The Japan 2011 earthquake registered 9.0; the Haiti 2010 quake registered 7.3. The gap looks like 1.7. The actual energy ratio is 350. One inverse function reveals what the number hides.
- Key case: Richter magnitude $M = \log_{10}(A/A_0)$, inverse $A = A_0 \cdot 10^M$. Amplitude ratio $10^{9-7.3} = 10^{1.7} \approx 50$, then energy scales as amplitude to the 1.5 power: $50^{1.5} \approx 350$.
- The Question: How can two numbers that differ by less than two encode a physical difference of 350 — and what is the mathematical machine that hides multiplication inside addition?
- Core idea: A logarithm compresses a quantity spanning many orders of magnitude into a compact readable number by turning multiplication into addition. Its inverse, the exponential, reverses the compression. Every logarithmic scale in science — decibels, pH, stellar magnitude — uses this same machinery.
- Visual object: A number line with magnitude on top (7.3 … 9) and a second axis below expanding exponentially to show amplitude (50×) and energy (350×), with the inverse-function arrow labeling the decode step.
- Manim move: transform (log scale ↔ linear scale), spread (the compressed gap expanding into 350×)
- Example seed: Richter magnitudes 7.3 vs. 9. Gap: 1.7. Amplitude ratio: $10^{1.7} \approx 50$. Energy ratio: $50^{1.5} \approx 350$. The entire Gulf War's explosive yield fits inside that gap. Two numbers. One inverse function.
- Length band: 2–3 min
- Still lanes: c2v/raster
- Prerequisites: None beyond basic multiplication; no prior calculus.
- Exclusions: Formal definition of functions; composition; vertical/horizontal line tests; trig.
- Score: 9/10

---

## Candidate 04 — Why Optimization Fails at Flat Points (and What That Means for Every Maximum in Nature)

- Source: `math-calculus/chapters/04-applications-of-derivatives.md`
- Topic: CALCULUS
- Hook: To find the maximum of any smooth function, you look for where the derivative equals zero. But zero derivative doesn't guarantee a maximum — it could be a minimum, or neither. And the minimum of one thing is often the maximum of another. The calculus doesn't care which you want; it just finds the flat spots.
- Key case: Rectangular field with 100 ft of fencing using a wall as one side. Maximize area: $A(y) = (100 - 2y)y$. Critical point at $y = 25$. The result ($x = 2y$) is a universal proportion — the same optimal ratio shows up regardless of total fence length.
- The Question: Why does setting the derivative to zero find optimal values — and why does the zero alone not tell you whether you found a maximum, a minimum, or neither?
- Core idea: At any interior maximum or minimum of a smooth function, the tangent must be horizontal — because if the function were still rising or falling, you could improve further. So $f'(c) = 0$ is a necessary condition, not a sufficient one. The first and second derivative tests discriminate between the candidates.
- Visual object: A smooth parabola ($A$ vs. $y$) with the tangent line drawn at the critical point, the second derivative concavity arrow showing curvature direction, and the candidate function values at the critical point and endpoints compared in a table.
- Manim move: trace (function rising then falling to identify maximum), collapse (all candidates compared)
- Example seed: Fencing problem, 100 ft. Derivative zero at $y = 25$. Evaluate corners and endpoints: $A(-2) = -1$, $A(25) = 1250$, $A(50) = 0$. The maximum is at the critical point, but you only know that by comparison — the derivative can't tell you.
- Length band: 3–5 min
- Still lanes: geo/c2v
- Prerequisites: What a derivative means; idea of slope.
- Exclusions: Multivariable optimization; Lagrange multipliers; Newton's method; L'Hôpital.
- Score: 9/10

---

## Candidate 05 — Jerk: The Derivative You Actually Feel

- Source: `math-calculus/chapters/03-derivatives.md`
- Topic: CALCULUS
- Hook: Position is where you are. Velocity is your speedometer. Acceleration is what your body registers as force. But what you feel when an elevator starts — the gut-lurch at the moment it begins to move — is not acceleration. It is the change in acceleration. It has a name: jerk. And it is the third derivative.
- Key case: Hennessey Venom GT: $v(t) = v_{\max}(1 - e^{-t/\tau})$. Differentiate once for acceleration (exponentially decaying launch shove), twice for jerk (most negative at $t = 0$ — the moment the shove begins to fade). Acceleration of 1.14g at launch; jerk is what pins you and then gradually releases.
- The Question: If velocity is the derivative of position and acceleration is the derivative of velocity, what does differentiating again actually measure — and why do engineers care about it?
- Core idea: Higher-order derivatives describe how the rate of change is itself changing. Jerk ($s'''(t)$) is the rate of change of acceleration; it governs the texture of motion, not just its magnitude. Roller-coaster engineers and ABS systems explicitly constrain jerk to prevent injury and wheel lock.
- Visual object: Three aligned time-series panels — $v(t)$ (growing S-curve), $a(t)$ (decaying exponential), $j(t)$ (negative decaying exponential) — stacked vertically, each labeled with what it measures physically, connected by the derivative arrow.
- Manim move: trace (the three curves appearing sequentially, each derived from the one above), decay (acceleration and jerk fading toward zero)
- Example seed: Venom GT, $v_{\max} = 270.49$ mph, $\tau \approx 10.79$ s. Launch acceleration: $a(0) = 270.49/10.79 \approx 25.1$ mph/s ≈ 1.14g. Jerk at launch: $j(0) = -v_{\max}/\tau^2 \approx -2.3$ mph/s². The derivative hierarchy in one car, three quantities, three derivatives.
- Length band: 3–5 min
- Still lanes: c2v/raster
- Prerequisites: What a derivative means; basic idea of velocity and acceleration.
- Exclusions: Snap/crackle/pop (fourth through sixth derivatives); formal chain rule derivation; logarithmic differentiation.
- Score: 9/10

---

## Candidate 06 — Slicing a Wine Bottle: How Integration Computes Any Volume

- Source: `math-calculus/chapters/06-applications-of-integration.md`
- Topic: CALCULUS
- Hook: A wine bottle is not a cylinder. There is no single formula for its volume. But there is a method: cut it into infinitely many horizontal disks, compute each disk's volume, add them up. That sum is the integral — and it works for any shape that can be described by a profile.
- Key case: Simplified wine bottle profile — body (radius 4 cm, 20 cm tall), tapering shoulder (4 → 1.5 cm over 5 cm), narrow neck (radius 1.5 cm, 5 cm tall). Three integrals, $V = \int_0^{30}\pi[r(y)]^2\,dy$, produce 1,167 cm³ ≈ 1.17 L vs. 750 mL standard — and the gap explains exactly why the body profile matters.
- The Question: How can you find the volume of an object with no simple formula — and why does slicing it into infinitely thin disks and adding them up give the exact answer?
- Core idea: Any continuously-profiled solid can be expressed as an integral of cross-sectional area over height. Each disk of radius $r(y)$ and thickness $dy$ contributes $\pi[r(y)]^2\,dy$; integrating over the full height sums all contributions. The same "slice, identify, integrate" pattern handles area, arc length, work, and probability.
- Visual object: Cutaway side view of a wine bottle with one horizontal disk extracted — radius $r(y)$, thickness $dy$, volume element labeled $\pi[r(y)]^2\,dy$ — with the stack of disks visible through the translucent bottle wall.
- Manim move: split (bottle into three profile segments), accumulate (disks stacking up from base to lip), scan (the horizontal slice moving through the bottle height)
- Example seed: Body: $\pi(4)^2 \times 20 = 320\pi \approx 1005$ cm³. Neck: $\pi(1.5)^2 \times 5 \approx 35$ cm³. Shoulder: integral of $(4 - 0.5u)^2$ over 5 cm $\approx 127$ cm³. Total: 1,167 cm³. Standard bottle: 750 mL. The geometry tells you where the missing volume went.
- Length band: 3–5 min
- Still lanes: geo/c2v
- Prerequisites: Idea of area under a curve; what an integral means.
- Exclusions: Shell method; washer method; arc length; work integrals.
- Score: 8/10

---

## Candidate 07 — The Tangent Line Trick: Why Engineers Approximate Everything

- Source: `math-calculus/chapters/04-applications-of-derivatives.md`
- Topic: CALCULUS
- Hook: $\sqrt{4.1}$ computed in your head, in one multiplication, with less than 0.01% error. The trick: near any known point, every smooth curve is essentially a straight line — and the derivative tells you which line.
- Key case: Linear approximation of $\sqrt{x}$ anchored at $x = 4$: $L(x) = 2 + \frac{1}{4}(x - 4)$. At $x = 4.1$: estimate 2.025, actual 2.0248, error 0.0002. At $x = 5$: estimate 2.25, actual 2.236, error 0.6% — sixty times larger.
- The Question: Why does the tangent line give such a good approximation close to the anchor — and why does accuracy collapse so fast when you move away?
- Core idea: Every differentiable function, zoomed in far enough near any point, looks like a straight line. The derivative gives the slope of that line. First-order approximation uses this linearity to replace a complicated function with a simple one, with error that is second-order small — it shrinks faster than the distance from the anchor.
- Visual object: A graph of $y = \sqrt{x}$ with the tangent line at $x = 4$ drawn over it — showing them nearly overlapping near $x = 4$ and visibly diverging by $x = 6$, with the error gap highlighted.
- Manim move: morph (curve straightening into tangent at anchor point), spread (error gap widening with distance)
- Example seed: Anchor: $x = 4$, $\sqrt{4} = 2$, slope $f'(4) = 1/4$. Estimate $\sqrt{4.1} \approx 2.025$. True: 2.0248. Error: 0.01%. Now try $\sqrt{5}$: estimate 2.25, true 2.236. Error: 0.6%. Moving one unit away multiplied the error by 60.
- Length band: 2–3 min
- Still lanes: geo
- Prerequisites: What a derivative means; idea of a tangent line.
- Exclusions: Taylor series; second-order approximation; error bounds; differentials.
- Score: 8/10

---

## Candidate 08 — The Camera Operator's Calculus: Related Rates

- Source: `math-calculus/chapters/04-applications-of-derivatives.md`
- Topic: CALCULUS
- Hook: A rocket climbs at 100 feet per second. A camera 1,000 feet away tilts to track it. When the rocket is low, the camera sweeps fast. When it's high, the camera barely moves — even though the rocket is screaming upward. The camera operator's hands are solving a calculus problem in real time.
- Key case: $\tan\theta = h/1000$. Differentiate: $\sec^2\theta \cdot d\theta/dt = (1/1000)(dh/dt)$. At $h = 500$ ft, $\sec^2\theta = 1.25$, $dh/dt = 100$: angular rate $= 0.08$ rad/s ≈ 4.6°/s. At launch (nearly flat), the sweep rate is much faster — the geometry dictates the operator's job gets easier as the rocket climbs.
- The Question: When two quantities both depend on time and are linked by a geometric equation, how does knowing one rate of change tell you the other — even when you can't watch both simultaneously?
- Core idea: Differentiating a geometric constraint (Pythagorean theorem, trig identity, etc.) with respect to time converts a static spatial relationship into a dynamic relationship between rates. The equation that constrains positions also constrains velocities — related rates is just implicit differentiation with time as the variable.
- Visual object: Side-view geometry diagram with the rocket height $h(t)$ rising along the left edge, the camera at distance 1,000 ft on the right, the angle $\theta$ labeled at the camera, and the angular rate $d\theta/dt$ shown as a small arc — with a time slider showing how both $h$ and $\theta$ evolve.
- Manim move: transform (static Pythagoras/trig equation → differentiated rate equation), scan (time moving forward, showing rates change)
- Example seed: Rocket at 500 ft, climbing 100 ft/s, camera 1,000 ft away. $\sec^2\theta = 1.25$. Angular rate: 0.08 rad/s. At launch height (near zero), the same 100 ft/s would produce a much faster sweep — the low part of the arc is geometrically wide. The operator knows this without doing the math; the math shows why.
- Length band: 3–5 min
- Still lanes: geo/c2v
- Prerequisites: Basic trigonometry; what a derivative means.
- Exclusions: Newton's method; optimization; L'Hôpital; antiderivatives.
- Score: 8/10
