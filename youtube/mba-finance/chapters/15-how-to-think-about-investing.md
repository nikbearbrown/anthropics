# Chapter 15 — How to Think about Investing
*Why the same $50,000 has completely different right answers depending on one question.*

---

You have $50,000. What should you do with it?

The question sounds like it has one answer. It has many, and they differ radically depending on one thing you haven't been asked yet: *when do you need it back?*

If you need the money in two years for a house down payment, the answer is mostly cash and short-term bonds. The 2008–2009 stock market crash would have cost a buyer with all-equity savings roughly half their down payment — a catastrophic outcome that a decade of strong subsequent returns could not undo for someone who had to buy a house in 2009.

If you don't need the money for thirty years, the answer is mostly equities. The same crash would have been a temporary drawdown on the way to substantial wealth accumulation by 2025.

Same $50,000. Same investor. Radically different right answers.

This chapter is about the framework that produces the right answer. It takes everything built in Chapters 1 through 14 — TVM, statistics, CAPM, market history — and applies it to the concrete question of what to do with money you actually have.

---

## The investor's framework

Before computing a single number, install the framework that orders the decisions. An investor is trying to do four things, which compete with each other: achieve specific goals at specific future times, match portfolio risk to actual tolerance, maximize after-tax and after-fee returns, and stay disciplined under stress. The first three are technical. The fourth is psychological and is where most empirical underperformance of individual investors comes from.

### Time horizon and asset allocation

The most important determinant of an appropriate investment strategy is **time horizon**. Different time horizons admit different levels of variance.

<!-- → [TABLE: time horizon vs. appropriate allocation — rows: <1 year, 1-3 years, 3-7 years, 7-15 years, 15-30+ years; columns: tolerable variance description, typical allocation (stocks/bonds/cash split), rationale — student should see the progression clearly] -->

The logic is asymmetric. Over short horizons, market downturns can permanently impair specific goals because you have to sell at the bottom. Over long horizons, downturns are recoverable, and the equity premium has time to compound. The same 50% drawdown that destroys a two-year horizon is a temporary noise event on a thirty-year timeline.

The classic shorthand is *age in bonds* — at 30, hold 30% in bonds; at 60, hold 60%. The rule is too crude for serious planning (it ignores wealth level, other income, specific goals, risk personality), but it captures the right qualitative shape: bond allocation rises with age as horizon shortens. Target-date funds implement a smoother version of this automatically, which is why they dominate 401(k) defaults.

### Risk capacity vs. risk tolerance

Two different things, often conflated.

**Risk capacity** is how much loss you can absorb without changing behavior or sacrificing goals. A retiree drawing on savings has low capacity; a 25-year-old with stable employment income has high capacity.

**Risk tolerance** is how much loss you can stomach emotionally. This is partly hardwired and partly experience-dependent. Investors who lived through 2008 often report lower tolerance even after their portfolios have fully recovered.

A well-designed portfolio matches the *lower* of the two. An investor with high capacity but low tolerance who builds a 100% equity portfolio will sell during the next drawdown and crystallize losses they didn't have to take. The rule is not "maximize expected return subject to your capacity constraint." It is "maximize expected return subject to the constraint you will actually honor when things get bad."

### The investment policy statement

The most useful tool in behavioral finance is probably also the simplest: write down your investment plan *before* making decisions. The **investment policy statement (IPS)** captures your goals (specific dollar amounts, specific dates), your risk limits (how much drawdown you'll tolerate without changing course), your target asset allocation, your rebalancing rules, and your selection approach. The IPS exists to be consulted when you feel the urge to do something different from the plan. Markets are volatile; human emotion is reactive; having a written plan gives you something to defer to that isn't "what I feel like doing right now."

For the equity research project, the individual stock pick fits inside an IPS — it does not replace it. A 30-year-old with $50,000 might have a defensible Buy thesis on a specific company. That company still shouldn't be 100% of the portfolio regardless of how compelling the thesis looks.

---

## Diversification: how many stocks, what kinds

Diversification is the simplest and most reliable risk-reduction tool available. It works because individual stocks carry **firm-specific risk** — risk that affects one company but not others — and that risk averages out as you add uncorrelated holdings.

The underlying math is the portfolio variance formula from Chapter 13. For two assets:

$$\sigma_p^2 = w_A^2 \sigma_A^2 + w_B^2 \sigma_B^2 + 2 w_A w_B \rho_{A,B} \sigma_A \sigma_B$$

When the correlation $\rho < 1$, portfolio variance is less than the weighted average of the individual variances. Adding more assets with correlations less than 1 keeps reducing portfolio variance — but with steeply diminishing returns.

Meir Statman's empirical result from 1987: going from 1 stock to 12 stocks dramatically reduces portfolio standard deviation; from 12 to 50 reduces it modestly; from 50 to 500 barely changes it at all. The diversification benefit is largely exhausted by roughly 15–20 holdings, provided those holdings are genuinely uncorrelated.

The empirical data on real stocks makes the correlation point vivid. Delta Airlines had a standard deviation of 51.9% over 2011–2020. Combining Delta with Southwest — correlation 0.87, same industry — reduced standard deviation to 49.1%. A small benefit. Combining Delta with Exxon — correlation 0.35, different industry — reduced standard deviation to 30.4%. A large benefit from the same number of holdings, because the industries respond differently to the same economic conditions.

**Correlation matters as much as count.** Twelve technology stocks is less diversified than four stocks spread across technology, finance, consumer staples, and industrials. The naive approach of counting holdings misses this entirely.

### Practical guidelines

A workable approach: use index funds where possible. A broad equity index gives you 500–3,500 holdings instantly at low cost. This is the cheapest and most reliable diversification available. If picking individual stocks, hold at least 10–15 with low cross-correlations across sectors. Limit any single position to roughly 5% of the portfolio. Limit any single sector to roughly 20%.

<!-- → [TABLE: sample 12-stock diversified equity portfolio — columns: sector, allocation %, representative names — showing sector balance roughly mirroring S&P 500 weights with small tilts — student should see what a real diversification structure looks like] -->

### What diversification cannot do

Diversification eliminates firm-specific risk. It does not eliminate **systematic (market) risk**. When the entire market falls 30% in a recession, every diversified portfolio falls roughly 30%. Diversification doesn't help.

In genuine crises, the benefit is further reduced because correlations rise. The 2008 episode showed international equities, REITs, commodities, and high-yield bonds all falling together with US stocks. Assets that had been historically uncorrelated became correlated precisely when diversification was most needed. Only Treasuries provided meaningful protection.

The 2022 episode showed a different failure mode: stocks and bonds both fell simultaneously because rising interest rates hurt both through different but related channels. The "60/40 portfolio" — the dominant diversification structure for retail investors — had its worst year since the 1930s in nominal terms.

The honest framing: diversification is necessary but not sufficient. It eliminates the kind of risk that comes from owning too few companies. It does not insure against the kind of risk that comes from being exposed to the economy at all.

---

## Performance evaluation and the active-passive question

Once you have a portfolio, three metrics quantify whether it's performing well.

**Sharpe ratio** — excess return per unit of total risk:

$$\text{Sharpe} = \frac{\bar{R}_p - R_f}{\sigma_p}$$

This is the right metric for evaluating a portfolio in isolation, on an absolute basis. The S&P 500's long-run Sharpe has been roughly 0.4. Active managers who consistently produce Sharpe ratios above 0.6 over long periods are exceptional.

**Treynor ratio** — excess return per unit of systematic risk only:

$$\text{Treynor} = \frac{\bar{R}_p - R_f}{\beta_p}$$

This is the right metric when the portfolio being evaluated is one piece of a larger diversified portfolio, where the only risk that matters is systematic exposure. A concentrated bet in a single stock contributes systematic risk to the broader portfolio; idiosyncratic risk diversifies away. Treynor captures just the systematic piece.

**Jensen's alpha** — the return above and beyond what CAPM predicts:

$$\alpha = \bar{R}_p - [R_f + \beta_p (\bar{R}_m - R_f)]$$

A positive alpha means the portfolio has delivered returns above what its market exposure alone would predict. This is what active managers are paid to produce. The empirical record on whether they do so is the crux of the active-passive debate.

### A worked comparison

Two managers over 10 years, with risk-free rate 2% and market return 11%:

<!-- → [TABLE: Wong vs. Petrov performance comparison — rows: return, std dev, beta, Sharpe, Treynor, CAPM expected, Jensen's alpha — student should see that higher absolute return does not mean better risk-adjusted performance] -->

Manager Wong: 14% return, standard deviation 8%, beta 1.2. Sharpe: $(14-2)/8 = 1.50$. Treynor: $(14-2)/1.2 = 10.0$. CAPM expected return: $2 + 1.2 \times 9 = 12.8\%$. Alpha: $+1.2\%$.

Manager Petrov: 16% return, standard deviation 10%, beta 1.6. Sharpe: $(16-2)/10 = 1.40$. Treynor: $(16-2)/1.6 = 8.75$. CAPM expected return: $2 + 1.6 \times 9 = 16.4\%$. Alpha: $-0.4\%$.

Petrov had higher absolute returns. Wong had better risk-adjusted performance on every metric — higher Sharpe, higher Treynor, positive alpha versus negative alpha. Petrov earned less than CAPM would predict given the risk taken. Wong earned more. The higher return is not the better performance.

### The active vs. passive question

The empirical case for passive indexing:

The SPIVA reports (S&P Indices vs. Active) show that 80–90% of active US large-cap mutual fund managers underperform their benchmark over 15–20 year periods after fees. This is not a close call or a borderline finding — it is one of the most replicated results in empirical finance. The few managers who outperform in any given period show limited persistence; past outperformance is a poor predictor of future outperformance. And the costs compound brutally: a 1% annual expense ratio over 40 years consumes roughly 25% of the wealth you would otherwise have accumulated in a low-cost index fund.

The case for active management:

Some markets are less efficient — small-cap, emerging market, and certain fixed-income segments show higher fractions of active managers who outperform. The best managers do exist; decades of consistent alpha from a small number of investors (Buffett is the canonical case, the Medallion Fund another) proves the concept. And passive investing involves a kind of deliberate complacency: you accept whatever the market prices, regardless of whether those prices are correct.

For most retail investors with horizons of 30 years or more, the empirical case strongly favors indexing. The cost savings are large, the behavioral discipline is simpler, and the underperformance of active managers is too consistent to dismiss. For an investor with genuine analytical skill and the discipline to apply it without behavioral error — rare but real — active strategies can be appropriate. The honest test is not "do I believe I'm above average?" (most people do) but "do I have a specific, defensible reason to think I can beat the market after costs?"

---

## The synthesis

Three concepts, one playbook.

Match portfolio risk to time horizon and tolerance. Long horizons can absorb equity variance; short horizons cannot. Write an IPS. Stick to it under stress — the whole point of writing it is to be able to stick to it under stress.

Diversify within asset classes. Index funds are the cheapest and most reliable diversification. If picking individual stocks, hold at least 10–15 across uncorrelated sectors. Correlation of holdings matters as much as count.

Default to passive unless you have a defensible reason for active. The empirical record favors indexing for most investors in most markets. The cost savings are real and compound. Active outperformance after fees is rare and hard to identify in advance.

The work in Chapters 1–14 made each of these statements concrete. TVM gives you the arithmetic for converting goals into future dollar targets. Statistics gives you the tools to measure risk. CAPM gives you the benchmark for evaluating whether you're earning what your risk justifies. Market history gives you the empirical base rates for setting realistic expectations. This chapter assembles them into a usable framework.

For the equity research project, this is the lens through which the final recommendation should be interpreted. A "Buy" rating does not mean "put all your savings in this stock." It means "this stock appears undervalued relative to intrinsic value; the appropriate amount to allocate in a diversified portfolio depends on your other holdings, your time horizon, and the strength and fragility of your analytical case."

Chapter 16 applies the same analytical machinery to a different question: not *should I own this stock* but *should the firm itself undertake this project*. The DCF math is identical; the decision-maker is the corporation rather than the individual.

---

## What would change my mind

The chapter argues that passive indexing is the right default for most individual investors. I would revise if (a) the cost of active management fell far enough to offset the performance gap — costs have been falling, but not fast enough to close the gap yet — or (b) active management consistently outperformed in clearly identifiable market segments over long periods. The small-cap and emerging-markets evidence is the most credible push against the full passive case, but the effect is modest and unstable across periods. For US large-cap equities specifically, the case for indexing is overwhelming.

## Still puzzling

The genuinely hard question this chapter frames but doesn't resolve: how should an investor behave when they've done substantial fundamental work on a specific stock and believe it's genuinely mispriced? The textbook answer is "size the position appropriately within a diversified portfolio." The harder reality is that even being right can be unprofitable for years if the market is slow to agree, and being wrong looks identical to being early for a long time. Active investing ultimately requires a temperament — the ability to hold a position under stress while the market disagrees with you — that most investors genuinely do not have, and no amount of analytical skill compensates for its absence.

---

## Connections forward

- **Chapter 16** applies the same NPV machinery to corporate capital budgeting — the firm deciding which projects to fund.
- **Chapter 17** computes WACC — the firm's discount rate for those decisions.
- **Chapter 18** forecasts cash flows for firm-level valuation.
- **Chapter 20** revisits portfolio risk in the context of firm-level risk management.

---

## Exercises

### Warm-up

**15.1** A stock you bought for $100 paid $3 in dividends during the year and is now worth $120. Compute: (a) dividend yield; (b) capital gain yield; (c) total holding-period return. *(Tests: return decomposition mechanics. Difficulty: low.)*

**15.2** Define risk capacity and risk tolerance. Give one example of an investor who has high capacity but low tolerance, and explain what the right portfolio design implication is. *(Tests: the capacity/tolerance distinction and its practical consequence. Difficulty: low.)*

**15.3** Two portfolios both returned 12% last year. Portfolio A had a standard deviation of 18% and a beta of 1.4. Portfolio B had a standard deviation of 10% and a beta of 0.8. Risk-free rate: 3%. Market return: 10%. Compute Sharpe, Treynor, and Jensen's alpha for each. Which performed better on a risk-adjusted basis? *(Tests: Sharpe/Treynor/alpha computation. Difficulty: low-medium.)*

### Application

**15.4** A 29-year-old earns $75,000 per year, has $15,000 in savings, no debt, and wants to retire at 65 with $2 million in today's dollars. Write a one-paragraph investment policy statement specifying: (a) target asset allocation; (b) rebalancing frequency and trigger; (c) account types (401(k), IRA, taxable); (d) selection approach (index vs. active). Justify each choice. *(Tests: IPS construction applied to a realistic investor. Difficulty: medium.)*

**15.5** You are building a 12-stock diversified equity portfolio. The following pairs of stocks are available. For each pair, explain which combination produces more diversification benefit and why: (a) Two airlines vs. one airline and one pharmaceutical; (b) Two large-cap US technology stocks vs. one large-cap US technology stock and one international consumer-staples stock; (c) A gold miner and a retailer vs. two retailers. *(Tests: correlation-based diversification reasoning without requiring calculation. Difficulty: medium.)*

**15.6** An investor holds a $200,000 portfolio. Her IPS limits any single position to 5% and any single sector to 20%. She wants to add the stock you've analyzed for the equity research project. (a) What is the maximum dollar position she can take? (b) If the stock has a beta of 1.4 and her current portfolio has a beta of 0.9, what happens to the portfolio's beta if she adds the maximum position? (c) Is that an acceptable outcome given a moderate risk-tolerance IPS? *(Tests: position sizing + beta impact calculation. Difficulty: medium.)*

### Synthesis

**15.7** The chapter states that 80–90% of active US large-cap mutual fund managers underperform their benchmark after fees over 15–20 years. A friend says: "That means 10–20% do outperform — I'll just find those." Construct the full case against this strategy, addressing: (a) persistence of outperformance; (b) identification problem (how do you find them in advance?); (c) fee drag on the search itself; (d) why the surviving outperformers may not persist. *(Tests: active vs. passive reasoning and survivorship bias. Difficulty: high.)*

**15.8** Using the forward-looking assumptions from Chapter 12 (current 10-year Treasury yield as the risk-free rate, ERP of 5%), compute the expected return on a portfolio with beta 1.2. Compare this to the Sharpe ratio of the same portfolio if it actually earns 13% with standard deviation 14%. Is the portfolio adding value above what its beta exposure justifies? *(Tests: integration of CAPM with Sharpe and alpha. Difficulty: high.)*

### Challenge

**15.9** Compute the long-run wealth difference between two investors, each investing $5,000 per year for 40 years: Investor A uses an actively managed fund with 9% gross return and a 1% expense ratio (8% net). Investor B uses an index fund with 8.5% gross return and a 0.05% expense ratio (8.45% net). (a) Compute terminal wealth for each using the annuity future-value formula from Chapter 8. (b) What is the dollar difference? (c) Express the fee drag as a percentage of Investor B's terminal wealth. What does the result say about the minimum alpha an active manager must generate to justify a 1% expense ratio? *(Tests: TVM + fee compounding + active management break-even. Difficulty: high.)*

**15.10** Find a real active mutual fund. Collect: its 10-year annualized return, its benchmark's 10-year annualized return, its expense ratio, and its beta relative to the benchmark. Compute Jensen's alpha net of fees. Then answer: has this fund generated enough alpha to justify its cost? If you had to advise the fund's current investors, what would you tell them? *(Tests: applying performance metrics to a real fund and forming a defensible judgment. Difficulty: high.)*

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

A 1–2 page investor-perspective section that becomes the report's executive summary and recommendation. The bear-thesis self-test is particularly valuable — most beginning analysts under-weight the case against their own conclusions.

### How to adapt this prompt

- *For your own company:* Replace [your company].
- *For ChatGPT / Gemini:* Identical.
- *For a Claude Project:* All prior outputs should already be in the project context.

### Connection to previous chapters

Synthesizes Chapters 1–14. Becomes the lens for the remaining chapters (capital allocation analysis in Ch 16–17, forecast scenarios in Ch 18, working capital in Ch 19, risk register in Ch 20).

### Preview of next chapter

Chapter 16 examines corporate capital budgeting from the firm's perspective. The Chapter 16 LLM Exercise will reverse-engineer how your company decides which projects to fund.

---

**Tags:** asset-allocation, diversification, IPS, Sharpe-ratio, active-vs-passive, indexing, risk-tolerance, time-horizon

---

## AI Wayback Machine

**Benjamin Graham** wrote *Security Analysis* (1934) — the founding text of value investing.

![Benjamin Graham](../images/benjamin-graham-5iz.png)

*Puppet Art by [Nik Bear Brown](https://www.nikbearbrown.com/).*

**Run this:**

```
Who is Benjamin Graham, and how does their work connect to how to think about investing we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about their career or ideas.
```

→ Search **"Benjamin Graham"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to apply Benjamin Graham's framework to a specific finance question.
- Add a constraint: "Answer including criticisms or limits of Benjamin Graham's framework."

What changes? What gets better? What gets worse?
