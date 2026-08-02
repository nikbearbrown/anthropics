# Prealgebra Bundle with LLMs — CLI Video Ideas ("X with Claude")

## Candidate 01 — "Build a Compound Interest Model with Claude: From Linear to Exponential Growth"
- Source: prealgebra-bundle-with-llms/chapters/01-foundations.md (LLM Exercise: Modeling One Phenomenon Project, Ch. 1 installment)
- Lane: BUILD (Claude Code)
- Hook: Linear savings models (add $100/month) vs. exponential growth (earn interest on interest) — the gap between them is invisible at year 1 but enormous at year 30. Claude writes the model and the animation shows where they diverge.
- The artifact: A plot of three savings trajectories over 30 years: (1) Linear: $200/month deposited, no interest; (2) Simple interest: $200/month + 6% annual on principal only; (3) Compound interest: $200/month + 6% compounded monthly. All three start the same; by year 30 the compound curve is ~2× the linear. The crossover point where compound dramatically outpaces linear is annotated.
- Prompt seed: `claude "Write Python that models three savings strategies over 30 years (360 months): (1) Linear: monthly deposit D=200, no interest; (2) Simple interest: deposit D + 0.06/12 * P0 per month on initial principal only; (3) Compound: monthly balance B = (B_prev + D) * (1 + r/12) where r=0.06. Plot all three on one axes. Label the final balance for each at year 30. Mark the point where compound interest first exceeds 150% of linear savings."`
- Read / check: Code: verify linear balance at year 30 = 200 × 360 = $72,000; verify compound balance using FV formula FV = D × ((1+r/12)^360 - 1) / (r/12) ≈ $200,903; verify compound exceeds 2× linear within the 30-year window. Output: the compound curve should clearly diverge from linear after year 15.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim — animate the three curves growing year by year; annotate final values and the crossover point; show the "interest on interest" visual as a shaded region between simple and compound curves.
- The change: Vary the interest rate from 2% to 10% and show how the final compound balance changes — demonstrating that even a 1% rate difference produces large long-run differences (the power of marginal rates).
- Teardown angle: Compound interest is the most important financial concept in prealgebra — the math is simple (repeated multiplication) but the implications take a lifetime to feel. This model makes the exponential curve visceral.
- Exclusions: Tax treatment of investment returns; risk vs. return trade-off; inflation adjustment.
- Score: 9/10

## Candidate 02 — "Solve Systems of Equations with Claude: Traffic Flow and Budget Constraints"
- Source: prealgebra-bundle-with-llms/chapters/05-systems-of-linear-equations.md (LLM Exercise: Ch. 5 installment of cross-chapter project)
- Lane: BUILD (Claude Code)
- Hook: Every "word problem" about mixtures, traffic, and budgets reduces to a 2×2 linear system. Claude solves them by substitution AND elimination, plots both lines, and shows that the solution is exactly the crossing point — making the geometry visible.
- The artifact: A plot of two linear equations from a budget constraint problem (e.g., 2x + 3y = 120 for total cost, x + y = 50 for total items). The two lines are plotted; their intersection labeled (x=30, y=20) with units (30 adult tickets, 20 child tickets). A table shows the step-by-step substitution and elimination solutions side by side. Final: both methods produce the same answer.
- Prompt seed: `claude "Write Python that solves a 2x2 system of linear equations using both substitution and elimination. System: 2x + 3y = 120 (total cost in dollars), x + y = 50 (total number of items). Show both methods step by step. Plot both equations as lines on a graph with x from 0 to 60, shade the feasible region if constraints apply. Mark the intersection point. Also solve using numpy.linalg.solve and verify all three methods agree."`
- Read / check: Code: verify substitution, elimination, and numpy all give x=30, y=20; verify the plotted lines intersect at (30, 20); verify both constraint equations are satisfied by substituting the solution. Output: all three solution methods should print identical (x, y) values.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim — animate the two lines being drawn; the intersection point appearing with a flash; a panel showing the elimination steps canceling the variable.
- The change: Change to an inconsistent system (parallel lines, no solution) and show what the code outputs — "no solution" — and what the graph looks like (parallel lines). Then show a dependent system (same line, infinite solutions).
- Teardown angle: Every 2×2 system has exactly one of three outcomes: one solution (lines cross), no solution (lines parallel), infinitely many (same line). The geometry makes the algebra structure obvious.
- Exclusions: 3×3 systems; matrix determinants; linear programming (feasible regions with inequalities).
- Score: 8/10

## Candidate 03 — "Build a Speed-Distance Calculator with Claude: Motion Problems Visualized"
- Source: prealgebra-bundle-with-llms/chapters/05-systems-of-linear-equations.md
- Lane: BUILD (Claude Code)
- Hook: "Two trains leave the station..." is a cliche because it's a real problem: when do two moving objects meet, and where? A system of equations gives the answer in seconds — and Claude animates the solution.
- The artifact: A distance-vs-time animation for two trains: Train A leaves Boston at 60 mph, Train B leaves New York (215 miles away) at 45 mph toward Boston. The two distance-from-Boston curves are plotted; their intersection marks the meeting point (distance 129 miles from Boston, time 2.15 hours). A map strip shows the meeting point geographically.
- Prompt seed: `claude "Write Python that models two trains on the same track 215 miles apart. Train A: leaves position 0 at speed 60 mph. Train B: leaves position 215 at speed -45 mph (traveling toward A). Distance from position 0: d_A(t) = 60t, d_B(t) = 215 - 45t. Find meeting time t* = 215/(60+45) and position x* = 60*t*. Plot both trajectories vs time from t=0 to t=4 hours. Mark the meeting point. Also solve using a linear system: d_A = d_B."`
- Read / check: Code: verify t* = 215/105 ≈ 2.048 hours; verify x* = 60 × 2.048 ≈ 122.9 miles from position 0; verify both distance functions give the same value at t*. Output: the two trajectory lines should cross at exactly the computed (t*, x*) point.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim — animate the two trains moving toward each other on a track, with a distance-time plot updating in real time; flash the meeting point when they cross.
- The change: Add a third scenario: Train B leaves 30 minutes later. Show the meeting point shifts, and require solving the modified system — the delay changes both the meeting time and location.
- Teardown angle: Distance = rate × time is the most important formula in prealgebra — not because trains are important, but because the same structure models anything that accumulates: money, work, flow. The system of equations is just two accumulations that meet.
- Exclusions: Acceleration; quadratic distance equations; relativity corrections at high speed.
- Score: 8/10

## Candidate 04 — "Model Linear Inequalities with Claude: Budget Feasibility Region"
- Source: prealgebra-bundle-with-llms/chapters/02-solving-linear-equations-and-inequalities.md
- Lane: BUILD (Claude Code)
- Hook: A budget constraint is an inequality, not an equation — you can spend less than $100, but not more. Claude plots the feasibility region and shows that every point inside is a valid plan, not just the one on the line.
- The artifact: A 2D feasibility region plot: x = cups of coffee ($3 each), y = sandwiches ($8 each), budget constraint 3x + 8y ≤ 96. The feasible region is shaded (all (x,y) combinations that fit the budget). Corner points are labeled. A second constraint added: x + y ≥ 5 (must buy at least 5 items). The feasible region shrinks to a polygon.
- Prompt seed: `claude "Write Python that plots the feasible region for a budget problem: constraint 1: 3x + 8y <= 96 (budget), constraint 2: x + y >= 5 (minimum items), constraint 3: x >= 0, y >= 0 (non-negative). Use matplotlib to shade the feasible region. Find and mark the corner points of the polygon (vertices of the feasible region). Label each corner with its (x, y) value and the total cost."`
- Read / check: Code: verify all 4 constraints are plotted as boundary lines; verify corner points satisfy all constraints simultaneously; verify the shaded region is the intersection of all four half-planes. Output: corner points should include (0,12) for budget limit on y-axis, (32,0) for x-axis, and two interior vertices.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim — animate the constraints being added one by one, each cutting the feasible region; final frame shows the polygon with corner points labeled.
- The change: Find the combination inside the feasible region that maximizes total satisfaction (objective function: maximize 2x + 5y "enjoyment units") — a preview of linear programming.
- Teardown angle: Inequalities are more realistic than equations — budgets are constraints, not exact targets. The feasibility region makes visible all valid plans at once, rather than finding a single "correct" answer.
- Exclusions: Simplex method for LP; integer programming; economic duality.
- Score: 8/10

## Candidate 05 — "Build a Unit Conversion Calculator with Claude: Dimensional Analysis Chains"
- Source: prealgebra-bundle-with-llms/chapters/01-foundations.md
- Lane: BUILD (Claude Code)
- Hook: Unit conversion is dimensional analysis — multiply by fractions that equal 1 until the wrong units cancel. Claude chains together 5 conversion steps and shows that the chain always collapses correctly, even for absurd conversions.
- The artifact: A conversion chain animation: converting 60 miles per hour → meters per second, shown as a sequence of multiplications with labeled fractions (×1609.34 m/1 mi × 1 hr/3600 s = 26.82 m/s). A table of 10 extreme conversions (light-years to centimeters, acres to square millimeters) each shown with the chain and the result. A "dimensional analysis checker" that verifies units cancel correctly.
- Prompt seed: `claude "Write Python that implements a dimensional analysis unit converter. Store unit conversion factors as a dictionary. Build a function chain_convert(value, from_unit, to_unit) that finds a path between units and multiplies the conversion factors. Test with: (1) 60 mph to m/s, (2) 1 light-year to km, (3) 1 acre to sq meters, (4) 100 Celsius to Fahrenheit. Print the conversion chain as a fraction multiplication for each."`
- Read / check: Code: verify 60 mph = 26.82 m/s within 0.01%; verify 1 light-year = 9.461×10¹² km; verify unit cancellation logic produces correct units at each step. Output: the chain display should show all intermediate fractions clearly with unit labels.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim — animate the conversion chain as a series of fractions multiplying, with each unit label crossing out when it cancels; final answer revealed at the end of the chain.
- The change: Build the conversion for a compound unit: convert 35 miles per gallon to kilometers per liter — requiring two separate chains for distance and volume, then combining.
- Teardown angle: Dimensional analysis is the most reliable check in science and engineering: if the units don't cancel to what you expected, the formula is wrong. Every physics textbook says this; prealgebra is where you should learn it.
- Exclusions: SI base units derivation; non-linear unit conversions (dB, pH); natural units in physics.
- Score: 7/10

## Candidate 06 — "Fit a Linear Model with Claude: Scatter Plot to Best-Fit Line"
- Source: prealgebra-bundle-with-llms/chapters/01-foundations.md (Modeling One Phenomenon Project — builds toward linear model fit)
- Lane: BUILD (Claude Code)
- Hook: A scatter plot of real data almost never lines up perfectly — but a linear model finds the best straight line through the noise. Claude fits one, computes the residuals, and shows where the model is wrong.
- The artifact: A scatter plot of 20 data points (e.g., hours studied vs. exam score, or temperature vs. ice cream sales) with the least-squares best-fit line y = mx + b overlaid. Three panels: (1) raw scatter; (2) best-fit line with equation labeled; (3) residual plot (errors between points and the line). R² value labeled, and one outlier identified and annotated.
- Prompt seed: `claude "Write Python that generates 20 synthetic data points: x = hours studied from 1 to 10 (repeated twice), y = 60 + 3.5*x + normal_noise(sigma=5). Fit a linear model using numpy.polyfit. Plot: (1) scatter + best-fit line with equation, (2) residuals vs x. Compute R^2. Add one intentional outlier at (5, 95) and show how it affects the fit. Print slope, intercept, and R^2 before and after adding the outlier."`
- Read / check: Code: verify slope ≈ 3.5 before outlier (within noise); verify R² decreases after adding outlier; verify residuals are randomly distributed around zero (no pattern). Output: the residual plot should show random scatter (no trend) for a good linear fit.
- Human supplies: Nothing — fully synthetic (noise generated by code). For a more authentic video, the human could supply a real dataset (e.g., class scores from a real course).
- Output medium: Manim — animate the scatter points appearing, then the best-fit line being drawn; animate the residual lines from each point to the line; show R² building up.
- The change: Fit a quadratic model (y = ax² + bx + c) to the same data and compare R² — showing that adding a parameter always improves fit, but the improvement is small for data that's truly linear.
- Teardown angle: The best-fit line minimizes the sum of squared residuals — it doesn't go through any point perfectly, but it's as close as a straight line can get to all of them simultaneously. This is the first step of all data science.
- Exclusions: Multiple regression; overfitting; cross-validation.
- Score: 7/10

## Candidate 07 — "Visualize Fraction Arithmetic with Claude: Adding Fractions on a Number Line"
- Source: prealgebra-bundle-with-llms/chapters/01-foundations.md
- Lane: BUILD (Claude Code)
- Hook: Adding fractions with different denominators is the most-failed topic in prealgebra — because students learn the algorithm without seeing why the common denominator is necessary. A number line animation makes the geometry obvious.
- The artifact: A number line animation showing: (1) 1/3 marked as one blue segment of 3 equal parts; (2) 1/4 marked as one red segment of 4 equal parts; (3) When you try to add them directly, the parts don't align; (4) After finding LCD=12, both fractions are redrawn as 4/12 and 3/12 — now they align; (5) Addition: 4/12 + 3/12 = 7/12, shown as a combined segment.
- Prompt seed: `claude "Write Python that creates a number line visualization for fraction addition. Show fractions 1/3 and 1/4: (1) Draw 1/3 on a number line divided into thirds (blue). (2) Draw 1/4 on a number line divided into fourths (red). (3) Find LCD = lcm(3,4) = 12. (4) Redraw both fractions on a number line divided into twelfths. (5) Show the sum 7/12 as a combined segment. Use matplotlib with colored segment patches."`
- Read / check: Code: verify LCD computed correctly via math.lcm; verify segment lengths are proportional to fraction values; verify 4/12 + 3/12 = 7/12 both visually and numerically. Output: the twelfths number line should show exactly 7 filled segments for the sum.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim — animate the three number lines appearing sequentially; animate the LCD finding step with the divisor marks appearing; animate the segments combining for the sum.
- The change: Show the same process for 1/6 + 1/4 where the LCD is 12 (not 24) — reinforcing that you use the LCD, not just the product of denominators, and the segments come out smaller.
- Teardown angle: The common denominator is not an algorithm — it's the answer to "what unit can measure both fractions exactly?" Finding the LCD is finding the common ruler. Every fraction is just a count of ruler units.
- Exclusions: Fraction multiplication and division (different geometric intuition); mixed numbers; continued fractions.
- Score: 7/10

## Candidate 08 — "Model Mixture Problems with Claude: Algebra in the Chemistry Lab"
- Source: prealgebra-bundle-with-llms/chapters/05-systems-of-linear-equations.md
- Lane: BUILD (Claude Code)
- Hook: Mixture problems (blend 40% solution with 60% solution to make 50% solution) are in every prealgebra textbook — because the math is the same as mixing alloys, adjusting pH, and blending coffee. Claude solves a real one and shows the two-equation system behind it.
- The artifact: A bar chart animation showing a mixture problem: x liters of 40% acid solution + y liters of 60% acid solution = 10 liters of 50% acid solution. Two equations: x + y = 10 (volume), 0.4x + 0.6y = 5 (acid). Solution: x=5, y=5. The bar chart shows the acid content of each component stacking to the target.
- Prompt seed: `claude "Write Python that solves a mixture problem: x liters of 40% acid + y liters of 60% acid = 10 liters of 50% acid. Set up system: x+y=10, 0.4x+0.6y=5. Solve using numpy.linalg.solve. Then plot a stacked bar chart: left bar = x liters of 40% (split into acid=0.4x and water=0.6x), right bar = y liters of 60% (split into acid=0.6y and water=0.4y), result bar = 10 liters of 50%. Verify acid amounts balance."`
- Read / check: Code: verify x=5, y=5; verify 0.4(5) + 0.6(5) = 2 + 3 = 5 liters acid = 50% of 10 liters; verify the bar chart shows acid amounts that add up correctly. Output: all three bar charts should show total height = correct volume with correct proportion of acid (colored) vs. water (gray).
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim — animate the two ingredient bars pouring into a combined container; the proportion lines settling to 50%; the two-equation system appearing beside the animation.
- The change: Change to a 3-solution mixture (adding pure water as a third component) and show how the system becomes 2 equations in 3 unknowns — underdetermined, requiring an additional constraint to solve.
- Teardown angle: Mixture problems are systems of equations in disguise — one equation for the whole (total volume), one for the part (solute amount). The same structure applies to alloys, income blends, and portfolio weightings.
- Exclusions: Non-linear mixing (temperature, phase changes); multi-component chemical equilibria.
- Score: 7/10

## Candidate 09 — "Build a Prime Factorization Tree with Claude: GCF and LCM from Structure"
- Source: prealgebra-bundle-with-llms/chapters/01-foundations.md
- Lane: BUILD (Claude Code)
- Hook: The GCF and LCM of two numbers are completely determined by their prime factorization trees — and visualizing the trees side by side makes the algorithm obvious. Claude builds the trees and animates the GCF/LCM extraction.
- The artifact: Side-by-side prime factorization trees for two numbers (e.g., 48 and 36). Each number splits into its prime factors (48 = 2⁴ × 3, 36 = 2² × 3²). A Venn-diagram overlay shows: common primes → GCF, all primes → LCM. Computed: GCF(48,36) = 2² × 3 = 12; LCM(48,36) = 2⁴ × 3² = 144.
- Prompt seed: `claude "Write Python that computes and displays prime factorization trees for two numbers (48 and 36). Use sympy.factorint to get prime factors with exponents. Draw the factorization tree structure using networkx. Then display a text-based Venn diagram: common prime factors in the overlap, unique factors on each side. Compute GCF = product of min exponents, LCM = product of max exponents. Verify GCF * LCM = 48 * 36."`
- Read / check: Code: verify prime_factors(48) = {2:4, 3:1}; verify prime_factors(36) = {2:2, 3:2}; verify GCF=12, LCM=144; verify GCF × LCM = 48 × 36 = 1728. Output: the Venn diagram should show 2² and 3 in the overlap, 2² extra on the 48 side, 3 extra on the 36 side.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim — animate the tree branching from each number; then animate the Venn diagram overlay with GCF factors highlighted in the center.
- The change: Try three numbers (48, 36, 60) and show how the GCF extends to three-way intersection of prime factors; verify GCF(48,36,60) = 12.
- Teardown angle: GCF and LCM are not algorithms — they're consequences of the Fundamental Theorem of Arithmetic (unique prime factorization). The Venn diagram makes the structure visible: GCF is the overlap, LCM is the union.
- Exclusions: Euclidean algorithm for GCF; modular arithmetic; applications in fraction simplification (covered separately).
- Score: 6/10
