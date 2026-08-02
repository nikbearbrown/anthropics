# Chapter 22 — Carbonyl Alpha-Substitution Reactions

*The carbon next to a carbonyl is acidic. That single fact opens up a whole new chemistry — alkylation, halogenation, and the condensation reactions that build the carbon skeletons of natural products.*

The α-carbon — the carbon directly attached to a C=O group — has pKa about 19–25 for most ketones and esters. That's much more acidic than a typical alkane (pKa ≈ 60), but much less acidic than a carboxylic acid (pKa ≈ 5). In between, in a useful range. With strong enough bases, you can deprotonate the α-carbon, generating a carbanion that is stabilized by resonance with the adjacent C=O. This carbanion — called an *enolate* — is a powerful nucleophile that opens up many of the reactions used to build complex carbon skeletons in synthesis.

This chapter is about α-substitution: reactions where an electrophile adds at the α-carbon of a carbonyl compound, replacing the original H. The enolate (or its protonated form, the *enol*) is the key intermediate. The next chapter (23) covers *condensations*, where two carbonyl compounds combine through enolate chemistry to give a larger product. Both chapters use the same fundamental enolate ion as the active nucleophile.

## Keto-enol tautomerism

Most carbonyl compounds with α-hydrogens exist in equilibrium with a small amount of an *enol* tautomer:

$$\text{R-CH}_2\text{-C(=O)-R'} \rightleftharpoons \text{R-CH=C(OH)-R'}$$

The keto form has the H on the α-carbon and a C=O. The enol form has the H on oxygen and a C=C between what was the α-carbon and the carbonyl carbon. Two distinct molecules with the same atoms in different positions — different bonds, different hybridizations.

The equilibrium typically favors the keto form heavily. For acetone, only about 6 × 10⁻⁵ % of the molecules are in the enol form at any moment. For cyclohexanone, about 0.0001%. For most simple ketones, the enol is essentially undetectable at equilibrium.

There are exceptions where the enol is more stabilized. For 2,4-pentanedione (a 1,3-diketone), about 76% of the molecules are in the enol form. The enol has a *six-membered ring* arising from intramolecular H-bonding between the OH and the second C=O, plus extensive conjugation. The stabilization is large enough to flip the equilibrium toward the enol.

The two tautomers are NOT resonance forms. They differ by the position of an actual atom (the H), so they are different molecules in equilibrium. Resonance forms differ only by electron position; tautomers also have a moved atom.

Tautomerism is catalyzed by acid or base. Acid catalysis: protonation of the C=O oxygen gives an oxocarbenium (a protonated ketone), which loses a proton from the α-carbon to give the enol. Base catalysis: deprotonation at the α-carbon by base gives an enolate, which is then protonated on oxygen to give the enol.

Despite their low concentrations, enols are responsible for many ketone reactions because the C=C of an enol is nucleophilic — it can attack electrophiles. The enol form is the reactive form; the keto form is just there to provide the supply.

## Acidity of the α-hydrogen

Why is the α-H acidic? Because deprotonating it gives an enolate that's stabilized by resonance with the adjacent C=O.

Resonance structures of an enolate: the negative charge sits on the α-carbon (with a localized C=O), or it sits on the oxygen (with a C=C connecting α to carbonyl). The actual hybrid is a delocalization across these positions. The negative charge spends some time on each.

The α-H of a typical ketone has pKa around 19. The α-H of an aldehyde is similar (~20). The α-H of an ester is somewhat less acidic (~25) because the ester's C=O is less electron-withdrawing (the ester oxygen donates lone pairs into the C=O via resonance).

When there are *two* C=O groups α to a single CH₂ — a β-diketone, β-ketoester, or β-diester — the α-H is much more acidic because the resulting enolate is doubly stabilized:

| Compound | pKa |
|---|---|
| Acetone | 19.3 |
| Acetaldehyde | 17 |
| Methyl acetate | 25 |
| 2,4-pentanedione (acetylacetone) | 9 |
| Methyl acetoacetate (β-ketoester) | 11 |
| Diethyl malonate (β-diester) | 13 |
| Nitromethane (CH₃NO₂) | 10 |

A β-ketoester or β-diester has pKa low enough (10–13) that hydroxide or alkoxide can fully deprotonate it. This is what makes the malonic ester and acetoacetic ester syntheses (below) practical — you don't need extremely strong bases.

For making ordinary enolates (from simple ketones, etc.), you need a strong base. The standard one is *lithium diisopropylamide* (LDA, pKa of conjugate acid ≈ 36). LDA is strong enough to deprotonate a ketone fully, but weak enough not to cause unwanted side reactions. Other strong, hindered bases include sodium hexamethyldisilazide (NaHMDS, pKa ≈ 30) and lithium tetramethylpiperidide (LiTMP, pKa ≈ 37).

The "hindered" part is important. LDA is bulky. It can grab a proton but can't easily attack a carbonyl carbon as a nucleophile. So when you treat a ketone with LDA, you get clean deprotonation rather than addition to the carbonyl. Hindered bases are essential for clean enolate formation.

## α-Halogenation

A ketone or aldehyde reacts with X₂ (Cl₂, Br₂) to give an α-halogenated carbonyl. The mechanism goes through the enol or enolate intermediate.

Acid-catalyzed mechanism:

1. Protonation of the C=O gives an oxocarbenium.
2. Loss of an α-proton gives the enol.
3. The enol's C=C is nucleophilic and attacks X₂; the C=C electrons go into a new C–X bond, and the X–X bond breaks to leave X⁻.
4. The resulting protonated carbonyl loses a proton to give the α-halogenated product.

Base-catalyzed mechanism:

1. Base removes the α-H, giving an enolate.
2. The enolate attacks X₂; the C–X bond forms and X⁻ leaves.

Acid-catalyzed halogenation gives mono-halogenation cleanly. The first halogenation makes the substrate slightly *more* acidic at the α-carbon (the halogen is electron-withdrawing), so further halogenation could in principle compete — but the new halide also makes the carbonyl less basic (less easily protonated), so the first halogenation wins in practice.

Base-catalyzed halogenation tends to over-halogenate methyl ketones, leading to *trihalo methyl ketones* that then undergo *haloform cleavage* (Chapter 19, but mostly relevant here): the C–C bond breaks and CHX₃ falls off, giving the carboxylic acid.

The Hell-Volhard-Zelinsky (HVZ) reaction halogenates the α-carbon of a *carboxylic acid* (which would otherwise be unreactive under normal halogenation). The mechanism: PBr₃ converts the acid to an acid bromide; the acid bromide is more easily enolized than the acid; the enol gets halogenated; the resulting α-bromoacid bromide is then hydrolyzed to the α-bromoacid. Net result: R-CH₂-COOH + Br₂/PBr₃ → R-CHBr-COOH.

α-Halogenated carbonyls are useful synthetic intermediates. The α-X is a leaving group, which means an α-halogenated ester or ketone can be used in SN2 reactions (the carbonyl makes the α-carbon more reactive, much more reactive than a simple alkyl halide). This is the basis of many alkylation reactions.

## α-Alkylation

The most important α-substitution reaction in synthesis: alkylation of an enolate with an alkyl halide.

$$\text{Enolate} + \text{R'X} \longrightarrow \text{α-alkylated carbonyl} + \text{X}^-$$

Mechanism: the α-carbon of the enolate (which carries partial negative charge from the resonance hybrid) attacks the carbon of the alkyl halide via SN2. Backside attack on R'X with the X⁻ leaving. Carbon–carbon bond formed at the α-position.

Limitations:
- Primary alkyl halides work well. Secondary halides give partial E2 elimination instead. Tertiary halides give clean E2; no useful alkylation product.
- The base must be hindered (LDA, NaHMDS) so it doesn't react with the alkyl halide as a nucleophile.

The reaction is a one-pot two-step procedure: deprotonate the carbonyl (e.g., with LDA at –78 °C in THF), then add the alkyl halide and warm. The result is the α-substituted carbonyl.

For complex carbonyls with multiple α-H's, *regioselectivity* becomes a question. Two possible enolates can form, depending on which α-H is removed. The one that forms first under kinetic control (LDA at low temperature) is usually the *kinetic enolate* — the less substituted one, formed faster because the less hindered α-H is easier for the bulky base to grab. Under thermodynamic control (warmer conditions, weaker base), the more stable *thermodynamic enolate* dominates — the more substituted one. The two give different products on alkylation.

Regiocontrol matters in synthesis. Modern asymmetric alkylations can also give specific stereochemistry at the α-carbon (when the molecule is chiral or when chiral auxiliaries are used).

## The malonic ester synthesis

Diethyl malonate (CH₂(CO₂Et)₂) has α-pKa about 13. NaOEt is strong enough to deprotonate it fully, giving the malonate enolate. Alkylation with R-X gives R-CH(CO₂Et)₂. A second alkylation with R'-X gives R-C(R')(CO₂Et)₂ (if desired). Hydrolysis of the esters gives the disubstituted malonic acid R-C(R')(COOH)₂. Heating decarboxylates one of the COOHs (β-ketoacid-type decarboxylation; the other COOH is technically a β-(C=O) of the first one being lost, plus the resulting carboxylate is stable). The net result: a substituted carboxylic acid R-CH(R')-COOH, two carbons longer than the original alkyl halides started.

This is the canonical method for making substituted acetic acid derivatives. Steps:

1. Diethyl malonate + NaOEt → enolate.
2. Enolate + R-X → R-CH(CO₂Et)₂.
3. (Optional) NaOEt + R'-X → R-CR'(CO₂Et)₂ (a second alkylation).
4. Saponification: NaOH/H₂O → R-CHCOOH-COOH (or R-CR'-COOH-COOH after the second alkylation).
5. Heat (200°C+) → decarboxylation of one COOH → R-CH₂-COOH (or R-CHR'-COOH).

The malonic ester synthesis is one of the cleanest methods for making α-substituted carboxylic acids. It's used widely in pharmaceutical chemistry — barbiturate synthesis, for example, uses malonic ester chemistry.

## The acetoacetic ester synthesis

A close cousin. Methyl acetoacetate (CH₃-CO-CH₂-CO₂Me) has α-pKa about 11. Even more acidic than the malonate (because of the additional ketone C=O). NaOEt deprotonates it fully.

Alkylation with R-X gives CH₃-CO-CHR-CO₂Me. A second alkylation gives CH₃-CO-CR'R-CO₂Me. Hydrolysis of the ester gives the β-ketoacid CH₃-CO-CR'R-COOH. Heating decarboxylates the β-ketoacid (clean β-ketoacid decarboxylation, very favorable) to give CH₃-CO-CR'R-H — a methyl ketone with R and R' on the α-carbon.

So the acetoacetic ester synthesis makes substituted methyl ketones. The sequence:

1. Methyl acetoacetate + NaOEt → enolate.
2. Enolate + R-X → CH₃-CO-CHR-CO₂Me.
3. (Optional) Second alkylation.
4. NaOH/H₂O → β-ketoacid.
5. Heat → CH₃-CO-CHR-H (or CH₃-CO-CR'R-H).

This is the standard method for making α-substituted methyl ketones. Like the malonic ester synthesis, it's a clean one-pot-style sequence (with workup steps in between) that produces a specific structural pattern.

## Stork enamine alkylation

Another α-alkylation method. The enamine (from a secondary amine + aldehyde or ketone, Chapter 19) has a nucleophilic β-carbon (α to the original carbonyl). Alkylation with R-X happens at this β-carbon. Hydrolysis of the enamine regenerates the carbonyl, now α-substituted.

The Stork enamine method works under milder conditions than direct enolate alkylation and tolerates a wider range of substrates. It's particularly useful for ketones that are hard to deprotonate cleanly with LDA.

## α-Halogenation in biology

Biological α-halogenation does occur (mostly in marine organisms, with haloperoxidase enzymes), but the more common biological pattern is α-substitution of a different kind: enolate-electrophile reactions where the electrophile is something like a phosphate, an aldehyde, or an iminium ion. We see this in many enzymatic mechanisms (aldolase, transketolase, citrate synthase, fatty acid biosynthesis).

The active enzymatic intermediate is often a *thioester enolate* — coenzyme A thioesters have α-pKa around 12 (lower than oxoesters because the thioester C=O is more electrophilic and the resulting enolate is more stabilized by the sulfur's polarizability). A thioester enolate is well-suited to react with carbonyl electrophiles in metabolic pathways. Acetyl-CoA is the canonical example.

↳ **Dig Deeper — Why kinetic and thermodynamic enolates differ**

> When a substituted ketone has two different α-H environments, deprotonation can give two different enolates. The kinetic enolate is the less substituted one (formed faster); the thermodynamic enolate is the more substituted one (more stable). Walk through the energetics. Cover: how steric accessibility of α-Hs differs (kinetic side is less hindered), how alkyl substitution stabilizes the more substituted enolate (more like a more substituted alkene), how to choose conditions for kinetic vs. thermodynamic control (temperature, base strength, solvent), and use 2-methylcyclohexanone as the worked example.

**What to do with the output:** Verify the explanation with the 2-methylcyclohexanone case. The kinetic enolate (with LDA at –78 °C) goes to the unsubstituted side; the thermodynamic enolate (with KOH or KOH/EtOH at room temperature) is the more substituted one with the methyl on the enolate side.

## What this chapter does

The α-carbon of a carbonyl compound is acidic (pKa 19–25 for typical aldehydes/ketones/esters; lower for β-dicarbonyls). Deprotonation gives an enolate, a resonance-stabilized carbanion that is nucleophilic at the α-carbon (and at the oxygen, but α-attack typically wins for hard electrophiles).

α-Substitution chemistry includes:
- α-Halogenation: ketone/aldehyde + X₂ + acid or base → α-halo carbonyl. HVZ for carboxylic acids (PBr₃ + Br₂).
- α-Alkylation: enolate (from LDA + carbonyl) + R-X → α-alkylated carbonyl.
- Malonic ester synthesis: substituted acetic acids via diethyl malonate alkylation, hydrolysis, and decarboxylation.
- Acetoacetic ester synthesis: substituted methyl ketones via methyl acetoacetate alkylation, hydrolysis, and decarboxylation.
- Stork enamine alkylation: indirect alkylation via the enamine intermediate.

The keto-enol tautomerism that makes all this chemistry possible has the keto form heavily favored at equilibrium. β-dicarbonyls are exceptions, with substantial enol content due to intramolecular hydrogen bonding and resonance.

The next chapter (23) extends this chemistry to *condensation* — where the enolate attacks another carbonyl compound (rather than an alkyl halide), forming a new C–C bond between two carbonyl-containing units. This is how aldol products, esters from enolates, and many natural products are made.

---

*Source for all data, examples, and historical references: OpenStax* Organic Chemistry*, Chapter 22, modules m00255 through m00262.*
---

## LLM Exercise — Chapter 22: Carbonyl Alpha-Substitution Reactions (Synthesize a Target Molecule Project)

**Project:** Synthesize a Target Molecule.
**What you're building this chapter:** alpha-alkylation steps in your synthesis.
**Tool:** **Claude Project**.

---

**The Prompt:**

```
Chapter 22 of my Synthesis project. Chapter 22 taught: alpha
hydrogens are acidic (pKa ~20-25 for ketone, ~25 for ester, ~30+
for amide); enol vs. enolate (the deprotonated form); LDA (lithium
diisopropylamide, very strong base) deprotonates carbonyls
quantitatively to form enolates; alpha-alkylation (enolate + R-X →
new C-C bond at alpha carbon); kinetic vs. thermodynamic enolates
(LDA at low temp gives kinetic; warmer conditions give
thermodynamic); malonic ester synthesis (CH₂(COOEt)₂ + base + R-X
→ alpha-substituted diester → hydrolysis + decarboxylation gives
RCH₂COOH); acetoacetic ester synthesis (similar with CH₃COCH₂COOEt
giving RCH₂COCH₃).

Write the brief's "Alpha-Alkylation Section" in 400–600 words.

1. **Identify alpha-substitution sites in your target.** Look
   for C-R bonds adjacent to a carbonyl that could have been
   made by alpha-alkylation.

2. **Propose the alpha-alkylation step.**
   - The carbonyl substrate (ketone, aldehyde, ester).
   - The base (LDA, NaH, KOtBu, depending on substrate).
   - The alkyl halide electrophile (R-X).
   - The product.

3. **Regioselectivity (kinetic vs. thermodynamic).** If your
   ketone has two alpha positions:
   - Kinetic enolate (LDA, low temp, -78°C): less-substituted
     alpha.
   - Thermodynamic enolate (NaOEt, room temp): more-substituted
     alpha (more stable conjugated/substituted enol).
   - Choose based on your target.

4. **Malonic ester or acetoacetic ester synthesis.** These are
   "umbrella" strategies for installing alpha-substituents using
   diester or ketoester intermediates:
   - Malonic ester gives carboxylic acids (alpha-substituted).
   - Acetoacetic ester gives ketones (alpha-substituted).
   Many drugs (especially carboxylic-acid-containing) come from
   malonic ester routes.

5. **Draw the mechanism.** Show enolate formation by deprotonation,
   then SN2 alkylation with R-X.

End with: how many alpha-substituents in your target came from
this chapter's chemistry?
```

---

**What this produces:** A 400–600 word section.

**Connection to previous chapters:** Ch 19's carbonyl chemistry, Ch 21's acid-derivative chemistry, Ch 22's alpha-substitution form the carbonyl-chemistry trio.

**Preview of next chapter:** Chapter 23 covers carbonyl condensation reactions — aldol and Claisen — that combine two carbonyl species into a single product with a new C-C bond. Among the most powerful ring-forming reactions in synthesis.


---

## AI Wayback Machine

**Arthur Lapworth** was British chemist who developed the modern theory of carbonyl alpha-substitution in 1903 — the proton transfer step still bears the form he proposed.

**Run this:**

```
Who is Arthur Lapworth, and how does their work connect to carbonyl alpha-substitution we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about their career or ideas.
```

→ Search **"Arthur Lapworth"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to walk through one of Arthur Lapworth's key experiments or syntheses in detail.
- Add a constraint: "Answer including criticisms or limits of Arthur Lapworth's framework."

What changes? What gets better? What gets worse?
