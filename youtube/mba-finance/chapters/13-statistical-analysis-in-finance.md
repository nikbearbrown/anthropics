# Chapter 13 — Statistical Analysis in Finance
*A single number tells you nothing. Here's the minimum you need to say something useful.*

---

## The puzzle of the single year

A friend tells you about an investment that returned 22% last year. Should you put your money in it?

You don't know yet. Twenty-two percent is one data point. The investment might typically return 15% — last year was lucky. It might typically return 25% — last year was actually disappointing by its standards. It might be a wild ride that returned -30% the year before and +22% last year, averaging roughly -4%. The single number tells you almost nothing about what to expect going forward.

To say something useful, you need a *sample* of returns over time. Then you can ask three questions: what's the typical return (the mean), how much does it vary (the standard deviation), and how does it move with other investments (the covariance, the correlation)?

These three questions are the foundation of everything quantitative in the second half of this book. Beta, Sharpe ratio, portfolio optimization, value-at-risk — all of them are built from the basic statistics here.

---

## Measuring the center: two kinds of average

The first question is "what's typical?" and there are at least two correct answers, depending on what you're actually asking.

### The arithmetic mean

The arithmetic mean is the simple average:

$$\bar{R} = \frac{1}{n}\sum_{i=1}^{n} R_i$$

Take a stock with annual returns of 10%, −5%, 15%, 20%, −10% over five years:

$$\bar{R} = \frac{10 - 5 + 15 + 20 - 10}{5} = 6\%$$

This is the right number to use if you're asking "what return should I expect next year, on average?" It is the *wrong* number to use if you're asking "what cumulative return did I actually earn over the five years?"

### The geometric mean

For multi-period investments with compounding, the geometric mean gives the constant annual rate that would have produced the same cumulative outcome:

$$\bar{R}_{\text{geo}} = \left[\prod_{i=1}^{n}(1 + R_i)\right]^{1/n} - 1$$

The clearest demonstration uses extreme numbers. Take 50% one year, −50% the next.

- Arithmetic mean: $(50 - 50)/2 = 0\%$
- Start with $100. Gain 50% to $150. Lose 50% to $75.

The arithmetic mean says you broke even. You didn't. You lost 25%. The geometric mean captures this:

$$\bar{R}_{\text{geo}} = (1.50 \times 0.50)^{1/2} - 1 = (0.75)^{0.5} - 1 = -13.4\%$$

Now work through the five-year example (10%, −5%, 15%, 20%, −10%):

$$\bar{R}_{\text{geo}} = (1.10 \times 0.95 \times 1.15 \times 1.20 \times 0.90)^{1/5} - 1$$

Product: $1.10 \times 0.95 = 1.045$; $\times 1.15 = 1.202$; $\times 1.20 = 1.442$; $\times 0.90 = 1.298$.

$$(1.298)^{0.2} - 1 = 5.37\%$$

Lower than the 6% arithmetic mean, as it must be. The geometric mean is *always* less than or equal to the arithmetic mean for any return series with non-zero variance. The relationship is approximately:

$$\bar{R}_{\text{geo}} \approx \bar{R}_{\text{arith}} - \frac{\sigma^2}{2}$$

This term $\sigma^2/2$ is called **volatility drag**: the more volatile a return series, the worse its actual compounded performance relative to its arithmetic average. A fund with 30% annualized volatility experiences a drag of roughly 4.5 percentage points per year — its actual compounded wealth grows 4.5 points slower than its arithmetic mean suggests.

<!-- → [TABLE: Volatility drag comparison — rows for three volatility levels (10%, 20%, 30%) — columns: arithmetic mean (fixed at 10%), volatility drag (σ²/2), implied geometric mean, dollar value of $10,000 after 30 years at arithmetic vs. geometric mean — student should see the drag compound severely over long horizons for high-volatility assets] -->

**When to use which.** Arithmetic mean for forward-looking expectations — "what will I earn next year on average?" Geometric mean for backward-looking actual performance — "what did this investment actually compound to?" Most published return statistics (the S&P 500's "10% long-run return") are arithmetic means. When you project portfolio growth over decades, the geometric mean is the right input.

### Portfolio return: the weighted mean

When assets have different sizes, the portfolio return is the weighted average:

$$\bar{R}_p = \sum w_i R_i$$

where $w_i$ is the weight of each position. If 60% is in stocks earning 10% and 40% in bonds earning 4%:

$$\bar{R}_p = 0.60 \times 0.10 + 0.40 \times 0.04 = 7.6\%$$

This is linear and works cleanly. The variance of a portfolio is *not* the weighted average of its components' variances — that's the central insight of portfolio theory, and we'll get there.

↳ **Dig Deeper — Why volatility drag matters for compounding**

*The arithmetic-geometric gap has real consequences for long-term investors. High-volatility assets that report strong arithmetic average returns may compound far more slowly than advertised. The size of the effect is often underappreciated.*

**Prompt:**
> Walk through the volatility-drag math: arithmetic mean ≈ geometric mean + σ²/2. Apply it to three asset classes: T-bills (low volatility), large-cap stocks (moderate), small-cap stocks or emerging markets (high). Compute the dollar difference in terminal wealth for $10,000 invested over 30 years at the arithmetic mean vs. the geometric mean for each. Why do practitioners typically quote arithmetic mean returns even when they're not the right number for compounding?

**What to do with the output:** Save it. The arithmetic-vs-geometric distinction recurs throughout the book; this builds intuition you'll use in Chapter 15's investment decisions.

---

## Measuring the spread: variance and standard deviation

A measure of center tells you what's typical. A measure of spread tells you how much returns vary around that typical value. In finance, spread is risk — these two things are not metaphorically related; they are the same thing.

### The calculation

The **variance** is the average squared deviation from the mean:

$$\sigma^2 = \frac{1}{n-1}\sum_{i=1}^{n}(R_i - \bar{R})^2$$

(Dividing by $n-1$ rather than $n$ gives an unbiased estimator for a sample. The distinction matters for inference; for first-pass analysis, use $n-1$.)

The **standard deviation** is the square root of the variance, which puts it back in the same units as the returns:

$$\sigma = \sqrt{\sigma^2}$$

For the five-year return series (10%, −5%, 15%, 20%, −10%, mean = 6%):

| $R_i$ | $R_i - \bar{R}$ | $(R_i - \bar{R})^2$ |
|---|---|---|
| 10% | +4 | 16 |
| −5% | −11 | 121 |
| 15% | +9 | 81 |
| 20% | +14 | 196 |
| −10% | −16 | 256 |
| **Sum** | | **670** |

$$\sigma^2 = \frac{670}{4} = 167.5 \qquad \sigma = \sqrt{167.5} \approx 12.9\%$$

So this stock returns about 6% per year on average, with a standard deviation of about 13%. In a typical year, the return sits somewhere between −7% and +19%.

### The normal distribution

If returns are normally distributed, the standard deviation is all you need to characterize the risk profile. For a normal distribution:

- ~68% of observations fall within ±1 standard deviation of the mean.
- ~95% within ±2 standard deviations.
- ~99.7% within ±3 standard deviations.

For our example (mean 6%, σ 13%): 95% of years fall between −20% and +32%. A loss worse than −33% is a roughly three-sigma event — expected about 0.3% of the time, or once every 300 years.

<!-- → [CHART: Bell curve overlaid on histogram of S&P 500 annual returns from 1928–present — student should see that the actual distribution matches the normal curve reasonably in the middle but has visibly fatter tails at both extremes, with actual extreme returns occurring more often than the curve would predict] -->

### When the normal assumption fails

Real financial return distributions deviate from the normal in two important ways.

**Fat tails (excess kurtosis).** Extreme events occur more often than the normal distribution predicts. The 1987 single-day crash of −22% was a roughly 20-sigma event under a normal model — something the model says should happen approximately never in the history of the universe. Real markets have seen multiple such events in living memory. The normal model systematically underestimates the probability of extreme outcomes.

**Negative skewness.** Real return distributions are asymmetric. Large negative outliers (crashes) occur more frequently than large positive outliers of equivalent magnitude. Equity returns have a long left tail.

The implication: standard deviation, by itself, *understates* tail risk. This matters most exactly when it matters most — in crisis conditions, the actual loss probabilities are higher than a normal-distribution calculation suggests. The 2008 financial crisis was, in part, a moment when institutions running normal-distribution risk models discovered their models had been wrong in ways that turned out to be catastrophic.

For the project: your company's standard deviation is a useful measure of typical variability. It is not a reliable measure of how bad things could get in a crisis. Keep both facts in mind.

↳ **Dig Deeper — Fat tails and what 2008 broke**

*Standard deviation describes a normal distribution. Real return distributions have fatter tails. Models calibrated on stable data underestimate tail risk. The 2008 financial crisis was, in part, the moment this assumption failed at scale.*

**Prompt:**
> Compare the empirical distribution of S&P 500 monthly returns over the past 50 years with a fitted normal distribution. How much of the actual distribution lies beyond ±3 standard deviations? Then walk through one specific 2008 event — the Lehman bankruptcy week — where market moves were many standard deviations beyond what a normal-distribution VaR would have predicted. What lessons did the financial industry draw, and what alternatives to normality-based risk measurement (CVaR, expected shortfall, stress testing) emerged?

**What to do with the output:** Save it. The fat-tails issue is the engine of "Still puzzling" in this chapter and the central concern in Chapter 20's risk management treatment.

---

## Measuring relationships: covariance and correlation

The third question is "how does this investment move with everything else?" This is where portfolio thinking begins.

### Covariance

The **covariance** between two return series measures how they move together:

$$\text{Cov}(A, B) = \frac{1}{n-1}\sum_{i=1}^{n}(R_{A,i} - \bar{R}_A)(R_{B,i} - \bar{R}_B)$$

When both series are above their means simultaneously, the product is positive. When one is above and the other below, negative. Positive covariance means assets tend to move together; negative covariance means they move opposite; zero covariance means no systematic relationship.

The problem with covariance is its units: (return)², which is not interpretable in isolation. Fix this by normalizing.

### Correlation

$$\rho_{A,B} = \frac{\text{Cov}(A, B)}{\sigma_A \sigma_B}$$

Correlation is bounded: always between −1 and +1. A correlation of +1 means the two assets move in perfect lockstep. A correlation of −1 means they move exactly opposite. A correlation of 0 means no linear relationship.

<!-- → [INFOGRAPHIC: Scatter plots of return pairs showing three correlation regimes — ρ = +0.9 (tight upward cluster), ρ = 0.0 (cloud), ρ = −0.5 (downward-sloping cloud) — with example asset pairs labeled at each; student should be able to estimate correlation from a scatter plot and know which regime enables diversification] -->

Some real-world benchmarks:
- US large-cap stocks and US small-cap stocks: ~0.85 (move together almost entirely)
- US stocks and international developed markets: ~0.7–0.9
- US stocks and long-term Treasuries: ~0.0 to 0.2 in normal markets, higher in stress
- US stocks and gold: ~−0.1 to +0.1 (essentially uncorrelated on average)
- Stocks within the same industry: typically 0.6–0.8

For diversification, low or negative correlations are valuable. Holding two assets with correlation 1.0 provides no diversification — you just own the same thing twice at different weights. Holding two assets with correlation −0.3 provides meaningful diversification: when one is down, the other is on average up.

### Portfolio variance

Here is the insight that drove Harry Markowitz to a Nobel Prize. The variance of a two-asset portfolio is *not* the weighted average of the individual variances:

$$\sigma_p^2 = w_A^2 \sigma_A^2 + w_B^2 \sigma_B^2 + 2 w_A w_B \rho_{A,B} \sigma_A \sigma_B$$

The third term — $2 w_A w_B \rho_{A,B} \sigma_A \sigma_B$ — is the covariance term, and it's what determines whether combining two assets actually reduces risk.

If $\rho = +1$: the covariance term is at maximum. Portfolio variance equals the weighted average of individual variances. No diversification.

If $\rho = -1$: the covariance term is at minimum. With the right weights, portfolio variance can reach zero. Perfect diversification is theoretically possible.

In practice, most real asset correlations are positive and below 1. The diversification benefit is real but partial.

Work through an example. Two stocks, each with mean 10% and standard deviation 18%, correlation 0.4:

$$\sigma_p^2 = (0.5)^2(18)^2 + (0.5)^2(18)^2 + 2(0.5)(0.5)(0.4)(18)(18)$$
$$= 81 + 81 + 64.8 = 226.8$$
$$\sigma_p = \sqrt{226.8} = 15.1\%$$

Each stock alone: 18% standard deviation. Equal-weight portfolio: 15.1% standard deviation. Same expected return (10%), lower risk. That's the free lunch in diversification — but only because the correlation is 0.4, not 1.0.

<!-- → [CHART: Line chart showing how equal-weight portfolio standard deviation changes as correlation varies from −1 to +1, for two assets each with σ = 18% — x-axis is correlation, y-axis is portfolio std dev; mark the ρ = +1 point (no benefit, σ_p = 18%), ρ = 0 point (meaningful reduction), ρ = −1 point (zero variance possible); student should see that diversification benefit scales continuously with how far correlation is below 1.0] -->

---

## Risk-adjusted return: the Sharpe ratio

Mean and standard deviation together answer the question "how much did I earn, and how much risk did I take to get there?" The Sharpe ratio combines them into a single number:

$$\text{Sharpe} = \frac{\bar{R}_p - R_f}{\sigma_p}$$

The numerator is the **excess return** — return above the risk-free rate (Treasury bills). The denominator is the standard deviation. The ratio is the excess return per unit of volatility taken: how much are you getting paid for each unit of risk?

Two stocks, both earning 10% historically:

- **Stock A**: standard deviation 13%, T-bill rate 4%.
  $\text{Sharpe}_A = (10 - 4)/13 = 0.46$

- **Stock B**: standard deviation 25%.
  $\text{Sharpe}_B = (10 - 4)/25 = 0.24$

Same average return. Stock A has twice the risk-adjusted efficiency. The Sharpe ratio captures the trade-off the raw return number hides.

Reasonable benchmarks from decades of US market data:
- Broad equity market (S&P 500): Sharpe ~0.4 over long horizons
- A consistently good active fund: 0.5–1.0
- Sharpe above 1.0: exceptional, and often unsustainable
- Sharpe below 0.3: should prompt the question "why not just hold bonds?"

For the equity research project: compare your chosen company's historical Sharpe ratio to the S&P 500's. If the company's Sharpe is substantially below the market's, you'd need a compelling reason to own it. The Sharpe ratio alone isn't the final word — it's backward-looking and built on the normal-distribution assumption — but it's the right first question.

<!-- → [TABLE: Sharpe ratio interpretation reference — rows for five Sharpe ranges (below 0.3, 0.3–0.5, 0.5–1.0, above 1.0, negative) — columns: Sharpe range, Interpretation, Typical example, What it implies for a long-only investor — student should be able to look up any computed Sharpe and quickly frame what it means relative to benchmarks] -->

---

## The statistics as a system

Three tools, one toolkit. Mean tells you what's typical and in what direction. Standard deviation tells you how far returns wander from that center. Correlation tells you how one asset's wandering relates to another's. Sharpe ratio puts return and risk on the same scale.

Together these are the foundation for:

**Modern Portfolio Theory** (Markowitz, 1952): combining assets with imperfect correlation lowers portfolio variance without reducing expected return. The efficient frontier — the set of portfolios that maximize return for a given variance — follows directly from the portfolio variance formula.

**The Capital Asset Pricing Model** (Sharpe, Lintner, 1960s): in a market where all investors hold efficient portfolios, the only risk that earns compensation is the non-diversifiable component — the covariance with the market portfolio, normalized by the market's variance. That's beta. Chapter 14.

**Performance evaluation**: comparing managers by Sharpe ratio, by alpha (return in excess of what beta predicts), by information ratio. Chapter 14 again.

The limit of all of this is the normal-distribution assumption. Mean, standard deviation, and Sharpe ratio compress a return distribution into two or three numbers. For distributions close to normal, the compression is fair. For distributions with fat tails and negative skewness — real financial returns — the compression loses the information that matters most in bad times. Chapter 20 treats risk measurement more fully; this chapter installs the vocabulary without which that treatment would have nowhere to land.

---

## What would change my mind

The chapter argues that mean, standard deviation, correlation, and Sharpe ratio are the right basic statistical toolkit for financial return analysis. The argument would have to revise if returns were so non-normal that summary statistics were systematically misleading for most analytical purposes — they're not normal, but they're approximately so in the middle of the distribution, where most observations live. The failures are real and important but concentrated in the tails. The tools remain the standard for good reasons.

## Still puzzling

The hardest unsolved problem this chapter sets up is what to do about the fact that standard deviation is a wrong model of risk in the moments risk matters most. Fat tails and negative skewness aren't minor technical corrections — they're the difference between "this fund might lose 10% in a bad year" and "this fund might lose 40%." More sophisticated alternatives exist (conditional VaR, expected shortfall, extreme-value theory, regime-switching models) but none has a clean undergraduate treatment that preserves the intuitive appeal of standard deviation. The honest position is that practitioners use Gaussian models while knowing they're wrong, compensate with stress testing and qualitative judgment, and periodically get humbled. I haven't found a better teaching approach that doesn't either oversimplify or overwhelm.

---

## Connections forward

- **Chapter 14** uses regression to extract beta — the slope of a stock's returns on the market return.
- **Chapter 15** applies this toolkit to portfolio construction.
- **Chapter 17** uses beta and the equity risk premium to compute cost of equity via CAPM.
- **Chapter 20** revisits risk measurement and introduces alternatives to standard deviation for tail risk.

---

## Exercises

### Warm-up

**13.1** A stock's annual returns over five years are 12%, −8%, 20%, 5%, −3%.

(a) Compute the arithmetic mean.
(b) Compute the geometric mean. Show the step-by-step product.
(c) Compute the variance and standard deviation (use $n - 1$ in the denominator).

**13.2** Explain in plain English why the geometric mean is always less than or equal to the arithmetic mean. Use the 50% / −50% example to illustrate.

**13.3** Define correlation. What does a correlation of +0.85 between two stocks imply for portfolio diversification? What about a correlation of −0.2?

### Application

**13.4** Two assets each have expected return 8% and standard deviation 15%. Compute the variance and standard deviation of an equal-weight (50/50) portfolio under three correlation assumptions:

(a) $\rho = +1.0$
(b) $\rho = +0.4$
(c) $\rho = 0.0$

For each, state by what percentage portfolio standard deviation is reduced compared to holding either asset alone. What does the comparison show about how diversification benefit scales with correlation?

**13.5** Compute the Sharpe ratio for:

(a) A stock with mean annual return 11%, standard deviation 18%, risk-free rate 4%.
(b) A stock with mean annual return 16%, standard deviation 32%, same risk-free rate.
(c) Which has superior risk-adjusted return? Would you choose the other stock under any circumstances?

**13.6** An asset has an arithmetic mean return of 10% per year. Use the approximation $\bar{R}_{\text{geo}} \approx \bar{R}_{\text{arith}} - \sigma^2/2$ to compute the geometric mean and the terminal wealth of $10,000 after 30 years for each of the following standard deviations: 5%, 15%, 25%, 35%. Plot or tabulate the results. What is the dollar cost of a 35% standard deviation versus a 5% standard deviation over 30 years, all else equal?

### Synthesis

**13.7** The S&P 500 has a long-run Sharpe ratio of roughly 0.4. Suppose your company's five-year historical Sharpe is 0.65. Three possible readings: (a) the company has genuinely been a superior risk-adjusted investment, (b) five years is too short a sample and the high Sharpe is partly noise, (c) the company's risk profile has been unusually calm in the recent period and may not persist. For each reading, identify one piece of evidence that would help distinguish it from the others.

**13.8** A colleague argues: "Standard deviation penalizes upside volatility the same as downside volatility, which is unfair — investors don't care about lucky big gains." Construct both sides of this argument: (a) a defense of standard deviation as a risk measure and (b) a case for using the Sortino ratio (downside deviation only) instead. What does the Sortino ratio cost in terms of complexity and data requirements?

### Challenge

**13.9** Pull five years of monthly returns for your chosen company and for the S&P 500 from Yahoo Finance or another data source.

(a) Compute arithmetic mean, standard deviation, and Sharpe ratio for each (annualize by ×12 and ×√12 respectively; use 4.5% as the risk-free rate).
(b) Compute the correlation between your company's monthly returns and the S&P 500's.
(c) Interpret: Is the Sharpe above or below the market? Is the correlation high enough to limit diversification value? Is the volatility drag material?

**13.10** Using the fat-tails insight from the chapter: if a normal distribution predicts that a −3σ event happens 0.15% of the time (roughly once every 650 observations), but the actual S&P 500 historical monthly return series shows how many months fell below −3σ, compute the empirical frequency and compare it to the normal model's prediction. Does the actual frequency suggest the normal model understates tail risk? By how much?

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
- *For Claude Code:* The full computation in Python is 5–10 lines using pandas — recommended if you have any code background.

### Connection to previous chapters

Builds on Chapter 12's return data. Sets up Chapter 14's beta regression.

### Preview of next chapter

Chapter 14 runs the regression to extract beta. The Chapter 14 LLM Exercise will compute your company's beta and apply CAPM to get the cost of equity.

---

## AI Wayback Machine

**Harry Markowitz** published "Portfolio Selection" in the *Journal of Finance* in 1952 — the paper that founded modern portfolio theory and eventually earned him a Nobel Prize in 1990.

**Run this:**

```
Who is Harry Markowitz, and how does their work connect to statistical analysis in finance we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about their career or ideas.
```

→ Search **"Harry Markowitz"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to apply Harry Markowitz's framework to a specific portfolio construction question.
- Add a constraint: "Answer including criticisms or limits of Harry Markowitz's framework."

What changes? What gets better? What gets worse?

---

**Tags:** mean, standard-deviation, variance, correlation, Sharpe-ratio, normal-distribution, fat-tails, volatility-drag
