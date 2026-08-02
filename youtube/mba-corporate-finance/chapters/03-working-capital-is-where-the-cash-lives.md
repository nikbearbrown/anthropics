# Chapter 3 — Working Capital Is Where the Cash Lives


## TL;DR

- The most important number in this book is measured in days, and almost nobody outside of treasury has heard of it.
- The chapter moves through The Capital Nobody Talks About, What Working Capital Actually Is, The Cash Conversion Cycle, The Arithmetic of Improvement, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

*The most important number in this book is measured in days, and almost nobody outside of treasury has heard of it.*

---

There is a number that will change how you read a balance sheet, and I want to tell you what it is before I explain where it comes from.

The number is measured in days. It tells you how long a dollar of cost spends inside the firm before it comes back as a dollar of revenue. At Halverson Manufacturing, that number is 85. From the moment Halverson pays for raw materials or labor, eighty-five days pass — on average — before the corresponding cash returns from a customer.

Eighty-five days does not sound alarming. But multiply it by the daily rate at which Halverson spends money, and something startling appears. Halverson's cost of goods sold is about $1.4 billion per year. Divide by 365 and you get roughly $3.8 million per day. Multiply that by 85 days and you get approximately $323 million — sitting inside the operating cycle at any given moment, not in a bank account, not invested in equipment, just in transit between outflow and inflow.

![Scale comparison ](images/03-working-capital-is-where-the-cash-lives-fig-01.png)
*Figure 3.1 — Scale comparison *

That is larger than Halverson's total long-term debt. It is six times the size of the Plant 4 expansion Maya is analyzing in Chapter 4.

The single largest pool of capital in the firm is not the factory. It is the gap between when money goes out and when money comes back in.

I want to spend this chapter on that gap — why it exists, how to measure it precisely, and what it means for how a finance team should think about funding the business.

---

## The Capital Nobody Talks About

When people argue about how a firm should finance itself, the debate is almost always framed as a choice between debt and equity. Borrow money or sell shares. Pay interest or dilute ownership. Chapters 7 and 8 will enter that debate in detail.

But there is a third source of capital that sits entirely outside the debt-versus-equity structure. It does not require a conversation with a banker. It does not require board approval. It does not add a penny of interest expense or dilute a single existing share. It is generated internally, by running the operating cycle more efficiently than you ran it last year.

Every day you shorten the cycle frees $3.8 million at Halverson's scale. Ten days of improvement — just ten days out of eighty-five — releases roughly $38 million of cash that was already inside the firm. That cash does not need to be borrowed. It does not need to be raised. It just needs to be unlocked.

This is not a marginal observation about treasury operations. It is a claim about where the real financing action is for most firms. I will make the case for it carefully, because it runs against the grain of how corporate finance is usually introduced.

---

## What Working Capital Actually Is

The textbook definition of working capital is current assets minus current liabilities. This is correct and nearly useless for operational purposes, because it lumps together several fundamentally different things.

Here is the definition I use instead:

$$\text{Operating working capital} = \text{Accounts Receivable} + \text{Inventory} - \text{Accounts Payable}$$

Each term represents cash in a specific state of transit.

Accounts receivable is cash that has been promised but not yet received. Halverson has shipped goods. The customer owes money. The cash is legally committed but physically absent — it exists as an obligation, not as a balance.

Inventory is cash that has already been spent but not yet converted into revenue. Halverson bought raw materials, paid workers to process them, and is now holding finished goods in a warehouse. The labor and materials cost has already left the firm. The corresponding revenue has not yet arrived. That gap is inventory.

Accounts payable is the reverse: cash that Halverson owes but has not yet paid. Suppliers have delivered materials and are waiting. For as long as they wait, Halverson retains the use of that cash. Payables are a source of financing — not because anyone designed them that way, but because the mechanics of commercial relationships create a natural float.

![Three-bucket diagram showing cash in transit through accounts receivable, inventory, and accounts payable](images/03-working-capital-is-where-the-cash-lives-fig-01.png)
*Figure 3.1 — Working capital is cash in transit*

Operating working capital is the net of these three. It is the amount of capital the firm has committed to keeping its operations running — the dollar value of the gap between when cash goes out and when cash comes back in.

Notice what this definition excludes. Cash itself is not in operating working capital — cash is the *result* of working capital decisions. Short-term debt is also excluded — that is a financing choice, not an operating one. Stripping those out is not a technicality. It is what lets you see the operating cycle clearly, without the financing layered on top of it.

---

## The Cash Conversion Cycle

The cash conversion cycle is a single formula that compresses everything above into one number.

$$\text{CCC} = \text{DSO} + \text{DIO} - \text{DPO}$$

Three terms, each in days.

Days sales outstanding (DSO) measures how long it takes to collect from customers after a sale:

$$\text{DSO} = \frac{\text{Accounts Receivable}}{\text{Revenue}} \times 365$$

Days inventory outstanding (DIO) measures how long inventory sits before it is sold:

$$\text{DIO} = \frac{\text{Inventory}}{\text{COGS}} \times 365$$

Days payable outstanding (DPO) measures how long the firm takes to pay its suppliers:

$$\text{DPO} = \frac{\text{Accounts Payable}}{\text{COGS}} \times 365$$

Now I will work through Halverson's numbers so the formula stops being abstract.

Revenue is $2.0 billion. COGS is $1.4 billion. Accounts receivable is $330 million. Inventory is $230 million. Accounts payable is $135 million.

$$\text{DSO} = \frac{330}{2000} \times 365 \approx 60 \text{ days}$$

$$\text{DIO} = \frac{230}{1400} \times 365 \approx 60 \text{ days}$$

$$\text{DPO} = \frac{135}{1400} \times 365 \approx 35 \text{ days}$$

$$\text{CCC} = 60 + 60 - 35 = 85 \text{ days}$$

So: from the moment Halverson pays for materials or labor to the moment the corresponding cash arrives from a customer, eighty-five days pass. That is the cycle.

![Cash conversion cycle as a horizontal timeline showing DSO, DIO, and DPO with a net 85-day exposure](images/03-working-capital-is-where-the-cash-lives-fig-02.png)
*Figure 3.2 — The cash conversion cycle*

The formula's structure tells you something directly. DSO and DIO are additions — they make the cycle longer, because they represent cash going out before cash comes back in. DPO is a subtraction — it makes the cycle shorter, because delaying payment to suppliers postpones the outflow. That asymmetry is not a coincidence of notation. It reflects the underlying mechanics: the firm wants to collect fast, turn inventory fast, and pay slowly.

What I want you to notice is what the CCC is *not*. It is not a profitability measure. A firm can have excellent margins and a terrible cash conversion cycle. It is not a liquidity measure in the accounting sense. It is a measure of operational efficiency — specifically, of how well the firm manages the transit time between spending and collecting.

---

## The Arithmetic of Improvement

Every day the CCC shortens frees roughly one day's worth of COGS as cash. At Halverson, that is $3.8 million per day. This creates a precise and unusual kind of calculation.

If the collections team reduces DSO by five days — by collecting from customers five days faster on average — that frees $19 million. Not next quarter. Continuously. The capital requirement of the operating cycle drops by $19 million permanently, as long as the improvement holds.

If the operations team reduces DIO by five days — by turning inventory five days faster — same result. $19 million freed.

If procurement extends DPO by five days — by negotiating an extra five days before paying suppliers — same result again.

Ten days of combined improvement, spread across all three levers, releases $38 million. I said this at the start of the chapter and I want to make the mechanism completely clear now: the improvement is not a one-time event. It is a permanent reduction in how much capital the operating cycle consumes. Halverson does not need to find $38 million. It is already there, inside the cycle, waiting to be freed.

| Lever | Mechanism | Cash freed per day shortened | Key cost / risk |
|---|---|---|---|
| **DSO** | Tighten credit terms; improve collections | $3.8M | Customer attrition — the strict-terms version of *we're losing customers because we changed payment terms* |
| **DIO** | Faster inventory turns; just-in-time sourcing | $3.8M | Stockout exposure — single-source supply disruption hits the line |
| **DPO** | Extend supplier payment terms; renegotiate top-10 contracts | $3.8M | Supplier pricing increases; weakened relationships when supply tightens |

*The arithmetic is identical across levers. The organizational and strategic challenges are not.*

The arithmetic is identical across all three levers. The strategy is completely different, and the costs of improvement are different in ways that matter.

Collecting faster from customers requires either tighter credit terms or a better collections process. Tighter credit terms can push customers to competitors who offer more generous terms. A better collections process requires investment and sometimes changes to commercial relationships. Neither improvement is free.

Reducing inventory requires holding less buffer stock, which means accepting more exposure when demand spikes or a supplier misses a delivery. Operations teams have entirely legitimate reasons for wanting more inventory, not less. The finance team's preference for smaller buffers is reasonable; so is the operations team's preference for larger ones. The right answer involves tradeoffs that cannot be resolved from a spreadsheet.

Extending payable terms requires suppliers to accept slower payment. Large firms with significant purchasing leverage can often do this. Whether they should — and how far they can push it before the relationship or the pricing deteriorates — is a harder question. I will return to it at the end of the chapter.

---

## Why the Headline Number Lies

The standard current assets minus current liabilities figure can stay flat while the operating cycle is deteriorating. This is not a theoretical possibility. It happens routinely in practice, and it is one of the reasons DSO, DIO, and DPO need to be tracked separately.

Consider: Halverson's DSO rises from 60 to 75 days because customers are paying later. The AR balance grows by roughly $57 million. At the same time, the cash balance falls by $57 million — perhaps the firm paid a large vendor early to secure favorable pricing on a bulk order. Headline working capital: unchanged. Operating working capital: $57 million worse. The CCC has risen from 85 to 100 days. The headline number showed nothing.

Or: DIO rises from 60 to 70 days because a product line is moving more slowly than expected. But the AP balance rises by the same amount because the firm has been slow to pay one large supplier. Again, headline unchanged, CCC worse.

These are not contrived edge cases. They appear in quarterly earnings calls under phrases like "working capital headwinds" — which is how management describes problems they noticed too late. The CFO who watches the headline is watching a symptom. The CFO who watches DSO, DIO, and DPO separately can see the problem forming three quarters before it appears in the cash flow statement.

---

## The Same Number, Three Different Problems

Even the component metrics require interpretation. A single DSO number can mean completely different things, and the distinction has serious practical consequences.

DSO of 60 days can mean Halverson sells on net-60 terms and customers pay on time. The number reflects the credit policy. There is no problem.

It can also mean Halverson sells on net-30 terms and customers are routinely paying 30 days late. The DSO is identical but the situation is an operational failure — a collections process that has broken down, or a customer base that has quietly shifted its payment behavior, or both. The aggregate number conceals the problem entirely.

Or it can mean Halverson is recognizing revenue aggressively at quarter-end, booking sales before invoices have been sent or payment terms have been negotiated. In that case the DSO is an accounting problem. The AR balance includes amounts that are not yet owed in any practical sense.

The way to tell these apart is the AR aging schedule: how much of the balance is 0–30 days old, 31–60 days, 61–90 days, over 90? A healthy book concentrates in the early buckets. A deteriorating book has a growing tail past 60 days — customers who are paying late or, eventually, not paying at all. The aging schedule is diagnostic in a way the aggregate DSO cannot be.

**Healthy book**

| Aging bucket | Balance ($M) | % of total AR | Healthy benchmark % |
|---|---|---|---|
| 0–30 days | 76 | 76% | 70–80% |
| 31–60 days | 18 | 18% | 15–20% |
| 61–90 days | 4 | 4% | 3–5% |
| 90+ days | 2 | 2% | < 3% |

**Deteriorating book**

| Aging bucket | Balance ($M) | % of total AR | Healthy benchmark % |
|---|---|---|---|
| 0–30 days | 52 | 52% | 70–80% |
| 31–60 days | 22 | 22% | 15–20% |
| 61–90 days | **18** | **18%** | 3–5% |
| 90+ days | **8** | **8%** | < 3% |

*The deteriorating book has the same total AR but the bulk has migrated past 60 days. The collections problem is diagnosable from the table alone.*

The same three-way ambiguity exists for DIO. Inventory growth can be rational (building stock ahead of a major product launch), operational (slow-moving SKUs that should have been written down quarters ago), or strategic (deliberately building buffer against supply chain risk). The aggregate DIO does not tell you which. You need to look at inventory by item, by age, by turnover rate.

And DPO: paying vendors slowly because you have leverage and they accept it is financial management. Paying slowly because cash is tight and you are stretching vendors to avoid drawing on the revolver is a warning signal. Paying slowly because the accounts payable system is backlogged and invoices are sitting unprocessed is operational dysfunction. Same number, three different situations.

This is why Tom, Halverson's treasurer, spends his mornings on the daily cash report and his mid-mornings with the AR manager going through delayed collections line by line. He is not being granular for its own sake. He is maintaining the diagnostic resolution that aggregate metrics cannot provide.

---

## The Organizational Reality

The CCC formula does not show this, so I want to say it directly: the three components of the cycle are owned by three different parts of the organization.

DSO is owned jointly by sales (which sets payment terms in commercial negotiations) and finance (which runs collections). Shortening DSO often requires sales to accept tighter credit terms with customers who push back on them. Sales teams dislike this. The trade-off between revenue opportunity and cash collection speed is real, and it cannot be resolved by the finance team alone.

DIO is owned by operations and supply chain. Reducing inventory means accepting less buffer stock, which means accepting more exposure to demand variability and supplier failure. The tension between the operations team's preference for larger buffers and the finance team's preference for smaller ones is legitimate on both sides.

DPO is owned by procurement. Extending payable days shifts a cash flow burden onto suppliers. For large firms dealing with smaller suppliers who have no alternatives, this can cross from negotiation into something more coercive. Several jurisdictions now regulate maximum payment terms precisely because of this dynamic. A CFO managing DPO aggressively needs to be aware of both the financial arithmetic and the relational and ethical consequences of using purchasing leverage this way.

![Org-chart diagram mapping each CCC component to the business functions that own it, with cross-functional tension points](images/03-working-capital-is-where-the-cash-lives-fig-03.png)
*Figure 3.3 — CCC as a cross-functional negotiation*

The cash conversion cycle is a number. The work of improving it is organizational, political, and — in the case of DPO — ethical. The formula is clean. The reality is not.

---

## Internal Capital Before External Capital

Chapters 4, 5, and 6 treat capital allocation as a question about investing a given pool of capital wisely. They ask whether specific projects create value — whether to build Plant 4, whether to acquire a competitor, whether to return cash to shareholders. Those chapters assume, more or less implicitly, that the capital exists somewhere and needs to be allocated well.

This chapter is about making sure that assumption holds — or rather, about noticing how much capital is already inside the firm, locked in the operating cycle, before anyone reaches for external financing.

A CFO who shortens Halverson's CCC by thirty days generates roughly $115 million of internal capital. Three Plant 4s. Without a bond. Without diluting shareholders. Without a credit agreement. The capital comes from shortening the time money spends in transit between expenditure and collection.

The practical implication, and the one I want you to carry forward from this chapter: before recommending external financing, ask what internal financing is being left on the table. Every basis point of interest on new debt is a cost. Every diluted share is a cost. Working capital improvement has costs too — organizational friction, relational stress, operational risk — but those costs are almost always smaller than the cost of external capital, and the internal opportunity is almost always less fully exploited than it could be.

Maya makes this her standing question in every capital memo she writes for the rest of the book. She does not ask "how do we fund this?" before she asks "how much of the funding is already inside the cycle, waiting to be freed?" That ordering matters.

---

## What Would Change My Mind

The chapter's central claim is that working capital efficiency is a genuine source of firm value — that firms with shorter cash conversion cycles, all else equal, are worth more than firms with longer ones. Empirical support for this exists in the literature; the canonical references are Deloof (2003) and Shin and Soenen (1998), and the relationship is plausible on its face given the mechanism.

But the causality is not clean. Firms that are operationally healthy tend to have both shorter CCCs and higher valuations, and it is hard to isolate how much of the value premium is coming from the CCC itself versus from the underlying operational competence that generates both. If careful cross-sectional research showed no independent relationship between CCC improvement and firm value — if firms that aggressively shortened their operating cycles did not, on average, trade at higher multiples or generate better long-run returns — the emphasis I have placed on working capital as a strategic lever would need to be revised. I think that evidence would be surprising given the arithmetic, but I am not certain it is wrong.

---

## Still Puzzling

There is a line somewhere between managing DPO aggressively and using size to coerce smaller suppliers into bearing a cash flow burden they cannot absorb. I do not have a clean rule for where that line falls.

Renegotiating payment terms from net-30 to net-45 with a supplier who accepts the change because the business relationship is valuable to them — that seems like legitimate negotiation. A large firm unilaterally extending terms to net-120 with a small supplier who has no alternative customers and cannot survive the cash flow delay — that is coercion, whether or not it is legal.

Between those extremes is a wide range of cases where the CCC arithmetic is clear and the ethics are genuinely murky. Standard financial analysis does not capture the distinction. The auditing standards do not capture it either. My honest answer is: exercise judgment, be transparent about whose cost you are externalizing, and do not pretend the financial benefit and the ethical question are in separate domains. They are not.

---

Chapter 4 takes the cash freed by working capital management — along with capital raised through external financing — and asks how to evaluate whether specific investments create value. The tool is net present value. The challenge is using it without lying to yourself about the assumptions.

---

## Exercises

### Warm-up

**1.** Halverson's accounts receivable balance is $330 million and annual revenue is $2.0 billion. Calculate DSO. Now suppose the AR balance rises to $390 million with revenue unchanged. What is the new DSO, and how much additional capital is tied up in the cycle?
*Tests: mechanical calculation of DSO; translating a balance sheet change into capital terms.*

**2.** A firm has COGS of $800 million per year, inventory of $120 million, and accounts payable of $60 million. Calculate DIO and DPO. If the firm's DSO is 45 days, what is the full CCC?
*Tests: calculation of all three CCC components and their combination.*

**3.** Explain in plain language why accounts payable appears as a subtraction in the CCC formula rather than an addition. What would change if a firm moved from net-30 to net-60 payment terms with its suppliers, and what would that do to the CCC?
*Tests: conceptual understanding of DPO's role in shortening the cycle.*

---

### Application

**4.** A mid-size distributor has annual revenue of $500 million, COGS of $350 million, AR of $75 million, inventory of $55 million, and AP of $40 million. Calculate the CCC and the total capital locked in the operating cycle. Management believes it can reduce DSO by 8 days and DIO by 5 days over the next two years. How much capital would those improvements free, and what external financing cost would that displace if the firm's borrowing rate is 6%?
*Tests: full CCC calculation, improvement arithmetic, and connection to financing cost.*

**5.** Halverson's CFO is presented with two working capital proposals: (a) offer a 1% early-payment discount to customers who pay within 10 days instead of 60, expected to reduce DSO by 20 days; (b) implement a new inventory management system costing $4 million upfront, expected to reduce DIO by 12 days permanently. Evaluate both proposals using only the working capital arithmetic from this chapter. What information is missing before you could make a final recommendation?
*Tests: applying the $3.8M/day framework to real proposals; identifying the limits of CCC arithmetic alone.*

**6.** A firm's headline working capital (current assets minus current liabilities) has been flat for three quarters at $180 million. DSO has risen from 42 to 58 days. DIO has risen from 55 to 65 days. DPO has risen from 30 to 45 days. Has the firm's operating position improved, deteriorated, or stayed the same? What is masking the change in the headline figure?
*Tests: distinguishing headline working capital from operating working capital; diagnosing the components.*

**7.** Tom, Halverson's treasurer, pulls the AR aging schedule and finds that the share of receivables over 60 days old has grown from 8% to 19% over two quarters, while DSO has risen by only 4 days. What are the two most likely explanations for this pattern, and what additional information would help you distinguish between them?
*Tests: interpreting aging schedules as diagnostic tools; reasoning beyond the aggregate metric.*

---

### Synthesis

**8.** The chapter argues that working capital efficiency is a form of internal financing that competes directly with debt and equity. A colleague pushes back: "Working capital improvement isn't really financing — you're just collecting money you were already owed." Construct the strongest response to this objection, drawing on the chapter's framework. Then state one condition under which your colleague's objection would be at least partially correct.
*Tests: defending the internal capital claim; stress-testing the framework's edges.*

**9.** Halverson is considering acquiring a smaller competitor whose CCC is 110 days versus Halverson's 85 days, with annual COGS of $400 million. If the acquisition price reflects the target's current working capital efficiency, and Halverson's treasury team believes it can bring the target's CCC to 85 days within 18 months, estimate the value of the working capital improvement as a source of acquisition financing. What organizational challenges from this chapter make that 18-month estimate uncertain?
*Tests: applying CCC arithmetic to an M&A context; connecting the organizational reality section to a specific analytical problem.*

---

### Challenge

**10.** The chapter's "Still Puzzling" section admits there is no clean rule for where aggressive DPO management becomes supplier coercion. Using only the frameworks introduced in this chapter (and any external knowledge you bring), propose a practical decision rule a CFO could apply when evaluating whether to extend payable terms with a specific supplier. The rule should be operationalizable — not just "exercise judgment" — and should account for both the financial and the ethical dimensions the chapter names. Then identify the hardest case your rule fails to resolve cleanly.
*Tests: extending the chapter's admitted uncertainty into a constructive framework; finding the boundary conditions of your own answer.*

---

###  LLM Exercise — Chapter 3: Working Capital Is Where the Cash Lives

**Project:** Halverson's Board Memo, Built Across the Course
**What you're building this chapter:** The Working-Capital Reality section of the memo: a cash-conversion-cycle analysis with the binding line item identified and an improvement plan that names dollar impact and an accountable owner.
**Tool:** Claude Project

---

**The Prompt:**

```
I'm working on Halverson's Board Memo. The inside-view read is in `02-inside-read.md`.

Chapter 3 taught:
- **The cash conversion cycle**: $\text{CCC} = \text{DSO} + \text{DIO} - \text{DPO}$
- **The trade-off between liquidity and yield**: a firm holding more working capital than it needs is forgoing return on that capital
- **The structural reasons a profitable firm runs out of cash**: receivables stretch, inventory builds, payables compress

Produce `03-working-capital.md` containing:

1. **The cash-conversion-cycle calculation.** Pull DSO, DIO, DPO from the filings (or from your firm's internal data). Compute CCC. Compare to the prior year and to two named industry peers. Show the arithmetic.

2. **The binding line item.** Of DSO / DIO / DPO, which one is dragging the cycle most? Name it specifically. Do not say "we should improve all three" — name the one that is binding and explain why.

3. **The dollar impact of a one-day improvement on the binding line.** If we cut DSO by one day, that releases (Daily revenue) × 1 day in cash. If we cut DIO by one day, that releases (Daily COGS) × 1 day. Compute the dollar number for *your* firm. State the assumption (e.g., "annual revenue $1.8B implies daily revenue $4.9M, so one DSO day = $4.9M of cash released").

4. **The improvement plan.** Three-to-five specific moves: change credit terms with the top-5 customers; tighten inventory safety-stock policy; renegotiate top-10 supplier payment terms. For each, specify the named operational owner (CFO, COO, controller, head of supply chain) and the expected dollar impact.

5. **The risk side.** One paragraph. What would go wrong if you executed this plan? Customer relationships, supplier reliability, stockout risk on the inventory side. The CFO who proposes a working-capital improvement plan without naming the operational risk is *moving cash, not creating it*.
```

---

**What this produces:** A markdown document `03-working-capital.md` containing the CCC calculation, the binding line item, the dollar impact of a one-day improvement, the named improvement plan, and the operational-risk paragraph.

**How to adapt this prompt:**

- *For your own project:* Substitute your firm for Halverson where Halverson appears; the exercise structure is firm-agnostic. Halverson's named cast (Diane / Priya / Cardinal) is scaffolding — replace as needed.
- *For ChatGPT / Gemini:* Works as-is. For ChatGPT, save the running memo to a Custom GPT instead of a Claude Project. For Gemini, paste the project's accumulated section files into the context window each session.
- *For Claude Code:* Optional — Claude Code can scaffold `analysis/03-ccc.py` that pulls DSO/DIO/DPO from a CSV or directly from EDGAR and computes the year-over-year deltas.
- *For a Claude Project:* Append to the project. The cash released here may fund Plant 4 (Ch 4) without new debt — flag the linkage.

**Connection to previous chapters:** Chapter 2 read the firm; Chapter 3 finds the cash hiding inside it.

**Preview of next chapter:** Chapter 4 takes the firm to capital budgeting — building the NPV-ranked portfolio of projects competing for the freed-up working capital.

---

##  AI Wayback Machine
The ideas in this chapter didn't appear from nowhere. **John Hicks** was publishing *Value and Capital* in 1939 — including the *liquidity preference* framework that explains why firms hold cash even when cash earns less than other assets decades before most people had heard of working capital management and the structural reasons firms hold the liquidity they do. Here's a prompt to find out more — and then make it better.

![John Hicks, c. 1940s. AI-generated portrait based on a public domain photograph (Wikimedia Commons).](images/john-hicks.jpg)
*John Hicks, c. 1940s. AI-generated portrait based on a public domain photograph.*

**Run this:**

```
Who was John Hicks, and how does his concept of *liquidity preference* — the framework explaining why economic actors hold low-yielding cash even when alternatives exist — connect to the chapter's treatment of working capital and the trade-offs in the cash conversion cycle? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.
```

→ Search **"John Hicks economist"** on Wikipedia after you run this. See what the model got right, got wrong, or left out.

**Now make the prompt better.** Try one of these:

- Ask it to explain *liquidity preference* in plain language, as if you've never seen Keynes
- Ask it to compare Hicks's framework to the modern question of why a profitable firm chooses to carry $5B in cash on its balance sheet
- Add a constraint: "Answer as if you're writing the rationale for a target cash balance in a treasury policy"

What changes? What gets better? What gets worse?
