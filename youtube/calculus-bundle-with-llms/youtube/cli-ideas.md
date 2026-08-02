# Calculus Bundle with LLMs — CLI Video Ideas ("X with Claude")

## Candidate 01 — Build the Logarithm Scale Compressor with Claude: Richter Numbers

- Source: calculus-bundle-with-llms/chapters/01-functions-and-graphs.md
- Lane: BUILD (Claude Code)
- Hook: Haiti 7.3, Chile 8.2, Japan 9. They look nearly equal. Japan released 350 times more energy than Haiti. The same string of digits hides a factor of 350 inside two digits — and you can't see it unless you understand what a logarithm actually does.
- The artifact: A Python script + Manim animation showing: (1) a number line with magnitude 7.3, 8.2, 9 — visually close; (2) the same values on an energy scale — exponentially separated; (3) the derivation: each unit of magnitude = ×10 in amplitude, ×10^1.5 ≈ 31.6 in energy, so Japan/Haiti = 10^(9-7.3)^1.5 ≈ 350×. The three numbers animate between the two scales.
- Prompt seed: `claude "Write a Python script using Manim that animates: (1) a linear number line showing Richter magnitudes 7.3, 8.2, 9 as nearly equal points; (2) the same values on a logarithmic energy scale showing they are exponentially separated; (3) text annotations showing the energy ratio formula: 10^((9-7.3)*1.5) ≈ 350. Warm monochrome palette, Georgia font, 1920×1080."`
- Read / check: Verify the energy formula: amplitude ratio = 10^(Δm), energy ratio = amplitude^1.5 = 10^(1.5×Δm). For Δm = 1.7: 10^(1.5×1.7) = 10^2.55 ≈ 354. Confirm the animation shows both scales simultaneously for the comparison to land. Output: the "linear" panel should show all three points clustered; the "energy" panel should show them separated by orders of magnitude.
- Human supplies: Nothing — fully synthetic. The three magnitudes and formula are hardcoded. For NEXT STEPS, viewer substitutes any two earthquake magnitudes.
- Output medium: Manim (two-panel animation, linear vs. log scale, number line transforms between them)
- The change: Add a fourth data point (the 1906 San Francisco earthquake, magnitude ~7.9) and show where it lands on both scales relative to Haiti and Japan — extending the compression demonstration.
- Teardown angle: The logarithm earns its name from the Greek "logos" (reason) and "arithmos" (number) — a reasoned number. It turns multiplication into addition, making enormous ranges legible. The compression is not approximation — it is exact mapping of exponential space to linear display.
- Exclusions: Skip the full derivation of logarithm rules, or natural log vs. log base 10 distinctions beyond the Richter context.
- Score: 9/10

---

## Candidate 02 — Visualize the Limit with Claude: Relativistic Mass Approaching c

- Source: calculus-bundle-with-llms/chapters/02-limits.md
- Lane: BUILD (Claude Code)
- Hook: What does the formula say at v = c exactly? The denominator becomes zero. Division by zero. No answer — not infinity as a number, not anything. The formula simply breaks. And yet the behavior is perfectly clear. That gap between "breaks at the point" and "approaches from the side" has a name: limit.
- The artifact: A Python + Manim animation of the relativistic mass function m = m₀/√(1−v²/c²) from v = 0 to v = 0.9999c. The curve sweeps in, stays nearly flat until ~0.7c, then bends sharply upward. The vertical asymptote at v = c is marked but clearly unreachable. Key points annotated: v = 0.5c → 1.15m₀, v = 0.9c → 2.29m₀, v = 0.999c → 22.4m₀.
- Prompt seed: `claude "Write a Python Manim script that plots relativistic mass m(v)/m₀ = 1/sqrt(1 - v²/c²) from v=0 to v=0.9999c. Show the asymptote at v=c as a dashed vertical line labeled 'v=c (unreachable)'. Animate the curve sweeping in from left. Annotate three key points: (0.5c, 1.15m₀), (0.9c, 2.29m₀), (0.999c, 22.4m₀). Add text: 'The limit exists. The value at v=c does not.' Warm monochrome."`
- Read / check: Verify the three annotated values: 1/√(1-0.25)=1/√0.75≈1.155; 1/√(1-0.81)=1/√0.19≈2.294; 1/√(1-0.998001)=1/√0.001999≈22.4. Confirm the asymptote is at x = 1 (normalized scale) not visually reaching it. Output: the curve should be visually nearly flat for the first 70% of the x-axis, then sharply upward in the last 30%.
- Human supplies: Nothing — fully synthetic. The function is analytic and requires no data.
- Output medium: Manim (curve sweeping in, asymptote appearing, annotations building, final text statement)
- The change: Add a second panel showing the three failure modes of limits side by side (jump discontinuity, blow-up/asymptote, oscillation) — using |x|/x, 1/x, and sin(1/x) as the three examples.
- Teardown angle: The limit concept resolves Berkeley's "ghosts of departed quantities." Newton and Leibniz used it intuitively for 150 years before Cauchy made it precise. The formal definition didn't change what calculus did — it explained why it worked.
- Exclusions: Skip the epsilon-delta formal definition in full, or the limit laws derivation.
- Score: 9/10

---

## Candidate 03 — Build the Derivative as Tangent Line with Claude: The Hennessey Venom GT

- Source: calculus-bundle-with-llms/chapters/03-derivatives.md
- Lane: BUILD (Claude Code)
- Hook: The camera operator tracking a rocket tilts the lens. At low altitude, the angular rate is fast — the camera sweeps across the low arc quickly. High up, the angle barely changes even though the rocket screams upward. That's not intuition. That's the inverse tangent differentiated.
- The artifact: A Python + Manim animation showing the secant line tilting toward the tangent line for f(x) = x² at x = 1, with h values shrinking from 1 to 0.5 to 0.25 to 0.1. The limit of the slope (2) is annotated. A second panel shows the rocket-camera angular rate dθ/dt vs. height h, revealing the counterintuitive decay.
- Prompt seed: `claude "Write a Python Manim script with two panels. Panel 1: plot f(x) = x² with a point at (1,1). Animate secant lines from (1,1) to (1+h, (1+h)²) for h = 1, 0.5, 0.25, 0.1 — each labeled with its slope. Then show the tangent line at slope 2. Panel 2: plot dθ/dt vs. rocket height h (in feet), with D=1000ft, dh/dt=100ft/s fixed, using dθ/dt = (1/D)/(1+(h/D)²) * dh/dt. Label the counterintuitive decay."`
- Read / check: Verify the angular rate formula: tan(θ) = h/D, differentiate: sec²(θ)·dθ/dt = (1/D)·dh/dt, so dθ/dt = (1/D·cos²(θ)) = (dh/dt/D)/(1+(h/D)²). At h=500, D=1000: dθ/dt = 100/1000/(1+0.25) = 0.08 rad/s ✓. Confirm the curve in panel 2 is decreasing (not increasing) as h grows. Output: the panel 2 curve should be highest at h=0 and decay toward zero as h→∞.
- Human supplies: Nothing — fully synthetic. The function is analytic.
- Output medium: Manim (secant-line animation panel, then angular-rate curve panel, building in sequence)
- The change: Differentiate f(x) = sin(x) using the limit definition (not the rule) — showing the limit mechanism producing cos(x), connecting the geometric animation to the algebraic derivation.
- Teardown angle: The chain rule is the derivative of composition. The rocket-camera problem uses it naturally — the angle is a function of height, height is a function of time, and the chain rule connects the two rates. The counterintuitive result (tracking gets easier as the rocket climbs) is what the math shows that intuition misses.
- Exclusions: Skip implicit differentiation, or higher-order derivatives in full.
- Score: 9/10

---

## Candidate 04 — Build the Linear Approximation Calculator with Claude

- Source: calculus-bundle-with-llms/chapters/04-applications-of-derivatives.md
- Lane: BUILD (Claude Code)
- Hook: √4.1 ≈ 2.025. Computed in your head. From one multiplication. The tangent line is the best linear approximation — and "best" is not an aesthetic claim, it is a theorem. The further you go from the anchor, the worse it gets, and that decay rate is also computable.
- The artifact: A Python script + Manim animation for linear approximation. Given a function f(x) = √x, anchor at a = 4: shows the tangent line L(x) = 2 + (1/4)(x−4), animates the gap between L(x) and f(x) as x moves away from 4, and marks the error at x = 4.1 (error = 0.0002) and x = 5 (error ≈ 0.014). The error grows visibly.
- Prompt seed: `claude "Write a Python Manim script: plot f(x) = sqrt(x) (solid curve) and its tangent line L(x) = 2 + 0.25*(x-4) at anchor a=4 (dashed). Animate x moving from 4.1 to 5, with two labeled gaps: at x=4.1 showing L(4.1)=2.025 vs sqrt(4.1)=2.0248, error=0.0002; at x=5 showing L(5)=2.25 vs sqrt(5)=2.236, error=0.014. Title: 'Linear approximation: perfect at the anchor, progressively wrong elsewhere.'"`
- Read / check: Verify √4.1 ≈ 2.02485 (error = |2.025 - 2.02485| ≈ 0.00015). Verify √5 ≈ 2.2360 (error = |2.25 - 2.2360| ≈ 0.014). Confirm the dashed tangent line extends both left and right of the anchor. Output: the error annotation gap should be visually tiny at x=4.1 and clearly visible at x=5.
- Human supplies: Nothing — fully synthetic. The function and anchor are hardcoded.
- Output medium: Manim (curve and tangent line rendered, x sliding right, error gap growing, annotations updating)
- The change: Ask Claude to add the quadratic approximation (second-order Taylor term) and show it stays accurate further from the anchor — introducing Taylor series as the generalization.
- Teardown angle: The linear approximation is exact at one point and progressively wrong everywhere else. That "progressive wrongness" is not a flaw — it is the price of linearity. The Taylor series pays that price less steeply at each order.
- Exclusions: Skip L'Hôpital's rule, or Newton's method for root-finding.
- Score: 8/10

---

## Candidate 05 — Build the Riemann Sum Convergence Animation with Claude

- Source: calculus-bundle-with-llms/chapters/05-integration.md
- Lane: BUILD (Claude Code)
- Hook: Four rectangles give you 30. The exact answer is 64/3 ≈ 21.33. With 20 rectangles, you're much closer. With 1000, you're there. The integral is not a formula — it is the limit of this process, and watching it converge is the whole lesson.
- The artifact: A Python + Manim animation of right-endpoint Riemann sums for ∫₀⁴ x² dx with n = 4, 10, 20, 100. Each frame shows the rectangles, the sum value, and the error from the exact answer 64/3. The rectangles shrink and multiply. The sum value converges to 21.33.
- Prompt seed: `claude "Write a Python Manim script: animate right-endpoint Riemann sums for f(x)=x² on [0,4] for n=4, 10, 20, 100 rectangles in sequence. Each frame: draw the n rectangles above the curve in muted red, label them with their total sum (e.g., S_4=30.0, S_10=24.2, S_20=22.9, S_100=21.55), and show the error from 64/3≈21.33 shrinking. Final frame: show the limit integral symbol ∫₀⁴ x²dx = 64/3."`
- Read / check: Verify the right-endpoint sums: S_4 = Σ(i=1 to 4) f(i)·1 = 1+4+9+16 = 30. S_∞ = 64/3 ≈ 21.33. For n=10: S_10 = (1/10)·Σf(k/10·4 + 0) ... actually Σ(i=1 to 10)(4i/10)²·(4/10). Confirm the error sequence is decreasing monotonically. Output: rectangle count labels should be visible and the sum value should visibly decrease toward 21.33.
- Human supplies: Nothing — fully synthetic. The function and interval are hardcoded.
- Output medium: Manim (rectangles morphing, counter showing n and sum value, error bar shrinking)
- The change: Show the left-endpoint sum for n=4 (S_4 = 0+1+4+9 = 14, underestimate) alongside the right-endpoint sum (overestimate 30), with the exact answer 21.33 between them — demonstrating both bounds converge.
- Teardown angle: The integral is the limit of sums — the elongated S is literally "sum." The Fundamental Theorem is not obvious, it is surprising: the local (derivative) and the global (integral) are inverse operations. Watching the sums converge makes the global nature of the integral visible before the theorem is stated.
- Exclusions: Skip improper integrals, or the formal measure-theoretic definition of the Lebesgue integral.
- Score: 9/10

---

## Candidate 06 — Build the Fundamental Theorem Proof Animation with Claude

- Source: calculus-bundle-with-llms/chapters/05-integration.md
- Lane: BUILD (Claude Code)
- Hook: Differentiation is local — an instantaneous slope. Integration is global — an accumulated area. They shouldn't have anything to do with each other. And yet: the Fundamental Theorem says differentiating the accumulation recovers what was being accumulated. That's the most surprising theorem in calculus.
- The artifact: A Python + Manim animation of FTC Part 1 proof: a positive curve f(t), the shaded accumulation F(x) = ∫ₐˣ f(t)dt, a thin additional strip from x to x+h (height ≈ f(x), width h), and the equation F(x+h)−F(x) ≈ f(x)·h. Divide by h, take limit: F'(x) = f(x). Three frames: general, then specific with f(t) = t².
- Prompt seed: `claude "Write a Python Manim script: Plot a positive curve f(t) on [0,4]. Show the shaded region F(x) = integral from 0 to x in blue. Animate a thin red strip from x to x+h, labeled 'F(x+h)-F(x) ≈ f(x)·h'. Show the algebra: divide by h → (F(x+h)-F(x))/h → limit → F'(x)=f(x). Use f(t)=t² as the specific example, anchor at x=2. Title: 'The running total's instantaneous rate of change is what's being accumulated.'"`
- Read / check: Verify that at x=2, f(2) = 4 and the thin strip at h=0.2 has area ≈ 4×0.2 = 0.8. Confirm the strip is drawn at a specific x position (not abstractly). Output: the strip should be visually thin and its height should clearly correspond to the curve height at x.
- Human supplies: Nothing — fully synthetic. The proof is analytic.
- Output medium: Manim (three-beat animation: accumulation shaded, strip added, algebra building, final equation highlighted)
- The change: Apply FTC Part 2 immediately after: show ∫₀⁴ x² dx = F(4)−F(0) = 64/3 − 0 = 64/3, connecting the proof to the computation from Candidate 05.
- Teardown angle: The Fundamental Theorem is not just a computational shortcut — it is the reason calculus is possible at scale. Without it, every definite integral would require Riemann sum arithmetic. With it, integration reduces to finding antiderivatives. That change is the whole subject.
- Exclusions: Skip measure theory, or the pathological case (non-Riemann-integrable functions).
- Score: 9/10

---

## Candidate 07 — Build the Related Rates Solver with Claude: Ladder and Rocket Camera

- Source: calculus-bundle-with-llms/chapters/04-applications-of-derivatives.md
- Lane: BUILD (Claude Code)
- Hook: Two quantities, both depending on time. Linked by one equation. Differentiate the equation — and suddenly you have a relationship between the rates. The camera operator isn't just tilting. They're solving a calculus problem with their wrists, in real time.
- The artifact: A Python + Manim animation of two related rates problems side by side: (1) the sliding ladder (13ft, bottom sliding at 2ft/s, top falling at 5/6 ft/s when bottom is 5ft from wall) and (2) the rocket camera (angular rate dθ/dt = 0.08 rad/s when h=500ft). Both show the geometric diagram, the differentiated equation, and the numerical answer.
- Prompt seed: `claude "Write a Python Manim script with two panels. Panel 1: ladder geometry (13ft ladder, x=distance from wall, y=height). Show x²+y²=169, differentiate to 2x(dx/dt)+2y(dy/dt)=0. Substitute x=5, y=12, dx/dt=2 → dy/dt=-5/6. Panel 2: rocket at height h=500ft, camera at D=1000ft. Show tan(θ)=h/D, differentiate, substitute dh/dt=100 → dθ/dt=0.08 rad/s. Warm monochrome."`
- Read / check: Verify: ladder problem: 2(5)(2)+2(12)(dy/dt)=0 → dy/dt=-5/6 ✓. Rocket: sec²(θ)·dθ/dt=(1/D)·dh/dt. At h=500, tan(θ)=0.5, sec²(θ)=1.25, dθ/dt=100/(1000×1.25)=0.08 ✓. Output: both numerical answers should appear clearly labeled with units.
- Human supplies: Nothing — fully synthetic. Both problems are textbook standard.
- Output medium: Manim (two-panel, each building geometry then differentiation then substitution then answer)
- The change: Add the optimization beat: ask Claude for the height that maximizes the angular rate dθ/dt for the rocket-camera problem (it's h=0, i.e., at launch — the rate is always decreasing, which connects to the optimization chapter).
- Teardown angle: Related rates problems look like geometry problems until you differentiate. Then they're about rates and the relationships between them. The picture isn't the problem — it's the key to writing the equation that can be differentiated.
- Exclusions: Skip the conical water tank problem, or 3D related rates variants.
- Score: 8/10

---

## Candidate 08 — Build the Volume of Revolution with Claude: Disk Method Wine Bottle

- Source: calculus-bundle-with-llms/chapters/06-applications-of-integration.md
- Lane: BUILD (Claude Code)
- Hook: A wine bottle is not a cylinder. It has a flared base, a curved shoulder, a tapering neck. You cannot compute its volume with πr²h. But you can if you know a profile curve r(y) — and you can compute the volume with a single definite integral.
- The artifact: A Python + Manim animation of the disk method: a wine bottle profile curve r(y) shown, a horizontal disk at height y pulled out with radius r(y) and thickness dy labeled, then the stack of disks filling the bottle, and the integral V = ∫ₐᵇ π[r(y)]² dy evaluated numerically. The disk animates its contribution to the growing sum.
- Prompt seed: `claude "Write a Python Manim script: (1) plot a wine bottle profile curve r(y) (use r(y) = 1.5 + sin(y/2) for y from 0 to 6 as an approximation). (2) Show one thin horizontal disk at y=3 with radius r(3) and thickness dy, pulled out from the bottle. (3) Show the disk method integral V=∫₀⁶ π[r(y)]² dy. (4) Animate the full stack of disks filling the bottle, showing the running sum. Use warm monochrome, label all dimensions."`
- Read / check: Verify the integral V = ∫₀⁶ π(1.5+sin(y/2))² dy is numerically computable (approximately π∫₀⁶(2.25 + 3sin(y/2) + sin²(y/2)) dy). Confirm the bottle profile looks bottle-shaped — wider at base, narrower at neck. Output: the stack of disks should fill a recognizable bottle silhouette.
- Human supplies: Nothing — fully synthetic. The profile curve is an analytic approximation.
- Output medium: Manim (profile shown, disk extracted, disks stacking, integral evaluating, final volume number)
- The change: Add the shell method panel for the same profile (rotated around the y-axis) — showing both methods give the same volume and discussing when each is easier to set up.
- Teardown angle: Every application in Chapter 6 uses the same pattern: slice into infinitesimal pieces, identify each piece's contribution, integrate. The wine bottle is not a special formula — it is the general pattern applied to a curved profile. Learning the pattern, not the formula, is what the chapter is for.
- Exclusions: Skip arc length (a less visual application), or surface area of revolution.
- Score: 8/10

---

## Candidate 09 — Build the Optimization Critical Point Finder with Claude

- Source: calculus-bundle-with-llms/chapters/04-applications-of-derivatives.md
- Lane: BUILD (Claude Code)
- Hook: A function reaches a maximum or minimum only at critical points — where the derivative is zero or undefined. But not every critical point is a maximum or minimum. The second derivative test separates them. Build it once with Claude and you can apply it to any function.
- The artifact: A Python CLI script + Manim animation that takes a polynomial function from the user, finds all critical points (symbolic differentiation via SymPy), applies the first and second derivative tests, and animates the function with critical points marked as local max (red), local min (green), or saddle (yellow).
- Prompt seed: `claude "Write a Python script using SymPy and Manim. Input: a polynomial f(x) as a string (e.g., 'x**4 - 8*x**2 + 3'). Steps: (1) compute f'(x) symbolically, (2) solve f'(x)=0 for critical points, (3) compute f''(x) at each critical point to classify (>0: local min, <0: local max, =0: inconclusive), (4) Manim: plot f(x), mark each critical point with colored dot and label. Output: table of critical points with x, f(x), f''(x), classification."`
- Read / check: Verify for f(x) = x⁴ − 8x² + 3: f'(x) = 4x³ − 16x = 4x(x²−4) = 0 → x = 0, ±2. f''(x) = 12x² − 16: f''(0) = −16 (local max), f''(±2) = 48−16 = 32 (local min). Confirm the Manim plot correctly positions the three colored dots. Output: x=0 should be red (local max), x=±2 should be green (local min).
- Human supplies: Nothing — fully synthetic. The polynomial is typed into the terminal. For NEXT STEPS, viewer substitutes their own function.
- Output medium: screen-recording mp4 + Manim (terminal: polynomial in, critical point table out; then Manim animation of function with colored critical points)
- The change: Ask Claude to extend the script to find the global max/min on a closed interval [a, b] — adding the endpoint evaluation step and the Extreme Value Theorem check.
- Teardown angle: Critical points are necessary but not sufficient for extrema. The second derivative test is a local criterion — it tells you the concavity at the point, not whether the point is the highest or lowest on the whole domain. The distinction matters for any optimization problem with constraints.
- Exclusions: Skip Lagrange multipliers for constrained optimization, or multivariable optimization.
- Score: 9/10

---

## Candidate 10 — Build the Chain Rule Decomposer with Claude

- Source: calculus-bundle-with-llms/chapters/03-derivatives.md
- Lane: BUILD (Claude Code)
- Hook: f(g(x)) — the outer function applied to the inner function. The chain rule says: differentiate the outside (leaving the inside alone), multiply by the derivative of the inside. It sounds like a recipe. It is also the reason sin(x²) and sin²(x) have completely different derivatives.
- The artifact: A Python + Manim animation showing the chain rule as a composition pipeline. Two examples: (1) f(x) = sin(x²) — outer = sin, inner = x², derivative = cos(x²)·2x; (2) f(x) = (x³+1)⁵ — outer = u⁵, inner = x³+1, derivative = 5(x³+1)⁴·3x². Each example shows the composition diagram, identifies the layers, and builds the derivative term by term.
- Prompt seed: `claude "Write a Python Manim script: show the chain rule as a two-box pipeline diagram. Box 1: inner function g(x). Box 2: outer function f(u). Arrow from x → g(x) labeled g'(x), arrow from g(x) → f(g(x)) labeled f'(g(x)). Show the product rule: d/dx[f(g(x))] = f'(g(x))·g'(x). Then animate two examples: (1) sin(x²) → cos(x²)·2x; (2) (x³+1)⁵ → 5(x³+1)⁴·3x². Build each derivative term by term with color-coded outer/inner contributions."`
- Read / check: Verify the two derivatives: d/dx[sin(x²)] = cos(x²)·2x ✓. d/dx[(x³+1)⁵] = 5(x³+1)⁴·3x² ✓. Confirm the pipeline diagram has two distinct boxes (not one monolithic function). Output: the "outer contribution" and "inner contribution" should be color-coded distinctly.
- Human supplies: Nothing — fully synthetic. Both examples are analytic.
- Output medium: Manim (pipeline diagram building, then two example animations, each showing the outer/inner separation)
- The change: Show how implicit differentiation uses the chain rule: differentiate y² (treating y as a function of x) → 2y·(dy/dx). The chain rule appears when the variable inside is not x.
- Teardown angle: The chain rule is the rule for composition. Every composed function — sin(x²), e^(x³), ln(cos(x)) — requires it. The common error is treating it as "multiply by the inner function's derivative" without understanding why: the inner function is changing, and its rate of change modifies the outer function's rate of change.
- Exclusions: Skip logarithmic differentiation, or the derivation of the chain rule from the limit definition.
- Score: 8/10

---

## Candidate 11 — Build the Exponential Growth Simulator with Claude

- Source: calculus-bundle-with-llms/chapters/01-functions-and-graphs.md + chapters/03-derivatives.md
- Lane: BUILD (Claude Code)
- Hook: The exponential eventually outgrows every polynomial. Not just faster — eventually, against any polynomial of any degree, the exponential wins. Build a simulation that shows when it happens for 2ˣ vs. x², x⁵, and x¹⁰.
- The artifact: A Python + Manim animation plotting 2ˣ, x², x⁵, and x¹⁰ on the same axes from x=0 to x=100. The three polynomial curves start higher than 2ˣ and are eventually overtaken. The crossover points are marked with vertical lines and labeled. A final text annotation: "2ˣ eventually always wins — regardless of the polynomial's degree."
- Prompt seed: `claude "Write a Python Manim script: plot 2^x, x^2, x^5, x^10 on the same axes from x=0 to x=100. Use log scale on the y-axis to show all curves simultaneously. Mark the crossover points where 2^x first exceeds each polynomial. Animate the curves sweeping in from left. Add a text annotation: '2^x eventually always wins.' Warm monochrome, each curve labeled."`
- Read / check: Verify approximate crossovers: 2^x > x^2 at x≈8.7; 2^x > x^5 at x≈22; 2^x > x^10 at x≈58. Confirm the log-scale y-axis makes all four curves legible simultaneously. Output: all three crossover points should be visible and marked on the same plot.
- Human supplies: Nothing — fully synthetic. All four functions are analytic.
- Output medium: Manim (curves sweeping in, crossover points appearing, annotation building)
- The change: Ask Claude to find the crossover analytically using Newton's method (solve 2^x = x^n numerically) — connecting the simulation result to a computation.
- Teardown angle: "Exponential growth" is not a metaphor for fast growth — it is a specific mathematical statement about the function's rate of change being proportional to its current value. That property is what makes it overtake every polynomial, because polynomials grow at fixed-power rates while exponentials grow at self-referential rates.
- Exclusions: Skip the derivation that e is the natural base for exponential differentiation, or complex exponents.
- Score: 8/10

---

## Candidate 12 — Build the Area Between Curves Calculator with Claude

- Source: calculus-bundle-with-llms/chapters/06-applications-of-integration.md
- Lane: BUILD (Claude Code)
- Hook: Enclosed by y = x² and y = x + 2. Where do they meet? Which is on top? How much area is inside? Three questions, each answerable from the same integral — but only if you set it up right. Get the order of subtraction wrong and you compute the negative of the answer.
- The artifact: A Python CLI script + Manim animation: given two function strings as input, finds the intersection points (via SymPy), identifies which function is on top on the interval, sets up ∫ₐᵇ [f(x)−g(x)]dx, evaluates it symbolically, and animates the enclosed region being shaded with the area labeled.
- Prompt seed: `claude "Write a Python script using SymPy and Manim. Input: two function strings f and g. (1) Find intersection points by solving f(x)=g(x). (2) Check which is greater on the interval. (3) Compute area = integral(f-g, a, b) symbolically. (4) Manim: plot both curves, shade the enclosed region, label the area. Demo case: f='x+2', g='x**2'. Expected: intersections at x=-1 and x=2, area=9/2."`
- Read / check: Verify: x+2=x² → x²-x-2=0 → (x-2)(x+1)=0 → x=-1,2. Area = ∫₋₁²[(x+2)-x²]dx = [x²/2+2x-x³/3]₋₁² = (2+4-8/3)-(1/2-2+1/3) = 10/3+7/6 = 9/2 ✓. Confirm the shading is between the two curves, not below both. Output: the area label should read "9/2" or "4.5".
- Human supplies: Nothing — fully synthetic. The viewer substitutes their own function pair for the CHANGE beat.
- Output medium: screen-recording mp4 + Manim (terminal: two functions in, intersection points and area out; then Manim shading the region)
- The change: Show the subtlety: if the curves cross within the interval, the integral requires splitting. Demonstrate with f(x) = sin(x) and g(x) = x/π on [0, 2π] — two crossings, three sub-intervals, each with different sign.
- Teardown angle: The area formula ∫[f−g]dx requires knowing which function is on top. When the curves cross, the integral can compute a net area that cancels positive and negative contributions. The fix is absolute value — ∫|f−g|dx — but that requires splitting at each crossing.
- Exclusions: Skip polar area formulas, or arc length applications.
- Score: 8/10

---

## Candidate 13 — Build the Continuity vs. Differentiability Checker with Claude

- Source: calculus-bundle-with-llms/chapters/03-derivatives.md
- Lane: BUILD (Claude Code)
- Hook: Continuous functions can fail to be differentiable. Differentiable functions are always continuous. The implication is one-way. |x| is continuous everywhere and differentiable nowhere at x=0. That's not a failure of the function — it's the difference between two levels of smoothness.
- The artifact: A Python CLI script + Manim animation: given a function string, (1) checks continuity at a specified point (left/right limits equal, function defined), (2) checks differentiability (left/right derivative limits equal), (3) classifies the failure mode if non-differentiable (jump discontinuity / corner / vertical tangent). Demo cases: |x| at x=0 (corner), step function (jump discontinuity), x^(1/3) (vertical tangent).
- Prompt seed: `claude "Write a Python script using SymPy and Manim that checks continuity and differentiability for three functions at x=0: (1) |x| (corner), (2) floor(x) step function (jump), (3) x^(1/3) (vertical tangent). For each: compute left and right limits, check continuity, compute left and right derivatives, classify failure. Manim: three-panel animation, each showing the function graph with the failure mode annotated."`
- Read / check: Verify for |x| at x=0: left derivative = -1, right derivative = +1, disagreement → corner. For x^(1/3): derivative = (1/3)x^(-2/3) → ∞ as x→0 → vertical tangent. For step function: left limit ≠ right limit at 0 → not even continuous. Output: three-panel animation should clearly show all three failure types with distinct geometric appearances.
- Human supplies: Nothing — fully synthetic. All three demo functions are analytic.
- Output medium: Manim (three-panel, each showing failure mode, left/right limit arrows, derivative slope indicators)
- The change: Ask Claude to check Weierstrass function (continuous everywhere, differentiable nowhere) — showing that the corner is not the extreme case: a function can be continuous everywhere and differentiable literally nowhere.
- Teardown angle: Differentiability is a stronger condition than continuity. Most functions you encounter in applications are differentiable almost everywhere. The failure modes are real but localized — corners, cusps, vertical tangents. When they appear, the derivative is simply not defined, and that's the correct answer.
- Exclusions: Skip Lipschitz continuity, or absolute continuity (measure theory).
- Score: 8/10
