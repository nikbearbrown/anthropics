# Chapter 4 — The Accrual Accounting Process
*Why the most useful number in a financial statement is the one furthest from cash.*

---

## The puzzle of two true stories

At the end of August, a small landscaping business has finished a full month of work. The owner mowed lawns, trimmed hedges, invoiced customers. He paid for truck repairs, fuel, and a full year's insurance premium up front.

Two accountants look at the same August. Each produces a correct income statement. One says the business earned $250. The other says it earned $1,167.

Both are telling the truth. They are answering different questions. The first asks: how much cash came in versus went out? The second asks: how much economic value did the business actually create? These are not the same question — and the gap between them is the subject of this entire chapter.

The SEC requires every public company in the United States to answer the second question. There is a reason. This chapter is about that reason.

---

## Two methods, two answers

The simpler method is the **cash basis**. Record a transaction the moment cash moves. Money in is revenue. Money out is an expense. The income statement is a categorized bank statement.

This is how most people run their personal finances. It has real virtues. It's simple. It surfaces cash risk clearly — for an early-stage business, running out of cash is the failure mode, and a cash-basis system shows you that danger without delay.

But it has limits that make it unsuitable for large firms.

Suppose the landscaper pays $1,000 in August for an insurance policy covering the next twelve months. Cash-basis accounting records a $1,000 expense in August and zero insurance expense in any of the following eleven months. August looks terrible; the rest of the year looks artificially clean. The cash basis tells the truth about cash. It lies about the economics.

Or: the landscaper does $500 of work in late August but the customer pays in mid-September. Cash-basis records zero August revenue and $500 of September revenue. The work was done in August. The value was created in August. The cash arrived later. Again — true about cash, misleading about when the economic activity happened.

The deeper problem is **comparability**. If two firms have identical underlying operations but different customer payment terms — one collects in 15 days, the other in 60 — their cash-basis income statements will look completely different. An investor trying to compare them would be looking at noise, not signal. Public capital markets require financial statements that mean the same thing across firms.

**Accrual accounting** solves this by separating economic events from cash flows. Two principles do most of the work.

The **revenue recognition principle**: revenue is recorded when it is *earned* — when goods are delivered or a service is performed — not when cash arrives. The $500 landscaping job done in August is August revenue, regardless of when the check clears.

The **expense recognition principle** (usually called the **matching principle**): expenses are recorded in the period they are incurred, ideally matched to the revenue they help generate. The $1,000 annual insurance premium is not an August expense — it's approximately $83 per month for twelve months.

Run those principles through Chris's August:

<!-- → [TABLE: Side-by-side transaction table for Chris's August — columns: Event, Cash effect (August), Accrual effect (August) — rows for: mowing revenue invoiced but uncollected, July collections received, truck repairs, fuel, annual insurance premium; student should see exactly where and why the two methods produce different totals] -->

**Cash-basis August:** $1,400 cash in (prior-month collections), $1,150 cash out (repairs, fuel, full insurance premium). Net income: **$250.**

**Accrual-basis August:** $1,400 revenue earned (August work), $233 in expenses ($100 repairs + $50 fuel + $83 insurance). Net income: **$1,167.**

Same business. Same August. A difference of $917 in reported profit — not because one accountant made an error, but because they were measuring different things.

Which is "correct"? Both are. An analyst evaluating the firm's economic performance prefers the accrual number. A bank evaluating whether Chris can make a loan payment next Tuesday cares about cash. This is exactly why public companies report *both* — an income statement (accrual) and a cash flow statement — every quarter.

<!-- → [INFOGRAPHIC: Two-column summary — "Cash basis answers: How much cash moved?" vs. "Accrual basis answers: How much value was created?" — list the three problems of the cash basis (timing distortion, revenue mismatch, comparability) and show how each is solved by accrual; useful as a quick-reference visual for the conceptual trade-off] -->

---

## The equation underneath everything

Before the mechanics of accrual accounting make sense, you need to see the foundation.

$$\text{Assets} = \text{Liabilities} + \text{Equity}$$

This is not a convention. It is a definition. **Equity is defined as assets minus liabilities** — what's left after creditors are paid. The equation cannot fail to balance for the same reason that $5 = 5$ cannot fail to balance. Both sides describe the same thing from different angles.

Read it as a sources-and-claims statement. Every dollar of assets the firm has came from *somewhere* — either from creditors (liabilities) or from owners (equity). The equation says: the total of what you have equals the total of where it came from.

This identity is the reason accounting is *self-checking*. If your books don't balance, you've made an error, and the equation tells you. It does not tell you whether the books are *honest* — Enron's books balanced — but it catches arithmetic.

**Assets** are things the firm owns with economic value. **Current assets** convert to cash within a year: cash itself, accounts receivable, inventory, prepaid expenses. **Noncurrent assets** are held longer: property, plant, equipment, patents, goodwill.

**Liabilities** are obligations. **Current liabilities** are due within a year: accounts payable, accrued wages, short-term debt. **Noncurrent liabilities** are due further out: bonds, long-term loans, pension obligations.

**Equity** for a corporation has two main pieces: contributed capital (what owners invested) and retained earnings (accumulated profits kept in the business rather than paid out).

<!-- → [TABLE: Balance sheet structure diagram — three columns: Assets (subdivided into Current and Noncurrent with example line items), Liabilities (Current and Noncurrent), Equity (Contributed capital and Retained earnings) — show the equation visually with Assets on the left equaling Liabilities + Equity on the right; student should be able to map any balance sheet line item to its correct bucket] -->

---

## Double-entry: the mechanism that keeps it balanced

The mechanism that maintains the accounting equation through every transaction is **double-entry bookkeeping**. Every transaction affects at least two accounts, recorded on opposite sides, in a way that the equation stays balanced after each entry.

The convention: assets increase on the *debit* side (left); liabilities and equity increase on the *credit* side (right). Revenue increases equity, so revenue increases on the credit side. Expenses decrease equity, so expenses increase on the debit side.

This sounds arbitrary until you see where it comes from. Assets are on the left side of the equation — their natural home is the left (debit) side of the ledger. Liabilities and equity are on the right — their natural home is the right (credit) side. The rest follows.

Three transactions build intuition.

**Transaction 1: Chris invests $5,000 of personal cash to start the business.**

| Account | Debit | Credit |
|---|---|---|
| Cash | $5,000 | |
| Common Stock (Equity) | | $5,000 |

Cash, an asset, goes up — debit it. Equity goes up — credit it. Equation: $5,000 assets = $0 liabilities + $5,000 equity. Balanced.

**Transaction 2: Chris buys $200 of supplies on credit.**

| Account | Debit | Credit |
|---|---|---|
| Supplies | $200 | |
| Accounts Payable | | $200 |

An asset rises. A liability rises. Equation: $5,200 = $200 + $5,000. Balanced.

**Transaction 3: Chris performs $1,400 of services and invoices the customer.**

| Account | Debit | Credit |
|---|---|---|
| Accounts Receivable | $1,400 | |
| Service Revenue | | $1,400 |

An asset (the receivable) rises. Revenue, which increases equity, rises. Equation: $6,600 = $200 + $6,400. Balanced.

<!-- → [DIAGRAM: T-account layout for the three transactions above — show left/right structure of each account with the debit/credit entries labeled; annotate the running balance of the accounting equation after each transaction so the student can see it hold throughout] -->

You, as an analyst, will never do this bookkeeping. What you need from it is one insight: every line on a firm's financial statements got there through this system. The system's integrity depends on correct account classification. When accounting fraud occurs, it almost never involves arithmetic errors — the debits still equal the credits. The fraud happens in *labeling* — calling an expense a capital expenditure, calling a liability a revenue. The mechanics are clean. The dishonesty is in the categorization.

---

## The hard cases

The revenue recognition and matching principles work cleanly for simple transactions. They get harder when economic activity stretches across many periods. Three cases come up enough to require attention.

### Multi-period contracts

A software company signs a three-year contract to provide service for $360,000, paid up front. When is the revenue recognized?

The answer under current rules (ASC 606 / IFRS 15, adopted in 2018): as the service is *delivered* — roughly $10,000 per month for thirty-six months. When the cash arrives:

| Account | Debit | Credit |
|---|---|---|
| Cash | $360,000 | |
| Deferred Revenue (liability) | | $360,000 |

Deferred revenue is a liability — the company owes the customer thirty-six months of future service. Each month, $10,000 moves from liability to revenue as the obligation is fulfilled.

<!-- → [CHART: Stacked bar or waterfall chart showing deferred revenue balance declining by $10,000/month over 36 months, with recognized revenue growing cumulatively — student should see the relationship between the liability drawdown and income statement recognition] -->

This matters enormously for the equity research project. SaaS companies — Salesforce, Workday, ServiceNow — carry deferred-revenue balances that are leading indicators of future revenue. A large deferred-revenue balance means contracts have been signed and cash has been collected but the service hasn't been delivered yet. Revenue will show up in future income statements as the company earns it. Reading that balance is a way of seeing income-statement line items before they appear.

↳ **Dig Deeper — ASC 606 and revenue recognition reform**

*The 2018 implementation of ASC 606 (and IFRS 15 internationally) replaced dozens of industry-specific revenue recognition rules with a unified five-step framework. Some companies' reported revenue patterns shifted noticeably as a result.*

**Prompt:**
> Explain the five-step framework of ASC 606 (identify the contract, identify performance obligations, determine transaction price, allocate to obligations, recognize revenue when obligations are satisfied). Then describe how three different industries (software/SaaS, telecom, construction) had their revenue recognition pattern changed by the rule. What did the rule fix, and what new ambiguities did it introduce?

**What to do with the output:** Save it. When you read your chosen company's 10-K, the revenue recognition footnote will reference ASC 606; understanding the framework helps you assess how the firm applies it.

### Depreciation of long-lived assets

When a firm buys a machine for $58,000 that will last five years, the matching principle says: don't record $58,000 of expense in the year of purchase. Record portions of the cost in each of the five years the machine helps generate revenue.

This is **depreciation** — the annual allocation of a fixed asset's cost over its useful life. Three methods exist, and the choice changes when the expense is recognized, though not how much total expense there is.

**Straight-line** allocates equal expense each year:

$$\text{Annual depreciation} = \frac{\text{Cost} - \text{Salvage value}}{\text{Useful life}} = \frac{58{,}000 - 10{,}000}{5} = \$9{,}600$$

**Units-of-production** ties expense to actual output. If the machine is rated for 960,000 lifetime units and produces 180,000 in year 1:

$$\text{Year 1 depreciation} = (58{,}000 - 10{,}000) \times \frac{180{,}000}{960{,}000} = \$9{,}000$$

**Double-declining-balance** front-loads expense — larger writeoffs early, smaller later. The rate is twice the straight-line rate, applied to remaining book value:

$$\text{Annual rate} = \frac{2}{5} = 40\%$$

| Year | Beginning book value | Depreciation | Ending book value |
|---|---|---|---|
| 1 | $58,000 | $23,200 | $34,800 |
| 2 | $34,800 | $13,920 | $20,880 |
| 3 | $20,880 | $8,352 | $12,528 |
| 4 | $12,528 | $2,528 (floored at salvage) | $10,000 |
| 5 | $10,000 | $0 | $10,000 |

Total depreciation across all methods: $48,000. The timing differs; the total does not.

<!-- → [CHART: Line chart comparing annual depreciation expense under all three methods for the $58,000 machine over 5 years — student should see straight-line as flat, DDB as steeply front-loaded, and units-of-production as variable; annotate that all three sum to the same total] -->

For the equity research project, this matters because two firms with identical economics but different depreciation methods report different earnings in any given year. Straight-line is by far the most common method for public companies. Check the accounting policies footnote — if a firm uses a different method, there is usually a reason, and the reason is worth understanding.

One point that confuses nearly everyone: **depreciation is not a cash outflow**. The cash left the firm when the machine was purchased. Depreciation is an accounting entry that allocates that historical cash outflow across multiple income statement periods. This is exactly why depreciation gets *added back* to net income on the cash flow statement — it reduced reported earnings without reducing cash.

<!-- → [DIAGRAM: Timeline showing the $58,000 machine purchase — single cash outflow arrow at time 0, then five annual depreciation arrows on the income statement across years 1–5; annotate that cash flow and earnings impact happen at different moments; student should internalize why depreciation is a non-cash add-back on the cash flow statement] -->

### When estimates become manipulation

Both depreciation and revenue recognition require estimates — useful life, salvage value, percentage of completion. Estimates are necessary because the future is unknowable. Estimates are also abusable. Two historical cases define the boundary.

**Waste Management (1998–2002).** The trash-collection company fraudulently extended the assumed useful lives of its trucks and containers. By assuming equipment lasted longer than it actually did, the company reduced annual depreciation expense and inflated reported earnings — by approximately $1.7 billion over multiple years. The mechanics were ordinary; the inputs were dishonest.

**WorldCom (2001–2002).** A larger and more instructive fraud. WorldCom improperly classified approximately $4 billion of *operating expenses* as *capital expenditures*. The distinction matters enormously: operating expenses hit the income statement immediately and reduce current-period earnings. Capital expenditures sit on the balance sheet as fixed assets and are depreciated over many years — so only a small fraction of the cost hits any given period's income statement. By mislabeling operating costs as capital investments, WorldCom inflated reported earnings across multiple quarters. The fraud unraveled when the company filed for bankruptcy in July 2002 — the largest bankruptcy in US history to that point. The CEO was convicted.

The WorldCom case is pedagogically important because it shows that accounting fraud doesn't require exotic techniques. Double-entry still worked perfectly. The debits equaled the credits. The fraud was entirely in one classification decision: is this cost an operating expense or a capital expenditure? That is a judgment call in legitimate accounting too — the line is genuinely fuzzy for some costs. WorldCom crossed from judgment into fraud by making choices that no reasonable accountant applying the rules honestly would make.

For the equity research project: when reading the accounting policies footnote, pay attention to what management says about useful lives, capital-versus-operating classifications, and allowance estimates. Compare the stated useful lives against industry peers. Outliers warrant a question.

---

## The permanent gap

Accrual accounting creates a deliberate, structural gap between net income and cash flow. It does this on purpose. The gap is not a bug; it is the whole point.

Cash is real but partial. It tells you what has *settled*, not what has been *done*. Earnings, properly measured under accrual rules, tell you what was done — the economic value created in a period — but they require assumptions and estimates that cash does not.

The price of getting closer to economic reality is opening a door for manipulation. The history of accounting fraud is the history of people walking through that door. The history of accounting reform — Sarbanes-Oxley, ASC 606, audit-committee independence — is the history of trying to narrow the door without closing the path to economically meaningful statements.

For the equity research project, this chapter installs three habits:

**First**, read accrual-basis statements with one eye on the cash flow statement. The gap between net income and cash from operations is a signal. Persistent positive gaps — cash exceeds earnings — often indicate conservative accounting. Persistent negative gaps — earnings exceed cash — deserve scrutiny.

**Second**, read the accounting policies footnote. It tells you the choices that produced the numbers. Choices that deviate from industry norms need explanation.

**Third**, read the PP&E and depreciation footnotes carefully. Asset lives, methods, impairment charges, and accumulated depreciation relative to gross cost all carry information that the income statement alone doesn't surface.

In Chapter 5, we'll work through all four primary financial statements in detail — income statement, balance sheet, cash flow statement, statement of equity — and learn to read each one the way an analyst actually reads them.

---

## What would change my mind

The chapter argues that accrual accounting is the right framework for public-company financial statements because it produces more economically meaningful and more comparable numbers than the cash basis. The reading would have to revise if evidence emerged that accrual accounting's susceptibility to manipulation is so severe that the gain in economic meaningfulness is outweighed by the loss in reliability. Some critics of fair-value accounting come close to this position. The consensus answer remains that accrual is the right framework, with reforms aimed at narrowing manipulation latitude rather than abandoning the method.

## Still puzzling

The unresolved tension is between **rule-based** and **principles-based** accounting. ASC 606 is principles-based — it tells firms what *should* happen and asks them to apply judgment. Older industry-specific GAAP rules were more rule-based — they prescribed exact treatment in defined fact patterns. Principles-based standards are harder to game in obvious ways and easier to game in subtle ways. Rule-based standards are the reverse. I don't have a clean argument for which is better in absolute terms; the optimal mix probably depends on the industry, the regulator's enforcement capacity, and the auditor's willingness to challenge management. Subsequent chapters return to this indirectly when we look at how analysts read footnotes and adjust reported earnings.

---

## Connections forward

- **Chapter 5** unpacks each of the four primary financial statements in detail.
- **Chapter 6** computes ratios from those statements.
- **Chapter 11** uses the cash flow statement — which inherits the cash/accrual gap — for DCF valuation.
- **Chapter 18** uses pro forma statements built on accrual logic for forecasting.

---

## Exercises

### Warm-up

**4.1** In your own words, state the accounting equation. Define each of its three components, and explain in one sentence why the equation cannot fail to balance.

**4.2** A freelance consultant finishes a project in November. The client pays in January. Under the cash basis, when is the revenue recorded? Under the accrual basis? Write one sentence explaining which method better reflects the economic substance of the transaction, and why.

**4.3** What is depreciation? Why is it added back to net income on the cash flow statement rather than treated as a cash outflow?

### Application

**4.4** A firm purchases equipment on January 1 for $80,000. Expected useful life: 8 years. Salvage value: $8,000. Compute depreciation expense for years 1, 2, and 3 under:

(a) Straight-line.
(b) Double-declining-balance.
(c) Units-of-production, assuming 720,000 expected total units of output and actual production of 90,000 / 108,000 / 72,000 in years 1 / 2 / 3.

For each method, show the ending book value after year 3.

**4.5** Record the journal entry for each of the following transactions. For each entry, confirm that the accounting equation remains balanced.

(a) A business owner invests $15,000 of personal cash to start the business.
(b) The business borrows $10,000 from a bank (one-year loan).
(c) The business performs $3,000 of services for a client and invoices them (payment due in 30 days).
(d) The business pays $600 cash for one year of insurance coverage starting today.
(e) The client from (c) pays the invoice in full.

**4.6** A SaaS company signs a two-year contract on July 1 for $240,000, paid in full up front.

(a) Record the journal entry when the cash is received.
(b) Record the monthly entry as service is delivered.
(c) What is the deferred revenue balance on December 31 of the same year (six months later)?
(d) Why does the deferred revenue balance appear as a liability on the balance sheet rather than as revenue?

### Synthesis

**4.7** A friend says: "Accrual accounting is just an artificial way to make profits look bigger than they are. Cash is the only honest measure." Construct your counter-argument in three parts: (a) what cash-basis income statements *miss* about a firm's economics; (b) a concrete situation where accrual earnings are *more* informative than cash flow; (c) a concrete situation where cash flow is *more* informative than accrual earnings.

**4.8** WorldCom's fraud involved reclassifying operating expenses as capital expenditures. In your own company's most recent 10-K, find the capital expenditures disclosure (usually in the cash flow statement and the PP&E footnote). What categories of spending does the firm capitalize? Does the firm's explanation of what qualifies as capital versus operating expense seem reasonable given its business? Explain your reasoning.

### Challenge

**4.9** Two competitors in the same industry — call them Firm A and Firm B — have identical underlying operations. Firm A depreciates its equipment over 5 years using straight-line. Firm B uses double-declining-balance over the same 5-year life. Both buy $10 million of equipment on the same date.

(a) By how much will their reported net income differ in year 1? In year 5?
(b) Over the full 5-year period, does one firm report higher total earnings than the other?
(c) If you were comparing these two firms as an analyst, what adjustment would you make, and why?

**4.10** Find a SaaS or subscription-software company in your chosen 10-K or a publicly available filing. Locate the deferred revenue balance on the balance sheet and the revenue recognition footnote. How large is the deferred revenue balance relative to annual revenue? What does the rate of change in deferred revenue from one year to the next tell you about the company's growth trajectory that the income statement alone does not show?

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

## AI Wayback Machine

**William Paton** was co-author of *An Introduction to Corporate Accounting Standards* (1940) — the foundational text on accrual accounting principles.

**Run this:**

```
Who is William Paton, and how does their work connect to accrual accounting we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about their career or ideas.
```

→ Search **"William Paton"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to apply William Paton's framework to a specific accounting question.
- Add a constraint: "Answer including criticisms or limits of William Paton's framework."

What changes? What gets better? What gets worse?

---

**Tags:** accrual-accounting, GAAP, double-entry, depreciation, revenue-recognition, matching-principle
