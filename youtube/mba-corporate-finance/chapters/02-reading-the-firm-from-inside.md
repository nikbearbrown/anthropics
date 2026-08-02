# Chapter 2 — Reading the Firm from Inside

## TL;DR

- The same numbers, read by someone who knows where they came from.
- The chapter moves through Warm-up, Application, Synthesis, Challenge, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

*The same numbers, read by someone who knows where they came from.*

There is a thing that happens when you sit next to the person who signs the filing.

Maya is sitting next to Aaron, the controller, on a Wednesday morning. He is not happy — the auditors arrive next week — and he has pulled up a working file on his second monitor to show her how things actually work. The file is the Q1 close package. It has eighty-seven tabs.

"This is what I send Diane," he says. "What you saw in the 10-Q is two layers of distillation past this."

In her MBA core, the financial statements were the source. Four statements per year, three per quarter, all clean, all reconciled, all available on EDGAR by the filing deadline. The analysis questions were always *given the statements, what do they tell us?* The data was bedrock.

Aaron's working file flips that entirely. The statements are the *output*. The bedrock is dozens of subsystems — the accounts-receivable aging report, the inventory standard-cost roll, the accrual journal entries, the foreign-exchange translation worksheet, the legal reserve memo, the warranty accrual model. The published statements are the result of decisions about how to summarize those subsystems. Different reasonable decisions produce different statements.

![Diagram showing the Q1 close package as an](images/02-reading-the-firm-from-inside-fig-01.png)
*Figure 2.1 — Diagram showing the Q1 close package as an*

What I want to do in this chapter is show you that. Not to make you suspicious of financial statements — you should trust them, within limits — but to show you that reading a statement as someone who will sign it is a different act from reading it as someone who found it on EDGAR. The inside view is not a different set of numbers. It is the same numbers, held by someone who knows where each one came from.

---

Let me start by being precise about what changes when you cross from outside to inside, because it is easy to understate the difference.

An analyst reading the 10-K uses the statements as a finished product. The numbers are given; the job is to compute ratios, compare them to peers, build a view of the company. Gross margin, operating margin, return on invested capital, days sales outstanding — all of these start from the published figures and reason about the business from there. This is legitimate and useful. It is also incomplete in a specific way.

A CFO reading the same 10-K is doing a different thing. She is asking: are these numbers right? Not right in the auditor's sense — complying with GAAP — but right in the operational sense of reflecting what actually happened. Revenue reported in Q1 is the result of contracts signed, deliveries completed, performance obligations satisfied, and revenue recognition rules applied. Two of those four steps involve judgment. A different judgment changes the reported revenue without changing a single underlying transaction.

The analyst can treat this as noise. The CFO cannot. The accounting choices are the public face of the underlying economics. If they are systematically aggressive — recognizing revenue too early, accruing liabilities too conservatively, depreciating assets too slowly — the statements eventually diverge from reality, and the firm pays in restatements, regulatory scrutiny, and a damaged relationship with auditors.

Maya has not yet felt the weight of her name on a certification. She will. And when she does, the statements will look different to her.

---

There are three things an outside analyst systematically cannot see. Each one is worth naming precisely before we go deep into one of them.

| Blind spot | What the outside analyst sees | What the inside view adds |
|---|---|---|
| **Accrual / cash divergence** | Net income from the income statement, OCF from the cash-flow statement, and the gap between them as a published number | The specific line items moving the gap (deferred revenue, accrued expenses, working-capital choices) and *why* — which choices were made deliberately by management to smooth or signal |
| **Accrual quality** | Reserve levels and revenue-recognition policies as disclosed; the auditor's signed opinion | Whether the reserve sizing is conservative or aggressive *given known operational realities* the public can't see (a customer about to file Chapter 11, a contract under renegotiation) |
| **Off-statement information** | The 10-K narrative; the earnings call; press releases | Internal forecasts, contract pipelines, customer-concentration data, the operations team's read on the next quarter — all the data that drives management's actual view of the firm |

The first is the divergence between accrual earnings and operating cash. Reported net income includes revenue recognized but not yet collected, expenses incurred but not yet paid, depreciation which is an accounting charge against an earlier cash outflow and does not move any cash today, and accruals — estimates of future obligations booked against current-period income to match costs to the revenue they support. Operating cash flow does none of that. It counts cash received, cash paid, and cash only. The two numbers can diverge for completely legitimate reasons or for deeply worrying ones, and the face of the 10-K does not tell you which story you are in.

The second is the quality of the accruals themselves. Not all accruals are equal. A warranty accrual derived from five years of return-rate data processed through an actuarial model is a different thing from a warranty accrual set at 4:00 PM on the last day of the quarter in response to an email asking whether there is "any flexibility" on the EPS number. From the outside, both look like warranty accruals. From inside, you know which one was the model and which one was the email.

The third is the information that never made it into the statements at all. The biggest customer was just acquired by a competitor, and the renewal probability has dropped dramatically. A class-action lawsuit was filed last week, and the legal reserve has not yet been booked because outside counsel is still assessing exposure. The main production system at the largest plant is end-of-life, and a thirty-million-dollar replacement is coming in the next fiscal year. None of this is in the Q1 statements. All of it is in Diane's head and in the planning materials for Q3. From inside, you read the firm with this overlay running constantly. From outside, you infer what you can from earnings call transcripts and management commentary — which is to say, you can mostly miss it.

Aaron, after his second coffee, puts it this way: the statements tell you what happened. The CFO tells you what is about to happen. Neither alone is the firm.

---

Now I want to go deep on one mechanism. One mechanism understood completely is worth more than five mechanisms understood shallowly. The one I want to show you is the relationship between net income and operating cash flow. It is the cleanest single lens I know for seeing the inside/outside difference in a concrete calculation.

Start with a simple income statement:

$$\begin{array}{lr}
\text{Revenue} & 1{,}000 \\
-\ \text{Cost of Goods Sold} & (600) \\
-\ \text{SG\&A} & (200) \\
-\ \text{Depreciation} & (50) \\
\hline
\text{Operating Income} & 150 \\
-\ \text{Interest Expense} & (30) \\
-\ \text{Tax Expense} & (25) \\
\hline
\text{Net Income} & 95
\end{array}$$

This firm earned $95M. Now build the operating cash flow from the same firm using the indirect method — which is what the cash flow statement actually does. You start from net income and work backward toward cash:

$$\begin{array}{lr}
\text{Net Income} & 95 \\
+\ \text{Depreciation (non-cash; add back)} & 50 \\
-\ \text{Increase in Accounts Receivable} & (40) \\
-\ \text{Increase in Inventory} & (20) \\
+\ \text{Increase in Accounts Payable} & 25 \\
+\ \text{Increase in Accrued Liabilities} & 10 \\
\hline
\text{Operating Cash Flow} & 120
\end{array}$$

![Bridge diagram ](images/02-reading-the-firm-from-inside-fig-02.png)
*Figure 2.2 — Bridge diagram *

This firm generated $120M of operating cash while reporting $95M of net income. The $25M gap is the arithmetic sum of several pieces: depreciation added back because it was a non-cash charge; receivables that grew because revenue was recognized before cash arrived; inventory that grew because cash was spent on goods not yet sold; payables and accruals that grew because obligations were incurred but not yet paid.

Each of those adjustments has a real-world story behind it. And here is the thing — the thing that I want you to sit with for a moment.

Take three different firms. Each one reports $95M of net income and $120M of operating cash flow. Identical numbers, to the digit.

Firm A is growing fast. New customers take sixty-day payment terms. Receivables build every quarter because the customer count is growing, not because anyone is delinquent. Inventory builds because the company is stocking to serve new demand. Operating cash lags net income. The firm is healthy. The gap is investment in working capital.

Firm B is stagnant. Revenue has been flat for six quarters. Receivables are growing because the largest customers stopped paying on time. The AR aging report shows sixty-day and ninety-day buckets increasing as a share of total receivables. Operating cash lags net income for the same numerical reason as Firm A, but the story is completely different. The gap is bad debt waiting to be recognized.

Firm C is managing its earnings. Revenue was light through the first eleven weeks of the quarter, and so in the final two weeks the sales team signed contracts with customers who have not yet received delivery and, under strict revenue recognition rules, should not have been recognized. The receivables spike at quarter-end reflects contracts signed but performance not yet completed. Operating cash lags net income because cash does not follow recognized revenue that has not yet been earned. The gap is the size of the misrepresentation.

| Firm | Revenue trend | AR growth driver | Inside diagnostic | Interpretation of the gap |
|---|---|---|---|---|
| **Firm A** | Growing | New customers | AR aging skews to *current* (0–30 days) | Working-capital investment supporting genuine growth |
| **Firm B** | Stagnant | Slow payers | AR aging skews to 60–90 days | Bad debt accumulating; collections operationally broken |
| **Firm C** | Managed | Quarter-end contracts | AR spike concentrated in the final two weeks of the quarter | Earnings being misrepresented through aggressive cut-off practice |

*Identical summary numbers map to three entirely different business realities. Only the inside view distinguishes them.*

Three firms. Identical income statements. Identical cash flow statements. The outside analyst cannot distinguish them from the numbers alone. The inside view distinguishes them immediately — because the inside view has Aaron's eighty-seven-tab working file, which includes the AR aging report showing whether the receivables belong to new customers, old customers, or contracts signed in the last forty-eight hours of the quarter.

---

This is the mechanism. Now let me say what to do with it.

The most useful single diagnostic I know for assessing earnings quality — the degree to which reported earnings reflect real, durable, cash-convertible economic activity — is the ratio of operating cash flow to net income. I'll call it the cash conversion ratio:

$$\text{Cash Conversion Ratio} = \frac{\text{Operating Cash Flow}}{\text{Net Income}}$$

A ratio consistently above 1.0 means the firm is generating more cash than its reported earnings, which is the signature of high earnings quality. Depreciation and payables management work in the firm's favor, and working capital dynamics are clean. A ratio declining over time means each dollar of reported earnings is backing up against more working capital — receivables building, inventory accumulating, something not converting to cash the way it used to. A ratio persistently below 1.0, in a firm that is not in an explainable high-growth phase, is the most reliable early warning signal I know of in financial statement analysis.

![Line chart showing cash conversion ratio over eight](images/02-reading-the-firm-from-inside-fig-03.png)
*Figure 2.3 — Line chart showing cash conversion ratio over eight*

The empirical foundation for this goes back to Richard Sloan's 1996 work on accruals, which showed that the accrual component of earnings — the difference between net income and operating cash flow — is less persistent than the cash component in predicting future earnings. Firms with high accruals tend to see subsequent earnings revisions downward. Firms with low accruals tend to see earnings persist. The mechanism is exactly what we described: when reported earnings run ahead of cash, either the cash catches up — meaning the accruals were legitimate timing differences — or the earnings come down, meaning they were overstated. The market has historically been slow to price this in, though the gap has narrowed as the finding became widely known.

But the diagnostic has not become less useful inside a firm. If Maya asks Aaron what their trailing-twelve-months cash conversion ratio has been over the last eight quarters, and the trend is declining — say, from 1.2 two years ago to 0.8 now — that is not an artifact of academic arbitrage. That is a real question about what changed in the working capital dynamics, and it requires an answer.

---

There is a further layer I want to point to: the difference between accruals that estimate real economic events and accruals shaped to produce a desired outcome.

Every accrual is an estimate. The question is whether the estimate is derived from the best available data about the underlying obligation, or from what the number needs to be. A warranty accrual can legitimately be revised downward if product quality improved and return rates dropped. It can also be revised downward because the CFO needs three more cents of EPS. The revision looks identical in the financial statements. The motivation is invisible from outside.

What makes this difficult is that most CFOs are not choosing between honesty and deception. They are choosing, within the corridor GAAP allows, between conservative and aggressive. Conservative accruals — larger reserves, earlier expense recognition, slower revenue recognition — tend to build hidden strength in the balance sheet. The earnings look worse in good quarters and better in bad ones, because the reserves are available to draw against when the business softens. Aggressive accruals do the reverse: earnings look better now, but the reserves are thin when business softens, and the accounting has nowhere to go but down.

| Dimension | Conservative posture | Aggressive posture |
|---|---|---|
| **Reserve sizing** | Larger reserves for receivables, warranty, returns; pre-emptive write-downs | Reserves released into earnings opportunistically; write-downs deferred |
| **Revenue recognition timing** | Earlier-stage revenue deferred until risk is clearly transferred | Revenue recognized at the earliest defensible point in the contract |
| **Depreciation pace** | Shorter useful lives, faster expensing | Longer useful lives, slower expensing |
| **Earnings in good quarters** | Visibly understated; reserves built | Visibly amplified; reserves flat or released |
| **Earnings in bad quarters** | Cushioned by reserve releases; smoother trajectory | Visible drops with no buffer; volatility flows through |
| **Balance sheet resilience** | Higher reserves and lower book asset values; more room to absorb shocks | Tighter reserves and higher book asset values; less buffer |

Both are legal. The outside analyst sees the reported number. The inside view sees which direction the estimates are running, and whether that direction has been consistent across the cycle.

Aaron's heuristic: watch what management does with accruals at the end of a good quarter versus a bad quarter. In a good quarter, does the firm build reserves or report every cent of earnings? In a bad quarter, does it draw carefully on reserves to smooth the shortfall, or take a large restructuring charge to reset the baseline? Consistent reserve-building in good times and measured release in bad times is the signature of a CFO who treats the balance sheet as a real economic object. The alternative — minimizing reserves when they would hurt earnings, maximizing them when they create a future release — is the signature of a CFO who treats it as a dial.

---

There is one more category of information to name, even though it resists quantification: the things that are not in the statements at all.

Financial statements are backward-looking by design. They record what happened, within the bounds of what accounting requires to be disclosed. What they do not record is what the CFO knows is coming. The customer who just told the sales team they are moving to a competitor. The supplier whose pricing resets at year-end, compressing margins. The regulation in final rulemaking that will require a capital expenditure not yet announced. The key engineer who is leaving and whose departure will slow the product roadmap.

None of this appears in the Q1 10-Q. All of it is in Diane's quarterly business review and in the forecasting model Maya will eventually maintain. The inside view is not just reading the statements more carefully. It is reading the statements with this forward-looking operational knowledge running alongside.

An outside analyst works around this by reading earnings call transcripts carefully, tracking what management chose to discuss and what it chose to avoid, building a picture from channel checks and industry contacts. This is legitimate and often effective. It is a secondhand version of information the inside view receives directly. The analyst estimates. The CFO knows. The asymmetry is permanent, and part of what Maya is learning to do is use it.

---

What Maya takes away from the hour with Aaron is not more sophisticated than this: the same numbers mean different things depending on what produced them, and the producing process is visible from inside in a way it is not from outside.

She will still compute the ratios she already knows. She will still benchmark against peers, run DuPont decompositions, look at trend lines. None of that changes. What changes is one additional question that runs alongside every ratio: is the component driving this number clean? Is the receivables growth from new business or slow payers? Is the margin expansion from pricing or from accrual release? Is the operating cash conversion improving because the business is getting healthier, or because payables are being stretched to manufacture the appearance of it?

These are not suspicious questions. They are the questions a person who will sign the filing has to be able to answer. The act of asking them is the difference between reading the statements as a consumer and reading them as someone responsible for what they say.

She will not read the next 10-Q the same way she read every 10-Q before this week. The document will look the same. But she will now see, behind every summary line, the working file that produced it — and she will know which questions to ask about what is in it.

---

*A note on what this chapter simplified.* The indirect method on the cash flow statement is the most common presentation and the one that makes the net income / operating cash relationship visible. The direct method — showing gross cash receipts and gross cash payments — would be more intuitive but is rarely used in practice. Sloan's accruals finding has been replicated and partially refined; the strongest version applies to firms where accruals are discretionary rather than mechanically driven by business model. High-growth firms with large but legitimate working capital buildups will show low cash conversion ratios without any earnings management involved, which is why growth-adjusted interpretation matters. Maya will get the growth-adjusted version in Chapter 8.

---

## Exercises

### Warm-up

**1.** A firm reports net income of $80M and operating cash flow of $60M. Its accounts receivable increased by $30M during the quarter, and depreciation was $15M. (a) Compute the cash conversion ratio. (b) Is a ratio below 1.0 automatically a warning sign here? What additional information would you want before forming a judgment? *(Tests: indirect method mechanics; cash conversion ratio interpretation)*

**2.** Explain in plain language why depreciation is added back when converting net income to operating cash flow. What would go wrong with the calculation if you did not add it back? *(Tests: understanding of non-cash charges and the logic of the indirect method)*

**3.** Aaron distinguishes between an accrual "derived from the model" and one "set at 4:00 PM on the last day of the quarter." Both result in the same line item in the published statements. What is the difference, and why does it matter to someone who will sign the filing? *(Tests: accrual quality distinction; inside vs. outside view)*

---

### Application

**4.** Below are eight quarters of cash conversion ratio data for a single firm: 1.18, 1.21, 1.15, 1.09, 0.97, 0.88, 0.81, 0.76. Revenue grew 12% annually over the same period. (a) Describe the trend. (b) Generate two competing explanations for the decline — one benign, one worrying. (c) Name the specific data from Aaron's working file you would request to distinguish between them. *(Tests: cash conversion ratio trend analysis; inside-view diagnostic reasoning)*

**5.** A firm's gross margin expanded 180 basis points year-over-year. The CFO attributes it to pricing discipline. An analyst suspects accrual release. Describe what you would look for in the working file — specific line items, specific trends — to evaluate which explanation is correct. *(Tests: connecting accrual posture to reported margin; applying the inside/outside distinction to a real analytical question)*

**6.** Find the most recent 10-Q for any publicly traded manufacturer. Locate the cash flow statement and compute the cash conversion ratio for the trailing twelve months. Then read the MD&A section and identify whether management's explanation for working capital changes is consistent with what the numbers show. Write a one-paragraph assessment. *(Tests: applying the diagnostic to a real filing; cross-referencing statement data with management narrative)*

**7.** Aaron's heuristic says to watch accrual behavior at the end of good quarters versus bad quarters. Design a simple data collection framework — what you would track, over how many periods, using which line items — to apply this heuristic systematically to a firm you are analyzing from the outside. *(Tests: translating the inside-view heuristic into an outside-analyst procedure)*

---

### Synthesis

**8.** The chapter presents three categories of information the outside analyst cannot see: the accrual/cash divergence, accrual quality, and off-statement information. For a firm you are evaluating for a potential investment, rank these three blind spots by materiality and explain your reasoning. Under what business conditions might the ranking change? *(Tests: weighing the three blind spots against each other; connecting information asymmetry to investment context)*

**9.** The chapter argues that the inside view and the outside view are reading the same numbers but doing fundamentally different things. A CFO at a public company has both views simultaneously — she can read the 10-K the way an analyst would, and she knows what produced it. Describe how this dual perspective should change the way she communicates with investors on an earnings call. What should she say that most CFOs do not? What would a purely outside-facing CFO miss? *(Tests: synthesizing the inside/outside distinction with investor communication; applying the chapter's core argument to a new context)*

**10.** Sloan's 1996 finding showed that high-accrual firms tend to see subsequent earnings revisions downward. The chapter notes the market has partially priced this in. Does the finding still generate useful information for someone working inside a firm, even if the arbitrage opportunity has narrowed? Construct an argument for why inside utility and outside arbitrage value are separable. *(Tests: distinguishing analytical utility from market pricing; applying the Sloan finding beyond its original investment context)*

---

### Challenge

**11.** The chapter uses Firms A, B, and C — all with identical published financials — to show that the same numbers can reflect three entirely different business realities. Construct a fourth scenario, Firm D, in which a cash conversion ratio above 1.0 is actually a warning sign rather than a signal of health. Explain the mechanism, identify what inside information would reveal it, and describe what an outside analyst would need to see to suspect something was wrong without having access to the working file. *(Tests: stress-testing the cash conversion ratio as a diagnostic; generating counterexamples to framework claims)*

**12.** This chapter focuses on what the inside view adds to reading financial statements. Consider the reverse: are there things the outside analyst can see more clearly than the CFO? Design an argument for why information asymmetry sometimes runs the other direction — where distance from the firm is an analytical advantage, not a liability. Use specific examples from the chapter's framework to ground your argument. *(Tests: challenging the chapter's directional claim; applying the inside/outside distinction to its own limits)*

---

###  LLM Exercise — Chapter 2: Reading the Firm from Inside

**Project:** Halverson's Board Memo, Built Across the Course
**What you're building this chapter:** The Inside-View Read section of the memo: a manager-eye assessment of the firm's three financial statements, the operational reality behind them, and the institutional-memory questions only an insider can answer.
**Tool:** Cowork

---

**The Prompt:**

```
I'm working on Halverson's Board Memo for the firm in `01-decision-frame.md`. Chapter 2 distinguished:

- The **outside-analyst view** — built from public data (10-K, earnings calls, EDGAR), with the verification loop running through cross-references
- The **inside-analyst view** — built from operational data, institutional memory, and people in the building, with the verification loop running through ownership of the underlying numbers

In **Cowork**, produce `02-inside-read.md` containing:

1. **The three-statement insider read.** Pull the most recent annual filing (10-K) and quarterly filing (10-Q) for your firm. For each statement, write 4–6 sentences that an analyst from outside the firm could *not* write — i.e., the inside-view interpretation. Examples:
   - **Income statement**: which revenue is the company internally calling *backlog conversion* vs. *new bookings*? Which margin is being protected by which operational lever?
   - **Balance sheet**: which receivables are the credit team flagging? Which inventory is the operations team writing down quietly?
   - **Cash flow statement**: which line of operating cash is being moved by working-capital choices vs. by underlying operational performance?

2. **The shadow numbers.** Three-to-five operational metrics the firm tracks internally that don't appear in any filing — backlog conversion rate, customer concentration, days of safety stock, average sales-cycle length, channel-mix shift. State each, give the latest internal value (or your best estimate), and explain why it matters for the third-Tuesday decision in `01-decision-frame.md`.

3. **The institutional-memory questions.** Three questions only an insider could answer that *should* be answered before the Chapter 15 board memo ships. Examples:
   - "Why was the Q3 2023 working-capital improvement reversed in Q1 2024?"
   - "What did Diane commit to the audit committee at the September meeting?"
   - "Who actually owns the customer-concentration policy?"

Save as `02-inside-read.md`. The verification loop here is *ownership-based* — for each claim, the inside view names *who you'd ask* to confirm it.
```

---

**What this produces:** A markdown document `02-inside-read.md` containing the three-statement insider read, three-to-five shadow numbers, and the institutional-memory questions that only an insider can answer.

**How to adapt this prompt:**

- *For your own project:* Substitute your firm for Halverson where Halverson appears; the exercise structure is firm-agnostic. Halverson's named cast (Diane / Priya / Cardinal) is scaffolding — replace as needed.
- *For ChatGPT / Gemini:* Works as-is. For ChatGPT, save the running memo to a Custom GPT instead of a Claude Project. For Gemini, paste the project's accumulated section files into the context window each session.
- *For Claude Code:* Not needed for the prose; Cowork's filing-pull is the load-bearing tool.
- *For a Claude Project:* Cowork is the right tool — it can pull the 10-K and 10-Q from EDGAR (or from a local file) and assemble the read in one session. The Project context inherits the firm choice.

**Connection to previous chapters:** Chapter 1 named the firm and the decision; Chapter 2 reads the firm from the inside, distinguishing what the public can see from what only Maya can.

**Preview of next chapter:** Chapter 3 zooms in on working capital — the part of the firm where cash actually lives — and produces the cash-conversion-cycle analysis.

---

##  AI Wayback Machine
The ideas in this chapter didn't appear from nowhere. **Mary Harris Smith** was becoming, in 1919, the first woman chartered accountant in the world — over four decades after she had already been doing the work without being credentialed for it decades before most people had heard of reading a firm's books from inside, with the discipline that distinguishes a manager's view from an outside analyst's. Here's a prompt to find out more — and then make it better.

![Mary Harris Smith, c. 1920. AI-generated portrait based on a public domain photograph (Wikimedia Commons).](images/mary-harris-smith.jpg)
*Mary Harris Smith, c. 1920. AI-generated portrait based on a public domain photograph.*

**Run this:**

```
Who was Mary Harris Smith, and how does her career — including the four-decade gap between her competence and her credentialing — connect to the chapter's argument that *reading the firm from inside* requires both technical accounting fluency and the practitioner-level access that historically gated who could exercise it? Keep it to three paragraphs. End with the single most surprising thing about her career or ideas.
```

→ Search **"Mary Harris Smith"** on Wikipedia after you run this. See what the model got right, got wrong, or left out.

**Now make the prompt better.** Try one of these:

- Ask it to explain why the *insider's view of the books* is structurally different from the *analyst's view*, in plain language
- Ask it to compare the credentialing barriers Smith fought to the access barriers a modern non-finance manager hits when reading their own firm
- Add a constraint: "Answer as if you're writing the introduction to a chapter on reading financial statements as a manager, not as an analyst"

What changes? What gets better? What gets worse?
