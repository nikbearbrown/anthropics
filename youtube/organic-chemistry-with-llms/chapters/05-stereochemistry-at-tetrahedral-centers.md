# Chapter 5 — Stereochemistry at Tetrahedral Centers

*Two molecules can have the exact same connectivity, the exact same atoms in the exact same bonds, and still be different compounds with different chemistry. The difference is which way they point in space.*

In 1848 Louis Pasteur was looking through a microscope at a sample of crystals he'd grown from a tartrate salt, and he noticed something. Half the crystals were one shape, half were another, and the two shapes were mirror images of each other. He spent days separating the crystals by hand into two piles using tweezers. When he dissolved each pile in water and shone polarized light through, one solution rotated the light to the right, the other to the left. Same molecule, by every chemical analysis available at the time. Different optical behavior, simply because the molecules came in two mirror-image versions.

Pasteur didn't know about tetrahedral carbon — that wouldn't be proposed by van't Hoff and Le Bel until 1874. But he knew he'd found something fundamental: the molecules of life come in handed forms, and the handedness matters.

Today we know exactly what was going on. Tartaric acid has two carbon atoms with four different substituents each. Each of those carbons, like methane, is tetrahedral. But unlike methane, where all four substituents are identical (H), a carbon with four different substituents has a three-dimensional arrangement that cannot be superimposed on its mirror image. The two arrangements are non-identical. They are *enantiomers* — chemistry's word for "mirror-image stereoisomers."

This chapter is about how to spot these chiral centers, how to name the two configurations unambiguously, how their physical properties differ, and how to keep track of multiple chiral centers at once. The reason this matters is biological: almost every drug molecule, every amino acid, every sugar, every neurotransmitter has chiral centers, and the body is exquisitely sensitive to which configuration you give it. Thalidomide is the classic example — one enantiomer of the drug treats morning sickness, the other causes birth defects. The same atoms, connected the same way, with one carbon's four substituents pointing in mirror-image directions, and the result is the difference between a medicine and a tragedy.

## Chirality, in one sentence

A molecule is *chiral* if it cannot be superimposed on its mirror image. Otherwise it is *achiral*.

That's the definition. The rest of this chapter is operational — how to tell whether a given molecule meets it.

The word "chiral" comes from the Greek *cheir*, meaning hand. Your hands are chiral: left and right are mirror images of each other, but no rotation can superimpose one on the other. (Try it. The thumbs always end up pointing opposite ways.) Most organic molecules with chiral centers behave the same way: two mirror-image versions exist, and rotating one cannot turn it into the other.

The most common cause of chirality in organic molecules is a tetrahedral carbon with four different substituents. We call such a carbon a *chirality center* (also: *stereocenter*, *asymmetric center*, *stereogenic center* — the terms are interchangeable). When a carbon has four different things attached, the four substituents can be arranged in two distinct three-dimensional ways. Those two arrangements are mirror images. The molecule containing one arrangement is the enantiomer of the molecule containing the other.

Lactic acid, CH₃CH(OH)CO₂H, is a clean example. The central carbon has four substituents: H, OH, CH₃, and CO₂H. All four are different. So the central carbon is a chirality center, and lactic acid exists as two enantiomers.

A molecule with a *plane of symmetry* — an internal mirror plane that maps the molecule onto itself — is achiral, even if it has carbons that look like they might be stereocenters. Methane (with four identical H's) has many planes of symmetry; it's achiral. Bromochloromethane (BrCH₂Cl) has one plane of symmetry; it's achiral. Lactic acid has none; it's chiral.

A diagnostic shortcut: to be a chirality center, a carbon must have *four different substituents*. CH₂, CH₃, C=O, C=C, and C≡C carbons cannot be chirality centers because they have at least two identical substituents (or fewer than four substituents total). When scanning a structure for chirality centers, look for sp³ carbons with four bonds, then check whether the four attached groups are different.

"Different" sometimes requires looking far down the chain. In 5-bromodecane, the central carbon (C5) has: −H, −Br, −butyl chain (4 carbons), and −pentyl chain (5 carbons). The butyl and pentyl groups differ only in length, but they *are* different — so C5 is a chirality center. To be sure, you have to walk along each substituent until you find a difference.

## The R/S system: how to name a chirality center

Once you've identified a chirality center, you need a way to describe which of the two possible configurations a particular molecule has. The system used universally is the Cahn–Ingold–Prelog (CIP) priority rules, which assign each chirality center either the label *R* (Latin *rectus*, right) or *S* (Latin *sinister*, left).

The rules:

**Rule 1.** *Rank the four substituents on the chirality center by atomic number.* The atom with higher atomic number gets higher priority. Br > Cl > S > P > O > N > C > H.

**Rule 2.** *If two substituents have the same first atom, look at the next atoms outward.* For −CH₂CH₃ vs. −CH₂OH, both start with C, so go to the next sphere. The first finds (H, H, C); the second finds (H, H, O). O > C, so −CH₂OH has higher priority.

**Rule 3.** *Treat double and triple bonds as duplicated single bonds.* A C=O is treated as a C bonded to two O's, and an O bonded to two C's. A C=C is treated as a C bonded to two C's on each side.

**Rule 4.** *Once you have all four priorities (a > b > c > d), orient the molecule with the lowest priority (d) pointing away from you.* Then trace the remaining three priorities a → b → c. If the trace goes clockwise, the configuration is R. Counterclockwise, S.

A worked case. (R)-2-bromobutane. The central carbon (C2) has: H, Br, CH₃, CH₂CH₃. Priorities: Br (35) > CH₂CH₃ (C, but the next sphere has C beating H) > CH₃ (just C, then H's) > H (1). So a = Br, b = CH₂CH₃, c = CH₃, d = H. Orient the molecule with H pointing away. Trace Br → CH₂CH₃ → CH₃. If clockwise, it's R. Otherwise S.

The mnemonic is the same as a steering wheel — when you turn the wheel right (clockwise as you face it), the car turns right. Right-turn = R. Left-turn = S.

This system is universal and unambiguous. Every chirality center in every molecule can be assigned R or S using the same procedure. When chemists communicate about chiral molecules, they use these labels: (R)-thalidomide, (S)-naproxen, (2R, 3S)-tartaric acid.

## Optical activity: how chirality is measured

Pasteur's polarimeter experiment is the foundational tool for detecting chirality experimentally.

When ordinary (unpolarized) light passes through a *polarizer* — a special filter — only light vibrating in one plane gets through. The result is *plane-polarized light*. If you then pass plane-polarized light through a sample of pure water, nothing happens; the polarization plane stays where it was.

If you pass plane-polarized light through a solution of an *optically active* substance — like one enantiomer of a chiral molecule — the polarization plane rotates by some angle α. The amount of rotation depends on the concentration of the chiral substance, the path length, and the wavelength of light, plus a substance-specific constant called the *specific rotation* [α]:

$$[α] = \frac{α}{c \cdot l}$$

where α is the observed rotation in degrees, c is concentration in g/mL, and l is path length in dm. Specific rotation is a physical property of the substance, like density or melting point. Pure (R)-glyceraldehyde has [α] = +8.7°. Pure (S)-glyceraldehyde has [α] = −8.7°.

Two key points. First, the *direction* of rotation (+ for clockwise, − for counterclockwise, sometimes written *d*- and *l*-) is independent of the *configuration* (R or S). The R enantiomer of one molecule might rotate light clockwise; the R enantiomer of a different molecule might rotate counterclockwise. You can't predict the sign of rotation from the configuration label without measuring.

Second, a *racemic mixture* — a 50:50 mixture of the two enantiomers — has zero net rotation. The rotations from one enantiomer cancel out the rotations from the other. Racemic mixtures are common in synthetic chemistry; making non-racemic chiral compounds (asymmetric synthesis) is a major area of organic chemistry research.

## Diastereomers and meso compounds

Once you have more than one chirality center in a molecule, things get more interesting.

Consider a molecule with two chirality centers. Each can be R or S, giving four possibilities: (R, R), (R, S), (S, R), (S, S). The (R, R) and (S, S) molecules are mirror images of each other — they're enantiomers. The (R, S) and (S, R) molecules are also mirror images of each other — also enantiomers. But the (R, R) and (R, S) molecules are *not* mirror images of each other. They're stereoisomers (same connectivity, different 3D arrangement) but not enantiomers. We call this relationship *diastereomers*.

Diastereomers are physically and chemically different. They have different boiling points, different melting points, different specific rotations, often different reactivities. Enantiomers, in contrast, have identical physical properties except for the direction of optical rotation, and they react identically with achiral reagents. Diastereomers are easier to separate (different boiling points → distillation works), enantiomers are notoriously difficult.

Now a special case. Tartaric acid, HO₂C–CH(OH)–CH(OH)–CO₂H, has two chirality centers. Following the four-possibility logic, you'd expect four stereoisomers: (R, R), (S, S), (R, S), (S, R). Let's check.

(R, R) and (S, S) are mirror-image enantiomers. Both are chiral, both are optically active.

(R, S) and (S, R) — but wait. Tartaric acid has a special feature: the two ends of the molecule are identical (both are –CHOH–CO₂H). So the (R, S) molecule and the (S, R) molecule are the same molecule, just numbered from the other end. And that single molecule has an internal plane of symmetry: cut it across the middle bond, and one half is the mirror image of the other. *The molecule is its own mirror image.* It's achiral, despite having two chirality centers.

We call this special case a *meso* compound. A meso compound has chirality centers but is overall achiral because of internal symmetry. Meso-tartaric acid exists. It's optically inactive (does not rotate plane-polarized light) and its solutions are not separable into enantiomers because it doesn't have any.

So tartaric acid has only three stereoisomers, not four: (R, R), (S, S), and meso (which is the same molecule as both (R, S) and (S, R)). The (R, R) and (S, S) are enantiomers of each other; the meso is a diastereomer of each of them.

Internal symmetry is the diagnostic. Whenever a molecule has multiple chirality centers, check whether you can draw an internal mirror plane (or other symmetry element) that maps the molecule to itself. If yes, it's meso, regardless of how many R's and S's it contains.

## Cis–trans isomerism is a special case of diastereomerism

The cis–trans isomers of disubstituted cyclohexanes (Chapter 4) are diastereomers. So are the E/Z isomers of disubstituted alkenes (Chapter 7). All of these are stereoisomers that are not mirror images of each other.

For 1,2-dimethylcyclohexane: the cis and trans isomers are different compounds, with different boiling points, different melting points, different conformational preferences. Their molecules cannot be superimposed by any rotation in space. They are diastereomers — which is to say, they are stereoisomers that are not enantiomers.

The cis isomer is itself a meso compound (it has an internal mirror plane). The trans isomer is chiral and exists as two enantiomers, (R, R) and (S, S).

## Fischer projections

A Fischer projection is a flat drawing convention for showing chirality, used heavily in carbohydrate chemistry. The convention:

- Draw the carbon chain vertically, with the most-oxidized end at the top.
- Each chirality center is a cross — the horizontal bonds point toward you (out of the page), the vertical bonds point away from you (into the page).
- The configuration at each center is read from the cross.

For (R)-glyceraldehyde, the Fischer projection has CHO at top, CH₂OH at bottom, and the central chirality center with H on the left and OH on the right. The OH on the right of a Fischer projection (with the chain conventionally oriented) corresponds to the *D* configuration in carbohydrate nomenclature; on the left corresponds to *L*.

The D/L system is older than R/S and is still standard for sugars and amino acids. Almost all natural sugars are D-, almost all natural amino acids are L-. (Both are biological accidents — the alternative configurations could in principle support life equally well; the actual chemistry of life is just one of two possible solutions.)

## Prochirality

A molecule with one chirality center already in place can be *prochiral* — meaning it has a face or an atom that, if substituted in a particular way, would create a new chirality center.

A flat sp² carbon in a ketone has two faces. Reagent attacks on the two faces give different products if the molecule has other chirality centers nearby. The two faces are called the *Re* and *Si* faces, named by applying the CIP rules to the three substituents on the sp² carbon (and noting which way they go around).

A CH₂ group between two different groups (like the central carbon of CH₃CH(OH)CH₂CH₂CO₂H) has two H's. They look identical, but they aren't quite. If we replaced one with deuterium, we'd create a chirality center. The two H's are called *pro-R* and *pro-S*. Enzymes can distinguish them, and they often do — alcohol dehydrogenase, for example, removes only the pro-R hydrogen from ethanol.

This kind of subtle stereochemical distinction matters most when biology is involved. Enzymes are highly chiral environments and routinely make distinctions between prochiral atoms or faces. Most laboratory reagents are achiral and treat the two faces or pro-R/pro-S hydrogens equivalently.

↳ **Dig Deeper — Why almost all amino acids in biology are L**

> All proteinogenic amino acids in biology except glycine are L-configured (S in CIP terms, with one famous exception). Explain what the L-versus-D distinction means for amino acids, why life on Earth seems to have committed entirely to the L versions, and what the few known exceptions (D-amino acids in bacterial cell walls, some neurotransmitters) tell us about the relationship between chirality and biological function.

**What to do with the output:** Sanity-check Claude's claim about cysteine being the exception (it's labeled R despite being chemically L because of CIP priority rules with the SH group). Compare against any biochemistry textbook chapter on amino acid stereochemistry.

## Why this matters for drug chemistry

Almost every drug molecule with a chirality center is sold and prescribed as a single enantiomer, even though synthesis often produces racemic mixtures. The reason: the body is built out of chiral molecules (proteins from L-amino acids, sugars from D-glucose, lipids with specific stereochemistry), so drug binding sites are chiral environments. One enantiomer of a drug fits the binding site like a hand fits a glove; the other enantiomer is the wrong-handed glove on the same hand — wrong fit, wrong activity, sometimes wrong effect.

Examples to remember:

- *Thalidomide*. The S enantiomer is sedative and treats morning sickness; the R enantiomer is teratogenic. (The two enantiomers also interconvert in the body, complicating matters; but the original tragedy in the 1950s and 60s was largely a chirality story.)
- *Ibuprofen*. The S enantiomer is the active painkiller; the R enantiomer is essentially inactive. Ibuprofen is sold as the racemate because the body slowly converts R to S in vivo.
- *Naproxen*. Sold as pure S enantiomer; the R enantiomer causes liver damage.
- *L-DOPA*. Used for Parkinson's disease. The L enantiomer crosses the blood-brain barrier and is converted to dopamine by decarboxylation; the D enantiomer cannot.

When designing a synthesis of a chiral drug, controlling which enantiomer you produce — and ensuring you don't sell the wrong one as a contaminant — is one of the central problems in pharmaceutical chemistry. Modern asymmetric synthesis (using chiral catalysts, chiral starting materials, or enzymatic methods) is the answer; the field has grown enormously since Pasteur's tweezers.

## What this chapter does

A tetrahedral carbon with four different substituents is a chirality center. It exists in two non-superimposable mirror-image arrangements, called enantiomers. The two arrangements are labeled R and S using the Cahn–Ingold–Prelog rules, which rank substituents by atomic number and trace the priority order around the chirality center.

Enantiomers have identical physical properties (mp, bp, density) but rotate plane-polarized light in opposite directions. They react identically with achiral reagents and differently with chiral reagents — including, in particular, the chiral reagents that biology runs on.

Multiple chirality centers create more stereoisomers. Some pairs are enantiomers (full mirror image), some are diastereomers (different but not mirror image). Internal symmetry can collapse what looks like four stereoisomers down to three, with the symmetric one being a meso compound.

Pasteur with his tweezers separated tartrate enantiomers because of a rare crystallographic accident — the molecules formed enantiomerically pure crystals that you could see and pick apart. We can now distinguish enantiomers by polarimetry, by chiral chromatography, by NMR with chiral shift reagents, and by X-ray crystallography. The tools have changed; the underlying fact has not. Atoms in space matter. The molecule's geometry is not just about how it looks — it determines what it can do.

The next chapter shifts gears. Now that we have structure, conformation, and stereochemistry under control, we start thinking about reactions. The same geometric reasoning will reappear there immediately: transition states have shapes too, and stereochemistry of the starting material often determines stereochemistry of the product.

---

*Source for all data, examples, and historical references: OpenStax* Organic Chemistry*, Chapter 5, modules m00049 through m00061.*
---

## LLM Exercise — Chapter 5: Stereochemistry at Tetrahedral Centers (Synthesize a Target Molecule Project)

**Project:** Synthesize a Target Molecule.
**What you're building this chapter:** the stereochemistry analysis of your target — identify every stereocenter, assign R/S, and discuss the consequences for synthesis and bioactivity.
**Tool:** **Claude Project**.

---

**The Prompt:**

```
Chapter 5 of my Synthesis project. Prior sections in this Claude
Project. Chapter 5 taught: chirality (non-superimposable mirror
image); stereocenters (typically sp³ carbon with 4 different
substituents); R/S nomenclature using Cahn-Ingold-Prelog priority
rules (highest atomic number first; for ties, look at next atom
out); enantiomers (mirror images, same physical properties except
optical activity and reactions with other chiral molecules);
diastereomers (different stereo at one of multiple stereocenters,
different physical properties); meso compounds (multiple
stereocenters but overall achiral due to internal mirror plane);
optical rotation as a measurable property.

Write the brief's "Stereochemistry Analysis" section in 400–600
words.

1. **Identify all stereocenters.** Mark each on a copy of the
   target structure. For each, identify the four substituents.

2. **Assign R/S to each.** Use CIP priority. Show your reasoning
   for at least one stereocenter (the most complex).

3. **Total possible stereoisomers.** 2ⁿ stereoisomers for n
   stereocenters (in general; subtract for meso compounds).

4. **Identify the target's specific stereochemistry.** Which
   specific stereoisomer is the target? For drugs, this is often
   the active enantiomer; the other enantiomer is inactive,
   reduced activity, or even harmful (the thalidomide tragedy
   was the wrong enantiomer).

5. **The synthesis consequence.** Stereoselective synthesis is
   one of organic chemistry's hardest challenges. Note:
   - Will your synthesis produce a single stereoisomer, a racemic
     mixture, or a mixture of diastereomers?
   - If racemic, will resolution be required (chiral
     chromatography, recrystallization of diastereomeric salts)?
   - If single enantiomer required, will asymmetric synthesis be
     needed (chiral catalysts, chiral auxiliaries)?

6. **The bioactivity consequence (if drug).** For each
   stereocenter that affects bioactivity:
   - Which configuration is the active one?
   - What does the wrong enantiomer do (inactive, partial
     antagonist, toxic)?
   - Examples: ibuprofen — both enantiomers are sold (S is the
     active one; R is inactive but slowly converts to S in vivo).
     Naproxen — only S is sold (R is hepatotoxic).
     Atorvastatin — only the (3R,5R) is active.

End with one specific implication: in your eventual synthesis
(Chs 6+), what's the stereochemistry challenge that will be
hardest to solve?
```

---

**What this produces:** A 400–600 word Stereochemistry Analysis. For drug targets, this section is often the most consequential single piece in the whole project.

**How to adapt this prompt:**

- *For your own project:* Use a wedge-dash drawing convention consistently. Many students get R/S wrong because they get the priorities right but the perspective wrong.
- *For ChatGPT / Gemini:* Works as written.
- *For Claude Code:* Optional — RDKit and OpenEye can assign R/S programmatically as a check.
- *For a Claude Project:* Append.

**Connection to previous chapters:** Chapter 4's ring conformations and Chapter 5's stereocenters together describe the target's 3D shape.

**Preview of next chapter:** Chapter 6 covers organic reactions in general — the major reaction classes, energy diagrams, and arrow-pushing. You'll propose the FIRST retrosynthetic disconnection — what's the final bond-forming reaction in your target's synthesis?


---

## AI Wayback Machine

**Louis Pasteur** was discovered molecular chirality in 1848 by manually separating two crystal forms of tartrate salts — founding stereochemistry.

**Run this:**

```
Who is Louis Pasteur, and how does their work connect to stereochemistry at tetrahedral centers we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about their career or ideas.
```

→ Search **"Louis Pasteur"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to walk through one of Louis Pasteur's key experiments or syntheses in detail.
- Add a constraint: "Answer including criticisms or limits of Louis Pasteur's framework."

What changes? What gets better? What gets worse?
