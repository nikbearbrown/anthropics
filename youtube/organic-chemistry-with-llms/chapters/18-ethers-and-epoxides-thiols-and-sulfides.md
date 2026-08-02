# Chapter 18 — Ethers and Epoxides; Thiols and Sulfides

*Ethers are mostly inert. Epoxides — three-membered ring ethers — are remarkably reactive. The same C–O–C connectivity, but a 60° bond angle instead of 110°, changes the chemistry completely.*

A diethyl ether bottle on a chemistry shelf has been sitting there since 1856 (the year diethyl ether was first introduced as a surgical anesthetic) doing essentially nothing. Ethers are spectacularly unreactive functional groups under most conditions. They're used as solvents (diethyl ether, THF, dioxane) precisely because they don't get in the way of the reactions you're trying to run.

But there's a special case. Replace the open-chain ether's geometry with a three-membered ring, and the C–O–C bond angle compresses from 110° to about 60°. The bonds are bent, the ring is strained by about 25 kJ/mol, and suddenly the molecule is one of the most reactive functional groups in organic chemistry. The strained three-membered ring (an *epoxide*) opens readily under nucleophilic attack, even by relatively poor nucleophiles. The driving force is relief of ring strain.

This contrast — ethers nearly inert, epoxides remarkably reactive — is the central theme of the chapter. Same connectivity (C–O–C), different geometry, completely different chemistry. The pedagogical point is that geometry matters as much as connectivity in determining how a molecule behaves.

The chapter also briefly covers thiols (R–S–H) and sulfides (R–S–R′), the sulfur analogs of alcohols and ethers. Sulfur's larger size and higher polarizability give it some specific roles in biology — most notably, the disulfide bonds that hold proteins in their folded shapes.

## Ethers

An ether is R–O–R′, with two organic groups attached to oxygen. The geometry around oxygen is tetrahedral (sp³), with two lone pairs and two bonds. The C–O–C bond angle is about 110°. Ethers are weakly polar (the C–O dipole is small) and have a small dipole moment — typically not large enough to substantially affect boiling point relative to alkanes of the same size.

Naming: simple ethers are usually named with the two organic groups followed by "ether" — diethyl ether (CH₃CH₂OCH₂CH₃), methyl phenyl ether (CH₃OC₆H₅, also called *anisole*). When the ether is part of a larger molecule, it can be treated as an *alkoxy* substituent on the parent — methoxybenzene = anisole. Cyclic ethers have their own names: tetrahydrofuran (THF) is the saturated five-membered ring, dioxane is the six-membered ring with two O's, and so on.

Ethers are widely used as solvents: ethers dissolve a wide range of organic compounds, are non-protic (no O–H), and are usually unreactive under typical reaction conditions. Diethyl ether is the standard solvent for Grignard reactions. THF is used when a higher boiling point is needed.

A practical hazard: low-molecular-weight ethers (diethyl, diisopropyl) react slowly with air to form *peroxides* — explosive contaminants that build up in old or improperly stored ether. Always check for peroxides before distilling old ether (a peroxide-detection strip turns blue if peroxides are present), and never distill to dryness.

## Williamson ether synthesis

The standard method for making an ether is the *Williamson ether synthesis*: an alkoxide ion attacks a primary alkyl halide via SN2.

$$\text{R}{-}\text{O}^- + \text{R'X} \longrightarrow \text{R}{-}\text{O}{-}\text{R'} + \text{X}^-$$

The alkoxide is generated from the alcohol with a strong base (NaH, NaNH₂, alkali metal). The alkyl halide must be primary (or, less commonly, methyl) — secondary and tertiary substrates undergo E2 elimination instead.

When making an unsymmetric ether (R ≠ R′), strategy: pick the side that comes from an alcohol → alkoxide → reaction with an *alkyl halide* whose group is the smaller, less hindered one. So *tert*-butyl methyl ether is best made from *tert*-butoxide + iodomethane, *not* from methoxide + 2-chloro-2-methylpropane (which would give E2 elimination instead of substitution).

A variant uses silver oxide (Ag₂O) instead of free alkoxide, with the alkyl halide and alcohol mixed directly. The Ag⁺ helps the leaving group depart and avoids needing a separate alkoxide-formation step. Useful for sensitive substrates.

## Alkoxymercuration

For ethers where one R is from an alkene, alkoxymercuration is an alternative: alkene + alcohol + Hg(OAc)₂, then reduction with NaBH₄. Mechanism is parallel to oxymercuration in Chapter 8 — Hg-bridged intermediate, alcohol attacks, Markovnikov regiochemistry. Useful when the Williamson method runs into problems with hindered substrates.

## Reactions of ethers

Ethers are remarkably unreactive. The major reactions are:

**Acidic cleavage with HX.** With concentrated HBr or HI at high temperature, an ether is protonated at oxygen (giving an oxonium ion) and then attacked by the iodide or bromide. The result is two products: an alkyl halide and an alcohol.

$$\text{R}{-}\text{O}{-}\text{R'} + \text{HI} \longrightarrow \text{R}{-}\text{OH} + \text{R'}{-}\text{I}$$

The mechanism follows SN1 or SN2 logic depending on the substrate. With one tertiary side (like methyl *tert*-butyl ether), SN1 dominates, and the I⁻ ends up on the tertiary carbon (giving *tert*-butyl iodide and methanol). With two primary sides, SN2 dominates, and the I⁻ ends up on the less hindered carbon.

HCl is too weak to cleave most ethers. HF doesn't cleave ethers under normal conditions. Acidic ether cleavage is the only reliable way to break a simple ether bond.

**Auto-oxidation.** As mentioned, ethers form peroxides on standing in air. The mechanism is a radical chain initiated by trace impurities. The peroxides accumulate slowly and can become explosive concentrations over months to years.

That's about it for simple ether chemistry. Ethers are unreactive; the lab uses them to *avoid* doing chemistry on the solvent.

## Epoxides

Now the special case. An *epoxide* is a three-membered ring with two carbons and one oxygen. The bond angles in the ring are forced to about 60° (rather than the normal 109.5° for sp³ atoms), giving substantial angle strain — about 27 kJ/mol per epoxide.

Epoxides are made:
- From alkenes by epoxidation with mCPBA (Chapter 8). Concerted, syn addition of an oxygen to the alkene.
- From halohydrins by intramolecular SN2: the OH (deprotonated to alkoxide by base) attacks the carbon bearing the halide from the back side, displacing the halide and forming the three-membered ring.

The strain in the ring makes epoxides reactive. They're attacked by nucleophiles much more readily than ordinary ethers. The strain pays off in opening the ring.

## Reactions of epoxides

**Acid-catalyzed ring opening.** With aqueous acid, an epoxide is protonated to give an oxocarbenium-like intermediate; water then attacks. The result is a 1,2-diol (also called a vicinal diol) with overall *trans* stereochemistry (because the water attacks from the back side of the protonated epoxide).

The regiochemistry under acid catalysis: the more substituted carbon of the original alkene gets attacked. This is because the protonated epoxide has more positive character on the more substituted carbon (it can form a more stable carbocation-like species). Under acid catalysis, the regiochemistry tends toward Markovnikov.

**Base-catalyzed ring opening.** Without acid, with a basic nucleophile (HO⁻, RO⁻, RS⁻, RNH₂, etc.), the nucleophile attacks the *less substituted* carbon. Why? Because no protonation activates the epoxide; the nucleophile attacks via a normal SN2-like mechanism, going for the less hindered side. This is anti-Markovnikov regiochemistry.

So an epoxide can open under acid to give a Markovnikov product, or under base to give the anti-Markovnikov product. The same starting material gives different regiochemistry depending on conditions.

**Other nucleophiles.** Grignard reagents and organolithiums open epoxides too. The product is an alcohol with a new C–C bond. R–MgX + epoxide → R–CH(OH)–CH₂–R′ (or similar). This is one of the cleanest ways to extend a chain by two carbons.

**Rearrangement under strong acid.** Epoxides can rearrange to ketones or aldehydes (Meinwald rearrangement) under strong acid catalysis, particularly with Lewis acids. The result depends on the substrate.

The synthetic usefulness of epoxides is hard to overstate. They're flexible electrophiles — opening with water gives diols, with alcohols gives ether-alcohols, with amines gives amino-alcohols, with carbon nucleophiles gives extended carbon chains with an alcohol. Once you have the alkene-to-epoxide route from Chapter 8, you have a one-carbon (or two-carbon, depending on how you count) extension that's useful all over synthesis.

## Crown ethers

A crown ether is a cyclic polyether — a ring containing several O atoms (typically 4 to 8) connected by ethylene linkers. The cavity in the middle of the ring is the right size to bind a metal cation through coordination of the oxygen lone pairs.

The most common: 18-crown-6 (six oxygens in an 18-membered ring), which strongly binds K⁺ in its cavity. 12-crown-4 binds Li⁺. 15-crown-5 binds Na⁺. The cavity sizes match the cation sizes.

Crown ethers are useful because they solubilize ionic salts (like KMnO₄, NaCN, KF) in nonpolar organic solvents. The crown binds the cation; the anion goes along with the now-organic-soluble pair. The "naked" anion in solution becomes much more nucleophilic (no solvation cage).

In synthesis, crown ethers are used to make reactions go in unusual solvents (e.g., do KMnO₄ oxidations in benzene), to enhance nucleophilicity (KCN in acetonitrile with 18-crown-6), and to control stereochemistry of ionic reactions.

The original work on crown ethers, by Charles Pedersen, was recognized with the 1987 Nobel Prize in chemistry.

## Thiols

A thiol is R–S–H — like an alcohol, but with sulfur instead of oxygen. The S–H bond is much weaker than the O–H bond (about 365 vs. 437 kJ/mol), and the hydrogen is more acidic (pKa about 10 for ethanethiol, vs. 16 for ethanol). The lower pKa makes thiols easier to deprotonate and useful as nucleophiles in mild conditions.

Thiols have very strong, often unpleasant smells. Methanethiol (CH₃SH) is the smell of skunk spray (along with related thiols and disulfides). Ethanethiol is added to natural gas to give it its detection-warning smell. Thiols are often used in small amounts in synthesis, with care.

Thiols are made by:
- Sulfide ion (HS⁻) attacking an alkyl halide via SN2.
- Reduction of disulfides.

The most distinctive reaction of thiols is their oxidation to *disulfides*:

$$2\,\text{R}{-}\text{S}{-}\text{H} \xrightarrow{\text{[O]}} \text{R}{-}\text{S}{-}\text{S}{-}\text{R} + 2\,\text{H}^+ + 2\,\text{e}^-$$

The S–S bond is significantly stronger than two S–H bonds (the disulfide is the favored product under mild oxidative conditions). The reaction is reversible — disulfides can be reduced back to thiols with reducing agents (DTT, β-mercaptoethanol, TCEP).

In biology, the disulfide bond is a key structural feature of many proteins. Cysteine residues in proteins can form disulfide bonds with other cysteine residues (within the same protein or between different proteins), holding the folded structure in place. Reducing the disulfide bonds (with DTT or similar reagents) unfolds the protein. This is a common step in protein-purification workflows.

## Sulfides

A sulfide is R–S–R′ — the sulfur analog of an ether. Like ethers, sulfides are less reactive than the corresponding alcohols/thiols. The S–C bond is reasonably strong, and the molecule is largely inert to most nucleophilic substitutions.

Sulfides are made by the Williamson-analog reaction: a thiolate (deprotonated thiol, RS⁻) plus a primary alkyl halide gives a sulfide via SN2. The thiolate is a much better nucleophile than the alkoxide (sulfur is bigger, more polarizable, and the negative charge is more delocalized), so the reaction works well even with relatively unreactive alkyl halides.

Sulfides can be oxidized to *sulfoxides* (R–S(=O)–R′) and *sulfones* (R–S(=O)₂–R′) with H₂O₂ or peroxyacids. Each oxidation step adds one oxygen to the sulfur. Dimethyl sulfoxide (DMSO) is dimethyl sulfide's sulfoxide; it's the workhorse aprotic solvent in many SN2 reactions. Methyl phenyl sulfoxide and other chiral sulfoxides have been used as chiral auxiliaries in asymmetric synthesis.

In biology, *S*-adenosylmethionine (SAM) — which we met in Chapter 11 — is a sulfide whose central sulfur has been alkylated (by adenosine) to give a sulfonium ion. SAM transfers methyl groups in many enzymatic reactions, acting as nature's CH₃Cl.

↳ **Dig Deeper — Why epoxide ring-opening regiochemistry depends on conditions**

> Acid-catalyzed epoxide opening gives Markovnikov regiochemistry (nucleophile on more substituted carbon); base-catalyzed opening gives anti-Markovnikov (nucleophile on less substituted carbon). Walk through the mechanism carefully. Cover: how protonation of the epoxide oxygen makes the C–O bonds polar in both directions (more positive character on the more substituted carbon), why this electronic effect dominates over steric effects under acid conditions, and why the steric effect dominates under base conditions where there's no protonation. Use the case of 2,2-dimethyloxirane (an asymmetric epoxide) opening with methanol under acid vs. base.

**What to do with the output:** Verify the explanation with a concrete substrate. The 2,2-dimethyloxirane case is clean — the more substituted carbon is the quaternary one, and acid opening puts the methoxide on it, while base opening puts the methoxide on the less substituted carbon.

## What this chapter does

Ethers (R–O–R′) are mostly inert and used as solvents. The major reaction is acidic cleavage (HBr or HI), which gives an alkyl halide and an alcohol via SN1 or SN2 depending on the substrate.

Epoxides — three-membered ring ethers — are an exception. The 60° ring angle gives substantial strain, making the C–O bonds reactive. Epoxides open under acid catalysis (Markovnikov) or base catalysis (anti-Markovnikov), giving 1,2-disubstituted products with anti stereochemistry. Carbon nucleophiles (Grignards) can also open epoxides, extending the carbon framework.

Epoxides are made by alkene oxidation with mCPBA (concerted, syn) or by halohydrin cyclization (intramolecular SN2).

Thiols (R–S–H) are sulfur analogs of alcohols, with lower pKa (about 10) and stronger nucleophilicity. They undergo characteristic oxidation to disulfides — the S–S bond holding two thiols together. The disulfide bond is reversible under reducing conditions and is a major structural feature of folded proteins.

Sulfides (R–S–R′) are sulfur analogs of ethers, made by a Williamson-style alkylation of thiolates. They can be further oxidized to sulfoxides and sulfones, and the sulfonium ion (R₃S⁺) is a key biological methylation agent in the form of SAM.

The next chapter (19) starts the long carbonyl chemistry sequence — aldehydes and ketones, then carboxylic acids and derivatives, then α-substitution and condensation. The carbonyl group is the largest single reactivity domain in organic chemistry, and we'll spend the next four or five chapters on it.

---

*Source for all data, examples, and historical references: OpenStax* Organic Chemistry*, Chapter 18, modules m00211 through m00219.*
---

## LLM Exercise — Chapter 18: Ethers, Epoxides, Thiols, Sulfides (Synthesize a Target Molecule Project)

**Project:** Synthesize a Target Molecule.
**What you're building this chapter:** ether/epoxide/thiol analysis and synthesis step if applicable.
**Tool:** **Claude Project**.

---

**The Prompt:**

```
Chapter 18 of my Synthesis project. Chapter 18 taught: ethers
(R-O-R, generally inert; cleavable by HX); epoxides (3-membered
ring containing O; strained, reactive; opened by nucleophiles
under acid OR base, with different regiochemistry); Williamson
ether synthesis (alkoxide + alkyl halide → ether via SN2); thiols
and sulfides (sulfur analogs, more nucleophilic than O analogs).

Write the brief's "Ethers, Epoxides, Sulfur" section in 250–400
words.

1. **Identify any ether linkages in your target.** Note each
   R-O-R or R-O-Ar pattern.

2. **Propose installation.** For each ether:
   - Williamson synthesis (alkoxide + R-X).
   - From an alkene + alcohol with acid catalyst (less common).
   - From an epoxide ring-opening with an alcohol nucleophile.

3. **Epoxides.** If your target has an epoxide (unusual in final
   targets but common as intermediates), propose its installation:
   - From alkene + mCPBA (peroxyacid).
   - From halohydrin + base.
   - As a stereospecific intermediate for ring-opening reactions.

4. **Epoxide ring-opening regiochemistry.** If epoxides feature
   as intermediates:
   - Acid conditions: nucleophile attacks the MORE-substituted
     carbon (carbocation-like transition state).
   - Base conditions: nucleophile attacks the LESS-substituted
     carbon (SN2-like).
   Choose the conditions for your desired outcome.

5. **Thiols and sulfides.** If your target contains sulfur (some
   drugs do — captopril, penicillins, others — and many biological
   molecules have S):
   - Thiols (R-SH) are MORE nucleophilic and acidic than alcohols.
   - Sulfides (R-S-R) are less reactive than ethers in most
     cases but can be oxidized to sulfoxides and sulfones.

End with: would an ether bond in your target be best formed
late in the synthesis (after sensitive groups are installed) or
early (to use the ether linkage as a structural anchor)?
```

---

**What this produces:** A 250–400 word section.

**Connection to previous chapters:** Ch 17 (alcohols) → Ch 18 (their derivatives). Alkoxide from Ch 17 + alkyl halide from Ch 10 = Williamson ether.

**Preview of next chapter:** Chapter 19 covers aldehydes and ketones — nucleophilic addition reactions. Many drugs have carbonyl-containing functional groups, so this chapter often contributes multiple steps to the synthesis.


---

## AI Wayback Machine

**Alexander Williamson** was developed the ether synthesis bearing his name in 1850 — and his work on equilibrium founded modern chemical kinetics.

**Run this:**

```
Who is Alexander Williamson, and how does their work connect to ethers and epoxides we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about their career or ideas.
```

→ Search **"Alexander Williamson"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to walk through one of Alexander Williamson's key experiments or syntheses in detail.
- Add a constraint: "Answer including criticisms or limits of Alexander Williamson's framework."

What changes? What gets better? What gets worse?
