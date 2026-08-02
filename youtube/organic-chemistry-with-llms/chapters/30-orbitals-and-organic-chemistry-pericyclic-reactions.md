# Chapter 30 — Orbitals and Organic Chemistry: Pericyclic Reactions

*Pericyclic reactions go through cyclic transition states with all electrons moving simultaneously. The Woodward-Hoffmann rules predict — exactly — which ones happen and which don't, based on the symmetry of the molecular orbitals involved.*

In 1969, Robert Woodward and Roald Hoffmann published their landmark paper *The Conservation of Orbital Symmetry*. They had found that an enormous body of seemingly unrelated reactions — Diels-Alder cycloadditions, electrocyclic ring closures, sigmatropic rearrangements — all obey a single set of rules based on the symmetry of the molecular orbitals involved. Reactions that the rules permitted would proceed thermally; those forbidden would not happen at all (or would require photochemical excitation to a different orbital configuration). The agreement between rule and experiment was remarkable. Hoffmann shared the 1981 Nobel Prize in chemistry with Kenichi Fukui (who developed frontier molecular orbital theory in parallel); Woodward had died two years earlier and so could not share it, but his contribution is universally acknowledged.

This chapter introduces pericyclic reactions and the orbital-symmetry rules that govern them. The mechanism is unusual: there's no nucleophile attacking an electrophile, no carbocation intermediate, no radical chain. Instead, a single concerted step rearranges electrons through a cyclic transition state, with all bonds breaking and forming simultaneously. The selectivity is exquisite: a small structural change can flip the reaction from allowed to forbidden, completely changing the outcome.

## What pericyclic reactions are

A *pericyclic reaction* is a reaction that takes place in a single concerted step through a cyclic transition state, with no intermediates. Three general types:

**Electrocyclic reactions**. A conjugated polyene closes into a cyclic compound, with one of the π bonds becoming a new σ bond. Or the reverse: a cyclic compound with one σ bond opens into a conjugated polyene. Examples:
- 1,3,5-hexatriene ↔ 1,3-cyclohexadiene
- cis,trans-2,4-hexadiene → cis-3,4-dimethylcyclobutene

**Cycloadditions**. Two π systems combine to form a cyclic product with two new σ bonds. The Diels-Alder reaction (Chapter 14) is a [4+2] cycloaddition: a diene (4 π electrons) plus a dienophile (2 π electrons) gives a cyclohexene.

**Sigmatropic rearrangements**. A σ bond migrates across a π system. Designated by [i,j] notation indicating the positions involved. The most common are [3,3]-sigmatropic rearrangements like the Cope and Claisen rearrangements.

All three classes share the same mechanistic features: cyclic transition state, concerted bond reorganization, no intermediate, exquisite stereochemistry control.

## Frontier molecular orbital theory

The key insight from Woodward and Hoffmann (and Fukui) is that pericyclic reactions are controlled by the symmetry of the *frontier molecular orbitals* — the highest occupied molecular orbital (HOMO) and lowest unoccupied molecular orbital (LUMO) of the reactants.

For a conjugated polyene with n π electrons, the molecular orbitals are arranged in a familiar ladder: ψ₁ (lowest energy, fewest nodes), ψ₂, ψ₃, etc. The lowest n/2 are bonding (filled); the higher are antibonding (empty). The HOMO is the highest filled level; the LUMO is the lowest unfilled.

For 1,3-butadiene (4 π electrons): ψ₁ and ψ₂ are filled, ψ₃ is empty. HOMO = ψ₂; LUMO = ψ₃*.

For 1,3,5-hexatriene (6 π electrons): ψ₁, ψ₂, ψ₃ are filled, ψ₄ is empty. HOMO = ψ₃; LUMO = ψ₄*.

For a photochemically excited state, the highest filled and lowest empty orbitals shift up by one — for excited 1,3-butadiene, HOMO = ψ₃*, LUMO = ψ₄*.

The symmetry of each MO matters. In 1,3-butadiene:
- ψ₁ has the same sign at both ends (no node between ends).
- ψ₂ has opposite signs at the two ends (one node between ends).
- ψ₃* has the same sign at the two ends (two nodes total, but ends match).
- ψ₄* has opposite signs at the two ends (three nodes total).

Whether the ends of the molecule have the *same sign* or *opposite signs* in a given orbital is the key feature for predicting whether a pericyclic reaction can proceed.

## Electrocyclic reactions: conrotatory vs. disrotatory

When a polyene's two terminal carbons rotate to form a new σ bond (closing into a ring), the two terminals can rotate in the same direction (both clockwise, or both counterclockwise — *conrotatory*) or in opposite directions (one clockwise, the other counterclockwise — *disrotatory*).

The mode of rotation is determined by the symmetry of the HOMO. The new σ bond requires bond formation between the two ends — orbital overlap requires that the lobes overlapping be of the same sign.

For the *thermal* (ground-state) reaction: the HOMO is what matters. The overlap requirement determines the rotation mode.

For the *photochemical* (excited-state) reaction: the HOMO is the orbital that was the LUMO of the ground state. So the rotation mode flips.

**For 1,3,5-hexatriene** (6 π electrons, 4n+2 with n=1):
- Ground-state HOMO is ψ₃, which has the same sign at the two ends.
- For these ends to rotate to form a σ bond with proper overlap, the rotation must be *disrotatory* (the upper lobes must come together).
- This is the experimental result: thermal closure of cis,cis-2,4,6-octatriene to give cis-5,6-dimethyl-1,3-cyclohexadiene with the methyls cis (disrotatory closure).
- Photochemically: the HOMO is now ψ₄*, opposite sign at the ends. Conrotatory closure is required. The product has the methyls trans.

**For 1,3-butadiene** (4 π electrons, 4n with n=1):
- Ground-state HOMO is ψ₂, opposite signs at the ends.
- Thermal closure (rare in this direction) is conrotatory.
- The reverse reaction — opening of cyclobutene to butadiene — is more common and clearly conrotatory.
- *cis*-3,4-dimethylcyclobutene opens conrotatorily to give *cis,trans*-2,4-hexadiene (the methyls end up on opposite sides of the diene plane).
- *trans*-3,4-dimethylcyclobutene opens conrotatorily to give *trans,trans*-2,4-hexadiene.

**The rule (for thermal electrocyclic reactions):**
- 4n electrons → conrotatory.
- 4n+2 electrons → disrotatory.

**For photochemical reactions, the rule reverses:**
- 4n electrons → disrotatory.
- 4n+2 electrons → conrotatory.

This is the general statement of orbital symmetry for electrocyclic processes.

## Cycloadditions

A [m+n] cycloaddition combines a π system with m π electrons and another with n π electrons, making two new σ bonds in a cyclic product.

The Diels-Alder reaction (Chapter 14) is [4+2]: 4 π electrons (the diene) + 2 (the dienophile) = 6 π electrons in the transition state. This is a *suprafacial-suprafacial* reaction — both new σ bonds form on the same face of each reactant (the upper face of the diene, the upper face of the dienophile, say). The geometry is favorable when both reactants have HOMO and LUMO of compatible symmetry.

The HOMO of the diene (ψ₂) has the right symmetry to overlap with the LUMO of the dienophile (ψ₂*, also called π*). The ends of the diene's HOMO have opposite signs, but the inner two carbons have the same sign as the ends. The dienophile's LUMO has opposite signs at the two ends. The orbital overlap is geometrically constructive when the two molecules approach in the standard endo or exo orientation.

A [4+2] thermal reaction is allowed because of this orbital symmetry.

A [2+2] thermal cycloaddition (e.g., two ethylenes combining to give cyclobutane) is *forbidden* by orbital symmetry. The HOMO of one alkene (ψ₁) has the same sign at both ends; the LUMO of the other (ψ₂*) has opposite signs. The orbital overlap is destructive at one of the two new bond positions and constructive at the other. The transition state has a node that prevents bond formation.

This is why ethylene + ethylene → cyclobutane essentially does not happen thermally. It does happen photochemically (with one of the alkenes promoted to its excited state, where the HOMO is now ψ₂* and the symmetry is right for a suprafacial-suprafacial reaction). Photochemical [2+2] is a useful synthetic method.

**The general rule:**
- [4n+2] thermal cycloaddition: allowed (suprafacial-suprafacial).
- [4n] thermal cycloaddition: forbidden (must be suprafacial-antarafacial, geometrically very difficult).
- [4n+2] photochemical: forbidden.
- [4n] photochemical: allowed.

## Sigmatropic rearrangements

A sigmatropic rearrangement moves a σ bond across a π system. The classification [i,j] tells you which atoms migrated to which: for a [3,3]-sigmatropic, the atom that was at position 1 of the σ bond migrates to position 3, while the atom at the other end of the σ bond moves three atoms over too.

Examples:

**Cope rearrangement**: 1,5-hexadiene rearranges to itself (in symmetric cases) or to a different 1,5-diene (in unsymmetric cases). [3,3]-sigmatropic. Goes through a chair-like cyclic transition state with 6 electrons (2 σ + 2 π + 2 π).

**Claisen rearrangement**: an allyl vinyl ether rearranges to a γ,δ-unsaturated carbonyl. [3,3]-sigmatropic. Highly useful in synthesis because it transfers an allyl group while creating a new C=O.

**[1,5]-Hydride shift**: an H atom migrates from C1 to C5 of a 1,3-cyclopentadiene, with the σ bond breaking and re-forming as it traverses the π system. Common in cyclopentadiene chemistry.

The Woodward-Hoffmann rules apply: [3,3]-sigmatropic rearrangements have 6 electrons in the transition state and are thermally allowed (suprafacial-suprafacial). [1,3]-sigmatropic rearrangements (4 electrons) are thermally forbidden suprafacial-suprafacial — they would require a suprafacial-antarafacial mode that's geometrically difficult.

## Diels-Alder revisited

With orbital symmetry in hand, we can revisit the Diels-Alder of Chapter 14.

The diene (4 π electrons) brings its HOMO (ψ₂); the dienophile (2 π electrons) brings its LUMO (ψ₂*). The HOMO has the right symmetry to overlap with the LUMO at both ends — both new σ bonds can form simultaneously, on the same face of each reactant. The reaction is *suprafacial-suprafacial* and *thermally allowed*.

The endo rule emerges from secondary orbital interactions. The dienophile's HOMO (ψ₁) can interact with the diene's LUMO (ψ₃*) in a way that stabilizes the endo transition state. This gives the small bias toward the endo product that's experimentally observed.

Substituent effects: an electron-poor dienophile has a lower-energy LUMO, which improves the HOMO-LUMO overlap with a normal electron-rich diene (smaller HOMO-LUMO gap). So electron-withdrawing groups on the dienophile speed up Diels-Alder reactions. An electron-rich diene (with an electron-donating group like alkoxy) has a higher-energy HOMO, also reducing the HOMO-LUMO gap and accelerating the reaction.

For *inverse-electron-demand* Diels-Alder (with an electron-poor diene and electron-rich dienophile), the LUMO of the diene matches the HOMO of the dienophile, and the orbital arithmetic is reversed. The reaction is still allowed, just controlled by different orbitals.

## Why orbital symmetry matters

The Woodward-Hoffmann rules are not a chemistry-class trick — they're the rigorous solution to a quantum-mechanical problem. The wavefunctions of reactants must connect to the wavefunctions of products through transition states without changing symmetry. If the orbital symmetries don't match, the reaction is forbidden in the strictest sense — not just slow, but blocked by symmetry-imposed selection rules.

This explains why some reactions go beautifully and others not at all. A thermal Diels-Alder works in seconds at room temperature; a thermal [2+2] cycloaddition doesn't go even at 200°C with a catalyst. The barrier isn't activation energy in the usual sense — it's a fundamental quantum-mechanical incompatibility between the starting and product orbitals.

The rules also explain why some reactions need light to go. UV light promotes one electron from the HOMO to the LUMO, changing the relevant frontier orbitals and reversing the symmetry analysis. So [2+2] cycloadditions, forbidden thermally, become allowed photochemically — and sunlight-driven [2+2] cycloadditions are responsible for some natural product chemistry, photo-induced damage to DNA, and useful synthetic methods.

## Practical applications

Pericyclic reactions are major synthetic methods. Diels-Alder reactions are used to assemble six-membered rings in countless natural product syntheses. Claisen rearrangements transfer allyl groups stereospecifically. Cope rearrangements interconvert 1,5-dienes for stereochemical control. Photochemical [2+2] cycloadditions make cyclobutanes that aren't easily accessible otherwise. Electrocyclic reactions are used to make cyclic dienes from linear ones (or to ring-open) with predictable stereochemistry.

In biology, pericyclic mechanisms are less common than the polar mechanisms we've covered, but they do exist. The [3,3]-sigmatropic Claisen rearrangement is the mechanism for the chorismate-to-prephenate step in the shikimate pathway (en route to aromatic amino acids). Several enzymes use pericyclic chemistry as part of their catalytic machinery — chorismate mutase being a clean example.

↳ **Dig Deeper — Why orbital symmetry is preserved**

> The Woodward-Hoffmann rules say a thermal [4n+2] cycloaddition is "allowed" while a [4n] one is "forbidden." Walk through what these terms mean rigorously. Cover: the conservation of total electron spin (which makes ground-state to ground-state transitions need symmetry-conserving paths), the role of nodes in molecular orbitals as features that propagate from reactants to products, why the symmetry of orbitals must be preserved through the transition state, and what "forbidden" means in practice (not "completely impossible" but "the transition state is so high in energy that the reaction doesn't proceed thermally").

**What to do with the output:** Compare against any modern physical organic chemistry textbook (Anslyn & Dougherty's chapter on pericyclic reactions is the standard reference). Verify that Claude correctly distinguishes orbital symmetry as a quantum-mechanical constraint from "ordinary" steric or electronic effects.

## What this chapter does

Pericyclic reactions go through cyclic transition states in single concerted steps. The three major classes:

- **Electrocyclic** reactions: ring closure or opening of a polyene, with one π bond becoming (or breaking) into a σ bond.
- **Cycloaddition** reactions: two π systems combine to give a cyclic product with two new σ bonds.
- **Sigmatropic** rearrangements: a σ bond migrates across a π system.

The Woodward-Hoffmann rules predict whether a pericyclic reaction is *allowed* or *forbidden* based on the symmetry of the frontier molecular orbitals (HOMO and LUMO).

For electrocyclic reactions:
- 4n electron systems: thermal conrotatory; photochemical disrotatory.
- 4n+2 electron systems: thermal disrotatory; photochemical conrotatory.

For cycloadditions:
- [4n+2] thermal allowed (suprafacial-suprafacial).
- [4n] thermal forbidden; photochemical allowed.

For sigmatropic rearrangements:
- [3,3] thermal allowed (e.g., Cope, Claisen).
- [1,5] thermal allowed.
- [1,3] thermal forbidden.

The rules are derived from quantum mechanics — orbital symmetry must be conserved through a concerted transition state, and the symmetry analysis of HOMO and LUMO determines whether the reaction can proceed.

The next (and final) chapter (31) covers synthetic polymers — the chemistry of large molecules made by polymerization of small monomers, with applications in plastics, fibers, and biomaterials.

---

*Source for all data, examples, and historical references: OpenStax* Organic Chemistry*, Chapter 30, modules m00339 through m00348.*
---

## LLM Exercise — Chapter 30: Pericyclic Reactions (Synthesize a Target Molecule Project)

**Project:** Synthesize a Target Molecule.
**What you're building this chapter:** pericyclic-reaction analysis in your synthesis (Diels-Alder, electrocyclic, sigmatropic).
**Tool:** **Claude Project**.

---

**The Prompt:**

```
Chapter 30 of my Synthesis project. Chapter 30 taught: pericyclic
reactions (cycloadditions, electrocyclic, sigmatropic, group
transfers) proceed via concerted, single-transition-state
mechanisms; the Woodward-Hoffmann rules predict allowed/forbidden
pathways via orbital symmetry; thermal Diels-Alder is allowed
(suprafacial-suprafacial); photochemical [2+2] cycloaddition is
allowed; suprafacial vs. antarafacial; sigmatropic rearrangements
(Cope, Claisen — different from Claisen condensation).

Write the brief's "Pericyclic Reactions" section in 300–500 words.

1. **Does your synthesis use a pericyclic reaction?** Most
   syntheses use Diels-Alder at some point if it fits. Check:
   - 6-membered ring with C=C and substituents in the right
     positions.
   - Stereochemistry consistent with the endo preference (bulky
     groups cis on the same face).

2. **If Diels-Alder applies, propose the cycloaddition.**
   - The diene (must be s-cis at the time of reaction).
   - The dienophile (typically electron-poor — has C=C with an
     EWG like CO₂R, NO₂, CN, etc.).
   - The product (cyclohexene with predicted stereochemistry).

3. **Suprafacial/antarafacial analysis.** For your pericyclic
   reaction, identify the orbital-symmetry conditions for
   allowed reaction.
   - Thermal [4+2] (Diels-Alder): allowed suprafacial-
     suprafacial.
   - Thermal [2+2]: forbidden; photochemical [2+2] is allowed.
   - Sigmatropic [3,3] shifts (Cope, Claisen): allowed thermally.

4. **Why pericyclic reactions are valuable in synthesis.** They:
   - Build multiple bonds in one step.
   - Are stereospecific (predictable stereochemistry).
   - Often work with high yield and selectivity.
   - Are the most powerful ring-forming reactions in synthetic
     chemistry.

5. **If no pericyclic in your synthesis:** that's fine. Note
   whether one COULD have been used (an alternative
   retrosynthesis) and why your route uses different chemistry.

End with: which Woodward-Hoffmann rule (or orbital-symmetry
argument) is most relevant to your synthesis's pericyclic step,
if any?
```

---

**What this produces:** A 300–500 word section. For syntheses with Diels-Alder, this is one of the most powerful single chapters.

**Connection to previous chapters:** Ch 14's Diels-Alder introduction is now formalized with orbital-symmetry rules.

**Preview of next chapter:** Chapter 31 is the closer. Synthetic polymers + the final integration. You'll compile your synthesis document into a polished retrosynthesis + forward synthesis with mechanism arrows, plus a literature comparison.


---

## AI Wayback Machine

**Roald Hoffmann** was co-developed the Woodward-Hoffmann rules for pericyclic reactions — Nobel 1981.

**Run this:**

```
Who is Roald Hoffmann, and how does their work connect to pericyclic reactions we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about their career or ideas.
```

→ Search **"Roald Hoffmann"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to walk through one of Roald Hoffmann's key experiments or syntheses in detail.
- Add a constraint: "Answer including criticisms or limits of Roald Hoffmann's framework."

What changes? What gets better? What gets worse?
