# Chapter 11 — Stocks and Stock Valuation

**Suggested titles**
1. Three Ways to Price an Uncertain Cash Flow
2. From Dividends to DCF
3. What Is a Stock Worth?

**TL;DR.** A bond's cash flows are contractual; a stock's are not. That single difference is what makes stock valuation harder, and why three different families of valuation methods exist — dividend discount models, discounted cash flow models, and relative-multiples approaches. None of them is right by itself. Serious equity research uses all three and triangulates.

---

## The puzzle of the missing contract

In Chapter 10, we priced a bond. The math was tight: known coupon payments, known principal, known maturity date. Everything you needed to compute a bond's present value was written in the bond's contract. The market's only judgment call was the discount rate.

A stock has no such contract.

A share of common stock entitles you to a fractional ownership in the issuing firm. That ownership comes with three things: a vote at shareholder meetings, a residual claim on the firm's assets in the event of liquidation, and a *possible* stream of dividends the company *may* decide to pay at *whatever amount it chooses* on *whatever schedule* the board approves. There is no contractual guarantee of any cash flow at any time.

So how do you value a stock?

The honest answer is: imperfectly, with three different families of methods, none of which agrees with the others, and all of which require judgment. The interesting answer is: each method works on a different principle, and understanding when each applies is the analyst's craft.

The three families:

1. **Dividend Discount Models (DDM)** — value the stock as the present value of future dividend payments, projected and discounted.
2. **Discounted Cash Flow (DCF) models** — value the firm as the present value of all future free cash flows, then divide by share count.
3. **Multiples-based approaches** — value the stock by comparing it to similar firms using ratios like P/E, P/B, EV/EBITDA.

Each is a different reading of "what is this share entitled to." Each works better in some circumstances than others. A serious equity research report uses all three and triangulates among them.

For the running project, this chapter is the analytical heart of the equity research deliverable. The DCF model you'll build for your chosen company in this chapter's exercises becomes the centerpiece of your final report.

---

## Learning objectives

After working through this chapter, you should be able to:

- Distinguish common stock from preferred stock, and identify the rights and limitations of each.
- Apply the **zero-growth dividend discount model** to value preferred stock and bond-like equity.
- Apply the **Gordon growth model** (constant-growth DDM) to value mature dividend-paying firms.
- Apply a **two-stage DDM** to value firms transitioning from high-growth to mature growth.
- Apply the **DCF model** to value firms where free cash flow is more reliable than dividends.
- Compute and interpret **P/E, P/B, P/S, P/CF, and EV/EBITDA** multiples.
- State the three forms of the efficient market hypothesis and assess what each implies for active equity research.

**Prerequisites.** Chapters 7–10 (TVM, bonds). Chapter 6 (financial ratios).

---

## Concept 1 — What a stock is, and why valuation is hard

Two things make a stock fundamentally different from a bond.

**No contractual cash flow.** A bond promises explicit, contractual coupon and principal payments. A stock promises nothing. Dividends, if any, are at the board's discretion. Capital gains, if any, depend on the market's evolving judgment of the firm's prospects. The cash flow stream is not specified; it has to be *forecast*.

**Residual claim.** Bondholders are paid first. After interest and principal are met, what's left flows to equity holders — but only what's left. In good years, that's a lot. In bad years, it can be zero. The variability is built into the equity claim.

These two features make stocks both more risky and more potentially rewarding than bonds. They also make valuation a fundamentally judgment-laden exercise.

### Common vs. preferred stock

Most public companies issue **common stock**. Common shareholders:
- Vote at shareholder meetings (typically one vote per share).
- Receive dividends if and when the board declares them.
- Have a residual claim on assets in liquidation (after all creditors and preferred shareholders are paid).
- Bear the full upside and downside of the firm's performance.

Some firms also issue **preferred stock**, a hybrid instrument with features of both stocks and bonds:
- Pays a *fixed* dividend at a stated rate, similar to a bond's coupon.
- Has priority over common stock in dividend payments and liquidation.
- Usually carries no voting rights.
- Has no maturity date — preferred dividends, in principle, continue indefinitely.

Preferred stock can be **cumulative** (missed dividends accumulate as a liability that must eventually be paid) or **noncumulative** (missed dividends are simply lost). Some preferred shares are **convertible** — the holder can exchange them for common shares at a specified ratio, providing upside participation if the common stock appreciates.

Because preferred dividends are fixed and continue indefinitely, preferred stock is essentially a perpetuity. Pricing it is straightforward (we'll see in Concept 2).

Common stock is the harder case and the focus of the rest of this chapter.

### Why investors hold stocks despite the uncertainty

Stocks have outperformed bonds and cash over almost every long-run period in US market history (Chapter 12 gets the data). The premium for bearing equity risk — the **equity risk premium** — has averaged roughly 4–5 percentage points over Treasury yields over the past century. That's the compensation for accepting variable cash flows and residual claim status.

For an investor with a long horizon, a diversified portfolio of stocks has historically produced wealth-compounding returns that bonds and cash cannot match. For a short horizon, the variability can be catastrophic — the S&P 500 fell 38% in 2008 and 34% in early 2020. Time horizon matters enormously.

For the equity research project: when you construct your investment thesis, you're implicitly betting that *your particular stock* will outperform the broader market. Most stocks don't. The work in the next several sections is about doing that analysis honestly.

↳ **Dig Deeper — Why some companies don't pay dividends**

*Apple paid no dividends from 1995 to 2012 — through the entire iPod and iPhone launch. Berkshire Hathaway has never paid a dividend. Amazon has never paid a dividend. Yet all three have created enormous shareholder value. The decision *not* to pay dividends is itself a capital allocation decision worth understanding.*

**Prompt:**
> Explain the trade-off between paying dividends and retaining earnings for reinvestment, from the firm's perspective. Walk through Berkshire Hathaway's stated rationale (Buffett's letters explain it). Compare to Apple's reversal in 2012 — what changed in Apple's situation that made dividends appropriate? Then summarize the empirical evidence: do non-dividend-paying firms outperform dividend-paying firms over long periods?

**What to do with the output:** Save it. If your project company doesn't pay dividends, this gives you the framework to assess whether that's value-creating capital allocation or hoarding.

### The trade-off (concept 1)

Equity ownership trades **higher expected returns against higher uncertainty about realized returns**. The contractual cash flows of bonds give you a much narrower range of outcomes. The non-contractual nature of equity widens the range in both directions. Whether equity is the right choice depends on your time horizon, your risk tolerance, and your alternative uses for capital.

### Common misconceptions

- *"Stocks always go up over the long run."* On average, in the US, over multi-decade horizons, yes. Japan since 1990 is a counterexample lasting more than 30 years. Country selection matters; time horizon matters; diversification matters.
- *"A high stock price means a valuable company."* The price per share is meaningless without context. A $10 stock with 100 billion shares outstanding has a much larger market cap than a $1,000 stock with 100,000 shares outstanding. Always reason about market cap, not price.

---

## Concept 2 — Three families of valuation methods

Each family answers "what is this stock worth?" by a different route. We work through them in order of conceptual cleanliness.

### Family 1 — Dividend Discount Models (DDM)

If a stock pays dividends, one defensible approach is to value it as the present value of all future dividend payments. The general formula:

$$P_0 = \sum_{t=1}^{\infty} \frac{D_t}{(1+r)^t}$$

where $D_t$ is the dividend in year $t$ and $r$ is the required rate of return.

The infinite sum looks intimidating, but with assumptions about how dividends behave, it collapses to closed forms.

**Zero-growth DDM.** If dividends are constant forever (a perpetuity):

$$P_0 = \frac{D}{r}$$

This is the formula we used in Chapter 8 for perpetuities. It applies cleanly to preferred stock and to mature firms whose dividends genuinely don't grow.

Example: a preferred stock pays $5.00 annually with a required return of 8%. Price = $5/0.08 = $62.50.

**Constant-growth DDM (the Gordon model).** If dividends grow at a constant rate $g$ forever:

$$P_0 = \frac{D_1}{r - g}$$

where $D_1 = D_0 \times (1+g)$ is next year's dividend. This is the growing-perpetuity formula from Chapter 8 applied to dividends. It requires $r > g$; if dividends grow as fast as the discount rate, the formula blows up.

Example: A stock pays $5.00 this year ($D_0$), is expected to grow dividends at 4% per year forever, and has a required return of 8%. Then $D_1 = 5.20$, and:

$$P_0 = \frac{5.20}{0.08 - 0.04} = \$130$$

The Gordon model is the workhorse of DDM. It applies to mature firms with stable dividend histories — utilities, consumer staples, established industrials.

**Sensitivity warning.** The Gordon model is brutally sensitive to the inputs. With $D_1 = 5.20$:
- $r = 8\%, g = 4\%$ → $130
- $r = 8\%, g = 5\%$ → $173 (33% higher for a 1-point change in $g$)
- $r = 9\%, g = 4\%$ → $104 (20% lower for a 1-point change in $r$)

A 1-percentage-point miss on either input swings the valuation 20–35%. This is why DDM valuations should never be reported as a single number; report a range.

**Two-stage DDM.** Real firms don't grow at a constant rate forever. The two-stage DDM splits the future into two periods: a high-growth phase (e.g., 10% growth for 5 years) followed by a stable-growth phase (e.g., 4% forever).

Procedure:
1. Compute and discount the dividends during the high-growth phase year by year.
2. At the end of the high-growth phase, compute a **terminal value** using the Gordon model on the start of the stable-growth phase.
3. Discount the terminal value back to today.
4. Sum: $P_0 = \sum_{t=1}^{n} \frac{D_t}{(1+r)^t} + \frac{TV_n}{(1+r)^n}$

Worked example. A company pays $14 dividend this year, growth of 13% for the next 5 years, then 5% forever. Required return: 12%.

Stage 1 dividends (years 1-5):
- $D_1 = 14 \times 1.13 = \$15.82$
- $D_2 = 17.88, D_3 = 20.20, D_4 = 22.83, D_5 = 25.79$

Terminal value at end of year 5 (using Gordon with $D_6 = 25.79 \times 1.05 = 27.08$):
$$TV_5 = \frac{27.08}{0.12 - 0.05} = \$386.89$$

Present value:
- PV of dividends years 1-5 ≈ $71.91
- PV of terminal value: $386.89 / (1.12)^5 = \$219.54$
- **Total: $291.45**

Two-stage DDM is more realistic than the simple Gordon model and is the standard for mature dividend-paying firms whose growth profile is changing.

**DDM limitations.** The model has serious limitations:
- It cannot value non-dividend payers. Many of the most successful firms — Amazon, Google (until 2024), Berkshire Hathaway — pay no dividends.
- It is brutally sensitive to growth and discount rate assumptions.
- Companies can manipulate dividend policy in ways that distort the model. A firm taking on debt to maintain a dividend looks fine to the DDM but is actually destroying value.

For the project: DDM works for some chosen companies (utilities, consumer staples, mature financials) and not others. If your company doesn't pay dividends, you'll need DCF.

### Family 2 — Discounted Cash Flow (DCF)

The DCF model values the firm as the present value of all future **free cash flows**. The general formula:

$$\text{Firm value} = \sum_{t=1}^{n} \frac{FCF_t}{(1+r)^t} + \frac{TV_n}{(1+r)^n}$$

where:
- $FCF_t$ is free cash flow in year $t$
- $r$ is the firm's weighted-average cost of capital (WACC, computed in Chapter 17)
- $TV_n$ is the terminal value at the end of the explicit forecast period
- $n$ is the length of the forecast period

After computing firm value, divide by shares outstanding to get value per share. Compare to the current market price.

**Why DCF is the analyst's preferred method.** Three reasons:

1. **Cash flows are harder to manipulate than earnings.** Accounting choices change reported earnings. Cash that arrives in the bank account is harder to fake.
2. **Works for non-dividend-payers.** A firm that retains cash and reinvests in the business has DCF value but no DDM value. Most growth firms are in this category.
3. **Forces explicit forecasts.** Building a DCF means projecting revenue, margins, capex, working capital changes, and tax for each year. The discipline of doing this is the analytical exercise; the resulting number is almost a byproduct.

**Free cash flow** is the cash available to all capital providers (debt and equity) after the firm has covered its operating expenses, taxes, capital expenditures, and working-capital needs:

$$FCF = \text{EBIT} \times (1 - \text{tax rate}) + \text{Depreciation} - \text{Capex} - \Delta \text{Working capital}$$

This is **free cash flow to the firm (FCFF)**, the standard input to enterprise-DCF. (There's also free cash flow to equity, FCFE, which subtracts net debt repayments. Both work; FCFF is more common.)

**Worked example — a hypothetical mid-size firm.** Forecast: $50M FCF in year 1, growing at 8% for 5 years, then 4% forever. WACC: 10%. 1 million shares outstanding.

Stage 1 FCF (years 1-5):
- $FCF_1 = 50, FCF_2 = 54, FCF_3 = 58.32, FCF_4 = 62.99, FCF_5 = 68.02$ (in $M)

Terminal value at year 5:
$$TV_5 = \frac{68.02 \times 1.04}{0.10 - 0.04} = \frac{70.74}{0.06} = \$1{,}179\text{M}$$

Present value:
- PV of FCF years 1-5: ~$222M
- PV of terminal value: $1,179 / (1.10)^5 = \$732\text{M}$
- **Firm value: $954M**
- **Value per share: $954**

Compare to current market price. If the stock trades below $954, DCF says it's undervalued.

**Sensitivity.** DCF inherits the same sensitivity problem as DDM. A 1-point change in WACC or in long-term growth rate moves the answer 15–25%. Always run sensitivity analysis.

**Terminal value dominance.** In most DCFs, the terminal value accounts for 60–80% of total firm value. The forecast for the explicit period (years 1-5 or 1-10) gets disproportionate analytical attention but contributes a minority of the answer. The terminal value — driven by long-term growth and WACC — dominates. This is humbling; honest analysts say so.

For the project: build a DCF for your chosen company. Year 1 FCF can be estimated from the most recent 10-K. Years 2-5 require forecasting growth (Chapter 18 will help). Terminal growth rate should be conservative — usually no higher than long-term GDP growth (2-3%). WACC computation is Chapter 17.

### Family 3 — Multiples (relative valuation)

The simplest valuation approach is *comparing* a firm to its peers. If the median software firm trades at 25× earnings, and your firm earns $4 per share, the firm is worth roughly $100 per share by multiples.

The most common multiples:

**Price-to-earnings (P/E).**
$$\text{P/E} = \frac{\text{Price}}{\text{EPS}}$$
The most quoted multiple. Trailing P/E uses the past year's earnings; forward P/E uses estimated next-year earnings. Useful for profitable, stable firms.

**Price-to-book (P/B).**
$$\text{P/B} = \frac{\text{Price}}{\text{Book value per share}}$$
Compares market value to accounting book value. Especially useful for financial firms (banks, insurers) where book value approximates economic value.

**Price-to-sales (P/S).**
$$\text{P/S} = \frac{\text{Price}}{\text{Revenue per share}}$$
Useful for unprofitable firms (where P/E is meaningless) and for early-stage growth firms.

**Price-to-cash-flow (P/CF).**
$$\text{P/CF} = \frac{\text{Price}}{\text{Operating cash flow per share}}$$
Useful when accounting earnings differ substantially from cash earnings.

**EV/EBITDA.**
$$\text{EV/EBITDA} = \frac{\text{Enterprise value}}{\text{EBITDA}}$$
**Enterprise value** = market cap + debt − cash. EV/EBITDA is the favorite multiple for cross-firm comparison because it neutralizes capital structure differences. A leveraged firm and an unleveraged firm with otherwise identical operations have similar EV/EBITDA but very different P/E ratios.

**Dividend yield.**
$$\text{Dividend yield} = \frac{\text{Annual dividend}}{\text{Price}}$$
Useful for income-oriented investors. High dividend yields can signal undervaluation or signal a dividend that's about to be cut.

**The multiples approach in practice.** For your chosen company, find 3-5 close peers. Compute each peer's P/E, P/B, EV/EBITDA, P/S. Compute the median (or trimmed mean) multiple for the peer group. Apply the median multiple to your company's relevant metric (earnings, book, EBITDA, sales). The result is an implied valuation under the assumption that your firm should trade at peer multiples.

**Limitations of multiples.**

- **Snapshot in time.** A multiple captures one moment of market sentiment, not long-run economics.
- **Garbage in, garbage out.** If peer multiples are inflated (as in 2021 tech), applying them to your firm produces inflated valuations.
- **Comparability.** "Peer firms" rarely match perfectly on all dimensions. Adjustments are subjective.
- **Aggregated bubbles.** When the whole market is overvalued, all peers are overvalued, and multiples-based valuations are uniformly wrong in the same direction.

Multiples should be used as a *cross-check* against DCF and DDM, not as a primary valuation method.

↳ **Dig Deeper — When DCF and multiples disagree dramatically**

*Two valuation methods, applied to the same firm, can give answers that differ by 50% or more. When this happens, the analyst's job is to figure out *why* — not to average the answers. The disagreement itself is informative.*

**Prompt:**
> Construct a hypothetical example where DCF says a stock is worth $100/share but the trailing P/E multiple comparison (using peer median) suggests $60/share. List six possible reasons for the disagreement, ranging from technical (DCF assumptions are wrong) to substantive (peer firms aren't actually comparable, or the market is mispricing the entire peer group). For each reason, identify what evidence would distinguish it.

**What to do with the output:** Save it. When your project's DCF and multiples disagree, you'll need to walk through this kind of diagnosis.

### The trade-off (concept 2)

Each valuation family trades **assumption-load against applicability**.

- **DDM** has the cleanest theory (PV of cash to equity holders) but requires dividends to exist and to be predictable.
- **DCF** has the broadest applicability but requires multi-year forecasts of cash flows.
- **Multiples** require the least forecasting but assume peer comparability and inherit market-wide mispricing.

A serious equity research report uses all three and reports the range. If they agree closely, confidence is high. If they disagree by 50%, you have a story to tell about why.

### Worked example — triangulating a single stock

Suppose your chosen company:
- Pays $2.50 dividend, growing at 6%, required return 9% → DDM gives $2.65/0.03 = $88
- DCF gives $94 per share
- P/E of 22 × EPS of $4.20 = $92
- EV/EBITDA of 14 × EBITDA per share of $7 = $98

The four methods give a range of $88-$98, clustering around $93. Current market price is $85. Your reading: the stock is moderately undervalued by about 10%, with reasonable confidence.

If the same exercise gave $50, $94, $135, and $200, you'd have much less confidence in any single number — and your research report would explain *why* the methods disagree. Disagreement is informative.

### Common misconceptions

- *"DCF is the right answer."* DCF gives one answer based on its assumptions. Different reasonable analysts using DCF will get different answers. It's a tool, not an oracle.
- *"Higher P/E means overvalued."* Not necessarily. A firm growing earnings faster than its peers deserves a higher multiple. Compare growth-adjusted multiples (PEG ratio) within an industry.
- *"Multiples replace fundamental analysis."* They don't. They summarize the market's current pricing of fundamentals.

---

## Concept 3 — Efficient markets and what we're really doing

The valuation methods in Concept 2 assume that stocks can be mispriced and that careful analysis can identify the mispricing. Whether this assumption is correct is one of the most contested questions in finance.

### The efficient market hypothesis

The **efficient market hypothesis (EMH)** says that current stock prices incorporate all available information. If true in its strong form, the entire equity-research industry is wasting its time.

EMH comes in three flavors:

**Weak form.** Current prices reflect all *historical price and volume information*. Charting and technical analysis cannot predict future prices. (This form is broadly supported by empirical evidence — technical-analysis trading rarely beats buy-and-hold after costs.)

**Semi-strong form.** Current prices reflect all *publicly available information* — financial statements, news, analyst reports, everything in the public domain. Fundamental analysis based on public information cannot consistently beat the market. (This form is contested. Some studies support it; some hedge funds appear to violate it.)

**Strong form.** Current prices reflect *all information* — public and private. Even insiders cannot beat the market. (Almost no one believes this. Insider trading regulations exist because insider information demonstrably has value.)

### Why analysts do equity research anyway

If markets are at least somewhat efficient, why does the equity research industry exist? Three reasons:

**1. Markets are efficient on average but not everywhere.** Liquid, heavily-followed large-cap stocks may be close to efficient. Small-cap stocks, foreign markets, emerging asset classes are demonstrably less efficient. Skilled analysts who specialize can find edges.

**2. The process matters even if the answer is wrong.** Building a DCF for your chosen company forces you to understand the firm — its products, customers, competitive position, cost structure, capital allocation. Even if the DCF answer is no better than the market price, the *understanding* is the asset.

**3. Different analysts have different inputs.** Two analysts using DCF will get different answers because they have different views on growth, margins, and discount rates. The market price is one weighted average of these views; your analysis is another. If your views are well-supported, your number can be a useful input even if the market disagrees.

For the equity research project, the deliverable is not a guarantee of future performance. It is a defensible reading of what your company is worth, with explicit assumptions and sensitivity analysis. The process is the work; the number is the byproduct.

### How professional analysts handle the methods

Professional sell-side analysts at investment banks typically present:
- A DCF as their primary valuation, with a base case and 2-3 alternative scenarios.
- Multiples-based valuations as cross-checks.
- An explicit price target derived from the analysis.
- A Buy/Hold/Sell recommendation tied to the price target relative to current market price.

Buy-side analysts (at hedge funds and asset managers) typically:
- Build their own models from scratch rather than rely on sell-side estimates.
- Apply more elaborate sensitivity analysis.
- Express less concrete recommendations (often holding longer or shorter than sell-side targets imply).

For the project, you'll produce something close to the sell-side format — a DCF, multiples cross-check, and a recommendation. The presentation matters; junior analyst work that looks unprofessional is dismissed regardless of the underlying analysis.

### The trade-off (concept 3)

Active equity research trades **the cost of analysis against the value of insight**. If markets are perfectly efficient, the cost is wasted; if markets are sufficiently inefficient, the insight is profitable. The empirical answer is somewhere in the middle, and skilled analysts in particular niches can sustain modest edges. Most active investors don't beat the market over the long run after costs. A small minority do, persistently. The interesting question for any individual analyst is whether they're in that minority.

### Worked example — putting your project together

For your chosen company, the deliverable from this chapter is a valuation section of the equity research report:

1. **DCF model** with explicit assumptions for revenue growth, margins, capex, tax rate, and WACC. Present base case + bull/bear sensitivity.
2. **Multiples comparison** to 3-5 peer firms on P/E, EV/EBITDA, and one other relevant multiple. Report median peer multiple and implied value.
3. **(If applicable) DDM** — for dividend-paying mature firms.
4. **Triangulation** — what range of values do the methods imply? Where do they agree, where do they disagree, and why?
5. **Price target** — your synthesized estimate of fair value per share.
6. **Recommendation** — Buy if your price target is materially above market price; Hold if roughly equal; Sell if materially below.

Chapters 14 (CAPM and beta), 17 (WACC), and 18 (forecasting) give you the inputs. Chapter 20 cross-checks against the firm's risk profile. By the end of the book, your final report integrates everything.

### Common misconceptions

- *"If the market is efficient, valuation is pointless."* Even efficient markets need analysts to make them efficient. Someone has to do the work that gets reflected in the price.
- *"Sell-side recommendations are reliable."* They have systematic biases. Empirical work shows sell-side analysts collectively over-recommend Buy and under-recommend Sell, partly because of investment-banking client relationships. Read recommendations critically.

---

## Synthesis — three families, one judgment

A stock has no contractual cash flow. Three families of valuation methods exist because no single approach captures everything that matters. DDM is theoretically clean but applies only to dividend-paying firms. DCF is broadly applicable but requires multi-year forecasts and is brutally sensitive to assumptions. Multiples are easy and useful as cross-checks but inherit market-wide mispricing.

A serious equity analyst uses all three, triangulates among them, presents the resulting range honestly, and commits to a recommendation that the analysis supports.

For the running project, the valuation section of your equity research report uses these methods to estimate your chosen company's fair value. The methods give you a range. The range plus your reading of the firm's qualitative position produces your investment thesis.

The next several chapters refine the inputs. Chapter 12 gives historical equity-return data. Chapter 13-14 install the statistical and regression tools for risk measurement. Chapter 17 computes WACC. Chapter 18 forecasts the cash flows. Chapter 20 frames risk management. By the end, the equity research report writes itself.

---

## Exercises

### Warm-up

**11.1** Distinguish common stock from preferred stock on at least four dimensions.

**11.2** State the Gordon growth model formula. Define each variable. What's the constraint on $r$ and $g$, and why?

**11.3** Why is DCF preferred over DDM for many companies? Name two types of firms where DCF is more appropriate.

### Application

**11.4** A stock pays $3.00 dividend this year, growing at 5% per year forever. Required return is 9%.
(a) What's the stock's value using the Gordon model?
(b) Recompute if growth is 6% (other inputs unchanged). By what percentage does the value change?
(c) Recompute if required return is 10% (other inputs unchanged). By what percentage does the value change?
(d) What does this tell you about the model's sensitivity?

**11.5** A firm has the following projected free cash flows ($M):
| Year | FCF |
|---|---|
| 1 | 80 |
| 2 | 95 |
| 3 | 115 |
| 4 | 130 |
| 5 | 140 |
After year 5, FCF grows at 3% forever. WACC is 9%. The firm has 50 million shares outstanding.
(a) Compute the present value of years 1-5 FCFs.
(b) Compute the terminal value at year 5.
(c) Compute the present value of the terminal value.
(d) Sum to get firm value, then divide by shares for value per share.

**11.6** For your chosen company, compute:
(a) Trailing P/E using the most recent 10-K's diluted EPS.
(b) Forward P/E using consensus next-year EPS estimates.
(c) P/B using the most recent balance sheet.
(d) EV/EBITDA using market cap + total debt − cash, divided by trailing EBITDA.

### Synthesis

**11.7** Build a complete DCF model for your chosen company in Excel:
- Project FCF for 5 years using historical growth as a starting point and adjusting based on industry trends.
- Compute terminal value with conservative long-term growth.
- Use a WACC estimate (you can use 8% if Chapter 17's WACC computation is not yet done).
- Compare the resulting value per share to the current market price.

**11.8** Compare your company to 3 peer firms on at least two valuation multiples. Are your company's multiples above or below the peer median? What does this suggest about the market's view of your company? How does it match or differ from your DCF?

### Challenge

**11.9** Two firms in the same industry have identical earnings, identical revenue, but very different P/E multiples (one is 15, one is 30). List five distinct factors that might justify the difference. For each, explain which is reasonable and which suggests mispricing.

**11.10** Your DCF says your chosen company's stock is worth $X. Your multiples comparison says it's worth $Y. They disagree by 30%. Construct three plausible explanations: (a) your DCF assumptions are off; (b) the market is mispricing the stock; (c) the peer firms aren't good comparables. For each, identify what evidence would distinguish the explanation from the alternatives.

---

## Chapter summary

- A stock has no contractual cash flow. Three families of valuation methods exist to handle the resulting uncertainty.
- **DDM** values stocks as the present value of future dividends. Forms: zero-growth, Gordon (constant growth), two-stage. Applies only to dividend payers; sensitive to assumptions.
- **DCF** values the firm as the present value of free cash flows, then divides by share count. Most broadly applicable; requires multi-year forecasts; terminal value typically dominates.
- **Multiples** (P/E, P/B, P/S, P/CF, EV/EBITDA) compare the firm to peers. Quick and useful as cross-checks; inherits market-wide mispricing.
- The **efficient market hypothesis** has three forms (weak, semi-strong, strong). Markets are roughly efficient on average; specific niches and firms can be inefficient enough to reward analysis.
- A serious equity research report uses all three families and triangulates.

---

## What would change my mind

The chapter argues that DCF is the gold-standard valuation approach for most equities, with multiples as cross-checks and DDM as a special case for dividend payers. The reading would have to revise if (a) DCF turned out to be systematically biased — there's empirical work suggesting analyst DCFs are typically too optimistic, but the bias is in the *inputs*, not the method, or (b) a fundamentally new valuation framework emerged that captured what DCF misses (real-options approaches come close for some firms; behavioral-finance approaches don't replace DCF, they qualify it). For now, DCF + multiples + DDM remains the working consensus.

## Still puzzling

The cleanest unresolved question this chapter sets up is *what to do when DCF, multiples, and DDM substantially disagree*. If they all agree to within 10-15%, the answer is easy. If they disagree by 50%, you have to decide which method to weight most heavily, and that decision is where the analyst's judgment lives. I don't have a clean rule for resolving disagreement. The honest framework is: each method has known biases; reason about which biases are most likely to apply to *this* firm in *this* market environment; weight accordingly. This is craft, not science.

---

## Connections forward

- **Chapter 12** examines historical equity returns — empirical context for the assumptions in DCF and DDM.
- **Chapter 13–14** install statistics and regression for measuring risk and computing beta.
- **Chapter 17** computes WACC, the firm's discount rate.
- **Chapter 18** forecasts the cash flows that go into DCF.
- **Chapter 20** frames the risk management required for the firm to deliver the forecast cash flows.

---

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

**John Burr Williams** was wrote The Theory of Investment Value (1938) — establishing the dividend discount model that still anchors stock valuation.

**Run this:**

```
Who is John Burr Williams, and how does their work connect to stock valuation we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about their career or ideas.
```

→ Search **"John Burr Williams"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to apply John Burr Williams's framework to a specific finance question.
- Add a constraint: "Answer including criticisms or limits of John Burr Williams's framework."

What changes? What gets better? What gets worse?
