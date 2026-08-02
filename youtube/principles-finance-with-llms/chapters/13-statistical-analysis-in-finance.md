# Chapter 13 — Statistical Analysis in Finance

**Suggested titles**
1. Measuring Risk
2. Mean, Variance, Sharpe
3. The Statistics That Matter for Returns

**TL;DR.** A single year's return tells you almost nothing about an investment. To say something meaningful, you need statistics on a *sample* of returns: a measure of the center (the average return), a measure of the spread (the variance or standard deviation), and a measure of the relationship to other returns (covariance, correlation). This chapter installs those tools and applies them to the problem of measuring an investment's risk-adjusted performance via the Sharpe ratio.

---

## The puzzle of the single year

A friend tells you about an investment that returned 22% last year. Should you put your money in it?

You don't know yet. The 22% is one data point. The investment might typically return 15% — last year was a lucky one. It might typically return 25% — last year was a bad year by its standards. It might be a wild ride that returned -30% the year before and +22% last year (averaging ~ -4%). The single number, by itself, tells you almost nothing about what to expect going forward.

To say something useful about an investment, you need a *sample* of its returns over time. Then you can compute statistics: the typical return (the mean), how much it varies year to year (the standard deviation), and how it relates to other investments (the covariance and correlation).

This chapter installs those statistical tools. They are the language of risk in modern finance. Beta, Sharpe ratio, value-at-risk, portfolio optimization — all of them are built from the basic statistics here.

For the equity research project, this chapter does something concrete: it teaches you to compute the mean, variance, and Sharpe ratio of your chosen company's returns, and to compare those to the broader market. Chapter 14 then takes the next step — running a regression to extract beta — which feeds directly into the cost-of-equity calculation in Chapter 17.

---

## Learning objectives

After working through this chapter, you should be able to:

- Compute the **arithmetic mean** and **geometric mean** of a return series, and explain when each is appropriate.
- Compute the **variance** and **standard deviation** of a return series.
- Distinguish **covariance** from **correlation** and explain what each measures.
- Apply the **normal distribution** to financial returns, including computing the probability of returns within a given range.
- Compute the **Sharpe ratio** for a portfolio and explain what it means.
- Recognize where the normal-distribution assumption fails in financial markets (fat tails, skewness).

**Prerequisites.** Chapter 12 (historical returns). Comfort with summation notation and basic algebra.

---

## Concept 1 — Measuring the center

The first question to ask of a return series is "what's typical?" Three measures of central tendency answer this differently.

### The arithmetic mean

The arithmetic mean is the simple average:

$$\bar{R} = \frac{1}{n}\sum_{i=1}^{n} R_i$$

where $R_i$ is the return in period $i$ and $n$ is the number of periods.

Example: A stock returns 10%, -5%, 15%, 20%, -10% over five years. The arithmetic mean is:

$$\bar{R} = \frac{10 - 5 + 15 + 20 - 10}{5} = \frac{30}{5} = 6\%$$

The arithmetic mean is what most people mean by "average return." It is the right answer if you ask "what return should I expect *next year*, on average?"

It is the *wrong* answer if you ask "what cumulative return did I actually earn over the five years?" For that, you need the geometric mean.

### The geometric mean

For a multi-period investment with compounding, the geometric mean gives the constant rate that produces the same cumulative return as the actual sequence:

$$\bar{R}_{\text{geo}} = \left[\prod_{i=1}^{n}(1 + R_i)\right]^{1/n} - 1$$

For the same return series (10%, -5%, 15%, 20%, -10%):

$$\bar{R}_{\text{geo}} = (1.10 \times 0.95 \times 1.15 \times 1.20 \times 0.90)^{1/5} - 1$$

$$= (1.3680)^{0.2} - 1 = 1.0648 - 1 = 6.48\%$$

Wait. The arithmetic mean was 6%, but the geometric mean is 6.48%? That seems wrong. Geometric mean should be *lower* than arithmetic mean.

Let me redo with cleaner numbers. Take 50% one year, then -50% the next.

- Arithmetic mean: $(50 - 50)/2 = 0\%$
- Geometric mean: $(1.50 \times 0.50)^{1/2} - 1 = (0.75)^{0.5} - 1 = -13.4\%$

Now we see it. If you start with $100, gain 50% (to $150), then lose 50% (to $75), you've lost 25% over two years. The arithmetic mean of zero falsely suggests you broke even. The geometric mean of -13.4% correctly captures the actual cumulative loss.

(My earlier example had positive numbers throughout; let me recompute carefully.)

For 10%, -5%, 15%, 20%, -10%:
- Arithmetic: 6.0%
- Geometric: $(1.10 \times 0.95 \times 1.15 \times 1.20 \times 0.90)^{1/5} - 1$
- Product: $1.10 \times 0.95 = 1.045$; $\times 1.15 = 1.20175$; $\times 1.20 = 1.4421$; $\times 0.90 = 1.29789$
- $(1.29789)^{0.2} - 1 = 1.0537 - 1 = 5.37\%$

That's lower than the arithmetic mean of 6.0%, as expected. (My earlier arithmetic was sloppy; geometric mean is *always* less than or equal to arithmetic mean for any return series with non-zero variance.)

The relationship:

$$\bar{R}_{\text{geo}} \approx \bar{R}_{\text{arith}} - \frac{\sigma^2}{2}$$

where $\sigma^2$ is the variance of returns. Higher variance → larger gap between arithmetic and geometric mean. This is the **volatility drag**: the more volatile a return series, the worse its actual compounded performance compared to its average.

### When to use which

- **Arithmetic mean** for forward-looking expectations. "What will my one-year return be on average?"
- **Geometric mean** for backward-looking actual performance. "What did this investment actually earn over 10 years?"

Most published return statistics (S&P 500's 10% per year, etc.) are arithmetic means. When you compound them to project portfolio growth, you should use a slightly lower number to account for volatility drag.

### The weighted mean

When data points have different weights — different sizes, different importances — the weighted mean adjusts:

$$\bar{R}_w = \frac{\sum w_i R_i}{\sum w_i}$$

where $w_i$ is the weight on observation $i$.

Most common application in finance: **portfolio return**. If you hold 60% in stocks earning 10% and 40% in bonds earning 4%, your portfolio return is:

$$\bar{R}_p = 0.60 \times 0.10 + 0.40 \times 0.04 = 0.076 = 7.6\%$$

The portfolio's expected return is the weighted average of its components' expected returns.

### Median and mode

Median: the middle observation when the data is sorted. Useful for skewed data because it's not pulled by extreme observations.

Mode: the most frequent observation. Rarely used in continuous return data but useful for discrete outcomes.

For financial returns, the mean (especially geometric) and median are the most useful. Mode is rarely used.

↳ **Dig Deeper — Why the geometric mean matters for compounding**

*The arithmetic mean is the right answer for "what's my expected return next year?" The geometric mean is the right answer for "what return have I actually compounded over my holding period?" The two diverge with volatility, and the divergence (volatility drag) compounds badly over decades.*

**Prompt:**
> Walk through the volatility-drag math: arithmetic mean ≈ geometric mean + σ²/2. Apply it to three asset classes: T-bills (low volatility, low arithmetic-geometric gap), large-cap stocks (moderate gap), small-cap stocks or emerging markets (large gap). Compute the dollar difference in terminal wealth for $10,000 invested over 30 years at the arithmetic mean vs. the geometric mean for each. Why do practitioners typically quote arithmetic mean returns even when they're not the right number for compounding?

**What to do with the output:** Save it. The arithmetic-vs-geometric distinction recurs throughout the book; this builds intuition you'll use in Chapter 15's investing decisions.

### The trade-off (concept 1)

Measures of center trade **simplicity against accuracy under different conditions**. Arithmetic mean is simple and right for one-period forecasts. Geometric mean is more complex and right for multi-period compounded performance. Weighted mean handles unequal observations. Choose based on the question.

### Common misconceptions

- *"Average return is one number."* It is at least two: arithmetic and geometric. They give different answers, especially for volatile assets.
- *"A 0% average return means you broke even."* Only if returns were also constant. With volatility, a 0% arithmetic mean produces a negative geometric mean.

---

## Concept 2 — Measuring the spread

A measure of center tells you what's typical. A measure of spread tells you how much returns vary around that typical value. In finance, **spread is risk**.

### Variance and standard deviation

The **variance** is the average squared deviation from the mean:

$$\sigma^2 = \frac{1}{n-1}\sum_{i=1}^{n}(R_i - \bar{R})^2$$

(For a sample, divide by $n-1$ rather than $n$ to get an unbiased estimator. For a known population, divide by $n$. The distinction matters for inference but rarely for first-pass thinking.)

The **standard deviation** is the square root of the variance:

$$\sigma = \sqrt{\sigma^2}$$

The standard deviation is in the same units as the returns themselves (percentages), which is why it's the more interpretable measure. Returns of "10% with a standard deviation of 16%" means: most years the return is roughly between -6% and 26% (within one standard deviation), and rarely is it outside -22% to 42% (within two standard deviations).

For our example return series (10%, -5%, 15%, 20%, -10% with mean 6%):

| $R_i$ | $R_i - \bar{R}$ | $(R_i - \bar{R})^2$ |
|---|---|---|
| 10 | 4 | 16 |
| -5 | -11 | 121 |
| 15 | 9 | 81 |
| 20 | 14 | 196 |
| -10 | -16 | 256 |
| Sum | | 670 |

$$\sigma^2 = \frac{670}{4} = 167.5$$ (using $n-1 = 4$)

$$\sigma = \sqrt{167.5} = 12.94\%$$

So this stock returns about 6% per year on average, with a standard deviation of about 13%. In a typical year, the return is somewhere between -7% and +19%.

### The normal distribution

The normal distribution (the bell curve) is a probability distribution defined by its mean and standard deviation. Many statistical procedures assume returns are normally distributed.

For a normally distributed variable:
- About 68% of observations fall within ±1 standard deviation of the mean.
- About 95% fall within ±2 standard deviations.
- About 99.7% fall within ±3 standard deviations.

For our return series with mean 6% and standard deviation 13%:
- 68% of years: returns between -7% and +19%.
- 95% of years: returns between -20% and +32%.
- 99.7% of years: returns between -33% and +45%.

If returns are well-described by a normal distribution, this is enough to characterize the entire risk profile.

### When the normal distribution fails

Financial returns are *roughly* normally distributed but not exactly. Two important deviations:

**Fat tails (excess kurtosis).** Extreme events occur more often than a normal distribution would predict. The 1987 crash, the 1998 LTCM crisis, the 2008 financial crisis, and the 2020 COVID crash all involved one-day stock returns of -10% or worse — events the normal distribution would predict happen approximately never. Real markets have more extreme events than the normal model suggests.

**Skewness.** The distribution can be asymmetric. Equity returns tend to have *negative* skewness — large negative outliers (crashes) are more likely than large positive outliers (rallies of equivalent magnitude).

The implication for risk measurement: standard deviation, by itself, *understates* tail risk. Models that assume normality (Black-Scholes options pricing, value-at-risk) systematically undercount the probability of extreme losses. The 2008 crisis was, in part, a moment when this assumption catastrophically failed at large financial institutions.

For the project: when you compute your chosen company's standard deviation of returns, you have a useful measure of typical variability. You do *not* have a good measure of tail risk. Standard deviation and tail risk diverge in the moments that matter most.

### Worked example — the volatility of two stocks

Consider two stocks:
- **Stock A**: returns of 8%, 12%, 7%, 13%, 10% over 5 years. Mean 10%, std dev 2.5%.
- **Stock B**: returns of -10%, 30%, -5%, 25%, 10% over 5 years. Mean 10%, std dev 17.7%.

Both have the same mean return. Stock B's standard deviation is 7× higher. An investor holding Stock A has a smooth ride; an investor holding Stock B has wild swings. Same expected return, very different risk profile.

Which is "better"? Depends on the investor's tolerance for variance and on the time horizon. For short horizons, the lower-variance stock is usually preferable. For long horizons, the higher-variance stock can compound to a similar place — but with much more volatility drag (the geometric mean is meaningfully lower than the arithmetic mean).

↳ **Dig Deeper — Fat tails and what 2008 broke**

*Standard deviation describes a normal distribution. Real return distributions have fatter tails — extreme events happen more often than the normal model predicts. Models calibrated on stable data underestimate tail risk. The 2008 financial crisis was, in part, a moment when this assumption catastrophically failed.*

**Prompt:**
> Compare the empirical distribution of S&P 500 monthly returns over the past 50 years with a fitted normal distribution. How much of the actual return distribution is in the tails (beyond ±3 standard deviations)? Then walk through one specific 2008 event (e.g., the Lehman bankruptcy week) where market moves were many standard deviations beyond what a normal-distribution VaR would have predicted. What lessons did the financial industry draw, and what alternatives to normality-based risk measurement (CVaR, expected shortfall, stress testing) emerged?

**What to do with the output:** Save it. The fat-tails issue is the engine of "Still puzzling" in this chapter and the central concern in Chapter 20's risk management treatment.

### The trade-off (concept 2)

Spread metrics trade **summarizable simplicity against capturing tail behavior**. Standard deviation is one number that compresses an entire distribution. The compression is useful — but it loses the information about whether the distribution is fat-tailed, skewed, or otherwise non-normal. For routine risk measurement, $\sigma$ is the workhorse. For tail-risk-sensitive decisions, you need richer tools (we'll touch on these in Chapter 20).

### Common misconceptions

- *"Higher standard deviation means worse performance."* No — it means more variability. An investor who can tolerate variance and has a long horizon may prefer higher-volatility assets that compensate with higher expected returns.
- *"Two-standard-deviation events almost never happen."* In a normal distribution, they happen ~5% of the time — about once every 20 observations. Markets see them more often than normal predicts.

---

## Concept 3 — Measuring relationships and risk-adjusted returns

The third question to ask of a return series is "how does it relate to other return series?" This is where portfolio thinking starts.

### Covariance

The **covariance** of two return series measures how they move together:

$$\text{Cov}(A, B) = \frac{1}{n-1}\sum_{i=1}^{n}(R_{A,i} - \bar{R}_A)(R_{B,i} - \bar{R}_B)$$

When both series are above their means simultaneously, their product is positive. When one is above and the other below, negative. The covariance is the average of these products.

- **Positive covariance**: the two assets tend to move together.
- **Negative covariance**: the two assets tend to move opposite.
- **Zero covariance**: the two assets move independently.

Covariance has the disadvantage of being measured in (return units)² — hard to interpret. The fix: divide by the product of the two standard deviations to get correlation.

### Correlation

The **correlation coefficient** is covariance normalized to a -1 to +1 scale:

$$\rho_{A,B} = \frac{\text{Cov}(A, B)}{\sigma_A \sigma_B}$$

A correlation of +1 means the two returns move in lockstep. A correlation of -1 means they move exactly opposite. A correlation of 0 means no linear relationship.

Real-world correlations:
- US stocks and US bonds: typically 0.0 to 0.2 in normal markets, can rise to 0.5+ in stress.
- US large-cap and US small-cap: ~0.85 (move together).
- US stocks and international developed markets: 0.7-0.9 (move together).
- US stocks and gold: -0.1 to 0.1 (essentially uncorrelated on average).
- Stocks of the same industry: typically 0.6-0.8.

For diversification, low or negative correlations are desirable. Holding two assets with correlation 1.0 produces no diversification benefit. Holding two assets with correlation -0.3 produces meaningful diversification — when one is down, the other is on average up, smoothing the portfolio's overall return.

### Portfolio variance

The variance of a two-asset portfolio is *not* just the weighted average of the individual variances. It depends on the correlation:

$$\sigma_p^2 = w_A^2 \sigma_A^2 + w_B^2 \sigma_B^2 + 2 w_A w_B \rho_{A,B} \sigma_A \sigma_B$$

where $w_A, w_B$ are the portfolio weights and $\rho_{A,B}$ is the correlation.

If $\rho = +1$ (perfect correlation): $\sigma_p = w_A \sigma_A + w_B \sigma_B$. The portfolio variance is the weighted average; no diversification.

If $\rho = -1$ (perfect negative correlation): the portfolio can have *zero* variance if weights are chosen correctly. Real diversification is possible.

In practice, $\rho$ is typically positive but less than 1. The diversification benefit depends on how much less than 1.

This formula is the foundation of **Modern Portfolio Theory** (Harry Markowitz, 1952). The basic insight: by combining assets with imperfect correlation, you can build a portfolio with the same expected return as any individual asset but lower variance.

### The Sharpe ratio

The **Sharpe ratio** is the standard measure of risk-adjusted return:

$$\text{Sharpe} = \frac{\bar{R}_p - R_f}{\sigma_p}$$

where $\bar{R}_p$ is the portfolio's expected (or mean) return, $R_f$ is the risk-free rate (T-bill yield), and $\sigma_p$ is the portfolio's standard deviation.

The numerator is the **excess return** — the portion of return above what you could earn in T-bills. The denominator is the variance you took to get it. The Sharpe ratio is the excess return per unit of variance — how much risk-adjusted return the portfolio is delivering.

Reasonable benchmarks:
- Sharpe of 0.3-0.5: typical of broad equity markets over long periods.
- Sharpe of 0.5-1.0: a good actively managed fund.
- Sharpe above 1.0: exceptional, often unsustainable.
- Sharpe below 0.3: questionable; might be doing better in bonds.

Worked example: Stock A has expected return 10%, standard deviation 13%. T-bill yield is 4%. Sharpe ratio:

$$\text{Sharpe}_A = \frac{0.10 - 0.04}{0.13} = 0.46$$

Stock B has expected return 12%, standard deviation 25%:

$$\text{Sharpe}_B = \frac{0.12 - 0.04}{0.25} = 0.32$$

Stock A has the higher Sharpe ratio — better risk-adjusted return. This is *despite* Stock B having a higher expected return. The Sharpe ratio captures the trade-off correctly.

For the equity research project, computing the Sharpe ratio of your chosen company's stock relative to the S&P 500's Sharpe is a useful comparison. If your company has a substantially lower Sharpe than the market, you'd need a strong reason to recommend it as a long-only investment. (You can always sell short, but that's a different analysis.)

### The trade-off (concept 3)

Risk-adjusted-return metrics trade **single-number convenience against fidelity to actual risk**. Sharpe ratio is convenient and widely used but built on the assumption that standard deviation captures all relevant risk. For non-normal distributions (real returns), Sharpe ratio understates true risk. Alternative measures — Sortino ratio (downside deviation only), Calmar ratio (max drawdown), VaR — fix some of these limits at the cost of complexity. Sharpe ratio is the workhorse despite its limits.

### Common misconceptions

- *"Higher Sharpe is always better."* Higher Sharpe is generally better, but a backward-looking Sharpe based on a small sample can be misleading. Many funds with high historical Sharpes have produced poor returns subsequently.
- *"Correlation 0 means independent."* Zero correlation means *zero linear relationship*. Two variables can be strongly related nonlinearly with zero correlation.

---

## Synthesis — statistics as the language of portfolio decisions

Three concepts, one toolkit. Mean tells you what's typical. Standard deviation tells you the variability. Correlation tells you how assets move together. Sharpe ratio combines them into a risk-adjusted-return measure.

Together, these tools are the foundation of:
- **Modern portfolio theory** (Markowitz, 1952): combining assets with imperfect correlation lowers portfolio variance.
- **The Capital Asset Pricing Model** (Sharpe, Lintner, Mossin, 1960s): individual assets earn expected returns proportional to their systematic (non-diversifiable) risk. Chapter 14.
- **Performance evaluation**: comparing managers' Sharpe ratios, alpha, beta. Chapter 14 again.

For the equity research project, the deliverable from this chapter is a statistical summary of your chosen company's return series: mean, standard deviation, correlation with the S&P 500, Sharpe ratio. Compare to peers and to the broad market. Chapter 14 takes the next step — extracting beta from a regression — and then Chapter 17 uses it for the cost of equity.

---

## Exercises

### Warm-up

**13.1** A stock's annual returns over 5 years are 8%, 12%, -3%, 18%, 6%. Compute:
(a) Arithmetic mean.
(b) Geometric mean (compound annual return).
(c) Variance and standard deviation.

**13.2** Why is the geometric mean usually less than the arithmetic mean?

**13.3** Define correlation. What does correlation of +0.8 imply about two stocks? Correlation of -0.3?

### Application

**13.4** Two stocks each have mean return 10% and standard deviation 18%. The correlation between them is 0.40.

(a) Compute the variance of an equal-weight portfolio of the two.
(b) Compute the standard deviation of the portfolio.
(c) Compare the portfolio's standard deviation to either individual stock's. By what percentage is portfolio variance reduced by diversification?

**13.5** Compute the Sharpe ratio for:
(a) An asset with expected return 8% and std dev 12%, when T-bill yield is 3%.
(b) An asset with expected return 15% and std dev 28%, same T-bill yield.
(c) Which has the better risk-adjusted return?

**13.6** For your chosen company:
(a) Pull 5 years of monthly stock returns from a data source (Yahoo Finance or your firm's data feed).
(b) Compute mean, standard deviation, and Sharpe ratio (use a 4% annualized risk-free rate, divided by 12 for monthly).
(c) Compute correlation with monthly S&P 500 returns over the same period.

### Synthesis

**13.7** The S&P 500 has a long-run Sharpe ratio of about 0.4. Your chosen company has a computed historical Sharpe of 0.6. Three possible interpretations: (a) the company has been a genuinely better risk-adjusted investment, (b) the historical sample is too short and the high Sharpe is partly noise, (c) the company's risk profile changes over time and recent calm doesn't predict future calm. For each interpretation, identify what evidence would distinguish it from the others.

**13.8** A friend says: "Standard deviation overstates risk because it counts upside volatility the same as downside volatility." Construct a defense of standard deviation as a risk measure, and a counter-argument that supports the friend's intuition. What alternative metric (Sortino ratio? max drawdown?) would address the criticism, and what does it cost?

### Challenge

**13.9** Compute the volatility drag for an asset with arithmetic mean return 10% and standard deviation:
(a) 10%
(b) 20%
(c) 30%

For each, compute the implied geometric mean using the approximation $\bar{R}_{\text{geo}} \approx \bar{R}_{\text{arith}} - \sigma^2/2$. By how much does volatility drag reduce compounded long-run wealth for each variance level?

**13.10** Pick two stocks in different industries and compute:
(a) Correlation between them over the past 5 years.
(b) The variance reduction achievable by holding them in equal weight vs. holding either one alone.
(c) Discuss whether the diversification benefit is large enough to make the two-stock portfolio meaningfully better than holding the higher-Sharpe stock alone.

---

## Chapter summary

- The **arithmetic mean** is the simple average — right for forward one-period expectations.
- The **geometric mean** is the compound annual return — right for measuring multi-period actual performance. Always ≤ arithmetic mean.
- **Variance** and **standard deviation** measure spread. Standard deviation is in the same units as returns and is the workhorse.
- **Correlation** measures how two return series move together, scaled to -1 to +1.
- Portfolio variance: $\sigma_p^2 = w_A^2\sigma_A^2 + w_B^2\sigma_B^2 + 2w_Aw_B\rho_{A,B}\sigma_A\sigma_B$. Diversification benefit comes from $\rho < 1$.
- **Sharpe ratio** = (mean return − risk-free rate) / standard deviation. The standard risk-adjusted-return metric.
- Real returns have **fat tails** and **negative skewness** — risks the normal-distribution assumption misses.

---

## What would change my mind

The chapter argues that mean, standard deviation, correlation, and Sharpe ratio are the right basic toolkit for analyzing financial returns. The reading would have to revise if (a) returns turned out to be so non-normal that summary statistics were systematically misleading — they're not normal, but they're approximately so for most analytical purposes; the failures matter only at the tails, or (b) more sophisticated risk measures (CVaR, expected shortfall) became standardized in undergraduate finance teaching — they may, eventually; for now standard deviation and Sharpe remain the core.

## Still puzzling

The genuinely hard question this chapter sets up is *what to do about non-normality*. Real return distributions have fat tails. Models that assume normality (Black-Scholes, value-at-risk) are systematically wrong about extreme events. Yet replacement models (extreme-value theory, regime-switching models, copulas) are dramatically more complex and don't have clean undergraduate treatments. The honest answer is that elementary risk modeling uses Gaussian assumptions while knowing they're wrong, and tries to compensate with stress-testing, scenario analysis, and qualitative judgment. The 2008 financial crisis was, in part, a moment when this compensation failed at scale. I haven't found a clean way to teach this without either oversimplifying or overwhelming.

---

## Connections forward

- **Chapter 14** uses regression to extract beta — the slope of a stock's returns on the market.
- **Chapter 15** applies these tools to portfolio construction.
- **Chapter 17** uses beta and the equity premium to compute the cost of equity.
- **Chapter 20** revisits risk measurement, including alternatives to standard deviation.

---

---

## LLM Exercise — Chapter 13: Risk Metrics on Your Return Series

**Project:** Equity Research Report on a Chosen Public Company
**What you're building this chapter:** Compute mean, standard deviation, and Sharpe ratio for your company and the S&P 500 over a 5-year window.
**Tool:** Excel or Python. Claude for interpretation.

### Setup

Use the 60 months of returns you computed in Chapter 12. If you don't have them yet, do that exercise first.

### The Prompt

```
For [your company], using the 60 monthly returns I have:

1. **Compute the arithmetic mean monthly return** for your company and for the S&P 500.

2. **Annualize each** — multiply by 12 for the arithmetic-mean approximation, or compute the geometric mean and annualize.

3. **Compute the standard deviation** of monthly returns for each. Annualize by multiplying by √12.

4. **Compute the Sharpe ratio** for each:
   Sharpe = (Annual mean return - Risk-free rate) / Annual std dev
   Use 4.5% as the risk-free rate (current 10-year Treasury yield).

5. **Compute the correlation** between your company's monthly returns and the S&P 500's monthly returns.

6. **Compute the volatility drag**: Geometric mean ≈ Arithmetic mean - σ²/2. By how much is your company's compounded long-run return reduced by its volatility, compared to its arithmetic mean?

Then interpret:
- Is your company's Sharpe ratio higher or lower than the S&P 500's? What does that suggest?
- Is your company's volatility drag substantial? What does it imply for long-term wealth creation?
- Is the correlation high or low? What does it imply about the firm's diversification benefit in a portfolio?

Show your calculations.
```

### What this produces

A risk-metrics summary table for the report. Quantifies the firm's risk profile relative to the market.

### How to adapt this prompt

- *For your own company:* Replace [your company]. Use the data you already pulled in Chapter 12.
- *For ChatGPT / Gemini:* Identical.
- *For Claude Code:* The full computation in Python is 5-10 lines using pandas — recommended if you have any code background.

### Connection to previous chapters

Builds on Chapter 12's return data. Sets up Chapter 14's beta regression.

### Preview of next chapter

Chapter 14 runs the regression to extract beta. The Chapter 14 LLM Exercise will compute your company's beta and apply CAPM to get the cost of equity.

---

**Tags:** mean, standard-deviation, variance, correlation, Sharpe-ratio, normal-distribution, fat-tails, volatility-drag


---

## AI Wayback Machine

**Harry Markowitz** was invented modern portfolio theory in 1952 — Nobel 1990.

**Run this:**

```
Who is Harry Markowitz, and how does their work connect to statistical analysis in finance we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about their career or ideas.
```

→ Search **"Harry Markowitz"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to apply Harry Markowitz's framework to a specific finance question.
- Add a constraint: "Answer including criticisms or limits of Harry Markowitz's framework."

What changes? What gets better? What gets worse?
