# Chapter 9 — Energy Dispersive X-ray Spectroscopy (EDS)


## TL;DR

- Every element in the periodic table emits X-rays at its own unique energies when you knock out an inner-shell electron — and the SEM can read those energies one photon at a time.
- The chapter moves through Why the photons have specific energies, The overvoltage rule, How the detector reads the photons, The artifacts, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

*Every element in the periodic table emits X-rays at its own unique energies when you knock out an inner-shell electron — and the SEM can read those energies one photon at a time.*

---

A geologist comes back from a hike with a pebble that catches the light in three colors: green-black, yellow-tan, rust-red. The optical microscope cannot name those colors. XRD would help but requires grinding the sample to powder. The fastest answer is in the next room.

She mounts a fresh-broken face on a stub, pumps down, sets the kV to 25, and parks the beam on the green-black region for thirty seconds. A spectrum builds on the screen, peaks appearing at specific energies: copper at 8.05 keV, sulfur at 2.31 keV, iron at 6.40 keV. The green-black phase is chalcopyrite, copper iron sulfide. She moves the beam to the yellow-tan region: silicon dominates, aluminum second, potassium third — a clay mineral. The rust-red region: iron and oxygen, with traces of sulfur — an iron oxide weathering crust. Three minutes, three phases identified, no chemistry, no grinding.

That is the EDS experiment. The beam ionizes inner-shell electrons in the atoms of the specimen; the atoms relax by emitting X-ray photons at energies that are fingerprints of the emitting element; a detector sitting a few centimeters away counts those photons and bins them by energy. The result is a histogram — the spectrum — with peaks at energies that name the elements, and peak heights that, with the right corrections, tell you the proportions.

The wonder is that this works at all. The inner-shell binding energies of every element in the periodic table are quantum-mechanically determined by nuclear charge and electron screening, and they are as distinct as signatures. Carbon's K-shell sits at 0.28 keV; iron's K-shell at 7.11 keV; gold's L-shell at about 11.9 keV. No two elements share the same fingerprint. Read the photon energies, name the atoms.

![Three EDS spot analyses on a single pebble — chalcopyrite (Cu, S, Fe), clay (Si, Al, K), and iron oxide (O, Fe). Inner-shell binding energies are signatures.](../images/09-energy-dispersive-spectroscopy-fig-01.png)

*Figure 1.* Three EDS spot analyses on a single pebble — chalcopyrite (Cu, S, Fe), clay (Si, Al, K), and iron oxide (O, Fe). Inner-shell binding energies are signatures.

## Why the photons have specific energies

To understand why the fingerprint exists, you need the atomic physics, and it is worth going through it once properly.

Bound electrons in an atom do not sit at arbitrary energies. They occupy shells — labeled K, L, M, N from the nucleus outward — each with a sharply defined binding energy set by the balance of Coulomb attraction to the nucleus and screening from all the other electrons. The K shell (the 1s electrons, two of them) sits deepest, most tightly bound. The L shell (the 2s and 2p electrons) sits higher. The M shell higher still.

When a beam electron arrives at the specimen with enough kinetic energy, it can knock a bound inner-shell electron completely out of the atom, leaving a **vacancy** in the shell. The minimum energy needed to do this is the **critical ionization energy** $E_c$ — also called the binding energy or the edge energy — for that specific shell of that specific element. For the K shell of copper, $E_c = 8.98$ keV. For the K shell of carbon, $E_c = 0.28$ keV. The beam electron must arrive with at least $E_c$ or the shell stays full and nothing happens.

Once the vacancy exists, the atom is in an excited state, and it relaxes within femtoseconds. An electron from an outer shell drops down to fill the hole, and the energy difference between the two shells is released. That energy release takes one of two forms.

The first is **characteristic X-ray emission**: the energy difference is emitted as a single photon. The photon's energy is exactly the energy difference between the two shells:

$$E_{\text{photon}} = E_{\text{upper shell}} - E_{\text{lower shell}}.$$

For copper, when an L-shell electron fills a K-shell vacancy, the photon energy is approximately $8.98 - 0.93 = 8.05$ keV. That is the Cu Kα line. The energy is specific to the element because the shell energies are specific to the element — set by the nuclear charge, which is the atomic number. There is no way to fake a Cu Kα line with a different element, because no other element has a nucleus with 29 protons and the same shell structure.

The second form of relaxation is the **Auger process**: instead of emitting a photon, the atom ejects a third electron — an Auger electron — with kinetic energy equal to the same energy difference. This is a competing channel. Every K-shell ionization leads either to a characteristic X-ray or to an Auger electron, never both.

The fraction that leads to X-rays is the **fluorescence yield** $\omega$. For light elements, almost nothing comes out as X-rays. For carbon ($Z = 6$), the K-shell fluorescence yield is about 0.5% — for every 200 K-shell ionizations in carbon, one X-ray. The other 199 become Auger electrons that are immediately reabsorbed in the solid. For copper ($Z = 29$), the K-shell fluorescence yield is about 45%. For gold ($Z = 79$), close to 100%. The fluorescence yield rises steeply with atomic number, which is why EDS struggles with light elements — not because they don't ionize, but because their ionizations produce almost no photons.

![Fluorescence yield ωK vs atomic number Z from](images/09-energy-dispersive-spectroscopy-fig-01.png)
*Figure 9.1 — Fluorescence yield ωK vs atomic number Z from*

The naming convention for X-ray lines encodes the transition. The K family of lines all result from filling a K-shell vacancy. The Kα lines come from L-shell electrons falling into the K vacancy; the Kβ lines from M-shell electrons. The Kα line is more intense than Kβ because L→K transitions are more probable than M→K transitions. Similarly, L-family lines result from L-shell vacancies filled by M-shell electrons. For high-Z elements that are analyzed using L or M lines rather than K lines, the same logic applies.

## The overvoltage rule

The beam electron must arrive with energy above $E_c$ to ionize the shell. But how much above?

The ionization cross-section — how likely the collision is — rises sharply above the threshold, peaks at about twice the threshold, and slowly decreases at higher overvoltage. The practical rule is to run at an **overvoltage** $U_0 = E_0 / E_c \geq 2$. Below that, ionization efficiency is poor and X-ray yield is low. The rule of two: beam energy at least twice the critical ionization energy of the heaviest line you want to see.

For a specimen containing aluminum and copper, the rule applies to each element separately. Aluminum's K-shell needs $E_c = 1.56$ keV, so $U_0 = 2$ requires at least 3.1 keV of beam energy. Copper's K-shell needs $E_c = 8.98$ keV, so $U_0 = 2$ requires at least 18 keV. Copper is the binding constraint: run at 20 keV, and aluminum's overvoltage is about 13 — far above the threshold, meaning aluminum X-ray yield is efficient. The light elements almost always have comfortable overvoltage once you've met the heavy-element requirement. The standard practice for alloy surveys is 15–25 kV, which covers most K and L lines of practical interest.

The other side of the kV choice is the interaction volume. Chapter 6 showed that the Kanaya–Okayama range scales as $E_0^{1.67}$: at 20 kV in copper, the interaction volume is about 1.4 μm across. X-rays come from that entire volume. The spatial resolution of an EDS measurement is not the probe diameter — it is the interaction volume diameter. A 1 nm probe at 20 kV still produces an EDS signal from a micrometer-scale region. If you need to analyze a 50 nm particle, you need low kV, and you may have to sacrifice K-line sensitivity on heavy elements. The kV choice is always this trade: higher kV for heavy-element sensitivity, lower kV for spatial resolution and surface sensitivity.

## How the detector reads the photons

The EDS detector is a slab of silicon — in modern instruments, a **silicon drift detector** (SDD), thermoelectrically cooled to around −20 °C. When an X-ray photon enters the silicon, it deposits its energy through photoelectric absorption, producing electron-hole pairs at a rate of about 3.6 eV per pair. A 5 keV photon creates roughly 1,400 pairs. Electronics collect that charge, amplify it, and produce a voltage pulse proportional to the charge. That pulse height is digitized and assigned to an energy bin. Repeat for millions of photons and you have the spectrum.

The detector is, operationally, a photon counter that turns energy into a bin address. Its great virtue is that it does this for every photon simultaneously, across the entire energy range from near zero to the beam energy. You get the full spectrum in one acquisition.

![Schematic cross-section of an SDD showing an incoming](images/09-energy-dispersive-spectroscopy-fig-02.png)
*Figure 9.2 — Schematic cross-section of an SDD showing an incoming*

The cost of this breadth is **energy resolution**. The number of electron-hole pairs per photon fluctuates statistically; a 5.9 keV photon that on average creates 1,640 pairs sometimes creates 1,610, sometimes 1,670. This statistical scatter in charge collection translates directly to an uncertainty in the measured energy. The result is that a line with an intrinsic width of a few electron volts appears in the EDS spectrum as a peak with a full width at half maximum (FWHM) of about 125–150 eV for a modern SDD. That is about 70 times broader than the natural linewidth. Two peaks closer together than about 100 eV are difficult to resolve.

The spectrum has two components: the **characteristic peaks** at element-specific energies, and a smooth **continuum background** running from zero up to the beam energy. The continuum is bremsstrahlung — braking radiation — emitted when beam electrons decelerate in the Coulomb field of specimen nuclei. Because deceleration events can lose any amount of energy from a few eV up to the full beam energy, the bremsstrahlung spectrum is continuous. Identifying characteristic peaks means finding them above this sloping, noisy background. The analysis software fits and subtracts the background; the operator's job is to make sure the characteristic peaks are high enough above the background to count reliably.

## The artifacts

Every real EDS spectrum contains artifacts, and recognizing them is what separates publishable analysis from wasted time.

**Peak broadening** is unavoidable. The 125–150 eV FWHM means that two elements whose lines happen to fall within that window are difficult to distinguish. The periodic table is dense with near-coincidences: manganese Kα at 5.90 keV and chromium Kβ at 5.95 keV differ by 50 eV — well below detector resolution, appearing as one peak. Oxygen Kα at 0.523 keV and vanadium Lα at 0.511 keV differ by 12 eV. If your specimen might contain both elements, you need additional evidence — perhaps another line from each element — to separate them. Analysis software does peak deconvolution, but the operator must verify the result.

![EDS spectrum segment showing the Mn Kα /](images/09-energy-dispersive-spectroscopy-fig-03.png)
*Figure 9.3 — EDS spectrum segment showing the Mn Kα /*

**Escape peaks** appear when an X-ray photon is absorbed in the silicon detector and the resulting Si Kα photon (1.74 keV) escapes the detector before being absorbed. The recorded energy for that event is the parent photon energy minus 1.74 keV. If you have a strong peak at 8.05 keV (Cu Kα), expect a small artifact peak at 6.31 keV. Recognition: a small peak at exactly $E_{\text{parent}} - 1.74$ keV. Modern analysis software flags and corrects escape peaks automatically, but the operator should confirm the assignment.

**Sum peaks** arise when two photons arrive at the detector so close in time that the electronics register them as one event at the sum of their energies. A strong peak at 5.9 keV produces a sum artifact at 11.8 keV. Sum peaks are most problematic at high count rates. The mitigation is to reduce the count rate — lower beam current, pull the detector back — until the dead time is in the 20–30% range. Above 50% dead time, sum peaks are a serious problem and quantification becomes unreliable.

**The dead time** itself is worth understanding. The detector cannot process events faster than its electronics can clear. While it is processing one photon, subsequent arriving photons are lost. The fraction of time the detector is busy is the dead time:

$$\text{Dead time} = \left(1 - \frac{\text{output count rate}}{\text{input count rate}}\right) \times 100\%.$$

At 25% dead time, one photon in four is lost — the spectrum takes longer to collect, but the photons that are counted are correctly processed. The spectrum is accurate; you just need more time. At 60% dead time, many photons pile up on each other, and the spectrum is distorted by coincidence events. The 20–30% dead time range is where efficiency and accuracy balance.

**Silicon internal fluorescence** is a small artifact unique to silicon-based detectors: X-rays absorbed inside the detector can produce secondary silicon Kα photons within the detector itself, which register as a small silicon peak even when the specimen contains no silicon. This is corrected automatically in modern analysis software. But if you see an anomalously large silicon peak on a specimen that should have none, check whether it is detector artifact or real silicon — the peak shape and the detector-correction log will usually tell you.

## What the spectrum can and cannot tell you

Once the spectrum is collected and artifacts identified, what can you learn?

**Qualitative identification** is fast and reliable for elements above about 0.5 wt%. A 30-second spectrum identifies the major elements present. The software assigns peaks to elements using the known line energies; the operator confirms by checking that the full family of lines for each assigned element is present. A copper identification should show Cu Kα, Cu Kβ, and at 20 kV also Cu Lα. If only one line is present, be skeptical.

**Semi-quantitative analysis** converts peak intensities into weight percentages using calculated matrix corrections. The standard approach is called ZAF or PhiRhoZ correction — accounting for the atomic-number effect on ionization cross-section (Z), absorption of X-rays as they travel out through the specimen (A), and secondary fluorescence of one element by X-rays from another (F). For major elements in a flat polished specimen, standardless ZAF gives accuracy of about ±5% relative — good enough to distinguish a 30 wt% copper phase from a 20 wt% copper phase, not good enough to measure 0.8 wt% manganese in steel. For trace work below 1 wt%, standards-based calibration is required.

**Detection limits** are a counting-statistics problem. A peak is detectable when it rises above three standard deviations of the background noise. For Poisson-distributed counts, the noise on the background is $\sqrt{N_{\text{bg}}}$, so you need the peak counts $P > 3\sqrt{N_{\text{bg}}}$. Under typical conditions — a 60-second acquisition on a polished metal at moderate beam current — the practical detection limit is around 0.1 wt% (1000 ppm) for elements with good fluorescence yield and no severe peak overlaps. For light elements with low fluorescence yield, or for elements whose lines overlap heavily with matrix peaks, the limit is worse. Doubling the counting time improves the detection limit by roughly $\sqrt{2}$; to improve by a factor of ten, you need to count a hundred times as long.

**Spatial resolution** is set by the X-ray-generating volume, which is approximately the Kanaya–Okayama interaction volume from Chapter 6. At 20 kV in copper, that volume is about 1.4 μm across. An EDS map at 20 kV cannot resolve compositional features below about 1 μm, regardless of how small the probe is. If you need sub-micrometer EDS resolution, you must lower kV — accepting reduced sensitivity to heavy-element K lines — or move to TEM-based EDS, where the thin specimen limits the lateral spreading of the beam.

![Comparison showing a 1 nm SE probe and](images/09-energy-dispersive-spectroscopy-fig-04.png)
*Figure 9.4 — Comparison showing a 1 nm SE probe and*

**Mapping** is EDS at every pixel. Modern SDDs handle full spectrum storage at each point in a raster scan, building a three-dimensional dataset: two spatial dimensions plus the energy axis. From that dataset you extract per-element maps showing where each element is spatially located. A map collection on a polished alloy cross-section takes 5–15 minutes at moderate magnification and yields simultaneous elemental distributions for all elements in the specimen. The spatial resolution of each map is still set by the interaction volume, not the pixel size.

## The chain of events, end to end

It is worth walking through the full chain once, from atom to number, to see where each piece of physics sits.

A 20 keV electron arrives at the specimen surface. It enters the solid and begins scattering. Somewhere in the interaction volume — maybe 300 nm below the surface, maybe 800 nm — it undergoes an inelastic collision with a copper atom and ejects a K-shell electron. The copper atom, now missing a K-shell electron, relaxes: an L-shell electron drops into the K vacancy, emitting a photon at 8.05 keV. That photon travels in a random direction. Some fraction of photons are absorbed in the specimen before they escape — the absorption correction A accounts for this. Some photons that do escape miss the detector, which subtends a small solid angle. The photons that reach the detector each create a charge pulse; the electronics measure the charge and assign an energy. After 60 seconds, the histogram of energies is the spectrum.

Reading the spectrum backward: the peak at 8.05 keV says copper is present. Its height, after ZAF correction, says how much. The absence of a peak at 8.98 keV (the Cu K absorption edge is above beam energy for a 5 kV experiment) would say the K line wasn't excited. The peak at 2.31 keV says sulfur. The peak at 6.40 keV says iron. Three elements, one interaction volume, one detector, thirty seconds.

The geologist's pebble is chalcopyrite. The spectrum told her.

---

## Exercises

### Warm-up

**9.1** In one sentence, explain why the Cu Kα photon always appears at 8.05 keV regardless of which beam electron caused the ionization. Your answer should invoke the concept of atomic energy levels, not detector properties. *(Tests: the origin of characteristic X-ray energies)*

**9.2** The Au L₃ critical ionization energy is 11.92 keV. What is the minimum beam energy that satisfies the overvoltage rule for analyzing gold using its L line? If your SEM maximum is 30 kV, is the Au K line ($E_c \approx 80.7$ keV) accessible? *(Tests: overvoltage rule and its practical limits)*

**9.3** You collect a spectrum from a copper specimen and see a small unexplained peak at 6.31 keV. The instrument software does not assign it to any element. Identify the artifact and explain its physical origin in one sentence. *(Tests: escape peak recognition)*

### Application

**9.4** You need to analyze a specimen that may contain iron ($E_{c,K} = 7.11$ keV), chromium ($E_{c,K} = 5.99$ keV), and nickel ($E_{c,K} = 8.33$ keV). Using the overvoltage rule, calculate the minimum beam energy to cover all three K lines efficiently. Then calculate the Kanaya–Okayama range at that energy in iron ($A = 55.85$, $\rho = 7.87$ g/cm³, $Z = 26$) and state what that tells you about the EDS spatial resolution. *(Tests: overvoltage calculation combined with Chapter 6 interaction-volume scaling)*

**9.5** A spectrum collected at 30% dead time shows a peak at 11.8 keV that the software does not assign to any element. The strongest peak in the spectrum is Fe Kα at 6.40 keV. Identify the artifact, explain its cause, and state one operational change that would reduce it. *(Tests: sum peak recognition and dead-time management)*

**9.6** A researcher collects a 60-second EDS spectrum on a stainless steel specimen and reports "no manganese detected." The published composition of the alloy is 1.5 wt% Mn. Propose two possible explanations for why Mn is absent from the spectrum — one involving acquisition parameters and one involving detector artifacts. *(Tests: detection limits, overvoltage, and peak overlap as competing failure modes)*

**9.7** You are mapping a polished cross-section of a TiN coating (200 nm thick) on a steel substrate. At 20 kV, the EDS map shows strong Fe signal everywhere, including inside the coating region. At 5 kV, the Fe signal disappears in the coating region. Explain the discrepancy using the interaction volume concept. What is the trade-off you accept by dropping to 5 kV? *(Tests: kV-dependent spatial resolution in EDS mapping)*

### Synthesis

**9.8** A pharmaceutical lab has tablets containing an active ingredient suspected to have a zinc-based impurity at approximately 0.05 wt%. The matrix is mostly carbon, hydrogen, oxygen, and nitrogen. Design an EDS acquisition strategy: specify kV, the line family you would use for Zn, expected counting time, and one artifact you would watch for. Explain in one sentence each why the low-Z matrix complicates the analysis and why the fluorescence yield matters for the impurity. *(Tests: integrating overvoltage, fluorescence yield, detection limits, and artifact awareness for a realistic low-Z matrix / trace-element problem)*

**9.9** A colleague reports that two phases in a polished alloy are "indistinguishable by EDS." Phase A is Fe₀.₅₅Cr₀.₄₅ and Phase B is Fe₀.₄₅Cr₀.₅₅. The EDS spectra show Fe Kα and Cr Kα peaks for both phases. Explain why quantitative distinction is difficult at the 10 wt% level, and propose what combination of acquisition conditions and analysis approach would give the most reliable result. *(Tests: quantification accuracy, standardless vs. standards-based ZAF, and the limits of semi-quantitative EDS)*

### Challenge

**9.10** You are characterizing a battery electrode cross-section containing lithium iron phosphate (LiFePO₄). Lithium has $Z = 3$ and $E_{c,K} = 0.054$ keV; its Kα line is at 0.054 keV. Explain why lithium is essentially undetectable by EDS, using at least two distinct physical reasons from this chapter. Then propose an alternative analytical technique (you may look this up) that could identify lithium in the same specimen, and state what SEM-based technique you would use alongside it to provide spatial context. *(Tests: combining fluorescence yield, detector physics, and peak-background limitations into a complete argument about why EDS has elemental floors — and thinking beyond the chapter)*

---

*What would change my mind:* evidence that standardless EDS quantification can routinely achieve ±2% relative accuracy on trace elements below 1 wt% without standards-based calibration. This is not what current technology delivers. For major-element surveys, standardless ZAF is adequate; for trace work, it is not.

*Still puzzling:* the practical decision of when to move from EDS to wavelength-dispersive spectrometry (WDS) is rarely formalized in laboratory practice. WDS gives 5–20 eV resolution and would resolve many of the peak-overlap problems that force complex deconvolution in EDS, but most labs default to EDS even when WDS would give cleaner data. The economics — EDS is faster, simpler, and already on the SEM — dominate over the physics.
