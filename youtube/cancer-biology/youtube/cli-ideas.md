# Cancer Biology — CLI Video Ideas ("X with Claude")

---

## Candidate 01 — Research the Hallmarks of Cancer: Are the 2022 Additions Real Hallmarks?
- Source: cancer-biology/chapters/02-introduction-to-cancer-a-disease-of-deregulation.md
- Lane: RESEARCH (Claude assistant)
- Hook: Hanahan added phenotypic plasticity, microbiomes, and senescence to the hallmarks in 2022 — but the chapter flags these as contested. Are they settled science or educated guesses?
- The artifact: a sourced comparison table — original 6 hallmarks vs 2011 additions vs 2022 additions, with a column for "evidence strength" (robust RCT/cohort, preclinical only, proposed) and one for "disputed / contested" drawn from primary literature
- Prompt seed: `claude "Research the 2022 Hallmarks of Cancer additions — phenotypic plasticity, polymorphic microbiomes, and senescent cells. For each, find the strongest supporting evidence and the strongest rebuttal. Produce a comparison table: hallmark | key supporting studies | key challenges | current consensus status"`
- Read / check: verify that cited studies exist and are correctly attributed; check that "contested" flags align with the 2022 Hanahan paper's own hedging language; verify the contrast between the 6 original hallmarks (robust mechanistic evidence) and the newer additions (emerging)
- Human supplies (Claude can't): Nothing — Claude can synthesize from citable primary literature (Hanahan 2022, Cancer Discovery; relevant RCTs and meta-analyses). Fully synthetic output is acceptable for the comparison table.
- Output medium: slate (annotated comparison table rendered as a formatted figure; animate reveal row-by-row with each addition appearing as the narrator reads it)
- The change: ask Claude to add a "what experiment would settle each dispute" column, then read back whether any proposed experiments already exist in the literature
- Teardown angle: the framework keeps growing because it absorbs anomalies rather than resolving them — this is a strength (organized growth) and a weakness (the list has no stopping rule)
- Exclusions: full mechanism of each hallmark, drug development timelines, history of the paper's reception
- Score: 9/10

---

## Candidate 02 — Research BRCA × PARP Synthetic Lethality: Why Does It Work in Some Cancers and Not Others?
- Source: cancer-biology/chapters/06-tumor-suppressor-genes.md
- Lane: RESEARCH (Claude assistant)
- Hook: Venetoclax produces deep remissions in CLL; PARP inhibitors work in BRCA-mutant ovarian cancer. Both exploit synthetic lethality. Yet the same drugs fail in most solid tumors. Why does the same molecular logic work in some contexts and not others?
- The artifact: a sourced synthesis brief — one page covering: (1) clinical contexts where BRCA/PARP synthetic lethality succeeds, (2) documented resistance mechanisms (BRCA reversion mutations, NHEJ upregulation), (3) attempts to extend the concept to other tumor suppressors (ARID1A, CDKN2A/MTAP–PRMT5), with success rates from trials
- Prompt seed: `claude "Research synthetic lethality in cancer therapy: starting from the BRCA/PARP paradigm, find the clinical evidence for its success (olaparib, rucaparib, niraparib approvals), the most common resistance mechanisms, and the three most promising synthetic lethality expansions beyond BRCA. For each expansion, cite the clinical trial status and objective response rates."`
- Read / check: verify FDA approval dates and indications for PARP inhibitors; check that resistance mechanisms cited (BRCA reversion mutations, RAD51 upregulation) match published clinical reports; verify MTAP–PRMT5 as an emerging synthetic lethal pair
- Human supplies (Claude can't): Nothing — all from published clinical literature. Fully synthetic.
- Output medium: Manim (animated two-by-two grid of the synthetic lethality matrix — cells appearing one at a time, then resistance mechanism annotated on the grid, then extensions appearing as new rows)
- The change: add the MTAP–PRMT5 pair and ask Claude to compare the strength of evidence for it versus the original BRCA/PARP pair
- Teardown angle: synthetic lethality is not a drug class — it is a geometric relationship between two vulnerabilities; the translation challenge is finding pairs where the tumor's specific defect aligns with a druggable partner
- Exclusions: detailed mechanism of HR repair, full pharmacology of individual PARP inhibitors, ADC side paths
- Score: 9/10

---

## Candidate 03 — Research Venetoclax: What Is BH3 Profiling and Why Does It Predict Response?
- Source: cancer-biology/chapters/14-apoptosis-in-cancer-evasion-and-restoration.md
- Lane: RESEARCH (Claude assistant)
- Hook: The oncologist in the chapter's opening cannot predict which CLL patient will achieve minimal residual disease negativity on venetoclax. BH3 profiling claims to solve this — but it is not standard of care. Why not?
- The artifact: a sourced brief covering: the BH3 profiling assay (Letai lab method), its predictive performance in published clinical correlatives, regulatory status, and current barriers to routine use; structured as a one-page decision memo a clinician could read
- Prompt seed: `claude "Research BH3 profiling as a predictive biomarker for venetoclax response. What is the assay methodology? What published studies have correlated BH3 profiling results with clinical outcomes in CLL, AML, and other cancers? What are the barriers to routine clinical implementation, and are any clinical trials currently incorporating it as a companion diagnostic?"`
- Read / check: verify the Letai group's seminal publications; check whether any FDA companion diagnostic for venetoclax relies on BH3 profiling; verify CLL and AML response rates in studies that used profiling for patient stratification
- Human supplies (Claude can't): Nothing — fully synthesizable from published literature.
- Output medium: slate (decision-tree diagram: patient arrives → BH3 profiling result → predicted response → clinical action; animate each branch appearing with narration)
- The change: ask Claude whether any analogous functional assay exists for MCL-1 inhibitors, which are the next-generation BH3 mimetics in development
- Teardown angle: the assay works scientifically but requires fresh cells, specialized flow cytometry, and rapid turnaround — the biology is solved, the logistics are not
- Exclusions: full caspase cascade mechanism, navitoclax platelet toxicity history (unless a brief callback)
- Score: 8/10

---

## Candidate 04 — Research Mutational Signatures: What Can a Tumor Genome Tell You About a Patient's Exposure History?
- Source: cancer-biology/chapters/09-cancer-etiology-chemical-and-radiation-carcinogens.md + chapters/04-genetics-and-genomic-instability-in-cancer.md
- Lane: RESEARCH (Claude assistant)
- Hook: A lung adenocarcinoma in a never-smoker has the APOBEC signature instead of the tobacco G→T signature. What does that mean for etiology, prognosis, and treatment — and how reliable is the inference?
- The artifact: a sourced annotation table of 5 major COSMIC mutational signatures — UV, tobacco, APOBEC, MMR-deficiency, aflatoxin — with columns for: dominant mutation type, cancer types it appears in, implied etiology, and whether the signature is actionable for therapy selection
- Prompt seed: `claude "Using the COSMIC Mutational Signatures database and published literature, describe five major mutational signatures: SBS4 (tobacco), SBS7a/b (UV), SBS2/13 (APOBEC), SBS6 (MMR-deficiency), and SBS22 (aflatoxin). For each: what is the dominant mutation spectrum, what cancers carry it, what exposure or process generates it, and does identifying it in a tumor currently change clinical management?"`
- Read / check: verify signature numbers against current COSMIC v3.4 catalog; verify whether MSI-high (SBS6 context) is actually used as a companion diagnostic for pembrolizumab; confirm the aflatoxin TP53 R249S codon specificity
- Human supplies (Claude can't): Nothing — fully synthesizable.
- Output medium: Manim (five-panel bar chart animation — each signature's mutation spectrum drawing in as a distinct fingerprint, with exposure label animating in alongside)
- The change: ask Claude to find a documented case where mutational signature analysis changed a patient's treatment plan — for example, a never-smoker found to have the tobacco signature from secondhand exposure
- Teardown angle: signatures read the past but are imperfect predictors of the future — they tell you what happened to the cell, not which current oncogene is driving it
- Exclusions: full COSMIC catalog (only 5 signatures), history of the Alexandrov 2013 paper, sequencing technology details
- Score: 8/10

---

## Candidate 05 — Research the Warburg Effect: Is Glucose Aerobic Glycolysis a Therapeutic Vulnerability?
- Source: cancer-biology/chapters/15-cancer-metabolism-the-warburg-effect-and-glucose.md
- Lane: RESEARCH (Claude assistant)
- Hook: The PET scan glows bright where cancer is because tumors gulp glucose 10x faster than normal tissue. But cancer cells are not bad at energetics — they are solving a biosynthesis problem. Forty years of trying to drug this have mostly failed. Why?
- The artifact: a sourced evidence brief — a timeline of Warburg-targeting drug attempts (2-DG, lonidamine, dichloroacetate, HIF-1α inhibitors, IDH inhibitors) with response rates and failure reasons; followed by a "what actually works" section on IDH inhibitors in leukemia as the successful narrow case
- Prompt seed: `claude "Research the clinical history of attempts to target the Warburg effect in cancer therapy. Cover: 2-deoxyglucose, dichloroacetate, HIF-1alpha inhibitors. For each, find the most advanced clinical trial, the reported response rates, and the stated reason for failure or limited efficacy. Then contrast with IDH inhibitors (ivosidenib, enasidenib) as the successful narrow case — what made those work when the broader Warburg-targeting approach did not?"`
- Read / check: verify 2-DG clinical trial results (phase I/II); verify DCA clinical evidence in brain tumors; verify ivosidenib approval indication and overall response rate in AML; confirm that HIF-1α inhibitors have not produced an approved oncology indication
- Human supplies (Claude can't): Nothing — fully synthesizable.
- Output medium: Remotion (timeline animation — drug attempts appearing chronologically along a horizontal axis, with response rate annotations; IDH inhibitors appearing at the end as the exception that proves the rule)
- The change: ask Claude to identify which current clinical trials targeting aerobic glycolysis show the highest response rates, and assess whether any might replicate the IDH inhibitor pattern
- Teardown angle: the Warburg effect is real but too universal to be selectively toxic — every proliferating cell (including gut epithelium and bone marrow) uses it, which narrows the therapeutic window to near zero for broad glycolysis inhibitors
- Exclusions: full biochemistry of the citric acid cycle, NADPH metabolism details, HIF detailed mechanism
- Score: 8/10

---

## Candidate 06 — Research Knudson's Two-Hit Hypothesis: How Did Mathematics Precede Molecular Evidence by 16 Years?
- Source: cancer-biology/chapters/04-genetics-and-genomic-instability-in-cancer.md + chapters/06-tumor-suppressor-genes.md
- Lane: RESEARCH (Claude assistant)
- Hook: In 1971, Alfred Knudson deduced from patient statistics alone — without sequencing, without molecular biology — that retinoblastoma requires two hits in the same gene. The molecule was cloned 16 years later and confirmed his prediction exactly. How does statistical logic without molecular evidence produce a correct mechanistic prediction?
- The artifact: a sourced reconstruction — the original 1971 Knudson PNAS argument laid out step by step, the 1987 RB1 cloning result, and a summary of how many other hereditary cancer syndromes the two-hit model subsequently predicted correctly (BRCA1/2, APC, VHL, TP53-Li Fraumeni)
- Prompt seed: `claude "Reconstruct Knudson's 1971 two-hit hypothesis argument from his original PNAS paper. What were his data inputs, what mathematical model did he apply, and what did he predict? Then list five hereditary cancer syndromes where the two-hit mechanism was subsequently confirmed at the molecular level, with the year of confirmation and the gene involved."`
- Read / check: verify the 1971 Knudson PNAS paper citation; check the 1986/87 RB1 cloning papers; verify that BRCA1 and BRCA2 conform to the two-hit model (they mostly do, with PTEN as the documented exception for haploinsufficiency)
- Human supplies (Claude can't): Nothing — fully synthesizable.
- Output medium: slate (a two-panel comparison — Knudson's statistical inference diagram on the left, the subsequent molecular confirmations listed chronologically on the right; panels animate in sequence)
- The change: ask Claude to explain the PTEN haploinsufficiency exception and whether it undermines or refines the two-hit model
- Teardown angle: the predictive power came from reasoning about probability distributions across populations, not individual molecular measurements — a reminder that mathematical epidemiology can outrun bench biology by decades
- Exclusions: full RB mechanism, p16/CDK4/6 pathway, synthetic lethality implications
- Score: 8/10

---

## Candidate 07 — Research the MGMT Methylation Biomarker: A Predictive Epigenetic Mark That Flips the Intuition
- Source: cancer-biology/chapters/07-epigenetics-in-cancer-the-methylation-and-histone-code.md
- Lane: RESEARCH (Claude assistant)
- Hook: In glioblastoma, patients whose tumor has a silenced repair gene live longer on temozolomide than patients whose repair gene is active. A broken repair system is an advantage for the patient — and the test for it is a methylation pattern, not a mutation. This counterintuitive result is now standard clinical practice.
- The artifact: a sourced clinical brief — MGMT methylation status in GBM, its predictive (not prognostic) value, the methylation-specific PCR test used clinically, and the frequency in the GBM patient population; then the question: should patients with unmethylated MGMT skip temozolomide?
- Prompt seed: `claude "Research the clinical significance of MGMT promoter methylation in glioblastoma. Specifically: What fraction of GBM patients have MGMT methylation? What is the difference in survival for methylated versus unmethylated patients receiving temozolomide? Is there evidence that unmethylated patients should receive alternative therapy instead? What clinical trials have addressed this? Distinguish predictive from prognostic value."`
- Read / check: verify MGMT methylation frequency (~40-45% of GBM); verify the Hegi 2005 NEJM pivotal study finding; confirm the distinction between predictive and prognostic biomarker as applied to this case; check whether any guideline now recommends withholding temozolomide in unmethylated GBM
- Human supplies (Claude can't): Nothing — fully synthesizable.
- Output medium: Manim (decision-tree animation — patient diagnosed → MGMT test → methylated branch (drug works) → unmethylated branch (drug wasted); branches animate with survival data appearing alongside)
- The change: ask Claude to find current clinical trials testing alternative or intensified regimens specifically for MGMT-unmethylated GBM
- Teardown angle: the counterintuitive lesson is that a broken repair gene helps the drug work — this generalizes to other contexts where tumor vulnerabilities can be exploited rather than repaired
- Exclusions: full chromatin code, HDAC inhibitors as a broader class, IDH mechanism
- Score: 8/10

---

## Candidate 08 — Research HPV Vaccination vs Cervical Cancer Elimination: How Close Is Australia?
- Source: cancer-biology/chapters/10-cancer-etiology-viral-and-bacterial-carcinogens.md
- Lane: RESEARCH (Claude assistant)
- Hook: Australia vaccinated adolescents against HPV at near-universal rates starting in 2007. They claim they are on track to eliminate cervical cancer as a public health problem within a generation. Is that true, and what does "elimination" actually mean?
- The artifact: a sourced evidence brief — Australian HPV vaccination coverage rates, the observed decline in vaccine-type HPV prevalence, the projected timeline to WHO cervical cancer elimination threshold (<4 cases per 100,000 per year), and a comparison with countries at low vaccination coverage
- Prompt seed: `claude "Research the Australian HPV vaccination program and its projected impact on cervical cancer. What is the current vaccination coverage, how has vaccine-type HPV prevalence changed in vaccinated cohorts, what does WHO define as cervical cancer elimination, and what is the projected year Australia will reach that threshold? Compare Australia with a comparable country that has low HPV vaccination coverage."`
- Read / check: verify Australian coverage rates from the national immunization program data; check the WHO elimination threshold (<4/100,000); verify published HPV prevalence declines in vaccinated cohorts (should show ~80-90% reduction in vaccine types); confirm the Nature Medicine 2019 Lew et al. projection paper
- Human supplies (Claude can't): Nothing — fully synthesizable from published public health literature.
- Output medium: Remotion (two animated trend lines — HPV-16/18 prevalence in Australia dropping vs. a comparison country; a projected line continuing to the elimination threshold date)
- The change: ask Claude what would happen to the elimination projection if HPV vaccination rates drop below a herd immunity threshold, and what that threshold is estimated to be
- Teardown angle: "elimination" is a public health definition, not zero cases — and the timeline is a projection that depends on sustained vaccination coverage across future cohorts; the biology is solved but the policy must hold
- Exclusions: full HPV E6/E7 mechanism, other HPV-driven cancers (focus on cervical), vaccine hesitancy policy details beyond one mention
- Score: 8/10

---

## Candidate 09 — Research IDH Mutations and Epigenetic Reprogramming: How a Metabolic Error Locks Leukemia Cells
- Source: cancer-biology/chapters/07-epigenetics-in-cancer-the-methylation-and-histone-code.md
- Lane: RESEARCH (Claude assistant)
- Hook: A single amino acid change in a metabolic enzyme produces a cancer-causing chemical that silences genes across the genome — and a drug that reverses a metabolic error can reverse an epigenetic state accumulated over years. This is the clearest proof that cancer epigenetics is pharmacologically reversible.
- The artifact: a sourced causal-chain brief — IDH1/2 mutation → 2-hydroxyglutarate production → TET and histone demethylase inhibition → hypermethylation → differentiation block; then the clinical reversal: ivosidenib/enasidenib reducing 2HG → differentiation resuming → leukemic blasts maturing; with response rates from the approval trials
- Prompt seed: `claude "Trace the complete causal chain from IDH1/IDH2 mutation to epigenetic phenotype in AML and glioma, citing primary literature at each step. Then research the clinical evidence for ivosidenib and enasidenib: what are the overall response rates in IDH-mutant AML from the pivotal trials, and what cellular evidence confirms that the epigenetic reversal mechanism (not just cytotoxicity) is responsible?"`
- Read / check: verify IDH1 R132 and IDH2 R140/R172 as the canonical cancer mutations; verify 2HG inhibition of TET2 and KDM histone demethylases; verify ivosidenib FDA approval and ORR from the AG-120-C-001 trial; check that differentiation syndrome is a documented on-target toxicity confirming the mechanism
- Human supplies (Claude can't): Nothing — fully synthesizable.
- Output medium: Manim (horizontal causal chain animation — each node appearing left to right: mutant IDH → 2HG (oncometabolite) → blocked demethylases → methylation accumulates → differentiation locked; then a reversal animation showing the inhibitor restoring the chain)
- The change: ask Claude whether the IDH inhibitor model generalizes — are there other oncometabolites that block epigenetic enzymes and could similarly be reversed?
- Teardown angle: the drug works by removing the cause of the methylation (the oncometabolite), not by reversing the methylation directly — this is why it works when generic demethylating agents have failed
- Exclusions: full TCA cycle biochemistry, succinate/fumarate as oncometabolites (brief mention only), chromatin remodeler mutations as a separate category
- Score: 9/10

---

## Candidate 10 — Research Checkpoint Immunotherapy Response Rates: Why Do Hot Tumors Respond and Cold Tumors Not?
- Source: cancer-biology/chapters/02-introduction-to-cancer-a-disease-of-deregulation.md (hallmarks — evading immune destruction)
- Lane: RESEARCH (Claude assistant)
- Hook: Anti-PD-1 works in 65-75% of Hodgkin lymphoma and under 5% of pancreatic cancer. These are both "cancer" — what biological difference produces a 15-fold difference in response rate, and is it addressable?
- The artifact: a sourced comparison table — 6 cancer types ranked by checkpoint inhibitor single-agent response rate, with columns for: TMB (tumor mutational burden), PD-L1 expression, CD8+ infiltration status (hot/cold/excluded), and the dominant resistance mechanism for non-responders
- Prompt seed: `claude "Compile published single-agent anti-PD-1 or anti-PD-L1 response rates across six cancer types: Hodgkin lymphoma, melanoma, MSI-high colorectal, NSCLC (PD-L1 high), triple-negative breast cancer, and pancreatic adenocarcinoma. For each, also report: median TMB, typical PD-L1 expression level, immune phenotype (hot/excluded/cold), and the leading proposed reason for non-response. Cite the pivotal trial or meta-analysis for each response rate."`
- Read / check: verify Hodgkin response rate (~65-87% ORR with anti-PD-1); verify pancreatic adenocarcinoma ORR (<5%); verify MSI-high colorectal as the tumor-agnostic pembrolizumab approval basis; check that TMB correlates imperfectly with response (Hodgkin is TMB-low but responds because of viral EBV or specific PD-L1 amplification)
- Human supplies (Claude can't): Nothing — fully synthesizable.
- Output medium: Manim (horizontal bar chart drawing in with bars ordered from highest to lowest ORR; color-coded by immune phenotype; a secondary axis showing TMB)
- The change: ask Claude to find whether any "cold-to-hot" conversion strategy (STING agonists, oncolytic viruses, radiation before checkpoint blockade) has moved the response rate in pancreatic cancer in a phase 2 trial
- Teardown angle: TMB and PD-L1 are correlates, not causes — the mechanistic driver is whether T cells were ever primed against tumor-specific antigens and whether the tumor is suppressing them with a mechanism the drug can reverse
- Exclusions: CAR-T therapy, full NK cell biology, detailed Treg mechanism
- Score: 8/10

---

## Candidate 11 — Research RAS Undruggability: Why Did It Take 40 Years to Drug the Most Common Oncogene?
- Source: cancer-biology/chapters/05-oncogenes.md
- Lane: RESEARCH (Claude assistant)
- Hook: KRAS is mutated in 30% of all human cancers and nearly 90% of pancreatic cancers. For 40 years it was "undruggable." Sotorasib appeared in 2021 for KRAS G12C. Why did one specific mutation finally yield — and why does the most common KRAS mutation, G12D in pancreatic cancer, still not have an approved drug?
- The artifact: a sourced brief covering: why RAS was classified undruggable (high GTP affinity, no obvious pocket), the chemistry that made G12C covalent inhibition possible (the reactive cysteine), sotorasib and adagrasib response rates in NSCLC, and the status of KRAS G12D inhibitor programs as of 2026
- Prompt seed: `claude "Research the history and current status of KRAS-targeted therapy. Specifically: what structural features of wild-type KRAS made it undruggable for 40 years, what chemical insight enabled the G12C covalent inhibitors (sotorasib, adagrasib), what are their clinical response rates in NSCLC from the CodeBreaK 100 and KRYSTAL-1 trials, and what is the current clinical development status of KRAS G12D inhibitors?"`
- Read / check: verify the covalent allosteric mechanism of sotorasib targeting the switch-II pocket; verify ORR ~37% for sotorasib in CodeBreaK 100; verify G12C mutation frequency in NSCLC vs. pancreatic cancer; verify that no G12D inhibitor has phase 3 approval as of 2026
- Human supplies (Claude can't): Nothing — fully synthesizable.
- Output medium: Remotion (timeline animation — 1982 (KRAS discovered), 2021 (sotorasib approved), 2022 (adagrasib), then a dotted projected line toward potential G12D approval with trial status annotations)
- The change: ask Claude to identify the key difference in chemical strategy required to target G12D versus G12C, and whether any G12D programs have reported phase 2 data
- Teardown angle: the reactive cysteine was an accident of the specific mutation — the G12C drug works because one nucleotide change in the codon created a unique chemical handle that G12D lacks; selectivity came from chemistry meeting mutation, not from choosing the most biologically important variant
- Exclusions: full RAS-RAF-MEK-ERK cascade, RAF/MEK inhibitor combinations, pancreatic cancer biology
- Score: 8/10

---

## Candidate 12 — Research Cancer Epidemiology and the Beta-Carotene False Positive: When Observational Data Lies
- Source: cancer-biology/chapters/03-cancer-epidemiology-and-risk-factors.md
- Lane: RESEARCH (Claude assistant)
- Hook: In the 1980s, consistent observational data showed that people who ate foods rich in beta-carotene had lower lung cancer rates. Supplements were developed. The randomized trials showed supplements increased lung cancer risk by 17-28% in smokers. The association had been entirely backwards. How does this happen and what does it teach us about reading cancer epidemiology?
- The artifact: a sourced reconstruction of the Bradford Hill analysis for the beta-carotene case — which criteria appeared satisfied from observational data, which criterion the trials addressed (experiment), and why the confounding pattern (healthy user bias + confounding by overall diet) produced a false directional effect; plus a short list of 3 other cancer epidemiology reversals
- Prompt seed: `claude "Research the beta-carotene and lung cancer epidemiology case study. What were the ATBC and CARET trial designs, what was the observed increase in lung cancer risk in supplement users, and what type of confounding explains why the observational signal was backwards? Then identify two other examples in cancer epidemiology where a plausible, replicated observational association failed to survive a randomized trial."`
- Read / check: verify ATBC (1994 NEJM) and CARET trial (1996 NEJM) findings; verify the ~17-28% increased lung cancer risk in smokers; confirm that the proposed mechanism is healthy-user confounding; verify that the Bradford Hill "experiment" criterion is the one that catches this class of error
- Human supplies (Claude can't): Nothing — fully synthesizable.
- Output medium: Manim (Bradford Hill checklist animation — criteria appearing one by one with checkmarks for observational data, then the "Experiment" criterion appearing last with a red X and the reversed finding annotated)
- The change: ask Claude to find the current consensus on whether vitamin D supplementation and cancer risk follows the same epidemiological pattern — plausible association from observational data but trials failing to confirm
- Teardown angle: the "experiment" criterion exists because confounding can satisfy every other Bradford Hill criterion — the observational data was not wrong, just misinterpreted; causation and correlation both produce consistent, plausible, strong associations
- Exclusions: full Bradford Hill list as a tutorial (focus on the reversal), alcohol epidemiology details, obesity mechanism
- Score: 8/10
