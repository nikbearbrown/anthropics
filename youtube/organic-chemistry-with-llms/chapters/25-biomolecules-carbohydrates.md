# Chapter 25 — Biomolecules: Carbohydrates

*Sugars are the original biological energy currency. Their chemistry combines aldehyde or ketone groups with multiple hydroxyls, and the geometry — which face is up, which OH is which — controls everything from sweet taste to immune-system recognition.*

About 50% of the dry weight of all biomass on Earth is cellulose. Cellulose is a polymer of glucose, with thousands of glucose units linked end-to-end through specific hydroxyl groups. The slight difference between cellulose's β-1,4 linkages and starch's α-1,4 linkages — a flip of stereochemistry at one carbon — makes the two polymers physically and biologically completely different. Cellulose is fibrous, water-insoluble, and indigestible by mammals (which is why we can't eat wood). Starch is amorphous, partly water-soluble, and one of our main dietary carbohydrates. Same monomer, different stereochemistry, totally different chemistry.

This chapter is about carbohydrates — the polyhydroxylated aldehydes and ketones (and their cyclic hemiacetal forms) that dominate biological structure and energy storage. The chemistry is mostly chemistry we've already seen — hemiacetal formation, acetal formation, oxidation/reduction at carbonyl groups, stereochemistry — but applied to molecules with multiple stereocenters. The patterns and conventions of carbohydrate chemistry have their own vocabulary (D and L, α and β, pyranose and furanose) that's worth learning.

## What carbohydrates are

A *carbohydrate* is a polyhydroxylated aldehyde or ketone, usually with a formula approximating Cₙ(H₂O)ₙ — hence the name (carbon + hydrate, "watered carbon"). Glucose is C₆H₁₂O₆ — six carbons and the molecular formula corresponds to six "H₂O" equivalents.

Carbohydrates are classified by:

- **Number of monomer units.** *Monosaccharides* are individual sugars (like glucose). *Disaccharides* are two linked sugars (like sucrose, glucose + fructose). *Oligosaccharides* are 3–10 linked sugars. *Polysaccharides* are large polymers of monosaccharides (cellulose, starch, glycogen).

- **Carbonyl type.** *Aldoses* have an aldehyde group (at C1). *Ketoses* have a ketone group (usually at C2).

- **Number of carbons.** *Triose* (3 C), *tetrose* (4 C), *pentose* (5 C), *hexose* (6 C), *heptose* (7 C). Combined with the carbonyl type: glucose is an *aldohexose* (a 6-carbon aldose).

The most common monosaccharides:
- Glucose (aldohexose): blood sugar, the primary cellular energy substrate. C₆H₁₂O₆.
- Fructose (ketohexose): fruit sugar. Same C₆H₁₂O₆ formula but different connectivity (and stereochemistry).
- Galactose (aldohexose): a glucose stereoisomer; one component of lactose.
- Ribose (aldopentose): the sugar in RNA. C₅H₁₀O₅.
- Deoxyribose (aldopentose): the sugar in DNA, missing one OH compared to ribose.
- Mannose (aldohexose): another glucose stereoisomer; common in glycoproteins.

## Stereochemistry of sugars

Glucose has 4 chirality centers (C2, C3, C4, C5). With 2⁴ = 16 possible stereoisomers, the aldohexose family has 16 distinct molecules. Of these, 8 are *D*-aldohexoses (with C5's OH on the right in Fischer projection) and 8 are *L*-aldohexoses (mirror images). In nature, almost all biologically relevant aldohexoses are D-.

The historical reason for D/L nomenclature: glyceraldehyde (the simplest aldose) has one chirality center. Emil Fischer arbitrarily designated one enantiomer of glyceraldehyde as "D" (which we now know to be R in CIP terms; the OH is on the right side of the Fischer projection). Larger sugars are then classified by the configuration of the *highest-numbered chirality center* (C5 in hexoses; C4 in pentoses), which is the closest to the bottom in the Fischer projection. If that OH is on the right (like D-glyceraldehyde), the sugar is D-. If on the left, L-.

Almost all natural sugars are D-. (Almost all natural amino acids are L-. The two patterns evolved independently and are unrelated other than as historical accidents of how Earth's biology came together.)

The eight D-aldohexoses are: allose, altrose, glucose, mannose, gulose, idose, galactose, talose. Different combinations of R and S at C2, C3, C4 (with C5 fixed as R). Each is a distinct compound with distinct properties — different sweetness, different molecular shape, different recognition by enzymes.

The Fischer projection is the standard way to display the stereochemistry of a sugar. Vertical bonds go away from the viewer; horizontal bonds come toward. The chain is drawn with the carbonyl at the top (C1 for aldoses, C2 for ketoses), and chirality centers' OHs are drawn to the left or right. For D-glucose:

```
   CHO       (C1, aldehyde)
   H–C–OH    (C2, OH on right)
  HO–C–H     (C3, OH on left)
   H–C–OH    (C4, OH on right)
   H–C–OH    (C5, OH on right — D)
   CH₂OH     (C6)
```

## Cyclic forms: hemiacetals

Glucose in solution doesn't exist as the open-chain aldehyde drawn above. Most of it (about 99%) is in cyclic form — a six-membered ring formed by intramolecular hemiacetal formation between the C1 aldehyde and the C5 hydroxyl.

The cyclization: the C5-OH attacks the C1 carbonyl carbon (across the chain). The C=O becomes a tetrahedral C-OH. A ring forms — six atoms total (C1-C2-C3-C4-C5-O-C1), with the oxygen now part of the ring. The C1 has a new OH (the *anomeric* OH, from the original aldehyde) plus a new ring bond.

Two possible products: depending on whether the new C1-OH is on the same face as the C5-OH (or, equivalently, in the same face as the CH₂OH) or on the opposite face. These are called α and β.

For D-glucose:
- *α*-D-glucopyranose: the C1 OH is *axial* in the chair (on the opposite face from the CH₂OH at C5).
- *β*-D-glucopyranose: the C1 OH is *equatorial* (on the same face as the CH₂OH).

The two are different molecules. They're stereoisomers — *anomers* — that differ only at C1, the *anomeric carbon*. They have different properties: α-D-glucose has [α]_D = +112°; β-D-glucose has [α]_D = +18.7°. In solution, they interconvert by ring-opening, rotation around the C1–O bond in the open form, and reclosing on the other face. The equilibrium mixture is about 36% α, 64% β, and a tiny fraction (<0.1%) of the open-chain form. The interconversion is called *mutarotation* — the slow change in optical rotation that occurs when you dissolve a pure anomer in water.

The "pyranose" suffix indicates a six-membered ring. The five-membered analog is "furanose." Glucose can form a five-membered ring too (between C1 and C4-OH), but the six-membered pyranose is much more stable. Fructose, with its C2 carbonyl, prefers the five-membered furanose form (between C2 and C5-OH).

## Chair conformations of glucose

The β-D-glucopyranose chair is one of the most beautiful pieces of biological chemistry. In the standard chair conformation:

- The OH at C2, C3, C4 are all equatorial.
- The CH₂OH at C5 is equatorial.
- The OH at C1 (the anomeric OH in β-form) is equatorial.

Every substituent on every chirality center is equatorial. There are no axial substituents at all (other than the hydrogens).

This is unusually stable. The equatorial-only arrangement means there are no 1,3-diaxial steric interactions — none of the strain that would come from putting bulky groups axial. β-D-glucopyranose is the most stable hexopyranose, and its high stability is one of the reasons it's the universal cellular fuel.

α-D-glucopyranose has the C1-OH axial. It still has all other groups equatorial, but the one axial OH costs a bit of strain — explaining the equilibrium mix that favors β over α.

Other hexoses (mannose, galactose) have at least one OH locked into an unfavorable axial position. They're less stable than glucose, and biology often converts them to glucose for metabolism (or vice versa for synthesis of specific glycoconjugates).

## Sugar reactions

Glucose is a hemiacetal, so it can:

**React with another alcohol (acid-catalyzed) to form a glycoside (an acetal).** The anomeric OH is replaced by an OR. This is how disaccharides are made: glucose + glucose with the anomeric C1-OH of one attacking the C4-OH of the other, with loss of water, gives a glycosidic bond. Two glucoses connected by an α-1,4-glycosidic bond → maltose. Connected by a β-1,4 bond → cellobiose (a degradation product of cellulose).

**Be oxidized.** Glucose's C1 (the open-chain aldehyde, in equilibrium with the cyclic hemiacetal) reacts with oxidants like Tollens reagent (Ag(NH₃)₂⁺) or Benedict's solution (Cu²⁺) to give the corresponding carboxylic acid. This is the basis for old-fashioned diabetes tests (high blood sugar → much glucose → reaction with reagent in urine). Modern tests use enzymatic methods, but the underlying chemistry is the same — glucose is a *reducing sugar* because of this aldehyde-equilibrium reactivity.

**Be reduced.** NaBH₄ reduces the open-chain aldehyde of glucose to give a polyol (sugar alcohol). The product is sorbitol — a C₆ alcohol with OH on every carbon. Sorbitol is used as a low-calorie sweetener.

**Form esters and ethers.** Each OH can be acylated or alkylated. Used in synthesis to *protect* specific OHs while doing chemistry on others. Common protecting groups for sugars: acetate (CH₃CO-), benzyl ether (PhCH₂-), and various silyl ethers.

## Disaccharides

Two monosaccharides linked by a glycosidic bond. The four most common:

**Maltose.** Two glucoses, α-1,4 linked. The C1 of one is bonded to C4 of the other through O. The C1 of the second glucose (the "reducing end") still has its hemiacetal anomeric OH. Sweet, in beer and barley.

**Cellobiose.** Two glucoses, β-1,4 linked. Same connectivity as maltose but with the opposite stereochemistry at C1 of the first glucose. The β-1,4 bond is what makes cellulose; cellobiose is its repeating disaccharide unit.

**Lactose.** Galactose-β-1,4-glucose. Found in milk. Hydrolyzed by lactase enzyme in the small intestine; lactase deficiency in adults causes lactose intolerance.

**Sucrose.** Glucose-α,β-1,2-fructose. The C1 of glucose linked to the C2 of fructose. Both anomeric carbons are involved in the bond, so neither is left as a free hemiacetal — sucrose has no free anomeric OH and is a *non-reducing sugar*. This is unusual; most sugars are reducing.

## Polysaccharides

**Cellulose.** β-1,4-linked glucose polymer, 2,000–14,000 units long. The β-glycosidic linkages give cellulose a rigid, extended structure with extensive hydrogen bonding between chains. Cellulose forms strong fibers — wood, cotton, paper, plant cell walls. Mammals lack cellulase enzymes, so we can't digest cellulose. Some bacteria, fungi, and termites can. Ruminants (cows, sheep) host cellulase-producing bacteria in their first stomach, which is how they get carbohydrate energy from grass.

**Starch.** α-1,4-linked glucose polymer, with α-1,6 branch points every 25 or so glucose units (giving a tree-like branched structure). The α-linkages give starch a coiled, helical structure — quite different from cellulose's extended structure. Starch is digestible by mammals; we have α-amylase enzymes that hydrolyze it. Starch is the major dietary carbohydrate from plants — rice, wheat, corn, potatoes are mostly starch.

**Glycogen.** Like starch, but more highly branched. The energy storage polysaccharide of animals (in liver and muscle).

The α vs. β linkage is the central structural distinction. The same monomer (D-glucose) gives a structural polymer (cellulose, β) or an energy polymer (starch, α), depending on the linkage stereochemistry. This is one of the cleanest examples of how a small structural change has enormous functional consequences.

## Glycoproteins and glycolipids

Many proteins and lipids have sugar units attached. Glycoproteins are essential for cell-cell recognition (the ABO blood group antigens are glycoprotein-based), for protein folding (sugar groups can stabilize specific folded structures), and for protein clearance (glycosylated proteins have specific recognition by liver receptors).

Cell-surface sugar patterns are central to:
- Immune recognition (the ABO blood groups are determined by single sugars at the ends of long chains).
- Pathogen entry (influenza virus binds to specific sugars on cell surfaces).
- Cell signaling (selectins and other lectins recognize specific sugar codes).

The sugar code — the specific arrangements of monosaccharides in glycoproteins — is sometimes called the "third alphabet" of biology, after DNA's letter code and protein's amino acid code. Unlike the linear codes of DNA and proteins, the sugar code is branched and three-dimensional, and decoding it is a major area of contemporary research.

↳ **Dig Deeper — Why β-glucose dominates in nature**

> β-D-glucose (with all-equatorial substituents on the chair) is more stable than α-D-glucose. Walk through why this matters biologically. Cover: the energy difference (about 4 kJ/mol favoring β), the equilibrium mix in solution (~64% β, 36% α), why enzymes that bind glucose typically bind the β anomer specifically (e.g., glucose-6-phosphate in glycolysis), and why cellulose's β-1,4 linkages give it such different physical properties from starch's α-1,4 linkages even though both are polymers of D-glucose.

**What to do with the output:** Verify the explanation with structural drawings. Compare the chair conformations of β-D-glucose with all groups equatorial vs. α-D-glucose with the C1 OH axial. The energy difference of 4 kJ/mol corresponds to about a 3:1 thermodynamic ratio at body temperature, consistent with the observed equilibrium.

## What this chapter does

Carbohydrates are polyhydroxylated aldehydes (aldoses) or ketones (ketoses), classified by carbon count (triose, pentose, hexose) and stereochemistry (D vs. L based on the highest-numbered chirality center).

The chemistry of sugars is the chemistry of carbonyl + multiple OHs. They form cyclic hemiacetals (pyranoses for 6-membered, furanoses for 5-membered), with two stereoisomers at the anomeric carbon (α and β).

The standard β-D-glucopyranose chair has all substituents equatorial — the most stable arrangement of any hexopyranose. This stability is one reason glucose is the universal cellular fuel.

Sugar reactions: glycoside formation (acetal, with another alcohol), oxidation to carboxylic acids (reducing sugars react with Tollens, Benedict's), reduction to polyols (NaBH₄). Disaccharides and polysaccharides are formed by specific α or β-glycosidic linkages.

Cellulose (β-1,4-glucose) is structural; starch and glycogen (α-1,4-glucose with branching) are energy storage. Glycoproteins and glycolipids carry information through sugar patterns on cell surfaces.

The next chapters cover the other major classes of biomolecules: amino acids, peptides, and proteins (Chapter 26); lipids (Chapter 27); nucleic acids (Chapter 28); metabolic pathways (Chapter 29); and finally pericyclic reactions and synthetic polymers (Chapters 30–31).

---

*Source for all data, examples, and historical references: OpenStax* Organic Chemistry*, Chapter 25, modules m00288 through m00298.*
---

## LLM Exercise — Chapter 25: Biomolecules — Carbohydrates (Synthesize a Target Molecule Project)

**Project:** Synthesize a Target Molecule.
**What you're building this chapter:** carbohydrate analysis if your target is a sugar or glycoside; otherwise structural commentary on why carbohydrate chemistry doesn't directly apply.
**Tool:** **Claude Project**.

---

**The Prompt:**

```
Chapter 25 of my Synthesis project. Chapter 25 taught: monosaccharide
structure (Fischer projection convention; D vs. L based on the
highest-numbered chiral center; α vs. β anomers from the
cyclization at the anomeric carbon); glycosidic bonds (acetal
linkages between sugars and anomeric carbons); pyranose (6-ring)
vs. furanose (5-ring) cyclization; reducing sugars (have free
anomeric carbon, can be oxidized) vs. non-reducing sugars.

Write the brief's "Carbohydrate Analysis" section in 250–500
words.

If your target IS a carbohydrate or contains a sugar:

1. **Identify the sugar.** Name it. Determine its absolute
   configuration (D or L). Identify the anomeric carbon (α or β).
   Sketch Fischer and Haworth (and chair, if pyranose).

2. **Glycosidic linkages.** If your target has multiple sugar units
   connected, identify each glycosidic bond by:
   - Anomeric configuration (α or β).
   - Position of the OH on the second sugar (e.g., 1→4 link).
   - Whether the bond is between two anomeric carbons (non-
     reducing) or between an anomeric and a non-anomeric (reducing
     end retained).

3. **Synthesis considerations for sugars.** Sugar synthesis is
   notoriously difficult because of the many OH groups (each with
   similar reactivity) and the stereochemistry of anomeric center.
   Note any protecting-group strategy your target requires.

If your target is NOT a carbohydrate:

1. **State that.** "[Target] is not a carbohydrate; this chapter's
   chemistry doesn't directly apply to its synthesis."

2. **Note any sugar-LIKE features.** Even non-sugars may contain
   acetals (sugar-like), hemiacetals, or polyols (multiple OH
   groups). If your target has these, note them.

3. **Test your structural fluency.** Briefly: would you be able to
   recognize and name glucose, fructose, ribose, or another common
   sugar from a Fischer or Haworth projection? Practice on one
   if helpful.

End with: which features of your target's structure would change
its chemistry if a sugar were attached or a sugar moiety
incorporated? (Many drugs have sugar appendages — glycosides like
digitalis cardiac drugs — that affect solubility and bioavailability.)
```

---

**What this produces:** A 250–500 word section. For sugar-containing drugs (digoxin, amygdalin, many antibiotics), this is central. For non-sugar targets, it's a brief check on structural fluency.

**Connection to previous chapters:** Ch 19's acetal chemistry directly underlies glycoside formation.

**Preview of next chapter:** Chapter 26 covers amino acids, peptides, and proteins. If your target is a peptide or contains amide linkages from amino acids, this is central. Many drugs are based on peptide frameworks.


---

## AI Wayback Machine

**Emil Fischer** was determined the structures of sugars, purines, and proteins in the 1890s — Nobel 1902.

**Run this:**

```
Who is Emil Fischer, and how does their work connect to carbohydrates we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about their career or ideas.
```

→ Search **"Emil Fischer"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to walk through one of Emil Fischer's key experiments or syntheses in detail.
- Add a constraint: "Answer including criticisms or limits of Emil Fischer's framework."

What changes? What gets better? What gets worse?
