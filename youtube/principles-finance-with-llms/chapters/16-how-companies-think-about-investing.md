# Chapter 16 — How Companies Think about Investing

**Suggested titles**
1. Capital Budgeting
2. NPV, IRR, and the Decisions Firms Have to Make
3. From Project to Portfolio of Projects

**TL;DR.** A firm with limited capital faces the same valuation problem an investor does, applied to its own internal projects: which projects increase shareholder value, and how do you rank competing options? The toolkit — payback, NPV, IRR, MIRR, profitability index — has clear hierarchy: **NPV is the gold standard for value creation**, with the others useful as supplementary checks. This chapter installs the toolkit and works through the cases where the methods disagree.

---

## The puzzle of two projects, two answers

A firm has two mutually exclusive projects to choose between. Both clear the firm's 9% cost of capital. The numbers:

| Project | Cost | NPV at 9% | IRR |
|---|---|---|---|
| Regular embroidery machine | $16,000 | $2,836 | 14.1% |
| Heavy-duty embroidery machine | $40,000 | $3,971 | 13.2% |

The IRR rule (pick the higher percentage return) says: regular machine. 14.1% beats 13.2%.

The NPV rule (pick the larger dollar value created) says: heavy-duty machine. $3,971 beats $2,836.

Both rules can't be right. Both are based on the same time-value-of-money math. Why do they disagree?

The IRR is a *rate* — it ignores project size. A 14.1% return on a $16,000 project produces less absolute wealth than a 13.2% return on a $40,000 project, even though the percentage is higher. NPV captures the absolute wealth difference; IRR doesn't.

When the two methods disagree, **NPV wins.** The firm's job is to maximize value — total dollars added to shareholder wealth. NPV measures that directly. IRR is a useful summary metric but a flawed decision rule under several common conditions.

For the equity research project, this chapter is essential because real firms make capital budgeting decisions all the time, and your job as an analyst is to evaluate whether they're making them well. A firm that consistently chooses lower-NPV projects because they have higher IRRs is making predictable mistakes, and the analytical signal is informative.

---

## Learning objectives

After working through this chapter, you should be able to:

- Compute payback period, discounted payback period, NPV, IRR, MIRR, and profitability index for a project.
- Apply the decision rule for each metric.
- Identify when NPV and IRR disagree, and explain why.
- Handle mutually exclusive projects, projects with unequal lives, and capital rationing.
- Recognize the multiple-IRR problem and apply MIRR as a workaround.

**Prerequisites.** Chapters 7-9 (TVM), Chapter 11 (DCF, valuation).

---

## Concept 1 — The decision rules

Five metrics serve five different purposes. We work through them in order of conceptual seriousness.

### Payback period

The simplest metric. **Payback period** is the number of years until the project's cumulative cash inflows recover the initial investment.

Example: A $16,000 machine produces $2,000 in year 1, $4,000 in year 2, and $5,000/year in years 3-6. Cumulative inflows reach $16,000 in year 4. Payback = 4 years.

**Decision rule** (informal): accept if payback is shorter than some threshold (3 years, 5 years — chosen by management).

**Strengths:** Simple. Quick. Easy to explain to non-finance audiences. Captures liquidity intuition.

**Weaknesses:**
1. **Ignores time value of money.** Treats $5,000 in year 5 the same as $5,000 in year 1.
2. **Ignores cash flows after the cutoff.** A project that pays back in 4 years and produces $50,000 more over the next 10 years looks identical to a project that pays back in 4 years and stops.
3. **Arbitrary threshold.** No principled answer for what payback period is "good enough."

For decision-making purposes, payback period is a supplementary metric, never the primary one.

### Discounted payback period

A modest improvement. **Discounted payback** uses the present-valued cash flows.

For Sam's project at 9% cost of capital:

| Year | Cash flow | PV factor | PV | Cumulative PV |
|---|---|---|---|---|
| 0 | -16,000 | 1.000 | -16,000 | -16,000 |
| 1 | 2,000 | 0.917 | 1,834.86 | -14,165.14 |
| 2 | 4,000 | 0.842 | 3,366.72 | -10,798.42 |
| 3 | 5,000 | 0.772 | 3,860.92 | -6,937.50 |
| 4 | 5,000 | 0.708 | 3,542.13 | -3,395.37 |
| 5 | 5,000 | 0.650 | 3,249.66 | -145.71 |
| 6 | 5,000 | 0.596 | 2,981.34 | 2,835.63 |

Discounted payback ≈ 5.05 years. The project recovers the discounted initial investment slightly into year 6. (Compared to undiscounted payback of 4 years.)

**Decision rule:** Same arbitrary threshold problem.

**Strengths:** Time-adjusted. Captures liquidity discipline.

**Weaknesses:** Still ignores cash flows beyond the cutoff. Still has an arbitrary threshold.

### Net Present Value (NPV)

The gold standard. From Chapter 9:

$$NPV = \sum_{t=0}^{n} \frac{CF_t}{(1+r)^t}$$

where $r$ is the firm's cost of capital and $CF_0$ is negative (the initial outflow).

For Sam's project at 9%:

$$NPV = \frac{-16{,}000}{1} + \frac{2{,}000}{1.09} + \frac{4{,}000}{1.09^2} + \frac{5{,}000}{1.09^3} + \frac{5{,}000}{1.09^4} + \frac{5{,}000}{1.09^5} + \frac{5{,}000}{1.09^6}$$

$$NPV = -16{,}000 + 1{,}835 + 3{,}367 + 3{,}861 + 3{,}542 + 3{,}250 + 2{,}981 = \$2{,}836$$

**Decision rule:** Accept if NPV > 0; reject if NPV < 0.

**Strengths:**
1. Incorporates time value of money.
2. Considers all cash flows over the project's life.
3. Has a clear decision rule grounded in shareholder wealth maximization.
4. Discount rate can be adjusted for project risk.
5. Value-additive: the NPV of a portfolio of projects equals the sum of individual NPVs.

**Weaknesses:**
1. Sensitivity to discount-rate assumption.
2. Less intuitive to communicate than a percentage return.
3. Doesn't handle capital rationing cleanly (you can compute NPV but ranking projects under a budget constraint requires the profitability index).

NPV is the right primary metric for capital budgeting. Other methods are supplementary.

### Internal Rate of Return (IRR)

The discount rate at which NPV = 0.

$$0 = \sum_{t=0}^{n} \frac{CF_t}{(1 + IRR)^t}$$

Solve for IRR using a financial calculator or `=IRR()` in Excel. For Sam's project, IRR = 14.09%.

**Decision rule:** Accept if IRR > cost of capital; reject if IRR < cost of capital.

**Strengths:**
1. Easy to communicate (a percentage return is intuitive).
2. Doesn't require specifying a discount rate to make the accept/reject decision.
3. Useful summary metric across multiple projects.

**Weaknesses:**
1. **Multiple IRRs.** When cash flows change sign more than once (initial outflow, then inflows, then another outflow — common for environmental cleanup or terminal-cost projects), there can be more than one mathematical solution. The Olympic-stadium example: $350M build, $950M operate, $620M demolish. The NPV profile crosses zero twice.
2. **Scale blindness.** A 25% IRR on $1,000 is preferred to a 15% IRR on $1,000,000 by the IRR rule, but the latter creates 600× more value in absolute terms.
3. **Reinvestment-rate assumption.** IRR implicitly assumes cash flows are reinvested at the IRR rate. For a 25% IRR project, that requires finding other 25% projects, which is rare.

### Modified Internal Rate of Return (MIRR)

Fixes IRR's reinvestment-rate problem. Three steps:
1. Compute the present value of all *outflows* at the cost of capital.
2. Compute the future value (at project end) of all *inflows*, compounded at the cost of capital.
3. Solve for the rate that grows step 1's PV into step 2's FV over the project's life.

For Sam's project:
- PV of outflows: $16,000 (just the initial)
- FV of inflows compounded at 9%: $31,595
- $16{,}000(1+i)^6 = 31{,}595$
- $i = (31{,}595/16{,}000)^{1/6} - 1 = 12.0\%$

MIRR = 12.0%.

Compare to IRR of 14.1%. The MIRR is lower because it assumes cash flows reinvest at 9% (the cost of capital), while IRR assumes they reinvest at 14.1% (the IRR itself). MIRR is more realistic.

**Decision rule:** Accept if MIRR > cost of capital.

**Strengths:** Single solution. Realistic reinvestment assumption.

**Weaknesses:** Still doesn't capture scale. Still requires choosing a cost of capital. Less commonly used than IRR despite its theoretical advantages.

### Profitability Index (PI)

A scaling measure for capital rationing.

$$PI = \frac{PV(\text{inflows})}{PV(\text{outflows})}$$

For Sam's project: $PI = 18,836 / 16,000 = 1.18$.

**Decision rule:** Accept if PI > 1 (equivalent to NPV > 0).

**Strengths:** Useful for ranking projects under budget constraints. Captures NPV per dollar invested.

**Weaknesses:** Equivalent to NPV for accept/reject decisions in the absence of constraints.

↳ **Dig Deeper — Real options in capital budgeting**

*Standard NPV treats capital projects as static — once committed, you proceed. But real projects often have flexibility: the option to expand if successful, abandon if unsuccessful, or delay the start. These flexibility features have value that NPV ignores.*

**Prompt:**
> Explain the four main types of real options in capital budgeting: option to expand, option to abandon, option to delay, option to switch. For each, give one industry example where it's most valuable (e.g., pharmaceutical R&D for option to abandon). Then briefly describe how option-pricing methods (Black-Scholes adapted, binomial trees) can be applied to real options. What practical limitations make real options analysis harder than the financial-options version?

**What to do with the output:** Save it. Real options are why some "negative NPV" projects are actually value-creating — and why some "positive NPV" projects need flexibility to deliver.

### The trade-off (concept 1)

The five metrics trade **comprehensiveness against simplicity**. Payback is simple but loses information. NPV is comprehensive but harder to communicate. IRR is intuitive but flawed in specific cases. The right approach for a capital-budgeting analysis: lead with NPV, supplement with IRR (with caveats), use PI for capital rationing, use MIRR when the reinvestment assumption matters.

### Common misconceptions

- *"All five metrics are equivalent for accept/reject decisions."* They are roughly equivalent for *standalone* projects with normal cash flow patterns. They diverge in important ways for ranking, mutually exclusive projects, and unusual cash flows.
- *"Higher IRR is always better."* Not when projects differ in scale or duration.

---

## Concept 2 — When the methods disagree

Three situations produce conflicts among the metrics. Each has a clean resolution.

### Conflict 1: Mutually exclusive projects

Two projects compete for the same resource — a factory site, a piece of equipment, an executive's time. The firm can do one but not both. Different metrics may rank them differently.

The chapter's opening puzzle: regular machine (NPV $2,836, IRR 14.1%) vs. heavy-duty machine (NPV $3,971, IRR 13.2%). IRR favors regular; NPV favors heavy-duty.

**Resolution:** When NPV and IRR disagree on mutually exclusive projects, **NPV wins**. The firm's objective is value creation, not rate maximization. The heavy-duty machine creates more value despite its lower percentage return.

### Conflict 2: Projects with unequal lives

A 3-year project with NPV of $50,000 vs. a 6-year project with NPV of $80,000. The 6-year project's NPV is larger, but it ties up resources for twice as long. Are they comparable?

Two methods to handle this.

**Replacement chain.** Repeat the shorter project to match the longer one's horizon. If the 3-year project has the same cash flows when repeated, build a 6-year cash flow model that does it twice. Compare to the 6-year project's NPV directly.

For OpenStax's truck example: old truck (3-year life, NPV $49,474) vs. new truck (6-year life, NPV $80,658). Chained over 6 years, two old trucks: $86,645 total NPV. Old truck wins.

**Equivalent annual annuity (EAA).** Convert each NPV to an annuity payment over the project's life:

$$EAA = \frac{NPV \times r}{1 - (1+r)^{-n}}$$

Compare the annuities directly. Higher annuity wins.

For the trucks at 10%: old truck EAA = $19,894/year; new truck EAA = $18,520/year. Old truck wins.

Both methods give the same ranking. Use whichever is cleaner for the analysis.

### Conflict 3: Capital rationing

The firm has more positive-NPV projects than capital. Rank them.

By NPV alone, you can't tell which combination of projects produces the highest *total* NPV given the budget. Use the **profitability index**: rank by PI, then accept projects in PI order until the budget is exhausted.

OpenStax example. Firm has $200M budget. Seven candidate projects:

| Project | NPV ($M) | Investment | PI | Rank by PI |
|---|---|---|---|---|
| A | 60 | 150 | 1.40 | 1 |
| E | 11 | 30 | 1.37 | 2 |
| F | 7 | 20 | 1.35 | 3 |
| D | 15 | 50 | 1.30 | 4 |
| B | 25 | 100 | 1.25 | 5 |
| G | 2 | 10 | 1.20 | 6 |
| C | 10 | 70 | 1.14 | 7 |

Rank by PI: choose A (cost $150M), E ($30M), F ($20M). Total cost: $200M. Total NPV: $78M.

If you'd ranked by NPV alone, you might have chosen A + B = $250M of investment, busting the budget; or A + D + B = $300M, even worse. Or A + B = top NPVs but $250M > $200M budget.

PI tells you: getting the most value per dollar means going with the highest PI projects until you can't fit another. This is the right answer under capital rationing.

↳ **Dig Deeper — How firms actually choose hurdle rates**

*The textbook says firms should use WACC (or a project-specific risk-adjusted rate) as the discount rate for capital projects. In practice, many firms use a single corporate hurdle rate for everything, often set well above WACC. Why?*

**Prompt:**
> Explain why corporate hurdle rates often exceed the firm's WACC. Three reasons frequently cited: (1) optimism bias in cash flow projections (the firm is correcting for systematic over-estimation), (2) capital rationing concerns (limited budget; need to prioritize), (3) "tradition" or executive risk aversion. Walk through evidence for each. Then argue: which is the strongest case, and which approaches the level of capital-misallocation that destroys shareholder value?

**What to do with the output:** Save it. Real corporate capital budgeting deviates from the textbook in predictable ways; understanding the deviations helps assess your project company's discipline.

### The trade-off (concept 2)

Method conflicts trade **simplicity against fidelity to the underlying optimization**. Each metric is right for some uses and wrong for others. The discipline is to know which conflict is operating and apply the right resolution. NPV is the value-creation metric; PI is the value-per-dollar metric for budget-constrained decisions.

### Worked example — your chosen company's recent capex

For your equity research project: identify a major capital expenditure your chosen company announced in the past two years. Most public companies disclose major capex in 8-K filings or in the MD&A section of the 10-K.

Estimate (using public information and reasonable assumptions):
- Initial investment.
- Annual cash flows over an estimated useful life.
- Cost of capital (use your WACC estimate from Chapter 17 once it's available; for now, approximate at 8-10%).

Compute NPV, IRR, payback. Decide whether the capex is value-creating. Compare to the firm's stated rationale in disclosures. Disagreements are analytically interesting and often inform investment thesis.

---

## Concept 3 — From mechanics to strategic capital allocation

The metrics tell you whether a single project clears a hurdle. Real corporate capital allocation is broader.

### Free cash flow estimation

The cash flows that go into NPV/IRR are not GAAP earnings. They are **incremental free cash flows**: the additional cash the firm generates *because* it does the project, net of all required reinvestment.

$$\text{Project FCF}_t = (\text{Revenue}_t - \text{COGS}_t - \text{Opex}_t) \times (1 - \tau) + \text{Depreciation}_t - \text{Capex}_t - \Delta \text{Working capital}_t$$

where $\tau$ is the tax rate.

The discipline: include only what the project changes. Don't include sunk costs. Don't ignore opportunity costs (using a building you already own to host the project means you can't use it for something else). Don't ignore cannibalization (if the new product steals revenue from existing products).

For an analyst evaluating a corporate decision, the FCF estimate is where the action is. Bad NPV decisions usually result from bad FCF estimation, not from bad arithmetic.

### Risk adjustment

The discount rate should reflect the project's risk, not just the firm's average cost of capital.

A diversified firm doing a low-risk project (replacing existing equipment) should discount at a rate below WACC. Doing a high-risk project (new market entry) should discount above WACC. In practice, many firms use WACC for everything, and the resulting decisions are biased — low-risk projects underapproved, high-risk projects overapproved.

For sophisticated capital budgeting, project-specific discount rates are computed from project beta and the project's debt capacity. This is intermediate finance; for principles-level work, WACC is the default.

### Real options

Standard NPV treats project decisions as static — once committed, you proceed. Real projects often have *flexibility*:
- The option to expand if successful.
- The option to abandon if unsuccessful.
- The option to delay the start.
- The option to switch technology mid-project.

These flexibility features have value that standard NPV misses. The field of **real options analysis** treats them explicitly using option-pricing methods. For analytical rigor in industries with high flexibility (biotech, energy exploration, technology), real options capture value the standard NPV underestimates.

For most projects, standard NPV is good enough. For projects with significant optionality, the analyst should at least flag that NPV likely understates value.

### Strategic context

Some projects have value beyond their direct NPV — they produce learning, build options for follow-on projects, signal to competitors, or protect existing market position. A defensive capex (matching a competitor's investment) might have negative direct NPV but positive total value if it prevents larger losses.

These are real considerations but hard to quantify. The discipline: present the NPV calculation honestly, then list the strategic considerations explicitly. Don't hide low NPV behind unquantified strategic claims.

### Worked example — Boeing's 787 Dreamliner

The 787 Dreamliner is a textbook capital-budgeting case. Boeing committed roughly $32 billion to develop the aircraft, expected to be recovered through aircraft sales over the next 30+ years. The development ran $20+ billion over budget and delivered three years late, with persistent quality issues that produced grounding events through 2024.

Was the project a good one? Hard to say definitively. By a narrow NPV measure with the actual cost overruns, the answer might be no. By a strategic-importance measure — Boeing maintaining technological leadership in widebody aircraft — the answer might be yes.

The case illustrates both the discipline of NPV (forces explicit estimation of cash flows) and its limits (can't fully capture strategic positioning). For the equity research project, capital-budgeting analysis should identify both the quantitative answer and the strategic factors that adjust it.

### The trade-off (concept 3)

Capital allocation trades **methodological rigor against business judgment**. The NPV machinery is rigorous and works well for projects with reasonably-known cash flows and risks. Strategic considerations are softer and harder to quantify. Both matter; neither replaces the other. A capital-budgeting analysis that produces a single NPV number with no qualitative discussion misses important context. An analysis that's all qualitative judgment with no NPV math is not analysis at all.

### Common misconceptions

- *"Sunk costs should be considered in NPV."* No. Sunk costs are gone regardless of the decision. Only incremental cash flows from the decision matter.
- *"Real options always justify going ahead."* Sometimes; sometimes the option value is small enough not to change the answer.
- *"Strategic value justifies low-NPV projects."* Sometimes — but the strategic value should be specifically articulated, not used as a catch-all justification.

---

## Synthesis — capital budgeting as the firm's investment problem

The firm faces, internally, the same problem an investor faces externally: pick the best uses of limited capital. The toolkit transferred from individual investing — TVM, NPV, risk-adjusted discounting — applies cleanly. The decision rules are clear in most cases:

1. **Lead with NPV.** It's the value-creation metric.
2. **Supplement with IRR** (with caveats about scale, multiple roots, reinvestment).
3. **Use PI for capital rationing.** Ranks NPV per dollar invested.
4. **Use MIRR when the reinvestment assumption matters.**
5. **Use payback only as a liquidity sanity check, never as primary criterion.**

The harder questions are upstream of the metrics: getting the cash flow estimates right, choosing the right discount rate, handling unequal lives, and deciding when strategic considerations justify deviating from the pure NPV answer. These are where analytical judgment matters.

For the equity research project, this chapter equips you to evaluate your chosen company's capital allocation. Are they investing in projects that look value-creating? Do their disclosures suggest they're using sound NPV-style discipline, or are they making predictable IRR-vs-NPV mistakes? The answer feeds into your investment thesis.

---

## Exercises

### Warm-up

**16.1** Define payback period, NPV, IRR, MIRR, and profitability index. State the decision rule for each.

**16.2** Why does NPV prevail over IRR when the two disagree on mutually exclusive projects?

**16.3** Explain the multiple-IRR problem. When does it arise?

### Application

**16.4** A project has the following cash flows:
- Year 0: -$100,000
- Years 1-4: $35,000 each
- Year 5: $40,000

Cost of capital: 8%. Compute:
(a) Payback period.
(b) Discounted payback period.
(c) NPV.
(d) IRR.
(e) Profitability index.

**16.5** Firm has two mutually exclusive projects, both with cost of capital 10%:
- Project A: -$50,000, then $20,000/year for 4 years.
- Project B: -$200,000, then $70,000/year for 4 years.

(a) Compute NPV and IRR for each.
(b) Which has higher IRR?
(c) Which has higher NPV?
(d) Which should the firm choose?

**16.6** Firm has a $300M budget and seven candidate projects. Use the profitability indices below to determine which projects to fund:

| Project | NPV ($M) | Investment ($M) |
|---|---|---|
| A | 80 | 200 |
| B | 50 | 150 |
| C | 30 | 100 |
| D | 25 | 70 |
| E | 18 | 50 |
| F | 12 | 40 |
| G | 8 | 30 |

Rank by PI; select projects until budget is exhausted. What's the total NPV under your selection?

### Synthesis

**16.7** For your chosen company, identify a major capex announcement in the past 2-3 years. Estimate (using public information and reasonable assumptions):
(a) Initial investment.
(b) Annual cash flows expected over a reasonable useful life.
(c) An appropriate discount rate.

Compute NPV. Argue whether the project is likely to be value-creating.

**16.8** A friend says: "Real options always justify going ahead with a project. Even if the standard NPV is negative, the option value can flip the decision." Construct a careful response addressing (a) when this is true, (b) when it's not, and (c) the practical difficulty of estimating option value for non-financial projects.

### Challenge

**16.9** Construct a specific example of a project with two IRRs (NPV crosses zero twice). Use real-feeling cash flows. Compute MIRR for the same project. Argue that MIRR gives the correct accept/reject signal in this case.

**16.10** Boeing's 787 Dreamliner ran roughly $20 billion over its initial $13B development budget. With actual delivery delays of 3+ years and ongoing quality issues, did the project produce positive NPV in retrospect? Build a rough model with:
- Initial development cost (actual).
- Annual cash flows from aircraft sales (estimate from public unit deliveries and pricing).
- Useful life (estimate based on aircraft generations).
- Discount rate (estimate Boeing's WACC at the time).

Argue whether the 787 was a financially good project. What strategic considerations might justify a different conclusion?

---

## Chapter summary

- **Five capital-budgeting metrics**: payback, discounted payback, NPV, IRR, MIRR, profitability index.
- **NPV is the gold standard** — directly measures value creation. Decision rule: accept if NPV > 0.
- **IRR has known flaws** — multiple roots when cash flows change sign more than once; scale-blind; reinvestment assumption.
- **MIRR fixes IRR's reinvestment-rate problem** by using cost of capital as the reinvestment rate.
- **Mutually exclusive projects**: NPV wins when methods disagree.
- **Unequal lives**: replacement chain or equivalent annual annuity.
- **Capital rationing**: use profitability index to rank.
- Cash flow estimation and discount rate choice are where most analytical errors come from, not the math itself.

---

## What would change my mind

The chapter argues NPV is the correct primary metric for capital budgeting. The reading would have to revise if (a) real options analysis became standard for general capital budgeting (currently it's used in specific industries), or (b) compelling empirical evidence emerged that firms using IRR-based decision rules systematically outperform firms using NPV — there's no such evidence, and theory predicts the opposite. NPV's primacy is well-established.

## Still puzzling

The genuinely hard question is *what discount rate to use for project evaluation*. Standard practice uses WACC for everything, but different projects have different risks. Project-specific discount rates would be more accurate but require more analytical work. The error from using WACC for everything is that low-risk projects get under-approved and high-risk projects get over-approved. In aggregate this leads to suboptimal capital allocation. Many large firms know this but don't adjust because the alternative (project-specific rates) is messy and contestable. The right answer in theory and the standard practice diverge here.

---

## Connections forward

- **Chapter 17** computes WACC — the firm's cost of capital, used as the discount rate.
- **Chapter 18** forecasts cash flows, the inputs to NPV.
- **Chapter 19** addresses working capital, a component of project FCF.
- **Chapter 20** addresses the risks that should determine project-specific discount rates.

---

---

## LLM Exercise — Chapter 16: Reverse-Engineer Your Company's Capital Budgeting

**Project:** Equity Research Report on a Chosen Public Company
**What you're building this chapter:** Assess your company's capital allocation track record — does it appear to be using NPV-disciplined decision-making, or is it making predictable IRR-vs-NPV mistakes?
**Tool:** Claude Project.

### The Prompt

```
For [your company], using the past 5 years of 10-Ks and major capex announcements:

1. **List the firm's largest capital allocation decisions** in the past 5 years. Examples:
   - Major acquisitions (with deal price)
   - Greenfield capex (new facilities)
   - R&D investments (especially multi-year programs)
   - Stock buybacks (cumulative spend)
   - Dividend changes
   - Major divestitures

2. **For 2-3 major decisions**, evaluate them with hindsight:
   - What did the firm say it would deliver (revenue growth, cost savings, strategic positioning)?
   - What has it actually delivered, based on subsequent financial results?
   - Was the decision likely value-creating in NPV terms (compared to an estimate of the firm's WACC at the time)?

3. **Pattern analysis** — Across the firm's decisions, do you see any of these patterns?
   - Bias toward bigger projects (scale-blindness in IRR)
   - Bias toward shorter-payback projects (payback-period thinking)
   - Bias toward strategic claims that NPV math doesn't support
   - Disciplined allocation that hits the WACC threshold reliably

4. **Comparison to peers** — How does the firm's capital intensity (capex/revenue) compare to peers? Is the firm investing more or less aggressively?

5. **Reading and recommendation** — One paragraph: based on the firm's track record, do you have confidence in management's capital allocation discipline? What does this imply for the investment thesis?

Cite sources. Don't speculate beyond the disclosed information.
```

### What this produces

A 1-2 page capital-allocation track-record section. Adds substantive context to the investment thesis — many investment outcomes hinge on whether management deploys capital well.

### How to adapt this prompt

- *For your own company:* Replace [your company].
- *For ChatGPT / Gemini:* Identical.
- *For a Claude Project:* All 10-Ks should be uploaded; the firm's history is in them.

### Connection to previous chapters

Builds on Chapters 6 (ratios), 9 (NPV), 11 (DCF), and the investment thesis from Chapter 15.

### Preview of next chapter

Chapter 17 computes WACC. The Chapter 17 LLM Exercise will produce the cost-of-capital number that gets used in Chapter 18's forecasting and revisits the DCF from Chapter 11.

---

**Tags:** capital-budgeting, NPV, IRR, MIRR, profitability-index, payback, mutually-exclusive, capital-rationing


---

## AI Wayback Machine

**Joel Dean** was developed the modern framework for capital budgeting in 1951 — including NPV and IRR as standard decision criteria.

**Run this:**

```
Who is Joel Dean, and how does their work connect to corporate investing we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about their career or ideas.
```

→ Search **"Joel Dean"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to apply Joel Dean's framework to a specific finance question.
- Add a constraint: "Answer including criticisms or limits of Joel Dean's framework."

What changes? What gets better? What gets worse?
