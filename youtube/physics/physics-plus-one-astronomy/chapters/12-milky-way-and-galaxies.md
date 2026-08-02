# Chapter 12 — The Milky Way and Galaxies

*A telescope in the mountains of Arizona, a spectrograph that took all night to record a single galaxy, and the moment a flat line in a graph forced the universe to be mostly invisible.*

---

## Suggested titles

1. The Milky Way and Galaxies
2. The Shape We Live Inside
3. Reading the Universe by the Mass You Cannot See

## TL;DR

A galaxy is a gravitationally bound assembly of stars, gas, dust, and — overwhelmingly — dark matter. The shapes galaxies wear (spiral, elliptical, irregular) encode their dynamical histories, and the way they rotate forces a conclusion almost nobody welcomed: most of the mass holding them together does not emit light, does not absorb light, and is not made of any known particle.

---

## Learning objectives

By the end of this chapter you will be able to:

1. **(Understand)** Describe the layered structure of the Milky Way — thin disk, thick disk, bulge, halo, dark matter halo — and locate the Sun within it.
2. **(Apply)** Classify a galaxy image into the Hubble sequence (E0–E7, Sa/Sb/Sc, SBa/SBb/SBc, Irr) and infer what its morphology implies about its stellar population and history.
3. **(Apply)** Use $M = v^2 r / G$ to compute the mass enclosed within a given orbital radius from the orbital speed at that radius, and interpret the result physically.
4. **(Analyze)** Read a galactic rotation curve and explain why a flat curve at large radius requires mass distributed beyond the visible disk.
5. **(Apply)** Build an interactive D3 simulation that compares observed vs. Keplerian-predicted rotation curves for a spiral galaxy and lets the user adjust the dark matter halo mass.

**Prerequisites.** Chapter 3 (spectra and the Doppler shift — you measure rotation by measuring redshift). Newton's law of gravity and circular motion ($F = GMm/r^2$, $F = mv^2/r$). Basic algebra. No general relativity required for this chapter; gravity at galactic speeds is well within the Newtonian regime.

---

## Opening case: Vera Rubin's spectrograph, Lowell Observatory, late 1960s

In the late 1960s, Vera Rubin and Kent Ford pointed an image-tube spectrograph at the Andromeda Galaxy from the 72-inch Perkins telescope at Lowell Observatory in Flagstaff, Arizona. The instrument was Ford's own design — a photocathode the size of a thumbnail that amplified faint light by a factor of thousands, making spectra of galaxy outskirts achievable on a single night's exposure rather than a week's. Rubin was after a specific number: how fast does ionized gas orbit the center of Andromeda, as a function of how far it sits from that center?

The textbook expectation was clear. Andromeda's light — its stars, its bulge, its glowing arms — is concentrated toward the center. By Newton's law of gravity, gas orbiting at the edge should feel the pull of essentially the whole galaxy beneath it and should move the way Neptune moves: more slowly than the inner stuff, falling off as roughly $1/\sqrt{r}$ once you are outside most of the mass. Plot orbital speed against radius and you should see a rise, a peak somewhere near where the visible disk ends, and a long Keplerian decline.

Rubin and Ford published their result for Andromeda in 1970 ([Rubin & Ford, 1970, *Astrophysical Journal* 159: 379](https://ui.adsabs.harvard.edu/abs/1970ApJ...159..379R)). The curve rose. It reached about 250 km/s. And then it just kept going. Sixty arcminutes from the center, seventy, eighty — well past the bright disk — the gas was still moving at roughly the same speed. No decline. Through the 1970s Rubin and collaborators repeated the measurement for galaxy after galaxy ([Rubin, Ford & Thonnard, 1980](https://ui.adsabs.harvard.edu/abs/1980ApJ...238..471R)). Every spiral showed the same pattern. The rotation curves were flat.

Fritz Zwicky had seen something analogous in 1933, measuring the speeds of galaxies in the Coma Cluster ([Zwicky, 1933, *Helvetica Physica Acta* 6: 110](https://ui.adsabs.harvard.edu/abs/1933AcHPh...6..110Z)). The galaxies were moving too fast for the visible mass of the cluster to hold them. He coined the term *dunkle Materie* — dark matter — and most of the field shrugged for forty years. Rubin's data made the shrug indefensible. The rotation curves of individual galaxies, measured one by one, demanded mass that was not where the light was.

This chapter is about what that mass implies, where the light is, and how the layered architecture of the Milky Way and the morphological zoo of other galaxies both follow from physics we can reach with high-school calculus and a careful spectrum.

---

## Core concept

### The Milky Way: our own galaxy from inside

We live inside the thing we are trying to map. That makes the geometry hard. The Sun sits in the disk of the Milky Way, embedded in dust that absorbs visible light efficiently — a star 10,000 light-years away in the galactic plane is dimmed by a factor of hundreds before its light reaches us. William Herschel counted stars in 1785 and concluded the Sun was at the center of the system. He was looking at a roughly 6,000 light-year bubble inside a 100,000 light-year disk. The dust made the bubble look symmetric, and he made the obvious inference. He was wrong.

The correction came from objects that sit above the dust. In 1918, Harlow Shapley at Mount Wilson measured distances to 93 globular clusters — dense spherical assemblies of hundreds of thousands of old stars — using the period-luminosity relation of variable stars within them ([Shapley, 1918, *Astrophysical Journal* 48: 154](https://ui.adsabs.harvard.edu/abs/1918ApJ....48..154S)). The clusters did not surround us symmetrically. They formed a sphere centered roughly 26,000 light-years away in the direction of Sagittarius. The clusters orbit the Galaxy's center; the center of their distribution is the Galaxy's center. We are in the suburbs.

The modern picture, calibrated by the [Gaia DR3](https://www.cosmos.esa.int/web/gaia/dr3) data release in 2022 — a catalog of positions and motions for nearly two billion stars from the European Space Agency's Gaia satellite — is a layered system.

**The disk.** A flat structure about 100,000 light-years across, divided into a thin component (~1,000 light-years thick, where stars are forming now) and a thick component (~3,000 light-years, older stars on more disordered orbits). The Sun lives in the thin disk, about 26,000 light-years from the center, orbiting at roughly 220 km/s. One orbit takes about 225 million years — the Sun has completed something like twenty laps since the solar system formed.

**The bulge.** A peanut-shaped concentration of mostly old stars at the center, about 20,000 light-years across. The Milky Way is a *barred* spiral, with a linear stellar structure running through the bulge — a fact established only in the 1990s when infrared surveys could see through the dust ([Blitz & Spergel, 1991](https://ui.adsabs.harvard.edu/abs/1991ApJ...379..631B); confirmed by COBE/DIRBE and later by VVV survey data).

**Sgr A\*.** At the very center, a supermassive black hole of about $4 \times 10^6$ solar masses, occupying a region smaller than the orbit of Mercury. Two independent teams — Reinhard Genzel's at the Max Planck Institute and Andrea Ghez's at UCLA — tracked individual stars on highly elliptical orbits around this point for two decades using adaptive-optics infrared imaging, and applied Kepler's third law to weigh whatever sits in the center. The 2020 Nobel Prize in Physics went to Genzel and Ghez for this work. In May 2022 the Event Horizon Telescope released the first direct image of the shadow of Sgr A* ([EHT Collaboration, 2022](https://iopscience.iop.org/issue/2041-8205/930/2)), a ring of light bent around an object whose diameter matched the prediction from the stellar orbits to within a few percent.

**The halo and the dark matter halo.** Surrounding the disk, a roughly spherical cloud of old stars and globular clusters — the stellar halo, which Shapley used as his ruler. And surrounding everything, extending to at least 200,000 light-years, an invisible distribution of mass that we cannot see directly but whose gravity is what holds the disk's outer stars in their fast orbits. That last layer is what the rotation curve will force on us.

### Galaxy types and the Hubble sequence

Once Edwin Hubble showed in 1925 — using a Cepheid variable star in the Andromeda nebula and the period-luminosity relation Henrietta Leavitt had calibrated in 1912 ([Leavitt & Pickering, 1912](https://ui.adsabs.harvard.edu/abs/1912HarCi.173....1L)) — that "spiral nebulae" were actually other galaxies, the question shifted from *what are they* to *what kinds are there*. Hubble's answer ([Hubble, 1936, *The Realm of the Nebulae*](https://archive.org/details/realmofnebulae00edwi)) was the morphological classification still used today.

**Spirals (S).** A rotating disk with a central bulge and arms that wind outward. Subdivided Sa → Sb → Sc by the ratio of bulge to disk and how tightly wound the arms are. The Milky Way and Andromeda are roughly Sb. About two-thirds of nearby bright spirals also show a bar across the bulge (SBa, SBb, SBc).

The arms in a spiral are not stable structures of stars. They cannot be — the galaxy rotates differentially (inner stars orbit faster than outer ones), so any pattern of stars would wind up tighter and tighter and erase itself within a few rotations. Thirteen billion years should have flattened the arms long ago. The resolution, due to C.C. Lin and Frank Shu in 1964 ([Lin & Shu, 1964](https://ui.adsabs.harvard.edu/abs/1964ApJ...140..646L)), is that spiral arms are *density waves* — regions where the orbital density is momentarily higher, like a slow zone on a highway through which individual cars pass. Stars and gas drift in and out; the pattern persists. Gas compression in the wave triggers star formation, which is why the arms are outlined by young, hot, blue stars, even though most of the galaxy's mass is older and redder.

**Ellipticals (E).** Smooth, featureless ovoids ranging from nearly spherical (E0) to highly flattened (E7). No disk, no spiral arms, almost no dust or cold gas. The stars are old and red; star formation effectively shut off billions of years ago. Ellipticals span an enormous range in size, from dwarfs with a few million stars to giants with $10^{13}$ stars at the centers of galaxy clusters.

**Lenticulars (S0).** The "between" category — a disk with a central bulge but no spiral arms and little gas. They behave dynamically like spirals but look photometrically like ellipticals.

**Irregulars (Irr).** No organized symmetry. The Large and Small Magellanic Clouds, visible from the Southern Hemisphere as fuzzy patches, are the most famous examples — both are gravitationally distorted satellites of the Milky Way.

Hubble drew this as a tuning-fork diagram and (incorrectly) speculated it might be an evolutionary sequence. It isn't — galaxies do not generally migrate from one type to another by aging. But the morphology does encode dynamical history. Ellipticals are typically the products of major mergers, where the ordered rotation of two spirals is randomized into the velocity-dispersion-supported configuration of an elliptical. Spirals retain their disks because their assembly was gentler — gas accretion and minor mergers rather than head-on collisions.

The diversity is the point. Shape, color, gas content, and stellar population all correlate, because all of them are downstream of the same dynamical history.

### Rotation curves and dark matter

This is the chapter's deep dive. Everything else in the chapter is preparation for this one calculation.

Consider a star or gas cloud at radius $r$ from the center of a galaxy, moving in a circular orbit at speed $v$. For the orbit to be stable, the gravitational pull toward the center must exactly equal the centripetal acceleration the orbit requires:

$$\frac{G M(r)\, m}{r^2} = \frac{m v^2}{r}$$

The mass of the orbiting object $m$ cancels (it always does in gravity — Galileo's discovery, refined). What is left, solved for the mass enclosed within radius $r$:

$$M(r) = \frac{v^2 r}{G}$$

This is the master equation. It says: if you can measure how fast something is orbiting at a given radius, you have measured the total mass — every bit of it, visible or not — inside that radius. The mass doesn't have to glow. It doesn't have to be made of anything in particular. It just has to be there gravitating.

The reason this works cleanly is a result Newton proved called the *shell theorem*: a spherically symmetric distribution of mass acts, from outside it, exactly as if all its mass were concentrated at the center. Galaxy halos are roughly spherical, and the disk's contribution to gravity at large radius is well approximated by treating it spherically too. The math handles the geometry for us.

Now ask what a flat rotation curve implies.

If $v$ is constant — independent of $r$, all the way out — then $M(r) = v^2 r / G$ grows *linearly with radius*. Double the radius, you double the enclosed mass. Triple it, you triple the enclosed mass. The mass keeps piling on even where there is nothing visible to provide it.

The visible matter in a spiral galaxy does not behave like this. Out to where the disk is bright, the enclosed visible mass grows roughly with radius — there is light at all those radii. But once you pass the edge of the visible disk, the visible mass stops growing. If only the visible matter were doing the gravitating, the rotation curve would peak near the disk edge and then fall off as $v \propto 1/\sqrt{r}$ — Keplerian decline, the same scaling that makes Neptune orbit slower than Mercury.

Rubin's data refused to do that. The gas at 30,000 light-years from Andromeda's center moved as fast as the gas at 60,000 light-years, and faster than the visible mass alone could explain. For the rotation curve to be flat, mass had to keep accumulating outside the visible galaxy. A lot of it. The Milky Way's visible matter — stars, gas, dust, every photon-emitting object — totals about $10^{11}$ solar masses. The mass required to keep the outer rotation curve flat out to 200,000 light-years is closer to $10^{12}$ solar masses. Roughly ten times more matter than we can see, distributed in a roughly spherical halo that extends well past the disk.

This is dark matter. The name describes the only thing we know about it: it does not emit, absorb, or scatter electromagnetic radiation at any wavelength we have looked. Every probe of its presence is gravitational. We see its effects in:

- **Galaxy rotation curves**, as above ([Rubin & Ford 1970](https://ui.adsabs.harvard.edu/abs/1970ApJ...159..379R); confirmed in hundreds of galaxies since).
- **Galaxy cluster dynamics** — Zwicky's original 1933 observation, refined by velocity-dispersion measurements and X-ray maps of the hot intracluster gas. The gas temperature tells you how deep the gravitational potential is; the well is deeper than the visible mass can dig.
- **Gravitational lensing**, where the mass of a foreground galaxy or cluster bends the light of more distant galaxies behind it. The bending traces out a mass distribution that does not match the light distribution.
- **The Bullet Cluster** (1E 0657-558), where two galaxy clusters collided about 150 million years ago. The hot gas — most of the baryonic mass — was decelerated by the collision and now sits in the middle, between the two galaxy concentrations. Gravitational lensing maps show the *mass* still centered on the galaxies, not on the gas ([Clowe et al., 2006, *ApJ Letters* 648: L109](https://iopscience.iop.org/article/10.1086/508162)). The mass and the gas have spatially separated. Modified-gravity theories that put the gravitational source where the visible matter sits cannot explain this. Collisionless dark matter that passed through the collision intact, while the gas got stuck, can.
- **The cosmic microwave background**, where the relative heights of the acoustic peaks in the power spectrum pin down the total matter content vs. the baryonic content. The two differ by a factor of about five ([Planck Collaboration, 2020](https://www.aanda.org/articles/aa/full_html/2020/09/aa33910-18/aa33910-18.html)).

All these probes agree. The total matter content of the universe is roughly 31%; ordinary baryonic matter is roughly 5%; the rest is dark matter. The remaining 69% is dark energy, which we will meet in Chapter 13.

What dark matter *is* — what particle, what field, what new physics — we do not know. The leading candidates are weakly interacting massive particles (WIMPs), axions, and sterile neutrinos; underground detectors have been hunting WIMPs for thirty years without a confirmed detection, and the parameter space they could still hide in is shrinking each year. A few researchers (Mordehai Milgrom, beginning in 1983) have argued that the data should be explained by modifying gravity at low accelerations rather than by adding mass — Modified Newtonian Dynamics (MOND) — and MOND does fit individual rotation curves with one parameter where dark matter needs several. But MOND struggles with galaxy clusters and the Bullet Cluster, and has no relativistic extension that explains the cosmic microwave background. The current consensus, calibrated, uncertain, but firm: there is missing mass, and it is mass.

---

## Worked example: weighing the Milky Way out to the Sun's orbit

The Sun orbits the galactic center at $v = 220$ km/s, at radius $r = 26{,}000$ light-years. What total mass is enclosed inside the Sun's orbit?

Convert to SI:

- $v = 220 \times 10^3$ m/s $= 2.20 \times 10^5$ m/s.
- $r = 26{,}000$ ly $\times \, 9.46 \times 10^{15}$ m/ly $= 2.46 \times 10^{20}$ m.
- $G = 6.67 \times 10^{-11}$ N·m²/kg².

Apply $M = v^2 r / G$:

$$M = \frac{(2.20 \times 10^5)^2 \times (2.46 \times 10^{20})}{6.67 \times 10^{-11}}$$

$$M = \frac{4.84 \times 10^{10} \times 2.46 \times 10^{20}}{6.67 \times 10^{-11}} = \frac{1.19 \times 10^{31}}{6.67 \times 10^{-11}}$$

$$M \approx 1.79 \times 10^{41} \text{ kg}$$

In solar masses ($M_\odot = 1.99 \times 10^{30}$ kg):

$$M \approx \frac{1.79 \times 10^{41}}{1.99 \times 10^{30}} \approx 9.0 \times 10^{10} M_\odot$$

About 90 billion solar masses inside the Sun's orbit. This is in the right ballpark for the Milky Way's bulge plus the inner disk — consistent with what stellar counts plus dust-corrected luminosity give for the visible matter inside 26,000 light-years.

Now the punchline. Apply the same formula at $r = 200{,}000$ light-years, where 21-cm hydrogen observations and satellite-galaxy dynamics give roughly $v \approx 200$ km/s — essentially the same speed as the Sun's:

$$M(200{,}000 \text{ ly}) = \frac{(2.0 \times 10^5)^2 \times (1.89 \times 10^{21})}{6.67 \times 10^{-11}} \approx 1.1 \times 10^{42} \text{ kg} \approx 5.7 \times 10^{11} M_\odot$$

Roughly six times more mass enclosed at eight times the radius. The visible matter did not increase by anything like that factor between 26,000 and 200,000 light-years — the bright disk effectively ends by about 50,000 light-years. The extra few hundred billion solar masses are dark.

You have just done, with high-school algebra, the calculation Rubin's data forced on the field.

---

## Common misconceptions

- **"Dark matter is just unobserved normal matter — faint stars, cold gas, rogue planets."** It isn't. Big Bang nucleosynthesis predicts how much baryonic matter (protons and neutrons) the universe contains based on the observed abundances of deuterium, helium-3, helium-4, and lithium-7. The answer is about 5% of the critical density — only one-sixth of the total matter inferred from rotation curves and lensing. Whatever dark matter is, it is not protons and neutrons hiding in the dark. The microlensing surveys (MACHO, OGLE) also looked for compact baryonic objects in the halo and ruled out the regime where they could account for most of the missing mass ([Tisserand et al., 2007](https://www.aanda.org/articles/aa/full_html/2007/15/aa6017-06/aa6017-06.html)).
- **"The Milky Way is a typical spiral."** This one is mostly true, which is the interesting part. The Milky Way's mass, luminosity, and Hubble type (SBb-ish) are unremarkable for a bright local spiral. It is slightly more massive than median for galaxies of its size, and slightly metal-poor for its mass, but well within the normal scatter. We are not at a cosmic curiosity. We are a fair sample of one common kind of galaxy.
- **"We know what dark matter is — physicists just haven't detected it yet."** We don't. We know what it isn't: ordinary baryons, neutrinos (their mass is too small to account for the required density), or any particle in the Standard Model. We know roughly what it gravitates as — cold, collisionless, distributed in halos. The leading candidates are theoretical objects (WIMPs, axions) that physicists have *predicted* might exist for independent reasons. Forty years of increasingly sensitive direct-detection experiments have not confirmed any of them. It is reasonable to think dark matter exists. It is not reasonable, given current evidence, to claim we know what it is.
- **"Spiral arms are clumps of stars rotating with the galaxy."** They aren't. If they were, differential rotation would wind them up into invisibility within a few rotation periods. Spiral arms are density waves — patterns through which gas and stars flow. The pattern moves slowly; individual stars cycle through it. Bright young stars outline the wave because the compression triggers star formation there; the stars age and redden as they drift out of the arm.

---

## Exercises

**Warm-up (Understand).** The Milky Way has a thin disk, a thick disk, a bulge, a stellar halo, and a dark matter halo. (a) Which layer contains the Sun? (b) Which layer is most extended in radius? (c) Which layer contains the oldest stars? (d) Which layer is invisible at every wavelength so far observed?

**Application (Apply).** A globular cluster orbits the Milky Way at radius $r = 50{,}000$ light-years from the galactic center, with orbital speed $v = 210$ km/s. (a) Compute the mass enclosed inside the cluster's orbit. (b) Compare to your Worked Example value at 26,000 light-years. (c) By what factor did the enclosed mass grow, and by what factor did the radius grow? What does the ratio imply?

**Synthesis (Analyze).** You observe a galaxy whose hydrogen 21-cm rotation curve is flat at $v = 180$ km/s from $r = 5$ kpc all the way to $r = 25$ kpc. The visible disk ends at $r = 15$ kpc. (a) Compute the total enclosed mass at $r = 15$ kpc and at $r = 25$ kpc. (b) Compute the mass *between* 15 kpc and 25 kpc. (c) State in plain language what the answer to (b) implies, and identify which assumption — Newton's gravity, circular orbits, the shell theorem — would have to fail for an alternative explanation to work.

**Challenge (Analyze).** The Bullet Cluster shows gravitational lensing mass concentrated in two regions matching the galaxy distributions of two recently-collided clusters, while the X-ray-emitting hot gas (most of the baryonic mass) sits in between, decelerated by the collision. (a) Explain in two sentences why this spatial separation is hard to produce with modified-gravity theories (MOND) but natural with collisionless dark matter. (b) Identify one assumption about dark matter — beyond "it has mass" — that the Bullet Cluster tests. (c) Propose a different observation that would *fail* to confirm dark matter if the Bullet Cluster's interpretation is wrong.

---

## LLM Exercises

### Build the galaxy morphology + rotation curve simulator (`12-galaxies.html`)

With `CLAUDE.md` and `DESIGN.md` loaded:

> **Show.** A two-panel D3 v7 visualization. Left panel: a **galaxy morphology classifier** — three labeled buttons (Elliptical, Spiral, Irregular) that toggle a stylized face-on view. The spiral view shows a face-on Milky Way with bar, bulge, and two trailing arms; arrows show differential rotation (inner faster than outer). The elliptical view shows a smooth E4 oval with random stellar motions (no organized rotation). The irregular view shows a clumpy distribution with no symmetry. Right panel: a **rotation curve plot** — x-axis radius from 0 to 30 kpc, y-axis orbital speed from 0 to 300 km/s. Three curves overlaid: (1) "Visible matter prediction" — peaks near 5 kpc, falls as $1/\sqrt{r}$ beyond 15 kpc; (2) "Dark matter halo contribution" — rises and flattens; (3) "Observed" — the sum, flat at ~220 km/s. A slider controls the dark matter halo mass (0 to $10^{12} M_\odot$); when set to zero, the observed curve falls back to the visible-matter prediction.
>
> **Say.** Build it in D3 v7. For the rotation curve, use a simple two-component model: $v_{\text{visible}}(r) = v_0 \sqrt{r/r_d} \exp(-r/r_d)$ shape for an exponential disk peaking at $r_d \approx 5$ kpc, and $v_{\text{dark}}(r) = v_h \cdot r / \sqrt{r^2 + r_c^2}$ for an isothermal halo with core radius $r_c \approx 5$ kpc and asymptotic speed $v_h$. Plot $v_{\text{total}}(r) = \sqrt{v_{\text{visible}}^2 + v_{\text{dark}}^2}$. The slider scales $v_h$ from 0 to 220 km/s.
>
> **Constrain.** D3 v7 only. No external astronomy libraries. Filename: `12-galaxies.html`. Morphology panel switches instantly on button click. Rotation curve updates in real time as the dark matter slider moves.
>
> **Verify.** (a) Set the dark matter slider to zero and confirm the observed curve drops as $1/\sqrt{r}$ past 10 kpc. (b) Set it to 220 km/s and confirm the curve flattens out around 220 km/s past 15 kpc — matching the Milky Way's actual rotation curve. (c) Switch to the elliptical morphology view and confirm there is no organized rotation indicator.

### Exploration

- Slide the dark matter halo mass from 0 to maximum and watch the rotation curve transition from Keplerian decline to flat. At what halo mass does the curve first become flat (within 10%) out to 25 kpc?
- Switch between spiral and elliptical morphology. Notice that the elliptical's "rotation curve" panel is conceptually different — ellipticals are supported by random stellar motions, not ordered rotation, and their mass is inferred from velocity dispersion instead. Have the simulator clarify this when the user switches to elliptical view.
- Use the Bullet Cluster interpretation to motivate a thought experiment: what would the rotation curve of a galaxy look like immediately after a recent major collision that stripped its gas but not its dark matter? Can the simulator show this hypothetical state?

### Bridge to Chapter 13

> **Show.** I now know how to measure the mass of a galaxy from its rotation curve, classify galaxies by morphology, and reckon with the fact that most of the universe's matter is invisible. Time to ask the larger question: how did all of this — the galaxies, the dark matter halos, the visible web of structure — come to be at all?
>
> **Say.** Modify the simulator: add a third panel showing Hubble's 1929 velocity-distance plot. X-axis: distance in Mpc (0 to 2). Y-axis: recession velocity in km/s (0 to 1,200). Plot ~24 galaxies along a line with slope $H_0$ controlled by a slider from 50 to 100 km/s/Mpc. Show the modern value (~70) and the "Hubble tension" range (67–73) as a shaded band.
>
> **Verify.** At the modern $H_0 \approx 70$ km/s/Mpc, a galaxy at 1 Mpc recedes at ~70 km/s. At 1 Gpc it would recede at ~70,000 km/s, ~23% of the speed of light. The simulator should make clear that the relationship is between *space-stretching* and distance, not between motion and distance.

Save as `12b-hubble-law-preview.html`. Lead-in to Chapter 13 — *The Big Bang and the Expanding Universe*.

---

## What would change my mind

The dark matter case rests on the gravitational evidence — rotation curves, lensing, cluster dynamics, the Bullet Cluster, the CMB — agreeing across independent methods. Any one of these alone could be argued; the convergence is what makes the case. Two specific results would force a serious revision. **First**: a direct laboratory detection of a dark matter particle, in any of the underground experiments (XENONnT, LUX-ZEPLIN, ADMX, DARWIN) currently looking, would change "we don't know what it is" to "we know what it is." The current null results have ruled out large regions of the parameter space but not the whole space. **Second**: a successful relativistic extension of MOND that reproduces the cosmic microwave background acoustic peaks *and* fits the Bullet Cluster's mass-light separation without invoking dark matter would force me to take modified-gravity seriously as more than a fitting function for individual rotation curves. As of this writing, neither has happened; the parameter space for both has shrunk over the last decade. I will track them.

## Still puzzling

- *What is dark matter?* Not "what gravitational signature does it leave" — that we know. What particle, what field, what mechanism. After forty years of direct-detection experiments and an arsenal of theoretical candidates, the honest answer is we do not yet know. This is the largest known unknown in physics.
- *Why do spiral arms persist as cleanly as they do?* Density wave theory explains the kinematics — patterns that move at a different speed than individual stars — but the *amplitude* of real spiral arms, their long-term stability, and the interplay between density waves, gravitational instabilities, and gas dynamics is an active simulation problem. The arms we see are clearer and more long-lived than the simplest density-wave models predict.
- *How did dark matter halos and the galaxies inside them form together?* Structure formation simulations ([Illustris-TNG](https://www.tng-project.org/), [EAGLE](http://icc.dur.ac.uk/Eagle/)) reproduce the broad statistics of the galaxy population, but specific questions — why some halos host barred spirals and others don't, what sets the bulge-to-disk ratio, why the Milky Way has the specific satellite system it does — remain genuinely open.

---

**Tags:** Milky Way, galaxies, Hubble sequence, rotation curve, dark matter, Vera Rubin, Bullet Cluster, Sgr A*, spiral arms, galactic structure
