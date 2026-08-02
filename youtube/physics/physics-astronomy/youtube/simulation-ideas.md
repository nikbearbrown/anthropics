# Physics: Astronomy — Simulation Ideas

**Pilot run: MANIM lane only. D3/DATAVIZ pass follows after human approval.**
*sim-scout run 2026-07-26 — all 19 chapters read.*

---

## Candidate 01 — Animate "Planck Curves: Temperature Sweep, Wien Shift, Stefan-Boltzmann Growth"
- Source: `physics-astronomy/chapters/03-radiation-and-spectra.md`
- Topic: Blackbody Radiation / Stellar Spectra
- Lane: MANIM (directed animation)
- Hook: Double a star's temperature and its luminosity increases 16-fold. The peak wavelength halves. A static spectrum hides both — watch the curve reshape and the area explode as T sweeps from a cool red dwarf to a blue supergiant.
- The rule: Planck: B_λ=(2hc²/λ⁵)/(e^{hc/λkT}−1); Wien's law: λ_peak=b/T (b=2.898×10⁻³ m·K); Stefan-Boltzmann: L=4πR²σT⁴; luminosity scales as T⁴ at fixed radius
- Concrete numbers: M-dwarf T=3000 K → λ_peak=966 nm (near IR); Sun T=5778 K → λ_peak=502 nm (green); Sirius A T=9940 K → λ_peak=292 nm (UV); Rigel T=12,100 K → λ_peak=240 nm; area ratio L(Rigel)/L(Sun) at same R: (12100/5778)⁴≈19.3×; all four stars detectable as distinctly colored in visible band
- The artifact / what moves: λ-axis (100 nm to 2000 nm); B_λ curve for T=3000 K draws — small, red-peaked; T sweeps continuously 3000 K → 12000 K; peak marker slides left (Wien shift) continuously; area under curve grows visibly (×16 per doubling of T); at key temperatures (Sun, Sirius) a labeled dot freezes; a color bar under the x-axis shows the visible spectrum — as T increases, the peak sweeps from IR through red, green, toward UV; a secondary panel tracks log₁₀(L/L_Sun) vs T, parabola rising steeply
- Output medium: Manim (mp4)
- Two testable predictions: P1: λ_peak×T=2.898×10⁻³ m·K — for T=5778 K, λ_peak=502 nm; for T=3000 K, λ_peak=966 nm — checkable from Wien's law; P2: Luminosity ratio L∝T⁴ — doubling T from 3000 K to 6000 K increases L by factor 16 exactly (at same R); checkable from Stefan-Boltzmann
- The change: Fix luminosity and vary radius — show that a red giant (T=3500 K but R=100 R_Sun) can outshine a main-sequence star (T=6000 K, R=1 R_Sun) by factor L∝R²T⁴; the curve is low and IR-peaked but enormous area
- Human supplies (Claude can't): Nothing — fully synthetic/analytic; Planck function from h, c, k
- Teardown angle: We know the surface temperature of stars we can't resolve as disks. The thermometer is the color. Wien's law converts a single spectral peak into a temperature, and that temperature plus the distance gives you the luminosity. Photons carry a lot of data
- Exclusions: Stellar atmosphere opacity and limb darkening; Saha equation and ionization; photosphere depth; non-blackbody departures; spectral classification history
- Sim slug: astro-planck-temperature-sweep
- Score: 9/10

---

## Candidate 02 — Animate "Mass-Luminosity and Lifetime: Why Massive Stars Die Young"
- Source: `physics-astronomy/chapters/09-stars-adolescence-to-old-age.md`
- Topic: Stellar Physics / Main Sequence Lifetimes
- Lane: MANIM (directed animation)
- Hook: A 10-solar-mass star has 10× the fuel but burns it 3,000× faster. It lives for 30 million years — while the Sun gets 10 billion. The power law is brutal. Watch both lines draw and the lifetime ratio emerge.
- The rule: L∝M^{3.5} (main-sequence mass-luminosity); fuel ∝ M; lifetime t_MS = M/L ∝ M^{1−3.5} = M^{−2.5}; t_MS(M) = t_Sun × (M/M_Sun)^{−2.5}; t_Sun≈10 Gyr; 10 M_Sun star: t=10×10^{−2.5}=32 Myr
- Concrete numbers: 0.5 M_Sun: L=0.088 L_Sun, t=230 Gyr; 1.0 M_Sun: L=1 L_Sun, t=10 Gyr; 2.0 M_Sun: L=11.3 L_Sun, t=1.77 Gyr; 5.0 M_Sun: L=279 L_Sun, t=179 Myr; 10 M_Sun: L=3162 L_Sun, t=32 Myr; 30 M_Sun: L=140,000 L_Sun, t=5.7 Myr; all on log-log axes — both relations are straight lines
- The artifact / what moves: Log M (x-axis) and log L (y-axis) draw; L∝M^{3.5} line draws (slope 3.5 in log-log); real stellar data points drop in sequence from 0.5 to 30 M_Sun — each sits on the line; then a second panel: log M vs log t_MS; line draws with slope −2.5; both panels shown side by side; M=10 M_Sun highlighted — a vertical dashed line connects the two panels, showing L=3162 L_Sun on the left and t=32 Myr on the right; annotation: "32 million years — the Milky Way has completed 250 such lifetimes since it formed"
- Output medium: Manim (mp4)
- Two testable predictions: P1: L∝M^{3.5} — for 2 M_Sun star, L should be 2^{3.5}=11.3 L_Sun; Sirius A (2.1 M_Sun) has L≈25 L_Sun, approximately consistent (exponent varies slightly from 3.5); P2: t_MS∝M^{−2.5} — a 10 M_Sun star lives 10^{−2.5}=0.00316× as long as the Sun, i.e. 32 Myr vs 10 Gyr; consistent with observed OB-star ages in young clusters
- The change: Overlay cluster HR diagrams: young clusters (Pleiades, 100 Myr) have main-sequence turnoff at ~4 M_Sun; old clusters (globular, 10 Gyr) at ~0.9 M_Sun — the turnoff point IS the cluster age, read directly from the mass-lifetime curve
- Human supplies (Claude can't): Nothing — fully synthetic/analytic; power-law relations from stellar structure theory; stellar data from standard catalogs
- Teardown angle: Massive stars are profligate. They burn their nuclear fuel in millions of years, manufacture heavy elements, and die in supernova explosions that seed the next generation. Low-mass stars are misers — some will outlive the current age of the universe by a factor of 20. Same physics, opposite strategies
- Exclusions: Derivation of mass-luminosity from stellar structure equations; CNO vs pp chain crossover; stellar winds and mass loss; Wolf-Rayet stars; upper IMF and the Humphreys-Davidson limit
- Sim slug: astro-mass-luminosity-lifetime
- Score: 9/10

---

## Candidate 03 — Animate "Stellar Evolution Track: ZAMS → Main Sequence → Red Giant → Endpoint"
- Source: `physics-astronomy/chapters/09-stars-adolescence-to-old-age.md`
- Topic: Stellar Evolution / HR Diagram
- Lane: MANIM (directed animation)
- Hook: The Sun will swell to 200 times its current radius and engulf Mercury, Venus, and possibly Earth — not in a million years but in 5 billion. Watch the evolutionary track draw on the HR diagram, stage by stage.
- The rule: Stars spend ~90% of t_MS on ZAMS; then hydrogen shell burning → red giant branch (L up, T down); then helium core burning (horizontal branch or blue loop); then AGB, planetary nebula, white dwarf for M<8 M_Sun; supernova for M>8 M_Sun; track shape dictated by stellar structure equations
- Concrete numbers: Sun: ZAMS (L=0.7 L_Sun, T=5600 K) → current MS (L=1 L_Sun, T=5778 K) → subgiant (L=2 L_Sun, T=5500 K) → red giant tip (L=2000 L_Sun, T=3500 K, R≈200 R_Sun) → horizontal branch (L=50 L_Sun, T=5000 K) → AGB (L=5000 L_Sun, T=3000 K) → planetary nebula → WD (L=0.001 L_Sun, T=50,000 K → cooling); 5 M_Sun star red giant tip L≈10,000 L_Sun
- The artifact / what moves: Log L vs log T HR diagram draws; main sequence line draws diagonally; evolutionary track for 1 M_Sun traces: ZAMS dot placed → track animates rightward and upward onto MS → pauses (10 Gyr) → continues leftward-upward to red giant branch (rightward in T, upward in L) → helium flash dot → horizontal branch → AGB → sharp left to hot post-AGB strip → down to white dwarf cooling track; timing annotations: "spends 10 billion years here"; "becomes a red giant in 5 billion years"; a 5 M_Sun track simultaneously traces faster trajectory with blue loop visible
- Output medium: Manim (mp4)
- Two testable predictions: P1: Red giant tip luminosity for the Sun ≈2000 L_Sun (helium flash occurs here) — confirmed by stellar models and globular cluster observations of the RGB tip; P2: White dwarf cooling track has T_eff≈50,000 K immediately after planetary nebula ejection, declining on timescale of Gyrs — observed in hot DA white dwarfs
- The change: Add a 10 M_Sun track — ZAMS to supergiant branch, no helium flash, ends in supernova; overlay both tracks to show the bifurcation at M≈8 M_Sun between white dwarf and neutron star endpoints
- Human supplies (Claude can't): Nothing — fully synthetic/analytic; track derived from stellar evolution theory; specific L,T values from published stellar evolution grids (e.g. MESA, Bressan et al.)
- Teardown angle: The HR diagram is not a photograph — it's a time machine. Stars in different evolutionary stages sit in different parts of the diagram. A globular cluster's HR diagram, with its main-sequence turnoff, tells you the cluster's age to within 1 billion years. The pattern is a clock
- Exclusions: Detailed shell burning nucleosynthesis schedule; dredge-up episodes; asymptotic giant branch thermal pulses; binary star mass transfer; R-process element synthesis in neutron star mergers
- Sim slug: astro-stellar-evolution-track
- Score: 9/10

---

## Candidate 04 — Animate "Nucleosynthesis Binding Energy Curve: Why Stars Stop at Iron"
- Source: `physics-astronomy/chapters/09-stars-adolescence-to-old-age.md`
- Topic: Stellar Nucleosynthesis / Nuclear Physics
- Lane: MANIM (directed animation)
- Hook: A massive star burns hydrogen, then helium, then carbon, neon, oxygen, silicon — each stage faster than the last, each producing an ash the star then ignites. The final stage lasts one day and produces iron. Then the star collapses. Iron is the graveyard of stellar fusion.
- The rule: BE/A peaks at Fe-56 (8.79 MeV/nucleon); fusion of A<56 nuclei releases energy (moves up the slope); fusion of A>56 absorbs energy; the nucleosynthesis sequence in massive stars: H→He (pp/CNO, 10 Myr), He→C+O (triple-α, 1 Myr), C→Ne+Mg (0.6 kyr), Ne→O+Mg (1 yr), O→Si+S (6 mo), Si→Fe+Ni (1 day)
- Concrete numbers: H fusion to He: ΔBE/A ≈ 7 MeV/nucleon; He to C: ΔBE/A ≈ 0.6 MeV/nucleon; Si to Fe: ΔBE/A ≈ 0.2 MeV/nucleon; total stages of a 20 M_Sun star cover 6 orders of magnitude in timescale; Fe-56: 26 protons, 30 neutrons, BE/A=8.794 MeV
- The artifact / what moves: BE/A curve draws (A=1 to 238) — steep rise through ⁴He (bump), ¹²C, ¹⁶O, continuing to Fe-56 peak, then gentle decline; nucleosynthesis arrows appear in sequence: first arrow ²H+²H→⁴He (bottom left to ⁴He point); second triple-alpha arrow ³⁴He→¹²C; carbon burning arrow; neon, oxygen, silicon arrows, each shorter, each releasing less energy; at Fe-56: final arrow attempts to go higher but no peak exists — the arrow stops; label: "Fusion stops. Collapse begins."; timing labels: "10 million years → 1 day" as arrows compress in time
- Output medium: Manim (mp4)
- Two testable predictions: P1: BE/A maximum at Fe-56 = 8.794 MeV/nucleon — confirmed by nuclear mass tables (AME 2020); P2: Triple-alpha reaction 3⁴He→¹²C requires the Hoyle state (excited ¹²C at 7.656 MeV) — predicted by Hoyle before discovery, confirmed by Cook et al. 1957; the prediction that Hoyle had to get right to explain stellar carbon
- The change: Add the r-process arrows from Fe outward to gold and uranium — these arrows go downhill (absorb energy) and only work in the extreme neutron flux of a neutron star merger, explaining why heavy elements are rare and why a kilonova produces gold
- Human supplies (Claude can't): Nothing — fully synthetic/analytic; BE/A from nuclear mass data; timing data from published stellar evolution models
- Teardown angle: The B²FH paper (Burbidge, Burbidge, Fowler, Hoyle, 1957) explained the origin of every element heavier than hydrogen except those made in the Big Bang. Stellar interiors are the universe's element factory. Iron is the factory's last product before the factory explodes
- Exclusions: Derivation of triple-alpha rate from nuclear cross sections; CNO cycle vs pp chain crossover temperature; s-process neutron capture; weak interaction rates in Si burning; neutron star equation of state
- Sim slug: astro-nucleosynthesis-binding-energy
- Score: 9/10

---

## Candidate 05 — Animate "Jeans Mass: Gravitational Collapse Threshold in a Molecular Cloud"
- Source: `physics-astronomy/chapters/08-birth-of-stars.md`
- Topic: Star Formation / Jeans Instability
- Lane: MANIM (directed animation)
- Hook: A cold, dense cloud collapses under gravity — but a warm, diffuse one does not. The boundary between stability and collapse is the Jeans mass. Watch M_J shift as temperature and density change, and watch the cloud decide its fate.
- The rule: Jeans mass M_J=C_J(kT/Gμm_H)^{3/2}ρ^{−1/2} where C_J≈(π/6)^{1/2}(5/2)^{3/2}; Jeans radius R_J≈√(15kT/4πGρμm_H); cloud collapses if M>M_J; free-fall time t_ff≈√(3π/32Gρ) ∝ ρ^{−1/2}
- Concrete numbers: Typical GMC: T=10 K, μ=2.3 (molecular H), n_H=10⁸ m⁻³: M_J≈2 M_Sun; warm diffuse ISM: T=100 K, n=10⁶ m⁻³: M_J≈100 M_Sun; cold dense core: T=10 K, n=10¹⁰ m⁻³: M_J≈0.2 M_Sun; free-fall time at n=10⁸ m⁻³: t_ff≈1 Myr
- The artifact / what moves: M_J vs density ρ (log-log) draws for T=10 K — declining line (M_J ∝ ρ^{−1/2}); a molecular cloud plotted as a point; as density increases (cloud contracts), point moves rightward along the x-axis, M_J curve falls — cloud stays above the curve (M>M_J, collapsing); a second panel shows T vs ρ with stable/unstable regions color-coded; temperature slider sweeps T from 10 K to 100 K — M_J curve shifts upward (warmer cloud needs more mass to collapse); collapse vs stable transitions labeled; free-fall time t_ff labels beside each density
- Output medium: Manim (mp4)
- Two testable predictions: P1: M_J ∝ T^{3/2}ρ^{−1/2} — at fixed ρ, doubling T increases M_J by 2^{3/2}=2.83×; a cloud just above M_J at T=10 K becomes stable (M<M_J) if heated to T=30 K; P2: t_ff ∝ ρ^{−1/2} — at n=10⁸ m⁻³, t_ff≈1 Myr; at n=10¹⁰ m⁻³, t_ff=0.1 Myr; ratio √100=10× as measured from ρ ratio
- The change: Add magnetic field support — show how B-field threading the cloud adds an effective pressure, raising the critical mass above M_J to the magnetic Jeans mass; the cloud must lose flux (ambipolar diffusion) before collapsing, adding a factor-of-several delay
- Human supplies (Claude can't): Nothing — fully synthetic/analytic; Jeans mass formula from virial theorem and energy balance
- Teardown angle: Molecular clouds are the nurseries of stars, and they spend most of their time NOT collapsing — turbulence and magnetic fields support them. When a region does collapse, it collapses fast: free-fall is merciless. The Jeans mass tells you which regions are doomed before they start
- Exclusions: Turbulent Jeans analysis; magnetic field reconnection and ambipolar diffusion; Bonnor-Ebert sphere profile; radiative cooling function; protostellar disk formation; binary star formation
- Sim slug: astro-jeans-mass-collapse
- Score: 9/10

---

## Candidate 06 — Animate "Spectral Line Doppler Shift: Radial Velocity from Wavelength Offset"
- Source: `physics-astronomy/chapters/03-radiation-and-spectra.md`
- Topic: Spectroscopy / Radial Velocity
- Lane: MANIM (directed animation)
- Hook: Astronomers measure the speed of stars, galaxies, and exoplanets without leaving Earth — by watching spectral lines shift. A line shifted 0.1 nm from its rest wavelength corresponds to a radial velocity of 46 km/s. Watch a spectrum scan from blue to red as a source recedes.
- The rule: Δλ/λ₀ = v_r/c (non-relativistic Doppler); v_r = c × (λ_obs − λ_rest)/λ_rest; recession: redshift (λ_obs > λ_rest); approach: blueshift; radial velocity method for exoplanets: stellar reflex velocity K = v_star ∝ (m_p/M_★)(2πa/P)^{1/2}
- Concrete numbers: Hα rest λ=656.3 nm; v_r=100 km/s → Δλ=0.219 nm → λ_obs=656.52 nm; Sun recession at 220 km/s → Δλ=0.481 nm; exoplanet hot Jupiter K≈100 m/s → Δλ=0.22 pm (detectable with HARPS); galaxy recession v=1000 km/s (Hubble flow) → Δλ=2.19 nm
- The artifact / what moves: Spectrum strip draws (400–700 nm with Fraunhofer line positions marked); Hα, Hβ, Na-D lines shown at rest; v_r slider sweeps from −500 km/s to +500 km/s; all lines shift simultaneously — toward blue for approach, toward red for recession; shift magnitude labeled in nm and km/s; a second panel shows stellar spectrum of 51 Peg oscillating at 4.2-day period (K=56 m/s) with tiny Hα shift drawn — amplitude barely visible but detectable; the exoplanet's orbital period reads directly from the velocity oscillation
- Output medium: Manim (mp4)
- Two testable predictions: P1: Hα at v_r=300 km/s shifts to λ=656.3×(1+300/c)=656.96 nm — a shift of 0.66 nm, checkable from the formula; P2: The radial velocity method for 51 Peg b (M_p=0.47 M_J, a=0.05 AU, P=4.23 days) gives K=56 m/s — matched by the Mayor & Queloz 1995 discovery measurement
- The change: Apply to galaxy spectra — show a galaxy spectrum with Ca K line at 396.8 nm (rest) shifted to 450 nm; infer recession velocity v=c(450−396.8)/396.8=40,000 km/s; this is z=0.134; connects Doppler to Hubble law cosmology
- Human supplies (Claude can't): Nothing — fully synthetic/analytic; Hα and other line positions from NIST atomic spectra database; 51 Peg b parameters from Mayor & Queloz 1995 (public)
- Teardown angle: The first exoplanet around a Sun-like star was discovered by watching the star wobble — not the planet move. The detection required measuring a wavelength shift of 0.22 picometers. That is 0.22 trillionths of a meter. Spectroscopy is the most productive instrument in astronomical history
- Exclusions: Thermal/pressure broadening vs Doppler broadening; interstellar absorption; spectrograph design; interferometry; VLBI proper motions; transverse Doppler effect (relativistic)
- Sim slug: astro-doppler-radial-velocity
- Score: 8/10

---

## Candidate 07 — Animate "Hayashi Tracks: Pre-Main-Sequence Descent on the HR Diagram"
- Source: `physics-astronomy/chapters/08-birth-of-stars.md`
- Topic: Star Formation / Pre-Main-Sequence Evolution
- Lane: MANIM (directed animation)
- Hook: A forming star begins as a cool, luminous, fully convective object — cooler than the Sun but far more luminous, because it is enormous. It contracts nearly vertically downward on the HR diagram over millions of years. Watch it fall.
- The rule: Hayashi track: fully convective protostars follow nearly vertical (constant T_eff) descent on log L vs log T diagram; T_eff≈3000–4000 K (ionization-determined); L decreases as R shrinks: L=4πR²σT_eff⁴; at base of Hayashi track, radiative core develops → star turns leftward onto ZAMS; timescale: Kelvin-Helmholtz t_KH = GM²/RL
- Concrete numbers: 1 M_Sun at onset of Hayashi track: L≈10 L_Sun, T_eff≈3800 K, R≈5 R_Sun; descends over t_KH≈10 Myr; arrives at ZAMS: L=0.7 L_Sun, T=5600 K, R=0.9 R_Sun; 0.3 M_Sun: entire PMS track stays on Hayashi track (fully convective throughout), arrives at MS as red dwarf; 3 M_Sun: short Hayashi phase, rapid leftward turn to ZAMS (t_KH≈0.3 Myr)
- The artifact / what moves: Log L vs log T HR diagram draws; ZAMS line drawn as reference; Hayashi track for 1 M_Sun begins high and right (large, cool) and animates downward nearly vertically — T barely changes, L drops steadily; at L≈1 L_Sun the track turns leftward onto ZAMS; simultaneously a 0.3 M_Sun track descends more slowly and arrives at ZAMS far to the right (M-dwarf); a 3 M_Sun track descends and turns quickly; all three tracks shown simultaneously with timing markers
- Output medium: Manim (mp4)
- Two testable predictions: P1: 1 M_Sun Kelvin-Helmholtz time t_KH = GM²/RL ≈ 10 Myr — consistent with age of T Tauri stars in star-forming regions (observed ages 1–10 Myr), the timescale during which protostars are still contracting; P2: During Hayashi descent, T_eff≈3800 K nearly constant for 1 M_Sun — observable as T Tauri stars clustering near 3800 K in young cluster color-magnitude diagrams
- The change: Overlay Lithium depletion boundary — low-mass stars deplete Li during convective Hayashi phase; the Li abundance in a young cluster gives a second age indicator independent of the Hayashi track position
- Human supplies (Claude can't): Nothing — fully synthetic/analytic; Hayashi track from stellar structure theory; t_KH from standard formula; pre-MS ages from published models
- Teardown angle: A forming star does not start cold and heat up — it starts too large and too luminous and contracts. Gravity is the power source, not nuclear fusion. The Sun spent 10 million years falling. Fusion only started when the core reached 15 million K
- Exclusions: Protostellar disk formation and angular momentum; T Tauri jets and outflows; Herbig Ae/Be stars (higher mass analog); deuterium burning phase; FU Orionis accretion burst events
- Sim slug: astro-hayashi-track
- Score: 8/10

---

## Candidate 08 — Animate "Transit Depth and Radial Velocity: Two Windows on the Same Planet"
- Source: `physics-astronomy/chapters/08-birth-of-stars.md`
- Topic: Exoplanet Detection / Transit + RV
- Lane: MANIM (directed animation)
- Hook: The same planet causes two completely different signals: a periodic brightness dip (transit) and a periodic Doppler wobble (radial velocity). Together they give you radius AND mass. Watch both signals generate from the same orbital geometry.
- The rule: Transit depth ΔF/F = (R_p/R_★)²; transit duration t_14 ≈ (R_★/πa)×P (for circular orbit, central transit); radial velocity semi-amplitude K = (2πG/P)^{1/3} × (M_p sin i)/(M_★+M_p)^{2/3} × 1/√(1−e²); bulk density ρ_p = M_p/(4πR_p³/3)
- Concrete numbers: Hot Jupiter (HD 209458 b): P=3.525 days, R_p=1.38 R_J=15% of R_★, ΔF/F=0.0226 (2.26% dip); K=85 m/s; M_p=0.69 M_J; ρ=0.36 g/cm³ (less dense than Saturn); transit duration 3 hr; TRAPPIST-1 b: R_p=1.09 R_Earth (ΔF/F=0.7%), K≈8 m/s
- The artifact / what moves: Left panel: orbital geometry top-down view — star centered, planet orbiting; transit ingress/egress labeled; right panel: light curve draws in real time as planet transits — flat baseline, symmetric dip, flat bottom (full transit), recovery; dip depth labeled as (R_p/R_★)²; third panel: radial velocity curve draws simultaneously — sinusoidal, period matching transit period, amplitude K; at transit midpoint, v_r crosses zero (planet moving perpendicular); the two panels kept synchronized to the same orbital phase; ratio K/ΔF/F gives mass-to-radius ratio without distance
- Output medium: Manim (mp4)
- Two testable predictions: P1: Transit depth ΔF/F=(R_p/R_★)² — for HD 209458 b (R_p=1.38 R_J, R_★=1.15 R_Sun): ΔF/F=(1.38×71,492/1.15×696,000)²=0.0226 (2.26%), matching observations; P2: K=85 m/s for HD 209458 b — from the RV semi-amplitude formula with M_p=0.69 M_J, a=0.047 AU, M_★=1.14 M_Sun, i≈87°; matches Mayor et al. discovery measurement
- The change: Show the effect of orbital inclination i — at i=90° (edge-on) transit occurs and K=K_true; at i=80° transit barely occurs (grazing), K_obs=K_true×sin(80°)=0.985 K_true; at i<88° (for this system) no transit but RV still gives M_p sin i (lower limit); illustrates why transit surveys are biased toward short-period planets (larger transit probability)
- Human supplies (Claude can't): Nothing — fully synthetic/analytic; HD 209458 system parameters from published exoplanet databases (NASA Exoplanet Archive, public)
- Teardown angle: The transit method gives you R_p. The radial velocity method gives you M_p sin i. Together they give you density. And density tells you whether you have a rock, a gas giant, or a water world. Two signals, one planet, full characterization — and you never left the ground
- Exclusions: Transmission spectroscopy; phase curve analysis; Rossiter-McLaughlin effect; TTVs (transit timing variations); ground-based photometric precision limits; Kepler/TESS mission design
- Sim slug: astro-transit-radial-velocity
- Score: 8/10

---

## Candidate 09 — Animate "Chandrasekhar Limit: White Dwarf Mass-Radius and the Relativistic Cliff"
- Source: `physics-astronomy/chapters/10-death-of-stars.md`
- Topic: White Dwarfs / Stellar Death
- Lane: MANIM (directed animation)
- Hook: Add mass to a white dwarf and it gets smaller — not bigger. Keep adding and the electron pressure goes relativistic, the curve bends toward zero radius, and at 1.44 solar masses there is no solution: the star cannot exist. Watch the cliff approach.
- The rule: Non-relativistic: R_WD ∝ M^{−1/3} (electron degeneracy, Pauli exclusion pressure); relativistic: pressure softens as v_e→c; Chandrasekhar limit M_Ch=5.87 μ_e^{−2} M_Sun ≈ 1.44 M_Sun (μ_e=2 for C/O WD); radius shrinks to zero at M_Ch; compact matter in this mass range must be a neutron star or black hole
- Concrete numbers: 0.5 M_Sun WD: R≈12,000 km (Earth-like); 1.0 M_Sun: R≈8,500 km; 1.3 M_Sun: R≈4,000 km; 1.44 M_Sun: R→0; Sirius B (1.02 M_Sun): observed R=5,840 km (HST); theoretical: R=√(1−M_Sib/M_Ch)^{1/3}×R₀ formula bending
- The artifact / what moves: M axis (0 to 1.5 M_Sun); two R(M) curves draw — non-relativistic (dashed, monotone M^{−1/3}) and full Chandrasekhar (solid, bending steeply downward); vertical dashed asymptote at M_Ch=1.44 M_Sun; Sirius B marked as a labeled dot; at M=1.0 M_Sun, non-relativistic and relativistic curves are close; above 1.2 M_Sun they diverge dramatically — the relativistic curve falls toward zero while the non-relativistic continues declining gradually; inset: at M→M_Ch, a neutron star appears at ~10 km radius and a separate dot for the Schwarzschild radius appears at ~4 km, marking the black hole limit
- Output medium: Manim (mp4)
- Two testable predictions: P1: Sirius B mass-radius consistency — M=1.02 M_Sun should give R=5,800 km; HST measurement gives 5,840±200 km; P2: The mass-radius product M^{1/3}×R = const (non-relativistic) — for Sirius B: (1.02)^{1/3}×5840≈5870, for a 0.5 M_Sun WD: (0.5)^{1/3}×12000≈9524; the product is NOT constant (deviates 62%), confirming relativistic corrections are needed above 0.5 M_Sun
- The change: Show Type Ia supernova trigger — a white dwarf accreting mass from a companion approaches M_Ch; the mass-radius curve shows the final approach to zero radius, then the thermonuclear runaway at the standard mass; explains why Type Ia are standard candles (same trigger mass, same peak luminosity)
- Human supplies (Claude can't): Nothing — fully synthetic/analytic; mass-radius relation from Chandrasekhar's polytrope formula; Sirius B data from HST (public)
- Teardown angle: Chandrasekhar's 1930 result proved there is a maximum mass for a dead star. For 10 years Eddington refused to believe it. The universe did not care: every white dwarf above 1.44 solar masses explodes. The Chandrasekhar limit is why we can measure the expansion of the universe — Type Ia supernovae all have the same intrinsic brightness because they all detonate at the same mass
- Exclusions: Derivation from relativistic Fermi gas pressure; Tolman-Oppenheimer-Volkoff equation for neutron stars; neutron star equation of state; quark matter; gravitational wave emission from WD-WD mergers
- Sim slug: astro-chandrasekhar-wd
- Score: 8/10

---

## Candidate 10 — Animate "Hubble Diagram: v=H₀d and the Expanding Universe"
- Source: `physics-astronomy/chapters/11-the-big-bang.md` (inferred from cosmology chapters)
- Topic: Cosmology / Hubble Law
- Lane: MANIM (directed animation)
- Hook: Every galaxy is receding from us — and the farther away it is, the faster it recedes. The slope of the velocity-distance graph is the age of the universe (roughly). Watch the Hubble diagram draw, galaxies appearing one by one, the best-fit line slope converging on 70 km/s/Mpc.
- The rule: Hubble law: v=H₀d; v measured from redshift z≈Δλ/λ; H₀=70 km/s/Mpc (current best); age of universe ≈ 1/H₀=14 Gyr (flat matter+Λ); distance from Cepheids, Type Ia, and surface brightness fluctuations
- Concrete numbers: Virgo cluster: d=16.5 Mpc, v=1150 km/s; Coma cluster: d=99 Mpc, v=6925 km/s; H₀=70 km/s/Mpc; Hubble time t_H=1/H₀=14.0 Gyr; Planck 2018: t_universe=13.8 Gyr; Hubble tension: local H₀≈73 vs CMB H₀≈67.4 km/s/Mpc
- The artifact / what moves: Distance d (x-axis, 0–500 Mpc) and recession velocity v (y-axis); galaxies appear one by one as colored dots — each labeled (Virgo, Coma, etc.); running best-fit line draws and updates slope as each point appears; slope converges toward H₀=70 km/s/Mpc; annotations: "slope = H₀ = 70 km/s/Mpc"; "y-intercept passes through origin (no preferred center)"; second panel: 1/H₀ = Hubble time = 14 Gyr, compared to age of oldest globular clusters (13.5 Gyr) — they barely fit; Hubble tension shown as two competing lines (local vs CMB)
- Output medium: Manim (mp4)
- Two testable predictions: P1: Virgo cluster at d=16.5 Mpc should have v=H₀×d=70×16.5=1155 km/s — observed v=1150 km/s (matches to 0.4%, within peculiar velocity noise); P2: Hubble time 1/H₀=14.0 Gyr must exceed age of oldest stars — globular cluster ages 11–13.5 Gyr, consistent if universe is 13.8 Gyr old; tension: if H₀=73, Hubble time=13.4 Gyr, barely consistent
- The change: Replace linear Hubble diagram with log distance — extend to z=1 (d≈4 Gpc, v≈c); show where the linear approximation breaks down; at high z, Type Ia supernovae reveal acceleration (the dots fall below the linear prediction), establishing dark energy
- Human supplies (Claude can't): Nothing for the animation — galaxy recession velocities and distance estimates from NED (NASA/IPAC Extragalactic Database, public); synthetic data sufficient for the illustration
- Teardown angle: Hubble's 1929 diagram had only 24 galaxies and distances that were off by a factor of 7. The slope implied the universe was 2 billion years old — less than the age of the Earth. The calibration took 50 more years to fix. The law was right; the numbers were wrong. Science fixed the numbers by looking harder
- Exclusions: Dark energy equation of state; CMB power spectrum derivation; inflationary cosmology; large-scale structure formation; Hubble tension statistical methods; ΛCDM fitting
- Sim slug: astro-hubble-diagram
- Score: 8/10

---

## Summary

| # | Title | Lane | Score | Slug |
|---|---|---|---|---|
| 01 | Planck Temperature Sweep + Wien Shift | MANIM | 9/10 | astro-planck-temperature-sweep |
| 02 | Mass-Luminosity + Main-Sequence Lifetime | MANIM | 9/10 | astro-mass-luminosity-lifetime |
| 03 | Stellar Evolution Track on HR Diagram | MANIM | 9/10 | astro-stellar-evolution-track |
| 04 | Nucleosynthesis Binding Energy + Fe Peak | MANIM | 9/10 | astro-nucleosynthesis-binding-energy |
| 05 | Jeans Mass Collapse Threshold | MANIM | 9/10 | astro-jeans-mass-collapse |
| 06 | Spectral Line Doppler Radial Velocity | MANIM | 8/10 | astro-doppler-radial-velocity |
| 07 | Hayashi Tracks Pre-MS Descent | MANIM | 8/10 | astro-hayashi-track |
| 08 | Transit Depth + Radial Velocity | MANIM | 8/10 | astro-transit-radial-velocity |
| 09 | Chandrasekhar Limit White Dwarf Curve | MANIM | 8/10 | astro-chandrasekhar-wd |
| 10 | Hubble Diagram Expanding Universe | MANIM | 8/10 | astro-hubble-diagram |

**Build-soon (≥9/10):** Candidates 01–05 (five cards). All are self-contained, fully synthetic, and animate astronomical results where the motion (shifting curve, climbing track, converging arrows) carries the argument.

**D3/DATAVIZ pass (future):** Interactive HR diagram with stellar parameter sliders; Monte Carlo star formation IMF sampler; exoplanet parameter space explorer (period vs radius vs mass scatter plot from Kepler data).
