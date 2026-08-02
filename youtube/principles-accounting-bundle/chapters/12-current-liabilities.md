# Chapter 12 — Current Liabilities

## 12.1 Opening: The other side of the ledger

We've spent eleven chapters building up the asset side of the balance sheet — cash, receivables, inventory, equipment, intangibles. Each chapter took a single asset class and worked through how it was recorded, valued, and reported. The balance sheet has another half. Liabilities are the obligations the company owes to others — the *claims* against its assets that aren't owners' claims. The accounting equation A = L + E will not balance unless the L side gets the same disciplined attention as the A side.

This chapter is about *current* liabilities — those due within a year (or one operating cycle, whichever is longer). Chapter 13 takes the long-term liabilities. The split is structural: short-term obligations are an immediate solvency question; long-term obligations are a capital-structure question.

By the end of this chapter, you should be able to:

- Identify the major categories of current liabilities: accounts payable, notes payable (short-term), payroll-related liabilities, sales tax payable, unearned revenue, current portion of long-term debt, dividends payable, contingent liabilities (when they qualify).
- Journalize transactions involving short-term notes payable, including interest accrual and principal repayment.
- Journalize payroll, including the employee-side withholdings and the employer-side payroll tax accruals.
- Recognize *contingent liabilities* and apply the *probable / reasonably possible / remote* criteria to determine whether they are recorded, disclosed, or ignored.
- Compute and interpret the *current ratio* and the *quick ratio* (acid-test ratio) as measures of short-term solvency.

## 12.2 Accounts payable and short-term notes payable

*Accounts payable* — the merchandiser's and service provider's open trade credit, the mirror image of accounts receivable from Chapter 9. When a company buys goods or services on net-30 terms, the entry is Debit Asset/Expense, Credit Accounts Payable. When the bill is paid (within or after the discount window), Accounts Payable is debited and Cash credited.

A discount taken on payment within the early-payment window — Chapter 6's 2/10, n/30 in reverse — reduces the recorded cost of inventory if the underlying purchase was inventory; for service purchases, the discount is typically credited to a Purchase Discount Revenue or netted directly. The amounts are usually small relative to the gross liability.

*Short-term notes payable* are formal IOUs with stated principal, interest rate, and maturity within a year. Used when a vendor extends a longer payment term than ordinary trade credit, when a company borrows from a bank short-term, or when an overdue accounts-payable balance is converted to a note.

A 90-day, 6% note for $20,000 issued April 1:

| Account | Debit | Credit |
|---|---|---|
| Cash | $20,000 | |
| Notes Payable | | $20,000 |

Interest accrues over the term: $20,000 × 6% × (90/360) = $300. If June 30 is a period-end, interest is accrued to that date:

Days April 1 to June 30 = 91 (close enough to 90 for this illustration; in practice, day-counting conventions matter). Accrued interest = $20,000 × 6% × (90/360) = $300:

| Account | Debit | Credit |
|---|---|---|
| Interest Expense | $300 | |
| Interest Payable | | $300 |

At maturity (June 30 or close), the company pays principal and interest:

| Account | Debit | Credit |
|---|---|---|
| Notes Payable | $20,000 | |
| Interest Payable | $300 | |
| Cash | | $20,300 |

A *discount note* is a variant where the interest is deducted upfront and the borrower receives less than face value. A 90-day $20,000 note at 6% discount: borrower receives $20,000 − $300 = $19,700, repays $20,000 at maturity. The mechanics differ slightly — Discount on Notes Payable is recorded as a contra-liability and amortized to Interest Expense over the term — but the economic effect is the same.

## 12.3 Payroll and the employer's hidden liabilities

Payroll is one of the most heavily regulated and structurally complex liability categories in accounting. A single employee paycheck triggers multiple liability accounts.

Suppose an employee earns $5,000 in gross wages for the period. From the *employee's* paycheck:

- Federal income tax withheld: $750 (varies by W-4)
- State income tax withheld: $200 (varies by state)
- FICA — Social Security tax (6.2%): $310
- FICA — Medicare tax (1.45%): $72.50
- Health insurance premium (employee portion): $150
- 401(k) contribution: $250

Net pay to employee: $5,000 − $750 − $200 − $310 − $72.50 − $150 − $250 = $3,267.50.

Journal entry:

| Account | Debit | Credit |
|---|---|---|
| Wages Expense | $5,000 | |
| Federal Income Tax Withholding Payable | | $750 |
| State Income Tax Withholding Payable | | $200 |
| FICA — Social Security Payable | | $310 |
| FICA — Medicare Payable | | $72.50 |
| Health Insurance Premium Payable | | $150 |
| 401(k) Contribution Payable | | $250 |
| Cash (Wages Payable) | | $3,267.50 |

The employee is paid $3,267.50; the rest of the gross wages sits in payable accounts until the company remits the funds to the IRS, the state, the insurance carrier, the 401(k) administrator. The employer is essentially a tax-collection and benefits-administration agent for these third parties.

But it doesn't end there. The *employer* owes its own payroll-related taxes — taxes paid by the employer rather than withheld from the employee:

- FICA — Social Security tax (employer match): $310
- FICA — Medicare tax (employer match): $72.50
- Federal Unemployment Tax (FUTA — typically 0.6% on first $7,000 of wages per employee per year): varies
- State Unemployment Tax (SUTA — varies by state and employer's experience rating)

The employer-tax accrual:

| Account | Debit | Credit |
|---|---|---|
| Payroll Tax Expense | (sum) | |
| FICA — Social Security Payable (employer) | | $310 |
| FICA — Medicare Payable (employer) | | $72.50 |
| FUTA Payable | | (varies) |
| SUTA Payable | | (varies) |

The employer's true cost of an employee earning $5,000 gross is $5,000 plus the employer payroll-tax burden plus any employer-paid benefits (health insurance employer share, retirement match, paid time off accrual). In total, for a fully-loaded U.S. employee, the cost to the company is typically 1.25 to 1.4 times the employee's stated salary.

The structural lesson: payroll generates liabilities to many parties — employees, federal IRS, state tax authorities, insurance carriers, retirement administrators — and the bookkeeping has to track each one separately. Payroll is the single most common place for small-business accounting errors, both because of its volume and because of the number of distinct payable accounts each payroll cycle touches.

## 12.4 Sales tax payable

A retailer collects sales tax from customers and owes it to the state (or local) tax authority. The sales tax is *not the company's revenue*; it's a pass-through obligation.

A retailer sells $100 of merchandise at a 7% sales tax rate:

| Account | Debit | Credit |
|---|---|---|
| Cash | $107 | |
| Sales Revenue | | $100 |
| Sales Tax Payable | | $7 |

When the company remits the collected tax to the state (typically monthly):

| Account | Debit | Credit |
|---|---|---|
| Sales Tax Payable | $7 | |
| Cash | | $7 |

The retailer never recognized the $7 as revenue, never had any expense related to it, and only had it on the balance sheet between collection and remittance. This is the standard treatment for any pass-through tax — the company is a collector, not the taxpayer.

## 12.5 Unearned revenue

We met unearned revenue in Chapter 4 as a deferred revenue. Customer pays in advance, company hasn't yet performed. The cash receipt creates a *liability* (the obligation to deliver), not revenue. As performance occurs, portions of the liability convert to revenue.

A magazine publisher receives $480 for a 12-month subscription on July 1:

| Account | Debit | Credit |
|---|---|---|
| Cash | $480 | |
| Unearned Subscription Revenue | | $480 |

Each month, the adjusting entry recognizes one month's earned revenue:

| Account | Debit | Credit |
|---|---|---|
| Unearned Subscription Revenue | $40 | |
| Subscription Revenue | | $40 |

Unearned revenue appears as a current liability if it will be earned within a year, noncurrent if longer (e.g., a multi-year warranty). Software companies, magazines, gym memberships, prepaid services all carry substantial unearned revenue balances.

## 12.6 Current portion of long-term debt

A company with a long-term mortgage or note has the *current portion of long-term debt* — the principal payments due within the next year — reported as a current liability, with the remainder as a long-term liability. The split is required because short-term solvency analysis depends on knowing what's due soon.

For a $200,000 mortgage with $24,000 of principal payments due in the next 12 months:

```
Current Liabilities:
   Current portion of long-term debt    $24,000
Long-term Liabilities:
   Mortgage payable                    $176,000
```

The mortgage itself is a single instrument; the balance sheet splits it into the two parts based on payment timing. Each year, as principal is paid down and the next 12 months of payments shifts forward, the split is recomputed.

## 12.7 Contingent liabilities

A *contingent liability* is a potential obligation whose existence depends on a future event. Pending lawsuits, product warranty claims yet to be filed, environmental remediation, tax disputes. The accounting question: should it be recorded, disclosed, or ignored?

GAAP applies a three-tier framework based on (a) probability of occurrence and (b) ability to estimate the amount.

*Probable and reasonably estimable* — *record* the liability and corresponding loss in the current period. Example: a lawsuit the company's lawyers say is likely to result in a $3 million settlement, with $3 million being a reasonable estimate.

*Reasonably possible (less than probable but more than remote)* — *disclose* in the notes to the financial statements but do not record. Example: a lawsuit the company is defending where the outcome is uncertain.

*Remote* — *ignore*. No recording, no disclosure required.

Product warranty obligations are a particular case. A company that sells products with a one-year warranty has a probable obligation (some warranty claims will come in) and can estimate the total cost based on historical experience (say, 2% of sales). At year-end, the company accrues:

| Account | Debit | Credit |
|---|---|---|
| Warranty Expense | (estimated) | |
| Warranty Liability | | (estimated) |

When actual warranty claims come in, they're charged against the Warranty Liability rather than against Warranty Expense again — the expense was recognized when the related sales were made.

Estimating contingent liabilities involves judgment, and the estimates are watched carefully by auditors and regulators. Underestimating a probable obligation overstates net income.

## 12.8 The current ratio and the quick ratio

We met the *current ratio* in Chapter 5: Current Assets / Current Liabilities. A second ratio, the *quick ratio* (or *acid-test ratio*), tightens the test:

Quick Ratio = (Cash + Short-Term Investments + Net Accounts Receivable) / Current Liabilities

The quick ratio excludes inventory and prepaid expenses from the numerator. The reasoning: inventory might not convert to cash quickly enough in a short-term-solvency crisis; prepaid expenses don't convert to cash at all. Cash, marketable securities, and receivables (which collect within weeks) are the truly liquid assets a company can deploy against immediate obligations.

A company with a current ratio of 2.0 and a quick ratio of 0.4 is signaling that most of its current assets are tied up in inventory or prepaid items — short-term obligations might be hard to meet without liquidating slow-moving inventory. A company with a current ratio of 1.5 and a quick ratio of 1.2 has truly liquid assets close to or above its current liabilities — short-term solvency is strong even excluding inventory.

The two ratios together tell a fuller story than either alone. Both are industry-dependent — grocers run thin current ratios because their inventory turns so fast; capital-intensive manufacturers run thicker ones because their working-capital cycle is longer.

## 12.9 Exercises

### Warm-up

1. **Name five categories of current liabilities** introduced in this chapter.

2. **State the formulas for the current ratio and the quick ratio** and explain how they differ.

3. **A company sells $200 of merchandise plus 6% sales tax.** Journalize the sale.

### Application

4. **A company issues a 120-day, 5% note payable for $30,000 on March 1.** Compute the interest at maturity. Journalize issuance, period-end accrual at June 30, and payment at maturity.

5. **An employee's gross pay for a period is $4,000. Withholdings: federal income tax $400, FICA Social Security 6.2%, FICA Medicare 1.45%, health insurance $120. Employer matches the FICA taxes.** Journalize the payroll entry and the employer payroll-tax accrual entry.

6. **A retailer collected $84,000 of sales tax during the quarter and remits it to the state.** Journalize the remittance.

### Synthesis

7. **A company is being sued for $5 million. Its lawyers indicate the suit is more likely than not to succeed against the company, with a likely settlement of $2-3 million.** What is the proper accounting treatment under GAAP? What if the lawyers indicate the case is "reasonably possible" but the amount cannot be reliably estimated? What if "remote"?

8. **A magazine publisher's December 31 balance sheet shows Unearned Subscription Revenue of $1,800,000.** Explain in two sentences what this represents and how it will be reduced over the next 12 months.

### Challenge

9. **A company's current ratio is 2.5 but its quick ratio is 0.6.** Walk through what this combination is signaling about the composition of current assets, and what additional information you would want before making a credit decision.

10. **The fully-loaded cost of a U.S. employee earning $80,000 in stated salary is typically $100,000-$112,000.** Itemize the additional employer costs that produce the gap and explain why each is structurally a current liability or current expense.

## 12.10 Chapter summary

You walked into this chapter with a deep understanding of the asset side of the balance sheet. You walk out with the short-term liability side.

Current liabilities — those due within a year — include accounts payable, short-term notes payable, payroll-related liabilities (employee withholdings and employer taxes), sales tax payable, unearned revenue, current portion of long-term debt, dividends payable, and contingent liabilities that meet the recording threshold.

Short-term notes payable carry interest that accrues over the note's life and is paid at maturity. Payroll triggers many liability accounts simultaneously — to employees, to tax authorities, to benefits administrators — and is the single most error-prone bookkeeping category for small businesses. Sales tax is a pass-through liability, never recorded as the company's revenue. Unearned revenue is a liability until performance occurs.

Contingent liabilities are accounted for under a three-tier framework (probable / reasonably possible / remote) that determines whether they're recorded, disclosed, or ignored. Warranty obligations are the canonical recorded contingent liability for product companies.

The current ratio and quick ratio are the two standard short-term-solvency measures. The quick ratio's exclusion of inventory and prepaids tightens the test — a company can pass the current ratio and fail the quick ratio if too much working capital is tied up in slow-moving inventory.

The single most important idea: current liabilities are not a single homogeneous category. The risk profile of an account payable (a vendor obligation, with relationship leverage) differs from the risk profile of a payroll liability (a legal obligation with quick remittance deadlines), which differs from the risk profile of unearned revenue (a performance obligation, settled by delivery rather than cash). A reader of the balance sheet who lumps them together loses information.

The common mistake to watch for: treating sales tax collected as revenue. It isn't. The collecting business is a tax agent, not the taxpayer.

## 12.11 Working capital management

A topic that ties together everything in this chapter and Chapters 9-10. *Working capital* is current assets minus current liabilities — the company's short-term operating cushion. Every receivable, every inventory unit, every prepaid expense is working capital tied up; every payable, every accrued expense, every deferred revenue is working capital extended by counterparties. Managing working capital — the *cash conversion cycle* — is one of the most consequential and underappreciated jobs in a finance organization.

The cash conversion cycle measures how long, on average, a dollar invested in inventory takes to come back as cash from a customer. The components:

- *Days' sales in inventory* (DSI) — how long inventory sits before selling (Chapter 10's measure).
- *Days' sales outstanding* (DSO) — how long after sale before the customer pays (Chapter 9's measure).
- *Days' payables outstanding* (DPO) — how long after purchase before the company pays its vendors.

Cash conversion cycle = DSI + DSO − DPO.

A company with DSI of 60 days, DSO of 45 days, and DPO of 30 days has a cash conversion cycle of 75 days. Each dollar spent on inventory is tied up in working capital for 75 days before returning to cash. A company with DSI of 30 days, DSO of 25 days, and DPO of 50 days has a *negative* cash conversion cycle of −5 days. Such companies — Amazon, Walmart, Costco — finance their growth from the working-capital float of their suppliers and customers, rather than from external borrowing or equity raises. This is one of the structural advantages those businesses enjoy.

For most other businesses, shrinking the cash conversion cycle is a continuous operational priority. Faster inventory turnover, faster collections, slower (within terms) payments to vendors — each component contributes. Most of what the controller and CFO actually do day-to-day in operational finance comes back to the working-capital cycle.

## 12.12 The interaction with the operating cash flow

The connection to the cash flow statement (which we'll develop fully in Chapter 16) is direct. Operating cash flow = Net Income + Depreciation/Amortization (non-cash charges) ± changes in working capital. A growing company that accumulates inventory and receivables faster than it accumulates payables will see operating cash flow lag behind net income. A company that compresses its working capital cycle will see operating cash flow exceed net income.

This is one of the most common patterns in financial statements: companies with strong income but weak operating cash flow have either growing working capital, aggressive revenue recognition, or quality-of-earnings issues. The relationship between the two figures is one of the most diagnostic things a financial reader looks at.

## 12.13 Dividends payable and similar discretionary liabilities

A few categories of current liability arise from discretionary decisions rather than from normal operations. The most common is *dividends payable* — created when a corporation's board declares a dividend. The board's declaration creates the legal obligation to pay; the actual cash payment comes later (typically a few weeks).

When the board declares a $500,000 dividend on June 15, payable July 15 to shareholders of record June 30:

| Account | Debit | Credit |
|---|---|---|
| Retained Earnings (or Dividends) | $500,000 | |
| Dividends Payable | | $500,000 |

When the cash is paid on July 15:

| Account | Debit | Credit |
|---|---|---|
| Dividends Payable | $500,000 | |
| Cash | | $500,000 |

Between the declaration date and the payment date, Dividends Payable sits on the balance sheet as a current liability. Companies that have declared dividends but haven't paid them yet show this — a single line that signals an upcoming cash outflow to equity holders. We'll develop the corporate-equity side fully in Chapter 14.

A related case: *income tax payable*. Estimated income taxes accrue throughout the year as net income is earned. The accrual hits Income Tax Expense (debit) and Income Tax Payable (credit). When the company makes its quarterly estimated tax payments to the IRS, Income Tax Payable is debited and Cash credited. At year-end, any difference between accrued and paid is settled when the annual return is filed. Income Tax Payable is a current liability for amounts due within a year; deferred-tax accounts (which arise from timing differences between book income and taxable income) are typically noncurrent.

## 12.14 A note on order of presentation

Convention: current liabilities are typically presented in the order Accounts Payable, Notes Payable, Accrued Liabilities, Unearned Revenue, Current Portion of Long-Term Debt, with various subcategories. The order is not legally specified by GAAP; it varies by company and industry. Most balance sheets group similar items together with subtotals where useful. The footnotes provide additional detail — particularly for accrued liabilities, which often get aggregated on the face of the balance sheet but broken out by type in the notes.

A subtlety: if a company has a long-term obligation that is callable on demand by the lender (for example, a covenant violation that gives the lender the right to demand immediate repayment), the obligation must be reclassified as current even if the lender has not actually called it. Substance-over-form rules apply. The same logic governs the current-portion-of-long-term-debt classification.

## 12.16 Connections forward

Chapter 13 takes the long-term liability side — bonds payable, long-term notes payable, mortgages, lease liabilities, deferred tax. The accounting mechanics get more complex (present-value calculations, premium and discount amortization, effective-interest method), but the structural concept is the same: an obligation owed by the company to someone else, recorded on the balance sheet, recognized on the income statement as interest expense over time.
---

## LLM Exercise — Chapter 12: Current Liabilities (AI Bookkeeping Tool Project)

**Project:** AI Bookkeeping Tool.
**What you're building this chapter:** the current-liabilities module — payroll with employer obligations, sales tax payable, unearned revenue, contingent liabilities, current/quick ratios.
**Tool:** **Claude Code.**

---

**The Prompt:**

```
I'm in Chapter 12 of building my AI Bookkeeping Tool. This chapter
taught: accounts payable and short-term notes payable; the payroll
cycle (gross wages → employee withholdings — federal income tax,
state income tax, FICA-Social Security 6.2%, FICA-Medicare 1.45% —
→ net pay) and the employer's hidden liabilities (FICA matching,
FUTA 0.6% on first $7,000 wages, SUTA varying by state); sales tax
payable (collected from customers, owed to state); unearned revenue
(cash received before service rendered); current portion of long-
term debt (the portion due within 12 months reclassified each
period); contingent liabilities (probable / reasonably possible /
remote — recorded if probable and estimable, disclosed if reasonably
possible); current ratio = CA/CL; quick ratio = (CA - Inventory -
Prepaid)/CL.

Extend the tool. Produce four outputs.

1. **A payroll module.** Functions for:
   - `process_payroll(period, employees_data, tax_rates)` — given
     each employee's gross wages, computes:
     - Employee withholdings: federal income tax, state income tax,
       FICA-SS (6.2%), FICA-Medicare (1.45%), other deductions.
     - Net pay.
     - Employer obligations: FICA matching (6.2% + 1.45%), FUTA
       (0.6% on first $7K cumulative), SUTA (state-specific).
   - Journalizes both halves:
     - Employee side: Debit Salaries Expense (gross), Credit each
       withholding liability, Credit Cash (net).
     - Employer side: Debit Payroll Tax Expense (employer's portion),
       Credit each tax liability.

2. **A sales-tax-collection module.** Functions for:
   - Sales transactions: collect sales tax in addition to the sale
     price; credit Sales Tax Payable separately.
   - Remit sales tax: debit Sales Tax Payable, credit Cash on the
     filing date.

3. **An unearned-revenue module.** Helpers for the receive-cash-
   before-service pattern (Ch 4's deferred revenue), with periodic
   recognition.

4. **A contingent-liability log.** A structure to track:
   - Probability (probable / reasonably possible / remote).
   - Estimable (yes / no).
   - Estimated amount or range.
   - Source (lawsuit, warranty, product recall, etc.).
   Functions:
   - `record_probable_contingency(amount, source)` — journalizes
     (debit Loss, credit Liability).
   - `disclose_reasonably_possible_contingency(amount_range, source)`
     — generates a disclosure entry for the financial-statement
     notes (no journal entry).

Plus current-ratio and quick-ratio calculations. Tests for each.

Update spec.
```

---

**What this produces:** A current-liabilities module that handles the realistic complexity of a small business — payroll, sales tax, deferred revenue, and contingent liabilities. The payroll module especially is where many small-business tools fall short.

**How to adapt this prompt:**

- *For your own project:* Payroll tax rates change yearly and vary by state. The tool should accept rates as parameters, not hardcode 2026 values.
- *For ChatGPT / Gemini:* Works as written.
- *For Claude Code:* The right tool. Payroll is the most error-prone module; thorough tests with multiple employees and edge cases are essential.
- *For a Claude Project:* Update spec.

**Connection to previous chapters:** Ch 8's audit log captures every payroll-cycle entry. Ch 7's special journals can include a payroll journal as a separate special journal.

**Preview of next chapter:** Chapter 13 adds long-term liabilities — bond pricing (present value of cash flows), effective-interest amortization, lease accounting under ASC 842, deferred tax. The most mathematically intensive module.


---

## AI Wayback Machine

**Robert N. Anthony** was Harvard Business School accounting professor who codified the modern framework for current liabilities and working capital.

**Run this:**

```
Who is Robert N. Anthony, and how does their work connect to current liabilities we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about their career or ideas.
```

→ Search **"Robert N. Anthony"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to apply Robert N. Anthony's ideas to a specific accounting question.
- Add a constraint: "Answer including criticisms or limits of Robert N. Anthony's framework."

What changes? What gets better? What gets worse?
