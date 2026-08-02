# Chapter 9 — Time Value of Money III: Unequal Multiple Payments

**Suggested titles**
1. The General Case
2. NPV — Where TVM Becomes a Decision Tool
3. Cash Flows That Aren't Equal

**TL;DR.** Real cash flow streams aren't equal. Bonds have a final principal repayment that dwarfs each coupon. Capital projects have lumpy upfront costs and uneven returns. Stocks pay dividends that grow at varying rates. The solution is the general case: discount each cash flow separately by its own time horizon, then sum. The result has a name — **net present value** — and is the single most useful number in finance for deciding whether an investment is worth making.

---

## The puzzle of the investment decision

A friend pitches you on a project. They want $450,000 up front. In return, the project will generate cash flows over the next five years:

| Year | Cash flow |
|---|---|
| 1 | $100,000 |
| 2 | $125,000 |
| 3 | $175,000 |
| 4 | $90,000 |
| 5 | $50,000 |

Total cash returned: $540,000. That's $90,000 more than you put in — about 20% gross return over five years. The project sounds good.

It probably isn't.

The simple-arithmetic comparison ignores time value. The $50,000 you receive in year 5 is worth substantially less today than $50,000 in your hand right now. The $100,000 you receive in year 1 is worth almost as much as $100,000 today, but not quite. To decide whether the project is actually a good investment, you have to discount each future cash flow to today's dollars and compare the total to the initial $450,000.

If your discount rate is 4% (a low-risk benchmark), the present value of the cash flow stream is about $485,326 — about $35,000 more than the initial investment. The project clears the bar by a modest margin.

If your discount rate is 10% (reflecting the project's actual risk), the present value drops to about $399,000 — about $51,000 *less* than you'd put in. The project doesn't clear the bar.

Same project, same cash flows. The discount rate decides.

This is the general case of time-value-of-money analysis. Chapter 7 handled single payments. Chapter 8 handled streams of equal payments (annuities). Chapter 9 handles arbitrary streams — the case that covers most real investments. The tool we build here, **net present value (NPV)**, is the foundation of capital budgeting (Chapter 16) and of every DCF valuation in equity research.

---

## Learning objectives

After working through this chapter, you should be able to:

- Compute the future value of a mixed stream of cash flows.
- Compute the present value of a mixed stream of cash flows by direct discounting and by decomposition into annuity-plus-single-payment components.
- Compute net present value (NPV) of an investment.
- State and apply the NPV decision rule.
- Build an NPV calculation in Excel using the `NPV()` function.
- Identify how sensitive an NPV calculation is to its discount rate.

**Prerequisites.** Chapters 7 and 8.

---

## Concept 1 — From equal payments to arbitrary streams

Chapter 8 gave you a closed-form formula for the present value of $n$ equal payments. Real cash flow streams rarely come in $n$ equal payments. The general formula has to handle any sequence of cash flows.

### The universal approach

Number the periods $t = 0, 1, 2, \ldots, n$. Let $CF_t$ be the cash flow in period $t$ — positive for inflows, negative for outflows, zero for periods with no cash movement.

The present value of the entire stream is:

$$PV = \sum_{t=0}^{n} \frac{CF_t}{(1+r)^t}$$

That is the whole technical content. Discount each cash flow by the number of periods until it arrives, and sum. The summation extends as far as the cash flows extend.

When the cash flows happen to be equal — say, $CF_t = C$ for all $t$ from 1 to $n$ — the geometric-series collapse from Chapter 8 gives the closed-form annuity formula. When they're unequal, the sum doesn't collapse, and you compute it explicitly.

### A worked example — the $450K project

For the friend's project, with a 4% discount rate:

| Year | Cash flow | Discount factor | Present value |
|---|---|---|---|
| 0 | −$450,000 | 1.0000 | −$450,000 |
| 1 | $100,000 | 0.9615 | $96,154 |
| 2 | $125,000 | 0.9246 | $115,570 |
| 3 | $175,000 | 0.8890 | $155,574 |
| 4 | $90,000 | 0.8548 | $76,932 |
| 5 | $50,000 | 0.8219 | $41,096 |
| **Total** | | | **$35,326** |

The sum of the discounted cash flows (positive entries) is $485,326. After subtracting the $450,000 initial outflow, the **net** present value is about $35,326 — meaning the project's cash flows, in today's dollars, exceed its cost by that amount.

A 4% discount rate is appropriate for very-low-risk projects. For most business investments, the right rate is higher. We'll come back to choosing the rate.

### Future value of a mixed stream

The mirror calculation runs forward in time. If you make a series of unequal contributions to a savings account over $n$ years, the future value at the end of year $n$ is:

$$FV = \sum_{t=0}^{n} CF_t \cdot (1+r)^{n-t}$$

Each contribution is compounded for the number of years remaining until the end of the horizon.

For a saver who contributes $2,000 per year for 7 years at 7%, plus an extra $10,000 in year 3 and an extra $3,000 in year 5:

| Year | Contribution | Years remaining | FV at year 7 |
|---|---|---|---|
| 0 | $2,000 | 7 | $3,212 |
| 1 | $2,000 | 6 | $3,001 |
| 2 | $2,000 | 5 | $2,805 |
| 3 | $12,000 | 4 | $15,730 |
| 4 | $2,000 | 3 | $2,450 |
| 5 | $5,000 | 2 | $5,725 |
| 6 | $2,000 | 1 | $2,140 |
| **Total** | $27,000 | | **$35,062** |

The saver contributed $27,000 in nominal terms and ended with $35,062. About $8,062 is interest earned through compounding.

### Two paths to the same answer

For unequal streams, there are usually two ways to compute the answer.

**Path 1 — Discount each cash flow individually.** As shown in the table above. Conceptually clean, mechanically tedious.

**Path 2 — Decompose into annuity + single payments.** If the stream contains a regular annuity component and irregular extras, value the annuity in one calculation (using the closed-form annuity formula) and value the irregular payments separately. Then sum.

The two paths give identical answers (up to rounding). Path 2 is faster when the annuity component is large; Path 1 is faster when the cash flows are genuinely irregular. For a five-year project with no obvious annuity structure, Path 1 is the default.

In practice, you'll do all of this in Excel.

↳ **Dig Deeper — When IRR has multiple solutions**

*The internal rate of return is the discount rate making NPV zero. For "normal" projects (one initial outflow, then inflows), IRR is unique. For projects with mixed cash flow signs (initial outflow, inflows, then a large terminal outflow — common in nuclear plants, mining, environmental cleanup), there can be multiple IRRs. Which one is right?*

**Prompt:**
> Explain the multiple-IRR problem with a specific example. Use the Olympic facility case: $350M build (year 0), $950M operating cash flow (year 1), $620M demolition cost (year 2). Show that this has two IRRs. Then explain why MIRR (modified internal rate of return) addresses this — and what assumptions MIRR makes that IRR doesn't.

**What to do with the output:** Save it. We'll come back to MIRR in Chapter 16; for now, knowing that IRR has known failure modes helps you trust NPV instead.

### The trade-off (concept 1)

The general approach trades **flexibility against speed**. The closed-form annuity formula handles a specific, common case in one step. The general PV-of-a-mixed-stream approach handles every case but requires you to compute each cash flow's discount factor and sum. Spreadsheets erase the speed difference; the conceptual framework matters.

### Common misconceptions

- *"Mixed stream means random."* Mixed just means unequal. The cash flows can still be predictable; they just don't all equal each other.
- *"You need a calculator or spreadsheet."* You don't. For small problems, the math is fast by hand. For project analysis with 30+ years of cash flows, a spreadsheet is essential.

---

## Concept 2 — Net present value: the decision tool

The PV-of-a-mixed-stream calculation is the engine. **Net present value (NPV)** is the conventional way of using that engine to make investment decisions.

### Definition

For an investment with an initial outflow $C_0$ (a negative cash flow at time 0) and subsequent cash inflows $C_1, C_2, \ldots, C_n$ at a discount rate $r$:

$$NPV = -C_0 + \sum_{t=1}^{n} \frac{C_t}{(1+r)^t}$$

(Some authors write the initial investment as $C_0$ already negative and absorb it into the sum from $t=0$. Either convention works; just be consistent.)

NPV is the present-value-of-inflows minus the present-value-of-outflows. It is denominated in today's dollars.

### The NPV decision rule

The standard rule for evaluating an investment with a known cash flow stream and a known discount rate:

- **If $NPV > 0$**, accept the investment. The discounted inflows exceed the cost.
- **If $NPV < 0$**, reject. The cost exceeds the discounted inflows.
- **If $NPV = 0$**, indifferent. The investment exactly meets the required return.

This is the cleanest decision rule in finance. It accounts for the time value of money, and it scales — the NPV of two combined projects is the sum of the individual NPVs (assuming independence). This last property, called **value additivity**, is what makes NPV the dominant tool in capital budgeting.

### The NPV is denominated in today's dollars

A subtle but important point. The NPV of a project is *the dollar amount by which the project will increase the wealth of its owners, today*. NPV of $35,326 means the project, properly executed, makes you $35,326 richer right now in present-value terms.

This isn't a forecast of profits. It isn't a return percentage. It is a single dollar number telling you how much the project is worth above its cost.

### Sensitivity to the discount rate

The NPV calculation depends critically on the discount rate. Small changes in the rate produce large changes in NPV, especially for long-horizon projects.

For the $450K project:

| Discount rate | NPV |
|---|---|
| 0% | $90,000 |
| 4% | $35,326 |
| 7% | $0 (approximate breakeven) |
| 10% | −$51,000 |
| 15% | −$120,000 |

At a 7% discount rate, the project breaks even. Above 7%, it destroys value. Below 7%, it creates value.

The 7% breakeven rate has a name: the **internal rate of return (IRR)**. We'll formalize IRR in Chapter 16. For now, note that:

- IRR is the discount rate that makes NPV = 0.
- A project should be accepted if IRR > the cost of capital, rejected if IRR < the cost of capital.

NPV and IRR usually agree on accept/reject decisions. They occasionally disagree (Chapter 16 will work through when), and when they disagree, NPV is the right tool.

### Worked example — using `=NPV()` in Excel

For Excel users, the `NPV()` function does most of the work. The syntax:

```
=NPV(rate, value1, value2, ...)
```

The function returns the present value of the cash flows starting in *period 1*. It does *not* include the initial investment at $t = 0$. To get full NPV including the initial outflow, subtract the initial investment from the function's result:

```
=NPV(rate, year1, year2, ..., yearN) - initial_investment
```

For the $450K project with a 10% discount rate:

```
=NPV(0.10, 100000, 125000, 175000, 90000, 50000) - 450000
```

returns approximately −$51,000. Reject.

The Excel formula is robust enough that for routine work, NPV calculations are a one-liner. The conceptual understanding is what's hard.

### Common misconceptions

- *"NPV is too sensitive to the discount rate to be useful."* The sensitivity is real, and analysts should report NPV at several discount rates as part of any serious analysis. The sensitivity is a feature, not a bug — it forces you to be honest about what you're assuming.
- *"NPV ignores the initial investment."* It doesn't. NPV explicitly subtracts the initial investment from the present value of inflows.
- *"A higher NPV is always better."* All else equal, yes. But two projects with different scales can have very different NPVs without one being better — a $50M project with NPV $5M is doing a lot more work to produce that NPV than a $1M project with NPV $4M would. Scale matters; NPV doesn't capture it.

---

## Concept 3 — How analysts actually use NPV

The NPV machinery as taught is straightforward. The hard parts in practice are getting the cash flows right and choosing the discount rate. Three observations from how the tool is actually used.

### Cash flows: get them as right as you can

NPV in the abstract assumes you know the cash flows. In practice, you're forecasting them.

For a capital-budgeting decision (Chapter 16), the cash flows include:
- The initial investment in equipment, working capital, and setup.
- Year-by-year incremental revenue from the project.
- Year-by-year incremental costs of running the project.
- The tax effects (depreciation, tax savings on losses, etc.).
- The terminal value — what the project's assets are worth, net of disposal costs, at the end of the project's life.

Each of these is an estimate. Bad estimates produce wrong NPVs. Good NPV practice involves running the calculation under multiple cash-flow scenarios and reporting the range, not just a point estimate.

### The discount rate: also a judgment call

The other input — the discount rate — is at least as judgment-laden. In corporate finance, the standard answer is the firm's **weighted average cost of capital (WACC)** — the blended cost of debt and equity weighted by the firm's capital structure. We'll compute WACC explicitly in Chapter 17.

But WACC itself depends on assumptions. The cost of equity comes from the **CAPM** (Chapter 14), which requires assumptions about the market risk premium and the firm's beta. The cost of debt comes from the firm's outstanding bonds, which may not be perfectly observable. Different reasonable analysts can produce 1–2 percentage point differences in estimated WACC for the same firm — and as we saw in the sensitivity table, that 1–2 points matters enormously.

For an equity research analyst, the discipline is:

1. Be transparent about the discount rate you used.
2. Compute NPV (or DCF value) at a few alternative rates to bound the answer.
3. Be honest about the range. A "valuation" expressed as a single number is usually overconfident.

### Real-options thinking

Finally, NPV in its standard form treats projects as fixed once started. Real projects often have flexibility — the option to expand if things go well, to shut down if they go badly, to delay the start. These flexibility features have value not captured in standard NPV. The field of **real options** addresses this. For the equity research project, this is mostly relevant when valuing companies with significant strategic flexibility — biotech firms with optional drug candidates, energy firms with optional extraction projects, growth firms with optional expansion paths. Standard NPV understates the value of such flexibility. Chapter 16 returns to real options briefly.

↳ **Dig Deeper — Terminal value dominance in DCF**

*A typical 5-year DCF has a terminal value that represents 60-80% of the total computed value. Year-by-year forecasts get most of the analytical attention, but the terminal value is doing most of the heavy lifting. This raises an uncomfortable question: how reliable is a valuation whose answer is dominated by a single perpetuity assumption?*

**Prompt:**
> Compute terminal value as a percentage of total firm value for three different DCF setups: (a) 5-year explicit forecast, 3% terminal growth, 9% WACC; (b) 10-year explicit forecast, 3% terminal growth, 9% WACC; (c) 5-year explicit forecast, 4% terminal growth, 8% WACC. Show the percentages. Then argue: is the dominance of terminal value a feature or a bug of DCF, and what does it imply for analyst practice?

**What to do with the output:** Save it. We'll do real DCFs in Chapter 11; this perspective on terminal value will inform how you set your assumptions.

### The trade-off (concept 3)

NPV in practice trades **mathematical precision against forecasting honesty**. The discounting machinery is exact. The cash flows and the discount rate going into the machinery are estimates. A serious NPV analysis acknowledges this asymmetry — the math is precise, the inputs are not, and the output's reliability is bounded by the inputs.

### Worked example — NPV of a corporate capital project

Suppose your chosen company announces a $500M factory expansion expected to generate the following incremental free cash flows:

| Year | Cash flow ($M) |
|---|---|
| 0 | −500 |
| 1 | 80 |
| 2 | 100 |
| 3 | 130 |
| 4 | 150 |
| 5 | 150 |
| 6 | 130 |
| 7 | 100 |
| 8 (terminal) | 600 |

If the firm's WACC is 8%:

NPV = $\sum CF_t / (1.08)^t$

Working through year by year, you get an NPV of approximately +$284M. The project clears the firm's cost of capital by a wide margin and is value-creating.

If the firm's WACC is actually 12% (perhaps because the project is riskier than the firm's average operations), the NPV falls to about +$95M — still positive, but much less impressive.

For the equity research project: when your chosen company announces a major capex initiative, this is the analytical move. Estimate the cash flows, choose the discount rate, compute NPV, examine sensitivity. The NPV tells you whether the announcement is value-creating, and your reading goes into the report.

### Common misconceptions

- *"Once you've computed NPV, the decision is made."* NPV is one input. Strategic considerations, risk tolerance, and execution capability all matter too.
- *"NPV always gets it right."* The math is right. Whether the answer is right depends on whether the cash flow estimates and discount rate are right. Both are judgment calls.

---

## Synthesis — the TVM toolkit complete

Three chapters of TVM, building toward a single tool. Chapter 7 gave you the master formula for a single payment. Chapter 8 extended to equal-payment streams. Chapter 9 generalized to arbitrary cash flow streams and introduced NPV — the decision rule that takes all of this machinery and produces an actionable answer.

NPV is not the last word in finance. The remaining chapters refine and extend it:

- **Chapter 10** uses NPV-style discounting to price bonds.
- **Chapter 11** uses it to value stocks via DCF.
- **Chapter 14** computes the discount rate (cost of equity) more carefully via CAPM.
- **Chapter 16** applies NPV to capital budgeting decisions and introduces IRR formally.
- **Chapter 17** computes WACC — the standard discount rate.

For the equity research project, this chapter completes the technical foundation. By Chapter 11, you'll have built a DCF model for your chosen company. The model is, structurally, an NPV calculation: project the firm's free cash flows over a forecast horizon, choose a discount rate, sum the discounted cash flows. The output is the firm's intrinsic value. Compare to the market price; you have your investment thesis.

---

## Exercises

### Warm-up

**9.1** Define mixed stream. Why do real-world cash flows almost always require the mixed-stream approach rather than the closed-form annuity formula?

**9.2** State the NPV decision rule.

**9.3** Why is NPV expressed in today's dollars rather than future dollars?

### Application

**9.4** A project requires $200,000 today and produces:
- Year 1: $40,000
- Year 2: $60,000
- Year 3: $80,000
- Year 4: $80,000
- Year 5: $60,000

(a) Compute NPV at a 6% discount rate.
(b) Compute NPV at a 12% discount rate.
(c) At what discount rate does the project break even? (Solve approximately.)

**9.5** Two projects, each requiring $100,000 today:

| Year | Project A | Project B |
|---|---|---|
| 1 | $50,000 | $20,000 |
| 2 | $50,000 | $40,000 |
| 3 | $30,000 | $50,000 |
| 4 | $20,000 | $70,000 |
| 5 | $10,000 | $60,000 |

(a) Compute NPV for each at a 10% discount rate.
(b) Which project has the higher NPV?
(c) What does the comparison tell you about the relative timing of the two projects' cash flows?

**9.6** Use Excel's `NPV()` function to verify your answers to 9.4 and 9.5. Confirm that you correctly handle the initial investment outside the function.

### Synthesis

**9.7** Identify a recent major capital expenditure announcement from your chosen company (a new factory, a major acquisition, a new product launch with disclosed expected economics). Estimate the cash flows. Estimate a reasonable discount rate. Compute NPV. Argue whether the project is likely to be value-creating.

**9.8** A friend says: "NPV is too sensitive to the discount rate. The whole exercise is just garbage in, garbage out." Construct (a) a defense of NPV that takes the criticism seriously, and (b) a description of how a sophisticated analyst handles the sensitivity. What does the criticism get right? What does it get wrong?

### Challenge

**9.9** A project produces the following cash flows:

| Year | Cash flow |
|---|---|
| 0 | −$100,000 |
| 1 | $300,000 |
| 2 | −$250,000 |

(a) Compute NPV at 5%, 25%, and 50%.
(b) The IRR can be defined as a discount rate that makes NPV = 0. How many such rates does this project have? (Hint: there can be more than one.)
(c) What does this tell you about the limitations of IRR as a decision rule when cash flows change sign more than once?

**9.10** Build a DCF-style NPV in Excel for a hypothetical company:
- Year 1 free cash flow: $50M, growing at 8% for years 2–5.
- Years 6–10: 5% growth.
- Year 10 terminal value: 12× year-10 FCF.
- Discount rate: 9%.

Compute the present value. Then examine sensitivity by varying the discount rate from 7% to 11% in 0.5% increments. By how much does the present value change? What does this tell you about how much confidence to place in any single DCF estimate?

---

## Chapter summary

- The general formula for the present value of a mixed cash flow stream:
  $$PV = \sum_{t=0}^{n} \frac{CF_t}{(1+r)^t}$$
- The general formula for the future value of a mixed stream:
  $$FV = \sum_{t=0}^{n} CF_t \cdot (1+r)^{n-t}$$
- **Net present value (NPV)** is the sum of all present-valued cash flows, including the initial investment as a negative entry.
- **NPV decision rule**: accept if NPV > 0; reject if NPV < 0.
- NPV is denominated in today's dollars.
- NPV is highly sensitive to the discount rate. Always test multiple rates.
- The discount rate at which NPV = 0 is the **internal rate of return (IRR)** — covered in detail in Chapter 16.

---

## What would change my mind

The chapter argues NPV is the right decision rule for evaluating investments with known cash flow streams. The reading would have to revise if (a) a competing decision rule (real-options-based valuation, e.g.) consistently outperformed NPV in real-world capital budgeting outcomes — there's a real literature here, and for projects with significant flexibility, real options is genuinely better; for most projects, NPV remains the standard, or (b) the assumption that future cash flows can be reasonably estimated broke down, in which case no formal decision rule helps and judgment dominates. Both qualifications are real; neither displaces NPV as the workhorse.

## Still puzzling

The same puzzle as Chapter 7 returns: *what discount rate*? NPV's mathematical precision is wasted if the discount rate is chosen casually. WACC (Chapter 17) is the standard answer, but WACC is itself an estimate built on more estimates. In practice, the discount rate is often where the most sensitivity in the analysis lives, and the choice can drive a project from accept to reject without any change to the underlying business. I notice myself uncomfortable with how casually most discounted cash flow analyses choose this number; the discomfort is appropriate. Honest analysts say so.

---

## Connections forward

- **Chapter 10** uses mixed-stream NPV math to price bonds.
- **Chapter 11** uses it to compute DCF stock value.
- **Chapter 14** refines the discount rate via CAPM.
- **Chapter 16** applies NPV to corporate capital budgeting and introduces IRR formally.
- **Chapter 17** computes WACC.

---

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

**Frederick Macaulay** was developed the duration framework in 1938 — the standard tool for analyzing unequal multi-payment cash flows.

**Run this:**

```
Who is Frederick Macaulay, and how does their work connect to unequal cash flows we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about their career or ideas.
```

→ Search **"Frederick Macaulay"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to apply Frederick Macaulay's framework to a specific finance question.
- Add a constraint: "Answer including criticisms or limits of Frederick Macaulay's framework."

What changes? What gets better? What gets worse?
