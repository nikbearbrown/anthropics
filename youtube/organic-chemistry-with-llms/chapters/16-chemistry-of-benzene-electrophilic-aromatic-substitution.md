# Chapter 16 — Chemistry of Benzene: Electrophilic Aromatic Substitution

*Aromatic rings react with electrophiles, not by adding to a double bond, but by substituting one H for the electrophile. The aromatic system is preserved, the chemistry is rich, and substituents already on the ring control where the next one goes.*

The chemistry of substituted benzenes is more sensitive to structural detail than almost any other chemistry in this book. A methyl group on the ring activates electrophilic substitution by a factor of about 25 over benzene itself; a nitro group deactivates it by a factor of more than 10⁷. The methyl group directs new substituents to the ortho and para positions; the nitro group directs them to meta. Two seemingly small structural changes — one electron-donating, one electron-withdrawing — produce dramatic shifts in both reactivity and regiochemistry.

This sensitivity is what makes aromatic chemistry such a precise tool. If you understand the patterns, you can predict where a new group will go on a complex substrate, and you can plan the order of substitutions to build any substituted benzene you want. Drug design and synthesis make heavy use of this control: most modern small-molecule drugs are built around substituted benzene scaffolds, and the position of each substituent is consequential for binding to a protein target.

This chapter covers the mechanism of electrophilic aromatic substitution, the major reactions (halogenation, nitration, sulfonation, Friedel-Crafts alkylation and acylation), the directing effects of substituents already on the ring, and a brief note on nucleophilic aromatic substitution (which works by a different mechanism and only on specific substrates).

## The mechanism in one shape

Every electrophilic aromatic substitution (EAS) goes through the same two-step pattern:

**Step 1.** An electrophile E⁺ attacks the π system of the benzene ring. The π electrons form a new C–E bond. One of the ring carbons becomes sp³ (with E attached and an H still attached). The other five carbons retain their sp² hybridization and now hold a +1 charge spread over them via resonance — three resonance structures with the positive charge on alternating carbons. This intermediate is called a *benzenium ion*, *arenium ion*, or *Wheland intermediate*. It has lost aromaticity.

**Step 2.** A base (often the conjugate base of the proton source from step 1, or just whatever is around) deprotonates the sp³ carbon. The two C–H bond electrons go back into the π system. Aromaticity is restored. The product is the substituted benzene with E in place of H.

Net result: an H on the ring has been replaced by E. The aromatic system is intact. The reaction is *substitution*, not addition.

The intermediate Wheland ion is the key. It has *non-aromatic* π character (5 sp² carbons in a row with a positive charge — like an open allylic cation, but trapped in a ring), and that's why the energy barrier is high. But once the H is lost in step 2, aromaticity is restored, and the system pays back essentially the entire energy cost of breaking aromaticity. The overall reaction is energetically downhill (substitution is not a high-energy reaction), even though the rate-determining step (Wheland ion formation) has a high transition-state energy.

Compare this to addition: in alkene addition (Chapter 8), a similar electrophile attack gives a carbocation that is *not* in an aromatic system. There's no aromaticity to disrupt, so the cost is lower. But there's also no energetic incentive to lose H⁺ at the end, so the cation is captured by a nucleophile instead. The reaction goes addition rather than substitution.

For benzene, the situation flips. The carbocation in the middle of the ring is high in energy (because the ring has lost aromaticity), but the loss of H⁺ to restore aromaticity is so strongly favored that the substitution pathway wins. Different substrate, different mechanism choice.

## Halogenation

Benzene + Br₂ + FeBr₃ → bromobenzene + HBr.

The Fe³⁺ in FeBr₃ acts as a Lewis acid, taking a lone pair from one of the bromines of Br₂. The resulting Br–FeBr₃⁺ complex has a δ⁺ on the other bromine, making it electrophilic enough to react with benzene's π system. After the substitution, FeBr₃ catalyst is regenerated.

Without the Lewis acid catalyst, Br₂ doesn't react with benzene at any practical rate — Br₂ is electrophilic, but not electrophilic enough on its own. The catalyst is essential.

Chlorination uses FeCl₃ analogously. Iodination requires more aggressive activating agents (sometimes oxidants like HNO₃) because I₂ is too unreactive on its own. Fluorination is impractical with F₂ directly because the reaction is too violent; fluorinated aromatics are made by other routes.

Aromatic halogenation also occurs in biology. Tyrosine is iodinated to form the precursors of thyroid hormones T3 and T4. The biological iodination is catalyzed by an iodoperoxidase that generates an electrophilic iodine species (I⁺ equivalent) from iodide and hydrogen peroxide.

## Nitration

Benzene + HNO₃ + H₂SO₄ → nitrobenzene + H₂O + (etc.).

The active electrophile is the nitronium ion NO₂⁺, formed when sulfuric acid protonates nitric acid to give a protonated species that loses water:

$$\text{HNO}_3 + \text{H}_2\text{SO}_4 \rightarrow \text{NO}_2^+ + \text{HSO}_4^- + \text{H}_2\text{O}$$

The NO₂⁺ ion attacks the benzene ring (it's a strong enough electrophile to do so without further activation), forming the Wheland intermediate. Loss of H⁺ to bisulfate restores aromaticity, giving nitrobenzene.

Nitration is industrially important because nitrobenzene can be reduced (Sn/HCl, or H₂/Pt, or other reductants) to aniline, which is the parent compound of many dyes and pharmaceuticals. The two-step nitration/reduction sequence is the standard way to introduce an –NH₂ group onto an aromatic ring.

## Sulfonation

Benzene + concentrated H₂SO₄ (or SO₃ in H₂SO₄) → benzenesulfonic acid + H₂O.

The electrophile is SO₃ or HSO₃⁺. The mechanism is standard EAS, with one twist: the reaction is reversible. In hot, dilute aqueous acid, the reverse reaction (desulfonation) dominates. This reversibility is sometimes useful synthetically — you can install a sulfonic acid group as a "blocking group" to direct other electrophiles, then remove it at the end.

Sulfonation is widely used to make detergents (alkylbenzenesulfonates) and dyes. The sulfa drugs (sulfanilamide, sulfamethoxazole, etc., the first effective antibiotics, dating to the 1930s) are aromatic sulfonamides made by aromatic sulfonation followed by amination.

## Friedel-Crafts alkylation

Benzene + R–X + AlCl₃ → R-substituted benzene + HX.

The Lewis acid AlCl₃ extracts the halide from R–X, generating a carbocation R⁺. The carbocation attacks benzene's π system; standard EAS gives the alkylated product.

This reaction has serious limitations:

**Carbocation rearrangements.** Primary alkyl halides give carbocations that rearrange to more stable secondary or tertiary cations. So Friedel-Crafts alkylation with 1-chloropropane gives mostly isopropylbenzene (cumene), not n-propylbenzene. The 1-propyl cation rearranges to the 2-propyl cation before attacking the ring.

**Polyalkylation.** The product (alkylated benzene) is often more reactive than the starting benzene (alkyl groups are activating, see below). So as soon as one alkylation happens, the product is more reactive than benzene and gets alkylated again. The result is usually a mixture of mono- and polyalkylated products, with control hard to achieve.

**No deactivated rings.** Friedel-Crafts alkylation requires a benzene ring that's at least as nucleophilic as benzene itself. Aromatic rings deactivated by EWGs (like nitrobenzene) are too unreactive to undergo F-C alkylation under normal conditions.

These limitations make Friedel-Crafts alkylation a less reliable reaction than other EAS. For making a specific alkylbenzene cleanly, the Friedel-Crafts acylation (below) followed by reduction is often preferred.

## Friedel-Crafts acylation

Benzene + R–C(=O)–Cl + AlCl₃ → R–C(=O)-substituted benzene + HCl.

The Lewis acid AlCl₃ takes the chloride from the acid chloride, generating an *acylium ion* R–C(=O)⁺. This is a stabilized cation (the C=O resonance form delocalizes the positive charge onto oxygen, like an acid chloride iminium ion). The acylium attacks benzene; standard EAS gives the aryl ketone.

Friedel-Crafts acylation has the advantages over alkylation:

**No rearrangement.** The acylium ion doesn't rearrange — it's already as stable as it's going to get. So the regiochemistry is preserved: R–CO–Cl gives R–CO–Ar specifically.

**No polyacylation.** The product is an aryl ketone, which is *deactivated* (the C=O is electron-withdrawing). So further acylation is suppressed. Mono-acylation is the dominant outcome.

The Friedel-Crafts acylation followed by Clemmensen reduction (Zn(Hg) + HCl) or Wolff-Kishner reduction (NH₂NH₂, KOH) reduces the ketone to a CH₂, giving the alkylbenzene that the Friedel-Crafts alkylation would have produced (without rearrangement). This two-step sequence (acylation, then reduction) is the standard way to put a specific straight-chain alkyl group on a benzene ring.

## Substituent effects: activators, deactivators

Once benzene has a substituent, the next electrophilic substitution behaves differently. The substituent affects both:

1. **The rate** of the next substitution. Activators speed it up; deactivators slow it down.
2. **The regiochemistry** of the next substitution. Substituents direct the next E⁺ to specific positions on the ring.

Activators have donating ability — either by resonance (lone pairs on a heteroatom) or by hyperconjugation (alkyl groups). They make the ring more electron-rich and therefore more nucleophilic toward electrophiles. They typically direct the next E⁺ to the *ortho* and *para* positions.

Deactivators have withdrawing ability — typically by resonance (when there's a π bond next to the ring connecting to an electronegative atom). They make the ring less electron-rich. They direct the next E⁺ to the *meta* position.

Halogens are a special case: they're deactivators (by induction — the halogen is electronegative) but ortho-/para-directors (by resonance — the halogen lone pair can stabilize the Wheland intermediate at the ortho and para positions).

The full classification:

**Strong activators (and ortho/para-directors):**
- –NH₂, –NHR, –NR₂ (amines)
- –OH (phenol)
- –OR (ethers)

**Moderate activators (and ortho/para-directors):**
- –NHCOR (anilides)
- –OCOR (esters of phenols)

**Weak activators (and ortho/para-directors):**
- –CH₃, –R (alkyl groups)
- –C₆H₅ (phenyl)

**Weak deactivators (but ortho/para-directors):**
- –F, –Cl, –Br, –I (halogens — special case, see below)

**Moderate deactivators (and meta-directors):**
- –CHO (aldehyde)
- –COR (ketone)
- –COOR (ester)
- –COOH (carboxylic acid)
- –SO₃H (sulfonic acid)

**Strong deactivators (and meta-directors):**
- –NO₂ (nitro)
- –NR₃⁺ (ammonium)
- –CF₃ (trifluoromethyl)

The pattern is clean. Almost every group with a lone pair on the atom directly bonded to the ring is an ortho/para-director (because the lone pair can stabilize the Wheland intermediate at those positions by resonance). Almost every group with a π bond adjacent to the ring (where the next atom is electronegative) is a meta-director (because the resonance structure of the Wheland intermediate would put a + next to a + at ortho/para, which is destabilizing).

The halogens are weak deactivators (their inductive electron withdrawal exceeds their resonance donation) but ortho/para-directors (because the resonance donation does help at those positions, just not enough to overcome the induction-based deactivation).

## Why ortho/para vs. meta? The resonance argument

The Wheland intermediate (after the electrophile attacks) has positive charge on three of the carbons of the ring — the ones not bearing E. Resonance structures distribute this positive charge across these carbons.

For an *ortho* attack: the positive charge in resonance structures sits on positions 1, 3, 5 of the original ring. If the substituent is at position 2 (the original substituent position), then in some resonance structures the positive charge is *adjacent* to the substituent.

For a *para* attack: positive charge sits on positions 2, 4, 6. Substituent at position 1; positive charge adjacent (at position 2).

For a *meta* attack: positive charge sits on positions 1, 3, 5. Substituent at position 2; positive charge *not* adjacent — at least one bond away.

If the substituent is electron-donating (lone pair, alkyl), it stabilizes the positive charge most when adjacent. So ortho and para attacks give lower-energy intermediates, are faster, and dominate.

If the substituent is electron-withdrawing (π-bonded to electronegative atom), it destabilizes the positive charge most when adjacent (the substituent's δ+ piles up next to the ring's positive charge). So ortho and para attacks give higher-energy intermediates, are slower, and meta dominates.

This is the resonance explanation. The Hammond postulate connects intermediate stability to transition-state energy and thus to reaction rate, and the regiochemistry follows.

## Disubstituted benzenes and beyond

When the ring already has two substituents and you're trying to add a third, the directing effects of both substituents come into play.

The general rules:
- If both substituents direct to the same set of positions, the new substituent goes there.
- If the two substituents disagree (one wants ortho/para, the other wants meta), the *more activating* substituent wins (its directing effect dominates the orientation).
- The new substituent often avoids highly hindered positions, regardless of electronic preferences.

Worked example: nitration of *p*-bromotoluene. The methyl group is ortho/para-directing; the bromine is ortho/para-directing too. Methyl directs to positions 2 and 4 (ortho and para to itself). But position 4 is blocked (Br is there). So the products are 2-bromo-4-nitrotoluene (ortho to methyl) and (less, because Br is sterically a moderate substituent) some at the 3-position. The dominant product is 2-bromo-4-nitrotoluene.

## Synthetic strategy: ordering substitutions

The directing effects let you plan multi-step substitutions. To make 4-nitrobromobenzene from benzene:

Strategy A: Brominate first, then nitrate.
- Br₂/FeBr₃ → bromobenzene
- HNO₃/H₂SO₄ → 4-nitrobromobenzene (Br is ortho/para-directing; major product is para)

Strategy B: Nitrate first, then brominate.
- HNO₃/H₂SO₄ → nitrobenzene
- Br₂/FeBr₃ → 3-bromonitrobenzene (NO₂ is meta-directing; major product is meta)

The two orders give different products. To get 4-nitrobromobenzene, use Strategy A.

This kind of ordering is at the heart of multi-step synthesis on aromatic rings. To build a particular substitution pattern, you have to think about which directing groups you want operating at each stage and arrange the order accordingly. Sometimes you install a temporary directing group (like an –SO₃H, which can be removed at the end via hot dilute sulfuric acid) to direct an intermediate substitution, then strip it off.

## Nucleophilic aromatic substitution

Most aromatic chemistry is electrophilic. But there's a less common mechanism, *nucleophilic aromatic substitution* (SNAr), in which a nucleophile replaces a leaving group on the ring.

SNAr only works when:
- There's a strong electron-withdrawing group ortho or para to the leaving group (which stabilizes the negative-charge intermediate).
- The leaving group is reasonable (Cl, F, NO₂, sometimes Br, OTs).

The mechanism is two-step: nucleophile attacks the ring at the carbon bearing the leaving group, forming a *Meisenheimer complex* (an addition intermediate with sp³ carbon and negative charge spread over the ring). Then the leaving group departs, restoring aromaticity.

The activating EWG (e.g., –NO₂) is essential because the Meisenheimer intermediate has substantial negative charge that needs to be stabilized. With one –NO₂ ortho or para to the leaving group, the reaction works. With two –NO₂ groups, much faster. Without strong activation, the reaction doesn't go.

A separate mechanism, the *benzyne mechanism*, operates with very strong bases (NaNH₂) on aryl halides without activating groups. The base deprotonates a C–H ortho to the halide, generating a triple-bond-containing intermediate (benzyne) that is then attacked by a nucleophile. The benzyne mechanism gives a mixture of regiochemical products because the triple bond has two carbons that can be attacked.

These nucleophilic aromatic substitutions are useful in specific cases (especially in pharmaceutical synthesis where activated aryl halides are common substrates) but are nowhere near as broadly useful as the electrophilic substitutions.

↳ **Dig Deeper — Why halogens are the special case**

> Halogens are the only common substituent class that is deactivating but ortho-/para-directing. Walk through the resonance and induction arguments separately. Cover: the inductive electron-withdrawal of halogens (because they're more electronegative than carbon), the resonance donation of halogen lone pairs (which only stabilizes the Wheland intermediate at ortho and para), and how the two effects compete. Explain why for fluorine the resonance effect is largest (despite F being most electronegative), making F the least deactivating of the halogens.

**What to do with the output:** Compare against any organic textbook discussion of "halogen as ortho/para director with deactivation." Verify Claude correctly explains why fluorine is anomalous in being less deactivating than chlorine (the orbital sizes are better matched to carbon for resonance overlap).

## What this chapter does

Aromatic compounds undergo electrophilic substitution rather than addition because aromaticity is preserved by substitution and broken by addition, and the energetic cost of breaking aromaticity is steep. The mechanism is:

1. Electrophile attacks the π system, forming a non-aromatic Wheland intermediate with positive charge.
2. Deprotonation restores aromaticity, giving the substituted benzene product.

The major reactions are halogenation (X₂ + Lewis acid), nitration (HNO₃ + H₂SO₄, generating NO₂⁺), sulfonation (concentrated H₂SO₄ or SO₃), Friedel-Crafts alkylation (R–X + AlCl₃, generating R⁺), and Friedel-Crafts acylation (RCOCl + AlCl₃, generating RCO⁺). Each has its own set of practical considerations — Friedel-Crafts alkylation has rearrangement and polyalkylation problems; sulfonation is reversible; etc.

Substituents on the ring direct subsequent substitutions:
- Activators (electron-donating) direct to ortho/para and speed the next reaction.
- Most deactivators (electron-withdrawing, π-bonded to electronegative atoms) direct to meta and slow the next reaction.
- Halogens are exceptional — deactivators that direct to ortho/para.

Multi-step substitution sequences are planned by considering directing effects in order. Sometimes you install temporary directing groups to control intermediates, then remove them.

The chapter has covered the dominant chemistry of aromatic rings. The next chapter pivots to alcohols and phenols — closely related to aromatic chemistry (phenols are aromatic alcohols) but with their own large body of chemistry that will dominate the next several chapters.

---

*Source for all data, examples, and historical references: OpenStax* Organic Chemistry*, Chapter 16, modules m00188 through m00198.*
---

## LLM Exercise — Chapter 16: Electrophilic Aromatic Substitution (Synthesize a Target Molecule Project)

**Project:** Synthesize a Target Molecule.
**What you're building this chapter:** propose the EAS sequence that installs your target's aromatic substituents.
**Tool:** **Claude Project**.

---

**The Prompt:**

```
Chapter 16 of my Synthesis project. Chapter 16 taught: the EAS
mechanism (electrophile attacks aromatic ring → arenium-ion
intermediate → loss of H to restore aromaticity); five canonical
EAS reactions:
   - Halogenation (X₂, FeX₃ catalyst).
   - Nitration (HNO₃, H₂SO₄).
   - Sulfonation (SO₃, H₂SO₄).
   - Friedel-Crafts alkylation (R-X, AlCl₃).
   - Friedel-Crafts acylation (RCOCl, AlCl₃).
Activating vs. deactivating substituents; ortho/para directors
(electron-donating + halogens, lone-pair donation) vs. meta
directors (electron-withdrawing without lone pairs);
multi-step sequencing for predictable substitution patterns.

Write the brief's "EAS Synthesis Sequence" section in 400–600
words.

1. **Identify the aromatic ring's substitution pattern in target.**
   Note each substituent's position relative to others (ortho,
   meta, para to each).

2. **Design the EAS sequence.** Work backward:
   - Which substituent goes on FIRST? Usually whichever can serve
     as a director for the next substitution.
   - Subsequent substituents go in the position the existing
     substituents direct them to.
   - Activating + deactivating groups in sequence: the activating
     group directs the next addition.

3. **Substituent-by-substituent breakdown.** For each substituent
   in your target's aromatic ring:
   - The EAS reaction used to install it.
   - The reagents and conditions.
   - The position it goes to (predicted from existing directors).

4. **Friedel-Crafts limitations.** Friedel-Crafts fails on
   strongly deactivated rings (already has -NO₂ or -CF₃). The
   sequence must install Friedel-Crafts substituents BEFORE
   strong deactivators.

5. **Multi-step sequencing example.** A specific multi-step
   problem: to make para-nitrobenzaldehyde, you can't acylate
   nitrobenzene (acylation fails on deactivated ring), nor can
   you nitrate benzaldehyde to para position (-CHO is meta-
   director). The trick: acylate benzene first (gives
   acetophenone), then nitrate (-COR is meta-director, so nitro
   goes meta to it = para to where you'd want it from a para-
   substituted benzaldehyde perspective)... or oxidize an
   activator route. Apply similar planning to your target.

6. **Draw the EAS mechanism for ONE step.** Push arrows: ring
   electrons attack electrophile → arenium intermediate →
   proton loss restoring aromaticity.

End with: how many of your target's aromatic-ring functional
groups did you account for, and which ones still need
installation?
```

---

**What this produces:** A 400–600 word EAS sequence section. The order-of-substitution discipline is one of organic chemistry's most testable applications of directing-effect reasoning.

**How to adapt this prompt:**

- *For your own project:* If your target's aromatic ring is heavily substituted, this is the biggest synthesis section. If it's bare or has one simple substituent, this is short.
- *For ChatGPT / Gemini:* Works as written.
- *For Claude Code:* Optional.
- *For a Claude Project:* Append.

**Connection to previous chapters:** Ch 15's aromaticity + Ch 16's EAS form the aromatic-chemistry pair.

**Preview of next chapter:** Chapter 17 covers alcohols and phenols. If your target has hydroxyl groups, you'll propose how each one gets installed (or how a precursor alcohol gets oxidized to the carbonyl that ends up in the target).


---

## AI Wayback Machine

**Charles Friedel** was co-discovered Friedel-Crafts acylation and alkylation in 1877 with James Crafts — still the standard route to aromatic ketones and alkyls.

**Run this:**

```
Who is Charles Friedel, and how does their work connect to electrophilic aromatic substitution we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about their career or ideas.
```

→ Search **"Charles Friedel"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to walk through one of Charles Friedel's key experiments or syntheses in detail.
- Add a constraint: "Answer including criticisms or limits of Charles Friedel's framework."

What changes? What gets better? What gets worse?
