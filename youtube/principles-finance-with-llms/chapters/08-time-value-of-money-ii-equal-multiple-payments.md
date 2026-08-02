# Chapter 8 — Time Value of Money II: Equal Multiple Payments

**Suggested titles**
1. Annuities, Perpetuities, and the Arithmetic of Streams
2. Lottery, Mortgage, Pension
3. Equal Payments Across Time

**TL;DR.** A single-payment time-value calculation handles one cash flow. An *annuity* handles a stream of equal payments over a fixed horizon (mortgages, car loans, pension annuities). A *perpetuity* handles an equal stream that continues forever (preferred stock dividends, college endowments). Both have closed-form formulas that reduce a stream of payments to a single present or future value. This chapter installs those formulas and uses them to price loans, evaluate retirement plans, and tell stated interest rates from effective ones.

---

## The puzzle of the lottery

You win the North Dakota Lottery. The prize is $1.2 million.

The state offers two payout options.

- **Option A** — $120,000 per year for ten years, starting next year.
- **Option B** — a single lump sum, today, of $787,000.

Which is better?

If the question were just "which is more dollars?", Option A wins easily — $1.2 million versus $787,000 is a 50% premium. But the question is which is worth more *today*. Option A's $1.2 million doesn't arrive all at once; it arrives in pieces, over a decade. The first $120,000 lands in twelve months. The second in twenty-four. The last $120,000 doesn't arrive until ten years from now — and a dollar ten years away is worth substantially less than a dollar today.

To answer the question, we have to compute the **present value of a stream of equal payments**. That kind of stream is called an **annuity**. The math we need is an extension of Chapter 7's single-payment time-value formula, but the result is a single closed-form expression that handles any annuity in one step.

Spoiler: at a 9% discount rate, the present value of Option A is about $770,000 — *less* than Option B's $787,000. Take the lump sum. But if you had a way to safely earn 9% on the money, Option A would be worth more than $1.2 million in your pocket at the end. The answer depends on the rate, and the rate depends on what you'd actually do with the money.

For the equity research project, this chapter is the bridge between single-payment TVM (Chapter 7) and the cash-flow streams that drive every valuation in finance (Chapters 9–11, 16–18). Most things you'll value — bonds, mortgages, pension plans, capital projects — are streams of cash, not single lumps.

---

## Learning objectives

After working through this chapter, you should be able to:

- Distinguish a perpetuity from an annuity, and an ordinary annuity from an annuity due.
- Compute the present value of a perpetuity (constant or growing).
- Compute the present value and future value of an ordinary annuity and an annuity due.
- Build a loan amortization schedule by hand or in Excel.
- Solve for any single unknown in an annuity equation (payment, rate, or term).
- Distinguish the stated annual rate from the effective annual rate, and compute the effective rate from any stated rate and compounding frequency.

**Prerequisites.** Chapter 7 (single-payment TVM). Comfort with summation and geometric series.

---

## Concept 1 — Perpetuities: streams that never end

The simplest stream of payments to value is a **perpetuity** — an equal payment that continues forever.

### Why perpetuities have finite present value

It seems impossible. An infinite number of payments, each worth something, adding up to a finite present value? But the math works because each future payment is discounted, and distant payments are discounted to almost nothing.

A $1 payment 50 years from now, discounted at 5%, has a present value of $0.087. A $1 payment 100 years from now, discounted at 5%, has a present value of $0.0076 — less than a penny. By 200 years, it's a hundredth of a cent. The payments approach zero in present value fast enough that their sum converges to a finite number.

The sum is the present value of the perpetuity:

$$PV = \sum_{n=1}^{\infty} \frac{C}{(1+r)^n}$$

This is a geometric series. Multiply both sides by $(1+r)$ and subtract the original to telescope:

$$PV \cdot (1+r) - PV = \frac{C}{(1+r)^0} - \lim_{n \to \infty} \frac{C}{(1+r)^{n}} = C - 0 = C$$

$$PV \cdot r = C$$

$$\boxed{PV = \frac{C}{r}}$$

Where $C$ is the constant payment per period and $r$ is the discount rate per period. That's it. One of the cleanest formulas in finance.

### Worked example — preferred stock as a perpetuity

A common application: a corporation issues preferred stock that pays a fixed dividend forever (or until the firm is dissolved or the stock is called back). If the dividend is $2.00 per share annually and investors require a 7% return, the price of the stock is:

$$PV = \frac{\$2.00}{0.07} = \$28.57$$

Investors will pay $28.57 per share. The math says: for every $28.57 they invest, they receive $2.00 per year forever, which is exactly a 7% return.

If interest rates rise and the required return becomes 10%, the same dividend now requires a price of $\$2.00 / 0.10 = \$20.00$. The stock price falls. This is the basic mechanism by which interest rates affect asset prices, in the simplest possible setting. We'll see the same mechanism much more elaborately in Chapter 10 (bonds) and Chapter 11 (stocks).

### Growing perpetuities

A **growing perpetuity** pays a stream that increases at a constant rate $g$ per period:

$$PV = \frac{C}{r - g}$$

The formula requires $r > g$; otherwise the geometric sum doesn't converge — the payments grow too fast for the discounting to keep up.

Example: a college endowment is structured to pay $4.00 per share to a charitable beneficiary annually, with the payment growing at 0.2% per year. The required return is 3%.

$$PV = \frac{\$4.00}{0.03 - 0.002} = \frac{\$4.00}{0.028} = \$142.86$$

Without growth, the same cash flow at 3% would have a present value of $\$4 / 0.03 = \$133.33$. Adding 0.2% annual growth raises the present value by about 7%.

This formula matters far more than its simplicity suggests. The Gordon growth model, which Chapter 11 uses to value stocks, is just the growing perpetuity formula applied to dividends.

↳ **Dig Deeper — The Gordon growth model's hidden assumption**

*The Gordon growth model — $P = D_1 / (r - g)$ — assumes growth at rate $g$ continues forever and is less than $r$. Both assumptions are violated in real cases. What happens when a firm's growth is genuinely high (close to $r$) for a sustained period? Or when growth is uneven? Practitioners use multi-stage models that the textbook formula doesn't capture cleanly.*

**Prompt:**
> Explain three specific situations where the Gordon growth model produces misleading valuations: (1) a high-growth firm where current $g$ is close to $r$, (2) a cyclical firm whose recent dividends are atypical, (3) a firm whose payout ratio is changing over time. For each, describe how a multi-stage DDM would address the issue, and what assumptions remain unobservable.

**What to do with the output:** Save it. We'll use multi-stage DDMs in Chapter 11; this background helps you set realistic stage transitions.

### The trade-off (concept 1)

The perpetuity formula trades **closed-form simplicity against the assumption of perpetual constancy**. Real cash flows don't stay constant or grow at a fixed rate forever. The formula is most useful for stable cash flows where modeling each period separately would be both difficult and unhelpfully precise. Preferred stock, dividend-paying mature firms, and endowment fund modeling are the natural applications.

---

## Concept 2 — Annuities: streams that end

An **annuity** is a stream of equal payments over a *finite* number of periods. Mortgages, car loans, retirement annuities, and pension payouts are all annuities.

Two flavors of annuity exist depending on when within the period the payment falls.

- **Ordinary annuity** — payment at the *end* of each period. Most loans work this way: you get the loan today, and your first payment is one period later.
- **Annuity due** — payment at the *beginning* of each period. Most lease payments and rent contracts work this way: you pay for January at the start of January, not the end.

The two differ by exactly one period of timing. Annuity due payments are received (or paid) one period earlier, so they're worth slightly more in present-value terms.

### Present value of an ordinary annuity

The present value of an annuity is the sum of the present values of each individual payment:

$$PV = \frac{C}{1+r} + \frac{C}{(1+r)^2} + \frac{C}{(1+r)^3} + \dots + \frac{C}{(1+r)^n}$$

Like the perpetuity, this is a geometric series. Some algebra (the same telescoping move) gives:

$$\boxed{PV = C \times \frac{1 - (1+r)^{-n}}{r}}$$

The bracketed term is called the **present-value annuity factor**. Tables of these factors used to be in the back of finance textbooks; today, every spreadsheet and financial calculator computes them on demand.

### Worked example — solving the lottery

Back to the opening puzzle. North Dakota Lottery: $120,000 per year for 10 years, discounted at 9%.

$$PV = \$120{,}000 \times \frac{1 - (1.09)^{-10}}{0.09} = \$120{,}000 \times 6.4177 = \$770{,}119$$

Lump-sum option: $787,000.

Lump sum wins by about $17,000. At 9%, you can't earn enough on the spread-out payments to justify giving up the cash today.

If your discount rate were lower — say, 6% — the calculation flips:

$$PV = \$120{,}000 \times \frac{1 - (1.06)^{-10}}{0.06} = \$120{,}000 \times 7.3601 = \$883{,}210$$

Now the annuity is worth more than the lump sum. The right discount rate is, as always, what you would actually earn on the money.

### Future value of an ordinary annuity

Sometimes the question runs the other direction: if I save $X per year for $n$ years at rate $r$, how much will I have at the end? The future value of an ordinary annuity is:

$$\boxed{FV = C \times \frac{(1+r)^n - 1}{r}}$$

The bracketed term is the **future-value annuity factor**.

Example: Save $3,000 per year for 5 years at 4%.

$$FV = \$3{,}000 \times \frac{(1.04)^5 - 1}{0.04} = \$3{,}000 \times 5.4163 = \$16{,}249$$

You contributed $15,000. Compounding added $1,249. Modest. Over longer horizons it grows fast.

Save $15,000 per year for 10 years at 8%:

$$FV = \$15{,}000 \times \frac{(1.08)^{10} - 1}{0.08} = \$15{,}000 \times 14.4866 = \$217{,}298$$

You contributed $150,000. Compounding added $67,298 — about 45% of the contributions.

### Annuity due — the (1+r) adjustment

If payments fall at the *beginning* of each period instead of the end, they each sit one period earlier. Multiply the ordinary-annuity formula by $(1+r)$:

$$PV_\text{due} = PV_\text{ordinary} \times (1+r)$$
$$FV_\text{due} = FV_\text{ordinary} \times (1+r)$$

For the lottery example at 9%: $\$770{,}119 \times 1.09 = \$839{,}429$. If the lottery's first payment were today instead of next year, the annuity would be worth more than the lump sum even at 9%.

The (1+r) adjustment is small in absolute terms but compounds across calculations. When evaluating any real annuity, check whether it's ordinary or due; the answer depends on it.

### Worked example — saving early vs. saving more

Two workers each plan to save until age 60 at 5% return.

- **Worker A** starts at age 30, saves $1,000 per year for 30 years.
- **Worker B** starts at age 20, saves $1,000 per year for 40 years.

Worker A's final balance:

$$FV = \$1{,}000 \times \frac{(1.05)^{30} - 1}{0.05} = \$1{,}000 \times 66.4388 = \$66{,}439$$

Worker B's final balance:

$$FV = \$1{,}000 \times \frac{(1.05)^{40} - 1}{0.05} = \$1{,}000 \times 120.7998 = \$120{,}800$$

Worker B contributes $40,000 and ends with $120,800. Worker A contributes $30,000 and ends with $66,439. The 33% more in contributions yields 82% more in final value, because Worker B's early contributions had ten more years to compound.

This is why every personal finance book emphasizes starting early. The arithmetic is built into the annuity formula.

### Solving for the unknown payment

The annuity formula has four variables: $PV$ (or $FV$), $C$, $r$, $n$. Given any three, solve for the fourth.

Most useful in practice: solve for $C$ given $PV$, $r$, and $n$. This is how mortgage payments are computed.

$$C = PV \times \frac{r}{1 - (1+r)^{-n}}$$

Example: Borrow $32,000 for a car at 6% APR over 36 months. Convert to monthly: $r = 0.005$, $n = 36$.

$$C = \$32{,}000 \times \frac{0.005}{1 - (1.005)^{-36}} = \$32{,}000 \times 0.030422 = \$973.50$$

Monthly payment: $973.50. Over 36 months: $35,046 total — meaning $3,046 of interest paid on the $32,000 borrowed.

↳ **Dig Deeper — Mortgages with prepayment options**

*A standard fixed-rate mortgage isn't actually a clean annuity — the borrower has the option to prepay (refinance) when rates fall. This option has value to the borrower and represents a cost to the lender, which is reflected in mortgage pricing. The mortgage market's complexity around prepayment is part of why mortgage-backed securities are harder to value than corporate bonds.*

**Prompt:**
> Explain how the prepayment option affects the valuation of a 30-year fixed-rate mortgage from the lender's perspective. Why are mortgage-backed securities typically priced at a yield premium to comparable Treasuries even after credit-quality adjustments? Then describe one approach lenders use to model expected prepayment (e.g., the PSA prepayment model).

**What to do with the output:** Save it. Mortgage-backed securities are a substantial part of the bond market; understanding prepayment is part of understanding the broader fixed-income landscape.

### The trade-off (concept 2)

Annuity formulas trade **realistic complexity against analytical tractability**. Real loans have prepayment options, variable rates, and balloon payments; pension annuities have inflation adjustments and survival contingencies. The closed-form annuity formula handles none of these. It does, however, value any *fixed-payment, fixed-term* stream in one calculation. Most consumer loans and many corporate-finance applications fit the simple model closely enough that it's the right starting point.

---

## Concept 3 — Real-world applications

Three applications come up routinely.

### Application 1 — Loan amortization

When you make a mortgage or car payment, part of the payment covers interest accrued in the period and part reduces the principal. The mix changes over the life of the loan. Early payments are heavily weighted toward interest; later payments toward principal.

**Why?** Interest accrues on the *outstanding balance*. At the start of the loan, the balance is at its highest, so interest is at its highest. As principal gets paid down, interest expense per period falls, and a larger share of the (constant) payment goes to principal.

For the $32,000 / 36-month / 6% car loan:

| Month | Payment | Interest | Principal | Remaining balance |
|---|---|---|---|---|
| 1 | $973.50 | $160.00 | $813.50 | $31,186.50 |
| 2 | $973.50 | $155.93 | $817.57 | $30,368.93 |
| 12 | $973.50 | $112.99 | $860.51 | $21,738.85 |
| 24 | $973.50 | $61.47 | $912.03 | $11,381.91 |
| 36 | $973.50 | $4.84 | $968.66 | $0.00 |
| **Total** | **$35,046** | **$3,046** | **$32,000** | |

In month 1, interest is 16% of the payment. By month 36, interest is less than 1% of the payment. The schedule of how much principal vs. interest is paid each period is called the **amortization schedule**.

For a 20-year mortgage on $140,000 at 3.6% APR:
- Monthly payment: $819.16
- Total paid over 20 years: $196,598
- Total interest: $56,598 — about 28% of the home's purchase price (after the down payment)

A useful mental model: extending the loan term lowers monthly payments but increases total interest paid. A 30-year mortgage at 3.6% has a lower monthly payment than a 20-year mortgage at the same rate but costs substantially more interest over the life of the loan.

**Prepayment**: paying extra toward principal early reduces the outstanding balance, which reduces interest accrued over the remaining life of the loan, which compounds (in the consumer's favor) as the loan progresses. Even a single extra payment in year 1 can shave several months off a 30-year mortgage.

### Application 2 — Retirement planning

Most retirement-planning calculations are annuity calculations. Two questions come up.

**Accumulation phase.** "If I save $X per year at rate $r$, what will I have at retirement age?" Solve with the future-value annuity formula.

**Distribution phase.** "If I have $Y at retirement age and want to withdraw equal amounts for $n$ years at rate $r$, how much can I withdraw?" Solve with the present-value annuity formula, rearranged for $C$.

Example: A 65-year-old retires with $750,000 in savings. They expect to live to 90 and want equal monthly withdrawals over those 25 years. Their portfolio is invested in a balanced fund earning 5% per year.

Convert to monthly: $r = 0.05/12 ≈ 0.00417$, $n = 25 \times 12 = 300$.

$$C = \$750{,}000 \times \frac{0.00417}{1 - (1.00417)^{-300}} = \$750{,}000 \times 0.005846 = \$4{,}385$$

About $4,385 per month, or roughly $52,600 per year. Combined with Social Security, this might or might not match the retiree's spending needs. The calculation is the input to that decision.

The retirement-planning literature also uses the **4% rule** as a shortcut — withdraw 4% of the initial portfolio per year (with inflation adjustment) and the portfolio should last about 30 years under reasonable return assumptions. The 4% rule is roughly consistent with the present-value annuity math but tilted slightly conservative to account for sequence-of-returns risk. We'll come back to it in Chapter 15.

### Application 3 — Stated vs. effective interest rates

A subtler issue. When a credit card statement says "1.5% per month," what's the annual rate?

The naive calculation: $1.5\% \times 12 = 18\%$. This is the **stated annual rate** or **APR (annual percentage rate)**.

But interest compounds monthly, not just at year-end. The actual annual rate, accounting for compounding, is the **effective annual rate (EAR)**:

$$EAR = (1 + r_\text{period})^m - 1$$

where $r_\text{period}$ is the periodic rate and $m$ is the number of compounding periods per year.

For 1.5% monthly:

$$EAR = (1.015)^{12} - 1 = 0.19562 = 19.56\%$$

The effective rate is 19.56%, not 18%. The difference is real money. On a $10,000 balance carried for a year, that 1.56% gap is $156 in additional interest.

For a credit card APR of 24%, the effective annual rate is over 27%. Compounding daily is more punitive still — closer to 27.1%.

**Why this matters as a consumer**: the rate quoted in marketing material is usually the APR, not the EAR. The effective rate is higher. Always.

**Why this matters as an analyst**: when comparing investments or loans with different compounding frequencies, you cannot compare APRs directly. Convert each to its effective annual rate first. A bond yielding 5% with annual compounding is genuinely lower-yielding than a bond yielding 5% with quarterly compounding (which has an EAR of 5.09%).

The Excel formula `=EFFECT(rate, periods)` returns the EAR directly. For rate 0.015 and 12 periods: `=EFFECT(0.015, 12)` returns 0.1956.

### Worked example — payday loans and the cost of "convenience"

A payday lender offers a cash advance: borrow $200 today, repay $214 in one week. The fee is $14 — 7% of the principal — for one week of borrowing.

Annualized using the simple-multiplication approach: $7\% \times 52 = 364\%$. Already alarming.

Annualized as an effective annual rate (assuming you roll the loan over week after week):

$$EAR = (1.07)^{52} - 1 = 33.7 = 3{,}370\%$$

The effective rate is over thirty-three times the nominal annual rate. This is what payday lending actually costs when consumers can't repay the principal at the end of the week and roll the loan forward. The math is what consumer-protection regulation in this space is up against.

### The trade-off (concept 3)

Real-world annuity applications trade **modeling realism against computational tractability**. Real mortgages have escrow, taxes, insurance, prepayment options, refinancing decisions, points, and origination fees. The simple annuity model treats all of those as separate. For first-pass thinking, the simple model is right. For final-pass financial decisions, the additional features matter and need to be modeled separately.

---

## Synthesis — annuities as the bridge to real valuation

The annuity machinery is the bridge between Chapter 7's single-payment math and the real-world cash-flow streams that make up most financial instruments. By the end of this chapter, you can:

- Value a perpetuity (constant or growing) — the foundation of preferred-stock pricing and the Gordon dividend-discount model.
- Value an annuity (ordinary or due) — the foundation of mortgage and loan pricing, retirement planning, and pension valuation.
- Build a loan amortization schedule by hand or in Excel.
- Convert between stated and effective interest rates — the foundation of comparing rates across products.

What's still missing: cash flow streams where the *payments are unequal*. Real bonds have coupon payments plus a final principal repayment. Real stocks have dividends that grow at varying rates. Real businesses have cash flows that vary year to year. Chapter 9 handles the unequal-payment case, and at that point, you have the full TVM toolkit.

For the equity research project, this chapter completes another piece of the foundation. A bond's value (Chapter 10) is the sum of an annuity (the coupon stream) and a single payment (the maturity value). A dividend-paying stock's value (Chapter 11) is a perpetuity in its simplest form. The arithmetic in this chapter is the arithmetic those chapters use.

---

## Exercises

### Warm-up

**8.1** Distinguish a perpetuity from an annuity. Distinguish an ordinary annuity from an annuity due.

**8.2** Write the present-value formula for: (a) a constant perpetuity, (b) a growing perpetuity, (c) an ordinary annuity. Define every variable.

**8.3** Why is the present value of a perpetuity finite, even though the number of payments is infinite?

### Application

**8.4** A preferred stock pays a $3.50 annual dividend. If the required rate of return is 6%, what is the price of the stock? If the required return rises to 8%, what is the new price?

**8.5** You win a $5 million prize, payable as $250,000 per year for 20 years (ordinary annuity) starting next year. The lump-sum option is $3.5 million today.

(a) At a 7% discount rate, which option is worth more?
(b) At what discount rate are the two options equivalent?
(c) Explain in plain English why the answer depends on the rate.

**8.6** A $250,000 mortgage at 4.5% APR over 30 years.

(a) Compute the monthly payment.
(b) How much interest is paid over the life of the loan?
(c) What's the loan balance after 60 monthly payments (i.e., 5 years)?

### Synthesis

**8.7** A friend's credit card has an APR of 22.99%. Compute the effective annual rate assuming daily compounding. Then compute how long a $10,000 balance would take to double if no payments were made. Use the rule of 72 to cross-check.

**8.8** Pension fund management. Your firm's pension obligations require paying out $2 million per year forever (well, effectively forever — for the foreseeable future of the firm) at a current discount rate of 4%. The firm has $40 million in pension assets.

(a) What is the present value of the obligation?
(b) Is the pension fully funded?
(c) If the discount rate falls to 3%, what happens to the pension's funded status?

### Challenge

**8.9** Two mortgage offers on a $500,000 home (after 20% down).

- Offer A: 30 years at 6.0% APR, no points.
- Offer B: 15 years at 5.0% APR, no points.

(a) Compute monthly payments for each.
(b) Compute total interest paid over the life of each loan.
(c) Argue which is the better choice and what assumption your argument depends on.

**8.10** Build an Excel amortization schedule for a $100,000 loan at 5% APR over 10 years (monthly payments). Use Excel formulas (not hard-coded values) so the schedule updates if you change the rate or term. What happens to the total interest paid if you pay an extra $100 per month? Quantify in dollars and years saved.

---

## Chapter summary

- **Perpetuities** pay an equal stream forever. Present value: $PV = C/r$ (constant) or $PV = C/(r-g)$ (growing).
- **Annuities** pay an equal stream for a finite number of periods.
  - Ordinary annuity (payments at end of period):
    - $PV = C \times \frac{1 - (1+r)^{-n}}{r}$
    - $FV = C \times \frac{(1+r)^n - 1}{r}$
  - Annuity due (payments at beginning of period): multiply by $(1+r)$.
- **Loan amortization** decomposes each payment into interest and principal. Early payments are interest-heavy; late payments are principal-heavy.
- **Stated vs. effective rates**: $EAR = (1 + r_\text{period})^m - 1$. Always convert before comparing rates with different compounding frequencies.

---

## What would change my mind

The chapter argues that annuity and perpetuity formulas are the right tools for valuing equal-payment streams. The reading would have to revise if (a) a closed-form valuation method emerged that handled both equal and unequal payments uniformly without the case-by-case approach this chapter teaches — some derivatives-pricing approaches do this in continuous time, but they're more complex than the closed-form annuity formulas; for introductory pedagogy the simpler approach wins, or (b) the underlying assumption of constant rates over the life of an annuity broke down so frequently in practice that the formulas became misleading. Real loans do have variable-rate features, but the fixed-rate annuity model remains the dominant one in consumer finance.

## Still puzzling

The cleanest unresolved question this chapter sets up is *what discount rate to use for an annuity*. For the lottery example, I used 9%, then 6%, and got opposite answers. Which one is right? The textbook answer is "your opportunity cost of capital" — what you'd earn on the money in your next-best alternative. But that requires me to know my own personal investment opportunities and risk tolerance. In practice, most people are sloppy about this, and the answer they get is whatever the assumed rate happens to produce. Honest financial advisors say so. I'll come back to this in Chapter 17 (WACC) and Chapter 11 (DCF discount rate) where the question of "what rate?" is dragged into the open.

---

## Connections forward

- **Chapter 9** extends to streams of *unequal* payments — the general TVM case.
- **Chapter 10** uses annuity + single-payment math to price bonds.
- **Chapter 11** uses the growing perpetuity formula (Gordon model) to value stocks.
- **Chapter 16** uses NPV (net present value of unequal cash flow streams) for capital budgeting.
- **Chapter 17** computes WACC, the firm's discount rate.

---

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

**Edmond Halley** was astronomer who computed the first life-annuity tables in 1693 — making rigorous pricing of multi-payment streams possible.

**Run this:**

```
Who is Edmond Halley, and how does their work connect to annuities we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about their career or ideas.
```

→ Search **"Edmond Halley"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to apply Edmond Halley's framework to a specific finance question.
- Add a constraint: "Answer including criticisms or limits of Edmond Halley's framework."

What changes? What gets better? What gets worse?
