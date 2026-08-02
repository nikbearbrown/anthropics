# MBA Intellectual Property: with LLMs — CLI Video Ideas ("X with Claude")

Lane: RESEARCH (law/policy — synthesized docs from citable IP sources; some BUILD-adjacent artifacts where quantitative outputs exist)
Book: mba-intellectual-property (5 substantive chapters: patent basics, patent enforcement, copyright, trademark, trade secret; running multi-chapter IP strategy project across all chapters using a Claude Project)

---

## Card 1 — Patent Patentability Checker

**Source:** Chapter 1 (Patent Basics) — three patentability requirements (novelty, non-obviousness, utility), bargain theory, 20-year term, LLM exercise: prior-art landscape for a new product idea
**Lane:** RESEARCH
**Hook:** Before a startup spends $15,000 on a patent attorney, Claude can run a preliminary patentability screen. Three questions, one session — and the output is a memo a lawyer can actually use as a starting point.
**The artifact:** A structured patentability analysis memo: (1) utility assessment — does the invention solve a specific real-world problem? (2) novelty screen — describe prior art landscape; (3) non-obviousness analysis — would a person of ordinary skill find this combination obvious? (4) recommendation: file, strengthen, or abandon. Output formatted as a professional memo with citations.
**Prompt seed:** `claude "Run a preliminary patentability analysis for the following invention: [invention description]. Apply the three-part test from 35 U.S.C. §§ 101, 102, 103: (1) Utility — does it solve a specific, credible problem? (2) Novelty — describe likely prior art categories and search strategy; (3) Non-obviousness — would a POSITA find this combination obvious given the prior art? Output a memo with a go/no-go recommendation and flagged risks."`
**Read/check:** Verify the three requirements match Chapter 1 (novelty = 35 U.S.C. §102, non-obviousness = §103, utility = §101). Confirm that Claude's prior-art categories are plausible given the technology domain.
**Human supplies:** The invention description — a 2-3 paragraph technical description of the product or process to be analyzed. The video uses the textbook's LLM chapter exercise (a smart-packaging startup idea from Chapter 1) as the example.
**Output medium:** Manim animated decision-tree — three nodes (utility → novelty → non-obviousness) illuminate green or yellow sequentially; final node shows "RECOMMENDED: File provisional" or "RISK: Prior art present." The memo text overlays each node as it activates.
**The change:** Modify the invention slightly (add a software layer) — ask Claude to re-run and flag the §101 abstract-idea exclusion risk (Alice Corp. doctrine). Watch the recommendation change from "file" to "file with caution — software claim scope."
**Teardown angle:** Ask Claude to identify the three weakest claims in the proposed patent and suggest how to narrow them to improve nonobviousness. This is the "make it better" revision that every viewer wants to see.
**Exclusions:** No actual patent drafting or claim language (that requires an attorney and is out of scope for a RESEARCH-lane video). No international PCT filing analysis.
**Score:** 9/10 — clean three-step structure, vivid revision beat (Alice Corp. risk appears on change), directly useful output. The artifact is a go/no-go memo — specific, checkable, actionable.

---

## Card 2 — Patent Claim Mapping and Infringement Analysis

**Source:** Chapter 2 (Patent Enforcement) — Polaroid v. Kodak ($900M judgment), claim construction, all-elements rule, PTAB inter partes review; doctrine of equivalents
**Lane:** RESEARCH
**Hook:** Kodak's camera had one extra mirror. Polaroid's patents had six claims. One word in one claim cost Kodak $900 million. Claude maps a patent's claims to a product's features — and flags the elements that create infringement risk.
**The artifact:** A claim-mapping table: rows = patent claims (independent + dependent), columns = product features. Each cell: present/absent/equivalent? Final row: infringement likelihood (all-elements test). Includes a PTAB prior-art challenge section: "which claims are most vulnerable to IPR challenge?"
**Prompt seed:** `claude "You are a patent analyst. Given this patent claim set: [paste claims]. And this product description: [paste product spec]. Apply the all-elements rule: for each independent claim, map each claim element to a product feature. Mark: (Y) present, (N) absent, (E) present under doctrine of equivalents. If any element is N, mark claim: NOT INFRINGED. If all Y or E, mark: POTENTIALLY INFRINGED. Output a structured table and a risk summary."`
**Read/check:** Verify Chapter 2's Polaroid v. Kodak narrative — confirm the all-elements rule and doctrine of equivalents are correctly stated. Check that the PTAB IPR timeline (9 months to institution) is accurate.
**Human supplies:** A public patent's claim set (copy-paste from Google Patents — free, public domain) and a product specification (can be a synthetic product description from the video). Chapter 2's Polaroid case provides a historical worked example.
**Output medium:** Manim animated claim-mapping table — rows populate one claim at a time; Y/N/E cells color-code (green/red/yellow); the "all-elements" row flashes red or green at the end. PTAB vulnerability section appears as a separate annotation block.
**The change:** Apply the doctrine of equivalents to one "N" element — show it flipping to "E" and watch the claim status change from NOT INFRINGED to POTENTIALLY INFRINGED. Narrate: "This is why patent lawyers argue about single words."
**Teardown angle:** Ask Claude which claims are most vulnerable to a PTAB IPR challenge and to suggest prior-art search terms. This gives the viewer the defendant's playbook.
**Exclusions:** No freedom-to-operate (FTO) formal opinion (requires attorney). No international patent family mapping.
**Score:** 8/10 — highly specific artifact (claim mapping table), the Polaroid/Kodak story is compelling, the doctrine-of-equivalents flip is a clean revision beat. Requires user to supply a real patent, which is easy (Google Patents).

---

## Card 3 — Fair Use Four-Factor Analyzer

**Source:** Chapter 3 (Copyright Basics) — Naruto monkey selfie, fair use four-factor test (§107), DMCA safe harbor, orphan works problem; transformative use doctrine
**Lane:** RESEARCH
**Hook:** A monkey takes a selfie. A photographer claims copyright. The court says: only humans can hold copyright. Meanwhile, someone else's AI-generated image gets rejected. Claude applies the four-factor fair use test to any content reuse scenario.
**The artifact:** A four-factor fair use analysis memo: (1) purpose and character (commercial vs. educational, transformative?), (2) nature of the copyrighted work (factual vs. creative), (3) amount and substantiality taken, (4) market effect. Outputs a fair-use likelihood score (low/medium/high) with reasoning for each factor.
**Prompt seed:** `claude "Apply the four-factor fair use test under 17 U.S.C. §107 to the following scenario: [describe the use]. For each factor: (1) Purpose — is it transformative, educational, commercial? (2) Nature — is the source work primarily factual or creative? (3) Amount — what portion was used, and was it the 'heart' of the work? (4) Market effect — does this use substitute for the original market or a licensing market? Weigh all four factors and state the fair-use likelihood as Low, Medium, or High with a one-paragraph defense and one-paragraph risk."`
**Read/check:** Confirm the four factors match 17 U.S.C. §107. Verify Chapter 3's statement that no single factor is determinative — Claude's output should reflect this.
**Human supplies:** A content reuse scenario — described in 2-3 sentences. The video uses two contrasting scenarios from Chapter 3: (a) a university professor posting 10 pages of a textbook for class (likely fair use), and (b) a YouTube channel reading an entire audiobook verbatim (likely not).
**Output medium:** Manim animated four-quadrant grid — each factor populates as a colored quadrant (green = favors fair use, red = favors infringement); final frame shows the overall balance with a likelihood indicator.
**The change:** Modify the university professor scenario to include an entire chapter rather than 10 pages — watch factor 3 (amount) flip from green to red, and the overall assessment shift from Medium to Low (fair use). Narrate: "The amount taken just crossed the 'substantiality' line."
**Teardown angle:** Ask Claude to suggest how the user could restructure the use to strengthen their fair-use argument — e.g., add commentary, reduce the excerpt, or obtain a license. This is the practical advisory beat.
**Exclusions:** No DMCA takedown procedure analysis (separate topic). No international copyright comparison (Chapter 3 covers US law only).
**Score:** 9/10 — four-factor structure maps perfectly to the CLI loop beats (four prompts, four outputs, one synthesis). The quadrant animation is visually clean. High viewer relevance (everyone wants to know if their content reuse is legal).

---

## Card 4 — Trademark Distinctiveness and Genericide Risk Assessor

**Source:** Chapter 4 (Trademark Basics) — Aspirin genericide story, distinctiveness spectrum (generic → descriptive → suggestive → arbitrary → fanciful), likelihood-of-confusion test, secondary meaning
**Lane:** RESEARCH
**Hook:** Aspirin used to be a trademark. So did Escalator, Thermos, and Xerox. The companies lost their marks by letting them become generic. Claude assesses a new brand name's position on the distinctiveness spectrum — and flags genericide risk.
**The artifact:** A trademark analysis report: (1) distinctiveness classification (generic/descriptive/suggestive/arbitrary/fanciful); (2) if descriptive — secondary meaning required? (3) likelihood-of-confusion analysis against a named competitor mark; (4) genericide risk score (low/medium/high based on whether the mark is the only word for the product category); (5) recommended monitoring strategy.
**Prompt seed:** `claude "Assess the trademark strength of the proposed brand name '[name]' for a product in the [category] market. Apply the Abercrombie distinctiveness spectrum: classify as generic, descriptive, suggestive, arbitrary, or fanciful. If descriptive, assess whether secondary meaning could be established. Run a likelihood-of-confusion analysis against [competitor mark]. Score genericide risk (low/medium/high) and explain the mechanism. Recommend three protective measures."`
**Read/check:** Verify Chapter 4's Abercrombie spectrum (the case is Abercrombie & Fitch Co. v. Hunting World, 1976). Confirm Aspirin's genericide story is accurate (Bayer's 1921 loss in the US). Check that the likelihood-of-confusion factors are correct (typically the Sleekcraft or Polaroid factors depending on circuit).
**Human supplies:** A proposed brand name and product category — synthetic for the video (Chapter 4 uses "Starbucks" and "Google" as examples of arbitrary/fanciful marks). The video can demo with a fictional startup name in the EdTech category.
**Output medium:** Manim animated distinctiveness spectrum — horizontal bar from "Generic" to "Fanciful" with the proposed mark placed as an animated dot; genericide risk gauge animates separately; confusion-factor table populates in sequence.
**The change:** Ask Claude to analyze what would happen if the mark became the dominant generic term (e.g., "people started saying 'I'm going to [brand] it' instead of 'search for it'"). Claude should flag this as a genericide trigger and recommend active brand policing (the Google "Please don't verb our noun" strategy).
**Teardown angle:** Ask Claude to draft a cease-and-desist style usage guide for employees — the kind of internal document that shows trademark policing effort in a future infringement case.
**Exclusions:** No trademark registration procedure (USPTO filing, office actions — that's attorney work). No international trademark analysis.
**Score:** 8/10 — Aspirin genericide story is textbook-memorable, the distinctiveness spectrum animation is visually elegant, the change prompt adds practical value. Clean RESEARCH artifact.

---

## Card 5 — Trade Secret Audit and Misappropriation Risk Report

**Source:** Chapter 5 (Trade Secret Basics) — Coca-Cola vault, three-element definition (valuable + secret + reasonable measures), Defend Trade Secrets Act (DTSA), inevitable disclosure doctrine
**Lane:** RESEARCH
**Hook:** Coca-Cola's formula has stayed secret for 130 years — not by patent, but by keeping it out of labs that file with the USPTO. Claude audits a company's trade secret program and scores the three elements that determine whether a court will protect it.
**The artifact:** A trade secret audit report with three scored sections: (1) Value — is the information actually valuable because it's secret (competitive advantage test)? (2) Secrecy — is it actually non-public? (3) Reasonable Measures — what physical, digital, contractual, and procedural protections exist? Each section is scored 1–5. Final output: a DTSA protection probability (low/medium/high) and a remediation checklist.
**Prompt seed:** `claude "Conduct a trade secret audit for the following business information: [description of information]. Apply the three-element test under the Defend Trade Secrets Act (18 U.S.C. §1836): (1) Economic value from secrecy — does it confer competitive advantage specifically because competitors don't know it? (2) Not generally known — is this information publicly available? (3) Reasonable measures — list current protections and score them 1-5 (NDA coverage, physical access controls, digital security, employee training). Output a protection probability and a prioritized remediation list."`
**Read/check:** Verify the DTSA citation (18 U.S.C. §1836, enacted 2016). Confirm Chapter 5's three-element definition. Check that the inevitable disclosure doctrine is correctly framed as a minority doctrine (most courts don't automatically apply it).
**Human supplies:** A description of the business information to be audited — e.g., a pricing algorithm, a customer list, a manufacturing process. The video uses the textbook's fictional trade secret exercise from Chapter 5 (a startup's proprietary recommendation engine) as the example.
**Output medium:** Manim animated three-section scorecard — each element populates with a score bar (1–5), color-coded red-to-green; the three bars combine into an overall DTSA protection probability gauge; remediation checklist items appear as a final animated checklist.
**The change:** Reveal that the startup posted a blog post describing the algorithm's "core innovation" — ask Claude to re-score the secrecy element. Score drops from 4 to 1, overall protection probability drops from High to Low. Narrate: "One blog post destroyed the trade secret status."
**Teardown angle:** Ask Claude to draft the key clauses of an NDA that would protect this trade secret going forward — focusing on the definition of confidential information, duration, and return-of-materials obligations. This is the practical output attorneys actually produce.
**Exclusions:** No criminal trade secret prosecution analysis (Economic Espionage Act — separate statute, separate topic). No employee non-compete enforceability analysis (varies too much by state).
**Score:** 9/10 — the three-element structure maps cleanly to three prompt beats, the scorecard animation is elegant, and the "one blog post destroyed it" change moment is a perfect narrative climax. Directly useful output.

---

## Card 6 — Multi-Asset IP Strategy Builder (Full Startup Portfolio)

**Source:** Chapters 1–5 combined — the book's running LLM exercise: build a complete IP strategy for a fictional startup covering patent, copyright, trademark, and trade secret layers
**Lane:** RESEARCH
**Hook:** A startup has one innovation — but four IP weapons. Claude walks through patent, copyright, trademark, and trade secret in sequence, building a complete IP strategy document in one session using a persistent Claude Project.
**The artifact:** A four-section IP strategy memo for a fictional startup: (1) Patent layer — what to patent, claim scope recommendation, timing; (2) Copyright layer — what software/content assets are protected, registration value, DMCA considerations; (3) Trademark layer — brand name strength, logo protection, domain strategy; (4) Trade secret layer — what to keep out of the patent application, reasonable measures checklist. Final section: competitive moat assessment — how do the four layers reinforce each other?
**Prompt seed:** `claude "You are an IP strategy advisor. My startup: [description]. Build a four-layer IP strategy: (1) Patent — identify the patentable core invention and recommend claim scope (broad vs. narrow, timing). (2) Copyright — list assets automatically protected (code, docs, UI) and recommend registration priorities. (3) Trademark — assess proposed brand name and recommend filing class. (4) Trade Secret — identify what must stay out of any patent application to remain protectable as a trade secret. Conclude with a moat assessment: how do these four layers together create a defensible competitive position?"`
**Read/check:** Verify the four-layer structure matches the running LLM exercise described in Chapter 1's introduction. Confirm the trade-secret-vs-patent tradeoff (filing a patent discloses the invention — sometimes it's better not to file).
**Human supplies:** A 3-5 sentence startup description — what it makes, who it serves, what the core innovation is. The video uses a fictional smart-packaging startup introduced in Chapter 1. Synthetic description is perfect for the video.
**Output medium:** Manim animated four-quadrant diagram — each IP layer populates as a quadrant with key protections listed; the competitive moat appears as the overlapping center of all four quadrants (Venn-style); final frame shows a timeline of "when to file/register each layer."
**The change:** Add a competitor who just filed a patent in the same space — ask Claude to revise the patent strategy section. It should recommend filing a provisional immediately to establish priority date, and strengthening the trade secret layer as a fallback.
**Teardown angle:** Ask Claude to identify the single biggest IP risk for this startup and what one action would reduce it most. This produces the "if you only do one thing" closing beat.
**Exclusions:** No IP valuation (financial modeling of IP asset value). No licensing negotiation strategy (Chapter 6 of a different IP textbook — not in scope here).
**Score:** 9/10 — the running-project structure is the unique feature of this book; this card captures the full synthesis. The four-quadrant animation is visually satisfying. The "add a competitor" change prompt is highly realistic and produces a genuinely useful revision.

---

## Card 7 — IP Due Diligence Checklist for M&A

**Source:** Chapters 1–5 combined — patent enforcement (Chapter 2: chain of title, assignment records), copyright ownership (Chapter 3: work-for-hire doctrine), trademark registration status (Chapter 4), trade secret contamination risk (Chapter 5: inevitable disclosure)
**Lane:** RESEARCH
**Hook:** A startup gets acquired — and the acquirer discovers the IP was never properly assigned from the founders. The deal collapses. Claude builds an M&A IP due diligence checklist and runs it against a target company's described IP portfolio.
**The artifact:** A structured IP due diligence report covering four risk categories: (1) Patent — chain of title, prosecution history estoppel, freedom to operate; (2) Copyright — work-for-hire documentation, open-source license compliance, DMCA status; (3) Trademark — registration status, renewal dates, likelihood-of-confusion risks; (4) Trade Secret — NDA coverage of all employees/contractors, reasonable-measures audit, departing employee contamination risks. Each category: risks found / severity / recommended remediation.
**Prompt seed:** `claude "You are conducting IP due diligence for an acquisition. Target company description: [describe the company's IP portfolio]. Run a four-category IP risk assessment: (1) Patent chain of title — are all assignments properly recorded with the USPTO? (2) Copyright work-for-hire — are contractor agreements explicit? (3) Trademark registrations — are all key marks registered, renewed, and free of pending disputes? (4) Trade secret — do all employees and contractors have signed NDAs? Are reasonable measures documented? Output a risk table with severity (High/Medium/Low) and remediation actions."`
**Read/check:** Verify Chapter 2's assignment recording requirement (35 U.S.C. §261 — assignments must be recorded with USPTO to be enforceable against a bona fide purchaser). Confirm the work-for-hire doctrine from Chapter 3 (commissioned works require a written agreement).
**Human supplies:** A description of the target company's IP portfolio — what patents it claims to hold, what software it has developed, what brand assets it uses, and what trade secrets it asserts. The video uses a fictional EdTech startup with mixed IP status as the example.
**Output medium:** Manim animated risk table — four sections animate in; each row populates with severity color (red = High, yellow = Medium, green = Low); total risk score appears as a final deal-health gauge.
**The change:** Reveal that two key software engineers were contractors without written agreements — ask Claude to re-score copyright risk. Severity jumps from Medium to High; the deal-health gauge drops into the red zone. Narrate: "This is the moment acquirers start renegotiating the price."
**Teardown angle:** Ask Claude to draft the two remediation documents that would resolve the highest-severity risk: (a) a nunc pro tunc assignment for the unrecorded patent, and (b) a retroactive work-for-hire agreement for the contractor code.
**Exclusions:** No SEC disclosure obligations for IP risks. No international IP due diligence (Chapter scope is US law).
**Score:** 8/10 — high-stakes narrative (deal collapse), four-category structure maps to natural video beats, the change prompt produces a visceral severity jump. Slightly more advanced audience (M&A participants) but extremely high relevance.

---

## Card 8 — Open Source License Compliance Checker

**Source:** Chapter 3 (Copyright Basics) — DMCA safe harbor, copyright in software, GPL/MIT/Apache license families; the "legal line" in software copyright; Chapter 5 (Trade Secret) — open-source disclosure risk
**Lane:** RESEARCH
**Hook:** Every software product contains open-source code. Each license has different rules about what you must disclose, what you must share, and what you can keep proprietary. Claude audits a stack of OSS licenses and flags the compatibility conflicts.
**The artifact:** An OSS license compliance report: input is a list of open-source libraries with their licenses (MIT, Apache 2.0, GPL-2.0, LGPL, AGPL, etc.). Output: (1) copyleft vs. permissive classification for each; (2) obligations triggered (attribution, source disclosure, share-alike); (3) compatibility conflicts (e.g., GPL-2.0 in the same binary as Apache 2.0 creates a conflict); (4) risk for commercial/proprietary use.
**Prompt seed:** `claude "Audit the following open-source dependencies for a commercial SaaS product: [library name: license]. For each library: (1) classify as permissive or copyleft; (2) list obligations triggered (attribution, source disclosure, share-alike, patent grant); (3) flag compatibility conflicts with other licenses in the list; (4) flag any libraries whose license terms prohibit commercial use without a commercial license. Output a table sorted by risk level (High/Medium/Low)."`
**Read/check:** Verify GPL compatibility matrix: GPL-2.0 and Apache 2.0 are incompatible in the same binary (confirmed by FSF); GPL-3.0 and Apache 2.0 are compatible. MIT and Apache 2.0 are compatible with each other and with GPL.
**Human supplies:** A list of OSS libraries and their license identifiers — easy to generate from any `package.json`, `requirements.txt`, or `pom.xml`. The video uses a synthetic 10-library stack covering all three risk levels.
**Output medium:** Manim animated dependency table — libraries appear row by row; classification badges animate (permissive = blue, copyleft = orange, unknown = grey); conflict arrows draw between incompatible pairs; risk column populates last with color coding.
**The change:** Add a single AGPL-3.0 library to the stack — watch it trigger a High-risk flag for the entire SaaS product (AGPL requires source disclosure even for network use, which is incompatible with closed-source SaaS). Narrate: "One library can poison the whole proprietary codebase."
**Teardown angle:** Ask Claude to recommend the remediation: (a) replace the AGPL library with an alternative; (b) obtain a commercial license from the vendor; (c) isolate it as a separate service with an API. Show how isolation can resolve the conflict without code changes.
**Exclusions:** No patent grant analysis (Apache 2.0's patent termination clause is complex — flag it but don't fully analyze). No dual-licensing strategy (that requires licensing negotiation expertise).
**Score:** 8/10 — highly practical artifact (every tech company faces this), the AGPL-poison change moment is dramatic and accurate, the three-remediation teardown gives viewers real options. Clean RESEARCH artifact with quantifiable outputs (risk levels).
