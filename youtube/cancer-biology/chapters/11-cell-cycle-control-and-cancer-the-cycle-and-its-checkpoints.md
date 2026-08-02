# Chapter 11 — Cell Cycle Control and Cancer: The Cycle and Its Checkpoints
*The Cell Does Not Decide to Divide.*

In a research lab, time-lapse microscopy follows a single human cell preparing to divide. For about eleven hours it grows, makes protein, senses its surroundings. Then it copies its entire three-billion-letter genome over roughly eight hours. It pauses, checks its work, and only then enters the brief, dramatic minutes of mitosis. As the chromosomes line up at the cell's equator, the movie shows something unexpected: the cell waits. For several minutes it sits at metaphase, chromosomes aligned but motionless. Then the sister chromatids snap apart and the cell divides.

That pause is not hesitation. It is a checkpoint doing its job — verifying, before the irreversible step, that every chromosome is correctly attached to the machinery that will pull it apart. The cell has not decided anything. There is no decision-maker inside it. A system of regulatory proteins detected that a condition was not yet met, and the system held.

This is the conceptual starting point for everything that follows. A cell does not *choose* to divide. A control system decides for it — and the control system's job is to ensure that replication happens exactly once, in order, only when conditions warrant, with every error caught before the point of no return. Cancer is what happens when that system breaks down. To understand the breakdown you first have to see the system, because the mutations that drive cancer are not random damage — they are systematic dismantling of the controls.

---

The cell cycle is four phases: **G1** (Gap 1), **S** (Synthesis), **G2** (Gap 2), and **M** (Mitosis). For a typical human cell dividing over twenty-four hours, G1 takes about eleven hours, S about eight, G2 about four, and M about one. G1, S, and G2 together are interphase — everything before the chromosomes become visible and move. M is the visible act.

In **G1** the cell grows and assesses its environment: nutrients, growth-factor signals, contacts with neighboring cells, the integrity of its own DNA. If conditions are favorable it eventually commits to S phase; if not, it can exit into **G0**, a quiescent state that is not death — the cell persists, metabolically active, awaiting a signal to re-enter. **S phase** replicates every chromosome exactly once. The once-and-only-once constraint is enforced by **origin licensing**: in G1, each replication origin is loaded with a protein complex that licenses it to fire, and the licensing is irreversible within a single cycle — once an origin fires, it cannot be relicensed until after mitosis is complete. This is why re-replication catastrophes are rare rather than routine. **G2** verifies that replication finished and checks for any residual breaks. **M** separates the chromosomes, first aligning them and then pulling the pairs apart, and divides the cell in two.

Three **checkpoints** guard this sequence — surveillance mechanisms that halt the cycle until specific conditions are met. The **G1/S checkpoint** is the major commitment decision: should the cell enter S phase at all? The **G2/M checkpoint** verifies that replication is complete and no unrepaired breaks remain before allowing the cell into mitosis. The **spindle assembly checkpoint**, operating within M phase, holds the cell at metaphase until every chromosome is correctly attached to the pulling machinery — it is the source of the pause in the opening time-lapse.

![Circular cell-cycle wheel showing G1, S, G2, and M phases with approximate hours, three checkpoints (G1/S, G2/M, spindle assembly) marked at their positions, and a G0 quiescence exit from G1.](images/11-cell-cycle-control-and-cancer-the-cycle-and-its-checkpoints-fig-01.png)
*Figure 11.1 — The cell cycle and its three checkpoints*

<!-- → [DIAGRAM: cell cycle wheel — G1, S, G2, M phases in order with approximate hours labeled; three checkpoints marked at their positions with their condition verified; G0 shown as an exit from G1] -->

---

The machine that drives the cycle is a family of **cyclin-dependent kinases** — CDKs. A CDK is an enzyme that phosphorylates other proteins, attaching phosphate groups that activate, inactivate, or relocate its targets. By itself a CDK is essentially inactive. It becomes active only when bound to a **cyclin** — a regulatory partner whose concentration rises and falls through the cell cycle (International Journal of Molecular Sciences, 2021). The cyclins are synthesized on demand and destroyed on schedule; their periodic accumulation is what makes the cycle directional.

A tempting analogy is a clock — the cyclins tick forward at a fixed rate. The analogy fails immediately for cyclin D, which is induced by external growth-factor signals and is intrinsically unstable, degraded within minutes if the signal drops. Cyclin D does not tick; it reports whether the cell is currently being told to grow. If growth-factor signaling stops, cyclin D falls, and so does the pressure to enter S phase. The cycle stalls, not because a timer ran out, but because the signal that the environment wanted the cell to divide was no longer present. The cyclins are **signal integrators**, not timekeepers.

The major cyclin–CDK pairings map to the transitions they drive:

**Cyclin D + CDK4/6** drives progression through G1. Cyclin D is induced by mitogenic signals through Ras–MAPK; it begins phosphorylating the Rb protein, starting the commitment process. **Cyclin E + CDK2** completes the G1/S transition, finishing Rb phosphorylation and committing the cell to S phase. **Cyclin A + CDK2** operates during S phase, coordinating replication. **Cyclin B + CDK1** drives entry into mitosis.

At the end of each phase, the relevant cyclin is tagged for destruction by the ubiquitin–proteasome system — the SCF ligase during G1/S and the APC/C ligase from M phase onward. This destruction is not incidental cleanup. It is mechanistically essential: each phase requires that the *previous* cyclin–CDK activity fall before the next can take over. If cyclin B, for instance, persists through the end of mitosis rather than being degraded, the cell cannot reset to G1 — the next cycle cannot begin because the engine from the last one is still running. One-directionality depends on each wave of cyclin activity destroying itself.

The CDK proteins themselves stay at roughly constant levels through the cycle; what changes is which cyclin is available and whether specific inhibitor proteins are bound to the complex.

---

The G1/S checkpoint is the control point cancer most frequently disrupts, and its logic is worth understanding carefully because it behaves not as a gradual dial but as a switch — one that, once thrown, cannot easily be reversed.

The molecular core is the **Rb–E2F switch**. Rb is the retinoblastoma protein, encoded by the *RB1* gene — the protein is the gate; the gene is the instruction; losing the gene removes the protein and leaves the gate permanently open. In a quiescent cell, hypophosphorylated Rb binds the E2F transcription factors and holds them at the promoters of S-phase genes, blocking transcription. The cyclin E gene cannot be expressed. The replication machinery cannot be assembled. The cell cannot enter S phase.

When growth signals drive cyclin D–CDK4/6 activity, the complex phosphorylates Rb. Partially phosphorylated Rb releases some E2F, which transcribes cyclin E. Cyclin E pairs with CDK2 and *further* phosphorylates Rb — a positive-feedback loop. Hyperphosphorylated Rb releases all E2F, and the full S-phase program switches on: cyclin E, cyclin A, DNA polymerases, the entire replication apparatus (NCBI Bookshelf, *Molecular Biology of the Cell*).

The feedback is what makes this a switch rather than a ramp. Below a threshold of mitogenic input, Rb stays bound and E2F stays silent. Above the threshold, positive feedback drives the system to the fully E2F-released state. This is **bistability**: two stable states, with a sharp transition between them. It explains why the restriction point is a true commitment. Before it, removing growth factors causes cyclin D to fall, Rb to become hypophosphorylated again, and the cell to return to G0. After it, the feedback has carried Rb phosphorylation to the hyperphosphorylated state, E2F is fully active, and the S-phase program is already running — removing growth factors at this point does not reverse the decision.

This bistability is not a peripheral detail. It is the design principle that makes cell division a commitment rather than a continuous process. A gradually increasing probability of entering S phase would mean cells would drift into replication at low growth-factor concentrations; the sharp threshold ensures that partial signals do not trigger division.

![Signal-circuit flow from mitogen through Ras–MAPK and cyclin D–CDK4/6 to partial Rb phosphorylation, E2F release transcribing cyclin E, and a positive-feedback loop where cyclin E–CDK2 fully phosphorylates Rb to commit the cell to S phase.](images/11-cell-cycle-control-and-cancer-the-cycle-and-its-checkpoints-fig-02.png)
*Figure 11.2 — The Rb–E2F switch*

<!-- → [DIAGRAM: Rb–E2F switch circuit — mitogen → Ras–MAPK → cyclin D → cyclin D–CDK4/6 → Rb partial phosphorylation → cyclin E released → cyclin E–CDK2 → Rb hyperphosphorylation → E2F fully released → S-phase genes activated; positive feedback arrow from cyclin E back to Rb phosphorylation clearly marked] -->

Cancer dismantles this switch by any of several equivalent routes. **Loss of Rb itself**: if the protein is absent, E2F is constitutively free and the cell enters S phase regardless of growth signals. **Amplification of cyclin D or CDK4**: if the kinase activity that phosphorylates Rb is excessive, the threshold is easily overcome. **Loss of p16/INK4a** (encoded by *CDKN2A*, one of the most frequently deleted tumor suppressor loci in human cancer): p16 specifically inhibits CDK4/6, so losing it removes the brake on Rb phosphorylation and lets cyclin D–CDK4/6 operate unopposed. All three routes produce the same cellular outcome — constitutive E2F activity, constitutive S-phase entry — by attacking different components of the same switch. This is why the restriction point is broken in so many cancers: there are multiple entry points.

![Convergence map: Rb loss, cyclin D amplification, CDK4 amplification, and p16/INK4a deletion all feed the Rb–E2F switch, producing constitutive E2F activity and unconditional S-phase entry.](images/11-cell-cycle-control-and-cancer-the-cycle-and-its-checkpoints-fig-04.png)
*Figure 11.4 — Four routes break one switch*

---

The CDK inhibitor proteins are the endogenous brakes. Two families govern this.

The **CIP/KIP family** — p21, p27, p57 — inhibits a broad range of cyclin–CDK complexes. **p21** (encoded by *CDKN1A*) is the critical one here: it is a direct transcriptional target of p53. When DNA damage activates p53, one of p53's first responses is to transcribe *CDKN1A*, producing p21, which inhibits cyclin E–CDK2 and arrests the cell at G1/S. This is the molecular explanation for why p53 is called the guardian of the genome — its tumor-suppressive activity operates substantially through halting the cell cycle before damaged DNA is replicated. A cancer that has lost p53 (about half of all human cancers) loses this arrest mechanism at G1/S.

The **INK4 family** — p16, p15, p18, p19 — inhibits CDK4/6 specifically, competing with cyclin D for binding. **p16/INK4a** is the most cancer-relevant. It is encoded by *CDKN2A*, which also encodes *ARF* (p14ARF), a stabilizer of p53. The same genomic locus therefore contributes to both CDK4/6 braking and p53 maintenance — losing it disables two controls at once, which is presumably why it is among the most commonly deleted regions in cancer.

---

The G2/M checkpoint and the spindle assembly checkpoint share an architectural logic: each holds the cycle at a boundary until the condition the boundary guards has been verified.

At **G2/M**, the activator is cyclin B–CDK1. During G2, CDK1 is held inactive by inhibitory phosphorylations placed by the kinases Wee1 and Myt1. Activation requires the CDC25 phosphatases to remove those phosphorylations. DNA damage or incomplete replication activates the sensor kinases ATM and ATR, which activate their effectors Chk1 and Chk2, which phosphorylate and inactivate CDC25. With CDC25 inactive, CDK1 stays off and the cell pauses in G2. If repair completes, ATM/ATR activity falls, CDC25 is restored, CDK1 fires, and the cell enters mitosis. If damage is irreparable, the sustained p53 activity triggered by ATM/ATR can route the cell into apoptosis instead.

The **spindle assembly checkpoint** operates within mitosis at the metaphase-to-anaphase transition. Every chromosome must be attached to microtubule spindle fibers from *both* poles before the cell is permitted to pull the chromosomes apart. An unattached kinetochore — the protein structure on a chromosome where spindle fibers attach — generates an active inhibitory signal through Mad and Bub protein complexes. That signal inhibits the APC/C ubiquitin ligase, keeping securin intact. Securin holds separase, the protease that cleaves the cohesin holding sister chromatids together, in an inactive state. As long as any kinetochore is unattached, APC/C stays inhibited, separase stays inactive, and chromatids cannot separate. The moment the last kinetochore attaches, the inhibitory signal stops, APC/C activates, securin is degraded, separase cleaves cohesin, and the chromosomes separate in seconds.

The spindle checkpoint is the source of the pause in the opening time-lapse. The cell was not hesitating; it was waiting for a molecular verification to complete before a step that, once taken, cannot be reversed. Weakened spindle checkpoint function — through mutation or overexpression of checkpoint-inhibiting proteins — allows premature chromosome separation, producing cells with extra or missing chromosomes. That aneuploidy is a feature of many cancer cells and a consequence of checkpoint failure.

![Two parallel checkpoint cascades side by side: the G2/M cascade (DNA damage → ATM/ATR → Chk1/Chk2 → CDC25 inactivated → cyclin B–CDK1 held off) and the spindle-assembly cascade (unattached kinetochore → Mad/Bub → APC/C blocked → securin intact → separase inactive), each ending in a held transition.](images/11-cell-cycle-control-and-cancer-the-cycle-and-its-checkpoints-fig-03.png)
*Figure 11.3 — G2/M and spindle-assembly checkpoint cascades*

---

A cell sustains DNA damage. At which checkpoint should it be halted, and by which mechanism?

The first-guess answer is G2/M — that is the checkpoint "just before mitosis," and stopping there before division seems sensible. It is true that the G2/M checkpoint will halt a cell with unrepaired breaks, via ATM/ATR → Chk1/Chk2 → CDC25 inactivation → CDK1 off. But stopping only at G2/M is too late if the damage occurred in G1.

A cell that enters S phase with damaged template DNA will replicate the damage into both daughter strands. A transient lesion — a single-strand break, an adduct — becomes a permanent double-strand mutation embedded in both copies of the chromosome. The G2/M checkpoint catches the cell after the damage has been copied. The G1/S checkpoint catches it before.

At G1/S, DNA damage activates ATM/ATR, which stabilize p53. p53 transcribes *CDKN1A*, producing p21, which inhibits cyclin E–CDK2. Rb stays hypophosphorylated. E2F stays bound. The cell cannot enter S phase until repair completes (NCBI Bookshelf, *The Cell Cycle*). The G1/S arrest is the more valuable one for preventing mutation because it acts before replication. The G2/M checkpoint is a second line — it catches damage that arose during S phase, or that the G1/S checkpoint missed.

The limits of this picture follow directly from the cancer context. A cell that has lost p53 loses the p21-mediated reinforcement of G1/S arrest. The checkpoint is weakened, not abolished — some p53-independent p21 regulation exists — but the primary sensor-to-brake pathway is gone. Cells with p53 loss tend to arrive at G2/M with more unrepaired damage. And because the G2/M checkpoint is largely Chk1/Chk2-driven and not p53-dependent, p53-null cancer cells come to *depend* on it more heavily than normal cells do. That differential dependency is the therapeutic logic behind Chk1/Chk2 inhibitors in p53-null cancers: the cancer cell has placed all its checkpoint eggs in one basket, and taking that basket away kills it while leaving p53-intact cells with a backup.

---

The cell cycle control system is among the most deeply conserved molecular machinery in eukaryotic biology. The core cyclin–CDK logic is recognizably the same from yeast to humans, an evolutionary stability that reflects how little room there is for error in a process this consequential. Cancer does not invent new biology to break the cycle; it systematically dismantles the same controls — Rb, p16, cyclin D amplification, CDK4 mutation, p53 — by many mutational routes, all arriving at the same outcome: S-phase entry regardless of conditions, checkpoint failure that lets damaged or improperly replicated DNA proceed, and the accumulation of the chromosomal chaos that aggressive cancers display.

Understanding the control system is not background knowledge before the interesting cancer biology. It *is* the cancer biology. The restriction point is broken in almost every tumor. The spindle checkpoint is weakened in most aneuploid cancers. The G1/S checkpoint is bypassed wherever p53 or Rb is lost. The therapeutic targets that have emerged from this framework — CDK4/6 inhibitors in hormone-receptor-positive breast cancer, checkpoint kinase inhibitors in p53-null tumors — follow directly from understanding what the controls are and where the cancer has broken them.

---

## Exercises

**Warm-up**

1. *[Recall — moderate]* In one sentence each, state the condition verified by the G1/S checkpoint, the G2/M checkpoint, and the spindle assembly checkpoint. For each, name one molecular component that carries the "stop" signal when the condition is not met.
*What this tests: whether you understand checkpoints as specific condition-verifying mechanisms rather than generic "pauses" — the molecular component forces a mechanistic rather than descriptive answer.*

2. *[Recall — moderate]* Explain why cyclin D is a signal integrator rather than a clock, using the consequence of growth-factor withdrawal before versus after the restriction point as your evidence. Your answer should name what happens to cyclin D levels in each scenario and what that implies for Rb phosphorylation.
*What this tests: the signal-integration logic of cyclin D — whether you understand that the cycle stalls because a signal was lost, not because a timer stopped.*

3. *[Recall — moderate]* Describe the positive-feedback mechanism in the Rb–E2F switch and explain in two sentences why this feedback makes the restriction point a bistable commitment rather than a gradual threshold. Name both cyclin–CDK pairs involved and the order in which they act.
*What this tests: mechanistic understanding of bistability — the feedback loop is the design principle, not a detail.*

**Application**

4. *[Apply — moderate-hard]* Growth factors are withdrawn from two genetically identical cells — one just before the restriction point, one just after. Predict what each cell does over the next several hours and explain the difference specifically in terms of cyclin D levels, Rb phosphorylation state, and E2F activity. Your answer should explain why the same environmental event (growth-factor removal) has different consequences depending on the cell's position in the cycle.
*What this tests: applying the bistable switch logic to a before/after comparison — the restriction point as a one-way gate, not a dial.*

5. *[Apply — moderate-hard]* A tumor genome shows that *CDKN2A* — the locus encoding both p16/INK4a and ARF/p14ARF — has been homozygously deleted. Draw a four-box mechanism map: normal control → cancer-relevant alteration → cellular phenotype → one therapeutic or diagnostic consequence. Label each arrow with the mechanism connecting the boxes. Then write one sentence explaining why this single deletion disables two tumor-suppressive pathways simultaneously.
*What this tests: applying the Rb pathway alteration to a specific locus; understanding why CDKN2A deletion is so common in cancer.*

6. *[Apply — hard]* A cell with functional p53 sustains DNA damage in G1. Trace the molecular events that arrest the cell at G1/S, naming every protein in the pathway from the initial damage sensor to the CDK whose inhibition prevents S-phase entry. Then explain what happens to this pathway in a p53-null cell, and predict where the p53-null cell's arrest — if it arrests at all — will occur instead.
*What this tests: tracing the full checkpoint signal cascade; understanding why p53 loss preferentially impairs G1/S arrest and shifts checkpoint dependency to G2/M.*

**Synthesis**

7. *[Synthesis — hard]* The same cellular outcome — constitutive S-phase entry regardless of growth signals — can be produced by loss of Rb, amplification of cyclin D, amplification of CDK4, or deletion of p16/INK4a. For each alteration, name the component it targets in the Rb–E2F pathway and the step at which the pathway is short-circuited. Then explain why a CDK4/6 inhibitor (such as palbociclib) would be expected to work in a cyclin D-amplified tumor but not in an Rb-deleted tumor, using the mechanism map to justify your prediction.
*What this tests: mapping multiple alterations to a single pathway; predicting therapeutic response based on where in the pathway the brake is broken.*

8. *[Synthesis — hard]* The spindle assembly checkpoint holds a cell at metaphase until every kinetochore is attached to spindle fibers from both poles. Explain the full molecular mechanism: what the unattached kinetochore generates, how that signal prevents chromosome separation, and what releases the hold. Then explain how a weakened (but not absent) spindle checkpoint would produce aneuploidy, and name the cancer-relevant consequence of that aneuploidy.
*What this tests: mechanistic understanding of the SAC beyond the opening metaphase pause; connecting checkpoint weakness to chromosomal instability in cancer.*

**Challenge**

9. *[Challenge — very hard]* The "Still Puzzling" section notes that the bistability of the restriction point is well supported in principle but that how cleanly individual cells in real tissues respect the sharp threshold — versus showing graded or noisy behavior — is still being measured with single-cell tools. Design a single-cell experiment that would determine whether the restriction point is truly bistable (sharp, switch-like commitment) or graded (cells show a distribution of commitment thresholds) in a specific primary human cell type. Specify the reporter constructs, imaging approach, perturbation strategy, and the result pattern that would distinguish bistability from a graded response. Then explain why the answer matters for understanding how oncogenic cyclin D amplification initiates tumorigenesis — specifically whether a small increase in cyclin D activity could gradually nudge many cells past threshold, or would need to exceed a sharp cliff.
*What this tests: translating a conceptual question about switch behavior into an experimental design; connecting the biophysics of the restriction point to the biology of oncogene-driven cell-cycle deregulation.*

---

## What Would Change My Mind

The central claim of this chapter is that the cell cycle is a conditional control system in which cyclin–CDK complexes drive progression and checkpoints — centered on the bistable Rb–E2F switch — gate commitment so that division occurs only under appropriate conditions. The strongest support is the deep evolutionary conservation of the cyclin–CDK machinery from yeast to humans and the consistent behavior of the Rb–E2F switch across cell types. This claim would need revision if careful single-cell measurements showed that the restriction point is not in fact a sharp, bistable commitment — that cells routinely ramp gradually into S phase and freely reverse after Rb hyperphosphorylation under normal conditions — or if a major proliferative tissue were shown to drive ordered division without cyclin–CDK control at all. Either finding would mean the "switch and checkpoint" account is, at best, one mechanism among several rather than the central logic of the cycle.

## Still Puzzling

- **How sharp is the switch, really?** The bistability of the restriction point is well supported in principle, but how cleanly individual cells in a real tissue respect the threshold — versus showing graded or noisy behavior — is still being measured with single-cell tools.
- **Redundancy among CDKs.** Genetic experiments show some CDKs can substitute for others under certain conditions. How much of the textbook "one cyclin–CDK pair per transition" picture is strict requirement versus convenient simplification remains an active question.
- **Where do non-genetic states fit?** Quiescence (G0), senescence, and reversible drug-tolerant states all involve the cycle machinery but are not simple on/off mutations. How these phenotypic states interact with the checkpoints — and whether they are stable or plastic — connects directly to the next chapter, where we ask how cancers break each of these controls and how those breaks become therapeutic targets.

## References

- NCBI Bookshelf. *The Cell Cycle and Programmed Cell Death.* https://www.ncbi.nlm.nih.gov/books/NBK21056/
- NCBI Bookshelf. *Molecular Biology of the Cell.* https://www.ncbi.nlm.nih.gov/sites/books/n/mboc4/
- International Journal of Molecular Sciences (2021). Cyclin-Dependent Kinases and Their Regulation. https://www.mdpi.com/1422-0067/22/6/2935
- NCI. *What Is Cancer?* https://www.cancer.gov/about-cancer/understanding/what-is-cancer
- Hanahan, D. (2022). Hallmarks of Cancer: New Dimensions. *Cancer Discovery*, 12(1), 31–46.

---

## Prompts

### Figure 11.1 — The cell cycle and its three checkpoints
Build a closed-loop cycle diagram: four arc segments around a circle for G1 (~11 h), S (~8 h), G2 (~4 h), and M (~1 h), traversed clockwise with arrowheads showing direction of progression. Size each arc roughly proportional to its hours if feasible, otherwise label hours directly. Place three checkpoint markers at their boundaries: G1/S, G2/M, and spindle-assembly (within M), each a distinct node on the ring with a one-line condition verified. Draw a G0 quiescence node as a branch exiting from G1 with a bidirectional arrow (exit/re-entry). Color G1 sky-blue (anchor phase), the three checkpoint markers green (active control/positive verification), G2 a transitional tone; remaining elements neutral. No quantitative axes. Deliverable: single standalone HTML file, inline CSS, D3 v7 pinned CDN, Okabe-Ito colorblind-safe palette via CSS variables.

### Figure 11.2 — The Rb–E2F switch
Build a left-to-right signal-circuit flowchart of seven sequential nodes with single forward arrows, plus one explicit feedback edge curving backward. Order: mitogen signal → Ras–MAPK relay → cyclin D–CDK4/6 → Rb partly phosphorylated (brake) → E2F released, transcribes cyclin E → cyclin E–CDK2 → S-phase genes on, committed. Draw a labeled "positive feedback" arrow from the cyclin E–CDK2 node back onto the Rb-phosphorylation node to show the loop that flips the switch. Color the mitogen input sky-blue (anchor), the Ras–MAPK node blue (dominant driver), the partly-phosphorylated-Rb brake node vermillion (negative/blocking), and the cyclin E–CDK2 feedback node green (positive/active commitment). Add a caption noting the loop converts a reversible state into committed S-phase entry. No axes. Deliverable: single standalone HTML file, inline CSS, D3 v7 pinned CDN, Okabe-Ito colorblind-safe palette via CSS variables.

### Figure 11.3 — G2/M and spindle-assembly checkpoint cascades
Build a two-panel comparison, left and right, each a top-to-bottom vertical cascade of five aligned rows so the two cascades read in parallel. Shared row axis: sensor → relay → blocked target → held outcome. Left panel "G2/M checkpoint": DNA damage → ATM/ATR sensor kinase → Chk1/Chk2 effector kinase → CDC25 phosphatase inactivated → cyclin B–CDK1 held off. Right panel "Spindle-assembly checkpoint": unattached kinetochore → Mad/Bub inhibitory signal → APC/C ligase blocked → securin left intact → separase inactive, chromatids joined. Align the two panels row-for-row. Color the top sensor row sky-blue (anchor), the relay/kinase row blue (dominant), the blocked-ligase/kinase row green (active block engaged), and the bottom held-transition row vermillion (negative/held). No numeric data. Deliverable: single standalone HTML file, inline CSS, D3 v7 pinned CDN, Okabe-Ito colorblind-safe palette via CSS variables.

### Figure 11.4 — Four routes break one switch
Build a node-edge convergence diagram: four lesion nodes on the left — p16/INK4a deletion, cyclin D amplification, CDK4 amplification, Rb loss — feeding toward a shared core. The first three converge via arrows onto a cyclin D–CDK4/6 node, which arrows into a constitutive-E2F node; the Rb-loss node arrows directly into the constitutive-E2F node (bypassing the kinase). The E2F node then arrows to a terminal node: unconditional S-phase entry. Lay lesions as a left column, the kinase and E2F nodes in the middle, the outcome at right. Color the four lesion nodes neutral gray (different origins), the cyclin D–CDK4/6 node blue (dominant hub), the E2F node a transitional tone, and the S-phase-entry outcome vermillion (negative endpoint). Arrowheads on every edge. No axes. Deliverable: single standalone HTML file, inline CSS, D3 v7 pinned CDN, Okabe-Ito colorblind-safe palette via CSS variables.
