# Chapter 7 — Time Value of Money I: Single Payment Value

**Suggested titles**
1. Why a Dollar Tomorrow Is Worth Less Than a Dollar Today
2. The Arithmetic of Waiting
3. Compounding, Discounting, and the Rule of 72

**TL;DR.** Money has a time value because money you have today can earn a return between now and any future date. The single-payment time-value-of-money formula — $FV = PV \times (1+r)^n$ — converts between present and future values given an interest rate and a time horizon. Master it, and you can solve four kinds of problems by rearrangement: future value, present value, required interest rate, and required time horizon.

---

## The puzzle of two offers

A relative offers you a deal. They have $10,000 they want to give you, but they need to make sure you actually want it. Two options:

- **Option A** — they hand you $10,000 today.
- **Option B** — they promise to hand you $11,000 two years from now, in writing, with no risk that they renege.

The answer depends entirely on one thing the question doesn't tell you. *What would you do with the $10,000 between now and two years from now?*

If you'd put it in a savings account at 2% per year, $10,000 today grows to $10,000 × (1.02)² = $10,404 in two years. Option B's $11,000 is more. Take Option B.

If you'd invest it in something that earned 6% per year, $10,000 grows to $10,000 × (1.06)² = $11,236 in two years. Option B's $11,000 is less. Take Option A.

If you'd earn exactly 4.88%, the two options are tied: $10,000 × (1.0488)² ≈ $11,000. The breakeven rate is the rate at which your money would grow over two years to match the future offer. Above that rate, today is better. Below that rate, future is better.

This is the entire field of finance, in miniature. Money has a time value because money you have today can earn a return between now and any future date. The size of that return — the **interest rate** — determines how much $1 today is worth in some future period, and conversely, how much $1 in some future period is worth today.

For the equity research project, this chapter installs the arithmetic that the rest of the book uses constantly. Every valuation in Chapters 10, 11, and 16 is, at its core, an application of the single-payment formula we build here.

---

## Learning objectives

After working through this chapter, you should be able to:

- Explain the three reasons money has a time value.
- Compute the future value of a single present cash flow at a given rate over any number of periods.
- Compute the present value of a single future cash flow at a given discount rate.
- Solve for the unknown variable (rate, time, PV, or FV) when the other three are known.
- Adjust the basic formula for compounding more frequent than annual.
- Distinguish nominal from real interest rates using the Fisher equation.
- Use the Rule of 72 to estimate doubling times for any rate of growth.

**Prerequisites.** Comfort with exponents and basic algebra. Chapter 3 (interest rates as the price of money).

---

## Concept 1 — Why money has time value, and the master formula

Three reasons, in order of importance.

**1. Money invested today earns a return.** A dollar in your pocket today can be deposited in a savings account, used to buy stocks, or lent to someone, and at some point in the future you'll have more than a dollar. A dollar that arrives in the future cannot have been earning anything in the meantime. So the present dollar is worth more than the future dollar by exactly the return you would have earned.

**2. Future payments are uncertain.** The person promising you $11,000 two years from now might not pay. The bank holding your savings might fail. The country might experience hyperinflation. Even if you trust the counterparty completely, accidents happen. A dollar in hand carries less default risk than a dollar promised.

**3. People prefer present consumption.** This is the softest of the three reasons but it's real. Most people would rather have a thing now than the same thing later. Even in a world with no investment opportunities and no default risk, most people would discount the future at some positive rate just because they'd rather not wait.

The first reason is the dominant one for finance. The second matters for credit-risk analysis. The third is more relevant for behavioral economics. For the rest of this book, when we say "money has time value," we mostly mean reason 1: present money can be invested.

### The master formula

Suppose you put $1,000 into a savings account paying 4% interest per year. After one year, you have $1,040 — your original $1,000 plus $40 of interest. Trivial.

After two years? Your $1,040 (the balance from year 1) earns 4% on itself: $1,040 × 0.04 = $41.60. So you end year 2 with $1,040 + $41.60 = $1,081.60.

Notice the $41.60. That's slightly more than the $40 you earned in year 1. Why? Because in year 2 you earned 4% on $1,040, not on $1,000. You earned interest on your interest. **Compound interest** — interest paid on past interest — is the engine of everything that follows.

The general formula. If you start with **PV** (present value), invest at rate **r** per period, and let it compound for **n** periods, you end with:

$$FV = PV \times (1+r)^n$$

Read it: the future value equals the present value times the future-value factor $(1+r)^n$. The factor is greater than 1 whenever $r > 0$, and grows exponentially with $n$.

Three concrete computations to anchor the formula:

| Initial $1,000, rate 4% | Future value | Multiplier |
|---|---|---|
| 3 years | $1,124.86 | 1.125 |
| 10 years | $1,480.24 | 1.480 |
| 50 years | $7,106.68 | 7.107 |

Three years — modest growth. Ten years — about 50% growth. Fifty years — over 7x. The formula is exponential, and exponentials feel slow at first and shockingly fast later. This is where the Feynman move "what's actually happening" earns its keep: each year, you earn 4% on a slightly larger base than the year before, and the compounding compounds.

### Compounding visualized

If you graph $FV = 1{,}000 \times (1.04)^n$ for n from 0 to 100, the curve is barely visible above the horizontal $1,000 line for the first 20 years, and then rockets upward. Most of the action is in the second half of the time horizon. This is why financial advice for young people emphasizes starting early — the early dollars get the most years of compounding.

A clean illustration. Two friends, both age 22.

- **Friend A** invests $5,000 per year from age 22 to age 30 (9 years), then stops, and lets it compound at 8% until age 65.
- **Friend B** waits until age 30, then invests $5,000 per year from age 30 to age 65 (35 years) at the same 8%.

At age 65:
- Friend A contributed $45,000 total but their balance is about $887,000.
- Friend B contributed $175,000 total but their balance is about $861,000.

A invested less than a third as much, started 8 years earlier, and ended up with slightly more. That is compound interest. The dollars contributed early have many more years to grow than the dollars contributed late, and the difference is enormous. (`[verify]` exact figures with current spreadsheet calculation; the qualitative point is robust.)

↳ **Dig Deeper — Negative interest rates**

*Standard TVM assumes positive interest rates. But several countries (Japan, Switzerland, some European banks) have at various times had negative nominal policy rates. Some Treasury yields have gone negative in real terms even more often. What does negative-rate TVM actually look like, and what does it imply for capital allocation?*

**Prompt:**
> Explain the mechanics of negative interest rates as observed in Japan (since 2016), Switzerland, and the Eurozone. What does the standard TVM formula produce when r < 0? Then describe two real economic phenomena that emerge under negative-rate conditions: (1) why some firms accumulate cash rather than borrowing, even at negative cost, and (2) what happens to the present value of long-dated future cash flows when rates are negative.

**What to do with the output:** Save it. The standard TVM intuition assumes rates are positive; understanding the edge case sharpens the standard reasoning.

### The trade-off (concept 1)

Time-value calculations trade **simplicity against realism**. The formula $FV = PV(1+r)^n$ assumes a constant interest rate over the full horizon, no taxes, no inflation, no risk of default, no withdrawal of funds. Real-world investing has all of these. The formula is the right starting point because it isolates the single most important effect — compounding — and shows it cleanly. Adjustments come later (Chapter 8 for streams of payments, Chapter 13 for variability of returns, Chapter 17 for risk-adjusted rates).

### Common misconceptions

- *"Compound interest is just simple interest plus a little extra."* No — over long horizons, compound interest is dramatically more than simple interest. Over 30 years at 8%, $1,000 grows to $10,063 with compounding but only $3,400 with simple interest.
- *"Higher returns mean linearly higher final values."* No — they mean exponentially higher. At 4%, $1 becomes $7.10 in 50 years. At 8%, $1 becomes $46.90 in 50 years. The final value at 8% is over 6× the final value at 4%, even though the rate is just 2× higher.

---

## Concept 2 — Computing in both directions

The master formula has four variables: PV, FV, r, n. Given any three, you can solve for the fourth. This single formula generates four kinds of problems, and equity analysts solve all four constantly.

### Direction 1 — Future value (compound forward in time)

You know PV, r, and n. You compute FV.

Direct application of the formula. Examples:

- $1,000 invested at 6% for 10 years: $FV = 1{,}000 \times (1.06)^{10} = \$1{,}790.85$.
- $25,000 retirement savings invested at 7% for 30 years: $FV = 25{,}000 \times (1.07)^{30} = \$190{,}306$.
- A $400,000 house appreciating at 4% per year for 6 years: $FV = 400{,}000 \times (1.04)^6 = \$506{,}128$.

In Excel: `=FV(rate, nper, pmt, [pv], [type])`. For a single payment with no recurring payment, set `pmt = 0`. For our $1,000 / 6% / 10-year example: `=FV(0.06, 10, 0, -1000)` returns 1790.85. Note the negative sign on PV — Excel uses sign convention where money flowing out (the deposit) is negative.

In a financial calculator: enter PV = −1000, I/Y = 6, N = 10, PMT = 0, then compute FV. The calculator returns 1790.85.

### Direction 2 — Present value (discount backward in time)

You know FV, r, and n. You compute PV. Rearranging the formula:

$$PV = \frac{FV}{(1+r)^n}$$

The factor $\frac{1}{(1+r)^n}$ is called the **present value factor** or **discount factor**. It is always less than 1 for positive r and positive n — meaning a future dollar is worth less than a present dollar.

Examples:

- A $50,000 lottery payout in 5 years, discounted at 5%: $PV = \frac{50{,}000}{(1.05)^5} = \$39{,}176$. The lottery is worth less today than its face value because you have to wait.
- A $1,000 savings bond maturing in 30 years, discounted at 5%: $PV = \frac{1{,}000}{(1.05)^{30}} = \$231$. A "$1,000 savings bond" — gifted to a child — is actually worth about $231 the day it's bought.
- A $1 million life insurance payout 20 years from now, discounted at 6%: $PV = \frac{1{,}000{,}000}{(1.06)^{20}} = \$311{,}805$.

In Excel: `=PV(rate, nper, pmt, [fv], [type])`. For our $50,000 lottery example: `=PV(0.05, 5, 0, 50000)` returns −39,176.31. Excel returns the negative because under sign convention, you'd "pay" that to receive the future $50,000.

The discount rate matters enormously. A future $1 million discounted at 5% over 30 years is worth $231,377. The same $1 million discounted at 8% is worth only $99,377. Higher discount rates compress future values much faster. Equity research analysts argue about discount rates because the answer is highly sensitive to it.

### Direction 3 — Solving for the rate (what return is implied?)

You know PV, FV, and n. You compute r. Rearranging:

$$r = \left( \frac{FV}{PV} \right)^{1/n} - 1$$

This is the **implied rate** — the constant annual return that would convert PV into FV over n periods.

Examples:

- A house bought for $300,000 sold for $450,000 ten years later. Implied rate: $(450{,}000/300{,}000)^{1/10} - 1 = 1.5^{0.1} - 1 = 4.14\%$ per year. Decent but not spectacular.
- An investment of $15,000 grew to $25,000 over 8.5 years. Implied rate: $(25{,}000/15{,}000)^{1/8.5} - 1 = 6.19\%$ per year.
- A college tuition that was $5,000 per year in 1985 and $25,000 per year in 2025. Implied rate: $(25{,}000/5{,}000)^{1/40} - 1 = 4.13\%$ per year — meaningfully above general inflation, which is why college affordability is a recurring concern.

In Excel: `=RATE(nper, pmt, pv, [fv], [type])`. For the $15,000 → $25,000 / 8.5-year example: `=RATE(8.5, 0, -15000, 25000)` returns 0.0619 (6.19%).

### Direction 4 — Solving for the time (how long until?)

You know PV, FV, and r. You compute n. Rearranging using logarithms:

$$n = \frac{\ln(FV/PV)}{\ln(1+r)}$$

Examples:

- $100 needs to grow to $133.82 at 5%. How many years? $n = \ln(1.3382) / \ln(1.05) = 5.97$ years.
- $25,000 college fund needs to reach $50,000. At 7%, how long? $n = \ln(2) / \ln(1.07) = 10.24$ years.
- A retirement account at $250,000 needs to reach $1 million. At 8%, how long? $n = \ln(4) / \ln(1.08) = 18.0$ years.

In Excel: `=NPER(rate, pmt, pv, [fv], [type])`.

### A worked example for the project — when does Apple's cash become "infinite"?

Apple holds about $191B in cash and short-term investments. If left in the bank earning 4% (current short-term rates) and not used for buybacks, dividends, or acquisitions, how big would that pile be in 30 years?

$FV = 191{,}000 \times (1.04)^{30} = 191{,}000 \times 3.243 = \$619{,}500$ million, or about $619 billion.

This is the kind of computation that makes Apple's capital-allocation decisions visible. Holding cash earns the risk-free rate; investing it productively (in capex, R&D, or returning to shareholders) might earn substantially more. Whether Apple's $191B is well-deployed or not depends entirely on the alternative uses available to the firm. Chapter 17 examines this question quantitatively.

↳ **Dig Deeper — The social discount rate for environmental decisions**

*When economists value future benefits of climate action vs. present costs, the discount rate matters enormously. A 1% rate values our great-grandchildren's welfare highly. A 5% rate barely values it at all. The Stern Review (2006) and the Nordhaus DICE model use very different rates — and arrive at very different policy implications. The discount-rate choice is technical, ethical, and consequential.*

**Prompt:**
> Explain why the social discount rate matters so much for cost-benefit analysis of long-horizon environmental decisions. Compare the rates used by Nordhaus's DICE model (around 4-5%) and Stern Review (1.4%). What's the philosophical argument for a lower social discount rate? What's the argument against? Then summarize what current US government cost-benefit analysis (under OMB Circular A-4) actually uses.

**What to do with the output:** Save it. The general TVM machinery applies; the choice of rate is where contested values enter.

### The trade-off (concept 2)

Each direction trades **what's known against what's unknown**. The same formula serves all four, and the choice of which one to use depends on what data the analyst has. In equity research, FV calculations are common in forecasting (what will revenue be in 5 years?). PV calculations are common in valuation (what is a future cash flow worth today?). Rate calculations are common in investment evaluation (what return did this investment earn?). Time calculations are common in financial planning (how long until I can retire?).

### Common misconceptions

- *"PV and FV are different concepts."* They are the same concept viewed from opposite directions. Compounding is forward-in-time; discounting is backward-in-time; both use $(1+r)^n$.
- *"You need a financial calculator."* You don't. Excel handles all of this with `=PV()`, `=FV()`, `=RATE()`, `=NPER()` functions. A calculator app on a phone does the math. The conceptual understanding is what's hard.

---

## Concept 3 — Refinements: compounding frequency, real rates, and the Rule of 72

The master formula assumes annual compounding. Real financial instruments often compound more frequently — quarterly, monthly, daily — and inflation eats away at returns over time. Three refinements.

### Refinement 1 — Compounding frequency

If interest is paid more than once per year, the effective return is higher than the stated annual rate suggests. The general formula:

$$FV = PV \times \left(1 + \frac{r}{m}\right)^{m \cdot n}$$

where $r$ is the stated annual rate, $m$ is the number of compounding periods per year, and $n$ is the number of years.

Compare $1,000 at 6% for one year:

- **Annual** ($m=1$): $1{,}000 \times (1.06)^1 = \$1{,}060.00$
- **Quarterly** ($m=4$): $1{,}000 \times (1.015)^4 = \$1{,}061.36$
- **Monthly** ($m=12$): $1{,}000 \times (1.005)^{12} = \$1{,}061.68$
- **Daily** ($m=365$): $1{,}000 \times (1 + 0.06/365)^{365} = \$1{,}061.83$
- **Continuous** ($m \to \infty$): $1{,}000 \times e^{0.06} = \$1{,}061.84$

The differences are small for one year at 6%. They grow with the time horizon and the rate.

Over 100 years at 3%:
- Annual: $\$19.22$ per dollar.
- Monthly: $\$397.44$ per dollar.

The monthly compounding produces a final value over 20× the annual. For long horizons, compounding frequency matters substantially.

The **continuous compounding** formula uses the natural exponential:

$$FV = PV \times e^{r \cdot n}$$

This is the limiting case as compounding frequency goes to infinity. It comes up routinely in derivatives pricing (Chapter 20) and in some bond mathematics (Chapter 10).

### Refinement 2 — Nominal vs. real rates (the Fisher equation)

The interest rate quoted on most financial instruments is the **nominal rate** — the rate you actually receive in dollars. Inflation eats away at the real purchasing power of those dollars. The **real rate** is the nominal rate adjusted for inflation.

Approximate relationship:

$$\text{Real rate} \approx \text{Nominal rate} - \text{Inflation rate}$$

Exact relationship (the **Fisher equation**):

$$(1 + \text{Nominal rate}) = (1 + \text{Real rate}) \times (1 + \text{Inflation rate})$$

Solving for the nominal rate when real rate and inflation are known:

$$\text{Nominal} = (1 + \text{Real}) \times (1 + \text{Inflation}) - 1$$

For a 6% real rate and 2% expected inflation:

$$\text{Nominal} = 1.06 \times 1.02 - 1 = 0.0812 = 8.12\%$$

The approximation gives 8% (just adding 6% + 2%); the exact equation gives 8.12%. For most purposes the approximation is fine; for precise work — particularly with high inflation rates — use the Fisher equation.

For the project: when reading historical financial data, always check whether returns are quoted in nominal or real terms. Long-term equity return data (Chapter 12) is typically presented both ways. Real returns are what matter for purchasing power.

### Refinement 3 — The Rule of 72

A useful mental shortcut. The number of years for a quantity to double at a given growth rate is approximately:

$$n_\text{double} \approx \frac{72}{r}$$

where $r$ is the rate as a percentage (so 6% for a 6% growth rate).

| Rate | Doubling time |
|---|---|
| 2% | 36 years |
| 4% | 18 years |
| 6% | 12 years |
| 8% | 9 years |
| 12% | 6 years |
| 24% | 3 years |

The rule comes from the fact that $\ln(2) / \ln(1+r) \approx 72/r$ for small r. It's accurate to within a fraction of a year for rates between 2% and 12%, and good enough for back-of-the-envelope thinking elsewhere.

Applications:

- **GDP growth.** The US economy grew at about 2% real per year for most of the 20th century. By the rule of 72, GDP doubles every 36 years — and indeed it did, roughly four times during the century.
- **Inflation.** At 3% inflation, prices double every 24 years. At 7% inflation, prices double every 10.3 years. The pre-1980 period had inflation that doubled prices repeatedly within a generation.
- **Credit card APR.** At 24%, balances double every 3 years if you make minimum payments. This is why credit-card debt is genuinely dangerous.
- **Population.** At 2% growth, a population doubles every 36 years. This is why demographic projections matter.

The rule works for any growing or shrinking quantity — population, GDP, inflation, debt — not just investment returns. It is the most useful one-line shortcut in finance.

### The trade-off (concept 3)

Refinements trade **precision against simplicity**. The basic $FV = PV(1+r)^n$ is intuitive and gets you 90% of the way there. Compounding frequency, Fisher adjustment, and continuous compounding handle the remaining 10% — important for precise work but unnecessary for first-pass thinking. The Rule of 72 trades exactness for usability and is invaluable for quick estimation.

### Worked example — comparing two real-world investment options

A simple investment decision the project will engage with. Two ways to put $10,000 to work for 20 years:

**Option A**: A 20-year Treasury bond yielding 4.5% nominal, semi-annual coupons (effectively semi-annual compounding when reinvested).
$$FV_A = 10{,}000 \times \left(1 + \frac{0.045}{2}\right)^{40} = 10{,}000 \times (1.0225)^{40} = \$24{,}376$$

**Option B**: An equity index fund with expected return of 7% nominal, dividends reinvested (effectively annual compounding for our purposes).
$$FV_B = 10{,}000 \times (1.07)^{20} = \$38{,}697$$

The expected difference is about $14,000 over 20 years. But Option B's actual outcome could range from about $22,000 (if returns underperform expectations) to $65,000 or more (if they outperform). Option A's outcome is essentially fixed at $24,376 (assuming the Treasury doesn't default).

The trade-off is the risk-return relationship from Chapter 1, made arithmetically concrete. Higher expected return; higher variability. The right choice depends on what the money is for and the investor's tolerance for variance.

### Common misconceptions

- *"More frequent compounding is always meaningfully better."* It's better, but the difference between monthly and annual compounding is usually under 1% per year. Don't agonize over compounding frequency unless rates or time horizons are extreme.
- *"Real rates are usually positive."* Not always. In some recent periods (2010s, briefly in 2020), real Treasury rates were negative because inflation exceeded nominal yields. Holders of cash and Treasuries lost purchasing power.

---

## Synthesis — TVM as the language of finance

Three concepts, one formula, four directions of use. The master formula:

$$FV = PV \times (1+r)^n$$

This is the spine of the time value of money. Compound forward to project a present sum into the future. Discount backward to express a future sum in today's dollars. Solve for r to find the implied return. Solve for n to find the required horizon. Adjust for compounding frequency when needed. Adjust for inflation using the Fisher equation when nominal vs. real distinction matters. Use the Rule of 72 for quick estimation.

This chapter handled single payments. Most real cash flows come in streams — annuities, mortgages, bond coupons, dividend streams. Chapter 8 extends the same logic to streams of equal payments. Chapter 9 extends to streams of unequal payments. Chapter 10 uses the result to price bonds. Chapter 11 uses it to price stocks via discounted cash flow.

For the project, the deliverable from this chapter is a working facility with the four directions of TVM. By the end of Chapter 9, you'll be able to discount any cash flow stream to a present value — the foundation of equity valuation.

---

## Exercises

### Warm-up

**7.1** State the master TVM formula. Define each of the four variables.

**7.2** State the three reasons money has time value. Which is most important from a finance perspective?

**7.3** Use the Rule of 72 to estimate doubling times at 3%, 6%, 9%, and 12%.

### Application

**7.4** Compute:

(a) FV of $5,000 invested at 7% for 25 years.
(b) PV of $100,000 needed in 15 years at a 6% discount rate.
(c) The interest rate that turns $10,000 into $25,000 over 12 years.
(d) The number of years for $50,000 to grow to $200,000 at 8%.

**7.5** Using the Fisher equation, compute the nominal rate required to deliver a 4% real return when inflation is expected to be 3.5%. Compare to the simple approximation.

**7.6** A $1,000 deposit at 5% nominal annual rate, compounded:
(a) Annually
(b) Quarterly
(c) Monthly
(d) Daily

Compute the future value after 1 year and after 30 years for each compounding frequency. By what percentage do the 30-year values differ between annual and daily compounding?

### Synthesis

**7.7** Two friends each save for retirement. Friend A starts at age 22, contributes $5,000 per year for 9 years (ages 22–30), and then stops contributing but lets the balance compound. Friend B starts at age 30, contributes $5,000 per year for 35 years (ages 30–65). Both earn 8% per year. At age 65:

(a) How much has each friend contributed in total?
(b) What is each friend's balance?
(c) Explain the difference in plain English. What does this tell you about the value of starting early vs. contributing more?

**7.8** Use TVM to evaluate one of your chosen company's recent decisions. Pick a major capital expenditure announced in the last 12 months — a factory, an acquisition, a major tech investment. Estimate the present value of the cash outflow at the time of the announcement (it may already be in present dollars if paid up front, or may need to be discounted if paid over time). Compare to the firm's market cap. Is this a material commitment? What discount rate would you use, and why?

### Challenge

**7.9** Inflation runs at 3% per year for 50 years. Use the Rule of 72 and the exact compound formula to compute (a) how much purchasing power is lost over the period, and (b) what nominal return an investor needs to earn just to break even on purchasing power. Compare to historical data on long-run inflation and equity returns from Chapter 12 (you can preview the data on FRED).

**7.10** A company offers two compensation packages:
- Package A: $80,000 per year for 4 years.
- Package B: $50,000 per year for the first 4 years and a guaranteed $200,000 bonus at the end of year 4.

Assume your discount rate is 6%. Which is the better deal? Now consider how your answer changes if the discount rate is 12%. What does the sensitivity tell you about the role of the discount rate in financial decisions?

---

## Chapter summary

- Money has time value because (1) money invested today earns a return; (2) future payments carry default risk; (3) people prefer present consumption.
- The master formula: $FV = PV \times (1+r)^n$. Four variables; given any three, you can solve for the fourth.
- **Compounding** (forward in time) and **discounting** (backward in time) are the same operation in opposite directions.
- More frequent compounding produces higher future values; the effect is small over short horizons and substantial over long ones.
- The **Fisher equation** $(1 + r_\text{nominal}) = (1 + r_\text{real}) \times (1 + \text{inflation})$ links nominal and real rates exactly. The simple subtraction is a useful approximation.
- The **Rule of 72** estimates doubling time as $72/r$ for any growth rate.

---

## What would change my mind

The chapter argues that the single-payment TVM formula is the foundation of all financial valuation, and that mastering its four directions is the foundational quantitative skill of the field. The reading would have to revise if (a) a non-discount-based approach to valuation became the dominant practice — some heterodox economists argue against discounting, particularly for long-horizon environmental and intergenerational decisions, but these debates haven't displaced the TVM framework in finance, or (b) the assumption that money has time value broke down in some persistent way — negative real interest rates over a sustained period would do this, and we've had brief episodes (2010s, briefly 2020), but not persistent ones.

## Still puzzling

The genuinely hard question this chapter sets up but doesn't resolve is *what discount rate to use*. The formula $PV = FV/(1+r)^n$ is mechanical; the choice of $r$ is judgment-laden. Should I discount future cash flows of a startup at the same rate as future cash flows of the US government? Obviously not — the risk is different. But how much different, and how do I quantify it? That question is the engine of Chapters 11 (DCF), 14 (CAPM and beta), and 17 (WACC). The TVM machinery is precise; what we put into the machinery is approximate. Honest analysts say so explicitly when they present valuations.

---

## Connections forward

- **Chapter 8** extends to streams of equal payments (annuities, perpetuities).
- **Chapter 9** handles arbitrary cash flow streams.
- **Chapter 10** uses TVM to price bonds.
- **Chapter 11** uses TVM (via DCF) to value stocks.
- **Chapter 16** uses TVM to evaluate corporate capital projects (NPV, IRR).
- **Chapter 17** computes WACC — the discount rate the firm itself uses.

---

---

## LLM Exercise — Chapter 7: Discount a Known Future Cash Flow

**Project:** Equity Research Report on a Chosen Public Company
**What you're building this chapter:** Apply single-payment TVM to a real future cash flow your company has — a bond maturity, a known capex commitment, or a contractual receivable.
**Tool:** Claude chat (with the 10-K's debt or commitments footnote handy).

### The Prompt

```
For [your company], identify three specific known future cash flows from the 10-K's debt footnote or commitments disclosure. Examples:
- A bond maturity (face value due on a specific date)
- A capital lease payment due in a specific year
- A long-term debt installment with a known schedule
- A scheduled dividend payment

For each cash flow:

1. State the dollar amount and the date due.

2. Compute its present value at three different discount rates:
   - The risk-free rate (use the current 10-year Treasury yield, e.g., 4.5%)
   - The firm's cost of debt (use the YTM of one of its bonds, or 5-6% if not available)
   - A higher rate reflecting equity risk (e.g., 9%)

3. Compare the three present values. By how much does the choice of discount rate change the answer?

4. For one of the cash flows, also compute: how many years until the present value falls below 50% of the future amount, at the firm's cost of debt?

Show your arithmetic. Use the formula PV = FV / (1+r)^n.
```

### What this produces

A 1-page exercise demonstrating how the choice of discount rate affects valuation. Builds intuition for the DCF work coming in Chapter 11.

### How to adapt this prompt

- *For your own company:* Replace [your company]. If your firm has no scheduled debt maturities, use a known capex commitment or operating lease.
- *For ChatGPT / Gemini:* Identical.
- *For Claude Code:* Could write a small Python script for the calculations, but Excel works fine.

### Connection to previous chapters

Builds on Chapter 5's statement reading and Chapter 6's TIE (which depends on interest expense, which depends on these debt schedules).

### Preview of next chapter

Chapter 8 extends to streams of equal payments — annuities and perpetuities. The Chapter 8 LLM Exercise will value your company's dividend stream as an annuity or perpetuity.

---

**Tags:** time-value-of-money, future-value, present-value, compounding, discounting, Fisher-equation, Rule-of-72


---

## AI Wayback Machine

**Leonardo Fibonacci** was introduced the Hindu-Arabic numeral system to Europe in 1202 — and his Liber Abaci taught medieval merchants to compute compound interest.

**Run this:**

```
Who is Leonardo Fibonacci, and how does their work connect to time value of money we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about their career or ideas.
```

→ Search **"Leonardo Fibonacci"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to apply Leonardo Fibonacci's framework to a specific finance question.
- Add a constraint: "Answer including criticisms or limits of Leonardo Fibonacci's framework."

What changes? What gets better? What gets worse?
