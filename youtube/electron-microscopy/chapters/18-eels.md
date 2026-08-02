# Chapter 18 — Electron Energy Loss Spectroscopy (EELS)


## TL;DR

- EDS tells you which elements are present; EELS tells you what those elements are doing.
- The chapter moves through What the spectrum looks like, Why the fine structure encodes chemistry, Spatial resolution: why STEM-EELS reaches the atomic scale, How EELS relates to EDS, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

*EDS tells you which elements are present; EELS tells you what those elements are doing.*

---

> **Author note:** This chapter is drafted from outline scope and standard textbook material, not from dedicated course lecture notes. All `[verify]` markers throughout are provisional claims that should be confirmed against Egerton's *Electron Energy-Loss Spectroscopy in the Electron Microscope* (Springer, current edition) or equivalent reference before publication. The chapter is structurally complete but numerically provisional.

---

Consider the problem of manganese. You have a thin oxide multilayer — say, a stack of alternating layers, each a few nanometers thick — and you suspect that the manganese changes oxidation state from layer to layer. Mn²⁺ and Mn³⁺ are chemically distinct: different electronic structures, different magnetic properties, different roles in the material's behavior. But both are manganese. Both will appear at exactly the same position in an EDS spectrum, because EDS reads characteristic X-ray energies, which are set by the inner-shell binding energies of the element, not by its oxidation state. The Mn Kα line sits at 5.90 keV whether the manganese carries two positive charges or three.

You cannot distinguish them with EDS. To know the oxidation state, you need to measure something that encodes the electronic environment of the atom — the way the outer electrons are arranged, how they interact with the neighbors, what energy levels are available for transitions. The technique that measures this is electron energy-loss spectroscopy, and its distinctive capability is not just elemental identification but chemical-state identification at near-atomic spatial resolution.

The physical principle is simple to state. When a beam electron passes through a thin specimen and undergoes an inelastic collision, it loses energy. The amount of energy it loses is not arbitrary — it is set by the quantum-mechanical transitions available in the specimen at that location. Measure the energy the beam electron lost, and you have measured those transitions. The spectrum of energy losses is a spectrum of the specimen's electronic structure, sampled one beam electron at a time.

![Schematic EELS spectrum from ~0 to 700 eV](images/18-eels-fig-01.png)
*Figure 18.1 — Schematic EELS spectrum from ~0 to 700 eV*

## What the spectrum looks like

An EELS spectrum runs from zero energy loss up to several keV. Three distinct regions carry distinct information.

The first is the **zero-loss peak**. Most electrons traverse the specimen without losing any significant energy — they scatter elastically, or barely interact. These electrons pile up at zero energy loss, forming a sharp peak whose width is set by the energy spread of the gun (Chapter 3). For a tungsten thermionic gun, the ZLP width is roughly 3 eV `[verify]`. For a Schottky or cold field-emission gun, it is 0.3 eV or below `[verify]`. The ZLP is the reference point: every other feature in the spectrum is measured as an energy loss relative to it.

The second region is the **low-loss region**, from about 5 eV to 50 eV `[verify]`. The dominant feature here is the **plasmon peak** — a broad peak at an energy characteristic of the material, arising from collective oscillations of the valence electrons. Aluminum has a plasmon at about 15 eV `[verify]`; silicon at about 17 eV `[verify]`. The plasmon energy depends on the free-electron density of the material, and it carries information about the dielectric properties of the specimen. The intensity of the plasmon peak relative to the zero-loss peak is also a measure of specimen thickness: a thicker specimen produces more plasmon scattering, and this ratio gives a quantitative thickness estimate `[verify]`.

Surface plasmons appear at lower energies than bulk plasmons, typically around half the bulk value `[verify]`, and are relevant when imaging very thin specimens or nanostructures with high surface-to-volume ratios.

The third region is the **core-loss region**, from about 50 eV to several keV. This is where EELS becomes analytically specific. When the beam electron ionizes an inner-shell electron of an atom in the specimen, it loses an energy approximately equal to the binding energy of that shell. Each element has characteristic core-shell binding energies, and the resulting **core-loss edges** appear at those energies like steps rising above a declining background. The edge onset identifies the element; the shape and fine structure of the edge encode the chemical environment.

Light elements are particularly accessible by EELS. The K-edges of boron, carbon, nitrogen, and oxygen appear at roughly 188, 285, 400, and 530 eV respectively `[verify]`. These energies are well within the practical range of the EELS spectrometer. For comparison, the characteristic X-rays of these elements fall at very low energies where detector quantum efficiency drops and atmospheric absorption is severe — which is why EDS struggles with light elements (Chapter 9). EELS does not have this problem. Carbon in a specimen produces a sharp K-edge at 285 eV `[verify]` that is easy to detect and quantify.

## Why the fine structure encodes chemistry

The edge onset is where the element announces itself. But the shape of the edge in the first 30–50 eV above the onset — the **near-edge fine structure**, abbreviated ELNES — encodes what the element is doing `[verify]`.

Here is the physical reason. When a core electron is ionized, it is promoted into an empty state above the Fermi level. The density of those empty states — the unoccupied electronic structure just above the Fermi energy — is not the same for all chemical environments. Manganese in the 2+ oxidation state has a different unoccupied density of states than manganese in the 3+ oxidation state, because the valence electrons are distributed differently, the bonding geometry differs, and the crystal field splitting differs `[verify]`.

The ELNES shape is therefore a fingerprint of the chemical environment. Transition metal L₂,₃ edges — the edges arising from 2p → 3d transitions in elements like Mn, Fe, Co, Ni — show characteristic **white lines**: sharp peaks at the edge onset that are particularly sensitive to oxidation state and spin state. The ratio of the L₃ to L₂ white-line intensities, and the exact energies of the peaks, shift measurably between oxidation states `[verify]`. This is how the student in the opening scenario reads Mn²⁺ from Mn³⁺: not from the edge onset energy, which differs by only a few eV, but from the white-line shapes and the intensity ratio.

![Overlay of Mn L₂,₃ edge ELNES spectra for](images/18-eels-fig-02.png)
*Figure 18.2 — Overlay of Mn L₂,₃ edge ELNES spectra for*

The same principle applies across the periodic table. Carbon K-edge fine structure distinguishes graphite from diamond from amorphous carbon, because the bonding is fundamentally different in each `[verify]`. Oxygen K-edge fine structure distinguishes different oxide phases. Nitrogen K-edge fine structure reveals whether nitrogen is in a nitride, a nitrate, or an organic compound `[verify]`. The ELNES library — the collection of reference spectra for known compounds — is effectively a chemical fingerprint database that EELS reads against.

## Spatial resolution: why STEM-EELS reaches the atomic scale

In a TEM operated in conventional broad-beam mode, EELS averages over whatever region the beam illuminates. Useful, but not spatially selective below a few nanometers. The capability that changed the field was combining EELS with STEM mode.

In STEM (Chapter 17), the beam is focused to a sub-angstrom probe that is scanned across the specimen. At each scan position, the HAADF detector collects the high-angle scattered electrons to form the structural image. Simultaneously, the EELS spectrometer beneath the specimen collects the transmitted electrons and records a full spectrum. The result is a **spectrum image**: a three-dimensional dataset with two spatial dimensions and one energy dimension, where each pixel contains a complete EELS spectrum.

From the spectrum image, you extract per-pixel elemental maps by integrating the signal under each core-loss edge. You extract per-pixel oxidation-state maps by fitting the white-line ratios. The spatial resolution of these maps is set by the STEM probe diameter — sub-angstrom in modern aberration-corrected instruments — combined with the delocalization of the inelastic scattering event `[verify]`. For core-loss edges at moderate energies (hundreds of eV), the delocalization is small enough that the spatial resolution of chemical maps approaches the inter-atomic spacing.

The consequence is that you can, in principle, map the oxidation state atom-column by atom-column across an interface. In practice, the limiting factors are usually signal-to-noise (core-loss signals are weak, requiring enough beam current and dwell time to accumulate adequate counts), specimen stability under the beam, and background subtraction accuracy `[verify]`. But the capability is real, and papers demonstrating single-atom chemical identification by STEM-EELS appear regularly in the literature.

![Schematic of the STEM-EELS spectrum image data cube](images/18-eels-fig-03.png)
*Figure 18.3 — Schematic of the STEM-EELS spectrum image data cube*

## How EELS relates to EDS

The two techniques measure different things from the same inelastic scattering events. EDS measures the characteristic X-rays emitted when the ionized core vacancy is filled (Chapter 9). EELS measures the energy the beam electron lost when it created that vacancy. Both events happen in femtoseconds; both carry elemental information; both can be collected simultaneously in a modern STEM.

The comparison in practice `[verify]`:

EDS excels at: fast acquisition, reliable major-element quantification, no strict thin-specimen requirement for qualitative ID, and elements of Z > 11 where fluorescence yields are reasonable. EDS struggles with: light elements (low fluorescence yield, soft X-ray absorption), chemical-state discrimination (the X-ray energy shifts by only fractions of an eV between oxidation states), and spatial resolution in SEM (limited by the interaction volume).

EELS excels at: light elements (B, C, N, O are all accessible), chemical-state information from ELNES, high spatial resolution in STEM mode (sub-nanometer to sub-angstrom), and thickness measurement from the plasmon peak ratio. EELS struggles with: heavy elements whose core-loss edges fall above ~2 keV are difficult to measure `[verify]`; the spectrum sits on a steeply declining background that must be subtracted accurately; thin specimens are required; and the data volume from spectrum imaging is large.

The detection limit comparison is approximate: EDS at roughly 0.1 wt% for major elements under typical conditions; EELS potentially an order of magnitude lower for favorable edges on thin specimens `[verify]`. Neither number is unconditional — both depend on the element, the matrix, the acquisition parameters, and what you define as "detected."

The working rule most practitioners use: if you need light elements or chemical-state information, EELS; if you need fast, reliable major-element quantification or a compositional survey, EDS. For a complete characterization, collect both simultaneously.

## The artifacts that haunt every EELS spectrum

The core-loss signal is weak — orders of magnitude weaker than the zero-loss peak — and it sits on a steeply declining background from other inelastic processes. Reading it accurately requires confronting several systematic errors.

**Multiple scattering** is the most fundamental. Every time the beam electron undergoes a plasmon excattering event, it loses another 15–30 eV `[verify]`. If the specimen is thick enough, the beam electron can lose energy from a plasmon event *and* a core-loss event, and the recorded core-loss edge appears shifted to higher energy loss by the plasmon energy. In a thick specimen, each core-loss edge develops a satellite at the edge energy plus the plasmon energy, which can be misidentified as a different element `[verify]`. Recognition: the low-loss spectrum shows a strong second-plasmon peak relative to the first; the specimen is too thick. Fix: thinner specimen or mathematical deconvolution of the plural-scattering contribution using the low-loss spectrum as a reference `[verify]`.

![EELS spectra from the same specimen at two](images/18-eels-fig-04.png)
*Figure 18.4 — EELS spectra from the same specimen at two*

**Background subtraction error** is the most common quantitative problem. The background under a core-loss edge is typically modeled as a power law $AE^{-r}$ fitted in a window before the edge onset, then extrapolated under the edge to subtract. If the pre-edge window is short, or if another edge overlaps the pre-edge region, the fitted power law is wrong, and the integrated edge signal is wrong `[verify]`. The result can be concentrations that are off by factors of two or more. The fix is a clean pre-edge window of adequate length and careful inspection of the background fit.

**Channeling artifacts** appear in STEM-EELS on crystalline specimens aligned along low-index zone axes. At certain orientations, the focused probe channels along atom columns with enhanced intensity, and the EELS signal becomes orientation-dependent rather than purely compositional `[verify]`. This makes quantitative comparison between differently-oriented regions unreliable. Recognition: HAADF image shows strong channeling contrast. Fix: image slightly off-axis or use simulations to account for the channeling effect.

**Beam damage during acquisition** is the practical constraint that limits spatial resolution in practice for many specimens. Getting adequate signal from a weak core-loss edge requires either high beam current, long dwell time, or both. Both damage beam-sensitive specimens. The manganese oxide layers in the opening scenario may survive a second of dwell time at atomic-column resolution. An organic polymer specimen may not survive a millisecond `[verify]`. Low-dose protocols — shorter dwell, faster scanning, signal averaging from multiple passes — mitigate but do not eliminate the tradeoff between signal and damage.

## Where EELS fits in the TEM session

A modern aberration-corrected STEM with a fast direct-detection EELS spectrometer can collect HAADF images, EDS maps, and EELS spectrum images simultaneously on the same scan. The three datasets are spatially registered to each other because they are collected in the same scan pass.

The workflow in practice: acquire an HAADF overview image to identify the region of interest and verify specimen quality. Run a quick EDS map for elemental overview — fast, low dose, identifies which elements are present and roughly where. Then run the STEM-EELS spectrum image on the specific region where chemical-state or light-element information is needed — slower, higher dose, richer information.

The HAADF image tells you the structure. The EDS map tells you the composition. The EELS spectrum image tells you the bonding. Together they give a complete nanoscale chemical and structural description of the specimen.

The limitation to carry honestly: spectrum imaging produces large datasets that require careful analysis. The energy axis must be calibrated against known edges or the ZLP position. The background subtraction under each edge is a modeling step with real uncertainty. The ELNES comparison to reference spectra is only as good as the reference library. And the results are only as representative as the few square nanometers that were imaged, which may or may not be typical of the bulk specimen.

EELS is the most information-dense technique in the TEM toolkit. It is also the most demanding — of specimen quality, of acquisition care, and of analysis rigor. The student who can collect and interpret a STEM-EELS spectrum image reliably is operating at the frontier of what materials characterization can do.

---

## Exercises

### Warm-up

**18.1** An EELS spectrum shows three labeled regions. Match each region to its physical origin: (a) zero-loss peak, (b) plasmon peak, (c) carbon K-edge at ~285 eV `[verify]`. Physical origins: electrons that traversed the specimen without energy loss; collective oscillation of valence electrons; inner-shell ionization of a specific element. *(Tests: basic spectrum anatomy)*

**18.2** A Schottky FE-gun TEM has a zero-loss peak width of ~0.3 eV `[verify]`. A tungsten thermionic TEM has a ZLP width of ~3 eV `[verify]`. Which instrument can better resolve closely spaced ELNES fine-structure features, and why? Connect your answer to Chapter 3's discussion of gun energy spread. *(Tests: ZLP width → energy resolution → ELNES interpretability)*

**18.3** In one sentence each, state one question that EDS answers better than EELS and one question that EELS answers better than EDS. *(Tests: complementarity of the two techniques)*

### Application

**18.4** You acquire an EELS spectrum on a carbon-nitrogen compound and see two edges: one at ~285 eV and one at ~400 eV `[verify]`. Identify the elements responsible for each edge. If you then acquire the spectrum on a pure carbon standard and see only one edge, which edge is absent and why? *(Tests: core-loss edge identification by energy and elemental assignment)*

**18.5** A STEM-EELS spectrum image of an iron oxide film shows an Fe L₂,₃ edge. You notice that in the low-loss region the second-plasmon peak is nearly as intense as the first-plasmon peak. Before interpreting the Fe oxidation state from the L₂,₃ white lines, what artifact should you address, and what is the fix? `[verify]` *(Tests: multiple-scattering recognition and remediation)*

**18.6** You are trying to quantify the nitrogen content in a titanium nitride film by integrating the N K-edge. Your pre-edge background window is only 5 eV wide because the Ti M-edge overlaps the region just below the N K-edge onset. Explain why this short background window is a problem and what quantitative error it is likely to introduce. *(Tests: background subtraction logic and its failure modes)*

**18.7** A colleague says their STEM-EELS oxygen map shows higher oxygen signal near grain boundaries than inside grains, and concludes that oxygen is segregating to the boundaries. Name one artifact from this chapter that could produce the same apparent result without any real oxygen segregation, and explain the physical mechanism. `[verify]` *(Tests: channeling artifact awareness in STEM-EELS)*

### Synthesis

**18.8** A materials chemist has a 5 nm thin film of lithium cobalt oxide (LiCoO₂) on a carbon support and wants to determine: (a) whether lithium is present (EDS cannot detect Li — explain why using Chapter 9), (b) the Co oxidation state, and (c) the oxygen coordination environment. Design an EELS acquisition strategy for each goal: state which spectral region or edge you would use, whether you would use broad-beam TEM-EELS or STEM-EELS, and one artifact to watch for in each measurement. `[verify where appropriate]` *(Tests: integrating spectrum anatomy, ELNES, STEM vs. TEM mode, and artifact awareness for a realistic multi-question analysis problem)*

**18.9** A nanotechnology lab reports that STEM-EELS spectrum imaging of their 2 nm quantum dots shows chemical maps at "0.2 nm spatial resolution." A reviewer is skeptical. Using the concepts in this chapter — probe diameter, inelastic delocalization, signal-to-noise, and beam damage — construct the argument the reviewer might make about why 0.2 nm EELS resolution is harder to achieve in practice than the probe size alone would suggest. `[verify]` *(Tests: critical reading of EELS resolution claims by connecting probe size, delocalization, SNR, and damage as compounding constraints)*

### Challenge

**18.10** Lithium has $Z = 3$ and a K-edge at approximately 55 eV. From what you know about the EELS spectrum structure — particularly the low-loss region with plasmon peaks — explain why the Li K-edge is difficult to detect even though it falls within the spectrometer's energy range. Then propose two experimental strategies (one involving the specimen, one involving acquisition parameters) that would improve Li detection. `[verify: Li K-edge energy and practical detectability]` *(Tests: applying the spectrum structure — overlap between the core-loss edge of a very light element and the plasmon/low-loss region — plus experimental problem-solving not directly stated in the chapter)*

---

*What would change my mind:* improvements in direct-detection EELS spectrometer efficiency and monochromated gun energy spread that push the routine energy resolution below 10 meV. This would open vibrational spectroscopy at atomic resolution — phonon modes, hydrogen bonds, molecular vibrations — from the same EELS spectrometer already used for core-loss work. Early demonstrations exist `[verify]`; whether it becomes routine instrumentation will determine whether this chapter needs a vibrational-EELS section in future editions.

*Still puzzling:* the transition from EELS data collection to reliable quantification remains harder than it should be, given how mature the technique is. Background subtraction, plural-scattering deconvolution, and ELNES fitting each introduce uncertainty that compounds. The error bars on EELS quantification are often underreported in published work. The community would benefit from more systematic reporting of fitting uncertainty alongside elemental concentrations `[verify]`.
