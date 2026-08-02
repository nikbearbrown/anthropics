# MBA Finance: with LLMs — CLI Video Ideas ("X with Claude")

Lane: BUILD (quantitative finance — artifacts are computed numbers, charts, models)
Book: mba-finance (25 chapters; equity research running project across all chapters)

---

## Card 1 — Compound-Interest Visualizer

**Source:** Chapter 7 (Time Value of Money I) — the Friend A / Friend B compounding story; $10,000 breakeven-rate puzzle
**Lane:** BUILD
**Hook:** Two friends invest the same asset class at the same rate. Friend A invests for 9 years, stops. Friend B invests for 35 years. At 65, Friend A wins. A single Manim curve reveals why — and Claude writes every line.
**The artifact:** Animated compound-growth curve showing PV, FV, and cumulative-interest split across n periods; optional side-by-side bar: Friend A vs. Friend B contribution vs. growth stacks.
**Prompt seed:** `claude "Write a Python/Manim script that animates compound interest: PV=1000, r=0.04, n=50. Show: (1) a curve of FV vs. year, (2) the split between principal and interest at each year as stacked bars, and (3) annotate the year where interest exceeds principal for the first time. Add a slider parameter for r so the curve updates for r=[0.02, 0.04, 0.08, 0.12]."`
**Read/check:** Verify Friend A / Friend B breakeven arithmetic matches Chapter 7's numbers; confirm the interest-exceeds-principal year.
**Human supplies:** Nothing — fully synthetic. If the user wants to model their own savings plan, they supply PV, r, n as CLI args. Synthetic illustrative data is perfectly acceptable for the video.
**Output medium:** Manim animated mp4 — growth curve sweeps across time axis, stacked bars animate year by year; r parameter value displayed live.
**The change:** Swap to r=0.12 (emerging-market rate); watch the crossover year shrink dramatically and the terminal value explode. Narrate: "That's the power of rate, not time."
**Teardown angle:** Add quarterly compounding (n×4, r/4) vs. annual — show the difference in the terminal bar. Is it significant? Chapter 7 says yes.
**Exclusions:** Skip continuous compounding (Chapters cover discrete only). No inflation adjustment — that's a separate card.
**Score:** 8/10 — clean artifact, strong visual, the Friend A/B story is textbook-viral. One-take runnable.

---

## Card 2 — Bond Yield-to-Maturity Solver with Price Sensitivity

**Source:** Chapter 10 (Bonds and Bond Valuation) — 3M bond puzzle ($1,051.20 price vs. $1,000 par), YTM formula, price-yield inverse relationship
**Lane:** BUILD
**Hook:** 3M's bond pays $22.50/year forever promises $1,000 at maturity — but it trades at $1,051. Someone's paying $51 too much. Claude reverse-engineers the implied market rate and builds the price-yield curve that explains it.
**The artifact:** A YTM solver that takes coupon, par, price, n as inputs and outputs YTM via Newton-Raphson iteration; then a Manim animated price-yield curve showing how price moves as yield changes, with the current bond plotted as a moving dot.
**Prompt seed:** `claude "Write a Python script that: (1) solves for YTM given coupon_rate=0.0225, par=1000, price=1051.20, n=5.5 years using scipy.optimize; (2) plots a Manim price-yield curve sweeping yield from 0.5% to 6%, with the current price/yield pair marked as an animated dot; (3) annotates the par-value crossover at yield = coupon_rate."`
**Read/check:** Check 3M bond math from Chapter 10 (YTM should be ≈1.24%). Verify the formula: P = C × [1-(1+y)^-n]/y + F/(1+y)^n.
**Human supplies:** Nothing — fully synthetic. Real users would need the bond's current market price from FINRA TRACE or Bloomberg; synthetic values from the chapter are fine for the video.
**Output medium:** Manim animated mp4 — price-yield curve draws across the frame; the moving dot shows where today's bond sits; par-price crossover annotated.
**The change:** Raise yield from 1.24% to 3.5% — watch the price drop below par. Ask Claude to annotate: "At what yield does this bond become a 'discount bond'?" Claude answers: when yield > coupon rate = 2.25%.
**Teardown angle:** Semi-annual coupon adjustment (US corporate convention) — prompt Claude to modify the script for semi-annual payments. Show the price differences. Are they material?
**Exclusions:** No callable bond OAS or duration calculation (Chapter 10 doesn't cover those). No credit spread modeling.
**Score:** 9/10 — artifact is deterministic, output is the lesson (price-yield inverse), visually stunning as an animation. One core formula, one revision, one punchline.

---

## Card 3 — Gordon Growth Model Sensitivity Grid

**Source:** Chapter 11 (Stocks and Stock Valuation) — DDM / Gordon growth model, sensitivity warning table (±1pp moves price ±20-33%), two-stage DDM
**Lane:** BUILD
**Hook:** The textbook shows a 2×2 sensitivity table for a stock — changing r or g by 1% moves the price 33%. Claude builds the full 5×5 grid in Manim, animating how dangerous the model is near the r=g boundary.
**The artifact:** An animated Manim heatmap/grid: rows = required return (7–11%), columns = dividend growth rate (2–6%). Each cell shows the Gordon-model price P₀ = D₁/(r−g). Cells near r=g boundary show extreme values (or "undefined"). Color gradient: green (low price) → red (high price).
**Prompt seed:** `claude "Write a Python/Manim script that builds a 5x5 sensitivity grid for the Gordon Growth Model. D0=5.00. Rows: required_return=[0.07,0.08,0.09,0.10,0.11]. Columns: growth_rate=[0.02,0.03,0.04,0.05,0.06]. Show P0=D0*(1+g)/(r-g) in each cell. Color cells by price magnitude (green→yellow→red). Cells where r≤g display 'N/A' in red. Animate cells populating row by row."`
**Read/check:** Verify textbook Table (r=8%,g=4%→$130; r=9%,g=4%→$104; r=9%,g=5%→$130) match Chapter 11 exactly.
**Human supplies:** Nothing — fully synthetic (D₀ from the textbook example). A real analyst would supply the firm's most recent dividend and consensus growth estimate.
**Output medium:** Manim animated mp4 — grid populates cell by cell; final frame zooms to the "danger zone" near the r=g diagonal; color gradient shifts as values move to extremes.
**The change:** Add a two-stage DDM scenario: high growth (13%) for 5 years, then settle to 5%. Ask Claude to compute the two-stage price and place it on the sensitivity grid as a star marker. Show it's outside the constant-growth model range.
**Teardown angle:** What inputs would justify Tesla's historical P/E of 100×? Back-solve for implied growth rate — expose how optimistic the market's implicit assumptions are.
**Exclusions:** No free-cash-flow-to-equity (FCFE) DDM variant. No P/E multiples valuation (Chapter 11 covers multiples separately).
**Score:** 9/10 — the danger-zone animation is a perfect explainer beat. The lesson is the visual: the grid shows the model is sensitive precisely where analysts disagree.

---

## Card 4 — Financial Ratio Dashboard (Five-Family Diagnostic)

**Source:** Chapter 6 (Measures of Financial Health) — five families (efficiency, liquidity, solvency, market value, profitability); Clear Lake Sporting Goods running example; $30M net income puzzle
**Lane:** BUILD
**Hook:** $30 million profit sounds great — until you divide by the right denominator. Claude reads two firms' financial statements and produces a five-family ratio dashboard, revealing which firm is actually healthy.
**The artifact:** A Python script that takes two firms' IS/BS as JSON inputs and outputs a color-coded five-family ratio comparison table: efficiency (asset turnover, AR turnover, inventory days), liquidity (current ratio, quick ratio), solvency (D/E, interest coverage), profitability (net margin, ROA, ROE), market value (P/E, P/B). Rendered as a Manim animated table with green/yellow/red cells.
**Prompt seed:** `claude "Write a Python script that computes financial ratios for two firms from JSON balance-sheet and income-statement inputs. Compute all five families: efficiency (asset_turnover, ar_turnover, days_inventory), liquidity (current_ratio, quick_ratio), solvency (debt_to_equity, interest_coverage), profitability (net_margin, roa, roe), market_value (pe_ratio, pb_ratio). Output a side-by-side table with industry-benchmark thresholds and color-code (green/yellow/red) each metric. Use the Clear Lake Sporting Goods data from Chapter 6 as Firm A."`
**Read/check:** Cross-check Clear Lake ratios against Chapter 6 worked examples. Verify the small retailer vs. industrial manufacturer comparison from the chapter opener.
**Human supplies:** For the video: synthetic JSON for Firm A (Clear Lake from chapter) and Firm B (synthetic industrial manufacturer). For real use: user supplies 10-K financials as JSON. Synthetic data is acceptable for the video.
**Output medium:** Manim animated table — cells populate family by family; color transition animates (grey → green/yellow/red) as each metric is computed; final frame shows the two-firm comparison side by side.
**The change:** Swap Firm B to a leverage-heavy firm (high D/E, low coverage ratio). Watch the solvency family cells turn red. Narrate: "Profitability looks similar — solvency tells the real story."
**Teardown angle:** Ask Claude to identify which single ratio most distinguishes the two firms. Claude should cite interest coverage or quick ratio as the primary solvency signal.
**Exclusions:** No DuPont decomposition (that's a separate card). No industry-specific normative ranges (those require external data).
**Score:** 8/10 — well-bounded artifact, color-coding is visually instructive, five-family structure gives the video natural beats. Requires minimal human input (synthetic JSON).

---

## Card 5 — NPV vs. IRR Conflict Resolver

**Source:** Chapter 16 (How Companies Think About Investing) — regular vs. heavy-duty machine conflict; five metrics hierarchy; IRR ignores project scale
**Lane:** BUILD
**Hook:** Two machines. IRR says buy the small one. NPV says buy the big one. Both are right about their own question. Claude builds a decision engine that shows which metric to trust — and animates the scale problem.
**The artifact:** A Python/Manim script that takes two mutually exclusive projects (cash flow arrays, discount rate) and computes all five metrics: payback, discounted payback, NPV, IRR, profitability index. Highlights conflicts, explains resolution via NPV supremacy. Outputs a bar-race animation comparing metrics.
**Prompt seed:** `claude "Write a Python script that evaluates two mutually exclusive capital projects. ProjectA: cost=16000, cashflows=[2000,4000,5000,5000,5000,5000], r=0.09. ProjectB: cost=40000, cashflows=[8000,14000,13000,12000,11000,10000], r=0.09. Compute: payback, discounted_payback, NPV, IRR (Newton-Raphson), profitability_index. Build a Manim animated table showing all five metrics side by side with a final NPV recommendation. Highlight the NPV/IRR conflict in red."`
**Read/check:** Verify Chapter 16 machines: regular machine NPV=$2,836 at 9%, IRR=14.1%; heavy-duty NPV=$3,971, IRR=13.2%.
**Human supplies:** Nothing — synthetic cash flows from the chapter. Real analysts would supply projected free cash flows from a capex memo; synthetic is fine for the video.
**Output medium:** Manim animated table — rows populate one metric at a time; conflict cells flash red; NPV recommendation appears as a highlighted final row with explanation.
**The change:** Modify the cash flow timing of ProjectB so it backloads more cash — show how IRR rises but NPV doesn't change. Reinforce: IRR is a rate, NPV is wealth.
**Teardown angle:** Add a "modified IRR" (MIRR) calculation that corrects for the reinvestment rate assumption. Show when MIRR and NPV align that IRR doesn't.
**Exclusions:** No real-options analysis. No multi-period capital rationing (PI ranking) — that would require more than one revision beat.
**Score:** 9/10 — classic textbook conflict with clean resolution. Conflict cells flashing red makes the lesson visceral. One of the highest-pedagogical-impact videos in the book.

---

## Card 6 — Pro Forma Three-Statement Forecaster

**Source:** Chapter 18 (Financial Forecasting) — Clear Lake Sporting Goods, percentage-of-sales method, seasonality distribution, linked IS/BS/CF statements
**Lane:** BUILD
**Hook:** A company reports record profit — then misses payroll three months later. Pro forma forecasting catches the cash gap before it kills the business. Claude builds the linked three-statement model in real time.
**The artifact:** A Python script that takes: (a) historical monthly sales, (b) cost percentages (COGS%, SGA%), (c) fixed costs, (d) working capital terms (AR days, inventory days, AP days), and outputs a 12-month pro forma income statement, balance sheet, and cash flow statement. Animates cash balance vs. net income monthly — showing the divergence during growth.
**Prompt seed:** `claude "Build a 12-month pro forma financial model for Clear Lake Sporting Goods. Inputs: base_annual_sales=148680, monthly_seasonality=[0.071,0.067,0.073,0.074,0.09,0.106,0.107,0.094,0.085,0.082,0.079,0.072], cogs_pct=0.50, fixed_monthly=[rent=458,salaries=468,depreciation=300,utilities=204], tax_rate=0.21, ar_days=30, inventory_days=120, ap_days=30. Output three linked statements. Animate monthly cash_balance vs. net_income on one chart to show the cash-profit divergence."`
**Read/check:** Verify January forecast matches Chapter 18: $10,408 sales, $5,204 COGS, $2,849 net income.
**Human supplies:** Nothing — synthetic inputs from Chapter 18. For real use, user supplies their own monthly sales history and cost structure. Synthetic data is fine for the video.
**Output medium:** Manim animated dual-line chart — net income (green) and cash balance (orange) trace month by month; divergence annotated in April when growth peaks and working capital consumes cash.
**The change:** Add the Chapter 18 adjustments: +$500 brand launch in March, +$2K/month June–August, −2% Q1 discontinued product. Watch the cash balance dip in Q1 even as income rises. This is the payroll-bouncing scenario made visible.
**Teardown angle:** Ask Claude to identify the minimum cash buffer needed to survive the worst-month gap. It should compute min(cash_balance) and suggest a revolving credit line for that amount.
**Exclusions:** No sensitivity analysis on growth rate (that would need a second prompt). No equity or debt raise modeling (Chapter 17 covers that separately).
**Score:** 8/10 — powerful real-world story (profitable companies that go bankrupt), the dual-line chart divergence is the lesson in one visual. Slightly higher complexity but still one-take with Claude.

---

## Card 7 — WACC Builder from First Principles

**Source:** Chapter 17 (How Firms Raise Capital) — Apple's $191B cash / $113B debt puzzle; after-tax cost of debt formula; CAPM for cost of equity; WACC construction
**Lane:** BUILD
**Hook:** Apple has more cash than it can spend — and it still borrows $113 billion. Claude computes the WACC that explains why, using live inputs from the 10-K structure, and shows what happens to firm value as the debt share changes.
**The artifact:** A Python WACC calculator that takes: equity market cap, debt market value, cost of debt (YTM), CAPM inputs (β, Rf, ERP), tax rate. Outputs: after-tax cost of debt, cost of equity via CAPM, WACC. Then a Manim animated bar chart showing how WACC shifts as the D/(D+E) weight changes from 0% to 50% debt, illustrating the optimal range.
**Prompt seed:** `claude "Build a WACC calculator in Python. Inputs: equity_mktcap=2900e9, debt_mv=111e9, ytm_debt=0.032, beta=1.24, rf=0.045, erp=0.05, tax_rate=0.21. Compute: after_tax_cost_debt = ytm*(1-tax_rate), cost_equity = rf + beta*erp, WACC = (E/(D+E))*re + (D/(D+E))*rd_aftertax. Then animate a curve: x=debt_weight from 0 to 0.6, y=WACC — show where WACC is minimized and annotate the optimal leverage point."`
**Read/check:** Verify Apple's actual WACC against published estimates (Chapter 17 values used here are illustrative but should produce a reasonable 8–10% WACC range).
**Human supplies:** Nothing for the video — synthetic inputs calibrated to Apple 2023. Real use requires user to supply live YTM from FINRA and beta from a financial terminal; synthetic is acceptable for the video.
**Output medium:** Manim animated curve — WACC vs. debt weight sweeps left to right; minimum WACC annotated; current Apple position marked as a dot.
**The change:** Double the tax rate to 42% (hypothetical tax increase scenario) — watch the after-tax cost of debt fall further, WACC curve shifts, optimal debt point moves right. Narrate: "Higher taxes make debt even cheaper, so firms borrow more."
**Teardown angle:** What happens to WACC if beta rises from 1.24 to 1.8 (tech sector stress)? Re-run — WACC jumps, firm value falls even with same operating cash flows.
**Exclusions:** No Hamada equation (unlevering/relevering beta). No multi-class share structure (beyond scope here).
**Score:** 8/10 — direct extension of the Apple puzzle, WACC curve animation is clean, connects capital structure theory to a real number. High MBA relevance.

---

## Card 8 — Regression Beta Estimator (CAPM Empirical)

**Source:** Chapter 14 (Regression Analysis in Finance) — OLS beta estimation, R², CAPM regression; Chapter 13 (Statistical Analysis) — arithmetic vs. geometric mean
**Lane:** BUILD
**Hook:** Beta is just the slope of a regression. Claude downloads historical returns, runs the OLS, and produces the security characteristic line — plus a confidence interval that most textbooks skip.
**The artifact:** A Python script that uses yfinance to pull 5 years of weekly returns for a stock (e.g., NVDA) and SPY, runs OLS regression (returns_stock ~ returns_market), extracts beta (slope), alpha (intercept), R², and plots the security characteristic line (SCL) as a Manim scatter + regression line animation.
**Prompt seed:** `claude "Write a Python script that: (1) downloads 5yr weekly returns for NVDA and SPY using yfinance; (2) runs OLS regression of NVDA excess returns on SPY excess returns (using 3-month T-bill rate as Rf); (3) prints beta, alpha, R-squared, and 95% confidence interval for beta; (4) produces a Manim scatter plot of (market_return, stock_return) with the regression line animated as a sweep across the data cloud; (5) annotates the slope as Beta and the intercept as Alpha."`
**Read/check:** Verify the NVDA beta from Chapter 11 (~1.6) is in the ballpark. Confirm OLS formula interpretation matches Chapter 14's treatment.
**Human supplies:** Internet access for yfinance during the run (download live data). If running offline, synthetic returns from a random-walk generator are acceptable for the demo. Notation: the video should clarify that live data requires internet; synthetic is used as fallback.
**Output medium:** Manim animated scatter plot — data points appear one by one (weekly returns), then regression line sweeps through the cloud; beta and R² annotated on final frame.
**The change:** Switch from NVDA to a utility stock (e.g., XLU) — beta drops below 1. Narrate: "Same market, same regression — completely different risk profile." The animated SCL becomes nearly flat.
**Teardown angle:** What happens when you shorten the window to 1 year (COVID crash included)? Beta becomes unstable — interval widens. Claude should print both betas and their CIs side by side.
**Exclusions:** No Fama-French three-factor model. No rolling-beta estimation (that's a follow-up card).
**Score:** 8/10 — uses real data (yfinance), produces a proper statistical output, connects Chapter 13 and 14 content. Slight dependency on internet access is the only friction.

---

## Card 9 — Hedging Payoff Simulator (Options/Futures)

**Source:** Chapter 20 (Risk Management) — jet fuel hedging, Southwest Airlines, forward contracts, speculation vs. hedging; commodity/FX/interest rate risk taxonomy
**Lane:** BUILD
**Hook:** Southwest Airlines saved hundreds of millions by hedging jet fuel. Claude simulates the payoff of a hedging strategy vs. being unhedged — and shows the break-even fuel price where hedging wins.
**The artifact:** A Python/Manim script that models two scenarios: (a) unhedged firm — cash flow = revenue − (spot_price × gallons); (b) hedged firm — locks in forward_price for a fraction of gallons, pays market for the rest. Sweeps spot price from $1.50 to $4.00/gallon and plots both cash-flow curves. Annotates the break-even spot price where hedging breaks even vs. unhedged.
**Prompt seed:** `claude "Simulate an airline's jet-fuel hedging decision. Inputs: annual_gallons=4e9, revenue=50e9, fixed_costs=40e9, forward_price=2.07, hedge_fraction=0.70. Compute for spot_prices in range(1.50, 4.01, 0.01): unhedged_profit = revenue - fixed_costs - spot*gallons; hedged_profit = revenue - fixed_costs - (forward*hedge_fraction + spot*(1-hedge_fraction))*gallons. Animate both profit curves sweeping across spot price in Manim. Annotate break-even spot price and the April 2018 actual spot of $2.19."`
**Read/check:** Verify Chapter 20's $480M cost shock calculation (4B gallons × $0.12) against script output at spot=$2.19 vs. spot=$2.07.
**Human supplies:** Nothing — fully synthetic (airline parameters from chapter). Real hedging requires actual contract terms from a derivatives desk; synthetic is fine for the video.
**Output medium:** Manim animated dual-curve chart — unhedged profit (red) and hedged profit (blue) sweep across spot price axis simultaneously; break-even crossover annotated; actual 2018 spot marked.
**The change:** Increase hedge_fraction from 70% to 100% — hedged profit becomes a flat line (full insurance). Narrate: "Perfect hedge eliminates upside too — Southwest didn't go to 100% for a reason." Show the forfeited upside when spot falls to $1.50.
**Teardown angle:** What's the cost of the hedge? If each forward contract costs a $0.03/gallon premium, recompute break-even. Show the premium's effect on the hedged curve shifting down.
**Exclusions:** No Black-Scholes options pricing (Chapter 20 covers forwards/futures, not options Greeks). No basis risk.
**Score:** 8/10 — vivid real story (Southwest), clean two-curve payoff animation, the change prompt has a strong narrative twist (upside forfeiture). Synthetic data is robust.

---

## Card 10 — Equity Research Project Assembler (Full Pipeline)

**Source:** Chapter 00 (Claude Basics) — running equity research project described across all chapters: regression → WACC → DCF → ratios → pro forma → stock valuation
**Lane:** BUILD
**Hook:** The book spans 20 chapters of building one equity research report — company selection in Ch.2, financial statements in Ch.5, ratios in Ch.6, TVM in Ch.7–9, bond/stock valuation in Ch.10–11, regression beta in Ch.14, WACC in Ch.17, pro forma in Ch.18. Claude assembles the full pipeline in one session.
**The artifact:** A Python orchestration script (using a Claude Project for persistent context) that prompts Claude to: (1) accept a stock ticker, (2) pull financial data (yfinance + SEC EDGAR), (3) compute the five ratio families, (4) run CAPM regression for beta, (5) build WACC, (6) generate a 3-year DCF with Gordon terminal value, (7) compare DCF to Gordon DDM to P/E multiple. Outputs a single analyst-summary JSON and a Manim title-card animation of the final valuation range.
**Prompt seed:** `claude "You are a financial analyst. Stock: AAPL. Pull last 10-K data from SEC EDGAR or use cached JSON I'll provide. Compute: (1) five-family ratio dashboard; (2) CAPM beta from 5yr weekly returns vs SPY; (3) WACC using market cap, debt, YTM, beta, rf=4.5%, ERP=5%, tax=21%; (4) 3-year DCF with terminal growth rate 3%; (5) Gordon DDM with current dividend and 5yr historical DGR; (6) P/E multiple vs. sector median. Return a JSON with all outputs and a 'valuation_range': [low, mid, high]."`
**Read/check:** Verify outputs are internally consistent — WACC from step 3 should match discount rate used in step 4. Gordon DDM and DCF should be within the same order of magnitude for a stable dividend payer.
**Human supplies:** SEC EDGAR access or a pre-downloaded 10-K JSON. If working offline, a synthetic balance sheet / income statement (provided in the script's defaults) is acceptable for the video; flag this on-screen.
**Output medium:** Manim title-card animation — valuation range displayed as a horizontal bar (low → mid → high); current market price marked as a line; color (green = undervalued, red = overvalued). One final frame per valuation method.
**The change:** Switch ticker from AAPL to a volatile growth stock (e.g., RIVN) — DDM fails (no dividend), DCF is highly sensitive to terminal rate. Claude adapts: skips DDM, widens confidence interval, flags WACC uncertainty. Narrate: "The model tells you when it can't tell you anything."
**Teardown angle:** What is the sensitivity of the DCF to terminal growth rate (g)? Run g from 1% to 5% — show valuation range doubles. This is the Gordon-model lesson from Card 3 applied to a real company.
**Exclusions:** No qualitative moat analysis. No peer-relative positioning (that would require multiple tickers in one run).
**Score:** 7/10 — the most ambitious card in the batch; the running-project structure makes it compelling but it depends on data access. Best built after Cards 2, 3, 7, and 8 exist as standalone pieces the viewer has already seen. Score reflects complexity, not value — this is the capstone video.
