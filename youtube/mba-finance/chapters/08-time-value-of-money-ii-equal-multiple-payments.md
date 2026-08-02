# Chapter 8 — Time Value of Money II: Equal Multiple Payments

*How an infinite stream of payments adds up to something you can hold in your hand.*

---

Here is a thing that seems impossible.

Suppose someone promises to pay you $1 every year, forever. Not for a hundred years. Not for a thousand. *Forever.* An infinite number of payments, each worth something, stretching out to the end of time.

What is that promise worth today?

Your first instinct might be: infinitely much. An infinite number of positive-valued payments — the sum ought to be infinite. But the promise is not worth infinite money. It is worth a perfectly specific, finite, calculable number. And the reason comes down to a fact about the future that we established in Chapter 7: a dollar far enough away is worth almost nothing today.

A $1 payment fifty years from now, discounted at 5%, has a present value of $0.087 — less than nine cents. A $1 payment a hundred years from now has a present value of $0.0076 — less than a penny. Two hundred years away: a hundredth of a cent. The payments keep shrinking toward zero fast enough that their infinite sum converges to a finite number. This is the same phenomenon that lets a geometric series — $1 + \frac{1}{2} + \frac{1}{4} + \frac{1}{8} + \cdots$ — add up to exactly 2, not infinity, even with infinitely many terms.

That finite number is where this chapter begins.

---

## Perpetuities: the infinite stream

A **perpetuity** is a constant payment $C$ received every period, starting one period from now, forever. The present value is:

$$PV = \frac{C}{(1+r)^1} + \frac{C}{(1+r)^2} + \frac{C}{(1+r)^3} + \cdots = \sum_{n=1}^{\infty} \frac{C}{(1+r)^n}$$

To evaluate this sum, use the geometric-series trick. Call the sum $PV$. Multiply both sides by $(1+r)$:

$$PV \cdot (1+r) = C + \frac{C}{(1+r)^1} + \frac{C}{(1+r)^2} + \cdots$$

Subtract the original equation:

$$PV \cdot (1+r) - PV = C - \lim_{n \to \infty} \frac{C}{(1+r)^n} = C - 0$$

$$PV \cdot r = C$$

$$\boxed{PV = \frac{C}{r}}$$

One of the cleanest results in finance. The present value of a constant stream that pays forever is just the payment divided by the discount rate. No exponents. No compounding schedules. One division.

Notice what drives the formula. Higher payments mean higher present value — obvious. Higher discount rates mean lower present value — also obvious. But the relationship is exactly inverse: double the rate, halve the value. This is the same mechanism that makes long-duration bonds sensitive to interest rate changes, as we'll see in Chapter 10.

**Preferred stock as a perpetuity.** A corporation sometimes issues preferred stock that pays a fixed dividend indefinitely. If the dividend is $2.00 per share annually and investors require a 7% return:

$$PV = \frac{\$2.00}{0.07} = \$28.57$$

That's the price investors will pay. For every $28.57 invested, they receive $2.00 per year — exactly a 7% return.

Now suppose interest rates rise and the required return becomes 10%:

$$PV = \frac{\$2.00}{0.10} = \$20.00$$

The stock price falls from $28.57 to $20.00 — a 30% drop — with no change in the underlying dividend. This is why bond and preferred-stock prices fall when interest rates rise. The mechanism is in the formula.

<!-- → [CHART: line chart showing how PV = C/r behaves as r rises from 2% to 15% for a fixed C = $2.00 — student should see the hyperbolic relationship and why small changes in r at low rates produce large changes in price] -->

**Growing perpetuities.** What if the payment grows at a constant rate $g$ each period? The first payment is $C$, the second is $C(1+g)$, the third $C(1+g)^2$, and so on. Apply the same telescoping trick — the sum converges as long as $r > g$, and the result is:

$$\boxed{PV = \frac{C}{r - g}}$$

If $r \leq g$, the formula breaks down — the stream grows too fast for discounting to cap it, and the sum diverges. This constraint ($r > g$) is not just mathematical; it is economic. A firm cannot grow faster than the economy forever without eventually *being* the economy. The condition is a sanity check built into the formula.

Example: a college endowment pays $4.00 per share annually to a charitable beneficiary, with payments growing at 0.2% per year, and the required return is 3%:

$$PV = \frac{\$4.00}{0.03 - 0.002} = \frac{\$4.00}{0.028} = \$142.86$$

Without growth, the same cash flow at 3% would be worth $\$4.00 / 0.03 = \$133.33$. A modest 0.2% growth rate adds about $9.50 to present value — roughly 7%. Growth matters more than it looks, because it persists forever.

This formula is the Gordon growth model for stock valuation, which we'll use in Chapter 11. If $D_1$ is next year's dividend and $g$ is the expected perpetual growth rate, then $P_0 = D_1 / (r - g)$. Everything in that model is right here in this section.

---

## Annuities: the finite stream

An **annuity** is like a perpetuity with an expiration date. Instead of paying forever, it pays for a fixed number of periods $n$ and then stops. Mortgages, car loans, pension payouts, and lottery prizes are all annuities.

Two timing conventions exist.

An **ordinary annuity** pays at the *end* of each period. You borrow money today; your first payment is one period later. Most loans work this way.

An **annuity due** pays at the *beginning* of each period. You sign a lease and pay January's rent on January 1, not January 31. Most rent and lease agreements work this way.

The difference is exactly one period of timing. Annuity due payments arrive one period earlier, so they're worth one period of compounding more. The relationship is simple:

$$PV_\text{due} = PV_\text{ordinary} \times (1+r) \qquad \text{and} \qquad FV_\text{due} = FV_\text{ordinary} \times (1+r)$$

I'll derive the ordinary annuity formulas; the annuity due versions follow by multiplying by $(1+r)$.

**Present value of an ordinary annuity.** There is a clever way to see the closed form without doing all the algebra: an ordinary annuity for $n$ periods is a perpetuity that starts today *minus* a perpetuity that starts $n$ periods from now.

The first perpetuity, valued today, is worth $C/r$. The delayed perpetuity is also worth $C/r$ from its future start — but discounted back to today is worth $(C/r)(1+r)^{-n}$. The difference is the annuity:

$$PV = \frac{C}{r} - \frac{C}{r}(1+r)^{-n} = \frac{C}{r}\left[1 - (1+r)^{-n}\right]$$

$$\boxed{PV = C \times \frac{1 - (1+r)^{-n}}{r}}$$

The bracketed term is the **present-value annuity factor** — a number that depends only on $r$ and $n$, not on $C$. Tables of these factors used to fill the appendix pages of finance textbooks; now you compute them with a single formula or Excel's `PV()` function.

<!-- → [TABLE: present-value annuity factors for selected rates (4%, 6%, 8%, 10%) and terms (5, 10, 20, 30 years) — student should notice how the factor grows much faster with term at low rates than at high rates] -->

**Future value of an ordinary annuity.** If the question runs the other direction — "if I save $C$ per period for $n$ periods, what will I have?" — compound each payment forward to period $n$:

$$\boxed{FV = C \times \frac{(1+r)^n - 1}{r}}$$

---

## The lottery, resolved

Back to the opening puzzle. North Dakota Lottery: $120,000 per year for 10 years (ordinary annuity), or $787,000 today as a lump sum.

At a 9% discount rate:

$$PV = \$120{,}000 \times \frac{1 - (1.09)^{-10}}{0.09} = \$120{,}000 \times 6.4177 = \$770{,}119$$

The lump sum ($787,000) is worth more by about $17,000. Take the cash.

At 6%:

$$PV = \$120{,}000 \times \frac{1 - (1.06)^{-10}}{0.06} = \$120{,}000 \times 7.3601 = \$883{,}210$$

Now the annuity is worth $96,000 more than the lump sum. Take the payments.

The crossover rate — where both options are equally valuable — sits around 8.1%. If you can earn more than 8.1% on your investments, take the lump sum. If not, take the payments.

The honest version: most people cannot guarantee themselves an 8.1% annual return after taxes. The lottery annuity provides a guaranteed 8.1% implied return on the spread-out payments, with zero risk. For someone without a high-confidence investment alternative, the annuity is probably the better choice. The formula doesn't tell you which to pick. It tells you what the pick depends on.

---

## Solving for any variable

The annuity formula has four variables: $PV$, $C$, $r$, $n$. Given any three, solve for the fourth.

**Solving for the payment** is how mortgage and car loan payments are computed. Rearrange for $C$:

$$C = PV \times \frac{r}{1 - (1+r)^{-n}}$$

Borrow $32,000 at 6% APR over 36 months. Monthly: $r = 0.005$, $n = 36$.

$$C = \$32{,}000 \times \frac{0.005}{1 - (1.005)^{-36}} = \$32{,}000 \times 0.030422 = \$973.50 \text{ per month}$$

Over 36 months you pay $35,046 total — meaning $3,046 in interest. That's 9.5% of the principal paid in interest charges.

**Solving for the term** — how long until a savings target is reached — requires logarithms or a numerical solver. Excel's `NPER()` function handles it directly.

**Solving for the rate** — what return does this investment implicitly promise? — generally has no closed form and requires numerical methods. Excel's `RATE()` and `IRR()` functions do this. We'll use them heavily in Chapter 16.

---

## Loan amortization: what's inside the payment

When you make a loan payment, part covers interest accrued during the period and part reduces the outstanding balance. Because interest accrues on the *remaining balance*, and the payment is constant, the split shifts over the loan's life. Early payments are heavily weighted toward interest; later payments toward principal.

For the $32,000 / 36-month / 6% car loan:

| Month | Payment | Interest | Principal | Remaining balance |
|---|---|---|---|---|
| 1 | $973.50 | $160.00 | $813.50 | $31,186.50 |
| 2 | $973.50 | $155.93 | $817.57 | $30,368.93 |
| 12 | $973.50 | $112.99 | $860.51 | $21,738.85 |
| 24 | $973.50 | $61.47 | $912.03 | $11,381.91 |
| 36 | $973.50 | $4.84 | $968.66 | $0.00 |
| **Total** | **$35,046** | **$3,046** | **$32,000** | |

In month 1, interest is 16% of the payment. By month 36, it's less than 1%.

The practical implication of this structure: prepaying principal early is disproportionately valuable. A $500 extra payment in year 1 reduces the balance on which future interest accrues, and those savings compound across the remaining life of the loan. A single extra payment early in a 30-year mortgage can eliminate several months of payments at the end.

<!-- → [CHART: stacked bar chart showing the interest vs. principal split for each payment of a 30-year mortgage — student should see how the bars flip from interest-heavy to principal-heavy and approximately where the crossover occurs] -->

On a 20-year, $140,000 mortgage at 3.6% APR, the monthly payment is $819.16. Total interest paid over the life of the loan: $56,598 — about 28% of the purchase price. A 30-year mortgage at the same rate has a lower monthly payment but costs more total interest, because the balance declines more slowly and interest accrues longer. Choosing between loan terms is choosing how to trade monthly cash flow against total interest cost. The amortization schedule makes that trade-off visible.

---

## Retirement planning: two annuities in sequence

Most retirement calculations are two successive annuity problems chained together.

**Accumulation phase.** Save $C$ per year for $n$ years at rate $r$:

$$FV = C \times \frac{(1+r)^n - 1}{r}$$

**Distribution phase.** Withdraw $W$ per month for $m$ months from a portfolio of size $FV$, at monthly rate $r_m$:

$$W = FV \times \frac{r_m}{1 - (1+r_m)^{-m}}$$

A 65-year-old retires with $750,000, plans withdrawals over 25 years, and the portfolio earns 5% annually. Monthly rate $\approx 0.00417$, $m = 300$:

$$W = \$750{,}000 \times \frac{0.00417}{1 - (1.00417)^{-300}} \approx \$4{,}385 \text{ per month}$$

About $52,600 per year. Whether that's enough depends on Social Security income, spending plans, and whether the retiree lives past 90 — all questions the formula forces you to state explicitly rather than handwave.

<!-- → [INFOGRAPHIC: two-phase timeline diagram for retirement planning — left phase shows annual contributions accumulating to FV at retirement date, right phase shows monthly withdrawals drawing down the same FV to zero; label both phases with their respective formulas and show how the retirement date is the hinge connecting them] -->

---

## Stated vs. effective interest rates

When a credit card says "1.5% per month," is the annual rate 18%?

Technically, 18% is the **stated annual rate** (also called APR) — the periodic rate times the number of periods. But interest compounds monthly. The cost of borrowing, after accounting for compounding, is the **effective annual rate (EAR)**:

$$\boxed{EAR = \left(1 + \frac{r_\text{stated}}{m}\right)^m - 1}$$

For 1.5% per month ($r_\text{stated} = 18\%$, $m = 12$):

$$EAR = (1.015)^{12} - 1 = 19.56\%$$

Not 18%. On a $10,000 balance carried for a year, that 1.56% gap is $156 in additional interest — real money.

For daily compounding at the same 18% APR:

$$EAR = \left(1 + \frac{0.18}{365}\right)^{365} - 1 \approx 19.72\%$$

Higher still. The more frequent the compounding, the higher the effective rate relative to the stated rate.

**Why this matters as an analyst.** When comparing instruments with different compounding frequencies, APRs cannot be compared directly. Convert to EAR first. A bond yielding 5% with annual coupons and a bond yielding 5% with quarterly coupons are not equally attractive — the quarterly one has an EAR of $(1.0125)^4 - 1 = 5.09\%$ and is marginally better.

**The extreme case.** A payday lender charges $14 to borrow $200 for one week — a 7% fee for one week. Rolled over weekly:

$$EAR = (1.07)^{52} - 1 = 3{,}370\%$$

The effective rate is over three thousand percent. The compounding machinery doesn't care about the loan's size or the borrower's desperation. The math is what it is.

<!-- → [TABLE: effective annual rates for common stated rates (12%, 18%, 24%) at monthly and daily compounding — student should see how EAR consistently and materially exceeds APR] -->

---

## The whole toolkit

This chapter added four pieces of machinery to Chapter 7's single-payment foundation.

The **constant perpetuity** ($PV = C/r$) values an infinite equal stream. The **growing perpetuity** ($PV = C/(r-g)$, with $r > g$) values an infinite growing stream — and is the mathematical core of dividend-discount stock valuation.

The **ordinary annuity** formulas value a finite equal stream in either direction: $PV = C \cdot \frac{1-(1+r)^{-n}}{r}$ and $FV = C \cdot \frac{(1+r)^n-1}{r}$. The **annuity due** variants multiply by $(1+r)$.

The **effective annual rate** ($EAR = (1 + r/m)^m - 1$) converts any stated rate to its true annual cost.

What the toolkit still can't handle: streams where the payments are unequal. Real capital projects. Real bonds with a terminal face-value payment. Real dividend streams that grow in stages before settling. Chapter 9 extends the framework to unequal payments with the NPV concept, and at that point the toolkit is complete.

For the equity research project, the machinery here is already at work. Bond valuation (Chapter 10) prices the coupon stream with an annuity formula and the principal repayment with a single-payment formula. Stock valuation (Chapter 11) applies the growing perpetuity formula to dividends. The arithmetic is exactly what's on this page.

---

## Exercises

### Warm-up

**8.1** A share of preferred stock pays a fixed annual dividend of $4.50. If the required return is 6%, what is the stock's price? If the required return rises to 9%, what is the new price? Explain in one sentence why the price moves in that direction.
*(Tests: constant perpetuity formula and the inverse relationship between rate and price)*

**8.2** Write the present-value formula for an ordinary annuity. Define every variable. Then explain in plain English what the present-value annuity factor represents and why it depends on $r$ and $n$ but not on $C$.
*(Tests: annuity formula structure and conceptual understanding of the annuity factor)*

**8.3** A stated annual rate of 12% is compounded monthly. Compute the effective annual rate. Then explain why the EAR is higher than the APR, and what the difference represents economically.
*(Tests: EAR formula and the compounding intuition behind it)*

### Application

**8.4** You win a lottery prize of $600,000, payable as $60,000 per year for 10 years (ordinary annuity) starting next year. The lump-sum alternative is $420,000 today.

(a) At a 6% discount rate, which option is worth more? Show your calculation.
(b) At a 10% discount rate, which option is worth more? Show your calculation.
(c) Find (by trial and error or algebra) the approximate crossover rate at which both options are equally valuable.
(d) Explain what the crossover rate means in terms of investment alternatives.

*(Tests: annuity PV formula, comparison with lump sum, and the meaning of the discount rate)*

**8.5** You borrow $48,000 to buy a car at 5.4% APR (compounded monthly) over 48 months.

(a) Compute the monthly payment.
(b) Compute total interest paid over the life of the loan.
(c) Build the first three rows and the last row of the amortization schedule (month, payment, interest portion, principal portion, remaining balance).
(d) What is the outstanding loan balance after 24 payments?

*(Tests: solving for payment C, and building/reading an amortization table)*

**8.6** A growing perpetuity pays $5.00 next year and grows at 1.5% per year. The discount rate is 4%.

(a) Compute the present value.
(b) What happens to the present value if the growth rate rises to 3%? Compute the new value.
(c) What happens if the discount rate falls to 2.5% while growth stays at 1.5%? Compute.
(d) Which change — in (b) or (c) — has a larger effect on present value? What does that tell you about which variable matters more?

*(Tests: growing perpetuity formula and sensitivity to changes in r vs. g)*

### Synthesis

**8.7** A 35-year-old plans to retire at 65 and wants to withdraw $6,000 per month for 25 years in retirement. Assume a 6% annual return throughout.

(a) How large a nest egg is needed at age 65 to fund the withdrawals?
(b) What annual savings amount, starting today and ending at age 65, would accumulate to that nest egg?
(c) Suppose the person waits until age 45 to start saving. What annual savings amount is now required? Explain the difference intuitively.

*(Tests: two-phase retirement planning — distribution phase PV, then accumulation phase FV — and the compounding cost of delay)*

**8.8** A credit card has an APR of 21.99%, compounded daily. A store card has an APR of 24.99%, compounded monthly.

(a) Compute the EAR for each card.
(b) Which card is more expensive? By how much in annual interest on a $5,000 balance?
(c) Explain why you cannot compare the two APRs directly to determine which is more expensive.

*(Tests: EAR computation and the limits of APR as a comparison metric)*

### Challenge

**8.9** Two mortgage offers on a $400,000 home (after 20% down, so $320,000 borrowed):

- Offer A: 30 years at 6.5% APR, no points.
- Offer B: 15 years at 5.75% APR, no points.

(a) Compute monthly payments for each.
(b) Compute total interest paid over the life of each loan.
(c) Compute the loan balance remaining after 5 years for each.
(d) Suppose you plan to sell the house in 7 years. Recalculate which offer costs less in total (payments made minus balance remaining at year 7). Does your answer change from (b)?
(e) Defend your mortgage recommendation and name the one assumption your argument most depends on.

*(Tests: annuity payment computation, amortization, total cost analysis, and sensitivity of the recommendation to holding-period assumptions)*

**8.10** Your chosen company pays (or has recently paid) a dividend. Using the company's actual dividend data from its most recent 10-K:

(a) Compute the five-year geometric average dividend growth rate.
(b) Apply the Gordon growth model at three combinations of $r$ and $g$ of your choosing. Display as a 3×3 sensitivity table (three values of $r$ across columns, three values of $g$ down rows — nine valuations total).
(c) Compare your range of modeled prices to the current stock price. Where does the model suggest the stock is fairly valued, overvalued, or undervalued?
(d) Identify the single assumption your valuation is most sensitive to — and explain what would have to be true about the company for that assumption to hold.

*(Tests: Gordon growth model applied to real data, sensitivity analysis, and critical evaluation of model assumptions)*

---

## What would change my mind

The chapter argues that annuity and perpetuity formulas are the right tools for valuing equal-payment streams. Two revisions would shake this. First, if continuous-time pricing methods became the standard introductory framework — they handle equal and unequal payments uniformly — the case-by-case structure here would feel redundant. For introductory pedagogy, the closed-form simplicity still wins. Second, if variable-rate loans became dominant in consumer finance rather than a minority, the fixed-rate annuity model would mislead more often than it helps. Neither shift has materialized.

## Still puzzling

The puzzle the chapter doesn't resolve: what discount rate to actually use. The lottery calculation got opposite answers at 9% versus 6%, and both rates are defensible for different people. The annuity formula doesn't choose the rate — it only translates a rate into a value. Choosing the right rate requires knowing your own opportunity cost of capital, and most people are imprecise about this. The formula makes the ambiguity explicit rather than resolving it. We return to the question of "what rate?" directly in Chapters 14 and 17.

---

## Connections forward

- **Chapter 9** extends to streams of unequal payments — the general TVM case.
- **Chapter 10** uses annuity + single-payment math to price bonds.
- **Chapter 11** uses the growing perpetuity formula (Gordon model) to value stocks.
- **Chapter 16** uses NPV (net present value of unequal cash flow streams) for capital budgeting.
- **Chapter 17** computes WACC, the firm's discount rate.

---

## LLM Exercise — Chapter 8: Value Your Company's Dividend Stream

**Project:** Equity Research Report on a Chosen Public Company
**What you're building this chapter:** Value the dividend stream of your chosen company using the Gordon growth model (perpetuity) or two-stage DDM. Or — for non-dividend-payers — note why the model doesn't apply and what alternative applies.
**Tool:** Claude Project.

### The Prompt

```
For [your company]:

1. **Does the firm pay dividends?** Check the 10-K's statement of stockholders' equity and any recent 8-K dividend declarations.

2. **If yes:**

   (a) State the most recent annual dividend per share (D₀).
   (b) State the dividend growth rate over the past 5 years (geometric average).
   (c) Estimate a sustainable long-term growth rate (g) — typically below 5%, often closer to GDP growth (~2-3%).
   (d) Estimate the required return (r) using a placeholder of 9-10% — we'll refine this in Chapter 14 with CAPM.
   (e) Compute the Gordon growth value: P₀ = D₀(1+g) / (r - g).
   (f) Compare to the current stock price. By what percentage is your computed value above or below the market price?
   (g) Run sensitivity: recompute at g = 1%, 2%, 3% and r = 8%, 9%, 10%. Display as a 3×3 table.

3. **If no:**

   Note that the DDM doesn't apply. Briefly explain what alternative valuation approach (DCF, multiples) the firm requires, and why it doesn't pay dividends (growth-stage, cash hoarding, share buybacks instead, etc.). We'll return to DCF in Chapter 11.

Show your arithmetic. Cite where you got the dividend data.
```

### What this produces

For dividend-payers: a Gordon-model valuation with sensitivity analysis. Adds to the report's valuation section. For non-dividend-payers: a one-paragraph explanation that frames the DCF approach in Chapter 11.

### How to adapt this prompt

- *For your own company:* Replace [your company]. Most large public companies fall into one camp or the other.
- *For ChatGPT / Gemini:* Identical.
- *For a Claude Project:* The 10-K's dividend history is in the statement of equity; reference it directly.

### Connection to previous chapters

Builds on Chapter 7's single-payment discounting. Foreshadows Chapter 11's DCF.

### Preview of next chapter

Chapter 9 generalizes to arbitrary cash flow streams and introduces NPV. The Chapter 9 LLM Exercise will compute NPV for one of your company's recent capex announcements.

---

**Tags:** annuity, perpetuity, ordinary-annuity, annuity-due, amortization, effective-rate, retirement-planning

---

## AI Wayback Machine

**Edmond Halley** was the astronomer who computed the first life-annuity tables in 1693 — making rigorous pricing of multi-payment streams possible.

**Run this:**

```
Who is Edmond Halley, and how does their work connect to annuities we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about their career or ideas.
```

→ Search **"Edmond Halley"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to apply Edmond Halley's framework to a specific finance question.
- Add a constraint: "Answer including criticisms or limits of Edmond Halley's framework."

What changes? What gets better? What gets worse?
