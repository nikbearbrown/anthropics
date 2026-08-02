# Chapter 2 — Anti-Angiogenic Therapy: Promise and Reality
*Doing the Work the Starving Tumor Won't.*

Here is a thing that should have been simple. Tumors need blood vessels. Blood vessels grow in response to a signaling protein called VEGF. Block VEGF, and the tumor's vessels wither, the tumor starves, and the patient lives. The logic is clean enough that Judah Folkman put it in print in 1971 and spent the next three decades insisting it was right while the oncology establishment treated him like a crank (Folkman, 1971). Then bevacizumab got approved, and the establishment changed its mind.

But the story didn't end there, and that's the reason we need this chapter. The logic was right. The prediction — the great cure, the end of cancer by vessel starvation — was wrong, or at least badly incomplete. Tumors that respond to anti-angiogenic therapy almost always progress. A drug can shrink a tumor on the scan and leave the patient no better off. The drug that looked like the vindication of Folkman's life's work turned out to work in a way Folkman never described and for reasons the field took decades to understand.

If you want to know how anti-angiogenic therapy actually works — not the marketing version, not the starvation version — you have to follow the vessels themselves, watch what happens to them under the drug, and then ask whether what's happening is what you thought you were causing.

---

The first drug to make it through is worth understanding as a piece of engineering, not just as a treatment. **Bevacizumab** is a humanized monoclonal antibody. "Humanized" means the engineers took a mouse antibody — mouse antibodies being much easier to generate against a human protein — and swapped most of the mouse sequence for human sequence, leaving only the binding region intact. This matters because a fully mouse antibody would trigger an immune reaction in a human patient; humanization reduces that risk to something manageable. The target of this antibody is **VEGF-A** circulating in the blood: bevacizumab grabs VEGF before it can reach the **VEGFR-2** receptor on the surface of endothelial cells. It doesn't enter cells. It doesn't need to. It intercepts the signal in transit.

The pivotal trial — metastatic colorectal cancer, bevacizumab added to standard chemotherapy — showed that median overall survival improved from roughly 15.6 to roughly 20.3 months (Hurwitz et al., 2004). About five months. Real, statistically significant, enough for FDA approval in 2004. Enough, eventually, for approvals across colorectal, lung, renal, cervical, ovarian, and hepatocellular cancer. The drug worked.

The side effects are a map of where VEGF does normal work when you're not sick. VEGF maintains normal vessel tone partly through nitric oxide signaling — block it and blood pressure rises. VEGF sustains the filtration apparatus in kidney glomeruli — block it and protein leaks into the urine. VEGF is needed for wound healing — block it and surgical wounds close poorly, and occasionally bowel anastomoses fall apart. Arterial clots become more likely. The toxicity profile is not random. It's a pharmacological consequence of interrupting a signaling protein that was doing useful things before the tumor co-opted it (NCI, Angiogenesis Inhibitors).

<!-- → [TABLE: bevacizumab toxicities mapped to their physiological VEGF function — columns: toxicity, VEGF's normal role in that tissue, clinical frequency/severity, management note] -->

Related agents extended the approach. **Aflibercept** is not an antibody but a "trap": a fusion protein built from the extracellular domains of VEGFR-1 and VEGFR-2, which catches VEGF-A, VEGF-B, and PlGF out of circulation. **Ramucirumab** is an antibody directed not at the ligand but at the receptor — VEGFR-2 itself — blocking access from the other side of the handshake.

---

The small-molecule approach to the same problem is structurally different and clinically broader. **Tyrosine kinase inhibitors** — TKIs — are not antibodies. They are small enough to cross the cell membrane and compete with ATP for the kinase domain of the receptor. When the kinase can't bind ATP, it can't phosphorylate its downstream targets, and the signaling cascade stops.

The clinically important feature of TKIs is that most of them are not specific to VEGFR. They are **multi-kinase inhibitors**, hitting VEGFR-2 alongside PDGFR, FGFR, c-KIT, RET, and others in varying combinations depending on the molecule. **Sunitinib**, approved in 2006, blocks VEGFR-1, -2, and -3; PDGFR-α and -β; c-KIT; FLT3; and RET. In metastatic clear cell renal cell carcinoma — the *VHL*-deleted tumor from the previous chapter, exquisitely dependent on VEGF — sunitinib produced response rates around 30% and progression-free survival around 11 months, compared to roughly 5% response on the previous standard of interferon (Motzer et al., 2007). That is not a modest improvement. That's a different disease course.

**Sorafenib** hits VEGFR-2, PDGFR-β, and the RAF kinases. The RAF target is why it works in hepatocellular and thyroid cancer, where RAF pathway activation matters independently of angiogenesis. **Pazopanib, axitinib, cabozantinib, lenvatinib, regorafenib** — the list grows. Each has a somewhat different kinase profile, and the differences matter clinically because off-target kinase inhibition determines both efficacy in a given tumor type and the specific toxicity pattern the patient faces.

The toxicities of TKIs read differently from bevacizumab's. **Hand-foot syndrome** — redness, blistering, and pain on palms and soles — arises from PDGFR and c-KIT inhibition in skin vasculature and stem cells. **Hypothyroidism** follows from VEGFR-dependent thyroid vascularity. **Hepatotoxicity** follows from kinase inhibition in liver. Hypertension and proteinuria appear here too, as with bevacizumab. The breadth of the kinase profile produces breadth of effect in both directions: the multi-target coverage that helps manage angiogenic redundancy in tumors also multiplies the organs exposed to off-target interference.

<!-- → [TABLE: TKI drugs with their kinase targets — columns: drug, approved indications, primary kinase targets beyond VEGFR, characteristic distinguishing toxicities] -->

---

Now for the piece that rewrote the conceptual framework. For years, the mental model was starvation: cut off the blood supply, and the tumor starves. Rakesh Jain's group at Massachusetts General Hospital spent years watching what actually happens to tumor vessels when you give an anti-VEGF drug, using **intravital microscopy** — a technique that lets you observe living tissue through a surgically implanted window in real time (Jain, 2005). They expected destruction. What they saw was something else entirely.

In the first days after starting anti-VEGF therapy, the most abnormal vessels — the hemorrhagic, tortuous, dead-ended ones — regress. The vessels that survive are better. They become *less* leaky. Their pericyte coverage improves. Perfusion becomes more uniform. Interstitial fluid pressure, which in untreated tumors is high enough to actually push drug *out* of the tumor, drops. Hypoxia decreases.

The tumor vasculature after a few days of anti-VEGF therapy is, by multiple measures, *more functional* than at baseline.

Jain called this **vascular normalization**, and it inverts the logic of the whole enterprise (Jain, 2005). The mechanism isn't starvation. It's pruning and repair — a transient window during which the tumor's plumbing, having shed its worst components, briefly approaches something like normal. The implications of this are not subtle:

**Drug delivery improves.** Chemotherapy travels in the blood. If interstitial fluid pressure is high and perfusion is chaotic, cytotoxic drugs don't penetrate the tumor core. During the normalization window, they do.

**Radiation works better.** Radiation kills through oxygen free radicals. Hypoxic tumors are radiation-resistant. During normalization, hypoxia falls, and the tumor becomes more radiosensitive.

**The dose-response is not linear.** Past some threshold, more anti-VEGF therapy over-prunes the vessels. The tumor becomes severely hypoxic. Drug delivery worsens. Hypoxia selects for aggressive, invasion-prone cells. The therapy optimized for starvation is achieving the opposite of what combination therapy requires.

**Timing becomes the critical variable.** The normalization window is transient — days to perhaps a few weeks. Chemotherapy timed into that window outperforms chemotherapy given before it or after the vasculature has been over-stripped.

![Time-course of vascular function under anti-VEGF therapy rising into a transient normalization window then falling as over-pruning produces hypoxia](images/02-anti-angiogenic-therapy-promise-and-reality-fig-01.png)
*Figure 2.1 — The vascular normalization timeline*

<!-- → [DIAGRAM: vascular normalization timeline — y-axis: vascular function/drug penetration, x-axis: days of anti-VEGF therapy; three phases labeled: baseline chaotic vasculature, normalization window, over-pruned hypoxic phase; arrow marking optimal chemotherapy delivery window] -->

This is the kind of conceptual shift that makes a field feel like it misunderstood itself. The starvation model suggested that maximal vessel destruction was the goal, and that anti-angiogenic monotherapy was a reasonable strategy. The normalization model suggests the goal is to briefly improve the tumor's plumbing so that other treatments can reach their targets — which means the drugs are most valuable in combination, the timing of that combination matters more than the dose of either drug alone, and aggressive monotherapy may actually be counterproductive.

---

To see why response doesn't always equal benefit, you need to understand what the scan is actually measuring.

The contrast-enhanced MRI that detects glioblastoma works because gadolinium contrast agent leaks out of abnormally permeable tumor vessels into the tumor tissue, lighting it up. **Bevacizumab tightens those vessels.** The leakage stops. The contrast stops accumulating. The tumor on MRI shrinks dramatically — not necessarily because tumor cells died, but because the vessels that were leaking are now sealed.

This is **pseudoresponse**: imaging improvement driven by vascular normalization, not by tumor cell kill. The clinical consequence is that progression-free survival improves — the scans look better for longer — but overall survival does not (Wick et al., 2017). The patients on bevacizumab live no longer than those who didn't receive it. The tumor *looks* better and the patient lives no different.

This is not a drug failure in the ordinary sense. It is a mismatch between what the drug does and what the endpoint measures. **Response rate** measures tumor shrinkage — a proxy for cell kill. **Progression-free survival** measures time until the disease grows or the patient dies — better, but still vulnerable to pseudoresponse inflating the "no growth" period. **Overall survival** measures whether the patient lives longer — the thing we actually care about.

When these endpoints disagree, overall survival wins. A drug that shrinks tumors without extending life has demonstrated activity. It has not demonstrated benefit. Every treatment chapter from here forward will require you to hold the hierarchy in place: endpoint tells you what the measurement is, survival tells you whether it mattered.

![Nested hierarchy of trial endpoints with response rate and progression-free survival as proxies beneath overall survival, the decisive outcome](images/02-anti-angiogenic-therapy-promise-and-reality-fig-02.png)
*Figure 2.2 — The endpoint hierarchy: response to PFS to OS*

---

Resistance to anti-angiogenic therapy is essentially universal, and the mechanisms tell you something important about what the drugs are and aren't doing.

**Alternative angiogenic factors.** Block VEGF and tumors upregulate FGF, PDGF, and angiopoietins. The tumor doesn't need VEGF specifically — it needs any signal that drives endothelial proliferation. This is why multi-kinase TKIs that also hit FGFR and PDGFR have theoretical advantages over single-target bevacizumab, and why sequential TKIs after progression on a first agent sometimes work: the second agent catches the escape pathway the first one missed.

**Vessel co-option.** Some tumors don't build new vessels — they grow along existing ones, hijacking the brain's vasculature or the liver's sinusoids without triggering angiogenesis at all. These tumors are intrinsically resistant to anti-VEGF therapy because they never needed VEGF-driven vessel formation. Anti-angiogenic therapy may actually *select* for this phenotype by eliminating the VEGF-dependent cells and leaving behind those that co-opt.

**Pericyte coverage.** The normalization process matures vessels — improving pericyte investment. Mature, pericyte-covered vessels are VEGF-independent: they don't need VEGF to survive because they have structural support. Anti-PDGFR agents, which strip pericytes, can resensitize these vessels.

**Myeloid recruitment.** Tumors under anti-VEGF pressure recruit bone-marrow-derived myeloid cells — VEGF-independent myeloid-derived suppressor cells and M2 macrophages — that supply angiogenic signals through other pathways. The tumor does an end-run around the targeted therapy using its own immune-system manipulation.

**Hypoxia-driven selection.** This is the mechanism that should give you the most pause. Severe and sustained hypoxia selects for cells that thrive without oxygen — which means cells that have accumulated mutations enabling anaerobic metabolism, that have upregulated HIF targets, and that tend to be more invasive and more metastatic. Some preclinical data and scattered clinical observations suggest anti-angiogenic therapy can accelerate metastasis in certain contexts `[contested — the human magnitude is debated; benefit-risk balance still favors approved indications]`. Whether the therapy that was meant to cage the tumor can, in some circumstances, push it toward escape is one of the genuinely open questions in the field.

![Hub-and-spoke diagram of five parallel escape routes — alternative factors, vessel co-option, pericyte-stabilized vessels, myeloid recruitment, hypoxia-driven selection — converging on sustained vascular supply despite VEGF blockade](images/02-anti-angiogenic-therapy-promise-and-reality-fig-03.png)
*Figure 2.3 — Routes of resistance to anti-VEGF therapy*

<!-- → [TABLE: resistance mechanisms — columns: mechanism, molecular driver, clinical consequence, rational counter-strategy] -->

---

The current frontier is where the biology becomes elegant rather than just complicated. The tumor microenvironment is immunosuppressive through multiple overlapping mechanisms — metabolic (hypoxia produces lactate, acidifying the milieu and suppressing T-cell function), structural (abnormal vessels limit immune-cell trafficking), and cellular (regulatory T cells and myeloid-derived suppressor cells populate the tumor). **VEGF itself is immunosuppressive**: it inhibits dendritic-cell maturation, promotes regulatory T-cell expansion, and recruits suppressive myeloid populations.

Anti-VEGF therapy therefore should, if the normalization model is right: (1) reduce hypoxia and its immunosuppressive metabolic consequences, (2) improve T-cell infiltration through better-perfused vessels, (3) relieve VEGF's direct suppression of dendritic cells and regulatory T-cell induction, and (4) improve delivery of checkpoint-inhibitor antibodies themselves. Each of these effects augments the action of PD-1/PD-L1 checkpoint inhibitors, which work by releasing suppressed T cells to kill tumor cells — but only if those T cells can get in, stay functional, and be activated properly.

The clinical data match the prediction. **Atezolizumab plus bevacizumab** versus sorafenib in hepatocellular carcinoma (IMbrave150 trial) showed improved overall survival. **Pembrolizumab plus axitinib** versus sunitinib in renal cell carcinoma (KEYNOTE-426) improved overall survival. **Lenvatinib plus pembrolizumab** in endometrial cancer (KEYNOTE-775) and **cabozantinib plus nivolumab** in renal cell carcinoma (CheckMate 9ER) joined the list. Several are now standard of care.

<!-- → [TABLE: anti-angiogenic plus immunotherapy combinations — columns: combination, trial name, cancer type, comparator, endpoint that improved, mechanistic rationale from normalization framework] -->

This is what it looks like when a conceptual framework generates testable predictions that turn out to be true. The normalization model said: normalize vessels, reduce hypoxia, improve immune trafficking, lift VEGF-mediated immunosuppression — and immune therapy should work better. Then it did. The reframing is now complete: anti-angiogenic drugs are not primarily tumor-starving agents. They are tumor-microenvironment modifiers whose most important clinical role may be making other therapies work.

---

The opening patient — sunitinib in VHL-deleted renal cell carcinoma, 30% shrinkage, progression at eleven months — was not a drug failure. It was a drug working as well as it can work against a tumor that has multiple escape routes available. The glioblastoma patient whose MRI improved but who lived no longer was not a drug failure either. It was a drug doing what it does — normalizing vessels, reducing contrast leakage, looking like a response — in a tumor where vessel normalization without tumor-cell kill doesn't extend survival.

What would change this picture: a finding that aggressive, sustained vessel destruction — verified to leave the tumor severely hypoxic — produced better outcomes than normalization-timed combination. That would resurrect the starvation model. It hasn't happened. What keeps happening instead is that the combinations doing the best work are the ones that use anti-angiogenic therapy to briefly improve the tumor environment and then deliver a second blow into that improved environment. Starvation as a goal; normalization as the mechanism; combination as the strategy.

The still-open questions are worth holding: Can we detect the normalization window in a living patient, in real time, to actually time the combination rationally rather than empirically? Does anti-angiogenic therapy ever accelerate metastasis in humans in a clinically meaningful way, and if so when? Why is renal cell carcinoma — specifically the VHL-driven, VEGF-addicted subtype — so much more responsive than most other tumors? The last question leads directly into the next chapter, where invasion and metastasis themselves become the subject, and where the cells that survived the hypoxic selection pressure we just described turn out to matter enormously.

---

## Exercises

**Warm-up**

1. *[Recall — moderate]* Explain in three sentences why bevacizumab causes hypertension and proteinuria. Your answer should name the molecular target, identify where VEGF does normal physiological work in each tissue, and state the consequence of blocking it there.
*What this tests: whether you understand the toxicity profile as a pharmacological consequence of the drug's mechanism, not as an unrelated side effect.*

2. *[Recall — moderate]* A colleague says bevacizumab and sunitinib "do the same thing." Write a two-sentence correction that distinguishes their mechanisms of action and explains why their toxicity profiles differ.
*What this tests: mechanical understanding of antibody vs. small-molecule TKI, single-target vs. multi-kinase.*

3. *[Recall — moderate]* Define vascular normalization in your own words. Name two changes that occur in tumor vasculature during the normalization window and explain why each one matters for drug delivery.
*What this tests: whether the normalization concept has replaced the starvation concept in your mental model.*

**Application**

4. *[Apply — moderate-hard]* A new anti-angiogenic agent shows a 35% response rate and a 3-month progression-free survival improvement in phase 2, but the phase 3 trial shows no overall survival benefit. Write the one-paragraph conclusion you would give a clinical colleague. Name the specific proxy-versus-outcome confusion you are guarding against, and connect it to the glioblastoma pseudoresponse mechanism.
*What this tests: endpoint hierarchy — response rate → PFS → OS — and why the hierarchy exists.*

5. *[Apply — moderate-hard]* A patient on bevacizumab progresses after eight months. Name three distinct resistance mechanisms that could explain the progression. For each, identify the molecular pathway driving resistance and the rational counter-strategy.
*What this tests: ability to map resistance mechanisms to molecular drivers and therapeutic responses.*

6. *[Apply — hard]* A trial is designed to test anti-angiogenic therapy added to chemotherapy. Two scheduling arms are proposed: Arm A delivers both drugs simultaneously from day one; Arm B gives anti-angiogenic therapy alone for 10 days, then adds chemotherapy. Using the normalization framework, predict which arm performs better and explain the reasoning. Then name the piece of information you would need to know to schedule the chemotherapy optimally in an individual patient, and explain why that piece of information is currently hard to obtain.
*What this tests: applying normalization logic to clinical trial design; recognizing the limits of the framework.*

**Synthesis**

7. *[Synthesis — hard]* Build a table with four anti-angiogenic plus immunotherapy combinations — IMbrave150, KEYNOTE-426, KEYNOTE-775, CheckMate 9ER — including the two drugs, cancer type, comparator arm, the endpoint that improved, and a one-phrase normalization-based mechanistic rationale for why combining the two classes helps. Then write a two-sentence summary of the pattern across all four rows.
*What this tests: integration of normalization framework with immunotherapy rationale; evidence synthesis.*

8. *[Synthesis — hard]* VEGF is sometimes described as "a tumor's best friend and an oncologist's best target." Using what you know about VEGF's dual role — angiogenic driver and immunosuppressive agent — write a 200-word explanation of why blocking it disrupts two overlapping systems simultaneously, and why that redundancy explains the success of anti-angiogenic plus checkpoint-inhibitor combinations.
*What this tests: mechanistic integration across angiogenesis and immune evasion.*

**Challenge**

9. *[Challenge — very hard]* The "Still Puzzling" section raises the possibility that anti-angiogenic therapy sometimes accelerates metastasis by driving hypoxia and selecting for invasion-competent cells. Design a clinical or translational study that could distinguish between two populations: patients in whom sunitinib is slowing tumor progression, and patients in whom sunitinib-driven hypoxia is selecting for a more aggressive phenotype. What endpoints, biomarkers, and biopsy timing would you need? What ethical constraints complicate the design? This question requires reasoning beyond this chapter into mechanisms covered in the following chapters on invasion and metastasis.
*What this tests: ability to design a study around a contested mechanistic claim; application of normalization and resistance concepts to a genuinely unsettled question.*

---

## What Would Change My Mind

The chapter's central claim is that the clinical reality of anti-angiogenic therapy is best explained by vascular normalization rather than tumor starvation — that the drugs work by transiently improving, then modestly pruning, tumor vasculature. The finding that would force revision: a large, well-controlled trial in which *maximal, sustained* vessel destruction — verified by imaging or histology to leave the tumor severely hypoxic and avascular — produced the *best* outcomes: durable tumor regression and an overall survival benefit larger than any normalization-based combination schedule. That result would resurrect the starvation model and demote normalization to a side effect. So far the opposite holds: aggressive monotherapy tends to produce hypoxic, resistant tumors, and the combination schedules that exploit the normalization window outperform.

## Still Puzzling

- **Can we identify the normalization window in a living patient?** The model is well supported in animal systems, but routinely detecting *when* an individual tumor is normalized — to actually time the partner drug — remains unsolved. Without that biomarker, the schedule logic stays theoretical for any one patient.

- **Does anti-angiogenic therapy ever accelerate metastasis in humans, and if so, when?** Preclinical data and scattered clinical observations suggest hypoxia-driven selection for invasive cells, but the human magnitude is genuinely contested. Resolving it bears directly on whether the benefit-risk balance shifts in early-stage or adjuvant use.

- **Why is renal cell carcinoma so much more responsive than most other tumors?** *VHL*-driven VEGF addiction explains part of it, but not the full gap. What molecularly separates a truly vessel-dependent tumor from one that can co-opt or adapt is the patient-selection question the field most needs to answer — and the bridge into the invasion and metastasis chapters that follow.

## References

- Folkman, J. (1971). Tumor angiogenesis: therapeutic implications. *New England Journal of Medicine*, 285(21), 1182–1186.
- Hurwitz, H., et al. (2004). Bevacizumab plus irinotecan, fluorouracil, and leucovorin for metastatic colorectal cancer. *New England Journal of Medicine*, 350(23), 2335–2342.
- Jain, R. K. (2005). Normalization of tumor vasculature: an emerging concept in antiangiogenic therapy. *Science*, 307(5706), 58–62.
- Motzer, R. J., et al. (2007). Sunitinib versus interferon alfa in metastatic renal-cell carcinoma. *New England Journal of Medicine*, 356(2), 115–124.
- National Cancer Institute. Angiogenesis Inhibitors. https://www.cancer.gov/about-cancer/treatment/types/immunotherapy/angiogenesis-inhibitors-fact-sheet
- National Cancer Institute. Targeted Therapy for Cancer. https://www.cancer.gov/about-cancer/treatment/types/targeted-therapies
- Wick, W., et al. (2017). Lomustine and bevacizumab in progressive glioblastoma. *New England Journal of Medicine*, 377(20), 1954–1963.

---

## Prompts

### Figure 2.1 — The vascular normalization timeline
Build a horizontal timeline / time-course line graph. X-axis: "Days of anti-VEGF therapy" (left to right, no zero-baseline emphasis needed on x). Y-axis: conceptual vascular function / drug penetration. Plot a single curve that starts low (baseline chaotic vasculature, neutral grey marker), rises to a peak (normalization window, green = positive — annotate "Optimal chemo delivery; days to a few weeks"), then falls below baseline (over-pruned hypoxic phase, vermillion = negative — "Function falls below baseline"). Add a horizontal reference line at baseline function so the trough reads as below-baseline. Drop a shaded vertical band over the peak marking the delivery window. Three labeled markers along the curve. Subtitle "Vascular function vs days of anti-VEGF therapy." Deliverable: single standalone HTML file, inline CSS, D3 v7 pinned CDN, Okabe-Ito colorblind-safe palette via CSS variables.

### Figure 2.2 — The endpoint hierarchy: response to PFS to OS
Build a top-down hierarchy (three-tier pyramid/tree) showing decreasing proxy and increasing meaning. Root/apex: "Overall survival (decisive endpoint)" in blue = dominant. Two children below: "Progression-free survival (time to growth/death, proxy)" (secondary) and "Response rate (tumor shrinkage, proxy for cell kill)" (transitional color). Connect apex to each child with simple edges. Annotate the vertical axis conceptually: top = "what matters," bottom = "proxy, vulnerable to pseudoresponse." Color encodes endpoint authority (dominant down to proxy). Subtitle "When endpoints disagree, overall survival wins." No numeric axes. Deliverable: single standalone HTML file, inline CSS, D3 v7 pinned CDN, Okabe-Ito colorblind-safe palette via CSS variables.

### Figure 2.3 — Routes of resistance to anti-VEGF therapy
Build a hub-and-spoke node-edge systems diagram. One blocked source node on the left: "VEGF / VEGFR-2 axis (anti-VEGF blocked)" in vermillion (negative) with a block/cross glyph on its outgoing edge. One anchor outcome node on the right: "Sustained vascular supply / progression" (sky-blue anchor). Between them, five parallel secondary/transitional escape-route nodes each with an arrow into the outcome: alternative factors (FGF, PDGF, angiopoietins); vessel co-option of host vessels; pericyte-covered VEGF-independent vessels; myeloid recruitment (MDSCs, M2 macrophages); hypoxia-driven selection of invasive cells (transitional). Arrows are directional; the blocked VEGF edge is visibly cut. Color: blocked target = vermillion, escape routes = secondary, outcome = anchor. Subtitle "Five escape routes converge on sustained supply." Deliverable: single standalone HTML file, inline CSS, D3 v7 pinned CDN, Okabe-Ito colorblind-safe palette via CSS variables.
