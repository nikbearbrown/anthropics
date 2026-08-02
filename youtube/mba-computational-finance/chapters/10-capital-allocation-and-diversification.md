# Chapter 10 — How Much Should You Risk?

## TL;DR

- Most investors optimize the wrong decision.
- The chapter moves through The Setup, The Capital Allocation Line, Where on the Line Should You Stand?, The Physics of the Problem: Human Capital, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

*Most investors optimize the wrong decision.*

There is a question hiding inside every investment decision that most people never ask directly. They ask: *which* stocks? *Which* funds? *Which* allocation between this sector and that one? But underneath all of that is a prior question, simpler and more important:

How much of your money should be in risky things at all?

This is the question I want to think through carefully in this chapter. Not because the answer is complicated — it isn't, once you see it clearly — but because the way of arriving at the answer teaches you something real about risk, about time, about the difference between a decision that's mathematically right and a decision that's right for a human life.

---

## The Setup

Suppose you've done the work in Chapter 9. You've built the efficient frontier — the curve of all achievable portfolios across risky assets. You've found the portfolio that maximizes the Sharpe ratio: the most expected return per unit of volatility. Call it the risky portfolio. It's a mix of assets, optimally weighted, and we're not going to second-guess those weights here.

Now you face a different question. You have that risky portfolio on one side. On the other side, you have something completely safe: Treasury bills, or a high-yield savings account, or just cash. They earn the risk-free rate. No volatility. No uncertainty. What they tell you they'll pay, they pay.

What fraction of your wealth do you put in the risky portfolio, and what fraction do you park in the safe asset?

Call that fraction $y$. If $y = 0$, you hold only cash. If $y = 1$, you're fully in the risky portfolio. If $y = 0.5$, you're halfway. And if $y > 1$ — if you borrow money to invest more than you actually have — you're using leverage. Every value of $y$ is a real portfolio. The question is which one is right.

---

## The Capital Allocation Line

Here is the elegant part. When you mix the risky portfolio and the risk-free asset, the combinations don't scatter randomly. They trace a straight line.

The arithmetic is clean. Suppose the risky portfolio has an expected return of 7% and a volatility of 9.5%. The risk-free rate is 4.5%. If you put fraction $y$ into the risky portfolio and $(1-y)$ into cash, the expected return of the combined portfolio is:

$$E(R_p) = (1-y) \cdot R_f + y \cdot E(R_{\text{risky}}) = R_f + y \cdot [E(R_{\text{risky}}) - R_f]$$

And the volatility — because cash has zero volatility and zero correlation with anything — is simply:

$$\sigma_p = y \cdot \sigma_{\text{risky}}$$

These two equations say something beautiful together. As you increase $y$ from 0 to 1, expected return goes up linearly, and volatility goes up linearly. If you plot expected return on the vertical axis and volatility on the horizontal axis, all the possible portfolios lie on a straight line — one endpoint at $(0,\, R_f)$ when $y = 0$, the other at $(\sigma_{\text{risky}},\, E(R_{\text{risky}}))$ when $y = 1$.

That line is the Capital Allocation Line. Here is what it looks like for these numbers:

| Fraction in risky portfolio | Expected return | Volatility |
|---:|---:|---:|
| 0% (all cash) | 4.5% | 0.0% |
| 25% | 5.1% | 2.4% |
| 50% | 5.75% | 4.75% |
| 75% | 6.4% | 7.1% |
| 100% (all risky) | 7.0% | 9.5% |
| 125% (borrow 25%) | 7.6% | 11.9% |
| 150% (borrow 50%) | 8.3% | 14.3% |

![Capital Allocation Line ](images/10-capital-allocation-and-diversification-fig-01.png)
*Figure 10.1 — Capital Allocation Line *

The slope of this line is:

$$\text{slope} = \frac{E(R_{\text{risky}}) - R_f}{\sigma_{\text{risky}}} = \frac{7\% - 4.5\%}{9.5\%} \approx 0.26$$

That is the Sharpe ratio of the risky portfolio. Every point on the Capital Allocation Line has the same Sharpe ratio. You cannot do better than this line — given your choice of risky portfolio, no combination of that portfolio and cash can land you above the line. The line is your frontier.

Notice what this means. The question of *which* risky portfolio to hold — the asset-mix question — determines the slope of the line. The question of *how much* to hold — the capital allocation question — determines where on the line you stand. These are two separate decisions. Most investors spend all their time on the first one and almost none on the second. That is backwards.

---

## Where on the Line Should You Stand?

The Capital Allocation Line tells you what is achievable. It doesn't tell you what is right for you. For that, you need to know something about your tolerance for risk.

Economists model this with a parameter called the coefficient of relative risk aversion, written $A$. The idea is that investors care about expected return (more is better) but dislike variance (more is worse). The utility function I'll use is:

$$U = E(R_p) - \frac{1}{2} A \sigma_p^2$$

Your satisfaction from a portfolio equals its expected return, minus a penalty for variance. The penalty is proportional to $A$. If $A$ is large, you really don't like variance. If $A$ is small, you're comfortable taking on volatility for more return.

Now plug in the expressions for $E(R_p)$ and $\sigma_p$ in terms of $y$:

$$U(y) = \left[R_f + y(E(R_{\text{risky}}) - R_f)\right] - \frac{1}{2} A (y \cdot \sigma_{\text{risky}})^2$$

To find the $y$ that maximizes this, take the derivative with respect to $y$ and set it to zero:

$$\frac{dU}{dy} = (E(R_{\text{risky}}) - R_f) - A y \sigma_{\text{risky}}^2 = 0$$

Solving for $y$:

$$y^* = \frac{E(R_{\text{risky}}) - R_f}{A \cdot \sigma_{\text{risky}}^2}$$

This is the optimal allocation to the risky portfolio. For our numbers — $E(R_{\text{risky}}) - R_f = 2.5\%$, $\sigma_{\text{risky}}^2 \approx 0.009$ — what does this give for different values of $A$?

| Risk aversion $A$ | Optimal $y^*$ | What it implies |
|---:|---:|---|
| 1 (very low) | ~277% | Heavy leverage — borrowing nearly 3× your wealth |
| 2 (low) | ~138% | Modest leverage |
| 4 (moderate) | ~69% | Roughly 65/35 stocks/bonds |
| 6 (high) | ~46% | Roughly 45/55 stocks/bonds |
| 10 (very high) | ~28% | Mostly conservative |

![Optimal allocation y* vs](images/10-capital-allocation-and-diversification-fig-02.png)
*Figure 10.2 — Optimal allocation y* vs*

The striking thing about this table isn't any single row. It's the range. Two investors with similar demographics but different risk tolerances might rationally hold portfolios that look completely different — one fully invested with leverage, one holding less than a third in risky assets. This is not a rounding error. This is the whole ballgame.

Here is the honest problem with this framework. You can write the formula for $y^*$ in one line. But when I ask you what your risk aversion parameter $A$ is, you will stare at me. Most people cannot introspect their way to a number. What they *can* do is tell you how they felt when they watched their portfolio drop 30% in a crisis, or whether they slept well during March 2020, or whether they found themselves checking prices obsessively. That is revealed risk aversion. It is messier than a parameter, but it is more real.

---

## The Physics of the Problem: Human Capital

Here is where the theory gets genuinely interesting, and where most textbook treatments shortchange you.

Think about what a young person actually is in economic terms. A 28-year-old with a good career trajectory is not just a small financial portfolio. She is a bundle of assets: that small portfolio, plus an enormous quantity of future labor income. Thirty-five years of salaries, raises, bonuses — all of it waiting to be earned. In present value, that stream of income is worth an enormous amount. For a professional earning $150,000 per year, growing modestly, the present value of future earnings can easily exceed $2–3 million.

And labor income, for most salaried workers, behaves like a bond. It pays out regularly. It doesn't crash when the stock market crashes. It has low correlation with equity markets. A software engineer's salary in 2022, when the stock market fell 20%, did not fall 20%.

This means a young person's *total wealth* — financial portfolio plus human capital — is already heavily weighted toward bond-like assets. The financial portfolio, which is all most people think about, represents only a small fraction of total wealth. The financial portfolio can afford to be very heavily in equities precisely to counterbalance the enormous bond-like component sitting in the human capital.

![The financial portfolio should counterbalance human capital — which is why equity allocation rationally declines with age](images/10-capital-allocation-and-diversification-fig-03.png)
*Figure 10.3 — Total wealth composition across a career *

An older worker approaching retirement has little future labor income; their human capital has been largely converted into financial assets over the course of a career. Their financial portfolio needs to start looking more balanced because their total wealth — not just their financial portfolio — has shifted.

This is the theoretically clean version of the "110 minus age" heuristic you've probably heard. It captures the right direction, if not the precise level. A 28-year-old: 110 − 28 = 82% equity. A 65-year-old: 110 − 65 = 45% equity. The heuristic is not a theorem — it ignores wealth level, income stability, whether the person has dependents, what other assets they hold. The empirical evidence on whether it outperforms simpler or more sophisticated rules is mixed [verify]. But it gets the direction right for the right reason, and that matters.

---

## Working It Through: Maya's Portfolio

Let me make this concrete. Maya is 28 years old. She has $80,000 in retirement accounts, $20,000 in savings, and is finishing an MBA. She expects her post-graduation salary to be in the $130,000–$200,000 range, growing from there. No dependents. She self-assesses as moderate risk tolerance: she could watch a 30% market drop without selling, but she has never been tested by one as a full adult. Thirty-five-year horizon to typical retirement.

What allocation is right for her?

The risky portfolio. For Maya's long horizon, we tilt the efficient-frontier portfolio toward equity. Over 35+ year horizons, equity's higher expected return compounds substantially, and the worst historical 35-year windows for diversified equity portfolios have still been positive [verify].

| Asset | ETF | Weight |
|---|---|---:|
| US Total Market Equity | VTI | 50% |
| International Developed Equity | VEA | 20% |
| Emerging Markets Equity | VWO [verify] | 10% |
| US Aggregate Bonds | BND | 15% |
| Inflation-Protected Bonds | VTIP | 5% |

This is an 80% equity / 20% fixed income risky portfolio.

The capital allocation. For Maya's $100,000 total, I'd recommend approximately 95% into this risky portfolio and 5% — about $5,000, roughly two months of living expenses — in cash. Her six-month emergency fund should live in a separate high-yield savings account, outside this portfolio entirely.

The combined allocation: roughly 76% equity, 19% fixed income, 5% cash. Aggressive, but appropriate for someone with Maya's horizon and human capital situation. The expected return is roughly 7–7.5% nominal annualized [verify]. The volatility is roughly 12–13% annualized [verify] — meaning in a bad year the portfolio might drop 25% or more. Over 35 years, with regular contributions, it compounds to a very different place than a conservative allocation would.

The life-cycle path. This allocation isn't permanent. As Maya ages, her human capital shrinks and her financial portfolio grows. The rational response is to slowly reduce equity exposure:

| Age | Equity | Fixed income | Cash |
|---:|---:|---:|---:|
| 28 | 76% | 19% | 5% |
| 38 | 70% | 25% | 5% |
| 48 | 60% | 35% | 5% |
| 58 | 50% | 40% | 10% |
| 68 (retired) | 40% | 50% | 10% |

![Maya's glidepath ](images/10-capital-allocation-and-diversification-fig-04.png)
*Figure 10.4 — Maya's glidepath *

This is the glidepath that target-date retirement funds implement. Target-date 2060 funds [verify] at major providers hold allocations broadly similar to Maya's 28-year-old portfolio. The convergence is reassuring — not because it proves anything, but because it suggests we haven't made an error that practitioners would immediately flag.

Two quick checks. First, the heuristic: 110 − 28 = 82% equity. Our recommendation is 76% equity. Within 6 percentage points, and the difference is defensible — we're accounting for the bond-like character of Maya's human capital by tilting even the risky portfolio toward equity, rather than maximizing the equity allocation in the financial portfolio alone.

Second, cross-model check: the same investor profile given to different AI models produces portfolios that agree within about 5 percentage points of each major asset class, all anchoring around the Vanguard target-date 2060 fund's baseline allocation [verify]. The spread across models is smaller than the uncertainty in Maya's own risk assessment.

---

## The Leverage Question

The formula for $y^*$ says that for very low risk aversion, the optimal allocation is well above 100% — an investor should borrow to invest more than they have. The Bodie-Merton-Samuelson framework, which formalizes the human capital argument, reaches the same conclusion for young investors: because your human capital is enormous in present value, you should hold far more financial equity than you can afford without leverage [verify].

I want to take this argument seriously before explaining why I don't follow it for Maya.

The theoretical case is real. A 28-year-old with stable employment and 35 years of future earnings could treat their human capital as collateral and lever up their equity exposure. The math supports it.

Here is the problem. Maya's human capital is not yet stable. She is finishing a graduate degree. Her career is not underwritten by years of established employment. Leverage amplifies not just good outcomes but bad ones. The precise scenario that would make leverage catastrophic — a market crash coinciding with difficulty finding employment — is more plausible at 28 than at 38. Leverage that is rational in expectation can be destructive in the specific tail scenario where a person is most vulnerable.

There is also a practical barrier: margin borrowing rates are not the risk-free rate. The formula assumes you can borrow at $R_f$. You cannot. Margin rates are typically several percentage points above the risk-free rate [verify], which changes the math considerably. The expected return advantage of leverage shrinks; the risk does not.

My recommendation: no leverage for Maya at 28. After her income is established — say, at 33 or 35, with a few years of employment history and a clearer earnings trajectory — the argument for modest leverage becomes more defensible. Not now. This is one of the places where I depart from the strict textbook prescription. The textbook answer is technically right in expectation. A human life adds constraints the formula doesn't see.

---

## Is Your Investment Manager Worth It?

There is a direct application of everything in this chapter to a practical question: should you pay a financial advisor for portfolio construction?

The logic is clean. Without a manager, you can buy the efficient-frontier portfolio in low-cost index ETFs at roughly 0.03–0.05% in annual expenses. If a manager charges 1% per year — which is not unusual — they need to produce at least 1% of annual outperformance after fees just to break even with the do-it-yourself alternative.

In compounding terms: over 30 years, 1% per year costs approximately 26% of terminal wealth [verify]. On a portfolio that grows to $1 million by retirement, that's roughly $260,000 in foregone wealth. That is the cost of underperforming by only 1% per year.

The empirical evidence on whether actively managed funds consistently beat low-cost index funds, net of fees, is not ambiguous. The majority underperform their benchmark after fees over long horizons [verify — see SPIVA reports]. This does not mean all advisors are worthless — a good advisor adds real value through tax planning, behavioral coaching, estate planning, and helping clients not panic-sell in a crash. But those are not portfolio construction services. If you are paying for portfolio construction, evaluate portfolio construction.

The test is simple: ask your advisor for their after-fee portfolio returns over the past 5–10 years. Compare to a simple low-cost 60/40 fund over the same period. If they've beaten it net of fees, they've added value in portfolio construction. If they haven't, they haven't — and you should be clear-eyed about what you're actually paying for.

---

## What This Chapter Taught

We started with a question that sounds deceptively simple: how much of your money should be in risky assets?

The answer requires three pieces. First, a risky portfolio — the efficient-frontier-optimized mix. Second, a risk-free asset. Third, the Capital Allocation Line, which traces all achievable combinations and shows that the slope of the line — the Sharpe ratio — is fixed by your choice of risky portfolio. Your only job is to find where on the line to stand.

Where to stand depends on risk aversion, time horizon, and the structure of your other wealth — particularly human capital. Young investors with large human capital can rationally hold very high equity allocations; older investors near retirement cannot. The mathematics of $y^*$ gives the direction; the specifics of a life give the constraints.

The one thing to carry forward: the decision of *how much* to risk is prior to and more important than the decision of *what* risky assets to hold. Getting the capital allocation wrong by 30 percentage points matters more to your long-run outcome than optimizing the weights inside the risky portfolio to three decimal places. Understand the line. Know where you stand on it. Know why.

---

## What Would Change My Mind

The framework here assumes that mean-variance optimization, even in constrained form, adds value over simpler heuristics. Some empirical literature challenges this — there is evidence [verify] that naive diversification (equal weights) and simple age-based rules produce results comparable to optimized portfolios in out-of-sample periods, after accounting for estimation error in expected returns. If this evidence is right, the optimization adds less value than I've claimed, and the simple rules deserve more respect.

I find this evidence genuinely unsettling in a productive way. It doesn't change the logic of the Capital Allocation Line, which is correct. It challenges whether the inputs — especially expected returns — are estimated precisely enough for the optimization to outperform simpler methods. Chapter 11 takes up that problem directly.

---

## Still Puzzling

The human capital argument gives directions but not levels. It says young people should hold more equity — much more than their financial portfolio alone would suggest. But the formal Bodie-Merton-Samuelson model [verify], pushed to its limit, implies extremely high equity allocations for young investors, sometimes with leverage. The chapter rejects leverage on practical grounds. Whether those practical grounds fully override the theoretical case is a genuinely open question. The theory is right about the direction. Whether it is right about the magnitude is something I don't know, and I think it's honest to say so.

---

*Coming up.* The portfolios in Chapters 9 and 10 used historical data to estimate expected returns. That's a problem — historical averages are noisy, and naive extrapolation can lead you to expect returns that have already been arbitraged away. Chapter 11 develops a more principled framework for estimating expected returns through the Capital Asset Pricing Model and its extensions, and asks when an asset's expected return justifies its role in the portfolio.

---

## Exercises

**Warm-up**

1. *(Capital Allocation Line mechanics)* Using the numbers from the chapter — risky portfolio with 7% expected return and 9.5% volatility, risk-free rate 4.5% — calculate the expected return and volatility of a portfolio that puts 40% in the risky portfolio and 60% in cash. Then calculate the same for a portfolio with $y = 1.2$ (20% leverage). Show your work using the two linear equations.

2. *(Sharpe ratio)* The chapter states that every point on the Capital Allocation Line has the same Sharpe ratio. Verify this by computing the Sharpe ratio at $y = 0.5$ and at $y = 1.25$ using the numbers above. Explain in one sentence why constant Sharpe ratio is a geometric inevitability given the shape of the line.

3. *(Optimal allocation formula)* An investor has risk aversion $A = 5$. Using the $y^*$ formula with the chapter's numbers (excess return = 2.5%, $\sigma^2 \approx 0.009$), calculate their optimal allocation. Is this above or below 100%? What does that imply for their portfolio?

**Application**

4. *(Risk aversion elicitation)* The chapter argues that people cannot directly report their risk aversion parameter $A$, but they can reveal it through behavior. Design a three-question interview you could use to estimate someone's approximate $A$ — questions that are specific, behavioral, and grounded in realistic scenarios rather than abstract probabilities. For each question, explain what answer pattern would suggest high vs. low $A$.

5. *(Human capital accounting)* A 35-year-old teacher earns $65,000 per year and expects roughly 2% annual raises until retirement at 65. Assuming a 5% discount rate, estimate the present value of her remaining labor income. Then describe how this human capital affects the optimal equity allocation in her financial portfolio. Does her job security matter? Why?

6. *(Glidepath construction)* A 45-year-old investor currently holds 80% equity, 20% bonds, with a 20-year retirement horizon. Using the human capital logic from the chapter, argue whether this allocation is too aggressive, too conservative, or appropriate — and what information about the investor you would need to be confident in your answer.

7. *(Leverage trade-off)* The chapter states that margin borrowing rates are typically several percentage points above the risk-free rate. Suppose the risk-free rate is 4.5% but margin borrowing costs 8.5%. Recalculate the expected return on a $y = 1.25$ portfolio (25% leverage) using the actual borrowing cost rather than $R_f$. How does the expected return change, and what does this imply for the optimal leverage level in $y^*$?

**Synthesis**

8. *(Capital allocation vs. asset selection)* The chapter's closing argument is that capital allocation — how much to risk — matters more than asset selection — which risky assets to hold. Construct a numerical example using the $y^*$ formula to demonstrate this claim. Show that an investor who gets the capital allocation wrong by 30 percentage points suffers a larger long-run cost than an investor who uses an unoptimized risky portfolio instead of the efficient-frontier portfolio, holding capital allocation constant.

9. *(Human capital and career risk)* The chapter treats labor income as bond-like for most salaried workers. But some careers have equity-like income: a startup employee whose salary is below market but who holds significant stock options, a commissioned salesperson whose income tracks the economy, a freelancer whose billings correlate with market cycles. How should these workers adjust their financial portfolio relative to the chapter's framework? What is the direction of the adjustment, and what is the mechanism?

**Challenge**

10. *(Stress-test the framework)* The $y^*$ formula is derived under assumptions the chapter doesn't fully defend: that a single parameter $A$ captures all relevant risk preferences, that the utility function is quadratic in returns, and that the investor maximizes expected utility over a single period. Identify the assumption you find most problematic, explain precisely why it fails for a realistic investor, and describe what a more realistic model would need to include. Does the failure of this assumption change the *direction* of the chapter's recommendations, or just the *magnitude*?

---

###  LLM Exercise — Chapter 10: How Much Should You Risk?

**Project:** Maya's Memo, Built Across the Course
**What you're building this chapter:** The y* Recommendation section of the memo: the fraction of the learner's wealth that belongs in the risky portfolio, defended.
**Tool:** Claude Code

---

**The Prompt:**

```
I'm working on Maya's Memo. The tangency portfolio is in `analysis/09-frontier.md`.

Chapter 10 taught:
- **The Capital Allocation Line** (CAL) connecting the risk-free asset to the tangency portfolio
- **The y* formula**: $y^* = (E[r_p] - r_f) / (\gamma \sigma_p^2)$, where γ is the risk-aversion coefficient
- **The Kelly fraction** as the related-but-different limit case (γ = 1 in log utility)
- The gap between *math-right* and *right for a human life*

Scaffold `analysis/10-allocation.py`:

1. **Load the tangency portfolio's expected return and variance** from `analysis/09-frontier.md`.

2. **Compute y* for three risk-aversion coefficients**:
   - γ = 2 (aggressive, e.g., a 25-year-old with high human capital)
   - γ = 4 (moderate, the textbook default)
   - γ = 8 (conservative, e.g., near-retirement)

   Report y* for each, and the resulting expected return and volatility of the *combined* portfolio (y* in the tangency portfolio plus (1 − y*) in the risk-free asset).

3. **Compute the Kelly fraction** for the same tangency portfolio. Compare to the y* values above.

4. **Plot the Capital Allocation Line.** Mark the three y* points, the Kelly fraction, and 100% tangency.

5. **The human-life check.** One paragraph. The math gives a fraction. What is the *behavioral* check — what's the largest drawdown the learner can live through without selling? Apply that constraint and report the implied y*.

6. **Save `analysis/10-allocation.md`** with the y* values, the CAL plot, the human-life check, and a one-sentence recommendation: *given my risk aversion and my behavioral capacity, the fraction of my wealth in the risky portfolio should be approximately X%.*

The script runs with `python analysis/10-allocation.py --gamma [VALUE]`.
```

---

**What this produces:** A runnable script `analysis/10-allocation.py` plus `analysis/10-allocation.md` containing y* for three risk-aversion levels, the Kelly fraction, the CAL plot, the behavioral check, and a final recommendation.

**How to adapt this prompt:**

- *For your own project:* Replace any bracketed domain placeholder with your specific instrument, ticker, or context. The exercise structure is instrument-agnostic; the content is yours.
- *For ChatGPT / Gemini:* Works as-is. For ChatGPT, save the running memo to a Custom GPT instead of a Claude Project. For Gemini, paste the project's accumulated section files into the context window each session.
- *For Claude Code:* Right tool — y* is a one-line formula but the comparison to Kelly and the behavioral check are easier to communicate from a script that produces the plot.
- *For a Claude Project:* Append to the project. The y* recommendation here is the *single most important number* for translating the analysis into action; the capstone (Ch 13) integrates it.

**Connection to previous chapters:** Chapter 9 produced the tangency portfolio; Chapter 10 asks how much of the learner's wealth belongs in it.

**Preview of next chapter:** Chapter 11 asks whether the position's return profile is *exceptional* (alpha) or *lucky* (beta-driven) — using CAPM and factor models.

---

##  AI Wayback Machine
The ideas in this chapter didn't appear from nowhere. **John Larry Kelly Jr.** was deriving the *Kelly criterion* in 1956 at Bell Labs — the formal rule for what fraction of capital to bet given a known edge, applied first to information theory and signal processing before it reached finance decades before most people had heard of capital allocation, the fraction of wealth at risk, and the math of *how much to bet*. Here's a prompt to find out more — and then make it better.

![John Larry Kelly Jr., c. 1960s. AI-generated portrait based on a public domain photograph (Wikimedia Commons).](images/john-larry-kelly-jr.jpg)
*John Larry Kelly Jr., c. 1960s. AI-generated portrait based on a public domain photograph.*

**Run this:**

```
Who was John Larry Kelly Jr., and how does his 1956 derivation of the *Kelly criterion* — originating in Shannon's information theory rather than in finance — connect to the chapter's question of how much of one's wealth to put in the risky portfolio versus the risk-free asset? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.
```

→ Search **"John Larry Kelly Jr."** on Wikipedia after you run this. See what the model got right, got wrong, or left out.

**Now make the prompt better.** Try one of these:

- Ask it to explain *the Kelly criterion* in plain language, as if you've never seen utility theory
- Ask it to compare the Kelly fraction to the chapter's optimal $y^*$ — what's the same, what's different
- Add a constraint: "Answer as if you're writing the case for sizing positions by the Kelly fraction in a real portfolio"

What changes? What gets better? What gets worse?
