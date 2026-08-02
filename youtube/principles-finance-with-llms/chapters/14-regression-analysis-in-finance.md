# Chapter 14 — Regression Analysis in Finance

**Suggested titles**
1. Beta, CAPM, and the Cost of Equity
2. The Slope That Sets the Discount Rate
3. From Correlation to Capital Cost

**TL;DR.** Regression analysis takes two return series and computes the line that best fits the relationship. In finance, the most important regression is one specific case: a stock's returns regressed on the market's returns. The slope of that regression is **beta** — the measure of systematic risk that drives the cost of equity through the **CAPM** equation. This chapter installs the regression machinery, computes beta, and uses it to build the cost-of-equity input the project needs for valuation.

---

## The puzzle of two stocks at the same return

Two stocks both have an expected return of 10% per year. Both have similar earnings and similar growth prospects. By any superficial measure, they should command the same valuation.

They don't. One trades at a P/E of 15, the other at a P/E of 25. Why?

The market is doing something the simple statistics from Chapter 13 don't capture. It's pricing risk — specifically, the kind of risk that *cannot be diversified away*. Stocks whose returns are highly tied to broad market movements (high **beta**) are riskier in a portfolio context than stocks whose returns are mostly idiosyncratic (low beta), because the latter's risk gets diluted in a diversified portfolio while the former's doesn't.

To measure this, finance uses regression analysis. Specifically: regress a stock's monthly returns on the market's monthly returns. The slope of that regression is the stock's beta. A beta of 1.0 means the stock moves one-for-one with the market. A beta of 0.5 means the stock moves half as much as the market — when the market is up 10%, the low-beta stock is up 5% on average. A beta of 1.8 means the stock amplifies market moves — up 18% when the market is up 10%.

Beta is the central output of this chapter. Combined with the risk-free rate and the equity risk premium (Chapter 12), it produces the **cost of equity** — the discount rate the market demands for that stock's risk profile. The Capital Asset Pricing Model (CAPM) is the equation that ties them together.

For the equity research project, this chapter delivers the discount-rate input to the DCF model from Chapter 11. Combined with Chapter 17's WACC computation, the cost of equity is the single most important number in the valuation.

---

## Learning objectives

After working through this chapter, you should be able to:

- Compute the correlation coefficient between two return series and test for significance.
- Compute the slope, intercept, and R² of a simple linear regression.
- Explain what beta measures and compute it as the slope of a stock's returns regressed on market returns.
- Apply CAPM to compute the cost of equity for a firm given beta, the risk-free rate, and the equity risk premium.
- Interpret R², alpha, and the security market line.
- Recognize the limitations of CAPM and beta in practice.

**Prerequisites.** Chapter 12 (historical returns), Chapter 13 (statistics).

---

## Concept 1 — Correlation and regression: the machinery

Before getting to beta and CAPM, install the basic regression machinery.

### Correlation

Chapter 13 introduced correlation as a measure of how two return series move together. The formula:

$$r = \frac{n\sum xy - (\sum x)(\sum y)}{\sqrt{n\sum x^2 - (\sum x)^2}\sqrt{n\sum y^2 - (\sum y)^2}}$$

Correlation $r$ ranges from -1 to +1. Two further moves matter for finance.

**Significance test.** Is the observed correlation strong enough to take seriously, or could it have arisen from random sampling? A useful rule of thumb: with $n$ observations, a correlation coefficient is statistically significant at roughly the 5% level if $|r| \geq 2/\sqrt{n}$. With 13 monthly observations, that threshold is $2/\sqrt{13} \approx 0.55$. With 60 monthly observations (5 years of monthly data), $0.26$.

For Nike vs. the S&P 500 over 13 months in 2020-2021, correlation was about 0.93 — highly significant.[^1]

[^1]: OpenStax data; `[verify]` for current vintage.

**Causation warning.** Correlation does not imply causation. The S&P 500 contains Nike, so Nike contributing to the index is mathematical rather than causal. More generally, two correlated time series can both be driven by a common third factor, or they can be coincidentally correlated in a small sample. The discipline is to never claim causal interpretation from correlation alone.

### Linear regression

If correlation is meaningful, the next step is to fit a line that captures the relationship:

$$\hat{y} = a + bx$$

where $\hat{y}$ is the predicted value of $y$ given $x$, $a$ is the intercept, and $b$ is the slope.

The line is chosen by **ordinary least squares (OLS)** — minimizing the sum of squared deviations between observed and predicted values. The formulas:

$$b = \frac{n\sum xy - (\sum x)(\sum y)}{n\sum x^2 - (\sum x)^2}$$

$$a = \bar{y} - b\bar{x}$$

In Excel: `=SLOPE(y_range, x_range)` and `=INTERCEPT(y_range, x_range)`. In R: `lm(y ~ x)`.

The slope $b$ measures how much $y$ changes for a one-unit change in $x$. The intercept $a$ is the predicted value of $y$ when $x = 0$.

### R²: how good is the fit?

The slope tells you the relationship's *direction*. R² (the coefficient of determination) tells you the relationship's *strength*.

$$R^2 = \frac{\text{Variance of } \hat{y}}{\text{Variance of } y}$$

Equivalently, R² = (correlation coefficient)². It ranges from 0 to 1.

- **R² = 1**: the regression line perfectly explains all variation in $y$. Every observed point is exactly on the line.
- **R² = 0**: the regression line explains no variation. The slope is essentially noise.
- **R² = 0.5**: the regression explains 50% of the variance in $y$.

For typical stock-vs.-market regressions, R² is in the 0.3 to 0.7 range — meaning 30% to 70% of a stock's return variation is explained by the market, and the remainder is firm-specific (idiosyncratic).

### Residuals

The regression line is an approximation. The difference between observed and predicted values is the **residual**:

$$\text{Residual}_i = y_i - \hat{y}_i$$

A positive residual means the actual value exceeded the prediction; negative means it fell short. For OLS to be valid, the residuals should be approximately:
- Centered on zero (no systematic bias).
- Normally distributed.
- Equal variance across the range of $x$ (homoskedastic).
- Independent of each other (no autocorrelation).

In practice, financial-return regressions often violate these assumptions to some degree. The most common failure: **heteroskedasticity** — variance of returns changes with market conditions. Robust techniques exist; we won't develop them here.

### Worked example — fitting a line

Suppose Nike's monthly returns over 13 months are $x = $ S&P 500 returns and $y = $ Nike returns. The OLS regression gives:

$$\hat{y}_\text{Nike} = a + b \cdot R_\text{S\&P}$$

with $b = 0.83, a = 0.005$ (illustrative).

This says: for each percentage point the S&P 500 moves, Nike moves about 0.83 percentage points in the same direction, plus a small constant offset. The slope $b = 0.83$ is **Nike's beta**.

If the regression's R² is 0.86, then 86% of Nike's monthly return variation is explained by the market.

↳ **Dig Deeper — Bayesian shrinkage and beta estimation**

*A historical beta from 60 monthly observations has substantial estimation error. One way practitioners adjust: shrink the estimate toward the market average of 1.0. The Blume adjustment (Blume 1975) and Vasicek shrinkage are two formal approaches. Bloomberg's "adjusted beta" applies a simple version.*

**Prompt:**
> Explain the rationale for Bayesian shrinkage of beta estimates. Walk through the Blume adjustment formula (β_adj = 0.67 × β_estimated + 0.33 × 1.0). Then explain why this might be appropriate even when the regression beta is statistically significant — what assumption is the shrinkage adding, and why might it improve forward forecasting accuracy?

**What to do with the output:** Save it. When your beta from Chapter 14's regression looks like an outlier (very high or very low), shrinkage is a defensible adjustment to consider.

### The trade-off (concept 1)

Regression trades **summary simplicity against fit quality**. A single line summarizes the relationship cleanly but never captures it perfectly. R² tells you how much of the data the line is missing. For most analytical purposes, an R² above 0.4-0.5 is enough to take the slope estimate seriously; below that, the relationship may be too noisy to use.

---

## Concept 2 — Beta: the slope that sets the cost of equity

Beta is the most-referenced number in equity research. It's also one of the most misunderstood. The technical definition is precise; the practical interpretation requires care.

### What beta measures

**Beta is the slope of a stock's returns regressed on the market's returns.**

$$\beta = \frac{\text{Cov}(R_\text{stock}, R_\text{market})}{\text{Var}(R_\text{market})}$$

This is mathematically identical to the OLS slope:

$$\beta = b = \frac{n\sum R_\text{stock} R_\text{market} - (\sum R_\text{stock})(\sum R_\text{market})}{n\sum R_\text{market}^2 - (\sum R_\text{market})^2}$$

In Excel, you compute beta with `=SLOPE(stock_returns, market_returns)`. In Yahoo Finance and most financial data providers, beta is precomputed and updated regularly.

**Interpreting beta:**

| Beta | Stock behavior |
|---|---|
| $\beta = 0$ | Uncorrelated with market |
| $\beta = 0.5$ | Moves half as much as market |
| $\beta = 1.0$ | Moves with the market (the market itself has β = 1) |
| $\beta = 1.5$ | Amplifies market moves by 50% |
| $\beta = -0.3$ | Moves opposite the market (rare; gold often shows this) |

Examples (approximate, vary over time):
- Walmart: beta around 0.5 — defensive stock, less volatile than the market.
- Apple: beta around 1.2 — slightly more volatile than market.
- Tesla: beta around 2.0 — substantially more volatile.
- Procter & Gamble: beta around 0.4 — defensive consumer staples.

### Why beta matters: systematic vs. idiosyncratic risk

Total return variability decomposes into two parts:

**Systematic (market) risk** — the part driven by broad market movements. Cannot be diversified away. *This is what beta captures.*

**Idiosyncratic (firm-specific) risk** — the part specific to the individual company. Largely diversified away in a portfolio of many stocks.

In a well-diversified portfolio, idiosyncratic risk is negligible. What's left is systematic risk. The market — a rational pricing mechanism in theory — should compensate investors only for systematic risk, since that's the risk they can't escape.

This is the central insight of the **Capital Asset Pricing Model (CAPM)**: an asset's expected return should be proportional to its beta.

### CAPM — the equation

$$E[R_i] = R_f + \beta_i \times (E[R_m] - R_f)$$

where:
- $E[R_i]$ = expected return on asset $i$ (the cost of equity)
- $R_f$ = risk-free rate (typically 10-year Treasury yield)
- $\beta_i$ = the asset's beta
- $E[R_m] - R_f$ = the equity risk premium (Chapter 12)

The intuition: an asset earns the risk-free rate (the time-value-of-money component) plus a premium proportional to its market exposure. A stock with $\beta = 0$ should earn just $R_f$. A stock with $\beta = 1$ should earn $R_f + ERP$ — exactly the market return. A stock with $\beta = 1.5$ should earn $R_f + 1.5 \times ERP$ — the risk-free rate plus 1.5 times the equity premium.

### Worked example — Nike's cost of equity

Nike's beta from our regression: 0.83.

Inputs:
- $R_f = 4.5\%$ (10-year Treasury yield, current vintage)
- $E[R_m] - R_f = 5\%$ (forward-looking equity risk premium estimate)

CAPM:
$$E[R_\text{Nike}] = 4.5\% + 0.83 \times 5\% = 4.5\% + 4.15\% = 8.65\%$$

Nike's cost of equity, by CAPM, is about 8.65%. This is the discount rate to use in a Nike DCF.

If Nike's beta were higher — say, 1.5 — the cost of equity would be:
$$4.5\% + 1.5 \times 5\% = 12\%$$

Higher cost of equity → higher discount rate in DCF → lower present value of future cash flows → lower implied stock price (all else equal). This is exactly why the same expected cash flow stream produces different valuations for different stocks. Beta is the bridge.

### The security market line

CAPM has a nice graphical representation. Plot expected return on the y-axis and beta on the x-axis. The CAPM equation traces a straight line:

- y-intercept: $R_f$ (the risk-free rate; corresponds to $\beta = 0$).
- Slope: $E[R_m] - R_f$ (the equity risk premium).
- The line passes through the point $(\beta = 1, R = E[R_m])$ — the market portfolio.

This line is the **security market line (SML)**. According to CAPM, every fairly-priced security should sit on the SML. Securities above the SML are underpriced (expected return is higher than CAPM predicts); securities below are overpriced.

### Alpha — the deviation from CAPM

In an OLS regression of stock returns on market returns:
- The slope is beta.
- The intercept is alpha.

$$R_\text{stock} = \alpha + \beta \times R_\text{market} + \text{error}$$

If CAPM holds perfectly, $\alpha = 0$ — the stock's return is fully explained by its market exposure plus the risk-free rate. A positive $\alpha$ means the stock has earned more than CAPM predicts. A negative $\alpha$ means it has earned less.

For active fund managers, generating positive alpha is the goal. The empirical record is humbling: most active managers do not consistently produce positive alpha after fees. The few who do (Buffett over 50+ years, Renaissance Technologies' Medallion Fund) are exceptional.

For the equity research project: when you compute your chosen company's regression vs. the S&P 500, the alpha tells you whether the stock has *historically* outperformed or underperformed CAPM expectations. This is suggestive but not predictive — historical alpha is a poor forecaster of future alpha.

### Limitations of CAPM and beta

CAPM is the workhorse model in finance, but it has well-known limits.

**Single-factor model.** CAPM assumes that beta captures all priced risk. Empirical research (Fama-French) shows that other factors — size, value, momentum, profitability — also explain return variation that beta misses.

**Beta is unstable.** A stock's beta calculated over different time windows can give different answers. Beta over 2018-2019 vs. beta over 2020-2021 can differ substantially. Practitioners typically use 3-5 years of monthly data and accept the noise.

**Equity premium is uncertain.** As we saw in Chapter 12, the equity risk premium is between 4% and 7% by most estimates, but the right number depends on the time horizon and methodology. CAPM's output is sensitive to this input.

**Forward vs. backward.** Beta is computed from historical data but used as a forward expectation. A firm whose business has materially changed (think: Tesla in 2015 vs. 2025) may have a beta that doesn't reflect its current risk profile.

For the project, use CAPM for the cost of equity but report a *range*. A point estimate is overconfident.

↳ **Dig Deeper — Fama-French three-factor and five-factor models**

*CAPM uses a single factor: market beta. Empirical work since the 1990s (Fama-French) has consistently found that two additional factors — size and value — also explain stock returns in ways CAPM misses. The five-factor extension (2015) adds profitability and investment factors. Multi-factor models are the academic standard now.*

**Prompt:**
> Explain the Fama-French three-factor model: market premium, size premium (small-minus-big), and value premium (high-minus-low book-to-market). Then describe what each factor represents economically and how it's measured. Briefly summarize the 2015 five-factor extension. Finally, run a hypothetical comparison: for a small-cap value stock, would CAPM under- or over-estimate its expected return?

**What to do with the output:** Save it. CAPM is the principles-course standard; multi-factor models are where the field actually is. Knowing both is part of being current.

### The trade-off (concept 2)

Beta trades **theoretical clarity against empirical messiness**. The CAPM model is mathematically elegant and connects asset pricing to portfolio theory cleanly. The actual application — historical beta from noisy data, forward expectations of an unstable premium, factors CAPM ignores — is much messier. Practitioners use CAPM despite its limits because the alternatives (multi-factor models, implied cost of capital methods) are more complex without being clearly more accurate.

### Common misconceptions

- *"Beta measures total risk."* It measures systematic risk only. The remainder (idiosyncratic) is captured by 1 − R². Total risk is standard deviation.
- *"A high beta means the stock is bad."* It means the stock is more market-sensitive. In an up-market, high-beta stocks outperform.
- *"Beta is constant."* It changes over time as the firm's business evolves.

---

## Concept 3 — Building the cost of equity for the project

The pieces from this chapter and earlier ones now combine into the practical cost-of-equity computation.

### Step 1: Pull return data

For your chosen company, pull 5 years of monthly returns. Pull the same 60 months of S&P 500 (or similar broad market index) returns. Yahoo Finance provides this; many other data sources do too.

### Step 2: Run the regression

In Excel:
- `=SLOPE(stock_returns, market_returns)` returns beta.
- `=INTERCEPT(stock_returns, market_returns)` returns alpha.
- `=RSQ(stock_returns, market_returns)` returns R².

Or in R:
```r
model <- lm(stock_returns ~ market_returns)
summary(model)
```

The output tells you:
- Beta (the slope).
- Alpha (the intercept).
- R² (how much of variance is explained by market).
- Statistical significance of beta (the t-statistic and p-value).

### Step 3: Apply CAPM

Use:
- Current 10-year Treasury yield as $R_f$.
- 4.5-5.5% as your equity risk premium estimate.
- The beta from your regression.

$$E[R_\text{stock}] = R_f + \beta \times (E[R_m] - R_f)$$

### Step 4: Sensitivity analysis

Recompute under alternative assumptions:
- ERP of 4%, 5%, 6%.
- Beta plus or minus 0.2 (acknowledging measurement error).

Report the range, not a single number.

### Step 5: Interpret the result

The cost of equity feeds into:
- WACC (Chapter 17).
- DCF discount rate (Chapter 11).
- The price-target calculation (Chapter 18).

A high cost of equity (say, 12-15%) means the stock has high systematic risk and the market demands high expected returns. Future cash flows are discounted aggressively. A low cost of equity (say, 6-8%) means low systematic risk; future cash flows are discounted gently and the stock is more valuable for the same cash flow stream.

### Worked example — applying it to a real firm

Suppose your chosen company's 5-year monthly regression vs. the S&P 500 produces:
- Beta = 1.15
- Alpha = 0.002 per month (2.4% annualized; positive — the firm has slightly outperformed CAPM expectations)
- R² = 0.45 (45% of monthly variance explained by market; remaining 55% is idiosyncratic)

With $R_f = 4.5\%$ and ERP = 5%:

$$E[R_\text{stock}] = 4.5\% + 1.15 \times 5\% = 10.25\%$$

Sensitivity:
- ERP = 4%: cost of equity = 4.5 + 1.15 × 4 = 9.1%
- ERP = 6%: cost of equity = 4.5 + 1.15 × 6 = 11.4%
- Beta = 0.95: cost of equity = 4.5 + 0.95 × 5 = 9.25%
- Beta = 1.35: cost of equity = 4.5 + 1.35 × 5 = 11.25%

So the cost-of-equity range across reasonable assumptions is roughly 9% to 11.5%. In your DCF, test sensitivity at both ends.

### What to do with R²

If R² is low (say, 0.2), the regression is not capturing much of your firm's return variability. The implications:
- Beta estimate is noisy. Use it cautiously.
- The firm has substantial idiosyncratic risk. Diversification benefits to a portfolio holder are large.
- Single-factor CAPM may be missing important factors. Multi-factor models (Fama-French) might give better answers.

For the project, just report R² alongside beta. A reader who's done equity research will understand the implications.

### The trade-off (concept 3)

Building the cost of equity trades **theoretical purity against practical decision-making**. CAPM is elegant in theory; in practice, there are many judgment calls (which time window, which index, which equity premium). The right approach is to be transparent about the choices, run sensitivity, and present a defensible range. The number in your DCF should be one input among others, not the answer to everything.

### Common misconceptions

- *"The cost of equity is what shareholders demand."* It's what the *market* demands, as inferred from CAPM and the firm's beta. Individual shareholders' personal demands can be quite different.
- *"Higher beta always means higher returns."* Higher beta means *higher expected returns*, on average, over time. Realized returns can deviate substantially in any given period.

---

## Synthesis — regression, beta, CAPM, and the discount rate

The chapter built up regression analysis from the basic correlation calculation, through OLS slope and intercept, to beta and CAPM. The end product is a single number: the cost of equity for your chosen company.

That cost of equity is the discount rate the market demands for the stock's risk profile. It's the input to every DCF in the next several chapters.

The Capital Asset Pricing Model is the bridge between observed return data and the discount rate. Its limits are real — single factor, unstable beta, uncertain equity premium — but it remains the dominant model in equity research. Sensitivity analysis is what makes it usable in practice.

For the equity research project, the deliverable from this chapter is:
1. Beta computed from 5 years of monthly regressions.
2. R² and alpha reported alongside.
3. Cost of equity computed via CAPM, with a sensitivity range.
4. Comparison to peer-firm betas and costs of equity.

Chapter 17 will integrate the cost of equity with the cost of debt to compute WACC. Chapter 11's DCF will use WACC as the discount rate.

---

## Exercises

### Warm-up

**14.1** Define correlation. Define R². How are they mathematically related?

**14.2** Write the regression equation $\hat{y} = a + bx$. Define each term. What do the slope and intercept mean?

**14.3** Define beta. Define alpha. What does each measure?

### Application

**14.4** A regression of a stock's monthly returns on the market's returns produces:
- Slope = 1.20
- Intercept = 0.001 (per month)
- R² = 0.55

Compute:
(a) The stock's beta.
(b) The annualized alpha.
(c) The percentage of monthly return variance explained by the market.
(d) The cost of equity using $R_f = 4.5\%$ and ERP = 5%.

**14.5** Pull 5 years of monthly returns for your chosen company and the S&P 500. Compute beta, alpha, and R². Compare beta to a published source (Yahoo Finance, Bloomberg). Are they similar? If not, what could explain the difference?

**14.6** Using your computed beta and a reasonable risk-free rate and equity premium, compute the cost of equity for your company. Run sensitivity for $\pm 0.2$ on beta and $\pm 1$ percentage point on ERP. Report the range.

### Synthesis

**14.7** Apple's beta has historically been around 1.1-1.3. Walmart's around 0.4-0.6. Construct (a) why these levels make sense given each firm's business model, (b) what implications they have for cost of equity, (c) what implications they have for the relative attractiveness of the two firms in a recession.

**14.8** A friend says: "If beta is so noisy and CAPM is missing important factors, why does anyone use it?" Construct a defense in three parts: (a) what CAPM gets right that simpler approaches miss; (b) why the alternatives (multi-factor models, ICC) aren't always better; (c) the role of sensitivity analysis in honest application.

### Challenge

**14.9** Run a regression of your chosen company's monthly returns on:
(a) The S&P 500 returns alone (single-factor CAPM).
(b) The S&P 500 returns + a "size" factor (small-cap minus large-cap returns).
(c) The S&P 500 returns + size + a "value" factor (high book-to-market minus low book-to-market).

Compare the R² across the three regressions. Does adding factors help? What does it tell you about the firm's risk profile?

**14.10** Compute alpha for a recent hedge fund (or portfolio manager you can find return data for). Is it positive or negative? Statistically significant? What does the answer suggest about the manager's stock-picking skill — keeping in mind the limits of single-factor CAPM and the noise inherent in alpha estimates?

---

## Chapter summary

- **Correlation** measures linear association; **regression** fits a line to two-variable data via OLS.
- The regression equation $\hat{y} = a + bx$ has slope $b$ and intercept $a$. R² measures how much of $y$'s variance the line explains.
- **Beta** is the slope of a stock's returns regressed on market returns. Measures systematic risk.
- **CAPM**: $E[R_i] = R_f + \beta_i (E[R_m] - R_f)$. Computes the cost of equity from beta and the equity premium.
- **Alpha** is the regression intercept — the deviation from CAPM expectations.
- The **security market line** is the graphical CAPM: expected return as a function of beta.
- CAPM has known limits: single-factor, unstable beta, uncertain equity premium. Sensitivity analysis is essential.

---

## What would change my mind

The chapter argues that CAPM is the right baseline model for cost of equity, with sensitivity analysis to handle its limitations. The reading would have to revise if (a) Fama-French or other multi-factor models became standard in undergraduate finance teaching (they may, eventually), or (b) implied-cost-of-capital methods (which back out cost of equity from current price + analyst consensus) consistently outperformed CAPM in forecasting future returns. Both are real alternatives; neither has displaced CAPM as the introductory standard.

## Still puzzling

The cleanest unresolved question: *should historical beta be used as a forward expectation?* The data is what it is — a stock's last 5 years of regression slope. But that 5-year slope reflects the firm's business as it was, not necessarily as it will be. Tesla's beta in 2018 is not Tesla's beta in 2025. Practitioners adjust for this with "Bayesian shrinkage" toward 1.0 (the market average) or by using a longer time window. Neither solution is fully satisfying. The honest framework is: historical beta is your best available estimate, but it's an estimate, and forward beta may be different.

---

## Connections forward

- **Chapter 15** applies beta and the cost of equity to investment decisions.
- **Chapter 17** combines cost of equity with cost of debt to compute WACC.
- **Chapter 18** uses WACC as the discount rate in the firm's pro forma forecasts.
- **Chapter 20** revisits beta and systematic risk in the context of risk management.

---

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

**William Sharpe** was developed the Capital Asset Pricing Model — Nobel 1990.

**Run this:**

```
Who is William Sharpe, and how does their work connect to regression analysis in finance we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about their career or ideas.
```

→ Search **"William Sharpe"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to apply William Sharpe's framework to a specific finance question.
- Add a constraint: "Answer including criticisms or limits of William Sharpe's framework."

What changes? What gets better? What gets worse?
