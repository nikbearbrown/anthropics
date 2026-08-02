# Chapter 13 — The Big Bang

*A persistent hiss in a New Jersey radio antenna in 1965, blamed first on pigeons, that turned out to be the oldest light in the universe — predicted in detail seventeen years before anyone bothered to look.*

---

## Suggested titles

1. The Big Bang
2. The Oldest Light, and the Three Things It Tells Us
3. How We Know the Universe Had a Beginning

## TL;DR

The universe began hot and dense about 13.8 billion years ago, and three independent observations — galaxies receding in proportion to distance, a 2.725 K microwave glow filling the sky, and the precise ratio of hydrogen to helium in old gas — agree on this story to within their measurement errors. The deepest evidence is the microwave glow, because its blackbody spectrum was predicted before it was found.

---

## Learning objectives

By the end of this chapter you will be able to:

1. **(Understand)** State Hubble's law $v = H_0 d$, give a modern value of $H_0$, and explain in plain language why "expansion of space" is not the same statement as "galaxies moving through space."
2. **(Apply)** Estimate the age of the universe from $1/H_0$ and explain why this is an order-of-magnitude shortcut rather than the exact answer.
3. **(Apply)** Use Wien's law (from Chapter 3) to predict the wavelength at which a 2.725 K blackbody peaks, and verify that prediction lies in the microwave band.
4. **(Analyze)** State the three independent pillars of Big Bang evidence — recession, CMB, primordial element abundances — and explain why their agreement is more powerful than any one of them alone.
5. **(Apply)** Build an interactive D3 simulation of the Hubble diagram and the CMB blackbody spectrum at 2.725 K, and use it to fit $H_0$ from supernova data.

**Prerequisites.** Chapter 3 (blackbody radiation, Wien's law, Doppler shift). Chapter 7 (distance scales — parsec, megaparsec). Chapters 9–10 (stellar nucleosynthesis as the contrast case). Basic algebra and unit conversion. No general relativity required — the relevant facts are stated where needed.

---

## Opening case: Penzias and Wilson, Holmdel, May 1965

In May 1965 two radio astronomers at Bell Labs in Holmdel, New Jersey, published a one-page note titled ["A Measurement of Excess Antenna Temperature at 4080 Mc/s"](https://articles.adsabs.harvard.edu/cgi-bin/nph-iarticle_query?bibcode=1965ApJ...142..419P&db_key=AST&page_ind=0&data_type=GIF&type=SCREEN_VIEW&classic=YES). Their 20-foot horn antenna, designed to track the Echo communications satellite, was picking up about 3.5 degrees Kelvin of "excess" radiation, isotropically, at every hour, in every season, after every instrumental check.

Arno Penzias and Robert Wilson had spent the better part of a year trying to make the signal go away. They cooled the receiver, tested the cabling, climbed into the antenna and scrubbed out a layer of "white dielectric material" left by nesting pigeons. The pigeons were relocated to Whippany; they flew back. Nothing changed the signal.

A theory existed — [Gamow, Alpher, and Herman](https://www.nature.com/articles/162774b0) had predicted in 1948 that the Big Bang should leave behind residual thermal radiation at a few degrees Kelvin — but Penzias and Wilson did not know about it, and almost nobody else did either. The prediction had been ignored for seventeen years. What got Penzias on the phone to Robert Dicke at Princeton was a casual conversation revealing Dicke's group was *building an antenna* to look for exactly this signal. Dicke hung up and said: "Well, boys, we've been scooped."

In an [accompanying paper](https://articles.adsabs.harvard.edu/cgi-bin/nph-iarticle_query?bibcode=1965ApJ...142..414D&db_key=AST&page_ind=0&data_type=GIF&type=SCREEN_VIEW&classic=YES) Dicke's group explained what Penzias and Wilson had seen: the cooled remnant of radiation from when the universe was hot enough to be opaque, stretched from visible light into microwaves by the expansion of space, arriving uniformly from every direction because it had originated everywhere at once. Penzias and Wilson got the [1978 Nobel Prize](https://www.nobelprize.org/prizes/physics/1978/summary/). The pigeons got nothing.

---

## Core concept

### Hubble's law and the expansion of space

Start with what you can see from a backyard telescope, given good enough instruments.

In 1929 Edwin Hubble, working at Mount Wilson, published [a four-page paper](https://www.pnas.org/doi/10.1073/pnas.15.3.168) showing spectral lines of distant galaxies were shifted to longer wavelengths in proportion to distance. Treating the shift as Doppler recession (Chapter 3, $\Delta\lambda/\lambda = v/c$):

$$v = H_0 \, d$$

The modern value is $H_0 \approx 70 \text{ km/s/Mpc}$ — a galaxy one megaparsec away (3.26 million light-years) recedes at 70 km/s. (The exact number is contested; we'll return to it.)

Credit gets reassigned slowly. In 1927 — two years before Hubble — the Belgian priest and physicist Georges Lemaître had [derived this exact relation](https://articles.adsabs.harvard.edu/pdf/1927ASSB...47...49L) from Einstein's equations, in French, in a small Belgian journal. He even estimated the constant. When the paper was translated into English in 1931 the relevant paragraphs were dropped — by Lemaître himself or by editors, historians still argue. Hubble's name attached. The physics belongs to both.

Language matters here. The naïve reading of $v = H_0 d$ is that galaxies are flying outward through space, like shrapnel from an explosion, with us at the center. This is wrong on every count. The general-relativistic reading is that space itself is stretching — the *metric* that defines distances between galaxies is growing with time — and the galaxies are mostly sitting still relative to their local patches of space, carried apart the way two ink dots on the surface of an inflating balloon are carried apart without crawling across the rubber.

The balloon analogy earns its place: every point sees every other receding; no point is the center; recession velocity grows in proportion to separation. It breaks because the balloon is a 2D surface embedded in 3D space we can step outside of; the universe has no outside vantage point.

The immediate consequence of $v = H_0 d$ is that running the film backward compresses everything. At some finite moment in the past, all the matter we now observe was packed together. The crude estimate:

$$T_0 \approx \frac{1}{H_0}$$

A megaparsec is $3.086 \times 10^{19}$ km, so $H_0 = 70 \text{ km/s/Mpc}$ converts to $H_0 \approx 2.27 \times 10^{-18} \text{ s}^{-1}$, giving $1/H_0 \approx 14$ billion years. The careful answer — accounting for gravity slowing the expansion early on and dark energy speeding it up now — is [13.8 billion years](https://arxiv.org/abs/1807.06209). The crude estimate is good to within a few percent.

### Three pillars of evidence: redshift, CMB, primordial element abundances

The expansion alone is an opening argument. It tells you the universe had a hot dense past. It does not tell you what conditions were like in that past. For that you need two more observations that come from entirely different physics.

**Pillar 1: the recession itself.** Hubble's law plus the inverse-square law plus a standard candle — Type Ia supernovae, calibrated through Cepheids — builds the distance ladder. The same redshift-distance relation has been measured out to $z > 10$ with JWST. The linear relation breaks at the highest redshifts (expansion has not been constant), but farther galaxies redshift more, all the way to the edge of what we can see.

**Pillar 2: the cosmic microwave background.** The next section unpacks it. The short version: [Gamow, Alpher, and Herman](https://link.aps.org/doi/10.1103/PhysRev.73.803) predicted in 1948 that a hot dense beginning leaves behind cooled thermal radiation at a few Kelvin. Penzias and Wilson stumbled onto it at 3.5 K. In 1990 [COBE FIRAS](https://articles.adsabs.harvard.edu/cgi-bin/nph-iarticle_query?bibcode=1990ApJ...354L..37M) measured the spectrum at $T = 2.725 \pm 0.001$ K — the most perfect blackbody ever observed in nature. The 2006 [Nobel Prize](https://www.nobelprize.org/prizes/physics/2006/summary/) recognized Mather and Smoot for it.

**Pillar 3: primordial light-element abundances.** In the first three minutes, the universe was hot enough for nuclear fusion but only briefly. Starting from a thermal soup at $10^{10}$ K with neutron-to-proton frozen near 1:6, the physics predicts ~25% helium-4 by mass, 75% hydrogen, deuterium at $\sim 2.5 \times 10^{-5}$ relative to hydrogen, and trace lithium-7. Measurements in the oldest gas clouds match helium and deuterium within uncertainty. (Lithium-7 disagrees by about a factor of three — the [lithium problem](https://arxiv.org/abs/1203.3551) — unresolved. The major isotopes agree.)

Three observations from different physical regimes — galaxy motions now, photons last scattered at 380,000 years, isotope ratios set in the first three minutes — give one consistent history. The convergence is the argument.

### The deep dive: why the CMB blackbody spectrum at 2.725 K is the smoking gun

Here is where the chapter slows down and unpacks one mechanism properly.

A blackbody spectrum (Chapter 3) is what a perfect absorber and emitter at temperature $T$ radiates: a specific intensity-versus-wavelength curve depending only on $T$. Nothing else — not composition, not geometry, not history. Only objects in thermal equilibrium with their radiation field produce a pure Planck spectrum. Stars are close but not perfect; absorption lines carve dark gouges into the continuum. The cleanest natural blackbody we know is the CMB — a thousand times more perfectly blackbody than any star. That fact is the smoking gun.

The Big Bang model says: in the first 380,000 years, matter and radiation were locked in thermal equilibrium. Photons could not travel far before scattering off a free electron. In thermal equilibrium, that radiation *must* have a pure blackbody spectrum — that is the definition for a photon gas. Then the universe cooled below 3,000 K, electrons and protons combined into neutral hydrogen, photons stopped scattering, and the radiation streamed freely. The universe expanded by a factor of about 1,100 since. Expansion stretches each photon's wavelength by the same factor — a blackbody at $T$ in a box expanding by factor $a$ becomes a blackbody at $T/a$. The Planck shape is preserved exactly.

The prediction was stringent. The leftover radiation had to be (a) a *perfect* blackbody, (b) at a temperature of a few Kelvin, (c) isotropic, and (d) cooler than any local astrophysical source. Penzias and Wilson confirmed (b), (c), and (d) in 1965 at one frequency, but could not test (a). The blackbody prediction was the riskiest part of the model: astrophysical sources can fake a thermal spectrum at one frequency by accident, but matching the Planck curve across decades of wavelength is essentially impossible unless the radiation really did come from thermal equilibrium.

In 1990 COBE's FIRAS tested (a) with [extraordinary precision](https://articles.adsabs.harvard.edu/cgi-bin/nph-iarticle_query?bibcode=1990ApJ...354L..37M), measuring from 0.5 to 5 mm — straight across the Planck peak. Residuals were consistent with zero at one part in $10^4$. The error bars on the published plot are smaller than the line width. Mather described unveiling the spectrum at an AAS meeting and getting a standing ovation.

Wien's law check. For $T = 2.725$ K:

$$\lambda_{\text{peak}} = \frac{b}{T} = \frac{2.9 \times 10^{-3} \text{ m·K}}{2.725 \text{ K}} \approx 1.06 \text{ mm}$$

The peak is at about a millimeter — which is why Penzias and Wilson detected it with a radio antenna, not an optical telescope.

The blackbody match is the smoking gun because no other model predicts it. A steady-state cosmos (Hoyle, into the 1960s) has no mechanism to produce a precise thermal field filling all of space. Starlight is dramatically non-thermal — absorption lines, emission lines, dust reddening, synchrotron — none of which survives integration into a clean blackbody. Only a universe that was once hot, dense, and in thermal equilibrium leaves behind a Planck spectrum to within $10^{-4}$. The model was tested at its riskiest point, and it held. [WMAP](https://wmap.gsfc.nasa.gov/) and [Planck](https://arxiv.org/abs/1807.06209) later mapped temperature fluctuations of one part in $10^5$ across the sky, extracting the acoustic-peak pattern that encodes composition and geometry. Each measurement was a fresh test the model could have failed and didn't.

### Dark energy and the accelerating universe

One more piece, because the modern Big Bang picture is not the picture of 1965.

In 1998 two independent teams — the [Supernova Cosmology Project](https://arxiv.org/abs/astro-ph/9812133) led by Saul Perlmutter, and the [High-Z Supernova Search Team](https://arxiv.org/abs/astro-ph/9805201) led by Brian Schmidt and Adam Riess — measured the brightness of Type Ia supernovae at redshifts up to $z \approx 0.8$. Type Ia supernovae are standard candles (their intrinsic peak luminosity is calibratable to within ~10%), so measured brightness gives distance and redshift gives velocity. Both teams expected to find expansion slowing under gravity. Both found the opposite: expansion is *accelerating*. The 2011 [Nobel Prize](https://www.nobelprize.org/prizes/physics/2011/summary/) recognized this.

Acceleration requires some component with negative pressure — *dark energy*. The simplest model is Einstein's cosmological constant $\Lambda$. Combined with CMB acoustic peaks (which constrain total energy density and geometry), the modern accounting is:

$$\Omega_\text{baryon} \approx 0.05, \quad \Omega_\text{dark matter} \approx 0.27, \quad \Omega_\Lambda \approx 0.68$$

Ordinary matter — every atom in every star, planet, and person — is 5% of the energy budget. The rest is two kinds of something we cannot see and do not understand. Treat that as how much remains to learn.

---

## Worked example: how old is the universe, really?

The crude estimate is $T_0 \approx 1/H_0$. Let's run it carefully.

Start with $H_0 = 70 \text{ km/s/Mpc}$. One megaparsec is $3.086 \times 10^{22}$ m, so:

$$H_0 = \frac{70 \times 10^3 \text{ m/s}}{3.086 \times 10^{22} \text{ m}} = 2.27 \times 10^{-18} \text{ s}^{-1}$$

Hubble's constant has units of inverse time — the first hint that $1/H_0$ is a timescale.

$$\frac{1}{H_0} = 4.41 \times 10^{17} \text{ s}$$

One year is $3.156 \times 10^7$ s, so:

$$\frac{1}{H_0} \approx 1.40 \times 10^{10} \text{ yr} = 14.0 \text{ billion years}$$

Compare to the careful answer from CMB measurements: $13.797 \pm 0.023$ billion years from [Planck 2018](https://arxiv.org/abs/1807.06209). The crude estimate is off by about 1.5%.

Why so close? $1/H_0$ would be the exact age if expansion rate had always been $H_0$. The actual history has two corrections pulling opposite ways. For the first ~9 billion years, gravity dominated and expansion was slower; that makes the universe *older* than $1/H_0$ suggests. For the last ~5 billion years, dark energy has accelerated expansion; that pushes the estimate the other way. For the actual $\Omega_m \approx 0.3$, $\Omega_\Lambda \approx 0.7$ mix we live in, the two corrections nearly cancel. The coincidence is not deep — a universe with very different parameters would have $1/H_0$ off the true age by 50% or more. The lesson: $1/H_0$ is a useful order-of-magnitude shortcut; agreement to 2% is a consistency check on the standard model, not an exact derivation.

---

## Common misconceptions

- **"The Big Bang was an explosion in space."** It was an expansion *of* space. An explosion happens at a location and propagates through a pre-existing medium. The Big Bang happened everywhere at once, and the subsequent expansion is the stretching of space itself. No center, no edge, no outside.
- **"Galaxies are moving through space at the recession velocity."** Mostly no. Galaxies have small "peculiar velocities" of a few hundred km/s from local dynamics, but the bulk of their recession is space stretching between us and them. This is why distant galaxies can have apparent recession velocities greater than $c$ — the metric expansion is not a velocity *through* space and is not bounded by $c$.
- **"We can see all the way back to the Big Bang."** No. The universe was opaque for its first 380,000 years. The CMB is the oldest light we can see, but it is light from 380,000 years after the beginning, not the beginning itself. Gravitational waves and neutrinos can in principle carry information from earlier epochs.
- **"The universe has an edge somewhere."** No edge has been observed and the model has no need for one. The *observable* universe has a boundary, but it moves outward at $c$ and is specific to our vantage point.

---

## Exercises

**Warm-up (Understand).** A galaxy in the Virgo cluster is about 16.5 Mpc away. (a) Using $H_0 = 70 \text{ km/s/Mpc}$, predict its recession velocity. (b) Using the non-relativistic Doppler relation $\Delta\lambda/\lambda = v/c$, predict the redshift of its hydrogen-alpha line (rest wavelength 656.3 nm).

**Application (Apply).** The CMB has $T = 2.725$ K today. The universe has expanded by a factor of about 1,100 since recombination, so $T$ at recombination was $\sim 2.725 \times 1100 \approx 3{,}000$ K. (a) Use Wien's law to find the peak wavelength of the CMB *at recombination*. (b) Confirm that this wavelength lies in the visible/near-infrared band. (c) Explain in one sentence why this means the universe was glowing dimly red just before it became transparent.

**Synthesis (Analyze).** Big Bang nucleosynthesis predicts a helium-4 mass fraction of about 25% in the oldest gas. (a) Why is this prediction not affected by stellar helium production? (b) Why measure helium in *metal-poor* environments rather than the solar neighborhood? (c) What independent observation pins down the same baryon density?

**Challenge (Analyze).** Planck CMB gives $H_0 = 67.4 \pm 0.5 \text{ km/s/Mpc}$. The [SH0ES local distance ladder](https://arxiv.org/abs/2112.04510) gives $H_0 = 73.0 \pm 1.0$. (a) Compute the disagreement in standard deviations, treating errors as independent Gaussians. (b) State one systematic that, if wrong, would push SH0ES down. (c) State one new physical effect that, if real, would push Planck up. (d) Explain why the disagreement matters even though it is only a 5% effect.

---

## LLM Exercises

### Build the Hubble diagram + CMB blackbody simulator (`13-hubble-cmb.html`)

With `CLAUDE.md` and `DESIGN.md` loaded:

> **Show.** A two-panel D3 v7 visualization. Left: a Hubble diagram with recession velocity (km/s) vs. distance (Mpc), populated with real Type Ia supernova data from the [Pantheon+ sample](https://github.com/PantheonPlusSH0ES/DataRelease), and a slider-controlled best-fit line $v = H_0 d$. Display residual sum of squares so the user can fit by eye. Right: the CMB blackbody spectrum $B_\lambda(T)$ at $T = 2.725$ K from 0.1 to 10 mm, with [COBE FIRAS](https://lambda.gsfc.nasa.gov/product/cobe/firas_overview.html) data overlaid and a slider varying $T$ from 1 to 5 K. Annotate the Wien peak dynamically.
>
> **Say.** Use $B_\lambda(T) = (2hc^2/\lambda^5) \cdot 1/(e^{hc/\lambda k_B T} - 1)$. For the Hubble panel, distance moduli convert to Mpc via $d = 10^{(m - M + 5)/5}$ pc. Show $H_0$ and $1/H_0$ (in Gyr) next to the slider.
>
> **Constrain.** D3 v7 only. Filename: `13-hubble-cmb.html`. Sliders update in real time.
>
> **Verify.** (a) $H_0 = 70$ minimizes the Hubble residual. (b) $T = 2.725$ K gives a Wien peak at ~1.06 mm. (c) $T = 2.000$ K moves the peak to ~1.45 mm. (d) $T = 5.000$ K moves it to ~0.58 mm — well outside the FIRAS data.

### Exploration

- Drag $H_0$ from 60 to 80 km/s/Mpc and watch $1/H_0$ change from 16.3 to 12.2 Gyr. The careful answer (13.8 Gyr) sits inside this range — but the spread is the full span of the Hubble tension.
- On the CMB panel, push $T$ to 3 K. The curve overshoots the FIRAS points by many standard deviations. Try 2.726 and 2.724 K — FIRAS constrains $T$ to milliKelvin precision.

### Bridge to Chapter 14

> **Show.** The universe is 13.8 billion years old, expanding, and contains roughly $10^{24}$ stars. Most of those stars host planets. The remaining question is the one Fermi asked at lunch in 1950: *if all this physics is universal, where is everybody?*
>
> **Say.** Add a third panel showing the [Drake equation](https://www.seti.org/drake-equation-index) with sliders for each of its seven factors, computing $N$ (the expected number of communicating civilizations in the Milky Way) in real time.

Save as `13b-drake-equation-preview.html`. Lead-in to Chapter 14 — *Life in the Universe*.

---

## What would change my mind

The CMB blackbody spectrum is the load-bearing piece. A reproducible measurement of a systematic *departure from the Planck curve at one part in $10^3$ or larger*, after every known foreground (galactic dust, free-free, synchrotron) is subtracted and confirmed by an independent instrument, would force a fundamental rewrite. The current best limit from [COBE FIRAS](https://articles.adsabs.harvard.edu/cgi-bin/nph-iarticle_query?bibcode=1996ApJ...473..576F) constrains $\mu$- and $y$-type distortions below $\sim 10^{-5}$. The proposed [PIXIE](https://arxiv.org/abs/1105.2044) and [LiteBIRD](https://arxiv.org/abs/2202.02773) missions aim to push this another two orders of magnitude. A second mind-changer: a primordial helium-4 fraction measured at 12% or 38% rather than 25%. A factor-of-two miss would mean Big Bang nucleosynthesis has the wrong input physics, which would mean the early-universe thermal history is wrong somewhere fundamental.

## Still puzzling

- *The Hubble tension.* The [Planck 2018 CMB value](https://arxiv.org/abs/1807.06209) $H_0 = 67.4 \pm 0.5 \text{ km/s/Mpc}$ disagrees with the [SH0ES 2022 local distance ladder](https://arxiv.org/abs/2112.04510) value $H_0 = 73.0 \pm 1.0$ at about $5\sigma$. Either one method has an unidentified systematic, or $\Lambda$CDM is missing a physics ingredient that affects early- and late-universe expansion measurements differently. JWST rechecks are ongoing.
- *What dark energy actually is.* "A cosmological constant" is a phenomenological description; "an energy density of empty space" is a restatement, not a mechanism. Quantum field theory's naïve estimate of the vacuum energy density is wrong by [120 orders of magnitude](https://link.aps.org/doi/10.1103/RevModPhys.61.1).
- *What triggered inflation.* The early universe appears to have undergone a brief epoch of exponential expansion that ironed out wrinkles and set initial conditions for the hot Big Bang. The observational case is strong (flatness, isotropy, the CMB angular spectrum). The physical mechanism — what field, what potential — is unsettled. A clean detection of primordial B-mode polarization in the CMB would be the cleanest discriminator.

---

**Tags:** Big Bang, Hubble's law, cosmic microwave background, Penzias and Wilson, Lemaître, COBE FIRAS, nucleosynthesis, dark energy, Hubble tension, $\Lambda$CDM
