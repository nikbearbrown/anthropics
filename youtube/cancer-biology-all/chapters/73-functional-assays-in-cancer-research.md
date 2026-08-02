# Chapter 73 — Functional Assays in Cancer Research


## TL;DR

- The number on the page tells you the cancer cells responded to your drug.
- The chapter moves through Cell viability and proliferation assays, Cell death assays, Migration and invasion assays, Specific tumor cell behavior assays, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

The number on the page tells you the cancer cells responded to your drug. What you actually want to know is whether they died, stopped dividing, or just looked sick.

Hold the framing. Cancer research generates numbers — IC50 values, fold-changes, percentages, p-values. Each number represents an experiment. The interpretation depends on what the experiment actually measured. A "cytotoxic" drug may have killed cells, stopped them from dividing, induced senescence, or some combination. The endpoint chosen determines what conclusion you can draw. Choosing the right assay for the question is essential to getting meaningful results.

The standard cancer research toolkit includes assays for proliferation, viability, cell death, migration, invasion, gene expression, protein levels, and many other endpoints. Each assay has specific advantages, limitations, and pitfalls. Modern cancer research uses combinations of assays to characterize phenotypes thoroughly.

This appendix — the first of two on techniques and assays — covers functional cellular assays: cell viability and proliferation, cell death assessment, and migration and invasion. The next — B-B — covers molecular biology techniques (Western blot, PCR, ELISA, etc.), experimental design, data analysis, and quality control.

Hold the question: *given the assay you ran, what biological phenomenon does the result actually tell you about?*

---

## Cell viability and proliferation assays

The most fundamental cancer research question — "Did the drug kill or stop the cells?" — requires distinguishing among multiple outcomes:
- *Cell death* (cytotoxic effect).
- *Growth inhibition without death* (cytostatic effect).
- *Differentiation*.
- *Senescence*.

Different assays measure different things. The choice matters for interpretation.

*MTT/MTS/XTT assays*. Colorimetric assays based on cellular reduction of tetrazolium compounds to formazan products. Live cells with intact metabolic activity reduce the tetrazolium. Read absorbance.

- *MTT*. Insoluble formazan product. Requires solubilization step. Older but widely used.
- *MTS/XTT*. Soluble formazan products. Simpler protocol. More modern.

Limitations:
- Measures metabolic activity, not directly viability or cell number.
- Cells in different metabolic states (drug-treated cells may have altered metabolism even when alive) can give misleading results.
- Cell-type and culture condition specific calibration needed.

Despite limitations, widely used due to simplicity and high-throughput compatibility.

*Resazurin (alamarBlue) assay*. Similar principle to MTT. Resazurin (blue, non-fluorescent) is reduced to resorufin (pink, fluorescent) by live cells. Can be measured by fluorescence or absorbance. Less toxic than MTT (cells can be continued in culture if needed). Linear range often better than MTT.

*ATP-based assays*. Measure cellular ATP, which correlates with cell number and viability:
- *CellTiter-Glo*. Bioluminescent assay (luciferin + ATP + luciferase produces light). Very sensitive. High-throughput compatible.
- *Other ATP assays* (CellTiter-Glo 2.0, 3D versions for spheroids and organoids).

Advantages of ATP assays:
- Sensitive (detect low cell numbers).
- Linear over wide range.
- Suitable for 3D models.
- High-throughput compatible.

Disadvantages:
- Single time point (cells consumed).
- Expensive reagents.
- ATP affected by metabolic state, not just cell number.

*DNA content assays*. Measure total DNA in well as surrogate for cell number:
- *Hoechst staining*. Fluorescent stain binds DNA.
- *CyQUANT*. Fluorescent dye for nucleic acids.

*Direct cell counting*. Counting cells using:
- *Hemocytometer*. Classical microscopy-based counting. Manual.
- *Automated cell counters*. Various commercial systems.
- *Flow cytometry*. Sophisticated single-cell analysis.
- *Imaging-based counting*. Automated cell counting from microscopy images.

*Colony formation (clonogenic) assays*. Measures the ability of single cells to form colonies over 1-2 weeks:
- Plate small number of cells.
- Treat with experimental conditions.
- Allow colonies to form.
- Stain and count colonies.

The clonogenic assay is the gold standard for measuring cell reproductive capacity. It distinguishes cells that survive and proliferate from those that survive but cannot proliferate (which would score positive in MTT-type assays but are functionally dead in cancer biology terms).

Limitations:
- Time-consuming (1-2 weeks).
- Not all cell lines form colonies efficiently.
- Variable colony size definitions.
- Lower throughput than other assays.

The clonogenic assay remains widely used despite these limitations because of its biological relevance.

*Proliferation-specific assays*:
- *BrdU/EdU incorporation*. Cells in S phase incorporate the thymidine analog into DNA. Detected by antibody (BrdU) or click chemistry (EdU).
- *Ki-67 staining*. Marker expressed in proliferating cells (any non-G0 phase). IHC or IF.
- *Cell cycle analysis*. Flow cytometry with DNA-binding dyes (propidium iodide, DAPI, others).

These assays distinguish proliferation specifically from total cell number, providing more mechanistic information.

*Choosing the right viability/proliferation assay*:
- For initial drug screening: ATP-based or MTT/MTS for throughput.
- For mechanism (proliferation vs death): BrdU or Ki-67 plus death assay.
- For long-term reproductive capacity: clonogenic assay.
- For 3D models: ATP-based 3D-compatible versions.
- For specific cell types: assay validation needed.

No single assay captures all aspects. Combinations provide more complete characterization.

---

## Cell death assays

Cell death takes multiple forms with different molecular mechanisms. Specific assays distinguish among them.

*Apoptosis assays*:

*Annexin V/PI staining*. Apoptotic cells expose phosphatidylserine on cell surface (normally inside-facing). Annexin V binds PS. Propidium iodide enters cells with permeable membranes (late apoptosis or necrosis). Flow cytometry or imaging:
- Annexin V+/PI-: early apoptosis.
- Annexin V+/PI+: late apoptosis or necrosis.
- Annexin V-/PI+: necrosis (membrane permeable without PS exposure).
- Annexin V-/PI-: viable.

The standard apoptosis assay for cell-based studies.

*TUNEL assay*. Terminal deoxynucleotidyl transferase dUTP nick end labeling. Detects DNA fragmentation characteristic of late apoptosis. Used in cell preparations and tissue sections.

*Caspase activity assays*:
- *Caspase activity*. Substrate cleavage assays (fluorogenic or chromogenic substrates).
- *Cleaved caspase IHC/Western blot*. Active caspases (cleaved versions) detectable by specific antibodies. Cleaved caspase-3 most commonly used.
- *FRET-based caspase reporters*. Allow live-cell imaging.

*PARP cleavage*. PARP-1 is cleaved by active caspase-3 to generate characteristic 85 kDa fragment. Marker of apoptosis. Western blot.

*Cytochrome c release*. Mitochondrial cytochrome c release into cytoplasm is a marker of mitochondrial outer membrane permeabilization. Cellular fractionation followed by Western blot.

*Mitochondrial membrane potential*. Loss of mitochondrial membrane potential is an early apoptotic event. Detected with potential-dependent dyes (JC-1, TMRE, others).

*Sub-G1 population*. DNA degradation in apoptotic cells produces a sub-G1 peak on flow cytometric DNA analysis. Quick assessment of apoptotic fraction.

*Necrosis assays*:
- *LDH release*. Cells with permeable membranes release lactate dehydrogenase into culture supernatant. Colorimetric assay for LDH activity. Detects necrosis and late apoptosis (after membrane permeabilization).
- *PI uptake*. Propidium iodide enters cells with permeable membranes. Flow cytometry or imaging.
- *Trypan blue*. Excluded by intact membranes. Manual or automated counting of trypan blue-stained (dead) cells.

*Necroptosis assays*:
- *RIPK1 and RIPK3 phosphorylation*. Activated kinases involved in necroptosis. Western blot.
- *MLKL phosphorylation*. Effector of necroptosis. Western blot.
- *Inhibitor studies*. Necrostatin-1 (RIPK1 inhibitor) blocks necroptosis. If cell death is blocked by necrostatin but not pan-caspase inhibitors, suggests necroptosis.

*Pyroptosis assays*:
- *Gasdermin cleavage*. GSDMD cleavage by inflammatory caspases. Western blot.
- *IL-1β release*. Inflammatory cytokine released with pyroptosis. ELISA.

*Ferroptosis assays*:
- *Lipid peroxidation*. BODIPY-C11 or similar lipid peroxidation reporters.
- *Iron accumulation*. Iron-specific staining.
- *Inhibitor studies*. Ferrostatin-1, liproxstatin-1 inhibit ferroptosis. Iron chelators block ferroptosis.
- *GSH and GPX4 levels*. Decreased in ferroptosis.

*Autophagy*:
- *LC3 conversion*. LC3-I converts to LC3-II during autophagy. Western blot or fluorescence imaging (LC3-GFP fusion).
- *p62 levels*. Autophagy substrate; accumulates when autophagy blocked.
- *Autophagosome imaging*. By electron microscopy or LC3 puncta.

*Senescence*. Not technically cell death but a non-dividing state:
- *Senescence-associated β-galactosidase staining*. The classical marker. Cells stained at pH 6.0.
- *p16 and p21 expression*. Cell cycle inhibitors elevated in senescent cells.
- *Cell morphology*. Senescent cells become enlarged and flattened.
- *Senescence-associated secretory phenotype (SASP)*. Increased secretion of inflammatory cytokines.

The cell death field has expanded substantially with recognition of multiple regulated cell death programs. Specific characterization is increasingly important for understanding mechanisms.

---

## Migration and invasion assays

Migration and invasion are key cancer behaviors. Multiple assays measure them.

*Scratch (wound healing) assay*. Make a "scratch" in confluent cell monolayer. Measure cell migration to close the gap over time:
- Image at intervals (typically 0, 6, 12, 24 hours).
- Quantify percentage gap closure or distance migrated.
- Simple and inexpensive.

Limitations:
- Measures both migration and proliferation (need to control for proliferation).
- 2D, doesn't model 3D invasion.
- Standardization challenges (scratch width and shape vary).
- Wound healing biology different from cancer invasion.

Despite limitations, widely used for initial screening of migration effects.

*Boyden chamber (transwell) migration assay*. Cells in upper chamber migrate through porous membrane to lower chamber containing chemoattractant:
- Quantify cells migrated to bottom of membrane.
- Various pore sizes (8 μm typical).
- Can test specific chemoattractants.

*Transwell invasion assay*. Same setup but with Matrigel barrier:
- Cells must degrade matrix to invade through.
- Better models invasion than migration alone.
- 24-48 hour assay.

*xCELLigence and similar real-time impedance-based migration*. Cells crossing membrane between two electrode-containing chambers cause impedance change. Real-time monitoring without endpoint staining.

*Scratch assay variants*:
- *Insert assays*. Pre-defined scratches using removable inserts. More standardized.
- *Microfluidic scratch assays*.

*3D invasion assays*:
- *Matrigel droplet invasion*. Cells embedded in Matrigel drops; quantify invasive sprouting.
- *3D spheroid invasion*. Tumor spheroids embedded in matrix; quantify invasion into surrounding matrix.

*Organoid invasion assays*. Patient-derived organoids in matrix systems.

*In vivo invasion and metastasis*:
- *Tail vein injection*. Intravenous injection of cancer cells; quantify lung colonization.
- *Splenic injection*. For liver metastasis modeling.
- *Intracardiac injection*. For bone metastasis modeling.
- *Orthotopic injection with metastasis tracking*. More physiologic but complex.

*Specific migration mode assays*:
- *Amoeboid vs mesenchymal migration*. Different morphology and mechanism.
- *Collective migration*. Cohesive cell migration in groups.

*Single-cell tracking*. Imaging-based tracking of individual cell movements. Provides direction, speed, persistence, individual heterogeneity.

*Choosing the right migration/invasion assay*:
- For initial screening: scratch assay.
- For chemotaxis specifically: transwell migration.
- For invasion through matrix: transwell with Matrigel or 3D invasion.
- For mechanism studies: combinations with detailed imaging.
- For in vivo relevance: animal models eventually needed.

---

## Specific tumor cell behavior assays

Several other functional assays characterize specific cancer cell behaviors:

*Sphere formation assays*. Cancer stem cell-related. Cells in non-adherent conditions form spheres; sphere number and size assessed:
- *Mammosphere assay* (breast cancer).
- *Neurosphere assay* (brain tumors).
- *Other tissue-specific sphere assays*.

The assay enriches for cancer stem cell-like populations, though interpretation is debated.

*Soft agar colony formation*. Anchorage-independent growth — cells form colonies in soft agar without substrate attachment. Classical test of transformation. Few normal cells grow without substrate; cancer cells often do.

*ALDH activity (ALDEFLUOR assay)*. Cancer stem cell markers in many cancers. Flow cytometry-based assay.

*Side population assay*. Hoechst-excluding cells often have stem cell properties.

*Tumor initiation assays*. Limiting dilution injection in immunodeficient mice — measures fraction of cells that can initiate tumors. Considered the gold standard for cancer stem cell identification.

*Drug resistance assays*. Compare drug sensitivity of treated and untreated cells over time to assess emergence of resistance.

*Senescence assays*. As covered in cell death section.

*Cellular cytotoxicity assays*:
- *Immune cell killing of tumor cells*. Co-culture of immune effector cells with target cancer cells; measure target cell death.
- *Antibody-dependent cellular cytotoxicity (ADCC)*. NK cells + antibody-coated target cells.
- *Complement-dependent cytotoxicity (CDC)*. Complement + antibody-coated cells.

These assays are particularly relevant to immunotherapy research.

---

## High-content screening

Modern cancer research increasingly uses high-content automated imaging for phenotype assessment:

*High-content screening platforms*. Automated microscopy systems with image analysis software. Capture multi-parameter cellular phenotypes:
- Cell number.
- Morphology (size, shape, granularity).
- Proliferation markers (Ki-67, EdU).
- Death markers (cleaved caspase-3, propidium iodide, others).
- Protein localization.
- Cellular signaling (phospho-protein levels).
- Many other parameters.

*Advantages*:
- Multiple measurements per cell.
- Population heterogeneity assessable.
- High-throughput.
- Quantitative.

*Applications*:
- Drug screens with multi-parameter phenotypic assessment.
- Genetic perturbation screens (CRISPR, RNAi).
- Combination drug studies.
- Mechanism of action studies.

*Analysis software*. Specialized software (Cellomics, Harmony, others) for automated analysis of high-content images.

The high-content approach represents a substantial advance over single-parameter assays for many applications.

---

## What this appendix gives you

Cancer research uses multiple functional assays to characterize cellular phenotypes. Each assay measures specific aspects with different strengths and limitations.

Cell viability and proliferation assays include metabolic activity assays (MTT, MTS, alamarBlue), ATP-based assays (CellTiter-Glo), DNA content assays (Hoechst, CyQUANT), direct cell counting (hemocytometer, automated counters, imaging), and the gold-standard clonogenic assay for reproductive capacity. Proliferation-specific assays use BrdU/EdU incorporation, Ki-67 staining, or cell cycle analysis. Choice depends on the question being asked.

Cell death assays distinguish among multiple death programs. Apoptosis is assessed by Annexin V/PI, TUNEL, caspase activity, PARP cleavage, cytochrome c release, mitochondrial membrane potential, and sub-G1 fraction. Necrosis uses LDH release, PI uptake, trypan blue. Necroptosis, pyroptosis, ferroptosis each have specific markers. Autophagy is assessed by LC3 conversion, p62, and imaging. Senescence by SA-β-gal and other markers.

Migration and invasion assays include scratch (wound healing) assay (widely used initial screen but with limitations), Boyden chamber/transwell migration, transwell invasion with Matrigel, real-time impedance-based assays, 3D invasion assays, organoid invasion, and in vivo models. Single-cell tracking provides detailed individual cell behavior.

Specific tumor cell behavior assays include sphere formation (mammosphere, neurosphere), soft agar colony formation (anchorage-independent growth), ALDH activity (cancer stem cell marker), side population, in vivo tumor initiation assays (gold standard for cancer stem cells), drug resistance assays, and cellular cytotoxicity assays for immune-tumor interactions.

High-content screening uses automated microscopy to measure multiple cellular phenotypes simultaneously. Provides multi-parameter assessment of drug screens, genetic perturbation screens, and mechanism studies. Substantial advance over single-parameter approaches.

Appendix B-B covers molecular biology techniques, experimental design, data analysis, and quality control — the remaining elements of the cancer research toolkit.

---

## LLM exercises

1. Ask your LLM to compare MTT, ATP-based, and clonogenic assays for measuring cancer drug effects. For each: what does it actually measure, what are the time scales, what are the major limitations, and what additional information would each provide that the others don't? Identify the situations where each is the preferred assay.

2. Have your LLM walk through the Annexin V/PI flow cytometry assay for apoptosis. What is the biological basis, how are the four quadrants interpreted, what controls are needed, and what alternative apoptosis assays could provide complementary information? Identify the situations where Annexin V/PI might give misleading results.

3. Use your LLM to compare the scratch assay and transwell migration assay. For each: the procedure, what's measured, the advantages, and the limitations. Then consider a research question about whether a specific drug affects cancer cell migration — what assay would you choose and what controls would you need?

4. Ask your LLM to explain the various forms of regulated cell death (apoptosis, necroptosis, pyroptosis, ferroptosis, autophagy-dependent death). For each: the molecular pathway, the morphological features, the specific markers, and the inhibitors. Construct a flowchart for determining which form of cell death is occurring in a specific experiment.

5. Have your LLM survey high-content screening approaches in cancer research. What types of assays can be performed (drug screens, CRISPR screens, mechanism studies), what platforms are commonly used, what are the data analysis challenges, and what are the major insights that have come from these approaches? Identify the limitations relative to in vivo studies.

---

##  AI Wayback Machine
The ideas in this chapter didn't appear from nowhere. **William Hahn** pioneered RNAi and CRISPR-based functional genomic screens in cancer — including the Project Achilles dataset that maps genetic dependencies across hundreds of cancer cell lines. The work identifies which genes individual cancers need to survive.

**Run this:**

```
Who is William Hahn, and how does his work on functional genomic screens connect to the functional assays we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.
```

→ Search **"William C. Hahn"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to walk through how a CRISPR-Cas9 dropout screen identifies cancer-essential genes in a specific cell line.
- Ask it about the practical translation of "dependency" findings into drug targets — and where the field has succeeded and failed.

What changes? What gets better? What gets worse?
