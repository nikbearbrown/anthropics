# Chapter 5 — The Cost of Capital and the WACC

## TL;DR

- A number that looks precise and isn't, sitting atop inputs that could move it by a hundred basis points without anyone being wrong.
- The chapter moves through Warm-up, Application, Synthesis, Challenge, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

*A number that looks precise and isn't, sitting atop inputs that could move it by a hundred basis points without anyone being wrong.*

Maya, drafting her cover note for Diane on Friday morning, types: *"The project's NPV at the firm WACC of 8% is positive."* She stops. Where did 8% come from?

The footnote in the operations team's spreadsheet cites it as "the firm WACC, per the FP&A team's most recent update." She walks down to FP&A. The lead analyst there, Priya, opens a worksheet titled "WACC FY26 Q1." It uses a 5.2% pretax cost of debt, a 9.8% cost of equity derived from CAPM with a beta of 1.1, a 4.2% risk-free rate, and a 5.0% market risk premium; a target debt-to-capital weight of 30%; and a marginal tax rate of 24%. The blended number rounds to 8.0%.

Each of those inputs is a choice. None of them is obviously wrong. Several could plausibly be defended as different numbers. If the cost of equity were 11% instead of 9.8%, the WACC would round to 8.6% instead of 8.0%, and Plant 4's NPV would drop by something like 15%. The decision Maya is about to recommend turns on numbers Priya updated last quarter and nobody has questioned since.

This chapter is about what those numbers mean, where the judgment lives, and why the formula is both essential and surprisingly easy to get wrong.

---

Before working through the inputs, I want to say something about what "cost of capital" actually means, because the phrase does three different jobs and the three are easy to blur.

The first meaning is a rate of return that capital providers expect. When equity holders give Halverson their money, they expect to earn some return — through dividends, share appreciation, or both — that compensates them for the risk of holding Halverson's stock. That expected return is, from Halverson's perspective, the cost of using their money. The same logic applies to bondholders: they lend at 5.2% because that is the rate they require given Halverson's credit risk. The cost of capital is what the providers require.

The second meaning is a hurdle rate the firm uses for investment decisions. When evaluating Plant 4, the firm needs a discount rate. That rate has to be at least as high as the cost of capital, or the project does not generate enough return to satisfy the providers. So the cost of capital is the threshold a project must clear.

The third meaning is the weighted average of debt and equity costs. Most firms use both, in proportions reflecting their capital structure. The weighted average of these two costs, adjusted for the tax deductibility of interest, is the WACC.

![Triangle diagram with three nodes labeled "Provider Required](images/05-the-cost-of-capital-and-the-wacc-fig-01.png)
*Figure 5.1 — Triangle diagram with three nodes labeled "Provider Required*

In the textbook treatment, all three meanings collapse into one: the WACC is the hurdle rate, and the hurdle rate equals what providers require. In practice they can drift apart. A firm whose stated WACC is 8% but whose investors actually require 11% is systematically mispricing its investments — taking on projects that destroy value while believing it is creating it. The CFO's job is to keep the three aligned. You cannot do that if you treat the WACC as a number someone else computes and puts in a footnote.

---

The formula is:

$$\text{WACC} = \frac{E}{V} \cdot R_e + \frac{D}{V} \cdot R_d \cdot (1 - T)$$

where $E$ is the market value of equity, $D$ is the market value of debt, $V = E + D$ is total firm value, $R_e$ is the cost of equity, $R_d$ is the pretax cost of debt, and $T$ is the marginal corporate tax rate. Six inputs. Let me take them in order of how much judgment each one requires — starting with the mechanical ones and working toward the contested ones.

| Input | Halverson's value | Source | Degree of judgment |
|---|---|---|---|
| **E (market equity)** | $1,840M | Shares outstanding × current price | **Low** (looked up) |
| **D (market debt)** | $660M | YTM-implied market value of outstanding debt | **Low** |
| **R_d (pretax cost of debt)** | 5.2% | YTM on outstanding bonds | **Low** |
| **Tax rate (T)** | 24% | Marginal — federal + state, blended | Medium (statutory vs. effective is a judgment) |
| **Weights E/V and D/V** | 73.6% / 26.4% (book); 50/50 (target) | Book vs. target — the choice itself is a judgment | **High** |
| **R_e (cost of equity from CAPM)** | 9.8% | $r_f + \beta(\text{ERP})$ — beta = 1.1, ERP = 5.0%, $r_f$ = 4.2% | **High** (every input argued) |

**Market values, not book values.** The formula calls for the market values of $E$ and $D$, not the book values from the balance sheet. For equity this is unambiguous: shares outstanding times current price. The book value of equity reflects accumulated retained earnings and historical accounting choices; it is almost never the right denominator. For debt, the market value differs from book when interest rates have moved since the bonds were issued. Halverson issued $300M of bonds at 5% in 2021. If current market rates for similarly rated debt are 5.2%, those bonds trade at a slight discount. The difference is small for investment-grade debt with modest rate moves and large for distressed debt or significant rate shifts. The discipline is simple: use market values when available, document clearly when you substitute book values.

**The cost of debt.** This is the easiest input. Halverson's existing bonds trade at some yield-to-maturity in the market. That yield is the market's current required return on Halverson's credit risk. Look it up. Use the yield on *new* debt at Halverson's current risk profile, not the coupon on old debt issued under different conditions. Then multiply by $(1 - T)$ to capture the tax shield — every dollar of interest reduces taxable income by one dollar, saving the firm $T$ cents in taxes. At a 24% marginal rate, a pretax cost of debt of 5.2% becomes an after-tax cost of 4.0%.

The tax adjustment is one of the genuinely mechanical parts of the formula. Congress decided that interest payments are deductible and equity dividends are not. The WACC captures that asymmetry by putting debt on an after-tax basis. This is correct, but it means the WACC depends on the tax code — any change in the marginal corporate rate changes the WACC even if the underlying business does not change at all. The formula is accurate. The number it produces is contingent.

**The weights.** The formula calls for $E/V$ and $D/V$, but there is a question underneath: which capital structure? Today's, or the one the firm is moving toward?

The conventional answer is target weights — the proportions the firm intends to maintain over the long run — on the theory that capital budgeting is a long-horizon exercise and the current structure is a snapshot. If Halverson is currently running at 25% debt but targets 30%, using target weights produces a lower WACC (more weight on cheaper after-tax debt). Whether this is right depends on how credible the target is, and credibility requires judgment.

The subtler point is that the weights should match the project, not just the firm. If Plant 4 will be financed differently from Halverson's average project — say, with project finance debt secured against the plant itself — then the appropriate WACC for Plant 4 uses the plant's own financing mix, not the firm average. Using firm-average weights for a project with above-average debt capacity understates the benefit of the tax shield; using it for a project with below-average debt capacity overstates it. The formula is right. The question is which capital structure to plug in.

---

Now to the input that carries the most uncertainty: the cost of equity.

There is no yield-to-maturity for equity. Equity has no contractual cash flows, no maturity date, no promised return. The cost of equity is not observed; it is inferred. The standard tool for the inference is the Capital Asset Pricing Model:

$$R_e = R_f + \beta \cdot (R_m - R_f)$$

where $R_f$ is the risk-free rate, $\beta$ is the firm's systematic risk — its sensitivity to market-wide movements — and $(R_m - R_f)$ is the equity risk premium, the extra return the market as a whole is expected to earn above the risk-free rate.

Three inputs, each with its own source of uncertainty. Let me take them in turn.

**The risk-free rate.** The standard proxy is the yield on US Treasury securities — no credit risk, no material liquidity risk, so the yield represents pure time value of money. The question is which maturity. Short-term Treasury bills yield one thing; 10-year notes yield something higher; 30-year bonds higher still. The term spread between short and long rates has historically been 50 to 100 basis points, and that flows directly into the WACC.

The right answer is to match the project's horizon. For a three-month working capital decision, use the three-month rate. For Plant 4, with a 25-year asset life, the 10-year or 30-year rate is appropriate. Priya used 4.2%, which is a current 10-year Treasury yield — reasonable for a long-horizon capital project.

**Beta.** Halverson's beta of 1.1 came from a regression of weekly stock returns against the S&P 500, probably over the past two years. That regression produces a point estimate with a standard error. The true beta — the parameter governing the relationship between Halverson's returns and market returns going forward — is unobservable. Different lookback windows produce different estimates. Different benchmark indices produce different estimates. Bloomberg and Yahoo Finance often report different betas for the same firm because they use different regression specifications.

A beta of 1.1 means that historically, when the market moved 1%, Halverson moved about 1.1% in the same direction. A beta of 1.0 is average market risk; below 1.0 is below-average; above 1.0 means the stock amplifies market movements.

The standard error on a two-year weekly regression is roughly 0.15 to 0.25. So Halverson's beta of 1.1 is better described as a point estimate within a range of approximately 0.9 to 1.3 — and each point in that range produces a different cost of equity. The precision of "beta = 1.1" is illusory.

**The equity risk premium.** This is the most contested input in corporate finance. The equity risk premium — how much extra return equity investors require above the risk-free rate, as compensation for the additional risk of owning stocks — has been debated for decades, and there is no settled answer.

Historical estimates, computed from realized stock and bond returns over different time periods, range from roughly 4% to 7% depending on how far back you go, whether you use arithmetic or geometric averaging, and which markets you include. The academic literature has a name for the observation that historical equity returns have been surprisingly high relative to bond returns: the equity premium puzzle. The puzzle is that the historical premium implies a degree of risk aversion among investors that is hard to reconcile with observed behavior.

Forward-looking estimates — derived by working backward from current market prices to the implied expected return — tend to come in lower, around 4% to 5% in current conditions. Priya used 5.0%, which is a defensible choice — squarely in the middle of the reasonable range. But it is not the only defensible choice. And that matters.

Notice what this means for the WACC. The equity risk premium has a defensible range of perhaps 4.5% to 6.0%. At the low end, $R_e = 4.2\% + 1.1 \times 4.5\% = 9.15\%$. At the high end, $R_e = 4.2\% + 1.1 \times 6.0\% = 10.8\%$. Combine this with the uncertainty in beta — say, 1.0 to 1.3 — and the range widens further. The WACC formula looks precise. It produces a number like 8.0%. But the number is sitting atop inputs that could move it by 100 to 150 basis points in either direction without anyone making a clearly wrong choice.

---

Let me make that concrete. With Priya's inputs:

$$R_e = 4.2\% + 1.1 \times 5.0\% = 9.7\%$$

Round to 9.8%. Pretax cost of debt 5.2%, after-tax 4.0%. Target weights 70% equity, 30% debt:

$$\text{WACC} = 0.70 \times 9.8\% + 0.30 \times 4.0\% = 6.86\% + 1.20\% = 8.06\%$$

Rounds to 8.0%. Now run a sensitivity. Suppose beta is 1.3 instead of 1.1 — within the standard error of most estimates. And suppose the equity risk premium is 6.0% instead of 5.0% — equally defensible. Then:

$$R_e = 4.2\% + 1.3 \times 6.0\% = 12.0\%$$

With the same debt and weights:

$$\text{WACC} = 0.70 \times 12.0\% + 0.30 \times 4.0\% = 8.40\% + 1.20\% = 9.60\%$$

| | ERP 4.5% | ERP 5.0% | ERP 6.0% |
|---|---|---|---|
| **β = 0.9** | 7.5% | 7.7% | 8.1% |
| **β = 1.1** (base) | 7.8% | **8.0%** | 8.6% |
| **β = 1.3** | 8.2% | 8.5% | 9.6% |

*The defensible WACC for Halverson runs roughly 7.5% to 9.6% depending on β and ERP. The base case of 8.0% sits near the optimistic corner of the grid — anyone arguing for a higher β or higher ERP would push the rate to 8.5–9.6%.*

Plant 4's NPV at 9.6% is substantially lower than at 8.0%. Whether it is still positive depends on the project's cash flows, but the decision can flip. Maya is about to recommend approval of a major capital project on the basis of an NPV that is sensitive, in an unknown direction, to inputs nobody has revisited since last quarter.

This is not a failure of analysis. It is the correct picture of the uncertainty. The failure would be to pretend the picture is sharper than it is.

---

There is one more thing to say before closing, and it concerns when the firm WACC is the wrong discount rate even if it is computed correctly.

The WACC is the right discount rate for a project when the project has the same risk profile as the firm average. Halverson's WACC of 8% reflects the risk of Halverson's existing portfolio of assets — its mix of products, geographies, and operating characteristics. If Plant 4 looks like the average Halverson project, use 8%. If it does not, you need a different number.

The question of whether it does is an operational one, not a financial one. A new plant producing existing products in an existing market is probably close to the firm average. A new plant in an unfamiliar geography, producing a product Halverson has never made, carries additional risk that should be reflected in the discount rate. How much additional? Estimate beta from comparable companies or comparable projects in that market, plug into CAPM with that beta, compute a project-specific $R_e$, and build a project-specific WACC.

Operations teams almost never do this. The FP&A spreadsheet has one WACC for all projects. Maya's job, on this particular memo, is to check: does Plant 4 look like a typical Halverson investment? If so, 8% is the right number. If it represents a departure — new geography, new product line, different operating leverage — the right rate is probably higher, and the NPV that looks positive at 8% should be stress-tested at 10% or 12% before the recommendation goes to Diane.

![Decision tree for choosing the right discount rate: firm WACC, comparable-firm-derived project WACC, or management uplift](images/05-the-cost-of-capital-and-the-wacc-fig-01.png)
*Figure 5.1 — Choosing the right discount rate*

The operations team's footnote does not specify which case applies. This is Maya's flag for the memo.

---

The WACC is mechanical to compute and conceptually fragile. Six inputs, three of them judgment calls, and the output drives every capital budgeting decision the firm makes. A CFO who treats it as a settled number has quietly handed capital allocation authority to the analyst who last updated the spreadsheet.

The defensible move is the one Maya is learning to make for every analytical claim in this book: state the assumption set explicitly, document the range of plausible inputs, run the sensitivities, and name what would change the decision. Not because the formula is hard — it is not — but because the inputs to the formula are softer than the formula's precision implies.

8.0% is a number. The question it answers — what rate of return does Halverson need to earn to keep its capital providers satisfied, on the margin, for this class of investment — is a question with a real answer that the formula approximates. The approximation is useful. Taking it for the answer is where the trouble starts.

---

*A note on what this chapter simplified.* The CAPM is the standard approach to cost of equity but not the only one. Multifactor models — Fama-French three-factor, Carhart four-factor — incorporate additional risk premia for size, value, and momentum, and produce systematically different $R_e$ estimates. The CAPM is also a single-period model being applied to a multi-period problem; strictly, the discount rate should vary by period if the risk-free rate or risk premium changes over time. The WACC also assumes the capital structure — and therefore the tax shield — remains constant over the project's life, which is an approximation for any project with scheduled debt repayment. These refinements matter less for most capital budgeting decisions than getting the right beta and ERP range. But they matter, and Chapter 9 will return to them.

---

## Exercises

### Warm-up

**1.** Using the WACC formula, compute the weighted average cost of capital for a firm with the following inputs: cost of equity 10.5%, pretax cost of debt 6.0%, marginal tax rate 21%, target debt-to-capital weight 35%. Show each step. What is the after-tax cost of debt, and why does the formula use the after-tax figure rather than the pretax one? *(Tests: mechanical WACC calculation; tax shield logic)*

**2.** A firm's beta is reported as 1.2 by Bloomberg and 0.95 by Yahoo Finance for the same stock on the same day. Is one of them wrong? Explain in plain language why two sources can report different betas for the same firm, and what a practitioner should do when the estimates diverge. *(Tests: understanding of beta estimation; regression specification choices)*

**3.** Halverson currently carries 25% debt in its capital structure but has publicly stated a target of 30%. Should Priya use 25% or 30% as the debt weight in the WACC calculation? State the conventional answer and the assumption it requires. *(Tests: current vs. target weights; the theory underlying the target-weight convention)*

---

### Application

**4.** Reconstruct Priya's WACC calculation using her stated inputs ($R_f = 4.2\%$, $\beta = 1.1$, ERP $= 5.0\%$, $R_d = 5.2\%$, $T = 24\%$, 30% debt weight). Then build a two-way sensitivity table: vary beta across 0.9, 1.1, and 1.3, and vary the ERP across 4.5%, 5.0%, and 6.0%. Report all nine WACC values. Which input has the larger effect on the result across its plausible range? *(Tests: WACC computation; sensitivity analysis; identifying the dominant source of uncertainty)*

**5.** Plant 4 generates projected free cash flows of $18M per year for 20 years. Compute its NPV at discount rates of 8.0%, 8.6%, and 9.6%. (Use the annuity formula: $NPV = CF \times \frac{1-(1+r)^{-n}}{r}$, ignoring terminal value for simplicity.) At which rate, if any, does the project cross from positive to negative NPV? What does this tell you about the relationship between WACC uncertainty and the capital budgeting decision? *(Tests: NPV sensitivity to discount rate; connecting WACC range to go/no-go decisions)*

**6.** Halverson is considering acquiring a small renewable energy developer — a business with meaningfully different risk characteristics from its core industrial operations. The FP&A spreadsheet will default to applying Halverson's 8.0% WACC to the acquisition's projected cash flows. Write a one-paragraph memo flag — the kind Maya would attach to the analysis before sending it to Diane — explaining why the firm WACC may be the wrong discount rate and what Priya should do instead. *(Tests: project-specific WACC; translating technical judgment into business communication)*

---

### Synthesis

**7.** The chapter identifies three distinct meanings of "cost of capital": the return providers require, the hurdle rate for investment decisions, and the weighted average of debt and equity costs. In theory they are the same number; in practice they can drift. Describe a realistic scenario in which a firm's stated WACC diverges meaningfully from what its equity investors actually require. What is the practical consequence of that divergence for capital allocation? *(Tests: the three-meaning distinction; connecting misalignment to value destruction)*

**8.** The tax deductibility of interest makes debt cheaper than equity on an after-tax basis, which lowers the WACC as debt weight increases. If this logic holds, why don't firms simply load up on debt to minimize WACC and maximize firm value? What is missing from the WACC formula that limits this strategy in practice? *(Tests: understanding the tax shield; limits of the WACC framework; connection to capital structure theory in later chapters)*

**9.** A colleague argues that the equity risk premium debate is academic noise — practitioners should just use 5% and move on. Construct the strongest version of that argument. Then construct the strongest counterargument, using the Plant 4 NPV calculation as a concrete example. Conclude with your own view on how much precision is appropriate when estimating the ERP for a single capital budgeting decision. *(Tests: understanding the ERP range; connecting input uncertainty to decision outcomes; epistemic judgment)*

---

### Challenge

**10.** The WACC formula assumes the capital structure — and therefore the tax shield — remains constant over the project's life. For a project financed with a term loan that amortizes to zero over ten years, this assumption clearly fails: the debt weight falls from, say, 40% to 0% as the loan is repaid. Describe qualitatively how this violates the WACC's assumptions, and explain what analytical approach a practitioner could use instead to correctly value the project's tax shield under a declining debt schedule. (You do not need to compute a full solution — explain the logic.) *(Tests: identifying the limits of the constant-WACC assumption; pointing toward APV as an alternative framework)*

---

###  LLM Exercise — Chapter 5: The Cost of Capital and the WACC

**Project:** Halverson's Board Memo, Built Across the Course
**What you're building this chapter:** The WACC Section of the memo: the firm WACC computed from first principles, stress-tested against ±100bp on each input, and defended against the FP&A footnote version.
**Tool:** Claude Code

---

**The Prompt:**

```
I'm working on Halverson's Board Memo. The capital-budget portfolio is in `analysis/04-portfolio-ranked.md`.

Chapter 5 taught:
- **The three meanings of cost of capital** — provider required return, hurdle rate, weighted-average cost — and how they drift apart in real firms
- **The WACC formula**: $\text{WACC} = (E/V) \cdot r_e + (D/V) \cdot r_d \cdot (1-T_c)$
- **Sensitivity** — small input changes can move the WACC by 100+ bp, which moves NPV by double-digit percentages

Scaffold `analysis/05-wacc.py`:

1. **Compute the cost of equity via CAPM.** $r_e = r_f + \beta \cdot (E[r_m] - r_f)$. Pull β by regressing your firm's monthly returns on the S&P 500 over the last 5 years (use `yfinance`). Use the current 10-year Treasury for $r_f$. Use 5.5% as the historical equity risk premium (or defend a different number).

2. **Compute the cost of debt.** Average yield-to-maturity on the firm's outstanding debt, from the 10-K's debt schedule. If unavailable, use the rating-implied yield (BBB ≈ Treasury + 150bp; BB ≈ Treasury + 350bp).

3. **Compute the WACC.** Use the *target* debt-to-capital ratio (not the book ratio) — pull from the firm's stated capital-structure policy or use the trailing 5-year average.

4. **Stress-test.** Build a ±100bp sensitivity table: rows are each input ($r_f$, β, equity risk premium, $r_d$, target debt weight, marginal tax rate), columns are -100bp / -50bp / 0 / +50bp / +100bp. Cells are the resulting WACC.

5. **Re-rank the Chapter 4 portfolio at the new WACC.** Take the corner of the sensitivity table that most plausibly represents *the WACC the FP&A team should be using next quarter*. Re-run the knapsack from `analysis/04-budget-portfolio.py`. Did the prioritization change? Which projects moved into or out of the recommended set?

6. **Produce `analysis/05-wacc.md`** containing: the WACC point estimate with provenance for each input, the sensitivity table, the alternative-WACC re-ranking, and a one-paragraph defense of the WACC the board memo will adopt.

Run with `python analysis/05-wacc.py --ticker [TICKER]`.
```

---

**What this produces:** A runnable script `analysis/05-wacc.py` plus `analysis/05-wacc.md` containing the WACC point estimate, the sensitivity table, the impact on the Chapter 4 portfolio, and the defended adopted rate.

**How to adapt this prompt:**

- *For your own project:* Substitute your firm for Halverson where Halverson appears; the exercise structure is firm-agnostic. Halverson's named cast (Diane / Priya / Cardinal) is scaffolding — replace as needed.
- *For ChatGPT / Gemini:* Works as-is. For ChatGPT, save the running memo to a Custom GPT instead of a Claude Project. For Gemini, paste the project's accumulated section files into the context window each session.
- *For Claude Code:* Right tool — pulling beta from `yfinance`, building the sensitivity table, and re-ranking the portfolio is multi-step quantitative work.
- *For a Claude Project:* Append to the project. The defended WACC here is the headline rate the rest of the memo discounts at.

**Connection to previous chapters:** Chapter 4 used a placeholder WACC; Chapter 5 produces the defended rate and shows what changes when the rate moves.

**Preview of next chapter:** Chapter 6 asks whether *the same* WACC is the right rate for *every* project — or whether some projects (high-risk, optionality-heavy) need their own rate.

---

##  AI Wayback Machine
The ideas in this chapter didn't appear from nowhere. **Fischer Black** was co-developing the option-pricing apparatus, *and* — less famously — extending CAPM into the *zero-beta model* in 1972, which is the foundational case for how a firm's cost of capital is actually estimated when borrowing rates differ from the textbook risk-free rate decades before most people had heard of the cost of capital and the weighted average cost of capital (WACC). Here's a prompt to find out more — and then make it better.

![Fischer Black, c. 1980s. AI-generated portrait based on a public domain photograph (Wikimedia Commons).](images/fischer-black.jpg)
*Fischer Black, c. 1980s. AI-generated portrait based on a public domain photograph.*

![Fischer Black](../images/fischer-black-4o2.png)

*Puppet Art by [Nik Bear Brown](https://www.nikbearbrown.com/).*

**Run this:**

```
Who was Fischer Black, and how does his 1972 *zero-beta CAPM* — extending Sharpe's model to handle the realistic case where borrowing and lending rates differ — connect to the chapter's apparatus for estimating a firm's cost of equity, cost of debt, and weighted average cost of capital? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.
```

→ Search **"Fischer Black"** on Wikipedia after you run this. See what the model got right, got wrong, or left out.

**Now make the prompt better.** Try one of these:

- Ask it to explain *the zero-beta CAPM* in plain language, as if you've already seen the standard CAPM
- Ask it to compare Black's adjustment to the practical case where a firm's borrowing rate is 7% and the risk-free Treasury is 3%
- Add a constraint: "Answer as if you're writing the cost-of-capital methodology section of a corporate finance policy"

What changes? What gets better? What gets worse?
