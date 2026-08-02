# Chapter 14 — Conjugated Compounds and Ultraviolet Spectroscopy

*Two double bonds in conjugation behave differently from two double bonds in isolation. The difference is delocalization — the π electrons spread out over more than two atoms — and it changes the chemistry, the spectroscopy, and the color of the molecule.*

In 1928 Otto Diels and Kurt Alder discovered that 1,3-butadiene and maleic anhydride combine spontaneously to form a six-membered ring at temperatures around 100 °C. No catalyst. No solvent. Two molecules joining to make one, with three bonds forming and two breaking in a single concerted step. The product is a cyclohexene with two new substituents and a defined stereochemistry. The reaction won them the 1950 Nobel Prize and is now one of the most useful in synthesis: thousands of total syntheses have used Diels–Alder reactions to assemble complex natural products.

The Diels–Alder reaction works specifically because butadiene is a *conjugated* diene — its two double bonds are connected by a single bond that has partial π character through delocalization. This delocalization is responsible for a whole bundle of unusual properties: the molecule is more stable than a non-conjugated diene, the central C–C bond is shorter than a normal single bond, the molecule absorbs UV light at longer wavelengths than an isolated alkene, and it undergoes 1,2- and 1,4-addition reactions with electrophiles. All of these traces back to the same physical fact: when two π bonds are conjugated, the electrons spread out across all four carbons rather than staying confined to two.

This chapter covers conjugated systems — what they are, why they're special, how they react, and how UV spectroscopy detects them. The chapter also formally introduces molecular orbital theory in a way that we'll need for the rest of the book, particularly Chapter 30 (pericyclic reactions).

## What conjugation means

Two double bonds are *conjugated* if they alternate with a single bond — pattern is C=C–C=C. The single bond between them is short and unusually rigid, suggesting it has some π character.

Examples of conjugated systems:
- 1,3-butadiene: H₂C=CH–CH=CH₂
- 1,3,5-hexatriene: H₂C=CH–CH=CH–CH=CH₂
- α,β-unsaturated ketones: R–C(=O)–CH=CH–R′ (a C=O conjugated with a C=C)
- benzene: C₆H₆, three alternating C=C and C–C bonds in a six-membered ring

Examples of *non-conjugated* systems:
- 1,4-pentadiene: H₂C=CH–CH₂–CH=CH₂ (two double bonds separated by two single bonds)
- 1,5-hexadiene: H₂C=CH–CH₂–CH₂–CH=CH₂

The diagnostic for conjugation is alternation. Each carbon between two double bonds must be sp² and contribute a p orbital that overlaps with the p orbitals of the double bonds on either side. If a CH₂ (sp³) is interrupting the chain, the conjugation is broken.

## Why conjugated dienes are more stable

A conjugated diene is about 15 kJ/mol more stable than the corresponding non-conjugated diene with the same number of double bonds. Two pieces of evidence:

**Heats of hydrogenation.** Hydrogenation of an isolated alkene releases about 126 kJ/mol of heat. Hydrogenation of two isolated alkenes (like 1,4-pentadiene) releases about 253 kJ/mol — twice the single-alkene value, as expected. But hydrogenation of 1,3-butadiene releases only 236 kJ/mol — 17 kJ/mol less than two isolated double bonds would give. This difference is the *conjugation stabilization* of butadiene.

**Bond lengths.** The central C–C single bond in 1,3-butadiene is 147 pm long — shorter than a typical C–C single bond (153 pm), longer than a typical C=C double bond (134 pm). The shortening reflects partial π character from the overlap of the two double bonds across the central bond.

The molecular orbital explanation. In a conjugated diene, all four 2p orbitals from the four carbons are aligned in the same plane and can overlap with each other, not just with the two p's that share the original double bond. Linear combinations of these four atomic orbitals give *four* π molecular orbitals — two bonding and two antibonding. The four π electrons (two from each original double bond) fill the two bonding MOs.

The lowest-energy bonding MO has electron density spread evenly across all four carbons — it's the *delocalized* MO. The fact that some electrons live in this fully delocalized MO is what gives conjugation its stabilizing effect. The electrons aren't constrained to be in particular C–C bonds; they spread out, lowering their average energy.

This is the same kind of stabilization that makes resonance structures more stable than any single contributor (Chapter 2). Conjugation is delocalization, in a slightly different (more orbital-physics-y) language.

## Electrophilic addition to conjugated dienes

Take 1,3-butadiene and add HBr at low temperature. The reaction follows the standard polar-addition mechanism — H⁺ attacks one of the alkene carbons to form a carbocation, then Br⁻ captures the carbocation. But because butadiene's first carbon (C1) is at the end of a conjugated system, the resulting cation is *allylic* — it has a C=C adjacent to the cationic carbon, so resonance delocalizes the positive charge across two carbons.

Two products are possible:
- **1,2-addition:** the Br lands on C2, immediately adjacent to the H. Product: 3-bromo-1-butene.
- **1,4-addition:** the Br lands on C4, the far end of the original conjugated system. Product: 1-bromo-2-butene.

At low temperature (–80 °C), the *1,2-product* dominates — it's the *kinetic product*. The Br lands faster on C2 because that's the carbon whose C–Br bond forms first as the cation is captured (the cation has slightly more positive charge on C2 than on C4 in the geometric arrangement that follows ionization).

At higher temperature (40 °C), the *1,4-product* dominates — it's the *thermodynamic product*. The 1,4-product is more substituted (an internal alkene with a longer chain) and therefore more stable. At higher temperature, the system has enough energy to reverse the 1,2-addition and find its way to the lower-energy 1,4-product. This is one of the cleanest examples of *kinetic vs. thermodynamic control*.

This phenomenon — kinetic product at low T, thermodynamic product at high T — recurs in many reactions throughout organic chemistry. It's a useful lever to know when planning syntheses.

## The Diels–Alder reaction

The Diels–Alder reaction couples a *diene* (the four-carbon piece) with a *dienophile* (typically an alkene, often with electron-withdrawing groups like esters, ketones, nitriles, or nitro groups attached). The two pieces come together to form a six-membered ring with two new σ bonds and one new π bond.

The reaction is *concerted* — all the bonds break and form in a single step. There's no carbocation intermediate, no carbanion, no radical. The transition state has six π electrons rearranging at once.

Several geometric and electronic constraints make the reaction work:

**The diene must be in the s-cis conformation.** Conjugated dienes can rotate around their central C2–C3 single bond. The two extreme conformations are *s-cis* (the two double bonds on the same side) and *s-trans* (on opposite sides). The s-trans is more stable but only the s-cis can react in a Diels–Alder, because the geometry of the transition state requires the diene's two ends to point at the dienophile simultaneously.

**The dienophile is best electron-poor.** A simple alkene like ethylene is a poor dienophile — the reaction is slow. An alkene with one or more electron-withdrawing groups (cyano, ester, nitro, ketone) is a good dienophile. The electron-withdrawing groups lower the energy of the dienophile's LUMO, which improves the orbital overlap with the diene's HOMO in the transition state.

**Stereochemistry is controlled by the geometry of the transition state.** Substituents on the diene that are cis at the start end up cis in the product; trans stay trans. Similarly for the dienophile. This *retention of stereochemistry* is one of the most useful features of the reaction — you can predict the product's stereochemistry from the reactants'.

**The endo rule.** When there's an electron-withdrawing group on the dienophile, the transition state preferentially has that group pointing inward (toward the diene) rather than outward. This is the "endo rule." It gives a specific stereochemistry that's often opposite to what you'd predict on simple steric grounds. The reason is electronic: in the endo transition state, secondary orbital overlap between the diene π system and the dienophile's electron-withdrawing group provides additional stabilization.

The Diels–Alder reaction is a concerted *pericyclic* reaction — the topic of Chapter 30. We'll see there how molecular orbital theory predicts the precise stereochemistry and selectivity. For now, the key idea is that conjugation makes the reaction possible: an isolated diene without conjugation wouldn't do it, because the geometry can't deliver both double bonds to the dienophile simultaneously.

## Polymers from conjugated dienes

Industrial polymerization of conjugated dienes gives the synthetic rubbers that replaced natural rubber in the 20th century.

- *Polybutadiene* (from 1,3-butadiene): used in tires and other rubber products.
- *Polychloroprene* (from chloroprene, 2-chloro-1,3-butadiene): trade name *Neoprene*. Used for wetsuits and chemical-resistant gloves.
- *Polyisoprene* (from 2-methyl-1,3-butadiene): synthetic version of natural rubber, which is also polyisoprene (with a specific stereochemistry — all-cis).

The polymers are made by 1,4-addition of one diene to the next, building chains that retain a double bond in each repeating unit. The remaining double bonds give the polymers their elasticity (they can be vulcanized — cross-linked with sulfur — to make them retain their shape).

Industrial production of these synthetic rubbers is in the millions of tons per year.

## UV–visible spectroscopy

Conjugated systems absorb light at longer wavelengths than isolated double bonds. The reason is in the molecular orbitals: as a π system extends, the energy gap between HOMO and LUMO decreases, and the wavelength of light needed to promote an electron from HOMO to LUMO increases.

For an isolated alkene, the HOMO–LUMO gap corresponds to ultraviolet light at about 170 nm — too short for most spectrometers and human eyes. For 1,3-butadiene, the gap shifts to about 217 nm. For 1,3,5-hexatriene, about 258 nm. For β-carotene (a polyene with eleven conjugated double bonds), the absorption is at 466 nm — visible light, and the molecule appears orange because it absorbs blue-green and transmits the rest.

This is why long-conjugated compounds are colored. Indigo (the dye), chlorophyll (the green pigment of plants), retinal (the chromophore of vision), porphyrins (in hemoglobin and cytochromes), and the carotenoids (orange of carrots, red of tomatoes, pink of flamingos) all have extended π systems that bring their absorptions into the visible.

UV–vis spectroscopy quantifies this. A solution of a chromophore in a clear solvent is irradiated with UV/visible light, and the absorption is measured as a function of wavelength. The output is a plot of absorbance vs. wavelength (or absorbance vs. wavenumber, similar to IR but at much higher energies).

The Beer–Lambert law:

$$A = \epsilon \cdot c \cdot l$$

A = absorbance (unitless), ε = molar extinction coefficient (units of L · mol⁻¹ · cm⁻¹), c = concentration (mol/L), l = path length (cm). For a typical chromophore, ε is in the range of 10² to 10⁵.

The peaks in a UV spectrum correspond to electronic transitions. The position (λ_max, the wavelength of maximum absorption) tells you about the chromophore. The intensity (ε at λ_max) tells you about the transition's allowed/forbidden character. The width of the peak gives information about the molecular environment.

UV–vis is most useful for:
- Detecting and identifying conjugated systems (especially extended ones).
- Measuring concentration of compounds with known ε at known λ_max.
- Following reaction kinetics by monitoring absorption changes.

It's less useful for:
- Distinguishing structural isomers without conjugated systems.
- Quantifying low-concentration analytes (NMR or MS is usually better).

## Reading a UV spectrum

A simple UV spectrum has one or two main bands. The position of each band, in nanometers, tells you something about the chromophore. Some characteristic wavelength ranges:

| Chromophore | λ_max (nm) | ε |
|---|---|---|
| Isolated alkene C=C | 170 | 10⁴ |
| Isolated ketone C=O | 280 (n→π*) | 15 |
| Conjugated diene | 220 | 10⁴ |
| Conjugated triene | 260 | 10⁴ |
| α,β-unsaturated ketone | 220–260 | 10⁴ |
| Benzene | 254 (with vibrational fine structure) | 200 |
| Naphthalene | 286 | 9000 |
| Anthracene | 375 | 8500 |
| β-carotene | 466 | 1.4×10⁵ |

The Woodward–Fieser rules let you estimate λ_max for substituted dienes and ketones based on the substituents:

- Base value for acyclic conjugated diene: 217 nm
- Each additional alkyl substituent: +5 nm
- Each additional double bond extending conjugation: +30 nm

For a complex molecule with multiple substituents, you add the increments to the base value to predict λ_max within ~10 nm of the experimental value.

## Allylic systems and stability

Briefly: allylic systems — anything next to a double bond — are reactive in distinctive ways. The allylic carbocation, allylic radical, and allylic anion all benefit from resonance delocalization across the adjacent double bond. The allylic C–H bond is weaker than other C–H bonds because the resulting radical is resonance-stabilized.

This is why allylic bromination (with NBS, Chapter 10) is selective: the radical chemistry preferentially attacks the weakest C–H bond, which is the allylic one. It's also why allylic substrates are unusually reactive in SN1 reactions — the resulting cation is stabilized.

Benzylic systems work similarly, with stabilization from the aromatic ring. We'll see them in Chapters 15 and 16.

↳ **Dig Deeper — Why endo selectivity in Diels–Alder is electronic, not steric**

> The endo rule predicts that Diels–Alder reactions with electron-poor dienophiles preferentially place the electron-withdrawing group on the same face of the diene as the developing C–C bond — even though steric arguments would predict the opposite. Walk through the molecular orbital explanation. Cover: the role of secondary orbital interactions, why the LUMO of the dienophile interacts with the diene HOMO not just at the reacting positions but also at the ene-substituent positions, and why this stabilization disappears in the exo transition state. Use a maleic anhydride + cyclopentadiene reaction as your example.

**What to do with the output:** Compare against any pericyclic reactions textbook (Fleming's *Frontier Orbitals and Organic Chemical Reactions* is the classic reference). Verify Claude correctly identifies the secondary orbital overlap argument as distinct from primary bond formation.

## What this chapter does

Conjugation is the alignment of multiple π systems through alternating single and double bonds, with the result that π electrons spread out (delocalize) over more atoms. The consequences:

- Conjugated systems are more stable than non-conjugated ones (about 15 kJ/mol per additional conjugation).
- The single bond between two double bonds is shorter and stiffer than a typical single bond.
- Conjugated dienes undergo both 1,2- and 1,4-addition with electrophiles, with the ratio determined by kinetic vs. thermodynamic control.
- Conjugated dienes participate in [4+2] cycloadditions with dienophiles (the Diels–Alder reaction), giving cyclohexenes with predictable stereochemistry.
- The π electrons absorb UV (or sometimes visible) light, with longer conjugation shifting the absorption to longer wavelengths.
- Industrial polymerization of conjugated dienes gives synthetic rubbers.

UV–vis spectroscopy detects extended π systems and measures their absorption maxima. Beer's law lets you quantify concentrations. The Woodward–Fieser rules predict λ_max from substituent effects.

The Diels–Alder reaction, perhaps the most synthetically useful conjugate-diene chemistry, gets its full molecular orbital treatment in Chapter 30 along with other pericyclic reactions. The next chapter (15) introduces benzene and aromaticity — the ultimate conjugated system, with six π electrons in a stable cyclic arrangement.

---

*Source for all data, examples, and historical references: OpenStax* Organic Chemistry*, Chapter 14, modules m00170 through m00179.*
---

## LLM Exercise — Chapter 14: Conjugated Compounds and UV Spectroscopy (Synthesize a Target Molecule Project)

**Project:** Synthesize a Target Molecule.
**What you're building this chapter:** identify conjugated systems in your target; predict UV absorption; check for Diels-Alder opportunities.
**Tool:** **Claude Project**.

---

**The Prompt:**

```
Chapter 14 of my Synthesis project. Chapter 14 taught: conjugation
(alternating single and double bonds, sharing p-orbital electrons);
resonance contributors; 1,2- vs. 1,4-addition to dienes (kinetic
vs. thermodynamic product); the Diels-Alder reaction (cycloaddition
of a diene and dienophile, forming a cyclohexene with stereo-
specific outcomes); UV-Vis absorption depends on conjugation
length (more conjugation → longer wavelength); chromophores.

Write the brief's "Conjugation and Diels-Alder" section in 300–500
words.

1. **Identify conjugated systems in your target.** Look for:
   - Alternating C=C bonds (dienes, polyenes).
   - C=C conjugated with C=O (alpha,beta-unsaturated carbonyls).
   - Aromatic rings (covered separately in Ch 15-16).
   - C=C conjugated with N, O lone pairs (in some heterocycles).

2. **Predict UV-Vis absorption.** For each conjugated system,
   estimate λmax. Rough guidance:
   - Isolated C=C: ~170-200 nm (in UV, may not affect color).
   - Conjugated diene: ~210-260 nm.
   - Trienes: ~250-300 nm.
   - Aromatic rings: ~260-280 nm with weak absorption (forbidden);
     plus stronger absorption at higher energy.
   - Conjugated carbonyl: ~210-260 nm (n→π*).
   - Extended conjugation (5+ conjugated bonds): can extend into
     visible (>400 nm), giving the compound a color.

3. **Color implication.** If λmax > ~400 nm, the compound absorbs
   visible light and appears colored. The complementary color is
   what you SEE. For example, β-carotene (11 conjugated double
   bonds) absorbs blue/green light and appears orange-red.

4. **Diels-Alder opportunity.** Does your target's structure
   contain a 6-membered ring with a particular substitution pattern
   that could be assembled by Diels-Alder? Specifically:
   - A ring with a C=C bond and two substituents at the right
     positions.
   - Stereochemistry that fits the Diels-Alder's endo preference
     (the bulky groups end up on the same face).
   If yes, propose the diene and dienophile starting materials.

5. **Add to the retrosynthesis.** If Diels-Alder fits, this is
   often a powerful disconnection — it builds a 6-membered ring
   and two new C-C bonds in one step, with controlled stereo.

End with: which side of the molecule is the dienophile and which
is the diene? (The dienophile is typically electron-poor; the
diene must adopt the s-cis conformation.)
```

---

**What this produces:** A 300–500 word section. If a Diels-Alder fits, this is one of the most powerful disconnections in the synthesis.

**How to adapt this prompt:**

- *For your own project:* If no diene system is apparent, that's fine. Many syntheses don't use Diels-Alder.
- *For ChatGPT / Gemini:* Works as written.
- *For Claude Code:* Optional for UV-Vis prediction.
- *For a Claude Project:* Append.

**Connection to previous chapters:** Ch 6's retrosynthesis logic; Ch 7-8's alkene chemistry; Ch 14 adds the cycloaddition power tool.

**Preview of next chapter:** Chapter 15 covers benzene and aromaticity. Most drug targets have aromatic rings. You'll analyze each aromatic ring's properties and verify Hückel's rule.


---

## AI Wayback Machine

**Otto Diels** was co-discovered the Diels-Alder reaction in 1928 with his student Kurt Alder — the cleanest conjugated-diene synthesis. Nobel 1950.

**Run this:**

```
Who is Otto Diels, and how does their work connect to conjugated compounds we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about their career or ideas.
```

→ Search **"Otto Diels"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to walk through one of Otto Diels's key experiments or syntheses in detail.
- Add a constraint: "Answer including criticisms or limits of Otto Diels's framework."

What changes? What gets better? What gets worse?
