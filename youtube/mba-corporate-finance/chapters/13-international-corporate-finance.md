# Chapter 13 — International Corporate Finance


## TL;DR

- There is a temptation, when first encountering international finance, to treat it as a fundamentally different subject from what came before — a separate discipline with its own rules, its own logic, its own...
- The chapter moves through Warm-up, Application, Synthesis, Challenge, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

*The framework doesn't change. The variables do.*

---

There is a temptation, when first encountering international finance, to treat it as a fundamentally different subject from what came before — a separate discipline with its own rules, its own logic, its own vocabulary of forwards and swaps and country risk premiums. The implication is that everything built in the previous twelve chapters needs to be replaced.

It does not. International corporate finance is corporate finance with additional dimensions. The cash flows are still cash flows. The discount rate still reflects risk. NPV is still the right criterion for investment decisions. Capital structure still trades off tax benefits against distress costs. What changes is that some quantities you previously took as given — a single currency, a single tax regime, a stable regulatory environment — are now variables that require explicit treatment.

There are five new dimensions. Two of them are genuinely analytically different from anything in domestic finance. The other three are mostly administrative complexity layered on top of the same underlying logic. Knowing which is which is most of the practical value of this chapter.

---

Halverson Manufacturing's UK subsidiary, Halverson Flow Control Ltd., generates roughly £80 million of revenue annually from a facility outside Manchester. It was acquired in 2014 and has paid for itself in cumulative repatriated cash. It currently holds £25 million of cash that has not been sent back to the parent — partly because UK-to-US tax planning became complicated after the 2017 US tax reform, and partly because nobody needed the money urgently enough to deal with it.

Diane now wants Maya to evaluate repatriating the £25 million to help fund an acquisition, and to frame a broader recommendation on Halverson's international financial structure.

The five new dimensions are currency, country risk, tax, transfer pricing, and repatriation friction. Let me work through each, and then show which ones are actually doing analytical work for Halverson and which ones are administrative complexity in disguise.

| Dimension | Analytically new vs. administrative overlay | What it changes in the analysis | Halverson UK exposure level |
|---|---|---|---|
| **Currency** | **New** | Cash flows must be denominated; discount rate must match currency; hedging is a real cost | **High** (UK subsidiary generates £-denominated revenue) |
| **Country risk** | **New** | Discount rate carries a country-risk premium; political and contract-enforcement risk priced explicitly | Low (UK is investment-grade sovereign) |
| **Tax (foreign jurisdiction)** | Administrative overlay | Effective tax rate changes; repatriation rules layer in | Medium (UK corporate tax + repatriation) |
| **Transfer pricing** | Administrative overlay | Where profit is booked vs. where it's earned; arm's-length-pricing documentation | Medium-High (intercompany IP licensing flows) |
| **Repatriation** | Administrative overlay | Withholding tax on dividends; cash trapped in subsidiary | Low (UK-US treaty is favorable) |

---

FX exposure is not one thing. It is three distinct problems that require different analytical tools and different management responses. Conflating them is a persistent source of confusion, and I want to separate them carefully.

Transaction exposure is the simplest. A specific future cash flow, denominated in a foreign currency, with a known amount and a known settlement date. Halverson UK signs a contract today for £10 million of revenue payable in 90 days. The dollar value of that £10 million will depend on the GBP/USD rate in 90 days. If the pound is at 1.28, Halverson receives $12.8 million. If the pound has fallen to 1.20, it receives $12.0 million. The $800,000 difference is pure FX risk on a transaction that has nothing to do with the underlying business quality.

Transaction exposure is manageable because you know the amount and the date. The firm can sell pounds forward — agree today to exchange the £10 million for dollars at a fixed rate on the settlement date — and lock in the dollar value of the receivable. The forward contract eliminates the FX risk at a cost roughly equal to the interest rate differential between the two currencies, which is usually small. Halverson hedges transaction exposure on a rolling 12-month horizon. This is standard treasury practice for any firm with meaningful foreign currency receivables.

Translation exposure is different and, I will argue, less important than it sounds. When Halverson consolidates its UK subsidiary's financials into the parent's annual report, it has to convert pound figures into dollars. Earnings use average exchange rates for the period. The balance sheet uses the period-end rate. If the pound weakens during the year, the UK subsidiary's earnings translate into fewer dollars, and reported consolidated earnings per share falls — even if the underlying UK business performed exactly as expected in local currency terms.

This is real for reported financials. It can affect how analysts read the income statement and move the stock price in the short run. But it is largely cosmetic for actual cash flows. The dollars Halverson can spend are not reduced by translation loss, because translation loss is an accounting artifact of currency conversion, not a cash event. Most CFOs do not hedge translation exposure because the hedge cost is real and the underlying economic exposure is not. Halverson does not hedge translation.

Economic exposure is the hardest to measure and can be the largest of the three. It is the long-run effect of persistent exchange rate movements on the firm's competitive position and underlying cash-flow-generating capacity.

Here is the mechanism. Suppose the pound weakens persistently — by 15% over three years, not a quarterly fluctuation but a structural shift. In the short run, Halverson UK's translated earnings fall. But something else happens: the UK subsidiary's cost base, which is largely in pounds, becomes cheaper relative to US-based competitors whose cost bases are in dollars. Halverson UK becomes more competitive. It can price more aggressively against US firms selling into the UK market, or export to the US at attractive prices, or maintain margins and grow market share. The underlying business becomes more valuable even as the translated earnings look worse.

Economic exposure runs in the opposite direction when the pound strengthens. Halverson UK's costs rise relative to US competitors.

Managing economic exposure requires operational decisions, not financial hedging. Where the firm sources its inputs, where it manufactures, where it denominates its invoices — these choices determine how sensitive the underlying cash flows are to exchange rate movements. A firm that manufactures in the UK, sources inputs in the UK, and sells in the UK has low economic exposure to GBP/USD movements. A firm that manufactures in the US and sells in the UK has high economic exposure. A financial hedge can address transaction flows. Only the operational structure can address the underlying exposure.

| Exposure type | What drives it | Affects cash flows? | Hedgeable financially? | Halverson's response |
|---|---|---|---|---|
| **Transaction** | Specific contracts denominated in non-USD currency, settling in the future | **Yes** — currency move directly hits realized cash | **Yes** — forwards, futures, options | Hedge 70% via rolling 12-month forwards |
| **Translation** | Consolidation of foreign-subsidiary financial statements into USD | No — accounting artifact only | No (not really — only cosmetically) | Do not hedge |
| **Economic** | Long-run shift in competitive position from currency moves | **Yes** — but slowly, through margin compression and volume changes | Partial (operational hedges: matching cost and revenue currencies) | Address via operational footprint over time, not financial hedge |

---

The NPV framework from Chapter 4 applies to cross-border projects. What changes is the discount rate and the currency in which cash flows are expressed. Getting these right matters more than it might seem, because the most common error in international project valuation produces numbers that are systematically wrong in a specific direction.

There are two equivalent approaches, and I want to be explicit about both because either can be executed correctly and one can be corrupted into a common error.

The first approach: project all cash flows in the foreign currency, discount at the foreign-currency cost of capital, convert the resulting NPV to home currency at today's spot exchange rate. For a Mexico plant, this means projecting the peso cash flows, applying a peso discount rate, and converting the peso NPV to dollars. The peso discount rate is the firm's dollar WACC adjusted for the Mexico-US inflation differential and a country risk premium.

The second approach: convert each year's foreign-currency cash flow to home currency using expected forward exchange rates, then discount the resulting dollar cash flow stream at the dollar cost of capital. Project the peso cash flows, convert each year to dollars using the forward rate for that year — observable in currency forward markets, or derivable from interest rate parity — and discount the dollar stream at Halverson's dollar WACC.

Both approaches give the same answer when executed consistently. The second is more common in practice because the forward rates are directly observable and the discount rate is the firm's familiar WACC.

![Two parallel paths to the same dollar NPV](images/13-international-corporate-finance-fig-01.png)
*Figure 13.1 — Two parallel paths to the same dollar NPV*

The error that produces nonsense: applying the dollar discount rate to unconverted foreign-currency cash flows. This is wrong because the dollar WACC implicitly contains US inflation and US interest rate expectations. Applying it to peso cash flows — which embed Mexican inflation — mixes incompatible units. The resulting NPV will be too low if Mexican inflation is high, because the peso cash flows are nominally large but you are discounting them at a rate that does not account for their inflation content. This error is easy to make without noticing, and it systematically biases the analysis against emerging-market projects where inflation differentials are large.

---

When Halverson evaluates a Mexico plant, it faces business risk that its US operations do not face: regulatory change, FX controls, political instability, contract enforcement difficulties. These risks reduce the expected value of the project's cash flows and increase their variability. The discount rate needs to reflect them.

The standard approach adds a country risk premium to the discount rate. Damodaran maintains a widely used series of these premiums, derived from sovereign CDS spreads adjusted for the relative volatility of equity markets versus bond markets. Indicative figures: the United Kingdom carries perhaps 50 basis points; Mexico, roughly 250; Brazil, roughly 400; Argentina, an order of magnitude higher.

| Country | Approximate CRP (bps) | Discount rate if base WACC is 8% | Primary driver of premium |
|---|---|---|---|
| **United States** | 0 | 8.0% | (Reference) |
| **United Kingdom** | 30 | 8.3% | Macro; mild contract-enforcement uncertainty post-Brexit |
| **Germany** | 50 | 8.5% | Macro; FX |
| **Brazil** | 250 | 10.5% | FX; political |
| **Argentina** | 800 | 16.0% | FX; macro; contract enforcement |
| **Russia** | 900+ | 17%+ | Political; contract enforcement |
| **Venezuela** | 1500+ | 23%+ | Political; FX; macro |

*The CRP is a bundled number masking several distinct risk types. For a real deployment in a high-CRP country, the bundling should be unbundled and each component priced separately.*

For a Mexico plant with a firm WACC of 8%, the adjusted discount rate is approximately 10.5%. This is consistent with what a pure-play comparables analysis produces for Mexican industrial operations — the two approaches triangulate to the same range, which is reassuring.

The CRP approach is a shortcut. It bundles political risk, FX risk, and macroeconomic instability into one number. For a more rigorous analysis in a high-risk jurisdiction, decomposing the premium into components and pricing each one separately is better — but requires estimates that are themselves uncertain. The shortcut is appropriate for project screening; the decomposed approach is appropriate for a final investment decision in a difficult jurisdiction.

I should flag a genuine disagreement in the academic literature here. The concern is that the CRP bundles together risks that have different pricing implications. Political risk, for instance, is largely diversifiable for an investor with a globally diversified portfolio; if so, it should not enter the discount rate at all — only systematic risk should be priced. The Damodaran approach includes political risk regardless of whether it is diversifiable, which may overstate the cost of capital for cross-border projects in politically unstable jurisdictions. Whether this critique is correct is empirically contested.

I find this debate genuinely open. The practitioner consensus uses CRP adjustments because they produce defensible numbers and because boards understand "Mexico is riskier, add 250 basis points" more readily than arguments about the diversifiability of political risk. Defensibility and theoretical correctness are not always the same thing, and I think it is better to name that honestly than to present the CRP shortcut as settled science.

---

International tax has been fundamentally restructured in the past decade. The 2017 US tax reform introduced new regimes governing foreign income that represent the largest change to international tax rules in a generation. Treasury regulations and case law continue to evolve. Any specific tax rate cited here may be outdated within months of publication, and for Halverson's actual decisions, the tax analysis belongs to specialists who know the current rules.

What I can give you is the framework, which is more durable than the rules.

International tax planning for a US multinational addresses three questions. Where is income earned — which is determined by transfer pricing, the price set on transactions between the US parent and its foreign subsidiaries. Where is income retained versus repatriated — income retained at the UK subsidiary may not be immediately subject to US tax, while income repatriated as a dividend triggers US tax after applying foreign tax credits. And what entity structure minimizes the combined tax burden — the domain of holding companies, hybrid entities, and intercompany financing arrangements, all of which must satisfy substance-over-form requirements in each jurisdiction.

The transfer pricing question is worth dwelling on, because it has no clean theoretical resolution and I want to be honest about this rather than presenting the arm's-length standard as if it solves the problem it claims to solve.

When Halverson licenses proprietary technology to its UK subsidiary — technology that was developed jointly, that has no external market price, and that the subsidiary needs to compete — there is no natural arm's-length transaction to reference. The "correct" royalty rate is whatever produces the desired income allocation between jurisdictions, dressed up in a comparables analysis. Both tax authorities know this. Both challenge the analysis when the allocation is not in their favor. The resulting compliance burden is real, the audit risk is real, and the outcome is largely a function of the negotiating leverage between the multinational and the respective tax authorities.

This is not a solvable technical problem. It is a political economy problem inside the firm's financial structure. A CFO who expects to find the right transfer price through financial analysis will be disappointed. The right transfer price is the one that survives audit challenge, which depends on documentation quality, the tax authorities' current enforcement priorities, and sometimes the firm's overall relationship with the revenue authorities in each jurisdiction.

---

For Halverson's specific question — repatriate the £25 million or leave it in the UK — the framework reduces to a capital allocation comparison.

If the cash stays in the UK, it earns returns appropriate for UK cash management — roughly UK short-term interest rates, currently modest. The capital remains available for potential UK reinvestment, but there are no identified UK opportunities of comparable attractiveness to the acquisition Diane is evaluating.

If the cash is repatriated, it earns whatever return the acquisition generates on invested capital, less the incremental US tax on the dividend. At a spot rate of roughly 1.27, £25 million is approximately $31 million. After estimated incremental US tax — which depends on Halverson's foreign tax credit position, but could be 0 to 5% of the repatriated amount — the parent receives approximately $29 to $31 million.

The acquisition's projected return substantially exceeds the UK cash management return. The incremental US tax cost is modest. The economic case for repatriation is positive if the acquisition's return exceeds the UK cash return by more than the tax cost — at 0 to 5%, that is a low bar.

The recommendation is to repatriate now, document the tax position carefully to support any future audit challenge on the foreign tax credits, and treat the decision as what it actually is: a capital allocation decision with a tax overlay, not a tax decision with a capital allocation dimension.

This illustrates the broader principle. Repatriation decisions are not fundamentally tax decisions. They are capital allocation decisions. The question is always whether the internal return on the capital is higher inside the foreign subsidiary or at the parent level. When the parent has an identified high-return use, the answer is almost always to repatriate.

---

There is a diagnostic question worth asking about any cross-border analysis: is the international layer adding genuinely new financial considerations, or is it adding compliance and administrative burden on top of the same underlying logic?

For Halverson UK — a UK firm doing the same kind of business as the US parent, in a stable legal jurisdiction, with transparent accounting standards and efficient capital markets — the honest answer is mostly the latter. The capital budgeting decisions follow domestic logic with currency and tax overlays. The capital structure question is the same trade-off analysis from Chapter 8 with a higher effective tax rate. The payout decision is the same cash deployment question with repatriation friction added.

For an operation in an emerging market with an unstable regulatory regime, weakly enforced contract law, and a history of capital controls — the honest answer is the former. The international complexity becomes first-order. The capital budgeting model needs fundamentally different inputs. The capital structure may require host-country financing to reduce expropriation exposure. The repatriation strategy may need to be built into the project design from day one, because getting money out may be the hardest part of the whole investment.

The diagnostic matters because treating first-category problems as if they are second-category wastes time and adds false precision. Treating second-category problems as if they are first-category is how firms lose money they did not expect to lose.

Halverson UK is first-category. A Mexico plant would be closer to the boundary — not the full complexity of an unstable emerging market, but enough genuine first-category risk that the analysis cannot be domestic-plus-tax-overlay.

The framework holds. The variables multiply. Knowing which variables are doing real analytical work, and which ones are administrative noise, is what separates a useful international financial analysis from a document that is thorough and wrong.

---

## Exercises

### Warm-up

**1.** Halverson UK has a £6 million receivable due in 60 days. Today's GBP/USD spot rate is 1.26. The 60-day forward rate is 1.24. The CFO decides not to hedge. Calculate the dollar value of the receivable if the spot rate at settlement is (a) 1.22 and (b) 1.29. Then state in one sentence what the forward contract would have cost in dollar terms and what it would have guaranteed. *(Tests: mechanical calculation of transaction exposure and the forward hedge.)*

**2.** Halverson's UK subsidiary reports £8 million in net income for the year. At the start of the year, GBP/USD was 1.30; the average rate for the year was 1.22; the year-end rate is 1.19. Calculate the translation of net income into dollars. Then explain in two sentences why this translated number is not the same as the cash Halverson can deploy at the parent level. *(Tests: translation exposure mechanics and the distinction between accounting and cash impact.)*

**3.** A firm's Mexico plant has a dollar WACC of 8%. The analyst discounts the plant's peso cash flows at 8% and gets a positive NPV. Identify the error and explain which direction it biases the result — too high or too low — when Mexico's inflation rate substantially exceeds the US rate. *(Tests: recognition of the unit-mixing error in cross-border valuation.)*

---

### Application

**4.** Halverson is evaluating a new subsidiary in Brazil. The firm's dollar WACC is 8% and the country risk premium for Brazil is approximately 400 basis points. Brazil's current inflation rate is roughly 8% annually; US inflation is roughly 3%. Using Approach 2 (forward rate conversion), explain what rate adjustment is needed to produce dollar cash flows for discounting, and why a simpler approach of just adding the CRP to the dollar WACC could double-count the inflation differential. *(Tests: cross-border valuation mechanics with a high-inflation case, distinguishing the CRP from the inflation adjustment.)*

**5.** Halverson UK holds £40 million of cash. The parent identifies two uses: (a) leave it in the UK in short-term gilts yielding 4.5% per year, or (b) repatriate and invest in a US acquisition projected to return 14% annually. Incremental US tax on repatriation is estimated at 3% of the repatriated amount. At a spot rate of 1.27, calculate the after-tax dollar proceeds from repatriation. Then state the minimum acquisition return that would make repatriation economically neutral versus leaving the cash in the UK. *(Tests: the repatriation-as-capital-allocation framework, quantified.)*

**6.** A US manufacturer sources all components in the US, manufactures in the US, and sells 40% of revenue into the eurozone at prices denominated in euros. A persistent 12% appreciation of the dollar against the euro occurs over two years. Describe the economic exposure: which of the firm's costs, revenues, and competitive positions are affected, and in which direction? Then explain why a euro forward contract hedges the transaction exposure but does not address the economic exposure. *(Tests: distinguishing economic from transaction exposure in a context different from Halverson; requires understanding the competitive mechanism, not just the cash flow arithmetic.)*

**7.** The chapter argues that transfer pricing for unique intrafirm IP licenses has "no clean theoretical resolution." A classmate counters: "The arm's-length standard solves this — just find comparable third-party transactions and use those rates." Identify the specific condition under which the classmate's approach works cleanly and the specific condition under which it fails — and explain why the failure condition is more common than the success condition for multinational IP licensing. *(Tests: understanding the limits of the arm's-length standard and why transfer pricing is a political economy problem.)*

---

### Synthesis

**8.** The chapter's diagnostic question asks whether the international layer is adding "genuinely new financial considerations" or "administrative complexity on top of the same underlying logic." Apply this diagnostic to the three types of FX exposure. For each one, state whether it represents a genuinely new consideration that has no domestic analog, or whether it is a known domestic concept (accounting noise, cash flow risk, competitive risk) that simply operates through a new mechanism. *(Tests: integrating the three-exposure taxonomy with the first-category/second-category diagnostic; rewards students who can connect the chapter's two organizational frameworks.)*

**9.** In Chapter 7, the MM framework established that every real capital structure result is a "deviation from zero" — a named, priceable friction added back to the frictionless baseline. Apply the same logic to international corporate finance. Name the frictionless international baseline (what would be true if MM's four assumptions applied globally and capital markets were perfectly integrated across borders), then identify each of the chapter's five dimensions as a named friction deviating from that baseline. For each, state the direction of the deviation's effect on value. *(Tests: cross-chapter transfer of the MM methodology; rewards students who can construct the "international MM baseline" without being told what it is.)*

---

### Challenge

**10.** The chapter acknowledges a genuine academic dispute about whether political risk should enter the country risk premium at all, since it may be diversifiable for globally diversified investors. Construct the full argument on each side: first, the case that the Damodaran CRP is theoretically correct to include political risk; second, the case that political risk is diversifiable and the CRP overstates the cost of capital. Then identify what empirical evidence would settle the dispute — specifically, what pattern in the data would confirm that political risk is priced systematically (not diversified away) versus what pattern would confirm that it is not. Your answer should engage with the mechanism, not just assert the conclusion. *(Tests: stress-testing the chapter's own admitted uncertainty; distinguishes students who can construct and evaluate competing arguments from students who can only summarize the one the chapter endorsed.)*

---

*Tags: international corporate finance, currency exposure, transaction exposure, translation exposure, economic exposure, country risk premium, transfer pricing, repatriation, foreign project valuation, interest rate parity*

---

###  LLM Exercise — Chapter 13: International Corporate Finance

**Project:** Halverson's Board Memo, Built Across the Course
**What you're building this chapter:** The International Risk Section of the memo: identification of the firm's currency and country exposures, with a hedging program and a transfer-pricing posture defended.
**Tool:** Claude Code

---

**The Prompt:**

```
I'm working on Halverson's Board Memo. The risk register is in `12-risk-register.md`.

Chapter 13 taught:
- **Three currency exposures**: transaction (specific contracts), translation (consolidating financials), economic (long-run competitive impact)
- **Cross-border capital flows**: transfer pricing, repatriation, withholding tax
- **Country risk**: political, regulatory, expropriation, sovereign

Scaffold `analysis/13-international.py`:

1. **Map the firm's geographic footprint.** Revenue by geography, costs by geography, assets by geography. From the segment disclosure in the 10-K. Most US-listed industrials report in 4–8 segments.

2. **Identify the currency exposures.** For each non-USD currency:
   - **Transaction exposure** = next 12 months of contractually committed FX-denominated cash flows
   - **Translation exposure** = net assets denominated in that currency on the consolidated balance sheet
   - **Economic exposure** = impact on competitive position if that currency moves significantly (qualitative)

3. **Quantify the FX-at-risk.** For the top 2–3 currencies, compute a 1-year 95th-percentile loss given the historical volatility of the FX pair. This is the FX exposure measured in dollars.

4. **Design a hedging program.** For each currency, recommend:
   - **Hedge ratio**: percentage of transaction exposure to hedge (typically 50–80% rolling forward)
   - **Instrument**: forwards, options, or natural hedges (matching FX-denominated revenue with FX-denominated costs)
   - **Cost**: the all-in cost of the hedging program (forward points + bid-ask + program management)
   - **What's left unhedged**: the residual exposure the firm consciously accepts

5. **The transfer-pricing posture.** One paragraph. Where does the firm book profit relative to where the operations actually generate it? What's the firm's stated transfer-pricing policy? Are there currently open audits or controversies?

6. **Save `analysis/13-international.md`** containing the geographic footprint, the FX exposure quantification, the hedging program, and the transfer-pricing posture.

Run with `python analysis/13-international.py --ticker [TICKER]`.
```

---

**What this produces:** A runnable script `analysis/13-international.py` plus `analysis/13-international.md` containing the geographic footprint, FX exposures, the hedging program, and the transfer-pricing posture.

**How to adapt this prompt:**

- *For your own project:* Substitute your firm for Halverson where Halverson appears; the exercise structure is firm-agnostic. Halverson's named cast (Diane / Priya / Cardinal) is scaffolding — replace as needed.
- *For ChatGPT / Gemini:* Works as-is. For ChatGPT, save the running memo to a Custom GPT instead of a Claude Project. For Gemini, paste the project's accumulated section files into the context window each session.
- *For Claude Code:* Right tool — pulling segment disclosures, computing FX-at-risk via historical vol, and modeling alternative hedge ratios is multi-step quantitative work.
- *For a Claude Project:* Append to the project. The hedging program goes in the Chapter 15 *risk position* section and interacts with the Chapter 12 risk register.

**Connection to previous chapters:** Chapter 12 priced operational risk; Chapter 13 prices the international slice of it explicitly.

**Preview of next chapter:** Chapter 14 turns inward — to the behavioral biases that distort the recommendations Chapters 1–13 produced.

---

##  AI Wayback Machine
The ideas in this chapter didn't appear from nowhere. **Susan Strange** was founding *international political economy* as a discipline in the 1970s and 1980s — including her account of *casino capitalism* and *mad money*, the foundational analyses of how international financial flows actually move and what they cost the firms exposed to them decades before most people had heard of international corporate finance, currency exposure, and the political economy of cross-border capital. Here's a prompt to find out more — and then make it better.

![Susan Strange, c. 1980s. AI-generated portrait based on a public domain photograph (Wikimedia Commons).](images/susan-strange.jpg)
*Susan Strange, c. 1980s. AI-generated portrait based on a public domain photograph.*

**Run this:**

```
Who was Susan Strange, and how does her work on the *political economy of international finance* — including her analyses of casino capitalism, mad money, and the structural power that international financial flows give certain actors — connect to the chapter's treatment of currency hedging, transfer pricing, and the real costs of operating a firm across borders? Keep it to three paragraphs. End with the single most surprising thing about her career or ideas.
```

→ Search **"Susan Strange"** on Wikipedia after you run this. See what the model got right, got wrong, or left out.

**Now make the prompt better.** Try one of these:

- Ask it to explain *structural power in international finance* in plain language, as if you've never read political economy
- Ask it to compare Strange's 1980s account of cross-border capital flows to a modern multinational's currency-hedging policy
- Add a constraint: "Answer as if you're writing the case for treating FX exposure as a strategic, not just operational, decision"

What changes? What gets better? What gets worse?
