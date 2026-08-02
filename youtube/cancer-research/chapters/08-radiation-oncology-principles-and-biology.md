# Chapter 8 — Radiation Oncology: Principles and Biology
*The Same Total Dose. Two Completely Different Outcomes.*

Two patients lie on two linear accelerators. The first has a head-and-neck cancer; the plan calls for 70 Gray delivered in 35 daily fractions of 2 Gy over seven weeks. The second has the same total prescription written differently: 70 Gy delivered in ten fractions of 7 Gy, finishing in two weeks. Same total dose. Same beams. Same tumor.

The first plan controls the tumor and her spinal cord, salivary glands, and mucosa recover. The second plan, had it been delivered, would have been a catastrophe: the larger fractions would have driven the late-responding normal tissues — spinal cord especially — far past tolerance, risking permanent paralysis, while not improving tumor control enough to justify it. The total dose was identical. The biological dose to the normal tissue was not.

Radiation cannot distinguish a cancer cell from a spinal-cord neuron. It damages DNA indiscriminately. So how does the same total dose, divided differently, spare the patient or destroy her? The answer is the subject of this chapter: the therapeutic effect of radiation is not read off the total dose. It is engineered — produced by exploiting a measurable biological difference between tumor and normal tissue, fraction by fraction.

---

**Ionizing radiation** transfers energy to tissue, knocking electrons out of atoms, breaking chemical bonds, and generating reactive species. The most consequential target is DNA.

Damage happens two ways. **Direct damage**: radiation energy breaks a DNA bond outright. This dominates for high-LET (high linear energy transfer) radiation — alpha particles, protons at the end of their range — where the ionization density along the particle track is high enough to damage the DNA directly. **Indirect damage**: radiation ionizes the water surrounding DNA, producing hydroxyl radicals and other reactive oxygen species that diffuse a short distance and attack the DNA strand. This dominates for the low-LET X-rays produced by a clinical linear accelerator — the photons that deliver most of the world's radiation therapy.

The indirect mechanism has a dependency that matters enormously for how tumors respond: it requires oxygen. Oxygen reacts with carbon-centered radicals generated on the DNA to form stable, difficult-to-repair peroxide lesions. Without oxygen, the radical can be "fixed" (made repairable) by a sulfhydryl donor instead. The ratio of radiation damage in well-oxygenated versus hypoxic cells is the **oxygen enhancement ratio** — roughly 2.5 to 3 for low-LET radiation. Hypoxic tumor cells are two to three times more radioresistant. This is why the poor, chaotic vasculature that produces hypoxic tumor regions is not just a drug-delivery problem — it is a radiation-sensitivity problem too.

Among the lesions radiation produces — single-strand breaks, base modifications, DNA-protein crosslinks — the **double-strand break** is the most lethal, because both strands are severed and accurate repair requires homologous recombination, which is error-prone and may fail entirely. A standard clinical fraction of 2 Gy produces roughly 40 double-strand breaks per cell. Most are repaired; the unrepaired or misrepaired ones are the lethal events.

---

The relationship between dose and cell survival is described by the **linear-quadratic model**. The surviving fraction of cells after a dose *D* is:

$$SF = \exp(-\alpha D - \beta D^2)$$

The **α term** represents cell kill from a single radiation track — damage from one ionization event that is lethal on its own, proportional to dose. The **β term** represents cell kill from two separate, independent events that together become lethal — proportional to dose squared, because the probability of two independent events occurring depends on the product of their individual probabilities.

At low doses per fraction, the linear term dominates and the two are roughly in proportion for most tissues. At high doses per fraction, the quadratic term grows quickly and the slope of the survival curve steepens. This is why fraction size matters: large fractions activate more quadratic kill than small ones delivering the same total dose.

The ratio **α/β** is the dose at which the linear and quadratic contributions to cell killing are equal — where αD = βD², so D = α/β. At fraction sizes well below α/β, the linear term dominates; at fraction sizes above α/β, the quadratic term is increasingly important.

This ratio differs systematically between tissue types, and that difference is what makes fractionation work.

**High α/β tissues** — typically around 10 Gy — include most cancers and the acutely responding normal tissues: skin, mucosa, bone marrow. Their survival curve has a shallow shoulder, meaning fraction size matters relatively little. They respond primarily to total dose, not to how it is divided.

**Low α/β tissues** — typically around 3 Gy or less — are the late-responding normal tissues: spinal cord, brain, kidney, lung. Their survival curve has a pronounced shoulder, meaning they respond disproportionately badly to large fractions. The same total dose delivered in large fractions causes far more damage to these tissues than the same total dose in small fractions.

This is the asymmetry that makes fractionation therapeutic rather than merely convenient. When a tumor has a high α/β and a critical normal tissue at risk has a low α/β, small daily fractions punish the tumor with every fraction while allowing the normal tissue to repair between fractions. The tumor's biology makes it relatively insensitive to fraction size; the normal tissue's biology makes it highly sensitive to fraction size. Small fractions exploit that difference. Large fractions collapse it — and in the opening case, 7 Gy fractions would have collapsed the difference catastrophically against the spinal cord.

![Semi-log LQ survival curves: tumor (alpha/beta ~10, shallow shoulder) and late normal tissue (alpha/beta ~3, pronounced shoulder) near-identical at small fractions but diverging sharply at large fractions](images/08-radiation-oncology-principles-and-biology-fig-01.png)
*Figure 8.1 — LQ survival curves: where fractionation matters*

<!-- → [CHART: cell-survival curves under the LQ model — two curves, one labeled "tumor (high α/β ≈ 10)" with a shallow shoulder, one labeled "late-responding normal tissue (low α/β ≈ 3)" with a pronounced shoulder; at small fraction sizes (2 Gy) the curves are close together; at large fraction sizes (7 Gy) they diverge sharply with normal tissue showing far greater kill; the divergence region labeled "where fractionation matters most"] -->

---

The **therapeutic ratio** is the gap between the dose that controls the tumor and the dose that injures the normal tissue in the field. Fractionation does not change where the photons land — it changes the biology of how tumor and normal tissue respond to each fraction, widening that gap.

Fractionation is the act of engineering a therapeutic ratio out of an indiscriminate weapon.

For some cancers the ratio is comfortable. Hodgkin lymphoma is controlled at 20–30 Gy, well below the tolerance of any structure in the field. The margin for error is large. For head-and-neck cancers the ratio is narrow — 70 Gy is needed for tumor control, and salivary glands, spinal cord, pharyngeal mucosa, and mandible all have tolerances that hover within or near the treatment volume. Every Gy matters, and every fraction-size decision matters. The narrower the therapeutic ratio, the more the fractionation scheme, the beam geometry, and the dose constraints determine whether treatment helps or harms.

---

The classical framework for understanding why fractionated radiation works differently for tumor and normal tissue is the five Rs of radiobiology, attributed to Withers (Withers, 1975).

**Repair.** Between fractions, cells repair sublethal DNA damage — damage that is not immediately lethal but becomes lethal when combined with additional damage from the next fraction. Normal tissue generally repairs sublethal damage more efficiently and quickly than tumor tissue, which often has defective DNA-damage response pathways (mutant *TP53*, defective checkpoint signaling). This repair differential is the primary biological basis of the fractionation advantage: normal tissue fixes more of its damage before the next fraction arrives; tumor cells carry more of it forward into cumulative lethality.

**Repopulation.** During a multi-week treatment course, cells divide. For acutely responding normal tissues — gut epithelium, skin, oral mucosa — repopulation is how the tissue survives treatment; it replaces cells killed by each fraction and maintains function. But tumors repopulate too. A fast-growing head-and-neck cancer may regenerate between fractions at a rate that partially offsets cell kill, especially if the treatment course is prolonged by gaps. This is why treatment interruptions are dangerous for rapidly dividing tumors and why **accelerated fractionation** — delivering the same total dose faster, sometimes with multiple fractions per day — reduces the time available for tumor repopulation.

**Redistribution.** Cells at different phases of the cell cycle differ in their radiosensitivity. Cells in G2/M — at or near mitosis — are the most sensitive; cells in S phase, actively synthesizing DNA and using homologous recombination repair pathways, are the most resistant. A single fraction kills the sensitive-phase cells preferentially, leaving the surviving population enriched in resistant cells. Over the next 6–24 hours, survivors redistribute through the cycle and enter more sensitive phases — making them more vulnerable to the next fraction. Fractionation works partly by this ratcheting effect.

**Reoxygenation.** Hypoxic tumor cells — 2–3× more radioresistant because the indirect damage mechanism needs oxygen — cluster around poorly perfused regions. A fraction kills the well-oxygenated cells near functioning vessels preferentially, reducing the oxygen demand in those regions, improving perfusion to formerly hypoxic areas, and exposing previously resistant cells to oxygen and to the full potency of the next fraction. This reoxygenation cycle, repeated across a multi-week course, is how fractionated radiation overcomes a resistance that a single large dose cannot.

**Radiosensitivity.** Intrinsic sensitivity varies by cell type and molecular state. BRCA-mutant cells, which lack functional homologous recombination, cannot repair double-strand breaks efficiently and are more sensitive to radiation. p53 status affects whether cells with unrepaired damage undergo apoptosis or slip through damaged checkpoints and die in mitosis later. Cell type — neuronal versus epithelial versus lymphoid — determines the baseline repair capacity. This R is less a modifiable clinical variable and more a reminder that population averages for α/β and repair rates are exactly that: averages, with patient-to-patient variation underneath.

A sixth R is sometimes added: **reactivation** of the immune system. Radiation can induce immunogenic cell death — releasing tumor antigens and damage-associated signals that activate dendritic cells and cytotoxic T cells — and can increase PD-L1 expression on surviving tumor cells, making them more susceptible to checkpoint inhibitor therapy. This is the biological basis for radiation-immunotherapy combinations: radiation as both a local treatment and a systemic immune primer.

![Five-row, two-column comparison matrix of the five Rs (repair, repopulation, redistribution, reoxygenation, radiosensitivity), showing how each acts on tumor versus normal tissue between fractions](images/08-radiation-oncology-principles-and-biology-fig-02.png)
*Figure 8.2 — The five Rs: tumor vs. normal tissue*

<!-- → [DIAGRAM: five Rs across a fractionation course — five rows, one per R, with two columns (tumor and normal tissue), showing what happens between fractions for each R; repair: normal tissue repairs more efficiently; repopulation: both repopulate, normal tissue needs to; redistribution: both redistribute, increasing sensitivity; reoxygenation: hypoxic tumor cells gain oxygen and sensitivity; radiosensitivity: fixed property of each tissue shown as background shading] -->

---

The five Rs translate into specific fractionation strategies, each with a biological rationale.

**Conventional fractionation** — approximately 2 Gy per day, five days per week, for five to seven weeks — is the baseline. The 2 Gy fraction size is not arbitrary; it sits in the range where the therapeutic ratio between high-α/β tumors and low-α/β late-responding tissues is most favorable, and 24 hours between fractions allows late-responding tissues to complete most of their repair.

**Hypofractionation** — fewer, larger fractions — is justified when the tumor has a *low* α/β, because large fractions are then disproportionately effective against the tumor. Prostate cancer has an α/β estimated around 1.5 Gy — lower than most carcinomas and similar to late-responding normal tissue. This unusual radiobiology means large fractions are biologically efficient for prostate cancer. **Stereotactic body radiotherapy (SBRT)** regimens of 36–40 Gy in 5 fractions exploit this directly. The **START trials** established that moderate hypofractionation in breast cancer — 40 Gy in 15 fractions rather than 50 Gy in 25 — gives equivalent outcomes, consistent with an α/β estimate for breast cancer lower than the traditional assumption (START Trialists' Group, 2008).

**Accelerated fractionation** maintains fraction size near 2 Gy but compresses the overall treatment time — sometimes delivering two fractions per day, separated by at least 6 hours to allow repair. The rationale is the repopulation R: reducing time for tumor regeneration in fast-dividing cancers without increasing the biological dose per fraction. Head-and-neck cancer, where accelerated repopulation is clinically significant, is the canonical application.

**Stereotactic radiosurgery and SBRT** use extreme hypofractionation — 10–25 Gy per fraction in one to five fractions — made feasible by highly conformal beam geometry that concentrates dose in the target and falls steeply outside it. At these fraction sizes the LQ model's predictions are less reliable; vascular damage and immune mechanisms may contribute meaningfully to the effect, and the clinical evidence from trials is more informative than the model's extrapolation `[contested — see pantry flag]`.

---

Compare two prostate cancer treatment plans, given prostate α/β ≈ 1.5 Gy:

Plan A: 60 Gy in 30 fractions of 2 Gy (conventional). Plan B: 36.25 Gy in 5 fractions of 7.25 Gy (SBRT).

The naive comparison: 36 Gy is much less than 60 Gy, so Plan B badly undertreats the tumor.

This is exactly the trap the opening case sets. Total Gy is not biological effect. Two schedules with different fraction sizes are not on the same biological scale. Comparing their physical totals is like comparing the mass of a bullet to its velocity and calling that energy — the numbers are different units of a phenomenon that depends on both.

The common currency is **biologically effective dose (BED)**:

$$BED = n \cdot d \cdot \left[1 + \frac{d}{\alpha/\beta}\right]$$

where *n* is the number of fractions and *d* is the dose per fraction.

**Plan A** (α/β = 1.5):
$$BED = 60 \cdot \left[1 + \frac{2}{1.5}\right] = 60 \cdot [1 + 1.33] = 60 \cdot 2.33 = \textbf{140 Gy}_{BED}$$

**Plan B** (α/β = 1.5):
$$BED = 36.25 \cdot \left[1 + \frac{7.25}{1.5}\right] = 36.25 \cdot [1 + 4.83] = 36.25 \cdot 5.83 = \textbf{211 Gy}_{BED}$$

Plan B delivers a higher biologically effective dose to the prostate tumor, not a lower one. The 7.25 Gy fractions land on the steep part of the LQ survival curve for a tissue with α/β of 1.5 — a low-α/β tissue responds disproportionately badly to large fractions, and the prostate tumor's α/β is in that range. Physical dose of 36 Gy is biologically more than 60 Gy for this tissue, at this fraction size.

Now apply the same arithmetic to the rectal wall at risk — a late-responding normal tissue with α/β ≈ 3 Gy — to check whether Plan B is safe:

**Plan A** (α/β = 3): BED = 60 · [1 + 2/3] = 60 · 1.67 = **100 Gy**BED
**Plan B** (α/β = 3): BED = 36.25 · [1 + 7.25/3] = 36.25 · [1 + 2.42] = 36.25 · 3.42 = **124 Gy**BED

The rectal BED is higher under Plan B than Plan A. This is why SBRT for prostate cancer requires precise, conformal targeting that minimizes rectal dose per fraction — the biological amplification that makes Plan B efficient for the tumor also makes it more demanding on adjacent normal tissue. The physics and the radiobiology must both be right.

![Grouped bar chart of biologically effective dose: SBRT 36.25 Gy delivers a higher BED to the prostate tumor and the rectal wall than conventional 60 Gy, showing physical Gy and biological effect are different scales](images/08-radiation-oncology-principles-and-biology-fig-03.png)
*Figure 8.3 — Same physical dose, different biological dose*

The limit of this reasoning: at the extreme fraction sizes used in SBRT, the LQ model is an approximation. Vascular damage, endothelial death, and radiation-triggered immune activation may contribute to tumor control through mechanisms the model does not capture, and BED calculations at 7–25 Gy per fraction may underestimate or overestimate the true effect. Clinical trial evidence from SBRT outcomes is more reliable than the model's extrapolation at these extremes `[verify against current SBRT literature]`.

---

The five Rs are not five independent variables a radiation oncologist adjusts separately. They are five manifestations of the same underlying fact: tumor and normal tissue respond differently to radiation, and fractionation schedules that exploit those differences — through repair time, reoxygenation cycles, redistribution through the cell cycle, control of repopulation — widen the gap between tumor control and normal-tissue damage.

The discipline of radiation oncology is the engineering of that gap. The LQ model and the α/β ratio quantify it. The five Rs explain why it exists and what each fraction does to sustain it. The therapeutic ratio is what results when the engineering succeeds.

The hard cases are the ones where the ratio is narrow to begin with — head-and-neck cancers with multiple critical structures in close proximity, glioblastoma where the brain is the surrounding normal tissue, lung cancers adjacent to central airways and the spinal cord. In those settings, every design decision — fraction size, total dose, treatment duration, beam arrangement — is a lever on the therapeutic ratio, and getting the lever wrong is how 70 Gy in 35 fractions and 70 Gy in 10 fractions produce outcomes as different as controlled disease and permanent neurological injury.

---

## Exercises

**Warm-up**

1. *[Recall — moderate]* Distinguish the direct and indirect mechanisms of radiation-induced DNA damage. Which mechanism dominates for clinical X-rays, what does it require to produce the full extent of DNA damage, and what does that requirement explain about the radiosensitivity of hypoxic tumor cells?
*What this tests: whether you can connect mechanism (indirect, oxygen-dependent) to clinical consequence (hypoxic resistance) — not just name the two mechanisms.*

2. *[Recall — moderate]* Define α/β ratio and explain what a high α/β tissue and a low α/β tissue each predict about sensitivity to fraction size. Name one cancer and one late-responding normal tissue with their approximate α/β values, and state in one sentence what the difference between them makes possible.
*What this tests: the α/β concept as a clinical tool — whether you can connect the number to the fractionation decision it licenses.*

3. *[Recall — moderate]* State the five Rs of radiobiology and for each name the biological process it describes and whether it favors the tumor, favors the normal tissue, or can go either way depending on circumstances.
*What this tests: whether you understand the five Rs as mechanisms rather than a list — the "can go either way" answer for repopulation is the one that separates mechanism from memorization.*

**Application**

4. *[Apply — moderate-hard]* Using the five Rs, predict what happens to a head-and-neck cancer treatment course interrupted for two weeks by a machine breakdown. For each of the five Rs, state whether the interruption improves or worsens the therapeutic ratio, explain the mechanism, and identify which single R poses the greatest danger to tumor control during the gap. Then describe what fractionation strategy is used to recover from prolonged treatment gaps and explain its radiobiological basis.
*What this tests: applying the five Rs to a dynamic clinical scenario rather than a static description — each R must be evaluated for its direction of effect during the interruption.*

5. *[Apply — moderate-hard]* A late-responding normal tissue has α/β = 3 Gy. Compute the BED for (a) 60 Gy in 30 fractions of 2 Gy and (b) 60 Gy in 10 fractions of 6 Gy. Show the arithmetic for both. Explain in two sentences why the same total dose gives a higher BED under the large-fraction schedule, and connect this specifically to the risk of spinal cord injury in the opening case.
*What this tests: numerical application of the BED formula and connection to clinical consequence — the numbers must be shown, not just stated.*

6. *[Apply — hard]* For a tumor with α/β = 10 Gy, design two fractionation schedules that deliver approximately equal tumor BED — one conventional (2 Gy/fraction) and one moderately hypofractionated (3–4 Gy/fraction). Compute both BEDs. Then compute the BED delivered to a late-responding normal tissue (α/β = 3 Gy) in the field by each schedule and state what the comparison tells you about whether the hypofractionated schedule is safe. Name the clinical trial evidence you would want before adopting the hypofractionated schedule.
*What this tests: end-to-end fractionation design — computing tumor BED equivalence, then checking normal-tissue BED, then naming the clinical evidence requirement.*

**Synthesis**

7. *[Synthesis — hard]* The opening case involved 70 Gy in 35 fractions (safe) versus 70 Gy in 10 fractions (catastrophic). Compute the BED for the spinal cord (α/β = 2 Gy) under each schedule and explain quantitatively why the two-week schedule would have caused permanent injury. Then use the same arithmetic to explain why prostate cancer SBRT (36 Gy in 5 fractions) is safe for the prostate but requires careful management of rectal dose — showing the BED calculation for both the prostate (α/β = 1.5) and the rectal wall (α/β = 3) under both the conventional and SBRT schedules.
*What this tests: integrative quantitative reasoning across two clinical scenarios using the same BED framework; the spinal cord calculation grounds the opening case in numbers.*

8. *[Synthesis — hard]* Reoxygenation predicts that fractionation should overcome hypoxic tumor resistance by killing well-oxygenated cells and improving perfusion to formerly hypoxic regions between fractions. But hypoxic tumors remain stubbornly radioresistant in practice, and adding hypoxia-directed strategies (hypoxic radiosensitizers, FLASH irradiation) is an active clinical research area. Explain the mechanism by which reoxygenation should work, identify two specific reasons why it may be insufficient in practice, and describe what the clinical evidence for hypoxia-directed radiation strategies tells you about whether reoxygenation adequately compensates for hypoxic resistance across fractions.
*What this tests: mechanistic reasoning about the limits of one of the five Rs; moving from the theoretical prediction to the clinical gap.*

**Challenge**

9. *[Challenge — very hard]* The "Still Puzzling" section asks whether the LQ model breaks down at SBRT fraction sizes and whether vascular and immune mechanisms contribute importantly to SBRT's effect. Design a clinical or translational study that would distinguish between two models for SBRT efficacy: (1) the LQ model is adequate and direct DNA damage is the dominant mechanism, or (2) vascular damage and immune activation contribute meaningfully and the LQ model underestimates the effect at high fraction sizes. Specify the patient population, the imaging or biopsy endpoints you would use to measure each mechanism, the fractionation comparison arms, and the result pattern that would support each model. Then explain what the answer would mean for how SBRT doses should be designed — specifically, whether BED calculations can be trusted for SBRT schedule comparison or whether clinical trial evidence is irreplaceable at these fraction sizes.
*What this tests: translating a mechanistic uncertainty into a study design; connecting the LQ model's validity to its practical role in schedule comparison.*

---

## What Would Change My Mind

The central claim is that radiation's selectivity is engineered — produced by fractionation exploiting the α/β difference between tumor and late-responding normal tissue, as described by the linear-quadratic model and the five Rs — rather than being an intrinsic property of the radiation. What would revise this: convincing evidence that at the high doses used in modern SBRT, the dominant determinant of outcome is not the LQ/α/β framework but a distinct mechanism — vascular collapse, endothelial death, or radiation-triggered immunity — that fractionation reasoning fails to capture. If clinical outcomes at extreme fraction sizes systematically departed from BED predictions in a way explained by these alternative mechanisms, the "engineered therapeutic ratio via α/β" account would become a special case valid only at conventional fraction sizes. The data on this are actively debated `[contested — see pantry flag]`.

## Still Puzzling

- Does the linear-quadratic model break down at SBRT fraction sizes, and if so, what replaces it — vascular effects, immune activation, or a modified LQ? `[contested — see pantry flag]`
- How much of SBRT's effect is direct DNA-damage cell kill versus indirect (vascular and immune) mechanisms, and can the two be disentangled clinically? `[verify]`
- Reoxygenation predicts that fractionation should overcome hypoxia, yet hypoxic tumors remain stubbornly radioresistant. Why doesn't reoxygenation fully rescue them, and which hypoxia-directed strategies actually help?
- Can we measure a patient-specific α/β or radiosensitivity before treatment, rather than relying on population averages — and would individualizing fractionation on that basis improve the therapeutic ratio?

## References

- Withers, H. R. (1975). The four R's of radiotherapy. *Advances in Radiation Biology*, 5, 241–271.
- START Trialists' Group. (2008). The UK Standardisation of Breast Radiotherapy (START) Trials. *Lancet Oncology*, 9(4), 331–341.
- National Cancer Institute. *Radiation Therapy to Treat Cancer.* https://www.cancer.gov/about-cancer/treatment/types/radiation-therapy

---

## Prompts

### Figure 8.1 — LQ survival curves: where fractionation matters
Build a two-curve semi-log survival plot (linear-quadratic model). X-axis = dose per fraction in Gy (linear); Y-axis = surviving fraction on a logarithmic scale, descending. Plot two curves from the same origin: "Tumor (alpha/beta ~10)" with a shallow, near-straight shoulder rendered as the dominant/anchor curve in blue; "Late normal tissue (alpha/beta ~3)" with a pronounced rounded shoulder bending steeply downward, in vermillion to signal harm. The curves should sit nearly together at small fraction sizes (~2 Gy) and diverge sharply at large fraction sizes (~7 Gy), with the normal-tissue curve dropping far below. Add a vertical reference line at ~2 Gy ("conventional fraction") and shade or annotate the high-fraction divergence region "where fractionation matters most." Annotate each shoulder. Deliverable: single standalone HTML file, inline CSS, D3 v7 pinned CDN, Okabe-Ito colorblind-safe palette via CSS variables.

### Figure 8.2 — The five Rs: tumor vs. normal tissue
Build a five-row, two-column comparison matrix. Left column header "Tumor," right column header "Normal tissue." One row per R, top to bottom: Repair (tumor: limited repair / normal: stronger sublethal repair — favors normal tissue, green accent on the normal cell); Repopulation (both repopulate — neutral gray); Redistribution (both redistribute into sensitive phases — neutral); Reoxygenation (tumor: hypoxic cells reoxygenate and become vulnerable, blue dominant accent / normal: already oxygenated); Radiosensitivity (both: intrinsic, fixed — neutral background shading). Each cell holds a short phrase. Use color to encode where each R widens the therapeutic gap: green = favors normal tissue, blue = dominant effect, gray = neutral/either-way. Label the matrix "Effect between fractions." Deliverable: single standalone HTML file, inline CSS, D3 v7 pinned CDN, Okabe-Ito colorblind-safe palette via CSS variables.

### Figure 8.3 — Same physical dose, different biological dose
Build a grouped vertical bar chart of relative biologically effective dose (BED). Zero baseline required. Two tissue groups — "Prostate tumor" and "Rectal wall" — each with two bars: conventional 60 Gy and SBRT 36.25 Gy. Values (relative): prostate tumor conventional 100, prostate tumor SBRT 130; rectal wall conventional 90, rectal wall SBRT 110. Y-axis = "Biologically effective dose (relative)." Color semantics: prostate tumor bars in blue (the intended/dominant target), rectal wall bars in vermillion (the at-risk normal tissue/harm). Highlight the two SBRT bars (e.g., heavier outline) to show that the same lower physical dose produces a higher biological effect in both tissues. Annotate "physical Gy is not biological effect." Sort groups tumor then rectum; within each group conventional then SBRT. Deliverable: single standalone HTML file, inline CSS, D3 v7 pinned CDN, Okabe-Ito colorblind-safe palette via CSS variables.
