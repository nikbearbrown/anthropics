# Chapter 1 — The CFO's First Question
*The hardest part of a calculation is knowing what you're actually calculating.*

![Two-column diagram contrasting the outside-analyst view (public data)](images/01-the-cfos-first-question-fig-01.png)
*Figure 1.1 — Two-column diagram contrasting the outside-analyst view (public data, models, cross-referenced estimates) with the inside-analyst view (live accounts, covenant language, institutional memory).*

---

Here is something your finance education probably didn't tell you, and I want to get it on the table before we go any further.

When you learn to analyze a firm — in an MBA program, from a textbook, from a CFA curriculum — you are learning to look at firms from the outside. You learn to read a 10-K. You learn to build a discounted cash flow model. You learn to calculate a weighted-average cost of capital. You are, implicitly, sitting in the position of an analyst at some investment bank, looking at a company across the street, armed with public data and your models.

That is a real kind of finance. It is useful. The trouble is that there is a second kind — the kind practiced by the people inside the firm, sitting in the CFO's office, with the actual cash position, the actual covenant language, the actual board dynamics — and the two kinds are not the same problem in different clothes. They are genuinely different problems. The confusing part is that the textbook treats them as one thing.

This chapter is about what happens when you fall into the gap between them on your third Tuesday on the job.

---

Maya Chen is a senior analyst at Halverson Industries. At 9:14 AM on a Tuesday, she gets a capital structure assignment: evaluate whether the firm should fund a $50M plant expansion with debt or equity. The CFO needs a memo by Friday. The board meets on the 15th.

Maya has a strong finance education. She can recite the Modigliani-Miller propositions. She can build a DCF. She knows what debt and equity are.

None of that tells her what to write in the memo.

I want to understand *why* none of that tells her what to write, because this is the important question. The gap is not in Maya's technical knowledge. The gap is between the question she learned to answer and the question she's actually been asked. The computation is the easy part. The specification is the hard part, and almost nobody teaches it.

---

The question "should we fund Plant 4 with debt or equity?" sounds like a single question. It isn't. It's doing five different jobs at once, and the job that sounds most obvious — which financing instrument to use — is actually the least interesting of the five.

There's the cost job: debt costs interest, equity costs dilution and expected future returns, so you'd prefer the cheaper one, all else equal. But all else is never equal. The cost depends on Halverson's existing capital structure, the current tax rate, what the credit market is pricing right now, how the equity market feels about Halverson specifically, and how the board feels about issuing shares this quarter. "Which costs less" is not a number you look up. It's a calculation that requires a specific firm, a specific moment, and specific market conditions.

There's the risk job: debt must be repaid on a fixed schedule whether Plant 4 succeeds or not. Equity has no such obligation. If the plant underperforms, equity holders are disappointed; debt holders are in line to be paid regardless. The financing choice changes the risk profile of the entire firm, not just the project.

There's the signaling job: when a public company issues equity, the market tends to read it as the insiders saying "we think our stock is overvalued, so we're selling some." When a company issues debt, the market tends to read it as "we think our future cash flows are strong enough to support fixed payments." The CFO's choice will be interpreted by equity analysts whether she intends a signal or not, and that signal can move the stock price in ways that outlast any news about Plant 4 itself.

There's the flexibility job: a new debt issuance typically comes with covenants — restrictions on additional borrowing, on dividends, on acquisitions. Equity has no covenants but permanently changes the ownership structure. The choice today constrains the option space available tomorrow.

And then, finally, there's the literal job: which instrument? Bank loan, bond offering, equity offering, retained earnings, convertibles? Each has its own execution timeline, transaction costs, investor appetite.

<!-- → [TABLE: five-job decomposition of Maya's assignment — columns: job name, the real question it asks, what data answers it, who inside Halverson owns that data — serves as the structural anchor for the whole chapter's argument that one question hides five] -->

Five jobs. One sentence. Before you can compute anything useful, you have to understand what you're actually being asked. This is the first thing the inside view teaches you.

---

Let me explain the inside/outside gap more carefully, because it matters for everything that follows.

Outside the firm, financial analysis has a clean structure. There is public data — 10-Ks, earnings releases, market prices — and there is your analysis of that data. The data is in EDGAR. You download it, you build your model, you verify that your model produces numbers consistent with what other analysts are reporting. If your WACC is wildly different from the consensus, you check your inputs. The verification process is fundamentally about cross-referencing public information against other public information.

Inside the firm, this breaks down immediately. Halverson's actual cash position isn't in EDGAR — it's in the controller's month-end report, which may not have been distributed yet, and which contains estimates that are themselves subject to revision when the accounts receivable team finishes the collections run. The actual covenant language on the existing revolver isn't in the bond indenture summary on the investor relations page — it's in the full credit agreement on the treasurer's hard drive, and the critical restrictive covenant is in Section 7.4 of an amendment filed in 2021 that nobody has summarized into readable form.

The numbers Maya needs don't exist as numbers yet. They exist as processes, spreadsheets, people, and institutional memory. Getting them requires going to talk to those people in a way that public-market analysis never requires.

This is not a minor inconvenience. It changes the nature of the verification problem entirely. Outside the firm, "verify" means cross-reference public information. Inside the firm, "verify" means find the person who owns the number and understand how they built it. Maya's verification instincts are trained on public data. The data she needs is not public. She is stuck not because she lacks the technical machinery but because she is orienting herself as a spectator when she needs to orient herself as a participant.

---

Now I want to give you the underlying theory, because you need the outline of it before the numbers mean anything.

In 1958, Franco Modigliani and Merton Miller proved something that still feels surprising: in a world without taxes, bankruptcy costs, or information asymmetries, the way a firm finances its assets doesn't affect the firm's total value. If Halverson is worth $500M as an unleveraged firm, it's worth $500M with 50% leverage. The source of the $50M for Plant 4 doesn't change what Plant 4 is worth. The pie — the total value created by the firm's assets — is the same size regardless of how you slice it into debt and equity claims.

![M&M "same pie" visual](images/01-the-cfos-first-question-fig-02.png)
*Figure 1.2 — M&M "same pie" visual: two pie charts of identical size, one sliced into two pieces (debt / equity), one unsliced, with the label "Same value, different claims."*

This is a clean and important result. It is also obviously not a description of the world Halverson operates in. But before we add back all the complications, it's worth sitting with the pure result for a moment, because it tells you something real: the *prima facie* case for caring about capital structure at all has to rest on the ways the world differs from M&M's frictionless world. Taxes. Distress. Information. Those are the three complications, and they account for essentially all of the content in a modern capital structure course.

Halverson's world has taxes. The tax treatment of debt versus equity is not symmetric: interest payments on debt are tax-deductible, while dividend payments and equity returns are not. Every dollar of interest Halverson pays saves the firm some fraction of a dollar in taxes — roughly the tax rate times the dollar of interest. At current federal rates plus state taxes, this is a real annual benefit. The debt option has a tax shield that the equity option doesn't, and the present value of that tax shield is real money. M&M, when they extended their original result to a world with taxes in 1963, found that the tax shield pushes toward 100% debt financing — which is obviously not what firms do, so something must be pushing back.

What's pushing back is the cost of financial distress. If Halverson takes on more debt than its cash flows can reliably support, and those cash flows turn out weaker than expected, the firm faces distress: missed payments, covenant violations, creditor negotiations, potential default. Distress is expensive independently of how it resolves. Lawyers are expensive. Distracted management is expensive. Customers who hear the company is in trouble take their business elsewhere. Suppliers tighten credit terms. The firm can survive distress and still have destroyed substantial value in the process.

So the trade-off is: more debt means more tax shield (good) and more distress risk (bad). The optimal capital structure sits where the marginal benefit of additional tax shield equals the marginal cost of additional distress risk. Where exactly that balance sits depends on the specific firm — how stable its cash flows are, how cyclical its business is, how much debt it already carries, what the credit market is charging right now.

![Trade-off theory curve](images/01-the-cfos-first-question-fig-03.png)
*Figure 1.3 — Trade-off theory curve: firm value on the y-axis, leverage on the x-axis. The curve rises with the tax shield, peaks at the optimal capital structure, then falls as distress costs accumulate.*

<!-- → [INFOGRAPHIC: annotated version of the trade-off curve with callouts for (1) where Halverson currently sits, (2) the direction Plant 4 debt would move them, (3) the distress-cost threshold — makes the abstract curve concrete for this specific firm] -->

For Halverson — an industrial company with relatively stable cash flows and conservative existing leverage — the preliminary case favors debt at this scale. The tax shield is real and the distress risk, at $50M additional leverage on top of a healthy balance sheet, is modest. But "preliminary case" is not a memo. The numbers need to be run.

There is a third complication, and I want to be honest that it doesn't resolve as cleanly as the first two. Managers inside the firm know things about Halverson's prospects that the equity market doesn't know yet. This information asymmetry means that financing choices carry signals. When the CFO chooses debt, the market reads confidence in future cash flows. When she chooses equity, the market reads a signal that management thinks the stock is fully valued or overvalued. The empirics show that equity issuances are often followed by stock price declines. The theory says this is because investors rationally discount the news of an equity offering, inferring management's private information about valuation.

The clean empirical test — separating the signal from the actual news that prompted the financing decision — is difficult. For our purposes, the operational point is this: whatever Maya recommends will be read as a signal by people who follow Halverson, whether or not she intends it that way. This is not a reason to avoid equity. It's a reason to understand that the capital structure decision is partly a communication decision.

---

Here is what the inside method looks like in practice. I'll call it the three-beat method, though the label matters less than the substance.

The first beat is verifying the inputs. Where is each number coming from? Who built it? What assumptions does it rest on? What's its update cadence? This is not a checkbox. When the controller's draft memo says "approximately $12M in interest expense next year," the word "approximately" is doing a lot of work. What is it approximately of? What scenario does it assume? What would change it? At Halverson, getting clean inputs for a Friday memo means making calls by Wednesday, and being explicit in the memo itself about which numbers are confirmed and which are planning-level estimates. A CFO who has been around can tell the difference, and she will trust a memo that makes the uncertainty legible more than she will trust a memo that papers over it.

The second beat is calculating transparently. No black-box outputs. Every number in the memo is one Maya can derive on a single page in front of the CFO, in real time, if asked. This is not about distrust of tools — computational tools can run the sensitivity tables, Excel can run the scenarios — it's about ensuring that Maya understands every step well enough to defend it and fix it when a number turns out to be wrong. The catastrophic memo is the one where the analyst can't explain how they got from input to conclusion. That memo gets stopped.

The third beat is the sanity check. If the WACC comes out at 4%, Maya knows that's wrong before she checks the math, because Halverson's bonds currently trade at a yield above that, and equity holders expect more than the cost of debt. The sanity check is cheap insurance against a catastrophic error. It costs almost nothing and catches the mistakes that matter most — not arithmetic errors but structural errors in the setup.

<!-- → [TABLE: three-beat method as a decision matrix — columns: beat name, the question it answers, what failure looks like at Halverson, what success looks like — parallels the five-job table above and gives students a compact reference for both frameworks] -->

These three beats are not a method for any particular financing decision. They are the discipline of someone whose recommendation will be taken to the board. The board will ask questions. The questions will be pointed. The answers need to be true.

---

Here is what Maya writes on a sticky note, which becomes the architecture of her memo.

She needs Halverson's current capital structure: total debt, weighted average interest rate, covenant restrictions, debt maturity schedule. She needs this from the treasurer by Wednesday morning, which means asking on Monday, not Wednesday. The request that arrives Wednesday morning at 9 AM will not get a useful answer before Friday.

She needs the project's cash flow assumptions verified. Plant 4 is supposed to produce some amount of incremental EBITDA per year for some number of years. Whose number is that? Has operations pressure-tested it? Is the $50M construction cost itself a confirmed estimate or a planning placeholder? A planning placeholder should be disclosed as such in the memo — the CFO will know the difference, and finding out later that the number was soft will damage Maya's credibility more than any calculation error would.

She needs to compute the cost of each financing option. The cost of debt comes from Halverson's existing bond yield curve, adjusted for current credit market conditions. The cost of equity comes from the CAPM — Halverson's beta, the risk-free rate, the equity risk premium — adjusted for taxes appropriately. Both need to be calculated explicitly so the comparison is honest.

She needs to compute the value impact of each option. The tax shield from debt financing has a present value. The dilution from equity financing has a cost. She needs both computed so the comparison is apples to apples.

She needs a stress test. If EBITDA comes in 30% below projection, does Halverson still cover debt service with margin? If the equity market closes for several months — not unprecedented — can Halverson fund the plant through other means or delay the project without destroying value?

Then she writes the memo. One page. Recommendation. Reasoning. Three honest risks named by name.

---

I want to end on the idea that opened the chapter, because I think it matters more than the capital structure content.

The gap between inside-the-firm and outside-the-firm finance is not a gap in technical knowledge. Maya has the technical knowledge. The gap is in orientation — how you position yourself when the analysis you need to do is not the analysis you were trained to do. Outside the firm, you are a spectator with good tools. Inside the firm, you are a participant whose recommendation has consequences. The data is messier. The questions are less clean. The people who own the numbers have other things to do.

And the memo goes to the board, where it will be read by people who will ask harder questions than any exam.

The textbook can give you the theory. What I'm trying to do in these pages is something additional: describe the practices — input verification, transparent calculation, honest risk-naming — that connect the theory to a memo you would actually sign your name to.

Maya's Friday memo will recommend debt financing, contingent on the covenant analysis from the treasurer and the EBITDA verification from operations. Whether it goes to the board on the 15th is not her decision. The analysis is.

That is the CFO's first question. Not which instrument. Not what the model says. But: do you understand what you're actually calculating?

---

## Exercises

### Warm-up

**1.** M&M's irrelevance proposition holds in a world with three specific frictions removed. Name all three. For each one, state in a single sentence why removing it makes capital structure irrelevant — and what adding it back changes. *(Tests: understanding of M&M's assumptions and their real-world counterparts.)*

**2.** Maya's memo requires a WACC calculation. Her bond yield curve shows Halverson's existing debt trading at a 6.2% yield. She runs the model and gets a WACC of 4.8%. Before checking a single formula, she flags this as wrong. Explain the sanity-check logic she used — what known anchor made 4.8% obviously incorrect, and what does that tell you about how to sequence a calculation? *(Tests: sanity-check beat of the three-beat method.)*

**3.** A colleague tells you that the "signaling" problem with equity issuance is just a theory, and that in practice, smart CFOs can explain away the signal in their earnings call. What's the empirical evidence the colleague would need to produce to support that claim? What evidence would refute it? *(Tests: distinction between the theory and the empirics of pecking order and signaling.)*

---

### Application

**4.** You are a junior analyst at a mid-sized manufacturing firm. Your CFO asks you for a capital structure recommendation on a $30M equipment purchase by end of week. List every data input you need, name the person or system inside the firm most likely to own it, and estimate the latest you can make each request and still have verified numbers for a Friday memo. *(Tests: input verification beat applied to a novel inside-the-firm context.)*

**5.** Halverson's effective corporate tax rate is 24%. It is considering $50M in new debt at a 6.5% interest rate. Calculate the annual tax shield and, assuming the debt is permanent, the present value of the tax shield using the cost of debt as the discount rate. Then state one assumption embedded in the "permanent debt" simplification that would make your answer an overestimate of the real benefit. *(Tests: tax shield calculation and awareness of its limits.)*

**6.** A startup founder argues: "We should always use equity because debt requires fixed payments and we can't predict our cash flows." A private equity analyst argues: "You should always prefer debt because the tax shield is free money." Using the trade-off theory, explain what both positions get right, what each ignores, and what question you'd need answered about the specific firm before you could evaluate which heuristic applies. *(Tests: applying the trade-off framework to competing claims about capital structure.)*

**7.** Reframe the five jobs embedded in Maya's assignment for a different decision: a hospital system evaluating whether to fund a new MRI suite through a municipal bond offering or a philanthropy campaign. Which of the five jobs look similar? Which look fundamentally different, and why? *(Tests: transferring the five-job decomposition to a non-corporate context.)*

---

### Synthesis

**8.** The chapter argues that the inside/outside gap is primarily a gap in orientation, not in technical knowledge. But M&M's three complications — taxes, distress, and information — are also taught in outside-the-firm courses. Write a paragraph making the strongest possible case that the technical content is the same in both settings, then write a paragraph rebutting it using the verification problem as your main argument. *(Tests: ability to hold and adjudicate competing framings of the inside/outside distinction.)*

**9.** The three-beat method (verify inputs, calculate transparently, sanity-check) is introduced here in the context of a capital structure memo. Identify one beat that would become significantly harder — not just more time-consuming — if Maya were working on a merger valuation rather than a financing decision. Explain why the difficulty is structural, not just a matter of scale. *(Tests: cross-chapter application of the three-beat method; anticipates later content on valuation and M&A.)*

---

### Challenge

**10.** The chapter states that the signaling problem "doesn't resolve as cleanly" as the tax and distress complications. Construct the argument for why it might actually be more tractable than claimed: under what conditions could a CFO credibly neutralize the equity-issuance signal through disclosure alone? Then construct the argument for why those conditions are almost never met in practice. Your answer should engage with the information asymmetry mechanism, not just assert intuitions about what CFOs can and can't say. *(Tests: stress-testing the chapter's own epistemic claims; pushes toward information economics and disclosure theory.)*

---

*Tags: capital structure, inside-the-firm, Modigliani-Miller, trade-off theory, three-beat method, cost of capital, signaling, financial distress*

---

### LLM Exercise — Chapter 1: The CFO's First Question

**Project:** Halverson's Board Memo, Built Across the Course
**What you're building this chapter:** The firm you'll analyze across the next fourteen chapters, Maya's *third Tuesday* version of the specification problem, and a decision frame that names the question precisely.
**Tool:** Claude Project

---

**The Prompt:**

```
I'm starting a project that will run across the next fourteen chapters of *Corporate Finance with AI* by Nik Bear Brown. Across the chapters I will adopt Maya Chen's role at Halverson Industries and build one complete CFO board memo, section by section.

Either I'll use Halverson as the running case (Diane is CFO, the firm is mid-cap industrial, the live decisions are the Plant 4 expansion, the Cardinal Flow Systems acquisition, the FY26 capital plan, and the operational-risk position) or I'll substitute my own employer / a public mid-cap I care about. Paste the firm choice below; if I haven't, ask.

Help me set up Chapter 1's deliverable. Chapter 1 introduces the **specification gap** — the difference between the question Maya was asked and the question her education prepared her for — and the **inside-vs-outside** split.

Produce four things, in order:

1. **The firm, named precisely.** One paragraph. Industry, size (revenue, EBITDA, market cap), capital structure at a glance, the live decision the CFO is wrestling with this quarter. Use Halverson defaults if I gave you no other firm.

2. **The third-Tuesday decision.** One paragraph. The specific decision you'll be analyzing across the book — written as Diane (or your CFO) would phrase it in an email to Maya. Bad: "Look at our capital structure." Good: "By Friday I need a one-page case for whether we fund Plant 4's $50M expansion with new debt, an equity issuance, or a mix — and what the implications are for the Cardinal acquisition we're advancing in parallel."

3. **The four interdependent decisions Chapter 15 will integrate.** A short bullet list — capital allocation, capital structure, payout policy, risk position — each instantiated for *your* firm in one sentence. These four decisions are what the capstone holds at once.

4. **The "what would change my mind" sentence.** One sentence. The specific evidence that would flip the recommendation. The verify-step's anchor for the entire memo.

Format the output as a markdown document `01-decision-frame.md`. Be honest about uncertainty in the firm's numbers — pick figures you'd defend in a meeting, not figures that sound impressive.
```

---

**What this produces:** A markdown document `01-decision-frame.md` containing the firm definition, the third-Tuesday decision, the four interdependent decisions, and the what-would-change-my-mind sentence. This document is the seed for every subsequent chapter's exercise.

**How to adapt this prompt:**

- *For your own project:* Substitute your firm for Halverson where Halverson appears; the exercise structure is firm-agnostic. Halverson's named cast (Diane / Priya / Cardinal) is scaffolding — replace as needed.
- *For ChatGPT / Gemini:* Works as-is. For ChatGPT, save the running memo to a Custom GPT instead of a Claude Project. For Gemini, paste the project's accumulated section files into the context window each session.
- *For Claude Code:* Not the right tool yet — pure markdown drafting.
- *For a Claude Project:* Create a Claude Project named *Halverson Memo — [your firm]*. Put in the system prompt: *every output is a section that will fit into a final 6–10 page integrated CFO board memo at Chapter 15*. Pin the four interdependent decisions list as a project file.

**Connection to previous chapters:** First chapter — no prior exercise to build on. The firm chosen here governs every subsequent exercise.

**Preview of next chapter:** Chapter 2 takes the same firm and produces the *reading-the-firm-from-inside* section — the manager-eye financial-statement read that an outside analyst cannot do.

---

### AI Wayback Machine

The ideas in this chapter didn't appear from nowhere. **Donaldson Brown** was designing the financial control system at DuPont in the 1910s and at General Motors in the 1920s — including the *DuPont identity* every CFO still asks first about return on equity decades before most people had heard of the CFO's first question and the financial-control framing that produces it. Here's a prompt to find out more — and then make it better.

![Donaldson Brown, c. 1920s. AI-generated portrait based on a public domain photograph (Wikimedia Commons).](images/donaldson-brown.jpg)
*Donaldson Brown, c. 1920s. AI-generated portrait based on a public domain photograph.*

**Run this:**

```
Who was Donaldson Brown, and how does his work designing the DuPont financial control system — and the *DuPont decomposition* of return on equity — connect to the chapter's argument that a CFO's first question is not *what's the number?* but *what does the number require to mean what it claims to mean?* Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.
```

→ Search **"Donaldson Brown"** on Wikipedia after you run this. See what the model got right, got wrong, or left out.

**Now make the prompt better.** Try one of these:

- Ask it to explain the *DuPont identity* in plain language, as if you've never seen ROE decomposed
- Ask it to compare Brown's 1920s GM control system to a modern CFO's monthly review
- Add a constraint: "Answer as if you're writing the rationale for the CFO's first three questions in any new fiscal year"

What changes? What gets better? What gets worse?
