# Chapter 9 — Portfolio Construction

## TL;DR

- The optimizer finds the frontier perfectly — and then misses the crisis entirely.
- The chapter moves through Warm-up, Application, Synthesis, Challenge, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

*The optimizer finds the frontier perfectly — and then misses the crisis entirely.*

In 1952, a twenty-four-year-old graduate student named Harry Markowitz published a fourteen-page paper in *The Journal of Finance* that contained one genuinely new idea. The idea was not complicated. It was, in retrospect, almost obvious. And yet nobody had written it down carefully before, and its consequences took the entire investment profession about thirty years to absorb.

The idea was this: the risk of a portfolio is not the average of the risks of its components. It is something smaller — how much smaller depends on how the components move relative to each other. Two assets that move in opposite directions can be combined into a portfolio that is less risky than either one alone, without sacrificing expected return. The combinations are constrained by the correlations, and the constraints trace out a boundary. That boundary is the efficient frontier.

This chapter is about how to find it, what it tells you, and — which is the part that trips everyone up the first time — what it cannot see.

---

A classmate, Priya, pulls Maya aside after class.

"My mom needs to redo her portfolio. She just turned sixty-five, has $1.2 million from selling her dental practice, twenty-year horizon, says she wants 5% real returns. Conservative but not panicked. She has an advisor but doesn't trust the recommendations."

Maya now has a real portfolio construction problem. A specific person, a specific dollar amount, specific constraints. Twenty years to draw on the money. Five percent real is roughly seven and a half percent nominal at typical inflation. Conservative-but-not-panicked is a tone of voice, not a parameter — and translating it into a number is most of the actual work.

The framework that takes you from "I need a portfolio" to a specific set of weights is mean-variance optimization. Let me build it up from the definition.

---

Suppose you have a universe of assets. Each has an expected return. Each has a volatility. Between every pair, there is a correlation. The question mean-variance optimization answers is: for any chosen level of expected return, what is the minimum-variance portfolio I can construct using these assets? Or equivalently: for any chosen level of variance, what is the maximum expected return I can achieve?

These are dual formulations of the same problem. They produce the same curve.

To see why a curve emerges, think about what happens in return-volatility space as you trace across all possible portfolios. You can put everything in one asset — that gives you one point. You can mix two assets in various proportions — that gives you a curved arc of points, bulging toward lower volatility than either asset alone when the assets are imperfectly correlated. Add more assets and more arcs intersect; the set of achievable portfolios fills in a lens-shaped region. The left edge of that region — where no portfolio has a lower volatility at the same return, and no portfolio has a higher return at the same volatility — is the efficient frontier.

![Scatter of points in (volatility, return) space representing](images/09-portfolio-construction-fig-01.png)
*Figure 9.1 — Scatter of points in (volatility, return) space representing*

Two points on the frontier deserve names.

The minimum-variance portfolio is the leftmost point — the lowest volatility achievable with this asset universe, regardless of return. An investor who cares only about stability, who would accept lower expected return in exchange for never seeing large swings, belongs here.

The maximum-Sharpe portfolio is the point where a line drawn from the risk-free rate is tangent to the frontier. The Sharpe ratio is:

$$S = \frac{E(R) - r_f}{\sigma}$$

It measures how much excess return you collect per unit of volatility accepted. The maximum-Sharpe portfolio is the most efficient use of risk in the asset universe — the portfolio where you get the most expected return for each unit of volatility you take on.

The operational procedure: feed in expected returns, volatilities, and the correlation matrix. Solve the constrained optimization — minimize portfolio variance subject to the portfolio achieving some target expected return, the weights summing to one, and no weight being negative. Repeat for every target return from the minimum to the maximum. The result is the frontier.

The math is well-understood quadratic programming and runs in any portfolio optimization software, or with a few dozen lines of Python. The difficulty is not the computation. It is the inputs.

---

Let me describe the three inputs and tell you what is wrong with each.

Expected returns are typically estimated from long-run historical averages, sometimes adjusted by analysts with specific views. The problem: historical averages are biased estimators of future returns. US large-cap equity has returned roughly 10–11% annualized over the past century, but that period includes a uniquely favorable combination of demographic tailwinds, technological expansion, dollar reserve currency status, and starting-valuation effects. Whether the next twenty years will replicate those conditions is a question the historical average cannot answer. A one-percentage-point error in the assumed expected return on a major asset class can swing the optimizer's recommended allocation by thirty percentage points or more.

Volatilities are also estimated from historical data. These are more stable than expected returns — volatility tends to cluster, mean-revert, and behave somewhat predictably. But they are not constants. Volatility in 2008 was roughly triple its pre-crisis level. The frontier constructed from 2006 historical volatility looked nothing like the actual risk being carried.

The correlation matrix — every pairwise correlation between assets, again from history — is the least stable of the three inputs. In normal markets, equity-bond correlations run slightly negative; in crisis markets they can spike toward positive. Equity-equity correlations across regions and sectors that look modest in calm periods converge toward one during global stress events. The optimizer sees the calm-period correlations and builds a portfolio that looks highly diversified; the crisis delivers something much less so.

| Asset pair | Calm-period correlation | Crisis-period correlation (2008) | Direction of change |
|---|---|---|---|
| **US equity / International equity** | 0.65 | 0.92 | ↑ — diversification benefit collapses just when needed |
| **US equity / Aggregate bonds** | -0.10 | +0.30 | ↑ — sign flips; the diversifier becomes a co-mover |
| **US equity / Long Treasuries** | -0.30 | -0.45 | ↓ (more negative) — Treasuries deliver in crisis as expected |
| **Aggregate bonds / TIPS** | 0.85 | 0.45 | ↓ — credit-bond correlations break in crisis |

*Equity-equity correlations converge toward 1 in crisis. Equity-bond correlations can shift sign. The optimizer trained on calm-period covariances cannot see this — and the portfolio it builds is exactly wrong about which assets diversify when diversification is most needed.*

The investor who feeds these three imperfect inputs into a mathematically exact optimizer gets an output that is only as reliable as the inputs warrant — which is to say, a useful starting point subject to wide uncertainty bands, not a precise answer. Markowitz knew this. The profession sometimes forgets it.

---

Maya picks a deliberately simple universe of six assets, all available as low-cost ETFs at any retail brokerage:

| Asset | ETF | Expected return | Volatility |
|---|---|---:|---:|
| US large-cap equity | VTI | 11% | 16% |
| US small-cap equity | VB | 10% | 21% |
| International developed equity | VEA | 7% | 17% |
| US aggregate bonds | BND | 3% | 6% |
| Long-term Treasuries | VGLT | 2.5% | 12% |
| TIPS | VTIP | 3.5% | 5% |

The equity-equity correlations run 0.60 to 0.85. Equity-bond correlations are near zero or slightly negative. Bond-bond correlations sit around 0.50 to 0.80.

She runs the optimization and pulls three portfolios off the resulting frontier:

| Portfolio | VTI | VB | VEA | BND | **VGLT** | VTIP | E(R) | σ |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Min-variance | 5% | 0% | 5% | 60% | **0%** | 30% | 4.0% | 4.5% |
| Max-Sharpe | 35% | 5% | 15% | 25% | **0%** | 20% | 7.2% | 9.5% |
| 7% target | 30% | 5% | 15% | 30% | **0%** | 20% | 7.0% | 9.0% |

Look at the bolded column. Long-term Treasuries: zero, zero, zero. At every point on the frontier, the optimizer is putting nothing in long-dated Treasuries.

This is the thing that tripped me up the first time I ran this.

---

The optimizer is not broken. Let me show you exactly why it makes this choice.

Long-term Treasuries have a 12% annualized volatility — nearly as high as international developed equity — for a 2.5% expected return. The optimizer is trying to minimize variance at any target return level. For any volatility it would accept from long Treasuries, it can construct a better alternative: mix the aggregate bond fund (6% vol, 3% return) with TIPS (5% vol, 3.5% return). That combination achieves lower volatility at a higher expected return than long Treasuries offer. Long Treasuries are dominated — their risk-return profile is reachable as a combination of other assets in the universe, but at better terms.

The technical name for this: long Treasuries lie inside the efficient frontier rather than on it. The optimizer correctly assigns them zero weight.

This is not just a technical observation. It reveals the precise way that mean-variance optimization fails to capture something important.

Long-term Treasuries do something specific that the optimizer cannot see: they appreciate dramatically in deflationary recessions. When growth expectations collapse, when credit spreads blow out, when investors flee to safety — long Treasuries are the thing they flee to. In 2008, when virtually every other asset fell together, long Treasuries returned roughly 25%. That behavior — the thing that makes them valuable — is a crisis-regime correlation that is completely absent from the calm-period historical data feeding the optimizer.

A mean-variance optimizer uses one correlation matrix. The real world uses two: one for normal times and one for crises. The optimizer built from normal-time data does not know about crisis-time behavior. When Priya's mother's portfolio hits a 2008-shaped event — which it will, at some point over a twenty-year horizon — she needs the long Treasury position that the optimizer just set to zero.

Maya's response is to override the optimizer. She adds a 5% floor on long Treasuries and rebalances the rest of the weights accordingly. The recommended portfolio:

| Asset | Vehicle | Weight |
|---|---|---:|
| US large-cap equity | VTI | 30% |
| US small-cap equity | VB | 5% |
| International developed equity | VEA | 15% |
| US aggregate bonds | BND | 30% |
| Long-term Treasuries | VGLT | 5% |
| TIPS | VTIP | 15% |

Six funds. Implementable through any retail brokerage on a Tuesday afternoon. Weighted expense ratio roughly four basis points — about $480 per year on Priya's mother's $1.2 million.

Expected return: roughly 7% nominal. Expected volatility: roughly 9.5% annualized. What that volatility means concretely: in any single year, returns will fall within approximately one standard deviation of the expected return with about two-thirds probability. A drawdown of roughly 20% is something the portfolio will experience at least once over a twenty-year horizon with high probability — that is the trade being purchased. Not a guarantee against bad years. A structure that, on average, compounds at roughly 7% and bears its losses with statistical regularity.

---

Maya does not stop at the optimizer output. Three checks before the recommendation leaves her hands.

Does the portfolio look like what informed practitioners actually hold? A roughly 65/35 stock-bond split, modest international exposure, inflation protection via TIPS, a small long-Treasury allocation — this is entirely conventional and defensible for a 65-year-old with a 20-year horizon. If the optimizer had produced something exotic — 40% small-cap, 0% bonds, large emerging-market exposure — that would be a flag, not a finding.

Are the expected return inputs plausible? US large-cap at 11% is near the long-run historical average. The bond allocations at 2.5–3.5% are consistent with current yields. If the optimizer needed TIPS to return 8% to justify its weight, the weight would be suspect.

She also runs the same specification through two other models. Both return portfolios whose weights cluster within five percentage points of each fund, and both return the same qualitative shape: heavy US equity, meaningful bond allocation, a slice of international and inflation protection. The optimizer output survives independent implementations.

---

I want to name three things that mean-variance optimization genuinely cannot handle, because omitting them from the analysis does real damage.

Taxes. The optimizer uses pre-tax expected returns. The after-tax return depends on where each asset is held — bonds in a tax-deferred account produce a different after-tax outcome than bonds in a taxable account; TIPS held outside a tax-deferred account generate phantom income on inflation adjustments that is taxable even though you haven't received cash. The optimal pre-tax portfolio and the optimal after-tax portfolio are not the same thing. For Priya's mother, the right conversation is about which accounts hold which assets, not just the aggregate weights.

Liabilities and goals. The optimizer treats the objective as "maximize Sharpe ratio." Real goals are more specific: have at least $X by year Y, generate $Y of income beginning in year Z, maintain a floor against running out of money by age 90. These concrete goals reshape the framework into what is called liability-driven investing — where the appropriate risk is defined not by volatility relative to a market index but by the shortfall risk relative to a specific target. Priya's mother's five-percent-real target is a liability structure. A pure Sharpe-maximizing optimizer does not know about it.

Behavior. A portfolio that is theoretically optimal but psychologically intolerable for the actual investor is worse than a slightly suboptimal one they can hold through a bad year. The optimizer has no model of human behavior. It does not know that Priya's mother might watch her $1.2 million fall to $960,000 in a downturn and sell everything at the bottom. The best portfolio for her is the most aggressive one she can stick with, which may be less aggressive than the frontier says is optimal. The right answer involves a conversation about what happened to her decision-making in 2008 or 2020 — not just an optimization.

---

The deepest problem with mean-variance optimization is its sensitivity to input errors.

A one-percent change in the assumed expected return on US large-cap equity — not a big assumption, entirely within the estimation uncertainty — can shift the optimizer's recommended allocation by thirty percentage points or more. The reason is that the optimizer treats expected returns as precisely known. It will exploit a one-percent edge with maximum aggression, concentrating heavily into whatever asset appears to offer that edge. In reality the one-percent edge is noise, and the resulting concentration is unjustified.

This is why DeMiguel, Garlappi, and Uppal (2009) found that a naive equal-weighted portfolio beats mean-variance-optimal portfolios out-of-sample in most of their tests. The equal-weighted portfolio ignores the uncertain input estimates entirely. The mean-variance portfolio exploits them with precision — and is precisely wrong.

The lesson is not that you should ignore the optimization. The lesson is that you should use the optimization to identify the structure of the solution — which asset classes belong, roughly what their role is, approximately what the risk-return tradeoffs look like — and then treat the specific weights as a starting point subject to expert judgment and sanity-checking, not as a precise answer.

What emerges from this process is not the optimal portfolio. It is a good portfolio: defensible from the inputs, robust to plausible variation in those inputs, informed by what the optimizer cannot see, and implementable by an actual investor on an actual Tuesday. That is what honest portfolio construction actually delivers.

---

The chapter would be incomplete without naming the piece of portfolio construction that nobody emphasizes enough: rebalancing.

A portfolio built with specific target weights drifts as assets perform differently. After two years of strong equity returns, a 65/35 portfolio may have drifted to 75/25 — with the risk profile and correlation properties of a 75/25 portfolio, not the intended 65/35. The investor who chose 65/35 for a specific risk reason is now unknowingly holding 75/25.

Rebalancing returns the portfolio to its target weights by selling what has appreciated and buying what has lagged — which is psychologically counter-cyclical and mechanically essential. Maya's recommendation for Priya's mother: review weights quarterly; rebalance any asset that has drifted more than five percentage points from its target; rebalance fully each January regardless; use new contributions and dividends to rebalance preferentially before triggering tax events through sales.

This protocol is not complicated. It is also almost never followed spontaneously by investors who are not explicitly committed to it in advance. The portfolio that is built correctly and never rebalanced gradually converges toward a portfolio that is mostly the best-performing asset — which is almost always the riskiest asset — which is almost always the worst thing to be holding heavily in the next drawdown.

![Two line charts side by side, both showing](images/09-portfolio-construction-fig-02.png)
*Figure 9.2 — Two line charts side by side, both showing*

---

*What would change my mind.* The chapter accepts mean-variance optimization as the right framework for portfolio construction while acknowledging its practical fragility. I would revise this position if evidence accumulated that simpler portfolio rules — equal weighting, risk-parity weighting, value-weighted indexing — consistently outperformed mean-variance optimization after costs, taxes, and rebalancing frictions, across a wide range of historical periods and asset universes. The DeMiguel-Garlappi-Uppal result is the most serious version of this argument. It is not decisive — it depends on specific backtesting choices and asset universes — but it is serious enough that I hold the mean-variance framework with genuine uncertainty. The strongest form of the argument against it: estimation error in expected returns is large enough to swamp the precision of the optimization, so the optimizer is optimizing noise. If that is right, the right portfolio is not a refined mean-variance estimate but a simpler rule robust to input uncertainty. I think the mean-variance framework is still worth knowing because it structures the thinking correctly — it forces you to ask about expected returns, volatilities, and correlations, which are the right questions — even if the resulting weights should be held loosely.

*Still puzzling.* The single biggest unresolved problem in portfolio construction is the one I named but didn't solve: how to estimate expected returns. Historical averages are biased toward the past conditions that produced them. CAPM-derived expected returns (Chapter 11) are theoretically grounded but require estimates of the equity risk premium and beta, both of which carry their own estimation error. Yield-based forecasts for bonds are the most reliable component — the current yield is a reasonable predictor of the bond's return over its duration — but yield-based forecasts for equity are contested. The honest position is that expected returns cannot be estimated with confidence, which means the efficient frontier cannot be located with confidence, which means the "optimal" portfolio weights are uncertain in a range wide enough to make precision feel fraudulent. The right response is not to abandon the framework but to hold its outputs loosely, check them against multiple methods, and use the sanity-check rather than the optimizer as the final arbiter of the recommendation. Chapter 11 introduces CAPM, which tries to derive expected returns from the structure of the market itself rather than from history. It is mathematically beautiful. It is, in practice, only slightly less wrong than historical averages. The book does not have a clean answer here. Neither does the discipline.

---

*Coming up.* This chapter stayed on the curved efficient frontier, where all portfolio construction involves actual assets with actual weights. Chapter 10 introduces the risk-free asset — cash, T-bills — and shows what happens to the geometry when you can combine any risky portfolio with a position in cash. The frontier collapses to a straight line, the optimal risky portfolio becomes the same for every investor, and the only remaining question is how far along that line each investor should stand. That is the Capital Allocation Line, and it completes the portfolio theory that Markowitz started.

---

## Exercises

### Warm-up

**1.** Two assets have the following properties: Asset A has an expected return of 8% and volatility of 14%; Asset B has an expected return of 4% and volatility of 6%. Their correlation is −0.20. (a) Without computing the exact formula, explain in one sentence why a portfolio combining A and B can have lower volatility than either asset alone. (b) If the correlation were +1.0 instead, what would happen to the diversification benefit? *(Tests: core Markowitz insight — correlation drives the benefit.)*

**2.** An optimizer is fed the following inputs for a two-asset universe: both assets have 10% expected return, but Asset X has 20% volatility and Asset Y has 10% volatility, with a correlation of 0.50. (a) Which asset should receive higher weight in the minimum-variance portfolio — X or Y? (b) What is the expected return of the minimum-variance portfolio, and why? *(Tests: minimum-variance portfolio intuition; equal-return case.)*

**3.** A portfolio has a Sharpe ratio of 0.45. The risk-free rate is 4%. (a) If the portfolio's expected return is 13%, what is its volatility? (b) A second portfolio has the same volatility but a Sharpe ratio of 0.60. What is its expected return? *(Tests: Sharpe ratio formula mechanics.)*

### Application

**4.** You are building a portfolio for a 40-year-old with a 25-year horizon and moderate risk tolerance. You run a mean-variance optimizer on a five-asset universe and find that the maximum-Sharpe portfolio allocates 0% to international developed equity. Describe two distinct reasons — one mathematical, one behavioral — why you might override this result and add a 10–15% international allocation anyway. *(Tests: optimizer override judgment; dominated-asset logic vs. crisis-regime reasoning.)*

**5.** Maya's recommended portfolio for Priya's mother has a 9.5% expected volatility. (a) Construct the approximate 68% and 95% confidence intervals for one-year returns, assuming returns are normally distributed around the 7% expected return. (b) What is the approximate probability of a negative return in any single year? (c) Over a 20-year horizon, roughly how many years should the investor expect to see a negative return? *(Tests: practical interpretation of volatility as a confidence interval; connecting σ to real investor experience.)*

**6.** A $1.2 million portfolio is built with the target weights from Maya's final recommendation. After 18 months of strong equity performance, the actual weights have drifted to: VTI 42%, VB 7%, VEA 18%, BND 22%, VGLT 4%, VTIP 7%. (a) Which assets have drifted more than 5 percentage points from their targets? (b) Assuming no tax constraints, describe the trades needed to rebalance to target. (c) If the investor uses $30,000 of new contributions to rebalance first, which funds should receive those contributions, and in what order of priority? *(Tests: rebalancing protocol applied to a real drift scenario.)*

### Synthesis

**7.** The chapter argues that mean-variance optimization uses one correlation matrix while the real world uses two. Using the long-Treasury example from the chapter, explain: (a) why long Treasuries are correctly assigned zero weight by the optimizer given the calm-period inputs, (b) why they belong in the portfolio anyway, and (c) what this reveals about the general class of assets that mean-variance optimization will systematically underweight. *(Tests: crisis-regime vs. calm-regime correlation; generalizing the long-Treasury lesson.)*

**8.** DeMiguel, Garlappi, and Uppal (2009) found that a naive equal-weighted portfolio outperforms mean-variance-optimal portfolios out-of-sample. (a) Explain in one paragraph why this result is theoretically surprising given what mean-variance optimization is designed to do. (b) Explain in one paragraph why the result is practically unsurprising given what the chapter says about estimation error. (c) Does this finding mean you should build equal-weighted portfolios? What nuance does the chapter provide? *(Tests: connecting input sensitivity, optimization precision, and out-of-sample performance — synthesis of the chapter's central tension.)*

**9.** Priya's mother tells Maya: "I don't care about Sharpe ratios. I just need to know I won't run out of money before I'm 90." Explain why this goal cannot be directly addressed by a standard mean-variance optimizer, what framework better captures it, and what additional information Maya would need to implement that framework properly. *(Tests: liability-driven investing as an alternative to Sharpe maximization; connecting portfolio theory to real investor goals.)*

### Challenge

**10.** The chapter notes that a 1% change in an assumed expected return can shift the optimizer's recommended allocation by 30 percentage points or more. Design a simple two-asset thought experiment — name the assets, their expected returns, volatilities, and correlation — and show numerically or by argument why a small change in one asset's expected return can produce a dramatically different allocation. Then propose one practical portfolio construction rule that would make the resulting allocation more robust to this sensitivity, and explain the trade-off your rule introduces. *(Tests: input sensitivity as a design problem; robustness rules and their costs — open-ended, goes beyond the chapter's direct examples.)*

---

###  LLM Exercise — Chapter 9: Portfolio Construction

**Project:** Maya's Memo, Built Across the Course
**What you're building this chapter:** The Portfolio Fit section of the memo: where does your position sit relative to the efficient frontier built from your candidate universe?
**Tool:** Claude Code

---

**The Prompt:**

```
I'm working on Maya's Memo. The single-position analysis (Chs 2–7) and the diversification decomposition (Ch 8) are in the project.

Chapter 9 taught:
- **Markowitz's mean-variance frontier**
- **The tangency portfolio** that maximizes Sharpe
- **What the optimizer cannot see**: regime change, fat tails, parameter uncertainty
- The case for *and* against running the optimizer on real data

Scaffold `analysis/09-frontier.py`:

1. **Load returns and the covariance matrix.** Use the same universe as Chapter 8 (the position + 5–10 candidate peers + benchmark).

2. **Build the efficient frontier.** Compute the minimum-variance portfolio at each of 50 target expected returns. Plot the frontier. Mark:
   - The minimum-variance portfolio
   - The tangency portfolio (max Sharpe)
   - 100% in your position alone
   - The benchmark (SPY)

3. **Where is your position?** Is it on the frontier? Inside the frontier? Outside? Report its distance from the frontier in Sharpe-ratio terms.

4. **What weight does the optimizer give it?** Report the optimizer's weight on your position in the tangency portfolio. State the most likely reason if it's much higher or lower than your own intuition (the optimizer doesn't see what you see, or vice versa).

5. **The three failure modes.** For your specific universe, name the most plausible failure mode the optimizer cannot see:
   - **Regime change**: covariance matrix from the lookback window may not hold
   - **Fat tails**: the historical worst case underestimates the future worst case
   - **Parameter uncertainty**: small changes in expected returns produce wildly different optimal weights

6. **Save `analysis/09-frontier.md`** with the frontier plot, the optimizer's tangency weights, the position's location relative to the frontier, and a paragraph naming the failure mode that most threatens the result.

The script should run with `python analysis/09-frontier.py --ticker [TICKER] --peers [TICKER1,...]`.
```

---

**What this produces:** A runnable script `analysis/09-frontier.py` plus `analysis/09-frontier.md` containing the efficient frontier plot, the optimizer's tangency weights, the position's location, and the failure-mode paragraph.

**How to adapt this prompt:**

- *For your own project:* Replace any bracketed domain placeholder with your specific instrument, ticker, or context. The exercise structure is instrument-agnostic; the content is yours.
- *For ChatGPT / Gemini:* Works as-is. For ChatGPT, save the running memo to a Custom GPT instead of a Claude Project. For Gemini, paste the project's accumulated section files into the context window each session.
- *For Claude Code:* Right tool — this is real numerical optimization. Claude Code can use `cvxpy` or `scipy.optimize` to build the frontier in 30–50 lines.
- *For a Claude Project:* Append to the project. The tangency portfolio's weight on your position becomes the input to Chapter 10's y* recommendation and Chapter 13's capstone.

**Connection to previous chapters:** Chapter 8 decomposed the position's variance; Chapter 9 builds the universe-level frontier and locates the position on it.

**Preview of next chapter:** Chapter 10 takes the tangency portfolio and asks: how much of your wealth should sit in it?

---

##  AI Wayback Machine
The ideas in this chapter didn't appear from nowhere. **James Tobin** was proving the *separation theorem* in 1958 — the result that any investor's optimal portfolio can be built from just two ingredients: the risk-free asset and the single tangency portfolio, regardless of risk preferences decades before most people had heard of the efficient frontier and the construction of an optimal portfolio. Here's a prompt to find out more — and then make it better.

![James Tobin, c. 1970s. AI-generated portrait based on a public domain photograph (Wikimedia Commons).](images/james-tobin.jpg)
*James Tobin, c. 1970s. AI-generated portrait based on a public domain photograph.*

**Run this:**

```
Who was James Tobin, and how does his 1958 *separation theorem* — that the choice of risky portfolio is independent of how much risk an investor wants to take — connect to the chapter's apparatus for constructing portfolios on the efficient frontier? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.
```

→ Search **"James Tobin"** on Wikipedia after you run this. See what the model got right, got wrong, or left out.

**Now make the prompt better.** Try one of these:

- Ask it to explain *two-fund separation* in plain language, as if you've never seen an efficient frontier diagram
- Ask it to compare Tobin's separation theorem to the chapter's construction of the tangency portfolio
- Add a constraint: "Answer as if you're writing the rationale for offering only two products to an investor: the risk-free asset and the tangency portfolio"

What changes? What gets better? What gets worse?
