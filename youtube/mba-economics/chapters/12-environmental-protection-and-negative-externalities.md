# Chapter 12 — Environmental Protection and Negative Externalities

*When the price doesn't include the cost — and what to do about it.*

In 1952, a thick fog settled over London. It lasted five days. By the time it lifted, an estimated 4,000 people were dead. Subsequent epidemiological work has raised that number — some estimates reach 12,000, accounting for deaths in the months that followed from respiratory damage done during the fog.

It was not a natural fog. It was coal smoke — from millions of domestic heating fires, from industrial production, from power generation — trapped by still, cold air. Each individual coal fire was a perfectly ordinary economic transaction: a homeowner bought coal, a factory burned coal, a power station generated electricity. Each transaction had a private buyer, a private seller, and a private price. None of those prices reflected what that fire contributed to the killing fog.

That gap — the cost of the smoke that didn't show up in the price of the coal — is the subject of this chapter.

Economists call it a **negative externality**: a cost imposed on third parties by a transaction, a cost the buyer and seller never agreed to bear and never paid. The fire that warms my house is mine to enjoy. The smoke filling my neighbor's lungs is theirs to deal with. The market priced the warmth. It did not price the smoke.

When the price is wrong in this way, the market produces the wrong quantity. It produces too much of whatever generates the harm — too much coal burning, too much tailpipe emission, too much carbon, too much antibiotic overuse. The diagnosis is precise. The treatment options differ, and choosing among them is what most environmental policy is actually about.

---

## The Geometry of the Problem

Start by drawing the market failure.

A factory produces widgets. The factory's private supply curve represents its private marginal cost — labor, materials, capital. The demand curve represents consumers' marginal benefit. They cross at the market equilibrium: some quantity $Q_{market}$, some price $P_{market}$.

But the factory also emits sulfur dioxide. Every ton of widgets costs the neighbors — in health effects, in corroded buildings, in reduced visibility — some additional amount per unit. Call it $d$ per unit of output. This cost is real. It's paid. It just isn't paid by the buyer or the seller.

The *socially efficient* supply curve lies above the private one, shifted up by $d$ at every quantity. Where the social supply curve crosses demand is the efficient quantity $Q^*$ — which is *lower* than $Q_{market}$. The market, ignoring $d$, produces too much. The wedge between $Q_{market}$ and $Q^*$ represents a triangle of social cost — a deadweight loss from overproduction. This is the geometry of the externality.

<!-- → [CHART: Negative externality diagram — standard supply-demand. Downward-sloping demand curve. Upward-sloping private supply curve (marginal private cost). A second supply curve above it labeled "Social supply = MPC + external cost," shifted up by the external damage d. Three points marked: market equilibrium (Q_market, P_market) at private supply ∩ demand; socially efficient equilibrium (Q*, P*) at social supply ∩ demand; and the triangle between them labeled deadweight loss. Caption: "The market equilibrium ignores the external cost d. Every unit produced between Q* and Q_market costs society more to produce than it's worth to consumers. The triangle is the deadweight loss from the externality."] -->

The mirror image — a positive externality, where third parties receive benefits the market ignores — produces underproduction instead of overproduction. We'll take that up in Chapter 13. For this chapter, the negative case: the market price is too low (doesn't include $d$), the quantity too high, and the problem is how to close the gap.

---

## The First Approach: Set Limits and Enforce Them

The first generation of U.S. environmental regulation, beginning in the late 1960s and accelerating through the 1970s, took the most direct approach: tell firms what they may and may not do. The Clean Air Act, the Clean Water Act, and their progeny specified directly — each smokestack emits no more than X tons per year; each car must have a catalytic converter meeting Y specification; each factory must install Z abatement technology.

This is **command-and-control** regulation, and it worked. From the late 1970s through the early 2020s, U.S. emissions of major air pollutants — sulfur dioxide, nitrogen oxides, particulates, carbon monoxide — fell substantially even as the economy grew several-fold. The London fog of 1952 has no modern equivalent in any wealthy country with serious environmental regulation. The command framework gets a substantial portion of the credit.

It also has two structural problems that become more visible as the easy reductions get made and the remaining reductions get expensive.

The first problem is **inefficiency**. Command-and-control imposes the same standard on every firm regardless of cost. A new factory might cut emissions 90 percent for $1 million. An old factory across town might spend $50 million to cut only 60 percent. Telling both to meet the same percentage reduction means society spends $51 million for a level of total reduction it could have achieved for much less — if the cheap-to-cut firm cut more and the expensive-to-cut firm cut less. The command system has no mechanism to discover which firm should cut what; it doesn't ask.

The second problem is **static incentives**. Once a firm has met the regulatory standard, it has no further incentive to reduce. If a new technology becomes available that could cut emissions further at low cost, the firm wouldn't adopt it — the benefit is zero and the cost is positive. Command-and-control rewards meeting the line. It ignores everything beyond.

These structural problems pushed economists toward market-based alternatives. The two main ones were developed over decades of theory and then implemented in practice. They solve the efficiency and incentive problems, but they introduce new complications worth being honest about.

<!-- → [INFOGRAPHIC: Why command-and-control is inefficient — two-firm illustration. Firm A (new factory): bar showing cost to cut 90% = $1M. Firm B (old factory): bar showing cost to cut 60% = $50M. Scenario 1 (equal standard — both cut 70%): total cost = $51M, total reduction = 130%. Scenario 2 (efficient allocation — Firm A cuts 90%, Firm B cuts 50%): total cost = much lower, same or greater total reduction. Caption: "Equal percentage standards ignore cost differences. If Firm A can cut cheaply and Firm B cannot, society overspends by having both meet the same standard. The efficient solution lets Firm A cut more and Firm B cut less — same total reduction, much lower total cost."] -->

---

## The Pigouvian Tax

The economist A.C. Pigou, writing in 1920, proposed a solution so clean it is worth quoting in structure if not in formula: tax the externality at exactly the rate of the external damage.

A factory emitting a ton of sulfur dioxide that does $500 worth of harm downwind should pay a $500 tax per ton. Now the factory treats the tax exactly like any other input cost. It will reduce emissions until the marginal cost of the next ton of abatement just reaches $500 — the tax rate. If it's cheaper to cut emissions than to pay the tax, cut. If it's cheaper to pay the tax than to cut, pay.

The efficiency result follows automatically. Every firm in the economy faces the same tax rate. Every firm reduces until its marginal abatement cost equals the tax. Therefore every firm's marginal abatement cost equals every other firm's. The same total reduction gets achieved at the lowest possible total cost, because no firm could rearrange who cuts how much and get more reduction per dollar.

<!-- → [CHART: Marginal abatement cost and the Pigouvian tax — diagram with quantity of emissions reduced on the horizontal axis and marginal abatement cost (MAC) on the vertical axis. Two upward-sloping MAC curves: Firm A (steep — expensive to abate) and Firm B (flat — cheap to abate). Horizontal line at the tax rate T. Firm A reduces to where its MAC = T (small reduction). Firm B reduces to where its MAC = T (large reduction). Caption: "Both firms face the same tax T and each reduces until MAC = T. Firm B, with lower abatement costs, reduces more. Firm A, with higher abatement costs, reduces less and pays more tax. Total reduction is achieved at minimum cost without the regulator knowing either firm's cost curve."] -->

<!-- → [CHART: Pigouvian tax — supply-demand diagram showing external cost d added as a tax. Original market at (Q_market, P_market). Tax shifts private supply curve up by d, producing new equilibrium at (Q*, P* + d) where Q* equals the socially efficient quantity. The tax revenue rectangle shown between P_market and P* + d at quantity Q*. Caption: "The Pigouvian tax set at exactly the marginal external damage shifts the market equilibrium to the socially efficient quantity. Firms pay P* + d; consumers receive the good at Q*; the government collects the rectangle as revenue. The deadweight loss from the externality disappears."] -->

The regulator's information problem is also smaller than under command-and-control. Under the command approach, the regulator has to know each firm's cost structure to set efficient firm-specific standards. Under a Pigouvian tax, the regulator only needs to know the aggregate damage per unit of emission — and lets the firms sort themselves out individually.

Carbon taxes in Sweden, Norway, Finland, France, and the United Kingdom have used this framework at scale. The U.S. has used it less, for reasons that are more political than economic. The resistance to "new taxes" in the American political environment exceeds the resistance to "new regulations," even when the regulations are more expensive for society. This is a fact about political economy, not a fact about the instrument.

---

## Cap-and-Trade

The second market-based instrument solves a problem the Pigouvian tax has: what if the regulator is more confident about the right *quantity* of emissions than about the right *price*?

**Cap-and-trade** starts from the quantity side. The regulator sets a total cap — say, 10 million tons of sulfur dioxide per year nationally — and issues that many tradable permits. Every firm must hold one permit for each ton it emits. Permits can be bought and sold freely.

The market does the allocation work. A firm with cheap abatement options reduces its emissions and sells its surplus permits. A firm with expensive options buys permits and emits more. The market price of permits settles at the level where buyers and sellers are just indifferent — which is the marginal cost of abatement at the cap level. This is exactly what a well-calibrated Pigouvian tax would have produced.

The U.S. ran this experiment at scale starting in 1990, applying cap-and-trade to sulfur dioxide under amendments to the Clean Air Act. The result: a 65 percent reduction in SO₂ emissions, at roughly 25 to 50 percent lower compliance cost than command-and-control would have achieved. It is one of the cleaner policy successes in the environmental economics literature.

The European Union runs a large cap-and-trade program for carbon dioxide (the EU Emissions Trading System). California runs its own. Both work, with ongoing debates about how to set the cap and how to handle permit price volatility.

<!-- → [TABLE: Cap-and-trade vs. Pigouvian tax — side-by-side comparison. Rows: What the regulator sets / What is uncertain / How firms respond / Cost-effectiveness / Who bears price risk / Best suited for / Real-world example. Columns: Pigouvian Tax | Cap-and-Trade. Values: Pigouvian Tax — sets price, quantity uncertain, firms minimize cost, cost-effective, firms (input price uncertainty), targets where damage per unit is well-known (carbon), Sweden carbon tax; Cap-and-trade — sets quantity, price uncertain, firms trade permits, cost-effective, firms (permit price volatility), targets where quantity certainty matters (acid rain), US SO₂ program / EU ETS. Caption: "The two instruments are theoretically equivalent under certainty. Under uncertainty, the choice depends on whether quantity or price certainty is more valuable — and on the shape of the marginal abatement cost curve."] -->

The difference between the two instruments shows up most clearly under uncertainty. If abatement turns out to be more expensive than expected, a cap-and-trade system produces permit price spikes — firms face large unexpected compliance costs, but the quantity target is still hit. A Pigouvian tax produces quantity uncertainty instead — firms know their cost, but the reduction achieved might be more or less than targeted if the cost-of-abatement estimate was off. Which uncertainty you prefer depends on the specific situation. For climate change, where quantity targets are tied to physical tipping points, cap-and-trade's quantity certainty has appeal. For local air pollution where the target is a price signal, the tax may be cleaner.

---

## The Coase Theorem and Its Limits

In 1960, the economist Ronald Coase made an observation that reframed the entire externality debate.

He pointed out that externalities exist where property rights are unclear. The factory pollutes the air over my neighborhood. Who has the right — the factory to emit, or me to breathe clean air? Both assignments are coherent; the legal system has to choose.

Coase's theorem says: if property rights are clearly assigned, and if the affected parties can negotiate without transaction costs, they will bargain their way to the efficient outcome regardless of who holds the initial right.

Walk through it. Suppose I hold the right to clean air. The factory wants to emit. It can do so only by paying me enough to compensate for the harm. I'll accept payment that exceeds the damage; the factory will pay if its profit from emitting exceeds the payment. The negotiation produces exactly as much emission as is worth the cost — the efficient quantity.

Now reverse the rights. The factory has the right to emit. I can stop it only by paying the factory. I'll pay if the harm to me exceeds my payment; the factory accepts if my payment exceeds its profit from emitting. The outcome — how much the factory emits — is the same. The distribution of money is different. The efficient quantity is identical.

<!-- → [TABLE: Coase theorem — two property-right assignments. Two-column table. Column 1: Factory holds right to emit. Column 2: Homeowner holds right to clean air. Rows: Who must initiate negotiation / Who pays whom / What determines the amount of pollution / Efficient outcome achieved? / Distribution of surplus. Caption: "The theorem's punch line: the efficient quantity of pollution doesn't depend on who holds the right. The distribution of money does. This is why Coase said property-rights assignment is a question of equity, not efficiency — under the theorem's assumptions."] -->

The assumptions are load-bearing. The theorem works for small-numbers situations where the parties know each other, can negotiate directly, and can verify compliance. Two neighboring landowners, an upstream and downstream water user, a factory and an adjacent homeowner — Coase logic applies. It has informed water-rights trading in some U.S. states and fisheries quota systems.

It does not work for the London fog. When the externality involves millions of emitters and millions of victims, the transaction costs of organizing a negotiation are prohibitive. You cannot negotiate on behalf of all Londoners with all coal-fire owners. The Coase mechanism fails exactly where the externality problem is largest.

---

## The Hardest Case: International Externalities

All four mechanisms I've described work within a jurisdiction with functioning enforcement. The hardest externalities cross national borders.

The largest is climate change. A coal plant in China emits CO₂ that contributes to warming everywhere. A reforestation project in Brazil sequesters carbon that benefits everyone. No single country can solve this externality because the benefits of action accrue globally while the costs are borne domestically.

The structure is a giant prisoner's dilemma played by sovereign nations. Each country's short-term interest is to have *other* countries reduce emissions while it free-rides — getting the climate benefit without the compliance cost. If every country acts on that interest, no one reduces. The cooperative outcome — everyone reduces, everyone benefits from a stable climate — requires international coordination that is hard to compel and hard to enforce.

<!-- → [TABLE: International climate prisoner's dilemma — two-by-two payoff matrix. Rows: Country A reduces / Country A free-rides. Columns: Country B reduces / Country B free-rides. Cells: (Both reduce): moderate cost to each, large shared climate benefit — net gain for both; (A reduces, B free-rides): A bears full cost, B gets free benefit — A loses, B gains most; (A free-rides, B reduces): B bears full cost, A gets free benefit — B loses, A gains most; (Both free-ride): no cost to either, no climate benefit — both lose slowly. Dominant strategy: free-ride. Caption: "Free-riding is the dominant strategy for each country individually. But if every country free-rides, the cooperative climate benefit disappears. This is why climate negotiations are hard: the structure of the game pushes every player toward the outcome that's worst for everyone."] -->

Within this constraint, the instruments we've discussed apply at national or regional scale: EU ETS, California cap-and-trade, Sweden's carbon tax, the U.K.'s carbon price floor. Each is partial. Together, they address some of the problem some of the time. The coordination problem at the international level is the part that doesn't get easier by choosing a better instrument. It gets easier only by building institutions that can sustain and verify cooperation — and that is a problem outside the scope of this chapter's tools.

---

## The Menu and What Determines the Order

Pull back. The market failure is the same in every case: the price is too low, production is too high, the gap between private and social cost generates deadweight loss. Four instruments close the gap differently.

**Command-and-control** sets a limit and enforces it. Effective at hitting explicit targets. Inefficient because it doesn't allow firms with different costs to trade reductions. Politically familiar.

**Pigouvian taxes** price the externality directly. Cost-effective; ongoing incentive to innovate; politically hard in "anti-tax" environments; needs good damage estimates.

**Cap-and-trade** sets a quantity and lets markets allocate. Cost-effective; hits quantity targets reliably; introduces permit price volatility; works well where emissions are measurable.

**Property rights / Coase** assigns the right and lets parties bargain. Elegant; efficient under the assumptions; fails for large-numbers externalities where transaction costs are prohibitive.

The London fog of 1952 led directly to the U.K. Clean Air Act of 1956 — command-and-control, because the political moment demanded visible prohibition, not price signals. The U.S. acid-rain problem was addressed first by command-and-control, then more cost-effectively by cap-and-trade in 1990, because the policy community had learned from the first generation of regulation. The carbon problem is being addressed unevenly, country by country, with all four tools deployed somewhere and none deployed everywhere.

The choice among instruments is not purely technical. It's political and institutional. Command-and-control survives partly because "we banned X" is easier to communicate than "we imposed an optimal Pigouvian tax on X." Cap-and-trade has the word "trade" in it, which sounds market-friendly, which is why it sometimes passes where taxes don't. The economics tells you the trade-offs. The politics decides what gets enacted. The model's job is to make the trade-offs visible so that the political choice, whatever it is, is at least made honestly.

<!-- → [TABLE: Four instruments compared — rows: Command-and-Control, Pigouvian Tax, Cap-and-Trade, Property Rights (Coase). Columns: What it sets / Cost-effectiveness / Innovation incentive / Information required by regulator / Handles large-numbers externalities? / Real-world example. Caption: "No instrument dominates on every dimension. Command-and-control is politically tractable but expensive. Pigouvian taxes are efficient but politically hard. Cap-and-trade is efficient and quantity-certain but introduces price risk. Coase works for small-numbers cases only. Policy is usually a second-best choice on this menu."] -->

---

## LLM Exercises

**Exercise 1 — Identify the externality.** Pick a market transaction in your daily life (driving to work, eating beef, online shopping with overnight delivery, streaming a high-resolution movie). Ask an LLM to identify the negative externalities the transaction may produce, who bears them, and roughly how large they might be. Push the LLM to be specific about magnitudes and to flag where it's guessing.

**Exercise 2 — Compare instruments on one case.** Tell an LLM you're designing a policy to reduce nitrogen runoff from agricultural fertilizer use. Ask it to compare command-and-control, a Pigouvian tax, and a cap-and-trade approach for this specific case. A good answer notes that diffuse non-point pollution (like fertilizer runoff) is hard for cap-and-trade because emissions are not easily measured at the source.

**Exercise 3 — Coase in practice.** Tell an LLM about two adjacent property owners — one owns a hog farm, the other a vacation rental — and the smell from the hog farm is hurting the rental's bookings. Ask the LLM to walk through the Coase-theorem analysis: what's the efficient outcome, how does it depend on who holds the property right, and what real-world frictions might prevent the parties from reaching it? Evaluate the LLM's handling of transaction costs.

**Exercise 4 — Carbon tax design.** Ask an LLM to design a U.S. carbon tax that would meet two political constraints: (a) revenue-neutral (the tax revenue is returned to households as a dividend or rebate); (b) gradually rising over a decade. Then ask: which industries would face the largest cost increases, and what would happen to overall emissions over a decade? Push the LLM to be specific about which sectors decarbonize fastest under such a regime.

**Exercise 5 — Why climate is hard.** Ask an LLM to explain why climate change is harder to address than the U.S. acid-rain problem of the 1980s, even though both are pollution externalities. A correct answer hits at least: scale (global vs. regional), free-rider problem at country level, longer time horizon, uncertain benefits, and the difficulty of attributing damage to specific emitters.

---

## LLM Exercise — Chapter 12: Environmental Protection and Negative Externalities (Policy Brief Project)

**Project:** Policy Brief.
**What you're building this chapter:** the negative-externality analysis — does your policy address (or create) negative externalities, and which intervention type fits?
**Tool:** **Claude Project** "Policy Brief" — appends a section.

---

**The Prompt:**

```
Chapter 12 of my Policy Brief project. Prior sections in this Claude
Project. Chapter 12 taught: a negative externality is a cost imposed
on a third party not in the transaction (pollution is the canonical
example, but congestion, secondhand smoke, antibiotic resistance
also qualify); four intervention types — command-and-control
regulation (set the limit, enforce it), Pigouvian taxes (price the
externality directly), cap-and-trade (set the quantity, let market
allocate), property rights (Coase theorem — assign rights, let
parties bargain); the international-externalities problem (no
global enforcement mechanism).

Write the brief's "Negative-Externality Analysis" section in
300–500 words.

1. **The externality identification.** Does your policy address a
   negative externality? If yes, name it specifically: what's the
   external cost, who bears it, what's the magnitude (if estimable)?
   If no, does the POLICY ITSELF create a negative externality
   (regulatory compliance costs imposed on small firms by a
   regulation designed for large ones; environmental harms of
   building the policy's infrastructure; etc.)?

2. **The intervention type.** Which of the four interventions does
   your policy use, and why? For each alternative the policy
   doesn't use, name one reason the chosen approach is preferred
   (or one reason the alternative would have been better).

3. **The Coasian critique.** Coase's theorem says that, in the
   absence of transaction costs, the assignment of property rights
   doesn't matter for efficiency — the parties bargain to the
   efficient outcome. The real-world relevance is that transaction
   costs are huge for many externalities (pollution affects
   millions; you can't bargain). Where do transaction costs make
   the Coasian solution infeasible for YOUR policy?

End with one sentence on the policy's expected efficiency relative
to a hypothetical first-best (a perfectly priced externality at
the marginal social cost). Most policies are second-best at
best; the brief should name the gap and what creates it.
```

---

**What this produces:** A 300–500 word section on the externality structure and the chosen intervention. The "second-best gap" framing is a useful discipline.

**How to adapt this prompt:**

- *For your own project:* Carbon-tax students: this is a central chapter. Sugar-tax students: the externality is healthcare-system costs and (more contested) the consumer's own future health. Antitrust students: the externality is the deadweight loss of market power on third parties (consumers and competitors).
- *For ChatGPT / Gemini:* Works as written.
- *For Claude Code:* If you want a Pigouvian-tax diagram showing the externality wedge, Claude Code can produce it.
- *For a Claude Project:* Append.

**Connection to previous chapters:** Ch 5's elasticity analysis determines who actually pays the Pigouvian tax. Ch 11's capture analysis determines whether the regulator will hold the line.

**Preview of next chapter:** Chapter 13 covers the mirror case — positive externalities and public goods. If your policy supports R&D, education, public health, or anything else with spillover benefits, this chapter is central.

---

## AI Wayback Machine

**Arthur Pigou** developed the framework for "Pigouvian taxes" on negative externalities in 1920.

![Arthur Pigou](../images/arthur-pigou-2z4.png)

*Puppet Art by [Nik Bear Brown](https://www.nikbearbrown.com/).*

**Run this:**

```
Who is Arthur Pigou, and how does their work connect to negative
externalities we covered in this chapter? Keep it to three
paragraphs. End with the single most surprising thing about
their career or ideas.
```

→ Search **"Arthur Pigou"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to apply Arthur Pigou's framework to a current economic question.
- Add a constraint: "Answer including criticisms or limits of Arthur Pigou's framework."

What changes? What gets better? What gets worse?

---

*Byline: Nik Bear Brown.*
