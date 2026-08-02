# Chapter 8 — The Birth of Stars

*A spectrograph in Haute-Provence, October 1995, and a Jupiter-mass planet on a four-day orbit that should not have existed.*

---

## Suggested titles

1. The Birth of Stars
2. How Cold Gas Decides to Collapse
3. Reading the Galaxy's Nurseries

## TL;DR

A star forms when a parcel of cold molecular gas exceeds a single critical mass — the Jeans mass — above which self-gravity overwhelms thermal pressure and the cloud collapses faster than it can hold itself up. The same disk left over from that collapse builds planets, and the same Doppler trick used to identify Fraunhofer's lines (Chapter 3) is what reveals those planets pulling on their stars.

---

## Learning objectives

By the end of this chapter you will be able to:

1. **(Understand)** State the Jeans criterion in words — pressure versus gravity in a cold cloud — and explain why molecular clouds, not diffuse hydrogen, are where stars form.
2. **(Apply)** Compute the Jeans mass $M_J \propto T^{3/2}/\rho^{1/2}$ for a typical molecular cloud core and estimate the free-fall collapse time.
3. **(Understand)** Trace a protostar's path from infalling cloud core through Hayashi-track contraction to the main sequence, and name the energy source at each stage.
4. **(Apply)** Use the non-relativistic Doppler formula and Newton's third law to compute the radial-velocity wobble a planet imposes on its star.
5. **(Analyze)** Compare the radial-velocity, transit, and direct-imaging methods by the selection effects each one imposes on the exoplanet population it discovers.

**Prerequisites.** Chapter 3 (light, Doppler shifts, spectral lines). Chapter 4 (orbital mechanics, Kepler's third law). Chapter 5 (the Sun as a main-sequence star). Newton's third law. Algebra; willingness to compare two terms in an inequality.

---

## Opening case: 51 Pegasi, Haute-Provence, October 1995

On the night of October 6, 1995, Michel Mayor and Didier Queloz pointed the ELODIE spectrograph at the Observatoire de Haute-Provence toward 51 Pegasi — a perfectly ordinary G-type star, naked-eye visible, about 50 light-years away in the constellation Pegasus. They were looking for the Doppler wobble that any orbiting companion would impose. They had been looking, on and off, for years.

The spectral lines of 51 Pegasi moved. Toward Earth, then away from Earth, then toward Earth again, in a smooth sinusoid with a period of 4.231 days and an amplitude of about 56 meters per second — the speed of a fastball ([Mayor & Queloz, *Nature* 1995](https://www.nature.com/articles/378355a0)).

By Newton's third law, if the star was being pulled, something was pulling. Mayor and Queloz did the arithmetic. The only way to produce that wobble at that period was a planet of at least half Jupiter's mass, orbiting at roughly 0.05 astronomical units — one-eighth of Mercury's distance from the Sun. A gas giant on a four-day orbit. Surface temperature on the day side: somewhere north of 1,000 K.

The problem was that gas giants are not supposed to form there. The standard picture, built from our own solar system, said gas giants form past the *ice line* — far enough from the star that water condenses to solid grains that help build a heavy rocky core that then sweeps up hydrogen. Four days from a Sun-like star is far inside the ice line. There is not enough solid material, and the temperature is wrong. 51 Pegasi b should not exist.

It existed anyway. The discovery did not just add one planet to the catalog. It demolished a framework that had quietly assumed our solar system was typical, and forced astronomers to start over with a more honest question: *what does the actual exoplanet population look like, and what does it tell us about how stars and planets form together?*

This chapter is about the machinery that builds stars in the first place, and the techniques that let us see what gets built around them.

---

## Core concept

### Gravitational collapse and the Jeans instability

There is a puzzle right at the start. The galaxy contains roughly $10^{10}$ solar masses of cold gas — mostly molecular hydrogen, $\mathrm{H}_2$, at temperatures of 10 to 30 K in dense regions called **giant molecular clouds** ([Heyer & Dame 2015](https://www.annualreviews.org/doi/10.1146/annurev-astro-082214-122324)). The clouds have been there for billions of years. If gravity simply pulled gas together, they should have collapsed into stars by now. They have not. Star formation in the Milky Way proceeds at about one solar mass per year — slow enough that the galaxy's gas reservoir lasts ten billion years longer.

Something resists gravity. The "something" is pressure. Thermal pressure of the gas, plus turbulence in its bulk motion, plus magnetic fields threading the cloud. All three push outward; gravity pulls inward. A cloud collapses only where gravity wins.

In 1902, [James Jeans](https://royalsocietypublishing.org/doi/10.1098/rsta.1902.0012) worked out the exact balance for thermal pressure alone. Take a uniform sphere of cold gas, mass $M$, radius $R$, mean molecular mass $\mu m_H$ (where $m_H$ is the hydrogen mass), temperature $T$. Compress it slightly and ask which side wins.

Gravitational potential energy, by sign convention, becomes more negative as the cloud contracts:

$$U_{\text{grav}} \sim -\frac{GM^2}{R}$$

Thermal energy stays roughly the same — the number of particles is fixed and we will treat the temperature as held constant by efficient radiative cooling (this is the *isothermal* limit, and it is a good approximation for cold dust-rich gas):

$$U_{\text{therm}} \sim N k_B T \sim \frac{M}{\mu m_H} k_B T$$

The cloud is unstable to collapse when its self-gravity wins — when $|U_{\text{grav}}| > U_{\text{therm}}$. Rearranging the inequality gives the critical mass, the **Jeans mass**:

$$M_J \sim \left(\frac{k_B T}{G \mu m_H}\right)^{3/2} \rho^{-1/2}$$

This expression is the central machinery of the chapter, and it deserves to be stared at for a moment. Two variables sit on the right: temperature $T$ and density $\rho$. Increase the temperature, the Jeans mass grows — hotter gas pushes back harder, and only a more massive cloud has enough gravity to win. Increase the density, the Jeans mass *shrinks* — densely packed gas has more gravitational pull per unit volume, so a smaller mass tips over the threshold. The scalings $T^{3/2}$ and $\rho^{-1/2}$ are not arbitrary; they fall straight out of the energy balance.

Two consequences follow that decide where and how stars actually form.

First, **only cold gas forms stars.** The diffuse warm hydrogen between molecular clouds — temperature $\sim 8{,}000$ K, density $\sim 1$ atom per cm³ — has a Jeans mass on the order of $10^6 M_\odot$. There are no parcels that large gravitationally bound in any one place. Cool the gas to 10 K and increase the density to $10^4$ molecules per cm³ (typical of a molecular cloud core), and the Jeans mass drops by a factor of $\sim 10^4$, into the range where realistic gravitational fluctuations can exceed it.

Second, **collapse runs away once it starts.** As a parcel above the Jeans mass contracts, $\rho$ rises while $T$ stays nearly constant (radiative cooling is efficient until the gas becomes opaque). Look at the formula: rising $\rho$ at fixed $T$ means the *local* Jeans mass inside the contracting parcel drops. Sub-regions that were stable a moment ago tip over the threshold and start their own collapse. The cloud **fragments**. One cloud core does not make one star — it makes a cluster of stars.

The free-fall timescale for the collapse is set by gravity alone:

$$t_{\text{ff}} \sim \frac{1}{\sqrt{G\rho}}$$

For $\rho \sim 10^{-19}$ kg/m³ (a dense cloud core), $t_{\text{ff}}$ is roughly $10^5$ years. Fast by stellar standards. Negligible compared with the $\sim 10^{10}$-year age of the galaxy.

Two limits Jeans's analysis ignores: rotation and magnetic fields. Both add support, both raise the effective Jeans mass, and both are real. The full picture is messier than the formula. But the formula gets the *direction* of every effect right, and the orders of magnitude usually right. It is the kind of result Feynman would have called clarifying: not the last word, but the first word that makes the question precise.

### From protostar to main sequence

Once a fragment is bound, what happens next is a sequence of stages, each ruled by different physics.

**Stage 1: free-fall collapse.** The core is transparent to infrared photons. Compression heating is radiated away as fast as it is produced; the gas stays cold; pressure stays low; gravity wins essentially unopposed. The collapse is close to free fall — every parcel moves toward the center on a timescale $\sim 1/\sqrt{G\rho}$. This phase lasts about $10^5$ years for a solar-mass core.

**Stage 2: opacity, the first hydrostatic core.** Density rises until the central region becomes opaque to its own radiation. Heat now accumulates. Temperature climbs. Pressure climbs. Collapse halts at a hot, dense, hydrostatic core — not yet a star, but the seed of one. Infalling material continues to rain onto it from the surrounding envelope.

**Stage 3: the protostar.** Energy released as infalling matter slams into the core powers the object's luminosity. This phase is heavily obscured by the envelope — protostars are visible mostly at far-infrared and submillimeter wavelengths, where dust re-emits the energy of the buried photons. The protostar of HL Tau, in the Taurus star-forming region, has been imaged in striking detail by [ALMA in 2014](https://www.eso.org/public/news/eso1436/): concentric bright rings and dark gaps in a disk surrounding a star less than a million years old, with the gaps almost certainly being swept clean by forming planets.

**Stage 4: T Tauri phase.** When the envelope thins enough that the protostar becomes visible at optical wavelengths, the object is called a **T Tauri star** (after the prototype in Taurus, identified by Alfred Joy in [1945](https://ui.adsabs.harvard.edu/abs/1945ApJ...102..168J)). It is no longer accreting heavily. Its energy comes from gravitational contraction — a slow shrinking of its radius, converting potential energy into heat and radiation. The mechanism is the *Kelvin-Helmholtz contraction* introduced for the Sun's pre-main-sequence phase. The T Tauri star sits in the upper right of the [Hertzsprung-Russell diagram](https://www.cv.nrao.edu/~sransom/web/Ch5.html) — large radius, modest surface temperature, high luminosity — and it descends along a track first computed by Chushiro [Hayashi in 1961](https://ui.adsabs.harvard.edu/abs/1961PASJ...13..450H), the *Hayashi track*. For a solar-mass star the descent takes roughly 30 to 50 million years.

**Stage 5: main sequence.** When the central temperature reaches about $10^7$ K, the proton-proton chain (Chapter 5) ignites. Fusion replaces contraction as the energy source. The pressure support generated by fusion exactly balances gravity. The star is in hydrostatic equilibrium and will remain so for its main-sequence lifetime — for a solar-mass star, about 10 billion years.

Mass sets the pace. A 10-solar-mass star covers the Hayashi-track descent in roughly $10^5$ years; a 0.5-solar-mass star takes more than $10^8$ years. The reason is gravitational potential energy: more massive stars have far more energy to dump, but their luminosities scale roughly as $L \propto M^{3.5}$, so they radiate that energy proportionally faster. Both ends of the mass range arrive at the main sequence; the timeline differs by three orders of magnitude.

I want to flag one thing the textbook version often skips. The descent is not just a star shrinking — it is a star *with a disk* around it, and the disk is doing its own evolution. The conservation of angular momentum from the original cloud's rotation forces infalling matter into a flattened structure that lasts roughly 1 to 10 million years ([Williams & Cieza 2011](https://www.annualreviews.org/doi/10.1146/annurev-astro-081710-102548)). Inside that window, planets must form. After it, the gas is gone — photo-evaporated by the young star's ultraviolet output and stripped by stellar winds.

### Detecting planets around other stars

By the time of 51 Pegasi b in 1995, four detection methods had been proposed in principle and one had just worked in practice. As of 2026 the [NASA Exoplanet Archive](https://exoplanetarchive.ipac.caltech.edu/) lists more than 5,800 confirmed planets across thousands of systems. Every method has a different signature and a different bias. Combining them is what reveals the real population.

**Radial velocity** is the technique Mayor and Queloz used. A planet of mass $m_p$ orbiting a star of mass $M_\star$ at separation $a$ does not orbit the star — both bodies orbit their common center of mass. The star's orbit around that center is smaller than the planet's by the ratio $m_p / M_\star$, but it is not zero. As the star swings toward and away from Earth on its tiny orbit, its spectral lines Doppler-shift (Chapter 3, $\Delta\lambda/\lambda = v/c$). The radial-velocity amplitude is:

$$K = \left(\frac{2\pi G}{P}\right)^{1/3} \frac{m_p \sin i}{(M_\star + m_p)^{2/3}} \frac{1}{\sqrt{1 - e^2}}$$

For a circular orbit, the messy factor at the end is 1. The geometry factor $\sin i$ depends on the inclination of the orbit to our line of sight: edge-on ($i = 90°$) gives the full $K$; face-on ($i = 0°$) gives nothing. Radial velocity measures $m_p \sin i$, not $m_p$. The bias is toward systems we see closer to edge-on.

For a Jupiter analog (Jupiter's mass at Jupiter's distance from a Sun-like star), $K \approx 13$ m/s with a 12-year period. For an Earth analog, $K \approx 0.09$ m/s with a 1-year period. The 1995 instruments could measure 10 m/s; modern spectrographs like ESPRESSO ([Pepe et al. 2021](https://www.aanda.org/articles/aa/full_html/2021/01/aa38306-20/aa38306-20.html)) push below 1 m/s. Earth-analog detection is at the edge of current capability.

**Transit photometry** watches the small dimming when a planet crosses in front of its star. The depth of the dip equals the area ratio:

$$\frac{\Delta F}{F} = \left(\frac{R_p}{R_\star}\right)^2$$

For Jupiter across the Sun, that's about 1%. For Earth across the Sun, it's $\sim 8 \times 10^{-5}$ — eighty parts per million, demanding photometric precision unattainable from the ground because of atmospheric turbulence. The Kepler spacecraft, launched 2009 and decommissioned 2018, monitored 150,000 stars from solar orbit and detected several thousand transiting planets ([NASA Kepler mission](https://www.nasa.gov/mission_pages/kepler/main/index.html)). Its successor, [TESS](https://tess.mit.edu/), launched 2018, surveys most of the sky on shorter dwell times. Transit detection also requires that the orbit be edge-on enough that the planet passes in front of the star — for an Earth-distance orbit around a Sun-sized star, that geometric probability is about 0.5%. Most planets are not transiting from our line of sight; we miss them.

**Direct imaging** photographs the planet itself, separating its light from the star's overwhelming glare with a coronagraph or starshade. It works only for young, hot, massive planets at wide separations from their stars — the four-planet HR 8799 system, imaged at Keck and Gemini ([Marois et al. 2008](https://www.science.org/doi/10.1126/science.1166585)), is the canonical example. Direct imaging finds the planets that are easiest to see directly. That sample is small and unrepresentative.

**Microlensing** detects the brief brightening of a background star when a foreground star (and its planets) crosses the line of sight and gravitationally focuses the light. Sensitive to planets at intermediate separations around distant stars; gives one-shot detections that cannot be revisited.

Combining all methods and correcting for each one's selection effects, the consensus by 2026 is roughly: **every star has, on average, more than one planet**. Hot Jupiters (Mayor and Queloz's discovery) turn out to be rare — they occur around about 1% of Sun-like stars. The most common planet type in the galaxy is something the solar system does not have at all: planets between Earth's size and Neptune's, in orbits between a week and a year. Whether these are rocky super-Earths, mini-Neptunes with thick hydrogen envelopes, or ocean worlds is an open question that JWST atmospheric spectroscopy is beginning to settle ([JWST exoplanet atmosphere observations program](https://www.stsci.edu/jwst/science-execution/program-information.html)).

The **habitable zone** is the narrow band of orbital distances around a star where a rocky planet's surface temperature would allow liquid water given an Earth-like atmosphere. For the Sun, it stretches from roughly 0.95 to 1.5 AU ([Kopparapu et al. 2013](https://iopscience.iop.org/article/10.1088/0004-637X/765/2/131)). The definition does the most useful work it can — it points the search at planets where biosignatures might appear in atmospheric spectra — but it is a starting point, not a verdict on life. Subsurface oceans on icy moons (Europa, Enceladus) are outside the habitable zone by this definition, and they remain among the most plausible places for biology in our own solar system.

---

## Worked example: the Jeans mass of a typical molecular cloud core

Take a dense core in a giant molecular cloud — the kind of fragment that might produce a single low-mass star. Typical numbers:

- Temperature: $T = 10$ K.
- Number density: $n = 10^4$ molecules per cm³ $= 10^{10}$ m⁻³.
- Mean molecular mass: $\mu \approx 2.3$ (mostly $\mathrm{H}_2$ with some helium).
- Mass density: $\rho = n \mu m_H = 10^{10} \times 2.3 \times 1.67 \times 10^{-27}$ kg/m³ $\approx 3.8 \times 10^{-17}$ kg/m³.

Plug into $M_J \sim (k_B T / G \mu m_H)^{3/2} \rho^{-1/2}$. Compute the bracket first:

$$\frac{k_B T}{G \mu m_H} = \frac{(1.38 \times 10^{-23})(10)}{(6.67 \times 10^{-11})(2.3)(1.67 \times 10^{-27})} \approx 5.4 \times 10^{17} \text{ m}^2/\text{s}^2$$

Raise to the 3/2 power: $(5.4 \times 10^{17})^{3/2} \approx 1.3 \times 10^{26}$.

Divide by $\sqrt{\rho} = \sqrt{3.8 \times 10^{-17}} \approx 6.2 \times 10^{-9}$ kg^{1/2}/m^{3/2}.

$$M_J \approx \frac{1.3 \times 10^{26}}{6.2 \times 10^{-9}} \approx 2 \times 10^{34} \text{ kg}$$

In solar masses ($M_\odot \approx 2 \times 10^{30}$ kg), that is $M_J \approx 10\, M_\odot$ — order of a few solar masses with a more careful prefactor. A 10-K, $10^4\,\mathrm{cm}^{-3}$ core is sitting near the threshold. A slightly denser pocket inside it has a smaller Jeans mass and can fragment off as a single Sun-like star. A slightly less dense surrounding has a larger Jeans mass and remains a stable reservoir.

The free-fall time for this density: $t_{\text{ff}} \sim 1/\sqrt{G\rho} \approx 1/\sqrt{(6.67 \times 10^{-11})(3.8 \times 10^{-17})} \approx 2 \times 10^{13}$ s $\approx 600{,}000$ years. The cloud, once tipped, becomes a protostar on a timescale shorter than the age of the human species.

---

## Common misconceptions

- **"Stars form one at a time."** They do not. A giant molecular cloud above its Jeans mass fragments into many sub-Jeans-mass cores as it contracts — the cascade picture from the deep-dive. The vast majority of stars form in clusters of tens to thousands of stars, sharing a common chemical composition and roughly common age. The Sun was almost certainly born in such a cluster, which has since dispersed; identifying the Sun's siblings from chemical fingerprints in the Gaia spectroscopic survey is an active research program ([Gaia DR3](https://www.cosmos.esa.int/web/gaia/data-release-3)).
- **"The habitable zone is the only place life could exist."** Strictly, the habitable zone is the orbital band where a rocky planet with an Earth-like atmosphere could maintain liquid water on its surface. That is a useful operational target for telescopes hunting for biosignature gases — oxygen, ozone, methane in disequilibrium. It is not the definition of "places where life can exist." Europa's subsurface ocean is heated by tidal flexing and is outside the conventional habitable zone; it remains a serious astrobiological target. Confusing the operational target with a metaphysical claim narrows the search wrongly.
- **"Protostars are powered by fusion."** They are not. A protostar's luminosity comes from gravitational contraction — the Kelvin-Helmholtz mechanism, releasing potential energy as the radius shrinks. Fusion ignites only when the core temperature crosses $\sim 10^7$ K, which for a solar-mass star happens at the *end* of the Hayashi-track descent, not the beginning. The pre-main-sequence phase is gravity converting itself into heat. Conflating "young star" with "fusing star" misses this stage entirely.
- **"Hot Jupiters are typical."** They were the first exoplanets found because radial velocity and transit detection both favor massive planets on short-period orbits — a textbook case of confusing what an instrument is sensitive to with what is actually out there. Hot Jupiters occur around about 1% of Sun-like stars. The most common planet type in the galaxy is a sub-Neptune the solar system does not contain. Our system is not the median.

---

## Exercises

**Warm-up (Understand).** State in plain words what the Jeans mass is and why it depends on temperature and density the way it does. Why does raising the temperature *raise* the Jeans mass, and why does raising the density *lower* it?

**Application (Apply).** A molecular cloud core has $T = 20$ K and number density $n = 10^5$ cm⁻³. (a) Compute the mass density $\rho$ assuming mean molecular mass $\mu = 2.3$. (b) Compute the Jeans mass. (c) Compare to the core in the worked example and explain in one sentence why this one is denser but has a *smaller* Jeans mass.

**Synthesis (Analyze).** A G-type star is observed to have a radial-velocity wobble with amplitude $K = 30$ m/s and period $P = 100$ days. The host star mass is $1\, M_\odot$. (a) Using Kepler's third law, find the semi-major axis of the planet's orbit. (b) Using the radial-velocity formula in the simplified circular form $K \approx (m_p \sin i / M_\star) v_{\text{orb}}$, where $v_{\text{orb}} = 2\pi a / P$, find $m_p \sin i$ in Jupiter masses. (c) Explain what additional measurement would convert $m_p \sin i$ into the true planet mass $m_p$.

**Challenge (Analyze).** The Kepler spacecraft confirmed thousands of transiting planets but found the most common planet type in its sample to be sub-Neptunes (1.4–2.8 Earth radii) on orbits of weeks to months. (a) For a sub-Neptune at 0.5 AU around a $0.8\, M_\odot$ star, estimate the geometric transit probability $p \approx R_\star / a$. (b) Estimate the radial-velocity amplitude $K$ for a $5 M_\oplus$ planet at this orbit. (c) Argue from (a) and (b) which selection effect (transit geometry, radial-velocity sensitivity) explains why Kepler dominates the sub-Neptune catalog while radial-velocity surveys do not.

---

## LLM Exercises

### Build the star-formation simulator (`08-star-and-planet-formation.html`)

With `CLAUDE.md` and `DESIGN.md` loaded:

> **Show.** A four-panel D3 simulation. Panel 1: a 2D molecular cloud with adjustable temperature (5–50 K) and density (10²–10⁶ cm⁻³); the Jeans mass is displayed as a number that updates live, and a status indicator shows "stable" or "collapsing" based on the cloud's total mass relative to $M_J$. Panel 2: when collapse is triggered, the cloud fragments into multiple cores that shrink on the free-fall timescale, each annotated with its mass. Panel 3: an H-R diagram with three Hayashi tracks (0.5, 1.0, 3.0 $M_\odot$) descending from the upper right to a main-sequence band; a moving dot traces each star's position over time. Panel 4: radial-velocity and transit signals for a system with adjustable planet mass (0.1–10 Jupiter masses) and orbital distance (0.05–5 AU), plotted side by side as time-series.
>
> **Say.** Build an interactive D3 v7 visualization. For Panel 1, evaluate $M_J = (k_B T / G \mu m_H)^{3/2} \rho^{-1/2}$ with $\mu = 2.3$ and update on every slider change. For Panel 2, propagate the collapsing region using the free-fall timescale $t_{\text{ff}} = \sqrt{3\pi / 32 G\rho}$. For Panel 3, use simplified Hayashi tracks with luminosity following $L \propto M^{3.5}$ at main-sequence arrival and contraction time scaling as $t_{\text{KH}} \propto M^{-2}$. For Panel 4, compute the radial velocity amplitude $K$ from the circular formula and transit depth $(R_p/R_\star)^2$ with $R_p$ scaling roughly as $R_p \propto m_p^{1/3}$ for terrestrial planets and constant near Jupiter's radius for gas giants.
>
> **Constrain.** D3 v7 only. No external astrophysics libraries. Filename: `08-star-and-planet-formation.html`. All sliders update their panels in real time.
>
> **Verify.** (a) Set Panel 1 to $T = 10$ K and $n = 10^4$ cm⁻³; the Jeans mass should land near $5$–$10\, M_\odot$ (matching the worked example). (b) Set Panel 4 to $m_p = 1\, M_J$ at $a = 0.05$ AU around a Sun-like star; $K$ should be near 60 m/s with a $\sim 4$-day period (matching 51 Pegasi b). (c) Set Panel 4 to $m_p = 1\, M_\oplus$ at $a = 1$ AU; $K$ should drop near 0.09 m/s and the transit depth near 80 parts per million.

### Exploration

- In Panel 1, hold $T$ at 10 K and sweep density from $10^2$ to $10^6$ cm⁻³. The Jeans mass should scale as $\rho^{-1/2}$; verify numerically by checking that $M_J \sqrt{\rho}$ stays constant.
- In Panel 3, watch a 0.5 $M_\odot$ star and a 3 $M_\odot$ star start at the top of their Hayashi tracks. The massive star should arrive at the main sequence before the low-mass star is halfway there. Time the difference and compare to the analytic prediction $t_{\text{KH}} \propto M^{-2}$.
- In Panel 4, find the slider settings that put $K$ above 1 m/s (the ESPRESSO sensitivity threshold) and transit depth above 100 ppm (the TESS detection threshold) simultaneously. Note that this region of parameter space — where both methods work — is the small overlap that lets us measure both planet mass and radius for the same object, which is the only way to determine bulk density and hence composition.

### Bridge to Chapter 9

> **Show.** I now know how stars are born. The next question is what happens to a star *after* it arrives on the main sequence. Different masses lead very different lives.
>
> **Say.** Modify the simulator: add a fifth panel showing the main-sequence lifetime as a function of stellar mass, from 0.1 to 50 $M_\odot$. Use $t_{\text{MS}} \propto M / L \propto M^{-2.5}$. Mark the Sun's position and label its 10-billion-year lifetime. Mark a 20 $M_\odot$ star with its few-million-year lifetime.
>
> **Verify.** A 10 $M_\odot$ star should have a main-sequence lifetime around 30 million years — about a factor of 300 shorter than the Sun's. The plot should make visible that massive stars live fast and die young, a fact that drives everything in the next chapter.

Save as `08b-main-sequence-lifetimes-preview.html`. Lead-in to Chapter 9 — *Stars from Adolescence to Old Age*.

---

## What would change my mind

The chapter rests on the claim that the Jeans criterion — thermal pressure versus self-gravity, with temperature and density as the only essential variables — is the right zeroth-order framework for where stars form, and that the resulting protostellar disk is the natural birthplace of the planets we now detect by the millions. The framework would need rebuilding if any of three observations held up under scrutiny. First, if a future high-resolution survey (ALMA, the [SKA](https://www.skao.int/), or a JWST follow-up) found a substantial population of *isolated* protostars forming far from any cold molecular environment — stars whose precursors had $T \gg 30$ K — the Jeans mass argument would need to be replaced or heavily amended. Second, if the [NASA Exoplanet Archive](https://exoplanetarchive.ipac.caltech.edu/) population, corrected for selection effects in all four detection methods, showed a planet occurrence rate per star that scaled wrongly with stellar mass (the current rough prediction is that lower-mass stars host *more* small planets per star; a robust reversal would falsify part of the disk-formation story). Third, if a substantial population of planets were found orbiting bodies that had never been in a protoplanetary disk at all — for example, around white dwarfs with no evidence of a second-generation disk — without a viable alternative formation channel, the disk story would be incomplete in a way that mattered. So far, every dataset has been consistent with the framework; the corrections to the framework have been quantitative, not foundational.

## Still puzzling

- *What determines the stellar initial mass function?* The distribution of stellar masses at birth — heavily weighted toward low-mass stars, falling off roughly as $dN/dM \propto M^{-2.35}$ above one solar mass ([Salpeter 1955](https://articles.adsabs.harvard.edu/cgi-bin/nph-iarticle_query?1955ApJ...121..161S)) — is observed to be nearly universal across very different star-forming environments. Why it should be universal, given that the cloud conditions differ, is not understood from first principles. Several candidate mechanisms (turbulent fragmentation cascades, magnetic regulation, feedback from the first massive stars in a cluster) each capture part of the story; no single picture is yet decisive.
- *How exactly do planets cross the meter-size barrier?* In a protoplanetary disk, gas orbits slightly slower than solid particles, so pebbles between roughly a millimeter and a meter experience aerodynamic drag and should spiral into the star in $\sim 10^4$ years — far faster than they can grow into kilometer-sized planetesimals by sticking collisions. The fact that planets exist tells us something escapes the trap. Streaming instabilities, pressure traps at disk substructures, and gravitational concentration in turbulent eddies are all candidate solutions. None has been confirmed observationally yet.
- *Are hot Jupiters migration outcomes or in-situ formation outcomes?* The standard story since 1995 has been that gas giants form past the ice line and migrate inward through disk-planet interactions. An alternative — that hot Jupiters can form in situ at small orbital separations under specific disk conditions — has gained some traction since the late 2010s. The two scenarios predict different orbital eccentricity and obliquity distributions for the surviving population. The data so far prefer migration as the dominant channel but do not rule out in-situ contributions; the question is genuinely open.

---

**Tags:** star formation, Jeans instability, molecular clouds, protostars, T Tauri, Hayashi track, exoplanets, 51 Pegasi b, radial velocity, transit photometry, habitable zone, Kepler, JWST
