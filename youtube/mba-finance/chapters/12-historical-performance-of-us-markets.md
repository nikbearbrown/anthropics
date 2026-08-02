# Chapter 12 — Historical Performance of US Markets
*What a century of data actually tells us — and what it doesn't.*

---

In January 1980, you put $10,000 into an S&P 500 index fund. You held it through the 1987 crash, the dot-com bust, the 2008 financial crisis, the COVID collapse, and the 2022 bear market. By mid-2020, through all of it, your $10,000 was worth approximately $697,000.[^1]

[^1]: Compounded at roughly 11.2% nominal over 40 years. Specific endpoint values vary by exact start/end dates; figures from data through mid-2020 cited in OpenStax.

Now suppose you panicked during the bad stretches and missed only the *ten best trading days* of those forty years. Your $10,000 grows to about $313,000 instead — less than half. Miss the five best days alone and you've lost over a quarter million dollars.

This is the central pattern in US market history. Stocks, over long periods, deliver compounding returns that are dramatic in their cumulative effect. Trying to time entry and exit around the bad days usually destroys more value than it creates — because the best days and the worst days cluster in the same volatile periods. An investor who flees the volatility misses the recovery.

The pattern has held, with episodes of severe interruption, for at least a century. This chapter is about what that history actually says: the numbers, the crashes, and the honest limits of what any of it implies for what comes next.

---

## The long-run record

Several decades of careful data collection — Ibbotson, Damodaran, Dimson-Marsh-Staunton — give us a reasonably reliable picture of asset-class returns over long periods. The numbers for 1981–2020:

<!-- → [TABLE: asset class returns table — columns: asset class, nominal return, real return, standard deviation — rows: large-cap stocks, small-cap stocks, investment-grade corporate bonds, 10-year Treasuries, T-bills, inflation — student should see the full hierarchy from stocks down to cash] -->

Large-cap stocks (S&P 500): roughly 12.6% nominal, 9.7% real, standard deviation 16.1%. Investment-grade corporate bonds: 10.3% nominal, 7.4% real, standard deviation 7.7%. Ten-year Treasuries: 8.2% nominal, standard deviation 9.9%. T-bills: 3.9% nominal, roughly 1% real, standard deviation 3.4%. Inflation over the same period: 2.9%.

The longer-horizon record (1928 through 2020) shows similar patterns but with slightly lower fixed-income returns — partly because 1981–2020 included the great bond bull market that began as inflation peaked. A specific comparison: $100 invested in long-term US Treasuries in 1928 and held through 2020 grew to about $8,000. The same $100 in large-cap stocks grew to over $400,000 — fifty times the bond return.[^2]

[^2]: Damodaran data series, NYU Stern. `[verify]` for current vintage and exact endpoints.

The pattern is consistent across almost every sub-period of US market history: stocks outperform bonds, bonds outperform cash, and the differences compound dramatically over long horizons.

---

## The equity risk premium

The gap between stock returns and Treasury returns is the **equity risk premium (ERP)**. Over the 1981–2020 sample:

$$\text{ERP} \approx 12.6\% - 3.9\% = 8.7\%$$

Over longer historical samples (1928 onward), the ERP has been more like 5–7 percentage points depending on which Treasury benchmark you use and the precise window. As of the post-2008 era, equity analysts typically use an *expected* ERP of 4–6% — lower than the realized historical average. The reasoning matters: the realized premium was partly elevated by one-time events that cannot repeat. Treasury yields fell from 14% in 1981 to 1.5% in 2020. That 12-point decline lifted bond prices, reduced corporate borrowing costs, raised price-to-earnings ratios, and pushed equity returns above what underlying earnings growth alone would have produced. The next forty years cannot deliver the same tailwind because yields cannot fall by another 12 points from where they are now.

The ERP is the most consequential single number in equity valuation after the risk-free rate. It feeds into the cost of equity (Chapter 14), which feeds into WACC (Chapter 17), which is the discount rate in every DCF model. Change the ERP by 2 percentage points and the DCF valuation swings by 30% or more. This is not a small decision.

There is also a subtler problem with the historical ERP: survivorship bias. The US has the highest realized equity premium in the developed world. Some of this reflects genuine economic strength. But markets that were destroyed — Russian equities in 1917, Chinese equities in 1949, several European exchanges in World War II — don't appear in the historical-returns dataset. The record we have is the record of markets that survived. If you had randomly selected a developed country's stock market in 1900 to invest in for a century, you would not have had 50% odds of choosing the United States. The realized US premium is the view from the winner's podium, and extrapolating from it without adjustment is optimistic.

<!-- → [CHART: equity risk premium over rolling 20-year windows, 1930–present — student should see how variable the premium is and that it has been both much higher and much lower than the long-run average in specific periods] -->

---

## Five crashes worth knowing

The smooth long-run averages hide brutal short-run episodes. Five drawdowns deserve specific attention — not as cautionary tales but as data about what equity investing actually involves.

**1929–1932.** The S&P composite peaked in September 1929 and fell roughly 86% over the next three years. Adjusted for deflation, the real loss was still well over 70%. The market did not regain its 1929 nominal peak until 1954 — twenty-five years later. This is the standard corrective to "stocks always recover quickly" intuitions. The recovery was real. The time scale was generational.

**1973–1974.** The S&P 500 fell about 48% during the recession that accompanied the OPEC oil shock and the Bretton Woods collapse. Inflation was high; real losses were severe. The market took roughly a decade to fully recover in real terms.

**2000–2002.** The S&P 500 fell about 49% from peak to trough. The NASDAQ fell about 78% — and many of its dominant 1999-vintage companies never recovered at all. Recovery to the prior peak took five years for the S&P, much longer for the NASDAQ.

**2008–2009.** The S&P 500 fell 57% from October 2007 to March 2009 — the most severe US drawdown since the Great Depression. It reclaimed its prior peak in March 2013, about 5.5 years from peak. Some sectors — financials, real estate — took much longer; many individual firms never recovered.

**2020.** The S&P 500 fell 34% in 33 days, the fastest bear market in US history. It reclaimed its prior peak in five months. The brevity of both the decline and the recovery was unusual; aggressive monetary and fiscal policy responses compressed what might otherwise have been a longer episode.

<!-- → [CHART: S&P 500 drawdown chart — showing each major drawdown as a shaded region with depth labeled — student should see the pattern and the severity clearly, with recovery timeline visible] -->

What these five events share: each was preceded by strong returns and rising valuations. Each was accompanied by a macro shock. Each was recovered through the next expansion.

What they did *not* share: timing predictability. With hindsight, every drawdown had warning signs. Without hindsight, none was widely anticipated. In every case, significant parts of the financial commentariat confidently denied the downturn right up to the moment it began. The 2007 Bernanke testimony before Congress in which subprime mortgage stress was assessed as "contained" happened in March 2007. The Lehman Brothers CEO reaffirmed the firm's financial strength in a September 10, 2008 analyst call. Lehman filed for bankruptcy three days later.

This is the core difficulty with active market timing: the events that cause the crashes are, almost by definition, the events that markets have not yet priced. If they were priceable in advance, they would already be priced, and the crash would have already happened.

---

## What the history implies — and what it doesn't

Three observations from the long-run record matter for any serious approach to investing or equity research.

**The equity premium is real but variable.** The US data over a century is clear: equities have outperformed bonds and cash by a substantial margin over essentially every long horizon. For a patient investor with a horizon of decades, equity allocation is the appropriate default. But "substantial margin" is not a fixed number. The realized premium is variable across sub-periods, and it is substantially higher in the US than in most other developed markets. Japan's equity market in 1990 was the largest in the world by some measures; it has spent the subsequent thirty-plus years below that peak. The US premium is not a law of nature. It is the historical experience of one country over one century, with a significant tailwind from a unique geopolitical moment.

**Market timing is harder than it looks.** The "missing the best days" data quantifies the problem precisely: in virtually every long sample, the best ten trading days produce so much of the total return that missing them — even if you also miss the worst days — leaves you substantially worse off than buy-and-hold. The mechanism is that best days and worst days cluster in the same volatile periods. An investor who exits during the volatility to avoid the worst days typically misses the best days too. The 2020 case is the sharpest recent example: 34% decline in 33 days, then 75% rally over 18 months. Investors who sold in the panic locked in the loss and often missed the recovery.

This does not mean every investor should hold every position through every drawdown. Individual stocks can permanently lose value; Lehman Brothers shareholders didn't get their money back. The buy-and-hold lesson is about diversified exposure to *the market*, not about any individual company. And for time horizons shorter than a decade or for investors who will need the capital within a few years, the volatility tolerance required for 100% equity exposure is genuinely unreasonable.

**Realized returns are not expected returns.** Every number in this chapter is *realized* return — what actually happened. Expected returns — what investors anticipated — are a different quantity. The two can diverge for long periods, and the historical record cannot tell you what forward returns will be. The 12.6% nominal return on US stocks since 1981 was partly driven by a 12-point decline in Treasury yields that raised all asset prices. A simple projection of that number forward assumes the same tailwind continues, which requires Treasury yields to fall from 4% to negative 8% over the next forty years. That is not a plausible scenario.

The appropriate forward-looking inputs for a DCF model: the current risk-free rate (the 10-year Treasury yield, whatever it is at the time of analysis), an equity risk premium of 4–6% (the current academic and practitioner consensus, informed by but lower than the historical realized average), and a long-term growth rate for terminal value of 2–3% (roughly long-run real GDP growth plus inflation).

<!-- → [TABLE: forward-looking vs. realized returns comparison — columns: parameter, realized historical average, forward-looking estimate, rationale for difference — rows: risk-free rate, equity risk premium, expected stock return, long-term growth rate] -->

---

## The synthesis

After a century of careful data, five claims are well-supported by the evidence:

Equities have outperformed bonds and cash by a substantial margin over long periods in the US. The premium is real and large.

The equity premium is variable — across countries, across time periods, and across the starting conditions of any investment. Forward expectations should be lower than realized historical averages.

Drawdowns are recurring and severe. An investor who cannot tolerate 30–50% interim losses should not hold a 100% equity portfolio, regardless of long-run averages.

Market timing is hard. Missing a small number of best trading days substantially reduces long-run returns. Most active timing strategies underperform buy-and-hold after costs.

Diversification works in normal markets but partially fails in crises. Correlations rise during stress; tail risks become systemic. The 2022 experience — stocks down 25%, bonds down 13% simultaneously — showed that the usual stock-bond diversification benefit can disappear in high-inflation, rising-rate environments.

These five claims are the empirical backbone of every defensible long-term investing argument. They are also the context the next several chapters build quantitative tools to engage with: Chapter 13 installs the statistical machinery for measuring risk, Chapter 14 computes beta, Chapter 15 applies these results to portfolio construction, and Chapter 17 uses the equity premium to compute the cost of equity.

For the equity research project specifically, this chapter establishes the empirical context for the investment thesis. When your DCF says your chosen company is worth $X and the market says it's worth 85% of $X, your case for the gap rests on firm-level analysis — but the broader claim that equity research can identify mispricings rests on the long-run record that markets are sometimes wrong. That record is real. It is also humbling: the same data that shows markets are occasionally mispriced shows that correctly identifying and timing those mispricings is one of the harder problems in finance.

---

## What would change my mind

The chapter argues that long-run US equity returns provide a useful but imperfect guide to forward expectations, and that the realized equity premium is real but smaller going forward than realized historical averages suggest. I would revise if (a) a sustained period of US equity returns substantially below historical averages emerged and persisted — the 2010s and 2020s may already be showing this in valuations-adjusted returns — or (b) forward-looking implied-cost-of-capital methods turned out to be substantially more accurate than backward-looking averages. These methods are the leading academic alternative and probably are better than naive averages; they are not yet precise enough to replace the historical record as a benchmark.

## Still puzzling

Whether the next forty years will resemble the last forty. The 1981–2020 period had an enormous tailwind from declining interest rates that lifted every asset class. That tailwind cannot repeat. Forward-looking returns are probably meaningfully lower than realized historical averages — but by how much? Reasonable estimates range from one percentage point lower to substantially lower. This uncertainty propagates directly into every DCF-based valuation. The honest analyst includes it as a sensitivity case rather than assuming the historical record extends mechanically into the future.

---

## Connections forward

- **Chapter 13** installs the statistical machinery for measuring risk: mean, standard deviation, covariance, Sharpe ratio.
- **Chapter 14** computes beta — the regression of a stock's returns on the market — and uses it to estimate the cost of equity via CAPM.
- **Chapter 15** applies the historical return and risk data to portfolio construction and personal investing.
- **Chapter 17** uses the equity premium and risk-free rate to compute the cost of equity and WACC.

---

## Exercises

### Warm-up

**12.1** State approximate long-run nominal annual returns for large-cap US stocks, 10-year Treasuries, and T-bills (1981–2020 averages). Compute the equity risk premium from these numbers. *(Tests: recall of the return hierarchy and ERP definition. Difficulty: low.)*

**12.2** What is a drawdown? State the approximate peak-to-trough magnitude and recovery time for the 2008–2009 financial crisis and the 2020 COVID crash. What was unusual about the 2020 recovery compared to earlier drawdowns? *(Tests: drawdown mechanics and episode knowledge. Difficulty: low.)*

**12.3** Why should forward-looking equity return assumptions be lower than the 1981–2020 realized average? Name the specific one-time tailwind that inflated the historical number. *(Tests: realized vs. expected returns and the interest-rate tailwind argument. Difficulty: low.)*

### Application

**12.4** Pull S&P 500 total return data (`^SP500TR` on Yahoo Finance) and 10-year Treasury return data for the past 20 years. Compute: (a) annualized equity return; (b) annualized bond return; (c) realized equity risk premium; (d) real equity return using CPI from FRED. Compare to the 1981–2020 averages in this chapter — is the premium higher, lower, or similar over your window? *(Tests: FRED/Yahoo fluency and ERP computation on real data. Difficulty: medium.)*

**12.5** For your chosen company, find its stock price history from October 2007 through March 2009. (a) Compute the maximum drawdown. (b) Compute the recovery time to the prior peak. (c) Compare both to the S&P 500's 57% drawdown and 5.5-year recovery. What does the comparison suggest about the firm's systematic risk? *(Tests: applying drawdown concept to a specific firm. Difficulty: medium.)*

**12.6** The chapter states that missing the ten best trading days over forty years cuts returns from roughly $697,000 to $313,000 on a $10,000 investment. (a) Verify this is consistent with the compounding math: approximately what annual return corresponds to $697,000, and what annual return corresponds to $313,000? (b) What does the gap between the two numbers imply about the concentration of returns in a small number of days? *(Tests: compound growth mechanics and the timing-the-market point. Difficulty: medium.)*

### Synthesis

**12.7** A colleague argues: "The equity risk premium is just survivorship bias. The US happened to win the 20th century. We should use a much lower forward ERP — maybe 2%." Construct (a) the strongest version of this argument, including at least one specific destroyed market as evidence, and (b) the strongest counter-argument for why the US premium reflects genuine structural advantages. What evidence would help you decide how much weight to give each side? *(Tests: survivorship bias argument and its limits. Difficulty: high.)*

**12.8** In 2022, both US stocks (−25%) and US bonds (−13%) fell simultaneously — a correlation that broke the usual stock-bond diversification logic. (a) Identify the macro mechanism that caused this. (b) In which of the five historical crash episodes covered in this chapter was a similar correlation failure present? (c) What does this imply for the "60/40 portfolio is safe" assumption? *(Tests: crisis correlation + macro mechanism identification. Difficulty: high.)*

### Challenge

**12.9** Using the forward-looking inputs suggested in the chapter (current 10-year Treasury yield, ERP of 4–6%, long-term growth rate of 2–3%), build two DCF scenarios for your chosen company: one using the bottom of the ERP range (4%) and one using the top (6%). By what percentage does your estimated intrinsic value change between the two scenarios? What does this tell you about how much of your investment thesis depends on the ERP assumption versus firm-specific analysis? *(Tests: ERP sensitivity in a real DCF. Difficulty: high.)*

**12.10** The chapter claims that market timing is hard because best and worst days cluster together. Design a simple test of this claim using historical data: (a) identify the 10 best and 10 worst single-day S&P 500 returns in any 10-year window you choose; (b) compute the average number of calendar days between consecutive best/worst days; (c) compare this to what you would expect if best and worst days were randomly distributed throughout the year. Does the data support the clustering claim? *(Tests: empirical reasoning about market timing and return clustering. Difficulty: high.)*

---

## LLM Exercise — Chapter 12: Realized Returns vs. the Market

**Project:** Equity Research Report on a Chosen Public Company
**What you're building this chapter:** Compute your company's realized returns over multiple horizons and compare to the S&P 500. Input data for the beta regression in Chapter 14.
**Tool:** Yahoo Finance for data, Excel/Python for computation, Claude chat for interpretation.

### Setup

Pull from Yahoo Finance (https://finance.yahoo.com):
- Your company's monthly closing prices for the past 10 years
- S&P 500 (^GSPC) monthly closing prices for the past 10 years

Save as a spreadsheet with date, your-company-price, S&P-price columns.

### The Prompt

```
For [your company], using the monthly price data I have:

1. **Compute monthly total returns** (price change + dividends, divided by prior price). Excel: =(P_t - P_{t-1} + D_t) / P_{t-1}. If dividends aren't easily available, use Yahoo's "adjusted close" series, which already incorporates dividends.

2. **Compute annualized returns** for the most recent 1-year, 3-year, 5-year, and 10-year periods. Use geometric mean for compound annual growth rate.

3. **Compute the same for the S&P 500** over the same periods.

4. **Compute excess returns** — your company minus S&P 500 — for each period.

5. **Compute drawdowns** — for both your company and S&P 500, identify the deepest peak-to-trough drawdown in the past 10 years. Note the dates.

6. **Plot the cumulative return chart** of $1 invested in your company vs. $1 invested in S&P 500 over the past 10 years.

Then write a brief interpretation:
- Has your company outperformed the market over each of the four time horizons?
- Did the firm survive the 2020 COVID drawdown better, worse, or about the same as the market?
- What does the comparison suggest about the firm's beta (which we'll formally regress in Chapter 14)?

Cite Yahoo Finance as the data source.
```

### What this produces

A return-comparison table and chart. Adds to the report's market-context section. Provides the data for Chapter 13's risk metrics and Chapter 14's beta regression.

### How to adapt this prompt

- *For your own company:* Replace [your company].
- *For ChatGPT / Gemini:* Identical.
- *For Claude Code:* Recommended for the data manipulation. Yahoo Finance has a Python library (`yfinance`) that pulls returns directly, much faster than manual download.

### Connection to previous chapters

Builds on Chapter 6's market-value ratios. Sets up Chapters 13 and 14.

### Preview of next chapter

Chapter 13 introduces statistical analysis. The Chapter 13 LLM Exercise will compute risk metrics (mean, std dev, Sharpe) on your return series.

---

**Tags:** historical-returns, equity-risk-premium, market-history, drawdowns, equity-premium, asset-class-returns

---

## AI Wayback Machine

**Roger Ibbotson** compiled the historical US stock-and-bond returns dataset that anchors modern asset-allocation studies.

**Run this:**

```
Who is Roger Ibbotson, and how does their work connect to US market history we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about their career or ideas.
```

→ Search **"Roger Ibbotson"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to apply Roger Ibbotson's framework to a specific finance question.
- Add a constraint: "Answer including criticisms or limits of Roger Ibbotson's framework."

What changes? What gets better? What gets worse?
