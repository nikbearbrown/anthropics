# Chapter 24 — Phylogenies and the History of Life
*How to read kinship from evidence when appearances lie.*

---

Here is a question that should unsettle you.

A dolphin looks more like a tuna than like a human. Same torpedo shape, same fins, same ocean, same efficient swimming motion. A whale looks more like a shark than like a cow. Yet the dolphin is more closely related to you than to any fish, and the whale's nearest living relative is the hippopotamus. If you sorted these animals by appearance, you would get the relationships exactly wrong.

This is the central problem of phylogenetics, and it matters enormously: how do you determine true evolutionary kinship when appearance can mislead you so completely? The answer is one of the more beautiful ideas in biology — and it requires learning to distrust your eyes.

---

## The Fundamental Distinction: Two Kinds of Similarity

When two organisms share a trait, there are exactly two possible explanations.

The first is homology: they share the trait because they inherited it from a common ancestor. The ancestor had the trait, and both descendants kept it. The bat's wing and your arm are homologous — not because they look the same or do the same thing (they don't), but because both are the same skeletal structure, inherited from the same ancestor. A bat wing, stripped of its membrane, reveals an arm: one upper arm bone, two forearm bones, wrist bones, and five elongated digits. It is a mammalian hand, stretched and wrapped in skin. Your hand and the bat's wing are the same bones doing different jobs.

The second is analogy: they share the trait because they independently evolved it in response to similar pressures. The bat's wing and the insect's wing both generate lift, but they have no structural relationship. An insect wing is an outgrowth of the exoskeleton — chitin-reinforced tubes with no bones at all. The two arrived at similar functions by entirely different routes, in lineages that haven't shared an ancestor for hundreds of millions of years.

The distinction is not subtle when you know what to look for, but it is easy to miss. It requires looking through function to structure, through appearance to mechanism.

Here is the key principle: complex shared structures are almost never analogous. The odds of two unrelated lineages independently inventing the same complicated architecture — the same bones, the same sequence, the same number — are vanishingly small. If two species share a simple trait (both have eyes, both have tails), that could be homology or analogy. If they share a specific complex arrangement of structures, that is almost certainly homology. Convergent evolution produces similar functions; it rarely produces identical mechanisms.

<!-- → [IMAGE: comparative forelimb anatomy — side-by-side skeletal diagrams of a human arm, bat wing, dolphin flipper, and bird wing, all to the same scale, with the humerus, radius, ulna, carpals, and individual digits color-coded identically across all four — student should see that the same bones are present in each case despite radically different external appearances and functions, making the homology visible rather than just described] -->

This is why the dolphin's flipper tells you the truth about its history. The flipper, examined carefully, shows arm bones — humerus, radius, ulna, carpals, and five digits packed closely together and flattened for hydrodynamic efficiency. These are not invented anew. They are the mammalian limb plan, inherited from a terrestrial ancestor, reshaped by millions of years of aquatic selection. The tuna's fin, by contrast, is rays of cartilage radiating from a base — the fish fin plan, unrelated in structure. Same function, different history, different homology. The bones tell you where each animal came from.

---

## Building the Tree: Cladistics

Once you accept that homology is what matters, you need a systematic way to use it. That system is cladistics.

The core insight of cladistics is that not all shared traits are equally informative. Consider the backbone: all vertebrates have it. If you are trying to figure out whether a fish or a lizard is more closely related to a mammal, the backbone is useless — it tells you nothing because everyone has it. The backbone is an ancestral character, inherited by all descendants of the common ancestor of vertebrates.

What you need is a derived character: a trait that arose in a specific ancestor and was inherited only by some descendants — those that came after the trait evolved. Hair is a derived character for mammals. No fish, amphibian, or reptile has it. Every mammal does. Hair was a novelty in some ancestral mammal, and all mammals inherited it. When you find hair, you have found a mammal or a descendant of a mammal.

Shared derived characters reveal relatedness. If two organisms share a derived character that a third lacks, those two are more closely related to each other — they share a more recent common ancestor from whom they both inherited the trait. The more shared derived characters two organisms share, the more recently they diverged.

The groups identified by shared derived characters are called clades. A clade is an ancestor and all of its descendants. The mammal clade includes all organisms that descended from the first mammal and all their descendants. It is defined by the shared derived characters all mammals possess: hair, mammary glands, three middle-ear bones (modified from ancestral reptilian jaw bones), warm blood, and others.

This last example — the ear bones — is worth dwelling on. Your inner ear contains three tiny bones: the malleus, incus, and stapes. They vibrate to translate sound into nerve signals. In your reptilian ancestors, two of these bones were part of the jaw joint. During mammalian evolution, they migrated from the jaw to the ear. The fossil record shows this transition clearly: there are ancient mammal-like reptiles whose jaw bones were shrinking and moving, partway through the transition. These bones are unambiguously homologous between reptiles and mammals — the same bones, doing different jobs. Homology reveals the history.

The practical procedure for building a cladogram is to score organisms for derived characters and then find the tree that most efficiently explains the pattern of shared characters. This leads to the principle of maximum parsimony: among all the possible tree arrangements, prefer the one that requires the fewest evolutionary changes.

Parsimony works because independent evolution of identical complex traits is rare. If two organisms share a derived character, the simpler explanation is usually that they inherited it from a common ancestor, not that it evolved twice independently. The most parsimonious tree — the one requiring the fewest convergent evolutions — is the most likely to be correct.

Here is how parsimony works in practice. Suppose you have three species and a derived character. If two species have the character and one doesn't, parsimony says the two with the character are more closely related — one evolutionary event (the origin of the character in their common ancestor) explains the data. If you instead proposed the two species evolved the character independently, that requires two events. One event is simpler than two. Parsimony chooses one.

<!-- → [DIAGRAM: parsimony comparison — two cladograms side by side for the same three taxa; left tree shows taxa A and B as sisters (one evolutionary event explains their shared derived character); right tree shows the character evolving independently in A and B (two events required); the number of required changes is labeled on each branch; student should see why parsimony favors the left tree and understand what "minimum number of changes" means visually] -->

This logic scales to larger datasets. With many species and many characters, the tree that minimizes the total number of required evolutionary changes across all branches is selected. Modern phylogenetic software searches this space and finds the most parsimonious arrangement.

---

## What the Molecular Record Added

Anatomical characters work well for organisms we can dissect. But appearances, even careful appearances, can mislead. Convergent evolution can fool you: two lineages can independently produce such similar structures that they look homologous when they aren't. And for microscopic organisms — bacteria, archaea — anatomy gives you almost nothing to work with. They are tiny, morphologically simple, and they look alike across vast evolutionary distances.

The revolution came from DNA. When Carl Woese began comparing ribosomal RNA sequences in the 1970s, he was analyzing a molecule present in every living cell — the machinery that translates genetic information into protein. It is the most universally conserved molecule in biology, which makes it ideal for comparing across the deepest branches of the tree.

Woese expected a spectrum: bacteria at one end, eukaryotes (nucleated cells) at the other, with a range of intermediates. What he found instead shocked the field. A group of methane-producing microbes from hot springs and anaerobic sediments — the methanogens — were as different from bacteria as eukaryotes were. Their ribosomal RNA occupied its own deep branch, separate from both bacteria and eukaryotes. Woese called this third group Archaea.

The discovery exposed something invisible to the naked eye. Archaea live in extreme environments — superheated volcanic vents, hypersaline lakes, anoxic sediments — and they are superficially indistinguishable from bacteria under a microscope. They have no nucleus. They are small. They look like bacteria. But their molecular machinery tells a different story. Their ribosomal RNA, their cell membrane chemistry, their transcription machinery, their gene regulation — all are fundamentally different from bacteria and in some ways more similar to eukaryotes.

The three-domain system of life that emerged from this work — Bacteria, Archaea, Eukarya — is one of the most significant reorganizations of biological knowledge in the twentieth century. It came entirely from applying cladistic logic to molecular data. Shared derived characters in ribosomal RNA sequences revealed a tree that appearance had hidden.

<!-- → [IMAGE: three-domain tree of life — branching diagram showing Bacteria, Archaea, and Eukarya as three major domains diverging from a common ancestor; within Eukarya, show further branching into protists, fungi, plants, and animals; label approximate divergence times where known from fossil/molecular evidence; student should see that Archaea and Eukarya are more closely related to each other than either is to Bacteria, and that the three-domain split is the deepest division in the history of life] -->

Molecular data also provided a tool for timing. DNA sequences accumulate mutations at roughly constant rates over time — not perfectly constant, but approximately so, especially for neutral substitutions in regions under little selective pressure. This is the molecular clock. If you know the mutation rate for a gene and you count the differences between two sequences, you can estimate when they diverged.

The logic is:

$$\text{Time since divergence} \approx \frac{\text{sequence differences}}{2 \times \text{mutation rate}}$$

The factor of two because each lineage has been accumulating mutations independently since they split. The calibration requires anchor points from the fossil record — pairs of species whose divergence time is known from fossils, which let you calculate the mutation rate, which you then apply to pairs without fossils.

Humans and chimpanzees differ at about one percent of their DNA. Calibrated against fossil evidence for a six-to-seven-million-year divergence, this gives a mutation rate that can be applied to other primate pairs and other lineages. The molecular clock is not a precision instrument — rates vary between genes and between lineages — but for rough estimates of divergence times over long scales, it works.

---

## When the Tree Gets Complicated

The tree model assumes that genes pass vertically — from parent to offspring, generation after generation, branching when populations split. For eukaryotes, especially sexually reproducing ones, this is roughly true. For prokaryotes, it is not.

Bacteria and archaea engage in horizontal gene transfer — the movement of genes between cells that are not in a parent-offspring relationship. There are three main routes. In transformation, a bacterium takes up free DNA from its environment, often from dead cells. In transduction, a bacteriophage accidentally packages some of its host's DNA and injects it into the next cell it infects. In conjugation, two bacteria form a direct bridge and transfer plasmids — small circular DNA molecules that can carry many genes at once.

These transfers are not rare. Estimates suggest that in some bacterial lineages, several percent of the genome may have arrived by horizontal transfer rather than vertical descent. The consequences for resistance evolution are well known: antibiotic resistance genes spread between species, between strains, across the entire bacterial world in years rather than millennia.

The consequence for phylogenetics is more troubling. If two bacterial species share a gene, it could mean they share a common ancestor — or it could mean one acquired the gene from the other (or from a third party) by horizontal transfer. A single gene tree might tell a different story than a different gene tree. Gene A says species X and Y are sisters. Gene B says X and Z are sisters. Gene C says Y and Z are sisters. Which is right?

This is not a resolution problem — it is a real phenomenon. Different genes have different histories when horizontal transfer scrambles them. The gene tree is not the same as the species tree. For prokaryotes, the species tree itself may be ill-defined: if genes can flow freely between lineages, the concept of a species — a discrete, isolated lineage — becomes uncertain.

<!-- → [DIAGRAM: tree vs. web of life — two panels; left panel: standard branching tree showing three bacterial species with purely vertical gene transmission; right panel: same three species with horizontal arrows crossing between lineages, showing gene A moving from species 1 to species 3 and gene B moving from species 2 to species 1; student should see how horizontal transfer creates a conflict between the gene tree (for any individual gene) and the species tree, and why the tree model is a simplification for prokaryotes] -->

The practical response is to use many genes, especially the core genes (ribosomal RNA, genes for core metabolic functions) that are less mobile than accessory genes. These tend to tell more consistent stories. The deep structure of the tree — the three-domain arrangement — is robust because it is supported by many independent core genes. But the finer branches, especially among bacteria, show more conflict.

Some researchers have proposed replacing the tree with a network or web model for prokaryotic life. Instead of strictly vertical branching, the model allows horizontal connections between lineages. This is more realistic but also more complex and harder to analyze. The tree model remains dominant, used with the understanding that it is a simplification — accurate for the major branches, increasingly approximate as you move into the prokaryotic details.

The deepest question this raises is about the base of the tree itself. Woese's three-domain model has a root — a common ancestor of all life — from which bacteria and archaea-plus-eukarya diverged. But when you look at eukaryotic genomes carefully, you find a mixture: some genes are most closely related to archaeal sequences, others to bacterial sequences. This is expected, given endosymbiosis: the mitochondrion was once a free-living bacterium, and its genes (now mostly transferred to the nucleus) are of bacterial origin. But beyond endosymbiosis, there may have been extensive gene mixing in early eukaryotic evolution.

Some models suggest the base of the tree is not really a trunk at all — not a single ancestral lineage — but a population of primitive cells exchanging genes so freely that they were more like a shared gene pool than distinct species. The tree of life emerges from this primordial web as lineages become isolated and vertical descent dominates. This is speculative, but it captures something important: the tree model is a good description of life after lineages separated and stopped exchanging genes, not necessarily before.

---

## What the Tree Reveals

Step back and see what the phylogenetic framework actually accomplishes.

It explains why appearance is unreliable. The dolphin looks like a fish because it independently evolved a fish-shaped body under the same hydrodynamic pressures that shaped fish. Convergent evolution produces similar appearances from different ancestries. The phylogenetic framework — using shared derived characters and molecular sequences rather than gross appearance — cuts through this noise.

It reveals deep connections invisible to intuition. Your middle ear bones were jaw bones in your reptilian ancestors. Your body is built on a vertebrate plan inherited from fish. Your cells run on molecular machinery shared with bacteria. These are not poetic observations — they are structural homologies, readable from the fossil record and from comparative anatomy and from DNA. Every homologous structure is a message from the past.

It provides a consistent method for building and testing hypotheses. Given a set of taxa and a set of characters, cladistics gives you a decision rule: find the tree that minimizes the required number of evolutionary changes. Different researchers using the same data should reach the same conclusion. When new data arrive — new fossils, new gene sequences — they can be incorporated and the tree revised. Phylogenies are hypotheses, and they improve with evidence.

It uncovers what we didn't know we were missing. Woese's discovery of Archaea was not a refinement of existing knowledge — it was the revelation that a third domain of life existed, invisible until molecular methods made it legible. What else remains invisible? Estimates of total species diversity suggest that most of life's diversity is microbial and uncharacterized. The tree of life we have drawn is mostly the eukaryotic tip of a vastly larger prokaryotic world.

And it raises the question that the next chapters will address: if we can read kinship from evidence, can we read history? Can we date the branches? Can we trace the sequence of events that produced the life we see today? The answer is yes, approximately, using the molecular clock and the fossil record together. But the deep past — the origin of the three domains, the origin of eukaryotes, the origin of life itself — remains incompletely mapped. The tree gives us the structure. The full story of what happened at each node is still being worked out.

---

## The Shape of the Argument

Here is the chapter's argument stated plainly.

Appearances mislead because similar function can evolve independently. The solution is to look for homologous structures — shared ancestry rather than shared function. Complex shared structures are strong evidence of homology. Cladistics formalizes this: build trees from shared derived characters, choose the most parsimonious tree, test the result with new data.

Molecular data extended this approach to organisms where anatomy gives little information, revealed the three-domain structure of life, and provided a molecular clock for dating divergences. Horizontal gene transfer complicates the picture for prokaryotes, where genes can flow between non-related lineages and produce gene trees that conflict with each other and with the species tree.

The framework is not complete — horizontal transfer, especially at the base of the tree, means the simple branching model is a simplification. But for eukaryotes, and for the major branches even of prokaryotic life, the tree provides an accurate picture of evolutionary kinship. It is one of the most powerful tools in biology, and its results — that whales are closer to hippos than to sharks, that you share ear bones with lizards, that there are three domains of life — are among the most surprising truths that careful evidence has revealed.

The bee on the echinacea flower, with which this chapter began, really is your relative. Everything alive is. The tools of phylogenetics let you know how close the relationship is — and more importantly, they let you *demonstrate* it from evidence, rather than simply assert it.

---

## Exercises

**Warm-up**

1. A student examining a shark and a dolphin notes that both have streamlined bodies, dorsal fins, and pectoral fins used for steering. The student concludes these structures are homologous and that sharks and dolphins are closely related. Identify the error in this reasoning. What type of similarity are these structures, and what evidence would you need to examine to determine whether they are homologous or analogous?

2. The chapter says the backbone is useless for determining which vertebrate is most closely related to which, because it is an ancestral character shared by all. Explain in your own words why ancestral characters cannot resolve relationships within the group that possesses them. What kind of character would actually distinguish a mammal from a fish within the vertebrate tree?

3. Woese found that methanogens — organisms that look like bacteria under a microscope and live in similar environments — are actually as different from bacteria as eukaryotes are. What specific type of data revealed this, and why was that data more informative than microscopic appearance? What does this episode tell you about the relationship between morphological similarity and evolutionary relatedness?

**Application**

4. You are constructing a cladogram for five vertebrates: a lamprey (jawless fish), a shark (cartilaginous fish), a salmon (bony fish), a frog (amphibian), and a mouse (mammal). You have scored them for the following derived characters: jaws (absent in lamprey, present in all others), bony skeleton (absent in lamprey and shark, present in all others), four limbs (present only in frog and mouse), amniotic egg (present only in mouse). Draw the most parsimonious cladogram, label each node with the derived character that defines the clade above it, and identify which pair is most closely related.

5. Two species of bacteria share a gene for antibiotic resistance. Species A and Species B are very different in every other measurable way — they belong to different phyla, have different metabolic strategies, and live in different environments. Yet their resistance gene sequences are 98% identical. What is the most parsimonious explanation for this observation? What alternative explanations exist, and how would you test between them?

6. Humans and chimpanzees differ at approximately 1% of their nuclear DNA. Humans and gorillas differ at approximately 1.6%. Using the molecular clock logic from the chapter, which pair diverged more recently? If the human-chimpanzee divergence is calibrated to 6 million years ago, estimate when humans and gorillas last shared a common ancestor. State clearly what assumption you are making, and explain why this assumption may introduce error.

**Synthesis**

7. The chapter argues that the three-domain structure of life (Bacteria, Archaea, Eukarya) was invisible until molecular methods revealed it. Yet morphological evidence has long shown that eukaryotes are structurally very different from prokaryotes (nucleus, organelles, cytoskeleton). Why didn't morphological cladistics separate Archaea from Bacteria before Woese's work? What does this reveal about the limits of morphology as a phylogenetic tool for prokaryotes specifically?

8. The chapter says that for sexually reproducing eukaryotes, the tree model works well because genes pass primarily vertically. But there are exceptions: horizontal gene transfer between eukaryotes is documented in plants (acquiring bacterial genes through plastid integration) and animals (endogenous retroviruses inserting viral DNA into host genomes). Using the same logic as the chapter applies to bacteria, predict what these horizontal transfers would do to a gene tree if you happened to analyze a gene that had been horizontally transferred. Would you expect to see the conflict if you analyzed ribosomal RNA instead? Explain why or why not.

9. The chapter ends with the observation that the tree model is "a good description of life after lineages separated and stopped exchanging genes, not necessarily before." This implies there may be a period early in the history of life where the concept of a species tree is not well-defined. Using what you know from Chapter 12 about cell reproduction and from Chapter 17 about DNA replication, describe what the early gene-pool model implies about the accuracy of the replication machinery in very early life. Would you expect early organisms to have higher or lower mutation rates than modern organisms, and how does that affect the concept of a molecular clock for events near the origin of life?

**Challenge**

10. The molecular clock assumes a roughly constant mutation rate, calibrated against known fossil divergences. But mutation rate is itself subject to natural selection: organisms under stronger selection for replication fidelity (large, long-lived organisms with complex development) tend to have lower mutation rates than organisms with short generation times and large population sizes. Design an experiment to test whether the molecular clock ticks at different rates in two distantly related organisms — one with a short generation time (bacteria) and one with a long generation time (whales). What genes would you compare, what reference calibration would you use, and what result would constitute evidence that the clock is running at different speeds in the two lineages?

11. A new computational study claims to have resolved the root of the tree of life by analyzing 100 universally conserved genes from all three domains. The study places the root between Bacteria and the Archaea-Eukarya clade. A second study, using different genes and a different analysis method, places the root between Archaea and the Bacteria-Eukarya clade. Both studies use maximum likelihood methods and claim statistical support for their conclusions. Using what you know about horizontal gene transfer, molecular clocks, and the limits of parsimony, identify at least three specific methodological differences or confounding factors that could explain why two rigorous studies reach opposite conclusions about the same root. What additional evidence — not yet available — would most decisively resolve the disagreement?

---

*By Nik Bear Brown*

---

## LLM Exercises

The following exercises are designed for use with a large language model. Paste the prompt into any capable model and examine the response critically — not for correctness alone, but for whether the reasoning is mechanistic or merely verbal.

**Exercise 1 — Reading a phylogenetic tree carefully**
Prompt a model: *"Given a rooted phylogenetic tree of vertebrates with branches for fish, amphibians, reptiles, birds, and mammals, walk me through what the tree does and does not tell me. Specifically: (1) does sister-taxon relationship between A and B mean A is more 'related to' B than to C? (2) Can I read the order of evolution from left-to-right at any node? (3) Does branch length necessarily correspond to time? Then identify one common misreading of a phylogenetic tree."*

Evaluate whether the model correctly identifies that (1) sister-taxon relationships reflect recency of common ancestor (yes — A and B share a more recent common ancestor with each other than either does with C), (2) left-to-right ordering at a node is arbitrary (the tree can be rotated at any node without changing relationships), and (3) branch length depends on the type of tree — chronograms have time-proportional branches; cladograms have arbitrary branch lengths; phylograms scale to molecular distance. The common misreading is treating extant taxa at the tips as ancestral to other extant taxa.

**Exercise 2 — Cladistics and the principle of parsimony**
Prompt: *"Cladistic analysis builds phylogenetic trees by minimizing the number of evolutionary changes (parsimony) required to explain observed character distributions. Walk me through this approach using a small example: given three taxa with binary characters, how do you determine which tree is most parsimonious? Then explain why parsimony has limits — what if the true history involved many parallel evolutions or reversals that parsimony would miss?"*

Evaluate whether the model correctly explains the basic parsimony algorithm and engages with the long-branch attraction problem: when evolutionary rates differ dramatically among lineages, parsimony can mistakenly group two long branches together because they share many independent (not homologous) changes. Modern methods (maximum likelihood, Bayesian inference) explicitly model evolutionary rates to avoid this.

**Exercise 3 — Molecular clocks and their calibration**
Prompt: *"Molecular clocks estimate divergence times by counting genetic differences between species and converting to time using a calibrated mutation rate. Walk me through the calibration problem: how do biologists choose calibration points, what assumptions does the molecular clock make, and what happens to time estimates when those assumptions are violated? Use the human-chimp split (~5-7 million years ago [verify]) as an example."*

Evaluate whether the model engages with the calibration challenges (most calibrations come from fossil dates, which provide minimum but not maximum ages; rates vary among genes, lineages, and time periods), and whether it correctly identifies that the human-chimp divergence date has been revised multiple times as both fossil dating and molecular clock methods have improved.

**Exercise 4 — Convergence vs. homology in tree-building**
Prompt: *"Building a phylogenetic tree requires distinguishing homologous traits (shared due to common ancestry) from analogous traits (shared due to convergent evolution). Walk me through how researchers distinguish the two — particularly when morphological traits are misleading. Why is molecular data often more reliable for tree-building than morphological data, and what are the cases where molecular data can also mislead?"*

Evaluate whether the model engages with the practical heuristics (look at multiple traits, check for similar developmental origin, examine the geographic and temporal context), and engages with molecular convergence (e.g., similar substitution patterns can arise in independent lineages under similar selection pressures, particularly in mitochondrial genes under metabolic constraints).

**Exercise 5 — Horizontal gene transfer and the 'tree of life'**
Prompt: *"In bacteria and archaea, horizontal gene transfer (HGT) is so common that perhaps 20-30% of genes in some species came from other organisms rather than from inheritance [verify]. This complicates the 'tree of life' metaphor — for prokaryotes, the appropriate metaphor may be a 'web of life' rather than a tree. Walk me through three mechanisms of HGT (transformation, transduction, conjugation) and explain what HGT means for phylogenetic analysis: which genes can still be used to build trees, and which cannot?"*

Evaluate whether the model engages with the mechanisms (transformation = uptake of free DNA; transduction = phage-mediated; conjugation = direct cell-to-cell via pili), and whether it correctly identifies that ribosomal RNA genes are typically not subject to HGT (they're essential, conserved, and any change would disrupt function), making them the gold standard for prokaryotic phylogeny. Genes encoding metabolism, antibiotic resistance, and many surface proteins are commonly transferred.

---

## AI Wayback Machine

The ideas in this chapter didn't appear from nowhere. **Willi Hennig** founded cladistics in his 1950 German monograph — proposing that classification should reflect shared derived characters and branching events, not overall similarity. His method now underlies essentially every phylogenetic tree in modern biology.

**Run this:**

```
Who was Willi Hennig, and how does cladistics connect to the phylogenies and history of life we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.
```

→ Search **"Willi Hennig"** on Wikipedia. See what the model got right, got wrong, or left out.

**Now make the prompt better.** Try one of these:

- Ask it to walk through what "shared derived character" (synapomorphy) means using a vertebrate example — what counts, what doesn't.
- Ask it to compare Hennig's cladistic method with the older "evolutionary systematics" of Mayr and Simpson.

What changes? What gets better? What gets worse?
