# Chapter 9 — Accounting for Receivables

## 9.1 Opening: The asset that hasn't arrived

A merchandiser sells a $4,000 order on credit, terms net 30. The journal entry records $4,000 of revenue (the income statement) and $4,000 of accounts receivable (the balance sheet). The company has done its part — the goods have shipped, the invoice has gone out. What it doesn't yet have is the cash. For the next thirty days, the $4,000 sits in Accounts Receivable, an asset, waiting.

Accounts receivable is the most ambiguous asset on a typical balance sheet. Cash is cash. Inventory you can count. Equipment you can touch. Receivables are *promises* — promises by customers to pay, in the future, in amounts the seller has already recognized as revenue. Most of them will pay. Some won't. Some will pay late. Some will dispute. The asset on the balance sheet is the company's best estimate of how much of the gross receivable it will actually collect — *net realizable value* — and the methodology for getting from gross receivables to net realizable value is the substance of this chapter.

By the end of this chapter, you should be able to:

- Distinguish *accounts receivable* (open trade credit) from *notes receivable* (formal IOUs with stated interest and maturity).
- Apply the *direct write-off method* and the *allowance method* for handling uncollectible accounts, and explain why GAAP requires the allowance method for any business whose receivables are material.
- Estimate uncollectible accounts using the *percentage-of-sales method* and the *percentage-of-receivables method* (including aging schedules).
- Journalize transactions for notes receivable, including the calculation of interest on dishonored or unpaid notes.
- Compute and interpret the *accounts receivable turnover* ratio and the *number of days' sales in receivables*.

You walk in with the merchandising mechanics from Chapter 6 and the cash controls from Chapter 8. You walk out with the discipline of treating receivables as an asset whose realizable value is always less than its face value, and knowing how that gap gets recorded.

## 9.2 Accounts receivable, notes receivable, and other receivables

*Accounts receivable* are amounts customers owe the company arising from sales of goods or services on credit. They are typically uncollateralized, due within 30-60 days, and informal — there's an invoice but no signed promissory note. The vast majority of B2B trade credit lives here.

*Notes receivable* are written promises to pay a specific amount on a specific date with a specific interest rate. The note is a more formal instrument — signed, often notarized for larger amounts — and typically arises in three contexts: (1) the customer needs more time to pay than ordinary trade credit allows, and converts an overdue account receivable into a note; (2) the company lends money outright; (3) the company sells expensive equipment with extended financing.

*Other receivables* — interest receivable, tax refunds receivable, employee advances, insurance claims receivable. Smaller in dollar terms, broken out separately on the balance sheet when material.

The balance-sheet presentation: under Current Assets, *Accounts receivable* is shown net of the *Allowance for Doubtful Accounts* (a contra-asset). The line might read:

```
Accounts receivable                       $487,000
Less: Allowance for doubtful accounts     (24,000)
Accounts receivable, net                  $463,000
```

The $463,000 net figure is the *net realizable value* — what the company expects actually to collect. The $24,000 allowance is the company's estimate of how much of the gross will go uncollected.

## 9.3 Direct write-off vs. allowance method

Two methods exist for handling uncollectible accounts. The choice has structural consequences.

### Direct write-off method

The simple version. When a specific account is determined to be uncollectible, the company writes it off directly: Debit Bad Debt Expense, Credit Accounts Receivable. There is no advance estimation, no allowance account.

The problem with this method is the *matching principle*. Suppose a 2024 sale is determined to be uncollectible in mid-2025. The revenue was recognized in 2024; the bad-debt expense lands in 2025. Two periods are misstated — 2024's income overstated, 2025's understated. For any business with material receivables, the matching distortion is material.

GAAP permits the direct write-off method only when receivables are *immaterial* — typically a small business with low credit volume. For most businesses, GAAP requires the allowance method.

### Allowance method

The standard. The company estimates, at the end of each period, what portion of its receivables will eventually go uncollected, and records that estimate as Bad Debt Expense in the period of the related sale. The estimate accumulates in *Allowance for Doubtful Accounts*, a contra-asset to Accounts Receivable.

The period-end adjusting entry:

| Account | Debit | Credit |
|---|---|---|
| Bad Debt Expense | (estimated) | |
| Allowance for Doubtful Accounts | | (estimated) |

When a specific account is later identified as uncollectible, the *write-off* is recorded against the allowance, not against expense:

| Account | Debit | Credit |
|---|---|---|
| Allowance for Doubtful Accounts | (specific amount) | |
| Accounts Receivable — Customer X | | (specific amount) |

Net realizable value of receivables is unchanged by the write-off — both Accounts Receivable and the Allowance go down by the same amount, leaving the net the same. The expense was recognized when the allowance was established, in the period of the sale. The matching principle is satisfied.

If a customer whose account was written off later pays anyway — *recovery of an account previously written off* — the write-off is reversed and then the cash receipt is recorded:

| Account | Debit | Credit |
|---|---|---|
| Accounts Receivable — Customer X | $X | |
| Allowance for Doubtful Accounts | | $X |

| Account | Debit | Credit |
|---|---|---|
| Cash | $X | |
| Accounts Receivable — Customer X | | $X |

## 9.4 Estimating uncollectibles: two methods

The allowance approach requires an *estimate* of how much of receivables will go bad. Two methods produce the estimate.

### Percentage-of-sales method

The company estimates bad debts as a percentage of *credit sales* for the period. The percentage is derived from historical experience — say, the company has historically lost 1.5% of credit sales to bad debts. If credit sales for the period are $800,000, the estimated bad-debt expense is $800,000 × 1.5% = $12,000. The adjusting entry:

| Account | Debit | Credit |
|---|---|---|
| Bad Debt Expense | $12,000 | |
| Allowance for Doubtful Accounts | | $12,000 |

The percentage-of-sales method emphasizes the *income statement* — bad-debt expense is matched to the period's revenue. It does not adjust to a target balance in the Allowance — the estimate is simply added to whatever balance was already there.

### Percentage-of-receivables method

The company estimates the *target balance* in the Allowance based on the year-end accounts-receivable balance. Various approaches:

*Flat percentage*: estimated uncollectibles = % × ending accounts receivable. Simple but imprecise.

*Aging schedule*: receivables are stratified by how long they've been outstanding, and a different percentage applied to each stratum. Older receivables are more likely to go uncollected. A typical aging:

| Age | Amount | Estimated % uncollectible | Estimated allowance |
|---|---|---|---|
| Not yet due | $300,000 | 1% | $3,000 |
| 1-30 days past due | $100,000 | 5% | $5,000 |
| 31-60 days past due | $40,000 | 15% | $6,000 |
| 61-90 days past due | $20,000 | 30% | $6,000 |
| Over 90 days past due | $10,000 | 60% | $6,000 |
| **Total** | **$470,000** | | **$26,000** |

The estimated target balance in the Allowance is $26,000. The adjusting entry brings the existing Allowance to that target:

If the existing Allowance has a credit balance of $4,000, the adjusting entry: Debit Bad Debt Expense $22,000, Credit Allowance for Doubtful Accounts $22,000 (raising the Allowance from $4,000 to $26,000).

If the existing Allowance has a debit balance (which happens when prior-period write-offs exceeded prior-period estimates) of $2,000, the adjusting entry: Debit Bad Debt Expense $28,000, Credit Allowance for Doubtful Accounts $28,000 (raising the Allowance from −$2,000 to +$26,000).

The percentage-of-receivables / aging method emphasizes the *balance sheet* — the Allowance is set to whatever balance best reflects the realizable value of the year-end receivables.

The trade-off: percentage-of-sales gives cleaner matching to revenue but can drift the Allowance balance over time if estimates are persistently off. Percentage-of-receivables / aging gives a more accurate balance-sheet figure but can produce volatile bad-debt expense as the Allowance is reset each period. Many companies use the aging method as the primary estimate and the sales method as a sanity check.

## 9.5 Notes receivable

A note receivable is a written promise to pay a specific *principal* amount on a specific *maturity date*, with a stated *interest rate*. The note exists as a separate document; the entry on the books records both the principal and (over the life of the note) the interest.

Origination. Suppose a customer with a $5,000 overdue accounts-receivable balance signs a 90-day, 8% note for the same amount on April 1.

| Account | Debit | Credit |
|---|---|---|
| Notes Receivable | $5,000 | |
| Accounts Receivable | | $5,000 |

The receivable converts from open trade credit to a formal note.

Interest accrual. Interest on a note is calculated as: *Principal × Annual Interest Rate × (Days / 360)*. Some industries use 365 days; the textbook convention is often 360 for simplicity. For our note: $5,000 × 8% × (90/360) = $100 of interest over 90 days.

If the note straddles a period-end, interest is accrued to the period boundary. Suppose May 31 is a period-end. Days April 1 to May 31 = 60. Interest accrued = $5,000 × 8% × (60/360) = $66.67.

| Account | Debit | Credit |
|---|---|---|
| Interest Receivable | $66.67 | |
| Interest Revenue | | $66.67 |

Maturity. June 30 (90 days after April 1), the customer pays principal plus the full $100 of interest:

| Account | Debit | Credit |
|---|---|---|
| Cash | $5,100 | |
| Notes Receivable | | $5,000 |
| Interest Receivable | | $66.67 |
| Interest Revenue | | $33.33 |

The Interest Receivable already accrued at May 31 ($66.67) is collected; the remaining $33.33 of interest earned in June is recognized as Interest Revenue at maturity.

*Dishonored* note. If the customer fails to pay at maturity, the note is *dishonored*. The company typically transfers the principal plus accrued interest back to Accounts Receivable and continues collection efforts:

| Account | Debit | Credit |
|---|---|---|
| Accounts Receivable — Customer X | $5,100 | |
| Notes Receivable | | $5,000 |
| Interest Revenue (or Interest Receivable) | | $100 |

If collection ultimately fails, the receivable goes through the allowance / write-off process from §9.3.

## 9.6 Receivables ratios

Two ratios are standard for analyzing how well a company is managing its receivables.

*Accounts receivable turnover*: Net Credit Sales / Average Accounts Receivable. Measures how many times during the period the receivables balance was "turned over" — collected and replenished. Higher is better; it means cash is coming in fast and stale receivables aren't piling up.

*Number of days' sales in receivables* (also called *Days Sales Outstanding*, DSO): 365 / Accounts Receivable Turnover. The same information, expressed in days: how long, on average, does it take to collect a receivable? Lower is better.

Industry benchmarks vary widely. A high-volume retailer with mostly cash sales has DSO near zero. A B2B distributor on net-30 terms typically runs DSO between 30 and 50 days (some lag is normal, since not all customers pay on time). A specialty manufacturer selling on net-90 terms might run DSO of 90-110 days. Trends matter as much as levels — a company whose DSO is climbing year over year is signaling either looser credit policy, deteriorating customer quality, or weakening collection effort.

## 9.7 Exercises

### Warm-up

1. **Distinguish accounts receivable from notes receivable** in two sentences each.

2. **Why does GAAP require the allowance method for any business with material receivables?**

3. **State the formula for accounts receivable turnover and explain what a higher number means.**

### Application

4. **A company has credit sales of $1,200,000 for the year and uses the percentage-of-sales method, estimating 2% of credit sales will be uncollectible.** Journalize the year-end adjusting entry.

5. **A company's aging schedule produces an estimated uncollectible balance of $34,000 at year-end. The Allowance for Doubtful Accounts has a credit balance of $5,000 before adjustment.** Journalize the adjusting entry.

6. **A company writes off a specific $1,800 customer account.** (a) Journalize the write-off under the allowance method. (b) Three months later the customer pays in full. Journalize the recovery.

### Synthesis

7. **A 60-day, 6% note for $9,000 is dated November 1 and matures December 31.** Calculate the interest. Journalize origination, no accrual needed (note matures within the period), and collection at maturity.

8. **A company shows accounts receivable turnover of 8.5 in Year 1, 6.8 in Year 2, and 5.4 in Year 3.** Convert each to days sales outstanding and discuss what the trend suggests. What additional information would you want before drawing a conclusion?

### Challenge

9. **An aging schedule shows uncollectibility percentages of 1%, 5%, 15%, 30%, and 60% across age buckets.** Where do these percentages come from in practice, and what should a controller do if a recent period's actual write-offs are running consistently higher than the schedule predicted?

10. **A company switches from the percentage-of-sales method to the aging method midway through a fiscal year.** Discuss what happens to the Allowance balance and to bad-debt expense in the year of the switch, and what disclosure GAAP would require.

## 9.8 Chapter summary

You walked into this chapter with merchandising mechanics. You walk out with the discipline of treating receivables as an asset whose realizable value is always less than its face.

Accounts receivable arise from credit sales and are reported on the balance sheet net of an Allowance for Doubtful Accounts, producing a net realizable value. The allowance method — required by GAAP for any business with material receivables — estimates uncollectibles in the period of sale, satisfying the matching principle. Two estimation approaches: percentage-of-sales (income-statement-focused) and percentage-of-receivables / aging (balance-sheet-focused).

Notes receivable are formal instruments with stated principal, interest, and maturity. Interest accrues over the life of the note and is recognized in the period earned. Dishonored notes typically convert back to accounts receivable and may ultimately be written off.

The accounts-receivable-turnover ratio and days-sales-outstanding are the standard measures of how efficiently the company is collecting from customers. Trends matter as much as absolute levels.

The single most important idea: the receivables on a balance sheet are not all going to be collected, and reporting them as if they were misleads readers. The allowance method is how the books admit that, in advance, in the period the related revenue was recognized.

The common mistake to watch for: confusing the allowance method's *estimate* of uncollectibility (the period-end adjusting entry, hitting Bad Debt Expense) with the eventual *write-off* of a specific account (which hits the Allowance, not Bad Debt Expense). Two distinct events, recorded differently.

## 9.9 Credit policy and the cost of receivables

A line on the balance sheet hides several real-world decisions that produced it. A controller who takes receivables seriously will think about the credit policy that generated them.

Every dollar of accounts receivable is a dollar the company has loaned its customer interest-free. If the company's cost of capital is 8% and its average customer pays at day 45, the implicit interest cost on that capital is 8% × (45/365) ≈ 1% of the receivable balance — every period. Spread across a year of credit sales, this is a real expense, even though it never appears on the income statement as one. Tighter credit terms shrink that cost; looser credit terms expand it.

The trade-off is between this carrying cost and the volume of sales the credit policy makes possible. A company that demands cash on delivery loses the customers whose business model requires net-30 trade credit (which is most B2B). A company that extends 90-day terms to anyone who asks finances a substantial portion of its customers' working capital and will see receivables balloon. The right policy depends on industry norms, customer profile, and the company's own access to capital — but the policy is a deliberate choice, not a default.

Three operational moves for a controller managing receivables.

*Set explicit credit limits per customer.* No customer should be able to run up an unlimited balance. New customers get a low limit; established customers earn higher limits through payment history. The limits are enforced at the order-entry stage, not after shipment.

*Run credit checks before extending material credit.* Dun & Bradstreet, Experian, and other commercial credit bureaus rate businesses on payment history and financial strength. The cost of a check ($50 to a few hundred dollars) is trivial against the cost of a $50,000 bad debt.

*Have a defined collections process with escalation.* Day 1 past due: a polite reminder. Day 15: a firmer reminder. Day 30: a phone call from the AR clerk. Day 60: escalation to a manager. Day 90: hold on new orders. Day 120: turnover to a collection agency or attorney. The escalation should be predictable to the customer — late-paying customers learn the rhythm and adjust to whatever schedule the seller actually enforces.

A receivable that hasn't been collected in 120 days is not just a slow account; it's a signal that something has changed at the customer — either their financial situation, their dispute about the goods or services, or simply their willingness to pay you specifically. Each requires a different response.

## 9.10 A note on factoring and receivables financing

Companies sometimes do not want to wait for receivables to collect. If working capital is tight, the company can convert receivables to cash earlier through *factoring* — selling the receivables to a third-party finance company at a discount.

The mechanics: the company sells $100,000 of receivables to a factor for, say, $96,000 cash. The factor takes ownership of the receivables and either collects from the customer or, in some arrangements, has recourse back to the seller if the customer doesn't pay. The 4% discount is the factor's profit and its compensation for taking the credit risk and the time value of waiting for collection.

The journal entry on the seller's side, for a non-recourse sale (factor bears the credit risk):

| Account | Debit | Credit |
|---|---|---|
| Cash | $96,000 | |
| Loss on Sale of Receivables (or Factoring Expense) | $4,000 | |
| Accounts Receivable | | $100,000 |

Factoring is more common in industries where receivables are large relative to operating capital — manufacturing with long collection cycles, staffing companies, healthcare. The cost of factoring is essentially a financing cost; companies typically use it when the cost is lower than alternatives (drawing on a credit line, selling equity).

Closely related: *credit card sales*. When a retailer accepts a credit card, the card network pays the retailer (typically within 24-48 hours) less a *merchant discount* (typically 1.5-3% of the transaction). From the retailer's perspective, the credit card company is a permanent factor for those sales — the retailer never carries the receivable, the card network does. The merchant discount is the price for that arrangement; for most retailers it's well worth it because cash arrives almost immediately and the credit risk shifts entirely to the card network.

## 9.11 The interaction with revenue recognition

A subtle but consequential point: an accounts receivable exists *because* revenue was recognized. The two arise together at the moment the company performs its obligation under the sales contract. If revenue recognition is delayed (because performance obligations aren't yet complete, or because collection is genuinely uncertain), no receivable is recorded yet either.

The 2014 update to revenue recognition standards (ASC 606 in U.S. GAAP, IFRS 15 internationally) tightened the criteria for recognizing revenue. One of the criteria is that collection of consideration is probable. If a sale is made to a customer whose creditworthiness is so doubtful that collection is *not* probable, the sale should not generate revenue at all — it generates a deposit liability until performance is complete or until collectibility becomes probable. The allowance method assumes that collectibility *was* probable at recognition; the allowance is for the small percentage that turns out, in retrospect, to be uncollectible.

The practical implication for a controller: extending credit to customers whose creditworthiness is doubtful produces revenue and receivables that shouldn't have existed in the first place under the strict reading of the standard, plus large allowance entries to true up. Tightening credit policy upstream — refusing to ship to customers whose credit checks fail — is cleaner accounting and cleaner business than booking the sale and writing it off later.

## 9.12 Connections forward

Chapter 10 turns to *inventory* — the asset that for merchandisers and manufacturers often dwarfs receivables in dollar terms. You'll see the cost-flow assumptions (FIFO, LIFO, weighted average) that determine which costs get assigned to ending inventory versus to cost of goods sold, and why the choice can change reported income substantially.
---

## LLM Exercise — Chapter 9: Accounting for Receivables (AI Bookkeeping Tool Project)

**Project:** AI Bookkeeping Tool.
**What you're building this chapter:** the receivables module — allowance method for doubtful accounts (percentage-of-sales + aging), notes receivable with interest accrual, receivables ratios, factoring.
**Tool:** **Claude Code.**

---

**The Prompt:**

```
I'm in Chapter 9 of building my AI Bookkeeping Tool. This chapter
taught: accounts receivable, notes receivable, and other
receivables; direct write-off vs. allowance method (allowance
required by GAAP for material AR); two methods of estimating
uncollectibles — percentage-of-sales (income-statement approach;
expense = X% of credit sales) and aging-of-receivables (balance-
sheet approach; allowance balance = sum of aged buckets × bucket
percentages); notes receivable with interest (debt instrument
with face value, interest rate, maturity); receivables ratios (AR
turnover = net credit sales ÷ average net AR; days sales
outstanding = 365 ÷ AR turnover); factoring (selling AR to a
third party at a discount).

Extend the tool. Produce five outputs.

1. **An allowance-for-doubtful-accounts module.** Functions for:
   - `record_bad_debt_estimate_percentage_of_sales(period, rate)` —
     produces the adjusting entry (debit Bad Debt Expense, credit
     ADA) at the chosen percentage.
   - `record_bad_debt_estimate_aging(aging_schedule)` — takes an
     aging schedule with bucket percentages, computes target ADA
     balance, produces the adjusting entry to bring ADA to that
     balance.
   - `write_off_uncollectible_account(customer, amount, date)` —
     debits ADA, credits AR-Customer.
   - `recover_previously_written_off_account(customer, amount,
     date)` — reverses the write-off and records the cash receipt.

2. **An AR aging generator.** A function that:
   - Reads the AR subsidiary ledger as of a given date.
   - Buckets each customer's balance by age (current, 1–30 days,
     31–60, 61–90, >90).
   - Produces a sheet showing each customer and the total in each
     bucket.

3. **A notes-receivable module.** Functions for:
   - `accept_note_receivable(maker, face_value, rate, term_days,
     date)` — creates the note and journalizes (debit Notes
     Receivable, credit AR or Cash or whatever was given up).
   - `accrue_note_interest(note_id, as_of_date)` — accrues interest
     for partial periods (debit Interest Receivable, credit Interest
     Revenue).
   - `collect_note_at_maturity(note_id, date)` — final entry with
     full interest.
   - `dishonor_note(note_id, date)` — debits AR for face + accrued
     interest, credits Notes Receivable and Interest Revenue.

4. **A factoring module.** Functions for:
   - `factor_receivables(receivables_to_sell, factor_fee_pct,
     date)` — debits Cash, debits Loss on Sale of AR (for fee),
     credits AR.

5. **A receivables-ratios module.** Computes AR turnover and DSO
   for a period.

Tests for each. Update spec.
```

---

**What this produces:** A full receivables subsystem. The aging generator and bad-debt-estimate functions are the most operationally consequential — they're what catches receivables that are heading bad before they're written off.

**How to adapt this prompt:**

- *For your own project:* If your fictional business is mostly cash sales (a coffee shop), the receivables module gets exercised lightly. Build it anyway — the next time the business extends credit, it's already ready.
- *For ChatGPT / Gemini:* Works as written.
- *For Claude Code:* The right tool. Aging generation benefits from concrete test data — generate 10–15 customers with various credit histories.
- *For a Claude Project:* Update spec.

**Connection to previous chapters:** Ch 7's subsidiary ledger for AR + Ch 9's aging analysis work together — the aging reads from the subsidiary ledger.

**Preview of next chapter:** Chapter 10 deepens inventory — the three cost-flow assumptions (FIFO, LIFO, weighted average) implemented properly, plus lower of cost or net realizable value. The simple specific-identification approach from Ch 6 gets generalized.


---

## AI Wayback Machine

**Edward Altman** was developed the Z-score in 1968 — the credit-risk model that still anchors how analysts evaluate receivables.

**Run this:**

```
Who is Edward Altman, and how does their work connect to accounting for receivables we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about their career or ideas.
```

→ Search **"Edward Altman"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to apply Edward Altman's ideas to a specific accounting question.
- Add a constraint: "Answer including criticisms or limits of Edward Altman's framework."

What changes? What gets better? What gets worse?
