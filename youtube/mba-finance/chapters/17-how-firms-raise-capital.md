# Chapter 17 — How Firms Raise Capital

*Why a company swimming in cash still borrows money — and what the answer tells you about the cost of capital.*

---

Apple ended fiscal 2020 with about $191 billion in cash and short-term investments. It generates roughly $100 billion in free cash flow per year. By any reasonable measure, it has more money than it can spend.

And yet, by the end of that same fiscal year, Apple had nearly $113 billion in long-term debt outstanding. It had been issuing bonds every year since 2013.

Why does a company with more cash than the GDP of several small countries borrow money?

The puzzle is real, and its resolution explains something fundamental about how firms think about capital. Debt is not simply a sign of need. It is a tool with a specific economic property that equity lacks: the interest payments are tax-deductible. When Apple borrows at 4% and pays interest, it deducts that interest from taxable income. At a 21% corporate tax rate, each dollar of interest saves 21 cents in taxes. The effective cost of borrowed money is not 4% — it's $4\% \times (1 - 0.21) = 3.16\%$. Meanwhile, a dollar of equity costs Apple whatever shareholders demand for holding Apple stock — historically somewhere in the 8–10% range — with no tax offset at all.

That gap is why firms borrow even when they don't need to. Cheap capital, cheapened further by the tax code, is worth using.

This chapter builds the **WACC** — the weighted-average cost of capital — from its components. WACC is the rate the firm must earn on its investments to satisfy both creditors and shareholders. It's the discount rate for every project in Chapter 16 and the denominator in every DCF valuation from Chapter 11. Getting it right is the central technical task of equity research.

---

## The cost of debt

For a firm with bonds trading in the market, the cost of debt is the **yield to maturity** — the rate the market demands to hold the firm's debt right now. This is not the coupon rate printed on the bond certificate. That's a historical number, set when the bond was issued. The YTM is a current number, driven by current credit conditions, current interest rates, and the market's current view of the firm's default risk.

From Chapter 10, the YTM is the $y$ that solves:

$$\text{Bond price} = C \times \frac{1 - (1+y)^{-n}}{y} + \frac{F}{(1+y)^n}$$

where $C$ is the coupon, $F$ is the face value, and $n$ is the number of periods. If the bond is trading below par, the YTM exceeds the coupon. If above par, the YTM is below the coupon. The market price tells you what the market is actually demanding.

After the YTM, apply the tax adjustment:

$$r_d^{\text{after-tax}} = r_d \times (1 - T)$$

For bonds yielding 6% with a 21% corporate tax rate:

$$r_d^{\text{after-tax}} = 6\% \times 0.79 = 4.74\%$$

The 1.26-percentage-point reduction is the **interest tax shield** — the government's implicit subsidy of corporate borrowing, through the deductibility of interest. Equity has no comparable subsidy. This is the structural reason that debt is cheaper than equity, net of taxes, and why rational capital structure includes some debt.

For the project: find your company's outstanding bonds in the 10-K debt footnote, look up current trading yields, and apply the effective tax rate. That's your after-tax cost of debt.

---

## The cost of equity

Equity's cost is harder to observe because there's no contract. Shareholders don't have a coupon — they have a claim on residual cash flows and an expectation of return that has to be inferred rather than read off a bond screen.

Two methods produce defensible estimates.

**Method 1: CAPM.** The method installed in Chapter 14:

$$r_e = R_f + \beta_e \times (E[R_m] - R_f)$$

A firm with $\beta_e = 1.3$, a current 10-year Treasury yield of 4.5%, and an equity risk premium of 5%:

$$r_e = 4.5\% + 1.3 \times 5\% = 11.0\%$$

CAPM works for all firms, dividend-paying or not.

**Method 2: Dividend Growth Model.** For firms with stable, predictable dividends:

$$r_e = \frac{D_1}{P_0} + g$$

where $D_1$ is next year's expected dividend, $P_0$ is today's stock price, and $g$ is the long-run dividend growth rate. This is the Gordon model rearranged: instead of computing a price, we compute the implied discount rate from the observed price.

For a stock at $12.50, next dividend $1.53, growth rate 2%:

$$r_e = \frac{1.53}{12.50} + 0.02 = 12.24\% + 2.0\% = 14.24\%$$

CAPM says 11.0%. DGM says 14.24%. Both are valid methods applied correctly to the same firm. The 3.2-point gap is not an error — it's the honest uncertainty in estimating the cost of equity. The right response is to report both and use sensitivity analysis, not to pick the one that produces the valuation you want.

**Flotation costs.** If the firm issues new equity (rather than using retained earnings), investment banking fees and registration costs add roughly 5-10% to the gross proceeds. The DGM adjusts:

$$r_{e,\text{new}} = \frac{D_1}{P_0 - F} + g$$

where $F$ is the flotation cost per share. For most analysis, retained-earnings cost is the right input — firms generally fund ongoing operations from internal cash flow and issue new equity only for material expansion. When they do issue, the flotation-cost adjustment matters.

<!-- → [TABLE: side-by-side comparison of CAPM vs. DGM for cost of equity — columns: method, inputs required, when it works well, when it breaks down; include one numerical example showing both methods applied to the same firm and the resulting gap; caption: both methods are correct in their domain; disagreement signals genuine uncertainty, not a calculation error] -->

---

## WACC: the weighted average

With component costs in hand, WACC is the weighted average:

$$\text{WACC} = D\% \times r_d(1-T) + P\% \times r_{\text{pfd}} + E\% \times r_e$$

where $D\%$, $P\%$, and $E\%$ are the fractions of total capital represented by debt, preferred equity, and common equity — weighted by **market values**, not book values.

The market-value weighting is not a formality. A firm with $1B of book debt trading at 70 cents on the dollar has $700M of market-value debt. Using book value instead would overstate the debt weight, understate the equity weight, and produce a biased WACC. Market values are what capital providers actually own; those are the weights that reflect their economic stakes.

**A complete example.** Bluebonnet Industries.

Market values: $4.85M debt, $15.0M equity, $19.85M total. Weights: $D\% = 24.4\%$, $E\% = 75.6\%$.

Cost of debt (YTM): 6.31%. After-tax: $6.31\% \times 0.79 = 4.99\%$.

Cost of equity (CAPM): $\beta = 1.3$, $R_f = 3\%$, ERP = 8%: $r_e = 3 + 1.3 \times 8 = 13.4\%$.

$$\text{WACC} = 0.244 \times 4.99\% + 0.756 \times 13.4\% = 1.22\% + 10.13\% = 11.35\%$$

With DGM cost of equity (14.24%):

$$\text{WACC} = 0.244 \times 4.99\% + 0.756 \times 14.24\% = 1.22\% + 10.77\% = 11.99\%$$

The two approaches give 11.35% vs. 11.99% — a 0.64-point spread. In a DCF with a 5-year explicit forecast, that difference moves the firm value by several percentage points. Reporting a single WACC number is false precision. Report the range.

<!-- → [CHART: tornado chart (or waterfall) showing WACC sensitivity — starting from a base-case WACC of ~11%, showing how much it shifts when each input changes by ±1 standard deviation: beta ±0.2, ERP ±1%, cost of debt ±0.5%, D% ±5%; student should see which input dominates WACC uncertainty for a typical firm] -->

**Practical inputs.** The four biggest sources of noise in WACC:

*Beta.* Different data sources give different betas. Yahoo Finance and Bloomberg regularly disagree by 0.2 to 0.3 for the same stock. Best practice: run your own 5-year monthly regression (Chapter 14) and compare to published sources.

*Equity risk premium.* Reasonable estimates range 4–7%. Most equity research uses 4.5–5.5%. A one-point change in ERP moves cost of equity by one beta-unit — for a high-beta stock, that's a 1.5-point cost-of-equity swing.

*Risk-free rate.* Use the Treasury yield matching the investment horizon. For a long-run DCF, use the 10-year yield, not the 90-day T-bill.

*Tax rate.* Use the marginal rate — the rate on the next dollar of income — not the average effective rate. For US firms post-2017, the federal marginal rate is 21%; combined federal + state is typically 25–28%.

---

## Modigliani-Miller: the clean theory

Before confronting real-world capital structure, understand what the clean theory says.

Franco Modigliani and Merton Miller proved in 1958 that, in a world with no taxes, no transaction costs, perfect information, and no bankruptcy costs, **capital structure is irrelevant to firm value**. Their argument is elegant: a firm's value depends on the cash flows from its assets, not on how those cash flows are divided between debt and equity holders. The total pie doesn't change with the slicing.

**MM Proposition I:** Levered firm value = unlevered firm value.

**MM Proposition II:** The cost of equity rises with leverage, in exact proportion: $r_E = r_U + \frac{D}{E}(r_U - r_D)$. As you add cheaper debt, the equity becomes riskier (residual claim on a more leveraged firm) and demands a higher return. The two effects cancel. WACC stays constant.

A numerical illustration. T-shirt business, $40K invested, $52K expected cash flow, WACC = 14%.

| Capital structure | $r_d$ | $r_e$ | WACC |
|---|---|---|---|
| 100% equity | — | 14.0% | 14.0% |
| 11% debt / 89% equity | 4% | 15.2% | 14.0% |
| 37% debt / 63% equity | 4% | 19.9% | 14.0% |
| 88% debt / 12% equity | 10% | 42.5% | 14.0% |

WACC is constant across all leverage levels. The rising cost of equity exactly offsets the lower weight on cheap debt. In the perfect-markets world, there's literally nothing to optimize in capital structure.

<!-- → [CHART: three-line chart showing MM Proposition II — x-axis: debt-to-total-capital from 0% to 80%; three lines: (1) cost of debt (nearly flat, rising slightly at high leverage), (2) cost of equity (rising linearly with leverage), (3) WACC (flat/constant); student should see visually how the rising equity cost exactly offsets the leverage benefit, keeping WACC constant in perfect markets] -->

The reason MM matters is not because the world is perfect. It's because MM tells you *why* capital structure matters in the real world: it's the things the model left out.

---

## Why capital structure matters: taxes and distress

**Taxes create a benefit to leverage.** Interest is deductible. Equity dividends are not. So the *after-tax* cost of debt is lower than MM assumed, and adding debt creates a **tax shield** — a real increase in firm value.

With taxes, MM Proposition I becomes:

$$V_L = V_U + T \times D$$

The levered firm is worth more by the present value of the tax shield. For the T-shirt business at a 28% tax rate, $7,000 in debt at 4% generates $280 in annual interest, a $78.40 tax saving per year. Present value of the shield: approximately $560. Firm value rises from $45,614 to $46,174.

By pure tax logic, firms should borrow as much as possible. They don't. Something else is working in the opposite direction.

**Financial distress costs create a penalty to high leverage.** As debt rises, the probability of default rises. With distress comes direct costs — legal fees, bankruptcy proceedings, asset liquidations at depressed prices — and indirect costs that are often larger: customers and suppliers walk away, key employees leave, management gets distracted managing the crisis rather than the business. For technology and pharmaceutical firms with brand-dependent value, intangible assets, and firm-specific human capital, distress is particularly devastating. Distress costs can run 10–20% of pre-distress firm value.

The two forces define the **trade-off theory** of optimal capital structure:

$$V_L = V_U + T \times D - \text{PV(distress costs)}$$

At low leverage: tax shield large relative to distress costs. Increase leverage.
At moderate leverage: both effects growing; diminishing returns to more debt.
At high leverage: distress costs dominate. Decrease leverage.

There is an interior optimum — the capital structure that maximizes firm value by balancing the two forces.

<!-- → [CHART: trade-off theory diagram — x-axis: debt level (D), y-axis: firm value; three curves: V_U (horizontal baseline), V_U + PV(tax shield) (rising), and V_L = V_U + PV(tax shield) - PV(distress costs) (hump-shaped); optimal D* labeled at the peak; student should see why the optimum is interior and why it shifts based on firm characteristics] -->

Different industries land at very different optimal leverage ratios for exactly this reason:

| Industry | Typical debt-to-total-capital | Why |
|---|---|---|
| Software / online retail | ~7–15% | High intangible value, high distress costs, high growth |
| Consumer staples | ~30–40% | Stable cash flows, tangible assets, low distress costs |
| Telecom | ~45% | Regulated revenue, capital-intensive, reliable cash flow |
| Airlines | ~60%+ | Capital-intensive; arguably over-leveraged given cyclicality |

For the equity research project: find your company's debt-to-equity ratio. Compare to industry peers. Significant deviation in either direction warrants explanation — either there are firm-specific reasons it belongs off-industry-average, or there's a capital-allocation story to tell.

---

## Pecking order: a complementary theory

The trade-off theory says there is an optimal capital structure that firms target. The **pecking order theory** (Myers and Majluf, 1984) says that in practice, firms don't start from an optimal target — they follow a financing hierarchy driven by information asymmetry.

The argument: managers know more about the firm's prospects than the market does. When a firm issues equity, the market interprets it as a signal that management thinks the stock is overvalued (why else sell shares now?). The stock price typically falls on equity issuance announcements. Debt issuance is less of a signal — it doesn't announce that management thinks the firm is expensive. And internal funds (retained earnings) involve no signaling at all.

The resulting pecking order:
1. **Internal funds** (retained earnings): first choice. No flotation costs, no signaling.
2. **Debt**: second choice. Modest issuance costs, modest signaling.
3. **External equity**: last resort. Expensive and interpreted badly.

Pecking order explains why high-cash-flow firms tend to carry less debt than trade-off theory would predict — they fund everything internally and don't need to borrow toward an optimal target. It also explains why distressed firms that have exhausted debt capacity issue equity reluctantly and at poor timing.

Trade-off and pecking order are not mutually exclusive. The honest answer is that both forces operate, and their relative importance varies by firm.

---

## What WACC means for the project

WACC is the firm's hurdle rate. Every investment is evaluated against it: if a project's IRR exceeds WACC, it creates value; if it falls short, it destroys value. In the DCF from Chapter 11, WACC is the discount rate applied to every future free cash flow.

The number you computed in this chapter — with its sensitivity range — replaces the 8% placeholder from Chapter 11. Run the DCF both ways. If the fair-value range shifts materially, your investment thesis depends on where WACC lands, and you should say so.

Capital structure analysis also tells you something qualitative. A firm issuing equity at a low stock price is signaling confidence (or desperation). A firm issuing debt is signaling stable cash flow confidence. A firm aggressively buying back stock is saying it believes the shares are cheap. These signals don't always bear out, but they're data.

For the deliverable: compute your firm's WACC with a sensitivity range. Assess its capital structure against industry peers. Note any recent financing activity and what it signals. Then update the Chapter 11 DCF with the real discount rate and report the updated fair-value range.

---

## Exercises

### Warm-up

**17.1** Define WACC. Write the formula including all three component costs. Explain in one sentence why each component is present.
*(Tests: basic WACC structure and the conceptual role of each term)*

**17.2** Why is the cost of debt multiplied by $(1 - T)$ in the WACC formula? Why isn't the cost of equity adjusted the same way?
*(Tests: the interest tax shield and the asymmetric tax treatment of debt vs. equity)*

**17.3** State MM Proposition I in plain English. State MM Proposition II. What is MM telling you about the real world by describing a world where it doesn't hold?
*(Tests: MM propositions and their role as a benchmark for identifying what actually matters in capital structure)*

### Application

**17.4** A firm has the following capital structure and component costs:

- Debt (market value): $300M; YTM: 5.8%
- Common equity (market value): $700M; beta: 1.4
- Tax rate: 25%
- 10-year Treasury yield: 4.0%
- Equity risk premium: 5%

(a) Compute the after-tax cost of debt.
(b) Compute the cost of equity using CAPM.
(c) Compute the capital structure weights.
(d) Compute WACC.
(e) The DGM gives a cost of equity of 13.5% instead. Recompute WACC. By how much does it change?

*(Tests: full WACC computation and the impact of cost-of-equity method choice)*

**17.5** A firm's unlevered value ($V_U$) is $80M. It is considering adding $20M of debt at a 25% tax rate. Distress costs are estimated to have a present value of $3M given this leverage level.

(a) Compute the levered firm value using the trade-off theory formula.
(b) Has value been created or destroyed by adding the debt?
(c) If the firm instead added $50M of debt, where distress costs rise to a PV of $12M, what is the new levered value? Is more or less debt preferable?
(d) Identify the approximate optimal debt level (max firm value) and explain what determines it.

*(Tests: trade-off theory formula and the identification of optimal leverage)*

**17.6** For your chosen company:

(a) Find the yield to maturity on the company's largest outstanding bond issue (from the 10-K debt footnote or a bond-pricing screen).
(b) Apply the effective tax rate to compute after-tax cost of debt.
(c) Use your CAPM cost of equity from Chapter 14.
(d) Compute market-value weights for debt and equity.
(e) Compute WACC. Run sensitivity: cost of equity ±1%, cost of debt ±0.5%, D% ±5 percentage points.

*(Tests: primary-source WACC construction from actual company data)*

### Synthesis

**17.7** Two firms in the same industry have nearly identical business profiles but very different capital structures: Firm Alpha has 15% debt-to-total-capital; Firm Beta has 55%.

(a) Using trade-off theory, construct an argument that Firm Alpha is under-leveraged and Beta is at or near optimal.
(b) Using pecking order theory, construct an alternative explanation: what does Beta's high leverage tell you about its financing history?
(c) What financial metrics — coverage ratios, cash flow stability, asset tangibility — would help you determine which explanation is more likely correct?

*(Tests: applying both capital structure theories to a real comparative scenario and identifying distinguishing evidence)*

**17.8** Apple's WACC is widely estimated at 8–9%. It generates roughly $100B per year in free cash flow and has spent over $80B per year on buybacks and dividends in recent years. Using Chapter 16 (NPV) and Chapter 17 (capital structure) principles:

(a) Under what condition is returning $80B+ per year to shareholders the value-maximizing decision?
(b) Under what condition would reinvesting more of it in the business create more value?
(c) What does the persistence of Apple's large buyback program signal under pecking order theory? Under trade-off theory?

*(Tests: integrating capital allocation and capital structure thinking around a well-known real case)*

### Challenge

**17.9** Build the WACC sensitivity table for your chosen company: cost of equity at three levels (CAPM estimate, CAPM − 1%, CAPM + 1%) across rows; D% at three levels (current, current − 5pp, current + 5pp) across columns. Nine WACC estimates.

Then re-run your Chapter 11 DCF at each of the nine WACC levels and record the resulting value-per-share. Report: (a) the minimum and maximum value-per-share across all nine cases; (b) which input — cost of equity or capital structure — drives more DCF variability; (c) whether your Buy/Hold/Sell recommendation from Chapter 11 holds across all nine scenarios, or only in some.

*(Tests: integrated WACC–DCF sensitivity analysis and the investment-thesis stability test)*

**17.10** A firm with stable cash flows and 20% debt-to-capital is considering a leveraged recapitalization — issuing $2B in debt and using the proceeds to buy back equity. The firm's marginal tax rate is 28%.

(a) Compute the present value of the incremental tax shield created by the additional $2B in debt.
(b) Estimate qualitatively how distress costs would change, given the firm's stable cash flows and tangible-asset base.
(c) Using the trade-off theory, make a quantitative and qualitative case for whether the recapitalization creates or destroys value.
(d) What signal would the recapitalization send to the market under pecking order theory — and how would you expect the stock price to react on announcement?

*(Tests: applying the full trade-off and signaling framework to a concrete financing decision, integrating tax shield arithmetic with qualitative judgment)*

---

## What would change my mind

The chapter argues that trade-off theory plus WACC is the right framework. Two things would revise it. First, if pecking order turned out to be the dominant explanation for observed capital structures — it fits the data well but doesn't displace the normative case for trade-off. Second, if WACC estimation were so noisy as to be useless — the inputs are genuinely uncertain, but sensitivity analysis bounds the uncertainty into a usable range. Neither revision has arrived. WACC remains the working consensus for both practice and pedagogy.

## Still puzzling

The cleanest unresolved question: when CAPM and DGM give substantially different cost-of-equity estimates, which one do you weight? The methods rest on different assumptions. CAPM is forward-looking in its inputs but backward-looking in its beta. DGM requires dividends to exist and a stable growth rate to project. When they disagree by 3 points, no clean rule resolves it. The honest practice is to report both, use the midpoint or a conservative average, and acknowledge the uncertainty explicitly in the sensitivity analysis. Anyone who presents a single WACC number without a range is either extremely confident or not being entirely honest.

---

## Connections forward

- **Chapter 18** uses WACC as the discount rate in pro forma forecasting.
- **Chapter 19** addresses working capital — short-term financial decisions.
- **Chapter 20** addresses risk management, including the risks that affect capital structure choice.

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

**Franco Modigliani** co-developed the Modigliani-Miller theorem on capital structure — Nobel 1985.

**Run this:**

```
Who is Franco Modigliani, and how does their work connect to raising capital we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about their career or ideas.
```

→ Search **"Franco Modigliani"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to apply Franco Modigliani's framework to a specific finance question.
- Add a constraint: "Answer including criticisms or limits of Franco Modigliani's framework."

What changes? What gets better? What gets worse?
