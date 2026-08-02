# Chapter 26 — Designing, Reporting, and Critiquing Electron Microscopy Experiments


## TL;DR

- The methods section is not paperwork.
- The chapter moves through The reporting contract, What a complete methods section names, The figure and the claim it makes, Reading someone else's figures critically, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

*The methods section is not paperwork. It is the argument. Without it, the image is a rumor.*

---

A reviewer reads a paper claiming that single iron atoms have been imaged on a graphene support by HAADF-STEM. The headline figure shows bright dots. The dots are labeled "Fe atoms." The EDS spectrum from one dot shows an iron peak. The histogram shows dot diameters consistent with single atoms.

The methods section has one sentence on imaging: *"Imaging at 80 kV in STEM mode."*

The reviewer puts down the paper and writes a list. What convergence angle? What inner-collection angle for the HAADF detector? What beam current? What dwell time? What is the point-to-point resolution under those conditions at 80 kV — is it even sufficient to distinguish a single iron atom from a small cluster? How many dots were measured for the histogram — three or three hundred? What is the standard deviation? What was the negative control — graphene without iron, imaged at the same conditions, to confirm the bright dots don't appear spontaneously from contamination?

None of this is in the paper. The reviewer cannot reproduce the experiment. The reviewer cannot evaluate whether the bright dots are iron atoms, iron clusters, hydrocarbon contamination, or artifacts of the sample preparation. The result may be correct. But it is not defensible.

The authors revise. The methods section becomes four paragraphs. The instrument is named with model number, operating voltage, detector geometry, convergence angle, beam current, dwell time, and frame count. The histogram now states N = 152 atoms measured across 47 micrographs from three independent grid preparations. A negative control is added. The reviewer accepts the paper. Six months later, a reader in a different country opens the paper, reads the methods, and can reproduce the imaging conditions to within measurement precision.

That is what a methods section is for. It is not prose wrapped around numbers the journal requires. It is the mechanism by which a result becomes a result — verifiable, reproducible, falsifiable.

![Comparison of the "bad" and "good" HAADF-STEM methods](images/26-designing-reporting-critiquing-fig-01.png)
*Figure 26.1 — Comparison of the "bad" and "good" HAADF-STEM methods*

## The reporting contract

When you publish an EM figure, you are making an implicit contract with every future reader. The contract says: what I show is representative of the specimen, acquired under the conditions described, processed in the ways disclosed, and sufficient to support the conclusion drawn. The methods section is the written terms of that contract. A complete methods section is an honest methods section. An incomplete methods section is a contract with unwritten terms — and those are the terms that fail at peer review.

The standard is not "everything imaginable." It is "everything consequential." A parameter is consequential if changing it by a plausible amount would change the result or its interpretation. The accelerating voltage is consequential — 80 kV produces different radiation damage and different chromatic aberration than 300 kV. The HAADF detector's inner collection angle is consequential — a 50 mrad cutoff gives different Z-contrast sensitivity than an 80 mrad cutoff. The number of particles measured for a size distribution is consequential — N = 15 is an anecdote, N = 200 is a distribution. The software version is consequential — the same reconstruction algorithm can give different results in different versions, and the field has documented cases where this mattered.

What is not consequential varies by technique. The color of the lab walls is not in the methods section. The brand of lint-free gloves is not in the methods section. The time of day is usually not in the methods section, unless the experiment is measuring something temperature-dependent. The line is drawn by asking: if a competent person read only this methods section and tried to reproduce the result, what would they need to know?

## What a complete methods section names

For SEM, a complete methods section names the instrument (make and model), the accelerating voltage, which detector produced which image (secondary electrons, backscattered, in-lens, EDS — these produce different images of the same specimen), the working distance, the aperture, the beam current or spot size, the magnification range, and the sample preparation in enough detail that someone else can reproduce it from scratch.

For TEM, it names the instrument, the voltage, the mode (bright-field, dark-field, HRTEM, STEM), which detector, the camera length for diffraction, the dose in electrons per square angstrom for any beam-sensitive specimen, and — for any analytical mode — the acquisition parameters specific to that mode.

For EDS, those specific parameters include the dead time percentage, the counting time per point or per pixel, whether the detector was fully extended or retracted, and the sample tilt if it differs from zero.

For EELS, they include the energy dispersion, the energy resolution (zero-loss peak width), the exposure time, and whether a monochromator was used.

For cryo-EM single-particle analysis, they include the total dose, the number of frames and the framing rate, the motion-correction algorithm and software version, the CTF-estimation software, the particle count used in the final reconstruction, the 3D classification scheme, and the FSC criterion at which resolution is claimed.

For any population measurement — particle size distribution, grain size, film thickness — they include N, the software used, and the selection criteria (were particles excluded from the count, and if so, why).

This list is not exhaustive. The principle is: name every parameter that a competent reader would need to reproduce the experiment or to evaluate whether a specific artifact could explain the result. If you are not sure whether a parameter is consequential, include it. The supplementary materials section exists for exactly this purpose — it is a place to be comprehensive without taxing the main text.

## The figure and the claim it makes

Every EM figure makes a claim. The claim might be morphological ("these particles are spherical"), compositional ("the bright regions are iron-rich"), structural ("this material is crystalline"), or dimensional ("the mean diameter is 45 nm"). The figure's job is to make that claim visible. The caption's job is to make the claim explicit. The methods section's job is to make the claim defensible.

A scale bar is not decoration. It is the claim that the magnification is what is stated, and that the features visible in the image are the size the scale bar implies. A figure without a scale bar makes an unverifiable claim about every feature in it. This is why peer review routinely rejects figures without scale bars; it is not pedantry. It is the simplest possible test of whether the figure is making a verifiable claim.

![Two versions of the same SEM image ](images/26-designing-reporting-critiquing-fig-02.png)
*Figure 26.2 — Two versions of the same SEM image *

A caption that says "representative image" is making a population claim — that this image represents the distribution of what was found. That claim requires that the operator imaged enough fields to know what was representative, and chose this image to show it. If the image was chosen because it looked the best, or showed the most interesting feature, without context about whether that feature was common or rare, the "representative" label is not honest. The honest caption says how many particles or fields were examined, and why this one was selected.

The hardest discipline in figure preparation is restraint in image processing. Adjusting brightness and contrast uniformly across an entire image to make features visible is acceptable and conventional. Adjusting brightness and contrast selectively in different regions of the same image — brightening one part while leaving another dark — is manipulation. Gamma correction applied uniformly is conventional disclosure; gamma correction applied to push faint features above a threshold without documenting it is not. False color is fine if disclosed. Deletion of "artifact" features from an image is misconduct. The line is this: any processing that changes what a viewer concludes about the specimen, applied without disclosure, is falsification. When in doubt, disclose in the methods or caption and let the reader decide.

![Image processing spectrum ](images/26-designing-reporting-critiquing-fig-03.png)
*Figure 26.3 — Image processing spectrum *

## Reading someone else's figures critically

The same framework that makes your methods section defensible is the framework for reading a published paper. Every figure in the literature is a claim. The reviewer's discipline is to ask whether the claim is supported by the evidence shown and documented in the methods.

The six questions to ask about any published EM figure:

Is the technique named, and does it match the question? A paper claiming surface morphology but using TEM (which images through-the-bulk) is mismatched. A paper using EDS to distinguish oxidation states cannot do it — EDS cannot resolve chemical bonding.

Is the detector named? The same specimen imaged with an Everhart-Thornley detector and an in-lens TTL detector looks different, because they collect different signals. If the caption says "SEM image" without naming the detector, the reader cannot interpret what the image shows.

Are the operating conditions stated? kV, magnification, working distance. If they are not, the reader cannot evaluate whether the resolution claimed is consistent with the technique at those conditions.

What was the sample preparation? Many artifacts originate in preparation — dehydration artifacts in biological TEM, FIB-induced amorphization at the surface of a lamella, sputter-coating rippling on a soft polymer for SEM. If the preparation is not described, the artifacts it introduces cannot be evaluated.

How many observations support the claim? N = 1 is an anecdote. For any quantitative claim — size, composition, phase distribution — the reader should be able to find N in the methods or figure, and assess whether it is adequate for the precision claimed.

What cross-check or control is reported? A complementary technique that confirms the result, or a negative control that would have appeared if the artifact hypothesis were true. In the iron-atom paper: what did the carbon-only graphene (no iron, same prep) look like under the same imaging conditions? If bright dots appeared there too, the dots are not iron atoms. The absence of that control is the absence of a critical piece of the argument.

| Question to ask | Where to find the answer in the paper |
|---|---|
| **Does the technique match the question?** | Methods section — does the experimental design address the claim made in the abstract? |
| **Is the detector named?** | Figure caption *or* Methods section (e.g., "HAADF-STEM at 200 kV", "in-lens SE detector") |
| **What were the operating conditions?** | Methods section *or* supplementary information — kV, beam current, dwell time, dose |
| **How was the specimen prepared?** | Methods section — fixation, sectioning, staining, coating, cryo-vitrification protocol |
| **What is N? How many replicates?** | Results captions *and* Methods section — number of particles measured, biological replicates, technical replicates |
| **What controls were run?** | Methods section *or* supplementary figures — negative controls, isotype controls, vehicle-only specimens, beam-damage controls |

## The methods section as intellectual honesty

There is a temptation to regard the methods section as a burden — the prose you write after the science is done, listing the parameters that the instrument software recorded automatically. Resisting that temptation is what distinguishes careful science from careless science.

The methods section is where you say: here is exactly what I did, and here is why the reader can trust that what I showed them is real. It is an act of intellectual honesty, not compliance. A weak methods section does not just inconvenience a reviewer — it makes the result weaker. The result depends on the methods. If the methods are ambiguous, the result is ambiguous. The image is not evidence of anything without the chain of documentation that connects the image to the specimen to the preparation to the imaging conditions to the analysis.

This is not a new insight. Richard Feynman said something similar about experimental science generally: the first principle is that you must not fool yourself, and you are the easiest person to fool. The methods section is the mechanism by which you make it possible for others — and for yourself, when you return to this work in six months — to check whether you have fooled yourself.

## Closing the book

Twenty-five chapters of this textbook have covered the physics, the instruments, the techniques, the artifacts, and the workflows of electron microscopy. This chapter is the last one, and its subject is what all the prior chapters were building toward: work that can be published, read, critiqued, reproduced, and built upon.

The microscopist who completes this training can operate SEM and TEM, choose techniques by question rather than habit, recognize artifacts and design around them, prepare specimens for both biological and inorganic work, run multi-technique workflows, and now — write the methods section that makes all of it defensible.

The field's standards have risen with its capabilities. A paper claiming a novel nanostructure in 1970 might have been accepted on one carefully captioned electron micrograph. A paper claiming the same in the 2020s requires multi-technique cross-checks, population statistics, FSC criteria or equivalent rigor, and a methods section that a competent laboratory on another continent could follow to reproduce the result. That elevation of standards is not bureaucracy. It is the field learning to trust itself.

The lab work continues. The methods sections await. Write them completely.

---

## Exercises

### Warm-up

**26.1** A methods section reads: "Cryo-EM at 300 kV." List five specific parameters that are missing and that a competent reader would need to reproduce the experiment. For each, explain in one sentence why that parameter is consequential rather than merely desirable. *(Tests: identifying the "consequential" standard for methods completeness)*

**26.2** An SEM figure shows particles with no scale bar. The caption says "representative image at high magnification." Name two distinct claims this figure is failing to support, and state what would need to be added to support each. *(Tests: scale bar as verifiable claim + "representative" as population claim)*

**26.3** A paper reports a HAADF-STEM image with "bright spots representing single Pt atoms" and an EDS spectrum showing a Pt peak from the same region. A reviewer asks for a negative control. Describe what the negative control would be and what it would demonstrate if it showed bright spots too. *(Tests: control logic — what a negative control must show and why its absence leaves the claim open)*

### Application

**26.4** Write a complete methods paragraph for the following imaginary SEM session, using the "consequential parameter" standard: FEI Quanta 650 FE-SEM, 15 kV, backscattered electron detector (solid-state, sum mode), working distance 10 mm, 60 μm objective aperture, 50 pA beam current, imaging at 5,000× to 100,000×, 5 μs dwell time, 212 particles measured for size distribution using ImageJ 1.53, three independent sample preparations. *(Tests: writing complete methods — student must organize the parameters into coherent prose and add what's implied but not stated, e.g., sample mounting)*

**26.5** A colleague shows you a TEM figure with five bright-field images of "representative" polymer nanoparticles. The caption names the instrument and voltage but not the detector mode, preparation, or N. The paper claims the particles are "uniformly 80 nm and spherical." Apply the six critical-reading questions and identify which are answered and which are not. Then state what one additional piece of information would most improve the credibility of the size claim. *(Tests: applying the six questions systematically and identifying the single most consequential gap)*

**26.6** A paper reports that two phases in a polished alloy are "clearly distinguished" in a BSE image, with one phase appearing bright and one dark. The methods say only "SEM-BSE imaging at 20 kV." What operating condition is missing that would help the reader evaluate whether the contrast difference reflects Z-contrast or geometric/topographic effects? Describe a simple experiment the authors could have done to distinguish between the two explanations. *(Tests: connecting methods completeness to artifact interpretation — requires linking the Z-contrast vs. topographic BSE distinction from Chapter 6 to the documentation standard)*

**26.7** You acquire a cryo-EM SPA dataset and your reconstruction reports 2.9 Å global FSC-0.143 resolution from 180,000 particles. Before submitting, you check the angular distribution plot and find that 75% of particles are in the same two orientations. Write two sentences that should appear in your methods or limitations section acknowledging this, and explain why the global FSC number alone is insufficient to characterize the reconstruction quality in this case. *(Tests: connecting preferred-orientation artifact from Chapter 21 to reporting standards — what the methods section must acknowledge even when the global metric looks good)*

### Synthesis

**26.8** A nanomedicine lab publishes a paper claiming that their lipid nanoparticles (LNPs) encapsulate mRNA in the aqueous core and that the lipid bilayer is continuous. The evidence is: one cryo-TEM image showing a ring-like structure, one EDS spectrum showing phosphorus (lipid headgroup), and one DLS size measurement. Apply the full reporting framework to critique this evidence: identify which claims are supported, which are not, what techniques are missing, what the methods section likely omits, and what a defensible version of this paper would require. *(Tests: full-chapter synthesis — technique selection, multi-technique workflow, methods completeness, and the "one image is an anecdote" problem applied to a realistic nanomedicine case)*

**26.9** Find a published EM paper in your research area. Apply all six critical-reading questions to one figure. Then check whether the methods section contains the parameters required for that figure's technique from the chapter's checklist. Write a one-paragraph reviewer comment that is specific, technically grounded, and constructive — not dismissive — naming exactly what is missing and why it matters for the paper's central claim. *(Tests: full critical-reading discipline applied to real literature — produces a reviewer-quality comment, not just a list of complaints)*

### Challenge

**26.10** A paper is retracted after the authors are found to have selectively enhanced contrast in one region of a HAADF-STEM image, making a cluster of atoms appear to be a single atom. Using the concepts in this chapter, explain: (a) why selective regional contrast enhancement crosses the line from acceptable processing to falsification, (b) what the reviewer could have asked during peer review that might have caught this, and (c) what structural feature of EM figure presentation makes this kind of manipulation both easy to perform and difficult to detect. Propose one change to publication practice that would reduce the risk of this class of error going undetected. *(Tests: integrating image processing ethics, reviewer diagnostic questions, and the systemic conditions that enable misconduct — requires the student to think beyond individual papers to the structure of the publication system)*

---

*What would change my mind:* evidence that publication standards for EM methods sections have uniformly improved across journals and disciplines over the past decade. The movement exists — journals like eLife and Nature journals have tightened reporting requirements — but enforcement is inconsistent, and the supplementary materials system, while intended to enable completeness, also enables burial of critical information. A uniform standard with mandatory structured methods reporting would help.

*Still puzzling:* the gap between what a methods section should contain and what peer review enforces varies significantly by journal, field, and reviewer. A reviewer who knows the technique reads the methods differently from one who does not. The incentive structure does not consistently reward methodological completeness.
