# Chapter 7 — Stellar Distances and the Cosmic Distance Ladder

*A Königsberg observatory in 1838, a star that shifted by less than a thousandth of a degree, and the geometric measurement on which every distance in the universe still rests.*

---

In late 1838 Friedrich Wilhelm Bessel, director of the Königsberg Observatory, published a number that astronomers had been failing to measure for two centuries. The star 61 Cygni — a faint double star, chosen because its unusually large proper motion hinted it was nearby — shifted against the background as Earth moved around the Sun. The shift was 0.314 arcseconds of half-angle. That is roughly the angle subtended by a tennis ball viewed from 40 kilometers away.

Tycho Brahe had searched for exactly this shift in the late sixteenth century, with the finest naked-eye instruments ever built. He found nothing and concluded — confidently and incorrectly — that Earth must be stationary. His instruments were not good enough by a factor of about a hundred. Bessel had a Fraunhofer heliometer and years of practice comparing 61 Cygni against two faint background stars across many months. He published the distance: roughly 10.3 light-years, within 10% of the modern value of 11.4 light-years.

![Top-down view of Earth orbiting the Sun with sight lines to 61 Cygni at January and July positions. The star's apparent position shifts 0.628 arcseconds against background reference stars; the parallax is half of that...](../images/07-stellar-distances-fig-01.png)
*Figure 7.1 — Bessel's 1838 Parallax Measurement of 61 Cygni*

That number is the foundation of everything that follows in this chapter. Every distance in modern astronomy — to Andromeda, to the Coma Cluster, to supernovae 5 billion light-years away — traces back, through a chain of calibrations, to Bessel's angle. The chain is called the cosmic distance ladder, and it is powerful for exactly the reason it is dangerous: every rung is anchored on the rung below it. Errors at the bottom are carried forward, amplified, and eventually expressed as a genuine disagreement about the size and expansion rate of the universe. That disagreement — currently at the 5σ level — is what compounding errors look like when the ladder is tall enough.

![Four rungs, each calibrated against the rung below. Parallax is the only purely geometric rung. Cepheid variables extend to ~10 Mpc. Type Ia supernovae extend to billions of light-years. Hubble flow extends to the obs...](../images/07-stellar-distances-fig-02.png)
*Figure 7.2 — The Cosmic Distance Ladder: Four Rungs*

---

## The bottom rung: parallax

Hold up a finger and alternately close one eye, then the other. The finger shifts against the background. The shift is the parallax — two sightlines from different positions converging on the same object, arriving from different angles.

Scale this to astronomy. As Earth orbits the Sun, our vantage point shifts by up to 2 AU — the full diameter of the Earth's orbit. A nearby star, viewed against the fixed backdrop of vastly more distant stars, appears to move in a small ellipse over the year. The **parallax** $p$ is defined as *half* the total angular shift — the angle subtended at the star by a baseline of 1 AU.

From small-angle geometry (the baseline is 1 AU, the distance is $D$, and the angle is small enough that $\tan p \approx p$):

$$p\,\text{(radians)} = \frac{1\,\text{AU}}{D}$$

Convert to arcseconds and define one **parsec** as the distance at which a star shows $p = 1$ arcsecond, and the formula becomes:

$$D\,\text{(parsecs)} = \frac{1}{p\,\text{(arcsec)}}$$

Proxima Centauri, the nearest star to the Sun, has the largest stellar parallax: 0.769 arcseconds — a distance of 1.30 parsecs, or 4.24 light-years.

What makes parallax the bedrock of the entire ladder is what it does *not* require. No assumption about the star's luminosity, temperature, composition, or age. No physical model of how stars work. You measure an angle and the size of Earth's orbit — the latter known to nine significant figures from radar ranging of the inner solar system. The distance is then pure geometry. Parallax is the one rung of the ladder that rests on nothing but space and arithmetic.

The cost is reach. Earth's atmosphere blurs images, setting a practical floor on the smallest angles measurable from the ground at around 0.01 arcseconds, corresponding to 100 parsecs. The Hipparcos satellite (1989–1993) extended reliable parallax to about 0.001 arcseconds for 120,000 stars. Gaia, launched in 2013, achieves 20 to 50 microarcseconds — millionths of a degree — for nearly two billion stars, pushing accurate parallax to several kiloparsecs. Beyond that the angles are smaller than the noise. The geometry runs out, and you need a different idea.

<!-- → [IMAGE: Diagram of stellar parallax geometry — Earth at two positions six months apart (left and right of the Sun), the baseline labeled as 2 AU, lines of sight converging on a nearby star, the parallax angle p labeled at the star; inset showing that 1 parsec is the distance at which p = 1 arcsecond; student should see that larger p means closer star, and why the method fails for distant objects where p becomes unmeasurably small] -->

![Top-down view of the Sun and Earth's 1 AU orbit, with sight lines from two opposite orbital positions to a star at distance D. The parallax angle p is the half-angle subtended at the star by the 1 AU baseline. When p...](../images/07-stellar-distances-fig-03.png)
*Figure 7.3 — Parallax from Earth's Orbit: The Geometric Definition*

---

## What Henrietta Swan Leavitt found

The next rung of the ladder rests on a discovery made by a woman hired to measure photographic plates by the hour.

In the early twentieth century, Harvard College Observatory employed a group of women — called "computers" — to catalogue the vast number of stellar photographs being taken. Henrietta Swan Leavitt was assigned the variable stars in the Magellanic Clouds, two satellite galaxies of the Milky Way visible from the Southern Hemisphere. By 1908 she had catalogued 1,777 variables; by 1912 she had spotted a pattern in a particular class of them.

These were Cepheid variables — pulsating stars that brighten and dim with a characteristic rhythm — and Leavitt noticed that the ones with longer periods were systematically brighter. More precisely: plot the logarithm of the period on one axis and the average apparent magnitude on the other, and a straight line falls through the points.

The Magellanic Cloud was crucial to recognizing what this meant. All the stars in the Cloud sit at essentially the same distance from Earth. Differences in their apparent brightness therefore reflect differences in their actual luminosity. The period-brightness relation Leavitt saw was not a coincidence of viewing angle — it was a period-luminosity relation, built into the physics of the stars themselves.

Leavitt had no way to calibrate the zero point. Her relation told her that a 30-day Cepheid is intrinsically brighter than a 10-day Cepheid by a certain number of magnitudes. It did not tell her how bright either was in absolute terms, because she did not know the distance to the Magellanic Cloud. That calibration required at least one Cepheid whose distance was known by other means — preferably parallax.

The calibration took time and was done imprecisely at first, well later. Today, Gaia parallaxes of Milky Way Cepheids anchor the zero point precisely. The calibrated relation, in the visual band, is approximately:

$$M_V \approx -2.43\,\log_{10}\!\left(\frac{P}{10\,\text{days}}\right) - 4.05$$

A 30-day Cepheid has $M_V \approx -5.2$ — about 12,000 times the luminosity of the Sun. Bright enough to be detected and measured in a galaxy 10 megaparsecs away.

The physical reason Cepheids pulsate, and why larger Cepheids pulsate more slowly, is a question of stellar structure — the outer layers of these stars are caught in an ionization cycle that alternately traps and releases radiation pressure, driving a periodic expansion and contraction. The longer the period, the more massive and luminous the star — a deep consequence of how stellar physics scales with mass. The period-luminosity relation is not empirical coincidence; it has a physical explanation. But you do not need that explanation to use it as a distance tool. What Leavitt gave astronomers was a clock in the sky whose tick rate reveals the clock's wattage.

<!-- → [CHART: Leavitt's period-luminosity relation — scatter plot with log₁₀(period in days) on x-axis and absolute magnitude M_V on y-axis (inverted, brighter up); points falling along a tight straight line; the calibrated slope −2.43 labeled; benchmarks marked: 10-day Cepheid at M ≈ −0.5, 30-day Cepheid at M ≈ −5.2; caption should note that each point is a real pulsating star and the line is calibrated by Gaia parallaxes of Milky Way Cepheids] -->

![Two panels. Left: Leavitt's 1908 plot of Small Magellanic Cloud Cepheids — period vs apparent magnitude — shows a tight linear relation because the stars are at one distance. Right: the modern calibrated period vs abs...](../images/07-stellar-distances-fig-04.png)
*Figure 7.4 — Leavitt's Period-Luminosity Discovery from the SMC*

---

## The standard-candle idea, in general

The Cepheid is the most important example of a general strategy. When you cannot measure a distance geometrically, you find an object whose luminosity you already know — or can infer from some observable property — and apply the inverse-square law.

If the luminosity is $L$ and the measured brightness at your telescope is $b$, then:

$$b = \frac{L}{4\pi d^2} \implies d = \sqrt{\frac{L}{4\pi b}}$$

Measure $b$, know $L$, get $d$. An object whose $L$ is known is a **standard candle**.

Astronomers express this in logarithmic units because astrophysical brightnesses span twenty orders of magnitude and logarithms keep the numbers civil. The **apparent magnitude** $m$ is a logarithmic measure of observed brightness; the **absolute magnitude** $M$ is the apparent magnitude the object would have at exactly 10 parsecs. Their difference is the **distance modulus**:

$$m - M = 5\,\log_{10}\!\left(\frac{d}{10\,\text{pc}}\right)$$

A larger distance modulus means a farther object. This is the inverse-square law in log dress. All the physics is in $M$; all the observation is in $m$; the distance falls out of the difference.

<!-- → [CHART: Distance modulus m−M vs. distance d on a log scale from 1 pc to 10,000 Mpc — a straight line with slope 5 on the log-log axes; tick marks on the d-axis labeled with recognizable benchmarks: nearest star (1.3 pc), Pleiades (136 pc), Galactic center (8.5 kpc), Andromeda (770 kpc), Virgo Cluster (16.5 Mpc), most distant SNe Ia (~6,000 Mpc); student should see the span of the ladder and where each method reaches] -->

---

## The third rung: Type Ia supernovae

Cepheids are bright enough to reach about 30 megaparsecs with the Hubble Space Telescope. Beyond that they cannot be resolved individually in the crowded stellar fields of distant galaxies. The third rung uses something catastrophically brighter.

A Type Ia supernova is the thermonuclear detonation of a white dwarf — the collapsed, burned-out core of a star like the Sun — that has been accumulating mass from a companion until it approaches the Chandrasekhar limit, about 1.4 solar masses. At that mass the electron degeneracy pressure supporting the dwarf can no longer resist gravity. The core collapses briefly, a runaway fusion reaction ignites throughout the white dwarf, and the entire star explodes in a few seconds. For weeks it outshines its entire host galaxy — releasing roughly $10^{44}$ joules, about a hundred times the total energy the Sun will radiate over its entire life.

Because the explosion is triggered at nearly the same mass every time — set by fundamental physics, not the idiosyncrasies of the particular star — the peak luminosities of Type Ia supernovae are similar across different events, in different galaxies, at different redshifts. Not identical: there is intrinsic scatter. But in 1993 Mark Phillips noticed that the scatter is not random. Supernovae that are intrinsically more luminous at peak also fade more slowly; dimmer ones fade faster. The light-curve width encodes the luminosity. Apply the Phillips correction — standardize the brightness using the decline rate — and the residual scatter is about 10% in luminosity. A standardizable candle, not a perfect one.

![Three panels. Left: a carbon-oxygen white dwarf accretes mass from a companion toward the Chandrasekhar limit and detonates. Middle: raw Type Ia light curves show significant peak-brightness scatter. Right: the Philli...](../images/07-stellar-distances-fig-05.png)
*Figure 7.5 — Type Ia Supernovae and the Phillips Relation*

How is the Type Ia rung calibrated? By finding Type Ia supernovae in galaxies that *also* contain Cepheids. The Cepheids give the galaxy's distance; knowing the distance converts the supernova's apparent peak brightness into an absolute magnitude. The SH0ES project has done this calibration in 42 host galaxies — 42 anchor points for the Type Ia absolute magnitude scale.

The reach of the Type Ia rung is enormous. A supernova that outshines a galaxy of 100 billion stars is visible at cosmological distances, where the Cepheids are entirely unresolvable. This is how the 1998 measurement that discovered cosmic acceleration was made — Type Ia supernovae in galaxies at redshifts up to $z \sim 1$, a few billion light-years away, were fainter than expected for a decelerating universe, and the inference was that the expansion of space is speeding up.

<!-- → [CHART: Type Ia supernova light curve — two panels side by side; left: raw light curves for a bright slow-fading SN Ia and a dim fast-fading SN Ia, both showing peak then decline over ~60 days; right: the same two curves after Phillips correction (stretch/decline-rate normalization), now overlapping to within ~10%; caption should make clear that the correction uses only the shape of the light curve — no knowledge of distance required — and that the standardized peak magnitude is what becomes the distance indicator] -->

---

## The compounding problem

Here is the structural problem with a ladder.

Each rung is calibrated against the rung below it. Parallax anchors Cepheids. Cepheids anchor Type Ia supernovae. Type Ia supernovae anchor the Hubble flow. Any systematic error at rung $n$ is inherited by rung $n+1$, and carried forward through every rung above it.

If parallax is systematically off by 2%, the Cepheid luminosities are off by 2%. If the Cepheid calibration introduces its own scatter (it does — the period-luminosity relation has scatter around the best-fit line, partly from metallicity differences between Milky Way Cepheids and those in other galaxies), that adds to the parallax error in quadrature. If the Type Ia Phillips correction introduces its own uncertainty, that adds too. And so on.

Fractional errors add in quadrature when they are independent:

$$\left(\frac{\sigma_d}{d}\right)^2_{\rm total} = \left(\frac{\sigma_d}{d}\right)^2_{\rm parallax} + \left(\frac{\sigma_M}{M}\right)^2_{\rm Cepheid} + \left(\frac{\sigma_M}{M}\right)^2_{\rm SN\,Ia} + \cdots$$

<!-- → [INFOGRAPHIC: Four-rung ladder diagram — each rung labeled with its method and typical fractional uncertainty: parallax ~1% (Gaia), Cepheid PL ~5%, Type Ia Phillips ~5%, Hubble flow ~2%; cumulative uncertainty bars growing at each rung by quadrature addition; final bar labeled "H₀ from SH0ES: ~7% before averaging"; caption should show that averaging over many objects per rung reduces the uncertainty, and SH0ES achieves ~1.4% by doing this on 100+ objects per rung] -->

![Bar chart showing cumulative fractional uncertainty at each rung of the distance ladder. Each rung adds its own uncertainty in quadrature: parallax 1%, Cepheid PL 5%, Type Ia 5%, Hubble flow 2%. Cumulative running tot...](../images/07-stellar-distances-fig-06.png)
*Figure 7.6 — Compounding Errors in Quadrature*

The SH0ES collaboration has reduced the cumulative uncertainty to 1.4% by averaging over large numbers of objects at each rung — hundreds of Cepheids per galaxy, dozens of calibrated Type Ia host galaxies, hundreds of Hubble-flow supernovae. Their result: $H_0 = 73.04 \pm 1.04$ km/s/Mpc, where $H_0$ is the current expansion rate of the universe.

An independent route gives a different answer. The Planck satellite measured the cosmic microwave background — the thermal radiation left over from when the universe was 380,000 years old — to exquisite precision. Fitting those temperature and polarization fluctuations with a six-parameter cosmological model extrapolates forward in time to the present expansion rate: $H_0 = 67.4 \pm 0.5$ km/s/Mpc. The two results disagree by about 5.7 km/s/Mpc — roughly 9% — at a statistical significance of about 5σ.

This is the **Hubble tension**.

---

## What the Hubble tension actually is

I want to be precise about what is being compared, because the comparison is subtler than it looks.

SH0ES measures the expansion rate directly and locally. Take a galaxy at known distance $d$ (from the ladder) and measure its recession velocity $v$ from the Doppler redshift of its spectral lines. $H_0 = v/d$. Do this for many galaxies in the nearby Hubble flow — far enough that peculiar velocities (galaxies' individual gravitational motions) are small compared to the Hubble flow, close enough that cosmological evolution is negligible. Average. You get the expansion rate of the universe *today*.

Planck does not measure $H_0$ directly. It measures the angular power spectrum of the CMB — how much temperature variation there is at different angular scales on the sky — and fits it to a six-parameter model of cosmology (matter density, baryon density, dark energy equation of state, and so on). The best-fit model has an expansion rate of 67.4 km/s/Mpc. That is the expansion rate the *model* implies for today, given the early-universe initial conditions.

So the comparison is: the expansion rate as measured directly with rulers and clocks *today*, versus the expansion rate predicted by a model calibrated to the universe when it was 380,000 years old. The disagreement means one of three things:

There is a systematic error somewhere in the local ladder — an error that has survived repeated checking, across multiple groups, over twenty years. It would have to conspire across all rungs to produce the same bias.

The cosmological model is missing something — new physics in the early universe that altered the sound horizon (the physical scale the CMB fluctuations are measuring), or new dark-sector physics, or evolving dark energy. Several models have been proposed; none is compelling enough to have won community consensus.

The two analyses are not being compared to a common framework correctly — a possibility that is harder to dismiss than it sounds, because the CMB measurement involves a long chain of model assumptions that the local measurement does not.

My reading is that the tension is real. The evidence against a single-rung systematic is that independent distance methods — the Tip of the Red Giant Branch method (TRGB), gravitational-wave standard sirens, megamaser geometric distances — do not all converge on Planck's value. The TRGB result sits at roughly 69 to 70 km/s/Mpc, between the two camps. The gravitational-wave constraint from GW170817 is consistent with either at current precision. If those independent methods settle, and they converge toward Planck, SH0ES has a systematic. If they converge toward SH0ES, the cosmological model is incomplete.

Either outcome matters. If the ladder is wrong, we need to understand why our best calibrations failed. If the model is wrong, we are missing something fundamental about the early universe. The ladder is working as intended — carrying errors faithfully forward until they become visible enough to argue about.

<!-- → [TABLE: Summary of H₀ measurements — columns: Method, H₀ value (km/s/Mpc), Uncertainty, Type (direct/model); rows: SH0ES Cepheid+SN Ia (73.04 ± 1.04, direct), Planck CMB (67.4 ± 0.5, model-extrapolated), TRGB Freedman et al. (~69.8 ± 1.9, direct), GW170817 standard siren (~70 ± 12, direct); caption should note that the "direct" measurements span a range and that the siren measurement's large uncertainty currently cannot adjudicate the tension] -->

---

## A worked example: from parallax to a galaxy distance

Suppose you observe a Cepheid in a nearby galaxy. You have two pieces of information.

A calibrator Cepheid in the Milky Way has a Gaia parallax of 2.50 milliarcseconds, an apparent magnitude of $m = 7.50$, and a period of 10 days. A Cepheid in the target galaxy has the same 10-day period and an apparent magnitude of $m_{\rm tgt} = 22.50$.

**Step 1: distance to the calibrator.** Parallax of 2.50 milliarcseconds = 0.00250 arcseconds. Distance $= 1/0.00250 = 400$ pc.

**Step 2: absolute magnitude of a 10-day Cepheid.** Distance modulus of the calibrator:

$$m - M = 5\,\log_{10}\!\left(\frac{400\,\text{pc}}{10\,\text{pc}}\right) = 5\,\log_{10}(40) \approx 8.01$$

$$M = 7.50 - 8.01 = -0.51$$

A 10-day Cepheid has absolute magnitude $-0.51$, calibrated to this parallax.

**Step 3: distance to the target galaxy.** The target Cepheid has the same period, so the same $M = -0.51$. Its apparent magnitude is 22.50.

$$m - M = 22.50 - (-0.51) = 23.01$$

$$d = 10\,\text{pc} \times 10^{23.01/5} = 10\,\text{pc} \times 10^{4.602} \approx 4.0 \times 10^5\,\text{pc} = 400\,\text{kpc}$$

About 1.3 million light-years — roughly the distance to Andromeda. Two observables — one angle, one period — and an inverse-square law dressed in logarithms.

**The error propagation.** If Gaia's parallax is good to 1% and the Cepheid period-luminosity relation contributes 5% scatter to the inferred $M$, then the fractional error on the target distance is:

$$\frac{\sigma_D}{D} \approx \sqrt{(0.01)^2 + (0.05)^2} \approx 0.051$$

About 5% from a single Cepheid. Measure 50 Cepheids in the same galaxy and the scatter contribution falls by $\sqrt{50}$, leaving the parallax error as the floor. This is the engineering of the SH0ES project: drive down statistical error by accumulating many objects at every rung, while hunting for the systematics that set the floor.

---

## What would change my mind

I think the Hubble tension is real — not a statistical fluctuation and not obviously explained by a single systematic. What would make me revise that: if an independent local measurement avoiding Cepheids entirely converged on Planck's 67.4 km/s/Mpc with precision comparable to SH0ES. The gravitational-wave standard-siren method is the cleanest candidate: the waveform of a binary merger encodes the luminosity distance directly from general relativity, requiring no calibration against any other rung. GW170817 gave a single event with large uncertainty. A catalog of tens of well-measured binary neutron-star mergers — which LIGO's next observing runs should begin to build — would settle whether the siren $H_0$ lands near 67 or near 73. If it lands near 67, the ladder has a hidden systematic. If it lands near 73, the standard cosmological model is missing something real.

![Two probability distributions for H_0. SH0ES (local distance ladder) is centered at 73.04 with sigma 1.04. Planck (CMB early universe) is centered at 67.4 with sigma 0.50. Gap 5.6 km/s/Mpc; combined sigma 1.15; tensio...](../images/07-stellar-distances-fig-07.png)
*Figure 7.7 — The Hubble Tension: SH0ES vs Planck*

---

## Exercises

**Warm-up.** A star has a parallax of 0.050 arcseconds. (a) Convert to distance in parsecs using $D = 1/p$. (b) Convert to light-years. (c) State in one sentence what additional measurement you would need to determine this star's luminosity from its apparent brightness. *(Tests: parallax formula, pc-to-ly conversion, distinction between apparent brightness and luminosity.)*

**Warm-up.** A star has apparent magnitude $m = 8.5$ and absolute magnitude $M = 3.5$. (a) Compute the distance modulus. (b) Solve for the distance in parsecs. (c) If a second star has the same apparent magnitude but is twice as far away, what is its absolute magnitude? *(Tests: distance modulus formula, solving for d, inverse-square law in magnitude form.)*

**Warm-up.** Explain in plain language why parallax is described as "assumption-free" relative to Cepheid distances. What physical quantity does parallax measure directly, and what does it *not* require you to know about the star? *(Tests: conceptual distinction between geometric and standard-candle distances.)*

**Application.** A Cepheid variable in a distant galaxy has a pulsation period of 30 days and an apparent magnitude of $m = 24.8$. Using the calibrated relation $M_V \approx -2.43\,\log_{10}(P/10\,\text{days}) - 4.05$: (a) compute $M_V$ for this Cepheid, (b) compute the distance modulus $m - M$, (c) compute the distance in megaparsecs. *(Tests: applying the period-luminosity relation, distance modulus, converting parsecs to Mpc.)*

**Application.** A Type Ia supernova reaches peak apparent magnitude $m = 16.5$ in a galaxy whose Cepheid distance is 15 Mpc. (a) Compute the distance modulus to this galaxy. (b) Compute the absolute magnitude $M$ of the supernova at peak. (c) A second Type Ia supernova in a galaxy with no Cepheid measurement has the same peak $M$ (after Phillips correction) and apparent magnitude $m = 21.0$. What is the distance to the second galaxy in Mpc? *(Tests: using a nearby calibrated SN Ia to bootstrap a distance to a more distant galaxy — the core SH0ES logic.)*

**Synthesis.** Suppose Gaia discovers a systematic error in its parallax zero point: all measured parallaxes are 2% too large (stars appear 2% closer than they are). (a) By what percentage are all Cepheid absolute magnitudes affected? State the sign: are they reported as brighter or dimmer than reality? (b) How does this propagate to the Type Ia absolute magnitude calibration? (c) What happens to the inferred value of $H_0$ — does it increase or decrease, and by roughly how much? Show the chain of reasoning. *(Tests: systematic error propagation through the ladder, sign of the effect on H₀.)*

**Synthesis.** The Hubble tension. SH0ES reports $H_0 = 73.04 \pm 1.04$ km/s/Mpc; Planck reports $H_0 = 67.4 \pm 0.5$ km/s/Mpc. (a) Compute the difference in km/s/Mpc and the combined uncertainty (add the two error bars in quadrature). (b) Express the disagreement as a number of standard deviations. (c) In plain language, explain why these two measurements are not measuring exactly the same thing — what is each actually measuring, and why does the comparison require an assumption? *(Tests: error propagation, significance of tension, distinction between direct measurement and model extrapolation.)*

**Challenge.** The gravitational-wave standard-siren method measures $H_0$ without any calibration chain. The waveform of a binary neutron-star merger encodes the luminosity distance directly from general relativity; the recession velocity comes from the host galaxy's redshift. GW170817 gave $H_0 = 70^{+12}_{-8}$ km/s/Mpc from a single event. (a) With this uncertainty, is the measurement consistent with SH0ES? With Planck? With both? (b) Approximately how many events with the same individual precision would be needed to reduce the uncertainty enough to adjudicate the 5.7 km/s/Mpc tension at 3σ? (c) What makes gravitational-wave standard sirens methodologically different from all other rungs of the distance ladder — what assumption do they *not* require? *(Tests: uncertainty scaling with sample size, reading consistency of overlapping error bars, conceptual independence of GW sirens from the calibration chain.)*

---

## LLM Exercises

### Build the distance-ladder simulator (`07-distance-ladder.html`)

With `CLAUDE.md` and `DESIGN.md` loaded:

> **Show.** A vertical four-rung ladder visualization. Each rung corresponds to one distance method: (1) parallax, (2) Cepheid period-luminosity, (3) Type Ia supernova, (4) Hubble-flow redshift. The user sets a fractional uncertainty for each rung with a slider. A bar to the right of each rung shows the *cumulative* fractional uncertainty after that rung — i.e., the quadrature sum of all rungs up to and including this one. Below the ladder, two horizontal bars compare an inferred $H_0$ value (with cumulative error bar) to the Planck CMB value of $67.4 \pm 0.5$ km/s/Mpc, with the tension expressed in sigmas.
>
> **Say.** Build an interactive D3 v7 visualization. Default slider values: parallax 1%, Cepheid PL 5%, Type Ia 5%, Hubble flow 2%. Cumulative uncertainty after rung $n$ is $\sigma_n = \sqrt{\sum_{i=1}^{n} \sigma_i^2}$. Assume a nominal local $H_0 = 73.04$ km/s/Mpc and propagate the cumulative fractional uncertainty into an absolute uncertainty on $H_0$. Compute tension in sigmas as $|73.04 - 67.4| / \sqrt{\sigma_{\rm SH0ES}^2 + 0.5^2}$.
>
> **Constrain.** D3 v7 only. No external statistics libraries. Filename: `07-distance-ladder.html`. Sliders update the cumulative uncertainty and tension bars in real time.
>
> **Verify.** (a) Default values should yield a cumulative uncertainty near 7.3% and a tension near 5σ. (b) Setting Cepheid PL to 10% should weaken the tension visibly. (c) Setting all rungs to zero should show the tension capped by the Planck error bar alone (about 11σ at $|73.04-67.4|/0.5$).

### Exploration

- Increase the Cepheid PL uncertainty until the tension drops below 3σ. What fractional Cepheid uncertainty does that require? Is that plausible given the Riess et al. 2022 error budget?
- Set parallax uncertainty to 5% (pre-Gaia ground-based precision) and the rest to defaults. By how much does the cumulative uncertainty grow? Does the tension survive at this precision?
- Add a fifth rung labeled "new physics" with its own slider. What fractional shift in the early-universe physics would absorb the entire 6 km/s/Mpc gap without invoking any change in the ladder?

### Bridge to Chapter 8 (Birth of Stars)

> **Show.** Now that distances are in hand, the next step is to use them. Specifically: combine distance with apparent brightness and color to place stars on a Hertzsprung-Russell diagram, and watch where star-forming regions concentrate.
>
> **Say.** Modify the simulator: load a small sample of Gaia DR3 stars within 300 pc, plot them on an HR diagram (color index on the x-axis, absolute magnitude on the y-axis with the axis inverted), and highlight the main sequence, giant branch, and the location of pre-main-sequence stars — the topic of Chapter 8.
>
> **Verify.** Pre-main-sequence stars should sit *above and to the right* of the main sequence — cooler and more luminous than their final main-sequence positions, because they are still contracting and have not yet ignited hydrogen fusion. That offset is the visible signature of star birth.

Save as `07b-hr-diagram-preview.html`. Lead-in to Chapter 8 — *The Birth of Stars*.

---

**Tags:** parallax, Cepheid variables, Henrietta Leavitt, standard candles, distance modulus, Type Ia supernovae, cosmic distance ladder, Hubble constant, Hubble tension, SH0ES, Planck, Gaia
