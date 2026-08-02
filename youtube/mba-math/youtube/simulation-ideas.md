# MBA Math — Simulation Ideas

## Candidate 01 — Portfolio Risk vs. Correlation: the Cross-Term Does Everything
- Source: `mba-math/chapters/10-risk-correlation-and-portfolio-math.md`
- Topic: Two-Asset Portfolio Variance — σ_p as a Function of Correlation ρ
- Lane: MANIM (directed animation)
- Hook: Two assets, σ₁ = 18%, σ₂ = 28%, held 50/50. Most people guess the portfolio risk is the weighted average: 23%. The math gives 22.4% at ρ = 0.9, 18.1% at ρ = 0.2, and 12.3% at ρ = −0.5. The same two stocks span a twelve-point range of risk based entirely on one number.
- The rule: σ_p² = w₁²σ₁² + w₂²σ₂² + 2w₁w₂ρσ₁σ₂. As ρ slides from +1 to −1, the cross-term drives σ_p from the weighted average (23%) down toward zero. At ρ = +1: no benefit; at ρ = 0: σ_p = σ/√2; at ρ = −1: σ_p = 0.
- Concrete numbers: σ₁ = 18%, σ₂ = 28%, w₁ = w₂ = 0.5. ρ = +1: σ_p = 23.0% (weighted average). ρ = +0.9: σ_p² = 81 + 196 + 226.8 = 503.8, σ_p = 22.4%. ρ = 0.2: σ_p² = 81 + 196 + 50.4 = 327.4, σ_p = 18.1% (below the safer stock). ρ = −0.5: σ_p² = 81 + 196 − 126 = 151, σ_p = 12.3%.
- The artifact / what moves: A Cartesian plane with ρ on the x-axis (from −1 to +1) and σ_p on the y-axis (from 0% to 28%). The curve σ_p(ρ) = √(w₁²σ₁² + w₂²σ₂² + 2w₁w₂ρσ₁σ₂) is traced as ρ animates from +1 to −1. A dashed horizontal line marks the weighted-average of 23% — the intuitive wrong answer. The curve passes through 23% only at ρ = +1, dips below the safer asset (18%) around ρ = 0.2, and reaches 5% at ρ = −1. Four labeled dots appear at the four values computed above. A running label shows the live σ_p value.
- Output medium: Manim (mp4)
- Two testable predictions: P1: At ρ = 0.2, σ_p² = 0.25(324) + 0.25(784) + 2(0.25)(0.2)(18)(28) = 81 + 196 + 50.4 = 327.4, so σ_p = 18.09% — the portfolio is *less risky than the safer asset alone* (18%), verifiable by arithmetic. P2: The curve σ_p(ρ) is a concave function of ρ that achieves its minimum at ρ = −1. At ρ = −1 exactly: σ_p = |w₁σ₁ − w₂σ₂| = |0.5×18 − 0.5×28| = 5.0% — the floor, verifiable from the formula.
- The change: Double the weight in the riskier asset to w₁ = 0.3, w₂ = 0.7. The curve shifts upward (higher minimum σ_p) but retains the same shape — the ρ = −1 floor is now |0.3×18 − 0.7×28| = |5.4 − 19.6| = 14.2%. The weighted-average trap also shifts. The core insight is unchanged: correlation, not asset count, drives the benefit.
- Human supplies (Claude can't): Nothing — fully analytic/synthetic
- Teardown angle: Every beginner thinks "portfolio risk = weighted average of risks." This is wrong whenever ρ < 1, which is always. The whole Markowitz revolution fits in one curve on one plot.
- Exclusions: Do not show the efficient frontier optimization. Do not animate the N-asset diversification limit. Stay on the two-asset formula and the ρ-axis.
- Sim slug: mba-portfolio-risk-vs-correlation
- Score: 10/10

## Candidate 02 — Discount Factor Collapse: Why Distant Cash Flows Are Nearly Worthless
- Source: `mba-math/chapters/04-time-value-of-money.md`
- Topic: Discount Factor 1/(1+r)^n Decay Over Time
- Lane: MANIM (directed animation)
- Hook: A dollar 30 years away at 10% is worth less than 6 cents today. The math is just one number raised to a power — but almost nobody has a visceral sense of how fast the collapse happens. Watching three discount curves fall in real time changes that.
- The rule: Discount factor = 1/(1+r)^n. At r = 4%: 0.308 at n = 30. At r = 7%: 0.131 at n = 30. At r = 10%: 0.057 at n = 30. A one-percentage-point increase in r at n = 30 can halve the present value of a distant cash flow.
- Concrete numbers: Three curves: r = 4%, 7%, 10%. At n = 1: 0.962, 0.935, 0.909. At n = 10: 0.676, 0.508, 0.386. At n = 20: 0.456, 0.258, 0.149. At n = 30: 0.308, 0.131, 0.057. A $1,000 payment at n = 30: worth $308 at 4%, $131 at 7%, $57 at 10%.
- The artifact / what moves: A coordinate frame: n (years, 0–30) on the x-axis, discount factor (0 to 1) on the y-axis. Three exponential decay curves — r = 4% (green), 7% (amber), 10% (red) — draw simultaneously from left to right. Each curve is labeled at the right endpoint with the final factor value. A vertical marker sweeps from n = 0 to n = 30; at each position a text label shows the three current discount factor values. At n = 30 the three endpoints (0.308, 0.131, 0.057) appear as labeled dots. A secondary panel shows what a $1,000 cash flow is worth at the current n and all three rates simultaneously.
- Output medium: Manim (mp4)
- Two testable predictions: P1: At r = 7% and n = 30, the discount factor is 1/(1.07)^30 = 1/7.612 = 0.1314. A $1,000 payment at n = 30 discounts to $131.40 — verifiable by hand on a calculator. P2: Moving from r = 7% to r = 10% at n = 30, the ratio of discount factors is 0.0573/0.1314 = 0.436 — a 56.4% reduction in present value from a 3-percentage-point rate increase. The sensitivity is compounding: a linear rate increase produces a super-linear reduction in PV at long horizons.
- The change: Hold r fixed at 7% and watch how sensitive PV is to n: at n = 5 the factor is 0.713 (still substantial); by n = 20 it is 0.258; by n = 50 it reaches 0.034. The animation illustrates that long-horizon projects are far more sensitive to the discount rate than near-term ones — which is why a 1% change in WACC can swing a long-horizon DCF valuation by 20–30%.
- Human supplies (Claude can't): Nothing — fully analytic/synthetic
- Teardown angle: Finance textbooks show a table of discount factors. This is the same data moving — and the visual makes the collapse intuitive in a way a static table cannot.
- Exclusions: Do not derive the annuity formula or growing perpetuity. Do not animate loan amortization. Show only the single-payment discount factor curve.
- Sim slug: mba-discount-factor-decay-over-time
- Score: 9/10

## Candidate 03 — Growing Perpetuity Explosion: the Denominator Trap (r − g)
- Source: `mba-math/chapters/04-time-value-of-money.md`
- Topic: Gordon Growth Model PV = C/(r − g) — Sensitivity as g Approaches r
- Lane: MANIM (directed animation)
- Hook: A startup's terminal value is estimated at C/(r − g) with r = 8% and g = 4%. Move g from 2% to 3% to 4%: the valuation goes from $33 to $50 to $100 — a tripling from a one-point assumption change nobody can pin down. The formula is fragile in a specific, computable way.
- The rule: PV = C/(r − g), valid only when r > g. As g → r, the denominator (r − g) → 0 and PV → ∞. The curve PV vs. g is a rectangular hyperbola — explosively sensitive near the singularity at g = r.
- Concrete numbers: C = $2 (next-period cash flow), r = 8%. PV at g = 2%: $2/(0.08 − 0.02) = $2/0.06 = $33.33. At g = 3%: $2/0.05 = $40.00. At g = 4%: $2/0.04 = $50.00. At g = 5%: $2/0.03 = $66.67. At g = 6%: $2/0.02 = $100.00. At g = 7%: $2/0.01 = $200.00. At g = 7.9%: $2/0.001 = $2,000.00.
- The artifact / what moves: A Cartesian frame with g (0% to 7.9%) on the x-axis and PV (0 to 500+) on the y-axis. A vertical dashed red line marks the singularity at g = r = 8% ("undefined / infinity"). The curve PV(g) = C/(r − g) is drawn from left to right, starting near flat (at g = 0, PV = C/r = 25) and curving up steeply as g approaches 8%. Labeled dots appear at g = 2%, 3%, 4%, 5%, 6%, 7%. An animated marker sweeps along the curve and a running label reads the live PV value. The curve accelerates — going vertical — near g = 7.9%.
- Output medium: Manim (mp4)
- Two testable predictions: P1: At g = 3%, PV = C/(r − g) = 2/(0.08 − 0.03) = 2/0.05 = $40.00 exactly. Moving g by one percentage point from 2% to 3% changes PV from $33.33 to $40.00, a 20% increase. Moving the next percentage point (3% to 4%) changes PV from $40 to $50, a 25% increase — the sensitivity *itself* is increasing as g rises. P2: The derivative dPV/dg = C/(r − g)² > 0 always — the curve is always increasing and always accelerating. At g = 6%, dPV/dg = 2/(0.02)² = 5,000 per 1% — meaning a 1-percentage-point move changes PV by ~$50, confirmed by the $100 − $66.67 = $33.33 discrete step shown in the animation.
- The change: Raise r from 8% to 10%. The singularity shifts right to g = r = 10%. The curve flattens and shifts down everywhere — at g = 2%, PV is now $2/0.08 = $25 instead of $33. The key property is unchanged: sensitivity explodes near the singularity.
- Human supplies (Claude can't): Nothing — fully analytic/synthetic
- Teardown angle: Every DCF with a terminal value uses this formula. The number it produces can double from a 1% change in g — a rate nobody can forecast. The formula is not wrong; it is fragile in a precise mathematical sense, and this animation shows exactly where and why.
- Exclusions: Do not derive the growing perpetuity formula from the geometric series on screen. Do not animate discount factor tables. Show only the PV(g) curve and its blowup near r.
- Sim slug: mba-growing-perpetuity-denominator-trap
- Score: 9/10

## Candidate 04 — Volatility Cone: Price Paths Spread as √t
- Source: `mba-math/chapters/14-quantitative-finance-returns-volatility-options-monte-carlo.md`
- Topic: √t Volatility Scaling — Price Uncertainty as a Function of Time
- Lane: MANIM (directed animation)
- Hook: Day 1, a stock could be anywhere within a 1% band. Day 10, the band is √10 ≈ 3.16% wide, not 10%. Day 100, the band is 10% wide, not 100%. Uncertainty grows with the square root of time — not linearly — and that single fact underlies all of options pricing.
- The rule: If daily log returns are i.i.d. with standard deviation σ_d, then the n-day standard deviation is σ_d × √n. Annual volatility = σ_daily × √252. A 1% daily vol annualizes to 1% × 15.87 ≈ 15.9%, not 252%.
- Concrete numbers: σ_daily = 1.5% (roughly mid-cap stock). σ(n) = 1.5% × √n. At n = 1: 1.5%. At n = 10: 4.74%. At n = 30: 8.22%. At n = 100: 15.0%. At n = 252: 23.8% (annual vol). ±2σ envelope: at n = 252, the stock could plausibly be anywhere from exp(−2 × 0.238) ≈ 0.62 to exp(+2 × 0.238) ≈ 1.61 times its starting value.
- The artifact / what moves: A coordinate frame: time n (days, 0–252) on the x-axis, price level on the y-axis, starting at $100. The ±1σ√t and ±2σ√t envelopes are drawn as curved bands spreading outward from $100. As time advances, the bands widen — not linearly but as parabolas rotated 90°. Faint gray Monte Carlo sample paths (10–20) fill the interior of the cone, illustrating individual outcomes. The ±2σ band widens from [$97, $103] at n = 1 to [$62, $161] at n = 252. A label on the right edge shows the current ±1σ and ±2σ boundaries and the effective annual volatility.
- Output medium: Manim (mp4)
- Two testable predictions: P1: The ±1σ boundary at n days is P₀ × exp(±σ_d√n). At n = 100, this is $100 × exp(±0.015 × 10) = $100 × exp(±0.15) ≈ [$86.07, $116.18] — the asymmetry of lognormal returns means the upper boundary is slightly further from $100 than the lower. P2: The ratio of the 252-day volatility to the 1-day volatility is exactly √252 ≈ 15.87. An analyst who multiplies by 252 instead of √252 would report 15.87× too large an annual vol (378% vs 23.8%), a mistake of a factor of 15.87 — visible in the animation by comparing the correct cone width to the absurd linear-scaling alternative.
- The change: Add a second, wider-vol stock (σ_daily = 3%) to the same frame. Its cone spreads faster — the bands are exactly 2× as wide at every n. The √t structure is the same; only the coefficient changes. This illustrates that σ_daily sets the cone's opening angle, while time sets the √t widening law.
- Human supplies (Claude can't): Monte Carlo random seeds (any seed works for illustration); no empirical data needed — all synthetic.
- Teardown angle: Every options pricing formula and every risk report runs on this law. The ±2σ cone is not a metaphor — it is the exact confidence interval for a geometric Brownian motion path.
- Exclusions: Do not derive the Black–Scholes formula. Do not show the implied volatility surface. Stay on the cone and the √t envelope.
- Sim slug: mba-volatility-cone-sqrt-t-scaling
- Score: 9/10

## Candidate 05 — Annuity Formula Convergence: Geometric Series Becoming the Perpetuity
- Source: `mba-math/chapters/04-time-value-of-money.md`
- Topic: Annuity Factor [1 − (1+r)^(−n)]/r Converging to 1/r as n → ∞
- Lane: MANIM (directed animation)
- Hook: A stream of $1,000 per year for 20 years at 5% is worth $12,462. For 50 years: $18,256. Forever: $20,000. Adding 30 more years of payments only adds $5,794 — because the discount factor crushes distant cash flows to nearly nothing. Watch the finite annuity creep toward the perpetuity cap.
- The rule: PV_annuity = C × [1 − (1+r)^(−n)]/r. As n → ∞, (1+r)^(−n) → 0 and PV → C/r (the perpetuity). The convergence is fast at high r and slow at low r.
- Concrete numbers: C = $1,000, r = 5%. PV_perp = $1,000/0.05 = $20,000. At n = 5: $4,329. n = 10: $7,722. n = 20: $12,462. n = 30: $15,373. n = 50: $18,256. n = 100: $19,848. n = ∞: $20,000. The perpetuity cap is reached at about 97% after 100 years.
- The artifact / what moves: A horizontal frame with n (years, 0 to 100) on the x-axis and PV (0 to $21,000) on the y-axis. A dashed red horizontal line marks the perpetuity value C/r = $20,000. The annuity PV curve [C × [1 − (1+r)^(−n)]/r] rises from 0 and asymptotically approaches the dashed line. At each labeled n (5, 10, 20, 30, 50, 100), a dot appears with the PV value. The gap between the curve and the $20,000 cap is shaded and labeled "remaining value of payments beyond year n." As n increases, the shaded gap closes — visibly at first, then imperceptibly.
- Output medium: Manim (mp4)
- Two testable predictions: P1: At n = 20 and r = 5%, PV = $1,000 × [1 − (1.05)^(−20)]/0.05 = $1,000 × [1 − 0.3769]/0.05 = $1,000 × 12.462 = $12,462. This is 62.3% of the $20,000 perpetuity value, verifiable by plugging numbers. P2: The convergence rate depends on r. At r = 10%, the perpetuity cap is $10,000; the annuity reaches 90% of that cap (i.e., $9,000) at n = log(10)/log(1.10) ≈ 24.2 years. At r = 5%, reaching 90% of $20,000 requires n = log(10)/log(1.05) ≈ 47.6 years — the lower rate means slower convergence, quantifiable and verifiable.
- The change: Switch r from 5% to 10%. The perpetuity cap halves from $20,000 to $10,000, but the curve reaches 90% of the cap twice as fast. This illustrates that high discount rates make the perpetuity a better approximation for shorter horizons — because distant cash flows are crushed more quickly.
- Human supplies (Claude can't): Nothing — fully analytic/synthetic
- Teardown angle: Perpetuity vs. annuity is a staple MBA trick question. This animation shows *why* they are often close: once you're past 30–50 years, the extra payments barely move the needle.
- Exclusions: Do not derive the geometric series formula on screen. Do not animate loan amortization schedules. Show only the annuity convergence curve approaching the perpetuity.
- Sim slug: mba-annuity-convergence-to-perpetuity
- Score: 8/10

## Candidate 06 — MR = MC: the Profit Peak Found by Setting a Derivative to Zero
- Source: `mba-math/chapters/11-calculus-for-business-marginal-elasticity-optimization.md`
- Topic: Profit Maximization — Marginal Revenue = Marginal Cost
- Lane: MANIM (directed animation)
- Hook: A firm can produce anywhere from 0 to 50 units. At too few units, each additional one earns more than it costs — so why stop? At too many, each additional one costs more than it earns — so why continue? There is exactly one output where the next unit is break-even. That is the profit maximum, and calculus finds it in one step.
- The rule: Profit π(q) = R(q) − C(q). Maximum where dπ/dq = 0, which gives dR/dq = dC/dq, i.e. MR = MC. For linear demand P = 100 − 2q and constant MC = 20: MR = 100 − 4q (same intercept as demand, twice the slope); MR = MC gives q* = 20. Profit: π(20) = (100×20 − 2×400) − 20×20 − 10 = 1200 − 800 − 400 − 10 = $790 (using C(q) = 20q + 10).
- Concrete numbers: Demand: P = 100 − 2q. Revenue: R = 100q − 2q². MR = dR/dq = 100 − 4q. Total cost: C(q) = 20q + 10. MC = dC/dq = 20 (constant). Intersection: 100 − 4q = 20 → q* = 20. Price: P* = 100 − 40 = $60. Profit: π* = $60×20 − $20×20 − $10 = $1200 − $400 − $10 = $790.
- The artifact / what moves: A two-panel animation. Top panel: MR curve (100 − 4q, downward-sloping) and MC line (horizontal at $20) on the same axes. An animated vertical line sweeps from q = 0 to q = 50. As it sweeps: a label shows the live gap MR − MC. When the sweep reaches q = 20, MR = MC exactly and the gap hits zero. A dot appears at the intersection. Bottom panel: the profit curve π(q) = R(q) − C(q). The animation shows the profit rising to a peak at q = 20 and falling after — the peak is labeled $790. The two panels animate simultaneously, so the viewer sees MR = MC in the top panel correspond to the profit peak in the bottom.
- Output medium: Manim (mp4)
- Two testable predictions: P1: At q = 15: MR = 100 − 60 = $40 > MC = $20. Profit is still rising (each extra unit adds $40 revenue for $20 cost). At q = 25: MR = 100 − 100 = $0 < MC = $20. Profit is falling. At q = 20 exactly: MR = $20 = MC. The profit curve is flat, verifiable by calculating π(19) = $789, π(20) = $790, π(21) = $789 — confirming the discrete peak. P2: The profit-maximizing price is $60, not $20. The markup above marginal cost (Lerner index) = (P − MC)/P = ($60 − $20)/$60 = 67%. For a linear demand curve with MC = constant, the markup is always 1/|ε| at the optimum — here |ε| at q* = 20 can be computed as (dQ/dP)(P/Q) = (1/2)(60/20) = 1.5, so markup = 1/1.5 = 67%, confirming both formulas agree.
- The change: Double marginal cost to MC = 40. The MC line rises; it intersects MR at a new q* = 15. Price rises to P = 100 − 30 = $70. Profit falls from $790 to a lower level. The viewer sees that a cost shock shifts the optimal output leftward and raises the price — the market response to a cost increase, derived from calculus.
- Human supplies (Claude can't): Nothing — fully analytic/synthetic
- Teardown angle: MR = MC is described verbally in every microeconomics course. This animation shows it as the condition that the tangent to the profit curve is horizontal — the same "flat top" that identifies any maximum. There is nothing mysterious; it is first-year calculus wearing an economics hat.
- Exclusions: Do not show the second-order condition derivation. Do not animate a downward-sloping MC curve. Keep demand linear and MC constant for clarity.
- Sim slug: mba-mr-mc-profit-maximum-calculus
- Score: 8/10

## Candidate 07 — Option Payoff Hockey Sticks: the Protective Put as a Floor
- Source: `mba-math/chapters/14-quantitative-finance-returns-volatility-options-monte-carlo.md`
- Topic: Option Payoffs — Call max(S−K,0), Put max(K−S,0), and Protective Put
- Lane: MANIM (directed animation)
- Hook: A straight stock position rises and falls one-for-one with the price. Add a put, and suddenly you have a floor: below the strike you are protected, above it you keep all the gain. The kink in the payoff diagram is the whole point of options — and it cannot be built from any combination of straight lines.
- The rule: Call payoff at expiration: max(S − K, 0). Put payoff: max(K − S, 0). Protective put (stock + put): max(S, K). At S > K: stock dominates, protective put = S. At S < K: put pays K − S, plus stock worth S, so total = K. The floor is locked at K.
- Concrete numbers: Strike K = $100. Stock only (bought at $100): linear — $80 stock = −$20 loss; $120 stock = +$20 gain. Put alone: at $80: pays $20; at $100: pays $0; at $120: pays $0. Protective put (stock + put, ignoring premium): at $80: value = $100 (floor); at $100: value = $100; at $120: value = $120.
- The artifact / what moves: Three panels drawn in sequence. Panel 1: the call payoff curve — flat at zero from S = 0 to K = 100, then rising at 45° above K. The kink at K is labeled. Panel 2: the put payoff curve — falling at 45° from left, kinking flat at zero at K = 100. Panel 3: the protective put (stock + put) — flat floor at $100 from S = 0 to K, then rising at 45° above K. A superimposed diagonal shows the raw stock P&L (rising through zero at S = $100). The difference between the protective put curve and the raw stock line is the insurance payoff — shown as a shaded region below K.
- Output medium: Manim (mp4)
- Two testable predictions: P1: At S_T = $70 (a 30% crash from K = $100), the put pays K − S = $100 − $70 = $30. Combined with the stock worth $70, the protective put is worth exactly $100 — the floor holds exactly. P2: Put–call parity: C − P = S − Ke^(−rT). With r = 5%, T = 1, K = $100, S = $100: C − P = 100 − 100e^(−0.05) ≈ 100 − 95.12 = $4.88. This is a model-free prediction — if any pricing model gives call and put prices that violate this, an arbitrage exists.
- The change: Move the strike K from $100 to $80 (a deeper out-of-the-money put). The floor drops to $80; the put is cheaper. Move K to $110 (in-the-money put): the floor rises to $110 but the put is more expensive. The tradeoff between the floor level and the premium — the "deductible" analogy — becomes visible as the kink slides left and right.
- Human supplies (Claude can't): Nothing — fully analytic/synthetic (payoffs are piecewise linear, no model needed)
- Teardown angle: Every options explainer draws hockey sticks. This animation draws them one at a time and combines them live — showing that the protective put is literally the sum of two curves, not a new concept.
- Exclusions: Do not animate the Black–Scholes formula or Monte Carlo paths. Do not show volatility. Show only the payoff at expiration.
- Sim slug: mba-option-payoff-hockey-stick-protective-put
- Score: 7/10
