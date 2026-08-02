# Chapter 14 — Regression Analysis in Finance

*The one regression that prices risk — and why two identical stocks can command completely different valuations.*

---

Two stocks. Both expect 10% returns. Both have similar earnings and similar growth. By every superficial measure, they should trade at the same price-to-earnings multiple.

They don't. One trades at a P/E of 15. The other at 25.

Why?

The market is doing something that the summary statistics from Chapter 13 don't capture. It's pricing *risk* — but not total risk. Specifically, it's pricing the risk that cannot be diversified away. If you hold a large portfolio of stocks, the firm-specific disasters — a product recall, a CEO scandal, a surprise accounting restatement — tend to cancel out across companies. What doesn't cancel out is the shared exposure to broad economic conditions: recessions, interest rate shocks, financial crises. That's the risk that survives diversification.

A stock whose returns are tightly tied to market-wide movements contributes more of that inescapable risk to a portfolio than a stock that mostly bounces around for its own idiosyncratic reasons. The market prices this. The first stock must promise higher expected returns to compensate investors for the higher systematic risk they're accepting. The second — with its mostly diversifiable risk — is less threatening to a portfolio and commands a lower return premium.

To measure this distinction, finance uses one specific regression: a stock's monthly returns regressed on the market's monthly returns. The slope of that regression is the stock's **beta**. And beta, plugged into the Capital Asset Pricing Model, becomes the cost of equity — the discount rate used in every DCF we've built.

That's the chapter.

---

## The regression machinery

Before getting to beta, install the tool.

**Ordinary least squares.** Given two series of data — call them $x$ and $y$ — we want the line $\hat{y} = a + bx$ that best fits the observed pairs. "Best fit" means minimizing the sum of squared vertical distances between observed points and the line. The resulting formulas:

$$b = \frac{n\sum xy - (\sum x)(\sum y)}{n\sum x^2 - (\sum x)^2}$$

$$a = \bar{y} - b\bar{x}$$

The slope $b$ tells you: when $x$ increases by one unit, the model predicts $y$ increases by $b$ units. The intercept $a$ tells you the predicted value of $y$ when $x = 0$.

In Excel: `=SLOPE(y_range, x_range)` and `=INTERCEPT(y_range, x_range)`. In Python or R: one line of code. The formula is the theory; the software is the arithmetic.

**R²: what fraction of the variance is explained.** The slope tells you the direction and magnitude of the relationship. R² tells you how *strong* the relationship is:

$$R^2 = r^2 = (\text{correlation coefficient})^2$$

R² ranges from 0 to 1. An R² of 0.6 means the regression line accounts for 60% of the total variation in $y$; the remaining 40% is noise — the gap between observed values and the line's predictions. For stock returns regressed on the market, R² typically falls between 0.3 and 0.7. A utility stock deeply tied to the broad economy might be at the high end; a biotech stock whose returns are dominated by clinical trial outcomes might be at the low end.

<!-- → [CHART: scatter plot of 60 months of a stock's returns (y-axis) vs. S&P 500 returns (x-axis), with the OLS regression line drawn through the points; two versions side-by-side — one with R² ≈ 0.6 (tight cluster around the line) and one with R² ≈ 0.2 (scattered cloud) — student should see at a glance what R² measures visually] -->

**Residuals.** The regression line is an approximation. The difference between an observed value and its predicted value is the residual: $\text{residual}_i = y_i - \hat{y}_i$. A positive residual means the actual exceeded the prediction; negative means the opposite. For the regression to be reliable, residuals should center on zero with no systematic pattern. In financial return data, they often don't — variance tends to cluster in high-volatility periods, a pattern called heteroskedasticity. That's a real problem, though practitioners usually proceed anyway on the grounds that beta estimates are useful even when technically imperfect.

**Significance.** A correlation — and therefore a regression slope — computed from finite data might look nonzero purely by chance. A useful rule of thumb: with $n$ paired observations, the correlation is statistically significant at roughly the 5% level if $|r| \geq 2/\sqrt{n}$. With 60 months of data, that threshold is $2/\sqrt{60} \approx 0.26$. Any beta regression run on 5 years of monthly data with a correlation above 0.26 is statistically distinguishable from zero.

---

## Beta: the slope that prices risk

**Beta is the slope of a stock's returns regressed on the market's returns.** That's the complete definition. Everything else is interpretation.

Mathematically:

$$\beta = \frac{\text{Cov}(R_\text{stock}, R_\text{market})}{\text{Var}(R_\text{market})}$$

This is identical to the OLS slope formula with $x = R_\text{market}$ and $y = R_\text{stock}$. In Excel: `=SLOPE(stock_returns, market_returns)`. Done.

What does the number mean?

| Beta | Stock behavior |
|---|---|
| $\beta = 0$ | Return uncorrelated with market |
| $\beta = 0.5$ | Moves half as much as the market |
| $\beta = 1.0$ | Moves one-for-one with the market |
| $\beta = 1.5$ | Amplifies market moves by 50% |
| $\beta = -0.3$ | Moves opposite the market (rare; gold sometimes shows this) |

Some approximate real-world examples: Walmart has historically had a beta around 0.5 — people buy groceries in recessions too, so it's less sensitive to economic cycles. Tesla has a beta around 2.0 — it amplifies market moves in both directions. Procter & Gamble sits near 0.4. Apple is closer to 1.2.

<!-- → [TABLE: beta values and interpretation for a set of real firms across industries — columns: firm, sector, approximate beta, interpretation of what the beta implies about the stock's behavior in a market downturn; student should see the pattern that defensive sectors cluster at low betas and cyclical/growth firms cluster at high betas] -->

**Why only beta is priced.** Total return variability decomposes into two parts. **Systematic risk** is the part correlated with the market — captured by beta. **Idiosyncratic risk** is the part specific to the individual firm. In a diversified portfolio, idiosyncratic risks from different companies partially offset each other. The larger the portfolio, the more they cancel. A portfolio of 50 uncorrelated stocks has essentially zero idiosyncratic risk remaining.

What doesn't cancel is systematic risk. Market crashes hit every stock simultaneously, regardless of how diversified you are. The market — pricing what rational, diversified investors will pay — compensates investors for the risk they can't escape. The risk they *can* escape (idiosyncratic) doesn't command a premium, because a rational investor would diversify it away rather than pay to hold it.

Beta measures what remains after full diversification. That's what gets priced.

---

## CAPM: the equation that connects beta to cost of equity

The Capital Asset Pricing Model says an asset's expected return is determined by two things: the time value of money, and compensation for systematic risk.

$$\boxed{E[R_i] = R_f + \beta_i \times (E[R_m] - R_f)}$$

where:
- $R_f$ = the risk-free rate (typically the current 10-year Treasury yield)
- $\beta_i$ = the asset's beta
- $E[R_m] - R_f$ = the **equity risk premium** (ERP) — the expected return of the market above the risk-free rate

The logic: a zero-beta asset contributes no systematic risk to a portfolio and should earn exactly $R_f$ — the time-value-of-money component. A stock with $\beta = 1$ is as risky as the market and should earn the market return. A stock with $\beta = 1.5$ accepts 50% more systematic risk than the market and should earn 50% more than the equity risk premium, on top of the risk-free rate.

**A concrete calculation.** Nike's beta from an OLS regression of 13 months vs. the S&P 500: approximately 0.83. Current 10-year Treasury yield: 4.5%. Equity risk premium estimate: 5%.

$$E[R_\text{Nike}] = 4.5\% + 0.83 \times 5\% = 4.5\% + 4.15\% = 8.65\%$$

Nike's cost of equity, by CAPM, is about 8.65%. This is the discount rate to apply in a Nike DCF.

Now watch what happens when beta changes. A stock with $\beta = 1.5$:

$$E[R] = 4.5\% + 1.5 \times 5\% = 12\%$$

Higher cost of equity → higher discount rate → lower present value of the same future cash flows → lower stock price. This is the mechanism. Two firms with identical free cash flow projections will have different valuations if their betas differ, because the market demands more return to hold the riskier one. The same $100 of FCF a year from now is worth $100/1.0865 = \$92.03$ at an 8.65% discount rate, but only $100/1.12 = \$89.29$ at 12%. Multiply that difference across a five-year DCF and it produces a substantial valuation gap.

**The security market line.** CAPM has a clean graph. Plot expected return on the y-axis, beta on the x-axis. The CAPM equation is a straight line:
- Intercept: $R_f$ (a zero-beta asset earns only the risk-free rate).
- Slope: $E[R_m] - R_f$ (the equity risk premium).
- The line passes through $(\beta = 1, R = E[R_m])$ — the market portfolio itself.

This line is the **security market line (SML)**. According to CAPM, every fairly priced security should sit on it. A security above the SML offers more expected return than its beta predicts — it's relatively cheap. One below the SML offers less expected return than its beta predicts — it's relatively expensive. In equilibrium, the argument goes, investors would bid up underpriced securities and bid down overpriced ones until all of them land on the line.

<!-- → [CHART: security market line — x-axis: beta from 0 to 2.0, y-axis: expected return; line starting at R_f (y-intercept), passing through the market portfolio at beta=1; two labeled points: one above the SML (underpriced security) and one below (overpriced); caption explaining that the vertical distance from the SML is alpha] -->

**Alpha.** In the regression equation:

$$R_\text{stock} = \alpha + \beta \times R_\text{market} + \text{error}$$

the slope is beta and the intercept is **alpha**. If CAPM holds perfectly, $\alpha = 0$: the stock's return is fully explained by its market exposure. A positive alpha means the stock has earned more than CAPM predicts — it has outperformed on a risk-adjusted basis. A negative alpha means it has underperformed.

For active fund managers, generating positive alpha is the explicit goal. The empirical record is sobering: most active managers do not produce positive alpha consistently after fees. The few who do over long horizons — Buffett across five decades, Renaissance Technologies' Medallion Fund — are genuine exceptions, and even distinguishing skill from luck in those cases requires careful analysis.

For the equity research project: your company's historical alpha is worth noting, but it is a weak predictor of future alpha. The number tells you how the stock performed relative to CAPM expectations over the regression window. It doesn't tell you what comes next.

---

## Limitations of CAPM — and why it's still used

CAPM is a model, which means it is wrong in specific, well-understood ways.

**Single factor.** CAPM says beta — market exposure — is the only priced risk. Forty years of empirical work (Fama and French since the early 1990s) has shown that other factors also explain returns: firm size (small-cap stocks have historically outperformed large-caps beyond what beta predicts), value (high book-to-market stocks have outperformed), momentum, profitability, investment intensity. These factors are not in CAPM. Multi-factor models capture them; CAPM misses them.

**Beta is unstable.** A regression over 2018–2019 can produce a very different beta than a regression over 2022–2023 for the same firm. A company undergoing a strategic pivot — expanding from a defensive consumer-staples business into a higher-growth segment, say — will have a beta that is changing. Historical beta is a lagging indicator of a forward-looking question.

**The equity risk premium is uncertain.** Chapter 12 established that reasonable ERP estimates range from 4% to 7% depending on methodology and time horizon. CAPM's output is proportional to ERP. A one-percentage-point difference in ERP moves the cost of equity by one full beta-unit. For a high-beta stock, that's a 1.5-point swing in cost of equity, which cascades into a meaningful valuation difference.

**Forward vs. backward.** Beta is computed from historical data and used as a forward expectation. These are not the same thing.

So why does every finance course still teach CAPM?

Because the alternatives are more complex without being clearly more accurate. Fama-French three-factor and five-factor models require additional factor return data, additional factor loadings, and additional assumptions about how many factors are "real." Implied-cost-of-capital methods (which back out the discount rate from current prices and analyst consensus forecasts) require trusting the consensus. In practice, after running all these approaches with their respective uncertainty, you typically end up with a range that overlaps substantially with a well-run CAPM plus sensitivity analysis.

CAPM is also transparent. Every assumption is visible. The inputs are few. Sensitivity analysis is straightforward. For introductory equity research, transparency plus sensitivity is more useful than complexity plus false precision.

The right practice: use CAPM, be explicit about every assumption, and report a range rather than a point estimate.

---

## Building the cost of equity for the project

The machinery is in place. Here is the practical procedure.

**Step 1: pull return data.** Five years of monthly returns for your company. Five years of monthly returns for the S&P 500 (or whichever broad market index you're using). Sixty pairs of observations. Yahoo Finance provides this; so do most financial data providers.

**Step 2: run the regression.** In Excel:
- `=SLOPE(stock_returns, market_returns)` → beta
- `=INTERCEPT(stock_returns, market_returns)` → alpha (monthly; multiply by 12 for an approximate annualized figure)
- `=RSQ(stock_returns, market_returns)` → R²

Compare your beta to the published figure on Yahoo Finance or Bloomberg. Differences of 0.1–0.2 are common (different time windows, different market indices). Differences above 0.3 warrant investigation: check for data errors or see whether the published source uses a fundamentally different methodology.

**Step 3: apply CAPM.** Use the current 10-year Treasury yield as $R_f$. Use 4.5–5.5% as your ERP estimate. Compute:

$$\text{Cost of equity} = R_f + \beta \times \text{ERP}$$

**Step 4: sensitivity analysis.** Recompute with beta ± 0.2 and ERP at 4%, 5%, 6%. You'll get a range of six or nine cost-of-equity estimates. Report the range, not a single number. The range is the honest answer; the single number is an illusion of precision.

**Step 5: interpret R².** If R² is 0.5, the market explains 50% of your stock's monthly return variation; the other 50% is idiosyncratic. If R² is 0.2, the market explains only a fifth of the variation — beta is estimated noisily and single-factor CAPM may be leaving important risk factors unaccounted for. Either way, report R² alongside beta. It tells the reader how much faith to put in the slope estimate.

**A worked illustration.** Suppose your company's 5-year regression produces beta = 1.15, alpha = 0.002 per month (≈ 2.4% annualized), R² = 0.45. With $R_f = 4.5\%$ and ERP = 5%:

$$\text{Cost of equity} = 4.5\% + 1.15 \times 5\% = 10.25\%$$

Sensitivity:

| | ERP = 4% | ERP = 5% | ERP = 6% |
|---|---|---|---|
| Beta = 0.95 | 8.3% | 9.25% | 10.2% |
| Beta = 1.15 | 9.1% | 10.25% | 11.4% |
| Beta = 1.35 | 9.9% | 11.25% | 12.6% |

The range across plausible assumptions: 8.3% to 12.6%. In your DCF, test sensitivity at both ends. Whatever conclusions you draw about the company's valuation should survive the full range.

<!-- → [TABLE: cost-of-equity sensitivity grid — rows: beta (0.7, 0.9, 1.1, 1.3, 1.5), columns: ERP (4%, 5%, 6%), with R_f = 4.5% fixed; each cell shows the resulting cost of equity; caption notes that the range within any plausible beta × ERP combination spans 3-5 percentage points, which is why reporting a single number is overconfident] -->

The cost of equity flows into Chapter 17's WACC computation, which in turn flows into the DCF discount rate. The number you just computed is the most consequential single input in the equity research report. Handle it with appropriate uncertainty.

---

## Exercises

### Warm-up

**14.1** Define beta in one sentence. Then explain in plain English — without using the word "covariance" — what a beta of 1.5 means for a stock held in a diversified portfolio.
*(Tests: conceptual grasp of beta beyond its formula)*

**14.2** Explain the difference between systematic risk and idiosyncratic risk. Why does the market price only the first one? What assumption about investor behavior underlies this claim?
*(Tests: the portfolio-diversification logic that gives beta its meaning)*

**14.3** Write the CAPM equation. Define every variable. A firm has beta = 0.8, the risk-free rate is 4%, and the equity risk premium is 5%. Compute the cost of equity.
*(Tests: basic CAPM application)*

### Application

**14.4** A regression of a stock's monthly returns on the S&P 500's monthly returns produces the following results:
- Slope (beta): 1.35
- Intercept (alpha, monthly): 0.0025
- R²: 0.48

(a) Interpret the beta in plain English: what does this stock do when the market rises 10%?
(b) What is the annualized alpha? Has this stock historically outperformed or underperformed CAPM expectations?
(c) What percentage of this stock's monthly return variance is explained by market movements? What accounts for the rest?
(d) Using $R_f = 4.5\%$ and ERP = 5%, compute the cost of equity.
(e) If R² were 0.15 instead of 0.48, would you trust this beta more or less? Why?

*(Tests: regression output interpretation, CAPM application, and the diagnostic use of R²)*

**14.5** Two firms operate in the same industry with nearly identical business models. Firm A has been financed entirely with equity; Firm B has 40% debt in its capital structure. Both have an unlevered beta of 0.9.

(a) Explain qualitatively why Firm B should have a higher equity beta than Firm A.
(b) If the corporate tax rate is 25% and Firm B's debt-to-equity ratio is 0.67, use the Hamada equation ($\beta_L = \beta_U \times (1 + (1-T) \times D/E)$) to compute Firm B's levered beta.
(c) Compute the cost of equity for each firm using CAPM ($R_f = 4\%$, ERP = 5%).
(d) Why would you want to "unlever" a comparable firm's beta before applying it to a firm with a different capital structure?

*(Tests: the relationship between leverage and beta, the Hamada equation, and re-levering for project analysis)*

**14.6** Pull 60 months of monthly return data for your chosen company and the S&P 500. In Excel (or Python), compute:
(a) Beta using `=SLOPE`.
(b) Alpha (monthly) using `=INTERCEPT`. Annualize it.
(c) R² using `=RSQ`.
(d) Compare your beta to the published value on Yahoo Finance. If they differ by more than 0.2, identify one plausible reason.

*(Tests: hands-on regression computation from primary-source return data)*

### Synthesis

**14.7** Build the full sensitivity table for your company's cost of equity: beta at your estimated value ± 0.2 (three rows), ERP at 4%, 5%, 6% (three columns). Report nine cost-of-equity estimates. Then identify which cell most closely matches the 8% WACC placeholder used in Chapter 11's DCF, and explain what assumption that implies about ERP and beta.
*(Tests: sensitivity analysis, CAPM application, and connecting the cost-of-equity output to the DCF built in Chapter 11)*

**14.8** A friend argues: "Beta is computed from historical data that reflects what the firm used to be. Why would I use it to discount what the firm will be?" Construct a three-part response: (a) why historical beta, despite its flaws, is still informative; (b) two specific circumstances where a historical beta would be particularly misleading; (c) what you would do differently in those two circumstances.
*(Tests: critical evaluation of beta's limitations and the analytical judgment required to apply it responsibly)*

### Challenge

**14.9** Your chosen company is planning a major acquisition in a different industry. The target firm operates in a sector with an average beta of 1.6, while your company's current beta is 0.9. After the acquisition, the combined firm will derive approximately 30% of its revenue from the acquired business.

(a) Estimate the post-acquisition beta of the combined firm as a weighted average of the two betas (by revenue contribution).
(b) Recompute the cost of equity for the combined firm using CAPM.
(c) How does this change your DCF valuation — does the acquisition appear more or less attractive after adjusting the discount rate?
(d) What limitations does this beta-blending approach have, and what would a more rigorous analysis require?

*(Tests: beta adjustment for corporate transactions, the impact of discount-rate changes on valuation, and honest acknowledgment of model limits)*

**14.10** The Fama-French three-factor model extends CAPM by adding size and value factors:

$$E[R_i] = R_f + \beta_\text{market}(R_m - R_f) + \beta_\text{size} \cdot SMB + \beta_\text{value} \cdot HML$$

where SMB (small-minus-big) and HML (high-minus-low book-to-market) are factor return series available from Kenneth French's data library.

(a) Explain what the size premium (SMB) and value premium (HML) represent economically. What is the proposed explanation for why each earns a return premium?
(b) For your chosen company, state whether you would expect positive or negative loadings on SMB and HML based on what you know about the firm's size and valuation multiple. Justify your expectation.
(c) If you had access to the factor data, describe step by step how you would run the three-factor regression and what you would compare to the single-factor CAPM result.
(d) Under what circumstances would a three-factor cost of equity be meaningfully different from the CAPM cost of equity — and in which direction?

*(Tests: conceptual understanding of factor models, the ability to reason about factor loadings from firm characteristics, and the analytical gap between CAPM and more complete asset-pricing models)*

---

## What would change my mind

The chapter argues that CAPM is the right baseline model for cost of equity, with sensitivity analysis to handle its limitations. Two things would revise this. First, if Fama-French multi-factor models became the introductory standard — which may happen eventually, as computing access to factor data improves — the single-factor framework here would feel incomplete. Second, if implied-cost-of-capital methods (backing out cost of equity from current prices and forecasts) consistently demonstrated superior forecasting accuracy in peer-reviewed empirical work, there would be a strong argument to teach that approach instead. Neither displacement has happened at the introductory level. CAPM plus sensitivity remains the standard.

## Still puzzling

The question I haven't resolved cleanly: should historical beta be used as a forward expectation? The data reflects the firm's business as it *was* during the regression window — its leverage, its business mix, its competitive position. All of those can change. A firm that has added substantial debt since the regression window will have a higher forward beta than the historical one implies. Practitioners adjust using "Bayesian shrinkage" (pulling the estimate toward 1.0, the market average) or re-levering the beta using current capital structure. Neither approach fully resolves the fundamental problem that we're using backward-looking data to make a forward-looking judgment. The honest response is to be explicit about this, use sensitivity analysis to bound the uncertainty, and resist the temptation to report a single beta as though it were a known quantity.

---

## Connections forward

- **Chapter 15** applies beta and the cost of equity to investment decisions.
- **Chapter 17** combines cost of equity with cost of debt to compute WACC.
- **Chapter 18** uses WACC as the discount rate in the firm's pro forma forecasts.
- **Chapter 20** revisits beta and systematic risk in the context of risk management.

---

## LLM Exercise — Chapter 14: Beta and Cost of Equity

**Project:** Equity Research Report on a Chosen Public Company
**What you're building this chapter:** Run the regression to extract beta, compute alpha and R², and apply CAPM to get the cost of equity. The cost of equity is the most-quoted discount-rate input for your DCF.
**Tool:** Excel (using `=SLOPE`, `=INTERCEPT`, `=RSQ`) or Python.

### Setup

Use the 60 monthly returns from Chapter 12 — your company's and the S&P 500's.

### The Prompt

```
For [your company], using the 60 months of paired return data:

1. **Run the OLS regression** of your company's returns on the S&P 500's returns:
   - In Excel: =SLOPE(stock_returns, market_returns) for beta
   - =INTERCEPT(stock_returns, market_returns) for alpha (monthly)
   - =RSQ(stock_returns, market_returns) for R²
   - In Python: use scipy.stats.linregress or np.polyfit

2. **Report the results**:
   - Beta (the regression slope)
   - Alpha (the intercept; annualize by multiplying by 12 for the rough approximation)
   - R² (proportion of variance in your company's returns explained by the market)

3. **Verify the beta** — Compare to the published beta on Yahoo Finance, MarketWatch, or Bloomberg. Are they similar? If not (differences > 0.3 are common), note the discrepancy and explain potential causes (different time windows, different indexes).

4. **Apply CAPM** to compute the cost of equity:
   Cost of equity = R_f + β × ERP
   - R_f = 4.5% (current 10-year Treasury)
   - β = your computed value
   - ERP = 5% (forward-looking estimate; can use 4-6%)

5. **Run sensitivity** on cost of equity:
   - β ± 0.2
   - ERP at 4%, 5%, 6%
   Display the resulting cost-of-equity range.

6. **Compare to your DCF discount rate** — In Chapter 11, you used 8% as a placeholder for WACC. In Chapter 17, you'll combine this cost of equity with the cost of debt (from Chapter 10) to compute real WACC. For now, note whether your computed cost of equity (with no debt blending) is above or below 8%.

Show your work. Report the regression equation and R² explicitly.
```

### What this produces

The cost-of-equity input for your DCF. Combined with cost of debt from Chapter 10, this becomes WACC in Chapter 17. Updated DCF in Chapter 17 with real WACC.

### How to adapt this prompt

- *For your own company:* Replace [your company].
- *For ChatGPT / Gemini:* Identical.
- *For Claude Code:* Recommended. Three lines of Python compute beta, alpha, and R² from the return arrays.

### Connection to previous chapters

Synthesizes Chapters 12 (returns) and 13 (statistics). Feeds Chapter 17's WACC.

### Preview of next chapter

Chapter 15 examines personal investing. The Chapter 15 LLM Exercise asks: would *you* hold this stock?

---

**Tags:** regression, CAPM, beta, alpha, cost-of-equity, security-market-line, R-squared, OLS

---

## AI Wayback Machine

**William Sharpe** developed the Capital Asset Pricing Model — Nobel 1990.

**Run this:**

```
Who is William Sharpe, and how does their work connect to regression analysis in finance we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about their career or ideas.
```

→ Search **"William Sharpe"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to apply William Sharpe's framework to a specific finance question.
- Add a constraint: "Answer including criticisms or limits of William Sharpe's framework."

What changes? What gets better? What gets worse?
