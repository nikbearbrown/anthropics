# Business Ethics with LLMs — CLI Video Ideas ("X with Claude")

## Candidate 01 — Research the Equifax Insider Trading Case with Claude

- Source: business-ethics-with-llms/chapters/01-why-ethics-matter.md
- Lane: RESEARCH (Claude assistant)
- Hook: Legal and ethical are two different axes. The executives sold before the public was told — and nothing technically prohibited it at the moment they clicked sell. The whole field of business ethics lives in the gap between those two columns.
- The artifact: A sourced 4-panel comparison table: the Equifax timeline (breach → internal briefing → stock sales → public disclosure) mapped against three frameworks (consequentialist verdict / deontological verdict / virtue ethics verdict), plus the SEC enforcement outcome and its legal basis. Each cell cites a checkable source.
- Prompt seed: `claude "Research the 2017 Equifax data breach insider trading case. Build a sourced timeline (breach date, internal briefing, executive stock sales, public disclosure, SEC action). Then apply three ethical frameworks: (1) consequentialist — who was harmed, how much? (2) deontological — what duties were violated? (3) virtue ethics — what kind of person makes this decision? Cite verifiable sources for each cell."`
- Read / check: Verify the timeline dates (breach May 2017, public disclosure September 7) against news sources. Confirm the SEC enforcement action exists (check SEC.gov enforcement releases). Output: the deontological column should identify fiduciary duty to shareholders as the violated duty; the consequentialist column should quantify the ~14% share price drop and estimated retail investor losses.
- Human supplies: Nothing — fully synthetic research. Claude searches its knowledge + viewer verifies against SEC.gov and public news archives. Sources should be checkable: company name, date, publication, URL when possible.
- Output medium: d3 (animated) — the four-column table building left to right, framework verdicts appearing in sequence, sources animating in as footnotes
- The change: Add a fourth column: the legal outcome. Ask Claude whether the legal outcome matched the ethical verdict under each framework — and where it didn't, why.
- Teardown angle: The Equifax case is not about incompetence or accident — it is about the legal/ethical gap that exists in every corporation every day. The law set the floor. Three executives chose to stand on it.
- Exclusions: Skip the broader Equifax data security failure, GDPR implications, or the congressional testimony in detail.
- Score: 9/10

---

## Candidate 02 — Map Stakeholders with Claude: The Starbucks Philadelphia Case

- Source: business-ethics-with-llms/chapters/03-defining-and-prioritizing-stakeholders.md
- Lane: RESEARCH (Claude assistant)
- Hook: Two people were arrested. Starbucks closed eight thousand stores. The response was orders of magnitude larger than the incident would seem to require — unless you understand who all the stakeholders were and what tier of awareness each reached.
- The artifact: A two-axis stakeholder map (Freeman taxonomy: enabling/normative/functional/diffused × Grunig-Hunt awareness: nonpublic/latent/aware/active) populated with the Starbucks Philadelphia stakeholders at the moment of the video's release (April 12, 2018). Sixteen cells, each with real named groups. The "diffused/active" cell shows how it grew from one bystander to 10M viewers in 24 hours.
- Prompt seed: `claude "Build a stakeholder map for Starbucks on April 12, 2018 — the day of the Nelson/Robinson arrest. Classify stakeholders using Freeman's taxonomy (enabling/normative/functional/diffused) AND Grunig-Hunt awareness (nonpublic/latent/aware/active). Populate all 16 cells with named groups. Show how the diffused/nonpublic cell became diffused/active within 24 hours. Cite the source of the 10M views figure."`
- Read / check: Verify the 10M views figure against a published news source (cite the article). Confirm the enabling stakeholders include the Starbucks board and institutional investors. Output: the diffused/active cell at T+24h should be larger than any other cell and include organized boycott callers and journalists.
- Human supplies: Nothing — fully synthetic research from Claude's knowledge of the documented case. For NEXT STEPS, the viewer applies the map to a company of their choice.
- Output medium: d3 (animated) — 4×4 grid building cell by cell, diffused row lighting up in sequence as time progresses, arrow showing the nonpublic → active transition
- The change: Fast-forward to T+6 weeks (May 29, store closure day) and show how the map has changed — which cells grew, which shrank, which new groups appeared.
- Teardown angle: The manager who called 911 wasn't thinking about diffused stakeholders becoming active publics in an afternoon. Stakeholder analysis is, in part, the discipline of thinking about that before you need to.
- Exclusions: Skip the racial-bias training content, the open-door policy change details, or post-settlement recidivism data.
- Score: 9/10

---

## Candidate 03 — Research What Employers Owe Employees: Ford Chicago Assembly Case

- Source: business-ethics-with-llms/chapters/06-what-employers-owe-employees.md
- Lane: RESEARCH (Claude assistant)
- Hook: Two settlements. Twenty-five years apart. Thirty million dollars. One of the plaintiffs says in retrospect: if I had that choice today, I wouldn't say a damn word. The law produced money and consent decrees. It did not change the operative culture of the assembly line.
- The artifact: A sourced three-tier analysis of the Ford Chicago case: (1) the legal floor — what Title VII of the Civil Rights Act and the EEOC framework required and produced; (2) the ethical space above — what an employer with genuine organizational integrity would have done between 1997 and 2014; (3) the gap — why $30M in settlements left the culture unchanged, with cross-reference to organizational culture research on consent-decree effectiveness.
- Prompt seed: `claude "Research the Ford Chicago assembly plant sexual harassment settlements (1999, 2014). For each settlement: amount, EEOC findings, consent decree terms. Then analyze: (1) what did the legal floor require? (2) what does virtue ethics say an employer of integrity would have done differently? (3) why did two settlements over 17 years not change the culture? Cite verifiable sources."`
- Read / check: Verify the 1999 settlement amount (~$22M) and the 2014 settlement amount (~$10M) against EEOC press releases (eeoc.gov). Confirm the New York Times article featuring Sharon Dunn is citable. Output: the "why settlements failed" section should cite at least one organizational behavior or compliance research finding on consent decree effectiveness.
- Human supplies: Nothing — fully synthetic research. Viewer verifies against EEOC.gov settlement database and news archives.
- Output medium: slate (timeline with three settlement events + policy changes, annotated with gap analysis text below each)
- The change: Compare the Ford case to a counterexample (a company that changed culture after one incident without requiring a second settlement) — making the structural argument about what the first settlement missed.
- Teardown angle: The question is not what the law requires — the law is just the floor. The question is what the floor leaves out, and what an employer is actually obligated to provide in the space above it.
- Exclusions: Skip federal employment law beyond Title VII, or global jurisdictional comparisons.
- Score: 8/10

---

## Candidate 04 — Apply the Three Ethical Lenses with Claude: Any Real Business Case

- Source: business-ethics-with-llms/chapters/01-why-ethics-matter.md + chapters/02-ethics-from-antiquity-to-the-present.md
- Lane: RESEARCH (Claude assistant)
- Hook: Consequentialism, deontology, virtue ethics — three different angles on the same decision. Each sees something the others miss. The cashier who gives the employee discount to her cousin needs all three verdicts before she knows what her own standard requires.
- The artifact: A structured three-lens analysis of any supplied business dilemma — a real case study format. Consequentialist verdict (who benefits, who is harmed, probability-weighted), deontological verdict (which duties are owed, which are violated), virtue ethics verdict (what kind of person/company does this make me over time). Each verdict is one paragraph, each cites the theoretical basis.
- Prompt seed: `claude "Apply three ethical frameworks to this business dilemma: [user supplies case]. Consequentialist verdict: identify all stakeholders, quantify harms and benefits, state the net utilitarian assessment. Deontological verdict: identify the duties owed to each party, state which are honored and which violated. Virtue ethics verdict: what character traits does this decision reinforce over time? Format as three labeled sections, each ≤ 150 words."`
- Read / check: Verify the consequentialist section identifies all named stakeholders (not "society in general"). Confirm the deontological section names a specific duty (fiduciary, contractual, professional code). Output: the three verdicts should not all agree — a good case produces at least one cross-framework tension.
- Human supplies: A business dilemma to analyze (from the chapter exercises, news, or the viewer's own professional context). The video uses the Equifax case as the demo dilemma; viewer substitutes their own for the CHANGE beat.
- Output medium: screen-recording mp4 (terminal: dilemma in, three-section analysis out, framework labels highlighted)
- The change: Add a fourth section: "Where the frameworks disagree and why" — forcing Claude to identify the cross-framework tension and explain what additional information would resolve it.
- Teardown angle: The three frameworks are not alternatives to choose between — they are complementary lenses. A decision that survives all three is robust. A decision that passes one and fails two reveals its moral structure.
- Exclusions: Skip the full history of each framework (Kant's categorical imperative proof, Mill's utility calculus), or applied theology.
- Score: 9/10

---

## Candidate 05 — Research Professions Under the Microscope: Code of Ethics Comparison

- Source: business-ethics-with-llms/chapters/09-professions-under-the-microscope.md
- Lane: RESEARCH (Claude assistant)
- Hook: Medicine, law, accounting, engineering — each has a professional code. But the codes were written at different times, for different threats, by people with different ideas about what the profession owes the public. How much do they actually agree?
- The artifact: A sourced comparison table of four professional ethics codes (AMA medical ethics, ABA model rules of professional conduct, AICPA code, NSPE engineering ethics) across five dimensions: (1) loyalty hierarchy (client vs. public vs. profession), (2) confidentiality exceptions, (3) conflict of interest rules, (4) whistleblower obligations, (5) self-regulation vs. external enforcement. Each cell cites the specific code provision.
- Prompt seed: `claude "Compare professional ethics codes across four fields: medicine (AMA), law (ABA Model Rules), accounting (AICPA), engineering (NSPE). For each, find the specific provision governing: (1) where client loyalty ends and public duty begins, (2) confidentiality exceptions, (3) conflict of interest disclosure, (4) when reporting wrongdoing is required vs. permitted. Build a 4×4 table with code citations (e.g., ABA Rule 1.6(b)(1))."`
- Read / check: Verify at least two specific code citations are real and checkable (ABA Rule 1.6 governs confidentiality — verifiable at americanbar.org; NSPE Section III.2 governs public safety — verifiable at nspe.org). Output: the loyalty hierarchy row should show medicine and engineering prioritizing public safety over client, while law prioritizes client confidentiality with narrower exceptions.
- Human supplies: Nothing — fully synthetic research. Viewer verifies against the actual code documents (all publicly available).
- Output medium: d3 (animated) — comparison table building column by column, disagreement cells highlighted in red, agreement cells in green
- The change: Add a fifth column for AI/tech ethics codes (e.g., ACM code of ethics) and ask Claude where they agree and disagree with the four established professions — especially on the question of public vs. client loyalty.
- Teardown angle: The codes were not written to agree with each other. Each profession defined its obligations in response to its own specific failure modes. Where the codes diverge reveals what each profession learned the hard way.
- Exclusions: Skip full text of any single code, international law practice differences, or disciplinary procedures.
- Score: 8/10

---

## Candidate 06 — Analyze the Culture-Time Shift in Business Ethics with Claude

- Source: business-ethics-with-llms/chapters/05-the-impact-of-culture-and-time-on-business-ethics.md
- Lane: RESEARCH (Claude assistant)
- Hook: Advertising cigarettes to children was legal and accepted. Insider trading was legal until 1934 (and not fully criminalized until 1988). What counts as ethical changes with time — and understanding the mechanism of that change is the only way to anticipate where the next shift is happening.
- The artifact: A sourced timeline of four historical ethical shifts in business practice: (1) child labor regulation, (2) insider trading prohibition, (3) environmental liability, (4) data privacy. For each: when the practice was accepted vs. prohibited, what triggered the shift (legislation, court ruling, scandal, or norm change), and what the leading indicators of the coming shift looked like before the law changed.
- Prompt seed: `claude "Build a sourced timeline of four business ethics shifts: child labor, insider trading, environmental liability, and data privacy. For each: (1) approximate date when the practice became legally/socially unacceptable, (2) what triggered the shift, (3) what leading indicators were present 10 years before the shift that a thoughtful observer could have seen. Cite a verifiable source per shift."`
- Read / check: Verify the insider trading timeline (Securities Act 1934, Insider Trading Sanctions Act 1984, Insider Trading and Securities Fraud Enforcement Act 1988) against SEC historical records. Confirm child labor regulation (Fair Labor Standards Act 1938) is correctly dated. Output: the "leading indicators" column should include at least one muckraking journalism example for child labor and one consumer privacy campaign for data.
- Human supplies: Nothing — fully synthetic research. Viewer verifies against accessible legal/historical sources.
- Output medium: d3 (animated) — horizontal timeline, four color-coded tracks, shift events marked, leading-indicator annotations appearing before each shift marker
- The change: Ask Claude to identify one current business practice that has the same leading-indicator profile as the four historical cases — where the law hasn't caught up to the emerging ethical consensus.
- Teardown angle: The pattern is consistent: the ethical consensus shifts before the law does, always. The practitioner who waits for the law has already made the decision that will define their reputation when the law arrives.
- Exclusions: Skip comparative international legal regimes, or the academic debate about moral progress.
- Score: 8/10

---

## Candidate 07 — Research the Charity vs. Justice Boundary with Claude

- Source: business-ethics-with-llms/chapters/08-recognizing-and-respecting-the-rights-of-all.md
- Lane: RESEARCH (Claude assistant)
- Hook: Is a living wage charity or justice? The distinction is not semantic — it determines whether the obligation is voluntary (CSR) or mandatory (rights-based). Business ethics gets stuck because it conflates the two.
- The artifact: A structured 3-case analysis distinguishing charity (voluntary enhancement of welfare) from justice (mandatory respect for rights) across three real company policies: (1) a company that pays above minimum wage (Amazon's $15/hr floor), (2) a company that voluntarily provides parental leave beyond the legal requirement, (3) a company that refuses to sell user data to third parties without consent. For each: is this charity or justice? What makes the answer non-obvious?
- Prompt seed: `claude "For each of these three company policies, argue both sides: is this a voluntary act of charity or a mandatory requirement of justice? (1) Amazon's $15/hr minimum wage in the US (above federal minimum), (2) paid parental leave beyond FMLA requirements, (3) opt-in consent for user data sharing. Use the rights-based framework: if a stakeholder has a legitimate claim that can be demanded, not merely requested, it is justice. If it is aspirational, it is charity."`
- Read / check: Verify the rights-based framework distinction (a right is a claim that can be demanded, not merely hoped for — see Feinberg's rights-as-claims theory). Confirm the Amazon $15/hr wage history is accurately described. Output: the three cases should produce different verdicts — at least one charity, one justice, one genuinely contested.
- Human supplies: Nothing — fully synthetic research. For NEXT STEPS, viewer applies the framework to a policy from their own organization.
- Output medium: screen-recording mp4 (terminal: three cases in, verdicts and arguments out, charity/justice labels color-coded)
- The change: Add a fourth case that the viewer proposes — applying the charity/justice distinction to something from their own professional context.
- Teardown angle: The business ethics conversation gets stuck because both sides are right about different things. Companies that call everything charity are right that some of it is voluntary. Critics who call everything justice are right that some of it is mandatory. The framework distinguishes which is which.
- Exclusions: Skip the full philosophical literature on rights theory, or international comparative labor law.
- Score: 8/10

---

## Candidate 08 — Research Stakeholder Priority with Claude: The Mitchell-Hastings Framework

- Source: business-ethics-with-llms/chapters/03-defining-and-prioritizing-stakeholders.md
- Lane: RESEARCH (Claude assistant)
- Hook: Freeman's stakeholder theory tells you who matters. It doesn't tell you who matters most when their claims conflict. The Mitchell-Hastings framework (power, legitimacy, urgency) is the tiebreaker — and it produces counterintuitive rankings.
- The artifact: A worked example of Mitchell-Hastings stakeholder salience scoring applied to a real business decision (a pharmaceutical company's decision on drug pricing). Seven stakeholder groups scored on three dimensions (power 1–3, legitimacy 1–3, urgency 1–3), with salience (sum) determining priority. The output shows which stakeholder the framework says to prioritize — and whether that matches the company's stated CSR commitments.
- Prompt seed: `claude "Apply the Mitchell-Hastings salience model (power, legitimacy, urgency, each 1–3) to the following stakeholder groups in a pharmaceutical company's drug-pricing decision: patients, insurers, shareholders, FDA, generic competitors, patient advocacy groups, physicians. Score each dimension with a one-sentence rationale. Rank by total salience score. Then compare: does the highest-salience stakeholder match the company's stated mission?"`
- Read / check: Verify that the Mitchell-Hastings model is correctly attributed (Mitchell, Agle, Wood 1997, Academy of Management Review). Confirm the seven stakeholders are all plausible for this decision context. Output: patients should score high on urgency and legitimacy but potentially low on power; shareholders should score high on power. The ranking should be non-obvious.
- Human supplies: Nothing — fully synthetic. For NEXT STEPS, viewer applies the scoring to a decision in their own organization.
- Output medium: d3 (animated) — radar chart per stakeholder (three axes: power/legitimacy/urgency), then a ranked bar chart of salience scores, then a comparison to stated mission.
- The change: Re-score the same stakeholders for a different company decision (e.g., data breach disclosure timing) and show how the salience ranking changes — demonstrating that priority is decision-specific, not company-level.
- Teardown angle: The point of the salience model is to surface whose claim is most pressing at this moment, for this decision. A company that answers the question generically ("we always prioritize customers") is not doing stakeholder analysis — it is doing public relations.
- Exclusions: Skip the full Mitchell-Hastings paper derivation, or evolutionary stakeholder theory.
- Score: 8/10

---

## Candidate 09 — Build an Ethics Audit Checklist with Claude for Any Business Decision

- Source: business-ethics-with-llms/chapters/01-why-ethics-matter.md + chapters/04-three-special-stakeholders-society-the-environment-and-government.md
- Lane: RESEARCH (Claude assistant)
- Hook: The cashier's decision to give the discount took three seconds and cost $25. She didn't run a checklist. She also didn't think about the six adjacent decisions it implied for how she'd treat the next customer who asked for a discount. Checklists are how the three-second decision gets the analysis it deserves.
- The artifact: A Python CLI script that prompts Claude with any business decision description and produces a structured ethics audit: stakeholder list (who is affected), legal floor check (is it legal?), three-lens analysis (consequentialist/deontological/virtue), newspaper test (would you be comfortable if reported?), and a recommended action with confidence score.
- Prompt seed: `claude "Run an ethics audit on this business decision: [user supplies decision]. Output: (1) stakeholder list with roles, (2) legal floor assessment, (3) consequentialist verdict, (4) deontological verdict, (5) virtue ethics verdict, (6) newspaper test: would this appear as wrongdoing in a front-page story? (7) recommended action with confidence 1–5. Format as a structured report."`
- Read / check: Verify all seven sections appear in the output. Confirm the newspaper test is framed correctly (both the "wrongdoing" test and the "too cautious" test — failing either is a flag). Output: when run on a clear-cut case (price-gouging during a hurricane), the confidence should be high (4–5) and the verdict should be consistent across all three frameworks.
- Human supplies: A business decision to audit (the viewer supplies this). The video demo uses the Equifax insider trading decision.
- Output medium: screen-recording mp4 (terminal: decision in, full audit report out, sections labeled and colored by verdict)
- The change: Run the same checklist on a genuinely contested decision (a company decision where reasonable people disagree) and show that the checklist surfaces the disagreement without resolving it — which is the correct output for genuinely contested cases.
- Teardown angle: The audit doesn't make decisions. It makes the ethical structure of a decision visible. A decision that passes all seven checks isn't guaranteed to be right — but a decision that fails three of them has a structural problem that deserves attention before action.
- Exclusions: Skip formal ethics committee procedures, Sarbanes-Oxley reporting requirements, or ESG scoring frameworks.
- Score: 9/10

---

## Candidate 10 — Research the Whistleblower Dilemma with Claude: Employee Loyalty vs. Public Duty

- Source: business-ethics-with-llms/chapters/07-what-employees-owe-employers.md
- Lane: RESEARCH (Claude assistant)
- Hook: Loyalty to an employer is a real obligation — not just a preference. But it has a limit. Every professional code specifies the point where public duty overrides client loyalty. The question is: where exactly is that line, and who decides?
- The artifact: A sourced comparison of three whistleblower cases (Sherron Watkins at Enron, Frances Haugen at Facebook, Edward Snowden at NSA) analyzed through the lens of the employee loyalty obligation: in each case, where did the obligation end, what was the competing obligation that overrode it, and how did each professional code (accounting, tech, government contractor) address the situation?
- Prompt seed: `claude "Analyze three whistleblower cases: Sherron Watkins (Enron), Frances Haugen (Facebook), Edward Snowden (NSA). For each: (1) what employee loyalty obligation existed? (2) what competing public-duty obligation triggered the disclosure? (3) what did the relevant professional code (AICPA / ACM / government contractor rules) say about the disclosure? (4) what legal protection (or prosecution) resulted? Cite verifiable sources."`
- Read / check: Verify that Sherron Watkins' AICPA obligations are accurately described. Confirm the Dodd-Frank whistleblower protection provisions are correctly cited for Haugen. Output: Snowden's case should produce the most contested verdict — with the "illegal/ethical" cell of Chapter 1's matrix as the applicable frame.
- Human supplies: Nothing — fully synthetic research. All three cases are extensively documented in public record.
- Output medium: slate (three-column case comparison table, each cell the sourced verdict, loyalty/duty annotations)
- The change: Add a fourth case from the viewer's own industry (they describe the situation in 2–3 sentences) and ask Claude where the loyalty line falls in that context.
- Teardown angle: The loyalty obligation is real and it is bounded. The professional codes exist precisely because the loyalty question cannot be resolved case by case — the codes encode the profession's accumulated judgment about where the line is.
- Exclusions: Skip the internal organizational escalation procedures, the full SEC whistleblower bounty program, or comparative international whistleblower law.
- Score: 8/10

---

## Candidate 11 — Research ESG Metrics with Claude: What Gets Measured, What Gets Managed

- Source: business-ethics-with-llms/chapters/04-three-special-stakeholders-society-the-environment-and-government.md
- Lane: RESEARCH (Claude assistant)
- Hook: Society, the environment, and the government are stakeholders — but they don't show up at the board meeting. ESG metrics are the attempt to make them legible. The question is whether the metrics measure what they claim to measure.
- The artifact: A sourced critical analysis of ESG scoring: three major ESG rating providers (MSCI, Sustainalytics, S&P Global) for the same company (e.g., ExxonMobil), their ESG scores, the methodology differences that explain the divergence, and the academic literature on whether ESG scores predict actual environmental or social outcomes.
- Prompt seed: `claude "Compare ESG scores for ExxonMobil from MSCI, Sustainalytics, and S&P Global. For each: (1) the current or recent score, (2) what each methodology weights most heavily, (3) why the scores diverge. Then: what does the academic literature say about whether ESG scores predict actual environmental outcomes? Cite the Berg, Koelbel, Rigobon 2022 paper on ESG rating divergence."`
- Read / check: Verify the Berg/Koelbel/Rigobon (2022) "Aggregate Confusion: The Divergence of ESG Ratings" paper exists and is from Review of Finance (it does, and it is). Confirm ExxonMobil's ESG score divergence is a documented phenomenon (it is frequently cited as a canonical example). Output: the methodology comparison should show that MSCI weights scope 1/2/3 emissions differently from Sustainalytics.
- Human supplies: Nothing — fully synthetic research. ESG scores change; the video should note the score date. For NEXT STEPS, viewer looks up a company of their choice.
- Output medium: d3 (animated) — three-column bar chart showing score divergence, then methodology breakdown, then literature verdict
- The change: Ask Claude to propose one metric that would be harder to game than the current composite scores — forcing a judgment about what "measuring ESG" would actually require.
- Teardown angle: The ESG scoring divergence is not a bug in the system — it reflects genuine disagreement about what "good" means for a corporation's environmental and social impact. The divergence is the data. Treating any single score as authoritative is the error.
- Exclusions: Skip SEC climate disclosure rule litigation, or SASB vs. GRI framework comparisons in detail.
- Score: 8/10

---

## Candidate 12 — Synthesize a Code of Ethics with Claude for a Hypothetical Company

- Source: business-ethics-with-llms/chapters/01-why-ethics-matter.md + chapters/09-professions-under-the-microscope.md
- Lane: RESEARCH (Claude assistant)
- Hook: A code of ethics that takes thirty minutes to write is not a code of ethics — it is a press release. A real code encodes the profession's accumulated judgment about its specific failure modes. What goes into building one that means something?
- The artifact: A five-section model code of ethics for a hypothetical AI startup (the viewer's choice of industry), built by prompting Claude through: (1) failure mode identification, (2) stakeholder hierarchy, (3) specific prohibited conduct, (4) reporting obligations, (5) enforcement mechanism. Each section is grounded in a professional code precedent.
- Prompt seed: `claude "Build a five-section code of ethics for an AI hiring-algorithm company. Section 1: identify the three most likely failure modes (bias, opacity, accountability gaps). Section 2: stakeholder hierarchy (who does the company owe what, in what order when they conflict?). Section 3: five specific prohibited conduct rules, each concrete enough that a violation would be recognizable. Section 4: when employees must report vs. may report violations. Section 5: enforcement mechanism (who adjudicates, what are penalties)."`
- Read / check: Verify the three failure modes are specific to AI hiring (bias in protected classes, lack of explainability for adverse action, scope creep beyond the hiring decision). Confirm the prohibited conduct rules are concrete (not "be fair" but "do not use features correlated with protected class membership as model inputs"). Output: the code should be evaluable — a reader should be able to say whether a given action violates it.
- Human supplies: The company description (the viewer's own context or a hypothetical). The video uses an AI hiring-algorithm company as the demo case.
- Output medium: screen-recording mp4 (terminal: company description in, five-section code out, each section labeled)
- The change: Take one section (prohibited conduct) and ask Claude to identify a real scenario that would be ambiguous under the code — then revise the code to make the ambiguity explicit.
- Teardown angle: A code that prohibits nothing is a statement of aspiration, not a governance document. The test of a code is whether a violation would be recognizable to a reasonable person reading it. If the answer is "it depends," the code needs another clause.
- Exclusions: Skip regulatory compliance layer (EEOC, GDPR), legal review requirements, or board-level governance structures.
- Score: 8/10
