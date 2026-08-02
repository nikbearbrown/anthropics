# Chapter 8 — Alkenes: Reactions and Synthesis

*Almost every alkene reaction follows the same two-step pattern: electrophile attacks the π bond to form a cation, nucleophile captures the cation. The variations are in what plays each role and what stereochemistry results from the geometry.*

The C=C double bond is the most heavily exploited functional group in synthetic organic chemistry. There are at least a dozen well-established ways to add things across an alkene, each one giving a different product with a different regiochemistry and stereochemistry. Some give Markovnikov products, some give anti-Markovnikov products. Some go syn (both new groups on the same face of the alkene), some go anti (on opposite faces). Some give racemic mixtures, some give single stereoisomers.

This bewildering variety, taught one reaction at a time, is the standard reason students hate sophomore organic chemistry. Taught with the underlying mechanism made central, it becomes manageable. Almost every reaction in this chapter follows the polar-addition pattern from Chapter 7: an electrophile picks up the π electrons, forming a carbocation (or a related electrophilic intermediate); a nucleophile then attacks. The differences between reactions come from:

1. Which electrophile delivers the first attack.
2. What kind of cation (or cation-like intermediate) forms — open carbocation, three-membered halonium ring, mercurinium ion, boron-bridged species.
3. What nucleophile arrives in step 2.
4. What stereochemistry the geometry of the intermediate forces on the product.

Once you can read those four variables for each reaction, the chapter becomes a small handful of patterns rather than fifteen separate facts.

## Hydrohalogenation: addition of HX

The simplest case. An alkene plus HX (X = Cl, Br, I) gives an alkyl halide. The mechanism is the canonical two-step polar addition:

1. The π electrons attack H of HX. The H–X bond breaks heterolytically, leaving X⁻. The carbon that picks up the H stays neutral (now sp³, with the new C–H bond); the other carbon is left with an empty p orbital and a +1 formal charge — a carbocation.
2. The X⁻ ion, attracted to the cation, donates a lone pair to form a C–X bond.

Markovnikov's rule controls regiochemistry: the H ends up on the less-substituted carbon (the carbon with more H's already), and X ends up on the more-substituted carbon. Why: the more-substituted cation is the more stable one, so the H goes wherever leaves the more-substituted carbon as the cation site.

A small twist: if the alkene is allylic or benzylic, the resonance-stabilized cation may form preferentially even if it's nominally "less substituted." The general rule is *the most stable cation wins*, with substitution and resonance both contributing.

The stereochemistry of HX addition is *not* particularly clean. The cation intermediate is sp² and planar; X⁻ can attack from either face. So if the alkene was a single stereoisomer that gave a chiral product, you usually get a racemic mixture — the reaction has scrambled the stereochemistry at the new stereocenter.

## Halogenation: addition of X₂

Adding Cl₂ or Br₂ to an alkene gives a 1,2-dihalide. Industrial scale: roughly 50 million tons of 1,2-dichloroethane (used to make vinyl chloride and then PVC) is produced this way each year.

The mechanism is mildly different from the HX case. The π electrons attack the halogen (say Br₂), pushing the σ bond's electrons onto the leaving Br. The result is a *cyclic bromonium ion* — a three-membered ring with Br at the bridging position, sharing a bond to both carbons of what was the alkene. The Br has a +1 formal charge.

Why a cyclic intermediate instead of an open carbocation? Because Br has a lone pair that, with the new C–Br bond, can form a second weak bond to the other carbon. The three-membered ring is more stable than the corresponding open carbocation would be. (For Cl₂, the chloronium ion is similar but somewhat less common; for I₂, iodonium ions are very stable.)

The bromide ion (Br⁻) generated in the first step then attacks the bromonium ion. Crucially, it attacks from the side opposite the Br — the same kind of backside attack you saw in SN2 reactions in Chapter 11. The result is *anti* addition: the two Br's end up on opposite faces of what was the alkene.

The stereochemistry consequence: addition of Br₂ to cyclohexene gives only the *trans*-1,2-dibromide. The cis isomer is not formed. This is an experimental signature for the bromonium-ion mechanism — clean anti addition, every time, on every substrate where the alkene's geometry permits it.

## Halohydrin formation

If you do bromination in water (instead of in inert solvent), the cyclic bromonium ion forms first as before — but then water, not bromide, gets to the substrate first because there's so much more of it. Water attacks the bromonium ion, opening the ring at the more substituted carbon (this is where the most positive charge resides) and giving a *halohydrin* — a compound with both an OH and an X on adjacent carbons.

So Br₂ + alkene + H₂O gives a 1,2-bromohydrin. The OH ends up on the more substituted carbon (Markovnikov pattern, because that's where the bromonium ion has the most + character) and the Br ends up on the less substituted carbon. The two new groups are added anti, because water still attacks the bromonium ion from the back side.

Halohydrins are useful synthetic intermediates and they're also produced biologically. *Haloperoxidase* enzymes generate hypohalous acids (HOX) and similar reactive species that halogenate marine natural products with structures that suggest halonium-ion intermediates.

## Acid-catalyzed hydration

Add water across an alkene with H₂SO₄ catalysis, and you get an alcohol. Mechanism: the H₂SO₄ protonates the alkene (electrophilic addition of H⁺), giving a carbocation. Water then attacks the cation, giving a protonated alcohol (R–OH₂⁺). A proton is then lost to give the neutral alcohol.

Markovnikov regiochemistry: OH ends up on the more substituted carbon. (More substituted cation forms preferentially; water attacks that carbon.)

Industrial scale: about 300,000 tons of ethanol per year are made by acid-catalyzed hydration of ethylene (this is actually a small fraction of total ethanol production; most ethanol is fermented from sugars or starches).

This method has limitations. The acidic conditions are harsh enough to promote rearrangements and side reactions when the substrate is sensitive. The reaction is not stereospecific — the cation intermediate is planar, water can attack either face, so a chiral product comes out racemic.

## Oxymercuration: a softer Markovnikov hydration

When you want the Markovnikov product but can't use strong acid, oxymercuration is the workaround. Treating an alkene with Hg(OAc)₂ in water forms a *mercurinium ion* — analogous to the bromonium ion, but with Hg bridging the two carbons. Water attacks the mercurinium ion at the more substituted carbon, giving (after proton loss) a β-hydroxymercuric compound. This is then reduced with NaBH₄, replacing the Hg with H, leaving an alcohol.

Net result: Markovnikov hydration without strong acid. Used in synthesis when the substrate has acid-sensitive groups elsewhere.

The stereochemistry is anti — the mercurinium ion forces backside attack of water, just like the bromonium ion forces backside attack of bromide.

## Hydroboration: anti-Markovnikov hydration

For the *anti*-Markovnikov hydration product — OH on the less substituted carbon, opposite of what acid-catalyzed hydration or oxymercuration give — you need a different mechanism. The standard solution is *hydroboration–oxidation*, developed by H. C. Brown at Purdue.

Step 1: the alkene reacts with borane (BH₃, often as the BH₃·THF complex) or a substituted borane (9-BBN, disiamylborane, etc.). The B–H bond adds across the double bond in a single concerted step. Boron, less electronegative than hydrogen, ends up on one carbon while H goes to the other. There is no carbocation intermediate; the addition is concerted, with both new bonds forming simultaneously on the same face of the alkene.

Boron prefers the less hindered carbon — *anti*-Markovnikov regiochemistry. The reason is partly steric (boron is large, the bulkier substituents push it toward the smaller carbon) and partly electronic (the transition state has some carbon-positive character on the less hindered carbon, where it's better stabilized).

Step 2: the resulting trialkylborane is treated with H₂O₂ in basic aqueous solution. Each C–B bond is replaced with a C–OH bond, with retention of configuration at carbon (the boron leaves and is replaced from the same face — there's no carbocation intermediate, no scrambling).

Net result: the alkene has been converted to an alcohol with the OH on the less substituted carbon, with both H and OH added on the same face (syn addition).

So hydroboration–oxidation and acid-catalyzed hydration are complementary: same overall transformation (alkene → alcohol), opposite regiochemistry, opposite stereochemistry.

## Catalytic hydrogenation

H₂ adds across an alkene in the presence of a transition metal catalyst (Pt, Pd, or Rh, often supported on carbon or alumina) to give an alkane. The mechanism is heterogeneous: H₂ molecules adsorb to the metal surface and dissociate into individual H atoms; the alkene also adsorbs to the surface; the H atoms migrate to the alkene's carbons. Both H's end up on the same face of the alkene because the catalyst surface delivers them together — *syn* addition.

This reaction is the standard way to "saturate" a double bond — to remove the unsaturation entirely. It's used industrially in the conversion of vegetable oils (which contain cis double bonds in the fatty acid chains) into solid fats (the saturated, fully hydrogenated versions). Margarine is partially hydrogenated vegetable oil.

A complication: the hydrogenation can sometimes leave the alkene's double bond in a different place than where it started, because intermediate metal–alkyl species can do β-hydride elimination and re-insert. This isomerization is the origin of *trans* fats — partial hydrogenation of cis-alkenes can produce trans-alkenes, which are not the thermodynamic preference but are kinetically accessible.

Alkenes are far more reactive toward catalytic hydrogenation than most other functional groups, which makes selective hydrogenation possible: you can reduce a C=C without touching a C=O or a C–halide elsewhere in the molecule.

## Hydroxylation: adding two OH groups

For a 1,2-diol product (also called a *vicinal diol* or a glycol), several reagents work.

*Cold dilute KMnO₄* in basic solution gives a *cis-1,2-diol* in clean syn addition. The mechanism is a cyclic permanganate intermediate that delivers both oxygens to the same face. KMnO₄ is also a strong oxidant in other modes, so this reaction has to be controlled (cold, dilute) to stop at the diol.

*OsO₄* (osmium tetroxide) gives the same result — cis-diol via a cyclic osmate intermediate — and is more reliable, though osmium is toxic. OsO₄ is often used catalytically with N-methylmorpholine-N-oxide (NMO) as a stoichiometric reoxidant.

For a *trans-1,2-diol*, you go through an epoxide first (see below) and then hydrolyze it.

## Epoxidation: oxygen across the double bond

A *peroxyacid* — typically meta-chloroperoxybenzoic acid (mCPBA) — transfers an oxygen atom to an alkene to give an *epoxide* (a three-membered ring with one O and two C).

The mechanism is concerted: in a single step, the peroxyacid's O–O bond breaks while two new bonds form between the oxygen and the two alkene carbons. Both new bonds form on the same face — clean syn addition.

Epoxides are useful intermediates because they can be opened by nucleophiles. If you epoxidize an alkene with mCPBA and then open the epoxide with water (or another nucleophile) under acid or base catalysis, you get a *trans*-1,2-diol (or other trans-1,2-substituted product), because the nucleophile attacks the back side of the epoxide carbon, inverting the stereochemistry at that carbon.

So: alkene → epoxide → diol gives the trans diol; alkene → KMnO₄ or OsO₄ gives the cis diol. Two different paths, two different stereoisomers of the same overall product.

## Ozonolysis: cleaving the double bond

For oxidative cleavage of an alkene, *ozone* (O₃) is the standard reagent. Treating an alkene with O₃, then reducing the resulting ozonide with Zn/H₂O or (CH₃)₂S, cleaves the C=C bond and gives two carbonyl compounds — aldehydes from terminal alkenes (or RHC=CHR groups), ketones from R₂C=CR₂ groups.

The mechanism goes through a cyclic *ozonide*, which is then reductively cleaved. The reaction is mainly diagnostic — it lets you locate a double bond in a complex molecule by cleaving it and identifying the fragments. Modern alternatives (cleavage with OsO₄/NaIO₄, for instance) are sometimes preferred for specific substrates.

## Carbene addition: making cyclopropanes

A *carbene* is a divalent carbon species, R₂C: with only six valence electrons. Carbenes are very reactive — they add to alkenes in a single concerted step to form cyclopropanes.

The most common laboratory carbene source is the Simmons–Smith reagent: CH₂I₂ + Zn(Cu), which generates an "iodomethylzinc iodide" species (I–CH₂–ZnI) that reacts as if it were a methylene carbene equivalent (:CH₂). The resulting product is a cyclopropane with both new C–C bonds formed in a syn manner.

Other carbenes (CCl₂, CBr₂, etc.) come from various base-induced eliminations of CHCl₃, CHBr₃, and similar precursors. They give halocyclopropanes when added to alkenes.

## Radical addition of HBr (anti-Markovnikov!)

A historical curiosity worth knowing. When HBr is added to an alkene in the presence of a peroxide (e.g., benzoyl peroxide), the regiochemistry reverses: Br ends up on the *less* substituted carbon, anti-Markovnikov.

Why? The peroxide initiates a radical chain mechanism. Instead of the polar two-step addition, the reaction goes:

1. Peroxide produces RO• radicals.
2. RO• abstracts H from HBr, producing Br• (a bromine radical) and ROH.
3. Br• adds to the alkene. It adds to whichever carbon gives the more stable carbon radical — the more substituted one. This places Br on the less substituted carbon.
4. The resulting carbon radical abstracts H from another HBr molecule, giving the product and a new Br•, which propagates the chain.

So the radical mechanism gives the anti-Markovnikov regiochemistry because radicals (like cations) are more stable when more substituted, and the radical forms by Br attacking the *less* substituted carbon.

This is the only common addition that flips regiochemistry by switching mechanism. It only works for HBr (HCl, HF, and HI don't undergo this radical chain effectively) and only with peroxides as initiators.

↳ **Dig Deeper — Why each reagent prefers a particular face**

> The stereochemistry of alkene additions is determined by the geometry of the intermediates: open cation gives mixed stereo; bromonium ion gives anti; concerted syn addition (hydroboration, hydrogenation, mCPBA) gives syn. Take each of: HX addition, Br₂ addition, hydroboration-oxidation, mCPBA epoxidation, KMnO₄ hydroxylation, and explain why the geometry of the intermediate forces the observed stereochemistry. Cover where each new bond is forming relative to the alkene plane in the rate-determining step.

**What to do with the output:** Compare against any organic textbook table of alkene reactions and stereochemistry. Verify that Claude correctly identifies which reactions are "stereospecific" (forced by the mechanism) versus "stereoselective" (preferred but not required).

## A summary table of alkene additions

The patterns to memorize are easier when seen side by side:

| Reaction | Reagent | Adds | Regio | Stereo |
|---|---|---|---|---|
| Hydrohalogenation | HCl, HBr, HI | H, X | Markovnikov | mixed (cation) |
| Halogenation | Br₂, Cl₂ | X, X | – | anti (halonium) |
| Halohydrin formation | Br₂ + H₂O | Br, OH | Markov OH | anti (halonium) |
| Acid hydration | H₂O, H⁺ | H, OH | Markovnikov | mixed (cation) |
| Oxymercuration | Hg(OAc)₂, H₂O, NaBH₄ | H, OH | Markovnikov | anti |
| Hydroboration–oxidation | BH₃, then H₂O₂/HO⁻ | H, OH | anti-Markovnikov | syn |
| Hydrogenation | H₂, Pt | H, H | – | syn |
| Hydroxylation | OsO₄ or KMnO₄ (cold, dilute) | OH, OH | – | syn |
| Epoxidation | mCPBA | O | – | syn |
| Cleavage | O₃, then Zn/H₂O | – | – | cleaves bond |
| Carbene addition | CH₂I₂/Zn(Cu) | CH₂ | – | syn |
| Radical HBr | HBr, peroxide | H, Br | anti-Markovnikov | mixed |

If you can predict every cell of this table from the underlying mechanism (which intermediate, what geometry, what regiochemistry rule applies), you've internalized alkene chemistry.

## Synthetic strategy with alkenes

The complementary nature of these reactions is the synthetic chemist's toolkit. If you need a Markovnikov alcohol with no rearrangement, oxymercuration. If you need anti-Markovnikov, hydroboration. Cis-1,2-diol — KMnO₄ or OsO₄. Trans-1,2-diol — epoxide and hydrolyze. Cyclopropane — carbene. Cleave at a specific position — ozonolysis. Each transformation has a regiochemistry and stereochemistry; once you know them, you select reagents to get the target.

In Chapter 9, we see the same kinds of additions on alkynes (with some differences arising from the second π bond). In Chapter 10, we shift to halides and see the eliminations that *make* alkenes (the reverse direction). Most of the rest of the book builds on the additions and eliminations introduced in Chapters 7, 8, 10, and 11.

## What this chapter does

Polar additions to alkenes follow a near-universal pattern: an electrophile attacks the π bond, generating a carbocation or cation-like intermediate; a nucleophile then captures that intermediate. The variations across reactions are in the identity of the electrophile (H⁺, Br⁺, Hg²⁺, B–H), the nature of the intermediate (open cation, three-membered halonium ring, mercurinium ion, four-membered B–C–C–H transition state), and the source of the nucleophile (X⁻, water, peroxide).

The stereochemistry comes from the geometry of the intermediate. Open cations give mixed stereo; cyclic halonium and mercurinium ions force anti addition; concerted reactions with no real intermediate (hydroboration, hydrogenation, mCPBA) give syn addition.

The regiochemistry comes from which carbocation (or cation-like species) is most stable. Markovnikov's rule, restated as "the most stable cation wins," is the operating principle. The exception is the radical-chain HBr addition, where radical stability (rather than cation stability) controls regiochemistry — and radicals follow the same substitution-stability ranking, but the bromine attacks first instead of the hydrogen.

Once these patterns are clear, the table of alkene reactions becomes a small handful of mechanistic ideas applied to different substrates. The next chapter does the same for alkynes — same mechanism logic, slightly different geometry, two π bonds to work through instead of one.

---

*Source for all data, examples, and historical references: OpenStax* Organic Chemistry*, Chapter 8, modules m00088 through m00101.*
---

## LLM Exercise — Chapter 8: Alkenes — Reactions and Synthesis (Synthesize a Target Molecule Project)

**Project:** Synthesize a Target Molecule.
**What you're building this chapter:** propose one synthetic step using an alkene reaction to construct part of your target.
**Tool:** **Claude Project**.

---

**The Prompt:**

```
Chapter 8 of my Synthesis project. Prior sections in this Claude
Project. Chapter 8 taught: electrophilic addition to alkenes
(Markovnikov regiochemistry: H goes to the carbon with more
H's, the carbocation forms at the more-substituted carbon); HX
addition; acid-catalyzed hydration; halogenation (anti addition,
trans halohydrin formation); hydroboration-oxidation (anti-
Markovnikov, syn addition); hydrogenation (syn addition);
oxidation (epoxidation with mCPBA; dihydroxylation with OsO₄
syn or KMnO₄; ozonolysis cleaves the C=C bond).

Write the brief's "Alkene-Based Synthetic Step" section in
400–600 words.

1. **Pick one specific bond or functional group in your target
   that could be made via an alkene reaction.** Examples:
   - An alcohol could come from hydration or hydroboration-oxidation.
   - An alkyl bromide could come from HBr addition.
   - A halohydrin could come from halogenation in water.
   - A vicinal diol could come from dihydroxylation.
   - A C-C bond cleavage could come from ozonolysis (reverse-
     engineering the starting alkene).

2. **Write the proposed step.** Starting material (the alkene
   precursor) → product (the functional group in your target's
   pathway). Show the reagents and conditions.

3. **Predict regiochemistry.** Markovnikov or anti-Markovnikov?
   What does the mechanism predict? Sketch the carbocation
   intermediate if applicable.

4. **Predict stereochemistry.** Syn or anti addition? What does
   the mechanism predict? Note any chiral products that would
   be racemic (Markovnikov + 2° carbocation = racemic) vs.
   stereospecific (hydroboration = syn = single diastereomer).

5. **Draw the mechanism with arrows.** Push electrons from
   nucleophile (alkene's pi bond) to electrophile (proton, halogen,
   or oxidant). Show every intermediate and the bond-forming/
   bond-breaking arrows.

6. **The retrosynthesis update.** Add this step to your running
   retrosynthesis. Where does the alkene precursor come from?
   This is the next disconnection — defer to a later chapter or
   resolve immediately if obvious.

End with: which other alkene reaction would have been an alternative
for this same transformation, and why did you choose the one you
did? (Bias is a real risk in retrosynthesis — naming alternatives
forces honest analysis.)
```

---

**What this produces:** A 400–600 word Alkene Step section with a proposed reaction, mechanism arrows, and regiochemistry/stereochemistry analysis. This is the first real "synthesis step" in the project.

**How to adapt this prompt:**

- *For your own project:* If your target doesn't naturally have an alkene-step precursor, propose one anyway — many targets have hidden alkene intermediates that simplify retrosynthesis.
- *For ChatGPT / Gemini:* Works as written.
- *For Claude Code:* Optional — RDKit can verify the connectivity of proposed intermediates.
- *For a Claude Project:* Append.

**Connection to previous chapters:** Ch 6 set up retrosynthesis logic; Ch 8 contributes the first concrete step.

**Preview of next chapter:** Chapter 9 covers alkynes. Acetylide alkylation is a powerful C-C bond-forming move that builds 2-carbon chains. If your target needs a chain extension at any point, the alkyne approach is a candidate.


---

## AI Wayback Machine

**Karl Ziegler** was developed transition-metal catalysts for alkene polymerization with Giulio Natta — Nobel 1963.

**Run this:**

```
Who is Karl Ziegler, and how does their work connect to alkene reactions and synthesis we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about their career or ideas.
```

→ Search **"Karl Ziegler"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to walk through one of Karl Ziegler's key experiments or syntheses in detail.
- Add a constraint: "Answer including criticisms or limits of Karl Ziegler's framework."

What changes? What gets better? What gets worse?
