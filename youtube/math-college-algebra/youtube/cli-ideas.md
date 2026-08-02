# College Algebra — CLI Video Ideas ("X with Claude")

## Candidate 01 — Build a Compound Interest Comparator with Claude

- Source: math-college-algebra/chapters/06-exponential-and-logarithmic-functions.md
- Lane: BUILD (Claude Code)
- Hook: Compounding once a year vs. continuously isn't a small difference when you run it out 30 years. Claude writes the calculator in under 20 lines, and the animated comparison reveals how much the compounding frequency matters.
- The artifact: a Python script that computes A = P(1+r/n)^(nt) for n = 1, 2, 4, 12, 365, and continuous (Pe^{rt}), then animates growth curves for each on the same axes from t=0 to t=30. P=$1000, r=7%. Labels on each curve show final value. Animated reveal from left to right.
- Prompt seed: `claude "Write a Python script that plots compound interest growth for P=1000, r=0.07, t=0 to 30 years, for compounding frequencies: annual (n=1), quarterly (n=4), monthly (n=12), daily (n=365), and continuous (P*exp(r*t)). Plot all curves on the same axes. Animate the curves drawing from left to right using matplotlib. Label each curve with its final value at t=30. Save as mp4."`
- Read / check: Verify annual → ~$7612, monthly → ~$8116, continuous → ~$8166. Check that the e-based continuous formula is implemented correctly. Confirm all curves are distinct and legible. Verify the animation timing is clear.
- Human supplies: Nothing — fully synthetic.
- Output medium: screen-recording mp4 (animated multi-curve growth chart)
- The change: Add a "rule of 72" annotation — for each compounding frequency, show the predicted doubling time (72/r%) next to the actual doubling time derived from the plot.
- Teardown angle: The difference between annual and continuous compounding shrinks rapidly with frequency — daily and continuous are nearly identical. The base e emerges naturally as the limit, making it "the natural base" in a concrete financial sense.
- Exclusions: Tax treatment of interest; inflation adjustment; derivation of e from first principles.
- Score: 9/10

---

## Candidate 02 — Animate Birthday Paradox Probability with Claude

- Source: math-college-algebra/chapters/13-sequences-probability-and-counting-theory.md
- Lane: BUILD (Claude Code)
- Hook: In a room of 23 people, there's a 50%+ chance two share a birthday — most people refuse to believe it. Claude computes and animates the probability climbing from 0% to 99% as room size grows.
- The artifact: a Python script that computes P(at least one shared birthday) = 1 - 365!/((365-n)!·365^n) for n = 2 to 70, then animates the probability climbing as a bar or line chart. Marks 50% threshold with a red line. Annotation shows the room size (23) where it first crosses 50%.
- Prompt seed: `claude "Compute the birthday paradox probability: P(n) = 1 - (365*364*...*(365-n+1)) / 365^n for n=2 to 70. Use Python's math.prod or a loop. Plot P(n) as an animated bar chart growing from n=2 to n=70. Mark a red horizontal line at 0.5. Annotate the first n where P(n) >= 0.5. Save as mp4."`
- Read / check: Verify P(23) ≈ 0.5073 and P(70) ≈ 0.9992. Check for numerical overflow — use logarithms if needed for large products. Confirm the red 50% line is clearly visible. Verify the animation pauses at n=23 with an annotation.
- Human supplies: Nothing — fully synthetic.
- Output medium: screen-recording mp4 (animated bar chart with threshold marker)
- The change: Simulate 10,000 random rooms of 23 people and show empirical probability vs. theoretical — demonstrating the complement probability approach validates against simulation.
- Teardown angle: The complement trick (P = 1 - P(no match)) makes an intractable direct calculation easy. This is the practical power of the complement — computing what you don't want is often far simpler.
- Exclusions: Generalized birthday problems (non-uniform distributions); cryptographic hash collision applications; full combinatorics derivation.
- Score: 9/10

---

## Candidate 03 — Plot Radioactive Decay and Find Half-Life with Claude

- Source: math-college-algebra/chapters/06-exponential-and-logarithmic-functions.md
- Lane: BUILD (Claude Code)
- Hook: The radioactive decay data in the chapter (1000 → 750 → 562 → 422 counts per hour) follows an exponential with ratio 0.75. Claude fits the model, finds the exact half-life, and animates the decay curve.
- The artifact: a Python script that: (1) fits N(t) = 1000·0.75^t to the data using numpy, (2) solves for half-life: t_{1/2} = ln(2)/ln(1/0.75) ≈ 2.41 hours, (3) animates the decay curve from t=0 to t=10 with data points plotted, a vertical marker at half-life, and a horizontal marker at N=500.
- Prompt seed: `claude "Fit an exponential decay model N(t) = N0 * b^t to the data: t=[0,1,2,3], N=[1000,750,562,422]. Use numpy curve_fit or direct calculation. Compute the half-life as log(0.5)/log(b). Animate the decay curve from t=0 to t=10. Mark the half-life point with a vertical and horizontal line. Show the data points as red dots. Label N0, half-life on the plot. Save as mp4."`
- Read / check: Verify b ≈ 0.75, half-life ≈ ln(2)/ln(4/3) ≈ 2.41 hours. Check the fit matches all four data points. Confirm the vertical line at t=2.41 intersects the curve at N=500. Verify the animation direction (decaying left to right).
- Human supplies: Nothing — fully synthetic. The data is from the chapter's example and is analytic.
- Output medium: Manim or screen-recording mp4 (animated decay curve with data markers)
- The change: Add a second decay curve with a different half-life (e.g., carbon-14's 5730 years, rescaled) and compare the two decay rates on the same axes.
- Teardown angle: The logarithm is the inverse that undoes the exponential — to find half-life from a decay ratio, you take the logarithm. The inverse function does real work here, not just symbolic algebra.
- Exclusions: Derivation of decay law from differential equations; quantum mechanical interpretation; radioactive chains.
- Score: 8/10

---

## Candidate 04 — Build a Systems of Equations Solver with Visualization with Claude

- Source: math-college-algebra/chapters/11-systems-of-equations-and-inequalities.md + chapters/10-further-applications-of-trigonometry.md
- Lane: BUILD (Claude Code)
- Hook: Two cyclists (Aiya, Boris) meet after 1 hour 40 minutes. Three methods give the same intersection point — but Claude also animates the cyclists moving toward each other on the road. The intersection on the graph IS the meeting point.
- The artifact: a Python script using sympy to solve the system {a(t)=18t, b(t)=50-12t} symbolically, then animates two curves crossing on a time-position plot. A second animation shows two dots moving along a number line, meeting at mile 30 at t=5/3 hours.
- Prompt seed: `claude "Use sympy to solve the system: a = 18*t and b = 50 - 12*t simultaneously (find t and position). Then create two matplotlib animations: 1) Plot a(t) and b(t) from t=0 to 2, animate lines drawing from left to right, mark the intersection point. 2) Animate two dots on a number line 0-50, one moving right at 18/hr, one moving left at 12/hr, pausing when they meet. Save both as mp4."`
- Read / check: Verify t=5/3 hours ≈ 1.667 hours, position=30 miles. Confirm sympy produces exact fractions. Check both animations converge to the same point. Verify the number-line animation scales correctly (1 hour = appropriate pixel distance).
- Human supplies: Nothing — fully synthetic.
- Output medium: screen-recording mp4 (dual animated visualization)
- The change: Add a third scenario — a slow headwind that changes Boris's speed to 12-2t — making the system nonlinear and showing where graphical solution is necessary.
- Teardown angle: The intersection point is the geometric form of the algebraic solution — both methods answer the same question. Real-world interpretation (the meeting point on the road) is what makes the algebra meaningful.
- Exclusions: Matrix methods for larger systems; linear programming; 3D systems.
- Score: 8/10

---

## Candidate 05 — Animate Conic Sections from a Cone with Claude

- Source: math-college-algebra/chapters/12-analytic-geometry.md
- Lane: BUILD (Claude Code)
- Hook: Slicing a cone at different angles produces circles, ellipses, parabolas, and hyperbolas — four seemingly different shapes from one operation. Claude animates the rotating cut plane and the resulting conic.
- The artifact: a Manim 3D animation showing a cone being sliced by a plane that rotates from horizontal (circle) through tilted (ellipse) through vertical-to-axis (parabola) through steeper (hyperbola). For each angle, the slice's equation appears in a side panel.
- Prompt seed: `claude "Create a Manim 3D animation showing a double cone being sliced by a plane at four angles: 0° (circle), 30° (ellipse), 90° (parabola), 120° (hyperbola). For each cut: rotate the cutting plane to the correct angle, show the intersection curve highlighted in red, and display the standard-form equation in a text panel on the right. Transition smoothly between cuts."`
- Read / check: Verify the four cutting angles produce the correct conic sections geometrically. Check the standard-form equations are correct: circle x²+y²=r², ellipse x²/a²+y²/b²=1, parabola y=ax², hyperbola x²/a²-y²/b²=1. Confirm 3D render is clear and not occluded.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim 3D (animated rotating cut plane)
- The change: Show how the same four conics appear in physics: circular orbits, elliptical planetary orbits, parabolic projectile paths, hyperbolic escape trajectories.
- Teardown angle: The four conics are not four different objects — they are one object (a cone) seen from four angles. The algebraic unification (the general second-degree equation Ax²+Bxy+Cy²+...=0) is what lets you classify any conic from its equation alone.
- Exclusions: Polar form of conics; rotated conics; degenerate cases (point, line, two lines).
- Score: 8/10

---

## Candidate 06 — Compute and Animate a Geometric Series Sum with Claude

- Source: math-college-algebra/chapters/13-sequences-probability-and-counting-theory.md
- Lane: BUILD (Claude Code)
- Hook: The repeating decimal 0.363636... equals 4/11 exactly. Claude derives this using the infinite geometric series formula, then animates each term being added, converging to the fraction.
- The artifact: a Python script that: (1) computes partial sums of 0.36 + 0.0036 + 0.000036 + ... (geometric with r=0.01), showing convergence to 4/11, (2) animates a number line from 0 to 1 with partial sums landing as dots, converging to the marked 4/11 target.
- Prompt seed: `claude "Compute partial sums of the geometric series: S = sum from k=0 to N of 0.36 * 0.01^k, for N=0 to 12. Print each partial sum and abs error from fractions.Fraction(4,11). Animate a number line from 0 to 0.5 showing each partial sum landing as a dot, with the 4/11 target marked in red. Show convergence. Save as mp4."`
- Read / check: Verify S = 0.36/(1-0.01) = 0.36/0.99 = 4/11 ≈ 0.3636... Check that fractions.Fraction(4,11) = 4/11 exactly. Verify partial sums converge monotonically (all terms positive). Confirm the number line scale and animation are legible.
- Human supplies: Nothing — fully synthetic.
- Output medium: screen-recording mp4 (animated number line convergence)
- The change: Show the divergent series 1+2+4+8+... on the same style plot, demonstrating why the |r|<1 condition is necessary and what happens when it fails.
- Teardown angle: An infinite sum can equal a finite fraction because the terms shrink fast enough. This is counterintuitive but exact — the formula S = a₁/(1-r) requires no approximation when |r|<1.
- Exclusions: Real analysis convergence theorems; p-series; alternating series.
- Score: 7/10

---

## Candidate 07 — Animate Trigonometric Identities Visually with Claude

- Source: math-college-algebra/chapters/09-trigonometric-identities-and-equations.md
- Lane: BUILD (Claude Code)
- Hook: Every trig identity is a geometric statement. sin²θ + cos²θ = 1 is just Pythagoras on the unit circle. Claude draws the unit-circle proof, making the algebra visible.
- The artifact: a Manim animation showing the unit circle. A point P = (cosθ, sinθ) sweeps around. At each position: a vertical line drops from P to the x-axis (length = sinθ), a horizontal line goes to the y-axis (length = cosθ), and a label shows sin²θ + cos²θ building to 1. A side panel shows the angle-addition identity for sin(α+β) derived geometrically using a right-triangle construction.
- Prompt seed: `claude "Create a Manim animation of the unit circle showing: 1) A point sweeping from 0 to 2*pi, with sin and cos labeled as the y and x coordinates. 2) A right triangle with legs labeled sin(theta) and cos(theta), hypotenuse = 1. 3) An animated equation showing sin^2 + cos^2 = 1 with each term's value updating as the point sweeps. Keep it under 60 seconds."`
- Read / check: Verify sin²θ + cos²θ = 1 at several angle values in the animation. Check the legs of the triangle are labeled correctly (cos on x, sin on y). Confirm the equation updates dynamically as the angle changes. Verify the animation loops cleanly.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim (animated unit circle with dynamic equation)
- The change: Derive the double-angle formula sin(2θ) = 2sinθcosθ geometrically using the angle-sum identity with α=β=θ.
- Teardown angle: Trig identities are not memorization tasks — they are geometric facts. The unit circle picture generates the entire library from two formulas and one picture.
- Exclusions: Full derivation of all identities; solving trig equations; inverse trig.
- Score: 7/10

---

## Candidate 08 — Build a Power vs. Exponential Race with Claude

- Source: math-college-algebra/chapters/06-exponential-and-logarithmic-functions.md
- Lane: BUILD (Claude Code)
- Hook: x¹⁰⁰ vs. 1.01^x — the exponential looks tiny at first, then wins. Claude plots the crossover and animates how far ahead the exponential eventually gets.
- The artifact: a Python script that plots y = x^100 and y = 1.01^x on the same axes over a range where the crossover is visible. Animates the two curves from x=0 outward, with a vertical marker sweeping to where e^x overtakes. Shows the ratio 1.01^x / x^100 approaching infinity on a second subplot.
- Prompt seed: `claude "Plot two functions: y1 = x**10 (polynomial) and y2 = 1.5**x (exponential) over x=0 to 50. Animate both curves drawing from left to right. Mark where they intersect. Add a second subplot showing the ratio y2/y1 from the first intersection onward. Title: 'Exponential eventually beats every polynomial'. Save as mp4."`
- Read / check: Verify intersection exists and exponential eventually dominates. Check ratio subplot shows monotonic increase after the crossover. Confirm scale allows both curves to be visible (may need log scale after crossing). Verify the animation makes the crossover moment visually clear.
- Human supplies: Nothing — fully synthetic.
- Output medium: screen-recording mp4 (dual-panel animated comparison)
- The change: Use 1.001^x vs x^1000 to show the same pattern — even with a barely-above-1 base and a huge polynomial degree, the exponential wins eventually.
- Teardown angle: The key word is "eventually" — exponential growth is not initially fast. The deceptive part of exponential growth is the long slow start before the accelerating phase. This is the core intuition failure in pandemic forecasting, compound interest, and population growth.
- Exclusions: Formal proof using L'Hôpital's rule; logarithms of the functions; asymptotic notation.
- Score: 7/10

---

## Candidate 09 — Animate Pascal's Triangle and the Binomial Theorem with Claude

- Source: math-college-algebra/chapters/13-sequences-probability-and-counting-theory.md
- Lane: BUILD (Claude Code)
- Hook: (a+b)^10 expands into 11 terms with coefficients from Pascal's triangle. Claude generates the triangle, animates it being built row by row, and reveals how each row gives binomial coefficients.
- The artifact: a Manim animation building Pascal's triangle row by row (up to row 10), with each entry computed as the sum of the two above. For a chosen row n, a second animation expands (a+b)^n showing each term with its coefficient from the triangle row. Final output: both the triangle and the expansion displayed side by side.
- Prompt seed: `claude "Create a Manim animation building Pascal's triangle up to row 10. Show each row appearing one at a time, with each entry computed as the sum of the two above (animate the addition arrows). Then animate (a+b)^5 expansion showing each term with its coefficient from row 5 of the triangle. Use colors: row 5 highlighted in orange. Title: 'Pascal's Triangle and the Binomial Theorem'."`
- Read / check: Verify Pascal's triangle rows are correct up to row 10. Check row 5 = [1,5,10,10,5,1]. Confirm (a+b)^5 = a^5 + 5a^4b + 10a^3b^2 + 10a^2b^3 + 5ab^4 + b^5. Verify addition arrows point to correct parent entries.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim (animated triangle construction + expansion reveal)
- The change: Show that the sum of each row is 2^n — connecting Pascal's triangle to counting: each row counts all subsets of n items (one for each size).
- Teardown angle: Pascal's triangle is not a memorization device — it is a combinatorial structure where each entry C(n,k) counts something real (the number of paths from top to entry, the number of k-subsets). The algebra (binomial theorem) and the combinatorics (counting) are the same object.
- Exclusions: Probability applications of binomial distribution; connection to polynomial roots; multinomial theorem.
- Score: 7/10

---

## Candidate 10 — Measure Matrix System Solutions with Claude

- Source: math-college-algebra/chapters/11-systems-of-equations-and-inequalities.md
- Lane: BUILD (Claude Code)
- Hook: A 2×2 system can have one solution, no solution, or infinitely many — and the determinant tells you which. Claude computes the determinant for three systems and visualizes the geometric meaning of each case.
- The artifact: a Python script using sympy to solve three 2×2 systems: one with unique solution, one inconsistent (parallel lines), one dependent (same line). For each: print the solution type, print the determinant, and animate the two lines on the same graph (intersecting, parallel, or coincident).
- Prompt seed: `claude "Using sympy, solve three 2x2 linear systems: 1) {2x+y=5, x-y=1} (unique), 2) {2x+y=5, 2x+y=7} (inconsistent), 3) {2x+y=5, 4x+2y=10} (dependent). For each: compute the determinant of the coefficient matrix, classify the system, and create a matplotlib plot showing both lines. Animate all three plots appearing in sequence. Save as mp4."`
- Read / check: Verify system 1 gives det=−3, unique solution (x=2, y=1). Verify system 2 gives det=0, parallel lines. Verify system 3 gives det=0, coincident lines. Check the geometric plots match the algebraic classification. Confirm the determinant values drive the classification correctly.
- Human supplies: Nothing — fully synthetic.
- Output medium: screen-recording mp4 (three-panel animated line plots)
- The change: Extend to a 3×3 system and show the determinant computed by Cramer's rule — scaling from 2D geometry (line intersections) to 3D geometry (plane intersections).
- Teardown angle: The determinant is not just a formula — it is the geometric volume of the parallelogram formed by the coefficient vectors. When it's zero, the vectors are dependent and the system is degenerate. Algebra and geometry are telling the same story.
- Exclusions: LU decomposition; Gaussian elimination; matrix inverses.
- Score: 6/10
