# Chapter 2 — Returns and Risk Measurement


## TL;DR

- The word "return" is doing two jobs at once, and the math for those two jobs is different.
- The chapter moves through Warm-up, Application, Synthesis, Challenge, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

*The word "return" is doing two jobs at once, and the math for those two jobs is different.*

---

Here is a magic trick. A stock goes up 50% one year, then down 50% the next. Are you back where you started?

Take a moment before answering.

You start with $100. After the up year: $100 × 1.5 = $150. After the down year: $150 × 0.5 = $75.

You are down 25%. A 50% gain followed by a 50% loss left you with 75 cents on every dollar you started with. The two moves did not cancel.

This is not a trick with the numbers. It is a structural fact about how returns combine, and it has consequences that run through everything in this chapter. The word "return" in everyday speech is doing two jobs at once — describing a single period's gain and describing a path through time — and the math for those two jobs is different. Getting comfortable with that difference is the chapter's first task.

---

When someone asks how a stock has performed, the honest answer begins with a question back: which version of "return" do you want?

There are three, and they give different numbers on the same underlying data.

The first is what most people mean. Simple return: the arithmetic percent change from start price to end price.

$$R_{\text{simple}} = \frac{P_{\text{end}} - P_{\text{start}}}{P_{\text{start}}}$$

If a stock was $100 at the start of the year and $178 at the end, the simple return is 78%. This is the right answer to the question *what fraction of my starting money did I make?* It's direct, intuitive, and correct for communicating results to a human who isn't going to do further math with the number.

The second is the logarithmic return:

$$R_{\text{log}} = \ln\!\left(\frac{P_{\text{end}}}{P_{\text{start}}}\right) = \ln(1.78) \approx 57.7\%$$

| Return type | Formula | When to use it |
|---|---|---|
| **Simple (arithmetic) return** | $r_t = (P_t - P_{t-1}) / P_{t-1}$ | Single-period return for one position; what brokers report on a statement |
| **Log return** | $r_t = \ln(P_t / P_{t-1})$ | When you need to add returns across time (log returns are time-additive); when modeling continuously compounded processes |
| **Total return (with dividends)** | $r_t = (P_t + D_t - P_{t-1}) / P_{t-1}$ | Comparing equity returns across companies with different dividend policies; computing realized investor return |

Smaller. Different. The natural question is why anyone would use a number that seems to understate what happened.

Because logarithms were invented precisely to turn multiplication into addition. John Napier published the first log tables in 1614 to let astronomers replace the tedious multiplication of large numbers with the addition of smaller ones — that's what "logarithm" means at its roots, the *ratio-number*. The same property is what makes log returns essential for statistical work.

If you have daily log returns $r_1, r_2, \ldots, r_n$, the total log return over the period is just their sum:

$$R_{\text{total}} = \sum_{i=1}^{n} r_i$$

This works because the log of a product equals the sum of the logs. Each daily log return is $\ln(P_i / P_{i-1})$, and when you add them up, all the intermediate prices telescope away — the $\ln(P_1)$ in the first term cancels with the $-\ln(P_1)$ in the second, and so on, until only $\ln(P_n / P_0)$ remains.

If you have daily *simple* returns and want the total simple return, you have to multiply: $\prod_{i=1}^{n}(1 + R_i) - 1$. A product, not a sum. For statistical work — standard deviations, regressions, fitting distributions — sums are vastly more tractable than products. That's why anyone doing serious return statistics works with log returns, and anyone reporting to a human works with simple returns. Both are correct. They answer different questions.

The third version is total return, and it's the most honest accounting of what you actually earned. A stock whose price went from $100 to $108 while paying a $2 dividend had a price return of 8% and a total return of 10%. If you held the stock, you got the dividend. For a company where dividends are a substantial fraction of the total return — an AT&T or Coca-Cola — reporting only price return dramatically understates what shareholders earned. The difference between price return and total return is the dividend yield, and forgetting it isn't a minor rounding error; it's a different measurement of a different quantity.

Now back to the magic trick, which we can understand properly.

The 50%-up / 50%-down result isn't a paradox. It's arithmetic: $(1.5)(0.5) = 0.75$. What it reveals is that volatility itself has a cost, even when the average return is zero. The arithmetic average of +50% and −50% is zero. The compounded result is −25%. That gap is called *volatility drag*, and it grows with the level of volatility. Assets that swing wildly must earn a higher arithmetic average just to break even on a compounded basis.

![Line chart showing two portfolios over 10 periods](images/02-returns-and-risk-measurement-fig-01.png)
*Figure 2.1 — Line chart showing two portfolios over 10 periods*

This is why log returns are the natural language for multi-period compounding. The log of $(1.5 \times 0.5)$ is $\ln(1.5) + \ln(0.5) \approx 0.405 - 0.693 = -0.288$, which corresponds to a simple return of $e^{-0.288} - 1 \approx -25\%$. The log-return arithmetic tells you the truth about the path.

---

Two cars leave Boston for New York, both arriving in exactly four hours. Average speed: 55 miles per hour. Identical performance by that measure.

Car A held steady at 55 the whole way. Car B oscillated wildly — 30, then 80, then 20, then 90 — but happened to average 55 and arrived at the same time. Same destination, same schedule, radically different rides.

Volatility is the second car. It is not about whether you got there. It is about how much it shook on the way.

In finance, volatility almost always means the standard deviation of returns over some window. Let me build that from the bottom up, because the formula earns its meaning when you see where it comes from.

Start with a set of daily returns $r_1, r_2, \ldots, r_n$ and their average $\bar{r}$. For each return, compute its deviation from the average: $r_i - \bar{r}$. Some are positive, some negative. If we averaged these deviations to get a sense of how spread out the returns are, we'd always get exactly zero — the positive and negative deviations cancel by the definition of the average.

So we square them. Squaring does two things: it makes every term positive so they don't cancel, and it punishes large deviations more than small ones — a return twice as far from the mean contributes four times as much to the sum. We average the squared deviations to get the variance:

$$\sigma^2 = \frac{1}{n-1}\sum_{i=1}^{n}(r_i - \bar{r})^2$$

The denominator is $n-1$ rather than $n$ because we estimated the mean from the same data we're using for the variance, costing us one degree of freedom — a correction that matters with small samples and is negligible with large ones.

Variance has the wrong units. If returns are in percent, variance is in percent-squared. Nobody thinks in percent-squared. So we take the square root:

$$\sigma = \sqrt{\sigma^2}$$

Standard deviation. The typical size of a deviation from the mean. The word does what it says.

Now the catch that trips up almost everyone the first time: how do you turn a daily standard deviation into an annual one?

There are 252 trading days in a year. The naive approach is to multiply by 252. Don't.

There is a property of variance that is one of the cleanest results in probability theory. If daily returns are independent of each other — today's return doesn't predict tomorrow's — then the variance of the annual return, which is the sum of 252 daily returns, is 252 times the variance of a single daily return:

$$\text{Var}(r_1 + r_2 + \cdots + r_{252}) = 252 \cdot \text{Var}(r)$$

Variance scales linearly with time. Standard deviation is the square root of variance, so:

$$\sigma_{\text{annual}} = \sqrt{252} \cdot \sigma_{\text{daily}} \approx 15.87 \cdot \sigma_{\text{daily}}$$

A daily volatility of 1% annualizes to about 15.9%, not 252%. The annualizer is $\sqrt{252}$, not $252$.

![Step-by-step diagram of the annualization derivation ](images/02-returns-and-risk-measurement-fig-02.png)
*Figure 2.2 — Step-by-step diagram of the annualization derivation *

Why variance and not standard deviation? The variance of a sum of independent variables equals the sum of their variances — that's a fundamental probability fact, following from the independence assumption. Standard deviation is the square root of variance, so when you go from one period to $n$ periods, the standard deviation scales as $\sqrt{n}$. The square root is not a convention. It is a consequence.

When you see an annualized volatility figure that looks bizarrely large, the first thing to check is whether someone multiplied the daily standard deviation by 252 instead of $\sqrt{252}$. That mistake produces a number roughly 16 times too large.

Standard deviation is symmetric: a return of +10% contributes the same to volatility as −10%. For most investors, that's a distortion — upside surprises don't feel like risk the same way downside surprises do. Alternatives exist (downside deviation, semivariance) that compute the standard deviation from only the below-average returns. They're more emotionally intuitive and less mathematically tractable: most of the standard toolkit — regression, portfolio theory, the central limit theorem — was built for symmetric statistics. The tradeoff is real.

What standard deviation can't see, primarily, is fat tails. If a stock has occasional monthly returns of −20% or +30% more often than a normal distribution would predict, the standard deviation underestimates the probability of those extreme events. Volatility captures the *typical* spread. It says little about how bad the bad days actually are.

---

Here are two investment options.

Option A earns 8% a year with 12% volatility. Option B earns 14% a year with 30% volatility. Which is better?

The question can't be answered without knowing what you value. If you need the money in two years and can't absorb a 40% drawdown, Option B might ruin you even if it has the higher expected return. If you have a 20-year horizon and iron nerves, Option B's higher expected return might dominate. The Sharpe ratio formalizes one version of the question: per unit of volatility absorbed, how much excess return did you earn?

$$S = \frac{R_p - R_f}{\sigma_p}$$

Three pieces. $R_p$ is the portfolio's return. $R_f$ is the risk-free rate — what you could have earned with no risk at all, currently short-term Treasury bills (verify for current rates). $\sigma_p$ is the portfolio's volatility.

Why subtract the risk-free rate? Because the alternative to taking risk is earning the risk-free rate. A stock that returned 5% in a year when T-bills also returned 5% gave you nothing for the volatility you absorbed. Sharpe measures *excess* return — what risk-taking actually earned above the free alternative.

Why divide by volatility? Because the question is whether you were *compensated* for the risk you took. Dividing by volatility makes Sharpe dimensionless and comparable across assets that differ in both return and risk. A Sharpe of 1.0 means you earned one unit of excess return per unit of volatility.

The long-run Sharpe ratio of broad US equity markets is roughly 0.4 to 0.6. A sustainable Sharpe for an individual stock in that range is normal. A Sharpe of 2.0 or more on a single name over a single year is more likely to be a lucky window than a persistent property of the asset.

NVDA's Sharpe over the most recent three-year window comes in at roughly 1.40 (verify against current data). Over the most recent five-year window, it falls to roughly 0.91. The difference is the AI rally of 2023 and 2024 — an 18-month period that was exceptional for NVDA specifically. The three-year Sharpe includes that period entirely; the five-year Sharpe dilutes it with two earlier years of more ordinary performance.

![Dual-panel bar chart ](images/02-returns-and-risk-measurement-fig-03.png)
*Figure 2.3 — Dual-panel bar chart *

This window sensitivity is not a flaw in the calculation. It's the calculation telling you something true: NVDA's recent performance was unusually good, and how good it looks depends entirely on where you start the clock. An analyst who presents only the three-year Sharpe without noting the five-year figure is presenting a fact that happens to be flattering rather than a full picture.

The Sharpe ratio's blind spot is the same as standard deviation's: it assumes returns are roughly bell-curved, and it treats upside and downside volatility symmetrically. For a stock like NVDA — which over the past five years had monthly skewness near +0.4 and excess kurtosis near +1.8 (verify) — the distribution is neither symmetric nor thin-tailed. There were more extremely good months than a normal distribution predicts, and more extremely bad months too. The positive skew means Sharpe slightly understates the asset's attractiveness; the fat tails mean Sharpe understates the risk of a genuinely bad month.

![Histogram of NVDA monthly returns with a fitted normal distribution overlay; both tails sit above the normal and the bulk shifts slightly right of zero](images/02-returns-and-risk-measurement-fig-01.png)
*Figure 2.1 — NVDA monthly returns vs. fitted normal*

Neither of these is a reason to abandon Sharpe. It is a reason to say what Sharpe is blind to when you cite it. A Sharpe of 1.40 on a fat-tailed, positively skewed asset is a different thing than a Sharpe of 1.40 on a normally distributed asset, and an analyst who knows this says so.

---

Maya's prompt to the model is specific in the way this chapter now makes possible:

> Compute annualized total return, annualized volatility (daily returns, annualized by √252), maximum drawdown, and Sharpe ratio (using 3-month T-bill as risk-free rate) for NVDA and SPY, over both a 3-year and a 5-year window ending most recent month. Also compute monthly skewness and kurtosis for NVDA. Show your data sources and any assumptions.

The specificity is doing real work. "Annualized total return" rather than "return" specifies dividend inclusion, annualization method, and period simultaneously. "Daily returns, annualized by √252" removes any ambiguity about how the volatility was scaled. "3-month T-bill as risk-free rate" pins the benchmark. Without this precision, two people running the same prompt could produce different numbers, and neither would be wrong — they'd just be answering different questions.

The results (all figures should be verified against primary data sources before use): NVDA over three years shows annualized total return near 78%, volatility near 52%, maximum drawdown near −57%, Sharpe near 1.40. SPY over three years shows annualized return near 14%, volatility near 17%, maximum drawdown near −25%, Sharpe near 0.51. Over five years, NVDA's Sharpe falls to roughly 0.91; SPY's long-run properties are more stable than any single tech stock's.

| | Annualized return | Annualized volatility | Max drawdown | Sharpe ratio | Skewness | Kurtosis |
|---|---|---|---|---|---|---|
| **NVDA — 3-year window** | 96% | 54% | -56% | 1.71 | -0.12 | 4.8 |
| **NVDA — 5-year window** | 53% | 49% | -66% | 0.99 | -0.34 | 5.6 |
| **SPY — 3-year window** | 11% | 16% | -25% | 0.50 | -0.41 | 4.2 |
| **SPY — 5-year window** | 13% | 18% | -34% | 0.55 | -0.46 | 4.9 |

*Reading across the window-sensitivity story: the same security looks dramatically different depending on whether you measure over the post-2022 AI-infrastructure run (3-year) or include the 2022 drawdown (5-year). The Sharpe ratio drops by nearly half. Specify the window before quoting the number.*

The verification runs as follows. The same prompt goes to two additional models. Both return three-year NVDA Sharpes within rounding distance of 1.40. Maximum drawdown figures agree within a percentage point. Skewness and kurtosis show more variation — different models use slightly different conventions for higher moments — but the qualitative finding holds across all three: NVDA's monthly return distribution is fat-tailed and slightly right-skewed.

Then Maya pulls NVDA's daily prices directly, computes daily log returns, computes mean and standard deviation, annualizes by $\sqrt{252}$, subtracts the risk-free rate, divides. The hand-calculated Sharpe lands within rounding of all three model estimates.

This is the verification chain. Not any single check, but the combination: cross-model consistency, then independent derivation from primary data. Each step could fail independently. When all of them agree, the number is defensible.

The memo is one page. NVDA and SPY at both windows. The fat-tail finding in plain English: NVDA's monthly returns are not bell-curved; extreme months — good and bad — are more common than standard models predict. The window sensitivity stated explicitly: the three-year Sharpe of 1.40 reflects an unusually strong period for NVDA; the five-year figure of 0.91 is the more conservative characterization for forward-looking purposes. The audit trail — prompts, cross-model checks, hand calculation — is attached.

---

Step back and ask why this specification discipline matters so much. Why do two analysts computing "NVDA's volatility" get different numbers?

Because finance is not measuring physical objects with stable properties. The boiling point of water is 100°C at sea level, and it will be the same number next Tuesday. NVDA's volatility over the past 36 months is one number; over the past 60 months, another; computed from daily returns, one answer; from monthly returns, a different one. The number is not a property of the stock alone. It is a property of the stock *and the measurement choices* simultaneously.

This is not a defect. It is the honest structure of the problem. Claims on uncertain futures don't have volatility the way copper has density. They have volatility *relative to* a window, a frequency, a return definition, and a sample period. Specification is how two analysts can disagree productively — they can compare numbers because they've agreed on a procedure. Without specification, every disagreement about return or risk is a definition fight masquerading as a disagreement about the world.

The number can't speak for itself. The choices behind it have to be visible and defensible. That habit — naming the window, the frequency, the return type, the benchmark — is what this chapter is actually building. The formulas are the vehicle. The specification discipline is the point.

---

## Exercises

### Warm-up

**1.** A stock opens the year at $200 and closes at $240. It paid no dividends. Calculate the simple return, the log return, and confirm that the log return is smaller. Why is the log return always smaller than the simple return for any positive gain? *(Tests: distinction between simple and log return.)*

**2.** A fund reports a daily volatility of 0.8%. An analyst annualizes it by multiplying by 252 and reports 201.6%. A second analyst multiplies by $\sqrt{252}$ and reports 12.7%. Which is correct, and what assumption makes it so? *(Tests: annualization mechanics and the independence assumption.)*

**3.** A portfolio earned 6% last year. The 3-month T-bill rate was 5.2%. The portfolio's annualized volatility was 9%. Compute the Sharpe ratio. Is this good, average, or poor relative to the long-run US equity benchmark? *(Tests: Sharpe ratio formula and benchmark calibration.)*

---

### Application

**4.** You have five annual returns for a stock: +30%, −20%, +15%, −10%, +25%. Calculate the arithmetic average return. Then compute the actual compounded result by chaining the multipliers $(1 + R_i)$. What is the gap between the two? What does this gap represent, and what drives its size? *(Tests: volatility drag; requires chaining returns rather than averaging.)*

**5.** A colleague hands you a Sharpe ratio of 1.8 for a hedge fund over the past two years, computed using monthly returns. You know the fund had several months with returns below −10% and several above +15%. Identify two specific reasons why the Sharpe ratio may be a misleading summary of this fund's risk-adjusted performance. Describe what additional statistics you would request and why. *(Tests: Sharpe ratio limitations — fat tails, symmetric treatment of upside and downside.)*

**6.** An analyst computes NVDA's "volatility" as 38% annualized. You suspect she used monthly returns rather than daily returns. Describe the procedure you would follow to verify or refute this, and explain what discrepancy you might expect to find if your suspicion is correct. *(Tests: specification discipline — return frequency as a measurement choice that changes the output.)*

**7.** A stock has a price return of 4% over the year and paid dividends totaling $3.50 on a starting price of $70. Compute the total return. Then explain why, for a retiree drawing income from a dividend portfolio, price return is a systematically misleading performance metric. *(Tests: total return vs. price return; connects the measurement choice to a real-world decision context.)*

---

### Synthesis

**8.** The chapter argues that "the number can't speak for itself — the choices behind it have to be visible and defensible." Using the Sharpe ratio as your example, list every choice an analyst makes before producing a single Sharpe ratio figure. For each choice, describe how a different but equally defensible choice would change the number. What does this exercise reveal about the nature of financial measurement? *(Tests: specification discipline applied to Sharpe; connects return type, window, frequency, and risk-free rate choices in one place.)*

**9.** A friend says: "Log returns are just a more complicated way of saying the same thing as simple returns — they both tell you how a stock performed." Write a two-paragraph response that uses the volatility drag example and the telescoping property to explain precisely why log returns and simple returns are *not* interchangeable, and when each is the right tool. *(Tests: deep distinction between simple and log returns; requires the student to articulate the Napier property and compounding in their own words — the Feynman test.)*

**10.** You are given two assets. Asset X has annualized return 12%, volatility 18%, Sharpe 0.39. Asset Y has annualized return 12%, volatility 18%, Sharpe 0.39. A colleague says the two assets are equivalent. You know Asset X has monthly skewness of −0.8 and excess kurtosis of +3.1, while Asset Y has skewness near zero and kurtosis near zero. Explain why the two assets are not equivalent, and describe the specific scenario in which Asset X would be far more damaging to a portfolio than Asset Y despite identical Sharpe ratios. *(Tests: fat tails and skewness as dimensions of risk invisible to standard deviation; integrates volatility, Sharpe, and distributional shape.)*

---

### Challenge

**11.** The square-root-of-time rule for scaling volatility rests on the assumption that daily returns are independent. In practice, financial returns show mild autocorrelation — positive autocorrelation in some momentum regimes, negative autocorrelation (mean-reversion) in others. Without doing the full derivation, describe qualitatively what would happen to the annualized volatility estimate if daily returns are positively autocorrelated (today's return predicts tomorrow's in the same direction). Would the $\sqrt{252}$ rule overestimate or underestimate true annual volatility? What does this imply for risk measurement during trending markets? *(Tests: the independence assumption underlying annualization; pushes beyond the chapter into where the framework breaks.)*

**12.** The chapter presents specification discipline as the solution to the problem of two analysts computing different "volatilities." But an adversarial reader might argue: if two equally defensible specifications give different numbers, then the number itself is arbitrary — and a precise-sounding Sharpe ratio is just a rhetorical device dressed up as measurement. Write a response to this critique. Does agreeing on a specification solve the problem, or does it merely defer it? What is the honest claim that a Sharpe ratio, properly specified, actually makes — and what is it not claiming? *(Tests: the epistemological status of financial measurement; stress-tests the chapter's own central argument.)*

---

*Tags: returns, volatility, Sharpe ratio, log returns, annualization, fat tails, skewness, kurtosis, specification discipline*

---

###  LLM Exercise — Chapter 2: Returns and Risk Measurement

**Project:** Maya's Memo, Built Across the Course
**What you're building this chapter:** The Return-and-Risk-Profile section of the memo: arithmetic and geometric returns, volatility, and a Sharpe ratio reported with the period and frequency stated.
**Tool:** Claude Project

---

**The Prompt:**

```
I'm working on Maya's Memo for the position named in `01-position-brief.md` (paste the position if not in the project context).

Chapter 2 introduced:
- **Arithmetic vs. geometric (CAGR) returns** — and the magic-trick result that 50% up then 50% down is not 0%
- **Volatility** as standard deviation of returns
- **The Sharpe ratio** as $(\text{return} - \text{risk-free rate}) / \text{volatility}$, *always* with the period and frequency stated

Produce `02-return-risk.md`, the second section of the memo, containing:

1. **The lookback window.** State the window you'll use to characterize returns and why (e.g., "10-year monthly returns, Jan 2015 – Dec 2024, capturing one full cycle plus the 2020 dislocation"). Defend the choice in two sentences against two alternative windows.

2. **Arithmetic and geometric returns.** Compute both for the position over your window. State the gap between them and what it tells you about volatility. *If the position is a private business or a bond, adapt: arithmetic = average annual cash yield, geometric = CAGR of intrinsic value.*

3. **Volatility.** Report the standard deviation of monthly returns, annualized by $\sqrt{12}$. Compare to the S&P 500 (or to the relevant benchmark for fixed income / private business — say which you used and why).

4. **The Sharpe ratio.** Compute it. State the period (annualized), the frequency the inputs were sampled at (monthly), and the risk-free rate you used (3-month T-bill, dated). State the convention you used for the excess-return calculation (subtracting the matching-period T-bill).

5. **What the numbers say about the position.** Two paragraphs. Not the numbers — what they *mean* for the recommendation. A high Sharpe ratio relative to the benchmark is one signal; a high Sharpe with low volatility is a different signal from a high Sharpe with high volatility paired with a high return.

Save as a section that will eventually go in the full memo. Be specific about the period and frequency throughout — *that* is the discipline this chapter teaches.
```

---

**What this produces:** A markdown document `02-return-risk.md` containing the lookback window, arithmetic and geometric returns, volatility, a fully-annotated Sharpe ratio, and a two-paragraph reading of what the numbers say.

**How to adapt this prompt:**

- *For your own project:* Replace any bracketed domain placeholder with your specific instrument, ticker, or context. The exercise structure is instrument-agnostic; the content is yours.
- *For ChatGPT / Gemini:* Works as-is. For ChatGPT, save the running memo to a Custom GPT instead of a Claude Project. For Gemini, paste the project's accumulated section files into the context window each session.
- *For Claude Code:* Optional — if you want the computations as a runnable script, ask Claude Code to scaffold `analysis/02-return-risk.py` that pulls the data via `yfinance` (for public equities) and produces the Sharpe ratio with the conventions stated.
- *For a Claude Project:* Append to the project. The Sharpe ratio computed here becomes the headline number that Chapter 9's portfolio analysis and Chapter 10's allocation decision will consume.

**Connection to previous chapters:** Chapter 1 set up the position; Chapter 2 produces its empirical return-and-risk profile.

**Preview of next chapter:** Chapter 3 produces the *equity-vs-debt framing* section: how does your position's claim structure (equity, debt, hybrid) shape the analysis?

---

##  AI Wayback Machine
The ideas in this chapter didn't appear from nowhere. **Louis Bachelier** was deriving the mathematics of random walks for the Paris Bourse in 1900 — five years before Einstein used the same equations to describe Brownian motion decades before most people had heard of returns, variance, and the formal measurement of risk. Here's a prompt to find out more — and then make it better.

![Louis Bachelier, c. 1900. AI-generated portrait based on a public domain photograph (Wikimedia Commons).](images/louis-bachelier.jpg)
*Louis Bachelier, c. 1900. AI-generated portrait based on a public domain photograph.*

![Louis Bachelier](../images/louis-bachelier-9wi.png)

*Puppet Art by [Nik Bear Brown](https://www.nikbearbrown.com/).*

**Run this:**

```
Who was Louis Bachelier, and how does his 1900 thesis *Théorie de la Spéculation* — applying random-walk mathematics to securities prices — connect to the modern measurement of returns, volatility, and risk that the chapter teaches? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.
```

→ Search **"Louis Bachelier"** on Wikipedia after you run this. See what the model got right, got wrong, or left out.

**Now make the prompt better.** Try one of these:

- Ask it to explain a *random walk* in plain language, as if you've never seen a probability density
- Ask it to compare Bachelier's 1900 framing to the modern Sharpe-ratio + standard-deviation toolkit
- Add a constraint: "Answer as if you're writing the historical preface to a chapter on volatility"

What changes? What gets better? What gets worse?
