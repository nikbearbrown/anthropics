# Chapter 18 — Financial Forecasting
*How a company can be profitable and out of cash at the same time.*

---

A firm grows sales 30% in a year. The income statement shows record profit. Management celebrates. Three months into the next year, the bank calls — the firm has bounced a payroll check.

This actually happens. It is not rare.

Here is the mechanism. Growth requires more working capital. Higher sales mean more inventory on hand, more receivables outstanding (customers pay in 30–90 days), and often more capital equipment to support the expanded operations. The cash these consume leaves the bank account *before* the profits arrive in cash form. The income statement records the profit when the sale happens; the cash statement records the inflow when the customer pays. In a fast-growing business, the gap between those two events can be large and persistent.

A firm can be perfectly profitable on the income statement and out of money in the bank. Many sound businesses have failed this way. The discipline that prevents it is **pro forma forecasting** — building forward-looking financial statements that capture not just expected profitability but the cash timing required to support it.

For the equity research project, pro forma forecasting is also how you produce the cash flow inputs to your DCF. By Chapter 11 you understood the DCF mechanics. By Chapter 17 you had a discount rate. This chapter gives you the forecasted free cash flows — the third piece.

---

## Sales drives everything

Pro forma forecasting begins with a single number: next year's sales. Almost every other line in the financial statements derives from it.

The starting point is historical sales data — ideally monthly, for the past two years or more. From that you extract three things.

**Trend.** What is the year-over-year growth rate? For Clear Lake Sporting Goods, the running example throughout this course, sales grew from $89K two years ago to $105K last year to $126K this year — roughly 18–20% annually.

**Seasonality.** Which months are high and which are low? Sporting goods retailers peak in summer and December. Clear Lake's June sales were 211% of January sales. Without recognizing seasonality, monthly forecasts will be systematically wrong — too high in the winter months, too low in summer — even if the annual total is approximately right.

**Adjustments.** What is known to be different next year that wasn't true historically? A discontinued product line, a new brand launch, expanded distribution, new regulation, a competitor entering or exiting the market. These cannot be read from past data. They must be explicitly added.

For Clear Lake, next year's adjustments include a discontinued product line (expected −2% impact in Q1), a new brand launching in spring (adding $500 in March, $1K in April, $1.4K in May, $2K/month from June through August), and a potential regulatory change that may increase COGS by up to 2% in Q4. Each adjustment is separate, documented, and subject to sensitivity analysis.

The **percentage-of-sales method** takes forecasted annual sales — in Clear Lake's case, 18% growth produces $148,680 — and distributes them by month using historical monthly percentages, then stacks adjustments. January historically accounts for 7.1% of annual sales, and the discontinued product reduces January 2% further:

$$\text{January sales} = \$148{,}680 \times 7.1\% \times (1 - 0.02) = \$10{,}408$$

The same logic runs through every month. The result is a 12-month sales forecast that carries the seasonality of the historical record plus the analyst's explicit view of what is different next year.

### Why historical data is a starting point, not the answer

Past performance is the cheapest forecast input but rarely the right answer alone. Two pitfalls show up consistently.

Anomalous periods get baked into the baseline. If historical data includes an unusually strong year — 2021 retail, boosted by stimulus checks — or unusually weak (2020 retail under lockdown), naive extrapolation produces the wrong number. The analyst has to identify and filter anomalies before extrapolating.

Trends mean-revert. Industries don't grow at high rates forever. A firm growing 25% per year will eventually slow as it approaches market saturation, faces stronger competition, or hits fundamental demand limits. Forecasts that assume current growth rates persist indefinitely are almost always too optimistic. The empirical record on this is consistent: corporate and analyst forecasts skew positive, revenue projections at year-end exceed actual results roughly 60–70% of the time across industries and decades.

The best forecast triangulates: historical trend as the baseline, management guidance as one input, bottom-up competitive analysis as another, sell-side consensus as a sanity check. No single source is the answer.

<!-- → [CHART: historical Clear Lake sales with seasonal pattern — monthly bars for two years plus first month of forecast year, showing the June peak and December secondary peak clearly — student should see what seasonality looks like in real data] -->

---

## From sales to the three statements

Once sales are forecasted, the income statement, balance sheet, and cash flow statement derive from them through explicit accounting linkages.

### The pro forma income statement

The structure is straightforward once you separate variable from fixed costs.

**Variable cost lines** scale with sales as percentages: cost of goods sold (typically 40–70% of sales for retailers, lower for software firms), sales commissions, direct labor for variable production. If COGS has historically been 50% of sales, forecast it at 50% of forecasted sales — subject to any known adjustments.

**Fixed cost lines** are dollar amounts that don't move with sales: rent (set by lease), base salaries (set by employment contracts), insurance, and depreciation (set by the capex schedule and depreciation method). These get forecasted as fixed amounts, occasionally adjusted for known changes (a lease renewal at higher rent, a planned salary increase).

For Clear Lake's January, the income statement builds like this: $10,408 in sales; COGS at 50% = $5,204; gross profit $5,204; then rent $458, salaries $468 (with an assumed 4% raise), depreciation $300, utilities $204; operating income $3,774; interest $167; pre-tax income $3,607; tax at 21% = $758; net income $2,849. Repeat for each month, with adjustments stacking where they apply.

### The pro forma balance sheet

The balance sheet is harder because it captures a point-in-time snapshot, and several lines are tied to sales through *timing* relationships rather than direct percentages.

The key linkages:

**Accounts receivable** equals the sum of sales that have been made but not yet collected. If the firm offers net-90 payment terms, the month-end A/R balance equals current-month plus prior two months of sales.

**Inventory** equals the stock on hand needed to support coming months' sales. A firm carrying 4 months of inventory holds stock equal to the next 4 months of COGS. The level varies seasonally — more inventory ahead of the busy season, less in the off-season.

**Accounts payable** equals recent expenses not yet paid to suppliers. With net-30 supplier terms, month-end A/P equals last month's COGS.

**Equipment (net)** = prior month net equipment − this month's depreciation + any new capex.

**Retained earnings** = prior month retained earnings + this month's net income − dividends declared.

**Cash** is the *plug variable* — the value that forces the balance sheet to balance. Total assets must equal total liabilities plus equity. After forecasting every other line, cash is whatever value is required to make the equation hold. Positive: the firm has surplus cash. Negative: the firm needs external financing.

<!-- → [TABLE: pro forma balance sheet construction example — columns: line item, linkage rule, Clear Lake January value, Clear Lake June value — student should see which items are calculated and how cash functions as the plug] -->

For Clear Lake's full-year pro forma, year-end cash comes out at $59,900 surplus. But the midyear picture is different: June cash is just $8,800 — well below the firm's $35,000 minimum cash policy. The firm needs short-term borrowing to bridge the midyear inventory buildup.

This is the pro forma's most valuable output: it identifies when financing is needed *before* the firm runs out of cash. Without the forecast, the cash crunch is a surprise. With it, the firm can arrange a credit line in January rather than panic-calling the bank in June.

### The cash flow statement

The cash flow statement falls out of the income statement and balance sheet through accounting reconciliation: net income plus noncash charges plus working capital changes equals cash from operations. But building it directly from collection and payment timing is often clearer for forecasting purposes.

Cash inflows: sales collections (with the credit-term lag), investment proceeds, financing inflows. Cash outflows: supplier payments (with the payment-term lag), payroll (paid when accrued), capex (paid when equipment is delivered), taxes (paid quarterly or at year-end), interest (on schedule), dividends (when declared).

The difference between accrual accounting and cash timing is the core of what the cash flow statement captures. A firm recording $10,408 of January sales on net-90 terms collects that cash in April. A firm paying its supplier net-30 pays its January COGS in February. The income statement records both in January. The cash flow statement records them when they actually move.

For Clear Lake, March's cash outflow exceeds inflows by about $13K because March involves heavy inventory build for the coming summer season. The firm starts March above its minimum cash requirement, ends March below it. Solution: $5K of short-term borrowing arranged in advance, repaid in April when summer collections catch up to expenses.

---

## Stress-testing the forecast

A single pro forma is one possible future. Real forecasting builds multiple scenarios and tests sensitivity to key assumptions.

### Scenario analysis

A scenario is a coherent set of assumptions describing one possible future. The standard set:

**Base case** — the analyst's best-guess view, calibrated to historical trends and management guidance.

**Bear case** — significantly worse than expected: recession, key customer loss, regulatory setback, margin compression from competition.

**Bull case** — significantly better than expected: market share gain, strong macro, new product success, margin expansion.

Each scenario produces its own pro forma. The resulting range of net incomes and cash flows shows the firm's resilience.

For Clear Lake, a recession scenario with sales falling 40% produces net income of $16.4K versus the base case's $47.6K — a 65% profit decline from a 40% sales decline. The amplification comes from **operating leverage**: fixed costs (rent, salaries, depreciation) don't fall when sales fall. Every dollar of lost revenue becomes a full dollar of lost gross profit; then fixed costs continue unchanged; operating income drops by more than gross profit. A firm with high fixed costs has high operating leverage and is more exposed in downturns. A firm with mostly variable costs has lower leverage and more resilience. This characteristic belongs in the equity research thesis.

<!-- → [TABLE: Clear Lake scenario comparison — rows: base case, recession case; columns: revenue, gross profit, operating income, net income, FCF — student should see the operating leverage amplification clearly] -->

### Sensitivity analysis

A sensitivity changes one variable at a time to identify which inputs most move the answer. For pro forma work: sales ±10%, COGS margin ±2 percentage points, capex ±20%. For DCF: WACC ±1 percentage point, long-term growth ±1 percentage point, operating margin in year 5 ±2 percentage points.

The variables that most affect the output are the ones the forecast depends most on — and the ones deserving the most analytical attention and the most honest uncertainty acknowledgment.

For DCF specifically, the most sensitive inputs are typically WACC, long-term growth rate, and operating margin in the explicit forecast period. A two-variable sensitivity table — WACC on one axis, terminal growth on the other — produces the honest range for fair value. If the matrix spans $80–120 per share and the stock trades at $100, the conclusion is "fairly valued, within the range of reasonable assumptions." If the matrix spans $60–180, the conclusion is "wide range; high uncertainty; this is a bet on the assumptions more than on the analysis."

<!-- → [TABLE: DCF sensitivity matrix — rows: WACC 7% through 11% in 1-point steps; columns: terminal growth 2%, 3%, 4%; cells: implied fair value per share — student should see how dramatically value moves and why single-point estimates are overconfident] -->

### What COVID-era forecasting demonstrated

A useful calibration: virtually every public company's forecasts for 2020 were dramatically wrong within weeks of being made. Some industries massively outperformed (online retail, software-as-a-service, home-improvement retail). Others suffered catastrophically (airlines, hotels, restaurants, commercial real estate). The variance was unprecedented in the modern era.

Three specific lessons that apply to any future forecasting:

Tail events are real. Forecasts built on "normal" conditions are wrong precisely in the moments when the answer matters most. Scenario analysis that explicitly models recession or disruption cases — rather than treating the base case as the only case — responds faster.

Scenario analysis matters more than point estimates. Companies with explicit recession scenarios built into their operating plans adapted quickly in March 2020. Companies whose entire planning apparatus assumed a continuation of 2019 conditions were still trying to understand what was happening when their competitors had already cut costs and drawn on credit lines.

Cash flexibility is asymmetric protection. Firms entering 2020 with strong cash positions and undrawn revolving credit facilities survived. Firms with high leverage and tight liquidity didn't, regardless of how good their pre-COVID forecasts had been. The cost of carrying excess liquidity in good times is low. The benefit in a crisis is existential. For the equity research project: when assessing a firm's resilience, the cash and credit capacity at any point in time is more important than the income statement for the prior year.

---

## The pro forma as the analyst's working canvas

Three chapters of TVM mechanics, two chapters of valuation, a chapter of cost of capital — all of it produces one number (WACC) and one requirement (future free cash flows). This chapter delivers the free cash flows.

The pro forma is the working canvas where those cash flows get built. Sales is the driver. Variable costs scale with it; fixed costs are anchored to dollar amounts. Accounting linkages connect the income statement to the balance sheet. Cash timing distinguishes what the income statement records from what actually moves through the bank. Scenario analysis acknowledges that the base case is one view among several that are plausible.

For the equity research project, the deliverable is a 5-year annual pro forma under base, bull, and bear scenarios. The free cash flows from each scenario go into the DCF with WACC from Chapter 17. The resulting range of intrinsic values — not a single point estimate but a range — is the honest output of the analysis. The job of the investment thesis is to argue why the stock's current market price is above, below, or within that range, and why.

---

## What would change my mind

The chapter argues that structured pro forma forecasting with explicit scenario and sensitivity analysis produces better decisions than simpler approaches. I would revise if (a) machine-learning-based forecasting consistently outperformed structured pro formas in general financial forecasting — there is growing evidence for specific applications (demand forecasting in retail, fraud detection) but not for the general financial-statement projection this chapter addresses — or (b) firms that skipped detailed scenario work systematically outperformed those that did it. There is no evidence of this; the COVID evidence runs strongly in the other direction.

## Still puzzling

The hardest forecasting question is how to use historical patterns as a baseline when the patterns themselves may have changed. The 2020–2024 inflation cycle broke many forecasting models that implicitly assumed continued disinflation. The current AI-productivity uncertainty makes forecasts of revenue growth, cost structures, and labor intensity highly unreliable. The discipline of using history as the baseline is good. The discipline of recognizing *when history doesn't apply* is harder and less teachable. Honest forecasters say so explicitly — and that admission is itself analytically useful.

---

## Connections forward

- **Chapter 19** addresses working capital management — the day-to-day operational handling of the cash timing gaps this chapter identifies.
- **Chapter 20** addresses risk management — formal tools for defending against the bear scenarios this chapter stress-tests.

---

## Exercises

### Warm-up

**18.1** Define pro forma. Why are pro forma statements typically built monthly for the first year and annually for years two through five? What is lost if you skip the monthly detail? *(Tests: definition and purpose of monthly granularity. Difficulty: low.)*

**18.2** Distinguish a variable cost from a fixed cost in pro forma construction. Give two examples of each for a sporting-goods retailer. Why does the distinction matter when sales decline 30%? *(Tests: variable vs. fixed cost mechanics and operating leverage intuition. Difficulty: low.)*

**18.3** What is the "cash plug" in a pro forma balance sheet? If the plug comes out negative, what does that tell you, and what should the analyst do with the information? *(Tests: balance sheet mechanics and financing-need identification. Difficulty: low.)*

### Application

**18.4** A retailer expects $5 million in annual sales, distributed seasonally (Q1: 15%, Q2: 25%, Q3: 25%, Q4: 35%). COGS is 60% of sales. Fixed costs: rent $30K/quarter, salaries $80K/quarter, depreciation $20K/quarter. Tax rate 21%. (a) Build the quarterly pro forma income statement. (b) Identify the quarter with the highest net income. Is it the same as the highest-revenue quarter? Why or why not? *(Tests: pro forma income statement construction with seasonality. Difficulty: medium.)*

**18.5** Same retailer, with these balance sheet assumptions: A/R = 60 days of sales; inventory = 90 days of COGS; A/P = 30 days of COGS; starting cash $50K; quarterly dividends $30K; equipment $400K declining $20K/quarter. (a) Build Q1 and Q2 pro forma balance sheets, using cash as the plug. (b) Identify whether the firm needs external financing at any point in the year. If so, how much and when? *(Tests: pro forma balance sheet construction and financing-gap identification. Difficulty: medium.)*

**18.6** A firm's income statement shows $2M net income last year. Its pro forma shows net income growing to $2.5M next year — but cash from operations is forecast to decline. Identify three specific line items or accounting linkages that could cause this pattern, and explain the mechanism behind each. *(Tests: accrual-vs-cash timing reasoning. Difficulty: medium.)*

### Synthesis

**18.7** Clear Lake's recession scenario produces a 65% profit decline from a 40% sales decline. (a) Explain the operating-leverage mechanism that causes the amplification. (b) A competitor firm has 80% variable costs and 20% fixed costs; Clear Lake has 60% variable and 40% fixed. For the same 40% sales decline, which firm's profit falls more? Show the arithmetic. (c) What strategic choices could reduce Clear Lake's fixed-cost exposure? *(Tests: operating leverage mechanics and strategic implications. Difficulty: high.)*

**18.8** For your chosen company, build a 3-year annual pro forma income statement under base and bear scenarios. Base: revenue growth at management-guided rate, current operating margin. Bear: revenue flat for two years, then base-case growth; operating margin compressed 2 percentage points. Compute free cash flow (net income + depreciation − capex − change in working capital) for each scenario. By how much do the year-3 FCFs differ? What does the gap imply for DCF valuation under each scenario? *(Tests: scenario construction applied to a real firm. Difficulty: high.)*

### Challenge

**18.9** Construct a 5×3 DCF sensitivity matrix for your chosen company: rows are WACC at 7%, 8%, 9%, 10%, 11%; columns are terminal growth at 2%, 3%, 4%; cells are implied fair value per share. (a) Report the range from the lowest to the highest cell. (b) Where does the current market price fall within the matrix? (c) At what combination of WACC and terminal growth does the stock appear fairly valued? What assumptions would have to hold for that to be the right discount rate and growth rate? *(Tests: DCF sensitivity matrix construction and interpretation. Difficulty: high.)*

**18.10** A firm announces 25% annual revenue growth for three years, driven by a new product launch. The stock rises 15% on the announcement. (a) Build a pro forma assuming the announced growth fully materializes. (b) Build a pro forma assuming only half the announced growth occurs. (c) Compute DCF intrinsic value under each. (d) How much would the stock have to fall — from the post-announcement price — to return to fair value under the pessimistic scenario? Is the market's 15% jump rational under your analysis? *(Tests: announcement analysis + scenario DCF + market-price interpretation. Difficulty: high.)*

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

**Wassily Leontief** developed input-output economics — the foundation of modern industry-level financial forecasting. Nobel 1973.

**Run this:**

```
Who is Wassily Leontief, and how does their work connect to financial forecasting we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about their career or ideas.
```

→ Search **"Wassily Leontief"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to apply Wassily Leontief's framework to a specific finance question.
- Add a constraint: "Answer including criticisms or limits of Wassily Leontief's framework."

What changes? What gets better? What gets worse?
