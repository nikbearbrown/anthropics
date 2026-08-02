# Chapter 17 — Angiogenesis: The Tumor's New Blood Supply


## TL;DR

- A tumor without blood vessels is a tumor that cannot grow past the size of a pinhead.
- The chapter moves through How blood vessels form, briefly, VEGF and the angiogenic signal, Other angiogenic factors, The angiogenic switch, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

A tumor without blood vessels is a tumor that cannot grow past the size of a pinhead.

Hold the constraint. A single cell can survive on diffusion. Two cells, ten cells, a few hundred cells — they can survive on diffusion. Oxygen and nutrients reach them through the surrounding tissue fluid; waste products diffuse out. But once a cluster of cells reaches a critical size — roughly a millimeter in diameter, or about a hundred thousand cells — diffusion alone cannot supply the center. The interior cells starve and asphyxiate. The mass becomes necrotic in the middle. It cannot grow further.

Solid tumors live by this constraint. Without a blood supply, a tumor is dormant. With one, it can grow indefinitely. The decision to recruit blood vessels — to switch from a quiescent micro-tumor to an expanding mass — is one of the most consequential transitions in cancer progression. Judah Folkman called it the *angiogenic switch* in his 1971 *New England Journal of Medicine* paper. He proposed that tumors must induce their own blood supply to become clinically dangerous, that anti-angiogenic therapy might starve tumors of nutrients without the toxicity of chemotherapy, and that the molecular signals driving tumor angiogenesis would be discoverable. He was right on all three counts. The field he founded has produced FDA-approved drugs, dramatically extended life for some cancer patients, and revealed surprising complexities about the relationship between tumors and their vasculature.

This chapter — the first of two on angiogenesis — covers the normal biology of blood vessel formation, the angiogenic switch in tumors, and the molecular signals (VEGF, FGF, HIF, PDGF) that drive it. The next — 12B — covers the clinical translation: anti-angiogenic therapy (bevacizumab, the tyrosine kinase inhibitors, the multi-kinase inhibitors), the surprises (vascular normalization, modest survival benefits, resistance mechanisms), and the future directions including combinations with immunotherapy.

Hold the question that organizes the chapter: *given that every tumor depends on its blood supply, why is anti-angiogenic therapy less of a silver bullet than Folkman hoped?*

---

## How blood vessels form, briefly

The vascular system is built by two distinct processes.

*Vasculogenesis* is the formation of blood vessels de novo from precursor cells. It happens primarily in the embryo, where endothelial progenitor cells differentiate from mesoderm, migrate, and coalesce into the first primitive vascular networks. In adults, vasculogenesis is rare but does occur in some contexts, including bone marrow contribution to new vessels and (controversially) in some tumor settings.

*Angiogenesis* is the formation of new vessels from existing ones. This is the dominant mechanism in adult life. Angiogenesis happens during the menstrual cycle, during pregnancy (placental vasculature), during wound healing, during exercise-induced muscle adaptation, and pathologically in cancer, in diabetic retinopathy, in age-related macular degeneration, and in chronic inflammation.

The process of sprouting angiogenesis follows a stereotyped sequence. A pro-angiogenic signal — typically VEGF released by a nearby cell — reaches an existing capillary. Endothelial cells in the capillary respond. One cell, selected by lateral inhibition mediated by Notch signaling, becomes the *tip cell* — it extends filopodia in the direction of the VEGF gradient and migrates toward the source. The endothelial cells behind it, called *stalk cells*, proliferate to extend the new vessel behind the tip. The cells reorganize to form a hollow tube — a lumen. The new vessel reaches its target, anastomoses with other vessels or another tip cell, and forms a functional connection. Pericytes (the support cells that wrap around capillaries) are recruited. The basement membrane is laid down. The new vessel matures.

The whole process is regulated by gradients of signaling molecules, by Notch signaling that decides which cell becomes the tip versus stalk, by integrin-mediated adhesion to the extracellular matrix, and by countervailing anti-angiogenic signals that limit the response. In healthy tissue, angiogenesis is tightly regulated and produces well-organized vasculature with regular branching, pericyte coverage, and selective permeability.

In tumors, the regulation is broken. The signals are amplified. The Notch-mediated tip-stalk selection is impaired. The new vessels are disorganized. The result is a chaotic tumor vasculature that looks nothing like normal capillary beds.

---

## VEGF and the angiogenic signal

The dominant pro-angiogenic signal is *vascular endothelial growth factor (VEGF)*. The discovery of VEGF — initially called *vascular permeability factor* by Donald Senger and Harold Dvorak in 1983, and rediscovered as VEGF by Napoleone Ferrara at Genentech in 1989 — was the foundation of modern angiogenesis research and of anti-angiogenic therapy.

VEGF is a family of related glycoproteins. *VEGF-A* (commonly just called VEGF) is the main angiogenic factor. *VEGF-B* has more limited roles. *VEGF-C* and *VEGF-D* are primarily lymphangiogenic, driving the growth of lymphatic vessels. *Placental growth factor (PlGF)* is a related VEGF family member with context-specific roles. The receptors are *VEGFR-1 (FLT1)*, *VEGFR-2 (KDR/FLK1)*, and *VEGFR-3 (FLT4)*. VEGFR-2 is the dominant receptor for VEGF-A's angiogenic effects.

VEGF-A binding to VEGFR-2 activates a cascade of intracellular signaling. The receptor tyrosine kinase dimerizes and phosphorylates itself on multiple tyrosine residues, creating docking sites for downstream effectors. PLC-γ is activated, generating DAG and IP3 and activating PKC. The Ras-Raf-MEK-ERK pathway is activated. PI3K-AKT signaling is activated. The combined effect on endothelial cells is: increased proliferation, enhanced migration, increased survival, increased vascular permeability (one of VEGF's original-named functions), and upregulation of nitric oxide synthase (which contributes to vasodilation and permeability).

VEGF expression is regulated by multiple inputs. The most important regulator is *hypoxia*, mediated by the *HIF-1α* transcription factor described in Chapter 11A. The *VEGF-A* gene carries hypoxia response elements (HREs) in its promoter; HIF-1α binds and drives transcription. Cells experiencing low oxygen produce VEGF, which diffuses into the surrounding tissue, finds nearby endothelial cells, and triggers angiogenesis toward the source.

This is the most elegant feedback loop in tumor biology. A tumor that outgrows its blood supply becomes hypoxic. Hypoxia stabilizes HIF-1α. HIF-1α drives VEGF expression. VEGF diffuses to nearby vessels. New vessels grow toward the hypoxic tumor. Oxygen is restored. HIF-1α is degraded. VEGF expression returns to baseline. The tumor has built its own oxygen supply by means of a hypoxia-sensing feedback loop.

The loop is also why anti-angiogenic therapy is logically appealing. Block VEGF, and the feedback loop is interrupted. The tumor cannot resupply oxygen. It either becomes dormant or dies of central necrosis. In theory.

In practice, as we will see in 12B, the situation is more complex. Tumors have alternative pathways to angiogenesis. They can co-opt existing vessels (vessel co-option). They can mimic vessels through cancer cells themselves forming channel-like structures (vasculogenic mimicry). The single-target approach has not been the panacea Folkman hoped for, but it has produced real clinical benefits.

---

## Other angiogenic factors

While VEGF is dominant, several other signaling families contribute to tumor angiogenesis.

*Fibroblast growth factors (FGFs)*. The FGF family includes more than 20 ligands and four receptors (FGFR1, FGFR2, FGFR3, FGFR4). Several FGFs (FGF1, FGF2, others) are pro-angiogenic — they stimulate endothelial cell proliferation, migration, and survival, and they cooperate with VEGF in vascular development. FGF signaling is also important for tumor cell biology directly (some cancers have activating FGFR mutations or amplifications), making it a target for therapeutic intervention.

*Platelet-derived growth factor (PDGF)*. PDGF is produced by many cell types including platelets (its original source). It is a ligand for PDGFR-α and PDGFR-β. In angiogenesis, PDGF-BB signals through PDGFR-β on pericytes, recruiting them to newly formed vessels and stabilizing the vasculature. Without proper pericyte coverage, vessels remain leaky and immature. Anti-PDGF or anti-PDGFR strategies can therefore destabilize tumor vasculature.

*Angiopoietins*. Ang-1 and Ang-2 are ligands for the Tie-2 receptor on endothelial cells. Ang-1 binding stabilizes vessels and reduces permeability. Ang-2 destabilizes vessels and primes them for VEGF-driven angiogenesis. The Ang-2/Tie-2 axis is dysregulated in tumors and is a target for therapy (vanucizumab and similar agents in development).

*TGF-β*. The transforming growth factor-β family has complex, context-dependent effects on angiogenesis. TGF-β1 can be pro- or anti-angiogenic depending on the cellular context. It is also important for pericyte recruitment and vessel maturation.

*Endothelins*. ET-1 produced by endothelial cells affects vasomotor tone and can have pro-angiogenic effects in tumors.

*Hepatocyte growth factor (HGF)*. The ligand for the MET receptor (a receptor tyrosine kinase). HGF has direct pro-angiogenic effects in addition to its better-known roles in tumor cell biology.

*Pro-angiogenic chemokines*. CXCL8/IL-8, CXCL12/SDF-1, and others recruit endothelial progenitor cells and modulate angiogenesis.

*Matrix metalloproteinases (MMPs)*. These extracellular proteases degrade extracellular matrix to allow endothelial cells to migrate. They also release matrix-bound growth factors, making them available for signaling. MMPs are essential for the angiogenic process even though they are not signaling molecules themselves.

The multiplicity of factors is part of why blocking a single one (VEGF) is not always enough — tumors can compensate by upregulating alternative pathways.

---

## The angiogenic switch

A small tumor — perhaps a hundred cells, perhaps a few thousand — can sit dormant indefinitely if it cannot trigger angiogenesis. Autopsies of people who died of unrelated causes routinely reveal microscopic in situ cancers in the prostate, the thyroid, the breast — small dormant tumors that never progressed clinically. The dormancy state is a real and common biological condition.

The *angiogenic switch* is the transition from dormant to actively growing. Mechanistically, it involves a shift in the balance between pro-angiogenic and anti-angiogenic signals. The cell secretes pro-angiogenic factors continuously, and it also produces anti-angiogenic factors (thrombospondin-1 in some contexts, endostatin from collagen XVIII cleavage in others, angiostatin from plasminogen cleavage). The net signal determines whether the tumor grows.

The switch can be triggered by several events:

*Genetic changes that increase VEGF expression*. Loss of *VHL* (Chapter 11A) stabilizes HIF-1α and drives VEGF expression. Activating mutations in oncogenes like Ras, EGFR, and PI3K all upregulate VEGF transcription. Loss of tumor suppressors like p53 can also affect VEGF balance — wild-type p53 induces thrombospondin-1 (an anti-angiogenic factor); loss of p53 reduces thrombospondin-1 and tilts the balance toward angiogenesis.

*Microenvironmental changes that produce hypoxia*. As a tumor grows past a few cell layers, central cells experience hypoxia, stabilize HIF-1α, and secrete VEGF.

*Recruitment of pro-angiogenic stromal cells*. Tumor-associated macrophages, neutrophils, and platelets all release VEGF, FGFs, and other factors. The infiltration of these cells into the early tumor can tip the angiogenic balance.

*Mobilization of bone marrow-derived endothelial progenitor cells*. Some studies suggest that endothelial progenitor cells circulate in the bloodstream and home to tumors, where they participate in new vessel formation. The contribution is contested but seems to be real in some settings.

Once the angiogenic switch flips, the tumor enters a growth phase. New vessels form. Hypoxia is partially relieved. Nutrients and oxygen reach the previously dormant interior. The tumor expands. New regions become hypoxic, drive more angiogenesis, and the cycle continues. The tumor grows by alternating between regions of high vascular supply and regions of hypoxia, with the angiogenic feedback loop maintaining the average oxygen level that the tumor needs.

The dormancy-to-growth transition is consequential clinically. Many of the cancers that recur after years or decades of apparent cure (some breast cancers, melanoma, prostate cancer) are thought to have been dormant — micrometastases that survived without progressing — until something triggered their angiogenic switch. Understanding what flips the switch in dormancy is one of the active questions in cancer biology and has implications for adjuvant therapy duration and surveillance strategy.

---

## What tumor vasculature looks like

The vasculature that tumors build is not normal. It is recognizable on imaging, recognizable on histology, and consequential for everything that happens in the tumor.

*Disorganized branching*. Normal capillary beds have regular, hierarchical branching from arterioles to capillaries to venules. Tumor vessels branch chaotically, with abrupt diameter changes, blind ends, and arteriovenous shunts. The pattern looks more like a tangle than a network.

*Leaky walls*. Normal endothelium has tight junctions between cells. Tumor endothelium has gaps. Macromolecules leak from blood vessels into the tumor interstitium. The leakiness is one reason tumors retain certain drugs longer than normal tissue (the *enhanced permeability and retention effect*, exploited by some nanoparticle drug delivery systems) but also why tumor interstitial fluid pressure is elevated.

*Incomplete pericyte coverage*. Pericytes — the smooth muscle-like cells that wrap around capillaries — are reduced or absent on tumor vessels. The pericytes that are present often have abnormal morphology and weak attachment to the endothelium. This contributes to leakiness and to vessel instability.

*Mosaic vessels*. Some tumor vessels are partially lined by tumor cells rather than entirely by endothelial cells. The phenomenon of *vasculogenic mimicry* — tumor cells forming channel-like structures that conduct blood — has been described in melanoma, ovarian cancer, and others, though its frequency and biological importance remain debated.

*Vessel co-option*. Some tumors grow by infiltrating existing tissue and co-opting the existing vasculature rather than building new vessels. Liver metastases and some brain tumors are particularly prone to this. Vessel co-option is one mechanism by which tumors can be resistant to anti-angiogenic therapy — they did not depend on new vessel formation to begin with.

*High interstitial fluid pressure*. The leaky vessels combined with poor lymphatic drainage produce high pressure in the tumor interstitium, sometimes 5- to 10-fold higher than in normal tissue. The high pressure pushes back against the blood pressure driving flow into the tumor, impedes drug penetration, and contributes to hypoxia.

*Hypoxic regions*. Despite the new vessel formation, tumors typically have regions of significant hypoxia. The hypoxia drives further VEGF production, more chaotic vessel formation, and a feedback loop that never quite stabilizes the supply.

The functional consequence is that tumor blood supply is heterogeneous, intermittent, and inefficient. Drugs delivered through the bloodstream do not reach all parts of the tumor equally. Oxygen reaches some regions but not others. The hypoxic regions are radioresistant (oxygen is required for the indirect ionization that mediates much of radiation's effect). The acidic, hypoxic microenvironment selects for cancer cells with metabolic adaptations and aggressive phenotypes.

This is why anti-angiogenic therapy is not as simple as "starve the tumor." Tumor vessels are already barely functional. Eliminating them entirely may not be the goal — *normalizing* them, making them more like normal capillaries with better drug delivery and oxygenation, may be more therapeutically useful. The vascular normalization hypothesis, developed by Rakesh Jain and colleagues, has reshaped how anti-angiogenic therapy is conceptualized and is covered in 12B.

---

## What this chapter gives you

Tumors depend on blood supply to grow beyond about a millimeter in diameter. Without angiogenesis, micro-tumors remain dormant indefinitely. The transition from dormant to growing tumor — the angiogenic switch — is one of the major events in cancer progression and is governed by the balance between pro-angiogenic factors (VEGF dominant, plus FGFs, PDGF, angiopoietins, and others) and anti-angiogenic factors (thrombospondin-1, endostatin, angiostatin, others).

The dominant pro-angiogenic signal is VEGF-A binding VEGFR-2 on endothelial cells. VEGF expression is driven primarily by HIF-1α in response to hypoxia, creating an elegant feedback loop that drives vessel growth toward oxygen-starved tumor regions. The loop is conceptually attractive as a therapeutic target — interrupt it, and tumor growth should be limited by oxygen and nutrient supply.

Tumor vasculature is recognizably abnormal — disorganized branching, leaky walls, incomplete pericyte coverage, vessel co-option, vasculogenic mimicry, mosaic vessels, high interstitial pressure, and persistent hypoxia despite vessel formation. The abnormality has consequences for drug delivery, radiation response, and the tumor microenvironment.

Chapter 12B continues with the clinical translation — bevacizumab and the anti-VEGF antibodies, the multi-kinase inhibitors targeting VEGFR and related kinases, the vascular normalization hypothesis, resistance mechanisms, and combinations with chemotherapy and immunotherapy.

---

## LLM exercises

1. Ask your LLM to walk through Judah Folkman's 1971 *New England Journal of Medicine* paper. What did he propose, what evidence did he have, and which of his predictions have held up over the subsequent 55 years? Identify the predictions that have been confirmed and those that have been refined or contradicted.

2. Have your LLM trace the HIF-1α-VEGF feedback loop in tumor angiogenesis. Then ask: in a patient with clear cell renal cell carcinoma carrying biallelic *VHL* inactivation, which step of the feedback loop is broken, and how does this explain the dramatic vascularity of these tumors?

3. Use your LLM to compare normal capillary beds with tumor vasculature in terms of architecture, function, and consequences for therapy. Identify three specific features of tumor vessels that affect drug delivery and explain how each could be exploited or addressed therapeutically.

4. Ask your LLM to explain the angiogenic switch — what tips the balance from quiescent micro-tumor to growing tumor? Then probe the LLM on tumor dormancy: why do some tumors stay dormant for years or decades, what triggers the switch from dormancy to growth, and what does this mean for adjuvant therapy duration?

5. Have your LLM survey the non-VEGF angiogenic factors (FGF, PDGF, angiopoietins, others) and explain how they cooperate with VEGF and how they can mediate resistance to anti-VEGF therapy. Identify the strongest targets among the non-VEGF factors for therapeutic intervention.

---

##  AI Wayback Machine
The ideas in this chapter didn't appear from nowhere. **Judah Folkman** proposed in 1971 that tumors cannot grow beyond 1–2 mm without recruiting new blood vessels — and that anti-angiogenic drugs could starve them. The field rejected the idea for decades before it became foundational to oncology.

**Run this:**

```
Who was Judah Folkman, and how does his angiogenesis hypothesis connect to the tumor blood supply biology we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.
```

→ Search **"Judah Folkman"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to trace the path from Folkman's 1971 hypothesis to bevacizumab (Avastin) becoming standard cancer therapy.
- Ask it about why Folkman's hypothesis was dismissed for two decades — and what evidence finally convinced the field.

What changes? What gets better? What gets worse?
