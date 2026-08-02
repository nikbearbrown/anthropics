# Computational Finance with AI — CLI Video Ideas ("X with Claude")

## Candidate 01 — Build a Cross-Model Sharpe Ratio Verifier with Claude
- Source: computational-finance-with-ai/chapters/02-returns-and-risk-measurement.md + LLM Exercise
- Lane: BUILD (Claude Code)
- Hook: Three models return NVDA Sharpes of 1.38, 1.41, and 1.62 for the same ticker — the spread is 15% and could flip a recommendation. Which one is right?
- The artifact: A Python script that pulls NVDA and SPY monthly returns via yfinance, computes arithmetic return, geometric CAGR, annualized volatility (daily × √252), and Sharpe (3-month T-bill risk-free) for both 3-year and 5-year windows, then renders a Manim bar-chart animation comparing the two windows side by side with the convention labels annotated on each bar.
- Prompt seed: `claude "Write a Python script using yfinance that computes NVDA vs SPY: arithmetic return, CAGR, annualized volatility (daily, scaled by √252), and Sharpe ratio at the 3-month T-bill rate, for both a 3-year and 5-year window. Print a labelled markdown table and save a CSV. Include the convention in every header: frequency, window, return type."`
- Read / check: Verify that NVDA 3-year Sharpe lands in 1.3–1.8; SPY 3-year Sharpe in 0.4–0.6. Confirm volatility was scaled by √252 not 252 (catch the ×16 error). Check that the 5-year Sharpe is lower than the 3-year (AI-rally dilution).
- Human supplies: A yfinance-capable Python environment. Optionally, a screen-recording of the terminal run for the screen-rec OUTPUT beat. Synthetic data is acceptable for the animation if live data is unavailable on record day.
- Output medium: Manim (animated) — two grouped bar charts growing side by side: 3-year window left, 5-year right, with bars for NVDA and SPY; NVDA's bar visibly larger; annotation arrow marking "AI rally window" on the 3-year bar.
- The change: Re-run with σ computed from monthly returns (scaled by √12) instead of daily returns. Show the spread between the two volatility estimates in a third Manim panel.
- Teardown angle: The Sharpe ratio is not a fact — it is a fact conditional on four choices (window, frequency, return type, risk-free rate). The CHANGE beat makes that concrete: the same asset, the same period, different number, different story.
- Exclusions: Black-Scholes, margin mechanics, Jensen's alpha, any Fama-French factors.
- Score: 9/10

## Candidate 02 — Build the Black-Scholes Put Pricer with Claude Code
- Source: computational-finance-with-ai/chapters/07-options-and-derivatives.md + LLM Exercise
- Lane: BUILD (Claude Code)
- Hook: Jin wants to floor his $925K AAPL position for six months. Black-Scholes says the put costs $5.16 per share — but the market quotes $5.27. That eleven-cent gap is the implied volatility difference that professional traders track.
- The artifact: A ~40-line Python script that prices a European put via Black-Scholes (SciPy for N()), then back-solves implied vol from any market quote using scipy.optimize.brentq, and renders a Manim animation of the put payoff hockey stick morphing into the full protective-put payoff as the user increases the notional from 100 to 5,000 shares.
- Prompt seed: `claude "Write a Python function bs_put(S, K, r, T, sigma) that prices a European put via Black-Scholes using scipy.stats.norm.cdf. Add a second function implied_vol(S, K, r, T, market_price) that back-solves sigma using scipy.optimize.brentq. Print both the theoretical price and the implied vol for AAPL: S=185, K=170, r=0.045, T=0.5, market_price=5.27."`
- Read / check: Verify d1 ≈ 0.694 and the put price ≈ $5.16 before the market-price correction. Check that implied vol is slightly above the flat-vol input (≈25.5% vs 25%). Confirm N() is called with negative arguments for the put formula.
- Human supplies: Live option-chain midpoint quote for AAPL or a substitute ticker (to make the implied-vol beat authentic). Synthetic parameters are acceptable if live data is unavailable on record day. No trained model required.
- Output medium: Manim (animated) — hockey-stick payoff diagram for the put alone, then the combined long-stock + long-put payoff drawn in, with the floor line highlighted and the premium ($5.16/share × 5,000 shares = $25,800) annotated.
- The change: Replace the flat-volatility assumption with a simple volatility skew: out-of-the-money puts at σ+3pp, at-the-money at σ, in-the-money at σ−3pp. Show how the skew-adjusted price compares to flat-vol.
- Teardown angle: The Black-Scholes price is not "what the option costs" — it is what is consistent with a given volatility. The market price implies the market's volatility estimate; the model just organizes the relationship.
- Exclusions: Greeks derivations, early-exercise for American options, barrier options, delta hedging mechanics.
- Score: 9/10

## Candidate 03 — Build the Efficient Frontier with Claude Code
- Source: computational-finance-with-ai/chapters/09-portfolio-construction.md + LLM Exercise
- Lane: BUILD (Claude Code)
- Hook: The optimizer gives zero weight to long Treasuries every time — but that's exactly the asset that saved portfolios in 2008. Can a 50-line script expose the flaw?
- The artifact: A Python script (cvxpy or scipy) that constructs the mean-variance efficient frontier for VTI, VB, VEA, BND, VGLT, VTIP using 10-year monthly returns from yfinance, plots the frontier as a Manim scene where the curve sweeps from min-variance to max-Sharpe, marks the tangency portfolio, and shows VGLT dropping to 0% weight at every point on the frontier.
- Prompt seed: `claude "Write a Python script that loads 10-year monthly returns for VTI, VB, VEA, BND, VGLT, VTIP via yfinance, computes the sample covariance matrix, and uses scipy.optimize to trace the efficient frontier across 50 target returns. Plot frontier points as (vol, return) pairs. Mark the minimum-variance portfolio and the maximum-Sharpe portfolio. Print the tangency-portfolio weights."`
- Read / check: Confirm VGLT weight ≈ 0% in the unconstrained tangency portfolio. Verify that adding a 5% floor on VGLT raises overall portfolio vol only marginally. Check that the frontier is strictly convex (no flat segments). Cross-check tangency Sharpe against a simple 65/35 VTI/BND Sharpe.
- Human supplies: yfinance-accessible Python environment. Screen-recording of the terminal output for the code beat. Optionally, historical returns from a CSV if yfinance is unavailable on record day — synthetic data acceptable with clear labelling.
- Output medium: Manim (animated) — the frontier curve draws itself from left to right; then dots appear for each individual asset; then the tangency point pulses; then VGLT's dot is shown inside the frontier with a callout: "dominated in calm markets."
- The change: Add a 5% minimum weight constraint on VGLT and re-run. Show the frontier contracting slightly and the tangency shifting; animate the portfolio composition bar chart updating.
- Teardown angle: Mean-variance optimization uses one correlation matrix. The real world uses two — one for calm markets, one for crises. The optimizer correctly sets VGLT to 0% using calm-period data; a crisis would reward the override.
- Exclusions: DeMiguel-Garlappi equal-weight comparison (save for a follow-on card), taxes, liability-driven investing, Black-Litterman.
- Score: 9/10

## Candidate 04 — Measure NVDA's Alpha with CAPM and Claude Code
- Source: computational-finance-with-ai/chapters/11-asset-pricing-models.md + LLM Exercise
- Lane: BUILD (Claude Code)
- Hook: NVDA returned 78% annualized over three years. CAPM says it should have returned 14.4% given its beta. The 64-percentage-point gap is alpha — but does that mean "exceptional skill" or "exceptional luck"?
- The artifact: A Python script that runs three OLS regressions (36-, 24-, 60-month windows) of NVDA monthly returns on SPY, extracts beta, 95% CI, and R², computes CAPM-implied expected return using a 6% equity risk premium, and computes realized alpha. Output: a Manim grouped bar chart with three clusters, each showing CAPM-expected vs actual return with the alpha gap shaded.
- Prompt seed: `claude "Write a Python script using yfinance and statsmodels to regress NVDA monthly log returns on SPY monthly log returns for three windows: 24, 36, and 60 months ending today. For each: print the beta estimate, its 95% CI, R-squared, and the implied CAPM expected return assuming rf=4.2% and ERP=6%. Also print the actual annualized return and the alpha gap."`
- Read / check: Confirm beta in range 1.4–2.0 across windows. Verify that wider windows produce tighter confidence intervals. Check that alpha is positive and large (≥30pp) in all windows given NVDA's recent performance. Confirm log-return regression (not simple returns).
- Human supplies: yfinance environment. Nothing else — fully synthetic computation. Screen-recording of terminal optional.
- Output medium: Manim (animated) — three grouped bars animate into place left to right; alpha gap fills in with a shaded region; annotation "64pp alpha: skill or luck?" appears; R² values annotate each cluster.
- The change: Switch to a Fama-French 3-factor regression by downloading the FF factors from Ken French's data library. Show how adding SMB and HML absorbs some of the CAPM alpha.
- Teardown angle: A large alpha means the model cannot explain the return — it doesn't partition the return into luck vs. skill. CAPM narrows the question precisely; it does not answer it.
- Exclusions: Fama-French factor construction from scratch, Carhart momentum, Jensen's alpha vs. information ratio distinction.
- Score: 8/10

## Candidate 05 — Price a Bond's Duration Risk with Claude Code
- Source: computational-finance-with-ai/chapters/03-equity-and-fixed-income.md + LLM Exercise
- Lane: BUILD (Claude Code)
- Hook: Apple's 2.95% bond due 2049 is rated AAA — yet it drops 11% when long rates rise 1%. How can a "safe" bond lose more than some stocks?
- The artifact: A Python script that computes the bond price, current yield, YTM, and Macaulay/modified duration for the Apple 2049 bond at two yield scenarios (5.0% and 6.0%), then renders a Manim animation where the price bar visibly shrinks (from ~$707 to ~$625) as a rate-rise arrow slides across the screen.
- Prompt seed: `claude "Write a Python function bond_price(face, coupon_rate, ytm, periods) that computes the present value of all cash flows. Also write modified_duration(face, coupon_rate, ytm, periods). Use semi-annual periods. Apply it to: Apple 2.95% bond due Sep 2049, ~47 periods remaining, compute price at YTM=5.0% and YTM=6.0%, and the resulting price change. Also compute current yield at both prices."`
- Read / check: Confirm price at 5.0% ≈ $707 and at 6.0% ≈ $625 per $1,000 face. Verify modified duration ≈ 16 years. Check that the duration-approximated price change (−16% × 1pp rise) matches the actual price change within ~1pp.
- Human supplies: Nothing — fully synthetic, no live data needed. Apple bond parameters are stated in the chapter.
- Output medium: Manim (animated) — a timeline shows coupon payments as downward arrows and the face-value return as a large upward arrow at maturity; then a yield-shift animation shrinks all the discount factors; the price bar falls with a counter.
- The change: Compute convexity and show how the duration-only approximation underestimates the price recovery when rates fall by 1pp, and the price decline when rates rise. Add convexity correction.
- Teardown angle: Duration is the first derivative; convexity is the second. The bond's price path is curved, not linear — duration gives the slope at one point, not the shape of the curve.
- Exclusions: Credit risk, embedded options, callable bond pricing, swap curves.
- Score: 8/10

## Candidate 06 — Build a Volatility Drag Simulator with Claude Code
- Source: computational-finance-with-ai/chapters/02-returns-and-risk-measurement.md
- Lane: BUILD (Claude Code)
- Hook: A stock goes up 50% then down 50%. The arithmetic average return is 0%. The actual result is −25%. That gap — volatility drag — grows with every leveraged ETF, every rebalancing decision, every long holding period.
- The artifact: A ~30-line Python script that simulates two portfolios over 1,000 daily steps — one at zero volatility compounding at the arithmetic mean, one at σ=30% around the same mean — and renders a Manim animation where the two paths diverge visibly, with the drag gap annotated as approximately σ²/2.
- Prompt seed: `claude "Write a Python script that simulates two portfolios over 252 trading days: Portfolio A compounds at a fixed daily return equal to the arithmetic mean of Portfolio B's distribution. Portfolio B draws daily log returns from N(mu, sigma^2) with mu=0.10/252 and sigma=0.20/sqrt(252). Run 500 Monte Carlo paths for B. Plot all B paths in light grey and the single A path in bold. Annotate the median gap at day 252 as the volatility drag: approximately sigma^2/2 per year."`
- Read / check: Verify that the median B path ends below A despite identical expected daily returns. Confirm the annotated drag ≈ σ²/2 = 0.02 (2pp for σ=20%). Check that log-return simulation is correct (not simple returns).
- Human supplies: Nothing — fully synthetic. No live data required.
- Output medium: Manim (animated) — 500 grey paths fan out; the deterministic A path draws as a bold line above the median fan; a shaded gap annotates the drag at year 1; the animation pauses on the divergence.
- The change: Double σ to 40% (a leveraged ETF proxy) and show the drag quadruples (σ²/2 = 8pp/year), making the leveraged version underperform even a lower-return unleveraged position.
- Teardown angle: Arithmetic mean and geometric mean diverge proportionally to variance. A leveraged ETF with twice the daily return and twice the volatility does not double the long-run compounded return — it roughly halves it.
- Exclusions: Path-dependent rebalancing, Kelly criterion, detailed Monte Carlo theory.
- Score: 8/10

## Candidate 07 — Build Maya's Three-Beat Verification Log with Claude Code
- Source: computational-finance-with-ai/chapters/01-introduction-the-three-beat-method.md + LLM Exercise
- Lane: BUILD (Claude Code)
- Hook: Three models return NVDA Sharpes of 1.38, 1.41, and 1.62. The 15% spread could flip a memo — but there is a disciplined way to classify whether that's cosmetic or substantive.
- The artifact: A Python script that prompts Claude API (claude-3-5-haiku) with a precise specification (ticker, window, return type, risk-free rate), parses the output into a verification log table (metric × model × value × spread), then flags rows where spread > 10% as "substantive disagreement requiring investigation."
- Prompt seed: `claude "Write a Python script using the Anthropic SDK that sends three identical prompts to claude-3-5-haiku asking for NVDA vs SPY Sharpe ratio (36-month daily, √252 annualization, 4.5% risk-free rate). Parse each response to extract the Sharpe ratio as a float. Print a verification log table showing all three values and the spread. Flag the row if spread > 10%."`
- Read / check: Confirm that API calls use the same prompt text. Verify that float parsing handles percentage vs. decimal format. Check that the spread threshold logic fires correctly. The actual numbers will vary by model run — the check is on the pipeline, not the specific value.
- Human supplies: Anthropic API key. Screen-recording of the terminal run (shows live API calls, the three outputs appearing, the log table printing) — this is the authentic OUTPUT beat.
- Output medium: Screen-recording mp4 of the terminal — three API responses streaming in, verification log printing, the flag appearing on the Sharpe row.
- The change: Add a fourth "primary source" row populated by a manual yfinance computation. Show that the primary source closes the disagreement or reveals a systematic bias in one of the model responses.
- Teardown angle: The three-beat method replaces the disciplines that spreadsheets enforced automatically (named ranges → specification; formula trace → editorial read; scenario tab → verification). The pipeline makes that explicit.
- Exclusions: Full memo generation, multi-model orchestration beyond three calls, production error handling.
- Score: 8/10

## Candidate 08 — Compute NVDA's DCF Sensitivity with Claude Code
- Source: computational-finance-with-ai/chapters/03-equity-and-fixed-income.md + LLM Exercise
- Lane: BUILD (Claude Code)
- Hook: The Gordon Growth Model says P = D₁/(r−g). A 1pp change in perpetual growth rate moves a stock's fair value by 33%. The formula is brutally sensitive — and most analysts hide that sensitivity.
- The artifact: A Python script that computes a Gordon Growth Model price for a dividend-paying stock across a grid of (r, g) pairs, then renders a Manim heatmap animation where the price surface sweeps up steeply as g approaches r, with the "denominator blows up" cliff visible.
- Prompt seed: `claude "Write a Python script that computes Gordon Growth Model stock price P = D1/(r-g) for D1=4.00 across a grid: r from 6% to 12% (step 0.5%) and g from 1% to 5.5% (step 0.5%). Flag cells where g >= r as undefined. Output a pandas DataFrame. Also print the % change in P when g moves from 4% to 5% holding r=8%."`
- Read / check: Confirm P = $100 at r=8%, g=4% (D1=$4.00). Verify the 33% price jump when g moves from 4% to 5%. Confirm NaN or infinity where g ≥ r.
- Human supplies: Nothing — fully synthetic. No live data required.
- Output medium: Manim (animated) — a 2D price surface (heatmap) rendered; a vertical cliff appears where g→r; an animated price bar shows the 33% jump when g increments by 1pp.
- The change: Apply a two-stage DDM: high growth (g₁=10%) for five years, then perpetual (g₂=3%). Show that the two-stage value is more conservative and less sensitive to the terminal assumption.
- Teardown angle: The sensitivity is not a flaw in the model — it is the model honestly telling you that perpetual growth rate is the dominant assumption. Making it visible is the discipline.
- Exclusions: Full DCF projection, FCFE vs. FCFF distinction, multi-stage models beyond two stages.
- Score: 7/10

## Candidate 09 — Stress-Test a Two-Asset Portfolio Correlation with Claude Code
- Source: computational-finance-with-ai/chapters/08-the-diversification-miracle.md + LLM Exercise
- Lane: BUILD (Claude Code)
- Hook: NVDA and SPY had a correlation of ~0.65 in calm markets. In August 2022 it spiked toward 0.92. The "diversification miracle" only works when correlation is low — and correlation is not stable.
- The artifact: A Python script that computes the rolling 60-day correlation between NVDA and SPY over five years, then plots a Manim time-series animation where correlation rises sharply during the 2022 drawdown, with the portfolio volatility formula σ_p² shown updating in real time.
- Prompt seed: `claude "Write a Python script using yfinance and pandas to compute the 60-day rolling Pearson correlation between NVDA and SPY daily log returns over the last 5 years. Also compute, for each day, the 50/50 portfolio volatility using the two-asset formula: sqrt(0.25*var_nvda + 0.25*var_spy + 2*0.5*0.5*corr*std_nvda*std_spy). Save both series and print the date of maximum correlation."`
- Read / check: Confirm correlation spikes above 0.85 during the 2022 drawdown period. Verify portfolio volatility formula implementation (check weights sum to 1). Confirm that low-correlation periods have portfolio vol well below the average of individual vols.
- Human supplies: yfinance environment. Screen-recording of the terminal optional.
- Output medium: Manim (animated) — dual time-series: upper panel correlation rolling line, lower panel portfolio vol vs. simple average vol. The 2022 drawdown period highlighted; labels showing "diversification benefit collapses here."
- The change: Add a third asset (BND, aggregate bonds) and show how the three-asset portfolio correlation to equities remained lower during the 2022 period, and how it would have shifted under 2008 conditions.
- Teardown angle: Correlation is not a constant — it is a regime-dependent statistic. The efficient frontier computed from calm-market correlations is wrong precisely when you most need it to be right.
- Exclusions: Copula models, conditional volatility (GARCH), crisis-period correlation estimation methods.
- Score: 7/10
