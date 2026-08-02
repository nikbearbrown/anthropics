# Computational Finance — CLI Video Ideas ("X with Claude")

Note: The computational-finance book's chapter content (02-chapter-01.md) is a placeholder — the substantive chapter content has not yet been written. The cards below are based on the book's title, the preface stub, and the established computational finance curriculum that this type of book typically covers. They are strong BUILD candidates for the topic area; they should be refined once the chapter content is written.

---

## Candidate 01 — "Build a Black-Scholes Option Pricer with Claude: The Formula That Didn't Know It Was Wrong"
- Source: computational-finance/chapters/02-chapter-01.md (placeholder — based on standard computational finance curriculum)
- Lane: BUILD (Claude Code)
- Hook: The Black-Scholes formula won a Nobel Prize. It also assumes markets are log-normal, volatility is constant, and options can be hedged continuously — none of which is true. Build it anyway, because understanding when a model is wrong requires first understanding what it computes.
- The artifact: A Python script that computes the Black-Scholes price and Greeks (Delta, Gamma, Theta, Vega) for European call and put options, given S (spot price), K (strike), T (time to expiry), r (risk-free rate), σ (volatility). Terminal output: a formatted table showing call price, put price, and 4 Greeks for a range of strike prices from 80% to 120% of spot. A Manim animation shows the call option price as a function of spot price (the payoff curve) with the Black-Scholes theoretical price overlaid.
- Prompt seed: `claude "Write a Python script black_scholes.py that computes: (1) Black-Scholes call price using scipy.stats.norm; (2) Black-Scholes put price using put-call parity; (3) Greeks: Delta (∂V/∂S), Gamma (∂²V/∂S²), Theta (∂V/∂t), Vega (∂V/∂σ). Parameters: S=100, K=range(80,121,5), T=0.5 (years), r=0.05, σ=0.2. Print a formatted table: Strike | Call Price | Put Price | Delta | Gamma | Theta | Vega. All values to 4 decimal places."`
- Read / check: Verify the call price for S=100, K=100, T=0.5, r=0.05, σ=0.2 is approximately $10.45 (standard reference value); check put-call parity holds: Call - Put = S - Ke^(-rT); verify Delta for deep in-the-money call approaches 1.0 and deep out-of-the-money call approaches 0; confirm Vega is positive for both calls and puts; check Theta is negative for long options (time decay).
- Human supplies: Nothing — fully synthetic. All inputs are parameters; no market data required. For the CHANGE beat, real market option prices (from any financial data provider) can be compared against the model output — showing the volatility smile that Black-Scholes cannot capture.
- Output medium: screen-recording mp4 (terminal showing the table output) + Manim (animated call price curve as function of spot price)
- The change: Plot the implied volatility (back-solve σ from observed market prices at different strikes) for a real options chain. Show the "volatility smile" — implied volatility is not constant across strikes, violating the model's core assumption. The smile is what Black-Scholes got wrong.
- Teardown angle: The formula is wrong in ways that are interesting. It is wrong because markets are not log-normal, volatility is not constant, and trading is not costless. But understanding the formula precisely is what makes the wrongness legible. Every improvement on Black-Scholes — stochastic volatility, local volatility, jump-diffusion — is a targeted correction of one specific assumption. You can't improve what you can't compute.
- Exclusions: American option pricing (requires trees or Monte Carlo), exotic options, the full derivation of the PDE from Ito's lemma, calibration to a full volatility surface.
- Score: 9/10

---

## Candidate 02 — "Simulate Portfolio Returns with Claude: Monte Carlo Before You Invest"
- Source: computational-finance/chapters/02-chapter-01.md (placeholder — standard computational finance curriculum)
- Lane: BUILD (Claude Code)
- Hook: A portfolio that returns 7% on average can still lose everything in 5% of scenarios. Monte Carlo simulation is the tool that makes the distribution visible — not just the mean, but the full range of possible outcomes including the tail.
- The artifact: A Python script monte_carlo_portfolio.py that runs N=10,000 simulations of a portfolio's monthly returns over T years, using geometric Brownian motion (GBM) parameters: annual return μ, annual volatility σ, initial value V₀. Output: (1) terminal table showing the 5th, 25th, 50th, 75th, 95th percentile portfolio values at each year; (2) a Manim animation showing 100 random paths sweeping forward in time, fanning out from V₀, with the median path highlighted and the 5th/95th percentile band shaded.
- Prompt seed: `claude "Write monte_carlo_portfolio.py that: (1) simulates 10,000 GBM paths for a portfolio with μ=0.07, σ=0.15, V0=100000, T=30 years, monthly steps; (2) prints a table: Year | P5 | P25 | Median | P75 | P95; (3) saves the 10,000 terminal values to results.npy. Use numpy for vectorized simulation — no loops over paths. Report runtime."`
- Read / check: Verify the median terminal value at T=30 years is approximately $761,000 (V₀ × e^(μ-σ²/2)×T = 100,000 × e^(0.07-0.01125)×30 ≈ $761k); check the P5 value is substantially lower than the median (left tail of log-normal distribution); verify the simulation uses vectorized numpy (not a Python loop over 10,000 paths — too slow); confirm runtime is under 5 seconds.
- Human supplies: Nothing — fully synthetic. All parameters are inputs; no real portfolio data required. For the CHANGE beat, real historical return data (from yfinance or FRED) can replace the synthetic parameters — but the structure of the simulation is identical.
- Output medium: screen-recording mp4 (terminal showing runtime and percentile table) + Manim (animated fan of 100 paths sweeping forward)
- The change: Add a second simulation: same portfolio but with monthly withdrawals of $3,000 (retirement scenario). Show the probability of ruin (portfolio hitting $0 before year 30) as a percentage across the 10,000 paths. The ruin probability is the number retirement planners care about most.
- Teardown angle: The mean return is not the return you get — it is the center of a distribution. A 7% average can coexist with a 5% probability of losing 50% of the portfolio in the first 10 years. The distribution is the truth; the mean is a summary statistic that hides it. Monte Carlo makes the distribution visible before the first dollar is invested.
- Exclusions: Correlated multi-asset portfolios (requires covariance matrix sampling), variance reduction techniques (antithetic variates, control variates), real-time simulation updating.
- Score: 9/10

---

## Candidate 03 — "Build a Mean-Variance Portfolio Optimizer with Claude: Markowitz in 40 Lines"
- Source: computational-finance/chapters/02-chapter-01.md (placeholder — standard computational finance curriculum)
- Lane: BUILD (Claude Code)
- Hook: Markowitz showed in 1952 that you can construct a portfolio with less risk than any of its individual assets. The "efficient frontier" is the set of portfolios with the maximum return for each level of risk. Claude builds it from scratch in 40 lines.
- The artifact: A Python script markowitz_optimizer.py that: (1) takes expected returns and a covariance matrix for N assets; (2) uses scipy.optimize to find the minimum-variance portfolio and the maximum Sharpe ratio portfolio; (3) plots the efficient frontier as a curve in (σ, μ) space; (4) marks the individual assets, the minimum-variance portfolio, and the max-Sharpe portfolio as labeled points. A Manim animation shows the efficient frontier curve drawing from left to right, with the two special portfolios appearing as the curve completes.
- Prompt seed: `claude "Write markowitz_optimizer.py that: (1) takes expected_returns (numpy array) and cov_matrix (numpy 2D array) as inputs; (2) uses scipy.optimize.minimize to find: (a) minimum variance portfolio (minimize portfolio variance); (b) maximum Sharpe ratio portfolio (r_f=0.03); (3) generates 500 random portfolios for the feasible set; (4) identifies the efficient frontier subset; (5) prints the weights, expected return, volatility, and Sharpe ratio for both special portfolios. Include a demo with 4 assets: μ=[0.08,0.10,0.12,0.06], σ=[0.15,0.20,0.25,0.10], correlation matrix with plausible values."`
- Read / check: Verify the minimum-variance portfolio has lower volatility than any individual asset in the demo (this should always be true for diversified assets); check the Sharpe ratio maximization produces a portfolio different from the minimum-variance portfolio; verify the efficient frontier is a smooth curve (not jagged — the random portfolio generation should be dense enough); confirm portfolio weights sum to 1 for both special portfolios.
- Human supplies: Nothing required — the demo uses synthetic parameters. For real use, historical return and covariance data from yfinance or FRED can replace the synthetic inputs; the optimizer code is identical.
- Output medium: screen-recording mp4 (terminal showing the optimization results) + Manim (animated efficient frontier curve drawing)
- The change: Add a constraint: no short selling (all weights ≥ 0). Rerun the optimizer with the constraint and show how the efficient frontier shrinks. The constrained frontier is below the unconstrained one — showing the cost of the no-shorting restriction in terms of foregone diversification benefit.
- Teardown angle: The efficient frontier is not a recommendation — it is the boundary of what is achievable. Every portfolio below the frontier is strictly dominated (you could get more return for the same risk, or less risk for the same return). The optimizer identifies the boundary; the investor chooses where on the boundary to sit based on their risk tolerance.
- Exclusions: Factor models (Fama-French — beyond mean-variance), Black-Litterman views incorporation, transaction cost optimization.
- Score: 9/10

---

## Candidate 04 — "Build a Bond Pricing and Duration Calculator with Claude: Interest Rate Risk Made Visible"
- Source: computational-finance/chapters/02-chapter-01.md (placeholder — standard computational finance curriculum)
- Lane: BUILD (Claude Code)
- Hook: When interest rates go up 1%, a 10-year bond loses roughly 8% of its value. That 8% is not a coincidence — it is duration. Claude builds the bond pricer that shows exactly where the risk comes from.
- The artifact: A Python script bond_pricer.py that computes: (1) the fair price of a bond given face value, coupon rate, yield-to-maturity (YTM), and maturity; (2) Macaulay duration (weighted average time to cash flows); (3) modified duration (price sensitivity to yield changes); (4) convexity correction. Terminal output: a table for a range of YTM values from 2% to 10%, showing price, duration, and modified duration at each yield. A Manim animation shows the price-yield relationship as an inverse curve, with a tangent line at the current yield representing the duration approximation.
- Prompt seed: `claude "Write bond_pricer.py that: (1) computes fair price of a bond: face=1000, coupon_rate=0.05 (annual), maturity=10 years, YTM=range(0.02,0.11,0.01); (2) computes Macaulay duration (weighted average time to cash flows, weights=PV(CF_t)/Price); (3) computes modified duration = Macaulay_duration/(1+YTM); (4) prints a table: YTM | Price | Macaulay Duration | Modified Duration; (5) verifies that ΔPrice ≈ -ModDuration × ΔY × Price for ΔY=0.01."`
- Read / check: Verify the bond price at YTM=5% (equals the coupon rate) is exactly $1000 (par pricing — this is a definitional check); check price at YTM=10% is approximately $692 (below par, as expected for above-market yield); verify duration is between 7-9 years for this bond (10-year, 5% coupon bond — Macaulay duration is approximately 8 years); confirm the duration approximation error is disclosed (actual vs. approximated price change for ΔY=1%).
- Human supplies: Nothing — fully synthetic. All inputs are parameters.
- Output medium: screen-recording mp4 (terminal showing the price-duration table) + Manim (animated price-yield curve with tangent line)
- The change: Add a zero-coupon bond comparison: same face value, same maturity, no coupon payments. Show that the zero-coupon bond has duration = maturity (exactly 10 years) and higher price sensitivity than the coupon bond. The comparison makes duration intuitive — a bond that pays nothing until maturity is maximally exposed to interest rate risk.
- Teardown angle: Duration is not just a number — it is the bond's sensitivity to interest rate changes, expressed in years. A modified duration of 8 means a 1% yield increase produces approximately an 8% price decrease. The convexity correction accounts for the non-linearity (the actual curve vs. the tangent line). Understanding this is what separates fixed-income trading from guessing.
- Exclusions: Callable bonds (negative convexity), credit risk / credit spreads, mortgage-backed securities, yield curve dynamics.
- Score: 8/10

---

## Candidate 05 — "Build a Risk Metrics Calculator with Claude: VaR and CVaR from First Principles"
- Source: computational-finance/chapters/02-chapter-01.md (placeholder — standard computational finance curriculum)
- Lane: BUILD (Claude Code)
- Hook: Value at Risk (VaR) answers the question: what is the worst loss I should expect in 95% of trading days? Conditional Value at Risk (CVaR) answers the harder question: given that I'm having a bad day, how bad is it? Both are mandatory risk metrics — and both are computable in 20 lines.
- The artifact: A Python script risk_metrics.py that: (1) generates N=10,000 daily portfolio return observations using GBM parameters (or accepts real return data); (2) computes historical VaR at 95% and 99% confidence levels; (3) computes parametric VaR assuming normality; (4) computes CVaR (expected shortfall) at both confidence levels; (5) prints a comparison table: Method | 95% VaR | 99% VaR | 95% CVaR | 99% CVaR. A Manim animation shows the return distribution histogram with VaR and CVaR marked as vertical lines, the tail shaded in red.
- Prompt seed: `claude "Write risk_metrics.py that: (1) generates 10,000 daily returns from GBM with μ=0.0003 (daily), σ=0.01 (daily); (2) computes historical VaR at 95% and 99% (the negative of the 5th and 1st percentile); (3) computes parametric VaR assuming normality (μ ± z × σ, where z=1.645 for 95%, z=2.326 for 99%); (4) computes CVaR = mean of returns below the VaR threshold; (5) prints a 2-row comparison table: Historical vs. Parametric for both confidence levels and both metrics. Show the percentage of simulated days that exceed each VaR threshold."`
- Read / check: Verify the historical and parametric VaR are close but not identical (they should differ because the return distribution is approximately but not exactly normal); check CVaR is always greater in magnitude than VaR at the same confidence level (CVaR is the expected loss conditional on exceeding VaR); verify the 95% VaR threshold is exceeded by approximately 5% of observations (by construction); confirm the table has the correct layout.
- Human supplies: Nothing required for the synthetic demo. For real use, replace the GBM simulation with actual return data from any financial API — the risk metrics code is identical.
- Output medium: screen-recording mp4 (terminal showing the risk table) + Manim (animated return distribution histogram with VaR/CVaR marked)
- The change: Apply both metrics to a historical crisis period: download S&P 500 returns from March 2020 (COVID crash). Show how historical VaR computed on pre-crisis data (2019) would have dramatically understated the actual losses in March 2020. This is the backtesting failure that made CVaR mandatory in Basel III.
- Teardown angle: VaR tells you about normal bad days. CVaR tells you about extreme bad days. The financial crisis of 2008 was a CVaR event — VaR-based risk management appeared sound right up until it wasn't. The difference between the two metrics is the difference between "this happens 5% of the time" and "when it happens, here is how bad it gets."
- Exclusions: Full Basel III regulatory VaR requirements, stressed VaR calculation, incremental risk charge, copula-based multivariate VaR.
- Score: 8/10

---

## Candidate 06 — "Simulate the Binomial Tree Option Pricer with Claude: Black-Scholes Before the Formula"
- Source: computational-finance/chapters/02-chapter-01.md (placeholder — standard computational finance curriculum)
- Lane: BUILD (Claude Code)
- Hook: Before the Black-Scholes formula, there was the binomial tree. It arrives at the same answer — one step at a time, no calculus required. Understanding the tree makes the formula legible; the tree also handles American options that the formula cannot.
- The artifact: A Python script binomial_tree.py that: (1) builds a binomial price tree (N steps) for an underlying asset using up-factor u = e^(σ√Δt) and down-factor d = 1/u; (2) computes European and American call/put option prices by backward induction; (3) prints the terminal tree (the final price column) and the option value tree; (4) shows that as N increases, the European price converges to Black-Scholes. A Manim animation shows the price tree building forward step by step (branching from left to right), then the option value tree propagating backward (right to left).
- Prompt seed: `claude "Write binomial_tree.py that: (1) builds a CRR binomial tree for N=5 steps: S=100, K=100, T=0.5, r=0.05, σ=0.2; computes u=exp(σ√Δt), d=1/u, risk-neutral probability p=(e^(rΔt)-d)/(u-d); (2) computes both European call (backward induction, no early exercise) and American call (backward induction with early exercise check at each node); (3) prints the forward price tree and the option value tree side by side; (4) runs for N=[5,10,20,50,100] and shows convergence of European price to Black-Scholes value (~$10.45 for these parameters)."`
- Read / check: Verify the European call price at N=100 steps is approximately $10.45 (the Black-Scholes benchmark); check the American call price equals the European call price for non-dividend-paying stock (no early exercise is ever optimal — this is a definitional check); verify the risk-neutral probability is between 0 and 1 for the given parameters; confirm the convergence table shows monotone approach to the Black-Scholes limit.
- Human supplies: Nothing — fully synthetic.
- Output medium: screen-recording mp4 (terminal showing the trees and convergence table) + Manim (animated forward tree branching, then backward option value tree)
- The change: Reprice as an American put (early exercise IS optimal for puts). Show the nodes where early exercise is optimal (American put value > Black-Scholes European put price). This is the case that the formula cannot handle — the binomial tree is the only tractable exact solution for American puts.
- Teardown angle: The binomial tree is not an approximation of the formula — the formula is the limit of the tree. The tree makes the logic of risk-neutral pricing explicit: at each node, the option value is the expected discounted value under the risk-neutral measure. The formula hides this logic in the integral; the tree makes it visible one step at a time.
- Exclusions: Trinomial trees, finite-difference methods, Longstaff-Schwartz Monte Carlo for American options.
- Score: 9/10

---

## Candidate 07 — "Build a Yield Curve from Zero Rates with Claude: Bootstrap the Risk-Free Term Structure"
- Source: computational-finance/chapters/02-chapter-01.md (placeholder — standard computational finance curriculum)
- Lane: BUILD (Claude Code)
- Hook: The yield curve is not observed — it is inferred. From a set of observable bond prices with different maturities, the bootstrapping algorithm recovers the zero-coupon yield at each maturity. Claude builds the bootstrapper; the yield curve is the artifact.
- The artifact: A Python script yield_curve.py that: (1) takes a set of observed coupon bond prices (face, coupon, maturity, price) as input; (2) bootstraps the zero-coupon yield curve by sequentially solving for zero rates at each maturity; (3) computes the discount factors; (4) prints a table: Maturity | Zero Rate | Discount Factor | Par Rate. A Manim animation shows the yield curve drawing from left to right as each zero rate is bootstrapped, with the original observed bond yields plotted as dots alongside the bootstrapped curve.
- Prompt seed: `claude "Write yield_curve.py that bootstraps a zero-coupon yield curve from coupon bonds. Input: a list of (face, coupon_rate, maturity_years, observed_price) tuples. Algorithm: (1) for the 1-year bond: solve for zero rate z₁ from P=F×(1+c)/(1+z₁); (2) for each subsequent maturity: solve for zₙ given all prior zero rates, using the present value equation that discounts each coupon at its maturity's zero rate. Print: Maturity | Zero Rate (%) | Discount Factor | Implied Par Rate. Demo bonds: [(100, 0.03, 1, 99.5), (100, 0.04, 2, 99.2), (100, 0.045, 3, 99.0), (100, 0.05, 5, 98.5), (100, 0.055, 10, 96.0)]."`
- Read / check: Verify the 1-year zero rate is close to 3.5% (back-calculate from the 1-year bond price: P=103/99.5, z₁≈3.5%); check the 10-year zero rate is plausible (should exceed the 10-year coupon bond's yield-to-maturity due to the upward slope); verify discount factors are less than 1 and decreasing with maturity; confirm the par rates are interpolated correctly.
- Human supplies: Nothing — fully synthetic for the demo. Real treasury bond prices from the Fed's website (freely available) can replace the synthetic inputs and produce a real yield curve.
- Output medium: screen-recording mp4 (terminal showing the bootstrapping table) + Manim (animated yield curve drawing from left to right)
- The change: Add forward rate extraction: given the zero rates, compute the implied forward rate for each period (f(t, t+1)). Show the forward curve alongside the zero curve and the par curve in a single Manim plot — the three curves that characterize the complete term structure.
- Teardown angle: The yield curve is not a price — it is a model of time value of money across maturities. Every derivative pricing model needs a yield curve as input. The bootstrapping algorithm recovers the zero curve from observable market prices without assuming any shape for the curve — it is the most model-free inference in fixed income.
- Exclusions: Nelson-Siegel fitting, cubic spline interpolation for the full curve, negative interest rate environments, multi-curve frameworks (post-2008 OIS vs. LIBOR).
- Score: 8/10

---

## Candidate 08 — "Compute Stock Correlations with Claude: When Diversification Fails"
- Source: computational-finance/chapters/02-chapter-01.md (placeholder — standard computational finance curriculum)
- Lane: BUILD (Claude Code)
- Hook: Diversification works when assets move independently. In a market crash, correlations spike to near 1 — every asset falls together. Claude computes rolling correlations to show exactly when diversification fails and why.
- The artifact: A Python script rolling_correlation.py that: (1) downloads historical price data for 5 assets (using yfinance or synthetic GBM paths); (2) computes daily log returns; (3) computes a 60-day rolling correlation between all pairs; (4) prints a heatmap of average correlation during normal periods vs. crisis periods (manually define 2-3 crisis windows); (5) plots the time series of one specific pair's rolling correlation to show the crisis spike. A Manim animation shows the correlation matrix heatmap morphing from "normal" to "crisis" colors as the time window shifts into a crisis period.
- Prompt seed: `claude "Write rolling_correlation.py that: (1) generates 5 years of synthetic daily returns for 5 assets using GBM with μ=[0.08,0.10,0.06,0.09,0.07]/252, σ=[0.15,0.20,0.12,0.18,0.14]/sqrt(252), and a correlation matrix with off-diagonal values around 0.3 (normal regime); (2) injects a 30-day crisis period where all pairwise correlations spike to 0.85; (3) computes 60-day rolling correlations for all 10 pairs; (4) prints average correlation for normal vs. crisis periods; (5) plots the time series of pair (0,1) rolling correlation highlighting the crisis period."`
- Read / check: Verify the average normal-period correlation is close to 0.3 (from the input parameters); check the crisis-period average correlation is substantially higher (should be near 0.85 from the injected crisis); verify the rolling correlation time series shows a clear spike during the crisis window; confirm the heatmap colors shift from cool (low correlation) to warm (high correlation) during the crisis.
- Human supplies: Nothing required for the synthetic demo. For real use, actual stock return data from yfinance (free, public API) can replace the synthetic returns — the correlation code is identical and produces real results.
- Output medium: screen-recording mp4 (terminal showing the correlation comparison table) + Manim (animated correlation heatmap morphing from normal to crisis)
- The change: Show the practical impact: a portfolio with 5 assets at 30% average correlation has substantially lower variance than the same portfolio at 85% average correlation. Compute both portfolio variances and show the diversification benefit evaporating in the crisis. This is why "flight to safety" happens — when everything falls together, no portfolio is safe.
- Teardown angle: Diversification is not free risk reduction — it is correlation-dependent risk reduction. When correlations are low, diversification works exactly as Markowitz promised. When correlations spike, it stops working at the worst possible moment. Rolling correlation is the monitor that shows you when your diversification benefit is degrading before the loss shows up in the portfolio value.
- Exclusions: Dynamic conditional correlation (DCC) models, copula-based correlation, correlation vs. dependence in tail events, factor model correlation structure.
- Score: 8/10
