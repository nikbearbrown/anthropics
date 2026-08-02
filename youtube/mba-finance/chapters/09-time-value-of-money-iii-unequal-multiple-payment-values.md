# Chapter 9 — Time Value of Money III: Unequal Multiple Payments
*How one number decides whether an investment is worth making.*

---

A friend pitches you a project. They want $450,000 up front. In return, the project will generate cash flows over the next five years: $100,000 in year one, $125,000 in year two, $175,000 in year three, $90,000 in year four, $50,000 in year five.

Total cash returned: $540,000. That's $90,000 more than you put in — about 20% gross return over five years. The project sounds good.

It probably isn't.

The arithmetic ignores time value. The $50,000 arriving in year five is worth substantially less today than $50,000 in your hand right now. The $100,000 in year one is worth almost as much as $100,000 today, but not quite. To decide whether the project is genuinely a good investment, you have to convert every future cash flow into today's dollars — each one discounted by the number of years until it arrives — and compare the total to the $450,000 it costs.

At a 4% discount rate, the present value of the five cash flows is about $485,000. The project clears the bar by $35,000.

At a 10% discount rate, the present value falls to about $399,000 — roughly $51,000 *less* than you'd put in. The project doesn't clear the bar.

Same project, same cash flows, same arithmetic. The discount rate decides. This is the general case of time-value-of-money analysis, and the tool it produces — **net present value** — is the single most useful number in finance for deciding whether an investment is worth making.

---

## From equal payments to arbitrary streams

Chapter 7 handled single payments. Chapter 8 handled streams of equal payments — annuities — and showed that the geometric-series structure of equal payments permits a closed-form collapse. The real world does not cooperate. Bonds have a final principal repayment that dwarfs each coupon. Capital projects have lumpy upfront costs and uneven returns. Stocks pay dividends that grow at varying rates. The general case has to handle any sequence.

The formula is simpler than it looks. Number the periods $t = 0, 1, 2, \ldots, n$. Let $CF_t$ be the cash flow in period $t$ — positive for inflows, negative for outflows, zero for periods where nothing happens. The present value of the entire stream is:

$$PV = \sum_{t=0}^{n} \frac{CF_t}{(1+r)^t}$$

That is the complete technical content. Discount each cash flow by the number of periods until it arrives, and sum. The annuity formula from Chapter 8 is a special case: when every $CF_t$ equals the same constant $C$, the geometric series collapses into the closed form. When the cash flows are unequal, the sum doesn't collapse, and you compute it term by term.

The friend's project, worked out at a 4% discount rate:

<!-- → [TABLE: five-year mixed cash flow table — columns: year, cash flow, discount factor (1/(1.04)^t), present value — rows 0 through 5 plus total row showing NPV of +$35,326 — student should see each flow discounted individually and the sum] -->

Year 0: −$450,000 × 1.0000 = −$450,000. Year 1: $100,000 × 0.9615 = $96,154. Year 2: $125,000 × 0.9246 = $115,570. Year 3: $175,000 × 0.8890 = $155,574. Year 4: $90,000 × 0.8548 = $76,932. Year 5: $50,000 × 0.8219 = $41,096. Sum: +$35,326.

The sum of the discounted inflows is $485,326. After subtracting the $450,000 initial outflow, the **net** present value is $35,326. The project's cash flows, expressed in today's dollars, exceed its cost by that amount.

The same calculation runs forward in time just as easily. If you make a series of unequal contributions to an investment account, the future value at the end of year $n$ is:

$$FV = \sum_{t=0}^{n} CF_t \cdot (1+r)^{n-t}$$

Each contribution is compounded forward for the years remaining until the horizon. A saver who deposits $2,000 per year for seven years but adds an extra $10,000 in year three and an extra $3,000 in year five would compound each deposit by its own remaining time: the year-zero deposit grows for seven full years, the year-three deposit (including the lump sum) grows for four, the year-five deposit (including its lump sum) grows for two. You sum across all of them. The arithmetic is the same as the PV calculation — just running in the opposite direction.

---

## Net present value: the decision tool

The general PV formula is the machinery. **Net present value** is the conventional way of using that machinery to make a yes-or-no decision.

For an investment with initial outflow $C_0$ and subsequent cash inflows $C_1, C_2, \ldots, C_n$ at discount rate $r$:

$$NPV = -C_0 + \sum_{t=1}^{n} \frac{C_t}{(1+r)^t}$$

NPV is the present value of inflows minus the present value of outflows, denominated in today's dollars. The decision rule:

- If NPV > 0, accept. The discounted inflows exceed the cost.
- If NPV < 0, reject. The cost exceeds the discounted inflows.
- If NPV = 0, the investment exactly meets the required return.

This is the cleanest decision rule in finance. It accounts for the time value of money, it is denominated in a concrete unit (today's dollars), and it has a property called **value additivity**: the NPV of two independent projects combined is exactly the sum of the individual NPVs. That property is what makes NPV the dominant tool in capital budgeting — you can evaluate each project on its own and then combine.

A point worth stating explicitly: the NPV is *the dollar amount by which the project increases the wealth of its owners, in present-value terms*. An NPV of $35,326 does not mean the project earns $35,326 in profit. It means the project, properly executed at the assumed discount rate, makes you $35,326 richer right now in present-value terms. That is a different and more useful statement.

### What the discount rate is actually doing

The sensitivity of NPV to the discount rate is not a flaw to be apologized for. It is the mechanism telling you the most important thing about the investment.

For the friend's project:

| Discount rate | NPV |
|---|---|
| 0% | +$90,000 |
| 4% | +$35,326 |
| 7% | ≈ $0 |
| 10% | −$51,000 |
| 15% | −$120,000 |

At approximately 7%, the project breaks even. The 7% rate has a name: the **internal rate of return (IRR)** — the discount rate that makes NPV exactly zero. The IRR is the project's maximum viable cost of capital. If you can fund the project more cheaply than 7%, it's worth doing. If it costs more than 7% to obtain the capital, it isn't.

The sensitivity table encodes something important. A project whose NPV turns negative at an 8% discount rate is a very different animal from a project that remains positive at 20%. The first is fragile — small changes in the cost of capital flip the decision. The second has margin for error. Any honest NPV analysis computes the answer at several discount rates and reports the range, not a single number.

<!-- → [CHART: NPV profile curve — NPV on y-axis, discount rate on x-axis, showing the project from the worked example — curve crosses zero at IRR (~7%), student should see the shape of the relationship and how steeply it declines] -->

---

## Two paths to the same answer

For any mixed cash flow stream, there are two equivalent approaches.

**Path one** — discount each cash flow individually and sum. This is what the table above does. Conceptually clean, mechanically tedious for long-horizon projects.

**Path two** — decompose into annuity plus single payments. If the stream contains a large regular component — say, equal cash flows for years one through five, plus a large terminal payment in year five — value the annuity in one calculation using the Chapter 8 formula and value the irregular payments separately. Then sum. The two paths give identical answers up to rounding.

Path two is faster when the annuity component dominates. Path one is the default when the cash flows are genuinely irregular throughout. For any project with more than eight or ten periods, you do this in a spreadsheet.

In Excel, the `NPV()` function does path one automatically:

```
=NPV(rate, value1, value2, ...) - initial_investment
```

The function returns the present value of the cash flows listed, starting from period one. It does *not* include the initial investment — you subtract that manually, because the initial outflow occurs at $t = 0$ and needs no discounting. For the friend's project at 10%:

```
=NPV(0.10, 100000, 125000, 175000, 90000, 50000) - 450000
```

returns approximately −$51,000. Reject.

The Excel formula is a one-liner. The conceptual understanding — why you subtract the initial investment outside the function, why the period numbering matters, what the output means — is what takes the rest of the chapter.

---

## How analysts actually use NPV

The mechanics are clean. The hard parts in practice are getting the cash flows right and choosing the discount rate. Both are judgment calls.

### Getting the cash flows right

For a capital-budgeting decision, the cash flows are not observed — they're forecast. A real analysis includes: the initial investment in equipment, working capital, and setup; year-by-year incremental revenue from the project; year-by-year incremental costs; tax effects (depreciation tax shields, effective tax rate on incremental income); and a **terminal value** — what the project's assets are worth, net of disposal costs, at the end of the project's life.

Each of these is an estimate. Bad estimates produce wrong NPVs even if the discounting arithmetic is perfect. Good practice runs the calculation under multiple scenarios — base case, optimistic, pessimistic — and reports the range. The NPV decision rule then becomes: accept if NPV > 0 in the base and pessimistic cases; examine carefully if the decision flips across scenarios; reject if NPV < 0 in all plausible scenarios.

### Choosing the discount rate

The standard answer in corporate finance is the firm's **weighted average cost of capital (WACC)** — the blended cost of debt and equity weighted by the firm's capital structure. Chapter 17 computes WACC in detail. But WACC is itself an estimate. The cost of equity comes from the CAPM (Chapter 14), which requires assumptions about the market risk premium and the firm's beta. Different reasonable analysts can arrive at 1–2 percentage point differences in WACC for the same firm.

A 1–2 percentage point difference in the discount rate can flip a project from positive to negative NPV. This is not a comfortable fact. It means the NPV calculation's output is only as trustworthy as the weakest link in its assumptions — and the discount rate is often that link. The discipline is to be transparent about what rate you used, to test sensitivity across a range, and to be honest about what the range implies for the decision.

<!-- → [TABLE: sensitivity table showing NPV at varying discount rates and cash flow scenarios — rows: discount rates from 6% to 14% in 1-point increments; columns: optimistic, base, pessimistic cash flows — student should see how the decision can flip in different quadrants] -->

### Terminal value dominance

For long-horizon projects and DCF stock valuations, a practical problem emerges: the terminal value — the lump sum representing all cash flows beyond the explicit forecast horizon — often represents 60–80% of the total computed value. The year-by-year forecast gets most of the analytical attention, but a single perpetuity assumption is doing most of the heavy lifting.

This is not a flaw in the math — it is a mathematical truth about how much near-term versus far-term cash flows contribute to present value at any reasonable discount rate. But it means the terminal value assumption deserves the same rigor as the year-by-year forecast, and usually gets less. An honest DCF says: "Here is what my terminal-value assumption implies about the long-run growth rate of the business. Is that plausible?" A DCF that doesn't ask that question is doing less than the math requires.

### Real options

NPV in its standard form treats projects as fixed once started. Real projects often have flexibility: the option to expand if early results are strong, to shut down if they're weak, to delay the start until market conditions improve. These flexibility features have economic value that standard NPV does not capture — it assumes you either fully commit now or don't commit at all.

The field of real options addresses this gap. For most routine capital projects, the difference is small enough to ignore. For projects with explicit flexibility built in — a biotech firm's option to develop a backup drug candidate, an energy firm's option to extract a reserve depending on future commodity prices, a technology firm's option to enter a new market — ignoring optionality can materially understate value. Chapter 16 returns to this briefly. For now, the point is that NPV is a floor on value when real options exist, not a ceiling.

---

## The TVM toolkit complete

Three chapters, one conceptual arc. Chapter 7 gave the master formula for a single payment. Chapter 8 showed what happens when equal payments form a geometric series and collapse into a clean closed form. Chapter 9 handles every case the earlier chapters excluded — the real cases, the ones with unequal cash flows, irregular timing, lumpy terminal payments.

The tool the general case produces — net present value — is the answer to the question that turns up on every serious investment decision: *is this worth doing?* Not whether the total dollars returned exceed the total dollars invested (the friend's 20% gross return), but whether the discounted inflows exceed the cost. The discount rate is the mechanism that encodes everything you know about the riskiness of the cash flows, the opportunity cost of capital, and the time preference of money.

What comes next is application. Chapter 10 uses this machinery to price bonds — the coupon stream is a mixed payment, with equal coupons plus a single par repayment at maturity. Chapter 11 uses it to value stocks via DCF. Chapter 16 applies it directly to corporate capital budgeting. Chapter 17 shows how to compute the discount rate carefully. The NPV concept from this chapter runs through all of them.

For the equity research project, the implication is concrete: when your chosen company announces a major capital expenditure, this is the analytical move. Estimate the incremental cash flows, choose a discount rate, compute NPV across a range of assumptions, and form a view on whether the announcement creates or destroys value. That analysis becomes a section of the report.

---

## What would change my mind

The chapter argues NPV is the right decision rule for evaluating investments with estimable cash flow streams. I would revise if (a) real-options-based valuation consistently outperformed NPV in predicting actual project outcomes — there is a genuine literature here, and for projects with significant flexibility, real options is better; for most standard projects, NPV remains the workhorse — or (b) the assumption that future cash flows can be reasonably estimated collapsed, in which case no formal decision rule helps and judgment dominates entirely. Both qualifications are real. Neither displaces NPV as the first tool to reach for.

## Still puzzling

The same discomfort returns that appeared in Chapter 7: *what discount rate?* The NPV calculation is mathematically exact. The discount rate going into it is an estimate built on other estimates. In practice, the discount rate is often where the most sensitivity in the analysis lives, and the choice can flip a project from accept to reject without changing anything about the underlying business. I am uncomfortable with how casually most applied DCF analysis chooses this number. The discomfort is appropriate, and analysts who feel it are usually better analysts than those who don't.

---

## Connections forward

- **Chapter 10** prices bonds using mixed-stream NPV math — equal coupons plus a single par repayment at maturity.
- **Chapter 11** values stocks via DCF — the general present-value formula applied to forecasted free cash flows.
- **Chapter 14** refines the discount rate via the Capital Asset Pricing Model.
- **Chapter 16** applies NPV formally to corporate capital budgeting and introduces IRR as a companion tool.
- **Chapter 17** computes WACC — the standard discount rate for corporate projects.

---

## Exercises

### Warm-up

**9.1** State the NPV decision rule in one sentence. Why is the rule stated in terms of today's dollars rather than future dollars? *(Tests: definition and unit-of-measure clarity. Difficulty: low.)*

**9.2** What is the internal rate of return (IRR), and how does it relate to the NPV of a project? If a project's IRR is 9% and the firm's cost of capital is 11%, what does NPV tell you? *(Tests: IRR-NPV relationship. Difficulty: low.)*

**9.3** The Excel `NPV()` function requires you to subtract the initial investment separately. Why — what assumption is built into the function that requires this manual step? *(Tests: period-zero mechanics. Difficulty: low.)*

### Application

**9.4** A project requires $200,000 today and produces the following cash flows: Year 1: $40,000; Year 2: $60,000; Year 3: $80,000; Year 4: $80,000; Year 5: $60,000. (a) Compute NPV at 6%. (b) Compute NPV at 12%. (c) Between 6% and 12%, does the IRR appear to be closer to 6%, 9%, or 12%? Justify your answer without solving for IRR exactly. *(Tests: direct NPV computation + IRR intuition. Difficulty: medium.)*

**9.5** Two projects each require $100,000 today. Project A pays $50,000 / $50,000 / $30,000 / $20,000 / $10,000 over five years. Project B pays $20,000 / $40,000 / $50,000 / $70,000 / $60,000 over five years. (a) Compute NPV for each at 10%. (b) Which project has higher NPV? (c) The projects have identical undiscounted cash flows — $160,000 each. Why does their NPV differ, and what does that tell you about the value of receiving cash flows earlier versus later? *(Tests: timing effects in mixed streams. Difficulty: medium.)*

**9.6** A project has the following cash flows: Year 0: −$100,000; Year 1: +$300,000; Year 2: −$250,000. (a) Compute NPV at 5%, 25%, and 50%. (b) The IRR is defined as the discount rate making NPV = 0. Based on your three computations, does this project appear to have one IRR or more than one? (c) What does this imply about using IRR as a decision rule when cash flows change sign more than once? *(Tests: multiple-IRR problem and NPV's advantage. Difficulty: medium-high.)*

### Synthesis

**9.7** Identify a major capital expenditure announced by your chosen company in the past three years. Estimate the incremental cash flows using the firm's 10-K and announcement disclosures. Compute NPV at 7%, 9%, and 11%. At which rate does the project turn value-destroying? Does your analysis support or challenge management's stated rationale for the investment? *(Tests: applied NPV on a real firm. Difficulty: high.)*

**9.8** The chapter notes that for a typical five-year DCF, terminal value represents 60–80% of total computed value. (a) Verify this claim numerically: build a five-year DCF with Year 1 FCF of $100M growing at 5% per year, a 9% discount rate, and a terminal value of 15× Year 5 FCF. What percentage of total value comes from the terminal value? (b) Now shift the terminal multiple from 15× to 12×. By how much does total value change? (c) What does this imply for how much analytical attention should go to terminal-value assumptions versus the year-by-year forecast? *(Tests: terminal-value dominance and sensitivity. Difficulty: high.)*

### Challenge

**9.9** A friend argues: "NPV is too sensitive to the discount rate to be useful — a 2-point change in the rate can flip the answer, so the whole exercise is garbage in, garbage out." Construct the strongest version of this criticism, then refute it. Your refutation should explain what information the sensitivity itself contains, and describe how a serious analyst handles it rather than ignoring it. *(Tests: meta-reasoning about NPV's limitations and proper use. Difficulty: high.)*

**9.10** Build a DCF-style NPV in Excel for a hypothetical company: Year 1 FCF of $50M growing at 8% through Year 5, then 5% through Year 10, with a terminal value of 12× Year 10 FCF and a 9% discount rate. (a) Compute total present value. (b) Vary the discount rate from 7% to 11% in 0.5-point increments and record total value at each rate. (c) Vary the terminal multiple from 10× to 15× at a fixed 9% discount rate and record total value at each multiple. (d) Construct a two-variable sensitivity table showing total value for every combination of discount rate (7–11%) and terminal multiple (10×–15×). What does the table tell you about which assumption matters more? *(Tests: spreadsheet NPV construction + two-variable sensitivity analysis. Difficulty: high.)*

---

## LLM Exercise — Chapter 9: NPV of a Recent Capex Announcement

**Project:** Equity Research Report on a Chosen Public Company
**What you're building this chapter:** Compute NPV for a real capital project your company announced — preparation for a deeper capital-budgeting analysis in Chapter 16.
**Tool:** Claude chat or Project.

### The Prompt

```
For [your company], identify a major capital expenditure announced in the past 2-3 years. This might be:
- A new factory or facility
- A major acquisition
- A new product line launch with disclosed expected economics
- A large multi-year capex program

For your chosen project:

1. **Initial investment** — Total announced cost. If staged, document the schedule of outflows.

2. **Cash flow forecast** — Estimate annual incremental free cash flows from the project for 5-10 years. Use:
   - Revenue projections from the firm's announcement or 10-K MD&A
   - Reasonable margin assumptions (use the firm's overall margin or industry norms)
   - Tax effects (use the firm's effective tax rate)
   - Maintenance capex assumptions

   Be explicit about each assumption. Where you're guessing, say so.

3. **Discount rate** — Use 8-10% as a placeholder for the firm's WACC. We'll compute the real WACC in Chapter 17.

4. **Compute NPV** at three discount rates: 7%, 9%, 11%. Show the present value of each year's cash flow.

5. **Verdict** — Is the project value-creating at a reasonable discount rate? At what discount rate does it become value-destroying (the IRR)?

6. **Compare to firm's stated rationale** — From the announcement and 10-K commentary, what did management say the project would produce? Does your NPV analysis support or challenge that view?

Show your work. Cite the source of every input.
```

### What this produces

A 2-page capital-budgeting analysis of a real corporate decision. Becomes Section 7 of the report (capital allocation). The same exercise will be revisited in Chapter 16 with more sophisticated treatment.

### How to adapt this prompt

- *For your own company:* Replace [your company]. If your firm hasn't announced a major capex recently, use any large project from the firm's recent history.
- *For ChatGPT / Gemini:* Identical.
- *For Claude Code:* The discounting math could be a small Python script; otherwise Excel.

### Connection to previous chapters

Builds on Chapters 7 and 8's TVM machinery. Sets up Chapter 16's deeper capital-budgeting treatment.

### Preview of next chapter

Chapter 10 prices bonds. The Chapter 10 LLM Exercise will price one of your company's outstanding bonds.

---

**Tags:** NPV, mixed-stream, present-value, capital-budgeting, discount-rate, time-value-of-money

---

## AI Wayback Machine

**Run this:**

```
Who is Frederick Macaulay, and how does their work connect to unequal cash flows we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about their career or ideas.
```

→ Search **"Frederick Macaulay"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to apply Frederick Macaulay's framework to a specific finance question.
- Add a constraint: "Answer including criticisms or limits of Frederick Macaulay's framework."

What changes? What gets better? What gets worse?
