# Chapter 16 — How Companies Think about Investing
*Five metrics, one hierarchy, and why the percentage return lies to you about scale.*

---

## The puzzle of two projects, two answers

A firm has to choose between two embroidery machines. It can't buy both. The numbers:

| Project | Cost | NPV at 9% | IRR |
|---|---|---|---|
| Regular machine | $16,000 | $2,836 | 14.1% |
| Heavy-duty machine | $40,000 | $3,971 | 13.2% |

The IRR rule says: take the regular machine. 14.1% beats 13.2%.

The NPV rule says: take the heavy-duty machine. $3,971 of value created beats $2,836.

Both rules use identical time-value-of-money arithmetic. They disagree. Which one is right?

NPV is right. Here's why the IRR is misleading. A 14.1% return on $16,000 produces $2,263 of annual value at the margin. A 13.2% return on $40,000 produces $5,280. The percentage looks better on the small machine; the absolute dollar creation looks better on the large one. IRR is a *rate* — it ignores project size entirely. NPV is a *dollar amount* — it measures what actually gets added to shareholder wealth. The firm's objective is to maximize value. NPV measures that directly.

This is the whole chapter. Five metrics, clear hierarchy, and a handful of cases where methods disagree with clean resolutions.

---

## The five metrics in order of seriousness

### Payback period

The simplest thing you can say about a project: how many years until the initial investment is recovered from cash inflows?

A $16,000 machine producing $2,000 in year 1, $4,000 in year 2, and $5,000 per year in years 3–6 reaches cumulative inflows of $16,000 in year 4. Payback = 4 years.

**Decision rule:** Accept if payback is less than some threshold — chosen by management, often 3 or 5 years.

Payback has two fatal flaws. First, it ignores the time value of money: $5,000 in year 5 is treated identically to $5,000 in year 1. Second, it ignores everything that happens after the cutoff: a project paying back in 4 years and then generating $50,000 more over the following decade looks identical to one that pays back in 4 years and stops producing cash entirely.

Use payback as a liquidity check — "how long until we're exposed?" — never as the primary decision rule.

### Discounted payback

A modest fix: apply present-value factors to each cash flow before accumulating them. This corrects the time-value problem but does nothing for the cash-flows-after-cutoff problem. The threshold is still arbitrary.

For the $16,000 machine at 9%:

<!-- → [TABLE: Discounted payback table — Year 0 through Year 6, columns: Year, Cash Flow, PV Factor (at 9%), Present Value, Cumulative PV — student should see undiscounted payback at year 4 and discounted payback slightly into year 6, understanding the year-2 gap as the price of ignoring time value] -->

Undiscounted payback: 4 years. Discounted payback: approximately 5.05 years. The gap is the cost of pretending early and late cash flows are equally valuable.

Discounted payback is strictly better than undiscounted payback. It's still a secondary metric.

### Net Present Value

The gold standard.

$$NPV = \sum_{t=0}^{n} \frac{CF_t}{(1+r)^t}$$

where $CF_0$ is negative (the outflow) and $r$ is the firm's cost of capital. Accept if NPV > 0. Reject if NPV < 0.

For the regular machine at 9%:

$$NPV = -16{,}000 + \frac{2{,}000}{1.09} + \frac{4{,}000}{1.09^2} + \frac{5{,}000}{1.09^3} + \frac{5{,}000}{1.09^4} + \frac{5{,}000}{1.09^5} + \frac{5{,}000}{1.09^6}$$

$$= -16{,}000 + 1{,}835 + 3{,}367 + 3{,}861 + 3{,}542 + 3{,}250 + 2{,}981 = \$2{,}836$$

NPV of $2,836 means: this project adds $2,836 of present-value wealth to the firm, above and beyond what the firm's cost of capital requires. It's the value the firm creates by choosing this project over investing the same $16,000 at its opportunity cost.

Why NPV is the right metric: it incorporates time value of money, includes all cash flows over the full project life, uses a principled decision rule tied directly to value creation, and is additive — the NPV of a portfolio of projects equals the sum of the individual NPVs. This last property matters for a CFO managing dozens of simultaneous projects.

### Internal Rate of Return

The discount rate at which NPV equals zero:

$$0 = \sum_{t=0}^{n} \frac{CF_t}{(1 + IRR)^t}$$

For the regular machine, IRR = 14.1%. For the heavy-duty machine, IRR = 13.2%.

**Decision rule:** Accept if IRR > cost of capital. Reject if IRR < cost of capital. For standalone project accept/reject decisions with normal cash flow patterns (one outflow followed by inflows), IRR gives the same answer as NPV.

IRR fails under three conditions.

**Condition 1: Mutually exclusive projects.** As the opening puzzle showed, IRR ranks by rate and ignores size. When projects differ in scale, the higher-IRR project can create less value. Use NPV.

**Condition 2: Multiple IRRs.** When cash flows change sign more than once — an initial outflow, then inflows, then another large outflow (environmental remediation, decommissioning costs, warranty reserves) — the NPV equation can have two or more values of IRR that set it to zero. There's no unambiguous solution. The NPV profile crosses zero twice. The IRR rule is undefined.

<!-- → [CHART: NPV profile for a project with non-conventional cash flows — x-axis is discount rate from 0% to 40%, y-axis is NPV; curve crosses zero twice (two IRRs), while NPV at the firm's actual cost of capital is clearly positive or negative; student should see that NPV gives an unambiguous answer at any discount rate while IRR is indeterminate] -->

**Condition 3: Reinvestment assumption.** IRR implicitly assumes intermediate cash flows are reinvested at the IRR rate. For a project with a 25% IRR, this means finding other 25% projects to reinvest every cash inflow. That's rarely realistic. For high-IRR projects, IRR overstates the return the firm actually earns.

### Modified Internal Rate of Return

MIRR fixes the reinvestment problem by being explicit about the reinvestment rate:

1. Compute the present value of all *outflows*, discounted at the cost of capital.
2. Compound all *inflows* forward to the end of the project at the cost of capital.
3. Find the single rate that turns step 1's PV into step 2's FV over the project's life.

For the regular machine:
- PV of outflows: $16,000 (just the initial)
- FV of inflows compounded at 9% to end of year 6: $31,595
- $16{,}000 \times (1+MIRR)^6 = 31{,}595$
- $MIRR = (31{,}595/16{,}000)^{1/6} - 1 = 12.0\%$

MIRR = 12.0%, compared to IRR of 14.1%. The difference is the reinvestment assumption: IRR assumes the $2,000 received in year 1 gets reinvested at 14.1% for five more years; MIRR assumes it gets reinvested at 9%. The 9% assumption is more realistic for most firms.

**Decision rule:** Accept if MIRR > cost of capital. Single solution, always. More realistic than IRR.

### Profitability Index

$$PI = \frac{PV(\text{inflows})}{PV(\text{outflows})}$$

For the regular machine: PV of inflows = $18,836; PV of outflows = $16,000; PI = 1.18. Accept if PI > 1 — equivalent to NPV > 0.

PI becomes useful under **capital rationing** — when the firm has more positive-NPV projects than available capital. Ranking projects by PI ranks them by NPV per dollar invested, which is what you want when the binding constraint is dollars, not the number of projects.

<!-- → [TABLE: Capital rationing example — firm with $200M budget and seven candidate projects, columns: Project, NPV ($M), Investment ($M), PI = (NPV+Investment)/Investment, PI Rank — show optimal selection by PI order versus what you'd get by naively selecting largest-NPV projects; student should see that PI maximizes total NPV within the budget constraint] -->

↳ **Dig Deeper — Real options in capital budgeting**

*Standard NPV treats capital projects as static — once committed, you proceed. But real projects often have flexibility: expand if successful, abandon if not, delay the start. These flexibility features have value that NPV misses.*

**Prompt:**
> Explain the four main types of real options in capital budgeting: option to expand, option to abandon, option to delay, option to switch. For each, give one industry example where it's most valuable (e.g., pharmaceutical R&D for option to abandon). Then briefly describe how option-pricing methods (Black-Scholes adapted, binomial trees) can be applied to real options. What practical limitations make real options analysis harder than the financial-options version?

**What to do with the output:** Save it. Real options are why some apparently negative-NPV projects are actually value-creating — and why some positive-NPV projects need explicit flexibility to deliver.

---

## When the methods disagree: three clean cases

### Mutually exclusive projects

The opening puzzle is the template. When IRR and NPV disagree, NPV wins. The firm maximizes value, not rate of return. The scale-adjusted comparison — incrementally, does the larger investment earn above the cost of capital? — is what NPV computes directly.

Intuition check. Suppose a friend offers you two deals: earn 20% on $100, or earn 15% on $10,000. Which do you take? Most people correctly take the second — $1,500 of actual income beats $20 regardless of the rate. That's the NPV calculation. It's not exotic; it's arithmetic.

### Projects with unequal lives

A 3-year project with NPV of $50,000 vs. a 6-year project with NPV of $80,000. The longer project's NPV is higher, but it occupies twice as much time. Are they genuinely comparable?

Two methods produce the same answer.

**Replacement chain.** Repeat the shorter project to match the longer one's horizon. If the 3-year project can be repeated with identical cash flows, build a 6-year model that does it twice. Compare both to the 6-year project's NPV directly.

**Equivalent annual annuity (EAA).** Convert each project's NPV into a constant annual payment over its life:

$$EAA = \frac{NPV \times r}{1 - (1+r)^{-n}}$$

The project with the higher EAA produces more value per year — the right comparison when projects can be repeated.

Use whichever is more transparent for the audience. For projects that genuinely can be repeated (equipment replacement), the replacement chain is most intuitive. For projects that can't be repeated, EAA handles the comparison cleanly.

### Capital rationing

Rank by profitability index, accept in PI order until the budget is exhausted.

The logic: PI is NPV per dollar of capital deployed. When capital is the scarce resource, you maximize the NPV extracted per unit of the scarce resource. Ranking by total NPV fails because it doesn't account for how much capital each project consumes — a project with NPV of $80M and cost of $200M might leave behind a combination of smaller projects with higher total NPV per dollar.

↳ **Dig Deeper — How firms actually set hurdle rates**

*The textbook says firms should use WACC as the project discount rate. In practice, many use a single hurdle rate set well above WACC. Why?*

**Prompt:**
> Explain why corporate hurdle rates often exceed the firm's WACC. Three reasons frequently cited: (1) optimism bias in cash flow projections (the firm corrects for systematic over-estimation), (2) capital rationing (limited budget forces prioritization), (3) executive risk aversion. Walk through evidence for each. Then argue: which reason is most defensible, and which represents capital misallocation that destroys shareholder value?

**What to do with the output:** Save it. Real corporate capital budgeting deviates from the textbook in predictable ways; understanding the deviations helps assess your project company's discipline.

---

## The harder problem: estimating the cash flows

The metrics tell you whether a project clears a hurdle. The harder problem is constructing the cash flows that go into them.

NPV uses **incremental free cash flows** — the additional cash the firm generates because it does the project, net of all required reinvestment:

$$\text{Project FCF}_t = (\text{Revenue}_t - \text{COGS}_t - \text{Opex}_t)(1 - \tau) + \text{Dep}_t - \text{Capex}_t - \Delta\text{NWC}_t$$

where $\tau$ is the tax rate and $\Delta\text{NWC}$ is the change in net working capital the project requires.

Four disciplines for getting this right.

**No sunk costs.** Money already spent is gone regardless of the decision. Including sunk costs in NPV is a systematic bias toward over-investment in losing projects — you keep funding things because you've already paid so much. The NPV calculation includes only future cash flows.

**Include opportunity costs.** If the project uses a building the firm already owns, the firm can't use that building for something else. The opportunity cost — the best alternative use foregone — is a real cash flow for NPV purposes, even if no cash changes hands.

**Account for cannibalization.** If the new product steals revenue from an existing product, the net revenue increment is smaller than the gross. Optimistic managers omit cannibalization; rigorous analysis includes it.

**Don't ignore terminal costs.** Projects end. The machine gets scrapped, the environmental cleanup happens, the lease terminates. Terminal cash flows are part of the project's economics and can flip marginal projects from positive to negative NPV.

<!-- → [TABLE: FCF estimation discipline checklist — rows: Sunk costs, Opportunity costs, Cannibalization, Terminal costs — columns: Rule (include/exclude), What managers often do wrong, Real-world example of the error, Impact direction on NPV (overstated/understated) — student should be able to audit any cash flow projection against these four rules] -->

### Boeing's 787 Dreamliner

The 787 is the capital-budgeting case that almost everyone in finance knows. Boeing committed approximately $13 billion to develop the aircraft. Development overruns exceeded $20 billion and deliveries arrived three years late, with structural and battery issues producing further grounding events through 2024. Estimated total program development cost exceeded $32 billion.

Was this a good capital-budgeting decision? The honest answer depends heavily on what cash flows you count and over what horizon. On direct program economics — development cost against aircraft margins over the delivery schedule — the case is questionable. On strategic-option value — Boeing maintaining widebody leadership against Airbus, a position worth considerable competitive value — the case is more defensible.

The 787 case is useful precisely because it illustrates both the discipline NPV brings (forces you to put explicit numbers on everything) and its limits (can't cleanly capture strategic optionality without additional frameworks). A capital-budgeting analysis of a Boeing-type decision should produce an NPV calculation *and* an explicit argument for why the strategic considerations justify whatever gap the NPV analysis shows.

---

## A hierarchy, not a menu

The five metrics aren't five equally valid choices. They have a structure:

**NPV is the primary criterion for value creation.** Accept or reject based on NPV. Full stop.

**IRR is a useful summary metric, not a decision criterion.** Report it alongside NPV; use it to communicate the project's implied return; don't rank by it for mutually exclusive projects.

**MIRR is the better version of IRR when the reinvestment assumption matters** — which is most of the time for high-IRR projects in firms that don't have unlimited 20%+ alternatives.

**PI is the ranking tool for capital-constrained decisions.** Not needed otherwise.

**Payback is a liquidity check.** A 12-year payback on a 10-year project is a problem the analyst should flag. Beyond that, it adds little.

For the equity research project: when you evaluate your chosen company's capital allocation, the question is whether management appears to be using NPV-consistent logic — taking projects whose expected returns exceed the cost of capital, calibrated appropriately to project risk — or making one of the predictable errors: pursuing high-IRR small projects over lower-IRR large ones, or anchoring on payback period at the expense of long-duration value creation.

The analytical signal is informative in both directions. A firm with disciplined capital allocation tends to earn returns above cost of capital over time. A firm that makes systematic capital-budgeting mistakes tends not to.

<!-- → [TABLE: Metric hierarchy summary — rows: NPV, IRR, MIRR, PI, Payback — columns: Primary use, Decision rule, When it fails, When to rely on it — student should be able to select the right metric for any capital-budgeting context without having to work through the logic from scratch] -->

---

## What would change my mind

The chapter argues NPV is the correct primary metric for capital budgeting, with the others serving supplementary roles in specific situations. The reading would have to revise if (a) real options analysis became standard for general capital budgeting — currently it's used in specific high-optionality industries but not routinely — or (b) compelling empirical evidence emerged that firms using IRR-based decision rules systematically outperform NPV-based firms. No such evidence exists; theory predicts the opposite.

## Still puzzling

The hardest unsolved problem in practice is the discount rate. Standard practice uses WACC for all projects, but different projects carry different risk. A low-risk capacity expansion should be discounted less than a high-risk new-market entry; using the same WACC for both systematically under-approves safe projects and over-approves risky ones. The right answer — project-specific discount rates derived from project beta and debt capacity — is theoretically clear and practically messy. Most firms know the argument and don't implement it because the marginal improvement in capital allocation doesn't justify the political cost of having different hurdles for different projects. The gap between theory and practice here is real and persistent.

---

## Connections forward

- **Chapter 17** computes WACC — the discount rate plugged into NPV.
- **Chapter 18** forecasts the cash flows that feed NPV.
- **Chapter 19** addresses working capital, a component of project FCF.
- **Chapter 20** addresses the risk factors that determine project-specific discount rates.

---

## Exercises

### Warm-up

**16.1** State the decision rule for each of the five capital-budgeting metrics: payback, discounted payback, NPV, IRR, and MIRR. For each, name one situation where it should not be used as the primary criterion.

**16.2** The opening puzzle showed a regular machine (NPV $2,836, IRR 14.1%) and a heavy-duty machine (NPV $3,971, IRR 13.2%). Without doing any new arithmetic, explain in two sentences why a firm that maximizes shareholder value should choose the heavy-duty machine despite its lower IRR.

**16.3** Describe the multiple-IRR problem. Under what cash flow conditions does it arise? Why does NPV remain well-defined in these cases?

### Application

**16.4** A project requires an initial investment of $80,000 and produces the following cash flows:

- Year 1: $20,000
- Year 2: $25,000
- Year 3: $30,000
- Year 4: $35,000
- Year 5: $20,000

Cost of capital: 10%. Compute:

(a) Payback period (to the nearest year).
(b) Discounted payback period (to the nearest 0.1 year).
(c) NPV.
(d) IRR (use Excel's `=IRR()` or iterate).
(e) Profitability index.
(f) State the accept/reject decision under each metric.

**16.5** A firm must choose between two mutually exclusive projects, both with a 12% cost of capital:

- Project A: Initial cost $60,000; annual cash flows of $22,000 for 4 years.
- Project B: Initial cost $250,000; annual cash flows of $80,000 for 4 years.

(a) Compute NPV and IRR for each.
(b) Which has the higher IRR? Which has the higher NPV?
(c) Which should the firm select, and why?
(d) Restate the "20% on $100 vs. 15% on $10,000" intuition in terms of these two projects.

**16.6** A firm with a $500M capital budget is evaluating six projects:

| Project | NPV ($M) | Investment ($M) |
|---|---|---|
| A | 120 | 300 |
| B | 90 | 250 |
| C | 60 | 150 |
| D | 45 | 120 |
| E | 30 | 80 |
| F | 20 | 60 |

(a) Compute PI for each project.
(b) Rank by PI and select projects until the $500M budget is exhausted.
(c) What is the total NPV under your selection?
(d) What would the total NPV have been if you had simply selected by largest NPV first? Compare.

### Synthesis

**16.7** A project has the following cash flows: Year 0: −$100,000; Years 1–3: +$60,000; Year 4: −$40,000 (environmental cleanup). Cost of capital: 8%.

(a) Compute NPV. Is it positive?
(b) Compute MIRR. Does the MIRR decision rule agree with NPV?
(c) Attempt to find the IRR. Does the project have one IRR, two, or is the situation ambiguous? Explain why.

**16.8** For your chosen company, identify a major capital expenditure announced in the past two years (8-K filing or 10-K MD&A). Estimate: (a) the initial outflow, (b) plausible annual incremental cash flows, (c) the project's life. Compute NPV using your estimate of the firm's WACC (10% is a reasonable placeholder if you haven't completed Chapter 17 yet). Argue whether the capex appears value-creating.

### Challenge

**16.9** Boeing committed approximately $13 billion to develop the 787 Dreamliner; actual development cost exceeded $32 billion. Build a rough NPV model:

(a) Use actual development cost as the outflow (you may need to spread it over 5 years of development).
(b) Estimate annual FCF from 787 deliveries: Boeing has delivered roughly 1,000+ aircraft at estimated net margins of $5–15M per plane. Spread over a reasonable delivery schedule.
(c) Use a discount rate of 8–10% (Boeing's approximate WACC at the time).
(d) Compute NPV. Does the program appear to have positive NPV on direct financials alone?
(e) Argue what strategic option value would need to be worth to justify the investment if the direct NPV is negative.

**16.10** A colleague argues: "Real options always justify going ahead with projects that have slightly negative NPV. The option to abandon is always worth something." Construct a careful response: (a) when is this argument valid, (b) when does option value fail to flip a negative-NPV project, and (c) what discipline should surround any real-options argument to prevent it from becoming a catch-all justification for bad capital allocation?

---

## LLM Exercise — Chapter 16: Reverse-Engineer Your Company's Capital Budgeting

**Project:** Equity Research Report on a Chosen Public Company
**What you're building this chapter:** Assess your company's capital allocation track record — does it appear to use NPV-disciplined decision-making, or is it making predictable IRR-vs-NPV mistakes?
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

A 1–2 page capital-allocation track-record section. Adds substantive context to the investment thesis — many investment outcomes hinge on whether management deploys capital well.

### How to adapt this prompt

- *For your own company:* Replace [your company].
- *For ChatGPT / Gemini:* Identical.
- *For a Claude Project:* All 10-Ks should be uploaded; the firm's history is in them.

### Connection to previous chapters

Builds on Chapters 6 (ratios), 9 (NPV), 11 (DCF), and the investment thesis from Chapter 15.

### Preview of next chapter

Chapter 17 computes WACC. The Chapter 17 LLM Exercise will produce the cost-of-capital number that gets used in Chapter 18's forecasting and revisits the DCF from Chapter 11.

---

## AI Wayback Machine

**Joel Dean** developed the modern framework for capital budgeting in 1951 — including NPV and IRR as standard decision criteria.

**Run this:**

```
Who is Joel Dean, and how does their work connect to corporate investing we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about their career or ideas.
```

→ Search **"Joel Dean"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to apply Joel Dean's framework to a specific finance question.
- Add a constraint: "Answer including criticisms or limits of Joel Dean's framework."

What changes? What gets better? What gets worse?

---

**Tags:** capital-budgeting, NPV, IRR, MIRR, profitability-index, payback, mutually-exclusive, capital-rationing
