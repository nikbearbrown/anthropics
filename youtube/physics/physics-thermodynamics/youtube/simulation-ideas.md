# Physics: Thermodynamics — Simulation Ideas

**Pilot run: MANIM lane only. D3/DATAVIZ pass follows after human approval.**
*sim-scout run 2026-07-26 — chapters 03, 04, 05, 06, 07, 08 read.*

---

## Candidate 01 — Animate "Maxwell-Boltzmann Speed Distribution: Curve Draw + Species Morph"
- Source: `physics-thermodynamics/chapters/03-ideal-gas-kinetic-theory.md`
- Topic: Maxwell-Boltzmann Distribution
- Lane: MANIM (directed animation)
- Hook: The Boltzmann tail is why Mars lost its hydrogen — but a static plot hides it. Watch the curve draw, three speed markers land in sequence, then the tail slide past Mars escape velocity as temperature rises.
- The rule: f(v) = 4π(m/2πk_BT)^(3/2) v² e^(−mv²/2k_BT); three characteristic speeds — v_mp = √(2k_BT/m), v_avg = √(8k_BT/πm), v_rms = √(3k_BT/m) — always in that order; escape fraction = ∫_{v_esc}^∞ f(v) dv
- Concrete numbers: O₂ at 300 K: v_mp=395, v_avg=446, v_rms=484 m/s; H₂ at 200 K: v_rms≈1580 m/s; Mars escape velocity = 5.0 km/s; H₂ escape fraction at 200 K ≈ 10⁻³
- The artifact / what moves: f(v) area-under-curve draws from left to right for O₂ at 300 K; three colored vertical markers drop in sequence (v_mp, then v_avg, then v_rms); curve then morphs as T sweeps 100→2000 K, peak visibly sliding right and broadening; final scene overlays H₂ vs N₂ at 200 K, shading the area above Mars escape velocity — H₂ tail is a visible sliver, N₂ tail is machine-zero
- Output medium: Manim (mp4)
- Two testable predictions: P1: ratio v_mp : v_avg : v_rms = 1 : √(4/π) : √(3/2) ≈ 1 : 1.128 : 1.225 — checkable for O₂ at 300 K (395:446:484, exact); P2: H₂ escape fraction above 5.0 km/s at 200 K ≈ 10⁻³ (confirming Mars atmosphere loss) vs N₂ ≈ 10⁻¹⁰⁰ (effectively zero)
- The change: Shift to Earth escape (11.2 km/s) — see H₂ fraction plummet to ~10⁻⁵⁰, explaining why Earth retains hydrogen on geological timescales even though Mars lost it
- Human supplies (Claude can't): Nothing — fully synthetic/analytic; all parameters from physics constants and tabulated molecular masses
- Teardown angle: Planetary atmospheres are sorted by molecular weight and temperature, not total pressure — the tail decides planetary history, and the tail is not in the average
- Exclusions: Derivation of the distribution from the Boltzmann distribution (Ch 9 territory); effusion and diffusion rate applications; van der Waals corrections; Maxwell's original derivation
- Sim slug: thermo-maxwell-boltzmann
- Score: 9/10

---

## Candidate 02 — Animate "Otto Cycle: Four-Leg Sequential Draw with Enclosed-Area Work"
- Source: `physics-thermodynamics/chapters/05-pv-diagrams-processes.md`
- Topic: Otto Cycle / Heat Engine Thermodynamics
- Lane: MANIM (directed animation)
- Hook: Four separate strokes, each a different curve shape on the PV diagram — watch them chain into a closed loop and see that the enclosed area IS the work extracted from each combustion cycle. Then sweep the compression ratio and watch efficiency climb.
- The rule: Leg 1→2: adiabatic compression PV^γ=const; leg 2→3: isochoric heat addition (vertical); leg 3→4: adiabatic expansion; leg 4→1: isochoric heat rejection. η_Otto = 1 − 1/r^(γ−1). Adiabatic constraint: T₂ = T₁ r^(γ−1)
- Concrete numbers: γ=1.4 (air), r=10, T₁=300 K → T₂=300×10^0.4≈754 K; η=1−10^(−0.4)≈60.2%; for comparison, real gasoline engines: 25–35%
- The artifact / what moves: PV axes draw. Each leg appears in sequence with a label: "adiabatic compression" (steep curve up-left), "isochoric heat spike" (vertical jump), "power stroke" (steep curve down-right), "exhaust valve" (vertical drop). Loop closes and interior fills gold — "net work = enclosed area." Efficiency readout: 60.2%. Then r sweeps 5→15: enclosed area grows, efficiency bar rises, following η = 1 − 1/r^(γ−1)
- Output medium: Manim (mp4)
- Two testable predictions: P1: η_Otto = 1 − r^(−(γ−1)) → at r=10, γ=1.4: η=60.2% (exact, verifiable analytically); P2: T₂/T₁ = r^(γ−1) = 10^0.4 ≈ 2.51, so T₂ ≈ 754 K — checkable from the adiabatic constraint TV^(γ−1)=const
- The change: Set γ=5/3 (monatomic hypothetical engine) vs 7/5 (diatomic air) at the same r — monatomic engine is more efficient because more energy per degree of freedom goes to pressure; shows how molecular structure sets the efficiency ceiling
- Human supplies (Claude can't): Nothing — fully synthetic/analytic
- Teardown angle: Real engines hit 25–35% against a theoretical 60.2% ceiling — not because engineers are bad, but because the Otto cycle assumes ideal gas, instant combustion, and zero heat loss; every deviation from those ideals erases the gap
- Exclusions: Diesel cycle comparison (related but a different card); deriving η_Otto algebraically as a Manim scene (belongs in narration script, not as animation beats); engine friction / pumping losses
- Sim slug: thermo-otto-cycle
- Score: 9/10

---

## Candidate 03 — Animate "Carnot Cycle: PV Lens and TS Rectangle Evolving Simultaneously"
- Source: `physics-thermodynamics/chapters/06-second-law-heat-engines.md`
- Topic: Carnot Efficiency / Second Law
- Lane: MANIM (directed animation)
- Hook: The Carnot cycle looks like a lens on PV, but on the TS diagram it collapses to a perfect rectangle — and both enclosed areas equal the same net work. Two representations, one truth, zero entropy generated. Watch both spaces draw in sync, then slide T_C upward and see the lens and rectangle shrink to nothing together.
- The rule: PV diagram: two isothermal hyperbolas (PV=nRT_H, PV=nRT_C) connected by two isentropic adiabats (ΔS=0). TS diagram: rectangle with vertices at (S_min, T_C), (S_max, T_C), (S_max, T_H), (S_min, T_H). η_C = 1 − T_C/T_H. W_net = (S_max−S_min)×(T_H−T_C) = Q_H − Q_C
- Concrete numbers: T_H=600 K, T_C=300 K → η_C=50%; Q_H=1000 J → W=500 J, Q_C=500 J; ΔS_hot = −Q_H/T_H = −1.667 J/K; ΔS_cold = +Q_C/T_C = +1.667 J/K; net ΔS_universe = 0 (reversible)
- The artifact / what moves: Split screen (PV left, TS right). Each leg draws in matching color on both diagrams simultaneously: isothermal at T_H draws a hyperbola on PV while a horizontal line extends on TS; adiabat draws a steeper curve on PV while a vertical line draws on TS. Loop closes. Interior fills on both panels — same numerical area (500 J). Then T_C slider rises toward T_H: lens squashes to a line on PV, rectangle squashes to a line on TS, efficiency bar drops to 0. Final scene: T_C = T_H, empty loops, η = 0, labeled "no temperature difference = no work"
- Output medium: Manim (mp4)
- Two testable predictions: P1: PV enclosed area = TS rectangle area = W_net = Q_H×η_C = 500 J (dual-diagram consistency, exact and checkable); P2: ΔS_universe = 0 for the Carnot cycle — ΔS_hot + ΔS_cold = −1000/600 + 500/300 = 0 (exact, verifiable numerically)
- The change: Run the cycle counterclockwise — same two diagrams, same shapes, but TS rectangle traversed right-to-left: now a Carnot refrigerator with COP_Carnot = T_C/(T_H−T_C) = 300/300 = 1.0; the same animation teaches two devices
- Human supplies (Claude can't): Nothing — fully synthetic/analytic
- Teardown angle: Every real engine's TS trace is a messy blob, not a clean rectangle — the Carnot rectangle is the tightest possible path between two temperatures; the blob's extra area is entropy generated and work permanently lost
- Exclusions: Proof that no engine can exceed Carnot (belongs in narration, not animation beats); Clausius inequality derivation; OTEC / geothermal cycle comparisons (save for script exploration)
- Sim slug: thermo-carnot-pv-ts
- Score: 9/10

---

## Candidate 04 — Animate "Adiabat Peeling Away From Isotherm: The Work Gap"
- Source: `physics-thermodynamics/chapters/05-pv-diagrams-processes.md`
- Topic: Adiabatic vs. Isothermal Processes / PV Diagram
- Lane: MANIM (directed animation)
- Hook: They look like the same hyperbola — but the adiabat is always steeper, and the gap between them is precisely the heat the isothermal expansion borrowed from outside to do more work. Watch the curves diverge and the gap fill.
- The rule: Isotherm: PV = nRT → slope = −P/V. Adiabat: PV^γ = const → slope = −γP/V. At any point, adiabat slope / isotherm slope = γ. W_iso = nRT ln(V_f/V_i); W_ad = (P_iV_i − P_fV_f)/(γ−1). Work gap = W_iso − W_ad
- Concrete numbers: P_i=3 atm=3.04×10⁵ Pa, V_i=2 L=2×10⁻³ m³, V_f=6 L, γ=1.4. P_f,ad = P_i×(V_i/V_f)^γ = 3.04×10⁵×(1/3)^1.4 ≈ 6.35×10⁴ Pa. W_ad = 567 J; W_iso = nRT_i ln(3) = (P_iV_i)ln(3) = 608×1.099 = 668 J. Gap = 101 J
- The artifact / what moves: Single state point appears at (V_i=2L, P_i=3 atm). Two curves simultaneously sweep rightward from that point: isothermal hyperbola in blue (labeled "absorbs heat from reservoir"), adiabatic hyperbola in orange (labeled "no heat in, cools as it expands"). The orange curve drops faster and diverges below the blue. At V_f=6L the gap between the two end-pressures highlights. The region between the two curves fills with a shaded band labeled "extra 101 J — the heat the isotherm borrowed." Numeric W values annotate each curve's area.
- Output medium: Manim (mp4)
- Two testable predictions: P1: At the starting point (P=3×10⁵ Pa, V=2×10⁻³ m³), adiabat slope / isotherm slope = γ = 1.4 exactly — checkable from the ratio of final pressures P_f,iso / P_f,ad = (P_i×V_i/V_f) / (P_i×(V_i/V_f)^γ) = (1/3)^1 / (1/3)^1.4 = (1/3)^(−0.4) = 3^0.4 ≈ 1.40; P2: W_iso − W_ad = 668 − 567 = 101 J equals the area between the two curves (checkable by numerical integration of PdV for each path)
- The change: Vary γ from 5/3 (monatomic He) to 7/5 (diatomic air) — adiabat steepness changes; monatomic adiabat diverges most from isotherm, meaning the work gap is largest, meaning heat engines using monatomic gases are most sensitive to the cooling effect of adiabatic expansion
- Human supplies (Claude can't): Nothing — fully synthetic/analytic
- Teardown angle: The isotherm wins on work not through clever engineering but by cheating — it maintains temperature by borrowing heat from a reservoir; the adiabat is the thermodynamically self-contained process, and self-containment costs work
- Exclusions: Full Otto or Carnot cycle (separate cards); deriving PV^γ=const from the first law (Ch 4 challenge — belongs in narration)
- Sim slug: thermo-adiabat-vs-isotherm
- Score: 8/10

---

## Candidate 05 — Animate "Diesel Adiabatic Compression: No Spark, Just Thermodynamics"
- Source: `physics-thermodynamics/chapters/04-first-law.md`
- Topic: Adiabatic Compression / First Law Applications
- Lane: MANIM (directed animation)
- Hook: A diesel engine has no spark plug. It ignites by compression alone — air squeezed to 1/20 its volume heats from 300 K to nearly 900 K. Watch the cylinder shrink and the temperature counter climb past diesel ignition point, driven only by TV^(γ−1)=const.
- The rule: Adiabatic process: Q=0, ΔU=−W. For ideal gas: TV^(γ−1)=const → T₂ = T₁(V₁/V₂)^(γ−1) = T₁×r^(γ−1). W_on_gas = nC_V(T₂−T₁). No heat flows — all work becomes internal energy, which means temperature.
- Concrete numbers: T₁=300 K, V₁=1.0 L, r=20 (diesel compression ratio), γ=1.4 (diatomic air). T₂ = 300×20^0.4 = 300×2.93 ≈ 879 K. Diesel ignition temperature ≈ 540°C = 813 K. For n=0.04 mol: W ≈ n×(5/2 R)×(T₂−T₁) = 0.04×20.8×579 ≈ 482 J
- The artifact / what moves: Animated cylinder cross-section with a descending piston. Gas fills interior; color gradient shifts blue→yellow→orange→red as T climbs. Numeric temperature counter ticks upward from 300 K. A horizontal dashed line at 813 K (diesel ignition) appears; the counter crosses it with a labeled event: "ignition point reached." Piston reaches minimum volume; final state annotated: T=879 K, V=0.05 L, Q=0, W=482 J stored as internal energy. Side panel: TV^0.4=const verified numerically at start and end.
- Output medium: Manim (mp4)
- Two testable predictions: P1: T₂/T₁ = r^(γ−1) = 20^0.4 ≈ 2.93, so T₂ ≈ 879 K — checkable from TV^(γ−1)=const (T₁×V₁^0.4 = 879×(V₁/20)^0.4, both sides = 300×V₁^0.4); P2: Compare r=10 (gasoline): T₂=300×10^0.4≈754 K, which is below diesel ignition temperature — explains why gasoline engines can't use r=20 (knocking) while diesel can
- The change: Contrast with isothermal compression at T=300 K — same volume ratio, but isothermal requires heat to be continuously dumped, and the final temperature would be only 300 K; diesel temperature rise comes entirely from being adiabatic, not from combustion
- Human supplies (Claude can't): Nothing — fully synthetic/analytic; diesel ignition temperature is a tabulated property (~540°C), used as a reference line only
- Teardown angle: The diesel engine is the first law made visible — every joule of work you put in through the piston becomes internal energy with nowhere to go (no heat exchange), so the temperature has no choice but to climb; thermodynamics does the ignition
- Exclusions: Full diesel PV cycle (isobaric heat addition leg — that's the Diesel cycle variant card); combustion chemistry; real-gas corrections near ignition; Otto cycle comparison (Candidate 02)
- Sim slug: thermo-diesel-adiabatic
- Score: 8/10

---

## Candidate 06 — Animate "Fermi-Dirac Step Function: T=0 Cliff Softening Into Thermal Blur"
- Source: `physics-thermodynamics/chapters/08-statistical-mechanics.md`
- Topic: Fermi-Dirac Distribution / Quantum Statistics
- Lane: MANIM (directed animation)
- Hook: At absolute zero the Fermi sea is a perfect cliff — every state below E_F filled, every state above empty. Raise the temperature and watch the cliff blur into a sigmoid. The blur width is exactly k_BT. For copper at 300 K, that blur is 0.7% of the Fermi energy — which is why metals have shockingly low electronic heat capacity, a fact that stumped pre-quantum physicists.
- The rule: f_FD(E) = 1/(e^((E−μ)/k_BT) + 1). At T=0: step function at E_F. f(E_F) = 1/2 exactly at all T > 0. Thermal smearing width ≈ 2k_BT centered on E_F. Electronic C_V ∝ (k_BT/E_F) × classical C_V
- Concrete numbers: Copper: E_F=7.0 eV, k_BT=0.025 eV at 300 K. Blur = 2k_BT = 0.05 eV = 0.71% of E_F. Electronic C_V ≈ (π²/3)(k_BT/E_F) × (3/2)Nk_B ≈ 0.009 × equipartition value. Classical (Boltzmann) prediction: C_V = 3/2 Nk_B (wrong by factor ~100)
- The artifact / what moves: Energy axis vertical (0 to 2E_F). f(E) axis horizontal (0 to 1). At T→0: perfect step at E_F (0 below, 1 above — inverted; filled states up to E_F). A temperature dial sweeps from 0 K upward. Step smooths into sigmoid symmetrically around E_F; a labeled brace tracks the blur width "= 2k_BT." At T=300 K for copper: brace is narrow (0.7% of range). At T=10,000 K: significant melting of step. Side panel: "classical prediction (wrong)" dashed line vs. actual electronic C_V(T), showing classical over-prediction at 300 K by factor ~100
- Output medium: Manim (mp4)
- Two testable predictions: P1: f(E_F) = 1/2 exactly at any temperature T > 0 — exact from the formula (symmetry point, independent of T); P2: At T=300 K for copper, the fraction of electrons within k_BT of E_F ≈ k_BT/E_F ≈ 0.0036, i.e., ~0.36% — electronic C_V ≈ 0.36% of classical prediction (matching the ~1% experimental value within the rough estimate)
- The change: Compare f_FD to f_Boltzmann = e^(−(E−E_F)/k_BT) on the same axes — Boltzmann gives an exponentially growing occupation above E_F (physically impossible for electrons), demonstrating why Pauli exclusion changes everything for dense fermion systems
- Human supplies (Claude can't): Nothing — fully synthetic/analytic; E_F for copper (7.0 eV) is a tabulated spectroscopic/experimental value used as a parameter
- Teardown angle: The Pauli exclusion principle is thermodynamic armor — it locks 99.3% of conduction electrons into states they can't leave, which is what makes metals stable conductors instead of quantum plasmas; the "frozen Fermi sea" is a thermodynamic consequence, not a special assumption
- Exclusions: Chemical potential vs. temperature dependence (μ shifts slightly with T — second-order correction, belongs in script); Bose-Einstein condensation (bosons, different sign); full band structure of real metals
- Sim slug: thermo-fermi-dirac-morph
- Score: 8/10

---

## Candidate 07 — Animate "Schottky Anomaly: Heat Capacity Peak From Two-Level Statistics"
- Source: `physics-thermodynamics/chapters/08-statistical-mechanics.md`
- Topic: Partition Function / Boltzmann Statistics
- Lane: MANIM (directed animation)
- Hook: A two-state system (spin-up / spin-down in a magnetic field) has zero heat capacity at T=0, zero heat capacity at T=∞ — but a sharp peak in between. Classical physics has no mechanism for a peak. Watch the two populations equalize as T rises, and watch the C_V(T) curve rise and fall in lockstep with how fast they're changing.
- The rule: E₀=0, E₁=ε. Z = 1 + e^(−ε/k_BT). P₁ = e^(−ε/k_BT)/(1+e^(−ε/k_BT)). ⟨E⟩ = ε×P₁. C_V = d⟨E⟩/dT = k_B(ε/k_BT)² × e^(ε/k_BT)/(e^(ε/k_BT)+1)². Peak at k_BT ≈ 0.417ε
- Concrete numbers: ε=0.02 eV (typical paramagnetic salt in B-field). Peak at T = 0.02/(0.417×8.617×10⁻⁵) ≈ 556 K. At T=100 K: P₁ ≈ 9.8%. At T=556 K: P₁ ≈ 37%, changing fastest. At T=10,000 K: P₁ ≈ 49%, approaching saturation
- The artifact / what moves: Split screen. Left: energy-level diagram with two horizontal lines (ground and excited states); bars at each level show population fractions P₀ and P₁ as T sweeps upward (ground bar shrinks, excited bar grows). Right: C_V(T)/k_B curve draws simultaneously — rises from 0, peaks at T_Schottky, falls back to 0. A vertical cursor links the two panels: when the cursor is in the steep-population-change zone, the C_V curve is at its peak. Final annotation: "real data: paramagnetic salts in magnetic fields match this curve quantitatively."
- Output medium: Manim (mp4)
- Two testable predictions: P1: C_V peaks at k_BT ≈ 0.417ε — derivable by setting d²⟨E⟩/dT²=0 analytically; for ε=0.02 eV, peak at T≈556 K (exact and confirmed in paramagnetic materials); P2: at T→∞, C_V→0 because P₁→1/2 (both levels equally occupied, population stops changing — rate of change of ⟨E⟩ with T goes to zero)
- The change: Add a third energy level (E₂=2ε) — Schottky peak broadens and shifts to higher T; or split the upper level into two degenerate states (degeneracy g=2) — peak shifts location; shows how real spin systems with complex level structure are tuned by field strength
- Human supplies (Claude can't): Nothing — fully synthetic/analytic; ε parameter is illustrative, not from a specific lab measurement
- Teardown angle: The Schottky peak is the Goldilocks signature of quantum statistics: too cold → upper level inaccessible, zero capacity; too hot → both levels saturated, zero capacity; only in between does temperature drive meaningful population change, and that's where the system can actually absorb heat
- Exclusions: Deriving C_V from the partition function in algebra steps on screen (belongs in narration); Debye T³ phonon contribution (a different system); magnetic-field dependence of the splitting ε
- Sim slug: thermo-schottky-anomaly
- Score: 8/10

---

## Candidate 08 — Animate "Boltzmann Microstate Counting: Why the Second Law Is Just Statistics"
- Source: `physics-thermodynamics/chapters/07-entropy.md`
- Topic: Entropy / Second Law Statistical Foundation
- Lane: MANIM (directed animation)
- Hook: For N=4 molecules you'll see all four on one side every 16 draws. For N=100 you'd wait longer than the age of the universe. Watch the probability distribution of macrostates sharpen from "noticeably spread" to "effectively a spike" as N grows — this is why the second law isn't a prohibition, it's overwhelming statistics.
- The rule: N molecules distributed in two halves of a box. Ω(n) = C(N,n) = N!/(n!(N−n)!). S = k_B ln Ω. P(all on left) = 1/2^N. Distribution narrows relative to N: standard deviation ∝ √N, relative width ∝ 1/√N
- Concrete numbers: N=4: P(all left)=1/16=6.25%. N=20: max Ω=C(20,10)=184756; P(all left)=1/2^20≈10⁻⁶; S_max/k_B=ln(184756)≈12.13. N=100: Ω(50)/Ω(100)=C(100,50)/1≈10²⁹. N=N_A: ratio ~ e^(N_A ln2) — beyond any notation
- The artifact / what moves: Horizontal axis: n (particles on left, 0 to N). Vertical axis: Ω(n)/Ω_max (normalized). N=4: all seven macrostates visible as bars, the n=0 and n=4 bars clearly non-zero. N increases in labeled steps — 4→10→20→50→100→500: distribution narrows. Relative bar heights at n=0 and n=N shrink toward zero. At N=100: n=100 bar is invisible, labeled "10²⁹× less likely than n=50." Final panel: S = k_B ln Ω(n_peak) vs S = k_B ln Ω(n=N) — gap grows exponentially with N. Punchline text: "N=4: wait 16 draws. N=100: wait 10²⁹ draws. N=10²³: wait longer than the universe."
- Output medium: Manim (mp4)
- Two testable predictions: P1: For N=20, Ω_max = C(20,10) = 184,756 exactly; S_max/k_B = ln(184756) ≈ 12.13 — checkable with a calculator; P2: Relative distribution width ∝ 1/√N — at N=100, FWHM/N ≈ 10%; at N=400, FWHM/N ≈ 5% — ratio = 2 = √(400/100), an exact prediction of binomial statistics
- The change: Show that at N=20 fluctuations are macroscopically visible — the system regularly visits n=14 or n=6; at N=1000 those fluctuations are below 1 molecule per 33 in relative terms; asks "at what N does the second law become practically unbreakable?" (answer: well before N=100)
- Human supplies (Claude can't): Nothing — fully synthetic/analytic; all Ω values computed from binomial coefficients
- Teardown angle: The second law isn't fundamental — it's a counting argument that just happens to be so overwhelming at macroscopic scale that it looks like a law of nature; at N=20, it's already a coin flip you can mostly trust; at N=10²³, it's a fact as reliable as arithmetic
- Exclusions: Time evolution / Loschmidt echo (interactive D3 territory); Clausius entropy dS=δQ/T (separate card or narration); entropy of mixing Gibbs paradox (different setup, Ch 7 synthesis exercise)
- Sim slug: thermo-boltzmann-microstate-N
- Score: 8/10

---

## Candidate 09 — Animate "C_V/R Quantum Stepladder for Diatomic Gas"
- Source: `physics-thermodynamics/chapters/03-ideal-gas-kinetic-theory.md` (Fig 3.5 and equipartition section)
- Topic: Equipartition / Quantum Degrees of Freedom
- Lane: MANIM (directed animation)
- Hook: Classical physics predicts C_V = 7/2 R for a diatomic gas — constant at all temperatures. Reality disagrees in a way that destroyed classical physics: the heat capacity steps up twice, at specific quantum threshold temperatures, with a molecular diagram activating at each step. Boltzmann's theory was embarrassed. Einstein's was not.
- The rule: f (active degrees of freedom): 3 at T < Θ_rot (translation only); 5 at Θ_rot < T < Θ_vib (add rotation); 7 at T > Θ_vib (add vibration). C_V = (f/2)R. Quantum activation temperatures: Θ_rot = ℏ²/(2Ik_B), Θ_vib = ℏω/k_B
- Concrete numbers: H₂: Θ_rot ≈ 85 K (from I=4.7×10⁻⁴⁸ kg·m²), Θ_vib ≈ 6000 K. N₂: Θ_rot ≈ 2.9 K (rotation active at room temp), Θ_vib ≈ 3350 K. Classical prediction at all T: C_V/R = 3.5 (wrong below 85 K and above 3000 K for H₂)
- The artifact / what moves: Log-scale temperature axis (10 K to 10,000 K). Two curves drawn: dashed horizontal at 3.5 (classical prediction, labeled "classical physics: wrong"); solid curve (experimental shape) draws left to right — plateau at 3/2, rise, plateau at 5/2, rise, approaches 7/2. At each step, a molecular diagram appears in a callout: first "translational motion only" (three bouncing arrows), then "rotation activates" (two spin arrows added), then "vibration activates" (spring motion added). Vertical dashed lines mark Θ_rot and Θ_vib for H₂. Second run overlays N₂ — shows Θ_rot so low (~2.9 K) that N₂ is already in the 5/2 plateau at room temperature.
- Output medium: Manim (mp4)
- Two testable predictions: P1: At 300 K, C_V for N₂ = 5/2 R = 20.8 J/(mol·K) — confirmed experimentally to ~1%; P2: Θ_rot for H₂ = ℏ²/(2Ik_B) with I=4.7×10⁻⁴⁸ kg·m² gives Θ_rot = (1.055×10⁻³⁴)²/(2×4.7×10⁻⁴⁸×1.38×10⁻²³) ≈ 85.4 K — matches the observed onset of the first step exactly
- The change: Show HD (hydrogen deuteride, asymmetric, different moment of inertia I) — step locations shift, demonstrating that Θ_rot is set by molecular geometry and can be tuned by isotopic substitution; connects quantum mechanics to measurable thermodynamics
- Human supplies (Claude can't): Nothing — fully synthetic/analytic; the step curve shape is derived from quantum mechanics and verified against historical H₂ heat capacity data (the shape is analytic, not from a specific modern dataset)
- Teardown angle: The steps in C_V are what broke classical physics — Boltzmann's equipartition gives a flat line, and flat lines don't describe reality below ~200 K; Einstein realized the modes have to be turned on by quantum thresholds, which is why he published his 1907 solid heat capacity paper before most people believed in quanta
- Exclusions: Full Einstein/Debye solid model (solids, different system); anharmonic corrections at very high T; derivation of the quantum harmonic oscillator partition function (Ch 8 challenge exercise)
- Sim slug: thermo-cv-quantum-steps
- Score: 8/10

---

## Summary — pilot scan (physics-thermodynamics, MANIM lane)

| Candidate | Title | Manim move | Score |
|---|---|---|---|
| 01 | Maxwell-Boltzmann Speed Distribution | Curve draw + parametric morph (T, m) | 9/10 |
| 02 | Otto Cycle Four-Leg Sequential | Sequential curve draw + enclosed area fill | 9/10 |
| 03 | Carnot PV + TS Dual Diagram | Split-screen simultaneous lens/rectangle | 9/10 |
| 04 | Adiabat vs. Isotherm Divergence | Two curves from one point, gap-fill | 8/10 |
| 05 | Diesel Adiabatic Compression | Cylinder animation + temperature counter | 8/10 |
| 06 | Fermi-Dirac Step → Sigmoid Morph | Step-function softening with T sweep | 8/10 |
| 07 | Schottky Anomaly C_V Peak | Dual-panel: population bars + C_V curve | 8/10 |
| 08 | Boltzmann Microstate N Scaling | Distribution bar chart sharpening with N | 8/10 |
| 09 | C_V/R Quantum Stepladder (Diatomic) | Step curve draw + molecular diagram callouts | 8/10 |

**Build-soon (9/10):** Candidates 01, 02, 03.
**Build after tightening (8/10):** Candidates 04–09.
**D3/DATAVIZ pass (not yet scouted):** Microstate random-walk simulator (Ch 7 LLM exercise), interactive Boltzmann distribution explorer (Ch 8 LLM exercise), PV diagram click-and-drag process builder (Ch 5 LLM exercise), first-law energy-balance sliders (Ch 4 LLM exercise). These are emergent/interactive and belong in the D3 lane — ready to scout on approval.
