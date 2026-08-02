# Math Algebra Video Ideas

Scouted 2026-07-09 from 12 narrative chapters (02–13). Nine candidates meet the ≥8 bar; three sub-threshold concepts noted at the end.

---

## Candidate 01 — Why Watching a Ferris Wheel From the Side Draws a Wave
- Source: `math-algebra/chapters/07-the-unit-circle-sine-and-cosine-functions.md`
- Topic: ALGEBRA
- Hook: A smooth, perfectly repeating wave emerges from something that has no wave in it at all — just a dot moving in a circle.
- Key case: A camera films a Ferris wheel from directly to the side. The car moves in a circle, but the video screen shows only its height — and that height traces a perfect sine wave.
- The Question: A dot going in a circle should draw a circle. Instead it draws a wave. Why?
- Core idea: The y-coordinate of a point on the unit circle is sin(θ) — as θ sweeps uniformly, that single coordinate oscillates up and down, producing the sine wave exactly; the wave IS the circle's shadow projected onto one axis.
- Visual object: A unit circle with a rotating point and a real-time sine curve being traced to its right by the point's y-coordinate
- Manim move: trace
- Example seed: A lighthouse beacon on a circle of radius 6 m rotates once every 8 seconds. At t = 2 s (quarter turn), the beacon's height above center is 6·sin(π/2) = 6 m — the top. At t = 4 s (half turn), height = 0 m again. At t = 6 s, height = −6 m — the bottom. Plotting height vs. time for one full revolution draws a complete sine wave.
- Length band: 3–5 min
- Still lanes: geo (circle-and-wave mechanical diagram), geo (coordinate-projection plate)
- Prerequisites: coordinate plane, what a circle is, angle measurement in degrees
- Exclusions: no radian conversion derivation, no other trig functions (cos/tan), no phase shift or amplitude parameters, no inverse trig, no real Ferris wheel engineering detail
- Score: 9/10

---

## Candidate 02 — Why 23 Strangers Have Better-Than-Even Odds of a Shared Birthday
- Source: `math-algebra/chapters/13-sequences-probability-and-counting-theory.md`
- Topic: ALGEBRA
- Hook: Most people guess you need about 180 people in a room before two are likely to share a birthday — the real answer is 23.
- Key case: A party of 23 people. No one knows anyone else's birthday. Before anyone speaks, the probability that at least two people share a birthday is already above 50%.
- The Question: With 365 days in a year and only 23 people, a shared birthday should be rare. The math says it's more likely than not. Why?
- Core idea: The probability accumulates across all C(23,2) = 253 possible pairs, not just one — each pair has a 1/365 chance, and 253 chances compound quickly via the complement rule (it is easier to count "all different" first, then subtract from 1).
- Visual object: A growing grid of pairs among 23 people, each pair lighting up as a potential match, until the count of 253 pairs visibly saturates the probability
- Manim move: accumulate
- Example seed: Start with 5 friends at a lunch table. P(all different birthdays) = 365/365 × 364/365 × 363/365 × 362/365 × 361/365 ≈ 0.973. So P(at least one match) ≈ 2.7% — small. Add 5 more people (10 total): P(at least one match) rises to about 12%. At 23 people: crosses 50%. At 30: about 70%.
- Length band: 3–5 min
- Still lanes: geo (pair-grid accumulation diagram), geo (number-line showing complement jump)
- Prerequisites: basic probability as favorable/total, complement rule
- Exclusions: no conditional probability formalism, no exact computation of the full 365!/342! fraction step-by-step on screen, no Poisson approximation, no generalizations to non-uniform birthday distributions
- Score: 9/10

---

## Candidate 03 — Why Every Exponential Eventually Beats Every Polynomial
- Source: `math-algebra/chapters/06-exponential-and-logarithmic-functions.md`
- Topic: ALGEBRA
- Hook: A polynomial like x^100 dwarfs 2^x for a long time — then 2^x catches up and never looks back.
- Key case: Compare x^10 and 2^x. At x = 100, x^10 = 10^20 — a hundred quintillion — while 2^100 ≈ 1.27 × 10^30, already a thousand billion times larger. The exponential has already won.
- The Question: x^10 grows by adding a bigger and bigger amount each step. So does 2^x. They should race neck and neck. Instead 2^x escapes permanently. Why?
- Core idea: Every step of a polynomial adds to the previous value by a polynomial-sized amount; every step of an exponential multiplies by a fixed ratio — and multiplication by a fixed factor, compounded forever, eventually dominates any additive growth no matter how fast the additions are.
- Visual object: Two curves on the same axes — x^10 and 2^x — the exponential appearing lower at first, then crossing and vanishing off the top of the screen while the polynomial flattens by comparison
- Manim move: compare
- Example seed: A savings account earning 5% interest annually vs. a savings account receiving a flat $5,000 added each year. Start both at $10,000. After 20 years the flat-addition account has $110,000; the 5% account has $26,533. After 100 years: flat-addition $510,000; 5% account $1,315,000. After 200 years: flat-addition $1,010,000; 5% account $172,800,000. The multiplicative account has lapped the additive one by a factor of 171.
- Length band: 2–3 min
- Still lanes: geo (crossing-curves diagram), geo (magnification inset showing divergence)
- Prerequisites: what a function and a graph are, basic exponent notation
- Exclusions: no formal limit definition (L'Hôpital, big-O notation), no comparison of different exponential bases against each other, no logarithm introduction, no polynomial-degree comparison among polynomials
- Score: 9/10

---

## Candidate 04 — Why a Repeating Decimal Is Secretly a Fraction
- Source: `math-algebra/chapters/13-sequences-probability-and-counting-theory.md`
- Topic: ALGEBRA
- Hook: 0.363636… goes on forever — and yet it is exactly 4/11, not an approximation of it.
- Key case: Type 0.363636… into a calculator and it shows a decimal. But 4 ÷ 11 = 0.363636… — identically. They are the same number.
- The Question: Adding infinitely many decimal places should give an infinitely precise approximation, never a clean fraction. How can an infinite sum equal a simple ratio like 4/11?
- Core idea: The repeating decimal is a geometric series with first term 0.36 and ratio 0.01; since |0.01| < 1, the infinite sum converges to 0.36/(1 − 0.01) = 36/99 = 4/11 — a finite answer because each successive term shrinks by the same factor, making the total bounded.
- Visual object: A number line between 0 and 1 with partial sums S1 = 0.36, S2 = 0.3636, S3 = 0.363636 zooming in, visibly pinching toward 4/11
- Manim move: collapse
- Example seed: 0.777… — the repeating 7. First term = 0.7, ratio = 0.1. Sum = 0.7 / (1 − 0.1) = 0.7/0.9 = 7/9. Check: 7 ÷ 9 = 0.777… ✓. Now try 0.142857142857… = 1/7. The pattern is 142857, ratio = 0.000001, first term = 0.142857. Sum = 0.142857/0.999999 = 142857/999999 = 1/7. ✓
- Length band: 2–3 min
- Still lanes: geo (number-line convergence diagram), geo (series stacking illustration)
- Prerequisites: what a fraction is, what a decimal is, basic idea of adding fractions
- Exclusions: no formal epsilon-delta limit, no comparison of converging vs. diverging series (harmonic), no proof that irrational numbers cannot repeat, no derivation of the general geometric-series formula from scratch on screen
- Score: 8/10

---

## Candidate 05 — Why Even-Multiplicity Zeros Bounce Instead of Cross
- Source: `math-algebra/chapters/05-polynomial-and-rational-functions.md`
- Topic: ALGEBRA
- Hook: Two polynomials can both equal zero at the same point, but one crosses the x-axis there and the other bounces off it — and you can tell which is which just by counting a factor.
- Key case: f(x) = (x − 2)(x + 1) crosses zero at x = 2. g(x) = (x − 2)²(x + 1) has zero at x = 2 also — but the graph touches the x-axis and turns around without crossing. Same x-value, completely different behavior.
- The Question: Both functions equal zero at x = 2. They should both cross the x-axis there. Why does one bounce back?
- Core idea: Near x = 2, (x − 2)² is always non-negative (a square), so the function cannot change sign through that zero — it goes to zero and comes back on the same side; odd-multiplicity factors do change sign, so the function passes through.
- Visual object: Two close-up graph panels at x = 2 — left showing a clean crossing (multiplicity 1), right showing a bounce (multiplicity 2) — with the sign of (x−2) vs. (x−2)² annotated above each
- Manim move: compare
- Example seed: Build (x − 1)²(x − 3) step by step. At x = 1, multiplicity 2: the function approaches zero from above (since (x−1)² ≥ 0), hits zero, and returns above — a bounce. At x = 3, multiplicity 1: the factor (x−3) changes sign, the function crosses. Plot x = 0: (−1)²(−3) = −3, below zero. Plot x = 2: (1)²(−1) = −1, still below zero — the bounce at x = 1 confirmed since the curve stays negative on both sides.
- Length band: 2–3 min
- Still lanes: geo (side-by-side graph panels with sign annotations), geo (sign-chart plate)
- Prerequisites: what a polynomial function is, what a zero is, basic graph reading
- Exclusions: no rational zero theorem, no synthetic division, no complex roots, no general degree-n end behavior, no multiplicity beyond 2 in the example
- Score: 8/10

---

## Candidate 06 — Why Multiplying Numbers Becomes Adding Logarithms
- Source: `math-algebra/chapters/06-exponential-and-logarithmic-functions.md`
- Topic: ALGEBRA
- Hook: Before calculators existed, astronomers multiplied 15-digit numbers by converting them to logarithms and doing addition instead.
- Key case: Multiply 1,234,567 × 8,765,432 with pen and paper — a nightmarish computation. Look up log(1,234,567) ≈ 6.0915 and log(8,765,432) ≈ 6.9428. Add: 13.0343. Look up 10^13.0343 ≈ 10,820,000,000,000. Done in three steps.
- The Question: Addition and multiplication are completely different operations. How can one turn into the other just by switching notation?
- Core idea: Logarithms translate from the multiplicative world into the additive world because b^m · b^n = b^(m+n) — when you write numbers as powers of the same base, multiplying them adds their exponents; the logarithm is precisely the exponent, so log(MN) = log(M) + log(N).
- Visual object: Two parallel number lines — one multiplicative (×10 gaps: 1, 10, 100, 1000) stacked above one additive (equal gaps: 0, 1, 2, 3) — with arrows showing multiplication on the top line corresponding to addition on the bottom
- Manim move: transform
- Example seed: Compound interest. $1,000 at 6% for 30 years: 1000 × 1.06^30. On a log scale, 1.06^30 becomes 30 × log(1.06) = 30 × 0.0253 = 0.759. So the final amount is 10^(3 + 0.759) = 10^3.759 ≈ $5,743. The exponent rule turned 30 multiplications into one multiplication and one addition.
- Length band: 2–3 min
- Still lanes: geo (dual number-line / log-scale diagram), geo (exponent-rule annotation plate)
- Prerequisites: what exponents are, basic multiplication, what a logarithm is (loosely)
- Exclusions: no change-of-base formula derivation, no natural log vs. common log distinction, no slide rule history beyond one sentence, no logarithmic equations, no pH or decibel scale applications
- Score: 8/10

---

## Candidate 07 — Why Complex Multiplication Is Secretly a Rotation
- Source: `math-algebra/chapters/10-further-applications-of-trigonometry.md`
- Topic: ALGEBRA
- Hook: Multiplying two complex numbers looks like messy algebra — but in the complex plane, it is simply spinning and stretching.
- Key case: (1 + i)^4. In rectangular form: four rounds of messy FOIL. In polar form: the number 1+i has magnitude √2 and angle 45°; raising to the 4th power means magnitude (√2)^4 = 4 and angle 4×45° = 180°. Answer: 4(cos 180° + i sin 180°) = −4. Four multiplications collapsed to one rotation.
- The Question: Complex multiplication mixes real and imaginary parts in a formula that looks arbitrary. Why does it secretly obey a simple rule about angles?
- Core idea: Writing a complex number in polar form (r, θ) reveals that multiplication scales magnitudes and adds angles — exactly what the cosine and sine addition formulas produce when you multiply out (r₁cosθ₁ + ir₁sinθ₁)(r₂cosθ₂ + ir₂sinθ₂).
- Visual object: The complex plane with a spiral showing (1+i)^1, (1+i)^2, (1+i)^3, (1+i)^4 as successive 45° rotations with growing magnitude, landing on −4 on the negative real axis
- Manim move: rotate
- Example seed: Start at the complex number i = (0, 1) — a point on the positive imaginary axis. Multiply by i: i × i = i² = −1, landing at (−1, 0) — a 90° rotation. Multiply again: −1 × i = −i, at (0, −1) — another 90°. Once more: −i × i = −i² = 1, at (1, 0) — back to start after four 90° turns. Four multiplications by i = four quarter-turns = full circle. The −1 that seems mysterious from algebra is obvious as geometry: two left turns.
- Length band: 2–3 min
- Still lanes: geo (complex-plane rotation spiral), geo (angle-addition diagram inset)
- Prerequisites: what complex numbers are, what the complex plane is, angle measurement
- Exclusions: no full proof of the angle-addition formula, no De Moivre's theorem stated as a named theorem, no nth roots of complex numbers, no applications to AC circuits or signal processing
- Score: 8/10

---

## Candidate 08 — Why One Polar Equation Draws an Ellipse, a Parabola, or a Hyperbola Depending on One Number
- Source: `math-algebra/chapters/12-analytic-geometry.md`
- Topic: ALGEBRA
- Hook: Three curves that look completely different — ellipses, parabolas, hyperbolas — are all written with the same formula; only one number changes.
- Key case: The equation r = 2/(1 − e·cosθ). Set e = 0.5: an ellipse appears. Set e = 1.0: a parabola. Set e = 1.5: a hyperbola. Three shapes, one formula, one dial.
- The Question: An ellipse closes on itself; a parabola opens to infinity; a hyperbola has two disconnected branches. How can three such different shapes be the same equation?
- Core idea: Eccentricity e measures the ratio of a point's distance to the focus vs. its distance to the directrix; as e crosses 1, the curve transitions from closed (sum of distances is fixed) through the exact-balance parabola to open (difference exceeds the baseline), with the shape morphing continuously through the transition.
- Visual object: A single polar plot with e as a slider — the curve visibly morphing from a fat ellipse through a parabola to a hyperbola as e increases from 0.3 to 1.5
- Manim move: morph
- Example seed: Earth's orbit: e = 0.017 — almost circular, barely distinguishable from a circle on a diagram. Halley's Comet: e = 0.967 — an extreme ellipse that stretches from inside Venus's orbit to beyond Neptune. A hypothetical comet at e = 1.001 — just past the parabola threshold — is on a hyperbolic path and will never return. Three objects, three fates, one number.
- Length band: 2–3 min
- Still lanes: geo (polar-plot morphing sequence), geo (focus-directrix distance diagram)
- Prerequisites: what an ellipse and hyperbola are (loosely), polar coordinates (loosely), what eccentricity means
- Exclusions: no Cartesian form derivation of each conic, no completing-the-square algebra for conics, no discriminant classification formula, no Kepler's laws beyond one mention, no whispering gallery or LORAN detail
- Score: 8/10

---

## Candidate 09 — Why Two Guitar Strings Slightly Out of Tune Make a Pulsing Sound
- Source: `math-algebra/chapters/09-trigonometric-identities-and-equations.md`
- Topic: ALGEBRA
- Hook: Two pure tones played together at slightly different pitches produce a single sound that fades in and out — and that pulsing is a math theorem in disguise.
- Key case: One string vibrates at 440 Hz, another at 442 Hz. Together they produce a sound that "beats" twice per second — a pulsing wah-wah effect any guitarist can hear when tuning.
- The Question: Two constant tones playing at the same time should produce a louder constant tone. Instead the volume oscillates. Why?
- Core idea: The sum-to-product identity rewrites sin(2π·440t) + sin(2π·442t) as 2·cos(2π·1·t)·sin(2π·441t) — a fast oscillation at 441 Hz (the average) multiplied by a slow envelope at 1 Hz (half the difference), making the amplitude rise and fall once per second.
- Visual object: A graph of the combined waveform showing the rapid oscillation inside a slowly varying amplitude envelope, with the two frequencies labeled and the envelope period labeled "beat frequency = |f₁ − f₂|"
- Manim move: slosh
- Example seed: Two tuning forks: one at 256 Hz (middle C), one at 260 Hz. Beat frequency = 260 − 256 = 4 Hz — four beats per second. The combined wave: 2·cos(2π·2·t)·sin(2π·258t). The envelope cos(2π·2t) completes a full cycle in 0.5 s, reaching zero amplitude twice per second, producing two audible "wahs" per second. A musician hears this beat and tightens one fork's pitch until the beats disappear — then the two tones are identical.
- Length band: 2–3 min
- Still lanes: geo (waveform-with-envelope graph), geo (sum-to-product formula annotation plate)
- Prerequisites: what sine waves and frequency are (loosely), what addition of functions means graphically
- Exclusions: no derivation of the sum-to-product formula from scratch, no Fourier series, no full complex signal-processing treatment, no other product-to-sum identities, no double-angle or half-angle formulas
- Score: 8/10

---

## Sub-threshold concepts (did not reach 8/10)

**Ch.8 — The four parameters of a sinusoidal function (amplitude, period, phase, shift).** Score: 7/10. Strong MC but the "aha" is distributed across four separate payoffs — no single counterintuitive claim anchors the film. Recommended fix: narrow to one parameter (e.g., phase shift — why f(x−3) shifts *right*, not left) and resubmit as a separate card.

**Ch.11 — The feasible region's corners always hold the optimum.** Score: 7/10. VG+PQ, good visual object (polygon with level-set lines sweeping across it). Self-containment requires setting up the LP context, adding 90 seconds of setup that eats into the payoff. Could be a strong 8 if the hook can be cast as a pure geometry claim without the business framing.

**Ch.3 — Why f(x−3) shifts the graph RIGHT, not left.** Score: 6/10. Classic misconception (VG), self-contained, but the resolution ("the output that f used to produce at 0 is now produced at 3") is a one-sentence fix — does not sustain 2 minutes without padding. Better served as a 60-second short or a static figure annotation.
