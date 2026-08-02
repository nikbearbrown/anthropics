# Chapter 7 — Options
*A price that doesn't depend on your forecast of the future — that is the strange thing.*

There is a strange thing that happens when you look at stock price graphs long enough. After a while you stop seeing the prices and start seeing shapes. Not shapes in the mystical chart-reading sense — I don't mean head-and-shoulders patterns or whatever the technical analysts are selling. I mean something more basic. You notice that wealth, when you own a stock, moves in a straight line with the stock. The slope is one. If the stock goes up a dollar, you go up a dollar. If it goes down a dollar, you go down a dollar. A straight line, slope one, through the origin of whatever coordinate system you draw.

This is almost the entire story of equity ownership. Boring. Symmetric. The line runs in both directions with equal indifference.

Now I want to show you that there is an entirely different class of financial instrument whose payoff is *not* a straight line — where the graph has a kink in it — and that kink turns out to be worth quite a lot of money to certain people. It is also, when you look at it carefully, something you already understand. You have probably bought this instrument before without knowing it had a name. And the strangest thing about pricing it is that the answer has almost nothing to do with what you think the future holds.

---

## Jin's Problem

Jin is a software engineer at a company that went public a year ago. He has $800,000 of stock that just unlocked. The stock has gone up a lot. He texts his friend Maya:

> *The lockup just ended. My financial planner says I should sell most of it. I want to. But the stock keeps going up and I think it has more room. I also can't bear the thought of it crashing 50% next month. Is there anything I can do besides hold or sell?*

What Jin is asking for, if you think about it carefully, is to be in two places at once. He wants to keep the upside if the stock keeps going. He wants to be off the hook if it crashes. These two desires are in obvious tension if all you can do is hold or sell. Holding gives you the upside but also the downside. Selling eliminates both. There is no way to construct "only the good half" from a straight line.

But there is a way to construct it from something that is not a straight line.

---

## The Kink

The instrument is called a put option. Here is what it is: a contract that gives you the right — but not the obligation — to sell shares of a specified stock to the contract writer, at a specified price called the strike, at any point before the contract expires.

Notice the asymmetry. This is the whole thing. You have the *right* to sell; the contract writer has the *obligation* to buy if you choose to exercise. You are not required to do anything. They are.

Watch what happens to your payoff at expiration as a function of the stock's price. If the stock is at $200 and your strike is $170, you don't exercise — you would be selling at $170 something the market will buy at $200. You let the contract expire worthless. Your payoff from the put: zero. If the stock is at $130 and your strike is $170, you do exercise — buy shares in the market at $130, sell them to the contract writer at $170, pocket $40 per share. More generally, the payoff is $\max(K - S, 0)$ per share, where $K$ is the strike and $S$ is the stock price at expiration.

<!-- → [CHART: Payoff diagrams — three panels on one axis; panel 1: long stock (straight line, slope 1); panel 2: put option payoff — flat at zero above strike K, rising linearly below K (hockey stick pointing upper-left); panel 3: long stock plus long put combined — slope-1 line above K, flat floor below K; label the kink at K in all three panels; caption: "The put introduces a kink that cannot be constructed from straight lines alone"] -->

Plot this. Above the strike, the payoff is flat at zero. Below the strike, the payoff rises linearly as the stock falls. There is a kink at the strike. The graph looks like a hockey stick lying on its side. And here is the key observation: you cannot make a hockey stick out of straight lines. No matter how you combine long and short positions in the stock itself, you will always get a straight line. The kink is genuinely new. It lives in a different mathematical family from everything you can do by simply owning or shorting the stock.

The mirror image is a call option — the right to *buy* at the strike. Calls have payoff $\max(S - K, 0)$: zero below the strike, rising above it. A different hockey stick, pointing the other way.

Jin's solution is now visible. He holds his stock and buys a put. Above the put's strike, the put expires worthless and he keeps all the upside. Below the strike, the put pays off, exactly offsetting his loss below that floor. The combined position has a floor at the strike and a ceiling at infinity.

You already know this structure. It is exactly insurance. The strike is the deductible — the loss you absorb before the policy pays out. The premium you pay for the put is the insurance premium. The expiration is your policy term. If you have ever bought homeowner's insurance, you have bought, in spirit, a protective put on your house. The structure is identical. Only the market is different.

Which brings us to the question that has been waiting since I described the contract: what does this cost?

---

## Why the Price Is Not an Opinion

This is where I want to slow down, because the answer is surprising, and the reason it is surprising is the most important thing in this chapter.

The price of a stock is an opinion. What is Apple worth? Reasonable analysts, looking at the same data, disagree by 20 or 30 percent. There is no formula that computes the right answer. It is a matter of judgment about future cash flows, competitive position, management quality — and people's judgments differ.

The price of an option on Apple, given Apple's current price and a few other observable inputs, is *not* an opinion in the same way. It is largely determined by mathematics. Not by any particular view of the future, but by the requirement that no one be able to make money out of nothing.

Let me show you why with the smallest version of the problem that still has all the interesting structure.

Forget the real market. Suppose there is a stock currently at $S = \$100$. One year from now, exactly one of two things will happen: the stock goes up to $\$120$, or it goes down to $\$80$. Nothing else. The risk-free rate is 5%, so a dollar today becomes $\$1.05$ a year from now.

Question: what is a fair price today for a call option with strike $\$100$, expiring in one year?

If the stock ends at $\$120$, the call pays $\$20$. If the stock ends at $\$80$, the call pays $\$0$. Most people's first instinct: estimate the probability of each outcome, take the expected payoff, discount it. "Let's say the stock has a 60% chance of going up. Expected payoff is $0.6 \times 20 = \$12$, discounted at the risk-free rate, the option is worth about $\$11.43$."

This reasoning feels right. It is wrong. The wrongness is not a technicality — it is the whole point.

Here is the right approach. Suppose I build a portfolio today consisting of $\Delta$ shares of the stock and $B$ dollars of bonds. If $B$ is negative, I am borrowing at the risk-free rate. What is this portfolio worth one year from now in each state?

If the stock goes up to $\$120$: the portfolio is worth $120\Delta + 1.05B$. If the stock goes down to $\$80$: the portfolio is worth $80\Delta + 1.05B$.

Can I choose $\Delta$ and $B$ so that this portfolio's payoff exactly matches the call's payoff in both states?

$$120\Delta + 1.05B = 20$$
$$80\Delta + 1.05B = 0$$

Two equations, two unknowns. Subtract the second from the first: $40\Delta = 20$, so $\Delta = 0.5$. Substitute back: $80(0.5) + 1.05B = 0$, giving $B = -40/1.05 \approx -\$38.10$. The negative sign means I am borrowing $\$38.10$.

The replicating portfolio is: long half a share of stock, borrow $\$38.10$ at the risk-free rate. What does it cost to assemble this today?

$$0.5 \times \$100 - \$38.10 = \$11.90$$

![One-step binomial tree for a call option ($100 → $120 or $80) alongside the replicating portfolio (0.5 shares − $38.10 borrowed) producing identical payoffs at $11.90](images/07-options-and-derivatives-fig-01.png)
*Figure 7.1 — Binomial tree and the replicating portfolio*

Now the punchline. This portfolio pays exactly $\$20$ if the stock goes up and exactly $\$0$ if the stock goes down — precisely what the call pays, in every possible future state of the world. Two things with identical payoffs in every state must have the same price today. If they did not, you could buy the cheaper one, sell the more expensive one, pocket the difference, and be guaranteed a profit regardless of what the stock does. Markets do not permit guaranteed profits from nothing — if they did, every trader would pile into the trade and drive the prices together. So the call must cost $\$11.90$.

Now stop and notice what did not appear in this calculation. The probability of the stock going up. Whether you think the stock has a 60% chance of going up or a 90% chance, the call still costs $\$11.90$. The price of the option is not a function of your beliefs about the future. It is a function of what the future *can* look like, what it costs to hold stock today, and the arithmetic of replication.

I want to be very clear about this because it is easy to nod at and miss. In almost every other corner of finance, the price of an asset depends on what you think the future holds — on opinions, on forecasts, on disagreements between well-informed people. Here, in the corner where derivatives live, the price falls out of an argument that does not require any forecast at all. That is strange. That is the thing worth understanding.

---

## From Two Branches to the Formula

The version I just showed you is a one-step binomial model — one period, two possible futures. You can extend it: split the year into two six-month periods, each with its own up-and-down branch. Then four three-month periods. Then twelve monthly periods. At each step you do the same replication calculation, working backwards through the tree. It gets tedious but never harder; the logic is the same recursion the whole way.

Take the limit. As the number of steps grows while each step shrinks, the binomial tree converges to a continuous process — geometric Brownian motion, the standard model for how stock prices move in continuous time. The replication argument holds in the limit, and the option price converges to the closed-form expression derived by Fischer Black and Myron Scholes in 1973.

A digression on the seventy-three-year arc, because the formula did not drop from the sky in 1973. In 1900, a student at the Sorbonne named Louis Bachelier defended a doctoral thesis titled *Théorie de la spéculation*, in which he derived — for the purpose of pricing options on French government bonds — essentially the model of stock prices as continuous random motion. The mathematics he used to describe it was the same mathematics physicists would borrow five years later to explain why pollen jiggles in water under a microscope. Henri Poincaré sat on Bachelier's committee. Poincaré gave the thesis a polite second-tier grade and a recommendation that did not lead to an academic job, because mathematical finance was not yet a respectable subject; the mathematics community of 1900 did not consider stock prices a domain worth its serious attention. Bachelier's work sat unread for half a century. In the 1950s the statistician Leonard Savage rediscovered it in a Yale library and sent a postcard to Paul Samuelson at MIT, asking whether Samuelson knew of this fellow Bachelier. Samuelson did not. He then did, and developed the line of work that Robert Merton and Fischer Black and Myron Scholes finished in 1973 — adding the no-arbitrage condition that gave the formula its distinctive uniqueness, and earning the 1997 Nobel Prize in Economics for the result. James Owen Weatherall tells the longer story in *The Physics of Wall Street* (2013). The short version is that the equation about to appear on the next line is the closed form of a model first written down in Paris before the airplane was invented. \[Verify: Bachelier 1900 thesis publication record; Savage-to-Samuelson postcard exact year.\]

The formula:

$$P = K e^{-rT} N(-d_2) - S \cdot N(-d_1)$$

for a European put, where

$$d_1 = \frac{\ln(S/K) + \bigl(r + \frac{1}{2}\sigma^2\bigr)T}{\sigma\sqrt{T}}, \qquad d_2 = d_1 - \sigma\sqrt{T}$$

$S$ is today's stock price. $K$ is the strike. $r$ is the risk-free rate. $T$ is time to expiration in years. $\sigma$ is the annualized volatility of the stock's returns — the only thing you have to estimate. $N(\cdot)$ is the standard normal cumulative distribution function, the area under the bell curve to the left of a given value.

| Symbol | Plain-English meaning | Observable or estimated | Where to find it |
|---|---|---|---|
| **$S$** — stock price | Current price of the underlying | **Observable** | Live quote from any broker or data feed |
| **$K$** — strike | Price at which the option holder can buy (call) or sell (put) | **Observable** | The option chain — the strike is contractual |
| **$r$** — risk-free rate | The continuously compounded risk-free rate over the life of the option | **Observable** | Treasury yield curve, matched to the option's maturity |
| **$T$** — time to expiration | Years remaining until the option expires | **Observable** | The expiration date, in calendar terms |
| ***$\sigma$ — volatility*** | The expected annualized standard deviation of the underlying's returns over the option's life | ***Estimated*** | Historical volatility of returns, OR (more commonly) the implied volatility back-solved from current option prices |

*Four inputs are observable right now. One — $\sigma$ — requires judgment. Notice what is missing: the expected return on the stock does not appear. The option's price does not depend on whether the stock is going up or down — only on how much it is going to move.*

Look at the inputs. Five of them. Four — $S$, $K$, $r$, $T$ — you can look up right now. Only $\sigma$ requires estimation. And notice again what is absent: the expected return on the stock, the probability that the stock goes up, any forecast of the future whatsoever. They drop out in the replication argument and stay dropped out in the continuous limit.

This is what I find so satisfying about derivative pricing. It is one of the few results in finance where you can invoke a single principle — no free money — and be forced to a specific number. Most of finance is about navigating honest disagreement between reasonable people with different views. This corner is about what disagreement is irrelevant to.

---

## Jin's Actual Calculation

Now we run the numbers. Suppose Jin holds 5,000 shares of AAPL at $\$185$ — about $\$925,000$ in total. He wants a floor at $\$170$ for the next six months.

Black-Scholes inputs: $S = 185$, $K = 170$, $r = 4.5\%$, $T = 0.5$ years, $\sigma = 25\%$ (a reasonable figure for AAPL; verify against current implied volatilities before trading).

Working through $d_1$: the numerator is $\ln(185/170) + (0.045 + 0.03125)(0.5) \approx 0.0846 + 0.0381 = 0.1227$. The denominator is $0.25\sqrt{0.5} \approx 0.1768$. So $d_1 \approx 0.694$ and $d_2 = 0.517$.

From the standard normal table: $N(-0.694) \approx 0.244$ and $N(-0.517) \approx 0.303$. The discount factor $e^{-0.045 \times 0.5} \approx 0.978$.

$$P = 170 \times 0.978 \times 0.303 - 185 \times 0.244 \approx 50.28 - 45.12 = \$5.16$$

A six-month put with strike $\$170$ costs about $\$5.16$ per share. To cover 5,000 shares, Jin needs 50 contracts (each covering 100 shares). Total premium: roughly $\$25,800$. Call it 2.8% of his $\$925,000$ position, or about 5.6% annualized.

That is what it costs to sleep.

If we open the actual option chain and look at the put with strike $\$170$ and six months to expiration, suppose we find a midpoint of $\$5.27$ (verify against current market). The gap between our formula and the market is about eleven cents — comfortably inside the bid-ask spread. The verification passes.

That gap is itself informative. We can run the formula in reverse: what value of $\sigma$ produces a Black-Scholes price of $\$5.27$? This is called the implied volatility, and it comes out to roughly 25.5%. The market is pricing in slightly higher volatility than our flat-vol assumption. This is real information — the market's collective current estimate of how volatile AAPL will be over the next six months. Professional options traders think and quote in implied volatility rather than in prices, because volatility is the only non-observable input, and disagreements about volatility are where all the interesting trading lives.

This also reveals something quietly important. There is no Platonic "true" option price floating in the sky waiting to be found. The formula is a consistency check — it tells you what price is consistent with a given volatility and the no-free-money principle. The market sets the price; the formula organizes it.

---

## What the Mathematics Doesn't Say

Here is what I want to say in closing, because it is the thing the calculation tends to bury.

We started with Jin, who wanted to be in two places at once. The mathematics shows that he can be — there is an instrument that provides a floor without giving up the ceiling, and we have priced it. The price falls out of the no-free-money argument, not from any opinion about Apple's future.

But the mathematics says nothing about whether Jin *should* do this.

The premium — 5.6% a year — is not free. Compounded over many years, systematic put protection is a serious drag on returns. Most people who carry protective puts as a permanent strategy pay for comfort they could have obtained more cheaply by simply reducing their exposure. Sometimes the right answer is to just sell. The Black-Scholes formula prices the contract; it does not tell you whether the contract is worth buying. Those are different questions, and only one of them has an objective answer.

What the mathematics gives you is a price, a structure, and a language for thinking about payoffs that are not straight lines. The surprising thing — the thing worth holding onto — is that this price is not an opinion. In almost every other corner of finance you are negotiating between forecasts. Here, in the thin strip of logic that runs from "no free money" through "replication" to the formula, you are not. The price is forced.

That is rare. That is what makes options worth understanding not just as instruments you might someday need, but as one of the few places where the machinery of markets becomes, briefly, transparent.

---

## What Would Change My Mind

The replication argument is airtight given its assumptions: continuous trading, no transaction costs, a stock price process that follows geometric Brownian motion, a known and constant volatility. The no-arbitrage conclusion — that the option price is forced — follows from these assumptions by pure logic.

What I would revise is the claim that Black-Scholes prices are close to fair value in practice. The constant-volatility assumption fails visibly: real option markets show that out-of-the-money puts trade at significantly higher implied volatilities than at-the-money options. This volatility skew reflects both the empirical fat tails of stock return distributions — large crashes happen more often than the lognormal model predicts — and the concentrated demand for downside protection from hedgers. Jin's put, struck below the current price, sits exactly where this skew bites hardest. The flat-vol calculation probably underestimates his real-world cost by 10–30%.

The logic survives. The constant-volatility assumption does not.

---

## Still Puzzling

The replication argument shows that the option's value doesn't depend on the probability of the stock going up or down — the probabilities simply don't appear in the price. But here is what puzzles me about this: you, as a buyer, presumably buy the put *because* you think there is a meaningful chance the stock falls below the strike. The seller presumably sells because they think that chance is small enough to be worth the premium. They disagree. Yet both are transacting at the same price, a price that required neither party's forecast to compute.

How can a price be simultaneously determined without anyone's probability estimate, and yet only transacted because the two parties hold different probability estimates? I find this philosophically strange. The no-arbitrage price is like a treaty — it says "you can't extract guaranteed money from this transaction," but it says nothing about what both parties believe, or whether either party is right. The market price clears. The beliefs underlying it don't have to.

I don't have a clean resolution. It is a feature of derivative markets generally: the pricing logic and the trading motivation operate at different levels of the argument, and they don't interfere with each other. But I find it worth sitting with.

---

*A note on what this chapter simplified.* Black-Scholes assumes constant volatility across all strikes and maturities. Real options markets show a volatility skew — out-of-the-money puts trade at higher implied volatilities than at-the-money options, reflecting demand for downside protection and the empirical fact that large stock drops happen more often than the lognormal model predicts. The skew-adjusted calculation, and why the skew exists, is a story for another chapter. The no-arbitrage argument at the heart of this chapter survives intact; it is the constant-volatility assumption that the real market violates, not the logic.

---

*Coming up.* We have priced an option using the requirement that no portfolio can generate guaranteed money from nothing. The same principle — no free money, enforced through replication — turns out to govern an enormous range of financial instruments beyond options. In Chapter 8 we apply it to forward contracts, futures, and the relationship between spot prices and expected future prices. The same argument, new instruments, stranger conclusions.

---

## Exercises

**Warm-up**

1. *(Payoff mechanics)* A put option has strike $K = \$150$ and expires in three months. For each of the following stock prices at expiration, calculate the payoff per share: (a) $\$180$, (b) $\$150$, (c) $\$120$, (d) $\$90$. Write the general formula and explain in one sentence why the payoff is never negative.

2. *(The kink)* The chapter claims you cannot construct a hockey-stick payoff from straight lines — no combination of long and short stock positions produces a kink. Explain in your own words why this is true. What geometric property of straight-line combinations makes the kink impossible without options?

3. *(Replication arithmetic)* Repeat the one-step binomial example from the chapter, but now price a *put* with strike $\$100$, using the same tree: stock goes up to $\$120$ or down to $\$80$, risk-free rate 5%. Set up the two equations, solve for $\Delta$ and $B$, and compute the put price. Note the sign of $\Delta$ — what does a negative delta mean in terms of what the replicating portfolio is doing?

**Application**

4. *(No-arbitrage logic)* Suppose someone offers to sell you the call from the chapter's binomial example for $\$9.00$ — below its no-arbitrage price of $\$11.90$. Describe the exact trade you would execute to lock in a guaranteed profit, state how much you would make, and explain why the profit is risk-free regardless of whether the stock goes up or down.

5. *(Black-Scholes inputs)* For each of the five Black-Scholes inputs — $S$, $K$, $r$, $T$, $\sigma$ — state whether it is observable or must be estimated, where you would find it or how you would estimate it, and give one reason why getting it wrong would cause the formula to misprice the option.

6. *(Implied volatility)* The chapter states that running the Black-Scholes formula in reverse — solving for $\sigma$ given the market price — produces the implied volatility. Explain in plain language what implied volatility measures, why professional traders quote options in volatility rather than in price, and what it would mean if a put option's implied volatility were substantially higher than a call option's implied volatility at the same strike.

7. *(Cost of protection)* Jin's six-month protective put costs 2.8% of his position, or 5.6% annualized. Suppose he holds the position for five years and rolls the put every six months, paying a similar premium each time. Assuming 7% annualized gross equity return, calculate his approximate net annualized return after the ongoing protection cost. Then explain, in one paragraph, the alternative strategy that the chapter suggests might achieve similar risk reduction at lower cost.

**Synthesis**

8. *(Pricing logic vs. trading motivation)* The chapter's "Still Puzzling" section raises a paradox: the option price is determined without anyone's probability forecast, yet the trade only occurs because buyer and seller hold different forecasts. Resolve this apparent paradox as clearly as you can. Your answer should distinguish between what the no-arbitrage argument establishes and what it leaves open, and explain why the two levels of the argument do not contradict each other.

9. *(Insurance analogy)* The chapter maps put options onto insurance contracts: strike = deductible, premium = insurance premium, expiration = policy term. Extend the analogy: what corresponds to the insurance concept of *moral hazard* in the context of a protective put? What corresponds to *adverse selection* — the tendency for people who need insurance most to buy it most? Does either concept create problems for the no-arbitrage pricing argument, or are they separate concerns?

**Challenge**

10. *(Stress-test the replication argument)* The no-arbitrage price is derived under assumptions the chapter acknowledges as false: continuous trading, no transaction costs, constant volatility. Pick one assumption, explain precisely how violating it undermines the replication argument, and describe what happens to the "forced" option price when the assumption fails. Does the price become indeterminate, or does it become a range rather than a point? What does this imply for how seriously practitioners should take the Black-Scholes number in illiquid or crisis markets?

---

###  LLM Exercise — Chapter 7: Options and Derivatives

**Project:** Maya's Memo, Built Across the Course
**What you're building this chapter:** The Option Overlay section of the memo: would an option-based position dominate the linear long or levered long, and what does the kinked payoff buy you?
**Tool:** Claude Project

---

**The Prompt:**

```
I'm working on Maya's Memo. Sections so far through Chapter 6 are in the project.

Chapter 7 taught:
- **The kinked payoff** — calls and puts as asymmetric claims
- **Intrinsic vs. time value**
- **The price barely depends on your forecast** — it depends on volatility, time to expiration, and rates
- **The Greeks** as the partial-derivative summary of how the option price changes

Produce `07-option-overlay.md` containing:

1. **Three candidate option overlays for this position.** Pick the three most defensible:
   - **Protective put**: long the stock, long an at-the-money put — capped downside, full upside, paid for in time premium
   - **Covered call**: long the stock, short an out-of-the-money call — collect premium, capped upside, full downside
   - **Long call as substitute**: long an at-the-money call instead of the stock — capped downside (the premium), uncapped upside, leveraged exposure to the stock's move

   For each, draw (in ASCII or markdown table) the payoff diagram at expiration.

2. **Pricing each.** For a public equity, look up the actual option chain. State the strike, the expiration, the bid-ask, the implied volatility. For a private business or a bond, simulate plausible parameters and label them as such.

3. **The expected-value comparison.** For each overlay vs. the linear long (Ch 6's unleveraged base case), compute the expected payoff under three scenarios: a base case, a 30% drawdown, a 30% rally. State which overlay dominates in which scenario.

4. **Volatility's role.** One paragraph. Why does the option price depend much more on volatility than on your forecast? What does this say about *when* an overlay is cheap vs. expensive — independent of your view on direction?

5. **The recommendation.** One paragraph. Which overlay (if any) belongs in the memo, against which scenario, with which expiration. The case for *no overlay* is also a defensible answer — name the volatility regime in which it is right.
```

---

**What this produces:** A markdown document `07-option-overlay.md` containing payoff diagrams for three candidate overlays, pricing for each, an expected-value comparison, and a recommendation that names the volatility regime supporting it.

**How to adapt this prompt:**

- *For your own project:* Replace any bracketed domain placeholder with your specific instrument, ticker, or context. The exercise structure is instrument-agnostic; the content is yours.
- *For ChatGPT / Gemini:* Works as-is. For ChatGPT, save the running memo to a Custom GPT instead of a Claude Project. For Gemini, paste the project's accumulated section files into the context window each session.
- *For Claude Code:* Optional — Claude Code can scaffold `analysis/07-option-pricing.py` using `py_vollib` for Black-Scholes pricing and the Greeks.
- *For a Claude Project:* Append to the project. The option-overlay decision is independent of the leverage decision (Ch 6) but combines with it in the integrated capstone (Ch 13).

**Connection to previous chapters:** Chapter 6 examined linear leverage; Chapter 7 examines whether the kinked payoff of an option dominates the linear case.

**Preview of next chapter:** Chapter 8 zooms out from the single position to the *diversification analysis* — how much of the risk in this position is idiosyncratic and how much is systematic?

---

## AI Wayback Machine

The ideas in this chapter didn't appear from nowhere. **Vinzenz Bronzin** was deriving option-pricing formulas in 1908 — sixty-five years before Black, Scholes, and Merton — in a German-language textbook that was rediscovered in 2002 and re-evaluated as parallel to the Black-Scholes apparatus decades before most people had heard of options pricing, the binomial model, and the Black-Scholes framework. Here's a prompt to find out more — and then make it better.

![Vinzenz Bronzin, c. 1900. AI-generated portrait based on a public domain photograph (Wikimedia Commons).](images/vinzenz-bronzin.jpg)
*Vinzenz Bronzin, c. 1900. AI-generated portrait based on a public domain photograph.*

**Run this:**

```
Who was Vinzenz Bronzin, and how does his 1908 *Theorie der Prämiengeschäfte* — derived parallel to and decades before Black-Scholes, but lost to history until 2002 — connect to the chapter's treatment of option pricing and the surprising stability of the underlying mathematics across rediscoveries? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.
```

→ Search **"Vinzenz Bronzin"** on Wikipedia after you run this. See what the model got right, got wrong, or left out.

**Now make the prompt better.** Try one of these:

- Ask it to explain why *option pricing kept getting reinvented* across the twentieth century, in plain language
- Ask it to compare Bronzin's 1908 derivation to the modern Black-Scholes formula the chapter introduces
- Add a constraint: "Answer as if you're writing a footnote in a chapter on option pricing"

What changes? What gets better? What gets worse?

