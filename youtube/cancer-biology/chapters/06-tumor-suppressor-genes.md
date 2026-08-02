# Chapter 6 — Tumor Suppressor Genes
*The inverted logic of brakes that must be broken twice — and how breaking them can become the cancer's fatal weakness.*

A 33-year-old woman has no symptoms. Every cell in her body carries a defective copy of a gene whose job is to repair a specific kind of DNA damage. She inherited it from her mother, who died of ovarian cancer at 48. Her aunt had breast cancer at 41. Her grandmother had breast cancer. The woman herself is healthy, and she may stay healthy for decades more — because she still has one working copy of that gene, and as long as she does, her cells repair DNA damage correctly.

Her elevated cancer risk — a lifetime breast cancer risk somewhere around 65–80 percent, ovarian risk around 40–60 percent — comes from a single probability: that somewhere in her breast or ovarian tissue, over the course of decades, one cell will lose its remaining good copy through an independent somatic mutation. In that one cell, and only that cell, the repair machinery fails completely. Mutations begin to accumulate. The cancer that eventually develops — if it does — will trace back to that single second event in that single cell.

This is the logic of tumor suppressor genes, and it is completely inverted from everything Chapter 5 said about oncogenes. Oncogenes are accelerators. One mutation, one activated copy, is enough to push. Tumor suppressors are brakes. Both copies must fail before the cell runs free. Understanding why that is — and what it implies for how cancers arising from broken brakes are detected, inherited, and treated — is this chapter.

---

### Why both copies must fail

Alfred Knudson did not know the molecular biology. In 1971 he was looking at the age distribution of retinoblastoma — a childhood eye tumor — and he noticed a statistical pattern that made no sense unless there were two independent events required for the tumor to form.

Children with the inherited form developed tumors early — often in the first year of life — and typically in both eyes, with multiple independent tumors in each retina. Children with the sporadic form developed tumors later, in one eye, with a single tumor. Knudson reasoned that the inherited patients had already received one hit at birth, in every cell. The second hit — in any one of the thousands of developing retinal cells — was nearly certain to happen somewhere, and happen soon. The sporadic patients needed both hits in the same cell independently, a much rarer coincidence. This was the **two-hit hypothesis**, published before *RB1* was cloned, before the protein was characterized, before anyone knew what the gene did.

The molecular confirmation came in 1986 when the gene was cloned and the tumor-suppressor concept was formalized. More important than the molecular details was the experimental logic that defined the category. You cannot find a tumor suppressor by transfecting it into a cell and watching for transformation — adding a working brake does not cause cancer; it prevents it. The proof came from a different direction: fusing a cancer cell with a normal cell produces a hybrid that *cannot* form tumors. The normal cell contains something dominant that suppresses the cancer phenotype. When you lose it, cancer emerges. When you restore it, cancer is suppressed. This rescue experiment — demonstrating that reintroducing a wild-type copy reverses tumorigenicity — remains the gold-standard test for whether a gene is a genuine tumor suppressor.

The biallelic requirement follows from the logic. Tumor suppressors are typically **recessive at the cellular level**: one good copy is enough to do the job. The brake works even at half dosage. Only when the second allele is lost — by mutation, deletion, methylation, or physical loss of the chromosome region — does function disappear. The inherited cancer syndromes make this visible: the patient is born with one hit, and the second hit rates are what determine the penetrance and tissue specificity of the syndrome.

![Retinoblastoma two-hit hypothesis: inherited germline hit gives bilateral, multifocal disease vs sporadic](images/06-tumor-suppressor-genes-fig-03.png)
*Figure 6.3 — Two-hit hypothesis: retinoblastoma, inherited vs sporadic*

<!-- → [DIAGRAM: two-hit hypothesis illustrated with retinoblastoma — left panel: inherited form, all cells carry one defective allele (first hit), second hit occurs in multiple retinal cells independently, multiple bilateral tumors; right panel: sporadic form, both hits must occur in the same cell, single unilateral tumor, later onset. Annotate the probability difference that explains the age-at-onset gap.] -->

---

### Two types of brake, two types of failure

Not all tumor suppressors restrain cells the same way, and the distinction matters for predicting what their loss does.

**Gatekeepers** directly control cell fate — they restrain entry into the cell cycle, promote cell death, or limit cell number in a tissue. Lose a gatekeeper and the cell divides when it should not, or survives when it should die. *RB1* is the canonical gatekeeper: its protein holds the cell at the G1/S boundary until growth signals give permission. *APC* is a gatekeeper in the gut: it holds β-catenin in check, so Wnt signaling is quiet unless there is a reason to grow. Lose *APC* and the Wnt pathway is permanently on regardless of upstream signal.

**Caretakers** maintain genome integrity. They do not directly restrain proliferation; they ensure that the mutations which would eventually release the gatekeepers do not accumulate so fast. *BRCA1* and *BRCA2* enable accurate repair of DNA double-strand breaks. The mismatch-repair genes — *MLH1*, *MSH2*, *MSH6*, *PMS2* — correct replication errors. Lose a caretaker and the cell does not immediately proliferate abnormally; it becomes a better mutator, accumulating errors that will eventually hit gatekeepers and oncogenes. The cancer risk from caretaker loss is real and substantial, but the mechanism is indirect: it raises the mutation supply, shortening the time to transformation.

The 33-year-old woman with the *BRCA1* variant is a caretaker case. Her cells are not dividing abnormally. Her cell cycle is normal. Her elevated risk comes from the probability that her cells will fail to accurately repair double-strand breaks for decades until some cell accumulates the combination of mutations that tips into malignancy. This is categorically different from *APC* or *RB1* loss, where the gate is directly open.

Some genes blur the boundary. *TP53* integrates damage signals and enacts responses — cell cycle arrest, apoptosis, senescence — making it a gatekeeper in the sense that its loss allows damaged cells to survive and divide. But it also activates repair machinery, giving it a caretaker dimension. It is the most important single gene in cancer biology precisely because its loss removes multiple protective functions simultaneously.

---

### p53: the decision hub

*TP53* is altered in roughly half of all human tumors, and in over 90 percent of some histologic types — high-grade serous ovarian carcinoma, head and neck squamous cell carcinoma. No other gene comes close to this frequency across cancer. Understanding why requires understanding what p53 does, not just what it is called.

p53 is a transcription factor. In an unstressed cell it is maintained at low levels by **MDM2**, an E3 ubiquitin ligase that continuously tags p53 for proteasomal degradation. The moment a cell experiences serious stress — DNA strand breaks, oncogene activation, hypoxia, nucleotide depletion — sensor kinases respond. **ATM** and **ATR** detect strand breaks; **CHK1** and **CHK2** amplify the signal. These kinases phosphorylate p53 at residues that prevent MDM2 binding. Without MDM2 tagging it for destruction, p53 accumulates rapidly. It then transcribes a set of target genes whose products execute a decision.

The decision has four possible outcomes, chosen by context:

**Arrest.** p53 transcribes *CDKN1A*, producing the protein p21, which inhibits cyclin-CDK complexes and halts the cell cycle at G1/S. This is the "wait and fix" response — stop dividing, repair the damage, restart.

**Repair.** p53 activates damage-response components including GADD45, XPC, and DDB2, directly scaffolding the repair machinery at the site of damage.

**Senescence.** Under some conditions — particularly oncogene activation — p53 drives a permanent non-dividing state. The cell is alive but will not replicate. This is a stable tumor-suppressive response, not merely a temporary pause.

**Apoptosis.** If damage is severe enough that repair would be futile, or if oncogene-driven replication cannot be contained, p53 transcribes pro-apoptotic genes: *PUMA*, *NOXA*, *BAX*. The cell activates its own death program rather than copy damaged DNA into daughter cells.

Lose p53 and the cell loses all four of these options simultaneously. A cell with irreparably damaged DNA that should have arrested, repaired, or died instead keeps dividing, accumulating further damage, copying it forward. This is the actual mechanism of p53 loss in cancer — not a metaphor about guarding the genome, but the specific removal of four protective transcriptional responses at once.

The mutational pattern in *TP53* reveals something beyond simple loss of function. Most tumor suppressors are inactivated by truncating mutations — frameshifts, nonsense, splice-site changes — that destroy the protein entirely. *TP53* is mostly inactivated by **missense mutations** that change single amino acids in the DNA-binding domain. Hot spots at R175, R248, R273, and a handful of others account for a disproportionate fraction of *TP53* mutations across cancer. This is not coincidence.

p53 works as a tetramer — four subunits assemble to bind DNA. A missense mutant subunit can incorporate into the tetramer alongside wild-type subunits and poison its function, a **dominant-negative** mechanism. This is how a single missense allele can inactivate the function of the remaining wild-type allele without requiring loss of heterozygosity. Some mutant p53 proteins go further: they acquire *new* activities that promote invasion, chemotherapy resistance, and altered metabolism — genuine gain-of-function properties. This is why *Li-Fraumeni syndrome*, caused by germline *TP53* mutations, produces an extraordinary spectrum of cancers from childhood — bone, brain, breast, adrenal, leukemia — in patients with partial retention of what looks like a single mutant allele.

![p53 decision hub: stress kinases displace MDM2, then p53 chooses arrest, repair, senescence, or apoptosis](images/06-tumor-suppressor-genes-fig-01.png)
*Figure 6.1 — p53: the decision hub*

<!-- → [DIAGRAM: p53 activation circuit — top: MDM2 tagging p53 for degradation in an unstressed cell; middle: DNA damage → ATM/ATR → CHK1/2 phosphorylation of p53 → MDM2 dissociation → p53 accumulation; bottom: four transcriptional outputs (CDKN1A/arrest, repair genes, senescence markers, PUMA/NOXA/BAX/apoptosis) with one-line annotations of what each does and when each is chosen.] -->

---

### RB1: the gate into replication

The Rb protein controls a single, critical transition: entry into DNA replication. Understanding how it works makes clear why losing it is so directly oncogenic.

In a quiescent or early G1 cell, Rb is **unphosphorylated**. In this state it binds the transcription factor **E2F** and holds it inactive. E2F, when free, turns on the genes needed for S phase — DNA polymerases, dNTP synthesis, replication origin firing machinery. As long as Rb holds E2F, the cell cannot enter replication.

Growth signals activate cyclin D–CDK4/6 complexes, which phosphorylate Rb at multiple sites. **Phosphorylated Rb** releases E2F. E2F drives S-phase entry. Subsequent phosphorylation by cyclin E–CDK2 keeps Rb inactivated through the rest of the cycle. At mitosis, phosphatases reset Rb to its active state for the next G1.

Lose *RB1* and the gate is permanently open: E2F is constitutively free, S-phase genes are permanently on, and the cell no longer requires growth signals to replicate. The checkpoint function the gate provided — coupling replication to external growth permission — is gone.

This connects directly to the CDK4/6 inhibitors that are now standard treatment in hormone-receptor-positive metastatic breast cancer. Palbociclib, ribociclib, and abemaciclib prevent cyclin D–CDK4/6 from phosphorylating Rb, holding it in its E2F-binding, growth-suppressive form. The logic only works if Rb is present and functional — which is why *RB1* loss in breast cancer is associated with resistance to CDK4/6 inhibition. The target of the drug is the pathway that Rb sits in; remove Rb from the pathway and the drug has no relevant substrate to act through.

Human papillomavirus attacks the same gate from the protein level. The E7 oncoprotein of high-risk HPV types (16, 18, 31, 33) binds Rb and targets it for degradation, functionally inactivating the *RB1* gene product without mutating the gene. The gate is opened by viral protein rather than by somatic mutation. This is why HPV-driven cervical cancers often have wild-type *RB1* at the sequence level while behaving as if Rb is absent.

---

### APC and PTEN: two more logics of loss

*APC* is the colorectal cancer gene, mutated in roughly 80 percent of colorectal cancers and typically the earliest detectable event — present in small polyps, before most other mutations. Its protein is a scaffold in the **Wnt destruction complex**: in the absence of a Wnt signal, APC, Axin, GSK-3β, and CK1 assemble and phosphorylate **β-catenin**, targeting it for ubiquitin-mediated degradation. When a Wnt ligand binds its receptor, the complex is disrupted, β-catenin escapes degradation, accumulates in the cytoplasm, and translocates to the nucleus where it drives transcription of proliferation targets including *MYC* and cyclin D1. Lose APC and the destruction complex cannot form, β-catenin accumulates regardless of Wnt signal, and the cell behaves as though it is continuously receiving a proliferate instruction even in a quiescent environment. **Familial adenomatous polyposis** — caused by germline *APC* mutations — produces hundreds to thousands of colonic polyps and near-certain colorectal cancer by middle age without surgical intervention, illustrating gatekeeper logic in its purest tissue-specific form.

*PTEN* opposes the PI3K pathway — the most frequently activated growth and survival pathway in human cancer. PI3K converts PIP2 to **PIP3** at the inner membrane leaflet; PIP3 recruits AKT, which is then activated by PDK1 and promotes proliferation, survival, and growth. PTEN is a lipid phosphatase that converts PIP3 back to PIP2, functioning as the off switch for the pathway. Lose PTEN and PI3K signaling fires constitutively without requiring an upstream receptor signal.

*PTEN* is notable for being **haploinsufficient**: unlike most tumor suppressors, *partial* loss — one allele, or reduced expression through promoter methylation without complete silencing — is sufficient to meaningfully dysregulate the pathway. The two-hit rule applies in its strict sense to complete loss, but even partial reduction of PTEN protein level is functionally consequential. This is the exception students should hold alongside the rule: biallelic loss is the general case for tumor suppressors, but PTEN is a documented exception where dosage matters.

![APC and the Wnt destruction complex: intact APC degrades beta-catenin; lost APC drives proliferation](images/06-tumor-suppressor-genes-fig-04.png)
*Figure 6.4 — APC and the Wnt destruction complex (two-state switch)*

<!-- → [DIAGRAM: APC/Wnt pathway — two-state schematic. Left: Wnt off, APC in destruction complex phosphorylating β-catenin → degradation, nucleus quiet. Right: APC mutated, destruction complex absent, β-catenin accumulates, enters nucleus, drives MYC/cyclin D1 transcription. Clean before/after diagram with labeled components.] -->

---

### Five ways to silence a brake

Because the goal is functional inactivation of both alleles, evolution — and cancer — has found multiple routes. Knowing them matters because each has a different diagnostic footprint.

**Point mutation** is the most familiar: a single nucleotide change in the coding sequence truncates or destabilizes the protein. Most tumor suppressors accumulate truncating mutations (frameshifts, nonsense), though *TP53* is the exception.

**Loss of heterozygosity (LOH)** is the most common second hit. A cell with one mutated allele loses the wild-type allele through chromosomal deletion, mitotic recombination, or the loss of an entire chromosomal arm. LOH is detectable by comparing allele frequencies in tumor versus normal tissue; large regions of LOH in tumor genomes point toward the location of relevant tumor suppressors.

**Large deletion** removes the gene entirely. *CDKN2A* (encoding both p16 and p14ARF) at chromosome 9p21 is among the most frequently homozygously deleted loci in human cancer — gone in glioblastoma, pancreatic cancer, melanoma, and others.

**Promoter hypermethylation** silences the gene without altering the sequence. A CpG island in the gene's promoter is chemically modified — cytosines are methylated — and transcription is blocked. The gene is intact; it simply is not read. *MLH1* silencing by methylation produces microsatellite-instability-high colorectal cancer in patients with no germline mutation in any mismatch-repair gene; the second allele is lost by LOH. This epigenetic silencing is in principle reversible — demethylating agents can restore transcription in some contexts — which has been one rationale for epigenetic therapy, explored in Chapter 8.

**Viral inactivation** targets the protein directly. HPV E6 binds p53 and recruits an E3 ubiquitin ligase to degrade it; E7 binds and degrades Rb. The genes are intact, the proteins are gone. This is mechanistically equivalent to biallelic loss for therapeutic and prognostic purposes, though it looks different in a sequencing analysis.

---

### Synthetic lethality: turning a loss into a target

The conventional problem with tumor suppressor loss as a therapeutic target is obvious: you cannot add back a gene with a small molecule. You cannot restore a deleted *TP53* with a drug. The loss-of-function logic seems to foreclose pharmacological intervention — how do you target something that is absent?

The answer is indirect, and it is one of the most elegant strategies in modern oncology. The logic is called **synthetic lethality**: two defects, each survivable alone, are lethal together. The cancer cell has one defect — BRCA1 loss. The therapy creates a second — PARP inhibition. Normal cells have BRCA function and survive the PARP inhibitor. Cancer cells lack BRCA function and die from the accumulated double-strand breaks the PARP inhibitor produces.

To see why it works, trace the repair pathway precisely. **PARP1** detects and repairs single-strand breaks — minor, common lesions. When PARP is inhibited, single-strand breaks accumulate. When a replication fork encounters an unrepaired single-strand break, the fork collapses into a double-strand break — a far more serious lesion. The cell normally repairs double-strand breaks by **homologous recombination**, using the sister chromatid as a template for accurate repair. This requires BRCA1, BRCA2, and RAD51. A cell with intact BRCA function repairs the double-strand break and survives. A cell with BRCA1 loss cannot perform homologous recombination; the double-strand break is either left unrepaired or repaired inaccurately by error-prone pathways, producing chromosomal rearrangements. Enough of these and the cell dies.

The selectivity is real and clean: normal cells throughout the body experience the same PARP inhibition and the same single-strand-break accumulation, but they repair the resulting double-strand breaks via homologous recombination and are unharmed. Only BRCA-deficient cells lack this rescue route.

Olaparib, the first PARP inhibitor approved, demonstrated this in BRCA-mutant ovarian cancer and subsequently in BRCA-mutant breast, prostate, and pancreatic cancers. The principle has extended beyond *BRCA* mutations: any cancer with a defect in homologous recombination — BRCA2 mutation, PALB2 mutation, RAD51 paralogue mutations, BRCA1 promoter methylation — shows the same PARP inhibitor vulnerability. The constellation of HR-defective features is called **homologous recombination deficiency (HRD)** and is now measured in tumor sequencing to identify PARP inhibitor candidates beyond germline BRCA carriers.

Resistance develops, primarily through *reversion mutations* that restore the BRCA open reading frame — a second somatic mutation in the tumor that repairs the original pathogenic variant. These reversions reconstitute HR and remove the synthetic lethality. Other resistance mechanisms include upregulation of drug efflux pumps, restoration of HR through other proteins, and switching to non-HR repair pathways. The existence of these resistance routes does not undermine the strategy; it defines its limits and motivates the search for combination therapies that close the escape routes.

![BRCA x PARP synthetic lethality grid: only the double-defect corner is lethal](images/06-tumor-suppressor-genes-fig-02.png)
*Figure 6.2 — Synthetic lethality: the BRCA × PARP grid*

<!-- → [DIAGRAM: synthetic lethality grid — two-by-two matrix. Axes: BRCA status (intact / deficient) and PARP inhibitor (absent / present). Four cells: BRCA intact + no inhibitor = live; BRCA intact + inhibitor = live (HR rescues); BRCA deficient + no inhibitor = live (survives with other repair); BRCA deficient + inhibitor = dead (DSBs accumulate, no HR rescue). Annotate with the mechanism at each cell.] -->

The broader principle extends beyond PARP inhibitors. Every tumor suppressor loss creates a dependency: the cell is now relying on whatever compensating mechanism it uses to survive in the absence of that suppressor's function. Map the dependency, find a drug that removes it, and the suppressor loss becomes a target rather than an obstacle. This is the conceptual frame that makes tumor suppressor biology therapeutically actionable — not by restoring what is lost, but by exploiting what the cell now cannot do without.

---

## Exercises

**Warm-up**

1. *(Recall — difficulty: low)* State the two-hit hypothesis in one sentence. Then explain why children with inherited retinoblastoma develop tumors earlier and more often bilaterally than children with sporadic retinoblastoma, using only the two-hit logic. *What this tests: whether you can derive the clinical observation from the probabilistic logic, not just state the hypothesis.*

2. *(Recall — difficulty: low)* Classify each of the following as gatekeeper or caretaker, and give a one-sentence explanation of why: *RB1*, *BRCA2*, *APC*, *MLH1*, *TP53*. *What this tests: functional classification applied to the five tumor suppressors covered in the chapter.*

3. *(Recall — difficulty: low)* Name five mechanisms by which a tumor suppressor can be functionally inactivated and give one example gene or cancer for each. *What this tests: the range of inactivation mechanisms beyond point mutation.*

**Application**

4. *(Apply — difficulty: medium)* A sporadic colorectal cancer is found to have silenced *MLH1* by promoter hypermethylation rather than by a coding mutation. Explain why this produces a microsatellite-instability-high phenotype even though no gene sequence has changed, and explain why this tumor could arise in a patient with no family history of Lynch syndrome. *What this tests: epigenetic silencing as an alternative to mutation, and the distinction between sporadic and inherited caretaker loss.*

5. *(Apply — difficulty: medium)* A breast cancer patient is treated with a CDK4/6 inhibitor (palbociclib) and responds initially, but her tumor acquires resistance. Sequencing of the resistant tumor shows loss of *RB1*. Explain mechanistically why *RB1* loss confers resistance to this drug class. *What this tests: the Rb/E2F gate and the therapeutic logic that depends on Rb being present.*

6. *(Apply — difficulty: medium)* An HPV-positive cervical cancer biopsy is sequenced and shows wild-type *TP53* and wild-type *RB1* coding sequences. Yet the cancer behaves as if both tumor suppressors are lost. Explain the mechanism by which this occurs and state what you would look for in the tumor to confirm it. *What this tests: viral inactivation of protein versus genetic mutation, and the distinction between gene sequence and protein function.*

**Synthesis**

7. *(Synthesize — difficulty: high)* Trace the full synthetic lethality mechanism of PARP inhibitors in BRCA1-deficient cancer. Start with PARP's normal function on single-strand breaks, proceed through fork collapse to double-strand breaks, explain why homologous recombination is the critical rescue pathway, and show why BRCA1-intact normal cells survive while BRCA1-deficient cancer cells do not. Then: describe the most common resistance mechanism and explain it in the same mechanistic terms. *What this tests: integration of the repair pathway with the therapeutic logic and the limits of the strategy.*

8. *(Synthesize — difficulty: high)* Compare the mechanisms of p53 inactivation and Rb inactivation. p53 is predominantly inactivated by missense mutation; Rb is predominantly inactivated by truncation or deletion. Explain why missense mutations in *TP53* are functionally different from simple loss of function — invoke the tetramer architecture and the dominant-negative mechanism — and explain what this implies about why *TP53* missense mutations are selected for in tumors rather than truncating mutations. *What this tests: structural reasoning about why the mutation spectrum of TP53 differs from other tumor suppressors.*

**Challenge**

9. *(Challenge — difficulty: high)* The synthetic lethality concept has been extended beyond BRCA/PARP to other tumor suppressor losses. Choose one tumor suppressor covered in this chapter (not BRCA1/2) and design a hypothetical synthetic lethality strategy for cancers that have lost it. Specify: (a) what cellular function is lost when this suppressor is inactivated, (b) what compensating pathway the cancer cell must now rely on, (c) what drug target in that compensating pathway could be inhibited to create synthetic lethality, and (d) what resistance mechanism you would most expect. Evaluate whether your proposed strategy is more or less mechanistically clean than the BRCA/PARP example and explain why. There is no single correct answer; mechanistically coherent reasoning is the goal. *What this tests: generalization of the synthetic lethality principle beyond the worked example, applied to a different tumor suppressor with a different functional loss.*

---

## Prompts

### Figure 6.1 — p53: the decision hub
Build a node-edge systems diagram with a vertical activation circuit fanning into a four-output decision. Central hub node: "p53 hub (accumulates when MDM2 dissociates)" (blue, dominant, large, centered). Two inputs: "Stress (DNA breaks, oncogene, hypoxia) → ATM/ATR → CHK1/CHK2" feeds an arrow into p53 labeled "stabilize" (secondary); "MDM2 ubiquitin-tags p53 (resting degradation)" connects to p53 with a blocking/inhibition edge labeled "degrade" (vermillion, negative). From the p53 hub, four output arrows fan downward to: "Arrest (p21/CDKN1A)" (green, positive), "Repair (GADD45/XPC/DDB2)" (secondary), "Senescence (permanent non-dividing)" (transitional hue), "Apoptosis (PUMA/NOXA/BAX)" (vermillion, negative). Use distinct arrowheads for activation vs the MDM2 blocking edge. Emphasize that one hub controls four fates, so losing it removes all four. Subtitle: "MDM2 displaced, then a four-way fate decision." Okabe-Ito semantics: blue dominant hub, green for arrest, vermillion for MDM2 inhibition and apoptosis. Deliverable: single standalone HTML file, inline CSS, D3 v7 pinned CDN, Okabe-Ito colorblind-safe palette via CSS variables.

### Figure 6.2 — Synthetic lethality: the BRCA × PARP grid
Build a 2×2 outcome matrix. Column headers: "BRCA/HR intact" (left) and "BRCA/HR deficient" (right). Row headers (axis label "PARP inhibitor status"): "PARP absent" (top) and "PARP present" (bottom). Four cells: top-left "live" (green); top-right "live (other repair)" (green); bottom-left "live (HR rescues DSBs)" (green); bottom-right "DEAD (no HR rescue)" (vermillion, negative). The single bottom-right corner is the only lethal outcome — make it visually dominant with the vermillion fill and a bold DEAD label while the three survivable cells share a calm green. Add a short mechanism annotation in each cell. The teaching point: two individually survivable defects are lethal only in combination. Subtitle: "Only the double-defect corner is lethal." Okabe-Ito semantics: green for the three live cells, vermillion for the single lethal cell. Deliverable: single standalone HTML file, inline CSS, D3 v7 pinned CDN, Okabe-Ito colorblind-safe palette via CSS variables.

### Figure 6.3 — Two-hit hypothesis: retinoblastoma, inherited vs sporadic
Build a two-panel comparison, left panel "Inherited," right panel "Sporadic," with a paired-eye clinical outcome at the bottom of each, under axis label "Retinoblastoma onset." Three aligned rows: (1) "Every retinal cell carries one germline-defective allele" vs "All cells start fully intact" (secondary) — show allele-box glyphs, one pre-hit on the inherited side; (2) "Single second hits transform multiple cells" vs "Two independent hits required in one cell (rare)" (vermillion, the probability driver); (3) "Bilateral, multifocal, early onset" vs "Unilateral, single tumor, later onset" (sky-blue anchor, the clinical payoff). Include a small paired-eyes icon per panel: both eyes affected with multiple foci on the inherited side, one eye single tumor on the sporadic side. Subtitle: "Germline first hit yields bilateral, multifocal disease." Okabe-Ito semantics: vermillion for the single-hit shortcut, sky-blue anchor for the clinical outcome row. Deliverable: single standalone HTML file, inline CSS, D3 v7 pinned CDN, Okabe-Ito colorblind-safe palette via CSS variables.

### Figure 6.4 — APC and the Wnt destruction complex (two-state switch)
Build a two-state before/after comparison, left "APC intact (Wnt off)," right "APC lost," under axis label "beta-catenin fate." Three aligned rows: (1) "Destruction complex (APC+Axin+GSK-3b+CK1) active" vs "destruction complex cannot form" (green left, the working brake); (2) "beta-catenin phosphorylated → degraded" vs "beta-catenin accumulates, enters nucleus" (sky-blue anchor, the pivotal molecule); (3) "Quiet nucleus" vs "drives MYC, cyclin D1 → proliferation" (vermillion right, negative outcome). On the left panel draw the assembled four-protein destruction complex tagging beta-catenin for degradation; on the right panel show the complex dissolved and beta-catenin translocating into the nucleus to fire target genes. Clean mirrored before/after layout. Subtitle: "Lose APC, and beta-catenin drives proliferation unchecked." Okabe-Ito semantics: green for the intact brake, sky-blue anchor for beta-catenin, vermillion for the proliferation outcome. Deliverable: single standalone HTML file, inline CSS, D3 v7 pinned CDN, Okabe-Ito colorblind-safe palette via CSS variables.
