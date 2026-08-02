# Chapter 20 — Metastasis: The Seed and the Soil


## TL;DR

- This chapter gives a working overview of Metastasis: The Seed and the Soil, focusing on the ideas a reader needs before moving to the next chapter.
- The chapter moves through The metastatic cascade, Intravasation: getting into the bloodstream, Circulating tumor cells, Arrest, extravasation, and the pre-metastatic niche, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

Metastasis is inefficient. The remarkable thing about cancer is not that it spreads, but that any single cell ever succeeds in spreading.

Hold the framing. Estimates from various model systems suggest that a primary tumor sheds *millions* of cells into the circulation per gram of tumor per day. Most of those cells die. They die from shear forces in the bloodstream. They die from immune attack by natural killer cells and macrophages. They die from anoikis — the apoptosis triggered when an epithelial cell loses contact with its proper extracellular matrix. They die from failure to extravasate at a distant site. They die from inability to find a hospitable microenvironment. The numbers suggest that fewer than 0.01 percent of circulating tumor cells successfully form metastatic colonies. Probably much fewer.

But the small fraction that succeed kill patients. Metastatic disease is responsible for about 90 percent of cancer mortality. The cells that escape, survive, and grow at distant sites are biologically unusual — they have acquired capabilities (invasion, immune evasion, organ-specific adaptation, dormancy management) that most cancer cells in a primary tumor do not have. They are the genetic and phenotypic selection that emerges from the metastatic cascade. Understanding which cells succeed, where they go, and what they do when they arrive is essential for understanding cancer mortality.

This is the second of two chapters on invasion and metastasis. The first — 13A — covered local invasion, EMT, MMPs, and the cellular machinery for movement. This one covers what happens after invasion: the metastatic cascade through the bloodstream, the survival of circulating tumor cells, the organ-specific patterns of seeding (the "seed and soil" hypothesis), the molecular basis of organotropism, and the dormancy-reactivation cycle that characterizes some metastatic disease.

Hold the question: *what makes a cancer cell that has invaded its tissue go on to actually colonize a new organ?*

---

## The metastatic cascade

The transition from local invasion to distant metastasis is sometimes called the *metastatic cascade*. The stages are conventionally:

1. *Local invasion* — escape from the primary tumor into surrounding tissue (Chapter 13A).
2. *Intravasation* — entry into a blood vessel or lymphatic vessel.
3. *Circulation* — survival in the bloodstream as a circulating tumor cell (CTC) or in lymph as a circulating tumor cell cluster.
4. *Arrest at distant site* — physical lodging in a capillary bed at a distant organ.
5. *Extravasation* — exit from the blood vessel into the parenchyma of the distant organ.
6. *Micrometastasis* — establishment of a small colony at the distant site.
7. *Macrometastasis* — growth of the colony into a clinically detectable lesion, often requiring its own angiogenesis (Chapter 12) and adaptation to the new microenvironment.

Each step has its own biology, its own bottleneck, and its own opportunity for therapeutic interruption. The cascade is sequential — failure at any step blocks metastasis at that step — but cells can also be released at multiple times from the primary tumor (constant shedding) and from already-established metastases (re-seeding). The geometry of metastatic spread is therefore not a simple tree from primary to distant sites but a network with multiple sources and destinations.

The clinical correlate is that the *number of metastases* and the *organs involved* matter enormously for prognosis and treatment. Single-organ metastatic disease, in some cancer types, can be treated with curative intent (oligometastatic disease — typically 1-5 lesions in 1-2 organs — is sometimes addressed with stereotactic radiation or surgical resection plus systemic therapy, with meaningful long-term survival in selected cases). Widespread multi-organ metastatic disease is usually treated palliatively.

---

## Intravasation: getting into the bloodstream

A cancer cell that has invaded through its tissue of origin has reached the stroma — the connective tissue between epithelial structures. To metastasize, the cell needs to enter a blood vessel or lymphatic vessel. This is *intravasation*.

The choice between blood and lymph routes affects what happens next. *Hematogenous spread* via blood vessels takes the cell to wherever the blood goes — typically the lung first (if from a primary site that drains through the systemic veins) or the liver (if from gastrointestinal organs whose veins drain through the portal circulation). *Lymphatic spread* through lymphatic vessels takes the cell to local and then distant lymph nodes. The lymphatic and hematogenous routes are connected — lymphatic vessels ultimately empty into the venous circulation through the thoracic duct — but the patterns of organ involvement differ.

Intravasation requires the cell to cross the vessel wall. Tumor vessels are leaky (Chapter 12A) — they have gaps in the endothelial layer, incomplete pericyte coverage, and reduced basement membrane. The leakiness facilitates intravasation. Cancer cells can squeeze through gaps, migrate along the abluminal surface of the endothelium, and enter the vessel lumen.

Some cancer cells use specialized structures called *invadopodia* to drill through the vessel wall directly. Others use the macrophage-cancer cell-endothelial cell complex called the *tumor microenvironment of metastasis (TMEM)*. TMEM is a tripartite structure where a perivascular macrophage, a vascular endothelial cell, and a tumor cell come into contact at a vessel. The macrophage releases factors (including EGF) that promote tumor cell migration toward the vessel; the endothelial cell releases factors (including TIE-2-related signaling) that increase local permeability. TMEM density in breast cancer biopsies correlates with subsequent distant metastasis and is an emerging prognostic marker.

The cells that successfully intravasate are not necessarily the most numerous in the primary tumor; they are the ones with the right combination of invasive capability and access to vasculature. The combination of nearness to vessels (some regions of the tumor are vascular-rich, others vascular-poor), interaction with stromal cells (TMEM formation), and EMT state determines which cells make it through.

---

## Circulating tumor cells

Once in the bloodstream, the cancer cell becomes a *circulating tumor cell (CTC)*. CTCs are detectable in patient blood at very low numbers — typically 1-10 cells per milliliter of blood in patients with widespread metastasis, sometimes fewer. The numbers vary by cancer type and stage. Detection requires sensitive enrichment and identification methods because CTCs are vastly outnumbered by normal blood cells (about 5 billion red blood cells per milliliter and 5 million white blood cells per milliliter).

Several technologies enable CTC detection. *CellSearch* (the first FDA-approved CTC assay) uses magnetic capture with antibodies against EpCAM (an epithelial surface marker) followed by cytokeratin and DAPI staining for identification. The technology has limitations — it misses EpCAM-negative cells, including those that have undergone EMT — but is reproducible enough for clinical use. *Microfluidic devices* exploit size, deformability, or surface markers to enrich CTCs. *Image-based screening* of all nucleated cells in a blood sample, followed by AI-driven identification, is increasingly used.

CTC enumeration has clinical utility in some cancers. In metastatic breast cancer, the CellSearch CTC count is an independent prognostic factor — patients with ≥5 CTCs per 7.5 mL of blood have worse outcomes than those with fewer. Similar relationships hold in prostate cancer, colorectal cancer, and others. *CTC dynamics during therapy* — whether CTC counts decrease in response to treatment — can be a real-time biomarker of treatment response, potentially earlier than imaging changes.

Beyond enumeration, *molecular characterization* of CTCs is increasingly possible. Single-cell sequencing of CTCs reveals their mutational profile, transcriptomic state, and EMT signature. The CTC profile can differ from the primary tumor — CTCs often carry mutations acquired after the primary biopsy, providing a real-time genetic snapshot of the disease. CTC-derived organoids and xenografts (cultured tumor models grown from CTC samples) provide functional models for testing drug sensitivity.

A striking biological observation is that CTCs frequently travel as *clusters* — groups of 2-50 cells held together by cell-cell adhesion. CTC clusters are far less common than single CTCs (perhaps 0.1-3 percent of total CTC events) but are 30-100 times more efficient at forming metastases per cell. The clustering provides protection against anoikis (cells in clusters retain cell-cell contacts), shields against shear forces, and may facilitate immune evasion (the central cells in a cluster are less exposed to NK cell attack).

What kills most CTCs? Several mechanisms. *Shear forces* in arterial circulation can deform cells beyond their tolerance. *Natural killer cells* and *macrophages* in the circulation kill many tumor cells through direct cytotoxicity. *Anoikis* — the apoptosis triggered by loss of normal cell-matrix contacts — kills cells that have failed to develop adequate survival adaptations. *Lack of survival signals* — circulating cells are not receiving the trophic signals that maintained them in their original microenvironment — drives apoptosis. *Failure to find a hospitable target tissue* — even cells that survive in circulation may fail to arrest in a useful organ.

Cancer cells that survive these challenges have specific adaptations. They often retain some epithelial features (partial EMT) that allow cluster formation. They activate platelets that surround the CTC and provide protection plus pro-survival signaling (TGF-β, lysophosphatidic acid). They form micro-aggregates with neutrophils. They activate anti-anoikis signaling (often through PI3K-AKT pathway activation). They downregulate immune-recognition markers.

---

## Arrest, extravasation, and the pre-metastatic niche

Where do CTCs end up? The answer depends partly on hemodynamic factors and partly on biological factors.

*Mechanical factors*. CTCs are typically larger than the smallest capillaries in major organ vascular beds. The first capillary bed they encounter often arrests them. For cancers draining through portal venous circulation (colorectal, pancreatic, stomach), the first capillary bed is the liver. For cancers in tissues drained by systemic veins (most other primary sites), the first capillary bed is the lung. The hemodynamic distribution explains some metastatic patterns — liver metastases from colorectal cancer, lung metastases from breast cancer, sarcomas, and renal cell carcinoma.

*Biological factors*. Beyond hemodynamics, certain cancer types show preferential metastasis to specific organs even when those organs are not the first encountered. *Breast cancer* metastasizes preferentially to bone, lung, liver, and brain. *Prostate cancer* metastasizes overwhelmingly to bone (especially the axial skeleton). *Melanoma* metastasizes to many sites but particularly brain. *Pancreatic cancer* to liver and lung. *Ovarian cancer* to peritoneum.

The phenomenon of organ-specific metastasis was articulated by Stephen Paget in 1889. He noted that breast cancer patients dying of metastatic disease showed certain patterns — bone, lung, liver involvement was common, while other organs were rarely involved. Paget proposed the *seed and soil* hypothesis: cancer cells are *seeds* that travel widely, and their success at any site depends on whether that site provides a hospitable *soil*. The seed-soil framework has been validated and expanded enormously in modern molecular terms.

The molecular basis of organotropism involves chemokine gradients, organ-specific adhesion molecules, and tissue-specific survival factors. *CXCR4* on cancer cells binds *CXCL12 (SDF-1)*, which is highly expressed in lung, liver, and bone marrow — supporting metastasis to those sites. *CCR7* binds *CCL19/CCL21* on lymphatic endothelium — supporting lymph node metastasis. Organ-specific integrin patterns determine which tissue extracellular matrices cancer cells can adhere to.

The *pre-metastatic niche* is one of the deeper findings of recent metastasis biology. Cancer cells at the primary tumor site can shape distant organs *before* any cancer cells arrive there. The mechanism involves tumor-secreted factors that travel through the bloodstream and recruit immune cells (especially myeloid-derived suppressor cells) to specific organs, alter the extracellular matrix at those sites, and create conditions favorable for arriving cancer cells. Tumor-derived exosomes (small membrane vesicles containing proteins, RNA, and lipids) play a key role — their integrin composition appears to determine which organs they target and which therefore become receptive niches.

Once arrested at a target site, the cancer cell must *extravasate* — exit the blood vessel into the surrounding tissue. The process is similar to intravasation in reverse: the cell migrates between endothelial cells, uses MMPs and other proteases to breach the vessel basement membrane, and enters the parenchyma. Successful extravasation depends on the cell's invasive capacity and on the receptiveness of the local microenvironment.

Some cancer cells take a more aggressive route — they remain inside the vessel and proliferate there. *Intravascular metastasis* is a less common pattern but is observed in some cancers (especially small-cell lung cancer and some breast cancers). The cells form intravascular colonies that eventually break through the vessel wall by mass effect.

---

## Dormancy and reactivation

A cancer cell that has successfully extravasated into a distant organ does not necessarily grow. In many cases, it enters a *dormant state* — remaining alive but not dividing, sometimes for years or decades. The dormant cell is below detection thresholds (too small to be seen on imaging, too few cells to release detectable biomarkers). When and if the cell reactivates and begins to proliferate, the lesion can grow into clinically detectable metastatic disease.

Dormancy is one explanation for *late recurrence* of cancer — the patient who is disease-free for 10, 15, or even 20 years after curative surgery and then develops metastatic disease. The cancer was not "cured"; it was dormant. Something — local microenvironment changes, immune system changes, hormonal shifts, inflammatory events — triggered the dormant cells to resume proliferation.

The molecular basis of dormancy is increasingly understood. Three main mechanisms.

*Cellular dormancy*. Individual cancer cells enter a non-dividing state through cell-cycle exit (G0 entry). This may be driven by lack of mitogenic signals at the metastatic site, by upregulation of cell-cycle inhibitors (p21, p27), or by specific niche-derived signals (BMP, TGF-β, others). The cells remain alive but quiescent.

*Angiogenic dormancy*. Micro-metastatic colonies remain small because they cannot trigger angiogenesis — the *angiogenic switch* described in Chapter 12 has not flipped. The cells are not dormant individually; they are proliferating, but they are also dying (from the central anoxia of an un-vascularized cluster) at the same rate, producing a steady state. When the angiogenic switch eventually flips, the lesion grows.

*Immune dormancy*. Immune surveillance keeps small metastatic colonies in check. Cells that proliferate are killed by NK cells or T cells; the surviving cells stay small. Immune dormancy persists as long as the immune system is intact and reactive against the cancer. Suppression of immunity (immunosenescence, immunosuppressive drugs, secondary disease) can release dormancy.

Different dormancy mechanisms operate in different cancers and different contexts. Breast cancer cells in bone marrow appear to have prolonged cellular dormancy. Some prostate cancers may show angiogenic dormancy. Melanoma may involve all three mechanisms at different times.

The clinical implications of dormancy are significant. It explains why adjuvant therapy (treatment given after primary tumor removal in patients without detectable metastatic disease) can reduce later recurrence — the adjuvant therapy kills the disseminated tumor cells that would otherwise have remained dormant and later reactivated. It also explains why follow-up after curative cancer treatment must continue for many years.

---

## Organotropism in detail

The organ-specific patterns of metastasis are now understood at substantial molecular detail. Three particularly well-studied examples:

*Bone metastasis* (especially from breast, prostate, lung cancer). Cancer cells reaching the bone marrow find an environment rich in growth factors (TGF-β, IGF-1) that support tumor cell proliferation. They also interact with bone-resorbing osteoclasts and bone-forming osteoblasts in a *vicious cycle* — cancer cells secrete factors (PTH-related protein, IL-6) that activate osteoclasts to resorb bone; bone resorption releases stored growth factors (TGF-β, calcium) that feed cancer cell growth; cancer cells secrete more activating factors. The cycle drives both tumor growth and bone destruction.

Bisphosphonates (zoledronic acid, pamidronate) and the RANKL inhibitor denosumab inhibit osteoclast function and break the vicious cycle. They reduce skeletal-related events (fractures, spinal cord compression, hypercalcemia) and are standard adjuvant therapy in patients with bone metastases.

*Brain metastasis* (especially from breast, lung cancer, melanoma). The brain is protected by the blood-brain barrier (BBB) — a specialized endothelial cell layer with tight junctions that excludes most molecules from the brain parenchyma. Cancer cells that successfully colonize the brain have either bypassed the BBB (entering through circumventricular organs or directly through vessels in tumors that have disrupted the BBB) or have molecular adaptations that allow BBB crossing.

Cancer cells in the brain interact with astrocytes (the dominant glial cell), which can either inhibit or support tumor growth depending on context. Some cancers (notably HER2-positive breast cancer and melanoma) appear to be particularly adept at exploiting brain microenvironment factors. Brain metastases are particularly difficult to treat — the BBB excludes many systemic therapies — and require local approaches (surgery, stereotactic radiation, whole-brain radiation) for control.

*Liver metastasis* (especially from colorectal cancer, pancreatic cancer, and others draining through portal circulation). The liver receives the venous drainage of the gut, which delivers any circulating tumor cells from gastrointestinal cancers directly to liver sinusoids — the first capillary bed encountered. The liver microenvironment is unusual: hepatocytes produce growth factors (HGF, EGF, IGF-1), Kupffer cells (resident macrophages) can both attack and support tumor cells, and the sinusoidal endothelium is fenestrated, allowing direct cell-cell contact between blood-borne cancer cells and hepatocytes.

Colorectal cancer liver metastasis is one of the most studied cases. About 50 percent of colorectal cancer patients develop liver metastases at some point. Selected patients with limited liver involvement can undergo curative liver resection. The biology of why colorectal cancer specifically thrives in the liver is partly hemodynamic (portal drainage) and partly molecular (specific chemokine and adhesion receptor expression patterns).

The other organ-specific patterns each have their own biology and therapeutic implications. Peritoneal metastasis from ovarian and gastric cancer involves cells dropping off into the peritoneal cavity rather than hematogenous spread. Pleural metastasis involves seeding the pleural surface. Adrenal, kidney, and skin metastases each have distinct biology. The general principle — Paget's seed and soil — applies across all of them.

---

## Therapeutic implications

The metastatic cascade has been hard to target therapeutically. Several approaches have been pursued.

*Anti-EMT therapies*. Drugs blocking TGF-β signaling, Wnt signaling, or EMT transcription factors. Modest success in some clinical trials.

*Anti-invasion therapies*. MMP inhibitors (which failed in phase 3 trials, as noted in 13A). Newer selective MMP inhibitors and anti-MT1-MMP strategies in development.

*Anti-CTC therapies*. Strategies to kill circulating cancer cells directly. CTC capture devices that may enable targeted therapy. Treatments that destroy platelet-tumor cell interactions to expose CTCs to immune attack.

*Pre-metastatic niche disruption*. Drugs that block tumor-derived exosomes, myeloid-derived suppressor cell recruitment, or organ-specific niche formation. Early-stage development.

*Dormancy-targeted therapies*. Drugs that either maintain dormancy (keeping cells in their quiescent state indefinitely) or activate dormant cells (so they can be killed by cytotoxic therapy while they are dividing). Both strategies are in early development.

*Anti-organ-specific colonization*. Bisphosphonates and denosumab for bone metastasis are the canonical example of disrupting the vicious cycle of organ-specific colonization. Brain-penetrant drugs for CNS metastasis (small-molecule EGFR inhibitors like osimertinib, HER2 inhibitors like tucatinib, BRAF inhibitors). Hepatic arterial infusion of chemotherapy for selected liver metastasis cases.

The fundamental challenge is that by the time metastatic disease is clinically detected, the cells have already completed most of the cascade and are established in the new environment. Prevention of metastasis would ideally happen before clinical detection — through adjuvant therapy in primary tumors, through targeting of dormant cells, through immune surveillance. Treatment of established metastasis is then more about managing the metastatic colonies than preventing their formation.

---

## What this chapter gives you

Metastasis is the cascade by which cancer cells leave the primary tumor and establish colonies at distant sites. The process involves intravasation, survival in circulation, arrest at distant sites, extravasation, and growth at new locations. Each step is a bottleneck, and the vast majority of cancer cells that enter the cascade die before completing it.

Circulating tumor cells (CTCs) are the carriers of metastatic potential. They circulate as individuals or in clusters (the clusters being more efficient at metastasis per cell). CTC enumeration and molecular characterization are increasingly clinically useful as prognostic markers and as a source of real-time tumor genetic information.

The organ-specific patterns of metastasis (organotropism) reflect both hemodynamic factors and biological factors. The seed-and-soil hypothesis articulated by Paget in 1889 has been validated and expanded. Chemokine gradients, organ-specific adhesion molecules, the pre-metastatic niche, and tumor-derived exosomes all contribute to the molecular basis of organotropism.

Cancer cell dormancy at distant sites — sometimes for years or decades — is an important contributor to late recurrence. Three main dormancy mechanisms (cellular, angiogenic, immune) operate in different contexts. Adjuvant therapy works in part by killing disseminated tumor cells before they can establish dormant or active metastases.

Therapeutic targeting of metastasis is challenging because by the time disease is clinically detected, the cascade has often already been completed. Current strategies focus on adjuvant therapy in primary tumor management, on managing established metastatic colonies (bisphosphonates for bone metastasis, brain-penetrant agents for CNS disease), and on emerging concepts of dormancy management and pre-metastatic niche disruption.

Chapter 14 turns to the tumor microenvironment — the cellular and matrix ecosystem in which primary tumors and metastatic colonies live. The biology of stromal cells, immune cells, and the matrix shapes everything that happens in cancer, and the targeting of the microenvironment is increasingly central to cancer therapy.

---

## LLM exercises

1. Ask your LLM to walk through Stephen Paget's 1889 paper articulating the seed-and-soil hypothesis. What were his observations, what did he propose, and how has the hypothesis been validated at the molecular level over the subsequent 130 years? Identify which aspects of his proposal have been confirmed and which have been substantially revised.

2. Have your LLM explain the CTC cluster phenomenon — what fraction of CTC events are clusters, why are clusters more efficient at metastasis, and what molecular mechanisms underlie cluster stability? Probe: what therapeutic strategies could specifically target CTC clusters?

3. Use your LLM to compare bone, brain, liver, and lung metastasis biology. What features of each organ make it a hospitable target for specific cancer types? What therapies have specifically addressed each pattern of metastasis, and what is the level of evidence for each?

4. Ask your LLM to explain cancer cell dormancy — the cellular, angiogenic, and immune mechanisms — and how each connects to late recurrence in different cancer types. Then ask: should dormancy be maintained (keeping cells quiescent) or disrupted (activating cells so they can be killed by cytotoxic therapy)? What is the rationale for each approach?

5. Have your LLM survey the data on liquid biopsy — CTC enumeration, circulating tumor DNA, and tumor-derived exosomes — as biomarkers in metastatic disease. Which approach is most clinically useful in which cancer, what does the FDA say about each, and what is the trajectory of the field over the next 5 years?

---

##  AI Wayback Machine
The ideas in this chapter didn't appear from nowhere. **Stephen Paget** proposed the "seed and soil" hypothesis in 1889 — analyzing autopsy records of 735 women with breast cancer to show that metastases are not random, but settle preferentially in specific organs. The hypothesis sat dormant for a century before molecular biology vindicated it.

**Run this:**

```
Who was Stephen Paget, and how does his seed and soil hypothesis connect to the metastasis biology we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.
```

→ Search **"Stephen Paget"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to compare Paget's "seed and soil" with James Ewing's later "mechanical" theory that metastasis follows blood flow patterns.
- Ask it about Paget's father, Sir James Paget, and what it was like growing up in 19th-century British medicine.

What changes? What gets better? What gets worse?
