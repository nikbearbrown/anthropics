# Chapter 11 — Reactions of Alkyl Halides: Nucleophilic Substitutions and Eliminations

*The carbon–halogen bond has four ways to break, and which one wins tells you almost everything about how organic chemistry works.*

In 1896, Paul Walden did something that bothered chemists for forty years. He took a sample of pure (−)-malic acid, ran it through two chemical steps, and got back malic acid — except now it rotated polarized light in the opposite direction. Same molecule. Wrong hand. Somewhere in the two steps, the spatial arrangement around a carbon atom had flipped. Fischer called it "the most remarkable observation in optical activity since Pasteur."

Walden knew something had inverted. He did not know which step, or why, or how. That took until 1937, when Hughes and Ingold worked it out, and the answer turned out to be one of the most satisfying mechanisms in all of chemistry. The same year, more or less, chemists also understood that alkyl halides could do something completely different — instead of swapping one group for another, they could lose a small piece of themselves and grow a double bond.

This chapter is about both processes. They share the same starting material. They share some of the same intermediates. And yet they produce completely different products, by mechanisms that are almost philosophical opposites. Once you understand why, you'll have the core of mechanism-based reasoning for the rest of organic chemistry.

## The first mechanism: backside attack

Start with the simplest possible case. Methyl bromide plus hydroxide gives methanol plus bromide. The oxygen swaps in, the bromine swaps out.

Measure the rate, and you find:

$$\text{rate} = k\,[\text{CH}_3\text{Br}]\,[\text{HO}^-]$$

Both concentrations matter. Double either one and the rate doubles. That means both species are involved in the step that controls the rate — there's a collision that requires both of them. The mechanism has one step, and both players are in it.

Now take a chiral version of this — (S)-2-bromobutane — and let hydroxide attack. The product is (R)-2-butanol. The configuration has inverted. This is Walden's puzzle, but now on a substrate simple enough to track.

Hughes and Ingold's proposal accounts for both observations at once. The nucleophile attacks from directly behind the leaving group — 180° away. As the new C–O bond forms, the old C–Br bond breaks. No intermediate. One transition state. At the moment of maximum crowding, the three remaining groups on the carbon have flattened into a plane, and carbon is briefly five-coordinate. Then the whole thing snaps through, like an umbrella inverting in a gust of wind, and the configuration is opposite to what it was.

This is SN2 — substitution, nucleophilic, bimolecular. The name is just a label for the mechanism, but the mechanism is why the name is what it is.

The geometry forces the inversion, and the geometry also explains rate differences across substrates. Methyl halides react fastest, because the back side of the carbon is completely open. Primary substrates are next. Secondary are slower. Tertiary are essentially inert — three alkyl groups block the approach trajectory so thoroughly that the activation energy becomes prohibitive. No backside attack reaches the carbon. The reaction just doesn't happen. This is not a continuous trend where tertiary halides are "slow"; it's a cliff. Tertiary substrates do not do SN2.

Branching one carbon away from the reacting center matters too. Neopentyl bromide — a primary halide with a *tert*-butyl group one carbon over — reacts sluggishly because the methyl groups project outward and obstruct the approach even from a distance. The nucleophile is trying to thread a needle; the geometry of the substrate is the needle's eye.

Four variables govern SN2 rates: the substrate (sterics), the nucleophile, the leaving group, and the solvent.

On nucleophiles: within the same row of the periodic table, nucleophilicity tracks with basicity — better bases are better nucleophiles. But going down a column of the periodic table, nucleophilicity increases while basicity decreases. Iodide is a far better nucleophile than fluoride, even though fluoride is the stronger base. The reason is polarizability: larger atoms have loosely held valence electrons that distort easily and form the new bond more readily. The actual rate data are striking — water and cyanide differ by about five orders of magnitude in how fast they react with methyl bromide. The nucleophile matters enormously.

On leaving groups: a good leaving group is one that's stable as a free anion. This is the same logic as acid strength — the stronger the acid H–X, the more stable the X⁻, and the better the leaving group. Tosylate and iodide are excellent. Bromide and chloride are good. Fluoride is poor. Hydroxide is essentially never a leaving group — its conjugate acid, water, has a pKa of 15.7, meaning the anion is too high in energy to depart spontaneously. Amines don't leave at all. To run SN2 on an alcohol, you have to convert the −OH into something else first — typically a tosylate, a bromide, or a chloride — before the reaction will go.

On solvent: this is the sneakiest variable. Protic solvents — those with O–H or N–H bonds — surround anions with hydrogen bonds, stabilizing them in the ground state and raising ΔG‡ for the SN2 reaction. The nucleophile has to shed its solvent cage before it can attack. Polar aprotic solvents — DMSO, DMF, acetonitrile — solvate cations well but leave anions relatively naked. The nucleophile sits with a high ground-state energy and a low barrier to reaction. The same pair of molecules can react 200,000 times faster in HMPA than in methanol. Five orders of magnitude from changing nothing but the solvent. The lesson: when you see "SN2 in DMSO," the solvent isn't just a detail — it's part of the mechanism.

## The second mechanism: the carbocation

Now take *tert*-butyl bromide — (CH₃)₃CBr — and dissolve it in water. No added base. No added nucleophile. Just water, which is a terrible nucleophile and a terrible base. By the SN2 analysis, this reaction should be essentially inert. Instead, it reacts more than a million times faster than methyl bromide with hydroxide.

The SN2 picture is simply wrong for this substrate. Either the picture has a hidden exception, or there's an entirely different mechanism. There's a different mechanism.

The rate law:

$$\text{rate} = k\,[(\text{CH}_3)_3\text{CBr}]$$

The nucleophile doesn't appear. Doubling the water concentration changes nothing. Only one species is in the rate-determining step.

Here's what's actually happening. The *tert*-butyl bromide ionizes spontaneously. The C–Br bond breaks heterolytically — both electrons leave with the bromide — and what's left is a carbocation: (CH₃)₃C⁺, a carbon with only six valence electrons and a positive charge. This step is slow; it's the rate-determining step. The nucleophile arrives later and captures the cation. Because the nucleophile isn't in the slow step, its concentration doesn't appear in the rate law.

This is SN1 — substitution, nucleophilic, unimolecular. One species in the rate-determining step, two-step mechanism, carbocation intermediate.

Why does the *tert*-butyl substrate — the worst SN2 substrate — become the best SN1 substrate? Carbocation stability. A carbocation has an empty p-orbital, and anything that donates electron density into that orbital stabilizes it. Three alkyl groups do this through hyperconjugation. A tertiary carbocation is genuinely stable, in the sense that it has a reasonable lifetime and can be observed. A primary carbocation is so unstable that it essentially doesn't form under normal conditions. The stability ordering — tertiary > secondary > primary > methyl — is the same ranking that appeared in Chapter 6, and for the same physical reason.

Allylic and benzylic cations get an extra dose of stability from resonance delocalization. An allylic cation — one adjacent to a C=C — has its positive charge spread over two carbons by resonance, which lowers the energy substantially. A secondary allylic carbocation is roughly as stable as a tertiary alkyl carbocation. The SN1 reaction runs on anything that can form a reasonably stable carbocation.

The stereochemistry reveals a subtle but important feature. A carbocation is sp² hybridized — it's flat, with the empty p-orbital perpendicular to the plane of the bonds. It's achiral. If you start with an enantiomerically pure alkyl halide and go through an SN1 reaction, the planar carbocation intermediate can be attacked from either face. Complete racemization is the prediction. This is mostly what's observed, but not exactly: most SN1 reactions on enantiomerically pure substrates give mostly racemic product with a small bias (typically 5–20%) toward inverted product.

Saul Winstein at UCLA explained this in the 1950s with the concept of ion pairs. The ionization isn't always complete before the nucleophile arrives. In the initial stage, the carbocation and the departing anion are still loosely associated — separated by solvent molecules but not fully independent. This is the ion pair. If a nucleophile arrives during the ion-pair stage, the departing anion partially shields one face, and attack preferentially occurs from the other face — net inversion. After the ions fully separate, both faces are equally accessible, and you get racemization. The observed product ratio reflects which stage the nucleophile arrives in. More polar solvents drive the ions apart faster; less polar solvents extend the ion-pair stage. This explains why the inversion bias depends on solvent.

The solvent story for SN1 is the mirror image of the SN2 story. Polar protic solvents accelerate SN1 by stabilizing the developing charges in the transition state of the ionization step. Water is 100,000 times better than ethanol for the ionization of *tert*-butyl chloride. The very conditions that slow SN2 — protic solvents — are ideal for SN1.

Biology runs SN1 chemistry constantly. In the biosynthesis of geraniol (the compound responsible for the scent of roses), the substrate is dimethylallyl diphosphate (DMAPP). The diphosphate group — stabilized as a low-pKa, charge-delocalized anion, and further assisted by a bound Mg²⁺ that neutralizes some of the negative charge — departs as an allylic carbocation forms. The cation reacts with another molecule, forming a new C–C bond. The enzyme catalyzes each step, but the mechanism is recognizably SN1.

Biology also runs SN2. The methylation of norepinephrine to give adrenaline uses *S*-adenosylmethionine (SAM) as the methyl donor. SAM has a positively charged sulfonium ion bonded to a methyl group; the positive charge polarizes the C–S bond and makes the carbon electrophilic. The nitrogen of norepinephrine attacks the methyl carbon from the back side; the leaving group — *S*-adenosylhomocysteine — departs. Clean SN2. SAM is the cell's version of methyl iodide.

↳ **Dig Deeper — Why basicity and nucleophilicity diverge**

> Hydroxide is a much stronger base than iodide (the conjugate acid of HO⁻ is water, pKa = 15.7; the conjugate acid of I⁻ is HI, pKa ≈ −10), but iodide is a better nucleophile than hydroxide in many SN2 reactions. Explain why basicity (affinity for H⁺) and nucleophilicity (affinity for C in an SN2) diverge here. Cover at least: solvent effects in protic vs. aprotic media, polarizability, and the difference between thermodynamic and kinetic basicity.

**What to do with the output:** Read it, then look at Table 11.1 in the OpenStax source — the relative rates flip when you change solvent. That's the diagnostic.

↳ **Dig Deeper — Why protic solvents push the mechanism**

*One of the most reliable predictive moves in organic chemistry: change the solvent, change the mechanism.*

> Explain in detail how switching from DMSO (polar aprotic) to water (polar protic) shifts an alkyl halide reaction from SN2 toward SN1, holding everything else constant. Cover: which intermediate is being stabilized, why that matters for the reaction coordinate, and what happens to ΔG‡ for each mechanism. Use a 2° benzylic substrate as your example.

**What to do with the output:** Compare against the OpenStax description in §11.5; check whether Claude correctly identifies which energy is being lowered in each case (ground state vs. transition state).

## The third mechanism: losing a piece

The same alkyl halide, treated with the same nucleophile, sometimes does something completely different. Instead of the OH⁻ attaching to the carbon bearing the halide, it pulls a proton off the adjacent carbon. The C–H bond breaks, the C–X bond breaks, a new C=C bond forms between them, and the molecule has lost HX. The product is an alkene. This is elimination.

Why does this happen? Because a nucleophile and a base are the same kind of species — both have a lone pair looking for a positive center. The carbon bearing the halide is one electrophilic site. The proton on the adjacent carbon is another. Which one the reagent attacks depends on the substrate's geometry, the base's size, and the conditions.

Three elimination mechanisms exist. They follow the same naming logic as the substitutions.

E2 is the workhorse. Concerted, bimolecular, second-order. The base abstracts a β-hydrogen at the same time that the C–X bond breaks and the new C=C bond forms — all in a single step. The rate law:

$$\text{rate} = k\,[\text{RX}]\,[\text{Base}]$$

The deuterium isotope effect confirms that the C–H bond is breaking in the rate-determining step: replacing H with D slows the reaction by a factor of about 7. (That's a large number — a sevenfold rate change from swapping out one atom's mass. When you see kH/kD ≈ 7, the C–H bond is definitely breaking in the slow step.)

The most important constraint in E2 is geometric: the H being removed and the X leaving must be anti periplanar. The four atoms H–C–C–X must all lie in the same plane, with H and X on opposite sides of the C–C bond. This is not a preference — it's a requirement. The C–H σ-bonding electrons and the C–X σ* antibonding orbital have to align to flow into the developing π bond. Anti periplanar gives this alignment with a staggered, low-energy geometry. Syn periplanar also has orbital overlap in principle, but the eclipsed geometry around the C–C bond makes it much higher in energy, and it rarely operates.

In cyclohexanes, anti periplanar translates directly to trans-diaxial: both the H and the X have to be axial, and they have to be on opposite faces of the ring. This is sharp enough to be a test. Neomenthyl chloride has its chlorine axial in the more stable chair conformation, with a trans-diaxial β-H available. It eliminates immediately and gives the Zaitsev product. Menthyl chloride has its chlorine equatorial; it has to ring-flip to put the chlorine axial, and in the flipped conformation, only one β-H is trans-diaxial — the one that gives the non-Zaitsev product. Neomenthyl reacts 200 times faster than menthyl and gives a different product. A 200-fold rate change and a complete switch in regiochemistry from changing only the configuration at one carbon.

Regiochemistry in elimination is governed by Zaitsev's rule: the more substituted alkene is the major product, because more substituted alkenes are more stable (hyperconjugation from alkyl groups stabilizes the π bond), and the Hammond postulate connects product stability to transition-state energy. Zaitsev's rule is the default, but anti-periplanar geometry overrides it when the geometry forces a specific β-H.

There's a steric twist: when the base is very bulky — potassium *tert*-butoxide is the standard example — it can't easily reach the carbon bearing the halide for SN2. It grabs a β-H instead. Bulky bases on primary substrates give elimination where you might expect substitution. The base's size shifts the reaction entirely.

E1 is to E2 what SN1 is to SN2: unimolecular, two-step, via a carbocation. The halide ionizes first (slow step); the carbocation then loses a β-proton to whatever weak base is around (fast step). Rate law: rate = k[RX]. No isotope effect — the C–H bond breaks after the slow step. No anti-periplanar requirement — the carbocation can rotate before deprotonation. Clean Zaitsev product.

E1 and SN1 share the same first step, which means they always run together. Form a tertiary carbocation and it will partly be captured by nucleophile (SN1) and partly lose a proton (E1). You can shift the ratio — more base favors elimination, lower temperature favors substitution, because entropy (elimination produces more molecules) becomes more significant at higher temperature — but you can't suppress one completely when the other is running.

E1cB is rare in the lab and common in biology. Here the order reverses: the C–H bond breaks first, giving a carbanion intermediate, and the leaving group departs in a second step. This happens when the β-hydrogen is unusually acidic (typically because an adjacent carbonyl stabilizes the carbanion by resonance) and the leaving group is poor (−OH or similar). Neither the E1 nor the E2 route works well — the leaving group can't ionize on its own (bad for E1), and the concerted geometry is poor (bad for E2). E1cB is what remains.

Fatty acid biosynthesis uses E1cB at every cycle: a 3-hydroxybutyryl thioester loses water to give the corresponding α,β-unsaturated thioester. An enzyme's histidine acts as the base, abstracting the acidic α-proton. Another residue simultaneously protonates the departing hydroxyl. E1cB at body temperature, in water.

↳ **Dig Deeper — The orbital argument for anti-periplanar geometry**

> Walk me through the molecular orbital argument for why anti-periplanar geometry is required for E2 elimination. Specifically: what are the relevant orbitals (C–H σ, C–X σ*, π-developing), how do they align in the anti-periplanar transition state, and why is syn periplanar geometry energetically worse despite having the same orbital alignment in principle? Include a sketch description of the orbitals during the transition state.

**What to do with the output:** Compare against an MO-aware source — Anslyn & Dougherty *Modern Physical Organic Chemistry* if you have it; otherwise check that Claude's answer correctly distinguishes orbital overlap (allowed in both periplanar arrangements) from steric and torsional energy (disfavors syn).

## Putting it together

Five mechanisms. One alkyl halide. The question is always the same: which one wins?

Three questions, in order: What's the substrate? What's the nucleophile or base? What's the solvent?

Primary substrates (methyl and 1°): SN2 if the nucleophile is strong and anionic in polar aprotic solvent. E2 if the base is strong and bulky. SN1 and E1 don't happen — primary carbocations are too unstable to form.

Secondary substrates: SN2 if the nucleophile is strong and anionic (especially non-basic: iodide, cyanide, thiolate) in polar aprotic solvent. E2 if the base is strong (hydroxide, alkoxide). SN1/E1 if the substrate is allylic or benzylic and the conditions are protic without strong base. Plain secondary substrates rarely do clean SN1.

Tertiary substrates: E2 almost always when there's a strong base — the back face of the carbon is completely blocked for SN2. SN1/E1 mixture in polar protic conditions without added base. The carbocation forms readily and partitions between nucleophilic capture and proton loss.

The conditions that flip mechanism are worth knowing precisely, because they're also experimental levers:

- Bulky base → pushes E2 even on primary substrates.
- Polar aprotic solvent → boosts SN2 by leaving the nucleophile unsolvated.
- Polar protic solvent, no added base → enables SN1/E1 on tertiary and resonance-stabilized substrates.
- Heating → favors elimination over substitution (entropy: elimination produces three particles from two; the TΔS term grows with temperature).
- β-H adjacent to a carbonyl, poor leaving group → E1cB.

One worked case to anchor this. 2-Bromobutane with sodium ethoxide in ethanol. The substrate is secondary. Ethoxide is a strong base (pKa of ethanol ≈ 16). Ethanol is a protic solvent, which doesn't help SN2. The strong base dominates. E2 is the major pathway. The product is 2-butene as the major alkene (more substituted — Zaitsev) over 1-butene, with some SN2 product (2-ethoxybutane) as a minor side reaction.

Change one variable: run the same substrate with sodium iodide in acetone. Iodide is a superb nucleophile (polarizable, anionic) but a terrible base (pKa of HI ≈ −10). Acetone is polar aprotic. Now SN2 dominates. Product: 2-iodobutane with inverted configuration.

Same substrate. Different outcome. The mechanism is determined by the conditions, not the molecule alone.

↳ **Dig Deeper — Why heating favors elimination**

> Explain quantitatively why elimination reactions tend to dominate over substitution at higher temperatures. Use the relation ΔG = ΔH − TΔS, and consider the change in moles of free particles for SN2 versus E2 reactions of an alkyl halide with hydroxide. Estimate roughly how many degrees of warming would be needed to flip a 60:40 SN2:E2 ratio to 40:60, assuming reasonable activation entropies.

**What to do with the output:** Sanity-check Claude's quantitative estimate by comparing to a textbook table of SN2 vs. E2 product ratios at different temperatures (e.g., the classic 2-bromobutane + NaOEt data series).

## What this chapter does

Walden's puzzle is now solved. Every step in his malic acid cycle was an SN2 reaction — a backside attack that inverted the configuration at a chiral center. An odd number of inversions in the cycle meant the final product was the enantiomer of the starting material. The "remarkable observation" turned out to be a clean geometric consequence of a single transition state.

That's the thing about mechanism: once you see it, a lot of confusing observations stop being confusing. The SN2 geometry predicts the Walden inversion, the second-order kinetics, the substrate reactivity order, and the solvent effect all at once, from a single picture. The SN1 mechanism predicts the first-order kinetics, the substrate order, the mostly-racemic stereochemistry, and the solvent acceleration all at once, from a carbocation intermediate. E2 predicts the isotope effect, the anti-periplanar requirement, the cyclohexane trans-diaxial rule, and the Zaitsev regiochemistry all from one transition state.

This is not memorization. It's one mechanism explaining many observations. When the next chapter introduces new reactions, the same logic applies — the same variables, the same questions, the same way of thinking.

---

*Source for all data, examples, and historical references: OpenStax* Organic Chemistry*, Chapter 11, modules m00121 through m00133.*
---

## LLM Exercise — Chapter 11: Reactions of Alkyl Halides (SN1/SN2/E1/E2) (Synthesize a Target Molecule Project)

**Project:** Synthesize a Target Molecule.
**What you're building this chapter:** propose a substitution or elimination step in your synthesis, choosing conditions to favor the desired outcome and predicting stereochemistry.
**Tool:** **Claude Project**.

---

**The Prompt:**

```
Chapter 11 of my Synthesis project. Chapter 11 taught the
substitution/elimination decision matrix:
   - **SN2** (1° or unhindered 2° substrate; strong nucleophile;
     polar aprotic solvent like DMSO or DMF; lower temperature) —
     concerted, backside attack, inversion of stereochemistry at
     stereocenter.
   - **SN1** (3° or stabilized 2° substrate; polar protic solvent
     like H₂O or ROH; weak nucleophile is fine) — stepwise via
     carbocation, racemization at stereocenter, possible
     rearrangement.
   - **E2** (need a strong base; anti-periplanar H-LG arrangement;
     concerted; Zaitsev — most-substituted alkene preferred unless
     bulky base gives Hofmann).
   - **E1** (3° substrate; weak base; via carbocation; Zaitsev).

Substitution vs. elimination competition: low temperature +
strong nucleophile favors SN; high temperature + strong base
favors E.

Write the brief's "Substitution or Elimination Step" section in
400–600 words.

1. **Identify a substitution or elimination step in your synthesis.**
   - Substitution: introducing a nucleophile (OH, OR, NR₂, CN,
     etc.) at a carbon that currently has a leaving group.
   - Elimination: forming a C=C bond from a precursor with an
     H and a leaving group on adjacent carbons.

2. **Choose the mechanism (SN1 vs SN2 vs E1 vs E2).** Justify
   based on:
   - Substrate (1°/2°/3°).
   - Nucleophile or base strength.
   - Solvent.
   - Desired stereochemistry.

3. **Predict the product.** Including:
   - Regiochemistry (Zaitsev or Hofmann for eliminations;
     unambiguous for SN where the LG is replaced).
   - Stereochemistry (inversion for SN2; racemization for SN1;
     anti-periplanar for E2).

4. **Draw the mechanism with arrows.** Show the nucleophile/base,
   the substrate, the leaving group, and every electron-flow
   arrow.

5. **Conditions check.** Specify the exact reagents you'd use:
   nucleophile/base, solvent, temperature, equivalents. Real
   syntheses succeed or fail on these details.

End with: name one undesired side reaction your conditions need
to suppress. Examples: "E2 elimination would compete with SN2
substitution; using a less basic nucleophile (NaCN instead of
NaOH) suppresses elimination."
```

---

**What this produces:** A 400–600 word section with a chosen mechanism, predicted product, drawn mechanism, and condition specification. The side-reaction analysis is the discipline this chapter trains.

**How to adapt this prompt:**

- *For your own project:* If your target doesn't have any obvious sub/elim step, find an intermediate that does. Many syntheses include at least one SN2-installed functional group.
- *For ChatGPT / Gemini:* Works as written.
- *For Claude Code:* Not the primary tool here.
- *For a Claude Project:* Append.

**Connection to previous chapters:** Ch 5's stereochemistry, Ch 7's stability rules, and Ch 11's mechanism choices interlock. Chapter 11 is where the synthesis starts to look real.

**Preview of next chapter:** Chapter 12 is mass spectrometry and infrared spectroscopy. You'll predict the MS and IR spectra of your target — the chemistry of structure determination, which the synthesis chemist uses to verify products at every step.


---

## AI Wayback Machine

**Christopher Ingold** was established the modern mechanistic framework for SN1, SN2, E1, and E2 reactions in the 1930s.

**Run this:**

```
Who is Christopher Ingold, and how does their work connect to substitution and elimination we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about their career or ideas.
```

→ Search **"Christopher Ingold"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to walk through one of Christopher Ingold's key experiments or syntheses in detail.
- Add a constraint: "Answer including criticisms or limits of Christopher Ingold's framework."

What changes? What gets better? What gets worse?
