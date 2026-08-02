# Chapter 16 — Information, Risk, and Insurance

*The third major source of market failure — when one side knows what the other doesn't.*

In 1970, an economist named George Akerlof published a short paper titled "The Market for 'Lemons.'" It was rejected by three top journals before it found a home. A few decades later it won him the Nobel Prize.

The paper made one observation. Used cars come in two qualities: good ones and lemons — cars with hidden problems the buyer won't discover for months. The seller knows which is which. The buyer doesn't.

Think through what happens. The buyer, unable to tell good from bad, pays an average price — somewhere between what a good car is worth and what a lemon is worth. At that average price, no one with a *good* car wants to sell; they'd lose money. So good cars stay off the market. Only lemons are offered. The buyer observes this and lowers her offer further. More good cars exit. In the limit, the market unravels completely: only lemons trade, and a huge number of mutually beneficial transactions never happen.

One observation. One paragraph of logic. A Nobel Prize.

The observation is called **asymmetric information** — when one side of a transaction knows materially more than the other. And once you see it, you see it everywhere. Health insurance, where the applicant knows her health risks better than the insurer. Job markets, where the applicant knows her own capabilities better than the employer. Lending, where the borrower knows her intent to repay better than the bank. Any market where the seller knows something about the product that the buyer can't verify without incurring substantial cost.

This is the fourth class of market failure — distinct from monopoly, externalities, and public goods. When information is asymmetric, the market fails not because of price-setting power or uncounted costs, but because the *selection* of who shows up to transact is distorted by private knowledge. The good deals leave first. The bad deals stay. You end up trading with the wrong people.

---

## Adverse Selection: The Problem at the Contracting Stage

Akerlof's lemons problem is an instance of **adverse selection**: a problem that operates before the contract is signed, at the selection stage.

The logic is always the same. The informed party has private information that determines whether the contract is favorable or unfavorable for them. Those who find it favorable accept it. Those who find it unfavorable don't. The uninformed party therefore ends up with a non-random sample of the population — systematically skewed toward the bad risks.

In the used-car market, bad-car owners find the average price favorable (they get more than their car is worth). Good-car owners find it unfavorable. So you get a market populated by lemons.

In the health-insurance market, high-risk individuals find coverage favorable — they expect more in claims than they pay in premiums. Low-risk individuals find it less compelling — they may well be healthy and never need it. So the insurance pool fills up with high-risk people. The insurer raises premiums to cover the higher expected claims. Some low-risk people now find coverage even less favorable and drop out. Premiums rise again. More people exit. This is the famous "death spiral" — a market that collapses because the selection problem compounds on itself.

<!-- → [CHART: Adverse selection death spiral — flowchart with arrows. Nodes: (1) Insurer sets premium at average expected cost → (2) Low-risk people find premium unfavorable, exit pool → (3) Pool becomes riskier on average → (4) Insurer raises premium to cover higher expected claims → back to (2). Arrow from (4) also points to: (5) Eventually only very high-risk individuals remain — market unravels. Caption: "Each round of adverse selection drives premiums higher and drives low-risk individuals out. Without intervention, the spiral ends when only the highest-risk individuals remain — or the market collapses entirely."] -->

The institutional responses to adverse selection are several, and each is worth understanding in its own right.

**Signaling.** The informed party takes a costly action that demonstrates their type. A college diploma signals ability to the employer — not necessarily because the courses taught useful skills, but because completing college is more expensive (in time, effort, money) for low-ability people than for high-ability people. The diploma is a signal precisely because it's hard to fake cheaply. Product warranties signal quality. A founder taking a large equity stake signals confidence in the venture.

**Screening.** The uninformed party offers a menu of contracts designed to make different types self-select. Auto insurers offer high-deductible / low-premium contracts (which careful drivers prefer) and low-deductible / high-premium contracts (which accident-prone drivers prefer). The contract choice itself reveals private information. The insurer doesn't have to know who's risky; the contracts do the work.

**Mandatory pooling.** The state requires everyone to participate, which eliminates the selection problem by removing the choice of whether to be in the pool. Social Security works this way — everyone pays in and receives benefits, so adverse selection is impossible. The ACA's individual mandate was an attempt to apply the same logic to private health insurance: if the healthy can't opt out, the pool stays balanced and premiums stay moderate.

**Reputation and third-party verification.** When transactions are repeated and public ratings exist, the seller's incentive to misrepresent quality is reduced. Online review systems are imperfect responses to information asymmetry — they don't solve the problem, but they shift it. Professional licensing, FDA approval, UL certification, building inspections — all are institutions that exist to bridge information gaps the market can't bridge cheaply on its own.

<!-- → [TABLE: Responses to adverse selection — four-row comparison. Columns: Response / How it works / What it requires / Limitation / Real-world example. Rows: Signaling (informed party signals type) — costly action by informed party, signal must be harder to fake for bad types, only works if signal cost is sufficiently different, college diploma / product warranty; Screening (uninformed party designs contract menu) — menu induces self-selection, uninformed party must design separating contracts, equilibrium can be inefficient, insurance deductible tiers; Mandatory pooling (state requires participation) — eliminates selection by removing opt-out, government enforcement, restricts individual choice, Social Security / ACA mandate; Reputation and certification (third-party verifies quality) — ongoing relationship or third-party substitutes for direct info, verification cost must be less than selection cost, doesn't work for one-shot transactions, FDA approval / UL certification. Caption: "No single response dominates. Each trades off the information cost against a different set of implementation costs, restriction costs, or compliance costs."] -->

---

## Moral Hazard: The Problem After the Contract

**Moral hazard** is a different information problem. It operates after the contract is signed.

Once coverage is in place, the insured party has incentives to behave differently than before — and the insurer can't fully observe the behavior. The contract changes the incentives, the informed party adjusts, and the cost lands on the uninformed party.

Examples accumulate quickly. A driver with full collision coverage takes more risks, knowing most accident costs are covered. A patient with comprehensive health insurance uses more medical services than they would if paying out of pocket — not necessarily fraudulently, just at the margin where cost was previously a factor. A bank whose deposits are insured by the FDIC has less reason to be cautious with its loan portfolio; depositors won't run because they're protected, which removes one of the key disciplinary forces on the bank. A tenured professor, freed from the threat of dismissal, may shift time toward research she finds personally interesting at the expense of teaching loads she finds tedious.

The pattern: the contract removes or reduces the cost of a particular behavior, so the party engaging in that behavior does more of it. The insurer — or employer, or regulator, or depositor — bears the resulting cost.

<!-- → [TABLE: Moral hazard examples across contexts — three-column table. Columns: Setting / The contract / How behavior changes afterward. Rows: Auto insurance (collision coverage / driver takes more risks); Health insurance (comprehensive coverage / patient uses more services); Bank deposit insurance (FDIC coverage / bank makes riskier loans); Employment with severance (generous termination package / employee reduces effort); Mortgage guarantee (government-backed loan / lender less careful about borrower quality). Caption: "Moral hazard is not fraud — the insured is acting rationally given their incentives. The problem is that the contract structure externalized part of the cost of the behavior."] -->

Institutional responses to moral hazard:

**Deductibles and copays.** Require the insured to pay a portion of any claim. This preserves some financial skin in the game. A $1,000 health insurance deductible doesn't eliminate moral hazard, but it substantially reduces the incentive to use marginally-valued care.

**Monitoring.** Telematics in auto insurance (a device records driving behavior and adjusts premiums accordingly). Drug testing in employment. Bank stress tests and examinations by regulators. The cost of monitoring is real, but it can substantially reduce the moral-hazard problem when the monitored behavior is observable.

**Performance-based contracts.** Pay tied to outcomes rather than effort. CEO compensation tied to stock price. Sales commissions. "Pay for performance" in medicine. If the agent bears some of the consequences of their choices, the moral-hazard incentive weakens.

**Capital requirements.** In banking, regulations require that banks hold a fraction of their loans as their own equity capital. If a loan defaults, the bank absorbs the first loss from its own capital. This is a structural response to the moral hazard created by deposit insurance — it forces the bank to have skin in the game.

<!-- → [TABLE: Responses to moral hazard — four-row comparison. Columns: Response / How it reduces moral hazard / Where it works best / Limitation. Rows: Deductibles and copays — insured bears part of every loss, health and auto insurance, doesn't help when costs are catastrophic; Monitoring — observe and price actual behavior, telematics, drug testing, bank exams, costly to implement, may create other distortions; Performance-based contracts — agent bears some consequences of outcomes, CEO pay, commissions, insufficient when outcomes are noisy or delayed; Capital requirements — firm bears first loss on own balance sheet, banking and finance regulation, only applies when the firm has identifiable capital at risk. Caption: "Moral-hazard responses generally work by restoring skin in the game — either through direct cost-sharing, observable behavior, outcome-linked pay, or capital at risk. The right response depends on what's observable and what the agent can absorb."] -->

---

## Insurance: The Mechanism

Insurance is the institutional invention that makes these information problems most visible, because it's the institution most completely built on managing risk and information.

The basic mechanism: many people each face a small probability of a large loss — a house fire, a car accident, a serious illness, a death. Each individual's loss is uncertain and unequal across people in any given year. The aggregate across many people is statistically predictable. By pooling premiums and paying out claims from the pool, insurers convert individual risk (highly variable) into predictable group cost (stable).

The mechanism works when four conditions roughly hold. Losses must be *independent* — one person's fire doesn't increase another's probability. The probability of loss must be *approximately known* — the actuary needs to price the premium. The insured can't *fully control* the loss — otherwise moral hazard dominates. And the insured pool must be *roughly random* — otherwise adverse selection dominates.

Insurance markets form and persist when all four hold approximately. They struggle or collapse when one fails. Earthquake insurance is hard because losses are correlated — one quake hits everyone at once. Health insurance for pre-existing conditions is hard because one side knows the probability too well. Long-term care insurance has been a repeated private-market failure because it combines uncertain probability (how long will people live?) with severe moral hazard and adverse selection.

<!-- → [TABLE: When insurance markets fail — summary table. Rows: Correlated losses (earthquake, pandemic) / One side knows probability (pre-existing conditions) / Insured controls the loss (arson) / Adverse selection (only high-risk buy). Columns: Failure mechanism / Why it breaks the market / Typical institutional response. Caption: "Private insurance markets fail in predictable ways. Each failure type maps to a specific mechanism and a specific class of institutional response — government provision, mandatory pooling, risk-rating, or monitoring."] -->

---

## The ACA Mandate and the Logic of Forced Pooling

The Affordable Care Act of 2010 included an individual mandate — a requirement that everyone obtain health insurance or pay a tax penalty. The penalty was zeroed out federally in 2017, though several states maintain their own.

The mandate's structural logic was a direct response to adverse selection. Before the ACA, insurers could screen applicants, deny coverage for pre-existing conditions, and charge higher premiums to sicker individuals. The ACA prohibited most of that screening. Once screening was prohibited, the healthy could stay out of the pool. But they had strong incentives to stay out — they'd pay premiums without expecting to receive much in claims. Without the mandate, the only people who would voluntarily buy insurance are those who expect it to pay off — the sick. Premiums would rise; more healthy people would exit; premiums would rise further. The death spiral.

The mandate was the structural response: if everyone must participate, the adverse selection problem disappears. The pool reflects the population's average risk, not the voluntary-buyer population's above-average risk.

The empirical evidence from states that removed mandates and from ACA markets without effective mandate enforcement is broadly consistent with the adverse-selection prediction — higher premiums, thinner enrollment, larger shares of sick enrollees. The magnitude is debated. The direction is not.

The mandate was politically controversial in ways the structural logic was not. The individual-liberty objection to a government requirement to purchase a private product is coherent and not settled by the economics. The economics tells you what happens to the insurance pool; it doesn't tell you whether forced pooling is a legitimate use of government power. Both observations can be held at once.

---

## Information Asymmetry as a Lens

Pull back. What have we built in this chapter?

A diagnosis: when one party knows materially more than the other, market transactions become systematically distorted. The wrong people show up to trade (adverse selection). The right behavior deteriorates after the deal is made (moral hazard). The market either fails to form or forms at the wrong price with the wrong mix of participants.

A vocabulary for institutions: signaling, screening, mandatory pooling, monitoring, performance contracts, capital requirements, reputation, certification. Each exists because the market, left alone, can't bridge the information gap cheaply enough. Each has its own cost.

A structure for healthcare: the market that most clearly illustrates all of these problems at once. Patients don't know what care is necessary (information asymmetry on quality). Insurers can't observe patient health choices (moral hazard on the insured side). Healthy individuals may not voluntarily buy coverage (adverse selection if screening is prohibited). Physician markets in many regions are concentrated (monopsony from Chapter 14). The industry has large externalities (Chapter 12: one person's vaccination protects others). And individual capacity to make rational decisions under stress and illness is limited (Chapter 6's behavioral economics applies directly). No single simple model handles all of this. But each model illuminates one piece of it.

<!-- → [TABLE: Healthcare as a convergence of market failures — one row per failure mode. Columns: Failure type / How it appears in healthcare / Which chapter's tools address it. Rows: Information asymmetry (patient-provider) — patient doesn't know if treatment is necessary, provider does — Ch 16 adverse selection and principal-agent; Moral hazard — insured patient uses more services than they would paying out of pocket — Ch 16 deductibles, copays, monitoring; Adverse selection — healthy individuals avoid coverage if premiums reflect sick pool — Ch 16 mandatory pooling, ACA mandate; Monopsony — hospital systems or large employers dominate local physician markets — Ch 14 monopsony; Negative externality — vaccination and disease control produce spillovers beyond the individual — Ch 12 Pigouvian subsidy; Behavioral failures — patients make poor decisions under stress, time pressure, limited information — Ch 6 present bias, framing effects. Caption: "Healthcare is the stress test for the entire toolkit. No single market-failure chapter handles it; each chapter handles one piece. This is why healthcare policy is hard: you can fix one failure and worsen another."] -->

That is how economics progresses. Not one model that explains everything, but a collection of models, each sharp about a different failure mode. The skill is knowing which model to reach for.

---

## LLM Exercises

**Exercise 1 — Diagnose the type.** Give an LLM this list and ask it to classify each as primarily an adverse-selection problem, a moral-hazard problem, or both:
- A driver buys auto insurance, then drives more aggressively.
- A person with cancer buys life insurance without disclosing the diagnosis.
- A student gets a job at a software company that promises six months of severance, then puts in less effort.
- A homeowner installs a fire-suppression system after buying fire insurance.
- A bank knows its deposits are FDIC-insured, then makes riskier loans.

**Exercise 2 — Design a screening contract.** Tell an LLM you run an auto insurance company. You suspect your customers fall into two groups — careful drivers (low accident probability) and reckless drivers (high probability) — but you can't tell them apart. Ask the LLM to design two insurance contracts that, taken together, will get the careful drivers to choose one and the reckless drivers to choose the other. The exercise teaches the screening logic concretely.

**Exercise 3 — Predict the death spiral.** Tell an LLM a hypothetical: a state outlaws insurer screening for pre-existing conditions but does *not* require people to buy insurance. Ask it to walk through what should happen to the insurance market over the next several years using adverse-selection logic. Push: what additional policy would be needed to prevent collapse?

**Exercise 4 — Argue for and against the individual mandate.** Ask an LLM to argue both sides of the ACA individual mandate as a structural response to adverse selection. The pro side should focus on adverse-selection logic and pool stability. The anti side should focus on personal liberty and the costs of coercion. Evaluate which case is stronger and what evidence would settle the empirical disagreement.

**Exercise 5 — Identify a moral-hazard problem you face.** Tell an LLM about a contract or institutional arrangement in your own life (employment, insurance, banking, relationships) that you suspect produces moral-hazard effects. Ask the LLM to identify the specific mechanism and to suggest institutional changes that would reduce it. Evaluate whether the suggestion is structural or just exhortational.

---

## LLM Exercise — Chapter 16: Information, Risk, and Insurance (Policy Brief Project)

**Project:** Policy Brief.
**What you're building this chapter:** the asymmetric-information analysis — adverse selection, moral hazard, and the insurance question as it bears on your policy.
**Tool:** **Claude Project** "Policy Brief" — appends a section.

---

**The Prompt:**

```
Chapter 16 of my Policy Brief project. Prior sections in this Claude
Project. Chapter 16 taught: asymmetric information (the lemons
problem — Akerlof's used-car market collapses when buyers can't
distinguish quality); adverse selection (occurs at the contracting
stage — bad risks are more likely to seek insurance); moral hazard
(occurs after the contract — insured behavior changes once the
risk is shared); insurance as risk pooling and the conditions for
viable insurance markets (independent risks, large pools, ability
to price risk).

Write the brief's "Information and Risk Analysis" section in
300–500 words.

1. **The information asymmetries in your policy's market.** What
   does each side know that the other doesn't? Sellers know
   product quality; buyers don't. Workers know effort; employers
   don't. Borrowers know default risk; lenders don't. Identify
   the central asymmetry in your policy's market and what
   distortion it creates.

2. **Adverse selection and moral hazard.** If your policy is
   insurance-like (pooling risk across people or time), name the
   adverse-selection and moral-hazard risks specifically. If it
   isn't, name where the policy might inadvertently CREATE
   adverse selection (e.g., a regulation that drives some
   suppliers out leaves the lemons behind) or moral hazard (e.g.,
   a guarantee that reduces the downside of risky behavior).

3. **The information solution.** Most asymmetric-information
   problems are addressed by signaling, screening, mandatory
   disclosure, or third-party certification. Name which solution
   your policy uses (if any) and what's foregone by the choice.

End with one sentence on the information failure that's most
predictive of your policy's success or failure. Many policies fail
because the information assumption underlying them was wrong.
```

---

**What this produces:** A 300–500 word section on information asymmetries and risk-pooling. Especially central for insurance, healthcare, financial-regulation, and consumer-protection policies.

**How to adapt this prompt:**

- *For your own project:* Healthcare students: this is the central chapter — adverse selection is what makes insurance markets fragile. UBI students: moral hazard (work disincentive) is the standard critique to address. Antitrust students: information asymmetries justify regulation when self-help solutions fail.
- *For ChatGPT / Gemini:* Works as written.
- *For Claude Code:* Not the primary tool here.
- *For a Claude Project:* Append.

**Connection to previous chapters:** Ch 12 (negative externalities) and Ch 13 (positive externalities) plus Ch 16 (asymmetric info) are the three classical market-failure chapters. Most policies address at least one.

**Preview of next chapter:** Chapter 17 covers financial markets — bonds, stocks, diversification, the random-walk hypothesis, financial-system fragility. If your policy touches finance directly, this is central; even if not, the financial-market response to your policy is worth tracing.

---

## AI Wayback Machine

**George Akerlof** developed the lemons model of information asymmetry in 1970 — Nobel 2001.

**Run this:**

```
Who is George Akerlof, and how does their work connect to
information and risk we covered in this chapter? Keep it to three
paragraphs. End with the single most surprising thing about
their career or ideas.
```

→ Search **"George Akerlof"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to apply George Akerlof's framework to a current economic question.
- Add a constraint: "Answer including criticisms or limits of George Akerlof's framework."

What changes? What gets better? What gets worse?

---

*Byline: Nik Bear Brown.*
