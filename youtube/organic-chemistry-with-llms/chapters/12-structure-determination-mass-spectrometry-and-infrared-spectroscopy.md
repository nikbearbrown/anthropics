# Chapter 12 — Structure Determination: Mass Spectrometry and Infrared Spectroscopy

*Once you've made a compound, you have to prove what it is. Mass spectrometry tells you the molecular formula and weight; infrared spectroscopy tells you what functional groups are present. Together, they answer half of every structure-determination problem you'll meet.*

In 1912, when J. J. Thomson built the first mass spectrometer to study isotopes of neon, he showed that there were two stable forms of the element with masses of 20 and 22. Neon-22 was a stable isotope nobody had previously known existed. The mass spectrometer could see what the periodic table couldn't.

A hundred years later, mass spectrometry is the workhorse for identifying unknown molecules. A modern instrument can take a microgram of a compound, vaporize and ionize it, sort the resulting fragments by mass, and produce a fingerprint that uniquely identifies most compounds in the database within seconds. The basic idea hasn't changed since Thomson — measure the mass of the molecule and its fragments, infer the structure — but the sensitivity, mass accuracy, and dynamic range have improved by many orders of magnitude.

This chapter and the next introduce four spectroscopic techniques that, together, are how organic chemists know what they've made. Mass spectrometry tells you the molecular weight (and often formula). Infrared spectroscopy tells you what functional groups are present. Nuclear magnetic resonance spectroscopy (Chapter 13) tells you the carbon and hydrogen framework — how many of each, where they sit, what they're connected to. Ultraviolet–visible spectroscopy (Chapter 14) tells you about extended π systems.

Each technique answers a different question, and the questions overlap just enough that the four together can usually pin down a structure that none of them could alone. Real structure determination in a research lab is almost always a four-way triangulation.

## The four spectroscopic questions

| Technique | Question |
|---|---|
| Mass spectrometry | What is the molecular formula? Is there an isotope pattern? |
| Infrared spectroscopy | What functional groups are present? |
| ¹H and ¹³C NMR | How many distinguishable hydrogens and carbons? In what environments? |
| UV–vis | Is there a conjugated π system? How extended? |

Each chapter takes one or two of these and unpacks them. The goal is for you to be able to look at a spectrum and read structural information off it, by recognizing patterns the way a pathologist recognizes histological patterns or a radiologist recognizes shadows on an X-ray.

## How mass spectrometry works

The standard electron-impact (EI) mass spectrometer has three components: an ion source, a mass analyzer, and a detector.

**Source.** The sample is vaporized, then bombarded with a high-energy beam of electrons (typically 70 eV, equivalent to about 6700 kJ/mol of energy per electron). When a high-energy electron hits a molecule, it knocks a valence electron out of the molecule. The result is a *radical cation* — a species with an unpaired electron and a positive charge. This is the molecular ion, M⁺·.

**Analyzer.** The molecular ion (and its fragments) are accelerated through a magnetic or electric field that separates them by mass-to-charge ratio (m/z). For singly-charged ions, m/z is just the mass.

**Detector.** Each m/z value reaching the detector produces a signal proportional to the number of ions arriving at that value. The output is a *mass spectrum*: a plot of relative intensity versus m/z.

The mass spectrum is conventionally presented with the most intense peak (the *base peak*) set to 100% intensity, and other peaks shown as fractions of that. The molecular ion peak (M⁺·) is at the highest m/z value (assuming the molecule survives the ionization without fragmenting). M⁺· may or may not be the base peak — sometimes a fragment is more abundant than the molecular ion.

## What you can read off a mass spectrum

**The molecular weight.** The molecular ion peak gives the total mass of the molecule. For propane (C₃H₈), the molecular ion is at m/z = 44. For 1-butene (C₄H₈), it's at m/z = 56.

**The molecular formula (sometimes).** If you can determine the exact mass to four decimal places (which requires high-resolution instruments), the molecular formula often follows uniquely, because different combinations of atoms have slightly different exact masses (carbon-12 is exactly 12.0000, but hydrogen is 1.00783, oxygen is 15.9949, nitrogen is 14.0031, and so on). For unit-resolution instruments, you have to combine the molecular weight with constraints (degrees of unsaturation from chemistry, isotope patterns) to narrow down the formula.

**Isotope patterns.** Many elements have isotopes whose abundances are reflected in the spectrum. Carbon is 98.9% ¹²C and 1.1% ¹³C — so a molecule with one carbon shows two peaks at M and M+1, with the M+1 about 1.1% as tall as M. With more carbons, the M+1 peak grows: ten carbons → ~11% at M+1.

Some elements have very characteristic isotope patterns. Bromine is 51% ⁷⁹Br and 49% ⁸¹Br — so a molecule with one Br shows essentially equal peaks at M and M+2. Chlorine is 76% ³⁵Cl and 24% ³⁷Cl — about a 3:1 M:M+2 ratio. Sulfur has a noticeable M+2 contribution (about 4%) too.

The isotope pattern is the diagnostic for halogen-containing molecules. If you see a strong M+2 peak almost equal in height to M, you're looking at a bromide. If 3:1, a chloride. If you see the M+2 peak about 4% the height of M, you're looking at a sulfide or thiol.

**The fragmentation pattern.** When the molecule absorbs the high-energy electron, it picks up enough energy to break weak bonds. The molecule fragments. Each fragment can be a cation (which the mass spectrometer detects) or a neutral (which it doesn't). The mass spectrum is the cation pattern.

Common fragmentation rules:
- Loss of a methyl group: M⁺· → (M−15)⁺ + CH₃·. Common but not always present.
- Loss of an ethyl group: M⁺· → (M−29)⁺ + CH₃CH₂·.
- Loss of a propyl group: M⁺· → (M−43)⁺ + CH₃CH₂CH₂·.
- Loss of water: M⁺· → (M−18)⁺ + H₂O. Common from alcohols.
- Loss of CO: M⁺· → (M−28)⁺ + CO. Common from aldehydes and ketones.

Fragmentations that produce *stable cations* are favored. So a substrate that can fragment to give a tertiary carbocation will show that fragment strongly. A substrate that can fragment to give a benzyl cation (resonance-stabilized) will show that strongly too. The fragmentation pattern is therefore a kind of structural fingerprint, with the most-stable cations dominating.

For 2-methylpentane, for instance, the molecular ion is at m/z = 86, and there's a strong fragment at m/z = 43 (corresponding to a propyl cation, formed by loss of a propyl radical). For hexane (no branches), you see a series of fragment peaks corresponding to losses of CH₃, C₂H₅, C₃H₇, C₄H₉ — m/z = 71, 57, 43, 29 — because all the C–C bonds in hexane are similarly weak.

In practice, modern compound identification often relies on database matching: take the spectrum, search a library (NIST has more than 700,000 reference spectra), and look for the closest match. Manual interpretation is reserved for unusual structures or new compounds.

## Soft ionization and modern variants

Electron impact is the classic technique, but it's not the only one. EI fragments many molecules so heavily that the molecular ion is faint or absent. For thermally fragile molecules (large biomolecules, polymers), softer ionization is needed.

Common soft ionization methods:
- *Chemical ionization (CI):* the sample is ionized by interaction with a reagent gas (methane, isobutane, ammonia) instead of by direct electron impact. Gives less fragmentation.
- *Electrospray ionization (ESI):* the sample is sprayed from a fine needle through a high-voltage potential. Used routinely for proteins and other large biomolecules. Can produce multiply-charged ions.
- *MALDI (matrix-assisted laser desorption/ionization):* the sample is mixed with a UV-absorbing matrix and zapped with a laser. Useful for proteins and polymers.
- *FAB (fast atom bombardment):* the sample is bombarded with a beam of fast neutral atoms. Gives clean molecular ions for non-volatile compounds.

Each technique has its niche. For routine identification of small organic molecules, EI is still the most common. For biomolecules and pharmaceuticals, ESI or MALDI dominates.

The mass analyzer also varies: magnetic-sector instruments are accurate but expensive; quadrupoles are cheap and fast; time-of-flight (TOF) gives high resolution; ion-trap instruments allow MS/MS experiments where you select one ion and fragment it further. The choice depends on the application.

## Infrared spectroscopy

Infrared light has wavelengths of about 2.5 to 25 micrometers (μm), with frequencies often reported as *wavenumbers* (the inverse of wavelength, in cm⁻¹). The infrared region extends from about 400 cm⁻¹ to 4000 cm⁻¹.

When IR light passes through an organic molecule, it can be absorbed if the energy of the photon matches the energy needed to excite a vibrational mode of the molecule. Different bonds vibrate at different frequencies, and the frequencies depend mostly on the *strength* of the bond and the *masses* of the atoms.

A simple harmonic oscillator model gives:

$$\nu = \frac{1}{2\pi} \sqrt{\frac{k}{\mu}}$$

where ν is the vibrational frequency, k is the force constant of the bond (a measure of bond strength), and μ is the reduced mass of the two atoms. Stronger bonds vibrate faster (higher frequency, higher wavenumber). Lighter atoms vibrate faster.

A C–H bond (k ≈ 500 N/m, μ ≈ 1) vibrates at about 3000 cm⁻¹. A C=O bond (k ≈ 1200 N/m) vibrates at about 1700 cm⁻¹. A C=C bond (k ≈ 1000 N/m) at about 1650 cm⁻¹. A C–C single bond at about 1000–1200 cm⁻¹.

The absorption pattern — the IR spectrum — has different bands at different positions, each corresponding to a particular vibrational mode of a particular bond.

## Reading an IR spectrum

The infrared spectrum is conventionally plotted with %T (percent transmittance) on the y-axis (or absorbance, but transmittance is older) and wavenumber (cm⁻¹) on the x-axis, *decreasing from left to right* (so 4000 cm⁻¹ is on the left and 400 cm⁻¹ is on the right). Absorption bands appear as downward-pointing valleys.

The spectrum has two regions:

**Functional-group region (4000–1500 cm⁻¹).** Where most diagnostic peaks live. Most functional groups have characteristic absorptions in this region.

**Fingerprint region (1500–400 cm⁻¹).** A complex pattern of overlapping bands, unique to each compound but hard to interpret in detail. Used mainly for matching against reference spectra.

Diagnostic bands to memorize for the functional-group region:

| Group | Wavenumber (cm⁻¹) | Comment |
|---|---|---|
| O–H (alcohol) | 3200–3550 | broad, strong |
| O–H (carboxylic acid) | 2500–3300 | very broad |
| N–H | 3300–3500 | sharp, can be doublet (NH₂) |
| C–H (sp) | 3300 | sharp, terminal alkyne |
| C–H (sp²) | 3000–3100 | medium |
| C–H (sp³) | 2850–2960 | strong |
| C≡C | 2100–2260 | weak (often hard to see) |
| C≡N | 2210–2260 | strong |
| C=O | 1670–1780 | very strong; position depends on type (aldehyde 1720, ketone 1715, ester 1735, amide 1690, anhydride 1750/1820) |
| C=C (alkene) | 1640–1680 | medium |
| C=C (aromatic) | 1450–1600 | several bands, medium |

The C=O band is one of the most useful in the spectrum. Its position varies enough to distinguish between aldehydes, ketones, esters, amides, and anhydrides:
- aldehyde: ~1720 cm⁻¹
- ketone: ~1715 cm⁻¹
- ester: ~1735 cm⁻¹
- amide: ~1690 cm⁻¹
- anhydride: 1750 and 1820 (two bands)
- acid chloride: ~1800 cm⁻¹
- carboxylic acid: ~1710 cm⁻¹

Conjugation with a C=C lowers the C=O frequency by about 30 cm⁻¹ (because the conjugated bond has more single-bond character). Conjugation also broadens the band.

A classic IR-based diagnostic move: see a strong band near 1700 cm⁻¹ → there's a carbonyl. The exact position tells you what kind of carbonyl. Confirm with NMR.

Another diagnostic: a broad O–H band centered around 3300 cm⁻¹ → alcohol or carboxylic acid. The width and breadth tell you which (alcohol bands are narrower; carboxylic acid bands are broader and extend further to lower wavenumbers).

## How IR spectra come from molecules

Each IR band corresponds to a specific *vibrational mode* — a specific way the atoms in the molecule move. The two main types:

**Stretching modes:** atoms moving along the bond axis, alternately stretching and compressing the bond. Higher energy than bending modes.

**Bending modes:** atoms moving sideways, with the bond angle changing. Lower energy.

For a diatomic molecule (one bond), there's only one stretching mode. For a polyatomic molecule, there are 3N − 6 vibrational modes (N is the number of atoms, the "−6" accounts for translation and rotation), or 3N − 5 for a linear molecule. So benzene (12 atoms) has 30 vibrational modes, all of which can in principle absorb IR light. Some are forbidden by symmetry; others overlap with each other; some are too weak to see.

A vibrational mode is *IR active* (visible in the spectrum) only if it changes the molecule's dipole moment. Symmetric stretching modes in symmetric molecules (like the symmetric C–H stretch in CO₂) are often IR inactive — the dipole moment doesn't change during the vibration, so no light is absorbed.

This is why CO₂ has a major IR-absorbing mode (the asymmetric stretch, with one C–O lengthening while the other compresses) but no IR signature at the symmetric stretch frequency. The same kind of selection rule explains why some bands are strong and others are weak in any IR spectrum.

## A worked IR interpretation

Suppose you have a compound with molecular formula C₅H₁₀O. The degree of unsaturation is (2×5 + 2 − 10)/2 = 1, so there's either one ring or one double bond.

The IR shows:
- Strong band at 1715 cm⁻¹.
- No O–H band in the 3200–3550 region.
- C–H bands at 2850–2960.

The 1715 cm⁻¹ band is a carbonyl, and it's a ketone (1715 ± 5). No alcohol. No ring (because the carbonyl explains the unsaturation).

C₅H₁₀O with one ketone — possibilities are 2-pentanone, 3-pentanone, 3-methyl-2-butanone. To distinguish, you'd use NMR.

## Limitations of mass spec and IR

Both techniques have limitations. Mass spectrometry tells you the molecular formula but not the connectivity — it can tell ethanol from methyl ether (C₂H₆O for both, but they fragment differently), but it cannot generally tell n-pentane from isopentane (similar fragments, similar pattern). For full structural determination, you need NMR.

IR spectroscopy tells you what functional groups are present but not how many or where. Two ketones in a molecule give one carbonyl band (which may be slightly broadened). A complex molecule with multiple functional groups gives a tangled spectrum. The fingerprint region is essentially unreadable by eye for new compounds — it's used for database matching, not de novo interpretation.

NMR (Chapter 13) is the technique that fills in the gaps. NMR can count carbons and hydrogens, distinguish them by chemical environment, and tell you what's connected to what.

↳ **Dig Deeper — Why the carbonyl frequency varies with electron donation/withdrawal**

> The C=O stretching frequency varies systematically: amide < ester < acid < ketone < aldehyde < ester < acid chloride < anhydride. Walk through the electronic argument. Cover: how electron donation from a heteroatom (N in amides, O in esters) reduces the C=O bond order via resonance, how electron withdrawal (Cl in acid chlorides, the inductive effect of acyl groups in anhydrides) increases the C=O bond order, and how the resulting changes in bond strength shift the IR frequency upward or downward.

**What to do with the output:** Verify the explanation accounts for both resonance (for nitrogen and oxygen donors) and induction (for chlorine in acid chlorides). The IR shift of 30 cm⁻¹ for conjugation with a C=C is also a useful sanity check — Claude should explain why conjugation lowers the frequency.

## What this chapter does

Mass spectrometry tells you the molecular weight (always), the molecular formula (often, especially with high-resolution instruments), and a fragmentation pattern that's a structural fingerprint. The molecular ion (M⁺·) sits at the highest m/z. Isotope patterns reveal the presence of bromine, chlorine, sulfur, and similar elements. Fragmentation favors stable cations, so the spectrum mostly shows fragments corresponding to favorable cleavages.

Infrared spectroscopy tells you what functional groups are present. The functional-group region (4000–1500 cm⁻¹) has diagnostic bands for O–H, N–H, C–H, C≡C, C≡N, C=O, C=C, and others. The C=O band is especially diagnostic — its position distinguishes aldehyde, ketone, ester, amide, anhydride, acid chloride, and acid. Conjugation lowers the carbonyl frequency.

Mass spec + IR together typically identifies the molecular formula and the functional groups. NMR (next chapter) fills in the connectivity. UV–vis (Chapter 14) tells you about extended π systems.

The combination of these techniques is how organic chemists know what they've made — both during a synthesis (verifying intermediates) and after (characterizing natural products, identifying unknowns, checking that drugs are pure). The actual practice of structure determination is a triangulation across these methods, and a chemist trained in reading spectra can usually identify a compound within minutes from the four together.

---

*Source for all data, examples, and historical references: OpenStax* Organic Chemistry*, Chapter 12, modules m00134 through m00142.*
---

## LLM Exercise — Chapter 12: Mass Spectrometry and Infrared Spectroscopy (Synthesize a Target Molecule Project)

**Project:** Synthesize a Target Molecule.
**What you're building this chapter:** predict the MS and IR spectra of your target molecule.
**Tool:** **Claude Project**.

---

**The Prompt:**

```
Chapter 12 of my Synthesis project. Chapter 12 taught:
   - **Mass Spectrometry**: ionization produces a molecular ion
     (M⁺); fragmentation produces fragment ions; the base peak
     is the most-intense ion; cleavage patterns follow predictable
     rules (alpha cleavage near functional groups; loss of common
     small molecules like H₂O, CO₂, CH₃).
   - **Infrared Spectroscopy**: bonds absorb at characteristic
     frequencies; the fingerprint region (below 1500 cm⁻¹) is
     molecule-specific; common diagnostic bands:
       - O-H (broad, 3200-3550 cm⁻¹ alcohols; 2500-3300 acids)
       - N-H (3300-3500, sharper than O-H)
       - C-H (2850-3000 sp³; 3030-3100 sp²; 3300 sp)
       - C=O (1680-1750, strong)
       - C=C (1640-1680, weak)
       - C≡C / C≡N (2100-2260)
       - Aromatic C=C (1600 and 1500, plus 690-900 fingerprint)

Write the brief's "MS and IR Prediction" section in 400–600 words.

1. **Mass spec prediction.**
   - Molecular ion (M⁺) at the molecular weight of your target.
   - Major fragments: alpha cleavage near each functional group
     produces predictable losses. For example, an aldehyde loses
     CHO (29 amu); a methyl ester loses OCH₃ (31 amu); aromatic
     compounds often show benzyl cation (91 amu) for substituted
     toluenes.
   - Predict the 2-4 most-intense peaks beyond M⁺.

2. **IR prediction.** For each functional group in your target,
   predict the diagnostic IR bands:
   - The wavenumber (or range).
   - The intensity (strong/medium/weak).
   - The shape (broad/sharp).

3. **Fingerprint analysis.** The fingerprint region (400-1500
   cm⁻¹) is complex but characteristic. Note any unusually
   diagnostic bands (e.g., the aromatic ring substitution pattern
   gives bands in 690-900 cm⁻¹ that distinguish ortho, meta,
   para, monosubstituted).

4. **Sketch the IR spectrum.** Show transmittance (y-axis) vs.
   wavenumber (x-axis, decreasing left to right from 4000 to
   400 cm⁻¹). Mark the major diagnostic bands.

5. **The synthesis-verification implication.** At which steps in
   your developing synthesis would IR (or MS) tell you the
   reaction worked or didn't?
   - Did the carbonyl get reduced? (Loss of C=O band ~1700 cm⁻¹;
     appearance of O-H band ~3500.)
   - Did the alkene get hydrogenated? (Loss of C=C band ~1650;
     loss of sp² C-H ~3050.)
   - Did the amine acylate? (Appearance of amide C=O at ~1650.)

End with one expected M⁺ peak and one expected IR band for the
final target. Both will be the verification signatures at the
end of your synthesis.
```

---

**What this produces:** A 400–600 word section with predicted MS fragments and IR bands. Most synthesis chemists check IR after every step; this exercise builds that habit.

**How to adapt this prompt:**

- *For your own project:* Online tools like ChemDraw or NIST WebBook can produce reference spectra to compare against your predictions. Don't trust LLMs for unusual molecules without verification — the book's premise is that LLMs are weak on spectroscopy.
- *For ChatGPT / Gemini:* Works as written. Predicted spectra should be cross-checked against published spectra.
- *For Claude Code:* Optional — RDKit and similar libraries can predict approximate IR/MS data.
- *For a Claude Project:* Append.

**Connection to previous chapters:** First time the project applies analytical chemistry to verify what mechanism predictions promise.

**Preview of next chapter:** Chapter 13 is NMR — the most powerful structure-elucidation tool. You'll predict the ¹H and ¹³C NMR spectra of your target, completing the structure-verification toolkit.


---

## AI Wayback Machine

**Fred McLafferty** was developed mass spectrometry interpretation rules — including the McLafferty rearrangement — that organic chemists still use.

**Run this:**

```
Who is Fred McLafferty, and how does their work connect to mass spectrometry we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about their career or ideas.
```

→ Search **"Fred McLafferty"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to walk through one of Fred McLafferty's key experiments or syntheses in detail.
- Add a constraint: "Answer including criticisms or limits of Fred McLafferty's framework."

What changes? What gets better? What gets worse?
