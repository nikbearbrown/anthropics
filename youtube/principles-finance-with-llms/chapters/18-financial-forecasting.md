# Chapter 18 — Financial Forecasting

**Suggested titles**
1. Building the Pro Forma
2. Sales Drives Everything (and Cash Doesn't Always Follow)
3. Forecasting the Three Statements

**TL;DR.** A pro forma is a forecasted set of financial statements — income statement, balance sheet, and cash flow — typically built monthly for a year and quarterly or annually beyond that. The mechanics are sequential: forecast sales first, then derive income-statement items from sales (variable items as percentages, fixed items as dollar amounts), then build the balance sheet from accounting linkages, then build cash flow from payment/collection timing. The hardest lesson: **growing profits and growing cash are not the same thing.** Working capital and capex requirements can produce a cash crunch even as the income statement looks great.

---

## The puzzle of profitable but broke

A firm grows sales 30% in a year. The income statement shows record profit. Management celebrates. Three months into the next year, the bank calls — the firm has bounced a payroll check.

How does this happen?

Growth requires more *working capital*. Higher sales mean more inventory on hand, more receivables outstanding (because customers pay in 30-90 days while expenses are paid more quickly), and often more capex to support the growth. The cash these consume comes out of the firm's bank account *before* the increased profits arrive in cash form months later.

A growing firm with poor cash forecasting can be perfectly profitable on the income statement and out of cash in the bank. Many otherwise sound firms have died this way. **Profit isn't cash. Forecasting requires understanding both, and the timing of each.**

The discipline that prevents this is **pro forma forecasting** — building forward-looking financial statements that capture not just expected profitability but the cash flow needed to support it.

For the equity research project, this chapter is the engine that produces the cash flow forecasts going into your DCF. By Chapter 11 you knew what DCF mechanically requires. By Chapter 17 you had a discount rate. This chapter gives you the forecasted cash flows — the inputs that, combined with WACC, produce the firm's intrinsic value.

---

## Learning objectives

After working through this chapter, you should be able to:

- Build a 12-month pro forma income statement using the percentage-of-sales method.
- Construct a forecasted balance sheet using accounting linkages between sales, A/R, A/P, and inventory.
- Build a cash flow forecast using collection and payment timing.
- Identify cash crunch periods and quantify financing needs.
- Apply scenario and sensitivity analysis to test forecast robustness.
- Recognize when forecasting assumptions are unrealistic (the COVID-era forecasting failures are an example).

**Prerequisites.** Chapter 5 (financial statements), Chapter 6 (ratios), Chapter 17 (WACC).

---

## Concept 1 — Sales drives everything

Forecasting begins with sales. Almost every other line in the financial statements depends on sales — directly or indirectly.

### Forecasting sales

The starting point is historical sales data, ideally at monthly granularity for the past 24+ months. From that you extract:

**Trend.** What's the year-over-year growth rate? For Clear Lake Sporting Goods (the OpenStax running example), sales grew from $89K (2 years ago) to $105K (last year) to $126K (current year). That's roughly 18-20% annually.

**Seasonality.** Which months are high and which are low? Sporting goods retailers typically peak in summer and December. Clear Lake's June sales were 211% of January sales. Without recognizing seasonality, monthly forecasts will be systematically wrong.

**Adjustments.** What's known to be different next year that wasn't true historically? Discontinued products, new lines, expanded distribution, demographic shifts, competition entering or exiting, regulatory changes — all need explicit adjustments to the historical baseline.

For Clear Lake, the analyst's notes for next year:
- Old product line discontinued, expected -2% impact in Q1.
- New brand launching, expected to add $500 (March), $1K (April), $1.4K (May), $2K/month (June-August).
- New regulation may increase COGS up to 2% in Q4.

The percentage-of-sales method takes annual sales (forecasted at 18% growth = $148,680 for next year) and distributes it by month using the historical monthly percentages, then applies adjustments. For January at 7.1% of annual sales:

$$\text{January sales} = \$148{,}680 \times 7.1\% \times (1 - 0.02) = \$10{,}408$$

(The 2% reduction reflects the discontinued product impact.)

The same logic applies to every other month, with adjustments stacking where they apply.

### Why historical data is a starting point, not the answer

Past performance is the cheapest source of forecast input but rarely the right answer alone. Two pitfalls:

**Anomalous periods get baked in.** If your historical baseline includes an unusually strong year (say, 2021 retail with stimulus checks) or unusually weak (2020 retail under lockdown), naive extrapolation gets the wrong answer. Filter the baseline for anomalies before extrapolating.

**Mean reversion.** Industries don't grow indefinitely at high rates. A firm growing 25% per year will eventually slow as it gets large enough to be affected by market saturation, competition, and fundamental demand limits. Forecasts that assume current growth rates persist are usually too optimistic.

For your equity research project, the firm's own management forecasts (in earnings calls and 10-K guidance) are useful inputs. So are sell-side analyst consensus estimates. So is your bottom-up reading of competitive dynamics. The best forecast triangulates among all three.

### Worked example — Big 5 Sporting Goods

Big 5 (a real public competitor) reported $1,041.2M in 2020 sales vs. $996.5M in 2019 — 4.5% growth. That growth was substantially elevated by COVID-era demand for outdoor goods. An analyst building a forecast for 2021 would have to decide: was 2020 a one-time bump that mean-reverts (likely), or has the firm gained durable share (less likely)? The decision drives the forecast.

In retrospect, 2021 saw partial mean reversion as outdoor-recreation spending normalized. Forecasting analysts in late 2020 who assumed 2021 sales would simply repeat 2020 were systematically too optimistic.

↳ **Dig Deeper — Why most forecasts are systematically too optimistic**

*A robust empirical finding: corporate forecasts (and analyst forecasts) are biased toward optimism. Revenue projections at year-end exceed actual results 60-70% of the time. The pattern holds across industries and decades. Behavioral economists have explanations; the practical question is what to do about it.*

**Prompt:**
> Summarize the empirical evidence on corporate forecast bias toward optimism. Key sources: Daniel Kahneman's "planning fallacy" framework, Bent Flyvbjerg's "reference class forecasting" approach to debiasing, and the analyst-consensus optimism literature. Then describe how Flyvbjerg's reference-class approach works in practice: identify the firm's class of comparable past projects, look at how they actually performed, use that distribution as your prior for the current project. What's the practical limit of this approach?

**What to do with the output:** Save it. When you build pro forma forecasts in Chapter 18's exercise, applying a reference-class adjustment to the management-guided forecast may meaningfully change your conclusions.

### The trade-off (concept 1)

Sales forecasting trades **fidelity to known patterns against acknowledgment of uncertainty**. A forecast that uses only historical data is precise but probably wrong. A forecast that incorporates many adjustments may be more accurate but is also more vulnerable to bias. The discipline: document each adjustment, justify it, and run sensitivity to test how much each one moves the answer.

### Common misconceptions

- *"Forecasting just means extrapolation."* Extrapolation is the easy part. The hard part is identifying when extrapolation is wrong and adjusting.
- *"More data is always better."* For mean-reverting series, recent data dominates. For trends, longer history helps. The right window depends on what you're forecasting.

---

## Concept 2 — From sales to the three statements

Once sales are forecasted, the rest of the statements derive from them through accounting linkages.

### The pro forma income statement

The basic structure: variable costs (which scale with sales) get forecasted as percentages; fixed costs get forecasted as dollar amounts.

**Variable cost lines:**
- COGS (cost of goods sold) — typically 40-70% of sales for retailers, 20-50% for manufacturers, much lower for software firms.
- Sales commissions — explicit percentage of sales.
- Direct labor for variable production — scales with output.

**Fixed cost lines:**
- Rent — fixed by lease.
- Salaries (excluding sales commissions) — set by employment contracts.
- Insurance, certain professional fees — fixed amounts.
- Depreciation — set by capex schedule and depreciation method.

For Clear Lake, the pro forma income statement for January:

| Line | Method | Amount |
|---|---|---|
| Sales | Forecasted | $10,408 |
| COGS | 50% of sales | $5,204 |
| Gross profit | Subtraction | $5,204 |
| Rent | Fixed | $458 |
| Salaries | Fixed (with 4% raise) | $468 |
| Depreciation | Fixed schedule | $300 |
| Utilities | Spread of annual | $204 |
| Operating income | Subtraction | $3,774 |
| Interest | Fixed | $167 |
| Tax | 21% of pre-tax income | $758 |
| Net income | | $2,849 |

Repeat for each month, adjusting for known changes (rent increases, depreciation changes, new product launches).

### The pro forma balance sheet

The balance sheet is harder because it's a snapshot at a point in time, and several lines are tied to sales through *timing* relationships rather than direct percentages.

The key linkages:

**Accounts receivable** = sum of sales not yet collected. If the firm offers net-90 payment terms, A/R at month-end equals current month + prior 2 months of sales.

**Inventory** = stock on hand to support coming months' sales. A firm carrying 4 months of inventory (typical for some seasonal retailers) holds inventory equal to the next 4 months' COGS. The pattern can vary by month — more inventory ahead of the busy season, less in the off-season.

**Accounts payable** = recent expenses not yet paid. With net-30 supplier terms, A/P at month-end equals last month's COGS.

**Equipment (net)** = prior month's net equipment − this month's depreciation + new capex.

**Retained earnings** = prior month's retained earnings + this month's net income − dividends paid.

**Cash** = the *plug variable* that makes the balance sheet balance.

The plug logic: total assets must equal total liabilities + equity. Once you've forecasted every other line, cash is whatever value forces the equation. If cash comes out positive, the firm has surplus cash. If cash comes out negative, the firm needs financing.

For Clear Lake's pro forma year:
- Year-end cash: $59,900 surplus.
- Midyear (June) cash: just $8,800 — barely above the firm's $35,000 minimum cash policy. The firm needs short-term borrowing to bridge the gap.

The midyear deficit is the pro forma's most valuable output: it identifies when financing is needed *before* the firm runs out of cash. Without the forecast, the cash crunch is a surprise. With it, the firm can arrange a line of credit or other working capital financing in advance.

### The pro forma cash flow statement

Strictly speaking, the cash flow statement falls out of the income statement and balance sheet via accounting reconciliation — net income plus noncash items plus working capital changes equals cash from operations. But for forecasting purposes, building it directly from collection and payment timing is often clearer.

**Cash inflows:**
- Sales collections (with the lag from credit terms — 30, 60, or 90 days after sale).
- Investment proceeds, financing inflows.

**Cash outflows:**
- A/P payments (current expenses paid 30 days later).
- Salaries (paid roughly when accrued).
- Capex (paid when equipment is delivered).
- Tax (paid quarterly or annually).
- Interest (paid on schedule).
- Dividends (paid when declared).

For Clear Lake, March's cash outlay exceeds inflows by about $13K (because March has high inventory build for the upcoming summer season). The firm starts the month with cash; ends below the $35K minimum policy. Solution: arrange $5K of short-term borrowing for March, which gets repaid in April when collections catch up.

### Why this matters for the project

For your equity research DCF in Chapter 11, the cash flows you discount are exactly these forecasted free cash flows. The discipline of building the pro forma — explicitly forecasting every component, recognizing seasonality, accounting for working capital — produces much better forecasts than naive extrapolation of past free cash flow.

A specific recommendation for the project: build a 5-year annual pro forma income statement and balance sheet for your chosen company. Use historical ratios as starting points. Adjust for management guidance and your view of the firm's future. The free cash flows that fall out of the pro forma are your DCF inputs.

↳ **Dig Deeper — Using Monte Carlo simulation in forecasting**

*A point estimate is overconfident. A three-scenario forecast is better. A Monte Carlo simulation, which runs thousands of scenarios with assumptions drawn from probability distributions, is better still — when the underlying assumptions can be reasonably modeled.*

**Prompt:**
> Explain how Monte Carlo simulation works for financial forecasting. Set up a simple example: 5-year revenue projection where annual growth is drawn from a normal distribution with mean 8% and std dev 5%. Run 1000 simulations. What does the distribution of terminal-year revenue look like? Then describe two practical limits: (1) how the assumed distribution shape affects results (normal vs. log-normal vs. fat-tailed), (2) the danger of "garbage in, garbage out" — sophisticated simulations of poorly-justified assumptions.

**What to do with the output:** Save it. Monte Carlo is intermediate-quant content; sensitivity analysis (Chapter 18) is the principles-level version. Knowing both is useful.

### The trade-off (concept 2)

Pro forma construction trades **realistic complexity against analytical effort**. A simple percentage-of-sales forecast can be built in an hour. A detailed monthly forecast with seasonality, working capital lags, and capex schedules takes much longer but identifies cash crunches a simple version misses. For investment decisions and lending decisions, the detailed version is worth the effort. For first-pass thinking, the simple version is enough.

### Common misconceptions

- *"The balance sheet should always balance."* It will, after the cash plug. Whether the cash plug is positive or negative is the analytical signal.
- *"Pro forma cash flow is just net income plus depreciation."* That's a rough approximation. Working capital changes can be larger than depreciation in growth periods.

---

## Concept 3 — Stress-testing the forecast

A single pro forma is one possible future. Real forecasting builds multiple scenarios and tests sensitivity to key assumptions.

### Scenario analysis

A **scenario** is a coherent set of assumptions describing one possible future. Typical scenarios:

- **Base case** — the analyst's best-guess view.
- **Bear case** — significantly worse than expected (recession, key customer loss, regulatory hit).
- **Bull case** — significantly better than expected (market share gain, strong macro, new product success).

Each scenario produces its own pro forma. Compare the resulting net income and cash flow to assess the firm's resilience.

For Clear Lake, a recession scenario with sales falling 40%:
- Base case net income: $47.6K
- Recession case net income: $16.4K — a 65% drop.

Why does a 40% sales drop produce a 65% income drop? **Operating leverage.** Fixed costs (rent, salaries, depreciation) don't decline with sales. So the same dollar of sales loss produces a larger dollar of operating income loss. The recession's impact on the bottom line is amplified.

A firm with high operating leverage (high fixed costs relative to variable) is more vulnerable in downturns. A firm with low operating leverage is more resilient. This characteristic should be captured in your equity research thesis.

### Sensitivity analysis

A **sensitivity** changes one variable at a time to identify which inputs most affect the answer. Typical:

- Sales ±10% → how does net income change?
- COGS ±2 percentage points → how does net income change?
- WACC ±1 percentage point → how does DCF value change?

The variables that move the answer most are the ones the forecast depends most on. They deserve the most analytical attention.

For DCF specifically, the most sensitive inputs are typically:
1. WACC (already noted in Chapter 17).
2. Long-term growth rate (in the terminal value).
3. Operating margin in the explicit forecast period.
4. Capex intensity (in calculating FCF).

### What COVID-era forecasting taught

A real-world test of forecasting discipline. In early 2020, virtually every public company's forecasts for the year were dramatically wrong. Some industries (online retail, software-as-a-service) substantially outperformed; others (airlines, hotels, restaurants) substantially underperformed. The variance from forecasts was unprecedented.

The lessons:

**1. Tail events are real and matter.** Forecasts based on "normal" conditions are wrong precisely in the moments when the answer matters most.

**2. Scenario analysis matters more than point estimates.** Companies with explicit recession scenarios responded faster than those that hadn't considered the possibility.

**3. Cash flexibility is asymmetric protection.** Firms entering 2020 with strong cash positions and undrawn credit lines survived. Firms with high leverage and tight liquidity didn't, regardless of how good their pre-COVID forecasts had been.

For the equity research project, when you assess your chosen company's recent forecasting record, ask: did they update their forecasts quickly and honestly during 2020? Did they have explicit scenarios? Did they manage cash defensively? The behavior in stress periods tells you more about management quality than the smooth-sailing periods do.

### The trade-off (concept 3)

Scenario and sensitivity analysis trade **breadth of consideration against effort**. Building one base case is easier; building three scenarios each with explicit sensitivity is much more work. For investment decisions of significant size, the additional work pays off in resilient analysis. For routine planning, base case alone is often enough.

### Worked example — sensitivity on your project's DCF

For your equity research DCF, run sensitivity on:

- WACC: 7%, 8%, 9%, 10%
- Long-term growth: 2%, 3%, 4%
- Operating margin in year 5: -2%, base, +2%

Compute the implied fair value for each combination. Display as a 4×3 matrix. The range of values is your honest fair-value estimate.

If the matrix produces a range of $80-120 per share and the stock trades at $100, your conclusion is "fairly valued, with reasonable confidence." If the matrix produces $60-180, your conclusion is "wide range; high uncertainty; small position size warranted."

The matrix itself is the analytical output. Reporting only the base case is overconfident.

### Common misconceptions

- *"Sensitivity analysis produces too many numbers."* That's the point — it shows you which numbers matter. The analyst's job is to focus on the high-sensitivity inputs.
- *"Scenario analysis means picking the most likely outcome."* No — it means showing what happens under each scenario. Probability weighting comes after.

---

## Synthesis — pro forma as the analyst's working canvas

This chapter built the forward-looking equivalent of the financial statements from Chapter 5. Pro forma forecasting is:

1. **Sales-driven.** Forecast sales first; everything else derives from it.
2. **Linked.** Income statement → balance sheet → cash flow statement, with explicit accounting connections.
3. **Cash-aware.** Profit ≠ cash. Working capital timing matters. Pro forma cash flow identifies financing needs.
4. **Stress-tested.** Single point estimates are overconfident; scenarios and sensitivity analyze the range.

For the equity research project, this chapter delivers the cash flow forecasts that go into your DCF. Combined with WACC from Chapter 17, the DCF produces an intrinsic value estimate, which you compare to current market price for your investment thesis.

The next two chapters extend the analytical toolkit: Chapter 19 handles working capital management (relevant for the cash crunches Chapter 18 identified), and Chapter 20 handles risk management (relevant for the scenarios Chapter 18 stress-tests).

---

## Exercises

### Warm-up

**18.1** Define pro forma. Why are pro forma statements built monthly for the first year and annually thereafter?

**18.2** Distinguish variable cost lines from fixed cost lines in pro forma construction.

**18.3** Why might a growing firm have negative cash flow despite growing profits?

### Application

**18.4** A retailer expects $5M of annual sales next year, distributed seasonally:
- Q1: 15%
- Q2: 25%
- Q3: 25%
- Q4: 35%

Other assumptions: COGS 60% of sales; rent $30K/quarter (fixed); salaries $80K/quarter (fixed); depreciation $20K/quarter (fixed). Tax rate 21%.

(a) Build the quarterly pro forma income statement.
(b) Compute net income for each quarter and the year.
(c) Identify the quarter with the highest profit. Is it the same as the highest-sales quarter?

**18.5** Same retailer, with these additional assumptions for the balance sheet:
- A/R = 60 days of sales
- Inventory = 90 days of COGS
- A/P = 30 days of expenses
- Equipment $400K (declining $20K/quarter from depreciation)
- Beginning cash $50K
- Quarterly dividends $30K

(a) Build the quarterly pro forma balance sheet.
(b) Identify any quarter where cash falls below zero. What's the financing need?

**18.6** For your chosen company, build a 5-year annual pro forma:
(a) Forecast revenue using a defensible assumption about growth rate.
(b) Apply historical operating margin (or your adjusted estimate) to forecast operating income.
(c) Estimate capex and working capital changes.
(d) Compute free cash flow for each year.
(e) Use these as the cash flow inputs to your DCF.

### Synthesis

**18.7** A firm forecasts strong sales growth for the next 3 years, but its pro forma cash flow shows persistent negative free cash flow. Three possible interpretations: (a) the firm needs to raise capital; (b) the forecast is wrong (some line items are mismodeled); (c) the firm is making good investments that will pay off later. For each, identify what additional analysis would distinguish them.

**18.8** Build a recession scenario for your chosen company:
(a) What's a reasonable assumption for sales decline in a moderate recession?
(b) Under that scenario, what happens to operating income (consider operating leverage)?
(c) Does the firm have enough liquidity (cash + revolving credit) to weather it?

### Challenge

**18.9** Construct a sensitivity table for your DCF:
- Rows: WACC at 7%, 8%, 9%, 10%, 11%
- Columns: Terminal growth at 2%, 3%, 4%
- Cells: implied fair value per share

Report the range. What's the lowest and highest defensible value? How do these compare to the current market price?

**18.10** A firm announces 25% revenue growth for the next 3 years (driven by a new product line). The stock jumps 15% on the announcement.

(a) Build a pro forma model assuming the announced growth materializes.
(b) Build a model assuming half the announced growth.
(c) Compare the implied DCF values. By how much would the stock have to fall (under the less optimistic assumption) to return to the pre-announcement price?

---

## Chapter summary

- Pro forma forecasting builds forward-looking financial statements: income statement, balance sheet, cash flow.
- **Sales is the primary driver.** Variable costs scale with sales as percentages; fixed costs are dollar amounts.
- **Balance sheet linkages**: A/R = sum of unpaid sales; inventory = forward COGS; A/P = recent unpaid expenses; cash is the plug.
- **Cash flow is separate from profit.** Timing differences between accrual and cash matter, especially for growing firms.
- **Scenario analysis** tests coherent alternative futures (base, bear, bull cases).
- **Sensitivity analysis** changes one variable at a time to identify the most-impactful inputs.
- For your DCF, the pro forma cash flows are the inputs. Combined with WACC, they produce intrinsic value.

---

## What would change my mind

The chapter argues that pro forma forecasting with explicit scenario and sensitivity analysis is the right approach to financial planning. The reading would have to revise if (a) machine-learning-based forecasting consistently outperformed structured pro forma approaches — there's growing evidence in some specific applications (demand forecasting, fraud detection) but not for general-purpose financial forecasting, or (b) firms that skip detailed scenario work outperformed those that do — there's no evidence of this and considerable evidence to the contrary.

## Still puzzling

The genuinely hard question is *how to forecast against historical patterns when the patterns themselves may have changed*. The 2020-2024 inflation cycle broke many forecasting models that assumed continued disinflation. The 2025+ AI-productivity uncertainty makes forecasts of revenue growth, cost structures, and labor productivity highly uncertain. The discipline of using history as the baseline is good; the discipline of recognizing when history doesn't apply is harder. Honest forecasters say "I don't know" about specific structural shifts — and that admission is itself useful information.

---

## Connections forward

- **Chapter 19** addresses working capital management — the day-to-day handling of the cash crunch this chapter identifies.
- **Chapter 20** addresses risk management — defending against the scenarios this chapter stress-tests.

---

---

## LLM Exercise — Chapter 18: Five-Year Three-Statement Projection

**Project:** Equity Research Report on a Chosen Public Company
**What you're building this chapter:** A 5-year pro forma income statement, balance sheet, and cash flow statement under three scenarios. The cash flow projections become the inputs to the final DCF.
**Tool:** Excel + Claude Project.

### The Prompt

```
For [your company], build a 5-year pro forma forecast with three scenarios (base, bull, bear).

### Base case assumptions
- Revenue growth: from Chapter 11's analysis, plus management guidance
- Operating margin: most recent 3-year average, adjusted for known trends
- Tax rate: most recent effective rate
- Capex/revenue: most recent 3-year average
- Working capital changes: linked to revenue growth (use historical NWC/revenue ratio)

### Bull case
- Revenue growth +30% above base
- Operating margin +1 percentage point
- Other inputs same

### Bear case
- Revenue growth -30% below base (or recession scenario: -10% per year for years 1-2, then base)
- Operating margin -1 percentage point
- Other inputs same

### What I need you to produce

For each scenario, build out year-by-year:

**Income statement:**
- Revenue
- COGS, operating expenses, depreciation
- Operating income
- Interest, tax
- Net income

**Balance sheet (year-end):**
- Receivables (linked to revenue and historical DSO)
- Inventory (linked to COGS and historical days)
- Payables (linked to COGS and historical days)
- Capex flowing through to net PP&E
- Retained earnings = prior + net income - dividends
- Cash as plug variable

**Cash flow statement:**
- Net income + depreciation - changes in working capital - capex = free cash flow

### Deliverable

A consolidated table showing FCF for each year under each scenario. These FCFs become the inputs to your final DCF (combined with your WACC from Chapter 17).

Show all assumptions explicitly. Cite sources for any historical ratios.
```

### What this produces

A 5-year pro forma model with three scenarios. The FCFs go into the final DCF in your equity research report. Sensitivity around the assumptions becomes the bull/bear analysis in the executive summary.

### How to adapt this prompt

- *For your own company:* Replace [your company].
- *For ChatGPT / Gemini:* Identical.
- *For Claude Code:* Recommended for the Excel automation. Can write a script that takes assumptions and generates the full pro forma.

### Connection to previous chapters

Synthesizes Chapters 5 (statements), 6 (ratios), 11 (DCF), 17 (WACC). The output feeds the final DCF.

### Preview of next chapter

Chapter 19 examines working capital management. The Chapter 19 LLM Exercise will analyze your company's cash conversion cycle and operational efficiency.

---

**Tags:** pro-forma, forecasting, percentage-of-sales, scenario-analysis, sensitivity-analysis, working-capital, cash-flow-forecast


---

## AI Wayback Machine

**Wassily Leontief** was developed input-output economics — the foundation of modern industry-level financial forecasting. Nobel 1973.

**Run this:**

```
Who is Wassily Leontief, and how does their work connect to financial forecasting we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about their career or ideas.
```

→ Search **"Wassily Leontief"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to apply Wassily Leontief's framework to a specific finance question.
- Add a constraint: "Answer including criticisms or limits of Wassily Leontief's framework."

What changes? What gets better? What gets worse?
