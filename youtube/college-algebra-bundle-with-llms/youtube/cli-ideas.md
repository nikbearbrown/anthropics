# College Algebra Bundle with LLMs — CLI Video Ideas ("X with Claude")

---

## Candidate 01 — "Plot the Number Hierarchy with Claude: Every Number You Will Ever Need"
- Source: college-algebra-bundle-with-llms/chapters/01-prerequisites.md (LLM Exercise 1.1)
- Lane: BUILD (Claude Code)
- Hook: Is every rational number an integer? Most students say yes. The nested set diagram reveals exactly where that claim falls apart — and why the question drove the invention of irrational numbers.
- The artifact: An animated Manim scene showing the real number hierarchy as nested rectangles (N ⊂ W ⊂ Z ⊂ Q ⊂ R), with labeled example values flying into their correct regions one by one: 5 lands in N, 0 lands in W-not-N, -7 lands in Z-not-W, 2/3 lands in Q-not-Z, √2 lands in R-not-Q. Final frame shows all examples positioned with the subset chain labeled.
- Prompt seed: `claude "Write a Manim scene that animates the real number hierarchy as nested rectangles. Animate example values flying into their correct regions: 5 → Naturals, 0 → Whole-not-Natural, -7 → Integers-not-Whole, 2/3 → Rationals-not-Integer, √2 → Irrationals. Label each region and show the subset chain N⊂W⊂Z⊂Q⊂R. Keep under 60 lines."`
- Read / check: Verify the nested rectangles are visually nested (not overlapping incorrectly); check the irrational region (R-not-Q) is clearly separate from Q; verify √2 is labeled as irrational and placed correctly; run the Manim scene and confirm all 5 value animations render without z-order errors.
- Human supplies: Nothing — fully synthetic. The hierarchy and example values are deterministic mathematical facts, not measurements.
- Output medium: Manim (animated)
- The change: Add a 6th value: π (irrational, transcendental). Animate it flying into the irrational region alongside √2, then add a label distinguishing algebraic irrationals from transcendental ones — previewing what's beyond the real number line.
- Teardown angle: Each extension of the number system was forced by a question the previous set could not answer. The diagram is not taxonomy — it is a history of mathematical necessity. The √2 proof (ancient Greek, still true) is the moment irrationality became unavoidable.
- Exclusions: Complex numbers (Chapter 2 material), transfinite cardinals, the Cantor diagonalization proof, historical attribution debates.
- Score: 9/10

---

## Candidate 02 — "Debug PEMDAS Ambiguity with Claude: When the Convention Breaks"
- Source: college-algebra-bundle-with-llms/chapters/01-prerequisites.md (LLM Exercise 1.2)
- Lane: BUILD (Claude Code)
- Hook: 8 ÷ 2(2+2) — is the answer 1 or 16? The internet fights about this every year. Claude can argue both sides. The fight reveals something true about mathematical notation that most textbooks avoid saying.
- The artifact: A Manim animation showing the two parse trees for 8 ÷ 2(2+2) — one tree reads left-to-right (giving 16), the other treats 2(2+2) as a grouped unit (giving 1). Each tree highlights where the ambiguity lives: the implicit multiplication vs. explicit division precedence. Final frame shows the resolution: both answers are defensible under different notation conventions, and the expression is badly written.
- Prompt seed: `claude "Write a Manim scene that shows two parse trees for the expression 8 ÷ 2(2+2). Tree 1: left-to-right evaluation (8÷2=4, then 4×4=16). Tree 2: implicit-multiplication-first (2(2+2)=8, then 8÷8=1). Animate each tree building from the expression left to right. Label the fork point where the two conventions diverge. Show both results. No winner — show why the expression is ambiguous."`
- Read / check: Verify both parse trees are mathematically valid representations; check the fork point is labeled clearly; verify the animation builds left-to-right (not random order); confirm neither tree is marked "correct" — the lesson is the ambiguity itself.
- Human supplies: Nothing — fully synthetic. The ambiguity is a known feature of PEMDAS notation.
- Output medium: Manim (animated)
- The change: Ask Claude to rewrite the expression unambiguously two ways: once to get 16 (explicit parentheses: (8÷2)×(2+2)) and once to get 1 (explicit parentheses: 8÷(2×(2+2))). Show both rewrites alongside the original — the resolution is always: write the parentheses you mean.
- Teardown angle: PEMDAS is a social contract, not a mathematical law. The expression 8÷2(2+2) violates the contract by leaving the convention ambiguous. The lesson for algebra students: never write an expression where the reader must guess which convention you intended.
- Exclusions: Full history of notation conventions, the vs-Wolfram Alpha debate, implied multiplication in LaTeX vs. programming languages.
- Score: 8/10

---

## Candidate 03 — "Animate Exponent Rules with Claude: Why a⁰ = 1 Is Not a Definition"
- Source: college-algebra-bundle-with-llms/chapters/01-prerequisites.md (LLM Exercise 1.3)
- Lane: BUILD (Claude Code)
- Hook: a⁰ = 1 is taught as a fact. It is actually a forced consequence — the only value that makes the quotient rule consistent. Claude can derive it live, and then animate it.
- The artifact: A Manim animation showing the zero-exponent derivation from the quotient rule: a^m / a^m = 1 (by division) and a^(m-m) = a^0 (by quotient rule), therefore a^0 = 1. Followed by a 7-rule summary table animating in row by row: product, quotient, power, zero exponent, negative exponent, product-to-a-power, quotient-to-a-power. Each rule shows a concrete numerical example alongside the general form.
- Prompt seed: `claude "Write a Manim scene that: (1) derives a^0 = 1 from the quotient rule by showing a^m/a^m simultaneously by division (=1) and by the quotient rule (=a^0), with an equals sign connecting both derivations; (2) animates a summary table of all 7 exponent rules appearing row by row, each with a general formula and a numerical example. Keep under 70 lines."`
- Read / check: Verify the derivation shows both paths arriving at the same result (not just stating the rule); check the numerical examples are correct (spot-check: 2^3 × 2^4 = 2^7 = 128); verify the negative-exponent rule shows the reciprocal, not a negative; confirm all 7 rules are present in the table.
- Human supplies: Nothing — fully synthetic. The exponent rules are deterministic.
- Output medium: Manim (animated)
- The change: Add an 8th "rule" that is NOT a rule: (a+b)^n ≠ a^n + b^n. Animate a concrete counterexample: (2+3)^2 = 25 but 2^2 + 3^2 = 13. Mark it in red with an X. This is the most common exponent error — naming it once cements it.
- Teardown angle: Every exponent rule is a consequence of the definition — a^n means a multiplied by itself n times. Nothing is arbitrary. The zero-exponent and negative-exponent rules follow from the quotient rule by the same counting argument. The animation makes this visible; the textbook table does not.
- Exclusions: Complex exponents, Euler's formula, logarithm connection (Chapter 6 material), calculator behavior edge cases.
- Score: 9/10

---

## Candidate 04 — "Factor Polynomials with Claude: The Decision Tree That Replaces Guessing"
- Source: college-algebra-bundle-with-llms/chapters/01-prerequisites.md (LLM Exercise 1.4)
- Lane: BUILD (Claude Code)
- Hook: Factoring feels like guessing. The chapter's decision tree converts it into recognition — if you can name the pattern, you know the technique. Claude builds the decision tree live.
- The artifact: A Manim animation of a factoring decision tree — 7 rows, each showing: pattern to recognize → technique → example in → example out. The tree animates as a flowchart with branching: "GCF first? → yes: pull GCF → then recurse on remainder; trinomial with a=1? → yes: find two numbers..." Each example is a specific polynomial that transforms as you watch.
- Prompt seed: `claude "Write a Manim scene that animates a factoring decision flowchart. 7 nodes: GCF, Trinomial a=1, Trinomial a≠1 (grouping), Difference of squares, Perfect square trinomial, Sum of cubes, Difference of cubes. For each node, show the recognition pattern, the technique name, and one example: input polynomial → factored output. Animate the flowchart building top-down, then show an example polynomial walking through the tree to its correct node."`
- Read / check: Verify all 7 factoring patterns are present; check the worked examples are correct (spot-check: x^3 - 8 = (x-2)(x^2+2x+4)); verify the tree branching logic is correct (GCF comes first, then pattern matching); run the animation and confirm the "walk through the tree" demonstration reaches the correct leaf.
- Human supplies: Nothing — fully synthetic. The factoring techniques are deterministic.
- Output medium: Manim (animated)
- The change: Add a terminal node: "Not factorable over ℤ — irreducible polynomial." Show a specific example (x^2 + x + 1) walking through the tree and failing all pattern checks, arriving at the irreducible node. This answers LLM Exercise 1.4's question about polynomials that cannot be factored.
- Teardown angle: Factoring converts sums into products. Products are what let you find zeros, simplify rational expressions, and solve equations. Sums don't do that. The decision tree is not a memorization aid — it is a pattern-recognition index for the algebraic move that unlocks everything downstream.
- Exclusions: Factoring over the reals (irrational roots), Eisenstein criterion, polynomial rings beyond college algebra scope.
- Score: 9/10

---

## Candidate 05 — "Visualize Domain Restrictions with Claude: The Hole That Travels"
- Source: college-algebra-bundle-with-llms/chapters/01-prerequisites.md (LLM Exercise 1.5)
- Lane: BUILD (Claude Code)
- Hook: Simplify (x^2-9)/(x+3) and you get x-3. But (x-3) at x=-3 gives -6. The original expression is undefined there. The restriction travels with the simplification even after the denominator disappears — and the graph shows a hole where the algebra shows nothing.
- The artifact: A Manim animated side-by-side graph of y = (x^2-9)/(x+3) and y = (x-3), both on the same axes. The left panel animates a visible hole at x=-3 (hollow circle); the right panel shows no hole (the simplified form). A cursor sweeps to x=-3 on both panels simultaneously — the left panel shows "undefined," the right shows "-6." Text annotation explains the restriction x≠-3 carried forward from the original denominator.
- Prompt seed: `claude "Write a Manim scene showing side-by-side graphs: left panel y=(x²-9)/(x+3) with a visible hole (open circle) at x=-3; right panel y=(x-3) with no hole. Animate a vertical cursor sweeping to x=-3 on both panels simultaneously. At x=-3: left panel shows 'undefined,' right panel shows '-6'. Add text: 'The restriction x≠-3 travels from the original denominator.' Same axes and scale on both panels."`
- Read / check: Verify the hole at x=-3 is visually distinct (hollow circle, not filled); check the right panel has no hole; verify the cursor is synchronized between panels; confirm the text labels are correct and legible; run the scene and check both panels share the same axis scale.
- Human supplies: Nothing — fully synthetic. The graphical behavior is determined by the mathematical functions.
- Output medium: Manim (animated)
- The change: Add a third panel showing the graph of y=x+3 (the denominator) — animate the zero of the denominator at x=-3 highlighted in red, then draw a dotted vertical line from that zero up to the hole in the left panel. Shows geometrically why the restriction comes from the denominator's zero.
- Teardown angle: Simplification changes the form, not the restriction. The cancellation is legal everywhere except where the cancelled factor was zero. The restriction is the price of the simplification — and it is permanently due even when the denominator is no longer visible.
- Exclusions: Vertical asymptotes vs. holes (Chapter 5 rational functions material), removable vs. non-removable discontinuities (calculus framing), complex number zeros of denominators.
- Score: 9/10

---

## Candidate 06 — "Animate the Discriminant with Claude: Three Parabolas, Three Stories"
- Source: college-algebra-bundle-with-llms/chapters/02-equations-and-inequalities.md (LLM Exercise 2-C)
- Lane: BUILD (Claude Code)
- Hook: The discriminant b²-4ac tells you how many solutions a quadratic has before you solve it. Three cases, three geometric pictures — and most students have never seen why the algebra and the geometry agree.
- The artifact: A Manim animation showing three parabolas (all opening upward) transitioning through the three discriminant cases. Case 1: discriminant > 0, parabola crosses x-axis at two points (animated growing from vertex). Case 2: discriminant = 0, parabola touches at exactly one point. Case 3: discriminant < 0, parabola floats entirely above. For each case, the discriminant value and the number/type of solutions are labeled simultaneously. Then a transition showing a single parabola morphing continuously through all three cases as b changes.
- Prompt seed: `claude "Write a Manim scene showing three upward-opening parabolas illustrating the three discriminant cases for ax²+bx+c=0. For each: (1) b²-4ac>0: two real roots marked on x-axis; (2) b²-4ac=0: one repeated root (vertex touching x-axis); (3) b²-4ac<0: no real roots (parabola above x-axis). Label each with its discriminant case and solution count. Then animate a single parabola morphing from case 1→2→3 as b decreases from 6 to 0 to -6, a=1, c=5 fixed."`
- Read / check: Verify the morphing animation is mathematically correct (vertex moves up as discriminant decreases through zero); check the roots are marked at the correct x-positions for the first case; verify the transition passes cleanly through the tangent case (discriminant=0); confirm labels stay legible during the morphing transition.
- Human supplies: Nothing — fully synthetic. All parabola geometry is computable.
- Output medium: Manim (animated)
- The change: Extend the animation: when the parabola is in the complex-root case (case 3), show the complex roots as points on the complex plane (a separate small inset plot) — the conjugate pair at -b/2a ± imaginary. This bridges to the complex number introduction in Chapter 2.
- Teardown angle: The discriminant is a decision procedure, not an intermediate step. Compute it first. It tells you what to expect before you commit to the full quadratic formula. The three cases are not equally common in practice — the negative discriminant case is the one that forced the invention of complex numbers.
- Exclusions: The full completing-the-square derivation of the quadratic formula (separate animation candidate), cubic and quartic discriminants, Newton's method numerical approach.
- Score: 9/10

---

## Candidate 07 — "Build a Linear Function Slope Visualizer with Claude"
- Source: college-algebra-bundle-with-llms/chapters/04-linear-functions/01-m51269.md + chapters/03-functions.md
- Lane: BUILD (Claude Code)
- Hook: A linear function has a constant rate of change. Bamboo grows 1.5 inches per hour — that's a slope. Claude builds a live slope visualizer where you can watch the rate change as you adjust the parameters.
- The artifact: A Manim scene showing a linear function y = mx + b with animated slope triangle (rise over run labeled). An interactive-style animation sweeps m from -3 to 3, showing the line rotating around its y-intercept while the slope triangle updates live. When m=0, the line is horizontal and the slope triangle collapses to a point. Labels show slope value and the verbal interpretation ("rises 2 for every 1 right").
- Prompt seed: `claude "Write a Manim scene animating a linear function y=mx+b. Show: (1) the line for m=2, b=1 with a slope triangle (Δx=1, Δy=2 labeled 'rise=2, run=1'); (2) animate m sweeping from -3 to +3 while b stays at 1, with the slope triangle updating live and a label showing the current slope value; (3) highlight m=0 (horizontal) and m=1 (45°) as special cases with distinct colors."`
- Read / check: Verify the slope triangle dimensions match the current m value at each frame; check the rotation pivot is the y-intercept (not the origin); verify the m=0 special case renders as a horizontal line with the triangle collapsing; confirm labels are readable during the sweep animation.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim (animated)
- The change: Add a second line y = mx + b with a different b value — animate both lines simultaneously with the same m sweep, showing that parallel lines have the same slope regardless of y-intercept. Highlight the moment when the lines coincide (when b values are equal).
- Teardown angle: Slope is not just a number — it is the rate at which one quantity changes relative to another. The bamboo example (1.5 inches/hour) is a slope. The rental car cost ($0.20/mile) is a slope. The visual rotation shows why negative slope feels "downhill" and why zero slope is horizontal — the geometry makes the arithmetic intuitive.
- Exclusions: Slope-intercept vs. point-slope vs. standard form comparison (next section), systems of equations, linear regression fitting.
- Score: 8/10

---

## Candidate 08 — "Animate Exponential Growth with Claude: From Bacteria to Compound Interest"
- Source: college-algebra-bundle-with-llms/chapters/06-exponential-and-logarithmic-functions/01-m49356.md + chapters/06-exponential-and-logarithmic-functions.md
- Lane: BUILD (Claude Code)
- Hook: One bacterium divides every hour. After 24 hours: 16 million. The growth doesn't feel like multiplication because it doesn't happen one step at a time. Exponential growth is the animation that makes it visceral.
- The artifact: A Manim animation showing two panels: left panel is a bar chart growing step by step (bacteria count doubling each hour, bars growing vertically from 1 to 1024 over 10 steps, with a speed-up after step 7 to reach step 24). Right panel is the exponential curve y=2^x drawn from x=0 to x=24, with a moving point tracing it. A vertical dashed line at x=10 connects both panels. Numbers on the bars switch to scientific notation when they exceed 4 digits.
- Prompt seed: `claude "Write a Manim scene with two panels: LEFT: bar chart showing 2^n for n=0 to 10, bars growing one step at a time, labels switching to scientific notation above 9999. RIGHT: exponential curve y=2^x from 0 to 24 drawn continuously, with a point tracing it synchronized with the bar chart steps. A vertical dashed line at x=10 connects both panels. Include a counter showing current n and 2^n value."`
- Read / check: Verify the bar values are correct (check n=10: 1024, n=20: 1048576); check the scientific notation switch fires at the right bar; verify the point on the right panel is synchronized with the bar chart steps; confirm the curve from x=10 to x=24 is extrapolated correctly.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim (animated)
- The change: Add a third comparison: linear growth y=100x on the same right panel axes (dashed line), labeled "linear for comparison." Show when the exponential overtakes the linear — the crossing point. This makes the qualitative difference between linear and exponential visceral.
- Teardown angle: The bacteria table (1, 2, 4, 8...) doesn't feel like 16 million at step 24. The animation does. Exponential growth is unintuitive precisely because our intuition is calibrated to linear change — we expect an extra hour to add roughly the same amount it always has. The curve's shape is the correction.
- Exclusions: Logarithm definition and inverse relationship (second half of Chapter 6 — separate video), continuous compound interest formula derivation (calculus adjacent), base-e motivation.
- Score: 9/10

---

## Candidate 09 — "Plot the Quadratic Inequality Garden with Claude: Algebra Meets Geometry"
- Source: college-algebra-bundle-with-llms/chapters/02-equations-and-inequalities.md (LLM Exercise 2-F)
- Lane: BUILD (Claude Code)
- Hook: The garden optimization problem has three answers to three different questions — an equation, a vertex, and an inequality. All three are about the same 40 feet of fence. Animating them together shows why the same algebra produces different objects depending on what you ask.
- The artifact: A Manim scene with two panels. Left: top-down garden diagram with the house as one wall, perpendicular sides labeled x, parallel side labeled 40-2x — animates as x changes. Right: downward-opening parabola A=40x-2x^2 with animated elements: vertex point at (10, 200) appearing, horizontal dashed line at A=150 sweeping in, intersection points at x=5 and x=15 marked, the interval (5,15) shaded on the x-axis. The left panel animates a rectangle growing and shrinking in sync with x sweeping from 0 to 20.
- Prompt seed: `claude "Write a Manim scene with two synchronized panels. LEFT: top-down garden rectangle, house as top edge, perpendicular sides labeled x, parallel side labeled 40-2x. RIGHT: parabola A=40x-2x²; animate: (1) vertex appearing at (10,200) labeled 'max area=200 sq ft'; (2) dashed horizontal line at A=150; (3) intersection points at x=5 and x=15; (4) interval (5,15) shaded on x-axis. Synchronize: as x sweeps 0→20 on right, the left rectangle updates dimensions."`
- Read / check: Verify the parabola opens downward (not upward); check the vertex coordinates (10, 200) are correct; verify the intersection points at x=5 and x=15 are correct (solve 40x-2x^2=150: x^2-20x+75=0 → (x-5)(x-15)=0); confirm the left panel rectangle dimensions update correctly with the x sweep.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim (animated)
- The change: Add a third horizontal line at A=0 showing the zeros of the parabola (x=0 and x=20) — the physical constraint that the fence dimensions must be positive. This shows the feasible domain for the problem is (0, 20), not all real numbers.
- Teardown angle: The same piece of land is described three ways: an algebraic expression (A=40x-2x²), a quadratic extremum (vertex gives max area), and an inequality solution (interval where area exceeds 150). The animation makes concrete that these are not three different problems — they are three different questions about the same physical situation.
- Exclusions: Calculus optimization (derivative=0 approach), three-sided vs. four-sided fencing variations, dimensional analysis for non-constant-fence scenarios.
- Score: 8/10

---

## Candidate 10 — "Research the Discriminant's History with Claude: From Diophantus to the Quadratic Formula"
- Source: college-algebra-bundle-with-llms/chapters/02-equations-and-inequalities.md (AI Wayback Machine section)
- Lane: RESEARCH (Claude assistant)
- Hook: The quadratic formula is taught as a fact. It was discovered across 4000 years and three continents. Claude traces the lineage — from Babylonian geometry to Brahmagupta's rules to the 16th-century symbolic form — and the research brief becomes the vox-explainer's PROBLEM beat.
- The artifact: A sourced 4-stop historical timeline (Babylonians → Brahmagupta → Al-Khwarizmi → Cardano/Viète) with one key finding per stop: what they could solve, what notation they used, what they couldn't do that the next person could. Formatted as a markdown timeline with dates, names, and 1-sentence contributions. Verified against Wikipedia and the book's AI Wayback sections.
- Prompt seed: `claude "Research and synthesize the history of solving quadratic equations, in 4 stops: (1) Babylonian clay tablets (~1800 BCE) — what they computed geometrically; (2) Brahmagupta (628 CE, Brāhmasphuṭasiddhānta) — his rules including the problematic zero-case; (3) Al-Khwarizmi (9th century, Kitāb al-mukhtaṣar) — the word 'algebra' and the rhetorical form; (4) Symbolic notation (16th century, Viète/Cardano) — when we finally got x. Format as a markdown timeline. Cite Wikipedia article names for each figure. Flag any dates you are uncertain about."`
- Read / check: Cross-reference Brahmagupta's entry against Wikipedia "Brahmagupta" article; verify Al-Khwarizmi's connection to the word "algebra" (it comes from his title "al-jabr"); check that the 4-stop structure is coherent (each stop extends what the previous could not do); verify uncertainty flags are present for any contested dates.
- Human supplies: The chapter's AI Wayback Machine sections (Brahmagupta for Chapter 1, Diophantus for Chapter 2) as seed context — paste as project context. Human verification required for dates and attributions; Claude may conflate or midate historical figures.
- Output medium: slate (human fills with historical images or illustrations from Wikipedia commons)
- The change: Add a 5th stop: why the quadratic formula works but the quintic formula does not (Abel-Ruffini theorem, 1823). This is the forward pointer — the research brief becomes a preview of "why algebra has limits" that college algebra students won't see until abstract algebra.
- Teardown angle: The formula students memorize was discovered piecemeal across 4 millennia in three different mathematical traditions. The symbolic form (x = ...) is less than 500 years old. The conceptual content is ancient. Notation is not mathematics — it is mathematics made readable.
- Exclusions: Full history of complex number acceptance, the cubic formula (Cardano's full story), numerical methods for higher-degree polynomials.
- Score: 7/10

---

## Candidate 11 — "Animate Trigonometric Function Behavior with Claude: The Unit Circle in Motion"
- Source: college-algebra-bundle-with-llms/chapters/07-the-unit-circle-sine-and-cosine-functions.md + chapters/08-periodic-functions.md
- Lane: BUILD (Claude Code)
- Hook: The unit circle is a static diagram in every textbook. Animated, it becomes the machine that generates the sine and cosine curves — and the relationship between circular motion and wave functions becomes obvious.
- The artifact: A Manim scene with two panels: left panel shows a unit circle with a point moving counterclockwise. Right panel shows the sine curve being drawn by the y-coordinate of that point, and the cosine curve by the x-coordinate, both growing in real time as the point sweeps. The angle θ is labeled on the circle; the corresponding (cos θ, sin θ) values are labeled on the right panel's current position on each curve.
- Prompt seed: `claude "Write a Manim scene with two synchronized panels. LEFT: unit circle with a point moving counterclockwise from (1,0), angle θ labeled from origin. RIGHT: two curves drawn simultaneously as θ increases from 0 to 2π — top: y=sin(θ) traced by the point's y-coordinate; bottom: y=cos(θ) traced by the point's x-coordinate. Show dashed lines connecting: point's y-coordinate to the sine curve value, point's x-coordinate to the cosine curve value. Label current θ, sin(θ), cos(θ) values as numbers."`
- Read / check: Verify the point moves counterclockwise (not clockwise); check the dashed projection lines connect correctly (y-projection → sine curve, x-projection → cosine curve); verify the curves complete exactly one full period in one revolution; confirm that at θ=π/2 the sine value is 1 and cosine is 0.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim (animated)
- The change: Extend to θ = 4π (two full revolutions) and add a third curve: y=tan(θ), showing it shooting to ±∞ at θ=π/2. Animate the vertical asymptote appearing as the point approaches the x-axis on the unit circle.
- Teardown angle: The unit circle is not a definition — it is a visualization device. The sine function is the y-coordinate of periodic circular motion. The animation makes this correspondence visible in a way no static textbook diagram can. Once seen, the "why" of periodicity is obvious: the circle repeats.
- Exclusions: Inverse trig functions (Chapter 9 material), trigonometric identities proofs, law of sines/cosines applications (Chapter 10).
- Score: 8/10

---

## Candidate 12 — "Build a Compound Interest Calculator with Claude: The Math Behind the Compounding Surprise"
- Source: college-algebra-bundle-with-llms/chapters/06-exponential-and-logarithmic-functions.md
- Lane: BUILD (Claude Code)
- Hook: $2000 at 6% for 30 years becomes $11,486 — not $5,600 as simple interest would give. The difference is compounding, and it grows quadratically different from what your intuition predicts. Claude builds the calculator; the animation reveals the gap.
- The artifact: A Python script that computes compound interest for any principal, rate, and time period, plus a Manim animation comparing compound growth (A = P(1+r/n)^nt) vs. simple interest (A = P(1+rt)) on the same axes, with the gap between the two curves growing and shaded. Key points labeled: 10-year value, 20-year value, 30-year value. A table printed to terminal showing the comparison at each decade.
- Prompt seed: `claude "Write: (1) a Python function compound_vs_simple(P, r, t_max, n=12) that returns two arrays: compound interest values and simple interest values for years 0 to t_max; (2) a Manim scene that plots both curves on the same axes, shades the gap between them, and labels the gap values at t=10, 20, 30 years. Use P=2000, r=0.06, t_max=30. Print a terminal table showing both values and the gap at each decade."`
- Read / check: Verify the compound interest formula implementation (A = P(1+r/n)^(nt), n=12 for monthly); check terminal output for year 30: compound should be ~$11,486, simple should be $5,600; verify the shaded gap is visible and growing; confirm the Manim scene and the Python script use consistent values.
- Human supplies: Nothing — fully synthetic. The compound interest formula is deterministic.
- Output medium: screen-recording mp4 (terminal showing the Python output) + Manim (animated, for the output beat showing the growth curves)
- The change: Add a third curve: A = Pe^(rt) (continuous compounding). At 6% for 30 years, compare monthly compounding vs. continuous compounding — the difference is smaller than most students expect, demonstrating why the compounding frequency matters less than the rate itself.
- Teardown angle: The early-start advantage is not intuitive from the formula. A 22-year-old saving $200/month from graduation vs. a 32-year-old saving the same amount — the 10 extra years at the beginning are worth more than all the contributions alone, because the compounding has more time to run. The animation makes this visible; the table quantifies it.
- Exclusions: Logarithm derivation of doubling time (Rule of 72 — separate video candidate), amortization/loan payoff formulas, present value/future value NPV calculations.
- Score: 8/10
