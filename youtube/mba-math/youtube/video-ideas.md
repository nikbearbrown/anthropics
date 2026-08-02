# MBA Math — Vox Explainer Video Candidates

Scouted from all 14 narrative chapters. Cards scored ≥ 8 only, ordered highest first.

---

## Candidate 01 — The Missing $16 Million
- Source: `mba-math/chapters/01-percentages-ratios-and-growth-rates.md`
- Topic: MBA MATH
- Hook: Up 40%, down 40% — everyone says "back to even." The company is down $16 million and nobody noticed.
- Key case: A division head reports +40% in H1, −40% in H2, and concludes the year was a wash. Actual ending value: $84M on a $100M base — a 16% loss hiding in plain sight.
- The Question: Why don't two equal-but-opposite percentage changes cancel?
- Core idea: Percentage changes compound (multiply) — they don't add. Successive factors are $(1+a)(1+b) = 1 + a + b + \mathbf{ab}$; the cross-term $ab$ is the interest-on-interest the additive view drops, and it is always negative when $a$ and $b$ have opposite signs. The loss is exact: $100 \times |ab| = 100 \times 0.16 = \$16M$.
- Visual object: Number line tracing $100M → $140M (+40%) → $84M (−40%), with the $16M gap labeled as the cross-term $ab$.
- Manim move: trace (walk the number line forward then back, then morph the algebraic expansion $(1+a)(1+b)$ to reveal the $ab$ term)
- Example seed: Start $100M. Up 40% to $140M. Down 40% on the new base: $140M × 0.6 = $84M. The gap is $(0.40)(0.40) × $100M = $16M. Reverse the order — down first, then up — and you land at the same $84M.
- Length band: 2–3 min
- Still lanes: geo
- Prerequisites: Basic arithmetic; notion of percentages as fractions of a current base
- Exclusions: CAGR derivation, Fisher equation, index numbers — all reserved for other cards or omitted
- Score: 10/10

---

## Candidate 02 — Why Adding Risky Stocks Makes You Safer
- Source: `mba-math/chapters/10-risk-correlation-and-portfolio-math.md`
- Topic: MBA MATH
- Hook: You can take two risky stocks, combine them, and end up with something less risky than either one — without changing your expected return.
- Key case: A defensive stock (σ = 18%) and a cyclical stock (σ = 28%) held 50/50. The naive guess for portfolio risk is the weighted average: 23%. At ρ = 0.2 the actual portfolio standard deviation is 18.1% — less risky than the safer stock alone.
- The Question: If standard deviations just added, diversification couldn't work. Why don't they?
- Core idea: Portfolio variance picks up a cross-term: $\sigma_p^2 = w_1^2\sigma_1^2 + w_2^2\sigma_2^2 + 2w_1w_2\rho\sigma_1\sigma_2$. When ρ < 1, the cross-term is smaller than it would be if assets moved in lockstep, so portfolio variance is strictly less than the square of the weighted-average standard deviation. Risk does not add — variances add (and even then only for independent assets). It is low correlation, not the count of holdings, that does the work.
- Visual object: Curve of portfolio standard deviation versus correlation ρ, from ρ = +1 (23%, no benefit) down through ρ = 0.2 (18.1%) to ρ = −1 (5%), with the naive "weighted-average" dashed reference line shown above.
- Manim move: trace (slide ρ from +1 to −1, watching σ_p fall below the dashed reference; annotate the three marked points)
- Example seed: σ₁ = 18%, σ₂ = 28%, 50/50. At ρ = +0.9: σ_p ≈ 22.4% — almost no gain. At ρ = 0.2: σ_p ≈ 18.1% — portfolio is safer than the safer asset alone. At ρ = −0.5: σ_p ≈ 12.3%. Same expected return throughout.
- Length band: 3–5 min
- Still lanes: geo
- Prerequisites: Variance and standard deviation as risk measures (Ch. 7); weighted average
- Exclusions: Efficient frontier optimization (computational finance), estimation risk, crisis correlation spikes — name as caveats but don't derive
- Score: 10/10

---

## Candidate 03 — The Prisoner's Dilemma Is Not a Story, It's an Equation
- Source: `mba-math/chapters/12-matrices-linear-programming-and-game-theory.md`
- Topic: MBA MATH
- Hook: Four detergent companies could have each earned $50M by holding a high price. They all chose a strategy that left them at $20M — and it was the rational thing to do.
- Key case: Two-firm, High/Low pricing game: (High, High) = (50, 50); (Low, Low) = (20, 20); but "Low" is dominant for each firm regardless of what the rival does. Nash equilibrium is (Low, Low). The cartel outcome requires an illegal agreement precisely because the math shows (High, High) is unstable.
- The Question: How can a choice that is best for every individual produce a result that is worst for everyone collectively?
- Core idea: A dominant strategy is an action that yields a higher payoff than any alternative — no matter what the opponent does. When both players have a dominant strategy and those strategies conflict with the jointly optimal outcome, the Nash equilibrium is the dominant-strategy cell, not the collectively best cell. The gap is structural, not a failure of goodwill; it can only be closed by a binding commitment device (a contract, repeated-game punishment, or in the real case, an illegal cartel).
- Visual object: 2×2 payoff matrix with arrows tracing each firm's best-response to each opponent action, both arrows pointing to (Low, Low), with the (High, High) = (50, 50) cell circled as "jointly best but unstable."
- Manim move: split (reveal matrix cells one row at a time, animate dominance arrows, then highlight the Nash cell and the Pareto-superior cell to show the gap)
- Example seed: Firm A: if B plays High → A gets 50 (High) or 80 (Low) → choose Low. If B plays Low → A gets 10 (High) or 20 (Low) → choose Low. Low dominates. Same logic for B. Both land at (20, 20). Both prefer (50, 50). No unilateral defection from (20, 20) helps either player.
- Length band: 3–5 min
- Still lanes: geo
- Prerequisites: Basic payoff reasoning; no prior game theory required
- Exclusions: Mixed strategies, repeated games, OPEC dynamics — mention as extensions but don't derive
- Score: 10/10

---

## Candidate 04 — Why Positive Test Results Are Usually Wrong
- Source: `mba-math/chapters/13-decision-analysis-trees-expected-utility-and-bayes.md`
- Topic: MBA MATH
- Hook: A fraud test that catches 90% of cheaters flags your supplier. Most people say "90% chance they're fraudulent." The real answer is about 15%.
- Key case: Base rate of fraud = 1%. Test sensitivity 90%, false-positive rate 5%. Of 1,000 firms: 10 fraudulent → 9 flagged; 990 clean → ~50 falsely flagged. Of 59 total flagged, only 9 are actually fraudulent. P(fraud | flag) ≈ 15%, not 90%.
- The Question: Why does a highly accurate test produce mostly false positives?
- Core idea: The posterior probability depends on both the test's accuracy and the base rate of the condition. When the condition is rare, the flood of false positives from the large clean population dwarfs the true positives from the small affected group — even for a very accurate test. People report P(flag | fraud) and call it P(fraud | flag): the prosecutor's fallacy is a conditional-probability reversal, corrected exactly by Bayes' rule.
- Visual object: Natural-frequency tree: 1,000 firms → 10 fraudulent (9 flagged, 1 missed) + 990 clean (~50 falsely flagged, 940 cleared). Box showing "of 59 flagged → only 9 are real."
- Manim move: split (branch the 1,000 firms, then annotate the flagged-box counts to build up the fraction)
- Example seed: 1,000 firms. 10 fraudulent: test flags 9. 990 clean: test falsely flags 50. Total flagged: 59. True positives: 9. P(fraud | flagged) = 9/59 ≈ 15%. The test is accurate; the base rate is the culprit.
- Length band: 2–3 min
- Still lanes: geo
- Prerequisites: Conditional probability as a concept; no formula required — the video derives from counting
- Exclusions: Full Bayes formula derivation, Bayesian updating over multiple rounds, subjective priors — name the formula at the end but derive the result from counting
- Score: 10/10

---

## Candidate 05 — Why the Higher IRR Project Is Usually the Wrong Choice
- Source: `mba-math/chapters/05-dcf-npv-irr-and-valuation.md`
- Topic: MBA MATH
- Hook: Project A creates $8.4M of value at a 19% return. Project B creates $5.1M at a 24% return. IRR says take B. You should take A.
- Key case: Two mutually exclusive projects at a 9% hurdle rate. Big project: NPV $8.4M, IRR 19%. Small project: NPV $5.1M, IRR 24%. IRR ranks Small first; NPV ranks Big first. The goal is to create wealth in dollars, not maximize a percentage on a small base.
- The Question: Why does the project with the higher percentage return sometimes create less value?
- Core idea: IRR is the root of a polynomial in the discount rate — it is scale-blind, a percentage on whatever base the project happens to have. A small project can earn a high percentage and still generate fewer dollars than a large project with a lower percentage. NPV measures dollars of value created and is the correct tiebreaker. The conflict has nothing to do with reinvestment assumptions (a documented myth); it is purely about scale. Additionally, a project with multiple sign changes in its cash flows can have multiple IRRs — or none — because it is a higher-degree polynomial.
- Visual object: Two downward-sloping NPV profile curves (NPV vs. discount rate): Big project crosses zero at 19%, Small at 24%, but at the 9% hurdle Big has higher NPV. The crossover rate where they intersect is marked.
- Manim move: trace (draw both NPV curves sliding from r=0 down to the x-axis, then drop a vertical line at r=9% to show which NPV is higher)
- Example seed: At r = 0%: Big NPV > Small NPV (Big is larger in dollar terms). As r rises, both NPVs fall. Big's NPV hits zero at 19%, Small's at 24%. At r = 9% (the hurdle): Big NPV = $8.4M, Small NPV = $5.1M. IRR rule picks Small; NPV rule picks Big.
- Length band: 3–5 min
- Still lanes: geo
- Prerequisites: What NPV is (discounted sum); what a discount rate means
- Exclusions: Multiple-IRR pathology derivation (mention Descartes' Rule but don't derive), MIRR, bond/equity valuation — save for other cards
- Score: 9/10

---

## Candidate 06 — The Infinite Game with a Finite Price
- Source: `mba-math/chapters/07-probability-and-expected-value.md`
- Topic: MBA MATH
- Hook: A coin-flip game has an infinite expected payout. Nobody will pay $20 to play.
- Key case: St. Petersburg paradox. Flip until heads: win $2^k if heads first appears on flip k. Each term of the expected value is $(1/2)^k \times 2^k = 1$. Sum = $\infty$. Yet a rational price is under $20.
- The Question: If the expected value is infinite, why is the rational price lunch money?
- Core idea: Expected monetary value is the probability-weighted average of dollar outcomes — but people value the *usefulness* of money, not its raw amount. Each additional dollar is worth a little less than the one before (diminishing marginal utility). The expected *utility* of the St. Petersburg game is finite and modest under any concave utility function. This is the founding argument that a rational agent maximizes expected utility, not expected money — and the cleanest proof that EV alone is insufficient as a decision rule.
- Visual object: Number line of payoffs $2, $4, $8, …, $1M, …, each weighted by its vanishingly small probability, summing to ∞ — then a concave utility curve showing that the utility of each extra dollar shrinks, making the expected utility finite.
- Manim move: accumulate (stack the infinite EV terms, then morph to the utility-of-wealth curve showing the squashing)
- Example seed: k=1: win $2 with prob 1/2. k=2: win $4 with prob 1/4. Each term = $1. Sum diverges. But utility of $2^k under log utility = k × ln 2; weighted by (1/2)^k, the sum converges. Certainty equivalent under log utility ≈ $2. The math is exact; the decision is finite.
- Length band: 2–3 min
- Still lanes: geo
- Prerequisites: Expected value as probability-weighted average; notion of diminishing returns
- Exclusions: von Neumann-Morgenstern axioms, Allais paradox, prospect theory — name the resolution but don't formalize utility axioms
- Score: 9/10

---

## Candidate 07 — Options Price Without Knowing the Direction
- Source: `mba-math/chapters/14-quantitative-finance-returns-volatility-options-monte-carlo.md`
- Topic: MBA MATH
- Hook: An option's price is set by math that never asks whether you think the stock will go up or down. The direction forecast is completely irrelevant.
- Key case: Put–call parity: Portfolio A (call + cash $Ke^{−rT}) and Portfolio B (put + stock) pay identically at expiration in every scenario — whether the stock ends above or below the strike. No probabilities enter. The price relationship C − P = S − Ke^{−rT} is forced by no-arbitrage, not by any forecast.
- The Question: How can a contract's price be determined without knowing where the price is going?
- Core idea: In every possible future state, two specific portfolios produce identical payoffs — so they must cost the same today or a riskless profit is available. The replication/no-arbitrage argument replaces forecasting: what matters is not *where* the stock goes but *how much it can move* (volatility) and the cost of carrying the replicating position. The option price is an arbitrage identity; its only non-observable input is volatility, not direction.
- Visual object: Side-by-side payoff diagrams for Portfolio A and Portfolio B at expiration, showing they are identical for S > K and S ≤ K — then the identity C − P = S − Ke^{−rT} emerging.
- Manim move: split (build Portfolio A payoff and Portfolio B payoff in parallel panels, then collapse them to show equality)
- Example seed: Strike K = $100. If S_T = $120: Portfolio A = (120−100) + 100 = $120; Portfolio B = 0 + 120 = $120. If S_T = $80: Portfolio A = 0 + 100 = $100; Portfolio B = (100−80) + 80 = $100. Always equal → same price today. No forecast used.
- Length band: 3–5 min
- Still lanes: geo
- Prerequisites: What a call and put option are (kink payoffs); present value discounting
- Exclusions: Black–Scholes formula derivation, stochastic calculus, implied volatility surface — mention BS exists but don't derive
- Score: 9/10

---

## Candidate 08 — Arithmetic Mean vs. Geometric Mean: The Return That Feels Good But Lies
- Source: `mba-math/chapters/01-percentages-ratios-and-growth-rates.md`
- Topic: MBA MATH
- Hook: An investment returns +50% one year, −50% the next. The average return is 0%. The investor lost 25% of their money.
- Key case: $100 → $150 → $75. Arithmetic average of returns: (50% − 50%)/2 = 0%. Geometric mean (CAGR): (75/100)^(1/2) − 1 = −13.4%/year. The arithmetic mean answers "what return would I expect in a typical single year?"; the geometric mean answers "what did I actually earn over the holding period?" The gap grows with volatility.
- The Question: Why does the average reported return overstate what an investor actually earned?
- Core idea: Returns compound (multiply), so the right "average" over multiple periods is the geometric mean — the single constant rate that, compounded, replicates the actual path. The arithmetic mean adds the rates without accounting for the base-change between periods (the cross-term again). The two are equal only when all period returns are identical; otherwise arithmetic ≥ geometric, and the gap grows with the variance of returns. Reporting arithmetic averages of volatile returns as if they were realized growth is the same $(1+a)(1+b)$ error from Candidate 01, now dressed in fund-performance language.
- Visual object: Bar chart: Year 1 $100→$150, Year 2 $150→$75. Arithmetic mean = 0% (shown as a flat line). Geometric mean = −13.4%/year (shown as a declining compound curve through both actual endpoints).
- Manim move: compare (place arithmetic average path next to geometric/actual path, showing the divergence growing with volatility)
- Example seed: $100 invested. Year 1: +50% → $150. Year 2: −50% → $75. Arithmetic: (0.5 − 0.5)/2 = 0. Geometric: (75/100)^0.5 − 1 ≈ −0.134. The investor is down $25 while the arithmetic average reports "breaking even."
- Length band: 2–3 min
- Still lanes: geo
- Prerequisites: Percentages as multipliers (Candidate 01 is a natural prerequisite); basic compounding
- Exclusions: CAGR derivation, Fisher equation, nominal vs. real — covered in Candidate 01 or elsewhere
- Score: 9/10

---

## Candidate 09 — CAPM: The Risk That Earns Nothing
- Source: `mba-math/chapters/06-cost-of-capital-capm-and-wacc.md`
- Topic: MBA MATH
- Hook: A stock that swings wildly might earn you no extra return at all — if those swings have nothing to do with the market.
- Key case: Beta measures only the portion of a stock's variance that moves with the market. A wildly volatile stock with near-zero correlation to the market has a low beta → low expected return. All its noise is idiosyncratic and diversifiable; no investor needs to be compensated for it because they can make it disappear.
- The Question: Why does total volatility fail to predict expected returns, while only market co-movement does?
- Core idea: CAPM says expected return = risk-free rate + β × (equity risk premium). Beta is Cov(R_i, R_m)/Var(R_m) — the slope of the regression of the stock's returns on the market's. It captures only the undiversifiable, market-linked risk. Idiosyncratic risk washes out in a diversified portfolio (Ch. 10's diversification limit). Because any investor can diversify for free, they will not pay a premium to hold idiosyncratic risk — they'll just combine it with other things until it disappears. Compensation is for the exposure that survives diversification: beta, the market co-movement.
- Visual object: Security Market Line: expected return on y-axis, β on x-axis, intercept at r_f = 4.2%, slope = 5% equity risk premium. A high-volatility, low-β stock plotted below a low-volatility, high-β stock — with the high-volatility one demanding a lower expected return.
- Manim move: scan (draw the SML line, then place two stocks — one high-σ/low-β, one low-σ/high-β — showing that the y-position is determined by β, not by total volatility)
- Example seed: Stock A: σ = 40%, β = 0.3. Expected return = 4.2% + 0.3 × 5% = 5.7%. Stock B: σ = 15%, β = 1.4. Expected return = 4.2% + 1.4 × 5% = 11.2%. Stock A is more than twice as volatile but demands far less compensation — because its volatility is idiosyncratic.
- Length band: 3–5 min
- Still lanes: geo
- Prerequisites: Variance and standard deviation (Ch. 7); diversification intuition (Ch. 10 Candidate 02 is natural complement)
- Exclusions: WACC construction, full equity premium debate, Fama-French factors — mention limits of CAPM but don't derive alternatives
- Score: 9/10

---

## Candidate 10 — Volatility Doesn't Scale the Way You Think
- Source: `mba-math/chapters/14-quantitative-finance-returns-volatility-options-monte-carlo.md`
- Topic: MBA MATH
- Hook: A stock has 1% daily volatility. A careless analyst says annual volatility is 252%. The correct answer is about 16%. The error is a factor of sixteen.
- Key case: Daily σ = 1%. Annual variance = 252 × (0.01)² = 0.0252. Annual σ = √0.0252 ≈ 15.9%. The naive multiplication (1% × 252 = 252%) ignores that variance — not standard deviation — is the additive quantity under independence.
- The Question: Why do you multiply volatility by √252, not 252, to annualize it?
- Core idea: If daily returns are i.i.d., the variance of the annual return (sum of 252 daily returns) is 252 × σ_daily². Variance is additive; standard deviation is not. Annual standard deviation = √(252 × σ_daily²) = √252 × σ_daily ≈ 15.87 × σ_daily. This is the same "variances add, standard deviations don't" law from Ch. 7, now applied to time: uncertainty grows with the square root of time, not linearly. Bachelier derived this for price uncertainty in 1900; it underpins every VaR report and risk horizon calculation in finance.
- Visual object: Fan diagram: simulated price paths spreading from a single point, with ±1σ√t and ±2σ√t envelopes widening as the square root of time — a sideways parabola, not a V-shape.
- Manim move: spread (paths fan out from a starting price, the envelope grows as √t — annotate at 1, 4, 9, 16 time-steps to show the √t progression)
- Example seed: Daily σ = 1%. 1 day: uncertainty ±1%. 4 days: ±2% (×√4). 9 days: ±3% (×√9). 252 days (1 year): ±15.87% (×√252). The naive "×252" would give ±252% — a stock can't lose 252% of its value.
- Length band: 2–3 min
- Still lanes: geo
- Prerequisites: Variance and standard deviation (Ch. 7); the rule that variances of independent variables add
- Exclusions: Geometric Brownian motion derivation, stochastic calculus, volatility clustering (name as caveat) — keep to the √t scaling law and its derivation
- Score: 9/10

---

## Candidate 11 — The p-Value Is Not the Probability You Think It Is
- Source: `mba-math/chapters/08-statistics-description-sampling-and-inference.md`
- Topic: MBA MATH
- Hook: "There's only a 4% chance this is due to chance." Almost every word of that sentence is wrong.
- Key case: A/B test: Variant B converts 12.1% vs. Variant A's 11.8%. The team reports p = 0.04 and says "only 4% chance this is due to chance." The p-value is actually P(data this extreme | H₀ true) — not P(H₀ true | data). The conditional is reversed. The 4% is the probability of seeing this gap or larger *if the pages were identical* — it says nothing about the probability that the null is true.
- The Question: What does a p-value actually measure — and what does it definitely not measure?
- Core idea: The p-value is a tail area under the null distribution — the probability of data at least as extreme as observed, *given* the null hypothesis is true. It is a conditional probability P(data | H₀). The claim "4% chance this is due to chance" silently reverses the conditional to P(H₀ | data) — which the p-value cannot supply. Additionally, at large sample sizes (n = 5M), a 0.3-percentage-point lift that is too small to act on becomes wildly statistically significant: significance and practical importance come completely apart. The ASA's six principles make this explicit.
- Visual object: Bell curve centered on zero (the null distribution), with the observed test statistic marked at z = 0.58 sitting deep inside — showing the tail area (p ≈ 0.56) is large, result is noise; then a second needle-thin bell at n = 5M where the same 0.3-point lift lands at z = 15.
- Manim move: compare (wide null bell → mark observed z → shade tail; then shrink the bell as n grows until the same tiny effect becomes "significant")
- Example seed: 8,000 visitors per variant. Lift = 0.3 pp. SE_diff ≈ 0.00514. z = 0.003/0.00514 ≈ 0.58. p ≈ 0.56 — not significant at all. Scale to n = 5M: same lift, z ≈ 15. Now wildly "significant" — yet still only 0.3 percentage points.
- Length band: 3–5 min
- Still lanes: geo
- Prerequisites: Basic notion of probability; sampling variability
- Exclusions: Confidence interval construction, power analysis, Type I/II error algebra — name them but don't derive
- Score: 9/10

---

## Candidate 12 — Revenue Peaks at Unit Elasticity (and Netflix Knew It)
- Source: `mba-math/chapters/11-calculus-for-business-marginal-elasticity-optimization.md`
- Topic: MBA MATH
- Hook: Netflix raised prices 60%, lost 800,000 subscribers, and made more money. The math told them exactly which direction was uphill before a single customer quit.
- Key case: Price elasticity of demand ε. When |ε| < 1 (inelastic), a price hike raises revenue. When |ε| > 1 (elastic), it lowers revenue. Revenue is maximized at exactly unit elasticity (|ε| = 1). Netflix's streaming service was in inelastic territory; the subscriber losses were the known cost of moving toward the revenue peak.
- The Question: When does raising your price actually make you more money — and when does it make you less?
- Core idea: Revenue R = P × Q. As price rises, quantity falls along the demand curve. Whether revenue rises or falls depends on which effect dominates — the price increase or the quantity loss. The price elasticity of demand ε = (dQ/Q)/(dP/P) captures the trade-off. MR = P(1 + 1/ε). When |ε| > 1, MR > 0: sell more and you gain. When |ε| < 1, MR < 0: you're past the peak, each unit sold at lower price is a loss. Set MR = 0 to find the revenue-maximizing price: that is the unit-elasticity point.
- Visual object: Linear demand curve with upper half labeled "elastic" and lower half "inelastic"; below it, the total revenue parabola peaking at the unit-elastic midpoint.
- Manim move: trace (walk along the demand curve from top to bottom, watching the revenue parabola rise then fall beneath it — mark the unit-elasticity peak)
- Example seed: Demand P = 100 − 2Q. MR = 100 − 4Q. Set MR = 0: Q = 25, P = 50. Revenue = $1,250. At Q = 20 (higher price P = 60): R = $1,200. At Q = 30 (lower price P = 40): R = $1,200. Peak is at Q = 25. The Netflix raise moved them along an inelastic segment toward this peak.
- Length band: 3–5 min
- Still lanes: geo
- Prerequisites: What a demand curve is; basic notion of revenue as P × Q
- Exclusions: MR = MC optimization (a separate card), Lagrange multiplier, second-order conditions — the video stops at the revenue-elasticity relationship
- Score: 9/10

---

## Candidate 13 — The Perpetuity That Pays Forever Is Worth a Finite Number
- Source: `mba-math/chapters/04-time-value-of-money.md`
- Topic: MBA MATH
- Hook: A stream of payments that goes on forever — $1,000 every year until the end of time — is worth exactly $20,000 today. Finite, despite being infinite.
- Key case: Perpetuity at r = 5%: PV = C/r = $1,000/0.05 = $20,000. The discount factor 1/(1+r)^n → 0 as n → ∞, so distant payments are worth essentially nothing today. The infinite sum converges.
- The Question: How can an infinite stream of payments have a finite present value?
- Core idea: The annuity formula PV = C × [1 − (1+r)^{−n}]/r as n → ∞: the term (1+r)^{−n} → 0 because each extra year's payment is discounted by another factor of 1/(1+r) < 1. The geometric series converges. The deeper insight: doubling the discount rate halves the present value of a perpetuity (C/r doubles if r halves). And for the growing perpetuity C/(r−g): if g approaches r from below, the value shoots toward infinity — a fragility that matters enormously in stock valuation.
- Visual object: Bar chart showing annual $1,000 payments diminishing in present-value terms: year 1 ≈ $952, year 10 ≈ $614, year 30 ≈ $231, year 50 ≈ $87 — stacking to $20,000 total despite the bars going on forever.
- Manim move: accumulate (stack discounted bars one at a time, bars shrinking as n grows, total converging to C/r = $20,000 with a horizontal asymptote)
- Example seed: r = 5%, C = $1,000/year. PV = $1,000/0.05 = $20,000. Check: year 10 payment worth $1,000/1.05^10 = $614. Year 50 worth $87. Year 100 worth $7.60. All future payments beyond year 50 combined contribute less than $2,400 — only 12% of the total.
- Length band: 2–3 min
- Still lanes: geo
- Prerequisites: Present value discounting; compound growth factor (1+r)^n
- Exclusions: Annuity derivation, growing perpetuity fragility (mention only), amortization schedule
- Score: 8/10

---

## Candidate 14 — Same ROE, Different Risk: The DuPont Trap
- Source: `mba-math/chapters/03-financial-statement-math.md`
- Topic: MBA MATH
- Hook: Two firms both report 25% ROE. One will survive a recession; the other will collapse. The number is identical. The businesses are opposites.
- Key case: Firm A: net margin 10%, asset turnover 1.0×, equity multiplier 2.5× → ROE = 25% (via leverage). Firm B: net margin 12.5%, asset turnover 2.0×, equity multiplier 1.0× → ROE = 25% (via operations). In a downturn, Firm A's interest payments are fixed while margins compress — the same leverage that lifted ROE amplifies losses. Firm B's low leverage means losses absorb into margins, not debt service.
- The Question: How can the same ROE signal two completely different levels of fragility?
- Core idea: ROE = Net Income / Equity = (NI/Sales) × (Sales/Assets) × (Assets/Equity). The DuPont identity — multiply by 1 twice in useful disguises — splits ROE into three independent drivers: profitability, efficiency, and leverage. Identical ROE can be manufactured by any combination of the three. Only by decomposing it can you tell whether the ROE is durable (earned through operations) or fragile (borrowed from future stress). The algebra is exact; the risk diagnosis is the analyst's.
- Visual object: Flow diagram: one ROE box splitting into three driver boxes (margin × turnover × multiplier), with two firms shown arriving at 25% via different paths — Firm A's high-multiplier path highlighted in red as "fragile leverage."
- Manim move: split (ROE box splits into three factors; then two firms' values fill in, both multiplying to 25% — with Firm A's multiplier flashing red)
- Example seed: Firm A: NI = $25M, Sales = $250M, Assets = $250M, Equity = $100M. Margin = 10%, Turnover = 1.0, Multiplier = 2.5. ROE = 25%. Firm B: NI = $25M, Sales = $200M, Assets = $100M, Equity = $100M. Margin = 12.5%, Turnover = 2.0, Multiplier = 1.0. ROE = 25%. Remove the leverage from Firm A and its ROE falls to 10%. Firm B's holds.
- Length band: 2–3 min
- Still lanes: geo
- Prerequisites: What ROE is; basic ratio intuition
- Exclusions: Full ratio taxonomy, amortization, DDB depreciation — this card covers only DuPont
- Score: 8/10
