# MBA Math — CLI Video Ideas ("X with Claude")

## Candidate 01 — "Build the Compounding Trap: Why Up 40% Then Down 40% Loses $16M with Claude"
- Source: mba-math/chapters/01-percentages-ratios-and-growth-rates.md
- Lane: BUILD (Claude Code)
- Hook: Every finance presentation adds percentages that the world multiplies — a $100M division "back to even" is actually $84M, and the gap is invisible until you plot it.
- The artifact: An animated Manim number-line showing $100M rising 40% to $140M then falling 40% to $84M, with the $16M cross-term ab highlighted as a sweeping bracket; a second panel sweeps CAGR vs. arithmetic-mean growth curves for the tuition example (5× over 40 years) to show the geometric-mean divergence.
- Prompt seed: `claude "Write a Python Manim script: animate a number line from $84M to $140M to $84M showing the up-40/down-40 path. Label the $16M gap as the cross-term ab = (0.4)(0.4). Second scene: plot arithmetic-mean vs. compound-growth curves for $5k→$25k over 40 years. Output vox-palette colors."`
- Read / check: Verify the cross-term ab = −0.16 numerically in the script; confirm both curves use the same endpoints and the CAGR = (5)^(1/40)−1 ≈ 4.10% is labeled correctly. Check that the animation pauses on the gap marker.
- Human supplies: Nothing — fully synthetic. The $5k→$25k tuition CAGR example uses only analytic inputs; no real dataset needed.
- Output medium: Manim (animated)
- The change: Add a third scene: show the Rule of 72 approximation (72/4.1 ≈ 17.6 years to double) as a tick-mark on the curve, then verify it against the exact compound formula.
- Teardown angle: Additive intuition is built into every planning meeting. The $16M gap is not rounding error — it is the cross-term ab that silent multiplication always produces. CAGR is a geometric mean, never an arithmetic one.
- Exclusions: Fisher equation / real-vs-nominal derivation; index-number construction; nominal vs. real detour.
- Score: 9/10

## Candidate 02 — "Build an NPV vs. IRR Profile with Claude: When the Two Numbers Fight"
- Source: mba-math/chapters/05-dcf-npv-irr-and-valuation.md
- Lane: BUILD (Claude Code)
- Hook: Two projects, one with a higher IRR and one with a higher NPV — pick the wrong rule and you destroy $3.3M of value, even though your spreadsheet says you're winning.
- The artifact: A d3-animated NPV-profile chart: two downward-sloping curves (Big project and Small project) plotted over a range of discount rates, each labeled with its IRR where it crosses zero; the 9% hurdle-rate vertical line sweeps in and a red dot highlights that Big wins at that rate despite having the lower IRR. A second frame shows the IRR-as-polynomial-root derivation for a project with two sign changes, with two roots marked.
- Prompt seed: `claude "Write a d3.js script: plot NPV vs. discount rate for Big (CF: -100, +40, +60, +50, NPV=$8.4M@9%) and Small (CF: -30, +20, +20, +20, NPV=$5.1M@9%) on the same axes. Animate the 9% vertical hurdle line sweeping in. Mark each curve's IRR crossing. Vox palette. Export runnable HTML."`
- Read / check: Verify the NPV calculations at r=9% match the book's $8.4M and $5.1M; check that Descartes' sign-change count for the two-sign-change project gives 2 possible IRRs; confirm the d3 scales don't clip curves.
- Human supplies: Nothing — fully synthetic. The cash flows are analytic; no real project data required.
- Output medium: d3 (animated)
- The change: Add an MIRR calculation for the Small project using a 9% reinvestment rate and show it on the chart, exposing why the "reinvestment rate assumption" story is a patch, not the real explanation.
- Teardown angle: IRR is a polynomial root — it can be multiple, absent, or misleading. NPV is the right rule because it measures dollars created, not a scale-blind percentage. The polynomial framing dissolves the textbook myth in one sentence.
- Exclusions: Bond pricing derivation; Gordon-model sensitivity detail; payback-period discussion.
- Score: 9/10

## Candidate 03 — "Simulate a Monte Carlo Option Pricer with Claude: Why Volatility is the Only Unknown"
- Source: mba-math/chapters/14-quantitative-finance-returns-volatility-options-monte-carlo.md
- Lane: BUILD (Claude Code)
- Hook: Black-Scholes prices an option from five inputs — four you can look up right now. Only sigma has to be estimated, and everything interesting in options trading lives in disagreement about that one number.
- The artifact: A Manim animation of 200 simulated GBM price paths fanning out from $185 (Jin's stock), with ±1σ√t and ±2σ√t envelopes widening as a sideways-parabola cone; a second panel computes the Monte Carlo call price from the payoff distribution, showing the discounted average converging as N paths grows (√N convergence bar); a third frame shows implied volatility backed out of a put price.
- Prompt seed: `claude "Write Python using numpy and matplotlib (Manim-wrapped): simulate 200 GBM paths for S₀=185, σ=0.25, r=0.045, T=0.5; draw the √t volatility cone; compute Monte Carlo call price for K=185; plot convergence of the estimate as N increases from 10 to 10000. Vox palette."`
- Read / check: Verify the annualized vol formula (daily σ × √252) is correct in the script; check that the Monte Carlo average converges to within $1 of Black-Scholes at N=10,000; confirm paths don't go negative.
- Human supplies: Nothing — fully synthetic. All inputs are illustrative; no live options data needed (book explicitly labels the worked example as illustrative).
- Output medium: Manim (animated)
- The change: Replace σ=0.25 with σ=0.35 and overlay the new cone and Monte Carlo price, showing how one extra 10-vol-point widens the cone and raises the put premium.
- Teardown angle: The √t rule is not a convention — it is a consequence of variance adding under independence. Monte Carlo prices anything by averaging, and its error shrinks as 1/√N — the same √-law, now governing simulation accuracy not price uncertainty.
- Exclusions: Black-Scholes PDE derivation; volatility-smile/skew deep dive; stochastic-vol models.
- Score: 9/10

## Candidate 04 — "Build Bayes' Rule from Natural Frequencies with Claude: The 15% Fraud Test"
- Source: mba-math/chapters/13-decision-analysis-trees-expected-utility-and-bayes.md
- Lane: BUILD (Claude Code)
- Hook: A fraud test is 90% sensitive, 5% false-positive rate, base rate 1%. Everyone says 90% chance of fraud. The correct answer is 15% — and you can derive it in 30 lines of code that draws the proof.
- The artifact: A Manim natural-frequency tree: 1,000 firms split into 10 fraudulent and 990 clean; each branch splits into flagged/not-flagged with pixel-block counts; 59 flagged total, only 9 truly fraudulent; the 9/59 fraction animates to 15%. A second panel sweeps the base rate from 0.1% to 10% and shows how the posterior probability curve rises.
- Prompt seed: `claude "Write Manim: draw a natural-frequency tree for 1000 firms (1% fraud base rate, 90% sensitivity, 5% FPR). Animate: split into 10 fraud/990 clean, split each into flagged/not-flagged with counts, circle the 59 total flagged and highlight the 9 true positives. Add a second panel: plot P(fraud|flag) vs. base-rate from 0.1% to 10%. Vox palette."`
- Read / check: Confirm that 9/(9+49.5) = 0.154 ≈ 15% matches the formula result; verify the sensitivity/FPR are correctly applied in both panels; check that the base-rate sweep is monotone and passes through 15% at base=1%.
- Human supplies: Nothing — fully synthetic. All parameters are analytic.
- Output medium: Manim (animated)
- The change: Change the test to 99% sensitive and 5% FPR (a "better" test) and show that the posterior at 1% base rate only rises to ~17%, demonstrating that base rate dominates in rare-event detection.
- Teardown angle: Natural-frequency counting is not a simplification of the formula — it is the formula, made legible. The posterior is dominated by the size of the clean population flooding the flagged pool. Improving test sensitivity has much less effect than practitioners expect when the base rate is low.
- Exclusions: EVPI derivation; decision-tree rollback for large trees; prospect theory.
- Score: 8/10

## Candidate 05 — "Solve the Prisoner's Dilemma LP with Claude: Why the Detergent Cartel Needed a Secret Meeting"
- Source: mba-math/chapters/12-matrices-linear-programming-and-game-theory.md
- Lane: BUILD (Claude Code)
- Hook: Four soap companies met in Paris cafes for seven years to agree on prices — because individually they had no choice but to undercut each other. The math shows the trap they were in, exactly.
- The artifact: A d3 animation of the 2×2 payoff grid; arrows sweep in showing each player's dominant strategy (Low); the Nash equilibrium cell (Low, Low) = (20, 20) highlights in red while (High, High) = (50, 50) is labeled "jointly better but unstable." A second frame shows the LP feasible-region plot (factory example) with the iso-profit line sliding to the corner at (30, 10), Z=$1,300.
- Prompt seed: `claude "Write d3.js: animate a 2×2 prisoner's dilemma payoff grid; sweep in arrows for dominant-strategy selection; highlight the Nash equilibrium cell. Second panel: draw the LP feasible region for 2x+4y≤100, x+y≤40 with the iso-profit line Z=30x+40y sliding outward to the optimal corner (30,10). Vox palette. Runnable HTML."`
- Read / check: Verify the corner evaluations: (0,0)→0, (40,0)→1200, (0,25)→1000, (30,10)→1300; confirm Nash cell is (Low,Low) and check best-response arrows for both players; verify the constraint lines intersect at (30,10).
- Human supplies: Nothing — fully synthetic.
- Output medium: d3 (animated)
- The change: Add a shadow-price scene: relax the machine-hours constraint from 100 to 101 and re-solve, animating the corner shift and labeling the $Δ as the Lagrange multiplier / shadow price.
- Teardown angle: The cartel needed a secret meeting because the Nash equilibrium is stable at the individually rational but collectively terrible outcome. LP shows that the optimum always lives at a corner — infinite interior is never where you need to search.
- Exclusions: Simplex algorithm step-through; mixed-strategy equilibrium algebra; Karmarkar interior-point method.
- Score: 8/10

## Candidate 06 — "Fit a Regression Beta with Claude: What R² Really Means for Portfolio Risk"
- Source: mba-math/chapters/09-regression-and-forecasting.md
- Lane: BUILD (Claude Code)
- Hook: Finance's most-run regression has a name for its slope: beta. And R² is not "how good is the model" — it is the fraction of the stock's variance that no amount of diversification can remove.
- The artifact: A Manim scatter-plot of 60 months of synthetic stock vs. market returns; the least-squares line animates in (b = Cov/Var), residuals draw as vertical segments, and the R²=0.40 split labels "systematic 40%" vs. "idiosyncratic 60%" as a horizontal bar decomposition. A second panel shows the holiday-season confounding example: slope drops from 4.2 to 2.6 when the season predictor is added.
- Prompt seed: `claude "Write Manim: generate 60 synthetic (market, stock) return pairs with beta=1.2 and R²≈0.40; draw the scatter, animate the OLS line arriving, mark residuals; split total variance into systematic and idiosyncratic bars. Second scene: two regression fits (naive β=4.2 vs. controlled β=2.6) for advertising-on-sales with and without a holiday dummy. Vox palette."`
- Read / check: Verify that the synthetic beta from the script matches the input β=1.2 within 0.1; check that systematic share = R² = 0.40; confirm the OLS slope formula b = Cov(x,y)/Var(x) is computed from the generated data, not hardcoded.
- Human supplies: Nothing — fully synthetic. The 60 return pairs are generated analytically.
- Output medium: Manim (animated)
- The change: Extrapolate the revenue trend line from 8 quarters to quarter 12, then shade the "danger zone" with a widening confidence band to show that high R² on past data does not guarantee future accuracy.
- Teardown angle: Beta is the covariance/variance ratio wearing a finance hat. R² here is not a fit diagnostic — it is a portfolio-risk decomposition. The confounding detour shows that a precise slope and a causal slope are completely different things.
- Exclusions: Multiple regression normal equations; Galton eugenics history beyond a sentence; spurious-correlation example beyond the advertising case.
- Score: 8/10

## Candidate 07 — "Animate the Annuity Formula with Claude: How a Geometric Series Generates All of Finance"
- Source: mba-math/chapters/04-time-value-of-money.md
- Lane: BUILD (Claude Code)
- Hook: Every mortgage payment, pension calculation, and bond price comes from one formula — and that formula is just the sum of a geometric series, derived in three lines of algebra most finance classes skip.
- The artifact: A Manim animation that derives the annuity formula step-by-step: write out the sum S = x + x² + ... + xⁿ, multiply by x, subtract to telescope, arrive at C·[1−(1+r)^−n]/r; then a bar-chart of discount factors across 30 years at 4%, 7%, 10% growing shorter over time; finally a growing-perpetuity cliff showing P = C/(r−g) exploding as g approaches r.
- Prompt seed: `claude "Write Manim: scene 1 — animate the geometric-series derivation of the annuity factor step by step with each algebraic manipulation appearing. Scene 2 — animated bar chart of discount factors 1/(1+r)^n for r=4,7,10% over n=1..30. Scene 3 — plot P=2/(0.08-g) for g=0..0.07 showing the vertical asymptote as g→r. Vox palette."`
- Read / check: Verify the annuity factor formula matches the standard closed form; check discount factors numerically at n=30: should be 0.308, 0.131, 0.057 for 4%, 7%, 10%; confirm the perpetuity curve diverges correctly at g=0.08.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim (animated)
- The change: Add a scene showing the early-vs-late saver comparison: Saver A contributes $5k/yr ages 22–30, Saver B ages 30–65, both at 8% — animate both wealth curves converging toward 65 to show A finishing ahead despite contributing 4× less.
- Teardown angle: One operation (multiply/divide by (1+r)) generates annuities, perpetuities, growing perpetuities, and the Gordon model — all from the same geometric series identity. The growing-perpetuity cliff is the visual proof that g matters more than C in long-horizon valuations.
- Exclusions: Continuous-compounding calculus; negative-rate episode; negative-interest discussion beyond a note.
- Score: 8/10

## Candidate 08 — "Build the Variance Algebra Proof with Claude: Why Standard Deviations Don't Add"
- Source: mba-math/chapters/07-probability-and-expected-value.md
- Lane: BUILD (Claude Code)
- Hook: Three product lines each have $2M revenue standard deviation; your colleague says total SD is $6M. The correct answer is $3.46M — and getting it wrong breaks every portfolio risk calculation you ever make.
- The artifact: A Manim animation: a box diagram where two independent random variables (σ=10 each) combine; variance adds to 200, SD = √200 ≈ 14.1, with "20" crossed out in red. A second panel shows the insurance example: 10,000 independent $10k-expected-loss policies, the insurer's per-policy SD shrinking by 1/√10,000 = 1/100 from $99.5k to $995, animated as a collapsing distribution.
- Prompt seed: `claude "Write Manim: scene 1 — two boxes labeled X (σ=10) and Y (σ=10) combine; animate Var(X+Y)=200, SD=14.1, cross out 20 in red. Scene 2 — draw bell curves for a single firm (σ=$99,500) and the insurer pooling 10,000 policies (σ=$995 per policy), overlaid to show the diversification collapse. Vox palette."`
- Read / check: Verify Var(coin flip at $500k) = E[X²] − (E[X])² = 1.25×10¹¹ − 6.25×10¹⁰ = 6.25×10¹⁰, SD=$250k; check the insurer SD = $99,500/√10,000 = $995; confirm the "20 crossed out" is graphically clear.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim (animated)
- The change: Extend to a binomial example: 50,000 mailer customers at p=0.03 response rate, animate the normal approximation bell curve with the 95% band (1,424–1,576) widening as n shrinks.
- Teardown angle: Variance adds; standard deviations do not. This single fact propagates through every standard error, every portfolio risk measure, and every insurance pricing model in the curriculum. The insurance example shows the cash value of diversification in one picture.
- Exclusions: St. Petersburg paradox extended; prospect theory; Kolmogorov axiom proofs.
- Score: 8/10

## Candidate 09 — "Build a Decision Tree Rollback with Claude: How to Put a Price on a Market Study"
- Source: mba-math/chapters/13-decision-analysis-trees-expected-utility-and-bayes.md
- Lane: BUILD (Claude Code)
- Hook: Should you pay for a market study before launching? The math gives you an exact ceiling — and it turns out most firms dramatically overpay for "strategic intelligence" that cannot move the decision.
- The artifact: A Manim decision-tree animation: square decision node branches to Settle (−$400k) and Trial (chance circle → 0.6×$0 + 0.4×−$1.2M = −$480k); rollback arrows sweep in; a second tree adds the pilot option and shows EVPI = $1.5M as the ceiling. A certainty-equivalent panel shows the √w utility curve with the risk-premium gap.
- Prompt seed: `claude "Write Manim: scene 1 — animate a decision tree with square node (Settle vs. Trial), chance circle (0.6→$0, 0.4→-$1.2M), rollback to EMV=-$480k, choose Settle at -$400k. Scene 2 — EVPI tree: perfect info gives 0.5×$5M + 0.5×$0 = $2.5M; EVPI = $2.5M - $1M = $1.5M. Scene 3 — concave utility u=√w with gamble outcomes and CE gap labeled. Vox palette."`
- Read / check: Verify rollback: 0.6(0) + 0.4(−1,200,000) = −480,000; confirm EVPI = 2.5 − 1 = 1.5M using the chapter's launch example; check CE: √(0.5×1M) = 500, CE = $250k for the utility example.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim (animated)
- The change: Re-run the tree with the CFO's actual risk-averse utility function (u=√w) to show the certainty-equivalent of the trial gamble is below even the −$400k settlement, justifying the CFO's settle decision even on near-neutral expected values.
- Teardown angle: EVPI is the ceiling — no study can ever be worth more. Most information buys are worth less than managers think because the study is imperfect and the prior odds already favor a dominant action. The rollback is exact; the inputs are contested.
- Exclusions: Allais/Ellsberg paradox deep dive; prospect theory vs. expected utility; multi-stage tree algebra.
- Score: 7/10

## Candidate 10 — "Simulate a CAPM Cost of Equity with Claude: Where the Discount Rate Comes From"
- Source: mba-math/chapters/06-cost-of-capital-capm-and-wacc.md
- Lane: BUILD (Claude Code)
- Hook: Three chapters of finance set up a discount rate of "9%" without explaining where 9% comes from. CAPM is literally the equation of a straight line — the Security Market Line — and every cost-of-equity estimate is just a point on it.
- The artifact: A Manim SML animation: axes of Expected Return vs. Beta; the risk-free rate anchors the y-intercept; the market portfolio marks (1, Rm); the SML line draws from left to right; three stocks with different betas plot as dots along the line, with their required returns labeled. A second panel animates the WACC formula as a weighted bar combining cost of equity and after-tax cost of debt.
- Prompt seed: `claude "Write Manim: draw the Security Market Line with Rf=4%, Rm=10%; mark betas 0.5, 1.0, 1.5 and their required returns; animate the line drawing with dots appearing. Second panel: WACC bar chart combining E/(D+E)×Re and D/(D+E)×Rd×(1-T) for Re=12%, Rd=6%, T=21%, D/E=0.5. Vox palette."`
- Read / check: Verify CAPM: E(R) = 4% + β(10%−4%) for each beta; confirm WACC formula numerically; check that the SML has positive slope and intercept at Rf=4%.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim (animated)
- The change: Shift the market risk premium from 6% to 4% and re-animate the SML slope flattening, showing how a 2-point change in the ERP moves every stock's cost of equity — linking back to the NPV sensitivity analysis from Chapter 5.
- Teardown angle: CAPM is a straight line, not a black box. The cost of equity is just a point read off that line using a beta derived from a regression (Chapter 9). The contested input is not the algebra — it is the equity risk premium, which finance cannot pin down from first principles.
- Exclusions: CAPM derivation from mean-variance optimization; Fama-French multi-factor model; tax shield derivation.
- Score: 7/10
