# Chapter 5 — Financial Statements

*One fact, four true stories, and why you need all of them.*

---

Here is a puzzle that took me an embarrassingly long time to make sense of.

A company buys a $100 million factory in March.

At the end of the year, you look at the income statement. The factory is almost invisible. There's a depreciation charge — maybe $6 million, if the factory is expected to last about ten years — but the other $94 million appears nowhere. The income statement doesn't seem to care that the company just spent $100 million.

You look at the balance sheet. The factory is there: $94 million under property, plant, and equipment ($100 million purchase price minus the $6 million depreciated so far). It looks like an asset, not a cost.

You look at the cash flow statement. There it is: a $100 million outflow under investing activities. The full amount, gone.

Same factory. Same company. Same year. Three different documents, three completely different stories about the same fact — and all three are true. The income statement is telling you about *earnings*. The balance sheet is telling you about *what the firm owns*. The cash flow statement is telling you about *cash*.

None of these is the complete picture. That's not a flaw in accounting — it's the design. Financial statements are not trying to tell you one simple number that summarizes a company. They are four different instruments, each measuring something different, each telling you something the others can't. An analyst's job is to read all four together and understand how they connect. That's what this chapter teaches.

---

## The income statement — performance over a period

The income statement answers one question: how did the firm perform financially over this period? It is a movie, not a photograph. It shows flow, not position.

The structure runs top to bottom:

```
   Net sales
 − Cost of goods sold (COGS)
 ─────────────────────────────  Gross profit
 − Selling, general & administrative expenses (SG&A)
 − Research and development
 − Depreciation and amortization
 ─────────────────────────────  Operating income (EBIT)
 ± Other income / expenses
 ─────────────────────────────  Income before tax
 − Tax expense
 ─────────────────────────────  Net income
```

**Net sales** is what the firm actually expects to collect — gross revenue minus returns, discounts, and allowances. **Cost of goods sold** captures direct costs of production: materials, direct labor, manufacturing overhead for the goods that actually left inventory during the period. The gap between them is **gross profit** — the first test of whether the company can sell things for more than it costs to make them. Gross margin (gross profit as a fraction of sales) is one of the most important single numbers in equity analysis. It tells you about pricing power and competitive position before anything else contaminates the picture.

Below gross profit, **operating expenses** cover everything else required to run the business — rent, salaries, marketing, R&D. What's left is **operating income**, sometimes called EBIT: earnings before interest and taxes. EBIT measures the profitability of the core business, independent of how the company is financed. A firm with lots of debt has high interest expense; a firm with little debt has almost none. EBIT cuts through that difference and lets you compare the underlying business.

Below EBIT, interest expense, other items, and taxes bring you to **net income** — what's actually left for shareholders after paying everyone else.

**EBITDA** — earnings before interest, taxes, depreciation, and amortization — adds the two largest noncash charges back to EBIT. The idea is that depreciation and amortization are accounting conventions that don't represent cash leaving the firm in that period. If you add them back, you get something closer to the operating cash the business generates. Many analysts and practitioners use EBITDA as a quick proxy for operating cash flow. Warren Buffett has called it a "flawed" metric; the criticism is that depreciation reflects real economic deterioration of assets. A factory that wears out needs to be replaced eventually. Pretending depreciation doesn't exist doesn't make the replacement cost disappear. Use EBITDA, but use it as a starting point, not a conclusion.

For Apple's fiscal 2020: net income approximately $57.4 billion on revenue of approximately $274.5 billion. EBITDA approaching $109 billion. These are the numbers from its 10-K filed on EDGAR, and they set the scale for everything downstream.[^1]

[^1]: Apple Inc., Form 10-K for fiscal year 2020, available via EDGAR. `[verify]` for current vintage.

<!-- → [INFOGRAPHIC: waterfall chart showing Apple's fiscal 2020 income statement from revenue down to net income, with each major subtraction labeled — student should see the relative size of COGS, operating expenses, and tax vs. the margin that survives] -->

---

## The balance sheet — position at a point in time

The balance sheet is a photograph. It doesn't care about flow; it shows what the firm owns and owes at one specific moment — typically the last day of the fiscal year.

Everything on the balance sheet is organized around one equation:

$$\text{Assets} = \text{Liabilities} + \text{Equity}$$

This isn't a coincidence or a convention. It's a tautology: every asset has to be financed by someone — either a creditor (liability) or an owner (equity). The equation must hold by construction.

**Assets** are split by time. *Current assets* are expected to convert to cash within a year: cash, marketable securities, accounts receivable, inventory, prepaid expenses. *Noncurrent assets* are longer-lived: property, plant, and equipment (recorded at historical cost, minus accumulated depreciation), intangibles like goodwill and patents, long-term investments.

**Liabilities** mirror the split. *Current liabilities* due within a year include accounts payable, accrued expenses, short-term debt, the current portion of long-term debt, and deferred revenue. *Noncurrent liabilities* include long-term debt, pension obligations, deferred tax liabilities.

**Equity** is what's left after you subtract liabilities from assets. For a corporation it has two main pieces: contributed capital (what owners paid in for stock) and retained earnings (cumulative profits not yet paid out as dividends). There are subtler pieces too — treasury stock (shares the firm has bought back), accumulated other comprehensive income (gains and losses that haven't yet flowed through the income statement) — but retained earnings is the one that connects the balance sheet to the income statement, and we'll come back to it.

Apple's fiscal 2020 balance sheet: total assets of $323.9 billion, current liabilities of $105.4 billion, noncurrent liabilities of $153.2 billion, equity of $65.3 billion. More striking: $191 billion in marketable securities — more cash and liquid investments than the entire market capitalization of most public companies. That number shapes everything about how Apple is analyzed.

Now, the balance sheet's limitations, which are serious and deserve stating plainly.

**Historical cost.** Most assets are recorded at what the firm paid for them, not what they're currently worth. A factory bought for $100 million, depreciated to $40 million on the books, might actually be worth $200 million if real estate values rose, or $20 million if it's technologically obsolete. The balance sheet doesn't tell you which. The real value of the assets is one of the central questions equity analysis tries to answer.

**Estimates everywhere.** Useful lives of assets, allowances for uncollectible receivables, pension obligations, deferred tax calculations — all of these are estimates. The estimates are disclosed in the footnotes. Reading footnotes is part of the work. A company that consistently lengthens the assumed useful life of its assets is reducing depreciation expense and increasing reported earnings without any change in underlying economic reality.

**Point in time.** A retail firm's balance sheet on December 31 looks very different from the same firm's balance sheet on July 31. Inventory builds before the holiday season. Cash builds after. Most large firms manage their year-end balance sheets to look as strong as possible — a practice called *window dressing*.

**Missing intangibles.** Internally developed brands, processes, software, and human capital don't appear on the balance sheet. Coca-Cola's balance sheet does not show a line for "the Coca-Cola brand." Acquired intangibles do show up (as goodwill), but internally generated ones don't. This is why many technology and consumer-brand companies trade at enormous multiples of book value: the book value is missing most of what makes the business valuable.

<!-- → [IMAGE: side-by-side illustration of two balance sheets for the same retailer — one at peak inventory (October) and one post-holiday (February) — showing how dramatically current assets and current liabilities can shift within one fiscal year] -->

---

## The statement of stockholders' equity — how owners' claims changed

The third statement is the bridge. It shows how the equity section of the balance sheet moved during the period, and in doing so it connects the income statement to the balance sheet.

The structure is a simple flow:

```
Beginning equity balance
+ Net income            (from income statement)
+ Stock issued          (cash from new share sales)
− Dividends paid        (cash returned to shareholders)
− Stock repurchased     (treasury stock purchases)
± Other comprehensive income items
────────────────────────────────────────
  Ending equity balance
```

The largest moving piece is usually **retained earnings**. Each period:

$$\text{Ending RE} = \text{Beginning RE} + \text{Net income} - \text{Dividends}$$

Net income flows from the income statement into retained earnings. Dividends flow out. The ending figure lands on the balance sheet. This is the linkage that makes the four-statement system self-checking: you can verify that the income statement's net income actually made it to the balance sheet.

Three things that trip people up.

Dividends are *not* an income statement expense. They reduce retained earnings directly — a payment out of accumulated profits, bypassing the income statement entirely. Stock buybacks work similarly: they reduce equity, but through a treasury stock account rather than through retained earnings.

Retained earnings is *cumulative*. It reflects every dollar of profit earned and every dollar of dividend paid since the company was founded. A firm with thirty years of profitability and modest dividends can have retained earnings that dwarf any single year's net income.

For the project, this statement is usually short. The key things to read: how much stock has the firm issued or repurchased recently, how much has it paid in dividends, and what does the cumulative scale of retained earnings say about the firm's history of profitability and capital allocation?

---

## The cash flow statement — where the cash actually went

The fourth statement exists because of a gap that accrual accounting creates. Net income is not cash. It includes noncash charges (depreciation) and timing differences (revenue recognized before the cash is collected, expenses accrued before the cash is paid). The cash flow statement exists to reconcile net income back to actual cash.

It has three sections.

**Operating activities** shows cash from the firm's core business. Almost always presented using the *indirect method*: start with net income, add back noncash items (depreciation, amortization), then adjust for changes in working capital (if accounts receivable grew, the firm earned revenue it hasn't collected yet — a cash use; if accounts payable grew, the firm incurred expenses it hasn't paid yet — a cash source). The result is *operating cash flow*.

**Investing activities** shows cash from buying and selling long-term assets. Capital expenditures — the firm buying new equipment, factories, or technology — appear here as outflows. Acquisitions appear here. Proceeds from selling subsidiaries or assets appear here.

**Financing activities** shows cash from interactions with capital providers. Issuing new debt or equity is an inflow. Repaying debt, paying dividends, and buying back stock are outflows.

Sum the three sections, and you get the change in the firm's cash balance for the period:

$$\text{Cash from Ops} + \text{Cash from Investing} + \text{Cash from Financing} = \Delta\text{Cash}$$

Add that change to the beginning cash balance, and you must get the ending cash balance — the same number that appears on the balance sheet. This is the second self-check in the four-statement system.

<!-- → [CHART: stacked bar chart for a hypothetical firm over five years showing operating, investing, and financing cash flows as separate bars — student should see what a healthy mature firm looks like (large positive ops, negative investing, negative financing) vs. a growth firm (positive ops but smaller, large negative investing, positive financing from debt/equity issuance)] -->

**Operating cash flow and free cash flow** are the two derived metrics that show up constantly in equity research, so they deserve a crisp definition here.

*Operating cash flow (OCF)* is the operating section of the cash flow statement. It is the most direct measure of cash generated by the firm's core business after working capital changes.

*Free cash flow (FCF)* subtracts capital expenditures:

$$\text{FCF} = \text{OCF} - \text{Capex}$$

FCF is what's left after the firm has paid for its operations and maintained or grown its productive assets. It is the cash genuinely available to be returned to capital providers — to pay dividends, buy back stock, repay debt, or simply hold. Most equity valuation models, including the discounted cash flow models we build in Chapter 11, discount FCF rather than net income. The reason is simple: FCF is real, distributable cash. Net income is an accounting figure that may include earnings the firm has not yet collected and may never fully collect.

---

## How the four statements connect

The four statements are not independent documents assembled by four different departments. They are one system, connected by accounting identities, and the connections are what make the whole thing auditable.

<!-- → [DIAGRAM: flow diagram showing the four statements as nodes with labeled arrows: net income flows from Income Statement → Statement of Equity → Balance Sheet (retained earnings); ending cash flows from Cash Flow Statement → Balance Sheet (cash line) — student should see at a glance which numbers appear in more than one statement and why] -->

The cleanest connection runs through retained earnings:

```
Income Statement          →   Net income for the period
                                    ↓
Statement of Equity       →   Beginning RE + Net income − Dividends = Ending RE
                                    ↓
Balance Sheet             →   Retained Earnings = Ending RE
```

Three statements, one number. If the retained earnings figure on the balance sheet doesn't match what you'd compute from the income statement and the prior year's balance sheet, something is wrong.

The second connection runs through cash:

```
Cash Flow Statement       →   Beginning cash + Net change in cash = Ending cash
                                    ↓
Balance Sheet             →   Cash and equivalents = Ending cash
```

Two statements, one number. The cash flow statement is essentially a derivation of why the cash balance moved; its endpoint must match the balance sheet.

One subtle point worth making explicit, because it trips up almost everyone when they first see it. An *expense* is recorded on the income statement when it is incurred. A *payable* is recorded on the balance sheet when you owe money without having paid it. When a company incurs $1,500 in utilities expense in October but doesn't pay until November, two things happen simultaneously in October: the expense reduces net income (on the income statement), and accounts payable increases by $1,500 (on the balance sheet). In November, when the cash is paid, accounts payable goes down by $1,500 and cash goes down by $1,500. The expense was recorded once (October); the cash moved once (November); the balance sheet bridged the gap.

This is why the cash flow statement adjusts for changes in working capital when moving from net income to operating cash flow. If accounts payable rose by $50 million during the year, the firm recorded $50 million of expenses but didn't pay that cash. Add it back: operating cash flow is higher than net income by that amount.

<!-- → [IMAGE: two-column timeline for October and November showing the journal entries for the utility-expense example — income statement effect on the left, balance sheet effect on the right, with arrows showing how accounts payable bridges the gap between expense recording and cash payment] -->

The practical consequence: a company can show growing net income while operating cash flow is deteriorating, if it is collecting receivables more slowly, building inventory, or squeezing its suppliers less effectively. Growing net income with declining operating cash flow is one of the earliest signals of financial distress. It is the kind of thing you catch only if you read both statements.

---

## Common-size analysis: making firms comparable

A final technique this chapter needs before the project can proceed.

Apple's revenue in a recent year was approximately $400 billion. A smaller competitor's revenue might be $4 billion. Comparing line items in absolute dollars produces useless conclusions — of course Apple spends more on R&D. The question that matters is what fraction of each dollar of revenue each company spends on R&D.

**Common-size analysis** rescales each line of a financial statement as a percentage of a base item. For the income statement, the base is net sales. For the balance sheet, the base is total assets. Every line becomes a fraction, and firms of radically different sizes become directly comparable.

<!-- → [TABLE: common-size income statement comparing Apple (illustrative) vs. a smaller competitor — rows: net sales 100%, cost of sales, gross profit, R&D, SG&A, operating income, net income — columns show the percentage for each firm, with a difference column; caption directs student to notice where Apple's structural advantages appear] -->

The stories that emerge from common-size analysis are real economic insights, not accounting curiosities. A firm with 44% gross margin versus a competitor's 35% is structurally more profitable at the product level — it either sells at higher prices, produces at lower cost, or both. A firm with 6% SG&A versus a competitor's 12% has a more efficient go-to-market operation. These differences compound: the firm with better gross margin and lower SG&A doesn't just look better on paper, it has more cash available to reinvest in R&D, acquisitions, or shareholder returns.

Common-size analysis also reveals how a firm has changed over time. Build a three-year common-size income statement for the same company. If gross margin is compressing, the firm's pricing power or cost structure is eroding. If SG&A is rising as a percentage of sales faster than revenue is growing, something in the cost structure is getting away from management. These time-series comparisons are part of the equity research report.

The limitation worth stating: common-size analysis works best within an industry. An inventory-intensive retailer, a capital-intensive manufacturer, and an asset-light software firm have structurally different balance sheet profiles — comparing them on a common-size basis requires careful interpretation. Use common-size within industries; apply more caution across them.

---

## The whole system, read together

The income statement, balance sheet, statement of equity, and cash flow statement are four views of the same underlying economic activity. The income statement measures performance. The balance sheet measures position. The statement of equity bridges them through retained earnings. The cash flow statement anchors accrual accounting back to cash.

The linkages between them are the system's self-checks. Net income must flow to retained earnings; retained earnings must land on the balance sheet. Ending cash on the cash flow statement must equal cash on the balance sheet. When these checks fail — when numbers that should match don't — something has gone wrong: an error, a misclassification, or something worse.

For the equity research project, the deliverable from this chapter is concrete. Locate your chosen company's most recent 10-K. Find all four statements. Verify the linkages. Build a common-size income statement and balance sheet for the past three years. Compute operating cash flow and free cash flow for the past five years. Plot them.

When all of that is done, you have the substrate for every analytical move that follows. Chapter 6 computes ratios from these numbers. Chapter 11 builds valuations from the free cash flow figures. The chapters in between apply these statements to specific questions about capital structure, working capital, and acquisition accounting. The four statements are where all of it starts.

---

## Exercises

### Warm-up

**5.1** Name the four primary financial statements. For each, state in one sentence what it measures and whether it covers a period of time or a single point in time.
*(Tests: basic identification of each statement's purpose and temporal orientation)*

**5.2** Explain in your own words why EBITDA is both useful and potentially misleading. What does it add back, and what does that addition assume about economic reality?
*(Tests: understanding of EBITDA as a metric and its limits)*

**5.3** A firm has operating cash flow of $80 million and capital expenditures of $35 million. Compute free cash flow. Then explain why an equity analyst would discount FCF rather than net income when valuing a firm.
*(Tests: FCF computation and the logic connecting it to valuation)*

### Application

**5.4** A firm reports the following for the year:

- Net income: $40 million
- Depreciation and amortization: $12 million
- Increase in accounts receivable: $8 million
- Increase in inventory: $5 million
- Increase in accounts payable: $6 million
- Capital expenditures: $18 million
- Proceeds from issuing long-term debt: $25 million
- Dividends paid: $10 million
- Beginning cash: $30 million

(a) Compute operating cash flow using the indirect method.
(b) Compute investing cash flow.
(c) Compute financing cash flow.
(d) Compute the ending cash balance.
(e) Compute free cash flow.

*(Tests: constructing all three sections of the cash flow statement and deriving FCF)*

**5.5** The following data ($ millions) is available for two firms in the same industry:

| Line | Firm A | Firm B |
|---|---|---|
| Net sales | 1,200 | 600 |
| COGS | 780 | 330 |
| SG&A | 144 | 96 |
| R&D | 60 | 18 |
| Operating income | 216 | 156 |

(a) Construct a common-size income statement for both firms.
(b) Which firm has stronger gross margin? Stronger SG&A discipline? Stronger operating margin?
(c) Firm B is half the size of Firm A. Does size explain the margin differences, or does something structural appear to be different between them? Defend your reading.

*(Tests: common-size construction and interpretation, including the discipline of asking what the percentages reveal)*

**5.6** A company reports beginning retained earnings of $42 million, net income of $18 million for the year, and dividends paid of $7 million.

(a) Compute ending retained earnings.
(b) Where does this ending figure appear, and in which statement?
(c) Suppose the balance sheet at year-end shows retained earnings of $50 million instead of your computed figure. Name two possible explanations for the discrepancy.

*(Tests: the retained earnings linkage and the ability to diagnose a break in it)*

### Synthesis

**5.7** A firm's net income has grown 15% per year for three consecutive years. Over the same period, operating cash flow has grown only 3% per year. Construct three distinct explanations for this divergence — ranging from a benign business reason to a warning sign — and identify what you would look for in the 10-K to distinguish them.
*(Tests: the relationship between net income and operating cash flow, and the analytical value of reading both)*

**5.8** Explain why the balance sheet's equity section (book value) often differs dramatically from the firm's market capitalization. Use the four structural limitations of the balance sheet discussed in the chapter to build your argument. Give one real-world example where the gap is especially large and explain why.
*(Tests: balance sheet limitations and the distinction between book value and market value)*

### Challenge

**5.9** Locate your chosen company's most recent 10-K on EDGAR. Build a common-size income statement and balance sheet for the most recent three fiscal years. Identify the two or three line items that have moved most as a percentage of total sales (or total assets). Then read the MD&A section of the same 10-K and determine whether management addresses those movements. Does management's explanation hold up against what the numbers show?
*(Tests: primary-source research, common-size time-series analysis, and critical reading of management commentary)*

**5.10** Most large public companies report both GAAP net income and one or more "adjusted" earnings figures in their earnings releases and investor presentations. Pick a public company of your choice and find its most recent earnings release. Identify the adjustments management makes to get from GAAP net income to adjusted net income. For each adjustment, evaluate: is it economically defensible (a genuine one-time item that distorts the trend), partially defensible, or essentially a way of flattering the earnings picture? What is the total dollar impact of all adjustments combined, and in which direction does it push reported performance?
*(Tests: critical evaluation of non-GAAP reporting and the judgment required to distinguish legitimate adjustments from earnings management)*

---

## What would change my mind

The chapter argues that the four-statement system is the right framework for analyzing public companies, and that common-size analysis is the right tool for cross-firm comparison. The reading would have to revise if (a) accounting standards moved away from the four-statement framework toward something more integrated — some IFRS proposals have moved in this direction — or (b) empirical evidence emerged that common-size ratios are systematically misleading because of industry-mix effects. The second concern is real but doesn't displace the chapter's claim; it qualifies it.

## Still puzzling

The tension I haven't resolved cleanly is the gap between GAAP reported numbers and management-reported "adjusted" numbers. Most large public companies report adjusted EBITDA, adjusted net income, adjusted EPS — alongside the GAAP statements. Some adjustments are economically defensible (backing out one-time charges that genuinely distort trend earnings). Others are not (excluding stock-based compensation, which is a real cost of attracting and retaining the people who run the business). Distinguishing the two requires judgment, and the judgment isn't always easy. Chapter 6 and the valuation chapters engage this more directly.

---

## Connections forward

- **Chapter 6** computes ratios from these statements — liquidity, leverage, profitability, efficiency, market.
- **Chapter 11** uses cash flow statement data for DCF valuation.
- **Chapter 16** uses the income statement and balance sheet to evaluate capital budgeting decisions.
- **Chapter 17** uses balance-sheet capital structure for WACC computation.
- **Chapter 18** uses all four statements as the substrate for pro forma forecasting.

---

## LLM Exercise — Chapter 5: Structured Summary of the Four Statements

**Project:** Equity Research Report on a Chosen Public Company
**What you're building this chapter:** A structured summary of all four financial statements for your company — the foundation for ratio analysis (Ch 6) and DCF valuation (Ch 11).
**Tool:** Claude Project (the 10-K should already be uploaded).

### The Prompt

```
Based on the most recent 10-K I have uploaded for [your company], produce a structured summary of all four primary financial statements. Use the following format:

### Income Statement (most recent fiscal year)
- Net sales / revenue: $___
- Cost of goods sold: $___
- Gross profit: $___
- Operating expenses (broken into major categories): $___
- Operating income (EBIT): $___
- Interest expense: $___
- Pre-tax income: $___
- Tax expense: $___
- Net income: $___
- Diluted EPS: $___
- EBITDA (computed): $___

### Balance Sheet (fiscal year-end)
- Total current assets: $___
- Major current asset components (cash, receivables, inventory): $___
- Total noncurrent assets: $___
- Major noncurrent components (PP&E net, intangibles, goodwill): $___
- Total assets: $___
- Total current liabilities: $___
- Total noncurrent liabilities: $___
- Total liabilities: $___
- Total equity: $___
- Common shares outstanding (diluted): ___ million

### Statement of Stockholders' Equity (fiscal year)
- Beginning retained earnings: $___
- Plus: net income: $___
- Less: dividends paid: $___
- Less: treasury stock purchased (buybacks): $___
- Ending retained earnings: $___

### Cash Flow Statement (fiscal year)
- Net cash from operations: $___
- Net cash from investing: $___ (note: usually negative for growth firms)
- Net cash from financing: $___
- Major capex line: $___
- Free cash flow (OCF minus capex): $___
- Net change in cash: $___

After the four summaries, do two sanity checks:
1. Verify that net income flows from income statement → statement of equity → balance sheet retained earnings.
2. Verify that ending cash on the cash flow statement equals cash on the balance sheet.

Note any discrepancies or items that look unusual (large goodwill writedowns, deferred revenue spikes, etc.).
```

### What this produces

A 1-2 page structured summary of all four statements. Becomes the financial-foundation section of the report. Used in Chapter 6 (ratios), Chapter 11 (DCF), and throughout.

### How to adapt this prompt

- *For your own company:* Replace [your company].
- *For ChatGPT / Gemini:* Identical.
- *For Claude Code:* Not needed for this exercise.
- *For a Claude Project:* The 10-K should be uploaded; this prompt then references it directly.

### Connection to previous chapters

Builds on Chapter 4's accounting fluency. The transactions you traced in Chapter 4 are aggregated into these statements.

### Preview of next chapter

Chapter 6 computes ratios from these statements. The Chapter 6 LLM Exercise will produce a complete ratio analysis.

---

**Tags:** financial-statements, income-statement, balance-sheet, cash-flow, common-size-analysis, EBITDA, free-cash-flow

---

## AI Wayback Machine

**Mary T. Washington** was the first Black woman CPA in the US (1943) — trained hundreds of accountants and shaped early small-business financial reporting.

**Run this:**

```
Who is Mary T. Washington, and how does their work connect to financial statements we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about their career or ideas.
```

→ Search **"Mary T. Washington"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to apply Mary T. Washington's framework to a specific finance question.
- Add a constraint: "Answer including criticisms or limits of Mary T. Washington's framework."

What changes? What gets better? What gets worse?
