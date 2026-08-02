# Chapter 34 — Frontiers of Physics

*We have explained almost everything we have ever measured, and we have measured less than 5% of the universe.*

---

![Strain h(t) waveform from a binary black hole merger (36 + 29 M_⊙). Frequency and amplitude rise into a chirp, peak at merger, ring down. Hanford and Livingston detectors observed coincident signals 7 ms apart, confirming GR's...](../images/34-frontiers-of-physics-fig-01.png)
*Figure 34.1 — LIGO GW150914 — First Direct Detection of Gravitational Waves (Sept 14, 2015)*

On September 14, 2015, at 5:51 AM Eastern time, both LIGO detectors — one in Hanford, Washington, and one in Livingston, Louisiana — recorded the same chirp. The signal swept upward in frequency over 0.2 seconds, peaked near 250 Hz, and died away. The two detectors are 3,000 km apart, and the signals arrived 7 milliseconds apart — exactly the light-travel time between the sites.

After three months of internal verification, LIGO announced the result: two black holes, about 30 and 35 solar masses, had spiraled together 1.3 billion light-years from Earth and merged into a single black hole of about 62 solar masses. The missing 3 solar masses were converted to gravitational-wave energy. In the last fraction of a second of the merger, the power radiated in gravitational waves briefly exceeded the combined electromagnetic luminosity of every star in the observable universe.

Einstein had predicted gravitational waves in 1916. The detection came 99 years later. It was the first direct confirmation that black holes — predicted by the equations of general relativity — exist as described. It opened a new window on the universe. And it is a fitting place to begin the final chapter of this book, because it represents everything physics has accomplished at its best: a precise prediction from a deep theory, confirmed by an experiment of almost inconceivable delicacy, a century later.

What comes after this chapter is the inventory of what physics does not yet understand.

---

## The universe, from the beginning

The modern picture of cosmology rests on three independent pieces of evidence, each pointing to the same conclusion.

**The expansion.** Edwin Hubble, in 1929, plotted the recession velocities of 24 galaxies against their distances and found a linear relationship:

$$v = H_0 d,$$

![Top: Hubble diagram showing recession velocity vs distance for galaxies, linear with slope H₀ ≈ 70 km/s/Mpc. Bottom: timeline from Big Bang (t=0) through inflation, CMB at 380,000 yr, reionization, galaxy formation, dark...](../images/34-frontiers-of-physics-fig-02.png)
*Figure 34.2 — Hubble Expansion and 13.8 Gyr Cosmic Timeline*

where $H_0 \approx 70$ km/s/Mpc is Hubble's constant. More distant galaxies recede faster. The universe is expanding — not galaxies flying through pre-existing space, but space itself stretching, carrying galaxies along. Run the expansion backward: about 13.8 billion years ago, all the matter in the universe was concentrated in an extremely hot, dense state. That is the Big Bang.

**The cosmic microwave background.** In 1964, Arno Penzias and Robert Wilson, adjusting a microwave antenna at Bell Labs, detected a faint hiss coming equally from every direction in the sky, at a temperature of 2.73 K. It was the cooled remnant of light released about 380,000 years after the Big Bang, when the universe finally cooled enough for electrons and protons to combine into neutral hydrogen atoms — and the universe, until then opaque to photons, suddenly became transparent. The photons released at that moment have been traveling freely ever since, stretched by the expansion to microwave wavelengths. The Planck satellite mapped them to extraordinary precision in 2009. The tiny temperature fluctuations ($\delta T / T \sim 10^{-5}$) in the CMB are the seeds from which every galaxy in the universe later grew under gravity.

**Light-element abundances.** In the first few minutes after the Big Bang, when temperatures were still nuclear ($\sim 10^9$ K), protons and neutrons fused into the lightest nuclei: hydrogen, helium-4, helium-3, deuterium, and trace lithium-7. The fractions are calculable from the known physics of Chapter 31. The observed abundances match the predictions. This is direct empirical confirmation that the universe was once at nuclear temperatures, and that the physics of those first minutes is ordinary nuclear physics — nothing exotic required.

These three independent measurements of the same event, agreeing quantitatively, constitute the evidence for the Big Bang. The age of the universe from the Planck satellite data: $13.80 \pm 0.02$ billion years. The oldest known stars in the Milky Way are about 13 billion years old. A star older than the universe would be a fatal problem; none has been found.

The Hubble time — the naive estimate $1/H_0$ — gives:

$$t_H = \frac{1}{H_0} = \frac{1}{2.27 \times 10^{-18} \text{ s}^{-1}} \approx 4.4 \times 10^{17} \text{ s} \approx 14 \text{ billion years}.$$

The actual age is slightly less because the expansion rate was different in the past, but the agreement to within 10% from this back-of-envelope estimate is encouraging.

<!-- → [INFOGRAPHIC: Timeline of the universe — horizontal axis from t=0 to t=13.8 Gyr; key events marked: Planck era (t < 10⁻⁴³ s, physics unknown), inflation (10⁻³⁶–10⁻³² s), quark-hadron transition (10⁻⁶ s), Big Bang nucleosynthesis (first 3 min), recombination/CMB release (380,000 yr), first stars (~100–200 Myr), Milky Way formation (~600 Myr), solar system formation (9.2 Gyr), present (13.8 Gyr); caption: the standard cosmological model is well-confirmed from about 10⁻³² seconds onward; before that, current physics breaks down and we have only speculation] -->

---

## Gravity as geometry

Newton described gravity as a force. Einstein, in 1916, described it as the curvature of spacetime.

The starting point is the **equivalence principle**: a person inside a freely falling elevator cannot distinguish, by any local experiment, whether they are in free fall in a gravitational field or floating in empty space far from any mass. Gravity and inertia are the same thing, locally. This means gravity must affect everything that inertia affects — including light. A horizontal beam of light in a gravitational field must bend downward, because from the perspective of a freely falling observer, the beam goes straight, but the room is accelerating up to meet it.

From this principle, Einstein derived that mass and energy curve the four-dimensional fabric of spacetime, and particles (including photons) follow the straightest possible paths through this curved geometry. What looks to us like gravitational attraction is just objects following straight lines through curved spacetime.

The field equations of general relativity — ten nonlinear partial differential equations — make specific, testable predictions. Every one confirmed:

**Mercury's perihelion.** Mercury's elliptical orbit rotates by 43 arcseconds per century more than Newtonian gravity predicts. GR accounts for this exactly. (This was actually a known anomaly before Einstein, not a prediction — GR explained it retroactively, which is less satisfying than predicting it in advance, but still counts.)

**Gravitational lensing.** Light passing near the Sun bends by 1.75 arcseconds for rays grazing the solar limb — twice the Newtonian prediction for a massless particle. Confirmed by Eddington's 1919 eclipse expedition.

**Gravitational redshift.** Clocks deeper in a gravitational well run slower. Confirmed at extraordinary precision; required for GPS to function (about 45 μs/day faster for the satellite clocks' gravitational contribution — compared to the special-relativistic effect of 7 μs/day slower from their orbital velocity, for a net +38 μs/day correction).

**Gravitational waves.** Accelerating masses radiate ripples in spacetime at the speed of light. Confirmed by LIGO in 2015.

**Black holes.** Solutions to Einstein's equations include regions so curved that nothing — not even light — can escape. The *Schwarzschild radius* of a non-rotating black hole of mass $M$ is

$$r_s = \frac{2GM}{c^2}.$$

For a solar-mass black hole: $r_s \approx 3$ km. The Event Horizon Telescope imaged the shadow of the supermassive black hole in the galaxy M87 in 2019 — a $6.5 \times 10^9$ solar-mass object with a Schwarzschild radius of about 20 billion km, resolved at 1.3 mm wavelength from Earth. The image matched GR predictions.

General relativity is one of the most precisely tested physical theories ever constructed. In every domain where its predictions can be checked, it has been confirmed.

<!-- → [TABLE: Tests of general relativity — columns: prediction, type (retroactive/predictive), experiment/observation, result; rows: Mercury perihelion precession (retroactive, solar-system timing, 43"/century confirmed), light bending (predictive, Eddington 1919 eclipse, 1.75" confirmed), gravitational redshift (predictive, Pound-Rebka 1959 + GPS, confirmed to 10⁻⁴), time delay (predictive, Shapiro delay, confirmed to 10⁻³), gravitational waves (predictive, LIGO 2015, confirmed), black hole shadow (predictive, Event Horizon Telescope 2019, confirmed); caption: every prediction of general relativity that has been testable has been confirmed; the theory is correct wherever it applies] -->

---

## What we cannot see

Now comes the honesty part.

![Plot of orbital velocity vs distance from galactic center. Newtonian prediction from visible mass: v falls as 1/√r at large r. Observed: v stays flat (~200 km/s) far beyond visible matter. Inferred mass = dark matter halo...](../images/34-frontiers-of-physics-fig-04.png)
*Figure 34.4 — Galactic Rotation Curves — Flat Beyond the Visible, Why Dark Matter*

In the 1970s, Vera Rubin measured the rotation curves of spiral galaxies — how fast stars orbit the galactic center as a function of distance from it. From Newtonian gravity, the rotational velocity should decrease with distance once you're outside the visible mass distribution, just as the orbital speeds of the planets decrease with distance from the Sun. What Rubin found was the opposite: the velocity curves were *flat*. Stars far from the center orbit just as fast as stars close in, even far beyond where the visible mass runs out.

For a flat rotation curve, the enclosed mass must grow linearly with radius: $M(r) = v^2 r / G$. There is more mass there than the visible stars and gas can account for — much more, in an extended halo around and beyond the visible galaxy. For a typical galaxy like the Milky Way with $v \approx 220$ km/s and $r \approx 50$ kpc:

$$M \approx \frac{(2.2 \times 10^5)^2 (1.5 \times 10^{21})}{6.67 \times 10^{-11}} \approx 10^{42} \text{ kg} \approx 5 \times 10^{11} M_\odot.$$

The visible stars and gas account for perhaps $10^{11} M_\odot$. The dynamically inferred mass is five times larger.

![Two panels. Left: Bullet Cluster — two galaxy clusters collided; hot gas (X-ray) lags between, but gravitational lensing (mass) stays with the galaxies. Direct evidence of dark matter as collisionless. Right: EHT shadow image...](../images/34-frontiers-of-physics-fig-05.png)
*Figure 34.5 — Bullet Cluster + Sgr A* — Two Smoking Guns for Dark Matter and Black Holes*

The same conclusion comes from galaxy clusters (Zwicky had noticed the discrepancy in 1933, ignored for decades), gravitational lensing by clusters, and the structure of the CMB itself. About 85% of all matter in the universe is *dark matter* — matter that gravitates but does not emit, absorb, or scatter electromagnetic radiation. We know it's there. We do not know what it is.

![Pie chart of present-epoch cosmic composition from Planck satellite data. Stars, gas, planets (baryons) 5%. Dark matter 27%, gravitates but doesn't shine. Dark energy 68%, the cosmological constant accelerating the expansion.](../images/34-frontiers-of-physics-fig-03.png)
*Figure 34.3 — Universe Composition — 5% Atoms, 27% Dark Matter, 68% Dark Energy*

In 1998, two teams independently studying Type Ia supernovae at high redshift found them fainter — and therefore farther away — than expected for a universe whose expansion is slowing down under gravity. The universe's expansion is *accelerating*. Something must be driving this acceleration: *dark energy*, a component of unknown nature that constitutes about 68% of the universe's total mass-energy and acts as a repulsive contribution to the expansion. The simplest model is a cosmological constant $\Lambda$ — a constant energy density of the vacuum — and it fits the data well.

Add them up. The current universe contains:

- 5% ordinary matter (everything you can see — all stars, gas, dust, planets, atoms).
- 27% dark matter.
- 68% dark energy.

We understand 5% of the universe's contents directly. The other 95% is identified by its gravitational effects and is otherwise uncharacterized. This is not a minor footnote to the success of physics. It is the central problem of 21st-century cosmology.

<!-- → [CHART: Galaxy rotation curve — x-axis: distance from galactic center in kpc (0 to 50); y-axis: orbital velocity in km/s (0 to 300); two curves: "expected from visible mass" (rises then falls as Keplerian r^{-1/2} beyond the visible disk, dropping to ~100 km/s at 30 kpc), "observed" (flat at ~220 km/s to the edge of the plot); shaded region between curves labeled "dark matter contribution — mass that must be present but cannot be seen"; caption: this is Vera Rubin's result, repeated for hundreds of galaxies — the discrepancy is not noise, it is a feature of every galaxy surveyed] -->

<!-- → [INFOGRAPHIC: Pie chart of universe composition — three slices: ordinary matter (5%, labeled "atoms, stars, gas — everything Standard Model"), dark matter (27%, labeled "gravitates, unknown identity"), dark energy (68%, labeled "drives accelerated expansion, unknown nature"); caption: the two successful theories of modern physics — the Standard Model and general relativity — directly account for only the white slice; the remaining 95% is characterized by what it does, not what it is] -->

---

## What we do not understand

The list is long. Here is the honest catalog of major open questions, as of 2026.

**Dark matter identity.** The candidates include weakly interacting massive particles (WIMPs, motivated by supersymmetry), axions (originally proposed to solve a problem in QCD), sterile neutrinos, and primordial black holes. Direct-detection experiments — kilometer-scale liquid-xenon detectors, like LUX-ZEPLIN and XENONnT — have found no signal, excluding large swaths of WIMP parameter space. The honest status: we know dark matter exists; we do not know what it is; the most popular candidate class (WIMPs) has been significantly constrained.

**Dark energy.** The cosmological constant $\Lambda$ fits the data, but the value of $\Lambda$ is $\sim 10^{-120}$ times what quantum field theory naively predicts for the vacuum energy. This is the *cosmological constant problem* — the worst quantitative discrepancy between theory and observation in the history of physics. Either our understanding of quantum vacuum energy is deeply wrong, or a yet-unknown mechanism selects the observed tiny value. Nobody knows.

**Quantum gravity.** General relativity and quantum mechanics are both extraordinarily successful, and they are incompatible. GR is a classical field theory of spacetime; quantum mechanics requires quantizing fields. When you try to quantize gravity in the straightforward way, you get infinities that cannot be renormalized away. At the Planck scale ($\ell_P = \sqrt{\hbar G/c^3} \approx 10^{-35}$ m, $t_P \approx 10^{-43}$ s), both theories apply and neither is adequate. No theory of quantum gravity has yet made a testable prediction that differs from GR + Standard Model at any energy scale accessible to experiment.

The two leading candidates are string theory (fundamental particles as 1D vibrations of strings in 10 or 11 dimensions) and loop quantum gravity (spacetime itself quantized into discrete "spin networks" at the Planck scale). Both have produced rich mathematics. Neither has produced a confirmed observational consequence that distinguishes it from existing theories.

**Matter-antimatter asymmetry.** The Big Bang should have produced equal amounts of matter and antimatter, which would have annihilated completely, leaving only photons. Instead, there is matter — enough to build $10^{80}$ atoms. The Standard Model contains CP violation (different behavior of matter and antimatter under combined charge-conjugation and parity transformation), but not enough to explain the observed asymmetry. Some new source of CP violation is required; what it is, we don't know.

**Neutrino masses.** The original Standard Model predicted massless neutrinos. They are not massless — neutrino oscillation experiments (Super-K 1998, SNO 2001) confirmed this. The mechanism for neutrino mass is unclear and is not included in the minimal Standard Model.

**The hierarchy problem.** The electroweak scale ($\sim 100$ GeV) and the gravitational (Planck) scale ($\sim 10^{19}$ GeV) differ by 17 orders of magnitude. Quantum corrections to the Higgs mass should drive it up to the Planck scale unless there is extraordinary fine-tuning — 30 orders of magnitude of cancellation between terms. Why the Higgs mass sits at 125 GeV/$c^2$ rather than $10^{19}$ GeV/$c^2$ is unexplained.

**The 19 free parameters.** The Standard Model takes about 19 numbers as input — quark and lepton masses, coupling constants, mixing angles — fitted to experiment. It explains none of them from first principles. Why these numbers? Why three generations of quarks and leptons? Why not two, or seven? The Standard Model accommodates three; it does not predict three.

---

## What we do understand

Before the list of open questions leaves the wrong impression: the picture of what we *do* understand is extraordinary.

We can compute the magnetic moment of the electron to 12 significant figures, and measure it to 12 significant figures, and they agree. We can predict the mass of the top quark from theory and measure it to a fraction of a percent. We can predict the abundance of helium-4 from Big Bang nucleosynthesis to better than 1% and measure it to better than 1% and they agree. We can predict the gravitational-wave signal from a binary black-hole merger — the waveform, the frequency evolution, the final mass and spin — compute it from numerical relativity, and have it match the observation with no free parameters. We understand the structure of matter down to $10^{-18}$ m (the reach of the LHC). We understand the history of the universe back to $10^{-32}$ s. We understand why the Sun shines, why stars explode, where the elements come from.

![Two-column comparison. "Settled": Standard Model (matter particles + electromagnetic, weak, strong forces), General Relativity (gravity), thermodynamics, QM, EM. "Open": dark matter, dark energy, quantum gravity,...](../images/34-frontiers-of-physics-fig-06.png)
*Figure 34.6 — The Honest Map — What Physics Has Settled vs the Open Problems*

The Standard Model of particle physics, for all its 19 free parameters and its failure to include gravity, is the most precisely tested physical theory in human history. General relativity, tested from millimeter scales to billion-light-year scales, has passed every test. Both are clearly incomplete — the dark matter and dark energy problems alone guarantee this. But the 5% of the universe we can see and interact with, we understand in extraordinary detail.

This is the correct picture: not "physics has explained everything" (it hasn't), and not "physics is mostly wrong" (it isn't). The picture is complete within a well-understood domain, and clearly limited outside it.

<!-- → [TABLE: What physics knows vs. what it doesn't — columns: domain, status, precision, representative example; rows: quantum electrodynamics (complete, 12 significant figures, electron magnetic moment), Standard Model particles and forces (complete except gravity, <1% for most predictions, Higgs mass), general relativity at classical scales (complete, sub-percent, gravitational wave waveforms), Big Bang cosmology from 10⁻³² s onward (well-confirmed, several-percent, CMB power spectrum), dark matter identity (unknown, N/A, no confirmed detection), dark energy mechanism (unknown, N/A, Λ fits data but not explained), quantum gravity (no theory, N/A, Planck scale inaccessible); caption: physics is not uniformly confident or uniformly ignorant — it is precisely calibrated about what it knows and where it stops] -->

---

## The honest frontier

Feynman gave a 1955 address — "The Value of Science" — in which he said that the scientist has a special responsibility to live with doubt: "It is our responsibility as scientists... to teach how doubt is not to be feared but welcomed and discussed; and to demand this freedom as our duty to all coming generations."

This chapter is the enactment of that duty.

We know the universe is expanding, and we don't know why the expansion is accelerating. We know dark matter is there, and we don't know what it is. We know quantum mechanics and general relativity must both be right (they've each been tested to extraordinary precision), and we know they cannot both be exactly right (they're incompatible at extreme conditions). We know the Standard Model is the correct theory of everything except gravity, and we know it's incomplete. We know the universe is 13.8 billion years old, and we don't know what happened before $10^{-43}$ seconds.

This is not a failure of physics. This is physics operating correctly — pushing against the boundary of what observation can currently test, being precise about what it knows and honest about what it doesn't. A century ago, the boundary was quantum mechanics and the nuclear force. Before that, it was electromagnetism. The boundary keeps moving.

The questions that remain are genuinely hard. The cosmological constant problem may be the hardest quantitative question in all of science — a $10^{120}$ discrepancy is not something you resolve with a small correction. The quantum gravity problem requires unifying the two most successful theories ever constructed, which currently resist unification. These may require conceptual revolutions as large as those of 1905 and 1925.

They may also be answerable. Physics has a long record of answering questions that seemed permanently intractable.

<!-- → [TABLE: Open questions in physics — columns: question, what we know, what we don't know, experimental approach; rows: dark matter identity (exists — 5 independent lines of evidence, identity unknown, direct detection / LHC / astrophysical), dark energy / cosmological constant (accelerated expansion confirmed / Λ fits data, why Λ is 10⁻¹²⁰ × expected, future surveys DESI/Euclid/Rubin), quantum gravity (both QM and GR are right, how to unify them, Planck-scale experiments / gravitational wave astronomy), matter-antimatter asymmetry (asymmetry exists / SM has insufficient CP violation, source of extra CP violation, Belle II / LHCb), neutrino masses (masses nonzero from oscillations, mechanism for mass / absolute mass scale, KATRIN / cosmological bounds); caption: these are the five most pressing open questions in fundamental physics as of 2026; all have experimental programs directed at them; none has a confirmed answer] -->

---

## Three commitments

**The universe has a history.** The Big Bang model is confirmed by three independent lines of evidence. The universe is 13.8 billion years old, began in a hot dense state, and has been expanding and cooling ever since. We understand this history in detail back to about $10^{-32}$ s.

**Gravity is spacetime curvature.** General relativity has passed every test for over a century. Black holes, gravitational waves, light bending, gravitational time dilation — all confirmed. The Schwarzschild radius $r_s = 2GM/c^2$ describes the point of no return for a black hole of mass $M$.

**95% of the universe is unaccounted for.** Dark matter (27%) and dark energy (68%) are confirmed by multiple independent observations and are unexplained by any current theory. The Standard Model and general relativity together, despite their extraordinary success, describe only ordinary matter.

The single deepest fact: **we know an enormous amount, and we know how much we don't know.** That combination — knowledge plus calibrated uncertainty — is what physics actually looks like at its frontier. It is also the most useful cognitive habit you can take from this book.

---

## Exercises

### Warm-up

**34.1** *(Hubble expansion)* State Hubble's law in one sentence. Explain what it means physically that more distant galaxies recede faster — is this evidence that we are at the center of the universe?

**34.2** *(Schwarzschild radius)* Compute the Schwarzschild radius of (a) the Sun ($M_\odot = 2.0 \times 10^{30}$ kg), (b) Earth ($M_\oplus = 6.0 \times 10^{24}$ kg), (c) a 10-solar-mass stellar black hole. Express in meters and compare to the object's actual radius.

**34.3** *(Hubble time)* Compute the Hubble time $t_H = 1/H_0$ for $H_0 = 70$ km/s/Mpc, where 1 Mpc = $3.086 \times 10^{22}$ m. Compare to the measured age of the universe (13.8 Gyr). Why are they close but not equal?

**34.4** *(Dark matter evidence)* Name three independent observational lines of evidence for the existence of dark matter. For each, state what would be different if dark matter did not exist.

**34.5** *(Open questions)* List five major open questions in fundamental physics as of 2026. For each, state in one sentence what we know and in one sentence what we don't.

### Application

**34.6** *(Galactic rotation curve)* A galaxy has a flat rotation curve at $v = 230$ km/s out to $r = 40$ kpc ($1 \text{ kpc} = 3.086 \times 10^{19}$ m). (a) Compute the enclosed mass $M(r) = v^2 r/G$. (b) Express in solar masses. (c) The visible mass of the galaxy is estimated at $8 \times 10^{10} M_\odot$. What fraction of the enclosed mass is dark matter?

**34.7** *(CMB temperature and redshift)* The CMB was emitted at recombination when the universe's temperature was about 3,000 K. Today it is 2.73 K. Compute the redshift factor $z + 1 = T_\text{emit}/T_\text{now}$. The universe has expanded by this factor since recombination — express this as a linear size ratio.

**34.8** *(Gravitational wave energy)* In the GW150914 event, about 3 solar masses were converted to gravitational-wave energy. (a) Compute this energy in joules ($M_\odot c^2 \approx 1.8 \times 10^{47}$ J). (b) The signal lasted about 0.2 s. Estimate the peak power and compare to the total electromagnetic luminosity of the observable universe ($\sim 10^{49}$ W).

**34.9** *(LIGO sensitivity)* LIGO's 4-km arms detected a strain of $\sim 10^{-21}$ from GW150914. Compute the corresponding length change $\Delta L = h \cdot L$. Compare this to (a) the diameter of a proton ($\sim 10^{-15}$ m), (b) the diameter of a hydrogen atom ($\sim 10^{-10}$ m).

### Synthesis

**34.10** *(The cosmological constant problem)* Naive quantum field theory estimates the vacuum energy density at $\rho_\text{QFT} \sim (E_\text{Planck})^4 / (\hbar c)^3 \approx 10^{113}$ J/m³. The observed dark energy density is $\rho_\Lambda \approx 10^{-9}$ J/m³. (a) Compute the ratio $\rho_\text{QFT}/\rho_\Lambda$. (b) Why is this called "the worst quantitative discrepancy in physics"? (c) What are the two main classes of proposed resolution?

**34.11** *(Big Bang nucleosynthesis as a test)* Big Bang nucleosynthesis predicts that about 25% of ordinary matter (by mass) emerged from the Big Bang as helium-4, with the remainder mostly hydrogen. The observed helium mass fraction in the oldest stars and gas clouds is about 24–25%. (a) Explain why this agreement constitutes a test of the Big Bang model. (b) What would the helium fraction be if the Big Bang temperature had been significantly lower? (c) Why can't stars account for all the helium we observe?

**34.12** *(Calibrated confidence)* The chapter argues the correct stance is neither "physics has explained everything" nor "physics is mostly wrong." For each of the following claims, state whether you would characterize it as well-established, actively investigated but uncertain, or speculative, and briefly justify your answer: (a) the universe began in a hot dense state 13.8 billion years ago; (b) dark matter is made of WIMPs; (c) string theory is the correct theory of quantum gravity; (d) general relativity correctly describes gravity at the scale of the solar system; (e) the universe is finite in extent.

### Challenge

**34.13** *(The Eddington 1919 measurement)* The deflection of light by the Sun was the critical test of general relativity in 1919. GR predicts a deflection of 1.75 arcseconds for light grazing the solar limb; Newtonian gravity (treating photons as massive particles) predicts 0.87 arcseconds — exactly half. (a) The 1919 measurement had uncertainties of order 0.3 arcseconds. Was Eddington's measurement precise enough to definitively distinguish the two predictions? (b) Look up (with a source you can verify) the current best measurement of solar light deflection and its precision. Has it confirmed GR to better than 1%? (c) Why was this measurement such a cultural event in 1919, beyond its scientific content?

**34.14** *(Gravitational waves as a probe of the early universe)* Inflation, if it occurred, should have produced a stochastic background of gravitational waves from quantum fluctuations in the early universe — the "primordial gravitational wave background." This would appear as a specific pattern of polarization in the CMB ("B-mode polarization"). (a) Why would detecting this background constitute direct evidence for inflation? (b) What experiment (currently operating or recently operating) is searching for this signal? (c) The BICEP2 team announced a detection in 2014, which was later shown to be primarily foreground dust emission. What does this episode illustrate about the scientific process?

---

## Still puzzling

The cosmological constant problem. Quantum field theory predicts that the vacuum — empty space — has an energy density from the zero-point fluctuations of all quantum fields. Compute this naively and you get something $\sim 10^{120}$ times the observed dark-energy density. No other discrepancy in physics is remotely this large. Either there is a mechanism that cancels the vacuum energy to extraordinary precision (and nobody has found one that works), or our understanding of quantum vacuum energy is fundamentally wrong (which would be a revolution in physics), or some anthropic selection mechanism operates (which troubles many physicists on philosophical grounds). The resolution of this problem — if it comes — will be one of the most consequential events in the history of science.

---

## LLM Exercise — Chapter 34: Frontiers in Your Anchor Phenomenon

**Project:** Physics Reality Check Logbook
**What you're building this chapter:** A Logbook entry connecting your phenomenon to the frontiers of physics — and reflecting on how 34 chapters of physics together account for (or fail to account for) your phenomenon. This is also the final entry in the Logbook.
**Tool:** Claude Project.

### The Prompt

```
I'm writing the final entry of my Physics Reality Check Logbook for College Physics with LLMs. My anchor phenomenon is [paste your 1-sentence description].

For Chapter 34 (the final chapter), I want to:

1. Identify ONE frontier-physics aspect of my phenomenon. Examples: for a bike commute — the GPS uses general-relativistic corrections, the dark matter all around me passing through my body undetected (~10⁹ WIMPs/cm²/s if WIMPs exist), the cosmic-ray muons that include occasional ultra-high-energy events from outside our galaxy. For a coffee maker — the underlying particle inventory of every atom includes Standard Model particles, and someday a unified theory may explain why coffee atoms have the masses they do. For a basketball shot — the atoms in my body and in the ball trace ultimately to nucleosynthesis in stars (Carl Sagan: "we are made of star stuff"). For a marathon — see above on cosmic rays and dark matter.

2. Reflect on the Logbook itself. Across all 34 chapters, what physics best explained my phenomenon? Where did the physics fall short? What surprised me most?

3. Identify three frontier questions in physics that, if answered, might illuminate my phenomenon further (or might not — many are unrelated to everyday phenomena).

4. Write a closing reflection: what does it mean to live in a world where ~95% of the universe's mass-energy is unaccounted for, but where the 5% we understand is enough to build everything we use?

5. Save the output as logbook/chapter-34-frontiers.md AND consider compiling all 34 entries into a single index.

This is my final Logbook entry. Make it thoughtful.
```

### What this produces

A reflective final entry that closes out the Logbook project and reflects on the year's-worth of physics applied to your one chosen phenomenon.

### How to adapt this prompt

- *For ChatGPT/Gemini:* Identical with interface substitutions.
- *For Claude Code:* Use it to compile the 34 entries into a single browsable document with table of contents.

### Connection to previous chapters

Reflects on all 34 chapters. The Logbook is now complete.

### Preview of next chapter

There is no next chapter. This is the end of the textbook. What comes next is your physics-informed engagement with the world — the discipline you've installed in 34 chapters of practice.

---

## Connections forward

There is no next chapter. The book ends here. What comes next is your own continued engagement with physics — through reading, through experiment, through honest skepticism about what is settled and what is not. The discipline of a physicist is not in the equations memorized but in the habits installed: caring about what units mean, caring about what uncertainties are, asking what assumptions the answer rests on, refusing to over-claim. If 34 chapters of practice have installed those habits, the book has done its job.

Welcome to the open frontier. Keep asking.

---

**Tags:** frontiers-of-physics, cosmology, general-relativity, dark-matter, quantum-gravity, Feynman-style
