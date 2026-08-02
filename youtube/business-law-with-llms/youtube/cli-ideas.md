# Business Law with LLMs — CLI Video Ideas ("X with Claude")

## Candidate 01 — Research the Madoff Fraud with Claude: White-Collar Crime Template

- Source: business-law-with-llms/chapters/05-criminal-liability.md
- Lane: RESEARCH (Claude assistant)
- Hook: Four of the seven citations in the pharmaceutical report were fabricated. Six of the seven were wrong. The citations looked perfect — right author surnames, right journal format, right DOI structure. That's what makes hallucination dangerous: it's not a failure to produce text. It's a success at producing the wrong text.
- The artifact: A sourced two-column comparison of the Madoff scheme (~$65B) and the Koss Corporation embezzlement (~$34M) across the white-collar crime template: position of trust / mechanism of extraction / concealment method / duration before detection / how detected / criminal outcome / civil consequence. Each cell cites a checkable source.
- Prompt seed: `claude "Compare the Madoff Ponzi scheme and the Koss Corporation Sachdeva embezzlement using the white-collar crime template: position of trust, mechanism of extraction, concealment method, duration before detection, how detected, criminal sentence, civil consequence. For each cell, cite one verifiable source (court document, SEC action, or news archive)."`
- Read / check: Verify Madoff's 150-year sentence (entered March 2009) and Sachdeva's 11-year sentence are correct. Confirm the detection mechanism for each (American Express raised concerns for Sachdeva; Madoff's sons reported him). Output: the "how detected" row should show that both were caught by external review, not internal audit — making the pattern explicit.
- Human supplies: Nothing — fully synthetic research from documented public record.
- Output medium: d3 (animated) — two-column comparison table building row by row, detection row highlighted as the pattern anchor, source citations fading in as footnotes
- The change: Add a third column for a more recent white-collar case (the viewer looks up one from the last five years) — testing whether the template generalizes.
- Teardown angle: What distinguishes Madoff is the scale, not the mechanism. The mechanism is the template. Concealment within normal business activity, detection through external pressure, the same three elements recur in thousands of smaller cases every year.
- Exclusions: Skip the full RICO statutory analysis, or Madoff's recovery trustee proceedings detail.
- Score: 9/10

---

## Candidate 02 — Research Contract Formation with Claude: The Carlill Case and Its Descendants

- Source: business-law-with-llms/chapters/07-contract-law.md
- Lane: RESEARCH (Claude assistant)
- Hook: An advertisement promising £100 to anyone who used a smoke ball and caught flu. A woman used the smoke ball. She caught flu. She sued. The court held she had a contract — with the world. 130 years of contract law descends from one sick woman and a quack remedy.
- The artifact: A sourced contract-formation analysis chain: Carlill v. Carbolic Smoke Ball (1893) → the five modern formation elements (offer, acceptance, consideration, capacity, legality) → three contemporary cases where one element was disputed and how courts resolved it (e.g., ambiguous online terms-of-service as "offer," silence as "acceptance," social media promises as "consideration").
- Prompt seed: `claude "Build a contract formation analysis starting with Carlill v. Carbolic Smoke Ball Co. (1893). Explain the five formation elements the case illustrates. Then find three modern cases (post-2000) where one formation element was contested in a business context — ideally involving digital agreements or social media. For each: what element was disputed, how the court ruled, and what the ruling means for practitioners. Cite case names and jurisdictions."`
- Read / check: Verify the Carlill citation ([1893] 1 QB 256) is correct. Confirm at least one of the three modern cases is real and citable (look for recent contract cases involving clickwrap agreements or social media promises). Output: the three modern cases should cover three different elements (offer, acceptance, consideration) — not all the same element.
- Human supplies: Nothing — fully synthetic research. Viewer verifies modern cases against Westlaw, LexisNexis, or published court records.
- Output medium: d3 (animated) — timeline from 1893 to present, three modern cases branching from the Carlill anchor, formation element color-coded per branch
- The change: Apply the five-element checklist to a contract the viewer has drafted or received — asking Claude to identify which elements are clearly established and which could be contested.
- Teardown angle: Contract law is more carefully calibrated to commercial practice than the casual reader assumes. The Carlill case is taught not because smoke balls matter but because it resolves the unilateral offer question that every modern promotional offer faces.
- Exclusions: Skip the full UCC Article 2 treatment for sales of goods, or international contract law (CISG).
- Score: 9/10

---

## Candidate 03 — Research Antitrust Law with Claude: Leniency Program and Price-Fixing Detection

- Source: business-law-with-llms/chapters/11-antitrust-law.md
- Lane: RESEARCH (Claude assistant)
- Hook: The first member of a price-fixing conspiracy to report it receives full immunity from prosecution. This structural feature has been the primary source of cartel-enforcement cases for twenty years. The legal architecture that catches cartels depends on a race to the door.
- The artifact: A sourced explainer of the DOJ Antitrust Division leniency program: how it works (first-in wins immunity, others face up to $100M corporate fine and 10 years imprisonment), the economic mechanism that makes defection dominant (prisoner's dilemma), and three documented cartel cases where the leniency race produced the enforcement action (with dates, industries, penalties).
- Prompt seed: `claude "Explain the DOJ Antitrust Division leniency program for price-fixing. How does it work mechanically (who qualifies, what immunity covers, timing requirements)? Why does it produce enforcement actions — explain the prisoner's dilemma mechanism. Then cite three documented cartel cases (post-2000) where a leniency applicant triggered the prosecution: industry, co-conspirators, penalties imposed."`
- Read / check: Verify the Corporate Leniency Policy (1993, revised 2008) is accurately described. Confirm at least one of the three cartel cases is verifiable from DOJ.gov press releases. Output: the prisoner's dilemma explanation should show why cooperation is dominant even when the cartel is profitable — any member who delays risks being second and losing immunity.
- Human supplies: Nothing — fully synthetic research. DOJ press releases are publicly accessible for verification.
- Output medium: d3 (animated) — prisoner's dilemma payoff matrix building, then three-case timeline with enforcement actions marked
- The change: Ask Claude to identify the industries with the highest cartel prevalence historically (airlines, lysine, vitamins) and explain what structural features of those industries make price-fixing easier to sustain — connecting the leniency program to the industries it most often prosecutes.
- Teardown angle: The leniency program is the most elegant piece of antitrust architecture — it turns the cartel's internal trust problem into an enforcement tool. Every member knows the immunity race exists. That knowledge destabilizes the cartel from the inside.
- Exclusions: Skip the full Sherman Act §2 monopolization analysis, or merger review procedures.
- Score: 9/10

---

## Candidate 04 — Research the FCPA with Claude: What Makes Bribery Federal

- Source: business-law-with-llms/chapters/05-criminal-liability.md
- Lane: RESEARCH (Claude assistant)
- Hook: A payment to a foreign government official to win a contract. Legal in the country where it was paid. Illegal under US law — for US persons and US-listed companies anywhere in the world. The FCPA's jurisdictional reach is broader than most practitioners realize.
- The artifact: A sourced three-case FCPA enforcement analysis: BHP Billiton (2014), GlaxoSmithKline China (2014), Telia (2017, $965M). For each: what conduct was alleged, what jurisdictional basis made US law applicable, the enforcement outcome (DOJ/SEC split), and what compliance program deficiency the resolution agreement identified.
- Prompt seed: `claude "Analyze three FCPA enforcement cases: BHP Billiton (2014), GlaxoSmithKline China (2014), Telia (2017). For each: (1) conduct alleged, (2) FCPA jurisdictional basis (why was US law applicable?), (3) total monetary settlement amount split between DOJ and SEC, (4) compliance program failure the settlement identified. Cite DOJ.gov or SEC.gov press releases where available."`
- Read / check: Verify the Telia settlement amount ($965M total, split between DOJ/SEC and Dutch and Swedish authorities) is approximately correct. Confirm the GlaxoSmithKline China case involved payments to physicians (not government procurement). Output: the jurisdictional basis column should show three different hooks — use of US wires, US-listed securities, US subsidiary involvement.
- Human supplies: Nothing — fully synthetic research from DOJ/SEC public enforcement records.
- Output medium: slate (three-row enforcement table, jurisdictional basis highlighted, monetary settlement in bold, compliance lesson per case)
- The change: Ask Claude to describe what a minimally adequate FCPA compliance program looks like (DOJ's 2020 Evaluation of Corporate Compliance Programs guidance) — connecting the enforcement lessons to prevention.
- Teardown angle: The FCPA's jurisdictional reach is its most underestimated feature. "We operate in a country where this is normal" is not a defense under US law. The question is whether the company or its executives touched US wires, held US securities, or operated a US subsidiary.
- Exclusions: Skip the full Books and Records provisions, or OECD Anti-Bribery Convention comparison.
- Score: 8/10

---

## Candidate 05 — Research Employment Law with Claude: At-Will Exceptions Map

- Source: business-law-with-llms/chapters/09-employment-and-labor-law.md
- Lane: RESEARCH (Claude assistant)
- Hook: "At-will employment" means the employer can fire for any reason. Except the reasons that are illegal. There are more exceptions than most managers know — and more variation across states than any single federal rule captures.
- The artifact: A sourced map of at-will employment exceptions: federal statutory exceptions (Title VII, ADA, ADEA, NLRA), common law exceptions (implied contract, public policy, good faith/fair dealing — adopted in varying combinations by state), and whistleblower protection statutes (Dodd-Frank, OSHA, SOX). For each: which states recognize it, what the exception protects, and one illustrative case.
- Prompt seed: `claude "Map the exceptions to US at-will employment doctrine. Three categories: (1) federal statutory exceptions — list the major employment discrimination and labor statutes and what each prohibits. (2) common law exceptions — which three exceptions exist, which states recognize each, and one case per exception. (3) whistleblower statutes — Dodd-Frank, SOX, OSHA — what conduct each protects and what remedies are available. Cite one verifiable source per category."`
- Read / check: Verify that the implied contract exception is recognized in most states but not all (Montana is the only state with a just-cause statute). Confirm the public policy exception (firing for jury duty, voting, etc.) is nearly universal. Output: the three-category structure should show that a termination can be legal under at-will doctrine but still violate a specific statute or common law exception.
- Human supplies: Nothing — fully synthetic research. State-level recognition varies — viewer should verify their specific state law.
- Output medium: d3 (animated) — US map showing at-will states vs. exception-adopting states, three-layer exception structure building in sequence
- The change: Apply the exception map to a specific termination scenario (the viewer describes a firing situation) — asking Claude which exceptions might apply and what evidence would be relevant.
- Teardown angle: The "at-will" label is accurate but incomplete. The exceptions are not footnotes — they are the substance of employment law litigation. A manager who fires without knowing the exceptions has made a legal decision without legal knowledge.
- Exclusions: Skip collective bargaining agreements (a separate chapter), or the full NLRA Section 7 analysis.
- Score: 8/10

---

## Candidate 06 — Research Tort Law with Claude: Negligence Elements and the Learned Hand Formula

- Source: business-law-with-llms/chapters/06-the-tort-system.md
- Lane: RESEARCH (Claude assistant)
- Hook: The Learned Hand Formula says a company is negligent if the cost of preventing the harm (B) is less than the probability of harm (P) times the magnitude of the harm (L). B < PL → liable. This turns negligence law into economics — and reveals why some "accidents" were predictable business decisions.
- The artifact: A sourced explanation of the negligence elements (duty, breach, causation, damages) with the Learned Hand formula applied to three real cases: United States v. Carroll Towing (1947, the original), a product liability case, and a premises liability case. For each: what B, P, and L values the court implicitly used, and whether the formula's verdict matches the court's verdict.
- Prompt seed: `claude "Explain the Learned Hand negligence formula (B < PL) using US v. Carroll Towing (1947). Then apply it to two additional cases: one product liability and one premises liability (post-1970). For each: estimate what B (burden of precaution), P (probability of harm), and L (magnitude of loss) the court implicitly weighed, and whether the B < PL verdict matches the court's negligence finding. Cite all three cases."`
- Read / check: Verify Carroll Towing citation (159 F.2d 169, 2d Cir. 1947). Confirm the formula is correctly stated (B < PL → negligent). Output: at least one of the three cases should show the formula predicting the opposite of what the court found — illustrating the limits of the economic model.
- Human supplies: Nothing — fully synthetic research. All three cases are in public legal record.
- Output medium: d3 (animated) — three cases as data points on a B-vs-PL scatter plot, negligent/not-negligent dividing line, cases labeled
- The change: Apply the formula to a current news event (a product recall or workplace accident) — asking Claude what B, P, and L values would need to be true for the company to be liable.
- Teardown angle: The Learned Hand formula makes negligence legible as an economics problem. But it also reveals that "accident" is a choice — a company that did the B < PL calculation and decided not to invest in precaution has made a business decision, not suffered a misfortune.
- Exclusions: Skip strict liability, comparative fault, or products liability design defect vs. manufacturing defect distinctions in full.
- Score: 8/10

---

## Candidate 07 — Research Government Regulation with Claude: Cost-Benefit Analysis of a Real Rule

- Source: business-law-with-llms/chapters/10-government-regulation.md
- Lane: RESEARCH (Claude assistant)
- Hook: Every major federal regulation is required to pass a cost-benefit analysis before it takes effect — but the analysis is conducted by the agency proposing the rule. The watchdog evaluates its own watch. Understanding how the analysis works (and where it can be gamed) is basic regulatory literacy.
- The artifact: A sourced cost-benefit analysis of one real federal regulation (the OSHA Silica Rule (2016) or the EPA Clean Power Plan (2015)): what the rule requires, the agency's stated cost estimate, the agency's stated benefit estimate, what industry challenged in the analysis, and what the OMB review found. Includes the OIRA review timeline.
- Prompt seed: `claude "Analyze the cost-benefit analysis for OSHA's 2016 crystalline silica rule. What are the rule's requirements? What cost did OSHA estimate? What benefits (lives saved, illnesses prevented) did they claim? What did industry challengers argue about the analysis? What did the OMB's OIRA review conclude? Cite OSHA's regulatory impact analysis and any published academic critiques."`
- Read / check: Verify OSHA's silica rule was finalized in 2016. Confirm the OIRA review process exists and is publicly documented (regulations.gov or oira.gov). Output: the industry challenge section should identify at least one methodological objection (e.g., discount rate used for future lives saved, or wage-risk premium studies used to value a statistical life).
- Human supplies: Nothing — fully synthetic research. OSHA regulatory impact analysis documents are publicly available.
- Output medium: screen-recording mp4 (terminal: rule description in, cost/benefit breakdown out, methodological challenge section highlighted)
- The change: Compare the silica rule's cost-benefit analysis to a recent proposed regulation the viewer cares about — applying the same analytical framework to a current case.
- Teardown angle: The cost-benefit analysis is not a neutral accounting exercise — the choice of discount rate, value of a statistical life, and what counts as a benefit are all contested choices that determine the outcome before the math starts.
- Exclusions: Skip the Chevron deference doctrine (now overruled), or full administrative law procedure (notice-and-comment rulemaking).
- Score: 8/10

---

## Candidate 08 — Research Securities Regulation with Claude: Rule 10b-5 and Insider Trading

- Source: business-law-with-llms/chapters/14-securities-regulation.md
- Lane: RESEARCH (Claude assistant)
- Hook: The Equifax executives sold $2M of stock after being briefed on the breach. They sold before the public was told. Rule 10b-5 is the single legal provision under which almost all insider trading cases are prosecuted — and it was written in 1942 in fifteen minutes because the SEC needed to stop a specific fraud.
- The artifact: A sourced analysis of Rule 10b-5 (Securities Exchange Act §10(b)): the rule's text, its elements (material nonpublic information / breach of duty / scienter), the tipper-tippee liability extension (Dirks v. SEC, 1983), and three recent enforcement actions (SEC.gov press releases) showing how the rule is applied in practice.
- Prompt seed: `claude "Analyze SEC Rule 10b-5 (17 CFR 240.10b-5). State the rule's text. Identify the three elements courts require for insider trading liability (material nonpublic information, duty, scienter). Explain the tipper-tippee doctrine from Dirks v. SEC (1983). Then cite three recent SEC insider trading enforcement actions (2020–2025) from SEC.gov showing each element being applied. Include civil penalty amounts."`
- Read / check: Verify the Dirks citation (463 US 646, 1983). Confirm the rule text is accurately quoted. Output: the three enforcement actions should each show a different fact pattern (direct insider, tippee, misappropriation theory) — demonstrating the rule's reach across relationship types.
- Human supplies: Nothing — fully synthetic research from SEC.gov public enforcement database.
- Output medium: d3 (animated) — three-element checklist building, then three case cards showing which element was contested in each
- The change: Apply the Rule 10b-5 elements to the Equifax case from Chapter 1 of the ethics book — asking whether the executives' sales satisfied all three elements or whether there was a colorable defense on any element.
- Teardown angle: Rule 10b-5 was written in fifteen minutes. It has been litigated for eighty years. The fact that a rule written quickly can carry that much interpretive weight is itself a lesson about how much legal doctrine lives in judicial elaboration of statutory text.
- Exclusions: Skip the full Exchange Act Sections 16 and 17, short-selling regulation, or market manipulation provisions.
- Score: 9/10

---

## Candidate 09 — Research Dispute Resolution with Claude: When to Arbitrate, When to Litigate

- Source: business-law-with-llms/chapters/02-disputes-and-dispute-settlement.md
- Lane: RESEARCH (Claude assistant)
- Hook: Most commercial contracts today include a mandatory arbitration clause. Most employees who sign them don't know what they've waived. Whether arbitration is better or worse than litigation depends on who you're asking — and what you're fighting about.
- The artifact: A structured comparison of litigation vs. arbitration vs. mediation across five decision factors: cost, speed, privacy, discovery rights, appeal rights. For each: what the default is, which party tends to benefit, and one documented case where the choice of forum changed the outcome.
- Prompt seed: `claude "Compare three dispute resolution mechanisms: litigation, binding arbitration, and mediation. For each of five factors — cost (average total legal spend), speed (average time to resolution), privacy (public record vs. confidential), discovery (scope of pre-hearing information exchange), appeal rights (grounds and process) — state the default, which party typically benefits, and cite one case where the forum choice changed the outcome. Ground with verifiable sources."`
- Read / check: Verify the Federal Arbitration Act (9 U.S.C. §§ 1-16) is correctly cited as the governing federal statute for arbitration enforceability. Confirm at least one of the three "forum mattered" cases is a real, citable case. Output: the discovery row should show that arbitration has significantly narrower discovery rights than litigation — a key advantage for the party with fewer documents.
- Human supplies: Nothing — fully synthetic research. For NEXT STEPS, viewer reviews the arbitration clause in their own employment or commercial contract.
- Output medium: d3 (animated) — five-factor comparison table, benefit-direction arrows (plaintiff-favoring vs. defendant-favoring), case cards per factor
- The change: Ask Claude to draft a two-paragraph analysis of a specific contract arbitration clause the viewer provides — identifying what rights it waives and what protections it preserves.
- Teardown angle: The arbitration clause is not a neutral choice between equivalent forums. It is a structural decision that determines what evidence is available, who pays, and whether an appeal is possible. The party that drafted the clause chose the forum they prefer.
- Exclusions: Skip international arbitration (ICSID, ICC), or class action arbitration waiver Supreme Court cases in detail.
- Score: 8/10

---

## Candidate 10 — Research the Constitutional Business Framework with Claude: Commerce Clause Scope

- Source: business-law-with-llms/chapters/04-business-and-the-united-states-constitution.md
- Lane: RESEARCH (Claude assistant)
- Hook: Congress can regulate anything that "affects interstate commerce." The Supreme Court has interpreted this to include a farmer growing wheat for his own consumption. Understanding where the Commerce Clause ends — and it does end — determines what federal business regulation is even legally possible.
- The artifact: A sourced Commerce Clause scope analysis: the four landmark cases that define the outer boundary (Wickard v. Filburn 1942, Heart of Atlanta Motel 1964, Lopez 1995, Morrison 2000), the test each case established or modified, and where the current boundary sits. Includes the Affordable Care Act Commerce Clause challenge (NFIB v. Sebelius 2012) as the most recent limit-setting case.
- Prompt seed: `claude "Trace the Commerce Clause scope through five Supreme Court cases: Wickard v. Filburn (1942), Heart of Atlanta Motel v. US (1964), US v. Lopez (1995), US v. Morrison (2000), NFIB v. Sebelius (2012). For each: what activity was regulated, how did the court rule, and what test or principle did the ruling establish or modify? Show how the outer boundary of Commerce Clause authority has moved. Cite full case citations."`
- Read / check: Verify all five citations (Wickard: 317 US 111; Heart of Atlanta: 379 US 241; Lopez: 514 US 549; Morrison: 529 US 598; NFIB: 567 US 519). Output: the sequence should show expansion through 1964, contraction in 1995-2000, and then the individual mandate question in 2012 as a new category (activity vs. inactivity).
- Human supplies: Nothing — fully synthetic research. All five cases are publicly reported Supreme Court decisions.
- Output medium: d3 (animated) — horizontal timeline of five cases, Commerce Clause "scope" bar expanding and contracting, activity/inactivity distinction highlighted at the NFIB node
- The change: Apply the Commerce Clause test to a hypothetical federal regulation the viewer proposes — asking Claude whether it would survive the Lopez/Morrison activity test or require the Wickard "substantial effects" argument.
- Teardown angle: The Commerce Clause question is not whether Congress intended to regulate something — it is whether the Constitution permits it. Most federal business regulation passes easily. The cases where it fails reveal the structure underneath the statute.
- Exclusions: Skip Dormant Commerce Clause (state regulations burdening interstate commerce), or the full Spending Clause analysis.
- Score: 8/10

---

## Candidate 11 — Build a Contract Red-Flag Detector with Claude

- Source: business-law-with-llms/chapters/07-contract-law.md + chapters/08-sales-contracts.md
- Lane: RESEARCH (Claude assistant)
- Hook: The contract that "just needs a quick look" has twelve provisions that shift risk, cap liability, waive jury trial, and strip the right to appeal. Spotting them takes legal training. Structuring the review takes a checklist. Building the checklist takes thirty minutes with Claude.
- The artifact: A Python CLI script that takes a contract text as input and prompts Claude to identify and categorize clauses by risk level: (1) standard provisions (flagged green), (2) notable provisions that shift risk (flagged yellow with explanation), (3) high-risk provisions requiring lawyer review (flagged red — e.g., broad indemnification, IP assignment, non-compete, arbitration with class waiver, limitation of liability caps below actual damages). Output is a prioritized review list.
- Prompt seed: `claude "Review this contract text. Categorize each material clause: GREEN = standard and expected, YELLOW = notable risk-shifting provision (explain what risk is shifted and to whom), RED = requires lawyer review (broad indemnification, IP assignment beyond project scope, non-compete, mandatory arbitration with class waiver, limitation of liability). Output as a prioritized list with one-sentence explanations. Note: this is preliminary review, not legal advice."`
- Read / check: Verify the script correctly identifies at least one RED-category clause in a test contract containing a broad indemnification clause. Confirm the "not legal advice" disclaimer appears in the output. Output: a standard SaaS subscription agreement should generate more GREEN than RED; a commercial IP development agreement should generate more RED flags.
- Human supplies: A contract text to review (the human must supply this). The video uses a synthetic commercial services agreement with deliberate red flags embedded.
- Output medium: screen-recording mp4 (terminal: contract text in, risk-categorized clause list out, RED flags highlighted)
- The change: Ask Claude to draft a counter-proposal for one RED-flagged clause — converting the review into a negotiation starting point.
- Teardown angle: The script is not a lawyer. It is a first-pass filter that makes the lawyer's time more efficient by surfacing what to look at first. The value is not in replacing legal review — it is in making the human's attention go to the provisions that matter.
- Exclusions: Skip UCC Article 2 specific sales provisions, or jurisdiction-specific enforceability analysis.
- Score: 9/10

---

## Candidate 12 — Research the AT&T Antitrust Case with Claude: Structure vs. Conduct Remedies

- Source: business-law-with-llms/chapters/11-antitrust-law.md
- Lane: RESEARCH (Claude assistant)
- Hook: The government broke up AT&T in 1984. By 2005, the Baby Bells had re-merged into two companies that together controlled most of the US telecommunications market. Structure remedies don't stay fixed. The question of whether to break up a monopoly or regulate its conduct is still being answered.
- The artifact: A sourced comparative analysis of structure vs. conduct remedies in three antitrust cases: AT&T breakup (1984), Microsoft consent decree (2001), and Google (ongoing as of 2025). For each: what the government alleged, what remedy was sought, what remedy was ordered, and whether the remedy achieved its objective (with evidence).
- Prompt seed: `claude "Compare antitrust remedies in three cases: AT&T breakup (United States v. AT&T, consent decree 1982/effective 1984), Microsoft (United States v. Microsoft, 2001 consent decree), and the current Google search antitrust case (DOJ v. Google, status as of 2025). For each: (1) government's core allegation, (2) remedy sought, (3) remedy ordered, (4) evidence of whether it worked. Cite case names and DOJ press releases or court opinions."`
- Read / check: Verify the AT&T divestiture date (1984, not 1982). Confirm the Microsoft consent decree outcome (behavioral restrictions, not breakup). Output: the "did it work" column for AT&T should note the re-consolidation into AT&T Inc. and SBC by 2005; Microsoft's should note the browser market evolution and the rise of Google during the consent decree period.
- Human supplies: Nothing — fully synthetic research from public legal record. The Google case status may require the viewer to check for developments after Claude's knowledge cutoff.
- Output medium: d3 (animated) — three-case timeline, structure/conduct remedy icons, "worked / partially / not" outcome indicators
- The change: Ask Claude whether the Google remedy (if ordered) is more likely to be effective than the AT&T or Microsoft remedies — using the historical evidence to evaluate the competing remedy theories.
- Teardown angle: The breakup of AT&T took twenty years of market pressure to undo. The government got the remedy it wanted and watched the market reverse it. Structure remedies are not permanent — markets adapt. The conduct vs. structure debate is ultimately a question about which adapts faster.
- Exclusions: Skip the full Sherman Act §2 monopolization legal standard, or EU competition law comparison.
- Score: 8/10

---

## Candidate 13 — Research Unfair Trade Practices with Claude: FTC Enforcement Pattern

- Source: business-law-with-llms/chapters/12-unfair-trade-practices-and-the-federal-trade-commission.md
- Lane: RESEARCH (Claude assistant)
- Hook: The FTC Act prohibits "unfair or deceptive acts or practices" — five words that have generated a century of enforcement and still have no fully settled definition. The FTC enforces it through a pattern of consent orders that tell companies what not to do without ever finishing the definition of what the law requires.
- The artifact: A sourced analysis of three recent FTC enforcement actions in different areas (data privacy, subscription cancellation, AI endorsements or deceptive AI claims) showing what conduct the FTC treated as "unfair or deceptive," what the consent order required, and what the underlying legal theory was (deception vs. unfairness — different tests).
- Prompt seed: `claude "Analyze three recent FTC enforcement actions (2020–2025) involving different theories: (1) one deception case (false claims about a product), (2) one unfairness case (harm to consumers without deception), (3) one emerging-technology case (AI, algorithmic bias, or data privacy). For each: what conduct was alleged, was the theory deception or unfairness (and why does it matter?), what did the consent order require, and what civil penalty was imposed? Cite FTC.gov press releases."`
- Read / check: Verify the deception vs. unfairness distinction (deception = likely to mislead a reasonable consumer; unfairness = causes or is likely to cause substantial injury, not outweighed by benefits). Confirm at least one case cites an FTC.gov press release URL. Output: the three cases should illustrate that the deception and unfairness theories have different elements — a case that fails the deception test might still be unfair.
- Human supplies: Nothing — fully synthetic research from FTC.gov enforcement database.
- Output medium: screen-recording mp4 (terminal: three cases researched, deception/unfairness label assigned per case, consent order terms listed)
- The change: Ask Claude to evaluate a current business practice the viewer describes — applying the deception and unfairness tests and stating which (if either) applies.
- Teardown angle: The FTC's power comes from the consent order model — companies agree to restraints without admitting liability, which means the legal standard is never fully tested. The enforcement pattern is more important than any single case definition.
- Exclusions: Skip Magnuson-Moss Warranty Act, or FTC merger review (Hart-Scott-Rodino) in detail.
- Score: 8/10
