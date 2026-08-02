# Chapter 14 — Apoptosis in Cancer: Evasion and Restoration
*The Cells Were Already Trying to Die.*

A 68-year-old man has chronic lymphocytic leukemia that has relapsed after several prior therapies. His leukemic B cells are not dividing especially fast — that is not the problem. The problem is that they will not die. They have accumulated to the point of crowding out his normal blood cells, and conventional cytotoxic drugs, which kill by inflicting DNA damage, have stopped working: each relapse has selected for cells better at surviving damage.

He is started on a single oral drug. Within weeks his leukemic count plummets and his bone marrow clears to the point where minimal residual disease is undetectable — a depth of response that none of his prior therapies had produced. The drug did not damage his cells. It released a brake those cells had been holding on their own death program, and they died by their own hand.

The drug is venetoclax, and the case forces a conceptual shift. For most of oncology's history, the strategy was to inflict enough damage to kill the tumor before killing the patient — a narrow therapeutic window, because the same DNA damage that kills cancer cells kills bone marrow, gut, and hair follicles. The venetoclax logic is different. Cancer cells already carry the full apoptotic machinery; they have simply suppressed it. Restore the suppression's release, and the cells die selectively — because normal cells were not suppressing apoptosis in the first place.

---

The most important misconception in this chapter to correct first: apoptosis evasion is not the *absence* of a death signal. It is an active defense against a death signal that is already present.

Cancer cells accumulate DNA damage, overactive oncogenes, and detachment from their normal tissue — each of these is a stimulus that should trigger the intrinsic apoptotic pathway. The signals are there. The cells survive not because nothing is pushing them toward death, but because they have acquired mechanisms that block the push from reaching the mitochondria. Evasion is an adaptation under selection, an arms race the cancer cell is winning. The opening patient's leukemic cells were straining against their own death program the entire time. Venetoclax worked not by adding a new death signal but by removing one defense, and the pre-loaded pressure did the rest.

Cancers evade apoptosis through a small, recurrent set of strategies (NCBI Bookshelf, NBK9963):

**Overexpression of anti-apoptotic BCL-2 family proteins.** The canonical case is BCL-2 itself, discovered at the t(14;18) translocation of follicular lymphoma, which fuses the *BCL2* gene to the immunoglobulin heavy-chain enhancer and drives extreme BCL-2 expression. The lymphoma cells are not proliferating unusually fast — they simply refuse to die. BCL-XL and MCL-1 overexpression are common across many solid and hematologic cancers, and MCL-1 is often the factor that limits the response when BCL-2 is inhibited.

**Loss of pro-apoptotic proteins.** Loss or mutation of BAX, BAK, or the BH3-only sensors — PUMA, NOXA, BIM — reduces the cell's total apoptotic capacity. BAX is mutated in some microsatellite-instability-high cancers. A cell that has lost its effectors cannot commit to MOMP regardless of upstream signaling; removing an anti-apoptotic guardian from such a cell does nothing.

**Mutation of *TP53*.** Present in roughly half of all cancers, this removes the upstream transcriptional sensor that links DNA damage to expression of pro-apoptotic genes including PUMA and NOXA (Chapter 13). The death signal arrives at the sensor but is not transmitted downstream.

**Overexpression of Inhibitor of Apoptosis Proteins.** The IAPs — XIAP, c-IAP1/2, and survivin — inhibit caspases directly, placing a brake at the execution stage rather than upstream of MOMP. Survivin is overexpressed in most cancers and nearly absent from normal adult tissue, making it one of the cleaner cancer-specific targets in this class.

**Downregulation of death receptors or caspase-8.** Loss of FAS, DR4, and DR5 blocks the extrinsic pathway; loss of caspase-8, sometimes through promoter hypermethylation rather than mutation, blocks the signal downstream of the receptors. Some neuroblastomas silence caspase-8 by methylation, making them resistant to death-receptor agonists.

**Active survival signaling.** PI3K–AKT phosphorylates and inactivates BAD, raises MCL-1 levels, and suppresses p53. NF-κB transcriptionally raises BCL-XL and IAPs. MAPK destabilizes BIM. Survival is the net output of these converging pathways, and oncogene activation — constitutive RAS, hyperactive PI3K — feeds them all.

These strategies are not mutually exclusive. A single cancer cell may overexpress BCL-2, lose BAX, carry mutant *TP53*, and run hyperactive PI3K–AKT simultaneously — layered, redundant defenses built up through years of selection. That redundancy explains why single-target apoptosis-restoring drugs sometimes fail and why combinations are needed: breaching one defense leaves five others intact.

![Annotated mechanism map of the intrinsic death circuit (p53 → BCL-2 balance → mitochondrion → apoptosome → caspases → death) with five sabotage points called out: TP53 mutation at the sensor, BAX/BAK loss at the effectors, guardian overexpression, IAPs at the caspase node, and PI3K-AKT/NF-κB survival signaling pressing the balance.](images/14-apoptosis-in-cancer-evasion-and-restoration-fig-02.png)
*Figure 14.2 — Apoptosis evasion map: where each strategy intervenes*

<!-- → [DIAGRAM: apoptosis evasion map — intrinsic pathway circuit from the previous chapter, with each evasion strategy marked at its point of intervention: anti-apoptotic BCL-2 family at the guardian level, BAX/BAK loss at the effector level, TP53 mutation at the sensor level, IAPs at the caspase level, survival signaling inputs at the BH3-only level] -->

---

A **BH3 mimetic** is a small molecule shaped to imitate the BH3 helix — the short alpha-helical domain that pro-apoptotic proteins use to bind anti-apoptotic guardians. It occupies the hydrophobic groove of an anti-apoptotic BCL-2 family member, displacing the pro-apoptotic proteins that were bound there, and freeing BAX and BAK to oligomerize and permeabilize the outer mitochondrial membrane (Letai, 2016).

![Competitive-displacement sequence: the BCL-2 groove holds a BH3-only protein (BIM) until venetoclax inserts into the groove, ejecting the BH3-only protein, freeing BAX and BAK to oligomerize, and producing a membrane pore that releases cytochrome c.](images/14-apoptosis-in-cancer-evasion-and-restoration-fig-01.png)
*Figure 14.1 — BH3 mimetic releasing effectors from the guardian*

The conceptual distinction that matters: a BH3 mimetic does not cause DNA damage. It introduces no new lesions, activates no damage sensors, and does not rely on p53. It simply removes a brake. A cancer cell that was straining against death — that had loaded its mitochondria with pro-apoptotic pressure and was surviving *only* because one guardian was sequestering the effectors — will die rapidly when that guardian is blocked. A normal cell that was not leaning on that guardian to stay alive is largely unaffected.

This selectivity is conditional, not universal. Whether a BH3 mimetic kills a specific cell depends on **apoptotic priming** — the degree to which the cell is poised at the threshold of MOMP, held back by a specific guardian. A cell that is highly primed and BCL-2-dependent will die quickly when BCL-2 is inhibited. A cell whose survival is distributed across BCL-2, MCL-1, BCL-XL, and multiple survival signaling inputs will tolerate BCL-2 inhibition because the other props remain in place. CLL cells are among the most BCL-2-dependent of any cancer type, which is why venetoclax works so well there. Most solid tumors depend on multiple guardians in parallel, which is why a single BH3 mimetic rarely produces the same depth of response.

The concept of priming can be measured. **BH3 profiling** — exposing isolated mitochondria to peptides corresponding to different BH3 domains and measuring cytochrome c release — quantifies how close a cell is to the threshold and which guardian is doing the most protective work. It was developed by Anthony Letai's group and has been used to predict sensitivity to specific BH3 mimetics prospectively in clinical samples (Letai, 2016). The idea that apoptotic sensitivity is a measurable property of the cell, predictable before treatment, is one of the more important advances in making this class of drugs rational rather than empirical.

---

The venetoclax story is worth tracing in detail because it contains a real dead end that the field had to solve, and the solution reveals a principle that governs every BH3 mimetic program.

Structural biology in the 1990s showed that anti-apoptotic guardians have a hydrophobic groove — the BH3-binding pocket — and that a small molecule occupying that groove would mimic a BH3 protein and disrupt the protective complex. **ABT-737**, developed at Abbott Laboratories, proved this in 2005: it bound BCL-2, BCL-XL, and BCL-W with nanomolar affinity and killed BCL-2-dependent tumors in animal models. Its orally bioavailable successor, **navitoclax (ABT-263)**, went into clinical trials in CLL and small-cell lung cancer and showed activity.

Then came the problem. Navitoclax inhibits BCL-XL as well as BCL-2, and **platelets require BCL-XL for survival**. Inhibiting BCL-XL triggered platelet apoptosis, and the clinical consequence was severe dose-limiting thrombocytopenia. The drug was biologically elegant — it did exactly what it was designed to do — and the platelet toxicity was not an off-target side effect. It was on-target toxicity in a normal cell that happened to share the dependency. The same molecular mechanism that killed the cancer cells killed the platelets.

The therapeutic window was too narrow. The fix was structural selectivity. **Venetoclax (ABT-199)** was designed by structure-guided medicinal chemistry to retain high-affinity BCL-2 binding while avoiding the BCL-XL pocket — preserving platelet survival (Letai, 2016). The drug binds BCL-2 with a Ki below 0.1 nM; its affinity for BCL-XL is more than 500-fold weaker. Platelets survive at therapeutic doses. FDA approval came in 2016 for relapsed/refractory CLL with 17p deletion.

![Two-condition comparison: navitoclax inhibits both BCL-2 and BCL-XL, killing the tumor cell but also the BCL-XL-dependent platelet (on-target toxicity), whereas selective venetoclax inhibits BCL-2 only, killing the tumor cell while sparing the platelet and opening the therapeutic window.](images/14-apoptosis-in-cancer-evasion-and-restoration-fig-03.png)
*Figure 14.3 — Navitoclax versus venetoclax: the platelet window*

In CLL, single-agent venetoclax produces response rates exceeding 70 percent in heavily pretreated patients, with a substantial fraction reaching undetectable minimal residual disease — a depth of response unprecedented in that setting `[verify — current trial response figures]`. Combined with anti-CD20 antibodies, in the MURANO and CLL14 regimens, responses are deeper and more durable `[verify — combination trial data]`. In AML, venetoclax combined with a hypomethylating agent (azacitidine or decitabine) became standard of care for elderly patients ineligible for intensive chemotherapy, roughly doubling response rates over the hypomethylating agent alone (VIALE-A trial) `[verify]`.

The decisive variable was not potency against the tumor. It was identifying which normal cell shared the dependency and engineering around it. That principle governs every BH3 mimetic program: before the molecule is designed, ask which normal tissues express the targeted guardian at survival-relevant levels, and confirm that therapeutic concentrations will spare them.

---

BCL-2 is one brake. The same logic of releasing a pre-loaded death program applies to other brakes, and the resulting drug classes target different points in the death-signaling circuit.

**TRAIL agonists** push the extrinsic pathway by engaging DR4 and DR5, the death receptors on the cell surface. Recombinant TRAIL showed striking preclinical selectivity — cancer cells died readily; normal cells were mostly spared. The selectivity has a plausible mechanistic basis: cancer cells frequently downregulate FLIP, a caspase-8 inhibitor, and upregulate DR4/DR5, making them more sensitive to death-receptor signaling. First-generation TRAIL agonists (recombinant TRAIL protein and monoclonal antibodies against DR4 or DR5) entered clinical trials in the 2000s and largely disappointed. Two specific problems: recombinant TRAIL has a short half-life in circulation, and the monoclonal antibodies fail to induce the receptor clustering that is required for strong caspase-8 activation — agonist antibodies need to crosslink multiple receptors to drive efficient assembly of the death-inducing signaling complex, and standard IgG antibodies do not do this as well as the natural ligand. Second-generation multivalent TRAIL receptor agonists, designed to enforce receptor clustering, are in early trials. The biology remains sound; the pharmacology has been the obstacle.

**IAP antagonists** mimic SMAC/DIABLO, the endogenous mitochondrial protein that is released during MOMP and relieves IAP-mediated caspase inhibition. Synthetic SMAC mimetics — small molecules matching the IAP-binding tetrapeptide of SMAC — include birinapant and LCL161. They work partly by directly relieving caspase inhibition and partly by triggering auto-ubiquitination and degradation of c-IAP1/2, which then allows TNF-receptor signaling to activate caspase-8. Their clinical activity has been modest as single agents; combinations with death-receptor agonists or with venetoclax are more promising. MCL-1 is required for cardiomyocyte survival, making MCL-1 inhibitors potentially cardiotoxic — whether a viable therapeutic window exists for MCL-1 inhibitors in patients is a genuinely open question.

**MDM2 inhibitors** are conceptually distinct from the other classes. Rather than directly releasing a pro-apoptotic protein from a guardian, they restore p53 activity in cancers where p53 is wild-type but suppressed by MDM2 overexpression. MDM2 normally targets p53 for proteasomal degradation; MDM2 amplification, present in 5–10 percent of cancers and especially common in well-differentiated liposarcoma, keeps p53 levels low despite an intact p53 gene. MDM2 inhibitors — nutlins and their successors (idasanutlin, navtemadlin) — block the MDM2–p53 interaction, stabilize p53, and activate its transcriptional program including BAX, PUMA, and NOXA induction. They are effective only in cancers with wild-type *TP53*; a cancer that has already mutated p53 has nothing to restore. In MDM2-amplified liposarcoma, responses have been documented but are not universal, and the dose-limiting toxicity is gastrointestinal — because intestinal stem cells also depend on the MDM2–p53 axis for normal homeostasis.

<!-- → [TABLE: apoptosis-restoring drug classes — columns: class, example agents, molecular target, mechanism of selectivity, cancer types showing activity, primary resistance mechanism] -->

---

The platelet problem with navitoclax was not a failure of the BH3 mimetic concept. It was the concept working exactly as intended — BCL-XL inhibition kills BCL-XL-dependent cells, and platelets are BCL-XL-dependent — in a normal cell type that was not supposed to be the target. The design answer was to narrow the selectivity until the drug killed the cancer cells it was aimed at and spared the platelets it needed to avoid.

That is the recurring logic across the entire class. The cancer cell is already dying — it is primed, loaded, and held back by one specific guardian. The drug's job is to identify that guardian and release it without releasing the same constraint in a normal cell that needs the guardian for survival. The therapeutic window is not set by the drug's potency; it is set by the difference in dependency between the cancer cell and the normal cell at risk.

Venetoclax works in BCL-2-dependent CLL because leukemic B cells depend on BCL-2 and platelets do not. It works less well in multiple myeloma, except in the t(11;14) subgroup that is BCL-2-dependent; outside that subgroup, the myeloma cells depend primarily on MCL-1, and venetoclax does not touch MCL-1. It fails when resistance mutations block binding at the G101V site, or when the cancer switches its dependency to BCL-XL or MCL-1. In each case, the boundary is the dependency — the drug works exactly as far as the concentrated dependency extends, and no further.

The strategy of restoring death rather than inflicting damage is the conceptual advance. The BCL-2 inhibitors are its most mature clinical expression. The TRAIL agonists, IAP antagonists, and MDM2 inhibitors are attempts to apply the same logic to other brakes. None has yet produced the same transformation as venetoclax in CLL, which reflects the difference between a cancer with one dominant, measurable dependency and a cancer whose survival is more broadly distributed. The field is working on how to identify, map, and exploit the dependencies in the harder cases.

---

## Exercises

**Warm-up**

1. *[Recall — moderate]* Explain in three sentences why apoptosis evasion in cancer is an active defense rather than a passive absence, and name three molecular strategies a cancer cell uses to maintain that defense. Your answer should make clear why the death pressure in cancer cells is often *higher* than in normal cells, not lower.
*What this tests: the conceptual reorientation from "cells fail to die" to "cells are fighting actively against death" — the framing that makes BH3 mimetics logical.*

2. *[Recall — moderate]* Define apoptotic priming. Explain why a highly primed, BCL-2-dependent cell is more vulnerable to venetoclax than a cell that expresses BCL-2 but distributes its survival across MCL-1 and BCL-XL as well.
*What this tests: the dependency concept — presence of a target versus dependence on a target, which is the boundary condition for the whole drug class.*

3. *[Recall — moderate]* Describe in two sentences what BH3 profiling measures and why it is a more direct predictor of BH3 mimetic sensitivity than sequencing the cancer genome.
*What this tests: functional assay logic — why measuring the output of the system (mitochondrial priming) predicts drug response better than cataloging its components.*

**Application**

4. *[Apply — moderate-hard]* A patient with CLL responds to venetoclax, then relapses. Resequencing identifies upregulated MCL-1 with no mutation in *BCL2*. Explain mechanistically why MCL-1 upregulation confers resistance to a BCL-2-selective drug — trace the path from MCL-1 upregulation to restored survival despite BCL-2 inhibition. Then name the class of drug you would add to overcome this resistance and explain why it would work in combination but likely not as a single agent.
*What this tests: applying the guardian-switching resistance mechanism to a clinical scenario; understanding why MCL-1 confers resistance and why combination therapy is mechanistically required.*

5. *[Apply — moderate-hard]* Build a three-column decision table for targeting BCL-2, BCL-XL, and MCL-1. For each column: name a BH3 mimetic or inhibitor class, the cancer types known to depend on it, and the normal cell type whose dependency creates the dose-limiting toxicity. Then write one sentence recommending which guardian you would prioritize in a new solid-tumor drug program and justify it using the therapeutic window logic.
*What this tests: systematic application of the normal-cell dependency principle across three guardian targets; translating the navitoclax lesson into a drug-design decision.*

6. *[Apply — hard]* TRAIL agonists showed striking preclinical selectivity — cancer cells died, normal cells largely survived — but first-generation clinical candidates were disappointing. Name two specific pharmacological reasons for the gap between preclinical and clinical results, explain the molecular mechanism underlying each, and describe what a second-generation design would need to fix to close that gap.
*What this tests: applying the receptor-clustering and ligand half-life problems to the TRAIL case; distinguishing elegant biology from translatable pharmacology.*

**Synthesis**

7. *[Synthesis — hard]* A cancer cell simultaneously overexpresses BCL-2, has lost BAX expression, and carries mutant *TP53*. Predict, with mechanistic justification, whether venetoclax would be expected to kill this cell. Then propose a combination strategy that could restore apoptotic sensitivity, naming each component, its target, and why the combination is required rather than either agent alone.
*What this tests: integrating multiple evasion mechanisms to predict the net vulnerability; designing combinations from mechanism rather than empirical trial.*

8. *[Synthesis — hard]* MDM2 inhibitors restore p53 activity in MDM2-amplified, *TP53* wild-type cancers. Compare this mechanism of apoptosis restoration to venetoclax's mechanism in three dimensions: (1) which step in the death pathway each drug restores; (2) the biomarker required to predict which patients will respond; (3) the normal-cell toxicity that limits the therapeutic window. Then explain why a combination of MDM2 inhibitor and venetoclax is mechanistically rational in MDM2-amplified, BCL-2-dependent CLL, and identify the interaction that would need to be monitored for overlapping toxicity.
*What this tests: comparative analysis of two distinct apoptosis-restoring strategies; integrating biomarker, mechanism, and toxicity reasoning across drug classes.*

**Challenge**

9. *[Challenge — very hard]* The "Still Puzzling" section asks whether MCL-1 can ever be safely drugged. MCL-1 is the most common limiting dependency in BH3 mimetic resistance, but it is also required by cardiomyocytes and hepatocytes. Design a preclinical and early clinical program — specifying the model systems, biomarkers, dosing strategy, and safety monitoring plan — that would determine whether a viable therapeutic window exists for MCL-1 inhibition in a specific cancer type. Your program should explain how you would distinguish on-target cardiac toxicity from off-target effects, how BH3 profiling of cardiomyocytes versus tumor cells would inform your dose selection, and what early clinical signal — short of a full phase III trial — would give you enough confidence to advance or stop. Identify the single experiment that would most change your confidence in the program's viability.
*What this tests: translating a mechanistic concern into a full drug-development risk-management strategy; applying the normal-cell dependency principle to a live clinical uncertainty.*

---

## What Would Change My Mind

The central claim is that selectively releasing a cancer cell's suppressed death program is a clinically powerful, mechanistically distinct strategy from inflicting damage. The finding that would most force a revision: a rigorous demonstration that venetoclax's clinical benefit in BCL-2-dependent cancers is actually driven by an off-target or DNA-damage-like mechanism rather than by on-target BCL-2 displacement — for instance, if BCL-2-mutant cells that cannot bind the drug still died at the same rate, or if biomarkers of apoptotic priming failed entirely to predict response in adequately powered cohorts. That would collapse the "restore death, selectively" framing back into ordinary cytotoxicity. The G101V resistance mutation, which maps precisely to the drug-binding groove and abolishes response, currently argues strongly for the on-target mechanism — but a clean dissociation between target engagement and killing would be the disconfirming test.

## Still Puzzling

- **Why does TRAIL biology fail to translate?** The preclinical selectivity of TRAIL for cancer cells is striking, yet first-generation agonists were disappointing. Whether newer multivalent constructs close the gap, or whether the extrinsic pathway is simply too easily bypassed in vivo, is unresolved.
- **Can MCL-1 ever be safely drugged?** MCL-1 is the most common limiting dependency, but it is also required by cardiomyocytes and hepatocytes, making selective inhibition treacherous. Whether a viable therapeutic window exists is an open clinical question.
- **Is mutant-p53 reactivation achievable?** Restoring DNA-binding function to a misfolded mutant p53 protein is a far harder problem than raising wild-type p53 levels, and the clinical record so far is mixed. This connects to the metabolism chapters, where p53's non-canonical roles reappear.

## References

- NCI Drug Dictionary. *BH3 mimetic ABT-737.* https://www.cancer.gov/publications/dictionaries/cancer-drug/def/bh3-mimetic-abt-737
- Letai, A. (2016). Mitochondrial apoptosis and BH3 mimetics. PMC5133681. https://pmc.ncbi.nlm.nih.gov/articles/PMC5133681/
- NCI. *The Genetics of Cancer.* https://www.cancer.gov/about-cancer/causes-prevention/genetics
- Hino, O., et al. (2017). The two-hit hypothesis. *Cancer Science.* https://onlinelibrary.wiley.com/doi/10.1111/cas.13116
- NCBI Bookshelf. *The Development and Causes of Cancer.* NBK9963. https://www.ncbi.nlm.nih.gov/books/NBK9963/

---

## Prompts

### Figure 14.1 — BH3 mimetic releasing effectors from the guardian
Build a left-to-right flowchart of five sequential stages showing competitive occupancy of the BCL-2 groove. Stages: (1) BCL-2 groove holds a BH3-only protein (BIM); (2) venetoclax inserts into the groove [edge label "drug enters"]; (3) BH3-only protein ejected [edge label "displace"]; (4) BAX/BAK freed, oligomerize; (5) membrane pore releases cytochrome c [edge label "MOMP"]. Single horizontal track, equal-width nodes, activating arrows between stages. Color the occupied-groove start node vermillion (guardian blocking death), the venetoclax node blue (dominant intervening drug), the freed-effector node green (positive/active), and the final pore node sky-blue (anchor outcome). Caption: one shape leaves the groove as another takes its place, and the displaced shape triggers pore formation. No numeric data, no axes. Deliverable: single standalone HTML file, inline CSS, D3 v7 pinned CDN, Okabe-Ito colorblind-safe palette via CSS variables.

### Figure 14.2 — Apoptosis evasion map: where each strategy intervenes
Build an annotated callout diagram: a central horizontal spine representing the intrinsic death circuit, drawn as labeled nodes in sequence — p53 → BCL-2 balance → mitochondrion → apoptosome → caspases → death. Around this spine, place five callout boxes connected by leader lines to the exact node each evasion strategy attacks: TP53 mutation → the p53 sensor; BAX/BAK loss → the effector/mitochondrion stage; guardian overexpression (BCL-2) → the BCL-2 balance; IAPs → the caspase node; PI3K-AKT / NF-κB survival signaling → pressing the BCL-2 balance. Color the central circuit spine sky-blue (anchor), and the five sabotage callouts vermillion (negative/blocking interventions) to make the layered, redundant attack spatially visible. Use thin leader lines, not arrows, for the callouts. No numeric data, no axes. Deliverable: single standalone HTML file, inline CSS, D3 v7 pinned CDN, Okabe-Ito colorblind-safe palette via CSS variables.

### Figure 14.3 — Navitoclax versus venetoclax: the platelet window
Build a two-panel comparison, left "Navitoclax (dual)" and right "Venetoclax (selective)," each a top-to-bottom cascade of four aligned rows so the two drugs read in parallel against a shared axis ("guardian targets and cell fate"). Rows: inhibits BCL-2 (both); inhibits BCL-XL too / BCL-XL not engaged; tumor cell dies (both); platelet dies (toxicity) / platelet survives. Align row-for-row to isolate the BCL-XL row as the single decisive difference. Color the shared BCL-2-inhibition row vermillion (target engaged), the BCL-XL row a transitional tone (the differentiator), the tumor-death row blue (dominant intended effect), and the bottom platelet-fate row green on the venetoclax side (platelet survives, window opens) versus plain/negative on the navitoclax side (toxicity). No numeric data. Deliverable: single standalone HTML file, inline CSS, D3 v7 pinned CDN, Okabe-Ito colorblind-safe palette via CSS variables.
