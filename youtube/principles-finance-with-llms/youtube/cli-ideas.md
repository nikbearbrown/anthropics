# Principles of Finance with LLMs — CLI Video Ideas ("X with Claude")

## Candidate 01 — Build a Beta Regression and CAPM Cost-of-Equity Calculator with Claude
- Source: principles-finance-with-llms/chapters/14-regression-analysis-in-finance.md + LLM Exercise
- Lane: BUILD (Claude Code)
- Hook: The number that sets your discount rate comes from a 60-line Python script — and most analysts copy it from Bloomberg without knowing if it's right for their firm.
- The artifact: a beta regression plot (scatter of stock vs. S&P 500 monthly returns with the OLS line drawn), plus a CAPM sensitivity table showing cost-of-equity across beta ±0.2 and ERP 4–6% — animated as a Manim scene revealing the SML and sweeping the sensitivity bands.
- Prompt seed: `claude "Write a Python script using yfinance and scipy.stats.linregress that fetches 60 months of monthly returns for a ticker vs the S&P 500, plots the OLS regression line, prints beta/alpha/R-squared, and then computes CAPM cost of equity at risk-free=4.5% and ERP=5%. Show me the output for AAPL."`
- Read / check: Verify the beta matches Yahoo Finance's published figure within ±0.2 (different windows explain gaps); verify the R² is in the 0.3–0.7 range typical for large-cap stocks; check that the scatter plot shows market returns on x-axis and stock returns on y-axis with the regression line passing through the centroid.
- Human supplies (Claude can't): No hardware capture needed. The script pulls live data from yfinance — a screen-recording of the actual Python run is the authentic output. The final Manim SML animation is fully synthetic (no real data required; Claude generates illustrative beta values). **Screen-recording of the terminal run is the real asset the human must capture**; the Manim scene is a synthetic explainer beat.
- Output medium: screen-recording mp4 (terminal + matplotlib plot appearing) for the CODE/OUTPUT beat; Manim animated Security Market Line for the SUMMARY beat.
- The change: swap the 60-month window for a 36-month window and re-run; show how beta shifts and explain Bayesian shrinkage (Blume adjustment: β_adj = 0.67×β + 0.33×1.0) as the revision.
- Teardown angle: A single historical beta is an estimate with noise baked in — the sensitivity table is not optional, it is the honest result. Most published betas are backward-looking; the video exposes what you're actually trusting when you plug one into a DCF.
- Exclusions: multi-factor Fama-French regression, implied-cost-of-capital methods, short-selling mechanics, options pricing.
- Score: 9/10

## Candidate 02 — Build a Compounding Curve Visualizer with Claude
- Source: principles-finance-with-llms/chapters/07-time-value-of-money-i-single-payment-value.md + LLM Exercise
- Lane: BUILD (Claude Code)
- Hook: The Rule of 72 says your money doubles every 72/r years — but the curve that actually shows you why is an exponential that feels flat for two decades and then rockets. Most people never see it drawn.
- The artifact: an animated Manim plot of FV = PV×(1+r)^n for r = 2%, 4%, 8%, 12% from n=0 to n=50 — four curves drawing simultaneously, with a vertical line sweeping from left to right and a callout showing each curve's value at the cursor. The doubling times (Rule of 72) are marked as dots on each curve.
- Prompt seed: `claude "Write a Python script that computes FV = 1000*(1+r)^n for r in [0.02, 0.04, 0.08, 0.12] and n from 0 to 50, then outputs a table showing year, FV for each rate, and the year each curve first doubles. Print the Rule of 72 estimate vs actual doubling year for each rate."`
- Read / check: Verify that the 8% curve reaches approximately $46,900 at n=50 (≈ 46.9× the 4% curve as stated in the chapter); verify Rule of 72 estimates are within 0.5 years of actual for rates 2–12%; check that the 4-curve table makes the exponential gap between 4% and 8% visible by n=30.
- Human supplies (Claude can't): Nothing — fully synthetic. All numbers are deterministic from the formula; no real market data needed. The Manim animation is generated from the script output.
- Output medium: Manim (animated multi-curve exponential plot with sweeping cursor and Rule of 72 annotations).
- The change: add a second panel showing the same curves in real (inflation-adjusted) terms at 3% inflation using the Fisher equation — revealing how much the "8% return" shrinks to ~4.9% real.
- Teardown angle: The gap between 4% and 8% over 50 years is not 2× — it is 6.6×. Starting early beats contributing more; the animation makes this visceral in a way a table cannot.
- Exclusions: annuities, mortgage math, negative interest rate edge cases, continuous compounding derivation.
- Score: 9/10

## Candidate 03 — Compute Sharpe Ratio and Volatility Drag for Any Ticker with Claude
- Source: principles-finance-with-llms/chapters/13-statistical-analysis-in-finance.md + LLM Exercise
- Lane: BUILD (Claude Code)
- Hook: A fund with 12% arithmetic return sounds better than one with 10% — until you realize volatility drag means the higher-return fund actually compounds to *less* over 20 years.
- The artifact: a side-by-side Manim bar chart showing arithmetic mean, geometric mean, standard deviation, and Sharpe ratio for a user-chosen stock vs. the S&P 500 — with an animated wealth-accumulation curve for $10,000 invested over 20 years under both the arithmetic and geometric mean, making the volatility drag gap visible as a shaded region.
- Prompt seed: `claude "Write Python using yfinance to fetch 60 months of monthly returns for TSLA and SPY, then compute: arithmetic mean, geometric mean, annualized standard deviation, Sharpe ratio (risk-free=4.5%), correlation between them, and volatility drag (arith_mean - sigma^2/2). Print a comparison table. Show the dollar difference in terminal wealth for $10,000 invested over 20 years using arith vs geo mean for each."`
- Read / check: Verify geometric mean is always ≤ arithmetic mean (with equality only when σ=0); verify TSLA's standard deviation is substantially higher than SPY's (chapter context: ~25–40% annualized for TSLA vs ~15% for SPY); verify the Sharpe ratio formula uses excess return over the risk-free rate, not just raw return.
- Human supplies (Claude can't): A screen-recording of the terminal run against live yfinance data is the authentic output beat. The Manim wealth-accumulation animation is synthetic (uses the computed numbers). **Human must screen-record the real Python run** to show actual current numbers.
- Output medium: screen-recording mp4 (terminal table) for OUTPUT beat; Manim animated wealth-accumulation comparison with shaded volatility-drag region for SUMMARY beat.
- The change: swap the single-ticker comparison for a two-ticker equal-weight portfolio and recompute — showing how correlation below 1.0 reduces the portfolio's standard deviation below the weighted average (the Markowitz diversification effect, animated as the portfolio variance formula sweeping in).
- Teardown angle: Arithmetic mean is what people quote; geometric mean is what they actually earn. The drag compounds. A high-volatility asset with 12% arithmetic return can underperform a low-volatility 10% asset over 20 years — and the number that reveals this fits in one Python function.
- Exclusions: fat-tail modeling, CVaR/expected shortfall, options-based hedging, individual stock fundamentals.
- Score: 9/10

## Candidate 04 — Build an NPV vs IRR Decision Tool with Claude
- Source: principles-finance-with-llms/chapters/16-how-companies-think-about-investing.md + LLM Exercise
- Lane: BUILD (Claude Code)
- Hook: Two mutually exclusive projects, both above the hurdle rate — NPV says pick one, IRR says pick the other. One of them is always wrong. The tool shows you which, and why.
- The artifact: an animated Manim plot showing NPV profiles (NPV as a function of discount rate) for two competing projects, with the crossover rate marked as a vertical line — the point where the NPV decision flips. A second panel shows a decision table (payback, discounted payback, NPV, IRR, MIRR) populated by Claude.
- Prompt seed: `claude "Write Python to compute payback period, discounted payback period, NPV, IRR, and MIRR for two mutually exclusive projects: Project A costs $16,000 with cash flows [2000, 4000, 5000, 5000, 5000, 5000] and Project B costs $40,000 with cash flows [8000, 14000, 13000, 12000, 11000, 10000]. Use a discount rate of 9%. Print the crossover rate where NPV(A) = NPV(B). Show which metric picks which project."`
- Read / check: Verify that NPV(B) > NPV(A) at 9% (the chapter states $3,971 vs $2,836); verify IRR(A) > IRR(B) (14.1% vs 13.2%); verify the crossover rate is between 9% and 14%; verify MIRR resolves the IRR size bias in the same direction as NPV.
- Human supplies (Claude can't): Nothing — fully synthetic from the textbook's own numbers. The Manim NPV profile animation is generated from the computed data. Screen-recording of the Python run is optional but strengthens authenticity.
- Output medium: Manim (animated dual NPV profiles with crossover rate marker and decision table reveal).
- The change: add capital rationing — a $40,000 budget constraint with four projects competing — and use the profitability index to rank them, showing how PI correctly handles the constraint where NPV alone cannot.
- Teardown angle: IRR is a rate; it cannot be compared across projects of different scales without losing information. NPV is a dollar value added; it is the correct objective. The crossover rate is the number that reveals exactly how much you're giving up by using the wrong metric.
- Exclusions: real-options analysis, staged investment decisions, Monte Carlo simulation of cash flows.
- Score: 8/10

## Candidate 05 — Price a Corporate Bond and Plot the Yield Curve with Claude
- Source: principles-finance-with-llms/chapters/10-bonds-and-bond-valuation.md + LLM Exercise
- Lane: BUILD (Claude Code)
- Hook: A bond trades at $1,051 even though the issuer will only ever pay back $1,000 at maturity — and understanding why is the foundation of every interest-rate decision in finance.
- The artifact: a Manim animation showing two panels — (1) the bond pricing formula summing coupon PVs and principal PV as animated bar segments stacking to the total price; (2) a yield curve (normal, flat, inverted) fetched from FRED or hardcoded, with the bond's YTM plotted as a point on the curve and an animated price-vs-YTM inverse relationship.
- Prompt seed: `claude "Write Python to price a semi-annual coupon bond with par=$1000, coupon_rate=2.25%, maturity=5.5 years (remaining), at YTM values from 0.5% to 5% in 0.25% steps. Print a table of price vs YTM. Also compute the price at YTM=1.24% and show that it equals approximately $1051.20. Plot price vs YTM as a curve."`
- Read / check: Verify that price at YTM=2.25% equals par ($1,000) exactly (coupon rate = YTM → par pricing); verify price at YTM=1.24% is approximately $1,051 (premium bond); verify the price-YTM relationship is monotonically decreasing (higher yield → lower price); verify semi-annual coupon payment is $11.25 per period.
- Human supplies (Claude can't): Nothing — fully synthetic from the chapter's 3M bond example. The yield curve can be hardcoded (normal/inverted shapes) or fetched from FRED with a `fredapi` call; the FRED fetch makes it authentic but requires a free API key the human must supply.
- Output medium: Manim (animated stacked-bar bond pricing + price-vs-YTM curve with inverse-relationship reveal).
- The change: swap the fixed-rate bond for a callable bond and show how the call option compresses the price-YTM curve above par (negative convexity) — illustrating why callable bonds have a different risk profile.
- Teardown angle: Bond math is just present-value arithmetic, but the inverse price-yield relationship catches every beginner. The animation makes visible what the formula implies: when yields fall, every future payment is worth more in today's dollars, so the price must rise.
- Exclusions: credit-spread analysis, CDS pricing, duration/convexity deep-dive, municipal bond tax-equivalence.
- Score: 8/10

## Candidate 06 — Build a Pro Forma Three-Statement Model with Claude
- Source: principles-finance-with-llms/chapters/18-financial-forecasting.md + LLM Exercise
- Lane: BUILD (Claude Code)
- Hook: A company grows profits 30% but runs out of cash — and every step of why is visible in a three-statement model that Claude can scaffold in 50 lines of Python.
- The artifact: a Manim animated waterfall chart showing how growth in sales drives up working capital requirements, producing a cash shortfall even while the income statement shows record profit — with a bar chart of monthly cash position going red before recovering.
- Prompt seed: `claude "Build a 12-month pro forma model for a sporting goods retailer: starting sales $126K/yr growing 18%, COGS 55% of sales, SGA $30K fixed/yr, A/R collection 45 days, inventory turns 6x/yr, A/P payment 30 days. Print monthly income statement, balance sheet deltas, and cash flow. Identify the month when cash goes negative."`
- Read / check: Verify that the model identifies a cash crunch in months 3–5 when growth is fastest (working capital buildup precedes cash collection); verify that the income statement shows positive net income in those same months (profitable but cash-negative); verify that A/R days and inventory turns are correctly modeled as timing differences, not profit impacts.
- Human supplies (Claude can't): Nothing — fully synthetic from the chapter's Clear Lake Sporting Goods framework. The human may optionally substitute real 10-K data for a chosen company (which makes it more authentic but requires reading the actual filing for the timing assumptions).
- Output medium: Manim (animated monthly waterfall chart with income vs. cash divergence highlighted and cash-negative bar turning red).
- The change: add a $50K credit line to the model and re-run — showing how the credit line smooths the cash crunch and what the interest cost does to profit, making the working-capital-financing trade-off visible.
- Teardown angle: Profit and cash are not the same number, and the gap between them can kill a company. The model makes this visible month by month — the animated bar turning red is the lesson, not the formula.
- Exclusions: tax modeling, stock-based compensation, goodwill amortization, DCF valuation from the model.
- Score: 8/10

## Candidate 07 — Build a Monte Carlo DCF Valuation with Claude
- Source: principles-finance-with-llms/chapters/18-financial-forecasting.md + 11 (implied) + LLM Exercise
- Lane: BUILD (Claude Code)
- Hook: A DCF gives you one price target. The real answer is a distribution — and a Monte Carlo simulation shows you how wide it actually is.
- The artifact: a Manim histogram of 10,000 simulated DCF values, with the distribution's median and 10th/90th percentile marked, plus a sensitivity tornado chart showing which input (WACC, growth rate, terminal multiple) contributes the most variance.
- Prompt seed: `claude "Write Python to run a Monte Carlo DCF simulation: base revenue $5B, revenue growth drawn from Normal(0.08, 0.03), EBIT margin drawn from Normal(0.15, 0.02), WACC drawn from Normal(0.09, 0.01), terminal growth drawn from Normal(0.025, 0.005). Run 10,000 trials. Print the median enterprise value, the 10th/90th percentile range, and which input has the highest Spearman correlation with the output (tornado chart)."`
- Read / check: Verify that the distribution is right-skewed (as expected for multiplicative growth compounded over time); verify that the 10th–90th percentile range is wide relative to the median (a defensible DCF always has substantial uncertainty); verify that WACC typically has the highest Spearman correlation (small WACC changes dominate in long-horizon DCFs due to exponential discounting).
- Human supplies (Claude can't): Real company revenue and margin figures from a 10-K make the simulation authentic. **Human must supply actual 10-K data** for any specific company; otherwise the illustrative parameters are acceptable as a teaching device. A screen-recording of the simulation running with a real ticker's parameters is the authentic output.
- Output medium: Manim (animated histogram building up from 10,000 draws + tornado chart bar animation).
- The change: switch from normal distributions to triangular distributions (min/base/max) for each input and re-run — showing how fat-tailed assumptions (e.g., WACC ranging 7–13%) widen the distribution and why analysts who report a single DCF target are overconfident.
- Teardown angle: A point estimate is not a valuation — it is the mean of a distribution you have not yet shown. The Monte Carlo forces honesty about input uncertainty and reveals which assumptions actually drive the answer.
- Exclusions: real-options modeling, sector-specific multiples, terminal value sensitivity in isolation.
- Score: 8/10

## Candidate 08 — Build a Jet Fuel Hedge Model with Claude
- Source: principles-finance-with-llms/chapters/20-risk-management-and-the-financial-manager.md + LLM Exercise
- Lane: BUILD (Claude Code)
- Hook: Southwest Airlines locked in jet fuel at $0.30/gallon for years while competitors paid $2+. A forward hedge is just arithmetic — but the arithmetic has a payoff that looks like a graph.
- The artifact: a Manim animated payoff diagram showing (1) unhedged airline P&L as fuel price varies; (2) the forward contract payoff (a straight line crossing zero at the forward price); (3) the combined hedged P&L — a flat line. Second beat: add an option overlay showing how a cap hedge works differently from a forward.
- Prompt seed: `claude "Write Python to compute an airline's quarterly fuel P&L for jet fuel prices from $1.50 to $4.00/gallon: baseline consumption 1 billion gallons/quarter, operating margin $0.08/gallon at $2.50 fuel. Show: unhedged P&L, forward-hedge payoff (locked at $2.50), option-cap payoff (cap at $2.80, premium $0.05/gallon), and combined hedged P&L for each strategy. Print a table and identify breakeven prices."`
- Read / check: Verify the forward hedge produces a flat combined P&L regardless of fuel price (the defining property of a forward); verify the option-cap payoff allows profit when fuel is cheap but caps the loss when it rises above $2.80; verify that the option strategy costs the premium ($0.05/gallon × 1B gallons = $50M) even when fuel stays below the cap.
- Human supplies (Claude can't): Nothing — fully synthetic. The $500M annual exposure figure from the chapter's American Airlines example can be used as the illustrative baseline. Screen-recording of the Python run is optional but anchors authenticity.
- Output medium: Manim (animated three-panel payoff diagram — unhedged, forward, option — with the combined line revealed last).
- The change: add a basis risk layer — show what happens when the forward is on crude oil but the actual exposure is jet fuel, and the two prices diverge by 15% during a refinery disruption. The hedged P&L is no longer flat, revealing basis risk.
- Teardown angle: A hedge converts price risk into basis risk — it is not free, and it is not perfect. The payoff diagram makes the protection and the cost both visible simultaneously, which is why every risk management textbook uses this picture.
- Exclusions: swap mechanics, counterparty credit risk, CVA/DVA, speculative derivatives positions.
- Score: 8/10

## Candidate 09 — Build a Financial Ratio Dashboard from a 10-K with Claude
- Source: principles-finance-with-llms/chapters/06-measures-of-financial-health.md + LLM Exercise
- Lane: BUILD (Claude Code)
- Hook: A company's 10-K is 200 pages. The six ratios that tell you whether to read the rest are computable in ten lines — if you know which ones and what they mean.
- The artifact: a Manim animated ratio dashboard (current ratio, debt-to-equity, ROIC, free cash flow conversion, TIE, quick ratio) shown as animated gauges or bar charts, with each ratio turning green/yellow/red against a sector benchmark band.
- Prompt seed: `claude "From this income statement and balance sheet data [paste numbers], compute: current ratio, quick ratio, debt-to-equity, interest coverage (TIE), return on invested capital (ROIC = NOPAT/Invested Capital), and free cash flow conversion (FCF/Net Income). Compare each to the following industry benchmarks [paste or ask Claude to use typical S&P 500 consumer staples ranges]. Format as a dashboard table with green/yellow/red status for each."`
- Read / check: Verify ROIC is computed as NOPAT/(total debt + equity - cash) not as net income / equity; verify TIE uses EBIT not net income in the numerator; verify the current ratio is computed from current assets and current liabilities only (not total assets/liabilities); check that FCF conversion uses operating cash flow minus capex, not just operating cash flow.
- Human supplies (Claude can't): **Actual 10-K data for a real company is required for authenticity** — the human must paste or upload the income statement and balance sheet from the company's most recent 10-K from EDGAR. Synthetic/illustrative numbers are acceptable for a teaching demo but weaker for a research-grade video.
- Output medium: Manim (animated ratio-gauge dashboard with red/yellow/green indicator bars appearing one by one).
- The change: compare the same company's ratios across three fiscal years (trend analysis) — showing whether financial health is improving or deteriorating, and which ratio moved most as a leading signal.
- Teardown angle: Each ratio is a question: Is it liquid enough to survive a bad quarter? Is the debt load sustainable? Is it actually earning returns above its cost of capital? The dashboard surfaces the answers in 30 seconds; the 10-K takes two hours.
- Exclusions: segment-level analysis, footnote-level adjustments, off-balance-sheet liabilities, goodwill impairment.
- Score: 7/10

## Candidate 10 — Build an Equity Research Snapshot Generator with Claude
- Source: principles-finance-with-llms/chapters/00-claude-basics.md + LLM Exercise
- Lane: BUILD (Claude Code)
- Hook: Every analyst starts with a one-page company snapshot. Claude can draft it from a 10-K upload in 90 seconds — the discipline is knowing what to verify and what to push back on.
- The artifact: a screen-recording of Claude (via claude CLI) ingesting a real 10-K and outputting a structured one-page snapshot (business overview, industry context, financial scale, three strategic themes, three key risks) — then a second pass showing the analyst correcting a hallucinated citation and a stale data point.
- Prompt seed: `claude "I have uploaded [company]'s most recent 10-K. Produce a one-page company snapshot: (1) business overview — what the company does, its main products/services, how it makes money (2-3 sentences); (2) industry context — sector, main competitors, approximate market position; (3) financial scale — most recent fiscal year revenue, operating income, net income, total assets as a small table; (4) three strategic themes from the MD&A; (5) three key risks from the risk factors. Cite specific pages or sections. Do not invent figures."`
- Read / check: Verify each financial figure against the actual 10-K (the video's key demonstration is catching a hallucinated or stale number); verify that cited pages exist and contain the claimed content; check that competitor names are real and current (LLMs frequently cite outdated competitive landscapes).
- Human supplies (Claude can't): **A real 10-K from EDGAR is required** — the human must download the PDF and upload it to Claude. The verification step (comparing Claude's output to the actual filing) requires the human to read specific pages, which is the point of the video. No synthetic substitute exists for authentic 10-K data.
- Output medium: screen-recording mp4 (full terminal session showing the upload, the Claude output, and the verification/correction loop).
- The change: re-run with a deliberately adversarial prompt — "answer as if it's five years ago" — to expose how LLMs handle time-shifted queries, then show the correct prompt structure that forces Claude to cite page numbers and flag staleness.
- Teardown angle: The power move is not generating the snapshot — it is knowing what to verify. A junior analyst who trusts every Claude output unverified is worse than one who doesn't use it. The video teaches verification as the skill, not generation.
- Exclusions: DCF valuation, sector-relative analysis, earnings model construction.
- Score: 7/10
