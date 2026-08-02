# Chapter 19 — Trade Credit and Working Capital in Planning

**Suggested titles**
1. The Cash Conversion Cycle
2. Working Capital and How Amazon Gets Paid First
3. The Day-to-Day Money Machine

**TL;DR.** Working capital is the day-to-day cash and short-term obligations a firm uses to fund operations. The **cash conversion cycle** — days inventory + days receivables − days payables — measures how long the firm's cash is tied up before customer payments come back. Shortening this cycle frees cash for higher-return uses; in extreme cases (Amazon, Costco), firms achieve a *negative* cycle, getting paid by customers before they pay suppliers.

---

## The puzzle of negative working capital

Amazon, in many years, has had **negative working capital**.

Read that again. Working capital is current assets minus current liabilities — the cash and short-term resources a firm needs to operate. Most firms have positive working capital because they need cash on hand, inventory in stock, and customers' unpaid bills (receivables) to fund the gap until those bills get paid.

Amazon often has the opposite. It collects payment from customers immediately (credit cards settle in 24-72 hours; some Prime customers prepay). It turns inventory in days, not months, because of relentless logistics. And it pays suppliers on long terms — often 60-90 days. The result: Amazon is, in effect, *being financed by its suppliers*. Each new dollar of sales generates more cash today than next month's payments require.

This isn't a quirk; it's a deliberate strategic choice. Negative working capital means the firm needs *less* equity and debt capital to grow. Every dollar of additional sales doesn't require a dollar of additional working capital — it generates working capital. For a firm growing 30% per year, this is the difference between needing massive outside financing and self-funding the growth.

Most firms aren't Amazon. They have positive working capital and they need to manage it carefully. The cash conversion cycle, the management of receivables, the management of inventory, and the management of trade credit are the core disciplines. They are also the main reason chapter 18's pro forma cash flows differ from net income.

For your equity research project, this chapter explains *why* your chosen company's free cash flow may differ from its earnings, and *what management is doing about it*. The 10-K's working capital footnotes and the cash flow statement's "changes in working capital" line tell you a lot about operational efficiency.

---

## Learning objectives

After working through this chapter, you should be able to:

- Define and compute the cash conversion cycle, days sales outstanding, days inventory, and days payable.
- Calculate the implicit annual cost of forgoing a trade-credit discount (e.g., 2/10 net 30).
- Identify how a firm can shorten its cash conversion cycle.
- Distinguish among the four motives for cash holdings (transactional, precautionary, speculative, compensating).
- Build a simple rolling cash budget identifying months with surplus or deficit.
- Compare working capital approaches across industries and explain the variation.

**Prerequisites.** Chapter 5 (financial statements), Chapter 6 (ratios), Chapter 18 (forecasting).

---

## Concept 1 — The cash conversion cycle

A firm's daily operations involve a sequence: spend cash on inventory and labor → produce or stock → sell → wait for collection → cash arrives back. The **cash conversion cycle (CCC)** measures how long that sequence takes.

### The formula

$$\text{CCC} = \text{Days Inventory} + \text{Days Sales Outstanding} - \text{Days Payable}$$

Each component has a precise definition:

**Days Inventory** = $\frac{\text{Average Inventory}}{\text{COGS}} \times 365$. The number of days a unit of inventory sits before it's sold.

**Days Sales Outstanding (DSO)** = $\frac{\text{Average Accounts Receivable}}{\text{Credit Sales}} \times 365$. The number of days from sale to cash collection.

**Days Payable Outstanding (DPO)** = $\frac{\text{Average Accounts Payable}}{\text{COGS}} \times 365$. The number of days from purchase to supplier payment.

### Worked example — King Sized Products

A firm with annual COGS $30M, credit sales $40M, average inventory $3M, average AR $6M, average AP $2.8M:

- Days Inventory = $\frac{3}{30} \times 365 = 36.5$ days
- DSO = $\frac{6}{40} \times 365 = 54.75$ days
- DPO = $\frac{2.8}{30} \times 365 = 34.07$ days
- **CCC = 36.5 + 54.75 − 34.07 = 57.18 days**

The firm's cash is tied up for about 57 days from when it pays suppliers to when it collects from customers. Every dollar of sales requires 57 days of working capital financing.

### What management can do

Three levers:

1. **Reduce inventory days.** Just-in-time logistics, better forecasting, shorter SKU counts. Trade-off: higher stockout risk.

2. **Reduce DSO.** Tighter credit policy (don't extend credit to risky customers), early-payment discounts (e.g., 2/10 net 30 — see Concept 2), better collections processes. Trade-off: lost sales to customers who needed longer payment terms.

3. **Increase DPO.** Negotiate longer payment terms with suppliers. Trade-off: damaged supplier relationships if pushed too far; potential price increases as suppliers compensate.

If King Sized improves to inventory $2.8M, AR $5.5M, AP $3.3M (same sales/COGS):
- Days Inventory = 34.07
- DSO = 50.21
- DPO = 40.15
- CCC = 44.13 days — about 13 days improvement.

Each day shortened frees roughly (annual COGS / 365) of working capital. For King Sized, that's $30M / 365 ≈ $82K per day. Thirteen days = $1.07M of cash freed.

### Industry variation

Cash conversion cycles vary enormously by industry:

- **Software/SaaS**: often near zero or negative (services prepaid; minimal inventory).
- **Restaurants**: typically negative (customers pay immediately; suppliers paid in 30 days).
- **Big-box retail (Walmart, Costco)**: roughly zero or slightly negative through aggressive supplier terms.
- **General retail**: 30-90 days.
- **Manufacturing**: 60-150 days, depending on production cycle.
- **Construction**: 200+ days (long projects, slow billing cycles).
- **Heavy equipment leasing**: 300+ days.

Compare your chosen company's CCC to its industry peers. A firm with much longer CCC than peers is using more capital to fund the same operations — a clear inefficiency. A firm with much shorter CCC than peers is potentially exposing itself to operational fragility (or running an operationally elite organization).

↳ **Dig Deeper — Just-in-time and the 2020-2022 supply chain stress test**

*Just-in-time inventory management was the operating doctrine that won the 2010s. Then COVID-19, the Suez Canal blockage, the Russia-Ukraine war, and chip shortages all stress-tested the doctrine. Many firms with the leanest inventories suffered most. The result: a partial revival of "just-in-case" inventory thinking.*

**Prompt:**
> Explain the just-in-time inventory framework as it dominated 2000-2020 corporate operations. Then walk through three specific 2020-2022 supply chain disruptions (COVID auto-industry chip shortage, Suez Canal blockage of March 2021, Ukraine war commodity disruption) and how they affected firms with different inventory strategies. Has corporate inventory management structurally shifted? Cite specific firm examples of strategy changes.

**What to do with the output:** Save it. When evaluating your project company's working capital, consider whether its CCC reflects 2010s-style optimization that may be miscalibrated for the current era.

### The trade-off (concept 1)

Cash conversion trades **operational efficiency against operational resilience**. Short cycles free capital but require aggressive inventory and credit management. The 2020-2022 supply chain disruptions punished firms with the leanest inventories — the just-in-time models that won in the 2010s exposed vulnerability when global logistics broke. The optimal CCC is industry-specific and depends on the firm's tolerance for stockout and disruption risk.

### Common misconceptions

- *"Negative working capital is always good."* Not always. It can also indicate the firm is squeezing suppliers in ways that backfire (suppliers raise prices or refuse to deliver). Sustainable negative working capital requires strong supplier relationships.
- *"All firms should target the same CCC."* No — the right CCC depends on the industry's structure and the firm's competitive advantages.

---

## Concept 2 — Trade credit: the most important "loan" most firms have

Most firms' largest source of short-term financing is *not* a bank loan. It's accounts payable — the money they owe suppliers but haven't paid yet. Trade credit is **spontaneous financing**: it grows automatically with sales, no paperwork, no interest.

### How trade credit works

When a supplier ships goods on net-30 terms, they're effectively lending the buyer the cost of the goods for 30 days. The buyer benefits from 30 days of free financing.

Many suppliers offer early-payment discounts. The standard format: **2/10 net 30** — pay within 10 days for a 2% discount, or pay the full amount within 30 days.

### The hidden cost of forgoing the discount

If you don't take the discount, you're effectively borrowing for 20 extra days at a 2% premium. What's the implicit annual cost?

$$\text{Implicit APR} = \frac{360}{\text{Net days} - \text{Discount days}} \times \frac{\text{Discount \%}}{100\% - \text{Discount \%}}$$

For 2/10 net 30:

$$\text{APR} = \frac{360}{30 - 10} \times \frac{2}{98} = 18 \times 0.0204 = 0.3673 = 36.73\%$$

**The implicit cost of forgoing a 2/10 net 30 discount is 36.73% annual.** Almost no other source of financing is more expensive. If the firm has access to bank credit at, say, 8%, it should always borrow from the bank to take the discount.

### When to take vs. forgo

The decision depends on alternative financing costs:

- **Always take if** you have cash or access to credit below ~37% APR (which is virtually all bank financing).
- **Maybe take if** your alternative is credit cards or payday-style lending.
- **Skip if** taking the discount would cause cash crunch and you have no alternative.

For a healthy firm, the answer is essentially always "take the discount." For a distressed firm, the discount may be unaffordable; suppliers can become the de facto lender of last resort, often at very high implicit cost.

### Worked example — Jackson's Premium Jams

A small grocery wholesaler buys $10,500 of inventory on 2/10 net 30 terms.

- Pay in 10 days: $10,500 × 0.98 = $10,290 (saves $210)
- Pay in 30 days: $10,500

The $210 saved by early payment, on $10,290 borrowed for 20 extra days, is the basis of the 36.73% APR. If the firm has any cash or affordable credit, taking the discount is clearly the right move.

### International variation: letters of credit

For international trade, where supplier-buyer trust may be limited, **letters of credit** replace traditional trade credit. A bank guarantees payment to the exporter once the exporter ships and provides the documentation. This adds cost but reduces counterparty risk for cross-border deals.

↳ **Dig Deeper — Supply chain finance and reverse factoring**

*Beyond traditional trade credit, large buyers can offer their suppliers a sweeter deal: pay the supplier early through a third-party financier, while the buyer pays the financier on its own (longer) terms. This is "supply chain finance" or "reverse factoring." It's a $1.5T+ market that has caused some spectacular failures (Greensill 2021).*

**Prompt:**
> Explain how reverse factoring (supply chain finance) works mechanically. Why does it appeal to buyers (extends payables without supplier-relationship damage) and to suppliers (faster cash)? Then summarize the Greensill Capital collapse of March 2021: what made the firm's model fragile, and why does the case study suggest that supply chain finance can hide leverage rather than reduce it?

**What to do with the output:** Save it. Some of your project company's "trade payables" may include reverse factoring; understanding the structure matters for assessing the firm's true short-term liquidity position.

### The trade-off (concept 2)

Trade credit trades **the cost of the discount against the convenience of delayed payment**. For firms with abundant cash or credit, taking the discount is almost free money. For distressed firms, the discount becomes unaffordable, but the implicit borrowing cost can be devastating.

### Common misconceptions

- *"Trade credit is free."* It's free if you pay within terms. It's expensive if you forgo discounts or if late payment damages your credit rating.
- *"Suppliers don't care if I pay on day 30 vs. day 10."* Some don't; some track payment timing carefully and adjust pricing or credit limits accordingly.

---

## Concept 3 — Cash management and the rolling budget

Working capital management ultimately produces a single output: the firm's cash position over time. Managing that output is the job of the **cash budget**.

### Why firms hold cash

Four motives, each with its own logic:

1. **Transactional** — pay bills, payroll, regular suppliers. The day-to-day operating need.
2. **Precautionary** — unexpected repairs, equipment failures, demand spikes. Insurance against the unknown.
3. **Speculative** — sudden opportunities (acquisitions, distressed asset purchases, strategic buys at low prices). Capacity for opportunistic action.
4. **Compensating** — minimum balances required by lender agreements (a $50K balance might be required against a $500K line of credit).

A firm with too little cash misses opportunities and can't survive shocks. A firm with too much cash is wasting capital that should be deployed in operations or returned to shareholders.

The right level depends on the firm's volatility, growth, and access to alternative liquidity (lines of credit, credit cards, factoring receivables).

### Where excess cash goes

Sitting on cash earns near-zero. Firms with excess cash typically invest in **cash equivalents**:

- **US Treasury bills** — 3-month or 6-month maturities, default-risk free, exempt from state and local tax.
- **Federal agency securities** (Fannie Mae, Freddie Mac) — slightly higher yields, near-Treasury credit quality.
- **Bank CDs** — higher yields than savings accounts, slight illiquidity.
- **Commercial paper** — large corporates lending to each other; 30-270 day terms.
- **Money market mutual funds** — pool of the above; suitable for smaller firms.

For a multinational like Apple with $191B in cash, the entire cash equivalents portfolio is invested across these instruments to maximize yield while preserving liquidity.

### The rolling cash budget

A **cash budget** is a forward-looking forecast of cash inflows and outflows, typically by month for a year ahead. **Rolling** means it's continuously updated — when one month's actuals come in, that month drops off the front, and a new month is added at the back. The horizon stays at 12 months ahead.

The components:

- **Cash collections** — receipts from sales (lagged by collection period), interest on cash holdings, dividends from investments.
- **Cash disbursements** — supplier payments (lagged by payable period), salaries (paid roughly when accrued), rent, utilities, taxes, debt service, dividends.
- **Net cash flow** = Collections − Disbursements.
- **Cumulative cash position** at month-end.

If the cumulative position drops below the firm's minimum cash policy in any month, the firm needs short-term financing. If the position is consistently above policy, the firm has surplus to invest.

### Sources of short-term financing

When the cash budget identifies a deficit, options include:

- **Revolving line of credit** — pre-arranged with a bank; firm draws as needed. Interest rate typically prime + small spread. The standard tool for working-capital fluctuations.
- **Commercial paper** — for large public firms only; cheaper than bank credit, but only available to highly-rated issuers.
- **Factoring** — selling receivables to a finance company at a discount. Expensive but immediate; useful for firms that can't access bank credit.
- **Trade credit extension** — pushing payables to suppliers. Limited but free if used carefully.
- **Asset-based lending** — borrowing against inventory or receivables as collateral. Common in distressed situations.

For your equity research project, the firm's revolving credit facility (described in the 10-K's debt footnote) tells you how much liquidity it has access to in stress. A firm with $5B revolving credit and no covenant risk has substantially more flexibility than one with $500M revolving credit and tight covenants.

### Worked example — building a simple cash budget

A firm with monthly sales of $100K average (varying ±20% by season), 50% gross margin, 30-day collections, 30-day payables, fixed expenses of $20K/month, and a $10K minimum cash policy.

Forecasted cash position:

| Month | Sales | Collections (lagged) | Disbursements | Net flow | Position |
|---|---|---|---|---|---|
| Jan | 80K | 100K (Dec) | 70K | +30K | 30K |
| Feb | 100K | 80K | 70K | +10K | 40K |
| Mar | 130K | 100K | 95K | +5K | 45K |
| Apr | 100K | 130K | 70K | +60K | 105K |
| May | 80K | 100K | 60K | +40K | 145K |

The firm has plenty of cash. The variation in monthly position should make a few things clear: the seasonal peak in March requires a big payable to suppliers in April (paid lagged); the spring buildup of cash gets invested or returned to shareholders.

If the firm's minimum cash policy is $10K, every month is comfortably above. If it's $30K, January is tight (right at it), and the firm should arrange a small line of credit just in case.

### The trade-off (concept 3)

Cash management trades **safety against opportunity cost**. Holding cash is safe; cash earns near-zero. Holding minimum cash and operating with tight liquidity is risky; the alternative uses (capex, dividends, M&A) deploy capital more productively. The right level depends on the firm's volatility and access to alternative liquidity.

### Common misconceptions

- *"More cash is always safer."* Up to a point. Beyond, idle cash is a drag on returns and may signal management isn't deploying capital well.
- *"Lines of credit are free until you draw."* They have unused-fee components; banks charge for the option of access even if you don't use it. The cost is small but real.

---

## Synthesis — working capital as ongoing operations

The chapter built three concepts:

1. **Cash conversion cycle** measures how efficiently the firm converts operations into cash. Shorter is better, with caveats about supply-chain resilience.
2. **Trade credit** is the most important short-term financing source for most firms. The implicit cost of forgoing discounts is far higher than typical bank credit.
3. **Cash budgeting** integrates working capital management into a forward view, identifying surplus and deficit periods and the financing needed to bridge them.

For the equity research project, this chapter provides the lens for assessing your chosen company's operational efficiency. Compare its CCC to peers. Check its cash holdings: too high, and management is hoarding capital that should be deployed; too low, and the firm is fragile to stress. Read its 10-K's working capital discussion in the MD&A.

The next and final chapter — Chapter 20 — addresses risk management. Working capital management is one form of risk management (specifically, liquidity risk). Chapter 20 generalizes to all risks the firm faces.

---

## Exercises

### Warm-up

**19.1** Define cash conversion cycle. State its formula. What does negative CCC mean?

**19.2** Compute the implicit APR for forgoing a 1/15 net 60 discount.

**19.3** Why might a firm hold cash even though it earns near-zero return?

### Application

**19.4** A firm has annual credit sales of $80M, COGS of $50M, average inventory of $5M, average accounts receivable of $12M, and average accounts payable of $4M. Compute:

(a) Days inventory.
(b) DSO.
(c) DPO.
(d) Cash conversion cycle.

**19.5** The firm in 19.4 wants to free $5M of working capital by improving CCC. By how many days does CCC need to shorten? Suggest two specific operational changes that could achieve this.

**19.6** For your chosen company, compute days inventory, DSO, DPO, and CCC for the most recent fiscal year. Compare to two peer companies. Which is most efficient?

### Synthesis

**19.7** Amazon often has a negative cash conversion cycle. Walmart's is roughly zero. Construct an analytical comparison: which firm is doing better in working capital management? What dimensions besides CCC matter for the comparison?

**19.8** A firm is experiencing rapid sales growth (40% per year). Construct an argument that this firm is at risk of cash crunch despite the growth. What working-capital strategies should it pursue, and how does it interact with its capital structure choices?

### Challenge

**19.9** Build a 12-month rolling cash budget for a hypothetical firm:
- Monthly sales: $200K-$400K range with seasonality.
- 30-day collections; 45-day payables.
- COGS 60% of sales; fixed expenses $50K/month; quarterly tax payments.
- Beginning cash $100K; minimum cash policy $80K.

Identify any month where additional financing is needed. Quantify it.

**19.10** Compute the dollar value of working capital tied up in your chosen company's CCC. (Hint: divide the annual COGS by 365 to get daily working capital, then multiply by CCC days.) Estimate how much would be freed by reducing CCC by 10 days. Compare to the firm's WACC and argue whether this is worth pursuing.

---

## Chapter summary

- **Cash conversion cycle (CCC)** = Days Inventory + DSO − DPO. Shorter is generally better.
- **Negative CCC** is achievable for firms with prepaid customers, fast inventory, and long payable terms (Amazon, Costco).
- **Trade credit terms** like 2/10 net 30 carry implicit annualized costs of 30%+ if discounts are forgone. Almost always take the discount if you can.
- **Cash holdings** serve four motives: transactional, precautionary, speculative, compensating.
- **Excess cash** goes into cash equivalents — Treasury bills, agency securities, CDs, commercial paper, money market funds.
- **Rolling cash budget** identifies surplus and deficit months and the financing needed.
- Industry variation in CCC is large; benchmarks should be peer-relative.

---

## What would change my mind

The chapter argues that the cash conversion cycle is the right master metric for working capital management, and that its three components are the operational levers to pull. The reading would have to revise if (a) supply-chain disruption made elite-low CCC firms systematically underperform robust-but-slow firms — there's some evidence post-2020, but the dominant strategy (low CCC) remains optimal in stable conditions, or (b) the role of trade credit fundamentally changed (e.g., real-time payments eliminating payment lags) — this is happening slowly but hasn't yet displaced the framework.

## Still puzzling

The genuinely hard question is *how lean working capital should be*. Negative CCC is theoretically optimal but requires aggressive supplier squeeze that may backfire (suppliers raise prices, refuse to deliver, or fail outright in stress). The 2020-2022 supply chain crisis was, in part, the bill coming due for years of just-in-time optimization that left no slack for shocks. The optimal CCC depends on a stress-tolerance the firm can't fully observe in normal times. Honest practitioners run scenarios; smart practitioners build redundancy into supplier relationships even when the immediate cost looks unjustified.

---

## Connections forward

- **Chapter 20** addresses risk management generally — including the supply-chain and liquidity risks this chapter touches on.

---

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

A 1-2 page working-capital section for the report. Often the most operationally insightful part of the analysis.

### How to adapt this prompt

- *For your own company:* Replace [your company].
- *For ChatGPT / Gemini:* Identical.

### Connection to previous chapters

Builds on Chapter 5 (statements), Chapter 6 (efficiency ratios), and Chapter 18 (working capital in pro forma). Adds operational depth to the financial analysis.

### Preview of next chapter

Chapter 20 — the final substantive chapter — examines risk management. The Chapter 20 LLM Exercise builds a risk register and assesses the firm's hedging program.

---

**Tags:** working-capital, cash-conversion-cycle, trade-credit, accounts-receivable, accounts-payable, inventory-management, cash-budget


---

## AI Wayback Machine

**Hyman Minsky** was economist whose Financial Instability Hypothesis explains why working-capital management matters as financial conditions tighten.

**Run this:**

```
Who is Hyman Minsky, and how does their work connect to working capital management we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about their career or ideas.
```

→ Search **"Hyman Minsky"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to apply Hyman Minsky's framework to a specific finance question.
- Add a constraint: "Answer including criticisms or limits of Hyman Minsky's framework."

What changes? What gets better? What gets worse?
