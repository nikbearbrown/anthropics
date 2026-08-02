# Physics: Thermodynamics (Plus One) — Simulation Ideas

**Pilot run: MANIM lane only — D3/DATAVIZ candidates deferred to a second pass.**

*sim-scout run 2026-07-26 — chapters read: 03, 06 and supporting chapters.*

---

## Candidate 01 — Animate "Maxwell-Boltzmann Distribution: The High-Speed Tail That Mars Loses"
- Source: `physics-plus-one-thermodynamics/chapters/03-ideal-gas-kinetic-theory.md`
- Topic: Maxwell-Boltzmann speed distribution
- Lane: MANIM (directed animation)
- Hook: Every molecule in a gas moves at a different speed, and the distribution has a high-velocity tail that never truly reaches zero. Mars has lost most of its atmosphere to that tail — the molecules with enough speed to exceed escape velocity simply left, one by one, over billions of years.
- The rule: f(v) = 4π(m/2πkT)^{3/2} v² e^{-mv²/2kT}. Characteristic speeds: v_mp = √(2kT/m), v_avg = √(8kT/πm), v_rms = √(3kT/m). Escape velocity v_esc = √(2gR) for a planet.
- Concrete numbers: N₂ molecule (m = 4.65×10⁻²⁶ kg), T = 293 K: v_mp = 417 m/s, v_avg = 471 m/s, v_rms = 511 m/s. Mars escape velocity: v_esc = √(2 × 3.72 × 3.39×10⁶) = 5.02 km/s. Mars surface T ≈ 210 K for CO₂ (m = 7.31×10⁻²⁶ kg): v_mp = 309 m/s, v_rms ≈ 377 m/s. Fraction CO₂ exceeding 5 020 m/s: negligibly small but nonzero — this fraction escapes over Gyr timescales.
- The artifact / what moves: The f(v) curve draws for N₂ at T = 293 K. Three vertical dashed lines mark v_mp < v_avg < v_rms, each labeled. A T slider morphs the distribution — lower T shifts peak left, narrowing the curve; higher T broadens the curve and shifts the peak right. A Mars escape velocity line appears at 5 020 m/s; the shaded tail area beyond it is labeled as the "escape fraction." The tail area visibly grows as T rises — intuition: warming Mars accelerates atmosphere loss.
- Output medium: Manim (mp4)
- Two testable predictions: P1: v_rms/v_mp = √3/√2 = √(3/2) ≈ 1.225 — the ratio is fixed regardless of T or m; measurable from the labeled lines at any temperature. P2: v_mp shifts as T^{1/2}: at T = 1 172 K (4× room temperature), v_mp = 2 × 417 = 834 m/s — exactly double, confirming the √T dependence.
- The change: Compare H₂ (m = 3.32×10⁻²⁷ kg) vs N₂ at the same T — H₂ peak is √(28/2) ≈ 3.7× faster. H₂ escape fraction from Earth is dramatically larger, which is why Earth's atmosphere contains almost no free hydrogen.
- Human supplies (Claude can't): Nothing — fully synthetic/analytic.
- Teardown angle: Atmospheric escape is not a sudden event. It is the Maxwell-Boltzmann tail, running continuously for billions of years. Mars had a magnetic field (and thus an atmosphere) once. When the core cooled, the field died, solar wind eroded the upper atmosphere, and the high-speed tail did the rest. The distribution is not an abstraction — it is planetary science.
- Exclusions: Boltzmann equation and transport theory; effusion rate (related but separate); atmospheric height distribution (barometric formula); Jeans escape vs non-thermal escape mechanisms.
- Sim slug: thermo-mb-distribution
- Score: 9/10

---

## Candidate 02 — Animate "Ideal Gas from First Principles: Bouncing Molecule → PV = NkT"
- Source: `physics-plus-one-thermodynamics/chapters/03-ideal-gas-kinetic-theory.md`
- Topic: Kinetic theory of gases / ideal gas law derivation
- Lane: MANIM (directed animation)
- Hook: PV = NkT is not a law discovered in a laboratory — it is derived from a single molecule bouncing inside a box. Multiply by N and you get a law that describes every gas in the universe, from your lungs to a stellar core.
- The rule: One molecule in box of length L: impulse per collision = 2mv_x. Time between collisions: Δt = 2L/v_x. Force on wall: F = 2mv_x / (2L/v_x) = mv_x²/L. Pressure: P = F/A = mv_x²/V. Average over all molecules: P = Nm⟨v_x²⟩/V. Using ⟨v_x²⟩ = ⟨v²⟩/3: PV = Nm⟨v²⟩/3 = NkT when ½m⟨v²⟩ = (3/2)kT.
- Concrete numbers: N₂ molecule, m = 4.65×10⁻²⁶ kg, T = 293 K: ½m⟨v²⟩ = (3/2) × 1.381×10⁻²³ × 293 = 6.07×10⁻²¹ J. ⟨v²⟩ = 2.61×10⁵ m²/s². v_rms = 511 m/s. P at N/V = 2.69×10²⁵ m⁻³ (STP): P = NkT/V = 2.69×10²⁵ × 1.381×10⁻²³ × 293 = 1.01×10⁵ Pa = 1 atm.
- The artifact / what moves: A single molecule bounces between two walls in a 1D box. The collision sequence animates step by step: approach → bounce → recede. Force spike appears at the wall at the moment of collision. Averaging many collisions: the average force bar builds up. Then N molecules added: N-times the force, same box. The equation PV = NkT appears as each step of the derivation completes, building from F → P → PV = Nm⟨v²⟩/3 → PV = NkT. A V slider and T slider verify the proportionality.
- Output medium: Manim (mp4)
- Two testable predictions: P1: At STP (T = 273 K, P = 1 atm = 1.013×10⁵ Pa), V/N = kT/P = 1.381×10⁻²³ × 273 / 1.013×10⁵ = 3.72×10⁻²⁶ m³ per molecule = 22.4 L/mol — matches the molar volume at STP. P2: v_rms = √(3kT/m) = √(3 × 1.381×10⁻²³ × 293 / 4.65×10⁻²⁶) = 511 m/s for N₂ — confirms the speed-temperature link in the ideal gas derivation.
- The change: Apply to the pressure at a stellar core: T ≈ 1.5×10⁷ K, ρ ≈ 1.5×10⁵ kg/m³ (mostly protons, m_p = 1.67×10⁻²⁷ kg). P_core = NkT/V ≈ 2.3×10¹⁶ Pa — compared to Earth's atmosphere (10⁵ Pa), a factor of 2×10¹¹. Same equation, eleven orders of magnitude different.
- Human supplies (Claude can't): Nothing — fully synthetic/analytic.
- Teardown angle: The ideal gas law is a derivation, not a discovery. It follows from Newton's second law applied to one molecule. The constant k_B connects the macroscopic P and T to the microscopic ½m⟨v²⟩ — it is the exchange rate between Joules and Kelvin, nothing more. The "law" is just counting bounces.
- Exclusions: Van der Waals corrections; virial expansion; equipartition theorem beyond translational degrees of freedom; quantum gas (Fermi-Dirac, Bose-Einstein).
- Sim slug: thermo-ideal-gas-derivation
- Score: 9/10

---

## Candidate 03 — Animate "Carnot Cycle: The PV Lens and η_C = 1 − T_C/T_H"
- Source: `physics-plus-one-thermodynamics/chapters/06-second-law-heat-engines.md`
- Topic: Carnot cycle / heat engine efficiency
- Lane: MANIM (directed animation)
- Hook: The Carnot cycle is not a real engine — no real engine achieves it. It is the maximum efficiency any heat engine can reach between two temperatures, and it is astonishingly low. A coal plant at 550°C burning into a 25°C atmosphere achieves at most 63% efficiency. Real plants get about 40%.
- The rule: Carnot cycle: two isothermals + two adiabats on PV diagram. η_C = W_net/Q_H = 1 − T_C/T_H (T in Kelvin). Carnot's theorem: no real engine between T_H and T_C can exceed η_C.
- Concrete numbers: Coal plant: T_H = 823 K (550°C), T_C = 298 K (25°C). η_C = 1 − 298/823 = 0.638 = 63.8%. Real plant ≈ 40%. Nuclear plant: T_H ≈ 600 K, T_C = 298 K. η_C = 1 − 298/600 = 50.3%. Body temperature: T_H = 310 K, T_C = 298 K (ambient). η_C = 1 − 298/310 = 3.9% — your body cannot run an efficient heat engine at 37°C into a 25°C room.
- The artifact / what moves: A PV diagram draws the four Carnot legs sequentially: (1) isothermal expansion at T_H (hyperbola, heat Q_H absorbed), (2) adiabatic expansion to T_C (steeper curve, no heat), (3) isothermal compression at T_C (heat Q_C rejected), (4) adiabatic compression back to start (closes the lens). The enclosed area W_net is shaded and labeled. Below: η_C = 1 − T_C/T_H is computed numerically; a T_H slider sweeps — higher T_H expands the lens and raises η_C. The coal plant, nuclear plant, and human-body points are plotted on an efficiency bar chart.
- Output medium: Manim (mp4)
- Two testable predictions: P1: At T_H = 823 K, T_C = 298 K: η_C = 63.8% — the coal plant maximum, checkable from the formula. P2: As T_H → ∞, η_C → 1 (100%) — the curve asymptotes, visible on the T_H slider sweep; as T_H → T_C, η_C → 0 (no work from equal temperatures).
- The change: Add the Kelvin-Planck statement overlay: any real engine violating η > η_C would imply a perpetual motion machine. Show what a "better than Carnot" engine would mean physically — it could drive the Carnot cycle in reverse (as a refrigerator) and extract net work from a single reservoir.
- Human supplies (Claude can't): Nothing — fully synthetic/analytic.
- Teardown angle: The Carnot limit is not an engineering problem. You cannot beat it by building a better engine. It is a statement about temperature differences, enforced by the second law. The reason fusion power is exciting is partly that T_H → 10⁸ K — a temperature ratio of ~3×10⁵, and an ideal efficiency approaching 100%.
- Exclusions: Entropy derivation from Clausius inequality; Otto cycle or other real engine cycles; refrigerator coefficient of performance; heat pump COP.
- Sim slug: thermo-carnot-cycle
- Score: 9/10

---

## Candidate 04 — Animate "Three Speeds: v_mp, v_avg, v_rms on the Maxwell-Boltzmann Curve"
- Source: `physics-plus-one-thermodynamics/chapters/03-ideal-gas-kinetic-theory.md`
- Topic: Maxwell-Boltzmann characteristic speeds
- Lane: MANIM (directed animation)
- Hook: The Maxwell-Boltzmann distribution has three natural "average" speeds, and they are all different. The most probable speed is where the curve peaks; the mean speed is pulled right by the high-v tail; the rms speed is higher still and is what enters the kinetic energy formula. They differ by exact factors of √(2/π) and √(3/2).
- The rule: v_mp = √(2kT/m). v_avg = √(8kT/πm) = v_mp × √(4/π) ≈ 1.128 v_mp. v_rms = √(3kT/m) = v_mp × √(3/2) ≈ 1.225 v_mp. Temperature dependence: all scale as √T. Mass dependence: all scale as m^{-1/2}.
- Concrete numbers: N₂, T = 293 K: v_mp = 417 m/s, v_avg = 471 m/s, v_rms = 511 m/s. Ratios: v_avg/v_mp = √(4/π) = 1.128; v_rms/v_mp = √(3/2) = 1.225; v_rms/v_avg = √(3π/8) = 1.085. At T = 1 172 K (4×): all speeds double (√4 = 2): v_mp = 834, v_avg = 942, v_rms = 1022 m/s.
- The artifact / what moves: The f(v) Maxwell-Boltzmann curve draws. Three vertical dashed lines appear, one at a time: v_mp (peak of curve, labeled with formula √(2kT/m)), v_avg (centroid, labeled √(8kT/πm)), v_rms (labeled √(3kT/m)). The ordering v_mp < v_avg < v_rms is labeled explicitly. A T slider morphs the curve and all three markers move together, maintaining the exact ratios. A ratio display confirms 1:1.128:1.225 throughout the sweep.
- Output medium: Manim (mp4)
- Two testable predictions: P1: v_rms/v_mp = √(3/2) = 1.2247 exactly — a ratio that holds for any gas at any temperature, verifiable from the labeled markers. P2: At T = 4T₀: all three speeds are exactly 2× their T₀ values — confirming the √T scaling (√4 = 2).
- The change: Compare the same curve for H₂ vs O₂ vs Xe at the same temperature — the peak shifts by √(m_O₂/m_H₂) = √16 = 4×, with all three characteristic speeds scaling accordingly. Same shape (Maxwell-Boltzmann), different horizontal scale.
- Human supplies (Claude can't): Nothing — fully synthetic/analytic.
- Teardown angle: The three speeds represent three different questions: "where does the curve peak?" (v_mp), "what is the mean?" (v_avg), "what goes into ½mv²?" (v_rms). They are all correct answers to different questions about the same distribution. Confusing them is one of the most common errors in kinetic theory.
- Exclusions: Maxwell-Boltzmann derivation from the partition function; anisotropic molecular velocities; speed distribution in 1D vs 3D; equipartition theorem for rotational degrees of freedom.
- Sim slug: thermo-three-speeds
- Score: 8/10

---

## Candidate 05 — Animate "Carnot Efficiency Surface: η vs T_C/T_H with Real Engine Benchmarks"
- Source: `physics-plus-one-thermodynamics/chapters/06-second-law-heat-engines.md`
- Topic: Carnot efficiency / real engine comparison
- Lane: MANIM (directed animation)
- Hook: The Carnot efficiency depends only on the temperature ratio T_C/T_H — not on the working fluid, the piston design, or the fuel. A single curve from 0 to 1 on the ratio axis contains the efficiency ceiling for every heat engine ever built or imagined.
- The rule: η_C = 1 − T_C/T_H = 1 − r, where r = T_C/T_H ∈ (0, 1). η_C → 0 as r → 1 (equal temperatures); η_C → 1 as r → 0 (T_C → 0 K).
- Concrete numbers: Steam (coal) plant: T_H = 823 K, T_C = 298 K, r = 0.362, η_C = 63.8%, real ≈ 40%. Natural gas combined cycle: T_H ≈ 1100 K (combustion), T_C = 310 K, r = 0.282, η_C = 71.8%, real ≈ 60%. Nuclear (PWR): T_H = 600 K, T_C = 310 K, r = 0.517, η_C = 48.3%, real ≈ 33%. Car engine (Otto): T_H ≈ 800 K, T_C = 310 K, r = 0.388, η_C = 61.3%, real ≈ 25%.
- The artifact / what moves: A single curve η_C = 1 − r draws from r = 0 (η = 1) to r = 1 (η = 0). Real engine data points appear one by one: each is plotted at its (r, η_actual) position below the Carnot curve, with a vertical "gap" to the ceiling labeled as "irreversibility loss." A region below the ceiling is shaded "achievable"; above it is labeled "forbidden by the second law." The T_H and T_C sliders move r on the axis.
- Output medium: Manim (mp4)
- Two testable predictions: P1: η_C = 0 at r = 1 (T_C = T_H) — identical temperatures produce no net work; confirmed by the curve touching zero at r = 1. P2: η_C = 0.5 at r = 0.5 (T_H = 2T_C) — exactly 50% Carnot efficiency when the hot reservoir is twice the cold temperature in Kelvin, not Celsius.
- The change: Add a combined-cycle efficiency argument: if exhaust at T_intermediate is fed into a second cycle with T_C at ambient, the combined η = 1 − (T_C/T_H) — same formula, higher effective T_H. Show that cascading cycles approach Carnot but never exceed it.
- Human supplies (Claude can't): Nothing — fully synthetic/analytic.
- Teardown angle: Every real engine falls below the Carnot curve. The gap between the data point and the ceiling is irreversibility — friction, heat leaks, finite-time processes. The second law does not forbid building a 63% efficient steam plant; it forbids building a 64% one.
- Exclusions: Entropy production calculation; exergy analysis; endoreversible engine (Curzon-Ahlborn efficiency); refrigerator COP ceiling.
- Sim slug: thermo-carnot-efficiency-surface
- Score: 8/10

---

## Candidate 06 — Animate "f(v) Temperature Morphing: Cold N₂ vs Hot H₂ vs Slow Xe"
- Source: `physics-plus-one-thermodynamics/chapters/03-ideal-gas-kinetic-theory.md`
- Topic: Maxwell-Boltzmann / mass and temperature dependence
- Lane: MANIM (directed animation)
- Hook: Room-temperature hydrogen molecules move as fast as nitrogen at 1 960°C. The Maxwell-Boltzmann distribution carries both pieces of information — temperature and mass — in a single curve, and you can read them off from the peak position alone.
- The rule: f(v) = 4π(m/2πkT)^{3/2} v² e^{-mv²/2kT}. Peak at v_mp = √(2kT/m). The curve scales: same shape, shifted by √(T/m). Two gases at same T: ratio of peaks = √(m₂/m₁). One gas at two temperatures: ratio of peaks = √(T₂/T₁).
- Concrete numbers: T = 293 K: H₂ (m = 3.32×10⁻²⁷ kg): v_mp = 1574 m/s. N₂ (m = 4.65×10⁻²⁶ kg): v_mp = 417 m/s. Xe (m = 2.18×10⁻²⁵ kg): v_mp = 193 m/s. Ratio H₂/N₂: √(28/2) = √14 = 3.74. Ratio N₂/Xe: √(131/28) = √4.68 = 2.16. N₂ at T = 1 960°C = 2 233 K: v_mp = 417 × √(2233/293) = 417 × 2.76 = 1 151 m/s — matching H₂ at room temperature to within 37%.
- The artifact / what moves: Three Maxwell-Boltzmann curves draw simultaneously: H₂ (light, fast, broad), N₂ (medium), Xe (heavy, slow, narrow). All at T = 293 K. Peak positions labeled. Then a T animation: N₂ curve heats up — the peak slides rightward as T rises. At T ≈ 1960°C = 2233 K, the N₂ peak aligns with the H₂ room-temperature peak. The overlap moment is labeled. An m slider replaces the preset gases with a continuous mass sweep.
- Output medium: Manim (mp4)
- Two testable predictions: P1: v_mp(H₂)/v_mp(N₂) = √(m_N₂/m_H₂) = √(28/2) = √14 = 3.742 at same T — directly readable from the peak positions in the animation. P2: N₂ at T = 2 233 K has v_mp = 417 × √(2233/293) = 1 149 m/s ≈ H₂ at 293 K (1 574 m/s) — not exact (ratio ~1.37) but close, showing that mass and temperature enter symmetrically through the ratio T/m.
- The change: Show the escape-velocity implication for each gas: mark Earth escape velocity (11.2 km/s) on the x-axis — all three gas peaks are far below it, but the H₂ tail extends meaningfully farther toward it, explaining why Earth has almost no free hydrogen but retains nitrogen and xenon.
- Human supplies (Claude can't): Nothing — fully synthetic/analytic.
- Teardown angle: Every atmospheric chemist reads Maxwell-Boltzmann distributions. The Moon has essentially no atmosphere because its escape velocity is only 2.4 km/s — N₂'s room-temperature v_mp (417 m/s) is much lower, but the tail extends to 2.4 km/s easily over geological time. The curve is not just physics; it is planetary history.
- Exclusions: Real gas corrections (van der Waals); Fermi-Dirac and Bose-Einstein distributions for quantum gases; effusion through a small hole (Knudsen flow); viscosity derivation from kinetic theory.
- Sim slug: thermo-mb-mass-temperature
- Score: 8/10

---

| # | Title | Lane | Score | Slug |
|---|---|---|---|---|
| 01 | Maxwell-Boltzmann: Mars Escape Tail | MANIM | 9 | thermo-mb-distribution |
| 02 | Ideal Gas Derivation: Bouncing Molecule → PV = NkT | MANIM | 9 | thermo-ideal-gas-derivation |
| 03 | Carnot Cycle: PV Lens + η_C = 1 − T_C/T_H | MANIM | 9 | thermo-carnot-cycle |
| 04 | Three Speeds: v_mp, v_avg, v_rms | MANIM | 8 | thermo-three-speeds |
| 05 | Carnot Efficiency Surface vs Real Engines | MANIM | 8 | thermo-carnot-efficiency-surface |
| 06 | f(v) Mass/Temperature Morphing: H₂, N₂, Xe | MANIM | 8 | thermo-mb-mass-temperature |

*6 candidates. MANIM: 6. D3/DATAVIZ: 0 (deferred). Score ≥8: 6.*
