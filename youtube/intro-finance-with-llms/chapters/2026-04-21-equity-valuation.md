> **Voice status:** `voice-unanchored`. Root `style/` and `books/intro-finance/style/` are still empty as of this draft. Calibrate review accordingly.
>
> **Chapter sequencing:** Drafted as Chapter 4 in source numbering, but the book's chapter order is being resequenced. References to "Chapter N" inside this draft are placeholders against the working outline.

---

## Suggested titles

1. **Equity Valuation: Three Models, Three Theories, One Stock**
2. **Why Valuations Disagree: A Field Guide to DDM, DCF, and Multiples**
3. **The Coca-Cola Puzzle: What Buffett Saw That Wall Street Missed**

---

## TL;DR

A "valuation" is not a number you extract from a company — it's a number you generate from a theory, and three different theories of value (dividend stream, free cash flow, market comparables) will produce three different numbers for the same stock. The disagreement among the methods is not a bug; it's the most useful output of the exercise, because it pinpoints which assumption you and the market do not share.

---

## Learning objectives

By the end of this chapter you should be able to:

1. Apply the Gordon Growth Model to a mature dividend-paying company and explain the conditions under which it gives reliable answers.
2. Construct a two-stage Dividend Discount Model when a company is expected to transition from high to stable growth.
3. Build a simple DCF valuation from a free-cash-flow forecast and compute the terminal value by both the perpetuity-growth and exit-multiple methods.
4. Calculate the five major relative-valuation multiples (P/E, P/B, P/S, EV/EBITDA, PEG) and name at least one business context where each misleads.
5. Reconcile three different valuations of the same company by identifying which assumption drives the disagreement.
6. Diagnose the four common valuation errors: circular reasoning via WACC, false precision, comparable-selection bias, and terminal-value dominance.

## Prerequisites

Time value of money and perpetuities (Chapter 2). The residual claim framework, the capital stack, and the four basic equity metrics (Chapter 3). Comfort reading Python functions and running them on small examples.

## Where this chapter fits

Chapter 3 introduced the instruments. This chapter introduces the machinery for estimating what they're worth. Chapter 5 (portfolios) takes single-security valuations and combines them, where risk interacts across holdings. Without single-security valuation, portfolio theory is symbol manipulation.

---

## 4.1 The Coca-Cola puzzle

In 1988 and 1989, Berkshire Hathaway bought roughly **$1.024 billion** of Coca-Cola stock — $593M in 1988, $431M in 1989 — making it [the single largest investment Berkshire had ever made at the time](https://www.berkshirehathaway.com/letters/1989.html). Buffett wrote in his 1989 letter that he had been watching Coca-Cola for decades.

Here's the strange part. Coca-Cola wasn't visibly cheap. The stock had recovered from the October 1987 crash and traded at roughly **15× trailing earnings** in 1988 — about in line with the broader market. Wall Street analysts widely [thought Buffett was overpaying](https://www.cnbc.com/2007/07/19/history-lesson-warren-buffetts-crazy-cocacola-bargain-buy.html); some called the trade "downright crazy." Buffett disagreed.

How does that happen? Two experienced investors look at the same company at the same price and reach opposite conclusions about whether to buy.

The short answer: they were using different models. A "valuation" is not a number you extract from a company. It is a number you generate from a theory. Change the theory, change the number. And because every theory of value has specific assumptions, every valuation has specific vulnerabilities.

Three theories dominate practice. Each produces a different number for the same stock.

- The **Dividend Discount Model** says a stock is worth the present value of all the dividends you will ever receive from it.
- The **Discounted Cash Flow Model** says a stock is worth the present value of all the free cash flows the company will ever generate, divided by the share count.
- The **Relative Valuation** approach says a stock is worth whatever comparable companies are trading for, scaled by some operating metric.

When the three agree on a price, your confidence in the valuation is high. When they disagree — which is most of the time — the disagreement itself is the most valuable thing the exercise produces. It tells you which assumption the market is making that you don't share.

The hook isn't whether Buffett was right about Coke (he was). It's the prior question: what theory of value made Coke look cheap to him at 15× earnings when the same number made it look expensive to everyone else? By the end of the chapter you'll be able to answer that, and — harder — to recognize when a valuation is being performed theatrically rather than honestly.

---

## 4.2 The Dividend Discount Model

The most direct theory of stock valuation is also the oldest: a share of stock is worth whatever cash you will eventually receive from owning it. For an equity investor planning to hold forever, that cash arrives as dividends. Sum the present value of all future dividends and you have the stock's value.

In one line:

$$P_0 = \sum_{t=1}^{\infty} \frac{D_t}{(1+r)^t}$$

The formula is honest. It is also impossible to use directly — nobody knows what dividends will be paid in year 47. Every practical version of the DDM makes some simplifying assumption about how dividends grow over time.

### The Gordon Growth Model

The simplest assumption: dividends grow at a constant rate forever. If that's true, the infinite sum collapses to a closed form:

$$P_0 = \frac{D_1}{r - g}$$

This is the **Gordon Growth Model**. It's named for [Myron Gordon's 1959 paper in *The Review of Economics and Statistics*](https://www.jstor.org/stable/1927792) (and his 1956 paper with Eli Shapiro in *Management Science*), but the underlying idea — value as the present value of future dividends — appears earlier in [John Burr Williams's 1938 *The Theory of Investment Value*](https://www.hbs.edu/faculty/Pages/item.aspx?num=37601). Williams did the conceptual work; Gordon and Shapiro nailed the closed-form result with constant growth.

Three things in the formula are worth dwelling on.

**First, the formula only makes sense when $r > g$.** If growth equals or exceeds required return, the denominator goes to zero or negative and the model returns infinity or a negative price. Both are nonsense. This is not a mathematical quirk — it's a statement about the world. No company can grow its dividends faster than investors' required return forever, because such a company would eventually consume the entire global economy. The $r > g$ check is a sanity check on your assumptions before it is anything else.

**Second, the formula is hypersensitive to small changes in $r$ and $g$ when they're close.** Take $D_1 = \$2$, $r = 0.08$, $g = 0.05$. Gordon gives $P_0 = \$2 / 0.03 = \$66.67$. Now raise $g$ to 0.06. New price: $\$2 / 0.02 = \$100$. A one-percentage-point change in growth produced a 50% change in value. This is why valuations disagree. Reasonable people can hold reasonable-looking assumptions that differ by 1–2 points and arrive at radically different answers.

**Third, the formula prices the trade-off between risk and growth in one expression.** A higher required return $r$ lowers the price (more compensation demanded, less paid). A higher growth rate $g$ raises the price (more expected, more paid). The stock's value is the tension between those two forces.

### A worked example — a mature utility

A regulated electric utility, hypothetical for clean numbers, paid a $4.00 dividend last year. Management has raised the dividend ~3% per year for a decade, and the regulatory framework caps growth around there. The market's required return for a stock of this risk is 7%.

$$D_1 = \$4.00 \times 1.03 = \$4.12 \qquad P_0 = \frac{\$4.12}{0.07 - 0.03} = \$103.00$$

If the stock trades at $90, it might be undervalued. If it trades at $120, it might be overvalued. Both judgments depend on whether you accept the 3% growth and 7% required return.

A sanity check that every Gordon valuation should pass: at $103 with a $4.12 forward dividend, the dividend yield is $4.12/$103 ≈ 4%, plus 3% growth gives a 7% expected total return — exactly the required return we started with. **Dividend yield + growth rate = required return.** When the model is internally consistent, that identity holds. When it doesn't, you've made an arithmetic error.

### Where Gordon Growth fails

Three common cases break the model.

*Companies that don't pay dividends.* Berkshire Hathaway has paid one dividend in its modern history — [a single $0.10 payout in 1967](https://www.cnbc.com/2018/05/04/heres-why-warren-buffetts-berkshire-hathaway-doesnt-pay-a-dividend.html), about which Buffett has joked he "must have been in the bathroom when the decision was made." Amazon has never paid one. Alphabet and Meta paid none for years and only [initiated dividends in 2024](https://www.cnbc.com/2024/04/25/alphabet-issues-first-ever-dividend-70-billion-buyback.html) — a decade-plus into being public. The DDM produces zero (or only a tiny figure based on those modest dividends) for these firms because $D_1 \approx 0$. The model implicitly assumes dividends are how value is delivered. Many companies explicitly reject that.

*Temporarily very high growth.* If $g = 0.25$ and $r = 0.10$, the formula returns a negative price — meaningless. You can't substitute a lower $g$ without throwing away real information about the near-term trajectory. The fix is a multi-stage model.

*Dividends disconnected from economic reality.* Some firms pay dividends out of debt, which is unsustainable. Some maintain dividends long after the economics have soured. Some cut during temporary distress when long-term economics are fine. The DDM treats dividends as a proxy for economic value; when the proxy breaks, the model breaks with it.

### The two-stage DDM

The standard fix for the high-growth problem: assume growth at a high rate $g_1$ for $n$ years, then a stable rate $g_2$ forever after.

$$P_0 = \sum_{t=1}^{n} \frac{D_0 (1+g_1)^t}{(1+r)^t} + \frac{1}{(1+r)^n} \cdot \frac{D_0(1+g_1)^n(1+g_2)}{r - g_2}$$

The first term discounts the high-growth dividends explicitly. The second term is the Gordon Growth Model applied at year $n$ to capture everything after, then discounted back. Same machinery, applied twice.

Minimal Python:

```python
def gordon_growth_value(next_dividend, required_return, growth_rate):
    """Value a stock under the Gordon Growth Model. Errors if g >= r."""
    if growth_rate >= required_return:
        raise ValueError(
            f"Growth ({growth_rate}) must be less than required return "
            f"({required_return}); the formula breaks otherwise."
        )
    return next_dividend / (required_return - growth_rate)


def two_stage_ddm(d0, g_high, g_stable, r, n):
    """Two-stage DDM: g_high for n years, then g_stable forever."""
    pv_high = sum(
        d0 * (1 + g_high) ** t / (1 + r) ** t
        for t in range(1, n + 1)
    )
    d_at_n = d0 * (1 + g_high) ** n
    terminal = d_at_n * (1 + g_stable) / (r - g_stable)
    pv_terminal = terminal / (1 + r) ** n
    return pv_high + pv_terminal
```

Each function does one thing. `gordon_growth_value` is the simple case. `two_stage_ddm` calls the same arithmetic at the transition year. No retrieval, no plotting, no estimation of the inputs. Each of those concerns belongs in its own function.

A note worth its own paragraph: students often treat $r$ and $g$ as objective, retrievable numbers. They are not. Both are assumptions. The required return $r$ reflects what investors collectively demand for the stock's risk; it's typically estimated using the Capital Asset Pricing Model, which carries its own assumptions. The growth rate $g$ is the analyst's best guess about the long-run future. Neither lives in a database. When you read an analyst report claiming a stock is worth $X by Gordon Growth, you are reading that analyst's opinions about $r$ and $g$ converted into a number. The model's mathematical precision is real. The inputs' epistemic precision is not.

---

## 4.3 The Discounted Cash Flow model — the deep dive

The DDM values a stock by the cash *you receive*. The DCF takes a different theory: a stock is worth the cash *the company generates*, regardless of whether that cash is paid as a dividend, reinvested, or used to buy back shares.

This matters in practice. Amazon generated enormous free cash flows for two-and-a-half decades while paying zero dividends. Alphabet, Meta, and Berkshire Hathaway have been cash-generating machines with little or no dividend history. The DDM says these firms are worth approximately nothing (or nothing more than the present value of small future dividends). The DCF says their value is the present value of the cash they produce, however they choose to deploy it. The DCF is the deep dive of this chapter because it makes the residual-claim machinery from Chapter 3 do real work.

### The formula

$$\text{Enterprise Value} = \sum_{t=1}^{n} \frac{FCF_t}{(1 + WACC)^t} + \frac{TV_n}{(1 + WACC)^n}$$

where $FCF_t$ is free cash flow in year $t$, WACC is the weighted-average cost of capital, and $TV_n$ is the terminal value at the end of the explicit forecast period.

Then:

$$\text{Equity Value} = \text{Enterprise Value} - \text{Net Debt} \qquad \text{Price per Share} = \frac{\text{Equity Value}}{\text{Shares Outstanding}}$$

Three things matter immediately.

*The DCF values the company, not the stock.* Equity value comes from subtracting debt, because bondholders sit higher in the capital stack (Chapter 3). Enterprise value goes to all capital providers; equity value is what's left.

*The discount rate is WACC, not cost of equity alone.* The cash flows being discounted belong to all capital providers — debt and equity together — so the discount rate should reflect what all capital providers require, weighted by capital structure.

*Terminal value typically dominates.* In a 5- or 10-year DCF, the terminal value often represents 60–85% of enterprise value. This is where most DCF errors originate and where most DCF abuses hide.

### Terminal value: two methods

The terminal value is the present value of all cash flows beyond the explicit forecast. Two methods dominate.

**Perpetuity growth.** Assume free cash flows grow at a stable rate $g$ forever after year $n$:

$$TV_n = \frac{FCF_{n+1}}{WACC - g}$$

This is just Gordon Growth applied to cash flows. Same $r > g$ constraint.

**Exit multiple.** Assume the company is sold at year $n$ for a multiple of its final-year operating metric, usually EBITDA: $TV_n = \text{EBITDA}_n \times \text{Multiple}$. The multiple is usually pulled from current trading multiples of comparable public companies.

The perpetuity method is mathematically cleaner. The exit-multiple method is more common in investment banking because it ties terminal value to observable market data. Sophisticated DCF models build both and triangulate.

### A worked example — a software company

Hypothetical mid-sized software company. Free cash flow this year: $200M. Forecast (decelerating growth):

| Year | FCF ($M) | Growth |
|---:|---:|---:|
| 1 | 240 | 20% |
| 2 | 288 | 20% |
| 3 | 345 | 20% |
| 4 | 397 | 15% |
| 5 | 437 | 10% |

After year 5, FCF grows at 3% forever. WACC is 9%. Net debt is $400M ($500M debt minus $100M cash). Shares outstanding: 100M.

Step 1 — discount the explicit forecast.

| Year | FCF | Discount factor | PV ($M) |
|---:|---:|---:|---:|
| 1 | 240 | 1/1.09 = 0.917 | 220.2 |
| 2 | 288 | 1/1.09² = 0.842 | 242.5 |
| 3 | 345 | 1/1.09³ = 0.772 | 266.3 |
| 4 | 397 | 1/1.09⁴ = 0.708 | 281.1 |
| 5 | 437 | 1/1.09⁵ = 0.650 | 284.1 |

Sum of explicit-period PVs: $1,294.2M.

Step 2 — terminal value, perpetuity-growth method.

$$FCF_6 = 437 \times 1.03 = \$450.1 \text{M} \qquad TV_5 = \frac{450.1}{0.09 - 0.03} = \$7{,}501.7 \text{M}$$

Discount to today: $\$7{,}501.7 \times 0.650 \approx \$4{,}876.1$M.

Step 3 — sum.

$\text{EV} = 1{,}294.2 + 4{,}876.1 = \$6{,}170.3$M.

The terminal value is $4{,}876 / 6{,}170 \approx \mathbf{79\%}$ of enterprise value. That is typical, and it is the single most important diagnostic in any DCF.

Step 4 — equity value per share.

$\text{Equity} = 6{,}170.3 - 400 = \$5{,}770.3$M. Per share: $\$5{,}770.3 / 100 = \mathbf{\$57.70}$.

Sanity check. At $200M current FCF and $5,770M equity value, the FCF yield is 3.5% — well below WACC of 9%, but that makes sense given the steep growth baked into the forecast. A check that *would* fail: an implied FCF yield of 15%, which would tell you investors aren't accepting your growth story.

The honest answer is not $57.70. It's a range — perhaps $45 to $75, depending on which assumptions you favor. A DCF that reports a single decimal-precision number without a sensitivity table is performing certainty it does not have.

```python
def dcf_valuation(fcf_forecast, terminal_growth, wacc, net_debt, shares):
    """Basic DCF using the perpetuity-growth terminal value.

    Returns enterprise value, equity value, per-share price, and the
    terminal-value share of EV — the most important diagnostic to watch.
    """
    if terminal_growth >= wacc:
        raise ValueError("Terminal growth must be less than WACC.")
    pv_explicit = sum(
        fcf / (1 + wacc) ** (t + 1)
        for t, fcf in enumerate(fcf_forecast)
    )
    last_fcf = fcf_forecast[-1]
    tv = last_fcf * (1 + terminal_growth) / (wacc - terminal_growth)
    pv_tv = tv / (1 + wacc) ** len(fcf_forecast)
    ev = pv_explicit + pv_tv
    return {
        "enterprise_value_M": ev,
        "equity_value_M": ev - net_debt,
        "price_per_share": (ev - net_debt) / shares,
        "terminal_pct": pv_tv / ev * 100,
    }
```

When the `terminal_pct` returned by this function exceeds 85%, the DCF isn't really valuing the explicit forecast — it's valuing the terminal assumption, with the explicit forecast as decoration. Either extend the forecast or admit you're doing Gordon Growth with extra steps.

### Where the DCF fails

*False precision.* The formula produces a single number that feels authoritative. It isn't. WACC and terminal growth changes well within reasonable analyst disagreement can shift the output by 30%+. A DCF without a sensitivity table is being used dishonestly.

*Terminal value dominance.* In high-growth valuations, the terminal value can exceed 85% of enterprise value. At that point the DCF is mostly a terminal-value calculation pretending to be something else.

*Circular reasoning via WACC.* WACC inputs include the market value of equity. But the DCF's purpose is to *estimate* the fair value of equity. If the fair value differs from the market value, WACC was wrong. [Sophisticated practitioners iterate](https://www.researchgate.net/publication/265304452_To_Iterate_Or_Not_To_Iterate_Using_The_WACC_In_Equity_Valuation) — assume capital structure, value, update, re-value, until convergence. Sloppy ones don't, and the resulting circularity can substantially over- or undervalue.

*Assumption cascades.* A 5-year forecast bundles five revenue growth assumptions, five margin assumptions, capital expenditure assumptions, working-capital assumptions, plus terminal assumptions, plus WACC components. Each carries uncertainty. The compounded uncertainty is almost always larger than presented.

---

## 4.4 Relative valuation — what the market has already solved

The third theory is the most pragmatic. Forget modeling future cash flows from scratch. The market is already valuing thousands of comparable companies every day. Find companies similar to your target, observe what multiple of earnings (or book value, sales, EBITDA) the market is paying, apply the same multiple.

This is **relative valuation**. The intellectual limitation: it tells you what the company is worth *relative to the market*, not what it's worth absolutely. The trade: it sidesteps most of the assumption-cascade problem of DCF by letting the market's collective digestion of those assumptions do the work for you.

### Five multiples worth knowing

$$P/E = \frac{\text{Price}}{\text{EPS}}$$ — the oldest and most quoted. Works for mature, profitable firms with stable capital structures. Fails on loss-making firms (negative P/E is meaningless), firms with large non-cash charges, and firms with heavy debt (which look artificially cheap).

$$P/B = \frac{\text{Price}}{\text{Book Value per Share}}$$ — useful for financial institutions where assets are marked-to-market. Weak signal for software or services firms whose primary assets (code, brand, talent) don't sit on the balance sheet.

$$P/S = \frac{\text{Price}}{\text{Sales per Share}}$$ — less sensitive to accounting choices than P/E. Useful for growth firms not yet profitable. Terrible across industries with different margin structures: a software firm at 10× sales and a grocer at 0.3× sales can both be fair.

$$EV/EBITDA = \frac{\text{Enterprise Value}}{\text{EBITDA}}$$ — preferred in M&A and across firms with different debt levels, because EV captures total firm value and EBITDA is computed before interest. Doesn't work for banks (EBITDA isn't meaningful for financial institutions).

$$PEG = \frac{P/E}{\text{Expected Earnings Growth (\%)}}$$ — Mario Farina described it in 1969; [Peter Lynch popularized it](https://www.amazon.com/One-Up-Wall-Street-Already/dp/0743200403) in *One Up on Wall Street* (1989). Attempts to correct P/E for growth differences. The catch: "expected growth" is itself an analyst forecast, so PEG inherits that uncertainty while hiding it inside a clean-looking ratio.

### A worked example

Specialty retailer, five comparables in the same sub-sector with similar growth profiles:

| Peer | P/E | EV/EBITDA | P/S |
|---|---:|---:|---:|
| A | 18 | 11 | 1.2 |
| B | 22 | 14 | 1.5 |
| C | 20 | 12 | 1.4 |
| D | 16 | 10 | 1.1 |
| E | 24 | 15 | 1.6 |

Medians: P/E = 20, EV/EBITDA = 12, P/S = 1.4.

Target's per-share figures: EPS $3.50, EBITDA $7.00 (minimal net debt, so EV/EBITDA implied price is the same as the multiple times EBITDA per share), Sales $45.00.

- P/E implied price: $20 \times \$3.50 = \$70.00$
- EV/EBITDA implied price: $12 \times \$7.00 = \$84.00$
- P/S implied price: $1.4 \times \$45.00 = \$63.00$

Three numbers, none of them matching. The disagreement is information. The P/S figure is lowest — if your target has lower margins than its peers, its P/S will look low even when fundamentals are fine. The EV/EBITDA figure is highest — if your target is more profitable than peers at the operating level, that shows up here. An honest practitioner reports a range ($63–$84), notes the median around $70–$72, and flags which multiple to trust under which scenario. A dishonest one picks whichever number supports their pre-existing view.

### The hardest part — selecting comparables

Everything in relative valuation depends on the peer set. Wrong peers produce wrong answers, and the cleanness of the multiple arithmetic disguises the failure. Good peer sets share five things: industry and sub-industry, growth profile, profitability profile, capital structure, and geography/regulatory environment. Hitting all five at once is hard; the standard temptation under time pressure is to enlarge the peer set hoping the dissimilarities wash out. They usually don't. Three genuinely comparable firms beat fifteen loosely-related ones.

### Where relative valuation fails

*When the market is wrong about the comparables.* In 1999, every dot-com traded at extreme multiples. Peer multiples could justify almost any price for almost any internet company. When the bubble collapsed, the [Nasdaq Composite fell ~78% peak-to-trough from March 2000 through October 2002](https://en.wikipedia.org/wiki/Dot-com_bubble); individual dot-coms fell further or vanished. Relative valuation embeds market opinion. When market opinion is wrong, relative valuations are wrong in the same direction.

*Cyclicals.* Commodity firms, homebuilders, and other cyclicals look cheap on P/E at the cycle top (peak earnings) and expensive at the bottom (trough earnings). Current P/E for a cyclical produces exactly the wrong signal.

*When no comparable exists.* Tesla in 2008–2012 had no comparable. SpaceX still doesn't. You can't do relative valuation when the market hasn't priced anything similar.

---

## 4.5 When three methods disagree — and the Coca-Cola answer

Apply all three to one company and you'll usually get three different numbers. The naive move is to average them. That is wrong, because the three are not three independent estimates of the same thing — they are three different theories of value, each with different vulnerabilities, each appropriate in different contexts. Averaging obscures which theory you actually believe.

The honest move is to read the disagreement.

A worked scenario. High-growth tech company. Gordon Growth implies $420 (assuming small current dividend growing at 15% then 3%). DCF implies $650 (25% FCF growth tapering to 3% over 10 years, 9% WACC). Relative valuation on EV/EBITDA implies $540. Market price is $500.

Average: $537. Tempting. Useless.

The DDM is the least reliable here — high-growth tech companies don't deliver value through dividends, and the model is being forced to fit a situation it isn't designed for. The two numbers that matter are $650 (DCF) and $540 (relative). The $110 gap tells you one of two things: the market is underpricing the stock relative to fundamental cash generation (a "the market is wrong" argument, rarely a great bet), or your DCF assumptions are too optimistic and the peer market is already discounting something you haven't priced — competitive risk, regulatory exposure, technology shift. Deciding which is the actual analysis. The three valuation numbers are the *inputs* to that question, not the answer.

### Coca-Cola, decoded

Now back to Buffett. At 15× earnings in 1988, Coca-Cola wasn't cheap on relative multiples. A standard DCF using market-consensus growth assumptions would have produced something close to the market price.

Buffett's implicit theory was different. He believed the Coca-Cola brand was a *durable economic moat* — one that allowed the company to raise prices slightly faster than inflation more or less forever, and to extend its global reach for decades. Translated to model terms: he was using a higher long-run growth rate $g$ than the market consensus, applied to a Gordon-Growth-flavored framework. With his $g$, Coke at 15× earnings looked like a long-duration cash flow stream selling at a discount. With the market's lower $g$, the same price looked fair.

Whose theory was right is now a settled question — Coca-Cola compounded handsomely. But the important point isn't who won. It's that Buffett had a *single, explicit theory* of what determined the stock's value, and he could name precisely where the market's implicit theory differed from his. The valuation wasn't his answer; it was the expression of a view.

That is what sophisticated valuation work looks like. It starts from a theory of why this stock might be mispriced, uses one or more models to test whether the theory is defensible at the current price, and ends with a clear conditional statement: "this stock is worth X *if* you believe Y about the future, *and here's why* I believe Y when the market doesn't." The conditional is the analysis. "Coca-Cola is worth $45 per share" is not a useful output. "Coca-Cola is worth $45 per share *if* its dividend grows at 6% for two decades, which is achievable given its pricing power and international expansion" is a useful one. The second can be challenged, refined, or rejected. The first just sits there.

### Forward connections

Chapter 5 takes single-security valuations and combines them into portfolios — diversification, correlation, the trade-off between risk and return at the portfolio level. The valuations from this chapter remain in use throughout the book: in risk-adjusted performance (Sharpe ratios, alpha), in capital budgeting decisions, in dividend and capital-structure choices. One topic this chapter deliberately doesn't touch: options pricing. Options value depends on the *distribution* of possible future prices, not their expected level — a different theory of value, developed in Chapter 11.

The instruments are named one way, the theories another, and the answers a third. The instruments are static. The theories shift with what you believe about the future. The answers shift with whichever theory you're holding. **A valuation is not a number you discover. It is a number you make, one assumption at a time, and the most useful number is the one whose assumptions you can defend.**

---

**What would change my mind:** A historical sample of valuations performed by sophisticated investors in which averaging the outputs of multiple models reliably outperformed the best single model. The chapter argues averaging obscures the analyst's theory; consistent averaging-wins evidence would force a rewrite of §4.5.

**Still puzzling:** Why so many sell-side equity reports report a single point-estimate "price target" without an honest sensitivity range, given that the analysts producing them clearly know their own DCFs are sensitivity-fragile. The institutional incentive structure (clarity sells, range-of-uncertainty doesn't) is a partial answer, but it doesn't explain the persistence in academic and CFA-level training, where the same conventions are taught as if precision were the goal.

---

**Tags:** equity-valuation, dividend-discount-model, discounted-cash-flow, relative-valuation-multiples, buffett-coca-cola-1988
