# Chapter 5 — Completing the Accounting Cycle

## 5.1 Opening: A second month begins

Mark Summers's October at Supreme Cleaners ends. He has the adjusted trial balance from Chapter 4. The financial statements for October are sitting on the printer. What happens to all those balances on November 1?

Some of them — Cash, Equipment, Accounts Receivable, Accumulated Depreciation, Wages Payable, Owner's Capital — should carry over. They describe the company's *position* on the date of the balance sheet, and that position doesn't reset just because the calendar turns. Cash on October 31 is the same Cash that exists on November 1.

Other balances — Service Revenue, Wages Expense, Depreciation Expense, Owner's Withdrawals — should *not* carry over. They describe the company's *performance during October*. If Mark's November Service Revenue starts at $3,100 (October's ending balance) instead of $0, his November income statement will look like the company earned $3,100 before doing any work. That's wrong. The income-statement and dividend accounts have to be reset to zero before the new period begins, and the cumulative effect of October's net income has to be moved into the equity section so Mark's books reflect that he's $250 better off than when he started.

The mechanism that does both of these things is *closing entries*. They are the last bookkeeping step of the accounting cycle. By the end of this chapter, you should be able to:

- Distinguish *temporary* accounts (revenues, expenses, withdrawals/dividends, Income Summary) from *permanent* accounts (assets, liabilities, equity capital).
- Prepare the four closing entries that zero out all temporary accounts at period-end and roll their cumulative effect into permanent equity.
- Prepare a *post-closing trial balance* — the report that confirms the closing process worked and that the company is ready for the next period.
- Prepare a *classified balance sheet* — a balance sheet organized by current vs. noncurrent and by asset/liability type — and use it to compute the *current ratio* as a basic measure of short-term liquidity.
- Walk through the full accounting cycle, from initial transaction analysis to closing entries, in the correct order.

You walk in with the adjusted trial balance from Chapter 4. You walk out with closed books, a post-closing trial balance, a classified balance sheet, and a working sense of the complete accounting cycle.

Why does it matter? Because every reporting period for every business that follows GAAP completes this same cycle, every time. Public companies do it quarterly; many private companies do it monthly. Bookkeeping software automates most of the mechanical steps, but the conceptual structure is what you need to know to interpret what the software is doing. A closing entry that fails to close a revenue account leaves last quarter's revenue mixed into this quarter's books. A balance sheet that isn't classified can't tell a banker whether the company can pay its bills. The cycle ends here, but the cycle has to actually *end* before the next one can begin cleanly.

## 5.2 Temporary and permanent accounts

Every account on the chart of accounts is either *temporary* or *permanent*. The distinction governs what happens to its balance at period-end.

*Permanent* accounts (also called *real* accounts) carry their balances forward indefinitely. They appear on the balance sheet — assets, liabilities, and the equity capital accounts (Owner's Capital, Common Stock, Retained Earnings). Their balances at the end of one period become their starting balances at the start of the next. Cash on December 31 is the same Cash on January 1.

*Temporary* accounts (also called *nominal* accounts) measure activity *during* a period and reset to zero at the end of each period. They appear on the income statement (revenues, expenses, gains, losses) plus the dividend or owner's withdrawals account. Their balances accumulate across the period and then get *closed* — zeroed out — before the next period begins. The cumulative effect of all those temporary-account balances doesn't disappear; it gets transferred into the permanent equity section so the balance sheet reflects the period's net result.

The reason for this design: the income statement is supposed to report performance *for a single period*. If revenues and expenses kept accumulating across multiple periods without resetting, every income statement after the first would show cumulative-since-inception figures rather than period-only figures, and comparisons across periods would be impossible. Closing entries are how the temporary accounts get reset.

A useful intermediary account in the closing process is *Income Summary* — a temporary account used only during closing to aggregate revenues and expenses before the net is moved to equity. Income Summary itself starts at zero, ends at zero, and exists only as a workspace.

## 5.3 The four closing entries

Closing entries happen in a fixed sequence at period-end, after the financial statements have been prepared.

**Closing entry 1: Close revenue accounts to Income Summary.**

Revenue accounts have credit balances. To close them, debit each revenue account for its full balance and credit Income Summary for the total. After this entry, every revenue account has a zero balance, and Income Summary carries a credit balance equal to total revenues for the period.

For Supreme Cleaners, with Service Revenue of $3,100 and Interest Revenue of $30 at October 31:

| Account | Debit | Credit |
|---|---|---|
| Service Revenue | $3,100 | |
| Interest Revenue | $30 | |
| Income Summary | | $3,130 |

**Closing entry 2: Close expense accounts to Income Summary.**

Expense accounts have debit balances. To close them, credit each expense account for its full balance and debit Income Summary for the total. After this entry, every expense account has a zero balance, and Income Summary's balance has been reduced by the total of expenses.

For Supreme Cleaners — assuming October expenses of Rent Expense $1,200, Wages Expense $1,750 ($1,500 paid plus $250 accrued), Insurance Expense $100, Supplies Expense $500, Depreciation Expense $100:

| Account | Debit | Credit |
|---|---|---|
| Income Summary | $3,650 | |
| Rent Expense | | $1,200 |
| Wages Expense | | $1,750 |
| Insurance Expense | | $100 |
| Supplies Expense | | $500 |
| Depreciation Expense | | $100 |

After closing entries 1 and 2, Income Summary carries a balance equal to net income (or net loss). For Supreme Cleaners: $3,130 credits − $3,650 debits = $520 debit balance. That means Supreme Cleaners had a net *loss* of $520 in October (this is a different scenario than Chapter 3's setup, which involved smaller expenses; we're using full October expenses including Chapter 4's adjustments now).

Wait — let's check that against the structure. If revenues are $3,130 and expenses are $3,650, expenses exceed revenues by $520. That's a net loss of $520. Income Summary, after both entries, should have a $520 debit balance — meaning the loss has accumulated as a debit (because expenses, debits, exceeded revenues, credits).

**Closing entry 3: Close Income Summary to the equity capital account.**

Move the net income or net loss from Income Summary into the permanent equity account. For a sole proprietorship, that's Owner's Capital. For a corporation, it's Retained Earnings.

For Supreme Cleaners with a $520 debit balance in Income Summary (a net loss):

| Account | Debit | Credit |
|---|---|---|
| Owner's Capital | $520 | |
| Income Summary | | $520 |

The debit to Owner's Capital reduces equity by the amount of the loss. Income Summary returns to zero. (If the result had been a net income — credit balance in Income Summary — the entry would reverse: Debit Income Summary, Credit Owner's Capital, increasing equity.)

**Closing entry 4: Close Owner's Withdrawals (or Dividends) to the equity capital account.**

Withdrawals or dividends are not expenses. They don't go through Income Summary. They reduce equity directly because they represent owner-distributions, not period costs. Close them straight to Owner's Capital (or Retained Earnings).

For Supreme Cleaners with Owner's Withdrawals of $500:

| Account | Debit | Credit |
|---|---|---|
| Owner's Capital | $500 | |
| Owner's Withdrawals | | $500 |

After all four closing entries, every revenue account, every expense account, the Income Summary account, and the Owner's Withdrawals account has a zero balance. Owner's Capital reflects the cumulative effect of investments, net income or loss, and withdrawals.

The four closing entries together implement a single accounting fact: equity changes during the period by exactly *(net income or loss) − withdrawals*. The mechanism makes that fact visible and auditable.

## 5.4 The post-closing trial balance and the complete cycle

After all closing entries are posted, the bookkeeper prepares one more trial balance: the *post-closing trial balance*. It lists every permanent account (asset, liability, equity capital) with its balance, in two columns. Total debits should equal total credits.

The post-closing trial balance has two structural features that distinguish it from the unadjusted and adjusted trial balances:

First, *no temporary accounts appear*. Revenue, expense, and withdrawal/dividend accounts have all been zeroed out and no longer have balances to report. The post-closing trial balance contains only assets, liabilities, and equity capital.

Second, *it confirms the closing process worked*. If total debits equal total credits *and* no temporary accounts have non-zero balances, the closing entries did their job. If a temporary account still has a balance, a closing entry was missed.

The post-closing trial balance is the bridge between one accounting period and the next. The balances in it become the opening balances for the next period.

This closes the accounting cycle, which in its complete form has nine steps:

1. Identify and analyze transactions
2. Journalize transactions in the general journal
3. Post journal entries to the general ledger
4. Prepare the *unadjusted* trial balance (Chapter 3 ends here)
5. Journalize and post adjusting entries
6. Prepare the *adjusted* trial balance (Chapter 4 ends here)
7. Prepare the financial statements (Chapter 5 introduces, later chapters detail)
8. Journalize and post closing entries
9. Prepare the *post-closing* trial balance (Chapter 5 ends here)

Some textbooks split or merge steps; the structure is the same. Steps 1–4 happen continuously throughout the period (modern systems automate them). Steps 5–9 happen at period-end. Then the cycle restarts at step 1 for the next period.

## 5.5 The classified balance sheet and current ratio

The balance sheet you produced in Chapter 2 was *unclassified* — assets and liabilities were listed without grouping. A *classified balance sheet* organizes assets and liabilities into subcategories that make the company's short-term and long-term position more readable. It's the form the financial statements actually take in real practice.

The standard classifications:

**Assets**
- *Current assets* — expected to be converted to cash, sold, or consumed within one year (or one operating cycle, if longer). Listed in approximate order of liquidity: Cash and cash equivalents; Short-term investments; Accounts receivable; Inventory; Prepaid expenses.
- *Long-term investments* — investments not expected to be liquidated within a year.
- *Property, plant, and equipment* (PP&E) — long-term tangible assets used in operations: Land, Buildings, Equipment, Vehicles. Listed at cost less accumulated depreciation (the *book value* or *net carrying value*).
- *Intangible assets* — long-term assets without physical substance: Patents, Copyrights, Trademarks, Goodwill.

**Liabilities**
- *Current liabilities* — due within a year (or operating cycle): Accounts payable; Wages payable; Short-term notes payable; Current portion of long-term debt; Unearned revenue (the portion to be earned within a year).
- *Long-term liabilities* — due more than a year out: Long-term notes payable; Mortgages payable; Bonds payable.

**Equity** continues with the same conventions as the unclassified balance sheet — Owner's Capital for a sole proprietorship; Common Stock + Retained Earnings (and possibly Additional Paid-in Capital) for a corporation.

The classification has direct analytical value. The first quick-read question a banker or analyst will ask of a balance sheet is: *can this company pay its short-term bills?* The metric that answers that question is the *current ratio*:

$$\text{Current ratio} = \frac{\text{Current assets}}{\text{Current liabilities}}$$

A current ratio above 1.0 means current assets exceed current liabilities — the company has enough short-term resources to cover its short-term obligations. A current ratio below 1.0 means the opposite — current obligations exceed current resources, a warning sign of potential liquidity trouble. A current ratio significantly above 2.0 or 3.0 might suggest the company is holding more current assets than it needs and might be deploying capital inefficiently. The "right" current ratio is industry-dependent — retailers running on thin margins often live with current ratios near 1.0; capital-intensive industries with long collection cycles often need higher ratios.

For Supreme Cleaners at October 31, with current assets (Cash $22,600 + Accounts Receivable $300 + Supplies $300 + Prepaid Insurance $1,100 + Interest Receivable $30 = $24,330) and current liabilities (Accounts Payable $800 + Wages Payable $250 = $1,050):

Current ratio = $24,330 / $1,050 = 23.2

Mark's company is in extreme short-term liquidity health, in part because Mark just contributed $20,000 of cash to launch the business and hasn't yet deployed most of it. As Supreme Cleaners grows and acquires more equipment and incurs more obligations, the current ratio will normalize to industry typicals.

The trade-off in the classified balance sheet: classification buys *fast readability* (a banker can compute current ratio in seconds) at the cost of *requiring judgment about classification* (some assets and liabilities sit ambiguously across the current/noncurrent line). The judgment is bounded by GAAP guidance, but real cases can require thought.

## 5.6 Exercises

### Warm-up

1. **Classify each as a temporary or permanent account:** Cash, Service Revenue, Wages Expense, Owner's Capital, Accounts Payable, Owner's Withdrawals, Equipment, Income Summary, Accumulated Depreciation, Interest Revenue.

2. **State the four closing entries in order, in plain English** (you don't need to write them out as journal entries — just describe what each one does).

3. **Define the current ratio and state the formula.** What does a current ratio of 0.7 suggest about a company's short-term position?

### Application

4. **A company's adjusted trial balance shows: Service Revenue $40,000; Sales Revenue $5,000; Rent Expense $8,000; Wages Expense $15,000; Supplies Expense $2,000; Depreciation Expense $1,500; Owner's Withdrawals $3,000.** Prepare the four closing entries.

5. **A company has the following at year-end: Cash $25,000; Accounts Receivable $12,000; Inventory $40,000; Equipment $80,000; Accumulated Depreciation $20,000; Land $50,000; Accounts Payable $18,000; Long-term Notes Payable $40,000; Owner's Capital $129,000.** Prepare a classified balance sheet. Compute the current ratio.

6. **Walk through all nine steps of the accounting cycle in order** for a single hypothetical transaction: a customer pays $500 cash for services performed today.

### Synthesis

7. **A bookkeeper accidentally closes Supplies (an asset) into Income Summary along with the expenses.** Describe the consequences for the post-closing trial balance, the next period's opening balance for Supplies, and the income statement of the period during which the error occurred.

8. **Two companies in the same industry both report net income of $50,000 for the year.** Company A has a current ratio of 1.2; Company B has a current ratio of 3.5. Discuss what each ratio suggests, and propose at least three additional pieces of information you'd want before drawing a final conclusion about which company is in better financial health.

### Challenge

9. **Income Summary is a temporary account that exists only during closing.** Why bother with it at all — couldn't revenues be closed directly to Owner's Capital and expenses also closed directly, in two entries instead of three? Propose a structural reason why the Income Summary intermediary improves auditability or readability of the closing process.

10. **A retailer chooses a fiscal year ending January 31.** Sketch how the closing process at January 31 would feel different, operationally, from a January 31 closing in the middle of a calendar-year company. What real-world advantages does the post-holiday close offer beyond the inventory-counting one mentioned in Chapter 4?

## 5.7 Chapter summary

You walked into this chapter with an adjusted trial balance and a set of financial statements. You walk out with closed books and the company ready for the next period.

Closing entries take all the temporary accounts — revenues, expenses, owner's withdrawals (or dividends) — and reset them to zero, transferring their cumulative effect into permanent equity. The four entries: (1) close revenues to Income Summary; (2) close expenses to Income Summary; (3) close Income Summary's balance (net income or net loss) to Owner's Capital or Retained Earnings; (4) close Owner's Withdrawals or Dividends directly to Owner's Capital or Retained Earnings.

The post-closing trial balance is the checkpoint that confirms the closing process worked. It contains only permanent accounts and reflects the company's position at the start of the next period.

The classified balance sheet — current vs. noncurrent assets and liabilities, organized by category — is the form a balance sheet actually takes in practice. It enables the current ratio (current assets divided by current liabilities), the most basic measure of short-term liquidity.

The single most important idea to carry forward: temporary accounts are *temporary* by design. They measure activity during a period; their balances must reset before the next period or every income statement becomes incomprehensible. The closing process is not optional; it is structurally required for the financial statements to mean what they're supposed to mean.

The common mistake to watch for: confusing the order of the closing entries. Income Summary serves as the holding account for the net income/loss calculation; it must receive both revenues and expenses *before* its balance can be moved to equity. Closing dividends or withdrawals goes around Income Summary entirely — these are owner distributions, not period costs.

## 5.8 A walk through the complete cycle

To consolidate the nine-step cycle into a single mental picture, follow one ordinary transaction through every step it touches.

A customer brings a load of laundry into Supreme Cleaners on November 3 and pays $40 cash on the spot. *Step 1*: identify and analyze. Two accounts move — Cash (asset) up, Service Revenue (revenue) up. Debits equal credits at $40. *Step 2*: journalize. Debit Cash $40, Credit Service Revenue $40, dated November 3, with a brief description ("dry-cleaning service for cash"). *Step 3*: post to ledger. The Cash T-account picks up a $40 debit; the Service Revenue T-account picks up a $40 credit. Both running balances update.

The transaction sits in the books unchanged through the rest of November. *Step 4* — preparing the unadjusted trial balance — happens at November 30 along with every other November transaction. *Step 5*: adjusting entries close out any deferrals or accruals at November 30 (depreciation, accrued wages, etc.) using the four-pattern rules from Chapter 4. *Step 6*: the adjusted trial balance is prepared, integrating those adjustments. *Step 7*: the income statement, statement of owner's equity, balance sheet, and statement of cash flows are produced from the adjusted trial balance.

*Step 8*: closing entries. The Service Revenue account, which by the end of November might carry a balance of, say, $4,200 (including this $40 plus all of November's other service revenue), gets closed to Income Summary along with all other revenues. Then expenses get closed to Income Summary. Then Income Summary's balance gets closed to Owner's Capital. Then Owner's Withdrawals get closed to Owner's Capital. *Step 9*: the post-closing trial balance is prepared. The Service Revenue account now shows $0; the Cash account still shows whatever balance has accumulated through November (less, of course, all the cash payments out across the period); Owner's Capital reflects the cumulative effect of October and November combined.

December 1 arrives. The Service Revenue account is at $0 again, ready to start measuring December performance. The Cash account carries forward. The cycle restarts at step 1 with whatever transactions December brings.

This is the rhythm of every accounting period in every accrual-basis business. The complexity of a Fortune 500 close — with thousands of accounts, hundreds of adjusting entries, multiple subsidiaries to consolidate — is not different in *kind* from Supreme Cleaners' month-end close. It is different in *scale*. The structural cycle is the same.

A subtle but consequential point: the closing process is one of the strongest internal-control features of double-entry bookkeeping. If a temporary account fails to close — if Service Revenue still shows a balance after closing entry 1 should have zeroed it — the post-closing trial balance flags it immediately. If the closing entry to Owner's Capital is wrong, the balance sheet's equity section will be wrong, and the next period's books will start from a wrong opening figure that propagates forward. Catching closing errors early is structurally easier than catching them after another period of activity has piled on top. The post-closing trial balance is not redundant; it is the last line of defense before next period's transactions start accumulating against potentially wrong opening balances.

The classified balance sheet, similarly, is more than a presentation choice. It encodes a hard distinction — current vs. noncurrent — that financial analysis depends on. Bankers underwriting short-term lines of credit care almost exclusively about current assets and current liabilities. Long-term lenders care about long-term debt service and the sustainability of long-term assets. Equity investors care about the residual claim and how it changes over time. The classification organizes the balance sheet into the sections each reader is going to focus on. An unclassified balance sheet forces every reader to do the classification themselves, which wastes time and invites errors of judgment.

## 5.9 Connections forward

Chapter 6 starts looking at *merchandising businesses* — retailers and wholesalers that buy and resell goods. The accounting cycle stays the same, but new accounts and new transactions enter: Inventory, Cost of Goods Sold, Sales Returns and Allowances, Purchase Discounts. The income statement gets a new top line — Gross Profit — that wasn't part of Mark Summers's service business. By the end of Chapter 6, you'll be able to handle the most common business type by revenue volume in the U.S. economy: the retailer or wholesaler that buys inventory and sells it on.
---

## LLM Exercise — Chapter 5: Completing the Accounting Cycle (AI Bookkeeping Tool Project)

**Project:** AI Bookkeeping Tool.
**What you're building this chapter:** closing entries, the post-closing trial balance, and the classified balance sheet. The tool can now complete a full accounting period.
**Tool:** **Claude Code.**

---

**The Prompt:**

```
I'm in Chapter 5 of building my AI Bookkeeping Tool. The tool now
handles transactions, adjustments, and the adjusted trial balance.
This chapter taught: temporary vs. permanent accounts (temporary —
revenues, expenses, dividends/drawings, income summary; permanent
— everything on the balance sheet); the four closing entries:
   1. Close revenues to Income Summary (debit revenue accounts,
      credit Income Summary).
   2. Close expenses to Income Summary (debit Income Summary,
      credit expense accounts).
   3. Close Income Summary to Owner's Capital/Retained Earnings
      (transfers net income or loss).
   4. Close Dividends or Drawings to Owner's Capital/Retained
      Earnings.
The post-closing trial balance contains only permanent accounts.
The classified balance sheet groups assets and liabilities into
current vs. non-current categories.
The current ratio = Current Assets ÷ Current Liabilities.

Extend the tool. Produce four outputs.

1. **A close_period function.** Given a period end date, this
   function:
   - Identifies all temporary accounts (revenues, expenses,
     dividends/drawings).
   - Generates the four closing entries automatically.
   - Posts them to the ledger.
   - Validates that all temporary accounts have zero balances
     after closing.

2. **A post-closing-trial-balance generator.** A function/sheet
   that produces the trial balance using only permanent accounts.
   It should match the balance sheet (Assets = Liabilities + Equity)
   and contain no temporary accounts.

3. **A classified-balance-sheet generator.** A function/sheet that:
   - Groups assets into Current (cash, AR, inventory, prepaid,
     short-term investments) and Non-current (PP&E, intangibles,
     long-term investments).
   - Groups liabilities into Current (AP, short-term debt, accrued
     expenses, unearned revenue) and Non-current (long-term debt,
     deferred tax).
   - Computes Total Current Assets, Total Non-current Assets, Total
     Current Liabilities, Total Non-current Liabilities, and Equity.
   - Computes and displays the current ratio.
   The function needs a way to flag accounts as current or non-
   current — either by chart-of-accounts metadata or by a
   convention (e.g., account numbers 1000–1499 are current assets).

4. **A complete-cycle test.** A test scenario that:
   - Starts with a blank set of books for a fictional business.
   - Records 15–20 transactions over a one-month period
     (revenues, expenses, asset acquisitions, liability creation).
   - Records 3–5 adjusting entries at month-end.
   - Closes the period.
   - Produces the four financial statements.
   - Verifies the income statement net income flows to equity, and
     equity flows to the balance sheet.
   - The classified balance sheet balances.

Update the spec doc.
```

---

**What this produces:** A complete-cycle implementation. The tool can now process a month or year of transactions and produce closing-period financial statements. This is the first chapter where the tool can plausibly run a small business's books end-to-end.

**How to adapt this prompt:**

- *For your own project:* If your business is a corporation, the closing-to-Capital becomes closing-to-Retained-Earnings, and dividends close there instead of drawings. The classified balance sheet structure is identical.
- *For ChatGPT / Gemini:* Works as written.
- *For Claude Code:* The right tool. The complete-cycle test is the chapter's biggest payoff — when it passes, the tool is genuinely operational.
- *For a Claude Project:* Update spec.

**Connection to previous chapters:** Chs 3 + 4 + 5 together form the accounting cycle. The tool is now an end-to-end bookkeeper for service businesses.

**Preview of next chapter:** Chapter 6 adds merchandising — inventory transactions in perpetual and periodic systems, COGS, purchase and sales discounts, the multi-step income statement. The tool's income statement gets more sophisticated.


---

## AI Wayback Machine

**William Cooper** was co-developed Data Envelopment Analysis — the framework for evaluating organizational efficiency in accounting and operations.

**Run this:**

```
Who is William Cooper, and how does their work connect to accounting cycle we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about their career or ideas.
```

→ Search **"William Cooper"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to apply William Cooper's ideas to a specific accounting question.
- Add a constraint: "Answer including criticisms or limits of William Cooper's framework."

What changes? What gets better? What gets worse?
