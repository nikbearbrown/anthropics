# Chapter 15 — Cancer Metabolism: The Warburg Effect and Glucose
*Why a cell that could extract thirty units of energy from a sugar deliberately extracts two — and what that tells us about what proliferation actually requires.*

The patient is injected with a radioactive glucose analog and slid into the PET scanner. An hour later the images come back. The brain glows — it always does, burning glucose constantly. The bladder glows — the tracer drains there. And then, in the chest, a cluster of lymph nodes glows that should be dark. No normal lymph node takes up glucose at that rate. The bright spots are cancer.

This is a routine clinical tool, used every day. And if you stop to think about what it is showing, it should be puzzling. The tumor is consuming glucose voraciously — that much is obvious from the image. But here is what the image does not tell you: the tumor is not burning most of that glucose for energy. It is converting most of it to lactate and excreting the lactate as waste. It is extracting roughly two ATP from each glucose molecule when, with the oxygen freely available to it, it could extract thirty.

No engineer designing for energy efficiency would do this. And yet many cancers, in many patients, across many settings, do exactly this. Either those cancer cells are extraordinarily bad at a simple biochemical problem, or they are solving a different problem than the one we assumed.

They are solving a different problem. This chapter is the explanation.

---

### What glycolysis does and where it ends

Glycolysis is a ten-step pathway in the cell's cytoplasm that splits one glucose molecule — six carbons — into two pyruvate molecules of three carbons each. The net yield is two ATP and two NADH. No oxygen required; no mitochondria involved.

What happens to pyruvate depends on the cell's situation. Two destinations, completely different consequences.

**Destination one: the mitochondrion.** In a cell with oxygen, pyruvate is imported into the mitochondrial matrix, converted to acetyl-CoA by pyruvate dehydrogenase, and fed into the citric acid cycle. The cycle extracts electrons, passes them through the respiratory chain, uses oxygen as the final electron acceptor, and drives the synthesis of roughly 30–32 ATP per original glucose. This is complete oxidation — every carbon in the glucose molecule leaves eventually as carbon dioxide. Maximum energy extracted, maximum carbon discarded.

**Destination two: lactate.** Without oxygen, the electron transport chain stalls — there is no oxygen to accept electrons, so the chain backs up. The cell needs a way to regenerate NAD⁺ (consumed by glycolysis) or glycolysis itself will stall. The solution is to use pyruvate as an electron acceptor: lactate dehydrogenase reduces pyruvate to lactate, regenerating NAD⁺ in the process. The cell excretes the lactate. Net yield: two ATP per glucose, and a pile of lactate waste.

Otto Warburg measured this in tumor tissue in the 1920s — high lactate production, even in the presence of oxygen — and proposed the explanation that seemed obvious at the time: the mitochondria must be damaged. Forced to ferment because oxidation is unavailable. He was half right about the observation and entirely wrong about the mechanism. The mitochondria, in most cancer cells, are not damaged. They are running. The lactate is not a failure of oxidation; it is a choice.

---

### Why the choice makes sense: the cell is building, not burning

The key to the Warburg effect is recognizing what a dividing cell is actually trying to do.

A quiescent cell — a neuron, a muscle fiber at rest, a liver cell not under stress — has one primary metabolic demand: generate enough ATP to power its maintenance functions. For this cell, extracting thirty ATP from each glucose is optimal. Oxidize completely, maximize yield, discard all the carbon as CO₂.

A proliferating cell has a fundamentally different demand. It is not just powering itself; it is **building a second copy of itself**. That requires an enormous supply of raw materials: nucleotides for a new genome, lipids for new membranes, amino acids for new proteins. Where do all those materials come from? Carbon. The same carbon that is in glucose.

Here is the problem with complete oxidation for a proliferating cell: every carbon that enters the citric acid cycle and leaves as CO₂ is a carbon that is *not available for building*. The cell breathed out its building material. For a cell that needs to double its biomass before dividing, complete oxidation of glucose is carbon waste, not carbon efficiency.

By stopping glycolysis at pyruvate and excreting the carbon as lactate instead, the cell preserves carbon at the branch points where biosynthesis departs from the main metabolic highway. Glucose carbon flows into **ribose-5-phosphate** (via the pentose phosphate pathway, for nucleotide synthesis), into **serine and glycine** (from 3-phosphoglycerate, for one-carbon metabolism and nucleotide synthesis), into **acetyl-CoA** and **glycerol-3-phosphate** (for lipid synthesis). These carbon diversions happen before or alongside the lactate step. The lactate that is excreted is the carbon the cell did not need for building — excess reduced carbon dumped to maintain redox balance.

This reframing — proposed with clarity by Matthew Vander Heiden, Lewis Cantley, and Craig Thompson in 2009 — is the modern understanding of the Warburg effect. The cell is not bad at energetics. It is treating glucose primarily as a **carbon source for biosynthesis**, not as an energy source. The "inefficiency" in ATP per glucose is not a failure; it is the cost of a carbon-allocation strategy. The cell compensates for the low ATP yield from glycolysis with high glucose uptake (hence the PET scan) and by oxidizing *other* fuels — glutamine, fatty acids — in its mitochondria for the ATP it still needs.

![Branching carbon-fate map: glucose forms a glycolytic trunk that branches into ribose-5-phosphate for nucleotides, serine/glycine for one-carbon units, acetyl-CoA for fatty acid synthesis, and excreted lactate for redox balance — carbon fans out rather than being fully oxidized to CO2.](images/15-cancer-metabolism-the-warburg-effect-and-glucose-fig-01.png)
*Figure 15.1 — Carbon fate map for a proliferating cell*

<!-- → [DIAGRAM: carbon fate map for a proliferating cell. Central trunk: glucose → glucose-6-phosphate → pyruvate → lactate (main glycolytic flow). Branch 1 off glucose-6-phosphate: pentose phosphate pathway → ribose-5-phosphate (label: nucleotides). Branch 2 off 3-phosphoglycerate: → serine → glycine (label: one-carbon metabolism, nucleotide synthesis). Branch 3 off pyruvate via acetyl-CoA: → fatty acid synthesis (label: membranes). Branch 4: lactate excreted (label: carbon waste / redox balance). The visual point is that glucose carbon fans into multiple biosynthetic destinations rather than funneling entirely to CO2.] -->

---

### Mitochondria: repurposed, not broken

The "broken mitochondria" explanation is wrong, and it is worth being direct about this because it is both common and consequential for how the metabolism of cancer is understood.

In most cancer cells, mitochondria are structurally and functionally intact. They produce ATP. They run the citric acid cycle. They synthesize lipids. They regulate calcium. They sit at the hub of the intrinsic apoptosis pathway. The cancer cell needs them. What changes is *what they are running on and what they are producing* — not whether they function.

The repurposed roles look like this. The citric acid cycle, rather than running closed to maximize ATP from glucose, runs **anaplerotic** — fed with carbon from glutamine (described in the next chapter) to replace the intermediates the cell exports for biosynthesis. Citrate is exported from the mitochondrion to the cytoplasm, where it is cleaved to produce acetyl-CoA for fatty acid synthesis. Alpha-ketoglutarate is used for amino acid synthesis and, in some cancers, accumulates as an oncometabolite when isocitrate dehydrogenase is mutated. Oxaloacetate is tapped for aspartate synthesis, which feeds nucleotide production. The cycle has become a precursor-export machine as much as an energy-generating one.

Mitochondria also remain the primary source of ATP when glucose is being diverted to biosynthesis. The oxidation of glutamine and fatty acids in the mitochondrial matrix fills the energy budget that glucose is no longer covering. In some cancer types — those that arise in tissues with high fatty acid availability, like some prostate cancers, or those that are under glucose limitation in the tumor microenvironment — OXPHOS dependence is actually *higher* than in normal tissue, not lower. The idea that all cancers rely on glycolysis and spare their mitochondria is the oversimplification of a more complex, context-dependent picture.

The one apoptotic role of mitochondria that cancer consistently suppresses is the release of cytochrome c — the initiating step of intrinsic apoptosis. The cell keeps the electron transport chain running for ATP while ensuring that the outer membrane does not permeabilize to release the apoptotic signal. Bcl-2 family members, overexpressed in many cancers, hold the outer membrane closed. This is not mitochondrial dysfunction; it is selective suppression of one mitochondrial output while preserving all others.

![Annotated cross-section of an intact but repurposed mitochondrion: the citric acid cycle exports citrate for fatty acid synthesis, α-ketoglutarate for amino acids, and oxaloacetate-derived aspartate for nucleotides, is refilled by glutamine anaplerosis, runs the electron transport chain for ATP, and keeps the outer membrane clamped shut by BCL-2 against cytochrome c release.](images/15-cancer-metabolism-the-warburg-effect-and-glucose-fig-03.png)
*Figure 15.3 — Repurposed mitochondria: cycle as precursor-export machine*

<!-- → [DIAGRAM: repurposed mitochondria in a cancer cell — citric acid cycle in the center with arrows exiting for: citrate → cytoplasm → fatty acid synthesis; α-ketoglutarate → amino acids; oxaloacetate → aspartate → nucleotides. Glutamine entering the cycle as anaplerotic carbon source. Electron transport chain running for ATP. Outer membrane with Bcl-2 proteins blocking cytochrome c release. Label: "running for biosynthesis and energy; apoptotic output suppressed."] -->

---

### HIF-1α: how the cell senses and responds to oxygen shortage

Tumors grow faster than their blood supply can follow. The expanding mass outpaces angiogenesis, and cells deep in the tumor or at its leading edge find themselves in regions of genuinely low oxygen — **hypoxia**. Hypoxia is not simply the absence of oxygen; it is a signaling state. The cell has a dedicated sensor that detects low oxygen and launches a transcriptional program that reprograms metabolism, stimulates angiogenesis, and promotes survival.

The sensor is **hypoxia-inducible factor 1α (HIF-1α)**.

In well-oxygenated conditions, a family of enzymes called **prolyl hydroxylases (PHDs)** continuously hydroxylate two proline residues on HIF-1α. Hydroxylated HIF-1α is recognized by the **von Hippel–Lindau (VHL)** protein, an E3 ubiquitin ligase component, which tags HIF-1α for proteasomal destruction. The half-life of HIF-1α in well-oxygenated cells is roughly five minutes; it is made and immediately destroyed. Functionally absent.

PHDs require oxygen as a substrate. When oxygen drops, PHDs stall. HIF-1α is made but not hydroxylated, and therefore not recognized by VHL and not destroyed. It accumulates, dimerizes with its partner HIF-1β, and drives transcription of a large set of target genes: glucose transporters (GLUT1, GLUT3) to increase glucose uptake, glycolytic enzymes (aldolase, enolase, phosphoglycerate kinase) to increase glycolytic flux, **PDK1** (which phosphorylates and inhibits pyruvate dehydrogenase, blocking pyruvate's entry to the citric acid cycle and pushing it toward lactate), MCT4 (the lactate exporter), and **VEGF** (to stimulate new blood vessel growth toward the hypoxic region).

In a single oxygen-sensing cascade, the cell simultaneously upregulates glucose import, glycolytic processing, lactate export, and the angiogenic signal to fix the problem. The HIF response is elegant precisely because it connects the metabolic reprogramming (more glycolysis, less OXPHOS) to the vascular response (more VEGF) through a single transcription factor.

HIF-1α can also be stabilized without any hypoxia, through oncogenic signaling. Activated PI3K–AKT–mTOR signaling increases HIF-1α translation. Succinate dehydrogenase mutations cause succinate accumulation, which inhibits PHDs by product inhibition, stabilizing HIF-1α. KRAS and MYC activation increase HIF-1α transcription and translation. In these cases the HIF program runs constitutively in a well-oxygenated cell — pseudohypoxia — driven not by oxygen shortage but by upstream oncogenic signaling that mimics the low-oxygen state.

![Two-state comparison of HIF-1α fate: in normoxia prolyl hydroxylases tag HIF-1α for VHL-mediated proteasomal destruction within minutes, while in hypoxia the hydroxylases stall, HIF-1α escapes VHL, accumulates, dimerizes with HIF-1β, and transcribes GLUT1, PDK1, MCT4, and VEGF.](images/15-cancer-metabolism-the-warburg-effect-and-glucose-fig-02.png)
*Figure 15.2 — HIF-1α oxygen sensing: normoxia versus hypoxia*

<!-- → [DIAGRAM: HIF-1α oxygen-sensing pathway. Left panel: normoxia — PHDs active → HIF-1α hydroxylated → VHL binds → ubiquitin ligase → proteasomal degradation. HIF-1α half-life ~5 min. Right panel: hypoxia — PHDs stall (no O2 substrate) → HIF-1α not hydroxylated → escapes VHL → accumulates → dimerizes with HIF-1β → nucleus → target gene transcription (GLUT1, glycolytic enzymes, PDK1, MCT4, VEGF). Below: oncogenic stabilization routes — PI3K/mTOR increasing translation, succinate/fumarate accumulation inhibiting PHDs, KRAS/MYC transcriptional upregulation.] -->

---

### VHL loss and pseudohypoxia: what clear cell renal carcinoma teaches

The clearest example of constitutive HIF activation by non-hypoxic means is clear cell renal cell carcinoma. The name describes the pathology: the cytoplasm of these cancer cells is loaded with lipid droplets and glycogen, giving them a "clear" appearance under the microscope. They express high levels of HIF target genes — GLUT1, VEGF, glycolytic enzymes — in regions of the tumor that are adequately oxygenated. The cells behave as if they are starved of oxygen while oxygen is available.

The resolution is in the degradation pathway, not the sensing pathway. Clear cell RCC almost universally loses functional **VHL** — either through deletion, mutation, or promoter methylation. Without VHL, HIF-1α cannot be targeted for degradation even when it is properly hydroxylated by the PHDs. The recognition step that VHL performs is missing. HIF accumulates constitutively regardless of oxygen. The entire hypoxic transcriptional program — metabolic reprogramming, lipid accumulation, VEGF-driven angiogenesis — runs even in well-oxygenated cells.

This is the dead-end-then-resolution structure in operation. The initial hypothesis — the cells are hypoxic — fails when you measure oxygen and find it adequate. The resolution requires tracing the pathway downstream to find the broken off-switch: VHL, not oxygen availability, is the lesion.

The therapeutic payoff is direct. The dominant HIF paralog driving clear cell RCC biology is **HIF-2α** rather than HIF-1α. **Belzutifan**, a small molecule that binds HIF-2α and prevents its dimerization with HIF-1β, was approved by the FDA in 2021 for VHL-disease-associated tumors and subsequently for advanced clear cell RCC — the first drug to directly target the HIF transcriptional program. It suppresses VEGF, reduces tumor vascularity, and produces durable responses in a tumor type that had long been treated primarily with VEGF-pathway antibodies and kinase inhibitors working one step downstream.

---

### FDG-PET: the metabolic map as clinical tool

The opening case's PET scan is the Warburg effect made visible. FDG — fluorodeoxyglucose — is a glucose analog with the 2-hydroxyl group replaced by a radioactive fluorine-18. It is taken up by cells using the same glucose transporters (GLUT1, GLUT3) that normal glucose uses. Once inside, hexokinase phosphorylates it to FDG-6-phosphate — and there the analog gets stuck, because the phosphate group cannot be removed and the molecule cannot proceed further down glycolysis or be exported. Cells with high hexokinase activity and high glucose transporter expression accumulate FDG-6-phosphate as a radioactive trap. The fluorine-18 emits a positron; the positron annihilates with a nearby electron to produce two gamma rays in opposite directions, detected by the scanner to localize the source.

Every element of the signal reflects the underlying biology. High glucose transporter expression is driven by HIF-1α transcription in hypoxic or VHL-deficient regions. High hexokinase activity — particularly HK2, overexpressed in many cancers — commits glucose rapidly and efficiently. The combination produces the bright signal against a background of normal tissue with lower transporter and hexokinase expression.

Not all cancers are FDG-avid. Slowly proliferating tumors, prostate adenocarcinoma, and some well-differentiated carcinoids may not show the high glycolytic flux the PET scan detects. FDG-PET is a measure of glycolytic activity, not of malignancy itself — it detects the metabolic phenotype that many but not all cancers express. An FDG-negative tumor is not necessarily a benign lesion; it may be a malignancy that relies on OXPHOS or fatty acid oxidation rather than glycolysis. The scan's sensitivity depends entirely on whether the tumor in question has adopted the Warburg metabolism.

---

### What the energetics actually look like

Students often worry, correctly, about the ATP arithmetic. If cancer cells extract only two ATP per glucose while burning vastly more glucose than normal tissue, how does the cell meet the ATP demand of rapid proliferation?

The answer has two parts. First, the flux compensation: two ATP per glucose at enormous glycolytic throughput can add up. A cell running glycolysis at ten times the normal rate generates five times more ATP from glycolysis than a quiescent cell running OXPHOS at the normal rate, despite the per-glucose inefficiency. Second, the mitochondrial contribution: glutamine oxidation, fatty acid beta-oxidation, and the citric acid cycle running on non-glucose substrates continue to generate ATP via OXPHOS. The cancer cell is not relying on glycolysis alone for energy; it is running glycolysis for carbon and running mitochondrial oxidation of other fuels for energy. The two metabolic streams are parallel, not competing.

![Two-bar comparison on a zero baseline: glycolysis to lactate yields roughly 2 ATP per glucose versus about 30 ATP from complete oxidation — a fifteen-fold per-glucose gap the cell accepts as the price of a carbon-allocation strategy.](images/15-cancer-metabolism-the-warburg-effect-and-glucose-fig-04.png)
*Figure 15.4 — ATP yield: glycolysis to lactate versus complete oxidation*

This is why the "broken mitochondria" explanation was not only wrong but predicted the wrong things. If mitochondria were the problem, you would expect cancer cells to be ATP-depleted and growth-limited by energy. They are not; they are proliferating aggressively. The energy supply is adequate. What changed is the routing of carbon — and the PET scan lights up because the carbon routing involves massive glucose uptake, even if much of that glucose is not going all the way to CO₂.

---

## Exercises

**Warm-up**

1. *(Recall — difficulty: low)* State in one sentence the modern explanation for why a cancer cell performs aerobic glycolysis despite available oxygen, and name the single quantity the cell is optimizing rather than ATP per glucose. *What this tests: whether you have replaced the broken-mitochondria framing with the biomass-allocation framing.*

2. *(Recall — difficulty: low)* Trace the HIF-1α destruction pathway in a normoxic cell: name the enzyme that hydroxylates HIF-1α, the protein that recognizes the hydroxylated form, and the outcome for HIF-1α protein levels. Then state what happens to each step when oxygen drops. *What this tests: the oxygen-sensing mechanism before the VHL-loss case is applied to it.*

3. *(Recall — difficulty: low)* Why does FDG accumulate in cancer cells after being taken up, while normal glucose does not accumulate? Name the enzyme responsible and explain the structural reason the analog gets trapped. *What this tests: the biochemical basis of PET imaging before applying it to clinical interpretation.*

**Application**

4. *(Apply — difficulty: medium)* Trace one glucose molecule's carbon into four destinations a dividing cell needs: ribose-5-phosphate, serine, a lipid precursor, and lactate. For each destination, name the glycolytic intermediate at the branch point and the biosynthetic product it supports. Then explain in one sentence why complete oxidation to CO₂ would defeat the purpose of this routing. *What this tests: the carbon-allocation map as the mechanistic basis for aerobic glycolysis.*

5. *(Apply — difficulty: medium)* A clear cell renal carcinoma biopsy shows high GLUT1 expression, abundant lipid droplets, and high VEGF secretion in a well-oxygenated tumor region. The HIF-1α coding sequence is wild-type. Propose the most likely molecular lesion, trace the mechanism from that lesion to the observed phenotype, and explain why HIF-1α protein would be elevated despite normal oxygen and a normal HIF-1α gene. *What this tests: VHL-loss-driven pseudohypoxia as a downstream lesion in the HIF pathway.*

6. *(Apply — difficulty: medium)* A metabolomics screen of a cancer cell line shows accumulation of succinate in the cytoplasm and mitochondria, elevated HIF-1α protein in normoxic conditions, and increased expression of GLUT1 and glycolytic enzymes. The upstream oncogenes (KRAS, MYC, PIK3CA) are all wild-type. Propose the genetic lesion most likely causing this phenotype, explain the mechanism by which succinate accumulation stabilizes HIF-1α, and name the enzyme whose loss would explain the succinate accumulation. *What this tests: oncometabolite-driven PHD inhibition as a third route to constitutive HIF activation, distinct from hypoxia and VHL loss.*

**Synthesis**

7. *(Synthesize — difficulty: high)* A cancer researcher proposes that the Warburg effect is primarily an adaptation to hypoxia, not a feature of normoxic proliferating cells. Evaluate this claim. Use isotope-tracing evidence (what ¹³C-glucose labeling experiments show about carbon fate), the behavior of VHL-deficient clear cell RCC in normoxia, and the relationship between HIF-1α stabilization by oncogenic signaling and aerobic glycolysis to construct an argument about whether hypoxia is necessary for the Warburg phenotype. Conclude with what the claim gets right and what it misses. *What this tests: integration of the biomass argument, pseudohypoxia, and oncogenic HIF stabilization into a single coherent evaluation of a specific mechanistic claim.*

8. *(Synthesize — difficulty: high)* Mitochondria in cancer cells are described as "repurposed, not broken." For each of the following mitochondrial functions, state whether it is preserved, enhanced, or suppressed in a typical highly glycolytic cancer cell, and explain why: (a) ATP production from OXPHOS; (b) citrate export for fatty acid synthesis; (c) anaplerotic carbon intake from glutamine; (d) cytochrome c release initiating apoptosis. Then explain why suppression of function (d) while preserving (a)–(c) is mechanistically coherent rather than contradictory. *What this tests: differentiated understanding of mitochondrial function in cancer, against the broken-mitochondria misconception.*

**Challenge**

9. *(Challenge — difficulty: high)* Belzutifan targets HIF-2α and produces durable responses in VHL-disease-associated clear cell RCC. Propose a mechanistic rationale for why a cancer driven by constitutive HIF activity would not simply develop resistance by upregulating HIF-1α to compensate for HIF-2α blockade. Then identify the tumor types and patient populations where you would most expect belzutifan resistance to emerge through HIF-1α compensation versus other resistance mechanisms, and propose a biomarker strategy that would distinguish these mechanisms at progression. Be explicit about what is known versus what you are inferring from mechanism, and identify the single most important clinical question your analysis leaves open. *What this tests: resistance reasoning applied to a recently approved targeted therapy, integration of HIF paralog biology, and the limits of mechanistic inference without direct clinical data.*

---

## Prompts

### Figure 15.1 — Carbon fate map for a proliferating cell
Build a top-down (or left-rooted) hierarchy / branching tree with a single root node, "Glucose (glycolytic trunk)," branching into four leaf nodes representing biosynthetic fates: G6P → pentose phosphate → ribose-5-P (nucleotides); 3-phosphoglycerate → serine → glycine (one-carbon units); pyruvate → acetyl-CoA → fatty acid synthesis; lactate excreted (carbon waste / redox). Draw the trunk prominently and the four branches diverging from it with directed edges. Color the root/trunk blue (dominant carbon source), the nucleotide branch green (positive/biosynthetic), the one-carbon branch a transitional tone, the lipid branch secondary/neutral, and the lactate branch sky-blue (anchor waste/redox outlet). The visual point: carbon fans into multiple destinations rather than funneling entirely to CO2. No numeric data, no axes. Deliverable: single standalone HTML file, inline CSS, D3 v7 pinned CDN, Okabe-Ito colorblind-safe palette via CSS variables.

### Figure 15.2 — HIF-1α oxygen sensing: normoxia versus hypoxia
Build a two-panel comparison, left "Normoxia" and right "Hypoxia," each a top-to-bottom cascade of five aligned rows tracing the fate of HIF-1α. Left: PHD hydroxylates HIF-1α → VHL recognizes the tag → proteasome destroys HIF-1α → no target genes → (dash). Right: PHD stalled (no O2) → escapes VHL → HIF-1α accumulates → dimerizes with HIF-1β, enters nucleus → GLUT1, PDK1, MCT4, VEGF on. Align row-for-row so the divergence at the top sensor step propagates downward. Color the top sensor row green (active PHD on the left, stalled on the right), the accumulation row blue (dominant outcome on the right), the nuclear/dimerization row a transitional tone, and the target-gene row sky-blue (anchor output). No numeric data, no axes. Deliverable: single standalone HTML file, inline CSS, D3 v7 pinned CDN, Okabe-Ito colorblind-safe palette via CSS variables.

### Figure 15.3 — Repurposed mitochondria: cycle as precursor-export machine
Build an annotated callout diagram: a central node "Citric acid cycle (intact, repurposed)" drawn as the hub, with six callout boxes connected by leader lines showing its simultaneous outputs and inputs — citrate → fatty acid synthesis; α-ketoglutarate → amino acids; oxaloacetate → aspartate → nucleotides; glutamine refills (anaplerosis); electron transport chain → ATP; BCL-2 clamps the pore shut (no cytochrome c). Arrange the export callouts radiating outward (arrows leaving the cycle), the glutamine-anaplerosis callout as an inbound arrow, and the BCL-2 callout as a distinct guarding annotation on the outer membrane. Color the central cycle node sky-blue (anchor), the biosynthetic export callouts green (active/positive outputs), the ATP/ETC callout blue (dominant energy output), and the BCL-2 pore-clamp callout vermillion (blocking apoptotic output). No numeric data, no axes. Deliverable: single standalone HTML file, inline CSS, D3 v7 pinned CDN, Okabe-Ito colorblind-safe palette via CSS variables.

### Figure 15.4 — ATP yield: glycolysis to lactate versus complete oxidation
Build a simple two-bar vertical bar chart, y-axis from a zero baseline, unit "ATP per glucose." Two bars: glycolysis to lactate = 2 (highlighted) and complete oxidation (OXPHOS) = 30. Keep bar heights strictly proportional to value with a mandatory zero baseline so the fifteen-fold gap reads honestly. Highlight the glycolysis-to-lactate bar in blue (the surprising choice the chapter explains) and render the OXPHOS bar in neutral gray. Add direct data labels on each bar (2 and 30) and a caption noting the fifteen-fold per-glucose difference the cell accepts as the price of carbon allocation. No legend needed. Deliverable: single standalone HTML file, inline CSS, D3 v7 pinned CDN, Okabe-Ito colorblind-safe palette via CSS variables.
