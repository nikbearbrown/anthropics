# Cancer Research — CLI Video Ideas ("X with Claude")

## Candidate 01 — "Research PPV Collapse with Claude: Why a 99%-Specific Test Is Wrong Two-Thirds of the Time"
- Source: cancer-research/chapters/01-cancer-screening-finding-it-early-enough-to-cure.md + LLM Exercise 2
- Lane: RESEARCH (Claude assistant)
- Hook: A multi-cancer blood test reports 99% specificity — so why does a positive result mean you probably don't have cancer? The math is counterintuitive and the number that actually matters is never in the press release.
- The artifact: a sourced research brief with (1) a fully worked 2×2 table at three prevalence levels (0.5%, 2%, 10%) for sensitivity=90%/specificity=99%, (2) a plain-English interpretation of each PPV, and (3) a one-paragraph evaluation of a real MCED test (Galleri) using the chapter's framework — displayed as a Manim animation of the 2×2 grid building cell-by-cell, then the PPV bar rising as prevalence climbs.
- Prompt seed: `claude "A screening test has sensitivity 90% and specificity 99%. Build a full 2×2 table for 100,000 people at three prevalence levels: 0.5%, 2%, 10%. Compute PPV at each level. Then apply this framework to the Galleri multi-cancer early detection test — what prevalence does it screen in, what does the literature say about its PPV in practice, and does the NHS-Galleri trial's interim report give us mortality data or only detection rate data? Cite sources."`
- Read / check: Verify the 2×2 arithmetic matches chapter values (PPV ≈ 31% at 0.5%); confirm Galleri citation is to an actual published trial or interim report, not hallucinated; check that mortality vs detection distinction is preserved in the synthesis.
- Human supplies: Nothing — fully synthetic. All numbers derive from published trial data Claude can retrieve. Manim animation is generated from the computed tables. If the human wants the exact Galleri interim numbers verified, they supply a PDF of the NHS-Galleri preprint.
- Output medium: Manim (animated 2×2 grid cells filling in with counts + PPV bar chart rising as prevalence slider moves)
- The change: Re-run the prompt asking: "Now apply Wilson and Jungner criterion 5 (benefits outweigh harms) — what false-positive burden does each prevalence scenario imply, and what follow-up workup cascade cost would that represent?"
- Teardown angle: The test's specificity sounds like the story; the population's prevalence is the story. The same test that looks useful in high-risk groups looks dangerous in low-risk groups — not because the test changed but because PPV is a joint property of the test and who you test.
- Exclusions: Technical chemistry of ctDNA assays; detailed NLST data on lung-CT; history of Wilson-Jungner beyond one sentence.
- Score: 9/10

## Candidate 02 — "Research the Three Biases That Make Screening Look Better Than It Is with Claude"
- Source: cancer-research/chapters/01-cancer-screening-finding-it-early-enough-to-cure.md + LLM Exercise 3
- Lane: RESEARCH (Claude assistant)
- Hook: A new screening test boasts 80% five-year survival vs 45% for symptom-detected cases — nearly double. But no one in the screened group lived a day longer. How can survival improve while lives stay identical?
- The artifact: a sourced 3-panel comparison brief — one paragraph per bias (lead-time, length-time, overdiagnosis), each with a concrete published example where the bias produced the gap, a diagram explanation, and the study design that rules it out — rendered as a Manim three-row table building left-to-right (apparent benefit → reality).
- Prompt seed: `claude "Explain lead-time bias, length-time bias, and overdiagnosis with one published real-world example of each where the bias inflated apparent screening benefit. For each, describe one study design feature that would allow a researcher to rule it out. Synthesize into a brief that a clinician could use to evaluate any new screening claim."`
- Read / check: Confirm each example is a real published study (not confabulated); verify the NLST is cited correctly as a mortality-endpoint trial; confirm the three study-design mitigations are mechanistically correct.
- Human supplies: Nothing — fully synthetic. Published examples (NLST, PSA/PLCO, thyroid screening) are in the public record.
- Output medium: Manim (three-row animated table: left column "What you see", right column "What's really happening", each row revealed sequentially with connecting arrows)
- The change: Add a fourth row: "What would settle it" — the study design that would be immune to all three biases simultaneously (randomized trial measuring disease-specific mortality).
- Teardown angle: Survival time from diagnosis is not the same as lifespan. The gap between those two statements is where most screening marketing lives.
- Exclusions: Individual screening modality details (mammography protocols, colonoscopy intervals); policy debates about specific programs; USPSTF grade criteria.
- Score: 8/10

## Candidate 03 — "Research the Three-Validity Hierarchy for Liquid Biopsy with Claude"
- Source: cancer-research/chapters/03-molecular-diagnostics-staging-and-the-liquid-biopsy.md + LLM Exercise 7 & 8
- Lane: RESEARCH (Claude assistant)
- Hook: A liquid biopsy company reports 45% of cancer patients carry an "actionable alteration." A colleague concludes nearly half could get targeted therapy. What's missing from that sentence?
- The artifact: a sourced research brief that (1) defines analytic validity / clinical validity / clinical utility in one sentence each with a real example of a test that has cleared each level, (2) applies the three-validity filter to three ctDNA use cases (resistance monitoring for EGFR T790M, DYNAMIC trial MRD-guided adjuvant de-escalation, MCED screening), ranking them by current strength of utility evidence, (3) identifies the single most important unresolved empirical question for MCED — displayed as a Manim three-gate funnel narrowing left to right with tests peeling off at each gate.
- Prompt seed: `claude "Apply the three-validity framework (analytic, clinical, clinical utility) to three uses of circulating tumor DNA: (1) EGFR T790M resistance monitoring in lung cancer, (2) the DYNAMIC trial's MRD-guided adjuvant de-escalation in stage II colon cancer, (3) multi-cancer early detection in asymptomatic people. For each: what validity level has been established, what utility evidence exists or is pending, what are the consequences of acting vs not acting? Rank the three by current strength of clinical utility evidence and justify the ranking."`
- Read / check: Confirm DYNAMIC trial conclusions match the chapter (non-inferior RFS with reduced chemo use); verify EGFR T790M osimertinib indication is correctly scoped; ensure the MCED ranking is justified by the absence of mortality data, not a hallucinated trial.
- Human supplies: Nothing — fully synthetic. All three examples are in the published literature Claude can retrieve.
- Output medium: Manim (three-gate funnel: each gate labeled, tests shown entering and some exiting at each gate as colored nodes; the MCED test stops at gate 3 in red)
- The change: Add a fourth use case: "Clonal hematopoiesis confounding — how does CHIP affect the interpretation of any ctDNA result in patients over 60?" and integrate this as a cross-cutting caveat on all three use cases.
- Teardown angle: Analytical sophistication is not clinical utility. The test that detects the most is not automatically the test that helps the most. The third validity level is the only one that matters for patients.
- Exclusions: Technical assay chemistry; detailed BRCA/PARP inhibitor companion diagnostic evidence; CHIP genetics beyond two mutations.
- Score: 8/10

## Candidate 04 — "Research Surrogate Endpoints vs Hard Endpoints with Claude: When Tumor Shrinkage Doesn't Save Lives"
- Source: cancer-research/chapters/04-principles-of-cancer-therapy-goals-and-modalities.md + LLM Exercises 2 & 3
- Lane: RESEARCH (Claude assistant)
- Hook: A new cancer drug shrank tumors in 60% of patients vs 20% for standard care. But patients in both arms died at the same time. Did the drug work?
- The artifact: a sourced endpoint analysis brief: (1) a table classifying ORR/PFS/OS/QoL as surrogate or hard endpoint for a hypothetical pivotal trial, with direction and significance columns, (2) a one-paragraph treatment recommendation that explicitly weights the hard endpoints above the surrogates, (3) three published examples where PFS improved but OS did not, identified from the oncology literature — rendered as a Manim three-tier hierarchy (hard endpoints top, surrogates bottom) with arrows showing when surrogates do and don't translate.
- Prompt seed: `claude "A pivotal trial reports: ORR 60% vs 20% (p<0.001); median PFS 9 vs 6 months (p=0.01); median OS 18 vs 17 months (p=0.41); grade 3-4 toxicity 35% vs 18%. Build a table classifying each endpoint as surrogate or hard, mark direction and significance. Then write a one-paragraph treatment recommendation explicitly weighting hard endpoints. Identify three real oncology trials where PFS improved but OS did not, and explain why the gap occurred in each."`
- Read / check: Verify the three real examples are actual published trials (e.g., bevacizumab in early breast cancer, some checkpoint inhibitor combinations); confirm the recommendation is internally consistent with the endpoint table; check that the FDA accelerated approval pathway is accurately characterized.
- Human supplies: Nothing — fully synthetic. Published examples are in the oncology literature.
- Output medium: Manim (animated three-tier hierarchy building top-to-bottom, with surrogate-to-hard endpoint arrows lighting green or red based on whether translation occurred in the cited trials)
- The change: Re-run asking: "Now apply the FDA Project Optimus framework — how does dose optimization relate to the hard endpoint problem, and what does it imply for the trial design question?"
- Teardown angle: Tumor shrinkage is what the drug does to the tumor. Survival is what it does for the patient. These are different measurements and they can diverge — the oncology literature is full of examples where they did.
- Exclusions: Regulatory approval mechanics beyond one sentence; individual trial enrollment criteria; historical chemotherapy development timeline.
- Score: 9/10

## Candidate 05 — "Research Predictive vs Prognostic Biomarkers with Claude: Why KRAS G12C Is Not EGFR"
- Source: cancer-research/chapters/05-precision-oncology-matching-therapy-to-tumor.md
- Lane: RESEARCH (Claude assistant)
- Hook: Two patients with the same KRAS G12C mutation get the same targeted drug. One responds for four months then progresses. The other never responds at all. Same biomarker, same drug, two different failures — what does the match actually guarantee?
- The artifact: a sourced comparative brief on two matched therapies — KRAS G12C (sotorasib) vs EGFR exon-19 deletion (osimertinib) — comparing response rate, durability, resistance mechanism, and degree of oncogene addiction; plus a one-sentence generalization about what makes a "good" actionable alteration vs a merely present one — rendered as a Manim three-trajectory plot (durable / transient / non-response) animated from the same starting point.
- Prompt seed: `claude "Compare KRAS G12C inhibition (sotorasib/adagrasib) to EGFR exon-19 deletion inhibition (osimertinib) across four dimensions: (1) response rate in the indicated population, (2) typical durability of response, (3) most common resistance mechanisms, (4) what these differences reveal about relative oncogene addiction. End with a one-sentence claim about what distinguishes a good actionable alteration from a merely present one. Cite published clinical trial data."`
- Read / check: Confirm KRAS G12C response rates (35-40% range) and EGFR response rates (>60%) are correctly cited; verify resistance mechanisms for each are mechanistically accurate; check that the oncogene-addiction explanation is consistent with published biology.
- Human supplies: Nothing — fully synthetic. Both alteration-drug pairs have robust published clinical trial literature.
- Output medium: Manim (three diverging tumor-burden trajectories animated from one starting point: durable descent, V-shape for transient response, flat line for non-response — with alteration name labeled)
- The change: Add a fourth trajectory showing the BRAF V600E story across melanoma vs colorectal cancer — same mutation, radically different response rate — as a demonstration that tissue context modifies even a strong molecular match.
- Teardown angle: The molecular match is a prediction. The response is the test. "Matched" and "responded" are different measurements separated by tumor evolution, co-occurring alterations, and the biology of oncogene dependence.
- Exclusions: Full genomic profiling panel technology; detailed drug mechanism chemistry; history of KRAS drug development before G12C-specific inhibitors.
- Score: 9/10

## Candidate 06 — "Research the Negative Biopsy Problem with Claude: When 'Nothing Found' Doesn't Mean Nothing There"
- Source: cancer-research/chapters/02-cancer-diagnosis-imaging-and-the-tissue-sample.md + Exercise 4
- Lane: RESEARCH (Claude assistant)
- Hook: A biopsy comes back benign. The oncologist considers the case closed. But the imaging still shows 80% pretest probability of malignancy. Should they be reassured?
- The artifact: a sourced research brief: (1) the Bayesian calculation for a pancreatic mass case — pretest 80%, FNA sensitivity 85%, posterior probability after negative result — with the full likelihood-ratio walkthrough, (2) three distinct physical mechanisms by which a needle returns a false negative (miss, unrepresentative zone, insufficient tissue), (3) the clinical decision rule the chapter recommends — rendered as a Manim two-bar before/after chart showing malignancy probability falling from 80% to ~39% but remaining far above the "safe to stop" threshold.
- Prompt seed: `claude "A pancreatic mass has imaging features placing pretest probability of malignancy at 80%. EUS-FNA has sensitivity approximately 85% for solid pancreatic masses. A negative biopsy result is returned. Use a likelihood-ratio approach to compute the posterior probability of malignancy. Then name the three physical mechanisms by which a needle can return a false negative from a true malignancy, and state the clinical decision the chapter's logic supports."`
- Read / check: Verify the Bayesian arithmetic is correct (LR− ≈ 0.176, posterior odds ≈ 0.71, posterior probability ≈ 41%); confirm the three false-negative mechanisms match the chapter exactly; check that the clinical recommendation (repeat core biopsy or MDT) is consistent with published guidelines.
- Human supplies: Nothing — fully synthetic. The Bayesian calculation requires only arithmetic; the clinical guidance is in the published literature.
- Output medium: Manim (two-bar chart: "Pretest" bar at 80% and "After negative biopsy" bar at ~39%, both in vermillion; horizontal reference line at 10% labeled "below this, stop looking"; annotation showing the gap)
- The change: Re-run with pretest probability of 30% (BI-RADS 4A breast lesion) and ask: "At what posterior probability does the chapter's logic support accepting a negative biopsy result?"
- Teardown angle: A negative biopsy does not mean no cancer. It means no cancer was found in this sample. How much that matters depends on how certain you were before the needle went in — and that arithmetic is rarely done at the bedside.
- Exclusions: Endoscopic ultrasound technique details; complete FNA vs core needle biopsy comparison beyond the decision framework; specific complication rates.
- Score: 8/10

## Candidate 07 — "Research Combination Chemotherapy Design Logic with Claude: Why MOPP and R-CHOP Work"
- Source: cancer-research/chapters/10-chemotherapy-principles-and-major-drug-classes.md
- Lane: RESEARCH (Claude assistant)
- Hook: The slogan "chemotherapy kills fast-dividing cells" is mostly true and partly false. It cannot explain why BEP cures testicular cancer or why vincristine is in so many regimens despite being one of the weakest individual agents.
- The artifact: a sourced brief on the three classical rules of combination chemotherapy — different mechanisms, non-overlapping toxicities, single-agent activity — applied to two landmark regimens (MOPP for Hodgkin lymphoma, R-CHOP for DLBCL), explaining why each drug was chosen and what would happen if one rule were violated — rendered as a Manim matrix showing drug class × mechanism × dose-limiting toxicity for each regimen.
- Prompt seed: `claude "The three classical rules for combination chemotherapy are: (1) different mechanisms, (2) non-overlapping dose-limiting toxicities, (3) demonstrated single-agent activity. Apply these rules to MOPP (mechlorethamine, vincristine, procarbazine, prednisone) and R-CHOP (rituximab, cyclophosphamide, doxorubicin, vincristine, prednisone). For each drug in each regimen, identify its mechanism class, its dose-limiting toxicity, and explain what would happen if it were replaced by a drug with the same mechanism as another drug already in the regimen."`
- Read / check: Verify vincristine's minimal myelosuppression claim is accurate; confirm doxorubicin's cumulative cardiomyopathy dose limit is cited correctly (450-550 mg/m²); check that MOPP's historical role as the first curative Hodgkin regimen is accurately described.
- Human supplies: Nothing — fully synthetic. Both regimens have exhaustive published pharmacology and clinical history.
- Output medium: Manim (animated matrix: rows = drug names, columns = mechanism class / toxicity / why it's in the regimen; cells fill in sequentially; color-coding by toxicity organ system)
- The change: Add the carboplatin dosing exception — why is it dosed by AUC using Calvert formula rather than by body surface area, and what does this reveal about the therapeutic window concept made quantitative?
- Teardown angle: Combination chemotherapy is not about hitting harder — it's about hitting differently so that resistance to one mechanism doesn't confer resistance to all others. The design logic behind the regimen is the mechanism of its efficacy.
- Exclusions: Full pharmacokinetics of each agent; secondary malignancy risk beyond etoposide AML mention; history of nitrogen mustard development.
- Score: 8/10

## Candidate 08 — "Research Cancer Staging Logic with Claude: Why TNM + Molecular Modifiers Changed the Story"
- Source: cancer-research/chapters/03-molecular-diagnostics-staging-and-the-liquid-biopsy.md (staging section)
- Lane: RESEARCH (Claude assistant)
- Hook: Two patients have the same T2N0M0 breast cancer. One is classified as Stage IIA. The other, thanks to a genomic test score, is Stage IA. Same anatomy. Different prognosis. Different treatment. What changed?
- The artifact: a sourced brief on TNM staging + AJCC 8th edition prognostic stage modifications, focusing on the breast cancer example (ER/PR, HER2, Oncotype DX integration); includes one specific case showing how anatomic stage and prognostic stage diverge and what treatment decision follows — rendered as a Manim tree: T/N/M dimensions converging to anatomic stage, then molecular modifiers branching off to prognostic stage.
- Prompt seed: `claude "Explain how AJCC 8th edition breast cancer staging incorporates hormone receptor status, HER2, and Oncotype DX recurrence score into prognostic stage groups. Give a specific worked example: a patient with T2N0M0, ER+, HER2-, Oncotype DX score 10. What is her anatomic stage? What is her prognostic stage? What treatment decision does this staging difference change, and what is the clinical utility evidence for the Oncotype DX in this setting?"`
- Read / check: Verify the T2N0M0 / Oncotype DX example yields the correct AJCC 8th ed prognostic stage downgrade; confirm the TAILORx trial is the cited utility evidence; check that the treatment-decision difference (chemotherapy omission) is correctly attributed.
- Human supplies: Nothing — fully synthetic. AJCC 8th edition is publicly available; TAILORx trial results are in published literature.
- Output medium: Manim (convergence tree: T/N/M nodes merging to anatomic stage node; molecular-modifier nodes branching from it to prognostic stage; color-coding showing the downgrade)
- The change: Apply the same framework to prostate cancer — T2cN0M0 with PSA 7 and Gleason 3+4 — and show how the PSA and grade inputs modify anatomic stage to produce a different prognostic stage group.
- Teardown angle: Staging is a vocabulary for comparing populations. The AJCC's decision to incorporate molecular biology into staging is an acknowledgment that anatomy understates how much biology determines what happens to the patient.
- Exclusions: Full TNM lookup tables for all cancer sites; clinical validity evidence for every molecular modifier beyond Oncotype DX; staging for hematologic malignancies.
- Score: 7/10
