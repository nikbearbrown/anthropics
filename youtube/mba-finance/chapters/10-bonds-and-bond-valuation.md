# Chapter 10 — Bonds and Bond Valuation
*A loan with a price tag — and why that price moves opposite to what most people expect.*

---

## The puzzle of a bond trading above par

In March 2021, 3M Company had a corporate bond outstanding with these specs: $1,000 par value, 2.25% coupon rate, maturing September 2026, currently trading at $1,051.20.

The bond would pay $22.50 per year and return exactly $1,000 at maturity. 3M would never pay more than $1,000. Yet investors were paying $1,051.20 for it. Why would anyone pay $51 more than they'll ever get back?

Because interest rates had fallen. When 3M issued the bond, investors demanded 2.25% annually for lending to A+ corporate paper of that maturity. By March 2021, market yields had dropped to about 1.24% — new bonds being issued that month offered only 1.24%. The old 3M bond, locked in at 2.25%, was suddenly more attractive than anything new. Investors bid its price up. They kept bidding until the effective yield on the old bond — accounting for the fact that you'd pay $1,051.20 and still only receive $1,000 at maturity — dropped to match the new market rate of 1.24%. That's where it stopped: $1,051.20.

This is the central fact about bonds: **price and yield move in opposite directions.** When rates fall, bond prices rise. When rates rise, bond prices fall. The mechanism is exactly the present-value arithmetic from Chapters 7–9, applied to a specific kind of cash flow stream. That's the whole chapter.

---

## What a bond is

A bond is a loan with explicit terms. The issuer borrows money from investors and promises to pay it back — with regular interest payments — on a known schedule. The terms are fixed in a legal contract called the **indenture**.

Five terms do most of the work.

**Par value** (also called face value): the principal the issuer promises to repay at maturity. Standard corporate bonds use $1,000.

**Coupon rate**: the annual interest rate the issuer pays on par value. A 5% coupon on a $1,000 bond pays $50 per year. This rate is fixed at issuance and never changes for the life of a fixed-rate bond.

**Coupon payment**: the actual dollar amount paid each period. For US corporate bonds, coupons are paid semi-annually — a 5% coupon means $25 every six months.

**Maturity date**: when the issuer pays back the par value and the bond ceases to exist. Maturities range from a few months (Treasury bills) to 30 years (long corporate and Treasury bonds).

**Yield to maturity (YTM)**: the discount rate that makes the present value of all the bond's cash flows equal to its current price. This is the key concept. The coupon rate is fixed by the issuer at issuance. The YTM is set by the market and changes every day.

The crucial distinction: **coupon rate is fixed; YTM varies.** When the market wants more (or less) yield than the coupon provides, the bond's *price* adjusts until the effective yield matches. The coupon doesn't change. The price does.

<!-- → [TABLE: Bond vocabulary quick-reference — columns: Term, Definition, Fixed or variable, Example — rows: par value, coupon rate, coupon payment, maturity, YTM — student should be able to distinguish the issuer-set terms from the market-set terms at a glance] -->

### Bond types worth knowing

The basic form is a fixed-rate coupon bond. Variations exist because different issuers and investors need different structures.

**Treasury securities** are issued by the US federal government, considered default-risk-free in nominal terms. T-bills (under one year, sold at discount, no coupons), Treasury notes (2–10 years, semi-annual coupons), Treasury bonds (20–30 years, semi-annual coupons).

**Corporate bonds** are issued by companies. Default risk varies from AAA-rated multinationals to deeply distressed firms. Corporate bond yields include a **credit spread** over equivalent-maturity Treasury yields — the premium the market demands for taking on default risk.

**Zero-coupon bonds** pay no coupons at all. Issued at a deep discount and redeemed at par. Entire return comes from price appreciation. Useful when you need a specific lump sum at a specific future date.

**Callable bonds** give the issuer the right to redeem early, typically when rates fall and the issuer can refinance cheaper. The investor bears the reinvestment risk — the bond disappears right when you'd most want to hold it. Issuers pay slightly higher coupons to compensate.

**Convertible bonds** can be converted into a fixed number of the issuer's common shares at the holder's option. Hybrid instrument priced accordingly.

For the equity research project: your chosen company's 10-K debt footnote lists all outstanding bonds with par values, coupon rates, maturities, and special features. Each is a window into the firm's capital structure and credit quality.

---

## The pricing formula

Pricing a bond is present value of a mixed cash flow stream — exactly the Chapter 9 toolkit. The stream has two parts: the coupon payments (an annuity) and the par repayment at maturity (a single payment).

For an annual-coupon bond with par value $F$, coupon payment $C$, $n$ years to maturity, and yield to maturity $y$:

$$P = C \times \frac{1 - (1+y)^{-n}}{y} + \frac{F}{(1+y)^n}$$

The first term is the present value of the coupon stream. The second is the present value of getting $F$ back at maturity. Three things determine the price: the coupon, the YTM, and the time to maturity. That's all.

<!-- → [DIAGRAM: Timeline showing a bond's cash flow structure — horizontal axis is time from 0 to maturity; coupon payments shown as uniform downward arrows at each period; single larger arrow at maturity representing par repayment; annotate which part of the pricing formula corresponds to each; student should see the annuity + single-payment structure visually] -->

### Working through the 3M bond

Take the chapter's opening puzzle. 3M bond: $1,000 par, 2.25% annual coupon, 5.5 years to maturity, market YTM of 1.24%.

Annual coupon: $1,000 × 0.0225 = $22.50.

PV of coupons:
$$22.50 \times \frac{1 - (1.0124)^{-5.5}}{0.0124} = 22.50 \times 5.281 = \$118.83$$

PV of par:
$$\frac{1{,}000}{(1.0124)^{5.5}} = \$934.44$$

Bond price: $118.83 + $934.44 = **$1,053.27**.

The actual market price was $1,051.20 — we're within 0.2%, with the gap explained by precise day-count conventions and accrued interest. The formula works.

### Semi-annual adjustment

US corporate and Treasury bonds pay coupons twice a year. Adjust by doubling the number of periods ($2n$), halving the periodic rate ($y/2$), and halving the coupon payment ($C/2$).

For a 15-year bond, 4% annual coupon, $1,000 par, 5% YTM:

$$P = 20 \times \frac{1 - (1.025)^{-30}}{0.025} + \frac{1{,}000}{(1.025)^{30}}$$

$$= 20 \times 20.93 + 476.74 = 418.66 + 476.74 = \$895.40$$

Discount bond: 4% coupon below 5% YTM, so price below par. The arithmetic confirms what intuition predicts.

### The premium-discount relationship

The pattern, stated cleanly:

- Coupon rate > YTM → coupons more attractive than alternatives → price bid *up* → **premium** (price > par)
- Coupon rate < YTM → coupons less attractive → price pushed *down* → **discount** (price < par)
- Coupon rate = YTM → price = par exactly

This is not a coincidence. It's definitional. YTM is the rate that equates price to the present value of the bond's cash flows. If the coupon rate matches the YTM, the discounting produces exactly par value. If the coupon is higher, discounting at the lower YTM produces a number above par.

<!-- → [TABLE: Three-column comparison of premium, discount, and par bonds — columns: Condition, Coupon vs. YTM, Price vs. Par, Intuition — rows for each bond type; student should be able to classify any bond by knowing only the coupon rate and YTM without doing arithmetic] -->

### Solving backwards: finding YTM from price

Given a bond's price, YTM is the discount rate that solves the pricing equation. There's no closed form — it requires iteration, a financial calculator, or Excel's `=RATE()` function.

A bond at $675, $1,000 par, 3.5% annual coupon ($35/year), 12 years to maturity. In Excel: `=RATE(12, 35, -675, 1000)` → YTM ≈ 7.76%.

The intuition: the bond is at a deep discount. You pay $675 and receive $35/year plus $1,000 at maturity. The $325 gap between your cost and the par repayment is additional return on top of the coupons. Together they produce 7.76% annually — far above the 3.5% coupon rate. The coupon understates the return whenever you buy below par.

↳ **Dig Deeper — The 2022–2024 yield curve inversion**

*The US Treasury yield curve inverted sharply in mid-2022 as the Fed began its tightening cycle. Historically, every yield curve inversion since the 1960s had been followed by a recession within 6–24 months. The 2022 inversion became the longest-sustained in modern history without immediately producing a recession.*

**Prompt:**
> Walk through the chronology of the 2022–2024 yield curve inversion: when it began, how deep it got, when it un-inverted, and what happened to the economy across that period. Then summarize the academic explanations for why this inversion didn't follow the historical pattern (post-pandemic distortions, fiscal policy, supply-chain disinflation). What's your reading: was 2022–2024 a one-time anomaly, or has the yield curve as a recession indicator structurally weakened?

**What to do with the output:** Save it. Yield curve interpretation appears throughout your equity research project; understanding the limits of historical patterns matters.

---

## What can go wrong: bond risks

Bonds are usually framed as "safe." Compared to equities, they're more predictable. But bonds carry several distinct risks, and each one dominates in different conditions.

**Interest rate risk** is the risk that rates rise after you buy a bond, pushing the bond's price down. This is the central risk for fixed-rate bonds. The 2022 bond market lost about 13% in a year as the Fed raised rates rapidly — the worst calendar-year return on the Bloomberg US Aggregate Index in modern history. Long-maturity bonds and low-coupon bonds are the most sensitive.

The standard measure of this sensitivity is **duration** — roughly, the percentage price decline for a 1-percentage-point rise in yields. A bond with duration of 8 falls about 8% if yields rise 1 point. Long bonds have higher duration than short bonds; zero-coupon bonds have the highest duration of all (duration equals maturity for a zero, since all the cash flow is at the end).

<!-- → [CHART: Bar chart comparing approximate duration across four bond types — 2-year Treasury note, 10-year Treasury note, 30-year Treasury bond, 30-year zero-coupon bond — all at 5% YTM; student should see that duration is always less than maturity for coupon bonds and equals maturity for zeros, and that the 30-year zero is dramatically more rate-sensitive than the 30-year coupon bond] -->

**Default risk** is the risk the issuer doesn't pay. Treasuries are treated as default-risk-free in nominal terms. Corporate bonds vary enormously — AAA-rated industrials are rarely in danger; CCC-rated junk bonds default at double-digit annual rates in recessions.

**Liquidity risk** is the risk you can't sell without taking a price hit. The Treasury market is extraordinarily liquid. Small-issue corporate bonds may not trade for days. In stressed markets — 2008, March 2020 — even normally-liquid instruments seized up.

**Reinvestment risk** is subtler. Standard YTM calculations assume you reinvest coupons at the same YTM for the life of the bond. In practice, you reinvest coupons at whatever rate prevails when they arrive. If rates fall after purchase, realized return is below the initial YTM.

**Call risk** applies to callable bonds. The issuer redeems early when rates fall — exactly when you'd prefer to keep earning the above-market coupon. The investor bears the cost; the higher coupon at issuance is the compensation.

### Bond ratings

Rating agencies — S&P, Moody's, Fitch — assign letter grades based on their assessment of default probability.

Using S&P notation: **AAA, AA, A, BBB** are investment-grade; **BB, B, CCC, CC, C** are speculative-grade ("junk" or "high-yield"); **D** is default. The line between BBB and BB — investment-grade versus junk — is a hard institutional boundary. Many pension funds and insurance companies cannot hold below-investment-grade paper by mandate.

Two important caveats. Ratings are opinions, not guarantees. Enron was investment-grade until two months before bankruptcy. Lehman Brothers was rated A two days before it collapsed. Rating agencies are paid by the issuers they rate, which creates a structural incentive problem that the 2008 mortgage-rating debacle made visible to everyone.

For an analyst, ratings are a starting point, not a conclusion. A serious credit view reads the financial statements directly — TIE ratio (Chapter 6), free cash flow, debt-to-equity, off-balance-sheet obligations — and compares against the rating agency's narrative.

<!-- → [TABLE: Bond rating scale — columns: S&P rating, Moody's equivalent, Category, Typical yield spread over Treasuries (rough range), Historical default rate — rows for each major rating tier from AAA to D; student should be able to locate any bond in the spectrum and have a rough intuition for its credit spread] -->

---

## The yield curve

Plot yields on the y-axis and time-to-maturity on the x-axis and you have a **yield curve**. Its shape carries economic information that analysts track closely.

**Normal curve** — upward-sloping. Long yields exceed short yields. This is the typical shape during expansions. It reflects a term premium: investors demand more yield for locking money up longer, both for duration risk and for inflation uncertainty.

**Inverted curve** — short yields exceed long yields. Unusual. Historically associated with recessions. The mechanism: investors expect the Fed to cut short rates in the future (in response to a slowdown), so they're willing to accept lower long yields to lock in current rates. Every US recession since the 1960s was preceded by an inversion — though the 2022–2024 episode showed the relationship is probabilistic, not mechanical.

**Flat curve** — short and long rates similar. Often a transitional state, or the result of unconventional monetary policy compressing long rates (quantitative easing in the 2010s).

For the equity research project: look up the current Treasury yield curve using FRED (tickers DGS3MO, DGS2, DGS5, DGS10, DGS30). Note the shape. Then find your company's outstanding corporate bond yields and subtract the equivalent-maturity Treasury yield. The difference is the **credit spread** — what the market charges the firm for default risk.

A widening spread means the market is growing more concerned about the firm. A narrowing spread means it's less concerned. The bond market's credit view and the equity market's view often diverge, and when they do, it's worth asking which is right.

<!-- → [CHART: Line chart showing a hypothetical investment-grade corporate bond's credit spread (basis points over 10-year Treasury) over a 5-year period, with shaded band showing typical BBB spread range (100–200 bps) and annotations marking a recession-period widening spike and a post-recession tightening; student should see spread as a time-varying signal of market credit concern, not a fixed number] -->

<!-- → [CHART: Yield curve showing three shapes — normal, inverted, and flat — on a single chart with maturity on the x-axis (3mo, 2yr, 5yr, 10yr, 30yr) and yield on the y-axis; annotate the 2022 inversion and the historical recession-prediction association; student should be able to identify the shape of any given curve and state what it implies] -->

↳ **Dig Deeper — Duration as a sensitivity measure**

*Duration measures how much a bond's price changes for a 1-percentage-point change in yields. The math comes from a Taylor-series approximation of the bond pricing formula.*

**Prompt:**
> Derive the relationship between Macaulay duration and modified duration. Then compute modified duration for: (a) a 5-year zero-coupon bond at 5% YTM, (b) a 10-year 5%-coupon bond at 5% YTM, (c) a 30-year 4%-coupon bond at 5% YTM. Show the math. Which has the highest interest-rate sensitivity, and why? Then briefly explain convexity — what duration alone misses.

**What to do with the output:** Save it. Duration is intermediate-finance content; the qualitative version in this chapter is enough for the project, but the math is worth seeing.

---

## Bonds as the simplest valuation problem

Bonds are the cleanest test of the TVM machinery. Cash flows are contractual: coupon dates, coupon amounts, maturity date, par value. Given a discount rate, the price is mechanical arithmetic.

What makes bonds non-trivial is that the discount rate — the YTM — is what the market sets, and the market changes its mind constantly. The same bond is worth different amounts in different rate environments. The rate environment depends on macro factors the issuer cannot control. A bond's price is, in that sense, out of the issuer's hands the moment after issuance.

Chapter 11 takes the same machinery and applies it to stocks — a harder problem because cash flows are uncertain rather than contractual. Chapter 14 returns to discount rates via CAPM. Chapter 17 uses bond yields as an input to the firm's WACC.

---

## What would change my mind

The chapter argues that bond prices are determined by present-value arithmetic and that YTM is the right market-set discount rate. The reading would have to revise if bonds consistently traded away from their PV-of-cash-flows values for extended periods — they do temporarily in stressed markets, but deviations are usually short-lived. The 2008 mortgage-rating debacle is a real caveat on ratings: the chapter argues ratings are a useful starting point, not a guarantee, and the history supports that qualifier more than it does the rating agencies.

## Still puzzling

YTM-as-return-measure is cleaner in theory than in practice. The calculation assumes coupons are reinvested at the same YTM for the bond's entire life. In reality, coupons arrive at quarterly or semi-annual intervals and are reinvested at whatever rate exists then — which can differ from the initial YTM by hundreds of basis points over a long horizon. The realized return on a long bond can differ materially from its initial YTM, and standard finance treatment papers over this with an assumption investors know isn't true. For retirement-portfolio modeling and liability-matching, the gap matters, and the field has better tools (immunization, duration-matching) that this chapter gestures toward but doesn't build.

---

## Connections forward

- **Chapter 11** applies similar PV machinery to stocks, where cash flows are uncertain.
- **Chapter 12** examines historical bond and equity returns.
- **Chapter 14** computes beta, connecting bond yields and equity risk premia via CAPM.
- **Chapter 17** uses the firm's bond yields to compute cost of debt as an input to WACC.
- **Chapter 20** revisits interest-rate risk as a risk-management problem.

---

## Exercises

### Warm-up

**10.1** Define the following in your own words: par value, coupon rate, coupon payment, maturity date, yield to maturity. For each, state whether it is fixed at issuance or set by the market.

**10.2** A bond has a coupon rate of 4% and is currently trading at a YTM of 6%. Without doing any arithmetic, state whether the bond is trading at a premium, at a discount, or at par — and explain the mechanism in one sentence.

**10.3** State the inverse relationship between bond prices and interest rates. Trace through the mechanism using the 3M bond from the chapter opening: why did falling rates cause the price to rise above par?

### Application

**10.4** Price each of the following bonds (assume annual coupons unless specified). Show the formula setup and numerical result for each.

(a) $1,000 par, 6% coupon, 10 years to maturity, YTM = 8%. Premium or discount?
(b) $1,000 par, 5% coupon, 8 years to maturity, YTM = 5%. Premium, discount, or par?
(c) $1,000 par, 3% semi-annual coupon (so 6% annual), 15 years to maturity, YTM = 4% annually (2% per period).

**10.5** A bond currently trades at $820. It has $1,000 par value, pays a $40 annual coupon, and matures in 10 years.

(a) Is this a premium or discount bond?
(b) Use Excel's `=RATE(10, 40, -820, 1000)` to find the YTM. Is the YTM above or below the coupon rate? Does that match your answer to (a)?
(c) Explain in one sentence why the YTM exceeds the coupon rate in this case.

**10.6** Look up the current 10-year US Treasury yield on FRED (ticker DGS10). Then find one investment-grade corporate bond for a company you know (use Yahoo Finance's bond screener or FINRA TRACE). Compute the credit spread. Does the spread seem consistent with the bond's rating category?

### Synthesis

**10.7** A bond is priced at $950, has $1,000 par, a 4% annual coupon, and 20 years to maturity. Interest rates then rise by 2 percentage points across all maturities.

(a) Compute the new bond price at the new YTM (hint: first find the original YTM from the $950 price, then add 2 percentage points).
(b) By what dollar amount and percentage did the price fall?
(c) How would the price change have been different if the bond had only 5 years to maturity instead of 20? Compute it. What does the comparison tell you about duration?

**10.8** A pension fund holds a portfolio of long-dated Treasury bonds. Interest rates rise sharply. Explain in two paragraphs: (a) what happens to the fund's portfolio value, and (b) why a pension fund — which has long-dated liabilities — might actually be partially hedged against this risk rather than fully exposed.

### Challenge

**10.9** A callable corporate bond has a 7% coupon, $1,000 par, 25 years to final maturity, and a 5-year call protection period. The call price is $1,050. Interest rates are currently 7% (so the bond trades near par).

(a) If rates fall to 4% after five years, would the issuer call the bond? Why?
(b) As a bondholder, what return did you earn if the bond is called at year 5 versus held to maturity?
(c) Why would a rational investor buy a callable bond at all? What compensation do they receive?

**10.10** Using FRED, build a chart of the 2-year Treasury yield minus the 10-year Treasury yield (the "2-10 spread," ticker T10Y2Y) over the past 30 years. Mark every period where the spread went negative (inversion). For each inversion, note whether a recession followed within 18 months (use NBER recession dating). Based on your chart, what is your assessment of the yield curve as a probabilistic recession indicator? Does the 2022–2024 episode change your view, or is it consistent with the curve being probabilistic rather than deterministic?

---

## LLM Exercise — Chapter 10: Price Your Company's Bond

**Project:** Equity Research Report on a Chosen Public Company
**What you're building this chapter:** Price one of your company's outstanding bonds using the bond pricing formula, and assess what its yield says about the firm's credit.
**Tool:** Claude chat or Project. You'll need bond data from the 10-K's debt footnote and a public bond data source (FINRA's TRACE, Bloomberg, or Yahoo Finance bond search).

### The Prompt

```
For [your company], identify one of its outstanding corporate bonds (from the 10-K's debt footnote — pick a bond with semiannual coupons and at least 3 years to maturity).

For your chosen bond, gather:
- Par value (typically $1,000)
- Coupon rate (annual, %)
- Maturity date
- Current credit rating (S&P, Moody's, or Fitch)
- Current market price (as % of par; from FINRA TRACE, Yahoo Finance bond search, or Bloomberg)

Then:

1. **Compute the YTM** using the bond pricing formula:
   P = C × [1 - (1+y)^-n] / y + F / (1+y)^n
   where you have P, C, n, F and need to solve for y.
   Use Excel's =RATE() function or iterate. Show your inputs and result.

2. **Determine premium or discount** — Is the bond trading above or below par? What does that imply about how its coupon rate compares to current market yields for similar bonds?

3. **Compute the credit spread** — Subtract the YTM of the same-maturity Treasury (use the appropriate FRED series — DGS5, DGS10, or DGS20 — depending on bond maturity).

4. **Interpret the spread** — How does this spread compare to typical spreads for the bond's rating? (Investment-grade BBB-rated bonds typically yield 100–200 basis points over Treasuries; investment-grade A-rated, 60–150 bps.)

5. **Compute approximate duration** — Use the rough rule that for a 10-year coupon bond, duration is roughly 7–8 years. State the implied price sensitivity to a 1% rate change.

Show all calculations. Cite the source of each input.
```

### What this produces

A 1–2 page bond-pricing analysis. Adds to the report's debt analysis section. Cross-checks the firm's cost of debt that you'll use in the WACC computation in Chapter 17.

### How to adapt this prompt

- *For your own company:* Replace [your company]. If the firm has no public bonds, use the bank credit facility's stated rate and skip the pricing math.
- *For ChatGPT / Gemini:* Identical.
- *For Claude Code:* The YTM solver could be a Python script using `scipy.optimize`, but Excel works fine.

### Connection to previous chapters

Builds on Chapters 7–9's TVM and uses the firm's credit context from Chapter 6's TIE ratio.

### Preview of next chapter

Chapter 11 builds the DCF model for stock valuation. The Chapter 11 LLM Exercise is the project's analytical centerpiece — your first complete DCF.

---

## AI Wayback Machine

**Frank Fabozzi** is the field's most prolific contributor to fixed-income analysis and bond mathematics.

**Run this:**

```
Who is Frank Fabozzi, and how does their work connect to bonds and bond valuation we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about their career or ideas.
```

→ Search **"Frank Fabozzi"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to apply Frank Fabozzi's framework to a specific finance question.
- Add a constraint: "Answer including criticisms or limits of Frank Fabozzi's framework."

What changes? What gets better? What gets worse?

---

**Tags:** bonds, bond-valuation, yield-to-maturity, coupon-rate, yield-curve, duration, credit-rating, interest-rate-risk
