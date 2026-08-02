# Chapter 5 — Elasticity

*How sharply the world responds when you push the price.*

---

In July 2011, Netflix sent an email to its U.S. customers announcing a price change. The combined DVD-and-streaming plan, which had been $9.99 a month, was being split into two separate plans at $7.99 each. The combined service, in effect, jumped sixty percent overnight — from $9.99 to $15.98.

The internet was furious. Petitions. Cancellation videos. Snarky tweets. Reed Hastings, the CEO, wrote a public apology that has been studied in business-school case classes ever since.

Then a strange thing happened. Most of the customers who said they would cancel didn't.

By the end of 2011, Netflix had lost about 800,000 subscribers — significant, but a small fraction of its more-than-25-million subscriber base. By 2013, subscriptions were higher than before the hike. The company's stock, which cratered in 2011, recovered and climbed for a decade.

Here is the puzzle: Chapter 3 told you that when price rises, quantity demanded falls. That happened — 800,000 people left. But the model doesn't tell you how *much* it falls. And whether you lose money on a price increase depends entirely on that how-much. Netflix raised prices sixty percent and came out ahead. That requires an explanation the demand-and-supply diagram alone cannot supply.

The explanation is **elasticity** — a single number that measures how responsive quantity is to a change in price. It is the refinement that turns "less" into "how much less." Once you have it, you can predict before opening the news whether a price hike will raise or sink a company's revenue. You can determine who actually pays a tax — not who is legally obligated to pay it, but who ends up poorer. You can read the Netflix story and know, without knowing the outcome, what the outcome had to be.

---

## What elasticity measures

Start with the definition.

The **price elasticity of demand** is the ratio of two percentages:

$$\text{Price elasticity of demand} = \frac{\% \text{ change in quantity demanded}}{\% \text{ change in price}}$$

Suppose the price of gasoline rises 10 percent and quantity demanded falls 4 percent. Elasticity: 4 ÷ 10 = 0.4. Suppose the price of restaurant meals rises 10 percent and quantity demanded falls 15 percent. Elasticity: 15 ÷ 10 = 1.5.

The number itself tells you which category you're in.

If elasticity is **greater than 1** — *elastic* demand. Quantity responds proportionally more than price. A 10 percent hike loses more than 10 percent of the customers. Restaurant meals at 1.5 are elastic.

If elasticity is **less than 1** — *inelastic* demand. Quantity responds proportionally less than price. A 10 percent hike loses less than 10 percent of the customers. Gasoline at 0.4 is inelastic.

If elasticity is **exactly 1** — *unitary elastic*. The percentage changes are equal. Revenue stays flat when price changes.

(Technical note: because price and quantity move in opposite directions, the elasticity is mathematically negative. By convention we report the absolute value. Don't let the sign trip you up.)

<!-- → [TABLE: Elasticity classification reference — columns: Elasticity value | Category | What it means | Revenue effect of a price increase; rows: >1 / Elastic / Quantity drops proportionally more than price / Revenue falls; =1 / Unitary elastic / Quantity drops by the same percent as price / Revenue unchanged; <1 / Inelastic / Quantity drops proportionally less than price / Revenue rises; special row: 0 / Perfectly inelastic / Quantity doesn't change at all / N/A; special row: ∞ / Perfectly elastic / Any price increase drives quantity to zero / N/A; caption: "Keep this table next to every elasticity problem — the revenue column is the one students most often get backwards"] -->

Two theoretical extremes sit at the boundaries. A **perfectly elastic** demand curve is horizontal — any price increase, even a penny, drives quantity to zero. This happens when buyers have perfect substitutes and will immediately defect if you charge more. A **perfectly inelastic** demand curve is vertical — quantity doesn't move at all regardless of price. This happens with absolute necessities and no alternatives. Neither extreme is common in pure form; they're limiting cases that anchor the intuition.

The same machinery applies to supply. **Price elasticity of supply**: percent change in quantity supplied divided by percent change in price. Pizza supply is highly elastic — when prices rise, a pizza shop can crank out more pies by the hour. Beachfront real estate supply is highly inelastic — there is only so much beachfront regardless of what buyers will pay.

<!-- → [DIAGRAM: Three demand curves on the same axes — steep nearly-vertical curve labeled "Inelastic (e.g. insulin)"; diagonal curve labeled "Unitary elastic"; shallow nearly-horizontal curve labeled "Elastic (e.g. one café's coffee)"; all passing through the same equilibrium point; caption: "Same equilibrium price — three very different responses to a price change. The slope of the curve is the visual signature of elasticity."] -->

---

## Why elasticities differ

Three factors drive how responsive demand is. Each is doing independent work, and they multiply.

**Substitutes.** The more substitutes exist, the more elastic. Coffee at one café has many substitutes — the café next door, the one across the street, the office machine down the hall. Demand at any single café is elastic. Insulin has almost no substitutes for a diabetic patient. Demand is inelastic. A strong brand creates artificial inelasticity by convincing buyers that no substitute is acceptable. That inelasticity is the asset the brand is actually selling.

**Share of budget.** The larger the fraction of your income a good consumes, the more carefully you watch its price and the harder you work to find alternatives when it rises. A 10 percent rise in the price of table salt is invisible to a household budget. A 10 percent rise in mortgage rates reorganizes it. Budget share and elasticity move together.

**Time horizon.** This is the most important of the three and the most often forgotten. When gas prices spike, you cannot stop driving to work tomorrow. Over six months, you can carpool. Over two years, you can buy a more efficient car. Over five years, you can move closer to work. **Demand is more elastic in the long run than in the short run.** The same logic applies to supply. A pizza shop can make more pizzas this evening; an oil company cannot drill a new well until next year. **Supply, too, is more elastic in the long run than in the short.**

This asymmetry between short-run and long-run elasticity is one of the most important facts in applied economics, and it explains why so many economic forecasts made at the moment of a price shock look wrong a decade later. We will come back to this.

<!-- → [TABLE: Three determinants of demand elasticity — columns: Factor | More elastic when... | More inelastic when... | Example of each direction; rows: Substitutes available / many substitutes exist / few or no substitutes / coffee at one café (elastic) vs. insulin (inelastic); Share of budget / good takes large share of income / good takes tiny share / mortgage rates (elastic) vs. table salt (inelastic); Time horizon / buyers have had time to adjust / change is immediate/short-run / gas prices long-run (elastic) vs. gas prices next week (inelastic); caption: "Elasticity is not fixed — it shifts when any of these three factors change"] -->

---

## Elasticity and revenue

Now the Netflix story becomes a calculation.

Total revenue is price times quantity: $P \times Q$. When you raise price, two things happen simultaneously: each unit sold earns more (revenue tends up), but fewer units are sold (revenue tends down). Which effect wins depends entirely on elasticity.

If demand is **inelastic** (elasticity < 1): the quantity drop is proportionally smaller than the price increase. The "more per unit" effect beats the "fewer units" effect. Revenue rises when you raise price.

If demand is **elastic** (elasticity > 1): the quantity drop is proportionally larger than the price increase. The "fewer units" effect beats the "more per unit" effect. Revenue falls when you raise price.

If demand is **unitary** (elasticity = 1): the two effects exactly cancel. Revenue is unchanged.

<!-- → [TABLE: Elasticity and total revenue — columns: Demand type | Elasticity | Price increase → revenue | Price decrease → revenue; rows: Elastic / >1 / Falls / Rises; Unitary / =1 / Unchanged / Unchanged; Inelastic / <1 / Rises / Falls; caption: "The revenue rule is the most practically useful result in this chapter — every pricing decision a firm makes is an implicit bet about which row it's in"] -->

Netflix in 2011 was inelastic. There were no good substitutes for streaming yet. Hulu was tiny. Disney+ didn't exist. Amazon Prime Video was a rudimentary library attached to a shipping service. HBO was still a cable-only product. The subscribers who left were the price-sensitive fringe; the ones who stayed were the committed core. The sixty percent price hike produced a substantial revenue gain even after accounting for the 800,000 departures.

Then something changed. Between 2018 and 2021, Disney+, Apple TV+, HBO Max, Peacock, Paramount+, and a half-dozen smaller services launched and scaled rapidly. Netflix's market went from near-monopoly to competitive. Substitutes appeared. Elasticity rose. By the early 2020s, Netflix was substantially more constrained in its pricing power — a fact visible in its subscriber growth numbers when it attempted further price increases. Same company, same product, different elasticity, different outcome.

The lesson is worth saying plainly: **elasticity is not a fixed property of a good. It is a property of the market situation the good is in — specifically, how many substitutes exist and how much time buyers have had to adjust.** Both of those change. A business that confuses past inelasticity for permanent inelasticity will eventually make the Netflix-2022 mistake instead of the Netflix-2011 gain.

---

## Tax incidence — who actually pays

Here is the most counterintuitive application of elasticity, and one of the most policy-relevant.

When a government taxes a good, the *legal* obligation to pay falls on either the buyer or the seller — whoever the law designates. The *economic* burden — who actually ends up poorer — is a different question, and it is determined by the relative elasticities of demand and supply, not by what the law says.

Suppose the government imposes a $1-per-pack tax on cigarettes, levied on the seller. The seller, in principle, owes that dollar to the government. But the seller raises the price to recoup some of it, and the buyer pays the higher price. How much of the dollar comes out of the seller's pocket and how much out of the buyer's depends on one thing: who can move along their curve more easily.

If demand is more inelastic than supply — cigarettes are the classic case, where addicted buyers have few substitutes and many sellers compete — buyers cannot easily walk away. The seller raises the price by close to the full dollar. Buyers absorb most of the tax, regardless of who writes the check.

If supply is more inelastic than demand — think beachfront real estate, where there is a fixed amount of beachfront and buyers can always look inland — sellers cannot reduce production. The price barely rises after the tax. Sellers absorb most of the burden in lower net receipts.

The rule: **the tax burden falls more heavily on whichever side of the market is less elastic.** Elasticity is a measure of how easily you can escape. The side that cannot escape pays.

<!-- → [DIAGRAM: Two-panel tax incidence comparison — left panel: inelastic demand (steep D), elastic supply (shallow S); tax wedge inserted; consumer price rises nearly the full tax amount, producer price barely moves; label "Buyers bear most of the tax"; right panel: elastic demand (shallow D), inelastic supply (steep S); tax wedge inserted; consumer price barely rises, producer price drops nearly the full tax amount; label "Sellers bear most of the tax"; caption: "The legal obligation to pay says nothing about who ends up poorer — that's determined entirely by which side can escape more easily"] -->

This principle has a famous application that surprises most people. The U.S. payroll tax for Social Security and Medicare is legally split fifty-fifty between employees and employers — each pays 7.65 percent of the wage. But economists' best estimates are that the burden falls closer to 80 percent on workers. The reason is that labor supply is more inelastic than labor demand. Workers cannot easily exit the labor force when their take-home pay is cut. Employers can substitute capital for labor, automate, hire part-time contractors, offshore. Workers are less mobile than employers; they absorb more of the tax. The legal split is fifty-fifty. The economic incidence is not.

Tax policy that ignores incidence is tax policy that surprises itself. A sugar tax intended to raise revenue from soda companies may in fact be paid mostly by low-income consumers, if demand for soda is inelastic and supply is elastic. A corporate income tax intended to fall on shareholders may shift partly onto workers if capital is more mobile internationally than labor. The law says who writes the check. Elasticity says who is actually poorer.

---

## Income elasticity and cross-price elasticity

Two extensions of the framework are worth naming before the synthesis.

**Income elasticity** measures how quantity demanded responds to a change in income, holding prices constant:

$$\text{Income elasticity} = \frac{\% \text{ change in quantity demanded}}{\% \text{ change in income}}$$

Most goods are *normal* — income rises, demand rises, positive income elasticity. Private jets and country-club memberships have very high positive income elasticities. Some goods are *inferior* — demand falls when income rises, because buyers trade up to something better. Bus tickets and instant ramen often show negative income elasticities. The category tells you something important about how a market will change as a population becomes richer or poorer over time.

**Cross-price elasticity** measures how the quantity demanded of one good responds to a change in the price of a different good:

$$\text{Cross-price elasticity of A with respect to B} = \frac{\% \text{ change in quantity of A demanded}}{\% \text{ change in price of B}}$$

A positive number means the goods are substitutes — when chicken gets expensive, more beef is bought. A negative number means complements — when gasoline gets expensive, fewer SUVs are sold. Tracking cross-price elasticities is how a company identifies which competitors actually compete with its product, regardless of what the marketing department believes. If the cross-price elasticity between your product and a competitor's is near zero, they are not actually substitutes in the eyes of consumers, whatever the category name says.

---

## Synthesis

Pull back. The demand-and-supply model from Chapter 3 told you the *direction* prices and quantities move when something changes. Elasticity tells you the *magnitude*. Direction and magnitude together turn the diagram from a qualitative sketch into a real predictive instrument.

The single most important fact in this chapter, the one that gets reused in every subsequent chapter: **elasticity grows with time.** Short-run inelasticity is not a permanent feature of demand — it is a temporary feature of how slowly people and firms can adjust. Over time, substitutes appear, behaviors shift, capital is reallocated, technologies emerge. The adjustment takes time, but it happens.

The 1973 oil embargo roughly doubled gasoline prices. In the short run, Americans barely changed their driving — short-run elasticity was tiny. But over the following twenty years, fuel-efficient vehicles replaced the gas-guzzlers, freight shifted from trucks to more-efficient diesel rail, suburban development patterns began to account for fuel costs, and per-vehicle gasoline consumption fell substantially. The same price shock that seemed to do almost nothing in the first year reshaped patterns of consumption and production over decades.

<!-- → [CHART: Line chart showing demand elasticity magnitude (y-axis) vs. time after price shock (x-axis, labeled: 1 week / 1 month / 6 months / 2 years / 10 years); single upward-sloping curve starting near zero and rising toward a plateau; annotations at key inflection points naming what adjustments occur (carpooling, fuel-efficient car purchase, job change, suburban redesign); caption: "The same shock. A different elasticity at each time horizon. The curve always rises — the question is how fast."] -->

Now read the Netflix story the same way. In 2011, streaming had one serious player. Inelastic. By 2024, it had ten. Elastic. The same kind of price increase by the same company with the same product produced different outcomes because the market structure changed. Time added substitutes. Substitutes raised elasticity. Higher elasticity changed the revenue math.

This is why every elasticity estimate needs a time horizon attached to it. "Inelastic" without a time horizon is incomplete. "Inelastic in the short run" is a specific, useful claim. "Inelastic in the long run" is a strong claim that needs justification — either the substitutes won't appear, or the time needed for adjustment is so long that it doesn't matter for the policy question at hand.

The chapter is one number, applied carefully, with the time horizon kept honest.

---

## Exercises

**Warm-up**

*1. Calculate and classify.* The price of a concert ticket rises from $80 to $100 (a 25 percent increase). Ticket sales fall from 4,000 to 3,400 (a 15 percent decrease). Calculate the price elasticity of demand using the percentage formula. Is demand elastic, inelastic, or unitary? Based only on this number, did the venue's total revenue rise or fall? Show your arithmetic. *(Tests: computing elasticity; applying the revenue rule.)*

*2. Slope and shape.* Draw two demand curves on the same axes passing through the same point — one steep, one shallow. Label which is more elastic and which is more inelastic. Then answer: if a $5 price increase is applied to both, which curve loses more quantity? Use the diagram to explain why, in one sentence, without using the word "slope." *(Tests: visual interpretation of elasticity; distinction between steep/shallow and elastic/inelastic.)*

*3. Classify three goods.* For each of the following, predict whether demand is more elastic or more inelastic, and name the dominant reason (substitutes, budget share, or time horizon): (a) emergency-room visits; (b) a specific brand of luxury handbag; (c) gasoline in the week after a price spike; (d) gasoline five years after a price spike. *(Tests: applying the three determinants; noting how time horizon changes the classification for the same good.)*

**Application**

*4. The revenue gamble.* A regional airline is considering raising ticket prices 20 percent on its most popular route. An analyst estimates demand elasticity on that route is 0.6. A second analyst says the route's elasticity is 1.4. (a) For each estimate, predict whether revenue rises or falls and by approximately how much. (b) Which analyst's estimate makes the price increase a good idea? (c) What information about the route would help you decide which analyst is right? *(Tests: applying the revenue rule with numerical elasticities; reasoning about what determines elasticity in a specific market.)*

*5. Who bears the gas tax?* The federal gasoline tax in the U.S. is levied on refiners (sellers). Short-run demand elasticity for gasoline is approximately 0.2; short-run supply elasticity is approximately 0.4. Use the incidence rule to estimate what fraction of the tax is borne by consumers versus producers in the short run. Then repeat the analysis assuming long-run elasticities of 0.7 (demand) and 1.2 (supply). How does the incidence shift? *(Tests: applying the incidence rule numerically; connecting short-run vs. long-run elasticity to policy consequences.)*

*6. Netflix 2022.* By 2022, Netflix faced meaningful competition from Disney+, HBO Max, Apple TV+, and Peacock. In January 2022, Netflix raised prices and lost 200,000 subscribers in Q1 — its first subscriber loss in a decade. Apply the elasticity framework: (a) What changed about Netflix's market structure between 2011 and 2022 that changed the relevant elasticity? (b) Was Netflix's demand elastic or inelastic in 2022 by the time losses appeared? (c) What does this imply about what Netflix's revenue did in Q1 2022? Check whether your prediction matches the reported outcome. *(Tests: elasticity as a market property not a product property; connecting substitutes and time to observable outcomes.)*

**Synthesis**

*7. The sugar tax paradox.* Several U.S. cities have levied taxes on sweetened beverages, legally imposed on distributors, with two stated goals: (a) raise revenue, and (b) reduce consumption of sugary drinks. Using the elasticity framework, explain under what conditions these two goals are in tension with each other. Specifically: what elasticity makes the tax good at raising revenue but bad at reducing consumption? What does the empirical evidence on soda demand elasticity suggest about which goal is actually being achieved? *(Tests: applying elasticity to policy goals that point in opposite directions; distinguishing revenue and behavior-change objectives.)*

*8. Payroll tax incidence.* The U.S. Social Security payroll tax is legally split 50-50 between workers and employers. Economists estimate that labor supply elasticity is approximately 0.1–0.2 and labor demand elasticity is approximately 0.3–0.5. (a) Using these ranges, estimate the fraction of the tax borne by workers. (b) Is the actual incidence closer to the legal split (50-50) or more tilted toward workers? (c) What would have to be true about labor markets for the legal split to actually equal the economic incidence? *(Tests: numerical incidence calculation; connecting labor market structure to policy claims about who a tax "hits.")*

**Challenge**

*9. When elasticity changes the moral argument.* The chapter notes that goods with inelastic demand are often necessities — gasoline, insulin, water — and that taxing them is effective for revenue but regressive. A policymaker argues: "We should tax luxury goods instead — their demand is elastic, so wealthier consumers will pay." Evaluate this argument using the elasticity framework: (a) If luxury demand is elastic, what happens to revenue from a luxury tax? (b) Who actually bears the burden of a tax on a good with elastic demand and inelastic supply? (c) Does the elasticity analysis support or complicate the policymaker's equity argument? *(Tests: applying the revenue rule and incidence rule together; evaluating a policy claim that conflates legal incidence with economic incidence.)*

*10. The long run arrives.* The chapter's synthesis claims that "elasticity grows with time" — that short-run inelasticity is temporary. Identify one market where this claim is empirically questionable: a market where demand or supply has remained inelastic over a long period, despite the passage of time and the apparent opportunity for substitutes to emerge. Explain why the standard adjustment mechanism hasn't worked in that market. What feature of the market (search costs, regulation, network effects, physical constraints) is blocking the elasticity from growing? *(Tests: critical evaluation of the chapter's central empirical claim; applying the framework to its own limits.)*

---

## LLM Exercises

**Exercise 1 — Calculate elasticity from data.** Find a real-world price change — a recent gas price spike, a Disneyland ticket increase, a Spotify hike — and the reported change in subscribers, demand, or sales. Give the numbers to an LLM and ask it to compute the price elasticity of demand. Then ask the LLM to interpret the number: elastic or inelastic? And to predict whether the company's revenue rose or fell. Verify the math by hand.

**Exercise 2 — Stress test the textbook examples.** Ask an LLM for a list of "five goods with elastic demand and five goods with inelastic demand." Then for each one, ask: under what conditions might that classification flip? Hint: more substitutes appearing, longer time horizon, higher share of budget. The exercise tests whether the LLM treats elasticity as a fixed property of a good (wrong) or a property of a market situation (right).

**Exercise 3 — Tax incidence in plain language.** Tell an LLM: "The government wants to raise $5 billion. They are choosing between a tax on gasoline (demand inelastic, supply moderately elastic) and a tax on luxury yachts (demand elastic, supply inelastic). For each tax, who actually pays the burden — buyers or sellers — and why?" Evaluate whether the LLM uses elasticity to reason, or relies on political talking points.

**Exercise 4 — Time horizon.** Ask an LLM: "If gasoline prices doubled tomorrow and stayed doubled for ten years, what would happen to driving in the U.S. over (a) the next month, (b) the next year, (c) the next decade?" Press the LLM to be specific about *how* short-run inelasticity gives way to long-run elasticity — what behaviors and decisions change at each time horizon. The exercise teaches that elasticity is not a single number; it depends on how much time you give the system.

**Exercise 5 — Build a pricing argument.** Tell an LLM you run a small streaming service and are considering a price increase. Ask it to estimate, in plain English, what factors determine whether the increase will raise or lower total revenue. A good answer names elasticity explicitly, asks about the availability of substitutes, and asks about switching costs. Push the LLM if it dodges the elasticity reasoning.

---

## LLM Exercise — Chapter 5: Elasticity (Policy Brief Project)

**Project:** Policy Brief.  
**What you're building this chapter:** the elasticity analysis of your policy — magnitudes, not just directions, and the incidence (who actually bears the cost) that elasticity determines.  
**Tool:** **Claude Project** "Policy Brief" — appends a section.

---

**The Prompt:**

```
Chapter 5 of my Policy Brief project. Prior sections in this Claude
Project. Chapter 5 taught: elasticity as the responsiveness of
quantity to price, expressed as a unitless ratio (% change in Q /
% change in P); the rule of thumb (>1 = elastic, <1 = inelastic);
why elasticities differ across goods (substitutes available,
share of budget, time horizon); the link from elasticity to total
revenue (raise price on inelastic goods, lower price on elastic);
the incidence rule — when supply is more inelastic than demand,
suppliers bear more of any tax/regulation, and vice versa.

Write the brief's "Elasticity and Incidence" section in 400–600
words.

1. **The relevant elasticities.** For your policy's primary
   market, what are the demand and supply elasticities? Cite
   published estimates if you can find them ([verify] anything you
   cite); otherwise, reason from first principles using the
   substitutes/budget-share/time arguments. Estimate ranges, not
   point values. Be honest about how thin the evidence is.

2. **Incidence — who actually pays.** A nominal tax on producers
   doesn't necessarily fall on producers; a nominal benefit to
   workers doesn't necessarily land with workers. Use the
   elasticity ratio to estimate the actual incidence of your
   policy. Show the math (it's just a ratio).

3. **The short-run vs. long-run shift.** Elasticities are larger
   in the long run than the short run — substitutes get developed,
   behaviors adapt. Estimate how the incidence changes between
   year 1 and year 5 of your policy.

4. **The elasticity-driven failure mode.** Many policies fail
   because their advocates assumed elasticities they don't have.
   Cigarette taxes assume inelastic demand (mostly true in the
   short run, less so over decades). Soda taxes assume the same
   (smaller effect than expected, because substitutes exist).
   Name the elasticity assumption your policy is making, and the
   failure mode if that assumption is wrong.

End with one sentence: based on the incidence analysis, your
policy's nominal target (the regulated party) and the actual
party who pays (or benefits) are [the same / different]. If
different, this is the most important finding of the chapter.
```

---

**What this produces:** A 400–600 word section with elasticity estimates, incidence analysis, and a short-run-vs-long-run comparison. The "nominal vs. actual party" finding is often the most counterintuitive piece of the brief.

**How to adapt this prompt:**

- *For your own project:* Carbon tax: demand for fossil fuels is inelastic short-run, more elastic long-run as substitutes scale. Minimum wage: low-wage labor demand elasticity is the central empirical question. Antitrust: cross-price elasticity with substitute platforms.
- *For ChatGPT / Gemini:* Works as written.
- *For Claude Code:* If you want a tax-incidence diagram with elastic vs. inelastic comparison, Claude Code can produce it.
- *For a Claude Project:* Append.

**Connection to previous chapters:** Ch 3 identified what shifts; Ch 4 traced spillovers; Ch 5 quantifies how much shift, and identifies who actually pays.

**Preview of next chapter:** Chapter 6 turns to the consumer's side — how individuals decide what to buy under your policy, and where the textbook utility-maximization model breaks (behavioral economics). The behavioral-econ piece often matters most for policies that depend on changing individual behavior.

---

## AI Wayback Machine

**Antoine Augustin Cournot** was the French mathematician and economist whose *Researches into the Mathematical Principles of the Theory of Wealth* (1838) was among the first works to use calculus to analyze economic behavior — decades before Marshall made the diagram familiar.

![Antoine Augustin Cournot](../images/antoine-augustin-cournot-fa4.png)

*Puppet Art by [Nik Bear Brown](https://www.nikbearbrown.com/).*

**Run this:**

```
Who is Antoine Augustin Cournot, and how does their work connect to
elasticity we covered in this chapter? Keep it to three paragraphs.
End with the single most surprising thing about their career or ideas.
```

→ Search **"Antoine Augustin Cournot"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to apply Antoine Augustin Cournot's framework to a current economic question.
- Add a constraint: "Answer including criticisms or limits of Antoine Augustin Cournot's framework."

What changes? What gets better? What gets worse?

---

*Byline: Nik Bear Brown.*
