# Chapter 21 — Carboxylic Acid Derivatives: Nucleophilic Acyl Substitution Reactions

*A carboxylic acid with the OH replaced by a different group becomes one of four "derivatives" — and each one has a distinct reactivity, exactly because the leaving group departs at a different rate. Understanding the order of reactivity is the central skill of this chapter.*

In 1834 Justus von Liebig and Friedrich Wöhler observed that benzoyl chloride (PhCOCl) reacts with ammonia to give benzamide (PhCONH₂) and HCl. The mechanism wasn't worked out for nearly a century, but the observation was already pointing at something important: a carbonyl with a halide attached is reactive enough to react with even mild nucleophiles, transferring the carbonyl group from one structural environment to another. The acyl group (R-CO-) had been moved.

That movement — substituting one group for another at a carbonyl carbon — is *nucleophilic acyl substitution*, the central reaction class for this chapter. It's not the nucleophilic addition of Chapter 19, where the carbon becomes sp³ permanently; it's a substitution where the addition forms a tetrahedral intermediate that then collapses, expelling a leaving group to regenerate the C=O.

The four derivatives of carboxylic acids — acid chlorides, anhydrides, esters, amides — differ from each other in their leaving group, and that leaving group's properties determine the reactivity. Acid chlorides are most reactive because Cl⁻ is the best leaving group. Amides are least reactive because the amide nitrogen is a terrible leaving group. The reactivity order — chloride > anhydride > ester > amide — is one of the most useful predictive rules in synthesis.

This chapter covers the four derivatives, their interconversions, and the unifying mechanism of nucleophilic acyl substitution.

## Structure of the derivatives

Each derivative is RCO–LG, where LG is the leaving group:

| Derivative | LG | Example |
|---|---|---|
| Acid chloride | –Cl | acetyl chloride (CH₃COCl) |
| Acid anhydride | –OCOR | acetic anhydride ((CH₃CO)₂O) |
| Ester | –OR | ethyl acetate (CH₃CO₂CH₂CH₃) |
| Amide | –NR₂ | acetamide (CH₃CONH₂) |
| Thioester | –SR | ethyl thioacetate (CH₃COSEt) — biological |
| Acyl phosphate | –OPO(OR)₂ | acetyl phosphate — biological |
| Nitrile | (–C≡N as a stretched form) | ethanenitrile (CH₃CN) — Chapter 20 |

The first four are the major laboratory derivatives. Thioesters and acyl phosphates are biological — fatty acid biosynthesis runs on coenzyme A thioesters; biological phosphate transfer often runs through acyl phosphate intermediates.

Naming:
- Acid chlorides: -*oyl chloride* on the parent. Acetyl chloride, propanoyl chloride.
- Anhydrides: replace "acid" with "anhydride" in the parent name. Acetic anhydride, benzoic anhydride.
- Esters: alkyl part first, then -*oate* on the parent acid. Ethyl acetate, methyl benzoate.
- Amides: -*amide* on the parent. Acetamide, benzamide. For substituted amides, N-methylacetamide (with N as the locant for substituents on nitrogen).

## The unifying mechanism: nucleophilic acyl substitution

Every reaction of a carboxylic acid derivative with a nucleophile follows the same two-step pattern:

**Step 1 (addition):** the nucleophile attacks the carbonyl carbon. The π electrons go onto oxygen, giving a tetrahedral intermediate with a negative charge on the oxygen (an alkoxide). This is identical to the first step of nucleophilic addition in Chapter 19.

**Step 2 (elimination):** the tetrahedral intermediate collapses. The C–LG bond breaks, with both electrons going onto the leaving group, and the C=O is reformed. The result is a new acyl compound, RCO–Nu, plus the leaving group LG⁻.

Net transformation: RCO–LG + Nu⁻ → RCO–Nu + LG⁻. The acyl group has moved from being attached to LG to being attached to Nu. Substitution at the carbonyl carbon.

The difference from nucleophilic addition (Chapter 19): aldehydes and ketones don't have a leaving group attached to the carbonyl, so the tetrahedral intermediate has nowhere to go except by protonation to give an alcohol. With a derivative present, the alkoxide can collapse by expelling the leaving group, regenerating the carbonyl.

The reaction's energetics: the rate-determining step is usually the addition (step 1), because forming the tetrahedral intermediate is endothermic. The leaving group's role is to determine *whether* the tetrahedral intermediate collapses forward (giving the substituted product) or backward (regenerating the starting material). A good leaving group means forward collapse, productive reaction. A bad leaving group means backward collapse, unproductive — the reaction reverses and equilibrium is unfavorable.

## The reactivity order

The order of reactivity for the derivatives:

**Acid chloride > anhydride > ester > amide**

(With thioester roughly between anhydride and ester. With carboxylate ion essentially unreactive.)

The order has two contributors:

**Steric.** Within a series, more bulk around the carbonyl means more difficult addition. But this is a relatively minor factor compared to electronic.

**Electronic.** A leaving group that is electron-withdrawing makes the carbonyl carbon more electrophilic. A leaving group that has lone pairs and can donate into the carbonyl makes the carbonyl less electrophilic.

For acid chloride: chloride is electron-withdrawing (high electronegativity, no donation back into the C=O). The carbonyl is highly electrophilic. Reactive.

For ester: alkoxide oxygen donates lone pairs into the C=O via resonance (the resonance structure RC(=OR')(-O⁻) has some weight). This reduces the carbonyl's electrophilicity. Less reactive.

For amide: nitrogen donates lone pairs into the C=O *strongly* via resonance — the amide resonance structure RC(=NR'')(-O⁻) has substantial weight (about 40% of the molecule's character). This makes the C=O much less electrophilic. Least reactive.

The amide resonance is so significant that amide rotation around the C–N bond is hindered (~80 kJ/mol barrier), giving amides observable cis/trans isomerism in NMR. This is the structural basis for protein backbone rigidity (every peptide bond is an amide; the planar geometry holds the backbone in regular structures).

The reactivity order also tells you about the *direction* of conversions: a derivative can be converted to a *less reactive* derivative without trouble. Acid chloride → ester: easy, just react with alcohol. Ester → amide: usually doesn't proceed cleanly (amide is less reactive, but the mechanism still requires the amine to attack and water to leave); strong conditions or activation needed.

But you can't go uphill: amide → ester is hard (amide is less reactive than ester in the forward direction, and the equilibrium for ester ↔ amide formation favors ester). To convert an amide to an ester, you'd typically hydrolyze the amide first (to acid) and then esterify.

## Acid chlorides

Acid chlorides (RCOCl) are the most reactive derivatives. They're typically prepared from carboxylic acids using SOCl₂ or PCl₃ or oxalyl chloride ((COCl)₂):

$$\text{R-COOH} + \text{SOCl}_2 \rightarrow \text{R-COCl} + \text{SO}_2 + \text{HCl}$$

Acid chlorides react with almost any nucleophile readily:
- + H₂O → carboxylic acid
- + R'OH → ester
- + R'NH₂ → amide
- + R'COO⁻ → anhydride (mixed)
- + R'-CdCl/R'₂CuLi → ketone (by addition, controlled to avoid further reaction)
- + LiAlH₄ → primary alcohol

The first three are routine, used in synthesis to make esters and amides cleanly. The acid chloride is often the activated form of an acid that is then condensed with the desired nucleophile.

Acid chlorides also undergo Friedel-Crafts acylation (Chapter 16) to give aryl ketones.

## Anhydrides

Acid anhydrides (RCOOCOR) are the second-most reactive derivative. They're prepared by:
- Condensation of two carboxylic acids (often by removing water with strong dehydration: P₂O₅, or refluxing in acetic anhydride itself).
- Reaction of an acid chloride with a carboxylate.

Anhydrides react with nucleophiles to give the same products as acid chlorides:
- + H₂O → 2 carboxylic acids
- + R'OH → ester + carboxylic acid
- + R'NH₂ → amide + carboxylic acid

Note that one of the two acyl groups becomes the product (ester or amide), while the other becomes a carboxylic acid (the leaving group during the substitution). For symmetric anhydrides (R = R'), both halves give the same product. For unsymmetric anhydrides, this is sometimes used in synthesis to deliver one specific acyl group.

Acetic anhydride is widely used as an acetylating agent — it converts amines to acetamides, alcohols to acetate esters. The byproduct is acetic acid, which is easy to remove.

## Esters

Esters (RCO₂R') are the most common derivative in everyday and biological chemistry. Triglycerides (the energy-storage fats in your body) are esters of fatty acids and glycerol. Polyesters (PET, the polymer of plastic bottles) are made from ester linkages between carboxylic acids and diols. Smell molecules — bananas, pears, apples — are often simple esters.

Esters are made by:

**Fischer esterification.** R–COOH + R'–OH + acid catalyst → ester + H₂O. Reversible. Needs water removal or excess of one reagent to drive forward.

**Acid chloride + alcohol.** Cleanest method. R–COCl + R'–OH (with base to neutralize HCl) → ester + HCl. Used in synthesis when high yields are needed.

**Anhydride + alcohol.** R–COOCOR + R'–OH → ester + carboxylic acid.

**DCC coupling.** R–COOH + R'–OH + DCC → ester + DCU (dicyclohexylurea). The DCC activates the carboxylic acid. Used when other methods aren't suitable.

Esters react with nucleophiles in standard nucleophilic acyl substitution, but more slowly than chlorides or anhydrides. The mostly important reactions:

**Hydrolysis (saponification).** Ester + H₂O (acid or base) → carboxylic acid + alcohol. Under base (NaOH), the reaction is irreversible because the carboxylate salt is the product (not the free acid). The reaction is called *saponification* (from the Latin *sapo*, soap) because the alkali metal salts of long-chain fatty acids are exactly soap.

**Aminolysis.** Ester + R'NH₂ → amide + alcohol. Slower than alcoholysis but happens with heat or excess amine.

**Reduction.** LiAlH₄ reduces esters to primary alcohols. The mechanism goes through an aldehyde intermediate, which is further reduced. DIBAL-H at low temperature stops at the aldehyde — useful when you need an aldehyde from an ester.

**Grignard addition.** R'–MgX + ester → tertiary alcohol (after workup). Two equivalents of Grignard add: the first one adds to the ester (giving a ketone-like tetrahedral intermediate that collapses to a ketone), the second adds to that ketone (giving the tertiary alcohol). The product has two of the new R' groups attached.

**Transesterification.** Ester + different R'OH (with acid or base catalyst) → different ester + original alcohol. The two ROHs swap. Used in industrial preparation of biodiesel (fatty acid methyl esters from triglycerides + methanol, with NaOH catalyst).

## Amides

Amides (RCONR'₂) are the least reactive derivative. Peptide bonds in proteins are amides. They're remarkably stable — the half-life of a peptide bond at neutral pH and 37 °C is hundreds of years (which is why proteins exist on biological timescales).

Amides are made by reaction of acid chlorides, anhydrides, or activated acids (DCC-coupled) with amines. The direct combination of carboxylic acid + amine usually fails because the acid–amine salt forms first, blocking the chemistry; high temperature (160°C+) or coupling reagents are needed.

Amide reactions:

**Hydrolysis.** Amide + H₂O (acid or base) → carboxylic acid + amine. Very slow at neutral pH. Acid hydrolysis (HCl, reflux) and base hydrolysis (NaOH, reflux) both work, though the conditions are usually harsh. Enzymatic hydrolysis (by proteases) is much faster — proteases evolved to hydrolyze peptide bonds in seconds rather than centuries.

**Reduction.** LiAlH₄ reduces amides to amines. The carbonyl C goes to CH₂; the result is R–CH₂–NR'₂. Useful for making secondary or tertiary amines.

**Hofmann rearrangement.** Amide + Br₂ + NaOH → primary amine with one fewer carbon. The mechanism involves α-halogenation, deprotonation, and migration of an alkyl group from carbon to nitrogen. R–CONH₂ → R–NH₂ + CO₂.

The Hofmann rearrangement is a useful but specialized reaction. It's one of a class of *rearrangements* with similar mechanisms (Curtius, Schmidt, Beckmann) that involve nitrogen migration in α-halogenated amides or related compounds.

## Polymers from acyl substitution

Several major industrial polymers come from nucleophilic acyl substitution:

- **Polyamides** (nylons): a diamine reacts with a dicarboxylic acid (or acid chloride) to give a polymer with amide linkages. Nylon-6,6 is from hexamethylenediamine + adipic acid. Used in fibers, textiles, plastics.

- **Polyesters**: a diol reacts with a dicarboxylic acid (or its derivative) to give a polymer with ester linkages. PET (polyethylene terephthalate) is from ethylene glycol + terephthalic acid. Soda bottles, polyester clothing.

- **Polyurethanes**: a diol reacts with a diisocyanate. Foam, mattresses, insulation.

These are step-growth polymers — each step is a single nucleophilic acyl substitution, and the polymer grows molecule-by-molecule by adding monomer units. Industrially, these are made on enormous scales (tens of millions of tons per year combined).

↳ **Dig Deeper — Why amide bond rotation is restricted**

> The amide C–N bond has substantial double-bond character due to resonance. Walk through the orbital picture. Cover: the alignment of nitrogen's lone pair with the C=O π system, the rotation barrier (~80 kJ/mol for amides) compared to a single bond (essentially free rotation), how this is observed in NMR (cis-trans isomerism around the amide bond, with separate peaks for cis and trans rotamers in proline-containing peptides), and how this is the structural basis for the planar peptide bond in protein structures.

**What to do with the output:** Compare against any biochemistry textbook on protein structure. Verify that Claude correctly identifies that the planar peptide bond is what makes Ramachandran plots possible — the geometry of the peptide bond is fixed, and only the φ and ψ angles around the α-carbon vary in protein conformation.

## What this chapter does

The four derivatives of carboxylic acids — chlorides, anhydrides, esters, amides — differ in their leaving groups and therefore in their reactivity. The order:

**chloride > anhydride > ester > amide**

The mechanism of every reaction is the same: nucleophile adds to the carbonyl carbon to form a tetrahedral alkoxide intermediate, which then collapses by expelling the leaving group to give a new acyl compound.

You can convert a more reactive derivative to a less reactive one easily (chloride → ester, ester → amide). Going the other direction (amide → ester) requires hydrolyzing back to the acid first.

Each derivative has its own characteristic synthetic uses:
- Chlorides: most-used activating form of an acid for synthesis.
- Anhydrides: convenient acetylating agents, often used in cyclic forms (like maleic anhydride) for Diels-Alder synthesis.
- Esters: most common in biology and consumer products; used industrially in polyesters.
- Amides: most stable of the derivatives; used in nylons, peptides, and pharmaceuticals.

Hydrolysis (back to the parent acid + leaving group), aminolysis (to amides), and reduction (to alcohols or amines) are the major reactions that consume each derivative.

The next chapter (22) and chapter 23 cover the chemistry that uses *the carbon next to the carbonyl* (the α-carbon) — α-substitution and condensation reactions. These are the C–C bond-forming reactions that build complex molecules from carbonyl building blocks.

---

*Source for all data, examples, and historical references: OpenStax* Organic Chemistry*, Chapter 21, modules m00244 through m00254.*
---

## LLM Exercise — Chapter 21: Carboxylic Acid Derivatives — Nucleophilic Acyl Substitution (Synthesize a Target Molecule Project)

**Project:** Synthesize a Target Molecule.
**What you're building this chapter:** acid-derivative chemistry — ester, amide, acid chloride, anhydride installations and interconversions.
**Tool:** **Claude Project**.

---

**The Prompt:**

```
Chapter 21 of my Synthesis project. Chapter 21 taught: the
carboxylic acid derivatives and their reactivity ordering:
   - Acid chloride (R-COCl) — most reactive (good LG).
   - Anhydride (RCOOCOR) — very reactive.
   - Ester (RCOOR') — moderately reactive.
   - Amide (RCONR'₂) — least reactive (poor LG, strong resonance
     stabilization).
Reactivity decreases as the leaving group becomes worse. The
universal rule: you can convert from MORE-reactive to LESS-
reactive in one step (acid chloride → ester, ester → amide, etc.).
The reverse requires activation (typically going through the acid
chloride or anhydride intermediate).

Write the brief's "Acid Derivatives Section" in 400–600 words.

1. **Identify any esters, amides, anhydrides, or acid chlorides
   in your target.** Amides are especially common in drugs
   (every peptide bond is an amide).

2. **Propose installation routes.** For each:
   - **Amide formation**: most common = acid chloride + amine, or
     coupling reagent (DCC, EDC, HATU) + carboxylic acid + amine.
   - **Ester formation**: Fischer esterification (RCOOH + ROH +
     acid, equilibrium); or acid chloride + alcohol; or via
     activated intermediates.
   - **Acid chloride formation**: RCOOH + SOCl₂ or (COCl)₂.
   - **Anhydride formation**: typically from two acid chlorides
     or specialized conditions.

3. **The reactivity-ordering rule applied.** For your target, did
   the synthesis use the rule efficiently? E.g., if you need to
   make an amide late in the synthesis, the standard move is:
   carboxylic acid → acid chloride → amide.

4. **Hydrolysis considerations.** Many esters and amides are
   prone to hydrolysis under acidic or basic conditions:
   - Esters: saponification by NaOH gives the carboxylic acid +
     alcohol.
   - Amides: hydrolyzed under more forcing conditions (strong
     acid or base, heat).
   These hydrolysis pathways are why amide bonds in proteins are
   relatively stable but can be cleaved enzymatically (proteases).

5. **Draw the nucleophilic acyl substitution mechanism for ONE
   step.** Show:
   - Nucleophile (e.g., amine) attacks the C=O carbon.
   - Tetrahedral intermediate.
   - Leaving group departs.
   - Product.

End with: which acid-derivative bond in your target requires the
most careful sequencing? (Often: the last amide installed, which
must survive subsequent conditions.)
```

---

**What this produces:** A 400–600 word section. Amide-bond formation is the single most-used reaction in pharmaceutical synthesis.

**Connection to previous chapters:** Ch 19 (general nucleophilic addition); Ch 20 (carboxylic acid); Ch 21 (derivatives) form the acyl-chemistry chain.

**Preview of next chapter:** Chapter 22 covers alpha-substitution at carbonyls. If your target has a C-C bond adjacent to a carbonyl, it may have been made by alpha-alkylation.


---

## AI Wayback Machine

**Bruce Merrifield** was invented solid-phase peptide synthesis in 1963 — Nobel 1984.

**Run this:**

```
Who is Bruce Merrifield, and how does their work connect to acyl substitution we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about their career or ideas.
```

→ Search **"Bruce Merrifield"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to walk through one of Bruce Merrifield's key experiments or syntheses in detail.
- Add a constraint: "Answer including criticisms or limits of Bruce Merrifield's framework."

What changes? What gets better? What gets worse?
