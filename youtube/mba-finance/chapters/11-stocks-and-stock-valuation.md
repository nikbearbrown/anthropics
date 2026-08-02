# Chapter 11 — Stocks and Stock Valuation

*Three methods, none of them right, all of them necessary.*

---

In Chapter 10, we priced a bond. The arithmetic was tight. Known coupon payments. Known principal. Known maturity date. Everything required to compute a present value was written in the bond's contract. The market's only judgment call was what discount rate to apply.

Now try to price a stock.

A share of common stock entitles you to a fractional ownership in the issuing firm. That ownership comes with a vote at shareholder meetings, a residual claim on assets if the firm is liquidated, and a possible stream of dividends the company *may* pay at *whatever amount the board decides* on *whatever schedule they choose*. There is no contractual guarantee of any cash flow at any time. The bond's clean problem — discount contractual payments at an appropriate rate — has been replaced by a genuinely open question: what cash flows will this firm produce, for whom, and when?

Nobody knows. That's not a temporary problem to be resolved with better data. It's the nature of the instrument.

So three families of valuation methods exist, because no single approach captures everything that matters. Each one works on a different principle. Each is right under its own assumptions. Each fails in its own specific way. A serious equity analyst uses all three and reports the range.

This chapter installs all three.

---

## What a stock is

Two things make a stock fundamentally different from a bond.

**No contractual cash flow.** A bond promises explicit coupon and principal payments. Miss one, and the firm is in default. A stock promises nothing. Dividends are at the board's discretion. Capital gains depend on the market's evolving judgment of the firm's prospects. The cash flow stream isn't specified — it has to be forecast.

**Residual claim.** Bondholders are paid first. After interest and principal are satisfied, what's left flows to equity holders — but only what's left. In good years, that's a lot. In bankruptcy, it can be zero. The variability is structural, not accidental.

These two features make stocks both more risky and more potentially rewarding than bonds, and they make valuation a fundamentally judgment-laden exercise.

**Common vs. preferred stock.** Most public companies issue **common stock**. Common shareholders vote at annual meetings (typically one vote per share), receive dividends if and when the board declares them, and have residual claims on assets in liquidation after all creditors and preferred shareholders are paid. They bear the full upside and downside of the firm's performance.

Some firms also issue **preferred stock**, a hybrid with features of both stocks and bonds. Preferred stock pays a *fixed* dividend at a stated rate, has priority over common stock in dividend payments and liquidation, and typically carries no voting rights. Because preferred dividends are fixed and continue indefinitely, preferred stock is a perpetuity — pricing it is the formula from Chapter 8: $P_0 = D / r$.

Common stock is the harder case, and the focus of everything that follows.

---

## The first family: Dividend Discount Models

If a stock pays dividends, one defensible approach is to value it as the present value of all future dividend payments. The general formula:

$$P_0 = \sum_{t=1}^{\infty} \frac{D_t}{(1+r)^t}$$

where $D_t$ is the dividend in year $t$ and $r$ is the required rate of return on equity. This is the present-value machinery from Chapters 7 and 8 applied to an equity stream.

The infinite sum collapses to closed forms when you make assumptions about how dividends behave.

**Zero-growth DDM.** If dividends are constant forever — a perpetuity — then $P_0 = D / r$. This applies cleanly to preferred stock and to mature firms whose dividends have been flat for years.

**The Gordon growth model.** If dividends grow at a constant rate $g$ forever:

$$\boxed{P_0 = \frac{D_1}{r - g}}$$

where $D_1 = D_0 \times (1+g)$ is next year's dividend. This is the growing-perpetuity formula from Chapter 8, applied to dividends. It requires $r > g$ — the same sanity check: a firm can't grow faster than the discount rate forever without the formula breaking down.

Example: a stock pays $5.00 this year, expects dividends to grow at 4% per year forever, and investors require an 8% return. Then $D_1 = \$5.20$, and:

$$P_0 = \frac{\$5.20}{0.08 - 0.04} = \$130$$

The Gordon model is the workhorse of DDM. It applies to mature firms with stable dividend histories — utilities, consumer staples, established financials.

**Sensitivity warning, and it's serious.** With $D_1 = \$5.20$:

| | $g = 4\%$ | $g = 5\%$ |
|---|---|---|
| $r = 8\%$ | $130 | $173 |
| $r = 9\%$ | $104 | $130 |

A one-percentage-point change in growth moves the price 33%. A one-percentage-point change in the required return moves it 20%. These are inputs that analysts disagree about routinely and by more than one point. Never report a Gordon model result as a single number. Report a range.

<!-- → [TABLE: Gordon model sensitivity grid — rows: required return (7%, 8%, 9%, 10%), columns: dividend growth rate (2%, 3%, 4%, 5%, 6%) — student should see how quickly values change near the r = g boundary and where the "safe" region of the model lies] -->

**Two-stage DDM.** Real firms don't grow at a constant rate forever. The two-stage model handles firms transitioning from high growth to mature growth by dividing the future into two periods: an explicit high-growth phase, and then a stable growth rate applied via the Gordon model as a terminal value.

Procedure: project dividends year by year during the high-growth phase; at the end of that phase, compute a terminal value as $TV = D_{n+1} / (r - g_\text{stable})$; discount both the dividends and the terminal value back to today.

Example: a company pays a $14 dividend today, expects 13% growth for five years, then settles at 5% forever. Required return: 12%.

Stage 1 dividends (years 1–5): $15.82, $17.88, $20.20, $22.83, $25.79$.

Terminal value at end of year 5:
$$TV_5 = \frac{25.79 \times 1.05}{0.12 - 0.05} = \frac{27.08}{0.07} = \$386.89$$

Present values:
- PV of dividends years 1–5: $\approx \$71.91$
- PV of terminal value: $386.89 / (1.12)^5 = \$219.54$
- **Total: $291.45$**

Two-stage DDM is more realistic than the simple Gordon model for any firm whose growth rate is changing. It's the standard for mature dividend-paying firms in transition.

**Where DDM breaks down.** The model cannot value non-dividend payers. Amazon never paid a dividend during decades of spectacular value creation. Google paid none until 2024. Berkshire Hathaway never has. For growth firms that retain cash and reinvest rather than distributing it, DDM gives you nothing — literally a zero, because you're discounting no dividends at all. A different family of methods is required.

---

## The second family: Discounted Cash Flow

The DCF model values the firm as the present value of all future **free cash flows** — the cash available to all capital providers after the firm has covered operating expenses, taxes, capital expenditures, and working-capital needs:

$$FCF = \text{EBIT} \times (1 - \text{tax rate}) + \text{Depreciation} - \text{Capex} - \Delta\text{Working capital}$$

The firm value is:

$$\text{Firm value} = \sum_{t=1}^{n} \frac{FCF_t}{(1+WACC)^t} + \frac{TV_n}{(1+WACC)^n}$$

where WACC is the firm's weighted-average cost of capital (computed in Chapter 17), $n$ is the length of the explicit forecast period, and $TV_n$ is a terminal value at the end. Divide by shares outstanding to get value per share.

**Why analysts prefer DCF over DDM.** Three reasons.

Cash flows are harder to manipulate than earnings. Accounting choices change reported earnings; cash that arrives in the bank account is more difficult to fake.

DCF works for non-dividend payers. A firm that retains cash and reinvests it in the business has DCF value even if it never pays a dividend. Most growth firms are in this category.

Building a DCF forces explicit forecasts. To run the model you must project revenue, margins, capex, working capital, and tax for each year. The discipline of doing this forces you to understand the firm. The resulting number is almost a byproduct; the understanding is the asset.

<!-- → [INFOGRAPHIC: DCF structure diagram — timeline showing explicit FCF forecasts for years 1-5, then a terminal value arrow at year 5; below the timeline, discounting arrows pointing back to year 0; labels for each component with the formula; caption: "Terminal value typically accounts for 60-80% of total firm value"] -->

**Worked example.** Forecast: $50M FCF in year 1, growing at 8% for five years, then 4% forever. WACC: 10%. One million shares outstanding.

Stage 1 FCF (in $M): $50, $54, $58.32, $62.99, $68.02$.

Terminal value:
$$TV_5 = \frac{68.02 \times 1.04}{0.10 - 0.04} = \frac{70.74}{0.06} = \$1{,}179\text{M}$$

Present values:
- PV of stage 1 FCF: $\approx \$222\text{M}$
- PV of terminal value: $1{,}179 / (1.10)^5 = \$732\text{M}$
- **Firm value: $954M**
- **Value per share: $954**

If the stock trades below $954, the DCF says it's undervalued.

**The terminal value problem.** In most DCFs, the terminal value accounts for 60–80% of total firm value. Think about what that means: the forecast for the explicit period (years 1–5), which analysts agonize over, contributes a minority of the answer. The terminal value — driven by the long-term growth rate and the discount rate — dominates. And both of those inputs are highly uncertain. Honest analysts say so explicitly in their reports. A DCF that presents a single number without sensitivity analysis on WACC and terminal growth is hiding the uncertainty rather than quantifying it.

**Sensitivity inherited from structure.** Like the Gordon model, DCF is sensitive to its inputs. A one-point change in WACC or long-term growth moves the answer 15–25%. Always run sensitivity analysis. Always present a range.

---

## The third family: Multiples

The simplest valuation approach is comparison. If the median consumer-staples firm trades at 22× earnings, and your firm earns $4.00 per share, a first approximation of the stock's value is $88. That's it.

The most common multiples:

**Price-to-earnings (P/E)** = Price / EPS. The most quoted multiple. Trailing P/E uses past-year earnings; forward P/E uses estimated next-year earnings. Most useful for profitable, stable firms.

**Price-to-book (P/B)** = Price / Book value per share. Compares market value to accounting book value. Especially useful for financial firms where book value approximates economic value.

**Price-to-sales (P/S)** = Price / Revenue per share. Useful for unprofitable firms where P/E is undefined, and for early-stage growth firms.

**EV/EBITDA** = Enterprise value / EBITDA. Enterprise value = market cap + debt − cash. This is the preferred multiple for cross-firm comparison because it neutralizes capital-structure differences. A highly leveraged firm and an unlevered firm with otherwise identical operations have similar EV/EBITDA but very different P/E ratios. When you want to compare underlying operating performance across firms with different debt loads, use EV/EBITDA.

<!-- → [TABLE: illustrative comparison of the same firm analyzed at different multiples — show how different choices of multiple (P/E vs. P/B vs. EV/EBITDA) can produce different implied valuations, and label the circumstances where each multiple is most appropriate] -->

**How multiples work in practice.** Find three to five close peers. Compute each peer's multiples. Take the median (or trimmed mean). Apply that median to your firm's relevant metric. The result is an implied value under the assumption that your firm should trade at peer multiples.

**Where multiples fail.** A multiples-based valuation assumes the peer group is fairly valued. If the whole sector is overvalued — as technology was in 2021 — applying elevated peer multiples to your firm produces elevated valuations that are uniformly wrong in the same direction. Multiples inherit market-wide mispricing. They are most useful as a cross-check against DCF, not as a primary method.

They also assume comparability. "Peer firms" rarely match perfectly on growth rates, margins, business mix, and financial structure. Adjustments are unavoidable and subjective.

---

## Triangulating: using all three together

Here is the core discipline of equity research: never trust a single method.

Suppose your company's analysis produces:
- DDM (Gordon model): $88
- DCF: $94
- P/E multiple: $92
- EV/EBITDA multiple: $98

The four methods cluster in a range of $88–$98, centered near $93. The stock trades at $85. Your reading: moderately undervalued by approximately 10%, with reasonable confidence across methods.

Now suppose the same exercise produced: DDM $50, DCF $94, P/E multiple $135, EV/EBITDA $200. You have far less confidence in any single number — but the disagreement is informative. Why does the DDM give $50 when DCF gives $94? Because the firm pays a low dividend relative to its free cash flow — it's retaining cash for reinvestment, which the DDM can't see but the DCF can. Why does the P/E multiple give $135 when the DCF gives $94? Because the peer group is expensive relative to fundamentals, which a multiples approach inherits. The research report would explain the disagreements, not paper over them.

<!-- → [INFOGRAPHIC: "valuation bridge" for a hypothetical company — a horizontal bar or range chart showing where each method falls, with the current market price marked as a vertical line; student should see what it looks like when methods cluster vs. when they diverge, and which situation should raise more caution] -->

**Professional practice.** Sell-side analysts at investment banks typically present: a DCF as primary valuation with a base case and two or three alternative scenarios; multiples as cross-checks; and an explicit price target derived from the synthesis. The recommendation — Buy, Hold, or Sell — is tied to the gap between the price target and the current market price.

For the project, you'll produce something close to this format. The methods give you a range. The range, combined with your reading of the firm's competitive position, produces your investment thesis. The presentation matters: junior analyst work that looks unprofessional is dismissed regardless of the underlying analysis.

---

## Efficient markets: what we're really doing

All three valuation methods assume stocks can be mispriced and that analysis can identify the mispricing. Whether this is correct is one of the most contested questions in finance.

The **efficient market hypothesis (EMH)** says current prices incorporate all available information. Three versions:

**Weak form:** Prices reflect all historical price and volume data. Chartism and technical analysis can't beat buy-and-hold. This version is broadly supported by evidence — technical trading strategies rarely outperform after costs.

**Semi-strong form:** Prices reflect all publicly available information — financial statements, news, analyst reports, everything in the public domain. Fundamental analysis based on public information cannot consistently beat the market. This version is contested. Some studies support it; certain hedge funds appear to contradict it persistently.

**Strong form:** Prices reflect all information, public and private. Even insiders cannot beat the market. Almost no one believes this. Insider-trading regulations exist precisely because private information demonstrably has value.

<!-- → [TABLE: three-row comparison of EMH forms — columns: form name, what information is incorporated, implication for technical analysis, implication for fundamental analysis, empirical support — student should see at a glance that evidence gets weaker as you move from weak to strong form] -->

**Why analysts do equity research anyway.** If markets are efficient, fundamental analysis is wasted effort. Several responses:

Markets are efficient on average but not everywhere. Liquid, heavily-followed large-cap stocks are close to efficiently priced. Small-cap stocks, emerging markets, and less-followed sectors are demonstrably less efficient. Analysts who specialize can find edges.

The process is valuable even when the answer isn't definitive. Building a DCF for a company forces you to understand it deeply — its products, customers, cost structure, competitive position, capital allocation. That understanding has value independent of whether the DCF answer beats the market price.

Different analysts have different inputs. Two careful analysts using DCF will get different answers because they hold different views on growth, margins, and risk. The market price is a weighted average of all these views. Your analysis is another data point. If your views are better-supported than the consensus, your number can be a useful input even when the market disagrees.

For the equity research project: the deliverable is not a promise of outperformance. It is a defensible reading of what your company is worth, with explicit assumptions, sensitivity analysis, and honest acknowledgment of what the model can't see. The process is the work. The number is the byproduct.

---

## The whole picture

A bond's value is determined by its contract. A stock's value is determined by forecasts, comparisons, and judgment. Three families of methods exist because forecasts and comparisons each capture a different piece of the picture, and no single piece is sufficient.

DDM is theoretically clean: if you hold equity to receive dividends, the stock is worth the present value of those dividends. But it can't see the value retained inside the firm that isn't paid out.

DCF is broadly applicable: it values all the cash the firm will ever generate, regardless of what form it takes. But it requires multi-year forecasts and is dominated by a terminal value that itself requires heroic assumptions about the long run.

Multiples are fast and grounded in observable market prices. But they inherit the market's current sentiment, including whatever overvaluation or undervaluation currently pervades the peer group.

Use all three. Report the range. Explain the disagreements. That is what equity research is.

The next several chapters refine the inputs. Chapter 14 establishes beta and the CAPM, which gives you the required return for DDM and DCF. Chapter 17 computes WACC. Chapter 18 builds the systematic forecasting framework for the cash flows that go into DCF. By the time those chapters are done, the first-cut model you'll build in the exercise below will be replaced by something considerably sharper.

---

## Exercises

### Warm-up

**11.1** Distinguish common stock from preferred stock on four dimensions: voting rights, dividend obligation, claim priority in liquidation, and upside participation. Which behaves more like a bond, and why?
*(Tests: fundamental distinction between equity types and where preferred stock sits on the risk spectrum)*

**11.2** State the Gordon growth model formula and define every variable. What is the mathematical constraint on $r$ and $g$, and what is the economic reason the constraint exists?
*(Tests: Gordon model structure and the logic behind the r > g requirement)*

**11.3** Name the three families of valuation methods. For each, state in one sentence the core principle it applies and one circumstance where it is the least reliable method.
*(Tests: conceptual overview of all three families and their failure conditions)*

### Application

**11.4** A stock pays $3.60 in dividends this year, growing at 5% per year forever. The required return is 10%.

(a) Compute the stock's value using the Gordon growth model.
(b) Recompute if growth rises to 7%. By what percentage does value change?
(c) Recompute if the required return rises to 12% (growth back to 5%). By what percentage does value change?
(d) Which input — growth or discount rate — produces the larger percentage change in (b) vs. (c)? What does that suggest about where analysts should focus their disagreements?

*(Tests: Gordon model computation and sensitivity intuition)*

**11.5** A firm has the following projected free cash flows ($ millions):

| Year | FCF |
|---|---|
| 1 | 60 |
| 2 | 72 |
| 3 | 86 |
| 4 | 100 |
| 5 | 112 |

After year 5, FCF grows at 3% forever. WACC is 9%. The firm has 40 million shares outstanding and $200M net debt.

(a) Compute the PV of years 1–5 FCFs.
(b) Compute the terminal value at year 5 and discount it to today.
(c) Compute firm value, subtract net debt, and divide by shares to get equity value per share.
(d) What percentage of total firm value comes from the terminal value? What does this tell you about where DCF results are most sensitive to assumptions?

*(Tests: full DCF computation including terminal value and equity bridge)*

**11.6** A company earns $5.50 in diluted EPS (trailing twelve months). You identify four peer firms with trailing P/E multiples of 18, 21, 24, 19, and 22.

(a) Compute the peer median P/E.
(b) Apply the median multiple to get an implied stock price.
(c) The company's current stock price is $85. Is it overvalued or undervalued by this measure? By how much?
(d) Name two reasons the company might legitimately deserve to trade above the peer median. Name two reasons it might deserve to trade below.

*(Tests: multiples computation and the judgment required to interpret the comparison)*

### Synthesis

**11.7** A mature consumer-products firm pays $4.00 in dividends (growing at 3.5%), has $6.00 in earnings, trades at $72 per share, and has a required return of 9%. Its peer group trades at a median P/E of 16.

(a) Apply the Gordon model. Is the stock undervalued or overvalued?
(b) Apply the P/E multiples comparison. Is it undervalued or overvalued?
(c) The two methods give different answers. Construct one explanation where the DDM result is more trustworthy, and one where the multiples result is more trustworthy. What evidence would distinguish them?

*(Tests: triangulation across methods and the analytical skill of explaining disagreement)*

**11.8** State the three forms of the efficient market hypothesis. Then construct a specific scenario — a real investment strategy or a real market event — that would count as evidence against each form. What would you need to observe to conclude a given form had been violated rather than merely noisy?
*(Tests: EMH definitions and the evidentiary standard required to challenge each form)*

### Challenge

**11.9** Build a first-cut DCF for your chosen company in Excel using data from its most recent 10-K. Use the following assumptions as a starting point:

- Revenue growth: 3-year historical average from MD&A.
- Operating margin: 3-year average.
- Tax rate: effective rate from most recent year.
- Capex: 3-year average as % of revenue.
- Working capital change: 3-year average as % of revenue.
- Terminal growth: 2.5%.
- WACC: 8% placeholder.

Compute base-case value per share. Then run a sensitivity table: WACC at 7%, 8%, 9% across columns; terminal growth at 1.5%, 2.5%, 3.5% across rows. Report the nine resulting values per share. Where does the current stock price fall in your sensitivity range? What does that placement imply about the market's embedded assumptions?

*(Tests: full DCF construction from primary-source data, sensitivity analysis, and the ability to read what a market price implies about assumptions)*

**11.10** Your DCF for a chosen company produces a value per share of $X. Your P/E and EV/EBITDA multiples comparison produces values of $Y and $Z. The three estimates differ by more than 25%.

Construct three distinct explanations for the disagreement:

(a) A problem with your DCF assumptions — which specific input is most likely wrong, and in which direction?
(b) A problem with the peer comparison — what makes your firm genuinely different from the peers in a way that justifies a premium or discount?
(c) A market-level mispricing — is there a reason the entire peer group might be over- or undervalued relative to fundamentals right now?

For each explanation, identify what additional evidence — from the 10-K, from market data, or from industry sources — would help you determine which explanation is most likely correct.

*(Tests: analytical diagnosis of valuation disagreement, the kind of reasoning that distinguishes serious equity research from mechanical model-running)*

---

## What would change my mind

The chapter argues that DCF is the gold-standard approach for most equities, with multiples as cross-checks and DDM as a special case. Two things would revise this. First, if analyst DCFs turned out to be systematically and incorrigibly biased — there is empirical evidence that sell-side DCFs are too optimistic — but the bias is in the *inputs*, not the method. Better inputs fix a biased DCF; no amount of better inputs fixes a wrong method. Second, if a fundamentally new valuation framework emerged that captured what DCF misses. Real-options approaches come close for some firms. Behavioral-finance adjustments qualify DCF but don't replace it. For now, DCF + multiples + DDM remains the working consensus.

## Still puzzling

The cleanest unresolved question: what to do when the three methods substantially disagree. If they agree within 10–15%, the synthesis is easy. If DCF says $100 and the multiples say $60, you have to decide which to weight, and that decision is where the analyst's judgment actually lives. The honest framework is: reason about which method's assumptions are most likely to be wrong for *this specific firm* in *this specific market environment*, and weight accordingly. This is craft, not algorithm. I have not found a clean rule for it, and I am skeptical of anyone who claims to have one.

---

## Connections forward

- **Chapter 12** examines historical equity returns — empirical context for the assumptions in DCF and DDM.
- **Chapter 13–14** install statistics and regression for measuring risk and computing beta.
- **Chapter 17** computes WACC, the firm's discount rate.
- **Chapter 18** forecasts the cash flows that go into DCF.
- **Chapter 20** frames the risk management required for the firm to deliver the forecast cash flows.

---

## LLM Exercise — Chapter 11: First-Cut DCF Model

**Project:** Equity Research Report on a Chosen Public Company
**What you're building this chapter:** A first-cut DCF model for your company's stock. This is the analytical centerpiece of the report; we'll refine it in Chapters 14, 17, and 18.
**Tool:** Claude Project + Excel. You'll build the actual model in a spreadsheet; Claude helps with assumption-setting, sensitivity, and sanity-checking.

### The Prompt

```
For [your company], we're building a first-cut DCF model. Help me set up a 5-year explicit forecast plus terminal value, with these inputs:

### Forecast assumptions

1. **Revenue growth** — From the most recent 10-K's MD&A and management guidance, what's a reasonable annual revenue growth rate for years 1-5? Provide a base case, a bull case (+30% above base), and a bear case (-30% below base).

2. **Operating margin** — Use the most recent 3-year average operating margin as a starting point. Adjust for any known structural changes (tariffs, new product mix, etc.).

3. **Tax rate** — Use the firm's effective tax rate from the most recent 10-K.

4. **Capex** — Use the most recent 3-year average capex as a percentage of revenue. Adjust if there are known major capex programs.

5. **Working capital** — Use the most recent 3-year average change in NWC as a percentage of revenue.

6. **Terminal growth** — Use 2-3% (a reasonable long-term GDP-linked rate).

7. **WACC** — Use 8% as a placeholder. We'll compute the real WACC in Chapter 17.

### What I need from you

For each year (1-5):
- Forecasted revenue (base case, bull, bear)
- Forecasted operating income
- Forecasted FCF = (operating income × (1 - tax rate)) + depreciation - capex - ΔNWC

For the terminal value at year 5:
- TV = FCF_year_5 × (1 + g) / (WACC - g)

For the present value:
- PV(FCF years 1-5) using WACC discounting
- PV(TV) using WACC discounting
- Total firm value

Then:
- Subtract net debt from firm value to get equity value.
- Divide by shares outstanding to get value per share.
- Compare to current market price.

Provide:
1. The base case value per share.
2. Bull case and bear case values.
3. The implied price target (or range).

Be explicit about every assumption. Show the math. Run sensitivity on WACC ±1% and terminal growth ±1%.
```

### What this produces

A first-cut DCF in Excel with three scenarios. The output is a fair-value range that you'll refine in subsequent chapters as you get better inputs (real WACC in Chapter 17, scenario-based forecasts in Chapter 18).

### How to adapt this prompt

- *For your own company:* Replace [your company]. Adjust the assumption ranges based on your firm's industry and growth profile.
- *For ChatGPT / Gemini:* Identical.
- *For Claude Code:* Could automate the spreadsheet with Python (pandas + openpyxl), but Excel is fine for one company.

### Connection to previous chapters

Synthesizes everything: Chapter 5's statements, Chapter 6's ratios, Chapter 7-9's TVM, Chapter 10's debt analysis.

### Preview of next chapter

Chapter 12 examines historical equity returns. The Chapter 12 LLM Exercise will compute your company's realized returns vs. the broad market — input to the regression in Chapter 14.

---

**Tags:** stock-valuation, DCF, dividend-discount-model, Gordon-growth, multiples, P/E, EV/EBITDA, efficient-markets

---

## AI Wayback Machine

**John Burr Williams** wrote *The Theory of Investment Value* (1938) — establishing the dividend discount model that still anchors stock valuation.

**Run this:**

```
Who is John Burr Williams, and how does their work connect to stock valuation we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about their career or ideas.
```

→ Search **"John Burr Williams"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to apply John Burr Williams's framework to a specific finance question.
- Add a constraint: "Answer including criticisms or limits of John Burr Williams's framework."

What changes? What gets better? What gets worse?
