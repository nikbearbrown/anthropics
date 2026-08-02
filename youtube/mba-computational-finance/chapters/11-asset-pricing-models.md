# Chapter 11 — Asset Pricing Models


## TL;DR

- To say a stock was exceptional, you need a baseline.
- The chapter moves through Warm-up, Application, Synthesis, Challenge, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

*To say a stock was exceptional, you need a baseline. Without one, "exceptional" and "lucky" are indistinguishable.*

---

Here is a question that sounds easy but isn't.

Last year, NVDA returned something in the neighborhood of 240%. The S&P 500 returned something in the neighborhood of 24%. Was NVDA exceptional, or was it just lucky?

Most people's answer is: exceptional. NVDA dominated AI infrastructure. The product was right, the timing was right, the financial results were right.

I want to push on that. Because "exceptional" turns out to be a word that sounds meaningful but conceals a serious problem the moment you try to make it precise. To say NVDA was exceptional, you need a baseline. You need to know what NVDA *should* have returned — not in hindsight, not by storytelling, but by some principled calculation derived from NVDA's risk profile. Without that baseline, "exceptional" and "lucky" are logically indistinguishable. They feel different. They aren't.

The Capital Asset Pricing Model is the tool for establishing that baseline. The chapter is about building the model from scratch, using it on a real problem, and being honest about what it can and cannot tell you.

---

Before the model, we need to clear something up about what risk actually is in this context.

Suppose you hold a single stock — NVDA, say — and nothing else. Every time the market sneezes, NVDA reacts. But NVDA also reacts to things that have nothing to do with the market: a product announcement, a competitor's chip, a CEO's interview. Your total anxiety as a shareholder comes from two places simultaneously.

Now suppose instead of one stock you hold five hundred stocks, approximately equally weighted. The idiosyncratic stuff — the product announcements, the earnings surprises — averages out across the portfolio. One company has a great product launch; another has a terrible quarter. They offset. What doesn't average out is the part that moves everything together: broad market sentiment, economic cycles, recessions, interest rate changes. This component can't be diversified away. It's present in every stock because it's driven by forces that affect all stocks.

![Two-panel diagram showing one stock decomposed into market plus idiosyncratic components, and a 500-stock portfolio where the idiosyncratic vectors cancel and only the market component remains](images/11-asset-pricing-models-fig-01.png)
*Figure 11.1 — Idiosyncratic risk cancels in a portfolio; market risk does not*

This is the conceptual foundation of the whole model: diversifiable risk doesn't get paid for, because a rational investor will diversify it away. The only risk a market of rational investors will compensate you for bearing is the risk you can't get rid of — the part that moves in step with the whole market.

This claim is contested. Empirically, idiosyncratic risk does get compensated in some periods and asset classes, which is part of why more complex models exist. But the core intuition survives the complications: risk that's diversifiable is cheap, and markets price assets based on the risk that's not.

---

Given that intuition, what you need is a single number that captures how much of any individual stock's behavior is tied to the market as a whole.

That number is beta. It's defined as the slope of the line you get when you plot the stock's returns against the market's returns over some historical window. If the market goes up 1% on a typical day, a stock with beta = 1.5 tends to go up 1.5%. When the market goes down 1%, that stock tends to go down 1.5%. Beta is a measure of systematic sensitivity — how tightly the stock's behavior is coupled to the market's.

Beta is not the same as volatility. A biotech stock awaiting a drug trial result might swing 15% on a single afternoon, but if those swings are driven by trial outcomes rather than market movements, its beta can be low. The volatility is there, but it's idiosyncratic; it doesn't move with the market. Conversely, a less volatile large-cap financial might have a high beta because its movements, though modest in size, are tightly coupled to the market cycle.

Beta is also not fixed. A company that becomes more leveraged, enters new markets, or gets pulled into a speculative wave will have a different beta than it did before. The number you estimate from history is a backward-looking summary, and using it as a forward-looking input requires judgment about how stable the underlying business has been.

---

The Capital Asset Pricing Model assembles these ideas into a formula.

$$E(R_i) = R_f + \beta_i \cdot (E(R_m) - R_f)$$

Read it left to right. $E(R_i)$ is the expected return on the asset you're pricing. $R_f$ is the risk-free rate — what you'd earn holding T-bills, the floor of any expected return. $\beta_i$ is the asset's beta. $E(R_m) - R_f$ is the equity risk premium — the extra return investors demand for holding a broad equity portfolio rather than T-bills.

The equity risk premium is not a precise number. It's estimated, typically by looking at long-run historical averages or by deriving it from current market prices and expected earnings. Practitioners commonly use something in the range of 4–7%, and they disagree about which end of that range is right. I'll use 6% as a round working estimate in the middle of the reasonable range.

![Security market line ](images/11-asset-pricing-models-fig-01.png)
*Figure 11.1 — Security market line *

The model says: your expected return is the risk-free rate plus beta times the equity risk premium. A stock with beta = 1 earns the market return, by definition. A stock with beta = 1.5 earns 1.5 times the premium above the risk-free rate. A stock with beta = 0 earns the risk-free rate — it has no market exposure.

This is surprisingly elegant. One number — beta — determines the required return, given a risk-free rate and an equity risk premium that apply equally to all assets. The whole model reduces to: how much are you buying into the market?

---

Knowing that beta is a regression slope doesn't tell you which regression to run. Three choices matter, and each produces a different answer.

Frequency: daily, weekly, or monthly returns? Monthly is the conventional choice for CAPM work, partly because monthly returns are less contaminated by intraday noise and partly because it's the standard in the academic literature that developed the framework. Daily data gives more observations but more noise.

Window length: how many months back? A 36-month window gives you 36 data points — enough to estimate a slope but not very precise. A 60-month window gives more precision but assumes the company hasn't fundamentally changed over five years. For NVDA, which went from graphics cards to AI infrastructure during the relevant period, a 60-month window mixes two different business profiles. Shorter is more relevant; noisier. Longer is more stable; possibly stale.

Market proxy: the S&P 500 is the standard choice for US large-caps. For most US large-cap stocks the choice of proxy barely matters.

None of these is objectively correct. They're engineering decisions. You should check your conclusions against multiple window lengths. If the answer changes dramatically when you switch from 36 to 60 months, that instability is itself important information.

---

Let's actually run the numbers.

Three regressions: 36-month, 24-month, and 60-month windows, all using monthly returns against the S&P 500. The results, which should be verified against primary data, come out approximately as follows.

![Three regression scatter plots of NVDA monthly returns vs. S&P 500 monthly returns, one per window, each showing the regression line...](images/11-asset-pricing-models-fig-01.png)
*Figure 11.1 — Three regression scatter plots of NVDA monthly returns vs*

| Window | Beta | 95% CI | R² | CAPM Expected Return | Actual Return | Alpha |
|--------|-----:|--------|---:|---------------------:|--------------:|------:|
| 36 months | 1.65 | [1.20, 2.10] | 0.62 | ~14.4% | ~78% | ~64% |
| 24 months | 1.85 | [1.30, 2.40] | 0.55 | ~15.6% | ~95% | ~79% |
| 60 months | 1.45 | [1.10, 1.80] | 0.60 | ~13.2% | ~49% | ~36% |

*All figures are approximate and should be verified. Beta estimates are illustrative of the methodology.*

![Bar chart with three grouped bars ](images/11-asset-pricing-models-fig-02.png)
*Figure 11.2 — Bar chart with three grouped bars *

Now look at this table slowly, because it contains several distinct lessons.

The first lesson is that beta is unstable. The 24-month estimate (1.85) and the 60-month estimate (1.45) are meaningfully different. The confidence intervals overlap, so they're not statistically distinguishable — but the shift is real in economic terms. A stock with beta 1.85 requires roughly 15.6% annual return in CAPM's framework; a stock with beta 1.45 requires only 13.2%. That 2.4-percentage-point gap matters for valuation. The instability is consistent with NVDA's transformation: higher systematic risk exposure as AI became a market-wide theme.

The second lesson is that the confidence intervals are wide. The 36-month estimate of 1.65 comes with a 95% interval of [1.20, 2.10] — a range of 0.90 in beta units. Anyone who reports "NVDA's beta is 1.65" without that range is reporting false precision. If your decision is sensitive to whether the true beta is 1.2 versus 2.1, you have a decision that depends on an estimate you can't make precisely enough to support it.

The third lesson is what R² tells you. An R² of 0.62 means that about 62% of NVDA's monthly return variation is explained by its co-movement with the market. The remaining 38% comes from somewhere else — idiosyncratic factors, AI hype cycles, specific product releases, competitive dynamics. CAPM has captured the majority of NVDA's risk, but a significant minority is running on its own logic.

The fourth lesson is the most important: the alphas are enormous. The CAPM-predicted return over the 36-month window is roughly 14.4% annualized. NVDA's actual return over that window was roughly 78% annualized. The gap — approximately 64 percentage points — is what the model calls alpha: return unexplained by market exposure.

This is the answer to the question we started with. NVDA's alpha was massive. Whether that represents exceptional management (genuinely superior decisions about AI investment) or exceptional luck (the AI wave arrived when NVDA happened to have the right products) or some combination is a question CAPM cannot answer. The model tells you the alpha was large. It cannot partition the alpha into luck and skill. That requires a different kind of analysis — and ultimately involves uncertainty that doesn't reduce to math.

---

I want to be careful here, because this is where bad CAPM teaching becomes dangerous.

The model rests on assumptions: markets are efficient, investors have homogeneous expectations, there are no taxes or transaction costs, investors can borrow and lend at the risk-free rate without limits. Every one of these is false.

The question is whether "false" means "useless." It doesn't, necessarily. In physics, you can calculate the trajectory of a cannonball by ignoring air resistance. The answer is wrong, but it's useful — it gets you to the right field, it tells you how high to aim, it gives you a starting point. Air resistance is a correction. CAPM works the same way: beta explains a real and meaningful fraction of stock return variation, and the model provides a principled starting point for expected return calculations even though it misses factors that matter.

What you cannot do is mistake the starting point for the complete answer.

Three situations where the model's limitations become critical. When idiosyncratic risk is actually being compensated — there are asset classes and time periods where idiosyncratic risk earns positive expected return, and CAPM says this can't happen, but it does. When beta is genuinely unstable — for companies undergoing fundamental transformation, the historical beta is almost certainly the wrong beta for the future, and NVDA during the AI transition is exactly this case. And when you're evaluating individual stocks rather than portfolios — CAPM is a model of expected returns, and for any individual stock over any finite period the realized return can differ from the expected return enormously, driven by idiosyncratic factors the model explicitly excludes. The model's predictions get accurate only in expectation, over many stocks, over long periods. For a single stock over three years, the model's prediction is a reference point, not a forecast.

---

The empirical challenges to CAPM aren't new. Beginning in the 1970s, researchers found systematic patterns the model couldn't explain.

Small-cap stocks outperformed large-caps more than their betas implied. Stocks with low price-to-book ratios outperformed growth stocks. Stocks that had outperformed over the past year continued to outperform over the next year, at rates inconsistent with their betas. These patterns — the size premium, the value premium, the momentum premium — are documented across enough markets and enough time periods to be taken seriously.

| Factor | What it captures | Approximate historical premium (annualized) | Data source / citation |
|---|---|---|---|
| **Market (CAPM)** | Excess return of the market portfolio over the risk-free rate | ~6–7% (1928–2024) | Damodaran NYU dataset; CRSP; *Sharpe (1964)*, *Lintner (1965)* |
| **SMB — size** | Small-cap excess return over large-cap | ~2–3% | Ken French Data Library; *Fama-French (1993)* |
| **HML — value** | High book-to-market (value) excess return over low (growth) | ~4–5% | Ken French Data Library; *Fama-French (1993)* |
| **UMD — momentum** | Past-year winners excess return over past-year losers | ~8–10% (with high turnover) | Ken French Data Library; *Carhart (1997)* |
| **RMW — profitability** | High operating profitability excess return over low | ~3% | Ken French Data Library; *Fama-French (2015)* |

*CAPM is one row in a family of compensated risk factors. A position whose return is fully explained by market + size + value + momentum + profitability has no alpha — the return came from factor exposure, which is available cheaply via factor ETFs.*

The Fama-French three-factor model responded by adding size and value as factors alongside the market. A four-factor model adds momentum. More recent work adds profitability and investment patterns. These models have more explanatory power than CAPM. They also require estimating more betas — one per factor — and making assumptions about each factor's expected premium that are no more certain than CAPM's equity risk premium. More sophisticated is not always better in practice; it's better when the additional complexity captures real variation in expected returns, and worse when it adds noise to noise.

The lesson from multifactor models is not that you should always use them. It's that CAPM's single factor is not the full picture, and that certain types of portfolios — value stocks, small-caps, momentum strategies — are better analyzed through a multifactor lens.

---

Let me come back to the question we started with, and give it a proper answer.

NVDA's beta of roughly 1.65 over the 36-month window implies an expected return of about 14.4%. NVDA delivered roughly 78%. The 64-percentage-point gap is real, it's large, and it substantially exceeds what you'd plausibly explain through estimation error in the beta.

What CAPM cannot tell you is whether the alpha was predictable in advance. If you'd held NVDA three years ago, reasoning that AI infrastructure was going to explode, you'd look prescient in hindsight. But the question isn't whether you can construct a narrative after the fact — it's whether the expected return, conditional on available information at the time, justified the position. CAPM says the market-risk-adjusted expected return was 14.4%. If you believed in a substantially higher expected return from specific NVDA factors, you were making an idiosyncratic bet — one that paid off magnificently, but was idiosyncratic.

CAPM's job is to tell you what the market was paying you for bearing systematic risk. What it cannot tell you is whether the remaining return — the alpha — was earned or given.

That gap is not a failure of the model. It's the honest limit of what any single-factor model can do. A lot of finance theory exists to narrow that gap. None of it closes it completely. And the professor's original question — exceptional or lucky? — still doesn't have a clean answer.

CAPM narrows the question precisely. That's what good models do. They don't eliminate uncertainty; they tell you where the uncertainty actually lives.

---

*A note on what the chapter simplified.* The cost of capital that appears in DCF models throughout corporate finance is built partly from CAPM estimates of equity beta. When a company evaluates whether to build a new factory, the discount rate applied to projected cash flows encodes a beta estimate, a risk-free rate, and an equity risk premium. The imprecision in beta is real — the confidence intervals are wide, the estimates are window-dependent, and the appropriate premium is debated — but CAPM's disciplined structure produces estimates that are more defensible than guessing. The alternative to an imperfect model is not a perfect model. It's an undisciplined judgment call with no audit trail. That's the practical case for learning CAPM even after you've seen its failure modes.*

---

## Exercises

### Warm-up

**1.** A stock has beta = 1.3. The current risk-free rate is 4.5% and the equity risk premium is 6%. What is CAPM's predicted expected return for this stock? If the stock actually returned 22% last year, what was its alpha? *(Tests: basic CAPM formula application; computing alpha as the gap between actual and predicted return.)*

**2.** Stock A has beta = 0.7 and volatility of 35%. Stock B has beta = 1.4 and volatility of 20%. Which stock does CAPM predict will have a higher expected return, and why? What does the comparison tell you about the relationship between total volatility and CAPM-required return? *(Tests: beta vs. volatility distinction; idiosyncratic vs. systematic risk.)*

**3.** Explain in plain language what R² means in the context of a CAPM regression. If NVDA's 36-month regression has R² = 0.62, what does the remaining 0.38 represent economically? What kinds of events would show up in that 0.38? *(Tests: interpreting regression R² as a risk decomposition; connecting the statistic to the systematic/idiosyncratic split.)*

---

### Application

**4.** You are given the following data for two stocks over a 36-month window: Stock X has estimated beta = 1.2 with a 95% CI of [0.85, 1.55]; Stock Y has estimated beta = 1.2 with a 95% CI of [1.10, 1.30]. Both point estimates are identical. Explain why you should have different levels of confidence in the two estimates, and describe how the width of each confidence interval should affect decisions that depend on the beta estimate. *(Tests: statistical precision of beta estimates; connecting confidence intervals to decision-making under uncertainty.)*

**5.** An analyst uses a 60-month beta estimate for a company that completed a major leveraged buyout 18 months ago. The buyout substantially increased the company's debt load and therefore its financial risk. Explain why the 60-month beta is likely to be a poor estimate for the company's current systematic risk, and describe what approach you would use instead. What does this case reveal about the tradeoff between window length and estimate relevance? *(Tests: beta instability; regime changes and their implications for historical estimation windows.)*

**6.** A portfolio manager claims her fund generated alpha of 8% last year against the S&P 500. You know the fund holds primarily small-cap value stocks. Using the Fama-French framework as your reference, explain why the single-factor CAPM alpha of 8% may overstate the manager's true skill. What additional factor exposures would you want to control for before concluding the alpha reflects genuine outperformance? *(Tests: CAPM vs. multifactor models; size and value premiums as alternative explanations for apparent alpha.)*

---

### Synthesis

**7.** The chapter argues that CAPM's assumption violations don't make it useless — they make it a starting point that requires correction, like calculating a cannonball's trajectory while ignoring air resistance. Evaluate this analogy carefully. In what ways is it apt? In what ways does it break down? Are there conditions under which CAPM's assumptions are so badly violated that the model provides no useful starting point at all? *(Tests: critical evaluation of model assumptions; integrates the cannonball analogy with the three failure modes.)*

**8.** NVDA's 36-month alpha is approximately 64 percentage points. The chapter says CAPM cannot partition this alpha into luck and skill. Describe what additional evidence or analysis you would want in order to make a judgment about how much of the alpha was skill-based. What would constitute strong evidence for skill? What would constitute evidence for luck? Is there any amount or type of evidence that would allow you to be certain? *(Tests: the luck-vs-skill problem; pushes the student to specify what "exceptional" would actually require to prove.)*

**9.** The chapter presents three engineering choices in estimating beta — frequency, window length, and market proxy — and notes that none is objectively correct. A colleague proposes always using whichever combination of choices produces the highest R². Critique this approach. What incentive problem does it create? What does selecting for R² likely produce in terms of the beta estimate's usefulness for forward-looking decisions? *(Tests: specification choices and their integrity; overfitting and its consequences for model-based decisions.)*

---

### Challenge

**10.** The Security Market Line plots expected return against beta for all assets. In a world where CAPM holds exactly, all assets lie on the line. In the real world, small-cap value stocks have historically plotted above the line (higher return than their beta predicts), and low-volatility stocks have also historically plotted above the line. These two anomalies suggest different stories. For each: describe what it implies about what CAPM is missing, and explain whether the anomaly is better interpreted as (a) a risk premium CAPM doesn't capture, (b) a persistent mispricing, or (c) a statistical artifact. What would each interpretation imply for how you should trade? *(Tests: the SML anomalies as competing explanations; connects CAPM's empirical failures to the multifactor literature and to the active-vs-passive investment debate.)*

**11.** The chapter closes by saying CAPM cannot answer whether NVDA's alpha was earned or given — and that this gap is not a failure of the model but the honest limit of what any single-factor model can do. An adversarial reader might push back: if no model can reliably partition alpha into luck and skill even in hindsight, what exactly is the practical value of computing alpha at all? Write a response to this critique. When is a large measured alpha informative, and when is it not? What would have to be true for alpha persistence across multiple periods to constitute evidence of skill rather than luck? *(Tests: the epistemological status of alpha; stress-tests the chapter's core claim about what CAPM is and isn't for.)*

---

###  LLM Exercise — Chapter 11: Asset Pricing Models

**Project:** Maya's Memo, Built Across the Course
**What you're building this chapter:** The CAPM and Factor Read section of the memo: was the position's return exceptional (alpha) or lucky (beta-driven)? Decompose into systematic factor exposures.
**Tool:** Claude Code

---

**The Prompt:**

```
I'm working on Maya's Memo. The diversification decomposition (Ch 8) and the frontier (Ch 9) are in the project.

Chapter 11 taught:
- **CAPM**: $E[r] = r_f + \beta (E[r_m] - r_f)$ — beta is the only systematic-risk number that should be priced
- **Alpha** as the residual: the part of the return CAPM cannot explain
- **Multi-factor extensions** — Fama-French 3-factor (market, size, value) and 5-factor (adds profitability and investment)
- The exceptional-vs-lucky question

Scaffold `analysis/11-asset-pricing.py`:

1. **Estimate β against the market.** Regress the position's monthly excess returns on the market's monthly excess returns. Report β, α, R^2, the standard error on β, and the p-value on α.

2. **The CAPM expected return.** Plug β into the CAPM formula. Compare to the position's *realized* return. The difference is α. State whether α is statistically distinguishable from zero.

3. **Three-factor decomposition.** Regress excess return on the three Fama-French factors (Market, SMB, HML). Report the loadings and the resulting α. Has the alpha shrunk relative to the CAPM single-factor regression? If yes, the position's return was partly explained by size and value factors that CAPM ignored.

4. **Five-factor decomposition.** Run again with profitability (RMW) and investment (CMA) added. Report and compare.

5. **The exceptional-vs-lucky verdict.** One paragraph. Was the realized return *exceptional* (statistically significant alpha after factor controls), *lucky* (alpha collapses once you control for factor exposure), or *systematic with a tilt* (significant factor loadings, no residual alpha)?

6. **Save `analysis/11-asset-pricing.md`** with the four regression results, the verdict paragraph, and the implication: a position with high alpha post-controls deserves single-name exposure; a position whose return is fully factor-explained should be replaced by the cheapest factor ETFs.

Run with `python analysis/11-asset-pricing.py --ticker [TICKER]`.
```

---

**What this produces:** A runnable script `analysis/11-asset-pricing.py` plus `analysis/11-asset-pricing.md` containing CAPM β and α, the three- and five-factor decompositions, the verdict on exceptional-vs-lucky, and the implication for direct ownership.

**How to adapt this prompt:**

- *For your own project:* Replace any bracketed domain placeholder with your specific instrument, ticker, or context. The exercise structure is instrument-agnostic; the content is yours.
- *For ChatGPT / Gemini:* Works as-is. For ChatGPT, save the running memo to a Custom GPT instead of a Claude Project. For Gemini, paste the project's accumulated section files into the context window each session.
- *For Claude Code:* Right tool — Fama-French factor data is downloadable from Ken French's website; `pandas-datareader` handles it. Claude Code can scaffold the full pipeline.
- *For a Claude Project:* Append to the project. The verdict here either reinforces or undermines the case for direct ownership made in Chapter 4 — flag the contradiction if it appears.

**Connection to previous chapters:** Chapter 9 placed the position on the frontier; Chapter 11 asks whether its historical return came from skill, luck, or factor tilts.

**Preview of next chapter:** Chapter 12 produces the *financial-statement diligence* section — pulling the actual numbers from the 10-K to test whether the position's case rests on facts or on hype.

---

##  AI Wayback Machine
The ideas in this chapter didn't appear from nowhere. **John Lintner** was co-developing the Capital Asset Pricing Model in 1965 — independently of Sharpe, with a slightly different derivation that arrived at the same equilibrium result and shaped the way institutional investors would price risk for the next half-century decades before most people had heard of the CAPM, beta, and the multi-factor extensions that followed. Here's a prompt to find out more — and then make it better.

![John Lintner, c. 1960s. AI-generated portrait based on a public domain photograph (Wikimedia Commons).](images/john-lintner.jpg)
*John Lintner, c. 1960s. AI-generated portrait based on a public domain photograph.*

**Run this:**

```
Who was John Lintner, and how does his independent 1965 derivation of the CAPM — published in *The Review of Economics and Statistics* months before Sharpe's better-known paper appeared — connect to the chapter's treatment of beta, market risk premium, and multi-factor extensions? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.
```

→ Search **"John Lintner"** on Wikipedia after you run this. See what the model got right, got wrong, or left out.

**Now make the prompt better.** Try one of these:

- Ask it to explain *systematic vs. idiosyncratic risk* in plain language, as if you've never seen beta
- Ask it to compare Lintner's 1965 derivation to Sharpe's 1964 paper — what was at stake in the difference
- Add a constraint: "Answer as if you're writing the historical preface to a CAPM chapter"

What changes? What gets better? What gets worse?

## Prompts

Use these prompts with Claude to generate interactive D3 v7 versions of the
figures in this chapter. Each produces a standalone HTML file you can open
in a browser and modify freely.

**Prerequisites:** Load `brutalist/CLAUDE.md` and `brutalist/DESIGN.md` into
your Claude project context before using these prompts. They define the stack,
naming conventions, color system, and typography the figures use.

---

### Figure 11.1 — Three regression scatter plots of NVDA monthly returns vs

Create a standalone D3 v7 HTML figure for "Three regression scatter plots of NVDA monthly returns vs". Use a horizontal bar chart with 5 labeled categories with approximate values from 0 to 100. Marks: bars or rectangular panels, direct labels, and concise value labels. Channels: position for sequence or category, length for quantitative emphasis when bars are used, color for the primary highlighted item only, and direct text labels for accessibility. Use a zero baseline for quantitative bars. Include title, desc, role="img", aria-labelledby, ResizeObserver redraw, dark mode CSS variables, and reduced-motion safeguards. Deliver as one HTML file with inline CSS and the D3 7.9.0 CDN.

> Reference implementation: `d3/11-asset-pricing-models-fig-01.html`
