# Chapter 16 — Cancer Metabolism: Lipids, Amino Acids, and the Tumor Microenvironment

A child with acute lymphoblastic leukemia is treated with a drug that is not a poison aimed at her cancer cells and not a molecule designed to fit any receptor on them. It is a bacterial enzyme, **asparaginase**, and all it does is circulate in her bloodstream consuming the amino acid **asparagine**. Normal cells shrug — they can synthesize their own asparagine when the supply runs low. Her leukemic cells cannot. They have lost the capacity to make asparagine and depend entirely on what they scavenge from the blood. Starve the blood of asparagine and the leukemic cells, unable to build protein, die.

This single metabolic dependency, exploited since the 1960s, helped push pediatric ALL cure rates toward 90 percent. Hold it as a template. The previous chapter showed that glucose is reprogrammed in cancer. But glucose is only one input. A dividing cancer cell also needs lipids for membranes, amino acids for protein and backbone carbon, and nucleotide precursors for DNA — and it rewires all of these. Each rewiring creates a dependency, and a dependency is a target. Asparaginase is the oldest proof: find a metabolic need the cancer cannot meet for itself, then cut off the supply. This chapter surveys the broader metabolic landscape and shows where the openings are.

---

## Lipids: building membranes, not storing energy

The first misconception to retire is that lipid metabolism in cancer is about energy storage. In a proliferating cancer cell, lipids are primarily structural and signaling molecules — membrane phospholipids, cholesterol, and the lipid anchors that hold proteins like RAS at the plasma membrane. When a cell divides, it must double its membranes. That requires fat. And many cancer cells, unlike most quiescent adult tissue, build their own rather than importing what they need.

Most differentiated cells take up fatty acids from the circulation. Cancer cells frequently reactivate **de novo fatty acid synthesis** — a pathway largely silenced after fetal development that cancer brings back. The pathway runs in sequence:

Citrate is exported from mitochondria to the cytoplasm, where **ATP-citrate lyase (ACLY)** cleaves it to acetyl-CoA. **Acetyl-CoA carboxylase (ACC)** converts acetyl-CoA to malonyl-CoA. **Fatty acid synthase (FASN)** condenses these units into palmitate, a 16-carbon saturated fatty acid. **Elongases and desaturases** — including **SCD1** — tailor palmitate into the full spectrum of fatty acids the cell needs for its membranes.

FASN is highly expressed in breast, prostate, lung, colon, and pancreatic cancers, often correlates with prognosis, and is frequently essential for tumor-cell survival in culture and in animal models. ACLY, ACC, and SCD1 are likewise targets in development. The reactivation is not incidental: when a cell is doubling its membranes every twenty hours, making lipids locally rather than depending on import is a significant logistical advantage.

Cholesterol synthesis via the mevalonate pathway is also upregulated in many cancers — relevant not just for membranes but because the pathway also produces the isoprenoid intermediates that prenylate RAS and other small GTPases, anchoring them to membranes and enabling their signaling. This is part of why statins, which block the mevalonate pathway, have attracted interest as potential cancer-preventive agents. The epidemiology suggests modestly reduced incidence in long-term users, but randomized trial evidence remains inconsistent, and no statin is established as a cancer therapy.

One further connection to earlier chapters: cancer cells often shift toward more saturated, rigid membranes. This matters for ferroptosis — which requires peroxidizable polyunsaturated fatty acids to propagate lipid peroxide chain reactions. A cancer cell that enriches its membranes in saturated fats is simultaneously building resistance to ferroptosis, linking lipid biosynthesis to the death-program evasion discussed in Chapter 13.

![Linear enzyme pathway with marked target nodes: exported citrate is cleaved by ACLY to acetyl-CoA, carboxylated by ACC to malonyl-CoA, condensed by FASN into palmitate, and tailored by SCD1 into membrane fatty acids — each catalytic step a druggable target.](images/16-cancer-metabolism-lipids-amino-acids-and-the-tumor-microenvironment-fig-03.png)
*Figure 16.3 — De novo fatty-acid synthesis pathway*

<!-- → [DIAGRAM: de novo fatty-acid synthesis — citrate → ACLY → ACC → FASN → palmitate → SCD1, with targetable enzymes marked] -->

---

## Glutamine addiction

Many cancers cannot survive without a steady supply of glutamine — the most abundant amino acid in blood — even when glucose is plentiful. This is the second major metabolic axis, and it is worth understanding not just as "another nutrient" but as something that does four distinct jobs simultaneously.

After import through transporters such as ASCT2 (SLC1A5), **glutaminase** converts glutamine to glutamate, which is then converted to **α-ketoglutarate** and fed into the citric acid cycle. From there, glutamine provides:

**Carbon for anaplerosis** — replacing the TCA cycle intermediates that are continuously siphoned off for biosynthesis. The Warburg reprogramming described in the previous chapter exports citrate to the cytoplasm for lipid synthesis, draining the cycle. Glutamine replenishes it, keeping the cycle turning even when glucose carbon is not completing the loop.

**Nitrogen for biosynthesis** — the nitrogen atoms of glutamine are transferred directly into amino acids and nucleotides. Every purine ring carries two glutamine-derived nitrogens; pyrimidines carry one.

**Glutamate for glutathione** — the tripeptide antioxidant that neutralizes reactive oxygen species. Cancer cells under oxidative stress — which is most of them — require glutamate to maintain glutathione levels. Cutting glutamine supply collapses the antioxidant buffer.

**NADPH** via malic enzyme reactions — contributing to the reducing power the cell needs for biosynthesis and for maintaining reduced glutathione.

Glutamine dependence is strongest in MYC-driven cancers, where MYC transcriptionally upregulates glutamine transporters and glutaminase. It is also prominent in some KRAS-mutant cancers. The glutaminase inhibitor CB-839 (telaglenastat) has shown modest clinical activity, typically in combination, and is in ongoing trials. The boundary condition is real and worth stating: normal proliferating cells — including intestinal epithelium and immune cells — also use glutamine heavily, so the therapeutic window is narrower than it would be for a truly cancer-specific dependency.

![Hub-and-spoke diagram: imported glutamine is converted by glutaminase through glutamate to α-ketoglutarate feeding the citric acid cycle, branching into four parallel uses — anaplerotic carbon, biosynthetic nitrogen, glutathione for antioxidant defense, and NADPH.](images/16-cancer-metabolism-lipids-amino-acids-and-the-tumor-microenvironment-fig-01.png)
*Figure 16.1 — Glutamine as a four-job metabolic hub*

<!-- → [FIGURE: glutamine entering the cell → glutaminase → glutamate → α-ketoglutarate feeding the TCA cycle, with branches to glutathione, nucleotides, and NADPH] -->

---

## The MTAP–PRMT5 synthetic lethality

The most elegant metabolic dependency story currently in clinical development involves not a pathway the cancer actively upregulates but a gap it cannot fill — and a second vulnerability that gap quietly creates.

**MTAP** (methylthioadenosine phosphorylase) sits on chromosome 9p21, directly beside the tumor suppressor *CDKN2A*. When *CDKN2A* is deleted — as it is in roughly 30% of all human cancers — MTAP is frequently co-deleted as a bystander, with no selective pressure for or against its loss. The result is that roughly 15% of all human cancers are MTAP-deleted.

MTAP normally clears the metabolite **MTA** (methylthioadenosine). In cells without MTAP, MTA accumulates. MTA is structurally similar to SAM (S-adenosylmethionine), the universal methyl donor used by methyltransferases, and it partially inhibits **PRMT5**, an arginine methyltransferase that methylates proteins involved in splicing and gene regulation. MTAP-deleted cells therefore run with PRMT5 partially throttled — not disabled, but running below full capacity, because the accumulated MTA is constantly competing with SAM at PRMT5's active site.

This creates a vulnerability that normal cells do not share. Normal cells have full MTAP activity, clear MTA, and run PRMT5 at full capacity. A PRMT5 inhibitor reduces PRMT5 activity below the level that normal cells can tolerate — but in MTAP-deleted tumor cells, PRMT5 is already partially inhibited by endogenous MTA. Adding an exogenous inhibitor pushes activity below the threshold the tumor cell can survive, while normal cells have enough spare capacity to absorb the drug effect.

This is **synthetic lethality**: MTAP deletion alone is survivable, PRMT5 inhibition alone is survivable in normal cells, but together they are lethal in the deleted cells. PRMT5 inhibitors (MRTX1719, AMG-193) are now in clinical trials specifically for MTAP-deleted tumors. It is one of the cleanest examples of translating a metabolic insight into a precision oncology strategy.

The worked example from this case deserves explicit framing. A 9p21 deletion removes *CDKN2A*, and the intuitive response is to target what *CDKN2A* loss does — unrestrained CDK4/6 — with a CDK4/6 inhibitor. That is a reasonable approach, but CDK4/6 is deregulated in a huge range of cancers and offers no selectivity specific to this deletion. The exploitable finding is not the famous driver gene but the passenger: MTAP loss creates a selective vulnerability that *CDKN2A* loss does not. Targeting the passenger through synthetic lethality gives selectivity that targeting the driver never could.

![Two-cell threshold comparison: in the MTAP-deleted tumor cell, accumulated MTA partially throttles PRMT5 so an added PRMT5 inhibitor pushes activity below the survival threshold into death, while the MTAP-intact normal cell clears MTA, runs PRMT5 at full capacity, and retains enough spare margin to survive the same drug.](images/16-cancer-metabolism-lipids-amino-acids-and-the-tumor-microenvironment-fig-02.png)
*Figure 16.2 — MTAP–PRMT5 synthetic lethality*

<!-- → [DIAGRAM: MTAP deletion → MTA accumulation → partial PRMT5 inhibition → added PRMT5 inhibitor tips MTAP-deleted (but not normal) cells into death] -->

---

## The tumor microenvironment as a metabolic ecosystem

A tumor is not a uniform mass of identical cancer cells. It is a spatially heterogeneous ecosystem — cancer cells, fibroblasts, endothelial cells, macrophages, T cells, NK cells, and extracellular matrix, all coexisting in a metabolic environment that no healthy tissue would produce.

**Hypoxia.** Tumors outgrow their blood supply, and their interior oxygen levels are typically far below normal tissue values. Hypoxic regions are also radioresistant — radiation kills largely through reactive oxygen species, and without oxygen the chemistry is blunted. The HIF-1α signaling described in the angiogenesis chapter is the cell's response to this, driving VEGF secretion to recruit new vessels and shifting metabolism further toward glycolysis.

**Acidosis.** Exported Warburg lactate acidifies the interstitial space; intratumoral pH often falls to 6.5–6.8 against a normal serum pH of 7.4. Acidosis suppresses cytotoxic T-cell and NK-cell function and promotes invasion — low pH activates matrix metalloproteinases and favors the EMT phenotypes discussed in earlier chapters.

**Nutrient depletion.** Voracious cancer cells deplete the interstitial glucose, glutamine, and arginine to levels well below serum concentrations. Activated T cells, like cancer cells, require glucose and glutamine to proliferate and function. In a nutrient-depleted tumor, the cancer cells outcompete the immune cells, contributing to T-cell exhaustion and failure of immune surveillance. This is immune evasion grounded in metabolic competition rather than in any molecular signaling program.

**Lactate as an immunosuppressive signal.** Exported lactate is not merely a metabolic waste product. It directly impairs T-cell and NK-cell function at the concentrations found in tumors, polarizes macrophages toward a tumor-promoting rather than tumor-killing phenotype, and supports the proliferation of regulatory T cells. The Warburg effect and immune evasion are therefore directly connected: the same metabolic reprogramming that fuels cancer-cell proliferation simultaneously suppresses the immune cells that would otherwise eliminate it.

**Stromal metabolic exchange.** Some cancer-associated fibroblasts produce and secrete lactate that cancer cells take up and oxidize — a "reverse Warburg" arrangement in which the fibroblast does the glycolysis and the cancer cell does the oxidative phosphorylation. Adipocytes in breast and ovarian tumor environments supply fatty acids to adjacent cancer cells, which take them up and use them for energy and membrane building. The tumor microenvironment is not just competitive; it involves symbiotic exchange.

![Metabolic-exchange schematic of a tumor region: cancer cells export lactate that acidifies the space and suppresses cytotoxic T/NK cells, win the competition for the shared glucose and glutamine pool over T cells, while cancer-associated fibroblasts feed lactate back to cancer cells in a reverse-Warburg loop — coupling metabolism to immune evasion.](images/16-cancer-metabolism-lipids-amino-acids-and-the-tumor-microenvironment-fig-04.png)
*Figure 16.4 — The tumor microenvironment as a metabolic ecosystem*

The immunometabolic picture is why combining metabolic drugs with immune checkpoint inhibitors is mechanistically appealing: the metabolic intervention could relieve the nutrient competition that suppresses T cells, while the checkpoint inhibitor releases the brakes on those T cells. The IDO inhibitor trials are the cautionary counterpoint — a metabolically grounded rationale that did not translate. The conditions under which the combination helps versus when it fails are not yet established.

---

## What would change this picture

The chapter's central claim is that cancer's metabolic rewiring of lipids and amino acids creates selective dependencies that drugs can exploit with a real therapeutic window. The finding that would force revision: well-controlled clinical demonstrations that the headline dependencies do not translate — that MTAP-deleted tumors respond to PRMT5 inhibitors no better than MTAP-intact tumors, or that glutaminase and FASN inhibitors show no enrichment of benefit in biomarker-defined dependent populations across adequately powered trials. If the dependencies identified in cell culture and xenografts consistently failed to predict response in patients, the "dependency as target" principle would have to retreat to asparaginase as a near-unique exception rather than a generalizable strategy.

The asparaginase precedent and early PRMT5 data argue the principle is sound. Broad biomarker-negative trial results would be the disconfirming test.

---

## Still open

How much dietary metabolic intervention actually does in patients — whether caloric restriction, ketogenic diet, or methionine restriction can meaningfully starve tumors in humans, as opposed to in mice — is unresolved. The preclinical signals are strong; the clinical evidence is weak and hard to obtain rigorously.

Whether metabolic and immune combination strategies can be made to work reliably is open. The rationale is mechanistically clear: relieve the metabolic suppression of T cells, then release the checkpoint brakes. The IDO inhibitor disappointments are a warning that removing one metabolic axis is not sufficient. The conditions under which these combinations help remain to be defined.

And why repurposed metabolic drugs — metformin, statins, aspirin — consistently show modest, confounded epidemiological signals but inconsistent trial results is a recurring puzzle. Whether these represent real but small effects, or artifacts of confounding in observational data, is not settled.

---

## LLM Exercises

1. **(Four jobs)** List the four distinct metabolic functions glutamine performs for a proliferating cancer cell, name the enzyme that initiates its catabolism, and explain why cutting glutamine supply simultaneously impairs biosynthesis, energy generation, *and* antioxidant defense.

2. **(Synthetic lethality logic)** A patient's tumor has a homozygous deletion at 9p21 that removes both *CDKN2A* and *MTAP*. Explain, in mechanistic steps from the deletion to selective cell death, why a PRMT5 inhibitor should be toxic to this tumor but relatively spare normal cells. Then propose one mechanism by which the tumor might become resistant, and explain how you would test for it.

3. **(Lipid and death programs)** A cancer cell has high FASN activity and an enriched saturated fatty-acid membrane composition. Using the ferroptosis mechanism from Chapter 13, predict whether this cell is more or less vulnerable to ferroptosis induction than a cell with normal, polyunsaturated membrane composition. Explain the mechanism at the level of lipid peroxidation chemistry.

4. **(TME metabolic map)** Construct a metabolic map of a hypoxic, lactate-rich tumor region showing at least three cell types: a cancer cell, a cytotoxic T cell, and a cancer-associated fibroblast. For each cell type, label the primary nutrients consumed and the metabolites secreted. Mark the specific mechanism by which lactate suppresses T-cell function, and add an arrow showing where a checkpoint inhibitor plus a glycolysis inhibitor would each intervene. Annotate every arrow with the responsible molecule.

5. **(Classify and argue)** Classify each of the following as a mechanism, an epidemiological association, a therapeutic implication, or a contested claim: (a) "FASN condenses acetyl-CoA and malonyl-CoA into palmitate for membrane synthesis." (b) "Long-term statin use is associated with modestly reduced cancer incidence." (c) "Asparaginase depletes blood asparagine, selectively killing ALL cells that cannot synthesize it." (d) "Lactate polarizes tumor-associated macrophages toward a tumor-promoting phenotype." For the contested claim, identify the specific evidence gap that would resolve the contest.

---

## References

- Nature Reviews Cancer (2021). Cancer metabolism: looking forward. https://www.nature.com/articles/s41568-021-00378-6
- Nature Reviews Cancer (2011). Regulation of cancer cell metabolism. https://www.nature.com/articles/nrc2981
- Cell Death & Differentiation (2022). Targeting mitochondrial metabolism for precision medicine in cancer. https://www.nature.com/articles/s41418-022-01022-y
- Frontiers in Oncology (2022). Differential glutamine metabolism in the tumor microenvironment. https://www.frontiersin.org/articles/10.3389/fonc.2022.1011191/full
- Signal Transduction and Targeted Therapy (2023). Epigenetic regulation in the tumor microenvironment. https://www.nature.com/articles/s41392-023-01480-x
- Experimental & Molecular Medicine (2023). Metabolic reprogramming and epigenetic modifications in cancer. https://www.nature.com/articles/s12276-023-01020-1
- Hanahan, D. (2022). Hallmarks of Cancer: New Dimensions. Cancer Discovery, 12(1), 31–46.

---

## Prompts

### Figure 16.1 — Glutamine as a four-job metabolic hub
Build a hub-and-spoke (top-rooted hierarchy) diagram: one root node, "Glutamine → glutaminase → glutamate → α-ketoglutarate," branching to four leaf nodes that represent its parallel uses — anaplerotic carbon (cycle refill); nitrogen for nucleotides and amino acids; glutathione (antioxidant defense); NADPH (reducing power). Draw the root prominently with four directed edges fanning out to the four leaves; the visual point is one input doing four jobs simultaneously. Color the root blue (dominant input), the anaplerosis leaf green (positive/cycle-sustaining), the nitrogen leaf secondary/neutral, the glutathione leaf a transitional tone, and the NADPH leaf sky-blue (anchor reducing power). No numeric data, no axes. Deliverable: single standalone HTML file, inline CSS, D3 v7 pinned CDN, Okabe-Ito colorblind-safe palette via CSS variables.

### Figure 16.2 — MTAP–PRMT5 synthetic lethality
Build a two-panel threshold comparison, left "Tumor cell (MTAP-deleted)" and right "Normal cell (MTAP intact)," each a top-to-bottom cascade of five aligned rows so the two cells read in parallel against a shared axis ("crossing the survival threshold"). Rows: MTAP deleted / MTAP intact; MTA accumulates / MTA cleared; PRMT5 partially throttled / PRMT5 at full activity; PRMT5 inhibitor added / same inhibitor added; below threshold → death / above threshold → survival. Align row-for-row to make the single divergence — pre-existing throttling — drive the opposite endpoints. Consider a shared horizontal "survival threshold" reference line that the left cascade crosses below and the right stays above. Color the top MTAP-status row sky-blue (anchor), the throttling row a transitional tone, the inhibitor-added row blue (dominant identical intervention), and the bottom outcome row vermillion (death, left) versus green (survival, right). No numeric data. Deliverable: single standalone HTML file, inline CSS, D3 v7 pinned CDN, Okabe-Ito colorblind-safe palette via CSS variables.

### Figure 16.3 — De novo fatty-acid synthesis pathway
Build a left-to-right linear flowchart of five sequential metabolite nodes joined by four labeled enzyme arrows, marking each catalytic step as a druggable target. Nodes: citrate (exported from mitochondrion) → acetyl-CoA → malonyl-CoA → palmitate → tailored fatty acids → membrane. Edge labels (the enzymes / drug targets): ACLY, ACC, FASN, SCD1. Single horizontal track, equal-width nodes. Color the starting citrate node sky-blue (anchor input), the early intermediates neutral/anchor tones, and the palmitate and tailored-fatty-acid product nodes secondary. Render the four enzyme edge labels as highlighted target badges (blue) to signal druggability. Add a caption: each catalytic step (ACLY, ACC, FASN, SCD1) is a druggable target. No numeric data, no axes. Deliverable: single standalone HTML file, inline CSS, D3 v7 pinned CDN, Okabe-Ito colorblind-safe palette via CSS variables.

### Figure 16.4 — The tumor microenvironment as a metabolic ecosystem
Build a node-edge systems diagram of a spatial metabolic ecosystem with five nodes: cancer cell, cytotoxic T/NK cell, cancer-associated fibroblast, lactate/acidosis pool, and shared nutrient pool (glucose, glutamine). Directed, labeled edges: cancer cell → lactate pool ("exports lactate"); lactate pool → T/NK cell ("suppresses", drawn as an inhibitory/block edge); cancer cell → nutrient pool ("wins competition"); T/NK cell → nutrient pool (competes); fibroblast → cancer cell ("reverse Warburg feed"). Lay nodes spatially as an ecosystem rather than a linear chain. Color the cancer cell blue (dominant competitor), the T/NK cell green (positive/anti-tumor immune effector), the fibroblast secondary, the lactate/acidosis pool vermillion (negative/suppressive), and the shared nutrient pool sky-blue (anchor contested resource); draw the suppression edge in vermillion as a blocking connector. No numeric data, no axes. Deliverable: single standalone HTML file, inline CSS, D3 v7 pinned CDN, Okabe-Ito colorblind-safe palette via CSS variables.
