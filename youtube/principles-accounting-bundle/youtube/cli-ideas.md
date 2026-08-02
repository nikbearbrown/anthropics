# Principles of Accounting Bundle — CLI Video Ideas ("X with Claude")

## Candidate 01 — "Analyze Cash Flow Quality with Claude: When Net Income Lies"
- Source: principles-accounting-bundle/chapters/16-statement-of-cash-flows.md
- Lane: BUILD (Claude Code)
- Hook: A company can show positive net income while hemorrhaging cash — and the Statement of Cash Flows reveals it. The gap between net income and operating cash flow is the single most reliable signal of earnings manipulation.
- The artifact: A bar chart comparing net income vs. operating cash flow for five real S&P 500 companies over 3 years (or a synthetic dataset of 10 companies with varying "cash conversion quality"). Companies are ranked by cash conversion ratio (OCF/Net Income); companies where OCF < Net Income are flagged in red. A scatter plot of OCF vs. Net Income shows the ideal 45° line, with outliers labeled.
- Prompt seed: `claude "Write Python that analyzes cash flow quality for 10 companies. Compute cash conversion ratio = Operating_Cash_Flow / Net_Income for each. Flag companies where ratio < 0.8 (earnings quality concern) or ratio > 2.0 (potential working capital release). Plot: (1) bar chart of Net Income vs OCF side by side for each company, (2) scatter plot of OCF vs Net Income with a 45-degree reference line. Use this synthetic dataset: [provide 10 rows of (company, net_income, OCF, year)]."`
- Read / check: Code: verify cash conversion ratio formula; verify flagging logic correctly identifies low-quality and high-quality earners; verify the 45° line passes through origin. Output: companies with OCF << Net Income should be clearly red; the scatter outliers should be annotated with company names.
- Human supplies: Real S&P 500 cash flow data from annual reports (SEC EDGAR, Compustat, or Yahoo Finance) for the most compelling version. Fully synthetic dataset with realistic parameters is acceptable for illustration — the human must decide which is appropriate.
- Output medium: Manim — animate the bar chart building up company by company, sorted by cash conversion ratio; annotate the red-flag companies as they appear.
- The change: Add the "accruals ratio" = (Net Income − OCF) / Total Assets and show that companies with high accruals ratios tend to have lower future returns (cite Richardson et al. 2005 if available in synthesis).
- Teardown angle: The indirect method of the cash flow statement starts from net income and then adjusts back to cash — which means every adjustment is a place where accounting discretion can diverge from economic reality. High accruals is the oldest trick in earnings management.
- Exclusions: Specific fraud case studies; direct method cash flow presentation; SEC enforcement patterns.
- Score: 9/10

## Candidate 02 — "Build the Accounting Cycle with Claude: Transaction to Financial Statements Pipeline"
- Source: principles-accounting-bundle/chapters/05-completing-the-accounting-cycle.md
- Lane: BUILD (Claude Code)
- Hook: Ten journal entries, a trial balance, four closing entries, and you have financial statements. The accounting cycle is an algorithm — and Claude can code the full pipeline from a list of transactions to a classified balance sheet.
- The artifact: A pipeline visualization showing 10 input transactions (e.g., sold $5,000 services, paid $1,200 rent, received $3,000 cash for future service) processed through: (1) journal entries → (2) T-accounts → (3) unadjusted trial balance → (4) adjusting entries → (5) adjusted trial balance → (6) four closing entries → (7) post-closing trial balance → (8) classified balance sheet + income statement. Each stage shown as a table.
- Prompt seed: `claude "Write Python that implements a complete accounting cycle for a small business. Input: 10 transactions as (date, account_debit, amount_debit, account_credit, amount_credit) tuples. Process: (1) Post to T-accounts (dict of account: balance), (2) Print trial balance (verify debits=credits), (3) Apply 3 adjusting entries (depreciation, prepaid expense, accrued revenue), (4) Print adjusted trial balance, (5) Apply 4 closing entries (close Revenue, Expense, Dividends to Retained Earnings), (6) Print classified balance sheet."`
- Read / check: Code: verify trial balance debits = credits at each stage; verify Revenue and Expense accounts zero out after closing; verify Retained Earnings changes by Net Income. Output: the classified balance sheet should show Assets = Liabilities + Equity (balance equation holds).
- Human supplies: Nothing — fully synthetic (a set of 10 representative transactions is provided in the prompt seed; the human may customize the transaction set to match a specific business scenario).
- Output medium: Manim — animate each stage of the pipeline as a table appearing sequentially, with amounts flowing (arrows) from journal entries to T-accounts to trial balance to financial statements.
- The change: Introduce an error (debit and credit reversed on one transaction) and show how the trial balance catches it (debits ≠ credits), then trace the fix.
- Teardown angle: The accounting cycle is a reconciliation machine — it converts economic events into financial position, with a built-in error-detection step (the trial balance) at every stage. The closing entries exist to reset the system for the next period.
- Exclusions: GAAP vs. IFRS differences; consolidation of subsidiaries; audit sampling procedures.
- Score: 9/10

## Candidate 03 — "Reconstruct Cash Flow from Accrual Data with Claude: The Indirect Method"
- Source: principles-accounting-bundle/chapters/16-statement-of-cash-flows.md
- Lane: BUILD (Claude Code)
- Hook: The indirect method starts from net income — which is based on accrual accounting — and adds back non-cash charges and working capital changes to arrive at cash from operations. It's a reverse-engineering problem: undo the accounting to find the cash.
- The artifact: A reconciliation waterfall chart: Net Income ($50,000) → + Depreciation ($8,000) → − Increase in Accounts Receivable ($12,000) → + Increase in Accounts Payable ($6,000) → − Decrease in Prepaid Expenses ($2,000) → + Amortization ($1,500) = Operating Cash Flow ($51,500). Each step annotated with the reason (non-cash addback, working capital source/use).
- Prompt seed: `claude "Write Python that builds an indirect-method cash flow statement from income statement and balance sheet changes. Given: Net Income=50000, Depreciation=8000, Change_AR=-12000 (increase), Change_AP=6000 (increase), Change_Prepaid=2000 (decrease), Amortization=1500. Compute OCF = Net Income + non-cash addbacks + working capital changes. Build a waterfall chart showing each adjustment as a bar (positive=source, negative=use). Print the reconciliation table step by step."`
- Read / check: Code: verify each working capital change has the correct sign convention (AR increase = use of cash = negative; AP increase = source of cash = positive); verify final OCF = $51,500; verify waterfall bars sum to OCF. Output: the waterfall chart should end at the correct OCF value with each step visible.
- Human supplies: Nothing — fully synthetic (all parameters given in prompt; the human may substitute real company data from 10-K filing for a more authentic version).
- Output medium: Manim — animate the waterfall bars appearing one at a time, with a running total updating after each bar; annotate each bar with the reason.
- The change: Add investing and financing activities (purchase equipment −$20,000, issued stock +$15,000) to complete the full cash flow statement and show ending cash balance.
- Teardown angle: The indirect method reveals every non-cash item and working capital change that separates accounting income from cash. A company with growing receivables is effectively lending money to its customers — the indirect method makes that visible.
- Exclusions: Direct method presentation; free cash flow vs. operating cash flow; cash flow from derivatives.
- Score: 8/10

## Candidate 04 — "Analyze Financial Ratios with Claude: Is This Company Healthy?"
- Source: principles-accounting-bundle/chapters/02-introduction-to-financial-statements.md
- Lane: BUILD (Claude Code)
- Hook: Financial ratios turn three statements (income, balance sheet, cash flow) into a 10-number dashboard. Claude computes all the standard ratios for a target company and compares them to industry benchmarks — flagging where the company is above or below normal.
- The artifact: A dashboard of 10 financial ratios organized in 4 categories: (1) Liquidity (current ratio, quick ratio); (2) Profitability (ROE, ROA, net margin, gross margin); (3) Leverage (D/E ratio, interest coverage); (4) Efficiency (asset turnover, receivables days). Each ratio shown as a gauge or bar, with industry benchmark highlighted and the company's value marked. Red/green coloring for above/below benchmark.
- Prompt seed: `claude "Write Python that computes 10 financial ratios from a company's financials. Given: Current Assets=120000, Current Liabilities=80000, Inventory=30000, Revenue=500000, Net Income=40000, EBIT=60000, Interest=10000, Total Assets=300000, Total Equity=150000, Total Debt=100000, Accounts_Receivable=60000, Gross_Profit=200000. Compute: current ratio, quick ratio, ROE, ROA, net margin, gross margin, D/E ratio, interest coverage, asset turnover, receivables days. Plot as a horizontal bar chart with industry benchmark lines (use retail industry benchmarks)."`
- Read / check: Code: verify current ratio = 120/80 = 1.5; verify quick ratio = (120-30)/80 = 1.125; verify ROE = 40/150 = 26.7%; verify interest coverage = 60/10 = 6.0×. Output: all 10 ratios should be computed with correct formulas; benchmark comparisons should use plausible retail industry values.
- Human supplies: A real company's 10-K annual report data (from SEC EDGAR) makes the analysis authentic. Fully synthetic data with realistic parameters is acceptable for illustration — human decides which level of authenticity is needed.
- Output medium: Manim — animate the 10 bars appearing grouped by category; animate benchmark lines appearing after; color-code each bar red/green based on benchmark comparison.
- The change: Change one key input (double the debt level) and show how all four ratio categories are affected — demonstrating how leverage ripples through the full ratio dashboard.
- Teardown angle: No single ratio tells the whole story — liquidity, profitability, leverage, and efficiency can point in different directions. The dashboard view is the way practitioners actually read financial statements.
- Exclusions: DuPont decomposition derivation; industry-specific ratio adjustments (banks, insurance); segment reporting.
- Score: 8/10

## Candidate 05 — "Build a Break-Even Calculator with Claude: Fixed Costs vs. Contribution Margin"
- Source: principles-accounting-bundle/chapters/05-completing-the-accounting-cycle.md
- Lane: BUILD (Claude Code)
- Hook: Every business has a break-even point — the sales level where revenue exactly covers costs. Below it, every sale loses money; above it, every sale is profit. Claude computes and visualizes the break-even for three different cost structures.
- The artifact: A break-even chart showing Total Revenue (linear), Total Cost = Fixed Cost + Variable Cost (linear), and the break-even point where they cross. Three scenarios side by side: (1) High fixed, low variable (manufacturing); (2) Low fixed, high variable (services); (3) Mixed structure. Break-even quantity and revenue labeled for each. Margin of safety (current sales vs. break-even) annotated.
- Prompt seed: `claude "Write Python that computes and plots break-even analysis for 3 businesses: (1) manufacturing: Fixed=100000, Variable_per_unit=20, Price=50; (2) services: Fixed=20000, Variable_per_unit=40, Price=60; (3) mixed: Fixed=50000, Variable_per_unit=30, Price=55. For each: compute BEP_units = Fixed/(Price-Variable), BEP_revenue = BEP_units*Price, contribution_margin_ratio = (Price-Variable)/Price. Plot Total Revenue, Total Cost, and Fixed Cost lines on the same axes. Mark the break-even point."`
- Read / check: Code: verify BEP_units(1) = 100000/(50-20) = 3333 units; verify BEP_revenue(1) = 3333 × 50 = $166,667; verify contribution margin ratio(1) = 30/50 = 60%. Output: the three charts should show different slope relationships; the manufacturing firm's BEP should be furthest to the right in units.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim — animate the Revenue and Total Cost lines being drawn; mark the crossover point with a flash; animate a "current sales" marker showing margin of safety.
- The change: Compute the target profit sales level (how many units needed to hit $50,000 profit?) and show it on the chart as a second target line beyond break-even.
- Teardown angle: The contribution margin — price minus variable cost — is what each unit contributes toward covering fixed costs. Once fixed costs are covered, the contribution margin becomes profit. This is the fundamental insight of cost-volume-profit analysis.
- Exclusions: Multiproduct break-even; non-linear cost functions; step-fixed costs.
- Score: 8/10

## Candidate 06 — "Simulate Depreciation Methods with Claude: Straight-Line vs. Declining Balance"
- Source: principles-accounting-bundle/chapters/05-completing-the-accounting-cycle.md
- Lane: BUILD (Claude Code)
- Hook: Two companies buy identical machines. One depreciates straight-line; the other uses declining balance. Their income statements diverge immediately — and their tax bills differ for years. Claude plots both and shows the long-run equalization.
- The artifact: A three-panel animation: (1) Book value vs. year for a $100,000 machine (5-year life, $10,000 salvage) under straight-line vs. double declining balance; (2) Annual depreciation expense for each method; (3) Cumulative accumulated depreciation. Both methods fully depreciate to the same salvage value — but the timing of the expense differs. A fourth panel shows the tax advantage of accelerated depreciation in early years.
- Prompt seed: `claude "Write Python that computes depreciation schedules for a $100,000 asset (5-year life, $10,000 salvage) using three methods: (1) Straight-line: (Cost-Salvage)/Life per year; (2) Double Declining Balance: 2*(1/Life)*Book_Value per year, switch to SL when SL > DDB; (3) Sum of Years Digits: depreciation = (remaining_years/sum_of_years)*(Cost-Salvage). Plot: book value vs year, annual depreciation expense vs year for all three. Print the depreciation schedule table."`
- Read / check: Code: verify SL annual depreciation = (100000-10000)/5 = $18,000; verify DDB rate = 40% of book value; verify all methods reach salvage value of $10,000 at end of year 5; verify DDB switches to SL at the correct year. Output: the book value curves should all end at $10,000; DDB curve should decline faster early and slower late.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim — animate the book value curves for all three methods side by side, diverging from $100,000 at year 0 and converging to $10,000 at year 5; annotate the largest early-year expense difference.
- The change: Compute the "present value of tax savings" from accelerated depreciation vs. straight-line (assuming 25% tax rate, 8% discount rate) — showing the real cash benefit of accelerated methods even though total depreciation is the same.
- Teardown angle: Depreciation method choice doesn't change total expense over the asset's life — it only changes when the expense is recognized. Accelerated methods shift expenses earlier, which has real tax and cash flow consequences.
- Exclusions: Section 179 expensing; MACRS for tax purposes; impairment testing.
- Score: 7/10

## Candidate 07 — "Audit the Accounting Equation with Claude: Does Every Transaction Balance?"
- Source: principles-accounting-bundle/chapters/02-introduction-to-financial-statements.md
- Lane: BUILD (Claude Code)
- Hook: Every accounting transaction must preserve Assets = Liabilities + Equity — no exceptions. Claude codes the equation as an invariant, runs 20 transactions, and flags any that would violate it (common student errors).
- The artifact: A transaction log with 20 entries showing the before/after state of A = L + E for each transaction. Green checkmarks for balanced transactions; red flags for the three intentionally planted errors (e.g., recorded revenue without increasing equity, recorded asset purchase that only debits one side). A running balance sheet updates after each transaction.
- Prompt seed: `claude "Write Python that simulates the accounting equation A = L + E for 20 transactions. Store balances as: assets, liabilities, equity = 100000, 40000, 60000 initially. For each transaction, apply the changes and verify A == L + E. Include 3 intentional errors (transactions that would violate balance). Flag violations. Transactions: buy inventory $5000 cash, sell services $3000 on account, pay rent $1200 cash, borrow $10000 from bank, pay salary $2000, etc."`
- Read / check: Code: verify the initial equation holds: 100000 = 40000 + 60000; verify each valid transaction is self-balancing (double-entry); verify the 3 error transactions are correctly detected. Output: the running balance sheet should update after each transaction; errors should print a clear message.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim — animate the A=L+E equation as a balance scale; each transaction tips it momentarily, then the double entry restores balance; error transactions break the scale (red animation).
- The change: Add a complex transaction (record depreciation: reduce asset, reduce equity via expense) and show how it remains balanced even though both sides decrease.
- Teardown angle: The accounting equation is the bedrock constraint of all financial reporting — double-entry bookkeeping exists specifically to enforce it. Every error in accounting ultimately manifests as a violation of this equation.
- Exclusions: Off-balance-sheet financing; consolidation eliminations; SPE accounting (Enron-style).
- Score: 7/10

## Candidate 08 — "Build a Ratio Trend Analysis with Claude: Spotting the Pattern Before the Crisis"
- Source: principles-accounting-bundle/chapters/02-introduction-to-financial-statements.md
- Lane: BUILD (Claude Code)
- Hook: Ratio deterioration typically starts 2–3 years before a financial crisis becomes public. A trend analysis of 5 years of ratios for a synthetic "distressed company" shows the warning pattern — and when a sophisticated analyst would have sold.
- The artifact: A multi-line trend chart showing 5 years of: current ratio (falling through 1.0), interest coverage (falling toward 1.5×), operating cash flow margin (declining), and debt-to-equity (rising). Three vertical zones: "healthy" (years 1-2), "warning" (years 3-4), "crisis" (year 5). An annotation layer shows which ratio triggered the warning signal first.
- Prompt seed: `claude "Write Python that plots 5-year trend analysis of financial ratios for a company approaching distress. Year 1-5 data (provide synthetic): current_ratio=[2.1, 1.8, 1.4, 1.1, 0.8], interest_coverage=[8, 6, 4, 2.5, 1.2], OCF_margin=[0.12, 0.10, 0.07, 0.04, 0.01], debt_equity=[0.5, 0.7, 1.0, 1.5, 2.2]. Plot all 4 ratios on a 2x2 subplot. Mark warning thresholds (current<1.5, coverage<3, OCF_margin<0.05, D/E>1.5) as horizontal dashed lines. Shade the warning and crisis zones."`
- Read / check: Code: verify threshold lines appear at the correct values for each ratio; verify color shading correctly identifies years 3-4 as "warning" and year 5 as "crisis" based on threshold violations; verify ratios monotonically deteriorate (the pattern should be consistent). Output: all four subplots should show a clear downward (or upward, for D/E) trend with threshold crossings visible.
- Human supplies: Optionally, real historical data from a company that went through financial distress (e.g., Sears, Toys R Us) from public 10-K filings — makes the pattern more compelling. Synthetic data acceptable for illustration.
- Output medium: Manim — animate the trend lines building year by year; when a ratio crosses its threshold, animate a warning flash; final frame shows the full 5-year picture with crisis zones shaded.
- The change: Add a "Altman Z-score" composite distress predictor computed from the same inputs and show it declining into the "distress zone" in parallel with the individual ratios.
- Teardown angle: Financial distress is rarely sudden — it's a gradual deterioration that shows up in the ratios 2–3 years before bankruptcy. The accounting data is public; the question is whether anyone reads it carefully enough.
- Exclusions: Detailed bankruptcy process (Chapter 11 reorganization); specific fraud case studies; credit rating agency methodology.
- Score: 7/10
