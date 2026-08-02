> **Voice status:** `voice-unanchored`. The workshop's root `style/` and this book's `books/intro-finance/style/` are both empty. Calibrate voice review accordingly.

---

## Suggested titles

1. **Equity Securities: Claims, Control, and the Architecture of Ownership**
2. **The $5 Billion Puzzle: Why Buffett Bought Preferred**
3. **What You Actually Own When You Own Stock**

---

## TL;DR

Every equity security is a bundle of three separable claims — on a company's income, on its remaining assets if it fails, and on how it's run — and the bundle, not the name, is what tells you what the instrument is for. Common stock, preferred stock, and dual-class structures are different solutions to the same allocation problem; once you see the bundles, the puzzles (including why Warren Buffett bought *preferred* stock in Goldman Sachs in 2008) stop being puzzles.

---

## Learning objectives

By the end of this chapter you should be able to:

1. Explain why common stockholders are called *residual* claimants, and how that status determines both their upside and their downside.
2. Compute the four foundational equity metrics — market capitalization, P/E, P/B, dividend yield — for any publicly traded company, and name at least one circumstance where each metric misleads.
3. Identify a dual-class share structure and explain the trade the founder is making when adopting one.
4. Distinguish common from preferred stock across six dimensions: claim priority, dividend rights, voting rights, price behavior, risk, and typical holder.
5. Value a non-callable preferred stock with the perpetuity formula and explain three ways the formula breaks.
6. Describe at least two business situations in which preferred stock is the right instrument to issue, with real historical examples.

## Prerequisites

Time value of money (Chapter 2), basic financial-statement literacy (income statement, balance sheet, EPS, book value), and Python at the level of reading and modifying a function (Appendix A).

## Where this chapter fits

Chapter 2 gave you present value. This chapter introduces the *instruments* that present-value mechanics get applied to. Chapter 4 takes the ownership structure you build here and runs full valuation models — DDM, DCF, multiples — against it. You can't value a claim until you know what's being claimed. This chapter is what's being claimed.

---

## 3.1 The $5 billion puzzle

In September 2008, with the financial system collapsing in real time, Warren Buffett wired $5 billion to Goldman Sachs. A month later he did something similar with General Electric. Three years after that, he put another $5 billion into Bank of America. Each time, the headlines called it a vote of confidence in American capitalism.

Here's the part most retellings skip. Buffett didn't buy common stock in any of those deals. He bought **preferred stock**.

This should strike you as strange. Buffett is the most famous common-equity investor in history. He runs a company whose annual letters argue, year after year, that long-term ownership of high-quality businesses through *common* shares is the best wealth-building strategy ever devised. And when the single biggest opportunity of his career showed up — American banks trading at pennies on the dollar — he passed on the common stock and took the preferred.

Why?

That question is the chapter.

The answer has nothing to do with Buffett being clever (he was) and everything to do with what preferred stock actually *is*. Preferred stock is not a weaker version of common stock. It is not a stronger version of a bond. It is a different instrument that solves a different problem, and until you understand what problem it solves, the Buffett deals look like a quirk rather than a blueprint.

By the end of the chapter, you'll see that every equity security is a bundle of three separate things: a claim on income, a claim on remaining assets if the firm fails, and a say in how the firm is run. Common stock bundles them one way. Preferred stock bundles them another. The whole rest of the chapter is about why those bundles exist and how to value them.

---

## 3.2 The residual claim — what you actually own

The word "stockholder" suggests something clean and simple. You own shares. You own a piece of the company. End of story.

That story is wrong in a specific and important way.

When you own common stock, you do not own a piece of the company's assets. You own a claim on whatever is left after everyone else has been paid. The word *residual* is doing a lot of work. It means: last in line.

### The capital stack

Every company that has raised outside money has a **capital stack** — an ordering of who gets paid in what order when cash comes in or when the firm shuts down. The order is fixed by contract and by [bankruptcy law](https://www.law.cornell.edu/uscode/text/11), and it matters enormously.

Top to bottom:

1. **Secured creditors** — lenders who lent against specific collateral (a mortgage, equipment financing). On failure, they have a claim on the collateral itself.
2. **Senior unsecured creditors** — bondholders whose debt isn't tied to specific assets but has contractual priority over junior debt.
3. **Subordinated creditors** — lenders who explicitly agreed to be paid only after seniors are satisfied. They took more risk in exchange for higher rates.
4. **Preferred stockholders** — above common, below all debt.
5. **Common stockholders** — you, if you bought the stock. Everyone above gets paid first. You get whatever is left, if anything.

When a healthy company is generating profit, this ordering doesn't feel relevant. Interest is paid, preferred dividends are paid, and there's plenty left for common. The stack is invisible.

In bad times it becomes the only thing that matters.

### The liquidation waterfall, on the page

Imagine a hypothetical company. Total obligations on a bad day:

- $40M in senior secured debt
- $30M in senior unsecured bonds
- $15M in subordinated debt
- $10M in preferred stock at par
- Common stockholders own the rest

Suppose the liquidation actually raises $80M. Walk through it on the page.

| Claimant | Claim | Receives | Loss |
|---|---|---|---|
| Secured | $40M | $40M | $0 |
| Senior unsecured | $30M | $30M | $0 |
| Subordinated | $15M | $10M | $5M |
| Preferred | $10M | $0 | $10M |
| Common | residual | $0 | everything |

The common stockholders nominally "owned" the company. In liquidation, they received nothing.

That is the residual claim made concrete. The flip side is the upside. If the same company's value grows from $100M to $500M, the incremental $400M belongs entirely to common shareholders, because every other claimant is capped at their contractual amount. Limited contractual rights in exchange for unbounded participation. That is the design of common equity.

The residual claim is also why common stocks have historically returned roughly 7% above inflation while long-term Treasuries have returned about 2% (see [Damodaran's historical series, 1928–](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/histretSP.html)). The extra return is not a gift. It's compensation for sitting at the bottom of the stack.

### A common misconception worth defusing

You'll hear "shareholders own the company" said casually. It is wrong in a way that matters.

Shareholders own *shares*. Shares confer specific rights — a residual claim on assets, voting on certain matters, the right to receive dividends *if* the board declares them. The rights are bounded. A shareholder cannot walk into a Tesla factory and demand a car as their pro-rata share of inventory. Their claim runs through the legal fiction of the corporation, and that fiction intermediates everything.

Why does this matter? Because when a CEO does something that seems to harm shareholders — cuts the dividend, makes a hated acquisition, issues more stock — the right question is not "why are they allowed to do that?" but "what are shareholders contractually entitled to, and what are they not?" Most of the time, the answer is: very little. Their main weapon is the vote — the subject of §3.3.

### Calculating what you own

Four numbers are the starting point for any equity analysis. Put them on the page:

$$\text{Market Cap} = \text{Shares Outstanding} \times \text{Price per Share}$$

$$P/E = \frac{\text{Price}}{\text{EPS}} \qquad P/B = \frac{\text{Price}}{\text{Book Value per Share}} \qquad \text{Dividend Yield} = \frac{\text{Annual Dividend}}{\text{Price}}$$

A company with 2.4B shares at $175 has a $420B market cap — what the market is saying the residual claim is worth, collectively. A P/E of 20 says investors are paying $20 for each $1 of current earnings. A P/B of 3 says the market values the company at three times what its balance sheet says equity is worth. A 3% dividend yield says cash dividends alone return 3% per year at the current price.

In Python, the minimum honest implementation:

```python
def equity_metrics(price, eps, book_value, dividend, shares_out):
    """Compute the four foundational equity metrics for one ticker."""
    return {
        "market_cap_billions": price * shares_out / 1e9,
        "pe_ratio": price / eps if eps > 0 else None,
        "pb_ratio": price / book_value if book_value > 0 else None,
        "dividend_yield_pct": (dividend / price) * 100 if price > 0 else None,
    }
```

Notice what the guards do. EPS guard: a P/E ratio on a loss-making company is not a ratio, it's a trap; `None` is more honest than a negative number. Book value guard: handles companies (often heavily leveraged) with negative book equity. Short functions, honest guards, clear inputs. The mega-class you'll see in production code comes later, after the concepts are built up piece by piece.

The calculation is the easy part. The hard part is knowing what a P/E of 42 means for *a specific company* in *a specific industry* at *a specific point in its history*. P/E is nearly meaningless for an early-stage biotech with no profits. P/B is a weak signal for a software firm whose primary assets are code and talent, neither of which lives on the balance sheet. The numbers do not interpret themselves. They tell you where to start asking.

---

## 3.3 Voting rights — what control actually means

The second claim bundled into a share of common stock is governance: the right to vote. Most casual discussion treats voting as a minor technical feature. It isn't. Control rights are one of the most important design variables in corporate finance.

### One share, one vote

For most of the twentieth century, U.S. public companies followed a simple rule: each share of common stock carried one vote. The NYSE [enforced it](https://www.sec.gov/divisions/marketreg/mrlistingstandard1994.htm) for listed firms. The idea was tidy and aligned: more economic exposure, more say.

Under one-share-one-vote, shareholder voting matters in three main situations: electing the board (who hires the CEO), approving major transactions (mergers, sale of the company, large new issuance), and voting on shareholder proposals. The theory is that if management underperforms, shareholders can vote them out. In practice, this rarely happens — when shareholdings are dispersed across thousands of passive investors, no individual investor has the incentive to spend time and money running a proxy fight. This is the **collective action problem**, and it's why corporate governance looks the way it does.

### The dual-class alternative

Starting in the 1990s and accelerating after 2010, particularly for founder-led tech companies, a different model took hold. In a **dual-class structure**, two classes of common stock exist with identical economic rights but different voting rights.

Three live examples:

- **Meta Platforms.** Class A carries one vote; Class B carries ten. Class B is held almost entirely by Mark Zuckerberg and a small group of insiders. The result: Zuckerberg controls roughly [61% of Meta's voting power](https://www.sec.gov/Archives/edgar/data/1326801/000132680125000018/0001326801-25-000018-index.htm) while owning about 13% of the economic value.
- **Alphabet.** A three-class structure: Class A (`GOOGL`) carries one vote, Class B carries ten and is held by Larry Page and Sergey Brin, Class C (`GOOG`) carries zero. The two founders control the company through Class B.
- **Berkshire Hathaway.** Class A (`BRK.A`) has full voting rights and trades for hundreds of thousands of dollars apiece. Class B (`BRK.B`) was [introduced in 1996 and adjusted by the 2010 50-for-1 split](https://www.berkshirehathaway.com/sharehold.html) to carry **1/1,500th of the economic rights** but only **1/10,000th of the voting rights** of Class A. Note the asymmetry: B-share economic exposure is *not* the same fraction as B-share voting power. This was designed deliberately so retail investors could buy Berkshire without diluting Class A control.

Why would a founder choose this structure? To raise capital without giving up control. In a one-share-one-vote world, a founder who sells down to 15% ownership retains 15% voting power and can be outvoted by a coalition. A dual-class structure decouples economics from control: the founder can sell most of the economic value and still control the votes.

The trade for public shareholders is the mirror image. You give up meaningful voting power. In exchange, you get access to companies run by founders with long horizons and strong convictions, who (the argument goes) make fewer short-term decisions to chase quarterly earnings. Whether the trade is good depends on the founder. Meta under Zuckerberg pivoted to mobile, bought Instagram and WhatsApp, and bet tens of billions on VR — bets that looked foolish when made and shaped the company. Other dual-class companies have used founder control to enable self-dealing or strategic paralysis. The structure optimizes for founder conviction at the cost of shareholder discipline. That is neither inherently good nor inherently bad. It depends on the founder.

### Computing voting power vs. economic exposure

A hypothetical illustration. A dual-class company has 800M Class A shares (1 vote each, public) and 200M Class B shares (10 votes each, founder).

- Total shares: 1B. Founder owns 200M = **20% of economics**.
- Total votes: 800M + (200M × 10) = 2.8B. Founder controls 2B = **71.4% of votes**.

With 20% of the economic value, the founder holds 71.4% of the voting power. They cannot be outvoted by any coalition of Class A shareholders.

The general lesson: voting multipliers create huge leverage between economic and control rights. When you read "the founder owns 20% of the company," in a dual-class structure that number tells you nothing about who is actually in charge.

---

## 3.4 Preferred stock — a hybrid for a specific problem

Now we can return to the puzzle. Why preferred and not common?

To answer, you need to understand what preferred stock actually is — not as a watered-down "stock with a fixed dividend" but as a specific instrument designed to solve a specific problem.

### The six characteristics

A typical share of preferred stock has the following features:

1. **Fixed dividend, paid before common dividends.** A preferred share might pay $5 per year on $100 par. That payment must clear before any common dividend is declared.
2. **Priority in liquidation over common.** On failure, preferred is paid before common — but still after all debt.
3. **Limited or no voting rights, normally.** Preferred holders typically can't vote in director elections. Voting rights often kick in only after a specified number of dividend payments are missed.
4. **Often cumulative.** If the company skips a preferred dividend, the missed payments accumulate and must be paid in full before common dividends can resume. This is the most important protective feature.
5. **Often callable.** The company can redeem at a set price (often par plus a small premium) after a specified date. The call caps the upside for the holder.
6. **No maturity date, typically.** Preferred is perpetual in most cases. There's no automatic return-of-principal date.

Read the six together and the instrument's character emerges: preferred stock is roughly *a perpetual bond with more risk and weaker legal protection*. The dividend is fixed like a coupon but isn't a contractual obligation — the board can skip it (they just can't pay common dividends until they catch up, for cumulative preferred). Liquidation priority is real but sits below all debt. There is no maturity date to guarantee return of principal.

### Valuing a non-callable preferred — the deep dive

Because the dividend is fixed and the security is perpetual, a non-callable preferred behaves mathematically like a perpetuity. The valuation formula is the simplest in finance:

$$P_0 = \frac{D}{r}$$

where $P_0$ is the value, $D$ is the annual dividend, $r$ is the required rate of return for a security of this risk.

Worked example. A preferred share pays $6 annually. The required return for similar-quality preferred is 6.5%. What is it worth?

$$P_0 = \frac{\$6}{0.065} \approx \$92.31$$

Sanity check: $6 forever, discounted at 6.5%. The price of $92.31 yields exactly $6 / $92.31 = 6.5%. The math checks out.

Now look at the formula carefully. It assumes two things, and both can break:

- *Dividend is paid every year forever.* In financial distress the board can skip the dividend. The actual cash flow then falls below $D$, and the formula overvalues the security. The riskier the issuer, the more this matters.
- *Discount rate $r$ is stable.* If interest rates rise sharply, $r$ rises, and the price of a fixed-dividend perpetual security falls mechanically — by a lot, because the security has no maturity to "pull it back" toward par. (You'll meet this idea formally as **duration** in Chapter 7. Perpetuities have effectively infinite duration.)

For callable preferred, a third break: the call feature caps the upside. If $r$ falls and the formula price rises above the call price, the issuer simply calls and the price never gets there. The formula then gives an *upper bound*, not a fair value.

A minimal Python implementation:

```python
def preferred_perpetuity_value(annual_dividend, required_return):
    """Value a non-callable preferred via the perpetuity formula.

    Returns the upper bound when the security is actually callable;
    extend with call logic separately.
    """
    if required_return <= 0:
        raise ValueError("Required return must be positive.")
    return annual_dividend / required_return
```

Notice what's *not* in this function: no logic for callable, cumulative, or credit-adjustment features. Those additions come next, as separate functions, because folding them all into one monolithic call makes the learning harder, not easier. Build the simple case. Understand why it works. Then extend.

### Why companies issue preferred stock

If preferred is worse for investors than either debt (which has legal claims) or common (which has uncapped upside), why does anyone issue it?

The answer depends on the issuer. Three cases cover most of the market.

**Case 1 — Banks and regulatory capital.** Bank regulators require banks to hold "capital" — money that absorbs losses before depositors and senior creditors do. Common equity is the best capital because it absorbs the most. It is also the most expensive to raise. Preferred stock counts as regulatory capital ([Additional Tier 1, in the Basel framework](https://www.bis.org/bcbs/publ/d424.htm)) while being cheaper than common on several dimensions, including voting dilution. This is why large banks — Bank of America, JPMorgan, Wells Fargo — all carry tens of billions of dollars of preferred. It is a *capital* instrument, not a financing instrument.

**Case 2 — Companies in distress, raising outside capital.** This is the Buffett case. In September 2008, Goldman Sachs needed capital urgently. Buffett would not commit $5B without downside protection — common stock offered none. Preferred let Goldman raise capital without giving up voting control and let Buffett lock in a 10% dividend with liquidation priority over common. Goldman also gave Buffett warrants (options to buy common at a set price), which created upside if the stock recovered. The structure matched the need.

**Case 3 — Utilities and mature companies with stable cash flows.** Utilities can predict revenues years in advance. They issue preferred to raise long-term capital at costs slightly above debt but without debt's legal obligations. In a bad year, they can skip the preferred dividend (which also blocks common dividends) without triggering default. The flexibility has value even when rarely exercised.

### Who buys it

Insurance companies are the biggest institutional buyers — long-term, predictable liability streams (annuities, life policies) match well to preferred dividends from investment-grade banks and utilities. Pension funds buy preferred for the same duration-matching reason. Some retail income investors buy it in retirement accounts where current income matters and price volatility is tolerable.

Buffett buys preferred in specific circumstances: when a distressed firm needs capital, and when the terms include meaningful equity upside through warrants. His 2008–2011 preferred deals generated total returns in the high-teens to low-twenties annualized, because the warrants captured the bank recoveries while the preferred dividends provided downside protection during the uncertain years.

---

## 3.5 The three claims, reassembled

We started by asserting that every equity security is a bundle of three claims: income, residual value, and control. The three sections you've just read unpacked each claim. Put them back together.

| Instrument | Income claim | Residual / liquidation claim | Control |
|---|---|---|---|
| Debt | Contractual, legally enforceable | Senior to all equity | None in normal operation |
| Preferred stock | Fixed, priority over common, board can skip | Above common, below all debt | Usually none |
| Common stock | Residual; dividends only if declared | Last in line | Voting (unless dual-class dilutes it) |

Look down the columns. As you move from debt to preferred to common, you're trading legal protection for participation in upside. Debt is the strongest legal position with no upside beyond interest. Common is the weakest legal position with unlimited upside. Preferred sits between on both dimensions. None of the three is "better." Each is a different point in the same design space.

### The Buffett-Goldman deal, decoded

Now read the [September 2008 Goldman deal](https://www.goldmansachs.com/pressroom/press-releases/2008/berkshire-hathaway-investment.html) with what you know.

Goldman issued $5B of preferred to Berkshire Hathaway with a 10% dividend. Berkshire also received warrants to buy $5B of Goldman common at $115/share, exercisable for five years. Goldman could redeem the preferred at 110% of par after three years.

Read the structure:

- The **10% preferred dividend** gave Buffett a high-priority income stream during a period when Goldman's common dividend and common stock price were both uncertain. If Goldman survived, Buffett got paid 10% on $5B — $500M per year — regardless of what happened to the common.
- The **warrants** gave Buffett upside if Goldman's common recovered. The $115 strike was roughly where Goldman traded at the deal date. Every dollar of recovery above $115 translated directly into warrant value.
- The **call at 110% of par** capped the preferred's upside. Goldman could pay Berkshire $5.5B (plus accrued dividends) and exit the preferred. Eventually they did, [redeeming in March 2011 for about $5.64B](https://www.goldmansachs.com/pressroom/press-releases/2011/goldman-sachs-redeems-preferred-stock-from-berkshire-hathaway.html). By that point, the warrants had become the real prize.

When the dust settled, Berkshire [exercised the warrants in October 2013 in a cashless conversion](https://www.goldmansachs.com/pressroom/press-releases/2013/berkshire-hathaway-exercises-its-warrant.html) and received about 13.1 million shares of Goldman common. Total profit on the original $5B investment ran to roughly $5–6B over five years — about $3.7B from the preferred (dividends plus the redemption premium) and another ~$2B+ from the warrants. The preferred provided income during the uncertainty; the warrants captured the recovery.

The deal's design philosophy: match the security structure to what each party actually needs. Goldman needed capital that didn't dilute voting control and that regulators would treat as equity. Buffett needed downside protection plus equity upside. A common-stock purchase would have failed both. A straight loan would have failed the regulatory capital test. Preferred plus warrants solved both problems at once.

That, finally, is why the chapter opened where it did. The Buffett deals look like a quirk only if you think preferred and common are stronger and weaker versions of the same thing. They aren't. They are different bundles of the same three claims, designed for different problems.

### Connections forward

Chapter 4 takes the residual-claim framework you now have and runs valuation models against it: the Dividend Discount Model values common stock as the present value of all future dividends, which only makes sense once you understand that those dividends are *discretionary* and *residual*. The DCF model values the entire firm and subtracts debt to arrive at equity value, which only makes sense once you understand the capital stack. Chapter 5 builds portfolios from these valuations — beta, correlation, diversification all sit on top of the residual-claim idea. Chapter 9 returns to preferred stock in the regulatory-capital context, where the Buffett-Goldman deal acquires its second meaning: it was also a regulatory capital transaction.

The residual-claim framework — *who gets paid in what order, with what legal protection, and what upside* — will keep appearing. Every financial instrument you meet for the rest of this book can be decomposed into questions about priority, protection, and participation. The vocabulary you now have is the vocabulary the rest of the field uses, whether it names it explicitly or not.

The instruments are named descriptively. Common stock is *common* because it's what most investors own. Preferred stock is *preferred* only in the narrow sense that it ranks ahead of common. Neither name tells you what the instrument is *for*. The bundle does.

---

**What would change my mind:** A historical episode in which preferred stock issued by a healthy, well-capitalized firm reliably outperformed that same firm's common stock over a long horizon, after adjusting for the warrant kicker. The chapter argues preferred is a compromise instrument that earns its keep in distress and regulatory contexts; sustained outperformance in normal conditions would force a rewrite.

**Still puzzling:** Why dual-class structures persist in companies long after the founder has left or died. The "founder conviction" justification is at least coherent for active founders. For successor CEOs running on inherited supervotes, the structure looks more like rent extraction than long-term optimization, and I haven't seen a clean account of why markets keep paying full price for such shares.

---

**Tags:** equity-securities, residual-claim, preferred-stock, dual-class-structures, buffett-goldman-2008
