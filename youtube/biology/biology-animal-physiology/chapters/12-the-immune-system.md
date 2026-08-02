# Chapter 12 — The Immune System

## TL;DR

- One wall, two layers, and an invention that happened twice.
- The chapter moves through The design problem, The wall: barriers, phagocytes, and pattern recognition, Pattern recognition — TLRs and the ancient wall, Adaptive immunity — a vertebrate invention built from a transposon, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

*One wall, two layers, and an invention that happened twice.*

---

In 1996, Bruno Lemaitre dropped fungal spores onto fruit flies missing one gene. The flies died within days, covered in filamentous growth — *Aspergillus fumigatus* eating them from the inside out. The missing gene was called *Toll*.

The strange part is that *Toll* was already famous, for a completely unrelated reason. A decade earlier, Christiane Nüsslein-Volhard had named the gene while mapping developmental mutations in *Drosophila* embryos. Flies lacking *Toll* had two backs and no belly — a body-plan catastrophe. She had looked at the mutant phenotype under the microscope and said *Toll* — "neat!" in German — and the name stuck. *Toll* was a developmental gene. It told the embryo which side was which.

Lemaitre and his supervisor Jules Hoffmann had just shown it also fought fungi.

One year later, Charles Janeway's lab at Yale, searching for what binds bacterial lipopolysaccharide in human cells, found a human gene that looked strikingly like *Toll*. They called it a Toll-like receptor — TLR. Bruce Beutler then found mice that could not respond to lipopolysaccharide, traced the defect to *TLR4*, and confirmed: TLR4 is the human receptor for the outer membrane of Gram-negative bacteria. Hoffmann and Beutler shared the 2011 Nobel Prize.

Here is what is worth sitting with. A fly and a human, separated by roughly 600 million years of evolution, fight microbes using the same family of receptors, signaling through the same family of intracellular adapters, ending at the same family of transcription factors. The molecules have different names because they were discovered separately in different organisms. They are the same machinery, inherited from a common ancestor that fought microbes before there were insects, before there were vertebrates, before there was anything more complex than a worm crawling through Cambrian mud.

That ancestor's immune system has not been replaced in either lineage. It has been *added to* in vertebrates. The antibody, the T cell receptor, immunological memory — these are layered on top of an older system that is still doing most of the work.

Now take the sea urchin. *Strongylocentrotus purpuratus*, the purple sea urchin of the California coast, lives in seawater containing roughly a billion bacteria per liter. No antibodies. No lymphocytes. No immunological memory. By the framing where adaptive immunity is the sophisticated defense and innate immunity the primitive backup, the sea urchin should be constantly dying. Some individuals live 200 years.

When the sea urchin genome was sequenced in 2006, the immune-relevant results should have been impossible under the old framing. The sea urchin has 222 Toll-like receptor genes. Humans have 10. The sea urchin has 203 NOD-like receptors. Humans have about 22. Innate immunity at staggering diversity, no adaptive layer, centuries of survival in bacterially saturated seawater.

So which animal has the "simple" immune system? The question is badly posed. The right question is: what is the problem, what solutions exist, and which solution does each lineage use? That is what this chapter is about.

---

## The design problem

Every animal faces the same puzzle. Pathogens share the environment. Some mutate fast. An individual host may encounter pathogen variants its ancestors never saw. The host needs a defense that works *immediately* against *anything*, the moment a pathogen crosses a barrier. But hosts also benefit from a defense that improves with experience — one that remembers, responds faster the second time.

Those two requirements are in tension. An immediate response cannot be highly specific, because specificity costs time — time to identify the matching receptor, time to amplify the cells that carry it. A specific response cannot be immediate, because amplification takes days. Optimize for one and you fail at the other.

Evolution has produced two architectural answers.

The first: recognize *categories* of pathogen using receptors encoded in the germline. Bacterial cell walls contain lipopolysaccharide; the receptor for LPS is built into every macrophage at birth. Recognition is instant; the response is generic. This is **innate immunity** — fast, broad, no memory, and ancient. Present in every animal phylum on Earth.

The second: generate receptors that recognize *individual* pathogen molecules, by random shuffling so the receptor repertoire covers an enormous space of possible shapes, then *select* from that repertoire the cells whose randomly-generated receptors happen to fit the pathogen at hand. This is **adaptive immunity** — slow at first, exquisitely specific, capable of memory, restricted to vertebrates.

Of the roughly 35 major animal phyla, only one — the chordates — contains lineages with adaptive immunity, and even within chordates the invertebrate members (tunicates, lancelets) do not have it. Adaptive immunity in the antibody-and-T-cell sense exists only in vertebrates. Innate immunity runs through all of them. When you hear "innate immunity," do not hear "primitive." Hear *universal* — the system most life on Earth uses.

---

## The wall: barriers, phagocytes, and pattern recognition

Before any cellular response engages, animals are protected by their integuments. Vertebrates have stratified keratinized skin, slightly acidic, colonized by normal flora. Arthropods have a chitin-protein cuticle, replaced periodically by molting. Molluscs have shells and mucus. Sponges have epithelial cell layers coated in glycoprotein mucus. The materials differ. The principle is the same: keep the outside outside.

Behind the physical barrier, every animal runs chemical defenses on surfaces that must remain permeable to function. Antimicrobial peptides — defensins in mammals, cecropins and drosomycin in insects, magainin in amphibians — are secreted onto mucosal surfaces. These short cationic peptides exploit the chemistry difference between bacterial and animal lipid bilayers: they punch holes in microbial membranes and bacteria die. Defensins exist in insects, plants, fungi, and vertebrates — separated by more than a billion years, still using the same chemistry.

When a pathogen breaches a barrier, some cell must find and destroy it. The answer, across the entire animal kingdom, is phagocytosis — wrapping membrane around the target, pulling it inside, fusing the vesicle to compartments full of digestive enzymes. The mechanism is so general that the same cellular machinery eats food in amoebae and eats pathogens in macrophages. Single-celled eukaryotes were doing phagocytosis a billion years before there were animals.

Every animal phylum examined has phagocytic cells: amoebocytes in sponges, hemocytes in insects, coelomocytes in sea urchins, macrophages and neutrophils in vertebrates. These are not analogous structures invented independently. They are homologous — they share an ancestral cell type. The molecular pathways inside a fly hemocyte engulfing a bacterium and a human neutrophil engulfing the same bacterium are recognizably the same machinery with the same conserved proteins doing the same molecular jobs.

The recognition step — how does the cell know what to phagocytose — is where the Toll-like receptors come in.

### Pattern recognition — TLRs and the ancient wall

How does a cell recognize a pathogen it has never seen before, in seconds? It does not recognize the specific pathogen. It recognizes a *pattern* characteristic of pathogens.

The shorthand: **PRR** stands for pattern recognition receptor, a protein that binds a molecular feature characteristic of microbes and absent from the host's own cells. The features it binds are called **PAMPs** — pathogen-associated molecular patterns. Bacterial lipopolysaccharide. Peptidoglycan fragments from bacterial cell walls. Flagellin. Double-stranded RNA in the cytoplasm. Unmethylated CpG DNA.

These features did not evolve to be recognized by immune systems. They are evolutionary inevitabilities — structures pathogens cannot conceal because they are essential to pathogen biology. A Gram-negative bacterium that gave up its lipopolysaccharide outer membrane would die. A virus that produced no double-stranded RNA at any stage of replication would not replicate. The immune system evolved receptors for these features precisely because the features cannot be hidden.

Each TLR recognizes a different PAMP class. TLR4 binds LPS. TLR5 binds flagellin. TLR3 binds double-stranded RNA. TLR9 binds unmethylated CpG DNA. The recognition is not strain-specific — TLR4 cannot distinguish *E. coli* LPS from *Salmonella* LPS. It just registers "Gram-negative outer membrane is present." Pattern, not identity.

The Toll receptor family runs across the entire animal kingdom, documented in cnidarians, the earliest-branching animals with true tissues. Sponges have similar pathways. *Drosophila* has 9 Toll receptors. Humans have 10. Sea urchins have 222. The downstream signaling is also conserved: in the fly, Toll binding leads to degradation of the inhibitor Cactus, releasing the transcription factor Dif to enter the nucleus and activate antimicrobial peptide genes. In humans, TLR binding leads to degradation of the inhibitor IκB, releasing the transcription factor NF-κB to enter the nucleus and activate inflammatory genes. Different names; same molecules; same circuit; 600 million years.

The fly's innate system has two distinct arms. The **Toll pathway** handles fungi and Gram-positive bacteria (thick peptidoglycan, no outer membrane). The **Imd pathway** handles Gram-negative bacteria (the lipopolysaccharide signature). Different recognition, different intracellular signaling, different downstream antimicrobial peptides. The output of both is a cocktail of peptides secreted by the fat body into the hemolymph — drosomycin for fungi, cecropin and diptericin for bacteria — at concentrations lethal to microbes. Phagocytic hemocytes circulate alongside; parasites too large to phagocytose are encapsulated by hemocytes that layer around them and deposit melanin to wall them off.

What the fly does not have: antibodies, T cell receptors, MHC molecules, somatically rearranged receptors, immunological memory, B cells, T cells, lymph nodes, thymus, spleen. None of it. The fly lineage has been doing this for at least 350 million years. There are roughly 150,000 extant species of dipterans. The strategy works.

![Parallel signaling columns ](images/12-the-immune-system-fig-01.png)
*Figure 12.1 — Parallel signaling columns *

---

## Adaptive immunity — a vertebrate invention built from a transposon

Roughly 500 million years ago, a transposable element — a stretch of DNA that moves around within genomes — landed inside an immune-receptor gene in the lineage that became jawed vertebrates. The element brought the molecular machinery for cutting and rejoining DNA: enzymes that recognize specific signal sequences, cut at those sequences, and splice the cut ends back together with errors. The errors became the feature.

The transposase became **RAG** — the recombination-activating genes RAG1 and RAG2. The genes it landed in became the immunoglobulin and T cell receptor loci. The process became **V(D)J recombination** — the mechanism by which vertebrate lymphocytes generate the diverse antigen receptors that define adaptive immunity.

V(D)J recombination is worth slowing down on.

Each immunoglobulin gene is not a single stretch of DNA. It is a library of gene segments. The heavy-chain locus contains a cluster of V (variable) segments, a cluster of D (diversity) segments, and a cluster of J (joining) segments. During B cell development, the RAG enzymes cut the DNA between segments and splice one V, one D, and one J segment together, deleting the intervening DNA permanently from that cell's genome. The choice is essentially random. Combinatorial diversity from this step alone — roughly 40 V segments × 23 D segments × 6 J segments for the heavy chain, times a similar count for the light chain — gives on the order of $3 \times 10^7$ possible antibody specificities from recombination alone.

Then the imprecision adds another layer. When RAG cuts and splices, it does the job with errors: nucleotides are added or removed at the junctions by a separate enzyme, terminal deoxynucleotidyl transferase (TdT). Each junction can be modified independently. The diversity multiplier from junctional variation drives the total potential repertoire to roughly $10^{11}$ distinct specificities — a hundred billion possible antibody shapes.

The library is generated randomly during lymphocyte development. The response to any pathogen is then the *selection* of the rare cells whose randomly-generated receptor happens to fit the pathogen's surface. Those cells proliferate — clonal expansion. The pathogen is cleared. A subset of the expanded cells persists as **memory cells**, positioned to respond faster and more powerfully on the next encounter. This is the **clonal selection** principle, worked out by Frank Macfarlane Burnet in the 1950s.

After antigen encounter, the bound B cells can undergo a third diversification step in germinal centers of lymph nodes: **somatic hypermutation** — their immunoglobulin genes mutate at rates roughly a million times higher than the rest of the genome. Variants whose mutations improve binding are selected; variants whose mutations destroy binding die. Antibodies progressively tighten their fit to the antigen over the days and weeks of an infection. This is affinity maturation.

The cost: the library generator produces some receptors that bind self molecules. If those cells matured and circulated, they would attack the animal's own tissues. The solution is **negative selection** in the thymus — developing T cells are tested against self-antigens and any that bind self too strongly are killed. Roughly 95–98% of developing thymocytes die this way. The cost of broad recognition is the near-total elimination of the cells you generate.

For T cells to recognize foreign antigens at all, they need to see what is happening inside other cells. The answer is **MHC** — major histocompatibility complex — cell-surface proteins that display fragments of the cell's own proteins on the surface for T cells to inspect. MHC is present in all jawed vertebrates and absent in all earlier lineages. The MHC region is the most genetically diverse part of the vertebrate genome, the diversity maintained by frequency-dependent selection from pathogens: a rare MHC variant is harder for pathogens to evade, so rare variants rise in frequency until they become common enough to be targeted.

![V(D)J recombination diagram ](images/12-the-immune-system-fig-02.png)
*Figure 12.2 — V(D)J recombination diagram *

---

## The lamprey's parallel system — adaptive immunity invented twice

Here is the result that made the field rethink the evolutionary story.

Jawless vertebrates — lampreys and hagfish — branched off from the jawed vertebrate lineage roughly 500 million years ago. They have backbones, most vertebrate organs, many vertebrate features. They do not have immunoglobulins, T cell receptors, or MHC molecules. By the standard story, they should have only innate immunity.

In 2004, Zeev Pancer and colleagues showed that lampreys have adaptive immunity — built from entirely different proteins.

The lamprey adaptive receptor is called a **variable lymphocyte receptor**, VLR. Instead of immunoglobulin domains — the protein fold that makes up vertebrate antibodies — the lamprey VLR is built from **leucine-rich repeats**, a different protein-folding motif. Each VLR is generated during lymphocyte development by gene conversion: a library of leucine-rich-repeat cassettes in the genome, assembled into a unique VLR on each lymphocyte by somatic shuffling. The estimated diversity is on the order of $10^{14}$ distinct VLRs — possibly higher than the immunoglobulin repertoire.

This is not a homolog of V(D)J recombination. The molecular machinery is different. The protein scaffold is different. The cellular biology is different. But the *strategy* is identical: generate diverse antigen receptors by somatic shuffling during the animal's lifetime; deploy them on lymphocytes that undergo clonal selection on antigen encounter; retain memory cells for faster response on re-exposure.

Two completely different protein systems, two different gene-shuffling mechanisms, two independent evolutionary inventions of adaptive immunity — one in jawed vertebrates, one in jawless vertebrates, starting from different molecular ingredients.

The fact that adaptive immunity evolved twice is a strong statement about the selective pressure. The engineering problem — broad receptor diversity beyond what germline encoding can provide — was the same problem, confronted independently, and evolution found two different solutions. The pressure to remember pathogens was apparently strong enough to drive the invention not once but twice within the vertebrate lineage.

This also makes the non-evolution of adaptive immunity in sea urchins or insects more interesting rather than less. The sea urchin solved the problem by expanding the germline repertoire of innate receptors — 222 TLRs encoding a broader library of fixed-recognition molecules, no somatic shuffling required. The insect did not expand the TLR repertoire to sea-urchin scale; it managed with 9 Toll receptors and a tight coupling to a few well-characterized pathogen classes. Neither strategy is adaptive in the vertebrate sense. Both strategies work.

---

## Memory — what vertebrates gain and what it costs

After an adaptive response clears an infection, most of the activated B cells and T cells die. A subset persists as memory cells — not actively producing antibodies, not actively killing infected cells, but pre-positioned with receptors already specific for the pathogen at hand, ready to expand rapidly on re-exposure.

The second response to the same pathogen is qualitatively different. Memory B cells reactivate within hours rather than days. Antibody titers rise within two to three days rather than seven to ten. The peak titer is ten to a hundred times higher than the primary peak. The pathogen is often eliminated before symptoms develop.

This is the mechanism vaccination exploits entirely. A vaccine delivers antigen without the danger of the actual disease; the immune system mounts a primary response, generates memory cells, and stands ready. When the real pathogen arrives later, the memory response eliminates it before it can establish. Vaccination is possible only in animals with adaptive immunity. The fly cannot be vaccinated. The sea urchin cannot be vaccinated.

The cost is twofold. First, the apparatus is expensive: the thymus, the bone marrow lymphoid niches, the lymph nodes, the spleen, the constant production of new lymphocytes, the near-total elimination of self-reactive clones — all metabolic load that an innate-only animal does not pay. Second, the system fails in characteristic ways. Autoimmunity — the same machinery attacking self. Allergy — responses against harmless antigens mediated by IgE. Immune evasion by pathogens — HIV exploits CD4 helper T cells; many viruses downregulate MHC I to hide from cytotoxic T cells. An animal without adaptive immunity cannot suffer IgE-mediated allergy, cannot develop the vertebrate form of autoimmunity, and cannot be targeted by HIV. It also cannot be vaccinated.

The trade-off is what makes the evolutionary picture coherent. Animals with short lifespans and rapid reproduction may not benefit enough from memory to justify the apparatus. A fly that lives weeks does not need to remember a pathogen for years. Animals with long lifespans, large bodies, and slow reproduction benefit a great deal from memory — and adaptive immunity arose in vertebrates, which have all three features.

The sea urchin is the counter-example that cannot be ignored. Some individuals live 200 years, in bacterially saturated seawater, without memory. Whether sea urchins have some functional analog of trained immunity — innate cells re-tuned by past exposure to respond more strongly to subsequent encounters — is an open question in the current literature. The honest answer is that we do not fully understand how sea urchins achieve century-scale survival without adaptive memory, and the simple formulation "long life requires adaptive immunity" is falsified by their existence.

---

## What the chapter is really about

Return to the fly and the human, running the same signaling circuit for 600 million years.

The vertebrate trick — V(D)J recombination, somatic hypermutation, MHC, clonal selection, memory — is real and powerful. It is also recent, restricted to a single subphylum, and built by repurposing a transposable element that happened to land in an immune-receptor gene. The fact that jawless vertebrates independently evolved a parallel system using entirely different proteins suggests the selection pressure was genuine and the engineering problem hard.

But the trick was not invented from nothing. It was added behind a wall that had been standing for 600 million years. The wall runs in the fly. The wall runs in the sea urchin. The wall runs in you. When you are exposed to a bacterium you have never encountered, your macrophages phagocytose it, your TLR4 fires on the LPS, your NF-κB activates, your neutrophils extravasate, your complement coats the bacterial surface — all before a single B cell has seen the antigen, all using machinery that operates by the same principle in an insect. The adaptive system takes over a few days later, if necessary.

Most encounters, the wall is enough. Adaptive immunity is the addition for cases where the wall is not enough, for animals that live long enough for re-encounters to matter, for pathogens that have evolved ways to evade innate recognition. It is layered, not replacing. The lecture note here is not "adaptive is better." It is: *different problems required different solutions, the solutions are layered in evolutionary order, and the oldest layer is still doing most of the work.*

---

## Exercises

| phagocytic cells | antimicrobial peptides | TLR | PRR count | complement |
| --- | --- | --- | --- | --- |
| sponge, Drosophila, sea urchin, lamprey, shark | frog | mouse | columns: phagocytic cells, antimicrobial peptides, TLR | PRR count, complement, somatic receptor shuffling, receptor type (immunoglobulin |
| immunological memory | to be placed at start of exercises as a working reference | A concrete checkpoint for applying the chapter concept. | A concrete checkpoint for applying the chapter concept. | A concrete checkpoint for applying the chapter concept. |

**Warm-up 1.** For each of the following animals, predict whether it has (a) phagocytic cells, (b) Toll-like receptors, (c) complement, (d) adaptive immunity with somatic receptor shuffling, and (e) immunological memory. Justify each prediction from the animal's phylogenetic position: hydra (cnidarian), octopus (mollusc), sea urchin (echinoderm), hagfish (jawless vertebrate), frog (amphibian). For the hagfish specifically, state whether its adaptive immune system resembles the jawed vertebrate system or the lamprey VLR system, and explain why. *Tests: mapping immune toolkit to phylogenetic position across the animal kingdom.*

**Warm-up 2.** A fruit fly is infected with two pathogens simultaneously: *Aspergillus fumigatus* (a fungus) and *Escherichia coli* (a Gram-negative bacterium). (a) Identify which intracellular signaling pathway is activated by each pathogen, and name the transcription factor each pathway activates. (b) Name one antimicrobial peptide secreted in response to each pathogen, and state how each kills the pathogen at the molecular level. (c) Predict what happens to the fly's immune response if a mutation eliminates the Cactus inhibitor protein. Does the fly become more resistant, less resistant, or do you predict a more complex outcome? Explain the mechanism. *Tests: the Toll vs. Imd pathway distinction and the logic of the inhibitor-release signaling architecture.*

**Warm-up 3.** V(D)J recombination generates antibody diversity in three sequential steps. (a) Name each step, identify which enzymes are responsible, and calculate the approximate number of distinct heavy-chain specificities produced by combinatorial joining alone (use: ~40 V segments, ~23 D segments, ~6 J segments). (b) Explain what junctional diversity adds and why the imprecision of RAG cutting is a feature rather than a bug. (c) Compare the total diversity estimate ($10^{11}$) to the number of B cells in the human body (approximately $10^{12}$). What does this ratio tell you about whether the adaptive immune repertoire is a representative sample of possible specificities? *Tests: V(D)J recombination arithmetic and the library-generator concept.*

**Application 1.** The sea urchin *Strongylocentrotus purpuratus* has 222 Toll-like receptor genes; humans have 10. (a) Explain what functional advantage the sea urchin's expanded TLR repertoire provides over the human TLR repertoire, in terms of pathogen recognition specificity. (b) State what the sea urchin's expanded repertoire cannot provide that vertebrate adaptive immunity does provide, and explain the mechanistic reason. (c) A genome-sequencing project reveals that a newly discovered deep-sea annelid has 180 Toll-like receptor genes. Predict, using the sea urchin as a reference, what this suggests about the annelid's ecological context and the trade-off it has made relative to an annelid with a more typical 5–10 TLR count. *Tests: interpreting TLR gene count as an ecological and evolutionary signal.*

**Application 2.** The VLR system in lampreys and the immunoglobulin system in jawed vertebrates both generate diverse antigen receptors by somatic shuffling and both support clonal selection and memory. (a) Identify the protein-folding motif used in each system and explain why this makes them parallel rather than homologous solutions. (b) The lamprey VLR repertoire is estimated at $10^{14}$ distinct specificities — larger than the human immunoglobulin estimate of $10^{11}$. What does this imply about the relative efficiency of leucine-rich repeat shuffling versus V(D)J recombination as diversity-generating mechanisms? (c) The fact that adaptive immunity evolved independently twice within the vertebrate lineage is described as "a strong statement about the selective pressure." State explicitly what inference this supports, why two independent inventions are stronger evidence for selective pressure than one invention would be, and what alternative explanation would need to be ruled out. *Tests: the parallel evolution logic and its implications for selection pressure.*

**Application 3.** A macrophage encounters a bacterium it has never seen before. Trace the events from initial contact to phagocytic destruction of the bacterium, naming: (a) the PRR that detects the bacterial PAMP, (b) the PAMP being detected, (c) the intracellular signaling cascade (in vertebrate terms), (d) the transcription factor that enters the nucleus, (e) the gene expression changes that result, and (f) the mechanism by which the phagocyte actually kills the bacterium inside the phagolysosome. Then identify which steps in this sequence would be absent in a fruit fly hemocyte performing the same function, and which steps would be present with homologous molecules. *Tests: tracing innate recognition from receptor to killing across the vertebrate-invertebrate divide.*

**Synthesis 1.** Construct a functional comparison between the sea urchin's strategy and the vertebrate adaptive strategy for handling a pathogen encountered multiple times during a long lifespan. (a) In the sea urchin, what happens at the molecular level during the first encounter with a novel pathogen, and what happens during the tenth encounter with the same pathogen? (b) In a mouse, what is the mechanistic difference between the first and second response to the same pathogen? (c) The sea urchin lives 200 years without immunological memory. Propose at least two mechanisms that might compensate for the absence of memory in a long-lived innate-only organism, and for each propose a specific experiment on sea urchin coelomocytes that would test whether the mechanism is operating. (d) State explicitly why the sea urchin's longevity is a challenge to the claim that adaptive immunity is necessary for long-lived animals, and what additional evidence would resolve whether the challenge is real or apparent. *Tests: integrating the sea urchin counter-example with the vertebrate memory framework — refusing the tidy resolution in either direction.*

**Synthesis 2.** Vaccination exploits immunological memory to generate protection before exposure to a dangerous pathogen. (a) Trace exactly what happens in a mouse after vaccination with an inactivated virus: which cells are activated, which receptors are engaged, what diversity-generating process operates, what happens at the germinal center, and what persists after the response resolves. (b) Explain why the same vaccine given to a sea urchin would provide no lasting protection, and what cellular machinery the sea urchin lacks that prevents the vaccine from working. (c) An immunologist proposes designing a "vaccine" for sea urchins that works through the innate system rather than the adaptive system — using repeated low-dose exposure to a pathogen PAMP to prime a stronger future innate response. Evaluate this proposal: what cellular mechanism would it need to exploit (trained immunity), and what feature of innate immune cells would need to be different from the default state for this to work? *Tests: connecting the mechanistic basis of vaccination to the comparative immune toolkit — and evaluating trained immunity as an alternative to adaptive memory.*

**Challenge.** You are studying a captive population of 200-year-old sea urchins that has experienced a 40% mortality event from a novel bacterial pathogen. Survivors have higher coelomocyte counts and produce more antimicrobial peptides when challenged with the same pathogen in vitro compared to naive sea urchins from a different population. (a) Propose two alternative hypotheses to explain the survivors' enhanced response: (H1) the survivors were selected from the original population because they happened to carry more TLR variants matching this particular pathogen; (H2) the survivors' coelomocytes were epigenetically reprogrammed by the initial infection to respond more strongly — a form of trained immunity. (b) Design a cross-population experiment to distinguish these hypotheses. Specify the experimental groups, the measurements you would take, and the result pattern that would support H1 versus H2. (c) If H2 is supported, what is the implication for whether sea urchins have "memory" in a functional sense? Would this count as the kind of memory that vertebrate adaptive immunity provides, or something fundamentally different? State the criteria you are using to make this distinction. *Tests: experimental design to test competing immunological hypotheses; precise definition of what counts as memory — mechanistic rather than operational.*

---

## LLM Exercise — building the comparative immunity simulator

Build **`12-immune-evolution.html`**: a single self-contained HTML file with an interactive simulator that lets the user select an animal and a pathogen and watch the immune response unfold as a timeline.

### Show

Tell the LLM what the simulator is for before asking for code:

> *"I am building an educational HTML simulator that compares innate immune responses across seven animals — sponge, Drosophila, sea urchin, lamprey, shark, frog, mouse — against four pathogens — bacterium, fungus, virus, parasite. The point is comparative evolutionary biology: the same problem (defend the animal against this pathogen) gets solved with different toolkits depending on which immune components the animal has. Adaptive immunity (antibodies, memory) should only appear for jawed vertebrates. The lamprey should show a VLR-based adaptive response that is structurally similar to but molecularly distinct from the jawed-vertebrate adaptive response. Invertebrates should show only innate components."*

### Say

Specify what mechanism each curve should embody:

```
For each animal-pathogen combination, the timeline should show:
(1) barrier breach at t=0
(2) PRR activation and phagocyte recruitment within hours
(3) antimicrobial peptide secretion within 12-24 hours
(4) complement activation within hours (where present)
(5) for jawed vertebrates only: B and T cell activation within days,
    antibody peak around days 14-21, memory cell generation by day 21
(6) for lamprey only: a parallel VLR-mediated curve, similar timing
    to immunoglobulin response, labeled as molecularly distinct
    
Sea urchin should show greater PRR diversity (wider, more sustained
PRR curve than the fly) but no adaptive response.

Drosophila should distinguish fungal vs. bacterial pathogens:
Toll pathway for fungi and Gram+ bacteria, Imd pathway for
Gram- bacteria, with different antimicrobial peptide outputs.

On a second-exposure toggle, jawed vertebrates and lamprey show
a faster, higher-titer secondary response. Invertebrates show
essentially identical curves to first exposure.

Also display:
- A bar chart comparing time-to-clearance and clearance efficiency
  across animals for the selected pathogen.
- A side panel with the Toll/TLR conservation diagram: fly
  components (Toll, Cactus, Dif) paired with human homologs
  (TLR4, IκB, NF-κB), drawn in parallel columns with connecting
  lines.
```

### Constrain

```
Hard constraints:
- Vanilla HTML, CSS, JavaScript only. No external libraries.
  No React, no D3. Canvas for rendering.
- Comment each calculation. Use clearly named functions
  (e.g., primaryAntibodyResponse(day, animal, pathogen))
  so the math is readable in source.
- The Drosophila Toll vs. Imd pathway split must be implemented
  correctly: Toll for fungi and Gram+, Imd for Gram-.
- The lamprey VLR curve must be labeled as molecularly distinct
  from immunoglobulin, not just a duplicate of the jawed-vertebrate
  curve with a different name.
- The sea urchin PRR curve must be visibly broader and longer-
  lasting than the fly PRR curve, reflecting greater TLR diversity.
- No server required. Must run by double-clicking the HTML file.
```

### Verify

When the code comes back, do not just run it. Read the source and check these seven conditions. For each failure, write a specific follow-up prompt naming the failure.

1. Does the sponge show no adaptive curves and no complement?
2. Does *Drosophila* correctly distinguish fungal (Toll pathway) from Gram-negative bacterial (Imd pathway) pathogens?
3. Does the sea urchin PRR curve show greater diversity than the fly's?
4. Does the lamprey show a VLR curve labeled as molecularly distinct from immunoglobulin?
5. Do jawed vertebrates (shark, frog, mouse) show both innate and full adaptive components?
6. On second exposure, do only jawed vertebrates and lamprey show a faster secondary response? Invertebrates should look the same as the first exposure.
7. Does the Toll/TLR conservation diagram correctly pair fly Cactus with human IκB, fly Dif with human NF-κB, and fly Toll with human TLR4?

### Explore

Once the simulator works, use it as a thinking tool.

Run the **sponge vs. mouse comparison against a bacterium on first exposure**. The sponge clears it with innate immunity alone; the mouse clears it at about the same speed on first exposure but much faster on second. The point: innate immunity is enough for first encounters; adaptive immunity's advantage is in *re-encounters*. The sponge has been managing first encounters for 600 million years.

Run ***Drosophila* against a fungus**, then switch the pathogen to a Gram-negative bacterium. Watch the dominant pathway switch from Toll to Imd, and the antimicrobial peptide cocktail change composition. This is what pattern-specific innate immunity looks like — two different arms responding to two different molecular signatures.

Run the **sea urchin against any pathogen and watch the PRR curve**. The breadth and sustained intensity of the PRR response should visually reflect the 222 TLR genes. This is the "scaled-up innate" alternative to adaptive immunity made visible — not a simple system, not a primitive system, a *different* system.

Run the **lamprey vs. the shark against the same virus, second exposure**. Both show fast secondary responses. Both are labeled with different molecular machinery — VLRs and immunoglobulins. Parallel evolution, same strategy, different proteins.

### Extension to Chapter 13

The immune system you have built operates throughout adult life. But many components are different in early development — fetal and neonatal immune systems are not smaller versions of adult ones. Maternal antibodies cross the placenta in mammals or transfer via yolk in birds, providing passive immunity to offspring. Before Chapter 13 (animal reproduction), ask your LLM:

*"In animals with internal fertilization and live birth, how does the maternal immune system avoid attacking the fetus, which is genetically half-foreign? Name the major mechanisms — placental immunoprivilege, regulatory T cells, HLA-G expression — and explain what trade-off each represents. What does this tell us about why immune tolerance and reproductive biology are deeply coupled in animals with long gestations?"*

The immune system is not a free parameter. It is constrained by the animal's reproductive biology, and the two evolved together.

---

**What would change my mind.** Convincing evidence that invertebrate trained immunity provides functionally equivalent memory to vertebrate adaptive memory — durable, antigen-specific, transferable — would force me to retreat from the claim that immunological memory is a vertebrate innovation. The current evidence for trained immunity in invertebrates is suggestive but falls well short of that bar. If it clears the bar, the evolutionary story would need to be rewritten around a deeper conservation of memory mechanisms.

**Still puzzling.** Why did adaptive immunity arise specifically in jawed vertebrates rather than earlier in deuterostome evolution? The transposable-element-insertion hypothesis explains the molecular origin but not the timing. The sea urchin's 222 TLRs and centuries-long lifespan suggest that long life without adaptive immunity is viable, so the selection pressure driving the vertebrate innovation is not yet fully accounted for. It is one of the genuinely open questions in evolutionary immunology.

---

**Tags:** comparative-immunology, toll-receptors, vertebrate-evolution, vdj-recombination, lamprey-vlrs
