# Video Ideas — math-college-algebra
*Scouted 2026-07-09. Ordered highest score first. Cards with score ≥ 8 only.*

---

## Candidate 01 — The Wave Is the Shadow of the Circle
- Source: `math-college-algebra/chapters/07-the-unit-circle-sine-and-cosine-functions.md`
- Topic: COLLEGE ALGEBRA
- Hook: The sine wave looks nothing like a circle — yet every wave in nature is literally a circle viewed from the side.
- Key case: A Ferris wheel car traces a perfect circle; plot its height against time and you get a sine curve — the wave *is* the circle, projected onto one axis.
- The Question: Why does circular motion produce a wave-shaped graph — what is the circle actually doing?
- Core idea: As a point travels around the unit circle, its y-coordinate (sine) and x-coordinate (cosine) each trace smooth oscillations. The wave is the shadow of the circle cast onto a single dimension; periodicity is baked in because after 2π radians you are back to the same point.
- Visual object: Animated unit circle with a point traveling counterclockwise; a horizontal "projection beam" traces the point's y-value onto a time axis, drawing the sine curve in real time as the circle spins.
- Manim move: trace (point on circle simultaneously traces wave on adjacent axis)
- Example seed: Ferris wheel radius 50 ft, one revolution per 60 seconds. At t = 15 s (quarter turn), height above center = 50 sin(π/2) = 50 ft. At t = 30 s (half turn), height = 0. The wave writes itself as the wheel turns.
- Length band: 3–5 min
- Still lanes: geo
- Prerequisites: What a function is; radian measure basics
- Exclusions: Do not cover the six trig functions, reference angles, or the full unit-circle value table — keep focus on the circle-to-wave connection only
- Score: 10/10

---

## Candidate 02 — One Cone, Four Curves: The Secret Behind Orbits and Headlights
- Source: `math-college-algebra/chapters/12-analytic-geometry.md`
- Topic: COLLEGE ALGEBRA
- Hook: A satellite orbit, a flashlight beam, and a nuclear cooling tower are the same mathematical object — all slices of the same cone.
- Key case: The polar equation r = ed / (1 − e·cos θ) describes every conic. Set e < 1 and you get a closed ellipse (satellite orbit); set e = 1 and you get a parabola (flashlight reflector); set e > 1 and you get a hyperbola (LORAN navigation). One formula, one parameter, three completely different real-world shapes.
- The Question: Why do a satellite's orbit, a car headlight, and a ship's GPS all obey the same equation — what do they share?
- Core idea: Every conic section is defined by a distance condition: a sum of distances (ellipse), a difference (hyperbola), or equality with a line (parabola). All four arise by tilting a plane through a double cone at different angles. Eccentricity e is the single number that measures how tilted the plane is, and it determines which shape you get.
- Visual object: Double cone (two cones joined at tip) with a cutting plane that slowly tilts from nearly horizontal (circle) through gentle tilt (ellipse) to parallel-to-side (parabola) to steep tilt (hyperbola); the intersection curve morphs continuously.
- Manim move: rotate (plane tilts through cone, intersection morphs across all four conics)
- Example seed: Earth's orbit: e ≈ 0.017 (nearly circular, seasons driven by axial tilt not distance). Halley's Comet: e ≈ 0.967 (elongated sliver). Same formula, radically different shape. A spacecraft on a flyby has e > 1 — it escapes forever.
- Length band: 3–5 min
- Still lanes: geo / raster
- Prerequisites: Basic coordinate geometry; what a parabola is
- Exclusions: Do not derive the conic equations algebraically — stay at the geometric/distance-condition level; skip completing-the-square drill
- Score: 9/10

---

## Candidate 03 — Why Logs Turn Multiplication Into Addition
- Source: `math-college-algebra/chapters/06-exponential-and-logarithmic-functions.md`
- Topic: COLLEGE ALGEBRA
- Hook: Before calculators, astronomers multiplied 12-digit numbers in seconds — using a trick that turns multiplication into addition. That trick is logarithms.
- Key case: log(1000 × 100) = log(1000) + log(100) = 3 + 2 = 5. No multiplication needed — the log of a product is the sum of the logs. The product rule is not a trick: it follows inevitably from the fact that b^m · b^n = b^(m+n), read backwards.
- The Question: Why does the logarithm turn multiplication into addition — what is really happening?
- Core idea: Exponential functions turn addition into multiplication (b^m · b^n = b^(m+n)). Logarithms are the inverse — they reverse that map, so multiplication in the original scale becomes addition in the log scale. Every log rule is just an exponent rule read from the other direction.
- Visual object: A number line that morphs into a logarithmic scale: equal multiplicative steps (×10, ×10, ×10) map to equal additive steps (1, 1, 1) on the log axis. Multiplying two numbers becomes sliding two arrows and adding their lengths.
- Manim move: transform (linear number line morphs to log scale; multiplying becomes addition of arrow lengths)
- Example seed: 2^10 = 1024 ≈ 1000. So log₂(1024) = 10. Doubling time at 6% continuous growth: t = ln(2)/0.06 ≈ 11.6 years. The Rule of 72 (72 ÷ 6 = 12) is the log formula in disguise.
- Length band: 3–5 min
- Still lanes: geo / c2v
- Prerequisites: What an exponent is; the idea of an inverse function
- Exclusions: Do not cover log equations or change-of-base in detail — stay on the conceptual why
- Score: 9/10

---

## Candidate 04 — Cross or Bounce? What Zero Multiplicity Actually Means
- Source: `math-college-algebra/chapters/05-polynomial-and-rational-functions.md`
- Topic: COLLEGE ALGEBRA
- Hook: Two polynomials can have zeros at exactly the same x-values — yet one graph crosses the x-axis there and the other bounces off. The difference is invisible in the roots but written in the exponent.
- Key case: f(x) = (x − 2)(x + 1) crosses at x = 2 and x = −1 (multiplicity 1 each). g(x) = (x − 2)²(x + 1) bounces at x = 2 but crosses at x = −1 (multiplicity 2 vs. 1). Same zeros, different behavior — multiplicity controls the graph completely.
- The Question: Why does an even-multiplicity zero make the curve bounce instead of cross — what is the exponent actually doing?
- Core idea: Near a zero of multiplicity k, the function behaves like (x − r)^k. For odd k, the factor changes sign as x passes through r, so the function crosses the axis. For even k, the factor stays positive (it is squared), so the function touches zero and returns to the same side — a bounce. Multiplicity is the shape of the graph at that zero, not just the location.
- Visual object: Three close-up animations of a curve approaching a zero: multiplicity 1 (clean cross), multiplicity 2 (bounce with tangent touch), multiplicity 3 (flattened S-shaped crossing). Same x location, three visually distinct behaviors.
- Manim move: compare (three side-by-side close-ups of the same zero with multiplicities 1, 2, 3)
- Example seed: f(x) = (x + 2)(x − 1)²(x − 3). Zero at x = 1 is multiplicity 2 → bounces. Zeros at x = −2 and x = 3 are multiplicity 1 → cross cleanly. Degree 4, even → both ends point up. Exactly one bounce, two crosses, from reading the formula alone.
- Length band: 2–3 min
- Still lanes: geo
- Prerequisites: What a polynomial zero is; basic graph reading
- Exclusions: Do not cover the rational zero theorem, synthetic division, or the fundamental theorem of algebra
- Score: 9/10

---

## Candidate 05 — Completing the Square Is the Quadratic Formula in Disguise
- Source: `math-college-algebra/chapters/02-equations-and-inequalities.md`
- Topic: COLLEGE ALGEBRA
- Hook: The quadratic formula looks like a miracle handed down from above — but it is actually just completing the square, done once in symbols so you never have to do it again.
- Key case: Apply the completing-the-square steps to the general ax² + bx + c = 0 symbol-by-symbol, and the formula x = (−b ± √(b²−4ac)) / 2a falls out line by line. The formula is not separate from the method — it *is* the method, pre-computed.
- The Question: Where does the quadratic formula come from — why does it have that shape?
- Core idea: Completing the square converts any quadratic into the form a(x − h)² = k, from which the square-root property solves it immediately. When you apply these steps to the abstract form ax² + bx + c = 0 instead of specific numbers, every step produces a piece of the quadratic formula. The formula is completing the square, done symbolically.
- Visual object: Two-column derivation: left column works a specific quadratic numerically (2x² − 7x + 3 = 0); right column works the general form ax² + bx + c = 0 in parallel. Each row of the general derivation produces a recognizable piece of the final formula.
- Manim move: split (numerical example on left, symbolic general case on right, steps aligned row by row)
- Example seed: x² + 6x − 7 = 0. Complete the square: x² + 6x + 9 = 16, so (x+3)² = 16, x = 1 or −7. Now run the same steps on ax² + bx + c = 0 in the parallel column — the formula emerges step by step from identical moves.
- Length band: 3–5 min
- Still lanes: geo / c2v
- Prerequisites: Solving linear equations; what a square root means
- Exclusions: Do not cover complex roots or the discriminant in depth — stay on the derivation of the formula itself
- Score: 8/10

---

## Candidate 06 — Complex Multiplication Is Just Spinning
- Source: `math-college-algebra/chapters/10-further-applications-of-trigonometry.md`
- Topic: COLLEGE ALGEBRA
- Hook: Multiplying two complex numbers looks like a mess of algebra — but in polar form it is nothing more than spinning one number around the origin and rescaling it.
- Key case: (1 + i)⁴. In rectangular form, this requires three rounds of messy multiplication. In polar form: 1 + i has modulus √2 and angle 45°. Raise to the 4th power: modulus = (√2)⁴ = 4, angle = 4 × 45° = 180°. That is the point (−4, 0), or −4. Four multiplications collapse to two arithmetic operations.
- The Question: Why does multiplying complex numbers in polar form just add their angles — what is multiplication actually doing to the complex plane?
- Core idea: Writing a complex number as r(cos θ + i sin θ) makes its position in the plane explicit — r is the distance from the origin, θ is the direction. When you multiply two such numbers, the angle-addition formulas for sine and cosine combine the two expressions, and the result has modulus r₁r₂ and angle θ₁ + θ₂. Multiplication is rotation-plus-scaling, hidden behind the algebra in rectangular form.
- Visual object: Complex plane with a single complex number z shown as an arrow. A second number w (with marked angle and modulus) rotates z: the result arrow shows the new angle (sum of original angles) and new length (product of moduli). Animate: multiply by i repeatedly to show 90° rotations.
- Manim move: rotate (arrow rotates by the argument of the multiplier; modulus scales simultaneously)
- Example seed: Multiplying by i four times: i has modulus 1 and angle 90°. So i¹ rotates any point 90°, i² rotates 180° (giving −z), i³ rotates 270°, i⁴ rotates 360° back to start. This is why i² = −1: one 90° rotation twice is a 180° flip.
- Length band: 3–5 min
- Still lanes: geo
- Prerequisites: What complex numbers are; basic polar coordinates
- Exclusions: Do not derive De Moivre's theorem formally or cover nth roots of complex numbers
- Score: 8/10

---

## Candidate 07 — Four Numbers Describe Everything That Repeats
- Source: `math-college-algebra/chapters/08-periodic-functions.md`
- Topic: COLLEGE ALGEBRA
- Hook: Ocean tides, alternating current, seasonal daylight, guitar string vibration — completely different phenomena — are all described by the exact same four numbers.
- Key case: Boston daylight: maximum 15 hours (June 21, day 172), minimum 9 hours (Dec 21). From these four data points — two extremes and their dates — you extract amplitude = 3, vertical shift = 12, period = 365, phase shift = 172, and write L(t) = 3 cos(2π(t−172)/365) + 12. The model predicts every day's daylight from four measurements.
- The Question: Why do four numbers completely specify any repeating phenomenon — what is each one doing?
- Core idea: Any sinusoidal function y = a·sin(bx − c) + d has exactly four geometric parameters: amplitude controls how far it swings, period (via b) controls how fast it repeats, phase shift (c/b) controls where in the cycle it starts, and vertical shift d sets the center line. These four are independent and exhaustive — change any one and only that geometric feature changes.
- Visual object: A single sine wave with four labeled, interactive controls: a slider for amplitude stretches the wave vertically; a slider for period compresses or extends horizontally; a slider for phase shift slides the wave left/right; a slider for vertical shift moves the midline up/down. Each change is isolated.
- Manim move: spread (four-panel diagram, each panel isolating one parameter change while the other three stay fixed)
- Example seed: Tide model: high tide 14 ft at 6 AM, low tide 2 ft at noon. Extract: amplitude = (14−2)/2 = 6, midline = (14+2)/2 = 8, period = 12 hours. Model: h(t) = 6 cos(π(t−6)/6) + 8. Verify at t = 6: h = 14 ✓. At t = 12: h = 2 ✓.
- Length band: 3–5 min
- Still lanes: geo / raster
- Prerequisites: What sine and cosine are; the unit circle
- Exclusions: Do not cover tangent/secant/cosecant or inverse trig functions — keep focus on the four sinusoidal parameters
- Score: 8/10

---

## Candidate 08 — The Birthday Problem: Why Intuition Is Wrong by an Order of Magnitude
- Source: `math-college-algebra/chapters/13-sequences-probability-and-counting-theory.md`
- Topic: COLLEGE ALGEBRA
- Hook: In a room of 23 people, there is better than a 50% chance that two of them share a birthday — most people guess you need 180+ people. The math is off by nearly an order of magnitude from intuition.
- Key case: With 23 people, there are C(23, 2) = 253 possible pairs. Each pair has a 1/365 chance of matching. The probability that *no* pair matches is (365/365)·(364/365)·(363/365)···(343/365) ≈ 0.493. So P(at least one match) ≈ 50.7%.
- The Question: Why does the shared-birthday threshold fall at 23 people, not 183 — what is human intuition getting wrong?
- Core idea: Intuition imagines asking "does anyone share MY birthday?" — that question needs ~183 people for 50% odds. The real question is "does any pair match?" With n people there are C(n, 2) = n(n−1)/2 pairs. That count grows as n², so the number of "tries" explodes long before n reaches 365. It is the pairs that count, not the people.
- Visual object: Two panels: left shows a single person's birthday checked against 22 others (linear, needs many people); right shows all 23 people's birthdays checked pairwise — 253 arcs light up simultaneously, showing why the threshold is so low. Below both: a line graph of P(shared birthday) vs. room size, crossing 50% at n = 23.
- Manim move: spread (pairwise connections between 23 dots materialize one by one, accumulating to 253 total)
- Example seed: 23 people → 253 pairs → P ≈ 50.7%. 30 people → 435 pairs → P ≈ 70.6%. 50 people → 1225 pairs → P ≈ 97%. 70 people → 2415 pairs → P ≈ 99.9%. The curve passes 50% far earlier than any intuitive estimate.
- Length band: 2–3 min
- Still lanes: geo / c2v
- Prerequisites: Basic probability (equally likely outcomes); what combinations count
- Exclusions: Do not cover the full combinatorics chapter — keep to this one problem and the pairs-growth insight
- Score: 8/10
