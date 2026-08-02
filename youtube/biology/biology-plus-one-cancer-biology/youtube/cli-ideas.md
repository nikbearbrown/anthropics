# Biology Plus One — Cancer Biology — CLI Video Ideas ("X with Claude")

---

## Card 01 — Research the Two-Hit Hypothesis: Knudson's Insight and RB1

- **Source**: Chapter 6 (Tumor Suppressor Genes) — RB1 discovery, Knudson two-hit reasoning
- **Lane**: RESEARCH
- **Hook**: One mutation won't do it. You need to break both brakes. How did Knudson prove that from statistics alone — before the gene was even found?
- **The artifact**: A sourced explainer brief tracing Knudson's 1971 statistical argument, the retinoblastoma data, the somatic-cell hybridization experiments, and the 1986 molecular cloning of RB1 — with a comparison table: hereditary vs sporadic retinoblastoma (age of onset, laterality, hit count).
- **Prompt seed**: `claude "Research the Knudson two-hit hypothesis for tumor suppressor genes. Trace the evidence: (1) somatic-cell hybridization (Henry Harris 1969), (2) Knudson 1971 statistical model for retinoblastoma, (3) chromosome 13q14 cytogenetics, (4) Dryja/Friend/Weinberg 1986 RB1 cloning. Produce a sourced brief with a comparison table: hereditary vs sporadic retinoblastoma (age, laterality, number of mutations required)."`
- **Read/check**: Verify Knudson 1971 PNAS citation; confirm RB1 cloning year (1986) and authors; check that two-hit logic holds for RB1 specifically.
- **Human supplies**: Nothing — fully synthetic from published literature.
- **Output medium**: Slate (animated reveal of comparison table: hereditary vs sporadic side-by-side, Knudson mutation count chart).
- **The change**: Before: mysterious cancer biology jargon. After: a clear causal chain from Knudson's pen-and-paper statistics to a molecular mechanism — the two-hit model visualized.
- **Teardown angle**: Cancer's first tumor suppressor was discovered by counting cases in a pediatric ophthalmology registry, not by sequencing genes.
- **Exclusions**: Do not discuss CDK4/6 inhibitors (therapy); do not conflate RB1 with Rb protein function in G1/S (covered in cell-cycle chapter).
- **Score**: 10/10 — landmark discovery story, checkable from primary sources, direct visual payoff.

---

## Card 02 — Research TP53: The Most Mutated Gene in Human Cancer

- **Source**: Chapter 6 (Tumor Suppressor Genes) — TP53 as guardian of the genome, Li-Fraumeni syndrome
- **Lane**: RESEARCH
- **Hook**: Half of all human cancers carry a broken copy of the same gene. Why is TP53 cancer's single most common target — and why is it still undruggable?
- **The artifact**: A sourced brief covering p53's four stress responses (arrest, apoptosis, repair, senescence), why missense hot-spot mutations dominate (dominant-negative + gain-of-function), Li-Fraumeni syndrome, and the three therapeutic strategies (PRIMA-1, MDM2 inhibitors, synthetic lethality) with a scorecard of clinical trial results.
- **Prompt seed**: `claude "Research TP53 as the most frequently mutated gene in cancer. Cover: (1) p53 protein function (arrest, apoptosis, DNA repair, senescence), (2) why missense mutations dominate vs truncating (dominant-negative + GOF), (3) Li-Fraumeni syndrome clinical profile, (4) three therapeutic strategies: PRIMA-1/COTI-2 reactivators, MDM2 inhibitors (nutlins/idasanutlin), synthetic lethality. Produce a sourced brief with a clinical-trial scorecard table."`
- **Read/check**: Confirm mutation frequency (~50% of all cancers); verify Li-Fraumeni lifetime cancer risk (>90%); confirm MDM2 inhibitor names and trial phase.
- **Human supplies**: Nothing — fully synthetic.
- **Output medium**: Slate (animated reveal: TP53 mutation frequency bar chart across cancer types; clinical trial scorecard as animated table).
- **The change**: Before: "p53 is a tumor suppressor" (rote fact). After: a mechanistic picture of why one gene is indispensable across tissues — and why fixing it is hard.
- **Teardown angle**: The most important anti-cancer gene in the human genome is still not druggable 35 years after discovery.
- **Exclusions**: Do not detail MDM2 structure; do not cover BRCA1/2 (separate card territory).
- **Score**: 9/10 — highest clinical relevance, strong visual for mutation frequency bar chart.

---

## Card 03 — Research VEGF and the Angiogenic Switch

- **Source**: Chapter 12A (Angiogenesis) — Folkman hypothesis, VEGF/HIF feedback loop
- **Lane**: RESEARCH
- **Hook**: A tumor that outgrows its blood supply doesn't die — it builds a new one. How? And if we block that signal, why doesn't the tumor starve?
- **The artifact**: A sourced explainer brief covering the angiogenic switch (Folkman 1971), the HIF-1α → VEGF → vessel growth feedback loop, tumor vasculature chaotic architecture, bevacizumab's mechanism, and a table of anti-angiogenic drugs (target, approved indication, resistance mechanism).
- **Prompt seed**: `claude "Research tumor angiogenesis and the VEGF-HIF feedback loop. Cover: (1) Folkman 1971 angiogenic switch hypothesis, (2) hypoxia → HIF-1α → VEGF → endothelial sprouting mechanism, (3) tumor vasculature disorder (leaky, no pericytes), (4) bevacizumab (Avastin) mechanism and clinical outcomes, (5) resistance mechanisms (vessel co-option, vasculogenic mimicry, alternative signals). Produce a sourced brief with a drug comparison table."`
- **Read/check**: Verify Folkman 1971 NEJM citation; confirm bevacizumab approval year and indication; confirm VEGF-A/VEGFR-2 as dominant axis.
- **Human supplies**: Nothing — fully synthetic.
- **Output medium**: Manim mp4 (animated: tumor mass → hypoxia gradient → HIF stabilization → VEGF diffusion gradient → sprout growth toward tumor; then bevacizumab blocks VEGF).
- **The change**: Before: "bevacizumab blocks VEGF" (rote). After: the full feedback loop animated — see WHY blocking it should work and WHY tumors escape.
- **Teardown angle**: Folkman was right that tumors need new vessels. He was wrong that blocking one signal would be enough — tumors have backup vascular plans.
- **Exclusions**: Do not cover lymphangiogenesis (VEGF-C/D); do not detail pericyte biology.
- **Score**: 9/10 — Manim animation of the feedback loop is inherently visual and didactically powerful.

---

## Card 04 — Research HPV, E6/E7, and Why Cervical Cancer Is Preventable

- **Source**: Chapter 8B (Viral Carcinogens) — HPV oncoproteins, vaccine development
- **Lane**: RESEARCH
- **Hook**: One virus causes essentially all cervical cancers — and we have a vaccine that eliminates 90% of them. So why is cervical cancer still killing 340,000 women per year?
- **The artifact**: A sourced brief covering HPV E6/E7 mechanism (p53 degradation + Rb release), CIN progression grades, Gardasil 9 efficacy data, and a table comparing global cervical cancer rates vs vaccination coverage — with the equity gap highlighted.
- **Prompt seed**: `claude "Research HPV-driven cervical cancer and prevention. Cover: (1) HPV E6 protein: degrades p53 via E6AP ubiquitin ligase, (2) HPV E7 protein: releases E2F by disrupting Rb, (3) CIN 1→2→3→invasive carcinoma progression timeline, (4) Gardasil 9 efficacy (nine types, ~90% prevention), (5) global cervical cancer mortality vs vaccination coverage gap. Produce a sourced brief with a country-level comparison table."`
- **Read/check**: Verify Gardasil 9 FDA approval (2014); confirm nine HPV types covered; verify global mortality figure (~340,000/year) and high-income vs low-income incidence gap.
- **Human supplies**: Nothing — fully synthetic.
- **Output medium**: Slate (animated reveal: E6/E7 mechanism diagram as annotated visual; country coverage map as data table reveal).
- **The change**: Before: "HPV causes cervical cancer." After: a mechanistic chain from viral protein to p53/Rb loss — and a clear picture of the equity gap that keeps mortality high despite the vaccine existing.
- **Teardown angle**: We have a vaccine that eliminates most cervical cancers. The deaths that still happen are a policy and equity failure, not a science failure.
- **Exclusions**: Do not cover HBV or H. pylori (different carcinogens); do not discuss colposcopy technique.
- **Score**: 9/10 — strong equity angle, mechanistic clarity, checkable data.

---

## Card 05 — Research the Cell Cycle: Cyclin-CDK Waves and the Restriction Point

- **Source**: Chapter 9A (Cell Cycle Control) — cyclins, CDKs, G1/S checkpoint, restriction point
- **Lane**: RESEARCH
- **Hook**: The cell cycle runs like a train through stations with locked gates. Cancer picks the locks. Which locks — and how?
- **The artifact**: A sourced explainer brief covering the four cyclin-CDK pairings (D/4-6, E/2, A/2, B/1), the restriction point mechanics (Rb phosphorylation → E2F release), the three checkpoints (G1/S, G2/M, spindle assembly), and a table of cancer mutations that bypass each checkpoint — with CDK4/6 inhibitor (palbociclib) as the clinical payoff.
- **Prompt seed**: `claude "Research the cell cycle as a cancer target. Cover: (1) four cyclin-CDK pairings and their phases, (2) restriction point: cyclin D-CDK4/6 phosphorylates Rb → E2F released → S phase, (3) three checkpoints and what cancer mutations disable each, (4) CDK4/6 inhibitors (palbociclib, ribociclib, abemaciclib) mechanism and approval. Produce a sourced brief with a checkpoint-disruption table."`
- **Read/check**: Confirm CDK4/6 inhibitor approval indications (HR+/HER2- breast cancer); verify cyclin E-CDK2 drives G1/S transition; confirm APC/C role in cyclin B destruction.
- **Human supplies**: Nothing — fully synthetic.
- **Output medium**: Manim mp4 (animated: cyclin level waves rising and falling through the cycle phases; Rb phosphorylation event unlocking E2F; checkpoint gates opening/closing).
- **The change**: Before: cell cycle as a static diagram. After: a dynamic animation of rising and falling cyclin waves — the cycle becomes intuitive as a timed engine, not a memorization chart.
- **Teardown angle**: The cell cycle's regulatory logic was discovered in yeast in the 1980s and immediately explained human cancer mutations found in the clinic.
- **Exclusions**: Do not cover meiosis; do not detail ubiquitin-proteasome mechanics of cyclin destruction.
- **Score**: 9/10 — Manim cyclin-wave animation is inherently compelling; CDK4/6 inhibitor hook is clinically immediate.

---

## Card 06 — Research the Warburg Effect: Why Cancer Cells Eat Sugar Differently

- **Source**: Chapter 11A (Cancer Metabolism — Warburg Effect)
- **Lane**: RESEARCH
- **Hook**: Cancer cells prefer inefficient energy production even with plenty of oxygen. Otto Warburg noticed this in 1924. We still don't fully know why — and it's now a drug target.
- **The artifact**: A sourced brief explaining aerobic glycolysis (the Warburg effect), why it is paradoxically useful (biosynthetic precursors, acidification of tumor microenvironment, pH-mediated immune evasion), HIF-1α's role in upregulating glycolytic enzymes, and a table of metabolic drug targets (LDHA, IDH1/2 mutants, glutaminase) with clinical development status.
- **Prompt seed**: `claude "Research the Warburg effect in cancer metabolism. Cover: (1) Warburg's 1924 observation: aerobic glycolysis despite oxygen, (2) why aerobic glycolysis is adaptive: biosynthetic precursors (nucleotides, lipids, amino acids) and lactate export acidifying TME, (3) HIF-1α upregulating GLUT1, LDHA, PDK1, (4) IDH1/2 gain-of-function mutations producing 2-HG (oncometabolite), (5) drug targets: LDHA inhibitors, IDH1/2 inhibitors (enasidenib, ivosidenib). Produce sourced brief with drug-target table."`
- **Read/check**: Confirm Warburg's original 1924 Biochemische Zeitschrift paper; verify enasidenib/ivosidenib FDA approvals for AML; confirm 2-HG as D-2-hydroxyglutarate (oncometabolite blocking TET enzymes).
- **Human supplies**: Nothing — fully synthetic.
- **Output medium**: Slate (animated reveal: bar chart of ATP yield — oxidative phosphorylation 36 ATP vs glycolysis 2 ATP — with annotation of why 2 is sometimes better for fast-growing cells).
- **The change**: Before: "cancer has altered metabolism" (vague). After: a specific, mechanistic explanation of WHY aerobic glycolysis is not a defect but an adaptive strategy — and what drugs target it.
- **Teardown angle**: Warburg thought cancer was primarily a metabolic disease. He was wrong about the cause but right that the metabolic signature is exploitable.
- **Exclusions**: Do not detail TCA cycle intermediates; do not cover lipid metabolism (chapter 11B territory).
- **Score**: 8/10 — counterintuitive biology, strong visual for ATP comparison bar, clinical drug payoff.

---

## Card 07 — Research Checkpoint Immunotherapy: How Releasing T Cells Transformed Oncology

- **Source**: Chapter 16B (Cancer Immunotherapy) and Chapter 25A — checkpoint inhibitors, CAR-T
- **Lane**: RESEARCH
- **Hook**: Tumors don't just hide from the immune system — they put up "don't eat me" signs. Checkpoint inhibitors tear those signs down. How do they work, and why do only some patients respond?
- **The artifact**: A sourced brief covering the CTLA-4 discovery (Allison) and PD-1/PD-L1 pathway (Honjo), checkpoint inhibitor approvals (ipilimumab, nivolumab, pembrolizumab), response rates by cancer type (melanoma vs bladder vs NSCLC), and a table of predictive biomarkers (TMB, MSI-H, PD-L1 expression) — with a response rate comparison.
- **Prompt seed**: `claude "Research immune checkpoint inhibitors in oncology. Cover: (1) CTLA-4 discovery (James Allison) and mechanism: CTLA-4 competes with CD28 for B7, blocking T cell activation, (2) PD-1/PD-L1 axis (Tasuku Honjo): tumor PD-L1 silences T cells, (3) ipilimumab (anti-CTLA-4), nivolumab/pembrolizumab (anti-PD-1) approvals, (4) response rate variability: melanoma ~40% vs pancreatic ~2%, (5) predictive biomarkers: TMB, MSI-H, PD-L1 IHC. Produce sourced brief with response-rate comparison table."`
- **Read/check**: Verify 2018 Nobel Prize to Allison and Honjo; confirm ipilimumab FDA approval year (2011) for melanoma; verify MSI-H as tumor-agnostic checkpoint inhibitor indication.
- **Human supplies**: Nothing — fully synthetic.
- **Output medium**: Slate (animated reveal: T cell activation diagram with CTLA-4 block; PD-1/PD-L1 brake diagram; response rate bar chart by cancer type).
- **The change**: Before: "immunotherapy releases T cells" (slogan). After: two distinct molecular brakes, two distinct antibody mechanisms, and a stark picture of why response rates vary so dramatically across cancers.
- **Teardown angle**: Two scientists won a Nobel Prize for discovering that the immune system has its own off-switches — and that cancer uses them.
- **Exclusions**: Do not cover CAR-T cell construction; do not detail irAE (immune-related adverse events) management.
- **Score**: 8/10 — Nobel Prize angle, mechanistic clarity, clinically immediate biomarker table.

---

## Card 08 — Research the Liquid Biopsy: Reading Cancer From a Blood Draw

- **Source**: Chapter 18B (Molecular Diagnostics and Liquid Biopsy)
- **Lane**: RESEARCH
- **Hook**: You used to need to cut into a tumor to study it. Now you can read fragments of tumor DNA from a blood draw. What can a liquid biopsy actually tell you — and what can't it?
- **The artifact**: A sourced brief covering ctDNA biology (tumor cell death → DNA fragments in plasma), detection methods (ddPCR, NGS-based cfDNA sequencing), clinical applications (minimal residual disease, resistance mutation tracking, early detection), and a limitations table (sensitivity, heterogeneity sampling, cost, regulatory status).
- **Prompt seed**: `claude "Research liquid biopsy and circulating tumor DNA (ctDNA). Cover: (1) ctDNA biology: how tumor DNA enters plasma, fragment size (~167 bp), half-life (~2 hours), (2) detection methods: allele-specific PCR, ddPCR, NGS-based ctDNA panels, (3) clinical applications: MRD detection post-surgery, resistance mutation tracking (e.g., T790M in EGFR), early detection trials (CCGA/GRAIL), (4) limitations: sensitivity in early-stage, clonal hematopoiesis confounding, cost. Produce sourced brief with applications-vs-limitations table."`
- **Read/check**: Verify ctDNA fragment size (~167 bp) and plasma half-life; confirm T790M resistance mutation in EGFR-mutant NSCLC as ctDNA-detectable; verify GRAIL/Galleri as lead early-detection product.
- **Human supplies**: Nothing — fully synthetic.
- **Output medium**: Slate (animated reveal: blood tube → ctDNA fragment extraction pipeline diagram as annotated visual; applications vs limitations comparison table as animated reveal).
- **The change**: Before: "liquid biopsy is the future" (hype). After: a clear picture of what ctDNA is, how it is detected, and an honest limitations table that separates current clinical reality from aspirational early-detection promise.
- **Teardown angle**: The most exciting cancer diagnostic of the decade still can't reliably find Stage I cancer — but it's already transforming how we track treatment response.
- **Exclusions**: Do not cover CTCs (circulating tumor cells) in depth; do not detail cfRNA or exosome-based liquid biopsy.
- **Score**: 8/10 — hot clinical topic, strong hype-vs-reality teardown, checkable from published trials.

---

## Card 09 — Research Metastasis: The Seed and Soil Hypothesis and Why It Took a Century to Validate

- **Source**: Chapter 13B (Metastasis — Seed and Soil)
- **Lane**: RESEARCH
- **Hook**: Stephen Paget proposed in 1889 that cancer cells seed specific organs — not randomly — based on the "soil." It took 100 years to prove him right. What did it take?
- **The artifact**: A sourced brief covering Paget's 1889 seed-and-soil hypothesis, the EMT transition (E-cadherin loss, vimentin gain), intravasation/extravasation steps, organ-tropism mechanisms (CXCR4/CXCL12, integrin signature), and a table of cancer type vs preferred metastatic site with the molecular determinant.
- **Prompt seed**: `claude "Research the seed-and-soil hypothesis for cancer metastasis. Cover: (1) Paget 1889 original paper and organ distribution in breast cancer autopsies, (2) EMT: E-cadherin downregulation, vimentin/fibronectin upregulation, transcription factors Snail/Twist/Zeb, (3) intravasation and extravasation steps, (4) organ tropism molecular mechanisms: CXCR4/CXCL12 axis (bone marrow), alpha-v integrins (lung), (5) metastatic niche formation. Produce sourced brief with cancer-type vs metastatic-site table."`
- **Read/check**: Verify Paget 1889 Lancet citation; confirm E-cadherin/CXCR4 as metastasis determinants; confirm breast cancer bone marrow tropism via CXCL12.
- **Human supplies**: Nothing — fully synthetic.
- **Output medium**: Slate (animated reveal: primary tumor → bloodstream → organ tropism table; EMT marker switch diagram as animated card reveal).
- **The change**: Before: metastasis as a random, hopeless spread. After: a directional process with molecular logic — cells don't go everywhere, they go where the soil is ready.
- **Teardown angle**: A Victorian surgeon figured out organ tropism in cancer from autopsy counts. Molecular biology confirmed him 100 years later.
- **Exclusions**: Do not cover dormancy in detail; do not cover lymphatic vs hematogenous route mechanics.
- **Score**: 8/10 — excellent historical angle, checkable mechanism, strong visual for organ-tropism table.

---

## Card 10 — Research Drug Pricing and Cancer: The Economics of Survival

- **Source**: Chapter 38A (Health Economics, Drug Pricing and Affordability)
- **Lane**: RESEARCH
- **Hook**: A drug that adds three months of life costs $100,000. Who decides that price — and is there any formula that justifies it?
- **The artifact**: A sourced brief covering the cost-effectiveness framework (QALY, ICER thresholds), cancer drug pricing trends (median launch price 1995 vs 2015 vs 2023), the R&D cost argument and its critics, international price comparison (US vs UK NICE vs Canada), and a table: five recent cancer drugs, launch price, ICER, approval indication, survival benefit.
- **Prompt seed**: `claude "Research cancer drug pricing and health economics. Cover: (1) QALY framework and ICER thresholds ($50k-$150k/QALY in US, $30k in UK NICE), (2) cancer drug launch price trends 1995-2023 (median), (3) R&D cost argument: $2.6B DiMasi estimate, Prasad/Mailankody counter-estimates, (4) US vs UK vs Canada price comparison for pembrolizumab and ibrutinib, (5) affordability: out-of-pocket impact and financial toxicity. Produce sourced brief with five-drug pricing comparison table."`
- **Read/check**: Verify DiMasi R&D cost estimate source (Tufts CSDD); confirm NICE ICER threshold (typically £20,000-£30,000/QALY); verify pembrolizumab US vs UK price difference.
- **Human supplies**: Nothing — fully synthetic.
- **Output medium**: Slate (animated reveal: drug launch price trend chart as animated line graph; five-drug comparison table as row-by-row reveal).
- **The change**: Before: "cancer drugs are expensive" (complaint). After: a specific analytical framework — QALY, ICER — showing how the industry and regulators actually argue about price, with a concrete cross-country comparison.
- **Teardown angle**: There is no formula that says a drug costs what it costs. The price is a negotiation — and in the US, the patient is not at the table.
- **Exclusions**: Do not cover Medicare Inflation Reduction Act drug negotiation provisions in detail; do not cover biosimilar competition specifics.
- **Score**: 7/10 — high public resonance, policy angle, checkable from published literature.

---

## Card 11 — Research AI and Machine Learning in Oncology: What Claude Can and Cannot Do

- **Source**: Chapter 29A (AI and Machine Learning in Oncology)
- **Lane**: RESEARCH
- **Hook**: AI can read a pathology slide faster and sometimes more accurately than a pathologist. Does that mean AI is about to replace the oncologist — or is the hype running ahead of the evidence?
- **The artifact**: A sourced brief covering FDA-cleared AI/ML devices in oncology (PathAI, Paige.AI, Viz.ai for stroke — oncology analog), AI in radiology (chest CT nodule detection, mammography screening), genomic AI (Foundation Medicine, Tempus, treatment matching), and a limitations table (dataset bias, regulatory pathway, explainability, clinical integration).
- **Prompt seed**: `claude "Research the role of AI and machine learning in oncology. Cover: (1) FDA-cleared AI in cancer pathology (Paige Prostate, PathAI), (2) AI in radiology: low-dose CT lung nodule detection, mammography (MIRAI model), (3) genomic AI: tumor mutational profiling for treatment matching (Foundation Medicine, Tempus), (4) limitations: training data bias, explainability, prospective validation gap, regulatory pathway. Produce a sourced brief with an FDA-cleared oncology AI device table."`
- **Read/check**: Verify Paige Prostate FDA clearance year (2021); confirm MIRAI mammography model publication (Shen et al. Nature Medicine); confirm Foundation Medicine FDA approval for CGP (2017).
- **Human supplies**: Nothing — fully synthetic.
- **Output medium**: Slate (animated reveal: FDA-cleared AI device table as row-by-row reveal; limitations scorecard as animated reveal).
- **The change**: Before: "AI is transforming oncology" (marketing). After: a specific inventory of FDA-cleared devices, what they actually do, and an honest limitations scorecard.
- **Teardown angle**: AI in oncology is real — three FDA-cleared pathology AI tools exist — but prospective clinical trial validation that AI improves survival is still largely absent.
- **Exclusions**: Do not cover drug discovery AI (AlphaFold2, generative chemistry); do not cover robotic surgery AI.
- **Score**: 7/10 — high currency, strong hype-correction angle, checkable from FDA device database.

---

## Card 12 — Research Synthetic Lethality: PARP Inhibitors and the BRCA Vulnerability

- **Source**: Chapter 6 (Tumor Suppressor Genes — BRCA + synthetic lethality) and Chapter 24B
- **Lane**: RESEARCH
- **Hook**: BRCA1/2 mutations cause cancer — but they also create a weakness the drug can exploit. PARP inhibitors kill BRCA-mutant cells by taking away their last DNA repair option. How does that work?
- **The artifact**: A sourced brief covering BRCA1/2 function in homologous recombination, the synthetic lethality concept (two pathways, each dispensable alone but lethal together), PARP1's role in single-strand break repair, PARP inhibitor trapping mechanism, and a table of approved PARP inhibitors (olaparib, niraparib, rucaparib, talazoparib) with approval indications and response rates.
- **Prompt seed**: `claude "Research synthetic lethality and PARP inhibitors in BRCA-mutant cancers. Cover: (1) BRCA1/2 function in homologous recombination (HR) repair, (2) synthetic lethality concept: BRCA-loss removes HR, PARP inhibition removes SSBR, together lethal, (3) PARP trapping mechanism (inhibitor locks PARP on DNA), (4) four approved PARP inhibitors: olaparib, niraparib, rucaparib, talazoparib — indications, (5) resistance mechanisms: secondary BRCA reversion mutations. Produce sourced brief with PARP inhibitor comparison table."`
- **Read/check**: Verify olaparib as first PARP inhibitor FDA approved (2014, ovarian cancer); confirm PARP trapping mechanism (catalytic inhibition ≠ trapping); verify BRCA reversion mutations as resistance mechanism.
- **Human supplies**: Nothing — fully synthetic.
- **Output medium**: Slate (animated reveal: two-pathway diagram — HR + SSBR — with knockout branches showing cell death only when both are blocked; PARP inhibitor approval table as reveal).
- **The change**: Before: "PARP inhibitors work in BRCA mutations" (rote). After: the conceptual elegance of synthetic lethality — exploiting a cancer's genetic defect as a drug vulnerability — visualized as a pathway diagram.
- **Teardown angle**: PARP inhibitors are one of the first truly rational cancer drugs: designed from first principles of DNA repair biology, not from empirical chemotherapy screening.
- **Exclusions**: Do not cover germline vs somatic BRCA testing protocol; do not cover BRCA2's role in Fanconi anemia.
- **Score**: 9/10 — conceptually elegant, clinically proven, checkable from published trials, strong visual logic.

---

| Book | Status | Lane | Candidates |
|------|--------|------|-----------|
| biology-plus-one-cancer-biology | SCOUTED | RESEARCH | 12 cards |
