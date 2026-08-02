# Chapter 12 — Cell Cycle Control and Cancer: Disruption and Therapy
*Why blocking a kinase perfectly can still fail — and what the downstream state of the pathway tells you before you write the prescription.*

For more than a year, the CDK4/6 inhibitor worked. Scans stable. Tumor markers down. The metastatic breast cancer that had been advancing stopped advancing. Then, gradually, it returned. A new biopsy was sequenced. In some cases the resistant tumor had lost Rb entirely. In others it had amplified cyclin E. The drug still blocked CDK4/6. CDK4/6, in the resistant cancer, no longer mattered.

This is the thing worth understanding before the mechanism: the cancer did not become resistant by evading the drug. It became resistant by changing what it depends on. CDK4/6 was the critical node. The tumor deleted the component downstream that gave CDK4/6 its power. Now the kinase sits blocked, doing nothing useful, because the gate it controlled — Rb — is already permanently open or permanently bypassed. Blocking an upstream driver only works if the downstream pathway is intact and still load-bearing. When it is not, the drug is irrelevant.

Every cancer disrupts the cell cycle. Not every cancer is disrupted in the same way. The specific way a tumor broke its cell-cycle control determines which drug will work, whether a drug will work at all, and why resistance looks the way it does. This chapter is about reading that specific disruption and reasoning from it to therapy.

---

### What cancer breaks, and what it does not

The previous chapter built the normal machinery: the cyclin–CDK engine driving the cell through four phases, the Rb–E2F switch governing entry into DNA replication, the three checkpoints enforcing order, and the CDK inhibitors providing the brakes. The first thing to establish about cancer is what it does to that machinery — and what it does not.

What cancer does: it removes **conditional control**. Normal cells divide when conditions are right and stop when they are not. Growth factors present, nutrients available, DNA intact, spindle assembled — divide. Conditions absent or corrupted — pause, repair, or die. Cancer cells lose this conditionality. They divide in the absence of growth factors, divide despite DNA damage, divide with mis-assembled spindles. The word for this is **proliferation-default**: division is the baseline state rather than a triggered response to the right environment.

What cancer does not do, necessarily: divide faster. This is a persistent misconception worth correcting before it misleads the therapeutic reasoning. Many cancer cells cycle at rates comparable to normal proliferating cells — intestinal crypt cells, hair follicle cells, bone marrow progenitors. What distinguishes the cancer cell is not speed but the absence of the conditions on speed. A cell that divides at a normal rate but never pauses to check its DNA accumulates mutations at a far higher rate than any speed number alone would predict. The damage accumulates not because replication is hurried but because it is unconditioned. Checkpoint failure is the disease; faster cycling is an occasional consequence.

With that frame in place, the disruptions that cancer accumulates make immediate mechanistic sense.

---

### Six ways to force the gate open

The most commonly disrupted transition in cancer is the G1/S checkpoint — the gate between the gap phase and DNA replication. In the previous chapter's terms, this is the Rb–E2F switch: Rb holds E2F inactive until growth signals activate cyclin D–CDK4/6 to phosphorylate Rb and release it. Every cancer disruption at this transition forces the same endpoint: E2F constitutively free, S phase constitutively accessible.

Six distinct molecular lesions produce this same endpoint, and real tumors often combine several.

**Rb loss** is the direct route. Delete or mutate *RB1* and there is no gate to hold. E2F is free from birth. Rb loss is nearly universal in small-cell lung cancer, common in retinoblastoma (the gene's namesake), bladder cancer, and a subset of breast cancers. When Rb is gone, the G1/S gate does not exist anymore — not jammed open, not bypassed, simply absent.

**p16 loss** is the indirect route via CDK4/6 deregulation. p16 (encoded by *CDKN2A*) is a CDK inhibitor that binds CDK4 and CDK6 and prevents them from phosphorylating Rb. Without p16, CDK4/6 run constitutively regardless of mitogenic input — they phosphorylate Rb even when growth signals are absent, forcing E2F release. *CDKN2A* deletion or methylation silencing occurs in roughly 30 percent of all cancers and far higher fractions of melanoma (50–70 percent), pancreatic cancer (approaching 90 percent), and glioblastoma (around 50 percent). p16 loss does not remove the gate; it permanently wedges it open by keeping the kinase that phosphorylates the gatekeeper always active.

**Cyclin D amplification or overexpression** increases the abundance of the cyclin D–CDK4/6 complex beyond what the available p16 can inhibit. The translocation t(11;14) in mantle cell lymphoma places the *CCND1* gene under immunoglobulin enhancer control, producing enormous cyclin D1 levels. Many breast and head-and-neck cancers amplify the cyclin D1 locus. The effect is the same: too much kinase complex, not enough brake, Rb gets phosphorylated.

**CDK4 or CDK6 amplification** raises the kinase itself rather than its cyclin partner. CDK4 amplification occurs in well-differentiated liposarcoma and some gliomas; CDK6 amplification in T-cell leukemias and certain lymphomas. Quantitatively more kinase overwhelms the inhibitor.

**Activating CDK4 mutations** — the R24C substitution in melanoma is the canonical example — change the kinase structure so that p16 can no longer bind. The kinase remains active even when p16 levels are normal. Structurally, it is a mutation that makes the brake impossible to apply.

**Hyperactive upstream growth signaling** — constitutively active Ras–MAPK (from *KRAS* or *BRAF* mutations), PI3K–AKT (from *PIK3CA* mutations or PTEN loss), or Wnt (from APC loss) — drives cyclin D transcription and protein stabilization continuously. These pathways converge on cyclin D, producing the same result as amplification: more kinase complex than the available p16 can restrain.

Six distinct mechanisms, one net effect: the Rb–E2F gate is permanently open. The convergence is not coincidental — it reflects selection pressure. Any cell that loses conditional control over G1/S entry has a growth advantage in conditions where normal cells would pause. Natural selection in the tumor picks for the gate-open state; there are many molecular paths to get there.

![Many-to-one fan-in diagram: six lesions — Rb loss, p16/CDKN2A loss, cyclin D amplification, CDK4/6 amplification, activating CDK4 mutation, and hyperactive growth signaling — all converge on E2F constitutively free and S-phase entry.](images/12-cell-cycle-control-and-cancer-disruption-and-therapy-fig-01.png)
*Figure 12.1 — Six convergent routes to an open Rb–E2F gate*

<!-- → [DIAGRAM: six convergent routes to an open Rb–E2F gate. Six boxes on the left, each labeled with one mechanism (Rb loss, p16 loss, cyclin D amplification, CDK4/6 amplification, CDK4 activating mutation, hyperactive upstream signaling). All six converge via arrows to a single central outcome: "E2F constitutively free → S-phase entry." The convergence is the visual point — same destination, many starting points.] -->

---

### The kinase inhibitors and the meaning of therapeutic window

The convergence of so many lesions on CDK4/6 makes them an attractive drug target: block the kinase and, in principle, you restore the Rb–E2F brake regardless of which upstream derangement drove CDK4/6 hyperactivation. Three CDK4/6 inhibitors — palbociclib, ribociclib, and abemaciclib, all ATP-competitive, all oral — were approved between 2015 and 2017 for hormone-receptor-positive, HER2-negative breast cancer.

The disease-biology rationale is clean. In HR+ breast cancer, estrogen drives cyclin D1 transcription through the estrogen receptor. High cyclin D1 activates CDK4/6. CDK4/6 phosphorylates Rb. Rb releases E2F. The cell enters S phase. Combine an aromatase inhibitor (cutting estrogen) with a CDK4/6 inhibitor (blocking the kinase that cyclin D1 was activating) and you cut the pipeline at two points simultaneously, keeping Rb hypophosphorylated and the cell arrested in G1. The clinical results validated the logic: progression-free survival extended by roughly 10–12 months in the metastatic setting, with overall survival benefits demonstrated for ribociclib and abemaciclib in the pivotal trials.

But these drugs do not selectively target cancer cells. They target CDK4/6 wherever it operates — and bone marrow progenitor cells, gut epithelial stem cells, and hair follicle cells all depend on the same machinery. This is the meaning of a **therapeutic window**: the difference in CDK4/6 dependence between the tumor and the rapidly renewing normal tissues that the drug also hits. Neutropenia is the most common and dose-limiting toxicity of palbociclib and ribociclib — the bone marrow is a major casualty. Abemaciclib, which has additional CDK2 activity, causes more diarrhea from gut epithelial effects. Neither is surprising: target the kinase that dividing cells require and you target all dividing cells.

The therapeutic window exists because tumors often have higher cyclin D levels, greater CDK4/6 dependence, and a stronger arrest response to inhibition than normal renewing cells do. But the window is not wide, and it narrows further if dose is escalated beyond what the hematopoietic system tolerates. The lesson is that there is no such thing as a division-targeting drug that spares all normal tissue. It spares non-dividing tissue — neurons, muscle, quiescent stem cells. The renewing tissues it hits are the source of every predictable side effect.

![Two-panel comparison: in an Rb-intact responder the CDK4/6 inhibitor blocks the kinase, Rb transmits the block, E2F is restrained, and the cell arrests in G1; in an Rb-null tumor the kinase is equally blocked but E2F stays free and the cell enters S phase — target engaged is not response present.](images/12-cell-cycle-control-and-cancer-disruption-and-therapy-fig-02.png)
*Figure 12.2 — CDK4/6 inhibitor: target engaged vs response present*

<!-- → [DIAGRAM: CDK4/6 inhibitor mechanism in HR+ breast cancer. Left side: estrogen → ER → cyclin D1 transcription → CDK4/6 activation → Rb phosphorylation → E2F release → S phase entry. Red block arrow labeled "CDK4/6 inhibitor" cutting the kinase step. Below the block: Rb stays hypophosphorylated, E2F stays bound, cell arrests in G1. Right side, separate panel: Rb-null tumor — CDK4/6 still blocked by drug, but no Rb present to hold E2F, so E2F is still free, no G1 arrest occurs. Label: "drug works, target is engaged; response is absent because downstream node is missing."] -->

---

### Why downstream integrity decides response

The CDK4/6 inhibitor case is the clearest example of a general principle: **blocking an upstream driver only works if the downstream pathway remains intact**.

CDK4/6 inhibitors do not directly hold E2F inactive. They hold Rb in its unphosphorylated state, and *Rb* holds E2F inactive. The drug's entire efficacy is mediated through Rb. A tumor with functional Rb will arrest when CDK4/6 is blocked. A tumor that has lost Rb — through deletion or mutation, or by HPV E7 protein degrading it — has no Rb for the drug to protect. The CDK4/6 inhibitor blocks the kinase perfectly, but the effect it was supposed to produce, through Rb, cannot occur. The experiment in the opening case confirmed this at the resistance stage: the tumor deleted Rb and became refractory.

The same logic applies to the other resistance route: cyclin E amplification. Cyclin E activates CDK2, which can phosphorylate Rb independently of CDK4/6. If cyclin E is amplified, Rb gets phosphorylated via CDK2 even when CDK4/6 is completely blocked. The tumor has found a parallel path to the same endpoint. The gate opens through a different kinase.

These two resistance mechanisms — Rb loss and cyclin E amplification — are exactly what would be predicted from first principles if you drew the pathway and asked: "how could this cell bypass the block?" Rb loss removes the downstream target; cyclin E amplification routes around the blocked kinase via an alternative. Both are rational escape routes that a tumor under selection pressure will find. The clinical literature confirms they are the dominant mechanisms observed in biopsies of tumors that have escaped CDK4/6 inhibitor therapy.

The predictive corollary is equally important: these mechanisms can be present *before* treatment begins. A tumor that has already lost Rb at diagnosis will not respond. This is why Rb status has become a biomarker of interest — not just for resistance monitoring but for primary treatment selection. Cancers known to have very high rates of Rb loss (small-cell lung cancer, for instance) are not typically treated with CDK4/6 inhibitors. The path to personalized cell-cycle therapy runs through understanding which part of the pathway is still functional before the first dose is given.

---

### G2/M: the checkpoint cancer stresses but cannot afford to lose entirely

The G2/M checkpoint is less often *deleted* in cancer and more often *pushed to its limits*. The reason is that cancer cells, paradoxically, often need their remaining checkpoint machinery more than normal cells do.

Oncogene activation — constitutively active Ras, overexpressed Myc, amplified cyclin E — drives the cell to over-replicate. Forks stall, single-stranded DNA accumulates, the replication stress response fires. ATR kinase detects the stalled forks and activates Chk1, which halts the cell at G2/M to allow replication to finish. This is not damage from an external carcinogen; it is stress from the cell's own oncogene-driven hyperproliferation. The oncogene is pushing replication faster than the machinery can sustain.

In this state, the cancer cell is genuinely dependent on ATR and Chk1. Without them, the replication stress that oncogene activation produces would be unresolvable — forks would collapse into double-strand breaks, chromosomal catastrophe would follow, and the cell would die. Normal cells, not experiencing oncogene-driven replication stress, have far less dependence on ATR–Chk1 activity. This differential dependence is the basis of a therapeutic strategy: inhibit Chk1 or ATR, and the oncogene-stressed cancer cell loses its survival mechanism while normal cells are less affected.

This is **synthetic lethality** applied to checkpoint biology: the oncogene creates one vulnerability (replication stress), and blocking the checkpoint that resolves that stress creates a second, synthetic lethal vulnerability. The cancer cell — but not the normal cell — requires both the oncogene and the checkpoint to survive. Remove the checkpoint pharmacologically and the oncogene-driven cell dies from its own stress.

The same logic applies to **Wee1 kinase**, which adds an inhibitory phosphate to CDK1 and prevents premature entry into mitosis while DNA synthesis is still proceeding. Wee1 inhibitors push stressed cancer cells into mitosis before replication is complete, producing catastrophic mitotic failure. Clinical programs exploiting this dependency are in trials, primarily in tumors with high replication stress markers — *CCNE1* amplification, high Myc levels, RB1 loss with attendant CDK2 hyperactivity.

---

### The melanoma case: reading a convergence and writing a combination

BRAF V600E is the most common mutation in melanoma — present in roughly half of cutaneous melanomas — and it is one of the best-characterized oncogenic drivers. It constitutively activates the MAPK pathway: BRAF V600E phosphorylates MEK, MEK phosphorylates ERK, ERK enters the nucleus and transcribes cyclin D1. The cell cycle link is direct: this single kinase mutation drives cyclin D1 accumulation, CDK4/6 activation, Rb phosphorylation, and S-phase entry without external growth factor input.

The first-order drug is a BRAF inhibitor. Vemurafenib or dabrafenib blocks the constitutively active kinase, ERK signaling drops, cyclin D1 levels fall, CDK4/6 is no longer hyperactivated, and the cell arrests. In patients, BRAF inhibitor monotherapy produces dramatic initial responses in BRAF V600E melanoma — tumor regressions visible within weeks.

The responses are almost always transient. Resistance emerges in months, typically through reactivation of the MAPK pathway via alternative mechanisms: amplification of BRAF itself, mutations in NRAS upstream of BRAF, or activation of parallel RAF isoforms. The pathway reconstitutes around the block; cyclin D1 climbs again; the cell resumes cycling.

There is a second problem, visible before resistance: most BRAF V600E melanomas also carry *CDKN2A* deletion (p16 loss), and many carry PTEN loss activating the PI3K–AKT pathway, which also stabilizes cyclin D1 and drives Rb phosphorylation through a parallel route. Even when BRAF is successfully blocked, p16 loss and PI3K activation are still forcing CDK4/6 to run and driving Rb phosphorylation through AKT-stabilized cyclin D. The BRAF inhibitor addresses one of three converging perturbations on the same gate.

The combination that became standard — BRAF plus MEK inhibitor — addresses this by blocking MAPK signaling at two sequential steps, making it far harder for the pathway to reconstitute around a single block. Dabrafenib + trametinib, or vemurafenib + cobimetinib, extend response duration substantially compared to BRAF inhibitor monotherapy. The rationale is vertical combination: two drugs in the same pathway, preventing bypass.

The cell-cycle reasoning points toward a horizontal addition: a CDK4/6 inhibitor targeting the kinase that the converging perturbations (MAPK reactivation *and* p16 loss) are both ultimately driving. Clinical trials of CDK4/6 inhibitors combined with MAPK-pathway drugs in BRAF-mutant melanoma have shown activity, though the combination toxicity and optimal sequencing are still being worked out.

The logic of combination therapy for melanoma is readable directly from the pathway diagram. Draw the lesions: BRAF V600E driving cyclin D from MAPK, p16 loss removing the CDK4/6 brake, and PTEN loss driving cyclin D from PI3K. All three converge on CDK4/6 → Rb phosphorylation → E2F release. Block BRAF alone and the other two keep the gate open. Block BRAF + MEK and you close the MAPK route while the other two persist. Add a CDK4/6 inhibitor and you address the convergence point itself — the kinase all three pathways are feeding. Each additional drug is justified by a specific residual mechanism that the previous combination leaves active. This is what combination-therapy reasoning looks like when it is mechanistically grounded rather than empirically assembled.

![Convergent pathway diagram: three perturbations — BRAF V600E driving cyclin D1 through MEK/ERK, p16/CDKN2A loss uninhibiting CDK4/6, and PTEN loss stabilizing cyclin D1 via PI3K/AKT — all feed the CDK4/6 → Rb-phosphorylation gate, with drug intervention points (BRAFi+MEKi, CDK4/6i) mapped to each residual input.](images/12-cell-cycle-control-and-cancer-disruption-and-therapy-fig-03.png)
*Figure 12.3 — BRAF V600E melanoma: three inputs converging on one gate*

<!-- → [DIAGRAM: BRAF V600E melanoma with three converging perturbations. Three input boxes: (1) BRAF V600E → MEK → ERK → cyclin D1; (2) p16 loss → CDK4/6 uninhibited; (3) PTEN loss → PI3K → AKT → cyclin D1 stabilization. All three converge on CDK4/6 → Rb phosphorylation → E2F free → S phase. Drug intervention labels: BRAF inhibitor on pathway 1; MEK inhibitor on pathway 1 downstream; CDK4/6 inhibitor on the convergence point. Annotate: single-agent failure leaves two active inputs; BRAF+MEK closes one pathway but not the others; CDK4/6 inhibitor addresses the convergence.] -->

---

### What resistance teaches about rational design

Every resistance mechanism to a cell-cycle drug is a lesson about what the drug did not address. Rb loss under CDK4/6 inhibitor pressure teaches that the downstream target must remain functional. Cyclin E amplification under the same pressure teaches that the pathway has an alternative input that can phosphorylate Rb without CDK4/6. MAPK reactivation under BRAF inhibitor pressure teaches that single-node blockade in a pathway with many bypass routes will always lose.

The general principle that emerges: a drug that blocks one node in a convergent pathway achieves complete arrest only if it is the rate-limiting node and there are no bypasses. In practice, cancer pathways have many inputs and multiple redundancies, so single-agent therapy against a pathway node is almost never rate-limiting across all cases or durable across all time points in the cases where it initially works.

The rational response to this is not to abandon targeted therapy but to ask, before beginning, which bypasses are already present and which are likely to emerge under selection. Rb status answers the first question for CDK4/6 inhibitors. The mutational landscape of the rest of the pathway answers it for MAPK-targeted drugs. And the second question — which resistance mechanisms are most likely to emerge — should guide the design of upfront combinations that close the most probable escape routes before they are selected.

Cell-cycle therapy has delivered some of the most durable benefits in the treatment of solid tumors when this reasoning has been applied. It has also produced some of the most predictable resistance patterns in all of oncology — because the logic of bypass and convergence is transparent enough that the resistance mechanisms can often be anticipated before they appear.

---

## Exercises

**Warm-up**

1. *(Recall — difficulty: low)* List four distinct molecular lesions that force the Rb–E2F gate open in cancer. For each, state in one clause what specifically it does to the gate and why the cell can no longer keep E2F inactive. *What this tests: whether you can generate the mechanism for each lesion rather than just naming it.*

2. *(Recall — difficulty: low)* What is the difference between "faster cell division" and "checkpoint failure" as descriptions of cancer cell-cycle biology? Why does the distinction matter for understanding how cancer accumulates mutations? *What this tests: the conceptual separation of proliferation rate from conditional control.*

3. *(Recall — difficulty: low)* Why does CDK4/6 inhibitor treatment cause neutropenia? Name the cell type affected and trace the mechanism from the drug's target to the clinical toxicity. *What this tests: the therapeutic window concept applied specifically to the bone marrow.*

**Application**

4. *(Apply — difficulty: medium)* Three tumors are sequenced. Tumor A has *CDKN2A* deletion with intact Rb. Tumor B has *RB1* deletion with normal p16. Tumor C has cyclin E1 amplification with intact Rb. Predict which would respond to a CDK4/6 inhibitor and which would not. For each prediction, trace the drug's mechanism through the pathway to the expected outcome. *What this tests: downstream-integrity reasoning applied to three distinct pathway configurations.*

5. *(Apply — difficulty: medium)* A patient's BRAF V600E melanoma responds to dabrafenib (BRAF inhibitor) for six months and then progresses. Sequencing of the resistant tumor shows no new mutations in BRAF but shows amplification of NRAS. Explain mechanistically how NRAS amplification produces resistance to BRAF inhibition, and predict whether adding a MEK inhibitor would restore response. *What this tests: pathway bypass logic and the rationale for vertical combination.*

6. *(Apply — difficulty: medium)* Explain the synthetic lethality rationale for Chk1 inhibitors in Myc-amplified cancers. Why does Myc amplification create replication stress? Why does that stress make the cancer cell dependent on Chk1? And why would normal cells be less affected by Chk1 inhibition? *What this tests: the replication stress → checkpoint dependency → synthetic lethality logic.*

**Synthesis**

7. *(Synthesize — difficulty: high)* A new tumor type is sequenced and found to have three concurrent alterations: activating *KRAS* mutation, *CDKN2A* deletion, and *PTEN* loss. Draw or describe the pathway diagram showing how all three converge on the Rb–E2F gate. Then design a three-drug combination therapy that addresses each convergent input, name the drug class for each, and identify the one biomarker you would check before treating to confirm the strategy is appropriate. *What this tests: convergent pathway reasoning and combination-therapy design from first principles.*

8. *(Synthesize — difficulty: high)* CDK4/6 inhibitors arrest cells in G1. Arrested cancer cells do not always die — many enter a senescent-like state and can resume proliferation later, or secrete pro-tumor signals. Using what you know about the cell cycle and apoptosis, propose why arrested cells might not die, and suggest one mechanistic combination strategy (CDK4/6 inhibitor plus a second agent) that would push arrested cells toward death rather than arrest. Justify the second agent's mechanism. *What this tests: integration of cell-cycle arrest with the apoptosis pathway, pointing forward to the next chapter.*

**Challenge**

9. *(Challenge — difficulty: high)* The success of CDK4/6 inhibitors in HR+ breast cancer has prompted proposals to use them across many other cancer types based on the prevalence of Rb-pathway alterations. Critically evaluate this generalization: what evidence from HR+ breast cancer supports broad application, what tumor-specific factors make the breast cancer setting unusual, and what you would need to see in preclinical and early-phase data before recommending a CDK4/6 inhibitor trial in a new indication. Identify the single most important biomarker criterion you would require and explain why. There is no single correct answer; mechanistically grounded reasoning with honest acknowledgment of limits is the goal. *What this tests: critical evaluation of generalization from a specific success, the relationship between pathway logic and clinical evidence, and biomarker-driven trial design.*

---

## Prompts

### Figure 12.1 — Six convergent routes to an open Rb–E2F gate
Build a node-edge systems diagram showing a many-to-one fan-in. Place six lesion nodes in a left column — Rb loss, p16/CDKN2A loss, cyclin D amplification, CDK4/6 amplification, activating CDK4 mutation, hyperactive growth signaling — each with a single directed arrow converging onto one shared node, "E2F constitutively free," which then arrows to a final node, "S-phase entry." The visual point is convergence: six origins, one destination. Keep the six inputs neutral gray, color the E2F node blue (dominant shared hub), and the S-phase node a secondary/anchor tone. Use clean arrowheads; avoid crossing edges by stacking inputs vertically and routing into the hub. No numeric data, no axes. Deliverable: single standalone HTML file, inline CSS, D3 v7 pinned CDN, Okabe-Ito colorblind-safe palette via CSS variables.

### Figure 12.2 — CDK4/6 inhibitor: target engaged vs response present
Build a two-panel before/after comparison, left "Rb intact (responder)" and right "Rb null (resistant)," each a top-to-bottom cascade of five aligned rows so the two read in parallel. Shared rows: cyclin D1 → CDK4/6; CDK4/6 blocked by inhibitor; Rb present transmits the block / Rb absent block not transmitted; E2F restrained / E2F still free; G1 arrest (response) / S-phase entry (no response). Align row-for-row to make the single divergence point obvious. Color the shared top input row sky-blue (anchor), the "CDK4/6 blocked" row vermillion (negative/blocked target, identical in both), the Rb-status row a transitional tone, and the bottom outcome row blue (dominant outcome) — green tint on the left arrest, plain on the right. Caption: the drug engages its target in both, but response requires an intact downstream node. No numeric data. Deliverable: single standalone HTML file, inline CSS, D3 v7 pinned CDN, Okabe-Ito colorblind-safe palette via CSS variables.

### Figure 12.3 — BRAF V600E melanoma: three inputs converging on one gate
Build a node-edge convergent pathway diagram with three input chains feeding one gate, plus labeled intervention points. Inputs: (1) BRAF V600E → MEK → ERK → cyclin D1; (2) p16/CDKN2A loss → CDK4/6 uninhibited; (3) PTEN loss → PI3K → AKT → cyclin D1. All three arrow into a central gate node "CDK4/6 → Rb phosphorylation," which arrows (block-style terminator) to "E2F free → S-phase." Annotate intervention points as edge labels: "BRAFi + MEKi" on input 1, "CDK4/6i" on the gate-to-S-phase block. Color the BRAF input blue (dominant driver), the p16-loss input a transitional tone, the PI3K input secondary/neutral, and the central gate sky-blue (anchor convergence point); draw the CDK4/6i block edge in vermillion. Lay inputs as three stacked left chains merging at the central gate. No numeric data, no axes. Deliverable: single standalone HTML file, inline CSS, D3 v7 pinned CDN, Okabe-Ito colorblind-safe palette via CSS variables.
