# Calculus — CLI Video Ideas ("X with Claude")

## Candidate 01 — Build a Relativistic Mass Visualizer with Claude

- Source: math-calculus/chapters/02-limits.md
- Lane: BUILD (Claude Code)
- Hook: The formula for relativistic mass blows up at v = c — but the blow-up isn't chaos, it's a perfectly defined one-sided limit. Watching it animate makes the "barrier" visible in a way algebra cannot.
- The artifact: a Manim animation of m(v)/m₀ vs. v/c that sweeps v from 0 to 0.9999c, shows the curve climbing steeply, marks key γ values (2×, 7×, 22×) with callouts, and annotates the asymptote at v = c. Output is an mp4.
- Prompt seed: `claude "Write a Python script using matplotlib to plot relativistic mass ratio m/m0 = 1/sqrt(1 - v^2/c^2) as v/c goes from 0 to 0.9999. Animate the curve drawing from left to right. Mark with vertical lines where the mass doubles, triples, and reaches 7x. Label each marker. Save as mp4."`
- Read / check: Verify the formula uses correct relativistic mass; confirm γ values at 0.5c ≈ 1.15, 0.9c ≈ 2.29, 0.99c ≈ 7.09, 0.999c ≈ 22.4. Check the animation runs end-to-end without divide-by-zero. Confirm the asymptote annotation is visually clear and the curve's rapid growth is visible at scale.
- Human supplies: Nothing — fully synthetic. The formula is analytic; no real physics data needed. A synthetic illustration is authentic for this concept.
- Output medium: Manim (animated curve sweep with callout markers)
- The change: Add a second overlaid curve showing Newtonian kinetic energy for comparison — letting viewers see where the relativistic and classical predictions diverge significantly.
- Teardown angle: The limit exists (and can be computed as ∞) even where the function is undefined — the limit concept is about approach, not arrival. This is the cleanest single example of why "approaching" and "equaling" are different.
- Exclusions: Full derivation of special relativity; the exact Michelson-Morley experiment; energy equivalence E=mc².
- Score: 9/10

---

## Candidate 02 — Animate Newton's Method Converging with Claude

- Source: math-calculus/chapters/04-applications-of-derivatives.md
- Lane: BUILD (Claude Code)
- Hook: Newton's method roughly doubles correct decimal places every iteration — starting from a guess of 1.0, it finds √2 to 10 decimal places in 5 steps. Watching the tangent lines converge on screen is more memorable than reading the numbers.
- The artifact: a Manim animation showing f(x) = x²−2 plotted, with each Newton iteration drawn as a tangent line whose x-intercept becomes the next guess. Each step labeled with the current x value and error. Quadratic convergence shown via a "correct digits" counter in corner.
- Prompt seed: `claude "Animate Newton's method for f(x) = x^2 - 2 using Manim. Start at x0=1.0. Show 5 iterations. For each iteration: draw the tangent line at the current point, mark where it crosses the x-axis, display the x value and abs error to 10 decimal places. Include a counter showing digits of precision. Render to mp4."`
- Read / check: Verify each x_n matches the formula x_{n+1} = x_n - f(x_n)/f'(x_n). Check convergence rate is quadratic (digits double). Confirm the tangent line visually connects the current point to the x-axis crossing. Check the error counter accurately reflects abs(x_n - sqrt(2)).
- Human supplies: Nothing — fully synthetic. The function and iteration are deterministic; no real data required.
- Output medium: Manim (iterative tangent-line animation with error counter)
- The change: Switch to f(x) = cos(x) − x to find the fixed point, showing how the same method works for transcendental equations where factoring fails.
- Teardown angle: Quadratic convergence is the design judgment — Newton's method is fast not because the algorithm is clever but because linear approximation near a root is extremely accurate. Understanding why it fails (near horizontal tangents, cyclic orbits) is the real lesson.
- Exclusions: Numerical stability analysis; complex Newton fractals; Newton's method in higher dimensions.
- Score: 9/10

---

## Candidate 03 — Plot a Venom GT's Velocity, Acceleration, and Jerk with Claude

- Source: math-calculus/chapters/03-derivatives.md
- Lane: BUILD (Claude Code)
- Hook: Position is where you are. Velocity is what the speedometer reads. Acceleration is what pins you to the seat. Jerk is what you feel when that force changes. All four are the same function differentiated, and you can watch them on one plot from a real car's 0-to-200 data.
- The artifact: a Manim or d3 animated time-series showing v(t), a(t), and j(t) for the Venom GT model (v_max=270.49 mph, τ≈10.79 s) from t=0 to t=30s. Each curve revealed in sequence with narration callouts. The animation pauses to highlight launch moment (max acceleration) and the fade to zero (jerk diminishes).
- Prompt seed: `claude "Write a Python script to compute and plot v(t), a(t), j(t) for v(t) = 270.49*(1 - exp(-t/10.79)) mph over t=0 to 30 seconds. Plot all three on subplots with labeled axes (mph, mph/s, mph/s^2). Mark t=14.51s (when v=200 mph). Mark the max acceleration at t=0. Save as png then animate with matplotlib animation."`
- Read / check: Verify a(0) = v_max/τ ≈ 25.1 mph/s ≈ 1.14g. Verify v(14.51) ≈ 200 mph given τ=10.79. Check j(t) is negative everywhere (deceleration of acceleration). Confirm unit labels are correct. Verify the animation reads smoothly.
- Human supplies: Nothing — fully synthetic. The model is a standard automotive approximation, explicitly noted as qualitative in the chapter. Synthetic is appropriate here.
- Output medium: Manim or screen-recording mp4 (animated multi-panel time series)
- The change: Add a fourth panel showing the snap (4th derivative) — the rate of change of jerk — and discuss at what order human physiological sensation saturates.
- Teardown angle: The hierarchy of derivatives encodes different textures of experience — you feel acceleration as a constant push, jerk as a lurch. Engineers design roller coasters by constraining jerk, not just acceleration. The mathematical object and the physical sensation are the same thing.
- Exclusions: Exact Venom GT manufacturer specifications; full drag model with aerodynamics; transmission shift dynamics.
- Score: 8/10

---

## Candidate 04 — Visualize the Fundamental Theorem: Riemann Sums to Exact Area with Claude

- Source: math-calculus/chapters/05-integration.md
- Lane: BUILD (Claude Code)
- Hook: With 4 rectangles, ∫₀⁴ x² dx gives 30 — wrong by 30%. Watch 4 grow to 400 rectangles and watch the estimate converge to 64/3. The FTC makes this instant. The video lets you watch both routes arrive at the same answer.
- The artifact: a Manim animation showing ∫₀⁴ x² dx in two panels: left panel shows animated Riemann sum rectangles being added (n=4, 8, 16, 32, 64 … 400), with a running estimate and error displayed; right panel shows the antiderivative approach (x³/3 evaluated at endpoints). Both panels highlight the moment they converge to 64/3.
- Prompt seed: `claude "Create a Manim animation for the integral of x^2 from 0 to 4 using right-endpoint Riemann sums. Left panel: animate adding rectangles for n=4,8,16,32,64,128,400. Show the running sum and percent error from exact value 64/3. Right panel: show the antiderivative x^3/3 evaluated from 0 to 4, giving the exact answer. Both panels side-by-side, exact value shown as a red line."`
- Read / check: Verify right-endpoint sum formula for n rectangles gives Σᵢ(i/n)²·(4/n)·4 → 64/3. Check the error percentage at each n step. Confirm both panels display the same final value. Verify the animation timing is clear.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim (dual-panel animated comparison)
- The change: Add a third panel showing the Gaussian e^{-x²} — for which no elementary antiderivative exists — and demonstrate numerical integration approximating √π.
- Teardown angle: The FTC is a trade: you get instant exact answers for anything with a known antiderivative, and numerical methods for everything else. Neither is universally superior — the choice depends on whether a closed form exists.
- Exclusions: Full proof of FTC from epsilon-delta; historical priority dispute Newton vs. Leibniz; substitution method.
- Score: 8/10

---

## Candidate 05 — Build a Wine Bottle Volume Calculator with Claude

- Source: math-calculus/chapters/06-applications-of-integration.md
- Lane: BUILD (Claude Code)
- Hook: A wine bottle is not a cylinder. Its volume requires an integral over a profile function r(y). Build the calculator in ~30 lines and watch it compute for the three-section model — then compare to the 750 mL standard.
- The artifact: a Python script that takes a piecewise profile r(y) (body: r=4 cm, 0-20 cm; shoulder: linear taper 4→1.5 cm, 20-25 cm; neck: r=1.5 cm, 25-30 cm), computes ∫π·r(y)²·dy by section, sums to total volume in mL, and renders an animated cross-section bar chart showing each section's contribution vs. the 750 mL standard. Output: animated bar chart mp4.
- Prompt seed: `claude "Write a Python script that computes the interior volume of a wine bottle modeled as three sections: body (y=0-20cm, r=4cm), shoulder (y=20-25cm, r linear from 4 to 1.5cm), neck (y=25-30cm, r=1.5cm). Use scipy.integrate.quad to compute pi*r(y)^2 for each section. Print volumes in mL and total. Then create an animated bar chart with matplotlib showing each section's volume building up, with a 750mL reference line."`
- Read / check: Verify body ≈ 1005 cm³, shoulder ≈ 127 cm³, neck ≈ 35 cm³, total ≈ 1167 mL. Confirm scipy.integrate.quad is called correctly. Check units (cm³ = mL). Verify the 750 mL reference line renders correctly.
- Human supplies: Nothing — fully synthetic. The profile is a pedagogical model, explicitly so in the chapter. Synthetic is authentic.
- Output medium: Manim or screen-recording mp4 (animated stacked bar chart with reference line)
- The change: Let the user provide a custom r(y) profile (e.g., from a real bottle's measurements) and recompute — showing how the slice-identify-integrate pattern generalizes to any shape.
- Teardown angle: The same integral pattern — slice, identify, integrate — computes volume for any shape describable by a profile function. The real-world payoff is that numerical integration handles actual bottle profiles that have no closed-form antiderivative.
- Exclusions: Arc length computation; shell vs. disk comparison; pumping-water-out calculation.
- Score: 7/10

---

## Candidate 06 — Squeeze Theorem: Bounding sin(1/x) with Claude

- Source: math-calculus/chapters/02-limits.md
- Lane: BUILD (Claude Code)
- Hook: sin(1/x) near x=0 oscillates infinitely and has no limit — but x²·sin(1/x) is pinned to zero by x² from above and below. Watch the "squeeze" in action frame by frame.
- The artifact: a Manim animation plotting three curves: y = x², y = -x², and y = x²·sin(1/x) from x = -0.3 to 0.3. The outer two curves appear first as "walls", then the oscillating middle curve fills in, visibly trapped between them. Final frame zooms to x → 0 showing all three converging to 0.
- Prompt seed: `claude "Create a Manim animation showing the squeeze theorem for x^2*sin(1/x). Plot three curves: y=x^2 (top bound), y=-x^2 (bottom bound), y=x^2*sin(1/x) (middle). Color: top=blue, bottom=blue, middle=orange. Animate from x=0.3 down to x=0.001. Show the middle function oscillating but staying between the bounds. Title: 'The Squeeze Theorem'."`
- Read / check: Verify x²·sin(1/x) stays within [-x², x²] for all x≠0. Check the animation doesn't break at x values too close to 0 (numerical precision). Confirm three curves are visually distinct. Check the zooming behavior communicates the convergence.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim (animated curve with squeeze bounds)
- The change: Show the failure case: sin(1/x) without the x² factor — demonstrating the oscillation has no limit — contrasting it with the bounded version.
- Teardown angle: The squeeze theorem's elegance is that it never looks at the complicated function directly — you only need bounds. This is the template for all bounding arguments in analysis.
- Exclusions: ε-δ proof of the squeeze theorem; the limit (sin θ)/θ → 1; L'Hôpital's rule on the same function.
- Score: 7/10

---

## Candidate 07 — Build a Logarithmic Scale Comparison Tool with Claude

- Source: math-calculus/chapters/01-functions-and-graphs.md
- Lane: BUILD (Claude Code)
- Hook: Japan's magnitude-9 quake released ~350× the energy of Haiti's magnitude-7.3 — but the numbers look almost the same. Build a tool that takes any two Richter magnitudes and computes the energy ratio using the inverse function machinery.
- The artifact: a Python CLI tool that accepts two Richter magnitudes, computes amplitude ratio (10^(M2-M1)) and energy ratio (amplitude^1.5), and animates a bar chart on log scale showing the comparison. A Manim or matplotlib animation grows the bars from left to right with the ratio labeled.
- Prompt seed: `claude "Build a Python script that takes two Richter magnitudes M1 and M2, computes: amplitude_ratio = 10^(M2-M1), energy_ratio = amplitude_ratio^1.5. Print both ratios. Then create a matplotlib bar chart comparing the two earthquakes on a logarithmic y-axis, with bars animated growing from zero. Label the bars with the ratio."`
- Read / check: Verify amplitude_ratio = 10^(9-7.3) = 10^1.7 ≈ 50. Verify energy_ratio = 50^1.5 ≈ 354. Check the log-scale bar chart renders correctly (no negative values). Confirm the labels are legible.
- Human supplies: Nothing — fully synthetic. Real Richter values are public knowledge and the formula is standard.
- Output medium: screen-recording mp4 (animated bar chart on log scale)
- The change: Add pH and decibels as selectable scale types — letting users see the same inverse-function pattern across three different logarithmic scales.
- Teardown angle: The logarithm compresses enormous ranges into human-readable numbers, but the inverse function is what restores the true scale. Every domain that uses log scales (earthquakes, sound, pH, stellar magnitude) is making the same mathematical choice.
- Exclusions: Derivation of seismic energy formula; comparison to nuclear weapons yield; historical context of Richter scale.
- Score: 7/10

---

## Candidate 08 — Animate the ε-δ Definition with Claude

- Source: math-calculus/chapters/02-limits.md
- Lane: BUILD (Claude Code)
- Hook: Most students memorize ε-δ without understanding it. What if you could animate the "game": your opponent picks ε (output tolerance), you must find δ (input tolerance) that keeps the function within ε of L? Watch the game play out on screen.
- The artifact: a Manim animation for the limit lim_{x→3}(2x+1) = 7. Animation shows: the function plotted; the horizontal band [7-ε, 7+ε] drawn in red; the viewer types ε=0.5 then ε=0.1; for each, the animation draws the corresponding [3-δ, 3+δ] vertical band in blue, showing that the function stays within the red band whenever x stays within the blue band.
- Prompt seed: `claude "Create a Manim animation demonstrating the epsilon-delta definition of the limit for f(x)=2x+1 at x=3, L=7. Show: 1) the function plotted, 2) animate a red horizontal band [L-eps, L+eps] appearing for eps=0.5, 3) find delta=eps/2, 4) animate a blue vertical band [3-delta, 3+delta], 5) highlight that the function stays within the red band when x is in the blue band. Repeat for eps=0.1."`
- Read / check: Verify δ = ε/2 is the correct choice for f(x)=2x+1. Check that the function values within the blue band do fall within the red band. Confirm both ε values demonstrate the relationship visually. Verify the animation is timed so the viewer can follow the two-step game.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim (interactive-style band animation)
- The change: Switch to f(x) = x² at x=2 to show a nonlinear case where finding δ requires more work — demonstrating the general procedure.
- Teardown angle: The ε-δ definition is not abstract formalism — it is a precise formulation of the intuitive idea that "you can get the output as close to L as you want by controlling the input." The game framing makes that operational.
- Exclusions: Full formal proofs; real analysis; the historical development from Newton to Weierstrass.
- Score: 7/10

---

## Candidate 09 — Optimize a Rectangle Under Constraint with Claude

- Source: math-calculus/chapters/04-applications-of-derivatives.md
- Lane: BUILD (Claude Code)
- Hook: A fenced field with one wall free always has the same optimal proportion — x = 2y — regardless of total fencing. Claude derives it, plots A(y), and animates the critical point.
- The artifact: a Python script that computes A(y) = (100-2y)·y, finds the critical point analytically (A'(y)=0 → y=25), and animates the area function as a parabola with a marker sweeping to the maximum. Second animation shows a rectangle changing shape, with area counter, converging on the optimal 50×25 dimension.
- Prompt seed: `claude "Write a Python script: 1) Define A(y) = (100-2y)*y for a fencing optimization with 100ft of fence and one wall free. 2) Find the critical point by solving A'(y)=0 symbolically using sympy. 3) Plot A(y) over y=0 to 50 with matplotlib, marking the maximum. 4) Animate a rectangle growing from y=1 to y=50, showing changing dimensions and area, pausing at the optimum. Save animation as mp4."`
- Read / check: Verify critical point at y=25, x=50, A=1250 sq ft. Check sympy correctly differentiates and solves. Confirm the animation pauses at the correct optimal dimensions. Verify the proportion x=2y is displayed.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim or screen-recording mp4 (animated parabola + rectangle morphing)
- The change: Switch to the classic can-optimization (minimize surface area of a cylinder for fixed volume) and show the optimal r = h/2 proportion.
- Teardown angle: Calculus optimization gives the general answer, not just the specific number — the proportion x=2y holds for any fence length. This is why calculus is more powerful than trial-and-error.
- Exclusions: Lagrange multipliers; multivariable optimization; second-order sufficiency conditions.
- Score: 7/10

---

## Candidate 10 — Measure the Gaussian's Numerical Area with Claude

- Source: math-calculus/chapters/05-integration.md
- Lane: BUILD (Claude Code)
- Hook: e^{-x²} has no elementary antiderivative — proven by Liouville. But its integral from -∞ to ∞ equals exactly √π. Build the numerical integrator and watch it converge to 1.7724... from Riemann sums.
- The artifact: a Python script using scipy.integrate.quad to compute ∫_{-5}^{5} e^{-x²} dx (approximating the infinite limits) and then animating a Riemann sum approximation converging to √π. The animation shows n=4, 8, 16, 32, 64 rectangles, with the running sum displayed and √π marked as a red line.
- Prompt seed: `claude "1) Use scipy.integrate.quad to compute the integral of exp(-x^2) from -10 to 10. Print the result and compare to sqrt(pi). 2) Create a matplotlib animation showing Riemann sum approximations for n=4,8,16,32,64 rectangles. Show the running sum and absolute error from sqrt(pi). Mark sqrt(pi) as a red horizontal dashed line."`
- Read / check: Verify result ≈ 1.7724538 ≈ √π. Check Riemann sum error sequence is decreasing. Confirm the red line for √π is correctly placed. Verify scipy.integrate.quad result matches to 6+ decimal places.
- Human supplies: Nothing — fully synthetic.
- Output medium: screen-recording mp4 (animated Riemann convergence)
- The change: Use the polar-coordinates trick to prove ∫∫ e^{-(x²+y²)} dx dy = π analytically, then take the square root — showing why the answer is √π.
- Teardown angle: The fact that no elementary antiderivative exists doesn't mean the integral has no value — it means numerical methods are the right tool, and they converge arbitrarily close. The FTC's trade-off is honest: closed forms for some, numerical for the rest.
- Exclusions: Liouville's theorem (the full proof); complex analysis; special functions (erf).
- Score: 6/10
