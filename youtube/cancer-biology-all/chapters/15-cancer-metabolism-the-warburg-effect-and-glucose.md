# Chapter 15 — Cancer Metabolism: The Warburg Effect and Glucose


## TL;DR

- A growing tumor eats sugar like nothing else in your body.
- The chapter moves through Glycolysis, briefly, The Warburg effect explained, Worked example: HIF-1α and the hypoxic transcription program, Mitochondria in cancer, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

A growing tumor eats sugar like nothing else in your body.

Hold that observation for a moment. If you scan a cancer patient with positron emission tomography (PET) using fluorodeoxyglucose (FDG) — a radioactive glucose analog — the tumors light up. They consume glucose at rates that would be unsustainable for any normal tissue. Lymphomas, lung cancers, colorectal cancers, head and neck cancers — the PET image is essentially a glucose-uptake map of the body's most metabolically active cells. Most of those active cells turn out to be cancer.

What is striking is *how* cancer cells use that glucose. Normal cells, when oxygen is available, oxidize glucose completely through the citric acid cycle and oxidative phosphorylation, generating about 30-32 molecules of ATP per glucose. Cancer cells, even when oxygen is plentiful, divert most of their glucose to *lactate fermentation* — producing only 2 ATP per glucose and excreting lactate as waste. The behavior makes no obvious energetic sense. You would not, intuitively, choose to extract fifteen-fold less energy from your food source if you didn't have to.

Otto Warburg observed this phenomenon in 1924, working at the Kaiser Wilhelm Institute in Berlin. He coined the term *aerobic glycolysis* — glycolysis in the presence of oxygen. He proposed, incorrectly, that cancer was caused by *mitochondrial dysfunction*. He thought tumor mitochondria were broken, and the cell was forced to ferment because it couldn't respire. His framing dominated cancer metabolism for decades. He won the Nobel Prize in 1931 for his earlier work on cellular respiration.

It turns out the mitochondria are not broken. Cancer cells *choose* aerobic glycolysis even though they have functional respiratory machinery available. This is the deep puzzle. Why would a cell give up most of its potential ATP from glucose?

The answer, worked out in the 2000s and 2010s, is that *cancer cells are not optimizing for ATP*. They are optimizing for *biomass* — for the carbon skeletons, nitrogen, and reducing equivalents needed to build new cells. A proliferating cell has to make new DNA, new proteins, new lipids, new everything, and the substrates for that biosynthesis come from intermediates of glycolysis and the citric acid cycle. By burning glucose only partway (to lactate), the cell preserves intermediates for biosynthesis. The decision is not about energy efficiency. It is about resource allocation for growth.

This is the first of two chapters on cancer metabolism. This one — 11A — covers the Warburg effect in detail, the glucose metabolism that underlies it, and the role of mitochondria (which turn out to be repurposed rather than broken). The next — 11B — covers the broader metabolic landscape of cancer: lipid biosynthesis, amino acid addictions, the tumor microenvironment's metabolic competition, and the therapeutic targeting that is increasingly emerging from understanding this biology.

---

## Glycolysis, briefly

Glycolysis is the universal pathway that breaks down glucose. It runs in the cytoplasm of essentially every cell on Earth and is one of the oldest metabolic pathways in evolution. In ten enzymatic steps, glycolysis converts one glucose molecule (six carbons) into two pyruvate molecules (three carbons each), generating two ATP and two NADH along the way.

The first few steps trap and prepare glucose: hexokinase phosphorylates glucose to glucose-6-phosphate (committing the molecule to glycolysis); glucose-6-phosphate isomerase converts it to fructose-6-phosphate; phosphofructokinase-1 (PFK-1) phosphorylates it to fructose-1,6-bisphosphate (the irreversible commitment step). The molecule is then split into two three-carbon sugars (glyceraldehyde-3-phosphate and dihydroxyacetone phosphate). Each of these is processed through the remaining steps to yield pyruvate, ATP, and NADH.

PFK-1 is the major regulatory enzyme of glycolysis. It is allosterically activated by AMP and ADP (signaling low energy) and inhibited by ATP and citrate (signaling high energy or abundant biosynthetic precursors). PFK-1 activity determines how much glucose flows through glycolysis at any given time. Cancer cells, with their high glycolytic flux, upregulate PFK-1 and related enzymes.

Hexokinase is the entry-point regulator. Cancer cells frequently overexpress hexokinase 2 (HK2), the isoform that binds to the outer mitochondrial membrane and accesses the local ATP supply efficiently. HK2 binding to mitochondria also has secondary effects — it blocks the binding of BAX to mitochondrial pores, contributing to apoptosis evasion. HK2 is a tumor-promoting protein on multiple fronts.

What happens after glycolysis depends on cellular conditions. In normal cells under aerobic conditions, pyruvate enters mitochondria, is converted to acetyl-CoA by the pyruvate dehydrogenase complex (PDH), and enters the citric acid cycle. The acetyl groups are oxidized to CO2; NADH and FADH2 are generated; these reduced cofactors donate electrons to the electron transport chain, which pumps protons across the mitochondrial inner membrane; ATP synthase uses the proton gradient to phosphorylate ADP to ATP. The full pipeline (glycolysis + PDH + citric acid cycle + oxidative phosphorylation) yields about 30-32 ATP per glucose.

In hypoxic cells, oxygen is not available as the final electron acceptor for the electron transport chain. The cell cannot complete oxidative phosphorylation. Pyruvate is instead reduced to lactate by lactate dehydrogenase (LDH-A), regenerating NAD+ so that glycolysis can continue. The cell makes only 2 ATP per glucose but keeps glycolytic flux running.

Cancer cells perform lactate fermentation even when oxygen is available. They have made a metabolic choice that hypoxia would force on a normal cell, and they have made it under aerobic conditions. The choice has a name: aerobic glycolysis, or the Warburg effect.

---

## The Warburg effect explained

Why would a cell pick lactate fermentation over oxidative phosphorylation when oxygen is available?

The answer, in modern formulation, is that proliferating cells need *building blocks*, not just ATP. Consider what a cell needs to make to divide into two:

- DNA replication requires nucleotides (purines and pyrimidines), built from ribose-5-phosphate (from the pentose phosphate pathway, branching off glycolysis at glucose-6-phosphate), nitrogen (from glutamine and aspartate), and carbon skeletons.
- Membrane synthesis requires lipids — fatty acids built from acetyl-CoA (from glycolysis-derived pyruvate or from citrate exported from the mitochondria), glycerol-3-phosphate (from glycolysis intermediates), and various polar headgroups.
- Protein synthesis requires amino acids — some from extracellular uptake, many synthesized de novo from glycolysis and citric acid cycle intermediates (alanine from pyruvate, glutamate from α-ketoglutarate, aspartate from oxaloacetate, serine from 3-phosphoglycerate).
- Energy for biosynthetic reactions, in the form of NADPH (a reducing cofactor), comes from the pentose phosphate pathway and from cytosolic isocitrate dehydrogenase reactions.

If a cell oxidizes glucose completely to CO2 through oxidative phosphorylation, it gets maximum ATP but no carbon skeletons. The carbons are all exhaled as CO2. For a quiescent cell, this is fine — the cell does not need new carbon, only ATP for maintenance.

For a proliferating cell, complete oxidation is wasteful. The cell needs the carbons. By stopping glycolysis at pyruvate (or even before, branching off at glucose-6-phosphate for the pentose phosphate pathway, or at 3-phosphoglycerate for serine synthesis), the cell preserves carbon skeletons for biosynthesis. Lactate excretion gets rid of the excess reduced carbon (and excess protons) without consuming the citric acid cycle intermediates that would otherwise be needed for amino acid and nucleotide synthesis.

Aerobic glycolysis is, in this framing, *biosynthetic glycolysis*. The cell is treating glucose as a carbon source for building blocks, not as an energy source. The high glucose uptake is required to supply enough flux. The lactate excretion is the waste product of the carbon-allocation strategy.

This reframing — sometimes called the "Vander Heiden-Cantley-Thompson model" after the 2009 paper that crystallized it (Vander Heiden, Cantley, Thompson, *Science* 2009) — has changed how cancer metabolism is taught. The classical Warburg story (mitochondria are broken) is wrong. The reformulated story (mitochondria are intact, the cell is making a carbon-allocation choice) is the current understanding.

What about ATP? Proliferating cells don't need less ATP, they need more (to support biosynthesis). They get it through two main routes. First, they upregulate glycolysis enough that even with low ATP yield per glucose, total ATP from glycolysis is substantial. Second, they use mitochondrial oxidation of *other* substrates — glutamine, fatty acids — for additional ATP. The mitochondria are running, just not on glucose. Their primary roles in cancer cells are biosynthetic precursor generation and oxidation of alternative substrates rather than complete glucose oxidation.

---

## Worked example: HIF-1α and the hypoxic transcription program

The molecular regulator that connects oxygen sensing to glycolytic gene expression is *hypoxia-inducible factor 1α (HIF-1α)*. Understanding HIF-1α is understanding one of the deep links between tumor biology and metabolism.

HIF-1α is a transcription factor. Under normal oxygen levels, HIF-1α protein is constantly produced and constantly degraded. The degradation depends on *prolyl hydroxylases* (PHDs) — enzymes that hydroxylate specific proline residues on HIF-1α. The hydroxylated HIF-1α is recognized by the von Hippel-Lindau (VHL) protein, which is part of an E3 ubiquitin ligase complex. The ligase tags HIF-1α for proteasomal degradation. HIF-1α has a half-life of about 5 minutes under normoxic conditions.

The prolyl hydroxylases require oxygen as a cosubstrate. When cellular oxygen drops below about 5 percent, PHD activity falls. HIF-1α is no longer hydroxylated. VHL no longer binds. HIF-1α accumulates. It dimerizes with HIF-1β (a constitutively present partner) and translocates to the nucleus. The HIF-1α/HIF-1β heterodimer binds hypoxia response elements (HREs) at target gene promoters and activates transcription.

The HIF-1α target gene set is extensive. It includes:

- *Glycolytic enzymes* — hexokinase 2, PFK-1, aldolase A, GAPDH, PGK1, enolase 1, pyruvate kinase M2, lactate dehydrogenase A. HIF-1α coordinately upregulates the entire glycolytic pathway.
- *Glucose transporters* — GLUT1 (SLC2A1), GLUT3 (SLC2A3). The cell can absorb more glucose.
- *Lactate transporters* — MCT4 (SLC16A3). The cell can excrete more lactate.
- *Angiogenic factors* — VEGF, FGF, PDGF-β. The tumor recruits new blood vessels (Chapter 12).
- *Erythropoietin* — in cells that can produce it, EPO drives red blood cell production (the original function of the hypoxia response system).
- *Pyruvate dehydrogenase kinase 1 (PDK1)* — phosphorylates and inhibits PDH, blocking pyruvate entry to the citric acid cycle and reinforcing the glycolysis-to-lactate flux.

HIF-1α is normally a *transient* response to acute hypoxia. In cancer, it is often *constitutively* activated. Several mechanisms produce constitutive HIF activity:

- *Tumor hypoxia*. Solid tumors typically outgrow their blood supply, creating regions of low oxygen. HIF-1α stabilizes in these regions.
- *VHL loss*. The VHL tumor suppressor is mutated or deleted in most clear cell renal cell carcinomas (it is the gene at the locus of von Hippel-Lindau syndrome). Without VHL, HIF-1α is not degraded even under normoxic conditions. The cell behaves as if chronically hypoxic.
- *Oncogenic signaling*. Ras, AKT, and other oncogenic pathways increase HIF-1α translation. Mitochondrial reactive oxygen species (ROS) from various sources can inhibit the prolyl hydroxylases. Several oncometabolites (2-hydroxyglutarate from IDH mutations, succinate from SDH mutations, fumarate from FH mutations) inhibit PHDs by competitive substrate similarity, producing pseudohypoxia.

HIF-2α is a paralog of HIF-1α with similar but not identical functions. HIF-2α is particularly important in clear cell renal cell carcinoma, where it drives much of the disease's biology in the setting of VHL loss. Belzutifan, an HIF-2α inhibitor, was approved by the FDA in 2021 for VHL-disease-associated cancers and subsequently for advanced clear cell renal cell carcinoma. It is the first drug targeting the HIF system clinically — a beautiful example of how a long-understood transcription factor became druggable.

---

## Mitochondria in cancer

The Warburg-era idea that cancer mitochondria are broken has been largely abandoned. Modern cancer biology recognizes that mitochondria in tumor cells are usually functional and are repurposed rather than disabled. They serve several functions critical for cancer cell survival and growth.

*Anabolic precursor generation*. The citric acid cycle produces intermediates that are exported from mitochondria for biosynthesis. Citrate is exported to the cytoplasm for fatty acid synthesis (cleaved to acetyl-CoA by ATP-citrate lyase). α-ketoglutarate and oxaloacetate support amino acid synthesis. The cycle in proliferating cells often runs "anaplerotic" — pulling in glutamine or other substrates to replace the carbons exported for biosynthesis.

*Oxidation of alternative substrates*. Cancer cells oxidize glutamine, fatty acids, and amino acids in mitochondria as alternative fuel sources. Glutamine in particular is a major substrate — many cancer cells are "glutamine-addicted" and require continuous glutamine import for survival and growth. The oxidation generates ATP, NADH, and FADH2, supporting mitochondrial energy production even when glucose is being diverted to lactate.

*ROS production*. Mitochondria are the major source of reactive oxygen species in cells. ROS signaling supports proliferation and certain oncogenic pathways, while excess ROS can be lethal. Cancer cells balance ROS production with antioxidant defenses (NRF2-driven gene expression, glutathione synthesis, NADPH for antioxidant regeneration) to maintain a productive level.

*Apoptosis gatekeeping*. Mitochondria are the central hub of intrinsic apoptosis (Chapter 10A). Cancer cells need their mitochondria functional enough to produce ATP and intermediates but suppressed in their apoptotic capacity (typically through elevated anti-apoptotic BCL-2 family proteins).

*Mitochondrial DNA mutations*. Mitochondrial DNA (mtDNA) is more vulnerable to damage than nuclear DNA — it lacks histones, has limited repair machinery, and is in proximity to ROS-generating electron transport chain. Cancer cells often carry mtDNA mutations, though the consequences for cancer biology are still being characterized.

*Mitochondrial dynamics — fission and fusion*. Mitochondria are dynamic; they fuse and divide constantly. The balance between fission and fusion affects bioenergetics, apoptosis sensitivity, and the spatial distribution of mitochondria within the cell. Cancer cells often have altered mitochondrial dynamics.

Several mitochondrial-targeted therapies are in development. Inhibitors of the electron transport chain (complex I inhibitors, complex III inhibitors) selectively kill cancer cells with high oxidative phosphorylation dependence. Metformin, a common diabetes drug that mildly inhibits complex I, has been associated with reduced cancer incidence and mortality in epidemiological studies, and clinical trials are exploring its use in cancer prevention and adjuvant therapy. The data on metformin are mixed but suggestive.

---

## Pentose phosphate pathway and biosynthesis

The pentose phosphate pathway (PPP) branches off from glycolysis at glucose-6-phosphate. It has two main functions: producing ribose-5-phosphate for nucleotide synthesis and producing NADPH for biosynthesis and antioxidant defense.

The *oxidative branch* of the PPP runs glucose-6-phosphate through glucose-6-phosphate dehydrogenase (G6PD) and 6-phosphogluconate dehydrogenase, generating two NADPH per glucose and ribulose-5-phosphate (which converts to ribose-5-phosphate). The *non-oxidative branch* interconverts five-carbon sugars and produces fructose-6-phosphate and glyceraldehyde-3-phosphate, which feed back into glycolysis.

Cancer cells often upregulate PPP flux. Higher G6PD activity supports nucleotide synthesis and NADPH production. The NADPH is essential for fatty acid synthesis, cholesterol synthesis, and (perhaps most importantly) regeneration of reduced glutathione, the major intracellular antioxidant. Cancer cells with high biosynthetic demand and high ROS production are heavily dependent on PPP flux for survival.

This dependence creates therapeutic vulnerabilities. G6PD inhibitors are in early preclinical development. More broadly, drugs that disrupt the cell's antioxidant capacity (BSO depletes glutathione; certain natural products inhibit thioredoxin reductase) can selectively kill cancer cells with high oxidative stress baseline.

---

## Serine and one-carbon metabolism

A growing area of cancer metabolism is *serine and glycine biosynthesis*, which feeds into *one-carbon metabolism* — the pool of single-carbon units used for nucleotide synthesis, methylation reactions, and other biosynthetic processes.

Glycolysis produces 3-phosphoglycerate (3PG), which can be diverted into serine synthesis via three enzymatic steps: PHGDH (phosphoglycerate dehydrogenase), PSAT1 (phosphoserine aminotransferase 1), and PSPH (phosphoserine phosphatase). The serine then enters one-carbon metabolism via serine hydroxymethyltransferase (SHMT), which converts serine to glycine and produces a methylene group attached to tetrahydrofolate.

The one-carbon units are used for purine synthesis, thymidine synthesis, SAM synthesis (the universal methyl donor), and homocysteine remethylation. The pathway is essential for proliferating cells.

PHGDH is amplified in a substantial fraction of breast cancers and melanomas. Cells with PHGDH amplification are addicted to serine synthesis flux. PHGDH inhibitors are in clinical development, and the strategy of *serine starvation* through dietary restriction has produced effects in some preclinical models.

One-carbon metabolism is also the target of *antifolate* drugs, which have been in cancer therapy since the 1940s. Methotrexate (introduced 1948), pemetrexed (approved 2004), and related drugs inhibit enzymes in the folate-dependent one-carbon pathway, blocking nucleotide synthesis and producing apoptosis in rapidly dividing cells. The drugs are still backbone agents in many regimens.

---

## What this chapter gives you

Cancer cells reprogram their metabolism to support biomass accumulation rather than maximum ATP production. The hallmark is *aerobic glycolysis* (the Warburg effect): glucose is taken up at high rates and converted to lactate even when oxygen is available, preserving glycolytic intermediates for biosynthesis. The behavior was originally interpreted as mitochondrial dysfunction; the modern understanding is that cancer cells choose biomass over ATP efficiency.

Mitochondria are not broken in cancer cells. They are repurposed for anaplerotic precursor generation, oxidation of alternative substrates (glutamine, fatty acids), ROS production, and apoptosis gatekeeping. The cell makes a strategic resource-allocation decision; oxygen and reduced carbon flow are managed to maximize growth.

HIF-1α is the molecular regulator that connects oxygen sensing to glycolytic gene expression. It is constitutively activated in cancer through tumor hypoxia, VHL loss (especially in renal cell carcinoma), and oncogene-driven mechanisms. HIF-2α-selective inhibitor belzutifan was approved in 2021 for VHL-disease cancers and clear cell renal cell carcinoma, validating HIF as a therapeutic target.

The pentose phosphate pathway, serine and glycine biosynthesis, and one-carbon metabolism are additional metabolic frontiers that are increasingly being targeted therapeutically. The antifolates have been in clinical use for decades; PHGDH inhibitors and other newer agents represent the next wave.

Chapter 11B continues with the broader metabolic landscape — fatty acid biosynthesis, glutamine addiction, amino acid dependencies, the metabolic competition between tumor and immune cells in the tumor microenvironment, and the therapeutic implications of targeting cancer's metabolic vulnerabilities.

---

## LLM exercises

1. Ask your LLM to explain the Vander Heiden-Cantley-Thompson reformulation of the Warburg effect (2009 paper). What is the key conceptual move from "mitochondrial dysfunction" to "biomass optimization"? Cross-check with the original paper and identify what evidence shifted the field's interpretation.

2. Have your LLM walk through the HIF-1α regulatory pathway: oxygen sensing, prolyl hydroxylase activity, VHL-mediated degradation, and the consequences of stabilization. Then trace through the gene expression changes that follow HIF stabilization. What does this tell us about why VHL-mutant kidney cancers behave the way they do?

3. Use your LLM to compare the metabolic profiles of three different cancer types (e.g., glioblastoma, pancreatic adenocarcinoma, and chronic lymphocytic leukemia). What are the dominant fuel substrates, the active biosynthetic pathways, and the metabolic vulnerabilities for each?

4. Ask your LLM to explain how FDG-PET imaging works and what it detects. Then probe: what cancers light up well on FDG-PET, what cancers don't, and what does PET avidity correlate with in terms of treatment response and prognosis?

5. Have your LLM analyze the epidemiological data on metformin and cancer incidence. What is the evidence for a protective effect, what is the proposed mechanism (complex I inhibition? AMPK activation? something else?), and how should we interpret the clinical trial results so far? Identify the strongest support and the strongest counterargument.

---

##  AI Wayback Machine
The ideas in this chapter didn't appear from nowhere. **Otto Warburg** observed in the 1920s that cancer cells consume glucose voraciously and produce lactate even with abundant oxygen — the Warburg effect. He won the 1931 Nobel Prize. His broader claim that cancer is a metabolic disease was largely abandoned, then partially revived in the 2000s.

![Otto Heinrich Warburg](../images/otto-heinrich-warburg-2i4.png)

*Puppet Art by [Nik Bear Brown](https://www.nikbearbrown.com/).*

**Run this:**

```
Who was Otto Warburg, and how does the Warburg effect connect to the cancer metabolism we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.
```

→ Search **"Otto Heinrich Warburg"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to explain why a cancer cell would choose inefficient aerobic glycolysis over efficient oxidative phosphorylation.
- Ask it to confront Warburg's politically compromised survival in Nazi Germany — and what that says about scientific legacy.

What changes? What gets better? What gets worse?
