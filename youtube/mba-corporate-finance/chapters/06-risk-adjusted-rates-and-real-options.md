# Chapter 6 — Risk-Adjusted Rates and Real Options


## TL;DR

- Maya's NPV is wrong — not in the arithmetic, but in the question it answers.
- The chapter moves through The Wrong Rate, Finding the Right Rate, The Future Isn't Locked, Real Options, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

*Maya's NPV is wrong — not in the arithmetic, but in the question it answers.*

---

Maya's revised NPV for Plant 4 came in at $42 million. She is reasonably proud of it. She spent two chapters getting there. The number is wrong.

Not wrong in the arithmetic sense. Wrong in a deeper sense: the calculation correctly answers a question that is not quite the question Halverson should be asking. It uses the wrong discount rate for this particular project. And it assumes a kind of irrevocability — commit today, no looking back — that no rational manager actually faces.

This chapter fixes both problems. The fixes point in opposite directions: the correct discount rate makes the NPV smaller, and acknowledging flexibility makes it larger. They do not cancel out. Understanding why they don't is most of what I want to teach you here.

---

## The Wrong Rate

Go back to Chapter 5 for a moment. The cost of capital depends on risk. We arrived at Halverson's WACC of 8% by blending the required returns on its debt and equity, where the equity return was derived from a beta estimated against the firm's existing operations. That 8% is the average risk of Halverson as it currently exists.

It is the right discount rate for a project that is exactly as risky as Halverson's average project — a capacity expansion in an existing product line, in an existing geography, using a proven manufacturing process.

Plant 4 is not that.

Suppose Plant 4 is in Mexico. Halverson operates in the US Midwest. The plant introduces country risk, currency risk, and operational risk that Halverson's existing business does not carry. The 8% WACC was estimated from a firm with none of those exposures. Discounting the Mexican plant's cash flows at 8% treats those additional risks as free. They are not free.

Here is the precise error. The NPV formula says: discount future cash flows at a rate that reflects their risk. When the risk of the project differs from the risk of the firm, the firm's WACC is the wrong rate to use. Using it anyway produces an NPV that is too high — the denominator is too small — and systematically overstates the case for projects that are riskier than the firm average.

Most firms apply the firm WACC to all projects because it is convenient. The convenience has a real cost. A firm that applies a low discount rate to high-risk projects will accept too many of them. Over years, this introduces a quiet drift toward riskier projects and away from the core competence the firm actually understands. The evidence on this drift in diversified conglomerates is suggestive. The discipline is simple to state: the discount rate should match the risk of the project, not the risk of the firm.

---

## Finding the Right Rate

How do you find a rate that matches the project rather than the firm?

The cleanest method is the pure-play comparable approach. Find publicly traded companies whose primary business is the same as the project's business — not firms that happen to have a division like the project, but firms whose entire operation looks like what the project will be. Compute their betas. Use those betas to estimate a project-appropriate required return.

The mechanics follow from Chapter 5's beta framework, with one important adjustment. The comparable firms have their own capital structures, and capital structure affects measured equity beta. A firm with more debt has a higher equity beta than the same firm with no debt, because fixed debt obligations amplify the variability of equity returns. Before we can use these betas for our project, we need to remove the effect of each firm's capital structure.

This is called unlevering the beta. The formula:

$$\beta_{\text{asset}} = \frac{\beta_{\text{equity}}}{1 + (1 - t) \cdot D/E}$$

where $t$ is the corporate tax rate and $D/E$ is the firm's debt-to-equity ratio. The asset beta removes the capital structure effect and gives a pure measure of business risk — the risk of the underlying operations, independent of how those operations are financed.

![Two-firm leverage diagram showing the unlever-to-asset-beta-then-relever-to-target procedure for project beta](images/06-risk-adjusted-rates-and-real-options-fig-01.png)
*Figure 6.1 — Unlevering and relevering project beta*

Once you have asset betas from several comparable firms, you average them, then re-lever using Halverson's capital structure for the project. This gives an equity beta appropriate for the project under Halverson's financing conditions. Plug into CAPM:

$$R_e^{\text{project}} = R_f + \beta_{\text{project}} \times \text{ERP}$$

For Halverson's Mexican plant, suppose pure-play comparables — publicly traded Mexican industrial manufacturers or US firms with majority Mexican operations — have average asset betas around 1.4 after unlevering. Relevered at Halverson's capital structure:

$$R_e^{\text{project}} = 4.2\% + 1.4 \times 5.0\% = 11.2\%$$

Halverson's firm-level required equity return is 9.8%. The project's required equity return is 1.4 percentage points higher. Combined with the same debt costs and weights, the project WACC comes out around 9.0% instead of 8.0%.

One percentage point sounds modest. Applied across a ten-year cash flow stream plus a terminal value, it is not modest. Maya's $42 million NPV at 8% becomes approximately $25 million at 9%. The project still passes the basic hurdle — the NPV is still positive — but the recommendation is now anchored to what Plant 4 actually is, not to what Halverson's average project is.

![NPV profile curve ](images/06-risk-adjusted-rates-and-real-options-fig-01.png)
*Figure 6.1 — NPV profile curve *

---

## The Future Isn't Locked

Here is a scenario.

Halverson's board approves Plant 4 today. The firm commits $50 million and begins construction. Six months in, regional demand data comes back weaker than expected. The project's NPV, recomputed with the new information, is negative — Halverson would not start this project today knowing what it knows now. But the plant is half-built. The firm has spent $30 million. The rational thing to do, however painful, is to complete the construction and operate at a loss rather than walk away from a half-built facility.

Alternative scenario: Halverson defers the construction commitment by six months. During the deferral, regional demand data comes back weaker than expected. The firm cancels the project. It has spent only the planning costs — perhaps $500,000. It avoids the $50 million capital outlay and the subsequent operating losses entirely.

These two scenarios produce materially different financial outcomes. The standard NPV formula does not distinguish between them.

The NPV formula asks: given today's probability distribution over future cash flows, is the expected discounted value positive? It implicitly assumes the decision is made today, irrevocably, and the firm then watches the future unfold without any ability to act on new information. No competent manager actually operates this way. Every manager retains the ability to accelerate, defer, scale up, or abandon as information arrives.

The value of that flexibility is real, and it belongs in the analysis.

---

## Real Options

The word "option" is doing the same work here as in financial options. A call option on a stock gives you the right, but not the obligation, to buy the stock at a fixed price on a future date. You exercise if the stock price exceeds the strike; you walk away if it doesn't. The asymmetric payoff — you capture the upside, you limit the downside — is why the option has value even before you know whether you will exercise it.

A real option is the same structure applied to a capital project: the right, but not the obligation, to make a capital investment at a future date based on information available at that date. Three forms appear most often.

The option to defer: the right to wait and invest later rather than now. Valuable when uncertainty is high and waiting will reveal information that matters for the decision. The firm gives up early cash flows in exchange for not committing capital before the uncertainty resolves.

The option to expand: the right to invest more if early results are good. Valuable when the initial project serves as a platform for follow-on investments. Plant 4 is not just Plant 4 — it is the option to build Plants 5 and 6 if Plant 4 demonstrates regional demand.

The option to abandon: the right to terminate the project and recover salvage value if results are bad. Valuable when assets are redeployable. A plant built with general-purpose equipment can be sold; a plant built with single-purpose tooling cannot.

Plant 4 plausibly has all three. Halverson can defer the commitment, expand if demand is strong, and sell a general-purpose manufacturing facility if demand collapses.

---

## Why Options Have Value

The key insight is about selective exercise.

When you hold an option, you exercise it selectively. You exercise when conditions are good. You decline when conditions are bad. This selective exercise breaks the symmetry of the underlying uncertainty: you get the full upside of good scenarios, and you limit your downside by refusing to participate in bad ones.

The NPV formula, by contrast, averages across all scenarios before discounting. It has no mechanism for the manager to say "I would not invest in the bad scenario." Every scenario, good and bad, contributes to the expected cash flow that gets discounted.

When a firm has real flexibility, the NPV formula systematically understates value because it charges the firm for bad scenarios it could actually avoid.

Here are numbers for Plant 4.

Suppose that regional demand over the next six months resolves into one of two roughly equally likely states: strong demand, where the NPV of committing to Plant 4 at that point is $80 million, or weak demand, where the NPV of committing is −$10 million.

If Halverson commits today, it commits regardless of which scenario materializes. The expected NPV — accounting for the time value of waiting six months — is roughly:

$$0.5 \times \$80\text{M} + 0.5 \times (-\$10\text{M}) = \$35\text{M}$$

If Halverson waits six months and decides based on the information that arrives, it commits only in the strong-demand scenario:

$$0.5 \times \$80\text{M} + 0.5 \times \$0 = \$40\text{M}$$

The $0 in the second term reflects the firm declining to invest in the weak-demand scenario. It does not lose $10 million — it simply does not commit the capital.

The difference between $40 million and $35 million is the option value: $5 million. That is what the deferral flexibility is worth. The standard NPV ignores it because the standard NPV formula has no mechanism for the manager to act on six-month information.

This is not a rounding error. In decisions with high underlying uncertainty — new geographies, new technologies, new product lines — option value can be the largest single component of a project's total value.

---

## Computing It: The Decision Tree

Two approaches are standard. I will spend more time on the first, because it is more transparent and more honest about what we actually know.

The decision tree maps out the scenarios, the probabilities, and the decisions available at each stage. Starting from the right — the final payoffs — you work backwards, taking expected values at chance nodes and choosing the best action at decision nodes. This backward-induction procedure is called dynamic programming, and it is simply the formal name for what a thoughtful manager does intuitively when she thinks through "what would I do if this happened, and what would I do if that happened."

For Plant 4, the tree has two stages. At the root: commit now, or wait six months. The left branch is the standard NPV calculation — commit today at the risk-adjusted rate, NPV approximately $25 million. The right branch — wait — leads to a chance node where strong demand and weak demand each arrive with probability 0.5. At the strong-demand node, the optimal decision is to commit, realizing the $80 million NPV. At the weak-demand node, the optimal decision is to walk away, realizing $0.

![Decision tree for the Plant 4 deferral option, showing commit-now vs. wait-six-months with strong/weak demand branches](images/06-risk-adjusted-rates-and-real-options-fig-02.png)
*Figure 6.2 — The Plant 4 deferral option*

The expected value of the right branch, discounted back six months at the project WACC, is approximately $40 million. The option to defer is worth about $5 million compared to the unconditional commitment — or about $15 million compared to the standard NPV calculation that assumed no optionality and the wrong discount rate simultaneously.

The second approach adapts financial option pricing models — Black-Scholes or binomial trees — to real assets, treating the project value as the underlying asset and the investment cost as the strike price. This approach is mathematically elegant. It is sometimes the right tool when the underlying uncertainty evolves continuously rather than in discrete jumps. For most capital project decisions, though, the decision tree is both more transparent and more honest about the actual nature of the uncertainty. Industrial demand cycles do not follow the lognormal diffusion process that underlies Black-Scholes, and fitting that model to data it was not designed for produces precision that is not accuracy.

---

## Why the Two Corrections Don't Cancel

The risk-adjustment makes the NPV smaller. The real options adjustment makes it larger. It is natural to wonder whether they approximately offset.

They do not cancel, and understanding why requires seeing that they correct different kinds of errors.

The risk-adjustment corrects a valuation error. The expected future cash flows from Plant 4 are being discounted at a rate that does not reflect how risky those cash flows are. Making the discount rate higher does not change what the cash flows are — it changes what they are worth today. The project is being overpriced; the correction re-prices it.

The real options adjustment corrects a strategy error. The standard NPV computes the expected value of a particular strategy: commit today, irrevocably. That is not the strategy Halverson will actually follow. The firm will follow a contingent strategy: commit if conditions look favorable, defer or abandon if they do not. The contingent strategy has higher expected value than the irrevocable commitment, because it excludes bad-scenario capital commitments. The correction replaces the wrong strategy with the right one.

One fixes the price. The other fixes the plan. These are genuinely different operations.

For Plant 4, the combined picture:

| Analysis | NPV |
|---|---:|
| Firm WACC (8%), no optionality — Maya's original | $42M |
| Project WACC (9%), no optionality | $25M |
| Project WACC (9%), with deferral option | ~$30M |

| Scenario | NPV finding | What error it corrects | What the board is actually being asked to approve |
|---|---|---|---|
| **Row 1** — Original analysis at firm WACC | Negative NPV ($-3M$) at firm WACC | (No correction) — the project is overpriced as proposed | Approve $50M of capital today |
| **Row 2** — Project-specific rate | Positive NPV ($+8M$) at project-specific rate of 9.5% | Corrects the discount-rate mismatch — the project's risk profile differs from the firm's | Approve $50M of capital today |
| **Row 3** — Project-specific rate + deferral option | Positive NPV ($+15M$); option value $+7M$ | Corrects both the rate *and* the timing — flexibility is worth pricing in | Approve up to $50M with six-month deferral right pending Q2 demand data |

*The third column makes visible that the recommendation's structure changes, not just the number.*

The risk adjustment costs $17 million of apparent NPV. The real option recovers about $5 million. Net effect: the defensible number is roughly $30 million, not $42 million.

Still positive. The project is still worth doing. But notice something more important than the number: the recommendation has changed in structure.

A recommendation grounded in the $42 million NPV says: approve the $50 million commitment today.

A recommendation grounded in the $30 million NPV with deferral option says: approve up to $50 million, but preserve the right to defer the final commitment by up to six months pending Q2 regional demand indicators. The option has value precisely because committing before those indicators arrive throws away information that would be available cheaply.

The real options analysis does not just change a number. It changes what the board is being asked to decide.

---

## The Honest Limits

I want to flag two places where this framework requires more judgment than the mathematics suggests.

The probabilities are judgment calls. The 50/50 split between strong and weak demand in the decision tree is a placeholder — I chose it to make the arithmetic clean. In practice, eliciting these probabilities from operating managers is genuinely difficult. They anchor on numbers that sound reasonable in a conference room. They do not arrive at meetings with calibrated probability distributions for regional industrial demand. The discipline of building a decision tree is valuable regardless — it forces explicit commitment to a structure of uncertainty that can be stress-tested. But the specific numbers going into the tree deserve as much scrutiny as the discount rate.

The pure-play betas are an approximation. The comparable firms are not identical to Plant 4. They have different capital structures, different product mixes, different positions in the economic cycle. The asset betas backed out from them contain noise. The project WACC of 9% should be thought of as "probably between 8.5% and 10%" rather than as a precise figure. The right response is to present a range — project NPV at 8.5%, 9%, 9.5% — so the board can see how sensitive the recommendation is to the rate assumption.

| Discount rate | NPV without optionality | NPV with deferral option | Option value |
|---|---|---|---|
| **8.5%** | +$12M | +$22M | $10M |
| **9.0%** | +$5M | +$15M | $10M |
| **9.5%** | +$0M | +$11M | $11M |
| **10.0%** | −$5M | +$8M | $13M |

*Both NPV and option value move with the discount rate. The option is *more* valuable as the rate rises — uncertainty becomes more expensive, so flexibility becomes more valuable.*

Both limits point toward the same meta-point: the value of risk-adjustment and real options analysis is not that they produce precise numbers. It is that they force the right questions. Is this project actually riskier than our average? How much of the project's value depends on our ability to learn before committing? These questions improve the decision even when the quantitative answers are approximate.

---

## What Would Change My Mind

The chapter's enthusiasm for real options rests on the claim that they genuinely improve capital allocation decisions when applied. The empirical evidence is suggestive but complicated. Firms that explicitly value real options do not consistently outperform firms that use simpler NPV approaches, at least not in ways that survive controls for other capital allocation quality differences. The optimistic interpretation is that real options are good but rarely applied correctly. The pessimistic interpretation is that the framework adds analytical complexity without adding decision quality.

I find the pessimistic interpretation plausible in the specific case where the probability estimates are arbitrary and the decision tree becomes a tool for rationalizing a conclusion already reached. If the tree's probabilities are chosen to make the option value whatever the sponsor wants, the real options analysis is not discipline — it is decoration. The framework is worth taking seriously precisely because it identifies real flexibility that standard NPV ignores. The discipline is to treat probability estimation as seriously as discounting, not as a free parameter.

---

## Still Puzzling

The two problems corrected here — wrong discount rate and no flexibility — both make the NPV analysis more accurate. But there is a third problem that this chapter does not solve: the cash flow forecasts themselves.

The $42 million NPV depends on a revenue forecast built on assumptions about regional demand, market share, pricing, and competitive response — all uncertain, all estimated by the same operating managers who proposed the project. There is a well-documented pattern in capital budgeting research where project proponents systematically overestimate revenues and underestimate costs, producing NPVs that are optimistic relative to eventual outcomes.

The risk-adjusted discount rate partially addresses this: a higher rate penalizes cash flows that are far in the future, which is where optimistic forecasts tend to be largest. But it does not address the optimism in the forecast itself. The best practice I know — comparing the project's assumptions to the base rate of actual outcomes from similar projects at this firm and comparable firms — is not a formula. It is a discipline that requires the CFO to push back on operating managers who are emotionally committed to seeing their projects approved.

The discount rate can be corrected with math. The forecast bias requires a different kind of honesty.

---

Chapters 4 through 6 have treated capital budgeting as a single-firm problem — Halverson deciding in isolation whether to build Plant 4. Chapter 7 zooms out: how does the firm choose between Plant 4 and the other capital requests competing for the same pool of funds? This is the capital rationing problem, and it requires a framework for ranking projects with different sizes, different durations, and different risk profiles.

---

## Exercises

### Warm-up

**1.** Halverson's firm WACC is 8%. A pure-play comparable for Plant 4 has an equity beta of 1.6, a debt-to-equity ratio of 0.4, and a tax rate of 25%. Unlever the beta. Then re-lever it at Halverson's D/E ratio of 0.3 and the same tax rate. Using a risk-free rate of 4.2% and an equity risk premium of 5.0%, compute the project-appropriate required equity return.
*Tests: mechanical application of the unlevering and relevering formulas; distinguishing firm beta from project beta.*

**2.** A project has equally likely upside NPV of $60 million and downside NPV of −$8 million if committed to today. If the firm instead waits one period and invests only in the upside scenario, what is the expected NPV of the contingent strategy? What is the option value of waiting? Ignore discounting for this calculation.
*Tests: the core selective-exercise arithmetic that underlies all real options valuation.*

**3.** Explain in plain language why using the firm WACC to discount a riskier-than-average project produces an NPV that is too high. What specific feature of the NPV formula causes this error, and in which direction does it push the recommendation?
*Tests: conceptual understanding of the discount-rate-as-risk-price mechanism.*

---

### Application

**4.** You are evaluating a new product line for a consumer goods firm whose WACC is 7%. The product line is in a higher-growth, higher-volatility segment than the firm's existing business. You identify three pure-play comparables with equity betas of 1.3, 1.5, and 1.2, D/E ratios of 0.5, 0.3, and 0.6, and a common tax rate of 25%. The firm's D/E ratio is 0.35. Unlever each comparable, average the asset betas, re-lever at the firm's D/E, and compute the project WACC using a risk-free rate of 4.0% and ERP of 5.5%. The project's NPV at 7% is $18 million. What is it at the project-appropriate rate?
*Tests: full pure-play comparable workflow end to end; translating a rate change into NPV impact.*

**5.** Halverson is deciding whether to commit $30 million to a new distribution center today or wait 12 months. If it waits, it will observe whether a major competitor enters its primary market. It estimates a 40% chance the competitor enters (making the distribution center NPV = −$5M) and a 60% chance they do not (NPV = $20M). If it commits today without waiting, the expected NPV is $9M. Should Halverson wait? What is the option value of the 12-month deferral? What would the competitor-entry probability need to be for immediate commitment and deferral to be equivalent?
*Tests: applying the deferral option framework to a specific scenario; solving for the break-even probability.*

**6.** A project sponsor argues: "We should use the lower firm WACC because the project is funded with the same debt and equity as everything else we do — the financing doesn't change just because the project is riskier." Identify the error in this argument. What is the sponsor conflating, and why does the source of funding not determine the appropriate discount rate?
*Tests: distinguishing the cost of financing from the required return on a risky asset; a common and consequential confusion.*

**7.** Plant 4 has been analyzed with a binary demand outcome (strong or weak, 50/50). A more careful analysis suggests three scenarios: strong demand (p = 0.3, NPV if committed = $90M), moderate demand (p = 0.5, NPV = $20M), and weak demand (p = 0.2, NPV = −$15M). The firm can defer six months to observe which scenario materializes, at a deferral cost equivalent to a $3M present value penalty. Build the decision tree and determine whether deferring is worth the cost. What is the net option value after the deferral penalty?
*Tests: extending the two-scenario framework to three outcomes; incorporating a cost of waiting.*

---

### Synthesis

**8.** The chapter argues that the risk-adjustment and the real options correction fix different errors and therefore do not cancel. A colleague claims: "They do partially offset — a higher discount rate already penalizes future bad scenarios by reducing their present value, which is doing some of the same work as real options." Evaluate this claim. In what sense is the colleague partially right? In what sense does this confuse two distinct problems?
*Tests: deep understanding of the valuation error vs. strategy error distinction; stress-testing the chapter's central claim.*

**9.** Maya presents the $30 million risk-adjusted NPV with deferral option to the board. A board member responds: "I don't trust the 50/50 probability assumption. If the probability of weak demand is actually 70%, does the project still make sense?" Compute the NPV with optionality at p(weak) = 0.7. Then identify what additional information Maya would need to argue confidently for a specific probability estimate, and what organizational dynamics the chapter describes that make that estimate hard to obtain.
*Tests: sensitivity analysis on decision tree inputs; connecting quantitative fragility to the organizational reality of probability elicitation.*

---

### Challenge

**10.** The "Still Puzzling" section identifies forecast bias — systematic optimism in project cash flow estimates — as a problem that risk-adjusted discount rates only partially address. Using the frameworks from this chapter and your own reasoning, design a practical procedure a CFO could use to detect and correct for forecast bias in capital project proposals. The procedure should be specific enough to implement (not just "be more skeptical") and should account for the organizational dynamic the chapter names: sponsors who are emotionally committed to approval. Then identify the one condition under which your procedure would fail to improve decision quality.
*Tests: extending the chapter's admitted limit into a constructive solution; finding the boundary condition of your own answer.*

---

###  LLM Exercise — Chapter 6: Risk-Adjusted Rates and Real Options

**Project:** Halverson's Board Memo, Built Across the Course
**What you're building this chapter:** The Project-Specific-Rate and Real-Options section of the memo: the projects in your portfolio that need a risk-adjusted rate, and the real-option value of the most flexibility-rich project.
**Tool:** Claude Code

---

**The Prompt:**

```
I'm working on Halverson's Board Memo. The WACC is defended in `analysis/05-wacc.md`.

Chapter 6 taught:
- **One discount rate doesn't always work** — projects with risk profiles different from the firm's average require project-specific rates
- **Real options** — defer, abandon, expand, contract — have value that NPV alone misses
- **The optionality premium** — flexibility is worth paying for when forecast uncertainty is high

Scaffold `analysis/06-real-options.py`:

1. **Identify the projects in your portfolio that have meaningfully different risk than the firm average.** For Halverson: a venture-style growth project has higher risk than a maintenance capex; a regulated utility build has lower risk. For each project, name its risk profile relative to the firm and recommend either *firm WACC* or *project-specific rate*.

2. **Estimate one project-specific rate.** For the project whose risk profile is most different from the firm average, build a comparable-firm beta proxy (pull pure-play comparables from the same industry segment), unlever and relever beta against the project's target capital structure, and compute a project-specific cost of capital.

3. **Identify the project with the most real-option content.** Look for: a project that can be deferred at low cost; a project that can be abandoned partway through with significant residual value; a project that creates a follow-on opportunity (an *expand* option). Pick one.

4. **Quantify the real-option value.** Use either a binomial tree (Cox-Ross-Rubinstein) or a Black-Scholes analog. State the inputs: underlying value (the project's NPV today), exercise price (the cost to expand / continue), volatility (your best estimate of the underlying business's annualized vol), time to expiration (when the decision gates close).

5. **Produce `analysis/06-real-options.md`** containing: the project-by-project risk-rate assignment, the one project-specific rate computed, the real-option valuation, and a one-paragraph case for whether the option value is large enough to change the Chapter 4 portfolio recommendation.

Run with `python analysis/06-real-options.py --portfolio analysis/04-portfolio-ranked.md`.
```

---

**What this produces:** A runnable script `analysis/06-real-options.py` plus `analysis/06-real-options.md` containing the project-rate assignments, one project-specific rate, one real-option valuation, and the impact on the portfolio recommendation.

**How to adapt this prompt:**

- *For your own project:* Substitute your firm for Halverson where Halverson appears; the exercise structure is firm-agnostic. Halverson's named cast (Diane / Priya / Cardinal) is scaffolding — replace as needed.
- *For ChatGPT / Gemini:* Works as-is. For ChatGPT, save the running memo to a Custom GPT instead of a Claude Project. For Gemini, paste the project's accumulated section files into the context window each session.
- *For Claude Code:* Right tool. Implementing the binomial tree and the comparable-firm beta unlever/relever is short but precise.
- *For a Claude Project:* Append to the project. If real-option value is material, it goes in the *Recommendation* section of the Chapter 15 board memo as an explicit modifier on Chapter 4's NPV ranking.

**Connection to previous chapters:** Chapter 5 produced one rate for the firm; Chapter 6 names where that one rate is wrong and what to use instead.

**Preview of next chapter:** Chapter 7 takes a step back from project-level analysis to the firm-level capital-structure question — beginning with the Modigliani-Miller baseline.

---

##  AI Wayback Machine
The ideas in this chapter didn't appear from nowhere. **Irving Fisher** was publishing *The Theory of Interest* in 1930 — the foundational treatment of how rational actors trade present consumption against uncertain future cash flows, the structural ancestor of every risk-adjusted discount rate and every real-option valuation decades before most people had heard of risk-adjusted rates and real options. Here's a prompt to find out more — and then make it better.

![Irving Fisher, c. 1920s. AI-generated portrait based on a public domain photograph (Wikimedia Commons).](images/irving-fisher.jpg)
*Irving Fisher, c. 1920s. AI-generated portrait based on a public domain photograph.*

![Irving Fisher](../images/irving-fisher-cz3.png)

*Puppet Art by [Nik Bear Brown](https://www.nikbearbrown.com/).*

**Run this:**

```
Who was Irving Fisher, and how does his 1930 *Theory of Interest* — the formal account of intertemporal choice under uncertainty — connect to the chapter's apparatus for risk-adjusted discount rates and the real-options framework for projects whose value depends on flexibility, not certainty? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.
```

→ Search **"Irving Fisher"** on Wikipedia after you run this. See what the model got right, got wrong, or left out.

**Now make the prompt better.** Try one of these:

- Ask it to explain *Fisher's separation theorem* in plain language, as if you've never read intertemporal choice theory
- Ask it to compare Fisher's discounting framework to the modern real-options approach for an R&D investment
- Add a constraint: "Answer as if you're writing the discount-rate justification for a project with deferred information value"

What changes? What gets better? What gets worse?
