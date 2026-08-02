# MBA Accounting — Video Ideas
<!-- Scouted 2026-07-09 from 16 narrative chapters -->

---

## Candidate 01 — Profitable and Broke: Why Your Income Statement Is Lying to You
- Source: `mba-accounting/chapters/16-statement-of-cash-flows.md`, `mba-accounting/chapters/02-introduction-to-financial-statements.md`, `mba-accounting/chapters/04-the-adjustment-process.md`
- Topic: ACCOUNTING
- Hook: A company reports $50 million net income and then files for emergency financing the next morning — how?
- Key case: A hypothetical retailer earns $40M net income but operating cash flow is only $20M while inventory balloons $35M and capex is $80M — the cash balance falls $45M in a profitable year.
- The Question: If net income is positive, why is cash shrinking — and which statement tells you before it's too late?
- Core idea: Accrual accounting records revenue when earned and expenses when incurred, not when cash moves. The cash flow statement reconciles accrual-basis net income to actual cash by adding back non-cash charges (like depreciation) and adjusting for working-capital changes, revealing the gap between reported profit and real liquidity.
- Visual object: A side-by-side split screen — Income Statement showing $40M profit on the left, Cash Flow Statement showing the adjustments that reduce it to $20M operating CF on the right — with arrows tracing each adjustment (depreciation add-back, inventory increase subtraction, AP decrease subtraction).
- Manim move: transform (net income line morphs into cash from operations through a cascade of labeled adjustments, each item animating in as a +/- delta)
- Example seed: The hypothetical retailer from Chapter 16: net income $40M, depreciation +$25M, stock comp +$10M, receivables −$12M, inventory −$35M, AP −$8M = operating CF $20M. Capex $80M means free cash flow is deeply negative. The company issues $50M of debt to stay afloat while paying $35M in dividends and buybacks. Result: cash falls $45M in a "profitable" year.
- Length band: 3–5 min
- Still lanes: c2v (formula bars animating), raster (real retailer earnings-release screenshot as intro hook, fair-use crop)
- Prerequisites: Basic understanding that companies can earn revenue on credit; familiarity with four financial statements at a conceptual level
- Exclusions: Tax implications of accrual vs. cash basis, IFRS interest-classification difference, direct vs. indirect method details
- Score: 10/10

---

## Candidate 02 — Depreciation Doesn't Cost You a Dime (This Year)
- Source: `mba-accounting/chapters/11-long-term-assets.md`, `mba-accounting/chapters/16-statement-of-cash-flows.md`, `mba-accounting/chapters/04-the-adjustment-process.md`
- Topic: ACCOUNTING
- Hook: A company's income statement shows $5,100 of depreciation expense this year — but not a single dollar left the bank account.
- Key case: A $40,700 delivery truck is depreciated $5,100 per year for 7 years under straight-line. Each year the income statement takes the hit; the cash flow statement adds it straight back in the operating section. The truck's $40,700 cash outflow happened only once — at purchase — and shows in investing activities, not operating.
- The Question: If depreciation is an expense that reduces net income, why does the cash flow statement add it back — and what does that reveal about how capital-intensive businesses actually generate cash?
- Core idea: Depreciation allocates the cost of a long-term asset across the years it benefits. The cash already left when the asset was purchased; depreciation is a non-cash accounting entry that matches cost to revenue over time. Adding depreciation back in the indirect-method operating section converts accrual income to cash income — which is why capital-intensive companies (utilities, manufacturers) routinely show operating cash flow far above net income.
- Visual object: A balance scale — on the left pan, the $40,700 cash outflow at purchase (investing section, one-time); on the right, seven years of $5,100 depreciation expense bars stacking up on the income statement, with each bar mirrored by an equal add-back arrow in the cash flow operating section.
- Manim move: accumulate (annual depreciation bars build up year by year on the income statement side; simultaneously a matching "add-back" bar stacks on the cash flow side, demonstrating the neutralization)
- Example seed: Supreme Cleaners' commercial press: bought for $12,000, estimated useful life 10 years, salvage $0. Straight-line depreciation = $100/month adjusting entry (Debit Depreciation Expense, Credit Accumulated Depreciation). Net income falls $100; cash unchanged. At year-end, cash from operations adds back $1,200. Compare: a utility with $2B net income and $3B depreciation — operating CF of $5B is the real story.
- Length band: 2–3 min
- Still lanes: c2v (T-account diagram, cash flow statement excerpt), geo (timeline arrow showing cash outflow at t=0 vs. depreciation spread)
- Prerequisites: Know what an income statement and balance sheet are; basic concept of expenses reducing net income
- Exclusions: Accelerated vs. straight-line comparison, tax depreciation (MACRS), impairment, intangible amortization
- Score: 10/10

---

## Candidate 03 — The Same Goods, Three Different Profits: FIFO vs. LIFO
- Source: `mba-accounting/chapters/10-inventory.md`
- Topic: ACCOUNTING
- Hook: Three identical widgets. Three identical sale prices. Three completely different profits — depending on which number you pick.
- Key case: A wholesaler buys 3 widgets: January at $10, June at $12, October at $14. Sells 2 in November for $25 each. FIFO COGS = $22, gross profit = $28. LIFO COGS = $26, gross profit = $24. Weighted average COGS = $24, gross profit = $26. Same physical sale, a $4 difference in reported profit — and the same difference in inventory on the balance sheet.
- The Question: When the goods are physically identical and the sale price is the same, how can the choice of an accounting method change reported profit by $4 per unit — and why does the IRS care?
- Core idea: Cost-flow assumptions (FIFO, LIFO, weighted average) don't describe which physical unit was sold — they describe which *cost layer* is matched to the sale. In a rising-price environment FIFO maximizes reported profit (older, lower costs go to COGS) while LIFO minimizes it (recent, higher costs go to COGS) and thus minimizes taxable income. The IRS LIFO conformity rule forces companies to use the same method for tax and financial reporting, preventing cherry-picking.
- Visual object: A single shelf of three labeled widget boxes (Jan $10, Jun $12, Oct $14). A sale arrow pulls 2 boxes off the shelf; three animated versions of the shelf show which boxes are removed under each method, with the resulting COGS and ending inventory highlighted below each version.
- Manim move: split (one shelf morphs into three parallel versions — FIFO pulls from left, LIFO pulls from right, weighted average uses blended cost — with profit readout animating under each)
- Example seed: Exact numbers from Chapter 10: Jan 1 unit at $10, Jun 1 at $12, Oct 1 at $14. 2 units sold at $25 each = $50 revenue. FIFO: COGS $22, GP $28, ending inventory $14. LIFO: COGS $26, GP $24, ending inventory $10. Weighted average: COGS $24, GP $26, ending inventory $12. Note IFRS bans LIFO entirely.
- Length band: 3–5 min
- Still lanes: geo (three-column comparison table), c2v (shelf/cost-layer diagram)
- Prerequisites: Know what COGS and gross profit are; understand a merchandiser buys and resells goods
- Exclusions: Periodic vs. perpetual LIFO differences, LIFO reserve disclosure mechanics, inventory write-downs (LCNRV), specific identification
- Score: 10/10

---

## Candidate 04 — The Equation That Can Never Break: Assets = Liabilities + Equity
- Source: `mba-accounting/chapters/03-analyzing-and-recording-transactions.md`, `mba-accounting/chapters/02-introduction-to-financial-statements.md`
- Topic: ACCOUNTING
- Hook: Every transaction in every business on earth, from a $2 coffee sale to a billion-dollar acquisition, has to keep this one equation balanced — and it never fails.
- Key case: Mark Summers opens Supreme Cleaners with three founding transactions: (1) contributes $20,000 cash → Cash +$20,000, Capital +$20,000; (2) borrows $15,000 → Cash +$15,000, Notes Payable +$15,000; (3) buys press for $12,000 cash → Equipment +$12,000, Cash −$12,000. After each transaction the equation is checked live. After 10 transactions the unadjusted trial balance totals $38,900 on both sides.
- The Question: Why does every transaction have to touch at least two accounts — and how does double-entry bookkeeping guarantee the balance sheet can never go out of balance?
- Core idea: Assets are claims — either by creditors (liabilities) or by owners (equity). Every transaction either adds to one side and adds equally to the other, or shifts within one side. Double-entry records each transaction as equal debits and credits, mechanically enforcing the equation with every entry. The trial balance is the period-end proof that the system hasn't broken.
- Visual object: A live balance scale — left pan labeled "Assets", right pan labeled "Liabilities + Equity". Each of Mark's transactions adds weights to both sides simultaneously, keeping the scale level. A final shot shows the full trial balance with matching totals.
- Manim move: accumulate (weights drop onto both pans of the scale with each transaction, scale stays level; at the end all 10 transaction-weights are stacked on both sides in balance)
- Example seed: Supreme Cleaners October transactions from Chapter 3: contributions, bank loan, press purchase, supplies on account, rent, cash revenue, credit revenue, wages, collection, withdrawal. Trial balance: debit total $38,900 = credit total $38,900.
- Length band: 2–3 min
- Still lanes: geo (balance scale, T-account layout), c2v (trial balance table)
- Prerequisites: Basic concept of a business having assets; awareness that businesses borrow and invest
- Exclusions: Adjusting entries, closing entries, specific debit/credit rules for each account type in depth, chart of accounts structure
- Score: 9/10

---

## Candidate 05 — Why a Bond With a 5% Rate Sells for Less Than Face Value
- Source: `mba-accounting/chapters/13-long-term-liabilities.md`
- Topic: ACCOUNTING
- Hook: A company issues a bond promising 5% interest — and investors pay less than the stated $100,000 because rates are 6%. How can a promise to pay more than you borrowed be worth less?
- Key case: $100,000 face-value bond, 5% stated, 10 years, issued when market rates are 6%. Issue price = PV of $5,000 annual coupons at 6% ($36,800) + PV of $100,000 principal at 6% ($55,840) = $92,640. The $7,360 discount is recorded as Discount on Bonds Payable (contra-liability) and amortized over 10 years using the effective-interest method — Year 1 interest expense is $5,558 (carrying value × 6%), cash paid is only $5,000, the $558 difference reduces the discount.
- The Question: When market interest rates rise above a bond's stated rate, why does the bond issue at a discount — and how does the effective-interest method make the income statement show the true cost of borrowing?
- Core idea: A bond's price is the present value of its future cash flows discounted at the current market rate. If market rates exceed the coupon, investors will only pay less than face because the lower coupon stream, discounted at the higher market rate, equals less than face. The effective-interest method amortizes the discount by computing interest expense on the carrying value (not face), making the reported interest cost match the economic cost of borrowing.
- Visual object: A present-value timeline — 10 year-marks on a horizontal axis, $5,000 coupon arrows dropping at each mark, $100,000 arrow at the end. A discount-rate shrinking lens collapses each future cash flow to its present value. A running total bar at t=0 shows the sum landing at $92,640, not $100,000.
- Manim move: collapse (future cash-flow arrows fold back to t=0 through a discount factor lens, each one visibly shrinking as it collapses to its PV; final bar shows the sum)
- Example seed: $100,000 bond, 5% coupon, 10-year, market 6%. Issue entry: Cash $92,640, Discount on Bonds Payable $7,360, Bonds Payable $100,000. Year 1: Interest Expense $5,558 (= $92,640 × 6%), Cash $5,000, Discount reduced $558. Year 2: Interest Expense $5,592 (= $93,198 × 6%). Pattern continues until carrying value reaches $100,000 at maturity.
- Length band: 3–5 min
- Still lanes: geo (PV timeline with labeled arrows), c2v (amortization-table excerpt with carrying value column)
- Prerequisites: Understand what a loan is; know that interest rates and bond prices move in opposite directions (conceptually); basic algebra
- Exclusions: Premium bonds, early extinguishment, lease accounting under ASC 842, deferred tax liabilities, sinking funds
- Score: 9/10

---

## Candidate 06 — How Walmart Gets Paid Before It Pays Its Suppliers
- Source: `mba-accounting/chapters/12-current-liabilities.md`, `mba-accounting/chapters/09-accounting-for-receivables.md`, `mba-accounting/chapters/10-inventory.md`
- Topic: ACCOUNTING
- Hook: Walmart has a negative cash conversion cycle — customers pay Walmart before Walmart pays its suppliers. That means Walmart is running its entire retail operation on other people's money.
- Key case: Cash conversion cycle = Days' Sales in Inventory (DSI) + Days' Sales Outstanding (DSO) − Days' Payables Outstanding (DPO). A company with DSI 30, DSO 25, DPO 50 has CCC = 30 + 25 − 50 = 5 days. Walmart: DSI ~40 days (fast inventory turn), DSO ~4 days (mostly cash/card sales), DPO ~45–50 days (leverage over suppliers). CCC approaches zero or negative. Amazon's negative CCC means customers pay immediately, then Amazon holds the cash for weeks before remitting to marketplace sellers.
- The Question: How does a retailer end up financing its own growth from supplier float rather than from bank debt or equity raises — and what does accounts payable have to do with it?
- Core idea: The cash conversion cycle measures how long a dollar invested in inventory takes to return as cash. Companies with market power over suppliers can extend payables (DPO) while collecting from customers immediately (low DSO) and turning inventory fast (low DSI). The result is a negative CCC — a structural working-capital advantage that funds growth without external financing.
- Visual object: A circular flow diagram — Inventory → Sale → Cash → Pay Suppliers. The three arc-segments are labeled DSI, DSO, DPO with length proportional to days. For a standard company the circle is large and mostly DSI+DSO; for Walmart/Amazon the DPO arc extends past the DSI+DSO arc, showing the negative CCC as the overlap.
- Manim move: trace (the cash conversion cycle circle animates as a clock; arc segments grow proportionally; the DPO arc extends past the zero point for Walmart, showing cash received before payment is due)
- Example seed: Two companies in the same industry. Company A: DSI 60, DSO 45, DPO 30 → CCC = 75 days; $1M invested in inventory is tied up 75 days. Company B (a large retailer): DSI 30, DSO 5, DPO 50 → CCC = −15 days; Company B has the customer's cash sitting in its account for 15 days before it even pays its supplier. Company B funds growth with supplier float, not debt.
- Length band: 3–5 min
- Still lanes: geo (circular flow / arc diagram), c2v (CCC formula with labeled components), raster (real retailer annual-report working-capital table, fair-use crop)
- Prerequisites: Know what accounts receivable, inventory, and accounts payable are; understand that businesses buy and sell on credit terms
- Exclusions: Factoring, detailed DSO/DPO calculation mechanics, just-in-time inventory philosophy, supply-chain risk implications
- Score: 9/10

---

## Candidate 07 — The Fraud Triangle: Why Your Honest Employee Is the Biggest Risk
- Source: `mba-accounting/chapters/08-fraud-internal-controls-and-cash.md`
- Topic: ACCOUNTING
- Hook: Most occupational fraud is committed by employees who never stole before — and wouldn't steal from an employer with better controls.
- Key case: A bookkeeper at a small business handles cash receipts, records cash transactions, AND reconciles the bank statement. That's all three legs of fraud in one person: opportunity created by access, no oversight, and a rationalization ("they don't pay me enough"). The bank reconciliation — the one control that would catch the theft — is prepared by the thief. Historical parallel: Al Capone's ledger entries caught him when no murder witness would testify.
- The Question: If a person is under financial pressure and convinces themselves "I'll pay it back," what is the only thing that actually prevents fraud — and why can't you talk or hire your way around it?
- Core idea: The fraud triangle has three legs: pressure (private financial stress), opportunity (access + lack of oversight), and rationalization (the internal story that makes it feel acceptable). Companies cannot see or control pressure and rationalization — they are internal to the employee. Opportunity is structural and CAN be removed through segregation of duties, mandatory vacations, and external review. Removing opportunity prevents fraud even when the other two legs are present.
- Visual object: An equilateral triangle with the three legs labeled Pressure, Opportunity, Rationalization. A scissors graphic cuts only the Opportunity leg — the other two are labeled "invisible to employer." The resulting broken triangle collapses. A second frame shows a bank reconciliation being prepared by the same person who handles cash — the Opportunity leg glows red.
- Manim move: split (the fraud triangle appears complete; scissors animate to cut the Opportunity side only; the triangle destabilizes and collapses; a new diagram shows segregated duties as three separate circles with no overlap)
- Example seed: One-bookkeeper small business: opens mail (cash), records receipts, reconciles bank. Controls that work despite small headcount: (1) bonding the bookkeeper; (2) mandatory two-week continuous vacation; (3) quarterly CPA review of bank reconciliations. Worked historical case: Chapter 1's Capone — ledgers kept by his organization were read by federal accountants even when murder witnesses were silenced.
- Length band: 2–3 min
- Still lanes: geo (fraud triangle diagram), c2v (bank reconciliation format with the bookkeeper-controlled fields highlighted)
- Prerequisites: Know what a bank account and bookkeeper are; no prior accounting required
- Exclusions: COSO framework five-component detail, SOX Section 302/404 legal requirements, PCAOB audit oversight mechanics, petty cash imprest fund
- Score: 9/10

---

## Candidate 08 — The Hidden $1,700 Your Employer Pays on Top of Your Salary
- Source: `mba-accounting/chapters/12-current-liabilities.md`
- Topic: ACCOUNTING
- Hook: An employee earning $5,000 gross takes home $3,267 — but the company's actual cost is even higher than $5,000 because of taxes the employee never sees.
- Key case: $5,000 gross wages. Employee withholdings: federal income tax $750, state $200, FICA-SS $310, FICA-Medicare $72.50, health premium $150, 401(k) $250 → net pay $3,267.50. Then the company pays employer's FICA match (SS $310 + Medicare $72.50), FUTA, SUTA. True cost to employer: roughly $5,700–$5,800 for a $5,000 stated salary, and $3,267 is what the employee actually receives. Two separate journal entries — one for the employee side, one for the employer obligations — each creating multiple distinct payable accounts.
- The Question: When an employee earns $5,000 in gross wages, how many separate parties does the company owe money to — and why does the payroll journal entry require seven credit lines?
- Core idea: Payroll converts one gross-wage debit into a cascade of liabilities: the employee (net pay), the IRS (federal income tax withheld + employee FICA + employer FICA), the state (state income tax withheld + SUTA), the insurance carrier, the 401(k) administrator. The employer is a tax-collection and benefits-administration agent for all of these parties simultaneously. The fully-loaded cost of an employee is typically 1.25–1.4× stated salary.
- Visual object: A single $5,000 gross-wages bar that splits into a cascade of colored wedges — each wedge labeled with the payee (employee net pay, IRS-federal, IRS-FICA, state, insurance, 401k) with dollar amounts. Below the employee wedge, a second bar shows the employer's own FICA match and FUTA/SUTA adding additional cost above the $5,000.
- Manim move: spread (the $5,000 gross-wages bar fans out horizontally into labeled wedges; the employer-cost additions appear below as additional segments extending the total beyond $5,000)
- Example seed: Chapter 12 worked example: $5,000 gross → employee-side journal entry (seven lines). Employer-side second entry: Debit Payroll Tax Expense, Credit FICA-SS $310, FICA-Medicare $72.50, FUTA ~$30 (estimated), SUTA varies. Total employer cost ~$5,780. The payables created are remitted at different deadlines: federal tax and FICA often bi-weekly, FUTA quarterly, insurance monthly.
- Length band: 2–3 min
- Still lanes: c2v (stacked payroll journal entries, color-coded by payee), geo (cost waterfall bar chart)
- Prerequisites: Know what gross vs. net pay means; no prior accounting required
- Exclusions: Defined-benefit pension liabilities, stock-based compensation, contractor vs. employee distinction, multi-state payroll complications
- Score: 8/10
