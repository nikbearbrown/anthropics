# Chapter 6 — An Overview of Organic Reactions

*Reactions don't memorize themselves. The way to learn them is to recognize the four types, see how electrons move within each, and understand the energy bookkeeping that makes some happen and others not.*

There are tens of millions of known organic reactions. No textbook can teach them all, and no chemist remembers them all. The reason organic chemistry is learnable at all — the reason this book has 31 chapters and not 31,000 — is that almost every organic reaction is one of four types, with electrons moving in one of two ways, in response to one of a small handful of energetic considerations.

This chapter introduces the framework. After this point, every new reaction you meet should be slotted into the framework — *addition, elimination, substitution, or rearrangement*; *polar or radical*; *fast or slow because of activation energy that depends on transition-state geometry*. The slotting is the act of understanding. Memorizing the reactions one at a time, without the framework, is the way undergraduates fail organic chemistry. With the framework, almost every reaction in the rest of this book becomes a variation on a theme you already know.

## Four kinds of reactions

Every organic reaction takes a starting material and turns it into a product. There are four ways the bonds can change:

**Addition.** Two molecules combine to give one. Some atoms or groups attach to a starting material, increasing the total bond count. The classic examples involve double bonds: an alkene plus a hydrogen halide gives an alkyl halide. The C=C double bond becomes a C–C single bond, and two new bonds form, one to H and one to X.

$$\text{H}_2\text{C}=\text{CH}_2 + \text{HBr} \longrightarrow \text{CH}_3\text{CH}_2\text{Br}$$

Two molecules in, one molecule out. The double bond is gone; two new single bonds have formed.

**Elimination.** The reverse of addition. One molecule splits into two molecules with the formation of a new multiple bond. An alkyl halide loses HX to form an alkene; an alcohol loses H₂O to form an alkene. The pattern: lose a small molecule, gain a multiple bond.

$$\text{CH}_3\text{CH}_2\text{Br} + \text{base} \longrightarrow \text{H}_2\text{C}=\text{CH}_2 + \text{HBr}$$

**Substitution.** One group replaces another. The total number of bonds doesn't change; the partners do. An alkyl halide reacting with a nucleophile to give a product with a different group attached: the C–X bond breaks, a new C–Nu bond forms.

$$\text{CH}_3\text{Br} + \text{HO}^- \longrightarrow \text{CH}_3\text{OH} + \text{Br}^-$$

**Rearrangement.** A single molecule reorganizes — atoms move, bonds shift, but no net molecules come or go. A common example: a primary carbocation reorganizing to a secondary or tertiary carbocation by migrating a hydride (H with both electrons) or methyl group (CH₃ with both electrons) from an adjacent carbon. The substrate before and after has the same atoms and bonds in different places.

Almost every reaction in this book is one of these four. Once you can spot which one is happening, the question reduces to *how* — what intermediates, what transition states, what conditions.

## Polar reactions vs. radical reactions

The other classification axis is how electrons move during the reaction.

**Polar reactions** involve heterolytic bond breaking and forming — electrons move in pairs. A bond breaks with both electrons going to one atom, leaving that atom with a lone pair (and a negative charge if it gained more than its share) and the other atom with an empty orbital (and a positive charge). New bonds form by an atom with a lone pair donating that pair to an atom with an empty orbital.

This electron-pair flow is what curly arrows track. A curly arrow with a full head represents the movement of two electrons. The tail of the arrow shows where the electrons started; the head shows where they're going. In a polar reaction, every step can be drawn with curly arrows, and every arrow involves two electrons.

Polar reactions need a *nucleophile* (electron-rich, donates the pair) and an *electrophile* (electron-poor, accepts the pair). The vocabulary: nucleophile = "nucleus-lover" = looking for positive charge, has a lone pair to give. Electrophile = "electron-lover" = looking for electron density, has an empty orbital or weak bond to take the pair into.

Most reactions in this book are polar. The substitutions and eliminations from Chapter 11 are polar. The carbonyl additions in Chapter 19 are polar. The Friedel-Crafts and other electrophilic aromatic substitutions in Chapter 16 are polar.

**Radical reactions** involve homolytic bond breaking and forming — electrons move singly. A bond breaks with one electron going to each atom. Each atom now has an unpaired electron and is called a *radical*. New bonds form when two radicals combine (their unpaired electrons pair up) or when a radical attacks a multiple bond (taking one of its electrons and leaving the other on a new radical).

Radical-arrow notation uses single-headed (fishhook) arrows, each representing the movement of one electron. A homolytic bond cleavage uses two fishhook arrows pointing in opposite directions from the bond being broken — one electron to each atom.

Radical reactions are the minority pattern, but they're not rare. Combustion is radical chemistry. Halogenation of alkanes (Chapter 10) is radical. Polymer synthesis often runs by radical mechanisms. Biological reactions involving oxygen — including some metabolic reactions — go through radical intermediates.

The two classifications are independent. A reaction can be:
- Polar substitution (SN1, SN2 — Chapter 11)
- Polar addition (alkene + HBr — Chapter 8)
- Polar elimination (E1, E2, E1cB — Chapter 11)
- Radical substitution (alkane + Cl₂ + light — Chapter 10)
- Radical addition (HBr + alkene with peroxides, anti-Markovnikov)
- And so on.

The combination tells you a lot about how the reaction works.

## Bond polarity and where reactions happen

A polar reaction can only happen at a polar bond — a place where the electrons aren't shared equally and there's already a partial positive or partial negative charge. That polarity is the entry point.

Every functional group has a characteristic polarity pattern:

- **C–O, C–N, C–halide:** carbon is δ⁺, the heteroatom is δ⁻. Carbon is electrophilic.
- **C=O (carbonyl):** carbon is δ⁺, oxygen is δ⁻. Strongly electrophilic carbon, available for nucleophile attack.
- **C=C (alkene):** the two carbons are equivalent, but the π electrons are loosely held and can attack an electrophile. The double bond is nucleophilic.
- **O–H, N–H:** the H is δ⁺ (because O and N are more electronegative than H), making the H acidic.
- **C–H:** essentially nonpolar. C–H bonds are spectators in most polar chemistry.

To predict where a reaction will occur, find the polar bonds, identify which end is electrophilic and which is nucleophilic, and look for incoming species of the opposite polarity. A nucleophile (like HO⁻) will attack the electrophilic carbon of a carbonyl. An electrophile (like H⁺) will attack the nucleophilic π electrons of an alkene. The first move in any mechanism is matching the polarities.

Beyond static polarity, there's also *polarizability* — the ease with which an atom's electron distribution can be distorted by an external electric field. Sulfur is more polarizable than oxygen because its valence electrons are in larger, looser orbitals. Iodide is more polarizable than chloride for the same reason. A polarizable atom can develop a temporary partial charge in response to an approaching reactant, even if its starting bond polarity is weak. This is why iodide is such a good nucleophile: not only does it carry a negative charge, but its electron cloud distorts easily to start forming a bond with an approaching electrophile.

## Curly arrows: how to draw a mechanism

A *mechanism* is a step-by-step picture of how reactants become products at the level of electron pairs and partial bonds. It tells you which bonds break, which form, and in what order. Mechanisms are how organic chemistry teaches you to *think* about a reaction, as opposed to just memorizing what comes out.

Curly arrow conventions:

- A full-headed curly arrow shows the movement of *two* electrons.
- The tail of the arrow starts at the source of the electrons (a lone pair, or a bond).
- The head of the arrow points to where the electrons are going (an atom, or between two atoms to indicate a new bond).
- Multiple arrows in a single step mean concerted electron flow — everything happens at once.

A sample step: HO⁻ attacks the carbon of CH₃Br. One curly arrow: from a lone pair on the hydroxide oxygen, to the carbon of CH₃Br. A second curly arrow: from the C–Br bond, to bromine. The two arrows are simultaneous — electrons flow from the nucleophile to carbon, and from carbon to bromine, in one concerted step. The result: HO–CH₃ + Br⁻.

Once you can draw curly arrows correctly, you can describe nearly any polar mechanism. The arrows tell you what's happening; the substrates and conditions tell you whether the step is fast or slow.

## Energy: how to tell whether a reaction will happen

Two things decide whether a reaction will go: thermodynamics (does the product have lower energy than the reactant?) and kinetics (is there an energy barrier the system has to climb to get there?).

The key thermodynamic quantity is the *Gibbs free energy change*, ΔG° (the ° superscript means standard conditions). For a reaction to be thermodynamically favorable — for the equilibrium to favor products — ΔG° must be negative.

ΔG° has two components:

$$ΔG° = ΔH° − TΔS°$$

ΔH° is the *enthalpy change* — the difference in bond energies between products and reactants. Breaking bonds costs energy; forming bonds releases it. If the bonds in products are stronger than the bonds in reactants, ΔH° is negative (exothermic). The reaction releases heat.

ΔS° is the *entropy change* — the change in disorder. Reactions that increase the number of free particles (like elimination, where one molecule becomes two) have positive ΔS°. Reactions that decrease the number (like addition, where two molecules become one) have negative ΔS°. The TΔS° term grows with temperature, which is why elimination tends to dominate over substitution at higher T (the entropy bonus matters more when T is large).

A reaction can have ΔH° > 0 (endothermic) but still have ΔG° < 0 if TΔS° is large and positive. Conversely, a reaction can be exothermic but unfavorable if entropy decreases enough.

The relationship between ΔG° and the equilibrium constant Keq:

$$ΔG° = -RT \ln K_{eq}$$

A ΔG° of −5.7 kJ/mol corresponds to Keq ≈ 10. A ΔG° of −11.4 kJ/mol corresponds to Keq ≈ 100. Each additional 5.7 kJ/mol of negative ΔG° multiplies the equilibrium constant by 10. Most reactions you'll meet in this book have |ΔG°| in the range of 10 to 200 kJ/mol; the corresponding equilibrium constants span up to 10³⁵ or more, meaning the reactions go to essentially complete conversion.

But ΔG° tells you only whether the reaction *can* happen. It doesn't tell you whether it *will* happen at a useful rate. For that, you need kinetics — and kinetics depends on the activation energy.

## The transition state and activation energy

When a reaction happens, the system passes through an intermediate geometry called the *transition state* — the highest-energy structure on the path from reactants to products. The transition state is not a stable molecule; it's a fleeting arrangement that exists only at the moment of bond breaking and forming. It cannot be isolated, but it can be described by the bonds that are partially broken and the bonds that are partially formed.

The energy difference between reactants and the transition state is the *activation energy*, ΔG‡ (read as "delta G double dagger"). This is the barrier the reaction has to climb. A high activation energy means a slow reaction; a low one means a fast reaction. The Arrhenius/Eyring relationship makes this quantitative:

$$\text{rate} \propto e^{-\Delta G^‡/RT}$$

Each 5.7 kJ/mol increase in ΔG‡ slows the rate by a factor of 10 at room temperature. Catalysis works by lowering ΔG‡ — the catalyst stabilizes the transition state, which speeds the reaction without changing the equilibrium.

For a one-step reaction, the energy diagram looks like a single hill. Reactants on the left, products on the right, transition state at the peak. The peak's height above reactants is ΔG‡; the difference between reactant and product valleys is ΔG°.

For multi-step reactions, the diagram has multiple hills with intermediate valleys between them. Each valley is an *intermediate* — a real, if often short-lived, molecule. Each peak is a transition state. The highest peak determines the overall rate; we call its corresponding step the *rate-determining step* or *rate-limiting step*. The reaction can't go faster than this step.

## The Hammond postulate

When a reaction has a high activation energy and a high-energy intermediate, the transition state structurally resembles the intermediate more than the reactant. When activation energy is low and the intermediate is similar to reactants, the transition state resembles the reactants.

This is the *Hammond postulate*: the structure of a transition state resembles whatever it's closer to in energy. For *endothermic* steps (climbing uphill in energy), the transition state is *late* — near the products. For *exothermic* steps (going downhill), the transition state is *early* — near the reactants.

The practical use of this principle is huge. It means: when you want to predict the relative rates of two different reactions that share the same kind of intermediate, you can rank them by the relative stability of their intermediates. The more stable intermediate corresponds to the lower activation energy and thus the faster reaction.

Specifically, in Chapter 11 we used the Hammond postulate to argue that SN1 reactions go faster on tertiary substrates than on primary substrates. The rate-determining step is carbocation formation, which is endothermic. The transition state therefore resembles the carbocation. A more stable carbocation (tertiary) corresponds to a lower transition-state energy, hence a faster reaction. The Hammond postulate is the chain that connects intermediate stability to reaction rate.

We'll use this argument again and again — to explain why electron-donating groups direct electrophilic aromatic substitution to specific positions, why some carbonyl additions are faster than others, why E2 reactions favor the more substituted alkene (Zaitsev's rule), and so on.

## Bond strengths

Many reactions are easier to predict if you know how strong the relevant bonds are. The energy required to break a bond homolytically is the *bond dissociation energy* (BDE) — the energy needed to give two radical fragments.

A few BDE values worth knowing:

| Bond | BDE (kJ/mol) |
|---|---|
| H–H | 436 |
| C–C (alkane) | 377 |
| C=C (π bond) | 273 |
| C=O (π bond) | 380 |
| C–H (methane) | 439 |
| C–H (1° alkyl) | 423 |
| C–H (2° alkyl) | 410 |
| C–H (3° alkyl) | 397 |
| C–H (allylic, benzylic) | 364 |
| O–H (water) | 497 |
| O–H (alcohol) | 437 |
| C–F | 485 |
| C–Cl | 339 |
| C–Br | 285 |
| C–I | 234 |

For an estimate of ΔH° for a reaction, sum the BDEs of bonds broken and subtract the BDEs of bonds formed. This is rough — bond strengths depend on the rest of the molecule, and exact values can shift by 20+ kJ/mol depending on context — but it's enough to tell you whether a reaction is exothermic or endothermic and roughly by how much.

The decreasing BDE going down the halogen series (C–F > C–Cl > C–Br > C–I) is the same trend that explains why iodide is the best leaving group: the bond is the weakest, and once formed, the iodide ion is the most stable.

The decreasing C–H BDE from 1° to 2° to 3° (and especially to allylic and benzylic) explains why radical halogenation is selective: the weakest C–H is the easiest to break, so the radical takes that one. We'll see this in detail in Chapter 10.

↳ **Dig Deeper — Why entropy matters for activation energy too**

> The textbook usually treats ΔG‡ as if it were entirely enthalpic — controlled by bond strengths. But ΔG‡ has both an enthalpy component (ΔH‡) and an entropy component (ΔS‡). Explain when the entropy component dominates. Cover: bimolecular vs. unimolecular reactions, the loss of translational entropy in bimolecular transition states, and why concerted reactions are sometimes "entropy-controlled" while stepwise ones are not.

**What to do with the output:** Compare against any physical organic chemistry textbook section on transition state theory. Verify Claude correctly explains why intramolecular reactions are typically faster than the equivalent intermolecular reactions, even when the intramolecular case has worse geometric alignment.

## How to think about a reaction you've never seen

The toolkit for reading any new reaction:

1. **Classify it.** Addition? Elimination? Substitution? Rearrangement?
2. **Identify the polarity pattern.** Where are the polar bonds in the starting material? Where is the electrophilic site? Where is the nucleophile coming from?
3. **Draw the curly arrows.** What pair of electrons attacks what site? In how many steps?
4. **Identify the intermediates.** Carbocation? Carbanion? Radical? An enol? A tetrahedral oxygen-bearing intermediate?
5. **Predict the rate-determining step.** Which step has the highest activation energy?
6. **Apply the Hammond postulate.** What does the structure of the rate-determining transition state look like?
7. **Predict the major product.** What's the most stable arrangement after all the bond breaking and forming?

By the time you finish this book, all seven of those steps will be automatic for any reaction in your training set. The first time, they'll be slow. With repetition, they become a single coordinated act of recognition.

## What this chapter does

Reactions are not arbitrary. They happen because electrons move from places where they're unstable (high energy, electron-rich) to places where they're more stable (low energy, electron-poor). The four reaction types — addition, elimination, substitution, rearrangement — describe the structural change. The polar/radical distinction describes the electron-flow pattern. The thermodynamic framework (ΔG° = ΔH° − TΔS°) tells you whether the reaction can happen. The kinetic framework (ΔG‡ controls the rate, Hammond postulate links transition states to intermediates) tells you how fast.

These are the tools. Every later chapter is application. The functional groups change, the specific transition-state geometries change, the names of the named reactions change. The toolkit doesn't.

The next chapter starts with alkenes, which is where polar addition chemistry begins.

---

*Source for all data, examples, and historical references: OpenStax* Organic Chemistry*, Chapter 6, modules m00076 through m00087.*
---

## LLM Exercise — Chapter 6: An Overview of Organic Reactions (Synthesize a Target Molecule Project)

**Project:** Synthesize a Target Molecule.
**What you're building this chapter:** the first retrosynthetic disconnection — what's the final bond formed in your target's synthesis?
**Tool:** **Claude Project**.

---

**The Prompt:**

```
Chapter 6 of my Synthesis project. Prior sections in this Claude
Project. Chapter 6 taught: reaction classes (addition, substitution,
elimination, rearrangement); reaction energy diagrams (transition
states are local maxima; intermediates are local minima); rate
(kinetics) vs. equilibrium (thermodynamics); kinetic vs. thermodynamic
products; the arrow-pushing convention (curved arrows from electron-
rich source to electron-poor sink).

Write the brief's "Retrosynthetic Disconnection — Step 1" section
in 400–600 words.

1. **State the retrosynthesis frame.** Retrosynthesis works
   BACKWARD from the target. Each "disconnection" identifies a
   bond and proposes the two halves (synthons) that, when
   reacted together, would form that bond.

2. **Identify the LAST bond to be formed in your synthesis.**
   This is the most consequential single decision in
   retrosynthesis. The criteria:
   - Reliability: known, high-yielding reaction.
   - Convergence: combine two roughly-equal-sized halves rather
     than building from a long linear chain.
   - Functional-group compatibility: late steps shouldn't have to
     install delicate functional groups; install them earlier.

3. **Propose the disconnection.** Draw your target with one bond
   marked as the "final" bond. Show the two synthons (the
   theoretical halves). For each synthon, propose the actual
   reagent that would deliver it:
   - Carbon nucleophile (e.g., Grignard, organolithium, enolate).
   - Carbon electrophile (e.g., alkyl halide, carbonyl, epoxide).

4. **Classify the disconnection.** Which reaction class does this
   correspond to?
   - Addition (e.g., Grignard + aldehyde → alcohol).
   - Substitution (e.g., alkyl halide + nucleophile → product +
     LG).
   - Elimination (e.g., dehydration to form alkene).
   - Rearrangement (less common in retrosynthesis).

5. **Sketch the reaction energy diagram.** Where do the
   transition state and any intermediates sit on the energy
   curve? Is the reaction exergonic (downhill, K > 1) or
   endergonic (uphill, K < 1)? Is the rate-limiting step the
   first or a later step?

6. **The arrows.** Push arrows for the proposed final step. Show
   electron flow from the nucleophile's lone pair / pi system to
   the electrophilic carbon. Show the leaving group departing
   with its bonding electrons. Get this right — it's the
   foundation for every later mechanism in the project.

End with one alternative disconnection you considered but
rejected. Name why it was worse than the chosen one. The
rejected-alternatives discipline trains real retrosynthesis.
```

---

**What this produces:** A 400–600 word Retrosynthetic Step 1 section. The "rejected alternative" framing is the discipline this chapter is training.

**How to adapt this prompt:**

- *For your own project:* Don't aim for the most exotic disconnection. The best retrosynthesis uses well-precedented reactions; the second-best uses well-precedented reactions; etc.
- *For ChatGPT / Gemini:* Works as written.
- *For Claude Code:* Not the primary tool here.
- *For a Claude Project:* Append.

**Connection to previous chapters:** Chapters 1–5 analyzed the target's structure; Chapter 6 begins the synthesis design.

**Preview of next chapter:** Chapter 7 covers alkene structure and reactivity. If your target contains or can be made from alkenes, this chapter is central. Even if not directly, alkene intermediates appear in many syntheses.


---

## AI Wayback Machine

**Friedrich Wöhler** was synthesized urea from inorganic ammonium cyanate in 1828 — toppling the doctrine that organic compounds required a "vital force".

**Run this:**

```
Who is Friedrich Wöhler, and how does their work connect to organic reactions we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about their career or ideas.
```

→ Search **"Friedrich Wöhler"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to walk through one of Friedrich Wöhler's key experiments or syntheses in detail.
- Add a constraint: "Answer including criticisms or limits of Friedrich Wöhler's framework."

What changes? What gets better? What gets worse?
