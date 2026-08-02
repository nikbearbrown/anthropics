# Chapter 6 — Merchandising Transactions

## 6.1 Opening: The brothers and the inventory

Jason and James own a small business called J&J Games, specializing in the sale of video games and accessories. They buy their merchandise from a manufacturer called Marcus Electronics and sell directly to consumers. When J&J orders from Marcus, the two parties sign a contract detailing the purchase price, the payment terms (often "net 30" — pay within 30 days), the possibility of a discount for early payment ("2/10, net 30" — 2% off if paid within 10 days), and who bears the cost and risk of shipping the merchandise from Marcus's warehouse to J&J's stockroom.

Every line in that contract becomes a journal entry. Some are easy — record the purchase, record the cost. Others are subtler — when goods arrive damaged and Marcus issues a credit, when J&J takes the early-payment discount, when the freight charge depends on whether the goods were sold *FOB shipping point* or *FOB destination*. Service businesses like Mark Summers's dry cleaner have none of these complications because they don't carry inventory. A merchandiser's books are denser than a service provider's by exactly the volume of these inventory-related transactions.

This chapter is about that density. Merchandisers — wholesalers and retailers — make up the largest share of U.S. businesses by transaction volume. The accounting cycle from Chapters 3-5 stays intact; what changes is the cast of accounts (Inventory, Cost of Goods Sold, Sales Returns and Allowances, Sales Discounts, Purchase Discounts, Freight In, Freight Out) and the structure of the income statement (Gross Profit becomes a key line that wasn't present for service businesses).

By the end of this chapter, you should be able to:

- Distinguish merchandising from service businesses and explain why their accounting differs.
- Distinguish the *perpetual* inventory system (records updated with every purchase and sale) from the *periodic* system (inventory counted at period-end).
- Journalize purchase transactions, including purchase discounts and purchase returns and allowances, under the perpetual system.
- Journalize sales transactions, including sales discounts and sales returns and allowances, under the perpetual system.
- Apply *FOB shipping point* and *FOB destination* terms to determine which party bears freight cost and when title transfers.
- Prepare a *multi-step income statement* showing Net Sales, Cost of Goods Sold, Gross Profit, Operating Expenses, and Net Income.

You walk in with the full accounting cycle from Chapters 3-5. You walk out with the cycle adapted for inventory-based businesses.

Why does it matter? Because every retailer, every wholesaler, every distributor in the economy runs through this set of accounts. Walmart, Amazon, Costco, your corner bodega — all merchandisers, all using accounts and patterns this chapter teaches. The math is no harder than what you've already learned. The vocabulary is wider, and the income statement gets a new shape that reveals what a service-business income statement could not: how much margin the merchant is making between cost and price.

## 6.2 Merchandiser vs. service business: what's different

A service business — Mark Summers's dry cleaner, a consulting firm, an accounting practice — generates revenue by performing services. The income statement is short: Service Revenue at the top, operating expenses below, Net Income at the bottom. There is no inventory. There is no cost of goods sold.

A merchandiser generates revenue by selling physical goods. Three new structural elements enter:

*Inventory* — the asset account holding goods purchased for resale, valued at cost. Inventory sits on the balance sheet as a current asset until it's sold.

*Cost of Goods Sold (COGS)* — the expense account that captures the *cost* of the inventory that was sold during the period. When a $20 pair of headphones is sold for $50, the merchandiser records $50 of revenue *and* $20 of COGS. The $30 difference is gross profit.

*Gross Profit* — the difference between Net Sales and COGS. It's the most-watched single line on a merchandiser's income statement, because it tells the reader how much margin the business earns on the merchandise itself, before any operating expenses (rent, wages, utilities) come into play.

The income statement of a merchandiser, in its standard *multi-step* form:

```
Net Sales (Sales Revenue − Sales Returns and Allowances − Sales Discounts)
  − Cost of Goods Sold
  = Gross Profit
  − Operating Expenses (Selling Expenses + Administrative Expenses)
  = Operating Income
  ± Other Revenues and Expenses (Interest, Gains, Losses)
  = Net Income
```

The simple income-statement form (revenues minus all expenses to net income, no Gross Profit subtotal) is also legal under GAAP, but the multi-step form is dominant in practice because Gross Profit is too analytically useful to bury.

## 6.3 Perpetual vs. periodic inventory systems

Two systems exist for tracking inventory and COGS, with different operational profiles and reporting timing.

The *perpetual* inventory system updates Inventory and COGS with every purchase and sale, in real time. When J&J buys $5,000 of merchandise, Inventory rises by $5,000 immediately. When J&J sells a unit costing $20, Inventory falls by $20 and COGS rises by $20 *at the moment of sale*. The Inventory balance on the books should match the physical count at any moment (subject to small discrepancies for shrinkage, miscount, theft, which a periodic physical count corrects).

The *periodic* inventory system updates Inventory only at period-end, after a physical count. During the period, purchases are recorded in a Purchases account (not Inventory), and no entry is made for COGS at the time of sale. At period-end, ending Inventory is determined by physical count, and COGS is calculated as: *Beginning Inventory + Purchases − Ending Inventory = Cost of Goods Sold*.

The trade-offs:

Perpetual buys *real-time visibility* of inventory and COGS at the cost of *requiring continuous tracking* — every sale needs cost information at the moment of recording. Modern point-of-sale systems and bar-code scanning make this feasible at scale; before computers, it was prohibitive for high-volume retailers. Today perpetual is the dominant system for any business larger than the smallest.

Periodic buys *operational simplicity during the period* (no cost lookups at sale time) at the cost of *no reliable inventory or COGS figure during the period* — the books simply don't know either number until the count happens. Periodic systems still appear in very small businesses, in some agricultural and seasonal contexts, and in parts of the world where point-of-sale technology is less ubiquitous.

This chapter develops journal entries primarily under the perpetual system, which is what most students will encounter in practice.

## 6.4 Purchase transactions

When J&J Games buys merchandise from Marcus Electronics, several distinct journal-entry patterns can arise.

**Cash purchase:** J&J pays $3,000 cash for merchandise.

| Account | Debit | Credit |
|---|---|---|
| Inventory | $3,000 | |
| Cash | | $3,000 |

**Credit purchase (on account):** J&J buys $3,000 of merchandise on terms 2/10, n/30 (2% discount if paid within 10 days; net amount due in 30).

| Account | Debit | Credit |
|---|---|---|
| Inventory | $3,000 | |
| Accounts Payable | | $3,000 |

**Purchase discount taken:** J&J pays the $3,000 invoice within 10 days, taking the 2% discount of $60.

| Account | Debit | Credit |
|---|---|---|
| Accounts Payable | $3,000 | |
| Cash | | $2,940 |
| Inventory | | $60 |

The credit to Inventory reduces the recorded cost of the merchandise by the discount amount — under the perpetual system, purchase discounts reduce the cost basis of inventory rather than being recorded as a separate revenue account. (Under periodic systems, a Purchase Discounts account holds the credit, but the structural effect is the same.)

**Purchase return:** J&J discovers $200 of the merchandise is defective and returns it for credit.

| Account | Debit | Credit |
|---|---|---|
| Accounts Payable | $200 | |
| Inventory | | $200 |

Inventory is credited (reduced) for the cost of returned goods; Accounts Payable is reduced because the obligation has been canceled to that extent.

**Purchase allowance:** J&J keeps the defective merchandise but receives a $100 credit from Marcus instead of a return.

| Account | Debit | Credit |
|---|---|---|
| Accounts Payable | $100 | |
| Inventory | | $100 |

Same accounts as a return, different operational pattern (the goods stay with J&J).

**Freight In (FOB shipping point):** J&J's purchase contract is FOB shipping point — title transfers at Marcus's loading dock, J&J bears freight cost. Marcus charges $150 for shipping.

| Account | Debit | Credit |
|---|---|---|
| Inventory | $150 | |
| Cash (or Accounts Payable) | | $150 |

Freight In is added to the cost of inventory because it is part of the cost of getting the merchandise ready for resale. Compare with FOB destination, where Marcus bears freight cost — in that case Marcus, not J&J, records the freight expense (as Freight Out, an operating expense, since for Marcus the merchandise is already past the inventory stage and is in delivery to a customer).

The principle: any cost that gets the merchandise *to the merchandiser ready for resale* (Freight In, applicable taxes, handling charges) is added to the cost of inventory. Costs of *delivering* merchandise out to customers are operating expenses, not inventory costs.

## 6.5 Sales transactions

The mirror image. When J&J sells a video-game console, two journal entries fire — one for the revenue, one for the COGS.

**Cash sale:** A customer buys a $200 console (which cost J&J $120).

Revenue side:

| Account | Debit | Credit |
|---|---|---|
| Cash | $200 | |
| Sales Revenue | | $200 |

Cost side (perpetual system):

| Account | Debit | Credit |
|---|---|---|
| Cost of Goods Sold | $120 | |
| Inventory | | $120 |

This dual entry is the defining feature of perpetual-system sales transactions. Every sale records both halves immediately — revenue and the cost of the goods leaving inventory.

**Credit sale:** Same console, but customer buys on terms 2/10, n/30.

| Account | Debit | Credit |
|---|---|---|
| Accounts Receivable | $200 | |
| Sales Revenue | | $200 |

| Account | Debit | Credit |
|---|---|---|
| Cost of Goods Sold | $120 | |
| Inventory | | $120 |

**Sales discount taken:** Customer pays within 10 days, taking 2% off ($4).

| Account | Debit | Credit |
|---|---|---|
| Cash | $196 | |
| Sales Discounts | $4 | |
| Accounts Receivable | | $200 |

Sales Discounts is a *contra-revenue* account — it reduces gross sales when the income statement is prepared. (Net Sales = Gross Sales − Sales Returns and Allowances − Sales Discounts.)

**Sales return:** Customer returns the $200 console undamaged. J&J refunds and the inventory comes back.

Revenue side:

| Account | Debit | Credit |
|---|---|---|
| Sales Returns and Allowances | $200 | |
| Cash (or Accounts Receivable) | | $200 |

Cost side (returned merchandise comes back into inventory):

| Account | Debit | Credit |
|---|---|---|
| Inventory | $120 | |
| Cost of Goods Sold | | $120 |

Sales Returns and Allowances is also a contra-revenue account. The two contra-revenue accounts (Sales Discounts and Sales Returns and Allowances) get netted against gross sales to produce Net Sales on the income statement.

**Sales allowance:** Customer keeps a slightly-damaged $200 console but receives a $30 reduction from J&J.

| Account | Debit | Credit |
|---|---|---|
| Sales Returns and Allowances | $30 | |
| Cash (or Accounts Receivable) | | $30 |

No cost-side entry — the goods stay with the customer; inventory and COGS are unchanged.

**Freight Out (FOB destination):** J&J's sales contract is FOB destination — title transfers when goods arrive at the customer, J&J bears freight cost. J&J pays $25 to a delivery service.

| Account | Debit | Credit |
|---|---|---|
| Freight Out (or Delivery Expense) | $25 | |
| Cash | | $25 |

Freight Out is an *operating expense* on the income statement — typically classified under Selling Expenses — not part of the cost of inventory.

## 6.6 The multi-step income statement

Pulling a merchandiser's transactions into a multi-step income statement at period-end. Suppose for one quarter J&J Games has:

- Sales Revenue (gross): $480,000
- Sales Returns and Allowances: $12,000
- Sales Discounts: $6,000
- Cost of Goods Sold: $280,000
- Selling Expenses (advertising, salesperson wages, Freight Out): $48,000
- Administrative Expenses (rent, utilities, office salaries): $30,000
- Interest Revenue (savings account): $400
- Interest Expense (note payable): $1,200

Multi-step income statement:

```
Sales Revenue                             $480,000
Less: Sales Returns and Allowances         (12,000)
Less: Sales Discounts                       (6,000)
                                          --------
Net Sales                                 $462,000
Less: Cost of Goods Sold                 (280,000)
                                          --------
Gross Profit                              $182,000
Less: Operating Expenses
   Selling Expenses          $48,000
   Administrative Expenses    30,000
                              -------
                                            (78,000)
                                          --------
Operating Income                          $104,000
Plus: Other Revenues
   Interest Revenue                              400
Less: Other Expenses
   Interest Expense                          (1,200)
                                          --------
Net Income                                $103,200
```

The reader can extract several signals from this structure that a simple income statement would obscure:

- *Gross profit margin* = Gross Profit / Net Sales = $182,000 / $462,000 ≈ 39.4%. This tells a reader how much of every sales dollar is left after the direct cost of merchandise. Industry benchmarks vary widely (grocers run 20-30%; specialty retailers can run 50%+).
- *Operating expense ratio* = Operating Expenses / Net Sales = $78,000 / $462,000 ≈ 16.9%.
- *Operating income margin* = Operating Income / Net Sales = $104,000 / $462,000 ≈ 22.5%. Tells the reader how much of every sales dollar survives after both merchandise cost and operating expenses.

These ratios become more meaningful across periods (is gross margin trending up or down?) and across peers (is this retailer's gross margin in line with industry norms or notably high/low?). Quality-of-earnings analysis often starts with these structural splits.

The trade-off in choosing the multi-step format: it buys *analytical visibility* at the cost of *visual complexity*. A simple income statement is easier to read in five seconds; a multi-step is necessary if the reader wants to understand *where* the profit comes from. Most public-company filings use a multi-step or near-multi-step format because the analyst community demands it.

## 6.7 Exercises

### Warm-up

1. **State the formula for Net Sales** in terms of gross sales and the two contra-revenue accounts.

2. **Distinguish FOB shipping point from FOB destination** in one sentence each. Identify which party bears freight cost in each.

3. **Under the perpetual inventory system, why does each sale generate two journal entries?**

### Application

4. **A merchandiser buys $4,000 of merchandise on terms 2/10, n/30.** (a) Journalize the purchase. (b) Journalize the payment 8 days later when the discount is taken. (c) Journalize the payment 25 days later if the discount lapses.

5. **A merchandiser sells goods costing $300 for $500 cash.** Journalize both sides of the transaction under the perpetual system.

6. **A retailer reports for the year: Sales Revenue $620,000; Sales Returns and Allowances $18,000; Sales Discounts $12,000; Cost of Goods Sold $370,000; Selling Expenses $60,000; Administrative Expenses $40,000.** Prepare a multi-step income statement and compute Gross Profit margin and Operating Income margin.

### Synthesis

7. **A wholesaler ships $10,000 of merchandise (cost $7,500) to a retailer on terms FOB destination, with freight of $200 paid by the wholesaler.** Walk through the journal entries on both sides — the wholesaler's books and the retailer's books — for the sale, the cost of goods sold, and the freight.

8. **A retailer uses the periodic inventory system. At year-end the records show:** Beginning Inventory $50,000; Purchases $290,000; Purchase Returns and Allowances $8,000; Purchase Discounts $5,000; Freight In $4,000; Ending Inventory (per physical count) $62,000. Compute Cost of Goods Sold.

### Challenge

9. **Two retailers in the same industry have similar Net Sales but very different Gross Profit margins — Retailer A at 45%, Retailer B at 25%.** Propose at least three plausible reasons grounded only in this chapter's material. What additional information would you want before drawing conclusions?

10. **Imagine a retailer running on a periodic inventory system experiences significant theft over the course of a quarter.** Will the theft be visible in the financial statements? In which account, and how soon? Compare with what would happen under a perpetual system.

## 6.8 Chapter summary

You walked into this chapter with the full accounting cycle adapted for service businesses. You walk out with it adapted for merchandisers.

A merchandiser sells physical goods, which means the books carry an Inventory asset and a Cost of Goods Sold expense that service businesses don't have. The income statement gains a new structural line — Gross Profit — that captures the margin between Net Sales and COGS before operating expenses are subtracted. The perpetual inventory system updates Inventory and COGS in real time at every purchase and sale; the periodic system delays both until a period-end physical count. Most modern businesses use perpetual.

Purchase transactions and sales transactions each have a small family of variants: cash and credit, with discounts taken or lapsed, with returns and allowances, with freight bearing different parties depending on FOB terms. Each variant gets a distinct journal entry; the patterns are systematic.

The multi-step income statement organizes a merchandiser's results into Net Sales, Cost of Goods Sold, Gross Profit, Operating Expenses, Operating Income, and Net Income — supporting the ratios (gross margin, operating margin) that financial analysts use to compare merchandisers across periods and peers.

The single most important idea: every sale at a merchandiser is *two* economic events, not one. Revenue is recorded; the cost of the goods leaving inventory is also recorded. The income statement nets the two against each other to produce Gross Profit, the line that tells a reader how much money the merchant makes on its merchandise.

The common mistake to watch for: treating freight uniformly. Freight In is part of the cost of inventory; Freight Out is an operating expense. The FOB term determines which party records which.

## 6.9 A note on terms, contracts, and credit relationships

The credit terms baked into a purchase or sale invoice are more than convenience features. They encode the trust relationship between the two parties and the cost of waiting for payment.

The notation *2/10, n/30* reads: two percent discount if paid within ten days; net (full) amount due in thirty. The seller is offering a bounty for early payment. From the seller's perspective, a 2% discount on a 30-day invoice is roughly equivalent to a 36% annualized cost of capital on the 20 days the buyer would otherwise hold the cash — because skipping 20 days of float to get 2% off is the same arithmetic as paying 2% to borrow for 20 days, which compounds to a hefty annual rate. Most well-managed buyers take all available purchase discounts even if they have to borrow short-term to do so. The annualized cost of *not* taking a discount is almost always higher than any short-term borrowing rate.

From J&J Games's perspective, taking the 2/10 discount on a $3,000 invoice means $60 in saved cost of inventory, applied against the same goods for the entire time J&J holds them. Across a year of regular purchases the discounts compound into meaningful gross-margin improvement.

Sales discounts work the same way in reverse. The seller offers 2/10 because being paid in ten days is worth more than being paid in thirty — the cash arrives sooner, can be redeployed sooner, and is no longer at risk of becoming an uncollectable account. The arithmetic favors the seller offering the discount and favors the buyer taking it. The terms persist in widespread use because both sides are usually better off than they would be without them.

The FOB terms similarly carry consequences beyond who pays for the truck. Title transfer determines *who bears the risk of damage in transit*. Under FOB shipping point, J&J owns the merchandise from Marcus's loading dock; if the truck crashes en route, J&J's insurance handles it (and J&J's books carry the loss). Under FOB destination, Marcus owns the merchandise until it arrives at J&J's stockroom; the same crash is Marcus's problem. The chosen FOB term should match which party can most efficiently insure and absorb the in-transit risk.

These contractual details — the percentages, the days, the FOB designation — are the small print that distinguishes a sophisticated merchandising operation from an amateur one. The journal entries this chapter teaches are how those details show up in the books, period after period, until the cumulative effect of taking discounts and managing freight terms aggregates into a measurable advantage on the gross margin line of the income statement and a quietly faster cash conversion cycle on the balance sheet.

## 6.10 Connections forward

Chapter 7 turns to *accounting information systems* — the software, controls, and workflows that take the journal entries this chapter taught and run them at the scale of a real business. By the end of Chapter 7, you'll have a sense of how the manual entries you've been writing get automated, what controls keep the automation honest, and what a real chart of accounts and accounting information system looks like at scale.
---

## LLM Exercise — Chapter 6: Merchandising Transactions (AI Bookkeeping Tool Project)

**Project:** AI Bookkeeping Tool.
**What you're building this chapter:** merchandising support — perpetual and periodic inventory systems, purchase and sales transactions with discounts and returns, the multi-step income statement.
**Tool:** **Claude Code.**

---

**The Prompt:**

```
I'm in Chapter 6 of building my AI Bookkeeping Tool. The tool now
handles the full accounting cycle for service businesses. This
chapter taught: merchandiser vs. service business (COGS appears,
inventory exists on the balance sheet); perpetual inventory system
(inventory updated on every transaction; COGS recorded with each
sale) vs. periodic system (inventory updated at period-end via
physical count; COGS computed from beginning inventory + purchases
- ending inventory); purchase transactions (FOB shipping point vs.
FOB destination determines title transfer; purchase discounts
2/10 net 30 type; purchase returns and allowances); sales
transactions (mirror image of purchases — sales discounts, sales
returns, sales allowances); the multi-step income statement (gross
sales → net sales → gross profit → operating income → net income).

Extend the tool. Produce four outputs.

1. **A merchandising-transaction module.** Specialized helpers:
   - `purchase_inventory(supplier, items, terms, fob, date)` —
     handles perpetual (debits Inventory, credits AP) or periodic
     (debits Purchases, credits AP) based on a tool-level setting.
   - `sell_inventory(customer, items, terms, fob, date)` — in
     perpetual, records two entries (revenue and COGS); in periodic,
     records only revenue.
   - `record_purchase_discount_taken(entry, date)` and
     `record_sales_discount_taken(entry, date)` — handle discount
     application when invoice is paid within the discount window.
   - `record_purchase_return(entry, returned_items, date)` and
     `record_sales_return(entry, returned_items, date)`.

2. **An inventory subsystem.** Track inventory items as objects
   (SKU, quantity, unit cost). On perpetual sales, decrement
   quantity and compute COGS using the cost-flow method. For Ch 6,
   use specific identification or simple FIFO. (Ch 10 deepens
   this.)

3. **A multi-step income statement.** Reorganize the income-
   statement generator into the multi-step structure:
   - Gross Sales
   - (Sales Returns, Sales Discounts, Sales Allowances)
   - Net Sales
   - (Cost of Goods Sold)
   - Gross Profit
   - Operating Expenses
   - Operating Income
   - (Non-operating items)
   - Income Before Tax
   - (Income Tax Expense)
   - Net Income

4. **Tests.** A scenario with:
   - 10 inventory purchases in perpetual system with discounts.
   - 8 inventory sales (some with returns).
   - A period-end multi-step income statement that matches the
     manual calculation.
   - The same scenario rerun in periodic system, verifying that
     net income matches (subject to chosen cost-flow method).

Update spec doc.
```

---

**What this produces:** Merchandising support. The tool handles a merchandiser's books — inventory transactions, discounts, returns, and the multi-step income statement.

**How to adapt this prompt:**

- *For your own project:* If your fictional business is a service business (consulting, software, professional services), this chapter is less central. Build the support anyway — it makes the tool usable for a broader range of businesses.
- *For ChatGPT / Gemini:* Works as written.
- *For Claude Code:* The right tool. The perpetual/periodic split is the chapter's most error-prone implementation; rigorous tests pay off.
- *For a Claude Project:* Update spec.

**Connection to previous chapters:** Ch 5's complete-cycle test gets extended — now it can include merchandising transactions.

**Preview of next chapter:** Chapter 7 covers Accounting Information Systems — the architecture refactor. You'll add special journals, subsidiary ledgers, and control accounts. The tool becomes structurally closer to a real ERP.


---

## AI Wayback Machine

**Antoine Lavoisier** was beheaded in the French Revolution despite — or because of — his pioneering role in standardizing measurement and merchant accounting.

**Run this:**

```
Who is Antoine Lavoisier, and how does their work connect to merchandising we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about their career or ideas.
```

→ Search **"Antoine Lavoisier"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to apply Antoine Lavoisier's ideas to a specific accounting question.
- Add a constraint: "Answer including criticisms or limits of Antoine Lavoisier's framework."

What changes? What gets better? What gets worse?
