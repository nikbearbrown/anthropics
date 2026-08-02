# Chapter 19 — Gene Expression: Why Identical DNA Makes Different Cells
*The same instruction manual, read a thousand different ways.*

---

Here is something that should bother you.

Every cell in your body — liver cell, neuron, muscle fiber, photoreceptor — contains exactly the same DNA. Same 3 billion base pairs. Same 20,000 genes. If you extracted the genome from your liver and compared it to the genome from your eye, you would find them identical.

And yet a liver cell makes enzymes that detoxify ammonia. An eye cell makes crystallins, proteins so transparent they refract light. A muscle cell makes myosin, a molecular motor that contracts. These cells look different, behave differently, and respond to the world differently. They are, functionally, completely different organisms sharing the same body.

How?

The answer is not that different cells have different genes. They do not. The answer is that the same genes are read differently in different cells — some sections open and available, others locked away; some transcribed constantly, others never touched; some mRNAs translated at high rate, others blocked or destroyed before a single ribosome reaches them. Gene expression is the control layer between DNA and protein, and it operates at five distinct levels. Each one is a checkpoint. Each one can fail. Understanding them is how we understand development, how we understand cancer, and how we understand why you are different from your identical twin despite sharing every base pair of DNA.

Let me build the picture from the simplest case outward.

---

## The Simple Case: How Bacteria Do It

Bacteria face a different version of the problem. An *E. coli* cell does not need to specify cell types — it is one cell and will always be one cell. What it needs is speed. When the environment changes, when a new food source appears or a previous one vanishes, the cell must retool its protein production in minutes. There is no time for a five-layer regulatory hierarchy.

Bacteria regulate almost entirely at transcription. And because there is no nuclear envelope separating transcription from translation, ribosomes can begin reading an mRNA while it is still being synthesized. The delay between gene activation and working protein is measured in seconds.

The lac operon is the classic example, and it is worth understanding in detail because it contains, in miniature, all the logic of eukaryotic regulation without the complexity.

*E. coli* can digest lactose, but only if it makes the right enzymes: beta-galactosidase (which cleaves lactose into glucose and galactose), permease (which brings lactose into the cell), and transacetylase (whose role in lactose metabolism is secondary). These three genes sit adjacent on the chromosome, transcribed as a single message. A single regulatory decision turns on all three.

But the cell does not simply ask "is lactose here?" It asks two questions simultaneously: Is lactose present? And is glucose absent?

The reason for the second question is straightforward. Glucose is the preferred fuel. If glucose is available, there is no point in spinning up the machinery to process lactose. Only when glucose is gone and lactose is present should the lactose-processing genes activate.

Here is the mechanism. When glucose is scarce, an enzyme called adenylyl cyclase produces cAMP — cyclic AMP, a small signaling molecule. cAMP binds to a protein called CAP, the catabolite activator protein. The CAP-cAMP complex then binds to the DNA just upstream of the lac genes, helping RNA polymerase bind the promoter and begin transcription. That is the positive signal: glucose is gone, good conditions exist to use an alternative fuel.

But there is also a negative signal. Floating in the cytoplasm is the lac repressor, a protein that can bind to a short DNA sequence called the operator, positioned between the promoter and the genes. When the repressor sits on the operator, it physically blocks RNA polymerase from proceeding. The genes are silenced.

What releases the repressor? Allolactose — a metabolite that forms when small amounts of lactose enter the cell. When allolactose binds to the repressor, the repressor changes shape and lets go of the operator. The block is removed.

So the logic runs: if CAP-cAMP is bound (glucose is low) AND the repressor is off the operator (lactose is present), then RNA polymerase proceeds and the three enzymes are made. If either condition fails — if glucose returns or if lactose disappears — the system shuts off. The cell makes these enzymes only when it needs them and not when it does not. Energy is saved.

<!-- → [INFOGRAPHIC: Lac operon state diagram showing all four combinations of glucose/lactose availability — (1) glucose present, lactose absent: repressor on operator, no CAP-cAMP, operon OFF; (2) glucose present, lactose present: repressor off operator but no CAP-cAMP, operon LOW; (3) glucose absent, lactose absent: CAP-cAMP present but repressor on operator, operon OFF; (4) glucose absent, lactose present: CAP-cAMP bound AND repressor off, operon ON HIGH — student should see the AND-gate logic visually before reading the trp operon comparison] -->

The trp operon runs the same logic inverted. Tryptophan is an amino acid the cell can synthesize, but synthesis is expensive. If tryptophan is already available in the environment, why make it? The trp operon is on by default. When tryptophan accumulates, it binds to the trp repressor, activating it — a repressor that, in its unbound form, cannot grip the operator. The tryptophan-bound repressor locks onto the operator and silences the synthesis genes. When tryptophan runs low, the repressor releases, transcription resumes, synthesis restarts.

One operon is inducible: silent by default, turned on by a signal. The other is repressible: active by default, turned off by a signal. The mechanisms are mirror images, but both are solving the same kind of problem — regulate at the cheapest possible point, which is before the RNA is even made.

---

## The Eukaryotic Problem: Five Layers of Control

Eukaryotes face a harder problem. You have 37 trillion cells, each expressing a different subset of your 20,000 genes, each maintaining a distinct identity across decades of cell divisions. You cannot solve this with a single repressor and a single activator. You need a layered architecture — multiple checkpoints, each operating on a different timescale, each sensitive to a different set of signals.

Evolution built five.

<!-- → [INFOGRAPHIC: Five-layer overview diagram — vertical stack showing DNA at the bottom, then: (1) epigenetic/chromatin layer, (2) transcription layer, (3) post-transcriptional/splicing and mRNA stability layer, (4) translation layer, (5) post-translational/protein modification layer — each layer labeled with its timescale (persistent/cell divisions; minutes-hours; near-instantaneous; seconds; milliseconds) and its function in a single phrase; designed as an orientation map the reader can return to while reading the sections below] -->

**The first is epigenetic: controlling access to DNA itself.**

Your DNA is not sitting naked in the nucleus. It is wound around protein spools called histones, coiled into nucleosomes, and then further compacted. If you stretched out all the DNA in a single human cell, it would reach about two meters. The nucleus is a few micrometers across. The compaction ratio is staggering, and the compaction is not uniform. Some regions of the chromosome are tightly packed — heterochromatin — and the genes there are essentially inaccessible. Other regions are open — euchromatin — where the transcription machinery can reach.

What determines which regions are open? Chemical modifications on the histone proteins themselves. When acetyl groups are added to histones, the DNA wraps less tightly and genes in that region become transcribable. When acetyl groups are removed, chromatin closes and genes go silent. Methyl groups added directly to cytosine bases in the DNA — particularly in regions called CpG islands near gene promoters — also silence genes, often for the lifetime of the cell.

<!-- → [IMAGE: DNA compaction diagram showing three levels — (1) DNA double helix wrapping around a histone octamer to form a nucleosome ("beads on a string"); (2) nucleosomes coiling into a 30nm chromatin fiber; (3) the fiber looped into condensed heterochromatin — left panel shows euchromatin (open, accessible) vs. right panel showing heterochromatin (closed, inaccessible); annotate the acetylation and methylation marks that distinguish the two states] -->

These modifications do not change the DNA sequence. They change whether the DNA is readable. They are called epigenetic — "above the genome." And they are heritable: when a cell divides, the epigenetic pattern is copied along with the DNA sequence. A liver cell does not accidentally activate eye genes not because the eye genes are deleted, but because they are epigenetically sealed. The marks that seal them are passed to every daughter cell.

This is both powerful and dangerous. The permanence that makes cell identity stable is the same property that, when misapplied, locks tumor suppressor genes in silence for the lifetime of a cancer.

**The second layer is transcriptional: controlling when RNA polymerase binds.**

Once a chromosomal region is open, transcription factors determine which genes in that region are actually transcribed. Transcription factors are proteins that recognize specific DNA sequences — usually short motifs of six to twelve base pairs — in promoters and in distant regulatory elements called enhancers.

A gene's promoter is the sequence immediately upstream of where transcription begins. General transcription factors assemble there, recruiting RNA polymerase and positioning it to start. But these general factors produce only a baseline level of transcription. The interesting control comes from activators and repressors that bind to enhancers — sequences that can be thousands of base pairs away from the gene they regulate, anywhere in the genome, on either side of the gene, even within it. When an activator binds an enhancer, the DNA between the enhancer and the promoter physically loops, bringing the activator into contact with the general transcription machinery and dramatically increasing transcription. When a repressor binds, it blocks this contact or actively recruits machinery to close the chromatin.

<!-- → [IMAGE: Enhancer-promoter looping diagram — showing a gene with its promoter (TATA box region) and a distant enhancer several kilobases upstream; an activator protein bound to the enhancer; the intervening DNA shown looped so the activator makes direct contact with general transcription factors assembled at the promoter; RNA polymerase shown positioned to begin transcription; annotate "DNA loop" and "enhancer can be thousands of base pairs away"] -->

A human cell expresses hundreds of different transcription factors. What a cell "is" — liver, neuron, muscle — depends substantially on which transcription factors are active in it and what suite of target genes they regulate. During embryonic development, signals from neighboring cells activate specific transcription factors. Those factors activate more transcription factors. The cascade locks in over time, until the cell's identity is stable and self-reinforcing.

**The third layer is post-transcriptional: controlling the RNA after it is made.**

In eukaryotes, the raw RNA transcript is not the final message. Before it leaves the nucleus, it is processed. Introns — non-coding sequences interrupting the coding regions — are cut out by a massive molecular machine called the spliceosome. The coding sequences, exons, are joined together. The result is the mature mRNA.

But which exons get joined is not fixed. Alternative splicing allows different exons to be included or excluded, producing different protein variants from the same gene. The spliceosome can skip exon 3, or include it, or include only part of it. In humans, alternative splicing occurs in more than 70 percent of multi-exon genes. One gene can produce dozens of distinct proteins, each with different functions, expressed in different cell types or at different developmental stages.

<!-- → [IMAGE: Alternative splicing diagram — a pre-mRNA shown with five exons (E1–E5) and four introns; three different splicing outcomes shown below: (1) all exons included → protein variant A; (2) exon 3 skipped → protein variant B; (3) exons 3 and 4 skipped → protein variant C — annotate "one gene, multiple proteins" and indicate which splicing pattern might occur in which tissue] -->

After splicing, the mRNA's stability — how long it persists before being degraded — becomes another control point. Stable mRNAs are translated many times. Unstable ones are destroyed before many ribosomes reach them. RNA-binding proteins can protect an mRNA or target it for destruction. MicroRNAs — short RNA molecules of about 21 nucleotides — bind to complementary sequences in the mRNA's untranslated end and recruit a protein complex that either blocks translation or degrades the message. A single microRNA can regulate hundreds of different mRNAs. Changes in which microRNAs are expressed shift the protein output of a cell broadly and rapidly.

**The fourth layer is translational: controlling whether the ribosome starts.**

An mRNA that reaches the cytoplasm intact can still fail to be translated. The assembly of a ribosome on an mRNA requires a set of proteins called initiation factors. One of them, eIF-2, is the key. When eIF-2 is phosphorylated, it cannot participate in ribosome assembly. Translation halts.

This is used as an emergency brake. When a cell detects viral infection, amino acid starvation, or accumulating misfolded proteins, kinases phosphorylate eIF-2. Protein synthesis drops globally. The cell stops making most of its proteins, buying time to deal with the crisis. In Alzheimer's disease, eIF-2 is chronically phosphorylated in affected neurons, suppressing synthesis of proteins needed for memory and synaptic function. The protein shortage may be part of the pathology.

**The fifth layer is post-translational: controlling what proteins do and how long they last.**

Proteins, once made, are not final products. They are starting points. Chemical modifications — phosphorylation, acetylation, ubiquitination — change their activity, their location within the cell, and their lifetime.

Phosphorylation is the most common: a kinase adds a phosphate group to the protein, changing its shape and often its activity, turning it on or off. Phosphatases remove the phosphate and reverse the change. Most signaling in a cell runs through cascades of kinase-mediated phosphorylation.

Ubiquitination is the death mark. A small protein called ubiquitin is attached to a target protein, and then more ubiquitin is added, building a chain. The proteasome, a barrel-shaped protein complex, recognizes the ubiquitin chain, unfolds the tagged protein, and degrades it into peptides. A protein can go from fully functional to completely destroyed in minutes. Cell cycle control, immune responses, quality control for misfolded proteins — all depend on ubiquitin-mediated degradation.

<!-- → [IMAGE: Ubiquitin-proteasome pathway diagram — a target protein shown with a chain of ubiquitin molecules attached; the ubiquitinated protein being threaded into the barrel of the proteasome; small peptide fragments exiting the other end; annotate the ubiquitin chain as the "death mark" and note the timescale (minutes from tagged to destroyed)] -->

---

## The Integration Problem

Five layers. Each operating on a different timescale: epigenetic marks persist through cell divisions; transcriptional changes take minutes to hours; splicing changes are essentially instantaneous; translational control responds in seconds; post-translational modifications happen in milliseconds. Each responding to different signals. Each reversible, each with its own failure modes.

The question worth sitting with is not how any one layer works — each is mechanistically clear. The question is how they integrate.

A liver cell and a neuron share perhaps 12,000 genes expressed at similar levels. They differ in the expression of a few thousand more. The liver's identity is not encoded in the presence of unique genes. It is encoded in the combination of which genes are epigenetically open, which transcription factors are active, which splicing patterns are selected, which mRNAs are stabilized, which proteins are phosphorylated. The same genome, read through a different filter at every level simultaneously.

Disrupting any one level can cause disease. Consider cancer.

A single mutation in a transcription factor that normally activates cell growth genes — say, it makes the protein constitutively active, unable to turn off — causes one cell to divide too fast. In Burkitt's lymphoma, a chromosomal rearrangement places the myc gene, which encodes a growth-promoting transcription factor, next to a powerful promoter normally active in immune cells. myc is now permanently on. The cell divides without stopping.

Epigenetic failure is another route. The p53 gene encodes a transcription factor that detects DNA damage, halts the cell cycle, and if damage is irreparable, triggers cell death. In normal cells, p53 is tightly controlled — rapidly degraded when not needed, stabilized and activated when damage is detected. In more than half of all cancers, p53 is mutated. But in a significant fraction of those cases, the gene is not mutated; it is silenced. Hypermethylation of CpG islands in the p53 promoter locks the gene in heterochromatin. The protein is never made. Cells with damaged DNA divide as if nothing happened.

MicroRNA dysregulation can do the same through the post-transcriptional layer. If a microRNA that normally degrades oncogene mRNA is itself silenced — by methylation, by deletion, by any means — the oncogene protein accumulates. If a microRNA that normally suppresses tumor suppressors is overexpressed, the tumor suppressor protein disappears. The cell shifts toward uncontrolled growth through a mechanism entirely at the RNA level, with no mutation in any coding sequence.

<!-- → [INFOGRAPHIC: Cancer as multi-layer failure diagram — the five regulatory layers shown as a vertical stack (same orientation as the overview diagram); for each layer, one named cancer example shown as a red "failure point": epigenetic layer → p53 CpG hypermethylation; transcriptional layer → Burkitt's lymphoma myc rearrangement; post-transcriptional layer → microRNA dysregulation of tumor suppressor; translational layer → chronic eIF-2 phosphorylation in neurodegeneration; post-translational layer → hyperphosphorylated cyclins bypassing cell-cycle checkpoints — caption: "cancer is not one mechanism failing; it is the same five layers, failures distributed across all of them"] -->

This is what makes cancer feel philosophically disturbing once you understand it. It is not, primarily, a disease of broken genes. It is a disease of broken reading — of the same genome read in the wrong context, the wrong layers unlocked, the wrong checkpoints bypassed. The information is still there. The interpretation has gone wrong.

---

## What Regulation Is For

Return to the puzzle. Why does a liver cell not accidentally make crystallins?

Not because it lacks the crystallin genes. It has them. But the crystallin genes are in densely packed heterochromatin in liver cells, methylated, histones deacetylated, marked for long-term silence. The transcription factors that would activate them are not present in liver cells. Even if, by some accident, a crystallin mRNA were made, it would lack the stabilizing factors that keep it intact in lens cells, and it would be rapidly degraded. Even if it survived to be translated, the post-translational environment in a liver cell — the kinases, the protein complexes, the compartmentalization — would not support the function of the protein.

All five layers, simultaneously, prevent the mistake.

This is the design logic: redundancy in the service of cell identity. One failed checkpoint should not be enough to reprogram a cell. And in normal biology, it is not. Cancer requires multiple failures — two, three, four regulatory layers compromised — before a cell truly loses its identity and begins dividing without constraint.

What I find genuinely remarkable about this architecture is its evolution. None of these five layers are arbitrary. The epigenetic layer provides memory — cell identity that persists through division. The transcriptional layer provides specificity — responses to the precise combination of signals a cell receives. The post-transcriptional layer provides diversity — many proteins from few genes. The translational layer provides emergency response — global shutdown when needed. The post-translational layer provides speed — millisecond adjustments without waiting for new protein synthesis.

Each layer evolved to solve a different aspect of the same problem: how do you take one genome and use it to build and maintain trillions of cells, each with its own identity, each stable across years of division, each responsive to its environment?

The answer is a hierarchy of filters, each reading the same information and passing forward only what the next filter should see. The genome does not contain the organism. It contains the instructions for building one, given the right context. The context is gene regulation.

You are not your genome. You are your genome expressed.

---

## Exercises

**Warm-up**

1. In the lac operon, the cell needs both conditions to be true before the genes are expressed at high levels: glucose must be absent AND lactose must be present. Identify which molecule signals each condition and how it does so. What would happen to expression if glucose were absent but lactose were also absent? *Tests: understanding the two-signal AND-gate logic of the lac operon.*

2. Define epigenetic modification. Explain why it is called "above the genome" and why this name is accurate. Give one example of an epigenetic mark that opens chromatin and one that closes it. *Tests: basic epigenetics vocabulary and mechanism.*

3. A gene has five exons. Alternative splicing can produce three different mature mRNAs from this gene. Is this possible while keeping the 5' to 3' order of exons intact? What is the maximum number of distinct proteins this one gene could produce if any combination of the five exons can be included or excluded? *Tests: post-transcriptional control through alternative splicing.*

**Application**

4. A drug inhibits histone deacetylase (the enzyme that removes acetyl groups from histones). Predict what would happen to gene expression broadly in cells treated with this drug. Would you expect all genes to be affected equally? Why might this drug have potential in cancer therapy? *Tests: applying epigenetic mechanism to a pharmacological intervention.*

5. In Burkitt's lymphoma, the myc gene is translocated next to a powerful promoter that is constitutively active in immune cells. Using the transcriptional control layer, explain why this translocation causes the lymphoma cells to divide uncontrollably. What would need to happen for a targeted therapy to address this specific defect? *Tests: applying transcriptional regulation to a cancer mechanism.*

6. A cell under viral infection rapidly phosphorylates eIF-2. Describe the immediate consequence for protein synthesis across the cell. Why would globally halting most translation be a useful response to viral infection? What is the cost of this response? *Tests: translational control as emergency response, with cost-benefit reasoning.*

**Synthesis**

7. A researcher discovers a cancer cell line in which the p53 gene sequence is completely normal — no mutations — but p53 protein is undetectable. Propose three different mechanisms, each at a different regulatory layer, that could explain this observation without any mutation in the p53 coding sequence. *Tests: integrating all five layers to reason about a single observed phenotype.*

8. A liver cell and a neuron share approximately 12,000 genes expressed at similar levels but differ in thousands more. Design a hypothetical experiment to determine whether the key differences between these two cell types are primarily due to (a) epigenetic differences, (b) differences in transcription factor expression, or (c) differences in alternative splicing. What would you measure, and what result would support each hypothesis? *Tests: applying the five-layer framework to experimental design.*

**Challenge**

9. Some epigenetic marks are heritable — passed from parent cell to daughter cell during division. But when a sperm and egg fuse, most epigenetic marks are erased and reset. This "epigenetic reprogramming" allows the zygote to develop into any cell type. What would go wrong if epigenetic marks were NOT erased at fertilization? Conversely, what is the risk if reprogramming is incomplete? Connect your answer to both normal development and disease. *Tests: reasoning about the function and failure modes of epigenetic inheritance at the organism level.*

10. MicroRNAs are small RNAs (~21 nucleotides) that bind to complementary sequences in target mRNAs and either block their translation or cause their degradation. A single microRNA can regulate hundreds of different mRNAs. Given this, explain why dysregulation of a single microRNA could have cascading effects on a cell's behavior. Then explain why this same property makes microRNAs attractive candidates for cancer therapy — and what the challenge of specificity would be. *Tests: reasoning from mechanism to clinical consequence for post-transcriptional control.*

---

## LLM Exercises

The following exercises are designed for use with a large language model. Paste the prompt into any capable model and examine the response critically — not for correctness alone, but for whether the reasoning is mechanistic or merely verbal.

**Exercise 1 — The lac operon as a logic gate**
Prompt a model: *"The lac operon in E. coli encodes the genes for lactose metabolism. The operon is induced by lactose AND repressed by glucose — meaning the cell only expresses these genes when lactose is available and glucose is not. Walk me through the molecular logic: how does the cell sense both signals (allolactose and cAMP), and how do the lac repressor and CAP protein implement this AND-NOT logic at the operator and promoter? What would happen if a mutant lac repressor could not bind allolactose?"*

Evaluate whether the model correctly identifies the dual-control mechanism — lac repressor (allosterically inhibited by allolactose, releasing operator) AND CAP-cAMP complex (activated when glucose is low, binding promoter) — and whether it engages with the metabolic logic: glucose is preferred, so the cell only expresses lactose-metabolizing enzymes when lactose is the only sugar available.

**Exercise 2 — Eukaryotic gene regulation: distance and complexity**
Prompt: *"Eukaryotic enhancers can be located thousands of base pairs upstream, downstream, or even within introns of the genes they regulate. Walk me through how DNA looping brings distant enhancers into contact with promoters, and how transcription factors at enhancers communicate with the basal transcription machinery. Why does this architecture enable the dramatically more complex regulation of eukaryotic genes compared to bacteria?"*

Evaluate whether the model engages with the chromatin-loop architecture (mediated by proteins like cohesin and CTCF), the role of Mediator complex in coupling enhancers to RNA polymerase II, and the combinatorial logic enabled by multiple enhancers at different distances providing tissue-specific and temporal-specific control.

**Exercise 3 — Chromatin state as gene regulation**
Prompt: *"Eukaryotic DNA is wrapped around histones to form nucleosomes, which can adopt 'open' (euchromatin, transcriptionally active) or 'closed' (heterochromatin, transcriptionally silent) states. Walk me through how histone modifications — specifically histone acetylation (typically activating) and histone methylation (context-dependent) — alter chromatin state. What is the role of the histone code and how does it integrate with DNA methylation to provide a stable but reversible regulatory layer?"*

Evaluate whether the model correctly identifies that histone acetylation neutralizes the positive charge of histones, weakening their DNA binding and opening chromatin, while specific methylation marks (e.g., H3K4me3 = active, H3K27me3 = repressed) recruit different effector proteins. The integration with DNA methylation involves both inheritable patterns (cell-type identity) and reversible patterns (developmental decisions).

**Exercise 4 — Post-transcriptional regulation: microRNAs**
Prompt: *"MicroRNAs (miRNAs) are short non-coding RNAs (~22 nucleotides) that regulate gene expression by base-pairing with target mRNAs and either blocking translation or accelerating degradation. A single miRNA can regulate hundreds of target mRNAs, and most human protein-coding genes are estimated to be miRNA-regulated [verify]. Walk me through the biogenesis pathway (Drosha, Dicer, RISC complex) and explain why this regulatory layer is particularly important for fine-tuning gene expression rather than on/off switching."*

Evaluate whether the model correctly traces the biogenesis (primary miRNA → pre-miRNA → mature miRNA → loading into RISC), and engages with the mechanism's strengths (small RNA → broad regulatory reach) and limits (miRNAs typically reduce protein output by 30-70% rather than switching genes off completely — they fine-tune rather than gate).

**Exercise 5 — How cells differ when they have the same genome**
Prompt: *"Every somatic cell in a multicellular organism contains essentially the same genome, yet a neuron and a hepatocyte are dramatically different cells. Walk me through how differential gene expression — controlled by tissue-specific transcription factors, chromatin state, and post-transcriptional regulation — produces this diversity. Then explain how a fertilized egg differentiates into hundreds of cell types: what drives the initial commitment decisions, and why are cell fates generally stable once established (even though the underlying genome is identical)?"*

Evaluate whether the model engages with the master-regulator concept (specific transcription factors like MyoD for muscle, Pax6 for eye, that initiate cell-type-specific cascades), and whether it correctly identifies that fate stability comes from positive-feedback loops (a transcription factor sustains its own expression while activating downstream cell-type programs) and chromatin-state inheritance through cell division.

---

## AI Wayback Machine

The ideas in this chapter didn't appear from nowhere. **Mary-Claire King** showed in 1990 that breast cancer susceptibility could be inherited through a single gene, BRCA1 — at a time when most of her field believed the disease was too genetically heterogeneous to track. The discovery reshaped both cancer genetics and gene expression studies.

**Run this:**

```
Who is Mary-Claire King, and how does her work on BRCA1 and gene expression connect to the regulation of gene expression we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about her career or ideas.
```

→ Search **"Mary-Claire King"** on Wikipedia. See what the model got right, got wrong, or left out.

**Now make the prompt better.** Try one of these:

- Ask it to explain how a single BRCA1 mutation affects gene expression in cells decades before any tumor appears.
- Ask it to compare King's BRCA1 work with her earlier finding that humans and chimps share 99% of their DNA.

What changes? What gets better? What gets worse?
