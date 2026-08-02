# Chapter 25 — Tumor Immunology: Surveillance, Antigens, and the Immune Response


## TL;DR

- This chapter gives a working overview of Tumor Immunology: Surveillance, Antigens, and the Immune Response, focusing on the ideas a reader needs before moving to the next chapter.
- The chapter moves through The immunosurveillance hypothesis, What makes a cancer cell different?, Neoantigens in detail, The adaptive immune response, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

The immune system can cure cancer. The trick is convincing it to.

Hold the sentence. The history of cancer immunology is one of perpetual oscillation between hope and disappointment, until about 2010 — when the disappointment ended. Coley's toxins in the 1890s produced some real but inconsistent responses by inducing fevers in cancer patients (likely activating innate immunity). BCG instillation for bladder cancer in the 1970s produced cures in some patients (working through immune mechanisms). Interleukin-2 in the 1980s produced durable responses in a minority of melanoma and renal cell carcinoma patients but at brutal toxicity. The conviction that the immune system *could* cure cancer was supported by these scattered successes; the inability to make it work reliably was the obstacle.

The obstacle fell with the discovery and clinical validation of the immune checkpoints — the molecular brakes that tumors use to disable T cells. CTLA-4 was identified as a negative regulator of T cell activation by Pierre Goldstein in the 1990s and translated by James Allison into a therapeutic blockade strategy that yielded ipilimumab, approved for melanoma in 2011. PD-1 and PD-L1 were characterized by Tasuku Honjo and colleagues in the 1990s and translated into nivolumab, pembrolizumab, and other antibodies that have since transformed the treatment of more than 20 cancer types. Allison and Honjo shared the 2018 Nobel Prize in Physiology or Medicine. The immunotherapy revolution is now in its second decade and continues to reshape oncology.

This is the first of two chapters on tumor immunology. This one — 16A — covers the immune system's interactions with cancer: the immunosurveillance hypothesis, the antigens that distinguish cancer from normal cells, the innate and adaptive immune responses, and the mechanisms by which tumors evade these responses. The next — 16B — covers the immunotherapeutic strategies that exploit this biology: checkpoint inhibitors, cellular therapies (CAR-T, TIL, TCR-T), cancer vaccines, and combinations.

Hold the question: *what makes a cancer cell different enough from a normal cell that the immune system can recognize it as a threat?*

---

## The immunosurveillance hypothesis

The idea that the immune system continuously patrols the body and eliminates incipient cancers is old. Paul Ehrlich proposed it in 1909, though the immunological details were not yet understood. Lewis Thomas in 1959 and Macfarlane Burnet in 1970 articulated the *immunosurveillance hypothesis* in modern terms: the immune system recognizes and eliminates transformed cells before they grow into clinical cancers. Clinical cancer represents failures of immunosurveillance.

The hypothesis was contested for decades because the supporting evidence was indirect. Then in the 1990s and 2000s, mouse models with specific immune deficiencies (RAG knockout mice lacking T and B cells; IFN-γ pathway knockout mice; perforin knockouts) showed dramatically elevated rates of spontaneous tumors. The genetic immune deficiency states confirmed that intact immunity protects against cancer.

In humans, the evidence converges. Immunocompromised patients (HIV/AIDS, transplant recipients on immunosuppression, congenital immunodeficiencies) have substantially elevated rates of certain cancers — virally driven cancers especially (Kaposi sarcoma, lymphomas, HPV-related cancers) but also non-virally driven cancers at modestly increased rates. The relationship is strongest for virally driven cancers because the immune system contains both the cancer cell and the virus driving it.

The current framework is sometimes called *cancer immunoediting* (Robert Schreiber and colleagues, early 2000s). It has three phases:

*Elimination*. The immune system recognizes and eliminates incipient cancer cells. Most transformed cells are killed before they form a tumor.

*Equilibrium*. Some cells survive elimination by acquiring resistance to immune attack. They are not eliminated but are held in check by ongoing immune pressure. The cells persist in a dormant or slow-growing state. The equilibrium can last years or decades — this is one form of cancer cell dormancy (Chapter 13B).

*Escape*. Eventually, some cells acquire mutations or epigenetic changes that allow them to escape immune pressure entirely. These cells expand into clinically detectable cancer. The escape phase is what we see when we diagnose cancer.

The framework explains several observations: the lag between when a cancer-initiating event occurs and when a tumor becomes clinically detectable; the appearance of cancers in immunosuppressed patients of cells that were presumably in the equilibrium phase; the dormancy that follows curative-intent surgery in some patients; and the variability of cancer outcomes that may reflect different immune capacity.

The framework also has therapeutic implications. If patients with established cancer have failed immunosurveillance, perhaps the failure can be reversed — the immune system can be reactivated to once again attack the tumor. This is the conceptual foundation of immunotherapy.

---

## What makes a cancer cell different?

For the immune system to attack a cancer cell, the cell must look sufficiently different from a normal cell. The question of *what makes cancer cells visible to the immune system* has been worked out over decades and forms the molecular basis of immunotherapy.

The major categories of *tumor antigens* — proteins or other molecules on cancer cells that the immune system can recognize:

*Tumor-specific antigens (TSAs)*. Antigens that exist only on cancer cells, never on normal cells. These are the cleanest targets because immune responses to them won't damage normal tissue.

- *Viral antigens*. Cancer cells transformed by oncogenic viruses (HPV, EBV, HBV, HCV) often express viral proteins. The E6/E7 oncoproteins of HPV in cervical and oropharyngeal cancer. EBV antigens in EBV-associated lymphomas and nasopharyngeal carcinoma. These antigens are foreign to the body and can be recognized as such.

- *Neoantigens*. Antigens arising from cancer-specific mutations. A point mutation in a gene that produces a new amino acid in the protein can create a peptide fragment that the immune system has never encountered. These neoantigens are tumor-specific and personalized to each patient's tumor.

*Tumor-associated antigens (TAAs)*. Antigens expressed on cancer cells but also on some normal cells, usually at low levels or in restricted contexts. Recognition of these antigens can drive anti-tumor responses but also risks attacking normal tissues.

- *Cancer-testis antigens (CTAs)*. Proteins normally expressed only in germ cells (testis) and in early embryonic development, but aberrantly re-expressed in some cancers. MAGE-A1, NY-ESO-1, and others. Because germ cells don't express MHC class I, immune attack on cancer-testis antigens spares normal tissues outside the testis.

- *Differentiation antigens*. Proteins expressed in specific cell lineages. Tyrosinase in melanocytes (and melanoma). PSA and PSMA in prostate cells (and prostate cancer). CD19, CD20 in B cells (and B-cell lymphomas). Immune attack on these antigens can damage normal cells of the same lineage but may still be acceptable if the affected normal cells are dispensable (B cells can be replaced; prostate function can be replaced).

- *Overexpressed antigens*. Proteins expressed at low levels in normal cells but at very high levels in cancer cells. HER2 in HER2-amplified breast cancer. EGFR in EGFR-amplified cancers. The high expression density allows immune attack with relative specificity.

*Posttranslationally modified antigens*. Proteins with cancer-specific modifications — glycosylation patterns, citrullination, phosphorylation patterns — that distinguish them from normal proteins.

For each category, the immune system's recognition machinery must engage with the antigen in a specific molecular context. For T cells, the antigen must be a peptide presented on MHC class I (for CD8+ T cells) or MHC class II (for CD4+ T cells). For B cells and antibodies, the antigen must be accessible at the cell surface or in the extracellular fluid.

---

## Neoantigens in detail

The *neoantigen* concept has become central to modern immunotherapy. A neoantigen is a peptide sequence derived from a cancer-specific mutation — most commonly a missense mutation that changes one amino acid in the protein and produces a fragment the immune system has not seen before.

Why are neoantigens special? Because they are completely tumor-specific, they cannot induce *central tolerance*. The immune system's T cell repertoire is shaped by deletion during thymic development of T cells that strongly recognize self-peptides. Self-peptides include all the normal proteins of the body, including their normal post-translational variants. Self-tolerant T cells will not attack normal cells but may be activated by neoantigens because the mutant peptide was never present during thymic education.

Neoantigen production scales with mutation burden. Tumors with high mutation burden (microsatellite-instability-high cancers, smoking-related lung cancers, melanoma with UV signature, POLE-mutant cancers) produce many neoantigens. Tumors with low mutation burden (pediatric cancers, some hematological cancers, leiomyosarcoma) produce few. The correlation between mutation burden and response to immune checkpoint inhibitors reflects this — higher mutation burden produces more neoantigens, which produces more potential T cell targets, which produces better immunotherapy response.

The bioinformatic challenge of neoantigen identification is significant. From a tumor's mutation profile, computational tools predict which mutations produce peptides that:
1. Are presented on the patient's specific MHC molecules (each patient has six MHC class I alleles, each presenting different peptides).
2. Are different enough from the wild-type peptide to be recognized as foreign.
3. Are derived from sufficiently expressed proteins to generate enough peptide for presentation.
4. Have sufficient binding affinity to the MHC molecule.

Tools like NetMHC, MHCflurry, and others predict MHC binding with reasonable accuracy. Tumor RNA sequencing confirms expression. Mass spectrometry can directly identify peptides actually presented on MHC. Combining these analyses produces neoantigen lists that can guide vaccine design or T cell receptor selection for personalized immunotherapy.

The neoantigen approach has produced exciting early clinical data. *Personalized cancer vaccines* — designed for the specific neoantigens of a patient's tumor — have shown activity in melanoma, glioblastoma, pancreatic cancer, and others. Companies like BioNTech and Moderna have advanced neoantigen vaccine development. The technology is still maturing but represents one of the most exciting directions in cancer immunotherapy.

---

## The adaptive immune response

When the immune system mounts an effective anti-tumor response, the central effector cells are T cells, especially CD8+ cytotoxic T cells (CTLs).

The basic sequence:

1. *Antigen capture and presentation*. Dendritic cells (DCs) in the tumor microenvironment encounter dying or damaged cancer cells. They take up cancer-derived antigens (through phagocytosis or pinocytosis) and process them. Antigens degraded in the proteasome are loaded onto MHC class I molecules for presentation to CD8+ T cells. Antigens degraded in endosomes are loaded onto MHC class II for CD4+ T cells.

2. *DC migration and maturation*. The antigen-loaded DCs migrate to the nearest lymph node. They mature into the *immunostimulatory phenotype* with elevated MHC, co-stimulatory molecules (CD80, CD86), and cytokines.

3. *T cell priming*. In the lymph node, the DC presents the antigen to T cells. T cells whose receptors specifically recognize the antigen-MHC complex are activated. The T cells receive the *first signal* from the antigen-MHC complex binding to their T cell receptor (TCR), the *second signal* from co-stimulation through CD28 binding CD80/CD86, and *third signals* from cytokines (IL-12, IL-2, type I interferons).

4. *T cell expansion and differentiation*. Activated T cells proliferate massively over days. CD8+ T cells differentiate into cytotoxic effectors. CD4+ T cells differentiate into Th1 (anti-tumor) or other subsets.

5. *T cell migration to the tumor*. Effector T cells leave the lymph node and circulate. Chemokine signals (CXCL9, CXCL10, CXCL11 produced in inflamed tumors) attract T cells to the tumor site. The cells extravasate into the tumor parenchyma.

6. *T cell-mediated killing*. T cells contact cancer cells. The cytotoxic T cell recognizes its specific antigen on MHC class I on the cancer cell. It engages and kills the cancer cell through perforin/granzyme (forming pores and delivering apoptosis-inducing proteins) and through FAS ligand and TRAIL (extrinsic apoptosis pathway). Multiple killings per CTL are possible.

7. *Memory formation*. After the response, most effector T cells die. A small fraction become long-lived *memory T cells* that persist and can rapidly respond if the antigen is encountered again.

The sequence is robust when it works. The problems in cancer come at multiple steps. DCs in the TME are often dysfunctional. T cell priming is suppressed by regulatory T cells and immunosuppressive cytokines. T cell migration into the tumor is impeded by chemokine deficits and physical barriers. T cell killing in the tumor is suppressed by checkpoint receptors and metabolic factors. Memory formation may be compromised in chronic immune responses.

---

## Innate immunity in cancer

Beyond the adaptive immune response, *innate immunity* plays important roles in cancer.

*Natural killer (NK) cells* are innate lymphoid cells that kill virus-infected and tumor cells through perforin/granzyme and FAS/TRAIL pathways, similar to CTLs but without antigen-specific recognition. NK cells use *missing-self recognition* — they kill cells that have downregulated MHC class I (which is what some tumor cells do to evade CTL attack). They also use *stress-ligand recognition* — they kill cells expressing stress-induced ligands like MICA, MICB, ULBP1-6, which are upregulated on damaged or transformed cells. NK cells are essential against tumors that have downregulated MHC I to evade T cells.

*Macrophages* can have anti-tumor activity. M1-polarized macrophages kill cancer cells through reactive nitrogen species, TNFα, and antibody-dependent cellular cytotoxicity (ADCC). In tumors, however, macrophages are often M2-polarized and immunosuppressive.

*Dendritic cells* bridge innate and adaptive immunity by presenting antigens. Different DC subsets have different roles. Plasmacytoid DCs produce type I interferons in response to viral or tumor-derived nucleic acids. Conventional DCs (cDC1, cDC2) present antigens to T cells.

*Inflammasomes* in immune cells respond to cellular damage and pathogen signals by producing IL-1β and IL-18. Inflammasome-driven inflammation can be either anti-tumor (immunogenic cell death) or pro-tumor (chronic inflammation supporting cancer).

*Innate lymphoid cells (ILCs)*. A diverse family of immune cells including NK cells and several other subsets. ILC1, ILC2, ILC3 have different cytokine profiles and tissue distributions. Their roles in cancer are still being characterized.

*Complement system*. Plasma proteins that can opsonize cancer cells for phagocytosis or directly lyse them through membrane attack complexes. Some antibody therapies (rituximab) work partly through complement-dependent cytotoxicity.

The interplay between innate and adaptive immunity is essential. Innate immunity recognizes pathogen and damage signals and initiates inflammation. Inflammation recruits adaptive immune cells. Adaptive immunity is amplified by innate co-stimulation. Failures in either compartment compromise anti-tumor immunity.

---

## How tumors evade immunity

Cancer cells that survived immunosurveillance and reached clinical detection have, by definition, evaded immune attack. The mechanisms of evasion are diverse and overlapping.

*Loss of antigen presentation*. Cancer cells downregulate MHC class I expression, reducing visibility to CD8+ T cells. They downregulate components of the antigen presentation machinery (TAP transporters, β2-microglobulin, the proteasome). Tumors with low MHC expression are invisible to CTLs.

*Loss or modification of specific antigens*. Through *immunoediting*, tumors lose specific tumor antigens that elicited immune responses. The cells that remain present fewer or weaker antigens. Memory T cell responses become less effective.

*Active immunosuppression*. Cancer cells and TME components secrete immunosuppressive factors: TGF-β (broad suppression of T cell, NK cell, and DC function), IL-10 (suppression of T cell responses and APC function), indoleamine 2,3-dioxygenase (IDO; tryptophan depletion suppressing T cell proliferation), and others.

*Recruitment of suppressive cells*. Regulatory T cells, MDSCs, M2 macrophages, and tolerogenic DCs are recruited to the tumor and actively suppress anti-tumor immunity (Chapter 14A).

*Checkpoint receptor signaling*. The molecular basis of much of immunotherapy. Cancer cells and TME components express ligands for inhibitory receptors on T cells. PD-L1 (on tumor cells and macrophages) binds PD-1 on T cells, suppressing T cell function. CTLA-4 on activated T cells and Tregs competes with CD28 for CD80/CD86 binding, reducing co-stimulation. LAG-3, TIM-3, TIGIT, BTLA, VISTA — additional checkpoint receptors with their own ligands. The system has many layers of negative regulation that tumors exploit.

*Metabolic immune suppression*. Lactate accumulation, oxygen depletion, glucose competition, amino acid depletion — all reduce T cell function in the TME (Chapter 14B).

*Physical exclusion*. Dense matrix, abnormal vasculature, and disorganized tumor architecture impede T cell infiltration. "Excluded" tumors have T cells at the periphery but not in contact with cancer cells.

*Tolerance induction*. Tumors can actively induce T cell anergy or exhaustion. Chronic antigen exposure without proper co-stimulation drives T cells into hypofunctional states with high expression of inhibitory receptors and reduced cytotoxic capacity. *Exhausted T cells* are a major target for reactivation by checkpoint inhibitors.

The evasion mechanisms operate in combination. A typical "cold" or immunosuppressive tumor has reduced antigen presentation plus active immunosuppression plus recruited suppressor cells plus checkpoint signaling plus metabolic suppression. Restoring effective anti-tumor immunity requires addressing multiple mechanisms — which is one reason combination immunotherapy is increasingly used.

---

## What this chapter gives you

The immune system continuously surveys the body for transformed cells and eliminates most of them before they develop into clinical cancer (immunosurveillance). Cancers that reach clinical detection have, through immunoediting, evolved to escape this surveillance. The three phases — elimination, equilibrium, escape — describe the dynamic interaction between cancer and immunity.

Tumor antigens are the molecular targets of anti-tumor immune responses. Tumor-specific antigens (viral antigens, neoantigens from cancer-specific mutations) are cleanest because they don't exist on normal cells. Tumor-associated antigens (cancer-testis antigens, differentiation antigens, overexpressed antigens) are present on cancer cells but also on some normal cells. Neoantigens — derived from somatic mutations — are particularly valuable because they cannot induce central tolerance.

The adaptive immune response against cancer relies on dendritic cells presenting antigens to T cells in lymph nodes, T cell priming with proper co-stimulation, T cell expansion and differentiation, T cell migration to the tumor, and T cell-mediated killing. Each step can be compromised in cancer.

Innate immunity contributes through NK cells (especially against MHC-low tumors), macrophages, dendritic cells, inflammasomes, ILCs, and complement. The interplay between innate and adaptive immunity is essential for effective anti-tumor responses.

Tumors evade immune attack through multiple mechanisms: loss of antigen presentation, antigen modification, active immunosuppression by secreted factors, recruitment of suppressive cells, checkpoint receptor signaling, metabolic immune suppression, physical exclusion, and tolerance induction. The mechanisms operate in combination and require comprehensive approaches to overcome.

Chapter 16B turns to the therapeutic side: how immunotherapy has reshaped oncology through checkpoint inhibitors, cellular therapies, and cancer vaccines. The clinical successes are dramatic in some cancer types and modest in others. Understanding why these therapies work — and where they fail — connects directly to the immunology covered here.

---

## LLM exercises

1. Ask your LLM to walk through the cancer immunoediting framework (Schreiber and colleagues). What are the three phases (elimination, equilibrium, escape), what evidence supports each, and how does the framework explain clinical observations like cancer dormancy and the cancers seen in immunocompromised patients?

2. Have your LLM compare the major categories of tumor antigens — viral antigens, neoantigens, cancer-testis antigens, differentiation antigens, and overexpressed antigens. For each: the specificity, the immunogenicity, the therapeutic accessibility, and an example cancer where each is most relevant.

3. Use your LLM to explain why tumor mutational burden (TMB) correlates with response to immune checkpoint inhibitors. What is the mechanistic basis (neoantigens), what cancers have particularly high TMB, and what cancers have low TMB? Identify the limitations of TMB as a biomarker.

4. Ask your LLM to construct the molecular pathway from dendritic cell uptake of tumor antigen through to T cell killing of a cancer cell. At each step, identify what can go wrong in cancer (what evasion mechanisms operate at each step), and which therapeutic interventions address each.

5. Have your LLM compare CD8+ T cell, NK cell, and macrophage-mediated tumor killing. What are the distinguishing molecular mechanisms, when does each contribute most, and which cancers are vulnerable to each? Identify the most promising therapeutic strategy targeting each effector cell type.

---

##  AI Wayback Machine
The ideas in this chapter didn't appear from nowhere. **Lloyd J. Old** spent his career identifying tumor-specific antigens — including the cancer/testis antigens like NY-ESO-1 — and was one of the first to insist tumor immunology was a serious field. He trained much of the modern immunotherapy community.

**Run this:**

```
Who was Lloyd J. Old, and how does his work on tumor antigens connect to the tumor immunology we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.
```

→ Search **"Lloyd J. Old"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to walk through how Old identified NY-ESO-1 as a cancer/testis antigen — and why those antigens are attractive immunotherapy targets.
- Ask it about Old's founding role at the Cancer Research Institute and the Ludwig Cancer Research network.

What changes? What gets better? What gets worse?
