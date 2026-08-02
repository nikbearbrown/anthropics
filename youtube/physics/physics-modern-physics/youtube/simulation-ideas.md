# Physics: Modern Physics — Simulation Ideas

**Pilot run: MANIM lane only. D3/DATAVIZ pass follows after human approval.**
*sim-scout run 2026-07-26 — all 20 chapters read.*

---

## Candidate 01 — Animate "Lorentz Factor: The Gamma Curve Asymptote"
- Source: `physics-modern-physics/chapters/01-special-relativity.md`
- Topic: Special Relativity / Lorentz Factor
- Lane: MANIM (directed animation)
- Hook: At 99% the speed of light, time runs at one-seventh normal pace — but the curve to that point is almost flat, then nearly vertical. A static table hides the cliff. Watch γ draw.
- The rule: γ = 1/√(1 − β²), where β = v/c; time dilation Δt' = γΔt₀; length contraction L' = L₀/γ; kinetic energy K = (γ−1)mc²
- Concrete numbers: β=0.5 → γ=1.155; β=0.9 → γ=2.294; β=0.99 → γ=7.089; β=0.999 → γ=22.37; muon τ₀=2.2 μs, altitude 15 km, v=0.998c → γ=15.8, observed lifetime = 34.8 μs, survival fraction to sea level ≈ 1 vs classical ≈ 10⁻²⁹
- The artifact / what moves: γ(β) curve draws from (0,1) leftward — nearly flat out to β≈0.7, then bending sharply upward, asymptoting toward infinity as β→1; three labeled dots land in sequence at β=0.5, 0.9, 0.99; a second axis on the right tracks time-dilation ratio Δt'/Δt₀ simultaneously; final beat: a muon dot placed at β=0.998 on the curve, with dashed lines showing how the observed flight path (15 km compressed to 0.95 km in muon frame) matches sea-level detection
- Output medium: Manim (mp4)
- Two testable predictions: P1: At β=0.99, γ=7.089 exactly — time runs at 1/7.089 of rest rate; P2: Atmospheric muons at β=0.998 (γ=15.8) survive from 15 km altitude to sea level with survival fraction e^{−15/(cτ₀γ)} ≈ e^{−0.34} ≈ 0.71, vs classical e^{−42} ≈ 10⁻¹⁸
- The change: Overlay kinetic energy K=(γ−1)mc² on the same β axis — at β=0.9, K≈1.3mc², showing why you can never reach c (infinite energy required)
- Human supplies (Claude can't): Nothing — fully synthetic/analytic; all parameters from physics constants and published muon data
- Teardown angle: The flatness at low β is why Newtonian mechanics worked for three centuries; the cliff at high β is why particle accelerators cost billions — you're climbing an asymptote
- Exclusions: Derivation of Lorentz transformation from Maxwell's equations; twin paradox spacetime diagrams; general relativistic corrections; 4-vector formalism
- Sim slug: modern-lorentz-gamma
- Score: 9/10

---

## Candidate 02 — Animate "Light Clock: Pythagorean Geometry of Time Dilation"
- Source: `physics-modern-physics/chapters/01-special-relativity.md`
- Topic: Special Relativity / Time Dilation
- Lane: MANIM (directed animation)
- Hook: Time dilation is not a clock malfunction — it is geometry. A light pulse bouncing between mirrors draws a longer path when the clock moves. The math falls out of Pythagoras.
- The rule: Light clock stationary: Δt₀ = 2d/c; moving at v: light traces hypotenuse of length √(d²+(vΔt/2)²) per half-trip; solving gives Δt = Δt₀/√(1−v²/c²) = γΔt₀
- Concrete numbers: d=1 m; v=0c → Δt₀=6.67 ns; v=0.6c → Δt=8.33 ns (γ=1.25); v=0.866c → Δt=13.33 ns (γ=2.0); v=0.99c → Δt=47.3 ns (γ=7.09)
- The artifact / what moves: Split screen — left panel shows stationary clock with photon bouncing vertically between two mirrors, tick period labeled Δt₀; right panel shows the same clock moving rightward at v=0.6c, photon traces diagonal paths forming a sawtooth, period labeled Δt; the right-triangle formed by d (vertical), vΔt/2 (horizontal), and ct/2 (hypotenuse) materializes and flashes; then β sweeps from 0 to 0.99, and both panels update synchronously — the right-panel tick period visibly stretching
- Output medium: Manim (mp4)
- Two testable predictions: P1: At v=0.866c (β=√3/2), γ=2.000 exactly — the stationary clock ticks twice for every moving clock tick; P2: The triangle satisfies (cΔt/2)²=(vΔt/2)²+d², yielding γ=1/√(1−v²/c²) — algebraically exact, checkable by substitution
- The change: Swap to a "ruler clock" (photon bouncing end-to-end along direction of motion) to derive length contraction — the two derivations in sequence reveal the asymmetry between time and space
- Human supplies (Claude can't): Nothing — fully synthetic/analytic; pure geometric construction
- Teardown angle: Einstein's genius was not the equation — it was the two postulates that made the geometry mandatory. The clock just makes you watch the constraint play out
- Exclusions: Doppler effect for light; Minkowski spacetime diagrams; Lorentz-boost matrix derivation; relativity of simultaneity demonstration
- Sim slug: modern-light-clock
- Score: 9/10

---

## Candidate 03 — Animate "Photoelectric Effect: Threshold Frequency and the Stopped Electron"
- Source: `physics-modern-physics/chapters/04-the-quantum-nature-of-light.md`
- Topic: Photoelectric Effect / Quantization of Light
- Lane: MANIM (directed animation)
- Hook: Brighter light doesn't eject faster electrons — higher frequency does. A wave theory predicts otherwise. Watch KEmax = hf − BE draw as a line with a threshold, and the classical prediction diverge from it
- The rule: KEmax = hf − BE (Einstein 1905); stopping voltage V_stop = KEmax/e; threshold frequency f₀ = BE/h; no emission below f₀ regardless of intensity
- Concrete numbers: Sodium: BE=2.28 eV, f₀=5.51×10¹⁴ Hz (λ≈544 nm); green light at f=6.0×10¹⁴ Hz → KE=0.20 eV; blue at f=7.5×10¹⁴ Hz → KE=0.82 eV; h=6.626×10⁻³⁴ J·s; Millikan's measured slope gave h to 1.5% accuracy
- The artifact / what moves: Horizontal frequency axis draws; a vertical threshold line rises at f₀=5.51×10¹⁴ Hz; KEmax line draws from zero at threshold, rising linearly to the right with slope h; three colored photon arrows drop at f<f₀ (red, bounces, no electron), f=f₀ (orange, barely ejects, KE≈0), f>f₀ (blue, ejects fast electron); a classical "intensity" control appears — cranking it up has zero effect on the KE line; a second comparison panel shows the classical wave prediction (KE grows with intensity, not frequency) flatly contradicted
- Output medium: Manim (mp4)
- Two testable predictions: P1: Slope of KEmax vs f equals h=6.626×10⁻³⁴ J·s — the same Planck constant from blackbody radiation, a completely different experiment; P2: Threshold wavelength for sodium λ₀=c/f₀=544 nm — green light at 550 nm barely fails to eject electrons, blue at 450 nm does
- The change: Switch metal to gold (BE=5.1 eV, f₀=1.23×10¹⁵ Hz, deep UV only) — shows that the threshold shifts right, demonstrating BE is a material property, not a light property
- Human supplies (Claude can't): Nothing — fully synthetic/analytic; all BE values from published photoemission data
- Teardown angle: Millikan spent years trying to disprove Einstein's photon hypothesis and ended up measuring h to within 0.5%. The experiment that should have killed the photon confirmed it
- Exclusions: Derivation of Planck's blackbody formula; Compton scattering calculation; quantum efficiency and secondary emission; photodiode circuit applications
- Sim slug: modern-photoelectric
- Score: 9/10

---

## Candidate 04 — Animate "Bohr Energy Ladder: Electron Drops and Balmer Series"
- Source: `physics-modern-physics/chapters/05-the-atom.md`
- Topic: Hydrogen Atom / Bohr Model
- Lane: MANIM (directed animation)
- Hook: The hydrogen spectrum is not a rainbow — it's a precise set of lines spaced by an exact formula. Watch the electron drop between rungs of a ladder it can only stand on, each drop firing one photon at one exact wavelength.
- The rule: En = −13.6 eV / n² (n=1,2,3,…); photon energy hf = En_i − En_f; wavelength 1/λ = R_H(1/n_f² − 1/n_i²); Balmer series n_f=2: Hα=656.3 nm, Hβ=486.1 nm, Hγ=434.0 nm, Hδ=410.2 nm
- Concrete numbers: n=1: E=−13.6 eV; n=2: E=−3.40 eV; n=3: E=−1.51 eV; n=4: E=−0.85 eV; n→∞: E=0; Lyman limit 91.2 nm; Balmer Hα 656.3 nm (red), Hβ 486.1 nm (blue-green)
- The artifact / what moves: Energy ladder draws on the left with labeled rungs n=1 through 6 and their eV values; an electron dot sits at n=4; transition arrow drops from n=4 to n=2 (Hβ), simultaneously a photon wave packet animates rightward with wavelength 486.1 nm drawn as oscillating waveform; a spectrum strip at bottom grows: each transition lands a colored vertical line at the correct wavelength; sequence repeats for all Balmer transitions in order (n=3,4,5,6 → n=2), filling in the Balmer series from red to violet; Lyman and Paschen series appear briefly as separate sub-spectra
- Output medium: Manim (mp4)
- Two testable predictions: P1: Hα (n=3→n=2) = 656.3 nm exactly — matches Ångström's 1853 measurement; P2: Series limit (n→∞ → n=2) at λ=364.6 nm, beyond which a continuum begins — the ionization edge is a testable prediction of the 1/n² formula
- The change: Switch to singly-ionized helium He⁺ (Z=2): En=−54.4/n² eV — Balmer analog lines shift into ultraviolet, demonstrating the Z² scaling of the Rydberg formula
- Human supplies (Claude can't): Nothing — fully synthetic/analytic; all wavelengths from Rydberg formula with R_H=1.097×10⁷ m⁻¹
- Teardown angle: Bohr got the right answer with a wrong model — quantization of angular momentum was a guess, not a derivation. It took de Broglie's standing waves and then Schrödinger to explain why
- Exclusions: Derivation from de Broglie standing waves; Sommerfeld elliptical orbits; Zeeman effect; fine structure; derivation of Rydberg constant from fundamental constants
- Sim slug: modern-bohr-ladder
- Score: 9/10

---

## Candidate 05 — Animate "Blackbody Radiation: The Ultraviolet Catastrophe and Planck's Fix"
- Source: `physics-modern-physics/chapters/04-the-quantum-nature-of-light.md`
- Topic: Blackbody Radiation / Birth of Quantum Theory
- Lane: MANIM (directed animation)
- Hook: Classical physics predicted that a hot oven emits infinite power at short wavelengths. A tungsten bulb would be an X-ray bomb. Watch the Rayleigh-Jeans curve diverge while Planck's curve peaks and falls.
- The rule: Planck: B_λ=(2hc²/λ⁵)/(e^{hc/λkT}−1); Rayleigh-Jeans (classical): B_λ^{RJ}=2ckT/λ⁴ (diverges as λ→0); Wien's law: λ_peak=b/T (b=2.898×10⁻³ m·K); Stefan-Boltzmann: P=σT⁴ (σ=5.67×10⁻⁸ W m⁻² K⁻⁴)
- Concrete numbers: Sun T=5778 K → λ_peak=502 nm (green); tungsten bulb T=2800 K → λ_peak=1035 nm (near IR, <10% visible); human body T=310 K → λ_peak=9.35 μm (mid-IR); Rayleigh-Jeans at λ=200 nm, T=6000 K gives B_λ^{RJ} ≈ 5× larger than Planck
- The artifact / what moves: Wavelength axis draws; Planck curve for T=5778 K draws from right (IR) to left (UV), peaks at 502 nm, then falls — area under curve shaded; Rayleigh-Jeans curve draws simultaneously, matching Planck in the IR but then diverging upward past the Planck peak and continuing off-screen; UV catastrophe labeled with an arrow; temperature then sweeps from 3000 K to 8000 K — Planck curve shifts left and grows, Wien peak marker slides; at each temperature the RJ divergence worsens, emphasizing the failure
- Output medium: Manim (mp4)
- Two testable predictions: P1: λ_peak × T = 2.898×10⁻³ m·K — for T=5778 K, λ_peak=502 nm, checkable against solar spectral peak observations; P2: Rayleigh-Jeans and Planck agree to within 1% when hc/λkT ≪ 1, i.e. λ ≫ hc/kT ≈ 5 mm at 290 K — in the microwave regime classical and quantum are identical
- The change: Overlay CMB at T=2.725 K — λ_peak=1.06 mm, perfectly Planckian; the curve narrows and shifts deep into microwave, showing the universe itself is a blackbody
- Human supplies (Claude can't): Nothing — fully synthetic/analytic; Planck curve computed from formula with h, c, k
- Teardown angle: The ultraviolet catastrophe was not a minor discrepancy — it was the prediction that every hot object should immediately radiate away all energy as X-rays. Planck's quantization was introduced to fix an embarrassment, not to launch a revolution
- Exclusions: Derivation of Rayleigh-Jeans from equipartition; cavity mode counting; Bose-Einstein statistics derivation; quantum field theory connection
- Sim slug: modern-blackbody-uv-catastrophe
- Score: 8/10

---

## Candidate 06 — Animate "Binding Energy per Nucleon: The Iron Peak and Fusion-Fission Arrows"
- Source: `physics-modern-physics/chapters/13-radioactivity-and-nuclear-physics.md`
- Topic: Nuclear Physics / Binding Energy
- Lane: MANIM (directed animation)
- Hook: Iron-56 is the graveyard of stellar fusion — and the reason a supernova releases more energy than the Sun emits in ten billion years. Watch the binding-energy-per-nucleon curve draw, fusion arrows converge from the left, fission arrows converge from the right.
- The rule: BE/A = (Z·m_p + N·m_n − M_nucleus)c²/A; maximum at Fe-56 (BE/A = 8.79 MeV); fusion of light nuclei (A<56) releases energy; fission of heavy nuclei (A>56) releases energy; both processes release energy by moving toward the peak
- Concrete numbers: ²H (deuterium): BE/A=1.11 MeV; ⁴He (alpha): BE/A=7.07 MeV; ¹²C: BE/A=7.68 MeV; ⁵⁶Fe: BE/A=8.79 MeV (maximum); ²³⁵U: BE/A=7.59 MeV; fusion of 4p→⁴He releases 26.7 MeV; ²³⁵U fission releases ~200 MeV per event
- The artifact / what moves: A (mass number) axis draws from 0 to 238; BE/A curve draws point by point, rising steeply through ²H, ³He, ⁴He (visible bump), continuing to rise through C, O, up to Fe-56 peak, then gently declining through Pb, U; Fe-56 peak is labeled with a gold marker; a blue arrow sweeps from ²H to ⁴He on the left slope, labeled "fusion — energy released"; a red arrow sweeps from ²³⁵U toward ¹⁴⁰Ba+⁹⁴Kr on the right slope, labeled "fission — energy released"; both arrows point toward the Fe-56 summit
- Output medium: Manim (mp4)
- Two testable predictions: P1: BE/A maximum at Fe-56 = 8.794 MeV/nucleon — checkable against Atomic Mass Evaluation 2020 table; P2: Fusion of 4 protons to ⁴He releases 26.73 MeV = 4×(1.007825 − 0.25×4.002602)×931.5 MeV/u — exact mass-defect calculation
- The change: Overlay the nucleosynthesis schedule for a massive star — H→He core, then He→C shell, then C/O→Ne/Mg→Si→Fe ash — each stage drawn as a sequence of arrows up the left slope until fusion stops at iron
- Human supplies (Claude can't): Nothing — fully synthetic/analytic; all BE/A values from published nuclear mass tables
- Teardown angle: Stars manufacture every element up to iron for free. Everything heavier — gold, lead, uranium — cost a supernova. The curve explains why the universe is mostly iron and why heavy elements are rare
- Exclusions: Shell model derivation of BE curve features; liquid drop model formula; magic numbers; semi-empirical mass formula derivation; neutrino emission in beta decay
- Sim slug: modern-binding-energy-curve
- Score: 9/10

---

## Candidate 07 — Animate "Alpha Decay and Quantum Tunneling: The Gamow Factor"
- Source: `physics-modern-physics/chapters/13-radioactivity-and-nuclear-physics.md`
- Topic: Nuclear Physics / Quantum Tunneling
- Lane: MANIM (directed animation)
- Hook: An alpha particle inside a uranium nucleus has less energy than the Coulomb barrier surrounding it. Classically, it cannot escape — ever. Quantum mechanically, it leaks through. Watch the wavefunction decay exponentially inside the barrier, emerge on the other side, and confirm the Geiger-Nuttall plot.
- The rule: Gamow factor G = (1/ℏ)∫√(2m(V(r)−E))dr over the classically forbidden region; tunneling probability T ≈ e^{−2G}; Coulomb barrier V(r)=kZze²/r for r>R_nuclear; Geiger-Nuttall: log t_{1/2} ∝ 1/√E_α (straight line across 24 decades of half-life)
- Concrete numbers: ²³⁸U: E_α=4.27 MeV, Coulomb peak≈27 MeV at r≈9 fm, t_{1/2}=4.47×10⁹ yr; ²¹²Po: E_α=8.78 MeV, t_{1/2}=298 ns; barrier width for U ≈ 30 fm; G(U)≈87, T≈e^{−174}≈10⁻⁷⁶ — yet U decays
- The artifact / what moves: Potential energy curve draws — Coulomb repulsion (1/r) outside, nuclear well inside; alpha-particle energy E_α drawn as horizontal dashed line well below the Coulomb peak; classically forbidden region between R_nuclear and R_outer shaded grey; wavefunction |ψ|² draws: oscillatory inside the nucleus, exponentially decaying through the barrier, small oscillatory tail outside; then two isotopes appear side by side (²³⁸U and ²¹²Po) — Po's E_α is higher, barrier is narrower, |ψ| outside is larger, t_{1/2} 24 orders of magnitude shorter
- Output medium: Manim (mp4)
- Two testable predictions: P1: Log t_{1/2} vs 1/√E_α for known alpha emitters falls on a straight line (Geiger-Nuttall, 1911) — six nuclides from ²³²Th to ²¹²Po span the line exactly; P2: ²¹²Po t_{1/2}=298 ns corresponds to tunneling frequency ×barrier probability ≈ 10²¹ Hz × e^{−2G} — quantitative match to the Gamow formula
- The change: Scale down E_α to 1 MeV (hypothetical) — barrier width nearly doubles, half-life jumps from centuries to longer than the universe's age; demonstrates the extreme sensitivity of tunneling to barrier width
- Human supplies (Claude can't): Nothing — fully synthetic/analytic; Coulomb barrier from V=kZ₁Z₂e²/r; Gamow integral approximable analytically
- Teardown angle: Radioactivity is not random in the intuitive sense — it's quantum certainty about a probability. Every U-238 nucleus has the same probability per second of decaying. The randomness is in when, not whether. And "whether" is guaranteed by a wavefunction that leaks
- Exclusions: Beta decay (weak force, entirely different mechanism); gamma decay; shell model magic numbers; neutron-to-proton ratio stability belt; nuclear reactions (fission/fusion reactor physics)
- Sim slug: modern-gamow-tunneling
- Score: 9/10

---

## Candidate 08 — Animate "Nuclear Decay: N(t) = N₀ e^{−λt} and Half-Life Staircase"
- Source: `physics-modern-physics/chapters/13-radioactivity-and-nuclear-physics.md`
- Topic: Nuclear Physics / Radioactive Decay
- Lane: MANIM (directed animation)
- Hook: Every radioactive atom has the same probability of decaying in the next second, regardless of age. The ensemble creates a smooth exponential — but the individual atoms fall off in a staircase the law never predicts. Watch both.
- The rule: N(t) = N₀ e^{−λt}; half-life t_{1/2} = ln2/λ; activity A = λN(t) = A₀ e^{−λt}; mean lifetime τ = 1/λ = t_{1/2}/ln2
- Concrete numbers: ¹⁴C: t_{1/2}=5730 yr, λ=3.83×10⁻¹² s⁻¹; after 5730 yr: N=N₀/2; after 17190 yr: N=N₀/8; after 57300 yr (10 half-lives): N=N₀/1024 ≈ 0.1%; ²²⁶Ra: t_{1/2}=1600 yr; ¹³¹I (medical): t_{1/2}=8.02 days
- The artifact / what moves: N-axis (log scale) on left; continuous exponential N(t) draws as a smooth curve from N₀; simultaneously, a staircase of discrete decay events drops in random sequence — visibly noisy but hugging the exponential envelope; half-life markers draw as horizontal dashed lines at N₀/2, N₀/4, N₀/8 at equal time spacings; activity A(t) simultaneously draws on a second panel below, identical shape — then t_{1/2} slider sweeps, compressing or expanding the decay time axis while the shape stays the same
- Output medium: Manim (mp4)
- Two testable predictions: P1: Three half-lives reduce N to exactly N₀/8 = 12.5% — checkable at any t_{1/2} value; P2: Mean lifetime τ = t_{1/2}/ln2 ≈ 1.443 × t_{1/2} — at t=τ, N=N₀/e ≈ 0.368 N₀, not N₀/2; the two times are distinct and checkable
- The change: Overlay ¹⁴C and ¹³¹I on the same panel — ¹³¹I collapses to near-zero in a week while ¹⁴C barely budges over the same interval, demonstrating the 4-order-of-magnitude range in half-life for common isotopes
- Human supplies (Claude can't): Nothing — fully synthetic/analytic; stochastic events generated from Poisson process with rate λ
- Teardown angle: Radiocarbon dating works because ¹⁴C is replenished in living organisms by cosmic-ray neutrons and stops at death. The clock starts when you stop breathing. The exponential decay is the clock
- Exclusions: Decay chains (Ra→Rn→Po→Pb); secular equilibrium; branching ratios; radiation dose and health effects; nuclear reactor criticality
- Sim slug: modern-decay-halflife
- Score: 8/10

---

## Candidate 09 — Animate "Chandrasekhar Limit: White Dwarf Mass-Radius Curve"
- Source: `physics-modern-physics/chapters/07-the-death-of-stars.md`
- Topic: Stellar Physics / White Dwarfs
- Lane: MANIM (directed animation)
- Hook: Add mass to a white dwarf and it shrinks. Keep adding and it collapses to zero radius at 1.4 solar masses. This is not an engineering limit — it's a quantum mechanical one. Watch the mass-radius curve bend toward zero.
- The rule: Non-relativistic: R ∝ M^{−1/3} (electron degeneracy pressure balances gravity); relativistic: pressure softens as electrons approach c, curve bends down; Chandrasekhar limit M_Ch = (5.87/μ_e²) M_☉ ≈ 1.44 M_☉ (for μ_e=2, fully ionized carbon/oxygen)
- Concrete numbers: 0.5 M_☉ WD: R ≈ 0.017 R_☉ ≈ 12,000 km; 1.0 M_☉: R ≈ 8,500 km; 1.3 M_☉: R ≈ 4,000 km; 1.44 M_☉: R → 0 (theoretical); Sirius B: 1.02 M_☉, R=5800 km (Earth-sized)
- The artifact / what moves: Mass axis draws from 0 to 1.5 M_☉; two curves draw simultaneously — non-relativistic (blue, monotonically decreasing, M^{-1/3} shape) and full Chandrasekhar result (orange, bending more steeply downward and asymptoting to zero at M_Ch); a vertical dashed line rises at M_Ch=1.44 M_☉; Sirius B plotted as a labeled dot; as the curves draw, an annotation shows "non-rel agrees below 0.5 M_☉, diverges above"; a second panel beside it shows what happens past M_Ch: neutron star or black hole endpoints
- Output medium: Manim (mp4)
- Two testable predictions: P1: Sirius B (1.02 M_☉) should have R≈5,800 km — Hubble Space Telescope measurement gives 5,840 km, within 1%; P2: The mass-radius relation inverts the normal trend: more massive WDs are smaller (R ∝ M^{−1/3}), the opposite of normal stars
- The change: Add neutron star mass-radius curve (completely different physics — nuclear repulsion) starting from a neutron star radius of ~10 km above 1.44 M_☉, then a black hole Schwarzschild radius line — three objects, three regimes, one plot
- Human supplies (Claude can't): Nothing — fully synthetic/analytic; mass-radius relation derived from polytrope equations; Sirius B data from published HST measurement
- Teardown angle: Chandrasekhar derived this at age 19 on a steamship from India to England. Eddington publicly ridiculed him. Chandrasekhar was right. There is a maximum mass for a cold dead star, and it is nature's way of announcing that black holes are mandatory
- Exclusions: Polytrope derivation; neutron star equation of state; Tolman-Oppenheimer-Volkoff equation; Type Ia supernova light-curve standardization; thermonuclear explosion mechanism
- Sim slug: modern-chandrasekhar-limit
- Score: 8/10

---

## Candidate 10 — Animate "LIGO Chirp: Binary Black Hole Inspiral and Gravitational Wave Frequency Sweep"
- Source: `physics-modern-physics/chapters/08-black-holes-and-curved-spacetime.md`
- Topic: Gravitational Waves / General Relativity
- Lane: MANIM (directed animation)
- Hook: Two black holes 1.3 billion light-years away spiraled together over a billion years, then merged in 0.2 seconds. The entire energy of a few suns converted to spacetime ripples, and LIGO felt a displacement of 10⁻¹⁸ meters — smaller than a proton. Watch the chirp.
- The rule: Gravitational wave frequency f_GW = 2 × orbital frequency; chirp rate df/dt ∝ M_chirp^{5/3} f^{11/3}; strain h = (4G/c⁴r)×(second time derivative of mass quadrupole moment); GW150914: M₁=36 M_☉, M₂=29 M_☉, merger product 62 M_☉ (3 M_☉ radiated)
- Concrete numbers: GW150914: f sweeps 35→250 Hz over 0.2 s; peak strain h≈10⁻²¹; LIGO arm length 4 km → displacement 4×10⁻¹⁸ m; chirp mass M_c=28.3 M_☉; final BH mass 62 M_☉; energy radiated 3×M_☉c²=5.4×10⁴⁷ J (equivalent to Sun's total lifetime output × 10)
- The artifact / what moves: Left panel: two black hole dots orbit each other — orbit visibly shrinking as they spiral inward over a compressed timeline; right panel: h(t) strain waveform draws in real time, frequency visibly increasing as the oscillation tightens; a spectrogram below shows f(t) as a bright sweeping line (the chirp); merger moment: both panels flash at the ringdown; final annotation: "3 solar masses → gravitational waves in 0.2 seconds"
- Output medium: Manim (mp4)
- Two testable predictions: P1: Chirp mass M_c = (M₁M₂)^{3/5}/(M₁+M₂)^{1/5} = 28.3 M_☉ for GW150914 — directly extractable from the rate of frequency increase (df/dt), checkable against LIGO parameter estimation; P2: Gravitational wave frequency at merger = 2 × orbital frequency at innermost stable circular orbit ≈ 2×(c³/6πGM)^{1/2} ≈ 150 Hz for 65 M_☉ final mass — matches the observed peak at ~150 Hz
- The change: Scale to a neutron star merger (M₁=M₂=1.4 M_☉) — chirp mass drops to 1.2 M_☉, inspiral takes longer, frequency at merger ~1600 Hz (outside LIGO's peak sensitivity), explaining why GW170817 required different analysis
- Human supplies (Claude can't): Nothing for the animation — waveform can be synthesized from post-Newtonian approximation; optionally the actual LIGO GW150914 strain data (public, GWOSC) for overlay validation
- Teardown angle: The detection was a 5-sigma event, but the smoking gun was the chirp mass. LIGO measured the mass of objects it couldn't see, from a billion light-years away, using rulers smaller than a proton. And it matched general relativity to within measurement noise
- Exclusions: Full numerical relativity derivation; ringdown quasi-normal modes; multi-messenger follow-up (GW+EM); LISA space antenna; matched-filter data analysis pipeline
- Sim slug: modern-ligo-chirp
- Score: 8/10

---

## Summary

| # | Title | Lane | Score | Slug |
|---|---|---|---|---|
| 01 | Lorentz Factor Asymptote | MANIM | 9/10 | modern-lorentz-gamma |
| 02 | Light Clock Time Dilation | MANIM | 9/10 | modern-light-clock |
| 03 | Photoelectric Effect Threshold | MANIM | 9/10 | modern-photoelectric |
| 04 | Bohr Energy Ladder + Balmer Series | MANIM | 9/10 | modern-bohr-ladder |
| 05 | Binding Energy per Nucleon | MANIM | 9/10 | modern-binding-energy-curve |
| 06 | Alpha Decay Gamow Tunneling | MANIM | 9/10 | modern-gamow-tunneling |
| 07 | Blackbody UV Catastrophe | MANIM | 8/10 | modern-blackbody-uv-catastrophe |
| 08 | Nuclear Decay Half-Life | MANIM | 8/10 | modern-decay-halflife |
| 09 | Chandrasekhar Limit Curve | MANIM | 8/10 | modern-chandrasekhar-limit |
| 10 | LIGO Chirp Inspiral | MANIM | 8/10 | modern-ligo-chirp |

**Build-soon (≥9/10):** Candidates 01–06 (six cards). All are self-contained, fully synthetic, and directly animate rules students are expected to know but rarely see move.

**D3/DATAVIZ pass (future):** Compton scattering angle-energy interactive; Monte Carlo nuclear decay chain simulator; Hubble diagram with real galaxy data.
