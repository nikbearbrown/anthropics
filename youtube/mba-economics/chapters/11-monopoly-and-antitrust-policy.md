# Chapter 11 — Monopoly and Antitrust Policy

*The legal apparatus that tries to keep markets from collapsing into one seller — and why it sometimes fails in both directions.*

---

In 1911, the U.S. Supreme Court ordered the breakup of Standard Oil, which by then controlled roughly 90 percent of American oil refining. The company was split into 34 separate firms — including the predecessors of what would become Exxon, Mobil, Chevron, and Amoco. The decision was the largest application yet of a law passed twenty years earlier, and it set the precedent for federal action against firms that had grown "too large." What "too large" actually means has been the subject of continuous legal and economic argument ever since.

In 1982, after a process that took thirty years, the Department of Justice broke up AT&T — the company that had operated essentially every telephone in the United States for most of the twentieth century. The breakup created seven regional companies and freed long-distance service to competitors. Within fifteen years the price of a long-distance call had fallen by more than 90 percent.

In 2024, the Department of Justice and several state attorneys general were prosecuting Google for monopolizing internet search and online advertising. Google argued its dominance reflected a better product. The government argued that contracts paying device manufacturers to set Google as the default search engine — among other practices — had insulated Google from competition it would otherwise face. Whatever the verdict, the structural question is the same one Standard Oil's lawyers faced: when does market dominance cross from "earned by being good" to "maintained by tactics that block competitors"?

This chapter is about the legal apparatus built to answer that question. Chapter 9 told us what monopoly costs society. Chapter 10 told us how a few firms can produce monopoly-like outcomes without any single firm controlling the whole market. This chapter is about the institutional response — the laws, the agencies, the regulatory frameworks that exist to prevent or correct excessive market power. By the end you should be able to read a major antitrust case in the news and locate it in the framework: what kind of market power is alleged, what remedy is sought, and what the costs and benefits of intervention look like.

---

## The legal toolkit

Three statutes form the core of American antitrust law.

**The Sherman Antitrust Act (1890).** The founding document. Section 1 prohibits every contract, combination, or conspiracy in restraint of trade. Section 2 prohibits monopolization or attempted monopolization. The language is broad and deliberately so — Congress wanted flexibility to reach conduct it couldn't anticipate. Most of the heavy enforcement work over the following century has used or extended this statute.

**The Clayton Act (1914).** A corrective lens on the Sherman Act, targeting specific practices the earlier statute handled awkwardly: price discrimination that harms competition, exclusive-dealing contracts that lock customers to a single supplier, and — most importantly for modern practice — mergers that "may substantially lessen competition." This is the statute that controls modern merger review.

**The Federal Trade Commission Act (1914).** Created the FTC and prohibited "unfair methods of competition" — a deliberately elastic standard that lets enforcement evolve as new business practices appear. The FTC can reach conduct that doesn't clearly violate the Sherman or Clayton Acts but still harms competition.

Two agencies enforce these laws: the **FTC** and the **Antitrust Division of the DOJ**. They split jurisdiction informally and coordinate to avoid overlap. Their tools are three: block mergers before they happen, challenge anticompetitive practices after the fact, and (rarely) seek structural remedies against firms that have already monopolized a market.

<!-- → [TABLE: The antitrust legal toolkit — columns: Statute | Year | Core prohibition | Primary modern use; rows: Sherman Act / 1890 / Contracts in restraint of trade (§1); monopolization (§2) / Monopolization cases, cartel prosecution; Clayton Act / 1914 / Price discrimination; exclusive dealing; mergers that may substantially lessen competition / Merger review; FTC Act / 1914 / Unfair methods of competition / Evolving conduct cases; enforcement agency for each; caption: "Three statutes, two agencies, one purpose: keep markets from settling into one seller"] -->

---

## Measuring concentration

Before regulators can decide whether a market is too concentrated, they need a way to measure it. Two metrics dominate.

**Four-firm concentration ratio (CR4).** The combined market share of the four largest firms. A market where the top four firms together hold 80 percent of sales is very different from one where they hold 30 percent. CR4 is easy to compute and easy to explain to a court. It's also crude — it treats the fourth and fifth firms the same, and it ignores the distribution of shares among the top four.

**Herfindahl-Hirschman Index (HHI).** Sum of the squared market shares of all firms. If one firm holds 100 percent, HHI = 100² = 10,000 — the theoretical maximum. If ten firms each hold 10 percent, HHI = 10 × 10² = 1,000. The squaring is the key: it gives proportionally more weight to large firms than to small ones. A market with one firm at 50 percent and ten firms at 5 percent each has HHI = 2,500 + 250 = 2,750 — substantially higher than ten equal firms, reflecting the dominance of that single 50-percent player.

Current DOJ guidelines: HHI below 1,500 is unconcentrated; 1,500–2,500 is moderately concentrated; above 2,500 is highly concentrated. A merger that would push HHI above the moderate threshold *and* increase HHI by more than 200 points typically triggers detailed review.

These numbers are tools, not verdicts. A market with HHI of 4,000 in a small town might still be competitive if entry is easy and the dominant firm can't raise prices without inviting new entrants. A market with HHI of 1,800 might be effectively monopolized if entry barriers are high. The agencies look at the numbers, then look at the underlying structure.

<!-- → [TABLE: HHI worked example — columns: Market structure | Firm shares | HHI calculation | HHI result | DOJ classification; rows: Pure monopoly / 100% / 100² / 10,000 / Highly concentrated; Tight duopoly / 60%, 40% / 3,600 + 1,600 / 5,200 / Highly concentrated; Four equal firms / 25% each / 4 × 625 / 2,500 / Highly concentrated (borderline); Ten equal firms / 10% each / 10 × 100 / 1,000 / Unconcentrated; One dominant + ten small / 50%, ten at 5% / 2,500 + 250 / 2,750 / Highly concentrated; caption: "The squaring punishes concentration at the top — a firm at 50% contributes 2,500 to HHI; ten firms at 5% together contribute only 250"] -->

---

## Three categories of enforcement

### Mergers

Most antitrust action involves mergers. The standard process: large companies planning to combine notify the FTC and DOJ. The agencies review whether the combined firm would substantially reduce competition. Most mergers go through unchallenged. Some are approved with conditions — the merging firms must divest specific assets to preserve competition in particular markets. Some are blocked, though "blocked" usually means the agencies signal they will sue and the firms abandon the deal rather than fight in court.

Famous blocks: AT&T's proposed acquisition of T-Mobile in 2011, which would have reduced major U.S. carriers from four to three. Staples' proposed merger with Office Depot in 2015, which would have created a near-duopoly in office supplies. Penguin Random House's proposed acquisition of Simon & Schuster in 2022, blocked on grounds it would harm competition for author advances — a somewhat unusual theory that focused on the market for purchasing manuscripts rather than the market for selling books.

The merger review framework is, on the whole, the most developed part of antitrust practice. The agencies have decades of experience. The error margin — letting harmful mergers through, blocking benign ones — is real but relatively narrow.

### Restrictive practices

These are tactics that distort competition without changing who owns whom.

**Price-fixing.** Two or more firms agree to charge a common price. Per se illegal — the agreement itself is the violation, no need to prove competitive harm. The economists' analysis of why is in Chapter 10: any agreement above marginal cost transfers surplus from consumers to producers and creates deadweight loss.

**Bid-rigging.** Two or more firms competing for a contract agree in advance which firm will "win" and at what price. The market appears competitive; the outcome isn't. Common in industries with repeat procurement — construction, defense, raw materials.

**Tying and bundling.** Selling product A only to customers who also buy product B. Can be efficient (a tightly integrated system performs better) or anticompetitive (leveraging monopoly power in one market to dominate another). The Microsoft case in the 1990s — must take Internet Explorer to get Windows — was the famous example. Courts look at both the efficiency justification and the exclusionary effect.

**Predatory pricing.** Discussed in Chapter 9: pricing below cost to drive out competitors, then raising prices once the market is cleared. Hard to prove because courts must distinguish between aggressive but lawful competition and below-cost pricing designed to monopolize.

**Exclusive dealing.** Contracts requiring retailers to carry only the manufacturer's products, or prohibiting them from dealing with competitors. Sometimes legal (creates adequate incentives for retailers to invest in the product), sometimes not (forecloses substantial competition). The rule of reason — do the effects, on balance, harm or help competition? — governs most restrictive-practice cases. The analysis is rarely clean.

<!-- → [TABLE: Restrictive practices — columns: Practice | Legal standard | How courts evaluate | Signature case; rows: Price-fixing / Per se illegal — no balancing test / Agreement itself is the violation / Lysine cartel (ADM, 1996); Bid-rigging / Per se illegal / Agreement itself is the violation / School milk bid-rigging (multiple states); Tying / Rule of reason / Efficiency justification vs. exclusionary effect / Microsoft / IE (1990s); Predatory pricing / Rule of reason / Below-cost pricing + recoupment intent / Hard to win — Brooke Group (1993); Exclusive dealing / Rule of reason / Market foreclosure extent vs. efficiency / Must be substantial foreclosure to be illegal; caption: "Per se = automatic violation; rule of reason = courts weigh benefits against harms. Knowing which standard applies tells you how hard the case is to win"] -->

### Monopolization

The hardest enforcement category. A firm has dominant market share. Did it get there by being good — building a better product, driving down costs, serving customers well? That's legal. Did it get there by tactics that exclude competitors — buying up potential rivals, entering into exclusivity agreements that foreclosed distribution, pricing below cost with predatory intent? That may be illegal.

Standard Oil (1911), AT&T (1982), Microsoft (the 2000s behavioral remedy), Google (ongoing) — all of these are or were monopolization cases. The remedies range from behavioral (the firm must change specific practices) to structural (the firm must be split).

Structural breakups are dramatic and rare. Behavioral remedies are common and often weak. The firm being constrained has every incentive to find new conduct that achieves the same anticompetitive purpose by different means. Microsoft's behavioral remedy from the early 2000s is widely regarded as having had limited effect on the underlying market structure. AT&T's structural breakup reshaped an entire industry. The trade-off between dramatic-and-durable and flexible-and-circumventable has no clean resolution — it depends on the specific conduct and the specific market.

<!-- → [TABLE: Structural vs. behavioral remedies — columns: Remedy type | What it does | Durability | Weakness | When it works best; rows: Structural (breakup) / Splits firm into independent competitors / High — hard to undo / Blunt, may destroy efficiencies, disrupts markets / When the firm's size itself is the problem (AT&T); Behavioral (conduct order) / Prohibits specific practices / Low — firm finds workarounds / Requires sustained monitoring; firm out-maneuvers the consent decree / When the problem is specific conduct, not size (price-fixing consent decrees); caption: "Structural remedies change the players; behavioral remedies change the rules. Courts choose based on which lever the violation was — size or conduct"] -->

---

## Natural monopoly regulation

We met natural monopoly in Chapter 9: cost structure where one firm can serve the entire market at lower average cost than two firms could. Splitting a natural monopoly raises average cost. Leaving it unregulated produces monopoly pricing. The standard resolution is regulation.

Two main regulatory frameworks, each with a characteristic pathology.

**Cost-plus regulation.** The regulator sets price at the firm's costs plus a fair rate of return on capital. The firm recovers its costs and earns a regulated return. The problem is immediately visible: the firm now has every incentive to *inflate* its costs, because higher costs allow higher regulated prices. Invest in unnecessary capacity. Gold-plate the headquarters. Hire excess staff. Over-insure. The U.S. utility sector through most of the twentieth century was the textbook case — regulated utilities chronically over-invested in infrastructure and operated well above the cost frontier.

The phenomenon has a name: the **Averch-Johnson effect**, after the economists who formalized it in 1962. When the allowed rate of return exceeds the cost of capital — which it typically does, because regulators err toward ensuring financial viability — firms over-invest in capital. The incentives are backward from what efficiency requires.

**Price-cap regulation.** The regulator sets a price ceiling and leaves the firm to manage costs. Any efficiency gains go to the firm as profit. The incentive is now sharply toward cost reduction: cut costs, keep the savings. The United Kingdom moved to price-cap regulation for most privatized utilities in the 1980s and 1990s. Results were mixed — where the caps were set reasonably, costs fell; where they were set too tightly, firms cut quality rather than cost. Infrastructure investment, which is expensive up front and profitable slowly, tended to be deferred.

Both frameworks rest on the regulator having good information about the firm's true cost structure. The firm has every incentive to prevent this. It controls the data. It employs the engineers who understand the technology. It shapes the framing of every regulatory submission. The information asymmetry is a permanent feature of natural monopoly regulation, not a fixable imperfection.

<!-- → [TABLE: Cost-plus vs. price-cap regulation — columns: Feature | Cost-plus | Price-cap; rows: Price-setting rule / Costs + allowed return / Regulator sets ceiling; firm keeps efficiency gains; Cost-control incentive / Weak — higher costs allowed higher prices / Strong — cuts go to the firm; Investment incentive / Overinvestment (Averch-Johnson effect) / Underinvestment risk if cap is tight; Quality incentive / Moderate — regulator monitors / Quality-cutting risk; Information required / Detailed cost reporting (firm controls) / Benchmark comparison (less firm-controlled); Historical context / U.S. utilities, 20th century / UK privatized utilities, 1980s–90s; caption: "Two regulators, two pathologies: cost-plus breeds gold-plating; price-cap breeds quality deterioration. Both assume information the regulator never fully has"] -->

---

## Regulatory capture

The information asymmetry points toward the deeper problem.

**Regulatory capture** is the tendency of regulators to identify, over time, with the interests of the firms they regulate rather than with the public they nominally serve. The mechanism is straightforward. Regulators spend their careers in one industry. They depend on the industry for technical information. They develop relationships with industry executives. The post-government job market, for a specialist regulator, is largely in the regulated industry. The pressures accumulate in one direction — toward sympathy with the regulated firm.

George Stigler formalized this in 1971 in a famous paper: regulation is not designed to serve the public interest but is "acquired by the industry and is designed and operated primarily for its benefit." This is a strong claim and not universally true. But the empirical record offers substantial support. The original purpose of much U.S. transportation regulation — railroads, trucking, airlines — was to protect incumbent firms from competition, with consumer protection a secondary concern. The deregulation of airlines and trucking starting in the late 1970s was driven in part by recognition that the regulatory structures had been captured and were functioning primarily as cartel-management devices.

The implication is uncomfortable. Some economists prefer market-based solutions — lower entry barriers, structural competition — over direct regulation, precisely because regulated monopolies with captured regulators may perform worse than unregulated industries facing competitive pressure. Whether this is true in any specific case is an empirical question, not one that theory can resolve from first principles.

---

## Synthesis

Pull back. Antitrust policy is the institutional response to the market structures examined in Chapters 9 and 10. Its three enforcement categories: merger review, prohibition of restrictive practices, and structural or behavioral monopolization remedies. Its measurement tools: CR4 and HHI. Its agencies: FTC and DOJ Antitrust Division. Its regulatory frameworks for natural monopoly: cost-plus (gold-plating risk) and price-cap (under-investment and quality-cutting risk), both imperfect because the regulator cannot fully see the firm's cost structure and is vulnerable to capture over time.

Two recurring lessons from the record.

First, *enforcement is itself imperfect in both directions*. Breakups are dramatic but rare. Behavioral remedies are common but often erode. Merger review catches some cases and misses others. Cost-plus regulation produces Averch-Johnson distortions. Price-cap regulation produces quality deterioration. Captured regulators eventually serve the industry. None of these failures is catastrophic, but none disappears with more funding or better-intentioned regulators.

Second, *the alternative to imperfect enforcement is not laissez-faire perfection*. A world without antitrust is a world where the coordination incentives from Chapter 10 go unchecked, where dominant platforms face no constraint on exclusionary conduct, where natural monopolies extract monopoly rent from captive consumers. The choice is not between government intervention and a well-functioning market. It is between two imperfect responses to the same underlying structural problem.

The Standard Oil breakup was a structural success that reshaped American energy. The AT&T breakup was a structural success that required decades of follow-on adjustment. The Microsoft case achieved less than hoped and left behavioral remedies looking weak. Google remains unsettled. Each case is a calibration of the same trade-off: how much enforcement, of what kind, against which dominant firms, seeking which remedy, at what point in a market's development. The model gives you the framework. The case-by-case judgment is what analysts, lawyers, and economists spend careers trying to get right.

---

## Exercises

**Warm-up**

*1. Compute the metrics.* An industry has firms with the following market shares: 35%, 28%, 12%, 8%, 7%, 5%, 3%, 2%. (a) Compute the CR4. (b) Compute the HHI. Show your squaring step. (c) By current DOJ guidelines, is this market unconcentrated, moderately concentrated, or highly concentrated? (d) A merger is proposed between the #1 firm (35%) and the #3 firm (12%). Compute the post-merger HHI and the HHI increase. Does this trigger detailed review? *(Tests: computing both metrics; applying DOJ thresholds; calculating a merger's effect on HHI.)*

*2. Per se or rule of reason?* For each of the following, identify whether it would be treated as per se illegal or evaluated under the rule of reason — and explain why the legal standard differs: (a) Two airlines agree to charge the same price on a specific route; (b) A shoe manufacturer requires retailers to sell only its brands; (c) A software company includes its own browser in the operating system; (d) A construction firm bids above cost on a government contract while colluding with a competitor on who will "win." *(Tests: distinguishing per se from rule-of-reason categories; knowing which standard applies to which practice.)*

*3. Averch-Johnson in plain English.* Explain the Averch-Johnson effect in two sentences without using the word "capital." Use only the logic of incentives and costs. Then explain: why doesn't the Averch-Johnson effect arise under price-cap regulation? *(Tests: conceptual understanding of the incentive distortion; connecting it to the difference between the two regulatory frameworks.)*

**Application**

*4. Evaluate a merger.* In 2011, AT&T proposed to acquire T-Mobile. At the time, the four major U.S. wireless carriers had approximate market shares of: Verizon 33%, AT&T 28%, Sprint 16%, T-Mobile 11%. (a) Compute the pre-merger HHI. (b) Compute the post-merger HHI if AT&T acquires T-Mobile. (c) What is the HHI increase? (d) By DOJ guidelines, does this deal trigger review? (e) Beyond the HHI calculation, what structural argument would the DOJ make against this merger — and what efficiency argument would AT&T make for it? *(Tests: full merger-review calculation; connecting the number to the substantive competitive concern.)*

*5. The Microsoft remedy question.* Microsoft's antitrust case in the early 2000s resulted in a behavioral remedy: Microsoft was required to change specific practices but was not broken up. (a) What practices was Microsoft ordered to change? (b) What structural remedy was the trial court initially ordered and then reversed on appeal? (c) Using the table from the chapter, evaluate: was a behavioral remedy the right choice given the conduct at issue, or would a structural remedy have been more durable? Defend your answer using the framework. *(Tests: applying the structural-vs-behavioral framework to a real case with a known outcome.)*

*6. Cost-plus for a water utility.* A city's water utility operates under cost-plus regulation with an allowed rate of return of 9% on invested capital. The actual cost of capital for the utility is 6%. (a) Using the Averch-Johnson logic, predict how this utility will behave differently than if it were unregulated. (b) Name two observable signs that the Averch-Johnson distortion has set in at this utility. (c) If the city switches to price-cap regulation, what new problems should it anticipate, and how could it design the cap to mitigate them? *(Tests: applying Averch-Johnson to a specific case; connecting the distortion to observable behavior; evaluating price-cap design.)*

**Synthesis**

*7. The capture mechanism, applied.* A state creates a new agency to regulate ride-share companies. Using the Stigler capture framework, describe the likely trajectory of this agency over 15 years: who has concentrated interests in its decisions, who has dispersed interests, what the information asymmetry looks like, and where the post-government job pipeline points. What would the agency's regulatory output look like if capture has fully occurred? What institutional design features could slow or prevent capture? *(Tests: applying the full capture mechanism to a novel regulatory case; connecting institutional design to capture prevention.)*

*8. Compare three antitrust outcomes.* The chapter discusses three monopolization cases with three different outcomes: Standard Oil (structural breakup, reshaped industry), AT&T (structural breakup, long adjustment period), Microsoft (behavioral remedy, limited effect). Using the structural-vs-behavioral framework, explain why the Standard Oil and AT&T breakups were more durable than the Microsoft behavioral remedy. What was different about the nature of Microsoft's monopoly that made a structural remedy harder to design? *(Tests: comparative analysis across three real cases; connecting the type of monopoly to the appropriate remedy.)*

**Challenge**

*9. The consumer-welfare standard debate.* Traditional antitrust doctrine focuses on consumer welfare — primarily prices. Lina Khan's *Amazon's Antitrust Paradox* argues this standard is inadequate for platform companies, which can sustain losses to achieve dominance and then harm competition in ways that don't show up in prices. Pick one specific platform (Amazon, Google, Meta, Apple). (a) Explain why the consumer-welfare standard, applied to current prices, might find no antitrust violation. (b) Explain what harm Khan's framework would identify that the price-focused standard misses. (c) What is the strongest argument *against* Khan's framework — specifically, what would an economist who defends the consumer-welfare standard say about the risks of expanding antitrust doctrine? *(Tests: engaging with an active policy debate; presenting both sides with specific arguments; not collapsing into a one-sided answer.)*

*10. Design the remedy.* Suppose a court rules that Google has illegally monopolized internet search through default-placement contracts. You are advising the court on remedies. (a) Describe a structural remedy: what would Google be split into, and what competition would result? (b) Describe a behavioral remedy: what specific practices would be prohibited? (c) Using the chapter's framework, evaluate which remedy is more likely to durably restore competition — and what the primary risk of your recommended remedy is. Be specific about Google's actual market structure, not just the generic trade-off. *(Tests: applying the remedies framework to a live case with specific market features; connecting the analysis to real structural choices rather than generic theory.)*

---

## LLM Exercises

**Exercise 1 — Compute concentration.** Tell an LLM: "Suppose an industry has firms with market shares 30%, 25%, 15%, 10%, 8%, 5%, 4%, 3%." Ask it to compute the four-firm concentration ratio and the HHI. Verify both by hand. Then ask: by current DOJ thresholds, how should this market be classified? What additional information would you need to evaluate whether intervention is warranted?

**Exercise 2 — Argue both sides of an antitrust case.** Pick a current or recent antitrust case — Google search, Apple App Store, Live Nation/Ticketmaster, your pick. Ask an LLM to argue both sides: that the firm's dominance is the result of a better product (no intervention warranted) and that the firm's dominance is maintained by anticompetitive tactics (intervention warranted). Evaluate which argument is stronger and what the determining evidence would be.

**Exercise 3 — Design a remedy.** Tell an LLM that a hypothetical case has been decided against a dominant firm and the court is choosing a remedy. Ask the LLM to compare a structural remedy (breaking the firm into pieces) and a behavioral remedy (requiring the firm to change specific practices) — strengths and weaknesses of each. A good answer notes that breakups are durable but blunt, and behavioral remedies are flexible but easy to circumvent.

**Exercise 4 — Cost-plus vs. price-cap.** Tell an LLM you are the regulator for a natural-monopoly water utility in a mid-sized city. Ask it to lay out the trade-offs between cost-plus and price-cap regulation for this case. Push: which mode creates stronger incentives for long-term infrastructure investment? Which protects consumers more in the short run? The exercise tests whether the LLM names the gold-plating problem for cost-plus and the under-investment and quality-cutting risk for price-cap.

**Exercise 5 — Spot regulatory capture.** Pick an industry critics often accuse of having captured regulators — banking, defense, pharmaceuticals, energy, agriculture. Ask an LLM to identify three pieces of evidence that *could* indicate capture, and three pieces of evidence that *would* indicate the regulators are still serving the public interest. Then ask: what's the strongest single test you could run to distinguish between the two hypotheses?

---

## LLM Exercise — Chapter 11: Monopoly and Antitrust Policy (Policy Brief Project)

**Project:** Policy Brief.  
**What you're building this chapter:** the antitrust and regulatory-capture analysis — does your policy involve antitrust enforcement, and is it vulnerable to regulatory capture?  
**Tool:** **Claude Project** "Policy Brief" — appends a section.

---

**The Prompt:**

```
Chapter 11 of my Policy Brief project. Prior sections in this Claude
Project. Chapter 11 taught: the legal toolkit (Sherman Act 1890,
Clayton Act 1914, FTC Act 1914); concentration measures (HHI = sum
of squared market shares; four-firm concentration ratio); the three
enforcement categories (collusion, mergers, anticompetitive
conduct); the natural-monopoly regulation dilemma (rate regulation,
average-cost pricing, price-cap regulation); regulatory capture
(when the regulated industry effectively controls its regulator).

Write the brief's "Antitrust and Capture Risk" section in 300–500
words.

1. **The antitrust dimension.** Even if your policy isn't antitrust,
   does it have antitrust effects? A tax that smaller firms can't
   absorb concentrates the industry. A regulation with high fixed
   compliance cost favors incumbents. A subsidy targeted at one
   firm tilts the playing field. Name the antitrust effect (if
   any) of your policy.

2. **The regulatory-capture risk.** Most regulatory policies are
   captured by the industry they regulate over a 10–20 year
   horizon. The mechanism: the industry has concentrated stakes;
   the public has dispersed stakes; the regulator's expertise
   pipeline runs through the industry. Name three specific capture
   risks for your policy and what would have to be true for capture
   NOT to happen.

3. **The natural-monopoly question (if applicable).** If your
   policy regulates a natural monopoly (utilities, last-mile
   broadband, certain health services), name the regulatory
   approach (rate regulation? cost-plus? price cap? cap-and-floor
   range?). If it doesn't, skip this section.

End with one sentence on the institutional design feature that
would most reduce capture risk for your policy. Standard
candidates: sunset clauses, public-interest representation in
rulemaking, transparent rule-revision processes, third-party
auditing. Name the one most appropriate for your specific policy.
```

---

**What this produces:** A 300–500 word section on antitrust dimensions and regulatory-capture risk. The capture-risk analysis is what most policy briefs skip and most informed readers will demand.

**How to adapt this prompt:**

- *For your own project:* Antitrust students: deepen the legal-doctrine analysis here. Carbon-tax students: the capture risk is whether carbon-pricing infrastructure becomes captured by the largest emitters. Healthcare students: the FDA/CMS capture story.
- *For ChatGPT / Gemini:* Works as written.
- *For Claude Code:* Not the primary tool here.
- *For a Claude Project:* Append.

**Connection to previous chapters:** Ch 9's monopoly analysis and Ch 10's strategic-behavior analysis feed Ch 11's regulatory-design questions.

**Preview of next chapter:** Chapter 12 introduces externalities — the most important market-failure concept in policy economics. If your policy addresses or creates an externality, the next two chapters are central. If not, they still set the analytical frame for thinking about which problems markets solve and which they don't.

---

## AI Wayback Machine

**Lina Khan** is an American legal scholar and former FTC Chair whose 2017 Yale Law Journal article *Amazon's Antitrust Paradox* argued that standard antitrust doctrine — focused on consumer prices — was inadequate to evaluate the competitive effects of platform companies that could sustain losses in order to achieve dominance.

**Run this:**

```
Who is Lina Khan, and how does their work connect to antitrust
we covered in this chapter? Keep it to three paragraphs. End with
the single most surprising thing about their career or ideas.
```

→ Search **"Lina Khan"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to apply Lina Khan's framework to a current economic question.
- Add a constraint: "Answer including criticisms or limits of Lina Khan's framework."

What changes? What gets better? What gets worse?

---

*Byline: Nik Bear Brown.*
