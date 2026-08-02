# Math Algebra — CLI Video Ideas ("X with Claude")

## Candidate 01 — "Explore the Quadratic Vertex and Optimization with Claude: LLM Exercise 5.x"
- Source: math-algebra/chapters/05-polynomial-and-rational-functions.md + chapters/02-equations-and-inequalities.md
- Lane: BUILD (Claude Code)
- Hook: The farmer has 100 feet of fencing and wants maximum area — the quadratic structure reveals the answer is always a square, for any fixed perimeter. Plot it, animate the vertex sweeping, and watch the geometry make the algebra obvious.
- The artifact: An animated Manim visualization of the farmer optimization problem — the area function A(x) = -x² + 50x plotted as a downward parabola, the vertex animating to (25, 625), a side-by-side panel showing the rectangle at x=10, x=25, x=40 with area labeled, and a dynamic annotation showing "area maximized when rectangle is square."
- Prompt seed: `claude "Generate a Python/Manim animation for the fencing optimization problem: A(x) = x(50-x) = -x^2 + 50x (perimeter=100 ft). Animation steps: (1) Draw the parabola from x=0 to x=50. (2) Mark the vertex at (25, 625) with a dot and annotation 'maximum area = 625 sq ft when x=y=25 ft.' (3) Side panel: animate three rectangles (x=10, x=25, x=40) showing how area changes. (4) Show the vertex formula x = -b/2a = -50/(2×(-1)) = 25. Animate the formula computing step by step."`
- Read / check: Verify the vertex is correctly placed at x=25 (not x=50). Confirm the side panel rectangles are drawn to scale relative to each other. Check that the vertex formula animation shows the substitution steps clearly — this is the procedural content students need to see.
- Human supplies: Nothing — fully synthetic. The LLM Exercise version would ask the student to try it with different perimeters.
- Output medium: Manim (animated parabola + rectangle comparison panel)
- The change: Animate the same optimization with a perimeter of 200 feet — showing the vertex shifts but the "always a square" conclusion holds, revealing the general principle.
- Teardown angle: The quadratic structure is not just a formula — it encodes the geometry of optimization, and the vertex is where the geometry and the algebra say the same thing.
- Exclusions: Full calculus derivation (this is algebra), Lagrange multipliers, constrained optimization in multiple dimensions.
- Score: 9/10

## Candidate 02 — "Investigate the PEMDAS Ambiguity with Claude: LLM Exercise 1.2"
- Source: math-algebra/chapters/01-prerequisites.md (LLM Exercise 1.2)
- Lane: BUILD (Claude Code)
- Hook: 8 ÷ 2(2 + 2) — is the answer 1 or 16? Both are defensible. The expression exposes a real ambiguity in mathematical notation that a well-prompted Claude can argue both sides of.
- The artifact: An animated Manim visualization showing the two parse trees for 8 ÷ 2(2+2) — tree A: (8 ÷ 2) × (2+2) = 16, tree B: 8 ÷ (2 × (2+2)) = 1 — with each tree's evaluation animated step by step, ending with the conclusion: the ambiguity is a notation problem, not a math problem, and parentheses resolve it.
- Prompt seed: `claude "Argue both sides of the expression 8 ÷ 2(2 + 2). First: argue why the answer is 16 (left-to-right evaluation, multiplication and division equal precedence). Second: argue why the answer is 1 (implicit multiplication before explicit division, juxtaposition binds tighter). Third: explain what this reveals about mathematical notation conventions. Fourth: write an unambiguous version that means 16, and one that means 1. Do not give a final verdict until you have argued both sides."`
- Read / check: Verify Claude argues both sides before concluding. Confirm the unambiguous rewrites use parentheses correctly: (8÷2)×(2+2)=16 and 8÷(2×(2+2))=1. Check that the explanation connects to the broader lesson — notation is a convention, not a law of nature, and ambiguous notation is a design flaw.
- Human supplies: Nothing — the entire card runs on Claude's reasoning about the expression.
- Output medium: Manim (two animated parse trees evaluating side by side)
- The change: Ask Claude for three more examples of ambiguous mathematical notation conventions where the "standard" varies by country or era — showing that the ambiguity is cultural, not mathematical.
- Teardown angle: The disagreement about PEMDAS is not "one side is right" — it is a notation convention whose ambiguity reveals how much mathematical notation assumes a reader who already knows the rules.
- Exclusions: Full formal grammar of mathematical expressions, computer algebra system parsing rules, history of mathematical notation.
- Score: 8/10

## Candidate 03 — "Animate Polynomial End Behavior with Claude Code"
- Source: math-algebra/chapters/05-polynomial-and-rational-functions.md
- Lane: BUILD (Claude Code)
- Hook: A polynomial of degree n has at most n-1 turning points — and its long-run behavior is determined entirely by the leading term, regardless of what the lower-degree terms do. Watch the leading term take over as x grows.
- The artifact: An animated Manim sequence — four polynomials (degree 2, 3, 4, 5) each plotted on expanding x-ranges, with the lower-degree terms highlighted and then faded as the leading term dominates. A comparison panel showing the full polynomial vs. its leading term only, with the difference shrinking to invisibility as x → ∞.
- Prompt seed: `claude "Generate a Python/Manim animation showing polynomial end behavior. Four polynomials: f(x)=x^2 - 10x + 25, g(x)=x^3 - 5x^2 + 2x - 1, h(x)=x^4 - 3x^3 + x - 7, k(x)=-x^5 + 2x^3 - x + 10. For each: (1) plot from x=-5 to x=5, (2) plot from x=-20 to x=20, (3) overlay the leading term only (dashed), (4) animate the range expanding from 5 to 20, showing the full polynomial converging toward the leading-term shape. Use color to distinguish leading term from full polynomial."`
- Read / check: Verify the negative-leading-coefficient polynomial (k(x)) shows both ends going to -∞ (falls left and right). Confirm the overlay comparison is visually clear — the full polynomial and the leading term should visibly converge at larger x. Check that the animation's x-range expansion is smooth.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim (four-polynomial animated comparison with range expansion)
- The change: Add a fifth polynomial where the lower-degree terms dominate in the visible range — showing that "end behavior" is about x → ∞, not x = 5, and that the textbook window can be misleading.
- Teardown angle: End behavior is not about what the graph looks like — it is about what the leading term does when the lower terms become irrelevant. The animation makes "eventually" concrete.
- Exclusions: Complex roots, full polynomial long division, rational root theorem.
- Score: 8/10

## Candidate 04 — "Build the Rational Function Asymptote Detector with Claude: LLM Exercise 8.2"
- Source: math-algebra/chapters/08-periodic-functions.md (LLM Exercise 8.2) + chapters/05-polynomial-and-rational-functions.md
- Lane: BUILD (Claude Code)
- Hook: Tangent has vertical asymptotes at θ = π/2 + kπ. Sine and cosine never do. The difference is one character: tangent is sin/cos — a rational function — and the denominator hits zero. This is Chapter 5's rational-function asymptote, wearing trigonometry's clothes.
- The artifact: An animated Manim dual-panel sequence — Panel 1: tangent function on [-2π, 2π] with asymptotes animating in as vertical dashed lines exactly where cosine = 0. Panel 2: the unit circle, showing the radius becoming vertical (undefined slope) at the same angles — the geometry explaining the algebra.
- Prompt seed: `claude "Generate a Python/Manim animation of tan(x) = sin(x)/cos(x) showing why vertical asymptotes occur at x = π/2 + kπ. Panel 1: plot tan(x) from -2π to 2π, animate vertical asymptote lines appearing at x = ±π/2, ±3π/2. Label each with 'cos(x)=0 here.' Panel 2: unit circle, animate the radius sweeping from 0 to 2π, highlight when the x-coordinate (cosine) hits zero — match those angles to Panel 1's asymptotes. Add text: 'slope = sin/cos = undefined when cos=0.'"`
- Read / check: Verify asymptotes appear at exactly ±π/2 and ±3π/2 (not at π, 2π). Confirm Panel 2's unit circle radius is shown at the exact asymptote angles with x-coordinate = 0 highlighted. Check that the "undefined slope" annotation connects tangent-as-slope to tangent-as-sin/cos.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim (dual-panel animated sequence: function plot + unit circle)
- The change: Add a third panel — the function y = 1/cos(x) (secant) — showing that it has the same asymptotes as tangent for the same reason, connecting the two functions through their common denominator.
- Teardown angle: Asymptotes are not special properties of trigonometry — they are what happens to any ratio when its denominator hits zero. Tangent is rational functions wearing a different name.
- Exclusions: Full complex analysis of trigonometric functions, derivation of the addition formulas, inverse trig domain restrictions (covered in a separate LLM exercise).
- Score: 9/10

## Candidate 05 — "Animate the Birthday Problem with Claude: LLM Exercise 13.5"
- Source: math-algebra/chapters/13-sequences-probability-and-counting-theory.md (LLM Exercise 13.5)
- Lane: BUILD (Claude Code)
- Hook: In a room of 23 people, the probability of a shared birthday is ~50%. Most people guess you need 100+. The combinatorial growth dominates intuition — and the animation shows why.
- The artifact: An animated Manim visualization of the birthday problem — a room of dots growing from 2 to 50 people, with pairs highlighted and the probability of at least one shared birthday plotted on a growing curve beside it. C(n,2) annotated as the number of pairs, growing faster than the number of people. A vertical marker at n=23 (≈50%) and n=50 (≈97%).
- Prompt seed: `claude "Generate a Python/Manim animation of the birthday problem. Compute P(at least one shared birthday) for n=2 to 60 people using the complement: P = 1 - (365/365)(364/365)...(365-n+1)/365. Animation: (1) grow a population of dots from 2 to 60, (2) simultaneously plot the probability curve, (3) highlight n=23 (≈50%) and n=50 (≈97%) with vertical markers, (4) animate C(n,2) pairs counting as n grows, (5) add annotation: 'intuition tracks one person matching you — reality is all pairs matching each other.'"`
- Read / check: Verify P(23) ≈ 0.507 and P(50) ≈ 0.970 in the computation. Confirm C(n,2) is annotated growing faster than n. Check that the "intuition vs. reality" annotation appears — this is the pedagogical hook that the LLM exercise targets.
- Human supplies: Nothing — fully synthetic using the standard birthday problem formula.
- Output medium: Manim (animated dot population + probability curve with pair count annotation)
- The change: Add a second panel: "the birthday problem at n=365" — showing the probability approaches 1.0 asymptotically but never reaches it exactly, with the distinction between "certain" and "near-certain" animated.
- Teardown angle: Combinatorial growth always dominates our additive intuition — the birthday problem is the clearest single demonstration of why probabilistic reasoning requires computation, not gut feeling.
- Exclusions: Full inclusion-exclusion proof, generalizations to non-uniform birthday distributions, cryptographic birthday attack applications.
- Score: 9/10

## Candidate 06 — "Build the Exponential vs. Linear Growth Race with Claude"
- Source: math-algebra/chapters/06-exponential-and-logarithmic-functions.md
- Lane: BUILD (Claude Code)
- Hook: The exponential looks slower than the linear function at first. Then it passes. Then the linear function is invisible. The "passing point" is the lesson — and you can only see it if you animate it.
- The artifact: An animated Manim sequence — three stages: (1) x = 0 to 5: linear y=10x looks dominant over exponential y=2^x; (2) x = 0 to 10: the crossing point appears; (3) x = 0 to 20: the exponential makes the linear look flat. A small inset showing y-values at each stage with numbers growing dramatically.
- Prompt seed: `claude "Generate a Python/Manim animation comparing linear y=10x vs exponential y=2^x growth. Three stages: Stage 1 (x=0 to 5): linear dominates, exponential barely visible. Stage 2 (x=0 to 10): crossing point appears around x=4.7, animate a 'crossing' marker. Stage 3 (x=0 to 20): exponential towers over linear. At each stage transition, show the y-values side by side as the x-range expands. Use logarithmic y-axis option toggle to show both scales."`
- Read / check: Verify the crossing point is near x ≈ 4.7 (solve 10x = 2^x approximately). Confirm the y-axis scale makes the Stage 3 dominance visually dramatic. Check that the log-scale option shows the exponential as a straight line (making the growth rate constant visible).
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim (three-stage animated comparison with stage transitions)
- The change: Replace y=2^x with y=1.05^x (5% annual growth) and y=10x with $100/year savings — showing compound interest passing linear savings in a household finance context, making the abstraction concrete.
- Teardown angle: "Exponential growth" is used as a metaphor constantly and understood almost never — the crossing animation is the one visual that makes the concept physically real.
- Exclusions: Full derivation of e as the natural base, continuous compounding formula derivation, logarithm properties beyond the visual.
- Score: 9/10

## Candidate 07 — "Investigate the Geometric Series with Claude: LLM Exercise 13.1"
- Source: math-algebra/chapters/13-sequences-probability-and-counting-theory.md (LLM Exercise 13.1)
- Lane: BUILD (Claude Code)
- Hook: An infinite sum of positive numbers equals a finite number — and the condition is simple: each term is less than a fixed fraction of the previous. Watch the partial sums converge as the bars shrink.
- The artifact: An animated Manim bar chart — for the geometric series 1 + 1/2 + 1/4 + 1/8 + ... — each bar added one at a time with the partial sum annotating in, converging toward 2.0. A second panel: the harmonic series 1 + 1/2 + 1/3 + 1/4 + ... with bars growing more slowly but never stopping — the sum labeled "diverges (→ ∞)" as a contrasting counterexample.
- Prompt seed: `claude "Generate a Python/Manim animation comparing two infinite series. Panel 1 (converging): geometric series 1 + 1/2 + 1/4 + ... Add bars one by one (first 12 terms), show partial sums converging toward 2.0, annotate 'sum = 1/(1-0.5) = 2'. Panel 2 (diverging): harmonic series 1 + 1/2 + 1/3 + ... Show partial sums growing slowly but without bound. Mark the point where harmonic sum crosses 3.0. Annotation: 'terms decrease but not fast enough.' Show |r|<1 condition text appearing over Panel 1."`
- Read / check: Verify the geometric partial sums visibly approach (but never reach exactly) 2.0 within 12 terms. Confirm the harmonic series panel shows divergence — the sum crossing 3.0 should require many terms (around n=11), making the "slow divergence" concrete. Check that the |r|<1 condition annotation is prominent.
- Human supplies: Nothing — fully synthetic using standard series formulas.
- Output medium: Manim (two-panel animated bar chart with partial sum annotation)
- The change: Add a third series — geometric with r=1.01 (|r|>1) — showing immediate divergence as the bars grow instead of shrinking, completing the three-case picture.
- Teardown angle: The convergence condition is not a technicality — it is the difference between a sum that settles and one that escapes. Seeing the bars shrink vs. barely-shrink makes the condition intuitive.
- Exclusions: Formal proof of convergence tests, power series, Taylor series applications.
- Score: 8/10

## Candidate 08 — "Animate the Unit Circle with Claude: Building Sine and Cosine from Geometry"
- Source: math-algebra/chapters/07-the-unit-circle-sine-and-cosine-functions.md
- Lane: BUILD (Claude Code)
- Hook: Sine and cosine are not formulas — they are coordinates. The unit circle makes that literal: as the radius sweeps, the y-coordinate traces the sine wave and the x-coordinate traces the cosine. The animation makes the definition geometric, not algebraic.
- The artifact: An animated Manim dual-panel — left: unit circle with a radius sweeping counterclockwise, a moving dot on the circle, and dashed projections to the axes. Right: the x and y coordinate values plotting in real time as the radius sweeps — two sinusoidal curves growing from left to right, labeled "cos(θ)" and "sin(θ)." The sweep is synchronized so circle angle and curve position are visually identical.
- Prompt seed: `claude "Generate a Python/Manim animation of the unit circle definition of sine and cosine. Left panel: unit circle with rotating radius (sweep 0 to 2π over 8 seconds), a point on the circle, dashed vertical projection to x-axis (labeled cos(θ)) and horizontal projection to y-axis (labeled sin(θ)). Right panel: simultaneously plot cos(θ) and sin(θ) as functions of θ, growing in real time as the radius sweeps. Synchronize angle on left with x-position on right. Mark π/2, π, 3π/2, 2π on both panels."`
- Read / check: Verify the left panel projection lines are dashed and clearly labeled. Confirm the right panel curves grow exactly in sync with the left panel's sweep. Check that the four quarter-points (π/2, π, 3π/2, 2π) are marked on both panels simultaneously.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim (synchronized dual-panel animation: circle sweep + curve growth)
- The change: Add a slow-motion moment at θ=π/2 — pause the sweep, highlight sin(π/2)=1 and cos(π/2)=0, then resume. Repeat at θ=π — making the special angle values obvious from the geometry.
- Teardown angle: Trigonometry stops being a collection of formulas and becomes a geometric fact — the definitions are pictures, and the pictures are more memorable than the mnemonics.
- Exclusions: Full derivation of the Pythagorean identity from the unit circle (a separate video), radian vs. degree conversion beyond one labeling, inverse trig function construction.
- Score: 9/10
