# Chapter 4 — Capital Budgeting at the Firm Level


## TL;DR

- A number that can't be questioned isn't a number — it's a prayer.
- The chapter moves through Warm-up, Application, Synthesis, Challenge, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

*A number that can't be questioned isn't a number — it's a prayer.*

---

When Maya opens the operations VP's business case on Thursday morning, the first thing she sees is a chart. At the bottom of the chart, a single line: *Projected NPV: $87.4M.*

The number has been rounded to one decimal place, which gives it a pleasing specificity. It has been labeled "projected," which is honest. It was produced by someone's model, using someone's assumptions, discounted at a rate that was chosen for reasons explained in a footnote.

Maya's job, as she now understands it, is not to recompute $87.4M. Her job is to figure out whether $87.4M is real — whether the inputs that produced it are the right inputs, whether the discount rate is the right discount rate, and what a smart board member would have to believe to reject the recommendation. That is the work. The math is not the work.

This chapter is about the gap between producing a number and defending one.

---

Net Present Value is, as a formula, straightforward. You project the cash flows a project will generate in each future year. You discount each cash flow back to today using a rate that reflects the riskiness of those cash flows. You sum. If the sum is positive — if the present value of what you expect to receive exceeds the present value of what you spend — you accept the project. If negative, you reject.

$$NPV = \sum_{t=0}^{T} \frac{FCFF_t}{(1+r)^t}$$

The calculation itself takes about thirty seconds in a spreadsheet. MBA programs teach it in two days because it does not take longer than two days to teach the mechanics. What they mostly teach it *with* is pre-cooked cash flow projections. The professor hands you a table: year 1, $15M; year 2, $18M; year 3, $20M; terminal value, $120M; discount rate, 8%. Compute NPV. Check answer. Move on.

The hard part — where those numbers came from and whether they're right — is upstream of the problem set, and mostly invisible.

![Two-column diagram ](images/04-capital-budgeting-at-the-firm-level-fig-01.png)
*Figure 4.1 — Two-column diagram *

From inside the firm, all of that upstream work is your job. Plant 4 does not have a published cash flow stream. It does not yet exist. Every line of the projection has to be constructed from forecasts about something that hasn't happened yet, and every forecast is owned by a person with a different relationship to optimism than you have.

The formula is a machine. Someone has to build the inputs the machine runs on, and the machine will accept whatever you give it. An NPV calculation with garbage inputs produces a confident garbage output. The formula doesn't know the difference.

---

Let me build the projection from first principles, because the standard presentation hides a few things worth seeing.

The cash flow a project generates each year — what finance calls the *free cash flow to the firm*, or FCFF — is not the same as the project's accounting profit, and not the same as its revenue. It's the cash the project actually produces for Halverson after taxes and after reinvestment requirements, and before any financing decisions. The formula is:

$$FCFF = EBIT \times (1 - \text{tax rate}) + \text{Depreciation} - \text{Capital Expenditures} - \Delta \text{Working Capital}$$

Each term is doing a specific job, and each one is worth understanding rather than just accepting.

$EBIT \times (1 - \text{tax rate})$ — called NOPAT, net operating profit after tax — is the after-tax operating profit the project earns. It excludes interest expense on purpose: interest is a financing choice, not an operating one, and the discount rate already accounts for the cost of financing. Mixing interest into the cash flows would double-count it. This is a design choice in the formula, not an oversight.

Depreciation gets added back because it reduced EBIT — it reduced the number we just multiplied by the tax rate — but it doesn't actually move cash. Depreciation matters because it creates a tax shield: by reducing taxable income, it reduces the taxes Halverson pays. But the depreciation itself doesn't leave the building as a check. So we add it back after the tax calculation, recovering the non-cash component while keeping the tax benefit.

Capital expenditures are subtracted because they do leave the building as a check, and the income statement spreads them across years through depreciation rather than recording them when the cash is spent. The cash flow statement wants to know when cash actually moved. For Plant 4, the $50M construction cost is a year-zero cash outflow, recorded in full regardless of how many years it will be depreciated over.

The change in working capital is the one that business cases most often undercount. When Plant 4 starts running, Halverson needs to hold more inventory, carry more accounts receivable, and the difference between those and accounts payable is the additional cash Halverson has to tie up just to operate at the new scale. This isn't profit. It isn't an expense. It's cash that goes into the machinery of the business and stays there until the plant closes. Forgetting working capital in a capital budget isn't technically wrong — it's just an incomplete answer to where the cash went.

| | Year 0 | Year 1 | Year 2 | Year 3 |
|---|---|---|---|---|
| Revenue | $0 | $30M | $50M | $60M |
| EBIT | $0 | $8M | $18M | $25M |
| × (1 − tax rate) → NOPAT | $0 | $6.1M | $13.7M | $19.0M |
| + Depreciation | $0 | $5.0M | $5.0M | $5.0M |
| − Capex | **−$50M** | −$2M | −$2M | −$2M |
| − ΔWorking Capital | **−$5M** | −$3M | −$2M | −$1M |
| **= FCFF** | **−$55M** | $6.1M | $13.7M | $21.0M |

*Year 0 is large negative — construction plus the working-capital draw most analyses omit. Years 1–3 turn positive and grow as the ramp progresses.*

Year zero of the Plant 4 projection is negative: the $50M construction cost plus a working capital investment to get operations started. Years one through ten are positive, starting modest as the plant ramps utilization and growing as it reaches full capacity. Year ten carries, in addition to that year's operating cash flow, a terminal value — a single number meant to represent everything the plant earns from year eleven to the end of its useful life.

That terminal value is where most of the NPV lives. This is the thing to hold in mind for what comes next.

---

The standard terminal value formula is the perpetuity growth model:

$$TV = \frac{FCFF_{T+1}}{r - g}$$

Where $r$ is the discount rate and $g$ is the long-run growth rate of the project's cash flows after the explicit forecast period.

In the operations team's model, $r$ = 8% and $g$ = 2.5%. With a year-11 FCFF in the range the projection produces, the terminal value is something on the order of $400–450M — a number that, after discounting back ten years at 8%, contributes perhaps sixty percent of the total NPV.

Let me say that again. Sixty percent of the recommendation to spend $50M is driven by a single parameter — $g$, the long-run growth rate — applied to cash flows that don't start for eleven years.

Now look at what happens when you vary $g$ across a range that all seem plausible for a US industrial manufacturer in a mature market. At $g$ = 1.5%, the NPV might be $30M. At $g$ = 2.5% (the operations team's assumption), perhaps $45M. At $g$ = 3.5%, perhaps $65M. The NPV range across a plausible input range is larger than the NPV itself at the low end.

![Sensitivity bar chart ](images/04-capital-budgeting-at-the-firm-level-fig-02.png)
*Figure 4.2 — Sensitivity bar chart *

The NPV is highly sensitive to a parameter that is hard to estimate and easy to choose optimistically. This is not a flaw in NPV as a method. It is a structural feature of long-lived assets discounted over long periods, and it applies to every capital project with a terminal value component — which is most of them. The formula amplifies small differences in $g$ because it sits in the denominator of a fraction that is then multiplied by a large numerator. Changing $g$ by one percentage point, in that formula, moves the terminal value by something like 25–40 percent depending on the specific numbers. That is not a rounding error.

The operations team said $g$ = 2.5%. The question Maya has to answer before Friday is not "what is the right $g$?" Nobody knows the right $g$ for a plant that will operate for 25 years. The question is: what is a *defensible* $g$, and can it be defended on the record in front of the board?

A defensible $g$ is derived from something external to the model — the long-run real growth rate of US industrial output, plus an inflation assumption, minus any productivity offset. The long-run nominal GDP growth rate of the US is roughly 4% historically; for a mature industrial segment, real growth below GDP growth is reasonable; with 2% inflation, $g$ in the range of 1.5%–2.5% is arguable. The operations team's 2.5% is at the top of that range but not outside it.

"We used 2.5% because it's at the top of the reasonable range for an industrial project, calibrated to long-run nominal GDP growth" is a defense. "We used 2.5%" is not. The board's job is to ask why. Maya's job is to make sure that question has been answered before the board asks it.

---

I've been focusing on the terminal value because it's the single most important input to this particular NPV. But the full projection has other places where defensible-looking numbers can quietly be wrong. Three of them appear in almost every capital budget review, and they're worth naming directly.

The first is the utilization assumption. The operations team's case assumes Plant 4 reaches full capacity by year two. Have they checked this against the sales pipeline? Against how long it took the last plant to ramp? If the actual ramp is slower — 60% utilization in year one and 80% in year two before reaching full capacity in year three — what happens to NPV?

This is a sensitivity that every capital budget should run and almost none do, for an understandable reason: running it requires the operations team to model their own optimistic assumption failing. Maya's job is to run it for them. A 30% shortfall in year-one revenue, combined with fixed costs that don't scale down proportionally, can cut year-one FCFF by 50% or more. On a project where early cash flows are already modest relative to the terminal value, this changes the NPV less than you'd expect — but it changes it. More importantly, it changes the answer to the stress test: can Halverson absorb this if things go worse than expected?

The second is cannibalization. Plant 4 adds capacity to Halverson's manufacturing network. But capacity additions are sometimes efficiency plays rather than pure growth plays: if the new plant is more efficient than Plants 1–3, production may migrate to Plant 4, which means some of its revenue comes at the expense of the existing plants' revenue. The incremental cash flow from Plant 4 in that scenario is smaller than its absolute cash flow, because some of what it earns is replacing what the existing plants lose.

Operations teams think in absolute terms about the project they're proposing. The CFO's office has to think in incremental terms about the firm. These produce different numbers. The question Maya has to get answered, in writing and before the board meeting, is whether operations has confirmed that Plant 4's projections are genuinely incremental to Halverson's total cash flows — or whether some fraction of the projected revenue is already flowing into the company through Plants 1–3.

The third is the discount rate. Halverson's firm-wide WACC is the right discount rate for a project that is precisely as risky as Halverson's average business activity. Plant 4, if it is a straightforward capacity expansion of an existing product line in an existing geography using existing technology, is a reasonable candidate for the firm WACC. But if it involves meaningful risk above Halverson's typical project — a new geography, a new customer base, a technology not yet proven at this scale — the right discount rate is higher than the firm WACC, and the NPV is correspondingly lower.

The operations team used 8%. Before accepting that number, the CFO's office should confirm: is Plant 4 a typical-risk project for Halverson, or riskier than typical? This question sounds soft but has a hard answer: you compare Plant 4's risk profile against Halverson's historical project universe and against comparable publicly-traded businesses if the profile is sufficiently different. "We used 8% because that's the firm WACC" is a flag, not an explanation. "We used 8% because Plant 4 is a domestic capacity expansion with existing technology, customers, and operating team, which puts it at or below average firm risk" is a defense.

| Assumption | What the operations team modeled | What can go wrong | How to stress-test it | Owner of verification |
|---|---|---|---|---|
| **Utilization ramp** | 90% of nameplate capacity by month 18, sustained thereafter | Slower ramp (production yields, training, certification); capacity comes online but customers don't | Run NPV at 60% / 75% / 90% sustained utilization; identify the breakeven utilization | Plant 4 program manager + sales |
| **Cannibalization** | New capacity serves *new* demand — no overlap with existing plants | Customers who would have bought at higher margin from existing plants migrate to the lower-cost Plant 4 line | Estimate cannibalization at 0% / 10% / 25% of incremental volume | Sales operations |
| **Discount rate** | Firm WACC of 8.0%, applied uniformly | Project risk is higher than firm average (new-plant ramp, single customer concentration on the line) | Use a project-specific rate from comparable-firm betas; report NPV at firm WACC and project rate | FP&A |

---

After running her own version of the projection — conservative utilization ramp, the same $g$ of 2.5% as the operations team but with explicit sensitivity to 1.5% and 3.5%, and a cannibalization confirmation request outstanding — Maya's NPV range looks something like this.

Operations team base case: approximately $87M (aggressive ramp, $g$ = 2.5%). Maya's base case: approximately $42M (conservative ramp, $g$ = 2.5%). Maya's downside: approximately $28M ($g$ = 1.5%, slow ramp). Maya's upside: approximately $65M ($g$ = 3.5%, operations team's ramp).

All of these are positive. That is actually the important result.

![Scenario waterfall ](images/04-capital-budgeting-at-the-firm-level-fig-03.png)
*Figure 4.3 — Scenario waterfall *

The decision to accept Plant 4 is robust across reasonable assumption changes. The exact NPV is not robust — it swings by a factor of three across the range — but the sign is stable. A positive NPV that stays positive across a wide sensitivity range is more defensible than a positive NPV that flips negative when you push one assumption. The memo should say this explicitly. Not "the NPV is $87M, accept the project." The recommendation is: "The NPV is positive across all reasonable assumptions, ranging from approximately $28M in the downside scenario to approximately $87M under the operations team's assumptions. The recommendation to proceed is robust. The exact value is not. Here is the sensitivity table. Here are the three assumptions that drive most of the range. Here is the one confirmation that should be obtained before the board meeting."

That memo can be defended. The $87M memo cannot, because the first board member who asks "what if the ramp takes three years instead of two?" will expose a number that was never stress-tested.

---

I want to end on something that might seem like a contradiction. I've spent most of this chapter explaining how NPV calculations go wrong. If the tool is this vulnerable to its inputs, why use it?

Because the alternatives are worse.

The alternatives to NPV are other methods for aggregating the costs and benefits of a multi-year investment: payback period, accounting rate of return, internal rate of return. Each has its uses. Payback period is useful for liquidity-constrained firms that need to recover cash quickly. IRR is useful for comparing projects with different scales. But all of them involve approximations or distortions that NPV doesn't, and none of them forces you to be as explicit about your assumptions.

The discipline of building an NPV is the discipline of stating, explicitly and in writing, what you believe about revenues, costs, working capital, capex, discount rate, and growth. Once you've done that, anyone who disagrees with your recommendation has to identify which specific assumption they disagree with. That is a productive argument — "I think the ramp takes three years, not two" is a falsifiable claim that can be investigated. "I don't like this project" is not.

NPV is not a machine for producing correct answers. It is a structure for having the right argument. The model is only as good as the construction work underneath it. But the model forces the construction work to be explicit, which means it can be questioned, stress-tested, and revised before the board meeting rather than after.

Maya's $87.4M is, in this sense, a starting point rather than a conclusion. The sensitivity table, the cannibalization flag, the defended growth rate — that is what turns a starting point into a recommendation you can actually sign your name to.

A number you can't question isn't a number. It's a prayer that nothing turns out to be different than you hoped.

---

## Exercises

### Warm-up

**1.** The FCFF formula adds depreciation back after computing NOPAT. A student argues: "Depreciation is fake — it's not a real cost, so it shouldn't affect the calculation at all." Identify the two errors in that reasoning. For each, explain what the student is missing about how depreciation interacts with taxes and with the income statement. *(Tests: understanding of why each term in the FCFF formula is present and what job it does.)*

**2.** In the perpetuity growth model $TV = \frac{FCFF_{T+1}}{r - g}$, suppose $r$ = 8% and $g$ rises from 2% to 3%. Without a calculator, explain directionally why this change has a larger effect on terminal value than raising $g$ from 1% to 2% by the same one percentage point. What property of the formula produces this asymmetry? *(Tests: intuition for the denominator sensitivity of the perpetuity formula.)*

**3.** Maya flags that the operations team's discount rate of 8% is "a flag, not an explanation." Describe exactly what additional information would convert that flag into a defense. What two comparisons would establish that 8% is appropriate for Plant 4 specifically, rather than just for Halverson on average? *(Tests: understanding of project-specific versus firm-average discount rates.)*

---

### Application

**4.** A manufacturing firm is evaluating a $20M equipment upgrade. The finance team's projection shows EBIT of $3.2M in year one, depreciation of $2M, no additional capex after the initial investment, and a working capital increase of $400K to support the higher production volume. The effective tax rate is 25%. Calculate FCFF for year one, showing each step. Then identify which line item a rushed analyst would most likely omit, and state what direction that omission would push the NPV. *(Tests: mechanical FCFF construction plus awareness of the working capital omission pattern.)*

**5.** You are reviewing a capital budget for a new distribution center. The terminal value accounts for 71% of the total NPV. The analyst used $g$ = 3.0%, citing "industry growth expectations." Write the two questions you would ask in the review meeting — not to reject the project, but to convert the analyst's $g$ assumption from an assertion into a defense. For each question, state what a satisfactory answer would look like. *(Tests: applying the defensibility standard to terminal growth rate assumptions.)*

**6.** A regional hospital system is evaluating a $15M MRI expansion. The CFO argues: "We should use payback period instead of NPV because our board thinks in terms of how fast we recover the investment." Make the strongest case for NPV over payback period in this specific context, then make the strongest case for why payback period might be a reasonable complement (not substitute) given the hospital's situation. *(Tests: comparative evaluation of capital budgeting methods; cross-context application from a corporate to a nonprofit setting.)*

**7.** Plant 4's projections assume no cannibalization of Plants 1–3. You are told that Plant 4 will produce the same product line as Plant 2 but at 15% lower unit cost. Explain why this cost advantage makes cannibalization more likely, not less, and describe how the incremental cash flow calculation should be adjusted if Plant 2's utilization is expected to fall by 20% after Plant 4 opens. *(Tests: incremental versus absolute cash flow thinking applied to a specific scenario.)*

---

### Synthesis

**8.** The chapter argues that "NPV is not a machine for producing correct answers — it is a structure for having the right argument." Connect this claim to the three-beat method introduced in Chapter 1 (verify inputs, calculate transparently, sanity-check). For each beat, identify what it contributes to making the NPV argument defensible rather than merely arithmetically correct, and give a specific example using the Plant 4 case. *(Tests: integration of the three-beat method from Chapter 1 with the capital budgeting framework from Chapter 4.)*

**9.** Maya's sensitivity analysis shows the NPV is positive across all plausible scenarios but ranges from $28M to $87M. A board member says: "The range is too wide — this analysis doesn't tell us anything useful." Write a one-paragraph response defending the sensitivity analysis as informative despite the wide range. Your response should distinguish between precision and robustness, and explain why the sign of the NPV is the decision-relevant output rather than its magnitude. *(Tests: ability to explain and defend the purpose of scenario analysis to a non-technical audience.)*

---

### Challenge

**10.** The chapter identifies terminal value as contributing ~60% of total NPV for Plant 4 — a proportion typical of long-lived industrial assets. A CFO argues that this makes NPV unreliable for long-lived projects and that firms should cap their explicit forecast period at five years and ignore terminal value entirely. Construct the strongest possible case for this position, then identify the specific condition under which it would actually lead to better decisions than the standard approach. Your answer should engage with what information is genuinely lost versus genuinely preserved by truncating the analysis at year five. *(Tests: stress-testing the chapter's own framework; distinguishes principled skepticism about terminal value from a misunderstanding of what it represents.)*

---

*Tags: capital budgeting, NPV, free cash flow, terminal value, sensitivity analysis, utilization assumption, discount rate, capital expenditure*

---

###  LLM Exercise — Chapter 4: Capital Budgeting at the Firm Level

**Project:** Halverson's Board Memo, Built Across the Course
**What you're building this chapter:** The Capital-Budgeting Portfolio section of the memo: an NPV-ranked list of candidate projects under a budget constraint, with the prioritization defended and the binding constraint named.
**Tool:** Claude Code

---

**The Prompt:**

```
I'm working on Halverson's Board Memo. Sections so far: `01-decision-frame.md`, `02-inside-read.md`, `03-working-capital.md`.

Chapter 4 taught:
- **NPV** as the primary decision rule (positive NPV = creates value, negative = destroys it)
- **The firm-level portfolio problem**: not one project at a time but the prioritization-under-budget problem
- **The difference between accept/reject and rank-under-constraint**

Scaffold `analysis/04-budget-portfolio.py`:

1. **Define the candidate-project set.** 6–10 projects the firm is currently considering. For Halverson use Plant 4 ($50M, projected $20M EBITDA), Cardinal acquisition ($700M, projected $50M synergized EBITDA), plus 4–6 organic projects you make up at plausible scales. For another firm: pull from the latest investor-day deck or 10-K capital-allocation discussion.

2. **For each project**, define: initial investment, year-by-year cash-flow forecast (5–10 years), terminal value, and a project-specific discount rate (use the firm WACC for now — Chapter 5 refines this; Chapter 6 adjusts for project risk).

3. **Compute NPV, IRR, profitability index** for each. Save as a CSV.

4. **Solve the budget knapsack.** Given a total capital budget — pick a number consistent with the firm's recent cash flow plus available debt capacity — find the subset of projects that maximizes total NPV subject to the budget constraint. Use `scipy.optimize.milp` or `pulp`.

5. **Identify the binding constraint.** The capital budget? Engineering capacity (Plant 4 needs the same engineering team as Project X)? Management bandwidth (the Penrose effect — see Ch 11's Wayback figure)? State the binding constraint explicitly.

6. **Produce `analysis/04-portfolio-ranked.md`** containing: the NPV-ranked list, the recommended portfolio under the budget, the binding constraint, and a one-paragraph defense of the prioritization that an audit-committee chair could read in 90 seconds.

The script runs with `python analysis/04-budget-portfolio.py --budget [DOLLARS] --wacc [RATE]`.
```

---

**What this produces:** A runnable script `analysis/04-budget-portfolio.py` plus a results file `analysis/04-portfolio-ranked.md` containing the NPV ranking, the knapsack solution, the binding constraint, and a defensible prioritization.

**How to adapt this prompt:**

- *For your own project:* Substitute your firm for Halverson where Halverson appears; the exercise structure is firm-agnostic. Halverson's named cast (Diane / Priya / Cardinal) is scaffolding — replace as needed.
- *For ChatGPT / Gemini:* Works as-is. For ChatGPT, save the running memo to a Custom GPT instead of a Claude Project. For Gemini, paste the project's accumulated section files into the context window each session.
- *For Claude Code:* Right tool — NPV portfolio + integer-program knapsack is exactly Claude Code's wheelhouse. Use `pulp` or `scipy.optimize.milp`.
- *For a Claude Project:* Append the portfolio markdown to the project. The recommended portfolio's total dollar amount becomes a constraint Chapter 5's WACC analysis must support and Chapter 8's capital structure must finance.

**Connection to previous chapters:** Chapter 3 freed up working capital; Chapter 4 deploys it (and more) across an NPV-ranked portfolio.

**Preview of next chapter:** Chapter 5 stress-tests the WACC that Chapter 4 used as the discount rate — and sees how much the prioritization moves under ±100bp shifts.

---

##  AI Wayback Machine
The ideas in this chapter didn't appear from nowhere. **Joel Dean** was publishing *Capital Budgeting* in 1951 — the foundational text that brought NPV and IRR out of the journals and into corporate practice decades before most people had heard of capital budgeting at the firm level, with NPV as the primary decision rule. Here's a prompt to find out more — and then make it better.

![Joel Dean, c. 1950s. AI-generated portrait based on a public domain photograph (Wikimedia Commons).](images/joel-dean.jpg)
*Joel Dean, c. 1950s. AI-generated portrait based on a public domain photograph.*

**Run this:**

```
Who was Joel Dean, and how does his 1951 book *Capital Budgeting* — translating present-value mathematics into a corporate decision rule — connect to the chapter's argument that NPV is not just a math technique but the structural form of every honest investment decision a firm makes? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.
```

→ Search **"Joel Dean economist"** on Wikipedia after you run this. See what the model got right, got wrong, or left out.

**Now make the prompt better.** Try one of these:

- Ask it to explain *NPV vs. IRR* in plain language, as if you've never run a capital-budgeting analysis
- Ask it to compare Dean's 1951 framework to the modern stage-gate process at a Fortune 500 firm
- Add a constraint: "Answer as if you're writing the policy memo establishing capital-budgeting standards for a new business unit"

What changes? What gets better? What gets worse?
