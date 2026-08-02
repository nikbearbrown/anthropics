# Chapter 7 — Capital Structure Theory: The Modigliani-Miller World


## TL;DR

- The most useful theorems are the ones that describe a world that doesn't exist.
- The chapter moves through Warm-up, Application, Synthesis, Challenge, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

*The most useful theorems are the ones that describe a world that doesn't exist.*

---

Here is a claim about the world: it doesn't matter how a firm finances itself.

Take Halverson Industries. It has a plant, a customer base, a workforce, a history of generating cash flows. Suppose that instead of its current mix of debt and equity, Halverson financed itself entirely with equity — no debt, no interest payments, just shareholders. The claim is that Halverson, in this alternative financing universe, would be worth exactly the same amount.

This sounds wrong. Debt is cheaper than equity. More debt means more tax deductions. Financial leverage amplifies returns. Surely the financing mix affects the value?

Franco Modigliani and Merton Miller proved in 1958 that in a specific, carefully described world, the answer is: no, it doesn't. The value of a firm depends on the cash flows its assets generate. Not on how those cash flows are sliced up between creditors and shareholders.

The result is not a description of reality. Modigliani and Miller knew the assumptions required to prove it were not literally true. The point was not to describe the world. The point was to identify exactly which frictions are responsible for capital structure mattering — by proving what happens when all of them are removed.

This chapter is about the proof, what it requires, and what it costs Halverson when one friction is added back: taxes.

---

Let me describe the world MM built the theorem for, because the theorem is only true in this world, and understanding the boundaries is the whole lesson.

Assume four things. No corporate taxes — interest payments are not deductible, and the government treats debt and equity financing neutrally. No bankruptcy costs — if a firm can't pay its debts, the process of renegotiating or defaulting costs nothing, and the assets retain their full value regardless of who owns them. No information asymmetries — everyone, management, shareholders, bondholders, the market, knows the same things about the firm's future cash flows. And finally: investors can borrow and lend at the same rate as the corporation.

| Assumption | What it rules out | What happens to the proof when you relax it |
|---|---|---|
| **No taxes** | Government's preferential treatment of debt over equity | Tax shield on interest is real; debt creates value equal to $T_c \cdot D$ — addressed in Ch 7 (taxes) and Ch 8 (real-world structure) |
| **No bankruptcy costs** | Direct legal/professional fees and indirect customer/supplier flight when a firm becomes distressed | Distress cost is real; trade-off theory emerges — Ch 8 |
| **No information asymmetry** | Management knows things the market doesn't | Issuance signals matter (pecking order, market timing) — Ch 8, Ch 10 |
| **Equal borrowing rates** | Investors can replicate corporate leverage at the same rate | Investor borrowing rate exceeds corporate; corporate leverage adds value the investor can't undo — Ch 8 |

In this world, the MM theorem holds. Outside it — as soon as you relax any of these four assumptions — you are no longer in MM's world, and the theorem no longer holds in its clean form.

This is a precise mathematical structure, not an empirical claim. Modigliani and Miller were not saying "we think these assumptions approximately hold." They were saying: given these assumptions, the following is necessarily true. The result is deductive. Whether you find it convincing as a description of reality is a different question from whether the proof is valid.

The proof is valid.

---

Here is the engine of the theorem. It is worth going through carefully, because the logic is both elegant and instructive about what kind of claim is being made.

Suppose two firms — call them L (levered, with debt) and U (unlevered, all equity) — have identical operating cash flows. Same industry, same size, same customers, same products. The only difference is how they're financed. L has debt; U doesn't.

MM's Proposition I says these two firms must have the same total value. If they don't, there's a money machine, and money machines don't persist.

Suppose $V_L > V_U$ — the levered firm is priced higher than the unlevered one. An investor who holds shares in the levered firm can do the following: sell those shares, borrow on personal account at the same rate the firm borrowed, and buy shares in the unlevered firm instead. The personal borrowing replicates the leverage the firm had. The investor now holds the same cash flow stream — same operating returns, same interest payments, same residual — but paid less for it. That's a free lunch. Investors will exploit it, selling L and buying U, until prices equalize.

The reverse arbitrage works in the other direction if $V_U > V_L$. Either way, any price difference is eliminated by rational investors acting in their own interest.

$$V_L = V_U$$

This is Proposition I. The value of the firm is independent of capital structure, in a world where investors can execute this arbitrage freely.

![The arbitrage mechanism as a two-step flow ](images/07-capital-structure-theory-the-modigliani-miller-world-fig-01.png)
*Figure 7.1 — The arbitrage mechanism as a two-step flow *

The leverage hasn't disappeared. L's debt is still there. What's changed is the distribution of the firm's value between debt and equity holders. Adding debt shrinks the equity claim and grows the debt claim. The pie doesn't change size. The slices change.

Proposition II follows directly. If the total value is fixed and we're adding debt — a fixed-obligation claim that gets paid first — the equity holders are taking on more residual risk. They're last in line if the firm runs into trouble. They will demand a higher return for that risk. The cost of equity rises as leverage rises.

$$R_E = R_U + \frac{D}{E} \times (R_U - R_D)$$

Where $R_U$ is the return equity holders would require on an unlevered version of the firm, $R_D$ is the cost of debt, and $D/E$ is the leverage ratio. As $D/E$ rises, $R_E$ rises linearly. The equity gets more expensive in exact proportion to the risk being transferred onto equity holders.

The implication for the weighted average cost of capital is that it doesn't change. Add cheap debt, and you also raise the cost of the now-riskier equity. The WACC stays flat. Firm value stays flat. This is internally consistent and theoretically tight. It is also the reason the result sounds paradoxical: financial leverage is supposed to create value by using cheap debt. MM says: yes, debt is cheaper, but the equity gets more expensive by exactly the same amount. The two effects cancel.

In the MM world, the cancellation is exact.

![Proposition II visualization ](images/07-capital-structure-theory-the-modigliani-miller-world-fig-02.png)
*Figure 7.2 — Proposition II visualization *

---

The arbitrage argument rests on the fourth assumption: investors can borrow at the same rate as the firm. This is the quiet load-bearing pillar of the whole proof.

If a corporation can issue bonds at 5% and individual investors can only borrow at 7%, then corporate leverage is not replicable by personal leverage. The money machine doesn't work. Investors can't arbitrage away the price difference because doing so on personal account costs more. The proof breaks.

This is worth sitting with carefully. MM didn't prove "leverage doesn't matter." They proved "leverage doesn't matter *if investors can replicate it*." In a world where individual borrowing is more expensive than corporate borrowing — which is our world — there is some value in corporate leverage that can't be arbitraged away.

The honest statement of Proposition I is: corporate capital structure is irrelevant *to the extent that investors can replicate it*. Where personal leverage is costly or restricted — for tax reasons, institutional reasons, transaction cost reasons — corporate leverage can create value through a channel MM's proof explicitly excluded.

MM knew this. They stated the assumption explicitly. The theorem is honest about its own limits. That honesty is part of what makes it a good piece of science.

---

Before going further, I want to explain why a theorem proved in a world that doesn't exist belongs in a book about decisions made in a world that does.

The way you understand a complex system is to first understand what happens when all the complexity is removed, and then add the complexity back one piece at a time. Physicists do this constantly: frictionless surfaces, massless strings, point charges in a vacuum. None of those exist. All of them are useful. They're useful because they let you see each force separately, rather than all tangled together.

Without MM, the question "why does Halverson have debt?" has ten entangled answers: taxes, signaling, bankruptcy avoidance, agency costs, debt overhang, market timing, pecking order preferences. You can't tell which force is dominant because you can't see them individually.

With MM as the baseline, the question becomes: which assumption is being violated, and what is the value impact of that violation? Each deviation from the MM world is a separate force with a separate direction and a separate magnitude you can estimate. You can price them one at a time, which you cannot do when they're all running simultaneously.

The MM world is the zero. Every real capital structure result is a deviation from zero — with a direction and a magnitude. The framework converts a philosophical question into an arithmetic one. That is the contribution, and it is larger than the specific theorem.

---

Now let me relax the first assumption — no taxes — and see what actually happens to firm value.

Allow corporate taxes at rate $T$. Interest payments are now deductible from taxable income. Equity returns — dividends, capital gains — are not deductible. This breaks the symmetry between debt and equity immediately. Debt has a tax advantage that equity doesn't. Each dollar of interest saves the firm $T$ in taxes. Over the life of the debt, the present value of those savings is the tax shield.

Modigliani and Miller extended their own theorem in 1963 to account for this. With corporate taxes, Proposition I becomes:

$$V_L = V_U + T \times D$$

The levered firm is worth more than the unlevered firm by the present value of the tax shield. With permanent debt, that present value is simply $T \times D$ — the tax rate times the dollar value of debt outstanding. Financing does matter once taxes exist. The irrelevance result is gone.

For Halverson, with a marginal tax rate around 24% and existing long-term debt in the range of $400M, the tax shield on existing debt is on the order of:

$$\text{Tax shield value} \approx 0.24 \times \$400M = \$96M$$

That $96M is not a cash flow from operations. It is value created entirely by the financing choice. Halverson's enterprise value is approximately $96M higher than it would be if the firm were financed entirely with equity — not because the plants run better, not because customers pay more, but because of the tax code.

Now apply the same logic to Plant 4. If the $50M expansion is debt-financed rather than equity-financed, the new debt creates an incremental tax shield:

$$\text{Plant 4 incremental tax shield} = 0.24 \times \$50M = \$12M$$

That $12M is the value of the financing choice itself — distinct from the operational value of the plant, which is the NPV Maya calculated in Chapter 4. The total value created by accepting and debt-financing Plant 4 is approximately the operational NPV plus this $12M. The two sources of value are separable and addable because the MM framework is clean enough to let you distinguish them.

![Value decomposition for Plant 4 ](images/07-capital-structure-theory-the-modigliani-miller-world-fig-03.png)
*Figure 7.3 — Value decomposition for Plant 4 *

This is a concrete, calculable number. It's why the MM framework belongs here rather than in a history-of-finance chapter. The tax shield isn't an abstraction. It's a number you can put in a memo.

---

$V_L = V_U + T \times D$ creates an immediate problem, and I want to be direct about it rather than paper it over.

If every dollar of debt adds $T$ dollars of value, the optimal capital structure is 100% debt. Every firm should borrow as much as it possibly can. The firm that borrows the most is the firm that maximizes value.

This is obviously not what firms do. Halverson has $400M of debt on a multi-billion dollar asset base. It is not close to fully debt-financed, even though the tax shield formula says it should be. No healthy firm carries debt approaching 100% of its assets.

The 1963 MM-with-taxes result is still not a complete description. It added one friction — taxes — back to the original model, but the other frictions are still excluded. Specifically, bankruptcy costs are still zero in the extended model. You can pile on debt indefinitely with no downside because default costs nothing. In the real world, financial distress is expensive — lawyers, lost customers, distracted management, forced asset sales at depressed prices. The threat of distress keeps firms from issuing maximum debt even when the tax shield is valuable. The distress cost is a friction that acts in the opposite direction from the tax shield, and until you put a number on it, you can't find the optimal balance.

This tension is real and intentionally left unresolved in this chapter. Taxes push toward more debt. Something else pushes back with roughly equal force for the typical healthy industrial firm. Chapter 8 identifies what that something else is and prices it.

What this chapter has established is the mechanism and the magnitude on one side of the trade-off. The tax shield is $T \times D$. For Plant 4, that's $12M. The case against unlimited debt rests on a distress cost that must exceed $12M per $50M of additional leverage before the rational choice switches away from debt. That's the specific question MM allows you to ask. Before MM, you couldn't ask it in that form.

---

I want to end on what the 1958 paper's contribution actually was, because it is consistently underappreciated.

Before MM, capital structure was discussed in terms of rules of thumb, practitioner intuitions, and loosely connected empirical observations. There was no theoretical framework that said: here is the world in which financing doesn't matter, and here are the specific mechanisms by which the real world differs from it.

What Modigliani and Miller contributed was not the result that financing doesn't matter — that result is only true in a frictionless world and everyone who thought about it for five minutes already suspected it wasn't literally true. What they contributed was the method: specify your world precisely, prove what follows in that world, and then treat every real-world deviation as a named, priceable force.

Every subsequent advance in capital structure theory — the trade-off theory, the pecking order, the market-timing hypothesis, the agency cost framework — is built on this method. Each one identifies a specific friction, shows how it deviates from MM, and prices the deviation. The whole intellectual structure of modern corporate finance rests on the foundation MM laid, not because their specific result is right but because their method of asking questions is right.

Maya, reading the paper for the second time, is doing the right thing. The paper isn't the answer to the CFO's question about Plant 4. It's the vocabulary and the logical structure that makes the CFO's question answerable in a way that can be put in front of a board.

The MM world does not exist. The MM logic is how you navigate the one that does.

---

## Exercises

### Warm-up

**1.** MM Proposition I rests on four assumptions. For each one, state in a single sentence what real-world friction it excludes and which direction that friction pushes firm value once added back — toward more debt being optimal, toward less, or ambiguously. *(Tests: understanding of the four assumptions as a map of the deviations chapters ahead will price.)*

**2.** Halverson issues $50M in new permanent debt at a 6% coupon. The marginal tax rate is 24%. Calculate the annual tax shield in dollars and the present value of the tax shield under the MM-with-taxes assumption. Then state one reason the present value calculation overstates the real benefit in practice. *(Tests: mechanical application of the tax shield formula plus awareness of the permanent-debt simplification.)*

**3.** A classmate argues: "MM Proposition II says leverage increases the cost of equity, so firms should avoid debt to keep their equity cheap." Identify the error. What does Proposition II actually imply about the weighted average cost of capital as leverage rises, and why does that conclusion follow from the pie analogy? *(Tests: correct reading of Prop II and the WACC implication.)*

---

### Application

**4.** Firm A is all-equity financed with a cost of equity of 9%. It has $200M in assets. Firm B is identical in operations but carries $80M in debt at a cost of 5%. Using MM Proposition II, calculate Firm B's cost of equity. Then verify that Firm B's WACC equals Firm A's cost of equity, showing your work. *(Tests: quantitative application of Prop II and WACC invariance.)*

**5.** A venture-backed startup argues it should use no debt because "we want to keep equity costs down and avoid the bankruptcy risk that would scare off customers." Evaluate this reasoning using MM's framework. Which of the four assumptions is the startup implicitly relaxing that makes its concern legitimate? What would MM say if all four assumptions held? *(Tests: applying the MM framework to a non-Halverson context, identifying which friction makes the startup's intuition correct.)*

**6.** Halverson is considering two financing options for Plant 4: $50M in new 10-year debt at 6.5%, or a $50M equity offering. Using $T \times D$ to price the tax shield, calculate the value difference between the two options under MM-with-taxes assumptions. Then name two factors the formula ignores that could reverse the ranking in practice. *(Tests: using the extended MM formula as a decision tool while recognizing its limits.)*

**7.** The chapter states that before MM, capital structure was discussed through "rules of thumb, practitioner intuitions, and loosely connected empirical observations." Identify one rule of thumb that corporate finance practitioners commonly used before 1958 (e.g., "debt-to-equity ratios should not exceed 1:1" or "mature firms use debt, growth firms use equity"). Explain why MM's framework converts that intuition into a priceable question rather than a heuristic. *(Tests: connecting the historical context to the methodological contribution.)*

---

### Synthesis

**8.** The chapter uses the physicist's analogy: frictionless surfaces, massless strings, point charges. Identify a specific place in your Chapter 4 NPV analysis where an analogous simplifying assumption is at work — a case where the model excludes a real friction in order to produce a tractable answer. For that assumption, state what the MM-style question would be: "which friction is being excluded, and what happens to the result when you add it back?" *(Tests: cross-chapter transfer of the MM method to capital budgeting; connects Chapters 4 and 7.)*

**9.** The chapter ends with an unresolved tension: $V_L = V_U + T \times D$ implies 100% debt is optimal, but firms don't do this. Without reading Chapter 8, construct the strongest possible argument for what force must be pushing back against the tax shield, using only the logic already established in this chapter — specifically, the list of frictions MM excluded. Your answer should predict the direction and rough magnitude of the countervailing force, not just name it. *(Tests: using MM's own exclusion list to anticipate the trade-off theory before it is taught; rewards integrative reasoning.)*

---

### Challenge

**10.** The chapter claims that MM's real contribution was methodological — not the irrelevance result itself, but the practice of "specify the frictionless world precisely, then price each deviation." Construct the strongest possible objection to this claim: argue that a finance practitioner who learned only the irrelevance result (without the method) would make systematically better capital structure decisions than one who had no theory at all. Then identify the specific type of decision where the method, not just the result, is genuinely necessary — where the irrelevance result alone would lead the practitioner astray. *(Tests: stress-testing the chapter's central methodological claim; distinguishes knowing a result from knowing how to use a framework.)*

---

*Tags: Modigliani-Miller, Proposition I, Proposition II, tax shield, capital structure, arbitrage, weighted average cost of capital, corporate taxes*

---

###  LLM Exercise — Chapter 7: Capital Structure Theory: The Modigliani-Miller World

**Project:** Halverson's Board Memo, Built Across the Course
**What you're building this chapter:** The MM Baseline section of the memo: a precise statement of the MM theorem applied to your firm, with each of the four assumptions stress-tested for fit.
**Tool:** Claude Project

---

**The Prompt:**

```
I'm working on Halverson's Board Memo. The portfolio (`04`) and WACC (`05`) sections are in.

Chapter 7 taught:
- **MM Proposition I (frictionless)**: under no taxes, no bankruptcy costs, no information asymmetry, and equal borrowing rates, firm value is independent of capital structure
- **MM Proposition II**: as leverage rises, expected return on equity rises proportionally — the cost of equity is increasing in the debt ratio
- The point is *not* that MM is true in the real world — it's that MM identifies which frictions matter

Produce `07-mm-baseline.md` containing:

1. **State MM precisely for your firm.** One paragraph. "If Halverson operated in the MM world, its enterprise value would be \$X billion regardless of whether it carried 20% debt or 80% debt or zero debt. The cash flows from operations are the only thing that matters."

2. **Walk through each of the four assumptions and ask: does it hold?**
   - **No corporate taxes.** Halverson pays a 24% marginal tax rate. *Assumption violated; tax shield is real.*
   - **No bankruptcy costs.** Halverson is investment-grade; bankruptcy costs are low but not zero. *Assumption partially violated.*
   - **No information asymmetry.** Halverson management knows things the market doesn't (covenant cushion, customer concentration trajectory). *Assumption clearly violated.*
   - **Equal borrowing rates for firm and investors.** Halverson borrows at 5.2% (Chapter 5); a retail investor borrows at 8% on margin. *Assumption clearly violated.*

3. **Rank the violations by impact on Halverson's specific capital-structure choice.** Which violation matters most for *your* firm? An investment-grade industrial: tax shield dominates. A growth-stage tech firm: information asymmetry dominates. A real-estate firm: bankruptcy cost dominates.

4. **State the MM-derived value of debt.** Present value of the tax shield = $T_c \cdot D$ at the simplest treatment. Compute this number for your firm at the current debt level and at a +20% debt level. The difference is the *MM-with-taxes* case for adding debt.

5. **The closing sentence.** The MM baseline tells you that adding debt to Halverson is worth approximately $T_c \cdot \Delta D$ in tax-shield value, *before* considering bankruptcy cost, agency cost, and signaling — which is what Chapter 8 takes up.
```

---

**What this produces:** A markdown document `07-mm-baseline.md` containing the precise MM statement, the four-assumption stress-test ranked by impact on your firm, the MM-with-taxes tax-shield value, and the framing for Chapter 8.

**How to adapt this prompt:**

- *For your own project:* Substitute your firm for Halverson where Halverson appears; the exercise structure is firm-agnostic. Halverson's named cast (Diane / Priya / Cardinal) is scaffolding — replace as needed.
- *For ChatGPT / Gemini:* Works as-is. For ChatGPT, save the running memo to a Custom GPT instead of a Claude Project. For Gemini, paste the project's accumulated section files into the context window each session.
- *For Claude Code:* Not needed for this section.
- *For a Claude Project:* Append to the project. The MM baseline is the foundation — Chapter 8 builds the real-world adjustments on top of it.

**Connection to previous chapters:** Chapters 1–6 analyzed projects; Chapter 7 starts the firm-level financing analysis with the simplest possible baseline.

**Preview of next chapter:** Chapter 8 takes the MM baseline and adds back the frictions — producing the recommended target debt-to-capital ratio for the firm.

---

##  AI Wayback Machine
The ideas in this chapter didn't appear from nowhere. **Merton Miller** was co-publishing the *Modigliani-Miller theorem* in 1958 — the result that, under specific frictionless-market assumptions, the value of a firm is independent of how it is financed decades before most people had heard of capital structure theory in the Modigliani-Miller world. Here's a prompt to find out more — and then make it better.

![Merton Miller, c. 1990. AI-generated portrait based on a public domain photograph (Wikimedia Commons).](images/merton-miller.jpg)
*Merton Miller, c. 1990. AI-generated portrait based on a public domain photograph.*

![Merton Miller](../images/merton-miller-62o.png)

*Puppet Art by [Nik Bear Brown](https://www.nikbearbrown.com/).*

**Run this:**

```
Who was Merton Miller, and how does the 1958 *Modigliani-Miller theorem* — that under perfect-market assumptions a firm's value is independent of its debt-equity mix — connect to the chapter's argument that the MM result is most useful as a *baseline* whose required violations name the real determinants of capital structure? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.
```

→ Search **"Merton Miller"** on Wikipedia after you run this. See what the model got right, got wrong, or left out.

**Now make the prompt better.** Try one of these:

- Ask it to explain *the MM irrelevance theorem* in plain language, as if you've never seen capital-structure mathematics
- Ask it to compare Miller's 1958 paper to the messier 1963 paper accounting for taxes — what changed and why it matters
- Add a constraint: "Answer as if you're writing the case for *why MM is the right baseline* in a corporate finance class"

What changes? What gets better? What gets worse?
