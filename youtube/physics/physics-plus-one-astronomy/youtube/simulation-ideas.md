# Physics: Astronomy (Plus One) — Simulation Ideas

**Pilot run: MANIM lane only — D3/DATAVIZ candidates deferred to a second pass.**

*sim-scout run 2026-07-26 — chapters read: 01, 03, 05, 08, 11, 13 and supporting chapters.*

---

## Candidate 01 — Animate "The Planck Curve Kills the Ultraviolet Catastrophe"
- Source: `physics-plus-one-astronomy/chapters/03-radiation-and-spectra.md`
- Topic: Blackbody radiation
- Lane: MANIM (directed animation)
- Hook: The classical Rayleigh-Jeans law predicts infinite brightness at short wavelengths — the Planck spectrum cuts it off cold at the exact frequency where stars actually peak.
- The rule: B_λ(T) = (2hc²/λ⁵) / (e^{hc/λkT} − 1); and Wien's law λ_peak = b/T, b = 2.898×10⁻³ m·K.
- Concrete numbers: T = 3 000 K (M dwarf, peak ~966 nm, near-IR), 5 778 K (Sun, peak ~502 nm, green), 10 000 K (A star, peak ~290 nm, UV). Compare Rayleigh-Jeans B_λ ∝ λ⁻⁴T overlay at each T.
- The artifact / what moves: Two curves draw simultaneously — Planck (correct) vs Rayleigh-Jeans (dashed, diverges to ∞ left). A temperature slider morphs both curves; λ_peak marker rides the Planck peak leftward as T rises. Rayleigh-Jeans crashes off screen; Planck stays finite.
- Output medium: Manim (mp4)
- Two testable predictions: P1: At T = 5 778 K the Planck peak lands at 502 nm (green), confirmed against NIST blackbody tables. P2: The Rayleigh-Jeans curve exceeds Planck by >50× at λ = 200 nm for T = 5 778 K — visible divergence in the animation.
- The change: Replace the T slider with a mass/radius sweep across stellar spectral classes (O → M), showing how surface temperature alone sets observed color.
- Human supplies (Claude can't): Nothing — fully synthetic/analytic; all curves computed from the closed-form Planck and Rayleigh-Jeans expressions.
- Teardown angle: Every star is a blackbody. The "ultraviolet catastrophe" wasn't a minor correction — classical physics predicted the universe glows infinitely bright at short wavelengths. Planck's fix, uncomfortable to him, was the first quantum.
- Exclusions: Derivation of the Planck distribution from statistical mechanics; photon gas formalism; color-rendering index details; stellar atmosphere corrections.
- Sim slug: astro-planck-blackbody
- Score: 9/10

---

## Candidate 02 — Animate "Spacetime Curves: Time Slows at the Schwarzschild Horizon"
- Source: `physics-plus-one-astronomy/chapters/11-black-holes-and-curved-spacetime.md`
- Topic: Schwarzschild radius and gravitational time dilation
- Lane: MANIM (directed animation)
- Hook: A clock near a black hole runs slower than one far away — and as r → R_S, the far observer watches it freeze. This is not science fiction; GPS satellites must correct for exactly this effect.
- The rule: Gravitational time dilation: dt_∞/dt_r = 1/√(1 − R_S/r), where R_S = 2GM/c².
- Concrete numbers: M = 10 M_☉ stellar black hole → R_S ≈ 29.5 km. Clocks at r = 2R_S run at 1/√(1−0.5) ≈ 1.41× slower; at r = 1.01R_S: 1/√(0.01) = 10× slower.
- The artifact / what moves: A radial axis draws from r = R_S outward. A clock face animates at each labeled radius; tick rate visually slows as r decreases toward R_S. The time-dilation factor dt_∞/dt_r is numerically displayed and rises toward ∞. The curve dt_∞/dt_r vs r/R_S draws in from the right, diverging at r/R_S = 1.
- Output medium: Manim (mp4)
- Two testable predictions: P1: At r = 2R_S (r/R_S = 2): dt_∞/dt_r = √2 ≈ 1.414 — animating clock runs at 70.7% of distant rate. P2: At r = 1.5R_S: dt_∞/dt_r = √3 ≈ 1.732 — clock at the photon sphere runs at 57.7% rate.
- The change: Overlay the M87* black hole (M = 6.5×10⁹ M_☉, R_S ≈ 19.2 billion km) to compare stellar vs supermassive scale while the time-dilation curve stays identical in r/R_S units.
- Human supplies (Claude can't): Nothing — fully synthetic/analytic.
- Teardown angle: The Schwarzschild radius is not just a math curiosity — it is a real surface where time stops for a distant observer. LIGO hears what happens when two of these objects collide; the EHT photographs the shadow. The physics is already here.
- Exclusions: Kerr metric for rotating black holes; Penrose diagrams; interior Schwarzschild geometry; derivation from Einstein field equations.
- Sim slug: astro-schwarzschild-time-dilation
- Score: 9/10

---

## Candidate 03 — Animate "Jeans Collapse: Where Gravity Beats Pressure"
- Source: `physics-plus-one-astronomy/chapters/08-birth-of-stars.md`
- Topic: Jeans instability and star formation
- Lane: MANIM (directed animation)
- Hook: A gas cloud does nothing for millions of years — then crosses the Jeans mass threshold and collapses in free fall. The border between stable cloud and newborn star is a single inequality.
- The rule: Jeans mass M_J ∝ T^(3/2) / ρ^(1/2); free-fall time t_ff ≈ √(3π/32Gρ). Collapse occurs when M > M_J.
- Concrete numbers: T = 10 K (cold molecular cloud), ρ = 10⁻²¹ kg/m³ → M_J ≈ 1–2 M_☉. Free-fall time ≈ 1 Myr. At T = 100 K (warm HII region): M_J ≈ 30 M_☉, only massive clouds collapse.
- The artifact / what moves: A 2D plane with axes T (10–100 K) and ρ (10⁻²² to 10⁻²⁰ kg/m³). The M_J(T,ρ) contour draws as a curve; a dot representing a real molecular cloud moves along a cooling/compression track and crosses the contour — at crossing, a collapse animation fires: a sphere shrinks toward a protostar point. t_ff counter runs.
- Output medium: Manim (mp4)
- Two testable predictions: P1: At T = 10 K, ρ = 10⁻²¹ kg/m³, M_J ≈ 1.8 M_☉ — consistent with observed solar-mass star-forming cores. P2: Doubling T raises M_J by factor 2^(3/2) ≈ 2.83 — visible as contour shift in the animation.
- The change: Animate a fragmentation sequence: a high-mass cloud above M_J starts collapsing, then subdivides into sub-Jeans fragments (cluster formation).
- Human supplies (Claude can't): Nothing — fully synthetic/analytic.
- Teardown angle: Stars don't form because gas "wants" to collapse. They form when conditions push a cloud across a threshold that gravity calculates without asking permission. Most clouds never make it.
- Exclusions: Magnetic field support (ambipolar diffusion); angular momentum / accretion disk formation; stellar feedback loops; full numerical MHD.
- Sim slug: astro-jeans-collapse
- Score: 9/10

---

## Candidate 04 — Animate "The CMB Blackbody: 2.725 K Relic from 380,000 Years Ago"
- Source: `physics-plus-one-astronomy/chapters/13-the-big-bang.md`
- Topic: Cosmic microwave background
- Lane: MANIM (directed animation)
- Hook: The best blackbody ever measured is not from a laboratory — it is the afterglow of the Big Bang, perfectly thermal at 2.725 K, peaking in microwaves you can detect with a satellite dish pointed at a blank patch of sky.
- The rule: B_λ(T = 2.725 K): Wien peak λ_peak = b/T = 2.898×10⁻³ / 2.725 ≈ 1.064 mm (microwave). Compare to Rayleigh-Jeans at same T.
- Concrete numbers: T = 2.725 K, λ_peak = 1.064 mm. COBE/FIRAS measurement uncertainty < 0.005%; deviation from perfect blackbody < 50 ppm.
- The artifact / what moves: A Planck curve draws at 2.725 K; wavelength axis spans UV to radio (10 nm to 10 cm). A label marks the microwave peak at 1.064 mm. A second overlay at T = 3 000 K (recombination) draws in a different color, then cools — the curve slides right and down to 2.725 K, showing redshift/cooling since decoupling. COBE data points appear and land exactly on the Planck curve.
- Output medium: Manim (mp4)
- Two testable predictions: P1: Wien peak at T = 2.725 K lands at λ = 1.064 mm — within 0.2% of COBE FIRAS measurement. P2: Cooling from T_recomb ≈ 3 000 K to 2.725 K corresponds to redshift factor z ≈ 1100, shown as λ shift ratio ≈ 1100× from ≈0.97 μm to 1.064 mm.
- The change: Add a ΔT/T = 10⁻⁵ anisotropy animation — the perfectly uniform curve gains a faint ripple representing the seeds of large-scale structure.
- Human supplies (Claude can't): COBE FIRAS data points (publicly available from NASA/IPAC); a synthetic stand-in is acceptable for the curve shape but real data makes the "best blackbody ever" claim tangible.
- Teardown angle: The CMB is not background noise. It is a 380,000-year-old photograph of the last moment light could travel freely. Every anisotropy is a galaxy that hasn't formed yet.
- Exclusions: CMB polarization (E/B modes); inflationary spectrum; acoustic peak derivation; baryon loading details.
- Sim slug: astro-cmb-blackbody
- Score: 8/10

---

## Candidate 05 — Animate "Hubble's Law: Recession Velocity Scales with Distance"
- Source: `physics-plus-one-astronomy/chapters/13-the-big-bang.md`
- Topic: Hubble's law and cosmic expansion
- Lane: MANIM (directed animation)
- Hook: Every galaxy in the universe is receding — and the farther away it is, the faster it moves. This is not explosion dynamics; it is space itself expanding, and the constant that describes it sets the age of the universe.
- The rule: v = H₀ d, H₀ ≈ 70 km/s/Mpc. Age estimate: t₀ ≈ 1/H₀ ≈ 14 Gyr.
- Concrete numbers: d = 1 Mpc → v = 70 km/s; d = 100 Mpc → v = 7 000 km/s; d = 4 286 Mpc → v = c (300 000 km/s, the Hubble radius).
- The artifact / what moves: A Hubble diagram draws: axes v (km/s) vs d (Mpc), 0–500 Mpc. A line v = H₀ d appears. Then individual galaxy data points scatter in, each with an error bar, clustering around the line. The slope (H₀) is read off and labeled. The Hubble radius (where v = c) is marked. An H₀ slider morphs the line — steeper H₀ gives a younger universe, shallower gives older; the implied age counter ticks in real time.
- Output medium: Manim (mp4)
- Two testable predictions: P1: At d = 10 Mpc, v = 700 km/s — matches M81 group recession velocity within observational scatter. P2: 1/H₀ = 1/(70 km/s/Mpc) ≈ 13.97 Gyr — consistent with CMB-derived age of 13.8 Gyr to within the H₀ tension.
- The change: Show the H₀ tension: overlay the CMB-derived H₀ ≈ 67.4 km/s/Mpc (Planck) vs the local distance ladder H₀ ≈ 73 km/s/Mpc (SH0ES), with the gap highlighted — two measurements, two lines, same universe.
- Human supplies (Claude can't): Real Hubble diagram data (e.g., from NED or Freedman 2001 compilation); synthetic stand-in acceptable for the animation shape but authentic points strengthen the "it's real" argument.
- Teardown angle: The universe's age is the inverse of a slope on a scatter plot. And that slope disagrees between two of the best measurements in physics. Either something is wrong with our tools, or something is very interesting about dark energy.
- Exclusions: Dark energy equation of state; deceleration parameter derivation; ΛCDM cosmological model details; peculiar velocity corrections.
- Sim slug: astro-hubble-law
- Score: 8/10

---

## Candidate 06 — Animate "The Proton-Proton Chain: Sunshine Is a Weak Interaction Bottleneck"
- Source: `physics-plus-one-astronomy/chapters/05-the-sun.md`
- Topic: Solar nuclear fusion
- Lane: MANIM (directed animation)
- Hook: The Sun is powered by nuclear fusion — but the first step (proton + proton → deuterium) requires a proton to turn into a neutron via the weak force, which is so slow that each proton waits billions of years on average. That slowness is why the Sun has lasted 4.6 billion years.
- The rule: pp chain: Step 1: p + p → ²H + e⁺ + ν_e (weak, rate-limiting, τ ≈ 9 Gyr per proton). Step 2: ²H + p → ³He + γ. Step 3: ³He + ³He → ⁴He + 2p. Net: 4p → ⁴He + 2e⁺ + 2ν_e + 26.7 MeV.
- Concrete numbers: L_☉ = 3.828×10²⁶ W requires ≈3.86×10³⁸ fusions/s. Each fusion releases 26.7 MeV = 4.28×10⁻¹² J. Mass converted to energy: 4.28×10⁹ kg/s. Neutrinos carry ≈2% of energy; ≈10¹⁰ solar neutrinos/cm²/s pass through you right now.
- The artifact / what moves: A three-step reaction diagram animates: Step 1 draws slowly (the rate-limiter is labeled with τ ≈ 9 Gyr); Steps 2 and 3 follow quickly. Total energy per chain (26.7 MeV) is tallied. A running counter shows fusions per second (3.86×10³⁸/s) and mass-to-energy conversion rate (4.28×10⁹ kg/s). A "fuel remaining" bar shows the Sun is at roughly mid-life.
- Output medium: Manim (mp4)
- Two testable predictions: P1: 4p → ⁴He releases 26.7 MeV — confirmed against nuclear binding energy tables (⁴He binding energy 28.3 MeV minus reactant rest masses). P2: Required fusion rate ≈ 3.86×10³⁸/s = L_☉ / 4.28×10⁻¹² J per event — direct arithmetic check.
- The change: Add step-by-step neutrino emission: show that each chain emits 2 neutrinos, make the neutrino flux density at Earth's surface the kicker (10¹⁰/cm²/s).
- Human supplies (Claude can't): Nothing — fully synthetic/analytic.
- Teardown angle: The Sun is not burning — it is doing the slowest possible nuclear reaction, constrained by the weakest fundamental force. A proton has to quantum-tunnel and change flavor simultaneously. If the weak force were slightly stronger, the Sun would have burned out before Earth formed.
- Exclusions: CNO cycle; heavy-element stellar burning; neutrino oscillation theory; solar neutrino problem history.
- Sim slug: astro-pp-chain
- Score: 8/10

---

## Candidate 07 — Animate "The Powers-of-Ten Ladder: 44 Orders of Magnitude"
- Source: `physics-plus-one-astronomy/chapters/01-science-and-the-universe.md`
- Topic: Astronomical scale / scientific notation
- Lane: MANIM (directed animation)
- Hook: From a proton (10⁻¹⁵ m) to the observable universe (10²⁶ m), 44 orders of magnitude separate the smallest and largest structures. Every order of magnitude is a factor of ten — and the Milky Way barely registers in the middle.
- The rule: Powers of ten: 10^n for n from −15 to +26. Key rungs: proton 10⁻¹⁵ m, atom 10⁻¹⁰ m, cell 10⁻⁵ m, human 10⁰ m, Earth 10⁷ m, AU 1.5×10¹¹ m, light-year 9.46×10¹⁵ m, parsec 3.09×10¹⁶ m, Milky Way 10²¹ m, observable universe 8.8×10²⁶ m.
- Concrete numbers: 44 orders of magnitude total span. Voyager 1 at ≈2.3×10¹³ m = 153 AU from Sun (2024). Speed of light: 3×10⁸ m/s; crosses Earth diameter in 43 ms.
- The artifact / what moves: A logarithmic ruler draws left to right, labeled from 10⁻¹⁵ to 10²⁶. Icons appear at each rung as the ruler sweeps: proton, atom, virus, cell, human, mountain, Earth, Moon distance, Sun, AU, light-year, parsec, Milky Way, Local Group, observable universe. A "zoom camera" metaphor: each step multiplies by 10×, labeled in the corner.
- Output medium: Manim (mp4)
- Two testable predictions: P1: The AU = 1.496×10¹¹ m lands between 10¹¹ and 10¹² — confirmed against JPL Horizons definition. P2: The ratio (observable universe) / (proton) = 8.8×10²⁶ / 10⁻¹⁵ = 8.8×10⁴¹ — confirmed in the animation ladder length of 41–42 steps.
- The change: Add a speed-of-light travel-time overlay: annotate each rung with how long light takes to cross it (e.g., 43 ms across Earth, 8.3 min to Sun, 4.2 yr to α Centauri).
- Human supplies (Claude can't): Nothing — fully synthetic/analytic.
- Teardown angle: The universe is not "really big." It is incomprehensibly big — and every time you think you have a handle on it, the next rung multiplies by another factor of 10. Intuition breaks around 10⁷; everything else requires the notation to even name it.
- Exclusions: Multiverse scales beyond observable universe; Planck length; derivation of parsec from parallax; historical definition of AU.
- Sim slug: astro-powers-of-ten
- Score: 8/10

---

## Candidate 08 — Animate "Radial Velocity Wobble: How 51 Peg b Was Found"
- Source: `physics-plus-one-astronomy/chapters/08-birth-of-stars.md`
- Topic: Exoplanet detection / radial velocity method
- Lane: MANIM (directed animation)
- Hook: No one has photographed 51 Pegasi b directly — it was detected as a 56 m/s wobble in starlight, a Doppler shift so small it is 1/5000th of a highway speed limit. The math behind it is orbital mechanics, measurable to meters per second from 50 light-years away.
- The rule: RV semi-amplitude K = (2πG/P)^(1/3) · m_p sin(i) / (m_* + m_p)^(2/3) / √(1−e²). Doppler: Δλ/λ = v_r/c.
- Concrete numbers: 51 Peg b: P = 4.23 days, m_p = 0.47 M_Jup = 8.9×10²⁶ kg, m_* = 1.04 M_☉, i ≈ 80°, e ≈ 0. K_predicted ≈ 56 m/s. λ shift at K = 56 m/s on Hα (656.3 nm): Δλ = 56/3×10⁸ × 656.3 nm ≈ 1.2×10⁻⁴ nm = 0.12 pm.
- The artifact / what moves: A star-planet system (top panel): star orbits barycenter while planet orbits. Bottom panel: RV curve v_r(t) draws as a sinusoid with P = 4.23 d, K = 56 m/s annotated. A spectrogram inset shows a spectral line shifting red then blue by 0.12 pm — the Doppler wobble made visible. An m_p slider morphs K; a P slider changes the period.
- Output medium: Manim (mp4)
- Two testable predictions: P1: K ≈ 56 m/s for the listed parameters — matches the 1995 Mayor & Queloz discovery paper within instrumental precision. P2: Increasing m_p by 2× doubles K linearly (in the m_p ≪ m_* limit), visible as curve amplitude doubling on the slider sweep.
- The change: Compare to Earth's 0.09 m/s signal on the Sun — show how 56 m/s was technically accessible in 1995 but 0.09 m/s requires future missions (ARES, ELT/ESPRESSO).
- Human supplies (Claude can't): Nothing — fully synthetic/analytic.
- Teardown angle: The first hot Jupiter detection was not a photograph or a transit — it was a number. 56 meters per second. A reading on a spectrograph. The planet announced itself through physics, not images.
- Exclusions: Transit photometry method; astrometry method; direct imaging contrast; full Keplerian orbit with eccentricity sweep beyond e=0.
- Sim slug: astro-rv-wobble
- Score: 8/10

---

| # | Title | Lane | Score | Slug |
|---|---|---|---|---|
| 01 | Planck Curve Kills the UV Catastrophe | MANIM | 9 | astro-planck-blackbody |
| 02 | Schwarzschild Time Dilation | MANIM | 9 | astro-schwarzschild-time-dilation |
| 03 | Jeans Collapse Threshold | MANIM | 9 | astro-jeans-collapse |
| 04 | CMB Blackbody at 2.725 K | MANIM | 8 | astro-cmb-blackbody |
| 05 | Hubble's Law: v = H₀ d | MANIM | 8 | astro-hubble-law |
| 06 | Proton-Proton Chain | MANIM | 8 | astro-pp-chain |
| 07 | Powers-of-Ten Ladder | MANIM | 8 | astro-powers-of-ten |
| 08 | Radial Velocity Wobble — 51 Peg b | MANIM | 8 | astro-rv-wobble |

*8 candidates. MANIM: 8. D3/DATAVIZ: 0 (deferred). Score ≥8: 8.*
