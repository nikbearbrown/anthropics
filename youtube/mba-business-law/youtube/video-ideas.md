# Video Ideas — mba-business-law
*Scouted 2026-07-09 from 14 narrative chapters.*

---

## Candidate 01 — Why a Farmer Who Never Left Ohio Could Be Taxed by the Federal Government
- Source: `mba-business-law/chapters/04-business-and-the-united-states-constitution.md`
- Topic: BUSINESS LAW
- Hook: Roscoe Filburn grew wheat in Ohio, never sold a bushel, never crossed a state line — and the Supreme Court held the federal government could still fine him. Not a loophole. The Constitution required it.
- Key case: *Wickard v. Filburn* (1942) — Ohio farmer fined under the Agricultural Adjustment Act for growing wheat to feed his own chickens.
- The Question: If a farmer never leaves his own farm, how can his private wheat harvest be subject to federal commerce law?
- Core idea: The substantial-effects test shifts the constitutional question from "did this individual transaction cross a state line?" to "does this *category* of activity, across all persons who engage in it, produce substantial effects on interstate commerce?" Because thousands of farmers growing their own wheat instead of buying market wheat materially depresses wheat prices, any individual farmer's private harvest is constitutionally reachable. The individual act is trivial; the aggregate category is enormous.
- Visual object: A scale-balance diagram morphing from "individual farm → market" (no connection visible) into "category of activity × 1 million farms → national wheat market" (connection obvious), with an HHI-style aggregate bar filling up.
- Manim move: accumulate (individual farm dots appear one by one, then collapse into a single aggregate bar that tips the scale)
- Example seed: A local bakery buys flour from a regional mill. One day the owner decides to grow and grind his own wheat instead. His individual decision has zero measurable impact on the flour market. But the Supreme Court's logic holds: if all small bakeries made the same decision, aggregate wheat demand would fall substantially — so Congress can regulate even this private bakery's private wheat. The principle that made the Civil Rights Act of 1964 constitutional (racial discrimination in lodging, in aggregate, burdens interstate travel) is the exact same principle.
- Length band: 3–5 min
- Still lanes: geo (map of Filburn's Ohio farm vs. national wheat market), raster (wheat field image as texture layer)
- Prerequisites: Basic idea that the federal government has limited powers; awareness that "interstate commerce" has something to do with federal authority.
- Exclusions: Full Lopez/Morrison/Sebelius chain (save for a separate card); New Deal context beyond minimum needed; dormant Commerce Clause.
- Score: 10/10

---

## Candidate 02 — How 26 Years of Legal Strategy Became Worthless Overnight
- Source: `mba-business-law/chapters/01-american-law-legal-reasoning-and-the-legal-system.md`
- Topic: BUSINESS LAW
- Hook: For 26 years, Amazon and thousands of other companies deliberately avoided building warehouses in certain states — purely to exploit a 1992 Supreme Court ruling. In 2018, that ruling was overruled. Every strategy built around it became instantly obsolete.
- Key case: *South Dakota v. Wayfair* (2018) overruling *Quill Corp. v. North Dakota* (1992) — the physical-presence sales-tax rule.
- The Question: How can a Supreme Court precedent that every company's tax lawyer treated as bedrock law simply disappear — and what does that mean for any legal strategy that exists right now?
- Core idea: *Stare decisis* makes legal rules durable but not permanent. When the factual conditions underlying a rule's original reasoning have changed so fundamentally that the rule now produces the opposite of what it intended, courts can and do overturn it. The physical-presence proxy — invented because a thin connection to a state shouldn't trigger obligations — inverted when e-commerce scaled: $100K of annual South Dakota sales is not a thin connection. The rule had become a lie about the reality it was meant to measure. The majority overruled it not because *Quill* was wrongly decided in 1992 but because 2018 conditions made its logic false.
- Visual object: A timeline arrow (1992 → 2018) with a "precedent cliff" — the arrow runs level for 26 years, then drops sharply when the Court overrules. Annotation: "e-commerce scales" appears midway, annotating the widening gap between rule-as-written and commercial reality.
- Manim move: trace (timeline traces 1992 rule → growing e-commerce curve → 2018 overrule cliff)
- Example seed: A Boston furniture company sets up its e-commerce presence in 2005. Its lawyers confirm: as long as you have no warehouse or employees in South Dakota, you owe them nothing. The company builds its entire logistics model around avoiding physical presence in high-tax states. On June 21, 2018, the Supreme Court decides *Wayfair* before the market opens. By the end of that business day, the company has new tax obligations in up to 45 states it had never filed in. No transition period. Immediate effect. The strategy worked — right up until the morning it didn't.
- Length band: 3–5 min
- Still lanes: geo (South Dakota vs. national e-commerce map), c2v (precedent timeline graphic)
- Prerequisites: Basic awareness that states can collect sales tax; no prior legal knowledge needed.
- Exclusions: Full four-source hierarchy of law (keep to minimum); dormant Commerce Clause doctrine; state-by-state economic nexus threshold variation.
- Score: 10/10

---

## Candidate 03 — The McDonald's Coffee Case Was Never About Clumsy Grandmothers
- Source: `mba-business-law/chapters/06-the-tort-system.md`
- Topic: BUSINESS LAW
- Hook: You probably heard the McDonald's coffee lawsuit as: old woman spills coffee, sues, wins lottery. The actual record shows: McDonald's knew its coffee caused third-degree burns, had 700 complaints, did a cost-benefit analysis, and decided the injury claims were worth it. The jury knew that too.
- Key case: *Liebeck v. McDonald's Restaurants* (1994) — 81-year-old sustains third-degree burns over 6% of her body; punitive award calibrated to two days of McDonald's coffee revenue.
- The Question: If the McDonald's coffee case wasn't about a clumsy customer winning the lottery, what was it actually about — and why does that distinction matter for how companies make safety decisions today?
- Core idea: The four-element negligence framework (duty → breach → causation → damages) is the machinery the verdict ran through. McDonald's breach was not serving hot coffee; it was serving coffee at a temperature they *documented* caused severe burns, to customers they *documented* had been burned before, after they *calculated* that injury payouts were cheaper than changing the temperature. The jury's punitive award was not sympathy — it was a response to documented decision-making that treated customer burns as an acceptable cost of business. The apparatus worked as designed: making documented corporate choices to accept known harms costly enough to change future choices.
- Visual object: A four-cell table (Duty / Breach / Causation / Damages) that builds element by element, with the McDonald's internal memo appearing as a "breach" evidence card that flips visible mid-animation.
- Manim move: transform (blank 4-element grid → each cell fills with specific case evidence → final cell (damages) splits into compensatory and punitive bars)
- Example seed: A grocery store receives a written complaint that aisle 7's refrigeration unit is leaking. The manager reads it, files it, does nothing. Three days later a customer slips on the puddle and breaks her wrist. The manager's inaction is not an accident — it is the breach. The negligence framework asks not "was there an accident?" but "did you take the care a reasonable person would take given what you knew?" The documented notice converts a slip-and-fall into a negligence case.
- Length band: 3–5 min
- Still lanes: raster (McDonald's styrofoam cup heat graphic), c2v (four-element framework)
- Prerequisites: No legal background needed; basic intuition that lawsuits involve a wrong and a remedy.
- Exclusions: Strict product liability (save for companion card); comparative negligence mechanics; punitive-damages constitutional limits.
- Score: 10/10

---

## Candidate 04 — Why Google Paying $10 Billion a Year to Be the Default Might Be Illegal
- Source: `mba-business-law/chapters/11-antitrust-law.md`
- Topic: BUSINESS LAW
- Hook: Google's search engine is free. On the standard model of antitrust harm — monopolist raises prices — there is no harm to identify. So why did a federal court find in 2024 that Google had illegally maintained its search monopoly?
- Key case: *United States v. Google* (2020/2024) — DOJ found that default-placement agreements paying ~$10B/year to Apple and others illegally foreclosed competing search engines from reaching viable query volume.
- The Question: If the price to consumers is zero, how can a dominant company's behavior be anticompetitive? What does antitrust law protect when there is no price to raise?
- Core idea: Antitrust distinguishes winning by making a better product (legal) from winning by making it structurally impossible for any competitor to challenge you (illegal). Google's default-placement payments did not improve search quality — they purchased the chokepoints through which users reach any search engine at all. Rivals who cannot reach sufficient query volume cannot train competitive algorithms. The barrier is not price; it is the feedback loop between query volume and algorithm quality that makes the market self-reinforcing. Antitrust was built for Standard Oil's physical infrastructure monopoly; the Google case asks whether the same principle applies to data-and-default monopolies.
- Visual object: A split diagram — left side: Standard Oil's pipeline map (physical infrastructure chokepoints); right side: Google's distribution map (device defaults as digital chokepoints). The structural parallel is visible: both create a toll on access to the market.
- Manim move: morph (Standard Oil pipeline map morphs into Google default-placement architecture; chokepoint nodes pulse in both)
- Example seed: Imagine you start a new search engine. Your results are good — maybe 90% as good as Google's. But you can only reach users who go out of their way to change their phone's default. Of the billion people who type searches into their phones today, 98% go to Google simply because it was there when they turned on the device. Your engine never gets enough queries to train its ranking algorithm to match Google's. The default placement is not a product feature. It is a structural exclusion — and it costs $10 billion per year to maintain because it is worth more than that.
- Length band: 3–5 min
- Still lanes: c2v (distribution-chokepoint diagram), geo (global search market share map)
- Prerequisites: Basic awareness that monopoly = bad; vague knowledge that antitrust exists.
- Exclusions: HHI merger math; per-se vs. rule-of-reason distinction (mention only); FTC v. Meta and DOJ v. Apple (save for companion card or brief mention).
- Score: 9/10

---

## Candidate 05 — Why a NASDAQ Listing in Sweden Made Ericsson Pay $1 Billion to the United States
- Source: `mba-business-law/chapters/13-international-law.md`
- Topic: BUSINESS LAW
- Hook: Ericsson is a Swedish company. Its bribes went to officials in Djibouti, Vietnam, Indonesia, and Kuwait. The U.S. Department of Justice collected $1 billion in settlement. The company had no operations in the United States.
- Key case: *United States v. Ericsson* (deferred prosecution agreement, 2019/2022) — FCPA enforcement against Swedish telco for multi-continent bribery.
- The Question: How does the United States have authority to prosecute a Swedish company for bribing officials in Southeast Asia — and what does that mean for any company with any connection to U.S. markets?
- Core idea: The Foreign Corrupt Practices Act's jurisdictional reach follows "hooks" — not geography. Any one hook (U.S. securities listing, U.S. employee, U.S. bank used in the transaction) is sufficient to bring a company fully inside U.S. FCPA jurisdiction for conduct anywhere in the world. Ericsson's NASDAQ ADR listing was the hook. That single capital-market decision made its entire global business conduct subject to U.S. law. The FCPA is structured this way deliberately: to prevent U.S.-connected firms from treating bribery as a permissible cost of doing business in markets where it is locally tolerated.
- Visual object: A hub-and-spoke diagram — center node: Ericsson (Stockholm). Spokes: Djibouti, China, Vietnam, Indonesia, Kuwait (bribery sites). Separate spoke: NASDAQ listing. Callout: "This one hook = U.S. jurisdiction over everything on this diagram."
- Manim move: spread (hub-and-spoke expands outward from Ericsson center; all bribery spokes appear first, then the NASDAQ hook lights up and a jurisdiction boundary ring closes around the entire diagram)
- Example seed: A German engineering firm has no U.S. offices, no U.S. customers, and makes all its products in Germany. But it lists shares on the New York Stock Exchange. Its sales team in Thailand pays a government ministry official to win a infrastructure contract — a practice they understand to be locally customary. The U.S. DOJ opens an investigation. The German firm's lawyers explain that the conduct happened entirely in Thailand. The DOJ's response: your NYSE listing is enough. One stock-exchange decision bound your entire global operation to U.S. anti-bribery law.
- Length band: 2–3 min
- Still lanes: geo (world map with bribery-site pins and U.S. jurisdiction ring), c2v (FCPA hook diagram)
- Prerequisites: Basic awareness that different countries have different laws; no prior legal knowledge needed.
- Exclusions: Full FCPA anti-bribery vs. accounting-provisions distinction (mention briefly); UK Bribery Act comparison; CISG and New York Convention.
- Score: 9/10

---

## Candidate 06 — The Secret That Kept 3.5 Million Fraudulent Accounts Open for Five Years
- Source: `mba-business-law/chapters/03-business-ethics-and-social-responsibility.md`
- Topic: BUSINESS LAW
- Hook: Wells Fargo had a code of conduct. A compliance function. A whistleblower hotline. An annual ethics training. And for five years, its employees opened 3.5 million fraudulent accounts in customers' names without their knowledge. The compliance apparatus failed completely. Here is why.
- Key case: Wells Fargo unauthorized-account scandal (2011–2016) — $185M initial fine, subsequent billions in regulatory actions, CEO resignation.
- The Question: If a company has all the formal ethics infrastructure — the code, the hotline, the training — why does systematic misconduct persist for five years without the infrastructure stopping it?
- Core idea: The operative culture of an organization — what actually governs employee behavior when no one senior is watching — is determined by what the incentive structure rewards and what management tolerates, not by what the code of conduct says. Wells Fargo's compensation structure rewarded account-opening volume above everything; management tolerated and in some cases encouraged the behavior required to hit targets. The code of conduct was decorative. The culture tracked the incentive structure. The apparatus predicts both the Wells Fargo outcome and its structural opposite (Gravity Payments / Dan Price): the firm's operative culture will consistently produce whatever its compensation structure rewards, at scale, for as long as the structure remains in place.
- Visual object: A two-panel "building" diagram — left panel: the formal compliance building (code of conduct on the first floor, whistleblower hotline, third-party investigation stacked above). Right panel: a second building showing what actually governed behavior (compensation targets on floor 1, management tolerance on floor 2, operative culture emerging at the top). The two buildings look identical from the outside.
- Manim move: split (a single building splits into two — one shows stated values, one shows operative incentives; both look identical from the street view)
- Example seed: A claims-handler at an insurance company is paid a bonus for each claim resolved per week. The code of conduct says treat every claimant fairly. Her supervisor tells her: "Get the number up." When she settles a valid claim prematurely to hit her target, no one notices — it looks like resolution speed. The code of conduct never fires. The operative culture, driven by the compensation signal her supervisor sends, fires every time. The Wells Fargo case multiplied this dynamic by a factor of 5,300 branch employees over five years.
- Length band: 3–5 min
- Still lanes: c2v (compliance-building diagram), raster (Wells Fargo branch interior texture)
- Prerequisites: Basic awareness of corporate governance; no legal background needed.
- Exclusions: Sarbanes-Oxley section-by-section detail (mention SOX briefly); Enron/WorldCom history (limit to one sentence); Dodd-Frank whistleblower program dollar figures (mention but don't dwell).
- Score: 9/10

---

## Candidate 07 — How a Victorian Smoke Ball Advertisement Became 130 Years of Contract Law
- Source: `mba-business-law/chapters/07-contract-law.md`
- Topic: BUSINESS LAW
- Hook: In 1893, a British court ruled that a newspaper advertisement — not signed, not negotiated, not delivered to any specific person — was a binding legal contract. The company had to pay. The principle that ruling created is still taught in every common-law contract course in the world.
- Key case: *Carlill v. Carbolic Smoke Ball Company* (Court of Appeal, 1893) — advertisement offering £100 to anyone who used the smoke ball and contracted influenza was a binding unilateral offer accepted by performance.
- The Question: If a contract requires two parties to agree, how can an advertisement you read in a newspaper — that no one sent you, that no one signed, that no one negotiated with you — be a legally binding contract?
- Core idea: A contract is not a ceremony — it is an agreement, and agreements can take many forms. The five-element framework (offer, acceptance, consideration, capacity, legality) determines whether an agreement is binding, not whether it was formal. A serious offer open to the world at large can be accepted by performance — not by saying "I agree" but by actually doing what the offer specified. The Carbolic Smoke Ball Company's deposit of £1,000 was a costly, visible signal that the offer was serious. Carlill's compliance with the conditions was her acceptance. No handshake, no signature, no negotiation. The five elements were satisfied. The implication for commerce: every factual claim your organization makes about its products — in ads, emails, demos, product pages — is potentially part of the legal architecture of a sale.
- Visual object: A pentagon labeled "CONTRACT" at the center with five vertices (Offer / Acceptance / Consideration / Capacity / Legality). A second animation shows the Carlill newspaper ad being parsed through each vertex — lighting each one green as it is satisfied — ending with all five lit and the word "ENFORCEABLE" appearing at the center.
- Manim move: accumulate (five-vertex pentagon builds from empty to fully lit as each element is established on the Carlill facts)
- Example seed: A software company's sales engineer sends a potential client a product demo showing the platform handles 10,000 concurrent users. The written contract later says "performance may vary." The demo was a factual representation. The client relied on it to sign. Under contract law, the demo may be an express warranty that survives the general disclaimer — because the conduct and representations are the evidence of the agreement, not just the final document. The Carlill principle: what the parties do and say is the contract, whether or not a ceremony happened.
- Length band: 2–3 min
- Still lanes: raster (Victorian newspaper advertisement image), c2v (five-element pentagon)
- Prerequisites: Intuition that a contract is "a deal" between two people; no legal background needed.
- Exclusions: Promissory estoppel (save for companion card); UCC mirror-image rule; full remedies framework.
- Score: 9/10

---

## Candidate 08 — The Worker Classification Question Worth $97 Million (and Counting)
- Source: `mba-business-law/chapters/09-employment-and-labor-law.md`
- Topic: BUSINESS LAW
- Hook: In 2000, Microsoft settled a class action for $97 million. The workers who sued had worked alongside Microsoft employees, doing identical work, for years. They had been classified as independent contractors — and that classification excluded them from Microsoft's stock-option plan, which had made Microsoft employees wealthy.
- Key case: *Vizcaino v. Microsoft* — long-tenure contractor class action; plus California's AB 5 / ABC test fight with Uber/Lyft/DoorDash ($200M Prop 22 campaign).
- The Question: What is the legal difference between an employee and an independent contractor — and why does that single classification question determine whether a company owes minimum wage, overtime, workers' comp, Social Security contributions, and anti-discrimination protection?
- Core idea: Three different tests apply — the IRS three-category test, the FLSA economic-realities test, and California's ABC test — and they can reach different conclusions on the same facts. The classification is not about the label on the contract; it is about the structural reality of the work relationship. The ABC test's B prong is the hardest for platform companies: you must show the worker's activity is outside the usual course of your business. It is difficult to argue that driving passengers is outside Uber's usual business when driving passengers is Uber's entire business. The classification question is, at its core, a question about who bears the cost of labor conditions.
- Visual object: A three-panel side-by-side of the three tests (IRS / FLSA / ABC) applied to one identical fact pattern (a ride-share driver) — showing where each test produces "employee" vs. "contractor" and why. The ABC test's B prong highlighted in red.
- Manim move: compare (three test columns appear simultaneously; each applies the same driver fact pattern down its rows; the bottom row shows the divergent conclusions)
- Example seed: A freelance graphic designer works exclusively for one company. She uses her own equipment. She sets her own hours. She works from home. But she has worked for this company for three years, has no other clients, and the company's creative director tells her what to design each week. Under the IRS test: probably a contractor (her own equipment, her own location). Under the FLSA economic-realities test: probably an employee (economically dependent on one client, integrated into the business). Under California's ABC test: almost certainly an employee (her design work is the company's core business — the B prong fails). Same person, same facts, three different answers.
- Length band: 3–5 min
- Still lanes: c2v (three-test comparison grid), geo (California vs. federal jurisdiction map)
- Prerequisites: Basic awareness that there is a difference between "an employee" and a freelancer; no legal background needed.
- Exclusions: Full FLSA wage-and-hour detail; NLRA collective-bargaining structure; ADA and ADEA detail.
- Score: 9/10

---

## Candidate 09 — How Congress Handed Its Lawmaking Power to Someone Else (Legally)
- Source: `mba-business-law/chapters/10-government-regulation.md`
- Topic: BUSINESS LAW
- Hook: The U.S. Constitution gives Congress — and only Congress — the power to make law. And yet: the EPA's emission limits have the force of law. The SEC's disclosure format requirements have the force of law. The FDA's drug approval standards have the force of law. None of these rules were passed by Congress. How is that constitutional?
- Key case: The *Chevron* deference doctrine (1984) and its 2024 overruling in *Loper Bright Enterprises v. Raimondo* — the most consequential administrative-law decision in 40 years.
- The Question: When Congress delegates its lawmaking authority to expert agencies, who gets to decide what ambiguous statutory language actually means — the agency, or the courts? And what changed in 2024?
- Core idea: The delegation chain works because Congress creates the policy mandate through an enabling statute and retains accountability through judicial review and APA procedural requirements. For 40 years, *Chevron* deference meant courts deferred to agencies' reasonable interpretations of ambiguous statutes — agencies accumulated interpretive authority. *Loper Bright* (2024) ended that: courts must now independently determine the best reading of ambiguous statutes. Regulations built on aggressive interpretations of ambiguous authority are more vulnerable than they were the day before the decision. The "regulatory cushion" is gone.
- Visual object: A three-node delegation chain: Congress (enabling statute) → Agency (rulemaking) → Courts (review). A large arrow from Courts back to Agency labeled "Chevron deference: was 'is this reasonable?'" morphs into a stronger arrow labeled "Post-Loper Bright: 'what is the best reading?'" The shift in arrow weight and direction shows the transfer of interpretive authority back to courts.
- Manim move: transform (Chevron-era chain diagram morphs into post-Loper Bright diagram; the court-to-agency deference arrow shrinks and reverses direction)
- Example seed: In 2022, the EPA argued that a Clean Air Act provision authorizing regulation of power-plant emissions gave it authority to restructure the entire U.S. power grid toward renewables. The Supreme Court said no — that is a "major question" requiring clear congressional authorization, not just a plausible reading of ambiguous text. *West Virginia v. EPA* was decided two years before *Loper Bright* fully ended Chevron deference. Together, the two cases mean: the bigger the regulatory claim, the clearer the congressional authorization must be. Rules resting on decades of agency interpretation of ambiguous authority are now more exposed than they were before June 2024.
- Length band: 3–5 min
- Still lanes: c2v (delegation-chain diagram with morphing deference arrow), raster (Federal Register cover as texture)
- Prerequisites: Vague awareness that government agencies (EPA, FDA, SEC) make rules; no legal background needed.
- Exclusions: Full notice-and-comment rulemaking process (mention briefly); APA arbitrary-and-capricious review (mention only); specific agency-by-agency detail.
- Score: 8/10

---

## Candidate 10 — Insider Trading's Dirty Secret: You Don't Have to Work at the Company
- Source: `mba-business-law/chapters/14-securities-regulation.md`
- Topic: BUSINESS LAW
- Hook: Rajat Gupta never bought a single share using inside information. He just told his friend Raj Rajaratnam what he had heard in Goldman Sachs board meetings. Gupta was convicted of securities fraud and sentenced to two years in federal prison. He never made a dime.
- Key case: *United States v. Gupta* (2012) — Goldman Sachs board member convicted as tipper under classical insider-trading theory; plus *United States v. O'Hagan* (1997) misappropriation theory for outsiders.
- The Question: You never bought or sold a share, you never worked at the company, you just passed along something you heard — can you be convicted of insider trading?
- Core idea: Insider-trading liability runs through two theories. The classical theory covers corporate insiders who trade on their company's own material non-public information — the breach is of a fiduciary duty to shareholders. The misappropriation theory (*O'Hagan*) extends liability to anyone who obtains material non-public information through a breach of duty to the *source* of the information — a lawyer, banker, or government employee who trades on a client's confidential information violates Rule 10b-5 even with no connection to the company whose securities are traded. Tippee liability (Gupta's path) adds a third layer: giving inside information to a trading friend or relative is itself the breach, and the benefit is the gift — you don't need to receive money or even a formal quid pro quo. The liability chain runs from the breach of trust at the source through every person who knowingly benefits from that breach.
- Visual object: A three-node chain: Gupta (tipper, Goldman board member) → Rajaratnam (tippee, Galleon Fund) → "Galleon profits on Goldman stock." Each node labeled with the legal theory that makes it liable. A parallel chain below: O'Hagan (lawyer) → trades in target company → no connection to company needed.
- Manim move: trace (liability chain traces from tipper to tippee; branching node shows classical theory vs. misappropriation theory as two routes to the same violation)
- Example seed: A paralegal at a law firm works on a merger file. She tells her sister "the company I'm working on is about to be acquired — don't tell anyone, just thought you'd want to know." The sister buys 500 shares. The SEC investigates. The paralegal: liable as a tipper under the misappropriation theory — she misappropriated information belonging to her firm's client. The sister: liable as a tippee if she knew (or should have known) the information came from a breach and the tipper got a personal benefit — here, the gift to a family member is the benefit under *Salman* (2016). Neither person is a corporate insider. Neither directly traded on the company's own information. Both are convicted.
- Length band: 2–3 min
- Still lanes: c2v (liability chain diagram), raster (Goldman Sachs building as texture)
- Prerequisites: Basic awareness that insider trading = trading on secret company information; no prior securities-law knowledge needed.
- Exclusions: Full securities-registration framework; Reg D/exemptions; SOX/Dodd-Frank amendments.
- Score: 8/10

---

## Candidate 11 — What Happens When the Law Says You Broke the Law Even Though You Didn't Mean To
- Source: `mba-business-law/chapters/05-criminal-liability.md`
- Topic: BUSINESS LAW
- Hook: Bernie Madoff received a 150-year prison sentence. Every legal defense available — the best white-collar lawyers money could buy — was useless. There was no settlement, no insurance payout, no board remediation plan that substituted for that sentence. Criminal law is the one risk in business you cannot pay your way out of.
- Key case: *United States v. Madoff* (2009) — $65B Ponzi scheme, 11 federal felony counts, 150-year sentence, died in custody; plus the structural template that appears in every smaller fraud case.
- The Question: What makes criminal liability categorically different from every other legal risk a business faces — and why does the structure of white-collar crime make it so hard to detect and so devastating when it surfaces?
- Core idea: Criminal law differs from every other legal framework in this book by making imprisonment, not money, the remedy. No settlement buys that back. The three structural features of white-collar crime (deceit, concealment, violation of trust) produce a consistent profile: offenses run for years before detection, are hidden within normal business operations, and are discovered through external review — not internal controls. The same template operates at every scale from Madoff ($65B) to Sachdeva ($34M): position of trust + sustained misrepresentation + concealment within business records + external trigger = prosecution. Scale differs; mechanism is identical.
- Visual object: A two-column structural comparison table — Madoff / Sachdeva (Koss Corporation). Rows: Position of Trust | Mechanism of Extraction | Concealment Method | Duration Before Detection | How Detected | Criminal Outcome. The 1,900x scale difference is visible in one column entry; every other row is structurally identical.
- Manim move: compare (two columns fill in row by row; a "scale" indicator shows $65B vs. $34M while all other rows show identical structural entries)
- Example seed: A university controller has check-writing authority over departmental accounts. Over three years, she processes $2.3 million in fictitious invoices, wiring the proceeds to a personal LLC. She is not detected by the university's annual audit — the invoices match procurement patterns and the external auditor samples only a fraction of payables. She is detected when a vendor contacts the department wondering why they keep receiving orders they never filled. The mechanism: position of trust + sustained misrepresentation + concealment within normal business records + external review. The same template as Madoff, at 0.0035% of the scale.
- Length band: 2–3 min
- Still lanes: c2v (structural-template comparison table), raster (courtroom image as texture)
- Prerequisites: Basic awareness that fraud is illegal; no prior legal background needed.
- Exclusions: RICO detail; FCPA (covered in Ch. 13 card); full constitutional analysis of Fourth/Fifth/Sixth amendments; civil-criminal parallel tracks.
- Score: 8/10

---

## Candidate 12 — The Ford Pinto Memo and What Happens When Your Internal Documents Go to Trial
- Source: `mba-business-law/chapters/06-the-tort-system.md`
- Topic: BUSINESS LAW
- Hook: Ford calculated that redesigning the Pinto's fuel tank would cost $11 per vehicle. It calculated that the expected cost of injury and death claims from leaving the tank as-is was lower. It chose not to redesign. Those internal documents went to a jury.
- Key case: *Grimshaw v. Ford Motor Company* (1981) — $125M punitive award (reduced to $3.5M) for design-defect strict liability after Ford's cost-benefit memo was admitted into evidence.
- The Question: What is the legal difference between a product that accidentally injures someone and a product whose manufacturer documented knowing it would injure people and chose not to fix it?
- Core idea: Strict product liability removes the question of fault entirely — a defective product that causes harm creates liability regardless of how careful the manufacturer was. The three defect categories (manufacturing / design / warning) define what "defective" means. But when a manufacturer has *documented* internal awareness of a known risk and *documented* a decision not to act on it, the case moves from compensatory territory into punitive territory. Punitive damages are calibrated not to the plaintiff's harm but to the defendant's conduct and capacity — the jury's job is to make the consequence register for a company large enough to absorb any individual compensatory award. The Ford memo made that move inevitable.
- Visual object: A two-column structural comparison: Liebeck (McDonald's) / Grimshaw (Ford). Rows: Known risk documented internally | Decision not to act | Internal rationale | Compensatory damages | Punitive damages awarded | Judicial reduction | Final outcome. Caption: "Documented awareness + documented decision not to act = punitive exposure. Scale varies. Pattern does not."
- Manim move: compare (two columns build side by side; the "internal document" row highlights red in both; punitive-damage bars appear at the bottom showing the magnitude of judicial exposure)
- Example seed: A medical device company's quality engineers flag in a internal report that a catheter design may fail under specific pressure conditions. The engineering team estimates the redesign cost at $340,000. The legal team estimates expected product-liability claims at $280,000. Management approves the original design. Three years later, three patients are injured by catheter failures. Discovery in the resulting lawsuit turns up the quality report. The calculation memo. The approval email. The jury sees all three.
- Length band: 2–3 min
- Still lanes: raster (Ford Pinto image), c2v (two-case structural comparison table)
- Prerequisites: Basic awareness that companies can be sued for defective products; no prior legal background needed.
- Exclusions: Full negligence framework (covered in Card 03); comparative negligence; assumption of risk; Liebeck detail (use as one comparative entry only).
- Score: 8/10

---

## Candidate 13 — Why the SEC's Disclosure Framework Doesn't Actually Tell You If a Stock Is Good
- Source: `mba-business-law/chapters/14-securities-regulation.md`
- Topic: BUSINESS LAW
- Hook: The SEC does not tell you whether a stock is a good investment. It does not approve or certify securities. A company can offer terrible securities to the public — as long as the prospectus accurately describes how terrible they are. This is the entire design philosophy of U.S. securities regulation, and most investors don't know it.
- Key case: The 1929 crash and Congress's response — Securities Act of 1933 + Securities Exchange Act of 1934. Design philosophy: mandatory disclosure, not merit review.
- The Question: If securities regulation doesn't protect investors from bad investments, what does it protect them from — and why is that distinction the organizing principle of the entire regulatory framework?
- Core idea: The fundamental problem in capital markets is information asymmetry: the issuer knows everything about the business; the investor knows almost nothing. If investors can't distinguish honest representations from fraudulent ones, either honest issuers can't raise capital at fair prices or investors stop investing entirely. The regulatory response is not to evaluate investments but to require disclosure sufficient for an informed decision and impose liability on those who lie. Section 11's strict issuer liability and Rule 10b-5's anti-fraud provision are the enforcement teeth. The framework solves the information problem without the government substituting its judgment for the investor's.
- Visual object: A two-panel diagram — Left panel: "Merit Review" model (regulator stands between issuer and investor, approving or rejecting securities). Right panel: "Disclosure" model (regulator requires information flow directly from issuer to investor; investor makes the decision). A large X over the left panel, a checkmark over the right panel. Caption: "The SEC is not in the business of telling you what to buy."
- Manim move: split (single box labeled "Information" splits into two models — merit review vs. disclosure — with the left model crossed out)
- Example seed: In 1925, a promoter sells shares in a copper mine in Arizona. The prospectus says the mine has "proven reserves" of 50 million tons. It actually has 500,000 tons. Investors buy. The mine produces nothing. Under the pre-1933 framework: sue the promoter for fraud — good luck finding him. Under the 1933 Act: Section 11 imposes civil liability on the issuer, the underwriter, every director who signed the registration statement, and every expert who certified a specific statement. The underwriter who did not verify the reserve estimate cannot claim ignorance. The due-diligence defense requires actual investigation.
- Length band: 2–3 min
- Still lanes: c2v (merit-review vs. disclosure-model diagram), raster (1929 stock-market newspaper headline as texture)
- Prerequisites: Basic awareness that companies raise money by selling stock; no prior securities-law knowledge.
- Exclusions: Reg D exemptions (mention briefly); Sarbanes-Oxley detail; Dodd-Frank whistleblower program; crypto-asset classification.
- Score: 8/10

---

## Candidate 14 — How Section 7 of the NLRA Protected Two Employees Who Were Never in a Union
- Source: `mba-business-law/chapters/09-employment-and-labor-law.md`
- Topic: BUSINESS LAW
- Hook: Two employees complain together to HR about a supervisor's conduct. There is no union. No organizing drive. The company fires both of them. This is an unfair labor practice under federal law — and most employers don't know it.
- Key case: NLRA Section 7 "protected concerted activity" — applies to any joint employee action about working conditions, union or no union; plus the Triangle Shirtwaist fire as the chapter's founding narrative.
- The Question: If you have no union and no organizing drive, can employees still have federally protected rights to act collectively about their working conditions — and what does "concerted activity" actually cover?
- Core idea: Section 7 of the NLRA protects employees who act together "for mutual aid or protection" — a scope that extends well beyond union organizing. Two employees who discuss their salaries, three who complain to management about an unsafe condition, workers who post on social media about working conditions as a group — all can be engaged in protected concerted activity. An employer that fires or disciplines employees for these activities commits an unfair labor practice regardless of whether a union is involved. Most employers associate labor law with collective bargaining agreements and union campaigns; the Section 7 protection is invisible precisely because it operates in non-union workplaces where employers don't expect it.
- Visual object: A Venn diagram — Circle A: "Union Organizing" (familiar territory). Circle B: "Section 7 Protected Concerted Activity" (much larger circle, mostly outside Circle A). Annotated examples in the non-union zone: salary discussions, safety complaints, workplace social-media posts. Caption: "Most of Section 7 applies here — not here."
- Manim move: expand (small "union" circle grows into the much larger Section 7 circle; annotated examples appear in the expanded area)
- Example seed: A restaurant's kitchen staff — all non-union — have been told that discussing wages with coworkers violates company policy and will result in termination. Two line cooks ignore the policy and compare paychecks, discovering a $3/hour disparity with no clear explanation. They bring it to the manager together. The manager fires both. The National Labor Relations Board's response: the conversation was protected concerted activity. The company policy prohibiting wage discussions is itself an unfair labor practice. The firings are unlawful regardless of the at-will employment relationship.
- Length band: 2–3 min
- Still lanes: c2v (Venn diagram), raster (Triangle Shirtwaist fire historical image as opening texture)
- Prerequisites: Basic awareness that there is something called "labor law"; no union-organizing background needed.
- Exclusions: Full collective bargaining / union election process; Taft-Hartley right-to-work detail; FLSA wage-and-hour mechanics.
- Score: 8/10

---

*End of scouted candidates. 14 cards written; all score ≥ 8/10.*
