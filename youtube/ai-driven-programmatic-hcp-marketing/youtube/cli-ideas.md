# AI-Driven Programmatic HCP Marketing — CLI Video Ideas ("X with Claude")

## Candidate 01 — Build the Script-Lift Audit: Reconstruct a Vendor Lift Number on Public Data with Claude

- Source: ai-driven-programmatic-hcp-marketing/chapters/00-introduction.md + chapters/08-uplift-and-incrementality.md
- Lane: BUILD (Claude Code)  — LLM Exercise (harvested from Ch. 00 candidate project list)
- Hook: Pharma vendors claim their platforms produce measurable script lift. That number has never been stress-tested on public data. What happens when you try to reproduce it — with a credible design?
- The artifact: A screen recording of Claude Code building a pipeline that joins CMS Open Payments promotion dose data with Medicare Part D prescribing records on NPI, then estimates a naive script-lift number using pre/post comparison — then re-estimates it with a simple propensity-score design that controls for physician selection. Two numbers appear side by side in a Manim scene: "vendor-style lift" (inflated) and "adjusted lift" (smaller or null), with the gap labeled "selection effect."
- Prompt seed: `claude "In this directory, using Open Payments data and Medicare Part D prescriber data for [SGLT2 inhibitors / drug class], do the following: (1) Join on NPI to create a physician-level panel with promotion exposure and prescribing volume. (2) Compute a naive pre/post script-lift estimate: average prescribing in quarters after first Open Payments payment minus average in quarters before. (3) Re-estimate with a propensity score matching design: match exposed physicians to unexposed physicians on specialty, state, and baseline prescribing decile. (4) Report both estimates, the gap between them, and a one-sentence interpretation. Add a CLAUDE.md rule: never write 'caused' in output; always print group sizes before reporting averages; if any group is under 20, label the result unreliable."`
- Read / check: Verify group sizes are reported before any averages. Confirm the causal language guard is active — output should say "associated with" not "caused." Check that propensity matching is not a random split. Confirm the gap between naive and adjusted estimates is real and meaningful.
- Human supplies: Download CMS Open Payments and Medicare Part D public files for the relevant drug class (public, available at cms.gov). No partner data. Synthetic stand-in acceptable for the video; real public data makes the finding authentic and reproducible.
- Output medium: screen-recording mp4 (Claude Code terminal session) + Manim two-bar comparison (naive vs. adjusted lift, gap labeled)
- The change: Ask Claude to write the "kill criterion" memo: "If the adjusted lift is less than 5% and not statistically distinguishable from zero, what does that imply for the platform's value proposition? Write the memo." Show the memo appearing in the terminal output.
- Teardown angle: The gap between the vendor number and the adjusted number is not fraud — it is selection. Platforms aim at physicians who would have prescribed anyway. That is what the gap measures. Knowing this is what lets you negotiate attribution claims honestly.
- Exclusions: Cut full DID methodology; cut channel decomposition; cut NPI identity graph pipeline detail.
- Score: 10/10

---

## Candidate 02 — Build the Propensity Baseline: XGBoost vs. "MoE" on NPI Targeting Data with Claude

- Source: ai-driven-programmatic-hcp-marketing/chapters/06-ensembles-tabular-advantage.md + chapters/07-mixture-of-experts.md — LLM Exercise (harvested from Ch. 6 exercise block)
- Hook: A vendor says their Mixture of Experts model beats standard gradient boosting. But the paper's boring model hit AUC 0.94 — before leakage. After fixing it: 0.78. That is the real bar. Does the vendor's claim clear it?
- The artifact: A screen recording of Claude Code building a complete propensity model pipeline on synthetic NPI-level data: feature engineering (claims-derived, Open Payments, affiliation), XGBoost baseline with calibration and out-of-time validation, then a stacking "MoE" variant. A Manim four-quadrant evaluation checklist animates: discrimination (AUC), calibration (reliability curve), out-of-time stability, subgroup breakdown by specialty. Both models plotted on the same chart.
- Prompt seed: `claude "In this directory, using the synthetic NPI prescribing dataset, build a propensity model pipeline: (1) Feature set: specialty, prescribing decile, Open Payments meal count, email engagement tier, loyalty decile. Check each feature for leakage against a January 1 prediction timestamp — flag any feature whose signal postdates that date. (2) Train an XGBoost baseline with 5-fold out-of-time validation (train on months 1–24, test on months 25–30). Report AUC, Brier score, and a calibration plot. (3) Build a stacking ensemble (two XGBoost base models + logistic meta-learner) and evaluate identically. (4) Break out AUC by specialty (primary care vs. specialty). Report which model wins, by how much, and whether the win survives the subgroup breakdown."`
- Read / check: Verify the leakage check flags any feature computed after the prediction timestamp. Confirm out-of-time split uses chronological ordering, not random shuffle. Check that both AUC and Brier score are reported — not just AUC. Verify the subgroup breakdown uses the same test set.
- Human supplies: Synthetic NPI dataset (Claude generates it, or use public Medicare Part D slice). No proprietary data needed. Real data upgrade: download public Part D file and subset to one specialty/state.
- Output medium: screen-recording mp4 (Claude Code terminal) + Manim four-quadrant checklist animation (metrics appearing in each quadrant)
- The change: Introduce deliberate leakage — add a "recent fill flag" computed after the prediction date. Show AUC jump from 0.78 to 0.94. Ask Claude: "What is this model actually predicting?" Show the diagnosis in the terminal.
- Teardown angle: The baseline is not the worst you can do — it is the honest bar. Every vendor claim must clear it on the same evaluation design. If their AUC is higher but their split is random, their number is the leakage number.
- Exclusions: Cut TabPFN and deep tabular learning frontier detail; cut full calibration theory; cut the covariance floor mathematical derivation.
- Score: 10/10

---

## Candidate 03 — Build the Open Payments Susceptibility Check: Does Promotion Targeting Track Need or Targetability with Claude

- Source: ai-driven-programmatic-hcp-marketing/chapters/03-the-hcp-identity-graph.md — LLM Exercise (harvested from Ch. 3 CLI exercise)
- Hook: A propensity model ranks physicians by predicted prescribing. But does it rank by patient need — or by how much the physician has historically accepted industry contact? The question is answerable on public data.
- The artifact: A screen recording of Claude Code joining CMS Open Payments with Medicare Part D for one specialty in one state. Split physicians into "Open Payments present" (any industry payment) vs. "absent." Compute average SGLT2 prescribing volume for each group. A Manim two-bar chart shows the group averages with a caveat annotation: "association, not causation." The terminal also prints group sizes and warns if either group is under 20.
- Prompt seed: `claude "In this directory, using Open Payments and Part D data slices: (1) restrict to endocrinology in [state]. (2) Split prescribers into those who appear in Open Payments (any payment type) vs. those who do not. (3) For SGLT2 inhibitors (drug class from DRUG.txt), compute average claim count per group. (4) Write ch03-openpayments-assoc.md with the two averages, group sizes, join key, and a mandatory one-sentence statement: 'This association does not establish that payments caused prescribing.' Safety rules: read-only on data files; never write the word 'caused' in output; if either group is under 10, label the result unreliable."`
- Read / check: Verify the causal language guard is active. Confirm group sizes are printed before averages. Check the join key is consistent (NPI formatted the same way in both files — common failure mode). Confirm "ch03-openpayments-assoc.md" exists and contains the required caveat sentence.
- Human supplies: CMS Open Payments and Medicare Part D public data (cms.gov). One state, one specialty, one drug class. Synthetic stand-in acceptable for the video; real data makes the finding checkable.
- Output medium: screen-recording mp4 (Claude Code terminal) + Manim two-bar chart (group averages with caveat annotation)
- The change: Ask Claude: "Classify each feature in the propensity model — specialty, claims decile, Open Payments meals, email engagement — as clinical-need, behavioral-neutral, or susceptibility-proxy. For which features, if heavily weighted, does the model select for targetability rather than patient need?" Show the classification table.
- Teardown angle: The association is not proof the model is biased. It is the question the model should be asked — and almost never is. This is the public-data test that could settle the susceptibility question.
- Exclusions: Cut legal analysis of Sorrell v. IMS Health; cut HIPAA de-identification mechanics; cut AMA Masterfile commercial structure.
- Score: 9/10

---

## Candidate 04 — Build the Uplift Estimator: Separate Real Effect from Selection with Claude

- Source: ai-driven-programmatic-hcp-marketing/chapters/08-uplift-and-incrementality.md
- Lane: BUILD (Claude Code)
- Hook: A campaign reaches physicians who prescribe more afterward. But did the campaign cause that — or did the platform just aim at physicians who were already trending up? The difference is worth millions.
- The artifact: A screen recording of Claude Code building a two-model uplift estimator on synthetic physician panel data: (1) a response model (probability of prescribing in treatment window), (2) a propensity model (probability of being targeted), combined into a CATE estimate. A Manim scene shows the uplift distribution across physicians as an animated histogram — most physicians near zero, a right tail of genuine responders, a left tail of negative-uplift physicians who should not be targeted.
- Prompt seed: `claude "Build an uplift model on the synthetic physician panel data in this directory. (1) Fit a response model: XGBoost predicting prescribing in the 90-day post-campaign window. (2) Fit a propensity model: XGBoost predicting probability of being targeted (treatment indicator). (3) Compute CATE using the two-model approach: predicted outcome under treatment minus predicted outcome under control. (4) Plot the CATE distribution as a histogram. (5) Report: median CATE, 90th-percentile CATE, fraction of targeted physicians with negative uplift (should not be targeted), and a one-sentence interpretation. Add a CLAUDE.md rule: report how miscalibrated the propensity model is before using it in CATE estimation."`
- Read / check: Verify the two-model construction is correct — CATE = outcome(treatment) - outcome(control), not a difference in raw rates. Check the propensity calibration report appears before the CATE estimates. Confirm the histogram shows genuine distribution variation — not all physicians at the same CATE value.
- Human supplies: Synthetic physician panel dataset with treatment indicator, pre-period prescribing, post-period prescribing (Claude can generate this or use a real public panel). Real data upgrade: use Part D data with Open Payments as proxy treatment indicator.
- Output medium: screen-recording mp4 (Claude Code terminal) + Manim CATE histogram animation (bars growing from zero, right tail highlighted)
- The change: Show what happens when the propensity model is miscalibrated — inflate all propensity scores by 0.05. Ask Claude: "How does this change the CATE estimates? Which physicians are now misclassified as responders?"
- Teardown angle: Uplift is not response probability. A high-propensity physician is likely to prescribe regardless. The physicians worth targeting are those whose uplift is positive — not those who were going to prescribe anyway.
- Exclusions: Cut meta-learner variants (S/T/X/R-learner taxonomy); cut full DID methodology; cut sample-size power analysis.
- Score: 9/10

---

## Candidate 05 — Research the Evidence Problem: What Does Vendor "Script Lift" Actually Measure with Claude

- Source: ai-driven-programmatic-hcp-marketing/chapters/05-the-evidence-problem.md
- Lane: RESEARCH (Claude assistant)
- Hook: Every pharma marketing platform claims measurable script lift. Almost none of those claims use a credible causal design. What would a real study look like — and why don't vendors run one?
- The artifact: Claude synthesizes a research brief on HCP marketing attribution methodologies: (1) what "lift" typically means in pharma marketing vendor reports (pre/post, exposed vs. unexposed); (2) the three design problems that bias vendor lift upward (selection, timing, proxy contamination); (3) what a credible causal design would require (randomized rollout, pre-registration, matched controls); (4) why vendors don't run randomized studies (commercial incentive, data access, client relationship risk). Output: a sourced 500-word brief with a evidence-level rubric (1–4, from association to RCT).
- Prompt seed: `claude "Research HCP marketing attribution methodology. Synthesize a brief covering: (1) how 'script lift' is typically computed in pharma marketing vendor reports — cite at least one published methodological critique or academic paper; (2) the three most common design problems that bias vendor lift estimates upward; (3) what a credible causal study design would require for pharma promotion measurement; (4) why the industry rarely runs randomized designs — cite specific commercial and structural reasons. Rate each source on a 1–4 evidence scale: 1 = association only, 2 = controlled observational, 3 = natural experiment, 4 = RCT. Flag any claim you cannot verify."`
- Read / check: Verify at least one cited methodological critique is real (spot-check title and author). Confirm the three design problems are specific and distinct. Check that the evidence-level ratings are justified. Flag unverified claims for human follow-up before publishing.
- Human supplies: Nothing — Claude researches from public sources. Human must verify any flagged claims and citations.
- Output medium: screen-recording mp4 (Claude chat building the brief) + slate (evidence-level rubric as a formatted table)
- The change: Ask Claude: "Write the kill criterion memo — what finding would definitively show that a pharma platform's lift claim is entirely selection and zero increment? What would that imply for the client's ROI?" Show the memo.
- Teardown angle: The evidence problem is not that vendors are lying. It is that the industry has accepted a measurement standard that cannot separate genuine effect from selection. That is what the evidence rubric names.
- Exclusions: Cut brand association vs. script lift distinction (save for another card); cut regulatory disclosure detail; cut specific vendor criticism by name.
- Score: 9/10

---

## Candidate 06 — Build the Physician Archetype Cluster: Are Vendor Segments Real or Round Numbers with Claude

- Source: ai-driven-programmatic-hcp-marketing/chapters/03-the-hcp-identity-graph.md
- Lane: BUILD (Claude Code)
- Hook: Pharma vendors sell "physician archetypes" — loyal prescribers, switchers, influencers. But are those segments a stable structure in the data, or a round number chosen to fit a slide?
- The artifact: A screen recording of Claude Code running k-means clustering on a synthetic NPI feature matrix (prescribing decile, switching rate, specialty, Open Payments history, engagement tier). A Manim scene shows the clustering geometry: silhouette scores plotted against k (2 through 10), with the "elbow" annotated. If the true k is 3 (vendor claim), the elbow may appear at k=4 or k=5 — or there may be no clear elbow at all.
- Prompt seed: `claude "On the synthetic NPI feature matrix in this directory (columns: prescribing decile, switch rate, specialty encoded, Open Payments meal count, email engagement tier): (1) Run k-means for k = 2 through 10. For each k, compute the silhouette score and inertia. (2) Plot silhouette score vs. k — annotate the 'elbow' if one exists. (3) If the vendor claims k=3 segments ('loyal', 'switcher', 'influencer'), test that claim: is k=3 actually the best silhouette? (4) Write a one-paragraph interpretation: does the data support the vendor's 3-segment structure, or does the geometry suggest a different k? Add a CLAUDE.md rule: never label clusters with marketing names; use neutral labels (cluster_1, cluster_2, etc.)."`
- Read / check: Verify silhouette scores are computed correctly (not just inertia). Confirm the vendor's k=3 claim is actually tested against the data. Check that cluster labels are neutral — no "loyal prescriber" in the output. Confirm the interpretation is specific to the silhouette curve shape.
- Human supplies: Synthetic NPI feature matrix (Claude generates, or use a public Part D slice). No proprietary data needed.
- Output medium: screen-recording mp4 (Claude Code terminal) + Manim silhouette-vs-k line chart (animated, elbow annotated or absence noted)
- The change: Ask Claude: "If I showed a client the silhouette curve showing k=5 is optimal but we label it as k=3 for simplicity, what is the cost of that rounding? Name two decisions that would change under k=5 vs. k=3."
- Teardown angle: Physician archetypes are a marketing convenience. Whether they are a statistical reality is a testable question. The silhouette curve is the test. The geometry either supports the vendor's segmentation or it doesn't.
- Exclusions: Cut GMM vs. k-means comparison; cut hierarchical clustering; cut segment stability over time.
- Score: 8/10

---

## Candidate 07 — Research the Brand Association Question: Does Mindshare Predict Market Share with Claude

- Source: ai-driven-programmatic-hcp-marketing/chapters/02-lift-vs-brand.md + chapters/09-brand-association.md
- Lane: RESEARCH (Claude assistant)
- Hook: The pharma industry spends billions on brand equity for HCPs — assuming mindshare today becomes prescribing tomorrow. This assumption has never been rigorously tested on linked data. Is it true?
- The artifact: Claude synthesizes a research brief on the brand equity → market share assumption in pharma: (1) what the industry claim is and how it is typically measured (unaided recall, share-of-voice surveys, SOM tracking); (2) the three papers or studies that come closest to testing it (with evidence level); (3) what a rigorous test would require (linked survey + prescribing panel, lagged analysis, market-level control); (4) what the IFS/ICER clinical value data says about whether high-equity brands are high-value brands. Output: a sourced brief with a "what would change my mind" section.
- Prompt seed: `claude "Research the empirical evidence for the pharma industry claim that HCP brand mindshare predicts future market share. Synthesize a brief covering: (1) how the claim is measured in current practice (unaided recall, SOV, equity tracking); (2) the strongest published evidence supporting or refuting the lagged mindshare → prescribing relationship — cite at least 2 studies with evidence levels; (3) what a rigorous test would require; (4) whether ICER cost-effectiveness data correlates with branded market share in any studied drug class. End with a 'what would change my mind' section: what single finding would confirm or refute the industry's core assumption? Flag any claim you cannot verify."`
- Read / check: Verify the cited studies are real and their findings are accurately characterized. Confirm the "what would change my mind" section is specific and falsifiable. Flag unverified claims for human follow-up.
- Human supplies: Nothing — Claude researches from public sources. Human must verify flagged claims.
- Output medium: screen-recording mp4 (Claude building the brief) + slate (evidence table showing 4 studies with evidence levels)
- The change: Ask Claude: "If the mindshare → market share relationship is real for some drug classes but not others, what would explain the difference? Generate three hypotheses and one test for each."
- Teardown angle: The brand equity assumption is the foundation of a large fraction of HCP marketing spend. It is also largely unverified. This is the research question that matters — and the public data to test it partially exists.
- Exclusions: Cut DTC vs. HCP brand equity distinction; cut specific drug class case studies; cut brand equity finance valuation methods.
- Score: 8/10

---

## Candidate 08 — Build the Calibration Diagnostic: Catch Overconfident Propensity Scores Before They Corrupt CATE Estimates with Claude

- Source: ai-driven-programmatic-hcp-marketing/chapters/06-ensembles-tabular-advantage.md + chapters/08-uplift-and-incrementality.md
- Lane: BUILD (Claude Code)
- Hook: A perfectly ranked model can be catastrophically miscalibrated. And miscalibration in propensity scores propagates directly into uplift estimates — biasing spend decisions by millions.
- The artifact: A screen recording of Claude Code deliberately training a miscalibrated propensity model (by oversampling high-propensity physicians in the training set), then running three diagnostics: reliability curve (observed rate vs. predicted probability, by decile), Brier score, and the propagation test — show how CATE estimates shift when computed with the miscalibrated propensity vs. the calibrated one. A Manim scene shows the reliability curve: a calibrated model hugging the diagonal vs. a miscalibrated model bent away from it.
- Prompt seed: `claude "Build a propensity model calibration diagnostic on the synthetic data. (1) Train two XGBoost models: one on balanced training data (calibrated), one on training data oversampling high-propensity physicians 3:1 (miscalibrated). (2) For each: plot a reliability curve — split predicted probabilities into deciles, compute observed positive rate per decile, plot observed vs. predicted. (3) Compute Brier score for each. (4) Use each as a propensity weight in a simple IPW CATE estimate. Report how much the CATE estimate shifts between the calibrated and miscalibrated versions. Write a one-sentence interpretation: in dollar terms (assuming $40 CPM and 50,000 target physicians), what does the miscalibration cost?"`
- Read / check: Verify reliability curves are computed correctly — decile-by-decile, not continuous. Confirm Brier scores are different and the miscalibrated model has the higher score. Check that the CATE shift is non-trivial. Verify the dollar-cost calculation uses the stated CPM and count.
- Human supplies: Synthetic physician panel dataset. No real data required.
- Output medium: screen-recording mp4 (Claude Code terminal) + Manim reliability curve animation (calibrated vs. miscalibrated curves animated side by side, diagonal reference line)
- The change: Apply Platt scaling to the miscalibrated model. Show the reliability curve improve. Ask: "Is the CATE estimate now the same as the calibrated baseline? If not — why not?"
- Teardown angle: AUC measures ranking. Calibration measures whether the probabilities mean what they say. For spend decisions, you need both. A model that ranks perfectly but is systematically overconfident will overbid on the wrong physicians.
- Exclusions: Cut isotonic regression calibration detail; cut full IPW vs. DR estimator comparison; cut sample-size power calculation.
- Score: 9/10
