# Chapter 19 — Trade Credit and Working Capital in Planning
*Most firms' biggest loan isn't from a bank. It's from their suppliers.*

---

## The puzzle of negative working capital

Amazon, in many years, has had **negative working capital**.

Working capital is current assets minus current liabilities — the cash and short-term resources a firm needs to run its operations. Most firms have positive working capital because they need cash on hand, inventory in stock, and receivables waiting to be collected before customer payments arrive.

Amazon has the opposite. It collects payment from customers immediately — credit cards settle in 24 to 72 hours; Prime prepays. It turns inventory in days because of relentless logistics investment. And it pays suppliers on long terms, often 60 to 90 days. The result: Amazon is effectively *financed by its suppliers*. Each additional dollar of sales generates more cash today than it will require next month.

This isn't an accident. It's a deliberate operating model. Negative working capital means the firm needs *less* equity and debt to grow. Every dollar of additional revenue doesn't require a dollar of working capital investment — it generates working capital. For a firm growing 30% per year, the difference between a positive-CCC and negative-CCC operating model can mean the difference between needing billions in outside financing and self-funding the growth.

Most firms aren't Amazon. They have positive working capital, they need to manage it carefully, and the discipline of working capital management is one of the main reasons a firm's free cash flow differs from its net income.

---

## The cash conversion cycle

A firm's daily operations follow a sequence: spend cash on inventory → produce or stock → sell → wait for collection → cash arrives. The **cash conversion cycle (CCC)** measures how long that sequence takes — how many days the firm's cash is tied up before customers pay back.

$$\text{CCC} = \text{Days Inventory} + \text{Days Sales Outstanding} - \text{Days Payable}$$

Each term has a precise definition:

**Days Inventory** = $\frac{\text{Average Inventory}}{\text{COGS}} \times 365$

How many days a unit sits in stock before it's sold.

**Days Sales Outstanding (DSO)** = $\frac{\text{Average Accounts Receivable}}{\text{Credit Sales}} \times 365$

How many days from sale to cash collection.

**Days Payable Outstanding (DPO)** = $\frac{\text{Average Accounts Payable}}{\text{COGS}} \times 365$

How many days from purchase to when the firm pays its supplier.

The logic of the formula: you start spending when you pay suppliers (end of DPO). You stop waiting when you collect from customers (end of DSO after the inventory has turned). The gap is your cash tied up.

<!-- → [DIAGRAM: Timeline showing the cash conversion cycle — horizontal axis from day 0 to day 90+; arrows marking: Purchase inventory (day 0), Pay supplier (day DPO), Sell inventory (day DPO + Days Inventory), Collect from customer (day DPO + Days Inventory + DSO); brace labeled "Cash conversion cycle" spanning from Pay supplier to Collect from customer; student should see that increasing DPO or decreasing Days Inventory or DSO each independently shortens the cycle] -->

### A worked example

A firm with annual COGS of $30M, credit sales of $40M, average inventory of $3M, average accounts receivable of $6M, and average accounts payable of $2.8M:

- Days Inventory: $(3/30) \times 365 = 36.5$ days
- DSO: $(6/40) \times 365 = 54.75$ days
- DPO: $(2.8/30) \times 365 = 34.07$ days
- **CCC: $36.5 + 54.75 - 34.07 = 57.18$ days**

The firm's cash is tied up for about 57 days. Every dollar of sales requires 57 days of working capital financing. That's the status quo cost of this particular operating model.

### The three levers

Management has three things it can pull to shorten the cycle:

**Reduce inventory days.** Just-in-time logistics, better demand forecasting, reducing SKU counts. The trade-off is stockout risk — run lean enough and a supply disruption leaves you with nothing to sell.

**Reduce DSO.** Tighter credit policy, early-payment discounts, better collections. The trade-off is lost sales to customers who needed longer terms.

**Increase DPO.** Negotiate longer payment terms with suppliers. The trade-off is damaged supplier relationships if pushed past what they can absorb; suppliers eventually compensate through higher prices or reduced priority.

If the example firm improves to average inventory $2.8M, average AR $5.5M, average AP $3.3M — modest improvements across all three:

- Days Inventory: 34.1 days
- DSO: 50.2 days
- DPO: 40.2 days
- **CCC: 44.1 days** — 13 days shorter

Each day shortened frees roughly $30M / 365 ≈ $82K of working capital. Thirteen days is $1.07M of cash released without any change in revenue or cost. This is operational finance — value creation through efficiency rather than investment.

<!-- → [TABLE: CCC improvement worked example — two columns: Before and After — rows for each input (Avg inventory, Avg AR, Avg AP), each computed metric (Days inventory, DSO, DPO), and the resulting CCC; final row shows cash freed = (days shortened) × (COGS/365); student should see that modest improvements across all three levers compound into meaningful cash release] -->

### Industry variation

Cash conversion cycles vary enormously by industry structure, and the right benchmark for any given firm is its peers, not some universal ideal.

<!-- → [TABLE: Industry CCC benchmarks — rows for 7-8 industries: Software/SaaS, Restaurants, Big-box retail, General retail, Manufacturing, Construction, Heavy equipment leasing — columns: Typical CCC range, Key driver, Why it's this way — student should be able to quickly locate any firm in the spectrum and assess whether its CCC is normal or an outlier] -->

Software and SaaS companies often approach zero or negative — services prepaid, minimal inventory. Restaurants are typically negative — customers pay instantly, suppliers wait 30 days. Big-box retail (Walmart, Costco) is roughly zero through aggressive supplier terms and fast inventory turns. Manufacturing runs 60–150 days depending on production cycle complexity. Construction can exceed 200 days.

For your equity research project: compute your company's CCC and compare to its industry peers. A firm with materially longer CCC than peers is using more capital to fund the same operations — a real efficiency gap. A firm with materially shorter CCC may be operationally elite — or may be squeezing suppliers in ways that backfire.

↳ **Dig Deeper — Just-in-time and the 2020–2022 supply chain stress test**

*Just-in-time inventory was the operating doctrine that won the 2010s. Then COVID-19, the Suez Canal blockage, the Russia-Ukraine war, and chip shortages all stress-tested it. Firms with the leanest inventories suffered most.*

**Prompt:**
> Explain the just-in-time inventory framework as it dominated 2000–2020 corporate operations. Then walk through three specific 2020–2022 supply chain disruptions (COVID auto-industry chip shortage, Suez Canal blockage of March 2021, Ukraine war commodity disruption) and how they affected firms with different inventory strategies. Has corporate inventory management structurally shifted? Cite specific firm examples of strategy changes.

**What to do with the output:** Save it. When evaluating your project company's working capital, consider whether its CCC reflects 2010s-style optimization that may be miscalibrated for the current era.

---

## Trade credit: the most expensive "free" money in finance

Most firms' largest source of short-term financing is not a bank loan. It's accounts payable — money owed to suppliers that hasn't been paid yet. Trade credit is **spontaneous financing**: it grows automatically with sales, requires no application, charges no stated interest.

The no-stated-interest part deserves scrutiny.

### The standard discount offer

Many suppliers offer early-payment discounts. The common format is **2/10 net 30**: pay within 10 days for a 2% discount, or pay the full amount within 30 days.

If you choose to wait until day 30, you're borrowing for 20 extra days — the gap between the discount window and the final due date — at a 2% premium. What does that 2% over 20 days cost in annualized terms?

$$\text{Implicit APR} = \frac{360}{\text{Net days} - \text{Discount days}} \times \frac{\text{Discount \%}}{100\% - \text{Discount \%}}$$

For 2/10 net 30:

$$\text{APR} = \frac{360}{30 - 10} \times \frac{2}{98} = 18 \times 0.0204 = 36.73\%$$

The implicit cost of forgoing a 2/10 net 30 discount is **36.73% per year.** This is not exotic high-yield debt. This is the standard payment terms at a hardware supplier, a food distributor, a print shop.

If the firm has access to a bank line of credit at 8%, it should always borrow from the bank and take the discount. The decision to forgo the discount is a choice to borrow at 36.73% when cheaper alternatives are available. Most healthy firms should never forgo these discounts.

<!-- → [TABLE: Implicit APR for common discount terms — rows for 1/10 net 30, 2/10 net 30, 2/15 net 45, 3/10 net 60 — columns: Discount %, Discount window, Net terms, Borrowing days, Implicit APR — student should see that the implicit cost is always very high and always should be compared to the firm's actual borrowing rate] -->

### When forgoing is rational

The only time forgoing a discount makes sense is when the firm has no cash and no access to cheaper credit — when paying in 10 days would cause a cash crunch that bank credit can't solve. In that case, the firm is effectively using trade credit as emergency financing. It's expensive but available.

For distressed firms, suppliers can become the lender of last resort. This is why late payment to suppliers is an early warning signal for financial distress — the firm is borrowing at 36% because no one cheaper will lend.

A worked example: a firm buys $10,500 of inventory on 2/10 net 30 terms. Pay in 10 days: $10,500 × 0.98 = $10,290 (save $210). Pay in 30 days: $10,500. The $210 savings on $10,290 effectively borrowed for 20 days is exactly the 36.73% annualized. If the firm has any access to bank credit, it takes the discount.

↳ **Dig Deeper — Supply chain finance and reverse factoring**

*Beyond traditional trade credit, large buyers can offer suppliers early payment through a third-party financier while the buyer pays the financier on its own longer terms. This "reverse factoring" is a $1.5T+ market that has caused spectacular failures — notably Greensill Capital in 2021.*

**Prompt:**
> Explain how reverse factoring (supply chain finance) works mechanically. Why does it appeal to buyers (extends payables without supplier-relationship damage) and to suppliers (faster cash)? Then summarize the Greensill Capital collapse of March 2021: what made the firm's model fragile, and why does the case suggest that supply chain finance can hide leverage rather than reduce it?

**What to do with the output:** Save it. Some of your project company's "trade payables" may include reverse factoring; understanding the structure matters for assessing the firm's true short-term liquidity position.

---

## Cash management and the rolling budget

Working capital management produces one ultimate output: the firm's cash position over time. The tool for managing that output is the **cash budget**.

### Why firms hold cash

Four motives, each legitimate:

**Transactional** — paying bills, payroll, suppliers. The daily operating need.

**Precautionary** — unexpected repairs, demand spikes, supply disruptions. Insurance against known unknowns.

**Speculative** — sudden acquisition opportunities, distressed asset purchases, strategic buys at favorable prices. Capacity for opportunistic action.

**Compensating** — minimum balances required by lenders. A bank may require a $50K average balance against a $500K credit line.

A firm with too little cash misses opportunities and can't absorb shocks. A firm with too much cash earns near-zero on idle balances that should be deployed in operations or returned to shareholders. The right level depends on the firm's cash flow volatility, growth rate, and access to alternative liquidity.

### Where excess cash goes

Sitting on raw cash earns near-zero. Firms with excess holdings typically park them in **cash equivalents** — instruments that are safe and liquid but earn slightly more than a checking account:

- **US Treasury bills** — 3-month or 6-month maturities, default-risk-free in nominal terms, exempt from state and local income tax.
- **Federal agency securities** — Fannie Mae, Freddie Mac; slightly higher yields than Treasuries, near-Treasury credit quality.
- **Bank CDs** — certificates of deposit; higher yields, modest illiquidity (typically 30-360 day terms).
- **Commercial paper** — large corporates lending to each other; 30-270 day terms.
- **Money market mutual funds** — pools of the above, suitable for smaller firms.

Apple's $191B cash hoard is invested across these instruments to maximize yield while preserving the liquidity needed to fund ongoing operations and opportunistic acquisitions.

### The rolling cash budget

A **cash budget** is a forward-looking forecast of cash inflows and outflows, typically monthly for the coming year. **Rolling** means it's continuously updated: when one month's actuals arrive, that month drops off the front, a new month is added at the back, and the horizon stays 12 months ahead.

Components:

- **Cash collections**: receipts from sales (lagged by the DSO), interest on invested cash, dividends from investments.
- **Cash disbursements**: supplier payments (lagged by DPO), salaries, rent, utilities, taxes, debt service, dividends.
- **Net cash flow** = collections − disbursements.
- **Cumulative cash position** at each month-end.

If the cumulative position drops below the firm's minimum cash policy in any month, the firm needs short-term financing. If it's persistently above, the firm has surplus to invest or return.

<!-- → [TABLE: Simple rolling cash budget template — rows for 6 months — columns: Month, Opening cash, Collections (lagged 30 days), Disbursements (COGS + fixed + taxes), Net flow, Closing cash, Financing needed (if closing < minimum) — annotations showing where seasonal variation creates a deficit month and how the line of credit covers it] -->

### Short-term financing when the budget shows a deficit

When the rolling budget identifies a cash shortfall:

**Revolving line of credit** — pre-arranged with a bank; the firm draws as needed, repays when cash improves. Interest typically at prime plus a small spread. The standard tool for working-capital fluctuations.

**Commercial paper** — for large public firms with high credit ratings; cheaper than bank credit, but only available to investment-grade issuers.

**Factoring** — selling receivables to a finance company at a discount. Expensive but immediate; useful for firms without bank access.

**Trade credit extension** — stretch payables further. Free if suppliers tolerate it; costly to supplier relationships if pushed too far.

For the equity research project: find your chosen company's revolving credit facility in the 10-K's debt footnote. It tells you how much liquidity buffer management has arranged. A firm with $5B in revolving credit and clean covenants has substantially more flexibility in a stress scenario than one with $500M and tight covenant restrictions.

<!-- → [TABLE: Short-term financing options comparison — rows: Revolving line of credit, Commercial paper, Factoring, Trade credit extension, Asset-based lending — columns: Typical cost (APR), Who can access it, Speed of access, Key risk or trade-off — student should be able to match any firm's situation to the appropriate financing source and understand why distressed firms end up with the most expensive options] -->

---

## The working capital picture as a whole

Three concepts, one system.

The **cash conversion cycle** measures operating efficiency — how long cash is tied up before it comes back through customer collections. Shorter is better, with resilience trade-offs.

**Trade credit** is the dominant source of short-term financing for most firms, and its implicit cost (forgoing discounts) is far higher than bank credit. Healthy firms pay early; distressed firms reveal their distress by failing to take discounts.

The **rolling cash budget** integrates these into a forward view, identifying which months require financing and how much, and flagging months of surplus that should be deployed rather than left idle.

For the equity research project, this chapter provides the operational efficiency lens. Compute your company's CCC and compare to peers. Check cash holdings against operating cash flow — too high flags potential capital inefficiency; too low flags liquidity fragility. Read the MD&A's working capital discussion for management's own framing.

The numbers here often explain why the company's free cash flow diverges from its net income — and that divergence, in many cases, is the most important analytical question you can ask about an operating business.

---

## What would change my mind

The chapter argues the cash conversion cycle is the right master metric for working capital management, and that firms should generally shorten it aggressively through inventory reduction, faster collections, and extended payables. The argument would have to revise if supply-chain disruption made lean-CCC firms systematically underperform over sustained periods — there's meaningful post-2020 evidence pointing in this direction. The dominant strategy remains low-CCC in stable conditions, but the resilience trade-off deserves more weight than it received in the 2010s optimization era.

## Still puzzling

The hardest unsolved practical question is how lean working capital should actually be. Negative CCC is theoretically optimal but requires supplier squeeze that can backfire: suppliers raise prices, deliver last, or fail in a crisis. The 2020–2022 supply chain crisis was, in part, the bill coming due for years of just-in-time optimization that left no slack. The optimal CCC depends on stress tolerance the firm can't fully measure in normal times. Honest practitioners run scenarios; smart ones build redundancy into supplier relationships even when the immediate cost looks unjustified.

---

## Connections forward

- **Chapter 20** addresses risk management — including the supply-chain and liquidity risks this chapter touches on.

---

## Exercises

### Warm-up

**19.1** State the cash conversion cycle formula. Define each component in one sentence. What does a negative CCC mean operationally, and name one firm known for achieving it.

**19.2** Compute the implicit APR for forgoing each of the following trade credit discounts. Show the formula and result for each.

(a) 1/10 net 30
(b) 2/10 net 30
(c) 3/15 net 60
(d) 2/10 net 45

**19.3** Name the four motives for holding cash. For each, give a one-sentence example of a firm type where that motive would be especially important.

### Application

**19.4** A firm has the following annual figures: credit sales $120M, COGS $75M, average inventory $9M, average accounts receivable $18M, average accounts payable $6M.

(a) Compute days inventory, DSO, DPO, and CCC.
(b) The firm's daily working capital requirement is approximately COGS/365. How many dollars of working capital are tied up in the current CCC?
(c) If management reduces average inventory to $7M and average AR to $15M while increasing average AP to $8M, compute the new CCC. How much working capital is freed?

**19.5** A supplier offers your firm terms of 2/10 net 45.

(a) Compute the implicit APR of forgoing the discount.
(b) Your firm has access to a revolving line of credit at 9%. Should you take the discount? Explain.
(c) Your firm is in financial distress and the bank has frozen the line of credit. Does your answer change? Why?

**19.6** For your chosen company, compute days inventory, DSO, DPO, and CCC for the most recent fiscal year using the balance sheet and income statement. Then find the same metrics for two peers in the same industry. Which firm manages working capital most efficiently? What specific component drives any difference?

### Synthesis

**19.7** Amazon's CCC is typically negative; a mid-size regional retailer's CCC might be 60 days. Construct a financial analysis comparing the two: how much additional equity or debt does the regional retailer need to fund the same $1M of revenue growth that Amazon funds with supplier money? What does this imply about Amazon's required return on equity?

**19.8** A firm is growing at 40% per year with a CCC of 75 days and COGS of $200M annually. Estimate the working capital funding required to support the next year's growth. If the firm's WACC is 10%, estimate the annual cost of that working capital. Now estimate the same cost if management reduced CCC to 45 days. Is the 30-day improvement worth pursuing?

### Challenge

**19.9** Build a 12-month rolling cash budget for a hypothetical retail firm:
- Monthly sales ranging from $150K (January) to $350K (November/December), with a mid-year dip.
- Collections lagged 30 days; payables lagged 45 days.
- COGS 60% of sales; fixed operating expenses $40K/month; quarterly tax payments of $25K each.
- Beginning cash balance: $80K; minimum cash policy: $60K.

Identify any months where additional financing is needed and quantify the shortfall. What revolving credit facility size would be adequate?

**19.10** The Greensill Capital collapse (March 2021) involved reverse factoring arrangements where suppliers were paid early by Greensill while buyers paid Greensill on extended terms. Research the collapse and answer: (a) how did this arrangement affect the buyers' reported accounts payable, (b) why might an analyst looking only at published DPO figures have underestimated buyer leverage, and (c) what should analysts look for in footnotes to detect reverse factoring arrangements that may be obscuring true payable periods?

---

## LLM Exercise — Chapter 19: Working Capital Assessment

**Project:** Equity Research Report on a Chosen Public Company
**What you're building this chapter:** A working-capital assessment for your company — cash conversion cycle, peer comparison, and assessment of operational efficiency.
**Tool:** Claude Project.

### The Prompt

```
For [your company], using the financial statements I have:

1. **Compute the cash conversion cycle** for the most recent fiscal year:
   - Days inventory = (Average inventory / COGS) × 365
   - DSO = (Average AR / Credit sales) × 365 (or use total revenue if credit sales not disclosed)
   - DPO = (Average AP / COGS) × 365
   - CCC = Days inventory + DSO - DPO

2. **Compute the historical trend** — Repeat for the prior 2 years. Is CCC increasing or decreasing? What's driving the change?

3. **Peer comparison** — Compute CCC for 2-3 peer firms in the same industry. How does the firm's CCC compare?

4. **Working capital efficiency assessment**:
   - Is the CCC industry-typical, leaner than peers, or longer than peers?
   - If leaner: is the efficiency sustainable, or could it indicate stress (e.g., squeezing suppliers)?
   - If longer: what specific component (inventory, receivables, payables) is the drag?

5. **Cash holdings assessment** — From the 10-K, what's the firm's cash and short-term investments balance? How does this compare to:
   - Annual operating cash flow
   - Total revenue
   - The amount needed for working capital

6. **Implications for valuation** — Is excess cash on the balance sheet effectively deadweight in the DCF (lowering returns), or is it strategic flexibility worth holding?

7. **Capital-allocation flag** — If the firm has substantial excess cash and isn't deploying it (no buybacks, no dividends, no acquisitions), is this a value-creation issue?

Cite sources. Show calculations.
```

### What this produces

A 1–2 page working-capital section for the report. Often the most operationally insightful part of the analysis.

### How to adapt this prompt

- *For your own company:* Replace [your company].
- *For ChatGPT / Gemini:* Identical.

### Connection to previous chapters

Builds on Chapter 5 (statements), Chapter 6 (efficiency ratios), and Chapter 18 (working capital in pro forma). Adds operational depth to the financial analysis.

### Preview of next chapter

Chapter 20 — the final substantive chapter — examines risk management. The Chapter 20 LLM Exercise builds a risk register and assesses the firm's hedging program.

---

## AI Wayback Machine

**Hyman Minsky** was an economist whose Financial Instability Hypothesis explains why working-capital management matters as financial conditions tighten.

**Run this:**

```
Who is Hyman Minsky, and how does their work connect to working capital management we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about their career or ideas.
```

→ Search **"Hyman Minsky"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to apply Hyman Minsky's framework to a specific finance question.
- Add a constraint: "Answer including criticisms or limits of Hyman Minsky's framework."

What changes? What gets better? What gets worse?

---

**Tags:** working-capital, cash-conversion-cycle, trade-credit, accounts-receivable, accounts-payable, inventory-management, cash-budget
