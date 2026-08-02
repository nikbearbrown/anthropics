# Chapter 12 — Historical Performance of US Markets

**Suggested titles**
1. The Numbers Behind the Theory
2. What a Century of Markets Teaches
3. The Equity Premium and Its Discontents

**TL;DR.** Over the past century, US stocks have returned roughly 10% per year (about 7% real), bonds 5–6%, and T-bills 3-4%. The gap between stocks and safer assets — the **equity risk premium** — is the empirical observation that compensates equity investors for accepting variable cash flows. The history is large enough to take seriously and short enough to leave room for honest doubt about whether it repeats.

---

## The puzzle of $10,000

In January 1980, you put $10,000 into an S&P 500 index fund (you'd have to wait two years for Vanguard to launch its low-cost retail version, but assume you got there). You held it through the 1980s expansion, the 1987 crash, the 1990s tech boom, the dot-com bust, the 2003-07 expansion, the 2008 financial crisis, the 2009-2020 expansion, the COVID crash and recovery, and the 2022 bear market. By mid-2020 — through good years and bad, through the painful drawdowns — your $10,000 was worth approximately $697,000.[^1]

If you had panicked and sold during the worst stretches, missing only the *ten best trading days* of those forty years, your $10,000 would have grown to about $313,000 instead — less than half. Missing the five best days alone would have cost you over a quarter million dollars.

[^1]: Compounded at roughly 11.2% nominal over 40 years. Specific endpoint values vary by exact start/end dates; figures from data through mid-2020 cited in OpenStax. `[verify]` for current data.

This is the central pattern in US market history. Stocks, on average, over long periods, deliver returns that compound dramatically. Trying to time entry and exit usually destroys more value than it creates. The pattern has held, with episodes of severe interruption, for at least a century.

For the equity research project, this chapter does two things. First, it gives you the historical data — long-run returns by asset class, the risk-return trade-off in observed numbers, the equity risk premium. Second, it forces honest engagement with what the history *means*: how much should we expect the past to repeat, and what does that imply for forward-looking valuation?

---

## Learning objectives

After working through this chapter, you should be able to:

- State approximate long-run nominal and real returns for US stocks, bonds, and T-bills.
- Compute the equity risk premium and explain what it compensates investors for.
- Identify the major US market downturns (1929-32, 1973-74, 2000-02, 2008-09, 2020) and their approximate magnitudes.
- Distinguish between **realized returns** (what actually happened) and **expected returns** (what investors anticipated).
- Explain why timing the market is difficult and usually counterproductive.
- Compare US equity performance to other developed markets (Australia, UK, Japan).

**Prerequisites.** Chapters 7-9 (TVM), Chapter 10 (bonds), Chapter 11 (stocks).

---

## Concept 1 — The long-run record

Several decades of careful data collection (Ibbotson, Damodaran, Dimson-Marsh-Staunton) give us a reasonably reliable picture of asset-class returns over long periods.

### Returns by asset class (1981–2020 averages)

| Asset class | Nominal return | Real return | Standard deviation |
|---|---|---|---|
| Large-cap stocks (S&P 500) | 12.6% | ~9.7% | 16.1% |
| Small-cap stocks | 12.1% | ~9.2% | higher |
| Investment-grade corporate bonds (Baa) | 10.3% | ~7.4% | 7.7% |
| 10-year Treasury bonds | 8.2% | ~5.3% | 9.9% |
| T-bills | 3.9% | ~1.0% | 3.4% |
| Inflation (CPI) | 2.9% | — | 1.8% |

The longer-horizon record (1928 to 2020 inclusive) shows similar patterns but with slightly lower nominal returns for fixed income — partly because the 1981–2020 period included the great bond bull market that began as inflation peaked.

A specific comparison from the historical record: $100 invested in long-term US Treasury bonds in 1928 and held through 2020 grew to about $8,000. The same $100 in large-cap stocks grew to over $400,000 — *fifty times* the bond return.[^2]

[^2]: Damodaran data series for historical asset class returns, NYU Stern. `[verify]` for current vintage and exact endpoints.

### The equity risk premium

The gap between stock returns and Treasury returns is the **equity risk premium (ERP)**. Over the 1981-2020 sample:

$$\text{ERP} \approx 12.6\% - 3.9\% = 8.7\%$$

Over longer historical samples (1928 onward), the ERP has been more like 5-7 percentage points, depending on which Treasury benchmark you use and the precise window. As of the post-2008 era, equity research analysts typically use an *expected* ERP of 4-6%, lower than the long-run realized average. The reasoning: the realized premium was unusually high in part because of one-time events (the post-WWII US economy, the 1980-2020 disinflation), and forward-looking expectations should be more modest.

The ERP is the single most important number in equity research after the discount rate. It feeds into the cost of equity (Chapter 14), which feeds into WACC (Chapter 17), which is the discount rate in DCF (Chapter 11). Get the ERP wrong by 2 percentage points and you can swing your DCF valuation by 30%.

### Bonds vs. cash

Bonds have outperformed cash (T-bills) by 3-5 percentage points on average over long horizons — the **term premium** for bearing duration risk. But bond returns are not stable: in some years they are sharply negative (2022 saw a -13% return on the bond aggregate, the worst calendar year in modern history), and in some years they exceed stock returns (2008's flight to safety produced 20%+ returns on Treasuries while stocks fell 38%).

The bond-stock balance is the foundation of every diversified portfolio. The classic "60/40" portfolio (60% stocks, 40% bonds) tries to capture most of the equity premium with materially lower variance. Whether 60/40 still works in a low-yield world is one of the active debates in asset allocation; we'll return to it in Chapter 15.

↳ **Dig Deeper — Survivorship bias and the equity premium**

*The US has the highest equity risk premium in the developed world. Some of this is genuine economic strength. Some of it is *survivorship bias*: the US is the country that won the 20th century. Countries whose markets were destroyed (Russia 1917, China 1949, several European exchanges in WWII) don't show up in the historical-returns dataset.*

**Prompt:**
> Summarize the survivorship bias argument as developed by Dimson, Marsh, and Staunton in *Triumph of the Optimists* and the Credit Suisse Global Investment Returns Yearbook. How much of the US equity premium is plausibly attributable to "winning the 20th century" vs. genuine structural advantages? What does this imply for forward-looking equity premium estimates? Then briefly describe one or two specific markets that suffered catastrophic losses but are typically excluded from "long-run equity return" analyses.

**What to do with the output:** Save it. The survivorship-bias argument is the strongest case for using forward-looking equity premium estimates *below* the realized US historical average.

### The trade-off (concept 1)

Asset class returns trade **expected reward against year-to-year variability**. The historical record shows clearly that the assets with higher long-run returns (stocks) have higher year-to-year variability. The premium isn't free — it's compensation for accepting variance, including the very real possibility of catastrophic short-term losses. The 2008 financial crisis or the 2020 COVID crash are the kind of events that punish investors who can't (or won't) hold through the drawdowns.

### Common misconceptions

- *"Stocks always outperform bonds over long periods."* In the US, yes — for the past century. In Japan since 1990, no. Country selection matters.
- *"Bonds are safe."* Bonds are safer than stocks but can have multi-year drawdowns of 20%+ in real terms (the late-1970s bond market is the canonical case).
- *"The equity premium is a constant."* It varies across periods, countries, and time horizons. Forward-looking expectations should be lower than realized historical averages.

---

## Concept 2 — Major drawdowns

The smooth long-run averages hide brutal short-run episodes. Five US drawdowns deserve specific attention.

### 1929-1932 (Great Depression)

The S&P composite peaked in September 1929 and fell about 86% over the next three years. Adjusted for the deflation of the period, the real loss was a bit less but still well over 70%. The market did not regain its 1929 peak (in nominal terms) until 1954 — twenty-five years later. In real, dividend-reinvested terms, recovery was somewhat faster but still took many years.

The 1929-32 episode is a useful corrective to "stocks always recover quickly" intuitions. The recovery was real, but the time scale was generational.

### 1973-1974

The S&P 500 fell about 48% from peak to trough during the recession that accompanied the OPEC oil shock and the Bretton Woods collapse. Inflation was high; real losses were severe. The market took roughly a decade to fully recover in real terms.

### 2000-2002 (dot-com bust)

The S&P 500 fell about 49% from peak to trough. The NASDAQ fell about 78%. Recovery to the prior peak took five years for the S&P, much longer for the NASDAQ. Many of the dominant 1999-vintage companies (pets.com, Webvan, AOL after the Time Warner merger) never recovered at all.

### 2008-2009 (Financial Crisis)

The S&P 500 fell about 57% from October 2007 to March 2009. It reclaimed its prior peak in March 2013 — about 5.5 years from peak to recovery. Some sectors (financials, real estate) took much longer; many never fully recovered.

### 2020 (COVID)

The S&P 500 fell 34% in 33 days — the fastest bear market in US history. It reclaimed its prior peak in just 5 months. The sharpness of both the decline and the recovery was unusual; the brevity is partly attributable to fast and aggressive monetary and fiscal policy responses.

### 2022 (rate spike)

Less severe but worth noting. The S&P 500 fell about 25% in calendar 2022 amid the fastest Fed tightening cycle in 40 years. Bonds simultaneously fell 13%, breaking the typical stocks-bonds diversification benefit. The "60/40 portfolio" fell about 17% — its worst year since the 1930s in nominal terms.

### What the drawdowns share

Each drawdown was preceded by a period of strong returns and rising valuations. Each was accompanied by a macro shock (depression, oil, tech bubble, financial crisis, pandemic, inflation). Each was partially recovered through the next expansion.

What they did *not* share: timing predictability. With hindsight, every drawdown had warning signs. Without hindsight, none was widely anticipated. Each one was confidently denied by significant fractions of the financial commentariat right up to the moment it began. This is the core difficulty with active market timing.

### Worked example — what your company looked like through 2008

For your chosen company, look up its stock chart from October 2007 through March 2009. What was the maximum drawdown? How does it compare to the S&P 500's 57% decline?

Some companies did much better than the market (consumer staples like Walmart, Procter & Gamble, McDonald's). Some did much worse (financial firms, leveraged industrials). Some were essentially destroyed (Lehman Brothers, Bear Stearns, Wachovia). The dispersion within the market is as informative as the market average.

This is exercise 12.7 in the project. It connects historical context to your company's idiosyncratic story.

↳ **Dig Deeper — Sequence-of-returns risk in retirement**

*Two retirees with identical 30-year average returns can have very different outcomes — the one who experiences early-retirement losses runs out of money; the one with early-retirement gains thrives. Sequence matters as much as average return when you're drawing on a portfolio.*

**Prompt:**
> Explain sequence-of-returns risk with a specific worked example: two retirees, both starting with $1M, both withdrawing 4% per year (inflation-adjusted), both achieving 7% average annual return over 30 years — but with the order of returns reversed. Show that the one with bad early returns runs out of money while the other ends up with substantial wealth. What does this imply for asset allocation around retirement age?

**What to do with the output:** Save it. Sequence-of-returns risk is a key concern in personal financial planning that the long-run-average framing hides.

### The trade-off (concept 2)

The realized return data trades **smoothness against representativeness**. Long-run averages smooth across drawdowns. Investors who actually invested through them experienced something very different from the smoothed average. For a buy-and-hold investor with a 30+ year horizon, the average is meaningful. For a 60-year-old who needs to draw on retirement savings, a 50% drawdown a year before retirement is catastrophic in a way the long-run average cannot capture.

### Common misconceptions

- *"The market always recovers."* It always has, in the US, eventually. Time horizons of 25 years (1929 case) or longer are real.
- *"Diversification protects against everything."* In ordinary markets, yes. In genuine crises (1929, 2008), correlations rise toward 1 and most assets fall together. The "correlation crisis" of 2008 made diversification much less helpful exactly when investors needed it most.

---

## Concept 3 — Implications for analysts and investors

Three takeaways from the historical record matter for the equity research project and for any thoughtful approach to investing.

### 1. The equity premium is real but not guaranteed

US stocks have outperformed bonds and cash by a wide margin over essentially every long horizon in the past century. The premium is large enough that, for a long-horizon investor, equity allocation is the correct default.

But the historical equity premium reflects the experience of *one country* over *one century*. The US economy benefited from political stability, geographic security, deep capital markets, and post-WWII economic dominance. None of these is guaranteed to continue. International data (Dimson-Marsh-Staunton's *Credit Suisse Global Investment Returns Yearbook*) shows that several developed markets have substantially lower equity premia than the US — and one (Japan) has had essentially no equity premium for over thirty years.

For forward-looking valuation, the cautious move is to use an expected ERP somewhat lower than the long-run US realized average. 4-6% is the modern academic and practitioner consensus.

### 2. Market timing is harder than it looks

The data on "missing the best days" is consistent and damning. Across virtually every long sample, the best 10 trading days produce so much of the total return that missing them — even if you also miss the worst days — leaves you substantially worse off than buy-and-hold.

The reason: the worst days and the best days tend to cluster in volatile periods. An investor who flees at the bottom misses the recovery. The 2020 COVID crash and recovery is the canonical recent case: the S&P 500 fell 34% in 33 days, then rallied 75% over the following 18 months. Many investors who sold during the panic locked in the loss and did not get back in for the recovery.

This does not mean every investor should hold every stock through every drawdown. It does mean that systematic, disciplined market timing is rare among professional investors, and even rarer when you adjust for survivorship bias.

For the project, this implies that your equity research thesis should be a long-run thesis. If your conclusion is "this stock will outperform over the next 5+ years for the following reasons," that's a defensible analytical claim. If your conclusion is "this stock will go up in the next month," you're doing technical analysis, not fundamental research.

### 3. The future is not the past

The most important caveat of historical-return analysis: every number in this chapter is *realized* return, not *expected* return. They are not the same thing.

Realized returns reflect what actually happened. Expected returns reflect what investors anticipated. The two can diverge for long periods — investors may underestimate or overestimate future returns, and the divergence shows up as realized returns being above or below expectations.

The long-run historical average return is a useful benchmark for *forward* expectations, but it is not a forecast. The 12.6% nominal return on stocks since 1981 reflects, in part, a falling discount rate from 14% Treasury yields in 1981 to 1.5% in 2020 — a one-time tailwind that lifted equity prices through multiple expansion. The next 40 years cannot deliver the same tailwind because Treasury yields cannot fall by another 12 percentage points.

For the equity research project, this means your DCF should not assume that future returns mechanically equal historical returns. The CAPM (Chapter 14) and WACC (Chapter 17) machinery embed this reality — the discount rate is forward-looking and reflects current conditions.

### Worked example — building forward expectations from the historical record

For your equity research model, you'll need a few forward-looking inputs. Reasonable starting points, with sensitivity analysis:

- **Risk-free rate**: current 10-year Treasury yield (around 4-5% as of recent data, depending on the cycle).
- **Equity risk premium**: 4.5-5.5% (current academic/practitioner consensus, lower than realized historical average).
- **Long-term growth rate** (for DCF terminal value): 2-3% (roughly long-run real GDP growth, consistent with mature-economy growth expectations).
- **Inflation expectation**: 2-3% (Fed target plus modest premium).

These are *base-case* assumptions. Your sensitivity analysis should include alternative scenarios. The work isn't picking one scenario; it's showing how the conclusion changes across reasonable scenarios.

### The trade-off (concept 3)

The historical record trades **certainty about the past against uncertainty about the future**. The data is what it is. Whether tomorrow looks like yesterday is a separate question, and one historical analysis alone cannot answer.

### Common misconceptions

- *"The historical equity premium will continue."* It probably won't be exactly the same. Forward-looking expectations are the appropriate input to valuation.
- *"You should buy and hold no matter what."* Buy-and-hold works for diversified equity index funds with long horizons. Individual stocks can permanently lose value. The buy-and-hold lesson is about *the market*, not about *individual stocks*.

---

## Synthesis — what the data lets us claim

After a century of careful data, the following claims are well-supported:

1. **Equities have outperformed bonds and cash by a substantial margin** over long periods in the US. The premium is real and large.
2. **The equity premium is variable**, both across countries and across time periods. Forward expectations should be lower than realized historical averages.
3. **Drawdowns are recurring and severe.** Investors who cannot tolerate 30-50% interim losses should not hold a 100% equity portfolio, regardless of long-run averages.
4. **Market timing is hard.** Missing a small number of best days substantially reduces long-run returns. Most active timing strategies underperform buy-and-hold after costs.
5. **Diversification works in normal markets but partially breaks in crises.** Correlations rise during stress; tail risks are systemic.

These five claims are the backbone of every defensible long-term investing argument. They are also the historical context that the rest of this book — particularly Chapters 13-15 — builds quantitative tools to engage with.

For the equity research project, this chapter establishes the empirical context for your investment thesis. When your DCF says your chosen stock is worth $X and the market says it's worth $0.85X, your case for the divergence rests on specific firm-level analysis — but the broader claim that equity research can identify mispricings rests on the long-run record that markets are sometimes wrong.

---

## Exercises

### Warm-up

**12.1** State approximate long-run nominal annual returns for: large-cap US stocks, US Treasury bonds, US T-bills, and inflation. State the equity risk premium implied by these numbers.

**12.2** Define "drawdown." What was the magnitude and duration of the 2008-09 S&P 500 drawdown? The 2020 COVID drawdown?

**12.3** Why might forward-looking expected equity returns be lower than realized historical returns?

### Application

**12.4** Pull data from FRED or another source on the S&P 500 (`SP500`), 10-year Treasury yield (`DGS10`), and headline CPI (`CPIAUCSL`) over the past 40 years. Compute:

(a) Annualized total return on the S&P 500 (assume dividend reinvestment; the total-return index ticker is `^SP500TR` on Yahoo Finance).
(b) Annualized return on a constant-maturity 10-year Treasury (approximate).
(c) Annualized inflation rate.
(d) The equity risk premium (S&P 500 return minus Treasury return).
(e) Real returns for each.

**12.5** For your chosen company, plot the stock price (or total return index) from October 2007 through December 2009. Compare its drawdown and recovery to the S&P 500's. What does the comparison tell you about the firm's resilience?

**12.6** A friend says, "I've been watching the market for the last 6 months and I think we're about to crash. I'm going to cash for now and get back in after." Construct three counter-arguments grounded in this chapter's data.

### Synthesis

**12.7** A 65-year-old retiree has $1 million in a 100% equity portfolio. The market falls 50% in the next year (a 2008-style drawdown). Write a one-page assessment of:

(a) The retirement plan's current sustainability under typical 4% withdrawal rules.
(b) Whether the long-run historical equity premium is consoling or insufficient at this point.
(c) What asset allocation might have been more appropriate, and why.

**12.8** The historical equity premium in the US is much higher than in many other developed economies. Construct three explanations: (a) the US has been genuinely better, (b) survivor bias makes us see the winning case, (c) the divergence is partly random. For each, identify what evidence would distinguish it from the others.

### Challenge

**12.9** Compute the consequence of "missing the best days" for your own retirement projection:

(a) Assume you invest $5,000 per year for 40 years at the long-run average S&P 500 return of 10%.
(b) Compute the future value with all returns intact.
(c) Compute the future value if you miss the *best 5% of years* (about 2 years of returns out of 40, randomly distributed but forced to be the highest 2 of the 40).

For (c), one approximation: if the worst 38 of 40 years average 6% nominal (the average minus the best 2 years roughly equates), use that for years 1-38 and zero for the missed best 2 years. The exact calculation requires Monte Carlo simulation; an approximate answer is fine.

**12.10** The Dimson-Marsh-Staunton dataset shows substantial variation in long-run equity premia across countries. The US, Australia, and South Africa have the highest premia; Italy, Belgium, and Austria the lowest. Speculate on why these differences exist. What implications might this have for an investor diversifying internationally today?

---

## Chapter summary

- Long-run US asset returns (1981-2020 averages): stocks ~12.6%, bonds ~8.2%, T-bills ~3.9%, inflation ~2.9%.
- The **equity risk premium** is the gap between stock and Treasury returns. Long-run realized: 5-9 percentage points. Forward-looking expectation: 4-6%.
- Major drawdowns: 1929-32 (-86%, 25-year recovery), 1973-74 (-48%), 2000-02 (-49%), 2008-09 (-57%), 2020 (-34%, 5-month recovery), 2022 (-25%).
- Missing the best 10 trading days over 40 years cuts long-run returns by more than half.
- The historical record reflects one country over one century. Forward-looking expectations should be more modest than realized historical averages.
- US equity premium is high by international standards.

---

## What would change my mind

The chapter argues that long-run US equity returns provide a useful but imperfect guide to forward expectations, and that the equity premium is real but smaller than realized averages suggest. The reading would have to revise if (a) a sustained period of equity returns substantially below historical averages emerged in the US (we may be in such a period now; the 2010-2020s may look unusual in retrospect), or (b) new methodologies for estimating expected returns turned out to be substantially more accurate than backward-looking averages. Forward-looking implied-cost-of-capital methods are the leading academic alternative; they're better than naive averages but still imperfect.

## Still puzzling

The cleanest unresolved question is *whether the next 40 years will look like the last 40*. The 1981-2020 period had an enormous tailwind: declining interest rates from 14% to 1.5% pushed bond prices up, reduced corporate borrowing costs, raised P/E ratios, and lifted equity returns. That tailwind cannot repeat. So forward-looking returns probably will be lower. By how much? I don't know. Reasonable estimates range from "1-2 percentage points lower" to "substantially lower." This uncertainty propagates directly into every DCF-based valuation. Honest analysts include it as a sensitivity case; sloppy analysts pretend it doesn't exist.

---

## Connections forward

- **Chapter 13** installs the statistical machinery for measuring risk.
- **Chapter 14** computes beta — the regression of a stock's returns on the market.
- **Chapter 15** applies these results to portfolio construction and personal investing.
- **Chapter 17** uses the equity premium and risk-free rate to compute the cost of equity.

---

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

**Roger Ibbotson** was compiled the historical US stock-and-bond returns dataset that anchors modern asset-allocation studies.

**Run this:**

```
Who is Roger Ibbotson, and how does their work connect to US market history we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about their career or ideas.
```

→ Search **"Roger Ibbotson"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to apply Roger Ibbotson's framework to a specific finance question.
- Add a constraint: "Answer including criticisms or limits of Roger Ibbotson's framework."

What changes? What gets better? What gets worse?
