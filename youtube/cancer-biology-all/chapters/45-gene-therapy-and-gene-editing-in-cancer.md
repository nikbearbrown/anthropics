# Chapter 45 — Gene Therapy and Gene Editing in Cancer


## TL;DR

- We've spent the last century learning how cancer breaks genes.
- The chapter moves through The principles of gene therapy for cancer, Viral vectors for gene delivery, Non-viral gene delivery, CRISPR-Cas9 gene editing, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

We've spent the last century learning how cancer breaks genes. Now we're learning how to edit them back.

Hold the framing. Cancer is, at one level, a disease of genetic alterations — mutations that activate oncogenes, mutations that inactivate tumor suppressors, gene fusions, copy number changes. The conventional therapeutic response has been to target the *products* of those alterations: the proteins that result from the changed genes, the pathways they activate, the cellular behaviors they drive. Targeted therapy, immunotherapy, and chemotherapy all work downstream of the genetic alteration.

*Gene therapy* takes a different approach. It changes the genetics themselves. The patient receives a genetic intervention — a corrected gene to replace a defective one, an added gene to provide a therapeutic function, an edited gene to fix a mutation. The intervention happens at the DNA level. The downstream consequences depend on the cellular response to the modified genetic information.

The conceptual appeal is enormous. If cancer is caused by genetic changes, fixing those changes should address the disease at its root. The practical reality has been more complex. Gene therapy has had a long, sometimes troubled history in oncology. Early trials encountered safety problems (insertional mutagenesis from viral vectors, immune reactions). The technologies for delivering genes to the right cells at the right level have been hard to develop. Many promising concepts haven't translated to clinical success.

But the field has progressed. CRISPR-based gene editing has matured into a clinically applicable technology. Viral vector design has become more sophisticated. CAR-T cells (Chapter 25B) are arguably the most successful gene therapy in oncology — engineered T cells with introduced CAR genes. The newer wave includes in vivo gene editing approaches, novel delivery systems, and combinations with other modalities.

This chapter — the first of two on gene therapy and oncolytic virotherapy — covers the principles of cancer gene therapy, the major delivery systems (viral vectors and non-viral approaches), and the gene editing technologies (CRISPR-Cas9 and others) increasingly applied to cancer. The next — 26B — covers oncolytic virotherapy and current clinical applications.

Hold the question: *if cancer's foundation is genetic alteration, how do we intervene at the genetic level — and what gets in the way?*

---

## The principles of gene therapy for cancer

Gene therapy delivers genetic material to cells to produce therapeutic effects. In cancer, the strategies fall into several categories:

*Gene replacement*. Delivering a functional copy of a tumor suppressor gene that the cancer has lost. The concept: cancers with TP53 deletion would be treated by delivering functional TP53 to restore the cell's protective machinery. The reality: tumor suppressor replacement has been technically challenging — delivering enough gene to enough cells to produce a clinical effect requires highly efficient delivery, which has been hard to achieve.

*Gene editing*. Correcting specific mutations or introducing specific changes to the cancer cell's DNA. The concept: a specific oncogenic mutation could be repaired, eliminating the driver of cancer. The reality: editing every cancer cell is challenging; even small numbers of unedited cells can re-establish the disease.

*Suicide gene therapy*. Delivering a gene that converts a prodrug into a toxic agent specifically in cancer cells. The classical approach uses herpes simplex virus thymidine kinase (HSV-tk) gene; cells expressing HSV-tk convert ganciclovir to a toxic phosphorylated form that kills the cell. The concept: deliver HSV-tk to cancer cells, then give ganciclovir, killing the cancer. Has been tested in glioblastoma and other cancers with limited success.

*Immunomodulatory gene therapy*. Delivering genes that enhance immune responses to cancer. Examples include cytokine gene therapy (delivering IL-12, GM-CSF, IL-2 genes to recruit immune responses) and tumor antigen genes (delivering specific antigens to prime immune responses).

*Engineered cell therapy*. The most successful gene therapy in oncology. T cells (CAR-T, TCR-T), NK cells, macrophages are engineered with introduced genes to acquire new functions. Discussed in Chapter 25B.

*RNA-based therapies*. Delivering RNA (mRNA for therapeutic proteins; siRNA for gene silencing; antisense oligonucleotides) to modulate cellular function. The mRNA vaccine technology proven in COVID-19 is being applied to cancer (personalized neoantigen vaccines, Chapter 25B).

The diversity of approaches reflects the diversity of mechanisms by which gene therapy can affect cancer. Some approaches work directly on cancer cells; others work through immune effects; others through systemic effects.

---

## Viral vectors for gene delivery

Most gene therapy uses viruses as vectors. Viruses evolved to deliver their genetic material to cells; they are repurposed to deliver therapeutic genes. The major vector types:

*Retroviruses* (specifically lentiviruses are widely used). RNA viruses that integrate their genetic material into the host cell genome through reverse transcription. The integration is permanent — the introduced gene is inherited by daughter cells.

Advantages: stable, long-term expression of the introduced gene.

Disadvantages: random insertion site can disrupt cellular genes or activate proto-oncogenes (insertional mutagenesis). The risk has been demonstrated clinically — several X-linked severe combined immunodeficiency (SCID) patients treated with retroviral gene therapy developed leukemia from insertional activation of LMO2. Modern lentiviral vectors have safety features (self-inactivating LTRs, insulator sequences) to reduce but not eliminate this risk.

Use in cancer: CAR-T manufacturing (the introduced CAR gene is delivered via lentiviral vector); some ex vivo gene therapy approaches.

*Adeno-associated viruses (AAV)*. Small DNA viruses with several distinctive properties. They infect cells without integrating into the host genome (mostly remaining as extrachromosomal episomes). Different serotypes have tissue-specific tropism (AAV2 broadly; AAV8 liver-tropic; AAV9 CNS and cardiac tropic; AAV5 retinal). They are generally non-pathogenic in humans.

Advantages: relatively safe (no integration), long-term expression in non-dividing cells, tissue-specific delivery through serotype selection.

Disadvantages: limited cargo capacity (about 4.7 kb), can be neutralized by pre-existing anti-AAV antibodies, expression diluted in dividing cells, immune responses can develop and limit duration of expression.

Use in cancer: largely limited so far; some emerging applications.

*Adenoviruses*. Larger DNA viruses with high transduction efficiency in many cell types. They don't integrate. Replication-competent (oncolytic) versions are used in oncolytic virotherapy (Chapter 26B); replication-defective versions are used for gene delivery.

Advantages: high transduction efficiency, large cargo capacity (up to about 8-30 kb), well-characterized.

Disadvantages: strong immune responses limit repeated dosing, transient expression (no integration), pre-existing immunity in most patients.

Use in cancer: some gene therapy applications; oncolytic virotherapy variants.

*Herpes simplex virus*. Large DNA virus with large cargo capacity. Used in oncolytic virotherapy (T-VEC, Chapter 26B) and some gene therapy applications.

*Vaccinia and other poxviruses*. Used as vaccines and as gene delivery vectors.

*Vesicular stomatitis virus (VSV)*, *Newcastle disease virus*, *measles virus*, and others — primarily for oncolytic applications.

Each vector has its own advantages and limitations. The choice depends on the application — target cell type, required cargo size, desired duration of expression, safety considerations.

---

## Non-viral gene delivery

Non-viral approaches to gene delivery avoid some of the safety concerns of viral vectors but typically have lower delivery efficiency.

*Lipid nanoparticles (LNPs)*. Lipid-based particles that encapsulate genetic material and deliver it to cells. The technology was scaled dramatically by the COVID-19 mRNA vaccines (Pfizer/BioNTech, Moderna). Advantages include scalable manufacturing, no integration risk, and broad target cell access.

LNPs for cancer applications: delivery of mRNA encoding therapeutic proteins or tumor antigens. Personalized neoantigen mRNA vaccines (Chapter 25B) use LNP delivery.

*Cationic polymers* (polyethylenimine, others). Synthetic polymers that condense DNA into nanoparticles for delivery. Lower efficiency than LNPs but useful for some applications.

*Electroporation*. Brief electrical pulses temporarily permeabilize cell membranes, allowing entry of DNA. Used ex vivo for some cell engineering applications.

*Gene guns*. Particle bombardment of cells with DNA-coated micro-particles. Used historically; less common now.

*Hydrodynamic injection*. Rapid injection of large volumes of DNA solution under pressure. Used in research; not standard for clinical gene therapy.

The non-viral approaches generally have lower delivery efficiency than viral vectors but can be advantageous for safety, scalability, and re-dosing.

---

## CRISPR-Cas9 gene editing

CRISPR-Cas9 has revolutionized gene editing since its publication in 2012 (Jinek, Charpentier, Doudna; Cong, Zhang group separately). The system uses an RNA-guided nuclease (Cas9) to cut DNA at specific sequences, allowing precise modification.

The mechanism:
1. *Guide RNA (gRNA)* is designed with a 20-nucleotide sequence complementary to the target DNA site.
2. *Cas9 protein* binds the gRNA, forming the Cas9-gRNA complex.
3. The complex finds the target site in the genome (requiring a *protospacer adjacent motif* or PAM — typically NGG for SpCas9 — at the 3' end of the target site).
4. *Cas9 cleaves DNA*, producing a double-strand break.
5. The cell's DNA repair machinery repairs the break, often imperfectly. *Non-homologous end joining (NHEJ)* typically produces insertions or deletions (indels) at the break site, disrupting gene function. *Homology-directed repair (HDR)*, less common, can use a provided template to introduce specific changes.

The technology allows:
- *Gene knockout*. Creating indels that disrupt gene function. The most common use.
- *Gene correction*. Using HDR to repair specific mutations.
- *Gene insertion*. Adding new sequences at specific locations.
- *Gene regulation*. Modified Cas9 (catalytically inactive — "dead" Cas9 or dCas9) can be used to activate or repress genes without cutting DNA.

CRISPR variants and improvements:
- *Base editors* (Liu lab and others, 2016 onward). Modified Cas9 fused to deaminase enzymes that can change one base to another without cutting DNA. C-to-T editors (CBE) and A-to-G editors (ABE) enable precise single-base changes.
- *Prime editors*. Use a Cas9 nickase fused to reverse transcriptase and a prime editing guide RNA. Allow precise edits without double-strand breaks.
- *Cas12 (Cpf1)* and *Cas13*. Alternative CRISPR enzymes with different properties (Cas12 has shorter PAM requirements; Cas13 cuts RNA rather than DNA).
- *Improved specificity*. Multiple modifications to Cas9 reduce off-target effects.
- *Different delivery systems*. RNP delivery (ribonucleoprotein complexes, with Cas9 protein and gRNA pre-assembled) avoids the need for cellular DNA expression.

The applications in cancer:

*Ex vivo CRISPR in cellular therapy*. CRISPR is used in CAR-T and other cellular therapy manufacturing to enhance cell function or to make off-the-shelf products. Examples:
- *Allogeneic CAR-T*. CRISPR knockout of TCR and HLA genes to prevent graft-versus-host disease and rejection.
- *Enhanced CAR-T*. CRISPR knockout of immune checkpoint genes (PD-1, TGF-β receptor) to improve CAR-T function.
- *Universal CAR-T*. Multiple gene edits to create a single product usable across many patients.

*In vivo gene editing*. Delivering CRISPR components directly to cells in the patient. Technically much more challenging but in clinical development. Examples include in vivo TTR knockout for amyloidosis (not cancer but proof of principle); in vivo lipid-mediated CRISPR delivery to liver and other tissues for various applications including cancer.

*CRISPR screens for drug discovery*. Whole-genome CRISPR screens identify essential genes in cancer cells, prioritizing candidate drug targets. The Cancer Dependency Map (DepMap) project has cataloged dependencies across many cancer cell lines.

*Tumor-specific CRISPR therapy*. Delivering CRISPR specifically to tumor cells to edit driver mutations or essential genes. Technically challenging but conceptually attractive.

*Casgevy* (exa-cel) is the first FDA-approved CRISPR therapy (2023, for sickle cell disease and beta-thalassemia, not cancer). The approval demonstrates the clinical feasibility of CRISPR-based therapy and paves the way for oncology applications.

The CRISPR field is moving rapidly. New variants, better delivery, broader applications. The cancer applications are accelerating, particularly through cellular therapy modifications and emerging in vivo approaches.

---

## Other gene editing technologies

CRISPR has dominated the gene editing field since 2012, but other technologies exist and have specific advantages:

*Zinc finger nucleases (ZFNs)*. The first programmable nucleases for gene editing. Composed of zinc finger protein domains for DNA recognition fused to nuclease domains. More technically demanding to design than CRISPR but with established safety record. Sangamo Therapeutics has developed clinical ZFN-based products.

*TALENs (transcription activator-like effector nucleases)*. Similar concept to ZFNs but using TAL effector proteins for DNA recognition. More modular than ZFNs but still less convenient than CRISPR.

*Meganucleases*. Naturally occurring rare-cutting endonucleases, engineered for specific target sites.

*Base editing and prime editing*. CRISPR-based but distinct from standard CRISPR-Cas9 in mechanism. Discussed above.

The choice among editing technologies depends on the application. CRISPR offers convenience and broad applicability. ZFNs and TALENs may have advantages for specific high-precision applications or where CRISPR's broad reach is undesirable.

---

## Specific cancer gene therapy approaches in development

Several specific gene therapy approaches in cancer are in clinical development:

*p53 gene therapy*. Restoring wild-type p53 function in tumors with p53 loss. Various delivery vehicles (adenoviral vectors, others). Has had limited clinical success despite extensive testing.

*BRCA gene therapy*. Restoring BRCA function in BRCA-mutated cancers as an alternative to PARP inhibitor therapy. In early development.

*Cytokine gene therapy*. Local delivery of cytokine genes to tumor sites. The introduced gene produces cytokines (IL-12, GM-CSF, others) that recruit immune responses. Local injection approach minimizes systemic toxicity.

*Suicide gene therapy*. HSV-tk + ganciclovir approaches in various cancers. Limited clinical success.

*Tumor-specific oncolytic gene therapy*. Viral vectors that replicate selectively in cancer cells. Discussed in detail in 26B.

*CAR-T and other engineered cellular therapy*. The most successful gene therapy in oncology. Discussed in Chapter 25B.

*Allogeneic CAR-T with CRISPR*. Multiple gene edits create off-the-shelf products. Several in clinical trials.

*mRNA-based therapy*. Delivering mRNA encoding therapeutic proteins or tumor antigens via LNPs. Personalized neoantigen vaccines (Chapter 25B). Emerging applications include mRNA encoding tumor-specific TCRs (combining engineering with mRNA delivery).

*siRNA and antisense oligonucleotides*. Silencing specific gene expression. Several drugs approved for non-cancer indications; cancer applications largely in development.

*Aptamers*. Short RNA or DNA sequences that bind specific targets with high affinity. Various cancer applications in development.

The pipeline is diverse but most approaches remain investigational. CAR-T cells remain the dominant clinical gene therapy in oncology as of 2026.

---

## Challenges in cancer gene therapy

Gene therapy faces several persistent challenges in cancer:

*Delivery*. Getting genetic material to enough cancer cells to produce a clinical effect remains difficult. Cancer cells are distributed throughout the body (especially metastatic disease); systemic delivery requires the gene therapy to reach all of them. Tumor microenvironment factors (dense matrix, immunosuppression, vasculature problems) impede delivery.

*Specificity*. Targeting cancer cells specifically while sparing normal cells. Most delivery systems have some off-target effects. Tumor-specific promoters (driving expression only in cancer cells) help but are imperfect.

*Efficacy*. Even when genes are delivered, the therapeutic effect must outweigh the cancer's intrinsic drivers. Restoring a single tumor suppressor doesn't necessarily eliminate cancer that has accumulated many alterations.

*Immune responses*. The patient's immune system may neutralize the gene therapy vector (especially adenoviruses and AAV with pre-existing immunity), or react against the gene therapy product itself. Immune responses can limit repeat dosing.

*Safety*. Insertional mutagenesis (especially with retroviral vectors), off-target effects of editing, immune reactions, and other safety concerns require careful monitoring.

*Manufacturing*. Producing gene therapy products at scale, with consistent quality, is technically demanding. The cost reflects this complexity.

*Cost*. Approved gene therapies are expensive ($100,000-3,000,000+ per treatment). The cost creates substantial access barriers.

*Regulatory pathway*. Gene therapy regulation has evolved as the field has matured. Long-term follow-up requirements add to development costs.

These challenges have limited the broader application of gene therapy in cancer. CAR-T cells have succeeded partly because they address several of these challenges — ex vivo manipulation avoids in vivo delivery limitations; lentiviral integration provides durable expression; the patient's own cells avoid major rejection issues.

The challenges are real but not insurmountable. The field continues to develop, with new approaches addressing each major limitation. The next decade will likely see more approved cancer gene therapies, both engineered cellular therapies and (potentially) in vivo gene editing approaches.

---

## What this chapter gives you

Gene therapy and gene editing represent fundamental approaches to cancer treatment that act at the genetic level rather than at the protein or cellular level. The strategies include gene replacement (restoring lost tumor suppressors), gene editing (correcting mutations), suicide gene therapy (prodrug conversion), immunomodulatory gene therapy (enhancing immune responses), engineered cellular therapy (CAR-T and others), and RNA-based therapies.

Viral vectors are the dominant delivery system. Lentiviruses provide integrated, durable expression (used in CAR-T manufacturing); adeno-associated viruses provide non-integrating, tissue-specific delivery; adenoviruses provide high efficiency for transient applications; herpes simplex and other viruses serve specific purposes.

Non-viral delivery (lipid nanoparticles, cationic polymers, electroporation) avoids some viral vector safety concerns but typically has lower efficiency. LNPs have been transformative for mRNA-based therapy, scaled by COVID-19 vaccine development.

CRISPR-Cas9 has revolutionized gene editing since 2012. The system enables gene knockout (most common), gene correction, gene insertion, and gene regulation. CRISPR variants (base editing, prime editing, alternative Cas enzymes) expand the editing toolkit. The first FDA-approved CRISPR therapy (exa-cel for sickle cell disease, 2023) demonstrates clinical feasibility.

Other gene editing technologies (ZFNs, TALENs, meganucleases) have specific applications and remain in development alongside CRISPR.

Cancer gene therapy applications in development include p53 restoration, BRCA gene therapy, cytokine gene therapy, suicide gene therapy, tumor-specific oncolytic gene therapy (Chapter 26B), engineered cellular therapy (Chapter 25B), allogeneic CAR-T with CRISPR modifications, mRNA-based therapy, and RNA silencing approaches.

Challenges include delivery to all cancer cells, specificity for cancer over normal cells, sufficient efficacy, immune responses to vectors and products, safety (insertional mutagenesis, off-target effects), manufacturing complexity, high cost, and evolving regulatory requirements.

Despite these challenges, the field continues to progress. CAR-T cells remain the dominant clinical gene therapy in oncology. The next wave likely includes off-the-shelf cellular products, in vivo gene editing, and integration with other modalities.

Chapter 26B turns to oncolytic virotherapy — using viruses themselves as the cancer-targeting agent rather than as delivery vehicles for therapeutic genes.

---

## LLM exercises

1. Ask your LLM to walk through the evolution of CRISPR from initial publications (2012) to first FDA approval (Casgevy for sickle cell, 2023). What were the key technological milestones, what were the major challenges (delivery, off-target effects, immune responses), and what does the timeline tell us about the pace of clinical translation for novel technologies?

2. Have your LLM compare lentiviral, AAV, and adenoviral vectors for gene therapy. For each: the cargo capacity, integration vs. non-integration, immune response considerations, and the cancer applications each is most suited for. Identify which vector you would choose for a hypothetical p53 gene replacement therapy.

3. Use your LLM to explain how base editing and prime editing differ from standard CRISPR-Cas9. What can base editors do that standard CRISPR cannot, what can prime editors do, and what are the current clinical applications and limitations of each? Identify the cancer applications most likely to benefit from these newer technologies.

4. Ask your LLM to walk through the use of CRISPR in engineering allogeneic CAR-T cells. What specific gene edits are typically introduced (TCR knockout, HLA knockout, immune checkpoint knockouts, others), why are they needed, and what is the clinical status of allogeneic CAR-T products? Identify the major remaining challenges.

5. Have your LLM survey the in vivo gene editing field. What are the major approaches being explored (LNP-delivered CRISPR, viral vector-delivered editing, others), what are the cancer applications in early development, and what are the major challenges remaining? Identify the most promising direction for in vivo gene editing in cancer.

---

##  AI Wayback Machine
The ideas in this chapter didn't appear from nowhere. **Feng Zhang** demonstrated CRISPR-Cas9 gene editing in mammalian cells in 2013 — making targeted human genome editing practical. The technique now underlies most cancer gene-editing research and therapeutics.

![Feng Zhang](../images/feng-zhang-e6s.png)

*Puppet Art by [Nik Bear Brown](https://www.nikbearbrown.com/).*

**Run this:**

```
Who is Feng Zhang, and how does his work on CRISPR in mammalian cells connect to the gene therapy and editing we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.
```

→ Search **"Feng Zhang"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to walk through how a CRISPR-Cas9 guide RNA targets a specific gene for editing in a human cell.
- Ask it about the patent dispute between the Broad Institute (Zhang) and Berkeley (Doudna/Charpentier) over CRISPR.

What changes? What gets better? What gets worse?
