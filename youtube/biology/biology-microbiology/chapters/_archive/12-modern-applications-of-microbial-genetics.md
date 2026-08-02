# Chapter 12 — Modern Applications of Microbial Genetics

*The tools we use to study microbes are mostly tools we stole from them.*

## The question before the answer

In 1968, a Swiss molecular biologist named Werner Arber was studying a strange phenomenon: when bacteriophages were grown on one strain of *E. coli* and then transferred to another strain, the phages often could not reproduce. Some kind of mechanism in the new host was destroying the incoming viral DNA. Arber called the phenomenon **restriction**.

Within a few years, the mechanism had been worked out. Bacteria contain enzymes called **restriction endonucleases** that recognize specific short DNA sequences and cut DNA at those sequences. Their function is to defend against incoming foreign DNA — phage genomes, transferred plasmids — by chopping it up. The bacterium protects its own DNA from these enzymes by chemically modifying (methylating) the same recognition sequences within its own chromosome, so they're invisible to the restriction enzyme.

This is one of those discoveries whose immediate scientific importance was overshadowed by its tool value. Restriction enzymes turned out to be precision DNA scissors. They cut at predictable sites. They produced predictable ends. They could be purified and used in test tubes. The ability to cut DNA at specific sequences, and then to re-join the pieces in arrangements of your choosing, was the foundational technology of modern molecular biology.

The story of this chapter is that almost every tool we use to manipulate DNA — restriction enzymes, ligases, polymerases, plasmid vectors, reverse transcriptase, CRISPR-Cas9 — was discovered in microorganisms first and adapted as a laboratory reagent second. Microbes invented this technology before we did. We just learned how to use it.

## Learning objectives

By the end of this chapter, you will be able to:

1. Describe how restriction enzymes cut DNA and explain why specific recognition sequences enable precise cloning.
2. Walk through the basic steps of making a recombinant DNA molecule and transforming it into a bacterial host.
3. Distinguish DNA libraries from PCR products as means of obtaining a specific gene sequence.
4. Explain how gel electrophoresis separates DNA fragments and how Southern, Northern, and Western blots use that separation.
5. Describe genomics, transcriptomics, and proteomics, and explain what each tells you about an organism.
6. Discuss the technical mechanisms, risks, and ethical issues of gene therapy.

Prerequisites: Chapters 10 and 11 especially, plus Chapters 1–9.

## Tools borrowed from microbes

Before getting to applications, let me list the borrowed parts. Each of these is a real microbial protein with a function in nature; we use them in test tubes.

**Restriction endonucleases**. Discovered by Arber, Daniel Nathans, and Hamilton Smith (Nobel Prize 1978). Hundreds of restriction enzymes are now characterized, each cutting at a specific recognition sequence. EcoRI, from *E. coli*, cuts at GAATTC, producing "sticky ends" that match the same sequence elsewhere — ideal for joining two pieces of DNA. HindIII, BamHI, NotI, and many others are workhorses of molecular cloning.

**DNA ligases**. Catalyze the joining of two DNA strands. T4 DNA ligase, from bacteriophage T4, is the most commonly used. It can join any two DNA ends, including blunt ends, given enough enzyme and time.

**DNA polymerases**. Taq polymerase, from the hot-spring bacterium *Thermus aquaticus*, is heat-stable and is the enzyme that made PCR (polymerase chain reaction) practical. Pfu polymerase, from *Pyrococcus furiosus*, is also thermostable but has proofreading activity, used when fidelity matters. Bacterial polymerases of many types are sold as reagents.

**Reverse transcriptase**. From retroviruses (Chapter 6). Used to convert RNA into DNA for sequencing and cloning. The basis of RT-PCR.

**RNA polymerases**. T7 RNA polymerase, from bacteriophage T7, is widely used to transcribe DNA into RNA in vitro. SP6 and T3 polymerases serve similar functions.

**Plasmid vectors**. Modified bacterial plasmids that carry the gene you want to clone, plus a selectable marker (typically an antibiotic resistance gene), plus origins of replication that work in your host of choice.

**CRISPR-Cas systems**. From bacterial adaptive immunity against phages. We will get to this.

The pattern is consistent: microbes invented enzymes to copy DNA, cut DNA, join DNA, transcribe DNA, edit DNA, defend against foreign DNA. We adopted those enzymes for our own purposes. The history of biotechnology is largely the history of finding which microbial enzyme does what we want and figuring out how to use it.

## Molecular cloning

The basic procedure for cloning a gene is fifty years old and is essentially unchanged.

**Step 1**: cut the source DNA with a restriction enzyme that flanks the gene of interest.

**Step 2**: cut a plasmid vector with the same restriction enzyme, opening up the circular plasmid at one site.

**Step 3**: mix the source DNA and the cut plasmid in the presence of DNA ligase. The sticky ends from the restriction cut will base-pair, and ligase will seal the bonds. The result is a recombinant plasmid containing the gene of interest inserted into the vector.

**Step 4**: introduce the recombinant plasmid into a bacterial host (typically *E. coli*) by transformation. The bacteria take up the plasmid and replicate it along with their own DNA.

**Step 5**: select for bacteria that received the plasmid. Most commonly, the plasmid carries an antibiotic resistance gene. Plating the transformation on agar containing the antibiotic kills bacteria without the plasmid and lets the resistant ones grow into colonies. Each colony is a clonal population descended from a single transformant.

**Step 6**: identify which colonies received the right insert. This is usually done by some combination of PCR, restriction mapping, and sequencing of the plasmid recovered from individual colonies.

**Step 7**: scale up. A colony with the correct construct can be grown overnight in liquid culture, producing milligrams of recombinant protein (if the gene is expressed) or microgram quantities of the plasmid for further work.

This procedure underlies the production of recombinant insulin (since 1982), recombinant human growth hormone, recombinant factor VIII for hemophilia, recombinant erythropoietin, recombinant interferons, recombinant vaccines (hepatitis B vaccine is made from yeast carrying a hepatitis B surface antigen gene), and a long list of other biologic drugs. The biotech industry is built on this seven-step procedure.

### Libraries

When you do not know exactly which DNA you want, you can make a **library**. A genomic library is a collection of bacterial colonies, each carrying a different piece of genomic DNA from a source organism, together covering the entire genome. A cDNA library is similar but is made from mRNA (reverse-transcribed to cDNA before cloning), so it represents only the genes being expressed in the source tissue.

Libraries can be screened in various ways to find a clone of interest. Nucleic acid probes — short single-stranded DNA labeled with a fluorophore or radioactive tag — can be hybridized to library colonies to identify ones carrying complementary sequences. Antibody probes can identify colonies producing the right protein. Sequencing can identify clones by genome position.

Most modern molecular biology has shifted away from libraries toward direct cloning of specific genes via PCR amplification. But libraries remain useful for some applications — particularly when characterizing genomes of organisms that cannot be easily handled in PCR.

## PCR — the polymerase chain reaction

In 1983, a biochemist named Kary Mullis was driving on Highway 128 in California, thinking about a problem, when an idea struck him. The idea was this: if you have a DNA template, two short primers flanking the region you want to copy, all four nucleotides, and a DNA polymerase, you can copy that region of DNA exponentially.

You add the ingredients to a tube and heat it to 95°C. The two strands of the template DNA separate. You cool to 50–60°C; the primers anneal to their complementary sequences on the template. You warm to 72°C; the polymerase extends each primer along its template, copying the region in between. You now have twice as much of that region as you started with.

You heat it again. The new copies and the original separate. Primers anneal. Polymerase extends. You now have four times as much. And then eight. And then sixteen. Thirty cycles produces 2³⁰ = a billion-fold amplification.

The polymerase chain reaction. **PCR**. Mullis won the Nobel Prize in 1993 for it. [^1] The technology has been so transformative that listing applications is futile — diagnostics (HIV testing, COVID testing), forensic DNA analysis, paternity testing, ancient DNA studies, monitoring gene expression, prenatal diagnosis, cloning genes for further work — PCR is in nearly every molecular biology pipeline.

The breakthrough was the discovery of thermostable polymerases — particularly Taq polymerase from *Thermus aquaticus*, isolated by Thomas Brock and Hudson Freeze from a hot spring in Yellowstone National Park in 1969. Taq survives the 95°C heating step that denatures the template DNA. Before Taq, every PCR cycle would have required adding fresh polymerase, making the procedure impractical. With Taq, you load all the reagents at the start and let a thermocycler run through the temperature steps automatically.

↳ **Dig Deeper — The basic-research-to-commercial-tool pipeline**

*Taq polymerase was isolated in 1969 by researchers studying extremophile microbiology with no commercial application in mind. It became a multi-billion-dollar reagent twenty years later.*

**Prompt:**
> Trace the path from Thomas Brock's 1969 isolation of *Thermus aquaticus* to the commercial success of Taq polymerase in PCR. Who patented Taq, when, and what was the legal history? How much money did the federal government make from royalties on a discovery originally funded by NSF basic research grants? Then identify three other extremophile enzymes that have become commercially important tools (you can include cryo-enzymes, Pfu polymerase, hyperthermophile DNA polymerases for higher-fidelity PCR).

**What to do with the output:** This is the most-cited case study for why basic research on weird organisms is worth funding. The economic return on extremophile microbiology has been enormous and was essentially impossible to predict.

The selection of an enzyme by an organism for survival in 70°C water at Yellowstone, twenty years before anyone thought of PCR, is part of why basic science about extremophiles is worth funding even when nobody can predict what use it will be put to. The use was waiting for the enzyme.

### Quantitative PCR

Standard PCR tells you whether a sequence is present. **Quantitative PCR** (qPCR or real-time PCR) tells you how much of it. The trick: add a fluorescent dye or probe to the reaction that becomes more fluorescent as more product accumulates. Read the fluorescence after every cycle. The cycle at which fluorescence crosses a threshold is inversely related to the starting amount of template — more template means earlier threshold crossing.

qPCR is the workhorse of clinical viral load testing — measuring how much HIV RNA is in a patient's blood, how much hepatitis C, how much SARS-CoV-2. It can detect a few copies of a virus in a sample.

## Gel electrophoresis and the blots

To analyze DNA fragments produced by restriction digestion or PCR, you typically separate them by size. **Gel electrophoresis** does this by pulling DNA through a gel matrix (agarose for large DNA, polyacrylamide for small fragments) with an electric field. DNA is negatively charged (because of the phosphate backbone) and migrates toward the positive electrode. Smaller fragments move through the gel matrix faster than larger ones. The result is bands of DNA at different positions in the gel, sorted by size.

You stain the gel with a DNA-binding dye (ethidium bromide, traditionally; safer alternatives now) and visualize under UV light. Each band is a population of DNA molecules of a particular size. By running standards alongside (a "ladder" of known fragment sizes), you can determine the size of unknown bands.

### Blots

**Southern blotting**, invented by Edwin Southern in 1975, transfers DNA from a gel onto a nitrocellulose or nylon membrane and probes it with a labeled DNA sequence. The probe binds to its complementary sequence, lighting up which band on the gel matches. This was the standard technique for detecting specific DNA sequences before PCR made it less necessary. [^2]

**Northern blotting** is the same idea applied to RNA — separating RNA by size on a gel, transferring to a membrane, probing with labeled nucleic acid to detect specific transcripts.

**Western blotting** is the same idea applied to proteins — separating proteins by size on a gel, transferring to a membrane, probing with labeled antibodies to detect specific proteins. The name is a pun on Southern; Northern and Western followed.

The blots are old techniques but still in use. Each gives you specificity (you can detect a particular sequence or protein) plus size information (you can see what size the molecule is, which often tells you something about its identity or post-translational modifications).

### RFLP

**Restriction Fragment Length Polymorphism** is a method for distinguishing two DNA samples by their restriction enzyme digestion patterns. If two samples differ by a single base in a restriction site, one will be cut and the other won't, producing different fragment patterns on a gel. RFLP analysis was a major tool in genetic mapping before PCR-based methods took over, and it is still used in some forensic and clinical applications.

## Microarrays

A **microarray** is a glass slide on which thousands of short DNA sequences have been spotted at specific locations. You hybridize a labeled sample (typically cDNA from a tissue) to the array. The labeled DNA binds to its complementary spots. By scanning the array for fluorescence at each spot, you measure how much of each transcript is present in your sample.

Microarrays were revolutionary in the 1990s and 2000s because they let you measure tens of thousands of gene expressions in a single experiment. You could compare healthy vs. diseased tissue, or treated vs. untreated cells, and see which genes were up- or down-regulated.

The technique has been largely superseded by **RNA-Seq** — sequencing all the mRNA in a sample directly. RNA-Seq has higher dynamic range, doesn't require knowing the genes in advance, and detects variants and splice forms that microarrays miss. Microarrays still have niches (cost, validated probe sets) but RNA-Seq is the default for most modern transcriptomics.

## Genomics, transcriptomics, proteomics

The three large-scale "-omics" approaches:

**Genomics**: sequencing entire genomes. The first bacterial genome (*Haemophilus influenzae*) was sequenced in 1995 by Craig Venter's group, using a "shotgun" approach — randomly fragmenting the DNA, sequencing the fragments, and assembling them computationally. [^3] The Human Genome Project (1990–2003) sequenced the human genome at a cost of about $3 billion. Today, a bacterial genome costs about $50 and a human genome about $200. The cost has dropped by roughly a million-fold in twenty years.

What you do with a genome: identify all the genes, infer metabolic capabilities from the gene list, identify virulence factors, identify antibiotic resistance genes, compare to related organisms to find unique features, design vaccines or therapeutics targeting specific gene products.

**Transcriptomics**: measuring which genes are expressed (and at what level) in a particular sample. RNA-Seq is now the standard. The transcriptome tells you what the cell is actually doing, as opposed to what it is capable of doing.

**Proteomics**: measuring which proteins are present (and at what level) in a sample. Mass spectrometry is the main tool. The proteome is closer to function than the transcriptome (because not all mRNA gets translated, and proteins are modified post-translationally) but harder to measure because proteins do not amplify.

All three -omics approaches together let you build a picture of an organism's biology at the molecular level. Combining them — looking at a microbe's genome to see what it could do, its transcriptome to see what it's doing now, and its proteome to see the actual molecular workforce — is the basis of much modern microbiology.

## Genetically engineered pharmaceuticals

The first recombinant pharmaceutical was insulin, produced commercially in 1982. Before then, insulin was extracted from pig and cow pancreases — a process that produced a slightly impure product, occasionally caused immune reactions, and was difficult to scale. The Genentech and Eli Lilly teams cloned the human insulin gene into *E. coli*, optimized the expression, and produced recombinant human insulin. The result was the first recombinant biologic on the market and the founding moment of the biotech industry.

Other recombinant biologics in clinical use:

- **Human growth hormone**: previously extracted from cadaver pituitaries, which transmitted CJD (Chapter 6) before recombinant production replaced the old source.
- **Factor VIII**: clotting factor for hemophilia A. Previously extracted from pooled plasma, which transmitted HIV and hepatitis C before recombinant production.
- **Erythropoietin (EPO)**: stimulates red blood cell production, used in anemia and in chronic kidney disease.
- **Interferons**: antiviral and immune-modulating proteins, used in hepatitis C, multiple sclerosis.
- **Monoclonal antibodies**: the largest current class of biologics. Each is a specific antibody produced by engineered cell lines, used to target cancer cells, inflammatory pathways, or specific pathogens. Trastuzumab, rituximab, infliximab, adalimumab — the "-mab" suffix tells you you're dealing with a monoclonal antibody.

## Gene therapy

Gene therapy is the introduction of a functional gene into a patient's cells to treat a disease — typically a disease caused by a defective gene.

The basic categories:

**Somatic gene therapy** modifies cells in the body that do not pass to offspring (most cells, including liver, blood, muscle, eye). Changes are limited to the patient.

**Germline gene therapy** modifies eggs, sperm, or embryos. Changes pass to all future generations of the patient's descendants. This is the controversial form and is currently banned for clinical use in most jurisdictions.

Approved gene therapies include:

- **Luxturna**: AAV-delivered RPE65 gene for inherited retinal disease.
- **Zolgensma**: AAV-delivered SMN1 gene for spinal muscular atrophy.
- **CAR-T therapies** (Yescarta, Kymriah): patient's T cells removed, engineered to express a chimeric antigen receptor targeting a tumor, and reinfused. Used for some leukemias and lymphomas.
- **Casgevy** (2023): the first FDA-approved CRISPR-based therapy, for sickle cell disease and beta-thalassemia. Patient's hematopoietic stem cells are removed, edited ex vivo with CRISPR to reactivate fetal hemoglobin, and reinfused.

The history of gene therapy includes several setbacks. The 1999 death of Jesse Gelsinger in a gene therapy trial for ornithine transcarbamylase deficiency triggered a major retraction of the field. Subsequent improvements in vector design (the move from adenovirus to AAV, the development of CAR-T approaches, the discovery of CRISPR) have made the technology more clinically viable. But every gene therapy still requires careful evaluation of risks: insertional mutagenesis (the inserted gene disrupting another gene), immune reactions to the vector, off-target editing in CRISPR cases.

### CRISPR-Cas9, briefly

The most consequential development in gene therapy in the past decade. CRISPR (clustered regularly interspaced short palindromic repeats) is a bacterial adaptive immune system. Bacteria use CRISPR-Cas systems to defend against phages: when a phage infects, the bacterium incorporates a piece of the phage's DNA into its own genome as a "spacer." If the same phage infects again, the bacterium produces an RNA copy of the spacer, which guides a Cas nuclease to find and cut the matching phage DNA.

The system can be programmed. By providing an artificial guide RNA, you can direct Cas9 (the most commonly used variant, from *Streptococcus pyogenes*) to cut any DNA sequence you specify. If you provide a repair template with the cut, the cell can repair the break using your template, effectively editing the genome.

Jennifer Doudna and Emmanuelle Charpentier shared the 2020 Nobel Prize in Chemistry for the development of CRISPR-Cas9 as a genome editing tool. [^4] The system was characterized in bacterial biology by 2007–2010, demonstrated as a genome editor in eukaryotic cells by 2013, and approved for clinical use in 2023. About a decade from concept to FDA-approved therapy. The pace has been unprecedented in gene therapy.

↳ **Dig Deeper — Beyond Cas9: the expanding CRISPR toolbox**

*Cas9 is the most famous CRISPR enzyme, but the system is much larger than that. New Cas variants and CRISPR-derived technologies are appearing constantly.*

**Prompt:**
> Survey the modern CRISPR toolbox beyond Cas9. Cover Cas12 (Cpf1) and its different cut pattern; Cas13 for RNA targeting and the SHERLOCK diagnostic system; base editors (cytosine and adenine base editors); prime editors; CRISPR activation and inhibition (CRISPRa/CRISPRi) for gene regulation without cutting; and CRISPR-derived diagnostics (the DETECTR and SHERLOCK platforms). For each, identify what new capability it adds and what its current clinical or research status is.

**What to do with the output:** The "CRISPR-Cas9" framing in most textbooks is already several years out of date. The field has fanned out into many specific tools, each suited to specific problems. Save the answer; carry forward to clinical chapters.

## Ethical issues, briefly

Gene therapy raises issues beyond the technical:

**Germline editing**. Modifying eggs, sperm, or embryos changes the genome of all future descendants of the modified individual. This is a one-way decision. There is essentially no consensus on what germline modifications should be allowed, even when technically possible. The 2018 announcement by He Jiankui that he had edited human embryos to disable CCR5 (an HIV co-receptor) and implanted them, producing two live births, was widely condemned. He served three years in prison in China.

↳ **Dig Deeper — He Jiankui in detail**

*The 2018 announcement of CRISPR-edited babies was one of the most consequential events in bioethics in recent decades. The details matter for understanding why the response was so uniformly negative.*

**Prompt:**
> Walk through what He Jiankui did in 2018. Cover: the science (CCR5 disruption as supposed HIV protection); the off-target editing he appears to have introduced; the consent process and what was inadequate about it; the medical justification (or lack thereof); the response from the international scientific community; and the legal consequences for He. Then discuss what specifically would need to be different — scientifically and ethically — for germline editing to be considered acceptable, if ever.

**What to do with the output:** This case will be in bioethics textbooks for the next century. Knowing the specifics rather than the cartoon version is worth the time. Save the answer.

**Access and equity**. Gene therapies are extraordinarily expensive — Zolgensma costs over $2 million per dose. The therapies that exist are accessible primarily to people in wealthy countries with good insurance. Whether this is acceptable, and what to do about it, is a major area of ongoing debate.

**Enhancement vs. therapy**. Most discussion focuses on using gene therapy to treat disease. Whether the same techniques should be used for enhancement — selecting for height, athletic ability, intelligence — is contested. The technical capability is not yet there, but the question is coming.

**Oversight**. Gene therapy trials in the US are overseen by an institutional review board (IRB) plus, until recently, a dedicated NIH committee (the RAC). The infrastructure of oversight has changed over the years; the current model relies heavily on FDA review.

I will not pretend to settle any of these questions in a paragraph. The technical chapter ends here; the ethical questions continue outside the textbook and into society.

## What the chapter is really about

The technologies of molecular biology — restriction enzymes, ligases, PCR, sequencing, microarrays, CRISPR — were nearly all discovered by studying microbes for their own sake. Restriction enzymes came from work on bacterial defenses against phages. Thermostable polymerase came from a hot-spring extremophile that nobody could see a use for in 1969. Reverse transcriptase came from studies of viral biology that violated the central dogma. CRISPR came from sequencing odd repeats in bacterial genomes that nobody could explain.

Every step in this chain is "basic research on something with no apparent practical value" turning out to be the foundation of a multi-billion-dollar industry. The lesson is not that all basic research pays off — most doesn't — but that the technology of the next decade is almost certainly being built today in some lab studying an obscure organism for reasons that no funding agency would call "translational."

For microbiology specifically, the lesson is that we have an enormous amount of tool-grade biology still uncharacterized in the unculturable majority of microbes. Most environmental microbes have not been studied at all. Their enzymes may include the next CRISPR, the next Taq polymerase, the next reverse transcriptase. The frontier is still wide open.

## Still puzzling

I do not fully understand why CRISPR-Cas9 editing is as specific as it is in some cell types and as off-target as it is in others. The same guide RNA, in different cellular contexts, produces different ratios of on-target to off-target edits. Some of the variability is presumably chromatin state — CRISPR may have easier access to euchromatic regions than heterochromatic ones — but the full picture is not worked out. This matters clinically: a gene therapy that is highly specific in liver cells may be unacceptably off-target in another tissue. The mechanistic basis is still being worked out and is one of the active areas of CRISPR biology.

## What would change my mind

Casgevy (the 2023-approved CRISPR therapy for sickle cell) was a breakthrough in approving CRISPR for clinical use. The long-term safety profile is still being established — what happens to patients ten or twenty years after CRISPR editing of their hematopoietic stem cells is not yet known. If unexpected long-term effects (cancer from insertional mutagenesis at unintended sites, immune complications) emerge, the field's enthusiasm will moderate, and approval criteria will become more stringent. `[verify: long-term Casgevy safety data as of 2026]`

## LLM exercises

1. **Cloning step by step.** Ask the LLM to walk you through making a recombinant *E. coli* strain that expresses human insulin. List each step, each reagent, and each potential failure mode. Compare to the actual procedure used by Genentech in 1978.
2. **Reading a Western blot.** Describe a Western blot result with three lanes: a positive control, a negative control, and a patient sample. The patient sample shows a band at the expected molecular weight but also a band at twice that weight. Ask the LLM to propose three explanations and rank them by likelihood.
3. **The Taq polymerase principle.** Ask the LLM why a thermostable polymerase was the critical missing piece for practical PCR before Taq was discovered. Then ask what other extremophile enzymes might enable new techniques. The point is generative — what microbial proteins do we not yet have tool versions of?
4. **CRISPR therapy design.** Tell the LLM you want to design a CRISPR therapy for cystic fibrosis (caused by mutations in CFTR). Ask it to identify the technical challenges, including delivery, specificity, target cell selection, and ethical considerations. Critique each part.
5. **The case against germline editing.** Ask the LLM to write the strongest case against germline editing of human embryos, and then to write the strongest case in favor. Both arguments should be defensible. Evaluate the cogency of each.

## References

[^1]: Mullis, K.B. "The unusual origin of the polymerase chain reaction." *Scientific American* 262, no. 4 (1990): 56–65. Nobel Lecture: Mullis, K.B. "The Polymerase Chain Reaction." Nobel Lecture, 8 December 1993.
[^2]: Southern, E.M. "Detection of specific sequences among DNA fragments separated by gel electrophoresis." *Journal of Molecular Biology* 98, no. 3 (1975): 503–517. doi:10.1016/S0022-2836(75)80083-0.
[^3]: Fleischmann, R.D. et al. "Whole-genome random sequencing and assembly of *Haemophilus influenzae* Rd." *Science* 269, no. 5223 (1995): 496–512. doi:10.1126/science.7542800.
[^4]: Royal Swedish Academy of Sciences. "The Nobel Prize in Chemistry 2020: Genome editing." Press release, 7 October 2020. https://www.nobelprize.org/prizes/chemistry/2020/press-release/
---

## LLM Exercise — Chapter 12: Modern Applications of Microbial Genetics (Microbe Profile Database Project)

**Project:** Microbe Profile Database.
**What you're building this chapter:** molecular-diagnostic-tool fields across entries.
**Tool:** **Cowork**.

---

**The Prompt:**

```
Chapter 12 of my Microbe Database project. Chapter 12 covered
modern molecular tools — PCR (specific gene amplification);
whole-genome sequencing (WGS); CRISPR-Cas systems (originally a
bacterial defense, now a tool); restriction enzymes; recombinant
DNA technology; nucleic-acid amplification tests (NAATs)
clinically.

Schema additions:
- **Molecular_diagnostics**: list of clinical molecular tests
  available — NAAT, PCR, WGS, sequencing assay name (e.g.,
  Mycobacterium tuberculosis Xpert MTB/RIF, COVID PCR, HIV viral
  load).
- **Reference_genome_available**: yes/no + accession if known.

Backfill these for existing entries. Most well-known pathogens
have molecular diagnostics — note them. Specifically:
- *M. tuberculosis*: Xpert MTB/RIF (Cepheid GeneXpert) — rapid
  diagnosis + rifampin resistance detection. Game-changing for
  TB programs globally.
- HIV-1: viral load testing (PCR-based), genotypic resistance
  testing (sequencing reverse transcriptase + protease).
- SARS-CoV-2: PCR is the gold standard; antigen tests for rapid
  but less sensitive.
- *C. difficile*: PCR for toxin gene (tcdB) much faster than
  culture.
- *N. gonorrhoeae* (add if missing): NAATs replaced cultures —
  faster + better sensitivity.

End with: query — "which entries have NAAT or PCR diagnostics
available?" The answer should be most clinically-relevant
pathogens. What does the gap (organisms without modern molecular
diagnostics) tell you about diagnostic limitations?
```

---

**What this produces:** Molecular-diagnostic fields populated. Database now ~26-31 entries with rich molecular-tools annotations.

**Connection to previous chapters:** Ch 10 genome (sequencing requires knowing the genome) + Ch 11 HGT (resistance genes identifiable by PCR) + Ch 12 (the clinical tools) form the molecular-microbiology spine.

**Preview of next chapter:** Chapter 13 covers control of microbial growth — sterilization, disinfection, sensitivity to physical/chemical agents. Adds sterilization-resistance fields.


---

## AI Wayback Machine

**Jennifer Doudna** was co-developed CRISPR-Cas9 gene editing — the modern application of a microbial defense system. Nobel 2020.

**Run this:**

```
Who is Jennifer Doudna, and how does their work connect to modern microbial genetics we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about their career or ideas.
```

→ Search **"Jennifer Doudna"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to apply Jennifer Doudna's ideas to a contemporary microbiology problem.
- Add a constraint: "Answer including criticisms or limits of Jennifer Doudna's framework."

What changes? What gets better? What gets worse?
