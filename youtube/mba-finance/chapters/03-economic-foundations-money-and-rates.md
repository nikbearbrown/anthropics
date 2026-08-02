# Chapter 3 — Economic Foundations: Money and Rates
*Why a number that seems to mean one thing always means something else.*

---

In March 2022, the federal funds rate was 0.08%. By July 2023, it was 5.33%. The Fed raised rates eleven times in sixteen months — the fastest tightening cycle in forty years.

What happened next is the puzzle this chapter is built around. A 30-year fixed mortgage that cost 3% in early 2022 cost 7% by late 2023. For the same house, the monthly payment roughly doubled. Three of the largest US bank failures in history happened in March 2023. Public-company tech valuations compressed 30–50% in some cases. The dollar appreciated against most major currencies. Inflation, which had peaked at 9.1% in June 2022, drifted back toward 3% by mid-2024.[^1]

[^1]: Federal Reserve Bank of St. Louis, "Federal Funds Effective Rate" (FEDFUNDS); Bureau of Labor Statistics, "Consumer Price Index for All Urban Consumers" (CPIAUCSL). Both via FRED.

That is one number — the federal funds rate — propagating through the entire economy. Every one of those consequences followed from the same mechanical fact: money got more expensive to rent.

The word "rent" is the key. Once you see an interest rate as a rental price, almost everything else in this chapter falls into place.

---

## Interest rates as the price of money

If you rent a car for a day, you pay a daily rate. If you rent money for a year, you pay an annual rate, and we call it interest. Same logic entirely. The rate is the price, and like all prices it is set in a market — the market for loanable funds.

Suppliers of loanable funds are people and institutions with more income than they want to spend right now: households saving for retirement, firms with surplus cash, foreign investors looking for safe places to park money. They will lend more when the price is higher. Demanders of loanable funds are people and institutions that want to spend more than their current income: households buying houses, firms financing factories, governments running deficits. They will borrow more when the price is lower. The intersection sets the equilibrium rate.

That is the surface story. Two layers underneath matter more for anything you will actually do with this.

**Layer one: nominal versus real.** The rate quoted on your savings account is the *nominal* rate — the actual stated number. But that number does not tell you whether saving is worthwhile or borrowing is expensive. Inflation does.

Put $1,000 in a savings account at 6% for a year. You have $1,060. But if inflation was 2%, the basket of goods that cost $1,000 twelve months ago now costs $1,020. Your $1,060 buys you that basket and leaves $40 over. The $40 is your *real* return — the actual gain in purchasing power. The rest was just compensation for the fact that prices rose.

The arithmetic:

$$\text{Real rate} \approx \text{Nominal rate} - \text{Inflation rate}$$

The exact formula is $(1 + r_\text{nominal})/(1 + \pi) - 1$, where $\pi$ is inflation, but the approximation is accurate enough at ordinary rates.

Here is why this matters in a way that surprises almost everyone who encounters it for the first time. A small business in 1981 paid 15% nominal interest on a bank loan. Fifteen percent. That sounds punishing. But inflation that year was running near 12%. Real cost: about 3%. Compare to a firm today paying 6% nominal in a 2% inflation environment — real cost about 4%. The 1981 rate was *less* expensive in real terms than the 6% rate today, even though the headline number was two and a half times higher.

The nominal rate is the thing you see. The real rate is the thing that matters. When you read about interest rates anywhere — a newspaper, an earnings call, a Fed statement — you must know inflation in the same period to understand them. The headline number without inflation context is not useful information. It is noise dressed as signal.

<!-- → [TABLE: side-by-side comparison of three historical rate environments — columns: year/period, nominal rate, inflation rate, real rate, implication for borrowers — should show the 1981 paradox visually] -->

**Layer two: the risk premium.** The market does not quote one interest rate. It quotes thousands. A 3-month Treasury bill, a 10-year corporate bond from a healthy firm, a high-yield bond from a struggling retailer, a credit card balance — all different rates, all on the same day.

What separates them is the risk premium. The lender charges more for credit that is more likely to default.

The lowest rate in the system is the risk-free rate — what the US government pays to borrow short-term in its own currency. The Treasury can, in extremis, raise dollars by taxing or creating them, so the risk of nominal default is essentially zero. Every other borrower pays more than the Treasury, and the spread is the market's live assessment of credit risk.

A few representative steps up the ladder: investment-grade corporate bonds carry a spread of perhaps 50–150 basis points over Treasuries (1 basis point = 0.01%). High-yield bonds carry 300–800 basis points, wider in stressed periods. Credit cards carry 15–25% APR because the lender has no collateral — if you stop paying, there is nothing to repossess.

For the equity research project, the rates that matter most for your chosen company are its own borrowing rates — the yields on its outstanding bonds and the rate on its bank credit lines. These appear in the 10-K's debt footnote and tell you the market's current assessment of the firm's credit risk in real time.

<!-- → [CHART: yield ladder showing risk premium steps from T-bill to investment-grade to high-yield to credit card, with approximate basis point spreads — student should see how each step adds credit risk premium] -->

---

## Inflation, GDP, and unemployment

Interest rates are the price of money. The macro variables — inflation, GDP, unemployment — are the environment that determines what that price should be and how it propagates.

**Inflation is not one number.** This is the thing the financial press obscures constantly, and it will trip you up in analysis if you don't have it straight.

*Consumer Price Index (CPI)* is the one most people mean when they say "inflation." The Bureau of Labor Statistics constructs a fixed basket of goods and services that a typical urban household buys — food and beverages, housing, apparel, transportation, medical care, recreation, education — and tracks what that basket costs month to month. The most-cited series is CPI-U All Items seasonally adjusted; the FRED ticker is `CPIAUCSL`.

*Core CPI* strips out food and energy. Why? Because food prices spike when there's a drought and energy prices spike when there's a war. These are real disruptions but they don't respond to monetary policy on the timescale of a Fed decision. The Fed watches core inflation more closely than headline CPI because core shows the underlying trend, not the noise.

*Producer Price Index (PPI)* tracks prices that producers pay for inputs — raw materials, intermediate goods, business services. PPI tends to move before CPI in many cycles, because input cost increases work their way into consumer prices over time. Rising PPI in 2021 was an early signal of the 2022 CPI surge.

*GDP deflator* is what the Bureau of Economic Analysis computes as the ratio of nominal GDP to real GDP. It covers everything in GDP — capital goods, government services, exports — not just consumer goods, and it is dynamically reweighted as the composition of GDP changes. For consumer-facing analysis, CPI is the right benchmark. For macro modeling or cross-country comparisons, the deflator is cleaner.

The choice of measure is itself an analytical decision. When you want to know whether your company's pricing is keeping pace with inflation, use CPI for consumer-facing firms. For input-cost analysis, find the relevant PPI sub-series. They are measuring different things.

<!-- → [TABLE: four inflation measures side by side — what's included, what's excluded, who uses it, FRED ticker, when to reach for it] -->

**GDP.** Gross Domestic Product is the market value of all goods and services produced within an economy in a year. The standard decomposition has four buckets: consumption (C), investment (I), government spending (G), and net exports (NX). So $\text{GDP} = C + I + G + NX$.

A few things worth getting straight. Consumption is roughly two-thirds of US GDP — the economy runs on household spending. Investment here means business spending on capital goods, residential construction, and inventory changes. It does *not* mean the everyday sense of buying stocks. Stock purchases between investors don't add to GDP; they are transfers of existing claims on real assets.

*Nominal GDP* is measured at current prices. *Real GDP* strips out the effect of inflation by using a base year's prices. The difference is not academic. If nominal GDP rose 5% and inflation was 4%, real growth was only about 1%. A "growing economy" by nominal numbers can be a stagnant or shrinking economy in real terms. Every time you see a GDP growth number, your first question should be: nominal or real?

**Unemployment.** The Bureau of Labor Statistics computes this monthly from a survey of roughly 60,000 households. The formula is:

$$\text{Unemployment Rate} = \frac{\text{Unemployed}}{\text{Employed} + \text{Unemployed}}$$

The crucial subtlety: the denominator is the labor force, not the working-age population. To be counted as unemployed, you must be actively looking for work. A discouraged worker — someone who has given up searching — disappears from the unemployment statistic without finding a job. That makes the headline rate look better than the underlying labor market is. The BLS publishes alternative measures (U-1 through U-6) that capture wider definitions of underutilization; the headline rate is U-3.

These three variables — inflation, GDP, unemployment — are not independent. They move together in patterns, and the patterns have names.

The **Phillips curve** is the empirical observation that low unemployment tends to come with rising inflation, and high unemployment with falling inflation. The Fed manages this relationship. It can produce low unemployment or low inflation more easily than both simultaneously. The 2022–2024 cycle was a live test of whether the Fed could engineer a "soft landing" — bring inflation down without sending unemployment sharply higher. By mid-2024, the soft landing looked partially achieved.

<!-- → [CHART: scatter plot of US unemployment rate vs. core CPI inflation, 1960–present, color-coded by decade — student should see the relationship, its breakdown in the 1970s, its apparent flattening in the 2010s, and the 2022 episode] -->

---

## The business cycle, exchange rates, and reading the data

The macro variables move together over time in a pattern: GDP expands faster than its long-run trend for a while, then contracts, then expands again. This is the **business cycle**, and it has four named phases.

*Expansion* — GDP rising, unemployment falling, inflation pressure building. *Peak* — the moment expansion stops and contraction begins, usually visible only in retrospect. *Recession (contraction)* — GDP falling, unemployment rising, inflation pressure easing. *Trough* — the moment contraction stops and recovery begins, also mostly visible in retrospect.

The popular shorthand for recession is two consecutive quarters of declining real GDP. The official US call is made by the **National Bureau of Economic Research**, a private nonprofit that considers a broader set of indicators: real income, employment, industrial production, wholesale and retail sales, plus GDP. The NBER call usually comes well after the recession has started — sometimes after it has ended. They are documenting, not predicting.

From the historical US data: average contraction lasts about 17 months; average expansion lasts about 41 months. The longest expansion on record ran from June 2009 to February 2020 — 128 months — before the COVID-19 pandemic ended it. The 2020 recession was one quarter long but unusually deep; the recovery was unusually fast.

For an analyst, cycle awareness is context, not forecast. In late expansion, watch for margin pressure from rising labor costs and signs the firm is over-extending capital expenditure. In contraction, watch for revenue compression and liquidity. Knowing where you are in the cycle changes what you look for, without requiring you to predict where you are going.

<!-- → [INFOGRAPHIC: business cycle diagram — the four phases labeled, with arrows showing the sequence and notes on what to watch for in each phase as an equity analyst] -->

**Exchange rates.** The **spot exchange rate** is the price to immediately convert one currency into another. If the rate is MXN16 per USD, it costs sixteen pesos to buy one dollar, or equivalently one dollar buys sixteen pesos.

When a currency's price rises relative to another, it has *appreciated*. When it falls, it has *depreciated*. These are always relative — the appreciation of one currency is the depreciation of its counterpart.

Three forms of currency exposure matter for a firm.

*Transaction exposure* — the firm has a known future cash flow in a foreign currency, and the exchange rate may move before that cash arrives. A US company contracted to receive €10 million in six months bears euro-exposure for those six months. If the euro depreciates 5% against the dollar, the firm receives 5% less in dollars than it expected. Forward contracts and options exist to lay off this risk.

*Translation exposure* — a multinational with foreign subsidiaries consolidates financial statements in one currency. Foreign subsidiary results get translated at prevailing exchange rates. If the foreign currency strengthens, the subsidiary's contribution to consolidated results looks larger in dollar terms — even if the underlying business didn't change at all. When you read a multinational's 10-K, the MD&A often presents "constant-currency" growth specifically to strip out this accounting effect.

*Economic exposure* — even a purely domestic firm can be affected by exchange-rate movements it never touches directly. A US ski resort competes with Mexican beach resorts for American vacationers. When the dollar appreciates against the peso, Mexico becomes cheaper for US tourists, and the ski resort loses customers without transacting in any foreign currency. Economic exposure is the longest-running and hardest-to-hedge of the three.

<!-- → [TABLE: three forms of currency exposure — transaction, translation, economic — with definition, example, typical hedging approach, where to find it in a 10-K] -->

**Reading the data.** The single most useful free tool for macro work is **FRED** — Federal Reserve Economic Data, maintained by the Federal Reserve Bank of St. Louis. FRED hosts more than 800,000 economic time series from the Federal Reserve, Bureau of Labor Statistics, Bureau of Economic Analysis, US Census, and dozens of other sources. Every series has a unique ticker. CPIAUCSL is headline CPI. FEDFUNDS is the federal funds rate. GDPC1 is real GDP. UNRATE is the unemployment rate. DGS10 is the 10-year Treasury yield. You can pull thirty years of any series and export it to CSV in under two minutes.

Two operations on time series come up constantly.

*Percentage change* from one period to the next:

$$\text{\% Change} = \frac{X_2 - X_1}{X_1}$$

Japanese real GDP was 522,594.2 billion yen in Q1 2013 and 527,277.0 billion yen in Q2 2013:

$$\frac{527{,}277.0 - 522{,}594.2}{522{,}594.2} = 0.00896 = 0.896\%$$

That is quarterly growth of about 0.9%, or roughly 3.6% annualized.

*Index construction* rescales a series so a chosen base period equals 100. This makes comparing across series with different absolute levels straightforward. CPI indexed to 1970 = 100 reads about 666 in 2020 for the US, meaning the US price level was roughly 6.7 times its 1970 level. Switzerland's same index reads about 302. Japan's reads about 332. Most of Japan's increase happened in the 1970s; the country then experienced decades of near-zero inflation and even deflation.

<!-- → [CHART: CPI index chart for US, Switzerland, and Japan from 1970–2020, all rebased to 100 in 1970 — student should see the divergent paths and the Japan story clearly] -->

---

## The thing that connects all of it

Here is the whole picture in one place.

Interest rates are the price of money. That price is set in the market for loanable funds, pushed up or down by the Federal Reserve's policy decisions, and modified for each borrower by a risk premium. The nominal rate is what you see; the real rate — nominal minus inflation — is what drives actual decisions about whether to borrow, lend, invest, or save.

Inflation, GDP, and unemployment are the macro environment that determines what that price should be and how the economy responds to it. They move together: when unemployment falls, inflation tends to rise, and the Fed responds by raising rates, which cools investment and consumption, which eventually raises unemployment again. The business cycle is this loop running repeatedly, with varying timing and amplitude.

Exchange rates add a second layer for any firm with cross-border operations: the price of money is now relative across currencies, and a move in exchange rates can change the economics of a business without anyone inside the business making a different decision.

FRED is where you find the data for all of it.

A finance student who can read a 10-K but cannot read the macro environment is half-trained. The 10-K tells you what happened at one firm. The macro environment tells you what was happening to everyone at once — the weather all the companies were operating in during that period. Skipping macro produces analysis that is technically precise and contextually blind. Putting them together is what the equity research project is actually for.

---

## What would change my mind

This chapter argues that macro variables — interest rates, inflation, GDP, unemployment, the cycle, exchange rates — are essential context for any serious financial analysis, and that they need to be made specific (CPI versus core, real versus nominal, U-3 versus U-6) rather than treated as one-word headlines. I would revise if (a) macro variables turned out to be substantially uncorrelated with company-level fundamentals over decadal horizons (some research suggests the link is weaker than introductory texts assume, particularly for large diversified firms), or (b) algorithmic approaches to investing made macro context less important than firm-specific data signals. Neither of these displaces the chapter's claim, but both qualify it.

## Still puzzling

I am most uncertain about how to teach the transmission from Fed policy to asset prices clearly. The channels are real — rates affect discount rates, which affect valuations; rates affect mortgages, which affect housing, which affects consumption; rates affect currency values, which affect multinational earnings. But the magnitudes vary cycle to cycle, and the quantitative effect in any given case is hard to predict in advance. The 2020 case (rates collapsed, asset prices soared) was clean. The 2022–2024 case (rates rose more than five points, equities fell less than expected, real GDP held up) was muddy. I don't have a clean way to make this both honest about the uncertainty and useful for someone encountering it for the first time. The chapter makes the qualitative case and shows where to find the data; the rest is judgment that develops with experience.

---

## Connections forward

- **Chapters 7–9** convert interest rates into the time-value-of-money arithmetic that underlies every valuation in the book.
- **Chapter 10** uses interest rates to price bonds.
- **Chapter 11** uses the discount rate in DCF models.
- **Chapter 14** computes beta — the regression of a stock's returns on the market — which is itself a function of the macro environment.
- **Chapter 17** uses the cost of debt and equity to compute WACC, the firm's weighted-average cost of capital.
- **Chapter 20** revisits exchange-rate exposure as a risk-management problem.

---

## Exercises

### Warm-up

**3.1** In your own words, explain the difference between the nominal interest rate and the real interest rate. Why is the nominal rate insufficient on its own for evaluating whether borrowing is expensive or saving is worthwhile? *(Tests: nominal vs. real distinction.)*

**3.2** A firm carries $2 billion in long-term debt at a nominal rate of 4.8%. Core CPI inflation is running at 3.1%. What is the firm's approximate real cost of debt? In dollar terms, of the $96 million in annual interest expense, how much is compensating lenders for inflation and how much is real cost? *(Tests: Fisher equation arithmetic. Difficulty: low.)*

**3.3** Name the four inflation measures covered in this chapter. For each, state in one sentence what it measures and name one analytical context where it is the right choice over the others. *(Tests: CPI / core CPI / PPI / GDP deflator distinctions. Difficulty: low.)*

### Application

**3.4** Pull the federal funds rate (FEDFUNDS) and the 30-year fixed mortgage rate (MORTGAGE30US) from FRED for the past 20 years. Plot them together. Write two paragraphs: one describing when the two series move together, one describing at least one period where they diverged — and your hypothesis for why. *(Tests: FRED fluency + transmission-channel reasoning. Difficulty: medium.)*

**3.5** Find your chosen company's most recent 10-K. From the debt footnote, extract the weighted-average nominal interest rate on outstanding long-term debt. Using current core CPI as your inflation measure, compute the real cost of debt. Compare to the same calculation for a period of high inflation of your choice. What does the comparison reveal? *(Tests: nominal-to-real translation applied to a real firm. Difficulty: medium.)*

**3.6** The official US recession call comes from the NBER, not from the two-consecutive-quarters rule. Pull the NBER recession dates for the past 40 years and compare them to the dates when real GDP first turned negative. For two recessions of your choice, describe how much time elapsed between the economy's deterioration and the official NBER call — and what that lag implies for using official recession dates in real-time analysis. *(Tests: business cycle mechanics + NBER vs. rule-of-thumb distinction. Difficulty: medium.)*

### Synthesis

**3.7** A US consumer electronics company generates 55% of its revenue in Europe and Asia. In a given quarter, its dollar-denominated revenue grows 4% year-over-year, but the MD&A reports that revenue growth at constant currency was 9%. Reconstruct the arithmetic: what does this imply about the direction and approximate magnitude of dollar movement against the relevant foreign currencies? Classify the exposure type at work in this MD&A adjustment. *(Tests: translation exposure + constant-currency arithmetic. Difficulty: medium-high.)*

**3.8** The chapter argues that macro variables are essential context for financial analysis but acknowledges that the link between macro variables and company-level fundamentals may be weaker than introductory texts assume for large diversified firms. Pick a large diversified company (a conglomerate, or a firm with significant revenue in multiple sectors and geographies). Identify two macro variables that should theoretically affect its business. Then pull those variables from FRED alongside the company's quarterly revenue for the past ten years. Describe what you observe: does the company move with the macro variables you chose, or does diversification dampen the relationship? *(Tests: macro-to-firm linkage skepticism + empirical observation. Difficulty: high.)*

### Challenge

**3.9** The 2022–2024 disinflation was unusual: inflation fell substantially without a sharp rise in unemployment, at least through mid-2024. The simple Phillips curve predicts this shouldn't be easy. Two competing explanations exist — one emphasizing that the 2021–2022 inflation was primarily supply-driven (and therefore would ease without monetary tightening causing unemployment), one arguing that well-anchored inflation expectations allowed the Fed to tighten without triggering the recessionary mechanism. Find one piece of evidence that supports each explanation and one piece of evidence that complicates each. Which do you find more persuasive, and what would definitively resolve the question? *(Tests: Phillips curve reasoning + empirical skepticism + causal inference. Difficulty: high.)*

**3.10** The chapter claims that a finance student who can read a 10-K but cannot read the macro environment is half-trained. Construct the steelman of the opposing view: that detailed macro analysis adds little value to bottom-up equity research because macro variables are largely priced into securities, firm-specific factors dominate long-run returns, and macro forecasts are unreliable enough to be noise. Then identify the conditions under which you would expect macro analysis to add the most value — and the least. *(Tests: integration of macro and company analysis; intellectual honesty about the limits of the chapter's own claims. Difficulty: high.)*

---

## LLM Exercise — Chapter 3: Macro Context for Your Company

**Project:** Equity Research Report on a Chosen Public Company  
**What you're building this chapter:** A one-page macro context section that connects current economic conditions to your company's specific exposures.  
**Tool:** Claude Project. You'll also pull a few series from FRED before prompting.

### Setup

Pull the following FRED series for the past 5 years (use https://fred.stlouisfed.org):
- **FEDFUNDS** — federal funds rate
- **DGS10** — 10-year Treasury yield
- **CPIAUCSL** — headline CPI
- **UNRATE** — unemployment rate
- **DXY** (or DTWEXBGS) — dollar index

Save them as a CSV or paste the recent values into the prompt below.

### The Prompt

```
For [your company], using the 10-K I have uploaded plus the macro data I'm pasting below, produce a one-page macro context section covering:

1. **Where we are in the cycle** — Recent GDP growth, unemployment, and inflation. State your reading of the current cycle position (early/mid/late expansion, contraction, etc.).

2. **The rate environment** — Current 10-year Treasury yield, federal funds rate, and recent direction. Note whether the yield curve is normal, inverted, or flat.

3. **Currency exposure** — From the 10-K's segment reporting, what percentage of revenue comes from outside the home country? Which currencies matter most?

4. **The company's interest rate exposure** — From the 10-K's debt footnote, what is the weighted-average cost of debt? How sensitive is the firm to a 1-percentage-point rate change? Is it stated in the 10-K?

5. **The company's pricing power vs. inflation** — From the most recent MD&A, has the firm been able to pass input cost inflation through to customers? Cite specific commentary.

[Paste your FRED data here — last 12 quarterly observations of each series.]

Don't invent numbers; if the 10-K or the data don't address something, say so.
```

### What this produces

A one-page macro context section connecting current economic conditions to specific firm exposures. Becomes a section in the final report, typically after the company snapshot and before the financial-statement analysis.

### How to adapt this prompt

- *For your own company:* Replace [your company] and adjust the currency considerations if non-US-headquartered.
- *For ChatGPT / Gemini:* Identical, but Custom GPT/Gem can hold the FRED data more cleanly than a chat window.
- *For Claude Code:* If you want the FRED pull to be automated, write a small Python script using the FRED API; otherwise use the web interface.

### Connection to previous chapters

Builds on Chapter 1's three decisions and Chapter 2's governance assessment. Macro context is the weather; the firm's decisions are made within that weather.

### Preview of next chapter

Chapter 4 introduces accrual accounting — the rules that produce the financial statements you'll be reading throughout the project. The Chapter 4 LLM Exercise will translate three of your company's recent transactions into accounting entries.

---

**Tags:** interest-rates, inflation, GDP, business-cycle, exchange-rates, FRED, macro-analysis

---

## AI Wayback Machine

**Irving Fisher** developed the Fisher equation linking nominal and real interest rates — and the Quantity Theory of Money.

![Irving Fisher](../images/irving-fisher-cz3.png)

*Puppet Art by [Nik Bear Brown](https://www.nikbearbrown.com/).*

**Run this:**

```
Who is Irving Fisher, and how does their work connect to money and rates we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about their career or ideas.
```

→ Search **"Irving Fisher"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to apply Irving Fisher's framework to a specific finance question.
- Add a constraint: "Answer including criticisms or limits of Irving Fisher's framework."

What changes? What gets better? What gets worse?
