# Chapter 9 — Alkynes: An Introduction to Organic Synthesis

*Alkynes do most of what alkenes do, plus two things alkenes can't: they have an acidic terminal hydrogen, and they make new C–C bonds easily. That's why they're the workhorse of synthetic planning.*

The triple bond — two carbons sharing six electrons in one σ and two π bonds — is geometrically the simplest and chemically among the most useful functional groups in synthesis. Acetylene (HC≡CH), the simplest alkyne, was once the high-temperature fuel of choice for cutting and welding metal; oxyacetylene torches burn at about 3,000 °C. Industrially, acetylene is now mostly a chemical intermediate rather than a fuel, but its chemistry — and the chemistry of more substituted alkynes — has special features that make alkynes essential to almost any multi-step organic synthesis.

This chapter introduces alkynes in their structural, reactivity, and synthetic dimensions. The chapter also makes its first explicit pass at *synthetic strategy* — how to plan a multistep transformation from a starting material to a target. Alkynes are used as a vehicle for that introduction because they offer the cleanest example of a functional group that does several different jobs in synthesis: alkylation (forming new C–C bonds), addition (becoming an alkene or alkane), and selective oxidation/reduction (yielding aldehydes, ketones, or alkenes with controlled geometry).

## Geometry and bonding

Each carbon of a triple bond is sp hybridized — one s orbital combined with one p orbital, leaving two p orbitals unhybridized. The two sp orbitals on each carbon point along a single axis, 180° apart. The unhybridized p orbitals are perpendicular to that axis and to each other.

When two sp-hybridized carbons approach each other, one σ bond forms (head-on overlap of one sp orbital from each). At the same time, the two pairs of p orbitals (px from each, py from each) overlap sideways to form two π bonds. The triple bond is thus one σ bond and two π bonds.

The bond is short and strong. C≡C bond length is 120 pm (versus 134 pm for C=C and 154 pm for C–C). C≡C bond strength is 965 kJ/mol (versus 728 for C=C and 377 for C–C). The high bond strength reflects the four-bond worth of orbital overlap. The short length reflects the high electron density between the nuclei.

Alkyne carbons are linear: H–C≡C–H bond angles are exactly 180°. Substituted alkynes (RC≡CR′) are also linear at the alkyne carbons. This is why alkynes can't show cis-trans isomerism — there's no "side" to the bond, just a single axis.

## Naming alkynes

The IUPAC suffix is *-yne*. Naming is parallel to alkenes:

1. Find the longest chain containing both alkyne carbons. That's the parent.
2. Number from the end nearest the triple bond.
3. The locant of the first triple-bond carbon goes before the parent name.

So HC≡C–CH₂–CH₃ is 1-butyne. CH₃–C≡C–CH₃ is 2-butyne. Cyclic alkynes are named with the cyclo prefix; the smallest stable cycloalkyne is cyclooctyne (an 8-membered ring with one triple bond), because smaller rings would require too much angle strain to accommodate the linear geometry.

A *terminal alkyne* has the triple bond at the end of the chain, with one H on the sp carbon. An *internal alkyne* has the triple bond in the middle.

## Alkyne acidity

A terminal alkyne's C–H bond is unusually acidic. The pKa of acetylene (≈ 25) is much higher than alcohols (≈ 16) but much lower than alkenes (≈ 44) or alkanes (≈ 60).

Why? The C–H bond at a terminal alkyne involves a carbon in sp hybridization. An sp orbital has more s-character (50%) than sp² (33%) or sp³ (25%). Higher s-character means the orbital is closer to the nucleus on average — the electrons in it are closer to the positive nucleus, more tightly held, and more stabilized. When the C–H bond breaks heterolytically to form an *acetylide* anion (RC≡C⁻), the negative charge sits in an sp orbital on carbon. That orbital, with high s-character, holds the negative charge more tightly than an sp² or sp³ would.

This relative stability of the acetylide anion is what makes the terminal alkyne acidic enough to deprotonate with reasonable bases.

The standard base for deprotonating terminal alkynes is sodium amide (NaNH₂) in liquid ammonia. The conjugate acid of NH₂⁻ is NH₃, with pKa ≈ 35. The pKa difference between acetylene (25) and ammonia (35) is 10, meaning the equilibrium constant for the deprotonation is about 10¹⁰ — essentially complete.

You cannot use hydroxide as the base, because hydroxide's conjugate acid (water, pKa 15.7) is more acidic than the terminal alkyne. The equilibrium would lie far to the left.

## Acetylides as nucleophiles

An acetylide ion (RC≡C⁻) is a strong nucleophile and a strong base. Like other carbanions, it has a lone pair on an sp carbon that can attack electrophilic carbons. The most useful application is alkylation — reacting an acetylide with a primary alkyl halide to form a new C–C bond.

$$\text{HC}{\equiv}\text{C}^- + \text{CH}_3\text{CH}_2\text{Br} \longrightarrow \text{HC}{\equiv}\text{C}{-}\text{CH}_2\text{CH}_3 + \text{Br}^-$$

This is an SN2 reaction (Chapter 11) — backside attack of the acetylide on the alkyl halide carbon, with bromide leaving. Net result: a new C–C bond and a longer alkyne.

The reaction works well only with primary alkyl halides. With secondary or tertiary substrates, the acetylide acts as a base instead of a nucleophile, doing E2 elimination to give an alkene. (The acetylide is basic enough to easily abstract β-H's from hindered substrates.)

The synthetic usefulness of acetylide alkylation cannot be overstated. With it, you can build up carbon chains step by step:

1. Start with acetylene (HC≡CH).
2. Deprotonate (NaNH₂, NH₃) → HC≡C⁻ Na⁺.
3. Alkylate with a primary halide R–X → HC≡C–R.
4. Deprotonate again → ⁻C≡C–R.
5. Alkylate with another primary halide R′–X → R′–C≡C–R.

After steps 1–5, you have an internal alkyne with both substituents that you chose. You can then further modify the alkyne (hydration, hydrogenation, etc.) to get whatever final functional group you want at the central position. The alkyne has served as a *connector*, joining two carbon chains and giving you a handle for further chemistry.

This is the canonical move for building disubstituted carbon frameworks: acetylene plus two alkylations gets you any internal alkyne, which is then a launching point for many things.

## Addition reactions to alkynes

Most of the polar additions you saw on alkenes (Chapter 8) also work on alkynes. With one or two twists.

**Hydrohalogenation.** HBr or HCl adds to an alkyne in a Markovnikov fashion. The H goes to the carbon with more H's already (or, for an internal alkyne, to whichever carbon has the more accessible Markovnikov logic). The product is a *vinyl halide* (if you stop after one addition) or, more commonly, a *gem-dihalide* (if a second equivalent of HX adds across the resulting alkene).

The vinyl halide intermediate is selectively obtained by careful control of stoichiometry. A second addition gives the geminal (1,1-) dihalide rather than the vicinal (1,2-) dihalide because the first H–X addition gave a vinyl halide whose Markovnikov regiochemistry directs the second H to the same carbon that already has X. Net result of two HX additions on a terminal alkyne: a CH₂–CX₂ unit.

**Halogenation.** Br₂ or Cl₂ adds to give first a *trans*-1,2-dihaloalkene (from anti addition across the alkyne), then a tetrahalide (from a second anti addition across the resulting alkene).

**Hydration.** Water adds to alkynes under either of two conditions. With H₂SO₄ catalysis plus mercury(II) sulfate (HgSO₄) as a co-catalyst, the addition is Markovnikov. The H₂O ends up on the more substituted carbon. The initial product, a *vinyl alcohol* (or *enol*, ene + ol), is unstable and rearranges immediately to the corresponding ketone via *keto–enol tautomerism*. So Markovnikov hydration of a terminal alkyne gives a methyl ketone (RC(=O)CH₃ from RC≡CH).

The mechanism: H⁺ adds to the alkyne to give a vinyl cation (which is stabilized by mercury bridging in a mercury-catalyzed version). Water then attacks the more substituted carbon, the vinyl cation gets neutralized, and after proton loss the product is the enol. The enol then tautomerizes to the ketone.

For terminal alkynes, the regiochemistry is unambiguously Markovnikov (water always goes to the internal carbon). For internal alkynes, the regiochemistry depends on which side of the alkyne is more substituted, and a mix of products is often obtained.

**Hydroboration–oxidation.** Like alkenes, alkynes undergo BH₃ addition. The result is a vinyl borane. Oxidation with H₂O₂ converts the C–B bond to a C–OH bond, giving an enol that tautomerizes to a carbonyl.

The regiochemistry is anti-Markovnikov: boron goes to the less substituted carbon. After H₂O₂ oxidation, the OH is on the less substituted carbon. The enol tautomerizes to give the *aldehyde* RCH₂CHO (from the terminal alkyne RC≡CH) — the opposite of what HgSO₄/H₂SO₄ hydration gives.

A standard variation uses dialkylboranes (like 9-BBN or disiamylborane) instead of BH₃; these are bulkier and react cleanly with terminal alkynes to give a single addition (not the double addition that BH₃ sometimes gives).

So the alkyne plus terminal-hydration gives:
- HgSO₄/H₂SO₄ → methyl ketone (Markovnikov)
- 9-BBN, then H₂O₂/HO⁻ → aldehyde (anti-Markovnikov)

These are complementary transformations. Pick one based on what end product you want.

## Reduction of alkynes

Two ways to reduce an alkyne to an alkene, with opposite stereochemistry:

**Catalytic hydrogenation with a poisoned catalyst** — the *Lindlar catalyst* (Pd/CaCO₃ poisoned with Pb(OAc)₂ and quinoline, or similar). The poisoned catalyst slows the hydrogenation enough that it stops cleanly at the alkene stage instead of going all the way to the alkane. The H₂ is delivered to the alkyne in syn fashion, giving the *cis*-alkene.

**Dissolving metal reduction** — sodium metal in liquid ammonia (or, equivalently, lithium in ethylamine). The mechanism is an electron-transfer chain: an electron adds to the alkyne to form a radical anion, which is protonated by NH₃ to give a vinyl radical; another electron adds to give a vinyl anion; another protonation gives the alkene. The geometry locks in *trans* during the second electron addition (the trans vinyl anion is more stable than cis), so the product is the *trans*-alkene.

So:
- Lindlar's catalyst → cis-alkene
- Na/NH₃ → trans-alkene

If you fully hydrogenate (H₂, Pt or Pd, no poisoning), you get the alkane — both π bonds reduced, with no stereochemistry control beyond syn addition.

## Oxidative cleavage of alkynes

Like alkenes, alkynes can be oxidatively cleaved. Strong oxidants (KMnO₄ in acidic solution, O₃) cleave the triple bond to give two carboxylic acids — one from each side. For terminal alkynes (RC≡CH), the terminal CH becomes CO₂ and CO₂H. So 1-pentyne (HC≡CCH₂CH₂CH₃) cleaves to give CO₂ + butanoic acid.

Ozonolysis is sometimes used for analytic purposes — to identify where a triple bond was located in a complex natural product.

## Synthetic strategy: thinking backward

The synthesis problem asks: starting from a small set of available compounds, how do you make a specific target?

The standard approach is *retrosynthesis* — start from the target and work backward, asking at each stage "what could have been the immediate precursor of this?" Each step backward is a *disconnection*: you imagine breaking a bond and identifying the synthons (the conceptual pieces) on each side.

A simple example. Suppose the target is 5-decanone:

CH₃(CH₂)₃–C(=O)–(CH₂)₃CH₃

You'd recognize the methyl ketone... wait, this is a symmetric internal ketone. Let me pick another target.

Try 2-hexanone (CH₃COCH₂CH₂CH₂CH₃). Disconnect at the C–C bond between the carbonyl carbon and the carbon next to it: imagine breaking the C(=O)–CH₂ bond. The two synthons would be CH₃C(=O)⁺ (an acyl cation) and ⁻CH₂CH₂CH₂CH₃ (a primary carbanion).

The carbanion is hard to make directly — primary carbanions are too unstable to handle. But an *acetylide* anion, HC≡C–CH₂CH₂CH₂CH₃, can serve as the carbon equivalent. After making the alkyne by alkylation of acetylene with 1-bromobutane (NaNH₂ then alkyl halide), Markovnikov hydration of the resulting 1-hexyne (HgSO₄/H₂SO₄) gives 2-hexanone.

The synthesis:

1. HC≡CH + NaNH₂/NH₃ → HC≡C⁻
2. HC≡C⁻ + CH₃CH₂CH₂CH₂Br → HC≡C–CH₂CH₂CH₂CH₃ (1-hexyne)
3. 1-hexyne + H₂O / HgSO₄ / H₂SO₄ → 2-hexanone

The alkyne played its role: a connector that, once installed, can be turned into a methyl ketone by Markovnikov hydration.

This is the pattern the chapter is teaching: alkynes are intermediates. They're cheap (acetylene is industrially abundant). They're easy to alkylate at the terminal carbon. They can be turned into many different functional groups (ketone, aldehyde, alkene-cis or alkene-trans, alkane, vicinal dihalide, etc.) by selecting the right reagent for the final step. The strategy of running a synthesis through an alkyne intermediate is one of the most general and most reliable in classical organic synthesis.

↳ **Dig Deeper — Why retrosynthesis isn't just running the synthesis backward**

> Retrosynthesis is a way of *thinking* about synthesis, not a literal reversal of forward chemistry. Explain the difference. Cover: what disconnections are, why they're written with a special open-arrow notation, what synthons are and how they differ from real reagents, and why a single retrosynthetic step might map to multiple actual reactions in the forward direction. Use the disconnection of 2-hexanone (worked example in this chapter) as a concrete case.

**What to do with the output:** Verify that Claude correctly distinguishes synthons (idealized fragments) from synthetic equivalents (the real reagents that play the synthon's role). Compare against E. J. Corey's introduction to retrosynthesis in his classic "Logic of Chemical Synthesis."

## What this chapter does

A triple bond is one σ bond plus two π bonds, giving sp-hybridized linear geometry, a short and strong bond, and 180° bond angles at the alkyne carbons. The terminal C–H of a 1-alkyne is unusually acidic (pKa ≈ 25) because the resulting acetylide anion has its negative charge in an sp orbital, with high s-character and good stabilization.

Alkynes do most of the polar additions that alkenes do — HX, X₂, water, BH₃ — with a few twists. The most important: alkyne hydration gives an enol that tautomerizes to a carbonyl, so the actual product is a ketone (Markovnikov, with HgSO₄/H₂SO₄) or an aldehyde (anti-Markovnikov, via hydroboration).

Reduction of an alkyne can give either the cis-alkene (Lindlar's catalyst) or the trans-alkene (Na/NH₃). Full reduction with H₂/Pt gives the alkane.

Acetylide alkylation builds new C–C bonds. Two successive acetylide alkylations on acetylene give a disubstituted internal alkyne with whatever two R groups you wanted. This makes alkynes the connector of choice for building carbon frameworks in multi-step synthesis.

All of this together makes alkynes one of the most versatile starting points in synthetic planning. The chapter has used them as a vehicle to introduce retrosynthetic thinking — disconnecting a target backward to find a starting material and a reaction sequence that delivers it. The same kind of thinking applies to every later chapter that involves multi-step synthesis.

---

*Source for all data, examples, and historical references: OpenStax* Organic Chemistry*, Chapter 9, modules m00102 through m00111.*
---

## LLM Exercise — Chapter 9: Alkynes — An Introduction to Organic Synthesis (Synthesize a Target Molecule Project)

**Project:** Synthesize a Target Molecule.
**What you're building this chapter:** an alkyne-based step (or analysis of why none is needed), plus the project's first 2-step synthesis chain.
**Tool:** **Claude Project**.

---

**The Prompt:**

```
Chapter 9 of my Synthesis project. Prior sections in this Claude
Project. Chapter 9 taught: alkyne structure (sp, linear); terminal
alkyne acidity (pKa ~25); acetylide formation with strong base
(NaNH₂, n-BuLi) → acetylide anion → C-C bond formation via
alkylation with primary alkyl halides; alkyne reduction
selectively to cis-alkene (Lindlar/Pd-CaCO₃) or trans-alkene
(Na/NH₃) or alkane (H₂/Pd-C); alkyne hydration → ketone (Markovnikov)
or aldehyde (anti-Markovnikov via hydroboration); the
"introduction to organic synthesis" framing — multi-step
planning.

Write the brief's "Alkyne Step + Multi-Step Chain" section in
400–600 words.

1. **Does your target need a 2-carbon chain extension?** Most
   complex molecules have a C-C bond that's naturally formed
   from a smaller piece + a 2-carbon unit. The acetylide
   alkylation does exactly that. State whether your target needs
   such a step.

2. **If yes, propose the acetylide alkylation step.**
   - Starting acetylide and alkyl halide.
   - Reaction with NaNH₂ (or similar base) to form acetylide.
   - Alkylation with R-X.
   - The product (extended alkyne).

3. **If no, propose an alternative C-C bond formation chain
   appropriate to your target.** (The Grignard from Ch 10 will
   be the more common alternative.)

4. **Build the first 2-step chain.** Combine an alkene-based step
   (from Ch 8) and an alkyne-based step (or alternative) into a
   2-step sequence toward your target. Show:
   - Step 1: starting materials, conditions, product 1.
   - Step 2: product 1 + new reagents → product 2.
   - The mechanism for each step (arrows).

5. **The convergent-vs-linear assessment.** Two short branches
   converging into one product (convergent) is more efficient
   than building one long chain step by step (linear). Where
   on this spectrum is your developing synthesis?

End with: what's the longest carbon chain in your target that
hasn't been retrosynthesized yet? That's the next chapter's
problem.
```

---

**What this produces:** A 400–600 word section + the first 2-step chain in the project. The convergent-vs-linear analysis is a real retrosynthesis discipline.

**How to adapt this prompt:**

- *For your own project:* If your target has no acetylide-friendly disconnection, that's fine — the Ch 10 Grignard and Ch 11 SN2 will cover the standard C-C bond cases.
- *For ChatGPT / Gemini:* Works as written.
- *For Claude Code:* Not the primary tool here.
- *For a Claude Project:* Append.

**Connection to previous chapters:** Ch 8's alkene step + Ch 9's alkyne step (or alternative) form the first 2-step chain.

**Preview of next chapter:** Chapter 10 covers organohalides — the alkyl-halide intermediates that drive most C-C-bond-forming chemistry. Grignards (from alkyl halides) are central to most complex syntheses.


---

## AI Wayback Machine

**Robert B. Woodward** was completed the total synthesis of quinine, cholesterol, cortisone, strychnine, and chlorophyll — Nobel 1965.

**Run this:**

```
Who is Robert B. Woodward, and how does their work connect to organic synthesis we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about their career or ideas.
```

→ Search **"Robert B. Woodward"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to walk through one of Robert B. Woodward's key experiments or syntheses in detail.
- Add a constraint: "Answer including criticisms or limits of Robert B. Woodward's framework."

What changes? What gets better? What gets worse?
