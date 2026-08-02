# Chapter 17 — DNA: Structure, Replication, and the Machinery of Heredity
*Why a simpler molecule turned out to be the right one.*

---

Here is the thing that confused everyone for decades.

Proteins are built from twenty different amino acids. They fold into hundreds of distinct shapes. They catalyze reactions, transmit signals, form structural scaffolds, and do nearly all the active work of the cell. DNA, by contrast, is built from four bases, a single sugar, and a phosphate backbone. It does almost nothing on its own. It just sits there.

So when scientists were trying to identify the molecule that carries inherited traits — the molecule that makes you *you*, that gets copied and passed to your children — the obvious candidate was protein. Not DNA. Protein, with its chemical diversity and functional complexity, seemed like the only molecule capable of encoding the richness of biological information.

They were wrong. And the reason they were wrong is one of the most illuminating things in molecular biology: the simpler molecule turned out to be more capable precisely *because* it was simpler. The four-base monotony of DNA is not a limitation. It is the mechanism.

---

## The Experiment That Settled It

The key experiments happened in two acts.

The first act was Griffith's 1928 experiment with bacteria. He had two strains of *Streptococcus pneumoniae*. One strain was smooth-coated and lethal to mice. The other was rough-coated and harmless. He killed the smooth bacteria with heat, mixed their remains with living rough bacteria, and injected the mixture into mice. The mice died. The rough bacteria had somehow acquired the lethal character of the smooth ones.

Something had passed from the dead smooth cells to the living rough ones — some molecule carrying the instruction for the smooth coat, for lethality. Griffith called it the "transforming principle" and did not know what it was.

The second act came in 1944. Oswald Avery and his colleagues took the transforming principle and systematically destroyed it with enzymes. Destroy proteins: transformation still works. Destroy RNA: transformation still works. Destroy DNA: transformation stops. The transforming principle was DNA.

Then in 1952, Hershey and Chase did something more direct. They used a virus that infects bacteria — a bacteriophage — and labeled its DNA with radioactive phosphorus and its protein coat with radioactive sulfur. The phage infects the bacterium. Which radioactive label enters the cell? Phosphorus, which is in the DNA. Sulfur, which is in the protein coat, stays outside. The cell is infected by DNA alone. New phage particles are produced from that DNA alone.

The molecule that enters and replicates is not protein. It is DNA.

<!-- → [DIAGRAM: side-by-side summary of the three key experiments — Griffith (1928): rough + heat-killed smooth → smooth bacteria recovered; Avery (1944): DNase stops transformation, protease/RNase do not; Hershey-Chase (1952): radioactive P enters cell, radioactive S stays outside — student should see the logical chain from "something transfers" to "DNA specifically transfers" across 24 years of evidence] -->

This should have been a surprise, but it wasn't entirely, because by 1952 Erwin Chargaff had already published something that hinted at DNA's deeper structure. He had measured the base compositions of DNA from many different organisms. The percentages of A, T, G, and C varied between species — different organisms have different DNA compositions. But within any species, something held constant: the amount of adenine always equaled the amount of thymine. The amount of guanine always equaled the amount of cytosine.

Why would A equal T and G equal C, always, in every organism? Chargaff didn't know. But the answer was embedded in the structure, waiting to be seen.

---

## The Structure

In 1953, Watson and Crick published the double helix — built partly from their own reasoning, partly from crystallography data including Rosalind Franklin's extraordinary X-ray photograph of DNA, which showed the molecule's geometry with unusual clarity.

The structure is this. DNA is a double strand. Each strand is a polymer: nucleotides linked together, the phosphate group of one nucleotide bonded to the sugar of the next, forming a sugar-phosphate backbone. From each sugar, a base points inward. The two strands wind around each other in a right-handed helix, with the backbones on the outside and the bases facing inward, toward each other.

The bases pair. Not randomly. Adenine on one strand pairs with thymine on the other — two hydrogen bonds. Guanine pairs with cytosine — three hydrogen bonds. These are the only pairings that work geometrically. A purine (two-ring base: A or G) must pair with a pyrimidine (one-ring base: T or C), and the specific hydrogen bond donors and acceptors in the bases enforce which pairs are stable. A-T and G-C are the only combinations that fit.

<!-- → [IMAGE: structural diagram of the double helix showing (1) the sugar-phosphate backbone on the outside, (2) base pairs in the interior, (3) A-T pair with 2 hydrogen bonds and G-C pair with 3 hydrogen bonds labeled, (4) antiparallel orientation of the two strands with 5'→3' arrows pointing in opposite directions — student should see why bases are protected inside and why A=T and G=C follows from the pairing geometry] -->

This is what Chargaff's rules were saying. If every adenine on one strand is paired with a thymine on the other, then measuring the entire double-stranded molecule, A must equal T. Same for G and C. Chargaff's rules are the chemical fingerprint of complementary base pairing.

Now consider the geometry more carefully. The two strands are *antiparallel*. One strand runs 5' to 3' (meaning the chain goes from the 5' carbon of one sugar to the 3' carbon of the next). The other strand runs in the opposite direction: 3' to 5'. They are antiparallel the way two lanes of traffic run in opposite directions on the same road.

The diameter of the helix is uniform: 2 nanometers. This is because a purine-pyrimidine pair always has the same width as any other purine-pyrimidine pair. The base pairs are spaced 0.34 nanometers apart. The helix completes one full turn every 3.4 nanometers — ten base pairs per turn.

These numbers matter less as facts to memorize and more as evidence of a specific point: the geometry is *regular*. It does not vary. The helix is the same shape regardless of the sequence of bases. That regularity — that independence of shape from sequence — is what allows DNA to store arbitrary information without changing its physical properties. You can put any base sequence you want into DNA and it will still be a double helix with the same dimensions. The backbone doesn't care what the bases are.

---

## Why the Structure Is Also the Solution to Copying

Watson and Crick's paper ended with a sentence that became famous: "It has not escaped our notice that the specific pairing we have postulated immediately suggests a possible copying mechanism for the genetic material."

The sentence is restrained. What they meant was: the structure *is* the mechanism. Look at how the base pairing works. If you have one strand — say, the sequence 5'-ATGCG-3' — then the complementary strand is completely determined: 3'-TACGC-5'. Not approximately determined. *Completely* determined. Given one strand, you can derive the other using only the pairing rules. No additional information is needed.

This means: if you separate the two strands and let each one serve as a template, and if you have free nucleotides available in the cell, each template will produce its complement. A on the template pulls in T. G pulls in C. The new strand grows from the template, base by base, until a new complementary strand is complete.

The result: two double-stranded DNA molecules, each consisting of one original strand and one newly synthesized strand. This is semiconservative replication — each original strand is *conserved* into a new molecule, paired with a fresh complement.

The proof came in 1958 when Meselson and Stahl grew *E. coli* in medium containing heavy nitrogen ($^{15}$N), which was incorporated into the DNA bases, making the DNA denser than normal. Then they transferred the bacteria to medium with normal nitrogen ($^{14}$N) and tracked what happened to the DNA density through successive generations.

If replication were conservative — old strands stay together, new strands form a new double helix — you'd see two DNA populations after one generation: heavy (old) and light (new).

If replication were dispersive — old and new material somehow scrambled into each strand — you'd see a gradual shift from heavy toward light, with no sharp bands.

What they actually saw after one generation was a single band at intermediate density. Every DNA molecule was a hybrid: one $^{15}$N strand, one $^{14}$N strand. After a second generation, two bands appeared: one hybrid (intermediate density) and one fully light (two $^{14}$N strands). This is exactly what the semiconservative model predicts. The heavy $^{15}$N strand from generation one kept serving as a template, producing hybrid molecules indefinitely. New $^{14}$N/$^{14}$N molecules appeared from hybrid templates.

<!-- → [DIAGRAM: Meselson-Stahl results — three columns showing generation 0, 1, and 2; each column shows a centrifuge tube with labeled bands (heavy, hybrid, light); alongside each generation, the predicted banding pattern for conservative, semiconservative, and dispersive models — student should see that only the semiconservative model matches all three generations simultaneously, not just one] -->

The experiment is beautiful because the prediction is so specific. If you understand the mechanism — one strand templates one complement — you can calculate exactly what the density distribution should be at each generation and then check it. Biology is not always like physics, but here it is exactly like physics: a structural model makes quantitative predictions, and the measurements confirm them precisely.

---

## The Machinery

The actual copying process in a cell requires more than just separating strands and letting bases find their complements. Several proteins do essential work.

**Helicase** unwinds the double helix. It breaks the hydrogen bonds between base pairs and separates the two strands, creating a replication fork — a Y-shaped junction where the two template strands diverge and copying proceeds.

**Primase** synthesizes short RNA primers — short complementary sequences that provide a starting point. DNA polymerase cannot start a new chain; it can only extend an existing one. The primer gives it a 3' end to work from.

**DNA polymerase** does the actual synthesis. It reads the template strand in the 3' to 5' direction and synthesizes the new strand in the 5' to 3' direction, adding nucleotides one at a time. Each incoming nucleotide is chosen by the template base — A pairs with T, G pairs with C — and attached to the growing chain's 3' end.

Here is where the antiparallel structure creates a problem. The two template strands run in opposite directions. DNA polymerase can only synthesize in one direction: 5' to 3'. On one strand — call it the *leading strand* — the template runs 3' to 5' in the direction the replication fork is moving. This means DNA polymerase can follow the fork continuously, synthesizing a long, uninterrupted new strand. Smooth.

But on the other strand — the *lagging strand* — the template runs 5' to 3' in the direction the fork is moving. DNA polymerase must synthesize *away* from the fork, in the direction opposite to fork movement. This means the lagging strand cannot be synthesized in one continuous piece. Instead, it is synthesized in short segments called Okazaki fragments — each one starting with a new RNA primer, growing a few hundred to a few thousand nucleotides, and stopping. The fragments are later joined together by an enzyme called DNA ligase after the RNA primers are replaced with DNA.

<!-- → [DIAGRAM: replication fork diagram — Y-shaped fork with leading strand shown as continuous synthesis in the direction of fork movement; lagging strand shown as Okazaki fragments synthesized away from the fork, each preceded by an RNA primer; label helicase at the fork tip, DNA polymerase on both strands, primase, and ligase joining fragments — student should see that the asymmetry is forced by the antiparallel structure, not a design choice] -->

This asymmetry — continuous synthesis on the leading strand, discontinuous synthesis on the lagging strand — is not a flaw in the system. It is an unavoidable consequence of the antiparallel structure of DNA combined with the unidirectional nature of DNA polymerase. The cell uses a slightly awkward workaround (Okazaki fragments) rather than a simpler-but-slower alternative. The cost is the RNA primer replacement and ligation steps. The benefit is that both strands are copied simultaneously at the replication fork, which is far faster than copying one strand at a time.

---

## How Accurate Is It?

DNA polymerase makes a mistake — incorporates the wrong nucleotide — about once per 100,000 bases during synthesis. That sounds bad. The human genome has about 3 billion base pairs. If every base were copied with 1-in-100,000 accuracy, each replication would introduce roughly 30,000 errors.

But DNA polymerase also proofreads. As it adds each nucleotide, it checks whether the new base correctly pairs with the template. A mismatch — a base added to the wrong template base — creates a slight distortion in the helix geometry. The polymerase detects this, backs up, removes the incorrect nucleotide, and inserts the correct one. This proofreading reduces the error rate to about 1 per 10 million bases.

Then mismatch repair enzymes scan the newly synthesized DNA for remaining errors and fix them. After all error correction, the final mutation rate in human DNA is about 1 error per billion base pairs per replication. That is extraordinary fidelity.

But it is not perfect. And it should not be perfect.

If copying were perfect — zero errors ever — DNA sequence would never change. Every generation would be identical to the last. There would be no variation, and without variation there is nothing for natural selection to act on. Evolution would stop.

If copying were much less accurate — say, 1 error per thousand bases — organisms would accumulate mutations so fast that vital genes would be disabled within a few generations. This is called error catastrophe: too many mutations per replication for an organism to remain viable.

The actual error rate — about 1 per billion — sits in the narrow window where variation is rare enough that organisms are stable from generation to generation, but common enough that populations accumulate variation over many generations, giving natural selection something to work with. This rate is not a coincidence. It is the product of billions of years of selection for replication fidelity that is high enough to preserve function but low enough to permit evolution.

The structure of the double helix is what makes this precision achievable. The complementary base pairing creates an error-detection mechanism: a mismatched base doesn't fit properly, creating a geometric distortion that the polymerase and repair enzymes can find. If DNA were single-stranded, or if bases could pair promiscuously with multiple partners, there would be no geometrically correct template to compare against. The complementary strand is the reference. The pairing rules are the standard. Without them, proofreading would have nothing to proofread against.

---

## What the Structure Actually Explains

Step back from the details and see the logic.

DNA is the right molecule for heredity not because of its chemical complexity but because of a structural coincidence that turns out not to be a coincidence at all: the same feature that stores information also provides the template for copying that information. These are not two separate properties that happen to coexist. They are the same property expressed twice.

The information is stored as a sequence of bases. The template for copying is the complementary strand that those bases determine. You cannot have one without the other. A sequence defines its complement. The complement defines how to reproduce the sequence. Store the information and you have automatically stored the copying instructions.

This is why DNA, not protein, is the genetic material. Proteins could store information in their amino acid sequences. But protein synthesis does not work by complementary templating. There is no straightforward way for a protein to serve as a template for making a copy of itself. The chemistry doesn't work that way.

DNA's chemistry does. Four bases, simple pairing rules, and a regular geometry. The simplicity that made DNA seem like the wrong candidate in the 1940s turned out to be exactly the property that made it the right one.

Chargaff measured A = T and G = C in samples from every organism he tested and didn't know what it meant. Franklin photographed a perfect helix and the geometry screamed double-stranded regularity. Meselson and Stahl watched the heavy strand chase through generations and the density bands told them exactly what was happening. In each case, the evidence was the structure announcing its own mechanism.

That is the shape of this chapter's argument: the structure of DNA is not a separate fact from the mechanism of heredity. It is the mechanism. Understand the geometry of the helix and you understand why information is stable, why copying is accurate, why mutations are rare but not absent, and why life is possible at all.

Below the cell is chemistry. At the cell is life. And threading through both, connecting them, is the double helix — a molecule whose form is its function.

---

## Exercises

**Warm-up**

1. A DNA strand has the sequence 5'-GCTATAC-3'. Write the complementary strand in the correct antiparallel orientation, with its 5' and 3' ends labeled. Then explain in one sentence why the complementary strand is completely determined by the first — why there is no other possible complement.

2. Chargaff measured the base composition of DNA from three organisms and found: organism A has 28% adenine; organism B has 18% guanine; organism C has 22% cytosine. For each organism, determine the percentage of every other base and explain how you know — without measuring — what those percentages must be.

3. The Hershey-Chase experiment labeled phage DNA with $^{32}$P and phage protein with $^{35}$S, then infected bacteria and used a blender and centrifuge to separate phage coats from infected cells. The $^{32}$P was found inside the bacteria; the $^{35}$S was in the supernatant outside. Why was the blender step necessary? What would the experiment have failed to show without it?

**Application**

4. Meselson and Stahl started with $^{15}$N/$^{15}$N DNA and allowed replication in $^{14}$N medium. Predict the banding pattern — heavy, hybrid, or light — at generations 0, 1, 2, and 3. Then predict what a fourth generation band would look like. Now predict what you would see at generation 1 if replication were conservative rather than semiconservative. What is the critical generation at which the conservative and semiconservative models make different predictions, and why?

5. A drug is developed that specifically inhibits primase. Predict its effect on leading strand synthesis and on lagging strand synthesis separately. Would the drug halt replication entirely, or affect only one strand? Explain why, using what you know about how each strand requires (or does not require) primers.

6. DNA polymerase has an error rate of about 1 per 100,000 bases before proofreading, and about 1 per 10 million bases after proofreading. The human genome contains roughly 3 billion base pairs. Calculate the number of errors expected per genome replication before proofreading and after proofreading. Then explain why proofreading requires complementary base pairing to function — what would be lost if DNA were single-stranded?

**Synthesis**

7. The chapter argues that the antiparallel structure of DNA and the unidirectional constraint of DNA polymerase together make Okazaki fragments unavoidable. Design a thought experiment: imagine a hypothetical DNA polymerase that could synthesize in both the 5'→3' and 3'→5' directions. Would Okazaki fragments still be necessary? Would the replication fork behave differently? What new problems might arise if both directions of synthesis were possible? (Consider: what would proofreading look like for a 3'→5' polymerase?)

8. The chapter notes that the actual mutation rate of about 1 per billion sits in "a narrow window" between error catastrophe and evolutionary stagnation. RNA viruses such as influenza replicate with error rates of about 1 per 10,000 bases — roughly 100,000 times higher than human DNA replication. Using the chapter's logic, what are the evolutionary advantages and disadvantages of this high error rate for a virus? Why might an RNA virus benefit from a higher error rate than a eukaryotic cell, even though the high rate would be lethal for a larger organism?

9. Griffith's 1928 experiment showed that "something" from dead smooth bacteria transformed live rough bacteria. Avery's 1944 experiment identified that something as DNA. Hershey and Chase's 1952 experiment confirmed that DNA — not protein — is the molecule that carries genetic information into an infected cell. Why did three separate experiments spread over 24 years seem necessary to convince the scientific community? What does this progression tell you about the standard of evidence required to overturn a prevailing hypothesis in science?

**Challenge**

10. The chapter explains that the uniform diameter of the double helix — 2 nanometers regardless of sequence — results from a purine always pairing with a pyrimidine. This means A (purine) pairs with T (pyrimidine), and G (purine) pairs with C (pyrimidine), never purine-purine or pyrimidine-pyrimidine. Consider what would happen structurally if a purine-purine mismatch were forced into the helix. What would happen to the helix geometry? How would DNA polymerase's proofreading mechanism detect this? Now consider the reverse: a pyrimidine-pyrimidine mismatch. Would it create the same distortion, a larger one, or a smaller one? What does this geometry tell you about why the pairing rules are absolute rather than probabilistic?

11. Watson and Crick famously noted that the complementary base pairing "immediately suggests a possible copying mechanism." But there is a constraint they didn't address in the original 1953 paper: the two strands of the double helix are intertwined. As replication proceeds, the parental helix must unwind ahead of the replication fork, and the two daughter helices must be untangled afterward. Look up "DNA topoisomerases" and describe the topological problem they solve. Why is this problem an unavoidable consequence of the double-helical structure, and why does solving it require breaking and rejoining DNA strands rather than simply pulling them apart?

---

*By Nik Bear Brown*

---

## LLM Exercises

The following exercises are designed for use with a large language model. Paste the prompt into any capable model and examine the response critically — not for correctness alone, but for whether the reasoning is mechanistic or merely verbal.

**Exercise 1 — Why double helix, geometrically**
Prompt a model: *"The Watson-Crick double helix is right-handed, with about 10 base pairs per turn and a diameter of approximately 2 nm. Walk me through why each of these geometric features is functionally important — not arbitrary. Specifically: why does a single-stranded molecule make a poor candidate for stable information storage, why does a triple helix make a poor candidate for replication, and why does the specific 2-nm diameter matter for the proteins that interact with DNA?"*

Evaluate whether the model engages with the structural-stability argument for the double helix (hydrogen bonds reinforced by base stacking), the access-during-replication problem with triple helices, and the protein-recognition argument for the consistent diameter (proteins that bind major and minor grooves can recognize sequences without unwinding the helix). Push for engagement with the "information storage AND retrievable" trade-off.

**Exercise 2 — Semiconservative replication and the Meselson-Stahl experiment**
Prompt: *"The Meselson-Stahl experiment (1958) distinguished three possible models of DNA replication: conservative, semiconservative, and dispersive. The semiconservative model won. Walk me through the experimental design — specifically, the use of heavy nitrogen (¹⁵N) labeling and density-gradient centrifugation — and explain how the observed banding patterns at one and two generations of replication ruled out the alternatives. Why was this called 'the most beautiful experiment in biology'?"*

Evaluate whether the model correctly identifies that semiconservative replication predicts a single intermediate-density band at one generation and two bands (intermediate + light) at two generations, while conservative would have predicted heavy + light at one generation and dispersive would have predicted progressively lighter intermediate at each generation. The "beautiful" framing reflects the experiment's three-way discrimination from a single elegant approach.

**Exercise 3 — DNA polymerase fidelity**
Prompt: *"DNA polymerase III in E. coli has an error rate of approximately 1 mistake per 10⁵-10⁶ base pairs incorporated, but proofreading reduces this to about 1 in 10⁷, and mismatch repair brings it to about 1 in 10⁹-10¹⁰. Walk me through each layer of accuracy: (1) the geometric and electrostatic discrimination at the active site, (2) the 3'→5' exonuclease proofreading activity, and (3) post-replication mismatch repair. Why does the cell need three layers — wouldn't a single very-accurate polymerase suffice?"*

Evaluate whether the model engages with the diminishing-returns argument: each additional layer of accuracy is more expensive (in time and energy) than the last. The cell evolved to a level where the residual error rate matches the optimal mutation rate for the species — too low and adaptation slows, too high and lethal mutations accumulate.

**Exercise 4 — Telomeres and the end-replication problem**
Prompt: *"Linear chromosomes face a problem prokaryotes (with circular chromosomes) do not: each round of DNA replication shortens the chromosome ends because DNA polymerase cannot fill in the gap left by removal of the final RNA primer on the lagging strand. Walk me through why this 'end-replication problem' is necessary, why telomeres provide a partial solution, and why telomerase reactivation is a near-universal feature of cancer. What would be the consequence for somatic cells if telomerase were constitutively active?"*

Evaluate whether the model correctly identifies that telomeres are repetitive non-coding sequences that act as buffers — they shorten with each division, but the loss is non-coding until the buffer is exhausted (Hayflick limit, ~50 divisions). Constitutive telomerase removes this brake, contributing to cancer cell immortality. Stem cells normally express telomerase; somatic cells generally do not.

**Exercise 5 — DNA repair pathways, distinguished**
Prompt: *"The cell uses different repair pathways for different types of DNA damage: nucleotide excision repair (NER) for bulky lesions like UV-induced thymine dimers; base excision repair (BER) for small chemical modifications like deamination; mismatch repair (MMR) for replication errors; homologous recombination (HR) and non-homologous end joining (NHEJ) for double-strand breaks. Walk me through the molecular logic of each pathway and explain why HR is high-fidelity while NHEJ is error-prone. Identify one human disease caused by failure of each pathway."*

Evaluate whether the model correctly identifies that HR uses a homologous template (sister chromatid) for accurate repair, while NHEJ directly ligates broken ends with potential loss of nucleotides. Disease examples: xeroderma pigmentosum (NER defect), MUTYH-associated polyposis (BER defect), Lynch syndrome (MMR defect), BRCA1/2-associated cancers (HR defect).

---

## AI Wayback Machine

The ideas in this chapter didn't appear from nowhere. **Erwin Chargaff** established in the late 1940s that in any sample of DNA, the amount of adenine equals thymine and guanine equals cytosine — Chargaff's rules. The pairing rules were Watson and Crick's most important clue, though Chargaff felt they never gave him proper credit.

**Run this:**

```
Who was Erwin Chargaff, and how do Chargaff's rules connect to the DNA structure we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.
```

→ Search **"Erwin Chargaff"** on Wikipedia. See what the model got right, got wrong, or left out.

**Now make the prompt better.** Try one of these:

- Ask it to walk through how A=T and G=C base pairing follows from Chargaff's quantitative rules — the inferential leap Watson and Crick made.
- Add a constraint: "Answer including Chargaff's famous bitterness about Watson and Crick, and what he felt was missing from their model."

What changes? What gets better? What gets worse?
