# Chapter 2 — Introduction to Cancer: A Disease of Deregulation
*Your Own Cells, Running the Wrong Program.*

A pathology report comes back on a 58-year-old woman with a breast lump. It uses four words she does not know: *invasive ductal carcinoma, grade 3, stage IIA, ER-positive*. Her sister, ten years earlier, had a *grade 1, stage IIIB* tumor and did badly. The patient assumes grade 3 must be worse than grade 1 — higher number, worse disease.

She is reading the wrong descriptor. Grade and stage measure entirely different things. Her sister's lower-grade tumor had spread further — stage IIIB — which mattered far more than how the cells looked under the microscope. The patient's higher grade, lower stage tumor carries a better prognosis. She will spend weeks believing the opposite.

Before that vocabulary means anything, you need the underlying idea, and it is stranger than most introductory courses let on. Cancer is not a foreign invader. It is not a bacterium, not a virus, not something that arrived from outside. It is your own cells, descended from your own DNA, that have lost the regulatory contract that holds multicellular tissue together. That is why it is hard to treat: killing the cancer cell means killing a cell that looks, in most respects, like you.

---

Most diseases medicine has conquered were caused by something foreign. A bacterium, a virus, a toxin — something you can name, isolate, and target precisely because it is not you. That strategy fails for cancer. Tumor cells carry your DNA, your machinery, your membrane proteins. What has changed is a small number of letters in a few critical genes, and those changes have unhooked one lineage from the regulatory system every normal cell obeys.

That is why the useful definition of cancer is not anatomical or taxonomic. The NCI defines cancer functionally: cells that grow when they should not, ignore signals to stop or die, and can spread (NCI, *What Is Cancer?*). That move — from a name to a *behavior* — is the key insight. Cancer is unified by what cells *do*, not by which mutation started it or which organ it arose in. A BRCA-mutated breast tumor, an EGFR-mutated lung tumor, and a Philadelphia-chromosome leukemia look nothing alike molecularly, but each has acquired some subset of the same capabilities. They are members of a family, not instances of one disease.

This matters for therapy. The goal is **therapeutic index** — the gap between the dose that kills the cancer cell and the dose that damages too many normal cells. The narrower that gap, the more harmful treatment becomes. Every advance in targeted therapy, immunotherapy, and precision oncology is, in essence, a strategy to widen it.

---

In 2000, Douglas Hanahan and Robert Weinberg published a paper asking a question that sounds simple but had not been answered: regardless of which mutations cause cancer, what must *every* cancer cell be able to do? Their answer was a finite list of acquired capabilities — the hallmarks framework — that organized a field drowning in molecular particulars (Hanahan, 2022). The point worth holding before encountering the list: hallmarks are *mechanisms*, not labels to memorize. They are not a checklist every tumor ticks in the same order. They are the common destinations reached by many different mutational routes.

The original six capabilities:

**Sustaining proliferative signaling.** Normal cells divide only on receiving an external growth signal. Cancer cells manufacture their own, or lock their receptors permanently on. The RAS mutation of Chapter 1 is the canonical example — a switch stuck in the "go" position regardless of whether any external signal is present.

**Evading growth suppressors.** Normal cells have brakes: proteins that monitor the cell cycle and halt division when DNA is damaged or growth is inappropriate. Cancer cells lose them. *TP53* is mutated in roughly half of all human cancers; *RB1* and *APC* are lost in others. The brake line is cut.

**Resisting cell death.** Every normal cell carries the machinery for its own destruction — apoptosis — which fires when the cell is too damaged to repair, or when it has divided too many times. Cancer cells silence this program, often by overexpressing Bcl-2 family proteins or by losing functional p53 (Letai, 2016). They become cells that will not die when they should.

**Enabling replicative immortality.** Normal cells count their divisions through telomere shortening — chromosomal end-caps that erode with each replication and, after roughly fifty cycles, trigger a permanent cell-cycle arrest called senescence. Cancer cells reactivate the enzyme **telomerase**, which rebuilds the telomeres after each division and resets the counter. The replicative clock is not just paused — it is wound back.

**Inducing angiogenesis.** A tumor larger than about one millimeter cannot survive on passive diffusion of oxygen and nutrients. Cancer cells secrete signals — chiefly VEGF — that recruit the host vasculature to build new vessels into the tumor. This capability is the subject of Chapter 2 of the previous section; here, it is enough to note that a tumor unable to recruit vessels cannot grow beyond the size of a pinhead.

**Activating invasion and metastasis.** Cancer cells detach from their tissue of origin, breach the basement membrane, enter the bloodstream or lymphatics, survive the journey, and seed distant organs. This capability is what converts a curable local disease into an incurable systemic one. It is the most consequential item on the list.

In 2011, two **emerging hallmarks** were added: reprogramming energy metabolism (the Warburg effect — cancer cells preferentially run glycolysis even when oxygen is available, trading efficiency for speed of substrate processing) and evading immune destruction (cancer cells that are not eliminated by the immune system either hide from it or actively suppress it). Two **enabling characteristics** — genome instability and mutation, and tumor-promoting inflammation — were added as foundational conditions that accelerate the acquisition of the other capabilities.

In 2022, Hanahan extended the framework further: **unlocking phenotypic plasticity** (cells de-differentiating to access new states, including stem-like states that resist therapy), **non-mutational epigenetic reprogramming** (chromatin and methylation changes that alter gene expression without changing DNA sequence), **polymorphic microbiomes**, and **senescent cells** as active contributors to the tumor microenvironment (Hanahan, 2022). The 2022 additions are presented honestly as active synthesis, not settled dogma — whether plasticity, microbiome effects, and senescence belong on the same list as the original six is still debated `[contested — see pantry flag]`.

![Layered hallmarks framework: six core hallmarks plus 2011 and 2022 additions](images/02-introduction-to-cancer-a-disease-of-deregulation-fig-01.png)
*Figure 2.1 — The hallmarks of cancer (layered framework)*

<!-- → [DIAGRAM: hallmarks wheel — six core capabilities in the inner ring, 2011 additions and enabling characteristics in a middle ring, 2022 additions in an outer ring; each slice labeled with one concrete example mechanism] -->

The framework's durability is itself informative. Twenty-two years of molecular oncology did not overturn the list — it extended it. Every chapter in this book traces one of these capabilities.

---

Before clinical vocabulary can mean anything, two distinctions need to be precise: benign versus malignant, and grade versus stage.

A **benign** tumor is a clonal expansion of cells that are dividing more than they should but are not going anywhere. A lipoma — a benign fat-cell growth — gets bigger over years, does not invade surrounding tissue, does not spread through the bloodstream, and does not recur if cleanly removed. The cells have acquired some proliferative capability but not invasion or metastasis. Benign does not mean harmless: a benign meningioma pressing against the brainstem can be lethal by mass effect. But benign means the cells have not acquired the escape capabilities.

A **malignant** tumor — what people mean by "cancer" in ordinary speech — invades surrounding tissue and can seed distant organs. The line between benign and malignant is not always sharp. A colorectal adenomatous polyp is benign, but it carries an *APC* mutation and can, over a decade or two, accumulate enough further mutations to acquire invasive capability and become carcinoma (NCBI Bookshelf, *Development and Causes of Cancer*). That window of progression is exactly what colonoscopy exploits: remove the polyp while it is still benign and the malignant transition never occurs.

Cancer is also classified by tissue of origin, and the taxonomy is not arbitrary — it tells you something real about behavior and treatment.

**Carcinomas** arise from epithelial cells — the cells lining surfaces and glands: skin, gut, breast, lung, prostate, cervix. They account for 85–90% of human cancers. Within carcinomas, *adenocarcinomas* come from glandular epithelium (the secreting cells of the lung, colon, pancreas, breast), *squamous cell carcinomas* from flat surface epithelium (skin, esophagus, cervix). **Sarcomas** arise from connective tissue — bone, muscle, fat, cartilage — and are rare in adults but disproportionately represented in pediatric oncology. **Leukemias** are malignancies of blood-forming cells that circulate rather than form solid masses; **lymphomas** are malignancies of lymphoid cells that tend to form masses in lymph nodes and other lymphoid tissue. **CNS tumors** and **germ cell tumors** are their own categories. The taxonomy is not pure — small-cell and non-small-cell lung carcinoma share an organ but are biologically different diseases with different mutations, different behaviors, and different treatments — but the label tells you, on first encounter, where the cancer came from.

![Cancer classification tree by tissue of origin, with carcinomas dominating at ~85-90%](images/02-introduction-to-cancer-a-disease-of-deregulation-fig-03.png)
*Figure 2.3 — Cancer classification by tissue of origin*

---

Now grade and stage — the words that misled the patient.

**Grade** describes how the tumor cells look under the microscope. A well-differentiated (low-grade) tumor still resembles the tissue it came from: the cells are organized, the nuclei are regular, the growth pattern recognizable. A poorly differentiated (high-grade) tumor has lost that identity — irregular enlarged nuclei, disordered architecture, many cells caught mid-division. High-grade tumors generally behave more aggressively, growing faster and spreading earlier, because the cells have lost more of the normal regulatory circuitry. Grade is the pathologist's assessment of *how much the cell has changed*.

**Stage** describes how far the tumor has spread. The standard system is **TNM**: **T** for the primary tumor (size and local invasion, scored T1 through T4), **N** for lymph node involvement (N0 through N3), **M** for distant metastasis (M0 for none, M1 for present). These three coordinates combine into stage groupings 0 through IV. Stage IV means M1 — metastatic disease, cancer that has spread to a distant organ. Stage 0 means in-situ disease, a pre-invasive lesion that has not yet breached the basement membrane.

Stage drives prognosis. For colorectal cancer, five-year survival is roughly 90% at stage I and about 14% at stage IV (ACS, *Cancer Facts & Figures 2026*). That gradient is steep enough that the stage at diagnosis determines, more than almost any other factor, whether treatment is curative or palliative in intent. Grade matters — a high-grade tumor within a given stage tends to behave more aggressively — but stage comes first.

This is what the opening case turned on. The patient's grade-3, stage-IIA tumor is higher grade than her sister's grade-1 tumor, but her sister's stage-IIIB disease had spread further into the regional lymph nodes. Stage outranked grade, as it almost always does.

![TNM staging: T, N, and M coordinates combine into overall stage groupings 0-IV](images/02-introduction-to-cancer-a-disease-of-deregulation-fig-02.png)
*Figure 2.2 — TNM staging structure*

<!-- → [TABLE: TNM staging — columns: descriptor, scale, what it measures, clinical example at each anchor point (T1/T4, N0/N2, M0/M1)] -->

---

The global scale of cancer is large enough to be worth anchoring with current numbers. In 2022, there were approximately 20 million new cancer diagnoses and 9.7 million cancer deaths worldwide — the most recent comprehensive GLOBOCAN estimates (IARC, 2024). Lung cancer is the leading cause of cancer death, at about 1.8 million annually. Breast, colorectal, prostate, and stomach cancers follow by incidence. In the United States, around 2 million new cases and 600,000 deaths are recorded annually, making cancer the second leading cause of death after heart disease (ACS, 2026). About 13% of cancers globally are attributable to infectious agents — a proportion concentrated in lower-income regions and largely preventable by vaccination and antimicrobial treatment, a point Chapter 11 develops.

Cancer is overwhelmingly a disease of age. About half of diagnoses occur after 65, because cancer is the product of accumulated mutations, and mutations accumulate over decades of cell division and carcinogen exposure. A 70-year-old's cells have divided many more times than a 25-year-old's, and each division is a chance for a replication error. The age distribution is not uniform by cancer type — pediatric cancers (sarcomas, leukemias, CNS tumors) peak early, while carcinomas of the colon, breast, and prostate accumulate across the lifespan — but the dominant demographic signal is age.

Outcomes are also shaped heavily by access, not biology alone. A given stage of cervical cancer diagnosed in a high-income country with access to chemoradiation and immunotherapy carries a different prognosis than the same stage diagnosed in a setting where those resources are unavailable. This is not a molecular fact. It is a structural one.

---

Three growths, classified against the functional definition.

A subcutaneous lipoma. The cells are dividing more than normal adipocytes, but they stay put. They do not invade, do not metastasize, and regress cleanly if removed. They have acquired some proliferative capacity but not the escape capabilities. By the functional definition — not by the presence of any abnormal growth, but by the specific capabilities the cells have and have not acquired — this is benign.

A breast lesion called *ductal carcinoma in situ* (DCIS). The word *carcinoma* signals cells with malignant-type characteristics. The words *in situ* signal they have not yet breached the basement membrane. The cells have acquired sustained proliferation, evaded growth suppressors, and resisted cell death — several hallmarks — but not invasion. This is stage 0, the genuinely ambiguous middle. Treated to prevent progression. A real site of overdiagnosis debate: not every DCIS would have become invasive, and the pathologist cannot reliably say which ones would.

A breast carcinoma that has spread to bone. Cells from the breast have invaded, entered circulation, survived, and colonized a distant organ. The full set of capabilities, including metastasis. Topographically in bone, but genetically and behaviorally breast cancer. TNM: M1. Stage IV.

Three growths, three positions on the deregulation spectrum. The functional definition sorts them. Capability acquired — not location, not cell type, not how the cells look — is what moves something along that spectrum.

---

The patient with the grade-3, stage-IIA tumor will probably do better than her sister. When someone explains why — explains that stage, not grade, was the prognostic driver; that her sister's lower-grade cells had already traveled further — the patient will need to undo an intuition that felt completely natural. Higher number, worse disease. That intuition is wrong because it conflates two descriptors that measure different things.

This is, in small, the recurring challenge of oncology. The vocabulary is precise, and precision matters, because grade and stage predict different futures and demand different treatments. The hallmarks framework is precise in the same way: it names not what cancer is called but what cancer cells *do*, and in doing so it organizes a field that would otherwise dissolve into thousands of isolated molecular facts.

Every chapter that follows examines one thread of this framework in more depth. But the thread to keep in view throughout is the one this chapter introduced: cancer is your own cells, running the wrong program, in a body that has to be treated carefully because the cells it needs to destroy and the cells it needs to protect are made of nearly the same material.

---

## Exercises

**Warm-up**

1. *[Recall — moderate]* In one sentence each, distinguish: (a) benign versus malignant; (b) grade versus stage; (c) carcinoma versus sarcoma. For each, name the single feature that does the distinguishing.
*What this tests: precision with the foundational vocabulary — whether you are using these words to mean different things or treating them as rough synonyms.*

2. *[Recall — moderate]* Name four of the original six hallmark capabilities and for each give one molecular example of how a cancer cell acquires it. Your examples should name a specific gene, protein, or pathway — not just describe the capability in different words.
*What this tests: whether the hallmarks are mechanisms for you or a memorized list — the molecular anchor is what makes them usable.*

3. *[Recall — moderate]* Explain in two sentences why the functional definition of cancer — cells that grow when they should not, ignore signals to stop or die, and can spread — is more useful for understanding therapy than a definition based on tissue origin or mutation type.
*What this tests: the logic of the capabilities framework and why it generates therapeutic strategy rather than just taxonomy.*

**Application**

4. *[Apply — moderate-hard]* A patient has a 5 cm colon tumor invading through the bowel wall, with 3 of 12 sampled lymph nodes positive and no distant metastases identified on imaging. Assign plausible T, N, and M values and reason about which overall stage grouping (I–IV) this most likely falls into. Then state what additional clinical information would sharpen the staging assignment, and explain why that information matters for treatment planning.
*What this tests: applying the TNM system to a clinical scenario; understanding that staging drives treatment intent.*

5. *[Apply — moderate-hard]* A 45-year-old man is told he has a grade-1, stage-IIIB lung adenocarcinoma. His brother had a grade-3, stage-IIA lung adenocarcinoma and recovered. The patient concludes his prognosis must be better because his grade is lower. Write the explanation you would give him — precisely enough that he understands not just the conclusion but the reason the two descriptors measure different things and which one dominates.
*What this tests: applying the grade/stage distinction to a clinical communication scenario; moving from definition to implication.*

6. *[Apply — hard]* Pick one tumor behavior — for example, "grows without receiving an external growth signal" — and trace it through three levels: (a) the hallmark capability it represents; (b) a specific molecular mechanism that produces it (name the gene, protein, or pathway); (c) one therapeutic or diagnostic consequence that follows from understanding that mechanism. Your answer should make clear how level (b) generates level (c), not just list three facts.
*What this tests: using the hallmarks framework as a mechanistic chain, not a classification scheme.*

**Synthesis**

7. *[Synthesis — hard]* Classify three growths against the functional definition of cancer — a uterine fibroid (benign smooth-muscle tumor), a thyroid papillary microcarcinoma (1 mm, found incidentally), and a melanoma with two positive sentinel lymph nodes — and for each state: which hallmark capabilities it has acquired, which it has not, and what those acquisitions imply for treatment intent (curative versus palliative) and method. Your classifications should differ from each other in ways that follow from the capabilities analysis, not from intuition about tumor size.
*What this tests: applying the functional definition and hallmarks framework to a graded classification problem; connecting capabilities to clinical decision-making.*

8. *[Synthesis — hard]* The 2022 hallmarks paper added phenotypic plasticity — the ability of cancer cells to de-differentiate and adopt new cell states — as an emerging hallmark. Write the strongest argument that this is *not yet* a stable, universal hallmark equivalent to the original six. Then write the one piece of evidence that would most convincingly settle the question in favor of including it, and explain what would need to be shown.
*What this tests: honest engagement with the limits of the framework; ability to distinguish established mechanism from active hypothesis.*

**Challenge**

9. *[Challenge — very hard]* The "Still Puzzling" section asks why some in-situ lesions progress to invasive cancer while others never would — the overdiagnosis problem that shapes screening policy for DCIS and low-risk prostate cancer. Design a study using current molecular tools — genomics, epigenomics, single-cell sequencing, or imaging biomarkers — that would attempt to distinguish, at diagnosis, which DCIS lesions are on a trajectory to invasive disease and which are not. Specify your study design, the molecular features you would measure, the outcome you would validate against, and the minimum follow-up time required to generate meaningful data. Then identify the single biggest obstacle to translating a successful study result into routine clinical practice, and explain why that obstacle is harder to solve than the molecular classification problem itself.
*What this tests: applying the hallmarks and capabilities framework to a real clinical uncertainty; moving from biological mechanism to study design to implementation barrier.*

---

## What Would Change My Mind

The chapter's central claim is that cancer is unified by deregulated *behavior* — a finite set of acquired capabilities — rather than by any shared cause or molecule. A finding that would force revision: a large, well-characterized cancer type that achieves uncontrolled growth, death resistance, and spread *without* acquiring the hallmark capabilities — for instance, a malignant, metastatic tumor driven entirely by a mechanism orthogonal to all the cataloged hallmarks and not reducible to any of them. The hallmarks framework has absorbed surprises by adding dimensions (2011, 2022) rather than being overturned; a cancer that fits none of them, even after expansion, would mean the unifying-capabilities frame is incomplete in kind, not just in detail.

## Still Puzzling

- Are the 2022 additions — plasticity, microbiomes, senescence — genuine hallmarks on par with the original six, or context-dependent modifiers? The field has not settled this `[contested — see pantry flag]`.
- Why do some in-situ lesions (DCIS) progress to invasive cancer while others never would? Predicting progression is exactly where the clean hallmark logic gets blurry, and it drives the overdiagnosis problem in screening.
- How much of cancer's clinical heterogeneity reflects different *routes* to the same capabilities versus genuinely different end-states? This bears directly on whether one therapeutic strategy can ever generalize across a cancer type.

## References

- NCI. *What Is Cancer?* https://www.cancer.gov/about-cancer/understanding/what-is-cancer
- Hanahan, D. (2022). Hallmarks of Cancer: New Dimensions. *Cancer Discovery*, 12, 31–46.
- NCBI Bookshelf. *The Development and Causes of Cancer.* https://www.ncbi.nlm.nih.gov/books/NBK9963/
- Letai, A. (2016). Mitochondrial apoptosis and BH3 mimetics. *PMC*, 5133681.
- IARC. *Global cancer burden in 2022.* https://www.iarc.who.int/news-events/new-report-on-global-cancer-burden-in-2022-by-world-region-and-human-development-level/
- American Cancer Society. *Cancer Facts & Figures 2026.* https://www.cancer.org/research/cancer-facts-statistics/all-cancer-facts-figures/2026-cancer-facts-figures.html

---

## Prompts

### Figure 2.1 — The hallmarks of cancer (layered framework)
Build a node-edge systems diagram organizing cancer hallmarks into historical layers. Five nodes: (1) "Six core hallmarks" — proliferation, evade suppressors, resist death, immortality, angiogenesis, invasion/metastasis (dominant, blue, central and largest); (2) "2011: reprogram energy metabolism, evade immune destruction" (secondary); (3) "Enabling: genome instability, tumor-promoting inflammation" (secondary); (4) "2022: phenotypic plasticity, non-mutational epigenetic reprogramming" (transitional, distinct hue for contested); (5) "2022: polymorphic microbiomes, senescent cells" (transitional). Directed arrows: core→2011, core→enabling, 2011→2022a, enabling→2022b — radiating outward from the dominant core to show the framework extending over time. Lay out as concentric/radial with the core node at center. Okabe-Ito semantics: blue for the dominant core, neutral secondary for 2011/enabling, a transitional hue (e.g., orange) for the contested 2022 nodes. Subtitle: "Six core hallmarks plus 2011 and 2022 additions." Deliverable: single standalone HTML file, inline CSS, D3 v7 pinned CDN, Okabe-Ito colorblind-safe palette via CSS variables.

### Figure 2.2 — TNM staging structure
Build a layered schematic showing three independent input coordinates combining into one output. Stack four horizontal layers top to bottom: (1) "T: primary tumor T1 → T4" note "increasing size / local invasion" (sky-blue anchor); (2) "N: nodal involvement N0 → N3" note "increasing lymph-node spread" (neutral); (3) "M: distant metastasis M0 vs M1" note "M1 forces stage IV" (vermillion, negative); (4) "Overall stage 0, I, II, III, IV" note "three coordinates combine to severity" (blue, dominant). Show the top three coordinate layers each as a graded scale (small ticks T1-T4, N0-N3, M0/M1) feeding downward via arrows into the bottom combined-stage bar. Emphasize that M1 alone forces stage IV with a callout. Okabe-Ito semantics: sky-blue anchor for T, vermillion for the M override, blue for the dominant output. Subtitle: "T, N, and M combine into stage groupings 0-IV." Deliverable: single standalone HTML file, inline CSS, D3 v7 pinned CDN, Okabe-Ito colorblind-safe palette via CSS variables.

### Figure 2.3 — Cancer classification by tissue of origin
Build a top-down hierarchy tree. Root: "Cancer by tissue of origin." Five first-level branches: (1) "Carcinoma (epithelial, ~85-90%)" rendered as the dominant branch (blue, largest, visually weighted to convey its share), with two children "Adenocarcinoma (glandular)" and "Squamous cell carcinoma (flat epithelium)" (secondary); (2) "Sarcoma (connective tissue)"; (3) "Leukemia (blood-forming, circulating)"; (4) "Lymphoma (lymphoid, mass-forming)"; (5) "CNS / germ-cell (other)". Use clean parent-child link lines, root at top, leaves at bottom. Encode the ~85-90% carcinoma dominance through node size or emphasis, not a numeric axis. Okabe-Ito semantics: blue for the dominant carcinoma branch, neutral secondary for its two subtypes and the other four branches. Subtitle: "Carcinomas dominate at ~85-90% of cases." Deliverable: single standalone HTML file, inline CSS, D3 v7 pinned CDN, Okabe-Ito colorblind-safe palette via CSS variables.
