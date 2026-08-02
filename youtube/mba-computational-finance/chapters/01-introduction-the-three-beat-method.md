# Chapter 1 — The Three-Beat Method

## TL;DR

- The spreadsheet used to enforce the discipline.
- The chapter moves through The Problem Maya Has on a Friday Afternoon, Beat One: Write Down What You Want Before You Ask for It, Beat Two: Read the Output Like an Editor, Not a Reader, Beat Three: Verify by Independent Means, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

*The spreadsheet used to enforce the discipline. Now you have to.*

I want to start with a confession about how I first used language models for analytical work.

I would sit down, open the chat window, and start typing. Ask the model to analyze something — a stock, a portfolio, a valuation — and it would produce a response with numbers and tables and confident prose. The numbers looked reasonable. The prose sounded authoritative. I would read through it, decide it looked right, and use it.

It was usually wrong. Not catastrophically wrong. Wrong in the small, precise way that ruins a memo when the person across the table knows the subject better than you do — a convention used inconsistently, a window that didn't cover the period that mattered, a Sharpe ratio computed one way being compared to a Sharpe ratio computed another way. The kind of wrong that makes you look like you understood the surface of the analysis but not what's underneath.

The fix, when I finally found it, was embarrassingly simple. A workflow. Three moves, always in the same order, non-skippable. Everything else in this book is those three moves applied to harder problems. I'm going to teach them to you here using one real problem, worked all the way through.

---

## The Problem Maya Has on a Friday Afternoon

It is Friday afternoon. Maya is a second-year MBA student — three core finance courses behind her, a summer banking internship in the rear-view mirror. Her phone vibrates. It is her old boss.

> Quick one. We have $2M in the reserve fund earning nothing. The CIO wants to put it in NVDA for 18 months. He's asked me to put together a one-page analysis. Can you take a first crack? No rush — just need it Monday morning.

She has a laptop, a coffee, and roughly 64 hours.

What she does next is the chapter.

---

## Beat One: Write Down What You Want Before You Ask for It

Maya does not open Claude. She opens a blank text file.

This is the move. This specific, small, slightly counterintuitive move — writing down what you want *before* you ask for it — is the single most important thing in this chapter. I want to explain why, because it sounds like obvious advice, and if it were obvious it would not need to be said. The fact that it needs to be said every time suggests something is actively working against the habit.

Here is the mechanical reason. A language model is a system that completes patterns of text. When you give it a prompt, it does not sit back and ask itself what you really meant. It picks the direction that looks most like a plausible continuation of what it has seen so far. If your prompt is precise, the model works in the direction you intended. If your prompt is vague, the model still picks a direction — you just don't get to choose which one. The specification is how you stop that selection from happening without you.

Here is the practical reason. The failure mode I described at the top of this chapter — analysis that looks right but isn't — almost always traces back to a prompt that didn't specify what it actually needed. The output answers the question the model thought it was being asked, not the question the analyst needed answered. By the time you notice, you've spent two hours going the wrong direction.

The specification has five elements. Let me give you each one, and the reason it matters.

| Element | What it forces you to decide | What goes wrong if omitted |
|---|---|---|
| **The Decision** | The specific action under consideration — buy, hold, sell, hedge, refuse | Without it, the analysis serves no one — every output sounds equally relevant |
| **The Alternative** | What you would do *instead* if the recommendation is *no* | Without it, the recommendation cannot be evaluated against opportunity cost |
| **The Data Window** | The exact period the analysis covers (e.g., monthly returns, Jan 2015 – Dec 2024) | Without it, comparable numbers across sources silently disagree about what they're comparing |
| **The Assumptions** | The premises the recommendation rests on — discount rate, growth rate, base rate, time horizon | Without them, the analysis cannot be stress-tested or audited |
| **The Output Shape** | The format of the deliverable — one-page memo, deck, table, executive summary | Without it, the work is sized wrong for the audience and gets re-done downstream |

**The decision.** Not "is NVDA good." A specific decision: should $2M go into NVDA for 18 months? A dollar amount, a specific instrument, a specific horizon. If you can't name the decision precisely, you don't yet know what you're analyzing.

**The alternative.** This is the element people most commonly omit, and its absence makes the analysis meaningless. "Should we invest in NVDA?" is not a real question. "Should we invest in NVDA *instead of leaving the cash in a money market fund yielding 4.5%*?" is a real question. The comparison is part of the specification or it isn't built in at all.

**The data window.** Not "recent price history." Thirty-six months daily. Five years monthly. The window is a decision, and it matters — a Sharpe ratio calculated over a window that excludes the 2022 drawdown tells you something different from one that includes it. Name it before the model picks it for you.

**The assumptions.** No rebalancing. No leverage. Dividends reinvested or not. Write these down not because they are right — some of them will turn out to be wrong — but because writing them down makes them visible. Future you, looking at the analysis six months later, needs to be able to see what was assumed. The hostile reader needs to be able to challenge the assumptions. You cannot challenge what was never recorded.

**The output shape.** A one-page memo. A table with four columns. An answer in one sentence followed by supporting evidence. If you don't name the shape, the model will pick one, and it will often be the wrong shape for what you're about to use it for.

Here is what Maya actually wrote:

> *I'm putting together a one-page analysis of whether to put $2M of company reserve money into NVDA stock for 18 months. I need: NVDA's price history (36 months daily), volatility, comparison to SPY, and the headline risks. The alternative is a money market fund yielding 4.5% — that's the hurdle rate. Holding period 18 months, no rebalancing, no leverage. Output is a one-page memo that ends with a question for the CIO, not a recommendation.*

Eighty words. Seven minutes. Every one of the five elements is in there. This spec will save her an hour of rework over the weekend, and — more importantly — it will produce an analysis that actually answers the question the CIO asked, because Maya made herself think carefully about what the question actually was before she typed a single prompt.

The thing the specification costs is a feeling. It feels like procrastination. Your hands are on the keyboard and you are deliberately not typing yet. Everything in you wants to start. The discipline is to not start until you've written the spec.

---

## Beat Two: Read the Output Like an Editor, Not a Reader

Maya opens Claude. Her first prompt follows the specification closely: pull NVDA daily closing prices for the last 36 months, calculate annualized return, annualized volatility, max drawdown, and Sharpe ratio at a 4.5% risk-free rate, do the same for SPY for comparison, show your work.

The model responds with a table. With unverified numbers temporarily annotated as `[verify]`:

| Metric | NVDA | SPY |
|---|---:|---:|
| Annualized return | [verify] 78% | [verify] 14% |
| Annualized volatility | [verify] 52% | [verify] 14% |
| Max drawdown | [verify] −57% | [verify] −25% |
| Sharpe ratio ($R_f$ = 4.5%) | [verify] 1.41 | [verify] 0.68 |

Now comes the second beat. The failure mode here is so common it has a name in the human factors literature: *automation complacency*. You ask the machine for an answer, the machine produces something that looks like an answer, and you move on. The discipline of the second beat is to read the model's output the way an editor reads a draft — not the way a reader reads a finished book. A reader absorbs. An editor challenges.

Let me show you what adversarial reading looks like on this specific table.

Does the table answer the specification? The spec asked for 36-month daily, both tickers, four specific metrics, with the work shown. The table has all four metrics for both tickers. The work is partially shown in the body of the response. Maya notes the "partially" and will return to it.

Do the numbers pass a bounds check? Start with the 78% annualized return on NVDA. Can that be right?

Back-of-envelope: if NVDA roughly quadrupled over three years — which is in the right ballpark for the 2021–2024 period — then the geometric annualized return would be $4^{1/3} - 1 \approx 0.587$, or about 59%. But 78% is not 59%. Stop.

The gap between 78% and 59% is about 19 percentage points. Is there a mechanism that explains this? Yes. The 78% is almost certainly the *arithmetic average* of annualized returns, not the geometric compound return. For a volatile asset, these two numbers diverge substantially — the gap is approximately $\sigma^2 / 2$, where $\sigma$ is the annualized volatility. With $\sigma = 0.52$, the gap is roughly $0.52^2 / 2 \approx 0.135$, or 13.5 percentage points. Check: geometric return ≈ 78% − 13.5% ≈ 64.5%. Close to our 59% estimate, and the remaining gap is explained by the fact that NVDA's trajectory wasn't smooth — it experienced periods of much more than 4× before the drawdown brought it back down.

![Arithmetic vs](images/01-introduction-the-three-beat-method-fig-01.png)
*Figure 1.1 — Arithmetic vs*

The 78% is not wrong. It is using a convention — arithmetic rather than geometric annualization — that the table doesn't name. This matters because if the CIO is mentally comparing NVDA's 78% to SPY's geometric return from somewhere else, the comparison is broken. Maya flags this in her notes and will specify it explicitly in the memo.

This is a successful Beat 2 read. She didn't catch a fabrication. She caught a *convention ambiguity* — a different and equally dangerous error. Convention ambiguities don't announce themselves. They hide inside plausible-looking numbers and only surface when a hostile reader in a meeting asks the right question.

Maya reprompts: *For each number above, tell me the exact start and end dates of the window, whether you used adjusted closing prices, the annualization convention (252 trading days vs. 365 calendar days), and whether the return figure is arithmetic or geometric.*

This follow-up is part of Beat 2, not a separate beat. Beat 2 is iterative. You read, find the ambiguity, close it, read again. You stop when the output actually answers the spec as written — not as interpreted, not as implied, but as written.

---

## Beat Three: Verify by Independent Means

Maya has her table and her convention notes. The temptation is to write the prose, format the memo, send it Saturday morning. She doesn't. She opens a new browser tab and pastes the prompt into ChatGPT. Then a third tab into Gemini. Then she opens Yahoo Finance. This is Beat Three.

The foundational principle of verification is this: **you check by independent means**. If the claim came from Claude, you do not verify it by asking Claude again. If the claim came from a model, you do not verify it by asking a different model and stopping there. You use the cross-check to catch model-specific errors; you use primary sources to catch errors that are common across models.

Here is what Maya finds.

ChatGPT returns: annualized return 81%, volatility 54%, drawdown −56%, Sharpe 1.44. Gemini returns: annualized return 76%, volatility 50%, drawdown approximately −57%, Sharpe approximately 1.38.

The spread across three models: return 76–81%, volatility 50–54%, drawdown −56% to −57%, Sharpe 1.38–1.44.

| Metric | Claude | ChatGPT | Gemini | Spread |
|---|---|---|---|---|
| **Annualized return** | 78% | 76% | 81% | 5 pp |
| **Volatility** | 53% | 51% | 49% | 4 pp |
| **Max drawdown** | -56% | -54% | -58% | 4 pp |
| ***Sharpe ratio*** | **1.41** | **1.46** | **1.62** | **0.21** |

*The Sharpe-ratio row is the substantive disagreement. Returns and volatility differ cosmetically (3–5%, mostly rounding and window choice). The Sharpe ratio differs by 15% — large enough to flip a recommendation. Verifying which model used which risk-free rate, which lookback window, and which return frequency is the load-bearing work.*

Now notice what the spread tells you. The qualitative story these three tables tell is identical: NVDA dramatically outperformed SPY on raw return, paid for that outperformance with dramatically higher volatility and drawdown, and came out with a Sharpe ratio roughly twice SPY's. The numbers disagree by a few percentage points — different window edges, slightly different annualization conventions, different handling of dividend adjustments. But the *conclusion* survives all three models, unchanged.

This is what robust cross-model agreement looks like. Not identical numbers — identical conclusions. If Claude had returned a Sharpe of 1.4 and ChatGPT had returned 0.6, that would be a real disagreement requiring investigation before anything goes in a memo. Disagreement is data. Agreement is evidence. The distinction between cosmetic and substantive disagreement is a judgment you develop over time, and we'll return to it.

Now the primary source check. Maya opens Yahoo Finance, NVDA, three-year chart. She's not trying to read off exact numbers — a chart isn't precise enough for that. She's doing a different kind of check: can the chart *rule out* the model's numbers as obviously wrong?

The chart shows a peak in late 2021, a trough in October 2022, and a sustained rally through 2024. From peak to trough, the price fell to roughly 40% of its peak — a drawdown of approximately 60%. The model says −57%. The chart is consistent with that. If the model had said the max drawdown was −15%, the chart would immediately rule it out. It doesn't. Pass.

Total return over the window: the chart shows NVDA ending at roughly 4× its starting point. This is consistent with a 76–81% arithmetic-annualized return given the variance drag we computed earlier. Pass.

Maya writes up her verification log:

```
Verification log — NVDA analysis
—
Cross-LLM: Claude / ChatGPT / Gemini
  - Return spread: 76–81% (arithmetic annualized)
  - Volatility spread: 50–54% annualized
  - Drawdown: −56% to −57%
  - Sharpe spread: 1.38–1.44
  - Qualitative story: consistent across all three
  - Disagreements: cosmetic (convention / window edge)
Bounds-check: Yahoo Finance 3yr chart
  - Drawdown ~−60% (chart) vs. −57% (model) — within bounds
  - Total return ~4x (chart) — consistent with 76–81% arith. annualized
Open issues:
  - Arithmetic vs. geometric convention — flagged, to note in memo
```

This log is the audit trail. Every claim in the memo that goes to the CIO on Monday has a corresponding line here. If someone challenges a number, Maya can show exactly how it was produced, how it was checked, and what was flagged as uncertain.

---

## What Gets Written

Maya's final prompt: *Draft a one-page memo to a senior banking executive. Do not recommend buying or selling — end with the question the CIO should ask before deciding. Use the numbers above, note that returns are arithmetic-annualized. Under 400 words. Include a one-line risk note about the 2023–2024 AI rally potentially inflating recent Sharpe estimates.*

The model produces a draft. Maya edits it — three changes: she removes a piece of jargon, adds one explicit sentence about the AI rally, and changes one generic phrase to name the firm's actual situation. The memo ends: *What is the firm's tolerance for sitting through a drawdown of 30–50% without selling? That is the actual decision.*

She saves the memo. She also saves the spec, the prompts, the three model responses, the Yahoo Finance screenshot, and the verification log. Total time: just under three hours.

---

## What the Substrate Used to Do for You

I want to step back and explain what the three-beat method is actually doing, because it looks like a set of procedural rules and it is something more than that.

The old substrate for finance analysis was the spreadsheet. Excel, for forty years. The spreadsheet enforced certain disciplines as side effects of its own limitations — you had to name your cells, trace your formulas, build your scenario tabs, because the spreadsheet couldn't explain itself. The discipline lived in the artifact. You could open someone else's spreadsheet and audit it.

The conversational substrate removes those constraints. The model explains its own logic. It produces finished-looking outputs that don't have a formula bar you can click. It doesn't show you a named range; it shows you prose. And prose triggers a different cognitive mode than formulas do. You read prose the way you read a book. You do not audit prose the way you audit a spreadsheet.

![Two-column comparison ](images/01-introduction-the-three-beat-method-fig-02.png)
*Figure 1.2 — Two-column comparison *

What the three-beat method does is reimpose the discipline that the substrate no longer enforces automatically. Beat 1 — the specification — is what the named range used to do: make the assumption explicit, visible, challengeable. Beat 2 — reading like an editor — is what the formula trace used to do: verify that the computation did what you think it did. Beat 3 — verification by independent means — is what the scenario tab used to do: confirm the answer makes sense against an independent reference.

The moves are old. The reason they need to be taught explicitly is new: the substrate that used to enforce them by necessity no longer does.

If you do the three beats, you have analysis — something another person can audit, challenge, and act on. If you skip a beat, you have a guess that sounds like analysis. The memo looks the same either way. The difference only surfaces when someone in the meeting knows the subject well enough to ask the right question.

That difference is the whole book.

---

## What Would Change My Mind

The strong claim here is that the three-beat method is non-skippable — that trying to shortcut any of the three beats produces work that is unreliable in a systematic way. I would revise this claim if careful empirical study showed that experienced analysts using AI tools without explicit Beat-1 specification produced work as defensible as analysts using the full workflow. As of late 2025, no such study exists in the published literature [verify]. The argument is empirical, forward-looking, and provisional.

The weaker claim — that the workflow helps, that it catches errors, that it produces better auditable artifacts — is harder to argue against. Every spectacular AI failure that has been documented publicly in legal, journalistic, and financial contexts has involved a skipped Beat 3. The lawyer who cited fake cases did not verify. The news outlet that published the invented interview did not verify. The pattern is consistent.

---

## Still Puzzling

The cross-LLM comparison in Beat 3 is a useful technique, but I don't have a clean rule for when cross-LLM *disagreement* signals a real error versus a defensible difference of convention. In this chapter, the arithmetic-vs.-geometric distinction was a clear case — cosmetic once you understood what each model was computing. In later chapters the disagreements get harder to classify. Different models pull from different data sources, apply different cleaning rules, use different reference dates for the risk-free rate. The disagreement can be cosmetic (a one-basis-point rounding difference) or substantive (one model has a data error in its training set for this ticker during this period).

The honest answer is that classification requires judgment you build over many verification cycles. You start recognizing the signature of cosmetic disagreements versus substantive ones. Chapter 11's confidence interval framework is the closest formal treatment this book offers. It isn't the complete answer.

---

*Coming up.* Maya wrote "annualized return" and "volatility" in her memo without specifying which version of either she meant. There are several versions of each, and they give different numbers. We caught the arithmetic-vs.-geometric gap in this chapter because we were looking for it. Chapter 2 is about building the habit of always looking: geometric versus arithmetic returns, log returns versus simple returns, the conventions for annualizing each, and how to make sure the number in your memo means the same thing as the number in the document it gets compared to.

---

## Exercises

**Warm-up**

1. *(Beat 1 — specification elements)* A colleague hands you this prompt they're about to send to an AI: *"What's the best ETF to buy right now?"* Identify which of the five specification elements are missing, and rewrite the prompt so all five are present.

2. *(Beat 2 — bounds checking)* A model tells you that a mutual fund returned 22% annualized over five years. The fund's NAV went from $10.00 to $18.50 over that period. Without a calculator, explain whether 22% is plausible, too high, or too low — and show the back-of-envelope reasoning.

3. *(Beat 3 — verification logic)* You run the same prompt on three models. Model A returns a max drawdown of −34%, Model B returns −36%, Model C returns −51%. Which disagreement is likely cosmetic and which is potentially substantive? What would you do next?

**Application**

4. *(Full three-beat workflow)* You've been asked whether $500K should be moved from a savings account (yielding 4.2%) into a 60/40 portfolio of VTI and BND for a two-year horizon. Write a complete Beat 1 specification for this analysis — all five elements, in the format Maya used. Do not run the analysis; just write the spec.

5. *(Beat 2 — convention hunting)* A model returns the following for a bond fund: *"Annualized return: 6.8%, Yield: 5.1%, Duration: 7.2 years."* List at least three convention ambiguities that a Beat 2 editorial read should flag before this table goes into a memo.

6. *(Beat 3 — audit trail)* Using the verification log format from this chapter, construct a blank template an analyst could fill in for any three-model cross-check. Your template should have labeled fields for each element Maya recorded, plus a field she omitted that you think should be standard.

7. *(Beat 1 — the alternative)* Explain in two or three sentences why omitting "the alternative" from a specification doesn't just weaken the analysis — it makes the analysis unanswerable in principle. Use a concrete example different from the NVDA case.

**Synthesis**

8. *(All three beats — failure mode mapping)* The chapter describes three failure modes: vague prompt → wrong direction (Beat 1 skipped); automation complacency → convention error undetected (Beat 2 skipped); no independent check → fabrication or data error undetected (Beat 3 skipped). For each failure mode, describe a realistic professional scenario — outside of finance — where that specific skip would cause a consequential mistake.

9. *(Substrate argument)* The chapter argues that spreadsheets enforced analytical discipline as a side effect of their limitations, and that conversational AI removes those guardrails. Identify one other technology transition in knowledge work (not AI, not spreadsheets) where a new tool removed a discipline that an older tool enforced by necessity. What did practitioners have to do explicitly that the old tool had done automatically?

**Challenge**

10. *(Stress-test the method)* The three-beat method assumes you have time to write a spec, iterate on output, and run cross-model verification. Describe a realistic professional scenario where all three constraints are genuinely unavailable — tight deadline, single model access, no primary source within reach. In that scenario, which beat is least skippable, and what is the minimum viable version of it? Argue for your answer.

---

###  LLM Exercise — Chapter 1: The Three-Beat Method

**Project:** Maya's Memo, Built Across the Course
**What you're building this chapter:** The position you will analyze across the next twelve chapters, plus a one-paragraph brief and an explicit three-beat plan for the work ahead.
**Tool:** Claude Project

---

**The Prompt:**

```
I'm starting a project that will run across the next twelve chapters of *Computational Finance with AI* by Nik Bear Brown. The book teaches the **three-beat method** — *idea, execute, verify* — as the discipline for producing analytical work with an AI tool that does not collapse into plausible-but-wrong output.

Across the chapters I am going to build one complete investment memo on a single real position. Help me set up Chapter 1's deliverable. Paste the position below; if I haven't yet, ask.

Produce four things, in order:

1. **The position, named precisely.** One paragraph. The actor (me / a hypothetical fund / Sara's small business buyer / etc.); the instrument (specific ticker, specific fund, specific bond, specific small business); the action under consideration (buy / size up / hedge / refuse); the time horizon; the constraint (capital available, mandate, personal liquidity).

2. **The three-beat plan.** Three sentences:
   - **Idea**: what is the question this memo has to answer?
   - **Execute**: what analytical tools will I bring to bear (preview the chapters that will produce them)?
   - **Verify**: what would a hostile reader ask, and what would I want in writing to defend the recommendation?

3. **The five layers.** The capstone (Ch 13) integrates five layers: return measurement, valuation, portfolio fit, capital allocation, financial-statement quality. For my specific position, write one sentence per layer naming what *this* layer must answer.

4. **The "what would change my mind" sentence.** One sentence. The specific evidence that would move my recommendation from buy to hold, or hold to sell. This is the verify-step's anchor.

Format the output as a markdown document I can save as `01-position-brief.md`. Be honest about uncertainty in the time horizon and the constraint — pick numbers I'd defend in a meeting, not numbers that sound impressive.
```

---

**What this produces:** A markdown document `01-position-brief.md` containing the precise position, the three-beat plan, the five-layer outline, and the what-would-change-my-mind sentence. This document is the seed for every subsequent chapter's exercise.

**How to adapt this prompt:**

- *For your own project:* Replace any bracketed domain placeholder with your specific instrument, ticker, or context. The exercise structure is instrument-agnostic; the content is yours.
- *For ChatGPT / Gemini:* Works as-is. For ChatGPT, save the running memo to a Custom GPT instead of a Claude Project. For Gemini, paste the project's accumulated section files into the context window each session.
- *For Claude Code:* Not the right tool yet. Save this as plain markdown.
- *For a Claude Project:* Create a Claude Project named *Maya's Memo — [position ticker / name]*. Put the three-beat method definition in the system prompt plus the rule: *every output is a section that fits into a final 6–10 page memo*. Each subsequent chapter's exercise becomes a new conversation in this project.

**Connection to previous chapters:** First chapter — no prior exercise to build on. The position chosen here governs every subsequent exercise; pick something real you actually want a defensible answer on.

**Preview of next chapter:** Chapter 2 takes your position and produces the *return and risk profile* section of the memo — arithmetic vs. geometric returns, volatility, and the Sharpe ratio with the period and frequency stated.

---

##  AI Wayback Machine
The ideas in this chapter didn't appear from nowhere. **Lillian Gilbreth** was decomposing every white-collar task into a sequence of named, observable, repeatable motions decades before most people had heard of the workflow discipline — idea, execute, verify. Here's a prompt to find out more — and then make it better.

![Lillian Gilbreth, c. 1920s. AI-generated portrait based on a public domain photograph (Wikimedia Commons).](images/lillian-gilbreth.jpg)
*Lillian Gilbreth, c. 1920s. AI-generated portrait based on a public domain photograph.*

**Run this:**

```
Who was Lillian Gilbreth, and how does her industrial-engineering practice of breaking work into named, observable steps connect to the three-beat method (idea → execute → verify) the chapter teaches as the central discipline for analytical work with AI? Keep it to three paragraphs. End with the single most surprising thing about her career or ideas.
```

→ Search **"Lillian Moller Gilbreth"** on Wikipedia after you run this. See what the model got right, got wrong, or left out.

**Now make the prompt better.** Try one of these:

- Ask it to explain *therbligs* in plain language, as if you've never read a time-and-motion study
- Ask it to compare Gilbreth's hand-decomposition of a kitchen task to the three-beat decomposition of a financial analysis
- Add a constraint: "Answer as if you're writing the introduction to a chapter on workflow discipline for analytical AI work"

What changes? What gets better? What gets worse?
