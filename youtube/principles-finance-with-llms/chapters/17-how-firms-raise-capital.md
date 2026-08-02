# Chapter 17 — How Firms Raise Capital

**Suggested titles**
1. WACC and the Mix
2. Debt, Equity, and Why Apple Borrows
3. The Cost of Capital

**TL;DR.** A firm's cost of capital — the **WACC** — is the weighted average of the costs of its debt and equity, with debt's cost adjusted for its tax-deductibility. WACC is the discount rate the firm uses to evaluate every project. Choosing the right capital structure (the mix of debt vs. equity) is a balance: debt is cheaper but increases default risk; equity is more expensive but more flexible. The optimal mix depends on the firm's industry, cash flow stability, and growth profile.

---

## The puzzle of Apple's debt

Apple held about $191 billion in cash and short-term investments at the end of fiscal 2020. The company generates roughly $100 billion in free cash flow per year. By any measure, it has more cash than it can possibly need.

And yet, Apple has issued tens of billions of dollars in long-term debt since 2013, with nearly $113 billion in total debt outstanding by the end of fiscal 2020.[^1] Why does a company with more cash than the GDP of several small countries borrow money?

[^1]: Apple Form 10-K filings via EDGAR. `[verify]` for current vintage.

Three reasons, all of which this chapter unpacks.

**1. Debt is tax-deductible. Equity is not.** When Apple borrows at 4% and pays interest, it deducts that interest from taxable income. The federal corporate tax rate is 21%, so each dollar of interest saves Apple 21 cents in taxes. The *effective* cost of the borrowed dollar is 4% × (1 - 0.21) = 3.16%. By contrast, a dollar of equity raised costs whatever the cost of equity is — typically 8-10% for a firm like Apple — with no tax shield.

**2. Apple's cash is largely held overseas (historically) or in short-term securities yielding less than its cost of debt.** Borrowing was, until tax reform, a way to fund US obligations (dividends, buybacks) without repatriating overseas cash and triggering tax. The structural reason has changed since 2017's tax reform, but the broader logic — borrowing at low rates to fund higher-return uses — remains.

**3. Capital structure has its own logic.** A firm that operates entirely on equity gives up the financial leverage that magnifies returns to shareholders. A firm that operates entirely on debt cannot survive a recession. The right answer is somewhere in the middle, and finding that middle is what capital structure theory is for.

This chapter computes the firm's **cost of capital** — the rate of return it must earn on its investments to satisfy both creditors and shareholders. The number that comes out, **WACC**, is the discount rate every project from Chapter 16 should be evaluated against. It's also the discount rate that goes into the DCF model in Chapter 11. WACC is one of the most important numbers a financial analyst computes.

---

## Learning objectives

After working through this chapter, you should be able to:

- Compute the after-tax cost of debt for a firm using its outstanding bond yields.
- Compute the cost of equity using CAPM and (where applicable) the dividend growth model.
- Compute the firm's WACC given component costs and capital structure weights.
- Apply Modigliani-Miller propositions to capital structure decisions.
- Explain the trade-off theory of optimal capital structure.
- Recognize the practical issues in WACC estimation (beta source, equity premium, flotation costs).

**Prerequisites.** Chapter 10 (bonds), Chapter 11 (stocks), Chapter 14 (CAPM), Chapter 12 (historical returns).

---

## Concept 1 — The three component costs

A firm raises capital from three sources: debt, common equity, and (sometimes) preferred equity. Each has its own cost. WACC is the weighted average.

### Cost of debt

For a firm with outstanding bonds, the **cost of debt** is the **yield to maturity** the market demands. From Chapter 10:

$$\text{Bond price} = C \times \frac{1 - (1+y)^{-n}}{y} + \frac{F}{(1+y)^n}$$

Solve for $y$ given the current price. That's the YTM, and it's the firm's pre-tax cost of debt.

But debt has a tax advantage that equity doesn't. Interest payments are deductible from taxable income; dividend payments are not. So the *effective* cost of debt is the YTM times $(1 - T)$, where $T$ is the marginal corporate tax rate:

$$r_d^{\text{after-tax}} = r_d \times (1 - T)$$

For a firm with bonds yielding 6% and a 21% tax rate:

$$r_d^{\text{after-tax}} = 0.06 \times (1 - 0.21) = 0.0474 = 4.74\%$$

The 1.26 percentage points of tax savings is the **interest tax shield** — the part of the firm's interest payment that the government effectively subsidizes through reduced taxes.

For your equity research project: read your chosen company's debt footnote in the 10-K. Find the weighted-average yield on its outstanding bonds (or compute it from the largest bond issues). Apply the firm's effective tax rate. That's your after-tax cost of debt.

### Cost of equity (common stock)

The cost of equity is the rate of return shareholders demand for holding the firm's common stock. Unlike debt, it isn't directly observable — there's no contractual rate. We have to estimate it.

**Method 1: CAPM** (Chapter 14):

$$r_e = R_f + \beta_e \times (E[R_m] - R_f)$$

where:
- $R_f$ = risk-free rate (10-year Treasury yield)
- $\beta_e$ = the firm's equity beta
- $E[R_m] - R_f$ = equity risk premium (4-6% range)

For a firm with $\beta_e = 1.3$, $R_f = 4.5\%$, ERP = 5%:

$$r_e = 4.5\% + 1.3 \times 5\% = 11.0\%$$

CAPM is the standard method and works for all firms.

**Method 2: Dividend Growth Model** (Chapter 11):

For dividend-paying firms with stable growth:

$$r_e = \frac{D_1}{P_0} + g$$

where $D_1$ is next year's dividend, $P_0$ is the current share price, and $g$ is the long-run dividend growth rate.

For a firm with $D_1 = 1.53$, $P_0 = 12.50$, $g = 2\%$:

$$r_e = \frac{1.53}{12.50} + 0.02 = 12.24\% + 2\% = 14.24\%$$

The dividend growth model gives a different answer than CAPM in many cases. The honest approach: compute both, average them, or use the higher of the two as a conservative estimate.

### Cost of preferred equity

If the firm has preferred stock outstanding, its cost is the dividend yield:

$$r_{\text{pfd}} = \frac{D_{\text{pfd}}}{P_{\text{pfd}}}$$

For a preferred stock paying $2.00 annually with a current price of $21.80:

$$r_{\text{pfd}} = \frac{2.00}{21.80} = 9.17\%$$

Preferred dividends are typically not tax-deductible, so the cost of preferred equity is not adjusted for taxes (unlike debt).

### Cost of new equity vs. retained earnings

Retained earnings are equity capital the firm has already accumulated; using them costs the cost of equity (no flotation costs).

Issuing new equity has additional costs — investment banking fees, legal fees, registration. **Flotation costs** typically run 5-10% of the gross offering amount.

The cost of new equity adjusts the dividend growth model:

$$r_{e,\text{new}} = \frac{D_1}{P_0 - F} + g$$

where $F$ is the flotation cost per share. If flotation is $0.75 on a $27.50 stock with $D_1 = 3.05$ and $g = 1.5\%$:

$$r_{e,\text{new}} = \frac{3.05}{26.75} + 0.015 = 11.40\% + 1.5\% = 12.90\%$$

vs. retained earnings: $\frac{3.05}{27.50} + 0.015 = 12.59\%$.

The 0.31% gap is the flotation cost. For most analyses, retained-earnings cost is the right metric (firms generally fund growth from internal cash flow and only issue new equity for material expansion).

↳ **Dig Deeper — The implied cost of capital approach**

*CAPM and DGM are the standard approaches to cost of equity. A third approach — implied cost of capital (ICC) — backs out the discount rate that reconciles current stock price with analyst consensus forecasts. Some practitioners argue ICC is more forward-looking than CAPM and more market-grounded than DGM. The academic evidence is mixed but interesting.*

**Prompt:**
> Explain the implied cost of capital approach: starting from current stock price and consensus analyst forecasts of future earnings or dividends, solve for the discount rate that makes the DCF equal to the current price. Then summarize empirical work (Gebhardt, Lee, and Swaminathan 2001 is a starting point) on whether ICC predicts future returns better than CAPM. What's the strongest case for using ICC, and what's the strongest case against?

**What to do with the output:** Save it. ICC is intermediate-finance content; the practical version of the discount-rate selection problem this chapter wrestles with.

### The trade-off (concept 1)

Component costs trade **observability against accuracy**. Cost of debt is highly observable (current bond yields). Cost of equity requires estimation with multiple defensible methods that often disagree. The wider the disagreement, the more sensitivity analysis the WACC computation needs.

### Common misconceptions

- *"Cost of debt is the coupon rate."* No — it's the yield to maturity (current market rate), not the historical coupon.
- *"Cost of equity is the dividend yield."* Dividend yield is part of the cost of equity (in the DGM), but only part. The growth rate matters. CAPM ignores dividends entirely.

---

## Concept 2 — WACC: putting it together

WACC is the weighted average of component costs, with weights determined by market values.

### The formula

$$\text{WACC} = D\% \times r_d (1-T) + P\% \times r_{\text{pfd}} + E\% \times r_e$$

where:
- $D\%, P\%, E\%$ are the firm's debt, preferred, and common equity weights (must sum to 100%)
- $r_d, r_{\text{pfd}}, r_e$ are the component costs

The weights are based on **market values**, not book values. A firm with $5M of book debt trading at 97% of face value has a market value of debt of $4.85M; a firm with 1M shares outstanding at $15 has equity market value of $15M; the weights are computed from those market values.

### Worked example — a complete WACC

Bluebonnet Industries.

**Capital structure (market values):**
- Debt: $4.85M
- Equity: $15.0M
- Total: $19.85M
- D% = $4.85/$19.85 = 24.4%
- E% = $15.0/$19.85 = 75.6%

**Component costs:**
- Cost of debt (YTM): 6.31%
- After-tax cost of debt: 6.31% × (1 - 0.21) = 4.99%
- Cost of equity (CAPM, β = 1.3, $R_f$ = 3%, ERP = 8%): $r_e = 3 + 1.3 \times 8 = 13.4\%$

**WACC:**

$$\text{WACC} = 0.244 \times 4.99\% + 0.756 \times 13.4\% = 1.22\% + 10.13\% = 11.35\%$$

If we'd used the dividend growth model for cost of equity instead (giving 14.24%):

$$\text{WACC} = 0.244 \times 4.99\% + 0.756 \times 14.24\% = 1.22\% + 10.77\% = 11.99\%$$

The two methods give 11.35% vs. 11.99% — a 0.6-percentage-point spread. Honest WACC analysis reports this range.

### Practical issues

WACC computation is more sensitive to its inputs than the formula's simplicity suggests. The major sources of imprecision:

**Beta estimation.** Different data sources give different betas. Yahoo Finance might say IBM has β = 0.97; MarketWatch might say β = 1.25. The cost of equity, and hence WACC, can swing by 2-3 percentage points depending on the source. Best practice: use a 5-year monthly regression against a broad market index, and report the value alongside other source estimates.

**Risk-free rate choice.** Use the Treasury yield matching the project horizon. For a long-term project or DCF, use the 10-year Treasury. For shorter-term work, the 5-year. Don't use the 30-day T-bill yield — it's volatile and doesn't match the long-term equity discount rate.

**Equity risk premium.** Estimates range from 4% to 7%. Most equity research uses 4.5-5.5%. The choice meaningfully affects WACC.

**Tax rate.** Use the firm's marginal tax rate (the rate that applies to the next dollar of income), not the effective tax rate (which is averaged across all income, including any tax credits or deductions). For US firms post-2017 reform, the federal marginal rate is 21%, plus state income taxes; the combined marginal rate is typically 25-28%.

For your equity research project, run sensitivity on these inputs:
- Beta ± 0.2
- ERP at 4%, 5%, 6%
- Cost of equity using both CAPM and DGM if applicable

The resulting WACC range is what you should report. A point estimate is overconfident.

### Net debt vs. gross debt

Some analysts use **net debt** (total debt minus cash and cash equivalents) instead of gross debt for capital structure weights. The argument: cash on the balance sheet effectively offsets debt, since the firm could pay down debt with cash if needed.

Apple end-2020:
- Gross debt: $112.4B
- Cash and short-term securities: $38.0B
- Net debt: $74.4B

Using net debt changes the weights and the WACC calculation. For a cash-rich firm like Apple, the difference can be substantial. There's no universal right answer; document which you used and be consistent.

↳ **Dig Deeper — Buybacks vs. dividends as capital allocation choices**

*A firm with $5B of excess cash can return it to shareholders via dividend or via stock buyback. The two are economically equivalent in a frictionless world but very different in real markets — taxation, signaling, market timing, executive compensation incentives all matter.*

**Prompt:**
> Compare dividends and stock buybacks as capital-return mechanisms. Cover (1) tax differences for shareholders, (2) signaling effects of each, (3) the timing question (does management buy back stock at attractive valuations or at market peaks?), (4) the impact on EPS arithmetic vs. economic value, (5) the role of executive compensation tied to EPS metrics. Cite empirical evidence on whether buybacks have on average created value (Manuel et al., or Fortune 500 buyback timing studies).

**What to do with the output:** Save it. Most large public companies do substantial buybacks; understanding whether they're value-creating or value-destroying is part of the project's capital-allocation analysis.

### The trade-off (concept 2)

WACC trades **a single number for a complex reality**. The firm's actual capital structure changes over time, beta isn't constant, the equity premium varies, and tax rates depend on jurisdiction and structure. Any single WACC estimate is, at best, a snapshot of one specific moment. Sensitivity analysis is the discipline that makes WACC usable.

### Common misconceptions

- *"WACC is the firm's required rate of return."* It's the rate that satisfies all capital providers on average. Debt holders have specific contractual returns; equity holders demand the cost of equity. WACC averages them, weighted by capital share.
- *"Higher leverage always lowers WACC because debt is cheaper."* Not always — increased leverage raises the cost of equity (riskier residual claim) and eventually starts raising the cost of debt (default risk). The U-shaped trade-off is the subject of Concept 3.

---

## Concept 3 — Choosing the right capital structure

Why do firms borrow at all? Why do they cap their borrowing at some level? The answers come from a famous theoretical result and its practical caveats.

### Modigliani-Miller (in perfect markets)

Franco Modigliani and Merton Miller (1958, 1963) proved that, in perfect markets — no taxes, no transaction costs, perfect information, no bankruptcy costs — **capital structure is irrelevant to firm value**. The theoretical argument:

A firm's value depends on the cash flows from its assets, not how those cash flows are sliced into claims. Whether the firm is funded with 100% equity or 50% debt / 50% equity, the total cash flow generated is the same. Splitting it between debt and equity holders just changes who gets which slice; the total pie is unchanged.

**MM Proposition I:** $V_L = V_U$ (value of levered firm = value of unlevered firm).

**MM Proposition II:** $r_E = r_U + \frac{D}{E}(r_U - r_D)$. As leverage rises, the cost of equity rises proportionally to compensate for higher residual risk. WACC stays constant.

A worked example illustrates: T-shirt business with $40K investment, $52K expected cash flow.

| Capital structure | $r_d$ | $r_E$ | WACC |
|---|---|---|---|
| 100% equity | n/a | 14.0% | 14.0% |
| 11% debt / 89% equity | 4% | 15.2% | 14.0% |
| 37% debt / 63% equity | 4% | 19.9% | 14.0% |
| 88% debt / 12% equity | 10% | 42.5% | 14.0% |

WACC is constant because the rising cost of equity exactly offsets the lower weight on cheaper debt. In this perfect-markets world, capital structure is genuinely irrelevant.

### Why MM doesn't fully apply: taxes and distress

In the real world, two MM assumptions break.

**Taxes break MM.** Interest is tax-deductible. Equity dividends are not. So the *after-tax* cost of debt is lower than its pre-tax cost. The interest tax shield creates a benefit to leverage that pure MM ignores.

The tax-adjusted MM proposition: $V_L = V_U + (T \times D)$. The firm's value rises by the tax shield.

For the T-shirt business at 28% tax rate:
- Unlevered firm value: $45,614
- Levered firm with $7,000 debt at 4%: tax shield = 0.28 × $280 = $78.40 per year, present value of tax shield ≈ $560
- Levered firm value: $46,174

Higher leverage produces more tax shield, which raises firm value. By this logic, firms should borrow as much as possible.

**Financial distress costs break MM in the other direction.** As leverage rises, the probability of default rises. With distress comes:
- Direct costs (legal, consulting, asset auctions during bankruptcy)
- Indirect costs (customers and suppliers walk away; key employees leave; managers get distracted)
- Lost growth options (the firm can't raise capital for new projects when distressed)

Distress costs are real and substantial, particularly for firms with high asset specificity (technology firms, pharmaceutical firms with brand-dependent products). The empirical estimate: total distress costs can run 10-20% of pre-distress firm value.[^2]

[^2]: Andrade and Kaplan (1998) and follow-on research. `[verify]` for current consensus.

### Trade-off theory

Combining the two:

$$V_L = V_U + (T \times D) - \text{PV of distress costs}$$

At low leverage: tax shield large; distress costs small. Firm value rises with leverage.
At moderate leverage: tax shield grows; distress costs start rising. Diminishing returns.
At high leverage: distress costs dominate. Firm value falls.

There's an **optimal capital structure** where firm value is maximized — the point where the marginal tax-shield benefit equals the marginal distress-cost penalty. Different industries have different optima:

| Industry | Typical D% | Why |
|---|---|---|
| Online retail | ~7% | High volatility, high growth, intangible assets — high distress costs |
| Software | ~10-15% | Similar profile |
| Telecom | ~45% | Stable cash flows, regulated revenue — low distress costs |
| Tires/rubber | ~64% | Capital-intensive, mature, stable | 
| Airlines | ~62% | Capital-intensive, but cyclical — actually overleveraged in many cases |

For your equity research project: compute your chosen company's debt-to-equity ratio. Compare to industry peers. If it's significantly higher or lower than peers, ask why. The disagreement might be efficient (firm-specific reasons) or it might be evidence of capital-allocation issues.

### Pecking order theory

A complementary theory: firms prefer financing in this order:

1. **Internal funds (retained earnings)** — no flotation costs, no signaling issues.
2. **Debt** — modest costs, doesn't signal anything bad about prospects.
3. **External equity** — most expensive, and (importantly) often interpreted as a negative signal that management thinks the stock is overvalued.

Pecking order explains why firms with strong internal cash flow generally don't issue much debt or equity, and firms that need outside capital prefer debt to equity. Empirically, this matches observed financing patterns better than pure trade-off theory.

### When firms should issue what

A practical guide:

- **Strong cash flow + low leverage**: continue to fund internally; consider buybacks if cash piles up.
- **Strong cash flow + leverage at target**: maintain.
- **Strong cash flow + over-target leverage**: pay down debt.
- **Insufficient cash flow + below-target leverage**: issue debt up to target.
- **Insufficient cash flow + at or above target leverage**: equity issuance becomes the option, despite higher cost.

For the equity research project: when your chosen company makes major financing announcements (debt issuance, equity offering, stock buyback), the decision tells you something about management's view of the firm's prospects. A firm issuing equity at a low stock price is signaling it thinks the cost of equity is right or even cheap. A firm issuing debt is signaling confidence in its cash flow stability.

### Worked example — assessing a leverage decision

Suppose your chosen company announces a $5B debt issuance at a 5% coupon. The firm's existing capital structure:
- Equity (market): $200B
- Debt (market): $50B before the issuance
- Cost of equity: 10%
- Cost of debt: 4.5%
- Tax rate: 25%

Existing WACC: 0.20 × 4.5% × 0.75 + 0.80 × 10% = 0.675% + 8.0% = 8.675%

After the issuance, debt = $55B; equity ≈ $200B (assuming the proceeds are used productively):
- D% = 55/255 = 21.6%; E% = 200/255 = 78.4%
- New cost of debt: assume the additional debt is at 5% (slightly higher reflecting marginally more risk) — blended cost of debt rises to ~4.55%
- Cost of equity: marginal increase to ~10.1% (slightly riskier residual claim)

New WACC: 0.216 × 4.55% × 0.75 + 0.784 × 10.1% = 0.737% + 7.92% = 8.66%

The WACC barely changes. But the firm has $5B more cash for projects (capex, buybacks, acquisitions). Whether this is value-creating depends on what the cash is used for.

### The trade-off (concept 3)

Capital structure trades **expected return amplification against bankruptcy risk**. Debt amplifies returns to equity holders when things go well — a leveraged firm earns higher ROE for the same operating performance. Debt amplifies losses too — a leveraged firm in trouble can quickly fail. The right level of leverage depends on the firm's cash flow stability, growth profile, and tolerance for volatility.

### Common misconceptions

- *"Firms should minimize WACC."* Sort of. They should *maximize firm value*, which usually means low-but-not-zero WACC. Going to extremely high leverage to minimize WACC eventually creates distress risk that destroys value.
- *"Capital structure doesn't matter."* In perfect markets (MM), no. In real markets with taxes and distress, it does — there's an optimum.

---

## Synthesis — WACC as the firm's universal hurdle rate

This chapter built the firm's cost of capital from its components:

- **Cost of debt** (YTM, after-tax adjustment for tax shield)
- **Cost of equity** (CAPM and/or DGM)
- **Cost of preferred** (if applicable)

Weighted by market-value capital structure shares, the result is **WACC** — the discount rate the firm uses for every project evaluation in Chapter 16, every DCF in Chapter 11, every pro forma in Chapter 18.

**Capital structure choice** balances the tax shield's benefit against financial distress costs. Different industries have different optima. Your chosen company's actual capital structure tells you something about its risk profile and management's view of the world.

For the equity research project, the deliverable from this chapter is:
1. Your firm's WACC (with sensitivity range).
2. An analysis of its capital structure relative to peers.
3. An assessment of whether recent capital structure decisions (debt issuance, buybacks, dividends) appear value-creating.

This number — WACC — feeds into the DCF model and the price target. Combined with the cash flow forecasts in Chapter 18, the equity research report converges to a final valuation.

---

## Exercises

### Warm-up

**17.1** Define WACC. State the formula including all three components.

**17.2** Why is the cost of debt adjusted for taxes? Why is the cost of equity not?

**17.3** Distinguish trade-off theory from pecking order theory.

### Application

**17.4** A firm has:
- $200M of debt at YTM 5.5%
- $800M of equity (market cap)
- Beta 1.2
- Tax rate 25%
- 10-year Treasury 4.5%, ERP 5%

Compute:
(a) Cost of equity using CAPM.
(b) After-tax cost of debt.
(c) Capital structure weights.
(d) WACC.

**17.5** Same firm announces a $200M debt issuance (raising D to $400M). Recompute WACC assuming costs stay roughly the same. By how much does WACC change?

**17.6** For your chosen company:
(a) Compute cost of debt from the largest bond outstanding (or weighted average of bond yields).
(b) Compute cost of equity using CAPM with beta from your Chapter 14 regression.
(c) Compute capital structure weights from market values.
(d) Compute WACC.
(e) Run sensitivity on beta and ERP.

### Synthesis

**17.7** A firm is choosing between issuing $1B of debt at 5% or $1B of equity at current prices. The firm's tax rate is 25%, and its current cost of equity is 11%. Construct a quantitative argument for and against each choice. What additional information would help decide?

**17.8** Two firms in the same industry have very different debt levels: Firm A is at 60% debt, Firm B at 20%. Three possible explanations: (a) different optimal levels, (b) Firm A is over-leveraged, (c) Firm B is under-leveraged. For each, identify what evidence (financial metrics, industry comparisons, management commentary) would distinguish them.

### Challenge

**17.9** Build a complete DCF for your chosen company using:
(a) The free cash flow projections you developed earlier (or estimate now).
(b) The WACC you computed in 17.6.
(c) Sensitivity analysis on WACC ± 1 percentage point.

Compare the resulting fair value range to the current market price. State your investment thesis (Buy/Hold/Sell with target price range).

**17.10** Apple's WACC is widely estimated at around 8-9% historically, and it generates roughly $100B of free cash flow per year. In recent years Apple has spent over $80B per year on buybacks and dividends. Argue (using Chapter 16 NPV principles and Chapter 17 capital structure principles) whether this is the right capital allocation or whether the cash should be used differently.

---

## Chapter summary

- **Cost of debt** = YTM × (1 - T). The after-tax adjustment captures the interest tax shield.
- **Cost of equity** can be estimated from CAPM ($r_e = R_f + \beta \times ERP$) or the Dividend Growth Model. Different methods often give different answers.
- **WACC** = $D\% \times r_d(1-T) + P\% \times r_{\text{pfd}} + E\% \times r_e$. Weights are market values.
- **MM Propositions** show that in perfect markets, capital structure doesn't affect firm value — WACC is constant across leverage choices.
- **Trade-off theory** adds taxes (favoring debt) and financial distress costs (limiting debt) — produces an optimal capital structure.
- **Pecking order theory**: firms prefer internal funds → debt → equity in that order.
- WACC is the firm's hurdle rate for every project (Chapter 16) and the discount rate for DCF (Chapter 11).

---

## What would change my mind

The chapter argues that the trade-off theory of capital structure (combined with WACC as the discount rate) is the right framework. The reading would have to revise if (a) compelling alternative theories of capital structure superseded trade-off — pecking order has merit but doesn't displace it, and behavioral theories haven't matured enough, or (b) practical estimation issues with WACC turned out to be so severe that the metric became unusable — they're severe but manageable with sensitivity analysis. WACC remains the working consensus.

## Still puzzling

The cleanest unresolved question is *what to do when CAPM and DGM give substantially different cost-of-equity estimates*. The two methods rest on different assumptions and can produce 2-3 percentage point differences. Honest practice is to report both and average; alternative methods (implied cost of capital from analyst forecasts) exist but aren't standard. The discount rate is the most sensitive input in the entire analysis, and getting it precisely right may not be possible.

---

## Connections forward

- **Chapter 18** uses WACC as the discount rate in pro forma forecasting.
- **Chapter 19** addresses working capital — short-term financial decisions.
- **Chapter 20** addresses risk management, including the risks that affect capital structure choice.

---

---

## LLM Exercise — Chapter 17: Compute Your Company's WACC

**Project:** Equity Research Report on a Chosen Public Company
**What you're building this chapter:** Compute your company's WACC using cost of equity from Chapter 14 and cost of debt from Chapter 10. This is the actual discount rate for your DCF.
**Tool:** Claude chat or Project.

### The Prompt

```
For [your company], compute WACC using the inputs we've already gathered:

### Input recap

- **Cost of equity** (from Chapter 14 CAPM): r_e = ___%
- **Cost of debt** (from Chapter 10 bond YTM): r_d = ___%
- **Effective tax rate** (from Chapter 5 income statement): T = ___%
- **Market value of debt**: from the 10-K (or use book value if market not available)
- **Market value of equity**: shares outstanding × current stock price

### Compute

1. **Capital structure weights** (using market values):
   - D% = D / (D + E)
   - E% = E / (D + E)

2. **WACC**:
   WACC = E% × r_e + D% × r_d × (1 - T)

3. **Sensitivity** — Recompute WACC at:
   - Cost of equity ±1 percentage point
   - Cost of debt ±0.5 percentage point
   - D% ±5 percentage points (different leverage assumption)
   Report the WACC range.

4. **Capital-structure assessment**:
   - How does the firm's D% compare to industry peers? Is the firm under- or over-leveraged?
   - Does the firm appear to have an explicit target capital structure? (Check the 10-K's MD&A and capital allocation discussions.)
   - Recent financing activity (debt issuances, buybacks): does it support or contradict the apparent target?

5. **Update the DCF** — Re-run your Chapter 11 DCF model using the WACC range you computed (instead of the 8% placeholder). Report the updated fair-value range.

Show all calculations.
```

### What this produces

The firm's actual WACC and an updated DCF using it. This is the most analytically important deliverable in the project after the initial DCF.

### How to adapt this prompt

- *For your own company:* Replace [your company].
- *For ChatGPT / Gemini:* Identical.
- *For Claude Code:* The WACC sensitivity could be a small Excel/Python script.

### Connection to previous chapters

Synthesizes Chapter 10 (cost of debt), Chapter 14 (cost of equity), Chapter 11 (DCF), and the firm's capital structure data from Chapter 5.

### Preview of next chapter

Chapter 18 builds pro forma forecasts. The Chapter 18 LLM Exercise will produce a 5-year three-statement projection with three scenarios — the cash flow inputs to the final DCF.

---

**Tags:** WACC, capital-structure, cost-of-capital, cost-of-debt, cost-of-equity, MM-propositions, trade-off-theory, pecking-order


---

## AI Wayback Machine

**Franco Modigliani** was co-developed the Modigliani-Miller theorem on capital structure — Nobel 1985.

**Run this:**

```
Who is Franco Modigliani, and how does their work connect to raising capital we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about their career or ideas.
```

→ Search **"Franco Modigliani"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to apply Franco Modigliani's framework to a specific finance question.
- Add a constraint: "Answer including criticisms or limits of Franco Modigliani's framework."

What changes? What gets better? What gets worse?
