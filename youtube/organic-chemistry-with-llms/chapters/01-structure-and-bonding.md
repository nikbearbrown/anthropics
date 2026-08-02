# Chapter 1 — Structure and Bonding

*Carbon's chemistry is decided by one fact: it has four valence electrons and forms four bonds. Everything else in this book is a consequence.*

There are about 197 million known chemical compounds. Almost all of them contain carbon. DNA molecules can contain more than 100 million carbon atoms. The proteins in your muscles, the medicines in your bloodstream, and the plastic of the chair you're sitting on are all carbon compounds. No other element behaves like this. Silicon is in the same column of the periodic table; it forms four bonds too. And yet there's no silicon-based version of biochemistry, no silicon analog of polypropylene at industrial scale. Carbon makes long chains, branches off, doubles back into rings, fuses rings together, and stays stable while doing it. Silicon doesn't.

Why? The answer is in carbon's electronic structure — what orbitals it has, how the electrons sit in them, and what happens when those orbitals overlap with orbitals on another atom. This chapter is a review of those ideas. Most of it should be familiar from general chemistry. But there's one thing in here that is genuinely strange the first time you see it, and it's worth understanding now because almost every reaction in this book depends on it.

The strange thing is methane. Carbon has six electrons, distributed as 1s² 2s² 2p². The 2s orbital and the 2p orbitals have different energies and different shapes. You would naively predict that methane, CH₄, should have two kinds of C–H bonds — some involving the 2s orbital, others involving the 2p orbitals. Instead, all four C–H bonds in methane are identical. Same length. Same strength. Same angle (109.5°) between any two of them. Tetrahedrally symmetric. The electrons don't seem to know they came from different orbitals.

Linus Pauling explained this in 1931, and the explanation reorganizes how you think about atomic orbitals. We'll get there. First, the foundation.

## What an atom looks like

An atom is a small, dense, positively charged nucleus surrounded by electrons. The nucleus contains protons (positive) and neutrons (neutral) and holds essentially all the mass. Electrons are nearly massless and orbit at much larger distances. A typical atom is about 200 pm across — a thin pencil line is roughly three million carbon atoms wide.

Two numbers identify an atom. The atomic number Z is the number of protons (and, in a neutral atom, electrons). Carbon has Z = 6, hydrogen has Z = 1, phosphorus has Z = 15. The mass number A is protons plus neutrons. Atoms of the same element with different mass numbers are isotopes. Carbon-12, carbon-13, and carbon-14 all have six protons, but six, seven, and eight neutrons respectively. Carbon-12 makes up 98.89% of natural carbon, carbon-13 about 1.11%, and carbon-14 is essentially negligible — but carbon-14's slow radioactive decay is what makes radiocarbon dating possible.

Electrons don't follow simple planetary orbits. They occupy orbitals — regions of space, defined by quantum mechanics, where the electron is most likely to be found. Each orbital is a wave function ψ; the square of that wave function, ψ², is the probability density. An orbital's "size" is conventionally drawn as the surface inside which the electron spends about 90% of its time.

There are four kinds of orbitals — s, p, d, f — distinguished by shape. Organic chemistry uses s and p. An s orbital is spherical, centered on the nucleus. A p orbital is shaped like a dumbbell, with two lobes separated by a node — a region of zero electron density right at the nucleus. There are three p orbitals at every level above the first, oriented along three perpendicular axes (x, y, z), and the two lobes of each p orbital have opposite algebraic signs in the wave function. That sign business looks like a technicality. It's not. We'll come back to it when we talk about how orbitals combine into bonds.

Orbitals are organized into shells. The first shell contains only one s orbital (1s) and holds at most two electrons. The second shell contains one s orbital (2s) and three p orbitals (2px, 2py, 2pz) — four orbitals total, holding at most eight electrons. The third shell adds five d orbitals to the s and three p, for a maximum of eighteen electrons.

Three rules tell you how electrons fill orbitals.

First — the Aufbau principle: electrons fill the lowest-energy orbitals first. The order is roughly 1s, 2s, 2p, 3s, 3p, 4s, 3d, 4p, 5s. (The 4s slips below the 3d, which is why the transition metals get weird.)

Second — the Pauli exclusion principle: at most two electrons in any orbital, and the two must have opposite spins. (Spin is an intrinsic angular momentum that has only two possible values — call them up and down.)

Third — Hund's rule: when there are several orbitals of equal energy (the three 2p orbitals, say), electrons go into separate orbitals first, with parallel spins, before pairing up.

Apply this to carbon (six electrons): 1s² 2s² 2px¹ 2py¹. The two 1s electrons are paired. The two 2s electrons are paired. The two remaining electrons go into different 2p orbitals (Hund) with parallel spins. Carbon's valence shell — the outermost shell, 2 — has four electrons.

That is the entire input to organic chemistry. Four valence electrons.

## Why atoms bond at all

Atoms bond because the result is more stable — lower in energy — than the separate atoms. Energy flows out of the system when a bond forms (usually as heat). Energy must be put back in to break a bond. This sign convention is not arbitrary; it reflects the actual physics of orbital overlap, which we'll get to. For now, just note that *every bond in every molecule is a place where the system is at lower energy than the separated atoms would be*. When a chemical reaction happens, the question is whether the bonds being broken cost more energy than the bonds being formed return.

The driving observation, known since the early 20th century: noble gases (group 8A) are unusually stable, and they all share a feature — eight electrons in their outermost shell. (Helium has two, but the 1s shell only holds two, so two is the full shell.) Other elements achieve stability by reaching the same configuration, either by gaining electrons, losing them, or sharing them.

Group 1A elements (sodium, potassium) have one valence electron beyond a noble-gas core. They tend to lose it, becoming +1 cations with a noble-gas configuration. Group 7A elements (chlorine, bromine) have seven valence electrons and need one more for an octet. They tend to gain one, becoming −1 anions. When the loss and the gain happen together — sodium gives an electron to chlorine — the electrostatic attraction between Na⁺ and Cl⁻ holds them together. This is an ionic bond. Sodium chloride is held together by it.

For carbon, which has four valence electrons, ionic bonding doesn't work. Carbon would have to either gain four electrons (becoming C⁴⁻) or lose four (becoming C⁴⁺). Both are energetically prohibitive — pulling four electrons off a carbon atom requires ionization energies that no reaction can supply. So carbon takes a different route. Instead of gaining or losing electrons, it shares them.

G. N. Lewis proposed this picture in 1916. Two atoms share a pair of electrons; both atoms count the pair as part of their valence shell. The shared pair is a covalent bond. Both atoms get closer to a noble-gas configuration without anyone gaining a full negative or positive charge.

Lewis structures show every valence electron as a dot. Hydrogen has one dot, carbon four, oxygen six. A pair of dots between two atoms is a bond. Pairs not in bonds are lone pairs. Two dots between atoms become a single line in line-bond (Kekulé) structures: H–C–H rather than H:C:H.

Counting bonds is straightforward. Hydrogen needs one more electron to fill 1s, so it forms one bond. Carbon needs four more to fill 2s and 2p, so it forms four. Nitrogen has five valence electrons and needs three more, so it forms three bonds and has one lone pair. Oxygen has six valence electrons, needs two more, forms two bonds, has two lone pairs. Halogens (fluorine, chlorine, bromine, iodine) have seven valence electrons, need one more, form one bond, and carry three lone pairs.

These valences are not rules. They are consequences of the octet target. Almost every neutral organic molecule you'll meet follows them. Exceptions exist — phosphorus and sulfur in the third row can expand their octets and form more bonds — but the four-three-two-one pattern (C-N-O-X) covers most of organic chemistry.

## Why methane is tetrahedral

Now back to the puzzle. Carbon has 2s² 2p² in its ground state. A 2s orbital and three 2p orbitals — four valence orbitals total, but only two of them are occupied with one electron each (the other two: the 2s is doubly occupied, and one of the 2p is empty). For carbon to form four bonds, it would need four singly occupied orbitals. The actual ground-state configuration provides only two.

You might guess that the easy fix is to promote one of the 2s electrons into the empty 2p orbital. That gives 2s¹ 2px¹ 2py¹ 2pz¹ — four singly occupied orbitals. But now you have one s-character orbital and three p-character orbitals. They have different energies. They have different shapes. They point in different directions (the 2s is spherical, the three 2p are along x, y, z axes). The four C–H bonds in methane should be different from each other.

They aren't. All four are identical. Same length (109 pm), same strength (439 kJ/mol), same H–C–H angle (109.5°), pointing toward the corners of a regular tetrahedron with carbon at the center. The 109.5° tetrahedral angle is the geometric solution that puts four equivalent things as far apart as possible on a sphere.

Pauling's resolution was hybridization. The 2s orbital and the three 2p orbitals don't stay separate when carbon prepares to bond. They mathematically combine — *hybridize* — to form four new orbitals, each one the same as the others. These are *sp³ hybrid orbitals*. The superscript 3 says how many p orbitals went into the mix; together with one s, that's four hybrid orbitals total.

Each sp³ hybrid orbital points toward one corner of a tetrahedron. The angle between any two of them is 109.5°. They have the same shape (an asymmetric dumbbell with one big lobe and one small lobe — the s and p contributions add on one side and subtract on the other), the same energy, and the same character. When each of the four sp³ orbitals on carbon overlaps with a 1s orbital on hydrogen, you get four identical C–H bonds, arranged tetrahedrally, all equivalent.

Hybridization is not a physical process the molecule does. It's a mathematical reshuffling of the basis we use to describe carbon's bonding. The actual electron distribution in methane is what it is; the hybrid-orbital description is a useful way of bookkeeping that distribution to make geometric predictions. The reason the description is useful is that it makes the right predictions: tetrahedral geometry, equivalent bonds, 109.5° angles, observed bond lengths and strengths.

Hybridization is also not unique to carbon. Nitrogen in ammonia (NH₃) is sp³ — three of its four sp³ orbitals form bonds to hydrogen, the fourth holds the lone pair. The H–N–H angle is 107.1°, slightly compressed from the tetrahedral 109.5° because the lone pair takes up more space than a bond. Oxygen in water is sp³ too — two bonds, two lone pairs, H–O–H angle of 104.5°. Carbon in any molecule with all single bonds (an *alkane*) is sp³.

So far we have one kind of hybridization. There are two others.

When carbon needs to form a *double* bond, as in ethylene (H₂C=CH₂), one s orbital combines with only two of the three p orbitals. The result is three sp² hybrid orbitals (the superscript 2 says two p's went in) and one unhybridized 2p orbital left over. The three sp² orbitals lie in a single plane, 120° apart. The unhybridized p orbital sticks straight up and down, perpendicular to that plane.

Two sp²-hybridized carbons approach each other and form two different bonds. The first is a sigma (σ) bond, formed by the head-on overlap of one sp² orbital from each carbon along the line between the two nuclei. This is structurally similar to the C–H σ bond in methane — cylindrically symmetric around the bond axis. The second is a pi (π) bond, formed by the sideways overlap of the two unhybridized 2p orbitals. The π bond electrons live in two lobes, one above and one below the molecular plane. They are *not* on the line between the nuclei.

A double bond, then, is one σ and one π. The σ is stronger (head-on overlap is more efficient than sideways overlap). The π is weaker but still substantial. Together: a C=C bond is 728 kJ/mol, almost exactly twice as strong as a C–C single bond at 377 kJ/mol — but not quite, because the π part contributes less than the σ part. The C=C bond is also shorter than C–C: 134 pm versus 153 pm. More electrons holding the nuclei together pulls them closer.

Ethylene has four hydrogens, four σ bonds to those hydrogens (each from an sp² orbital on a carbon overlapping with a 1s on a hydrogen), one C=C σ bond, and one C=C π bond. All six atoms lie in a single plane. The H–C–H angle is 117.4°, the H–C–C angle 121.3°, both close to the 120° expected for sp².

The third hybridization handles triple bonds. In acetylene (HC≡CH), one s orbital combines with only one p orbital. The result is two sp hybrid orbitals (180° apart, along one axis) and two unhybridized p orbitals (perpendicular to each other and to the sp axis). Two sp-hybridized carbons form one σ bond (head-on sp–sp overlap) and two π bonds (sideways overlap of two pairs of perpendicular p orbitals). A triple bond is one σ + two π. The C≡C bond strength is 965 kJ/mol; the bond length is 120 pm. Each sp orbital that's not in the triple bond overlaps with a hydrogen 1s — giving acetylene its linear geometry, with H–C–C angles of exactly 180°.

Three hybridizations, three geometries:

| Hybridization | Geometry | Bond angles | Example |
|---|---|---|---|
| sp³ | tetrahedral | 109.5° | methane (CH₄) |
| sp² | trigonal planar | 120° | ethylene (H₂C=CH₂) |
| sp | linear | 180° | acetylene (HC≡CH) |

If you can identify the hybridization of every carbon, nitrogen, and oxygen in a structure, you can predict its three-dimensional shape. That single move is the foundation for almost every stereochemical argument in the rest of this book.

↳ **Dig Deeper — Why orbitals hybridize**

> Hybridization isn't something the molecule physically does — it's a mathematical re-basing of atomic orbitals to make predictions easier. Explain in detail why mathematicians and chemists are allowed to do this without changing the underlying physics. Cover: the linearity of the Schrödinger equation, what it means for two solutions to be "the same physical state in different bases," and why the hybridized basis is more useful for predicting molecular geometry even though the unhybridized basis is just as valid.

**What to do with the output:** Compare against any quantum-chemistry textbook (Levine's *Quantum Chemistry* is the standard reference). Verify that Claude correctly distinguishes between the mathematical operation of hybridization and the physical electron distribution.

## Two ways of describing a bond

Hybridization is a tool inside *valence bond theory* — the framework that explains bonds as overlap between atomic orbitals (or hybrid orbitals) on the bonded atoms. Valence bond theory is intuitive and visual, and most of this book uses it. But it's not the only theory.

The other major framework is *molecular orbital (MO) theory*. In MO theory, atomic orbitals on different atoms combine mathematically — through addition and subtraction of wave functions — to form *molecular orbitals* that span the entire molecule. Each molecular orbital, like an atomic orbital, has a specific shape, energy, and electron capacity (two electrons per MO).

In H₂, two 1s atomic orbitals combine in two ways. The additive combination (the wave functions reinforce each other in the region between the nuclei) gives a *bonding* MO, lower in energy than either 1s. The subtractive combination (the wave functions cancel in the region between the nuclei, creating a node) gives an *antibonding* MO, higher in energy. Both MOs exist as soon as the orbitals combine, but only the bonding MO is occupied — both electrons drop into the lower-energy combination, and the antibonding MO sits empty above. The two electrons in the bonding MO bind the two nuclei together.

If you forced electrons into the antibonding MO (by exciting the molecule with light, say), they would actively *push* the nuclei apart. The node in the antibonding MO means there's zero electron density between the nuclei, so the nuclei see each other's positive charges with nothing in between to mediate the repulsion. This is why the antibonding orbital is called antibonding — its electrons would weaken or break the bond.

The same logic generalizes. In ethylene, two p orbitals on adjacent sp²-hybridized carbons combine to form a π bonding MO (additive, lobes on the same side reinforce) and a π* antibonding MO (subtractive, with a node between nuclei). The two π electrons occupy the bonding MO; the antibonding MO is empty. The π* MO becomes important in chapters on photochemistry, conjugated systems, and pericyclic reactions, because it's the lowest-energy place to put an electron when the molecule absorbs light.

Why have two theories? Because each one is good at different problems. Valence bond theory makes geometry predictions easy — count the σ bonds and lone pairs on an atom, identify the hybridization, you've got the geometry. MO theory makes electronic structure predictions easy — predict the colors of molecules, the chemistry of conjugated systems, the relative stabilities of aromatic rings. Most of this book uses VB; chapters 14, 15, and 30 lean on MO. Knowing both is worth the effort.

## How to draw a molecule

Lewis structures with every dot drawn are accurate but tedious. For molecules with more than a handful of atoms, you need shorthand. Three levels of shorthand exist, each more compressed than the last.

*Line-bond (Kekulé) structures* draw every atom and replace each shared electron pair with a single line. Lone pairs are usually still shown as dots. This is the most explicit form, useful for tracking electrons in mechanisms.

*Condensed structures* drop the C–H and C–C single bonds entirely. CH₃ means a carbon with three hydrogens; CH₂ means a carbon with two; CH means a carbon with one. The chain is read as if you're listing atoms in order: 2-methylbutane is CH₃CH(CH₃)CH₂CH₃. The (CH₃) in parentheses is a methyl group branching off the main chain. Vertical bonds are still drawn explicitly when needed for clarity.

*Skeletal structures* go further. Carbon atoms are not drawn at all — they're implicit at every line endpoint and every line intersection. Hydrogens on carbon are not drawn either — you're supposed to mentally fill them in based on carbon's valence of four. Atoms that aren't carbon or hydrogen *are* drawn, along with their attached hydrogens. So the structure of cyclohexane (C₆H₁₂) is just a hexagon. The structure of methylcyclohexane (C₇H₁₄) is a hexagon with a single line sticking off one corner.

Skeletal structures look bare the first time. They become natural quickly because they highlight what changes in a reaction (functional groups, named atoms, the locations where bonds break and form) and suppress what doesn't (the carbon-hydrogen scaffolding). For the rest of this book, skeletal structures are the default. Get used to mentally adding hydrogens to bring every carbon up to four bonds.

Reading a skeletal structure: the *end* of any line is a CH₃. A two-line intersection (where one carbon connects to two others) is a CH₂. A three-line intersection is a CH. A four-line intersection (rare in organic chemistry but possible) is just C, with no hydrogens. When other atoms — O, N, halogens — are drawn explicitly, their hydrogens are usually drawn too, except in long-form structures where conventions vary.

## What this chapter does

The atom is mostly empty space with a tiny dense nucleus and electrons in orbitals. The chemistry is decided by the valence shell. Carbon's four valence electrons want partners, and the way they get them is through covalent bonds — pairs of electrons shared between atoms. Hybridization tells you the geometry: sp³ for single bonds (tetrahedral), sp² for double bonds (planar), sp for triple bonds (linear). Skeletal structures are the working notation.

That is the apparatus. It's enough to start.

What's coming next is functional groups — the small, named arrangements of atoms (C=O, OH, NH₂, COOH) that determine how a molecule reacts. The reason functional groups matter is that bond polarity, electron density, and steric availability are predictable from hybridization and orbital geometry. Once you can read a skeletal structure and recognize the hybridization at every atom, you can predict where reactions will happen and what kinds of bonds will form. The carbon backbone is mostly inert; the functional groups do the work.

The methane puzzle from the start of the chapter — why all four C–H bonds are identical — is no longer mysterious. Carbon doesn't bond using its raw 2s and 2p orbitals. It rebuilds them into four equivalent sp³ hybrids and uses those. The molecule arranges itself to be at the lowest energy, and the lowest energy comes from putting four identical bonds at the corners of a tetrahedron. The geometry follows from the energy, and the energy follows from the orbitals.

That order — orbitals → energy → geometry → reactivity — is the thread the rest of the book pulls on.

---

*Source for all data, examples, and historical references: OpenStax* Organic Chemistry*, Chapter 1, modules m00157 through m00169.*
---

## LLM Exercise — Chapter 1: Structure and Bonding (Synthesize a Target Molecule Project)

**Project:** Synthesize a Target Molecule — across the semester, pick one real target molecule (drug, natural product, or industrial chemical) and develop a complete retrosynthetic analysis + forward synthesis. By Chapter 31: a 5,000–8,000 word synthesis document with mechanism arrows, spectra predictions, and a literature comparison.
**What you're building this chapter:** the project's foundation — pick your target, draw it, and analyze every bond, hybridization, and geometry.
**Tool:** **Claude Project** "Synthesis of [Your Molecule]" — every later chapter adds a section to a single document. Save the structure as a clean image (use ChemDraw, MarvinSketch, or sketch-and-photo).

---

**The Prompt:**

```
I'm starting a semester-long project to design a complete synthesis
of one real target molecule. Each chapter, I'll either analyze part
of the molecule's structure or propose a synthetic step. By Chapter
31: a complete retrosynthesis + forward synthesis with mechanism
arrows.

Help me set up the project. Ask me ONE question at a time, waiting
for my answer.

1. Pick the target. Pick ONE molecule from this list (or propose a
   sharper one in the same shape):
   - DRUGS: aspirin, ibuprofen, naproxen, paracetamol/
     acetaminophen, atorvastatin (Lipitor), sertraline (Zoloft),
     sildenafil (Viagra), taxol/paclitaxel, simvastatin,
     amoxicillin, omeprazole, fluoxetine (Prozac), morphine,
     oxycodone, diphenhydramine (Benadryl).
   - NATURAL PRODUCTS: vanillin, caffeine, capsaicin, menthol,
     camphor, salicin, quinine, nicotine, morphine, taxol.
   - INDUSTRIAL CHEMICALS: BHT, BHA, vanillin (synthetic),
     aspartame, saccharin, PET monomer, nylon-6,6 monomer,
     methacrylic acid.
   The target must (a) have enough functional-group diversity to
   touch most chapters, (b) have a documented synthesis you can
   compare against in Chapter 31, (c) be something you care
   enough about to spend 31 chapters on.

2. Why this target. One paragraph on why you picked it — pre-med
   relevance? Personal interest? Commercial importance? The
   answer doesn't matter, but having one answer helps you finish.

3. Find a published synthesis. Locate a published industrial or
   research synthesis for comparison in Chapter 31. Note the
   citation (DOI if available, or a textbook/Wikipedia reference).
   Don't memorize it — but know it exists.

4. Draw the structure. Use ChemDraw, MarvinSketch, an iPad sketch
   app, or a hand-drawn-and-photographed sketch. Save the image
   to your Claude Project.

After all four answers, write a 400–600 word **Target Profile**
section. Cover:

- The target's name and structure (image link).
- Its molecular formula and molecular weight.
- Its commercial/biological significance.
- For each atom in the molecule (or each unique atom type):
  hybridization (sp³/sp²/sp) and geometry. Be thorough — every
  carbon matters.
- Identify any unusual bonding situations: aromatic rings, conjugated
  systems, strained rings, hypervalent atoms.
- Note any formal charges or unusual bond patterns.

End with a "What I Don't Yet Know" list of 5 things about this
molecule's synthesis that the analysis will need to address. These
become the project's working questions.
```

---

**What this produces:** A 400–600 word Target Profile section + structure image. The list of unknowns at the end becomes the project's working agenda.

**How to adapt this prompt:**

- *For your own project:* Don't pick a target with no published synthesis (e.g., a hypothetical molecule). The Chapter 31 literature comparison is the project's most valuable piece.
- *For ChatGPT / Gemini:* Works as written.
- *For Claude Code:* Optional — for any computational chemistry sanity-checks (e.g., orbital visualizations via RDKit).
- *For a Claude Project:* Essential. The Target Profile lives in the project's instructions; every later chapter loads it as context.

**Connection to previous chapters:** This is the project's opening.

**Preview of next chapter:** Chapter 2 covers acid-base behavior. You'll identify every acidic and basic site on your target, rank them by pKa, and predict any acid-base behavior the synthesis will need to handle (especially relevant for drug molecules where protonation states matter for activity).


---

## AI Wayback Machine

**Friedrich August Kekulé** was proposed the ring structure of benzene in 1865 — reportedly after dreaming of a snake biting its own tail.

**Run this:**

```
Who is Friedrich August Kekulé, and how does their work connect to structure and bonding we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about their career or ideas.
```

→ Search **"Friedrich August Kekulé"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to walk through one of Friedrich August Kekulé's key experiments or syntheses in detail.
- Add a constraint: "Answer including criticisms or limits of Friedrich August Kekulé's framework."

What changes? What gets better? What gets worse?
