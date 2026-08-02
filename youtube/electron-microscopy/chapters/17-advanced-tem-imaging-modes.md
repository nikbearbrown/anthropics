# Chapter 17 — Advanced TEM Imaging Modes: HRTEM, STEM, and HAADF


## TL;DR

- HRTEM tells you where the atoms are.
- The chapter moves through Warm-up, Application, Synthesis, Challenge.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

*HRTEM tells you where the atoms are. HAADF tells you which atoms they are. Every other advanced TEM mode is a variation on those two sentences.*

---

A graduate student has prepared a thin lamella of an epitaxial germanium film on silicon by FIB lift-out, thinned the interface region to under ten nanometers. At the 200 kV TEM, with the objective aperture removed, the specimen tilted to the [110] zone axis of silicon, the screen shows a lattice — periodic bright spots, spacing 0.31 nm one way and 0.27 nm another. Each bright spot corresponds to a column of silicon atoms, or to the channel between columns, depending on focus. Across the interface to the germanium side, the lattice continues, same structure, slightly larger spacing because germanium atoms are bigger. At the boundary, a faint strain pattern.

The student switches modes to STEM. The wide flood illumination collapses to a focused probe. The image rebuilds point by point as the probe scans. The silicon side appears dim. The germanium side appears bright. Not a little brighter — substantially brighter. The interface is obvious in a way the phase-contrast image did not show.

Nothing changed in the specimen. What changed is which electrons were measured and how.

---

Start with what HRTEM is actually doing, because it is different in kind from everything before it.

In conventional bright-field TEM, the objective aperture sits at the back focal plane and admits only the direct beam — the electrons that were not scattered. Chapter 14 established that this produces amplitude contrast: regions that scatter strongly appear dark because they depleted the direct beam. Remove the aperture, and the direct beam and several diffracted beams all pass through to the image plane together. They interfere. The image is now a record of that interference — an intensity pattern whose periodicities match the spacings of the crystal planes that produced the diffracted beams. This is HRTEM, and the periodic spots in the image are lattice fringes.

The key word is *interference*. HRTEM is not imaging the atoms the way a camera images a scene. It is recording the interference pattern of electron waves that passed near and around the atomic columns. The intensity at each pixel depends on how the waves from different diffracted beams combined at that point: constructively, producing a bright spot, or destructively, producing a dark one. Whether a bright spot corresponds to an atomic column or to the channel between columns depends on the focus, the specimen thickness, and the particular diffraction conditions — and getting this mapping right requires either careful control of those conditions or comparison with simulated images computed from a known structural model.

![HRTEM is precisely the case where the aperture is removed and interference between direct and diffracted beams is allowed.](../images/17-advanced-tem-imaging-modes-fig-01.png)

*Figure 1.* HRTEM is precisely the case where the aperture is removed and interference between direct and diffracted beams is allowed.


This is what makes HRTEM simultaneously powerful and treacherous. The spatial resolution is extraordinary — sub-angstrom in aberration-corrected instruments — but the relationship between the image and the atomic structure is not straightforward in the way that, say, a photograph is straightforward. The image is a coherent superposition of waves, and the interpretation requires knowing the physics of that superposition.

For a silicon specimen oriented at the [011] zone axis, the relevant reflections are the (111) planes at 0.314 nm spacing, the (200) planes at 0.272 nm, and the (220) planes at 0.192 nm. An uncorrected 200 kV instrument, limited by spherical aberration to an information limit around 0.15–0.2 nm, will show the first two spacings cleanly and struggle with the third. An aberration-corrected instrument, where $C_s$ has been reduced to roughly one micrometer by multipole correctors, pushes that limit to 0.05–0.1 nm — sub-angstrom, where individual atomic columns are resolved and light elements like oxygen and carbon become visible.

| Reflection | d-spacing (nm) | Visible at 200 kV (uncorrected)? | Visible at 200 kV (aberration-corrected)? |
|---|---|---|---|
| (111) | 0.314 | **Yes** | **Yes** |
| (200) | 0.272 | **Yes** | **Yes** |
| (220) | 0.192 | **Yes** | **Yes** |
| (311) | 0.164 | Marginal | **Yes** |

*Reflections at d > 0.20 nm are routine on a clean uncorrected 200 kV instrument. Reflections below 0.20 nm require alignment discipline; aberration correction makes them routine.*

The resolution limit of HRTEM is therefore not the electron wavelength, which at 200 kV is about 2.5 pm — far below any atomic spacing. The limit is spherical aberration of the objective lens, exactly as Chapter 2 established for SEM. The difference is that in TEM the objective lens is the strongest in the column and the specimen sits inside its field, which makes aberration correction harder but also more impactful. When Haider and colleagues demonstrated the first practical spherical-aberration corrector for TEM in 1998, they were solving a problem that Otto Scherzer had proved to be fundamental for round magnetic lenses in 1936 — and solving it by adding non-round multipole elements that violate Scherzer's rotationally symmetric constraint. The result is instruments that can show, routinely, lattice fringes at spacings that would have seemed physically impossible to earlier generations of microscopists.

---

STEM reverses the architecture completely.

In conventional TEM, a broad, coherent beam illuminates the entire specimen simultaneously. The image forms by parallel acquisition — all pixels at once — through the objective and projector lenses. STEM instead focuses the beam to a probe as small as 0.05–0.1 nm in diameter and scans it across the specimen, collecting transmitted electrons at each scan position. The image is built sequentially, pixel by pixel, exactly as the SEM rasters its probe over a surface — except the specimen is thin enough for the electrons to pass through.

This architecture change has consequences that go well beyond the cosmetic similarity to SEM.

Because there are no imaging lenses below the specimen in STEM, there are no post-specimen projector lenses to introduce aberrations. The objective lens governs the probe size; after that, detectors simply collect whatever electrons arrive. And because the probe is scanned, different detectors at different angular ranges can collect different signals simultaneously from the same scan. Each detector produces a different image of the same specimen.

![STEM — three concentric detector zones below the specimen. One scan, three images, three contrast mechanisms.](../images/17-advanced-tem-imaging-modes-fig-02.png)

*Figure 2.* STEM — three concentric detector zones below the specimen. One scan, three images, three contrast mechanisms.


The detector on the optic axis, within the cone of the direct beam, produces a bright-field STEM image — conceptually analogous to BF in conventional TEM, though the details of contrast formation are not identical. Surrounding that central detector is a ring: the annular dark-field detector, collecting scattered electrons at moderate angles. This produces an ADF image where strongly scattering regions appear bright. Move to larger angular range — a bigger ring, farther from the axis, collecting only electrons scattered beyond about 50 milliradians — and you have the high-angle annular dark-field detector: HAADF.

HAADF is where the interesting physics lives.

---

At high scattering angles, something qualitative changes about how electrons interact with matter. For small angles, scattering involves the whole atom — nucleus and electron cloud together — and the scattering depends on the crystal structure, producing the coherent diffraction patterns that HRTEM exploits. For large angles, the electrons pass so close to the atomic nucleus that the interaction is dominated by the nuclear charge directly. The electron cloud of bound electrons is relatively spread out; at impact parameters small enough to produce 50 mrad scattering angles at 200 kV, the nucleus is what the electron "sees."

This is Rutherford scattering. The same physics that Ernest Rutherford used in 1911 to establish that atoms have small, dense nuclei by watching alpha particles deflect at large angles from gold foil — the same physics, applied now to electrons. The differential scattering cross-section at high angles scales as $Z^2$: an atom with twice the atomic number scatters electrons at high angles four times more strongly. An atom with four times the atomic number scatters sixteen times more strongly.

This means a HAADF image is a $Z^2$ map. At each pixel, the HAADF signal is proportional to $Z^2$ summed over all atoms the probe passed through in that column. A germanium column ($Z = 32$) produces $32^2/14^2 \approx 5.2$ times the HAADF signal of a silicon column ($Z = 14$). A platinum atom ($Z = 78$) on a carbon substrate ($Z = 6$) produces $78^2/6^2 \approx 169$ times the signal of a carbon atom. A single platinum atom can be seen as a bright dot on a carbon background. Single-atom catalysis, which is about understanding the behavior of individual metal atoms dispersed on a support, became experimentally accessible when HAADF-STEM became routine.

The reason this is qualitatively different from HRTEM is that HAADF contrast is largely free of the phase complications that make HRTEM difficult to interpret. HRTEM intensity depends on focus, specimen thickness, and the specific interference conditions — features can appear bright or dark depending on conditions, and the relationship between image intensity and atomic position requires careful analysis. HAADF intensity is monotonic in $Z$ across a useful range of thicknesses and is relatively insensitive to focus within the normal operating range. A brighter column means heavier atoms; a dimmer column means lighter atoms. This directness is the reason HAADF has become the dominant mode for atomic-resolution structural and compositional analysis in modern materials science.

---

The complementarity between HRTEM and HAADF is not incidental. It is the reason a complete atomic-resolution characterization often uses both.

HRTEM gives structural information: lattice spacings, crystal symmetry, defect positions, strain fields. When the specimen is oriented at a zone axis, HRTEM shows the projected atomic structure with sub-angstrom precision. But HRTEM is chemically blind within a single crystal structure — if two materials have the same or similar structures but different compositions, the HRTEM image shows the structural features without directly revealing what the atoms are.

HAADF gives compositional information: which columns are heavier, which lighter. The Si-Ge interface seen by the student in this chapter's opening scene is a perfect example. HRTEM shows the structure continuing across the interface with a small strain variation — useful, but subtle. HAADF shows the interface as a step change in brightness — silicon dim, germanium bright, boundary obvious. A more extreme case: a multilayer of alternating platinum and carbon would look nearly identical on both sides in HRTEM (both are periodic structures) but would show a contrast ratio of over a hundred in HAADF.

There are also cases where HRTEM sees what HAADF misses. Light atoms — oxygen, carbon, nitrogen — scatter electrons so weakly that their HAADF signal can be lost in the noise, especially on thicker specimens. But light atoms do shift the phases of passing electron waves, which means they can appear in HRTEM phase contrast with adequate signal. Aberration-corrected HRTEM has been used to image oxygen columns in complex oxides and individual carbon atoms in graphene — specimens where HAADF would show almost nothing.

| Specimen / question | HRTEM shows | HAADF shows | Which to use (or why use both) |
|---|---|---|---|
| **Si-Ge interface** | Lattice fringes — strain visible | Z-contrast — composition step visible | **Both** — HRTEM for strain, HAADF for composition gradient |
| **Pt nanoparticles on amorphous carbon support** | Pt particles invisible against amorphous C in phase contrast | Bright dots on dark background (Z⁴ scaling) | **HAADF** — single-atom sensitivity for heavy on light |
| **Oxygen sublattice in a complex oxide (e.g., perovskite)** | Visible in phase contrast under correct conditions | Weak (Z = 8 contrast against heavy cations) | **HRTEM** (or annular-bright-field, ABF) — HAADF underweights low-Z |
| **Unknown crystal phase** | Lattice planes resolved → identify by FFT | Z-contrast yes; structure indirectly | **HRTEM** for structure ID, then HAADF for composition mapping |

---

Running a STEM session requires thinking in terms of dose, because the probe-based architecture concentrates energy in a way that conventional TEM does not.

In conventional TEM, the beam illuminates a region perhaps a micron across. The dose per unit area is spread over that whole region at once. In STEM, the same probe current is focused to 0.1 nm and dwells on each pixel for microseconds to milliseconds. The dose at each pixel, during that dwell, is enormous compared to the average dose across a conventional TEM field of view. Beam-sensitive specimens — polymers, biological materials, any specimen where bond-breaking by inelastic scattering matters — can be damaged faster in STEM than in conventional TEM if care is not taken. The countermeasure is to reduce the probe current and shorten the dwell time, then average many fast scans. The same logic as SEM imaging of beam-sensitive specimens from Chapter 5, applied to transmitted electrons.

There is also a spatial artifact that scanning introduces. Any drift of the specimen stage during a STEM scan appears as a distortion in the image — features stretched along the slow-scan direction, or tilted relative to the true crystal orientation. Fast scanning reduces this but does not eliminate it. Modern instruments apply drift correction between frames by cross-correlating successive fast scans. For atomic-resolution work where a few picometers of distortion matters, this is not optional.

---

Step back now and look at the progression from Chapter 14 to here. Conventional bright-field TEM operates at the scale of nanoparticles, grain boundaries, dislocations — features of tens to hundreds of nanometers. HRTEM operates at the scale of crystal lattice planes — features of tenths of nanometers, meaning fractions of unit cells. HAADF-STEM operates at the scale of individual atomic columns — features below a nanometer — and at the limit, individual atoms. Each step down in scale is a factor of roughly a hundred in spatial resolution, and each step down requires qualitatively different physics.

At the scale of individual atoms, the boundary between "imaging the structure" and "measuring quantum-mechanical wave functions" dissolves. What HRTEM measures is a coherent interference pattern of quantum-mechanical electron waves; what HAADF measures is a set of quantum-mechanical scattering cross-sections. The image in both cases is a statistical accumulation of individual electron detection events. A single electron landing at a pixel in an HAADF image is a quantum measurement — the electron, having scattered at a high angle from a particular atomic nucleus, was detected at a particular location on the annular ring. Repeat that measurement $10^8$ times at each pixel and you have an image.

The atoms in the image are real. The image of those atoms is a carefully constructed statistical aggregate of quantum events, shaped by choices of probe size, detector geometry, accelerating voltage, specimen thickness, and dozens of other parameters. Understanding how those choices shape the image — and what artifacts they introduce — is what separates an operator who can generate images from one who can interpret them.

---

**What would change my mind:** evidence that conventional bright-field and dark-field TEM can routinely match HAADF-STEM Z-contrast for atomic-resolution compositional characterization on a wide class of specimens. The direct comparison between conventional DF and HAADF on the same specimens consistently shows HAADF's advantage in quantitative Z-sensitivity and interpretability. The one domain where this might not hold is very light-element imaging, where phase-contrast HRTEM still outperforms HAADF — but that is a complement to the general statement, not a counterexample.

**Still puzzling:** quantitative HAADF — converting the measured signal at each column into an actual atom count — remains technically demanding. It requires comparison with simulations that account for probe spreading, channeling effects in thick specimens, and detector response function. The field has made substantial progress in recent years using reference standards and statistical methods, but it is not yet routine.

---

## Exercises

### Warm-up

**17.1** In conventional bright-field TEM, the objective aperture passes only the direct beam. In HRTEM, the aperture is removed. Explain in two sentences why removing the aperture produces lattice fringes that were invisible in bright-field. *(Tests: phase contrast mechanism and the role of multi-beam interference.)*

**17.2** Calculate the expected HAADF intensity ratio between a column of pure gold ($Z = 79$) and a column of pure aluminum ($Z = 13$), using the $Z^2$ approximation. *(Tests: $Z^2$ scaling and its numerical application.)*

**17.3** An HRTEM image of a known crystalline specimen shows lattice fringes at one spacing but not at a finer spacing that should also be present. Name two instrument-related reasons why the finer spacing might be missing. *(Tests: information limit concept and the two main contributors to it.)*

### Application

**17.4** A student wants to image (220) lattice fringes of silicon ($d = 0.192$ nm) at 200 kV. Will this be accessible on an uncorrected instrument with an information limit of 0.17 nm? On an aberration-corrected instrument with a limit of 0.08 nm? Justify each answer. *(Tests: information limit applied to a specific d-spacing.)*

**17.5** A STEM session on a beam-sensitive polymer nanoparticle produces a first frame with clear structure, but by the third frame the particle has visibly changed. Describe the physical damage mechanism and specify two acquisition strategy changes that would reduce it, with a one-sentence trade-off for each. *(Tests: dose-damage mechanism in STEM and mitigation strategies.)*

**17.6** A HAADF-STEM image of a Pt/TiO₂ catalyst shows bright dots on the TiO₂ support, some isolated and some clustered. The methods section reports $Z_\text{Pt} = 78$, $Z_\text{Ti} = 22$, $Z_\text{O} = 8$. Calculate the expected HAADF intensity ratio between a single Pt atom and a TiO₂ formula unit (one Ti + two O). What does this ratio imply about the visibility of isolated Pt atoms? *(Tests: $Z^2$ calculation for a multi-atom unit and single-atom detection feasibility.)*

**17.7** You need to image an interface between two cubic perovskite oxides (ABO₃ structures) that have the same crystal structure but different B-site cation compositions: one has $Z_B = 22$ (Ti), the other $Z_B = 40$ (Zr). Would you expect HRTEM or HAADF to more clearly distinguish the two sides of the interface? Justify in two sentences. *(Tests: HRTEM vs. HAADF mode selection based on the specific structural and compositional question.)*

### Synthesis

**17.8** A materials group is studying a heterogeneous catalyst consisting of 3 nm iridium nanoparticles ($Z = 77$) on a cerium oxide support ($Z_\text{Ce} = 58$, $Z_\text{O} = 8$). They need to: (a) confirm the particles are crystalline; (b) identify the exposed crystallographic facets; (c) detect any individually dispersed Ir atoms on the CeO₂ surface; (d) characterize the Ir-CeO₂ interface at atomic resolution. Specify a complete TEM session plan — mode, aperture configuration, and what each acquisition reveals — for all four goals. *(Tests: multi-mode TEM planning integrating BF, HRTEM, HAADF, and zone-axis orientation for a realistic catalyst specimen.)*

**17.9** A published HAADF-STEM image of a GaAs/InAs quantum well heterostructure claims to show "direct atomic-number contrast" at the interface. The methods report 200 kV, HAADF detector inner angle 50 mrad. $Z_\text{Ga} = 31$, $Z_\text{As} = 33$, $Z_\text{In} = 49$. Calculate the expected HAADF intensity ratio between a Ga column and an In column at the interface. Given that ratio, evaluate whether the authors' claim of "direct" Z-contrast is straightforward to interpret, and identify one complication that could make the interface appear sharper or more diffuse than it truly is. *(Tests: $Z^2$ calculation for near-Z pairs, critical reading of HAADF claims, and probe-spreading artifacts.)*

### Challenge

**17.10** Find a published paper that uses both HRTEM and HAADF-STEM on the same specimen. In two paragraphs, explain what structural information the HRTEM image provided that HAADF could not, and what compositional information the HAADF image provided that HRTEM could not. Assess whether the authors used the complementarity deliberately or whether one mode appears to have been the afterthought. *(Tests: critical literature reading, HRTEM/HAADF complementarity, and methods evaluation.)*

