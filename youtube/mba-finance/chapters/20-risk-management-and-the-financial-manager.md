# Chapter 20 — Risk Management and the Financial Manager

*Everything we've built assumes the firm survives. This chapter is about making sure it does.*

---

Spring 2018. The price of jet fuel rises from $2.07 to $2.19 per gallon — a 5.8% increase that looks modest until you multiply it by scale. American Airlines burns about 4 billion gallons a year. Twelve cents a gallon times 4 billion gallons is $480 million of additional annual operating cost. At industry margins where 5–7% operating profit is considered healthy, a half-billion-dollar cost shock can turn a profitable quarter into a loss.

This happens routinely in the airline industry. Some airlines hedge fuel costs with futures contracts, locking in prices months in advance and insulating themselves from the spike. Southwest Airlines was famous for this — in the early 2000s, it hedged so aggressively that it held fuel contracts at prices far below the market, giving it a structural cost advantage over competitors for years. Other airlines hedge less, accepting fuel exposure as the cost of doing business. Both approaches are defensible.

The question the financial manager has to answer: which risks do we hedge, at what cost, and with which instruments? What is it worth to remove uncertainty from the firm's cash flows?

That's the subject of this chapter. It's also the last chapter, and there's something fitting about that. Everything we've built — the DCF valuations, the CAPM cost of equity, the WACC, the capital structure decisions — rests on the assumption that the firm can execute its operating plan. Risk management is the discipline of protecting that assumption. The book has been about value. This chapter is about the things that can destroy it.

---

## What risk actually is

In finance, **risk** is uncertainty about future outcomes. Not just bad outcomes — uncertainty in either direction. A stock that might return anywhere from −30% to +50% is riskier than one ranging from −5% to +10%, because the first one's outcomes are harder to predict. Wider dispersion means more risk.

For a firm's cash flows, the major sources of that uncertainty decompose into five categories.

**Commodity price risk.** Raw material costs change unpredictably. Starbucks's coffee beans, American Airlines's jet fuel, an automaker's steel and aluminum, a semiconductor fab's rare earths. A firm whose input costs are volatile faces cash flow uncertainty that feeds directly into margins and, through the discount rate, into firm value.

**Exchange rate risk.** Any firm with revenues or costs in multiple currencies faces this. A US firm that manufactures in Germany and sells in Japan has euro-denominated costs and yen-denominated revenues; dollar fluctuations against both expose it to cash flow uncertainty even if the underlying business is stable. Exchange rate risk comes in three forms: **transaction risk** (a specific contracted cash flow changes value before it settles), **translation risk** (the accounting translation of foreign-subsidiary results), and **economic risk** (the firm's long-run competitive position shifts because currencies change the relative costs of doing business across countries).

**Interest rate risk.** Firms with floating-rate debt see their interest expense fluctuate with market rates. Firms with fixed-rate debt are insulated from rate changes on existing obligations but face refinancing risk when the debt matures. Financial institutions, which hold assets (loans) and liabilities (deposits) with different maturities and rate structures, face particularly acute interest rate risk.

**Credit risk.** Customers may not pay. Suppliers may not deliver. Counterparties on derivative contracts may default. The firm's own creditors may withdraw credit facilities. Each of these can impair cash flows in ways unrelated to the firm's own operating performance.

**Operational risk.** Supply chains break. IT systems fail. Key people leave. Regulatory environments shift. Natural disasters, pandemics, cyberattacks. Operational risks are the hardest to hedge because they're often one-off, difficult to quantify, and not amenable to financial instruments.

The first three categories are the ones financial hedging addresses directly. The latter two are more about operations, redundancy, and insurance.

<!-- → [INFOGRAPHIC: risk taxonomy diagram — five categories (commodity, exchange rate, interest rate, credit, operational) arranged as branches from a central "firm cash flow risk" node; under each branch, 2-3 real-world examples; color or icon distinguishes the three "hedgeable" categories (financial instruments exist) from the two "operational" categories (hedged through redundancy, insurance, process); caption: the distinction between hedgeable and non-hedgeable risk determines which tools apply] -->

---

## Why risk affects firm value — and why hedging can increase it

The connection to value is direct. From Chapter 11:

$$\text{Firm value} = \sum_{t=1}^{n} \frac{\text{Expected cash flow}_t}{(1 + \text{WACC})^t}$$

Risk enters through the denominator. Investors are risk-averse — they demand higher expected returns for bearing more uncertainty. Higher uncertainty means a higher discount rate. A higher discount rate means a lower present value for the same expected cash flows. Two firms with identical expected cash flows but different volatility will trade at different valuations. The more volatile firm is worth less.

Hedging reduces volatility. Lower volatility reduces the discount rate. Lower discount rate increases firm value. This is the theoretical case for hedging — not that it changes expected cash flows, but that it reduces the premium investors charge for uncertainty.

The practical caveat is immediate: hedging has costs. Forward contracts carry bid-ask spreads. Futures require margin. Options require premiums paid upfront. The value of reduced volatility must exceed the cost of the instruments that produce the reduction. For small exposures or low-volatility industries, it often doesn't. For a Southwest Airlines, it clearly did.

---

## Hedging vs. speculation — same instrument, different intent

The instruments used in hedging and speculation are often identical. The difference is whether the position reduces existing exposure or creates new exposure.

**Hedging** is taking a position that offsets an existing risk. A US firm with a €10M payable in 90 days buys euros forward — the forward contract and the underlying payable cancel each other out. Whatever happens to the exchange rate, the firm's dollar cost is fixed. The exposure is gone.

**Speculation** is taking a position in search of profit from anticipated price movements, without an underlying exposure to offset. The same firm, with no euro payable, buying euros forward because it thinks the dollar will weaken is speculating. The position is identical; the underlying obligation is absent.

The history of risk-management failures is largely a history of hedging programs that drifted into speculation — sometimes through poor governance, sometimes through deliberate concealment, often through the fog that develops when the people running the hedges aren't clearly accountable for the distinction. Procter & Gamble lost $157 million in 1994 on leveraged derivatives that started as hedges. Metallgesellschaft lost $1.3 billion in 1993 hedging oil delivery contracts in a way that created a gigantic cash-flow mismatch when oil prices fell. Sumitomo's copper trader accumulated speculative positions over a decade that ultimately produced $2.6 billion in losses. In each case, the instruments themselves were unremarkable. The problem was how they were used.

The lesson for reading your company's 10-K: transparent, specific disclosure of hedging programs — with notional amounts, instrument types, maturity schedules, and risk-reduction rationale — is a sign of good governance. Vague language about "using derivatives to manage risk" without specifics is a yellow flag.

---

## The hedging instruments

Four instrument types do most of the work.

**Forward contracts.** A bilateral agreement to exchange a specified asset on a future date at a price set today. The US firm with the €10M payable contracts with a bank to buy €10M at $1.10/€ in 90 days. Whatever the spot rate is at settlement, the firm pays $11M. Done.

Forwards are customizable to any amount, currency, and date — the defining advantage. The defining disadvantage is counterparty risk: if the bank fails, the contract is unenforceable.

<!-- → [TABLE: comparison of the four hedging instruments — rows: forward, futures, option, swap; columns: standardized?, exchange-traded?, counterparty risk, upfront cost, payoff structure (symmetric vs. asymmetric), typical use case; student should see the trade-off structure clearly] -->

**Futures contracts.** The standardized, exchange-traded version of a forward. Instead of a bilateral bank contract, the firm buys futures on an organized exchange (CME for currencies and interest rates; ICE for commodities). The contracts are standard sizes and expiry dates — a firm can't buy exactly €10M of futures, so it approximates with 80 contracts at €125,000 each.

The exchange's clearinghouse stands between buyer and seller, essentially eliminating counterparty risk. The cost is daily marking-to-market — gains and losses settle every day, which requires the firm to maintain a margin account and meet margin calls when positions move against it.

Futures are cheaper than forwards (no counterparty spread, narrow bid-ask) but less flexible (you must round to standard contract sizes and expiry dates). For commodity hedges, futures are the dominant instrument.

**Options.** A contract giving the holder the right, but not the obligation, to transact at a specified price.

A *call option* gives the right to buy. A *put option* gives the right to sell. The key asymmetry: the holder's downside is capped at the premium paid, while the upside is preserved.

For the firm with the €10M payable: buy a call option to purchase €10M at $1.10/€ in 90 days. If the euro strengthens to $1.18, exercise the option and pay $11M rather than $11.8M — the hedge worked. If the euro weakens to $1.04, let the option expire and buy at spot — the firm pays $10.4M plus the premium, which is less than the locked-in forward rate. The firm keeps the benefit of favorable moves while being protected against unfavorable ones.

The cost: the premium, paid upfront. Typically 1–5% of notional value, depending on volatility and time to expiration. Options are more expensive than forwards for the same exposure, because they don't require the hedger to give up favorable outcomes. When the firm has an option-shaped underlying exposure — a contingent obligation, an M&A deal subject to regulatory approval — options are the right instrument. When the exposure is definite, forwards or futures are cheaper.

<!-- → [CHART: payoff diagram comparing forward vs. option hedge for a euro payable — x-axis: euro/dollar spot rate at maturity; y-axis: dollar cost of the payable; two lines — the forward (flat horizontal, locked in at the forward rate) and the option hedge (flat at the strike rate for adverse moves, declining for favorable moves, offset by the premium); student should see exactly what is given up and what is preserved with each instrument] -->

**Swaps.** An agreement to exchange one cash flow stream for another over a defined period. The most common: interest rate swaps.

A firm with floating-rate debt faces uncertainty about future interest payments — which is fine if the firm's revenues are also floating (they move together), but dangerous if revenues are fixed while debt service varies. By entering a swap with a bank — receiving floating payments and making fixed payments — the firm converts its floating-rate obligation to a fixed one. The bank takes the other side, effectively extending fixed-rate credit to the floating-rate borrower.

Interest rate swaps are also used to exploit comparative advantage in credit markets. A AAA-rated firm can borrow at 5% fixed or LIBOR + 0.25% floating. A BBB firm can borrow at 6.75% fixed or LIBOR + 0.75% floating. The spread in fixed markets (1.75%) exceeds the spread in floating (0.50%) — so the BBB firm has a comparative disadvantage in fixed. If the AAA firm prefers floating and the BBB firm prefers fixed, they can each borrow in their area of comparative advantage and swap. Both end up at a lower effective rate than if they'd borrowed directly in their preferred market. The credit-rating arbitrage is shared between them.

Currency swaps work similarly — firms swap principal and interest streams in different currencies, often to match the currency profile of their assets and revenues.

---

## Enterprise risk management: the whole picture

Individual hedges address individual exposures. **Enterprise risk management (ERM)** is the discipline of viewing the firm's risk profile as a whole — identifying every material risk, deciding how much of each to accept, and designing a coherent response.

The foundational tool is the **risk register**: a documented inventory of the firm's material risks, organized by category, with estimated likelihood and magnitude, current mitigation, and residual exposure after mitigation.

| Risk | Likelihood | Magnitude | Current mitigation | Residual |
|---|---|---|---|---|
| Commodity price spike | High | $200M annually | Futures covering 60% of volume, 12-month horizon | $80M if 40% of volume exposed |
| Euro depreciation | Medium | $50M per 10% move | Forward contracts covering 6 months | Near-zero short-term; 12-24 months exposed |
| Key-customer credit default | Low | $30M per event | Credit monitoring, invoice insurance | $10M excess exposure |
| Cybersecurity breach | Medium | $100M+ | Insurance, redundant systems, incident response | $40M estimated uninsured exposure |

The risk register is not a compliance document — or rather, it shouldn't be. It's an operational tool for deciding where to allocate hedging budget and operational-risk-management attention. A firm that has done this analysis well can answer a simple question: of all the things that could go wrong, which ones matter most, and what are we doing about them?

**Risk appetite** is the quantitative complement. The board sets the maximum loss the firm is willing to sustain in any given period — from each category and in total. Everything else follows from that. Hedging programs, credit limits, liquidity reserves, insurance coverage — all of it calibrates against the risk appetite.

Where risk management fails, it almost always fails at one of two places. Either the firm's stated risk appetite doesn't match its actual behavior (Lehman Brothers had risk policies; they were overridden by profit incentives). Or the firm faced risks that weren't in the register — things nobody modeled because they hadn't happened before.

**Value at Risk (VaR)** is the standard quantitative metric for financial portfolios: it estimates the maximum expected loss over a period at a specified confidence level. A 1-day, 99% VaR of $50M means the firm expects to lose more than $50M in one day only 1% of the time. The metric is widely used and widely criticized.

The criticism is serious. VaR tells you nothing about what happens in the 1% — the tail beyond the threshold can be catastrophic, and VaR doesn't measure it. The 2008 crisis was, among other things, a moment when VaR-based risk management failed systemically: models calibrated on the quiescent 2003–2006 period dramatically underestimated tail risk in correlated, illiquid markets. The lesson: supplement VaR with stress testing and scenario analysis that explicitly models the distribution's tails.

<!-- → [INFOGRAPHIC: risk register template for a hypothetical firm — rows for each of 6-7 major risk categories; columns for description, likelihood (low/medium/high), magnitude ($), current mitigation, residual exposure; one row partially filled as example; caption: the point of the register is deciding where to allocate hedging attention, not compliance] -->

---

## The book's final move

Twenty chapters. They started with the observation that finance is the study of trade-offs over time under uncertainty. Time value of money handled the time dimension. Statistics and CAPM handled the uncertainty. NPV and DCF handled the trade-offs.

Risk management closes the loop. Every cash flow projection we built in Chapter 18 might not materialize. Every discount rate from Chapter 14 rests on a beta that might shift. Every capital structure in Chapter 17 might prove fragile under a scenario the model didn't include. Risk management is the explicit acknowledgment that models are approximations and that real firms face real shocks.

The deepest lesson isn't in any hedging formula. It's this: the risks that destroy firms are usually not the ones they modeled carefully. They're the ones nobody saw coming — a pandemic, a cyberattack, a regulatory shock, a competitor with a genuinely better product, a financial structure that looked safe under normal conditions and collapsed under stress. The honest framework for thinking about risk isn't "build a more comprehensive model." It's "build enough financial cushion to survive shocks the model didn't predict, cultivate enough operational flexibility to adapt, and resist the false confidence that comes from tightly-modeled risk metrics."

The book ends here. The work doesn't.

---

## Exercises

### Warm-up

**20.1** Define hedging and speculation. Use the same derivative contract — a euro forward — to construct one example of each. What makes them different if the instrument is identical?
*(Tests: the hedging vs. speculation distinction and its basis in whether an underlying exposure exists)*

**20.2** Name the five major risk categories from the chapter. For each, give one specific real-world example (not from the chapter) and state whether the risk is primarily addressable through financial instruments or through operational controls.
*(Tests: risk taxonomy and the boundary between hedgeable and non-hedgeable exposure)*

**20.3** Explain why hedging can increase firm value even though it doesn't change expected cash flows. Trace the mechanism through the valuation formula.
*(Tests: the discount-rate channel connecting volatility reduction to firm value)*

### Application

**20.4** A US pharmaceutical firm expects to receive £20M from UK product sales in 180 days. The current spot rate is $1.26/£. The 180-day forward rate is $1.25/£. A put option on £20M at strike $1.25/£ carries a premium of $0.03/£.

(a) If the firm hedges with a forward, what dollar proceeds does it lock in?
(b) If the firm hedges with a put option, what is the minimum dollar proceeds? The maximum?
(c) If at maturity the spot rate is $1.18/£, which hedge — forward or option — produces higher dollar proceeds? By how much?
(d) If at maturity the spot rate is $1.31/£, which hedge produces higher dollar proceeds? Why?
(e) Under what circumstances is the option the better hedge, and what does it cost to have that flexibility?

*(Tests: forward vs. option payoff structure, with specific scenarios and the cost-of-flexibility trade-off)*

**20.5** A BBB-rated firm has floating-rate debt at SOFR + 1.2% and wants to convert to fixed-rate. An AAA-rated firm has fixed-rate debt at 4.8% and wants floating. The BBB firm could borrow fixed directly at 6.4%; the AAA firm could borrow floating at SOFR + 0.3%.

(a) Compute the total interest-rate spread if each firm borrows in its own preferred market vs. borrows in its comparative-advantage market and swaps.
(b) If the arbitrage gain is split equally, what effective rate does each firm pay after the swap?
(c) Why does the comparative advantage in credit markets arise, and who captures it in a fairly negotiated swap?

*(Tests: interest rate swap mechanics and comparative-advantage credit arbitrage)*

**20.6** For your chosen company, locate the "Quantitative and Qualitative Disclosures About Market Risk" section of its most recent 10-K (Item 7A). Identify: (a) which financial risks the firm says it faces; (b) what instruments it uses to hedge them; (c) the notional value of any outstanding derivatives. Assess whether the disclosure is specific enough to understand the firm's actual risk position, or whether it is generic and uninformative.
*(Tests: primary-source risk disclosure reading and assessment of disclosure quality)*

### Synthesis

**20.7** Southwest Airlines became famous in the early 2000s for aggressive jet-fuel hedging, which gave it a cost advantage when prices spiked. By 2014–2016, when jet-fuel prices fell sharply, the same hedge book created substantial losses relative to unhedged competitors.

(a) Explain why the hedge that was profitable in 2004–2008 produced losses in 2014–2016. Draw the payoff diagram.
(b) Was the 2014–2016 result evidence of a bad hedging decision? Construct an argument that it was not, and one that it was.
(c) What does this case teach about how to evaluate a hedging program ex ante vs. ex post?

*(Tests: forward contract payoffs under different price scenarios, and the analytical discipline of separating decision quality from outcome quality)*

**20.8** Build a simplified risk register for your chosen company with at least five entries. For each risk: name it, estimate likelihood (low/medium/high) and magnitude ($ range), describe the firm's current mitigation approach (from 10-K disclosures or management commentary), and estimate residual exposure. For one risk where the current mitigation appears insufficient, recommend a specific additional action and justify it.

This exercise produces the risk section of your final equity research report.

*(Tests: primary-source risk identification and assessment, and the synthesis skill of recommending action)*

### Challenge

**20.9** A firm has a €50M annual payable (raw material costs) and €30M annual receivable (European sales), both in euros. The net euro exposure is a €20M annual payable.

(a) The CFO argues: "Our euro revenues offset our euro costs — we're naturally hedged on 60% of the payable." Evaluate this argument. Is the CFO right, and does the €20M residual need to be hedged?
(b) If the firm decides to hedge the €20M residual with forward contracts and options (splitting the hedge 50/50 between the two instruments), construct the complete hedge position and compute the maximum and minimum dollar cost of the hedged payable.
(c) The risk manager notes that the €30M in receivables and the €50M in payables don't always arrive in the same months — the receivables are seasonally concentrated in Q4, the payables are spread evenly. How does this timing mismatch affect the natural-hedge argument, and what instrument would best address it?

*(Tests: natural hedge analysis, residual exposure identification, instrument selection under timing complexity)*

**20.10** Pick one of the following corporate failures: Lehman Brothers (2008), MF Global (2011), Wirecard (2020), FTX (2022), or Silicon Valley Bank (2023).

(a) Identify the 2–3 most consequential risk-management failures that led to the collapse.
(b) For each failure: was it a failure to *identify* the risk, a failure to *measure* it accurately, a failure to *mitigate* it, or a failure of *governance* (the risk was known but ignored or overridden)?
(c) For each failure type: what specific risk-management practice — risk register, VaR supplement, stress test, board-level oversight, position limits — would have been most likely to prevent it?
(d) Having identified the failures, make a general claim: do corporate risk-management failures tend to be failures of *tools* (we didn't have the right instruments) or failures of *incentives and governance* (we had the tools but didn't use them)? Defend your claim with evidence from your case.

*(Tests: real-world risk failure analysis, the taxonomy of risk-management breakdowns, and the deeper question of whether better tools or better governance is the binding constraint)*

---

## What would change my mind

The chapter argues that hedging financial exposures adds value when the cost of the hedge is less than the discount-rate benefit of reduced volatility, and that enterprise risk management is the right framework for viewing the firm's risk profile holistically. The reading would have to revise if (a) empirical evidence accumulated showing that active hedging programs systematically destroyed value net of costs — the evidence is mixed but generally supportive — or (b) ERM frameworks consistently failed to identify the risks that actually materialized. The 2008 crisis and subsequent failures (SVB, FTX) do suggest that formal ERM can become compliance theater when it's detached from the actual distribution of outcomes. The framework is right; the execution is often wrong.

## Still puzzling

The hardest unresolved question: how do you manage risks you don't know about? Every model, every register, every VaR calculation addresses risks that have been identified and quantified. The risks that destroy firms are typically the ones nobody saw coming — Taleb's Black Swans. The 2008 crisis was one. COVID-19 was one. Each had elements that conventional risk-modeling systematically underweighted. The honest response isn't a better model; it's structural robustness — enough excess capital, enough operational flexibility, enough diversification — to survive outcomes the model doesn't contain. The book ends, appropriately, on a note of humility about what we don't know.

---

## Connections forward

This is the book's last chapter. The substantive arc closes here. What remains is the equity research project — the full report integrating everything built across twenty chapters — and the practice of finance itself: the lifelong discipline of treating uncertainty seriously, reasoning honestly about trade-offs, and building recommendations on evidence rather than on the desire to have a clean answer.

---

## LLM Exercise — Chapter 20: Risk Register and the Final Report

**Project:** Equity Research Report on a Chosen Public Company
**What you're building this chapter:** A complete risk register for your company, plus the synthesis that pulls together everything from prior chapters into the final equity research report.
**Tool:** Claude Project.

### The Prompt — Part A: Risk Register

```
For [your company], using the most recent 10-K's risk-factor section and your accumulated analysis from prior chapters:

1. **List the 5-7 most material risks** the firm faces. For each:
   - Description (1 sentence)
   - Likelihood (low / medium / high) — qualitative
   - Magnitude (estimated $ impact if it materializes)
   - Current mitigation (insurance, hedging, operational redundancy, etc.)
   - Residual exposure after mitigation

2. **Risk categories to consider**:
   - Strategic (competition, technology disruption)
   - Financial (commodity, currency, interest rate, credit)
   - Operational (supply chain, IT, key people)
   - Compliance (regulatory, legal, tax)
   - Reputational (brand, ESG, social)

3. **Hedging program assessment** — From the 10-K's risk-factor and quantitative-and-qualitative-disclosures sections:
   - What financial risks does the firm hedge?
   - Which instruments (forwards, futures, swaps, options)?
   - Does the disclosure suggest active management or token compliance?

4. **Recommendations** — For 1-2 risks where the firm's current mitigation seems insufficient, what would you recommend? Be specific about what additional hedging or operational change would address it.

Show your work.
```

### The Prompt — Part B: Final Equity Research Report Synthesis

```
For [your company], using all materials produced across Chapters 00 through 20, synthesize a complete equity research report with the following structure:

### 1. Executive Summary (1 page)
- Investment thesis (3 sentences)
- Recommendation (Buy/Hold/Sell)
- Price target (with range)
- Key catalysts and risks

### 2. Business Overview (1 page)
- What the firm does, how it makes money, competitive position
- (From Chapter 00 snapshot, refined)

### 3. Industry and Macro Context (1 page)
- Industry dynamics
- Macro exposure (rates, currency, cycle)
- (From Chapter 3 macro section)

### 4. Financial Analysis (3-4 pages)
- The four statements summary (Chapter 5)
- Ratio analysis with trends and peer comparison (Chapter 6)
- Capital allocation track record (Chapter 16)

### 5. Valuation (3-4 pages)
- DCF model with assumptions explicit (Chapters 11, 17, 18)
- Multiples comparison (Chapter 11)
- DDM if applicable (Chapter 8)
- Triangulation across methods → fair value range

### 6. Risk Assessment (1-2 pages)
- Risk register (this chapter, Part A)
- Working capital and liquidity (Chapter 19)
- Hedging program

### 7. Investment Conclusion (1 page)
- Bull case scenario
- Bear case scenario
- Base case price target
- Recommendation justified

This is the project's final deliverable — typically 12-18 pages. Use clear headers, bullet points, and tables. Cite specific sources for every claim.
```

### What this produces

The complete equity research report. This is the final deliverable of the entire course.

### How to adapt this prompt

- *For your own company:* Replace [your company].
- *For ChatGPT / Gemini:* Identical.

### Connection to previous chapters

Synthesizes everything. Every chapter has contributed.

### End of project

This is the project's last LLM Exercise. The remaining work is your editing, refinement, and ownership of the final report.

---

**Tags:** risk-management, hedging, forwards, futures, options, swaps, enterprise-risk-management, VaR

---

## AI Wayback Machine

**Daniel Kahneman** was the psychologist whose Prospect Theory reshaped how the field thinks about risk perception — Nobel 2002.

**Run this:**

```
Who is Daniel Kahneman, and how does their work connect to risk management we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about their career or ideas.
```

→ Search **"Daniel Kahneman"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to apply Daniel Kahneman's framework to a specific finance question.
- Add a constraint: "Answer including criticisms or limits of Daniel Kahneman's framework."

What changes? What gets better? What gets worse?
