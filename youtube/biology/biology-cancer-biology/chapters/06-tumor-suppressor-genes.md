# Chapter 6 — Tumor Suppressor Genes


## TL;DR

- Cancer needs two things: an accelerator that is stuck, and a brake that is broken.
- The chapter moves through The discovery move, TP53 — the guardian of the genome, RB1 — the gate at G1/S, BRCA1 and BRCA2 — DNA repair guardians, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

Cancer needs two things: an accelerator that is stuck, and a brake that is broken.

Chapter 5 was about the accelerators — the proto-oncogenes that, when mutated, push the cell to keep dividing. This chapter is about the brakes — the genes whose normal job is to stop division, repair damage, or kill the cell when something has gone too wrong to fix. When these genes work, they hold cancer at bay. When they fail, cells that should have stopped do not, and cells that should have died live on. Almost every cancer carries mutations in *both* categories. An accelerator alone is not enough. A broken brake alone is not enough. The combination is what produces the disease.

The brakes are called *tumor suppressor genes*. The category was harder to discover than the oncogenes, because the logic is inverted. Oncogenes are dominant — one mutated copy is enough to push the cell forward. Tumor suppressors are typically recessive at the cellular level — both copies have to be inactivated for the brake to fail. You cannot identify a tumor suppressor by transfecting it into a normal cell and watching for transformation (which is how many oncogenes were found); inserting an extra copy of a tumor suppressor does not cause cancer, it suppresses cancer. The conceptual breakthrough required different experiments — somatic cell hybridization studies, statistical analysis of inherited cancer syndromes, and the eventual molecular cloning of the genes whose loss left those families vulnerable.

This chapter does five things. It walks through the discovery of the first tumor suppressor — RB1 — and Knudson's beautiful two-hit reasoning that anticipated the molecular biology by 15 years. It introduces the major tumor suppressor genes — TP53, RB1, BRCA1/2, APC, PTEN — and what each one does normally. It catalogs how tumor suppressors get inactivated, both genetically (mutation, deletion, loss of heterozygosity) and epigenetically (promoter hypermethylation, chromatin remodeling). It explains how loss of tumor suppressors creates therapeutic vulnerabilities — synthetic lethality is the principle, PARP inhibitors in BRCA-mutant cancers are the proof of concept. And it shows how hereditary cancer syndromes — Li-Fraumeni, hereditary breast/ovarian cancer, Lynch syndrome, familial adenomatous polyposis, retinoblastoma, von Hippel-Lindau — are the clinical expressions of tumor suppressor biology.

---

## The discovery move

The first hint that genes could *prevent* rather than cause cancer came from cell fusion experiments. In 1969, Henry Harris and his colleagues at Oxford fused cancer cells with normal cells. The resulting hybrid cells — carrying chromosomes from both parents — turned out to be largely incapable of forming tumors in animals. Something in the normal cell was suppressing the cancer phenotype.

The cell fusion experiments did not identify *which* genes were doing the suppressing. They just established that such genes existed. It took another 15 years to find the first one molecularly. The path went through retinoblastoma — Knudson's two-hit hypothesis (Chapter 4) had predicted, statistically, that retinoblastoma was caused by inactivation of both copies of a single gene. Cytogenetic analyses of retinoblastoma tumors showed deletions of chromosome 13q14 in some cases, narrowing the search region. In 1986, Thaddeus Dryja, Stephen Friend, and Robert Weinberg cloned the gene. RB1 was the first tumor suppressor identified molecularly — and gene transfer experiments confirmed the prediction. Introducing a wild-type RB1 gene back into retinoblastoma cells suppressed their tumorigenicity. The brake, once restored, worked.

The conceptual framework that emerged: a tumor suppressor gene encodes a protein whose normal function is to restrain cell proliferation, induce apoptosis when warranted, repair DNA damage, or otherwise hold cancer-promoting behavior in check. Loss of function — typically requiring both alleles to be inactivated — removes that restraint. The gene transfer rescue experiments are the gold-standard test: introduce a working copy back into the tumor cell and watch the phenotype reverse.

Following RB1, the floodgates opened. TP53 was identified in 1989 as a tumor suppressor (it had been described a decade earlier but mistakenly classified as an oncogene because of initial work with mutant alleles). BRCA1 was cloned in 1994; BRCA2 in 1995. APC in 1991. PTEN in 1997. VHL in 1993. NF1 and NF2. The mismatch repair genes in the early 1990s. Each one carried a story — a family with an inherited cancer syndrome, a chromosomal region implicated by linkage analysis, a gene cloned and confirmed.

---

## TP53 — the guardian of the genome

TP53 is the most frequently mutated gene in human cancer. Roughly half of all human tumors carry a TP53 mutation. In some cancers — high-grade serous ovarian carcinoma, head and neck squamous cell carcinoma, esophageal squamous cell carcinoma — the mutation rate exceeds 90 percent. TP53 is so central to cancer biology that it has been called *the guardian of the genome*, a phrase coined by David Lane in a 1992 review.

The protein encoded by TP53 is p53 (the lowercase is convention; the protein is 53 kilodaltons, named for its size). It is a transcription factor. In normal, healthy cells, p53 is present at low levels — its protein is rapidly degraded by an E3 ubiquitin ligase called MDM2, which keeps p53 levels low. When the cell experiences stress — DNA damage, hypoxia, ribosomal stress, oncogenic signaling, telomere dysfunction — sensor proteins (ATM, ATR, CHK1, CHK2) phosphorylate p53 in ways that prevent MDM2 binding. p53 accumulates. It accumulates in the nucleus. It binds specific DNA sequences. It turns on genes.

What genes? Several categories.

*Cell-cycle arrest genes.* p53 transcribes CDKN1A (p21), which inhibits cyclin-CDK complexes and halts the cell cycle at G1/S. If the damage is fixable, the cell repairs and resumes. This is the *guardian* function at its most direct.

*Apoptosis genes.* If the damage is too severe, p53 transcribes pro-apoptotic genes — PUMA, NOXA, BAX — which trigger the intrinsic apoptosis pathway. The cell dies rather than dividing with damaged DNA. This is the failsafe.

*DNA repair genes.* p53 also activates DNA repair pathway components — XPC, DDB2, GADD45 — that participate in nucleotide excision repair and base excision repair. The cell mobilizes machinery to fix the damage that was detected.

*Senescence genes.* In some contexts, p53 drives cells into a permanent non-dividing state called senescence. Senescent cells stay alive but cannot divide. They are removed from the proliferative pool. Senescence is a third option between repair-and-resume and apoptosis.

*Metabolic genes.* p53 also regulates genes involved in glycolysis, oxidative phosphorylation, and lipid metabolism, shifting cellular metabolism toward stress-tolerant patterns.

The combination of these functions is why p53 mutations are so consequential. Lose p53, and the cell loses its ability to halt the cycle when damaged, to die when broken beyond repair, to repair damage efficiently, to senescence when overstressed, to manage metabolic insult. A cell without p53 can sustain DNA damage that would have killed it and continue dividing — copying the damage into daughter cells. The mutations accumulate. The phenotype drifts.

The unusual feature of TP53 mutations in cancer is that they are mostly *missense* — single amino acid substitutions in the DNA-binding domain — rather than the truncating loss-of-function mutations typical of other tumor suppressors. The reason: mutant p53 often acts as a *dominant negative*. The protein assembles into tetramers, and mutant subunits in a tetramer can poison the function of wild-type subunits. Some mutant p53 alleles also have *gain-of-function* properties, where the mutant protein takes on new oncogenic functions (driving invasion, metastasis, drug resistance) that wild-type p53 does not have. The hot spots — R175, R248, R273, R282 — are among the most frequently mutated specific codons in all of cancer.

*Li-Fraumeni syndrome* is the inherited form of TP53 deficiency. Patients carry a germline TP53 mutation and develop multiple primary cancers — typically sarcomas, brain tumors, breast cancers, adrenocortical carcinomas, leukemias — often starting in childhood or early adulthood. The lifetime cancer risk in Li-Fraumeni carriers exceeds 90 percent. The syndrome is the clinical demonstration of how essential p53 is for preventing cancer across most tissues.

Drugging p53 has been a decades-long challenge. The protein is a transcription factor without an enzymatic active site. The mutations cause loss of function, not gain of an inhibitable activity. Current strategies include: small molecules that reactivate mutant p53 (PRIMA-1, COTI-2 — early-phase trials, mixed results); MDM2 inhibitors that stabilize wild-type p53 in tumors with intact TP53 (nutlins, idasanutlin, milademetan — modest activity); synthetic lethal approaches that target vulnerabilities specific to TP53-mutant cells. The field is still searching for the breakthrough that BCR-ABL got from imatinib.

---

## RB1 — the gate at G1/S

RB1 is the prototype tumor suppressor — first to be discovered, first to demonstrate the two-hit model. The protein it encodes (Rb) is a cell-cycle regulator. In its hypophosphorylated state, Rb binds and inhibits a transcription factor called E2F. E2F's normal function is to turn on the genes required for S phase — DNA polymerase, dihydrofolate reductase, thymidine kinase, and others. With Rb bound, E2F cannot transcribe these genes. The cell stays in G1.

When the cell receives growth signals, cyclin D-CDK4/6 complexes phosphorylate Rb. Phosphorylated Rb releases E2F. E2F drives S-phase entry. The cell progresses to DNA replication.

Lose RB1, and the gate is permanently open. E2F is always free. The cell is always primed to enter S phase. Combined with proliferative signals from oncogene activation, the result is unrestrained division.

Retinoblastoma is the canonical RB1-loss tumor. Hereditary retinoblastoma carriers inherit one mutant RB1 allele in every cell; loss of the wild-type allele in any retinal cell during development produces the tumor. The bilateral and multifocal pattern of hereditary retinoblastoma reflects the high probability that, given thousands of retinal cells each carrying the first hit, one of them will acquire the second hit.

RB1 loss is not limited to retinoblastoma. It is found in many adult cancers — small-cell lung cancer (essentially universal), some breast cancers, bladder cancers, osteosarcomas. RB1 loss is also a key feature of cancers driven by certain DNA tumor viruses. Human papillomavirus encodes an oncoprotein, E7, that binds Rb and degrades it. The cervix cells transformed by HPV-16 or HPV-18 have functionally lost Rb — not by mutation of the gene itself, but by viral degradation of the protein. The viruses have evolved to attack the same brake that cancers attack genetically.

CDK4/6 inhibitors — palbociclib, ribociclib, abemaciclib — exploit the Rb pathway from the other direction. These drugs inhibit the kinases that phosphorylate Rb. In cells with intact Rb, the drugs keep Rb hypophosphorylated and bound to E2F, halting the cell cycle. In cells with lost Rb, the drugs have no target to act through. The drugs are useful in hormone-receptor-positive breast cancer (which retains intact Rb) and are being explored in other contexts. They are an example of how understanding tumor suppressor biology informs cancer therapy even when the tumor suppressor itself is intact.

---

## BRCA1 and BRCA2 — DNA repair guardians

BRCA1 and BRCA2 are tumor suppressors whose function is not direct cell-cycle restraint but accurate DNA repair. They are essential components of the homologous recombination (HR) machinery that repairs DNA double-strand breaks.

A double-strand break — both DNA strands severed — is the most dangerous kind of DNA damage. Misrepair can produce chromosomal translocations, large deletions, or genomic chaos. The cell has two pathways to handle it. *Non-homologous end joining (NHEJ)* simply pastes the broken ends back together, sometimes with errors. *Homologous recombination (HR)* uses the sister chromatid as a template for accurate repair. HR requires BRCA1, BRCA2, PALB2, RAD51, and a host of other proteins.

In cells with functional BRCA1/2, double-strand breaks are repaired by HR — accurately, conservatively. In cells that have lost BRCA1 or BRCA2, double-strand breaks are repaired by NHEJ or by error-prone alternative pathways — inaccurately, with structural rearrangements. Over time, BRCA-deficient cells accumulate genomic alterations, including the mutations that drive cancer.

Hereditary BRCA1/2 mutations are the most common cause of hereditary breast and ovarian cancer. A woman carrying a pathogenic BRCA1 variant has a lifetime breast cancer risk of about 65 to 80 percent and ovarian cancer risk of about 40 to 60 percent. BRCA2 carriers have similar risks, with somewhat lower ovarian risk and additional risks for pancreatic cancer and male breast cancer. The cancers that develop are often triple-negative (BRCA1) or hormone-receptor-positive (BRCA2) breast cancers, high-grade serous ovarian cancers, and pancreatic adenocarcinomas. Genetic testing for BRCA1/2 has been routine since the late 1990s and is the basis for risk-reducing surgery (prophylactic mastectomy, salpingo-oophorectomy) in carriers who choose it.

The therapeutic story is one of the most beautiful in modern oncology. BRCA-mutant cancers turn out to be exquisitely sensitive to a class of drugs called *PARP inhibitors*. PARP1 is an enzyme involved in repair of single-strand DNA breaks. When PARP is inhibited, single-strand breaks accumulate. When a replication fork encounters an unrepaired single-strand break, the break is converted to a double-strand break. In a normal cell, HR repairs the double-strand break and the cell survives. In a BRCA-mutant cell, HR is broken, the double-strand break cannot be repaired, and the cell dies.

The principle is called *synthetic lethality* — two genetic defects, each tolerable alone, become lethal in combination. PARP inhibition alone is tolerable for normal cells. BRCA mutation alone is tolerable for cancer cells. Both together kill the cancer cells (because they have the BRCA defect) without harming normal cells (which still have BRCA function).

Olaparib was the first PARP inhibitor approved (in 2014, by the European Medicines Agency, for BRCA-mutant ovarian cancer). It has since been approved for BRCA-mutant breast, pancreatic, and prostate cancers. Talazoparib, rucaparib, and niraparib followed. The class is now a standard of care in BRCA-mutant cancers and is being expanded to other HR-deficient cancers (HRD-positive ovarian cancers that lack BRCA mutations but show genomic signatures consistent with HR defect — the HRD assay introduced clinically in 2019).

Resistance to PARP inhibitors emerges, of course. The most common mechanism is *reversion mutations* — a second mutation in BRCA1 or BRCA2 that restores the reading frame and produces a partially functional protein. Other mechanisms include loss of 53BP1 (which restores HR by alternative routes) and altered drug pharmacology. The clinical management of PARP-resistant disease is an active area.

The BRCA-PARP story has reshaped cancer biology in another way too. It established synthetic lethality as a workable principle for drug discovery. The search is now on for other synthetic lethal pairs — and several are in clinical development. WRN helicase inhibitors for microsatellite-instability-high cancers. MAT2A inhibitors for MTAP-deleted cancers. ATR inhibitors and CHK1 inhibitors for cancers with replication stress. Each one starts from a similar logic: identify the dependency that a specific genetic defect creates, then drug it.

---

## APC and Wnt signaling

APC is the colorectal cancer gene. About 80 percent of colorectal adenocarcinomas — both sporadic and familial — carry an inactivating APC mutation. APC mutations are typically the *earliest* genetic event in colorectal carcinogenesis, appearing in small adenomatous polyps before any other recurrent mutation.

The protein encoded by APC is a large (2,843 amino acid) scaffold protein that participates in the Wnt signaling pathway. The Wnt pathway controls proliferation in tissues that need constant replenishment — most importantly the intestinal epithelium, which is replaced every 3-5 days from stem cells at the base of intestinal crypts. The pathway works through a transcription factor called β-catenin. In the absence of Wnt signal, APC, together with axin, GSK3β, and CK1, forms a *destruction complex* that phosphorylates β-catenin and targets it for proteasomal degradation. β-catenin is constantly produced and constantly destroyed; its cytoplasmic level is kept low.

When a Wnt signal arrives — Wnt ligand binding to Frizzled receptors at the cell surface — the destruction complex is inactivated. β-catenin accumulates, enters the nucleus, partners with TCF/LEF transcription factors, and drives expression of target genes including MYC, cyclin D1, and others that promote proliferation.

When APC is mutated, the destruction complex fails. β-catenin accumulates regardless of upstream signal. The pathway is permanently on. The cell divides as if it were constantly receiving Wnt signaling. In the colon, this produces hyperproliferative crypts and, eventually, adenomatous polyps.

*Familial adenomatous polyposis (FAP)* is the inherited form of APC mutation. Affected individuals develop hundreds to thousands of colorectal adenomas, starting in adolescence. Without prophylactic colectomy, essentially every FAP patient develops colorectal cancer by age 40. FAP is rare (1 in 7,000 to 22,000 births) but its biology — one inherited APC mutation, many polyps, eventual cancer — has been a paradigm-defining example of tumor suppressor function.

Sporadic colorectal cancer follows a similar but slower trajectory. The first event is usually somatic biallelic APC inactivation in a single colonic stem cell. The polyp that grows from that cell accumulates additional mutations — KRAS (often next), SMAD4 or DCC, eventually TP53. The Vogelstein adenoma-carcinoma sequence (1988-1990) traced this molecular progression carefully, and it remains one of the cleanest examples of stepwise genetic progression in any human cancer.

Drugging the Wnt pathway has been difficult. The pathway has multiple feedback loops and many cell-type-specific components. Direct Wnt inhibitors (porcupine inhibitors, anti-Frizzled antibodies, tankyrase inhibitors) are in development but have produced limited responses. The therapeutic frontier for APC-mutant colorectal cancer is currently more about exploiting *downstream* dependencies than restoring the brake itself.

---

## PTEN and the PI3K pathway

PTEN is a phosphatase that opposes the PI3K signaling pathway. It is the second most commonly mutated tumor suppressor across cancers (after TP53). PTEN is lost in roughly 30 percent of glioblastomas, 50 percent of endometrial cancers, 20 to 50 percent of prostate cancers, and a substantial fraction of breast cancers.

The PI3K pathway, introduced briefly in Chapter 1 and Chapter 5, controls cell growth, metabolism, and survival. Active PI3K phosphorylates membrane phosphatidylinositol 4,5-bisphosphate (PIP2) to phosphatidylinositol 3,4,5-trisphosphate (PIP3). PIP3 recruits AKT to the membrane, where it is phosphorylated and activated. AKT then phosphorylates dozens of substrates that promote proliferation, glucose uptake, protein synthesis (via mTOR), and survival.

PTEN dephosphorylates PIP3 back to PIP2. It is the off switch for the pathway. Lose PTEN, and PIP3 accumulates, AKT remains active, the pathway fires constitutively.

What makes PTEN unusual is that *haploinsufficiency* matters. Many tumor suppressors require complete loss-of-function — both alleles inactivated — to manifest cancer phenotype. PTEN appears to be dose-dependent: even partial loss of function (one inactivated allele, or reduced expression of both) is enough to perturb the pathway in cancer-favoring directions. This makes PTEN a partial exception to Knudson's two-hit rule and helps explain why PTEN loss is so common — it does not require two precise inactivating events.

*Cowden syndrome* (PTEN hamartoma tumor syndrome) is the inherited form. Affected individuals develop multiple benign hamartomas and have elevated risks of breast, thyroid, endometrial, kidney, and colon cancers. The syndrome is rare but informative — it confirms PTEN's role as a tumor suppressor across multiple tissues.

PI3K pathway inhibitors — alpelisib (a PI3Kα-specific inhibitor approved for PIK3CA-mutant breast cancer), copanlisib, idelalisib, and others — partly target the same pathway from upstream. Their use is constrained by on-target toxicity (hyperglycemia, immunosuppression) reflecting the fact that the pathway has essential functions in normal cells.

---

## Mechanisms of inactivation

Tumor suppressors are inactivated in cancer by several mechanisms. The pattern is different from oncogene activation — instead of locking a protein "on" with one mutation, the cell needs to *lose* function, typically from both copies.

**Point mutations** in tumor suppressors are usually loss-of-function — nonsense mutations, frameshift indels, splice-site mutations. Most truncate the protein or destabilize it. TP53 is the exception: most of its mutations are missense in the DNA-binding domain, with dominant-negative properties that allow one mutant allele to compromise the function of the wild-type allele.

**Loss of heterozygosity (LOH)** is the second event in the Knudson model. The cell carrying one mutated tumor-suppressor allele loses the wild-type allele through a chromosomal mechanism — deletion of the wild-type chromosome region, mitotic recombination converting heterozygous to homozygous, gene conversion, or whole-chromosome loss. LOH at known tumor-suppressor loci is one of the most common molecular features of cancers and can be detected by analysis of polymorphic markers across the genome.

**Large deletions** can eliminate a tumor-suppressor gene entirely. CDKN2A (encoding p16) is located at 9p21, a region frequently lost in many cancers. RB1 at 13q14 is similarly lost in retinoblastomas and other cancers. These deletions sometimes encompass multiple tumor suppressors in a region; the *biallelic* deletion of CDKN2A often also removes CDKN2B and MTAP, with downstream consequences for treatment options (MTAP-deleted tumors are vulnerable to PRMT5 inhibitors via a synthetic-lethal mechanism currently in clinical development).

**Promoter hypermethylation** is the epigenetic equivalent of mutation. CpG islands in the promoter regions of tumor suppressor genes are normally unmethylated, allowing transcription. In cancers, these CpG islands often become heavily methylated, silencing transcription without altering the DNA sequence. MLH1 is silenced by promoter hypermethylation in sporadic colorectal cancers with microsatellite instability. p16 is silenced this way in many cancers. RB1 is occasionally silenced by methylation in some retinoblastomas.

The hypermethylation phenomenon is interesting because it is *reversible*. Drugs that inhibit DNA methyltransferases — azacitidine, decitabine — can reactivate silenced tumor suppressors in some contexts. These drugs are FDA-approved for myelodysplastic syndromes and acute myeloid leukemia and are being investigated more broadly. The epigenetic-therapy concept extends to histone-modifying enzymes (HDAC inhibitors, EZH2 inhibitors, DOT1L inhibitors, IDH1/2 inhibitors) — drugs that target the broader chromatin machinery that maintains silenced states.

**Viral inactivation** is the mechanism in HPV-driven cancers. HPV E6 binds and degrades p53. HPV E7 binds and degrades Rb. The virus does not mutate the host's tumor-suppressor genes — it just removes the protein products, functionally equivalent to loss-of-function. HPV-positive head and neck cancers and cervical cancers therefore have functional loss of both p53 and Rb even though the genes themselves are typically wild-type.

---

## Synthetic lethality as a unifying principle

The BRCA-PARP story is the cleanest example of how tumor-suppressor loss creates therapeutic vulnerability. The deeper principle — *synthetic lethality* — is reshaping cancer drug discovery.

Synthetic lethality refers to a relationship between two genes where loss of either gene alone is tolerable but loss of both is lethal. In cancer therapy, the logic is: a tumor has lost one gene (a tumor suppressor) that normal cells still have. If we can find another gene whose function is essential *only* in cells that have lost the first gene, we can selectively kill the cancer.

BRCA + PARP is the prototype. BRCA mutations alone are tolerable for cells (with caveats). PARP inhibition alone is tolerable for cells. Both together are lethal. Normal cells, with functional BRCA, survive PARP inhibition. BRCA-mutant cancer cells do not.

Other synthetic lethal pairs in clinical development:

*WRN helicase + microsatellite instability.* MSI-high cancers carry massive numbers of TA-repeat mutations that create non-B DNA structures requiring WRN helicase for resolution. Microsatellite-stable cancers tolerate WRN loss. WRN inhibitors selectively kill MSI-high cancers.

*PRMT5 + MTAP deletion.* MTAP is frequently co-deleted with CDKN2A. MTAP-deleted cells accumulate MTA, a metabolic intermediate that inhibits PRMT5. The cells become uniquely sensitive to additional PRMT5 inhibition.

*ATR + ATM-mutant cancers.* ATR and ATM are parallel kinases in the DNA damage response. Cancers that have lost ATM are more dependent on ATR. ATR inhibitors selectively kill ATM-deficient tumors.

*PARP + BAP1 mutations* in mesothelioma. *USP1 + BRCA1* loss in breast cancer. The list keeps growing.

The conceptual move synthetic lethality makes is to *turn tumor suppressor loss into a vulnerability*. For decades, tumor-suppressor cancers were considered harder to drug than oncogene-driven cancers — there is no "off switch" for a gene that has already been lost. Synthetic lethality reframes the question. The thing the cell is missing is not the target. The target is whatever the cell now needs that its normal counterpart did not. Loss creates dependency. Dependency is druggable.

---

## What this chapter gives you

Tumor suppressor genes are the brakes on cell proliferation, the guardians of DNA integrity, the failsafes against accumulating damage. Their loss — typically through inactivation of both alleles — removes the restraints that normally keep cells in tissue-appropriate behavior. The combination of accelerated growth (oncogene activation) and lost restraint (tumor-suppressor loss) is what produces the cancer phenotype. Almost every cancer carries mutations in both categories.

The major tumor suppressors — TP53, RB1, BRCA1/2, APC, PTEN — share a common logic but cover different cellular functions. TP53 integrates stress signals and decides between repair, arrest, senescence, and apoptosis. RB1 gates entry into S phase. BRCA1/2 enable accurate repair of double-strand breaks. APC controls Wnt signaling. PTEN opposes PI3K signaling. Loss of any one of them creates a specific cancer phenotype and, increasingly, a specific therapeutic vulnerability.

The therapeutic frontier — synthetic lethal targeting — has converted tumor-suppressor loss from a problem (you can't restore a missing protein with a drug) to an opportunity (you can drug the things the missing protein's absence makes the cell depend on). PARP inhibitors in BRCA-mutant cancers are the proof of concept; the broader pipeline is rapidly expanding.

The picture so far: Chapter 4 gave you the genetic substrate (mutations accumulating in a clonal lineage); Chapter 5 gave you the accelerators (oncogenes locked in active states); Chapter 6 has given you the brakes (tumor suppressors lost or silenced). Chapter 7 takes the next layer — the epigenetic landscape that overlays the genetic one and which cancers reshape extensively.

---

## LLM exercises

1. Ask your LLM to walk through the molecular mechanism by which HPV E6 degrades p53 and HPV E7 degrades Rb. Why does the virus need to inactivate both? Then probe: what does this tell us about the redundancy (or non-redundancy) of these two tumor suppressors?

2. Have your LLM construct the family tree of a person with Li-Fraumeni syndrome. What cancers appear at what ages? Generate a recommended screening protocol for an asymptomatic 25-year-old carrier — what tests, at what intervals, with what tradeoffs of benefit and harm.

3. Use your LLM to explain synthetic lethality to a non-scientist, using BRCA-PARP as the example. Then ask the LLM to propose three hypothetical synthetic lethal pairs not yet in clinical development. Evaluate which are biologically plausible and which are not. What makes the difference?

4. Have your LLM compare the inherited cancer syndromes — Li-Fraumeni (TP53), HBOC (BRCA1/2), Lynch (MMR genes), FAP (APC), retinoblastoma (RB1), VHL — in a single table. For each: lifetime cancer risk, which specific cancers, age of onset, screening recommendations, prophylactic interventions. Cross-check the numbers with a recent NCCN guideline or equivalent.

5. Ask your LLM to find a recent (2024 or later) phase 3 trial of a PARP inhibitor in a non-BRCA-mutant cancer with a homologous recombination deficiency signature. Walk through the trial design, the results, and the regulatory implications. How well does the synthetic lethality model predict the outcome — and where does the model break down?

---

##  AI Wayback Machine
The ideas in this chapter didn't appear from nowhere. **Suzanne Cory** has spent her career studying the genes that regulate cell death and B-cell development — including foundational work on the Bcl-2 family of tumor suppressors. She co-directed Australia's Walter and Eliza Hall Institute and trained generations of cancer biologists.

**Run this:**

```
Who is Suzanne Cory, and how does her work on Bcl-2 and B-cell genes connect to the tumor suppressor biology we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about her career or ideas.
```

→ Search **"Suzanne Cory"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to walk through how Bcl-2 was originally identified as a translocation partner in lymphoma — and what that revealed about apoptosis evasion.
- Ask it about Cory's leadership role in mentoring Australian women in cancer biology.

What changes? What gets better? What gets worse?
