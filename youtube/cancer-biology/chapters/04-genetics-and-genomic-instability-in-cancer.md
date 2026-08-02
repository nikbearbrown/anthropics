# Chapter 4 — Genetics and Genomic Instability in Cancer

A sequencing report for a patient with metastatic colorectal cancer lists 187 mutations. The family, reading it, asks the natural question: which of these caused the cancer, and did the patient inherit them?

Both halves of that question rest on a misunderstanding the report itself invites. The 187 mutations are not 187 causes. The overwhelming majority are **passengers** — changes the cell accumulated while it was evolving, selected for nothing, leaving marks the way a glacier leaves scratches on rock. A small handful — here, an *APC* truncation, a *KRAS* G12D, a *TP53* loss — are **drivers**, the changes that actually gave this lineage its growth advantage. And almost all 187 are **somatic** — acquired in the tumor over years, present in no other cell of the body, inheritable by no one.

The report looks like an indictment of the genome. It is really a fossil record of a Darwinian process that ran inside one tissue for a decade or more. To read it correctly you need the framework this chapter builds: how mutations arise and which kinds exist, how to distinguish drivers from passengers, what Knudson's math tells us about inherited risk, and why the failure of DNA repair is one of the deepest engines of cancer.

---

## Cancer as evolution

The organizing idea for this chapter is that cancer is a sequence of mutations selected for in a clonal lineage — evolution, in real time, inside the body, over decades. This is not a metaphor. The process has the three features Darwin identified: heritable variation (mutations), differential reproduction (some cells divide faster, some die less), and selection operating on that variation over successive generations.

Bert Vogelstein's work on colorectal cancer was the founding demonstration. By biopsying the same lineage at successive stages — normal mucosa, small adenoma, large adenoma, carcinoma — his group read out which mutations appeared at which stage. *APC* first, then *KRAS*, then loss of chromosome 18q, then *TP53*. Each appeared at the transition to the next stage. Each conferred a step-change advantage. The cancer was not created by a single event; it was assembled over years, one selected mutation at a time.

![Adenoma-carcinoma sequence: stepwise driver accumulation from normal mucosa to invasive carcinoma](images/04-genetics-and-genomic-instability-in-cancer-fig-01.png)
*Figure 4.1 — Clonal evolution: the adenoma-carcinoma sequence*

This framing does immediate work. It explains why cancer risk rises steeply with age — decades of selection are needed to assemble the required mutations. It explains why environmental carcinogens increase risk — they accelerate the mutation supply. And it explains why a 187-mutation report contains only a few drivers: most mutations arise during the evolutionary process and hitchhike along, selected for nothing.

---

## Where mutations come from

A human cell holds about 3 billion base pairs, replicated each S phase by DNA polymerase, which reads the parent strand and builds a complement. Polymerase errs at about 1 in 10⁵ per base, proofreads its own work down to roughly 1 in 10⁷, and mismatch repair afterward brings the final rate to about 1 in 10⁹ — roughly three uncaught errors per division across the genome. Most are silent or neutral. The rare error in the wrong codon of the wrong gene, in a cell that survives and divides, is the substrate cancer evolves from.

Beyond replication errors, cells face tens of thousands of DNA lesions per day from oxidative metabolism, ionizing radiation, UV light, and chemical mutagens. Without repair, the genome would degrade within days. Each source of damage produces a characteristic spectrum of mutations — a **mutational signature** — and these signatures can be read in tumor genomes the way a forensic scientist reads trace evidence. Signatures of UV damage (C→T transitions at dipyrimidines) are the dominant signal in melanoma; tobacco smoke signatures (G→T transversions) dominate lung adenocarcinoma in smokers; APOBEC enzyme signatures appear in breast and bladder cancer. The tumor genome records not just what went wrong but what was exposing the cell as it went wrong.

---

## The catalog of mutation types

**Point mutations** change one base. A missense mutation substitutes one amino acid; a nonsense mutation creates a premature stop codon, truncating and usually destroying the protein; a silent mutation changes the DNA but not the protein; a splice-site mutation disrupts mRNA processing. **Insertions and deletions** — indels — add or remove bases; if not a multiple of three, they cause a frameshift, typically producing a truncated, nonfunctional protein. These small mutations are the most common type in cancer.

**Copy-number variations** gain or lose large genomic regions. Amplification boosts the output of oncogenes — *MYC* amplification in neuroblastoma, *HER2* amplification in breast cancer, *EGFR* amplification in glioblastoma. Deletion removes tumor suppressors — loss of *CDKN2A* at 9p21 eliminates the CDK inhibitor p16, releasing cyclin D–CDK4/6.

**Chromosomal translocations** fuse segments of two different chromosomes. The Philadelphia chromosome — t(9;22), fusing *BCR* and *ABL1* into a constitutively active tyrosine kinase — drives chronic myeloid leukemia. Identified by Nowell and Hungerford in 1960, it became the target of imatinib forty years later, the first truly targeted cancer therapy and the proof-of-concept that a single chromosomal abnormality could be both necessary and sufficient for a cancer and that targeting its product could work. Other translocations act differently: t(8;14) places *MYC* under immunoglobulin enhancers in Burkitt lymphoma, driving massive overexpression; t(14;18) does the same for *BCL2* in follicular lymphoma, blocking apoptosis.

At the extreme end of structural disruption, **chromothripsis** — a chromosome shattered and reassembled imperfectly in what may be a single catastrophic event — produces dozens of rearrangements simultaneously, rather than accumulated one at a time. Its frequency and significance are still being worked out, but it demonstrates that cancer's genetics are not always a slow accumulation.

**Epigenetic changes** — DNA methylation, histone modification — alter gene expression without changing DNA sequence and are heritable through cell division. Cancers commonly silence tumor-suppressor promoters by hypermethylation, achieving the same effect as deletion without a sequence change.

---

## Drivers and passengers, and the three gene categories

A typical solid tumor carries tens to hundreds of coding mutations, but only two to eight drivers. The distinction matters enormously: passengers are noise, however numerous; drivers are signal, however few.

Several features distinguish them. Drivers recur across independent patients — independent evolution keeps landing on the same gene because selection keeps finding the same gene useful. Drivers land in functionally critical protein regions — the GTPase domain of RAS, the DNA-binding domain of p53. Drivers produce specific gain- or loss-of-function changes. Passengers are scattered, tumor-unique, and lack functional impact. The large catalogues — COSMIC, The Cancer Genome Atlas — have mapped recurrent drivers across cancer types by pattern of recurrence.

Three functional categories:

**Oncogenes** are normal genes whose overactivation drives proliferation. Their cancer mutations are dominant gain-of-function: a single mutated allele suffices. *KRAS* G12D — one mutant allele locking RAS in its active GTP-bound state — is the canonical example. RAS proteins appear mutated in roughly 30% of all human cancers; in pancreatic cancer, the figure is around 90%. The normal job of RAS is to relay growth factor signals through the RAF-MEK-ERK cascade; mutant RAS relays the signal whether or not a growth factor is present.

**Tumor suppressors** are genes whose normal function restrains proliferation or promotes death. Their cancer mutations are recessive loss-of-function: both copies must be inactivated. *TP53*, *RB1*, *APC*, *PTEN*, *BRCA1/2* fall into this category. *TP53* is mutated in roughly half of all human cancers — more than any other gene — because p53's role as the arbiter of the arrest-or-die decision makes it the single most valuable thing for a cancer cell to lose.

**DNA-repair genes** act one step removed. Losing them does not directly drive proliferation; it lets *other* mutations accumulate faster. Mismatch-repair genes (*MLH1*, *MSH2*, *MSH6*, *PMS2*) and homologous-recombination genes (*BRCA1*, *BRCA2*, *PALB2*) sit here. They are technically tumor suppressors, but their loss creates the hypermutator phenotype that enables the assembly of drivers at a rate the normal mutation rate could not support in a human lifetime.

---

## Knudson's two-hit hypothesis

Alfred Knudson's 1971 analysis of retinoblastoma is the cleanest cancer mathematics ever done, and it was done entirely without molecular evidence — from patient statistics alone.

Retinoblastoma is sporadic in about 60% of cases and familial in about 40%. Sporadic cases usually appear in one eye, at slightly later ages. Familial cases usually appear in both eyes, earlier, and are heritable. Knudson observed that the cancer requires *two* mutations in the same cell. In sporadic cases, both mutations must arise de novo in one retinal cell — a rare event squared, hence slow and usually unilateral. In familial cases, the child inherits one mutation already present in every retinal cell; only a single second mutation is needed, and since every retinal cell is already one hit away, independent second mutations occur across many cells — faster onset, often bilateral.

The model fit the observed age-at-onset distributions quantitatively, predicting that both copies of a single gene must be lost. Sixteen years later *RB1* was cloned and the prediction held exactly: every sporadic tumor carried two somatic mutations; every familial tumor carried one germline mutation plus one somatic mutation. The two hits were always both alleles of the same gene.

This resolves what is initially a paradox: the predisposition is **dominant at the family level** — carrying one defective *RB1* allele dramatically raises lifetime cancer risk, and the allele is passed to half of offspring. But the gene is **recessive at the cellular level** — the cell behaves normally until both alleles are gone. The germline carrier simply starts with the first hit already present in every retinal cell, reducing the somatic requirement from two events to one.

The principle extends to all tumor suppressors with germline variants: *BRCA1/2*, *APC*, *TP53*, *VHL*, *MLH1*, and others. It is the biological basis for screening carriers aggressively — every cell they have already has one hit, and a single somatic event is the only distance between a normal cell and a cancer cell.

![Knudson two-hit hypothesis: sporadic needs two somatic hits, familial needs one second hit](images/04-genetics-and-genomic-instability-in-cancer-fig-02.png)
*Figure 4.2 — Knudson's two-hit hypothesis (probability logic)*

<!-- → [DIAGRAM: two-hit hypothesis — sporadic (two somatic hits, unilateral, later) vs. familial (one germline + one somatic hit, bilateral, earlier), with the probability logic annotated] -->

One nuance: *PTEN* shows **haploinsufficiency** in some contexts — a single lost allele can reduce PTEN protein below the threshold needed for normal function. The two-hit rule is a strong default, not an absolute law.

---

## DNA repair and what happens when it fails

Cells suffer tens of thousands of DNA lesions per day from oxidative metabolism and environmental exposure. Specialized repair pathways handle different lesion types, and understanding which pathway handles which damage is directly clinically relevant.

**Base excision repair** fixes small single-base modifications — oxidized bases, alkylated bases — by cutting out the damaged base and resynthesizing the strand. **Nucleotide excision repair** handles bulky lesions that distort the helix — UV-induced thymine dimers, bulky chemical adducts. Cells with inherited NER defects have the syndrome *xeroderma pigmentosum*: extraordinary UV sensitivity and childhood skin cancers, because the signature UV damage cannot be corrected. **Mismatch repair** corrects errors that escape proofreading — base–base mismatches and small indel loops from replication slippage, particularly at repetitive sequences called microsatellites.

When mismatch repair fails — whether by inherited mutation in *MLH1*, *MSH2*, *MSH6*, or *PMS2* (Lynch syndrome) or by somatic silencing of *MLH1* — the microsatellites accumulate errors and vary in length between cells. This **microsatellite instability** is directly detectable in a tumor biopsy and is both a diagnostic biomarker for MMR failure and a predictor of immunotherapy response. High microsatellite instability means high mutation burden means many neoantigens means a visible target for checkpoint inhibitors. This is why pembrolizumab received the first tumor-agnostic FDA approval: MSI-high tumors, regardless of where they arise, respond to checkpoint blockade because their defective repair has made them immunologically conspicuous.

**Double-strand break repair** is the most critical pathway, because an unrepaired double-strand break can kill the cell or produce catastrophic rearrangements. Two mechanisms exist. **Homologous recombination** is high-fidelity: it uses the sister chromatid as a template, directed by RAD51, BRCA1, BRCA2, and PALB2, and repairs the break accurately. It is available only in S and G2 phase, when the sister chromatid is present. **Non-homologous end joining** is fast but imprecise: it ligates broken ends without a template, introducing small insertions or deletions at the junction. NHEJ operates throughout the cell cycle and handles most double-strand breaks, but its error-prone nature makes it a source of chromosomal rearrangements.

Inherited *BRCA1* or *BRCA2* mutations disable homologous recombination. Breaks fall to NHEJ, which misjoins ends, accumulating rearrangements — explaining the genomic instability of BRCA-mutant tumors. This deficiency is also exploited therapeutically through **synthetic lethality**. PARP inhibitors block single-strand-break repair; those lesions are converted to double-strand breaks during replication. HR-competent cells repair the double-strand breaks through HR and survive. *BRCA*-mutant cells have lost HR — the only high-fidelity double-strand-break repair available to them — and die. The drug selectively kills tumor cells not because it targets a growth pathway but because it exploits a repair vulnerability that normal cells do not share. Olaparib and other PARP inhibitors are now standard for BRCA-mutant breast, ovarian, and prostate cancers.

![Synthetic lethality: PARP inhibition makes double-strand breaks that kill only HR-deficient cells](images/04-genetics-and-genomic-instability-in-cancer-fig-03.png)
*Figure 4.3 — Synthetic lethality: BRCA loss and PARP inhibition*

---

## Genomic instability as the engine

Hanahan and Weinberg classified **genomic instability** not as a hallmark of cancer in itself but as an *enabling characteristic* — a condition that lets the other hallmarks be acquired. The logic is direct: a normal cell accumulates roughly three mutations per division, making the assembly of five to ten specific drivers statistically slow across a human lifetime. A cell that has lost a repair pathway or a mitotic checkpoint mutates ten to a hundred times faster, vastly raising the probability of assembling the needed drivers in time.

Lawrence Loeb called this the **mutator phenotype**: before a cancer lineage can acquire all the required drivers, it needs to become a better mutator first. The repair-gene mutations are the mutations that enable all the other mutations.

Theodor Boveri anticipated the chromosome-level version in 1914, observing that cells with abnormal chromosome numbers behave abnormally, and proposing that chromosome segregation errors might be a cancer cause — largely dismissed for fifty years, then vindicated. Roughly 90% of solid tumors carry chromosomal abnormalities, **aneuploidy** that perturbs thousands of genes simultaneously. Telomere shortening — the gradual erosion of chromosome ends with each division — drives a pre-cancer "crisis" of chromosome fusions and breaks when telomeres are exhausted. Most cells die in this crisis; a rare cell emerges with telomerase reactivated, stable chromosomes, and the ability to divide indefinitely. That cell has passed through a bottleneck that selected for the hardiest survivors. What emerges has already been tested against multiple death signals.

---

## Reading the mutation report

Return to the opening case: 187 mutations including *APC* frameshift, *KRAS* G12D, *TP53* nonsense, a 9p21/*CDKN2A* deletion, and high microsatellite instability.

The wrong approach is to rank by how damaging each mutation looks — a nonsense mutation "sounds worse" than a missense, so declare *TP53* the main driver and stop. That conflates molecular severity with selective role and ignores recurrence.

The right approach sorts by function and recurrence. *APC* frameshift: tumor suppressor, loss-of-function, the recurrent first hit in colorectal cancer — driver. *KRAS* G12D: oncogene, the most common activating RAS mutation, single allele sufficient — driver. *TP53* nonsense: tumor suppressor, loss-of-function — driver. 9p21/*CDKN2A* deletion: copy-number loss of a tumor suppressor encoding the CDK inhibitor p16 — driver. That is four drivers in the recognizable colorectal adenoma-carcinoma sequence. The other 183 mutations are passengers.

Now the MSI-high finding reframes the report. MSI-high means mismatch repair has failed, which explains why there are 187 mutations rather than the typical thirty or forty: the tumor has been running a hypermutator phenotype. MSI can be sporadic — usually caused by epigenetic silencing of *MLH1* — or germline, indicating Lynch syndrome. This triggers genetic testing of the patient and potentially their relatives. And MSI-high predicts strong response to immune checkpoint inhibitors, because the mutation burden generates abundant neoantigens the immune system can recognize.

The most clinically decisive finding in this report is not any individual mutation. It is the repair-pathway failure that explains the mutation count, demands family counseling, and predicts immunotherapy benefit.

---

## What would change this picture

The chapter's central claim is that cancer is clonal evolution: drivers selected over time within a lineage, with genomic instability as the accelerating engine. The finding that would force revision: a common cancer type shown to arise fully formed from a single, non-selective, non-clonal event with no preceding driver accumulation and no detectable instability — a tumor assembled instantaneously without the evolutionary process. Chromothripsis shows that some genomic rearrangements happen in bursts, not slowly, but those still feed a subsequent clonal selection process. A reproducible cancer that bypassed selection entirely — same mutations, same instability, but no lineage — would mean the evolutionary frame is one route among several rather than the unifying one. That has not been shown.

---

## Still open

How many drivers a given cancer actually requires, and why the number varies so widely — a single fusion gene in some leukemias, four or more specific drivers in colorectal cancer — is not fully resolved. The differences in tissue context, cellular origin, and niche environment presumably explain it, but the quantitative rules are not worked out.

Whether aneuploidy is primarily a *cause* of cancer progression or primarily a *consequence* of the selection pressures that produce unstable cells is still argued. The direction of causality matters: if aneuploidy is causal, generating it is a viable therapeutic target; if it is mostly downstream, other things need to be targeted first.

And for the 10 to 15% of cancers maintaining telomeres without telomerase — using the alternative lengthening of telomeres (ALT) pathway — why this route gets selected in some lineages, and whether it can be targeted the way telomerase can, remains genuinely open.

---

## LLM Exercises

1. **(Classification)** For each, name the mutation class and the gene category: (a) *KRAS* G12D; (b) *BRCA1* frameshift; (c) *HER2* amplification; (d) t(9;22) *BCR-ABL1*; (e) *MLH1* promoter hypermethylation. For each, predict whether one mutant allele is sufficient for cancer contribution or whether both alleles must be affected, and justify from the gene category.

2. **(Driver/passenger)** A tumor carries mutations in *APC*, *KRAS*, *TP53*, and fifty scattered missense changes unique to this patient that appear in no cancer database. Identify the likely drivers versus passengers, justify each call using recurrence and gene function, and explain why the fifty unique mutations are almost certainly passengers rather than undetected private drivers.

3. **(Knudson's logic)** Explain qualitatively why familial retinoblastoma onset is earlier and more often bilateral than sporadic, in terms of the probability of one required event versus two. Then extend the argument: a child inherits a germline *BRCA1* frameshift. Using two-hit logic, predict the tissue distribution of cancers that child is at elevated risk for, and explain why it is elevated but not inevitable.

4. **(Synthetic lethality)** A patient's tumor carries biallelic *BRCA2* loss. Explain step by step why a PARP inhibitor selectively kills tumor cells but spares normal cells, naming the repair pathways involved and the specific point where tumor cells fail. Then propose two distinct mechanisms by which the tumor could become resistant to the PARP inhibitor.

5. **(Report interpretation)** A sequencing report for a lung adenocarcinoma lists 340 mutations and is flagged as TMB-high (high tumor mutational burden). It includes *KRAS* G12C, *STK11* loss, *KEAP1* loss, and 336 predominantly C→T mutations at dipyrimidines. Identify the likely drivers, characterize the mutational signature and what it implies about tumor history, and predict the immunotherapy response and its likely mechanism. Note any apparent contradictions in the prediction and explain them.

---

## References

- NCI. *The Genetics of Cancer.* https://www.cancer.gov/about-cancer/causes-prevention/genetics
- NCI. *What Is Cancer?* https://www.cancer.gov/about-cancer/understanding/what-is-cancer
- Knudson, A. G. (1971). Mutation and Cancer: Statistical Study of Retinoblastoma. *PNAS* 68, 820–823.
- Hino, O., & Kobayashi, T. (2017). The two-hit hypothesis. *Cancer Science.* https://onlinelibrary.wiley.com/doi/10.1111/cas.13116
- NCBI Bookshelf. *The Development and Causes of Cancer.* https://www.ncbi.nlm.nih.gov/books/NBK9963/
- NCBI Bookshelf. *Molecular Biology of the Cell.* https://www.ncbi.nlm.nih.gov/sites/books/n/mboc4/
- Hanahan, D. (2022). Hallmarks of Cancer: New Dimensions. *Cancer Discovery* 12, 31–46. https://aacrjournals.org/cancerdiscovery/article/12/1/31/675608

---

## Prompts

### Figure 4.1 — Clonal evolution: the adenoma-carcinoma sequence
Build a left-to-right flowchart of four sequential stages with driver-mutation labels on the connecting arrows, and a clonal fan that visibly widens at each step. Nodes in order: (1) Normal mucosa (neutral); (2) Small adenoma (green, positive growth advantage); (3) Large adenoma (green); (4) Carcinoma — invasive, breaches basement membrane (vermillion, negative). Arrow labels between nodes: "APC loss," "KRAS activation," "18q loss → TP53 loss." Beneath or behind the node sequence, draw an expanding wedge/fan of cells growing wider at each successive stage to convey clonal expansion of the advantaged lineage. Subtitle: "Vogelstein's stepwise driver accumulation." Okabe-Ito semantics: green for the proliferating adenoma stages, vermillion for the invasive carcinoma endpoint, neutral for normal tissue. Deliverable: single standalone HTML file, inline CSS, D3 v7 pinned CDN, Okabe-Ito colorblind-safe palette via CSS variables.

### Figure 4.2 — Knudson's two-hit hypothesis (probability logic)
Build a two-panel comparison, left panel "Sporadic," right panel "Familial," sharing axis label "Path to biallelic loss." Four aligned rows compare the two paths: (1) "All cells start with two intact alleles" vs "All cells carry one inherited defective allele" (secondary); (2) "Two independent somatic hits in same cell (rare)" vs "Only a single second hit needed" (vermillion, the key probability difference); (3) "Single transformed clone" vs "Multiple independent transformations" (neutral); (4) "Later onset, one tumor" vs "Earlier, multifocal onset" (sky-blue anchor, the clinical payoff). Represent each allele as a paired-box glyph (intact vs hit) so the reader sees one inherited hit pre-present on the familial side. Emphasize row 2 as the row that explains everything downstream. Subtitle: "Biallelic loss required — one inherited hit changes the odds." Okabe-Ito semantics: vermillion for the single-hit shortcut, sky-blue anchor for the onset outcome. Deliverable: single standalone HTML file, inline CSS, D3 v7 pinned CDN, Okabe-Ito colorblind-safe palette via CSS variables.

### Figure 4.3 — Synthetic lethality: BRCA loss and PARP inhibition
Build a left-to-right flowchart of a shared lesion chain that then branches to two opposite fates. Main chain, four numbered nodes: (1) PARP inhibition blocks SSB repair (vermillion, the intervention); (2) SSBs accumulate; (3) Replication fork collapse; (4) Double-strand break (sky-blue anchor, the decisive lesion). From node 4, branch two outcome arrows: upper "HR-intact (BRCA/RAD51 sister-template) → survives" (green, positive); lower "BRCA-deficient → DSB unrepaired → cell death" (vermillion, negative). The single shared lesion produces opposite fates by HR status — make the branch visually emphatic. Subtitle: "Same lesion, opposite fates by HR status." Okabe-Ito semantics: vermillion for the blocking intervention and the lethal branch, green for the surviving branch, sky-blue anchor for the DSB. Deliverable: single standalone HTML file, inline CSS, D3 v7 pinned CDN, Okabe-Ito colorblind-safe palette via CSS variables.
