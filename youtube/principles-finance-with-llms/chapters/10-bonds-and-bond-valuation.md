# Chapter 10 — Bonds and Bond Valuation

**Suggested titles**
1. Pricing a Loan
2. Coupons, Yields, and the Inverse That Runs Underneath
3. Why Bond Prices Move Opposite Interest Rates

**TL;DR.** A bond is a loan: the issuer borrows money from investors and promises to pay it back, with periodic interest, on a known schedule. Pricing a bond means discounting those future cash flows to today's dollars. The discount rate the market uses — the **yield to maturity** — moves inversely with the bond's price. Understanding why is the difference between knowing a bond's specs and understanding what owning one actually means.

---

## The puzzle of a bond trading above par

In March 2021, 3M Company had a corporate bond outstanding with these specs:

- **Par value**: $1,000
- **Coupon rate**: 2.25% annually
- **Maturity date**: September 19, 2026
- **Market price**: $1,051.20 — a fraction over 105% of par
- **Quoted yield**: 1.24%

The bond was paying $22.50 per year per $1,000 of par value. It would return the $1,000 face value in September 2026. Why was it trading at $1,051.20 — *more* than its face value, more than the issuer would ever pay back at maturity?

Because interest rates had fallen. When 3M issued the bond, market yields for A+ corporate paper of similar maturity were around 2.25%. By March 2021, market yields had dropped to about 1.24%. New 3M bonds being issued in March 2021 had to offer only 1.24% to attract investors. The old bond, locked into 2.25%, was suddenly more attractive than the alternatives — so investors bid its price up until its *yield* matched the market. The price stopped rising at $1,051.20, where the higher coupon rate and the $1,000 maturity payment together produce an effective yield of 1.24% per year.

This is the puzzle. Bond prices move *opposite* interest rates, not with them. When rates fall, prices rise. When rates rise, prices fall. The mechanism is just present-value arithmetic — the same arithmetic from Chapters 7–9 — applied to a specific kind of cash flow stream.

For the equity research project, this chapter does two things. First, it teaches you to price bonds, including the bonds your chosen company has outstanding. Second, it gives you the tools to read the **yield curve** — the term structure of interest rates — which is one of the most important macro indicators an analyst tracks.

---

## Learning objectives

After working through this chapter, you should be able to:

- Define and use the basic vocabulary of bonds: par value, coupon rate, coupon payment, maturity, yield to maturity, callable, convertible, zero-coupon, floating-rate.
- Compute a bond's price as the present value of its coupon stream plus the present value of its principal repayment.
- Identify whether a bond trades at a premium, at a discount, or at par, based on the relationship between its coupon rate and the market YTM.
- Compute YTM given a bond's price and other characteristics.
- Read a yield curve and identify normal, inverted, and flat shapes.
- Distinguish among the major bond risks: interest rate risk, default risk, credit risk, liquidity risk, call risk, reinvestment risk, term risk.
- Read a bond rating from S&P, Moody's, or Fitch, and locate where it sits on the investment-grade/junk boundary.

**Prerequisites.** Chapters 7–9 (TVM); Chapter 5 (financial statements — for understanding issuer credit quality).

---

## Concept 1 — What a bond is

A **bond** is a loan with structured terms. The issuer (a corporation, a government, a municipality) borrows money from investors and promises to pay it back with interest on a known schedule.

The vocabulary takes a chapter to install. Once you have it, the rest is arithmetic.

### The basic terms

**Par value (face value)**: the principal amount the issuer promises to repay at maturity. The standard par value for corporate bonds is $1,000. Some Treasury securities use $100. The face value is fixed at issuance and does not change.

**Coupon rate**: the annual interest rate the issuer pays on the par value. A 5% coupon on a $1,000 par bond pays $50 per year. The coupon rate is fixed at issuance and stays fixed for the life of the bond — this is the defining feature of a fixed-rate bond.

**Coupon payment**: the dollar amount paid to the bondholder per period. For an annual-coupon bond at 5% on $1,000 par, that's $50 per year. For a *semi-annual* bond — the standard for US corporate bonds — the coupon payment is $25 every six months.

**Maturity date**: the date on which the issuer pays back the par value and the bond ceases to exist. Maturities can be a few months (Treasury bills) or 30 years (long Treasuries and many corporates).

**Yield to maturity (YTM)**: the discount rate that, when applied to the bond's cash flows, makes their present value equal to the current market price. Equivalently, the rate of return the bondholder earns if they hold the bond to maturity and reinvest the coupons at the same rate. YTM is set by the market, not by the issuer. It moves daily; the coupon rate doesn't.

The crucial pair: **coupon rate is fixed; YTM varies.** When market interest rates change, the bond's price adjusts so its YTM matches the new market rate. The coupon doesn't change — the *price* changes.

### Bond pricing conventions

Bond prices are quoted as a percentage of par. A bond trading at 95.0 means $950 per $1,000 of par. A bond trading at 105.0 means $1,050 per $1,000 of par. The 3M bond from the opening puzzle, quoted at 105.120%, traded at $1,051.20 per $1,000 of par.

A bond trading at par (100.0) is selling for exactly its face value. This happens when the coupon rate equals the YTM — the bond pays exactly what the market is demanding.

A **premium bond** trades above par (price > 100%). This happens when the coupon rate exceeds the market YTM — the bond's payments are more attractive than alternatives, so investors pay extra. The 3M bond is a premium bond.

A **discount bond** trades below par (price < 100%). This happens when the coupon rate is less than the market YTM — the bond's payments are less attractive, so investors demand a price below face value to compensate.

### Types of bonds

**Treasury securities** — issued by the US government, considered default-risk-free in nominal dollars.
- T-bills: maturity ≤ 1 year, sold at a discount and redeemed at par (zero-coupon).
- Treasury notes: maturity 2–10 years, semi-annual coupons.
- Treasury bonds: maturity 20 or 30 years, semi-annual coupons.

**Municipal bonds (munis)** — issued by states, cities, or local authorities. Generally exempt from federal income tax (and sometimes state and local tax) in the US, which makes their yields look low until you adjust for taxes.

**Corporate bonds** — issued by companies. Risk varies enormously, from AAA-rated industrials to high-yield ("junk") bonds. Corporate bond yields typically include a credit spread over Treasury yields.

**Zero-coupon bonds** — pay no coupons at all. Issued at a deep discount and redeemed at par. The investor's entire return comes from the price appreciation. Useful for matching specific future obligations (a college tuition bill ten years away).

**Convertible bonds** — corporate bonds that can be converted into a fixed number of the issuer's common shares at the holder's option. Combine bond and stock features and are priced accordingly.

**Floating-rate bonds (floaters)** — coupon resets periodically based on a reference rate (Treasury rate, prime, or — historically — LIBOR). Less price-sensitive to interest-rate changes than fixed-rate bonds.

**Callable bonds** — give the issuer the option to redeem the bond before maturity, usually when interest rates fall and the issuer can refinance at a lower rate. Investors are compensated for this option with a slightly higher coupon.

For the equity research project: when reading your chosen company's 10-K debt footnote, you'll find a list of outstanding bonds with their par values, coupon rates, maturities, and any special features (callable, convertible). Each piece of debt has economic implications for the firm's capital structure and cost of capital.

### Common misconceptions

- *"Bond and 'fixed income' mean low risk."* Treasuries have low default risk. Junk bonds, emerging-market debt, and long-duration bonds during rate spikes can lose 20–40% in a year. Fixed income does not mean fixed price.
- *"Coupon rate is the bond's yield."* Coupon rate is what the issuer pays per dollar of par. Yield is what the investor earns at the current price. The two coincide only when the bond trades at par.

---

## Concept 2 — Pricing a bond

Pricing a bond is mechanically just present value of a mixed cash flow stream — exactly the Chapter 9 toolkit applied to a specific stream. The stream has two parts: the coupon payments (an annuity) and the par-value repayment at maturity (a single payment).

### The bond pricing formula

For an annual-coupon bond with par value $F$, annual coupon payment $C$, $n$ years to maturity, and yield to maturity $y$:

$$P = \sum_{t=1}^{n} \frac{C}{(1+y)^t} + \frac{F}{(1+y)^n}$$

The first term is the present value of the coupon stream — an annuity. Using the closed-form annuity formula from Chapter 8:

$$\text{PV of coupons} = C \times \frac{1 - (1+y)^{-n}}{y}$$

The second term is the present value of the par-value repayment — a single payment:

$$\text{PV of par} = \frac{F}{(1+y)^n}$$

So:

$$\boxed{P = C \times \frac{1 - (1+y)^{-n}}{y} + \frac{F}{(1+y)^n}}$$

Three quantities determine the price: the coupon $C$, the YTM $y$, and the time to maturity $n$. The par value $F$ is fixed. That's all that's in there.

### Worked example — pricing the 3M bond

The 3M bond from the chapter opening: $1,000 par, 2.25% coupon (annual), about 5.5 years to maturity from March 2021, market YTM of 1.24%.

Annual coupon: $1,000 × 2.25\% = \$22.50$.

PV of coupons:
$$\text{PV}_C = 22.50 \times \frac{1 - (1.0124)^{-5.5}}{0.0124} = 22.50 \times 5.281 = \$118.83$$

PV of par:
$$\text{PV}_F = \frac{1{,}000}{(1.0124)^{5.5}} = \frac{1{,}000}{1.0699} = \$934.44$$

Bond price:
$$P = 118.83 + 934.44 = \$1{,}053.27$$

The market price was $1,051.20. We're within 0.2% of the actual market price, which is what you'd expect — small discrepancies arise from precise day-count conventions, accrued interest, and the fact that the market YTM I used ($1.24\%$) is a rounded summary of the actual yield.

### Semi-annual coupons — adjustments

Most US corporate and Treasury bonds pay coupons twice a year, not annually. Adjust the formula:

- Number of periods $n$ becomes $2n$ (for an $n$-year bond).
- Periodic interest rate $y/2$ becomes the discount rate per period.
- Periodic coupon payment becomes $C/2$.

For a 15-year bond with 4% annual coupon (so 2% per semiannual period), $1,000 par, and 5% market YTM (2.5% per period):

$$P = \frac{1{,}000 \times 0.02}{0.025} \times [1 - (1.025)^{-30}] + \frac{1{,}000}{(1.025)^{30}}$$

$$= 800 \times [1 - 0.4767] + 1{,}000 \times 0.4767$$

$$= 800 \times 0.5233 + 476.74$$

$$= 418.66 + 476.74 = \$895.40$$

This is a discount bond. The 4% coupon rate is below the 5% market YTM; the bond trades for less than par.

### Premium, discount, par — the underlying logic

The pattern is simple once you see it:

- **Coupon rate > YTM** → coupons are more attractive than market alternatives → investors bid the price *up* → price > par → **premium**.
- **Coupon rate < YTM** → coupons are less attractive than market alternatives → investors require a price discount → price < par → **discount**.
- **Coupon rate = YTM** → coupons exactly match the market → price = par → **par bond**.

### YTM — the inverse computation

Given a bond's price, YTM is the discount rate that solves:

$$P = \sum_{t=1}^{n} \frac{C}{(1+y)^t} + \frac{F}{(1+y)^n}$$

There's no closed-form solution for $y$. It has to be solved iteratively — by trial and error, by financial calculator (`I/Y` key after entering PV, FV, PMT, N), or by Excel's `=RATE()` function.

Example. A bond trades at $675, has a $1,000 par, pays a 3.5% annual coupon ($35 per year), and has 12 years to maturity. The YTM solves:

$$675 = 35 \times \frac{1 - (1+y)^{-12}}{y} + \frac{1{,}000}{(1+y)^{12}}$$

Solving (iteratively or with `=RATE(12, 35, -675, 1000)` in Excel) gives YTM ≈ 7.76%.

The intuition: at $675, the bond is deeply discounted. The investor pays $675 today for $35/year of coupons plus $1,000 at maturity. The implied return is 7.76% per year — much higher than the 3.5% coupon rate, because the investor also captures $325 of price appreciation between purchase and maturity.

↳ **Dig Deeper — The 2022-2024 yield curve inversion that didn't (immediately) produce a recession**

*The US Treasury yield curve inverted sharply in mid-2022 as the Fed began its tightening cycle. Historically, every yield curve inversion since the 1960s has been followed by a recession within 6-24 months. The 2022 inversion was the longest-sustained without a recession in modern history. What does the case study tell us about the yield curve as an indicator?*

**Prompt:**
> Walk through the chronology of the 2022-2024 yield curve inversion: when it began, how deep it got, when it un-inverted, and what happened to the economy across that period. Then summarize the academic explanations for why this inversion didn't follow the historical pattern (post-pandemic distortions, fiscal policy, supply-chain disinflation). What's your reading: was 2022-2024 a one-time anomaly, or has the yield curve as a recession indicator structurally weakened?

**What to do with the output:** Save it. Yield curve interpretation appears throughout your equity research project; understanding the limits of historical patterns matters.

### The trade-off (concept 2)

Bond pricing trades **mathematical precision against future-rate uncertainty**. The pricing formula is exact given the YTM. The YTM at the moment of purchase is observable. But the YTM that prevails in the future — and therefore the bond's price between now and maturity — is uncertain. The pricing formula tells you what the bond is worth *today* given today's yields. Chapter 12 will give you tools to think about how rates have moved historically.

### Common misconceptions

- *"You earn the coupon rate by holding a bond."* You earn the YTM at the time of purchase if you hold to maturity. The coupon rate is what the issuer pays per dollar of par. If you bought a bond at a discount, your effective return is higher than the coupon rate.
- *"Bond prices are mostly determined by the coupon."* For a fixed-coupon bond, the price is mostly determined by the YTM. The coupon is a constant; the yield is the variable.

---

## Concept 3 — Bond risks and the yield curve

Bonds are usually framed as "safe" investments. Up to a point, that's true — they're more predictable than stocks. But bonds carry several distinct risks, and each one matters in different conditions.

### The taxonomy of bond risks

**Interest rate risk (market risk).** Bond prices move inversely to interest rates. If you own a 30-year bond and interest rates rise 1 percentage point, the bond's price falls — possibly substantially. The 2022 bond market lost about 13% in a year because of the Fed's tightening cycle, the worst calendar-year return on the bond aggregate index in modern history. Long-maturity bonds and low-coupon bonds are the most sensitive.

The standard measure of interest-rate sensitivity is **duration** — roughly, the percentage price change per 1-percentage-point change in yields. A bond with a duration of 10 will fall about 10% if rates rise 1%. The full math is beyond this chapter; the qualitative point is that long bonds are more rate-sensitive than short bonds, and zero-coupon bonds are the most rate-sensitive of all.

**Default risk.** The risk that the issuer fails to make scheduled payments. Treasuries are usually treated as default-risk-free (in nominal terms; inflation can eat the real return). Corporate bonds carry default risk that varies with the issuer's financial health.

**Credit risk** (a related concept) — the bondholder's overall assessment of the issuer's likelihood of meeting all obligations on schedule. Default risk is the binary version; credit risk is the broader concept.

**Liquidity risk.** The risk that you can't sell the bond quickly without taking a price hit. Treasuries are extremely liquid; small-issue corporate bonds may not be. In stressed markets, even normally-liquid bonds can become hard to trade — 2008 and the early days of the 2020 COVID panic both featured bond-market liquidity crises.

**Call risk.** For callable bonds, the risk that the issuer redeems the bond early when rates have fallen — exactly when the investor would prefer to hold it. Callable bonds compensate investors with slightly higher coupons.

**Reinvestment risk.** Even non-callable bonds expose investors to reinvestment risk: when coupons are received, the investor must reinvest them at *whatever rate prevails* at that time, which may be lower than the bond's YTM. The standard YTM calculation assumes coupons are reinvested at the same YTM, which is rarely true in practice.

**Term risk** — the broader risk that lending at a fixed rate over a long horizon may underperform a sequence of shorter-term lending decisions if rates rise.

For your chosen company's bonds, the relevant risks depend on the bond. A short-dated investment-grade corporate has low default risk and low duration risk. A long-dated high-yield bond has substantial default risk and substantial duration risk. The 10-K's debt footnote tells you which bonds the company has outstanding; the bond ratings tell you what the market thinks of the credit risk.

### Bond ratings

Three major rating agencies — **Standard & Poor's**, **Moody's**, and **Fitch** — assign letter grades to bond issues based on their assessment of default risk.

The hierarchy (using S&P / Fitch notation):

- **AAA, AA, A, BBB**: investment grade. Considered low risk of default.
- **BB, B, CCC, CC, C**: speculative grade ("junk" or "high-yield"). Higher default risk, higher yield.
- **D**: in default.

Moody's uses slightly different notation (Aaa, Aa, A, Baa for investment grade; Ba, B, Caa, Ca, C for speculative; with default not formally rated). The boundary between investment-grade and junk — BBB/Baa — is a bright line in many institutional investment mandates.

Two important caveats. **Ratings are opinions, not guarantees.** Enron was rated investment-grade until two months before its bankruptcy. Lehman Brothers was rated A two days before its collapse. Rating agencies face institutional incentive problems (they're paid by the issuers they rate) and have historically been late to identify deteriorating credit.

For an analyst, ratings are a useful starting point but not a final answer. A serious credit analysis examines the issuer's financial statements directly, looks at debt-coverage ratios (TIE from Chapter 6), examines off-balance-sheet obligations, and cross-checks against the rating agency's narrative.

### The yield curve

Plot bond yields on the y-axis and time-to-maturity on the x-axis, and you have a **yield curve**. The shape of the curve carries economic information.

**Normal yield curve** — upward-sloping. Long-term yields exceed short-term yields. This is the typical shape and reflects a term premium: investors demand more yield to lend longer, both because of duration risk and because of inflation expectations. Most expansions feature a normal yield curve.

**Inverted yield curve** — downward-sloping. Long-term yields are *below* short-term yields. Unusual and historically associated with recessions. The mechanism: investors expect future short rates to fall (because they expect the Fed to cut rates in response to a slowdown), so they're willing to lock in current long-term yields even though they're lower than short rates. Every US recession since the 1960s has been preceded by a yield curve inversion at some point — though not every inversion has been followed by a recession in the immediate term.

**Flat yield curve** — short and long rates are about the same. Often a transitional state between normal and inverted shapes, or a result of unconventional monetary policy (quantitative easing pushed long rates down toward short rates in the 2010s).

The 2022 cycle saw the yield curve invert sharply (short Treasury yields rose well above 10-year yields) as the Fed tightened to fight inflation. The recession the inversion implied took longer to arrive than expected — by mid-2024, the inversion had been the longest on record without producing a recession. The yield curve is a probabilistic indicator, not a deterministic one. `[verify]` for current curve shape.

### Worked example — reading the curve for your company

For the project, look up the current US Treasury yield curve (the FRED tickers DGS3MO, DGS2, DGS5, DGS10, DGS30 will give you key points). Plot them against maturity. Note the shape.

Then look at your company's outstanding corporate bonds. Each one has a YTM that should be roughly equal to the Treasury yield at the same maturity *plus a credit spread*. If your company's 10-year bond yields 5.5% and the 10-year Treasury yields 4.0%, the credit spread is 150 basis points. That spread is what the market is charging your company for default risk.

When the credit spread widens (say, from 150 bp to 250 bp), it means the market is more worried about your company. When it narrows, less worried. Watching the spread over time is a way to track the firm's credit health from the bond market's perspective, independent of the equity market.

↳ **Dig Deeper — Duration as a sensitivity measure**

*Duration measures how much a bond's price changes for a 1-percentage-point change in yields. It's not a calendar concept (despite being measured in years); it's a sensitivity measure. The math comes from a Taylor-series approximation of the bond pricing formula.*

**Prompt:**
> Derive the relationship between Macaulay duration and modified duration. Then compute modified duration for: (a) a 5-year zero-coupon bond at 5% YTM, (b) a 10-year 5%-coupon bond at 5% YTM, (c) a 30-year 4%-coupon bond at 5% YTM. Show the math. Which has the highest interest-rate sensitivity, and why? Then briefly explain convexity — what duration alone misses.

**What to do with the output:** Save it. Duration is intermediate-finance content; the qualitative version in Chapter 10 is enough for the project, but the math is worth seeing.

### The trade-off (concept 3)

Yield curve analysis trades **forecasting power against precise interpretation**. The curve carries genuine information about market expectations. The information is imprecise — inversions don't always lead to recessions, and recessions can come without prior inversions. Treat the curve as a probabilistic input to your view, not as a forecast.

### Common misconceptions

- *"AAA-rated means safe."* AAA corporate paper has a very low historical default rate, but that's not the same as zero. AAA-rated structured products (mortgage-backed securities) defaulted en masse in 2008. The label means the agency thinks default is unlikely; that's not a guarantee.
- *"Long bonds always pay more than short bonds."* During inversions, short bonds pay more. The premium for long bonds is normal but not universal.

---

## Synthesis — bonds as the simplest valuation problem

Bonds are the cleanest test case for the TVM machinery. The cash flows are explicitly contractual: coupon dates and amounts, maturity date and value. Given a discount rate (the YTM), the price falls out by direct computation.

What makes bonds non-trivial is that the discount rate is the *output* the market sets, and the market changes its mind constantly. A bond's price moves daily as the market re-evaluates what yield to demand. The same bond is worth different amounts at different rate environments — and the rate environment depends on macro factors the bond's issuer can't control.

For the equity research project, the deliverable from this chapter is an analysis of your chosen company's debt: outstanding bonds, their ratings, their yields, the credit spread to Treasuries, and what these tell you about the firm's perceived credit health. This becomes part of Chapter 17's analysis of the firm's capital structure and Chapter 6's ratio analysis (TIE, in particular).

Chapter 11 takes the same TVM machinery and applies it to stocks — a harder valuation problem because the cash flows are uncertain. Chapter 14 returns to discount rates with the CAPM. Chapter 17 puts it all together for the firm's WACC.

---

## Exercises

### Warm-up

**10.1** Define: par value, coupon rate, coupon payment, maturity date, yield to maturity. Which of these are fixed at issuance, and which can change?

**10.2** When does a bond trade at a premium? At a discount? At par?

**10.3** State the inverse relationship between bond prices and interest rates. Explain the mechanism in plain English.

### Application

**10.4** A 10-year corporate bond has $1,000 par value, a 5% annual coupon, and a market YTM of 6%.

(a) What is the bond's price?
(b) Is it a premium or discount bond? Why?
(c) Recompute the price if the YTM rises to 8%. By what percentage did the price change?

**10.5** A Treasury bond pays semi-annual coupons of $30 (so 6% annual coupon on $1,000 par), matures in 8 years, and is currently priced at $1,055.40.

(a) What is the YTM? (Use Excel's `=RATE()` or iterate by hand.)
(b) Is this above or below the coupon rate? What does that tell you about whether the bond is at a premium or discount?

**10.6** Locate one of your chosen company's outstanding bonds (the 10-K debt footnote will list them). Find its current market YTM (corporate bond data is on Bloomberg, Yahoo Finance, or your firm's data feed). Compute the credit spread over the same-maturity Treasury yield. What does the spread tell you?

### Synthesis

**10.7** A 30-year zero-coupon bond and a 30-year coupon bond both have $1,000 par values and identical YTMs of 5%. Compute the duration of each. (For the zero, duration equals maturity = 30 years. For the coupon bond, use a duration formula or the rough rule that duration < maturity for any coupon bond.) Which is more sensitive to a 1% rise in interest rates?

**10.8** Read recent news about the US Treasury yield curve. Has it been inverted? For how long? What has happened to the economy in that period? What does the experience tell you about the yield curve as a recession indicator?

### Challenge

**10.9** A callable corporate bond has a 6% coupon, $1,000 par, 20 years to maturity, and a 5-year call protection (cannot be called for the first 5 years). After year 5, the issuer can call the bond at $1,030.

(a) If interest rates have fallen meaningfully by year 5, would the issuer call? Why?
(b) What's the implication for the bondholder?
(c) How would the bond's price compare to a non-callable bond with the same other terms?

**10.10** Using the FRED database, build a chart of the US 2-year Treasury yield, the 10-year Treasury yield, and the spread between them over the past 20 years. Identify periods of inversion. For each, note whether a recession followed within the next 18 months. What is your reading of the yield curve as a recession-prediction tool?

---

## Chapter summary

- A bond is a structured loan: par value at maturity plus periodic coupon payments.
- Bond price = PV of coupon stream (annuity) + PV of par value repayment (single payment).
- Coupon rate is fixed at issuance; YTM is set by the market and varies daily.
- Premium bond (price > par): coupon rate > YTM. Discount bond (price < par): coupon rate < YTM. Par bond: coupon rate = YTM.
- Bond prices move *inversely* to interest rates. Long-maturity bonds are more sensitive (higher duration).
- Bonds carry interest-rate, default, credit, liquidity, call, reinvestment, and term risks.
- Bond ratings from S&P, Moody's, Fitch summarize credit risk. Investment-grade boundary: BBB/Baa.
- The yield curve plots yields against maturity. Normal (upward), inverted (downward), and flat shapes carry economic information.

---

## What would change my mind

The chapter argues that bond prices are determined by present-value arithmetic and that the market's YTM is the right discount rate. The reading would have to revise if (a) liquidity premia or behavioral factors consistently caused bonds to trade away from their PV-of-cash-flows values for extended periods — they do, in stressed markets, but the deviation is usually temporary; for first-pass thinking, the PV framework is right, or (b) credit ratings turned out to be so unreliable that they couldn't be used as inputs to credit analysis at all — they're imperfect, but they're not random. The 2008 mortgage-rating debacle is a real and important caveat.

## Still puzzling

The honest unresolved tension is between **YTM as a return measure** and **realized return**. YTM assumes coupons are reinvested at the same YTM. In practice, coupons are reinvested at whatever rate prevails when they arrive, which can be very different. Over a long horizon, the realized return on a bond can differ meaningfully from its initial YTM — sometimes by hundreds of basis points. The standard finance treatment papers over this with the "held to maturity, coupons reinvested at YTM" assumption. Real bond investors are more careful, and the difference matters in retirement-portfolio modeling.

---

## Connections forward

- **Chapter 11** applies similar PV machinery to stocks, where cash flows are uncertain.
- **Chapter 12** examines historical bond and equity returns.
- **Chapter 14** computes beta, which connects bond yields and equity risk premia via CAPM.
- **Chapter 17** uses the firm's bond yields to compute the cost of debt, an input to WACC.
- **Chapter 20** revisits interest-rate risk as a risk-management problem.

---

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

4. **Interpret the spread** — How does this spread compare to typical spreads for the bond's rating? (Investment-grade BBB-rated bonds typically yield 100-200 basis points over Treasuries; investment-grade A-rated, 60-150 bps.)

5. **Compute approximate duration** — Use the rough rule that for a 10-year coupon bond, duration is roughly 7-8 years. State the implied price sensitivity to a 1% rate change.

Show all calculations. Cite the source of each input.
```

### What this produces

A 1-2 page bond-pricing analysis. Adds to the report's debt analysis section. Cross-checks the firm's cost of debt that you'll use in the WACC computation in Chapter 17.

### How to adapt this prompt

- *For your own company:* Replace [your company]. If the firm has no public bonds, use the bank credit facility's stated rate and skip the pricing math.
- *For ChatGPT / Gemini:* Identical.
- *For Claude Code:* The YTM solver could be a Python script using `scipy.optimize`, but Excel works fine.

### Connection to previous chapters

Builds on Chapters 7-9's TVM and uses the firm's credit context from Chapter 6's TIE ratio.

### Preview of next chapter

Chapter 11 builds the DCF model for stock valuation. The Chapter 11 LLM Exercise is the project's analytical centerpiece — your first complete DCF.

---

**Tags:** bonds, bond-valuation, yield-to-maturity, coupon-rate, yield-curve, duration, credit-rating, interest-rate-risk


---

## AI Wayback Machine

**Frank Fabozzi** was fixed-income scholar whose textbooks have shaped how a generation of finance students think about bond valuation.

**Run this:**

```
Who is Frank Fabozzi, and how does their work connect to bonds and bond valuation we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about their career or ideas.
```

→ Search **"Frank Fabozzi"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to apply Frank Fabozzi's framework to a specific finance question.
- Add a constraint: "Answer including criticisms or limits of Frank Fabozzi's framework."

What changes? What gets better? What gets worse?
