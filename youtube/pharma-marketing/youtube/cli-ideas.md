# Pharma Marketing — CLI Video Ideas ("X with Claude")

> Scout date: 2026-07-12
> Source material: Chapter content is scaffold placeholders. Real content available in pantry research syntheses (`pantry/pharma-marketing-evidence-synthesis.md`, `pantry/pharma-ai-hcp-marketing-synthesis.md`). A rich `video-ideas.md` already exists with 8+ vox-explainer scout cards (candidate 01–08+). CLI cards below are distinct: they focus on what Claude can BUILD or RESEARCH in a terminal session, not what can be narrated as an explainer.

---

## Candidate 01 — "Research the Physician Payment-Prescribing Evidence Base with Claude"
- Source: pharma-marketing/pantry/pharma-marketing-evidence-synthesis.md (pantry)
- Lane: RESEARCH (Claude assistant)
- Hook: A single sponsored meal under $20 is statistically associated with significantly higher prescribing of branded drugs — with a dose-response pattern across four drug classes (OR 1.18 to 2.18). The systematic evidence runs to 36 studies and 89 of 101 analyses. Claude can synthesize the strongest evidence and check the numbers.
- The artifact: A sourced 3-section brief: (1) the strongest systematic review on meals-to-prescribing: full citation, n studies, effect sizes for at least 3 drug classes with confidence intervals, (2) the immunity illusion finding — studies showing physicians systematically underestimate their own susceptibility to industry influence (the third-person effect), (3) the downstream cost: the Johns Hopkins estimate of excess annual spending and patient cost attributable to brand-over-generic promotion.
- Prompt seed: `claude "Research the systematic evidence on pharmaceutical company payments to physicians and prescribing behavior. (1) Find the strongest systematic review: full citation, sample, effect sizes (odds ratios or risk ratios) for at least 3 drug classes. If the study reports OR 1.18 for rosuvastatin, 1.70 for nebivolol, 1.52 for olmesartan, 2.18 for desvenlafaxine — verify and cite the source. (2) Find studies on the 'physician immunity illusion' — physicians' self-assessed vs measured susceptibility to pharma influence. (3) The Johns Hopkins estimate of excess spending from brand-over-generic promotion — full citation, dollar figure, methodology. Cite all sources."`
- Read / check: Verify the four ORs are from a real published study with a cited journal and DOI. Check that the immunity illusion studies measure self-assessment, not just opinions (the "third-person effect" literature). Confirm the Johns Hopkins excess spending estimate is the correct institution and dollar figure.
- Human supplies: The primary study PDFs if paywalled. A clinical pharmacologist or health economist would validate the methodology section.
- Output medium: slate (3-panel sourced brief with the OR table for 4 drug classes as a Remotion visualization)
- The change: Find one study that found no effect of payments on prescribing — and compare its methodology to the positive studies. What accounts for the discrepancy?
- Teardown angle: The evidence that pharma payments influence prescribing is not contested at the systematic review level. The contested question is mechanism — is it persuasion, reciprocity, or simply that the highest-volume prescribers are the ones being targeted? The answer has different policy implications.
- Exclusions: Full pharmaceutical marketing regulatory history, individual physician case investigations, drug efficacy data.
- Score: 9/10

---

## Candidate 02 — "Build a Sunshine Act Payment-Prescribing Linkage Visualizer with Claude"
- Source: pharma-marketing/pantry/pharma-marketing-evidence-synthesis.md (pantry)
- Lane: BUILD (Claude Code)
- Hook: The Open Payments database is public. It contains every dollar pharma paid every physician in the US since 2013. Claude can write the script that joins it with Medicare Part D prescribing data and visualizes the payment-prescribing relationship for any drug class — in a terminal session.
- The artifact: A Python script that downloads the CMS Open Payments API data for a specified drug company and date range, joins it with CMS Medicare Part D prescribing data by physician NPI, and produces: (1) a scatter plot of total payments received vs branded drug prescribing rate, (2) a Manim animation of the scatter plot growing point by point as physicians are added, with the regression line appearing at the end.
- Prompt seed: `claude "Write a Python script that: (1) queries the CMS Open Payments API (https://openpaymentsdata.cms.gov/api) for general payments from a specific pharma company to physicians in a date range, (2) queries the CMS Medicare Part D prescribing API for the same physicians' prescribing rates for the company's drugs, (3) merges by physician NPI, (4) outputs a scatter plot (matplotlib) of total payments vs branded prescribing rate, and (5) creates a Manim animation of the scatter plot building point by point. Handle API pagination and rate limits."`
- Read / check: Verify the CMS Open Payments API endpoint is correct and accessible. Check that the join is by NPI (National Provider Identifier), not physician name. Confirm the Manim scatter plot adds points in order of payment amount and the regression line appears at the end.
- Human supplies: A specific pharma company name and date range (the human selects the scope). CMS APIs are public, but large queries require pagination handling. The human should verify the legal scope before running on specific physicians.
- Output medium: screen-recording mp4 (terminal showing API query running, then Manim scatter plot animation)
- The change: Add a choropleth map variant: aggregate payments and prescribing rates by state, and animate a US map where each state colors in by the payment-prescribing correlation coefficient.
- Teardown angle: The Sunshine Act created the dataset. Studies have shown the correlation. The script makes the analysis reproducible — anyone can run it, for any company, for any time period. That is the accountability argument that disclosure was supposed to enable.
- Exclusions: Individual physician identification (for privacy), full causal inference methodology (observational data only), international pharma payment databases.
- Score: 9/10

---

## Candidate 03 — "Research the Massachusetts Disclosure + Restriction Law Outcome with Claude"
- Source: pharma-marketing/pantry/pharma-marketing-evidence-synthesis.md (pantry)
- Lane: RESEARCH (Claude assistant)
- Hook: Massachusetts paired its disclosure law with access restrictions — limiting when pharma reps could visit hospitals and what they could give. The Sunshine Act (federal) did disclosure only. Massachusetts produced measurable prescribing declines. The federal law produced papers. Claude can find and verify the comparison.
- The artifact: A sourced 3-section brief: (1) the Massachusetts disclosure + restriction law — what was mandated beyond disclosure (gift restrictions, prior approval for rep visits, hospital access restrictions), (2) the measured outcome — specific studies on prescribing behavior change in Massachusetts vs control states after the law, (3) the comparison: what the Sunshine Act (disclosure only) did and didn't change — studies specifically testing whether Sunshine Act disclosure reduced prescribing of promoted drugs.
- Prompt seed: `claude "Research the comparative effectiveness of pharma marketing regulations. (1) Massachusetts Gift Ban (2009): what restrictions were imposed beyond disclosure — gift limits, hospital access rules, prior approval for meals. (2) Studies measuring Massachusetts prescribing behavior change after the 2009 law vs control states — specific drug classes affected, effect sizes, citations. (3) Sunshine Act (2010): find studies specifically testing whether public payment disclosure under the Sunshine Act changed physician prescribing behavior for promoted drugs. What was found? Cite sources with DOIs where possible."`
- Read / check: Verify the Massachusetts Gift Ban year is correct (2009). Check that the prescribing outcome studies specifically compare Massachusetts to control states (not just before-after). Confirm the Sunshine Act studies specifically test behavior change (not just document that payments occurred).
- Human supplies: The key study PDFs if paywalled. A health economist familiar with the Massachusetts natural experiment would validate the comparison.
- Output medium: slate (3-panel sourced brief with a two-column comparison table: Massachusetts law elements vs Sunshine Act — what each changed and what the measured outcome was, as Remotion)
- The change: Identify a third state with a similar restriction law and check whether the Massachusetts outcome replicated — or find the systematic review that compares multiple state-level marketing restriction laws.
- Teardown angle: Disclosure is necessary but not sufficient. Massachusetts's additional step — restricting access, not just requiring transparency — is what moved prescribing behavior. The policy lesson is that accountability requires structural friction, not just information.
- Exclusions: Full regulatory history of pharmaceutical marketing law, FDA off-label promotion rules, direct-to-consumer advertising regulation.
- Score: 8/10

---

## Candidate 04 — "Build a Generic vs Brand Prescribing Cost Calculator with Claude"
- Source: pharma-marketing/pantry/pharma-marketing-evidence-synthesis.md (pantry)
- Lane: BUILD (Claude Code)
- Hook: Generics are bioequivalent to branded drugs in FDA-confirmed pharmacokinetic trials. They account for 80% of prescriptions but only 27% of spending. The gap is the cost of the marketing premium. Claude can build the calculator that shows what that gap costs patients — drug by drug.
- The artifact: A Python CLI that takes a drug name as input, queries the FDA drug price database (or uses Medicare Part D data), retrieves the brand and generic average retail price, computes the cost difference per month and per year, and produces a Manim bar chart comparing brand vs generic annual cost with the gap annotated as "marketing premium."
- Prompt seed: `claude "Write a Python CLI that: (1) takes a drug name as input, (2) queries the Medicare Part D drug spending dashboard or the FDA Orange Book API for the average brand and generic retail price per unit, (3) computes: monthly cost difference, annual cost difference, and the brand premium as a percentage, (4) creates a Manim bar chart with two bars (brand, generic) and the gap annotated as 'annual patient cost of brand loyalty' in dollars. Handle drug names with multiple generic manufacturers."`
- Read / check: Verify the API endpoint is correct (CMS Part D API or GoodRx/Medicaid data if CMS is unavailable). Check that the generic price uses the lowest-available generic, not the average. Confirm the Manim bars are labeled with brand and generic names and the gap arrow is annotated.
- Human supplies: A specific drug name (the human picks the drug class relevant to their context). API keys if required by the chosen data source.
- Output medium: screen-recording mp4 (terminal showing drug lookup) + Manim (animated bar chart with gap annotation)
- The change: Add a "payer impact" mode: scale the individual patient gap to a population — given a physician with 500 patients on a branded drug, compute the total annual population cost vs if all patients were switched to generic. Express as: "that physician's brand preference costs the healthcare system $X/year."
- Teardown angle: The 80%/27% split is the aggregate. The individual patient gap is concrete. Seeing $2,400/year vs $240/year for the same drug — bioequivalent by FDA — makes the marketing premium legible at the patient level.
- Exclusions: Drug-specific clinical considerations where brand/generic differ meaningfully (e.g., narrow therapeutic index drugs), formulary and insurance pricing complexity, international drug pricing.
- Score: 8/10

---

## Candidate 05 — "Research AI-Driven HCP Marketing: What Changed with Claude"
- Source: pharma-marketing/pantry/pharma-ai-hcp-marketing-synthesis.md (pantry)
- Lane: RESEARCH (Claude assistant)
- Hook: Pharma companies are deploying AI to predict which physicians are most "influenceable" at which moment — combining EHR patterns, conference attendance, social media activity, and Open Payments history into a targeting score. Claude can research what is publicly known about these systems.
- The artifact: A sourced 3-section brief: (1) the documented capabilities of AI-driven HCP targeting systems — what data inputs are used, what the predictive models target (prescription likelihood, educational event attendance, speaker nomination), citing specific vendor reports and published analyses, (2) the regulatory gap: what existing FTC, FDA, and HIPAA rules apply to AI-driven physician targeting — and what the gap is, (3) the conflict of interest question: if AI can identify the physician who is most susceptible to a given message at a given time, does that change the ethical analysis of pharmaceutical detailing?
- Prompt seed: `claude "Research AI-driven pharmaceutical HCP (healthcare professional) marketing targeting systems. (1) What data inputs do these systems use? What are they predicting — prescribing likelihood, conference attendance propensity, KOL nomination potential? Cite specific vendor case studies or published analyses of these systems. (2) What regulatory framework applies — FTC, FDA, HIPAA — and what is the documented gap? Is AI-driven targeting currently regulated differently than traditional detailing? (3) Ethically: if AI enables micro-targeting of the most susceptible physicians at the optimal moment, how does that change the traditional conflict-of-interest analysis? Cite published commentary."`
- Read / check: Verify the vendor systems cited are real (not fabricated). Check that the regulatory gap analysis cites actual regulatory text or FTC/FDA guidance, not just opinion. Confirm the ethical analysis cites published commentary (not just Claude's reasoning).
- Human supplies: Vendor documentation if publicly available. A health policy researcher or pharma ethicist would validate the regulatory gap analysis.
- Output medium: slate (3-panel sourced brief with a data-input taxonomy as a Remotion visualization)
- The change: Find a specific AI targeting vendor that has published a case study or white paper — and analyze what the case study reveals about the prediction methodology.
- Teardown angle: The meal as influence vector has been studied for 30 years. AI-driven targeting is the same influence vector at industrial precision. The research question is not new — the scale and specificity are new, and the regulatory framework has not caught up.
- Exclusions: Consumer DTC AI advertising, general healthcare AI regulation, non-pharma HCP marketing.
- Score: 8/10

---

## Candidate 06 — "Build a Journal Article Conflict-of-Interest Extractor with Claude"
- Source: pharma-marketing/pantry/pharma-marketing-evidence-synthesis.md (pantry)
- Lane: BUILD (Claude Code)
- Hook: Every published clinical trial has a conflict-of-interest disclosure. Most readers skip it. Claude can build the script that extracts all COI disclosures from a set of papers and produces a summary table: which companies funded which authors, which drug companies appear most, and whether industry funding correlates with positive trial outcomes.
- The artifact: A Python script that takes a set of paper abstracts or full texts (or PubMed IDs), extracts COI disclosures using Claude, structures them as: author | company | relationship type (research funding / honoraria / advisory board / equity / employment), and produces: (1) a company frequency table (which company appears in the most papers), (2) a by-author conflict table, (3) an outcome correlation: funded vs non-funded papers and whether the outcome is positive, negative, or null.
- Prompt seed: `claude "Write a Python script that: (1) takes a list of PubMed IDs or paper texts, (2) uses Claude API to extract COI disclosures from each paper — structured as: author name | company | relationship type (funding/honoraria/advisory/equity), (3) produces a company frequency table, (4) correlates funding source with outcome favorability: for each paper, classifies whether the primary outcome is positive (drug effective), negative (drug not effective), or null (inconclusive), and groups by industry-funded vs not-funded. Output as markdown tables. Use anthropic SDK."`
- Read / check: Verify the COI extraction correctly structures the relationship types (not just "has a conflict"). Check that the outcome classification is based on the paper's stated primary outcome, not the abstract framing. Confirm the frequency table is sorted by company, not author.
- Human supplies: A set of PubMed IDs for papers on a specific drug class (the human selects the domain). Anthropic API key.
- Output medium: screen-recording mp4 (terminal showing COI extraction running against 5 papers, tables appearing)
- The change: Add a "publication bias" mode: compare the mean effect size for industry-funded vs independently-funded papers on the same drug — testing whether funded papers report systematically larger effects.
- Teardown angle: COI disclosures are present in every paper. The structural relationship between industry funding and positive outcomes has been documented at the meta-analytic level for 30 years. The extractor makes the data computable for any reader, on any drug, in real time.
- Exclusions: Full meta-analysis of publication bias, legal analysis of research integrity, individual fraud investigation.
- Score: 8/10

---

## Candidate 07 — "Research the KOL Marketing Machine with Claude"
- Source: pharma-marketing/pantry/pharma-marketing-evidence-synthesis.md (pantry)
- Lane: RESEARCH (Claude assistant)
- Hook: Key Opinion Leaders (KOLs) are the physicians pharma companies pay to speak at conferences, sit on advisory boards, and appear in continuing medical education. The system turns the most influential doctors into funded amplifiers of branded drug messages. Claude can research how it works and what the evidence says about its effectiveness.
- The artifact: A sourced 3-section brief: (1) how KOL programs work — the typical payment structure, the activities (speaker bureaus, advisory boards, CME, journal supplements), and the scale (how many KOLs a major pharma company maintains per drug launch), (2) the evidence on KOL influence on prescribing among non-KOL physicians — peer influence effects, seminar attendance, and social network propagation, (3) the regulatory status: what FDA rules govern KOL speaking at CME events vs promotional events, and how the line is drawn in practice.
- Prompt seed: `claude "Research the pharmaceutical KOL (Key Opinion Leader) marketing system. (1) Structure: how are KOLs selected, what are the typical payment types and amounts (speaker bureau fees, advisory board retainers, meals, travel), and how many KOLs does a major pharma company maintain per drug launch? (2) Evidence: are there studies on whether KOL speaking and CME events change prescribing among the physicians who attend? What is the magnitude of the effect? (3) Regulatory: what FDA/OIG rules govern KOL speaking — what distinguishes an 'educational' CME from a promotional event in regulatory terms? Cite sources."`
- Read / check: Verify the KOL payment structure claims are sourced (not anecdotal). Check that the prescribing effect studies specifically measure non-KOL physician behavior (not just the KOLs themselves). Confirm the FDA/OIG distinction between CME and promotion is cited from actual guidance documents.
- Human supplies: Nothing — Claude synthesizes from published literature and regulatory documents. A pharmaceutical industry compliance officer or health policy researcher would validate the regulatory section.
- Output medium: slate (3-panel sourced brief with a KOL program flow diagram as Remotion — company → KOL selection → activities → non-KOL physician influence)
- The change: Find the total annual spend on KOL programs by the top 10 pharma companies — or the best available estimate — and put it in context of total pharmaceutical marketing spend.
- Teardown angle: KOL programs work because they route pharma's message through the physicians other physicians trust. The message doesn't come from the company — it comes from a respected colleague who happens to be paid to deliver it. That is not incidental; it is the design.
- Exclusions: Individual KOL identification, anti-kickback statute litigation, academic medical center conflict-of-interest policies.
- Score: 8/10

---

## Candidate 08 — "Build a Pharma Marketing Spend vs R&D Spend Visualizer with Claude"
- Source: pharma-marketing/pantry/pharma-marketing-evidence-synthesis.md (pantry)
- Lane: BUILD (Claude Code)
- Hook: The major pharmaceutical companies spend more on marketing than on R&D. That claim circulates constantly — but the data is harder to pin down than it sounds, because the industry doesn't separately report "marketing" spend in financial filings the way it reports R&D. Claude can find the best available data and build the visualizer.
- The artifact: A Python script that retrieves publicly available financial data for the top 10 pharmaceutical companies (from SEC 10-K filings or company reports), extracts R&D spend and "selling, general, and administrative" (SG&A) spend as a proxy for marketing, and produces a Manim animated grouped bar chart showing R&D vs SG&A vs net revenue for each company — with the R&D/SG&A ratio annotated.
- Prompt seed: `claude "Write a Python script that: (1) retrieves 10-K financial data for 5 major pharma companies (Pfizer, Johnson & Johnson, Merck, AbbVie, Bristol-Myers Squibb) from SEC EDGAR API, (2) extracts: R&D expense, SG&A expense, total revenue for the most recent fiscal year, (3) computes: R&D as % of revenue, SG&A as % of revenue, SG&A/R&D ratio, (4) creates a Manim animated grouped bar chart showing R&D vs SG&A vs revenue for each company, with the SG&A/R&D ratio annotated above each pair."`
- Read / check: Verify the SEC EDGAR API endpoint is correct (EDGAR full-text search API). Check that R&D and SG&A line items are correctly identified (the line names vary by company). Confirm the Manim bar chart is grouped by company (not stacked). Flag if the SG&A proxy is acknowledged as an overestimate of marketing spend.
- Human supplies: Nothing — the data is from public SEC filings. The script handles the download. A financial analyst would validate the line-item identification.
- Output medium: Manim (animated grouped bar chart with R&D/SG&A ratio annotations)
- The change: Add a time-series version: show how the R&D/SG&A ratio has changed over 10 years for each company — whether the marketing premium has grown or shrunk as the industry has changed.
- Teardown angle: SG&A includes more than marketing — but even with that caveat, the ratio is instructive. The companies that spend most on marketing are not necessarily the ones with the most innovative pipelines. The ratio makes that structural pattern visible.
- Exclusions: Full pharma financial analysis, drug pricing economics, pipeline valuation, M&A.
- Score: 7/10
