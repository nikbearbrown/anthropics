# Physics Plus One: Thermodynamics — CLI Video Ideas ("X with Claude")

---

## Card 1 — Maxwell-Boltzmann Speed Distribution Simulator

**Source:** Ch 3 (Ideal Gas and Kinetic Theory) — Maxwell-Boltzmann distribution, rms speed, most-probable speed, atmospheric escape tail

**Lane:** BUILD

**Hook:** "Mars lost its hydrogen atmosphere because of a tail. Not a comet tail — the tail of a probability distribution. Build it."

**The artifact:** Animated d3 visualization of the Maxwell-Boltzmann speed distribution f(v) = 4π n (m/2πkT)^(3/2) v² exp(−mv²/2kT) for any gas species and temperature. Three vertical markers: most-probable speed v_p = √(2kT/m), mean speed ⟨v⟩ = √(8kT/πm), and rms speed v_rms = √(3kT/m). Sliders for temperature (100–10000 K) and gas species (H₂, He, N₂, O₂, CO₂, Ar). The escape-velocity for Earth (11.2 km/s) and Mars (5.0 km/s) are shown as vertical dashed lines. The tail fraction P(v > v_escape) is integrated numerically and displayed as a percentage. Animation: sweep T from 200 K to 2000 K and watch the fraction escaping change by orders of magnitude.

**Prompt seed:** `claude "Build d3 v7 single-HTML Maxwell-Boltzmann speed distribution visualizer. f(v) = 4π·n·(m/2πkT)^(3/2)·v²·exp(−mv²/(2kT)) where n=1 (normalized). Gas species dropdown: H₂ (m=3.32e-27), He (m=6.64e-27), N₂ (m=4.65e-26), O₂ (m=5.32e-26), CO₂ (m=7.31e-26). Temperature slider 100–10000 K. Mark v_p=√(2kT/m), ⟨v⟩=√(8kT/πm), v_rms=√(3kT/m) with colored vertical lines. Show escape velocity dashed lines for Earth (11200 m/s) and Mars (5000 m/s). Compute tail fraction P(v>v_esc) numerically with 1000-point integration. Plot area under tail shaded red. Animate T sweep with Play button. SVG only."`

**Read/check:** Set T=300 K, N₂. Verify v_rms = √(3·1.38e-23·300/4.65e-26) ≈ 517 m/s. Check v_p < ⟨v⟩ < v_rms (always true for MB distribution). Set H₂ at T=273 K and Mars escape velocity; verify tail fraction is small but nonzero (~10⁻⁸ or so). Verify normalization: integral of f(v)dv ≈ 1.

**Human supplies:** Nothing — fully synthetic.

**Output medium:** d3 animated HTML (single file, SVG, CDN).

**The change:** Switch from N₂ to H₂ and watch the distribution shift dramatically leftward on the speed axis (mass ratio 14:1 means H₂ is √14 ≈ 3.7× faster at same T). The escape tail fraction for H₂ from Mars is ~10⁶× larger than for N₂ — at the same temperature. This explains why hydrogen and helium are absent from Mars's atmosphere while CO₂ (heavier) remains.

**Teardown angle:** "The Maxwell-Boltzmann distribution uses v_rms for temperature, but v_rms is √(⟨v²⟩), not ⟨v⟩. These are different by a factor of √(8/3π) ≈ 0.92. The rms is what appears in PV = NkT (from the pressure derivation); the mean is what appears in effusion rates. Mixing them up gives wrong answers in atmospheric escape calculations."

**Exclusions:** 2D Maxwell-Boltzmann (different formula). Quantum statistics corrections (relevant only at very low T). Molecular velocity vs speed distinction.

**Score:** 9/10

---

## Card 2 — PV Diagram: Four Thermodynamic Processes Animated

**Source:** Ch 5 (PV Diagrams and Processes) — isothermal, isochoric, isobaric, adiabatic processes, work as area under curve

**Lane:** BUILD

**Hook:** "The area under the PV curve IS the work. Not a metaphor — the definition. Build the simulator that makes every process a race to see who encloses the most area."

**The artifact:** Animated d3 PV diagram. Axes: P (vertical, 0–5 atm) and V (horizontal, 0–5 L). User selects starting state (P₀, V₀, T₀ = P₀V₀/nR with n=1 mol). Four process buttons: Isothermal (PV = const, hyperbola), Isochoric (vertical line), Isobaric (horizontal line), Adiabatic (PV^γ = const, steeper hyperbola with γ = 5/3 for monatomic or 7/5 for diatomic). For each process, a path animates and the area under the curve fills in with color — that area equals the work done. Numerical readout: W (work), Q (heat), ΔU (internal energy change). A cycle builder: string up to 4 processes into a closed loop; the enclosed area = net work per cycle; efficiency for heat engine cycles computed.

**Prompt seed:** `claude "Build d3 v7 single-HTML PV diagram animator for thermodynamic processes. n=1 mol ideal gas, R=8.314 J/(mol·K). Initial state sliders: P₀ (0.5–5 atm), V₀ (0.5–5 L). Four process buttons: Isothermal (PV=P₀V₀, draw hyperbola), Isochoric (P changes, V=V₀, vertical line), Isobaric (V changes, P=P₀, horizontal line), Adiabatic (PV^γ = P₀V₀^γ, γ adjustable 5/3 or 7/5). End-point sliders for each process. Animate path drawing with filled area (work). Show W=∫PdV numerically (trapezoid, 500 points), Q=ΔU+W, ΔU=nCvΔT. Cycle mode: string processes, show enclosed area as net work, efficiency η=W_net/Q_in. SVG only."`

**Read/check:** Start at P=2 atm, V=2 L, T=585 K. Run isothermal expansion to V=4 L. Verify W = nRT·ln(V₂/V₁) = 1·8.314·585·ln(2) ≈ 3370 J. Run adiabatic from same start to V=4 L. Verify W = (P₁V₁−P₂V₂)/(γ−1). Verify that adiabatic curve is steeper than isothermal (adiabat slope = −γP/V vs. −P/V for isotherm).

**Human supplies:** Nothing — fully synthetic.

**Output medium:** d3 animated HTML (single file, SVG, CDN).

**The change:** Build a Carnot cycle: isothermal expansion at T_H → adiabatic expansion → isothermal compression at T_C → adiabatic compression. The enclosed area is the net work. Efficiency η = W_net/Q_H. Verify numerically that η = 1 − T_C/T_H. Then deform the cycle into a triangle (non-Carnot) and verify efficiency drops.

**Teardown angle:** "The fact that adiabat and isotherm have different slopes — γP/V vs. P/V — is not a formula to memorize. It has a physical origin: during adiabatic compression, the temperature rises (no heat reservoir to absorb the work), so the pressure rises faster than if temperature stayed constant. The γ is the ratio of heat capacities Cp/Cv, and it is always ≥ 1."

**Exclusions:** Real gas (van der Waals). Phase transitions on PV diagram (liquid-vapor coexistence). 3D PVT surface.

**Score:** 9/10

---

## Card 3 — Carnot Engine Efficiency and Second Law Visualizer

**Source:** Ch 6 (Second Law and Heat Engines) — Carnot efficiency η = 1 − T_C/T_H, Kelvin-Planck statement, comparison of real engines to Carnot bound

**Lane:** BUILD

**Hook:** "The maximum efficiency of any heat engine depends only on two temperatures. Every engine ever built — no exceptions — is bounded by one formula. Build the proof."

**The artifact:** Animated d3 visualization showing a heat engine "box" with T_H reservoir on top, T_C reservoir on bottom, and work output on the side. User adjusts T_H (300–2000 K) and T_C (200–600 K) with sliders. Real-time display of η_Carnot = 1 − T_C/T_H. Second panel: bar chart of efficiency comparison — Carnot, real steam (Rankine, ~38%), jet engine (Brayton, ~45%), car engine (Otto, ~25%), combined cycle (60%). Third chart: η_Carnot as a 2D heat map over (T_H, T_C) space. Animation: given input heat Q_H (slider), animate the energy flow — Q_C dumped to cold reservoir and W = Q_H − Q_C = η·Q_H as work output.

**Prompt seed:** `claude "Build d3 v7 single-HTML Carnot efficiency visualizer. Sliders: T_H (500–2000 K), T_C (200–500 K, constrained < T_H). Display η_Carnot = 1−T_C/T_H as large readout. Animated energy flow diagram: rectangle labeled 'Engine' with arrow from T_H reservoir (top, red) showing Q_H flowing in, arrow to T_C reservoir (bottom, blue) showing Q_C = (1−η)Q_H flowing out, arrow to right showing W = η·Q_H. Animate flow with particle dots along arrows. Bar chart comparing η_Carnot to real engines: Otto=0.25, Rankine=0.38, Brayton=0.45, combined_cycle=0.60, labeled with actual T_H,T_C. 2D heat map: color = η_Carnot over T_H=400–2000K vs T_C=200–600K grid. SVG only."`

**Read/check:** Set T_H = 600 K, T_C = 300 K. Verify η_Carnot = 1 − 300/600 = 0.500 = 50%. Set T_H = 1000 K, T_C = 300 K. Verify η = 0.700. Note that doubling T_H is not twice as efficient — the relationship is linear in the temperature ratio. Verify Q_C = Q_H(1−η) in the energy flow animation.

**Human supplies:** Nothing — fully synthetic.

**Output medium:** d3 animated HTML (single file, SVG, CDN).

**The change:** Observe the 2D heat map: η approaches 1 only as T_C → 0 or T_H → ∞. The combined cycle power plant at 60% achieves this by exhausting gas at ~900 K into a steam cycle that extracts additional work — effectively raising T_H and lowering the effective T_C. Still bounded by Carnot. Then pose the question: why not just make T_C = 0? Because cooling the cold reservoir costs work (refrigerator), and the net benefit vanishes.

**Teardown angle:** "Carnot's result is remarkable: it says nothing about the working fluid, the engine geometry, or the mechanism. It says only that two temperatures bound every engine ever built. The proof depends only on the fact that entropy is a state function and that the total entropy of the universe can't decrease. The engineering details don't matter."

**Exclusions:** Endoreversible engine (maximum power, Curzon-Ahlborn efficiency). Refrigerators / heat pumps (COP). Stirling engine cycle.

**Score:** 9/10

---

## Card 4 — Entropy Production Calculator: Irreversibility Made Visible

**Source:** Ch 7 (Entropy) — Clausius entropy dS = δQ/T, Boltzmann entropy S = k_B ln Ω, irreversibility, free expansion, mixing

**Lane:** BUILD

**Hook:** "The cream never comes back because there are 10^(10^20) more mixed microstates than separated ones. Build the entropy calculator that makes that ratio a number you can see."

**The artifact:** d3 multi-scenario entropy production visualizer. Three scenarios user can select: (1) Free expansion: gas doubles volume at constant T. ΔS = nR ln(2), computed and shown. Number of microstates ratio Ω₂/Ω₁ = exp(ΔS/k_B) displayed (a huge power of 10). (2) Heat transfer from hot to cold: Q joules cross from T_H to T_C. ΔS_universe = Q/T_C − Q/T_H > 0 always. Visual: entropy change of hot body (negative) and cold body (positive) shown as bars; net is always positive. (3) Mixing of two gases (equal moles): entropy of mixing ΔS_mix = 2nR ln 2. Slider for n. The animation shows entropy as a running total increasing during each irreversible step.

**Prompt seed:** `claude "Build d3 v7 single-HTML entropy production visualizer. Three scenario tabs: (1) Free expansion: n moles (slider 0.1–5), ΔS=nR·ln(V₂/V₁) with V₂/V₁ slider (1–10). Display ΔS in J/K and Ω₂/Ω₁=exp(ΔS/k_B) in scientific notation (exponent to 10^x). (2) Heat transfer: Q (slider 0–1000 J), T_H (slider 400–1000 K), T_C (slider 200–400 K, < T_H). Show ΔS_hot = −Q/T_H (red bar, downward), ΔS_cold = +Q/T_C (blue bar, upward), net = sum (always positive). (3) Mixing: two ideal gases, n₁=n₂=n. ΔS_mix = 2nR·ln2. Show Boltzmann S=k_B·ln(Ω) interpretation: Ω for mixed/separated ratio. Animate entropy accumulation as a dial. SVG only."`

**Read/check:** Scenario 1: n=1, V₂/V₁=2. Verify ΔS = 1·8.314·ln(2) = 5.76 J/K. Compute Ω₂/Ω₁ = exp(5.76/1.38e-23) ≈ 10^(1.8×10²³). Scenario 2: Q=100 J, T_H=600 K, T_C=300 K. Verify ΔS_net = 100/300 − 100/600 = 0.333 − 0.167 = 0.167 J/K > 0.

**Human supplies:** Nothing — fully synthetic.

**Output medium:** d3 animated HTML (single file, SVG, CDN).

**The change:** In scenario 2, make T_H → T_C (isothermal heat transfer in the reversible limit). Watch ΔS_net → 0 from above, never reaching zero for finite ΔT. The reversible process is the ideal limit: zero entropy production, maximum work extracted, infinitely slow. Every finite-speed real process produces entropy. The faster you run an engine, the more entropy it produces and the further below Carnot efficiency it falls.

**Teardown angle:** "Boltzmann's S = k_B ln Ω is inscribed on his tombstone in Vienna. The k_B = 1.38×10⁻²³ J/K sits there converting between the world of molecules (Ω, a count) and the world of joules and kelvins (S, an engineering quantity). The exponent in Ω₂/Ω₁ for 1 mole of gas is ~10²³ — this is why you have never seen a gas spontaneously unmix."

**Exclusions:** Entropy of black holes (Bekenstein-Hawking). Non-equilibrium entropy production (Prigogine). Negentropy / information entropy (Shannon) — see capstone card.

**Score:** 8/10

---

## Card 5 — Boltzmann Distribution and Partition Function Explorer

**Source:** Ch 8 (Statistical Mechanics) — Boltzmann distribution P_i = exp(−E_i/kT)/Z, partition function Z, deriving thermodynamic quantities from Z

**Lane:** BUILD

**Hook:** "The partition function Z is the master object of statistical mechanics. Every thermodynamic quantity — energy, entropy, heat capacity — is a derivative of ln Z. Build the explorer."

**The artifact:** d3 visualization with two panels. Left panel: an energy-level system with user-defined levels (up to 8 levels, energies adjustable 0–10ε). Boltzmann occupation probability P_i = exp(−E_i/kT)/Z shown as horizontal bar at each level. Temperature slider T sweeps 0.1ε/k to 10ε/k. At T→0: ground state fully occupied. At T→∞: all levels equally occupied (P_i = 1/N). Right panel: derived quantities plotted vs T — (a) partition function Z(T), (b) average energy ⟨E⟩ = −∂ln Z/∂β, (c) heat capacity C_V = ∂⟨E⟩/∂T, (d) entropy S = k_B(ln Z + β⟨E⟩). Show Schottky anomaly: two-level system with large gap shows C_V peak at T ~ ε/(2k_B).

**Prompt seed:** `claude "Build d3 v7 single-HTML Boltzmann distribution explorer. Up to 8 energy levels, each draggable on the left panel (energies 0–10 in units of ε, start with equally spaced 0,1,2,3,4). Temperature slider β = 1/(kT) from 0.1 to 10 (in units of 1/ε). Compute Z = Σ exp(−βE_i), P_i = exp(−βE_i)/Z. Left panel: horizontal bar chart, bar width = P_i, bar at height E_i. Right panel: four line charts vs T (from 0.1 to 10 ε/k): Z(T), ⟨E⟩=−d(ln Z)/dβ (finite difference), C_V=d⟨E⟩/dT, S=k_B(ln Z + ⟨E⟩/kT). Add preset: two-level system (E=0, E=ε gap) to show Schottky peak. SVG only."`

**Read/check:** Two-level system, E₀=0, E₁=1ε. At T=0.1ε/k: P₀ ≈ 0.999, P₁ ≈ 0.001. Z ≈ 1. At T=10ε/k: P₀ ≈ P₁ ≈ 0.5. Z ≈ 2. Verify Schottky peak in C_V at T ≈ 0.42ε/k (known result for two-level system: C_V peak at T = ε/(2k_B·arccosh-related value)). Verify S approaches k_B·ln(N) as T→∞.

**Human supplies:** Nothing — fully synthetic.

**Output medium:** d3 animated HTML (single file, SVG, CDN).

**The change:** Start with N equally spaced levels and sweep T from near zero upward. Watch Z grow from 1 (ground state dominates) toward N (all states accessible). Note that ⟨E⟩ saturates as T→∞ at the average energy of all levels — no UV catastrophe for discrete levels. Switch to harmonic oscillator (E_n = nε, infinite ladder) and watch ⟨E⟩ → kT at high T (classical limit: equipartition).

**Teardown angle:** "The partition function connects statistical mechanics to thermodynamics through one formula: F = −kT·ln Z. From the Helmholtz free energy F, all other quantities follow by differentiation: S = −∂F/∂T, P = −∂F/∂V, U = F + TS. The entire thermodynamic potential landscape drops out of a single number — the sum of Boltzmann factors over all microstates."

**Exclusions:** Quantum statistics (Fermi-Dirac/Bose-Einstein partition functions — see QM card set). Grand canonical ensemble. Path integrals.

**Score:** 8/10

---

## Card 6 — Heat Transfer: Conduction, Convection, and Stefan-Boltzmann Radiation

**Source:** Ch 2 (Heat Transfer) — Fourier's law, thermal resistance in series, Newton's law of cooling, Stefan-Boltzmann radiation, Wien's law

**Lane:** BUILD

**Hook:** "We know the Sun's surface temperature to four significant figures and no spacecraft has ever touched it. The color of its light is the thermometer. Build the demo."

**The artifact:** d3 three-panel simulation. Panel 1 (Conduction): a composite wall with N layers (N up to 5). Each layer has material (copper, steel, glass, wood, fiberglass, aerogel — look-up table for k), thickness L, and area A. Thermal resistance R = L/(kA) computed per layer; total R = ΣR_i (series). Heat flux P = ΔT/R_total shown. The temperature profile across the wall is plotted — steep drops in high-R layers. Panel 2 (Newton's cooling): object at T₀ cools in ambient T_∞. ODE dT/dt = −hA(T−T_∞)/mc, solved numerically, animated as T(t) curve. Panel 3 (Radiation): Planck spectrum B(λ,T) plotted for adjustable T. Wien peak λ_max = 2898 μm·K/T shown. Stefan-Boltzmann total power P = εσAT⁴. Enter Sun's peak wavelength (502 nm) → solve for T.

**Prompt seed:** `claude "Build d3 v7 single-HTML heat transfer visualizer with three tabs. Tab 1: Composite wall — up to 5 layers, material dropdown (copper k=400, steel k=50, glass k=1, wood k=0.13, fiberglass k=0.04, aerogel k=0.013 W/mK), thickness slider 0.001–0.3 m, area 1 m². Compute R_i=L_i/(k_i·A), R_total=ΣR_i, P=ΔT/R_total, temperature profile plotted as step function. Tab 2: Newton's cooling — T₀ slider 20–200°C, T_ambient=20°C, hA/mc slider (0.001–0.1 per second). Animate exponential decay T(t)=T_ambient+(T₀-T_ambient)·exp(−hA/mc·t). Tab 3: Planck spectrum — B(λ,T) = 2hc²/λ⁵ · 1/(exp(hc/λkT)−1), T slider 300–30000 K, mark Wien peak, compute integrated power P=εσT⁴ (ε slider 0–1). SVG only."`

**Read/check:** Tab 1: Single fiberglass layer, L=0.1 m, A=1 m², k=0.04, ΔT=25°C. Verify R = 0.1/0.04 = 2.5 m²K/W, P = 25/2.5 = 10 W. Tab 3: T=5778 K (Sun). Verify Wien peak at λ = 2898/5778 = 0.501 μm = 501 nm ≈ 502 nm. Verify Stefan-Boltzmann power at ε=1 matches known solar flux (≈ 6.3×10⁷ W/m²).

**Human supplies:** Nothing — fully synthetic.

**Output medium:** d3 animated HTML (single file, SVG, CDN).

**The change:** In Panel 1, add a second layer of fiberglass and watch how the total resistance nearly doubles while the temperature at the interface shifts — the insulation layer carries almost all the temperature drop. Demonstrate why adding brick to a fiberglass wall does almost nothing for insulation: brick's R is ~0.14 m²K/W vs. fiberglass's 2.5 per 0.1 m — brick is 18× less resistive per unit thickness.

**Teardown angle:** "The thermal resistance analogy (R = L/kA, series = sum) is exact for steady-state conduction. But Newton's law of cooling is an approximation — it linearizes the actual Stefan-Boltzmann radiation (P ∝ T⁴) around the ambient temperature. For small ΔT, the linearization is excellent. For a rocket nozzle or a star, you need the full T⁴ term."

**Exclusions:** Transient conduction (heat equation PDE). Turbulent vs. laminar convection. Radiative transfer in participating media.

**Score:** 8/10

---

## Card 7 — Real Thermodynamic Cycles: Rankine and Brayton Efficiency Calculator

**Source:** Ch 9 (Thermodynamics in the Real World) — Rankine cycle (steam), Brayton cycle (jet), real engine losses, comparison to Carnot bound

**Lane:** BUILD

**Hook:** "The best power plant in the world is 60% efficient. The worst thermodynamics allows is 40%. The difference is clever cycle design. Build the calculator that shows where the efficiency goes."

**The artifact:** d3 dual-cycle visualizer. Left: Rankine cycle (steam power plant). Four stages: (1) pump compresses liquid water (isentropic), (2) boiler heats water to steam at constant P, (3) turbine expands steam (isentropic), (4) condenser cools steam back to liquid. P-h diagram (pressure vs. enthalpy) with the cycle traced as a closed loop. User adjusts boiler pressure (1–20 MPa) and condenser pressure (0.01–0.1 MPa). Efficiency η = W_net/Q_boiler computed from enthalpy differences. Comparison bar to Carnot. Right: Brayton cycle (jet engine / gas turbine). T-s diagram. Four stages: (1) isentropic compression, (2) constant-pressure combustion, (3) isentropic expansion, (4) constant-pressure exhaust. η_Brayton = 1 − T₁/T₂ = 1 − r_p^{(1−γ)/γ} where r_p = pressure ratio. Slider for r_p.

**Prompt seed:** `claude "Build d3 v7 single-HTML real thermodynamic cycle calculator. Two tabs. Tab 1: Rankine cycle. Use simplified enthalpy lookup for water (polynomial fit or table): h_f and h_g at saturation for P from 0.01 to 20 MPa. Four states: (1) saturated liquid at P_cond, (2) compressed liquid at P_boil (pump: h₂=h₁+v_f·ΔP), (3) saturated vapor at P_boil, (4) wet steam at P_cond after turbine (isentropic: s₄=s₃). W_pump=h₂-h₁, Q_boil=h₃-h₂, W_turbine=h₃-h₄, η=(W_T-W_P)/Q_boil. Plot on P-h axes. Tab 2: Brayton cycle. γ=1.4, T₁=300 K slider, T₃=900-1700 K slider, r_p=1-40 slider. T₂=T₁·r_p^((γ-1)/γ), T₄=T₃/r_p^((γ-1)/γ). η=1-T₁/T₂=1-r_p^((1-γ)/γ). Plot on T-s axes. Show Carnot η for same T_min/T_max. SVG only."`

**Read/check:** Rankine: P_boil = 5 MPa, P_cond = 0.01 MPa. At 5 MPa, h_fg ≈ 1640 kJ/kg. Expected η ≈ 30–35%. Verify η < η_Carnot using T_sat at those pressures. Brayton: r_p = 10, T₁=300 K, T₃=1200 K. Verify T₂ = 300·10^(0.286) ≈ 579 K. η_Brayton = 1 − 300/579 ≈ 0.482 = 48%.

**Human supplies:** Nothing — fully synthetic.

**Output medium:** d3 animated HTML (single file, SVG, CDN).

**The change:** In the Brayton cycle, sweep r_p from 1 to 40. Efficiency rises — but so does T₂ (compressor exit temperature). At very high r_p, the turbine inlet T₃ is only marginally above T₂, and the power output shrinks even though efficiency is high. There's an optimal pressure ratio for maximum power (Curzon-Ahlborn point). Show this trade-off: maximum efficiency ≠ maximum power.

**Teardown angle:** "The Rankine cycle's real limitation is the turbine and pump isentropic efficiency — real machines aren't isentropic. A real turbine with 85% isentropic efficiency degrades the steam more than ideal expansion; the actual exit state has higher enthalpy and the work output is reduced. Every percentage point of isentropic efficiency translates directly into cycle efficiency. Materials science limits turbine inlet temperature, and that limits everything."

**Exclusions:** Combined cycle (Rankine + Brayton in series). Refrigeration cycle / heat pump COP. Otto cycle (internal combustion).

**Score:** 8/10

---

## Card 8 — Ideal Gas Law Derivation: Pressure from Molecular Collisions

**Source:** Ch 3 (Ideal Gas and Kinetic Theory) — PV = NkT derived from Newton's second law, equipartition theorem, degrees of freedom

**Lane:** BUILD

**Hook:** "PV = NkT isn't a law of nature — it's a theorem. Derive it from billiard balls bouncing off walls, live in the browser."

**The artifact:** d3 animated simulation of N hard-sphere particles bouncing in a 2D box. Each particle moves with a random initial velocity drawn from a Maxwell-Boltzmann distribution at temperature T (set by a slider). The walls are tracked for collisions; each collision transfers momentum 2mv_x to the wall. The total force on the right wall is averaged over time and displayed as pressure P = F/A. Compare measured P to theoretical PV = NkT. Histogram of particle speeds (righthand panel) built up in real time — should approach Maxwell-Boltzmann. Toggle: turn on particle-particle collisions (elastic); observe the distribution thermalizing from a non-equilibrium initial state.

**Prompt seed:** `claude "Build d3 v7 single-HTML ideal gas molecular simulation. N=50 particles (slider 10–200) in a 400×400 px box. Each particle: mass m=1, initial speed drawn from Maxwell-Boltzmann at T=300 (slider 100–1000 K, sets ⟨KE⟩=0.5m⟨v²⟩=1.5kT with k=1 arbitrary). Particles bounce elastically off walls, transfer momentum 2mv_x per collision. Count wall collisions per frame, compute F=Δp/Δt, display P=F/(4·box_side) as running average. Plot measured P vs NkT/V (theoretical) as two horizontal bars. Build real-time speed histogram (20 bins) updated each frame; overlay Maxwell-Boltzmann curve. Toggle elastic particle-particle collisions. Animate with requestAnimationFrame. SVG only."`

**Read/check:** Set N=100, T=300. After ~100 frames, verify measured P ≈ NkT/V (within ~10% statistical noise). Verify speed histogram approaches Maxwell-Boltzmann shape. With particle-particle collisions on, start with all particles moving in one direction; verify distribution thermalizes toward M-B within ~50 collisions.

**Human supplies:** Nothing — fully synthetic.

**Output medium:** d3 animated HTML (single file, SVG, CDN).

**The change:** Double N at fixed V and T. Verify P doubles (linear in N). Double T at fixed N, V. Verify P doubles (linear in T). These are not approximations — they are exact consequences of the ideal gas model. Note what breaks the model: add a "van der Waals correction" toggle that adds a short-range repulsion and a long-range attraction between particles; observe how P deviates from NkT/V at high density.

**Teardown angle:** "The simulation uses elastic collisions — no energy lost to wall heating or internal molecular vibrations. This is why it's called 'ideal': the model ignores everything except kinetic energy. The places where it fails (near condensation, at high pressure, for polar molecules) are exactly where those neglected effects become significant."

**Exclusions:** Quantum ideal gas (Bose/Fermi corrections). Long-range interactions (plasma). Chemical reactions during collisions.

**Score:** 7/10

---

## Card 9 — Maxwell's Demon and Landauer's Principle: Information Erasure Costs Energy

**Source:** Ch 10 (Capstone: Entropy, Information, and Quantum) — Maxwell's demon, Szilard engine, Landauer's principle k_B T ln 2 per bit erased, information-theoretic entropy

**Lane:** BUILD

**Hook:** "Maxwell's demon seemed to beat the second law for 80 years. The resolution: erasing a bit of memory costs at least k_B T ln 2 joules. Build the Szilard engine that shows it."

**The artifact:** d3 animated Szilard engine simulation. A single particle in a box at temperature T. The "demon" watches which half the particle is in (left or right) and inserts a piston in the middle. The particle then expands isothermally against the piston, doing work W = k_BT·ln(2). The demon's memory bit must then be erased to reset the cycle. Erasure costs at minimum k_BT·ln(2) joules (Landauer's principle). Net thermodynamic cost: zero. The entropy bookkeeping is shown: ΔS_particle = −k_B·ln(2) (compression), ΔS_memory = +k_B·ln(2) (erasure). Total ΔS_universe = 0. Shannon entropy of the demon's 1-bit memory displayed. The cycle runs in animation with energy and entropy balance ledger.

**Prompt seed:** `claude "Build d3 v7 single-HTML Maxwell's demon / Szilard engine simulator. Four animation stages: (1) Particle bounces randomly in full box — show as moving dot. (2) Demon observes which half it's in (left/right), 50/50 random; show demon thought bubble with bit value. (3) Insert piston; particle expands isothermally against piston, extracting W = kT·ln2 displayed as 'work extracted: X mJ'. (4) Demon erases memory bit — show entropy cost k_B·T·ln2 drawn from reservoir. Entropy ledger panel: ΔS_particle, ΔS_memory_write, ΔS_memory_erase, ΔS_total (always ≥ 0). T slider 100–500 K. Run cycle button. Show Landauer limit k_B·T·ln2 in kJ/mol = R·ln2 = 5.76 J/mol at 1000 K. SVG only."`

**Read/check:** Set T=300 K. Verify k_BT·ln(2) = 1.38e-23 × 300 × 0.693 = 2.87×10⁻²¹ J per cycle. Verify R·ln(2) = 8.314 × 0.693 = 5.76 J/mol (labeled). Verify entropy ledger: write step ΔS_memory = +k_B·ln2, expand step ΔS_particle = −k_B·ln2, erase step ΔS_environment = +k_B·ln2. Total per cycle = +k_B·ln2 ≥ 0. Second law preserved.

**Human supplies:** Nothing — fully synthetic.

**Output medium:** d3 animated HTML (single file, SVG, CDN).

**The change:** Show that if you could erase memory for free (ΔS=0), the demon would violate the second law — extracting k_BT·ln(2) work per cycle at no thermodynamic cost. This is precisely what Maxwell imagined in 1867. Landauer (1961) showed why it's impossible: any irreversible logical operation (bit erasure) must dissipate at least k_BT·ln(2). In 2012, Bérut et al. measured Landauer dissipation directly in a single colloidal particle. The measurement agreed with k_BT·ln(2) to within 10%.

**Teardown angle:** "The Shannon entropy H = −Σ p_i log₂ p_i (bits) is related to Boltzmann entropy S = k_B·ln(Ω) by S = k_B·ln(2)·H. The conversion factor k_B·ln(2) = 9.57×10⁻²⁴ J/K is the cost of one bit of information at temperature T. Every computation that erases memory — which is every practical computation — has a thermodynamic floor. Modern CPUs dissipate ~10⁶ times this minimum; the Landauer limit is not yet an engineering constraint, but it's the theoretical wall."

**Exclusions:** Quantum Maxwell's demon (requires density matrices). Reversible computing (Bennett's solution). Black hole information paradox.

**Score:** 9/10

---

## Card 10 — First Law Energy Accounting: State Functions vs. Path Functions

**Source:** Ch 4 (First Law) — ΔU = Q − W, state functions vs. path functions, four process comparisons, heat capacities C_V and C_P

**Lane:** BUILD

**Hook:** "Q and W are path-dependent — they change depending on how you get from A to B. ΔU doesn't. Build the visualizer that proves it."

**The artifact:** d3 PV diagram with two different paths connecting the same two states A (P₁, V₁, T₁) and B (P₂, V₂, T₂). Path 1: isochoric then isobaric (two right angles). Path 2: smooth diagonal curve (e.g., straight line in PV space). For each path, the simulation computes W = ∫PdV (area under curve, different for each path), Q = ΔU + W, ΔU = nCᵥΔT (same for both paths, since T₁ and T₂ are fixed). Shows side-by-side bar charts: W (different), Q (different), ΔU (identical). A third panel: compare C_V and C_P for monatomic (3/2 R, 5/2 R) and diatomic (5/2 R, 7/2 R) gases, with equipartition bars showing which modes are active.

**Prompt seed:** `claude "Build d3 v7 single-HTML First Law energy accounting visualizer. n=1 mol ideal gas, R=8.314 J/(mol·K). State A: P₁=2 atm, V₁=10 L. State B sliders: P₂ (0.5–4 atm), V₂ (5–20 L). Path 1: isochoric A→A' (V=V₁, P changes to P₂) then isobaric A'→B (P=P₂, V changes to V₂). Path 2: straight line in PV space from A to B (P = P₁+(P₂-P₁)·(V-V₁)/(V₂-V₁)). Compute W₁=∫P₁dV+P₂ΔV (path 1, exact), W₂=∫PdV (path 2, trapezoid 500 pts). ΔU = nCᵥΔT = 3/2·nR·(P₂V₂−P₁V₁)/nR = 3/2(P₂V₂−P₁V₁). Q₁=ΔU+W₁, Q₂=ΔU+W₂. Show bars: W₁, W₂, Q₁, Q₂, ΔU side by side. Highlight ΔU identical. SVG only."`

**Read/check:** Set A = (2 atm, 10 L), B = (1 atm, 20 L). ΔU = 3/2·(P₂V₂−P₁V₁) = 3/2·(20,000−20,000) J·L/(L) = 0 J (isothermal at nRT = const). Verify ΔU ≈ 0. W_path1 = ∫_{10}^{10} 2atm·dV + ∫_{10}^{20} 1atm·dV = 0 + 1·10 = 10 L·atm ≈ 1013 J. W_path2 = trapezoid area under diagonal: (2+1)/2·10 L·atm = 15 L·atm ≈ 1520 J. Verify Q₁ ≠ Q₂ but ΔU₁ = ΔU₂ = 0.

**Human supplies:** Nothing — fully synthetic.

**Output medium:** d3 animated HTML (single file, SVG, CDN).

**The change:** Move state B to a point where T₂ ≠ T₁. Observe that ΔU changes (it depends on the temperature difference) but is still the same for both paths since it only depends on endpoints. Drag state B to explore: as B moves right-and-down (volume up, pressure down), what combination gives ΔU=0 (isothermal)? Answer: PV = const — the hyperbola. This makes visible why the isothermal hyperbola is special.

**Teardown angle:** "The fact that ΔU is path-independent is not a definition — it's a physical law. It encodes the impossibility of a perpetual motion machine of the first kind. If ΔU were path-dependent, you could cycle the gas through two paths between the same states, extract the difference in ΔU as work, and run forever. The conservation of energy is the statement that ΔU is always the same regardless of path."

**Exclusions:** Enthalpy H = U + PV (constant-pressure processes). Gibbs/Helmholtz free energy. Non-ideal gases (intermolecular potential contribution to U).

**Score:** 7/10

---

| Book | Status | Lane | Candidates |
|------|--------|------|------------|
| physics-plus-one-thermodynamics | SCOUTED | BUILD | 10 |
