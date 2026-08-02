# Prealgebra Video Ideas

---

## Candidate 01 — Why Squaring Both Sides Can Lie to You
- Source: `math-prealgebra/chapters/09-roots-and-radicals.md`
- Topic: PREALGEBRA
- Hook: Squaring both sides of an equation looks like a legal move — it is not always reversible.
- Key case: A student solves $\sqrt{x} = -3$ by squaring: $x = 9$. She checks: $\sqrt{9} = 3$, not $-3$. The algebra produced a confident wrong answer from a perfectly correct procedure.
- The Question: Squaring both sides should preserve equality. We did that, we got $x = 9$, but $x = 9$ does not satisfy the original. Why did a valid algebraic step produce a false solution?
- Core idea: Squaring loses sign information — $(-3)^2 = 9$ and $(3)^2 = 9$ are the same, so squaring "forgets" which side of zero you were on and can pull in a mirror-image solution the original equation never permitted.
- Visual object: A number line with a mirror placed at zero — squaring maps both $+3$ and $-3$ to the same point $9$, collapsing two positions into one.
- Manim move: collapse
- Example seed: Maria solves $\sqrt{2x + 1} = x - 1$. Squaring gives $2x + 1 = x^2 - 2x + 1$, which simplifies to $x^2 - 4x = 0$, yielding $x = 0$ or $x = 4$. Check: $x = 0$ gives $\sqrt{1} = -1$, false. $x = 4$ gives $\sqrt{9} = 3$, true. One answer survives; one was a phantom of squaring.
- Length band: 3–5 min
- Still lanes: geo (mirror-at-zero number line), geo (squaring-as-folding diagram)
- Prerequisites: what a square root is, basic equation solving
- Exclusions: no complex numbers, no absolute-value equation formalism, no cube-root cases, no formal definition of function domain
- Score: 9/10

---

## Candidate 02 — Why the Bigger Pizza Is Almost Twice the Food
- Source: `math-prealgebra/chapters/06-polynomials.md`
- Topic: PREALGEBRA
- Hook: A 14-inch pizza is 40% wider than a 10-inch pizza, but it contains nearly twice as much food.
- Key case: A pizza shop prices a 14-inch at $22 and a 10-inch at $12. The 14-inch is 83% more expensive and appears to be only 40% bigger — but the area ratio is $49\pi / 25\pi = 1.96$.
- The Question: If the 14-inch diameter is only 40% bigger than the 10-inch, why is there nearly double the pizza? Where does the extra food come from?
- Core idea: Area scales with the square of the radius — double the diameter means four times the area; a 40% wider circle covers $1.4^2 = 1.96$ times the area. Length scales linearly; area scales quadratically. That single exponent is the entire explanation.
- Visual object: Two circles — one with diameter 10, one with diameter 14 — the smaller one tiled inside the larger to show the area gap visually.
- Manim move: accumulate
- Example seed: A small round garden plot has radius 5 feet (area $25\pi \approx 78.5$ sq ft). A neighbor's plot has radius 7 feet (area $49\pi \approx 153.9$ sq ft). The neighbor's radius is 40% bigger; her garden has 96% more area. Fencing cost scales with radius; seed cost scales with area.
- Length band: 2–3 min
- Still lanes: geo (circle-area diagram), c2v (pizza slice illustration)
- Prerequisites: what area is, basic multiplication
- Exclusions: no calculus, no volume scaling (cubic), no formal polynomial definition, no FOIL or polynomial arithmetic
- Score: 9/10

---

## Candidate 03 — Why Your Average Speed on a Round Trip Is Never What You Think
- Source: `math-prealgebra/chapters/03-math-models.md`
- Topic: PREALGEBRA
- Hook: If you drive 30 mph to a destination and 60 mph back, your average speed is not 45 mph.
- Key case: A driver covers a 60-mile route at 30 mph (takes 2 hours). Returns the same 60 miles at 60 mph (takes 1 hour). Total: 120 miles in 3 hours. Average: 40 mph — not 45.
- The Question: The average of 30 and 60 is 45. You drove at those two speeds for the same distance each way. Why isn't the average speed 45 mph?
- Core idea: Average speed is total distance over total time — but time spent at each speed is unequal. You spend twice as long at 30 mph as at 60 mph, so the slow leg dominates the average. The arithmetic mean of two speeds is only the average when you spend equal *time*, not equal *distance*, at each.
- Visual object: A timeline bar split into two unequal segments — 2 hours at 30 mph vs. 1 hour at 60 mph — showing the slow leg takes twice the time for the same distance.
- Manim move: compare
- Example seed: A commuter biked to work at 10 mph and rode the bus home the same 5-mile route at 30 mph. Bike: 30 min. Bus: 10 min. Total: 10 miles in 40 min = 15 mph average. The arithmetic mean of 10 and 30 is 20 — five mph off.
- Length band: 2–3 min
- Still lanes: geo (timeline bar / distance diagram), geo (speed-time rectangle comparison)
- Prerequisites: the formula $d = rt$, basic fractions
- Exclusions: no harmonic mean formula, no weighted average formalism, no multi-leg trip, no logarithms or calculus
- Score: 9/10

---

## Candidate 04 — Why Multiplying by a Negative Flips the Inequality
- Source: `math-prealgebra/chapters/02-solving-linear-equations-and-inequalities.md`
- Topic: PREALGEBRA
- Hook: Every other operation preserves an inequality's direction — but multiplying by a negative reverses it, every time, for a reason that has nothing to do with algebra conventions.
- Key case: The inequality $3 < 5$ is obviously true. Multiply both sides by $-1$: we get $-3$ on the left and $-5$ on the right. But $-3 > -5$. The inequality flipped — and no one told us to flip it.
- The Question: Multiplying both sides by the same number should preserve equality and inequality alike — we do it constantly for equations. We multiplied both sides of $3 < 5$ by $-1$ and the direction changed. Why?
- Core idea: Multiplying by a negative is a reflection across zero on the number line. Reflection reverses left-right order: the number that was to the *left* (smaller) ends up to the *right* (larger). The flip rule is not a convention — it is the geometry of negation.
- Visual object: A number line with two labeled points, then a mirror placed at zero — the reflection animation shows both points swapping sides, and the smaller-on-the-left relationship reversing.
- Manim move: rotate
- Example seed: Solving $-2x + 7 \ge 1$: subtract 7 to get $-2x \ge -6$. Divide by $-2$ (flip!): $x \le 3$. A student who forgets the flip writes $x \ge 3$ — which includes $x = 10$. Check: $-2(10) + 7 = -13$, which is not $\ge 1$. The flip was real and necessary.
- Length band: 2–3 min
- Still lanes: geo (number-line reflection diagram), geo (before/after comparison of two labeled points)
- Prerequisites: what an inequality is, basic number-line orientation, multiplying by negatives in equations
- Exclusions: no compound inequalities, no interval notation, no absolute-value inequalities, no formal order-axiom proof
- Score: 9/10

---

## Candidate 05 — Why Completing the Square Reveals the Vertex
- Source: `math-prealgebra/chapters/10-quadratic-equations.md`
- Topic: PREALGEBRA
- Hook: The vertex of a parabola seems buried inside the equation $y = ax^2 + bx + c$ — completing the square digs it out by changing the equation's shape, not its meaning.
- Key case: The parabola $y = x^2 - 4x + 3$ has its lowest point somewhere around $x = 2$, but that is invisible from the standard form. Rewrite it as $y = (x - 2)^2 - 1$: the vertex $(2, -1)$ appears directly in the equation.
- The Question: Two equations — $y = x^2 - 4x + 3$ and $y = (x - 2)^2 - 1$ — describe the same parabola. The first hides the vertex; the second names it. How does rewriting an expression reveal geometric structure that was always there?
- Core idea: Completing the square rewrites $x^2 - 4x$ as $(x - 2)^2 - 4$ by adding and subtracting the same value. The new form $(x - h)^2 + k$ makes the vertex $(h, k)$ readable because $(x - h)^2$ is always non-negative and equals zero exactly when $x = h$ — so $k$ is the minimum value of the whole expression.
- Visual object: A parabola on the coordinate plane — the algebraic rewrite plays out as the vertex dot and axis-of-symmetry line appear, labeled directly from the $(x - 2)^2 - 1$ form.
- Manim move: morph
- Example seed: A projectile's height is $h(t) = -16t^2 + 80t + 4$. Complete the square: factor out $-16$, get $h(t) = -16(t - 2.5)^2 + 104$. The maximum height of 104 feet at 2.5 seconds is now readable directly, without plugging $t = -b/(2a)$ into the original.
- Length band: 3–5 min
- Still lanes: geo (parabola with vertex labeled, axis of symmetry), geo (algebraic rewrite shown step by step beside the graph)
- Prerequisites: what a parabola looks like, basic polynomial arithmetic, the binomial square pattern $(a+b)^2 = a^2 + 2ab + b^2$
- Exclusions: no quadratic formula derivation, no complex roots, no conic sections, no calculus extrema, no "completing the square to solve an equation" (only the geometric interpretation here)
- Score: 9/10

---

## Candidate 06 — Why the Discriminant Knows the Answer Before You Solve
- Source: `math-prealgebra/chapters/10-quadratic-equations.md`
- Topic: PREALGEBRA
- Hook: You can know whether a quadratic equation has two solutions, one solution, or no solutions without solving it — from a single number computed in two seconds.
- Key case: A student stares at $x^2 - 4x + 5 = 0$ and tries to factor. She finds no integer pair with product 5 and sum $-4$. She grinds through the quadratic formula and gets $\sqrt{-4}$ under the radical — impossible in the reals. She wasted three minutes. Computing $b^2 - 4ac = 16 - 20 = -4$ first would have told her immediately.
- The Question: The quadratic formula gives solutions only if the number under the radical is non-negative. Before you solve, how can you know in advance whether the formula will produce real answers — and how many?
- Core idea: The discriminant $b^2 - 4ac$ is exactly the expression under the radical in the quadratic formula. Its sign determines the count: positive gives two distinct real roots (the $\pm$ splits into two values), zero gives one repeated root (the $\pm$ adds and subtracts nothing), negative means no real roots (you can't take the square root of a negative real number).
- Visual object: A parabola that slides vertically — above the x-axis (no intersections, $\Delta < 0$), tangent to it (one, $\Delta = 0$), crossing it at two points ($\Delta > 0$) — the discriminant value displayed alongside as the parabola moves.
- Manim move: scan
- Example seed: A ball is thrown from 4 feet up at 8 ft/s upward. Will it reach 20 feet? Height: $h(t) = -16t^2 + 8t + 4 = 20$ → $-16t^2 + 8t - 16 = 0$. Discriminant: $64 - 4(-16)(-16) = 64 - 1024 = -960 < 0$. No — the ball never reaches 20 feet. No computation of the formula needed.
- Length band: 2–3 min
- Still lanes: geo (sliding parabola crossing the x-axis in three configurations), geo (discriminant sign shown beside each parabola)
- Prerequisites: what a parabola is, the quadratic formula at a surface level, what a square root of a negative number means (just "not real")
- Exclusions: no complex number arithmetic, no completing-the-square derivation of the formula, no Vieta's formulas, no proof that the discriminant equals the square of the difference of the roots
- Score: 9/10

---

## Candidate 07 — Why Subtracting a Negative Is the Same as Adding
- Source: `math-prealgebra/chapters/01-foundations.md`
- Topic: PREALGEBRA
- Hook: The bumper sticker says "two negatives make a positive" — but only for subtraction, and only because negation is a direction flip, not a number change.
- Key case: A thermometer reads $-8°$F outside. The thermostat reads $68°F$ inside. The difference is $68 - (-8) = 76$ degrees — not 60. Subtracting a negative gave a bigger gap than the numbers' magnitudes suggested.
- The Question: $5 - 3 = 2$ makes sense — you remove 3. But $5 - (-3) = 8$: removing a negative number made the result *larger*. How does removing something make an increase?
- Core idea: Subtracting a number means adding its opposite. The opposite of $-3$ is $+3$, so $5 - (-3) = 5 + 3 = 8$. The negative sign on the $3$ said "go left"; the subtraction operator flips that to "go right." Two direction-changes compose into no change in direction — which is why the result is a positive move.
- Visual object: A number line — an arrow pointing left for $-3$, then a second operation that flips the arrow to point right, showing the composed motion lands at 8.
- Manim move: rotate
- Example seed: A scuba diver is at $-30$ feet (30 feet below surface). A buoy floats at $-5$ feet. The depth difference — how much higher the buoy is — is $(-5) - (-30) = -5 + 30 = 25$ feet. Draw the subtraction as arrow-flip on a vertical number line.
- Length band: 2–3 min
- Still lanes: geo (vertical number line with labeled arrows for the diver/buoy), geo (arrow-flip diagram showing direction reversal)
- Prerequisites: what negative numbers represent, basic number-line orientation
- Exclusions: no multiplication of negatives (different concept), no algebra equations, no absolute value, no formal additive-inverse axiom
- Score: 8/10

---

## Candidate 08 — Why Rational Expressions Have Forbidden Values
- Source: `math-prealgebra/chapters/08-rational-expressions-and-equations.md`
- Topic: PREALGEBRA
- Hook: A fraction with a variable in the denominator looks like an ordinary algebraic expression — but it secretly has holes punched in its domain.
- Key case: The expression $\dfrac{x + 3}{x - 2}$ is defined everywhere *except* at $x = 2$. Plug in $x = 2$: the denominator is zero. The expression is not just "large" there — it is undefined, a gap in the function's territory.
- The Question: An expression like $\dfrac{x + 3}{x - 2}$ seems to accept any value of $x$ — it's just arithmetic. But $x = 2$ breaks it completely while $x = 1.99999$ works fine. Why does a single input create a forbidden zone that the algebra cannot cross?
- Core idea: Division by zero is not a very large number — it is undefined, because no real number times zero equals anything other than zero. The moment the denominator hits zero, the division has no answer. The forbidden values are not singularities to approach; they are genuine absences — holes in the domain.
- Visual object: A graph of $y = \dfrac{x + 3}{x - 2}$ with a visible vertical asymptote at $x = 2$ — a dashed line marking the boundary the curve approaches but never crosses, with an explicit open-circle hole on the domain.
- Manim move: split
- Example seed: A car's fuel efficiency is $\dfrac{240}{g}$ miles per gallon, where $g$ is gallons used. At $g = 0$ (no gas), the formula says infinity — actually undefined. Solving $\dfrac{240}{g} = 30$ gives $g = 8$. But solving $\dfrac{240}{g} = 0$ has no solution: no amount of gas gives zero efficiency. The forbidden zone ($g = 0$) is the physical "engine off" state.
- Length band: 2–3 min
- Still lanes: geo (number line with open circle at the excluded value), geo (graph of simple rational function with asymptote)
- Prerequisites: what fractions are, why division by zero is undefined (basic), what a variable is
- Exclusions: no complex-plane poles, no limit formalism, no partial fractions, no asymptote arithmetic, no adding or multiplying rational expressions
- Score: 8/10

---

## Candidate 09 — Why the Zero Product Property Turns Factoring into Solving
- Source: `math-prealgebra/chapters/07-factoring.md`
- Topic: PREALGEBRA
- Hook: Factoring a quadratic looks like it just rewrites the expression — until one single property of zero turns the rewrite into the solutions.
- Key case: A baseball is hit upward at 64 ft/s. Height: $h(t) = -16t^2 + 64t$. Set equal to zero: $-16t^2 + 64t = 0$. Factor: $-16t(t - 4) = 0$. Two factors. Two solutions: $t = 0$ (the swing) and $t = 4$ (the landing). The factoring didn't compute anything — it just separated the equation into two solvable pieces.
- The Question: Factoring rewrites $-16t^2 + 64t$ as $-16t(t-4)$ — that's a simplification, not a solution. How does rewriting a product lead directly to the values of $t$?
- Core idea: The Zero Product Property — if a product equals zero, at least one factor equals zero. It is the only case where a product gives direct information about the individual factors. Every other product value ($AB = 12$, $AB = -7$) tells you nothing useful about $A$ or $B$ alone. Zero is uniquely revealing.
- Visual object: A multiplication table with one row highlighted: anything times zero is zero — and the reverse: the only way to get zero from a product is if one of the pieces is zero. Two factors in boxes; either box going to zero makes the product zero.
- Manim move: split
- Example seed: A rectangular garden has area $w(w + 6) = 40$ square feet. Move everything: $w^2 + 6w - 40 = 0$. Factor: $(w + 10)(w - 4) = 0$. Either $w = -10$ (rejected — no negative width) or $w = 4$ feet. Length $= 10$ feet. Check: $4 \times 10 = 40$. The factoring handed the solutions directly from the product structure.
- Length band: 2–3 min
- Still lanes: geo (multiplication table highlighting the zero row/column), geo (two-factor box diagram with one going to zero)
- Prerequisites: what factoring is, basic multiplication, setting up equations from word problems
- Exclusions: no GCF factoring details, no AC method, no special products, no discussion of the Zero Product Property failing in other algebraic systems (matrices, modular arithmetic)
- Score: 8/10

---

## Candidate 10 — Why Two Equations Can Be Easier Than One
- Source: `math-prealgebra/chapters/05-systems-of-linear-equations.md`
- Topic: PREALGEBRA
- Hook: A problem with two unknowns seems harder than a problem with one — but sometimes giving yourself two variables makes the algebra simpler, not harder.
- Key case: A boat travels 36 miles downstream in 2 hours and 36 miles upstream in 3 hours. With one unknown speed, the equation produces a quadratic. With two unknowns (boat speed and current speed), the equations are both linear and the system solves cleanly: $b + c = 18$, $b - c = 12$, add: $2b = 30$, $b = 15$.
- The Question: Adding a second unknown to a problem should make it harder — now you have two things to find instead of one. In the boat-with-current setup, the one-unknown approach produces a quadratic; the two-unknown approach produces two linear equations. Why does more complexity in the naming lead to simpler algebra?
- Core idea: One unknown forces you to express both quantities in terms of a single variable — and the constraint that relates them enters the equation as a product, creating nonlinearity. Two unknowns let you state each constraint as a separate linear equation; the nonlinearity never appears because you never multiplied the two unknowns together.
- Visual object: Two number lines or coordinate axes — one showing the single-variable setup collapsing to a parabola, the other showing the two-variable system as two intersecting lines, with the intersection labeled as the solution.
- Manim move: compare
- Example seed: A jar has 25 coins (nickels and dimes) totaling $1.85. One-unknown: $0.05n + 0.10(25-n) = 1.85$ — manageable linear. Two-unknown: $n + d = 25$ and $0.05n + 0.10d = 1.85$ — same solution ($n = 13$, $d = 12$), same work. The two-unknown advantage becomes clear in the boat problem, where one-unknown forces a quadratic.
- Length band: 3–5 min
- Still lanes: geo (two-line intersection diagram vs. parabola comparison), geo (variable labeling showing the constraint structure)
- Prerequisites: what a system of equations is, basic linear equations, that quadratics are harder to solve than linear equations
- Exclusions: no substitution vs. elimination technique detail, no inconsistent/dependent system classification, no graphing method, no linear programming
- Score: 8/10

---

## Candidate 11 — Why Slope Times Negative Reciprocal Equals Perpendicular
- Source: `math-prealgebra/chapters/04-graphs.md`
- Topic: PREALGEBRA
- Hook: Two lines are perpendicular when their slopes multiply to $-1$ — a rule that looks arbitrary until you see it as a rotation.
- Key case: A ramp has slope $\frac{2}{3}$. A wall perpendicular to the ramp has slope $-\frac{3}{2}$. Multiply: $\frac{2}{3} \times -\frac{3}{2} = -1$. The rule works — but why does rotating a line 90° change its slope from $m$ to $-\frac{1}{m}$?
- The Question: Parallel lines have the same slope — that feels obvious (same tilt, same steepness). But perpendicular lines have slopes that are negative reciprocals, not negatives or reciprocals alone. Why does a 90° rotation produce exactly the flip-and-negate of slope?
- Core idea: Rotating a line 90° swaps rise and run (because what was vertical becomes horizontal) and introduces a sign change (because the rotation reverses one direction). Slope is rise/run; after rotation, slope is $-\text{run}/\text{rise} = -1/(\text{rise}/\text{run}) = -1/m$.
- Visual object: A right triangle on the coordinate plane — rotating the triangle 90° shows the legs swapping roles, and the new slope visibly becomes the negative reciprocal.
- Manim move: rotate
- Example seed: A wheelchair ramp rises 1 foot for every 4 feet of horizontal run: slope $\frac{1}{4}$. A support beam perpendicular to the ramp has slope $-4$. Verify: $\frac{1}{4} \times (-4) = -1$. Sketch both on graph paper to confirm they meet at a right angle.
- Length band: 2–3 min
- Still lanes: geo (right triangle rotation on coordinate axes), geo (slope-as-ratio labeled before and after 90° turn)
- Prerequisites: what slope is (rise over run), the coordinate plane, basic fractions
- Exclusions: no Pythagorean theorem proof, no dot-product formalism, no non-Euclidean geometry aside, no writing equations of perpendicular lines
- Score: 8/10
