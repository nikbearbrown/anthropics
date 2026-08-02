# Chapter 7 — Time Value of Money I: Single Payment Value
*One formula. Four directions. The arithmetic spine of every valuation in this book.*

---

## The puzzle of two offers

A relative offers you a deal. They have $10,000 to give you. Two options:

- **Option A** — they hand you $10,000 today.
- **Option B** — they promise $11,000 two years from now, in writing, guaranteed.

Most people sense Option B might be better — it's more money. But that intuition is incomplete, because the right answer depends entirely on something the question doesn't tell you: *what would you do with the $10,000 in the meantime?*

If you'd put it in a savings account at 2% per year, today's $10,000 grows to $10,000 × (1.02)² = $10,404 in two years. Option B's $11,000 beats that. Take Option B.

If you'd invest it in something earning 6% per year, today's $10,000 grows to $10,000 × (1.06)² = $11,236 in two years. Option B no longer wins. Take Option A.

If you'd earn exactly 4.88%, the two options are tied: $10,000 × (1.0488)² ≈ $11,000. That's the breakeven rate — the rate at which today's money would grow to exactly match the future offer. Above that rate, today is better. Below it, the future is better.

This is not a trick. This is the entire field of finance, in miniature. Money has a time value because money you have today can be invested, and invested money grows. The question is never "which is more dollars?" It's always "at what rate would you invest the present amount, and does the future offer beat that?"

---

## Why money has time value

Three reasons, in order of importance.

**First: money invested today earns a return.** A dollar in your pocket can be deposited, lent, or invested — and at some future point you'll have more than a dollar. A dollar arriving in the future cannot have been earning anything in the meantime. The present dollar is worth more than the future dollar by exactly the return you would have earned on it. This is the dominant reason, and it's purely mechanical.

**Second: future payments are uncertain.** Even if someone promises you $11,000 in two years, something might prevent delivery. The counterparty might fail. The country might experience inflation that shrinks purchasing power. Default risk makes future dollars worth less than present dollars for reasons beyond opportunity cost.

**Third: people prefer present consumption.** Most people would rather have something now than wait for the same thing later, even absent any investment opportunity or default risk. This is real but it's the softest of the three. For this book, when we say "money has time value," we mostly mean the first reason: present money can be invested.

---

## The master formula

Suppose you put $1,000 into a savings account paying 4% interest per year.

After one year: $1,000 × 1.04 = $1,040. Straightforward.

After two years: $1,040 × 1.04 = $1,081.60.

Notice that $1,081.60 is not $1,080. The extra $1.60 comes from the fact that in year 2 you earned 4% not on your original $1,000 but on $1,040 — you earned interest on your interest. This is **compound interest**, and it is the engine of everything that follows.

The general formula. If you start with **PV** (present value), invest at rate **r** per period, and let it compound for **n** periods:

$$FV = PV \times (1+r)^n$$

Read it: the future value equals the present value, scaled up by the factor $(1+r)^n$. That factor is always greater than 1 when $r > 0$, and it grows exponentially with $n$.

What does "exponentially" actually mean here? Work through a few values:

<!-- → [TABLE: $1,000 at 4% compounded annually — rows for n = 1, 5, 10, 20, 30, 50 years — columns: years, future value, multiplier (FV/1000) — student should see the multiplier start small and accelerate; annotate where the curve starts to feel "fast"] -->

Three years at 4% gives about $1,125. Ten years gives about $1,480. Fifty years gives about $7,107. The first ten years add about $480. The next forty years add another $5,627.

That asymmetry is the whole story of compounding. Each year, you earn 4% on a base that is slightly larger than the year before. The growth in the base is small at first and large later. Plot the formula as a curve and you get a shape that looks nearly flat for decades and then bends sharply upward. The bend is not a trick; it's arithmetic.

This is why financial advice for young people emphasizes starting early. Two friends, both starting at 22:

- **Friend A** invests $5,000 per year from age 22 to 30 (nine years), then stops. Lets the balance compound at 8%.
- **Friend B** waits until 30, then invests $5,000 per year all the way to 65 (thirty-five years) at the same 8%.

At age 65, Friend A has contributed about $45,000 total. Friend B has contributed about $175,000. Yet their ending balances are nearly equal — Friend A's, in fact, is slightly higher.

The early dollars got more years of compounding. The late dollars, no matter how numerous, couldn't catch up.

<!-- → [CHART: Side-by-side bar chart comparing Friend A and Friend B at age 65 — show total contributions (shaded one color) versus total growth (shaded another) for each friend; student should see that Friend A's growth dwarfs contributions while Friend B's balance is more evenly split, making the power of early compounding viscerally visible] -->

↳ **Dig Deeper — Negative interest rates**

*Standard TVM assumes positive interest rates. But several countries — Japan, Switzerland, the Eurozone — have at various times had negative nominal policy rates. Some Treasury yields have gone negative in real terms even more often. What does the formula produce when r < 0?*

**Prompt:**
> Explain the mechanics of negative interest rates as observed in Japan (since 2016), Switzerland, and the Eurozone. What does the standard TVM formula produce when r < 0? Then describe two real economic phenomena that emerge under negative-rate conditions: (1) why some firms accumulate cash rather than borrowing, even at negative cost, and (2) what happens to the present value of long-dated future cash flows when rates are negative.

**What to do with the output:** Save it. The standard TVM intuition assumes rates are positive; understanding the edge case sharpens the standard reasoning.

---

## The formula has four directions

The master formula has four variables: PV, FV, r, n. Given any three, solve for the fourth. That single equation generates four kinds of problems, and equity analysts work all four of them constantly.

### Compound forward: finding future value

You know PV, r, n. You compute FV.

This is the formula as written. Put $25,000 in a retirement account earning 7% for 30 years:

$$FV = 25{,}000 \times (1.07)^{30} = \$190{,}306$$

A $400,000 house appreciating at 4% per year for 6 years:

$$FV = 400{,}000 \times (1.04)^6 = \$506{,}128$$

In Excel: `=FV(0.07, 30, 0, -25000)` returns 190,306. The negative sign on PV follows Excel's sign convention — money flowing out (your deposit) is negative; money flowing in (your future balance) is positive.

### Discount backward: finding present value

You know FV, r, n. You compute PV. Rearrange:

$$PV = \frac{FV}{(1+r)^n}$$

The factor $1/(1+r)^n$ is called the **discount factor**. It is always less than 1 for positive r — meaning a future dollar is always worth less than a present dollar.

<!-- → [TABLE: Present value factors at three discount rates (4%, 7%, 10%) for n = 1, 5, 10, 20, 30 years — student should see how quickly high discount rates compress distant future values toward zero] -->

A $50,000 lottery payout in 5 years, discounted at 5%:

$$PV = \frac{50{,}000}{(1.05)^5} = \$39{,}176$$

A "$1,000 savings bond" gifted to a child, maturing in 30 years, discounted at 5%:

$$PV = \frac{1{,}000}{(1.05)^{30}} = \$231$$

That savings bond is worth $231 the day you buy it, not $1,000. The face value is a future value. The present value is what you're actually giving.

The discount rate matters enormously here. A future $1 million discounted at 5% over 30 years is worth $231,377 today. The same $1 million discounted at 8% is worth only $99,377. The discount rate can more than double or halve the valuation of the same cash flow. This is why equity research analysts argue so intensely about discount rates — the answer is highly sensitive to the choice, and the choice requires judgment that the formula cannot provide.

### Solve for the rate: what return is implied?

You know PV, FV, n. You compute r. Rearrange:

$$r = \left(\frac{FV}{PV}\right)^{1/n} - 1$$

A house bought for $300,000 and sold for $450,000 ten years later:

$$r = \left(\frac{450{,}000}{300{,}000}\right)^{1/10} - 1 = 1.5^{0.1} - 1 = 4.14\%$$

Decent but not spectacular — roughly on par with inflation during many periods.

College tuition of $5,000 per year in 1985 and $25,000 per year in 2025:

$$r = \left(\frac{25{,}000}{5{,}000}\right)^{1/40} - 1 = 5^{0.025} - 1 = 4.13\%$$

Tuition inflation has run at about 4% real per year — meaningfully above general inflation. This is one reason why college affordability is a recurring concern: the cost has compounded faster than most families' incomes.

In Excel: `=RATE(nper, pmt, pv, fv)`.

### Solve for time: how long until?

You know PV, FV, r. You compute n. Take logs of both sides of the formula:

$$n = \frac{\ln(FV/PV)}{\ln(1+r)}$$

A $25,000 college fund needs to reach $50,000. At 7%:

$$n = \frac{\ln(2)}{\ln(1.07)} = \frac{0.6931}{0.0677} = 10.24 \text{ years}$$

A retirement account at $250,000 needs to reach $1 million. At 8%:

$$n = \frac{\ln(4)}{\ln(1.08)} = 18.0 \text{ years}$$

In Excel: `=NPER(rate, pmt, pv, fv)`.

---

## A worked example: Apple's cash pile

Apple holds roughly $191 billion in cash and short-term investments. Suppose — purely as a thought experiment — that money sat in a bank account earning 4% (current short-term rates) for 30 years and was never deployed for buybacks, dividends, or acquisitions. What would it be worth?

$$FV = 191{,}000 \times (1.04)^{30} = 191{,}000 \times 3.243 \approx \$619 \text{ billion}$$

That calculation makes Apple's capital-allocation decisions legible. Holding cash earns the risk-free rate. Investing it productively — in R&D, capex, or returning to shareholders — might earn substantially more. Whether Apple's $191 billion is well-deployed depends entirely on the alternatives available to the firm. Chapter 17 examines that question quantitatively.

---

## Three refinements

The master formula assumes annual compounding. Reality is messier in three ways worth addressing.

### Compounding frequency

Most financial instruments compound more than once per year. The adjusted formula:

$$FV = PV \times \left(1 + \frac{r}{m}\right)^{m \cdot n}$$

where $m$ is the number of compounding periods per year and $r$ is the stated annual rate.

Compare $1,000 at 6% for one year at different frequencies:

<!-- → [TABLE: Compounding frequency comparison — rows: Annual, Quarterly, Monthly, Daily, Continuous — columns: formula applied, FV after 1 year, FV after 30 years — student should see that the 1-year difference is trivial but the 30-year difference is substantial] -->

At one year: annual gives $1,060.00; monthly gives $1,061.68; continuous gives $1,061.84. The difference is under $2. Barely matters.

At 30 years: annual gives $5,743; monthly gives $6,023. A $280 gap per original $1,000. Matters more as the horizon grows.

The **continuous compounding** formula uses the natural exponential:

$$FV = PV \times e^{r \cdot n}$$

This is the limiting case as $m \to \infty$. It comes up in derivatives pricing (Chapter 20) and some bond mathematics (Chapter 10). For most corporate-finance work, annual or semi-annual compounding is close enough.

### Nominal vs. real rates

The interest rate quoted on most instruments is the **nominal rate** — the rate you actually receive in dollars. Inflation eats away at the real purchasing power of those dollars. The **real rate** is the nominal rate adjusted for inflation.

Approximate relationship:

$$\text{Real rate} \approx \text{Nominal rate} - \text{Inflation rate}$$

Exact relationship (the **Fisher equation**):

$$(1 + r_\text{nominal}) = (1 + r_\text{real}) \times (1 + \pi)$$

For a 6% real rate target and 2% expected inflation:

$$r_\text{nominal} = (1.06)(1.02) - 1 = 8.12\%$$

The simple approximation gives 8%. The exact equation gives 8.12%. For low inflation rates the approximation is fine. For high inflation — think the 1970s, or certain emerging markets — use the exact formula.

For the equity research project: long-term equity return data is typically presented both in nominal and real terms. Real returns are what matter for purchasing power. When you see a historical return of "10% per year," check whether that's nominal or real before drawing conclusions.

### The Rule of 72

A useful mental shortcut. The number of years for a quantity to double at a given growth rate is approximately:

$$n_\text{double} \approx \frac{72}{r}$$

where $r$ is the rate as a percentage.

At 6%, money doubles in approximately 12 years. At 8%, about 9 years. At 24% — typical credit-card APR — outstanding balances double in about 3 years if you make only minimum payments.

The rule derives from the fact that $\ln(2) / \ln(1+r) \approx 72/r$ for small $r$. It's accurate to within a fraction of a year for rates between 2% and 12%, and useful for back-of-the-envelope thinking everywhere else.

The rule applies to any growing quantity — not just investment returns. US GDP growing at 2% real doubles every 36 years. Inflation at 3% doubles prices every 24 years. A population growing at 2% per year doubles every 36 years. Once you know the rule, you start seeing compounding everywhere.

<!-- → [TABLE: Rule of 72 reference table — rows for rates 1%, 2%, 3%, 4%, 6%, 8%, 10%, 12%, 18%, 24%, 36%, 72% — columns: rate, approximate doubling time (72/r), exact doubling time (ln2/ln(1+r)), real-world example at that rate (GDP, inflation, credit card, etc.) — student should internalize the table as a mental shortcut they use for the rest of the course] -->

↳ **Dig Deeper — The social discount rate for environmental decisions**

*When economists value future benefits of climate action against present costs, the discount rate determines almost everything. A 1% rate weights our great-grandchildren's welfare nearly as heavily as our own. A 5% rate barely weights it at all. The Stern Review (2006) and Nordhaus's DICE model use very different rates — and arrive at very different policy conclusions.*

**Prompt:**
> Explain why the social discount rate matters so much for cost-benefit analysis of long-horizon environmental decisions. Compare the rates used by Nordhaus's DICE model (around 4–5%) and the Stern Review (1.4%). What's the philosophical argument for a lower social discount rate? What's the argument against? Then summarize what current US government cost-benefit analysis (under OMB Circular A-4) actually uses.

**What to do with the output:** Save it. The TVM machinery applies directly; the choice of rate is where contested values enter.

---

## Putting it together: two investment options

A simple decision that the equity research project will engage with directly. Two ways to invest $10,000 for 20 years:

**Option A**: A 20-year Treasury bond yielding 4.5% nominal, with semi-annual coupons reinvested:

$$FV_A = 10{,}000 \times \left(1 + \frac{0.045}{2}\right)^{40} = 10{,}000 \times (1.0225)^{40} = \$24{,}376$$

**Option B**: An equity index fund with expected return of 7% nominal, dividends reinvested:

$$FV_B = 10{,}000 \times (1.07)^{20} = \$38{,}697$$

The expected difference is about $14,000. But Option B's actual outcome could range from roughly $22,000 (if returns disappoint) to $65,000 or more (if they outperform). Option A's outcome is essentially fixed at $24,376, assuming the Treasury doesn't default.

<!-- → [CHART: Fan chart showing Option B's distribution of possible 20-year outcomes as a cone of uncertainty, with Option A's $24,376 shown as a fixed horizontal endpoint — student should see both the expected advantage of equities and the width of the uncertainty band around it] -->

This is the risk-return trade-off from Chapter 1, made arithmetically concrete. The TVM formula doesn't make the choice for you. It makes the stakes of the choice visible.

---

## What the formula can't do

The master formula $FV = PV(1+r)^n$ assumes a constant rate over the entire horizon, no taxes, no inflation adjustments, no defaults, no withdrawals. Real-world investing has all of these. The formula is the right starting point because it isolates the single most important effect — compounding — and shows it clearly. The refinements come later: Chapter 8 for streams of equal payments, Chapter 13 for return variability, Chapter 17 for the risk-adjusted rate the firm itself uses.

The genuinely hard question the formula sets up but cannot answer is: *what discount rate do I use?* The arithmetic of $PV = FV/(1+r)^n$ is precise; the choice of $r$ is judgment-laden. Should I discount a startup's future cash flows at the same rate as the US government's? Obviously not. But how much higher, and on what basis? That question drives Chapters 11, 14, and 17. The TVM machinery is exact. What we feed into the machinery is approximate. Honest analysts say so.

---

## What would change my mind

The chapter argues that the single-payment TVM formula is the foundational quantitative tool of finance, and that mastering its four directions builds the arithmetic spine for everything that follows. The reading would have to revise if a non-discount-based approach to valuation became dominant practice — some heterodox economists argue against discounting for long-horizon environmental decisions, and the debate is real. But those debates haven't displaced the TVM framework inside finance. The deeper challenge is persistent negative real interest rates: if the assumption that money earns a positive real return over time breaks down sustainably, the whole intuition of "present is worth more than future" inverts. We've had brief episodes. We haven't had a sustained breakdown.

## Still puzzling

The hardest thing this chapter sets up but doesn't resolve is the discount rate choice. The formula is clean. The rate is contested. For a startup, should I use 12%? 20%? 40%? The answer changes the present value by an order of magnitude over a 30-year horizon. The field has frameworks — CAPM in Chapter 14, WACC in Chapter 17 — that give you a principled method. But every framework requires inputs that are themselves estimated, and the estimates carry their own uncertainty. Valuations are sensitive to the discount rate in a way that should make anyone presenting a single-number DCF uncomfortable. Chapter 11 will return to this explicitly.

---

## Connections forward

- **Chapter 8** extends to streams of equal payments — annuities and perpetuities.
- **Chapter 9** handles arbitrary cash flow streams.
- **Chapter 10** prices bonds using TVM.
- **Chapter 11** values stocks via discounted cash flow.
- **Chapter 16** evaluates corporate capital projects using NPV and IRR.
- **Chapter 17** computes WACC — the discount rate the firm itself uses.

---

## Exercises

### Warm-up

**7.1** State the master TVM formula. Define each of the four variables in one sentence each. Then explain in plain English what the factor $(1+r)^n$ is actually doing to the present value.

**7.2** State the three reasons money has time value and rank them by importance for corporate finance. In one sentence, explain why the dominant reason is "purely mechanical."

**7.3** Use the Rule of 72 to estimate doubling times at 2%, 4%, 6%, 8%, and 12%. Then verify one of them with the exact formula $n = \ln(2)/\ln(1+r)$. How close is the approximation?

### Application

**7.4** Compute the following. Show the formula setup and the arithmetic for each.

(a) FV of $8,000 invested at 6% for 20 years.
(b) PV of $150,000 to be received in 12 years at a 7% discount rate.
(c) The annual interest rate that turns $12,000 into $30,000 over 9 years.
(d) The number of years for $40,000 to grow to $160,000 at 6%.

**7.5** Using the Fisher equation, compute the nominal rate required to deliver a 3.5% real return when expected inflation is 4%. Compare to the simple approximation of adding the two rates. By how many basis points does the approximation understate the exact answer?

**7.6** You invest $2,000 at a 6% stated annual rate. Compute the future value after 1 year and after 40 years under:

(a) Annual compounding.
(b) Monthly compounding.
(c) Continuous compounding ($FV = PV \times e^{rn}$).

By what percentage does 40-year continuous compounding exceed 40-year annual compounding? Why is the gap so much larger at 40 years than at 1 year?

### Synthesis

**7.7** Return to the Friend A / Friend B illustration. Verify both ending balances numerically at 8% compounded annually. (Hint: treat each year's $5,000 contribution as a separate single payment that compounds for its own number of years, then sum them.) What is the exact difference in their age-65 balances? What does the difference represent in terms of the cost of waiting?

**7.8** A future $1 million cash flow is to be received in 25 years.

(a) Compute its present value at discount rates of 3%, 6%, 9%, and 12%.
(b) Which rate cuts the present value roughly in half compared to the 3% base case?
(c) An analyst presents a single-number DCF valuation to a client and uses an 8% discount rate. A colleague argues it should be 10%. Using your results from (a), estimate what percentage of the stated value the disagreement would destroy. What does this tell you about the stakes of discount rate debates?

### Challenge

**7.9** Tuition at a selective US university was approximately $5,000 per year in 1975 and approximately $60,000 per year in 2025. Use the implied-rate formula to compute the compound annual growth rate of tuition over this period. Then compute what tuition would be in 2045 if that rate continues. Compare your 2045 figure to median US household income growth over the same 1975–2025 period (look it up or use an estimate of roughly 2% real). What does the comparison suggest about the long-run trajectory of college affordability?

**7.10** The two-offer puzzle at the opening of this chapter has a breakeven rate of approximately 4.88%. Solve for this exactly using the formula, then explain: if your personal opportunity cost — the return you could actually earn on the money — is unknown, how would you use the breakeven rate as a decision tool? Give a concrete example of a situation where knowing the breakeven rate is more useful than knowing the discount rate itself.

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

## AI Wayback Machine

**Leonardo Fibonacci** introduced the Hindu-Arabic numeral system to Europe in 1202 — and his *Liber Abaci* taught medieval merchants to compute compound interest.

**Run this:**

```
Who is Leonardo Fibonacci, and how does their work connect to time value of money we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about their career or ideas.
```

→ Search **"Leonardo Fibonacci"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to apply Fibonacci's historical context to a specific finance question.
- Add a constraint: "Answer including criticisms or limits of Fibonacci's framework."

What changes? What gets better? What gets worse?

---

**Tags:** time-value-of-money, future-value, present-value, compounding, discounting, Fisher-equation, Rule-of-72
