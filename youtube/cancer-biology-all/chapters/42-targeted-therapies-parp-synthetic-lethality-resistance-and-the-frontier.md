# Chapter 42 — Targeted Therapies: PARP, Synthetic Lethality, Resistance, and the Frontier


## TL;DR

- The best targeted therapy isn't about hitting what cancer needs.
- The chapter moves through PARP inhibitors and synthetic lethality, Beyond BRCA: expanding PARP inhibitor indications, Other synthetic lethal approaches, CDK4/6 inhibitors: clinical implementation, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

The best targeted therapy isn't about hitting what cancer needs. It's about hitting what cancer can't survive without after you've already broken something else.

Hold the framing. The targeted therapy strategy of Chapter 24A — find the oncogene driving the cancer, inhibit it, watch the cancer collapse — works dramatically in cancers driven by clear oncogene addiction. But many cancers don't have a single dominant druggable oncogene. They have lost tumor suppressors (TP53, RB1, BRCA1/2, APC), they have complex multi-factorial driving biology, they have alterations that aren't directly druggable. For these cancers, a different framework is needed.

*Synthetic lethality* is that framework. Two genetic alterations, each tolerable alone, are lethal in combination. Cancer cells with one alteration become vulnerable to a drug that exploits the second. Normal cells, without the first alteration, are spared. The strategy turns loss-of-function mutations (which can't be "inhibited" directly) into therapeutic opportunities.

The cleanest example is PARP inhibitors in BRCA-mutant cancers. BRCA mutation alone is tolerable for the cancer cell (with caveats). PARP inhibition alone is tolerable for the normal cell. Both together are lethal in BRCA-mutant cancer cells (because they have the BRCA defect) but not in normal cells (which still have BRCA function). The principle has launched a new generation of cancer therapy that complements the oncogene-addiction approaches.

This chapter — the second on targeted therapy — covers PARP inhibitors and synthetic lethality, returns to other targeted therapy classes (CDK4/6 inhibitors, angiogenesis inhibitors) in their clinical implementation context, examines resistance mechanisms across targeted therapies, and surveys the future directions of the field including emerging targets, combinations, and approaches.

Hold the question: *if many cancers can't be addressed by hitting a single oncogene addiction, what else can we do?*

---

## PARP inhibitors and synthetic lethality

The biology of PARP inhibitors was introduced in Chapter 6 (tumor suppressors) in the context of BRCA1/2 and DNA repair. The clinical story is worth detailed treatment here because it represents one of the major successes of synthetic lethal therapeutics.

The mechanism: PARP (poly-ADP-ribose polymerase) is an enzyme involved in repair of single-strand DNA breaks through the base excision repair pathway. PARP1 is the major isoform. When PARP detects a single-strand break, it binds the break, becomes activated, and adds poly-ADP-ribose chains to itself and other proteins. This recruits repair factors and signals for repair to proceed.

PARP inhibitors block this activity in two ways:
1. *Catalytic inhibition*. They block PARP enzymatic activity, preventing the recruitment of repair factors.
2. *PARP trapping*. They stabilize the PARP-DNA complex, preventing PARP from dissociating from the break site. The trapped complex becomes a roadblock for DNA replication.

In normal cells with functional homologous recombination (HR), PARP inhibition produces some single-strand breaks that progress to double-strand breaks during replication, but the double-strand breaks are repaired accurately by HR. The cells survive.

In BRCA-mutant cancer cells with deficient HR, the double-strand breaks can't be repaired accurately. The cells use error-prone alternative pathways (alt-NHEJ, microhomology-mediated end joining) that produce genomic chaos and cell death. The synthetic lethal effect.

The clinical story:

*Olaparib* (Lynparza) was the first PARP inhibitor approved (2014, European Medicines Agency; 2014, FDA for BRCA-mutant ovarian cancer). Subsequent approvals expanded to:
- Maintenance therapy after platinum response in BRCA-mutant ovarian cancer.
- Treatment of BRCA-mutant metastatic breast cancer.
- Maintenance therapy in HRD-positive ovarian cancer.
- Treatment of BRCA-mutant metastatic prostate cancer.
- Maintenance therapy after platinum response in BRCA-mutant pancreatic cancer.

*Niraparib* (Zejula). Approved 2017. Maintenance therapy for ovarian cancer regardless of BRCA status (with greater benefit in BRCA-mutant or HRD-positive disease).

*Rucaparib* (Rubraca). Approved 2016. Initially for BRCA-mutant ovarian cancer; expanded to other indications.

*Talazoparib* (Talzenna). Approved 2018. The most potent PARP-trapping inhibitor. Approved for BRCA-mutant breast cancer and for prostate cancer (in combination with enzalutamide).

The clinical benefits have been substantial. In ovarian cancer, maintenance PARP inhibitor therapy after platinum response extends progression-free survival by years in many patients. Some patients have remained on PARP inhibitor maintenance for 5+ years. Overall survival benefits have been demonstrated in some settings.

The toxicities are generally manageable:
- *Myelosuppression*. Anemia, thrombocytopenia, neutropenia. Generally moderate; sometimes dose-limiting.
- *Fatigue*. Common.
- *Nausea and vomiting*. Generally mild with prophylaxis.
- *Hepatotoxicity*. Monitoring needed.
- *Secondary malignancies*. Small risk of myelodysplastic syndrome and acute leukemia, especially with prolonged use after prior chemotherapy.

The PARP inhibitor story has been transformative for BRCA-mutated cancers and has validated the synthetic lethal therapeutic approach.

---

## Beyond BRCA: expanding PARP inhibitor indications

The success of PARP inhibitors in BRCA-mutated cancers has driven exploration of *homologous recombination deficiency (HRD)* as a broader biomarker.

*HRD assays*. Tests that measure genomic scars indicating impaired HR. Several commercial assays (Myriad MyChoice, FoundationOne CDx with HRD score, others) attempt to identify HR-deficient tumors beyond those with simple BRCA mutations. The tests examine loss of heterozygosity (LOH), telomeric allelic imbalance (TAI), and large-scale state transitions (LST).

*HRD-positive non-BRCA ovarian cancer*. Substantial subset that responds to PARP inhibitors despite BRCA wild-type status. Maintenance therapy with niraparib is approved for this population.

*HRD-positive prostate cancer*. About 20-30% of prostate cancers have HR defects (BRCA1, BRCA2, ATM, CHEK2, RAD51, PALB2, others). Olaparib and other PARP inhibitors are approved for HRD-positive metastatic prostate cancer.

*Other cancers under investigation*. Pancreatic cancer (BRCA-mutated), breast cancer (HRD-positive), endometrial cancer, others.

The broader HRD framework has expanded PARP inhibitor utility substantially. Implementation challenges remain — different HRD assays produce somewhat different results; the optimal cutoffs are debated; some "HRD-positive" tumors may not be as responsive as BRCA-mutant ones.

---

## Other synthetic lethal approaches

Beyond PARP inhibitors, several other synthetic lethal approaches are in clinical development:

*WRN helicase inhibitors* for microsatellite-instability-high cancers. MSI-H cancers depend on WRN helicase to manage the unusual DNA structures they generate. WRN inhibitors selectively kill MSI-H cells. In clinical trials.

*PRMT5 inhibitors* for MTAP-deleted cancers. About 15% of all cancers have CDKN2A deletion that co-deletes MTAP. MTAP-deleted cells accumulate MTA (methylthioadenosine), which inhibits PRMT5. Additional PRMT5 inhibition is selectively lethal. PRMT5 inhibitors (AMG-193, MRTX1719, others) are in clinical trials.

*ATR inhibitors* for ATM-deficient cancers and replication-stress-high cancers. ATR and ATM are parallel checkpoint kinases. Cancers with ATM loss become more dependent on ATR. ATR inhibitors (ceralasertib, others) are in clinical trials.

*WEE1 inhibitors* for p53-mutated or replication-stress-high cancers. Wee1 enforces the G2 checkpoint. Cells with p53 loss depend more heavily on the G2 checkpoint. Wee1 inhibition pushes them through inappropriate mitosis. Adavosertib and others in clinical trials.

*MAT2A inhibitors* for MTAP-deleted cancers. Alternative approach to PRMT5 in MTAP-deleted disease. In clinical trials.

*POLQ inhibitors* for HR-deficient cancers. Polymerase theta provides backup repair when HR fails. Inhibiting POLQ in HR-deficient cancers should produce another layer of synthetic lethality. In early clinical development.

*ATM/ATR/DNA-PK inhibitors* in various combinations. The DDR field has multiple emerging targets.

*USP1 inhibitors* for BRCA-deficient cancers. USP1 deubiquitinates FANCD2 and PCNA, supporting alternative repair pathways. USP1 inhibition in BRCA-deficient cells produces synthetic lethality. KSQ-4279 and others in clinical trials.

The synthetic lethal approach has the potential to address many cancers that lack classical oncogene addiction. The challenge is identifying the right partner genetic alteration and the right drug. Multiple combinations are being explored.

---

## CDK4/6 inhibitors: clinical implementation

CDK4/6 inhibitors were discussed in Chapter 9B (cell cycle) and Chapter 23A (breast cancer combinations). The clinical implementation deserves additional attention.

The three approved CDK4/6 inhibitors (palbociclib, ribociclib, abemaciclib) differ in some details:

*Palbociclib* (Ibrance). The first approved (2015). Selective CDK4/6 inhibitor. Major dose-limiting toxicity is neutropenia. Discontinuous dosing (3 weeks on, 1 week off) allows hematologic recovery.

*Ribociclib* (Kisqali). Approved 2017. Similar mechanism. Specific concerns include QT prolongation (ECG monitoring required), liver toxicity, and rare cases of severe drug-induced lung disease. Has shown overall survival benefit in some breast cancer trials.

*Abemaciclib* (Verzenio). Approved 2017. Different toxicity profile (more diarrhea, less neutropenia) due to different kinase selectivity (more activity against CDK4 vs CDK6, plus some other activities). Can be given continuously. Has FDA approval for adjuvant high-risk early breast cancer (monarchE trial), making it the first CDK4/6 inhibitor for early-stage disease.

The CDK4/6 inhibitors are now standard of care for HR-positive HER2-negative metastatic breast cancer in combination with endocrine therapy. The improvements in PFS (typically 10-12 months added) and (in some studies) OS are substantial.

Beyond breast cancer, CDK4/6 inhibitors are being tested in many other contexts: mantle cell lymphoma (palbociclib has approval), liposarcoma with CDK4 amplification, lung cancer, head and neck cancer, others. The activity varies; the specific molecular requirements for response are being refined.

Resistance to CDK4/6 inhibitors involves loss of RB1, cyclin E1 amplification, FAT1 loss, and other mechanisms. CDK2 inhibitors are being developed to address cyclin E1-amplified resistance.

---

## Angiogenesis inhibitors: clinical lessons

Angiogenesis inhibition was covered in Chapter 12B. The clinical lessons are worth re-emphasizing in the targeted therapy context.

The initial vision of anti-angiogenic therapy (Folkman, 1971) was tumor starvation. The clinical reality has been more modest. Bevacizumab, the multi-kinase inhibitors targeting VEGFR (sunitinib, sorafenib, others), and related agents produce real but modest survival benefits in approved indications.

The reframing through *vascular normalization* (Jain and colleagues) has been more clinically useful. Anti-angiogenic therapy improves tumor vasculature in a window of opportunity, enabling better drug delivery and reducing immunosuppressive hypoxia.

The current clinical state:
- *Bevacizumab* approved for colorectal, lung, glioblastoma, ovarian, cervical, hepatocellular, and other cancers.
- *Multi-kinase inhibitors* (sunitinib, sorafenib, pazopanib, cabozantinib, lenvatinib, regorafenib, others) approved for renal cell carcinoma, hepatocellular carcinoma, thyroid cancer, GIST, soft tissue sarcoma, colorectal cancer, others.
- *Ramucirumab* (anti-VEGFR2) approved for gastric, lung, hepatocellular, colorectal cancers.

The most exciting development has been combinations of anti-angiogenic therapy with immune checkpoint inhibitors. The mechanistic rationale (anti-angiogenic agents normalize the immunosuppressive tumor microenvironment, improving immune therapy effectiveness) has been borne out in several approved combinations:
- Atezolizumab + bevacizumab in hepatocellular carcinoma.
- Pembrolizumab + axitinib in renal cell carcinoma.
- Lenvatinib + pembrolizumab in endometrial cancer.
- Cabozantinib + nivolumab in renal cell carcinoma.

These combinations are now standards of care in their respective indications.

---

## Resistance to targeted therapy

Resistance to targeted therapy is essentially universal in metastatic cancer. The mechanisms fall into several categories:

*Target alterations*. The cancer modifies the target so the drug no longer binds effectively.
- *Secondary mutations* in the target. Examples: T790M in EGFR (after first-/second-generation EGFR inhibitor); G2032R and other ROS1 mutations; G1202R in ALK; T315I in BCR-ABL; gatekeeper mutations in various kinases; specific BRAF resistance mutations; ESR1 mutations in breast cancer; AR mutations in prostate cancer.
- *Target amplification*. The cancer increases target expression to overcome inhibition. Common with BCR-ABL.

*Bypass signaling*. Alternative pathways activated to bypass the inhibited target.
- *MET amplification* as resistance to EGFR inhibitors.
- *RTK upregulation* (multiple receptors).
- *Downstream pathway activation* (MAPK reactivation in BRAF-inhibitor resistance; PI3K/AKT in various contexts).

*Phenotypic transformation*. The cancer changes its identity.
- *Small-cell transformation* of EGFR-mutant lung adenocarcinoma. The transformed cells lose EGFR dependence and acquire small-cell phenotype, requiring entirely different treatment.
- *Neuroendocrine transformation* in castration-resistant prostate cancer.
- *Mesenchymal transition* in various cancers.

*Loss of target dependence*. The cancer no longer needs the target. Various molecular mechanisms.

*Pharmacological resistance*. Drug doesn't reach the target.
- *Reduced cellular drug uptake*.
- *Increased drug efflux* through ABC transporters.
- *Drug metabolism*.

*Tumor microenvironment-mediated resistance*. CAFs, immune cells, and the microenvironment protect cancer cells.

The pattern across targeted therapies is similar — early response followed by resistance emergence at characteristic times. The biology of resistance has been characterized in detail for many targets, allowing development of next-generation drugs that address specific resistance mechanisms.

The general strategies for managing resistance:
- *Sequential targeted therapy*. Use next-generation drugs that address resistance mechanisms. Multiple generations of EGFR inhibitors, ALK inhibitors, BCR-ABL inhibitors illustrate this.
- *Combination therapy*. Hit multiple pathways simultaneously to prevent resistance through single-pathway alterations. BRAF + MEK inhibitors in melanoma is the classic case.
- *Liquid biopsy monitoring*. Detect resistance mutations early, allowing prompt switch to next-line therapy.
- *Adaptive therapy*. Vary treatment based on response and resistance dynamics.

---

## The future of targeted therapy

Several directions are reshaping the targeted therapy field:

*New targets becoming druggable*. Targets long considered "undruggable" are being addressed. KRAS G12C was undruggable for decades; now sotorasib and adagrasib are approved. KRAS G12D, G12V, and other variants are in advanced development. MYC, p53, and other classical undruggable targets remain difficult but are being approached through new strategies (PROTACs, molecular glues, allosteric inhibitors).

*PROTACs (proteolysis-targeting chimeras)*. Bifunctional molecules that bring an E3 ubiquitin ligase to a target protein, marking it for proteasomal degradation. Different from inhibitors — they cause target degradation rather than just blocking activity. Several PROTACs are in clinical trials (ARV-471 for ER-positive breast cancer; ARV-110 for AR-positive prostate cancer; bavdegalutamide; others targeting various proteins). The technology may make previously undruggable proteins targetable.

*Molecular glues*. Small molecules that promote protein-protein interactions, particularly with E3 ubiquitin ligases. Lenalidomide and pomalidomide work partly through this mechanism. New molecular glue degraders are in development.

*Allosteric inhibitors*. Drugs that bind sites other than the active site, providing different selectivity profiles and sometimes addressing resistance to active-site inhibitors. Asciminib in CML (allosteric BCR-ABL inhibitor) is a recent example.

*Covalent inhibitors*. Drugs that form covalent bonds with their targets. Provide prolonged target inhibition and can hit specific cysteine residues that allow exquisite selectivity (KRAS G12C inhibitors exemplify this).

*Multi-kinase rational design*. Drugs designed to hit specific combinations of kinases simultaneously, rather than the off-target activity of older multi-kinase inhibitors.

*Tumor-agnostic therapies*. The trend toward approving drugs across cancer types based on molecular features rather than tissue of origin will continue. NTRK fusion drugs, RET-targeted drugs, BRAF + MEK in BRAF V600E across cancers, microsatellite instability immunotherapy, and others have established the paradigm. More tumor-agnostic approvals are expected.

*Theranostics*. Combined molecular imaging and targeted radioligand therapy. PSMA-targeted approaches for prostate cancer. Somatostatin receptor approaches for neuroendocrine tumors. More targets and isotopes being developed.

*Targeted therapy + immunotherapy combinations*. Multiple FDA approvals already. The integration will deepen.

*Targeted therapy + ADC combinations*. Combining mechanism types.

*AI-assisted drug discovery*. Computational approaches identifying new targets and predicting drug behavior.

*Patient-derived models for drug testing*. Organoids, xenografts, and other models that predict individual patient drug responses.

The pace of targeted therapy development continues to accelerate. The next 5-10 years will likely bring approvals for many new targets and substantial expansion of currently approved targets to additional cancer types.

---

## Challenges and limitations

Despite the successes, targeted therapy faces significant challenges:

*Most cancers don't have actionable targets*. Even with comprehensive genomic profiling, only 30-50% of cancers harbor mutations matched to FDA-approved targeted therapies. Many cancers (pancreatic, glioblastoma, most sarcomas) have remained refractory to targeted approaches despite extensive efforts.

*Resistance limits durability*. Most targeted therapy responses are time-limited. The cancer evolves around the blockade. Sequential therapy can extend responses but doesn't typically produce cures in metastatic disease.

*Cost*. Targeted therapies are expensive — $100,000-200,000+ per year is common. The cost creates access disparities globally and financial toxicity for patients.

*Diagnostic infrastructure*. Comprehensive genomic profiling requires NGS-capable laboratories, bioinformatic expertise, and interpretation by molecular oncologists. This infrastructure is uneven across institutions and even more uneven across countries.

*Clinical trial access*. Patients with rare molecular alterations may not have access to appropriate clinical trials, especially if they don't live near major academic centers.

*Tumor heterogeneity*. Subclonal targets produce more modest responses than clonal targets. Heterogeneous tumors may have differential response across populations.

*Off-target effects*. Even "selective" inhibitors have other activities. Side effects are real and sometimes treatment-limiting.

*Resistance prediction*. Identifying who will respond and for how long remains imperfect.

The challenges suggest where future development should focus: addressing more cancers, more durable responses, lower costs, broader access, better diagnostic infrastructure, smarter combinations.

---

## What this chapter gives you

PARP inhibitors and synthetic lethality represent a major framework for targeting cancers without classical druggable oncogenes. BRCA-mutant cancers respond dramatically to PARP inhibitors through the synthetic lethal interaction between PARP inhibition and BRCA deficiency. HRD-positive cancers (beyond BRCA mutations) also benefit. The principle has launched a new generation of cancer therapies.

Other synthetic lethal approaches in clinical development include WRN inhibitors (MSI-H), PRMT5 inhibitors (MTAP-deleted), ATR inhibitors (ATM-deficient and replication-stress-high), WEE1 inhibitors, USP1 inhibitors, POLQ inhibitors, and others. The pipeline is expanding.

CDK4/6 inhibitors (palbociclib, ribociclib, abemaciclib) have become standard for HR-positive HER2-negative metastatic breast cancer in combination with endocrine therapy. Abemaciclib has FDA approval for adjuvant high-risk early breast cancer. The drugs differ in detail but produce similar benefits.

Angiogenesis inhibitors, reframed through the vascular normalization hypothesis, are most useful in combinations — particularly with immune checkpoint inhibitors (atezolizumab + bevacizumab in HCC, pembrolizumab + axitinib in RCC, lenvatinib + pembrolizumab in endometrial cancer, cabozantinib + nivolumab in RCC).

Resistance to targeted therapy is essentially universal in metastatic disease. The mechanisms include target alterations (secondary mutations, amplifications), bypass signaling, phenotypic transformation, loss of target dependence, pharmacological resistance, and tumor microenvironment effects. Strategies for managing resistance include next-generation drugs, combinations, liquid biopsy monitoring, and adaptive therapy.

Future directions include making more targets druggable (PROTACs, molecular glues, allosteric inhibitors, covalent inhibitors), tumor-agnostic therapies, theranostics, AI-assisted drug discovery, and integration with immunotherapy and ADCs.

Challenges include the fact that most cancers don't have actionable targets, resistance limits durability, cost creates access disparities, diagnostic infrastructure is uneven, and tumor heterogeneity complicates responses. Addressing these will require sustained investment and innovation.

Chapter 25 turns to cancer immunotherapy from a clinical implementation perspective — the practical aspects of using checkpoint inhibitors, CAR-T cells, cancer vaccines, and other immune-based therapies in real-world patient care.

---

## LLM exercises

1. Ask your LLM to walk through the discovery of the synthetic lethal relationship between BRCA and PARP. What were the key early experiments (Bryant et al., Farmer et al., 2005 Nature papers), how did the concept move from preclinical to clinical, and what does the timeline reveal about how translational science actually works?

2. Have your LLM compare the four major PARP inhibitors (olaparib, niraparib, rucaparib, talazoparib) in their mechanisms (PARP inhibition vs PARP trapping), pharmacokinetics, approved indications, and toxicity profiles. Identify which is preferred in specific clinical scenarios.

3. Use your LLM to explain the PRMT5-MTAP synthetic lethal axis in detail. What is the underlying biology of MTA accumulation in MTAP-deleted cells, how does this create PRMT5 vulnerability, and what is the status of clinical development for PRMT5 inhibitors? Identify the next steps in development.

4. Ask your LLM to walk through the major resistance mechanisms in EGFR-mutant lung cancer treated with osimertinib. What are the on-target resistance mutations (C797S, others), what are the bypass mechanisms (MET amplification, HER2 amplification, others), what is the role of small-cell transformation, and how is each managed?

5. Have your LLM survey the PROTAC field in oncology. What are the leading candidates in clinical trials (ARV-471 for ER, ARV-110 for AR, others), what are the proposed advantages over conventional inhibitors, and what targets are most likely to benefit from PROTAC approaches? Identify the most promising direction in PROTAC development.

---

##  AI Wayback Machine
The ideas in this chapter didn't appear from nowhere. **Alan Ashworth** showed in 2005 that PARP inhibitors selectively kill cells with BRCA mutations — a clinical demonstration of synthetic lethality. The result became olaparib, the first cancer drug designed around an explicit synthetic-lethal interaction.

**Run this:**

```
Who is Alan Ashworth, and how does his work on PARP inhibitors and synthetic lethality connect to the targeted therapy frontier we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.
```

→ Search **"Alan Ashworth"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to walk through the synthetic-lethal logic: why BRCA-mutant cells die when PARP is inhibited, but BRCA-wildtype cells survive.
- Ask it about resistance mechanisms that have emerged in BRCA-mutant cancers on PARP inhibitors.

What changes? What gets better? What gets worse?
