# Chapter 13 — Structure Determination: Nuclear Magnetic Resonance Spectroscopy

*NMR is the structural microscope of organic chemistry. It tells you how many distinguishable carbons and hydrogens are in a molecule, and what each one is attached to. Most published structures of new organic compounds are essentially NMR-determined.*

In 1946 Felix Bloch at Stanford and Edward Purcell at Harvard independently discovered that atomic nuclei in a magnetic field absorb radiofrequency energy at very specific frequencies — frequencies that depend not just on the nucleus type but on its chemical environment. They shared the 1952 Nobel Prize for the discovery. Within twenty years, NMR spectroscopy had become the most powerful technique in the structure-determination toolkit. The MRI scanner in a hospital is a direct industrial descendant: same physics, same detection of nuclear-spin transitions, applied to the protons of water in the body instead of the protons of a synthetic compound in a tube.

This chapter is about how NMR works, how to read a spectrum, and how to use NMR (alongside mass spectrometry and infrared spectroscopy from Chapter 12) to determine the structure of an unknown compound. The chemistry is essentially unchanged since the 1950s; the instrumentation has improved by many orders of magnitude.

## What NMR sees

Atomic nuclei have a property called *spin*. Some nuclei have nonzero spin, others don't. The rule of thumb: nuclei with odd numbers of protons or odd numbers of neutrons have spin; nuclei with even numbers of both don't.

The two most important NMR-active nuclei in organic chemistry:

- **¹H** (protium, the most common isotope of hydrogen): spin = ½, abundance ~100%.
- **¹³C** (carbon-13): spin = ½, natural abundance about 1.1% (the rest is ¹²C, which has zero spin and is invisible to NMR).

Other useful nuclei: ¹⁹F, ³¹P, ²H (deuterium, used as a label), ¹⁵N. The most abundant carbon isotope (¹²C) and the most abundant oxygen isotope (¹⁶O) both have zero spin and are invisible.

When you put a sample in a strong magnetic field, the spins of NMR-active nuclei align either *with* the external field (lower energy) or *against* it (higher energy). The energy gap between the two states is small but real. If you irradiate the sample with a radiofrequency electromagnetic wave whose photon energy exactly matches the gap, some nuclei in the lower state absorb a photon and "spin-flip" to the higher state. The instrument detects this absorption.

The frequency at which a particular nucleus absorbs depends on:

1. The strength of the external magnetic field.
2. The kind of nucleus (¹H absorbs at a different frequency from ¹³C, at the same field strength).
3. *The chemical environment of the nucleus.*

Point 3 is what makes NMR a structural tool. Two protons in the same molecule, in different chemical environments, absorb at slightly different frequencies. The pattern of absorption frequencies is a map of the molecule's chemical environments.

## Chemical shift

The frequency at which a particular nucleus absorbs is conventionally measured relative to a reference compound — usually tetramethylsilane (TMS, (CH₃)₄Si) — and reported as a *chemical shift* in parts per million (ppm), denoted δ:

$$\delta = \frac{\nu_{\text{sample}} - \nu_{\text{TMS}}}{\nu_{\text{instrument}}} \times 10^6$$

The reason ppm is used (instead of absolute frequencies) is that ppm values don't change when you change the instrument. A proton at δ 2.0 on a 60 MHz instrument is at δ 2.0 on a 600 MHz instrument too, even though the absolute frequency in Hz differs by a factor of 10.

For ¹H NMR, chemical shifts run from about 0 to 12 ppm. For ¹³C NMR, they run from about 0 to 220 ppm.

What controls the chemical shift? Mostly *electron density*. Nuclei surrounded by more electron density are *shielded* — the electrons partially cancel the external magnetic field at the nucleus, so the nucleus needs a slightly stronger applied field (or equivalently, slightly higher frequency) to come into resonance. Shielded nuclei have *lower chemical shifts* (further to the right in a spectrum, conventionally).

Nuclei with less electron density — for instance, hydrogens bonded to electronegative atoms or carbons attached to electron-withdrawing groups — are *deshielded*, and they appear at *higher chemical shifts* (further to the left).

Some characteristic ¹H chemical shift ranges:

| Hydrogen environment | δ (ppm) |
|---|---|
| Si–CH₃ (TMS) | 0 |
| –CH₃ (alkane) | 0.7–1.3 |
| –CH₂– (alkane) | 1.2–1.5 |
| –CH (alkane) | 1.4–1.7 |
| –CH₂ adjacent to heteroatom | 2.0–4.5 |
| C=C–H (alkene) | 5.0–6.5 |
| Ar–H (aromatic) | 7–8 |
| O–CH₃ (methyl ether) | 3.3–3.9 |
| O–H (alcohol) | 0.5–5 (variable, broad) |
| C–CHO (aldehyde) | 9.5–10 |
| –COOH | 10–12 |

For ¹³C:

| Carbon environment | δ (ppm) |
|---|---|
| –CH₃ (alkane) | 0–35 |
| –CH₂– (alkane) | 15–55 |
| –CH< (alkane) | 25–55 |
| –C–O–C– (ether) | 50–70 |
| C=C (alkene) | 100–150 |
| Ar–C (aromatic) | 110–160 |
| C≡N (nitrile) | 110–125 |
| C=O (carbonyl) | 160–220 (specific by type) |

The position of a peak tells you what environment the nucleus is in. Aromatic protons at δ 7–8 mean a benzene ring. A peak at δ 9.7 means an aldehyde proton. Carbons at δ 200 mean a ketone.

## Counting peaks: equivalent nuclei

Two nuclei in the same molecule give the same NMR signal if and only if they're *chemically equivalent* — i.e., interchangeable by symmetry.

In ethanol, CH₃CH₂OH, the three hydrogens of the methyl group are equivalent (they're related by rotational symmetry around the C–C bond axis), so they give one peak. The two hydrogens of the CH₂ group are equivalent for the same reason, so they give one peak. The OH hydrogen is unique, giving its own peak. So ethanol has three ¹H peaks.

The same logic applies to ¹³C. In ethanol, there are two carbons: one methyl C, one CH₂ C. Two ¹³C peaks.

In benzene (C₆H₆), all six protons are equivalent (the ring is symmetric), so the spectrum shows just one peak. All six carbons are equivalent too, so the ¹³C spectrum shows one peak.

Counting equivalent and inequivalent nuclei is one of the first things you learn to do with structures. The number of peaks in the spectrum equals the number of distinguishable environments.

## Integration: counting hydrogens at each peak

In ¹H NMR, the *area* under each peak is proportional to the number of equivalent protons giving rise to it. Modern instruments measure the area automatically and report it as an *integration* — usually as a horizontal step at each peak, with the height of the step proportional to the area.

So a peak with three protons has three times the area of a peak with one proton. By comparing integrations across the spectrum, you can determine the number of hydrogens at each environment.

For ethanol: integrations are 3:2:1 (CH₃:CH₂:OH). Sum to 6, the total number of protons.

(¹³C integrations are not generally accurate, because the technique used to acquire ¹³C spectra distorts the relative areas. ¹³C peaks are typically counted but not integrated.)

## Spin–spin coupling: hydrogens that talk to each other

Adjacent NMR-active nuclei can magnetically interact, splitting each other's signals. This is *spin–spin coupling*, and it's the most information-rich feature of an NMR spectrum.

Consider a CH–CH fragment. Each carbon has one H, and the two H's are on adjacent carbons. The spin of each H affects the local magnetic field experienced by the other. So the H on the first carbon "feels" two slightly different magnetic fields — one when its neighbor's spin is up, one when its neighbor's spin is down. Each H in the spectrum therefore splits into two peaks (a *doublet*) instead of one.

The general rule (the *n+1 rule*): a hydrogen with *n* equivalent neighboring hydrogens (on adjacent carbons) is split into *n+1* peaks. So:

- A H next to no other H's: singlet (1 peak)
- A H next to one H: doublet (2 peaks)
- A H next to two equivalent H's: triplet (3 peaks)
- A H next to three equivalent H's: quartet (4 peaks)
- A H next to four equivalent H's: quintet (5 peaks)
- A H next to six equivalent H's: septet (7 peaks)

The *intensities* of the peaks within a multiplet follow Pascal's triangle: 1:1 for a doublet, 1:2:1 for a triplet, 1:3:3:1 for a quartet.

The *spacing* between peaks within a multiplet is the *coupling constant J*, measured in Hz. For typical alkyl C–H couplings, J is about 6–8 Hz. For C=C–H couplings, J ranges from 0 (geminal) to 19 (trans) depending on geometry. The coupling constant doesn't depend on the magnetic field strength, so it's an absolute measure of the magnetic interaction.

Coupling is between *neighboring* hydrogens, not equivalent ones. The three CH₃ hydrogens in ethanol are all equivalent — they don't split each other. They're coupled to the two CH₂ neighbors. The CH₂ hydrogens are coupled to the three CH₃ neighbors and to the OH hydrogen.

So in ethanol's ¹H spectrum:
- The CH₃ peak appears as a triplet (n = 2 from CH₂), at about δ 1.2.
- The CH₂ peak appears as a quartet (n = 3 from CH₃, with maybe additional fine structure from OH), at about δ 3.7.
- The OH peak is variable in position and shape (often broad due to exchange).

Diethyl ether (CH₃CH₂OCH₂CH₃) shows just two ¹H peaks because the two ethyl groups are equivalent. The CH₃ peak is a triplet (n = 2), the CH₂ peak is a quartet (n = 3). Same pattern as ethanol's two main peaks, simpler because there's no OH.

## Reading a multiplet pattern

The combination of chemical shift, integration, and splitting pattern lets you read off structural information:

- Chemical shift → what environment is this proton in?
- Integration → how many equivalent protons?
- Splitting → how many neighboring protons?
- Coupling constant → what kind of coupling? (geminal, vicinal, allylic, etc.)

A worked example. The molecule 2-bromopropane, (CH₃)₂CHBr.

Two distinct H environments: the central CH (one proton) and the two equivalent CH₃ groups (six protons).

¹H spectrum:
- A septet (n = 6 neighboring H's from the two methyls) at higher chemical shift (the CH near a Br is deshielded), integrating for 1 H.
- A doublet (n = 1 neighboring H from the CH) at lower chemical shift, integrating for 6 H.

The 1:6 integration ratio confirms the assignment, and the septet/doublet pattern matches the molecular structure exactly.

## ¹³C NMR: simpler in shape, just as informative

¹³C NMR is acquired in a way that decouples it from ¹H spins, so all ¹³C signals appear as singlets (no splitting). This makes the spectrum easier to read but loses the multiplet information that helps in ¹H.

What ¹³C gives you:
- The number of distinct carbon environments.
- The chemical shift of each, which identifies the carbon type (sp³ alkyl, sp² alkene, aromatic, carbonyl, etc.).

¹³C is particularly diagnostic for aromatic substitution patterns and for carbonyl-containing molecules. A clean spectrum with peaks at δ 20, 30, 50, 130, 165 (for example) tells you immediately: an alkyl region, an alkene/aromatic region, and a carbonyl. The positions narrow down the structure further.

A modern ¹³C NMR experiment runs in a few minutes for a good sample and provides a cleaner, more interpretable spectrum than ¹H for many compounds.

## DEPT and other variants

Several specialized NMR experiments give additional structural information:

**DEPT** (Distortionless Enhancement by Polarization Transfer): a ¹³C experiment that distinguishes carbons by how many H's they bear. CH₃ peaks point up, CH peaks point up, CH₂ peaks point down, and quaternary carbons (no H's) don't appear. So one DEPT spectrum tells you how many carbons have 0, 1, 2, or 3 attached H's.

**COSY** (Correlation Spectroscopy): a 2D NMR experiment that maps which protons are coupled to which. A 2D spectrum has chemical shift on both axes; cross-peaks indicate coupling between the two corresponding protons. Excellent for tracing the H–H connectivity of a molecule.

**HSQC** (Heteronuclear Single Quantum Coherence): a 2D experiment that maps each ¹³C to the ¹H attached to it. Used to identify which proton in a complex spectrum corresponds to which carbon.

**HMBC** (Heteronuclear Multiple Bond Correlation): the longer-range version of HSQC, mapping H to C through 2 or 3 bonds. Used to establish which fragment connects to which.

**NOESY** (Nuclear Overhauser Effect Spectroscopy): detects through-space proximity (not through-bond connectivity), useful for stereochemistry and three-dimensional structure.

For most organic structures, the standard battery is ¹H NMR + ¹³C NMR + DEPT + COSY + HSQC + HMBC, often with NOESY for stereochemistry. With these, you can determine almost any structure if you have a few milligrams of pure material.

For biological NMR — protein structures, drug binding, metabolomics — many additional experiments are used, and the experiments on pure proteins can take days. The 1991 Nobel Prize (Ernst, for FT-NMR development) and the 2002 Nobel Prize (Wüthrich, for protein NMR) reflect the importance of this work.

↳ **Dig Deeper — Why ¹H and ¹³C have such different chemical shift ranges**

> ¹H NMR shifts span about 0–12 ppm. ¹³C shifts span 0–220 ppm. Why is the carbon range almost twenty times larger? Walk through the physical origins. Cover: paramagnetic vs diamagnetic shielding contributions, the role of low-lying excited states (which affect ¹³C much more than ¹H), the σ → π* and π → σ* contributions in C=C and C=O groups, and why aromatic ring currents dominate the chemical shift range for both nuclei.

**What to do with the output:** Compare against any physical chemistry textbook chapter on NMR theory. Verify that Claude correctly distinguishes the diamagnetic term (electron density in s orbitals around the nucleus) from the paramagnetic term (couples ground-state to excited-state through the magnetic field).

## A worked structure determination

Let's combine everything. An unknown compound has:
- Mass spectrum: M⁺ = 88. Fragment at m/z = 73 (loss of 15, CH₃·).
- IR: strong band at 1715 cm⁻¹.
- ¹H NMR: triplet at δ 1.05 (3H), singlet at δ 2.13 (3H), quartet at δ 2.45 (2H).
- ¹³C NMR: peaks at δ 7.9, δ 29.5, δ 36.1, δ 209.6.

Step by step:

Molecular weight 88. Consistent with C₅H₁₂O (M = 88), C₄H₈O₂ (M = 88), C₃H₈O₂N (M = 90, too high), or other. Loss of CH₃· (15) suggests a methyl group.

IR 1715 cm⁻¹ is a ketone C=O. So C₄H₈O is consistent (M = 72, no), wait — C₅H₁₀O (M = 86, no). Let me recheck: C₅H₁₂O = 88, but the IR says ketone, which wouldn't fit C₅H₁₂O (no double bond). C₅H₁₀O (M = 86) is close but off by 2. Let me try C₄H₈O₂ (88): two oxygens, ketone band — could be a hydroxyacid or ester, but the ¹H pattern doesn't quite match.

The ¹³C peak at δ 209.6 is unmistakably a ketone C=O. Combined with the M = 88 and the IR, this is probably 2-pentanone (C₅H₁₀O, M = 86 — close to 88, hmm).

Let me reconsider. Perhaps M⁺ at 88 is wrong, or perhaps I miscounted. With M = 86 (C₅H₁₀O), the fragment at 73 (loss of 13?) — that doesn't make sense.

Try M = 72: C₄H₈O. Loss of 15 → 57. So fragments at 57 — and the ¹³C at 209.6 means ketone — this could be 2-butanone (CH₃COCH₂CH₃).

¹H of 2-butanone: methyl singlet δ 2.1 (3H), CH₂ quartet δ 2.5 (2H), CH₃ triplet δ 1.0 (3H). That matches! So the unknown is 2-butanone, M = 72. (I'd had M = 88 wrong; it should be 72.)

The lesson: cross-check across all four sources (MS, IR, ¹H, ¹³C). If the data don't all fit, recheck the data. Real structure determination is iterative.

## What this chapter does

NMR maps the framework of a molecule. ¹H NMR tells you how many distinguishable hydrogens there are, what environment each is in (chemical shift), how many of each (integration), and how each is connected to its neighbors (splitting/coupling). ¹³C NMR does the same for carbon. Specialized experiments (DEPT, COSY, HSQC, HMBC, NOESY) fill in details about which carbon has how many hydrogens, which hydrogens are coupled to which, and which atoms are close in space.

The combination of mass spectrometry (Chapter 12) + IR (Chapter 12) + ¹H NMR + ¹³C NMR is enough to identify almost every small organic molecule. The detective work — chemical shifts that locate functional groups, splittings that count neighbors, integrations that count hydrogens, mass-spec fragmentations that locate weak bonds — combines into a structural assignment that's usually unambiguous.

This is how organic chemistry knows what it's made. A synthesis can produce a target, a side product, or a complete mess, and the spectroscopy tells you which. Modern NMR is so sensitive that micrograms of material are often enough; modern mass spec is so accurate that exact masses confirm formulas. The bottleneck in most syntheses is no longer "did I make the right thing?" — it's "did I make enough of it?"

The next chapter pivots to a different topic: conjugated systems and ultraviolet spectroscopy. We come back to spectroscopy briefly there to cover how UV-vis fits in. After that, the chemistry returns to functional-group reactions, with NMR and MS implicit in everything we discuss.

---

*Source for all data, examples, and historical references: OpenStax* Organic Chemistry*, Chapter 13, modules m00143 through m00156.*
---

## LLM Exercise — Chapter 13: Nuclear Magnetic Resonance Spectroscopy (Synthesize a Target Molecule Project)

**Project:** Synthesize a Target Molecule.
**What you're building this chapter:** predict ¹H and ¹³C NMR spectra of your target.
**Tool:** **Claude Project**.

---

**The Prompt:**

```
Chapter 13 of my Synthesis project. Chapter 13 taught:
   - **¹H NMR**: chemical shift in ppm (0-10 typical for organic);
     higher shift = more downfield = more deshielded by nearby
     electronegative atoms; chemical-shift table:
       - 0.5-1.5: alkane CH
       - 1.5-2.5: allylic, alpha to C=O, alpha to halogen
       - 2.5-3.5: alpha to N, S, electronegative
       - 3.5-4.5: alpha to O (alcohols, ethers)
       - 4.5-6.5: vinyl CH (alkene)
       - 6.5-8: aromatic CH
       - 9-10: aldehyde CH
       - 10-13: carboxylic acid OH (exchangeable)
   - **Integration**: ratio of protons per signal.
   - **Multiplicity (n+1 rule)**: # neighbors + 1 = peaks; singlet
     (no neighbors), doublet (1), triplet (2), quartet (3), etc.
   - **Coupling constants (J)**: vicinal coupling ~6-8 Hz typical;
     cis-vinyl 6-12 Hz; trans-vinyl 12-18 Hz; aromatic ortho 8 Hz.
   - **¹³C NMR**: chemical shift 0-220 ppm; alkyl 0-50; alkene 100-
     140; aromatic 110-160; carbonyl 160-220.
   - **DEPT, COSY, HSQC, NOESY**: 2D NMR for connecting protons to
     carbons and to each other.

Write the brief's "NMR Prediction" section in 500–700 words.

1. **¹H NMR.** For each unique proton in your target (use the
   molecular symmetry to group equivalent protons):
   - Predicted chemical shift (ppm).
   - Integration (number of H's).
   - Multiplicity (n+1 rule based on adjacent non-equivalent
     protons).
   - Expected coupling constant (J) for the dominant coupling.

2. **¹³C NMR.** For each unique carbon:
   - Predicted chemical shift.
   - Type (alkyl, alkene, aromatic, carbonyl, etc.).

3. **Sketch the ¹H NMR.** Show δ (ppm) on x-axis, intensity on
   y-axis. Mark each peak with its multiplicity and integration.

4. **Key diagnostic signals.** Identify the 2-3 most diagnostic
   signals in the ¹H NMR — the ones that would tell you you have
   the right product. For drugs, this often includes:
   - The aromatic protons' pattern (singlets vs. doublets indicate
     substitution pattern).
   - Specific functional-group protons (OH, NH, alpha to
     carbonyl).
   - Stereocenter protons (chemical shift sensitive to
     stereochemistry).

5. **2D NMR.** For complex products: which 2D experiment would
   be most useful for unambiguous structure assignment? COSY
   shows H-H correlations through bonds; HSQC shows H-C
   correlations; NOESY shows H-H proximity through space (useful
   for stereochemistry).

End with: at which steps in your developing synthesis would NMR
catch the most diagnostic failure modes (wrong regio, wrong
stereo, incomplete reaction)?
```

---

**What this produces:** A 500–700 word section with predicted NMR signals. NMR is organic chemistry's most powerful verification tool; this exercise builds the prediction discipline.

**How to adapt this prompt:**

- *For your own project:* Use a reference table or NMR predictor (ChemDraw, Mestrelab Mnova) to cross-check. LLM-predicted chemical shifts are often roughly right but unreliable in detail.
- *For ChatGPT / Gemini:* Works as written. Verify shifts against published spectra.
- *For Claude Code:* Optional — RDKit and Mnova can predict NMR.
- *For a Claude Project:* Append.

**Connection to previous chapters:** Ch 12's MS/IR + Ch 13's NMR form the complete spectroscopic toolkit.

**Preview of next chapter:** Chapter 14 covers conjugated systems and UV spectroscopy. If your target has conjugation (most drugs do), you'll predict UV absorption and check for Diels-Alder opportunities in synthesis.


---

## AI Wayback Machine

**Isidor Isaac Rabi** was discovered nuclear magnetic resonance in 1938 — the technique that became the workhorse of organic structure determination. Nobel 1944.

**Run this:**

```
Who is Isidor Isaac Rabi, and how does their work connect to NMR spectroscopy we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about their career or ideas.
```

→ Search **"Isidor Isaac Rabi"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to walk through one of Isidor Isaac Rabi's key experiments or syntheses in detail.
- Add a constraint: "Answer including criticisms or limits of Isidor Isaac Rabi's framework."

What changes? What gets better? What gets worse?
