# Chapter 8 — The Birth of Stars

*A spectrograph in Haute-Provence, October 1995, and a Jupiter-mass planet on a four-day orbit that should not have existed.*

---

On the night of October 6, 1995, Michel Mayor and Didier Queloz pointed a spectrograph at 51 Pegasi — an ordinary G-type star, naked-eye visible, about 50 light-years away in Pegasus. The spectral lines moved. Toward Earth, then away, then toward Earth again, in a smooth sinusoid with a period of 4.231 days and an amplitude of about 56 meters per second — roughly the speed of a thrown baseball.

By Newton's third law, something was pulling. The arithmetic pointed to a planet of at least half Jupiter's mass orbiting at 0.05 astronomical units — one-eighth of Mercury's distance from the Sun. A gas giant on a four-day orbit, with day-side temperatures above a thousand Kelvin.

The problem: this should not exist.

Gas giants, as everyone then understood them, form past the *ice line* — far enough from the star that water condenses onto solid grains, building up the heavy rocky core that then sweeps up hydrogen gas and balloons into a giant. Four days from a Sun-like star is nowhere near the ice line. The temperature is wrong. The available solid material is wrong. 51 Pegasi b should not be there.

It was there anyway. And this single observation did more damage than just adding an awkward entry to a catalog. It quietly demolished the assumption that our solar system was typical, that the model we had built for our own backyard was a general theory. It forced astronomers to ask an honest question they had mostly avoided: what does the actual planet population look like, and what does that tell us about how stars and planets form?

![Mayor and Queloz's 1995 phase-folded radial-velocity curve for 51 Pegasi. A 4.231-day sinusoid with 56 m/s amplitude implies a Jupiter-mass planet at 0.05 AU — a hot Jupiter where gas giants were not supposed to form.](../images/08-birth-of-stars-fig-01.png)
*Figure 8.1 — 51 Pegasi b Discovery Radial-Velocity Curve*

This chapter is about both halves of that question — the machinery that builds stars, and the techniques we use to see what gets built around them.

---

## Why stars don't form everywhere

The galaxy contains roughly $10^{10}$ solar masses of cold gas, mostly molecular hydrogen at temperatures of 10 to 30 K, concentrated in giant molecular clouds. If gravity simply pulled gas together, these clouds should have collapsed into stars long ago. They have not. Star formation in the Milky Way proceeds at roughly one solar mass per year — slow enough that the gas reservoir lasts another ten billion years.

Something holds the clouds up. Thermal pressure of the gas pushes outward. Turbulent bulk motions add more pressure. Magnetic fields thread the cloud and resist compression. All three fight gravity. A region collapses only where gravity wins.

In 1902, James Jeans worked out the exact balance for thermal pressure alone. Take a uniform sphere of cold gas, temperature $T$, mass density $\rho$. Ask: if you compress it slightly, which side wins — gravity pulling inward, or pressure pushing back? The answer depends on whether the gravitational potential energy exceeds the thermal energy. Gravitational potential energy scales as $-GM^2/R$; thermal energy scales as $(M/\mu m_H) k_B T$, where $\mu m_H$ is the mean particle mass. Set them equal and solve for the critical mass — the **Jeans mass**:

$$M_J \sim \left(\frac{k_B T}{G \mu m_H}\right)^{3/2} \rho^{-1/2}$$

This is worth staring at. Two variables: temperature and density. Both have physically sensible effects. Raise the temperature, and pressure pushes back harder — you need a more massive cloud before gravity can win, so $M_J$ goes up. Raise the density, and the same mass is packed into a smaller volume, making gravity stronger per unit volume — a smaller mass tips the threshold, so $M_J$ goes down. The exponents $T^{3/2}$ and $\rho^{-1/2}$ are not chosen to fit data; they fall directly out of the energy balance.

<!-- → [CHART: Two panels showing Jeans mass vs. temperature (left, at fixed ρ) and Jeans mass vs. density (right, at fixed T) — both log-log axes; left panel shows M_J rising as T^(3/2), right panel shows M_J falling as ρ^(−1/2); mark the warm diffuse ISM (T=8000 K, n=1 cm⁻³) and cold molecular core (T=10 K, n=10⁴ cm⁻³) on each, showing the factor-of-10,000 drop in M_J between the two environments] -->

Two consequences decide where stars actually form.

First, only cold gas forms stars. The warm diffuse hydrogen between molecular clouds — temperature around 8,000 K, density around one atom per cubic centimeter — has a Jeans mass on the order of a million solar masses. No parcel that large sits gravitationally bound in one place. Cool the gas to 10 K and compress it to $10^4$ molecules per cubic centimeter (a typical molecular cloud core), and the Jeans mass drops by a factor of roughly ten thousand, into the range where realistic gravitational fluctuations can exceed it. Cold, dense regions are the birthplace of stars. Nothing else is close.

Second, collapse runs away once it starts. As a fragment contracts, density rises while temperature stays nearly constant — cold molecular gas radiates efficiently, dumping heat as fast as compression generates it. Look at the Jeans formula: rising $\rho$ at fixed $T$ means the local Jeans mass inside the contracting fragment keeps dropping. Sub-regions that were stable moments ago tip over the threshold and begin their own collapses. The cloud **fragments**. One cloud core does not produce one star — it produces a cascade of smaller collapses, a cluster of stars sharing a common chemical fingerprint and a roughly common age.

![Two panels. Left: a sphere of cold gas with gravitational binding energy versus thermal energy. Right: Jeans mass falls with density as rho to the minus one half. Warm diffuse ISM has Jeans mass too large to collapse;...](../images/08-birth-of-stars-fig-02.png)
*Figure 8.2 — Jeans Criterion: When Gravity Beats Pressure*

The free-fall timescale is set by gravity alone:

$$t_\text{ff} \sim \frac{1}{\sqrt{G\rho}}$$

For a typical dense core ($\rho \sim 10^{-17}$ kg/m³), this comes out to roughly $10^5$ years. A cloud fragment, once it tips over the Jeans threshold, becomes a protostar on a timescale shorter than the age of the human species.

I want to flag two things Jeans's analysis ignores: rotation and magnetic fields. Both add support, both raise the effective threshold, and both are real. The full picture is messier than the formula. But the formula gets the direction of every effect right, and the orders of magnitude usually right. It makes the question precise, which is what a good first approximation is supposed to do.

---

## A worked collapse

Take a typical molecular cloud core: temperature $T = 10$ K, number density $n = 10^4$ molecules per cm³, mean molecular mass $\mu = 2.3$ (mostly H₂ with helium). The mass density is:

$$\rho = n \mu m_H = 10^{10} \times 2.3 \times 1.67 \times 10^{-27} \approx 3.8 \times 10^{-17} \text{ kg/m}^3$$

Compute the bracket in the Jeans formula:

$$\frac{k_B T}{G \mu m_H} = \frac{(1.38 \times 10^{-23})(10)}{(6.67 \times 10^{-11})(2.3)(1.67 \times 10^{-27})} \approx 5.4 \times 10^{17} \text{ m}^2/\text{s}^2$$

Raise to the 3/2: $(5.4 \times 10^{17})^{3/2} \approx 1.3 \times 10^{26}$. Divide by $\sqrt{\rho} \approx 6.2 \times 10^{-9}$:

$$M_J \approx \frac{1.3 \times 10^{26}}{6.2 \times 10^{-9}} \approx 2 \times 10^{34} \text{ kg} \approx 10\, M_\odot$$

A 10-K, $10^4$-cm⁻³ core sits near the threshold — order of a few solar masses with a careful prefactor. A slightly denser pocket inside it has a smaller Jeans mass and can fragment off as a single Sun-like star. The slightly less dense surrounding envelope has a larger Jeans mass and stays stable.

Free-fall time: $t_\text{ff} \sim 1/\sqrt{G\rho} \approx 1/\sqrt{(6.67 \times 10^{-11})(3.8 \times 10^{-17})} \approx 2 \times 10^{13}$ s $\approx 600{,}000$ years.

<!-- → [DIAGRAM: Two-panel diagram — left: a molecular cloud with density contours, Jeans mass labeled at two locations (diffuse outer region: large M_J, stable; dense core: small M_J, collapsing); right: the fragmentation cascade, one cloud breaking into multiple sub-Jeans cores each on its own free-fall trajectory] -->

---

## From falling gas to burning star

Once a fragment is gravitationally bound, it passes through a sequence of stages, each governed by different physics.

**Free-fall collapse.** The core is transparent to infrared photons. Compression heat radiates away faster than it accumulates; the gas stays cold; pressure stays low; gravity wins essentially unopposed. This is about $10^5$ years for a solar-mass fragment.

**The first hydrostatic core.** Density rises until the central region becomes opaque to its own radiation. Heat now accumulates. Temperature climbs. Pressure climbs. Collapse halts in a hot, dense, pressure-supported seed — not yet a star, but the beginning of one. Infalling material continues to rain in from the surrounding envelope.

**The protostar.** Energy released as infalling matter slams onto the core powers the luminosity. The object is buried under its own envelope, visible mostly at far-infrared and millimeter wavelengths where dust re-emits the energy of the hidden photons. The protostar of HL Tauri — in the Taurus star-forming region, about a million years old — was imaged by ALMA in 2014, and the image is remarkable: a flat rotating disk of dust with concentric bright rings and dark gaps already cleared by forming planets, surrounding a star that has barely begun.

![Schematic of ALMA's 2014 millimeter image of HL Tau. Concentric bright rings separated by dark gaps cleared by planet-mass bodies. The protostellar disk caught in the act of building planets, 259 years after Kant prop...](../images/08-birth-of-stars-fig-04.png)
*Figure 8.4 — HL Tau ALMA Image: A Disk Caught in the Act*

**The T Tauri phase.** When the envelope thins enough that the protostar becomes visible at optical wavelengths, it is called a T Tauri star — named after the prototype in Taurus, identified by Alfred Joy in 1945. No longer accreting heavily, its energy now comes from gravitational contraction: a slow shrinking of its radius, converting potential energy into heat and light. This is the *Kelvin-Helmholtz* mechanism. On the Hertzsprung-Russell diagram, a T Tauri star sits in the upper right — large radius, modest surface temperature, high luminosity — and it descends toward the main sequence along a track first computed by Chushiro Hayashi in 1961. For a solar-mass star, the descent takes 30 to 50 million years.

![Top: five stages from gravitational free-fall through opacity-trapped first hydrostatic core, embedded protostar, optically visible T Tauri star, to main sequence ignition. Bottom: Hayashi-track descents for 0.5, 1.0,...](../images/08-birth-of-stars-fig-03.png)
*Figure 8.3 — Five-Stage Protostar Evolution + Hayashi Track*

**The main sequence.** When the central temperature reaches about $10^7$ K, the proton-proton chain ignites. Fusion replaces contraction. Thermal pressure from nuclear burning exactly balances gravity. The star is now in hydrostatic equilibrium and will remain there for billions of years.

<!-- → [DIAGRAM: H-R diagram showing three Hayashi tracks (0.5, 1.0, 3.0 solar masses) descending from upper right to the main sequence — annotate each stage: T Tauri phase at top, main-sequence arrival at bottom, time annotations showing that the 3-solar-mass star arrives before the 0.5-solar-mass star is halfway down] -->

Mass sets the pace throughout. A 10-solar-mass star covers the Hayashi descent in roughly $10^5$ years; a 0.5-solar-mass star takes more than $10^8$. The reason is energy bookkeeping: more massive stars have more gravitational potential energy to dump, but their luminosities scale roughly as $L \propto M^{3.5}$, so they radiate that energy proportionally faster. Both arrive at the main sequence; the timeline differs by three orders of magnitude.

One thing the standard story often skips: the descending star arrives with a disk. Conservation of angular momentum from the original cloud's rotation forces infalling matter into a flattened structure. The disk lasts roughly 1 to 10 million years, photo-evaporated over time by the young star's ultraviolet output and stripped by its winds. Inside that window, planets must form. After it, the gas is gone. The disk is not a side effect of star formation — it is where the planets come from, and the clock on planet formation starts with the star's birth and runs for only a few million years.

<!-- → [INFOGRAPHIC: Timeline of star and disk evolution — horizontal axis 0 to 10 Myr; labeled events: molecular cloud collapse (0), first hydrostatic core (~10³ yr), protostar phase (~10⁵ yr), T Tauri phase (~1 Myr), disk dispersal window (~1–10 Myr), main-sequence ignition (~30–50 Myr for solar-mass star); shaded bar showing "planet formation window" inside disk dispersal; student should see how narrow the window is relative to the star's main-sequence lifetime] -->

---

## Seeing what gets built

By 1995, four planet-detection methods had been proposed. Mayor and Queloz's success with 51 Pegasi b was the first unambiguous use of one of them in practice. As of now, the NASA Exoplanet Archive lists more than 5,800 confirmed planets. Every method has a different bias. Understanding the bias is how you get from "what we found" to "what is actually out there."

**Radial velocity** — the Mayor-Queloz method — measures the Doppler wobble a planet imposes on its star. A planet does not orbit its star; both bodies orbit their common center of mass. The star's orbit around that center is smaller than the planet's by the mass ratio $m_p/M_\star$, but it is real and measurable. The radial-velocity amplitude for a circular orbit is:

$$K \approx \frac{m_p \sin i}{M_\star} \cdot \frac{2\pi a}{P}$$

where $i$ is the orbital inclination to our line of sight and $a/P$ gives the orbital speed. For Jupiter at Jupiter's distance from a Sun-like star, $K \approx 13$ m/s with a 12-year period. For Earth at 1 AU, $K \approx 0.09$ m/s with a 1-year period. The method measures $m_p \sin i$, not $m_p$ — it gives a lower bound on mass, not the mass itself. The bias: toward massive planets on short-period orbits seen nearly edge-on.

**Transit photometry** watches the fractional dimming when a planet crosses in front of the star:

$$\frac{\Delta F}{F} = \left(\frac{R_p}{R_\star}\right)^2$$

For Jupiter across the Sun, about 1%. For Earth, about 80 parts per million — demanding photometric precision impossible from the ground. The Kepler spacecraft, in solar orbit from 2009 to 2018, monitored 150,000 stars and detected several thousand transiting planets. The bias: toward planets whose orbits happen to be nearly edge-on as seen from Earth. For a planet at 1 AU around a Sun-sized star, the geometric probability of a transiting alignment is about 0.5%. Most planets are not transiting from our vantage point.

<!-- → [DIAGRAM: Side-by-side comparison of radial velocity and transit signals for the same hypothetical planet — left: sinusoidal radial velocity curve, amplitude K labeled, period P labeled; right: photometric light curve showing the flat bottom transit dip, depth (R_p/R_★)² labeled, contact points marked — student should see what each method measures and how each is blind to different parts of orbital geometry] -->

**Direct imaging** photographs the planet itself, separating its light from the star with a coronagraph. It works only for young, hot, massive planets at wide separations — the four-planet HR 8799 system, imaged at Keck and Gemini, is the canonical example. The bias: toward the planets that are easiest to see, which are the least typical.

**Microlensing** detects the brief brightening of a background star when a foreground star and its planets pass across the line of sight and gravitationally focus the light. It is sensitive to planets at intermediate separations around distant stars, and it gives one-shot detections that cannot be revisited.

Combining all four methods and correcting for each one's selection effects, the picture that emerges is this: every star has on average more than one planet. Hot Jupiters — Mayor and Queloz's discovery type — occur around only about 1% of Sun-like stars. They were the first found because radial velocity and transit detection both favor massive planets on short orbits, a textbook case of confusing what an instrument is sensitive to with what is actually out there. The most common planet type in the galaxy is something our solar system does not have at all: planets between Earth's size and Neptune's, on orbits between a week and a year. Whether these are rocky super-Earths, mini-Neptunes with thick hydrogen envelopes, or ocean worlds is a question that JWST atmospheric spectroscopy is beginning to answer.

![A two-by-two comparison of radial velocity, transit, direct imaging, and microlensing. Each method's signal shape is shown alongside its sensitivity range and built-in selection bias toward certain orbital geometries...](../images/08-birth-of-stars-fig-05.png)
*Figure 8.5 — Four Exoplanet Detection Methods*

![Mass-vs-semi-major-axis scatter of detected exoplanets, color-coded by method. Hot Jupiters cluster top-left. Earth analogs (1 AU, 1 Earth mass) sit at the edge of capability. Solar system planets marked for reference...](../images/08-birth-of-stars-fig-06.png)
*Figure 8.6 — Selection Effects: What's Actually Out There vs What We Can See*

<!-- → [CHART: Exoplanet population scatter plot — axes: orbital period (x, log, days) vs. planet radius (y, log, Earth radii); points color-coded by detection method (radial velocity, transit, direct imaging, microlensing); shaded regions showing each method's sensitivity window; student should see that RV and transit discoveries cluster at short periods and large radii, while the sub-Neptune gap around 1.5–2 R_Earth sits near the center of Kepler's coverage — the detection bias is visible in the clustering] -->

The **habitable zone** — the band of orbital distances where a rocky planet with an Earth-like atmosphere could maintain liquid surface water — spans roughly 0.95 to 1.5 AU for the Sun. The definition does real work: it focuses telescope time on planets where biosignature gases might appear in atmospheric spectra. But it is a starting point for the search, not a verdict on where life can exist. Europa's subsurface ocean lies outside the habitable zone by this definition and remains one of the most plausible places for biology in our own solar system. The zone defines the observational target. It does not define the boundary of possibility.

![Habitable-zone orbital range plotted against host-star spectral type. The HZ moves inward for cool dwarfs and outward for luminous A stars. Proxima b in the HZ at 0.05 AU around an M dwarf. Sun's HZ approximately 0.95...](../images/08-birth-of-stars-fig-07.png)
*Figure 8.7 — Habitable Zone vs Star Type*

---

## What the planet population tells us about star formation

The discovery of 51 Pegasi b did not just add a datum. It forced a revision of mechanism. Hot Jupiters cannot form where they are found — the ice line argument is sound. So they must form elsewhere and migrate. The standard story has gas giants coalescing past the ice line and then losing angular momentum to the disk gas as they spiral inward, stopping when the disk dissipates.

This matters for star formation because it connects the planet population to the disk. The existence of hot Jupiters is evidence that disk-planet interactions are real and energetic enough to move a Jupiter-mass body across several astronomical units in a few million years. The rarity of hot Jupiters (1% of Sun-like stars) tells you that most disks dissipate before migration can complete, or that most giants never form close enough to migrate far, or both. The distribution of planet orbital separations is a fossil of the disk's lifetime and structure.

And the disk's lifetime is set by the star. A more massive star has more ultraviolet output; it photo-evaporates its disk faster; planets have less time to form. Current data suggest that lower-mass stars host more small planets per star than higher-mass stars — consistent with the idea that the slower, longer-lived disks around cool stars give planet formation more time to run.

The Jeans mass, the free-fall time, the disk lifetime, the planet population — these are not separate topics that happen to appear in the same chapter. They are one connected story about what happens when a cold parcel of molecular gas exceeds a critical mass and falls.

---

## What you should be able to do now

You should be able to state the Jeans criterion in physical terms — pressure versus gravity in a cold cloud — and explain why the Jeans mass increases with temperature and decreases with density. The scaling $M_J \propto T^{3/2} \rho^{-1/2}$ should feel inevitable, not memorized.

You should be able to walk through the protostellar sequence: free-fall collapse, first hydrostatic core, protostar, T Tauri, main sequence — and name the energy source at each stage. The transition from Kelvin-Helmholtz contraction to nuclear fusion is the moment the main sequence begins.

You should be able to compute the radial-velocity amplitude $K$ for a planet of known mass and orbital period around a star of known mass, and explain what $\sin i$ means and why it limits what radial velocity can tell you.

You should be able to compare the radial-velocity and transit methods by the planets each one is biased toward, and explain why the first confirmed exoplanets were hot Jupiters rather than Earth-like planets.

And you should understand that the solar system is not the template. The galaxy's most common planet type is something we do not have. The framework built from our own backyard was wrong in the specific way that frameworks built from one example are always wrong: it mistook the particular for the general.

---

## Exercises

**Warm-up** *(Tests: Jeans criterion; protostellar sequence; detection method concepts)*

1. State the Jeans criterion in plain words — no formula. What two physical quantities compete, and what happens when one wins? Then explain in one sentence why raising the temperature increases the Jeans mass rather than decreasing it.

2. List the five stages of protostellar evolution covered in this chapter (free-fall collapse through main sequence), and for each stage name the dominant energy source. At which stage does the object first become visible at optical wavelengths?

3. The radial-velocity method measures $m_p \sin i$, not $m_p$. What does $i$ represent, and under what geometric condition does the method give the true planet mass? Under what condition does it give the smallest possible measurement for a given actual mass?

**Application** *(Tests: Jeans mass calculation; radial-velocity formula; transit depth)*

4. A molecular cloud core has $T = 20$ K and number density $n = 10^5$ cm⁻³, with mean molecular mass $\mu = 2.3$. (a) Compute the mass density $\rho$. (b) Compute the Jeans mass. (c) Compare to the worked example at $T = 10$ K, $n = 10^4$ cm⁻³. The new core is denser but warmer — which effect dominates, and by how much?

5. A planet of mass $m_p = 2\,M_J$ orbits a $1\,M_\odot$ star in a circular orbit with period $P = 3$ days at semi-major axis $a = 0.04$ AU. Assume $\sin i = 1$ (edge-on). (a) Compute the orbital speed $v_\text{orb} = 2\pi a / P$ in m/s. (b) Compute the radial-velocity amplitude $K \approx (m_p/M_\star) v_\text{orb}$. (c) Is this detectable with a 1995-era spectrograph (sensitivity ~10 m/s)? With a modern instrument (sensitivity ~1 m/s)?

6. The Kepler spacecraft detected an Earth-sized planet ($R_p = 1\,R_\oplus$) transiting a Sun-like star ($R_\star = 1\,R_\odot$). (a) Compute the transit depth $\Delta F / F = (R_p/R_\star)^2$. (b) Express your answer in parts per million. (c) The geometric transit probability for this planet at $a = 1$ AU is approximately $p \approx R_\star/a$. Evaluate it. What does this tell you about how many Earth-analogs Kepler must monitor to find even one?

**Synthesis** *(Tests: connecting Jeans physics to fragmentation; connecting detection biases to the actual population)*

7. A giant molecular cloud has total mass $10^5\,M_\odot$, temperature 15 K, and mean density $n = 500$ cm⁻³. (a) Estimate the Jeans mass for these conditions. (b) If the cloud fragments into cores each near the Jeans mass, roughly how many cores — and therefore how many star systems — would form? (c) Each core subsequently contracts to higher density. Explain qualitatively why the Jeans mass inside each contracting core drops further, and what this predicts about the typical multiplicity of stellar systems.

8. Hot Jupiters were the first exoplanets confirmed around Sun-like stars. The most common planet type in the galaxy is a sub-Neptune on a short-period orbit. (a) Explain, using the radial-velocity amplitude formula, why a hot Jupiter ($m_p \sim 1\,M_J$, $P \sim 4$ days) is far easier to detect via radial velocity than a sub-Neptune ($m_p \sim 5\,M_\oplus$, $P \sim 30$ days) around the same star. Estimate the ratio of their $K$ amplitudes. (b) Does the rarity of hot Jupiters in the true population contradict the fact that they were the first type found? Explain the distinction between detection frequency and occurrence rate.

**Challenge** *(Tests: Jeans mass scaling; combining transit and RV to get density)*

9. The Jeans mass scales as $M_J \propto T^{3/2} \rho^{-1/2}$. (a) By what factor does the Jeans mass change if the temperature drops from 30 K to 10 K while density stays constant? (b) By what factor does it change if the density increases by $10^4$ at constant temperature? (c) A region starts at $T = 30$ K, $n = 10^2$ cm⁻³ (warm diffuse gas) and cools and condenses to $T = 10$ K, $n = 10^5$ cm⁻³. What is the combined factor of change in $M_J$? What does this tell you about why molecular clouds, not the diffuse ISM, are where stars form?

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
