# Chapter 4 — The Accrual Accounting Process

**Suggested titles**
1. Two Stories About the Same Month
2. When Did You Earn It?
3. Why Profit and Cash Are Not the Same Number

**TL;DR.** Accrual accounting records revenue when earned and expenses when incurred — *not* when cash changes hands. This produces a more honest picture of a firm's economic performance than cash accounting, but it also creates a permanent gap between net income and cash flow that an analyst has to learn to read. This chapter builds the system from first principles: cash vs. accrual, the accounting equation, double-entry mechanics, recognition rules, and depreciation as the hardest case of the matching principle.

---

## The puzzle of two true stories

Imagine a small landscaping business — call it Chris's Landscaping — at the end of August. Chris worked through August, mowing lawns, trimming hedges, hauling brush. He spent some money on truck repairs, fuel, and an annual insurance premium. He invoiced his customers, most of whom paid him within thirty days, but some of whom paid in early August for July work, and one of whom would not pay until September.

Two accountants look at Chris's August. Each prepares an income statement.

**Accountant A**, working on the **cash basis**, asks: how much cash came in during August, and how much went out? She tallies the customer checks Chris deposited (some for July work, none yet for late-August work) and the bills he paid (truck repairs, fuel, the full $1,000 insurance premium for the coming year). Her August income statement shows $1,400 of cash in, $1,150 of cash out, $250 of profit.

**Accountant B**, working on the **accrual basis**, asks: how much economic value did Chris's business generate during August, regardless of cash timing? She counts the revenue Chris *earned* in August — every job he completed, even the one that hasn't been paid yet — and the expenses he *incurred* — including a portion of the insurance premium that covers August (about $83) but excluding the eleven months of insurance that covers future months. Her August income statement shows different numbers. Possibly very different numbers.

**Both income statements are correct.** They are answering different questions. Accountant A is answering "how much cash did the business generate in August?" Accountant B is answering "how much value did the business generate in August?" These are not the same question, and the difference between them is what makes accounting both subtle and contested.

The Securities and Exchange Commission requires every public company in the United States to use accrual accounting in its financial statements. Most large private companies use it too. There is a reason. This chapter is about that reason — and about the mechanics that make accrual accounting work.

For the equity research project, the importance of this chapter is direct. Every line of the income statement and balance sheet in your company's 10-K is produced under accrual accounting rules. If you do not understand the rules, you cannot read what you are looking at. And the gap between net income and cash flow — which is partly a feature of accrual accounting — is one of the things an analyst pays the most attention to.

---

## Learning objectives

After working through this chapter, you should be able to:

- Distinguish cash-basis from accrual-basis accounting and identify which is appropriate for which kind of firm.
- State the accounting equation and the rules of double-entry bookkeeping, and apply them to simple transactions.
- Apply the revenue recognition principle and the expense recognition (matching) principle to short-term transactions.
- Compute straight-line, units-of-production, and double-declining-balance depreciation for a fixed asset.
- Distinguish profit from cash flow, and explain why net income and cash from operations diverge.
- Identify ethical pressure points in revenue recognition and depreciation estimation, with reference to historical cases (Waste Management, WorldCom).

**Prerequisites.** Chapter 2 (corporate structure, what's in a 10-K). One semester of introductory accounting helps; this chapter rebuilds the essentials in case you don't have it.

---

## Concept 1 — Cash vs. accrual: two methods, two answers

### The cash basis

The simplest way to keep books is to record a transaction the moment cash moves. Money in is revenue. Money out is an expense. The income statement is essentially a categorized bank statement. The balance sheet, in its purest cash-basis form, is just the cash balance.

This is how most people manage their personal finances. It is how very small businesses often run. It has real virtues. **Simplicity** — anyone can do it, no special training required. **Cash focus** — for a startup, running out of cash is the failure mode, and a cash-basis system surfaces that risk first. **Tax simplicity** — many small businesses are taxed on a cash basis under IRS rules (with exceptions, particularly for inventory-heavy businesses).

The cash basis also has limits that make it unsuitable for most large firms.

The first problem is **timing distortion**. If Chris pays $1,000 in August for an insurance policy that covers the coming year, cash-basis accounting records a $1,000 expense in August and zero insurance expense in any of the next eleven months. The August income statement looks much worse than the business actually performed; the next eleven months look better than they actually performed. The cash basis tells the truth about cash but lies about the economics.

The second problem is **revenue timing**. If Chris invoices a customer for $500 of work done in late August and receives the check in mid-September, cash-basis accounting records zero August revenue and $500 of September revenue. The work was done in August. The economic value was created in August. The cash basis records it in September. Again, true about cash, misleading about economics.

The third problem is **comparability**. If two firms operate in the same industry but have different customer payment terms — one collects in 15 days, the other in 60 — their cash-basis income statements will look completely different even if their underlying businesses are identical. An investor cannot easily compare them. For public capital markets to function, financial statements need to be comparable across firms.

### The accrual basis

Accrual accounting solves the three problems by separating *economic events* from *cash flows*. Two principles do most of the work.

**Revenue recognition principle.** Revenue is recorded when it is *earned* — when the goods are delivered or the service is performed — not when cash is received. Chris earns the $500 of revenue in August when he does the work, even if the check arrives in September.

**Expense recognition principle (the matching principle).** Expenses are recorded in the period in which they are *incurred*, and ideally in the period in which they help generate the revenue they're paired with. Chris's $1,000 annual insurance premium gets allocated across the twelve months it covers — about $83/month — rather than recorded entirely in August.

The result is an income statement that reflects the *economic substance* of the firm's activity in a given period, regardless of cash timing. Two firms with identical operations but different customer-payment terms will look the same on an accrual income statement. That is the comparability the public capital markets need.

The cost of accrual accounting is **mechanical complexity**. Tracking who owes you money (accounts receivable), who you owe money to (accounts payable), how much of an annual premium has been "used up," when revenue should be recognized for a multi-year contract — these add up to a serious amount of bookkeeping that small businesses often cannot justify.

### Who uses which

The split is roughly:

- **Public companies** — accrual, mandatory under SEC rules and GAAP.
- **Most large private companies** — accrual, often required by lenders for loan covenants.
- **Small businesses without inventory** — often cash, by choice and IRS allowance.
- **Professional services firms (lawyers, doctors, consultants)** — historically often cash; many switched to accrual as they grew.
- **Farms** — often cash, with special IRS provisions.

For the equity research project, every public-company filing you read will be on accrual. The mental discipline to remember is that **net income on an accrual income statement is not cash**. We will track this distinction through the rest of the chapter and re-encounter it formally as the cash flow statement in Chapter 5.

↳ **Dig Deeper — ASC 606 and revenue recognition reform**

*The 2018 implementation of ASC 606 (and IFRS 15 internationally) replaced dozens of industry-specific revenue recognition rules with a unified five-step framework. Some companies' reported revenue patterns shifted noticeably as a result. The reform is a real-world example of a principles-based vs. rules-based accounting trade-off.*

**Prompt:**
> Explain the five-step framework of ASC 606 (identify the contract, identify performance obligations, determine transaction price, allocate to obligations, recognize revenue when obligations are satisfied). Then describe how three different industries (software/SaaS, telecom, construction) had their revenue recognition pattern changed by the rule. What did the rule fix, and what new ambiguities did it introduce?

**What to do with the output:** Save it. When you read your chosen company's 10-K, the revenue recognition footnote will reference ASC 606; understanding the framework helps you assess how the firm applies it.

### The trade-off (concept 1)

Accrual accounting trades **simplicity against economic accuracy**. The cash basis is easier to keep but tells a partial story. The accrual basis is harder to keep but tells a more useful one for analysts, lenders, and investors. Neither is "right" in absolute terms; the choice depends on who needs to read the statements and for what purpose.

### Worked example — Chris's August, both ways

Take Chris's August in detail.

| Event | Cash effect (August) | Accrual effect (August) |
|---|---|---|
| Mows several lawns; sends invoices for $1,400 | $0 cash in (paid in September) | $1,400 revenue recognized |
| Receives July payments of $1,400 from customers | $1,400 cash in | $0 (earned in July) |
| Pays $100 for truck brakes | $100 cash out | $100 expense |
| Pays $50 for fuel | $50 cash out | $50 expense |
| Pays $1,000 for one-year insurance policy | $1,000 cash out | $83 expense (1/12 of premium); $917 prepaid asset |

**Cash-basis August:**
- Revenue: $1,400 (the July collections)
- Expenses: $1,150 ($100 + $50 + $1,000)
- Net income: $250

**Accrual-basis August:**
- Revenue: $1,400 (August work, regardless of when paid)
- Expenses: $233 ($100 + $50 + $83)
- Net income: $1,167

Same business, same August. Cash basis says Chris earned $250. Accrual says he earned $1,167. Which is "the truth"?

Both are. The cash basis is correct about cash; the accrual basis is correct about economic value created. An analyst looking at the firm's economic performance prefers the accrual number. A bank evaluating Chris's ability to pay an upcoming loan installment cares more about cash. This is why public companies report *both* — an income statement and a cash flow statement — every quarter.

### Common misconceptions

- *"Accrual accounting is just an accounting trick."* It is the dominant method globally for a reason — it produces statements that compare across firms and time periods.
- *"If a business is profitable, it has cash."* Not necessarily. A growing firm can be profitable on accrual but cash-poor because it's tied up in receivables and inventory. Many otherwise sound firms have failed for exactly this reason.
- *"Cash-basis accounting is fraudulent."* Not at all — it's perfectly legal for the firms that use it. It just doesn't satisfy the requirements of public-company disclosure.

---

## Concept 2 — The accounting equation and double-entry bookkeeping

### The equation

The foundation of every accrual accounting system is one identity:

$$\text{Assets} = \text{Liabilities} + \text{Equity}$$

Read it as a sources-and-claims statement: every dollar of assets the firm has came from somewhere, and someone has a claim against it. **Liabilities** are claims by creditors (lenders, suppliers, employees who haven't been paid yet, the IRS). **Equity** is the residual claim by the owners — what's left after creditors are paid.

This identity is not a convention. It is a definition. **Equity is defined as Assets minus Liabilities.** The equation cannot fail to balance, in the same sense that the equation $5 = 5$ cannot fail to balance — they are statements of the same thing on either side.

This is why every well-run accounting system is *self-checking*. If your books don't balance, you've made an error somewhere; the equation tells you. (It does not tell you whether the books are *honest*, which is a different question.)

### Categories that go inside the equation

**Assets** are things the firm owns that have economic value. They split by lifespan.

- **Current assets** are expected to be converted to cash or used within one year. Cash, accounts receivable (money customers owe you), inventory, prepaid expenses, short-term investments.
- **Noncurrent (long-term) assets** are held for more than a year. Property, plant, and equipment (PP&E); long-term investments; intangible assets like patents and goodwill.

**Liabilities** are obligations the firm owes.

- **Current liabilities** are due within a year. Accounts payable (money you owe suppliers), accrued expenses (wages owed but not yet paid), short-term debt, the current portion of long-term debt.
- **Noncurrent liabilities** are due in more than a year. Bonds payable, long-term loans, pension obligations.

**Equity** for a corporation is split into two main pieces:

- **Contributed capital** (or paid-in capital, or common stock) — what owners have invested in the firm.
- **Retained earnings** — accumulated profits that have been kept in the business rather than paid out as dividends.

When you read a balance sheet in a 10-K, every line item lands in one of these buckets, and the buckets sum to the equation.

### Double-entry bookkeeping — every transaction has two sides

The mechanism that keeps the accounting equation in balance, transaction by transaction, is **double-entry bookkeeping**. Every transaction affects at least two accounts, and the changes are recorded on opposite sides — debits and credits — in a way that the equation always balances after each entry.

The convention:

| Account type | Increases on... | Decreases on... |
|---|---|---|
| Assets | Debit | Credit |
| Liabilities | Credit | Debit |
| Equity | Credit | Debit |
| Revenue | Credit | Debit |
| Expense | Debit | Credit |

This looks arbitrary. It is half arbitrary and half consequence: assets are on the left side of the equation, so increases live on the left (debit) side of the ledger. Liabilities and equity are on the right side, so increases live on the right (credit) side. Revenue increases equity, so revenue increases on the credit side. Expenses decrease equity, so expenses increase on the debit side.

A few examples make it concrete.

**Transaction 1: Chris invests $5,000 of personal cash to start the business.**

| Account | Debit | Credit |
|---|---|---|
| Cash | $5,000 | |
| Common Stock (Equity) | | $5,000 |

Cash (an asset) goes up — debit it. Equity goes up — credit it. The accounting equation: $5,000 = $0 + $5,000. Balances.

**Transaction 2: Chris buys $200 of supplies on credit.**

| Account | Debit | Credit |
|---|---|---|
| Supplies | $200 | |
| Accounts Payable | | $200 |

An asset (supplies) goes up. A liability (accounts payable) goes up. Equation: $5,200 in assets = $200 in liabilities + $5,000 in equity. Balances.

**Transaction 3: Chris performs $1,400 of services and invoices the customer.**

| Account | Debit | Credit |
|---|---|---|
| Accounts Receivable | $1,400 | |
| Service Revenue | | $1,400 |

An asset (accounts receivable) goes up. Revenue, which increases equity, goes up. Equation: $6,600 in assets = $200 in liabilities + $6,400 in equity. Balances.

This is the system. Every transaction must produce equal debits and credits. If you make an error, the trial balance — the sum of all debits compared to the sum of all credits — will not match, and you'll know to look for it.

For an analyst, you do not need to *do* this bookkeeping. You need to *understand* that every line on the firm's financial statements got there through this system, and that the integrity of the statement depends on the system working correctly. When companies commit accounting fraud, they typically do it not by violating double-entry mechanics but by mislabeling transactions or making improper estimates within the system. The mechanics catch arithmetic errors; they do not catch dishonesty.

↳ **Dig Deeper — When earnings management crosses into fraud**

*The boundary between "aggressive but legal" earnings management and "fraudulent" misrepresentation is fuzzy in real cases. Cookie-jar reserves, big-bath accounting, channel stuffing, and roundtripping all sit somewhere on the continuum. Understanding where the line gets drawn requires looking at specific SEC enforcement cases.*

**Prompt:**
> Walk through three SEC enforcement cases since 2010 where the agency charged a public company with accounting fraud (not just earnings management). For each, describe (1) the specific accounting choice the firm made, (2) why the SEC determined it crossed into fraud rather than aggressive interpretation, and (3) the consequences (fines, executive charges, restatement). Try to pick cases from different industries.

**What to do with the output:** Save it as analytical context. When reading your chosen company's audit reports and footnotes, knowing the line between aggressive and fraudulent helps calibrate your skepticism.

### The trade-off (concept 2)

Double-entry is **redundant by design**. Recording every transaction twice doubles the bookkeeping work. The redundancy buys self-checking and audit trail. Single-entry systems exist (and are used by very small businesses — a checkbook is essentially single-entry) but do not produce the kind of statement reliability that public capital markets need.

### Worked example — building Chris's first balance sheet and income statement

After Transactions 1, 2, and 3 above, plus the August activity from Concept 1's worked example:

**Income Statement (August, accrual basis)**

```
Service Revenue                $1,400
   Truck repairs                 (100)
   Fuel                           (50)
   Insurance (1 month)            (83)
                                ──────
Net Income                       $1,167
```

**Balance Sheet (end of August)**

```
ASSETS
   Cash                          $4,650   ($5,000 − $100 − $50 − $1,000 + previously collected $800 if any)
   Accounts Receivable           $1,400
   Supplies                        $200
   Prepaid Insurance               $917
                                  ──────
   Total Assets                  $7,167

LIABILITIES
   Accounts Payable                $200
                                  ──────
   Total Liabilities               $200

EQUITY
   Common Stock                  $5,000
   Retained Earnings             $1,967   ($1,167 from August + $800 from prior periods, or whatever the prior balance was)
                                  ──────
   Total Equity                  $6,967

   Total Liabilities + Equity    $7,167   ← matches Total Assets ✓
```

The numbers are illustrative and the prior-period balances are simplified for pedagogy. The point is the structure: every transaction recorded under the rules, the equation always balances, the income statement shows accrual economic performance, and both statements derive from the same underlying ledger.

### Common misconceptions

- *"Debit means decrease and credit means increase."* No — and no convention sounds more counterintuitive to first-time accounting students than this. Debit and credit just mean "left side of an account" and "right side of an account." Whether they increase or decrease the account depends on what type of account it is.
- *"The accounting equation only matters at year-end."* It must balance after every transaction.
- *"If the books balance, the firm is honest."* No. The books can balance perfectly and still be fraudulent. Enron's books balanced.

---

## Concept 3 — Recognition over time, and the harder cases

The two principles introduced in Concept 1 — revenue recognition and expense recognition — are the engine of accrual accounting. The engine works fine for simple cases. It runs into hard cases when economic activity stretches across many periods. Three hard cases come up enough to deserve the rest of the chapter.

### Hard case A — Multi-period revenue contracts

Suppose a software company signs a three-year contract to provide a customer with a software service for $360,000, paid up front. When does the company recognize the revenue?

Old answer (pre-2018): It depends, and there were dozens of industry-specific rules.

New answer (post-2018, under ASC 606 / IFRS 15): The revenue is recognized as the company *performs* the service. Roughly $10,000 per month for thirty-six months. When the cash arrives up front, the company records:

| Account | Debit | Credit |
|---|---|---|
| Cash | $360,000 | |
| Deferred Revenue (liability) | | $360,000 |

Deferred revenue is a liability — the company owes the customer thirty-six months of future service. As the service is delivered, $10,000 per month moves out of deferred revenue and into recognized revenue:

| Account | Debit | Credit |
|---|---|---|
| Deferred Revenue | $10,000 | |
| Service Revenue | | $10,000 |

For the equity research project: SaaS companies (Salesforce, Workday, ServiceNow, etc.) carry enormous deferred-revenue balances that are crucial to understanding their economics. A SaaS firm that signs a lot of long-term contracts will have a large deferred-revenue balance — that's a leading indicator of future revenue. Read the deferred-revenue line on these firms' balance sheets carefully; it tells you something the income statement does not.

### Hard case B — Depreciation of long-lived assets

When a firm buys a machine for $58,000 that will last five years, the matching principle says: don't record $58,000 of expense in the year of purchase. Record portions of the cost in each of the five years that the machine helps generate revenue.

This is called **depreciation**. The machine is a fixed asset on the balance sheet, recorded at *historical cost* (what you paid for it, including shipping and setup). Each year, a portion of the cost is moved from "asset" to "expense" via a depreciation entry. Over the asset's useful life, the entire cost (less expected salvage value) gets expensed.

There are several methods, and the choice changes the *timing* of the expense (though not the total).

**Straight-line depreciation.** Equal expense each year. The simplest method.

$$\text{Annual depreciation} = \frac{\text{Cost} - \text{Salvage value}}{\text{Useful life}}$$

For a $58,000 machine with a $10,000 expected salvage value and a 5-year life:

$$\text{Annual depreciation} = \frac{58{,}000 - 10{,}000}{5} = \$9{,}600$$

After year 1, the machine sits on the balance sheet at $58,000 (cost) minus $9,600 (accumulated depreciation) = $48,400 (book value). After year 5, book value reaches $10,000 — the salvage value — and depreciation stops.

**Units-of-production depreciation.** Expense based on actual usage. If the machine is rated to produce 960,000 units over its life, and it produces 180,000 in year 1:

$$\text{Year 1 depreciation} = (58{,}000 - 10{,}000) \times \frac{180{,}000}{960{,}000} = \$9{,}000$$

This better matches expense to economic reality when usage varies year to year.

**Double-declining-balance depreciation.** Front-loads the expense — bigger writeoffs in early years, smaller in later years. The rate is twice the straight-line rate, applied to the *remaining book value* (not the depreciable base):

$$\text{Annual rate} = \frac{2}{\text{Useful life}}$$

For our 5-year machine: $2/5 = 40\%$ annual rate.

| Year | Beginning book value | Depreciation expense | End-of-year book value |
|---|---|---|---|
| 1 | $58,000 | $58,000 × 40% = $23,200 | $34,800 |
| 2 | $34,800 | $34,800 × 40% = $13,920 | $20,880 |
| 3 | $20,880 | $20,880 × 40% = $8,352 | $12,528 |
| 4 | $12,528 | $12,528 × 40% = $5,011 → capped at $2,528 (can't go below salvage) | $10,000 |
| 5 | $10,000 | $0 (already at salvage) | $10,000 |

Total: $48,000, the same total as the other methods. Different *timing* — much more in year 1, much less in years 4–5.

**Why the choice matters for the equity research project.** Two firms with identical economics but different depreciation methods will show different reported earnings in any given year. A firm that uses double-declining-balance shows lower early-year earnings; a firm that uses straight-line shows steadier earnings. Total earnings over the asset's life are the same. When comparing companies, check the depreciation methods in the 10-K's accounting policies footnote — the difference can be material.

**One important note: land is never depreciated.** It is assumed to have unlimited useful life. It sits on the balance sheet at historical cost forever (with periodic write-downs only if the value materially impairs).

### Hard case C — When estimates can be manipulated

Both depreciation and revenue recognition involve **estimates** — useful life, salvage value, percentage-of-completion, expected returns. Estimates are necessary because we cannot know the future. Estimates are also abusable. Two cases illustrate.

**Waste Management (1998–2002).** The trash-collection company was disciplined by the SEC for fraudulently extending the useful lives of its trucks and equipment. By assuming trucks lasted longer than they did, the company reduced annual depreciation expense and inflated reported earnings — by approximately $1.7 billion over multiple years. Several executives faced charges. Andersen, the auditor, missed the manipulation (the firm's troubles with Andersen didn't end with Waste Management — Enron came shortly after).

**WorldCom (2001–2002).** WorldCom committed an even larger fraud by misclassifying *operating expenses* as *capital expenditures*. Operating expenses hit the income statement immediately and reduce reported earnings. Capital expenditures sit on the balance sheet as fixed assets and are depreciated over many years — meaning only a small fraction of the expense hits any given period's income statement. By improperly capitalizing nearly $4 billion of what should have been operating expenses, WorldCom inflated reported earnings dramatically. The fraud unraveled when the firm filed for bankruptcy in July 2002 — at the time, the largest bankruptcy in US history. The CEO went to prison.

The pedagogical lesson is severe. Accounting *looks* mechanical. The mechanics genuinely are mechanical. But the mechanics are built on judgments — *useful life is X years*, *salvage value is Y dollars*, *this expenditure is capital and not operating* — and the judgments are where dishonesty lives. A 10-K reader's job is partly to evaluate the reasonableness of the estimates, not just to verify the arithmetic.

For the equity research project: when reading your company's 10-K accounting policies footnote, pay attention to what management says about useful lives, salvage values, allowance for doubtful accounts, and revenue recognition timing. Compare to peers. Outliers warrant explanation.

### The trade-off (concept 3)

Recognition rules trade **strict matching against operational practicality**. Perfect matching of every dollar of revenue to every dollar of expense in the same period is impossible — economic activity does not respect period boundaries that cleanly. The rules are pragmatic approximations. They produce statements that are *close enough* to economic reality to be useful for analysis, while remaining mechanical enough that two competent accountants applying the same rules to the same facts will arrive at similar numbers. The remaining judgment latitude is the territory where ethics and analysis both live.

### Worked example — finding depreciation in your company's 10-K

In your chosen company's most recent 10-K:

1. Find the **PP&E note** (usually in the financial statement footnotes, often called Note 5 or Note 6, "Property, Plant and Equipment"). It will show:
   - Gross PP&E (the historical cost of all fixed assets the firm owns).
   - Accumulated depreciation.
   - Net PP&E (the difference — the book value).
   - A breakdown by asset type (land, buildings, machinery, equipment, leasehold improvements).
2. Find the **accounting policies footnote** (usually Note 1 or Note 2, "Summary of Significant Accounting Policies"). The depreciation policy will name the method (almost always straight-line for public companies) and the typical useful lives by category (e.g., "Buildings: 25–40 years; Machinery and equipment: 3–10 years").
3. Find the **depreciation expense** line. It usually appears in the cash flow statement (as an add-back to net income to get to cash from operations) and sometimes broken out in the MD&A.

Apple's 10-K, for example, shows total PP&E of about $103 billion gross and roughly $67 billion of accumulated depreciation as of recent fiscal year-ends, leaving net PP&E around $37 billion. The bulk depreciates over 1–10 years; buildings depreciate over up to 30 years. Apple is a useful demo company for the project because its disclosures are clean and its scale is large.[^1]

[^1]: Apple Inc., Form 10-K filings, available via EDGAR. `[verify]` for current vintage.

### Common misconceptions

- *"Depreciation is the loss of value of an asset."* It is the *accounting allocation* of cost over time. The actual market value of an asset can rise or fall independent of the depreciation schedule.
- *"Capitalizing always inflates earnings."* Compared to expensing, yes — in the year of purchase. Over the asset's life, total expense is the same. The cumulative effect is timing, not magnitude.
- *"Aggressive depreciation policies are always wrong."* Not necessarily. A firm with assets that genuinely deteriorate quickly may use accelerated methods legitimately. Context matters; the question is whether the chosen method matches the underlying economic reality.

---

## Synthesis — accrual accounting as a system of intentional gaps

The accrual accounting system creates a deliberate gap between cash and reported earnings, and it does so for good reasons. Cash is real but partial — it tells you what has settled, not what has been done. Earnings, properly measured, tell you what has been *done* — the economic value created in a period — but require assumptions, estimates, and judgments that cash does not.

The price of getting closer to economic reality is opening a door for manipulation. The history of accounting fraud is the history of people walking through that door. The history of accounting reform — Sarbanes-Oxley, ASC 606, the PCAOB, audit-committee independence — is the history of trying to make the door narrower without closing the path to economically meaningful statements.

For the equity research project, this chapter installs three habits:

1. **Always read accrual-basis statements with one eye on the cash flow statement.** The gap between net income and cash from operations is informative. Persistent positive gaps (cash exceeds earnings) often indicate conservative accounting; persistent negative gaps (earnings exceed cash) deserve scrutiny.
2. **Read the accounting policies footnote.** It tells you the choices that produced the numbers. Outliers from industry norms warrant questions.
3. **Read the PP&E and depreciation footnotes carefully.** Asset lives, methods, and impairment activity all carry information.

In Chapter 5, we'll work through the four primary financial statements in detail — income statement, balance sheet, cash flow statement, statement of equity — and learn to read each one as the analyst's primary data source.

---

## Exercises

### Warm-up

**4.1** State the accounting equation. Define each of its three components in your own words.

**4.2** Distinguish revenue recognition under cash basis and accrual basis. Give one example where the two methods produce a different income statement for the same transaction.

**4.3** Define depreciation. Why is land not depreciated?

### Application

**4.4** A firm buys a machine on January 1 for $100,000. Expected useful life: 8 years. Salvage value: $20,000. Compute depreciation expense for years 1, 2, and 3 under:

(a) Straight-line.
(b) Double-declining-balance.
(c) Units-of-production, assuming 30,000 expected total units of output and actual production of 5,000 / 6,000 / 4,000 in years 1 / 2 / 3.

Show the book value at the end of each year for each method.

**4.5** Record the journal entries for the following Chris's Landscaping transactions:

(a) Chris contributes $10,000 of personal cash to the business.
(b) The business buys $500 of supplies on credit.
(c) The business performs $2,000 of work for a customer who pays $1,200 cash and agrees to pay the remaining $800 in 30 days.
(d) The business pays $300 of the supplies bill from (b).
(e) The business pays $1,200 cash for an annual insurance policy starting today.

Confirm that the accounting equation balances after all five entries.

**4.6** Locate the accounting policies footnote in your chosen company's most recent 10-K. Identify:

(a) The depreciation method used.
(b) The range of useful lives by major asset category.
(c) The revenue recognition policy (one paragraph summary).

### Synthesis

**4.7** A friend says: "Accrual accounting is just an artificial way to make profits look bigger than they are. The real measure of a business is cash." Construct your strongest counter-argument in three parts: (a) what cash *misses* about a business, (b) when accrual numbers are *more* informative than cash numbers, and (c) when cash numbers are *more* informative than accrual numbers.

**4.8** WorldCom's accounting fraud — improper capitalization of operating expenses — was technically possible because line operations had genuine ambiguity about whether certain network costs were capital or operating. The boundary is not always clear in legitimate businesses either. Pick a real public company in a capital-intensive industry (telecom, mining, transportation) and examine its 10-K's discussion of capitalized vs. expensed line costs. How does the firm explain the boundary? Does the explanation give you confidence?

### Challenge

**4.9** SaaS companies often report negative GAAP earnings (net losses on the income statement) while reporting positive operating cash flow. Explain the mechanism. Find a real SaaS company in this position and quantify the gap from its most recent 10-K. Argue whether the firm's economics are good or bad — accrual statements alone won't tell you.

**4.10** Compute the cumulative effect of depreciation method choice on a hypothetical $1 billion of total fixed assets over a 10-year period, comparing straight-line to double-declining-balance. How much higher would year-1 GAAP earnings be under straight-line than under DDB? How much lower would year-10 GAAP earnings be? Why does this matter for an analyst comparing two firms with different methods?

---

## Chapter summary

- **Cash-basis accounting** records transactions when cash moves. Simple but partial. Used by small firms.
- **Accrual-basis accounting** records revenue when earned and expenses when incurred. More mechanically complex but produces more economically meaningful statements. Required for public companies under GAAP.
- The **accounting equation** ($\text{Assets} = \text{Liabilities} + \text{Equity}$) is a definitional identity. **Double-entry bookkeeping** keeps the equation in balance after every transaction by recording each transaction as offsetting debits and credits.
- The **revenue recognition principle** records revenue when earned. The **expense recognition (matching) principle** records expenses in the period that produces the matching revenue.
- **Depreciation** spreads a fixed asset's cost over its useful life — straight-line, units-of-production, or double-declining-balance. Total expense is the same; timing differs.
- Estimates (useful life, salvage value, capital vs. operating distinctions) are where accounting fraud most often lives. Waste Management and WorldCom are the canonical cases.

---

## What would change my mind

The chapter argues that accrual accounting is the right framework for public-company financial statements because it produces more economically meaningful and more comparable numbers than the cash basis. The reading would have to revise if (a) a major economy moved away from accrual GAAP/IFRS toward something closer to cash-basis disclosure (no large economy currently does this), or (b) empirical evidence emerged that accrual accounting's susceptibility to manipulation is so severe that the gain in economic meaningfulness is outweighed by the loss in reliability. Some critics of fair-value accounting come close to this position; the consensus answer remains that accrual is the right framework, with reforms aimed at narrowing the manipulation latitude.

## Still puzzling

The cleanest unresolved tension in the chapter is between **rule-based** and **principles-based** accounting. ASC 606 (the 2018 revenue recognition standard) is principles-based — it tells firms what *should* happen and asks them to apply judgment. Older industry-specific GAAP rules were more rule-based — they told firms exactly what to do in defined fact patterns. Principles-based standards are harder to game in obvious ways and easier to game in subtle ways. Rule-based standards are the opposite. I don't have a clean argument for which is better in absolute terms; the optimal mix probably depends on the industry, the regulator's enforcement capacity, and the auditor's ability to challenge management. The chapter doesn't resolve this; subsequent chapters will return to it indirectly when we look at how analysts read footnotes and adjust reported earnings.

---

## Connections forward

- **Chapter 5** unpacks each of the four primary financial statements in detail.
- **Chapter 6** computes ratios from those statements.
- **Chapter 11** uses the cash flow statement (which inherits the cash/accrual gap) for DCF valuation.
- **Chapter 18** uses pro forma statements built on accrual logic for forecasting.

---

---

## LLM Exercise — Chapter 4: Translate Transactions into Accounting Entries

**Project:** Equity Research Report on a Chosen Public Company
**What you're building this chapter:** Develop fluency with how your company's transactions become accounting entries — preparation for Chapter 5's deep read of the four statements.
**Tool:** Claude chat (this exercise doesn't need the full project context).

### The Prompt

```
For [your company], identify three specific recent transactions or events from the most recent 10-K or 8-K filings. Choose one each from these categories:

1. A **revenue-related transaction** (e.g., a major product launch, a long-term contract, a deferred-revenue addition).

2. A **capital expenditure or asset purchase** (e.g., a new facility, equipment purchase, acquisition).

3. A **financing transaction** (e.g., debt issuance, equity issuance, dividend declaration, stock buyback).

For each, write:
- The transaction description with dollar amount and date.
- The journal entry (debits and credits) showing what accounts are affected.
- The expected impact on the income statement and balance sheet over the relevant period.
- Whether the transaction's accounting timing differs from its cash timing (and if so, by how much).

Cite the 10-K or 8-K page or section where you found the information. If you can't find specific dollar amounts, say so rather than inventing.
```

### What this produces

A short technical exercise that builds fluency with accounting linkages. Doesn't necessarily appear in the final report, but the analytical practice transfers to Chapter 5's statement reading.

### How to adapt this prompt

- *For your own company:* Replace [your company]. Adjust the categories if your firm doesn't have material recent transactions in each.
- *For ChatGPT / Gemini:* Identical.
- *For Claude Code:* Not needed for this exercise.
- *For a Claude Project:* Optional; chat works fine.

### Connection to previous chapters

Builds on Chapter 2's understanding of disclosure (8-Ks announce material events). Sets up Chapter 5's deep read of the four statements.

### Preview of next chapter

Chapter 5 walks through the four primary financial statements in detail. The Chapter 5 LLM Exercise will produce a structured summary of all four for your company.

---

**Tags:** accrual-accounting, GAAP, double-entry, depreciation, revenue-recognition, matching-principle


---

## AI Wayback Machine

**William Paton** was co-author of An Introduction to Corporate Accounting Standards (1940) — the foundational text on accrual accounting principles.

**Run this:**

```
Who is William Paton, and how does their work connect to accrual accounting we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about their career or ideas.
```

→ Search **"William Paton"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to apply William Paton's framework to a specific finance question.
- Add a constraint: "Answer including criticisms or limits of William Paton's framework."

What changes? What gets better? What gets worse?
