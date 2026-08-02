# Chapter 6 — Margin and Short Selling
*The borrowed thing doesn't move — and that's what makes it dangerous.*

Almost every financial blow-up you have heard of has leverage somewhere in its causal chain. Long-Term Capital Management. Lehman Brothers. Bill Hwang's Archegos. The Robinhood GameStop weekend. The instruments are always different. The mechanism is always the same.

I want to teach you the mechanism — not the vocabulary, not the regulatory details, not the cautionary tale framing — the actual mechanical thing that happens, step by step, in whose account, with whose money, when someone buys on margin or sells short. The reason to understand it precisely is not to avoid it. It is because leverage is one of the most useful tools in finance and one of the most dangerous, and the difference between those two outcomes is almost entirely whether you understood the mechanism before you used it.

---

Suppose you have $5,000 in a brokerage account and you want $10,000 of a stock. You could wait until you save another $5,000. Or you could ask your broker to lend you the other $5,000 against the stock as collateral.

That is a margin loan. The broker is willing to make it because the stock is collateral and they can sell it if you stop paying — and because the Federal Reserve's Regulation T has set the initial margin requirement at 50% for most equities since 1974, meaning they will lend you up to the value of what you put in. So $5,000 of yours buys $10,000 of stock: $5,000 of your cash plus a $5,000 loan from the broker.

Four numbers govern a margin account:

$$\text{Position value} = \text{your cash} + \text{broker's loan}$$
$$\text{Equity} = \text{position value} - \text{loan}$$
$$\text{Margin \%} = \frac{\text{equity}}{\text{position value}}$$
$$\text{Margin call price} = \frac{\text{loan}}{\text{shares} \times (1 - \text{maintenance margin})}$$

That last line is the one to memorize. It tells you the price at which the broker will call you. You should know this number for any position you hold on margin the way you know your own phone number.

Let me work through an example so the formula becomes intuitive rather than abstract. You buy 100 shares at $100 with 50% initial margin. Maintenance margin — the minimum you must maintain, set by FINRA Rule 4210 as a floor of 25%, with most brokers requiring 30% — is 30% in this example.

$$\text{Position value} = 100 \times \$100 = \$10{,}000$$
$$\text{Your cash} = \$5{,}000 \quad \text{Broker's loan} = \$5{,}000$$
$$\text{Equity} = \$10{,}000 - \$5{,}000 = \$5{,}000 \quad \text{Margin \%} = 50\%$$
$$\text{Margin call price} = \frac{\$5{,}000}{100 \times (1 - 0.30)} = \frac{\$5{,}000}{70} = \$71.43$$

You bought at $100. The margin call arrives at $71.43. That is a 28.6% decline. On Tesla, or any high-volatility stock, a 28% move is a matter of weeks, not years.

Here is what I want you to see clearly, because it is the entire personality of margin and it is what most people misunderstand.

The broker's loan is fixed. It stays at $5,000 regardless of what the stock does. The position value moves with the stock price. The equity — which is the gap between position value and the fixed loan — therefore moves *faster* than the position value, in percentage terms.

Watch it happen. Stock falls from $100 to $71.43.

- Position value: $10,000 → $7,143 (−28.6%)
- Loan: $5,000 → $5,000 (unchanged)
- Equity: $5,000 → $2,143 (−57.1%)

A 28.6% decline in the stock produces a 57.1% decline in your equity. That is the 2× leverage doing exactly what leverage does — but the direction matters. On the way down, the fixed loan means your equity moves roughly twice as fast as the stock.

Here is the critical misconception to name and bury: students often say "I have 50% initial margin, so I can absorb a 50% drop before I'm in trouble." This is wrong by a factor of nearly two, in the wrong direction. The 50% initial margin means you start at 50% equity-to-position. The margin call triggers at 30% equity-to-position — which, given that the loan is fixed, happens after roughly a 29% drop in the stock, not a 50% drop. The initial margin cushion is much thinner than it appears.

![Two side-by-side balance sheets for a margin account at entry vs. after a 28.6% drop in the underlying — equity falls 57%, the loan does not move](images/06-margin-and-short-selling-fig-01.png)
*Figure 6.1 — A 28.6% drop wipes out 57% of equity*

Beyond the margin call trigger price, there is a clock. Margin loans accrue interest daily — currently 6–10% annualized at retail brokers depending on the firm and balance size. The loan costs money every day you hold the position, whether the stock is moving in your favor or not. In practice the interest cost is secondary to the price movement on short timescales. On long timescales — holding a margin position through a six-month drawdown — the interest adds up.

The practical consequence of the margin call is the most important thing in this section, and it is not mathematical. It is this: the margin call removes your most valuable asset as an investor, which is time.

An unlevered investor who buys a stock at $100 that falls to $70 has a choice. They can hold and wait for the stock to recover. They have no deadline. The stock will recover, or it won't, and they will find out which on the market's schedule.

A levered investor who buys the same stock at $100 that falls to $71.43 does not have that choice. They receive a call on a Tuesday morning asking them to deposit cash by end of day or watch the broker sell their position. If they have no cash, their position is liquidated at $71.43 — and any subsequent recovery they would have captured instead becomes the next investor's gain.

Leverage compresses time. That compression is the core of what you need to understand about it.

---

Now suppose you don't own any Tesla and you want to profit when Tesla falls. There is no financial instrument called "the opposite of owning a stock." You cannot simply buy one. So you have to construct it.

Here is the construction. You borrow 100 shares of Tesla from someone who already owns them, sell those 100 shares in the open market right now, and receive the proceeds. Later, you buy 100 shares back and return them to the lender. If you bought them back cheaper than you sold them, you keep the difference. If more expensive, you pay the difference.

That is a short sale. The mechanism has been in use since at least the Dutch East India Company in the early 17th century — Joseph de la Vega's *Confusión de Confusiones*, published in 1688, describes recognizable short-selling mechanics. But it inverts the natural direction of every ordinary trade, which makes it confusing on first contact.

Your broker handles the logistics, but the process is worth knowing. When you place a short order, the broker has to *locate* shares to borrow. The most common source: another customer's margin account. Anyone holding shares in a margin account has signed an agreement — buried in the standard account documentation — allowing the broker to lend those shares to short sellers. The shares move from that customer's account to yours briefly, then to the buyer's account when you sell them. The original customer still shows their shares on their statement; they have a claim on equivalent shares plus a small fraction of the borrow fee you are paying.

The proceeds from the sale don't come to you as cash you can spend. Your broker holds them as collateral against your obligation to return the shares. You also post additional margin — the same 50% Reg T requirement — on top of the proceeds. So a $37,000 short generates $37,000 of proceeds held by the broker plus $18,500 of your own cash you have to post, for a total of $55,500 in the account securing your obligation to return the shares.

![Flow diagram of a short sale across four parties (Lender, Broker, Short Seller, Buyer), showing share flow, cash collateral, and the borrow fee](images/06-margin-and-short-selling-fig-02.png)
*Figure 6.2 — Short-sale mechanics*

Three things accumulate against you while the position is open.

Borrow fees. You pay the share lender an annualized rate for the privilege of using their shares. For liquid, heavily traded names like Apple or Microsoft, this might be a fraction of a percent. For hard-to-borrow names — stocks where many people want to short and lenders are scarce — the rate can be 20, 30, 50% or more annually. These rates are quoted daily and can change without notice. A position that costs 1% per year to borrow can become a position that costs 35% per year to borrow over a weekend, and you have no contractual protection against this.

Dividends. If the company pays a dividend while you are short, the buyer who purchased your borrowed shares is entitled to that dividend. Your broker reaches into your account and pays them — because you sold them the shares and they own the shares now. This is called a payment in lieu of dividend, and the mechanical effect is identical to a charge against your account.

Recall risk. The lender of the shares can recall them at any time, for any reason. If they do, your broker must either find you a new lender or force you to close the position — buying shares in the open market at whatever price is currently available, regardless of whether you want to exit. For widely held stocks this is rare. For squeezed names it happens at exactly the worst moment.

Three asymmetries make a short structurally different from a long in ways that matter.

A stock you own at $100 can fall to zero — maximum loss is 100%. A stock you are short at $100 can rise to any number: $200, $500, $1,000. Your loss tracks the stock dollar-for-dollar with no ceiling. Conversely, the maximum gain on a short is the stock falling to zero — a 100% gain on the proceeds, which means roughly a 200% return on the 50% margin you posted. The asymmetry is unfavorable in a way that the reverse isn't.

Carry costs compound against you. An unlevered long position costs almost nothing to hold. A short position pays borrow fees and dividends every day it is open. Time is the long investor's friend. It is the short seller's enemy.

And you fight the drift. The US equity market has gone up roughly two-thirds of all years since 1928. Short sellers fight against that upward drift every day they are positioned. Even when the short thesis is correct — the company is overvalued, the earnings will disappoint, the fraud will be exposed — the stock can drift up on the tide of general market appreciation while the short waits for the thesis to resolve. The carry costs accumulate the entire time.

Michael Burry is the canonical illustration of how this geometry can break a short seller who is right. Burry, a former neurologist running a hedge fund called Scion Capital out of San Jose, spent the back half of 2004 reading the prospectuses of subprime mortgage-backed securities the way most people read no document on earth, and concluded — well before the crisis became a phrase people used — that the underlying loans were so badly underwritten that the bonds had to default. Beginning in 2005, he bought credit-default swaps against the worst of them. The trade was structurally a short, with the same problem this chapter has been describing: he had to post collateral against the swaps, the swaps paid him nothing while the bonds kept performing, and his investors did not enjoy paying carry on a position the market disagreed with for two years running. By 2006 his investors were demanding their money back. He gated the fund — restricted withdrawals — to keep the position open. They sued. Some of them, with their lawyers' help, came close to forcing him to liquidate at a loss. He was right. They knew he was right by then; the data was visible. They wanted out anyway, because the path to being proven right was longer than their patience. The trade resolved in 2007 with a return that made Scion's surviving investors very wealthy. The lesson is not that you should imitate Burry. The lesson is that this is what it looks like when a short thesis is correct: the carry costs compound, the investors revolt, and the trade pays only after the structural geometry has nearly broken the trader. Michael Lewis tells the story at length in *The Big Short* (2010); the underlying economics are exactly what this section has been laying out, played out in real money. \[Verify: Burry's specific gating timeline; Scion 2007 returns from Lewis's reporting and from contemporaneous SEC filings.\]

---

Let me make the numbers concrete. You short 100 shares of Tesla at $370. Initial margin: 50%. Maintenance margin: 30%. Borrow fee: 3% annualized. Hold period: 6 months. Tesla pays no dividend.

Account setup:

$$\text{Short proceeds (held by broker)} = 100 \times \$370 = \$37{,}000$$
$$\text{Your margin} = \$18{,}500 \quad \text{Total in account} = \$55{,}500$$
$$\text{Carry cost over 6 months} = 0.03 \times 0.5 \times \$37{,}000 \approx \$555$$

The margin call trigger price for a short inverts the long formula:

$$\frac{\$55{,}500 - 100 \cdot P}{100 \cdot P} = 0.30$$
$$\$55{,}500 - 100P = 30P \implies P = \frac{\$55{,}500}{130} = \$426.92$$

If Tesla rises to $427, you get a margin call. That is a 15.4% adverse move from the $370 entry.

Fifteen point four percent. Tesla's 52-week range has historically spanned 70–80% from trough to peak. A 15% move is something Tesla can execute in a single week on good earnings news or a positive product announcement. The short seller's margin call is not a distant possibility — it is the kind of move that happens in ordinary market conditions.

| Tesla price | Position value | Account equity | P&L vs. entry | Return on $18,500 margin |
|---:|---:|---:|---:|---:|
| $250 | $25,000 | $30,500 | +$12,000 | +64.9% |
| $300 | $30,000 | $25,500 | +$7,000 | +37.8% |
| $370 | $37,000 | $18,500 | $0 | 0% |
| $420 | $42,000 | $13,500 | −$5,000 | −27.0% |
| $427 | $42,700 | $12,800 | (margin call) | (forced cover) |

<!-- → [CHART: P&L curve for the Tesla short, plotting return on initial margin (y-axis) against Tesla price (x-axis). Curve slopes downward right — gains accumulate as the stock falls, losses accumulate as it rises. Vertical reference lines at $370 (entry), $427 (margin call), and a lower price showing maximum gain territory. A horizontal dashed line at +200% marks the theoretical maximum. Overlay the mirror-image long P&L curve on the same axes — bounded below at −100%, extending upward without limit. The contrast makes the asymmetry visible.] -->

Three observations the table makes visible.

First, the leverage ratio works as advertised. A 32% fall in Tesla produces a 65% gain on the margin posted. A 14% rise produces a 27% loss. Every percentage move in the underlying becomes approximately a doubled percentage move in the equity.

Second, the asymmetry is real and large. The maximum theoretical gain is +200% (Tesla to zero). The loss at the margin call trigger is approximately 31%. The call mechanism caps the practical loss, but it also ends the trade — you are forced to cover at $427 whether you believe the thesis or not.

Third, the borrow fee at 3% annualized over six months comes to $555 — 3% of the initial margin, collected by the lender before the trade moves at all. If Tesla were a hard-to-borrow name at 25% annualized borrow, the carry over six months would be $4,625 — 25% of the initial margin, guaranteed to the lender win or lose. This is the silent enemy of short positions.

There is a dynamics point the table doesn't capture. When Tesla rises 15% and forces margin calls on short sellers, those short sellers must buy shares back to close their positions. Buying shares drives the price up further. Further price increases force more margin calls on other short sellers. More buying. More price increases. This is a short squeeze — a positive feedback loop with no natural stopping point until short positions are exhausted.

GameStop in January 2021 is the canonical example: the stock rose from roughly $20 to over $480 in weeks, driven partly by forced covering of heavily-shorted positions. Every short seller who was right about GameStop's long-term business prospects still lost money, because the squeeze forced them to cover at prices that made the thesis irrelevant. Being right about the company is not the same as surviving the path to being proven right. The margin call is indifferent to whether your analysis is correct.

<!-- → [INFOGRAPHIC: Timeline of the GameStop squeeze, January 4–28, 2021 — x-axis is date, y-axis is share price. Annotate key moments: short interest peak, first Reddit surge, Robinhood trading halt, price peak above $480, subsequent collapse. A second panel shows short interest percentage over the same period, declining as the squeeze forced covering. The visual point: the squeeze and the covering are the same event seen from two sides.] -->

---

Margin and short selling are professional tools that are also available to retail investors, and this combination requires honest discussion.

Margin is appropriate when the investor has high conviction, a defined exit, enough cash outside the position to meet a margin call without panic, and — crucially — the psychological capacity to sit through the drawdown that will test that conviction. Long-term investors using modest margin to amplify equity exposure over decades have, on average, been rewarded historically because the long-term drift of equity markets is positive and modest leverage compounds that drift. They have also been wiped out at scale during sharp drawdowns when forced to cover at the bottom. The historical record is: reward on average, ruin in the tail.

Margin is not appropriate if you cannot calmly write a check on Saturday morning to meet a Monday margin call. This is not a financial test. It is a psychological one. Leverage amplifies emotional pressure in exactly the same proportion as financial pressure. If your psychological response to a 20% market drop is to sell to stop the pain, margin will hurt you more than it helps, because it guarantees that the forced selling happens at precisely the wrong moment.

Short selling is appropriate when the investor has a specific, catalyst-driven thesis with a defined time horizon — this company will miss earnings on March 12 — can quantify and absorb the carry costs over that horizon, and has access to institutional infrastructure (stable borrow, prime broker relationships, robust risk management) that makes the position sustainable through volatility. Short positions are professional tools not because they are complicated but because they require professional infrastructure.

Short selling is not appropriate when the thesis is "this stock looks high." The history of that thesis is brutal. Every level at which Tesla "looked high" retired a succession of short sellers while the stock climbed further. "Looks high" is an aesthetic judgment. Without a catalyst that will force the market to reprice the stock within a defined window, the short bleeds carry costs while the market drifts upward around it.

---

Step back and look at what margin and short selling have in common.

Both are implementations of leverage — the use of borrowed resources to amplify exposure beyond what your own capital supports. The borrowed resource is money in the case of margin; it is shares in the case of shorting. In both cases, the borrowed resource does not move with the market. The loan is fixed at $5,000 whether the stock is at $100 or $70. The borrow obligation is 100 shares whether Tesla is at $370 or $470. The borrowed thing is an anchor, and your equity pivots around it as prices move.

This is why every major financial blow-up has leverage in its causal chain. It is not because leverage is inherently evil or because the people who used it were stupid — many were neither. It is because leverage converts the ordinary volatility of markets into a forced-selling event. Markets are volatile. Forced-selling events are not recoverable. The 1929 crash was a margin spiral. 2008 was mortgage-securitization leverage stacked five layers deep. Archegos was swap-based leverage that hid from prime brokers. The instrument changes; the mechanism does not.

The phrase I find most useful: leverage converts a survivable trade into an unsurvivable one. A drawdown that an unlevered investor experiences as a year of patience becomes, for a levered investor, a forty-eight-hour decision about whether they are still solvent. Most blown-up positions are not blown up by being wrong about the company. They are blown up by running out of time. And leverage is the device that creates the deadline.

Used carefully — modest size, defined exit, enough cash to absorb a call — leverage amplifies competence. Used carelessly, it amplifies anything, including your own confusion about why a position is moving against you.

---

*What would change my mind.* The chapter's skepticism about retail short selling rests on the empirical track record: retail short books have historically underperformed their corresponding long books, even before accounting for borrow fees and carry. If careful analysis demonstrated that retail investors with a specific type of disciplined, catalyst-driven short strategy outperformed over a long horizon, the warning about retail shorts would need to be requalified. I am also aware that the chapter is somewhat asymmetric in its treatment — margin gets a nuanced cost-benefit framing while short selling is presented with more caution. The asymmetry reflects the asymmetric risk geometry (capped upside, uncapped downside) and the structural carry costs, both of which work against shorts in a way that they don't against longs. Sophisticated short sellers who do it professionally disagree that this caution is warranted at appropriate position sizes with proper borrow management. They are not wrong. The chapter's framing is appropriate for the retail investor it is primarily written for.

*Still puzzling.* The chapter has not engaged with leveraged ETFs — 3× bull and 3× bear products that offer leverage without requiring a margin account. They appear to be a simpler path to the same exposure. They are not, for holding periods longer than a day. A 3× leveraged ETF rebalances daily to maintain 3× the underlying's daily return. This daily rebalancing introduces volatility decay: when the underlying is volatile, the compounding of daily returns over a holding period produces a result that is less than 3× the underlying's total period return, and can be significantly less. On a path where the underlying alternates between up 10% and down 10% days, the 3× ETF loses value even though the underlying is essentially flat over the full period. The longer you hold, the worse this decay becomes. The correct treatment requires Itô's lemma and path-dependent processes, which the book has not built up to yet. For now: treat leveraged ETFs as tools for short-term tactical trading, not as substitutes for margin in a long-term leveraged strategy.

---

*Coming up.* Margin and short selling produce linear leverage — every percentage move in the underlying becomes a magnified but still linear percentage move in your equity. The payoff is a straight line with a steeper slope. Chapter 7 introduces options, where the payoff becomes a curve. An option gives you the right but not the obligation to buy or sell at a fixed price — and the asymmetry of that right versus obligation is what produces the curve. The curve is what makes options the most powerful risk-shaping tool in public markets. Pricing the curve is the Black-Scholes problem, and we will work through it mechanically even without deriving it from scratch.

---

## Exercises

### Warm-up

**1.** You buy 200 shares of a stock at $80 using 50% initial margin. Your broker requires 30% maintenance margin. (a) Calculate your initial equity and loan balance. (b) Calculate the margin call trigger price. (c) How far does the stock have to fall, in percentage terms, before you receive the call? *(Tests: margin call formula, fixed-loan mechanics.)*

**2.** A stock you hold on margin falls from $80 to $64 — a 20% decline. Your initial margin was 50%. (a) What is your new equity-to-position percentage? (b) Are you above or below a 30% maintenance requirement? (c) How does the percentage loss on your equity compare to the percentage loss on the stock price? *(Tests: leverage amplification, equity vs. position value distinction.)*

**3.** You short 50 shares of a stock at $200. Initial margin is 50%. The stock pays a $2.00 annual dividend per share, paid quarterly. (a) How much cash do you post as margin? (b) What is the quarterly dividend payment that will be charged against your account? (c) If the borrow fee is 4% annualized, what is your annual carry cost in dollars? *(Tests: short account structure, carry cost components.)* 

### Application

**4.** You have $20,000 in cash and want maximum exposure to a $40 stock using 50% initial margin with 25% maintenance margin. (a) How many shares can you buy? (b) What is your margin call trigger price? (c) If the stock rises 40%, what is your return on the $20,000 you put in — and how does this compare to an unlevered purchase? *(Tests: leverage amplification on the upside, return-on-equity vs. return-on-position.)*

**5.** You short 100 shares of a stock at $150. Total account collateral (proceeds plus margin) is $22,500. Maintenance margin is 30%. (a) Derive the margin call trigger price for this short position. (b) How far does the stock have to rise, in percentage terms, to trigger the call? (c) You hold the position for 9 months at a borrow fee of 8% annualized. What is your total carry cost? *(Tests: short margin call formula, carry cost over a non-standard hold period.)*

**6.** A stock is trading at $100 with 40% of its float sold short. It announces better-than-expected earnings and rises 12% in a day. (a) Describe in mechanical terms what happens to the short sellers' margin accounts. (b) Why might the stock continue rising even after the initial 12% move? (c) What is the name for this dynamic, and what condition must be true for it to intensify? *(Tests: short squeeze mechanics, feedback loop identification.)*

### Synthesis

**7.** An investor holds an unlevered long position in a stock that falls 35% over six months. A second investor holds the same stock on 2× margin (50% initial margin) and faces a margin call at a 29% decline. Compare the two investors' situations at the six-month mark. What did each investor lose? What choices does each have? What does this illustrate about the relationship between leverage and time? *(Tests: margin call as a time-compression mechanism, unlevered vs. levered outcomes.)*

**8.** A short seller and a put option buyer both profit when a stock falls. (a) Describe two structural differences between the two positions — not just the payoff, but the mechanics of how each is constructed and what the holder owes during the holding period. (b) Which position has theoretically unlimited downside risk if the stock rises? (c) What does this comparison suggest about why a short seller might prefer to use put options instead? *(Tests: cross-chapter integration with Chapter 7 options preview; carry cost vs. premium structure.)*

**9.** The chapter argues that leverage converts a survivable trade into an unsurvivable one. Using the margin account mechanics from this chapter, construct a specific numerical example — not Tesla, not the textbook example — that demonstrates exactly how this conversion happens: start with the purchase price, initial margin, maintenance margin, the stock's subsequent price path, and identify the moment the trade becomes unsurvivable. *(Tests: full synthesis of margin mechanics applied to a novel scenario.)*

### Challenge

**10.** A leveraged ETF that promises 3× the daily return of an index opens at $100. Over four consecutive days, the index moves: +5%, −5%, +5%, −5%. (a) Calculate the index's value after four days. (b) Calculate the 3× ETF's value after four days, applying the 3× daily return each day. (c) Compare the ETF's total return to 3× the index's total return. (d) What is the name for the phenomenon that explains the gap, and why does it grow larger as holding periods extend? *(Tests: volatility decay in leveraged ETFs, compounding of daily returns, the "Still Puzzling" section.)*

---

###  LLM Exercise — Chapter 6: Margin and Short Selling

**Project:** Maya's Memo, Built Across the Course
**What you're building this chapter:** The Leverage Decision section of the memo: should this position be levered, and what does the margin-call price say about the size that survives a 30% drawdown?
**Tool:** Claude Project

---

**The Prompt:**

```
I'm working on Maya's Memo. Sections so far: `02-return-risk.md`, `03-claim-framing.md`, `04-fund-vs-direct.md`, `05-dcf.md`.

Chapter 6 taught the four margin numbers:
- **Position value** = cash + broker's loan
- **Equity** = position value − loan
- **Margin %** = equity / position value
- **Margin-call price** = loan / (shares × (1 − maintenance margin))

And the discipline: leverage amplifies both directions; the difference between useful and ruinous is whether you understood the mechanism before you used it.

Produce `06-leverage.md` containing:

1. **The unleveraged base case.** State the position size you would take with no margin. Reference Chapter 5's DCF and Chapter 4's fund-vs-direct call to defend the size.

2. **The leveraged variant.** Compute, at a chosen leverage ratio (1.5×, 2×, or 3×): position value, equity, margin %, margin-call price, the stock-price drawdown that triggers the margin call. *For a private business: substitute "the LBO debt covenant breach price" or the lender's call provision.*

3. **The 30% adverse-move test.** Suppose the position drops 30% from entry. For each candidate leverage ratio (1.5×, 2×, 3×), state whether the margin call fires. Report the size you can take at each leverage and survive the 30% move with margin to spare.

4. **The expected return on equity at each leverage.** Multiply the unleveraged expected return by the leverage ratio, subtract the broker's interest (state the rate). Compare the levered expected return to the unleveraged.

5. **The recommendation.** One paragraph. Lever / don't lever, at what ratio, with what stop-loss, against what specific risk. Reference the worked-out margin-call price as the binding constraint. The case against leverage is the LTCM/Archegos/GameStop sentence — name which scenario most closely resembles the failure mode this position is exposed to.
```

---

**What this produces:** A markdown document `06-leverage.md` containing the leverage decision, the four margin numbers at each candidate ratio, the 30% drawdown test, and a recommendation that names the binding constraint.

**How to adapt this prompt:**

- *For your own project:* Replace any bracketed domain placeholder with your specific instrument, ticker, or context. The exercise structure is instrument-agnostic; the content is yours.
- *For ChatGPT / Gemini:* Works as-is. For ChatGPT, save the running memo to a Custom GPT instead of a Claude Project. For Gemini, paste the project's accumulated section files into the context window each session.
- *For Claude Code:* Optional — Claude Code can scaffold `analysis/06-margin.py` that takes leverage, maintenance margin, and entry price and returns the margin-call price and the survivable drawdown.
- *For a Claude Project:* Append to the project. The leverage decision interacts with the diversification analysis (Ch 8) and the y* recommendation (Ch 10) — flag the linkage.

**Connection to previous chapters:** Chapter 5's DCF produced the price; Chapter 6 asks whether a leveraged version of the same position dominates the unleveraged one and at what risk.

**Preview of next chapter:** Chapter 7 asks whether an option overlay (a put hedge, a call substitute, a covered-call income trade) dominates the linear leverage move.

---

## AI Wayback Machine

The ideas in this chapter didn't appear from nowhere. **Hyman Minsky** was developing the *financial instability hypothesis* — the argument that stable financial conditions actively produce the leverage cycles that destabilize them decades before most people had heard of leverage, margin loans, and the mechanism by which short positions and borrowed money amplify both returns and ruin. Here's a prompt to find out more — and then make it better.

![Hyman Minsky, c. 1980s. AI-generated portrait based on a public domain photograph (Wikimedia Commons).](images/hyman-minsky.jpg)
*Hyman Minsky, c. 1980s. AI-generated portrait based on a public domain photograph.*

**Run this:**

```
Who was Hyman Minsky, and how does his *financial instability hypothesis* — that stability breeds the leverage that breaks stability — connect to the chapter's mechanical treatment of margin accounts, short positions, and the way leverage moves from useful tool to existential risk? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.
```

→ Search **"Hyman Minsky"** on Wikipedia after you run this. See what the model got right, got wrong, or left out.

**Now make the prompt better.** Try one of these:

- Ask it to explain *the Minsky moment* in plain language, as if you've never read macrofinance
- Ask it to compare Minsky's three borrower types (hedge, speculative, Ponzi) to the margin-account stages in this chapter
- Add a constraint: "Answer as if you're writing the warning section of a margin-lending policy"

What changes? What gets better? What gets worse?

