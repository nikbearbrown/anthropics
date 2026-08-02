# Chapter 22 — Inflation

*The slow erosion of money's value — what it actually is, why it matters more than you'd think, and what happens when it gets out of control.*

In July 2008, in Zimbabwe, a loaf of bread cost about 1.6 trillion Zimbabwean dollars. The country was in the middle of one of the worst hyperinflations in modern history. Annual inflation was running at an estimated 89.7 sextillion percent (that's 89,700,000,000,000,000,000,000 percent). Prices doubled, by some estimates, every 24 hours. The Reserve Bank of Zimbabwe issued a 100-trillion-dollar note. People shopped for groceries with wheelbarrows of cash. The currency was eventually abandoned entirely; Zimbabwe started using the U.S. dollar instead.

Most of the time, in most countries, inflation is much milder. The U.S. Consumer Price Index has risen at an average of about 3 percent per year over the past forty years. Some years are higher (the 9.1 percent peak in 2022); some are lower (negative briefly in 2009 during the Great Recession). The U.S. has not experienced anything like Zimbabwe's hyperinflation in over a century, and not even the 1970s peak got close.

But even modest inflation matters. It changes who wins and who loses across the economy. It affects how people invest, save, work, and contract. It is the central focus of monetary policy, which is the subject of Chapter 28. And the question of whether inflation today is the brief consequence of a specific shock or the start of something more sustained is one of the most-watched questions in macroeconomics.

This chapter is about inflation: how it's measured, why it happens, and what it does. By the end you should be able to read CPI data, distinguish nominal from real values, identify who's helped and hurt by unexpected inflation, and recognize the warning signs of high inflation in policy and in the data.

**Learning objectives.** By the end you should be able to: (1) calculate inflation from a price index using the basket method; (2) explain how the CPI is constructed and identify three sources of bias; (3) describe the U.S. inflation pattern over the past 70 years; (4) explain how inflation redistributes wealth between debtors and creditors, and between fixed-income and variable-income recipients; (5) define indexing and identify the major U.S. programs that use it; (6) describe the conditions that produce hyperinflation.

**Prerequisites.** Chapter 19 (nominal vs. real, GDP deflator). Chapter 21 (wages and the labor market).

## Measuring inflation — the basket and the index

Inflation is the rate at which the general price level rises. To measure it, you need a single number that represents the average price level — but average across what?

The standard approach uses a **basket** of goods and services that's representative of typical household spending. The Bureau of Labor Statistics (BLS) constructs the **Consumer Price Index (CPI)** by:

1. Defining the basket — what a typical urban household consumes. Roughly 80,000 prices for ~200 categories (food, housing, transportation, medical care, recreation, etc.) collected each month.
2. Establishing a base period — typically 1982–1984 in the historical U.S. series.
3. Calculating the cost of the basket in each period.
4. Expressing each period's cost as an index number relative to the base (= 100).

A worked example. Suppose the basket is: 12 burgers, 5 movie tickets, 1 month's rent. In 2020, prices: $5 per burger, $10 per movie ticket, $1,200 per month rent. Total basket cost: 12×$5 + 5×$10 + $1,200 = $60 + $50 + $1,200 = $1,310. In 2024, prices have risen: $7 per burger, $13 per movie ticket, $1,500 per month rent. New basket cost: 12×$7 + 5×$13 + $1,500 = $84 + $65 + $1,500 = $1,649. The CPI in 2024, with 2020 as the base, is (1,649 / 1,310) × 100 = 125.9. Inflation from 2020 to 2024 was 25.9 percent.

The annualized rate over 4 years would be (1.259^(1/4) − 1) ≈ 5.9 percent per year. This compares to actual U.S. CPI inflation 2020–2024 of about 4 percent annually, average — close enough that the worked example is in the right neighborhood.

## Biases in the CPI

The CPI is the most important inflation measure, but it has known biases. Three matter most.

**Substitution bias.** When the price of one good rises, consumers substitute toward cheaper alternatives. The fixed-basket method doesn't capture this — it assumes consumers keep buying the same basket even at higher prices for some items. A "chained" CPI updates the basket regularly to reflect actual substitution; the standard CPI doesn't, and so it slightly overstates the true cost-of-living change.

**Quality-change bias.** A 2024 smartphone is dramatically more capable than a 1990 cellphone, but in the basket they may both appear as "a phone." If the price index doesn't adjust for quality improvement, the price level appears to rise faster than the true cost-of-living index. The BLS uses **hedonic regression** to adjust for quality changes in some categories, with mixed success.

**New-goods bias.** When new products enter the market (smartphones in 2007, e-bikes in 2015, generative AI services in 2023), they're not in the basket initially. By the time they're added, much of the consumer welfare gain from their introduction has already been captured by buyers, and the index misses it.

The combined effect of these biases is that the standard U.S. CPI may overstate true inflation by a percentage point or two per year. The Federal Reserve's preferred inflation measure, the **PCE Price Index** (Personal Consumption Expenditure Price Index), uses chain-weighting and updates more frequently; it typically reads about 0.3 percent lower than the CPI. The BLS also publishes the **chained CPI**, which is closer to the PCE.

The biases matter for policy. Social Security cost-of-living adjustments use CPI. Income tax brackets are CPI-indexed. If CPI is overstated, COLA payments and bracket adjustments are larger than the true cost of living change requires, with substantial budgetary implications over decades.

## The historical pattern

U.S. inflation since 1950:

- **1950s–1960s.** Generally low and stable, in the 1–3 percent range.
- **1970s.** A burst of high inflation — peak around 14 percent in 1980. Triggered by oil shocks (1973, 1979) and accommodated by a Federal Reserve that hesitated to raise rates aggressively until Paul Volcker took over in 1979.
- **1980s–1990s.** Volcker's aggressive monetary tightening crushed inflation by the mid-1980s. Inflation settled into a 2–4 percent range that persisted for two decades.
- **2000s–2010s.** Even lower — inflation typically below 2.5 percent. Sometimes deflation worries (2009 briefly, 2015).
- **2021–2024.** A burst of inflation following COVID supply disruptions and substantial fiscal stimulus. Peak around 9 percent in mid-2022. Returned to 3–4 percent range by 2024.

The 1970s remain the modern reference case for high U.S. inflation. The 2021–2024 episode was much milder by comparison, and was largely brought back down by aggressive Federal Reserve interest-rate hikes from 2022 onward.

Internationally, inflation patterns vary widely. Some emerging-market countries have struggled with chronically high inflation (Argentina, Turkey, Venezuela). The euro area has typically been close to 2 percent but with periods of much higher (during the post-COVID surge) and much lower inflation. Japan has experienced sustained near-zero or negative inflation for most of the 2000s and 2010s.

## What inflation does — distributional effects

Inflation doesn't affect everyone equally. Some people benefit; some lose. The pattern depends on who has fixed obligations vs. flexible obligations, fixed income vs. flexible income.

**Debtors typically benefit from unexpected inflation.** If you borrow $100,000 at 4 percent interest, expecting 2 percent inflation, your real interest rate is 2 percent. If actual inflation turns out to be 6 percent, your real interest rate is −2 percent — you're paying back dollars worth less than the dollars you borrowed.

**Creditors typically lose.** The lender expected to be repaid in dollars worth what they expected. Higher actual inflation means they get back dollars worth less.

**Fixed-income recipients lose.** If your pension or your fixed annuity pays $5,000/month and inflation rises, your purchasing power falls.

**Workers with strong bargaining power (and indexed contracts) gain.** Wages can be re-negotiated upward. Some union contracts have COLA provisions.

**Workers with weak bargaining power lose.** Their wages may rise more slowly than prices.

These distributional effects are the main reason high inflation creates political pressure. The losers are loud (retirees, savers, fixed-income workers); the gainers are quieter (mortgaged homeowners, indexed Social Security recipients, indebted businesses). Politicians get heat for inflation that they often can't easily fix in the short run.

## Why high inflation is bad even when it's "fair"

Even setting aside redistribution, high inflation has real economic costs.

**Menu costs.** Firms have to constantly update prices, reprint catalogs, retag products. Small in any individual transaction but substantial in aggregate.

**Shoe leather costs.** People spend more time and effort minimizing their cash holdings (which are losing value rapidly) — running to the bank, holding more in non-cash assets, etc.

**Distortions in relative prices.** When all prices are changing rapidly, it's hard to tell which prices are rising for fundamental reasons (supply and demand for that good) versus which are just rising with general inflation. Buyers and sellers make worse decisions because the price signal is degraded.

**Tax distortions.** The tax system uses nominal values. Capital gains tax applies to nominal gains, not real gains. Bracket creep pushes people into higher tax brackets through nominal raises that don't reflect real income increases.

**Investment uncertainty.** Investments require comparing future returns to current costs. High and variable inflation makes this comparison harder. Long-term investment falls.

These costs are why central banks target low and stable inflation — typically 2 percent. Lower would risk deflation, which has its own problems. Higher would impose the costs above.

## Indexing — a partial fix

To reduce the harm from inflation, many contracts and government programs are **indexed** — they automatically adjust for inflation.

Major examples:

- **Social Security benefits.** Indexed to CPI annually.
- **Federal income tax brackets.** Adjusted for CPI annually.
- **Some union wage contracts.** Have explicit cost-of-living adjustments.
- **Treasury Inflation-Protected Securities (TIPS).** Bonds whose principal adjusts with CPI.
- **Some adjustable-rate mortgages.** Tied to nominal interest rates, which include an inflation component.

Indexing softens the effects of inflation but doesn't eliminate them. The index itself may have biases (CPI biases discussed above). Some contracts can't be easily indexed (long-term fixed-rate mortgages, multi-decade pension obligations). And indexing transfers the inflation cost from one party to another rather than eliminating it.

## Hyperinflation and how it happens

Most high-inflation episodes are bad but not catastrophic. **Hyperinflation** — typically defined as inflation exceeding 50 percent per month — is a different phenomenon.

The conventional definition (Cagan, 1956): inflation above 50 percent per month, sustained for at least several months. At 50 percent monthly, prices double every couple of months and rise nearly 130-fold over a year.

Major historical hyperinflations:
- **Germany, 1922–1923.** Inflation exceeded 20,000 percent monthly at peak. Prices doubled every few hours. Workers were paid twice a day so they could spend before money became worthless. The hyperinflation contributed to political instability that eventually empowered the Nazi party.
- **Hungary, 1945–1946.** The worst on record. Prices doubled every 15 hours. Inflation peaked at 41.9 quadrillion percent monthly.
- **Zimbabwe, 2007–2008.** Prices doubled approximately daily.
- **Venezuela, 2017–2019.** Inflation exceeded 1 million percent annually.

The mechanism is consistent across cases. The government runs large fiscal deficits. It can't fund them through normal taxes or borrowing. The central bank prints money to fund the deficit. The money supply grows much faster than real output. Prices rise to absorb the new money. People expect more inflation and adjust contracts accordingly. The inflation accelerates.

Once expectations are set on rapid inflation, breaking the cycle requires restoring fiscal discipline and a credible commitment to monetary stability. Both are politically costly and require institutional changes that often take years.

The lesson for normal monetary policy: protect the central bank's independence, maintain a credible inflation target, prevent the kind of fiscal-monetary fusion that produces hyperinflation. The Federal Reserve, despite a colorful political history, has maintained these conditions. The U.S. has not experienced hyperinflation since the Confederate currency collapse during the Civil War.

## Synthesis

Pull back. Inflation is the rate at which the general price level rises. CPI is the standard measure, with known biases that probably overstate true inflation by a percentage point or so. Inflation in the U.S. has averaged 3 percent over the past forty years, with episodes of higher and lower. It redistributes wealth between debtors and creditors, between fixed and variable income recipients. Beyond the redistribution, high inflation imposes real costs on the economy through menu costs, distorted prices, and investment uncertainty. Indexing can soften some of the harm but not eliminate it.

Hyperinflation is a different phenomenon — usually the result of fiscal-monetary fusion, where governments fund deficits by printing money. When it happens, it's catastrophic. Modern advanced-economy central banks are designed to prevent it.

The 2021–2024 U.S. inflation episode was significant — the largest sustained inflation since the early 1980s — but it was nothing like Zimbabwe or even like the U.S. 1970s. The Fed responded aggressively with rate hikes, inflation came back down, and the lessons of the 1980s (decisive monetary action restores price stability quickly) appear to have been remembered. The next chapter, on international trade and capital flows, brings in the open-economy dimension; chapters 27 and 28 cover money and banking and the monetary policy that does the inflation-fighting work.

## LLM Exercises

**Exercise 1 — Build a basket-based inflation index.** Tell an LLM to construct a hypothetical basket of consumer goods (specify five items with quantities) and to calculate what the index would be for two different sets of prices. Compute the inflation rate. Verify the math.

**Exercise 2 — Diagnose a CPI bias.** Tell an LLM the situation: smartphone prices have stayed roughly constant for a decade, but smartphone capabilities have improved enormously over the same period. Ask: how does the CPI handle this? Does it overstate or understate the true cost-of-living change? Push the LLM to be specific about the hedonic-adjustment process and its limits.

**Exercise 3 — Trace the redistributional effects of unexpected inflation.** Tell an LLM about three hypothetical households: one renting an apartment with a long-term lease, one with a 30-year fixed-rate mortgage, one living on Social Security. Ask: what happens to each household's real situation if inflation jumps from 2% to 6% unexpectedly? Push for specifics.

**Exercise 4 — Hyperinflation analysis.** Pick a historical hyperinflation case (Weimar Germany, Hungary 1945, Zimbabwe 2008, Venezuela 2018) and ask an LLM to walk through the chain: fiscal pressure → monetary financing → expectations adjustment → accelerating inflation. Identify the institutional features that would have prevented it.

**Exercise 5 — Predict the next inflation episode.** Ask an LLM to identify the conditions that would precede the next major U.S. inflation episode. The answer should engage with fiscal-monetary tensions, supply-side shocks, anchoring of expectations, and Federal Reserve credibility. Push back on any analysis that ignores the role of the Fed.

## What comes next

Chapter 23 — International Trade and Capital Flows extends the macroeconomic framework to the open economy: imports, exports, the current account, capital flows. Chapter 24 — The Aggregate Demand–Aggregate Supply Model brings together GDP, unemployment, and inflation in a single framework. Chapters 25 and 26 cover the Keynesian and neoclassical perspectives on how the macroeconomy actually works.

**What would change my mind.** The case that the CPI overstates true inflation rests on assumptions about how to measure quality improvement and substitution behavior — both of which are debatable. If new evidence showed that the actual quality improvement in the past several decades has been smaller than CPI methods assume, the bias would be smaller or even reversed. The methodological debate is technical but consequential for trillion-dollar programs that index off the CPI.

**Still puzzling.** I do not have a clean account of why some hyperinflations are eventually resolved (Argentina at various points, Brazil 1990s) while others persist for decades (Venezuela). The institutional response — currency reform, fiscal restraint, central bank independence — looks similar in successful and unsuccessful cases. The difference seems to be in the political will to sustain the response, which is itself shaped by factors I don't have a model for.

*Byline: Nik Bear Brown.*
---

## LLM Exercise — Chapter 22: Inflation (Policy Brief Project)

**Project:** Policy Brief.
**What you're building this chapter:** the inflation analysis — how the policy affects measured inflation, distributional effects across debtors/creditors and fixed-vs-variable income, indexing solutions.
**Tool:** **Claude Project** "Policy Brief" — appends a section.

---

**The Prompt:**

```
Chapter 22 of my Policy Brief project. Prior sections in this Claude
Project. Chapter 22 taught: inflation measurement (CPI = basket of
goods, weighted; PCE; GDP deflator) and the biases (substitution
bias, quality-improvement bias, new-goods bias — CPI overstates
true inflation by ~0.5 to 1 pp/yr); the distributional effects
(unexpected inflation transfers wealth from creditors to debtors;
hurts those on fixed nominal income; helps those with assets that
appreciate with inflation); why high inflation is bad even when
it's "fair" (menu costs, price-distortion costs, planning costs);
indexing as a partial fix; hyperinflation mechanics.

Write the brief's "Inflation Analysis" section in 300–500 words.

1. **The direct inflation effect.** Does your policy raise or
   lower measured inflation? Magnitude in basis points or
   percentage points. Carbon tax: raises measured inflation in
   the short run (passes through to fuel and transport prices).
   Antitrust: lowers measured inflation if it reduces market-
   power-driven pricing. Minimum wage: small upward effect on
   prices in low-wage-input goods.

2. **The distributional effect of any inflation surprise.** If
   the policy creates a one-time price-level jump (carbon tax,
   sugar tax, tariff), the surprise transfers wealth: nominal-
   creditor losers, nominal-debtor winners. Fixed-income retirees
   take a real cut. Indexed-income groups (Social Security
   recipients, union contracts with COLAs) are protected. Name
   who's hit and how the policy could be designed to protect
   the most-exposed group.

3. **The expectations channel.** A policy that's expected to be
   inflationary often becomes self-fulfilling — wage and price
   setters bake in the expectation. The brief should name whether
   the policy's inflation effect is one-time (price level shift)
   or persistent (rate of inflation shift), because the
   monetary-policy response in Ch 28 will depend on the answer.

End with one sentence on whether the policy's inflation effect
is small enough to ignore, large enough to require monetary-
policy response, or large enough to constitute a public concern
in its own right.
```

---

**What this produces:** A 300–500 word section on the inflation effect, distributional consequences, and the one-time-vs-persistent distinction. The monetary-policy implication carries into Ch 28.

**How to adapt this prompt:**

- *For your own project:* Carbon-tax students: this is central — the price-level pass-through is the standard regressive critique. UBI students: macro-significant if funded by deficit; smaller if funded by tax. Tariff students: directly inflationary at the consumer level.
- *For ChatGPT / Gemini:* Works as written.
- *For Claude Code:* If you want to model the price pass-through across CPI components, Claude Code can produce a working calculator.
- *For a Claude Project:* Append.

**Connection to previous chapters:** Ch 5's elasticity work + Ch 22's inflation analysis together describe how the policy moves prices in the short and long run.

**Preview of next chapter:** Chapter 23 turns to international trade and capital flows — the savings-investment identity, why trade deficits aren't always bad, when they become problems. If your policy has any international dimension (most do at the margin), this is where it gets developed.


---

## AI Wayback Machine

**Irving Fisher** was developed modern theory of interest rates and the quantity theory of money — and famously declared stocks "permanently high plateau" days before the 1929 crash.

**Run this:**

```
Who is Irving Fisher, and how does their work connect to inflation we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about their career or ideas.
```

→ Search **"Irving Fisher"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to apply Irving Fisher's framework to a current economic question.
- Add a constraint: "Answer including criticisms or limits of Irving Fisher's framework."

What changes? What gets better? What gets worse?
