# Chapter 5 — Time Value and Discounted Cash Flows

*A dollar today is worth more than a dollar tomorrow — and the discipline is making that preference precise.*

---

Maya's friend Sara calls with a question that sounds like it has a simple answer.

Her parents own a regional catering company they have been running for thirty years. They want to retire. They want to sell to Sara at a fair price. The asking price is $850,000. The business cleared about $180,000 last year.

"Is this a good deal?" Sara asks.

The naive calculation is seductive. $850,000 divided by $180,000 is under five years to pay back. Five years sounds fast. Sounds great.

But "pays back in five years" is not the same thing as "is a good deal." There are at least four questions hiding inside Sara's one. Is the business worth $850,000 — which is distinct from whether it generates $180,000, because $180,000 for two years is one thing and $180,000 for thirty is another. Compared to what — Sara could put $850,000 into something else. What discount rate — the number that captures both the time value of money and the risk that the projected cash flow doesn't materialize. And how certain are we about the inputs — the $180,000 is last year's number, one data point, and we do not yet know the trend.

The math that connects all four questions — that connects what something costs today to what something will be worth — is the time value of money. It is the foundational tool for almost every decision the rest of this book makes. Once you have it, a large fraction of finance falls out the way a large fraction of mechanics falls out of $F = ma$: not as a series of separate techniques to memorize, but as one engine running underneath.

---

Let me make you an offer. I will give you $100 today, or I will give you $100 a year from now. Same amount. Which do you prefer?

Almost everyone says today. If you press on why, three reasons emerge. First, you could invest the $100 today and have more than $100 a year from now. Second, prices might rise — $100 buys less next year than it buys today. Third, the future is uncertain. I might forget. I might default. A hundred dollars a year from now has all three of those shadows on it that today's $100 does not.

That preference, made quantitative, is the discount rate. The discount rate is the price of waiting — the fraction by which a future dollar must be marked down to be worth today's dollar to you.

The mechanism of compounding and discounting is a single operation seen from two directions. Suppose you invest $1 today at annual rate $r$. After one year you have $1 + r$. After two years the second year's growth is on the new balance, so you have $(1+r)^2$. After $n$ years:

$$\text{FV} = \text{PV} \cdot (1+r)^n$$

That is compounding. Forward in time. Money grows.

Now turn it around. Suppose I am going to pay you a fixed amount in $n$ years. What is it worth today? Whatever amount, invested at rate $r$, would grow into that payment after $n$ years. Solve the same equation for PV:

$$\text{PV} = \frac{\text{FV}}{(1+r)^n}$$

That is discounting. Backward in time. Future money shrinks.

![Two-arrow timeline showing compounding (today → year n) and discounting (year n → today) as the same factor in opposite directions](images/05-time-value-of-money-and-discounted-cash-flows-fig-01.png)
*Figure 5.1 — Compounding and discounting are one operation, run two ways*

Read those two formulas side by side. They are the same equation. Compounding multiplies by $(1+r)^n$. Discounting divides by $(1+r)^n$. Most students hold these as two separate formulas to memorize. They are one formula, one operation, two directions.

Inside the discount rate are three components. The risk-free rate — what you could earn with certainty by lending to the safest available borrower, roughly the short-term Treasury rate. An inflation component — compensation for the loss of purchasing power, already embedded in nominal rates. And a risk premium — compensation for the chance the cash flow does not materialize as expected. The riskier the cash flows, the larger this premium must be. A 12% discount rate on Sara's catering business encodes all three: perhaps 4% risk-free, some embedded inflation, and a substantial premium for the operating risk of a small private business with concentrated customers and a founder who is about to leave.

<!-- → [INFOGRAPHIC: stacked bar decomposing a 12% discount rate into its three components — risk-free rate (~4%), inflation (~2%), risk premium (~6%) — labeled with brief descriptions of what each compensates for] -->

---

Now I want to show you what discounting actually does to a stream of future payments — why it is not the same as nominal arithmetic, and why the difference matters.

Here is a contract. You pay $1,000 today. In return, you receive $300 a year for the next four years. Total nominal inflows: $1,200. Naive arithmetic says you profit $200. Good deal?

Not so fast. Each of those $300 payments arrives at a different time and must be discounted back to today. Suppose the discount rate is 8% — what you could earn by putting the $1,000 into something else.

Year 1: $300 / 1.08 = \$277.78$

Year 2: $300 / 1.08^2 = \$257.20$

Year 3: $300 / 1.08^3 = \$238.15$

Year 4: $300 / 1.08^4 = \$220.51$

Sum of present values: $\$277.78 + \$257.20 + \$238.15 + \$220.51 = \$993.64$

Net present value: $\$993.64 - \$1{,}000 = -\$6.36$

Negative. Slightly. The $1,200 of nominal inflows, when properly time-aligned, is worth $993.64 today. You are paying $1,000 for it. You lose six dollars.

A reader who skipped the discounting would have called this deal profitable. The reader who discounted sees it is marginally money-losing. That gap — between nominal arithmetic and time-aligned arithmetic — is what the tool is for. The $300 arriving in year four is simply not the same thing as $300 today, and any analysis that treats them as equivalent is making an error. The discounting forces you to see the difference.

| Year | Nominal cash flow | Discount factor $1/(1.08)^t$ | Present value |
|---|---|---|---|
| 1 | $300 | 0.9259 | $277.78 |
| 2 | $300 | 0.8573 | $257.20 |
| 3 | $300 | 0.7938 | $238.15 |
| 4 | $300 | 0.7350 | $220.51 |
| **Sum of PVs** | | | **$993.64** |
| **Cost** | | | **$1,000.00** |
| **NPV** | | | **−$6.36** |

*Nominal cash flows total $1,200 — the contract "looks" profitable at the $1,000 price. Discounted at 8%, the present value is $993.64 — narrowly negative NPV. The "profit" was eaten by the time value of money. The discount rate is where the entire decision lives.*

The general formula: for a stream of cash flows $\text{CF}_0, \text{CF}_1, \ldots, \text{CF}_n$ at discount rate $r$, the net present value is

$$\text{NPV} = \sum_{t=0}^{n} \frac{\text{CF}_t}{(1+r)^t}$$

The decision rule follows directly. NPV greater than zero means the inflows, properly time-aligned, exceed the outflows — the project clears the bar. NPV less than zero means it does not. NPV equal to zero means the project earns exactly your required return — take it or leave it, you are indifferent.

There is a related question worth naming. What discount rate would make the NPV exactly zero? That rate is the project's internal rate of return — IRR. It is the implicit return the cash flow stream itself earns. For the toy contract above, NPV is negative at 8% and positive at lower rates; the IRR works out to about 7.7% [verify]. The decision rule: if IRR exceeds your hurdle rate, take the project. If it falls short, reject.

IRR and NPV almost always agree. When they disagree — usually when comparing mutually exclusive projects of different sizes — trust NPV. The reason is this: IRR measures a percentage rate; NPV measures total dollars created. A 50% return on a $1,000 investment creates $500 of value. An 18% return on a $1,000,000 investment creates $180,000 of value. You cannot spend a percentage. For ranking decisions, dollars win.

---

Two cash flow shapes appear often enough to have names and closed-form solutions, and both are worth deriving rather than just stating, because the derivation is the same machinery that generates every closed-form valuation formula in finance.

A perpetuity is a stream of equal payments that goes on forever — payment $C$ each period, forever. The present value looks impossible to compute, because you are summing infinitely many terms. But the sum is a geometric series:

$$\text{PV} = \frac{C}{1+r} + \frac{C}{(1+r)^2} + \frac{C}{(1+r)^3} + \ldots$$

A geometric series with first term $a = C/(1+r)$ and common ratio $q = 1/(1+r)$. When $|q| < 1$, the sum converges:

$$\text{PV} = \frac{a}{1-q} = \frac{C/(1+r)}{1 - 1/(1+r)} = \frac{C/(1+r)}{r/(1+r)} = \frac{C}{r}$$

An infinite stream of payments collapses to a single fraction. The mathematics is saying: if you discount future payments far enough, they become negligible, and the sum converges to something finite.

The growing perpetuity — payment $C$ next period, growing at rate $g$ per period forever — works the same way with a different common ratio. As long as $r > g$:

$$\text{PV} = \frac{C}{r - g}$$

This is the Gordon growth model, and it does enormous work in valuation. It converts "cash flows continuing indefinitely at some sustainable growth rate" into a single number. We are about to use it for Sara's catering business.

---

Now Sara's deal, end to end.

The structure of the valuation: ten years of explicit cash flow projections, a terminal value at the end of year 10 representing all cash flows from year 11 onward, and a discount rate that reflects the risk of a small private business with concentrated customers and a founder transition.

Maya builds the model. Year 1 cash flow: $180,000. Growth rate: 2% per year. Discount rate: 12% — reflecting the risk-free rate, embedded inflation, and a substantial risk premium for a single-operator small business.

The terminal value at the end of year 10: the growing perpetuity formula applied to year-10 cash flow. Year 10 cash flow is $180,000 \times (1.02)^9 \approx \$215,000$. Terminal value $= 215,000 / (0.12 - 0.02) = \$2,150,000$. That is what we assume all cash flows from year 11 onward are worth, at the moment of year 10.

Discounting all of this back to today: the present value of the ten explicit years of cash flow comes to roughly $1,074,000 [verify]. The present value of the terminal value — $2,150,000 discounted ten years at 12% — comes to roughly $692,000 [verify]. Total enterprise value: approximately $1,766,000 [verify]. Subtract the purchase price of $850,000. NPV: approximately $916,000 [verify]. IRR: roughly 23% [verify].

<!-- → [CHART: stacked bar chart showing the two components of the $1,766,000 enterprise value — present value of 10-year explicit cash flows (~$1,074,000) and present value of terminal value (~$692,000) — student should see how much of the total valuation rests on the terminal value assumption] -->

The deal looks spectacular. Sara is paying $850,000 for cash flows worth $1,766,000.

This should make you suspicious. Real businesses do not sell at half their fair value. If Sara could genuinely buy $1,766,000 of value for $850,000, every sophisticated acquirer in the country would be bidding for the same business and driving the price up. The fact that the parents are willing to sell at $850,000 means either the model's inputs are too optimistic, or there are structural costs the model is not capturing, or the parents are deliberately pricing below market for personal reasons — retirement, family transfer, tax planning.

This is where bounds-checking earns its place.

Small food-service businesses typically sell at one to three times annual cash flow [verify against current transaction data]. Sara's deal, at $850,000 for $180,000 of cash flow, is at 4.7 times — near the upper end of what the market would support. The model's optimistic answer is coming from the model's optimistic inputs: a 12% discount rate that may understate the risk of a concentrated-customer, single-operator business; a 2% growth assumption that implies Sara can raise prices with inflation, a notoriously difficult thing for catering owners to do; and a $180,000 figure that may be a peak year rather than a representative one.

Change the assumptions honestly. Discount rate 18% — appropriate for concentrated-customer, single-operator risk where the operator has no track record. Year-1 cash flow $150,000 — assume last year was somewhat strong. Growth 0% — no price pass-through. Run the same model.

NPV: roughly $50,000 [verify]. IRR: roughly 13% [verify].

Under these assumptions, the deal barely clears the bar. Sara is paying close to fair value, not getting a steal.

This is the answer Sara actually needs. Not "great deal" or "bad deal" but: at the optimistic end of plausible assumptions, the NPV is nearly a million dollars positive. At the realistic end, the deal is approximately fair. The asymmetry is in the upside, not the downside — meaning the deal is not obviously bad, but it is not obviously good either, and the outcome hinges on specific questions about the business that the model cannot answer.

---

Those specific questions are what the sensitivity table reveals, and the sensitivity table is where the analysis becomes useful rather than merely correct.

The single-number NPV — whether $916,000 or $50,000 — is a point on a curve. The curve is the answer. You cannot use a single NPV to make a decision unless you know how sensitive it is to the inputs you are uncertain about.

The discipline is mechanical. Pick the inputs you are most uncertain about — discount rate, year-1 cash flow, long-run growth rate. For each one, compute NPV at a base case, a low case, and a high case, holding the other inputs at their base values. The shape of the resulting table tells you what the answer actually depends on.

For Sara's deal, varying the year-1 cash flow at the 12% discount rate:

| Year-1 CF | NPV (approx) |
|---:|---:|
| $120,000 | ≈ $0 |
| $150,000 | ≈ $400,000 |
| $180,000 | ≈ $916,000 |
| $210,000 | ≈ $1,500,000 |
| $240,000 | ≈ $2,000,000 |

| | Year-1 CF: \$120K | \$150K | \$180K | \$210K |
|---|---|---|---|---|
| **Discount rate 10%** | -$95K | $42K | $179K | $316K |
| **Discount rate 12%** | -$143K | -$15K | $113K | $241K |
| **Discount rate 15%** | -$208K | -$93K | $22K | $137K |
| **Discount rate 18%** | -$262K | -$159K | -$56K | $47K |

*The break-even boundary runs from the upper-left toward the lower-right. The deal works in roughly the upper-right triangle (high CF, low discount rate). It does not work in the lower-left triangle. Most disagreements about a DCF are disagreements about which corner of this table the decision-maker is anchoring to.*

The break-even year-1 cash flow — the number below which the deal destroys value — is roughly $120,000 [verify]. If Sara believes the business can sustain at least $120,000 annually, the deal clears the bar at a 12% discount rate.

The most useful single number in a sensitivity analysis is usually the break-even on the most uncertain input. Not "the NPV is positive" but "the business needs to sustain at least $X of cash flow per year for this to make sense, and here is what the history looks like relative to that threshold."

There is a failure mode worth naming. Most DCF errors are not arithmetic. They are upstream — the inputs were optimistic, the discount rate too low, the growth assumption too generous. The single-point NPV does not expose any of this. It hides it behind a clean number. The sensitivity table exposes it by showing how the answer moves when the inputs move. A model whose NPV collapses from $916,000 to $50,000 with a modest change in assumptions is a model telling you that the answer is really about the assumptions — and the prudent question is which assumptions are actually defensible.

The question that matters for Sara is not whether the model can be made to show a positive NPV. It can. The question is: what does the business need to do, and how confident are we that it will do it? The sensitivity table is what allows her to ask that question precisely rather than generically.

---

There is a practical consequence of all this for how Maya structures the memo to Sara.

Not a verdict. A range, a set of conditions, and a list of questions the analysis cannot answer but that Sara should answer before signing.

The questions: Is $180,000 representative or a peak year? What did the prior five years of cash flow look like? Are major customers concentrated in a way that follows the parents personally rather than the business? What happens to cash flow in year two after the transition? What are the capital expenditure requirements on aging refrigeration, vans, and kitchen equipment?

The price implication: at an 18% discount rate and $150,000 year-1 cash flow, the break-even acquisition price is roughly $750,000 [verify]. If Sara's due diligence pushes toward the pessimistic assumptions, $750,000 is a defensible counter-offer. If the due diligence is reassuring, $850,000 is fair.

The contract structure matters as much as the price: an earn-out tying part of the purchase price to actual year-one and year-two performance, a non-compete binding the parents, and a structured transition period with the parents introducing Sara to the customer base. These are not afterthoughts. They are the tools that align the parents' incentives with Sara's outcome after the sale.

This is what the time-value-of-money framework actually produces: not a number, but a structured way to think about a decision, with the load-bearing assumptions made explicit and the questions that remain unanswered clearly labeled. The memo is something Sara can use. It converts a gut-feeling question — is this fair? — into a set of verifiable propositions — here is what the business needs to do, here is the price at which it makes sense, and here are the things I need to check before I commit.

---

Let me end with the thing I find most satisfying about this machinery.

Most of finance reduces to one operation: moving cash flows through time. Compounding forward, discounting backward. Bond valuation is discounting coupons and principal. Stock valuation is discounting dividends or free cash flow. Project finance is discounting operating cash flows against an upfront investment. Retirement planning is discounting future consumption against present savings. In every case, the underlying machinery is the same — you put cash flows on a common time scale by multiplying or dividing by $(1+r)^n$.

Master the operation once, and the field stops looking like a list of separate techniques. It starts looking like one tool applied in many different circumstances. The formula changes shape — perpetuity, annuity, growing perpetuity, multi-stage DCF — but the engine underneath is always the same geometric series, always the same intuition that a dollar today is worth more than a dollar tomorrow, always the same question: what rate reflects the time preference and the risk of these specific cash flows?

The discount rate is where the judgment lives. Everything else is arithmetic. The arithmetic can be done by a spreadsheet; the judgment about what rate to apply to Sara's catering business, or to a startup, or to a bond, or to a capital project — that judgment is what the framework asks you to supply. The framework makes that judgment explicit, forces it onto the page, and then shows you how sensitive the answer is to the choice. That is the discipline. The rest is calculation.

---

*A note on what the chapter simplified.* The discount rate was chosen by appeal to "small private business risk" at 12% to 18%, without a formal method for arriving at either number. For public companies, the CAPM provides a more principled approach to the equity discount rate, building it from the risk-free rate, the equity risk premium, and the firm's beta. Chapter 9 develops that framework. For private cash flows like Sara's catering business, the CAPM does not apply cleanly — there is no observable beta — and practitioners use a build-up method (risk-free rate plus equity risk premium plus size premium plus company-specific premium) whose company-specific component is essentially judgment. The honest answer is: the discount rate is the most leveraged single input in any DCF, you defend it as carefully as you can, and you always sensitivity-test against alternatives. The math is precise. The rate is approximate. Any DCF whose answer hinges on a 1% difference in the discount rate is being asked to do work it cannot do.*

---

## Exercises

### Warm-up

**1.** You are offered $5,000 today or $6,500 in four years. The relevant discount rate is 7%. Compute the present value of $6,500 in four years. Which offer has higher present value, and by how much? *(Tests: basic discounting; PV formula with a single future cash flow.)*

**2.** A bond pays $80 per year for three years, then $1,080 in year four (the final coupon plus principal). The discount rate is 6%. Compute the present value of each cash flow, then sum them to find the bond's total present value. Is this bond worth more or less than $1,000 at face value, and why? *(Tests: discounting a multi-period cash flow stream; interpreting the result against a reference price.)*

**3.** Derive the perpetuity formula $\text{PV} = C/r$ by writing out the first four terms of the geometric series and showing how the convergence formula reduces the infinite sum. What condition on $r$ is required for the series to converge, and what does that condition mean economically? *(Tests: geometric series derivation of the perpetuity formula; connects the math to the economic intuition.)*

---

### Application

**4.** A project requires a $200,000 investment today and returns $60,000 per year for five years, with no terminal value. The hurdle rate is 10%. Compute the NPV and the IRR [approximate numerically or by trial]. Should the project be accepted? Now suppose the hurdle rate rises to 14% due to increased risk. Does the decision change? What does this tell you about the relationship between discount rate and NPV? *(Tests: NPV and IRR calculation; sensitivity of the accept/reject decision to the discount rate.)*

**5.** A local gym offers you a lifetime membership for $3,000 today, or annual dues of $350 per year. You expect to use the gym for at least 15 years. At a discount rate of 5%, which option has the lower present value cost? At what discount rate are the two options equivalent (i.e., what is the IRR of the "buy lifetime membership" decision)? *(Tests: comparing lump-sum vs. annuity cash flow structures; IRR as a break-even discount rate.)*

**6.** Sara's catering business model uses a 2% perpetual growth rate in the terminal value. Suppose you argue the growth rate should be 0% because the business has no pricing power. Recompute the terminal value at year 10 using $215,000 / (0.12 − 0) and recalculate the total enterprise value and NPV. How much of the original $916,000 NPV came from the growth assumption alone? *(Tests: sensitivity of terminal value to the growth rate; isolates a single assumption's contribution to the total valuation.)*

**7.** A startup offers you a revenue-share agreement: $0 for the first two years (pre-revenue), then $50,000 per year for years 3–7, then $100,000 per year in perpetuity starting year 8. At a discount rate of 15%, what is the present value of this agreement today? *(Tests: discounting a multi-stage cash flow structure with a deferred perpetuity; requires chaining PV operations across stages.)*

---

### Synthesis

**8.** The chapter argues that the sensitivity table is "where the analysis becomes useful rather than merely correct." Using Sara's deal as your example, explain why a single-point NPV of $916,000 can be misleading, and describe what a sensitivity table adds that the single-point NPV cannot show. What is the minimum information a decision-maker needs from a DCF analysis before acting on it? *(Tests: integrates NPV calculation, sensitivity analysis, and the chapter's core argument about the role of assumptions.)*

**9.** IRR and NPV almost always agree, but the chapter says to trust NPV when they conflict. Construct a concrete numerical example — two mutually exclusive projects with different sizes — where IRR ranks Project A above Project B but NPV ranks Project B above Project A. Explain why the NPV ranking is the correct one for a decision-maker trying to maximize value. *(Tests: IRR vs. NPV conflict; requires constructing an example rather than recalling one.)*

**10.** The chapter ends by claiming most of finance reduces to one operation: moving cash flows through time. Test this claim. Take two financial instruments from outside this chapter — a mortgage and a stock dividend stream — and show how their valuation reduces to the same discounting machinery developed here. Where, if anywhere, does the analogy break down? *(Tests: transfer of the core DCF framework to unfamiliar instruments; stress-tests the "one tool" claim.)*

---

### Challenge

**11.** The Gordon growth model requires $r > g$. What happens economically and mathematically when $g$ approaches $r$? What happens when $g > r$? Firms like NVDA have had periods where analysts used near-term growth rates of 30–40% — clearly above any plausible long-run discount rate. Describe the correct way to handle high near-term growth in a DCF model, and explain why using a single-stage growing perpetuity with $g > r$ produces a nonsensical result. *(Tests: limits of the Gordon growth model; pushes toward multi-stage DCF as the correct response to high near-term growth.)*

**12.** The chapter notes that "the discount rate is the most leveraged single input in any DCF." An adversarial reader might argue: if the answer is this sensitive to the discount rate, and the discount rate is ultimately judgment, then the DCF is not analysis — it is a sophisticated way of dressing up a conclusion you already reached. Write a response to this critique. Does the sensitivity of DCF to the discount rate undermine its usefulness, or is there a sense in which forcing the judgment onto the page is itself the value? Under what conditions is DCF most reliable, and under what conditions should it be treated with the most skepticism? *(Tests: epistemological limits of DCF; stress-tests the chapter's own framework against the strongest version of the objection.)*

---

*Tags: time value of money, discounting, compounding, NPV, IRR, perpetuity, Gordon growth model, sensitivity analysis, discount rate, terminal value*

---

###  LLM Exercise — Chapter 5: Time Value and DCF

**Project:** Maya's Memo, Built Across the Course
**What you're building this chapter:** The DCF Valuation section of the memo: a present-value model of the position, with the discount rate defended and a clean sensitivity table.
**Tool:** Claude Project

---

**The Prompt:**

```
I'm working on Maya's Memo for the position in `01-position-brief.md`. Sections so far: `02-return-risk.md`, `03-claim-framing.md`, `04-fund-vs-direct.md`.

Chapter 5 taught:
- **Present value** as the discounted sum of future cash flows
- **Discount rate** selection and why it matters more than any other assumption
- **Terminal value** via Gordon growth and why it usually dominates the answer
- **Payback-period intuition** (Sara's catering case) and why it systematically over-pays

Produce `05-dcf.md` containing:

1. **The cash-flow forecast.** A 5–10 year projection of the cash flow that accrues to your position. For an equity: free cash flow to equity (or dividends, if a stable payer). For a bond: the contractual coupon and principal stream. For a private business: forecast operating cash flow with explicit assumptions about growth, margin, and reinvestment. Show the full table.

2. **The discount rate, defended.** State the rate you're using and why. For a public equity: the cost of equity from CAPM (β × market risk premium + r_f) — even though Chapter 11 will refine β, do a rough cut now. For a bond: the YTM on a comparable-credit instrument. For a private business: the hurdle rate the buyer would accept, defended against alternative uses of the capital.

3. **The present value.** Compute the PV of the explicit forecast. Compute the terminal value (Gordon growth: $TV = CF_n \times (1+g) / (r - g)$, with $g$ defended). Discount the terminal value back. Sum to get the total present value.

4. **The sensitivity table.** A 5×5 table: discount rate on one axis (5 values around your central estimate), terminal growth on the other (5 values). Each cell is the resulting PV. *This is the most important table in the memo* — most disagreements about a DCF are disagreements about the corner values, not the math.

5. **Compare PV to current price.** State the implied margin of safety (or shortfall). One sentence: at this PV, the position is *attractive / fairly valued / expensive*. Name the corner of the sensitivity table that flips your recommendation.
```

---

**What this produces:** A markdown document `05-dcf.md` containing the cash-flow forecast, the discount-rate defense, the PV computation, the 5×5 sensitivity table, and the recommendation framing relative to the current price.

**How to adapt this prompt:**

- *For your own project:* Replace any bracketed domain placeholder with your specific instrument, ticker, or context. The exercise structure is instrument-agnostic; the content is yours.
- *For ChatGPT / Gemini:* Works as-is. For ChatGPT, save the running memo to a Custom GPT instead of a Claude Project. For Gemini, paste the project's accumulated section files into the context window each session.
- *For Claude Code:* Optional but useful — ask Claude Code to scaffold `analysis/05-dcf.py` so the sensitivity table re-runs with one command when you update assumptions.
- *For a Claude Project:* Append to the project. The DCF's central PV and the sensitivity-table corners become the *valuation* layer the capstone integrates.

**Connection to previous chapters:** Chapters 2–4 measured the position empirically and structurally; Chapter 5 produces the first defensible price for it.

**Preview of next chapter:** Chapter 6 asks whether a leveraged version of this position dominates the unleveraged one — and at what cost.

---

## AI Wayback Machine

The ideas in this chapter didn't appear from nowhere. **John Burr Williams** was publishing *The Theory of Investment Value* in 1938 — the foundational case that an asset's value is the present value of its future cash flows, formalized into the discount-rate apparatus the chapter teaches decades before most people had heard of the time value of money and discounted-cash-flow valuation. Here's a prompt to find out more — and then make it better.

![John Burr Williams, c. 1940s. AI-generated portrait based on a public domain photograph (Wikimedia Commons).](images/john-burr-williams.jpg)
*John Burr Williams, c. 1940s. AI-generated portrait based on a public domain photograph.*

**Run this:**

```
Who was John Burr Williams, and how does his 1938 dissertation *The Theory of Investment Value* — the foundational text on intrinsic value as the present value of future cash flows — connect to the chapter's apparatus of present value, discount rates, and discounted-cash-flow valuation? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.
```

→ Search **"John Burr Williams"** on Wikipedia after you run this. See what the model got right, got wrong, or left out.

**Now make the prompt better.** Try one of these:

- Ask it to explain why *intrinsic value* required a formal definition before 1938, in plain language
- Ask it to compare Williams's dividend-discount-model framing to the modern free-cash-flow-to-equity DCF the chapter teaches
- Add a constraint: "Answer as if you're writing the historical foundation paragraph for a DCF chapter"

What changes? What gets better? What gets worse?

