# Chapter 3 — Economic Foundations: Money and Rates

**Suggested titles**
1. The Price of Money
2. Why Every Finance Decision Has a Rate Inside It
3. Inflation, Interest, and the Macro Weather a Firm Operates In

**TL;DR.** Every financial calculation discounts cash by an interest rate, and every interest rate is the result of supply, demand, expected inflation, and a risk premium. This chapter pulls those four moving parts apart, then shows the macroeconomic instruments — CPI, GDP, unemployment, the business cycle, exchange rates — that an analyst reads to understand the weather a firm operates in.

---

## The puzzle of the rate move

In March 2022, the federal funds rate — the short-term interest rate the Federal Reserve targets, and the rate that anchors most other US borrowing rates — was 0.08%. By July 2023, sixteen months later, the same rate was 5.33%. The Fed had raised rates eleven times in a row, the fastest tightening cycle in forty years.

The mechanics are straightforward. The Federal Reserve's Federal Open Market Committee voted at each meeting to lift its target band. The actual market rate followed within hours. By the end of the cycle, the cost of overnight money had risen by more than five percentage points.

The consequences were everywhere, and they were not straightforward at all.

A 30-year fixed mortgage that cost about 3% in early 2022 cost about 7% by autumn 2023 — for the same house, the monthly payment had roughly doubled. Used-car loans, credit cards, business lines of credit, corporate bonds, government debt: all repriced upward. Banks that had bought long-duration Treasury bonds at low yields found those bonds underwater on a mark-to-market basis; three of the largest US bank failures in history happened in March 2023, partly as a consequence. Public-company tech valuations, which had been built on near-zero discount rates, compressed by 30–50% in some cases. The dollar appreciated against most major currencies. Construction starts fell. The labor market cooled but did not crack. Inflation, which had peaked at 9.1% in June 2022, drifted back toward 3% by mid-2024 — slower than the Fed wanted, faster than many had feared.[^1]

[^1]: Federal Reserve Bank of St. Louis, "Federal Funds Effective Rate" (FEDFUNDS); Bureau of Labor Statistics, "Consumer Price Index for All Urban Consumers" (CPIAUCSL). Both via FRED. `[verify — refresh series for current vintage]`

That is one number — the federal funds rate — propagating through the economy. A finance student who can read a 10-K but cannot read the macro environment is half-trained. The 10-K tells you what happened; the macro environment tells you why what happened was happening, and what is likely to happen next.

This chapter is about the macro environment as a tool. We pull apart what an interest rate actually is, what inflation actually measures, how GDP moves, why the business cycle exists, what exchange rates do, and where to find all of this data. By the end, you should be able to read a Fed announcement and know what it implies for the company you are analyzing.

---

## Learning objectives

After working through this chapter, you should be able to:

- Distinguish nominal and real interest rates, and compute one from the other given an inflation rate.
- Explain interest rates as the equilibrium price of loanable funds.
- Specify what CPI, core CPI, the GDP deflator, and PPI measure, and identify which is right for which question.
- Define real vs. nominal GDP and explain why the difference matters.
- Identify the four phases of a business cycle and where the US economy sits in the current cycle.
- Compute the percentage change of any economic time series.
- Explain spot exchange rates, currency appreciation/depreciation, and the three flavors of currency exposure (transaction, translation, economic).
- Locate any of the above series on FRED.

**Prerequisites.** Chapters 1 and 2. Comfort with percentages and basic algebra.

---

## Concept 1 — Interest rates as the price of money

The cleanest way to think about an interest rate is as a *rental price*. If you rent a car for a day, you pay a daily rate. If you rent money for a year, you pay an annual rate, and we call that rate "interest." Same logic. Interest rates are prices.

Like all prices, they are set in a market. The market for borrowing and lending is called the **market for loanable funds**, and like the pizza market in a microeconomics textbook, it has a supply curve and a demand curve.

**Suppliers of loanable funds** are people and institutions with more income than they want to spend right now. Households saving for retirement, firms with surplus cash, governments running surpluses (less common), foreign investors looking for safe places to park money. They will lend more when the interest rate is higher — the supply curve slopes up.

**Demanders of loanable funds** are people and institutions that want to spend more than their current income. Households buying houses, students borrowing for school, firms financing factories, governments running deficits. They will borrow more when the interest rate is lower — the demand curve slopes down.

The intersection sets the **equilibrium interest rate**. When the Fed wants rates higher, it tightens the supply of available bank reserves (and now, the rate it pays on those reserves), shifting the supply curve. When borrowing demand is high — as it was during the post-2020 fiscal expansion — the demand curve shifts right and rates rise even before the Fed acts.

This is the surface story. Two layers underneath matter more.

### Layer one — nominal vs. real

The interest rate quoted on your savings account or your auto loan is the **nominal rate** — the actual stated number. Quote me 5.5% on a four-year loan, that's nominal. Quote me 6% on a savings account, that's nominal.

The nominal rate is not what tells you whether saving is worthwhile or borrowing is expensive. Inflation does. If you put $1,000 in a savings account at 6% and inflation is 2%, after one year you have $1,060 in nominal dollars — but the basket of goods that cost $1,000 a year ago now costs $1,020. Your $1,060 buys you the basket and has $40 left over. The $40 is your *real* return — what you actually gained in purchasing power.

The arithmetic is direct:

$$\text{Real rate} \approx \text{Nominal rate} - \text{Inflation rate}$$

(That is the convenient approximation; the exact formula is $r_{real} = (1 + r_{nominal})/(1 + \pi) - 1$, where $\pi$ is inflation. The two are within a fraction of a percentage point at the rates we typically see.)

The early-1980s example makes the concept land. A small business in 1981 paid 15% nominal interest on a bank loan — a number that sounds ruinous. But inflation that year was running near 12%. Real cost: about 3%. Compare to a firm today paying 6% nominal in a 2% inflation environment — real cost about 4%. The 1981 rate was less expensive in real terms than the 6% rate today, even though the headline number was 2.5x higher.

The discipline this enforces: when you read about interest rates, you must know inflation in the same period to understand them. Headline nominal rates with no inflation context are not useful information.

### Layer two — the risk premium

The market does not quote one interest rate. It quotes thousands. A 3-month Treasury bill, a 10-year corporate bond from a high-rated firm, a high-yield bond from a struggling retailer, a credit-card balance, a mortgage to a borrower with a 740 credit score, a mortgage to a borrower with a 620 credit score — all different rates, all in the same market on the same day.

What separates them is the **risk premium**. The lender charges more for credit that's more likely to default.

The lowest rate in the system is the **risk-free rate** — what the US government pays to borrow short-term in its own currency. The Treasury can, in extremis, raise dollars by taxing or by printing them, so the risk of default is essentially zero in nominal terms. Every other borrower pays more than the Treasury, and the spread is the market's assessment of credit risk.

A few representative steps up the ladder:
- **Treasury bills** — risk-free.
- **Investment-grade corporate bonds** — large, financially stable companies. Spread of perhaps 50–150 basis points over Treasuries depending on the cycle (1 basis point = 0.01%).
- **High-yield ("junk") corporate bonds** — riskier firms. Spread of perhaps 300–800 basis points over Treasuries, with much wider variation in stressed periods.
- **Prime rate** — what banks charge their best corporate customers, usually a fixed margin above the federal funds rate.
- **Mortgage rates** — long-term, secured by real estate. Generally above Treasury rates of similar maturity.
- **Credit-card rates** — unsecured, frequently 15–25% APR. The lender has no collateral; if you stop paying, they cannot repossess what you bought.

For the equity research project, the rates that matter most for your chosen company are *its* borrowing rates — the yields on its outstanding bonds and the rate on its bank credit lines. These appear in the 10-K's debt footnote and tell you the market's assessment of the firm's credit risk in real time.

↳ **Dig Deeper — Real interest rates and the Fed**

*The Fed nominally controls only the very short end of the yield curve — the federal funds rate — but its influence radiates throughout the term structure. The "real" rate (nominal minus inflation expectations) is what affects investment decisions, but inflation expectations are themselves shaped by Fed policy. The whole system has more feedback loops than the simple textbook model suggests.*

**Prompt:**
> Explain how Fed policy affects long-term real interest rates through three channels: (1) direct effects on bank borrowing costs, (2) signaling about future short-rate paths (forward guidance), and (3) shaping inflation expectations through the Fed's stated inflation target. Then describe at least one period in recent US history where Fed policy and observed long-term rates diverged from what the simple model would predict, and explain what filled the gap.

**What to do with the output:** Save it. The mechanics are the substrate of the WACC discount rate you'll compute in Chapter 17.

### The trade-off (concept 1)

Interest rates trade **the lender's compensation for waiting and bearing risk against the borrower's cost of pulling consumption forward in time**. A high interest rate makes lending more attractive (more savings) and borrowing more expensive (less investment, less consumption). The economy responds — that is the lever the Fed pulls. There is no neutral rate that satisfies everyone; the rate moves until supply and demand match.

### Worked example — what is your company's real cost of debt?

Suppose your chosen public company has $5 billion of long-term debt at a weighted-average nominal interest rate of 4.2% (you find this in the 10-K's debt footnote). Inflation, as measured by core CPI, is running at 2.8% over the past 12 months.

Real cost of debt:
$$r_{real} \approx 4.2\% - 2.8\% = 1.4\%$$

Now compare across two states of the world:
- **High-inflation regime** (early 1980s analog): nominal cost 12%, inflation 10%, real cost 2%.
- **Low-inflation regime** (2010s analog): nominal cost 4%, inflation 1.5%, real cost 2.5%.

The high-nominal regime is *cheaper* in real terms. This is non-obvious to first-time analysts and is the kind of pattern a Feynman-style first reading makes visible. The headline number lies. The inflation-adjusted number tells the truth.

### Common misconceptions

- *"Higher interest rates are bad for everyone."* They are bad for borrowers and good for savers. They redistribute, they don't uniformly destroy.
- *"Real and nominal are interchangeable in casual conversation."* They are not, especially during periods of high or volatile inflation. The 1970s lessons from this distinction were learned painfully and forgotten in the long disinflation; the 2022 inflation spike re-taught them.
- *"The risk-free rate is risk-free."* In *nominal* terms over short horizons, yes. Over long horizons in *real* terms, even Treasury holders bear inflation risk and reinvestment risk.

---

## Concept 2 — Inflation, GDP, and unemployment (the macro instruments)

If interest rates are the price of money, the next layer of the macro environment is the broader stock and flow of activity in the economy. Three measurements anchor it.

### Inflation — four measures, not one

**Inflation** is a general increase in the price level — equivalently, a fall in the purchasing power of currency. There are at least four distinct measurements that show up in a finance context, and they answer different questions.

**Consumer Price Index (CPI).** A weighted index based on the cost of a fixed basket of goods and services that a typical urban household buys. Eight major categories: food and beverages, housing, apparel, transportation, medical care, recreation, education and communication, and other. The Bureau of Labor Statistics surveys roughly 4,000 housing units and 26,000 retail establishments across 87 urban areas every month and computes the index from observed prices. The most-cited series is **CPI-U All Items** (all urban consumers, all items, seasonally adjusted) — the FRED ticker is `CPIAUCSL`. CPI is the standard gauge of consumer inflation.

A historical note that quantifies how powerful long-run inflation is: $100 in January 1913 had the same purchasing power as roughly $1,722 in 2000 and roughly $2,699 in 2021. Compounded slow inflation, over a century, is most of the change in nominal price levels you see in old photographs of department stores.[^2]

[^2]: Bureau of Labor Statistics, "CPI Inflation Calculator." `[verify]` for current values.

**Core CPI.** CPI with food and energy stripped out. Why? Food prices spike when there's a drought or a supply shock. Energy prices spike when there's a hurricane on the Gulf Coast or a war in the Middle East. These are real but volatile. Core CPI removes the volatility to show the underlying trend. The Federal Reserve watches core inflation more closely than headline CPI when setting policy because the volatile components don't respond to monetary policy on the timescales of a Fed decision.

**Producer Price Index (PPI).** Prices that producers pay for inputs — raw materials, intermediate goods, services to businesses. PPI moves before CPI in many cycles, because input-price increases work their way into consumer prices over time. Rising PPI in 2021 was an early signal of the 2022 CPI surge.

**GDP deflator.** The Bureau of Economic Analysis computes this as the ratio of nominal GDP to real GDP — effectively, the price level for everything in GDP, not just consumer goods. It includes the prices of capital goods, government services, and exports, and it is dynamically reweighted as the composition of GDP changes. For most consumer-facing finance work CPI is more relevant; for macro modeling and cross-country GDP comparisons the deflator is the right tool.

For the equity research project: when you want to ask "is my company's pricing keeping pace with inflation?", CPI is the right benchmark for consumer-facing firms. For input-cost analysis, look at the relevant PPI sub-series. The choice of inflation measure is itself an analytical decision.

### GDP — what's in the number, and why real ≠ nominal

**Gross Domestic Product (GDP)** is the market value of all goods and services produced within an economy in a year. The standard expenditure-side decomposition has four buckets:

- **Consumption (C)** — household spending. Roughly two-thirds of US GDP.
- **Investment (I)** — business spending on capital goods (factories, machinery, software), residential construction, and changes in inventories. Roughly 15–18%. Note: this is *not* the everyday meaning of "investment" (buying stocks). Stock purchases between investors don't add to GDP — they're transfers of existing claims.
- **Government spending (G)** — federal, state, and local purchases of goods and services. Roughly 20%. Excludes transfer payments (Social Security, unemployment) which are already counted when recipients spend the money.
- **Net exports (NX)** — exports minus imports. Often negative for the US.

So $\text{GDP} = C + I + G + NX$.

**Nominal GDP** is GDP measured at current prices. **Real GDP** is GDP measured at the prices of a base year — it strips out the effect of inflation. The difference matters enormously. If nominal GDP rose 5% and inflation was 4%, real growth was only about 1%. A "growing economy" by nominal numbers can be a stagnant or shrinking economy in real terms.

A scale check: at the turn of the millennium, US GDP was about $10 trillion. By 2020 it had passed $21 trillion. The economy more than doubled in nominal terms in twenty years. After accounting for inflation, real growth was much less than that — the deflator absorbed most of the increase.

### Unemployment — what's measured, and what isn't

**Unemployment** is the share of the labor force that is not working but is actively looking for work. The unemployment rate:

$$\text{Unemployment Rate} = \frac{\text{Unemployed}}{\text{Labor Force}} = \frac{\text{Unemployed}}{\text{Employed} + \text{Unemployed}}$$

The Bureau of Labor Statistics computes this monthly from a survey of roughly 60,000 households (the Current Population Survey).

The crucial subtlety: the labor force is *not* the working-age population. To be counted as unemployed, you must be actively seeking work — not retired, not in school, not "discouraged" (people who have given up looking). A discouraged worker disappears from the unemployment statistic without finding a job, which makes the headline rate look better than the labor market actually is. The BLS publishes alternative measures (U-1 through U-6) that capture wider definitions of underutilization. The headline rate is U-3.

For the project: your chosen company's labor market exposure depends on the industry. A retailer with high turnover is sensitive to the headline unemployment rate (when unemployment is low, wages rise and turnover gets expensive). A specialized engineering firm is more sensitive to skilled-labor markets where the headline rate may not capture the relevant supply.

↳ **Dig Deeper — The Phillips curve, broken or just resting?**

*The Phillips curve — the empirical relationship between unemployment and inflation — has been pronounced dead more than once. The 1970s killed the simple version. The 2010s' low-inflation, low-unemployment combination embarrassed the next-simplest version. The 2022 inflation spike resurrected interest in it. What does the modern empirical literature actually say?*

**Prompt:**
> Summarize the modern macroeconomic literature on the Phillips curve since 2000. Cover (1) the apparent flattening through the 2010s, (2) the role of inflation expectations anchoring, (3) what the 2021-2024 inflation cycle revealed about the curve's behavior at different points in the labor market. Cite specific recent papers if available. Then state your reading: is the Phillips curve a useful tool for forecasting today, or is it more of a historical relationship?

**What to do with the output:** Save it. Inflation forecasting is critical for the macro section of your equity research report; the Phillips-curve framework is one of several ways to think about it.

### The trade-off (concept 2)

Inflation, GDP, and unemployment are not independent variables. The **Phillips curve** is the empirical observation that low unemployment tends to come with rising inflation, and high unemployment with falling inflation. The relationship is weaker than economists once believed (the 1970s blew up the simple version) but the basic shape is real and is what the Fed manages — it can have low unemployment OR low inflation more easily than both. The 2022–2024 cycle was a test of whether the Fed could engineer a "soft landing" — bring inflation down without sending unemployment sharply higher. By mid-2024, the soft landing looked partially achieved; by mid-2025, the answer was clearer but still contested.

### Worked example — translating macro data into a company-specific question

Suppose you're analyzing a regional grocery chain. Three macro questions matter:

1. **Inflation:** Is the chain passing food-price inflation through to consumers, or absorbing it? Compare the company's reported same-store sales growth (from the 10-K MD&A) with food-component CPI inflation over the same period. If same-store sales growth (in dollars) outpaces food CPI, the chain is gaining real volume. If it lags food CPI, the chain is losing real volume even as nominal sales grow.

2. **GDP / consumer spending:** Grocery is income-stable — people eat in recessions — but mix shifts. In recessions, consumers trade down to private-label products and discount stores. Look at the chain's private-label penetration and gross margin trends in recent recessionary quarters.

3. **Unemployment:** Grocery is labor-intensive. When unemployment is low, hourly wages rise, increasing the chain's labor cost. Track the company's labor-cost-as-percentage-of-revenue and compare to the local unemployment rate over time.

These are the kinds of questions that turn macroeconomic data into investment-relevant analysis. The data is free (FRED) and the company data is in EDGAR. The analytical move is putting them next to each other.

### Common misconceptions

- *"Inflation is one number."* It is at least four numbers, and the choice of measure matters.
- *"GDP measures wellbeing."* It measures market output. It does not measure the value of unpaid household work, environmental quality, leisure, or distribution of income.
- *"Unemployment of 4% means 4% of working-age people are unemployed."* It means 4% of the labor force, which excludes those not looking. The denominator matters.

---

## Concept 3 — The business cycle, exchange rates, and reading economic data

The macro variables move together in patterns. The pattern has a name.

### The business cycle

GDP does not grow at a constant rate. It expands faster than its long-run trend for stretches, then contracts, then expands again. The pattern — expansion, peak, contraction, trough, expansion — is the **business cycle**. The pattern is not regular (cycles vary in length) but it is reliable enough to give names to the parts.

- **Expansion** — GDP rising, unemployment falling, eventually inflation pressure rising.
- **Peak** — the moment when expansion stops and contraction begins. Identifiable mostly in retrospect.
- **Recession (contraction)** — GDP falling, unemployment rising, inflation pressure usually easing.
- **Trough** — the moment contraction stops and expansion resumes. Also mostly identifiable in retrospect.

The popular shorthand for recession — *two consecutive quarters of declining GDP* — is a useful rule of thumb. The official call in the United States is made by the **National Bureau of Economic Research (NBER)**, a private nonprofit, which considers a broader information set: real income, employment, industrial production, wholesale and retail sales, plus GDP. The NBER call usually comes well after the recession has begun and sometimes after it has ended — they are documenting, not predicting.

Average durations from US data:
- Average contraction: about 17 months.
- Average expansion: about 41 months.
- Typical full cycle: about 4.5 years.

The longest US expansion on record ran from June 2009 to February 2020 — 128 months — before being ended by the COVID-19 pandemic. The 2020 recession was unusually short (NBER dated it as a single quarter) but unusually deep. The recovery was unusually fast. The expansion that followed has now run, depending on how you measure, into its sixth year.

For an analyst, knowing where you are in the cycle changes what you should be looking for. In late expansion, watch for margin pressure from rising labor costs and signs that the firm is over-extending capex. In contraction, watch for revenue compression and the firm's liquidity position. Cycle awareness is not a forecast — it's a context.

### Exchange rates and the multinational firm

A second set of macro forces affects any firm with operations or customers outside its home market — which is most large public companies.

The **spot exchange rate** is the price to immediately convert one currency to another. If the rate is MXN1 = USD0.0625, it costs $0.0625 to buy one Mexican peso (equivalently, MXN16 ≈ USD1).

When a currency's price rises, we say it has **appreciated**. When the price falls, **depreciated**. If the peso appreciates from MXN16/USD to MXN14/USD, the dollar buys fewer pesos — equivalently, the dollar has depreciated against the peso. Currencies move relative to each other; appreciation of one is depreciation of the other.

Three flavors of currency exposure matter for a firm.

**Transaction exposure.** The firm has a known future cash flow in a foreign currency, and the exchange rate may move before the cash flow occurs. A US firm that has signed a contract to receive €10 million in six months bears euro-exposure for those six months. If the euro depreciates by 5%, the firm receives 5% less in dollars than it expected. Hedging tools (forward contracts, options) exist to lay off this risk; we'll come back to them in Chapter 20.

**Translation exposure.** A multinational with foreign subsidiaries reports consolidated financial statements in one currency (the parent's). Subsidiary balance sheets and income statements get translated at exchange rates. If the foreign currency strengthens, the foreign subsidiary's contribution to consolidated results — measured in dollars — looks bigger. Translation effects can swing reported GAAP earnings substantially without changing the underlying business at all. When you read a multinational's 10-K, the MD&A often distinguishes "constant-currency" growth from reported growth specifically to strip out this effect.

**Economic exposure.** Even a purely domestic firm can be affected by exchange-rate movements. A US ski resort competes with Mexican beach resorts for vacationing US households. When the dollar appreciates against the peso, Mexico becomes cheaper for US tourists, and the ski resort loses customers. Economic exposure is the longest-running and hardest-to-hedge of the three.

For your equity research project: read the segment reporting and geographic-exposure disclosures in the 10-K. A company with 60% of revenue outside the US is, by definition, materially exposed to currency moves. A company with 5% non-US revenue has limited exposure. The MD&A will usually address currency effects explicitly.

### Reading economic data — FRED and the percentage-change calculation

The single most useful free tool for macro work is **FRED** (Federal Reserve Economic Data), maintained by the Federal Reserve Bank of St. Louis. FRED hosts more than 800,000 economic time series, drawn from the Federal Reserve, Bureau of Labor Statistics, Bureau of Economic Analysis, US Census, and dozens of other sources. Every series has a unique ticker (CPIAUCSL for headline CPI, FEDFUNDS for the federal funds rate, GDP for nominal GDP, GDPC1 for real GDP, UNRATE for the unemployment rate, DGS10 for the 10-year Treasury yield). Series can be displayed graphically, downloaded to Excel or CSV, and combined into custom charts.

For the project, FRED is your macroeconomic data backbone. You can pull a 30-year history of any series in under a minute.

Two operations on a series come up constantly.

**Percentage change.** From one period to the next:

$$\text{\% Change} = \frac{X_2 - X_1}{X_1}$$

Example: Japanese real GDP was 522,594.2 billion yen in Q1 2013 and 527,277.0 billion yen in Q2 2013. Change:

$$\frac{527{,}277.0 - 522{,}594.2}{522{,}594.2} = 0.00896 = 0.896\%$$

That's a quarterly growth rate of about 0.9%, or roughly 3.6% annualized. (Annualizing by multiplying by 4 is a useful approximation; the exact calculation compounds.)

**Index construction.** An **index** rescales a series so a chosen base period equals 100. This makes it easy to compare across series with different absolute levels. CPI for the US in 1970 = 100; in 2020, that same index reads 666.6, meaning the US price level in 2020 was about 6.7 times its 1970 level. Switzerland's CPI rose from 100 to 302.3 over the same span (about 3x); Japan's from 100 to 331.8 (about 3.3x — most of which happened in the 1970s).

For the project: build a small set of FRED charts you reference throughout — federal funds rate, CPI, real GDP growth, unemployment rate, the dollar index (DXY), the 10-year Treasury yield. Update them once a quarter as the project progresses.

### The trade-off (concept 3)

Macro analysis trades **specificity against scope**. A deep dive into one company's customer base, supply chain, and competitive position is irreplaceable for understanding *that company*. Macro work tells you about the weather everyone is operating in — the things that affect every company in the same direction at once. A complete equity research report needs both. Skipping macro produces analysis that is technically tight but blind to the systemic forces that sometimes dominate company-specific factors. Skipping bottom-up work produces macro narratives that don't connect to actual cash flows.

### Worked example — using FRED to answer one question about your company

Suppose your chosen company is a major homebuilder. The macro question is: *how have rising mortgage rates over the last three years affected its business?*

Pull these three FRED series:
- **MORTGAGE30US** — 30-year fixed mortgage rate, weekly.
- **HOUST** — housing starts, monthly.
- **EXHOSLUSM495S** — existing home sales, monthly.

Plot them together over the past five years. You'll see the mortgage rate triple between early 2022 and late 2023. Housing starts and existing home sales both fell — existing home sales fell more, because new homebuilders could offer rate buy-downs that secondary-market sellers could not.

Now compare to your company's segment data from its 10-K. Did its unit volumes track housing starts? Did its average selling price hold up because of a supply shortage in the resale market? Did its margin expand because input costs (lumber, copper) declined as the broader economy slowed?

Three FRED series + the company's 10-K = a real macro-aware analytical chapter in your equity research report. This is exactly the kind of work the project produces by Chapter 18.

### Common misconceptions

- *"You can't predict a recession."* The NBER doesn't predict; it dates. But several real-time indicators (yield-curve inversions, leading indicators, ISM manufacturing index) have track records of preceding recessions, with varying reliability. Calibrated uncertainty, not blind prediction.
- *"FRED data is the truth."* FRED hosts data from primary sources. The data is as good as those sources, and many series are revised after initial release. Treat the most recent data points as preliminary.
- *"Inflation hurts all companies equally."* No — pricing power differs. Companies with strong brands and inelastic demand pass inflation through to customers; companies with commodity-like products absorb it. Analyzing pricing power is part of fundamental analysis.

---

## Synthesis — the macro environment as the analyst's weather

Three concepts, one job. **Interest rates** are the price of money. **Inflation, GDP, and unemployment** are the macro variables that determine what that price should be. **The business cycle, exchange rates, and the data tools** turn macro variables into a usable analytical context.

Underneath every line of a financial statement is a macro environment. The discount rate in a DCF model is built from a risk-free rate, an inflation premium, and a risk premium. The growth assumption in a forecast depends on where the economy sits in its cycle. The currency translation in a multinational's 10-K depends on exchange rate history. An analyst who treats these as background noise produces models that are technically clean and substantively wrong.

For the running project, this chapter equips you to do three things by the end of the book:

1. Read your company's debt footnote and assess its real cost of capital relative to inflation.
2. Read its MD&A's currency commentary and segment data and quantify currency exposure.
3. Pull the FRED series your company is most exposed to and integrate them into the equity research report.

---

## Exercises

### Warm-up

**3.1** Define, in your own words: nominal interest rate, real interest rate, CPI, core CPI, GDP deflator. Which is most relevant for a Fed policy decision?

**3.2** A company has $1 billion of debt at 5% nominal interest. Inflation is 3%. What is the company's real interest cost? In dollars per year, how much of the company's $50 million annual interest expense is "compensating the lender for inflation" vs. "real cost"?

**3.3** Identify the four expenditure categories of GDP. Which is the largest in the United States? Which is the most volatile from quarter to quarter?

### Application

**3.4** Pull the federal funds rate from FRED (ticker FEDFUNDS) for the past 30 years. Plot it on the same chart as the 30-year mortgage rate (MORTGAGE30US). Describe the relationship in two paragraphs — when do they move together, when do they diverge?

**3.5** For a multinational firm of your choice, find its segment reporting in the most recent 10-K. What percentage of revenue comes from outside the firm's home country? What languages and currencies does that imply? What's the firm's stated approach to currency risk?

**3.6** Compute the percentage change in US real GDP for each of the past 8 quarters. Identify any quarters with negative growth. Is the US in expansion or contraction by the rule-of-thumb (two consecutive quarters of declining GDP) definition?

### Synthesis

**3.7** The 2022–2024 disinflation was unusual: inflation came down meaningfully without a sharp rise in unemployment. The simple Phillips curve says this shouldn't happen. Construct two competing explanations — one structural (something about the economy was different this time), one transitory (the disinflation was easier than the simple model predicted because the inflation was driven by supply shocks rather than overheated demand). Which do you find more plausible, and what evidence would distinguish them?

**3.8** For the company you've chosen for your equity research project, write a one-page macro section. Cover: (a) where the US is in the business cycle, (b) the company's currency exposure if any, (c) the company's interest-rate exposure (cost of debt, sensitivity to rate changes), (d) the inflation environment relative to the company's pricing power. This is the macro context that will frame the rest of your report.

### Challenge

**3.9** The "soft landing" debate in 2024–2025 hinged on whether the Fed could bring inflation back to target without a recession. Some economists argued that the long-run cost of letting inflation expectations un-anchor would be larger than the short-run cost of a recession that re-anchored them. Others argued that the inflation surge was largely supply-driven and would resolve without monetary intervention. Read one paper or speech from each camp (the Fed's website and Brookings have reasonable starting points) and write a one-paragraph evaluation of who turned out to be more right, with evidence.

**3.10** Currency hedging is expensive. A multinational firm could hedge most of its currency exposure but typically chooses to hedge only a portion. Explain, using the concepts of transaction, translation, and economic exposure, why fully hedging is not optimal. What considerations determine the right level of hedging? (We'll return to this in Chapter 20; you're constructing intuition now.)

---

## Chapter summary

- An interest rate is the price of money, set in the market for loanable funds. The federal funds rate is the policy lever; everything else floats off it with adjustments for risk and term.
- The **nominal rate** is what's quoted; the **real rate** is the nominal rate minus inflation. Real is what determines economic behavior.
- Inflation has at least four measures: CPI, core CPI, PPI, and the GDP deflator. They answer different questions; CPI is the consumer-facing benchmark.
- **GDP** is total output. **Real** GDP strips out inflation. The four expenditure categories: consumption, investment, government, net exports.
- The **business cycle** has four phases (expansion, peak, recession, trough). Average expansion ~41 months, average recession ~17 months. NBER dates US cycles.
- **Exchange rates** create three exposures: transaction, translation, economic. Multinationals manage all three.
- **FRED** is the analyst's macro database. Percentage change and index construction are basic operations.

---

## What would change my mind

The chapter argues that macro variables — interest rates, inflation, GDP, unemployment, the cycle, exchange rates — are essential context for any serious financial analysis, and that they should be made specific (CPI vs. core, real vs. nominal, U-3 vs. U-6) rather than treated as one-word headlines. The reading would have to revise if (a) macro variables turned out to be uncorrelated with company-level fundamentals over decadal horizons (some research suggests the link is weaker than introductory texts assume, particularly for large diversified firms), or (b) the rise of algorithmic/quant approaches to investing made macro context less important than firm-specific data signals. The first is partial; the second is technical. Neither displaces the chapter's claim, but both qualify it.

## Still puzzling

I am most uncertain about how to teach the relationship between Fed policy and asset prices to a first-time finance student. The transmission channels are real (rates → discount rates → valuations; rates → mortgages → housing → consumption; rates → currency → multinational earnings) but the magnitudes vary cycle to cycle, and the quantitative impact in any given case is hard to predict. The 2020 case (rates collapsed, asset prices soared) was clean. The 2022–2024 case (rates rose 5+ points, equities fell less than expected, real GDP held up) was muddy. I don't have a clean way to make this both honest about the uncertainty and useful for a beginner. The chapter makes the qualitative case and shows where to find the data; the rest is judgment that comes with experience.

---

## Connections forward

- **Chapters 7–9** convert interest rates into the time-value-of-money arithmetic that underlies every valuation in the book.
- **Chapter 10** uses interest rates to price bonds.
- **Chapter 11** uses the discount rate in DCF models.
- **Chapter 14** computes beta — the regression of a stock's returns on the market — which is itself a function of macro environment.
- **Chapter 17** uses the cost of debt and equity to compute WACC, the firm's weighted-average cost of capital.
- **Chapter 20** revisits exchange-rate exposure as a risk-management problem.

---

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

**Irving Fisher** was developed the Fisher equation linking nominal and real interest rates — and the Quantity Theory of Money.

**Run this:**

```
Who is Irving Fisher, and how does their work connect to money and rates we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about their career or ideas.
```

→ Search **"Irving Fisher"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to apply Irving Fisher's framework to a specific finance question.
- Add a constraint: "Answer including criticisms or limits of Irving Fisher's framework."

What changes? What gets better? What gets worse?
