# Chapter 15 — How to Think about Investing

**Suggested titles**
1. The Investor's Framework
2. Risk, Return, and What to Do With $50,000
3. Asset Allocation, Diversification, and the Indexing Question

**TL;DR.** Personal investing is the application of everything in this book to the question of what to do with money you actually have. The framework rests on three pillars: matching portfolio risk to time horizon (asset allocation), diversifying within asset classes to eliminate firm-specific noise, and accepting that systematic risk is what gets rewarded. The empirical record on active management is humbling — most professional managers underperform low-cost index funds after fees, and the indexing case for individual investors is strong.

---

## The puzzle of $50,000

You have $50,000. What should you do with it?

The answer, like everything in this book, depends on the question hidden inside the question. *When* do you need the money? *How* much loss can you tolerate without changing your behavior? *What* is the alternative use of the cash?

If you need the money in two years for a house down payment, the answer is mostly cash and short-term bonds. The 2008-2009 stock market crash would have cost a homebuyer with all-equity savings about half their down payment — a catastrophic outcome that eight years of strong returns afterward could not undo for someone who had to buy a house in 2009.

If you don't need the money for thirty years, the answer is mostly equities. The same 2008-2009 crash would have been a temporary drawdown on the way to substantial wealth accumulation by 2025.

Same $50,000. Same investor. Radically different right answers.

This chapter is about the framework that produces the right answer. It synthesizes the tools from Chapters 1–14 into the practical decision space of personal investing. For students who will end up making personal portfolio decisions for themselves and possibly for clients, the framework here is the day-one foundation.

For the equity research project, this chapter provides the personal-investor lens on the company you've been analyzing. Even if your DCF says the stock is undervalued, the question for an individual investor is *should it be in the portfolio*, not just *is it underpriced*. Position sizing, portfolio fit, and tax considerations matter alongside the valuation work.

---

## Learning objectives

After working through this chapter, you should be able to:

- Articulate an investment policy statement (IPS) — risk tolerance, time horizon, return objectives, allocation rules.
- Compute holding-period and annualized returns; distinguish dividend yield from capital gain.
- Apply diversification principles to design a multi-stock portfolio.
- Use Sharpe ratio, Treynor ratio, and Jensen's alpha to evaluate performance.
- Explain the empirical evidence for and against active management.
- Construct a defensible asset allocation for a hypothetical investor.

**Prerequisites.** Chapters 11-14 (stocks, market history, statistics, CAPM).

---

## Concept 1 — The investor's framework

Before computing returns or building portfolios, install the framework that orders the decisions.

### What you're solving for

An investor is trying to do four things, which compete with each other:

1. **Achieve specific goals** — retirement, a house, education, charitable giving — at specific future times.
2. **Match risk to tolerance** — including the risk of changing behavior at the wrong moment (selling during a panic).
3. **Maximize after-tax, after-fee returns** — the only returns that actually compound to wealth.
4. **Stay disciplined** — the hardest of the four, and the one where most investors lose to themselves.

The first three are technical. The fourth is psychological and is where most of the empirical underperformance of individual investors comes from. We'll touch on all four.

### Time horizon and asset allocation

The single most important determinant of an appropriate investment strategy is **time horizon** — when you'll need the money. Different time horizons admit different levels of variance.

A rough hierarchy:

| Time horizon | Tolerable variance | Typical allocation |
|---|---|---|
| < 1 year | None | Cash, T-bills |
| 1-3 years | Low | Short-term bonds, T-bills |
| 3-7 years | Moderate | Mix of bonds and stocks |
| 7-15 years | Higher | Mostly stocks, some bonds |
| 15-30+ years | High | Mostly equities, small fixed-income |

The logic: over short horizons, market downturns can permanently impair specific goals (you have to sell at the bottom because you need the money). Over long horizons, downturns are recoverable, and the equity premium has time to compound.

The classic shorthand is **age in bonds** — at age 30, hold 30% in bonds; at age 60, hold 60%. The rule is too crude for serious planning (it ignores wealth, other income sources, specific goals) but captures the right qualitative shape: bond allocation rises with age as horizon shortens.

More sophisticated approaches use **glide paths** — the asset allocation declines smoothly as the target date approaches. Target-date funds (the dominant default option in 401(k) plans) implement this automatically.

### Risk tolerance vs. risk capacity

Two different things, often conflated.

**Risk capacity** is *how much loss you can absorb without changing your behavior or sacrificing goals*. A retiree drawing on savings has low risk capacity; a 25-year-old with stable income has high risk capacity.

**Risk tolerance** is *how much loss you can stomach emotionally*. This is partly hardwired and partly experience-dependent. Investors who lived through 2008 often have lower risk tolerance even if their financial position has fully recovered.

A well-designed portfolio matches the *lower* of the two. An investor with high capacity but low tolerance who builds a 100% equity portfolio will sell during the next drawdown and crystallize losses they didn't have to take.

### The investment policy statement

A useful discipline: write down your investment plan *before* making decisions. The standard format is the **investment policy statement (IPS)**, which captures:

- **Goals**: what you're investing for, with target amounts and dates.
- **Risk tolerance and capacity**: explicit limits on how much loss you'll accept.
- **Asset allocation**: target weights to stocks, bonds, cash, by category.
- **Rebalancing rules**: when and how often to bring allocations back to targets.
- **Selection rules**: low-cost index funds vs. active management; specific accounts (401(k), IRA, taxable).
- **Tax considerations**: tax-advantaged accounts, asset location, harvest losses.

Writing an IPS before market stress means having a plan to follow when stress arrives. The IPS is the antidote to behavioral mistakes — it gives you something to refer to that's not "what I feel like doing right now."

For the equity research project, your individual stock pick fits inside the IPS; it does not replace it. A 30-year-old with $50,000 might decide that Apple looks attractive, but Apple shouldn't be 100% of the portfolio regardless of how attractive it looks.

↳ **Dig Deeper — Behavioral finance and the gap between rational and actual*

*Modern Portfolio Theory assumes rational investors. Real investors have well-documented behavioral biases — loss aversion, recency bias, overconfidence, herding. Behavioral finance (Kahneman, Thaler, Shiller) is the field that maps when actual investing diverges from rational.*

**Prompt:**
> Summarize five core findings from behavioral finance that affect investing decisions: (1) loss aversion (Kahneman-Tversky), (2) the disposition effect (selling winners, holding losers), (3) overconfidence and trading frequency, (4) herding/momentum behavior, (5) recency bias in return-extrapolation. For each, describe one piece of empirical evidence and one practical implication for an individual investor's discipline.

**What to do with the output:** Save it. The investment policy statement is partially a tool for managing your own behavioral biases — knowing them helps you write a better IPS.

### The trade-off (concept 1)

The investor's framework trades **simple rules against personalized optimization**. A target-date fund is one decision and gives you a passable allocation for life. A custom-designed portfolio with explicit IPS, tax planning, and rebalancing rules can outperform on the margin but requires active attention. For most investors, the target-date fund or a simple two-fund portfolio (broad equity index + broad bond index) is good enough — and good enough beats the more elaborate approach if "elaborate" leads to behavioral mistakes.

### Common misconceptions

- *"Aggressive investing means high risk tolerance."* It might mean the investor has high risk capacity (long horizon) — or it might mean they're not honestly assessing tolerance. Both should be considered.
- *"Volatile years can be made up."* They can — over time. The investor who needs the money during the volatility cannot wait for the recovery.

---

## Concept 2 — Diversification: how many stocks, what kinds

Diversification is the simplest and most reliable risk-reduction technique. It works because individual stocks have **firm-specific risk** that gets averaged out across many holdings.

### The math (briefly)

Recall from Chapter 13: portfolio variance with two assets is

$$\sigma_p^2 = w_A^2 \sigma_A^2 + w_B^2 \sigma_B^2 + 2 w_A w_B \rho_{A,B} \sigma_A \sigma_B$$

When the correlation $\rho < 1$, the portfolio variance is less than the weighted average of the individual variances. As more assets are added (with correlations less than 1), the portfolio variance keeps falling — though with diminishing returns.

### Empirical results

**Meir Statman's classic result:** a 12-stock portfolio captures most of the diversification benefit. Going from 1 stock to 12 stocks dramatically reduces portfolio standard deviation; going from 12 to 50 reduces it modestly; going from 50 to 500 barely reduces it at all.[^1]

[^1]: Statman, "How Many Stocks Make a Diversified Portfolio?" *Journal of Financial and Quantitative Analysis*, 1987.

**The OpenStax data on real stocks:** Delta Airlines alone had a standard deviation of 51.9% over 2011-2020. Combining DAL with Southwest (correlation 0.87) reduced std dev to 49.1% — a small benefit because they're in the same industry. Combining DAL with Exxon (correlation 0.35) reduced std dev to 30.4% — a much larger benefit because the industries are different.

The lesson: **correlation matters as much as count.** Twelve technology stocks is less diversified than four stocks across technology, finance, consumer, and industrial sectors.

### Practical guidelines

A workable approach:

1. **Use index funds where possible.** A broad equity index (S&P 500 or total stock market) gives you 500-3,500+ holdings instantly at low cost. This is the cheapest and most reliable diversification available.
2. **If picking individual stocks**, hold at least 10-15 with low cross-correlations across sectors and industries.
3. **Limit single-stock concentration**. A common rule: no more than 5% of the portfolio in any single position. (Some investors go higher; some go lower.)
4. **Limit single-sector concentration**. The Cramer rule of "no more than 20% in one sector" is reasonable.
5. **Diversify internationally** if possible. US-only portfolios have country-specific risk; adding international exposure reduces it.

### What diversification cannot do

Diversification eliminates **firm-specific risk**. It does *not* eliminate **systematic (market) risk**. When the entire market falls 30% in a recession, every diversified portfolio falls roughly 30%. Diversification doesn't help.

In genuine crises, correlations also rise — the "correlation crisis" of 2008 saw asset classes that had been historically uncorrelated all fall together. International equities, REITs, commodities, and high-yield bonds all crashed alongside US stocks. Only Treasuries provided meaningful diversification in 2008. Diversification still helps in crises, but less than its smoothness in normal markets would suggest.

For 2022, the failure was different: stocks and bonds *both* fell because rising rates hurt both simultaneously. The 60/40 portfolio's worst year since the 1930s. Diversification across asset classes can fail when the same shock hits multiple asset classes through different channels.

The honest framing: diversification is necessary but not sufficient. It cannot replace good asset allocation, and it cannot insure against systematic shocks.

### Worked example — building a diversified equity portfolio

Suppose you want a 12-stock portfolio. A reasonable approach:

| Sector | Allocation | Sample names |
|---|---|---|
| Technology | 20% | Apple, Microsoft, Alphabet |
| Healthcare | 15% | Johnson & Johnson, UnitedHealth |
| Consumer staples | 12% | Procter & Gamble, Coca-Cola |
| Financials | 12% | Berkshire Hathaway, JPMorgan |
| Industrials | 10% | Caterpillar |
| Energy | 8% | Exxon Mobil |
| Materials | 8% | Linde |
| Communications | 8% | Verizon |
| Real estate | 7% | (REIT) |

The balance roughly mirrors the S&P 500's sector weights with small tilts. For an analyst doing fundamental research, this is the kind of structure that lets your individual stock picks (one or two per sector) replace the broad index without sacrificing diversification. If your work is good enough to outperform the index in a few specific picks, you keep the diversification while adding the alpha. If the picks underperform, you've added risk without reward.

↳ **Dig Deeper — The 4% rule and its critics**

*The "4% rule" — withdraw 4% of your initial portfolio per year (inflation-adjusted) and the portfolio should last 30 years — was popularized by William Bengen in 1994. It's been the dominant retirement-planning rule of thumb for thirty years. Recent research suggests it may be too aggressive in low-return environments and too conservative in others.*

**Prompt:**
> Explain Bengen's original 4% rule and the empirical analysis behind it. Then summarize three lines of recent critique: (1) the Trinity Study confirming and extending Bengen's findings, (2) Wade Pfau's research suggesting lower safe withdrawal rates in low-yield environments, (3) "guardrail" approaches (Klinger, Guyton-Klinger) that adjust withdrawals based on portfolio performance. What's a defensible withdrawal rate for a 65-year-old retiring today, and what assumptions does it depend on?

**What to do with the output:** Save it. Personal-investing decisions ultimately come back to safe-withdrawal-rate questions; this gives you the modern landscape.

### The trade-off (concept 2)

Diversification trades **the chance of large outperformance against the assurance of avoiding catastrophic single-stock losses**. A concentrated portfolio (5 stocks) can substantially outperform if you pick well. It can also be wiped out by a single Enron-style failure. A diversified portfolio gives up the upside but eliminates the catastrophic downside. For long-term wealth-building, the diversified path is almost always the right one.

### Common misconceptions

- *"Owning 50 stocks is more diversified than 12."* If they're correlated (e.g., all tech), it's not much more diversified. If they're uncorrelated, the marginal benefit beyond ~15-20 is small.
- *"Diversification reduces returns."* It reduces *variance*. Expected return is unchanged (you still earn the expected returns of the assets you hold). Diversification doesn't compromise expected return; it only reduces realized variance around it.

---

## Concept 3 — Performance evaluation and the active/passive question

Once you have a portfolio, how do you measure whether it's doing well? Three metrics from Chapter 14, each useful for different purposes.

### Sharpe ratio (revisited)

Excess return per unit of total risk:

$$\text{Sharpe} = \frac{\bar{R}_p - R_f}{\sigma_p}$$

Useful for comparing portfolios in absolute terms. A higher Sharpe means more return per unit of variance. The S&P 500's long-run Sharpe has been about 0.4. Active managers who consistently produce Sharpe ratios above 0.6 over long periods are exceptional.

### Treynor ratio

Excess return per unit of *systematic* (market) risk:

$$\text{Treynor} = \frac{\bar{R}_p - R_f}{\beta_p}$$

Used for portfolios already part of a diversified larger portfolio, where idiosyncratic risk doesn't matter. For an investor whose only risk is the manager's exposure to market moves, Treynor is the more relevant metric.

### Jensen's alpha

The portion of return that *exceeds* what CAPM predicts given the portfolio's beta:

$$\alpha = \bar{R}_p - [R_f + \beta_p (\bar{R}_m - R_f)]$$

A positive alpha means the manager has produced returns above what their market exposure would justify. This is what active managers are paid for. The empirical record: most active managers don't sustain positive alpha after fees.

### Worked example — comparing two managers

Mr. Wong and Ms. Petrov each ran a portfolio over 10 years.

| Manager | Return | Std Dev | Beta |
|---|---|---|---|
| Wong | 14% | 8% | 1.2 |
| Petrov | 16% | 10% | 1.6 |

Risk-free rate: 2%. Market return: 11%. Market premium: 9%.

For Wong:
- Sharpe: $(14-2)/8 = 1.50$
- Treynor: $(14-2)/1.2 = 10$
- CAPM expected: $2 + 1.2 \times 9 = 12.8\%$. Alpha: $14 - 12.8 = +1.2\%$.

For Petrov:
- Sharpe: $(16-2)/10 = 1.40$
- Treynor: $(16-2)/1.6 = 8.75$
- CAPM expected: $2 + 1.6 \times 9 = 16.4\%$. Alpha: $16 - 16.4 = -0.4\%$.

Petrov has higher absolute returns. Wong has better risk-adjusted performance on every metric. Wong's portfolio is doing more with less.

### The active vs. passive debate

Should you actively pick stocks (or hire someone to do it) or just buy the index?

The empirical case for **passive (indexing)**:

1. **Most active managers underperform.** The SPIVA (S&P Indices vs. Active) reports show that 80-90% of active US large-cap mutual fund managers underperform their benchmark over 15-20 year periods, after fees.[^2]
2. **The few who outperform are hard to identify in advance.** Past outperformance is a poor predictor of future outperformance.
3. **Costs compound.** A 1% annual expense ratio over 40 years turns $10,000 of equity savings into about $108,000 less than the same investment in a 0.05% index fund — over 25% of the index investor's wealth lost to fees.

[^2]: SPIVA U.S. Year-End reports, S&P Dow Jones Indices. `[verify]` for current data.

The case for **active (stock picking or hiring active managers)**:

1. **Some markets are less efficient.** Small-cap, emerging market, and fixed-income markets have higher proportions of active managers who outperform.
2. **The best managers do exist.** Buffett, Renaissance Medallion, a few others have generated decades of consistent alpha. The challenge is identifying them in advance.
3. **Indexing is a form of complacency.** Passive investing means you accept whatever the market does. Active investing means you have a view.

For most retail investors with 30+ year horizons, the empirical case strongly favors indexing. The cost savings are large, the behavioral discipline is easier, and the historical evidence consistently shows underperformance of active managers after fees.

For institutional investors, sophisticated investors with edges in specific niches, or investors who genuinely believe they have skill they can exploit, active strategies can be appropriate. The honest test: do you have a *defensible* reason to think you can beat the market after costs? If not, the passive default is probably right.

### Where the equity research project fits

The equity research project is a fundamental analysis exercise. It produces a defensible view on a single stock. That's valuable analytical training even if you ultimately put your savings in an index fund.

The project does not (by itself) imply that your subsequent investing should be active. It implies that you understand what active managers are trying to do, why most of them fail, and what the few successful ones are doing differently. Both the passive case and the active case become more informed.

For the project deliverable, the personal-investing implications of your work are part of the final report's executive summary. Position sizing, fit within a diversified portfolio, and the question of whether the analytical edge justifies the risk are all relevant.

### The trade-off (concept 3)

Active vs. passive trades **the cost of analysis (and behavioral discipline) against the potential for outperformance**. Passive is cheap and reliable. Active is expensive and unreliable. The rare combination of skill, discipline, and market opportunity that produces sustainable alpha is genuinely rare. Honest investors take the indexing default unless they have a specific reason to deviate.

### Common misconceptions

- *"Index funds are guaranteed to match the market."* They closely track the market, less their (low) expense ratios. Pure indexing produces market returns minus tiny tracking costs.
- *"I'll just buy the active funds that have outperformed lately."* This is "performance chasing." The empirical record is that recent outperformance is a poor predictor of future outperformance.

---

## Synthesis — the investor's playbook

Three concepts, one playbook:

1. **Match portfolio risk to time horizon and tolerance.** Long horizons can absorb equity variance; short horizons cannot. Write an investment policy statement. Stick to it.
2. **Diversify within asset classes.** Index funds are the cheapest reliable diversification. If picking individual stocks, hold at least 10-15 across uncorrelated sectors.
3. **Default to passive unless you have a defensible reason for active.** The empirical record favors indexing for most investors, most of the time.

The work in Chapters 1-14 made these statements concrete. TVM gives you the arithmetic for projecting goals into future dollar amounts. Statistics gives you risk measurement. CAPM gives you the cost-of-equity benchmark. Market history gives you the empirical context for setting expectations. This chapter integrates them into a usable investing framework.

For the project, the personal-investing perspective is the lens through which your equity research recommendation should be weighed. A "Buy" rating doesn't mean "put all your savings in this stock." It means "this stock is undervalued; the right amount to add to a diversified portfolio depends on your other holdings, your time horizon, and the strength of your conviction."

Chapter 16 takes the analytical machinery in a different direction — applying it to *corporate* investment decisions. The DCF math is the same; the question (should the firm undertake this project?) is different.

---

## Exercises

### Warm-up

**15.1** A stock you bought for $100 paid $3 in dividends and is now worth $120. Compute the dividend yield, capital gain yield, and total holding-period return.

**15.2** Define risk capacity and risk tolerance. How are they different? Why does it matter to distinguish them?

**15.3** State the rough relationship between time horizon and appropriate equity allocation. What happens if you ignore the relationship?

### Application

**15.4** Compute Sharpe, Treynor, and Jensen's alpha for a portfolio with 12% return, std dev 16%, and beta 1.1. Risk-free rate: 4.5%. Market return: 10%.

**15.5** A 40-year-old earning $80,000/year with $20,000 in cash savings, no debt, and the goal of retiring at 65: write a one-paragraph IPS for them. Specify allocation, rebalancing frequency, and account types (401k, IRA, taxable).

**15.6** Build a 10-stock diversified portfolio template (you don't need to pick specific stocks; just sectors and approximate weights). Then justify why your weights are reasonable for a 35-year-old saving for retirement.

### Synthesis

**15.7** A friend says: "I've been picking individual stocks for 20 years. My portfolio is up about 100%. Index funds returned 280% over the same period." Construct a diagnosis of what went wrong and a recommendation for how to fix it going forward.

**15.8** For the company you've analyzed in the project, evaluate it from a personal-investor perspective:
(a) What position size would be reasonable in a $1M diversified portfolio?
(b) Does the stock's beta increase or decrease the portfolio's overall systematic risk?
(c) Are there tax considerations (dividend yield, expected capital gains) that affect the answer?

### Challenge

**15.9** Compute the long-run wealth difference between two investors:
- Investor A: $5,000/year in an actively managed fund with 9% gross return and 1% expense ratio (8% net) for 40 years.
- Investor B: $5,000/year in an index fund with 8.5% gross return and 0.05% expense ratio (8.45% net) for 40 years.

What's the difference in terminal wealth? What does it tell you about the importance of fees?

**15.10** Pick a real active mutual fund (any fund family, any category). Find:
(a) Its 10-year return.
(b) Its 10-year benchmark return.
(c) Its expense ratio.
(d) The portfolio's beta relative to its benchmark.
(e) The fund's Jensen's alpha (calculate from the data).

Argue whether the fund has earned its fees.

---

## Chapter summary

- **Time horizon** is the most important driver of asset allocation. Longer horizons admit higher equity allocation.
- **Risk capacity** (financial ability) and **risk tolerance** (emotional capacity) are different. Match the lower of the two.
- **Diversification** is necessary but not sufficient. ~12-15 stocks across uncorrelated sectors captures most benefit.
- Diversification eliminates **firm-specific risk**, not **systematic risk**. In crises, correlations rise.
- **Sharpe, Treynor, Jensen's alpha** are the standard performance metrics. Sharpe for total-portfolio absolute risk-adjusted return; Treynor for systematic-risk-only; Alpha for the active manager's value-add over CAPM.
- The **empirical record favors passive (indexing)** for most investors. After-fee active outperformance is rare and unpredictable in advance.
- A written **investment policy statement** is the single most useful behavioral discipline.

---

## What would change my mind

The chapter argues that passive indexing is the right default for most individual investors. The reading would have to revise if (a) costs of active management fell dramatically (they have been falling, but not enough to overcome the underperformance gap), or (b) active management consistently outperformed in some identifiable category (small-cap and emerging markets show some evidence here, but the effect is modest and unstable). For US large-cap stocks specifically, the case for indexing is overwhelming.

## Still puzzling

The genuinely hard question this chapter sets up is *how to advise an individual investor who has done substantial fundamental work on a stock they believe is mispriced*. The textbook answer is "size the position appropriately within a diversified portfolio." The harder question is how to balance the analytical edge (which may be real) against the psychological cost of underperforming a simpler index strategy by years if you're wrong (or even if you're right but the market takes a long time to agree). I haven't found a clean rule. The honest framework is: do the work, size the position modestly relative to your conviction, accept that you may be wrong for years before being right or wrong forever. Active investing requires a temperament most investors don't have.

---

## Connections forward

- **Chapter 16** applies the same analytical machinery to *corporate* investment decisions (capital budgeting).
- **Chapter 17** computes WACC — the firm's discount rate.
- **Chapter 18** forecasts cash flows for valuation.
- **Chapter 20** revisits portfolio risk in the context of risk management.

---

---

## LLM Exercise — Chapter 15: The Investor's Perspective

**Project:** Equity Research Report on a Chosen Public Company
**What you're building this chapter:** A personal-investor perspective on whether to own this stock — separate from the analytical "is it undervalued" question. This becomes the executive-summary recommendation language.
**Tool:** Claude chat or Project.

### The Prompt

```
For [your company], take everything we've built so far (DCF from Chapter 11, beta from Chapter 14, ratios from Chapter 6, governance from Chapter 2) and answer the personal-investor question:

1. **Investment thesis in three sentences** — Why would (or wouldn't) you put your own money in this stock?

2. **Position sizing** — In a $100,000 diversified portfolio, what's the maximum reasonable position size for this stock? Justify based on: (a) the firm's beta and concentration risk, (b) sector exposure relative to the rest of the portfolio, (c) the strength of your conviction.

3. **Risk-adjusted comparison** — Compare your company's Sharpe ratio (from Chapter 13) to the S&P 500's. Has the firm produced superior risk-adjusted returns historically? Is that likely to persist?

4. **Time horizon match** — For what kind of investor (3-year horizon, 10-year horizon, retirement?) is this stock most appropriate? What kind would be wrong for it?

5. **The honest case against** — What's the strongest argument you can make *against* owning this stock? Construct it as a hostile bear thesis. Then assess how much credence to give it.

6. **Recommendation** — Buy, Hold, or Sell. With a price target range (use your DCF range from Chapter 11). State your conviction level.

Don't sugar-coat. The point is to produce a defensible call, not a sales pitch.
```

### What this produces

A 1-2 page investor-perspective section that becomes the report's executive summary and recommendation. The bear-thesis self-test is particularly valuable — most beginning analysts under-weight the case against their own conclusions.

### How to adapt this prompt

- *For your own company:* Replace [your company].
- *For ChatGPT / Gemini:* Identical.
- *For a Claude Project:* All prior outputs should already be in the project context.

### Connection to previous chapters

Synthesizes Chapters 1-14. Becomes the lens for the remaining chapters (capital allocation analysis in Ch 16-17, forecast scenarios in Ch 18, working capital in Ch 19, risk register in Ch 20).

### Preview of next chapter

Chapter 16 examines corporate capital budgeting from the firm's perspective. The Chapter 16 LLM Exercise will reverse-engineer how your company decides which projects to fund.

---

**Tags:** asset-allocation, diversification, IPS, Sharpe-ratio, active-vs-passive, indexing, risk-tolerance, time-horizon


---

## AI Wayback Machine

**Benjamin Graham** was wrote Security Analysis (1934) — the founding text of value investing.

**Run this:**

```
Who is Benjamin Graham, and how does their work connect to how to think about investing we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about their career or ideas.
```

→ Search **"Benjamin Graham"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to apply Benjamin Graham's framework to a specific finance question.
- Add a constraint: "Answer including criticisms or limits of Benjamin Graham's framework."

What changes? What gets better? What gets worse?
