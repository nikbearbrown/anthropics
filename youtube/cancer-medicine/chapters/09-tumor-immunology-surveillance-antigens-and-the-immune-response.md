# Chapter 9 — Tumor Immunology: Surveillance, Antigens, and the Immune Response
*Why the cancer you can see is the one that won an evolutionary contest you never knew was happening.*

The kidney donor had melanoma fifteen years before she died. It was treated, and declared cured. By every available measure it was gone. When her kidneys were transplanted into a recipient who then began lifelong immunosuppression, something happened that no one had anticipated: the recipient developed melanoma. Not a new primary tumor arising from her own cells — the cells were the donor's. Melanoma cells that had been, apparently, sitting dormant somewhere in the donor's tissue for fifteen years, kept silent by the donor's immune surveillance, re-emerged once they were transplanted into a body whose immune defenses were deliberately switched off.

Nothing about the cancer cells changed. What changed was who was watching them.

This case is not a curiosity. It is a clean natural experiment that answers a question immunologists had argued about for most of the twentieth century: can the immune system genuinely hold cancer in check, not by eliminating it but by containing it, for years? The answer is yes. And the follow-up question — which is what this chapter is built on — is: if containment is real, what is the immune system recognizing, and why does that recognition eventually fail?

---

### The idea that was too intuitive to trust

Paul Ehrlich gestured at immunological tumor control in 1909. Lewis Thomas and Macfarlane Burnet developed it into a formal hypothesis in the 1950s and 1970s. The claim was simple: the immune system continuously inspects the body's own cells, identifies those that have turned cancerous, and destroys them before they become detectable tumors. The word for this is **immunosurveillance**, and for decades the evidence for it was frustratingly indirect.

The problem was that cancer is common. If the immune system were surveilling and eliminating transformed cells, why did so many people get cancer at all? The easy objection was that surveillance must fail far more than it succeeds, in which case calling it "surveillance" was generous. The evidence that shifted the field was experimental rather than epidemiological. When geneticists engineered mice lacking functional T and B cells — RAG2-knockout mice, which cannot complete lymphocyte development — those mice developed spontaneous tumors at elevated rates and responded to carcinogens more dramatically than immunocompetent controls. Remove the watchers, and the cancers appear. Separately, mice lacking the interferon-γ response, or lacking perforin (the pore-forming protein through which cytotoxic cells kill), showed the same pattern. Each component of the immune killing machinery, when disabled, made tumors more frequent and more aggressive.

In humans the same logic plays out in the clinic. Transplant recipients on chronic immunosuppression have elevated rates of cancer — most dramatically the virally driven ones, where the immune system is simultaneously containing both the cancer cell and the oncogenic virus that drives it. People with HIV/AIDS, before effective antiviral therapy, showed extraordinary rates of Kaposi's sarcoma and certain lymphomas. The donor-derived melanoma case is simply one of the starkest illustrations of a general principle the epidemiology had already established.

But the simple surveillance hypothesis — immune system watches, eliminates, success — was too simple. The transplant case showed why: containment for fifteen years is not elimination. A more nuanced framework was needed.

---

### Immunoediting: the immune system sculpts what it cannot destroy

The modern refinement is **cancer immunoediting**, described by Dunn, Schreiber, and colleagues in 2002. It reframes the immune system's relationship to a developing cancer not as binary success or failure but as a dynamic, three-phase process.

**Elimination** is classical surveillance: the immune system recognizes and destroys most transformed cells before they form a tumor. This is the phase Ehrlich and Burnet imagined. Most transformed cells probably end here.

**Equilibrium** is what the transplant case made visible. Some cells survive elimination by acquiring partial resistance. They are not destroyed, but they are not expanding either — they are held in check by ongoing immune pressure. Dormant. This phase can last years or decades. The donor's melanoma cells persisted in equilibrium for fifteen years.

**Escape** is what we observe when we diagnose cancer. A variant acquires changes that let it evade immune pressure entirely. It expands. The equilibrium breaks. The tumor becomes clinically visible.

The word "editing" is the insight. The immune system is not just failing when cancer escapes — it is, in the process of eliminating the most visible cells, *selecting for* the less visible ones. Every cancer cell the immune system successfully kills is one that expressed something recognizable. The cells that survive are, by selection, the ones that were harder to see, or harder to kill, or better at suppressing the response. The tumor that finally escapes is almost by definition one that has been shaped by immune pressure toward invisibility. A cancer diagnosis is the endpoint of an evolutionary contest. You are seeing the winner.

This reframing has a disquieting corollary. A more effective immune response — one that eliminates more cells in earlier phases — applies more selection pressure and may produce, in the cells that survive, a more aggressively evasive tumor. The immune system that does the best job at surveillance also does the most editing. This is not an argument against immunosurveillance; it is an argument for understanding what makes cells recognizable before the editing goes too far.

![Three-phase immunoediting arc: elimination, equilibrium, escape](images/09-tumor-immunology-surveillance-antigens-and-the-immune-response-fig-02.png)
*Figure 9.2 — Cancer immunoediting: elimination, equilibrium, escape*

<!-- → [DIAGRAM: cancer immunoediting — three-phase arc showing a population of transformed cells. Phase 1 (Elimination): immune cells clearing most transformed cells. Phase 2 (Equilibrium): a small dormant population held in check, balanced arrows between immune pressure and tumor persistence. Phase 3 (Escape): a resistant clone expanding past immune control. Annotate the evolutionary selection dynamic: eliminated cells = visible, escaping cells = edited toward invisibility.] -->

---

### What makes a cell visible: the antigen problem

For the immune system to recognize a cancer cell, the cell must display something that marks it as different. A **tumor antigen** is any molecule a cancer cell presents — usually as a peptide fragment on MHC — that an immune cell can recognize as a target. The distinction that matters practically is whether that molecule exists anywhere in normal tissue.

**Tumor-specific antigens** exist only on cancer cells, never on normal tissue. They are the cleanest targets: an immune response against them cannot, in principle, damage healthy cells. Two sources.

The first is viral antigens. When an oncogenic virus transforms a cell, viral proteins are expressed and displayed on MHC — and the immune system has never been taught to tolerate them. HPV-transformed cervical and oropharyngeal cancer cells display the E6 and E7 oncoproteins on MHC class I. EBV-transformed lymphoma cells display EBV antigens. These are genuinely foreign, and the immune response against them is unconstrained by any tolerance mechanism.

The second source is neoantigens — peptides arising from cancer-specific somatic mutations. When a point mutation changes one amino acid in a protein, the resulting peptide may be one the immune system has never encountered. Neoantigens are personal: each patient's tumor generates a largely private set. They are also, mechanistically, the most attractive targets in immunotherapy, for a reason that requires understanding how T cells are educated.

**Tumor-associated antigens** are expressed on cancer cells but also — usually at lower levels, or in restricted tissue contexts — on normal cells. The immune system has partial tolerance to them. Targeting them produces an anti-tumor effect but also collateral damage to whatever normal tissue shares the target. Cancer-testis antigens like NY-ESO-1 and MAGE-A1 are normally restricted to germ cells, which are immunologically privileged — so they behave nearly like tumor-specific antigens, but not quite. Differentiation antigens like tyrosinase (in melanocytes) or CD19 and CD20 (in all B cells) are shared with normal tissue. CD19-targeted therapies reliably eliminate normal B cells alongside malignant ones — a toxicity that is, fortunately, survivable. PSA is expressed in normal prostate as well as prostate cancer. HER2 is expressed at low levels in normal breast and cardiac tissue; its overexpression in amplified tumors makes it a useful target but not an entirely safe one.

The practical question to ask of any antigen is simple: what normal tissue shares this target, and what happens when the immune response hits it? The answer is the toxicity prediction. Attack something truly tumor-specific — a private neoantigen — and the only collateral damage is to tumor cells. Attack a differentiation antigen expressed on a tissue the body needs, and the therapy is bounded by what that tissue loss costs.

---

### Why neoantigens escape central tolerance

The immune system contains T cells capable of recognizing almost any peptide — including the peptides on cancer cells. So why does it not always attack? The answer is tolerance, and understanding tolerance is what makes the neoantigen concept mechanistically coherent rather than just empirically useful.

During development in the thymus, T cells whose receptors bind strongly to the body's own peptides are deleted. This **central tolerance** is how a healthy immune system avoids attacking normal tissue: every self-peptide is represented, and T cells that recognize self-peptides with high affinity are eliminated before they mature. The result is a T-cell repertoire that is, in principle, tolerant to every protein a normal cell expresses.

Tumor-associated antigens are self-proteins expressed at higher levels or in aberrant locations. Central tolerance to them is partial — some self-reactive T cells escape deletion, but their activation thresholds are raised by peripheral tolerance mechanisms. Targeting TAAs means pushing against that tolerance, which is possible but requires help — adjuvants, checkpoint inhibition, the engineering of high-affinity T-cell receptors.

Neoantigens were never present in the thymus. A peptide arising from a somatic mutation that occurred after thymic education is a peptide that was never evaluated during T-cell selection. T cells capable of recognizing it survived thymic selection intact, with no tolerance imposed. This is why neoantigens are so attractive: they can be targeted without first overcoming the brakes the body deliberately placed on the immune response to protect normal tissue. They are foreign in the only sense that matters to a T cell.

The number of neoantigens a tumor offers scales directly with how many mutations it carries — its **tumor mutational burden (TMB)**. More mutations, more chances for novel peptides. Tumors with very high TMB — melanomas with UV signatures, lung cancers from tobacco carcinogens, mismatch-repair-deficient colorectal cancers, POLE-mutant cancers — generate large neoantigen pools. Pediatric cancers and many leukemias, arising with very few mutations, generate almost none. This is the mechanistic root of why TMB has emerged as a predictor of immune-based therapy response: more targets, more potential T-cell recognition. But TMB sits at the top of a long chain, and any step in the chain can fail.

![A post-thymic mutant peptide finds an undeleted T cell that survived central tolerance](images/09-tumor-immunology-surveillance-antigens-and-the-immune-response-fig-03.png)
*Figure 9.3 — Neoantigen generation escapes central tolerance*

<!-- → [DIAGRAM: neoantigen generation and central tolerance — left panel: thymic education deleting self-reactive T cells (self-peptide/MHC → T cell deletion); center: a somatic mutation in a tumor cell producing a novel peptide; right: the novel peptide presented on MHC class I, recognized by a non-deleted T cell. Annotate: no tolerance to this peptide, T cell survives to respond.] -->

---

### The chain from recognition to killing

An effective adaptive anti-tumor response runs through a sequence of linked steps. Chen and Mellman drew this as the *cancer-immunity cycle* in 2013, and it is the most useful framework for understanding both how the response works and where it breaks.

The cycle opens when cancer cells die — from spontaneous apoptosis, from therapy, from necrosis — and release antigens into the tumor microenvironment. **Dendritic cells** take up the debris, process it, and load peptide fragments onto MHC class I (for CD8+ T cells) and MHC class II (for CD4+ T cells).

The dendritic cell then migrates to a draining lymph node and matures — upregulating its MHC molecules, its co-stimulatory ligands CD80 and CD86, and its cytokine production. In the lymph node it presents to naïve T cells. Activation requires two signals in parallel: the T-cell receptor binding the antigen–MHC complex (signal 1), and co-stimulation through CD28 binding CD80 or CD86 (signal 2). A T cell that receives signal 1 without signal 2 does not become activated — it becomes anergic, functionally silenced. IL-12 and other cytokines from the dendritic cell provide a third signal that shapes the character of the response.

Activated T cells expand enormously — a single antigen-specific clone can produce thousands of daughters — and then follow chemokine gradients out of the lymph node and toward the tumor. CXCL9, CXCL10, and CXCL11, produced in the tumor, guide them in. At the tumor, CTLs bind cancer cells displaying their specific antigen on MHC class I and kill through two mechanisms: **perforin/granzyme** (the CTL releases pore-forming proteins and apoptosis-inducing enzymes into the cancer cell) and **death-receptor ligation** (FasL on the CTL binds Fas on the cancer cell, triggering apoptosis). A single CTL can kill multiple targets sequentially before dying itself. A subset of activated T cells survives as long-lived memory cells, poised to respond faster to a second exposure.

![The six-step cancer-immunity cycle, from antigen release to CTL killing and back](images/09-tumor-immunology-surveillance-antigens-and-the-immune-response-fig-01.png)
*Figure 9.1 — The cancer-immunity cycle*

<!-- → [DIAGRAM: the cancer-immunity cycle as a loop — six labeled steps: (1) antigen release from dying tumor cells; (2) dendritic cell uptake and MHC loading; (3) DC migration to lymph node, maturation, T-cell priming (signal 1 + signal 2 both required); (4) T-cell expansion and trafficking via CXCL9/10/11; (5) tumor infiltration; (6) CTL killing via perforin/granzyme and FasL/Fas. Annotate each step with one way a tumor can break it.] -->

The chain is robust when intact, but each link is a place a tumor can sever it. Defective antigen processing breaks step 2. Failure to mature dendritic cells breaks step 3. Absence of chemokine expression breaks step 4. Dense matrix and abnormal vasculature block step 5. Checkpoint ligand expression suppresses the CTL in step 6. The cancer-immunity cycle is the map of the battleground.

---

### When T cells are not enough: NK cells and missing-self recognition

CD8+ T cells are the primary adaptive killers, but they have a vulnerability: they require antigen presentation on MHC class I. A tumor that downregulates MHC — and many do, because it hides cancer-specific peptides from T cells — has found a way to become invisible to CTLs. It has also, in doing so, set a trap for itself.

**Natural killer (NK) cells** patrol for cells that have downregulated MHC class I. The mechanism is **missing-self recognition**: NK cells express inhibitory receptors (KIRs and NKG2A) that are normally engaged by MHC class I on healthy cells, sending a "do not kill" signal. When MHC is absent or reduced, that inhibitory signal is lost, and the NK cell defaults to killing. A tumor that hides from T cells by removing MHC has simultaneously removed the brake on NK-cell attack. This is not a coincidence of design — it is precisely the kind of cross-monitoring that makes immune evasion harder.

![Losing MHC class I to hide from T cells removes the inhibitory signal and exposes the cell to NK killing](images/09-tumor-immunology-surveillance-antigens-and-the-immune-response-fig-04.png)
*Figure 9.4 — Missing-self recognition: NK cells and the MHC trap*

NK cells also recognize cells displaying stress ligands — MICA, MICB, and the ULBP family — which are expressed on transformed cells in response to genotoxic stress, replication errors, and oncogene activation. These ligands signal through NKG2D on NK cells (and on some CTLs) to trigger killing independently of antigen presentation.

The practical consequence for therapy is direct: a treatment strategy based on potentiating T-cell killing will be insufficient in a tumor that has lost MHC class I. The limiting effector for that tumor is the NK cell, and the relevant question shifts from "how do we present antigen better" to "how do we activate NK cells in the tumor microenvironment."

---

### The broken link that predicts failure

The worked example in the source material for this chapter describes two patients: one whose tumor responds to checkpoint-releasing therapy and one whose does not, despite having *higher* tumor mutational burden. The resolution is that the second tumor is not failing because it lacks targets — it is failing because it has excluded T cells physically. The cells are present in the blood and at the tumor margin; they simply cannot penetrate. Dense matrix and aberrant vessels form a wall between the immune infiltrate and the cancer cells.

This is worth dwelling on because it illustrates the central mistake in applying population-level correlations to individual patients. TMB predicts response on average because, on average, more mutations mean more targets, and more targets mean more T-cell priming. But TMB is the input to a chain, and the chain has six links. A tumor can have abundant targets and still fail because dendritic cells are dysfunctional, or because the vasculature does not express the right trafficking chemokines, or because the matrix is impenetrable, or because checkpoints are saturated once T cells do arrive. The limiting step in the chain — not the average potential — decides the outcome. Finding the broken link in a specific patient requires walking the cycle, not reading a single number.

The immunotherapy revolution of the last decade — checkpoint blockade — worked where it worked by releasing step 6: removing an inhibitory signal on a T cell that was already present, primed, and blocked from firing. The tumors that respond best are ones in which the only broken link was the checkpoint brake. The tumors that do not respond have broken links elsewhere in the cycle, and releasing a brake does nothing for a chain that is already cut upstream.

---

## Exercises

**Warm-up**

1. *(Recall — difficulty: low)* State the three phases of cancer immunoediting and give one piece of evidence for each phase. For the equilibrium phase specifically, explain why the donor-derived melanoma case is evidence for equilibrium rather than for elimination. *What this tests: whether you can distinguish the three phases and use the chapter's central case correctly.*

2. *(Recall — difficulty: low)* For each of these antigens — HPV E7, CD19, tyrosinase, HER2, a private neoantigen — name the normal tissue that shares the target (if any) and predict the on-target toxicity of a therapeutic immune response against it. *What this tests: the TSA vs. TAA distinction applied to specific clinical targets.*

3. *(Recall — difficulty: low)* Why does a tumor that downregulates MHC class I to evade CD8+ T cells expose itself to NK-cell killing? Name the recognition mechanism NK cells use and the specific molecular event that removes the "do not kill" signal. *What this tests: missing-self recognition as the complement to MHC-restricted surveillance.*

**Application**

4. *(Apply — difficulty: medium)* A high-TMB tumor does not respond to a checkpoint inhibitor. Walk through the cancer-immunity cycle and propose three mechanistically distinct explanations — each located at a different step — for why the response fails despite abundant neoantigens. For each explanation, name one measurement on a biopsy or blood sample that would confirm or rule it out. *What this tests: cycle-based mechanistic reasoning and the limits of TMB as a predictor.*

5. *(Apply — difficulty: medium)* A T cell in the thymus encounters a peptide derived from tyrosinase (a normal melanocyte protein) displayed on MHC class I. What happens to this T cell, and why? Now suppose a point mutation in a melanoma cell produces a novel peptide adjacent to the tyrosinase peptide sequence. Does the same mechanism apply to a T cell that recognizes the mutant peptide? Explain the difference in terms of central tolerance. *What this tests: the mechanistic basis for why neoantigens are preferential targets.*

6. *(Apply — difficulty: medium)* A cancer cell in equilibrium has been held in check for eight years. Propose three distinct mechanisms by which it could acquire escape — one involving antigen presentation, one involving the co-stimulatory signal, and one involving the effector phase. For each, name the specific molecular change in the cancer cell or the microenvironment. *What this tests: mechanistic specificity about how each phase of the cycle can be broken.*

**Synthesis**

7. *(Synthesize — difficulty: high)* Draw or describe the immunoediting framework as an evolutionary process. Show how the elimination phase applies selection pressure that enriches for immune-evasion phenotypes, and explain why the tumor that escapes is almost by definition a more edited, less visible version of its ancestors. Then connect this to the neoantigen concept: if neoantigens are the targets immune pressure selects against, what does a high-TMB escaped tumor reveal about the relationship between mutation load and antigen visibility? *What this tests: integration of immunoediting, selection pressure, and neoantigen biology as a single evolutionary argument.*

8. *(Synthesize — difficulty: high)* A patient has a tumor classified as "excluded" — abundant T cells at the margin, almost none inside. Using the cancer-immunity cycle, identify which step is broken and which are intact. Then: (a) explain why checkpoint blockade alone is unlikely to be sufficient, and (b) propose a two-part combination strategy that addresses both the exclusion problem and a second likely broken link in the same tumor type. Justify each arm mechanistically. *What this tests: step-specific diagnosis of immune failure and combination logic.*

**Challenge**

9. *(Challenge — difficulty: high)* Design a hypothetical personalized vaccine strategy for a patient with a high-TMB microsatellite-instability-high colorectal cancer. Specify: (a) how you would identify target neoantigens, (b) what formulation or delivery approach would most effectively prime dendritic cells, (c) what co-treatment would address the most likely step-specific failure you would anticipate in this tumor type, and (d) what you would measure at weeks 4, 8, and 16 to determine whether each step of the cycle is functioning. Identify the single biggest unknown in your design and what clinical data would resolve it. There is no single correct answer; mechanistically coherent reasoning with honest acknowledgment of limits is the goal. *What this tests: integrative design across the full cancer-immunity cycle, connecting antigen biology, dendritic cell priming, T-cell trafficking, and measurement strategy.*

---

## Prompts

### Figure 9.1 — The cancer-immunity cycle
Build a closed-loop cycle diagram with six nodes arranged clockwise around a ring, each connected to the next by a curved arrow that returns to the start. Nodes in order: (1) "Antigen release from dying tumor cell" (secondary); (2) "DC uptake and MHC loading" (sky-blue, anchor); (3) "DC migration and T-cell priming" (sky-blue, anchor); (4) "T-cell expansion and trafficking" (green, positive); (5) "T-cell infiltration of tumor" (green, positive); (6) "CTL killing of tumor cell" (vermillion). The arrow from node 6 returns to node 1, emphasizing that killing feeds new antigen release. Marks: labeled circular nodes, curved directional arrows forming the loop, a center label "Cancer-immunity cycle." Color semantics (Okabe-Ito): sky-blue = antigen-presentation anchor steps, green = T-cell activation/trafficking, vermillion = the killing step. Closed loop, no axis. Deliverable: single standalone HTML file, inline CSS, D3 v7 pinned CDN, Okabe-Ito colorblind-safe palette via CSS variables.

### Figure 9.2 — Cancer immunoediting: elimination, equilibrium, escape
Build a left-to-right three-phase process arc tracking a population of transformed cells across time. Phase 1 "Elimination": immune cells clear most transformed cells (green, positive) — population shrinks sharply. Phase 2 "Equilibrium": a few survivors held in a dormant standoff (~15 yr) — population flat, balanced opposing arrows between immune pressure and tumor persistence. Phase 3 "Escape": an edited variant breaks out and expands past immune control (vermillion, negative) — population rises. Overlay a population-count band across all three phases so the shrink-hold-grow shape is visible. Add a note: "Selective immune pressure edits the population toward less-visible variants." Marks: three labeled phase panels, two connecting arrows, a population envelope, opposing-arrow motif in phase 2. Color semantics (Okabe-Ito): green = elimination/positive, neutral = equilibrium standoff, vermillion = escape/negative. Deliverable: single standalone HTML file, inline CSS, D3 v7 pinned CDN, Okabe-Ito colorblind-safe palette via CSS variables.

### Figure 9.3 — Neoantigen generation escapes central tolerance
Build a three-panel left-to-right mechanistic schematic. Panel 1 "Thymus": a self-peptide on MHC contacting a T cell, with the T cell marked deleted (vermillion, negative) — central tolerance removes self-reactive T cells. Panel 2 "Tumor": a point mutation in a protein yielding a novel peptide shape (neutral/emphasis). Panel 3 "Response": the novel peptide on MHC class I contacting a surviving T cell that fires (green, positive). Connect panels with two rightward arrows. Add a banner note: "The mutant peptide was never present during thymic selection, so its T cell was never deleted." Marks: peptide/MHC/T-cell glyphs per panel, deletion mark in panel 1, activation mark in panel 3, two flow arrows. Color semantics (Okabe-Ito): vermillion = deletion/tolerance, green = the surviving productive response, sky-blue = the novel peptide as anchor element. Deliverable: single standalone HTML file, inline CSS, D3 v7 pinned CDN, Okabe-Ito colorblind-safe palette via CSS variables.

### Figure 9.4 — Missing-self recognition: NK cells and the MHC trap
Build a two-panel before/after comparison contrasting an NK cell's response to two target cells. Left panel "MHC-positive cell": surface MHC class I tabs present (sky-blue, anchor), the inhibitory "do not kill" signal engaged, NK cell remains inactive. Right panel "MHC-negative tumor cell": surface MHC tabs absent, inhibitory signal lost (vermillion, negative), NK cell attacks and kills (green, positive). Use three aligned rows so the panels read row-for-row: MHC status, inhibitory signal state, NK outcome. Marks: target-cell glyph with/without MHC tabs, an NK cell with an inhibitory-receptor contact, outcome label. Color semantics (Okabe-Ito): sky-blue = present MHC/anchor, vermillion = lost inhibitory signal, green = NK killing/positive. Structural contrast, no axis. Deliverable: single standalone HTML file, inline CSS, D3 v7 pinned CDN, Okabe-Ito colorblind-safe palette via CSS variables.
