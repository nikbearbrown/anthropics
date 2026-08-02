# Chapter 2 — Polar Covalent Bonds, Acids and Bases

*Almost every reaction in this book happens because electrons are shared unequally. This chapter is about how to spot the unevenness and predict where it sends the chemistry.*

Methane boils at −161 °C. Water boils at +100 °C. The two molecules have nearly the same molecular weight (16 g/mol vs. 18 g/mol). They have similar shapes — water is bent rather than tetrahedral, but neither is large or complicated. And yet methane is a gas at any temperature you'd encounter in everyday life, while water is a liquid that fills oceans and runs through your veins. That 261-degree gap between their boiling points is one of the most important facts in chemistry. Without it, no oceans, no liquid water, no biology.

The cause is simple to state and worth understanding deeply. The electrons in the C–H bonds of methane are shared almost equally between carbon and hydrogen. The electrons in the O–H bonds of water are not. Oxygen pulls them more strongly toward itself, leaving the hydrogens slightly positive and the oxygen slightly negative. Water molecules attract each other through these partial charges — the partial-positive H of one molecule reaching toward the partial-negative O of another — and to pull them apart you have to put in real energy. Methane molecules barely attract each other at all; a little thermal jiggling and they fly apart into vapor.

This same uneven sharing of electrons is what makes some bonds reactive and others inert. It's what makes acetic acid an acid and methane not. It's what makes the carbon of a carbonyl group attractive to nucleophiles. The whole reactivity story of organic chemistry, told properly, starts here. So this chapter is about how to read electron distribution out of structure, and how to predict — quantitatively — what that distribution will do.

## Electronegativity, and why some bonds are polar

The pull an atom exerts on bonding electrons is its *electronegativity*. Pauling defined a scale on which fluorine is the most electronegative element (EN = 4.0) and cesium the least (EN = 0.7). The values are arbitrary in absolute terms, but the differences between elements are meaningful.

For organic chemistry, the electronegativities you'll use most often:

| Element | EN |
|---|---|
| F | 4.0 |
| O | 3.5 |
| Cl, N | 3.0 |
| Br | 2.8 |
| I, S, C | 2.5 |
| H | 2.1 |
| Na, K | 0.9 |

Carbon and hydrogen are nearly the same (2.5 vs 2.1), which is why C–H bonds are essentially nonpolar. The bonding electrons sit nearly halfway between the two nuclei. The bond has no chemistry of its own to speak of — it just holds atoms together.

C–O and C–N are different. Oxygen and nitrogen pull electrons substantially toward themselves; the carbon is left electron-poor. We mark the bond's asymmetry with two devices. First, partial-charge symbols: δ⁻ on the more electronegative atom, δ⁺ on the less. Second, a crossed arrow drawn along the bond, pointing from positive end to negative end, with the cross at the positive end. Both are bookkeeping for the same physical fact: where the electrons live, on average.

The electronegativity *difference* between two bonded atoms is what determines polarity. The convention is roughly:

- ΔEN < 0.5 → nonpolar covalent (C–H, C–C, S–H)
- 0.5 ≤ ΔEN < 2.0 → polar covalent (C–O, C–N, C–Cl, O–H)
- ΔEN ≥ 2.0 → mostly ionic (Na–Cl, K–F)

These boundaries are smooth, not sharp. Bond character runs along a continuum from "perfectly equal sharing" (ΔEN = 0) through "increasingly polar covalent" to "essentially full electron transfer" (ΔEN large). There's no atomic-bond switch that flips between covalent and ionic.

A useful related idea is the *inductive effect*: an atom's pull on bonding electrons can travel through a chain of bonds. If you put a chlorine on a carbon two bonds away from another carbon, that second carbon is also slightly electron-poor — less so than the carbon directly bonded to chlorine, but measurably so. The effect dies off quickly with distance (it falls roughly with the cube of the number of bonds), but over one or two bonds it's substantial and predictable. Inductive effects show up later when we talk about why some carboxylic acids are stronger than others, why electron-withdrawing groups direct aromatic substitution to specific positions, and why some carbocations are more stable than others.

## Molecular polarity and dipole moments

Individual bond polarities sum (vectorially) to give the polarity of the whole molecule. If the bond dipoles point in opposite directions and have equal magnitude, they cancel — the molecule has no overall polarity. If they don't cancel, the molecule is polar.

Carbon dioxide (O=C=O) has two highly polar C=O bonds. But the molecule is linear and symmetric, so the two bond dipoles point in exactly opposite directions and cancel completely. CO₂ is nonpolar despite having very polar bonds. Methane has four C–H bonds, each weakly polar, all arranged tetrahedrally — they sum to zero. Methane is nonpolar. Carbon tetrachloride: same logic, four polar C–Cl bonds in tetrahedral arrangement, vector sum zero. Nonpolar.

Water, on the other hand, has two O–H bonds plus two oxygen lone pairs. The molecule is bent (104.5° H–O–H angle), and the lone pairs contribute their own dipole component pointing the same way as the O–H dipoles. Nothing cancels. Water has a substantial molecular dipole.

Dipole moments are measured experimentally and reported in *debyes* (D). One debye is 3.336 × 10⁻³⁰ coulomb-meters. The full charge of an electron separated by 100 pm gives a dipole moment of 4.80 D, so any real molecular dipole is a fraction of that — partial charges separated by partial distances.

A few values worth knowing:

| Molecule | μ (D) | Comment |
|---|---|---|
| NaCl (gas) | 9.00 | nearly fully ionic |
| CH₂O (formaldehyde) | 2.33 | strong C=O dipole |
| CH₃Cl | 1.87 | strong C–Cl dipole |
| H₂O | 1.85 | bent, polar |
| CH₃OH | 1.70 | C–O dipole + O–H |
| CH₃CO₂H | 1.70 | similar |
| NH₃ | 1.47 | bent (pyramidal), polar |
| CH₃NH₂ | 1.31 | weaker than NH₃ |
| CO₂ | 0 | linear, cancellation |
| CH₄ | 0 | tetrahedral, cancellation |
| CH₃CH₃ | 0 | symmetric |
| benzene | 0 | symmetric |

Notice the practical lesson: solubility tracks polarity. Polar molecules dissolve in polar solvents (like water). Nonpolar molecules dissolve in nonpolar solvents (like hexane). "Like dissolves like" is a chemistry-class slogan, but it's grounded in this physics. A polar solute fits comfortably into a polar solvent because both have unevenly distributed charges that can interact electrostatically. A nonpolar solute in a polar solvent is energetically expensive — it disrupts the solvent's hydrogen-bonded network without compensating with new attractive interactions.

## Formal charges

When you draw a Lewis structure with all the dots, sometimes an atom has a different number of electrons than it would in its neutral elemental state. The bookkeeping for that is *formal charge*.

The rule:

$$\text{formal charge} = (\text{group number}) - (\text{nonbonding electrons}) - \tfrac{1}{2}(\text{bonding electrons})$$

For each atom in a structure:
- Group number = the number of valence electrons the neutral atom has (4 for C, 5 for N, 6 for O, etc.)
- Nonbonding electrons = electrons in lone pairs on this atom
- Bonding electrons = electrons shared in bonds, counted with this atom getting half

If the result is zero, no formal charge. If positive, the atom has formally lost electrons. If negative, formally gained.

Methane carbon: 4 valence − 0 lone pair − 4 (half of 8 in bonds) = 0. Neutral.

Ammonia nitrogen: 5 valence − 2 lone pair − 3 (half of 6 in bonds) = 0. Neutral.

Hydronium oxygen (H₃O⁺): 6 valence − 2 lone pair − 3 (half of 6 in bonds) = +1. Positive, as expected.

Hydroxide oxygen (HO⁻): 6 valence − 6 lone pair − 1 (half of 2 in bonds) = +6 − 6 − 1 = −1. Negative.

Formal charges are a formalism — they don't represent actual full charges on atoms. The methylsulfonium ion (CH₃)₃S⁺ has a formal +1 on sulfur; the actual charge distribution is more spread out, but for bookkeeping purposes the +1 sits on S. The formalism is useful because it tracks where electrons are "missing" or "extra" in your structure, which in turn tells you something about how the molecule will react.

A pattern worth memorizing: in neutral organic compounds,
- carbon has 4 bonds, no formal charge
- nitrogen has 3 bonds + 1 lone pair, no formal charge
- oxygen has 2 bonds + 2 lone pairs, no formal charge
- halogens have 1 bond + 3 lone pairs, no formal charge

Any deviation from these means a formal charge. If you see a nitrogen with four bonds, it's +1 (like the ammonium ion, NH₄⁺). If you see an oxygen with one bond and three lone pairs, it's −1 (like hydroxide, HO⁻). If you see a carbon with three bonds and a lone pair, it's −1 (a carbanion). With three bonds and no lone pair, it's +1 (a carbocation). The 3-bonds-+1, 3-bonds-and-pair-−1 pattern repeats across the periodic row.

## Resonance: when one structure isn't enough

Sometimes a single Lewis structure can't capture where the electrons actually are. The classic example is the acetate ion, CH₃CO₂⁻, the conjugate base of acetic acid. You can draw it with the negative charge on either of the two oxygens:

```
CH₃–C(=O)–O⁻         ↔         CH₃–C(–O⁻)=O
```

Each structure has one oxygen double-bonded to carbon (no formal charge) and one oxygen single-bonded with a −1 formal charge. The two structures are equivalent — a mirror image of each other across the central carbon. Experimentally, the two C–O bonds in acetate are exactly the same length (about 127 pm, in between the typical C=O bond at 123 pm and C–O bond at 143 pm). Both oxygens carry equal partial negative charge.

Neither single Lewis structure shows this. The actual molecule is a *resonance hybrid* — a single quantum-mechanical state that is best described by averaging the two contributing structures. The double-headed arrow (↔) between resonance forms means "these are not separate molecules, this is one molecule that needs both pictures to be described accurately."

This is a place where the limits of Lewis-dot bookkeeping show. Real molecules don't have integer numbers of electrons in specific bonds. They have electron distributions, and the distributions can spread over multiple atoms. Resonance is the workaround: draw the contributing structures, recognize that the truth is a weighted average.

Five rules for working with resonance:

**Rule 1.** *Individual resonance forms are imaginary. The hybrid is real.* The molecule is not flickering between structures. There is one molecule, with a single electron distribution that the structures together approximate.

**Rule 2.** *Resonance forms differ only in the position of electrons.* The atoms stay where they are. Only the π electrons and lone pairs move between forms. If you find yourself moving an atom from one place to another, you've drawn a constitutional isomer, not a resonance form.

**Rule 3.** *Resonance forms don't have to contribute equally.* Some forms are more stable than others. The hybrid resembles the more stable forms more strongly. A form with all atoms having octets is more important than one with an electron-deficient atom. A form with the negative charge on a more electronegative atom is more important than one with it on a less electronegative atom.

**Rule 4.** *Resonance forms must obey valence rules.* Carbon can't have five bonds. Hydrogen can't have two. If a structure violates valence, it's not a valid resonance form.

**Rule 5.** *The hybrid is more stable than any single resonance form.* Resonance is stabilizing. Every additional valid resonance form lowers the energy of the molecule. This is why the acetate ion is so much more stable than the alkoxide of an alcohol — acetate has two equivalent resonance forms; an alkoxide has only one place to put the charge. The same logic explains why allylic and benzylic carbocations are unusually stable, why amide bonds resist rotation, and why benzene is essentially unreactive compared to other unsaturated hydrocarbons.

A practical move for drawing resonance forms: look for the pattern X–Y=Z (where X has a lone pair, Y=Z is a double bond). The lone pair can flow into the X–Y bond, pushing the Y=Z double bond's electrons onto Z as a lone pair. The result: a new structure with X=Y–Z, the bonds and the lone pairs swapped. Whenever you see this pattern, two resonance forms exist. The acetate case is one example. Many enolates, amides, and conjugated systems have this same flow.

↳ **Dig Deeper — Why electron distributions look like averages**

> Resonance hybrids are not "rapidly interconverting structures." They are single quantum mechanical states best described as superpositions. Walk through what this means in actual quantum-mechanical terms. Cover: why the ground-state wave function of acetate ion is genuinely a single state (not an oscillation), how the two resonance structures correspond to two basis functions in a linear combination, and what experimental observations (vibrational spectra, NMR coupling, X-ray structure) confirm that a single molecular state is being observed rather than averaged dynamics.

**What to do with the output:** Compare against any quantum chemistry textbook section on resonance theory. Verify that Claude doesn't accidentally describe resonance as time-dependent flicker.

## Acids and bases: the Brønsted–Lowry definition

A *Brønsted–Lowry acid* is a substance that donates a proton (H⁺). A *Brønsted–Lowry base* is a substance that accepts a proton.

The two definitions are inseparable. Every time an acid donates a proton, something else accepts it; the donor and acceptor go together. When HCl dissolves in water, HCl is the acid (donates H⁺) and water is the base (accepts H⁺ to become H₃O⁺). When acetic acid (CH₃CO₂H) reacts with hydroxide ion, acetic acid is the acid and hydroxide is the base.

After the proton transfer, two new species exist. The HCl that lost its proton is now Cl⁻; this is the *conjugate base* of HCl. The water that gained the proton is now H₃O⁺; this is the *conjugate acid* of water. Every acid–base reaction has two acid–base pairs:

```
HCl    +    H₂O    →    Cl⁻    +    H₃O⁺
acid       base       conj. base   conj. acid
```

The relationship: an acid and its conjugate base differ by exactly one H⁺. Same for a base and its conjugate acid.

How strong is an acid? Quantitatively, by the equilibrium constant for its dissociation in water:

$$\text{HA} + \text{H}_2\text{O} \rightleftharpoons \text{H}_3\text{O}^+ + \text{A}^-$$

$$K_a = \frac{[\text{H}_3\text{O}^+][\text{A}^-]}{[\text{HA}]}$$

Ka is the *acidity constant*. A strong acid has Ka much greater than 1 (HCl has Ka ≈ 10⁷). A weak acid has Ka much less than 1 (acetic acid has Ka ≈ 1.8 × 10⁻⁵). The values span more than 50 orders of magnitude. Working with logs is easier:

$$\text{p}K_a = -\log_{10} K_a$$

Now strong acids have small or negative pKa, and weak acids have large positive pKa. Each unit of pKa is a factor of ten in Ka.

Some pKa values to anchor the scale:

| Acid | pKa | Conjugate base |
|---|---|---|
| HCl | −7.0 | Cl⁻ |
| HNO₃ | −1.3 | NO₃⁻ |
| H₃PO₄ | 2.16 | H₂PO₄⁻ |
| CH₃CO₂H (acetic acid) | 4.76 | CH₃CO₂⁻ |
| H₂PO₄⁻ | 7.21 | HPO₄²⁻ |
| HCN | 9.31 | CN⁻ |
| CH₃CH₂OH | 16.00 | CH₃CH₂O⁻ |
| H₂O | 15.74 | HO⁻ |
| NH₃ | ≈ 35 | NH₂⁻ |
| HC≡CH (acetylene) | ≈ 25 | HC≡C⁻ |
| CH₂=CH₂ (ethylene) | ≈ 44 | CH₂=CH⁻ |
| CH₄ | ≈ 60 | CH₃⁻ |

A few things stand out from this list.

First, water itself has a pKa. Water can act as an acid: H₂O + base → HO⁻ + H–base. The pKa of 15.74 is calculated from the autoionization equilibrium and the concentration of pure water (55.4 M at 25 °C).

Second, all the typical alcohols have pKa values around 16, very close to water. Alcohols are barely acidic — comparable to water, slightly weaker.

Third, hydrocarbons sit way to the basic end. Methane has pKa ≈ 60. There is essentially no chance of removing a proton from methane under normal conditions. To get any equilibrium concentration of CH₃⁻, you'd need a base whose conjugate acid has pKa > 60 — which means an extremely strong base, the kind used only in carefully controlled reactions.

Fourth — the key working insight — *the strength of an acid is determined by the stability of its conjugate base*. A strong acid (low pKa) has a stable conjugate base. A weak acid has an unstable conjugate base. Why? Because if the conjugate base is stable, the equilibrium for the acid's dissociation lies further to the right; the acid loses its proton readily because the resulting anion is happy. If the conjugate base is unstable — high in energy — the equilibrium lies far to the left; the acid holds onto its proton.

This is the most useful rule in organic chemistry for predicting acidity. Almost everything that determines pKa traces back to factors that stabilize or destabilize the conjugate base. The four big ones:

1. **Electronegativity of the atom holding the negative charge.** A more electronegative atom is happier with a negative charge. Methanol (pKa 15.5) is much more acidic than methylamine (pKa 35) because oxygen handles the negative charge better than nitrogen.

2. **Size of the atom holding the charge.** A larger atom can spread the charge over more space, lowering its energy. HF (pKa 3.2) is a weaker acid than HCl (pKa −7) because chlorine is bigger than fluorine, even though fluorine is more electronegative. Going down a column, acids get stronger because conjugate bases get more diffuse.

3. **Resonance.** If the negative charge can be delocalized over multiple atoms via resonance, the conjugate base is more stable. Acetate ion, with its two equivalent resonance forms, is much more stable than ethoxide, with only one. Hence acetic acid (pKa 4.76) is much more acidic than ethanol (pKa 16).

4. **Inductive effects.** Electron-withdrawing groups near the negative-charge site stabilize it by pulling some of the charge away. Trichloroacetic acid (CCl₃CO₂H, pKa 0.7) is much stronger than acetic acid because three chlorines pull electron density away from the negatively charged oxygen of trichloroacetate.

The four factors compete and combine. When predicting the relative acidity of two compounds, find the conjugate bases, look at where the negative charges are, and identify which conjugate base is more stable using the four factors. The acid with the more stable conjugate base wins.

## Predicting whether a proton transfer will go

A proton transfer goes in the direction that produces the weaker acid. Equivalently: the equilibrium favors the side with the more stable acid–base pair.

Hydroxide ion plus acetic acid: HO⁻ + CH₃CO₂H → H₂O + CH₃CO₂⁻. The forward direction produces water (pKa 15.74) and acetate. The reverse direction would produce hydroxide and acetic acid (pKa 4.76). The forward direction has a *weaker* acid (water). The equilibrium favors the forward direction. Strongly. The pKa difference is 15.74 − 4.76 = 11, which means the equilibrium constant for the forward reaction is about 10¹¹. Essentially complete.

This is the diagnostic. To predict whether a base will deprotonate an acid, look up two pKa values: that of the acid being deprotonated, and that of the conjugate acid of the base. If the conjugate acid of the base has the higher pKa (weaker acid), the deprotonation will go. If lower, it won't.

A practical example. Will sodium hydride (NaH) deprotonate ethanol? NaH is a source of H⁻ (hydride), an extremely strong base. The conjugate acid of H⁻ is H₂, which has pKa ≈ 35 — very weak as an acid, very strong base on the H⁻ side. Ethanol's pKa is 16. The pKa gap is 35 − 16 = 19, favoring ethanol's deprotonation by 10¹⁹. NaH plus ethanol → sodium ethoxide plus H₂ gas, essentially complete.

Will hydroxide deprotonate acetylene (pKa 25)? Hydroxide's conjugate acid is water (pKa 15.74). Water is a stronger acid than acetylene by about 10 pKa units, so hydroxide does *not* deprotonate acetylene. To get the acetylide ion, you'd need a base whose conjugate acid has pKa > 25 — for example, NaNH₂ (the conjugate acid is NH₃, pKa 35). The pKa gap is 35 − 25 = 10, favoring acetylene deprotonation by 10¹⁰. Sodium amide and acetylene → sodium acetylide plus ammonia.

This pKa-difference rule is one of the most powerful predictive tools in the book. Whenever you see a base added to a substrate, ask: does the conjugate acid of the base have a higher pKa than the acid being deprotonated? If yes, the proton transfer happens. If no, it doesn't.

↳ **Dig Deeper — Why pKa is a thermodynamic fact, not a kinetic one**

> pKa values describe equilibrium positions for proton transfer reactions, not the speeds at which proton transfers occur. Explain the distinction. Cover: what equilibrium versus kinetic control means in proton transfer, when the kinetic and thermodynamic acidities can differ (especially for compounds where deprotonation creates an unusually stabilized carbanion), and how this distinction matters in real laboratory chemistry. Use a CH-acid (like acetone, pKa ≈ 19) versus an OH-acid (like acetic acid, pKa 4.76) as your example.

**What to do with the output:** Verify Claude correctly identifies that proton transfers between heteroatoms (O, N) are typically very fast and reach equilibrium quickly, while C–H deprotonations can be slow.

## The Lewis definition

The Brønsted–Lowry definition is convenient but limited. It captures every reaction that involves a proton being moved, and that's a lot of chemistry. But there are reactions that look acid-base in character — electron-pair donation from one species to another — without any proton being transferred at all.

A *Lewis acid* is an electron-pair acceptor. A *Lewis base* is an electron-pair donor. The proton (H⁺) is a Lewis acid (it has an empty 1s orbital, ready to accept a pair). Hydroxide (HO⁻) is a Lewis base (it has lone pairs, ready to donate). So every Brønsted–Lowry acid is a Lewis acid and every Brønsted–Lowry base is a Lewis base — the Lewis definition is broader.

What makes Lewis broader: it includes substances with empty orbitals that are not protons. The boron in BF₃ has an empty p orbital. The aluminum in AlCl₃ has an empty p orbital. The carbocation R⁺ has an empty p orbital. All three are Lewis acids — they accept electron pairs. They show up everywhere in organic reactions: as catalysts (BF₃·OEt₂, AlCl₃ in Friedel-Crafts reactions) and as intermediates (carbocations in SN1/E1 reactions).

The Lewis definition also includes anything with a lone pair as a base: water, ammonia, alcohols, amines, halide ions, alkoxides, sulfides — all donate electron pairs to electrophiles. The big conceptual unification: *nucleophiles are Lewis bases, electrophiles are Lewis acids*. The whole reactivity story of organic chemistry is repeated proton transfers (special case) and repeated electron-pair donations between Lewis bases and Lewis acids (general case).

## Hydrogen bonding

One last piece — the special interaction that explains why water boils at +100 °C.

A *hydrogen bond* is the attraction between an H attached to a strongly electronegative atom (typically O, N, or F) and a lone pair on another strongly electronegative atom in a different molecule. The H is partial-positive because its bonding partner pulls the electrons away. The lone pair on the second molecule is the partial-negative target. The electrostatic attraction between them holds the two molecules close — not as strongly as a covalent bond, but a lot more strongly than ordinary van der Waals attractions.

A typical hydrogen bond is about 20 kJ/mol — five percent of a covalent C–H bond, ten times stronger than a typical dispersion interaction. Water can form up to four hydrogen bonds per molecule (two through its hydrogens, two through its oxygen lone pairs). The result is a network of mutually attracted molecules, dense enough to hold water in the liquid state up to 100 °C and dense enough to give ice its low density (the open hydrogen-bonded structure of solid ice has more space per molecule than liquid water).

Hydrogen bonding is not just about boiling points. It's the structural basis for protein folding (the α-helix and β-sheet are stabilized by C=O···H–N hydrogen bonds along the backbone). It's the genetic-code basis for DNA (A pairs with T through two hydrogen bonds, G with C through three; the specific pairing is what makes information storage possible). It's the reason why polar groups — alcohols, amines, carboxylic acids — dissolve readily in water and why nonpolar groups don't. Most of the macroscopic biology you've heard of traces back, eventually, to a hydrogen bond.

## What this chapter does

The reactivity of an organic molecule is determined by where the electrons are. The first move is identifying bond polarity from electronegativity differences and bond geometry. The second is summing those bond dipoles to predict molecular polarity, which controls solubility and intermolecular forces. The third is recognizing places where one Lewis structure isn't enough — where resonance distributes electrons across multiple atoms and confers extra stability. The fourth is reading acidity off conjugate-base stability, using pKa as the quantitative measure and the four stabilizing factors (electronegativity, size, resonance, inductive effects) as the qualitative tools for prediction.

Once these tools are in hand, the rest of the book is mostly application. Functional groups will turn out to be patterns of bond polarity. Reaction mechanisms will be sequences of electron-pair donations from Lewis bases to Lewis acids. Selectivity — why a reaction goes to one product instead of another — will trace back to the relative stability of competing transition states and intermediates, which in turn trace back to electronegativity, resonance, and inductive effects.

Methane boils at −161 °C because its electrons are evenly shared. Water boils at +100 °C because they're not. That asymmetry, played out over the entire periodic table and across all the functional groups of organic chemistry, is what makes organic reactions go.

---

*Source for all data, examples, and historical references: OpenStax* Organic Chemistry*, Chapter 2, modules m00017 through m00029.*
---

## LLM Exercise — Chapter 2: Polar Covalent Bonds, Acids and Bases (Synthesize a Target Molecule Project)

**Project:** Synthesize a Target Molecule.
**What you're building this chapter:** the acid-base profile of your target — pKa values, protonation states, and inductive effects.
**Tool:** **Claude Project** "Synthesis of [Your Molecule]" — appends a section.

---

**The Prompt:**

```
Chapter 2 of my Synthesis project. The Target Profile is in this
Claude Project. Chapter 2 taught: electronegativity and bond
polarity; the inductive effect (electron-withdrawing or -donating
groups shifting electron density through sigma bonds); Brønsted
acid-base (proton donor/acceptor) and Lewis acid-base (electron
pair acceptor/donor) definitions; pKa as the quantitative
acidity scale.

Write the brief's "Acid-Base Profile" section in 400–600 words.

1. **Polar bonds.** List every polar bond in the target. For each:
   the two atoms, the dipole direction, and an estimate of the
   bond's polarity (weak/moderate/strong) based on
   electronegativity difference.

2. **Acidic protons.** Identify every potentially acidic proton in
   the target. For each: name the functional group it's attached
   to, estimate the pKa, and rank them in order from most to least
   acidic.
   Standard pKa references:
   - Carboxylic acid OH: ~4-5
   - Phenolic OH: ~10
   - Alcohol OH: ~16-18
   - Amide NH: ~17-25
   - Aliphatic CH: 40-50 (not really acidic at physiological pH)
   - Aromatic CH: ~43

3. **Basic sites.** Identify every potentially basic site in the
   target. For each: name the functional group and rank basicity.
   Common bases:
   - Aliphatic amine NH: pKb ~3-4 (pKa of conjugate acid ~10-11)
   - Aromatic amine NH: pKb ~10 (less basic due to lone pair in
     aromatic system)
   - Pyridine N: pKa of conjugate acid ~5
   - Imidazole N: pKa of conjugate acid ~7 (close to physiological)

4. **Inductive effects.** For each acidic proton, identify any
   nearby electron-withdrawing or -donating groups that shift the
   pKa from the "neutral" reference value. Be specific: "the
   ortho-nitro group on the phenol lowers the pKa from 10 to ~7
   because nitro is a strong electron-withdrawer through
   resonance and induction."

5. **The protonation state at physiological pH (if applicable).**
   For drug targets: at pH 7.4, which functional groups are
   protonated vs. deprotonated? This bears directly on bioactivity
   (protonated amines bind differently to receptors than neutral
   ones).

End with one paragraph naming any acid-base behavior the synthesis
must handle. Examples: "the phenol will need to be protected
during basic conditions"; "the carboxylic acid must be made before
the amine to avoid intramolecular amide formation"; "the basic
amine will need to be neutralized for chromatography."
```

---

**What this produces:** A 400–600 word Acid-Base Profile section. The protonation-state analysis is especially valuable for drug targets — it predicts the molecule's behavior in the body and in chromatography.

**How to adapt this prompt:**

- *For your own project:* Use a pKa reference table (Bordwell, Evans). Don't trust LLM-generated pKa values for unusual structures without verification.
- *For ChatGPT / Gemini:* Works as written.
- *For Claude Code:* Optional — RDKit can compute approximate pKa values for sanity-checking.
- *For a Claude Project:* Append.

**Connection to previous chapters:** Chapter 1 identified bonds and hybridization; Chapter 2 quantifies the electronic environment.

**Preview of next chapter:** Chapter 3 turns to alkane structure and Newman projections. You'll identify any conformationally-significant portions of your target — important for ring systems, peptide bonds, and any rotation around single bonds that affects shape.


---

## AI Wayback Machine

**Gilbert N. Lewis** was developed the electron-pair theory of chemical bonding and the modern acid-base framework that bears his name.

**Run this:**

```
Who is Gilbert N. Lewis, and how does their work connect to polar bonds, acids, and bases we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about their career or ideas.
```

→ Search **"Gilbert N. Lewis"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to walk through one of Gilbert N. Lewis's key experiments or syntheses in detail.
- Add a constraint: "Answer including criticisms or limits of Gilbert N. Lewis's framework."

What changes? What gets better? What gets worse?
