# Chapter 23 — Carbonyl Condensation Reactions

*The aldol and the Claisen are the workhorses of C–C bond formation in nature. Almost every carbon skeleton in biology is built, somewhere along the way, by an enolate attacking another carbonyl.*

In acetyl-CoA reaction with oxaloacetate, the methyl carbon of acetyl-CoA (the α-carbon of a thioester) attacks the carbonyl carbon of oxaloacetate. A new C–C bond forms. The product is citrate, after a hydrolysis step. This is the entry reaction of the citric acid cycle, and it's catalyzed by citrate synthase. The mechanism is — fundamentally — an aldol-like reaction, where an enolate of acetyl-CoA attacks the C=O of oxaloacetate. The same mechanism that biology uses billions of times a second is the same mechanism that chemists use in the laboratory aldol reaction.

A *carbonyl condensation reaction* is a reaction between two carbonyl-containing partners, where one is converted to its enolate (the α-carbon is the nucleophile) and the other serves as the electrophile (the carbonyl carbon is attacked). The product has both carbonyl groups in the same molecule, with a new C–C bond. Most natural-product carbon skeletons are built this way, in successive condensation steps, by enzymes whose mechanisms are recognizably aldol- or Claisen-like.

This chapter covers the major condensation reactions: aldol, Claisen, Michael (conjugate addition), and a few important crossed and intramolecular variants. Together with chapters 19–22, it completes the carbonyl chemistry of the book.

## The aldol reaction

In the basic aldol reaction, a base (typically NaOH or NaOR) generates a small amount of enolate from an aldehyde or ketone. The enolate then attacks the carbonyl of another molecule of the same aldehyde/ketone. The result is a β-hydroxy carbonyl compound.

Two molecules of acetaldehyde + dilute NaOH → 3-hydroxybutanal (the original "aldol", from "aldehyde + alcohol"):

$$2\,\text{CH}_3\text{CHO} \xrightarrow{\text{NaOH}} \text{CH}_3\text{CH(OH)CH}_2\text{CHO}$$

Mechanism:

1. NaOH deprotonates the α-carbon of one acetaldehyde, giving an enolate.
2. The enolate attacks the carbonyl carbon of another acetaldehyde, forming a new C–C bond. The carbonyl oxygen becomes a tetrahedral alkoxide.
3. The alkoxide picks up a proton (from water or another acetaldehyde) to give the β-hydroxy aldehyde.

The aldol product has two key features:
- A new C–C bond between the α-carbon of one molecule and the carbonyl carbon of the other.
- A β-hydroxy group (the alcohol that came from the captured carbonyl oxygen).

The reaction is reversible. For most aldehydes, the equilibrium favors the aldol product modestly. For ketones, it favors the starting material — ketones are less electrophilic than aldehydes, and steric crowding around the new bond is worse. To run an aldol on a ketone, you typically need to remove the product or run the dehydration step (next section) to drive the equilibrium.

## Aldol dehydration: the Δ in the name "condensation"

The β-hydroxy carbonyl from the aldol reaction can lose water to give an α,β-unsaturated carbonyl:

$$\text{CH}_3\text{CH(OH)CH}_2\text{CHO} \xrightarrow{\Delta, \text{base or acid}} \text{CH}_3\text{CH=CHCHO}$$

The dehydration is unusually favorable — much more so than dehydration of typical alcohols — because the resulting alkene is conjugated with the carbonyl, stabilizing the product. The driving force is conjugation.

Mechanism (base-catalyzed):

1. Base removes the α-H of the β-hydroxy carbonyl (acidified by the adjacent C=O — it's an enolate of the original carbonyl).
2. The enolate's π electrons push out the β-hydroxide as a leaving group, giving the α,β-unsaturated carbonyl.

The whole sequence (aldol + dehydration) is what makes carbonyl condensation a useful synthetic operation. Even if the initial aldol step is unfavorable, the dehydration drives the overall equilibrium to the unsaturated carbonyl product.

A typical experimental procedure: add NaOH to acetone, warm. The product is 4-methyl-3-penten-2-one (mesityl oxide), the dehydrated aldol product of two acetones. Without the dehydration step, the equilibrium would favor starting acetone.

## Crossed aldol reactions

When two different carbonyl compounds are mixed, four products are possible:

- A enolate + A carbonyl → A-A product
- A enolate + B carbonyl → A-B product
- B enolate + A carbonyl → B-A product
- B enolate + B carbonyl → B-B product

Without further control, you get a mixture of all four. To get a clean crossed aldol, you need to ensure only one enolate forms.

The typical strategy: pick one partner that has *no α-hydrogens*, so it can't form an enolate. It only acts as the electrophile. Then pick the other partner — which has α-hydrogens — and use it as the enolate source.

Common α-hydrogen-free carbonyls: formaldehyde, benzaldehyde, *tert*-butyl ketone (no α-Hs on the *t*-Bu side, only on the methyl), cinnamaldehyde, etc. Any aromatic aldehyde works (no α-H because there's no α-C in the conventional sense — the α-position would be an aromatic C with no H to lose to the enolate).

Example: PhCHO + CH₃COCH₃ + base → PhCH=CHCOCH₃ (benzalacetone). The acetone enolate attacks benzaldehyde; the resulting aldol dehydrates to the conjugated enone. Clean reaction because benzaldehyde has no α-H and can't enolize.

Crossed aldols with two enolizable partners can be done by *first* forming one enolate exclusively (by pre-deprotonation with LDA at low temperature) and then adding the other partner. The kinetic enolate of one molecule reacts with the electrophilic carbonyl of the other, before the second enolate has a chance to form. This is the modern approach in synthesis, used widely.

## The Claisen condensation

The ester analog of the aldol. Two molecules of an ester combine, with the α-carbon of one attacking the carbonyl carbon of the other.

$$2\,\text{CH}_3\text{CO}_2\text{Et} \xrightarrow{\text{NaOEt}} \text{CH}_3\text{COCH}_2\text{CO}_2\text{Et} + \text{EtOH}$$

The product is a β-ketoester. Mechanism:

1. NaOEt deprotonates the α-carbon of one ester (generating the enolate, slowly because ester pKa is about 25).
2. The enolate attacks the carbonyl of another ester molecule, forming a tetrahedral intermediate.
3. Unlike the aldol case, the tetrahedral intermediate can collapse by expelling the *alkoxide* (–OEt) leaving group, regenerating the C=O. The result is a new C–C bond and an ester turned into a ketone.
4. The resulting β-ketoester has an acidic α-H (between two C=O groups, pKa about 11). It's deprotonated by ethoxide, giving a stabilized enolate. This deprotonation pulls the equilibrium forward.

Step 4 is essential. Without the very acidic β-ketoester product to absorb the alkoxide, the Claisen wouldn't go — the equilibrium for the basic step (enolate + ester → β-ketoester + alkoxide) is unfavorable. The acid-base equilibrium that follows (β-ketoester + alkoxide → β-ketoester anion + alcohol) is very favorable, and Le Chatelier's principle drives the whole sequence forward.

The Claisen condensation is essentially universal in fatty acid biosynthesis. Each round of fatty acid chain extension is a Claisen condensation between a CoA thioester (the "growing chain") and another acetyl-CoA (the "extender unit"), catalyzed by an enzyme called fatty acid synthase. Eight or more rounds of Claisen condensation, each adding two carbons, build palmitic acid (C₁₆) from a starting acetyl-CoA.

## Crossed Claisens and intramolecular Claisens

As with aldols, crossed Claisens require careful control. The standard strategy is to use a non-enolizable ester (no α-H) as the electrophile and a regular ester as the enolate source.

Intramolecular Claisens give cyclic β-ketoesters. The *Dieckmann condensation* is a Claisen on a diester — the two ends of one molecule condensing to form a ring. Diethyl heptanedioate (a 7-carbon diester) undergoes Dieckmann to give a cyclic β-ketoester (5-carbon ring with both ester groups still attached at strategic positions).

## The Michael (conjugate) addition

A nucleophile can attack the β-carbon of an α,β-unsaturated carbonyl, giving conjugate addition (Chapter 19). When the nucleophile is an enolate, this is a Michael addition.

$$\text{Enolate} + \alpha,\beta\text{-unsaturated carbonyl} \longrightarrow \text{1,5-dicarbonyl}$$

The Michael addition is the basis for synthesizing 1,5-dicarbonyls (with two C=O groups separated by three C's, a useful structural pattern).

Stabilized enolates (from β-ketoesters, β-diesters, malonates) are typical Michael donors. The acceptor is any α,β-unsaturated carbonyl. The base (catalytic) generates the enolate, which adds to the β-carbon of the acceptor. The resulting enolate (now of the acceptor) picks up a proton.

The Michael addition is one of the most-used reactions for building C–C bonds in synthesis. It's also widely used in step-growth polymer synthesis (making polyacrylates, for example).

## The Robinson annulation

A two-step sequence that combines Michael addition and intramolecular aldol. The Michael reaction gives a 1,5-diketone; the intramolecular aldol cyclizes it (with dehydration) to give a six-membered ring with a new C=C. Net result: a cyclohexenone from an open-chain dicarbonyl substrate.

The Robinson annulation is the standard method for building 6-membered carbocyclic rings with specific substitution patterns. It's at the heart of many steroid syntheses (and, historically, was central to the development of total synthesis as a field — R. B. Woodward and colleagues used Robinson annulations extensively in the 1940s–60s).

A typical Robinson:

1. β-diketone (or β-ketoester) + α,β-unsaturated ketone + base → 1,5-diketone (Michael).
2. Heat with base or acid → intramolecular aldol + dehydration → cyclohexenone.

The reaction is a cornerstone of synthetic organic chemistry. Most six-membered rings in natural products that the chemist needs to make are made by Robinson-like sequences, often with modern asymmetric variations to control stereochemistry.

## Biological condensations

A surveyed list:

**Citrate synthase** (citric acid cycle): acetyl-CoA + oxaloacetate → citrate. Aldol-like; the methyl of acetyl-CoA is the nucleophile.

**Aldolase** (glycolysis): fructose-1,6-bisphosphate ⇌ glyceraldehyde-3-phosphate + dihydroxyacetone phosphate. A retro-aldol — the reverse direction. The enzyme catalyzes the cleavage of a 6-carbon sugar into two 3-carbon sugars at the aldol-product's β-hydroxy bond.

**Fatty acid synthase** (lipid synthesis): runs Claisen condensation. Each round adds two carbons to a growing acyl-CoA chain. Catalyzed by KAS (β-ketoacyl synthase) domain of the enzyme.

**Polyketide synthases** (natural product biosynthesis): another Claisen-based system. Builds aromatic and aliphatic polyketide natural products by repeated condensation steps. Erythromycin and other macrolide antibiotics are polyketides.

**Aldol reactions in metabolism**: appear in dozens of pathways. The mechanism is so general that any C–C bond formation in metabolism that produces a β-hydroxy compound (or its derivative) is likely to be aldol-mechanism.

In all these cases, the active intermediate is an enolate (or enol). The enzyme stabilizes the enolate, brings the second substrate close, and lowers the activation energy. The chemistry is the same as in the lab; the rate enhancement and selectivity come from the protein scaffold.

↳ **Dig Deeper — Why fatty acids are even-numbered**

> Almost all naturally occurring fatty acids have even numbers of carbons (16, 18, 20, etc.). Walk through why this is mechanistically. Cover: the role of acetyl-CoA as the C₂ extender unit in fatty acid synthase, why the synthase only adds two carbons per cycle, what would happen if propionyl-CoA (C₃) were used as an extender, and the rare cases (in some marine organisms and bacteria) where odd-numbered fatty acids arise. Use palmitic acid biosynthesis (16 carbons, 7 cycles of Claisen condensation) as the worked example.

**What to do with the output:** Verify the explanation with mechanism details. Each round of fatty acid synthase: condensation (Claisen of acetyl-CoA with the growing acyl chain), reduction (β-keto → β-OH), dehydration (α,β-unsaturated), and reduction (alkene → alkane). Net: addition of two carbons.

## Synthesis using condensations

A toolkit summary:

To make β-hydroxy aldehydes or ketones: aldol reaction (base, then keep at low T to retain alcohol).

To make α,β-unsaturated carbonyls (enones): aldol reaction with subsequent dehydration (base, heat).

To make β-ketoesters: Claisen condensation of esters.

To make cyclic β-ketoesters: Dieckmann condensation of diesters.

To make 1,5-dicarbonyls: Michael addition.

To make cyclohexenones (especially as part of steroid or natural-product synthesis): Robinson annulation.

For specific products, the synthesis question is usually: which of these reactions, run in which order, with which substrates, gives the target? The answer involves both retrosynthetic disconnection (find the C–C bonds that could have been made by aldol or Claisen, see what fragments they imply) and forward planning (recognize the steps and check for compatibility with other functional groups).

## What this chapter does

Carbonyl condensation reactions form C–C bonds between two carbonyl-containing partners, with one partner serving as the enolate (nucleophile at α-carbon) and the other as the electrophile (carbonyl carbon).

The major reactions:
- **Aldol**: enolate of aldehyde/ketone + aldehyde/ketone → β-hydroxy carbonyl. With dehydration: α,β-unsaturated carbonyl.
- **Claisen**: enolate of ester + ester → β-ketoester (with loss of an alcohol). The acidic β-ketoester product drives the equilibrium.
- **Michael**: stabilized enolate + α,β-unsaturated carbonyl → 1,5-dicarbonyl.
- **Robinson annulation**: Michael followed by intramolecular aldol + dehydration → cyclohexenone.
- **Dieckmann**: intramolecular Claisen on a diester → cyclic β-ketoester.

Crossed reactions need a non-enolizable partner (no α-H) as the electrophile, or careful pre-formation of one specific enolate (LDA at low T) to dominate the reaction.

Biological condensations include the citric acid cycle's first step (citrate synthase), glycolysis (aldolase, retro-aldol), fatty acid biosynthesis (fatty acid synthase, Claisen-based), and many polyketide pathways. The same mechanisms run in chemists' flasks and in cells; the enzymes are catalysts that speed up reactions chemists can do (slowly) themselves.

The next chapter (24) shifts to a different functional group: amines and heterocycles. After that, the remaining chapters (25–31) cover biomolecules — sugars, amino acids, lipids, nucleic acids — in which most of the chemistry we've covered comes back as the workings of biology.

---

*Source for all data, examples, and historical references: OpenStax* Organic Chemistry*, Chapter 23, modules m00263 through m00276.*
---

## LLM Exercise — Chapter 23: Carbonyl Condensation Reactions (Synthesize a Target Molecule Project)

**Project:** Synthesize a Target Molecule.
**What you're building this chapter:** aldol or Claisen condensation in your synthesis; Robinson annulation if applicable.
**Tool:** **Claude Project**.

---

**The Prompt:**

```
Chapter 23 of my Synthesis project. Chapter 23 taught:
   - **Aldol condensation**: ketone/aldehyde enolate + a second
     ketone/aldehyde → β-hydroxy carbonyl → (dehydration) → α,β-
     unsaturated carbonyl (enone).
   - **Claisen condensation**: ester enolate + a second ester → β-
     keto ester (Dieckmann is intramolecular version).
   - **Michael addition**: enolate (or any soft nucleophile) +
     α,β-unsaturated carbonyl → conjugate addition at β-carbon.
   - **Robinson annulation**: Michael + aldol = ring construction
     (most famous for steroid synthesis).
Intermolecular vs. intramolecular — intramolecular is usually
preferred when geometry permits (entropy favors ring closure).

Write the brief's "Condensation Section" in 400–600 words.

1. **Identify C-C bonds in your target that could have been
   formed by aldol or Claisen.** Look for:
   - A β-hydroxy ketone (direct aldol product).
   - An α,β-unsaturated ketone (aldol with dehydration).
   - A β-keto ester (Claisen product).
   - A 6-membered ring with an α,β-unsaturated ketone (Robinson
     annulation product).

2. **Propose the aldol step.** For one such bond:
   - The two carbonyl partners.
   - The base used (NaOH, NaOEt, LDA — depending on selectivity
     needs).
   - The product structure (β-hydroxy carbonyl or its dehydrated
     enone).
   - Stereochemistry (aldol gives variable; aldol with chiral
     auxiliaries gives controlled).

3. **Propose the Claisen step (if applicable).** Two esters give
   β-keto ester after deprotonation/addition/loss of OR.

4. **The Michael option.** If your target has a 1,5-dicarbonyl
   pattern or any carbonyl with a β-quaternary carbon, a Michael
   addition might be the disconnection.

5. **Robinson annulation (if applicable).** If your target has a
   6-membered ring with an enone and the right substitution
   pattern, a Robinson annulation is one of organic chemistry's
   most celebrated reactions. Propose the diketone starting
   material and the methyl vinyl ketone or similar Michael
   acceptor.

End with: which condensation in your synthesis would be most
challenging to execute selectively (intermolecular aldol is
notorious for mixed products)?
```

---

**What this produces:** A 400–600 word section. Aldol and Claisen condensations are organic chemistry's most powerful ring-forming reactions.

**Connection to previous chapters:** Ch 22 (enolate formation) and Ch 23 (enolate reactions) are paired.

**Preview of next chapter:** Chapter 24 covers amines and heterocycles. Most drugs contain at least one amine group. You'll propose how each amine in your target gets installed and how any heterocyclic rings get formed.


---

## AI Wayback Machine

**Charles Adolphe Wurtz** was discovered the aldol reaction in 1872 — the carbonyl condensation that organic chemistry students still rehearse.

**Run this:**

```
Who is Charles Adolphe Wurtz, and how does their work connect to carbonyl condensations we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about their career or ideas.
```

→ Search **"Charles Adolphe Wurtz"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to walk through one of Charles Adolphe Wurtz's key experiments or syntheses in detail.
- Add a constraint: "Answer including criticisms or limits of Charles Adolphe Wurtz's framework."

What changes? What gets better? What gets worse?
