# Organic Chemistry — Simulation Ideas

*Generated 2026-07-26 · MANIM lane only · Score ≥ 6 · D3 cards excluded · Reaction mechanism arrows explicitly excluded per brief*

---

## Candidate 01 — Newman Projection Rotation: Torsional Strain Curve Drawing

- Source: `organic-chemistry/chapters/03-organic-compounds-alkanes-and-their-stereochemistry.md`
- Topic: Conformational analysis; torsional strain; Newman projections
- Lane: MANIM (directed animation)
- Hook: The energy landscape of butane as a C-C bond rotates has three minima and three maxima — but the two anti minima are NOT equivalent to the two gauche minima, and students consistently misread Newman projections as static snapshots rather than frames of a continuous rotation.
- The rule: V(φ) = Σ Vn/2 × (1 − cos(nφ)); for butane (CH₃CH₂CH₂CH₃), the dominant torsional potential along the C2–C3 bond is: V(φ) = (V₁/2)(1 − cos φ) + (V₂/2)(1 − cos 2φ) + (V₃/2)(1 − cos 3φ); the gauche-anti energy difference ≈ 3.8 kJ/mol; eclipsed-staggered barriers: H/H eclipsing ≈ 4.0 kJ/mol, CH₃/H eclipsing ≈ 6.0 kJ/mol, CH₃/CH₃ eclipsing ≈ 11.0 kJ/mol.
- Concrete numbers: φ = 0° (eclipsed, CH₃ // CH₃): max, E ≈ 19 kJ/mol above anti; φ = 60° (gauche): local min, E = 3.8 kJ/mol above anti; φ = 120° (eclipsed, CH₃ // H): local max, E ≈ 16 kJ/mol above anti; φ = 180° (anti): global min, E = 0; φ = 240° (eclipsed, CH₃ // H): local max again ≈ 16 kJ/mol; φ = 300° (gauche): local min 3.8 kJ/mol; φ = 360° = 0° cycle closes. Three maxima, three minima. The two gauche wells are equal to each other (and to 3.8 kJ/mol) but the anti well is lower.
- The artifact / what moves: Left panel: Newman projection of the C2–C3 bond — the front CH₃ rotates continuously while the rear CH₃ is fixed; the dihedral angle label φ counts from 0° to 360°; substituent labels (H or CH₃) update as they pass through front positions. Right panel: A potential energy curve V(φ) draws simultaneously as the Newman projection rotates; a live dot rides the curve, pausing at maxima (eclipsed) and minima (staggered) with labeled energy values in kJ/mol; the anti minimum (φ = 180°) is visually deeper than the gauche minima (φ = 60°, 300°).
- Output medium: Manim (mp4)
- Two testable predictions: P1: At φ = 0° (both methyls eclipsed, plus 2 pairs H/H eclipsing), total strain = 2×4.0 + 11.0 = 19.0 kJ/mol above anti — the global maximum in the rotation scan. P2: The Boltzmann ratio of anti:gauche at 298 K = e^(ΔE/RT) = e^(3800/8.314×298) = e^1.53 ≈ 4.6:1; so butane spends ~82% of its time in anti conformations (anti + mirror-anti counted together vs. the two gauche wells).
- The change: Substitute one of the terminal CH₃ groups with a *tert*-butyl group — the gauche energy penalty rises from 3.8 to ~20 kJ/mol (A-value for *tert*-butyl); the gauche minima nearly disappear from the energy landscape; the rotation curve is now dominated by the anti minimum, and the molecule is effectively locked in anti.
- Human supplies (Claude can't): Nothing — fully synthetic/analytic; all strain values from published spectroscopic and computational studies.
- Teardown angle: Room-temperature molecules are not frozen in their most stable conformation — they sample all of them. The question is which conformations they spend the most *time* in, and the Boltzmann distribution answers that from the energy curve alone.
- Exclusions: Reaction mechanism steps (explicitly excluded), cyclohexane ring flip (separate animation below), transition states for reactions.
- Sim slug: newman-butane-torsional-strain
- Score: 9/10

---

## Candidate 02 — Cyclohexane Ring Flip: Axial to Equatorial Population Shift

- Source: `organic-chemistry/chapters/04-organic-compounds-cycloalkanes-and-their-stereochemistry.md`
- Topic: Cyclohexane conformational analysis; 1,3-diaxial interactions; A-values
- Lane: MANIM (directed animation)
- Hook: Adding a single methyl group to cyclohexane shifts the ring-flip equilibrium to 95:5 — but the counterintuitive part is that the "disfavored" chair isn't rare because it's unstable in isolation, it's rare because it has *two simultaneous gauche interactions* that stack additively.
- The rule: ΔG = −RT ln(K_eq); for methylcyclohexane, ΔG = 7.6 kJ/mol (2 × 3.8 kJ/mol per 1,3-diaxial contact); K_eq = e^(7600/8.314×298) = e^3.07 ≈ 21.5; equatorial:axial = 21.5:1 ≈ 95.4%:4.6%.
- Concrete numbers: Methylcyclohexane, T = 298 K; equatorial-methyl chair has 0 axial-methyl contacts (no 1,3-diaxial strain from methyl); axial-methyl chair has 2 gauche-equivalent methyl↔axial-H contacts at C3 and C5, each costing 3.8 kJ/mol; total ΔG = 7.6 kJ/mol; K = 21.5; population 95.4% equatorial, 4.6% axial. Tert-butyl: A-value > 20 kJ/mol; K > 3000; equatorial fraction > 99.97%.
- The artifact / what moves: A 3D chair-conformation Manim scene shows methylcyclohexane flipping between two chairs; the methyl group switches from equatorial (pointing outward, relaxed) to axial (pointing straight up, close to two axial H's at C3/C5); the 1,3-diaxial H···CH₃ distances appear as dashed red lines when axial; a population meter in the corner shows the 95/5 split with a live fraction counter; as a substituent A-value slider increases from 0.5 (F) through 7.6 (CH₃) to >20 (tBu), the population bar shifts progressively more to equatorial.
- Output medium: Manim (mp4)
- Two testable predictions: P1: At A = 7.6 kJ/mol (methyl), K_eq = e^(7600/2478) = e^3.07 = 21.5; equatorial fraction = 21.5/22.5 = 95.6% — confirmed by NMR integration ratios in the literature. P2: For 1,3-dimethylcyclohexane (cis), each chair has one axial methyl; ΔG between chairs = 0 kJ/mol (symmetric); 50:50 mixture — both chairs are equally populated. For trans-1,3-dimethylcyclohexane, the diequatorial chair (both methyls equatorial) is preferred by 2 × 7.6 = 15.2 kJ/mol; K = e^6.14 ≈ 465; the diaxial chair is essentially absent.
- The change: Cool the animation to T = 200 K — the Boltzmann factor increases (K_eq rises for the same ΔG), making the equatorial preference even stronger; the population bar shifts toward 99%; warm to T = 600 K and watch the two chairs approach 50:50 as entropy dominates.
- Human supplies (Claude can't): Nothing — all A-values are from experimental NMR equilibrium measurements, tabulated in textbook; the 3D geometry is fully analytic.
- Teardown angle: The ring flip happens millions of times per second at room temperature. Every "locked" cyclohexane in a drug molecule is locked not by magic but by a large A-value group making the flip energetically costly — and the pharmaceutical chemist's job is knowing which group to install to achieve that lock.
- Exclusions: Reaction mechanisms using E2 anti-periplanar requirement (mechanism arrows excluded); full steroid ring-fusion geometry (separate analysis).
- Sim slug: cyclohexane-ring-flip-axial-equatorial
- Score: 9/10

---

## Candidate 03 — Hückel's Rule: π Electron Count Sweeping n = 0 to n = 3

- Source: `organic-chemistry/chapters/15-benzene-and-aromaticity.md`
- Topic: Aromaticity; Hückel's rule; MO energy levels
- Lane: MANIM (directed animation)
- Hook: Hückel's rule says 4n+2 electrons = aromatic, but the *reason* is the MO filling pattern — at 4n+2, all bonding MOs are exactly filled; at 4n, two electrons are forced into degenerate non-bonding orbitals with no stabilization. Cyclobutadiene (4 π electrons, n=1) is so destabilized it dimerizes at room temperature, while benzene (6 π electrons, n=1 in 4n+2) is one of the most stable molecules known.
- The rule: For a planar cyclic conjugated ring with N atoms, MO energies are ε_k = α + 2β cos(2πk/N) for k = 0, 1, ..., N−1; the 4n+2 pattern fills all negative-energy (bonding) MOs with no electrons left over; 4n leaves 2 electrons in the degenerate k = ±N/4 level with zero bonding character (these are either zero-energy or antibonding depending on sign of β).
- Concrete numbers: Cyclobutadiene (N=4): MO energies at k=0,1,2,3: α+2β, α, α, α−2β; 4 electrons fill: k=0 (2e), k=1 and k=2 degenerate (1e each by Hund's rule) — two unpaired electrons in non-bonding orbitals; zero net stabilization energy from the degenerate MOs; molecule is a diradical, violently reactive. Benzene (N=6): MO energies at k=0,1,2,3,4,5: α+2β, α+β, α+β, α−β, α−β, α−2β; 6 electrons fill k=0 (2e) + k=1,2 (2e each, degenerate pairs) — all three bonding MOs exactly full; aromatic stabilization = 2(2β) + 4(β) = 8β relative to 3 localized double bonds (6β); resonance energy ≈ 2β ≈ 150 kJ/mol.
- The artifact / what moves: An energy-level diagram animates for ring sizes N = 3, 4, 5, 6, 7, 8; at each N, the MO rungs appear on the left; then electrons fill from the bottom up (Aufbau) as red balls dropping in; for 4n+2 systems, all balls pair up neatly in bonding orbitals; for 4n systems, the last two electrons sit lonely in degenerate non-bonding rungs (shown with Hund's rule splitting); a "stability score" bar at the right grows for aromatic cases and shrinks (turns red) for anti-aromatic cases; a counter shows π electron count and flashes "AROMATIC" or "ANTI-AROMATIC" or "NON-AROMATIC".
- Output medium: Manim (mp4)
- Two testable predictions: P1: Benzene's experimental heat of hydrogenation is 206 kJ/mol vs. the theoretical 354 kJ/mol for three isolated double bonds — the 148 kJ/mol gap is the aromatic stabilization energy; the MO model predicts stabilization ≈ 2β where β ≈ −75 kJ/mol, giving ≈ 150 kJ/mol ✓. P2: Cyclopentadienyl anion (C₅H₅⁻) has 6 π electrons (n=1, aromatic); its conjugate acid cyclopentadiene has pKa ≈ 16 (vs. ≈44 for a typical alkene C–H bond) — a difference of 28 pKa units corresponding to ΔΔG ≈ 160 kJ/mol, nearly all of it aromatic stabilization of the anion.
- The change: Add a nitrogen into the ring to make pyridine (N replaces one CH) — show that pyridine's N contributes 1 electron to the π system (its lone pair is in the plane, not the π system), so 6 π electrons is maintained; aromatic ✓. Then switch to pyrrole (5-membered ring, N's lone pair enters the π system, contributing 2 electrons to give 6 total) — still 6 π electrons, still aromatic but with the lone pair in the ring now committed to aromaticity, making it a poor base.
- Human supplies (Claude can't): Nothing — the Hückel MO energies and experimental heats of hydrogenation are textbook analytic values.
- Teardown angle: The 4n+2 rule is not numerology — it is the consequence of filling a circular MO energy ladder. The circles that happen to have a non-degenerate lowest level (Hückel's ladder for any N not divisible by 4) are the ones that achieve perfect Aufbau filling with 2, 6, 10, 14, ... electrons.
- Exclusions: Reaction mechanisms for aromatic substitution (explicitly excluded), specific drug molecules containing aromatic rings (qualitative).
- Sim slug: huckel-rule-mo-energy-filling
- Score: 9/10

---

## Candidate 04 — Reaction Coordinate Diagram: Activation Energy and Arrhenius Rate

- Source: `organic-chemistry/chapters/06-an-overview-of-organic-reactions.md`
- Topic: Transition state theory; activation energy; rate constant
- Lane: MANIM (directed animation)
- Hook: The Arrhenius equation says every 10 kJ/mol increase in activation energy slows the reaction by a factor of 57 at room temperature — so the difference between a reaction that works in 10 seconds and one that takes 100 years is about 50 kJ/mol of activation energy, a gap that a single methyl group can create or destroy.
- The rule: k = A × e^(−Ea/RT); at T = 298 K, RT = 2.478 kJ/mol; for ΔEa = 5.7 kJ/mol, rate changes by e^(5700/2478) = e^2.30 ≈ 10×; for ΔEa = 50 kJ/mol, rate changes by e^(50000/2478) = e^20.2 ≈ 6×10⁸×; ΔG° = −RT ln K_eq; a ΔG° of −11.4 kJ/mol gives K = 100.
- Concrete numbers: Two-step reaction with intermediates; Step 1: ΔG‡₁ = 80 kJ/mol; Step 2: ΔG‡₂ = 40 kJ/mol (from the intermediate); intermediate at −20 kJ/mol relative to reactants; products at −50 kJ/mol; rate of Step 1 (rate-determining) ∝ e^(−80/2.478) = e^(−32.3) ≈ 10^(−14) relative to A; rate of Step 2 ∝ e^(−40/2.478) = e^(−16.2) ≈ 10^(−7) relative to A — Step 1 is 10^7 times slower; it is the rate-determining step.
- The artifact / what moves: A reaction coordinate diagram draws from left to right — reactants at 0 kJ, curve rises to TS1 peak (+80 kJ), falls to intermediate (−20 kJ), rises to TS2 peak (+20 kJ from intermediate = 0 kJ absolute), falls to products (−50 kJ); a red "reaction ball" travels along the curve with its speed proportional to the local downhill slope; at the two TS peaks it slows dramatically; a live rate-constant label on each step shows the relative rate; TS1 is labeled "rate-determining step" with an arrow; a second sub-panel shows the same diagram after a catalyst is added — TS1 drops from 80 to 60 kJ, the ball now speeds through step 1 noticeably faster.
- Output medium: Manim (mp4)
- Two testable predictions: P1: Lowering Ea from 80 to 60 kJ/mol (catalyst) speeds up step 1 by e^(20000/2478) = e^8.07 ≈ 3,200× — the overall reaction accelerates by the same factor since step 1 is rate-determining; step 2 is unchanged. P2: The equilibrium constant for the overall reaction K = e^(50000/2478) = e^20.2 ≈ 6×10⁸ — the reaction is thermodynamically very favorable regardless of the kinetic barrier; adding catalyst does not change K, only how fast equilibrium is reached.
- The change: Make the reaction endothermic (products at +30 kJ instead of −50 kJ) — the reaction coordinate hill now ends higher than it started; K = e^(−30000/2478) = e^(−12.1) ≈ 5×10^(−6) (mostly reactants); but Ea from the reactant side is still 80 kJ/mol; the Hammond postulate now applies: the TS must resemble the products (endothermic, late TS) — label this shift visually.
- Human supplies (Claude can't): Nothing — fully synthetic/analytic; the energy values are hypothetical illustrative numbers consistent with real organic reaction scales.
- Teardown angle: Thermodynamics (ΔG°) says whether a reaction *can* happen. Kinetics (ΔG‡) says whether it *will* happen on a human timescale. Diamond is thermodynamically unstable with respect to graphite — it just needs 20 billion years to equilibrate. Activation energy is the reason diamonds exist.
- Exclusions: Specific reaction mechanisms (SN1, SN2, E2 arrows — explicitly excluded), photochemical excitation (different energy landscape), solvent effects.
- Sim slug: reaction-coordinate-activation-energy-arrhenius
- Score: 8/10

---

## Candidate 05 — Beer-Lambert Law: Absorbance vs. Concentration Drawing

- Source: `organic-chemistry/chapters/14-conjugated-compounds-and-ultraviolet-spectroscopy.md`
- Topic: UV-vis spectroscopy; Beer-Lambert law; quantitative absorbance
- Lane: MANIM (directed animation)
- Hook: Chemists use Beer-Lambert (A = εcl) as a routine analytical tool, but the law is counterintuitive in one direction: absorbance is *linear* in concentration, but transmittance is *exponential* — so doubling the concentration does NOT halve the transmitted light; it squares the fraction transmitted.
- The rule: A = ε × c × l; A = −log₁₀(T); T = 10^(−A) = 10^(−εcl); at A = 1, T = 10% (90% absorbed); at A = 2, T = 1% (99% absorbed); at A = 3, T = 0.1%; each unit of absorbance removes 90% of the remaining light.
- Concrete numbers: β-carotene in ethanol: λ_max = 466 nm; ε = 1.40 × 10⁵ L·mol⁻¹·cm⁻¹; l = 1.00 cm; at c = 1.0 × 10⁻⁵ M: A = 1.40×10⁵ × 1.0×10⁻⁵ × 1.0 = 1.40; T = 10^(−1.40) = 4.0% transmission; at c = 5.0 × 10⁻⁶ M: A = 0.70; T = 20%; at c = 2.0 × 10⁻⁵ M: A = 2.80; T = 0.16% — nearly opaque.
- The artifact / what moves: Left panel: a cuvette diagram with an incident beam entering (full width/brightness) and emerging at reduced width; as a concentration slider increases from 0 to 3.0 × 10⁻⁵ M, the transmitted beam shrinks (exponential in c, not linear); a live A readout and T% readout update in the corner. Right panel: simultaneously draws two curves — A vs. c (a straight line through the origin, slope = εl) and T vs. c (an exponential decay curve dropping steeply); the dot on each curve tracks the slider position; at c where A = 1, a vertical marker highlights and labels "90% absorbed."
- Output medium: Manim (mp4)
- Two testable predictions: P1: At A = 2 (c = 1.43 × 10⁻⁵ M for β-carotene with l=1cm), T = 1% — only 1 photon in 100 passes through; confirmed by T = 10^(−2) = 0.01. P2: Doubling the path length from 1 cm to 2 cm doubles A (from 1.40 to 2.80) but reduces T from 4.0% to 0.0016% — an 25-fold decrease in transmitted light, not a 2-fold decrease, because A and T are related by a logarithm.
- The change: Switch chromophore from β-carotene (ε = 140,000) to an isolated ketone n→π* transition (ε = 15) — at the same concentration, A drops by a factor of 9,333; the ketone at 1.0×10⁻⁵ M is nearly transparent (A = 0.00015); illustrating that ε is the molecular-scale absorptivity — a property of the chromophore, not the solution.
- Human supplies (Claude can't): Nothing — ε for β-carotene is a published, verified spectroscopic constant; the Beer-Lambert relationship is analytic.
- Teardown angle: Spectroscopy is one of the few analytical techniques where you can measure the concentration of an absorbing compound without destroying the sample, without separating it, and in real time — if you know ε and l, a single absorbance reading gives you c in seconds.
- Exclusions: NMR spectroscopy (different principle), infrared spectroscopy (different selection rules), fluorescence (emission rather than absorption).
- Sim slug: beer-lambert-absorbance-vs-concentration
- Score: 7/10

---

## Candidate 06 — sp3/sp2/sp Hybridization: Bond Angle Geometry Constructing

- Source: `organic-chemistry/chapters/01-structure-and-bonding.md`
- Topic: Hybridization; molecular geometry; VSEPR
- Lane: MANIM (directed animation)
- Hook: Carbon's three hybridizations are usually presented as three separate facts to memorize — but they are one fact: as more p orbitals mix in, the geometry contracts from 180° to 120° to 109.5°, and the bond-length shortens by a predictable amount. The progression is a single continuous story, not three disconnected cases.
- The rule: sp: 2 hybrid orbitals at 180°, bond length to H ≈ 106 pm (acetylene C–H); sp²: 3 hybrid orbitals at 120°, bond length ≈ 110 pm (ethylene C–H); sp³: 4 hybrid orbitals at 109.5°, bond length ≈ 109 pm (methane C–H); C–C bond lengths: triple bond 120 pm (two π bonds), double bond 134 pm (one π bond), single bond 153 pm (no π bond). Each π bond reduces bond length by ≈13–17 pm relative to the σ-only case.
- Concrete numbers: Methane: 4 sp³ hybrid orbitals, H–C–H = 109.5°, C–H bond = 109 pm, C–C single bond = 153 pm. Ethylene: 3 sp² hybrid orbitals, H–C–H = 117.4°, H–C–C = 121.3°, C=C = 134 pm, C–H = 110 pm. Acetylene: 2 sp hybrid orbitals, H–C–C = 180° (linear), C≡C = 120 pm, C–H = 106 pm.
- The artifact / what moves: A central carbon atom draws; then sp³ hybridization assembles — four equal orbitals pop into place one by one at 109.5° tetrahedral angles; H atoms attach; bond-angle arcs appear with the 109.5° labels; bond-length ruler labels appear. Then the scene transitions: one orbital "merges back" into the p manifold — three sp² orbitals rearrange to 120° trigonal planar; the remaining unhybridized p orbital appears perpendicular as a blue lobe; the second C joins and the π bond forms as blue side-by-side lobes; bond-length ruler shortens from 153 to 134 pm. Then transition again to sp: only 2 sp hybrids, 180° linear; two blue p lobes on each C; the triple bond forms; ruler shortens to 120 pm.
- Output medium: Manim (mp4)
- Two testable predictions: P1: H–C–C angle in ethylene = 121.3° (measured by microwave spectroscopy), not 120°, because the two C–H bonds are slightly pushed apart by the larger C=C π system — the deviation from ideal is 1.3°, consistent with the VSEPR refinement. P2: The C–H bond in acetylene (106 pm) is shorter than in methane (109 pm) despite acetylene C being bonded to fewer atoms — because sp C has more s-character (50%) than sp³ C (25%), pulling H closer to the nucleus. Each 1% increase in s-character shortens the bond by ≈0.2 pm; sp vs. sp³ is 25% more s-character → ≈5 pm shorter ✓.
- The change: Replace one H in methane with Cl (more electronegative) — show that the H–C–Cl angle compresses slightly from 109.5° (Cl's bonding pair is pulled closer to Cl, taking less angular "room" around carbon than H does); VSEPR predicts H–C–Cl angle ≈ 108°; the animation shows the orbital contraction.
- Human supplies (Claude can't): Nothing — all bond lengths and angles are from published microwave and X-ray crystallography data.
- Teardown angle: Why does organic chemistry have only three hybridizations? Because carbon has one s and three p orbitals in its valence shell — you can mix 1, 2, or 3 p's with the s, giving exactly three hybrid types. There are no others. The geometry follows from the count.
- Exclusions: MO theory energy diagrams for these molecules (separate animation), reaction mechanisms that depend on hybridization.
- Sim slug: hybridization-sp3-sp2-sp-geometry
- Score: 8/10
