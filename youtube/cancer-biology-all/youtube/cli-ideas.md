# Cancer Biology All (Comprehensive) — CLI Video Ideas ("X with Claude")

## Candidate 01 — Research the Adaptive Therapy Revolution: Can We Manage Cancer Like a Chronic Disease?
- Source: cancer-biology-all/chapters/24-tumor-heterogeneity-and-clonal-evolution.md
- Lane: RESEARCH (Claude assistant)
- Hook: Standard oncology tries to kill every cancer cell. Adaptive therapy deliberately leaves sensitive cells alive — to out-compete the resistant ones. The Moffitt abiraterone trial doubled time-to-progression. Why isn't every oncologist doing this?
- The artifact: a sourced comparison brief — standard maximum-dose therapy vs. adaptive therapy — organized as a 4-column table (rationale | clinical evidence | practical barriers | cancer types where it fits best), animated as a Remotion panel reveal, with the abiraterone trial data plotted as a progression-free survival comparison.
- Prompt seed: `claude "Research adaptive therapy in cancer: what is the evolutionary rationale (Gatenby framework), what clinical evidence exists (the abiraterone prostate cancer trial, other cancers), what are the practical barriers to adoption, and in what specific settings is it most likely to outperform continuous dosing? Synthesize from citable published sources."`
- Read / check: verify the Gatenby abiraterone trial result (2017, Zhang et al.), confirm adaptive therapy trials underway in other cancers, check whether any have proceeded to phase 3; confirm the competitive suppression mechanism is accurately stated.
- Human supplies (Claude can't): Nothing — fully synthetic. Claude can synthesize from published literature (Gatenby papers, MSKCC trial data, review articles). A screen-recording of a Claude conversation enriches the terminal beat.
- Output medium: Remotion (animated 4-column table reveal + survival curve comparison panel)
- The change: ask Claude to identify the three specific cancers where adaptive therapy is most likely to succeed and explain why each fits the evolutionary prerequisite (pre-existing heterogeneous resistance).
- Teardown angle: the evolutionary mismatch — we apply drugs like antibiotics (maximum tolerated dose) to a problem that behaves like ecosystem management (population dynamics). The science has the right model; the clinical infrastructure doesn't yet.
- Exclusions: mathematical game theory details, all individual drug mechanisms beyond abiraterone, history of chemotherapy dosing philosophy.
- Score: 9/10

## Candidate 02 — Research CAR-T Cells: Why They Cure Leukemia but Stall at Solid Tumors
- Source: cancer-biology-all/chapters/44-cellular-therapies-vaccines-and-cytokines.md
- Lane: RESEARCH (Claude assistant)
- Hook: CAR-T achieves 70-90% complete response in relapsed pediatric leukemia — diseases that were once terminal. The same approach barely registers in lung, breast, or pancreatic cancer. The cells are engineered the same way. What's so different?
- The artifact: a sourced side-by-side comparison brief — hematologic CAR-T (B-ALL/DLBCL/myeloma) vs. solid tumor CAR-T — structured as five biological obstacles (antigen heterogeneity, on-target/off-tumor toxicity, TME suppression, T cell exhaustion, matrix penetration), with approval timeline animated as a Manim horizontal bar chart (year vs. indication).
- Prompt seed: `claude "Research why CAR-T cell therapy has been transformative for B-cell malignancies but has largely failed in solid tumors. For each of the five major biological barriers (antigen heterogeneity, on-target/off-tumor toxicity, immunosuppressive TME, T cell exhaustion, matrix penetration), explain the mechanism and what engineering approaches are being tried. Include the FDA-approved indications and response rates."`
- Read / check: confirm FDA approval dates and response rates for tisagenlecleucel, axicabtagene ciloleucel, ide-cel, cilta-cel; verify no solid tumor CAR-T is FDA-approved as of 2026; confirm early signals in claudin 18.2 and GD2 indications.
- Human supplies (Claude can't): Nothing — fully synthetic. All information is drawn from FDA labels, published trials, and review articles accessible to Claude.
- Output medium: Manim (animated bar chart of approvals by year/indication) + Remotion (five-barrier comparison panel)
- The change: ask Claude to identify which solid tumor CAR-T target has the most credible clinical signal as of 2026 and explain why it partially overcomes the barriers.
- Teardown angle: CAR-T is the proof that immunity can be engineered — the design question is whether solid tumor biology is an engineering problem (add more features to the CAR) or a fundamental access problem (the tumor microenvironment wins regardless of T cell quality).
- Exclusions: full CAR-T manufacturing process details, neurotoxicity management protocols, TCR-T therapy details.
- Score: 9/10

## Candidate 03 — Research the Clonal Evolution of Drug Resistance: Can We Predict It Before It Happens?
- Source: cancer-biology-all/chapters/24-tumor-heterogeneity-and-clonal-evolution.md   (+ LLM Exercise)
- Lane: RESEARCH (Claude assistant)
- Hook: Every patient on a targeted cancer therapy develops resistance. The resistant cells were there at the start — too rare to detect. By the time we see resistance, we've already lost the selection battle. Can we predict and pre-empt it?
- The artifact: a sourced resistance playbook for EGFR-mutant non-small-cell lung cancer — three resistance mechanisms (T790M mutation, MET amplification, small-cell transformation), each with molecular basis, diagnostic detection method, and treatment option — rendered as an animated Manim decision tree (ASK → treat → resistance mechanism → detection → next therapy).
- Prompt seed: `claude "Research resistance to osimertinib in EGFR-mutant non-small-cell lung cancer. What are the three most common resistance mechanisms (T790M on osimertinib is less relevant — focus on C797S, MET amplification, histologic transformation), their molecular basis, how each is detected (ctDNA, tissue, FISH), and what subsequent treatments exist for each. Build a clinical decision tree for managing acquired resistance."`
- Read / check: verify resistance mechanism frequencies (C797S vs. MET amplification vs. small-cell transformation), confirm available treatments for each mechanism, check whether any head-to-head comparisons of subsequent therapies exist.
- Human supplies (Claude can't): Nothing — fully synthetic. All resistance mechanisms are documented in published literature; Claude synthesizes.
- Output medium: Manim (animated clinical decision tree — EGFR inhibitor → resistance branch → detection → next therapy)
- The change: ask Claude to compare how ctDNA (liquid biopsy) and tissue re-biopsy perform at detecting each resistance mechanism — sensitivity, lead time, and clinical implications.
- Teardown angle: resistance is not treatment failure — it is an evolutionary prediction that clinicians can learn to anticipate. The clonal tree is always branching; the question is whether we can read the branches before they expand.
- Exclusions: full pharmacology of each subsequent therapy, comprehensive list of all known resistance mutations, statistical modeling of resistance emergence.
- Score: 9/10

## Candidate 04 — Research ctDNA Minimal Residual Disease: The Blood Test That Sees Cancer Before Imaging Can
- Source: cancer-biology-all/chapters/24-tumor-heterogeneity-and-clonal-evolution.md   (+ LLM Exercise)
- Lane: RESEARCH (Claude assistant)
- Hook: After surgery for colorectal cancer, the scan is clean. But a ctDNA blood test taken six weeks later is positive. That patient will almost certainly relapse within two years — and the ctDNA-negative patient probably won't. We now have a biomarker that sees micrometastatic disease that imaging can't touch. Should every patient get it?
- The artifact: a sourced evidence summary on ctDNA-based MRD detection — organized by cancer type (colorectal, breast, lung), with evidence level, leading trials, current clinical availability, and decision impact — animated as a Remotion matrix (cancer type × evidence level × action) filling cell by cell.
- Prompt seed: `claude "Research ctDNA-based minimal residual disease (MRD) detection in cancer. For colorectal, breast, and lung cancer: what is the evidence that ctDNA MRD predicts recurrence, what are the landmark trials (GALAXY, DYNAMIC, others), is ctDNA-guided adjuvant decision-making standard of care yet, and what are the limitations (sensitivity at low tumor fractions, assay differences)?"`
- Read / check: verify GALAXY trial result in colorectal, confirm DYNAMIC trial design, check whether ctDNA-guided de-escalation or escalation of adjuvant therapy has shown a survival benefit (not just prognostic signal), confirm FDA regulatory status.
- Human supplies (Claude can't): Nothing — fully synthetic. All trial data is published and citable.
- Output medium: Remotion (animated matrix — cancer type × evidence strength × clinical action)
- The change: ask Claude to compare ctDNA MRD, CEA (the old standard), and imaging (CT) for post-surgical surveillance in colorectal cancer — sensitivity, lead time, cost, and current guideline recommendations.
- Teardown angle: the distinction between prognostic (knowing who will relapse) and predictive (using that knowledge to change care). ctDNA MRD is proven prognostic in several cancers; it is still proving predictive. The gap between "this patient is high risk" and "here is the clinical action that helps" is where trials are running right now.
- Exclusions: multi-cancer early detection (a different application), the technical sequencing methodology, comprehensive list of all ctDNA assays.
- Score: 9/10

## Candidate 05 — Research Personalized Neoantigen Vaccines: Engineering an Immune Response to Your Own Cancer
- Source: cancer-biology-all/chapters/44-cellular-therapies-vaccines-and-cytokines.md
- Lane: RESEARCH (Claude assistant)
- Hook: Every cancer has mutations. Some of those mutations produce abnormal proteins that the immune system can learn to recognize. Sequence the tumor, predict the targets, manufacture a vaccine — in weeks — specific to that patient's cancer. The mRNA-4157 melanoma trial showed it works. Can this scale?
- The artifact: a sourced brief tracing the neoantigen vaccine pipeline — sequencing → computational neoantigen prediction → manufacturing → clinical results — covering the mRNA-4157 trial (Moderna/Merck), current phase 3 expansion, and comparison with shared-antigen vaccines (sipuleucel-T), rendered as a Remotion pipeline animation (steps filling left to right with evidence callouts).
- Prompt seed: `claude "Research personalized neoantigen cancer vaccines. Walk through the complete technical pipeline (tumor sequencing → neoantigen prediction algorithms → manufacturing platforms — mRNA, peptide, DNA). What did the mRNA-4157 melanoma phase 2 trial show, what are the phase 3 trials now underway, and in which cancer types are personalized vaccines most likely to benefit patients? Compare with sipuleucel-T as the historical baseline."`
- Read / check: confirm mRNA-4157 (BNT122) recurrence-free survival benefit in adjuvant melanoma, verify phase 3 trial names and cancer types, confirm current manufacturing turnaround time (weeks, not months), verify neoantigen prediction algorithm performance metrics cited.
- Human supplies (Claude can't): Nothing — fully synthetic. All published trial data and pipeline information is accessible.
- Output medium: Remotion (animated pipeline — sequencing → prediction → manufacturing → trial results → current status)
- The change: ask Claude to identify the three tumor types where personalized neoantigen vaccines are most likely to succeed and explain why each has the right immunological prerequisites (mutation burden, immunogenicity, checkpoint inhibitor synergy).
- Teardown angle: the engineering reversal — instead of making a drug that fights cancer, you are making cancer's own mutations into a weapon against itself. The bottleneck is no longer biology; it is manufacturing speed and cost at scale.
- Exclusions: full immune checkpoint inhibitor mechanism, all historical cancer vaccine failures, mRNA manufacturing chemistry details.
- Score: 8/10

## Candidate 06 — Research the Metastatic Cascade: Why 99.99% of Cancer Cells That Enter the Bloodstream Never Succeed
- Source: cancer-biology-all/chapters/20-metastasis-the-seed-and-the-soil.md   (+ LLM Exercise)
- Lane: RESEARCH (Claude assistant)
- Hook: A primary tumor sheds millions of cells into the bloodstream per day. Almost none of them form metastases. The cells that do kill 90% of cancer patients. Metastasis is the most important question in cancer — and the bottleneck is not invasion but survival.
- The artifact: a sourced bottleneck map of the metastatic cascade — seven steps (intravasation → circulation → arrest → extravasation → micrometastasis → macrometastasis), with estimated attrition at each step and the one therapeutic approach targeting each — animated as a Manim funnel (population shrinking at each stage).
- Prompt seed: `claude "Research the metastatic cascade: the seven stages from intravasation to macrometastasis. At each stage, what fraction of cells successfully advance (best available estimates), what kills the cells that fail, and what therapeutic strategies have been tried at that step? Focus on the biology of circulating tumor cell survival, the pre-metastatic niche, and dormancy-reactivation."`
- Read / check: confirm the ~0.01% CTC-to-metastasis estimate, verify the TMEM (tumor microenvironment of metastasis) evidence, confirm that anti-angiogenic drugs target the macrometastasis step, verify bisphosphonate mechanism at the bone colonization step.
- Human supplies (Claude can't): Nothing — fully synthetic. All published cascade biology and therapeutic data is accessible.
- Output medium: Manim (animated funnel — cell population shrinking through seven cascade steps)
- The change: ask Claude to explain why CTC clusters are 30-100× more efficient at metastasis than single CTCs — the biological reasons — and what therapeutic strategies could specifically target clustering.
- Teardown angle: Paget's seed-and-soil hypothesis from 1889 was right — organ-specific metastasis reflects molecular compatibility between cancer cell and target organ microenvironment. The biology vindicated a Victorian pathologist's autopsy statistics; now the challenge is interrupting the crosstalk before the colony establishes.
- Exclusions: full treatment protocols for established bone/brain/liver metastasis, surgical metastasectomy details, comprehensive list of anti-metastatic drug failures.
- Score: 8/10

## Candidate 07 — Research Cancer Dormancy: The 15-Year Recurrence No One Can Explain
- Source: cancer-biology-all/chapters/20-metastasis-the-seed-and-the-soil.md
- Lane: RESEARCH (Claude assistant)
- Hook: A breast cancer patient finishes treatment and is declared disease-free. Fifteen years later, she develops bone metastases from the same cancer. The cells were there the whole time — dormant, invisible, waiting. What wakes them up?
- The artifact: a sourced mechanistic brief on cancer dormancy — three mechanisms (cellular dormancy via G0 arrest, angiogenic dormancy via balanced proliferation/death, immune dormancy via T cell/NK suppression), with the clinical evidence for each and the therapeutic implications — animated as a Remotion three-panel comparison (mechanism × evidence × therapeutic target).
- Prompt seed: `claude "Research cancer cell dormancy in metastasis. Explain the three main mechanisms — cellular dormancy (G0 arrest), angiogenic dormancy (balanced proliferation and apoptosis), and immune dormancy (immune surveillance suppression). For each: the molecular signals, the cancer types where it is best documented, the trigger that ends dormancy, and the therapeutic strategies being tested (maintain vs. disrupt approaches)."`
- Read / check: verify that breast cancer bone marrow dormancy is the best-documented case, confirm the angiogenic switch concept (Folkman), verify that immune dormancy connects to the immunoediting equilibrium phase, check whether any clinical trial has successfully targeted dormancy.
- Human supplies (Claude can't): Nothing — fully synthetic. Published dormancy biology and adjuvant therapy rationale are accessible.
- Output medium: Remotion (three-panel animated comparison — mechanism × evidence × clinical strategy)
- The change: ask Claude to explain why the same dormancy question appears in both metastasis biology (late recurrence) and immunotherapy (acquired resistance after durable response) — what is the common mechanism, and is targeting dormancy a single unified problem?
- Teardown angle: the clinical paradox of dormancy — we call it "cure" when we mean "dormancy we haven't detected yet." Adjuvant therapy works partly by killing dormant disseminated cells. The question is whether we can maintain dormancy indefinitely rather than trying to detect and kill every last cell.
- Exclusions: MRD/ctDNA detection methodology, full adjuvant chemotherapy protocols, the full metastatic cascade beyond dormancy.
- Score: 8/10

## Candidate 08 — Research Tumor Heterogeneity: Why Every Biopsy Tells a Different Story
- Source: cancer-biology-all/chapters/24-tumor-heterogeneity-and-clonal-evolution.md   (+ LLM Exercise)
- Lane: RESEARCH (Claude assistant)
- Hook: A surgeon takes a biopsy from one side of the tumor. A geneticist sequences it. They pick a targeted therapy. But the mutation driving treatment choice exists in only 40% of the tumor. The other 60% was never tested. This is the TRACERx problem — and it is why targeted therapies almost always fail eventually.
- The artifact: a sourced brief on the TRACERx lung cancer study — what spatial heterogeneity was found, how the clonal tree was reconstructed from multi-region biopsies, what the implications are for single-biopsy clinical practice, and how liquid biopsy partly addresses the problem — rendered as a Manim animated clonal tree (trunk → branches → subclones, with sampling strategy overlaid).
- Prompt seed: `claude "Research the TRACERx lung cancer study (Charles Swanton, UCL/Francis Crick). What did multi-region sequencing reveal about spatial heterogeneity in lung adenocarcinoma? Explain trunk vs. branch mutations, subclonal driver mutations, and what happened at relapse. What are the implications for standard single-biopsy clinical practice, and how does liquid biopsy (ctDNA) complement or replace multi-region tissue sampling?"`
- Read / check: verify TRACERx founding publication (Jamal-Hanjani, NEJM 2017) and key follow-up papers, confirm the fraction of driver mutations that are subclonal vs. clonal, verify that ctDNA provides a more representative sampling than single biopsy, check whether TRACERx data changed any clinical guidelines.
- Human supplies (Claude can't): Nothing — fully synthetic. TRACERx is published in NEJM and Nature; Claude synthesizes.
- Output medium: Manim (animated clonal tree — trunk mutations shared by all cells, branches showing subclonal divergence, sampling bias illustrated)
- The change: ask Claude to explain the concept of subclonal driver mutations and why a targeted therapy against a subclonal driver (present in 20% of cells) produces a more limited response and faster resistance than a therapy against a clonal driver.
- Teardown angle: the biopsy problem is an information problem — one needle in one region of a tumor produces a partial view of an evolving population. Treatment decisions based on that partial view are predictably incomplete. The solution is either more biopsies (TRACERx approach) or a different sampling strategy (liquid biopsy integrates the whole tumor).
- Exclusions: full mathematical models of clonal evolution, comprehensive list of all subclonal drivers in lung cancer, epigenetic heterogeneity details.
- Score: 8/10

## Candidate 09 — Research Clinical Trial Design in Oncology: Why PFS Is a Surrogate That Sometimes Lies
- Source: cancer-biology-all/chapters/49-clinical-trial-phases-and-design.md   (+ LLM Exercise)
- Lane: RESEARCH (Claude assistant)
- Hook: A cancer drug wins FDA approval showing it delays progression by 2.5 months on a CT scan. Three years later, the same drug fails to improve survival. The patients lived just as long whether they took it or not. This is the PFS-to-OS surrogate endpoint problem — and it happens more often than the public knows.
- The artifact: a sourced analysis of surrogate endpoint validity in cancer trials — when PFS predicts OS and when it doesn't — organized by cancer type and drug class, with specific examples of PFS benefit that failed to translate to OS benefit, rendered as a Remotion 2×2 matrix animation (PFS benefit × OS translation: validated / not validated).
- Prompt seed: `claude "Research the surrogate endpoint problem in cancer clinical trials. When does progression-free survival reliably predict overall survival, and when does it not? Provide specific examples of PFS benefits that failed to show OS benefit. Explain the FDA's criteria for surrogate endpoint validation, the role of accelerated approval, and how the field has changed since the 2021 Project Optimus initiative. Focus on 3-5 concrete case studies."`
- Read / check: verify specific examples of PFS benefit without OS benefit (bevacizumab in breast cancer is the classic case), confirm FDA Project Optimus focus (optimal biological dose, not surrogate endpoints — do not conflate), verify the FDA's surrogate endpoint validation framework, confirm current accelerated approval process.
- Human supplies (Claude can't): Nothing — fully synthetic. All FDA approval data, trial results, and regulatory framework are publicly documented.
- Output medium: Remotion (animated 2×2 matrix — PFS benefit / OS translation — filling with case study examples)
- The change: ask Claude to compare basket trials and umbrella trials as modern adaptive designs — explain the design logic of each, give one real example of each in oncology, and identify which design is most appropriate for testing a hypothetical drug targeting a rare molecular alteration across cancer types.
- Teardown angle: the clinical trial is an epistemological instrument — its validity depends on the endpoint actually measuring what matters. OS is what matters. PFS is a convenience. The gap between them is where oncology's evidence base has been quietly eroding, and the regulatory conversation to fix it is still ongoing.
- Exclusions: full statistical methodology of trial design, Bayesian adaptive design mathematics, full regulatory pathway details for drug approval.
- Score: 8/10

## Candidate 10 — Research the Pre-Metastatic Niche: How a Tumor Prepares Its Future Home Before Sending Any Cells
- Source: cancer-biology-all/chapters/20-metastasis-the-seed-and-the-soil.md
- Lane: RESEARCH (Claude assistant)
- Hook: A breast cancer patient has no liver metastases — yet. But the tumor is already sending signals to the liver, recruiting immune cells, remodeling the matrix, and creating a hospitable landing zone. The cancer is doing real estate preparation before colonization. And it's doing it through exosomes with organ-specific integrin addresses.
- The artifact: a sourced mechanistic brief on the pre-metastatic niche — how primary tumor-secreted factors (exosomes, cytokines) travel through the bloodstream and reshape target organs before cancer cells arrive — with the organ-specific integrin addressing mechanism and the therapeutic implications — animated as a Manim schematic (primary tumor → secreted factors → organ remodeling → arriving CTC finding prepared niche).
- Prompt seed: `claude "Research the pre-metastatic niche in cancer metastasis. Explain the mechanism by which primary tumors shape distant organs before cancer cells arrive: the role of tumor-derived exosomes (and their integrin 'address' hypothesis), MDSC recruitment, ECM remodeling at target organs, and the VEGFR1+ hematopoietic progenitor cell findings (Kaplan et al. 2005). What therapeutic strategies are being developed to disrupt niche formation?"`
- Read / check: confirm the Kaplan 2005 Nature paper on VEGFR1+ cells and pre-metastatic niche, verify the exosome integrin addressing work (Hoshino et al. 2015, Nature), confirm that MDSCs are key pre-niche recruiters, check whether any clinical trial has successfully targeted pre-niche formation.
- Human supplies (Claude can't): Nothing — fully synthetic. The founding papers are published and accessible.
- Output medium: Manim (animated schematic — primary tumor secreting exosomes → organ-specific landing → MDSC recruitment → arriving CTC colonizing prepared site)
- The change: ask Claude to explain why the pre-metastatic niche concept overturns the purely mechanical view of organotropism (the "blood flow explains everything" model) and what the exosome integrin data specifically added.
- Teardown angle: the pre-metastatic niche is Paget's seed-and-soil at the molecular level — but the twist is that the seed prepares the soil before it arrives. The tumor is doing real estate development. Therapeutic disruption of niche formation is conceptually appealing but practically early-stage; the biology is ahead of the drugs.
- Exclusions: full metastatic cascade biology, complete organotropism patterns for all cancer types, TIL and CAR-T in the metastatic setting.
- Score: 8/10

## Candidate 11 — Research Oncolytic Virotherapy: Harnessing Viruses as Anti-Cancer Agents
- Source: cancer-biology-all/chapters/46-oncolytic-virotherapy-viruses-as-cancer-drugs.md
- Lane: RESEARCH (Claude assistant)
- Hook: T-VEC is a herpes simplex virus engineered to infect and destroy cancer cells — and to make a cytokine that recruits the immune system to clean up the rest. It is FDA-approved for melanoma. But it works by injecting it directly into the tumor, and systemic oncolytic virotherapy has been harder than anyone expected. Why?
- The artifact: a sourced brief on oncolytic virotherapy — the mechanism (tumor-selective replication → lysis → immune activation), the approved agent (T-VEC/talimogene laherparepvec), the systemic delivery problem, and the combination strategies being tested with checkpoint inhibitors — rendered as a Remotion mechanism animation (virus enters tumor → replicates → lyses → releases GM-CSF → immune recruitment).
- Prompt seed: `claude "Research oncolytic virotherapy in cancer. Explain the mechanism of tumor-selective viral replication and immune stimulation. What makes T-VEC (talimogene laherparepvec) unique (herpes simplex backbone, GM-CSF engineering, FDA approval for melanoma), and what were the clinical results? Why has systemic oncolytic virotherapy been harder than local delivery, and what combination strategies with checkpoint inhibitors are in clinical trials?"`
- Read / check: confirm T-VEC FDA approval (2015 for advanced melanoma), verify GM-CSF engineering rationale, confirm clinical response rates and whether abscopal-type systemic responses were observed, check status of leading oncolytic + checkpoint inhibitor combinations.
- Human supplies (Claude can't): Nothing — fully synthetic. T-VEC approval data and published trials are accessible.
- Output medium: Remotion (animated mechanism — virus → tumor selective replication → lysis → immune activation cascade)
- The change: ask Claude to compare oncolytic virotherapy with CAR-T cell therapy as engineered immune approaches — mechanism, target cancer types, clinical evidence, and the specific biological barriers each faces.
- Teardown angle: the oncolytic virus is an immune activator wearing a cancer-killing disguise. The direct lysis is the entry point; the immune cascade is the actual therapeutic mechanism. The systemic delivery problem is not a biology problem — it is a pharmacology problem (the immune system clears the virus before it reaches the tumor).
- Exclusions: detailed virology of each virus platform, full immunology of abscopal effects, CAR-T manufacturing in depth.
- Score: 7/10

## Candidate 12 — Research Cancer Health Disparities: Why ZIP Code Predicts Survival More Than Tumor Biology
- Source: cancer-biology-all/chapters/70-global-disparities-ethics-and-policy-in-cancer-care.md
- Lane: RESEARCH (Claude assistant)
- Hook: Black patients with breast cancer have a 40% higher mortality rate than white patients despite similar incidence. The biology of the tumors is different — higher triple-negative rate — but biology explains only part of the gap. Access, screening timing, treatment quality, and clinical trial representation each contribute. Which interventions actually close the gap?
- The artifact: a sourced analysis of racial and socioeconomic disparities in cancer outcomes — structured as a causal chain (incidence → late-stage diagnosis → treatment access → trial enrollment → survival) for breast and colorectal cancer — with the evidence for each link and the interventions that have been shown to work, animated as a Remotion causal chain filling left to right.
- Prompt seed: `claude "Research racial and socioeconomic disparities in cancer outcomes in the United States. For breast cancer and colorectal cancer, trace the causal chain from incidence through late-stage diagnosis, treatment access, clinical trial enrollment, and survival outcomes. What proportion of the gap is explained by tumor biology (e.g., triple-negative breast cancer rates) vs. systemic factors? Which specific interventions (patient navigation, community screening programs, Medicaid expansion) have demonstrated measurable reduction in the disparity?"`
- Read / check: verify Black/white breast cancer mortality gap and its decomposition into biological vs. access factors, confirm colorectal cancer disparity magnitude and leading causes, verify specific intervention effect sizes (patient navigation programs, Medicaid expansion outcomes), check whether any clinical trial enrollment diversity initiative has been formally evaluated.
- Human supplies (Claude can't): Nothing — fully synthetic. SEER data, published health disparities research, and policy evaluations are accessible.
- Output medium: Remotion (animated causal chain — incidence → diagnosis timing → treatment access → trial enrollment → survival gap, with intervention evidence callouts)
- The change: ask Claude to evaluate whether biological differences (tumor subtype distribution) or structural differences (access, insurance, treatment quality) contribute more to the Black/white breast cancer mortality gap, and cite the specific studies that have tried to decompose this.
- Teardown angle: the disparity is not a mystery — it is a documented causal chain, most links of which have evidence-based interventions. The political question is why documented, effective interventions have not been scaled. The science knows what to do; the policy is the bottleneck.
- Exclusions: international disparities between high-income and low-income countries (a different causal structure), cancer drug pricing policy details, full trial diversity initiative methodology.
- Score: 7/10
