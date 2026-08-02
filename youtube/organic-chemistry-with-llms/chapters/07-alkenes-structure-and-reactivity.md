# Chapter 7 — Alkenes: Structure and Reactivity

*The double bond is where carbon chemistry stops being inert. Almost every reaction in the rest of this book starts at a place where two carbons share four electrons instead of two.*

The petrochemical industry produces 215 million metric tons of ethylene every year — more than any other industrial organic chemical. From it we make polyethylene (the plastic of milk jugs and grocery bags), ethylene glycol (antifreeze), ethylene oxide (a feedstock for surfactants and ethanolamines), and dozens of other molecules. The reason ethylene is the front-end molecule for so much chemistry is that the C=C double bond is reactive. The π electrons are loosely held, accessible to electrophiles, and ready to enter into all sorts of addition reactions. By contrast, the C–C single bonds in ethane are inert. Ethane is a fuel; ethylene is a starting material.

This chapter is about alkenes — the carbon compounds with one or more C=C double bonds. We covered the bonding briefly in Chapter 1: each carbon is sp² hybridized, with three σ bonds in a plane and one p orbital perpendicular to that plane; two adjacent sp² carbons share a σ bond plus a π bond, the latter from sideways overlap of their two p orbitals. The geometry is planar, the bond angles around each carbon are 120°, and there's no rotation around the C=C bond at room temperature — the π bond would have to break for one carbon to twist relative to the other.

The lack of rotation around the double bond is what gives alkenes a new kind of stereoisomerism: cis–trans isomerism, or in the IUPAC system, E/Z isomerism. Once again, the same atoms in the same connectivity can give two distinct compounds depending on three-dimensional arrangement. And once again, those arrangements differ in stability — and that difference matters when we look at reactions that could go to either isomer.

This chapter covers the structure, naming, stability, and electronic character of alkenes. The next chapter (Chapter 8) covers their reactions.

## Naming alkenes

The IUPAC suffix for an alkene is *-ene*. The naming rules are extensions of the alkane rules:

1. Find the longest continuous chain containing both carbons of the double bond. That's the parent.
2. Number the chain from the end nearest the double bond to give the double bond the lowest possible locant.
3. Indicate the position of the double bond with the locant of its first carbon. So 2-butene means the double bond is between C2 and C3 of butane.
4. List substituents alphabetically with their locants, as in alkane naming.

Some examples:
- CH₂=CH–CH₂–CH₃ → 1-butene (double bond between C1 and C2)
- CH₃–CH=CH–CH₃ → 2-butene
- (CH₃)₂C=CHCH₃ → 2-methyl-2-butene

For cycloalkenes, the carbons of the double bond are always numbered C1 and C2, and you don't need a locant for the double bond:
- cyclohexene
- 3-methylcyclopentene (methyl at C3, double bond between C1 and C2)

A few common names are firmly entrenched and accepted by IUPAC:
- Ethylene = ethene
- Propylene = propene
- Isobutylene = 2-methylpropene
- Vinyl = H₂C=CH–
- Allyl = H₂C=CH–CH₂–

## Degree of unsaturation

A quick diagnostic. An alkane has the formula CₙH₂ₙ₊₂. Each C=C double bond reduces the H count by two; each ring also reduces it by two. So:

$$\text{degrees of unsaturation} = \frac{(2n + 2) - H}{2}$$

For C₆H₁₂: alkane formula would be C₆H₁₄. Difference is 2 H; degrees of unsaturation = 1. The molecule has either one ring or one double bond. Could be cyclohexane, cyclopentane with a methyl, hex-1-ene, hex-2-ene, etc.

For C₆H₆ (benzene): difference from C₆H₁₄ is 8 H, so degrees of unsaturation = 4. Benzene has three double bonds and one ring — total of four degrees.

When a heteroatom is involved:
- Halogens count as if they were hydrogens (subtract one for each).
- Oxygen and other divalent atoms: ignore.
- Nitrogen and other trivalent atoms: add one to the H count for each.

Degrees of unsaturation give you a quick ceiling on how many rings + double bonds + triple bonds (counts as 2) the molecule has, before you even draw the structure. Useful when working from a molecular formula given by mass spectrometry.

## Cis–trans isomerism in alkenes

Take 2-butene, CH₃CH=CHCH₃. The two methyl groups can be on the same side of the double bond (cis) or on opposite sides (trans). These are different compounds.

*cis*-2-butene boils at 3.7 °C and has a heat of formation of −7 kJ/mol.
*trans*-2-butene boils at 0.9 °C and has a heat of formation of −11 kJ/mol.

The trans isomer is more stable than the cis isomer by about 4 kJ/mol. The reason is steric: in the cis isomer, the two methyl groups are close enough to bump into each other; in the trans isomer, they're as far apart as possible.

For this isomerism to exist, each carbon of the double bond must have two *different* substituents. If either carbon has two identical groups (like the H₂C= of 1-butene, or the (CH₃)₂C= of 2-methyl-2-butene with one C bearing two methyls), there's no cis or trans — both arrangements give the same molecule.

The cis–trans nomenclature works fine for disubstituted alkenes but breaks down when the two carbons have more than one different substituent. For those cases, IUPAC uses the *E/Z* system, which assigns priorities to the substituents on each carbon and labels the alkene based on whether the highest-priority groups are on the same side (Z, from German *zusammen*, "together") or on opposite sides (E, from German *entgegen*, "opposite").

The priority rules are the Cahn–Ingold–Prelog rules from Chapter 5. For each carbon of the double bond:

1. Identify the two substituents on that carbon.
2. Rank them by atomic number — higher atomic number = higher priority.
3. If the first atoms tie, look at the next atoms outward (and the next, and so on) until a difference is found.

Once you have the higher-priority substituent on each carbon, look at the molecule:

- If both higher-priority substituents are on the same side of the double bond → Z.
- If on opposite sides → E.

So *cis*-2-butene = (Z)-2-butene; *trans*-2-butene = (E)-2-butene. For more complex cases where cis/trans is ambiguous, E/Z is unambiguous.

## Why alkenes have stability differences

The 4 kJ/mol stability gap between *cis*- and *trans*-2-butene is a clean steric story. For other alkene comparisons, the explanation often involves *hyperconjugation* — the stabilization of a double bond by adjacent C–H σ bonds.

Hyperconjugation works like this: a σ-bonding orbital from a C–H bond on a carbon adjacent to the alkene can donate some of its electron density into the antibonding π* orbital of the C=C. This donation is small per C–H bond but additive — more adjacent C–H bonds, more hyperconjugation, more stabilization. So the alkene with the most alkyl substituents (which contribute the most adjacent C–H bonds) is the most stable.

Numerical version: the relative stability of differently substituted alkenes (estimated from heats of hydrogenation) goes:

- tetrasubstituted (R₂C=CR₂) > 
- trisubstituted (R₂C=CHR) > 
- disubstituted, geminal (R₂C=CH₂) ≈ 
- disubstituted, trans (RHC=CHR, trans) > 
- disubstituted, cis (RHC=CHR, cis) > 
- monosubstituted (RHC=CH₂) > 
- ethylene (H₂C=CH₂)

Each step up the substitution ladder is worth about 10 kJ/mol of stability.

This stability ranking is the basis for *Zaitsev's rule* in elimination reactions (Chapter 11) — the more substituted alkene is the major product of E1 and E2 because it's the lower-energy outcome.

It's also why some isomerization reactions go where they do. If you treat an alkene with a small amount of strong acid, the proton can add to one carbon to give a carbocation, then leave from a different position, giving a different alkene. The thermodynamic product of this isomerization is always the most substituted alkene.

## The π bond and what makes it reactive

A C=C double bond is one σ bond plus one π bond. The σ bond is strong (the same as a C–C single bond, about 350 kJ/mol). The π bond is weaker — about 270 kJ/mol — because sideways overlap of two p orbitals is less efficient than head-on overlap of sp³ hybrids.

The π electrons are also less tightly held than σ electrons. They sit in two lobes above and below the molecular plane, where they're physically further from the nuclei (compared to σ electrons that sit on the line between nuclei). This makes the π electrons available — accessible to electrophiles that can pull them away.

The whole reactivity of alkenes traces back to this. The C=C bond is a *nucleophile* — the π electrons can attack a positive center. When an electrophile (like H⁺ from a strong acid, or Br⁺ from Br₂, or any other electron-poor reagent) approaches an alkene, the π electrons migrate to form a new bond to the electrophile. This breaks the π bond. One of the carbons ends up with the electrophile attached; the other ends up with an empty orbital — a carbocation.

That's the first step of essentially every polar addition to an alkene:

$$\text{C=C} + \text{E}^+ \longrightarrow \text{C(-E)–C}^+$$

The carbocation then gets attacked by a nucleophile (the conjugate base of the acid, or whatever else is around) to complete the addition:

$$\text{C(-E)–C}^+ + \text{Nu}^- \longrightarrow \text{C(-E)–C(-Nu)}$$

Net result: the alkene has added E and Nu across the double bond. We'll see this pattern over and over in Chapter 8: HBr addition, water addition, halogen addition, and several others all follow this two-step polar mechanism.

## Markovnikov's rule

When an unsymmetrical electrophile adds to an unsymmetrical alkene, two regiochemical outcomes are possible. Take HBr + propene (CH₃CH=CH₂). The H⁺ can add to either C1 or C2; correspondingly, the Br⁻ adds to the other carbon. The two possible products are:

- 2-bromopropane (CH₃CHBrCH₃) — H on C1, Br on C2
- 1-bromopropane (CH₃CH₂CH₂Br) — H on C2, Br on C1

Empirically, the major product is 2-bromopropane. In 1869 Vladimir Markovnikov stated the empirical rule: *in the addition of HX to an alkene, the H attaches to the carbon with more H's already, and the X attaches to the carbon with fewer H's.* In 21st-century language, the H goes to the less substituted carbon and the X goes to the more substituted carbon.

The mechanism explains why. The first step is H⁺ adding to one of the carbons of the double bond, generating a carbocation. There are two possible carbocations:

- Adding H to C1 (the less substituted carbon) gives a secondary carbocation on C2: CH₃CH⁺CH₃.
- Adding H to C2 gives a primary carbocation on C1: ⁺CH₂CH₂CH₃.

Secondary carbocations are more stable than primary ones (roughly 80 kJ/mol more stable, due to hyperconjugation). The Hammond postulate then connects this stability difference to the activation energy: the path through the more stable cation has a lower transition-state energy, so it's faster. The major product comes from the more stable carbocation, which in this case puts the H on the less substituted carbon (giving the more substituted cation).

Markovnikov's rule, restated: *electrophiles add to alkenes via the carbocation that is most stable.* The empirical rule about which carbon the H goes to is just a consequence of that, applied to the H+/X- case.

This generalization is more useful than Markovnikov's original statement because it works for cases the original rule doesn't cover cleanly — for instance, additions to alkenes where a more substituted cation isn't simply "the carbon with fewer H's" but is determined by other factors (resonance stabilization in benzylic or allylic positions, for example).

## Resonance-stabilized carbocations

Some additions to alkenes give carbocation intermediates whose stability comes not just from substitution pattern but from resonance.

A *benzylic carbocation* (next to a benzene ring) is stabilized by resonance — the positive charge can delocalize into the ring. So additions of H⁺ to a styrene-type alkene (PhCH=CH₂) give the benzylic carbocation (PhCH⁺CH₃) preferentially, even though it's structurally only a secondary cation. Resonance puts it on par with a tertiary alkyl cation.

An *allylic carbocation* (next to a C=C) is similarly stabilized. The positive charge can delocalize through the adjacent π system. So additions to dienes (like 1,3-butadiene) give allylic intermediates with characteristic regiochemistry.

These resonance-stabilized cases come up in Chapter 14 (conjugated dienes), Chapter 16 (electrophilic aromatic substitution), and elsewhere. The general principle is the same: the cation that's most stable wins.

↳ **Dig Deeper — Why hyperconjugation is real and how it differs from resonance**

> Both hyperconjugation and resonance stabilize carbocations and alkenes. But they're not the same — hyperconjugation uses σ orbitals donating into empty p or π* orbitals, while resonance uses π orbitals or lone pairs delocalizing across formal double bonds. Explain the distinction in terms of orbital types involved, the energy of stabilization (which is bigger?), and how to spot which is operating in a given example. Cover the case of *tert*-butyl cation (hyperconjugation only) versus benzyl cation (resonance only) versus allyl cation (resonance only).

**What to do with the output:** Verify Claude correctly states that hyperconjugation involves σ orbitals while resonance involves π or lone-pair orbitals. Sanity-check the relative energy contributions (resonance is typically larger than hyperconjugation per stabilizing interaction).

## The Hammond postulate, applied to alkene additions

The two-step polar addition mechanism — first form a carbocation, then capture it with a nucleophile — has its rate-determining step in the first step, where the cation is forming. The transition state for that step is endothermic (the cation is much higher in energy than the alkene + electrophile), so by Hammond's postulate, the transition state resembles the cation.

This means: anything that stabilizes the cation also stabilizes the transition state for forming the cation. Tertiary > secondary > primary cation stability translates directly into faster reactions for substrates that can form more stabilized cations. Allylic and benzylic positions are extra-fast for the same reason.

The same logic explains why Markovnikov's rule works: the path through the more stable cation has the lower transition-state energy.

## Industrial production of alkenes

Briefly, where do all those millions of tons of ethylene and propylene come from? They're produced by *steam cracking* — heating high-molecular-weight hydrocarbons (from petroleum or natural gas) to about 850 °C in the presence of steam. At those temperatures, the C–C bonds break homolytically (radical chemistry, not polar) and the resulting fragments lose H atoms to form double bonds. The product mix is a mixture of small alkenes — mostly ethylene, with propylene and butenes as significant secondary products.

Steam cracking is one of the highest-energy industrial processes in chemistry. The fraction of total petroleum consumption that goes through steam crackers is in the single-digit percent range, but it sits at the front end of an enormous downstream chemical industry. Almost every plastic, every detergent, every alcohol-based industrial chemical traces back to ethylene or propylene from a steam cracker.

The biological version of alkene synthesis is fundamentally different — enzymatic eliminations from oxygenated precursors (alcohols, esters), often via E1cB mechanisms. The relevant enzymes are dehydratases. We saw an example in Chapter 11: fatty acid biosynthesis runs an E1cB to introduce double bonds at specific positions. We'll see more in Chapter 27.

## What this chapter does

The C=C double bond is one σ bond plus one π bond. The π bond is weaker and the π electrons are less tightly held, which makes alkenes nucleophilic — accessible to electrophiles. The geometry is planar, with 120° bond angles around each sp² carbon, and rotation around the bond is locked at room temperature.

Cis–trans isomerism (or E/Z, in the IUPAC system) exists because of that locked rotation. The cis isomer is generally less stable than the trans because of steric strain between substituents on the same side. The general stability ranking (tetrasubstituted > trisubstituted > disubstituted > monosubstituted > unsubstituted) reflects hyperconjugation from adjacent C–H bonds.

When an alkene reacts with an electrophile, the first step is electrophile addition to one carbon of the double bond, with the π electrons forming the new bond. This generates a carbocation on the other carbon. The cation that forms is the most stable one available — substitution-stabilized, or resonance-stabilized via allyl/benzyl groups. In the second step, a nucleophile captures the carbocation. The net result is addition across the double bond, with regiochemistry controlled by carbocation stability (Markovnikov's rule).

Almost every reaction in Chapter 8 follows this two-step pattern. The variations come from which electrophile is used, what nucleophile captures the cation, and what stereochemistry results from the geometry of the steps.

---

*Source for all data, examples, and historical references: OpenStax* Organic Chemistry*, Chapter 7, modules m00062 through m00073.*
---

## LLM Exercise — Chapter 7: Alkenes — Structure and Reactivity (Synthesize a Target Molecule Project)

**Project:** Synthesize a Target Molecule.
**What you're building this chapter:** alkene analysis — does the target have alkenes? Do intermediates? Stability rankings, E/Z assignments.
**Tool:** **Claude Project**.

---

**The Prompt:**

```
Chapter 7 of my Synthesis project. Prior sections in this Claude
Project. Chapter 7 taught: alkene structure (planar sp² carbons,
~120° bond angles); cis/trans (E/Z) isomerism using CIP priority
rules; alkene stability (more-substituted alkenes are more stable
— Zaitsev's rule for elimination products); carbocation stability
(3° > 2° > 1°, due to hyperconjugation and inductive effects).

Write the brief's "Alkene Analysis" section in 300–500 words.

1. **Are there alkenes in the target?** If yes, identify each
   one. For each: assign E/Z, identify the substituents, note
   whether it's terminal, monosubstituted, disubstituted,
   trisubstituted, or tetrasubstituted.

2. **If no alkenes in target:** identify alkene intermediates
   likely to appear in a synthesis. Examples:
   - A precursor that gets hydrogenated to a saturated chain.
   - A Wittig precursor that establishes a C=C bond stereo-
     selectively.
   - A diene used in a Diels-Alder.

3. **Stability ranking.** Whichever alkenes are present in target
   or synthesis: rank by stability using substitution pattern.
   More substituted = more stable. Useful for predicting which
   elimination product dominates (Zaitsev) and which alkene survives
   thermodynamic conditions.

4. **Carbocation intermediates.** Many alkene reactions (Markovnikov
   addition of HX) proceed via carbocations. For your synthesis,
   are any reactions likely to generate carbocations? If yes:
   - Will the carbocation be 1°, 2°, or 3°?
   - Are rearrangements (hydride shift, methyl shift) likely?
   - What's the regiochemistry implication?

5. **The geometric consequence.** Cis (Z) alkenes introduce kinks
   into chains (consequential in fatty acids, Ch 27). Trans (E)
   alkenes preserve roughly linear chain geometry. If your target
   has alkenes, this often matters for biological activity or
   crystal packing.

End with one synthesis-design implication: how will the alkene
geometry be controlled? Stereoselective options include:
- Wittig (stereoselective for Z with stabilized ylide; for E with
  non-stabilized).
- Hydroboration + Suzuki (clean stereochemistry).
- Catalyzed metathesis (case-dependent).
```

---

**What this produces:** A 300–500 word Alkene Analysis. If your target has alkenes, the stereochemistry-control discussion previews real synthesis challenges.

**How to adapt this prompt:**

- *For your own project:* If your target is fully saturated, this section is short but still useful as preview for alkene-intermediate steps.
- *For ChatGPT / Gemini:* Works as written.
- *For Claude Code:* Optional.
- *For a Claude Project:* Append.

**Connection to previous chapters:** Ch 5's stereochemistry now extends to double-bond geometry (E/Z); Ch 6's reaction-class framework labels alkene additions.

**Preview of next chapter:** Chapter 8 covers alkene reactions. You'll propose a synthetic step that uses an alkene reaction (hydrogenation, Markovnikov, hydroboration, etc.) to install a functional group present in your target.


---

## AI Wayback Machine

**Vladimir Markovnikov** was Russian chemist who established the rule bearing his name in 1870 — predicting regioselectivity in alkene addition reactions.

**Run this:**

```
Who is Vladimir Markovnikov, and how does their work connect to alkene reactivity we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about their career or ideas.
```

→ Search **"Vladimir Markovnikov"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to walk through one of Vladimir Markovnikov's key experiments or syntheses in detail.
- Add a constraint: "Answer including criticisms or limits of Vladimir Markovnikov's framework."

What changes? What gets better? What gets worse?
