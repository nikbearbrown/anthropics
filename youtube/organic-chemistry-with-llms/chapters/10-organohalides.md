# Chapter 10 — Organohalides

*Halogens turn an inert alkane into a reactive substrate. The C–halide bond is the entry point for almost every multi-step synthesis the rest of this book describes.*

In the deep oceans there are red algae that produce a small molecule called bromoform — CHBr₃ — at industrial-scale rates per organism. Marine sponges synthesize halogenated terpenes that include three chlorines, two bromines, sometimes both, plus various hydroxyl and methyl groups. The Pacific Ocean releases hundreds of thousands of tons of methyl bromide annually from biological sources alone. More than 5,000 organohalide natural products have been characterized, mostly from marine organisms living in halide-rich environments where the metabolic cost of halogenation is low.

This is striking because organohalides have a reputation as "synthetic" — products of human chemistry, not of biology. The reputation is wrong. Halogenation is a real biological strategy, used by enzymes called *haloperoxidases* that generate reactive halogenating species from inorganic halide ions and hydrogen peroxide. The molecules these enzymes produce are sometimes structurally similar to the products of the laboratory halogenation reactions covered in this chapter — though the mechanisms are often different.

But the main importance of organohalides is synthetic. Alkyl halides — compounds with a halogen on an sp³ carbon — are some of the most useful intermediates in all of organic chemistry. They participate in nucleophilic substitutions and eliminations (Chapter 11). They form Grignard reagents and other organometallics that build new C–C bonds. They're used to introduce halogen atoms into target molecules for biological or material applications. The chemistry that starts at "C–halide" and moves through nucleophilic chemistry is the chemistry that builds most pharmaceuticals.

This chapter covers naming, preparation, and a few special reaction types — radical halogenation of alkanes, allylic bromination, and the formation of organometallic reagents. The substitution and elimination reactions of alkyl halides are deferred to Chapter 11.

## Names and structural classes

The IUPAC name for a halogen substituent uses the halogen prefix (fluoro-, chloro-, bromo-, iodo-) with a locant. So 2-bromopentane has Br on C2 of pentane. 1,3-dichlorobutane has Cl on C1 and C3 of butane.

Older common names for some simple alkyl halides survive in the literature:

| IUPAC | Common |
|---|---|
| chloromethane | methyl chloride |
| 2-chloropropane | isopropyl chloride |
| 2-chloro-2-methylpropane | *tert*-butyl chloride |
| bromobenzene | phenyl bromide |
| chloroethene | vinyl chloride |
| 3-bromoprop-1-ene | allyl bromide |

Most contemporary papers use IUPAC names. The common names persist mostly in industrial and historical contexts.

Structural classification: alkyl halides are *primary*, *secondary*, or *tertiary* based on the number of carbons attached to the halogen-bearing carbon (Chapter 3). This classification dominates the chemistry — primary alkyl halides do SN2 well, tertiary do SN1, and so on (Chapter 11). *Vinyl halides* have the halogen on an sp² carbon of an alkene; *aryl halides* have it on an aromatic ring. Vinyl and aryl halides are essentially inert to SN1 and SN2 — the geometry doesn't permit either, and the C–halide bonds are also stronger.

## Industrial importance and applications

About 50 million tons of 1,2-dichloroethane (often called ethylene dichloride) are produced annually, mostly by Cl₂ addition to ethylene. It's then cracked to vinyl chloride (CH₂=CHCl), which is polymerized to polyvinyl chloride (PVC), one of the largest-volume plastics in the world. The pipes carrying water in most American homes, the coverings on most electrical wires, and a good fraction of vinyl flooring are PVC.

Several halogenated solvents have been used at industrial scale and then largely phased out for environmental reasons: chloroform (CHCl₃), carbon tetrachloride (CCl₄), and the chlorofluorocarbons (CFCs). The CFCs were extraordinarily useful — non-toxic, non-flammable, easy to work with, and excellent refrigerants — but their stratospheric chemistry destroys ozone. The Montreal Protocol of 1987 phased them out, and the ozone hole over Antarctica has since slowly contracted. Substitutes (HCFCs, then HFCs, now HFOs and CO₂-based refrigerants) have been adopted with varying environmental trade-offs.

Pharmaceutical applications are too numerous to summarize. A representative example: many antidepressants, antibiotics, and antiviral drugs contain at least one C–halide bond, often on an aromatic ring, where the halogen affects the molecule's electronic properties, lipophilicity, or metabolic stability.

## Radical halogenation of alkanes

Alkanes plus halogens (Cl₂, Br₂) plus light or heat give alkyl halides, by a radical chain mechanism. This is the easiest way to put a halogen on an unfunctionalized carbon, but it has serious limitations.

The mechanism, for chlorination:

**Initiation.** Cl₂ + light (hν) → 2 Cl•. Light splits the Cl–Cl bond homolytically, giving two chlorine radicals.

**Propagation step 1.** Cl• + R–H → HCl + R•. The chlorine radical abstracts a hydrogen atom from the alkane, giving HCl and an alkyl radical.

**Propagation step 2.** R• + Cl₂ → R–Cl + Cl•. The alkyl radical attacks one of the chlorines of Cl₂, taking it to form R–Cl and releasing a new chlorine radical.

The two propagation steps cycle. For each cycle, one alkane is converted to one alkyl halide and one HCl is produced. The chlorine radical at the end of step 2 starts a new cycle.

**Termination.** Eventually, two radicals collide (rather than reacting with substrate) and combine: Cl• + Cl• → Cl₂; R• + Cl• → R–Cl; R• + R• → R–R. These steps consume radicals and slow the chain. Some radicals are always lost to termination, which is why initiation needs to keep producing new ones.

The reactivity of an alkane toward chlorination depends on the C–H bond strength: weaker C–H bonds (allylic, benzylic, tertiary) react fastest; stronger ones (vinyl, methane, primary alkyl) react slowest. The order:

allylic ≈ benzylic > 3° > 2° > 1° > methyl > vinyl

For chlorination of butane, the relative reactivity per H is approximately 1:3.5:5 for primary:secondary:tertiary. For bromination, the differences are much larger: about 1:80:1700. This is because Br• is less reactive (the C–H BDE of HBr is much lower than HCl), so the Br• has more time to discriminate among different C–H bonds and goes preferentially for the weakest one. The Hammond postulate explains this: a less reactive (more endothermic) abstraction has a transition state that resembles the resulting radical, and the more stable radical (tertiary or allylic) gives the lower transition-state energy.

Radical bromination is therefore *more selective* than radical chlorination. Bromination of 2-methylbutane (a tertiary alkane) gives almost exclusively the tertiary bromide. Chlorination gives a mixture of all isomers, weighted by the per-H reactivity factors.

The synthetic limitation: even with the high selectivity of bromination, monohalogenation is hard to control. Once a bromine is in the molecule, the resulting alkyl bromide is more reactive than the starting alkane (because the C–H bonds adjacent to the bromine are weakened), so further halogenation is competitive. The overall result is usually a mixture of mono-, di-, tri-, and possibly higher halogenated products.

For these reasons, radical halogenation of alkanes is rarely the synthesis of choice for a specific alkyl halide. It's a way to make some halogenated material from a cheap alkane (industrial scale) but not a precision tool. For laboratory work, more specific methods are preferred (see below).

## Allylic bromination with NBS

A clean exception to the "radical halogenation is messy" rule. *N*-Bromosuccinimide (NBS) is a reagent that supplies a low, steady concentration of Br₂ for radical bromination. In the presence of a radical initiator (a peroxide, or just light), NBS selectively brominates allylic positions — the C–H bonds next to a C=C double bond.

The mechanism is the standard radical chain, but with two key features:

1. The allylic C–H bond is weakest (because the resulting allylic radical is resonance-stabilized — the unpaired electron can delocalize across the double bond and onto the other allylic carbon). So Br• preferentially abstracts the allylic hydrogen.

2. NBS slowly releases small amounts of Br₂ at low steady-state concentrations. The low Br₂ concentration discourages the radical addition of Br₂ across the C=C double bond (which is an alternate pathway available at higher Br₂ concentrations).

The result: allylic bromination cleanly, without significant addition across the alkene.

Cyclohexene + NBS gives 3-bromocyclohexene (allylic Br) cleanly. This is one of the most commonly used radical halogenations in synthesis.

A subtlety: the allylic radical has two resonance forms, with the unpaired electron on either of the two ends of the original allyl system. So the bromination can happen at either position, giving (in some cases) a mixture of regiochemical products. For symmetric substrates like cyclohexene, it doesn't matter — both positions give the same product. For unsymmetric substrates, you get a mix.

## Preparing alkyl halides from alkenes and alcohols

In Chapter 8 we saw the polar additions that put halogen onto alkenes:
- HX (Markovnikov): alkene + HCl, HBr, or HI gives the alkyl halide with X on the more substituted carbon.
- X₂: alkene + Br₂ or Cl₂ gives a 1,2-dihalide via the bromonium/chloronium ion mechanism, with anti stereochemistry.
- Halohydrin formation: alkene + Br₂ in water gives a 1,2-bromohydrin.
- Radical HBr (with peroxides): alkene + HBr gives the anti-Markovnikov bromide.

All of these are standard preparative routes for alkyl halides. The polar HX addition is most common.

From alcohols, several reagents convert R–OH to R–X:
- HX (HCl, HBr, HI). Works best for tertiary alcohols (which form tertiary cations easily, SN1 mechanism). Primary alcohols often need stronger conditions or different reagents.
- SOCl₂ (thionyl chloride). Converts primary and secondary alcohols to alkyl chlorides cleanly, with retention of configuration via a cyclic intermediate. The byproducts (SO₂ and HCl) are gases and easy to remove.
- PBr₃ (phosphorus tribromide). Converts primary and secondary alcohols to alkyl bromides. Mechanism similar to SOCl₂.
- TsCl (tosyl chloride) + base. Converts the OH to a tosylate, which is then displaced by halide in a separate step. Useful when you need to control the stereochemistry of the displacement.

The choice between these reagents depends on the substrate's structure, the desired stereochemistry, and what other functional groups are present. In a complex synthesis, the SOCl₂/PBr₃ combination is the workhorse.

## Organometallic reagents from alkyl halides

The biggest single use of alkyl halides in synthesis is as a precursor to *organometallic compounds* — molecules with a carbon–metal bond. The two most important kinds:

**Grignard reagents.** R–X + Mg → R–MgX (in dry diethyl ether or THF). The reaction inserts a magnesium atom between the carbon and the halogen, giving an organometallic with a polarized C–Mg bond. The carbon now bears a partial negative charge and behaves as a nucleophilic carbanion equivalent.

Grignards add to carbonyl compounds (Chapter 19), to epoxides, to nitriles, and to a few other electrophiles. They form new C–C bonds. They've been a staple of synthesis since their discovery by Victor Grignard in 1900 (Nobel Prize in 1912).

The reaction is sensitive to moisture: any water immediately destroys the Grignard reagent (R–MgX + H₂O → R–H + Mg(OH)X). Glassware, solvents, and atmospheres must be dry.

A subtle but useful point: a Grignard reacts as if it were a carbanion (the R⁻ part attacking the electrophile), but it's really a polar covalent compound. The C–Mg bond polarity makes the carbon nucleophilic. The actual reactivity is often described as if the R⁻ were a free carbanion, even though it isn't.

**Organolithium reagents.** R–X + 2 Li → R–Li + LiX. Like a Grignard but more reactive. Organolithiums are often more useful than Grignards when extra nucleophilic strength is needed. They form via a similar electron-transfer mechanism.

Organolithium and Grignard reagents are similar but not identical. Both are nucleophilic at carbon. Both are very basic (pKa of the conjugate acid R–H is around 50, so R⁻ is essentially the deprotonated form of an alkane). Both react with water, alcohols, amines, and other O–H/N–H acids — so substrates with such groups must be protected first.

The synthesis of an alkyl halide is therefore the entry point for *making a new C–C bond*. From R–X you get R–MgX, which adds to a carbonyl to give a new C–C bond and a new alcohol. From there, the rest of organic chemistry opens up.

## Coupling reactions: the modern era

A more recent and immensely useful class of organometallic reactions builds C–C bonds by *cross-coupling* an alkyl or aryl halide with another organometallic in the presence of a transition metal catalyst.

The Suzuki coupling (Pd-catalyzed coupling of an aryl halide with an arylboronic acid), the Heck coupling (Pd-catalyzed coupling of an aryl halide with an alkene), and the Negishi coupling (Pd-catalyzed coupling of an aryl halide with an alkylzinc) are some of the most-used reactions in modern synthesis. The 2010 Nobel Prize in chemistry went to Heck, Negishi, and Suzuki for their development of these reactions.

These reactions are not covered in detail in OpenStax Organic Chemistry, but the existence of the chemistry should be known: alkyl and aryl halides are starting materials for cross-coupling chemistry, and the cross-coupling chemistry is often the easiest way to assemble complex aromatic and heteroaromatic compounds in synthesis.

↳ **Dig Deeper — Why bromination is more selective than chlorination**

> The Hammond postulate explains why radical bromination strongly prefers the most stable C–H site (relative reactivity 1:80:1700 for 1°:2°:3°), while chlorination is much less selective (1:3.5:5). Walk through the energetics. Cover: the C–H BDEs of HCl (432 kJ/mol) and HBr (366 kJ/mol), why the H abstraction step is endothermic for bromination but exothermic for chlorination, how this affects the position of the transition state along the reaction coordinate, and how that translates into selectivity differences between the two halogens.

**What to do with the output:** Verify that Claude correctly applies the Hammond postulate to identify which transition state (early vs. late) gives more selectivity. The chlorination case has an early transition state (reactant-like), the bromination case a late one (product-like, resembles the radical) — that's why bromination discriminates.

## What this chapter does

Alkyl halides are the entry point for most of the substitution and elimination chemistry of Chapter 11, and for the organometallic chemistry that builds new C–C bonds throughout the rest of the book. The C–halide bond is polar (carbon δ+), making the carbon electrophilic and accessible to nucleophilic attack. The halide is a good leaving group, especially as you go down the column: I > Br > Cl >> F.

Preparation methods include:
- Alkene additions (HX, X₂, halohydrin formation) — the most common and reliable route.
- Alcohol conversion (SOCl₂, PBr₃, HX, TsCl) — the second most common.
- Radical halogenation of alkanes — useful only in specific cases (allylic/benzylic NBS, industrial scale).

Once made, alkyl halides feed into:
- SN1, SN2, E1, E2, E1cB chemistry (Chapter 11).
- Grignard and organolithium reagent formation, then C–C bond formation.
- Cross-coupling reactions (Suzuki, Heck, Negishi).
- Direct industrial use as solvents, polymers (PVC), and pharmaceuticals.

This is a relatively short chapter because most of the chemistry of halides is *applied* in other chapters. The next chapter (Chapter 11) is the canonical case — where a half-dozen reactions converge on the alkyl halide as substrate.

---

*Source for all data, examples, and historical references: OpenStax* Organic Chemistry*, Chapter 10, modules m00112 through m00120.*
---

## LLM Exercise — Chapter 10: Organohalides (Synthesize a Target Molecule Project)

**Project:** Synthesize a Target Molecule.
**What you're building this chapter:** identify alkyl-halide intermediates in your synthesis; propose a Grignard step if relevant.
**Tool:** **Claude Project**.

---

**The Prompt:**

```
Chapter 10 of my Synthesis project. Prior sections in this Claude
Project. Chapter 10 taught: alkyl halide nomenclature (1°, 2°, 3°);
preparation methods (radical halogenation; allylic bromination
with NBS); Grignard reagents (R-Mg-X, an organomagnesium
nucleophile/carbon-nucleophile) made from alkyl halide + Mg metal;
the Grignard's broad utility — adds to carbonyls, epoxides, CO₂,
nitriles, halides.

Write the brief's "Alkyl Halide + Grignard Step" section in
300–500 words.

1. **Identify the C-C bonds in your target that COULD come from
   a Grignard addition.** A Grignard adds to a carbonyl to make
   a new C-C bond + an alcohol. Look for alcohols (especially
   tertiary alcohols) adjacent to a carbon that could have been
   the carbonyl.

2. **Propose the Grignard step.** For one such C-C bond:
   - The alkyl halide (precursor to the Grignard).
   - Mg activation conditions.
   - The carbonyl electrophile.
   - The product (the new C-C bond + the alcohol).

3. **Where does the alkyl halide come from?** Trace back further:
   - From an alcohol (via SOCl₂ or PBr₃, Ch 17).
   - From an alkene (via HX or HBr addition, Ch 8).
   - From a hydrocarbon (via radical halogenation, but selectivity
     is often poor unless the position is allylic or benzylic).

4. **The Grignard's incompatibilities.** Grignards react with:
   - Water and alcohols (they'll be quenched).
   - Carboxylic acids (similar reason).
   - Aldehydes, ketones, esters (the desired reaction — but other
     such groups in the molecule will be attacked too).
   - Even amides and nitriles (which themselves contain C=O or
     C≡N).

   So a Grignard step must come BEFORE you install any of these
   incompatible functional groups, OR they must be protected
   first. Note any incompatibilities in your target's emerging
   synthesis.

5. **Update the retrosynthesis.** Add this step to the chain.
   The chain should now go: ... starting materials → ... → C-C
   bond formed by Grignard → ... → target.

End with: would a Grignard be the BEST choice for this specific
bond, or would an alternative (acetylide, enolate, organocuprate)
be better? Defend your choice.
```

---

**What this produces:** A 300–500 word section adding the Grignard step. The functional-group-incompatibility check is a real retrosynthesis discipline that students often skip.

**How to adapt this prompt:**

- *For your own project:* If your target has multiple alcohols, multiple Grignard steps may be needed. Or one Grignard that's done before functional groups conflict.
- *For ChatGPT / Gemini:* Works as written.
- *For Claude Code:* Not the primary tool here.
- *For a Claude Project:* Append.

**Connection to previous chapters:** Ch 8 (alkene-to-halide) + Ch 9 (acetylide alternative) + Ch 10 (Grignard pathway) form the C-C-bond-forming triad.

**Preview of next chapter:** Chapter 11 turns to substitution and elimination reactions. You'll choose conditions for desired SN1/SN2/E1/E2 outcomes in your synthesis and predict stereochemistry.


---

## AI Wayback Machine

**Victor Grignard** was discovered the organomagnesium halide reagents bearing his name in 1900 — Nobel 1912.

**Run this:**

```
Who is Victor Grignard, and how does their work connect to organohalides we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about their career or ideas.
```

→ Search **"Victor Grignard"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to walk through one of Victor Grignard's key experiments or syntheses in detail.
- Add a constraint: "Answer including criticisms or limits of Victor Grignard's framework."

What changes? What gets better? What gets worse?
