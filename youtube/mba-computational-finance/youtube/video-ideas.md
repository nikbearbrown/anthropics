# MBA Computational Finance Video Ideas

## Candidate 01 — Why +50% Then −50% Leaves You Worse Off Than Zero
- Source: `mba-computational-finance/chapters/02-returns-and-risk-measurement.md`
- Topic: COMPUTATIONAL FINANCE
- Hook: A stock gains 50% one year and loses 50% the next — intuition says you break even, math says you lose 25%.
- Key case: $100 grows to $150 after year one, then falls to $75 after year two — a net loss of $25 on a two-year average return of zero.
- The Question: If the average of +50% and −50% is zero, the portfolio should be flat. It isn't — it is down 25%. Why does averaging returns lie about compounding?
- Core idea: Volatility drag — because returns compound multiplicatively, not additively, each down period must be made up from a smaller base, so the geometric mean is always below the arithmetic mean by approximately σ²/2; the more volatile the path, the deeper the permanent shortfall.
- Visual object: Two price paths with identical arithmetic averages diverging on a chart — the smooth path holds even, the volatile path falls behind
- Manim move: compare
- Example seed: A tech stock held by Priya swings +60%, −40%, +60%, −40% over four years. Arithmetic average: +10% per year. Actual ending value on $1,000: $1,000 × 1.6 × 0.6 × 1.6 × 0.6 = $921. Four years of positive "average" returns left her with less money.
- Length band: 2–3 min
- Still lanes: geo (two diverging price-path lines), geo (bar showing arithmetic vs geometric gap)
- Prerequisites: what a percentage return means, basic multiplication
- Exclusions: no log-return derivation or ln formula, no Itô's lemma, no continuous-compounding math, no discussion of skewness or kurtosis, no Kelly criterion
- Score: 10/10

---

## Candidate 02 — Why Adding a Risky Stock Can Make Your Portfolio Less Risky
- Source: `mba-computational-finance/chapters/08-the-diversification-miracle.md`
- Topic: COMPUTATIONAL FINANCE
- Hook: Adding a volatile stock to a portfolio can reduce total portfolio risk — even though the stock itself is riskier than what you already own.
- Key case: A 50/50 mix of Apple (28% vol) and Johnson & Johnson (16% vol) has lower volatility than either stock alone, because their correlation is only 0.30.
- The Question: JNJ is safer than Apple. Adding Apple to a JNJ-only portfolio should make it riskier. The math says the mix is calmer than JNJ alone. Why?
- Core idea: Portfolio variance has a cross-term: 2·w_A·w_B·ρ·σ_A·σ_B. When correlation ρ is below 1, this term is smaller than the variance contributions it supplements — so the combined variance falls below the weighted average of the individual variances. Low correlation does the work, not low individual volatility.
- Visual object: The two-asset variance formula with its cross-term highlighted, showing the cross-term shrink as ρ moves from +1 to 0 to −1
- Manim move: morph
- Example seed: Investor holds $10,000 entirely in a home-builder stock (35% vol). She adds $5,000 of a home-insurance stock (30% vol, ρ = −0.40 with the builder). New portfolio vol: √(0.67²×35² + 0.33²×30² + 2×0.67×0.33×(−0.40)×35×30) ≈ 21% — lower than either stock alone.
- Length band: 3–5 min
- Still lanes: geo (variance formula with cross-term box), geo (three-scenario correlation slider), c2v (yin-yang two-asset object)
- Prerequisites: what variance and standard deviation mean, basic portfolio weights
- Exclusions: no N-asset general formula, no efficient-frontier derivation, no matrix algebra, no Markowitz biography, no Evans-Archer 20-stock curve, no 60/40 portfolio discussion
- Score: 10/10

---

## Candidate 03 — Why an Option Price Has Nothing to Do With Your Forecast
- Source: `mba-computational-finance/chapters/07-options-and-derivatives.md`
- Topic: COMPUTATIONAL FINANCE
- Hook: The price of an option on a stock does not depend on whether you think the stock will go up or down — the probability of each outcome drops out of the math entirely.
- Key case: Stock at $100, can go to $120 or $80. A 60% chance of going up should make the call worth more than a 40% chance — but both probabilities give the same call price of $11.90.
- The Question: Higher probability of the stock rising should make a call option more valuable. Running the numbers with 60% or 10% up-probability gives the same answer. Why does the probability vanish?
- Core idea: Replication — you can construct a portfolio of stock and bonds whose payoff exactly matches the call's payoff in every future state (Δ = 0.5 shares, borrow $38.10). Two things with identical payoffs in every state must have the same price today; no-arbitrage forces a unique answer, and the probabilities are not needed to build the replicating portfolio.
- Visual object: One-step binomial tree with the replicating portfolio assembled beside it, payoffs matching in both branches
- Manim move: compare
- Example seed: A bakery owner wants to lock in the right to buy 1,000 lbs of flour at $2/lb in three months. The flour can go to $2.40 or $1.60. Replicating portfolio: long 0.5 units of flour futures, borrow $0.76 at the risk-free rate. Portfolio cost = $0.24 per lb of coverage — no one needed to estimate whether flour prices will rise.
- Length band: 3–5 min
- Still lanes: geo (binomial tree with two branches labeled), geo (replicating-portfolio construction step by step)
- Prerequisites: what a call option payoff is (max(S−K, 0)), the concept of arbitrage
- Exclusions: no Black-Scholes formula derivation, no Greeks, no implied volatility, no put-call parity proof, no continuous-time limit or Brownian motion, no option chain reading
- Score: 9/10

---

## Candidate 04 — Why a 29% Drop Triggers Your Margin Call, Not a 50% Drop
- Source: `mba-computational-finance/chapters/06-margin-and-short-selling.md`
- Topic: COMPUTATIONAL FINANCE
- Hook: You put up 50% margin — most investors assume they're safe until the stock drops 50%. The call arrives after a 29% drop.
- Key case: Buy 100 shares at $100 with 50% initial margin: $5,000 yours, $5,000 borrowed. Maintenance margin 30%. The margin call fires at $71.43 — a 28.6% decline, not 50%.
- The Question: With 50% margin you should be insulated until the stock falls 50%. The call fires at 29%. Why does the cushion vanish so fast?
- Core idea: The broker's loan is fixed in dollar terms — it stays at $5,000 while the stock price falls. Your equity is the gap between the shrinking position value and the fixed loan, so it falls twice as fast as the stock; a 28.6% drop in the stock wipes out 57% of your equity, pushing equity-to-position below the 30% maintenance threshold.
- Visual object: A balance sheet with "loan" frozen and "position value" shrinking, showing equity collapse faster than the stock price
- Manim move: compare
- Example seed: Sam buys 200 shares of a solar company at $80 (initial margin 50%, maintenance 30%). Loan: $8,000. Margin call trigger = $8,000 / (200 × 0.70) = $57.14. Solar stocks drop 29% in a week. Sam's account: position value $11,428, equity $3,428, margin % = 30%. The call fires. An unlevered investor sits calmly — same 29% loss, no deadline.
- Length band: 2–3 min
- Still lanes: geo (balance-sheet animation with frozen loan bar), geo (two-column timeline: levered vs. unlevered investor path)
- Prerequisites: what a margin account is (borrowed money against stock collateral), percentage arithmetic
- Exclusions: no short-selling mechanics in this film, no interest-rate calculation on the loan, no GameStop or LTCM narrative, no leveraged ETF volatility-decay discussion, no Regulation T details
- Score: 9/10

---

## Candidate 05 — Why a Bond Issued by Apple Can Lose 11% Even If Apple Never Defaults
- Source: `mba-computational-finance/chapters/03-equity-and-fixed-income.md`
- Topic: COMPUTATIONAL FINANCE
- Hook: An Apple bond — zero default risk — can lose 11% of its value in a single interest-rate move, with the contract never broken.
- Key case: Apple's 2.95% bond due 2049, rated impeccable, drops from $707 to roughly $625 per $1,000 face when long yields rise 1 percentage point — because the bond's 16-year duration means each 1% rate rise costs about 16% of price.
- The Question: Apple will certainly pay every coupon and return every dollar at maturity. The bond should be safe. But a 1% rate rise causes an 11% price loss. How can a bond lose money if nothing in the contract broke?
- Core idea: Bond price is the present value of future cash flows; when the discount rate rises, the same cash flows are worth less today. The further the cash flows are in the future (duration), the more sensitive the price — a 1% rate rise reduces a 16-year-duration bond's price by about 16%, all without the issuer missing a payment.
- Visual object: A present-value timeline — rows of coupon arrows shrinking as the discount rate rises, with the sum (price) visibly falling
- Manim move: decay
- Example seed: A teacher's pension fund holds $100,000 face of a 3% 20-year government bond priced at par. Interest rates rise 1.5%. Duration 14 years. Price falls by 14 × 1.5% ≈ 21%. Fund value: $79,000. The government never missed a payment.
- Length band: 2–3 min
- Still lanes: geo (present-value timeline with discount arrows), geo (price-vs-yield curve showing the inverse relationship)
- Prerequisites: what a bond's coupon and maturity are, the idea that money in the future is discounted to present value
- Exclusions: no convexity derivation, no Macaulay vs. modified duration formula, no credit spread or default risk, no YTM vs. current yield distinction in detail, no callable bond mechanics
- Score: 9/10

---

## Candidate 06 — Why the Fee You Barely Notice Costs You a Quarter of Your Retirement
- Source: `mba-computational-finance/chapters/04-funds-and-etfs.md`
- Topic: COMPUTATIONAL FINANCE
- Hook: A fund fee of 0.95% per year — less than $1 on every $100 — compounds into a loss of 26% of your retirement balance over 35 years.
- Key case: Two investors put $10,000 into identical-return funds. One pays 0.05%; the other pays 1.0%. After 35 years at 7% gross: $103,900 vs. $76,900 — a $27,000 gap on a $10,000 start.
- The Question: A 0.95% fee difference is barely visible year to year. After 35 years it erases 26% of the ending balance. How does such a small annual fee become such a large permanent loss?
- Core idea: Compounding the fee drag — each year the fee not only removes money but also removes the future returns that money would have generated. The loss compounds just like the gains do: money extracted early is missing for all the remaining years, so the total loss grows faster than a linear extrapolation suggests, reaching 26% over 35 years.
- Visual object: Two compounding-wealth curves starting at the same point and diverging over 35 years, with the gap shaded and labeled
- Manim move: trace
- Example seed: Mei invests $20,000 in a target-date fund at age 30. She has a choice: a 0.03% index ETF or a 0.85% actively managed fund. Same underlying stocks. At 7% gross over 35 years: ETF → $207,800; active fund → $153,800. The $54,000 gap is the compounded cost of 0.82% per year that felt invisible.
- Length band: 2–3 min
- Still lanes: geo (two diverging curves with shaded gap), geo (stacked-bar showing how early-year fee losses cascade forward)
- Prerequisites: the idea of compound interest, what an expense ratio is
- Exclusions: no active-vs-passive alpha debate, no tax efficiency mechanics, no authorized-participant arbitrage, no fund-structure comparison (open-end vs. ETF vs. closed-end)
- Score: 9/10

---

## Candidate 07 — Why the Terminal Value You Barely Notice Controls the Whole Valuation
- Source: `mba-computational-finance/chapters/05-time-value-of-money-and-discounted-cash-flows.md`
- Topic: COMPUTATIONAL FINANCE
- Hook: In a discounted cash flow model, the cash flows you explicitly forecast for 10 years often contribute less to the valuation than a single number representing everything after year 10.
- Key case: Sara's catering business: 10 years of projected cash flows sum to a present value of ~$1,074,000. The terminal value — a single Gordon Growth number — contributes ~$692,000. Change the perpetual growth rate by 1 percentage point and the total value swings by hundreds of thousands of dollars.
- The Question: A DCF model produces detailed year-by-year forecasts. Yet the single terminal-value assumption at the end dominates 60–80% of total value. How can one number you cannot observe carry more weight than ten years of explicit analysis?
- Core idea: Geometric discounting means near-term cash flows shrink quickly in present value while a growing perpetuity is anchored by its denominator (r − g); a small change in g moves the denominator dramatically — a 1-point drop from 4% to 3% in a 10%-rate model doubles the terminal value — so the terminal assumption carries structural leverage over every explicit year.
- Visual object: Stacked bar: explicit-year PV vs. terminal value PV, with the terminal bar growing as g rises
- Manim move: accumulate
- Example seed: An analyst values a chain of car washes at 5× next year's free cash flow of $400,000, for $2M. A buyer's DCF uses 12% discount rate, 3% perpetual growth. Terminal value at year 10 = $536K / (0.12 − 0.03) = $5.96M. PV of terminal value = $5.96M / (1.12)^10 = $1.92M. Explicit years add $1.08M. Total = $3.0M — 50% above the simple multiple. The growth-rate assumption explains the entire gap.
- Length band: 3–5 min
- Still lanes: geo (stacked bar shifting as g changes), geo (sensitivity table showing NPV corners)
- Prerequisites: what a discount rate is, the concept of present value, basic perpetuity formula C/r
- Exclusions: no Gordon Growth derivation from geometric series, no multi-stage growth discussion, no IRR vs. NPV debate, no Sara business backstory
- Score: 8/10

---

## Candidate 08 — Why the Number of Stocks in Your Portfolio Matters Less Than Their Correlation
- Source: `mba-computational-finance/chapters/04-funds-and-etfs.md`
- Topic: COMPUTATIONAL FINANCE
- Hook: An investor with 30 mutual funds thinks they are well-diversified; an investor with 5 low-correlation stocks may be far more diversified.
- Key case: A portfolio of 30 US large-cap technology funds has a pairwise correlation near 1.0 — adding funds 6 through 30 reduced risk by almost nothing. A portfolio of 5 funds from 5 different asset classes with 0.2 average correlation can achieve far lower variance.
- The Question: Diversification means spreading across many holdings. Thirty funds should be far safer than five. But the 30-fund portfolio has nearly the same risk as holding one fund. Why doesn't count equal protection?
- Core idea: Portfolio variance formula: Var(R_p) = (σ²/N) + (1 − 1/N)·ρ·σ² — as N grows large the first term vanishes and variance approaches ρσ². More holdings help only when they reduce ρ (the average pairwise correlation). Funds with ρ near 1.0 add positions without reducing correlation — the floor never falls.
- Visual object: The two-term variance decomposition: the diversifiable piece shrinking to zero, the ρσ² floor staying put
- Manim move: collapse
- Example seed: Raj holds 20 US equity mutual funds. Average pairwise ρ = 0.90. Portfolio vol ≈ √(0.90 × 18%²) ≈ 17.1%. He replaces 15 funds with a single international bond ETF (ρ = 0.15 with his US equity). Five-asset portfolio vol falls to ~12%. The count went down; the protection went up.
- Length band: 2–3 min
- Still lanes: geo (two-term variance bars with shrinking diversifiable piece), geo (floor line that does not move as N increases)
- Prerequisites: what portfolio variance is, basic concept of correlation
- Exclusions: no efficient-frontier derivation, no Markowitz optimization, no covariance matrix formalism, no Evans-Archer 20-stock paper citation, no factor models
- Score: 8/10

---

## Candidate 09 — Why Beta Measures What Volatility Cannot
- Source: `mba-computational-finance/chapters/11-asset-pricing-models.md`
- Topic: COMPUTATIONAL FINANCE
- Hook: A stock that swings 35% annually on drug-trial news can have a beta near zero — meaning it contributes almost no market risk to your portfolio, despite its wild swings.
- Key case: A biotech stock awaiting FDA approval swings 35% in a single afternoon, but the move is driven entirely by the trial outcome — uncorrelated with the S&P 500. Beta ≈ 0.15. Meanwhile a bank stock moves only 18% annually but tracks the market tightly; beta ≈ 1.4.
- The Question: Volatility measures how much a stock swings. Beta measures something else. A 35%-vol stock with near-zero beta barely matters for portfolio risk. An 18%-vol stock with beta 1.4 contributes heavily. Why does adding them to a portfolio reveal their true costs and benefits?
- Core idea: CAPM prices only systematic risk — the portion of a stock's variance that co-moves with the whole market. Idiosyncratic variance (the trial outcome, the product recall) diversifies away when you hold many stocks and earns no expected premium. Beta = Cov(stock, market)/Var(market) isolates only the co-movement that survives diversification.
- Visual object: A two-panel scatter plot: biotech vs. S&P 500 (flat regression line, low beta) beside bank vs. S&P 500 (steep regression line, high beta)
- Manim move: compare
- Example seed: An analyst builds a 10-stock portfolio. She adds a solar startup (vol = 45%, beta = 0.20). The portfolio volatility barely moves. She then adds a railroad stock (vol = 15%, beta = 1.50). The portfolio vol rises noticeably. Same stock count, opposite portfolio-risk effects — driven entirely by beta, not vol.
- Length band: 2–3 min
- Still lanes: geo (two scatter plots side by side with regression lines), geo (variance decomposition: systematic vs. idiosyncratic)
- Prerequisites: what standard deviation of returns means, the concept of a market index, what a regression line is (loosely)
- Exclusions: no CAPM expected-return formula or security market line, no alpha calculation, no Fama-French factors, no beta confidence interval statistics, no NVDA case numbers
- Score: 8/10

---

## Candidate 10 — Why How Much You Risk Matters More Than Which Assets You Pick
- Source: `mba-computational-finance/chapters/10-capital-allocation-and-diversification.md`
- Topic: COMPUTATIONAL FINANCE
- Hook: Most investors spend their time choosing between stocks and funds; the decision that actually drives long-run wealth is how much of their money is in risky assets at all.
- Key case: Two investors hold the same optimal risky portfolio (7% expected return, 9.5% vol). Investor A puts 95% in it; investor B puts 40%. After 30 years the difference in terminal wealth dwarfs any reasonable asset-selection edge.
- The Question: Both investors own the same well-constructed portfolio. Yet their outcomes over 30 years look almost unrelated. How can the same portfolio produce such different results?
- Core idea: The Capital Allocation Line: mixing the risky portfolio with cash traces a straight line in return-volatility space; every point on the line has the same Sharpe ratio. The only question is where on the line to stand (y*), which is set by risk aversion: y* = (E[r] − r_f) / (A·σ²). Getting y* wrong by 30 percentage points is worth more in compounded wealth than near-perfect asset selection.
- Visual object: The Capital Allocation Line with two labeled points — one at 40% risky (y=0.4), one at 95% (y=0.95) — and their compounded terminal-wealth bars at year 30
- Manim move: scan
- Example seed: Both Kenji and Ana build an efficient portfolio with 7% expected return. Kenji sets y* = 0.90 (risk-averse coefficient A ≈ 3). Ana sets y* = 0.45 (A ≈ 6). After 30 years at 7% compound: Kenji's $50K → ~$407K; Ana's $50K at 5.35% → ~$235K. They held the same portfolio. The allocation decision explains the $172K gap.
- Length band: 3–5 min
- Still lanes: geo (Capital Allocation Line with two points marked), geo (two compounding-wealth curves diverging)
- Prerequisites: what the Sharpe ratio is, what a risk-free rate is, the concept of expected return and volatility
- Exclusions: no efficient-frontier derivation, no utility function formalism beyond the intuition, no human-capital argument for young investors, no Kelly criterion, no leverage discussion
- Score: 8/10
