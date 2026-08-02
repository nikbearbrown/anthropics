# Chapter 12 — Financial Statement Analysis
*Three documents, one system — and the numbers only make sense when you read all of them.*

There is a thing that happens when you hand someone a hundred-and-seventy-six-page document and tell them to have an opinion on it in forty-eight hours. Most people flip to the summary, read the executive's letter, look at a few big numbers, and walk into the room hoping no one asks a follow-up question.

Maya is not going to do that. She is going to learn to read financial statements the way a doctor reads a chart — not memorizing every number, but knowing which numbers to look at, why they matter, and what it means when two of them are moving in opposite directions. By the time she sits down in that interview room, she will have a view. Not a hedge. A view.

---

A company keeps three financial statements, and the most important thing to understand about them before you compute a single ratio is that they are not three separate documents. They are one system described from three angles.

The income statement shows what happened during a period — a quarter, a year. Revenue at the top. Cost of goods sold subtracted to get gross profit. Operating expenses subtracted to get operating income. Interest, taxes, and a few other items subtracted to get net income. It answers the question: did the company make money during this period?

The balance sheet shows what the company owns and owes at a single moment in time — a snapshot. Assets on one side: cash, receivables, inventory, equipment, intellectual property, goodwill from past acquisitions. Liabilities on the other: accounts payable, short-term debt, long-term debt, deferred revenue. Equity is the difference — the residual claim of the owners after all obligations are netted out. It answers: what is the company's financial structure right now?

The cash flow statement shows where cash actually moved during the period. Three sections: operating activities (cash generated or consumed by running the business), investing activities (cash spent on or recovered from physical and financial assets), financing activities (cash raised from debt and equity issuers, or returned to them). It answers: is the company actually generating cash, independent of what the accounting says?

![Three-box diagram showing the income statement, cash flow statement, and balance sheet linked by net income, ending cash, and retained earnings — one accounting system viewed from three angles](images/12-financial-statement-analysis-fig-01.png)
*Figure 12.1 — Three statements, one system*

Here is the connection between them, and why it matters. Net income from the income statement is the starting point for the operating section of the cash flow statement — but then you add back non-cash charges and adjust for changes in working capital to get from accounting profit to actual cash. The ending cash balance from the cash flow statement updates the cash line on the balance sheet. The retained earnings on the balance sheet equal the prior period's retained earnings plus net income minus any dividends paid. Pull one thread and you see the others move.

The practical implication of this interconnection is that you cannot read any one statement alone without being misled. A company can be profitable on the income statement and cash-negative in the same period — this happens routinely in fast-growing companies that are building receivables and inventory faster than they collect cash. A company can be generating cash while reporting losses — this happens in declining companies that are harvesting their asset base faster than it deteriorates. The three statements together tell the story. Any one alone is a rumor.

---

A financial ratio is just a way of putting a number in context. Revenue of $400 million tells you almost nothing by itself — is that good? For what kind of company? Compared to what? Revenue divided by total assets tells you how efficiently the company is converting its asset base into revenue. Revenue compared to the same period last year tells you growth. Gross profit divided by revenue tells you how much money the company keeps before operating expenses. The ratio is not more sophisticated than the underlying numbers; it is just the underlying numbers in a form you can compare.

There are five families of ratios, each answering a different question.

Liquidity: can the company pay its near-term bills? The current ratio — current assets divided by current liabilities — is the headline number. A current ratio above 1.5 is generally healthy. Below 1.0 is a warning. The quick ratio refines this by stripping out inventory, which may not be easily liquidated, leaving only cash and receivables in the numerator.

Profitability: is the business actually making money, and how much? Gross margin tells you the economics of producing the product before any overhead. Operating margin tells you whether the business generates profit from its core operations. Return on assets tells you how much profit the company generates per dollar of assets deployed. Return on equity tells you how much profit per dollar of book equity.

Leverage: how much debt is the company carrying relative to its capacity to service it? Debt-to-equity is the structural measure. Interest coverage — EBIT divided by interest expense — measures the cushion. Coverage of five times means operating earnings could fall by 80% before the company struggles to pay interest. Coverage below two times is worth paying attention to.

Efficiency: how well is the company using what it has? Asset turnover — revenue divided by total assets — is the top-line efficiency measure. Days sales outstanding — receivables divided by daily revenue — tells you how long it takes to collect cash after a sale. A rising DSO is worth investigating: it might mean the company is extending easier credit to boost revenue, which can unwind.

Valuation: how expensive is the stock? Price-to-earnings, price-to-book, enterprise value to EBITDA. These ratios matter when you are thinking about the stock price, not the underlying business's health. They are the last family to consider, not the first.

The right order: get the liquidity and leverage picture first — can the company survive — then profitability — is the model working — then efficiency — is the asset base being used well — then valuation. Many analysts do this in reverse order and then wonder why they keep getting surprised.

---

The most powerful single technique in financial statement analysis is called DuPont decomposition, and it is worth understanding on its own terms rather than just as a formula to apply.

Return on equity — net income divided by shareholders' equity — is the most widely quoted measure of a company's financial performance. The problem is that a given ROE can arise from very different underlying situations, and unless you know which situation you are in, you do not know what the number is telling you.

DuPont is the fix. The identity is:

$$\text{ROE} = \frac{\text{Net Income}}{\text{Revenue}} \times \frac{\text{Revenue}}{\text{Assets}} \times \frac{\text{Assets}}{\text{Equity}}$$

which is, after cancellation, just net income over equity. But the decomposition says something. The first term is net margin — how much profit per dollar of revenue. The second is asset turnover — how much revenue per dollar of assets. The third is the leverage multiplier — how much assets per dollar of equity, which rises as a company takes on more debt.

ROE = Net Margin × Asset Turnover × Leverage.

Two companies with identical ROEs of 20% can be in completely different states. One might have 5% net margin, 2.0× asset turnover, and 2.0× leverage — a retailer, perhaps, with thin margins and fast inventory turns. Another might have 20% net margin, 0.5× asset turnover, and 2.0× leverage — a software company with high margins and low capital intensity. Same headline, different business, different risks, different questions to ask. DuPont is what makes the comparison meaningful.

---

Let me walk through this with three companies Maya will recognize, because the patterns are instructive and the numbers are large enough to make the differences visible.

Microsoft, Apple, and Alphabet are all large-cap technology companies. They are roughly comparable in the sense that they all write software and have global distribution. They are radically different in their financial structures, and examining them side by side is a better education than any textbook problem.

Approximate ratios from their most recent 10-Ks:

| Ratio | MSFT | AAPL | GOOGL |
|---|---:|---:|---:|
| Current ratio | 1.8 | 1.0 | 2.1 |
| Gross margin | 70% | 45% | 58% |
| Operating margin | 42% | 30% | 28% |
| Net margin | 36% | 25% | 24% |
| ROA | 14% | 28% | 16% |
| ROE | 36% | 175% | 26% |
| Debt-to-equity | 0.5 | 1.5 | 0.1 |
| Asset turnover | 0.55 | 1.05 | 0.65 |

Start with Microsoft. Gross margin of 70% is the signature of a software business with high recurring revenue and negligible marginal cost of delivery. Once the software is written and the infrastructure is running, an additional customer costs very little to serve — that economics shows up as gross margin. Operating margin of 42% is among the highest of any large company anywhere, reflecting the same structure: fixed costs for R&D and sales, but very low variable costs. The DuPont decomposition: 36% net margin × 0.55 asset turnover × 1.8 leverage ≈ 36% ROE. All three terms are moderate. Microsoft's ROE is built on genuine profitability, not financial engineering.

Now Apple. Gross margin of 45% is lower than Microsoft — not because Apple is less well run, but because hardware has meaningfully higher cost of goods than software. When you sell iPhones at scale, you are paying for aluminum, glass, chips, and assembly. The software and services revenue that Apple is growing has much higher margins, and you can watch this dynamic play out in the gross margin trend over five years: it has been rising as services grow as a share of the mix.

But look at ROE. 175%. This number requires explanation. The DuPont decomposition: 25% net margin × 1.05 asset turnover × 6.6 leverage ≈ 173% ROE. That leverage multiplier — 6.6 — is the answer. Apple has been borrowing money for years, using the proceeds to buy back shares, shrinking the equity base. As equity shrinks, ROE rises mechanically: the same net income divided by a smaller equity base produces a larger ratio. This is not manipulation; it is a deliberate capital allocation strategy. The company generates more cash than it can reinvest profitably in its own business, so it returns it to shareholders, in part by buying back shares financed with cheap debt. The ROA — 28%, the highest of the three — tells you what the underlying business produces before leverage. It is an exceptional business. The 175% ROE is that exceptional business amplified by a highly aggressive balance sheet.

Alphabet is the contrast. Debt-to-equity of 0.1 — the company carries almost no debt relative to its equity base. ROE of 26% is achieved with essentially no leverage. The DuPont: 24% net margin × 0.65 asset turnover × 1.6 leverage ≈ 25%. Every percentage point of that ROE is operational. The company has a current ratio of 2.1 — a large cash cushion, consistent with a management culture that has historically preferred financial conservatism to capital return optimization. Whether this is the right policy (leaving capital idle) or prudent (maintaining optionality for large investments like AI infrastructure) is a real question about the business.

| Company | Net margin | Asset turnover | Leverage multiplier | Computed ROE | Reported ROE |
|---|---|---|---|---|---|
| **MSFT** | 36% | 0.51 | **1.8×** | 33% | 33% |
| **AAPL** | 25% | 1.04 | **6.6×** | 172% | 172% |
| **GOOGL** | 22% | 0.62 | **1.6×** | 22% | 22% |

*Same headline ROE story (high), three completely different decompositions. Apple's 6.6× leverage multiplier — driven by its capital-return program (large buybacks shrinking equity) — produces a 172% ROE that has almost nothing in common with MSFT's 33% from operating performance. Reading ROE without the DuPont decomposition is reading a single number that is doing three different jobs.*

The lesson of the comparison is not which company is "best." It is that identical headline numbers mean different things, and that DuPont is what lets you see through the headline to what is actually happening. A naive analyst seeing Apple's 175% ROE next to Microsoft's 36% would draw the wrong conclusion. The decomposition draws the right one.

---

Trend analysis is, in my view, the most underrated tool in financial statement analysis. A single year's ratios are a photograph. Five years of ratios are a film. The photograph shows you where the company is. The film shows you where it is going.

Gross margin trend is the one I watch most carefully, because it reveals pricing power and competitive position over time. A company whose gross margin has been stable for five years can hold price; its competitive advantage is intact. A company with declining gross margin is losing the ability to hold price — customers are defecting, competitors are undercutting, the product is commoditizing. You cannot see this in a single year, but you see it unmistakably in a five-year chart.

For Microsoft, gross margin has been stable to slightly rising over five years, consistent with a dominant SaaS business with strong renewal economics. For Apple, gross margin has been gradually expanding as services grow — the mix shift toward higher-margin revenue is visible in the trend. For Alphabet, margins have been more volatile, compressing in periods of heavy cloud and AI investment — the company is choosing to invest aggressively and accepting margin compression as the cost.

The trend tells a different story than the level. A company at 25% gross margin that has been at 24%, 24.5%, 24.8%, 25% is in a better position than one at 28% that has been at 33%, 32%, 30%, 28%. The absolute number favors the second company; the direction of travel favors the first. You need both.

<!-- → [CHART: Five-year gross margin trend lines for MSFT, AAPL, and GOOGL on the same axes — x-axis is year, y-axis is gross margin percentage. Three lines, different colors. MSFT line is stable/slightly rising near 70%. AAPL line starts lower (~38%) and trends upward toward 45%. GOOGL line is more volatile, compressing in investment-heavy years. Student should see that the absolute levels matter less than the direction and stability of each line.] -->

---

Maya's interview target — a mid-stage growth tech company, $400M revenue, eighteen months public — is a different financial profile from any of the three giants above. But the framework applies identically.

She runs the same analysis. Three things stand out.

Operating margin is negative, running around -8% in the most recent period. For a growth-stage tech company, this is not a crisis — it is a description. The company is spending more on sales and marketing and R&D than it is retaining as operating profit, deliberately, because it is buying growth. The question is not whether the number is negative but whether it is getting less negative. Two years ago it was -25%. A year ago, -16%. Most recently, -8%. The trend is the story.

Gross margin is 75% and stable. This is the most important number in the whole analysis, and it is good news. Gross margin in a software business is roughly what the unit economics look like before overhead. 75% means that for every dollar of revenue, seventy-five cents is available to cover sales, marketing, R&D, and G&A, and then hopefully to contribute to profit. A business with 75% gross margins can, in principle, become very profitable when it stops investing so aggressively. A business with 40% gross margins is structurally less able to do so. The gross margin tells you what the company will look like when it grows up.

Cash position is substantial. Current ratio is high. The company has roughly two years of runway at current burn. It is not under near-term financial pressure.

The answer to the interview question assembles from these three observations. The business model is sound — gross margins confirm it. The path to profitability is visible — the trend in operating margin shows it. The timeline is adequate — the cash position supports it. The questions that remain are about the rate of customer acquisition cost growth, the durability of the gross margin as competition intensifies, and the revenue level at which the model reaches break-even.

That is a defensible view. It is specific. It can be argued. It came from forty-eight hours of looking at the right numbers in the right order.

---

I want to end with something about what this framework does and does not give you.

Financial statement analysis is the systematic translation of three accounting documents into a coherent picture of a company's financial health. The ratios put numbers in context. DuPont decomposition reveals what is driving ROE. Trend analysis shows direction of travel. Peer comparison gives meaning to absolute levels. These techniques are not difficult, individually. What makes them powerful is discipline — actually pulling the comparable companies' numbers, actually working through five years of history, actually checking that the DuPont multiplication produces the reported ROE within rounding. The check matters because the discipline of doing it is what builds the intuition for when something looks wrong.

What the framework does not give you is the full picture of a modern software or platform business. The most important metrics for a SaaS company — net revenue retention, customer acquisition cost, contract duration, dollar-based expansion — do not appear in standardized form in the 10-K. They appear in earnings releases with definitions that change by company and quarter. The GAAP statements capture the financial structure. They do not capture the customer dynamics that will determine whether the financial structure improves or deteriorates.

This is not a flaw in the framework. It is a feature of the problem. Financial statement analysis is the foundation, not the ceiling, of fundamental research. Maya walks into the room with a view on the financial position — liquidity, profitability, leverage, trend. The next questions, the ones about unit economics and retention and competitive position, are where the conversation goes from there. Having the foundation in place is what makes the next questions intelligible.

She will be ready.

---

*A note on what the chapter simplified.* The three-statement analysis presented here treats GAAP financials as the primary source. In practice, analysts layer in non-GAAP adjustments — stock-based compensation add-backs, restructuring charge exclusions, and others — that companies report alongside GAAP figures and that require their own scrutiny. The DuPont ratios also interact with accounting choices: whether a company capitalizes or expenses R&D, how it recognizes revenue for multi-year contracts, whether it leases or owns its real estate. These choices change the ratio levels without changing the underlying business. Learning to identify them is the next layer beyond this chapter.

---

## Exercises

### Warm-up

**1.** A company reports net income of $80M on revenue of $500M, total assets of $600M, and shareholders' equity of $200M. (a) Calculate the three DuPont components: net margin, asset turnover, and leverage multiplier. (b) Compute ROE using the DuPont identity and verify it matches net income divided by equity directly. (c) If the company paid down debt until equity rose to $300M — with all else equal — what would happen to each of the three DuPont components and to ROE? *(Tests: DuPont mechanics and the directional effect of leverage changes.)*

**2.** A company has current assets of $420M and current liabilities of $310M. Inventory is $90M. (a) Calculate the current ratio. (b) Calculate the quick ratio. (c) The current ratio is above 1.5 but inventory is 40% of current assets. What concern does the quick ratio raise that the current ratio conceals, and in what type of business would this gap matter most? *(Tests: liquidity ratio mechanics; the informational difference between current and quick ratios.)*

**3.** A company's income statement shows EBIT of $200M and interest expense of $40M. (a) Calculate the interest coverage ratio. (b) What is the maximum percentage decline in EBIT the company can absorb before it can no longer cover interest? (c) A competitor has coverage of 1.8×. What does this signal about its financial risk relative to the first company? *(Tests: interest coverage mechanics; coverage as a margin-of-safety measure.)*

### Application

**4.** Two retailers report identical ROEs of 18%. Retailer A has 3% net margin, 3.0× asset turnover, and 2.0× leverage. Retailer B has 9% net margin, 1.0× asset turnover, and 2.0× leverage. (a) Verify both ROEs using the DuPont identity. (b) Retailer A operates discount grocery stores; Retailer B sells luxury goods. Does the DuPont decomposition match the business model you would expect for each? (c) If Retailer B's net margin compresses to 6% due to a competitive pricing war, what happens to its ROE? *(Tests: DuPont interpretation across business models; sensitivity to margin compression.)*

**5.** A SaaS company has the following three-year gross margin history: Year 1: 62%, Year 2: 65%, Year 3: 67%. Its nearest competitor shows: Year 1: 71%, Year 2: 69%, Year 3: 66%. (a) Describe the competitive signal each trend communicates, using the chapter's pricing-power argument. (b) Which company would you prefer to own, all else equal, and why — even though the competitor's gross margin is still higher in Year 3? (c) What additional information would you want before acting on this comparison? *(Tests: trend vs. level distinction; gross margin as a competitive-position signal.)*

**6.** A growth-stage company has the following operating margin history: −30%, −22%, −14%, −7%. Revenue has grown 40% year-over-year throughout. Gross margin has held steady at 72%. Cash runway is 18 months. (a) Construct the investment thesis in two sentences using only these data points. (b) Identify the single most important risk to that thesis, and name which ratio or metric you would monitor to track it. (c) At what operating margin level would the company reach approximate cash-flow breakeven, assuming sales and marketing are 35% of revenue and G&A is 12%? *(Tests: applying the Maya framework to a novel growth-stage profile; constructing a thesis from trend data.)*

### Synthesis

**7.** Apple's ROE of 175% and ROA of 28% appear contradictory to a student who has not worked through the DuPont decomposition — a very high ROE alongside a merely good ROA. Explain in prose, without using the formula, why a company can have exceptional ROA and extraordinary ROE simultaneously, and what that combination tells you about the company's capital allocation strategy. Then explain why ROA is, in this case, the more informative measure of the underlying business. *(Tests: DuPont intuition without formula reliance; ROA vs. ROE as measures of business quality vs. financial structure.)*

**8.** The chapter argues that the three financial statements are one system, not three separate documents. A company reports: net income of $50M (income statement); a $30M increase in accounts receivable and a $20M increase in inventory (balance sheet changes); operating cash flow of −$5M (cash flow statement). (a) Reconcile these numbers: explain in mechanical terms why a profitable company can have negative operating cash flow in the same period. (b) What does this situation suggest about the company's revenue recognition practices or growth dynamics? (c) Is this a warning sign, a growth signature, or impossible to classify without additional information? *(Tests: three-statement interconnection applied to a specific numerical scenario; cash vs. accrual accounting distinction.)*

**9.** The chapter presents five ratio families and specifies a reading order: liquidity and leverage first, profitability second, efficiency third, valuation last. A colleague argues the opposite: "Start with valuation — if the stock isn't cheap, nothing else matters." Construct the strongest version of your colleague's argument, then explain why the chapter's ordering is nonetheless correct for the purpose of building a fundamental view on a company's financial health. *(Tests: ratio-ordering logic; distinguishing business-health analysis from stock-price analysis.)*

### Challenge

**10.** You are analyzing a company whose GAAP financials show the following over four years: revenue growing 25% annually, gross margin stable at 68%, operating margin improving from −18% to −4%, and net income negative throughout. However, the company's stock has tripled over the same period. Using only the analytical tools from this chapter — the three statements, the five ratio families, DuPont, and trend analysis — identify what a GAAP-only analysis would miss that might explain the stock's performance, and describe what non-GAAP or supplementary metrics you would need to complete the picture. *(Tests: the chapter's stated limits — what GAAP captures and what it doesn't; bridging from financial statement analysis to the unit-economics layer the chapter points toward but does not cover.)*

---

###  LLM Exercise — Chapter 12: Financial Statement Analysis

**Project:** Maya's Memo, Built Across the Course
**What you're building this chapter:** The Financial-Statement Diligence section of the memo: does the company's accounting support the equity case, or contradict it?
**Tool:** Cowork

---

**The Prompt:**

```
I'm working on Maya's Memo. All quantitative sections are now in the project.

Chapter 12 taught:
- **The three statements as one system**: net income → cash flow → balance-sheet retained earnings
- **Accrual quality**: net income vs. operating cash flow; growing gap = warning
- **The ratios that matter**: ROE, ROIC, current ratio, debt/equity, FCF margin
- Reading 10-Ks like a doctor reads a chart

For a public-equity position, do this in **Cowork**:

1. **Pull the latest 10-K and 10-Q** from SEC EDGAR for the company. Save them in `filings/`.

2. **Read for structure.** Extract:
   - Income statement: revenue, gross profit, operating income, net income (last 5 years)
   - Balance sheet: cash, total assets, total liabilities, equity (last 5 years)
   - Cash flow statement: operating cash flow, capex, FCF (last 5 years)

3. **Reconcile the system.** Confirm that:
   - Net income from the income statement matches the cash-flow statement's starting line
   - Ending cash balance from cash flow ties to the balance sheet's cash line
   - Retained earnings movement = net income − dividends

4. **Compute the ratios.** Five years for each:
   - **ROE** = net income / equity
   - **ROIC** = NOPAT / invested capital
   - **Current ratio** = current assets / current liabilities
   - **Debt/equity** = total debt / equity
   - **FCF margin** = FCF / revenue

5. **The accrual-quality check.** Plot net income vs. operating cash flow over the five years. A widening gap (net income growing faster than OCF) is a warning. State what the chart shows.

6. **The diligence verdict.** One paragraph. Does the accounting support the equity story — *the same story you used in `03-claim-framing.md` and `05-dcf.md`* — or contradict it? Name three specific line items that would change your recommendation if they moved.

7. **Save the analysis as `analysis/12-statements.md`** with the ratios table, the accrual-quality chart description, and the verdict.

For a private business or a bond, adapt: the bond's covenant compliance schedule + the issuer's credit metrics; the private business's tax returns + bank statements + AR/AP aging.
```

---

**What this produces:** A markdown document `analysis/12-statements.md` containing the five-year ratios table, the accrual-quality finding, and a verdict that names specific line items whose movement would change the recommendation.

**How to adapt this prompt:**

- *For your own project:* Replace any bracketed domain placeholder with your specific instrument, ticker, or context. The exercise structure is instrument-agnostic; the content is yours.
- *For ChatGPT / Gemini:* Works as-is. For ChatGPT, save the running memo to a Custom GPT instead of a Claude Project. For Gemini, paste the project's accumulated section files into the context window each session.
- *For Claude Code:* Optional — `analysis/12-statements.py` can pull EDGAR filings via `sec-edgar-downloader` and compute ratios automatically. Cowork's file-handling makes this section easier to assemble than pure code.
- *For a Claude Project:* Cowork is the right tool — it can read PDFs from EDGAR, extract numbers, and assemble the ratios table in one session. Save the result to the project for the capstone.

**Connection to previous chapters:** Chapters 5 and 11 produced the *price* and the *factor read*; Chapter 12 tests whether the company's actual accounting supports the case the prior chapters assumed.

**Preview of next chapter:** Chapter 13 — the capstone — assembles all twelve sections into one integrated 6–10 page memo with a defended recommendation.

---

## AI Wayback Machine

The ideas in this chapter didn't appear from nowhere. **Luca Pacioli** was publishing *Summa de Arithmetica* in 1494 — including the first complete printed treatment of double-entry bookkeeping, the structural ancestor of every income statement, balance sheet, and cash-flow statement the chapter teaches decades before most people had heard of the three financial statements as one interconnected accounting system. Here's a prompt to find out more — and then make it better.

![Luca Pacioli, c. 1495. AI-generated portrait based on a public domain painting (Wikimedia Commons).](images/luca-pacioli.jpg)
*Luca Pacioli, c. 1495. AI-generated portrait based on a public domain painting.*

**Run this:**

```
Who was Luca Pacioli, and how does his 1494 publication of double-entry bookkeeping in *Summa de Arithmetica* — over five centuries before any spreadsheet existed — connect to the chapter's argument that the three financial statements are one interconnected system, not three independent documents? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.
```

→ Search **"Luca Pacioli"** on Wikipedia after you run this. See what the model got right, got wrong, or left out.

**Now make the prompt better.** Try one of these:

- Ask it to explain *double-entry bookkeeping* in plain language, as if you've never seen a balance sheet
- Ask it to compare Pacioli's 1494 ledger to the modern income-statement / balance-sheet / cash-flow-statement triad
- Add a constraint: "Answer as if you're writing the historical foundation paragraph for a chapter on financial-statement analysis"

What changes? What gets better? What gets worse?

