# Chapter 5 — Financial Statements

**Suggested titles**
1. The Four Views of a Company
2. Reading a 10-K
3. The System That Turns a Year Into Numbers

**TL;DR.** Every public company produces four primary financial statements that, taken together, describe its economic activity for a period: the income statement (what it earned), the balance sheet (what it owns and owes), the statement of stockholders' equity (how owners' claims changed), and the cash flow statement (where the cash actually went). The statements are linked — a number that appears in one shows up in another by design — and an analyst's job is to read all four together. This chapter teaches the structure, the linkages, and how to use common-size analysis to compare firms of different sizes.

---

## The puzzle of one fact, three different stories

A company buys a $100 million factory in March of fiscal year 2024.

On the **income statement** for fiscal 2024, the factory purchase appears almost nowhere. There's a fraction of a year of depreciation expense — perhaps $6 million if the factory has a useful life of about ten years — but the bulk of the $100 million does not appear. The income statement shows what the firm *earned*, not what it bought.

On the **balance sheet** at year-end fiscal 2024, the factory appears as a $94 million line item under property, plant, and equipment ($100 million original cost, less the $6 million of accumulated depreciation). The balance sheet shows what the firm *owns* on a particular date.

On the **cash flow statement** for fiscal 2024, the factory appears as a $100 million outflow under investing activities. The cash flow statement shows what the firm actually *paid for and received*.

Same fact, three different stories, all true. The income statement tells you about earnings. The balance sheet tells you about position. The cash flow statement tells you about cash. None of them is the complete picture; only the three together, with the statement of stockholders' equity, give you what an analyst needs.

For the equity research project, this chapter installs the most fundamental analytical skill — *reading the four statements together*. Every chapter from here forward assumes you can do this. The 10-K's pages 30–50 contain the financial statements; what's on them is what we work with.

---

## Learning objectives

After working through this chapter, you should be able to:

- Identify the four primary financial statements and what each measures.
- Trace how the income statement, balance sheet, and statement of equity connect through retained earnings.
- Distinguish operating, investing, and financing cash flows on a cash flow statement.
- Compute and interpret EBITDA, operating cash flow, and free cash flow.
- Construct a common-size income statement and balance sheet.
- Compare two firms of different sizes using common-size analysis.
- Locate each of the four statements in a real 10-K (Apple is our demo).

**Prerequisites.** Chapter 4 (accrual accounting). Chapter 2 (10-K filings).

---

## Concept 1 — The four statements and what each one measures

A public company's annual report — Form 10-K, filed with the SEC — contains four primary financial statements. They are not independent reports. They are four views of the same underlying economic activity, linked by accounting identities.

### The income statement — performance over a period

The income statement (sometimes called *statement of operations* or *profit and loss statement*) measures the firm's financial performance for a defined period — typically a quarter or a fiscal year. It is built top-down from revenue to net income.

The standard structure:

```
   Net sales (or net revenue)
 − Cost of goods sold (COGS)
                                  Gross profit
 − Selling, general & administrative expenses (SG&A)
 − Research and development
 − Depreciation and amortization
                                  Operating income (or EBIT — earnings before interest and taxes)
 + Other income / − Other expenses
                                  Income before tax
 − Tax expense
                                  Net income
```

The terms have specific meanings.

**Net sales** is gross sales minus returns, allowances, and discounts. It is what the firm actually expects to collect from customers. **Cost of goods sold** captures the direct costs of producing what was sold — direct materials, direct labor, manufacturing overhead allocated to the products that left inventory during the period. The difference, **gross profit**, is the most basic measure of a firm's pricing power: how much does revenue exceed the direct cost of goods?

**Operating expenses** below gross profit cover everything else needed to run the business: rent, sales commissions, executive salaries, R&D, marketing. **Operating income** (EBIT) is what's left after operating expenses — the profitability of the firm's core business, before financing costs and taxes.

The split between EBIT and net income matters. EBIT is comparable across firms with different capital structures (one firm with lots of debt has high interest expense; another with little debt has almost none). Net income is what the firm actually keeps for shareholders after paying creditors and the IRS.

**EBITDA** — earnings before interest, taxes, depreciation, and amortization — adds back two large noncash items to EBIT. Many analysts and practitioners use EBITDA as a rough proxy for operating cash flow because it removes the effects of accounting choices about depreciation. EBITDA has critics; Warren Buffett famously dismissed it as a way for executives to make weak businesses look strong. The criticism has merit. Depreciation reflects real economic deterioration of assets; pretending it isn't an expense doesn't make the deterioration go away. Use EBITDA, but use it carefully.

For Apple's fiscal 2020 (the OpenStax demo year), net income was about $57.4 billion on revenue of about $274.5 billion, and EBITDA approached $109 billion.[^1] Real-scale numbers — the company throws off enormous absolute earnings.

[^1]: Apple Inc., Form 10-K for fiscal year 2020, available via EDGAR. `[verify]` for current vintage.

### The balance sheet — position at a point in time

If the income statement is a movie of a period, the balance sheet is a photograph of one moment — typically the last day of the fiscal year or quarter.

The balance sheet has three sections, organized by the accounting equation we built in Chapter 4:

$$\text{Assets} = \text{Liabilities} + \text{Equity}$$

**Assets** are split by liquidity. *Current assets* — expected to convert to cash within a year — include cash and equivalents, marketable securities, accounts receivable, inventory, and prepaid expenses. *Noncurrent assets* — held for more than a year — include property, plant, and equipment (net of accumulated depreciation), intangibles like goodwill and patents, and long-term investments.

**Liabilities** mirror this split. *Current liabilities* due within a year include accounts payable, accrued expenses, short-term debt, the current portion of long-term debt, and deferred revenue. *Noncurrent liabilities* include long-term debt, pension obligations, and deferred tax liabilities.

**Equity** for a corporation has two main pieces: contributed capital (what owners have paid in for stock) and retained earnings (cumulative profits not paid out as dividends). Subtler pieces include treasury stock (shares the firm has bought back) and accumulated other comprehensive income (gains and losses that haven't yet hit the income statement).

Apple's fiscal 2020 balance sheet showed total assets of $323.9 billion, current liabilities of $105.4 billion, noncurrent liabilities of $153.2 billion, and equity of $65.3 billion.[^1] The firm had $191 billion in marketable securities (cash plus short-term and long-term investments) — more cash on its balance sheet than the entire market capitalization of most public companies. This shapes everything about how the company is analyzed; we'll come back to it in Chapter 17.

#### Limitations of the balance sheet

A balance sheet has structural limitations the analyst has to keep in mind.

1. **Historical cost.** Most assets are recorded at what the firm paid for them, not what they're currently worth. A factory bought for $100M that has been depreciated to $40M might actually be worth $200M (if real estate values rose) or $20M (if it's obsolete). The balance sheet doesn't tell you which.
2. **Estimates everywhere.** Useful lives of assets, allowance for doubtful accounts, pension obligations, deferred tax assets — all involve estimates. Estimates can be reasonable or aggressive. The estimates are disclosed in the footnotes, and reading footnotes is part of the work.
3. **Point in time.** A firm with seasonal cash flow can have a very different balance sheet on December 31 than on June 30. Most large firms manage their balance sheets to look strongest at fiscal year-end (a phenomenon called *window dressing*).
4. **Missing intangibles.** Internally developed brands, processes, software, and human capital are *not* on the balance sheet. Coca-Cola's balance sheet does not show "the value of the Coca-Cola brand." Acquired intangibles show up (as goodwill and identified intangibles); internally generated ones don't. This is one reason many tech and consumer-brand companies trade at large multiples of book value — the book misses much of what's valuable.

### The statement of stockholders' equity — how owners' claims changed

The third statement bridges the income statement and the balance sheet. It shows how the equity section of the balance sheet changed during the period.

The structure is a simple flow:

```
Beginning equity balance
+ Net income (from income statement)
+ Stock issued (cash from sale of new shares)
− Dividends paid
− Stock repurchased (treasury stock)
± Other comprehensive income items
                                  Ending equity balance
```

For most corporations, the largest moving piece is **retained earnings**. Each period:

$$\text{Ending RE} = \text{Beginning RE} + \text{Net income} - \text{Dividends}$$

Net income flows from the income statement. Dividends are decided by the board. The result becomes part of the new balance sheet.

Three points to notice. First, retained earnings is *cumulative*. Apple's retained earnings has been built up over decades and reflects all profits earned minus all dividends paid (and stock buybacks, which we'll cover separately). Second, dividends *decrease* retained earnings — they are payments out of accumulated profits, not income statement expenses. Third, stock buybacks (treasury stock purchases) also decrease equity, but through a different mechanism than dividends.

For the project, the statement of equity is usually short and dense. It tells you a few important things: how much stock the firm has issued or repurchased recently, how much it pays in dividends, and the cumulative scale of its retained earnings. A firm that has been buying back stock aggressively (Apple, repeatedly, over the past decade) shows large negative entries in the treasury stock line.

### The cash flow statement — where the cash actually went

The fourth statement is the one that ties accrual accounting back to cash. It reconciles net income (which can include lots of noncash items) to actual cash that moved.

The cash flow statement has three sections.

**Operating activities** — cash from the firm's core business. Almost always presented using the *indirect method*: start with net income, add back noncash expenses (depreciation, amortization), and adjust for changes in working capital accounts (receivables, payables, inventory). The result is *cash from operations*.

**Investing activities** — cash from buying and selling long-term assets and investments. Major capital expenditures (capex) appear as outflows here. Sales of subsidiaries, acquisitions, and changes in investment portfolios all show up.

**Financing activities** — cash from interactions with capital providers. Issuing debt or equity is a cash inflow; repaying debt, paying dividends, and buying back stock are outflows.

Sum the three sections. The total equals the change in the firm's cash balance for the period:

$$\text{Cash from Ops} + \text{Cash from Investing} + \text{Cash from Financing} = \text{Change in cash}$$

And:

$$\text{Beginning cash} + \text{Change in cash} = \text{Ending cash}$$

The ending cash on the cash flow statement must equal the cash on the balance sheet at year-end. If it doesn't, someone made an error.

↳ **Dig Deeper — Non-GAAP measures and "adjusted" earnings**

*Most large public companies report multiple "adjusted" earnings figures alongside GAAP — adjusted EBITDA, adjusted net income, adjusted EPS, "core earnings." The adjustments often add back stock-based compensation, restructuring costs, and acquisition-related expenses. Some adjustments are economically defensible; others are creative accounting in a different costume.*

**Prompt:**
> Explain the SEC's regulations on non-GAAP measures (Regulation G and Item 10(e) of Regulation S-K). Then walk through three specific examples of common non-GAAP adjustments (stock-based compensation, "one-time" restructuring, amortization of acquired intangibles). For each, evaluate: is the adjustment economically defensible, partially defensible, or essentially earnings management dressed up as transparency?

**What to do with the output:** Save it. Your chosen company almost certainly reports non-GAAP measures; the discipline of asking whether each adjustment is real or cosmetic is part of equity analysis.

### The trade-off (concept 1)

Each statement trades **what it shows clearly against what it obscures**. The income statement shows earnings cleanly but hides timing differences with cash. The balance sheet shows position cleanly but hides how the firm got there. The cash flow statement shows cash cleanly but hides the economic substance of the firm's activities. The statement of equity shows owner-claim changes cleanly but in isolation tells you almost nothing. Each statement alone is a partial view; the *system* of four statements is the complete one.

### Worked example — connecting four statements through one transaction

Suppose Apple buys back $80 billion of its own stock in fiscal 2024. Trace the impact:

- **Income statement:** No effect on net income. Buybacks are not an expense.
- **Cash flow statement:** $80 billion outflow under financing activities (cash paid to repurchase stock).
- **Statement of equity:** Treasury stock balance increases by $80 billion (stock repurchased and held by the firm). Common shares outstanding decrease.
- **Balance sheet:** Cash decreases by $80 billion (asset side). Treasury stock increases by $80 billion (a contra-equity account, reducing total equity by $80 billion). Both sides remain in balance.

For the project: when Apple buys back stock, EPS rises mechanically because shares outstanding fall, even if net income is flat. Read the share-count footnote and the buyback announcements carefully; they affect every per-share metric in the rest of the analysis.

### Common misconceptions

- *"Net income is what the firm earned in cash."* No — net income includes noncash items like depreciation and accruals.
- *"Equity is what the firm is worth."* Equity is book value, an accounting construct. Market value (market cap) is what the firm trades for. The two can differ by 10x or more.
- *"The four statements are independent."* They are linked by design. A change to one usually requires changes to others.

---

## Concept 2 — Connecting the statements: the integrated system

The four statements form one self-checking system. The same numbers appear in multiple statements by design. If they don't match, there's been an error or a misclassification.

### The retained earnings link

The cleanest link runs through retained earnings:

```
Income Statement (period)        →   Net income for the period
                                            ↓
Statement of Equity               →   Beginning RE + Net income − Dividends = Ending RE
                                            ↓
Balance Sheet (period-end)       →   Retained Earnings line equals "Ending RE"
```

Three statements, one number. Net income flows from top to bottom. If you compute net income and roll it through to the balance sheet, the retained earnings figure on the balance sheet must match.

### The cash link

A second link runs through cash:

```
Cash Flow Statement (period)     →   Beginning cash + Net change in cash = Ending cash
                                            ↓
Balance Sheet (period-end)       →   Cash and Equivalents line equals "Ending cash"
```

Two statements, one number. The cash flow statement is essentially a derivation of the cash balance change, broken down by source (operating, investing, financing). The endpoint must match the balance sheet.

### Expenses vs. payables — a common confusion

A subtle point worth making explicit. An *expense* is recorded on the income statement when it's incurred (the matching principle from Chapter 4). A *payable* is recorded on the balance sheet to represent an obligation to pay. The two are linked: when you incur an expense without paying cash, you simultaneously record the expense (reducing equity through retained earnings) and a payable (a liability).

Concrete example: a firm incurs $1,500 of utilities expense in October but doesn't pay until November.

**October entries:**
- Utility expense: +$1,500 (income statement, reducing net income)
- Accounts payable: +$1,500 (balance sheet liability)

**November entries:**
- Cash: −$1,500 (balance sheet asset down)
- Accounts payable: −$1,500 (balance sheet liability down)

The expense was recorded once (in October). The cash payment was recorded once (in November). The balance sheet bridges the gap with the accounts payable line item.

For the project, this is why the cash flow statement adds back changes in accounts payable to get from net income to operating cash flow. If accounts payable rose by $50M during the year, that means $50M of expenses recorded on the income statement were *not* paid in cash — the firm preserved cash by extending its payables.

### Reading Apple's four statements together

A useful exercise. Open Apple's most recent 10-K. Find:

1. **Income statement** — usually labeled "Consolidated Statements of Operations." Note net income for the most recent fiscal year.
2. **Balance sheet** — labeled "Consolidated Balance Sheets." Note total assets and total liabilities + equity (must be equal).
3. **Statement of equity** — labeled "Consolidated Statements of Shareholders' Equity." Verify that beginning RE + net income − dividends ≈ ending RE (small adjustments for stock-based compensation and other items will make it not exactly equal).
4. **Cash flow statement** — labeled "Consolidated Statements of Cash Flows." Verify that beginning cash + net change in cash = ending cash on the balance sheet.

Once the four statements check out, you have the firm's financial picture for the period. Subsequent chapters give you tools to *interpret* what the picture shows.

↳ **Dig Deeper — Goodwill impairment and what it actually means**

*When a firm acquires another firm for more than the target's fair value, the excess gets recorded as "goodwill" — an intangible asset on the balance sheet. Goodwill doesn't depreciate; it sits there indefinitely unless impaired. When firms write down goodwill in large amounts (think Yahoo writing down Tumblr or AT&T writing down Time Warner), the write-down is admitting an acquisition didn't pan out.*

**Prompt:**
> Explain how goodwill is created in an acquisition (purchase price minus identifiable net assets at fair value). Then explain how goodwill impairment testing works under ASC 350. Walk through one famous goodwill writedown case (Yahoo/Tumblr 2016, AT&T/Time Warner 2022, or another large recent case): what the original deal was, what changed, and what the impairment said about the acquisition's outcome.

**What to do with the output:** Save it. Goodwill on your chosen company's balance sheet is the residue of past acquisitions; impairment events tell you about deals that didn't work.

### The trade-off (concept 2)

The integrated system trades **redundancy against verification**. Every important number appears in at least two places. The redundancy is what makes accounting fraud difficult to commit cleanly — manipulating one statement requires manipulating others, and cross-checks can catch inconsistencies. The cost is bookkeeping complexity. The benefit is auditability.

### Worked example — building Clear Lake Sporting Goods' integrated statements

Clear Lake (the OpenStax running example) had:
- Prior year retained earnings: $15,000
- Current year net income: $35,000
- Current year dividends: $30,000

The statement of equity shows:
- Beginning RE: $15,000
- + Net income: $35,000
- − Dividends: $30,000
- = Ending RE: $20,000

The current-year balance sheet should show retained earnings of $20,000. If it shows anything else, there's an error.

Now check cash. The cash flow statement showed:
- Beginning cash: $90,000
- Net cash from operations: $53,600
- Net cash used in investing: −$18,600
- Net cash from financing: −$15,000
- Net change in cash: $20,000
- Ending cash: $110,000

The current-year balance sheet should show cash of $110,000. If it shows anything else, there's an error.

The point of the exercise is not the numbers. It's the discipline of *checking* them. As an analyst, when something looks off in a 10-K, the linkages between statements are where you start.

### Common misconceptions

- *"You can analyze a firm from one statement."* Some analysts try; the result is partial. Skipping the cash flow statement, in particular, hides the firm's actual cash performance.
- *"The statements are derived in isolation."* They are derived together. Net income doesn't get computed without consequences for the balance sheet and cash flow.

---

## Concept 3 — Common-size analysis: comparing across size

Two firms in the same industry can have very different absolute numbers. Apple's revenue in a recent year was roughly $400 billion. A small competitor's revenue might be $4 billion — one one-hundredth the scale. Comparing line items in dollars produces useless answers; Apple spends 100× more on R&D than the competitor, but that's not the meaningful comparison.

**Common-size analysis** (also called *vertical analysis*) restates each line of a financial statement as a percentage of a base item. For income statements, the base is usually net sales. For balance sheets, the base is usually total assets.

The result: two firms of vastly different sizes can be compared on the same page.

### Common-size income statement

Each line as a percentage of net sales.

| Line item | Apple (illustrative) | Smaller competitor |
|---|---|---|
| Net sales | 100% | 100% |
| Cost of sales | 56% | 65% |
| **Gross profit** | **44%** | **35%** |
| R&D | 7% | 5% |
| SG&A | 6% | 12% |
| **Operating income** | **31%** | **18%** |
| Net income | 26% | 13% |

A few stories pop out immediately. Apple has a structurally higher gross margin (44% vs. 35%) — it sells higher-priced products with lower per-unit costs as a fraction of price. Apple's SG&A is half the competitor's as a percentage of sales — operational leverage from its scale and brand. Apple converts roughly twice as many cents per dollar of revenue into net income (26% vs. 13%) — a much more profitable business.

These are real economic insights, not just accounting curiosities. They tell you something about pricing power, cost structure, and operating efficiency that the absolute dollar figures hide.

### Common-size balance sheet

Each line as a percentage of total assets.

| Line item | Firm A | Firm B |
|---|---|---|
| Cash & marketable securities | 18% | 5% |
| Accounts receivable | 6% | 12% |
| Inventory | 9% | 22% |
| **Total current assets** | **45%** | **42%** |
| PP&E (net) | 25% | 38% |
| Goodwill & intangibles | 22% | 8% |
| **Total assets** | **100%** | **100%** |
| Accounts payable | 12% | 18% |
| **Total current liabilities** | **20%** | **35%** |
| Long-term debt | 30% | 22% |
| **Total liabilities** | **55%** | **62%** |
| **Total equity** | **45%** | **38%** |

Firm A has more cash, less inventory, more goodwill (suggesting a history of acquisitions), less debt, and more equity. Firm B has more receivables and inventory (perhaps slower-collecting customers, perhaps more inventory-intensive operations), more debt, less equity.

Common-size analysis surfaces these structural differences without requiring you to scale or remember the absolute dollar numbers.

### Industry comparison — the move that matters

The most useful common-size analysis compares a firm to its industry peers. Two firms that look unusual in isolation can both be normal for their industry; a firm that looks normal in isolation can be unusual when compared to peers.

For the equity research project: build a common-size income statement and balance sheet for your chosen company. Then build the same for two or three peer firms. Compare. Where does your firm sit relative to peers on gross margin, SG&A intensity, capex intensity, leverage? Where does it look unusually profitable or unusually leveraged? These are the questions a research report answers.

### Operating cash flow and free cash flow — beyond the statements

Two derived metrics deserve special attention because they appear constantly in equity research.

**Operating cash flow (OCF)** is cash from operations as reported on the cash flow statement. It is the most direct measure of how much cash the firm's core business generates each year, after working capital changes. For a stable firm, OCF should track net income reasonably closely; large persistent gaps between OCF and net income — in either direction — are signals worth investigating.

**Free cash flow (FCF)** subtracts capital expenditures from operating cash flow:

$$\text{FCF} = \text{OCF} - \text{Capex}$$

FCF is what's left after the firm has paid for its operations *and* maintained or grown its productive assets. This is the cash genuinely available to be returned to capital providers — debt holders (interest and principal repayment), equity holders (dividends and buybacks), or simply held on the balance sheet.

Most equity valuation models in this book — including the DCF model in Chapter 11 — discount FCF, not net income. The reason is simple: FCF is real cash that can be paid out. Net income is an accounting figure that includes noncash items and may not be available to distribute.

For the project: compute OCF and FCF for your chosen company over the past five years. Plot them. Are they growing, shrinking, volatile? Does FCF cover dividends and buybacks, or does the firm rely on debt issuance to fund returns to shareholders? These questions feed directly into the report's investment thesis.

### The trade-off (concept 3)

Common-size analysis trades **absolute precision against comparability**. You lose information about scale (Apple is 100× the competitor's size, period). You gain the ability to compare structure and ratios across firms and over time. For an analyst trying to decide whether a firm's gross margin is high or low, the *level* (44% vs. 35%) is more informative than the absolute dollar amount. The trade-off is favorable for almost every comparative question.

### Worked example — Clear Lake vs. Charlie's Camping World

The OpenStax source compares Clear Lake Sporting Goods (a small retailer) with Charlie's Camping World (a competitor about 7× larger). On a common-size basis:

| Line | Clear Lake | Charlie's |
|---|---|---|
| Net sales | 100% | 100% |
| COGS | 50% | 59% |
| Rent | 5% | 11% |
| Salaries | 5% | 12% |
| Depreciation | 4% | (lower) |
| **Operating income** | 36% | (lower) |

Clear Lake has lower COGS as a percentage of sales (better pricing or better procurement), lower rent (more efficient real estate use), and lower labor (fewer staff per dollar of sales). Charlie's is bigger but, by these measures, structurally less profitable. This is exactly the kind of comparison the project produces in Chapter 6 (ratios) and refines in Chapter 11 (valuation).

### Common misconceptions

- *"Higher percentages are always better."* Not necessarily. Higher cash as percentage of assets might mean strong liquidity or might mean management is hoarding cash that should be returned to shareholders. Context matters.
- *"Common-size analysis works across industries."* Less reliably. Inventory-intensive retailers, capital-intensive manufacturers, and asset-light software firms have structurally different common-size profiles. Compare within an industry; cross-industry comparisons require more care.

---

## Synthesis — the four statements as the analyst's instrument

The four statements are the substrate. Income statement, balance sheet, statement of stockholders' equity, cash flow statement — each one a partial view, all four together a working picture of the firm. Reading them is not optional; it is the foundational technical skill of equity research.

This chapter taught what each statement measures, how they connect, and how to make them comparable across firms via common-size analysis. We did not yet *interpret* what the numbers mean. That is the job of Chapter 6 (ratio analysis) and the chapters on valuation that follow.

For the running project, the deliverable from this chapter is concrete:

1. Locate and read your chosen company's most recent 10-K, including all four statements.
2. Verify the linkages — net income flows into retained earnings; ending cash matches the balance sheet.
3. Build a common-size income statement and balance sheet for the past three years.
4. Compute OCF and FCF for the past five years.

When all of that is done, you have the raw material for everything that follows.

---

## Exercises

### Warm-up

**5.1** Name the four primary financial statements and what each one measures. Which one is a snapshot in time, and which one is a measurement over a period?

**5.2** Define EBITDA. Give one reason an analyst might prefer EBITDA over net income, and one reason an analyst should be skeptical of EBITDA as a measure.

**5.3** Distinguish operating cash flow from free cash flow. Which is used for valuation? Which is reported directly on the cash flow statement?

### Application

**5.4** A firm has the following data for the year:

- Beginning cash: $50 million
- Net income: $30 million
- Depreciation: $10 million
- Increase in accounts receivable: $5 million
- Decrease in inventory: $3 million
- Increase in accounts payable: $2 million
- Capital expenditures: $20 million
- Dividends paid: $8 million
- Issuance of long-term debt: $15 million

(a) Compute operating cash flow (indirect method).
(b) Compute investing cash flow.
(c) Compute financing cash flow.
(d) Compute the change in cash and the ending cash balance.
(e) Compute free cash flow.

**5.5** Construct a common-size income statement from the following two firms' data (in $ millions):

| Line | Firm X | Firm Y |
|---|---|---|
| Net sales | 800 | 4,500 |
| COGS | 480 | 2,250 |
| SG&A | 100 | 720 |
| R&D | 80 | 90 |
| Operating income | 140 | 1,440 |

Compare. Which firm has stronger gross margin? Stronger SG&A discipline? Stronger overall operating margin?

**5.6** Locate your chosen company's most recent 10-K on EDGAR. For the most recent fiscal year:

(a) Find the income statement, balance sheet, and cash flow statement.
(b) Compute net income, total assets, and operating cash flow.
(c) Verify that the change in cash on the cash flow statement matches the change in the cash balance on the balance sheet.

### Synthesis

**5.7** A firm reports growing net income but declining cash from operations over the past three years. Construct three plausible explanations and explain how you would distinguish them by reading the firm's 10-K.

**5.8** Apple has, for years, generated FCF substantially larger than its dividend payments and stock buybacks combined, building up a cash pile of nearly $200 billion. Argue (a) why Apple might be doing this rather than returning more cash to shareholders, and (b) what an analyst should say about it in an equity research report. Defend a position.

### Challenge

**5.9** A firm's accounts receivable balance grows from 10% of revenue to 18% of revenue over three years, while revenue itself grows steadily. List four possible explanations, ranging from benign (rapid growth in customer base) to alarming (revenue recognition manipulation). For each, identify what footnote or other disclosure would help you distinguish.

**5.10** Build a common-size balance sheet for your chosen company for the most recent three years. Which line items have moved most as a percentage of total assets? What does the movement suggest about the firm's evolution? Cross-check with the MD&A section of the 10-K to see whether management discusses the same items.

---

## Chapter summary

- Four primary statements: income statement (period), balance sheet (point in time), statement of stockholders' equity (changes in equity), cash flow statement (changes in cash).
- The statements are linked. Net income from the income statement flows through the statement of equity into the balance sheet's retained earnings. The cash flow statement reconciles to the balance sheet's cash line.
- The balance sheet uses historical cost, contains estimates, is a point-in-time snapshot, and excludes most internally generated intangibles. These are structural limitations to keep in mind.
- The cash flow statement has three sections: operating, investing, financing. Their sum is the change in cash for the period.
- **Common-size analysis** restates statements as percentages of a base (net sales for income statement, total assets for balance sheet), enabling comparison across firms of different sizes.
- **Operating cash flow** is from the cash flow statement; **free cash flow** subtracts capex. FCF is the standard input to valuation.

---

## What would change my mind

The chapter argues that the four-statement system is the right framework for analyzing public companies, and that common-size analysis is the right tool for cross-firm comparison. The reading would have to revise if (a) accounting standards moved away from the four-statement framework toward something more integrated (some IFRS proposals have moved in this direction), or (b) empirical evidence emerged that common-size ratios are systematically misleading because of industry-mix effects (this is a real concern but doesn't displace the chapter's claim — it qualifies it).

## Still puzzling

The real tension I haven't resolved cleanly is the gap between **GAAP/IFRS reported numbers** and **management-reported "adjusted" numbers**. Most large public companies report a pile of non-GAAP measures — adjusted EBITDA, free cash flow ex-something, normalized earnings — in addition to the GAAP statements. The non-GAAP numbers are sometimes more economically meaningful (they back out one-time charges that distort GAAP earnings) and sometimes less (they exclude real expenses like stock-based compensation that materially deplete shareholder value). Distinguishing the two requires judgment, and the judgment isn't always easy. The chapter gestures at this; the project will engage it more deeply in Chapter 6 and the valuation chapters.

---

## Connections forward

- **Chapter 6** computes ratios from these statements — liquidity, leverage, profitability, efficiency, market.
- **Chapter 11** uses cash flow statement data for DCF valuation.
- **Chapter 16** uses the income statement and balance sheet to evaluate capital budgeting decisions.
- **Chapter 17** uses balance-sheet capital structure for WACC computation.
- **Chapter 18** uses all four statements as the substrate for pro forma forecasting.

---

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

**Mary T. Washington** was first Black woman CPA in the US (1943) — trained hundreds of accountants and shaped early small-business financial reporting.

**Run this:**

```
Who is Mary T. Washington, and how does their work connect to financial statements we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about their career or ideas.
```

→ Search **"Mary T. Washington"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to apply Mary T. Washington's framework to a specific finance question.
- Add a constraint: "Answer including criticisms or limits of Mary T. Washington's framework."

What changes? What gets better? What gets worse?
