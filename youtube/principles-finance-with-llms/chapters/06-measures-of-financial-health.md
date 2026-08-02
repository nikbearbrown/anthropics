# Chapter 6 — Measures of Financial Health

**Suggested titles**
1. Five Families of Ratios
2. What the Numbers Mean
3. From a 10-K to a Diagnosis

**TL;DR.** A 10-K is a pile of numbers. Ratios are the lenses that turn those numbers into a diagnosis: can the firm pay its bills, manage its assets, cover its debt, generate returns, and at what valuation. This chapter introduces the five families of ratios — efficiency, liquidity, solvency, market value, profitability — and the DuPont decomposition that reveals what's actually driving a company's return on equity.

---

## The puzzle of one identical number

Two firms each report $30 million of net income for the year. Same number, same income statement line.

The first firm is a small specialty retailer with $100 million of revenue and $80 million of total assets. Net income of $30 million on that base means the firm earned 30 cents of profit on every dollar of revenue and 37.5 cents on every dollar of assets. By any measure, it is an extraordinary business.

The second firm is a large industrial manufacturer with $50 billion of revenue and $80 billion of total assets. Net income of $30 million on *that* base means the firm earned 0.06 cents of profit on every dollar of revenue and 0.04 cents on every dollar of assets. By any measure, it is a failing business.

**Same net income. Opposite stories.** What separates them is *scale*, and ratios are how analysts make the comparison meaningful.

The four statements you learned to read in Chapter 5 produce dozens of numbers per company. Reading the numbers is necessary but not sufficient. Turning them into a diagnosis — *can this company pay its bills, manage its inventory, cover its debt, generate returns?* — is what ratio analysis does. Every quarter, every research analyst on Wall Street builds and updates a ratio table for every company they cover. By the end of this chapter, you will have built one for your chosen company.

For the equity research project, this chapter delivers Section 4 of your final report: a complete ratio analysis comparing your company to its industry peers and historical trends.

---

## Learning objectives

After working through this chapter, you should be able to:

- State and compute the four major efficiency ratios (accounts receivable turnover, total asset turnover, inventory turnover, days' sales in inventory).
- Compute the three liquidity ratios (current, quick, cash) and explain when each is most informative.
- Compute the three core solvency ratios (debt-to-assets, debt-to-equity, times interest earned) and assess a firm's leverage.
- Compute the three market-value ratios (EPS, P/E, book value per share) and discuss their limitations.
- Compute profitability ratios (profit margin, ROA, ROE) and decompose ROE using the DuPont method.
- Read a complete set of ratios for a real public company and compare to industry benchmarks.

**Prerequisites.** Chapter 5 (the four financial statements). Comfort with division.

---

## Concept 1 — What a ratio is, and why it beats raw numbers

A **financial ratio** is the quotient of two numbers, both of which come from the firm's financial statements. That is the whole technical definition. Net income divided by revenue. Current assets divided by current liabilities. The simplicity of the construction is the source of its power.

A ratio does three things that raw numbers do not.

**It controls for scale.** As the opening puzzle illustrated, $30 million of net income is meaningless without context. Net income divided by revenue (profit margin) tells you something about the firm's pricing efficiency that scales across firms of any size. This is why ratios are the language of cross-firm comparison.

**It surfaces relationships.** Some ratios pair items from different statements — net income from the income statement divided by total assets from the balance sheet, for instance. The ratio measures something neither statement alone tells you: how productively the firm's asset base generates earnings.

**It enables benchmarking.** Industry averages, peer comparisons, historical trends — all of these are expressed in ratios. A debt-to-equity ratio of 1.5 is meaningless in isolation; compared to an industry average of 0.8, it tells you the firm is significantly more leveraged than peers. Compared to its own history of 0.5, it tells you the firm is leveraging up.

### Five families of ratios

Ratios are organized into five families based on what financial dimension they measure.

| Family | What it measures | Key stakeholder |
|---|---|---|
| **Efficiency** | How well the firm uses its assets | Internal management, operators |
| **Liquidity** | Can the firm pay short-term bills? | Suppliers, short-term creditors |
| **Solvency** | Can the firm pay long-term debt? | Long-term creditors, bondholders |
| **Market value** | What is the stock worth, and why? | Investors, equity analysts |
| **Profitability** | How much earnings come from operations and capital? | All stakeholders |

The five categories overlap. Profitability and efficiency are connected through the DuPont decomposition (we'll get to it). Solvency and liquidity both touch the firm's ability to meet obligations, just at different time horizons. Market-value ratios depend on profitability ratios. Treat the five as views into one connected reality, not as five separate boxes.

### What ratios cannot do

Ratios have limitations that an honest analyst doesn't paper over.

**Past performance is not future performance.** A firm with three years of expanding profit margin can have its margin collapse in year four if competitors enter the market or input costs rise. Ratios describe what has been; they do not predict what will be.

**Accounting choices distort comparability.** Two firms using different inventory accounting methods (FIFO vs. LIFO), different depreciation methods, or different revenue-recognition policies can show very different ratios for genuinely similar businesses. The footnotes tell you what the firm chose; reading them is part of the work.

**Industry context is everything.** A current ratio of 0.8 is alarming for a manufacturer and unremarkable for a fast-food chain (which collects cash daily and pays suppliers on net-30 terms). The same number, opposite implications. Ratios should always be interpreted against industry norms.

**One ratio in isolation is rarely enough.** A firm can look healthy on liquidity and disastrous on solvency, or strong on profit margin and weak on asset turnover. The diagnosis comes from the *system* of ratios, not from any single number.

↳ **Dig Deeper — Industry-specific ratio benchmarks**

*"What's a good current ratio?" depends entirely on the industry. Restaurants, with negative working capital, can run current ratios below 0.5 and be perfectly healthy. Construction firms with current ratios of 11 are not unusually healthy — they're capital-tied-up. Knowing the industry-specific benchmarks is what separates analysts from list-checkers.*

**Prompt:**
> For three contrasting industries (restaurants, big-box retail, construction), give typical ranges for current ratio, debt-to-equity, profit margin, asset turnover, and ROE. Explain *why* each industry's typical ratios are what they are — what business-model features produce those benchmarks. Then give one example of a firm in each industry whose ratios are unusual, and explain what the deviation might mean.

**What to do with the output:** Save it. When comparing your project company's ratios to peers, you need industry-specific benchmarks; this is one cheap way to build a starting reference.

### The trade-off (concept 1)

Ratios trade **specificity against generalizability**. They reduce a firm's complex financial reality to a small number of comparable values. The reduction makes comparison possible. The reduction also throws away information — context, qualitative factors, accounting policies — that a thorough analyst recovers by reading the rest of the 10-K. Ratios are the starting point for analysis, never the end of it.

### Worked example — same number, three ratios

Take Apple's roughly $400 billion of recent annual revenue and roughly $100 billion of net income. Three ratios:

- **Profit margin** = $100B / $400B = 25%. Apple converts a quarter of every revenue dollar into bottom-line profit.
- **Asset turnover** = $400B / $360B (recent total assets) ≈ 1.1. Apple generates $1.10 of revenue per dollar of assets.
- **Return on assets** = $100B / $360B ≈ 28%. Apple earns 28 cents of profit per dollar of assets per year.

Same firm, three ratios, three different stories: pricing power, asset efficiency, and asset productivity. The ratio table tells you what the income statement and balance sheet alone do not.

---

## Concept 2 — The five families, with formulas

We work through the five families in the order they typically appear in an analyst's ratio table.

### Family 1 — Efficiency (asset utilization)

Efficiency ratios measure how well the firm uses its assets to generate revenue.

**Accounts receivable turnover** — how many times per year the firm collects its receivables.

$$\text{AR Turnover} = \frac{\text{Net Credit Sales}}{\text{Average Accounts Receivable}}$$

A high ratio means quick collection (good for liquidity, may indicate tight credit terms that exclude marginal customers). A low ratio means slow collection (cash tied up in receivables, possibly poor collection practices, possibly higher bad debt).

For a firm with $100M of credit sales and average receivables of $25M, the ratio is 4 — meaning the firm collects its receivables about four times per year, or about every 90 days.

**Total asset turnover** — how much revenue the firm generates per dollar of assets.

$$\text{Asset Turnover} = \frac{\text{Net Sales}}{\text{Average Total Assets}}$$

Higher means more revenue per asset. Capital-intensive industries (heavy manufacturing, utilities) have low asset turnover by structure; software and services firms typically have high turnover. Compare within an industry, never across.

**Inventory turnover** — how many times per year the firm sells through its inventory.

$$\text{Inventory Turnover} = \frac{\text{Cost of Goods Sold}}{\text{Average Inventory}}$$

A high ratio means inventory is sold quickly (good — less cash tied up, less obsolescence risk; bad — possible stockout risk and lost sales). A low ratio means slow-moving inventory (possible overstocking or product obsolescence).

**Days' sales in inventory** — how many days the firm holds inventory before selling it.

$$\text{Days' Sales in Inventory} = \frac{\text{Ending Inventory}}{\text{COGS}} \times 365$$

This is the inventory turnover expressed in days. A grocery chain might have 20–30 days; an aerospace manufacturer might have 200–300 days. Industry context dictates everything.

For the project: compute these four for your chosen company over the past three years. Trend matters as much as level. A firm whose inventory turnover is falling from 6 to 4 to 3 over three years is accumulating inventory faster than it's selling — a serious warning, especially if revenue isn't growing proportionally.

### Family 2 — Liquidity

Liquidity ratios measure the firm's ability to pay short-term obligations.

**Current ratio** — total current assets divided by current liabilities.

$$\text{Current Ratio} = \frac{\text{Current Assets}}{\text{Current Liabilities}}$$

A ratio of 2.0 means current assets are twice current liabilities. Generally, ratios above 1.0 indicate a buffer for short-term obligations. Above 2.0 may indicate excess current assets sitting unproductively.

**Quick ratio (acid-test ratio)** — current assets minus inventory and prepaid expenses, divided by current liabilities.

$$\text{Quick Ratio} = \frac{\text{Cash} + \text{Short-Term Investments} + \text{Accounts Receivable}}{\text{Current Liabilities}}$$

The quick ratio strips out the slowest-converting current assets. Inventory may take months to convert to cash; prepaid expenses may never convert at all. The quick ratio asks: can the firm meet current liabilities from genuinely liquid assets? A quick ratio above 1.0 is comfortable.

**Cash ratio** — the most conservative measure.

$$\text{Cash Ratio} = \frac{\text{Cash and Cash Equivalents}}{\text{Current Liabilities}}$$

A cash ratio of 1.0 means the firm could pay all current liabilities entirely from cash on hand. Most healthy firms run cash ratios well below 1.0 — sitting on enough cash to cover all near-term liabilities is usually inefficient. Apple is an exception, with cash and securities exceeding current liabilities by a wide margin; that profile is unusual and reflects deliberate corporate strategy.

For the project: liquidity ratios are typically the easiest to compute and the first an analyst checks. A firm with a current ratio below 1.0 and limited access to credit is at imminent risk of bankruptcy.

### Family 3 — Solvency

Solvency ratios measure the firm's ability to meet long-term debt obligations.

**Debt-to-assets ratio** — what fraction of assets is financed by debt.

$$\text{Debt-to-Assets} = \frac{\text{Total Liabilities}}{\text{Total Assets}}$$

A debt-to-assets ratio of 0.6 means 60% of the firm's assets are financed by creditors; 40% by equity. Higher ratios indicate higher leverage and higher financial risk.

**Debt-to-equity ratio** — debt as a multiple of equity.

$$\text{Debt-to-Equity} = \frac{\text{Total Liabilities}}{\text{Total Equity}}$$

A debt-to-equity ratio of 1.5 means $1.50 of debt for every $1 of equity. The two solvency ratios — debt-to-assets and debt-to-equity — contain mathematically equivalent information; you can derive one from the other. Practitioners use whichever is more familiar in their industry.

**Times interest earned (TIE)** — how comfortably operating profits cover interest expense.

$$\text{TIE} = \frac{\text{EBIT}}{\text{Interest Expense}}$$

A TIE ratio of 5 means operating profits are five times the firm's interest obligations. Lenders and bond rating agencies watch this ratio carefully. A TIE below 1.5 is concerning; below 1.0 means the firm cannot cover interest from operating earnings — a near-term default risk.

For the project: bond covenants in many corporate debt agreements impose minimum TIE requirements. If a firm's TIE drops below the covenant level, the lender can call the debt or impose penalties. Read the 10-K's debt footnotes for covenant terms.

### Family 4 — Market value

Market-value ratios connect the stock price to the firm's financials. They are the bridge between accounting and investment analysis.

**Earnings per share (EPS)** — net income per common share.

$$\text{EPS} = \frac{\text{Net Income} - \text{Preferred Dividends}}{\text{Weighted Average Common Shares Outstanding}}$$

Public companies are required to report two versions: **basic EPS** (the formula above) and **diluted EPS** (which adjusts the share count to include shares that *could* be issued through stock options, convertible securities, etc.). Diluted EPS is usually slightly lower and is the more conservative measure.

A subtlety worth naming: a firm can increase EPS without increasing earnings simply by **buying back its own stock**. Reducing the share count raises EPS mechanically. This is one reason why many large public companies — Apple is the most aggressive — have buyback programs at the scale of tens of billions of dollars per year. The buybacks are economically equivalent to dividends but increase EPS in the process. Whether this is good capital allocation or executive compensation engineering depends on how the firm's stock is priced relative to its intrinsic value at the time of repurchase. A buyback at a price above intrinsic value destroys shareholder value.

**Price-to-earnings (P/E) ratio** — how much investors pay per dollar of earnings.

$$\text{P/E} = \frac{\text{Market Price per Share}}{\text{EPS}}$$

A P/E of 20 means investors are paying $20 for each $1 of annual earnings. Implicit assumption: the earnings will continue, and there's reason to think they may grow. Two flavors are common:

- **Trailing P/E (P/E TTM)** — uses the past twelve months' EPS.
- **Forward P/E** — uses analysts' consensus estimate of next year's EPS.

Forward P/E is what most equity research uses. A forward P/E meaningfully below the firm's industry average suggests the market is pricing the firm's earnings as less reliable or less growth-oriented; meaningfully above suggests the market expects faster-than-peer growth.

**Book value per share** — accounting equity divided by share count.

$$\text{Book Value per Share} = \frac{\text{Total Equity} - \text{Preferred Equity}}{\text{Common Shares Outstanding}}$$

Compared to market price per share, book value per share gives the **price-to-book (P/B) ratio**. A P/B above 1 means the market values the firm at more than its accounting equity — the market is implicitly pricing intangibles (brand, IP, growth opportunities) that the balance sheet doesn't capture. A P/B below 1 means the market values the firm at less than its accounting equity — possibly undervalued, possibly the market is signaling that reported book value is overstated.

For the project: market-value ratios are how you connect your analysis to the actual share price. Chapter 11 builds the DCF model that produces an *intrinsic* value estimate; comparing intrinsic value to market value (and to peers' P/E and P/B ratios) is the bridge to a Buy/Hold/Sell call.

### Family 5 — Profitability

Profitability ratios measure how much profit the firm generates from its operations and capital.

**Profit margin** — net income as a percentage of revenue.

$$\text{Profit Margin} = \frac{\text{Net Income}}{\text{Net Sales}}$$

Apple's profit margin runs around 25%. Walmart's runs around 2–3%. Both are extraordinarily successful firms; the difference reflects radically different business models. Compare within industries.

**Return on assets (ROA)** — net income as a percentage of average assets.

$$\text{ROA} = \frac{\text{Net Income}}{\text{Average Total Assets}}$$

ROA tells you how productively the firm's asset base generates earnings. It captures both pricing efficiency (margin) and asset efficiency (turnover) in one number.

**Return on equity (ROE)** — net income as a percentage of average equity.

$$\text{ROE} = \frac{\text{Net Income} - \text{Preferred Dividends}}{\text{Average Common Equity}}$$

ROE is the single most-watched profitability metric in equity analysis. It tells you what the firm earns on the capital that common shareholders have invested. Industry averages vary enormously — a 2020 snapshot showed market average around 8%, with ranges from negative 47% (air transportation, COVID-affected) to over 70% (some health-care subsegments). For a stable industrial firm, ROE in the high teens or twenties is strong. For a software firm with light asset bases, ROE above 30% is achievable.

ROE can be inflated by leverage — financing the firm with debt rather than equity reduces the equity denominator and raises ROE without changing operating performance. This is where DuPont decomposition becomes essential.

↳ **Dig Deeper — Earnings-quality red flags**

*Beyond the standard ratios, equity analysts watch for specific quantitative signals that reported earnings may be lower-quality than they appear. The Beneish M-score and Piotroski F-score are the academic versions; in practice, analysts look at simpler signals.*

**Prompt:**
> Explain what each of these earnings-quality red flags would suggest if observed in a public company's financials: (1) growing accounts receivable as a percentage of revenue, (2) declining cash conversion (cash from operations vs. net income), (3) increasing days inventory, (4) rising "other income" or non-recurring items as a share of net income, (5) frequent accounting policy changes. Then briefly describe the Beneish M-score model — what variables it uses and what cutoff value flags potential earnings manipulation.

**What to do with the output:** Save it as your earnings-quality checklist for any company you analyze. Apply it routinely.

### The trade-off (concept 2)

Each family of ratios trades **completeness against focus**. Liquidity ratios tell you about short-term survival; solvency about long-term survival; profitability about returns; efficiency about asset use; market-value about how the market is pricing all of it. No single ratio tells you everything; the *combination* gives you the diagnosis. The discipline is to look at all five families before forming a judgment.

### Worked example — Clear Lake's complete ratio table

The OpenStax running example, Clear Lake Sporting Goods, with current-year data: net sales $120,000, net income $35,000, total assets $250,000, total equity $100,000, EBIT $43,000, interest expense $2,000.

| Family | Ratio | Value |
|---|---|---|
| Efficiency | Total asset turnover | 0.53 ($120K / $225K avg) |
| Efficiency | Inventory turnover | 1.6 ($60K / $37.5K) |
| Efficiency | Days' sales in inventory | 243 days |
| Efficiency | AR turnover | 4 times |
| Liquidity | Current ratio | 2.0 |
| Liquidity | Quick ratio | 1.6 |
| Liquidity | Cash ratio | 1.1 |
| Solvency | Debt-to-assets | 60% |
| Solvency | Debt-to-equity | 1.5 |
| Solvency | Times interest earned | 21.5 |
| Profitability | Profit margin | 29% |
| Profitability | ROA | 16% |
| Profitability | ROE | 32% |
| Market | EPS | $3.75 |
| Market | P/E | 18.5 |
| Market | Book value per share | $10.00 |

Reading the table: Clear Lake is a profitable, well-capitalized, moderately-leveraged firm. Liquidity is comfortable. Solvency is strong (TIE of 21.5 means interest is easily covered). Profitability is strong by most retail benchmarks. The one warning sign: 243 days' sales in inventory is high for a sporting-goods retailer; the firm may be over-stocked. Inventory turnover of 1.6 is correspondingly low.

This is what an analyst's ratio table looks like. For the project, you'll build the same table for your chosen company.

### Common misconceptions

- *"Higher is always better."* Not for liquidity (excess cash is unproductive), not for inventory turnover (too high means stockouts), and not for leverage (depends on the cost of debt vs. return on assets).
- *"Industry averages are the truth."* They are baselines. A firm above or below the industry average isn't necessarily better or worse — sometimes a firm has good reasons to deviate.
- *"All ratios are equally important."* The most important ratios depend on the firm and the question. For a high-growth tech firm, asset turnover and profitability matter more than liquidity. For a distressed firm, liquidity matters most.

---

## Concept 3 — DuPont decomposition: what's actually driving ROE

ROE is a single number that bundles three different things together. The DuPont decomposition pulls them apart.

### The DuPont identity

Start with the standard ROE formula:

$$\text{ROE} = \frac{\text{Net Income}}{\text{Equity}}$$

Multiply numerator and denominator by sales and by total assets:

$$\text{ROE} = \frac{\text{Net Income}}{\text{Sales}} \times \frac{\text{Sales}}{\text{Total Assets}} \times \frac{\text{Total Assets}}{\text{Equity}}$$

Each fraction is itself a ratio you've already met:

$$\text{ROE} = \text{Profit Margin} \times \text{Asset Turnover} \times \text{Equity Multiplier}$$

The equity multiplier (total assets over total equity) is leverage expressed as a different ratio. A firm with no debt has an equity multiplier of 1.0; a firm financed half with debt and half with equity has an equity multiplier of 2.0.

### What DuPont reveals

The decomposition surfaces the three drivers of ROE:

- **Profit margin** (operating efficiency) — how much of each sales dollar becomes profit.
- **Asset turnover** (asset efficiency) — how much sales each dollar of assets generates.
- **Equity multiplier** (financial leverage) — how much of the asset base is financed by debt rather than equity.

Two firms with identical 25% ROE can be very different businesses.

**Firm A**: profit margin 10%, asset turnover 1.0, equity multiplier 2.5. ROE = 25%. A leveraged business with moderate margins and moderate asset use.

**Firm B**: profit margin 25%, asset turnover 1.0, equity multiplier 1.0. ROE = 25%. An unleveraged business with very high margins.

Firm A is generating its returns substantially through leverage. If interest rates rise or business deteriorates, Firm A's returns can collapse quickly. Firm B's returns are coming from operational excellence and survive a rate hike better.

This is the analytical move DuPont enables. ROE in isolation hides the structure; DuPont surfaces it.

### Three-step DuPont, five-step DuPont

The three-step decomposition above is the basic version. A five-step version splits the profit margin into operating margin and the tax-and-interest burden, and splits the equity multiplier into operating-asset and financial-asset components. Five-step DuPont is more revealing for highly leveraged firms (banks, insurers) but is overkill for most general analysis. Three-step is the standard.

### Worked example — DuPont on a real firm

Consider a hypothetical industrial firm with:
- Net sales: $5,000M
- Net income: $400M
- Total assets: $4,000M (average)
- Total equity: $1,500M (average)

Direct ROE: $400M / $1,500M = 26.7%.

DuPont:
- Profit margin: $400M / $5,000M = 8%
- Asset turnover: $5,000M / $4,000M = 1.25
- Equity multiplier: $4,000M / $1,500M = 2.67

ROE = 8% × 1.25 × 2.67 = 26.7% ✓

The decomposition tells you the firm earns 8 cents per dollar of revenue (modest margins typical of industrial businesses), generates $1.25 of revenue per dollar of assets (decent asset productivity), and uses $2.67 of assets per dollar of equity (significant leverage). The 26.7% ROE comes substantially from the leverage. A peer with the same margin and turnover but no debt would have ROE of 8% × 1.25 × 1.0 = 10%. The leverage adds 17 percentage points.

### Industry context for ROE

A 2020 snapshot of US industry ROEs shows wide variation:

| Industry | ROE |
|---|---|
| Health-care facilities | ~70% |
| Financial services (non-bank) | ~64% |
| Auto retail | ~36% |
| Grocery retail | ~31% |
| Software (systems & applications) | ~28% |
| Online retail | ~27% |
| **Total market average** | **~8%** |
| Banking | ~8% |
| Computer services | ~14% |
| Recreational products | ~13% |
| Real estate (general) | ~2% |
| Air transportation | **−47%** (pandemic-affected) |
| Hotels/gaming | **−30%** |

`[verify]` for any of these for current vintage; industry averages vary year to year.

A firm's ROE should always be read against its industry, not the market average. A 13% ROE for a recreational-products company is *above* its industry average and impressive. A 13% ROE for a software firm is *below* its industry average and concerning.

### The trade-off (concept 3)

DuPont decomposition trades **simplicity against insight**. The single ROE number is easier to communicate; the three-component decomposition is more diagnostic. For external communication (a research-report headline number), single ROE is fine. For analytical work, DuPont is essential. The decomposition is what tells you whether ROE is sustainable or fragile.

### Worked example — applying ratio analysis to your project company

For the equity research project, the deliverable from this chapter is a complete ratio table for your chosen company with three years of historical data, plus a peer comparison. The analytical sequence:

1. **Pull the financial statements** for the past three fiscal years from EDGAR.
2. **Compute every ratio** in the five families, plus the DuPont decomposition of ROE.
3. **Trend analysis**: is each ratio stable, improving, or deteriorating?
4. **Peer comparison**: how does your firm compare to two or three industry peers on the same ratios?
5. **Anomaly investigation**: for any ratio that's far from peer averages, read the relevant section of the MD&A and footnotes. The firm usually explains the anomaly somewhere in the 10-K.
6. **Synthesis**: write a one-paragraph diagnosis of the firm's financial health from the ratios, identifying strengths, weaknesses, and any items requiring further investigation in subsequent chapters.

This becomes Section 4 of your final research report. The work in subsequent chapters — TVM, bond and stock valuation, capital budgeting — depends on having this base in place.

### Common misconceptions

- *"DuPont is just an academic exercise."* It is the standard framework used in equity research and credit analysis. Practitioners use it.
- *"A high equity multiplier is bad."* Not necessarily. Banks have equity multipliers of 10+ by design. Whether high leverage is appropriate depends on the stability of the firm's cash flows.
- *"You can compare DuPont components across industries."* You cannot, cleanly. A bank's profit margin and asset turnover are not comparable to a manufacturer's. Compare components within industry; combine into ROE for cross-industry comparison.

---

## Synthesis — ratios as instruments

The five families of ratios are instruments. Each measures something the income statement and balance sheet do not directly tell you. Used together, they produce a diagnosis.

The diagnosis is not the analysis. It is the foundation for the analysis. Subsequent chapters of this book — TVM (Chapters 7–9), bond and stock valuation (Chapters 10–11), capital budgeting (Chapter 16), capital structure (Chapter 17), forecasting (Chapter 18) — all assume you have the ratio table in front of you. The ratios tell you what kind of firm you are looking at, what its financial position is, what concerns to investigate. The valuation and decision-making chapters that follow tell you what to *do* about that information.

For the running project, this chapter delivers the firm's ratio diagnosis. Subsequent chapters build on it.

---

## Exercises

### Warm-up

**6.1** Name the five families of ratios. For each, name two specific ratios in the family and what they measure.

**6.2** Write the formula for: profit margin, ROA, ROE, current ratio, debt-to-equity, P/E ratio, accounts receivable turnover, days' sales in inventory.

**6.3** Why is a current ratio of 0.8 alarming for a manufacturer but unremarkable for a fast-food chain? What underlying business mechanism explains the difference?

### Application

**6.4** A firm has the following data:

| Item | Value |
|---|---|
| Net sales | $800M |
| COGS | $480M |
| Operating income (EBIT) | $120M |
| Net income | $80M |
| Interest expense | $20M |
| Total assets (average) | $1,000M |
| Total equity (average) | $400M |
| Current assets | $300M |
| Current liabilities | $150M |
| Cash | $80M |
| Inventory (average) | $80M |
| Accounts receivable (average) | $60M |
| Total liabilities | $600M |

Compute:
(a) Current ratio, quick ratio, cash ratio.
(b) Debt-to-assets, debt-to-equity, times interest earned.
(c) Profit margin, ROA, ROE.
(d) Total asset turnover, inventory turnover, AR turnover.
(e) DuPont decomposition of ROE.

**6.5** Two firms in the same industry have the following ROEs:
- Firm X: ROE 25%, profit margin 10%, asset turnover 1.0
- Firm Y: ROE 25%, profit margin 5%, asset turnover 2.5

Each has the same ROE. Which is more financially fragile, and why?

**6.6** Pull three years of financial statements for your chosen company from EDGAR. Compute the complete ratio table for the most recent year. Identify three trends that are improving and three that are deteriorating, if any.

### Synthesis

**6.7** A firm reports steadily increasing EPS over five years, but during the same period, its share count has been falling due to large stock buybacks. Construct two competing arguments: (a) management is creating shareholder value through smart capital allocation, and (b) management is engineering EPS growth without operational improvement. What evidence in the 10-K would distinguish the two?

**6.8** Apple has historically maintained a P/E ratio significantly above the S&P 500 average. Is this evidence that Apple is overvalued, that Apple is genuinely worth a premium, or that the market expects above-average growth? What additional information would help you decide?

### Challenge

**6.9** Build a complete ratio table for your chosen company AND two peer firms in the same industry. Identify the three ratios where your firm differs most from the peer average. For each, hypothesize why and read the MD&A section of the 10-K to test your hypothesis.

**6.10** A firm's DuPont decomposition over five years shows: profit margin steadily declining, asset turnover steadily rising, equity multiplier rising sharply in the past two years. ROE is approximately constant. Construct a narrative explaining what is happening to this firm's business. What kind of strategic shift would produce this pattern? Use a real-world parallel from any industry you know.

---

## Chapter summary

- A **financial ratio** is the quotient of two numbers from the financial statements. Ratios control for scale, surface relationships, and enable benchmarking.
- Five families: **efficiency, liquidity, solvency, market value, profitability.** Each measures a different dimension of financial health.
- **Efficiency:** AR turnover, asset turnover, inventory turnover, days' sales in inventory.
- **Liquidity:** current, quick, cash.
- **Solvency:** debt-to-assets, debt-to-equity, times interest earned.
- **Market value:** EPS, P/E, book value per share.
- **Profitability:** profit margin, ROA, ROE.
- **DuPont decomposition** breaks ROE into profit margin × asset turnover × equity multiplier, surfacing the three drivers of return on equity.
- Industry context is essential. A ratio that is healthy for one industry may be alarming for another.

---

## What would change my mind

The chapter argues that the five-family ratio framework is the right organizing structure for diagnosing a firm's financial health. The reading would have to revise if (a) industry-specific frameworks consistently outperformed the general framework for their industries — there's some evidence for this in financial-firms analysis, where bank-specific ratios (Tier 1 capital, NIM, efficiency ratio) replace much of the general framework — but for general industrials and consumer firms the five families remain the working consensus, or (b) machine-learning approaches to firm classification produced more useful diagnoses than human-readable ratios. Some quantitative funds use this approach; the ratios remain dominant in fundamental analysis.

## Still puzzling

The cleanest tension in the chapter is between **using ratios as a diagnosis** and **using ratios as a screen**. A diagnosis aims to understand a single firm deeply. A screen aims to filter many firms quickly to identify candidates for deeper analysis. The same ratios can serve both purposes, but the rules of interpretation differ. A firm with high leverage might be flagged by a screen and then explained by a diagnosis. A firm with low ROE might fail a screen but pass a diagnosis if the low ROE is the result of conservative balance-sheet management with strong long-term economics. I haven't found a clean way to teach both uses in one chapter without confusing the two; the project's emphasis on a single deep analysis tilts toward diagnosis. Screen-driven analysis is a topic for a later course.

---

## Connections forward

- **Chapter 7–9** install the time-value-of-money arithmetic that turns the firm's cash flows into valuation inputs.
- **Chapter 10** prices the firm's debt using TIE and the cost of debt.
- **Chapter 11** values the firm's equity using DCF, with margin and turnover assumptions inherited from this chapter's ratios.
- **Chapter 16** uses ROA as a benchmark for the firm's hurdle rate in capital budgeting.
- **Chapter 17** uses the firm's leverage and cost of capital to compute WACC.
- **Chapter 18** uses ratio trends as the basis for forecasting future statements.

---

---

## LLM Exercise — Chapter 6: Complete Ratio Analysis

**Project:** Equity Research Report on a Chosen Public Company
**What you're building this chapter:** A complete ratio analysis for your company across all five ratio families, with three years of historical trends and peer benchmarking.
**Tool:** Claude Project (with 10-K and statement summary already in place).

### The Prompt

```
For [your company], using the four-statement summary I built in Chapter 5 and the most recent three 10-Ks (uploaded to this project), produce a complete ratio analysis with the following structure:

### Family 1 — Efficiency
- Total asset turnover (most recent 3 years)
- Inventory turnover (most recent 3 years)
- Days' sales in inventory
- Accounts receivable turnover and DSO

### Family 2 — Liquidity
- Current ratio
- Quick ratio
- Cash ratio

### Family 3 — Solvency
- Debt-to-assets
- Debt-to-equity
- Times interest earned (TIE)

### Family 4 — Profitability
- Profit margin
- Return on assets (ROA)
- Return on equity (ROE)
- DuPont decomposition: ROE = Profit Margin × Asset Turnover × Equity Multiplier

### Family 5 — Market value
- EPS (basic and diluted)
- P/E ratio (using current market price)
- Book value per share
- P/B ratio

### Trend analysis
For each family, identify the 2-3 most important trends across the past three years. Are ratios improving, deteriorating, or stable? What's driving the change?

### Peer comparison
For three peer firms (you choose, or list specific peer tickers if you want me to suggest them), compute the same ratios for the most recent year. How does [your company] compare?

### Diagnosis
Write a one-paragraph synthesis: based on these ratios, what kind of firm is this — high-growth/low-margin, low-growth/high-margin, leveraged/unleveraged, efficient/inefficient? What strengths and weaknesses are visible?

Show your work. If a ratio requires a specific line item, cite where you got the number.
```

### What this produces

A 3-4 page ratio analysis section. Becomes Section 4 of the final report (after company snapshot, governance, and financial summary).

### How to adapt this prompt

- *For your own company:* Replace [your company]. Pick relevant peers in the same industry.
- *For ChatGPT / Gemini:* Identical.
- *For Claude Code:* Could automate the calculations from a CSV of statements, but for one company the manual approach is fine.

### Connection to previous chapters

Builds directly on Chapter 5's statement summary. Feeds Chapter 11's DCF inputs and Chapter 17's WACC capital structure analysis.

### Preview of next chapter

Chapter 7 installs single-payment time-value-of-money. The Chapter 7 LLM Exercise will discount one of your company's known future cash flows.

---

**Tags:** financial-ratios, DuPont-analysis, liquidity, solvency, profitability, market-value-ratios, ROE, financial-analysis


---

## AI Wayback Machine

**Edward Altman** was developed the Z-score in 1968 — the bankruptcy-prediction model that anchors modern financial-health analysis.

**Run this:**

```
Who is Edward Altman, and how does their work connect to measures of financial health we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about their career or ideas.
```

→ Search **"Edward Altman"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to apply Edward Altman's framework to a specific finance question.
- Add a constraint: "Answer including criticisms or limits of Edward Altman's framework."

What changes? What gets better? What gets worse?
