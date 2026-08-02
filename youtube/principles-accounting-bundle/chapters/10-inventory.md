# Chapter 10 — Inventory

## 10.1 Opening: Three identical widgets, three different costs

A wholesaler buys three identical widgets across the year — January 15 at $10 each, June 12 at $12 each, October 28 at $14 each. Three units in stock at year-end, total cost $36. In November, the company sells two of the three for $25 apiece. Total revenue from the sale: $50.

Question. What was the *cost* of those two widgets?

If the company says it sold the January and June widgets, COGS is $10 + $12 = $22 and Gross Profit is $50 − $22 = $28. The remaining widget on the balance sheet, valued at $14, is the October purchase.

If the company says it sold the June and October widgets, COGS is $12 + $14 = $26 and Gross Profit is $50 − $26 = $24. The remaining widget, valued at $10, is the January purchase.

If the company says it sold widgets at average cost ($36/3 = $12 each), COGS is $24 and Gross Profit is $26. The remaining widget is on the books at $12.

The widgets are *identical*. The customer cannot tell the difference. The company cannot, in any operationally meaningful sense, identify *which* physical widget was sold. And yet the choice of cost-flow assumption changes COGS by $4, Gross Profit by $4, ending Inventory by $4, and (eventually) net income and income taxes. The choice is consequential, the difference is real, and the accounting profession has standardized on a small set of permitted methods.

This chapter is about that choice. By the end of it, you should be able to:

- Distinguish the three major *cost-flow assumptions*: FIFO (first-in, first-out), LIFO (last-in, first-out), and weighted average.
- Compute ending inventory and COGS under each method, in both periodic and perpetual systems.
- Explain why the three methods produce different results in periods of changing prices, and identify which method tends to produce higher reported income in inflationary periods.
- Apply the *lower of cost or market* (LCM) rule — actually *lower of cost or net realizable value* under current GAAP — to write down inventory whose value has dropped below cost.
- Compute and interpret *inventory turnover* and *days' sales in inventory*.
- Recognize that LIFO is permitted under U.S. GAAP but is not permitted under IFRS, and explain the implications for international comparability.

You walk in with merchandising mechanics from Chapter 6. You walk out understanding the asset that, for many businesses, is the largest item on the current-assets side of the balance sheet.

## 10.2 The three cost-flow assumptions

Let's stay with the three-widget example. The company's purchases for the year:

| Date | Units | Unit cost | Total |
|---|---|---|---|
| Jan 15 | 1 | $10 | $10 |
| Jun 12 | 1 | $12 | $12 |
| Oct 28 | 1 | $14 | $14 |
| **Total available** | **3** | | **$36** |

The company sells 2 units for $25 each in November.

### FIFO (first-in, first-out)

FIFO assumes that the *oldest* inventory is sold first. The two units sold in November are deemed to be the January and June units. COGS = $10 + $12 = $22. Ending Inventory (the one remaining unit) = the October purchase, $14.

The intuition: most physical inventory does flow this way (a grocer rotates stock, putting older items in front so they sell first). FIFO mirrors what physically tends to happen.

### LIFO (last-in, first-out)

LIFO assumes that the *newest* inventory is sold first. The two units sold in November are deemed to be the October and June units. COGS = $14 + $12 = $26. Ending Inventory = the January purchase, $10.

The intuition: in periods of rising prices, LIFO charges the most recently incurred (highest) costs against the most recently earned revenue, satisfying the matching principle in a particularly tight way. Reported COGS is higher, reported Gross Profit and net income are lower, and (consequentially) reported income taxes are lower. This last effect is the entire reason LIFO became popular in the U.S. — companies that adopted LIFO during inflationary periods of the 1970s and 1980s reduced their tax liability substantially compared to FIFO peers.

### Weighted-average cost

Weighted average assigns the *average* cost across all units available for sale. Average cost = $36 / 3 = $12 per unit. COGS for the two units sold = 2 × $12 = $24. Ending Inventory = 1 × $12 = $12.

Weighted average is the middle ground — neither the oldest nor the newest costs dominate. It smooths out the effect of price changes.

### Specific identification

A fourth method, used when each unit is genuinely distinguishable — luxury cars by VIN, jewelry by serial number, real estate. The company tracks *which* specific unit was sold and assigns its actual cost. Specific identification is precise but feasible only when units are individually identifiable; for fungible inventory it's impractical.

### Comparing the methods

Side by side, for our three-widget example:

| Method | COGS | Gross Profit (Sales $50) | Ending Inventory |
|---|---|---|---|
| FIFO | $22 | $28 | $14 |
| LIFO | $26 | $24 | $10 |
| Weighted Average | $24 | $26 | $12 |

In a period of *rising* prices, FIFO produces the highest gross profit and the highest ending inventory. LIFO produces the lowest of both. Weighted average is in between.

In a period of *falling* prices, the relationships flip — LIFO would produce higher gross profit and higher ending inventory than FIFO.

In a period of *stable* prices, the three methods converge.

The trade-offs:

FIFO buys *balance-sheet realism* (ending inventory is valued at recent costs) at the cost of *income-statement looseness in inflationary periods* (older, lower costs flow to COGS, inflating gross profit beyond what current-cost matching would suggest).

LIFO buys *income-statement matching* (current costs flow to COGS, gross profit reflects current pricing relationships) at the cost of *balance-sheet staleness* (ending inventory is valued at old costs, sometimes very old; companies that have been on LIFO for decades carry inventory at 1970s prices).

Weighted average buys *simplicity and middle-ground reporting* at the cost of *not optimally matching either side*.

## 10.3 LIFO and the U.S./IFRS divergence

A consequential international point. *LIFO is permitted under U.S. GAAP. LIFO is prohibited under IFRS.* IFRS allows only FIFO and weighted average.

This means that a U.S. company on LIFO and an otherwise-identical European company under IFRS will report different inventory values, different COGS, different gross profits, and different net incomes — for reasons that have nothing to do with their actual operations and everything to do with the accounting standard each follows. Cross-border comparisons require translation.

U.S. companies on LIFO must disclose, in the notes to their financial statements, the *LIFO reserve* — the difference between LIFO inventory value and what the inventory would have been valued at under FIFO. Sophisticated analysts adjust the reported numbers using the LIFO reserve to make companies on different methods comparable. The disclosure is mandatory because without it, two companies could look very different on the financials despite operating identically.

The IRS *LIFO conformity rule*: U.S. companies that use LIFO for tax purposes must also use LIFO for financial reporting purposes. This rule prevents companies from claiming the tax benefit of LIFO without also bearing the lower-reported-income consequence. It's why LIFO use shows up consistently across a company's books and tax filings, not selectively.

## 10.4 Periodic vs. perpetual: how the systems handle cost flow

Both periodic and perpetual systems can use any of the three methods, but the mechanics differ.

Under the *periodic* system, COGS is computed once at the end of the period using the formula *Beginning Inventory + Net Purchases − Ending Inventory = COGS*. Whichever cost-flow assumption is in use determines how Ending Inventory gets valued; COGS is then computed by subtraction.

Under the *perpetual* system, COGS is computed at the moment of every sale. The cost-flow assumption is applied transaction-by-transaction. FIFO under perpetual: at every sale, the oldest layers of inventory still on hand are pulled. LIFO under perpetual: the newest layers at the moment of sale are pulled. Weighted average under perpetual is sometimes called *moving average* — the average cost is recomputed every time new purchases arrive.

A subtle but real consequence: LIFO under periodic and LIFO under perpetual can produce different COGS and ending-inventory figures for the same set of transactions, because periodic LIFO pulls from the *latest layers as of period-end*, while perpetual LIFO pulls from the *latest layers as of each sale date*. FIFO produces identical results under either system because the oldest layers are oldest regardless of when you check. Weighted average under perpetual ("moving average") differs from weighted average under periodic. The choice of system matters for LIFO and weighted-average reporting in ways it doesn't for FIFO.

## 10.5 Lower of cost or net realizable value

Inventory is recorded at cost (under whichever cost-flow method the company uses), but if its market value falls below cost, GAAP requires a write-down. The principle of *conservatism* (Chapter 3) is in play: don't carry inventory at more than it can realistically be sold for.

Under U.S. GAAP for companies using FIFO or weighted average, the rule is *lower of cost or net realizable value* (LCNRV). *Net realizable value* is the estimated selling price minus reasonable costs of completion and disposal. If recorded cost is $50 per unit and NRV is $42, the inventory is written down to $42:

| Account | Debit | Credit |
|---|---|---|
| Loss on Inventory Writedown (or COGS) | $8 per unit | |
| Inventory | | $8 per unit |

For companies using LIFO, the older *lower of cost or market* (LCM) rule still applies, with "market" defined within bounds (replacement cost, capped at net realizable value, floored at NRV minus normal profit margin). The difference is technical and rarely matters for typical situations.

The trade-off: write-downs buy *balance-sheet realism* (inventory carried at no more than what it can fetch) at the cost of *immediate income-statement hits* in the period of write-down. Companies do not write up inventory if its market value rises (with the limited exception of recovering prior write-downs in some IFRS contexts) — the conservatism is asymmetric.

Write-downs are most common for inventory affected by obsolescence (last year's electronics), seasonal expiration (holiday merchandise after the holiday), damage in storage, or oversupply that depresses market price. A company that consistently has to take inventory write-downs is signaling either weak inventory management, weak demand forecasting, or both.

## 10.6 Inventory ratios

Two ratios standardize the analysis of inventory efficiency.

*Inventory turnover*: Cost of Goods Sold / Average Inventory. Measures how many times during the period the inventory was "turned over" — sold and replenished. Higher is generally better, signaling the inventory isn't sitting idle.

*Days' sales in inventory*: 365 / Inventory Turnover. Same information in days.

Industry norms vary by orders of magnitude. Fresh-food grocers run inventory turnover above 20 (days' sales in inventory below 18). General-merchandise retailers run 6-10 (days' sales 36-60). Heavy-equipment distributors might run 2-4 (90-180 days). Within an industry, trends matter as much as levels — turnover declining over time signals slowing sales, overordering, or pricing problems.

## 10.7 Exercises

### Warm-up

1. **Define FIFO, LIFO, and weighted average** in one sentence each. Identify which method each assumes for which units flow first.

2. **In a period of rising prices, which method produces the highest gross profit?** Which produces the lowest?

3. **State the formula for inventory turnover and explain what a higher number suggests.**

### Application

4. **A company has the following inventory activity for May:** May 1 beginning inventory 100 units at $5 = $500; May 12 purchase 200 units at $6 = $1,200; May 25 purchase 100 units at $7 = $700. May 28 sale of 250 units at $12 each. Compute COGS and ending inventory under (a) FIFO periodic, (b) LIFO periodic, (c) weighted average periodic.

5. **A retailer has 1,000 units in inventory recorded at $20 each. Year-end NRV is $17 per unit.** Journalize the LCNRV write-down.

6. **A company reports COGS of $1,800,000 and average inventory of $300,000.** Compute inventory turnover and days' sales in inventory.

### Synthesis

7. **A company on LIFO has carried a portion of its inventory at 1985 unit costs for nearly forty years.** Explain how this can happen and what the LIFO reserve disclosure tells a reader about the company's inventory if it were instead reported under FIFO.

8. **U.S. GAAP permits LIFO; IFRS does not.** Explain how an analyst would adjust a U.S. LIFO company's reported inventory to make it comparable with an IFRS competitor, using only the LIFO reserve disclosure.

### Challenge

9. **In a period of falling prices, which cost-flow method produces the highest reported income?** Walk through the logic; do not just state the answer.

10. **A retailer's inventory turnover is dropping each year — 8.5, 7.2, 5.8.** Propose at least three plausible operational explanations. What would you need from the company's other financial statements (and from operations) to distinguish among them?

## 10.8 Chapter summary

You walked into this chapter knowing that merchandisers carry inventory. You walk out knowing how the cost of that inventory gets allocated between the balance sheet and the income statement.

Three cost-flow methods are permitted under U.S. GAAP — FIFO, LIFO, weighted average — plus specific identification when units are individually distinguishable. The choice changes COGS, Gross Profit, ending inventory, and net income whenever prices are not stable. In rising-price periods, FIFO maximizes reported income and ending inventory; LIFO minimizes both. The IRS LIFO conformity rule forces companies that use LIFO for tax to also use LIFO for reporting. IFRS prohibits LIFO entirely.

The lower-of-cost-or-net-realizable-value rule (and the older LCM rule for LIFO inventories) writes down inventory when its market value falls below cost — never up if it rises. Conservatism is asymmetric.

Inventory turnover and days' sales in inventory are the standard efficiency ratios. They vary widely by industry; trends matter as much as levels.

The single most important idea: identical physical inventory can be reported at different values on the balance sheet, with different COGS on the income statement, depending on the cost-flow assumption the company uses. The choice is real and consequential, even though the goods themselves are indistinguishable.

The common mistake to watch for: treating cost-flow assumptions as if they describe physical movement of goods. They don't. Most physical goods do flow FIFO regardless of accounting method (older stock sells first to avoid spoilage and obsolescence). The accounting choice is purely about *which costs* are matched to *which revenues*, independent of which physical units left the building.

## 10.9 A note on inventory errors

Inventory errors propagate. An understatement of ending inventory in Year 1 produces an overstatement of COGS in Year 1, which understates net income in Year 1. The same understated ending inventory becomes Year 2's beginning inventory; this understates Year 2's COGS, which overstates Year 2's net income. The effect reverses out over two years. But the two years' financial statements are wrong individually until corrected.

The implication for controllers: a periodic physical inventory count must be taken seriously. Errors propagate; they don't go away on their own.

## 10.10 Inventory cost: what's in, what's out

Before any cost-flow assumption can be applied, the company has to determine the *cost* of each unit of inventory. This is less straightforward than it sounds for a manufacturer, and a significant source of error and judgment.

For a *retailer or wholesaler*, inventory cost includes the invoice price of the goods, less any cash or trade discounts taken, plus freight in (under FOB shipping point), plus any costs of getting the goods ready for sale (handling, repackaging, import duties, sales tax that the retailer cannot recover). Storage cost in the merchant's own warehouse, advertising, and post-acquisition holding costs are *not* inventory costs — they are operating expenses charged to the period in which incurred.

For a *manufacturer*, inventory cost includes three categories of cost: *direct materials* (raw materials traceable to specific units), *direct labor* (factory wages traceable to specific units), and *manufacturing overhead* (indirect factory costs — utilities for the plant, depreciation of factory equipment, supervisor salaries, factory supplies, factory insurance). All three flow into Work-in-Process Inventory and then into Finished Goods Inventory and finally to Cost of Goods Sold when the units are sold. *Selling expenses* (sales commissions, marketing, distribution to customers) and *administrative expenses* (corporate overhead, accounting, executive salaries) are *not* inventory costs — they are period expenses.

The distinction matters because a misclassification of overhead — treating administrative cost as overhead, or factory overhead as administrative — shifts the cost between inventory (which is on the balance sheet until the units sell) and immediate expense (which is on the income statement now). In effect, classification can move a cost between this period and a later period. The classification rules (in U.S. GAAP, codified primarily in ASC 330) are not flexible — they exist because their flexibility would be too easy to abuse for earnings management.

A manufacturer's *Cost of Goods Manufactured* statement (sometimes called a *Schedule of Cost of Goods Manufactured*) is the period-end report that pulls together direct materials used, direct labor incurred, and manufacturing overhead applied, plus the change in Work-in-Process Inventory, to produce the cost of finished goods completed during the period. That figure feeds into Finished Goods Inventory and ultimately into COGS. We won't develop the full mechanics here — that's the subject of cost-accounting and managerial-accounting courses — but understanding that inventory cost for a manufacturer is a constructed number, built from many sub-components, is worth carrying forward.

## 10.11 Estimation methods when a count isn't possible

Sometimes a physical inventory count is impossible or prohibitively expensive — a fire that destroys the warehouse, a flood that contaminates everything, a need to estimate inventory between physical-count dates for interim financial reports. Two estimation methods are standard.

The *gross profit method* uses the company's historical gross profit margin to estimate cost of goods sold from sales, then estimate ending inventory by subtraction:

1. Beginning inventory + purchases = goods available for sale (known from the books)
2. Net sales × (1 − historical gross profit margin) = estimated COGS
3. Goods available − estimated COGS = estimated ending inventory

For a company with $400,000 of goods available, $500,000 of sales, and a historical gross profit margin of 30%: estimated COGS = $500,000 × 70% = $350,000; estimated ending inventory = $400,000 − $350,000 = $50,000.

The accuracy of the gross profit method depends entirely on the historical margin still being representative. A retailer that has been steadily losing pricing power, or that has shifted its product mix, will have a historical margin that no longer applies — and the estimated inventory will be off.

The *retail inventory method* is used by department stores and retailers who track inventory at retail price as well as at cost. By computing a cost-to-retail ratio for the period, the company can convert ending inventory at retail (which can be calculated from the books) back to ending inventory at cost without a physical count. The mechanics are more involved than space allows here, but the principle is the same: leverage a known relationship to estimate what would otherwise require a count.

Both methods are approximations and are used either for interim reporting or for insurance claims after destruction events. Annual financial statements still require a physical count under most GAAP rules.

## 10.12 Inventory and the cost of holding too much

Carrying inventory has costs that don't appear on the income statement until something goes wrong. A unit that sits in the warehouse for six months ties up cash that could have been deployed elsewhere, occupies storage space that has rent, requires insurance, risks obsolescence, and, in some industries, risks physical deterioration. The *carrying cost of inventory* is the sum of all of these — typically estimated at 20-30% of inventory value per year for most industries, though it can be much higher for fast-moving consumer electronics where obsolescence is real on a quarterly time scale.

Just-in-time (JIT) inventory practices, pioneered by Toyota and now standard across many manufacturing industries, attempt to minimize this carrying cost by holding the smallest possible inventory consistent with operational continuity — ordering parts to arrive just before they're needed, holding finished goods for the shortest possible time before customer shipment. JIT works when supply chains are reliable and demand is predictable; it breaks when either of those assumptions fails (as the COVID-era supply-chain disruptions made vivid for industries that had run lean for decades).

The accounting consequence: a company that successfully implements JIT will see inventory turnover rise dramatically and days' sales in inventory drop. The balance sheet will show smaller inventory; the income statement will see lower operating expenses related to warehousing and obsolescence write-downs. The risk side — that a single supplier disruption can halt production entirely — does not show up in the financial statements at all until it materializes. This is one of the structural reasons why financial statements alone are an incomplete picture of operational health: the resilience trade-offs that JIT involves are management choices the financials report on only after the fact.

## 10.13 Connections forward

Chapter 11 turns to *long-term assets* — equipment, buildings, vehicles, intangibles — that are used over multiple periods rather than sold. You'll see the depreciation, amortization, and impairment mechanics that allocate their cost across the periods they benefit, and how disposal entries handle assets at the end of their useful lives.
---

## LLM Exercise — Chapter 10: Inventory (AI Bookkeeping Tool Project)

**Project:** AI Bookkeeping Tool.
**What you're building this chapter:** the inventory cost-flow module — FIFO, LIFO, weighted average implemented in both perpetual and periodic systems, plus LCNRV (lower of cost or net realizable value) and inventory ratios.
**Tool:** **Claude Code.**

---

**The Prompt:**

```
I'm in Chapter 10 of building my AI Bookkeeping Tool. The Ch 6
merchandising module handled simple inventory; this chapter
generalizes it. This chapter taught: the three cost-flow
assumptions:
   - FIFO (first-in-first-out): COGS uses oldest inventory; ending
     inventory uses most recent costs.
   - LIFO (last-in-first-out): COGS uses most recent inventory;
     ending inventory uses oldest costs. (LIFO prohibited under
     IFRS; US allows.)
   - Weighted average: COGS and ending inventory both at the
     weighted-average cost.
How perpetual vs. periodic systems treat each method (perpetual
applies the method at each sale; periodic applies it at period-end);
lower of cost or net realizable value (LCNRV — inventory write-down
when NRV < cost); inventory ratios (inventory turnover = COGS ÷
average inventory; days sales in inventory = 365 ÷ turnover).

Extend the tool. Produce four outputs.

1. **The cost-flow module.** A configurable inventory layer that
   supports FIFO, LIFO, and weighted average. For each method,
   functions for:
   - Recording a purchase (adds a layer with cost and quantity).
   - Recording a sale (computes COGS based on the method).
   - Reporting current inventory value at any date.
   The tool should let the user choose the method at setup; the
   method applies consistently across all reports.

2. **Perpetual vs. periodic mode.** The cost-flow application
   differs:
   - Perpetual: COGS computed at each sale.
   - Periodic: COGS computed at period-end using a single
     calculation (beginning inventory + purchases - ending
     inventory).
   Both modes should produce the same period-end COGS and ending
   inventory for FIFO; LIFO and weighted average may differ
   between modes (which is itself a useful demonstration).

3. **LCNRV check.** A function that:
   - Compares each inventory item's cost to its NRV (selling
     price - costs to complete and sell).
   - Computes the write-down for items where NRV < cost.
   - Generates the adjusting entry (debit Loss on Inventory
     Write-down, credit Inventory).

4. **Tests with concrete cost layers.** A scenario with:
   - 5 inventory purchases at varying costs.
   - 4 sales at varying quantities.
   - Compute COGS and ending inventory under FIFO, LIFO, weighted
     average — both perpetual and periodic.
   - Verify the inventory-turnover and DSI calculations against
     the computed inventory values.

Update spec.
```

---

**What this produces:** A complete cost-flow inventory module that handles the three standard methods in both perpetual and periodic. The cross-method comparison is itself useful — students see why the same operations produce different net income under different cost flows.

**How to adapt this prompt:**

- *For your own project:* If your business uses serialized inventory (cars, art, custom equipment), specific-identification is the only sensible method and FIFO/LIFO/weighted-average aren't applicable. The tool should support all three plus specific-ID.
- *For ChatGPT / Gemini:* Works as written.
- *For Claude Code:* The right tool. The LIFO implementation is the most error-prone; rigorous tests with known correct answers help.
- *For a Claude Project:* Update spec.

**Connection to previous chapters:** Ch 6's simple inventory engine generalizes here. The Ch 6 tests should still pass under FIFO (the default in Ch 6).

**Preview of next chapter:** Chapter 11 adds long-term assets — capitalization rules, three depreciation methods (straight-line, units-of-production, double-declining-balance), asset disposal, intangibles, impairment. The tool's PP&E module.


---

## AI Wayback Machine

**Joseph Wharton** was founded the Wharton School in 1881 — the first collegiate business school in the world, formalizing inventory and operational accounting.

**Run this:**

```
Who is Joseph Wharton, and how does their work connect to inventory we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about their career or ideas.
```

→ Search **"Joseph Wharton"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to apply Joseph Wharton's ideas to a specific accounting question.
- Add a constraint: "Answer including criticisms or limits of Joseph Wharton's framework."

What changes? What gets better? What gets worse?
