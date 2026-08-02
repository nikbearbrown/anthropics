# Chapter 20 — Risk Management and the Financial Manager

**Suggested titles**
1. Hedging, Speculation, and Knowing the Difference
2. The Financial Toolbox for Uncertainty
3. The Risks Firms Choose and the Risks They Cannot Avoid

**TL;DR.** Every firm faces risk — commodity price swings, exchange rate moves, interest rate changes, counterparty defaults, operational shocks. Risk management is the discipline of identifying which risks the firm bears, deciding which to keep and which to lay off, and choosing the right instruments to hedge the ones it lays off. The hedging tools (forwards, futures, options, swaps) trade upside for protection. Used well, they reduce variance without sacrificing expected return — but used poorly, they're expensive insurance for risks the firm should have taken anyway.

---

## The puzzle of $500 million per year

In spring 2018, the price of jet fuel rose from $2.07 to $2.19 per gallon. Twelve cents — roughly 5.8% — of fuel-cost increase. American Airlines consumes about 4 billion gallons per year. The fuel-price move translated into roughly $500 million of additional annual operating cost.

Jet fuel costs are about 25% of an airline's total operating expenses. A 5.8% increase in fuel feeds directly to a roughly 1.5% increase in total cost — at industry margins where 5-7% operating margins are typical, this kind of increase can move a profitable airline into a quarter of losses.

Some airlines hedge fuel costs aggressively. Southwest Airlines was famous in the 2000s for hedging jet fuel through futures contracts and other derivatives, allowing it to lock in below-market prices during fuel spikes. Other airlines hedge less, accepting fuel-price exposure as the cost of doing business. Both approaches are defensible.

The question this chapter answers: how does a financial manager decide which risks to hedge, and which instruments to use? What's the cost of hedging vs. the cost of leaving the risk on the firm's balance sheet?

For your equity research project, this is the final analytical layer. A complete equity research report includes a risk assessment: what risks does the firm face, how is it managing them, and what does that say about the firm's resilience? The deliverable from this chapter is the risk section of your final report.

This chapter is also the book's last. We've built up from time value of money (Chapter 7) through valuation (Chapter 11) through capital structure (Chapter 17) to forecasting (Chapter 18) to working capital (Chapter 19). Risk management is where everything ties together — because every assumption you've made depends on the firm being able to execute.

---

## Learning objectives

After working through this chapter, you should be able to:

- Distinguish hedging from speculation and explain why competent firms do both selectively.
- Identify the major risk types: commodity price, exchange rate (transaction, translation, economic), interest rate, credit/counterparty, operational.
- Use forward, futures, option, and swap contracts to construct hedges.
- Explain how each instrument differs in standardization, counterparty risk, and payoff structure.
- Construct a risk register for a firm and assess the management of each risk.

**Prerequisites.** All previous chapters; the entire book is implicit in this one.

---

## Concept 1 — What risk management actually is

Three definitions worth getting right.

### Risk

In finance, **risk** is uncertainty about future outcomes. Not danger, not just bad outcomes — uncertainty in either direction. A stock with returns ranging from -30% to +50% is *more* risky than a stock with returns ranging from -5% to +10%, because the dispersion is wider, even though the second one's worst-case is also a loss.

Cash flow risk decomposes into several types:

1. **Commodity price risk.** Raw material costs change unpredictably. Starbucks coffee, American jet fuel, automaker steel.
2. **Exchange rate risk.** Currency moves affect costs and revenues for any firm operating across borders. Three flavors (Chapter 3 introduced these): transaction, translation, economic.
3. **Interest rate risk.** Changes in rates affect the cost of debt, the value of fixed-rate assets, and the discount rate the firm uses to evaluate projects.
4. **Credit risk.** Customers may not pay; suppliers may not deliver; counterparties may default.
5. **Operational risk.** Things break — supply chains, IT systems, regulatory environments, key people.

Of the five, the first three are amenable to financial hedging. The latter two are more about operations and process management.

### Why risk affects firm value

Recall from Chapter 1: investors are risk-averse. They demand higher returns for bearing more risk. So a firm with more volatile cash flows has a higher cost of capital, which lowers the present value of its future cash flows, which lowers firm value.

The mechanism is direct:

$$\text{Firm value} = \sum \frac{\text{Expected cash flow}}{(1 + \text{discount rate})^t}$$

Volatile cash flows produce a higher discount rate (the equity premium and credit spreads embed risk compensation). Hedging reduces volatility. Reducing volatility reduces the discount rate. A lower discount rate produces a higher firm value, all else equal.

This is the theoretical case for hedging. The practical question is whether the cost of hedging — the premium paid, the upside given up — exceeds the value created by reducing volatility.

### Hedging vs. speculation

The distinction matters.

**Hedging** is taking an action that reduces existing exposure to risk. A US firm with a euro-denominated payable in 90 days hedges by buying euros forward — locking in the dollar cost. Hedging is loss prevention.

**Speculation** is taking an action that creates new exposure to risk in pursuit of profit. The same firm betting that the dollar will fall against the euro and buying euros forward without an underlying obligation is speculating. Speculation is profit-seeking.

The instruments are often the same (forward contracts, futures, options). The position is different. Hedging and speculation can use identical contracts in opposite directions, and a poorly-supervised hedge desk can drift from hedging into speculation — sometimes catastrophically. Procter & Gamble's $157M derivatives loss in 1994 and Metallgesellschaft's $1.3B 1993 loss were both cases of hedging programs that became speculative.

### When firms should hedge

Not every risk should be hedged. Three considerations:

1. **Is the risk material?** Hedging $5K of currency exposure isn't worth the time. Hedging $500M is.
2. **Does the firm have an information advantage?** A firm that knows its own demand patterns better than the market can sometimes profit by *not* hedging. (This argues against hedging too aggressively.)
3. **Does hedging create a corresponding cost?** Forward contracts have small bid-ask spreads. Options have premiums. The hedging instrument's cost reduces the value created by reducing variance.

For small firms or firms in stable industries, the cost of an active hedging program may exceed its benefits. For large multinationals or firms in volatile commodity markets, hedging is essential.

↳ **Dig Deeper — Black Swans and what risk models miss**

*Nassim Taleb's "Black Swan" framework argues that the most consequential risks are those *not* in the historical dataset and therefore not in the standard risk models. The 2008 crisis, COVID-19, FTX collapse, SVB failure — each had elements that conventional risk-modeling approaches systematically underweighted.*

**Prompt:**
> Summarize Taleb's Black Swan framework from his 2007 book. Then identify three specific recent corporate or financial-system failures (LTCM 1998, Lehman 2008, FTX 2022, SVB 2023, Wirecard 2020) and explain what their conventional risk models missed. Then describe Taleb's proposed responses: anti-fragility, the barbell strategy, building "convex" rather than "concave" exposures. What's a defensible critique of Taleb's approach?

**What to do with the output:** Save it. The book's last chapter wrestles with the limits of formal risk management; this gives you the most-cited critique of where those limits matter.

### The trade-off (concept 1)

Hedging trades **expected return for reduced variance**. A firm that hedges all currency exposure gives up the upside of favorable currency moves but is protected from the downside. A firm that hedges nothing keeps full upside but bears the full downside. Most firms occupy a middle ground — hedging the most material exposures, accepting the rest.

### Common misconceptions

- *"Hedging is always good."* It's expensive. For small or low-volatility risks, the cost may exceed the benefit.
- *"Hedged firms are safer."* They're variance-reduced. They can still fail from operational, strategic, or counterparty risks the hedges don't cover.

---

## Concept 2 — The hedging toolbox

Four instruments dominate financial hedging. Each has its own structure, costs, and use cases.

### Forward contracts

A **forward contract** is a bilateral agreement to exchange a specified asset on a future date at a price set today.

Example: A US firm with a €10M payable in 90 days enters into a forward contract with a bank to buy €10M at $1.10/€ in 90 days. Today's spot rate might be $1.09/€; the forward rate is $1.10/€ (slightly above spot, reflecting the interest-rate differential).

Whatever happens to the spot rate over the next 90 days, the firm pays $11M for the €10M. The exposure is eliminated.

**Structure:** Customizable to any amount and date. Bilateral — the firm and the bank are direct counterparties.

**Cost:** Small bid-ask spread. No upfront premium.

**Risk:** Counterparty default. If the bank fails before maturity, the contract is unenforceable.

**Use case:** Currency hedges for known future flows. Standard for multinationals.

### Futures contracts

A **futures contract** is a standardized exchange-traded forward.

Same example: instead of buying €10M forward from a bank, the firm buys 80 euro futures contracts (each for €125,000, the standard contract size on CME) on the Chicago Mercantile Exchange.

**Structure:** Standardized — fixed contract sizes, fixed expiration dates, fixed underlying. Exchange-traded.

**Cost:** Margin requirement (collateral, often 5-10% of contract value). Daily marking-to-market — gains and losses settle daily.

**Risk:** Essentially no counterparty risk because the exchange clearinghouse stands between buyer and seller.

**Use case:** Standardized hedges where exact dates and amounts are flexible. Particularly common for commodities (oil, wheat, gold, lumber) and major currencies.

The trade-off vs. forwards: futures are cheaper (no counterparty risk, narrower spreads), but less flexible (you can't customize to your exact need).

### Options

An **option** gives the holder the right, but not the obligation, to exchange the asset at a specified price.

Two types:

**Call option:** Right to *buy* at the strike price.
**Put option:** Right to *sell* at the strike price.

For a US firm with an €10M payable in 90 days:

- Buy a call option on €10M at strike $1.10/€, expiring in 90 days.
- If spot rises to $1.15/€, exercise: pay $1.10/€ × €10M = $11M. The hedge worked.
- If spot falls to $1.05/€, let the option expire. Pay the spot rate: $10.5M. The firm pocketed the premium-cost-adjusted savings.

**Cost:** Premium paid upfront. Typically 1-5% of the underlying exposure, depending on volatility and time to expiration.

**Payoff structure:** *Asymmetric* — the buyer's downside is capped at the premium, while the upside is preserved.

**Use case:** Hedging when the firm wants protection against bad outcomes but doesn't want to give up the upside of favorable moves. Common for option-shaped exposures (acquisition contingent on regulatory approval, contingent obligations).

The trade-off vs. forwards/futures: options preserve upside but cost premium. Forwards/futures lock in the price but eliminate both upside and downside.

### Swaps

A **swap** is an agreement to exchange one cash flow stream for another.

The most common: an interest rate swap. Firm A has floating-rate debt; firm B has fixed-rate debt. They swap their interest payments — A now pays fixed, B pays floating. Each party gets the rate type they prefer.

Why does this work? Because firms with different credit ratings have different relative spreads in fixed vs. floating markets. A AAA firm might borrow fixed at 5% but floating at LIBOR + 0.25%. A BBB firm might borrow fixed at 6.75% but floating at LIBOR + 0.75%. The credit spreads aren't equal across rate types — fixed-rate spreads are wider.

If the AAA firm prefers floating and the BBB firm prefers fixed:
- AAA borrows fixed at 5%, then swaps with BBB.
- BBB borrows floating at LIBOR + 0.75%, then swaps with AAA.
- After swap: each firm gets a better rate than they could get directly. The credit-rating arbitrage is shared.

**Cost:** Bilateral negotiation; typically small spreads.

**Use case:** Long-term interest rate hedging, currency swaps for cross-border financing.

### Worked example — Starbucks's coffee hedging

Starbucks consumes large quantities of coffee. Coffee prices are volatile — historically swinging from $0.52 to $3.00 per pound over the past two decades.

A simplified hedge:

1. Estimate annual coffee consumption: 150 million pounds.
2. Buy futures contracts on the IntercontinentalExchange (ICE) for delivery in 6, 12, 18, 24 months.
3. Lock in a portion of next year's coffee at known prices.

If coffee prices spike, the futures gains offset the higher cash purchase costs. If coffee prices fall, the futures losses offset the lower cash purchase savings. Either way, the firm's coffee cost is locked in.

In practice, Starbucks layers in hedges over time and uses options as well as futures. The 10-K's risk-factor section discusses the strategy in some detail.

For your equity research project: read the risk-factor section and note how your chosen company describes its hedging program. A firm that hedges actively and discloses transparently is usually well-managed; a firm that under-discloses hedging activity may be hiding losses or speculating outside its mandate.

↳ **Dig Deeper — When hedging programs become speculation**

*Procter & Gamble lost $157M in 1994 on derivatives that started as hedges and drifted into speculation. Metallgesellschaft lost $1.3B in 1993 in a similar drift. Sumitomo's Yasuo Hamanaka lost $2.6B in copper trading. Each was a case of risk management that became risk creation through poor governance.*

**Prompt:**
> Walk through one major case study (P&G 1994, Metallgesellschaft 1993, or Sumitomo) of a hedging program that drifted into speculation and produced massive losses. For your chosen case: (1) what was the original hedging rationale, (2) how did the position evolve into something different, (3) what governance failures allowed the drift, (4) what specific reforms emerged from the case (e.g., enhanced derivatives disclosure, board-level derivatives oversight committees).

**What to do with the output:** Save it. The lessons of historical hedging failures inform how to assess your project company's current derivatives program.

### The trade-off (concept 2)

Each hedging instrument trades **flexibility against cost and risk**. Forwards are flexible but bilateral. Futures are standardized but cheap and exchange-guaranteed. Options preserve upside but cost premium. Swaps create arbitrage but require finding a counterparty with offsetting needs.

### Common misconceptions

- *"Options are always better than forwards because they preserve upside."* They're more expensive (premium) and can be less efficient if upside isn't valuable.
- *"Hedging eliminates risk."* It transfers risk. If the counterparty fails or the underlying exposure shifts in ways the hedge doesn't track, residual risk remains.

---

## Concept 3 — Enterprise risk management

A complete view of the firm's risk position is more than the sum of the individual hedges. **Enterprise risk management (ERM)** is the discipline of viewing the firm's risk profile holistically.

### The risk register

The first step in ERM is identifying every material risk the firm faces. The result is a **risk register** — a documented list of risks, organized by type:

- **Strategic** — competitive, market-share, technology disruption.
- **Financial** — commodity, currency, interest rate, credit.
- **Operational** — supply chain, IT, key personnel.
- **Compliance** — regulatory, legal, tax.
- **Reputational** — brand damage, social media, ESG.

For each risk, the register documents:
1. **Description** — what could go wrong.
2. **Likelihood** — how often does this happen (annual probability).
3. **Magnitude** — what's the financial impact if it does.
4. **Current mitigation** — what the firm is doing now.
5. **Residual exposure** — what's left after current mitigation.

### Risk appetite

The firm decides how much risk it's willing to accept. This is the **risk appetite**. A bank that's willing to lose 2% of its equity capital in any single year has a different risk appetite than one willing to lose 10%. A pharmaceutical company willing to fund 30 simultaneous drug-development programs has a different risk appetite than one willing to fund 5.

Risk appetite should be quantified, communicated, and periodically reassessed. Major financial-services failures (Barings 1995, Lehman 2008, FTX 2022) often involved firms operating well outside any reasonable interpretation of their stated risk appetites.

### Risk transfer vs. risk acceptance

For each material risk, the firm chooses among four responses:

1. **Avoid** — exit the activity that generates the risk. (Stop selling in a country with high political risk.)
2. **Transfer** — buy insurance, hedge with derivatives, contract risk to a third party.
3. **Mitigate** — reduce the likelihood or magnitude through operational changes.
4. **Accept** — take the risk, factoring it into pricing and capital reserves.

Different risks call for different responses. A small firm doesn't insure every parking-lot bump (accept). A multinational hedges its currency exposure (transfer). A bank limits its loan book to industries it understands (avoid). A retailer adds redundancy to critical IT systems (mitigate).

### Value at Risk

A widely-used quantitative metric: **Value at Risk (VaR)** estimates the maximum likely loss over a specified period at a specified confidence level.

For example: "The firm's 1-day, 99% VaR is $50M" means there's a 1% probability that the firm loses more than $50M in any one day.

VaR is most useful for portfolios of liquid assets where return distributions are well-characterized. It has known limitations: it ignores what happens *beyond* the threshold (the 1% tail can be much larger than the VaR), and it assumes return distributions are stationary (which they aren't in stress).

The 2008 financial crisis was, in part, a moment when VaR-based risk management failed catastrophically. Models calibrated on years of stable data dramatically underestimated tail risk. Lessons learned: supplement VaR with stress testing, scenario analysis, and explicit consideration of regime changes.

### The trade-off (concept 3)

Enterprise risk management trades **comprehensive coverage against analytical effort**. A complete risk register with quantified residual exposures is expensive to maintain. A naive approach (insure everything; hedge everything) is also expensive. The right balance is industry-specific and firm-specific.

### Worked example — risk register for your chosen company

For your equity research project, build a simplified risk register:

1. List the 5-7 most material risks the firm faces (typically the firm's own 10-K risk factors are a starting point).
2. For each, estimate likelihood and magnitude.
3. Identify what the firm is doing to manage it (from the 10-K and other disclosures).
4. Assess whether the management approach seems adequate.

This is the risk section of your final equity research report. Combined with the valuation work from Chapter 11 and the capital allocation analysis from Chapters 16 and 17, it produces a complete investment thesis.

### Common misconceptions

- *"More hedging is always safer."* No — hedges have costs, and over-hedging can be as expensive as under-hedging.
- *"VaR is the answer to risk measurement."* It's an answer; not the answer. Tail risk (CVaR, expected shortfall, stress testing) matters too.

---

## Synthesis — the book's final move

This chapter — and the book it concludes — is about treating uncertainty seriously.

Twenty chapters ago, in Chapter 1, we set up finance as the study of trade-offs over time under uncertainty. Time value of money handled the time dimension. Statistics and CAPM handled the uncertainty dimension. NPV and DCF handled the trade-off dimension. Each chapter added tools.

Risk management closes the loop. The cash flows we project in Chapter 18 might not materialize. The discount rate we use in Chapter 11 might be wrong. The capital structure choices in Chapter 17 might prove unwise. Each piece of analytical machinery is built on assumptions that risk threatens. Risk management is the discipline of acknowledging the threats explicitly and deciding how to respond.

For the equity research project, this chapter equips you to write the final section of your report — the risk assessment. Combined with everything else, the report tells a complete story: what the firm is, what it's worth, what could go wrong, and what to do about it.

The book ends here. The work doesn't.

---

## Exercises

### Warm-up

**20.1** Distinguish hedging from speculation. Give an example of each.

**20.2** Name the five major risk types covered in this chapter and give one real-world example of each.

**20.3** What's the difference between a forward contract and a futures contract?

### Application

**20.4** A US firm has a €5M payable in 90 days. Today's spot rate is $1.08/€. The 90-day forward rate is $1.09/€. The 90-day call option at strike $1.09/€ has a premium of $0.02/€.

(a) If the firm hedges with a forward, what does it pay in 90 days? In dollars?
(b) If the firm hedges with a call option, what's the maximum dollar cost? The minimum?
(c) Under what scenario does the option dominate the forward?

**20.5** A firm has fixed-rate debt at 6% and would prefer floating. Another firm has floating-rate debt at LIBOR + 1% and would prefer fixed. They enter an interest rate swap.

(a) Sketch the cash flows.
(b) If the credit-spread arbitrage is split equally, what's each firm's effective rate?

**20.6** For your chosen company, identify the firm's stated currency exposure (from the 10-K's currency risk discussion) and its hedging approach. Argue whether the firm is hedged appropriately.

### Synthesis

**20.7** A firm is considering whether to hedge its annual coffee purchases. Construct an argument for hedging and an argument against, with explicit cost-benefit reasoning. What additional information would help decide?

**20.8** Build a complete risk register for your chosen company:
(a) List 5-7 material risks.
(b) For each, estimate likelihood (low/medium/high) and magnitude (in dollar terms).
(c) Document the firm's current mitigation approach.
(d) Assess residual exposure.

This becomes the risk section of your final equity research report.

### Challenge

**20.9** Construct a complete equity research report for your chosen company:
(a) Executive summary (1 page).
(b) Business overview (2-3 pages).
(c) Financial analysis from Chapters 5-6 (ratios, statements).
(d) Valuation from Chapter 11 (DCF + multiples + DDM if applicable).
(e) Risk register from Exercise 20.8.
(f) Investment thesis with Buy/Hold/Sell recommendation and price target.

This is the project's final deliverable.

**20.10** Pick a major corporate failure of the last decade (Lehman 2008, MF Global 2011, Wirecard 2020, FTX 2022, SVB 2023, Credit Suisse 2023). Construct an analysis: which risks did the firm fail to manage, and which risk-management failures were most consequential? What does this case teach about the limits of hedging and ERM?

---

## Chapter summary

- **Risk** is uncertainty about future outcomes. Five major types: commodity, currency, interest rate, credit, operational.
- **Hedging** reduces existing risk exposure; **speculation** creates new exposure for profit. Same instruments; different positions.
- **Forward contracts** are bilateral, customized, and have counterparty risk.
- **Futures contracts** are standardized, exchange-traded, and have minimal counterparty risk via marking-to-market.
- **Options** preserve upside while capping downside, in exchange for an upfront premium.
- **Swaps** exchange one cash flow stream for another, often exploiting credit-rating arbitrage.
- **Enterprise risk management** views the firm's risk profile holistically: identify, quantify, decide on response (avoid, transfer, mitigate, accept), monitor.
- **Value at Risk** is a useful but imperfect metric; tail risk and stress testing supplement it.

---

## What would change my mind

The chapter argues that financial hedging is a useful but imperfect tool for managing firm risk, and that enterprise risk management is the right framework for thinking holistically. The reading would have to revise if (a) hedging consistently failed to add value (the empirical record is mixed but generally supportive), or (b) ERM frameworks turned out to be more bureaucratic theater than useful discipline (some critics make this case, particularly after 2008 and 2023 bank failures, but the framework remains the working consensus).

## Still puzzling

The hardest unresolved question is *how to manage the risks you don't know about*. Every model, every framework, every risk register addresses risks the firm has identified. The risks that destroy firms are typically the ones nobody saw coming — Black Swans, in Nassim Taleb's terminology. 2008 was full of these. 2020 was full of these. The honest framework is: build enough financial cushion to survive shocks the model didn't predict; cultivate enough operational flexibility to adapt; resist the false confidence that comes from tightly-modeled risk metrics. The book's final lesson is humility about what we don't know.

---

## Connections forward

This is the book's last chapter. The substantive arc closes here. What remains, for the engaged student, is the work itself — the equity research project, the broader practice of finance, and the lifelong discipline of treating uncertainty seriously.

The next chapter — Chapter 0, **Claude Basics** — is the onboarding to the LLM tools used throughout this book. By design, it's the *first* chapter the reader encounters when picking up the book, but it's the *last* one to be drafted, because it had to know what running project it was introducing.

---

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

**Daniel Kahneman** was psychologist whose Prospect Theory reshaped how the field thinks about risk perception — Nobel 2002.

**Run this:**

```
Who is Daniel Kahneman, and how does their work connect to risk management we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about their career or ideas.
```

→ Search **"Daniel Kahneman"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to apply Daniel Kahneman's framework to a specific finance question.
- Add a constraint: "Answer including criticisms or limits of Daniel Kahneman's framework."

What changes? What gets better? What gets worse?
