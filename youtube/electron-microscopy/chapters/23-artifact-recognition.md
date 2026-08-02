# Chapter 23 — Artifact Recognition Across Techniques: A Comparative Synthesis


## TL;DR

- The same specimen can show different "features" in SEM, TEM, and EDS for reasons that have nothing to do with the specimen.
- The chapter moves through Warm-up, Application, Synthesis, Challenge.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

*The same specimen can show different "features" in SEM, TEM, and EDS for reasons that have nothing to do with the specimen. Knowing this is what separates a microscopist from a credulous image-reader.*

---

A graduate student is reading a paper that claims a novel nano-feature in a polymer composite: bright spots at roughly fifty nanometer spacing in an SEM image, identified as embedded gold nanoparticles. The paper shows a second panel — a backscattered electron image of the same field. In that image, the spots are darker than the polymer matrix.

Stop. In backscattered electron imaging, intensity scales with atomic number. Carbon, the main element in a polymer matrix, has $Z = 6$. Gold has $Z = 79$. A gold nanoparticle in a carbon matrix should appear dramatically brighter in BSE, not darker. The paper's interpretation is internally inconsistent: the two panels are telling opposite stories about the same location, and the authors did not notice.

What the student is actually looking at, in both panels, is charging. The polymer is insulating. At the kV the authors used, the polymer surface accumulated charge, and the bright halos in the SE image — which the authors called gold particles — are charge-induced artifacts. The SE detector, being sensitive to low-energy secondary electrons, is easily perturbed by surface electrostatic fields. The BSE detector, collecting high-energy backscattered electrons, is much less affected by surface charge, which is why the same locations appear at matrix contrast in BSE rather than bright. Neither panel shows gold particles. Both panels are showing charging in different ways, and the comparison between them makes it obvious — if you know what to look for.

The failure in that paper is not the experiment. The failure is the interpretation. The authors looked at one technique, believed it, and published. They did not apply the comparative check that would have taken perhaps twenty minutes.

This chapter is that check, formalized.

---

Every electron microscopy technique introduces its own artifacts. This is not a deficiency in instrument design; it is a consequence of the physics. The electron beam interacts with the specimen and the chamber and the detector in ways that produce signals unrelated to the structure the investigator wants to see. Some artifacts come from specimen preparation — the chemistry and mechanics of converting a real sample into something the instrument can handle. Some come from the imaging process itself. Some come from the detector and signal-processing chain. And the same specimen, imaged by different techniques at different conditions, can show different apparent "features" for entirely artifactual reasons.

The central skill this chapter teaches is triangulation: using multiple techniques, multiple conditions, or multiple specimen preparations to decide whether something you see is a property of the specimen or a property of the measurement.

---

Start with the taxonomy, because you need a way to classify what you are looking at before you can reason about it.

Preparation artifacts are introduced before the specimen reaches the chamber. They are physical or chemical changes made to the specimen. Drying shrinkage in biological SEM — cells that appear collapsed relative to their native morphology because surface tension during drying pulled them inward. Fixation artifacts in TEM — cells that appear swollen or shrunken because the osmolarity of the fixative was wrong relative to the cytoplasm. Microtomy chatter — parallel ridges across a section because the knife was dull or the specimen arm vibrated. FIB curtaining — vertical streaks across a lamella because the gallium beam did not cut uniformly through a heterogeneous material. Heavy-metal stain precipitation — bright granular deposits on a TEM grid section because the uranyl acetate solution was contaminated or exposed to ultraviolet light.

These artifacts are in the specimen. You cannot remove them by changing imaging mode. The specimen must be re-prepared. The only corrective is recognizing them early enough — ideally at the thick-section light-microscopy stage, or at the first overview image — to avoid investing imaging time on a compromised specimen.

Imaging artifacts are introduced during data acquisition. Charging in SEM is the most common: the electron beam deposits charge faster than the insulating specimen can drain it, the surface electric field deflects subsequent secondary electrons and the incident probe, and the image shows bright halos, stripe patterns, and local contrast reversals that have nothing to do with the underlying structure. Drift — the slow mechanical movement of the specimen stage during a long acquisition — blurs features along the scan axis in SEM and smears images in TEM. Astigmatism in either instrument produces directional blur that rotates 90° through focus, recognizable if you know what to look for. Bend contours in TEM — dark bands that sweep across crystalline specimens as the orientation of the crystal relative to the beam changes with tilt — are not defects; they are regions of strong diffraction that produce locally depleted bright-field images, and they can be moved or eliminated by tilting the specimen.

Unlike preparation artifacts, imaging artifacts can sometimes be eliminated without re-preparing the specimen. Drop the kV, and charging often disappears — because at lower accelerating voltage, the secondary electron yield of many insulators exceeds one, meaning more electrons leave the specimen than arrive, and the surface charge equilibrates near zero. Change the tilt, and bend contours move or vanish. Run the stigmator correction, and astigmatic blur disappears. The imaging artifacts are in the measurement, not the specimen, and the measurement can be changed.

Detector and analytical artifacts are a third category. The Everhart-Thornley detector in SEM, being an electrostatic collector of low-energy secondary electrons, produces an image where thin edges and protrusions facing the detector appear disproportionately bright — not because they contain more signal, but because they are geometrically positioned to emit secondary electrons more efficiently in the detector's direction. In EDS, sum peaks appear at energies that are exactly twice the energy of a strong characteristic peak: they result from two photons arriving at the detector simultaneously and being recorded as one event with combined energy. Escape peaks appear below strong peaks by 1.74 keV, the silicon fluorescence energy of the Si(Li) or SDD detector itself. Neither sum peaks nor escape peaks represent elements in the specimen.

| Category | Example artifacts | Corrective action |
|---|---|---|
| **Preparation** | Knife marks, charging from incomplete coating, fixation artifacts (extraction, shrinkage), beam damage during cryo-section thinning, contamination layers | **Re-prepare** the specimen — adjust the protocol upstream; the artifact is built in before the microscope |
| **Imaging** | Drift smear, astigmatism, defocus, aperture-misalignment asymmetry, charging during scan, mass loss under beam, tilt-series misalignment | **Change operating conditions** at the microscope — the specimen is fine, the parameters are wrong |
| **Detector / analytical** | Beam-damage artifacts in EDS line scans, EELS quantification errors from plural scattering, count-rate saturation, spectral-overlap misassignment, detector geometry effects | **Adjust acquisition parameters** — count rate, dwell time, deconvolution, calibration |

---

The question "is this real?" has a reliable method. It is not complicated, but it requires discipline to actually do rather than skip.

For any unusual feature — any bright spot, dark band, periodic pattern, or localized intensity anomaly — ask what a different technique would show at the same location.

SE and BSE tell opposite stories about composition. In SE, bright regions are surface-emitting (topography, edge effects, charging). In BSE, bright regions are heavy-element-enriched. If a feature is bright in SE and matrix-gray in BSE at the same location, the feature is a surface or charging artifact, not a composition anomaly. If it is bright in both, with the BSE brightness proportional to the expected $Z^2$ contrast, it is real.

Bright-field and dark-field in TEM tell opposite stories about scattering. In BF, regions that scatter strongly appear dark. In DF with the aperture on a specific scattered beam, those same regions appear bright. A feature that is dark in BF and fails to appear in DF at the expected aperture position is not a scattering feature — it is a defocus shadow, a Fresnel fringe, or a void. A feature that inverts correctly between BF and DF is real scattering.

Tilting resolves the question of whether a feature is structural or a beam-path artifact. Real structural features maintain their position relative to other features on the specimen as you tilt. Features that depend on the beam direction — charging shadows, certain contrast reversals in HAADF due to channeling — will shift position or change character when the specimen tilts. Tilt by 10° and observe.

Defocusing through the focus point reveals Fresnel fringes: they are bright-dark stripes that appear parallel to edges and interfaces in TEM, changing polarity between underfocus and overfocus, and disappearing at focus. They are phase-contrast artifacts of the edge, not structural features of the specimen. A real interface feature stays real throughout the focus series; a Fresnel fringe moves and inverts.

EDS at a suspected feature tells you whether a composition difference exists. A bright spot interpreted as a heavy-element inclusion should produce elemental peaks characteristic of that element at the suspected location. If the EDS spectrum at the spot is identical to the matrix, the spot has no compositional origin — it is morphological, charging, or beam damage. A real inclusion gives a distinctive spectrum.

Re-imaging after time tests for instability. Beam-induced features grow: carbon contamination deposits accumulate, ice in cryo-EM melts or builds, damaged polymer features evolve. Stable real features remain constant. If you return to the same field after an hour and the feature has changed, it is not a stable structural property of the specimen.

| Cross-check pair | What each technique is sensitive to | Artifact diagnosis if they disagree | Real-feature signature if they agree |
|---|---|---|---|
| **SE vs. BSE** | SE: surface topography + charging; BSE: average atomic number (Z) | Bright in SE only — likely charging artifact, not real Z-contrast | Both consistent — feature is morphologically *and* compositionally distinct |
| **BF vs. DF in TEM** | BF: amplitude/absorption + diffraction-out; DF: scattered intensity at a chosen angle | Visible in BF only — likely Fresnel/contamination contrast | Visible in both with reciprocal contrast — real diffracting feature |
| **kV variation** | Charging behavior changes with kV; intrinsic morphology does not | Feature appearance changes with kV — charging | Feature stable across 5/10/20 kV — real morphology |
| **Tilt series (TEM/SEM)** | Beam-path artifacts vary with tilt; structural features persist | Feature changes shape or disappears with tilt — likely projection artifact | Feature persists across tilts — real 3D structure |
| **Defocus series** | Fresnel fringes and contrast-transfer artifacts oscillate; real interfaces stay put | Edge brightness reverses through focus — Fresnel fringe, not interface | Edge contrast stable through focus — real material boundary |
| **EDS at the feature** | Composition-specific spectral signatures | No characteristic peaks at feature location — likely topographic shadow, not phase | Characteristic peaks → real elemental signal |
| **Re-image after time** | Stable specimens persist; beam-damaged specimens decay | Feature changes between first and second image — beam-damage artifact | Feature unchanged after 5–10 min — stable specimen |

---

The gold standard is reproducibility across independent preparations. If a feature appears in specimens prepared by two different methods — conventional chemical fixation and high-pressure freezing, for instance, or FIB milling from opposite faces of the same sample — and if it appears under different imaging conditions and in different instruments, then it has passed the strongest available test. Artifacts are preparation-specific, operator-specific, instrument-specific. Real features are not.

This standard is demanding and sometimes impractical in a busy research environment. The more achievable version is reproducibility within a session: the feature appears consistently across multiple fields, in multiple imaging modes, under conditions that would produce different artifacts. When every cross-check you can run in a two-hour session points to the same conclusion, the burden of proof shifts toward real.

---

The comparative check is most powerful when the techniques in question are sensitive to different physical signals. The reason SE and BSE are so useful together is that SE is dominated by surface emission and topography while BSE is dominated by atomic number. A feature can be explained by one physical mechanism or the other, but rarely both, and the comparison quickly narrows the possibilities. Similarly, HAADF-STEM and HRTEM are powerful together because HAADF is sensitive to atomic number and relatively insensitive to phase, while HRTEM is phase-contrast and relatively chemistry-blind within a single crystal structure. A composition change at an interface produces different signatures in the two modes, and seeing both is more convincing than seeing either alone.

EDS provides elemental specificity that morphological imaging cannot. EELS provides bonding-state information that EDS cannot. Crystallographic information from selected-area electron diffraction is orthogonal to the intensity information in a bright-field image. Each technique constrains the interpretation from a different direction. The more constraints that agree, the more confident the conclusion.

![Constraining a feature by independent measurements. Each technique is sensitive to a different physical signal; consistency across N of them is stronger evidence than consistency across one.](../images/23-artifact-recognition-fig-01.png)

*Figure 1.* Constraining a feature by independent measurements. Each technique is sensitive to a different physical signal; consistency across N of them is stronger evidence than consistency across one.


There is a failure mode worth naming explicitly: confirmation bias. Once a researcher has decided that a feature is real — especially if the feature supports an interesting scientific hypothesis — evidence of artifact-hood becomes easy to overlook. The bright SE spots were called gold particles because the paper's hypothesis required gold particles to be present. The BSE panel, which contradicted the interpretation, was included in the figure anyway but not discussed. The authors saw what they expected to see.

The corrective is to approach any unusual feature with the hypothesis that it is an artifact until evidence demonstrates otherwise. This inverts the natural tendency. It feels pessimistic. But it produces better science, because it forces the additional measurements that either confirm or eliminate the artifact hypothesis before publication.

---

The practical implementation of artifact skepticism is simpler than it sounds. It is mostly a habit of asking one question for every image: what else could produce this, and would that show up differently in a complementary measurement?

For an SEM SE image: does it change in BSE? Does it disappear at low kV? Does it move when the specimen is tilted?

For a TEM BF image: does the feature invert in DF? Does it move during defocus? Is it present in another specimen region prepared identically?

For an EDS map: are the peaks at the expected positions? Are sum or escape peaks present that could be misidentified as trace elements? Does the spatial resolution claimed in the map match what the interaction volume at the stated kV actually allows?

For an HRTEM lattice image: is the feature present across multiple fields? Does it survive a change in focus? Does an image simulation from the proposed structure match the observed contrast?

The questions are not hard. Answering them adds perhaps thirty to sixty minutes to a session. The alternative — publishing a result based on an artifact and retracting it eighteen months later — costs orders of magnitude more in time, credibility, and scientific productivity.

---

Step back and look at what is actually happening when multiple techniques are used to cross-check a result. Each technique samples the same physical specimen through a different physical interaction: secondary electron emission, backscattering from atomic nuclei, coherent interference of transmitted waves, incoherent high-angle scattering, characteristic X-ray emission. These interactions are physically independent. Two physically independent measurements that agree on the same feature are strong evidence that the feature is real. Two measurements that disagree are evidence that one of them is showing an artifact.

This is the logic of any experimental science. You design measurements that are sensitive to the phenomenon you are studying and insensitive to the things you are not studying, and you require that independent measurements agree before drawing conclusions. Electron microscopy has an unusually rich set of orthogonal measurements available — in many cases, in the same instrument, within the same session. The discipline to use them is what the field owes to itself, and what every microscopist owes to the reader of their published figures.

The student who spotted the BSE/SE inconsistency in the retracted paper did not have access to the original instrument or the original specimen. The authors did. They simply didn't look.

---

**What would change my mind:** evidence that any single EM technique produces artifact-resistant results without cross-checking on a wide range of specimen types and research questions. The empirical record — decades of retractions, corrections, and post-publication debates in high-profile journals — consistently shows the opposite. Single-technique evidence is over-interpreted at a rate that multi-technique cross-checking dramatically reduces.

**Still puzzling:** the practical threshold for "how much cross-checking is enough before publication" is almost entirely judgment-driven and community-norm-dependent. Materials science norms differ from biological EM norms; high-impact journals sometimes demand more; some subfields accept single-technique evidence as standard. A principled, quantitative framework for evidential sufficiency in EM imaging would be genuinely useful and does not, as far as I know, exist.

---

## Exercises

### Warm-up

**23.1** For each of the following unusual image features, name the most likely artifact category (preparation, imaging, or detector/analytical) and one technique change that would confirm or eliminate your hypothesis: (a) bright halos around features in an SEM SE image of an uncoated polymer; (b) parallel ridges crossing a TEM section perpendicular to the presumed knife direction; (c) a peak in an EDS spectrum at exactly twice the energy of the strongest characteristic line; (d) dark bands sweeping across a crystalline specimen in TEM BF that move when the specimen is tilted. *(Tests: artifact taxonomy and first-line diagnostic response.)*

**23.2** A feature appears bright in an SEM SE image and dark in an SEM BSE image at the same location. The specimen is a polymer matrix claimed to contain gold nanoparticles ($Z = 79$). What is the most likely explanation for this observation, and what is the physical reason the two detectors respond differently? *(Tests: SE vs BSE cross-check logic applied to the chapter's opening example.)*

**23.3** In TEM, a bright-dark fringe appears parallel to a grain boundary at both underfocus and overfocus, but reverses polarity between the two. At exact focus, it disappears. Name this artifact, explain its physical origin, and describe how to distinguish it from a real compositional variation at the boundary. *(Tests: Fresnel fringe identification and defocus-series diagnostic.)*

### Application

**23.4** A graduate student reports a new structural feature in a silicon film: 20 nm bright spots in HAADF-STEM that they interpret as oxygen-rich precipitates. Design a cross-check protocol with at least three independent measurements that would distinguish real oxygen precipitates from HAADF artifacts such as channeling or probe-spread blurring. For each measurement, state what result would support the "real" hypothesis and what result would support the "artifact" hypothesis. *(Tests: multi-technique cross-check design for a specific HAADF claim.)*

**23.5** A published EDS map of a stainless steel weld shows apparent phosphorus enrichment at the weld line at exactly half the energy of the sulfur K peak. Is this likely real? Name the artifact mechanism, explain why it appears at that specific energy, and describe how to confirm your diagnosis. *(Tests: EDS sum/escape peak recognition in a materials science context.)*

**23.6** You are reviewing a paper that shows an SEM image of an uncoated ceramic particle at 25 kV with the SE detector. The image shows fine surface texture at 10 nm resolution. The methods section contains no information about charging mitigation. List three reasons to be skeptical that the texture is real, and specify one additional experiment the authors should have reported. *(Tests: critical methods-section reading for artifact-resistance.)*

**23.7** A TEM BF image of a biological section shows what the authors describe as "membrane-bound vesicles" that appear as small circular features with bright interiors and dark rings. Identify the projection-ambiguity issue (revisiting Chapter 14), propose two alternative structural interpretations consistent with the same BF image, and specify a cross-check that would distinguish them. *(Tests: integration of projection-ambiguity reasoning with artifact skepticism.)*

### Synthesis

**23.8** A research group publishes a claim that a polymer nanocomposite contains self-assembled 50 nm gold nanoparticle superlattices. Evidence: a single SEM image at 20 kV showing regularly spaced bright spots, with a fast Fourier transform of the image showing periodic peaks. Evaluate this evidence systematically using the artifact taxonomy and at least four cross-checks. Identify the minimum additional evidence required before the claim would be credible. *(Tests: full diagnostic workflow applied to a multi-evidence claim, including recognizing that FFT periodicity can come from charging artifacts as well as real lattices.)*

**23.9** Read the following hypothetical methods sentence and identify every artifact-relevant detail that is absent: *"Nanoparticles were imaged by TEM at 100 kV. EDS confirmed the presence of Fe."* List five pieces of missing information that would be needed to evaluate whether the TEM images and EDS result are free of the most common artifacts for this specimen type, and explain why each piece matters. *(Tests: methods-section completeness evaluation from an artifact-resistance perspective.)*

### Challenge

**23.10** Find a published electron microscopy paper in your research field where the main claim depends substantially on a single imaging mode or technique. Evaluate whether the authors applied sufficient cross-checks to rule out the most common artifacts for that technique and specimen type. If cross-checks are absent, propose the specific measurements that would have been most informative. Write a paragraph-length critical commentary. *(Tests: independent artifact evaluation, critical literature reading, and scientific communication.)*

