# Chapter 24 — Choosing the Right Electron Microscopy Technique


## TL;DR

- A graduate student arrives at the EM facility with an antique key and a question: how is the iron distributed in the rust?
- The chapter moves through Five dimensions of the choice, The first rule: start broad, narrow in, Matching question to technique: the working map, When multi-technique workflows are not optional, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

*The question comes first. The technique follows. Every other order is superstition.*

---

A graduate student arrives at the EM facility with an antique key and a question: how is the iron distributed in the rust? The facility has eleven techniques on offer across four instruments. The student, trained on SEM, instinctively reaches for the SEM.

This is the wrong instinct — not because SEM is wrong, but because the student has not thought about the question carefully enough to know whether SEM is right. The question has at least two scales embedded in it: macroscopic (where on the key does corrosion concentrate?) and microscopic (in which specific layer, at what depth, with what chemistry?). SEM-EDS will answer the macroscopic question well. It will not answer the microscopic question. To know the iron oxidation state in a 50 nm corrosion layer between two grains, you need STEM-EELS on a FIB-prepared lamella — a different instrument, a different session, and three days of additional preparation.

The student who picks SEM and stops there will publish a partial result. The student who picks SEM first, reads what it reveals, and uses that to justify STEM-EELS next will publish a complete one. The discipline of technique selection is the discipline of thinking clearly about what information each technique actually produces, at what scale, with what artifacts, and at what cost — and then building a workflow that assembles those pieces in the right order.

This chapter is that discipline.

## Five dimensions of the choice

Every technique-selection decision lives in five-dimensional space. The dimensions are not independent, but naming them separately helps avoid the most common mistake, which is thinking about only one of them.

**Information type** is the most fundamental. What does the question actually ask? Surface morphology is a different question from internal structure, which is different from elemental composition, which is different from chemical bonding state, which is different from crystallographic phase. The EM toolkit has distinct techniques optimized for each:

Surface morphology is the domain of SEM — secondary electrons, topographic contrast, the familiar light-and-shadow image. Internal structure is the domain of TEM — the beam passes through, the image is a projection through the volume. Elemental composition is EDS in either SEM or TEM, with spatial resolution set by the interaction volume. Chemical bonding state — whether iron is Fe²⁺ or Fe³⁺, whether carbon is graphitic or amorphous — is the domain of EELS. Crystallographic structure, down to unit-cell identification, is SAED in TEM or EBSD in SEM. Three-dimensional internal structure is tomography. Native hydrated biological structure is cryo-EM.

These are not interchangeable. You cannot get oxidation state from EDS. You cannot get internal structure from SEM. The first question to ask about any specimen is: what category of information does my question require?

**Spatial resolution required** sets the instrument. A feature that is 10 μm across is visible in a light microscope, a low-magnification SEM image, and a TEM survey micrograph. A feature that is 0.5 nm across requires aberration-corrected HRTEM or HAADF-STEM and cannot be seen in a conventional SEM at any voltage. Mismatching scale to technique produces images that are technically correct and scientifically useless. The question "how big is the smallest feature I need to resolve?" must have an honest answer before any instrument is touched.

The rough hierarchy: optical microscopy handles above ~200 nm. SEM handles from ~1 μm down to ~1 nm at the best FE-SEM with modern detectors. Conventional TEM handles down to ~0.2 nm. Aberration-corrected STEM handles below 0.1 nm, into the regime where individual atomic columns are visible.

**Specimen compatibility** is the constraint that most often surprises students. The specimen is not just a passive subject — it has physical and chemical properties that interact with the technique in ways that can prevent imaging altogether or produce artifacts that look like results.

A hydrated biological sample will outgas in the vacuum of a conventional SEM and collapse in the electron beam. An insulating polymer charges under the beam unless you coat it, lower the kV to the crossover energy, or use a variable-pressure instrument. A magnetic specimen can deflect the beam or magnetize the pole pieces. A beam-sensitive organic crystal can recrystallize or decompose under a standard TEM dose before you finish focusing. None of these are reasons to give up — they are reasons to plan the prep and the imaging conditions accordingly.

**Prep burden** is the practical economics of the investigation. The difference between SEM of a bulk metal (mount it, pump it down, image it — thirty minutes total) and cryo-EM single-particle analysis (weeks of specimen optimization before useful data appears) is not a small logistical detail. It is a factor of a hundred in labor. Before committing to a technique, the question "how long will this take to prepare?" deserves an honest answer. Many questions that seem to demand TEM can be answered at least provisionally by SEM in a fraction of the time, at a fraction of the cost, leaving TEM for the follow-up that genuinely requires it.

**Artifact risk** is the dimension most often ignored and most often regretted. Chapter 23 catalogs the artifacts of each technique. The relevant question here is not "does this technique have artifacts?" — they all do — but "which artifacts does this technique have, and are they a problem for my specific question?" A charging artifact in SE imaging is obvious and easily mitigated. A channeling artifact in STEM-EELS is subtle and can produce apparent oxidation-state gradients that are completely artifactual. For any question where the answer is novel or surprising, a technique with a known artifact that could produce the same apparent result requires a cross-check.

## The first rule: start broad, narrow in

Given those five dimensions, there is one overriding principle: start with the broadest, fastest, cheapest technique that addresses the question at the scale you care about, and use what you learn to justify the next step.

This is not timidity. It is efficiency. SEM of a corroded key takes an afternoon and produces an elemental map of the whole surface, identifying which regions are most interesting. TEM-EELS of a FIB lamella from the most interesting region takes a week and produces nanoscale oxidation-state data. The SEM step is not redundant — it is the navigation that makes the TEM step tractable. Without it, you are preparing lamellae blindly and spending expensive instrument time hoping you hit the right region.

The same logic applies at every scale. An optical micrograph before the SEM session. An SEM survey before the TEM session. A low-magnification TEM bright-field before the HRTEM session. Each step narrows the field of view to the region that actually answers the question, at the resolution that actually requires it.

The student who inverts this — who starts with the most powerful technique and works backward — wastes time, accumulates artifacts, and sometimes damages the specimen before the right region has been identified.

## Matching question to technique: the working map

For each major category of question, there is a first-choice technique and a set of extensions.

**Surface morphology, micron scale:** SEM with secondary electrons. For insulators, low-kV imaging or VP-SEM. For the absolute finest surface features at sub-nanometer resolution, a through-the-lens detector on a Schottky FE-SEM at low kV. Extensions: EDS for composition, BSE for Z-contrast.

**Surface morphology, sub-10 nm:** This is at the edge of what SEM can do and requires careful technique. An FE-SEM with an immersion objective and a TTL detector at 1–3 kV. Alternatively, a TEM lamella prepared from the surface of interest, imaged in STEM bright-field.

**Internal ultrastructure, biological:** Conventional TEM with bright-field on a stained and sectioned specimen (Chapter 20). Extension: tomography for three-dimensional structure, cryo-EM for native-state conformations.

**Internal ultrastructure, materials:** TEM with bright-field and dark-field imaging. SAED for phase identification. For atomic-resolution, HRTEM or HAADF-STEM. Extension: EELS for chemistry, EDS for composition. Site-specific access via FIB lamella preparation (Chapter 22).

**Elemental composition, micron scale:** EDS in SEM. Fast, reliable, covers most elements above Z ~5. Spatial resolution set by the interaction volume — 1–2 μm at 20 kV in metals.

**Elemental composition, nanometer scale:** STEM-EDS or STEM-EELS. The probe diameter (sub-angstrom in modern instruments) and thin specimen set the resolution. For light elements (B, C, N, O), EELS is preferred because EDS fluorescence yields are too low. For heavy elements, EDS is faster and more quantitative.

**Chemical bonding state:** EELS, specifically the near-edge fine structure (ELNES) of core-loss edges. No other EM technique does this. For bulk specimens where EM access is expensive, XPS is an alternative — but XPS averages over a millimeter of surface, not a nanometer of specimen.

**Crystal phase identification:** SAED in TEM (Chapter 15) for small regions; XRD for bulk averages; EBSD in SEM for surface grain mapping. SAED from a 100 nm selected area is the only technique that identifies crystal phase of a specific grain, particle, or inclusion at that spatial scale.

**Atomic-resolution structure:** HRTEM or HAADF-STEM in an aberration-corrected instrument. Not every question requires this; atomic resolution is expensive in instrument time, specimen preparation, and expertise. Many materials questions are fully answered at 1–2 nm resolution.

**Three-dimensional internal structure:** Electron tomography (Chapter 19) for samples prepared for TEM. FIB-SEM slice-and-view for volumes that are too thick for TEM and need 3D at 10–50 nm resolution. For biological macromolecules at near-atomic resolution, cryo-EM single-particle analysis (Chapter 21).

**Native hydrated biological structure:** Cryo-EM, specifically vitrification followed by low-dose imaging. No other technique preserves the hydrated conformation of a membrane protein or a large molecular complex. The cost is months of optimization and terabytes of data. The reward is structures unavailable any other way.

## When multi-technique workflows are not optional

Some questions genuinely cannot be answered by a single technique. Recognizing this early — rather than after two weeks of effort on the wrong instrument — is the most valuable output of the discipline this chapter describes.

The pattern that signals a multi-technique question: the question contains an "and" that maps to two different information types, or two different scales, or two different specimen states.

"Confirm nanoparticle size distribution *and* verify crystalline phase" — size distribution is SEM (fast, statistical), crystal phase is SAED in TEM (slow, one particle at a time). One instrument for each.

"Map surface composition *and* identify oxidation state in a specific buried layer" — surface composition is EDS in SEM, oxidation state is EELS in STEM, buried layer requires FIB lamella. Three techniques, three sessions, a week of work.

"Image the lipid bilayer of a nanoparticle *and* localize mRNA inside the core" — bilayer imaging is cryo-TEM, mRNA localization is cryo-tomography. Two modes on the same instrument, but different acquisition protocols and processing pipelines.

In each case, the "and" is the signal. The student who tries to answer both parts of a compound question with a single technique will either fail to answer one part, or collect data with an inappropriate technique and accumulate the corresponding artifacts.

## Writing the choice into the methods section

Technique selection is not just a planning discipline — it is a communication discipline. A methods section that says "samples were imaged by SEM and TEM" has not done its job. A methods section that explains *why* each technique was chosen — what information need it addresses, what alternatives were considered, what artifact-mitigation steps were taken — is the methods section that survives reviewer scrutiny.

The standard questions a reviewer should be able to answer from reading your methods: Why this technique for this question? What is the spatial resolution relative to the feature of interest? What artifacts does this technique have that could affect the conclusion, and how were they checked? If a multi-technique workflow was used, how were the results from different techniques related to each other (same specimen region? same preparation batch?)?

A methods section that answers these questions does not require the reader to trust the authors — it allows the reader to evaluate the logic. That is the standard.

## The worked example, stated simply

Return to the rusted key. The student's question is: how is iron distributed in the rust?

The question has two scales. At the macroscopic scale — which regions of the surface are rust-rich, and what other elements are present — SEM-EDS answers in an afternoon. The elemental map identifies iron-rich corrosion at the surface, a chromium-depleted sub-surface zone, and the approximate depth of each layer.

That SEM-EDS result generates the next question: what is the iron oxidation state in the depletion zone, and does it differ between the surface corrosion and the buried layer? That question requires chemical-state information at 50 nm spatial resolution, which requires EELS, which requires a TEM specimen from that specific region, which requires FIB lift-out.

The total workflow: one afternoon of SEM-EDS to survey and locate, two days of FIB preparation to extract a lamella from the identified region, one day of STEM-EELS to measure oxidation state. Three techniques, four days, one complete answer.

No single technique could have produced that answer. The SEM gave the navigation; the FIB gave the specimen; the EELS gave the chemistry. Each was chosen because it was the best tool for one specific part of the question. That is how multi-technique EM works.

---

*What would change my mind:* evidence that any single EM technique can routinely substitute for the multi-technique workflows described here on complex materials or biological questions. The empirical record consistently shows that compound questions — those asking about multiple scales, multiple information types, or surface and interior simultaneously — require compound workflows. A technique that collapses this would be a genuine advance.

*Still puzzling:* the "good enough for publication" threshold for technique justification varies significantly across fields and journals. Materials science methods sections routinely include more technique-selection rationale than biological methods sections, even when the biological questions are equally complex. Whether this reflects disciplinary standards, reviewer expectations, or something deeper about how the fields think about methodology is not obvious.

