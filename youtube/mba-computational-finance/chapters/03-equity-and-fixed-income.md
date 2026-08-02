# Chapter 3 — Equity and Fixed Income


## TL;DR

- It is 4:17 on a Thursday afternoon and Maya is trying to leave the office.
- The chapter moves through LLM Exercise — Chapter 3: Equity and Fixed Income.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

It is 4:17 on a Thursday afternoon and Maya is trying to leave the office. She has her bag on her shoulder. Her laptop is half-closed. And then the boss forwards the thread.

The subject line says **Re: NVDA position**. The first message in the chain is from the CFO, who is the kind of person who writes "Sidebar" at the start of an email and means it.

> Sidebar from the NVDA conversation: the CFO is asking whether we should fund the position by issuing debt rather than dipping into the reserve. He thinks we could put out an Apple-style bond — investors would buy it. Cheaper than touching the reserve. What do you think?

The boss adds: *I don't actually know how to think about this. Help.*

Maya sits down. Closes the bag. Reopens the laptop properly.

The CFO is asking her to compare two financial instruments she has only ever considered separately — the equity claim represented by the proposed NVDA stock position and the debt claim represented by the proposed Apple-style bond. The two are different in ways that matter for the decision. They are also identical in ways that don't. She needs to know which is which before she can write a single sentence back.

---

Forget Apple for a moment. Imagine your cousin opens a coffee shop and asks you for ten thousand dollars.

There are two ways to give him the money.

The first way: you write him a check and he gives you a piece of paper saying you own 25% of the shop. The paper says: *if the shop distributes profits, you get a quarter. If it sells, you get a quarter of what remains after paying everyone else. If it goes bankrupt, you get whatever scraps survive after the lenders, the suppliers, and the IRS have taken theirs — which is usually nothing.*

The second way: you write him a check and he gives you a different piece of paper saying he will pay you $500 every year for ten years and return your $10,000 at the end. That paper also says: *if he doesn't pay, you can sue. You can put a lien on the espresso machine. You will be paid before any equity holder sees a cent.*

Same $10,000 in. Two completely different contracts.

The first is equity. The second is debt. Every stock you have ever heard of is the first contract, scaled up and standardized. Every bond is the second.

Notice what the contracts say and what they don't say. The equity contract does not promise you anything. It does not say *you will receive X dollars*. It says *if there is anything left over, you get a fractional share.* The Latin word is *residuus* — remaining. You are last in line, and what you receive is what remains.

The debt contract is full of promises. *I will pay $500 on this date. And another $500 on that date. And $10,000 on the final date.* These are not vague hopes. They are legal obligations, enforceable in court.

Three consequences follow from this difference, and almost everything in this chapter is an elaboration on these three.

The first is order of payment. When a company is doing well, it does not matter much — there is enough cash to pay everyone. When the company is in distress, it matters enormously. Bondholders are paid first. Equity holders are paid last. In bankruptcy, equity holders typically receive nothing. The phrase "wiped out" is almost always literally accurate. This is what residual claim means concretely: you are the residual, and when there is no residual, you are nothing.

The second is predictability. Bond cash flows are specified in the contract. You know what you will receive and when. The only uncertainty is whether the issuer actually pays — default risk — and in some bonds, whether they prepay early. Equity cash flows can be anything from zero to the company's entire enterprise value. The contract provides no answer.

The third is the shape of the upside. A bond's upside is capped. The contract says $500 per year and $10,000 back. It does not say *or more, if the coffee shop becomes Starbucks*. No matter how spectacularly your cousin succeeds, you receive the contracted amount and nothing more. The equity holder captures all of the upside above that. If he builds an empire, your 25% might be worth fifty million dollars.

Debt optimizes for predictability and legal priority. The price of that optimization is capped upside and exposure to interest rate movements. Equity optimizes for participation in whatever the business becomes. The price is going to the back of the line and accepting cash flows that are, contractually, zero.

I want to puncture one misconception before it hardens. People describe bonds as "safe" and stocks as "risky" and stop there. This is roughly true on average and badly false in detail. A 30-year bond can lose 40% of its market value in a single year if interest rates rise sharply. A diversified portfolio of stocks held for 30 years has, historically, almost always finished higher than where it started. The risk profiles are different, not simply ordered from one to the other.

---

The valuation question for a stock is: what is this contract worth?

The general answer is the same answer Chapter 1 gave for any stream of future payments — discount them back to today at a rate reflecting how risky they are. The hard part, and stocks are mostly hard part, is that the cash flows are not specified. The contract does not say what you will receive. You have to figure that out before you can discount it.

Two methods exist. They look different. They are the same idea wearing different clothes.

The first is called the Dividend Discount Model, and it applies to companies that pay regular dividends — Procter & Gamble, Coca-Cola, the old utilities and telecoms. For these companies, the cash flow you actually receive as a shareholder *is* the dividend. So the value of the stock is the present value of all future dividends, forever.

The simplest version is the Gordon Growth Model:

$$P = \frac{D_1}{r - g}$$

where $D_1$ is the dividend you will receive next year, $r$ is your required rate of return, and $g$ is the rate at which the dividend grows, forever. An infinite stream of dividends, growing every year, collapses to a single fraction. The mathematics is geometric series, and the infinite sum has a closed form as long as $r > g$.

Suppose Procter & Gamble pays a $4.00 dividend next year, you require an 8% return on a low-risk consumer staples stock, and you expect dividends to grow at 4% per year forever:

$$P = \frac{4.00}{0.08 - 0.04} = \frac{4.00}{0.04} = \$100$$

Three things are worth slowing down on.

First, the formula only works when $r > g$. If $r \leq g$, the denominator goes to zero or negative and the price explodes to infinity. Real companies do not have infinite value, so when the formula produces one, it is telling you that the assumption — dividends growing forever at rate $g$ — has broken down. The math is not being stupid; it is flagging that you are.

Second, the answer is brutally sensitive to $g$. Try $g = 5\%$ instead of 4%:

$$P = \frac{4.00}{0.08 - 0.05} = \frac{4.00}{0.03} = \$133$$

A one-percentage-point change in the perpetual growth rate moved the value by 33%. This sensitivity is not a flaw in the model. It is the model telling you, honestly, that your assumption about perpetual dividend growth is carrying enormous weight. Make it carefully.

Third, DDM only applies where dividends carry the value. Apple pays roughly $1.04 per share annually, a yield of about 0.38%. NVDA pays essentially nothing. Applying DDM to these companies produces a tiny number that has no connection to what the stock actually represents. The value is not in the dividend. It is in the much larger free cash flow the company is retaining, reinvesting, or returning through buybacks. For those companies, you need a discounted cash flow model.

A DCF for an equity claim has three components. First, you forecast free cash flow to equity for five to ten years — revenues, margins, capital expenditure, working capital changes. This is where most of the labor goes. Second, you calculate a terminal value: at year $n$, you can no longer project explicitly, so you summarize everything from year $n+1$ onward with a single number, usually the Gordon Growth formula applied to a long-run sustainable growth rate. Third, you discount all of it — the explicit cash flows and the terminal value — back to today.

The terminal value almost always accounts for 60 to 80% of the total, which means the DCF result depends heavily on a growth rate assumption that extends to infinity. A 1% change in the terminal growth rate moves a per-share value by 20% or more. This is not a bug. It is the honest statement that "what this company grows at forever" is a consequential assumption, and the model makes that consequence visible rather than hiding it inside a single price target.

The discipline is naming the assumptions rather than concealing them. DDM is honest where it applies and silent where it does not. DCF can value any company in principle but is exquisitely sensitive to inputs you cannot verify out of sample. The cash-flow shape of the company tells you which tool fits.

---

Now bonds — and here the mathematics is substantially cleaner, because the cash flows are specified in the contract rather than inferred.

A bond has three numbers built into it: the face value (almost always $1,000 for a corporate bond), the coupon rate (the percentage of face paid each year, typically in two semi-annual installments), and the maturity date (when you receive the face value back). The price you pay today is the present value of all the promised payments, discounted at the market's current required yield:

$$P = \sum_{t=1}^{n} \frac{C}{(1+r)^t} + \frac{F}{(1+r)^n}$$

where $C$ is the periodic coupon, $F$ is the face value, $r$ is the periodic discount rate, and $n$ is the total number of periods. In words: the price is the present value of every coupon you will receive, plus the present value of the principal returned at maturity.

This is where students encounter the most persistent confusion in fixed income, and I want to stop on it.

Yield to maturity — YTM — is not a feature engraved on the bond. It is not the coupon rate. It is the discount rate that makes the present value of all the bond's cash flows equal to its current market price. It is the implied return you would earn if you bought the bond today at its current price, held it to maturity, and the issuer paid every promised amount.

Think of it like an internal rate of return. You pay $P$ today, you receive coupons and principal over the life of the bond, and YTM is the single discount rate that reconciles the two sides. It bakes in three things simultaneously: the coupon income, the gain or loss from the bond's price moving toward face value at maturity, and the timing of all of it.

There is a simpler measure called current yield:

$$\text{Current yield} = \frac{\text{Annual coupon dollars}}{\text{Current price}}$$

Current yield tells you what coupon income you are collecting per dollar invested. It does not tell you your total return. A bond trading below face value has a current yield below its YTM, because the YTM also captures the price appreciation as the bond pulls toward face value over time. A bond trading above face has current yield above YTM for the opposite reason.

When a CFO says "we can issue at five percent," the correct question is: do you mean coupon rate, current yield, or YTM? All three can differ by hundreds of basis points on the same bond. Conflating them is a significant source of bad analysis.

Let me work through a real bond. In September 2019, Apple sold $1.5 billion of 2.95% Notes due September 11, 2049, coupon paid semi-annually. As of late April 2026, roughly 23.4 years remain to maturity. Suppose the market's required yield on long-dated high-grade corporate paper is about 5.0%.

The semi-annual coupon: $2.95\% \times \$1{,}000 / 2 = \$14.75$. The semi-annual discount rate: $5.0\% / 2 = 2.5\%$. The number of periods: approximately 47.

Present value of the coupons:

$$PV_{\text{coupons}} = 14.75 \times \frac{1 - (1.025)^{-47}}{0.025} \approx 14.75 \times 27.20 \approx \$401$$

Present value of the principal:

$$PV_{\text{face}} = \frac{1{,}000}{(1.025)^{47}} \approx \$306$$

Total price: approximately $\$707$ per $\$1{,}000$ of face — about 29% below par.

That sounds alarming from a bond that Apple has never come close to defaulting on. The discount is not about credit risk. It is arithmetic. The contract pays $14.75 every six months. The market currently thinks it should be paying something closer to $25 every six months, given prevailing rates. The $293 discount per $1,000 face is exactly the compensation for that gap, which the investor recovers as the bond's price climbs back toward face over the remaining 23 years.

Now notice the two yields. Current yield: $\$29.50 / \$707 \approx 4.17\%$. YTM: $5.0\%$. Same bond. The 83-basis-point gap is the average annual capital appreciation embedded in the bond's trajectory back to face value. The CFO who reports "Apple's 2049 bond yields 4.17%" is reading the coupon income per dollar invested. The actual all-in return for a buyer who holds to maturity is 5.0%. These are not interchangeable numbers.

The most under-appreciated fact about long bonds: they are extremely sensitive to interest rate movements. This bond has a duration of roughly 16 years, meaning a 1% rise in the yield causes the price to fall by approximately 16%. If long rates move from 5.0% to 6.0%, this bond — issued by one of the world's most creditworthy companies, with no default risk whatsoever — drops from $707 to roughly $625 per $1,000 face. An 11% loss on a bond from a top-rated issuer, in a single rate move.

The contract did not break. The market's valuation of the contract changed. This is the sense in which "bonds are safe" is incomplete. The contractual cash flows are safe, given no default. The price at which you can sell the bond before maturity is not safe at all.

---

Maya now lays out the head-to-head, using the same issuer for both sides to take credit quality off the table.

AAPL common stock at roughly $267. The AAPL 2.95% Notes due 2049 at roughly $70.70 per $100 of face, implying a YTM of about 5.0%.

The contractual cash flows for the stock are, strictly speaking, zero. Apple pays a quarterly dividend of about $0.26 per share, but the board can cut or eliminate it at any time. No court will force Apple to pay a dividend. The bond pays $14.75 every six months and $1,000 at maturity, full stop. If Apple fails to pay, bondholders have legal recourse. Equity holders do not.

Consider recession sensitivity. The stock falls — how much depends on the severity and whether Apple's business is directly affected. The bond price could rise (recessions often pull long rates down, which lifts long-bond prices), fall (if the recession is inflationary), or stay roughly flat. The two do not move in lockstep, which is the entire reason a balanced portfolio of stocks and bonds behaves differently from either alone.

Consider rising rate sensitivity. The stock can absorb moderate rate increases but suffers when higher rates compress earnings multiples — the present value of future cash flows falls when the discount rate rises. The bond's price falls mechanically, and with 16-year duration, every 1% rise in long rates knocks roughly 16% off the price.

The comparison makes the structural logic visible. The equity holder participates in Apple's success without a cap. The bondholder does not participate in Apple's success at all — the upside is fixed by contract — but sits ahead of the equity holder if something goes wrong. Both instruments are claims on the same underlying enterprise. They are different contracts designed for different kinds of investors with different priorities.

---

The CFO's question — *should we issue debt to fund the NVDA position* — is a financing question, not a valuation question. But you cannot answer the financing question without first understanding what the two contracts are. The firm's cost of capital is a weighted average of the cost of each contract. The cost of equity is different from the cost of debt, for reasons that now have names: residual versus senior claim, uncapped upside versus fixed promise, last in line versus first in line. You cannot compute the average until you understand what you are averaging.

There is a still deeper point here, and it is the one I want to end on.

Finance did not invent equity and debt arbitrarily. They are a structural solution to a structural problem. Capital providers vary in their tolerance for variance and their need for predictability. Some want priority and fixed promises and accept capped upside. Some want participation in whatever the enterprise becomes and accept going last. The two contracts carve the future cash flows of an enterprise into two complementary slices, each priced for a different type of investor. Everything else in finance — preferred stock, convertible bonds, structured products, options on either — is built from these two pieces, or sits somewhere on the spectrum between them.

Read the contract first. The mathematics, the risk profile, the appropriate valuation tool — they all follow from the cash-flow structure the contract creates. If you can specify the contract clearly, you can almost always pick the right tool to value it. If you can't specify the contract, you will reach for the wrong tool and not know why the answer feels wrong.

Maya can write the memo now. The CFO asked whether issuing debt is cheaper than touching the reserve. She can answer that question with a structure, not a guess.

---

*A note on what this chapter simplified.* The discount rate for equity — what Chapter 11 will formalize as the cost of equity — was treated here as a number you choose to reflect the riskiness of the cash flows. Choosing it properly requires either CAPM or a multifactor model, and those require variance, covariance, and the concept of the market portfolio, none of which are yet in place. The DDM and DCF mechanics are correct as presented; the discipline for choosing $r$ comes later. For bonds, the chapter assumed no call provisions, no embedded options, and no default — the clean case. Real corporate bonds often have all three, and each one requires modifications to the basic pricing formula.

---

###  LLM Exercise — Chapter 3: Equity and Fixed Income

**Project:** Maya's Memo, Built Across the Course
**What you're building this chapter:** The Equity-vs-Debt Framing section of the memo: what kind of claim is this position, and how does that claim structure shape the rest of the analysis?
**Tool:** Claude Project

---

**The Prompt:**

```
I'm working on Maya's Memo for the position in `01-position-brief.md`. The Chapter 2 return profile is in `02-return-risk.md`.

Chapter 3 distinguished:
- **Equity claim** — residual after all obligations; uncapped upside, full downside, voting / discretion over distributions
- **Debt claim** — fixed contractual cash flows; capped upside (par + coupon), prior claim in liquidation, priced from coupon, par, YTM, and maturity
- **Three different bond yields**: coupon rate, current yield, yield-to-maturity — and why they are not the same number

Produce `03-claim-framing.md` containing:

1. **What kind of claim is this?** Equity / debt / hybrid (preferred, convertible, mezzanine, MLP)? One paragraph naming the claim and listing the specific obligations and rights it carries (dividend, voting, conversion, seniority, callability).

2. **The bond / debt analysis (skip if pure equity).** If the position is debt or has a debt component: compute coupon rate, current yield, YTM. If you only have one of the three, work back to the others. State which yield is the right number for your decision and why. *For private business: substitute the implied yield on the seller-financing terms or the leveraged-buyout debt.*

3. **The equity analysis (skip if pure debt).** If the position is equity: name the equity story in two sentences. The story has a who-pays (operating cash) and a who-receives (residual after every other claim). What conditions would have to break for the residual to disappear? *For private business: identify the dominant operating-cash driver and the obligations senior to the equity holder.*

4. **The substitution test.** If your position is equity, name the bond a rational investor in the *same* company would prefer if the equity story breaks (the company's senior bonds, if any). If your position is debt, name the equity case a rational investor would prefer if the debt story is too cautious. The substitution test is what disciplines the framing.

5. **Implications for the rest of the memo.** Two sentences. Equity vs. debt structurally changes Chapter 6's leverage decision and Chapter 7's option overlay; name how.
```

---

**What this produces:** A markdown document `03-claim-framing.md` containing the claim type, the relevant yield calculation (or equity story), the substitution test, and the implications for downstream chapters.

**How to adapt this prompt:**

- *For your own project:* Replace any bracketed domain placeholder with your specific instrument, ticker, or context. The exercise structure is instrument-agnostic; the content is yours.
- *For ChatGPT / Gemini:* Works as-is. For ChatGPT, save the running memo to a Custom GPT instead of a Claude Project. For Gemini, paste the project's accumulated section files into the context window each session.
- *For Claude Code:* Not needed for this section.
- *For a Claude Project:* Append to the project. The claim type drives several downstream decisions — surface it in the project's running notes so each subsequent chapter inherits the framing.

**Connection to previous chapters:** Chapter 2 measured the position's empirical risk and return; Chapter 3 names the claim structure that produces that profile.

**Preview of next chapter:** Chapter 4 produces the *fund-vs-direct decision* section: would an ETF or fund dominate the case for direct ownership of this specific position?

---

##  AI Wayback Machine
The ideas in this chapter didn't appear from nowhere. **Frederick Macaulay** was introducing the bond-duration concept in 1938 — the single number that makes interest-rate risk on a fixed-income security legible decades before most people had heard of bond pricing, yield-to-maturity, and the structure of interest-rate risk. Here's a prompt to find out more — and then make it better.

![Frederick Macaulay, c. 1930s. AI-generated portrait based on a public domain photograph (Wikimedia Commons).](images/frederick-macaulay.jpg)
*Frederick Macaulay, c. 1930s. AI-generated portrait based on a public domain photograph.*

**Run this:**

```
Who was Frederick Macaulay, and how does his 1938 introduction of *duration* — the cash-flow-weighted average time to receipt — connect to the chapter's treatment of bond pricing and the way fixed income's risk is fundamentally different from equity's? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.
```

→ Search **"Frederick Macaulay"** on Wikipedia after you run this. See what the model got right, got wrong, or left out.

**Now make the prompt better.** Try one of these:

- Ask it to explain *Macaulay duration* in plain language, as if you've never seen a bond yield curve
- Ask it to compare Macaulay's duration to the modern *modified duration* and *convexity* concepts the chapter introduces
- Add a constraint: "Answer as if you're writing the rationale for why fixed-income risk needs its own metric"

What changes? What gets better? What gets worse?

